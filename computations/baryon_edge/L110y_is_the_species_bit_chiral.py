#!/usr/bin/env python3
"""
L-110y — THE SECTOR'S LAST LIVE DISCHARGE CLAUSE, ANSWERED. AND THE ANSWER IS NO.

c54.78 re-specified S3 to the question the old clause was reaching for, addressed to the operator
that carries it: ** does $T$ act on one $R$-eigenspace of the wall mode and trivially on the
other? **  c54.80 folded S4 into it.  It is the sector's one remaining live clause, and it is a
computation rather than a decision.

** IT IS DECIDABLE FROM WHAT IS ALREADY BANKED, AND THE ANSWER IS NEGATIVE: $T$ ACTS THE SAME ON
BOTH $R$-EIGENSPACES.  THE CONSTRUCTION SUPPLIES A SPECIES *LABEL* AND NOT $SU(2)_L$'s CHIRAL
GAUGING -- AND THE MISMATCH WITH THE STANDARD MODEL IS EXACTLY ONE PAIR WIDE. **

  PART 1  Why the question cannot be asked at a single wall at all.
  PART 2  ** SO IT IS A QUESTION ABOUT THE OCCUPATION, AND `L-117`'s COUNT ANSWERS IT. **
  PART 3  ** THE STANDARD MODEL'S OWN OCCUPATION, BESIDE IT -- AND THEY DIFFER ON ONE PAIR. **
  PART 4  What that does and does not damage.
  PART 5  `L-110` discharged: the verdict on all five clauses.

Run: python3 L110y_is_the_species_bit_chiral.py      (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE QUESTION CANNOT BE ASKED AT A SINGLE WALL")
print("=" * 78)
print("  `prop:wall`'s zero-mode, exactly as the paper solves it:")
print()
print("     H = -i sigma_x d_x + m(x) sigma_z,   m odd, crossing zero at the throat")
print("     psi(x) = exp(-int_0^x m dx') chi_+,  with chi_+ the sigma_y = +1 eigenspinor")
print("     ** and the conjugate branch chi_- GROWS as cosh^{+a} and is REJECTED **")
print()
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
print("  R = gamma^5 = sigma_y on the cut spinor, so the wall's R-eigenspaces are sigma_y = +/-1,")
print("  each ONE-dimensional; and only the + one is bound.")
print()
# the commutant of sigma_y in the 2x2 algebra
a, b, c, d = sp.symbols('a b c d')
Mx = sp.Matrix([[a, b], [c, d]])
comm = sp.simplify(Mx*sy - sy*Mx)
sol = sp.solve([comm[i] for i in range(4)], [a, b, c, d], dict=True)[0]
gen = sp.simplify(Mx.subs(sol))
print("  Every 2x2 matrix commuting with sigma_y:")
sp.pprint(gen)
print(f"     -- a two-parameter family, spanned by the identity and sigma_y itself")
free = sorted({s for s in gen.free_symbols}, key=str)
assert len(free) == 2
print()
for s in [
 "⇒⇒ ** AND $T$ COMMUTES WITH $R$ (computed c54.78, on independent data).  SO $T$ IS DIAGONAL IN",
 "   THE $\\sigma_y$ BASIS AND ACTS ON EACH ONE-DIMENSIONAL EIGENSPACE BY A SCALAR. **",
 "",
 "⇒ ** AT A SINGLE WALL THE CLAUSE IS THEREFORE NOT WELL-POSED: there is one bound eigenspace, it",
 "   is one-dimensional, and every operator commuting with $R$ acts on it by a number.  'Acts",
 "   non-trivially on one and trivially on the other' has no content on a one-dimensional space",
 "   with a rejected partner. **",
 "",
 "⌗ *That is not an evasion -- it is what the clause was really asking, relocated.  A chiral",
 "action is a statement about which STATES the operator moves, so the question is about the",
 "sector's OCCUPATION of the available characters, not about a single wall.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO IT IS A QUESTION ABOUT THE OCCUPATION, AND THE COUNT ANSWERS IT")
print("=" * 78)
print("  `L-117`: the turnaround's group is D_6 = S_3 x Z_2 with the deck Z_3 = A_3 inside the")
print("  S_3, and the colourless (deck-trivial) sector is its FOUR one-dimensional characters,")
print("  indexed by (T, R) = (the S_3 sign, the parity).  All four are present -- the count is")
print("  forced by the group, not chosen.")
print()
GEO = [(t, r) for t in (+1, -1) for r in (+1, -1)]
print(f"  {'the four colourless characters':>32} {'T':>4} {'R':>4}")
for t, r in GEO:
    print(f"  {'(T,R) = (%+d,%+d)' % (t, r):>32} {t:>4} {r:>4}")
print()
print(f"  {'R-eigenspace':>16} {'the T-values it carries':>28} {'is T trivial there?':>21}")
chiral_geo = None
for r in (+1, -1):
    ts = sorted(t for (t, rr) in GEO if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>28} {str(all(t == 1 for t in ts)):>21}")
triv = {r: all(t == 1 for (t, rr) in GEO if rr == r) for r in (+1, -1)}
chiral_geo = (triv[+1] != triv[-1])
print()
print(f"  ** IS THE GEOMETRY'S ACTION CHIRAL -- trivial on one R-eigenspace and not the other?"
      f"  {chiral_geo} **")
assert chiral_geo is False
print()
for s in [
 "⇒⇒ ** NO.  EACH $R$-EIGENSPACE CARRIES ONE $T$-EVEN AND ONE $T$-ODD STATE, so $T$ acts",
 "   non-trivially on BOTH and trivially on NEITHER. **",
 "",
 "⌗ ** AND THE REASON IS STRUCTURAL RATHER THAN NUMERICAL: on a character of a DIRECT product the",
 "   two factors' values are independent by construction, and the colourless sector is exactly",
 "   the four characters of $S_3 \\times \\mathbb{Z}_2$ trivial on the deck. **  *An action that",
 "   depended on the chirality would require the product NOT to be direct -- and its directness is",
 "   itself a computed fact, $T$ and $R$ acting on independent data and commuting.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE STANDARD MODEL'S OWN OCCUPATION, BESIDE IT")
print("=" * 78)
print("  The Standard Model's colourless four, with T the isospin Z_2 (the Weyl element of")
print("  SU(2)_L, which EXCHANGES the doublet's members and fixes each singlet):")
print()
print(f"  {'states':>22} {'chirality R':>12} {'SU(2)_L':>10} {'what T does':>22} {'T-values':>12}")
SM = [("nu_L, e_L", "L", "doublet", "exchanges them", [+1, -1]),
      ("nu_R, e_R", "R", "two singlets", "fixes each", [+1, +1])]
for nm, ch, ir, act, ts in SM:
    print(f"  {nm:>22} {ch:>12} {ir:>10} {act:>22} {str(ts):>12}")
print()
sm_triv = {ch: all(t == 1 for t in ts) for nm, ch, ir, act, ts in SM}
chiral_sm = (sm_triv['L'] != sm_triv['R'])
print(f"  {'R-eigenspace':>16} {'is T trivial there?':>21}")
for ch in ('L', 'R'):
    print(f"  {('R = ' + ch):>16} {str(sm_triv[ch]):>21}")
print(f"\n  ** IS THE STANDARD MODEL'S ACTION CHIRAL?  {chiral_sm} **")
assert chiral_sm is True
print()
print(f"  {'':>16} {'R-even side':>22} {'R-odd side':>22}")
print(f"  {'THE GEOMETRY':>16} {'{+1, -1}':>22} {'{+1, -1}':>22}")
print(f"  {'THE SM':>16} {'{+1, -1}  (the doublet)':>22} {'{+1, +1}  (two singlets)':>22}")
print()
for s in [
 "⇒⇒ ** THE TWO OCCUPATIONS AGREE ON ONE $R$-EIGENSPACE AND DIFFER ON THE OTHER, AND THE",
 "   DIFFERENCE IS EXACTLY ONE PAIR WIDE: the Standard Model's right-handed pair carries TWO",
 "   $T$-even states and the geometry's carries one of each. **",
 "",
 "⌗ ** THAT IS THE SHARPEST STATEMENT THIS SECTOR CAN MAKE ABOUT WHAT IT DOES NOT DELIVER, and it",
 "   is sharper than 'the weak sector is not built': the construction reproduces the LEFT-handed",
 "   side's shape exactly and fails on the RIGHT-handed side, by making a distinction there that",
 "   the Standard Model does not make. **",
 "",
 "⌗ *And it is falsifiable in the honest direction: if a right-handed weak structure distinguishing",
 "$\\nu_R$ from $e_R$ by an isospin-like $\\mathbb{Z}_2$ were ever found, the geometry would be right",
 "and the comparison wrong.  ** The corpus should not want that, and should record the mismatch as",
 "a mismatch. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THAT DOES AND DOES NOT DAMAGE")
print("=" * 78)
CLAIMHDR = "the sector's claim"
print(f"  {CLAIMHDR:>44} {'touched by this?':>18}")
for a, b in [("the generation COUNT (three)", "no"),
             ("the CHIRALITY (R = gamma^5, one mode per wall)", "no"),
             ("the within-state S_3 and the deck Z_3", "no"),
             ("the discrete content of COLOUR (the branching)", "no"),
             ("the two-bit LABELLING of the colourless four", "no -- it stands"),
             ("** reading T as SU(2)_L's chiral gauging **", "** YES -- withdrawn **")]:
    print(f"  {a:>44} {b:>18}")
print()
for s in [
 "⌗ ** NOTHING THE SECTOR DELIVERS RESTS ON THE CLAUSE, WHICH IS WHY THE NEGATIVE IS PUBLISHABLE",
 "   RATHER THAN COSTLY. **  *c54.80 had already established that no $\\mathbb{Z}_2$ grading can",
 "   reproduce $SU(2)_L$'s $2{+}1{+}1$ decomposition; this adds the ORBIT question, which a",
 "   $\\mathbb{Z}_2$ COULD have answered, and answers it in the negative too.*",
 "",
 "⇒ ** SO THE SECTOR'S ISOSPIN READING IS BOUNDED FROM BOTH SIDES NOW: not the decomposition (a",
 "   $\\mathbb{Z}_2$ cannot have three blocks) and not the orbit structure (the product is direct,",
 "   and all four characters are occupied).  $T$ is a species LABEL. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-110` DISCHARGED: THE VERDICT ON ALL FIVE CLAUSES")
print("=" * 78)
print(f"  {'clause':>5} {'verdict':>36} {'when':>10}")
for a, b, c in [
    ("S1", "PARTIAL -- gives FOUR, and four is right", "c54.45"),
    ("S2", "** PASS ** -- lem:twoturnings keeps them apart", "c54.45"),
    ("S3", "re-specified, and now ** ANSWERED: NO **", "c54.78 / here"),
    ("S4", "** WITHDRAWN ** -- structurally ill-posed", "c54.80"),
    ("S5", "** PASS ** -- irreps are equivariant", "c54.45"),
]:
    print(f"  {a:>5} {b:>36} {c:>10}")
print()
for s in [
 "⇒⇒ ** EVERY CLAUSE IS DISPOSED, SO THE SPECIFICATION HAS DONE ITS JOB AND `L-110` STRIKES. **",
 "   *Its job was to say what discharging the count requires, and to be testable rather than",
 "   arguable.* ** The verdict it returns is that the turnaround's colourless sector supplies the",
 "   right SIZE, the right two-bit LABELLING, and NOT the weak sector's chirality. **",
 "",
 "⌗⌗ ** AND THE SPEC EARNED ITS KEEP BY BEING WRONG TWICE IN A USEFUL WAY: S3 as written asked",
 "   COLOUR for an asymmetry colour does not carry, and S4 asked a $\\mathbb{Z}_2$ for a",
 "   decomposition a $\\mathbb{Z}_2$ cannot have.  Both were sharp enough to be shown ill-posed,",
 "   which a vaguer condition would not have been. **  *A specification that can be refuted as a",
 "   specification is doing more work than one that can only be failed.*",
]:
    print("  " + s)
