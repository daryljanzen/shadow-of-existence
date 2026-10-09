#!/usr/bin/env python3
"""POST-HOC, not pre-registered: of the keys at D > 300, how many are >300 only because of the prose-span bound
(PREDICTION.md's one named adaptation)?  Re-measures those keys with the bound lifted.  No class in the census
changes; this only attributes the >300 bucket."""
import collections
from load270 import load, per_key
import measure as M

ns = load(); t, keys = per_key(ns)
SRC = ns['SRC']; W = ns['I']['WINDOW']
out = collections.Counter()
for rec, lit, st, used in keys:
    ds = [M.site_D(ns, p, off, lit) for p, off in used]
    if not any(d in (None, 'CAP') for d in ds):
        continue
    free = []
    for p, off in used:
        c = ns['clause_at'](SRC[p], off, off + len(lit))
        a = off - SRC[p].find(c, max(0, off - W - 2))
        free.append(M.min_ext(c, a, len(lit), ns['reversals'](c)))
    if any(d in (None, 'CAP') for d in free):
        out['>300 even unbounded'] += 1
    else:
        m = max(free)
        out['bound-caused, unbounded D ' + ('<=100' if m <= 100 else '>100')] += 1
print('  ', dict(out), ' total', sum(out.values()))
