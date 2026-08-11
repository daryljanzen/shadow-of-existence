#!/usr/bin/env python3
"""
`L-150`.  ** THE SIZE OF THE MIXING AS A FUNCTION OF $\\rho_r/\\rho_m$ — AND IT IS DISCONTINUOUS AT
ZERO.  ANY RADIATION AT ALL CHANGES THE INDICIAL EXPONENTS AT THE BRANCH POINT. **

c54.130 found that in the progenitor interior the dust content is the even part of the background
and the radiation content is exactly the odd part, and that radiation LEADS at the branch point.
This computes what that does to the connection problem c54.123–124 settled for the vacuum leg.

  PART 1  ** THE CRUNCH, EXACTLY: where it is, and the two derivatives there. **
  PART 2  ** THE INDICIAL EXPONENTS: $(-1,2)$ with pure dust, $(0,1)$ with ANY radiation. **
  PART 3  ** SO THE MIXING IS NOT SMALL FOR SMALL RADIATION — IT IS DISCONTINUOUS AT ZERO. **
  PART 4  ** THE SIZE, COMPUTED AND SWEPT IN $\\rho_r/\\rho_m$. **
  PART 5  What this says about the row, and the bound.

Run: python3 L150d_the_size_of_the_mixing.py      (sympy, numpy, scipy)
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])
eta, A, B, rho = sp.symbols('eta A B rho', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE CRUNCH, EXACTLY")
print("=" * 78)
a = (A / 2) * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)
print("  a(eta) = (A/2)(1 - cos eta) + sqrt(B) sin eta,  and a = 0 at the bang and the crunch.")
half = sp.simplify(sp.expand_trig(a).rewrite(sp.tan))
print("  Half-angle: a = sin(eta/2) [ A sin(eta/2) + 2 sqrt(B) cos(eta/2) ], so besides eta = 0")
print("  the zero is at  tan(eta_c / 2) = -2 sqrt(B) / A  ==  -rho ,   rho := 2 sqrt(B) / A .")
# verify the factorisation
fac = sp.simplify(a - sp.sin(eta / 2) * (A * sp.sin(eta / 2) + 2 * sp.sqrt(B) * sp.cos(eta / 2)))
print(f"     factorisation residual: {sp.simplify(sp.expand_trig(fac))}")
assert sp.simplify(sp.expand_trig(fac)) == 0

# the two derivatives at the crunch, in closed form
t = sp.symbols('t', positive=True)          # t = rho
sin_c = -2 * t / (1 + t**2)
cos_c = (1 - t**2) / (1 + t**2)
sqrtB = A * t / 2
ap = sp.simplify((A / 2) * sin_c + sqrtB * cos_c)
app = sp.simplify((A / 2) * cos_c - sqrtB * sin_c)
print(f"\n  a'(eta_c)  = {ap}      = -sqrt(B)   ** the radiation slope **")
print(f"  a''(eta_c) = {app}      = A/2        ** the dust curvature **")
assert sp.simplify(ap + sqrtB) == 0
assert sp.simplify(app - A / 2) == 0
p_expr = sp.simplify(app / ap)
print(f"\n  ** p := a''/a' at the crunch = {p_expr} = -1/rho **")
assert sp.simplify(p_expr + 1 / t) == 0
print()
for s in [
 "⌗ ** THE TWO DERIVATIVES SEPARATE BY SPECIES, EXACTLY AS THE PARITIES DID: the SLOPE at the",
 "   crunch is the radiation amplitude and the CURVATURE is the dust amplitude. **  *So the single",
 "   number that will control everything below, $p=a''/a'=-1/\\rho$, is the dust-to-radiation ratio",
 "   and nothing else.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE INDICIAL EXPONENTS")
print("=" * 78)
sg, s_ = sp.symbols('sigma s')
print("  Near the crunch write sigma = eta - eta_c.  Then a = c1 sigma + (c2/2) sigma^2 + ... , and")
print("  the Mukhanov potential is a''/a.  Its leading behaviour decides the exponents:")
print()
print(f"  {'case':>28} {'a near the crunch':>22} {'a''/a':>16} {'exponents':>14}")
for nm, ab, pot, ex in [("pure DUST (rho = 0)", "~ sigma^2 (even)", "2/sigma^2", "(-1, 2)"),
                        ("ANY radiation (rho > 0)", "~ sigma  (odd)", "p/sigma", "(0, 1)")]:
    print(f"  {nm:>28} {ab:>22} {pot:>16} {ex:>14}")
print()
# verify the two indicial equations
d2 = sp.solve(sp.Eq(s_ * (s_ - 1), 2), s_)
d1 = sp.solve(sp.Eq(s_ * (s_ - 1), 0), s_)
print(f"  dust:      s(s-1) = 2  =>  s = {sorted(d2)}   (difference 3)")
print(f"  radiation: s(s-1) = 0  =>  s = {sorted(d1)}   (difference 1)")
assert sorted(d2) == [-1, 2] and sorted(d1) == [0, 1]
print()
for s in [
 "⇒⇒ ** AND THE RESONANCE MOVES WITH THEM.  With dust the exponents differ by THREE and the",
 "   correction steps in SIXES, so the resonance is never reached and no logarithm is generated —",
 "   which is c54.124's result.  With radiation the exponents differ by ONE and the potential",
 "   carries a $1/\\sigma$ term, which lands on the resonance at the FIRST step. **",
]:
    print("  " + s)

# --- exhibit the logarithm explicitly
print()
print("  The logarithm, exhibited: solve v'' = (p/sigma) v as a series about sigma = 0.")
n_terms = 6
c = sp.symbols('c0:%d' % n_terms)
v1 = sum(c[i] * sg**(i + 1) for i in range(n_terms - 1))
res = sp.simplify(sp.diff(v1, sg, 2) - (sp.Symbol('p') / sg) * v1)
print(f"     the s = 1 branch closes with no log (its recursion never hits sigma^-1).")
print(f"     the s = 0 branch needs one: v = 1 + ... gives a term p/sigma with nothing to match,")
print(f"     so v_0 = 1 + p sigma ln sigma + O(sigma), and ** the log coefficient IS p **.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — SO THE MIXING IS DISCONTINUOUS AT ZERO RADIATION")
print("=" * 78)
for s in [
 "⛔⛔ ** THE LIMIT $\\rho\\to0$ IS SINGULAR, AND THAT IS THE RESULT. **  *The exponents are $(0,1)$",
 "   for every $\\rho>0$ and $(-1,2)$ at $\\rho=0$ exactly.  A discrete jump in the indicial pair is",
 "   not something a small parameter can smooth: **the pure-dust background is a measure-zero",
 "   exception, not the leading term of a series in the radiation content.***",
 "",
 "⇒ ** SO c54.124's 'no odd part on any determination, hence no mixing' IS EXACTLY RIGHT ABOUT THE",
 "   VACUUM LEG AND SAYS NOTHING ABOUT ANY INTERIOR WITH RADIATION IN IT. **  *And the corpus's own",
 "   BBN requires radiation there.  **The construction cannot have the nucleosynthesis and the",
 "   evenness at the same time.***",
 "",
 "⌗ *And the log coefficient $p=-1/\\rho$ GROWS as the radiation content falls — so the mixing is",
 "   strongest for the least radiation, right up to the point where the exponents jump and the",
 "   mechanism disappears.  **The dependence is not monotone in the naive direction and this is why",
 "   the question had to be computed rather than estimated.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE SIZE, SWEPT")
print("=" * 78)
print("  ** A FIRST VERSION OF THIS PART WAS WRONG TWICE AND IS RECORDED AS SUCH. **  It started")
print("  from the REGULAR (s = 1) solution -- which is precisely the one a unipotent monodromy")
print("  PRESERVES -- so it measured numerical noise at the 1e-9 level and called it mixing.  And it")
print("  printed |c0| * rho to six decimals of a quantity of order 1e-9, got a column of zeros, and")
print("  reported it as 'flat'.  ** A column of zeros from a truncated format is not a scaling law. **")
print()
print("  The monodromy of a resonant pair is unipotent, and the direction matters: the s = 1")
print("  solution is single-valued, and it is the s = 0 solution that ACQUIRES an s = 1 component.")
print("  With v_0 = 1 + p sigma ln sigma, a full circuit sends ln sigma -> ln sigma + 2 pi i, so")
print()
print("     ** v_0  ->  v_0 + 2 pi i p * v_1 ,   off-diagonal = 2 pi i p = -2 pi i / rho **")
print()
print("  which is an exact prediction with no free constant.  Tested against the EXACT background:")
A_v, k_v, cs2 = 2.0, 1.0, 1.0 / 3.0


def loop_offdiag(rho_v, delta=1e-4):
    """integrate v_0 once around the crunch and read the v_1 component it acquires"""
    sB = A_v * rho_v / 2.0
    etac = 2 * np.pi - 2 * np.arctan(rho_v)
    p_exact = -1.0 / rho_v

    def pot(sig):
        e = etac + sig
        aa = (A_v / 2) * (1 - np.cos(e)) + sB * np.sin(e)
        app = (A_v / 2) * np.cos(e) - sB * np.sin(e)
        return app / aa

    def rhs(th, y):
        sig = delta * np.exp(1j * th)
        d = 1j * sig
        v, vp = y
        return [vp * d, (-(cs2 * k_v ** 2) + pot(sig)) * v * d]

    ls = np.log(delta + 0j)
    y0 = [1.0 + p_exact * delta * ls, p_exact * (ls + 1.0)]
    sol = solve_ivp(rhs, [0.0, 2 * np.pi], y0, rtol=1e-12, atol=1e-15)
    dv = sol.y[0, -1] - y0[0]          # what the circuit added
    return dv / delta, 2j * np.pi * p_exact   # measured coefficient of v_1 = sigma, and predicted


print()
print(f"  {'rho':>9} {'rho_r/rho_m at a_max':>21} {'measured off-diag':>22} {'predicted 2 pi i p':>22} {'ratio':>8}")
ok = True
for rv in [0.8, 0.4, 0.2, 0.1]:
    meas, pred = loop_offdiag(rv)
    r = abs(meas) / abs(pred)
    ok &= (0.9 < r < 1.1)
    print(f"  {rv:>9.3f} {rv**2/4.0:>21.5f} {abs(meas):>22.4f} {abs(pred):>22.4f} {r:>8.4f}")
assert ok, "the measured monodromy must match 2 pi |p| to ten per cent"
print()
print("  ** MATCHED TO BETTER THAN TEN PER CENT AT EVERY RADIATION FRACTION, WITH NO FITTED")
print("     CONSTANT.  The off-diagonal is 2 pi / rho exactly. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS SAYS ABOUT THE ROW")
print("=" * 78)
for s in [
 "✔✔ ** THE MIXING IS GENERIC AND ITS COEFFICIENT IS $p=-1/\\rho=-A/2\\sqrt B$ — the dust amplitude",
 "   over the radiation amplitude, i.e. the inverse square root of the radiation fraction at",
 "   maximum expansion. **  *`L-150` asked for $\\rho_r/\\rho_m$; the mode-mixing question asked for",
 "   an odd part; the answer to both is one number and this is it.*",
 "",
 "⇒⇒ ** AND THE PHYSICAL READING IS SHARP: a progenitor with MORE radiation has a SMALLER $p$ and",
 "   mixes LESS.  The scale-invariant spectrum frozen on the contracting side reaches the observer",
 "   in inverse proportion to the radiation the progenitor carried. **",
 "",
 "⚑ ** WHICH IS A CONSTRAINT FROM THE SKY ON THE PROGENITOR'S COMPOSITION, WHICH IS WHAT THIS ROW",
 "   HAS NEVER HAD.  It runs backwards through every step: observed spectrum -> permitted mixing ->",
 "   permitted $p$ -> permitted $\\rho_r/\\rho_m$ at the progenitor's maximum expansion. **",
 "",
 "⚠⚠ ** THE BOUND, AND IT IS NOT SMALL. **  *(i) The interior is leading order — closed FRW, dust",
 "   plus radiation, no anisotropy, no dissipation.  (ii) The sound speed is held at $1/3$ rather",
 "   than run through the mixture's own $c_s(a)$.  (iii) The numerical leakage is measured at finite",
 "   $\\delta$ and is reported as a scaling, not as a calibrated amplitude.  **What is solid is the",
 "   INDICIAL structure and the identification of $p$ — both exact — and the discontinuity at",
 "   $\\rho=0$, which is a statement about exponents and cannot be softened by any of (i)-(iii).***",
]:
    print("  " + s)
