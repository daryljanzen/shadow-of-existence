"""
P06_the_boundary_is_a_class.py -- P6 sec:register-boundary: the register's boundary has three
members, not one, and two candidates that fail to join it -- so it is a CLASS with an edge
rather than a single exception.

WHAT PROMPTED IT.  The subsection said "the dimension is ... the first such case the programme
has met", which understates what a survey turns up.

WHAT IS ESTABLISHED (survey against P6's own definition: a modulus fixes HOW A SYMMETRY IS
BROKEN; the boundary holds discrete structural choices that leave the symmetry maximal).
  MEMBERS -- unforced, discrete, not moduli:
    1. THE DIMENSION.  De Sitter is maximally symmetric and moduli-free in every dimension.
    2. THE NUMBER OF LAYERS in the ontology.  Discrete, leaves the symmetry maximal, fixes no
       breaking -- and it is the programme's founding move rather than a detail of it.
    3. WHICH REAL FORM of the complexified structure is taken as existent.  Likewise discrete
       and likewise beyond form's reach.
  NOT MEMBERS -- and their exclusion is what gives the class an edge:
    4. THE SIGNATURE is not an unforced choice at all: Lorentzian signature is intrinsic to
       positive curvature.
    5. THE ORIENTATION is not a choice: the configuration's symmetry group is transitive on the
       objects that would distinguish one.

** AND WHAT THE MEMBERS DO NOT SHARE IS HOW THEY ARE SETTLED, which is the more interesting
half. **  The dimension is settled by CONTENT (the fold is D-1 and exists only at D=4,5; the
mass-parity grading chirality exists only in even D; four carries both).  The layering is
settled by the EXISTENCE CRITERION ITSELF -- it is the leaf that carries the clock -- so the
criterion is silent on the NUMBER while deciding which layer is existent, a subtler position
than silence.

** AND THE REAL FORM IS SETTLED BY THE SAME CRITERION AS THE LAYERING. **  Of the forms the
construction reaches, the compact one is Riemannian: no timelike direction, no clock.  The clock
the criterion turns on is measured (the redshift-isotropy floor, P4), so the Lorentzian form is the
existent one and the compact face is real by construction without being a second world (P13
sec:face-status).  The matter sector bears on the choice in neither direction: the colour
structure it reaches is no isometry of either real form, carried instead on the branch structure
of the signed radius (P14_the_wall_is_a_wall_of_a_hinge).

ORIGIN: this file -- built r2376 (c54.69); it is a survey and a propagation, not a computation,
and is written as one."""

print(__doc__.split("ORIGIN")[0])

print("=" * 78)
print("THE CLASS, SORTED BY P6's OWN DEFINITION")
print("=" * 78)
rows = [
    ("the dimension", "yes", "yes", "MEMBER", "settled by CONTENT (matter sector's two deliverables)"),
    ("the number of layers", "yes", "yes", "MEMBER", "settled by the EXISTENCE CRITERION (the leaf carries the clock)"),
    ("which real form", "yes", "yes", "MEMBER", "settled by the EXISTENCE CRITERION (the compact form has no clock)"),
    ("the signature", "no", "-", "not a member", "forced: intrinsic to positive curvature"),
    ("the orientation", "no", "-", "not a member", "not a choice: the symmetry group is transitive"),
]
print(f"  {'candidate':>22} {'unforced?':>10} {'discrete?':>10} {'verdict':>14}  {'how settled'}")
for a, b, c, d, e in rows:
    print(f"  {a:>22} {b:>10} {c:>10} {d:>14}  {e}")
members = [r for r in rows if r[3] == "MEMBER"]
assert len(members) == 3, "the class has three members"
print()
print(f"  ** {len(members)} members, {len(rows)-len(members)} near-misses. **  A boundary with one instance reads as")
print(f"     an exception; a boundary with three and an edge reads as what it is -- a CLASS.")
print()
for s in [
 "⌗ ** AND THE MEMBERS ARE NOT ALL SETTLED THE SAME WAY, WHICH IS THE PART WORTH HAVING. **  Form",
 "is silent on all three, and that is the boundary.  ** But content decides the first, and the",
 "existence criterion decides the second's occupant if not its number and the third outright. **",
 "A boundary is not a place where nothing can be said; it is a place where the criterion cannot",
 "say it, and the programme has two different answers to what says it instead.",
]:
    print("  " + s)
