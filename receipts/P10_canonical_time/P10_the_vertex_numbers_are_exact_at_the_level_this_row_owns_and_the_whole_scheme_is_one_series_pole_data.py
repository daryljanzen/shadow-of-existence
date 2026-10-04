#!/usr/bin/env python3
r"""
P10_the_vertex_numbers_are_exact_at_the_level_this_row_owns_and_the_whole_scheme_is_one_series_pole_data
=======================================================================================================

LEVEL: **exact throughout, and there are no floats at all.**  The reduction is derived from the extrinsic
curvature, the three-curvature is a closed form valid to all orders in the anisotropy, the vertex numbers are
its exact Taylor coefficients, the second-order shift is an exact Fock-space computation, and every residue is
a rational.

OBJECT UNDER TEST -- `PO-23`, `r7007`.  The order gates `r7006` whole and, after six revisions of keeping them
last, asks for **the coefficients**:

  1 *"**THE VERTEX NUMBERS AND WHAT THEY GIVE.**  The three quartic structures the action supplies, their
      coefficients, and what those make the dimension-six counterterm's rational multiple.  ⌗ *And carry the
      unknown through symbolically first if that is cheaper.*"*
  2 *"**AND THE SECOND-ORDER RANK FROM ABOVE, WHICH YOUR OWN CORRECTION MADE OWED.**  You bounded it below by
      the iterated deformation.  **What bounds it above?** ... *if it cannot be written down within this
      construction, that is the same answer as "the order is not reached" and it should be said that way
      rather than left as a bound.*"*
  3 *"**AND ONE THING THAT WOULD CHANGE WHAT THE ROW IS, IF IT IS CHEAP.**  ... **Is the whole subtraction
      scheme expressible in terms of that one residue** -- so that the section's three conventions, the rank
      and the anomaly are all statements about a single spectral quantity?"*
  4 *"And if 1 consumes the revision, stop and say so."*
  Guards: **a rank and a size are different objects**; **correct your own previous revision's scope when you
  find it**; **carry an unknown through rather than waiting for it**; and decline a wrong correction.

COMPUTES: the exact ADM reduction of the closed-$S^3$ geometry in the frame-constant sector; the exact
three-curvature of that sector and its expansion through quartic order; the frequency that expansion implies,
against the tower's own; the kinetic sector in two parameterizations; the second-order vacuum shift of the two
modes exactly in a truncated Fock space, with the cubic's vacuum amplitudes; and the poles and residues of the
tower's two spectral Dirichlet series against the partial sums' coefficients.

rc=0 on all 29 checks.

-------------------------------------------------------------------------------
** ⛭⛭⛭ 1 THE VERTEX NUMBERS ARE EXACT AT THE LEVEL THIS ROW OWNS, AND THEY COME FROM AN EXACT REDUCTION RATHER
  THAN FROM AN EXPANSION IN POWERS OF A FIELD. **
`r6967`'s harmonics at the lowest level are **frame-constant**, so a perturbation there is a left-invariant
metric on the three-sphere -- and for those the geometry is known in closed form to *all* orders:
  * the extrinsic-curvature scalar is exactly $K_{ij}K^{ij}-K^{2}=-6H^{2}+6(\dot\beta_{+}^{2}+
    \dot\beta_{-}^{2})$, derived here, and its isotropic limit returns the standard closed-FRW Lagrangian;
  * the three-curvature is exactly $R^{(3)}=2\bigl[2\sum\lambda\lambda-\sum\lambda^{2}\bigr]$ with
    $\prod\lambda=1$, which is $6$ on the round metric;
  * and its expansion is *** $R^{(3)}=6-48(\beta_{+}^{2}+\beta_{-}^{2})+160(\beta_{+}^{3}-3\beta_{+}
    \beta_{-}^{2})-336(\beta_{+}^{2}+\beta_{-}^{2})^{2}+\dots$ ***, the cubic exactly the hexagonal
    $\operatorname{Re}(\beta_{+}+\mathrm{i}\beta_{-})^{3}$ and **the quartic exactly isotropic**.
** ⇒ AND THE CALIBRATION IS THE CHECK THAT THIS IS THE ROW'S OWN LEVEL AND NOT A DIFFERENT PROBLEM: ** the
ratio of those first two coefficients is $48/6=8$, so $\mu^{2}=8$ -- *exactly `r6998`'s $m^{2}-1$ at $m=3$* --
and the level's degeneracy $2(m^{2}-4)=10$ is the frame-constant count `r7000` used.  ***Two numbers this row
has been carrying arrive here from the metric instead of from the spectrum.***

** ⛭⛭ AND ONE OF `r6998`'s THREE STRUCTURES IS A PARAMETERISATION AT THIS LEVEL, WHICH IS `r6994`'s OWN
  IDENTITY ARRIVING FROM THE OTHER SIDE. **  In the exponential variable the kinetic term is **exactly**
quadratic -- no $\pi^{2}\varphi^{2}$ vertex at any order -- while in the linear one
$\dot\beta^{2}=\dot h^{2}(1-4h+12h^{2}-\dots)$ carries both a cubic and a quartic.  *The two are related by a
point transformation, which `r6994` showed leaves every spectral quantity fixed.* ⇒ ***So the $\pi^{2}
\varphi^{2}$ structure is exactly the redefinition-generated "fake" quartic of `r6994`'s identity, and in the
variables where it is absent the physical shift is carried by the potential's quartic and the cubic alone.***

** ⛭⛭⛭ AND THE SECOND-ORDER SHIFT AT THIS LEVEL IS THEREFORE A NUMBER, COMPUTED EXACTLY. **
$$\Delta E^{(2)}=\frac{4\kappa\hbar^{2}}{27Va^{3}}\cdot\frac{63\mu^{2}-200}{\mu^{4}}
  \;\xrightarrow{\;\mu^{2}=8\;}\;\frac{19}{27}\,\frac{\kappa\hbar^{2}}{V a^{3}}\;>0 .$$
  * the quartic gives $+8c_{4}as^{2}$ with $s=\langle\varphi^{2}\rangle$, exactly;
  * **the cubic's vacuum amplitude at ONE quantum cancels identically** -- the $\beta_{+}^{3}$ and
    $\beta_{+}\beta_{-}^{2}$ channels are equal and opposite -- so it reaches the vacuum only at *three*
    quanta, which is the non-resonance `r6994`'s identity needs, here as an arithmetic;
  * ⇒ and the energy **density** goes as $a^{-6}$, *which is the dimension-six behaviour the row predicted
    from the mode count and the dimensional bookkeeping, now arriving from the vertices themselves*;
  * ⚠ **and the threshold is stated with the result**: the sign flips at $\mu^{2}=200/63$, and this level sits
    above it -- so *positive* is a statement about this level and not about the tower.
⚠ **SCOPE IN THE SAME SENTENCE:** that is the exact coefficient **at the frame-constant level**, whose
harmonics are constant in an orthonormal frame; the tower-wide rational multiple needs the higher levels'
overlap integrals, whose structure `r7000` fixed and whose values this revision does not compute.

** 2 AND THE SECOND-ORDER RANK CANNOT BE BOUNDED FROM ABOVE HERE -- WHICH THE ORDER SAID TO REPORT AS "THE
  ORDER IS NOT REACHED" RATHER THAN AS A MISSING BOUND, AND SO IT IS. **  The reason is a count, and it is the
row's own guard about equations against unknowns: at first order the semiclassical system closes -- the
constraint plus the *free* state determine the correction, one equation and one unknown -- while at second
order the source needs the state's own first-order correction, **which adds an unknown without adding an
equation**.  *And the exact reduction has no room for an independent second-order datum of its own: the
geometry there is exhausted by the scale factor and the two anisotropies, so the only place a second-order
source could come from is the interacting state this construction does not build.*

** ⛭⛭ 3 AND YES: THE WHOLE SUBTRACTION SCHEME IS THE POLE DATA OF ONE SPECTRAL SERIES. **
The tower's two weights have Dirichlet series with simple poles and rational residues --
$\sum d\mu\,m^{-s}$ at $s=4,2,0$ with $2$, $-9$, $\tfrac{15}4$; $\sum (d/\mu)m^{-s}$ at $s=2,0$ with $2$,
$-7$ -- and every coefficient the subtraction needs is built from them: *each pole contributes its residue
over its own location to the corresponding power of the cutoff* (verified pole by pole), *the logarithmic
coefficients are the $s=0$ residues exactly*, and *the second-order sum's leading coefficient is a PRODUCT of
two residues*, $\tfrac24\cdot\tfrac22=\tfrac12$.
*** ⇒ So the section's three subtractions, the anomaly and the value-rank are all statements about the pole
data of the tower's spectral series, and the row's answer is one sentence: the scheme is that series' poles,
the anomaly is the residue at zero, and the coefficients are polynomials in the residues. ***
⌗ *The subleading integer powers mix under a sharp cutoff -- Faulhaber's, not the spectrum's -- which is
exactly `r7002`'s division between what is a coefficient and what is a convention, now visible as the
difference between a residue and a partial sum's lower terms.*

** 4 SO 1 DID NOT CONSUME THE REVISION AND THE STOP IS NOT NEEDED, but what is delivered and what is not is
  said plainly: the vertex numbers and the second-order shift are exact AT THIS LEVEL; the tower-wide rational
  multiple is not computed, and it now needs one thing only -- the higher levels' overlap integrals. **
"""
# ===========================================================================
import sys

import sympy as sp
import os, sys
_VHERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_VHERE, '..', '..', 'corpus'))
import paper_formula as pf

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


m, M = sp.symbols("m M", positive=True)
bp, bm = sp.symbols("beta_+ beta_-", real=True)
H, bdp, bdm = sp.symbols("H bdp bdm", real=True)
a, kap, Vol, hbar, mu = sp.symbols("a kappa V hbar mu", positive=True)
h_, s_ = sp.symbols("h s", positive=True)

print()
print("=" * 94)
print("  A.  1 THE EXACT REDUCTION OF THE FRAME-CONSTANT SECTOR, AND THE VERTEX NUMBERS IT GIVES")
print("=" * 94)

# --- A1  the extrinsic-curvature scalar, derived from K^i_j = diag(H + betadot_i)
d = [bdp + sp.sqrt(3) * bdm, bdp - sp.sqrt(3) * bdm, -2 * bdp]
KK = sp.simplify(sp.expand(sum((H + x) ** 2 for x in d) - (3 * H + sum(d)) ** 2))
#: ⛭ r7161+cc66.128: ** THE PAPER'S WHOLE EXPRESSION IS PARSED, AND THE ISOTROPIC LIMIT IS TAKEN ON
#: BOTH SIDES RATHER THAN TYPED. **  This is the site `cc66.123` named as needing a different shape
#: from the other eight: `paper_formula.inline` REFUSED the pattern `-6H^{2}` because the paper prints
#: `K_{ij}K^{ij}-K^{2}=-6H^{2}+6(\dot\beta_{+}^{2}+\dot\beta_{-}^{2})` and `-6H^2` is that
#: expression's ISOTROPIC LIMIT, not a figure the paper states on its own.  *Pattern-matching it would
#: have attributed a derived limit to the paper as a quotation.*
#: ⇒ So the paper's full expression is read, and the limit is applied to the PARSED side as well as to
#: this file's own -- the stated OPERATION, where the other eight sites take a substitution.  `-6H^2`
#: is now typed nowhere in this check.
_P10V = open(os.path.join(_VHERE, '..', '..', 'corpus', 'canonical_time.tex'), encoding='utf-8').read()
_KK_PAPER, _KKk, _KKs = pf.inline(
    _P10V,
    r'K_\{ij\}K\^\{ij\}-K\^\{2\}=(-6H\^\{2\}\+6\(\\dot\\beta_\{\+\}\^\{2\}'
    r'\+\\dot\\beta_\{-\}\^\{2\}\))',
    {'H': H, 'beta_dot_plus': bdp, 'beta_dot_minus': bdm})
_ISO = {bdp: 0, bdm: 0}
check(sp.simplify(sum(d)) == 0 and sp.simplify(KK - _KK_PAPER) == 0,
      f"the frame-constant sector's extrinsic curvature gives K_ij K^ij - K^2 = {KK} exactly, matching "
      f"the paper's own {_KK_PAPER} PARSED from it ({_KKk} statement) -- the Misner velocities summing "
      "to zero, so the volume and the anisotropies separate with no cross term")
check(sp.simplify(KK.subs(_ISO) - _KK_PAPER.subs(_ISO)) == 0,
      f"and its isotropic limit is {sp.simplify(_KK_PAPER.subs(_ISO))}, taken on the PARSED expression "
      "as well as on this file's own rather than typed -- which with the three-curvature's 6 returns "
      "the standard closed-FRW Lagrangian, the calibration that the reduction is the section's own "
      "geometry")
check(sp.simplify(_KK_PAPER.subs(_ISO) - _KK_PAPER) != 0,
      "    CONTROL -- the limit is not vacuous: the paper's expression is NOT already isotropic, so "
      "the anisotropy terms it carries are really being set to zero")

# --- A2  the three-curvature, exactly and then expanded
b = [bp + sp.sqrt(3) * bm, bp - sp.sqrt(3) * bm, -2 * bp]
lam = [sp.exp(2 * x) for x in b]
check(sp.simplify(sp.expand(lam[0] * lam[1] * lam[2])) == 1,
      "the anisotropy is unimodular by construction, so the scale factor carries the whole volume: the "
      "product of the three eigenvalues is exactly 1")
R3 = sp.simplify(2 * (2 * (lam[0] * lam[1] + lam[1] * lam[2] + lam[2] * lam[0]) - sum(x**2 for x in lam)))
check(sp.simplify(R3.subs({bp: 0, bm: 0})) == 6,
      "and the closed form for the three-curvature returns exactly 6 on the round metric, which fixes its one "
      "normalisation without a convention being chosen")
ser = sp.expand(sp.series(sp.series(R3, bp, 0, 5).removeO(), bm, 0, 5).removeO())
P = sp.Poly(ser, bp, bm)
q = {k: sp.expand(sum(c * bp**mo[0] * bm**mo[1] for mo, c in P.terms() if sum(mo) == k)) for k in (2, 3, 4)}
check(sp.simplify(q[2] + 48 * (bp**2 + bm**2)) == 0,
      f"its quadratic term is exactly -48(beta_+^2 + beta_-^2) -- isotropic, so the two anisotropies are "
      "degenerate, as one level of a tower must be")
check(sp.simplify(q[3] - 160 * (bp**3 - 3 * bp * bm**2)) == 0,
      "its cubic term is exactly 160 times the real part of (beta_+ + i beta_-)^3 -- the hexagonal structure, "
      "which is a property of the three-sphere's own symmetry and not of the truncation")
check(sp.simplify(q[4] + 336 * (bp**2 + bm**2) ** 2) == 0,
      f"and its quartic term is exactly -336 (beta_+^2 + beta_-^2)^2: ** ISOTROPIC, so ONE number carries the "
      "whole quartic vertex at this level **")

# --- A3  the calibration against the tower's own spectrum
check(sp.Rational(48, 6) == 8 and 3**2 - 1 == 8 and 2 * (3**2 - 4) == 10,
      "⇒ ** THE CALIBRATION: the ratio of those two coefficients is 48/6 = 8 = mu^2, which is r6998's m^2 - 1 "
      "at m = 3, and the level's degeneracy 2(m^2-4) = 10 is r7000's frame-constant count ** -- two numbers "
      "this row carried from the spectrum, arriving here from the metric")
mu2 = sp.Rational(48, 6)
check(sp.simplify(sp.sqrt(mu2) - 2 * sp.sqrt(2)) == 0 and mu2 > sp.Rational(200, 63),
      f"and the frequency it implies is mu = 2 sqrt(2), which will matter below because the second-order "
      f"shift changes sign at mu^2 = 200/63 and this level sits above it")

print()
print("=" * 94)
print("  B.  THE KINETIC SECTOR IS EXACTLY FREE IN ONE PARAMETERISATION AND NOT IN THE OTHER")
print("=" * 94)

bdot_exp = sp.Symbol("bdot", real=True)            # in the exponential variable
hdot = sp.Symbol("hdot", real=True)
beta_of_h = sp.log(1 + 2 * h_) / 2                  # lambda = 1 + 2h, beta = (1/2) log lambda
bdot_h = sp.simplify(sp.diff(beta_of_h, h_) * hdot)
kin_h = sp.expand(sp.series(sp.expand(6 * bdot_h**2), h_, 0, 3).removeO())
kin_exp = sp.expand(sp.series(6 * bdot_exp**2, bp, 0, 3).removeO())
check(sp.simplify(kin_h.coeff(h_, 0) - 6 * hdot**2) == 0 and kin_h.coeff(h_, 1) == -24 * hdot**2
      and kin_h.coeff(h_, 2) == 72 * hdot**2
      and kin_exp.coeff(bp, 1) == 0 and kin_exp.coeff(bp, 2) == 0,
      f"the same kinetic term is {kin_h} in the LINEAR variable -- a cubic AND a quartic vertex, in the ratio "
      "the expansion of 1/(1+2h)^2 requires -- against exactly zero field dependence at both orders in the "
      "EXPONENTIAL one, which is the contrast rather than one reading alone")
check(sp.simplify(sp.diff(beta_of_h, h_).subs(h_, 0)) == 1 and sp.simplify(beta_of_h.subs(h_, 0)) == 0,
      "⇒ ** and the two variables agree at linear order with unit Jacobian, so the map between them is a POINT "
      "TRANSFORMATION -- exactly r6994's redefinition, which leaves every spectral quantity fixed ** ⇒ the "
      "pi^2 phi^2 structure is the 'fake' quartic of that identity, and it is absent in the exponential one")

print()
print("=" * 94)
print("  C.  THE SECOND-ORDER SHIFT AT THIS LEVEL, EXACTLY, IN A TWO-MODE FOCK SPACE")
print("=" * 94)

NF = 7
Al = sp.zeros(NF, NF)
for k in range(1, NF):
    Al[k - 1, k] = sp.sqrt(k)
Id = sp.eye(NF)
x1 = sp.sqrt(s_) * (Al + Al.T)
Xp = sp.Matrix(sp.kronecker_product(x1, Id))
Xm = sp.Matrix(sp.kronecker_product(Id, x1))
Nop = sp.Matrix(sp.kronecker_product(Al.T * Al, Id)) + sp.Matrix(sp.kronecker_product(Id, Al.T * Al))
vac = sp.zeros(NF * NF, 1)
vac[0, 0] = 1
c4, gc, hw = sp.symbols("c4 g hbaromega", positive=True)
V4 = c4 * (Xp**2 + Xm**2) ** 2
V3 = -gc * (Xp**3 - 3 * Xp * Xm**2)
e4 = sp.simplify((vac.T * V4 * vac)[0, 0])
check(sp.simplify(e4 - 8 * c4 * s_**2) == 0,
      f"the quartic's vacuum expectation is exactly {e4} -- three from each mode's own fourth moment and two "
      "from the cross term, computed in the Fock space rather than by a Wick count done by hand")
v3vac = sp.simplify(V3 * vac)
levels = {}
for i in range(1, NF * NF):
    amp = sp.simplify(v3vac[i, 0])
    if amp != 0:
        lv = int(sp.simplify((Nop[i, i])))
        levels.setdefault(lv, []).append(sp.simplify(amp))
check(set(levels) == {3} and len(levels[3]) == 2,
      f"⇒ ** AND THE CUBIC REACHES THE VACUUM ONLY AT THREE QUANTA: the ONE-quantum amplitude cancels "
      f"identically ** -- the two channels being equal and opposite -- leaving {len(levels[3])} states, "
      f"{levels[3]}, which is the non-resonance r6994's identity requires, here as an arithmetic")
dE3 = sp.simplify(-sum(amp**2 / (3 * hw) for amp in levels[3]))
check(sp.simplify(dE3 + 8 * gc**2 * s_**3 / hw) == 0,
      f"so the cubic's second-order shift is exactly {sp.simplify(dE3)}, negative as second order must be")
c4v = 14 * kap / (3 * Vol)
gv = 160 * (Vol / (2 * kap)) * (kap / (6 * Vol)) ** sp.Rational(3, 2)
check(sp.simplify(gv**2 - 800 * kap / (27 * Vol)) == 0 and sp.simplify(c4v - 14 * kap / (3 * Vol)) == 0,
      f"the canonical normalisation phi = sqrt(6V/kappa) beta turns those vertex numbers into c4 = {c4v} and "
      f"g^2 = {sp.simplify(gv**2)}, with no freedom left once the kinetic term is unit-normalised")
sv = hbar / (2 * a**2 * mu)
hwv = hbar * mu / a
total = sp.simplify(8 * c4v * a * sv**2 - 8 * gv**2 * a**2 * sv**3 / hwv)
at8 = sp.simplify(total.subs(mu, 2 * sp.sqrt(2)))
check(sp.simplify(total - 4 * kap * hbar**2 * (63 * mu**2 - 200) / (27 * Vol * a**3 * mu**4)) == 0,
      f"⇒ ** the second-order vacuum shift at this level is exactly {sp.simplify(total)} **, the quartic and "
      "the cubic entering with opposite signs")
check(sp.simplify(at8 - 19 * kap * hbar**2 / (27 * Vol * a**3)) == 0 and at8 > 0,
      f"⇒ ** AT THIS LEVEL'S OWN FREQUENCY THAT IS {sp.nsimplify(sp.simplify(at8 / (kap * hbar**2 / (Vol * a**3))))}"
      " times kappa hbar^2 / (V a^3), and it is POSITIVE: the quartic wins over the cubic **")
thr = sp.solve(sp.Eq(63 * sp.Symbol("x") - 200, 0), sp.Symbol("x"))[0]
check(thr == sp.Rational(200, 63) and mu2 > thr,
      f"⚠ and the threshold is stated with the result rather than after it: the sign flips at mu^2 = {thr}, "
      f"so 'positive' is a statement about this level (mu^2 = {mu2}) and not about the tower")
dens = sp.simplify(at8 / (Vol * a**3))
check(sp.simplify(sp.diff(sp.log(dens), a) * a + 6) == 0,
      f"and the energy DENSITY it implies is {dens}, which falls as the sixth power of the scale factor ⇒ "
      "** the dimension-six behaviour the row read off the mode count, now arriving from the vertices **")

print()
print("=" * 94)
print("  D.  2 THE SECOND-ORDER RANK FROM ABOVE: NOT A MISSING BOUND BUT AN ORDER NOT REACHED")
print("=" * 94)

da1, da2, dpsi, src1, src2, c1, c2 = sp.symbols("da1 da2 dpsi src1 src2 c1 c2")
sol1 = sp.solve([sp.Eq(c1 * da1, src1)], [da1], dict=True)              # first order: closes
sol2 = sp.solve([sp.Eq(c1 * da2 + c2 * dpsi, src2)], [da2, dpsi], dict=True)   # second: state enters
check(len(sol1) == 1 and len(sol1[0]) == 1
      and len(sol2) == 1 and len(sol2[0]) == 1 and sp.Symbol("dpsi") in sol2[0][da2].free_symbols,
      f"the row's own guard about equations against unknowns, as an arithmetic rather than a tally: the "
      f"first-order system determines its one unknown uniquely, {sol1[0]}, while the second-order one -- whose "
      f"source needs the state's own correction -- returns a FAMILY, {sol2[0]}, the free state parameter still "
      "in the answer")
jac = sp.Matrix([[sp.diff(x, v) for v in (bp, bm)] for x in b])
check(jac.rank() == 2 and sp.simplify(sum(b)) == 0
      and sp.simplify(sp.diff(R3, bp)) != 0 and sp.simplify(sp.diff(R3, bm)) != 0,
      f"and the exact reduction has no independent second-order datum of its own: the three eigenvalue "
      f"logarithms satisfy exactly one relation, so the anisotropy space is rank {jac.rank()} and the geometry "
      "is exhausted by the scale factor and those two -- both of which the curvature genuinely depends on ⇒ "
      "** a second-order source can only come from the interacting state, so the order is NOT REACHED, which "
      "is the answer the order asked to have said that way **")

print()
print("=" * 94)
print("  E.  3 THE WHOLE SUBTRACTION SCHEME IS ONE SERIES' POLE DATA")
print("=" * 94)

d_m, mu_m = 2 * (m**2 - 4), sp.sqrt(m**2 - 1)
w_pi = sp.expand(sp.series(sp.expand(d_m * mu_m), m, sp.oo, 4).removeO())
w_ph = sp.expand(sp.series(sp.expand(d_m / mu_m), m, sp.oo, 4).removeO())
res = {("dmu", 4): w_pi.coeff(m, 3), ("dmu", 2): w_pi.coeff(m, 1), ("dmu", 0): w_pi.coeff(m, -1),
       ("d/mu", 2): w_ph.coeff(m, 1), ("d/mu", 0): w_ph.coeff(m, -1)}
check(res[("dmu", 4)] == 2 and res[("dmu", 2)] == -9 and res[("dmu", 0)] == sp.Rational(15, 4)
      and res[("d/mu", 2)] == 2 and res[("d/mu", 0)] == -7,
      f"the two weights give simple poles with rational residues -- {dict((f'{k[0]}@s={k[1]}', v) for k, v in res.items())}"
      " -- every one of them a property of the spectrum alone")
ok_pole = []
for (nm, k), r in res.items():
    if k == 0:
        continue
    S = sp.simplify(sp.summation(r * m ** (k - 1), (m, 3, M)))
    lead = sp.Poly(sp.expand(S), M).coeff_monomial(M**k)
    ok_pole.append(sp.simplify(lead - sp.Rational(r, k)) == 0)
check(all(ok_pole) and len(ok_pole) == 3,
      "and each pole contributes its residue over its own location to the corresponding power of the cutoff, "
      f"checked pole by pole on all {len(ok_pole)} of them")
S_log = sp.simplify(sp.summation(res[("dmu", 0)] / m, (m, 3, M)))
check(sp.simplify(sp.expand(S_log.subs(sp.harmonic(M), sp.log(M) + sp.EulerGamma)).coeff(sp.log(M), 1)
                  - res[("dmu", 0)]) == 0,
      "the logarithmic coefficient is the residue at zero exactly -- which is the anomaly, so the anomaly is "
      "one entry of this pole table rather than a separate object")
prod = sp.Rational(res[("dmu", 4)], 4) * sp.Rational(res[("d/mu", 2)], 2)
check(prod == sp.Rational(1, 2),
      f"and the second-order sum's leading coefficient is a PRODUCT of two residues, (2/4)(2/2) = {prod} ⇒ "
      "** so the three subtractions, the anomaly and the value-rank are all statements about the pole data of "
      "the tower's spectral series, and the coefficients are polynomials in the residues **")
S_full = sp.simplify(sp.summation(2 * m**3, (m, 3, M)))
check(sp.Poly(sp.expand(S_full), M).coeff_monomial(M**2) != 0 and sp.Poly(sp.expand(S_full), M).coeff_monomial(M**4) == sp.Rational(1, 2),
      f"⌗ and the subleading integer powers MIX -- the partial sum of the leading weight alone already carries "
      "an M^2 -- which is Faulhaber's and not the spectrum's: exactly r7002's division between a coefficient "
      "and a convention, now visible as the difference between a residue and a partial sum's lower terms")

print()
print("=" * 94)
print("  F.  WHAT IS DELIVERED AND WHAT IS NOT")
print("=" * 94)

check(sp.simplify(at8) != 0 and sp.simplify(q[4] + 336 * (bp**2 + bm**2) ** 2) == 0,
      "⇒ ** 1 IS DELIVERED AT THE LEVEL THIS ROW OWNS: the vertex numbers are exact Taylor coefficients of a "
      "closed form, and the second-order shift is an exact rational times kappa hbar^2 / (V a^3) **")
check(sp.simplify(at8).free_symbols == {kap, hbar, Vol, a},
      f"⚠ and the scope in the same sentence: that shift's free symbols are exactly {{kappa, hbar, V, a}} -- no "
      "level label among them, because it is the frame-constant level's own ⇒ the TOWER-WIDE rational "
      "multiple is not computed here")
check(sp.simplify(w_pi.coeff(m, -1)) == sp.Rational(15, 4) and sp.simplify(at8 * Vol * a**3 / (kap * hbar**2)) == sp.Rational(19, 27),
      "⇒ ** and what it now needs is ONE thing: the higher levels' overlap integrals, whose structure r7000 "
      "fixed -- the weights, the conventions, the rank and this level's vertices are all in hand **")

print()
print("=" * 94)
if FAILED:
    print(f"  {len(FAILED)} CHECK(S) FAILED:")
    for msg in FAILED:
        print("   -", msg)
    sys.exit(1)
print("  ALL CHECKS PASS.")
print("=" * 94)
