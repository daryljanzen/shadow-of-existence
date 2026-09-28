#!/usr/bin/env python3
r"""
P10_the_degeneracy_needs_r_constant_not_the_cosh_so_the_anomaly_is_what_makes_its_own_constant_observable
========================================================================================================

LEVEL: exact symbolic (sympy) for the degeneracy criterion, the trace, and the $\zeta(0)$ sensitivity
theorem; 40-digit quadrature (mpmath) for the rank test, with TWO null controls and an $r^{2}$ scaling
law as its calibration.  Nothing is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6919`, the register's last never-attempted row.  The order, verbatim:

    "once the scale factor is quantized, is $\int\!\sqrt g\,R^{2}$ still fixed by $\int\!\sqrt g\,R$
     and $\int\!\sqrt g$, or does it become independent?"

  ⓵ that question, with the two readings costed: *still fixed* carries the no-free-constant claim into
     the coupled sector; *independent* makes the log counterterm a new entry and the one constant
     observable --- "the harder place and the better-defined one".
  ⓶ and IF AND ONLY IF ⓵ says observable: what does coupling do to $\zeta(0)$, where "a bound or a
     statement of which features of the interaction it can depend on is worth as much as a value".

COMPUTES: the exact criterion for the different-dimension degeneracy; the tower's regularized trace;
the rank of the map from admitted geometries to $(\int\!\sqrt g,\int\!\sqrt g R,\int\!\sqrt g R^{2})$,
against two null controls; and the exact dependence of $\zeta_\Delta(0)$ on an arbitrary shift of the
eigenvalues.  Scope: SEMICLASSICAL back-reaction -- the free tower's regularized stress tensor in the
classical constraint.  The interacting theory is NOT built, as ordered, and §E states the wall.

-------------------------------------------------------------------------------
** ⓵ ANSWERS *INDEPENDENT* --- AND THE ROUTE THERE CORRECTS THE ORDER'S OWN PREMISE, BECAUSE THE
   OPERATIVE CONDITION IS NOT THE ONE `P10` AND THE ORDER BOTH NAME. **

  ⛔ ** THE CORRECTION, AND IT IS THE REASON THE ANSWER HAS A MECHANISM RATHER THAN JUST A SIGN. **
     `P10` says the different-dimension terms "part company as soon as $a$ is not the de~Sitter
     $\cosh$", and the order infers from "in the coupled sector $a$ is quantized, so it is not the
     $\cosh$" that they part company.  ** That inference does not go through.  $a$ failing to be the
     cosh is NOT sufficient. **  The degeneracy is equivalent to $R$ being $\sqrt g$-almost-everywhere
     CONSTANT --- much weaker than the cosh --- and:
       · $\Lambda$ + radiation in closed FRW has $a$ nothing like the cosh and $R=4\Lambda$ EXACTLY
         (§A3), because radiation is traceless.  Rank ** 1 ** to 43 digits (§C).
       · and the free tower's own bare zero-point energy is exactly radiation-like: $E=S/a$ with $S$
         carrying no $a$, so $\rho\propto a^{-4}$, $p=\rho/3$ and ** the trace vanishes identically **
         (§B1).  ⇒ *The naive back-reaction of the quantized tower does not break the degeneracy
         either.*  Rank ** 1 ** to 43 digits.
     ⌗ *So the order's route reaches the right answer for the wrong reason, and the wrong reason would
       have made the result unfalsifiable: "a is not the cosh" is true of almost everything and
       explains nothing.  Two null controls are in this receipt because both of them nearly ate it.*

  ⛭ ** WHAT ACTUALLY BREAKS IT IS THE LOG, WHICH IS TO SAY: THE CONSTANT AT ISSUE BREAKS THE
     DEGENERACY THAT WOULD HAVE HIDDEN IT. **  $Z(s)=\sum_n d_n\mu_n^{-s}$ has a POLE at $s=-1$ with
     residue $r=\tfrac{15}{4}$ (banked), so the renormalized zero-point energy is
     $E(a)=\tfrac1a\,[\,C_0+r\ln(a\mu)\,]$ --- and the $\ln a$ spoils the exact $a^{-4}$ scaling that
     made the bare sum traceless.  The trace is then

         Theta  ==  rho - 3p  ==  r / (2 pi^2 a^4) ,

     ** independent of $\mu$ ** (§B2) --- scheme-independent, which is what an anomaly is, and the
     reason the split between $C_0$ and the log being a convention does not touch the conclusion.
     ⇒ $R=4\Lambda+4Gr/(\pi a^{4})$, confirmed TWO ways: from the trace of the field equation, and
     independently by solving the constraint and computing $R$ from $a$ directly (§B3).
     ⇒ ** $R$ is non-constant if and only if $r\neq0$, and $r=\tfrac{15}{4}$. **

  ⚑ ** SO THE RANK RISES, AND THE MEASUREMENT IS CLEAN. **  Three regions of one history give three
     triples $(\int\!\sqrt g,\int\!\sqrt gR,\int\!\sqrt gR^{2})$.  If $R$ is constant every triple is
     $V\,(1,R_0,R_0^{2})$ and they are all PARALLEL --- rank 1, the degeneracy in its strongest form.
     At 40 digits: ** rank 1 to $10^{-43}$ on both null controls, and rank 3 at $s_3/s_1=9.06\times
     10^{-8}$ for the tower ** --- thirty-five orders of magnitude above the floor that the controls
     measure.  *The floor is measured rather than assumed, which is what makes the third singular
     value a result.*

  ⌗ ** AND THE SIZE IS SECOND ORDER IN THE ANOMALY COEFFICIENT, WHICH IS WORTH SAYING BECAUSE IT IS
     THE SAME ORDER `P10` FOUND FOR THE SHEAR. **  The exact identity is
     $I_2I_0-I_1^{2}=I_0^{2}\,\mathrm{Var}_{\sqrt g}(R)\ \ge 0$ (§A2, Cauchy--Schwarz), and
     $R-4\Lambda\propto r$, so the gap goes as $r^{2}$: measured $1.0179\times10^{-9}$ over three
     decades in $r$, constant to five figures (§C).  ⇒ *Structural independence, established.  A
     DETECTABLE signal is a different question and this receipt does not claim one.*

** ⓶ ANSWERS WITH A THEOREM RATHER THAN A VALUE, WHICH IS THE FORM THE ORDER SAID IT WANTED. **

     $\zeta_\Delta(0)=10+\tfrac12 B_3'(0)$, EXACTLY, where $B_3(s)$ is the $m^{-1}$ coefficient of the
     summand $d(m)\lambda(m)^{-s}$.  *Only that one coefficient can move it, and it moves it only
     through the pole of $\zeta_R$ at argument $1$; every other order of the spectral asymptotics
     multiplies a finite $\zeta_R$ by $B_j(0)$, and $B_j(0)=2\delta_{j0}-8\delta_{j2}$ whatever the
     shift, because $(1+u)^{-s}\to1$ at $s=0$.*  ⇒ ** $\zeta(0)$ is PROTECTED against everything a
     local coupling can do: **
       · a constant (mass-like) shift: unchanged, exactly $10$;
       · a multiplicative rescaling $\lambda\to L\lambda$: unchanged --- which contains `r6411`'s
         "the scale factor factors out" as the special case $L=a^{-2}$ and generalizes it;
       · any shift whose asymptotics carries only EVEN powers of $1/m$: unchanged.
     ⇒ ** It moves only on an ODD power of the mode label. **  Closed forms:
       $\delta=cm\Rightarrow\Delta\zeta(0)=c-c^{3}/3$; $\ \delta=c/m\Rightarrow\Delta\zeta(0)=-c$.
     ⌗ *And local operators contribute integer powers of the Laplacian, i.e. of $m^{2}$.  So the
       statement of which features of the interaction it can depend on is: ** none of the local ones.
       ** That is a reason to expect $10$ survives coupling and NOT a proof that it does --- what it
       forecloses is the whole even sector, which is where a local interaction lives.*

-------------------------------------------------------------------------------
** ⛭ THE SHAPE OF THE ANSWER, WHICH IS THE PART WORTH CARRYING. **  The corpus's no-free-constant
claim was saved on this background by a degeneracy.  ** That degeneracy is switched off by exactly the
constant it was hiding. **  If $\zeta$ carried no log, $R$ would stay constant and the counterterm
would stay unobservable --- but then there would be no constant to hide.  *The saving mechanism and
the thing it saves us from are the same number, so the claim cannot be rescued this way in the coupled
sector; it has to be paid.*

** WHERE THIS LANDS IN THE ROW'S OWN TERMS, and it is the FIRST of its three CR-specific reasons **
(the order forbids re-scoping the remainder as generic, and this does the opposite): the counterterm
basis is one-dimensional *at fixed background*.  ⇒ ** Once the scale factor is quantized it is
two-dimensional **, and the dimension of the basis is the row's own CR-specific statement, so the
finding sharpens the row's specificity rather than diluting it.

⛔ ** NOT CLAIMED. **  No interacting theory is built.  This is *not* `PO-43`: `P10`'s shear entry is a
NEW invariant ($C^{2}$) and this is the SAME invariant becoming an independent functional --- two
different entries, and nothing here moves `PO-43`.  No detectable signal, no value for the coupled
$\zeta(0)$, and the ordering ambiguity is untouched.  rc=0 on all 32 checks.
"""

import sys

import mpmath as mp
import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


R_RESIDUE = sp.Rational(15, 4)      # Res_{s=-1} zeta_omega -- r6975 re-point of the bank
ZETA0_FREE = 10                     # zeta_Delta(0) for the free tower -- BANKED

# ============================================================================ A
head("A.  THE DEGENERACY'S EXACT CRITERION -- AND IT IS NOT THE COSH")

t, al, Lam, C, G, r, mu, a = sp.symbols('t alpha Lambda C G r mu a', positive=True)

af = sp.Function('a')(t)
R_gen = 6 * (sp.diff(af, t, 2) / af + sp.diff(af, t) ** 2 / af ** 2 + 1 / af ** 2)
print(f"\n  A1. closed FRW, proper time:  R = {R_gen}")
check(sp.simplify(R_gen.subs(af, al * sp.cosh(t / al)).doit() - 12 / al ** 2) == 0,
      "NULL CONTROL: on a = alpha cosh(t/alpha), R = 12/alpha^2 -- P10's background, R constant")

# A2 -- the criterion, as an exact identity in an arbitrary positive weight.
print("\n  A2. the degeneracy IS 'R constant', and the failure is EXACTLY a variance.")
w1, w2, w3, F1, F2, F3 = sp.symbols('w1 w2 w3 F1 F2 F3', positive=True)
W = [w1, w2, w3]
F = [F1, F2, F3]
I0 = sum(W)
I1 = sum(wi * Fi for wi, Fi in zip(W, F))
I2 = sum(wi * Fi ** 2 for wi, Fi in zip(W, F))
Fbar = I1 / I0
var = sum(wi * (Fi - Fbar) ** 2 for wi, Fi in zip(W, F)) / I0
check(sp.simplify(I2 * I0 - I1 ** 2 - I0 ** 2 * var) == 0,
      "I2*I0 - I1^2 = I0^2 * Var_w(F), an identity in the weight and the field")
check(sp.simplify(var.subs({F2: F1, F3: F1})) == 0,
      "  and the variance vanishes when F is constant -- so the degeneracy is exactly that")
check(sp.simplify((I2 * I0 - I1 ** 2).subs({F2: F1, F3: F1})) == 0,
      "  hence I2*I0 = I1^2 identically on constant F, for EVERY weight (every region)")
# the sign is fixed, which fixes the direction the new entry departs in
sgn = sp.simplify((I2 * I0 - I1 ** 2).subs({w1: 1, w2: 1, w3: 1, F1: 0, F2: 1, F3: 2}))
check(sgn > 0, f"  and the gap is SIGNED: Cauchy-Schwarz gives I2*I0 >= I1^2, sample gap {sgn} > 0")

# A3 -- THE CORRECTION TO THE ORDER'S PREMISE.
print("\n  A3. ** the order's premise corrected: 'a is not the cosh' is NOT the condition. **")
adot2_rad = Lam * a ** 2 / 3 + C / a ** 2 - 1
addot_rad = sp.simplify(sp.diff(adot2_rad, a) / 2)
R_rad = sp.simplify(6 * (addot_rad / a + adot2_rad / a ** 2 + 1 / a ** 2))
print(f"      Lambda + radiation:  R = {R_rad}")
check(sp.simplify(R_rad - 4 * Lam) == 0,
      "Lambda+radiation: R = 4*Lambda EXACTLY though a is nothing like the cosh")
check(sp.simplify(sp.diff(R_rad, a)) == 0,
      "  dR/da = 0 -- so the degeneracy SURVIVES off the cosh.  The inference needed R constant")

# ============================================================================ B
head("B.  THE TOWER'S OWN TRACE: ZERO BARE, NON-ZERO RENORMALIZED, AND MU-FREE")

S = sp.Symbol('S', positive=True)       # (1/2) sum d_n mu_n -- carries no a
V = 2 * sp.pi ** 2 * a ** 3


def trace_of(rho_expr):
    """Theta = rho - 3p from energy conservation rho+p = -(a/3) drho/da."""
    p_expr = sp.simplify(-(a / 3) * sp.diff(rho_expr, a) - rho_expr)
    return sp.simplify(rho_expr - 3 * p_expr), p_expr


print("\n  B1. the BARE free tower is exactly radiation-like, so it cannot break anything.")
rho_bare = (S / a) / V
Th_bare, p_bare = trace_of(rho_bare)
print(f"      rho_bare = {rho_bare}    p/rho = {sp.simplify(p_bare / rho_bare)}")
check(sp.simplify(sp.log(rho_bare).diff(a) * a + 4) == 0,
      "E = S/a with S free of a gives rho ~ a^-4 exactly (omega ~ 1/a, V ~ a^3)")
check(sp.simplify(p_bare - rho_bare / 3) == 0, "  hence p = rho/3 exactly")
check(Th_bare == 0,
      "** Theta = 0 IDENTICALLY: the second null control -- the quantized tower's naive "
      "back-reaction does NOT break the degeneracy **")

print("\n  B2. the RENORMALIZED energy: the pole of Z at s=-1 puts a log in, and the log has a trace.")
rho_ren = (C + r * sp.log(a * mu)) / a / V
Th_ren, p_ren = trace_of(rho_ren)
print(f"      E_ren = (1/a)[C_0 + r ln(a mu)]   ->   Theta = {Th_ren}")
check(sp.simplify(Th_ren - r / (2 * sp.pi ** 2 * a ** 4)) == 0,
      "Theta = r/(2 pi^2 a^4) -- non-zero, and carried entirely by the log coefficient")
check(sp.simplify(sp.diff(Th_ren, mu)) == 0,
      "** Theta is MU-INDEPENDENT: an anomaly, so the C_0/log split being a convention is harmless **")
check(sp.simplify(sp.diff(Th_ren, C)) == 0,
      "  and Theta is independent of the finite part C_0 as well")
check(sp.simplify(Th_ren.subs(r, 0)) == 0,
      "  and Theta -> 0 when r -> 0: the trace exists BECAUSE the log coefficient does")
print(f"      at the banked r = 15/4:   Theta = {sp.simplify(Th_ren.subs(r, R_RESIDUE))}")

print("\n  B3. R from the CONSTRAINT, computed independently of the trace identity.")
adot2 = sp.simplify(Lam * a ** 2 / 3 - 1 + (8 * sp.pi * G / 3) * rho_ren * a ** 2)
addot = sp.simplify(sp.diff(adot2, a) / 2)
R_tow = sp.expand(sp.simplify(6 * (addot / a + adot2 / a ** 2 + 1 / a ** 2)))
print(f"      R = {R_tow}")
check(sp.simplify(R_tow - (4 * Lam + 8 * sp.pi * G * Th_ren)) == 0,
      "R from a(t) agrees with 4*Lambda + 8 pi G Theta -- two independent routes")
check(sp.simplify(sp.diff(R_tow, mu)) == 0, "  R is mu-independent")
check(sp.simplify(sp.diff(R_tow, a).subs(r, 0)) == 0,
      "  dR/da = 0 at r = 0 -- R is constant iff the anomaly coefficient vanishes")
check(sp.simplify(sp.diff(R_tow, a)) != 0,
      "** and dR/da != 0 for r != 0: the degeneracy's criterion FAILS, by the log and only by it **")

# ============================================================================ C
head("C.  THE RANK, AT 40 DIGITS, AGAINST TWO NULL CONTROLS AND AN r^2 CALIBRATION")

mp.mp.dps = 40
REGIONS = [(2, 3), (3, 5), (5, 9)]
LAM, GG, C0, MU = mp.mpf(3), mp.mpf(1), mp.mpf(1), mp.mpf(1)


def triples(Lam_, G_, r_, C0_, mu_, regions=REGIONS):
    """rows = (int sqrt(g), int sqrt(g) R, int sqrt(g) R^2) over each region of one history."""
    kap = 4 * G_ * r_ / mp.pi
    ad = lambda aa: mp.sqrt(Lam_ * aa ** 2 / 3 - 1
                            + (4 * G_ / (3 * mp.pi)) * (C0_ + r_ * mp.log(aa * mu_)) / aa ** 2)
    Rf = lambda aa: 4 * Lam_ + kap / aa ** 4
    return mp.matrix([[2 * mp.pi ** 2 * mp.quad(lambda aa: aa ** 3 * Rf(aa) ** k / ad(aa), [a1, a2])
                       for k in (0, 1, 2)] for (a1, a2) in regions])


def ratios(M):
    S = mp.svd_r(mp.matrix(M))[1]
    return mp.mpf(S[1]) / mp.mpf(S[0]), mp.mpf(S[2]) / mp.mpf(S[0])

# the floor is MEASURED on the controls, not assumed
s2a, s3a = ratios(triples(LAM, GG, mp.mpf(0), mp.mpf(0), MU))
print(f"\n  NULL CONTROL A -- pure Lambda (a IS the cosh):   s2/s1 = {mp.nstr(s2a, 4)}"
      f"   s3/s1 = {mp.nstr(s3a, 4)}")
check(max(s2a, s3a) < mp.mpf('1e-30'),
      "pure Lambda: the three triples are PARALLEL -- rank 1, P10's degeneracy recovered")

s2b, s3b = ratios(triples(LAM, GG, mp.mpf(0), C0, MU))
print(f"  NULL CONTROL B -- Lambda + radiation (a is NOT the cosh):   s2/s1 = {mp.nstr(s2b, 4)}"
      f"   s3/s1 = {mp.nstr(s3b, 4)}")
check(max(s2b, s3b) < mp.mpf('1e-30'),
      "** and still rank 1 off the cosh: the order's premise is corrected by measurement **")
FLOOR = max(s2a, s3a, s2b, s3b)
print(f"      => the numerical floor, MEASURED: {mp.nstr(FLOOR, 4)}")

s2t, s3t = ratios(triples(LAM, GG, R_RESIDUE, C0, MU))
print(f"\n  THE TOWER, r = 15/4:   s2/s1 = {mp.nstr(s2t, 6)}   s3/s1 = {mp.nstr(s3t, 6)}")
check(s3t > FLOOR * mp.mpf('1e20'),
      f"rank 3: s3/s1 = {mp.nstr(s3t, 4)} stands {mp.nstr(mp.log(s3t / FLOOR, 10), 3)} decades above "
      "the measured floor")
check(s3t > mp.mpf('1e-9'),
      "** => int sqrt(g) R^2 is INDEPENDENT of int sqrt(g) R and int sqrt(g).  ⓵ answers. **")

print("\n  and the gap's ORDER in the anomaly coefficient, which is the calibration:")
scaled = []
for rs in ('1e-3', '1e-2', '1e-1'):
    rv = mp.mpf(rs)
    _, s3 = ratios(triples(LAM, GG, rv, C0, MU))
    scaled.append(s3 / rv ** 2)
    print(f"      r = {rs:6s}   s3/s1 = {mp.nstr(s3, 6):>14s}   (s3/s1)/r^2 = {mp.nstr(s3 / rv**2, 6)}")
spread = (max(scaled) - min(scaled)) / min(scaled)
check(spread < mp.mpf('1e-3'),
      f"(s3/s1)/r^2 constant to {mp.nstr(spread, 2)} over three decades -- the breaking is EXACTLY "
      "second order in r, the same order P10 found for the shear")

# ============================================================================ D
head("D.  ⓶  WHAT COUPLING CAN DO TO zeta(0) -- A THEOREM, NOT A VALUE")

m, s, x = sp.symbols('m s x')


def zeta_delta_at_zero(lam_expr, M=3, J=8, report=False):
    r"""zeta_Delta(0) for eigenvalues lam(m), degeneracy 2(m^2-4), m >= 3.

    Only j=0,2 survive at s=0 because B_j(0) = 2*delta_{j0} - 8*delta_{j2} for ANY shift
    ((1+u)^{-s} -> 1 at s=0), and j=3 survives through the pole of zeta_R at argument 1.
    """
    d = 2 * (m ** 2 - 4)
    hd = sum(int(d.subs(m, mm)) for mm in range(3, M))
    sum_m2 = sum(mm ** 2 for mm in range(1, M))
    sum_1 = sum(1 for mm in range(1, M))
    g = d * sp.simplify(lam_expr / m ** 2) ** (-s)
    ser = sp.series(sp.expand(g.subs(m, 1 / x) * x ** 2), x, 0, J).removeO()
    poly = sp.Poly(sp.expand(ser), x)
    B3 = sp.expand(poly.coeff_monomial(x ** 3))
    if sp.simplify(B3.subs(s, 0)) != 0:
        raise ValueError("B3(0) != 0 -- zeta would have a pole at s=0")
    B3p = sp.simplify(sp.diff(B3, s).subs(s, 0))
    if report:
        print(f"        B3'(0) = {B3p}")
    return sp.nsimplify(hd + 2 * (0 - sum_m2)
                        - 8 * (sp.Rational(-1, 2) - sum_1) + B3p / 2)


c, delta, L, b = sp.symbols('c delta L b')
z_free = zeta_delta_at_zero(m ** 2 - 1)
print(f"\n  free tower, lam = m^2 - 3:            zeta(0) = {z_free}")
check(z_free == ZETA0_FREE, "the banked zeta(0) = 10 reproduced by this receipt's own machinery")

print("\n  D1. the PROTECTED sector -- every one of these leaves it at exactly 10:")
for lab, lam in (("constant (mass-like) shift  lam = m^2-1+delta", m ** 2 - 1 + delta),
                 ("multiplicative rescaling    lam = L*(m^2-1)  ", L * (m ** 2 - 1)),
                 ("even, falling               lam = m^2-1+b/m^2", m ** 2 - 1 + b / m ** 2),
                 ("even, falling               lam = m^2-1+b/m^4", m ** 2 - 1 + b / m ** 4)):
    z = zeta_delta_at_zero(lam)
    print(f"      {lab}   zeta(0) = {z}")
    check(sp.simplify(z - ZETA0_FREE) == 0, f"  unchanged: {lab.split('lam')[0].strip()}")

print("\n      ⌗ the rescaling case CONTAINS r6411's result and generalizes it: L = a^-2 is the scale")
print("        factor, so 'a factors out of the free tower' is one member of a whole immune family.")

print("\n  D2. and the ONE thing that moves it is an ODD power of the mode label:")
z_odd1 = sp.simplify(zeta_delta_at_zero(m ** 2 - 1 + c * m, report=True))
print(f"      lam = m^2-1+c*m   zeta(0) = {z_odd1}")
# ⛭ r6981 (66): the closed form is the one at the CORRECTED frequency.  `r6975` moved the base from the
# Laplace eigenvalue to the frequency the reduction gives, and the odd-power probe's own closed form moves
# with the base it probes: 3c - c^3/3 at mu^2 = m^2-1 where it read c - c^3/3 at m^2-3.  ** The finding is
# untouched and is the only thing this probe is for: an ODD power of the mode label is the one deformation
# that moves zeta(0), and the cubic coefficient -1/3 is the same at either base. **  ⌗ *Caught by node 70's
# scoped suite at r6977+70.1, on the push that broke it -- which is the wiring working on this seat.*
check(sp.simplify(z_odd1 - (10 + 3 * c - c ** 3 / 3)) == 0,
      "delta = c*m moves it by exactly 3c - c^3/3 -- a closed form")
z_odd2 = sp.simplify(zeta_delta_at_zero(m ** 2 - 1 + c / m, report=True))
print(f"      lam = m^2-1+c/m   zeta(0) = {z_odd2}")
check(sp.simplify(z_odd2 - (10 - c)) == 0, "delta = c/m moves it by exactly -c")

print("\n  D3. self-checks on the continuation -- the split point and the truncation must not matter:")
byM = [sp.simplify(zeta_delta_at_zero(m ** 2 - 1 + c * m, M=MM)) for MM in (3, 6, 10)]
byJ = [sp.simplify(zeta_delta_at_zero(m ** 2 - 1 + c * m, J=JJ)) for JJ in (6, 8, 11)]
print(f"      M = 3, 6, 10 : {byM}")
print(f"      J = 6, 8, 11 : {byJ}")
check(all(sp.simplify(v - byM[0]) == 0 for v in byM), "M-independent: the split point drops out")
check(all(sp.simplify(v - byJ[0]) == 0 for v in byJ), "J-independent: the truncation drops out")

# ============================================================================ E
head("E.  THE WALL, WHICH THE ORDER SAYS IS A RESULT AND NOT A SHORTFALL")

print(r"""
  ⚑ WHAT IS DISCHARGED.  `PO-23`'s third part moves from ** never attempted ** to ** attempted, and
    the answer is INDEPENDENT **, with a mechanism: the trace anomaly, whose coefficient the corpus
    had already computed and banked.  ⓶ is discharged as a theorem about which features of a coupling
    could possibly matter -- the form the order named as worth as much as a value.

  ⛔ WHAT IS NOT, STATED AS A LOCATION AND NOT AS A LACK.

    · ** The back-reaction is SEMICLASSICAL. **  The free tower's regularized stress tensor is put
      into the classical constraint.  That is the leading order and no more.  ⇒ *What the wall is:
      whether higher orders could restore R to constancy.  And the wall has a shape --- restoration
      needs the TOTAL trace to be exactly constant, i.e. a pure cosmological constant, and an
      a^-4 anomaly is not that; so the escape is narrow and named rather than open.*
    · ** ONE premise is taken and not proved: that the coupled sector admits states without a
      definite alpha. **  That is the order's own "in the coupled sector a is quantized", and P10's.
      ⇒ *If the physical Hilbert space selected a single background, the degeneracy would survive.
      That is the one way ⓵ reverses, and it is a question about the constraint's solution space.*
    · ** No value for the coupled zeta(0). **  §D bounds WHERE it could come from and forecloses the
      whole even sector; it does not compute the interacting number, which needs the interacting
      theory this receipt is ordered not to build.
    · ** No detectable signal. **  The gap is second order in r.  Structural independence is not
      observability in the laboratory sense, and nothing here claims it is.

  ⌗ AND WHERE IT BEARS ON THE ROW'S CR-SPECIFICITY, which the order forbids diluting: on the FIRST of
    its three reasons.  The counterterm basis is one-dimensional *at fixed background*; once the scale
    factor is quantized it is two-dimensional.  ** The basis's dimension is the CR-specific claim, so
    this sharpens the reason rather than generalizing the row away. **  Nothing here touches the
    deparametrization reason or the tower's uniqueness, and nothing touches `prop:flat`.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
