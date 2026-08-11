#!/usr/bin/env python3
"""
L-127b — THE LAP ORIENTATION, DERIVED RATHER THAN CHOSEN.  And the flagged "hazard" turns
out to be MY BUG, not the corpus's gap, so the alarm is withdrawn as well as fixed.

At c54.50 `L-127` reported that the mode's monodromy eigenvalue came out omega^(+lambda)
while `L-78`'s triality is -lambda mod 3, and concluded that the corpus had never fixed the
LAP ORIENTATION -- calling it a bookkeeping hazard for `L-65`/`L-73`, where windings are
SUMMED across constituents.  ** Daryl said fix it.  Deriving it instead of choosing it shows
there was nothing to fix in the corpus: the orientation IS determined, `L-78` has it right,
and `L-127`'s matrix was the shift in the wrong direction. **

  PART 1  The cover, the deck map, and the action on FUNCTIONS -- built from scratch, with
          nothing assumed about which way anything shifts.
  PART 2  ** THE MONODROMY OF A SECTION IS PULLBACK ALONG THE DECK MAP, AND THAT FIXES THE
          DIRECTION.  `L-127`'s P was P^(-1). **
  PART 3  What survives, what does not, and why every `L-127` conclusion is untouched.
  PART 4  ** THE SUMS CHECKED: `L-73`'s three classes re-run under the derived orientation. **
  PART 5  The alarm withdrawn, and what was actually learned.

Run: python3 L127b_fix_the_orientation.py
"""
import sympy as sp
from fractions import Fraction as F

print(__doc__.split("Run:")[0])

I3 = sp.eye(3)
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0

# =====================================================================
print("=" * 78)
print("PART 1 — THE COVER AND THE DECK MAP, BUILT WITH NOTHING ASSUMED")
print("=" * 78)
for s in [
 "The branching is `L-78`'s and it is not a modelling choice: near the wall the bead's law is",
 "  ** r^3 = (9/2) M l^2 **,  so r is a CUBE ROOT of a quantity with a simple zero.",
 "",
 "So take the base coordinate to be l, and the three sheets to be the three cube roots",
 "  ** r_k = omega^k r_0,   k = 0, 1, 2 **   with r_0 one chosen branch.",
 "A crossing is a half-loop in l, and `L-78` computes its effect: ** r -> omega r **.",
 "",
 "⇒ ** THE DECK GENERATOR D IS THEREFORE FIXED BY THE GEOMETRY, NOT CHOSEN: it is the map",
 "   that sends the sheet carrying r_k to the sheet carrying omega r_k, i.e. D : k -> k+1. **",
 "   There is no freedom here.  The freedom I thought I had was somewhere else, and PART 2",
 "   shows it was not freedom at all.",
]:
    print("  " + s)

lam = sp.Symbol('lambda', integer=True)


def psi_on_sheet(k, L):
    """value of psi ~ r^(-lambda) on sheet k, in units of r_0^(-lambda)"""
    return sp.simplify((w**k)**(-L))


print()
print("  The mode on each sheet (units of r_0^(-lambda)), from psi ~ r^(-lambda) alone:")
print(f"     {'lambda':>7}  {'sheet 0':>10} {'sheet 1':>26} {'sheet 2':>26}")
for L in range(4):
    row = [sp.nsimplify(psi_on_sheet(k, L)) for k in range(3)]
    print(f"     {L:>7}  {str(row[0]):>10} {str(row[1]):>26} {str(row[2]):>26}")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE MONODROMY IS PULLBACK, AND THAT SETTLES THE DIRECTION")
print("=" * 78)
for s in [
 "A section of the pushforward E = pi_*(mode bundle) over a base point is the TUPLE OF VALUES",
 "on the three preimages: s = (s_0, s_1, s_2), s_k = psi(sheet k).",
 "",
 "** Transporting a section once around the branch point acts on FUNCTIONS, and the action of",
 "   a deck map on functions is PULLBACK: (D* psi)(x) = psi(D x).  In components that reads",
 "   (D* s)_k = s_{k+1}, because D sends sheet k to sheet k+1. **",
 "",
 "⌗ ** THAT IS THE WHOLE OF IT, AND IT IS FORCED.  A function is evaluated at the image, so",
 "   the index moves the SAME way the deck map does; the pushforward's monodromy matrix is",
 "   therefore the shift (Ms)_k = s_{k+1}, and NOT the shift (Ms)_k = s_{k-1}. **",
]:
    print("  " + s)

# D* : (M s)_k = s_{k+1}   -- pullback along k -> k+1
M = sp.Matrix([[0, 1, 0],
               [0, 0, 1],
               [1, 0, 0]])
# what L-127 used
P_old = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])
print()
print(f"  derived monodromy M (pullback)      = {M.tolist()}")
print(f"  what `L-127` used, P                = {P_old.tolist()}")
print(f"  ** M = P^(-1) : {sp.simplify(M - P_old.inv()) == sp.zeros(3)} "
      f"-- so `L-127` used the INVERSE deck generator. **")
print()
print(f"  {'lambda':>7} {'M-eigenvalue':>14} {'L-78 phase omega^(-lambda)':>28} "
      f"{'agree':>7} {'triality -L mod 3':>18}")
allok = True
for L in range(7):
    s = sp.Matrix([psi_on_sheet(k, L) for k in range(3)])
    img = sp.simplify(M * s)
    eig = sp.simplify(img[0] / s[0])
    assert sp.simplify(img - eig * s) == sp.zeros(3, 1), "must be an eigenvector"
    l78 = sp.simplify(w**(-L))
    ok = sp.simplify(eig - l78) == 0
    allok &= ok
    kk = [j for j in range(3) if sp.simplify(eig - w**j) == 0][0]
    print(f"  {L:>7} {'omega^' + str(kk):>14} {'omega^' + str((-L) % 3):>28} "
          f"{str(bool(ok)):>7} {(-L) % 3:>18}")
print()
print(f"  ** THE DERIVED MONODROMY REPRODUCES `L-78` EXACTLY, FOR EVERY lambda: {bool(allok)}. **")
for s in [
 "",
 "⇒ ** SO THERE IS NO UNFIXED CONVENTION.  `L-78`'s omega^(-lambda) per crossing and",
 "   triality = -lambda mod 3 are the DERIVED values, and `L-127` disagreed with them because",
 "   it wrote the shift in the wrong direction -- pushing the index instead of pulling it. **",
 "",
 "⚠ ** THE FLAGGED HAZARD IS THEREFORE WITHDRAWN, AND IT WAS MINE. **  `L-127` reported 'a",
 "   signed Z_3 label whose sign depends on an unfixed orientation is a hazard wherever",
 "   windings are SUMMED' and put the debt on P14.  ** The corpus owed nothing.  A node that",
 "   finds a disagreement between its own new matrix and an established result should suspect",
 "   the matrix first, and I published the alarm before doing the derivation that settles it. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT SURVIVES, AND WHY IT IS EVERYTHING")
print("=" * 78)
same_group = (sorted([sp.nsimplify(x) for x in M.eigenvals()], key=str) ==
              sorted([sp.nsimplify(x) for x in P_old.eigenvals()], key=str))
inv_M = sp.simplify(M * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1)
inv_P = sp.simplify(P_old * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1)
Q = sp.diag(1, w, w**2)
heis_M = sp.simplify(Q * M - sp.simplify(w**2) * M * Q) == sp.zeros(3)
m = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'z{i}{j}'))
sol = sp.solve(list(sp.simplify(m * M - M * m)) + list(sp.simplify(m * Q - Q * m)),
               list(m), dict=True)[0]
irred = len(sp.simplify(m.subs(sol)).free_symbols) == 1
B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'c{min(i,j)}{max(i,j)}'))
bsol = sp.solve(list(sp.simplify(M.T * B * M - B)) + list(sp.simplify(Q.T * B * Q - B)),
                sorted(B.free_symbols, key=str), dict=True)
noform = sp.simplify(B.subs(bsol[0])) == sp.zeros(3) if bsol else False

print(f"  {'L-127 claim':>52} {'holds under M?':>16}")
for a, b in [
    ("rank 3, complex, flat", True),
    ("holonomy is Z_3 (M^3 = I, det M = +1, unitary)",
     sp.simplify(M**3) == I3 and sp.det(M) == 1 and sp.simplify(M.H * M) == I3),
    ("<M> and <P> are the SAME group and the same eigenlines", bool(same_group)),
    ("the colourless line is the invariant vector (1,1,1)", bool(inv_M and inv_P)),
    ("the mode is an eigenvector for every lambda", bool(allok)),
    ("clock/shift relation Q M = omega^(-1) M Q", bool(heis_M)),
    ("<M,Q> acts irreducibly on C^3 (commutant = scalars)", bool(irred)),
    ("<M,Q> preserves no symmetric bilinear form", bool(noform)),
    ("smallest connected group containing both is SU(3)", bool(irred and noform)),
]:
    print(f"  {a:>52} {str(b):>16}")
print()
for s in [
 "** EVERY CONCLUSION OF `L-127` IS UNTOUCHED, and it is not luck: M and P generate THE SAME",
 "   Z_3 and have THE SAME eigenlines. **  Only the LABELLING of two of the three eigenlines by",
 "   triality is swapped, and the swapped labelling was the wrong one.  The reality obstruction,",
 "   the elimination of P14's list, the correction to `L-115`, the identification of the",
 "   pushforward, the singlet line and the one-generator gap all stand exactly as recorded.",
 "",
 "⌗ AND THE ONE SUBSTANTIVE CHANGE IS THAT THE RESULT GOT STRONGER, not weaker: `L-127` said",
 "   the eigenvalue 'differs from triality by a convention'.  ** It does not differ from triality",
 "   at all.  The monodromy eigenvalue of the pushforward IS the triality, on the nose, with no",
 "   convention interposed -- which is a cleaner statement than the one it replaces. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE SUMS, CHECKED UNDER THE DERIVED ORIENTATION")
print("=" * 78)
print("  `L-73` derives the thirds from closure: a triple splits 1+2 by horn, the two routes")
print("  differ by one lap, and an admissible object closes.  Its classes are k mod 3 with")
print("  x = k/3 (head) and y = x - 1 (partner).  ** The question the alarm raised was whether")
print("  a sign flip in the Z_3 label breaks the SUMS.  Run both orientations and compare: **")
print()
print(f"  {'k':>3} {'x':>7} {'y':>7} {'upper x+2y':>11} {'lower y+2x':>11} "
      f"{'triality (M)':>13} {'triality (P)':>13} {'class':>11}")
names = {0: 'LEPTONIC', 2: 'QUARKS', 1: 'ANTIQUARKS'}
rows = []
for k in (0, 2, 1):
    xv, yv = F(k, 3), F(k, 3) - 1
    tri_M, tri_P = k % 3, (-k) % 3
    rows.append((k, xv, yv, xv + 2*yv, yv + 2*xv, tri_M, tri_P))
    print(f"  {k:>3} {str(xv):>7} {str(yv):>7} {str(xv + 2*yv):>11} {str(yv + 2*xv):>11} "
          f"{tri_M:>13} {tri_P:>13} {names[k]:>11}")
print()
tot_ok = all(r[3] in (0, -1, -2) or True for r in rows)
closes_M = all((r[5] * 3) % 3 == 0 for r in rows)
swap = {r[0]: r[6] for r in rows}
print("  ** THE SUMS DO NOT MOVE.  x, y and the two totals are computed from k alone and never")
print("     touch the Z_3 label's sign; the orientation only decides WHICH of the two coloured")
print("     classes is called triality 1 and which 2. **")
print(f"     under M:  k=2 (u,d) has triality {swap and rows[1][5]},  k=1 (dbar,ubar) has "
      f"triality {rows[2][5]}")
print(f"     under P:  k=2 (u,d) has triality {rows[1][6]},  k=1 (dbar,ubar) has "
      f"triality {rows[2][6]}")
print()
for s in [
 "⌗ ** AND THE TWO COLOURED CLASSES ARE EXCHANGED BY OVERALL SIGN REVERSAL, WHICH `L-73`",
 "   ALREADY IDENTIFIES AS C. **  So the orientation flip acts on the ledger exactly as charge",
 "   conjugation does -- it swaps quark with antiquark and fixes the leptonic class.  ** That is",
 "   why nothing downstream could have broken: `L-65`/`L-73` sum x and y, which are rationals",
 "   fixed by k, and the label's sign only names which member of a C-pair you started from. **",
 "",
 "⚠ ** BUT IT IS NOT VACUOUS, AND THIS IS THE PART WORTH KEEPING. **  It means the corpus's",
 "   'quark' vs 'antiquark' assignment is fixed by the ORIENTATION OF THE LAP and by nothing",
 "   else in the geometry.  ** The geometry produces a C-pair and does not, on its own, say",
 "   which member is matter. **  That is `L-73`'s own 'quark or antiquark is a RELATIVE",
 "   designation' and P13's 'the sign is field-level, not geometric' arriving a third time, and",
 "   it is consistent with both rather than a new gap.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT WAS ACTUALLY LEARNED")
print("=" * 78)
for s in [
 "① ** THE ORIENTATION IS DERIVED, SO IT NEEDS NO CONVENTION AND P14 NEEDS NO SENTENCE FIXING",
 "   ONE. **  What P14 should carry instead is the derivation's content: the monodromy of the",
 "   pushforward is pullback along the deck map, and its eigenvalue on psi ~ r^(-lambda) is",
 "   omega^(-lambda), which IS the triality.  ** A stronger sentence than the one that was owed. **",
 "",
 "② ** THE ALARM WAS FALSE AND IT WAS MINE, AND THAT IS THE REPORTABLE PART. **  `L-127` found",
 "   a disagreement between a matrix it had just written and a result established twenty",
 "   revisions earlier, and recorded the ESTABLISHED result as the doubtful one.  ** The base",
 "   rate is against the new matrix every time, and I did not apply it. **  Recorded to",
 "   `THE_BASE_RATE.md` as a class: when new work disagrees with old work, the burden of proof",
 "   is on the new work, and 'flagging honestly' is not a substitute for doing the derivation.",
 "",
 "③ ** AND ONE REAL THING SURVIVES THE WITHDRAWAL: the geometry fixes the C-PAIR and not its",
 "   MEMBERS. **  The orientation flip is exactly C on `L-73`'s ledger.  ** So the corpus's",
 "   matter/antimatter assignment at this level is not geometric, which is what P13 says at",
 "   field level and what the antimatter-progenitor theorem says at cosmological level. **",
 "   Three levels, one statement, and this is the third independent arrival.",
]:
    print("  " + s)
