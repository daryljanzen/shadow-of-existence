#!/usr/bin/env python3
"""r7355+cc66 ④ — the two patches the re-measurement needs, applied to a COPY of
`scripts/mutate_assertions.py` (the instrument in the tree is never touched).

⛭ WHY THIS FILE EXISTS AT ALL.  The `r7341` hop was measured four times and its patch was NEVER
COMMITTED: `r7341_cc66_the_narrowed_hop/` holds `MEASURED.md`, `REGISTRATION.md` and `deadpin.py`,
and the only trace of the hop's code in the whole tree is `split_patch.py`'s two anchor strings,
which reference a `_hop_ok` that exists nowhere.  *So the population the `r7351` limit was stated
over could be re-derived only from a prose description.*  ⇒ **This script is committed so the next
re-measurement is a re-run and not a reconstruction.**

** ⛔ AND IT DELIBERATELY DOES NOT RECONSTRUCT THE HOP'S GATE. **  `r7341` ① states three conditions
that decide WHICH keys the hop mints.  Reconstructing them from prose would give a population that
is *almost* the frozen one, and every figure below would then be incomparable to `r7351`'s by an
unknown amount.  *** The membership is already frozen in `new117.tsv`, so the gate is not needed:
what is needed is the hop's FOLLOW — read the container through the loop/comprehension binding —
which is one line, and the frozen list selects from the superset it mints. ***
  ⌗ The check that this is faithful for this population: the follow must surface ALL `117` frozen
    keys.  It does.

    python3 -I follow_patch.py <copy-of-mutate_assertions.py>
"""
import sys

# (1) r7345+cc66 CORRECTION.md's one-line cause: `_multi_flags` pops `_trace` off every row before
#     `quote()` returns, so a driver reading `r.get('_trace') or ''` gets `''` for every row and any
#     measurement over the narrow trace silently reads nothing.
POP = "        tr = r.pop('_trace', None)"
GET = "        tr = r.get('_trace', None)"

# (2) the hop's FOLLOW, and nothing else.
OLD = """        for n, lit, cont, alt in best.values():
            trace = _reads(cont, asg, fns, src)
            if trace is None:
                continue"""
NEW = """        for n, lit, cont, alt in best.values():
            trace = _reads(cont, asg, fns, src)
            if trace is None:
                trace = _reads(cont, tasg, fns, src)      # r7355+cc66: the hop's FOLLOW, no gate
            if trace is None:
                continue"""

p = sys.argv[1]
s = open(p, encoding='utf-8').read()
assert s.count(POP) == 1, 'the _trace pop is not where CORRECTION.md says it is'
assert s.count(OLD) == 1, 'the narrow-trace branch is not where it was'
open(p, 'w', encoding='utf-8').write(s.replace(POP, GET, 1).replace(OLD, NEW, 1))
print('patched', p, '-- _trace kept, hop follow added, gate NOT reconstructed')
