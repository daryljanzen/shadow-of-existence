#!/usr/bin/env python3
"""
L-16w — THE FIVE 're-run at general $D$' LEADS, WORKED AS ONE FILE, because four of them turn out
to be consequences of a single fact and the fifth is the control that shows the fact is doing work.

  `L-16`  the equianharmonic value is dimension-selected.  Does the CM-by-$\\omega$ structure have
          a dimensional reason?
  `L-19`  what IS the ringdown shape at general $D$?  `O6` was shown non-constant; the actual
          $D$-dependence was never computed.
  `L-20`  the $+2$ isotropy enhancement at a degenerate horizon holds in every $D$.  A general
          theorem, or a CR fact?
  `L-21`  `X5`'s check at higher $D$ is a LARGER check -- $S_{D-1}$ needs $D-2$ transpositions.
  `L-23`  $\\mathrm{Aut}(A_2)=S_3\\times\\mathbb{Z}_2$ factorises at one dimension.  Does that give
          the gauged/global split a REASON rather than a description?

** THE ONE FACT: AT ODD $D$ THE HORIZON POLYNOMIAL IS EVEN IN $r$.  That already accounts for the
missing mass parity and for $-r_0$ lying in the root set; here it accounts for two more things,
and neither was known to be the same fact. **

  PART 1  ** `L-19`, ANSWERED EXACTLY: $\\lambda^2/\\Omega_c^2 = D-3$, for every $M$ and every
          $\\alpha$.  So the $M$-independence is NOT four-dimensional -- what is four-dimensional
          is the value being ONE. **
  PART 2  ** `L-21`: the check at $D=5$ is not larger, it is IMPOSSIBLE. **
  PART 3  ** `L-23`: at $D=5$ there is no $A_2$ to take the automorphisms of, and the direction of
          explanation was backwards anyway. **
  PART 4  ** `L-16`: the equianharmonic value is the cross-ratio whose stabiliser is $\\mathbb{Z}_3$
          -- and it is the WRONG three for the bridge the lead wanted. **
  PART 5  ** `L-20`: THE CONTROL.  This one is NOT dimension-selected, and showing so is what
          keeps the other four from being a pattern imposed. **
  PART 6  The five strikes, and the one fact.

Run: python3 L016w_the_dimension_cluster.py      (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])
r, M, al = sp.symbols('r M alpha', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — `L-19`: THE EIKONAL RATIO AT GENERAL D, EXACTLY")
print("=" * 78)
print("  `O6`: *'the identity $2f - r^2 f'' \\equiv 2$ for every $r$ and every $M$, so")
print("  $\\lambda^2-\\Omega_c^2 \\equiv 0$'* -- established at $D=4$.  First, the identity at general D:")
print()
HDR = "2f - r^2 f''"
print(f"  {'D':>3} {HDR:>26} {'the coefficient':>26}")
for D in range(4, 9):
    f = 1 - 2*M/r**(D-3) - r**2/al**2
    idn = sp.simplify(sp.expand(2*f - r**2*sp.diff(f, r, 2)))
    coef = sp.expand((D-3)*(D-2) - 2)
    print(f"  {D:>3} {str(idn):>26} {f'(D-3)(D-2)-2 = {coef}':>26}")
    assert sp.simplify(idn - (2 + 2*M*((D-3)*(D-2)-2)*r**(-(D-3)))) == 0
print()
Dd = sp.Symbol('D')
print(f"  and the coefficient factors: (D-3)(D-2)-2 = {sp.factor(sp.expand((Dd-3)*(Dd-2)-2))}")
assert sp.expand((Dd-3)*(Dd-2)-2 - (Dd-1)*(Dd-4)) == 0
print("  ** so it vanishes exactly at D = 4 (and at the vacuous D = 1). **")
print()
print("  Now the ratio itself.  Photon sphere at r f' = 2f; Omega_c^2 = f_c / r_c^2;")
print("  lambda^2 = -(r_c^2 f_c / 2) (f/r^2)''|_{r_c}.  Computed, not quoted:")
print()
print(f"  {'D':>3} {'r_c':>22} {'lambda^2 / Omega_c^2':>22} {'lambda / Omega_c':>18}")
for D in range(4, 10):
    f = 1 - 2*M/r**(D-3) - r**2/al**2
    g = sp.simplify(f/r**2)
    rc = [x for x in sp.solve(sp.Eq(sp.simplify(r*sp.diff(f, r) - 2*f), 0), r)
          if x.is_real is not False][0]
    fc = sp.simplify(f.subs(r, rc))
    lam2 = sp.simplify(-(rc**2*fc/2)*sp.simplify(sp.diff(g, r, 2).subs(r, rc)))
    Om2 = sp.simplify(fc/rc**2)
    ratio = sp.simplify(sp.radsimp(lam2/Om2))
    print(f"  {D:>3} {str(sp.simplify(rc)):>22} {str(ratio):>22} "
          f"{str(sp.sqrt(ratio)):>18}")
    assert sp.simplify(ratio - (D - 3)) == 0
print()
for s in [
 "⇒⇒ ** $\\lambda^2/\\Omega_c^2 = D-3$ EXACTLY, ASSERTED AT SIX DIMENSIONS, AND IT IS INDEPENDENT",
 "   OF BOTH $M$ AND $\\alpha$ AT EVERY $D$. **",
 "",
 "⌗ *And the reason is one line: the photon-sphere condition gives $M r_c^{-(D-3)} = 1/(D-1)$, so",
 "the identity's excess $2M[(D-3)(D-2)-2]r_c^{-(D-3)}$ becomes $2(D-1)(D-4)/(D-1) = 2(D-4)$, and",
 "$\\lambda^2-\\Omega_c^2 = (D-4)\\Omega_c^2$.*",
 "",
 "⚠⚠ ** SO THE CORPUS'S READING OF `O6` NEEDS ONE WORD CHANGED, AND IT IS THE WORD THE LEAD WAS",
 "   ASKING ABOUT. **  *The eikonal quality factor's independence of $M$ and $\\alpha$ was recorded",
 "   as resting on the $D=4$ identity.  ** It does not: the quality factor is",
 "   $\\ell/[\\sqrt{D-3}\\,(n+\\tfrac12)]$ in EVERY dimension, always $M$- and $\\alpha$-free.  What is",
 "   four-dimensional is not the independence but the VALUE: $\\lambda = \\Omega_c$ exactly at",
 "   $D=4$. ***",
 "",
 "⌗ *`L-19` asked for $\\Omega_c/\\lambda$ at $D=5,6$ and the answers are $1/\\sqrt2$ and $1/\\sqrt3$;",
 "the lead is discharged by a closed form rather than by two numbers.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — `L-21`: THE CHECK AT D=5 IS NOT LARGER, IT IS IMPOSSIBLE")
print("=" * 78)
print("  `X5`: P5's deck group is $S_3$ *'generated by the monodromies about the branch points'*,")
print("  and two transpositions generate $S_3$ only if they DIFFER -- computed, $(0\\,2)$ and")
print("  $(1\\,2)$, order six.  `L-21`: at $D=5$ the analogue needs $S_4$ and three transpositions.")
print()
print(f"  {'D':>3} {'the horizon polynomial in 2M':>34} {'even in r?':>11}")
for D in range(4, 9):
    P = sp.expand(r**(D-1) - r**(D-3) + 2*M)
    ev = sp.simplify(sp.expand(P.subs(r, -r) - P)) == 0
    print(f"  {D:>3} {str(P):>34} {str(ev):>11}")
    assert ev == (D % 2 == 1)
print()
S4 = list(itertools.permutations(range(4)))
inv = (1, 0, 3, 2)


def comp(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


cent = [p for p in S4 if comp(p, inv) == comp(inv, p)]
print(f"  At D=5 the root set is stable under r -> -r with no fixed root (r=0 is a root only at")
print(f"  2M=0), so the involution is FIXED-POINT-FREE and the monodromy COMMUTES with it.")
print(f"     |S_4| = {len(S4)},   |centraliser of (0 1)(2 3) in S_4| = {len(cent)}")
assert len(S4) == 24 and len(cent) == 8
print()
for s in [
 "⇒⇒ ** SO AT $D=5$ THE MONODROMY GROUP IS CONTAINED IN A GROUP OF ORDER EIGHT AND CANNOT BE",
 "   $S_4$, WHICH HAS ORDER TWENTY-FOUR.  `L-21`'s 'larger check' does not exist: the structure",
 "   it would check is absent. **",
 "",
 "⌗ ** AND THE REASON IS THE EVENNESS -- THE SAME ONE THAT REMOVES THE MASS PARITY AND PUTS",
 "   $-r_0$ IN THE ROOT SET. **  *Three consequences, one fact, and this is the first time they",
 "   have been on the same page.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-23`: THERE IS NO $A_2$ AT FIVE, AND THE ARROW POINTED THE WRONG WAY")
print("=" * 78)
print(f"  {'D':>3} {'roots':>7} {'sum of roots':>13} {'structure of the root set':>34}")
for D in range(4, 8):
    P = sp.Poly(r**(D-1) - r**(D-3) + 2*M, r)
    cs = P.all_coeffs()
    s_ = -cs[1]/cs[0]
    shape = ("+/- PAIRED (even polynomial)" if D % 2 else "no pairing (odd polynomial)")
    print(f"  {D:>3} {D-1:>7} {str(sp.simplify(s_)):>13} {shape:>34}")
print()
for s in [
 "⇒ ** AT $D=4$: THREE roots summing to zero -- the $A_2$ skeleton.  AT $D=5$: FOUR roots summing",
 "   to zero IN $\\pm$ PAIRS -- $\\{\\pm a, \\pm b\\}$, which is not $A_2$ and is not $A_3$ either. **",
 "",
 "⇒⇒ ** SO `L-23`'s TEST -- 'what does the factorisation's failure at $D=5$ do to the split?' --",
 "   HAS NO SUBJECT: at five there is no $A_2$ to take $\\mathrm{Aut}$ of, so the factorisation",
 "   does not fail, it does not arise. **",
 "",
 "⌗⌗ ** AND THE QUESTION'S ARROW POINTS THE WRONG WAY, WHICH IS THE PART WORTH KEEPING. **  It",
 "   asks whether the factorisation gives the gauged/global split a REASON.  *`L8.3` already",
 "   supplies the reason and it is not dimensional: the residue factorises because ON and TANGENT",
 "   are **independent relations to one circle**, a ruling being a line of the substrate (a",
 "   motion, hence gauged) and a root labelling a different cut (solution space, hence global).*",
 "   ** The split explains the factorisation; the factorisation does not explain the split. **",
 "",
 "⌗ *What IS dimension-selected is the EXISTENCE of the $\\mathbb{Z}_2$ factor -- even $D$ -- and",
 "c54.82 supplies its mechanism.  ** An existence condition on a factor is not a reason for the",
 "product, and conflating the two is what the lead was doing. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-16`: THE EQUIANHARMONIC VALUE'S THREE IS THE WRONG THREE")
print("=" * 78)
lam = sp.Symbol('lambda')
ANH = [lam, 1 - lam, 1/lam, 1/(1 - lam), lam/(lam - 1), (lam - 1)/lam]
print("  The anharmonic group is the $S_3$ acting on a cross-ratio.  Its six values:")
print(f"     {[str(sp.simplify(v)) for v in ANH]}")
print()
print(f"  {'special value':>20} {'stabiliser order':>18} {'orbit size':>11} {'stabiliser is':>16}")
for nm, vals in (("equianharmonic", sp.solve(sp.Eq(lam**2 - lam + 1, 0), lam)),
                 ("harmonic", [sp.Integer(-1), sp.Integer(2), sp.Rational(1, 2)])):
    v0 = vals[0]
    orb = {sp.nsimplify(sp.simplify(x.subs(lam, v0))) for x in ANH}
    st = 6 // len(orb)
    print(f"  {nm:>20} {st:>18} {len(orb):>11} "
          f"{('** Z_3, the 3-cycle **' if st == 3 else 'Z_2, a transposition'):>16}")
    if nm == "equianharmonic":
        assert st == 3 and len(orb) == 2
    else:
        assert st == 2 and len(orb) == 3
print()
for s in [
 "⇒ ** SO THE EQUIANHARMONIC VALUE IS EXACTLY THE CROSS-RATIO WHOSE STABILISER IN THE VANTAGE",
 "   $S_3$ IS THE $\\mathbb{Z}_3$, AND ITS THREE-FOLDNESS IS THAT STABILISER -- not a coincidence",
 "   of complex multiplication. **  ** `L-16`'s 'is it dimension-selected' is therefore YES, and",
 "   trivially so: the vantage $S_3$ exists because the vantages number three, which is $D-1=3$. **",
 "",
 "⇒⇒ ** AND THAT IS THE WRONG THREE FOR THE BRIDGE THE LEAD WANTED. **  *The stabiliser lives in",
 "   the VANTAGE $S_3$ -- the hinge three, which P14 `sec:whichthree` assigns to the WITHIN-STATE",
 "   index -- while the deck action's $\\mathbb{Z}_3$ is the TURNAROUND's, and `lem:twoturnings`",
 "   proves no affine change of variable identifies the two root sets.*",
 "",
 "⌗ ** AND THE CORPUS ALREADY HAD THE OTHER HALF: `PHASE8` records that the $j=0$ curve is the",
 "   DOUBLE cover branched at four points while `sec:deck`'s is THREE-sheeted over the $2M$-plane",
 "   branched at two -- 'a different degree over a different base with a different branch set'. **",
 "   *So both routes from CM-by-$\\omega$ to the deck $\\mathbb{Z}_3$ are closed, and by unrelated",
 "   arguments: the cover is wrong, and the three is the other three.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-20`: THE CONTROL.  NOT DIMENSION-SELECTED.")
print("=" * 78)
print("  A degenerate horizon is a DOUBLE zero of f, so near it f = c(r-r_h)^2 + O((r-r_h)^3).")
print("  The two-dimensional (t, r) block is then, with x = r - r_h:")
print()
t_, x_ = sp.symbols('t x', real=True)
cc = sp.Symbol('c', positive=True)
ff = cc*x_**2
gm = sp.Matrix([[-ff, 0], [0, 1/ff]])
co = [t_, x_]
gi = gm.inv()


def Gam(a, b, cn):
    return sp.simplify(sum(gi[a, d]*(sp.diff(gm[d, b], co[cn]) + sp.diff(gm[d, cn], co[b])
                                     - sp.diff(gm[b, cn], co[d])) for d in range(2))/2)


G = [[[Gam(a, b, cn) for cn in range(2)] for b in range(2)] for a in range(2)]


def Ric(b, d):
    s_ = 0
    for a in range(2):
        s_ += sp.diff(G[a][b][d], co[a]) - sp.diff(G[a][b][a], co[d])
        for e in range(2):
            s_ += G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a]
    return sp.simplify(s_)


Rs = sp.simplify(sum(gi[b, d]*Ric(b, d) for b in range(2) for d in range(2)))
print(f"     ds^2 = -c x^2 dt^2 + dx^2/(c x^2)      Ricci scalar = {Rs}")
assert sp.simplify(Rs + 2*cc) == 0
print()
print(f"  ** CONSTANT AND NEGATIVE: it is AdS_2, of radius^2 = 2/c. **")
print(f"  A maximally symmetric space of dimension n has n(n+1)/2 Killing vectors; "
      f"n=2 gives {2*3//2}.")
print(f"  The non-degenerate case has only the single time translation: 1.")
print(f"     enhancement = {2*3//2} - 1 = ** {2*3//2 - 1} **")
assert 2*3//2 - 1 == 2
print()
for s in [
 "⇒⇒ ** AND NOTHING IN THAT ARGUMENT MENTIONS $D$.  The near-horizon block is TWO-DIMENSIONAL in",
 "   every dimension, so a maximally symmetric two-space always has three Killing vectors and the",
 "   enhancement is always $3-1=2$.  ** `L-20`'s answer is: A GENERAL THEOREM ABOUT DEGENERATE",
 "   HORIZONS, NOT A CR FACT. **",
 "",
 "⌗ ** AND ITS $\\so(2,1)$ IS THE BOOST PAIR, WHICH IS THE CHECK THE LEAD ASKED FOR: the three are",
 "   the $AdS_2$ translation, dilatation and special conformal, i.e. $\\mathfrak{sl}(2,\\mathbb{R})$",
 "   -- and the two ADDED to $\\mathbb{R}_t$ are exactly the pair that fails to be Killing away",
 "   from degeneracy. **",
 "",
 "⌗⌗ ** WHY THIS ONE MATTERS MORE THAN THE OTHER FOUR: it is the CONTROL.  Four of these five",
 "   leads turn out to be dimension-selected and this one turns out not to be -- so the pattern",
 "   is being read off the computations rather than imposed on them. **  *A cluster in which",
 "   everything came out the same way would be evidence about the reader.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE FIVE STRIKES, AND THE ONE FACT")
print("=" * 78)
print(f"  {'lead':>7} {'disposal':>13} {'answer':>48}")
for a, b, c in [
    ("L-16", "** STRIKE **", "yes, and it is the vantage three, not the deck's"),
    ("L-19", "** STRIKE **", "lambda^2/Omega_c^2 = D-3, exactly, for all M, alpha"),
    ("L-20", "** STRIKE **", "general theorem: AdS_2, hence +2 in every D"),
    ("L-21", "** STRIKE **", "impossible at five: monodromy is imprimitive"),
    ("L-23", "** STRIKE **", "no A_2 at five, and the arrow pointed backwards"),
]:
    print(f"  {a:>7} {b:>13} {c:>48}")
print()
for s in [
 "⌗⌗ ** THE ONE FACT, STATED ONCE: AT ODD $D$ THE HORIZON POLYNOMIAL IS EVEN IN $r$, AND FOUR",
 "   SEPARATE STRUCTURES FAIL AT ODD $D$ BECAUSE OF IT: **",
 "     ① the mass function is even, so there is no $\\gamma^5$ and no mass-reflection $\\mathbb{Z}_2$",
 "     ② $-r_0$ lies in the geometry's OWN root set, so the parity has nothing to relate",
 "     ③ the monodromy commutes with a fixed-point-free involution, so it cannot be $S_{D-1}$",
 "     ④ the root set is $\\pm$-paired, so it is not an $A_2$-type zero-sum triple",
 "   ** Three of those four were reached in three different revisions for three different leads,",
 "   and none of them named the evenness. **",
 "",
 "⚠ *And `L-19` is the odd one out and is worth keeping separate: its selection of $D=4$ runs",
 "through $(D-1)(D-4)$ and has nothing to do with parity.  ** Two independent dimension",
 "selections, and it would have been easy to file them as one. ***",
]:
    print("  " + s)
