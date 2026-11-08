#!/usr/bin/env python3
"""r7705+70 item 1 gate: the harness `_RUN` before the guard (the receipt at PRE, from git) and after it (the working
tree), on every rederive_lowell_sweep CASE, the four (L) rows, FROZEN (L) NS3 1800/2400 at the distances point, and the
positive control FROZEN (L) NS3 3600. RESULT lines compared byte for byte. Writes gate_guard.json."""
import ast, importlib.util, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..')); PRE = sys.argv[1] if len(sys.argv) > 1 else '2fdd39190'
RREL = 'receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py'
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s); _s.loader.exec_module(rl)
ns = rl.engine()


def run_src(src):
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) == '_RUN' for t in n.targets):
            return ast.literal_eval(n.value)


RUN = {'pre': run_src(subprocess.run(['git', 'show', f'{PRE}:{RREL}'], cwd=ROOT, capture_output=True, text=True).stdout),
       'post': run_src(open(os.path.join(ROOT, RREL)).read())}
assert RUN['pre'] != RUN['post'] and RUN['post'] == ns['_RUN'], 'the engine must read the edited harness'
REFIT = ((68.570730, 0.291246), {'OBF': f'{0.021643 / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}'})
DIST = ((68.60, 0.2973), {})
BG = {'CTL': (ns['CTL'], {}), 'ADJ': (ns['ADJ'], {})}
CASES = {k: (w, env) for k, w, env in rl.CASES}
F, D = CASES['FROZEN_adjudicated_KLO_0_1'][1], CASES['DECOUPLED_adjudicated_KLO_0_1_NS3_60000'][1]
JOBS = {f'CASE__{k}': (BG[w], env) for k, (w, env) in CASES.items()}
JOBS.update({f'{p}__{b}__L': (pt, dict(env, SPLITCLOCK='L')) for p, pt in (('refit', REFIT), ('distances', DIST))
             for b, env in (('frozen', F), ('decoupled', D))})
JOBS.update({f'distances__frozen__L__NS3_{n}': (DIST, dict(F, SPLITCLOCK='L', NS3=n)) for n in (1800, 2400, 3600)})
for (bg, _), _e in JOBS.values():
    ns['R0'].setdefault(bg, ns['r0_of'](*bg))


def one(arg):
    key, which = arg; (bg, extra), env = JOBS[key]
    e = dict(os.environ, BH0=f"{bg[0]}", BOM=f"{bg[1]}", BR0=f"{ns['R0'][bg]:.10f}", HIER_DIR=ns['HIER_DIR'])
    for k in ('ZEND', 'ZDEC', 'NTAU', 'KLO', 'NLOW', 'NS3', 'HKCAP', 'SPLITCLOCK'):
        e.pop(k, None)
    e.update({k: str(v) for k, v in dict(env, **extra).items()})
    p = subprocess.run([sys.executable, '-c', RUN[which]], env=e, capture_output=True, text=True)
    line = next((l for l in p.stdout.splitlines() if l.startswith('RESULT')), (p.stdout + p.stderr)[-200:])
    print(which, key, line[:90], flush=True)
    return (key, which), line


with ThreadPoolExecutor(int(os.environ.get('GATE_WORKERS', '3'))) as ex:
    got = dict(ex.map(one, [(k, w) for k in JOBS for w in ('pre', 'post')]))
out = {k: dict(pre=got[(k, 'pre')], post=got[(k, 'post')], identical=got[(k, 'pre')] == got[(k, 'post')]) for k in JOBS}
ctl = 'distances__frozen__L__NS3_3600'
summary = dict(n=len(JOBS), identical=sum(v['identical'] for k, v in out.items() if k != ctl),
               of=len(JOBS) - 1, control_pre=out[ctl]['pre'][:60], control_post=out[ctl]['post'][:90],
               control_ok=out[ctl]['pre'].startswith('RESULT 1.000000') and out[ctl]['post'].startswith('RESULT NONFINITE'))
summary['PASS'] = summary['identical'] == summary['of'] and summary['control_ok']
json.dump(dict(summary=summary, runs=out, pre=PRE), open(os.path.join(HERE, 'gate_guard.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))
