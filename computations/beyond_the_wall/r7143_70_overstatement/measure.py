"""r7143+70.1 (70) -- how much do the corpus's `N of N checks pass` headlines overstate what was verified?
Pre-registered at PREDICTION.md beside this file.  Runs every registered receipt once through `_counted.py`,
four at a time, from its own directory; edits nothing.

  python3 measure.py            # the full run (writes runs/*.json and measure_log.txt's body to stdout)
  python3 measure.py --report   # aggregate the runs already on disk
"""
import ast
import glob
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RUNS = os.path.join(HERE, 'runs')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
sys.path.append(os.path.join(ROOT, 'corpus'))
import mutate_assertions as MA      # noqa: E402
import run_all_receipts as RA       # noqa: E402

NOT_OWED = {'CONSTANT', 'NOT-A-DEFECT', 'UBIQUITOUS-ARM'}
LINE = re.compile(r'\s*\[CANNOT-FAIL\]\[(T\w+) [^\]]*\]\s+(\S+?):(\d+):(\d+)\s+(.*)$')
TIMEOUT = 1500


def owed_sites():
    """live instrument sites whose baseline verdict is owed: {receipt: [(line, col, cls, text)]}"""
    verdict = {}
    for ln in open(os.path.join(ROOT, 'corpus', 'cannot_fail_baseline.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if ln.startswith('#') or len(p) < 5:
            continue
        verdict[(p[0], p[1], p[2])] = p[4]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'mutate_assertions.py'), '--cannot-fail'],
                       cwd=ROOT, capture_output=True, text=True)
    out = defaultdict(list)
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            cls, p, l, c, text = m.groups()
            v = verdict.get((p, cls, ' '.join(text.split())))
            if v is None:
                sys.exit(f'site not in the baseline: {ln}')
            if v not in NOT_OWED:
                out[p].append((int(l), int(c), cls, v, text))
    return out


def helper_span(path, line, col):
    """(lo, hi) of the innermost Name-called Call with >= 2 args containing the site, else None"""
    tree = ast.parse(open(os.path.join(ROOT, path), encoding='utf-8').read())
    best = None
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and len(n.args) >= 2
                and (n.lineno, n.col_offset) <= (line, col) <= (n.end_lineno, n.end_col_offset)):
            if best is None or (n.lineno, n.col_offset) >= (best.lineno, best.col_offset):
                best = n
    return None if best is None else (best.lineno, best.end_lineno)


def run_one(path, spans):
    key = path.replace('/', '__')
    js, log = os.path.join(RUNS, key + '.json'), os.path.join(RUNS, key + '.out')
    t = time.time()
    try:
        p = subprocess.run([sys.executable, '-W', 'ignore', os.path.join(HERE, '_counted.py'), os.path.join(ROOT, path),
                            js] + [f'{a}:{b}' for a, b in spans], capture_output=True, text=True, timeout=TIMEOUT,
                           env=dict(os.environ, PYTHONUNBUFFERED='1', MPLBACKEND='Agg'))
        rc, so = p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired as e:
        rc, so = 'TIMEOUT', (e.stdout or b'').decode('utf-8', 'replace') if isinstance(e.stdout, bytes) else (e.stdout or '')
    open(log, 'w', encoding='utf-8').write(so[-20000:])
    meta = dict(path=path, rc=rc, s=round(time.time() - t, 1), spans=spans)
    try:
        meta.update(json.load(open(js)))
    except (OSError, ValueError):
        meta['N'] = None
    json.dump(meta, open(js, 'w'))
    return meta


HEADLINE = [re.compile(p) for p in (r'(\d+)\s+checks?,\s+(\d+)\s+pass', r'(\d+)\s*/\s*(\d+)\s+(?:checks?\s+)?pass',
                                     r'(\d+)\s+of\s+(\d+)\s+(?:checks?\s+)?pass', r'all\s+(\d+)\s+checks?\s+pass', r'on\s+all\s+(\d+)\s+checks')]


def headline(text):
    """the LAST printed `N of N`-type headline: its denominator, or None"""
    best = None
    for rx in HEADLINE:
        for m in rx.finditer(text):
            g = [int(x) for x in m.groups()]
            best = (m.start(), max(g))
    return None if best is None else best[1]


def report(sites):
    rows = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(RUNS, '*.json')))]
    ran = len(rows)
    cov = [r for r in rows if r.get('N')]
    print(f'\n  RECEIPTS RUN: {ran}   rc 0: {sum(r["rc"] == 0 for r in rows)}   '
          f'timeout: {sum(r["rc"] == "TIMEOUT" for r in rows)}   other rc: '
          f'{dict(Counter(str(r["rc"]) for r in rows if r["rc"] not in (0, "TIMEOUT")))}')
    print(f'  COVERED (N > 0 under the wrapper): {len(cov)} of {ran} = {100 * len(cov) / ran:.1f} %')
    sumN = sum(r['N'] for r in cov)
    k_of = {r['path']: sum(r.get('span', [])) for r in rows}
    sumk = sum(k_of[r['path']] for r in cov)
    print(f'\n  ΣN = {sumN} executed verdicts;  Σk = {sumk} of them at owed cannot-fail sites')
    print(f'  ⇒ CORPUS-WIDE DYNAMIC OVERSTATEMENT  Σk/ΣN = {100 * sumk / sumN:.3f} %')

    # headline agreement: does N equal the receipt's own printed denominator?
    agree = tot = 0
    for r in cov:
        # the printed headline if there is one, else the one the receipt's own text states (`rc=0 on all 34 checks`)
        h = headline(open(os.path.join(RUNS, r['path'].replace('/', '__') + '.out'), encoding='utf-8').read())
        if h is None:
            h = headline(open(os.path.join(ROOT, r['path']), encoding='utf-8', errors='replace').read())
        if h is not None:
            tot += 1
            agree += h == r['N']
    print(f'  wrapper N against the receipt\'s own printed headline: {agree} of {tot} headlines agree exactly')

    # static
    sv = 0
    for f in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True):
        try:
            src = open(f, encoding='utf-8', errors='replace').read()
            tree = ast.parse(src)
        except SyntaxError:
            continue
        _a, fns = MA._defs(tree)
        sv += len(MA._verdicts(tree, fns, src))
    so = sum(len(v) for v in sites.values())
    print(f'  STATIC: {so} owed sites / {sv} verdict sites (`_verdicts`, every receipt) = {100 * so / sv:.3f} %')

    print('\n  PER RECEIPT CARRYING OWED SITES -- k of N, and what the headline honestly reads')
    per = []
    by = {r['path']: r for r in rows}
    for p, ss in sorted(sites.items()):
        r = by.get(p)
        if r is None:
            print(f'    [NOT RUN -- not registered] {p}  ({len(ss)} site(s))')
            continue
        N, k = r.get('N'), k_of[p]
        if not N:
            print(f'    [NOT COVERED rc={r["rc"]}] {p}')
            continue
        per.append((k / N, k, N, p))
    for f, k, N, p in sorted(per, reverse=True):
        print(f'    {100 * f:5.1f} %   {k:2d} of {N:4d}  -> honestly {N - k} of {N}   {os.path.basename(p)[:90]}')
    fr = sorted(x[0] for x in per)
    if fr:
        med = fr[len(fr) // 2] if len(fr) % 2 else (fr[len(fr) // 2 - 1] + fr[len(fr) // 2]) / 2
        print(f'\n  over {len(fr)} receipts: median {100 * med:.1f} %, max {100 * fr[-1]:.1f} %, min {100 * fr[0]:.1f} %')

    print('\n  OWED SITES OUTSIDE ANY HELPER CALL (counted in neither N nor k):')
    for p, ss in sorted(sites.items()):
        for l, c, cls, v, text in ss:
            if helper_span(p, l, c) is None:
                print(f'    {p}:{l}  {cls} {v}  {text[:80]}')
    print('\n  SPANS NOT EXECUTED (k = 0 at a site inside a helper call):')
    for r in rows:
        for (lo, hi), n in zip(r.get('spans', []), r.get('span', [])):
            if n == 0:
                print(f'    {r["path"]}:{lo}-{hi}  rc={r["rc"]}')
    return sumk, sumN


def main():
    sites = owed_sites()
    if '--report' not in sys.argv:
        os.makedirs(RUNS, exist_ok=True)
        files, unresolved = RA.registered()
        files = [os.path.relpath(f, ROOT) for f in files if f.endswith('.py')]
        exp = RA.expected_seconds() or {}
        files.sort(key=lambda f: -(exp.get(f) or 0))
        spans = {}
        for p, ss in sites.items():
            sp = sorted({helper_span(p, l, c) for l, c, *_ in ss} - {None})
            spans[p] = sp
        missing = sorted(set(sites) - set(files))
        print(f'  registered .py receipts: {len(files)};  unresolved rows: {len(unresolved)};  '
              f'owed-site receipts not registered: {missing}')
        files += missing
        t0 = time.time()
        with ThreadPoolExecutor(4) as ex:
            for i, m in enumerate(ex.map(lambda f: run_one(f, spans.get(f, [])), files)):
                if i % 50 == 0:
                    print(f'    {i} / {len(files)}  {time.time() - t0:.0f}s', flush=True)
        print(f'  wall {time.time() - t0:.0f}s')
    report(sites)


if __name__ == '__main__':
    main()
