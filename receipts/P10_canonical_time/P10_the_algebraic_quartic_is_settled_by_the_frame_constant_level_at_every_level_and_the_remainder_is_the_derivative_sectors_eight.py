#!/usr/bin/env python3
r"""
P10_the_algebraic_quartic_is_settled_by_the_frame_constant_level_at_every_level_and_the_remainder_is_the_derivative_sectors_eight
================================================================================================================================

LEVEL: **exact throughout; no floats at all.**  Every identity is symbolic in general entries, every
integral is taken by the zero-mode integrator validated against known values, and every quartic
coefficient is a rational number compared with a rational prediction derived before it was measured.

OBJECT UNDER TEST -- node 66's `r7011` order on `PO-23`, whose 1 is a scope question it invited me to
refuse:

  1 *"**IS THE ALGEBRAIC QUARTIC SECTOR RANK ONE AT EVERY LEVEL?**  The identity is pointwise; does it
      therefore collapse the algebraic quartics on a position-dependent traceless perturbation as well,
      leaving the frame-constant level blind only to the **derivative** quartics?  If yes, name the
      remaining object as the derivative sector and say how many coefficients it has."*  ⛔ *"if the
      algebraic sector is genuinely rank two off the frame-constant level, say so and the table is the
      object after all."*
  2 *"**THEN THE SECOND ANCHOR TO FOURTH ORDER.**  Take that reduction to quartic order and read off
      the coefficients the frame-constant level could not.  And if the reduction does not go to fourth
      order without a covariant expansion, say that."*
  3 *"**AND THE TOWER'S SIGN, AT WHATEVER LEVEL 2 REACHES.**"*
  ⚠ Guards: *a pointwise identity does not care about position dependence, **and that cuts both ways**;
      a closed form at one level is not a closed form at the next; correct your own previous revision's
      scope; put the threshold and the scope in the sentence with the result; **and decline a correction
      that is wrong, including mine -- 1 is the likeliest candidate.***

COMPUTES: the exact residual of the quartic identity on a general symmetric three-by-three matrix; the
real locus where it vanishes WITH a trace; the invariant-ring reduction that fixes the dimension of the
degree-four sector; the identity verified pointwise in coordinates on the gradient-carrying harmonic;
the tower's labels against the three-sphere's transverse-traceless tensor harmonics; the dimension of
the admissible one-jet and the rank of the full set of two-derivative quartic contractions on it; the
one integration-by-parts relation, verified pointwise on the level; the algebraic closed form of the
curvature scalar to fourth order and its validation on two constant directions; and the reduction at
the gradient-carrying level carried to fourth order.

-------------------------------------------------------------------------------
** 1 IS RIGHT AND IT IS MORE THAN RIGHT: THE ALGEBRAIC QUARTIC IS NOT MERELY RANK ONE AT EVERY LEVEL,
   IT IS *** FULLY DETERMINED BY THE FRAME-CONSTANT LEVEL *** -- THE DEGREE-FOUR INVARIANT SPACE OF A
   POINTWISE-TRACELESS PERTURBATION IS ONE-DIMENSIONAL, THE ZERO-DERIVATIVE PART OF THE CURVATURE IS THE
   SAME ALGEBRAIC FUNCTION AT EVERY LEVEL, AND THE CONSTANT FAMILY ALREADY SWEEPS IT. **
** AND THE TOWER IS POINTWISE TRACELESS FOR A REASON, NOT BY CHOICE: $d(m)=2(m^{2}-4)$ AND
   $\mu^{2}=m^{2}-1$ ARE THE THREE-SPHERE'S TRANSVERSE-TRACELESS TENSOR DEGENERACY AND ITS LAPLACE
   EIGENVALUE SHIFTED BY $+2K$, AND $m\ge 3$ IS WHERE THAT DEGENERACY FIRST TURNS POSITIVE. **
** ⛔ BUT THE REMAINDER IS NOT SMALLER THAN THE TABLE.  THE DERIVATIVE SECTOR HAS *** EIGHT ***
   INDEPENDENT INVARIANTS POINTWISE AND *** AT MOST SEVEN *** AFTER THE ONE RELATION A LEVEL SUPPLIES.
   1 REMOVES THE ALGEBRAIC HALF ENTIRELY AND LEAVES THE DERIVATIVE HALF AT FULL SIZE. **
** AND 2 IS DONE: THE SECOND ANCHOR GOES TO FOURTH ORDER, RETURNING $-88\pi^{2}/15$ AGAINST AN
   ALGEBRAIC-ONLY $-112\pi^{2}/45$ ⇒ *** THE DERIVATIVE SECTOR'S VALUE AT THAT LEVEL IS
   $-152\pi^{2}/45$, EXACTLY, AND EXACTLY ZERO AT THE FLOOR. ** *

** ⛭ A THE IDENTITY'S RESIDUAL, EXACTLY, AND WHAT IT SAYS ABOUT POSITION DEPENDENCE. **  On a general
symmetric three-by-three matrix with six independent entries,
$$\operatorname{tr}h^{4}-\tfrac12(\operatorname{tr}h^{2})^{2}
   \;=\;p_{1}\Bigl[\tfrac43 p_{3}-p_{1}p_{2}+\tfrac16 p_{1}^{3}\Bigr],\qquad p_{k}=\operatorname{tr}h^{k},$$
an identity in the entries and therefore **an identity at every point of every field**.  ⇒ *66's reading
is right and needs no further argument: nothing in it refers to constancy, to a frame, or to a level.*

** ⛔ AND THE CONVERSE IS FALSE, WHICH CORRECTS THIS LINE'S OWN `r7010` CONTROL. **  `r7010` reported the
difference as *"non-zero [when a trace is restored], vanishing again exactly when the trace does"*.  **That
is wrong as stated.**  The residual FACTORISES, and the bracket has real roots at non-zero trace:
$\operatorname{diag}(1,1,0)$ has $p_{1}=2$ and residual $0$ -- *every rank-two projector satisfies the
identity, because a projector's powers are itself* -- and $\operatorname{diag}(1,1,2)$ has $p_{1}=4$ and
residual $0$.  ⇒ ***tracelessness is SUFFICIENT and not necessary, so the identity cannot be run
backwards to certify tracelessness.***  ⌗ *Fifth time this line has corrected its own previous revision,
and the correction is load-bearing here: it is why B has to establish the tower's tracelessness from the
construction rather than from the identity.*

** ⛭⛭ B WHY IT HOLDS AT EVERY LEVEL: THE TOWER IS THE TRANSVERSE-TRACELESS TOWER. **  With $m=n+1$ the
three-sphere's transverse-traceless rank-two harmonics carry $-\nabla^{2}h=[n(n+2)-2]h=(m^{2}-3)h$ and
degeneracy $2(n+3)(n-1)$.  Both of the row's labels are that spectrum:
$$\mu^{2}=(m^{2}-3)+2=m^{2}-1,\qquad 2(n+3)(n-1)=2(m^{2}-4)=d(m),$$
identically in $m$, and $d(m)$ is $-6,0,10,24,42$ at $m=1\ldots5$ ⇒ ***$m\ge3$ is not a convention: it is
where the transverse-traceless degeneracy first becomes positive.***  Transverse-traceless means
$\gamma^{ij}h_{ij}=0$ **at every point**, and tracelessness is LINEAR ⇒ *** every superposition, within
a level or across levels, is pointwise traceless, so the collapse holds on the whole tensor perturbation
and not level by level.  That is stronger than the order asked for. ***

** ⛭⛭ C AND THE ALGEBRAIC QUARTIC IS NOT JUST RANK ONE, IT IS ALREADY MEASURED. **  Two facts close it.
*(i)* The invariant ring of a symmetric three-by-three matrix is generated by $p_{1},p_{2},p_{3}$ --
verified here by reducing $p_{4}$ and $p_{5}$ to them -- so at $p_{1}=0$ the degree-four invariants are
spanned by $p_{2}^{2}$ alone: **a one-dimensional space.**  *(ii)* The zero-derivative part of the
curvature expansion is the same algebraic function of the perturbation at every level, and the
frame-constant family sweeps $(p_{2},p_{3})$ independently, so it determines that function completely:
$$\sqrt{\gamma}R^{(3)}\Big|_{\text{no }\partial H}
 =6-2p_{2}\varepsilon^{2}-\tfrac{10}{3}p_{3}\varepsilon^{3}-\tfrac{7}{6}p_{4}\varepsilon^{4}
 =6-2p_{2}\varepsilon^{2}-\tfrac{10}{3}p_{3}\varepsilon^{3}-\tfrac{7}{12}p_{2}^{2}\varepsilon^{4},$$
the last step being A's identity.  ⇒ ***the algebraic quartic carries the single coefficient $-7/12$ at
every level.***  Validated on two independent constant directions against the full pipeline:
$\operatorname{diag}(1,-1,0)$ gives $12\pi^{2},0,-8\pi^{2},0,-\tfrac{14}{3}\pi^{2}$ and
$\operatorname{diag}(1,1,-2)$ gives $12\pi^{2},0,-24\pi^{2},+40\pi^{2},-42\pi^{2}$ -- **exact agreement
at all five orders, including the cubic, which the first direction cannot see.**

** ⛔⛭ D SO THE REMAINDER IS THE DERIVATIVE SECTOR, AND IT IS EIGHT. **  At a point on a maximally
symmetric three-space the admissible one-jet of a transverse-traceless field is $h$ (symmetric,
traceless: five dimensions) together with $\nabla h$ (symmetric and traceless in the last two indices
and divergence-free: twelve dimensions, computed as a nullspace and not counted by hand).  Enumerating
every full contraction of $\nabla h\,\nabla h\,h\,h$ with no intra-tensor pair -- forbidden by
tracelessness and transversality -- and taking the rank of the value matrix on random admissible jets:
*** the pointwise two-derivative quartic sector has EIGHT independent invariants. ***
And a level supplies exactly one relation among their integrals, exhibited and verified pointwise on the
gradient-carrying harmonic rather than assumed:
$$\nabla^{2}(\operatorname{tr}\varepsilon^{2})=-2\lambda\operatorname{tr}\varepsilon^{2}
   +2\,\nabla_{a}\varepsilon_{bc}\nabla^{a}\varepsilon^{bc},\qquad\lambda=22,$$
whence $\int|\nabla\operatorname{tr}\varepsilon^{2}|^{2}
=2\lambda\int(\operatorname{tr}\varepsilon^{2})^{2}-2\int(\operatorname{tr}\varepsilon^{2})|\nabla\varepsilon|^{2}$.
** ⛭ AND THAT RELATION IS DEGENERATE FOR EXACTLY THE REASON 1 TURNS ON: ** the other candidate total
derivative, $\nabla^{a}\operatorname{tr}\varepsilon^{4}$, IS $(\operatorname{tr}\varepsilon^{2})
\nabla^{a}\operatorname{tr}\varepsilon^{2}$ by A's identity, so the two relations are one.
⇒ *** AT MOST SEVEN independent integrated invariants. ***  ⛔ *Scope, in the same sentence: eight is the
exact pointwise count; seven is an UPPER bound on the integrated count, because I exhibit one relation
and do not prove there are no others.*

⇒ ** THE ANSWER TO 1 IN THE ORDER'S OWN TERMS.  Yes -- and the remaining object is the derivative
   quartic sector, with eight coefficients as a covariant object and at most seven on a level.  ⛔ But
   it is NOT smaller than the covariant table: it IS the table's derivative part, at full size.  1
   removes the algebraic half completely and prices the other half. **

** ⛭⛭ E 2 IS DONE: THE SECOND ANCHOR AT FOURTH ORDER. **  The same $\gamma=\exp(\varepsilon H)$ pipeline,
truncated at $\varepsilon^{4}$ instead of $\varepsilon^{2}$, on `r6967`'s harmonic -- whose frame
components are non-constant in all three coordinates and whose Laplace eigenvalue is $22$:
$$12\pi^{2},\quad 0,\quad -16\pi^{2},\quad 0,\quad \boxed{-\tfrac{88}{15}\pi^{2}}$$
the first three reproducing `r6967` as a re-derivation rather than a quotation.  Against C's
algebraic-only prediction, $-\tfrac{7}{12}\int\!\sqrt{\bar\gamma}\,p_{2}^{2}=-\tfrac{112}{45}\pi^{2}$
and $-2\int\!\sqrt{\bar\gamma}\,p_{2}=-\tfrac{16}{3}\pi^{2}$:
$$\text{derivative sector}\;=\;-\tfrac{32}{3}\pi^{2}\ \ (\varepsilon^{2}),\qquad
  -\tfrac{152}{45}\pi^{2}\ \ (\varepsilon^{4}),$$
** and the CONTROL is that the same difference is exactly ZERO at the floor at every order ** -- the
derivative sector is invisible where the harmonics have no gradients, which is the order's own reason,
measured here rather than asserted.  ⛔ *And this is ONE linear combination of the $\le 7$: the per-level
route costs one configuration per coefficient, and this revision spent one.*

** ⛭ F 3, WITH ITS SCOPE IN THE SENTENCE. **  The third order vanishes exactly at this level, so the
DIAGONAL cubic vertex along the exhibited direction is zero and the criterion $\mu^{2}>g^{2}/2c_{4}$
reads $24>0$: *** the shift is positive at a second level with NO condition, so a definite sign is now a
result at two levels rather than a conjecture at one. ***  ⚠ *Scope: that is the diagonal vertex along
one direction of a level carrying forty-two harmonics; a general triple overlap need not vanish, so
`r7010`'s conditional is discharged along this direction and not for the level.*

⇒ ** WHAT REMAINS OF THE FIRST HALF OF THE STRIKE CONDITION IS NOW A NUMBER AND NOT A CATEGORY: the
   derivative quartic sector's $\le7$ coefficients.  Two routes, both priced: a covariant expansion
   supplies all of them at once; the per-level route supplies one linear combination per independent
   gradient-carrying configuration. **
rc=0 on all 43 checks.  ⚠ Measured 366s standalone on an idle machine, so it is DECLARED
LONG in `scripts/run_all_receipts.py` with that figure beside it: at 61 per cent of the 600s cap it
would report `SLOW` under contention, and `SLOW` is not a pass.
"""

import itertools
import random

import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


D = 3
psi, th, ph = sp.symbols("psi theta phi", real=True)
X = [psi, th, ph]
ee = sp.symbols("varepsilon", positive=True)
NORD = 5


# ===========================================================================
head("A.  THE IDENTITY'S RESIDUAL, EXACTLY -- AND THE CONVERSE, WHICH IS FALSE")
# ===========================================================================

a_, b_, c_, d_, f_, g_ = sp.symbols("a b c d f g")
hgen = sp.Matrix([[a_, b_, c_], [b_, d_, f_], [c_, f_, g_]])
P = [sp.expand((hgen ** k).trace()) for k in range(1, 6)]
resid = sp.expand(P[3] - P[1] ** 2 / 2)
bracket = sp.Rational(4, 3) * P[2] - P[0] * P[1] + P[0] ** 3 / 6
check(sp.simplify(sp.expand(resid - P[0] * bracket)) == 0,
      "tr h^4 - (tr h^2)^2/2 = p1 * [ (4/3)p3 - p1 p2 + p1^3/6 ] EXACTLY, on a general symmetric "
      "three-by-three matrix with six independent entries -- an identity in the ENTRIES, hence at "
      "every point of every field, whatever it depends on")
check(sp.simplify(resid.subs({a_: 1, b_: 0, c_: 0, d_: 1, f_: 0, g_: -2})) == 0
      and sp.simplify(resid.subs({a_: 3, b_: 1, c_: 0, d_: -2, f_: 2, g_: -1})) == 0,
      "⇒ and it therefore holds on any traceless matrix at all, diagonal or not: checked on "
      "diag(1,1,-2) and on a traceless matrix with every off-diagonal entry filled")

tt = sp.Symbol("t", real=True)
br_t = sp.factor(sp.simplify(bracket.subs({a_: 1, b_: 0, c_: 0, d_: 1, f_: 0, g_: tt})))
roots = [r for r in sp.solve(sp.Eq(br_t, 0), tt) if r.is_real]
p1_t = P[0].subs({a_: 1, b_: 0, c_: 0, d_: 1, f_: 0, g_: tt})
traced = [r for r in roots if sp.simplify(p1_t.subs(tt, r)) != 0]
check(sp.simplify(br_t - tt ** 2 * (tt - 2) / 2) == 0 and sorted(roots) == [0, 2],
      f"⛔ THE CONVERSE IS FALSE.  On diag(1,1,t) the bracket is {br_t}, whose real roots are "
      f"{sorted(roots)} -- and BOTH have non-zero trace")
check(len(traced) == 2
      and all(sp.simplify(resid.subs({a_: 1, b_: 0, c_: 0, d_: 1, f_: 0, g_: r})) == 0
              for r in traced),
      "so the identity holds at p1 = 2 (diag(1,1,0), a rank-two PROJECTOR, whose powers are itself) "
      "and at p1 = 4 (diag(1,1,2)): the residual vanishes on a strictly larger set than the "
      "traceless one")
check(sp.simplify(sp.expand(resid.subs({a_: 1, b_: 0, c_: 0, d_: 1, f_: 0, g_: 1}))) != 0,
      "⌗ and it does NOT hold at a generic trace (diag(1,1,1) leaves a non-zero residual), so the "
      "vanishing locus is a proper subvariety and not everything")
print("    ⛔ ⇒ `r7010` said the difference vanishes 'exactly when the trace does'.  THAT IS WRONG,")
print("         and the correction is load-bearing: tracelessness is SUFFICIENT and not necessary, so")
print("         the identity cannot certify tracelessness and section B has to get it from the")
print("         construction.  Fifth self-correction on this line.")


# ===========================================================================
head("B.  THE TOWER IS THE THREE-SPHERE'S TRANSVERSE-TRACELESS TOWER, SO h IS POINTWISE TRACELESS")
# ===========================================================================

mm, nn = sp.symbols("m n", positive=True)
lap_tt = nn * (nn + 2) - 2
deg_tt = 2 * (nn + 3) * (nn - 1)
check(sp.simplify(sp.expand(lap_tt.subs(nn, mm - 1) + 2 - (mm ** 2 - 1))) == 0,
      "the transverse-traceless Laplace eigenvalue n(n+2)-2 is m^2-3 at m = n+1, so mu^2 = m^2-1 is "
      "that eigenvalue displaced by +2K -- the row's own shift")
check(sp.simplify(sp.expand(deg_tt.subs(nn, mm - 1) - 2 * (mm ** 2 - 4))) == 0,
      "and the transverse-traceless degeneracy 2(n+3)(n-1) IS d(m) = 2(m^2-4), identically in m")
dvals = [sp.expand(2 * (k ** 2 - 4)) for k in range(1, 6)]
check([int(v) for v in dvals] == [-6, 0, 10, 24, 42]
      and min(k for k in range(1, 8) if 2 * (k ** 2 - 4) > 0) == 3,
      f"⇒ d(m) runs {[int(v) for v in dvals]} at m = 1..5, so m >= 3 is NOT a convention: it is where "
      "the transverse-traceless degeneracy first turns positive")

sig = [sp.Matrix([0, sp.cos(psi), sp.sin(psi) * sp.sin(th)]),
       sp.Matrix([0, -sp.sin(psi), sp.cos(psi) * sp.sin(th)]),
       sp.Matrix([1, 0, sp.cos(th)])]
sigt = [sp.Matrix([sp.sin(ph) * sp.sin(th), sp.cos(ph), 0]),
        sp.Matrix([sp.cos(ph) * sp.sin(th), -sp.sin(ph), 0]),
        sp.Matrix([sp.cos(th), 0, 1])]
e = sp.Matrix(3, 3, lambda i, j: sig[i][j] / 2)
et = sp.Matrix(3, 3, lambda i, j: sigt[i][j] / 2)
einv = sp.simplify(e.inv())
gb = sp.simplify(e.T * e)
gbi = sp.simplify(gb.inv())
sq = sp.simplify(sp.sqrt(sp.simplify(gb.det())))
Rad = sp.simplify(et * einv)

H4 = sp.zeros(3, 3)
H4[0, 0] = -Rad[0, 0]
H4[1, 1] = Rad[0, 0]
H4[0, 1] = Rad[0, 1]
H4[1, 0] = Rad[0, 1]
H4 = sp.simplify(H4)
epsT = sp.simplify(e.T * H4 * e)
Mx = sp.simplify(gbi * epsT)
q = [sp.simplify(sp.trigsimp(sp.expand((Mx ** k).trace()))) for k in range(1, 5)]
check(sp.simplify(q[0]) == 0 and sp.simplify(sp.expand(q[3] - q[1] ** 2 / 2)) == 0,
      f"ON THE GRADIENT-CARRYING HARMONIC, POINTWISE AND IN COORDINATES: p1 = {q[0]} and "
      f"p4 - p2^2/2 = {sp.simplify(sp.expand(q[3] - q[1] ** 2 / 2))}")
varies = [v for v in X if sp.simplify(sp.diff(q[1], v)) != 0]
check(len(varies) == 2 and sp.simplify(q[1] - (2 - 2 * sp.sin(ph) ** 2 * sp.sin(th) ** 2)) == 0,
      f"and p2 = {q[1]} genuinely VARIES ({varies}), so the check is on a position-dependent "
      "configuration and not on a constant one in disguise")
check(sp.simplify(q[2]) == 0,
      f"⌗ and this harmonic's cubic invariant vanishes identically (p3 = {q[2]}) -- used in F")

H4b = sp.zeros(3, 3)
H4b[0, 0] = -Rad[1, 1]
H4b[2, 2] = Rad[1, 1]
H4b[0, 2] = Rad[1, 2]
H4b[2, 0] = Rad[1, 2]
H4b = sp.simplify(H4b)
mix = gbi * sp.expand(e.T * (H4 + H4b) * e)
check(sp.simplify(sp.trigsimp(sp.expand(mix.trace()))) == 0,
      "⛭ AND A SUPERPOSITION of two distinct harmonics is pointwise traceless too -- tracelessness "
      "is LINEAR, so A's identity applies to it with no further computation")
PTS = [{sp.sin(psi): sp.Rational(3, 5), sp.cos(psi): sp.Rational(4, 5),
        sp.sin(th): sp.Rational(5, 13), sp.cos(th): sp.Rational(12, 13),
        sp.sin(ph): sp.Rational(8, 17), sp.cos(ph): sp.Rational(15, 17)},
       {sp.sin(psi): sp.Rational(-24, 25), sp.cos(psi): sp.Rational(7, 25),
        sp.sin(th): sp.Rational(20, 29), sp.cos(th): sp.Rational(21, 29),
        sp.sin(ph): sp.Rational(12, 37), sp.cos(ph): sp.Rational(-35, 37)},
       {sp.sin(psi): sp.Rational(9, 41), sp.cos(psi): sp.Rational(40, 41),
        sp.sin(th): sp.Rational(28, 53), sp.cos(th): sp.Rational(45, 53),
        sp.sin(ph): sp.Rational(-11, 61), sp.cos(ph): sp.Rational(60, 61)}]
check(all(sp.simplify(pt[sp.sin(v)] ** 2 + pt[sp.cos(v)] ** 2 - 1) == 0
          for pt in PTS for v in X),
      "three exact points are built from Pythagorean triples, so sin^2 + cos^2 = 1 holds EXACTLY at "
      "each and the arithmetic below is rational rather than approximate")
spot = []
for pt in PTS:
    Mp = sp.Matrix(3, 3, lambda i, j: sp.expand(sp.expand_trig(sp.expand(mix[i, j]))).subs(pt))
    assert not Mp.free_symbols, f"a trig atom survived the substitution: {Mp.free_symbols}"
    pkp = [sp.Rational((Mp ** k).trace()) for k in range(1, 5)]
    spot.append((pkp[0], sp.simplify(pkp[3] - pkp[1] ** 2 / 2), pkp[1]))
check(all(s[0] == 0 and s[1] == 0 and s[2] != 0 for s in spot),
      f"and the superposition is verified there in RATIONAL arithmetic: p1 = 0, p4 - p2^2/2 = 0, and "
      f"p2 non-zero at each ({[s[2] for s in spot]}), so it is a LIVE configuration, not a vanishing "
      "one")


# ===========================================================================
head("C.  THE DEGREE-FOUR INVARIANT SPACE IS ONE-DIMENSIONAL, AND THE CONSTANT FAMILY SWEEPS IT")
# ===========================================================================

e1, e2, e3 = sp.symbols("e1 e2 e3")
newton = {1: e1, 2: e1 ** 2 - 2 * e2, 3: e1 ** 3 - 3 * e1 * e2 + 3 * e3}
newton[4] = sp.expand(e1 * newton[3] - e2 * newton[2] + e3 * newton[1])
newton[5] = sp.expand(e1 * newton[4] - e2 * newton[3] + e3 * newton[2])
elem = {e1: P[0], e2: (P[0] ** 2 - P[1]) / 2,
        e3: (P[0] ** 3 - 3 * P[0] * P[1] + 2 * P[2]) / 6}
check(sp.simplify(sp.expand(newton[4].subs(elem) - P[3])) == 0
      and sp.simplify(sp.expand(newton[5].subs(elem) - P[4])) == 0,
      "p4 and p5 both reduce to p1, p2, p3 through the elementary symmetric functions, so the "
      "invariant ring is generated in degrees one to three")
check(sp.simplify(sp.expand(newton[4].subs(elem).subs(
          {a_: -d_ - g_}) - (P[1] ** 2 / 2).subs({a_: -d_ - g_}))) == 0,
      "⇒ at p1 = 0 the degree-four invariants are spanned by p2^2 ALONE: a ONE-dimensional space, "
      "checked by imposing tracelessness on the reduction itself")


def tre(x, n=NORD):
    x = sp.expand(x)
    return sp.expand(sum(x.coeff(ee, j) * ee ** j for j in range(n)))


def trM(M, n=NORD):
    return M.applyfunc(lambda z: tre(z, n))


def curvature_series(H):
    """the volume-preserving split gamma = exp(eps H), curvature scalar truncated at eps^4."""
    hh = ee * H
    Pw = [sp.eye(3), hh]
    for k in range(2, NORD):
        Pw.append(trM(Pw[-1] * hh))
    gg = trM(sum((Pw[k] / sp.factorial(k) for k in range(NORD)), sp.zeros(3, 3)))
    gi = trM(sum(((-1) ** k * Pw[k] / sp.factorial(k) for k in range(NORD)), sp.zeros(3, 3)))
    G = trM(sp.expand(e.T * gg * e))
    Gi = trM(sp.expand(einv * gi * einv.T))
    C = [[[tre(sum(Gi[i, l] * (sp.diff(G[l, j], X[k]) + sp.diff(G[l, k], X[j])
                               - sp.diff(G[j, k], X[l])) for l in range(3)) / 2)
           for k in range(3)] for j in range(3)] for i in range(3)]
    Ric = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            t = 0
            for i in range(3):
                t += sp.diff(C[i][j][k], X[i]) - sp.diff(C[i][j][i], X[k])
                for l in range(3):
                    t += C[i][i][l] * C[l][j][k] - C[i][k][l] * C[l][j][i]
            Ric[j, k] = tre(t)
    return tre(sum(Gi[j, k] * Ric[j, k] for j in range(3) for k in range(3)))


zz, ww = sp.symbols("z_mode w_mode")


def tri(x):
    """the exact integral over the three angles by picking the zero mode in exp(i psi) and exp(i phi),
    both ranges being whole periods of every harmonic present, then integrating in theta."""
    x = sp.expand(sp.expand(x).rewrite(sp.exp))
    x = x.subs({sp.exp(sp.I * psi): zz, sp.exp(-sp.I * psi): 1 / zz,
                sp.exp(sp.I * ph): ww, sp.exp(-sp.I * ph): 1 / ww})
    x = sp.expand(sp.powsimp(sp.expand(x), force=True))
    num, den = sp.fraction(sp.cancel(sp.together(x)))
    Pn, Pd = sp.Poly(sp.expand(num), zz, ww), sp.Poly(sp.expand(den), zz, ww)
    assert len(Pd.monoms()) == 1, "the denominator is not a single monomial in the two modes"
    dz, dw = Pd.monoms()[0]
    dc = Pd.coeffs()[0]
    zero = sp.Integer(0)
    for mon, co in zip(Pn.monoms(), Pn.coeffs()):
        if mon[0] == dz and mon[1] == dw:
            zero += co / dc
    return sp.simplify(sp.integrate(sp.simplify(sp.expand(zero)), (th, 0, sp.pi))
                       * (2 * sp.pi) * (4 * sp.pi))


check(sp.simplify(tri(sq) - 2 * sp.pi ** 2) == 0
      and sp.simplify(tri(sp.cos(psi) ** 2 * sq) - sp.pi ** 2) == 0
      and sp.simplify(tri(sp.sin(ph) * sp.cos(psi) * sq)) == 0,
      "the zero-mode integrator is validated on the volume, a squared harmonic, and one that must "
      "vanish by parity")


def algebraic_prediction(Hc):
    """C's closed form, integrated: 6 - 2 p2 eps^2 - (10/3) p3 eps^3 - (7/6) p4 eps^4."""
    M = sp.simplify(gbi * sp.simplify(e.T * Hc * e))
    pk = [sp.simplify(sp.trigsimp(sp.expand((M ** k).trace()))) for k in range(1, 5)]
    return [tri(6 * sq), sp.Integer(0), tri(-2 * pk[1] * sq),
            tri(-sp.Rational(10, 3) * pk[2] * sq), tri(-sp.Rational(7, 6) * pk[3] * sq)], pk


HA = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
HB = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
floor_results = {}
for Hc, tag, want in ((HA, "diag(1,-1,0)", [12, 0, -8, 0, sp.Rational(-14, 3)]),
                      (HB, "diag(1,1,-2)", [12, 0, -24, 40, -42])):
    Rs = curvature_series(Hc)
    got = [sp.simplify(tri(sp.simplify(Rs.coeff(ee, k)) * sq) / sp.pi ** 2) for k in range(NORD)]
    pred, pk = algebraic_prediction(Hc)
    predn = [sp.simplify(v / sp.pi ** 2) for v in pred]
    floor_results[tag] = (got, predn, pk)
    check(got == [sp.nsimplify(w) for w in want],
      f"FLOOR, {tag}: the pipeline gives {got} times pi^2 at orders 0..4, matching the value "
      "derived from the eigenvalue closed form BEFORE it was run")
    check(got == predn,
      f"⇒ and C's algebraic closed form reproduces every order there ({predn}), so at a level with "
      "no gradients the algebraic part is the WHOLE answer")

check(all(sp.simplify(sp.Rational(-7, 6) * floor_results[tg][2][3]
                      - sp.Rational(-7, 12) * floor_results[tg][2][1] ** 2) == 0
          for tg in floor_results),
      "⛭ and on BOTH directions' own computed invariants the quartic's -(7/6) p4 IS -(7/12) p2^2 by "
      "A's identity: ONE coefficient, -7/12, and the frame-constant family already determines it")
check(floor_results["diag(1,-1,0)"][0][3] == 0 and floor_results["diag(1,1,-2)"][0][3] != 0,
      "⌗ and the two directions are genuinely independent probes: the cubic is invisible on the "
      "first and non-zero on the second, so the (p2, p3) family is swept and not sampled once")


# ===========================================================================
head("D.  THE DERIVATIVE SECTOR: EIGHT POINTWISE, AND THE ONE RELATION A LEVEL SUPPLIES")
# ===========================================================================

random.seed(7)
hb = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    M = sp.zeros(3, 3)
    M[i, j] = 1
    M[j, i] = 1
    hb.append(M)
hb.append(sp.diag(1, -1, 0))
hb.append(sp.diag(1, 1, -2))
check(all(sp.simplify(M.trace()) == 0 and sp.simplify(M - M.T) == sp.zeros(3, 3) for M in hb)
      and sp.Matrix([[M[i, j] for i in range(3) for j in range(3)] for M in hb]).rank() == 5,
      "the symmetric traceless h at a point spans a five-dimensional space, by rank rather than "
      "by counting")

jidx = [(p, r, s) for p in range(D) for r in range(D) for s in range(r, D)]
Vs = sp.symbols(f"v0:{len(jidx)}")


def Gj(p, r, s):
    return Vs[jidx.index((p, min(r, s), max(r, s)))]


cons = [sum(Gj(p, k, k) for k in range(D)) for p in range(D)]
cons += [sum(Gj(p, p, s) for p in range(D)) for s in range(D)]
Mc = sp.Matrix([[sp.expand(x).coeff(v) for v in Vs] for x in cons])
ns = Mc.nullspace()
check(len(ns) == 12,
      f"and the admissible one-jet grad h -- symmetric and traceless in its last two indices and "
      f"divergence-free -- has dimension {len(ns)}, computed as a NULLSPACE of those conditions")
GB = []
for v in ns:
    arr = [[[sp.Integer(0)] * D for _ in range(D)] for _ in range(D)]
    for (p, r, s), val in zip(jidx, v):
        arr[p][r][s] = val
        arr[p][s][r] = val
    GB.append(arr)

GROUP = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3]


def matchings(slots):
    if not slots:
        yield []
        return
    p = slots[0]
    for i in range(1, len(slots)):
        r = slots[i]
        if GROUP[p] == GROUP[r]:
            continue
        for m in matchings(slots[1:i] + slots[i + 1:]):
            yield [(p, r)] + m


pats = list(matchings(list(range(10))))


def contract(pat, hm, gm):
    tot = sp.Integer(0)
    for asg in itertools.product(range(D), repeat=5):
        ind = [None] * 10
        for k, (p, r) in enumerate(pat):
            ind[p] = asg[k]
            ind[r] = asg[k]
        tot += (gm[ind[0]][ind[1]][ind[2]] * gm[ind[3]][ind[4]][ind[5]]
                * hm[ind[6], ind[7]] * hm[ind[8], ind[9]])
    return sp.expand(tot)


rows = []
for _ in range(20):
    hr = sum((random.randint(-9, 9) * M for M in hb), sp.zeros(3, 3))
    gr = [[[sp.Integer(0)] * D for _ in range(D)] for _ in range(D)]
    for arr in GB:
        cf = random.randint(-9, 9)
        for p in range(D):
            for r in range(D):
                for s in range(D):
                    gr[p][r][s] += cf * arr[p][r][s]
    rows.append([contract(pat, hr, gr) for pat in pats])
rk = sp.Matrix(rows).rank()
check(rk == 8,
      f"⛭ THE POINTWISE TWO-DERIVATIVE QUARTIC SECTOR HAS {rk} INDEPENDENT INVARIANTS -- the rank of "
      f"the value matrix over the {len(pats)} admissible contractions of grad h grad h h h, no "
      "intra-tensor pair being allowed because h is traceless and transverse")
rk_sub = sp.Matrix(rows[:12]).rank()
check(rk_sub == rk and rk < 12,
      f"⌗ and the rank SATURATES strictly below the number of jets: twelve of the twenty already give "
      f"{rk_sub}, and the remaining eight add nothing, so {rk} is the sector's dimension and not an "
      "artefact of how many jets were tried")

Chr = [[[sp.simplify(sum(gbi[i, l] * (sp.diff(gb[l, j], X[k]) + sp.diff(gb[l, k], X[j])
                                      - sp.diff(gb[j, k], X[l])) for l in range(3)) / 2)
         for k in range(3)] for j in range(3)] for i in range(3)]
E = [[epsT[i, j] for j in range(3)] for i in range(3)]
DE = [[[sp.simplify(sp.diff(E[i][j], X[k])
                    - sum(Chr[l][k][i] * E[l][j] + Chr[l][k][j] * E[i][l] for l in range(3)))
        for k in range(3)] for j in range(3)] for i in range(3)]
divs = [sp.simplify(sum(gbi[i, k] * DE[i][j][k] for i in range(3) for k in range(3)))
        for j in range(3)]
check(all(x == 0 for x in divs),
      "the harmonic is transverse, recomputed here from the Christoffel symbols rather than quoted")
G2 = sp.simplify(sp.expand(sum(
    gbi[k, l] * gbi[i, m] * gbi[j, n] * DE[i][j][k] * DE[m][n][l]
    for k in range(3) for l in range(3) for i in range(3) for j in range(3)
    for m in range(3) for n in range(3))))
lap_q2 = sp.simplify(sp.expand(sum(
    gbi[i, j] * (sp.diff(sp.diff(q[1], X[j]), X[i])
                 - sum(Chr[k][j][i] * sp.diff(q[1], X[k]) for k in range(3)))
    for i in range(3) for j in range(3))))
LAM = 22
check(sp.simplify(sp.expand(lap_q2 - (-2 * LAM * q[1] + 2 * G2))) == 0,
      f"⛭ THE RELATION, POINTWISE: nabla^2(tr eps^2) = -2*{LAM}*(tr eps^2) + 2|grad eps|^2 exactly, "
      f"with |grad eps|^2 = {G2} -- the Laplace eigenvalue entering as the level's own datum")
lhs = tri(sum(gbi[i, j] * sp.diff(q[1], X[i]) * sp.diff(q[1], X[j])
              for i in range(3) for j in range(3)) * sq)
rhs = sp.simplify(2 * LAM * tri(q[1] ** 2 * sq) - 2 * tri(q[1] * G2 * sq))
check(sp.simplify(lhs - rhs) == 0,
      f"⇒ integrated: int |grad tr eps^2|^2 = {sp.simplify(lhs / sp.pi ** 2)} pi^2 on both sides -- "
      "ONE relation among two derivative invariants and one algebraic one")
lhs4 = sp.simplify(sp.expand(sum(gbi[i, j] * sp.diff(q[3], X[i]) * sp.diff(q[3], X[j])
                                 for i in range(3) for j in range(3))))
lhs2 = sp.simplify(sp.expand(q[1] ** 2 * sum(gbi[i, j] * sp.diff(q[1], X[i]) * sp.diff(q[1], X[j])
                                             for i in range(3) for j in range(3))))
check(sp.simplify(sp.expand(lhs4 - lhs2)) == 0,
      "⛭ AND THE SECOND CANDIDATE RELATION IS THE SAME ONE, for exactly the reason 1 turns on: "
      "grad(tr eps^4) = (tr eps^2) grad(tr eps^2) by A's identity, so the two total derivatives are "
      "one ⇒ AT MOST SEVEN independent integrated invariants")
print("    ⛔ SCOPE IN THE SAME SENTENCE: eight is the EXACT pointwise count; seven is an UPPER bound")
print("       on the integrated count, because one relation is exhibited and no proof is offered that")
print("       there are no others.")


# ===========================================================================
head("E.  THE SECOND ANCHOR AT FOURTH ORDER, AND THE DERIVATIVE SECTOR'S VALUE THERE")
# ===========================================================================

nonconst = [v for v in X if sp.simplify(sp.diff(H4[0, 0], v)) != 0]
check(len(nonconst) == 3,
      f"the harmonic's frame components are non-constant in all three coordinates ({nonconst}), so "
      "the gradient terms are present rather than vanishing")
Rs4 = curvature_series(H4)
got4 = [sp.simplify(tri(sp.simplify(Rs4.coeff(ee, k)) * sq) / sp.pi ** 2) for k in range(NORD)]
check(got4[:3] == [12, 0, -16],
      f"orders 0..2 at that level are {got4[:3]} times pi^2, reproducing r6967's 12, 0, -16 as a "
      "RE-DERIVATION in the fourth-order pipeline and not as a quotation")
check(got4[3] == 0 and got4[4] == sp.Rational(-88, 15),
      f"⛭⛭ AND THE FOURTH ORDER IS {got4[4]} pi^2, with the third vanishing ({got4[3]})")

pred4, pk4 = algebraic_prediction(H4)
pred4n = [sp.simplify(v / sp.pi ** 2) for v in pred4]
check(pred4n[2] == sp.Rational(-16, 3) and pred4n[4] == sp.Rational(-112, 45),
      f"C's algebraic-only prediction at that level is {pred4n[2]} pi^2 at second order and "
      f"{pred4n[4]} pi^2 at fourth")
d2 = sp.simplify(got4[2] - pred4n[2])
d4 = sp.simplify(got4[4] - pred4n[4])
check(d2 == sp.Rational(-32, 3) and d4 == sp.Rational(-152, 45),
      f"⇒ THE DERIVATIVE SECTOR'S VALUE AT THAT LEVEL: {d2} pi^2 at second order and {d4} pi^2 at "
      "fourth -- exact rationals, by difference against a prediction derived independently")
for tag in ("diag(1,-1,0)", "diag(1,1,-2)"):
    g_, p_, _pk = floor_results[tag]
    check(all(sp.simplify(g_[k] - p_[k]) == 0 for k in range(NORD)),
          f"** CONTROL, {tag}: the same difference is exactly ZERO at every order ** -- the "
          "derivative sector is invisible where the harmonics have no gradients, which is the "
          "order's own reason, measured rather than assumed")
check(sp.simplify(d4) != 0 and sp.simplify(d2) != 0,
      "⇒ and non-zero where they are present: the two numbers above are what a gradient-carrying "
      "level supplies, and each is ONE linear combination of the sector's coefficients")


# ===========================================================================
head("F.  THE SIGN AT THE SECOND LEVEL, WITH ITS SCOPE")
# ===========================================================================

mu2_lvl = LAM + 2
check(sp.simplify(mu2_lvl - (5 ** 2 - 1)) == 0 and got4[3] == 0,
      f"at this level mu^2 = {mu2_lvl} = m^2-1 at m = 5, and the third order VANISHES, so the "
      "diagonal cubic vertex along the exhibited direction is zero")
c4_here, g2_here = d4, got4[3]
thresh = sp.simplify(g2_here / (2 * abs(c4_here)))
check(sp.simplify(thresh) == 0 and mu2_lvl > thresh,
      f"⇒ the criterion mu^2 > g^2/2c4 reads {mu2_lvl} > {thresh}: POSITIVE WITH NO CONDITION at a "
      "second level, so a definite sign is a result at two levels rather than a conjecture at one")
cub_A = floor_results["diag(1,-1,0)"][2][2]
cub_B = floor_results["diag(1,1,-2)"][2][2]
check(sp.simplify(cub_A) == 0 and sp.simplify(cub_B) != 0
      and floor_results["diag(1,-1,0)"][0][3] == 0 and floor_results["diag(1,1,-2)"][0][3] != 0,
      f"⚠ SCOPE, established rather than asserted: a vanishing diagonal cubic is a property of a "
      f"DIRECTION and not of a level -- at the floor one direction has p3 = {cub_A} and a vanishing "
      f"third order while another has p3 = {cub_B} and a third order that does not vanish")
check(sp.simplify(q[2]) == 0 and sp.simplify(2 * (5 ** 2 - 4) - 2 * (4 + 3) * (4 - 1)) == 0,
      "⇒ so the zero above is this harmonic's own pointwise p3, one direction of a level whose "
      "degeneracy 2(m^2-4) = 2(n+3)(n-1) counts many; a general triple overlap need not vanish, and "
      "r7010's conditional is discharged ALONG THIS DIRECTION and NOT for the level")


print()
print("=" * 96)
if FAILED:
    print(f"VERDICT: {len(FAILED)} CHECK(S) FAILED")
    for m in FAILED:
        print("   ", m)
    raise SystemExit(1)
print("VERDICT: ALL PASS.  1 IS RIGHT AND STRONGER THAN ASKED -- the algebraic quartic is a")
print("  ONE-dimensional invariant space, its single coefficient -7/12 is already determined by the")
print("  frame-constant family, and the tower is pointwise traceless because it IS the three-sphere's")
print("  transverse-traceless tower, d(m) = 2(m^2-4) and mu^2 = m^2-1 being that spectrum exactly.")
print("  ⛔ BUT THE REMAINDER IS NOT SMALLER THAN THE TABLE: the derivative sector has EIGHT")
print("  invariants pointwise and AT MOST SEVEN on a level, the one relation being degenerate for")
print("  exactly the reason 1 turns on.  AND 2 IS DONE: the second anchor reaches fourth order,")
print("  -88/15 pi^2 against an algebraic-only -112/45, so the derivative sector's value there is")
print("  -152/45 pi^2 -- and exactly zero at the floor.  3: the sign is positive with no condition")
print("  at a second level, along one direction of it.")
print("=" * 96)
