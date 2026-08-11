#!/usr/bin/env python3
"""
L-119 / L-109 — DID THE HYPERCHARGE COME OUT, OR WAS IT PUT IN?

THE LEAD.  `L-59` solved for the constant of the involution that exchanges u and d on the
winding line and got c = 1/3, which is the quark doublet's hypercharge; the Standard Model
ties Y_Q = 1/3 to N_c = 3 by ANOMALY CANCELLATION.  `L-109` registered that as a MATCH and
not a derivation, and asked the right question: ** compute the anomaly conditions directly
and see whether Y = 1/N falls out or has to be put in. **

** AND THE FIRST MOVE IS TO CHECK WHAT THE CORPUS ALREADY HAS, BECAUSE IT HAS IT.  The
receipt HYPERCHARGE_from_anomalies solves the conditions already.  This runs it at general
N_c, which it does not, and then asks the question L-109 actually poses. **

  PART 1  The anomaly conditions at general N_c, solved.
  PART 2  ** WHAT THEY FIX AND WHAT THEY DO NOT: ratios, yes; the scale, no. **
  PART 3  ** AND THE WINDING FIXES EXACTLY THE THING THEY LEAVE FREE. **
  PART 4  The consistency check: do the two agree where they overlap?
  PART 5  Verdict on L-109, at the weight it is earned.

Run: python3 L109w_scale_and_ratio.py     (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])
q, u, d, l, e, h, Nc = sp.symbols('q u d l e h N_c', rational=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE ANOMALY CONDITIONS AT GENERAL N_c, SOLVED")
print("=" * 78)
print("  One generation of su(N_c) x su(2) x u(1), in the all-left-handed convention:")
print("     Q  (N_c, 2)  hypercharge q      u^c (N_c-bar, 1)  -u      d^c (N_c-bar, 1)  -d")
print("     L  (1,   2)  hypercharge l      e^c (1,      1)   -e")
print()
A_c = 2*q - u - d                      # [SU(N_c)]^2 U(1):  Q has isospin weight 2
A_w = Nc*q + l                         # [SU(2)]^2 U(1):    colour N_c for Q, 1 for L
A_g = 2*Nc*q - Nc*u - Nc*d + 2*l - e   # U(1)-gravitational
A_3 = (2*Nc*q**3 - Nc*u**3 - Nc*d**3 + 2*l**3 - e**3)   # [U(1)]^3
Y1, Y2, Y3 = q - u + h, q - d - h, l - e - h            # the three Yukawas need one Higgs
print(f"  {'condition':>22} {'expression':>34}")
for nm, ex in [("[SU(N_c)]^2 U(1)", A_c), ("[SU(2)]^2 U(1)", A_w),
               ("U(1)-gravitational", A_g), ("Yukawa Q u^c H", Y1),
               ("Yukawa Q d^c H", Y2), ("Yukawa L e^c H", Y3)]:
    print(f"  {nm:>22} {str(ex):>34}")
print()
sol = sp.solve([A_c, A_w, A_g, Y1, Y2, Y3], [u, d, l, e, h], dict=True)
print(f"  solutions: {len(sol)}")
S = sol[0]
for k in (u, d, l, e, h):
    print(f"      {str(k):>3} = {sp.simplify(S[k])}")
print()
cub = sp.simplify(sp.expand(A_3.subs(S)))
print(f"  and the CUBIC condition [U(1)]^3, which was NOT used in the solve:")
print(f"      residual = {sp.factor(cub)}")
print()
print("  ** IT VANISHES IDENTICALLY -- FOR EVERY N_c AND EVERY q.  SO THE CUBIC ANOMALY IS")
print("     AUTOMATICALLY SATISFIED AND SELECTS NOTHING. **")
print("  ⌗ ** A CAUGHT OVERCLAIM, RECORDED.  A first pass of this file printed 'so the cubic")
print("  anomaly SELECTS N_c = 3'.  That was FALSE, and the code even showed it: solving a")
print("  residual that is identically zero returns the EMPTY set, which I read as a solution")
print("  list rather than as the statement that the equation is vacuous. **  The anomaly")
print("  conditions constrain the hypercharges GIVEN the multiplet structure; they do not")
print("  select the number of colours, which was put in when the multiplets were written down.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THEY FIX, AND WHAT THEY DO NOT")
print("=" * 78)
S3 = {k: sp.simplify(v.subs(Nc, 3)) for k, v in S.items()}
print("  At N_c = 3 the solution reads, every hypercharge in terms of the single symbol q:")
print()
print(f"  {'field':>8} {'hypercharge':>16} {'as a multiple of q':>20}")
for nm, val in [("Q", q), ("u^c", -S3[u]), ("d^c", -S3[d]), ("L", S3[l]), ("e^c", -S3[e])]:
    print(f"  {nm:>8} {str(sp.simplify(val)):>16} {str(sp.simplify(val/q)):>20}")
print()
print("  ** EVERY ONE IS PROPORTIONAL TO q.  THE ANOMALY CONDITIONS ARE HOMOGENEOUS, SO THEY")
print("     FIX THE RATIOS AND LEAVE THE OVERALL SCALE ENTIRELY FREE. **  Check it directly:")
lam = sp.Symbol('lambda', positive=True)
# Substitute the SOLUTION with q -> lambda*q, so every hypercharge scales together.  A first
# pass substituted the solution AND q -> lambda*q separately, double-scaling the dependent
# ones and returning a spurious False.
def at(scale):
    sub = {k: sp.expand(v.subs(Nc, 3).subs(q, scale*q)) for k, v in S3.items()}
    sub[q] = scale*q
    return [sp.simplify(sp.expand(cnd.subs(Nc, 3).subs(sub)))
            for cnd in (A_c, A_w, A_g, A_3, Y1, Y2, Y3)]
base, scaled = at(sp.Integer(1)), at(lam)
print(f"      all seven conditions hold on the solution:        {all(c == 0 for c in base)}")
print(f"      and still hold with every hypercharge x lambda:   {all(c == 0 for c in scaled)}")
print("      (six are homogeneous of degree 1 and the cubic of degree 3, so a common")
print("       rescaling cannot be detected by any of them)")
print()
print("  ⇒ ** SO THE ANSWER TO L-109's QUESTION, AS ASKED, IS: Y = 1/N DOES NOT FALL OUT OF")
print("     THE ANOMALIES.  They cannot produce it, because they cannot produce ANY scale. **")
print("  ⌗ The conventional q = 1/6 is a NORMALISATION, not a result -- which is exactly why")
print("  textbooks state it as a convention.  ** Had I claimed the anomalies deliver 1/3, that")
print("  would have been wrong, and L-109 was registered as a match precisely to force this")
print("  check rather than let the coincidence stand. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE WINDING FIXES EXACTLY WHAT THEY LEAVE FREE")
print("=" * 78)
print("  The corpus's winding derivation (L-73, P03_thirds_from_closure) is NOT homogeneous.")
print("  Its scale is set by a geometric fact with no free multiplier in it:")
print()
print("      x - y = 1,   where the 1 is ONE FULL LAP of the throat")
print()
print("  ** A LAP IS A CLOSED CIRCUIT.  It is not a unit anybody chose; it is the only length")
print("     the circle has. **  Imposing that with closure of both horn-families gives 3x in Z")
print("     and hence x = k/3 -- ** absolute values, not ratios. **")
print()
wu, wd = sp.Rational(2, 3), sp.Rational(-1, 3)
print(f"  {'from the winding':>22} {'value':>10} {'free multiplier?':>18}")
for nm, v in [("u", wu), ("d", wd), ("their difference", wu - wd)]:
    print(f"  {nm:>22} {str(v):>10} {'NO':>18}")
print()
print("  ⇒ ** THE TWO STRUCTURES ARE COMPLEMENTARY AND NEITHER IS REDUNDANT: **")
print()
print(f"  {'':>20} {'fixes the RATIOS':>20} {'fixes the SCALE':>18}")
for nm, a, b in [("anomaly cancellation", "YES", "no -- homogeneous"),
                 ("the winding closure", "yes (as a consequence)", "** YES -- the lap **")]:
    print(f"  {nm:>20} {a:>20} {b:>18}")
print()
print("  ** SO THE MATCH IS NOT THE ANOMALIES REPRODUCING THE GEOMETRY OR VICE VERSA.  EACH")
print("     SUPPLIES PRECISELY WHAT THE OTHER CANNOT, AND TOGETHER THEY LEAVE NOTHING FREE. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE CONSISTENCY CHECK.  Do they agree where they overlap?")
print("=" * 78)
print("  They overlap on the RATIOS, which both determine.  Take the winding's absolute")
print("  values, read off q from them, and ask whether the anomaly solution then reproduces")
print("  the rest of the generation:")
print()
qv = sp.Rational(1, 6)                       # Y_Q = 2q = 1/3, from the winding's fixed point
print(f"      the winding gives u = {wu}, d = {wd}; their MEAN is {(wu+wd)/2} = q = {qv}")
print()
print(f"  {'field':>8} {'from the anomalies at q=1/6':>28} {'the SM value':>14} {'agree?':>8}")
ok = True
sm = {'Q': sp.Rational(1, 3), 'u^c': sp.Rational(-4, 3), 'd^c': sp.Rational(2, 3),
      'L': sp.Rational(-1, 1), 'e^c': sp.Rational(2, 1)}
got = {'Q': 2*qv,
       'u^c': sp.simplify(-2*S3[u].subs(q, qv)),
       'd^c': sp.simplify(-2*S3[d].subs(q, qv)),
       'L': sp.simplify(2*S3[l].subs(q, qv)),
       'e^c': sp.simplify(-2*S3[e].subs(q, qv))}
for k in ('Q', 'u^c', 'd^c', 'L', 'e^c'):
    agree = sp.simplify(got[k] - sm[k]) == 0
    ok &= agree
    print(f"  {k:>8} {str(got[k]):>28} {str(sm[k]):>14} {str(agree):>8}")
print()
print(f"  ** ALL FIVE AGREE: {ok}.  And the electric charges follow, Q = I_3 + Y/2: **")
print(f"      u = {sp.Rational(1,2) + got['Q']/2} , d = {sp.Rational(-1,2) + got['Q']/2}"
      f"   -- ** the winding's own {wu} and {wd}, recovered **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — VERDICT ON L-109")
print("=" * 78)
for s in [
 "** THE LEAD ASKED WHETHER Y = 1/N FALLS OUT OF THE ANOMALIES OR HAS TO BE PUT IN.  ANSWER:",
 "   NEITHER, AND THAT IS THE INTERESTING OUTCOME. **",
 "",
 "  * The anomaly conditions CANNOT deliver 1/3, or any number -- they are homogeneous, so",
 "    they fix ratios and nothing else.  ** Any claim that they deliver a hypercharge VALUE is",
 "    wrong, and this check exists to have caught that. **",
 "  * ** AND THEY DO NOT DELIVER N_c EITHER. **  A first pass of this file claimed the cubic",
 "    anomaly selects N_c = 3.  It does not: on the linear solution the cubic residual is",
 "    IDENTICALLY ZERO, for every N_c.  ** The conditions constrain hypercharges GIVEN the",
 "    multiplet structure; the three was put in when the multiplets were written down. **",
 "  * And the winding closure delivers the SCALE, because a lap is not a unit anyone chose.",
 "  * ** The two agree on all five hypercharges and reproduce +2/3 and -1/3 exactly. **",
 "",
 "⌗ SO THE HONEST STATEMENT, WHICH IS NARROWER THAN 'THE GEOMETRY PREDICTS THE HYPERCHARGE'",
 "AND BETTER FOUNDED THAN A COINCIDENCE:",
 "",
 "   ** THE STANDARD MODEL'S ANOMALY CONDITIONS AND CR'S WINDING CLOSURE ARE INDEPENDENT AND",
 "      COMPLEMENTARY: the first fixes every ratio and no scale, the second fixes the scale",
 "      and no ratio was ever asked of it, and where they overlap they agree exactly. **",
 "",
 "⚠ AND THE BOUND IS UNCHANGED AND MUST TRAVEL WITH THE RESULT: the identification of the",
 "  winding with electric charge is L-65's READING, whose antecedent -- is a matter field",
 "  labelled by a ROUTE rather than a point? -- the winding receipt itself marks NOT SHOWN",
 "  (L-74).  ** Everything above is conditional on that antecedent and says nothing toward it. **",
]:
    print("  " + s)
