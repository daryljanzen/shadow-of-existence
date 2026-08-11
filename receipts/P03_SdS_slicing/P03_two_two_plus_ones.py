"""
P03_two_two_plus_ones.py -- P3 sec:cubic / sec:ellipse: the corpus carries TWO 2+1s among
the horizon roots, and they are different partitions of the same three roots.

P14 names both in one sentence -- "the 2+1 of a DESIGNATED ROOT against the ellipse pair
is the diagonal designation sigma, and the SIGN 2+1 (two horizons of one sign against
one) the reflection through the origin" -- and no catalogue had drawn the consequence.

  THEY CUT ACROSS EACH OTHER.  Along the dial the ellipse pair generally holds ONE
  POSITIVE AND ONE NEGATIVE root, so the designated root is never simply "the odd one by
  sign".  Sampled at eight dial positions, the two partitions agree at ONE -- and that
  one is past the throat-tangent, where both negative roots lie together.

  AND THEY ARE DIFFERENT KINDS OF OBJECT.  Holding one geometry (one 2M) and cycling the
  designation through all three roots: THE SIGN SPLIT DOES NOT MOVE.  So the sign 2+1 is
  a property of the GEOMETRY and the designation 2+1 is a property of the VANTAGE --
  the corpus's own geometry/vantage division appearing INSIDE a single triple.

  AT THE DEGENERATE MEMBER THEY MEET.  At r0 = 2/sqrt3 the lone root is both the
  designated one and the odd one by sign; at r0 = 1/sqrt3 they differ.  That is the
  corpus's own "one geometry under two designations", now with a second reading.

  AND AT GENERAL D (L-17): the line component survives always -- it must, since 2M is
  defined as the value making r0 a root -- but the COFACTOR has degree D-2, so it is a
  CONIC only at D=4.  The object generalises as "designated root against the rest";
  what is four-dimensional is its being a 2+1 rather than a 1+(D-2).

** WHAT THIS DOES NOT DO. **  It does not answer FIGURE R3, and is not evidence for or
against any mapping to uud.  It NAMES THE OBJECTS the row failed to name, which is the
work PROTECTED_OPEN PO-1 says is owed before the question can be asked.  Each 2+1 has a
natural candidate side -- the designation one toward generations/flavour-breaking (P14
calls the slicing's singling-out of one root a flavour-breaking structure), the sign one
toward species -- and R3's row names both targets in one line, so the pairing may run
the other way from how it reads.  ** That is a question to ask, not an answer. **

ORIGIN: computations/baryon_edge/L10_name_the_object.py -- built r2376 (c54.17); edit the
origin, not this copy."""



import numpy as np
import sympy as sp

r, r0, M = sp.symbols('r r_0 M', real=True)
print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO PARTITIONS, along the dial")
print("=" * 78)
print("  P3 prop:factor: the horizon cubic factors when the slicing parameter is one of")
print("  its own roots -- (r - r0)(r^2 + r r0 + r0^2 - 1) = 0.  So for every r0:")
print("     the DESIGNATION 2+1 :  { r0, on the LINE }  |  { the ELLIPSE PAIR }")
print("     the SIGN 2+1        :  { positive roots }   |  { negative roots }")
print()
print(f"{'r0':>7} {'the three roots':>34} {'designation split':>26} {'sign split':>22} "
      f"{'same partition?':>16}")
same_count = 0
rows = 0
for r0v in [0.10, 0.25, 0.40, 0.5773, 0.70, 0.90, 1.00, 1.10]:
    twoM = r0v - r0v**3
    rts = np.sort(np.roots([1.0, 0.0, -1.0, twoM]).real)
    # designation: r0 alone vs the conic pair
    des_alone = min(rts, key=lambda x: abs(x - r0v))
    des_pair = sorted([x for x in rts if x is not des_alone and abs(x - des_alone) > 1e-9])
    if len(des_pair) != 2:                       # degenerate; handle by nearest
        des_pair = sorted([x for x in rts if abs(x - des_alone) > 1e-9])
    pos = sorted([x for x in rts if x > 0])
    neg = sorted([x for x in rts if x < 0])
    sign_alone = neg if len(neg) == 1 else pos
    des_set = frozenset([round(des_alone, 6)])
    sgn_set = frozenset([round(x, 6) for x in sign_alone])
    same = des_set == sgn_set
    same_count += bool(same); rows += 1
    print(f"{r0v:>7.4f} {str([float(round(x,4)) for x in rts]):>34} "
          f"{'{'+f'{des_alone:.3f}'+'} | '+str([float(round(x,3)) for x in des_pair]):>26} "
          f"{str([float(round(x,3)) for x in pos])+' | '+str([float(round(x,3)) for x in neg]):>22} "
          f"{str(bool(same)):>16}")
print()
print(f"  the two partitions agree on {same_count} of {rows} dial positions sampled")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 1's CLAIM, ASSERTED.  INDEX: "the ellipse pair generally holds one positive and one
# negative root, so the designated root is never simply the odd one by sign (agreement at
# 1 of 8 sampled dial positions, and that one past the throat-tangent)."
#   · the two partitions agree on EXACTLY ONE of the EIGHT sampled dial positions;
#   · and the one is the LAST, r0 = 1.10, past the throat-tangent, where BOTH other roots
#     are negative: the roots there are -0.8541, -0.2459, 1.10, so the sign split is
#     {1.10} | {-0.8541, -0.2459} and it coincides with the designation split.
assert (same_count, rows) == (1, 8), \
    "the two 2+1s must agree on exactly 1 of the 8 sampled dial positions"
assert same and abs(r0v - 1.10) < 1e-12, \
    "the single agreement must be the last sample, r0 = 1.10, past the throat-tangent"
assert len(neg) == 2 and abs(neg[0] + 0.8541381265149110) < 1e-9 \
    and abs(neg[1] + 0.2458618734850889) < 1e-9 and abs(pos[0] - 1.10) < 1e-9, \
    "at r0 = 1.10 the roots must be -0.8541, -0.2459 and the designated 1.10"
# -----------------------------------------------------------------------------------
print("  ⇒ THEY ARE DIFFERENT PARTITIONS OF THE SAME THREE ROOTS, and they CUT ACROSS")
print("     each other: the ellipse pair generally holds ONE POSITIVE AND ONE NEGATIVE")
print("     root, so the designated root is never simply 'the odd one by sign'.")
print("     ** Two 2+1s, two different cuts.  The corpus's sentence was exact and the")
print("        catalogues had never drawn the consequence. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT ACTS ON EACH")
print("=" * 78)
print("  DESIGNATION: which root is called one's own black-hole horizon.  P3: 'each")
print("  geometry is met at several r0-values -- ONE PER ROOT IT MAY DESIGNATE -- while")
print("  the swing angle places each geometry ONCE'.  So the designation partition is a")
print("  CHOICE, there are three of them per geometry, and S_3 permutes them.")
print()
print("  SIGN: a property of the root SET, computed before any designation is made.")
print()
print("  Test: hold the geometry (one 2M) and cycle the designation through all three")
print("  roots.  Does the sign partition move?")
print()
twoM = 0.336
rts = np.sort(np.roots([1.0, 0.0, -1.0, twoM]).real)
print(f"  one geometry, 2M = {twoM}:  roots = {[float(round(x,4)) for x in rts]}")
for k, dr in enumerate(rts):
    pair = [x for x in rts if abs(x - dr) > 1e-12]
    pos = [x for x in rts if x > 0]; neg = [x for x in rts if x < 0]
    print(f"    designate {dr:+.4f} -> designation split "
          f"{{{dr:+.3f}}} | {[float(round(x,3)) for x in pair]}   "
          f"sign split {[float(round(x,3)) for x in pos]} | {[float(round(x,3)) for x in neg]}")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 2's CLAIM, ASSERTED.  One geometry, 2M = 0.336, has roots -1.13808315, 0.4 (exact,
# since 0.4 - 0.4^3 = 0.336) and 0.73808315.  Its SIGN 2+1 is {0.4, 0.738} | {-1.138} --
# a 2+1 with the LONE root NEGATIVE, and it is the same for every designation, since it is
# read off the root set alone.  The DESIGNATION 2+1 is not: the loop's last designation
# picks out +0.73808315, which is NOT the sign-lone root, so the two cuts differ there.
assert len(rts) == 3 and abs(rts[0] + 1.1380831519646859) < 1e-9 \
    and abs(rts[1] - 0.4) < 1e-12 and abs(rts[2] - 0.7380831519646859) < 1e-9, \
    "at 2M = 0.336 the horizon roots must be -1.1380831, 0.4 and 0.7380831"
assert len(pos) == 2 and len(neg) == 1 and abs(neg[0] + 1.1380831519646859) < 1e-9, \
    "the sign 2+1 must be two positive against one negative root"
assert abs(dr - 0.7380831519646859) < 1e-9 and len(pair) == 2 and dr != neg[0], \
    "the last designation must single out 0.7380831, not the sign-lone root"
# -----------------------------------------------------------------------------------
print("  ⇒ THE SIGN SPLIT IS DESIGNATION-INVARIANT; the designation split is not.")
print("     ** So they are not two readings of one structure.  One is a property of the")
print("        geometry, the other is a property of the VANTAGE. **")
print("     And that is the corpus's own on/tangent, geometry/vantage division showing up")
print("     inside a single triple -- which is what L8.3 called the marriage.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AT THE DEGENERATE MEMBER")
print("=" * 78)
print("  P3: 'the same Nariai geometry is met at |r0| = 2/sqrt3 with the LONE root")
print("  designated and the other two MERGING: one geometry under two designations.'")
print()
for r0v, label in [(1/np.sqrt(3), 'r0 = 1/sqrt3  (Nariai, designating a merged root)'),
                   (2/np.sqrt(3), 'r0 = 2/sqrt3  (Nariai, designating the LONE root)')]:
    twoM = r0v - r0v**3
    rts = np.sort(np.roots([1.0, 0.0, -1.0, twoM]).real)
    print(f"  {label}")
    print(f"     2M = {twoM:.6f}   roots = {[float(round(x,4)) for x in rts]}")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 3's CLAIM, ASSERTED.  The loop's last member is the r0 = 2/sqrt3 = 1.1547005383792517
# designation, 2M = -2/(3 sqrt3) = -0.3849001794597505, whose roots are the MERGED PAIR
# -1/sqrt3 (twice) and the LONE +2/sqrt3.  There the designated root IS the odd one by sign,
# which is exactly where the two 2+1s meet.
assert abs(r0v - 1.1547005383792517) < 1e-12 and abs(twoM + 0.3849001794597505) < 1e-9, \
    "the last degenerate member must be r0 = 2/sqrt3 with 2M = -2/(3 sqrt3)"
assert abs(rts[0] + 0.5773502691896258) < 1e-9 and abs(rts[1] + 0.5773502691896258) < 1e-9 \
    and abs(rts[2] - 1.1547005383792517) < 1e-9, \
    "at r0 = 2/sqrt3 the roots must be the merged -1/sqrt3 pair and the lone 2/sqrt3"
assert len([x for x in rts if x > 0]) == 1, \
    "at r0 = 2/sqrt3 the designated lone root must also be the odd one BY SIGN"
# -----------------------------------------------------------------------------------
print("  ⇒ at the degenerate member the two partitions COINCIDE for the r0 = 2/sqrt3")
print("     designation -- the lone root is both the designated one AND the odd one by")
print("     sign -- and they DIFFER at r0 = 1/sqrt3, which designates one of the merged")
print("     pair.  ** The degenerate member is where the two objects meet, and the")
print("     corpus already calls that 'one geometry under two designations'. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — L-17: is the locus still line-union-conic at general D?")
print("=" * 78)
print("  The DESIGNATION 2+1 *is* the line/conic split.  If the factorisation fails at")
print("  other D, the object does not exist there -- which the register needs to know.")
print()
print(f"{'D':>3} {'horizon polynomial in r, at r0 a root':>44} {'divisible by (r - r0)?':>24} "
      f"{'cofactor degree':>16}")
for D in range(4, 9):
    poly = r**(D - 1) - r**(D - 3) + (r0**(D - 3) - r0**(D - 1))
    q, rem = sp.div(sp.expand(poly), r - r0, r)
    ok = sp.simplify(rem) == 0
    print(f"{D:>3} {'r^'+str(D-1)+' - r^'+str(D-3)+' + 2M(r0)':>44} {str(ok):>24} "
          f"{int(sp.degree(sp.expand(q), r)):>16}")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 4's CLAIM, ASSERTED.  INDEX: "the divisibility exact in sympy at D=4..8", and
# "the cofactor has degree D-2, so it is a CONIC only at D=4".  The loop's last row is
# D = 8, where the remainder is exactly zero and the cofactor's degree is 6 = D-2 -- a
# sextic, not a conic; the 2+1 is a 1+(D-2) away from four dimensions.
assert ok and sp.simplify(rem) == 0, "(r - r0) must divide the horizon polynomial at D = 8"
assert int(sp.degree(sp.expand(q), r)) == 6, "the cofactor at D = 8 must have degree D-2 = 6"
# -----------------------------------------------------------------------------------
print("  ⇒ THE LINE COMPONENT SURVIVES AT EVERY D -- and it must, because 2M is DEFINED")
print("     as the value making r0 a root, so (r - r0) divides identically.")
print("     ** But the COFACTOR has degree D-2, so it is a CONIC only at D=4. **")
print("     At D=5 the designated root stands against a CUBIC cofactor, at D=6 a quartic.")
print("     So the object generalises as 'designated root against the rest', and the")
print("     'ELLIPSE PAIR' -- the thing that makes it a 2+1 rather than a 1+(D-2) -- is")
print("     four-dimensional.  L-17 answered: reducible always, conic only at D=4.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT EACH IS A CANDIDATE FOR (candidacy, not a match)")
print("=" * 78)
print("  R3's row names TWO targets in one line -- 'uud / generations' -- and the corpus")
print("  has TWO 2+1s.  The pairing has never been stated, and stating it is L-10's job.")
print()
print("  THE DESIGNATION 2+1  { my root } | { the rest }")
print("    · is a property of the VANTAGE, three per geometry, permuted by S_3")
print("    · P14 calls the slicing's singling-out of one root against the ellipse pair a")
print("      FLAVOUR-BREAKING STRUCTURE, supplied with the triplet in P13")
print("    · and each hinge designating one root is what P14 reads as ONE GENERATION")
print("    ⇒ its natural target is the GENERATION side: which generation is 'mine', i.e.")
print("      a candidate for the flavour HIERARCHY among three identical copies.")
print()
print("  THE SIGN 2+1  { positive } | { negative }")
print("    · is a property of the GEOMETRY, designation-invariant, one per geometry")
print("    · sign(r) is SPECIES (matter/antimatter) in the corpus's own canon")
print("    ⇒ its natural target is the SPECIES side, not a within-baryon flavour split.")
print()
print("  ** SO R3'S TWO TARGETS MAY BELONG TO ITS TWO OBJECTS THE OTHER WAY ROUND FROM")
print("     HOW THE ROW READS -- and that is a question to ask, not an answer. **")
print()
print("  WHAT IS NOT SETTLED HERE, and is the next work:")
print("    · whether uud has ANY geometric counterpart -- neither 2+1 has been shown to")
print("      be one, and neither has been shown not to be")
print("    · what the ellipse pair IS, physically, as against the designated root")
print("    · whether the flavour-BREAKING structure P14 names is the hierarchy or")
print("      something else -- P14 explicitly declines to claim it is the hierarchy")
print("  ** PO-1's object is now NAMEABLE: R3 must be split into R3a (designation) and")
print("     R3b (sign), and each asked separately. **")
