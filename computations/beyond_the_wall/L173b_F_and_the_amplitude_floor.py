#!/usr/bin/env python3
"""
`L-173`.  ** $F$ IS COMPUTED — AND IT RETURNS A VERDICT THE ROW DID NOT ANTICIPATE: THE PROGENITOR'S
OWN VACUUM, AMPLIFIED BY THE BRANCH-POINT MIXING, FALLS $\\sim10^{104}$ SHORT OF THE OBSERVED $A_s$.
SO $A_s$ IS NOT AN INSTRUMENT; IT IS A CLASSICAL DATUM, AND NOW FOR A REASON. **

c54.136 established that $\\hbar$ survives in $A_s$ and cancels in $n_s$, and closed with
$A_s=F(2M/\\alpha)$, $F$ uncomputed.  This computes $F$.  The pieces were all banked: the collapse
leg is $\\beta=2$ (c54.122), the crunch monodromy is unipotent with off-diagonal $2\\pi/\\rho$
(c54.131), and the interior is dust + radiation exactly (c54.130).  What was missing was the
NORMALISATION carried through all three rather than tracked as a scaling.

  PART 1  ** THE BACKGROUND IS ONE FUNCTION AND ITS MS POTENTIAL IS $M$-FREE:
          $z''/z = 2/(|\\sigma|(|\\sigma|+2\\rho))$ — matter at $|\\sigma|\\gg2\\rho$, radiation below. **
  PART 2  ** THE CONNECTION COEFFICIENT: the growing mode's matter amplitude $D/|\\sigma|$ arrives at
          the crunch as the constant $c_0=(3/2\\rho)D$.  Closed form, then integrated. **
  PART 3  ** $F$ ASSEMBLED.  $A_s=(9/4)(\\ell_P/M)^2\\rho^{-6}$ — scale-invariant, and a function of
          TWO moduli, not one. **
  PART 4  ** THE NUMBER, AND IT IS NOT CLOSE: $2\\times10^{-113}$ against $2\\times10^{-9}$. **
  PART 5  ** WHAT THAT SETTLES: P15 `prop:amplitude` ruled out the SUBSTRATE's vacuum and the corpus
          read the classical character off it.  The PROGENITOR's vacuum was never checked, and it
          is the one the inheritance story actually needs.  It is checked here, and it fails too. **

Run: python3 L173b_F_and_the_amplitude_floor.py      (numpy, scipy, sympy)
"""
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE BACKGROUND, AND ITS M-FREE POTENTIAL")
print("=" * 78)
sig, M_, rho_, A_, B_ = sp.symbols('sigma M rho A B', positive=True)
x = sp.symbols('x', positive=True)                       # x = |sigma|, crunch at x = 0

print("  c54.130's exact closed interior is a(eta) = (A/2)(1-cos eta) + sqrt(B) sin eta, and at the")
print("  crunch a'(eta_c) = -sqrt(B) (radiation), a''(eta_c) = A/2 (dust).  With rho = 2 sqrt(B)/A")
print("  and A = 2M this is, in x = |sigma| = |eta - eta_c|,")
a_x = M_ * (rho_ * x + x**2 / 2)
print(f"     ** a(x) = {a_x} **        (exact to O(x^3))")
print()
print("  and the SAME function comes off the bead law by a route with no step in common:")
tau, al = sp.symbols('tau alpha', positive=True)
a_tau = (sp.Rational(9, 2) * M_ * tau**2)**sp.Rational(1, 3)      # r^3 = (9/2) M tau^2
eta_tau = sp.integrate(1 / a_tau, tau)
tau_of_eta = sp.solve(sp.Eq(eta_tau, x), tau)[0]
a_of_eta = sp.simplify(a_tau.subs(tau, tau_of_eta))
print(f"     r^3 = (9/2) M tau^2  ⇒  eta = {sp.simplify(eta_tau)}  ⇒  a = {a_of_eta}")
assert sp.simplify(a_of_eta - M_ * x**2 / 2) == 0
print("  ** = M x^2 / 2, which is the rho -> 0 limit of the line above, exactly. **")
print("  *Two derivations, one from the closed dust+radiation interior and one from the bead's own")
print("   cosmogenesis law, and they agree on the coefficient and not merely the power.*")
print()

U = sp.simplify(sp.diff(a_x, x, 2) / a_x)
print(f"  The Mukhanov--Sasaki potential with z ∝ a is z''/z = a''/a =")
print(f"     ** {sp.simplify(sp.factor(U))} **")
assert sp.simplify(U - 2 / (x * (x + 2 * rho_))) == 0
print("  ** and M has CANCELLED: the potential depends on rho alone. **")
print(f"  {'regime':>28} {'condition':>18} {'z''/z':>16} {'exponents':>14}")
for nm, cond, pot, ex in [("matter-dominated contraction", "x >> 2 rho", "2/x^2", "(-1, 2)"),
                          ("radiation-dominated crunch", "x << 2 rho", "1/(rho x)", "(0, 1)")]:
    print(f"  {nm:>28} {cond:>18} {pot:>16} {ex:>14}")
print()
for s in [
 "⇒ ** SO THE ENTIRE COLLAPSE-SIDE PROBLEM IS ONE ONE-PARAMETER FAMILY, and $M$ enters ONLY through",
 "   the overall scale of $a$ — i.e. only in the final division $\\zeta=v/a$. **  *That is why the",
 "   answer below factorises into a mass part and a composition part.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CONNECTION COEFFICIENT")
print("=" * 78)
print("  At k = 0 the equation v'' = (a''/a) v has the two exact solutions v = a and v = a ∫ dx/a^2.")
print("  The second is the one that DOMINATES the contraction.  Its integral is elementary:")
I = sp.integrate(1 / a_x**2, x)                 # sympy's choice fixes the constant by I -> 0 at oo
v0 = sp.simplify(a_x * I)
print(f"     ∫ dx/a^2 = {sp.simplify(I)}")
print("     (the constant of integration is fixed by ∫ -> 0 as x -> oo; adding a constant adds a")
print("      multiple of the OTHER solution v = a, which is precisely the v_0/v_1 basis ambiguity)")
print()
lim0 = sp.simplify(sp.limit(v0, x, 0))
print(f"  ** as x -> 0 :  v0 -> {lim0} **                (a CONSTANT — the s = 0 Frobenius root)")
assert sp.simplify(lim0 + 1 / (M_ * rho_)) == 0
# the x -> oo coefficient.  sympy's series mis-cancels the two logs here, so it is taken
# numerically at high precision instead -- the expression is an exact one, only the limit is hard.
v0_num = sp.lambdify(x, v0.subs({M_: 1, rho_: sp.Rational(1, 1000)}), 'mpmath')
mp.mp.dps = 60
tail = [mp.mpf(x_) * v0_num(mp.mpf(x_)) for x_ in ['1e4', '1e5', '1e6']]
print(f"  ** as x -> oo:  x * v0 -> {float(tail[-1]):.10f}  (M = 1)  = -2/(3M) **")
print(f"     at x = 1e4, 1e5, 1e6 :  {', '.join(f'{float(t):.10f}' for t in tail)}")
assert abs(float(tail[-1]) + 2.0 / 3.0) < 1e-8
coef = -2 / (3 * M_)
ratio = sp.simplify(lim0 / coef)
print()
print(f"  ** so a growing mode of amplitude D (i.e. v -> D/x in the matter era) arrives at the")
print(f"     crunch as the constant  c_0 = {ratio} * D. **")
assert sp.simplify(ratio - sp.Rational(3, 2) / rho_) == 0
print("  ** M cancels in the ratio, as it must: the connection is a property of the potential. **")
print()
print("  The log that the (0,1) resonance forces is present and subleading in v itself:")
print("     v0 = -1/(M rho) + O(x ln x)     -- the resonance's signature, not its leading term")

# ---- numerical confirmation on the FULL equation, from vacuum data -------------
print()
print("  NUMERICAL CONFIRMATION, on the full k != 0 equation from vacuum initial data.")
print("  Vacuum on the contracting side: v -> e^{i k x}/sqrt(2k) as x -> oo (hbar = 1).")
print("  Prediction:  |c_0| * k^(3/2) * rho  =  3 / (2 sqrt 2)  =  1.06066 , for all k with k rho << 1.")


def c0_c1(k, rho, x_f=None, n_osc=300.0):
    """integrate v'' + (k^2 - 2/(x(x+2rho))) v = 0 inward; return |c0|, |c1|"""
    if x_f is None:
        x_f = 1e-4 * rho
    x_i = n_osc / k

    def rhs(xx, y):
        pot = 2.0 / (xx * (xx + 2.0 * rho))
        return [y[1], (pot - k**2) * y[0], y[3], (pot - k**2) * y[2]]

    n = np.sqrt(2.0 * k)
    # v = e^{i k x}/sqrt(2k), dv/dx = i k v
    y0 = [np.cos(k * x_i) / n, -k * np.sin(k * x_i) / n,
          np.sin(k * x_i) / n, k * np.cos(k * x_i) / n]
    sol = solve_ivp(rhs, [x_i, x_f], y0, rtol=1e-12, atol=1e-16, method='DOP853')
    v = sol.y[0, -1] + 1j * sol.y[2, -1]
    vx = sol.y[1, -1] + 1j * sol.y[3, -1]
    c1 = -vx                      # v ~ c0 - c1 x   (v1 = sigma = -x)
    c0 = v + c1 * x_f
    return abs(c0), abs(c1)


TARGET = 3.0 / (2.0 * np.sqrt(2.0))
print(f"\n  {'rho':>10} {'k':>8} {'|c0|':>16} {'|c0| k^(3/2) rho':>20} {'3/(2 sqrt2)':>14}")
ok = []
for rho in [1e-3, 1e-4]:
    for k in [2.0, 5.0, 10.0, 30.0]:
        c0, c1 = c0_c1(k, rho)
        val = c0 * k**1.5 * rho
        ok.append(abs(val / TARGET - 1))
        print(f"  {rho:>10.0e} {k:>8.1f} {c0:>16.6g} {val:>20.6f} {TARGET:>14.6f}")
print(f"\n  ** worst relative departure over the grid: {max(ok)*100:.2f}% **")
assert max(ok) < 0.03, max(ok)
print()
print("  ** AND THE SAME CLOSED FORM HANDS BACK c54.131's MONODROMY, WHICH WAS OBTAINED NUMERICALLY. **")
print("  Normalising v0 to 1 at the crunch, the subleading term is the resonance's logarithm:")
print("     v_0(x) = 1 + (x/rho) ln(x / 2 rho) + O(x)")
v0hat = sp.simplify(-M_ * rho_ * v0)
resid = sp.simplify(v0hat - 1 - (x / rho_) * sp.log(x / (2 * rho_)))
chk = [(float(xx), float(sp.N(resid.subs({rho_: sp.Rational(1, 1000), x: sp.Float(xx)}), 30) / xx))
       for xx in [1e-7, 1e-8, 1e-9]]
print(f"  {'x':>12} {'[v_0 - 1 - (x/rho)ln(x/2rho)] / x':>36}   (rho = 1e-3; must approach a constant)")
for xx, r in chk:
    print(f"  {xx:>12.0e} {r:>36.6f}")
assert abs(chk[-1][1] - chk[-2][1]) < 1e-3 * abs(chk[-1][1])
print()
print("  Continue x once around the branch point.  With v_1 = sigma = -x, the log term gains")
print("     (x/rho)(2 pi i) = -(2 pi i / rho) v_1 ,   i.e.   v_0 -> v_0 - (2 pi i/rho) v_1 ,")
print("  ** which is exactly v_0 -> v_0 + 2 pi i p v_1 with p = -1/rho — c54.131's result, there")
print("     obtained by numerical continuation at four values of rho, here in closed form. **")
print()
for s in [
 "✔✔ ** THE CLOSED FORM AND THE INTEGRATION AGREE TO BETTER THAN THREE PER CENT ACROSS A DECADE IN",
 "   $\\rho$ AND A FACTOR FIFTEEN IN $k$ — and the $k^{-3/2}$ is the scale invariance of the",
 "   $\\beta=2$ leg surviving the passage through equality intact. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — F ASSEMBLED")
print("=" * 78)
print(f"  {'step':>46} {'factor':>30}")
for a, bb in [("vacuum, frozen on the beta = 2 leg", "D = sqrt(hbar/2) k^(-3/2)"),
              ("connection through equality (PART 2)", "c_0 = (3/2 rho) D"),
              ("monodromy at the crunch (c54.131)", "C = |2 pi i p| c_0 = (2 pi/rho) c_0"),
              ("the survivor's curvature, zeta = v/a", "zeta = C / (M rho)"),
              ("the spectrum", "P = (k^3/2 pi^2) |zeta|^2")]:
    print(f"  {a:>46} {bb:>30}")
hbar, kk, Msym, rr = sp.symbols('hbar k M rho', positive=True)
D = sp.sqrt(hbar / 2) * kk**sp.Rational(-3, 2)
c0s = sp.Rational(3, 2) / rr * D
Cs = 2 * sp.pi / rr * c0s
zeta = Cs / (Msym * rr)
P = sp.simplify(kk**3 / (2 * sp.pi**2) * zeta**2)
print()
print(f"  ** P_zeta(k) = {sp.simplify(P)} **")
assert sp.simplify(P - sp.Rational(9, 4) * hbar / (Msym**2 * rr**6)) == 0
assert sp.simplify(sp.diff(P, kk)) == 0
print("  ** and k has CANCELLED IDENTICALLY: the spectrum is scale-invariant, n_s = 1 exactly at")
print("     this order, which is c54.122's result arriving through the crossing rather than before")
print("     it. **")
print()
print("  In G = c = 1 the combination hbar/M^2 is (l_P/M)^2 with l_P^2 = hbar G / c^3, so")
print()
print("     ***  A_s  =  (9/4) (l_P / M)^2 rho^(-6)  ***")
print()
for s in [
 "⇒⇒⇒ ** SO $F$ IS NOT A FUNCTION OF ONE MODULUS.  It is a function of TWO — the mass and the",
 "   composition — and the second enters at the SIXTH POWER. **  *`L-173` was registered on the",
 "   premise that the construction has essentially one modulus; it has two, and the one nobody was",
 "   tracking is the one with all the leverage.*",
 "",
 "⌗ ** WHERE THE SIX POWERS COME FROM, since a $\\rho^{-6}$ is the kind of thing one should be able",
 "   to say out loud: two from the connection (PART 2, squared), two from the monodromy (c54.131,",
 "   squared), and two from $a'(\\eta_c)=-M\\rho$ — the crunch's own slope, which is small exactly",
 "   because the radiation fraction is small. **  *Three independent factors of $1/\\rho$, one per",
 "   stage of the passage, and none of them optional.*",
 "",
 "⌗ *Convention: $z=a$ is used throughout.  The hydrodynamical normalisation",
 "   $z=a\\sqrt{3(1+w)/8\\pi G}/c_s$ multiplies $A_s$ by $8\\pi/3$.  Nothing below turns on it.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3b — A BREAK THAT IS NOT THERE  [ WITHDRAWN c54.139 ]")
print("=" * 78)
for s_ in [
 "⚠⚠⚠ ** THIS PART ARGUED THAT THE FLAT BRANCH EXISTS ONLY FOR $k<1/\\rho$, AND SO TIGHTENED",
 "   c54.133's BOUND TENFOLD TO $\\rho\\le1.1\\times10^{-3}$.  IT IS WITHDRAWN. **",
 "   *A flat branch is what VACUUM data manufacture, and PART 5 of this very computation establishes",
 "   that the data are not vacuum, by $10^{94}$.  **The assumption was retired in the amplitude and",
 "   re-used, in the same file, to sharpen a bound.***",
 "",
 "✔ ** WHAT SURVIVES IS c54.133's CROSSOVER, BECAUSE IT IS A RATIO AND NOT A NORMALISATION: WKB",
 "   fixes $|c_0|/|c_1|=1/(c_sk)$ whatever the incoming amplitude, so",
 "   $\\mathcal{P}_{\\rm out}/\\mathcal{P}_{\\rm in}\\propto(c_sk+2\\pi/\\rho)^2$ — a transfer independent",
 "   of the data entirely.  The bound is that this stay flat across the observed range. **",
 "   *`L150h_which_side_of_equality_did_the_observed_modes_cross.py` carries the retraction and the",
 "   reconciliation it opens: P15's transmission account and the $\\beta=2$ freezing account are not",
 "   rivals but PARTITION the observed range, splitting near $\\ell\\simeq115$.*",
]:
    print("  " + s_)
rho_break = 0.0539       # c54.143: the composition DETERMINED (one M + a crossing plasma)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE NUMBER")
print("=" * 78)
LAM = 1.1056e-52          # m^-2
LP = 1.616255e-35         # m
MPC = 3.0857e22           # m
AS_OBS = 2.1e-9
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))               # c54.135: 2M <= 2 alpha/(3 sqrt 3)
print(f"  {'quantity':>44} {'value':>18}")
for nm, v, u in [("alpha = sqrt(3/Lambda)", alpha / MPC, "Mpc"),
                 ("M_max = alpha/(3 sqrt 3)   (c54.135, Nariai)", M_nar / MPC, "Mpc"),
                 ("(l_P / M_max)^2", (LP / M_nar)**2, ""),
                 ("(l_P / alpha)^2  [P15 prop:amplitude's number]", (LP / alpha)**2, "")]:
    print(f"  {nm:>44} {v:>18.4g} {u}")


def As_vac(rho, M=M_nar):
    return 2.25 * (LP / M)**2 * rho**(-6.0)


print(f"\n  the parent's DETERMINED composition (c54.143):  rho = {rho_break:.4g}"
      f"   (rho_r/rho_m|max = {rho_break**2/4:.2e})")
print(f"\n  {'rho':>14} {'rho_r/rho_m at a_max':>22} {'A_s from the vacuum':>22} {'shortfall':>14}")
for rho in [1.0, 0.2, rho_break, 1e-2, 1e-3]:
    v = As_vac(rho)
    print(f"  {rho:>14.4g} {rho**2/4:>22.3e} {v:>22.4e} {AS_OBS/v:>14.2e}")
v133 = As_vac(rho_break)
print(f"\n  ** AT THE MOST GENEROUS COMPOSITION THE SKY ALLOWS, THE VACUUM DELIVERS "
      f"{v133:.2e} **")
print(f"  ** AGAINST AN OBSERVED {AS_OBS:.1e}.  SHORT BY {AS_OBS/v133:.1e}. **")
assert 1e101 < AS_OBS / v133 < 1e106

rho_need = (2.25 * (LP / M_nar)**2 / AS_OBS)**(1.0 / 6.0)
print(f"\n  Run backwards, the vacuum reaches the observed amplitude only at")
print(f"     ** rho = {rho_need:.3e} ,  i.e. rho_r/rho_m|max = {rho_need**2/4:.3e} **")

# ---- does that composition survive nucleosynthesis on the same leg? ----------
print()
print("  ** AND THAT COMPOSITION HAS TO SURVIVE P16's NUCLEOSYNTHESIS ON THE SAME LEG. **")
print("  Equality sits at a_eq = A rho^2/4 with A = 2M, and the temperature there follows from")
print("  rho_m(a_eq) = 3 A c^2/(8 pi G a_eq^3) with no further input:")
G, C = 6.674e-11, 2.99792458e8
HBARC = 1.0545718e-34 * C
GSTAR, JperGeV = 10.75, 1.602176634e-10   # g_* AT the MeV threshold where the bound bites


def T_eq_GeV(rho, M=M_nar):
    A = 2 * M
    a_eq = A * rho**2 / 4.0
    rho_mass = 3 * C**2 * A / (8 * np.pi * G * a_eq**3)      # kg m^-3
    u = rho_mass * C**2                                       # J m^-3
    kT4 = 30 * u * HBARC**3 / (np.pi**2 * GSTAR)
    return kT4**0.25 / JperGeV


print(f"\n  {'rho':>14} {'T_eq':>16} {'rho_r/rho_m at T = 1 MeV':>28} {'BBN runs in':>16}")
for rho in [rho_break, 1e-3, 1e-5, rho_need]:
    Te = T_eq_GeV(rho)
    frac = Te / 1e-3                       # a/a_eq at 1 MeV = T_eq/T
    print(f"  {rho:>14.3e} {Te*1e9:>13.3g} eV {1.0/frac:>28.3e} "
          f"{'radiation' if frac < 1 else 'MATTER':>16}")
assert T_eq_GeV(rho_break) < 1e-3            # T_eq below an MeV: BBN is radiation-dominated
assert T_eq_GeV(rho_need) > 1e-3           # T_eq above an MeV: BBN is matter-dominated
# the composition at which BBN stops being radiation-dominated
lo, hi = rho_need, rho_break
for _ in range(200):
    mid = np.sqrt(lo * hi)
    if T_eq_GeV(mid) > 1e-3:
        lo = mid
    else:
        hi = mid
rho_bbn = np.sqrt(lo * hi)
print(f"\n  ** nucleosynthesis is radiation-dominated only for rho >~ {rho_bbn:.2e} **")
print("  ⌗ g_* is taken at 10.75, its value AT the MeV threshold this bound is set by;")
print("    at the bound itself T_eq sits in the keV range where g_* ~ 3.4, which moves")
print("    T_eq by a factor 1.3 and the threshold not at all.")
print(f"  ** the vacuum needs                                   rho  = {rho_need:.2e} **")
print(f"  ** i.e. {rho_bbn/rho_need:.1e} times more geometric stacking than the leg's own BBN permits. **")
assert rho_need < rho_bbn
print()
for s in [
 "⌗⌗ ** AND THAT LOWER BOUND IS ITSELF NEW, AND IT CORRECTS `L-172`. **  *That row's BBN check used",
 "   OUR OWN $T_{\\rm eq}=0.8\\,$eV for the parent's leg.  The parent's equality temperature is not a",
 "   free input — it follows from its own $A$ and $\\rho$ by the line above — and once computed it",
 "   bounds $\\rho$ from BELOW, which `L-172` did not have.*  **So the progenitor's composition is",
 "   now bracketed on both sides for the first time:**",
]:
    print("  " + s)
print(f"\n     ***  {rho_bbn:.1e}  <=  rho  <=  {rho_break:.1e}  ***")
print(f"     ***  {rho_bbn**2/4:.1e}  <=  rho_r/rho_m at maximum expansion  <=  {rho_break**2/4:.1e}  ***")
print(f"\n  *BBN from below (radiation must dominate at an MeV), the sky's flatness from above")
print(f"   (c54.133).  A window {rho_break/rho_bbn:.0e} wide, and the vacuum amplitude sits"
      f" {rho_bbn/rho_need:.0e} outside it.*")
print(f"  ⚠ *The lower end carries an $M$ dependence the upper end does not: $T_{{\\rm eq}}\\propto")
print(f"    A^{{-1/2}}\\rho^{{-3/2}}$, so a lighter progenitor tightens it.  Quoted at the Nariai cap.*")
print()
for s in [
 "⇒⇒⇒ ** SO THE TWO ROUTES TO THE PROGENITOR'S COMPOSITION DO NOT MEET, AND THEY MISS BY THIRTEEN",
 "   ORDERS OF MAGNITUDE. **  *The construction determines $\\rho\\simeq5\\times10^{-2}$;",
 "   nucleosynthesis on the same leg needs $\\rho\\gtrsim10^{-6}$; and the vacuum amplitude would need",
 "   $\\rho\\sim10^{-19}$, where equality sits above the GUT scale and helium synthesis runs in a",
 "   matter-dominated universe expanding some $10^{10}$ times too fast.*",
 "",
 "⌗ ** THIS IS THE OVERDETERMINATION `L-172` WENT LOOKING FOR AND DID NOT FIND. **  *That row",
 "   returned three constraints acting on three nearly independent quantities, which is no test at",
 "   all.  Adding $A_s$ closes it: three constraints, two moduli — **and the closure fails, which is",
 "   the outcome a real test is allowed to have.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THAT SETTLES")
print("=" * 78)
print("  P15 `prop:amplitude` establishes that the SUBSTRATE's de Sitter vacuum sits at ~1e-122 and")
print("  is short of A_s by ~1e113, and the paper reads off it that the fluctuations are 'classical,")
print("  inherited content -- boundary data from the progenitor'.")
print()
print(f"  {'vacuum':>44} {'delivers':>14} {'short by':>12}")
for nm, v in [("the substrate's own (P15 prop:amplitude)", (LP / alpha)**2),
              ("the progenitor's, no amplification", (LP / M_nar)**2),
              ("the progenitor's, WITH the mixing (this)", v133)]:
    print(f"  {nm:>44} {v:>14.2e} {AS_OBS/v:>12.1e}")
print()
for s in [
 "⚠⚠ ** AND THE GAP IN THE ARGUMENT IS NOW VISIBLE: `prop:amplitude` rules out the SUBSTRATE's",
 "   vacuum, and the classical-character conclusion was drawn from it — but the story the",
 "   proposition supports is that the amplitude comes from the PROGENITOR, whose own vacuum the",
 "   proposition says nothing about. **  *The one thing ruled out was the one thing the picture was",
 "   not claiming.*",
 "",
 "✔✔✔ ** THE HOLE IS FILLED HERE, AND IT FILLS THE RIGHT WAY: the progenitor's vacuum, amplified by",
 "   the full three-stage passage — freeze on the $\\beta=2$ leg, connect through equality, mix at",
 "   the crunch — reaches $2\\times10^{-113}$ and is short by $10^{104}$.  ** So the classical,",
 "   non-vacuum character of the primordial statistics is now DERIVED for the source that actually",
 "   supplies them, and not only for the one that does not. ** *P15's `sec:predictions` has listed",
 "   it as an established signature all along; it was established for the wrong vacuum.*",
 "",
 "⇒⇒ ** AND `L-173`'s HOPED INVERSION IS DEAD, WITH A CAUSE OF DEATH.  $A_s$ does not measure the",
 "   progenitor's mass, because $F$ does not carry a fixed normalisation: the amplitude entering",
 "   the passage is a CLASSICAL datum of the parent, free at this level of description. **",
 "   *What the calculation leaves standing is the TRANSFER, which is parameter-free and is a real",
 "   result:*",
 "",
 "        ***  A_s^out  =  (9/2) k^3 D_k^2 / (M^2 rho^6)  ***",
 "",
 "   *for any incoming growing-mode amplitude $D_k$ — quantum or classical.  **The construction",
 "   fixes how much the crossing multiplies an amplitude; it does not fix the amplitude.  That is",
 "   c54.128's one-constant theorem again, now with the multiplier computed.***",
 "",
 "⌗ ** AND THE SIZE OF THAT CLASSICAL DATUM IS NOW A NUMBER RATHER THAN A PLACEHOLDER: since",
 "   $A_s\\propto D_k^2$, the parent's growing-mode amplitude must exceed its OWN vacuum's by",
 f"   $\\sim10^{{{int(round(np.log10(np.sqrt(AS_OBS / v133)))) }}}$ at the top of the permitted"
 " composition window. **",
 "   *So this cosmology does not merely decline to predict $A_s$ — it says the parent's",
 "   perturbations were enormously super-vacuum, which is a statement about the previous generation",
 "   and not about ours.*",
 "",
 "⚠ *Bounds, stated rather than buried: (i) $z\\propto a$ with $c_s=1$ is assumed on the",
 "   $\\beta=2$ leg, which is c54.122's own hypothesis and is the standard matter-contraction",
 "   idealisation — genuine pressureless dust has $c_s=0$ and no vacuum oscillation to normalise;",
 "   (ii) the $10^{104}$ is so large that no $O(1)$ convention, and no plausible change in the",
 "   $c_s$ treatment, touches the conclusion; (iii) the BBN comparison uses standard $g_*$ and",
 "   standard thermodynamics on the parent's leg, as P16 already does.*",
]:
    print("  " + s)
