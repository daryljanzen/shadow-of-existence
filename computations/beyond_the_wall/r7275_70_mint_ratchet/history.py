#!/usr/bin/env python3
"""r7275+70.1 ①: the three ratchet shapes against the last 200 first-parent commits on origin/main."""
import collections, json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
UNV = ('UNADJUDICATED', 'UNADJUDICATED-LIST', 'UNADJUDICATED-PINNED')
P = 'corpus/quote_pin_baseline.tsv'

def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout

def rows(rev):
    out = {}
    for ln in git('show', f'{rev}:{P}').split('\n'):
        q = ln.split('\t')
        if len(q) >= 6 and not ln.startswith('#'):
            try:
                out[(q[0], json.loads(q[1]))] = q[5]
            except ValueError:
                pass
    return out

def judge(a, b):
    """a = parent rows, b = child rows -> dict of facts"""
    ua = {k: v for k, v in a.items() if v in UNV}
    ub = {k: v for k, v in b.items() if v in UNV}
    minted = {k: v for k, v in ub.items() if k not in a}
    retired = {k for k in ua if k not in b}
    per_a = collections.Counter(k[0] for k in ua); per_b = collections.Counter(k[0] for k in ub)
    rk = collections.Counter(k[0] for k in retired)
    v2 = [k for k in minted if rk[k[0]] == 0]
    rises = [r for r in per_b if per_b[r] > per_a[r]]
    return dict(minted=minted, v1=bool(minted), v2=bool(v2), v2keys=v2, v3=bool(rises), rises=rises,
                delta=len(ub) - len(ua), cls=collections.Counter(minted.values()))

if __name__ == '__main__':
    revs = git('rev-list', '--first-parent', '-n', '200', 'origin/main').split()
    touch = []
    for c in revs:
        if not git('diff', '--name-only', f'{c}^', c, '--', P).strip():
            continue
        j = judge(rows(f'{c}^'), rows(c))
        j['sha'] = c[:8]; j['subj'] = git('log', '-1', '--format=%s', c)[:70]
        touch.append(j)
    print(f'M-a commits touching the baseline: {len(touch)} of {len(revs)}')
    for s in ('v1', 'v2', 'v3'):
        ref = [t for t in touch if t[s]]
        low = [t for t in ref if t['delta'] < 0]
        print(f'{s.upper()}: refuses {len(ref)} ({100*len(ref)/max(1,len(touch)):.0f}% of touching); of them '
              f'{len(low)} LOWERED the unadjudicated total: {[t["sha"] for t in low]}')
    big = max(touch, key=lambda t: len(t['minted']))
    print(f'M-f largest single-commit mint: {len(big["minted"])} keys at {big["sha"]} {big["subj"]}')
    cls = collections.Counter()
    for t in touch:
        cls.update(t['cls'])
    print('minted keys by class over the window:', dict(cls))
    print()
    for t in touch:
        if t['v1'] or t['v3']:
            print(f'  {t["sha"]} d={t["delta"]:+5d} minted={len(t["minted"]):3d} v2={len(t["v2keys"]):3d} '
                  f'v3_receipts={len(t["rises"]):2d} {dict(t["cls"])}  {t["subj"]}')
