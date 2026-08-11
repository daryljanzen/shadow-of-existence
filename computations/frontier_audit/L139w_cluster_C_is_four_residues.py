#!/usr/bin/env python3
"""
L-139w — CLUSTER C, WORKED AS A BLOCK. FOUR ITEMS WHOSE MAIN PARTS ARE DONE AND WHOSE RESIDUES
ARE, IN EVERY CASE, SOMETHING THE REGISTER ALREADY HOLDS.

  `L-139` (map `C·3`)  the smeared infinite-dimensional homomorphism as a structural statement
  `L-140` (map `C·4`)  charges into the construction
  `L-141` (map `C·5`)  the full classification of causal reassignments
  `L-144` (map `C·9`)  the explicit matter functionals off the kernel

** ALL FOUR SAY INSIDE THEMSELVES THAT THEIR MAIN PART IS BUILT, AND ONE OF THEM SAYS OUTRIGHT
THAT IT IS *STRIKE-ELIGIBLE*.  What they lacked was not work but a register that could see where
each residue had gone -- which is the thing the fold supplied. **

  PART 1  Each item's own verdict, quoted, and where the work actually sits.
  PART 2  ** THE RESIDUES, TRACED -- and every one lands on a registered item or on nothing. **
  PART 3  The load-bearing checks, run rather than trusted.
  PART 4  The four strikes, and the one honest caveat that travels with them.

Run: python3 L139w_cluster_C_is_four_residues.py
"""
import os
import re
import subprocess
import sys

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def body(name):
    return '\n'.join(l for l in open(os.path.join(ROOT, 'corpus', name),
                                     encoding='utf-8', errors='replace').read().split('\n')
                     if not l.lstrip().startswith('%'))


# =====================================================================
print("=" * 78)
print("PART 1 — EACH ITEM'S OWN VERDICT")
print("=" * 78)
VERDICT = [
    ("C·3", "L-139", "the reducible corollary is DONE in P12",
     "\"P12 §scope §137-138 now STATES AND PROVES IT CLEANLY … C·3-reducible is thus met in P12\""),
    ("C·4", "L-140", "largely subsumed by P9's kernel",
     "\"only the explicit slicing-curve/groupoid fold remains, small\""),
    ("C·5", "L-141", "the reducible-sector part is DONE (r569)",
     "\"C·5-whole now open ONLY on the gated Tier-3 Kerr-inner/RN remainder, matter-side\""),
    ("C·9", "L-144", "collected and verified symbolically (r964)",
     "\"** strike-eligible: collected + verified + baked into P9 §open **\""),
]
print(f"  {'map':>5} {'lead':>7} {'its own verdict':>42}")
for code, lid, short, quote in VERDICT:
    print(f"  {code:>5} {lid:>7} {short:>42}")
    print(f"        {quote}")
print()
for s in [
 "⌗ ** ONE OF THE FOUR CARRIES THE WORDS 'STRIKE-ELIGIBLE' IN ITS OWN TEXT and had been sitting",
 "   open regardless. **  *That is not an oversight by whoever wrote it -- the map had no",
 "   striking bar and no gate; a note that an item COULD be struck had nowhere to go.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE RESIDUES, TRACED")
print("=" * 78)
print(f"  {'map':>5} {'what is left of it':>40} {'where that already lives':>30}")
RES = [
    ("C·3", "the past-the-wall grand claim", "** `A2` = `L-136` **"),
    ("", "(P12 hands it to the free transverse", "registered and open"),
    ("", "sector past the wall)", ""),
    ("C·4", "the explicit slicing-curve/groupoid fold", "** `C·9` = `L-144` **"),
    ("", "(charge / rotation instance)", "which says it is its home"),
    ("C·5", "Kerr-inner / RN-interior, matter-side", "** `A·4` = `L-138` **"),
    ("", "(P7 frontier item 3's own remainder)", "registered and open"),
    ("C·9", "-- nothing --", "** collected and baked **"),
]
for a, b, c in RES:
    print(f"  {a:>5} {b:>40} {c:>30}")
print()
for s in [
 "⇒⇒ ** NO RESIDUE IS ORPHANED.  Three land on items the register already holds and one is empty,",
 "   so striking the four loses nothing and the burndown stays honest. **",
 "",
 "⌗ ** AND `C·4` IS THE PRETTIEST OF THE FOUR: its residue is `C·9`, and `C·9`'s own text names it",
 "   -- *'C·4 (charge/rotation instance) and the strut caveat now have their general home here'*.",
 "   The map contained the pointer and could not act on it. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE LOAD-BEARING CHECKS, RUN")
print("=" * 78)
P12 = body('algebroid_paper.tex')
P9 = body('range_paper.tex')
checks = []

hit = re.search(r'the smeared closure for arbitrary lapses follows on this sector as a corollary',
                P12)
checks.append(("P12's body carries the smeared corollary (not only its comments)", bool(hit)))
hit2 = re.search(r'smeared, infinite-dimensional homomorphism \\emph\{on the symmetry-reducible '
                 r'sector\} follows as the corollary', P12)
checks.append(("P12's own summary lists it as a handoff, not an open closure", bool(hit2)))
checks.append(("P9 carries the Kantowski--Sachs class", 'Kantowski' in P9))
checks.append(("P9 carries the axial strut / conical defect", 'strut' in P9 or 'conical' in P9))

comp = os.path.join(ROOT, 'computations', 'matter_functionals', 'matter_functionals_C9.py')
rc = subprocess.run([sys.executable, comp], capture_output=True).returncode if os.path.exists(comp) else 99
checks.append(("C·9's symbolic verification exists and RUNS (rc=0)", rc == 0))
checks.append(("C·5's reducible build is on disk (retired, as a completed build)",
               os.path.exists(os.path.join(ROOT, 'retired', 'C5_reducible_build.md'))))

print(f"  {'check':>62} {'result':>8}")
for what, res in checks:
    print(f"  {what:>62} {('** yes **' if res else 'NO'):>8}")
assert all(r for _, r in checks), [w for w, r in checks if not r]
print()
for s in [
 "⌗ ** SIX CHECKS, ALL PASSING, AND THE ONE THAT MATTERS MOST IS THE THIRD-FROM-LAST: `C·9`'s",
 "   symbolic verification is not merely on disk, it RUNS. **  *A collected result whose",
 "   computation no longer executes is not collected, and that is the check a striking bar should",
 "   make and the map never could.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE FOUR STRIKES, AND THE CAVEAT THAT TRAVELS WITH THEM")
print("=" * 78)
print(f"  {'lead':>7} {'map':>6} {'disposal':>16} {'residue goes to':>26}")
for a, b, c, d in [
    ("L-139", "C·3", "** STRIKE **", "L-136 (A2)"),
    ("L-140", "C·4", "** STRIKE **", "L-144, then nothing"),
    ("L-141", "C·5", "** STRIKE **", "L-138 (A·4)"),
    ("L-144", "C·9", "** STRIKE **", "-- nothing --"),
]:
    print(f"  {a:>7} {b:>6} {c:>16} {d:>26}")
print()
for s in [
 "⚠ ** THE CAVEAT, AND IT IS THE SAME ONE FOR ALL FOUR: A STRIKE HERE MEANS THE ITEM'S OWN",
 "   QUESTION IS ANSWERED OR REHOUSED, NOT THAT THE PHYSICS IS FINISHED. **  *The past-the-wall",
 "   claim, the Kerr-inner and Reissner--Nordström interiors, and the matter dynamics they are",
 "   gated on are all genuinely open -- they are open ON OTHER ROWS, where the burndown can see",
 "   them and the gates can police them.*",
 "",
 "⌗⌗ ** WHAT THE BLOCK SHOWS ABOUT THE FOLD: none of these four needed a computation.  They needed",
 "   a register with a striking bar, a burndown that counts, and somewhere for a residue to be",
 "   sent. **  *The map had a readiness sort and a priority sort and no way to CLOSE anything --",
 "   so items that had finished stayed on it, and the count it reported was never the work",
 "   remaining.*",
]:
    print("  " + s)
