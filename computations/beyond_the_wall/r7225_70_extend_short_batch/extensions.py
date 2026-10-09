#!/usr/bin/env python3
"""The extended literal for each of the 158 keys: r7215/r7221's minimal-D search, returning the string (leftmost on
ties), at each key's wrap-tolerant site in the body S7/S8 read.  Writes extensions.json."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7223_70_detector_blindnesses'))
import r1_wrap as W
import load442, load270

CAP = 25


def ext(c, a, n, flips, lo=0, hi=None):
    hi = len(c) if hi is None else hi
    for t in range(0, CAP + 1):
        for l in range(0, t + 1):
            r = t - l
            if a - l < lo or a + n + r > hi:
                continue
            s = c[a - l:a + n + r]
            if all(s not in fl for fl in flips.values()):
                return t, s
    return None, None


W.paper_half(); W.source_half()
nsP, _, bodies, *_ = load442.load()
nsS = load270.load()
batch = json.load(open(os.path.join(HERE, 'batch_inputs.json')))
out = []
for half, rec, lit, D in batch:
    key = ('P' if half == 'PAPER' else 'S', rec, lit)
    b, sites = W.SITES[key]
    res = []
    for p, i, j in sites:
        if half == 'PAPER':
            x = bodies[p]; c = nsP['clause_at'](x, i, j); start = x.find(c, max(0, i - nsP['WINDOW'] - 2))
            res.append(ext(c, i - start, j - i, nsP['reversals'](c)))
        else:
            x = nsS['SRC'][p]; I = nsS['I']; c = I['clause_at'](x, i, j); start = x.find(c, max(0, i - I['WINDOW'] - 2))
            nsS['is_prose'](p, i); span = next(q for q in nsS['_PS'][p] if q[0] <= i < q[1])
            res.append(ext(c, i - start, j - i, I['reversals'](c), max(0, span[0] - start), min(len(c), span[1] - start)))
    strs = {s for _, s in res}
    t = max((d for d, _ in res), default=None) if None not in [d for d, _ in res] else None
    s = res[0][1] if len(strs) == 1 else None
    p = sites[0][0]
    out.append(dict(half=half, receipt=rec, lit=lit, D=int(D), D_found=t, ext=s, site=p, n_sites=len(sites), divergent=len(strs) > 1, wrap='\n' in (s or '')))
json.dump(out, open(os.path.join(HERE, 'extensions.json'), 'w'), ensure_ascii=False, indent=1)
import collections
print(len(out), 'keys; multi-site:', sum(o['n_sites'] > 1 for o in out), '; divergent:', sum(o['divergent'] for o in out), '; D agrees:', sum(o['D'] == o['D_found'] for o in out), '; extension spans a wrap:', sum(o['wrap'] for o in out))
