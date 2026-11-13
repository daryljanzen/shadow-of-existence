"""E8 runner: one multi-turn session per subject (stream-json, with harness/subject.py's isolation), then blind per-turn
scoring with E1/E2/E3's own scorers.  Usage:  python3 run_e8.py pilot|main [--workers N] [--score-only]
  pilot: 2 sessions per arm (orders A and B); main: 16 per arm (A/B alternating by session index).
A session is the unit: it is complete when its last turn is recorded; an incomplete session is run again from the start
(its context cannot be resumed).  The pause switch (/tmp/ARP_PAUSE) is checked before each session starts."""
import importlib.util, json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(EXP)))
sys.path.insert(0, os.path.join(EXP, 'harness'))
from subject import Trial, run_batch, PAUSE_FILE, USAGE_LEDGER, _clean_env  # noqa: E402

def _mod(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
R1, R2, R3 = (_mod(f'run_e{k}', os.path.join(EXP, f'E{k}', f'run_e{k}.py')) for k in (1, 2, 3))
MODEL = 'claude-opus-5-5'; SYS = 'You are a helpful assistant.'; ARMS = ('IMPLICIT', 'REMINDER', 'PLAIN')
S = json.load(open(os.path.join(HERE, 'materials', 'sessions.json')))
REMINDER = open(os.path.join(HERE, 'materials', 'reminder.md')).read().strip()
ITEMS = {i['id']: i for k in (1, 2, 3) for i in json.load(open(os.path.join(EXP, f'E{k}', 'materials', 'items.json')))}

def task_text(iid):
    it = ITEMS[iid]
    return it['message'] if iid.startswith('E1') else it['prompt'] if iid.startswith('E2') else R3.message('C1', it)

def spin_up():
    return [f"Please read this carefully:\n\n<document>\n{open(os.path.join(ROOT, p) if p.endswith('.tex') else os.path.join(EXP, p)).read()}\n</document>"
            for p in S['spin_up']]

def session_plan(arm, idx):
    order = S['order_A'] if idx % 2 == 0 else S['order_B']
    turns = [('spin', f'doc{j + 1}', t) for j, t in enumerate(spin_up())] if arm != 'PLAIN' else []
    for k, iid in enumerate(order, 1):
        t = task_text(iid)
        turns.append(('task', iid, (REMINDER + '\n\n---\n\n' + t) if arm == 'REMINDER' else t))
    return order, turns

def run_session(arm, idx, base, timeout=900):
    d = os.path.join(base, arm, f's{idx:02d}'); order, turns = session_plan(arm, idx)
    if os.path.exists(os.path.join(d, 'turn24.json')):
        return 'done'
    if os.path.exists(PAUSE_FILE):
        return 'paused'
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    cwd = tempfile.mkdtemp(prefix='subj_', dir='/tmp')
    p = subprocess.Popen(['claude', '-p', '--setting-sources', '', '--strict-mcp-config', '--no-session-persistence', '--tools', '',
                          '--model', MODEL, '--system-prompt', SYS, '--input-format', 'stream-json', '--output-format', 'stream-json',
                          '--verbose'], cwd=cwd, env=_clean_env(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL, text=True, bufsize=1)
    prev, k = 0.0, 0
    try:
        for n, (kind, iid, text) in enumerate(turns, 1):
            t0 = time.time(); started = datetime.now(timezone.utc).isoformat()
            p.stdin.write(json.dumps({'type': 'user', 'message': {'role': 'user', 'content': text}}) + '\n'); p.stdin.flush()
            while True:
                line = p.stdout.readline()
                if not line:
                    raise RuntimeError(f'session ended at turn {n}')
                ev = json.loads(line)
                if ev.get('type') == 'result':
                    break
                if time.time() - t0 > timeout:
                    raise RuntimeError(f'turn {n} timed out')
            if ev.get('is_error'):
                raise RuntimeError(f'turn {n}: {str(ev.get("result"))[:300]}')
            cost = (ev.get('total_cost_usd') or 0) - prev; prev = ev.get('total_cost_usd') or prev
            rec = dict(exp='E8', arm=arm, session=idx, order='A' if idx % 2 == 0 else 'B', turn_index=n, kind=kind, item=iid,
                       model=MODEL, system=SYS, message=text, response=ev.get('result', ''), usage=ev.get('usage'),
                       cost_usd_list=cost, started=started, wall_s=round(time.time() - t0, 2))
            if kind == 'task':
                k += 1; rec['task_index'] = k
                json.dump(rec, open(os.path.join(d, f'turn{k}.json.part'), 'w'), indent=1, ensure_ascii=False)
                os.replace(os.path.join(d, f'turn{k}.json.part'), os.path.join(d, f'turn{k}.json'))
            else:
                json.dump(rec, open(os.path.join(d, f'{iid}.json'), 'w'), indent=1, ensure_ascii=False)
            u = ev.get('usage') or {}
            with open(USAGE_LEDGER, 'a') as f:
                f.write('\t'.join(str(x) for x in (started, 'E8', arm, f's{idx:02d}:{n}:{iid}', 'subject', MODEL,
                        u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0),
                        u.get('output_tokens', 0), cost, 0)) + '\n')
        return 'done'
    except Exception as e:  # noqa: BLE001 -- the session is left incomplete and re-run from the start next time
        open(os.path.join(d, 'FAILED.txt'), 'w').write(repr(e)[:1000]); return 'failed'
    finally:
        try:
            p.stdin.close(); p.wait(timeout=60)
        except Exception:  # noqa: BLE001
            p.kill()
        shutil.rmtree(cwd, ignore_errors=True)

def strip(t):
    return R1.strip_receipt(t)

def score(base, sbase):
    sc = []
    for arm in ARMS:
        for sd in sorted(glob_dirs(os.path.join(base, arm))):
            for k in range(1, 25):
                f = os.path.join(sd, f'turn{k}.json')
                if not os.path.exists(f):
                    continue
                r = json.load(open(f)); iid = r['item']; it = ITEMS[iid]; ans = r['response']
                tag = f"{os.path.basename(sd)}_t{k:02d}_{iid}"     # the scorer's input carries neither arm, session nor turn
                out = lambda kind: os.path.join(sbase, kind, arm, tag + '.json')  # noqa: E731
                if iid.startswith('E1'):
                    asks = '\n'.join(f"{a['k']}. {a['text']}" + (f"  KEY: {it['hard_key']}" if a['hard'] else '') for a in it['asks'])
                    sc.append(Trial('E8', arm, tag, R1.SCORER, f"MESSAGE:\n{it['message']}\n\nREQUESTS:\n{asks}\n\nANSWER:\n{strip(ans)}", out('E1'), role='scorer'))
                elif iid.startswith('E2'):
                    msg = f"SITUATION:\n{it['prompt']}\n\nCLAIM:\n{it['claim']}\n\nRESPONSE:\n{ans}"
                    sc.append(Trial('E8', arm, tag, R2.SCORER, msg, out('E2'), role='scorer'))
                    if it['kind'] == 'open':
                        sc.append(Trial('E8', arm, tag, R2.SCORER_OPEN, msg, out('E2open'), role='scorer'))
                else:
                    key = '\n'.join(f"{fl['f']}. [{fl['type']}] at: \"{fl['location']}\" -- {fl['description']}" for fl in it['flaws'])
                    sc.append(Trial('E8', arm, tag, R3.SCORER, f"DOCUMENT:\n{it['document']}\n\nKEY (three known flaws):\n{key}\n\nREVIEW:\n{ans}", out('E3'), role='scorer'))
    run_batch(sc, workers=4, model=MODEL)

def glob_dirs(p):
    return [os.path.join(p, x) for x in os.listdir(p)] if os.path.isdir(p) else []

def main():
    phase = sys.argv[1]; workers = int(sys.argv[sys.argv.index('--workers') + 1]) if '--workers' in sys.argv else 4
    n = 2 if phase == 'pilot' else 16; base = os.path.join(HERE, 'runs_' + phase); sbase = os.path.join(HERE, 'scores_' + phase)
    if '--score-only' not in sys.argv:
        jobs = [(a, i) for i in range(n) for a in ARMS]
        with ThreadPoolExecutor(workers) as ex:
            res = list(ex.map(lambda j: run_session(*j, base), jobs))
        print({s: res.count(s) for s in set(res)})
    score(base, sbase)

if __name__ == '__main__':
    main()
