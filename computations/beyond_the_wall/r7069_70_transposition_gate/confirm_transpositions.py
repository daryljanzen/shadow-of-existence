"""On-demand companion to corpus/check_marker_transposition.py (r7069+70).

The gate reads SOURCE only.  For every baseline line adjudicated as a TRANSPOSITION candidate, this
script RUNS the own group's receipts and the carrier, and reports whether each run's OUTPUT carries the
number -- the case the gate cannot see (a number a receipt prints and never writes).

A transposition is confirmed when the carrier's output or source carries the number and no own-group
output does.  Not a registered receipt: the carriers include CAMB runs of up to ~25 minutes, so it is run
by hand and its log is committed beside it (confirm_log.txt).

Usage:  python3 confirm_transpositions.py [--jobs N]
"""
import glob
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7043_70_citation_sweep'))
import check_marker_transposition as G      # noqa: E402
import trace_citations as T                 # noqa: E402

IDX = {}
for d in ('storyboard_receipts', 'receipts'):
    for p in glob.glob(os.path.join(ROOT, d, '**', '*.py'), recursive=True):
        IDX[os.path.basename(p)[:-3]] = p


def run(name):
    p = IDX[name]
    try:
        r = subprocess.run([sys.executable, os.path.basename(p)], cwd=os.path.dirname(p),
                           capture_output=True, text=True, timeout=1800)
        return r.returncode, (r.stdout + r.stderr).replace('−', '-')
    except subprocess.TimeoutExpired:
        return 'timeout', ''


def out_carries(txt, tok):
    if '/' in tok:
        a, b = tok.lstrip('-').split('/')
        val = int(a) / int(b) * (-1 if tok.startswith('-') else 1)
        vals = [float(x) for x in re.findall(r'-?\d+\.\d+|-?\d+', txt) if len(x) < 30]
        return G.carries(txt, tok) or any(abs(v - val) < 1e-9 for v in vals)
    vals = set()
    for s in T.num_pool(txt):
        try:
            vals.add(float(s))
        except ValueError:
            pass
    return T.matches(tok, vals)


def main():
    jobs = int(sys.argv[sys.argv.index('--jobs') + 1]) if '--jobs' in sys.argv else 4
    lines = [l.rstrip('\n').split('\t') for l in open(G.BASE, encoding='utf-8')
             if l.strip() and not l.startswith('#')]
    cands = [l for l in lines if l[4].startswith('TRANSPOSITION')]
    names = sorted({n for l in cands for n in l[1].split('+') + [l[3]]})
    with ThreadPoolExecutor(jobs) as ex:
        outs = dict(zip(names, ex.map(run, names)))
    ok = True
    for paper, own, tok, car, *_ in cands:
        own_hits = [n for n in own.split('+') if out_carries(outs[n][1], tok)]
        car_hit = out_carries(outs[car][1], tok) or G.carries(G.unquoted(open(IDX[car]).read()), tok)
        verdict = 'CONFIRMED' if car_hit and not own_hits else 'NOT CONFIRMED'
        ok &= verdict == 'CONFIRMED'
        print(f'{verdict:14s} {paper:26s} {tok:9s} carrier rc={outs[car][0]} carries={car_hit}  '
              f'own rc={[outs[n][0] for n in own.split("+")]} carries={own_hits or "none"}  | {car[:60]}')
    print('\nALL CONFIRMED' if ok else '\nSOME NOT CONFIRMED -- re-adjudicate those lines')


if __name__ == '__main__':
    main()
