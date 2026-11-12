"""One clean model trial per call, recorded in full.  Shared by E1-E8.

Each trial runs in its own new directory under /tmp, never under the repository or this seat's scratchpad
(whose path names the repository: SUBJECT_ROUTE_PROBE.md).  The session has no setting sources, no MCP
servers, no tools, no persistence and a one-line system prompt; the variables that carry extra CLAUDE.md
directories and the account email are removed.  What still reaches a subject, identically in every condition,
is recorded in SUBJECT_ROUTE_PROBE.md.

Every trial writes one JSON record: experiment, condition, item, model, UTC timestamp, the exact system prompt
and message, the full response, usage and timing.  A record that exists is never re-run, so a batch resumes
where it stopped.

    from subject import Trial, run_batch
    run_batch([Trial(exp, cond, item_id, system, message, out_path), ...], workers=4, model='claude-opus-5-5')
"""
import json
import os
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

DROP_ENV = ('CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD', 'CLAUDE_ADDITIONAL_DIRECTORIES',
            'CLAUDE_CODE_USER_EMAIL')
DEFAULT_MODEL = 'claude-opus-5-5'
# Daryl's usage rule (2026-11-12): pause when his overall usage nears 90%, so he can keep working until the weekly
# reset.  This seat cannot read his usage meter, so the run is made pausable: a trial does not start while
# PAUSE_FILE exists, and every finished trial appends its tokens and list-price cost to the usage ledger, which is
# reported after each batch.  Records already written are kept, so a paused batch resumes where it stopped.
PAUSE_FILE = '/tmp/ARP_PAUSE'
USAGE_LEDGER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'USAGE.tsv')


class Paused(Exception):
    pass


@dataclass
class Trial:
    exp: str
    cond: str
    item: str
    system: str
    message: str
    out: str               # path of the JSON record
    role: str = 'subject'  # 'subject' or 'scorer'
    rep: int = 0


def _clean_env():
    env = dict(os.environ)
    for k in DROP_ENV:
        env.pop(k, None)
    return env


def run_one(t: Trial, model: str = DEFAULT_MODEL, timeout: int = 600, retries: int = 2):
    if os.path.exists(t.out):
        return json.load(open(t.out))
    if os.path.exists(PAUSE_FILE):
        raise Paused(t.out)
    os.makedirs(os.path.dirname(t.out), exist_ok=True)
    rec = dict(asdict(t), model=model, started=datetime.now(timezone.utc).isoformat())
    for attempt in range(retries + 1):
        d = tempfile.mkdtemp(prefix='subj_', dir='/tmp')
        t0 = time.time()
        try:
            p = subprocess.run(
                ['claude', '-p', '--setting-sources', '', '--strict-mcp-config', '--no-session-persistence',
                 '--tools', '', '--model', model, '--system-prompt', t.system, '--output-format', 'json',
                 t.message],
                cwd=d, env=_clean_env(), capture_output=True, text=True, timeout=timeout)
            out = json.loads(p.stdout)
            if out.get('is_error'):
                raise RuntimeError(out.get('result'))
            rec.update(response=out.get('result', ''), usage=out.get('usage'),
                       cost_usd_list=out.get('total_cost_usd'), duration_ms=out.get('duration_ms'),
                       wall_s=round(time.time() - t0, 2), attempt=attempt)
            break
        except Exception as e:                       # noqa: BLE001 -- recorded, then retried
            rec['error_' + str(attempt)] = repr(e)[:500]
            time.sleep(5 * (attempt + 1))
        finally:
            shutil.rmtree(d, ignore_errors=True)
    else:
        rec['failed'] = True
    tmp = t.out + '.part'
    json.dump(rec, open(tmp, 'w'), indent=1, ensure_ascii=False)
    os.replace(tmp, t.out)
    u = rec.get('usage') or {}
    with open(USAGE_LEDGER, 'a') as f:
        f.write('\t'.join(str(x) for x in (
            rec['started'], t.exp, t.cond, t.item, t.role, model,
            u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0),
            u.get('output_tokens', 0), rec.get('cost_usd_list', 0), int(bool(rec.get('failed'))))) + '\n')
    return rec


def run_batch(trials, workers: int = 4, model: str = DEFAULT_MODEL):
    """runs what is not yet recorded; stops cleanly (keeping every finished record) once PAUSE_FILE appears"""
    def one(t):
        try:
            return run_one(t, model)
        except Paused:
            return None
    with ThreadPoolExecutor(workers) as ex:
        recs = list(ex.map(one, trials))
    done = [r for r in recs if r is not None]
    bad = [r for r in done if r.get('failed')]
    cost = sum(r.get('cost_usd_list') or 0 for r in done)
    print(f'  {len(done)} of {len(trials)} trials recorded, {len(bad)} failed after retries, '
          f'{len(trials) - len(done)} held by PAUSE; this batch about ${cost:.2f} at list price')
    return done
