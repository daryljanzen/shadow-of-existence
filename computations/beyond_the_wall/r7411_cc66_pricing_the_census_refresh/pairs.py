#!/usr/bin/env python3
"""r7411 (1), refinement -- is the refresh 21 reads, or 11 re-reads of claims 69 already verdicted?

price.py returns 10 stale rows and 11 new candidates.  If a new candidate is a REWORDING of a stale
row's own sentence, the refresh re-reads ONE claim and carries 69's existing verdict forward; if it is
unrelated prose, 69 reads something it has never seen.  The two cost different things, so they are
counted separately rather than added.

The pair test is deliberately crude and stated: normalised token sets, Jaccard >= 0.5, within the same
paper.  A pair is reported with its overlap so the call is visible rather than asserted.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util as u
spec = u.spec_from_file_location('price', os.path.join(HERE, 'price.py'))
pr = u.module_from_spec(spec)
_out = []
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(pr)       # price.py prints its own report; we want its data

def toks(s):
    s = re.sub(r'\\[a-zA-Z]+\*?(\{[^}]*\})?', ' ', s)
    return {w for w in re.findall(r'[a-z]{3,}', s.lower())}

stale = [r for r in pr.rows if r['sent'] not in pr.now.get(r['paper'], set())]
new = pr.new
def jac(a, b):
    ta, tb = toks(a), toks(b)
    return len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0

print('  PAIRING THE STALE ROWS AGAINST THE NEW CANDIDATES -- same claim reworded, or new prose?')
print(f'    {len(stale)} stale row(s), {len(new)} new candidate(s); pair test = same paper, token Jaccard >= 0.50')
print()
used, pairs, orphan_new = set(), [], []
for p, s in sorted(new):
    best, bi = 0.0, None
    for i, r in enumerate(stale):
        if r['paper'] != p or i in used:
            continue
        v = jac(s, r['sent'])
        if v > best:
            best, bi = v, i
    if bi is not None and best >= 0.50:
        used.add(bi); pairs.append((p, best, stale[bi], s))
    else:
        orphan_new.append((p, best, s))
orphan_stale = [r for i, r in enumerate(stale) if i not in used]
print(f'  PAIRED (a reworded claim -- one read, 69 already has a verdict)   {len(pairs)}')
print(f'  NEW and UNPAIRED (never read by 69 -- a fresh verdict)           {len(orphan_new)}')
print(f'  STALE and UNPAIRED (the claim is GONE -- a row to retire)        {len(orphan_stale)}')
print(f'  ⇒ CLAIMS the refresh must read: {len(pairs) + len(orphan_new)}'
      f'  (of which {len(pairs)} carry an existing verdict)')
print()
for p, v, r, s in pairs:
    print(f'    [{p}] paired J={v:.2f}  {r["cls"]:8} {r["topic"][:40]}')
    print(f'         was: {r["sent"][:118]}')
    print(f'         now: {s[:118]}')
print()
for p, v, s in orphan_new:
    print(f'    [{p}] UNPAIRED NEW (best J={v:.2f}): {s[:118]}')
print()
for r in orphan_stale:
    print(f'    [{r["paper"]}] UNPAIRED STALE {r["cls"]:8} {r["topic"][:40]}: {r["sent"][:90]}')
