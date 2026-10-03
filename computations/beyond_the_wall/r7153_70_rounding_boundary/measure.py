"""r7153+70.1 (70) -- is a rounding-boundary verdict measurable?  Pre-registered at PREDICTION.md beside this file.

  python3 measure.py           # static census, then the dynamic margin on the receipts it selects (4 at a time)
  python3 measure.py --recall  # R3: the pre-r7153 P15_the_exact_transmission_ratios (136dd81f^), run the same way

An execution is ON-BOUNDARY when its margin is below 1e-3 of a unit in the decisive decimal.
"""
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RUNS = os.path.join(HERE, 'runs')
LINE = re.compile(r'\s*\[ROUNDING-BOUNDARY\]\[(ROUND|HALF-UNIT)\]\[n=([^\]]*)\]\s+(\S+?):(\d+):(\d+)\s+(.*)$')
ON = 1e-3
TIMEOUT = 1500


def census(files=None):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'mutate_assertions.py'), '--rounding-boundary']
                       + (['--files'] + files if files else []), cwd=ROOT, capture_output=True, text=True)
    sites = defaultdict(list)
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            form, n, p, l, c, text = m.groups()
            sites[p].append((int(l), int(c), form, n, text))
    return sites


def run_one(path, ss, tag=''):
    os.makedirs(RUNS, exist_ok=True)
    js = os.path.join(RUNS, tag + path.replace('/', '__') + '.json')
    t = time.time()
    try:
        p = subprocess.run([sys.executable, '-W', 'ignore', os.path.join(HERE, '_margin.py'), os.path.join(ROOT, path), js]
                           + [f'{l}:{c}' for l, c, *_ in ss], capture_output=True, text=True, timeout=TIMEOUT,
                           env=dict(os.environ, PYTHONUNBUFFERED='1', MPLBACKEND='Agg'))
        rc = p.returncode
    except subprocess.TimeoutExpired:
        rc = 'TIMEOUT'
    try:
        rec = json.load(open(js))
    except (OSError, ValueError):
        rec = {}
    return dict(path=path, rc=rc, s=round(time.time() - t, 1), rec=rec, sites=ss)


def report(results):
    on = []
    print(f'\n  {"site":<100} {"execs":>5} {"min margin (units)":>19}')
    for r in sorted(results, key=lambda r: r['path']):
        for l, c, form, n, text in r['sites']:
            ms = r['rec'].get(f'{l}:{c}', [])
            mm = min(ms) if ms else None
            flag = ' ⛔ ON-BOUNDARY' if mm is not None and mm < ON else ''
            if flag:
                on.append((r['path'], l, mm, text))
            print(f'  {os.path.basename(r["path"])[:80] + ":" + str(l):<100} {len(ms):>5} '
                  f'{"—" if mm is None else f"{mm:.2e}":>19}{flag}   rc={r["rc"]}')
    return on


def main():
    t0 = time.time()
    if '--recall' in sys.argv:
        src = subprocess.run(['git', 'show', '136dd81f^:receipts/P15_CR_cosmology/P15_the_exact_transmission_ratios_are_'
                              'recomputed_and_the_offset_saturates.py'], cwd=ROOT, capture_output=True, text=True).stdout
        tmp = 'receipts/P15_CR_cosmology/_r7153_recall_pre_repair.py'
        open(os.path.join(ROOT, tmp), 'w').write(src)
        try:
            sites = census([os.path.join(ROOT, tmp)])
            print(f'  RECALL: the pre-r7153 file carries {sum(len(v) for v in sites.values())} static site(s)')
            res = [run_one(tmp, sites[tmp], tag='recall__')]
        finally:
            os.remove(os.path.join(ROOT, tmp))
        on = report(res)
        print(f'\n  ON-BOUNDARY executions (margin < {ON}): {len(on)}')
        for p, l, mm, text in on:
            print(f'    line {l}: margin {mm:.2e} units  {text[:100]}')
        return
    sites = census()
    n = sum(len(v) for v in sites.values())
    print(f'  STATIC: {n} site(s) in {len(sites)} receipt(s)')
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(lambda p: run_one(p, sites[p]), sorted(sites)))
    print(f'  DYNAMIC: {len(res)} receipt(s) run in {time.time() - t0:.0f}s wall; rc 0: '
          f'{sum(r["rc"] == 0 for r in res)}; timeout: {sum(r["rc"] == "TIMEOUT" for r in res)}')
    on = report(res)
    reached = sum(1 for r in res for l, c, *_ in r['sites'] if r['rec'].get(f'{l}:{c}'))
    print(f'\n  sites reached at run time: {reached} of {n}')
    print(f'  ON-BOUNDARY executions (margin < {ON} of a unit): {len(on)}')
    for p, l, mm, text in on:
        print(f'    {p}:{l}  margin {mm:.2e}  {text[:100]}')


if __name__ == '__main__':
    main()
