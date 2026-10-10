#!/usr/bin/env python3
"""r7243+70.1 -- the extended literal for each of the 295 EXTEND-LONG keys: r7225's minimal-D search with the cap
raised to 100, and ACCEPTANCE (b) IN THE ENGINE -- the candidate's own wrap-tolerant sites are recomputed over the same
bodies and r7223's verdict rule must return DISCRIMINATING for it, or the key is NOT-DISCRIMINATING and never applied.
Run in a worktree at fae76e75, where r7223's loaders reconcile with S7/S8.  Writes extensions.json."""
import bisect, json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7223_70_detector_blindnesses'))
import r1_wrap as W
import load442, load270

CAP = 100


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
SRC, I = nsS['SRC'], nsS['I']
blob, offs, pos = [], [], 0
for p in sorted(SRC):
    offs.append((pos, p)); blob.append(SRC[p]); pos += len(SRC[p]) + 3; blob.append('\n\x00\n')
BLOB = ''.join(blob); starts = [o for o, _ in offs]


def b_check(half, rec, s):
    """acceptance (b): the extended literal's own sites, and every declared reversal must break it"""
    P = W.pat(s)
    if half == 'PAPER':
        sites = [(p, m.start(), m.end()) for p, x in bodies.items() for m in P.finditer(x)]
        return W.verdict(sites, bodies.get, nsP['clause_at'], nsP['reversals'], s) if sites else 'ABSENT'
    sites = []
    for m in P.finditer(BLOB):
        i = bisect.bisect_right(starts, m.start()) - 1; p = offs[i][1]
        if p != rec:
            sites.append((p, m.start() - starts[i], m.end() - starts[i]))
    pros = [x for x in sites if nsS['is_prose'](x[0], x[1])]
    return W.verdict(pros, SRC.get, I['clause_at'], I['reversals'], s) if pros else 'CODE'


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
            x = SRC[p]; c = I['clause_at'](x, i, j); start = x.find(c, max(0, i - I['WINDOW'] - 2))
            nsS['is_prose'](p, i); span = next(q for q in nsS['_PS'][p] if q[0] <= i < q[1])
            res.append(ext(c, i - start, j - i, I['reversals'](c), max(0, span[0] - start), min(len(c), span[1] - start)))
    strs = {s for _, s in res}
    t = max((d for d, _ in res), default=None) if None not in [d for d, _ in res] else None
    s = res[0][1] if len(strs) == 1 else None
    bv = b_check(half, rec, s) if s else None
    out.append(dict(half=half, receipt=rec, lit=lit, D=int(D), D_found=t, ext=s, site=sites[0][0], n_sites=len(sites),
                    divergent=len(strs) > 1, none=None in strs, b_verdict=bv, wrap='\n' in (s or '')))
json.dump(out, open(os.path.join(HERE, 'extensions.json'), 'w'), ensure_ascii=False, indent=1)
print(len(out), 'keys; multi-site:', sum(o['n_sites'] > 1 for o in out), '; divergent:', sum(o['divergent'] for o in out),
      '; no extension within the cap:', sum(o['none'] for o in out), '; D agrees:', sum(o['D'] == o['D_found'] for o in out),
      '; (b) verdicts of the non-divergent:', dict(collections.Counter(o['b_verdict'] for o in out if not o['divergent'])))
