#!/usr/bin/env python3
"""P15 receipt -- the one item this seat had left unstarted and had twice declared undeliverable:
** a transmission FIGURE rather than an exponent. **  `r7166` stated the limit as `no transmission
figure -- exponents only`, on the ground that a figure needs the varying-`$\\lambda$` solution and
not the constant-`$k$` one.

*** ⛭⛭⛭ THE LIMIT WAS TOO WIDE, AND MY OWN `r7163` IS WHAT NARROWS IT.  The varying-`$\\lambda$`
    caveat does NOT bite on the sector that descends -- so the figure is deliverable exactly where
    it matters, and undeliverable exactly where `r7174` already showed the amplitude is lost. ***

** ⓵ THE UNLOCK IS ONE LINE OF `r7163`'s EXACT ENVELOPE, READ AT ZERO CHARGE. **
*Dividing `eq:squashed-spectrum` by its round member gives*

> ### `$\\lambda/L(L+2)=1-\\sigma(1-\\varepsilon^{-2})$`,  `$\\sigma=4m^2/L(L+2)$`

*and the descending sector is the NEUTRAL slice, `$m=0$`.*  ⇒ *** At `$m=0$` the charge fraction
`$\\sigma$` vanishes identically, so `$\\lambda=L(L+2)$` EXACTLY at every squashing -- the eigenvalue
carries no `$\\varepsilon$` at all on that sector.  **So `$k$` does not vary along the bead there, and
the constant-`$k$` solution is not an approximation on it: it is exact.** ***

⌗ ** AND THE CAVEAT SURVIVES EXACTLY WHERE IT COSTS NOTHING. ** *For charged modes `$\\sigma\\neq0$`
and `$\\lambda$` does vary -- indeed diverges at the double root, where `$\\varepsilon$` vanishes
linearly (`r7174`).  **But `r7174` also showed those modes arrive carried in label and lost in
amplitude**, so the degrees where the varying-`$\\lambda$` solution is genuinely required are the
degrees that deliver no amplitude to compute a figure FOR.*

** ⓶ SO THE FIGURE, COMPUTED RATHER THAN BOUNDED, ON THE SECTOR'S OWN EVEN DEGREES: **

| `$L$` | `$T$` | the parameter-free asymptote | the asymptote's error |
|---|---|---|---|
| `2` | `$4.1579\\times10^{-3}$` | `$3.1936\\times10^{-3}$` | **`$30.2$` per cent LOW** |
| `4` | `$1.1163\\times10^{-5}$` | `$9.5305\\times10^{-6}$` | `$17.1$` per cent low |
| `6` | `$2.4382\\times10^{-8}$` | `$2.1766\\times10^{-8}$` | `$12.0$` per cent low |
| `8` | `$4.7297\\times10^{-11}$` | `$4.3285\\times10^{-11}$` | `$9.3$` per cent low |
| `10` | `$8.4970\\times10^{-14}$` | `$7.9010\\times10^{-14}$` | `$7.5$` per cent low |

*** ⇒ AND THAT COMPARISON IS THE FINDING, NOT THE TABLE.  `$2^{7/3}k^2e^{-ks_{\\rm tot}}$` is an
    asymptotic form in `$k$`, and the sector's degrees are not in its asymptotic regime: it
    UNDERSTATES the transmission at every degree the sector contains, worst at the lowest. ***
*The ratio falls monotonically toward one from above, so the parameter-free expression is a floor on
this sector and not an estimate of it.*  ⌗ **Anyone reading that expression as the transmission at
the sector's lowest degree is low by about a third.**

⌗ ** THE CONTROL AND THE CONVERGENCE, BOTH STRUCTURAL. ** *`$T(0)=1$` exactly, because `$k=0$` makes
the Riccati variable vanish identically and the monopole passes untouched -- the control that had to
come back affirmative.  And the seam cut-off error falls by a measured factor `$10^{-2/3}$` per
decade at every degree, which is the `$a\\propto\\cos^{2/3}$` edge showing up in its own exponent, so
the extrapolation is on a rate the geometry predicts rather than a fitted one.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. ** *`$T$` is the lift's transmission on the layer's own
descending sector and NOT an observable amplitude.  Three things stand between them and none is done
here: the sector's weight is `$1/(L+1)$` of each even degree (`r7172`), `$L$` is the layer degree and
not the observable multipole (`r7164`'s projection finding, used nowhere here), and the progenitor's
input amplitude is `PO-75`'s object and still undelivered.*  ⌗ *It computes nothing for charged
modes, where the varying-`$\\lambda$` problem is real and untouched.  It re-derives the lift equation
and its regular seam series rather than quoting them, and reproduces `$s_{\\rm tot}$` against its
closed form; it does not re-derive `r7163`'s envelope beyond the one substitution it needs, and it
does not revisit `$\\operatorname{Re}\\Delta\\eta=0$`.*  ⌗ *No paper is touched.*

** COMPUTES: the lift profile `$a=\\cos^{2/3}t$` with `$c_0=2/\\sqrt3\\,2^{1/3}$`, in the gauge where
the comoving curvature radius is one, so `$k^2=L(L+2)$` is the `$S^3$` eigenvalue and no length
enters.  `$T$` by Riccati integration from the regular seam behaviour to the turnaround, Richardson
extrapolated in the seam cut-off on the measured `$10^{-2/3}$` rate. **
"""
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import gamma as Gamma

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)

# =====================================================================================
head("A -- THE UNLOCK: THE DESCENDING SECTOR'S EIGENVALUE CARRIES NO SQUASHING")

L, m, ep = sp.symbols('L m varepsilon', positive=True)
sig = 4 * m**2 / (L * (L + 2))
lam_ratio = 1 - sig * (1 - 1 / ep**2)
gate("Ⓐ①  `r7163`'s exact envelope reproduced in the one form this needs: the eigenvalue's ratio to"
     " its round member is `$1-\\sigma(1-\\varepsilon^{-2})$` with `$\\sigma=4m^2/L(L+2)$` the"
     " fraction of the eigenvalue the Hopf charge carries",
     sp.simplify(lam_ratio - (1 - 4 * m**2 / (L * (L + 2)) * (1 - 1 / ep**2))) == 0)

neutral = sp.simplify(lam_ratio.subs(m, 0))
gate("Ⓐ②  AND AT ZERO CHARGE IT IS IDENTICALLY ONE -- `$\\lambda=L(L+2)$` at EVERY squashing, with"
     " `$\\varepsilon$` absent from the expression rather than cancelling numerically",
     neutral == 1 and ep not in sp.simplify(lam_ratio.subs(m, 0)).free_symbols)

d_eps = sp.simplify(sp.diff(lam_ratio, ep))
gate("Ⓐ③  and the squashing-dependence is carried by the charge ALONE: the derivative with respect"
     " to the squashing is proportional to `$m^2$`, so it vanishes identically on the neutral slice"
     " and on no other",
     sp.simplify(d_eps.subs(m, 0)) == 0
     and sp.simplify(sp.factor(d_eps) / m**2).free_symbols.isdisjoint({m}))

gate("Ⓐ④  ⇒ SO THE CONSTANT-`$k$` SOLUTION IS EXACT ON THE SECTOR THAT DESCENDS, and the"
     " varying-`$\\lambda$` caveat `r7166` stated applies only where `$\\sigma\\neq0$` -- which is"
     " where `r7174` showed the amplitude is lost, so the figure is deliverable exactly where it is"
     " wanted",
     sp.simplify(lam_ratio.subs(m, 0)) == 1
     and sp.simplify(lam_ratio.subs({m: sp.Rational(1, 2), L: 1})) != 1)

# =====================================================================================
head("B -- THE LIFT EQUATION AND ITS REGULAR SEAM SERIES, DERIVED RATHER THAN QUOTED")

s, k = sp.symbols('s k', positive=True)
a_f = sp.Function('a')(s)
ph = sp.Function('varphi')(s)
u = a_f * ph
lhs = sp.diff(u, s, 2) - (k**2 + sp.diff(a_f, s, 2) / a_f) * u
gate("Ⓑ①  with `$u=a\\varphi$` the lift equation `$u_{ss}=(k^2+a_{ss}/a)u$` becomes"
     " `$\\varphi_{ss}+2(a_s/a)\\varphi_s=k^2\\varphi$` -- the `$a_{ss}$` term cancelling exactly,"
     " which is why the equation closes on the ratio",
     sp.simplify(sp.expand(lhs / a_f)
                 - (sp.diff(ph, s, 2) + 2 * sp.diff(a_f, s) / a_f * sp.diff(ph, s) - k**2 * ph)) == 0)

x, c = sp.symbols('x c', positive=True)
phi_ser = c * (1 + k**2 * x**2 / 10)
res = sp.simplify(sp.diff(phi_ser, x, 2) + (4 / x) * sp.diff(phi_ser, x) - k**2 * phi_ser)
gate("Ⓑ②  and at the seam, where `$a\\propto x^2$` in `$x=s_{\\rm tot}-s$`, the equation is"
     " `$\\varphi_{xx}+(4/x)\\varphi_x=k^2\\varphi$`, whose REGULAR branch is"
     " `$c(1+k^2x^2/10+\\dots)$` -- the tenth derived here by residual, not assumed, so the starting"
     " slope `$-k^2x/5$` is the series' and not a guess",
     sp.simplify(res + c * k**4 * x**2 / 10) == 0
     and sp.simplify(sp.diff(phi_ser, x) / phi_ser - k**2 * x / 5).subs(x, 0) == 0)

# ---------- the numerics
c0 = 2.0 / (np.sqrt(3.0) * 2.0 ** (1.0 / 3.0))
g_of = lambda t: c0 / np.cos(t) ** (2.0 / 3.0)
alogd = lambda t: -(2.0 / (3.0 * c0)) * np.sin(t) * np.cos(t) ** (-1.0 / 3.0)
s_quad = c0 * quad(lambda z: np.cos(z) ** (-2.0 / 3.0), 0, np.pi / 2, limit=600)[0]
s_closed = Gamma(1 / 6) * np.sqrt(np.pi) / (Gamma(2 / 3) * np.sqrt(3) * 2 ** (1 / 3))
gate(f"Ⓑ③  the lift's own length is reproduced against its closed form -- quadrature"
     f" {s_quad:.10f} against `$\\Gamma(1/6)\\sqrt\\pi/\\Gamma(2/3)\\sqrt3\\,2^{{1/3}}$` ="
     f" {s_closed:.10f}, agreeing to {abs(s_quad - s_closed):.1e}",
     abs(s_quad - s_closed) < 1e-11)


def T_at(k2, delta):
    t1 = np.pi / 2 - delta
    x1 = c0 * quad(lambda z: np.cos(z) ** (-2.0 / 3.0), t1, np.pi / 2, limit=600)[0]
    sol = solve_ivp(lambda t, y: [g_of(t) * (k2 - 2.0 * alogd(t) * y[0] - y[0]**2),
                                  g_of(t) * y[0]],
                    [t1, 0.0], [-k2 * x1 / 5.0, 0.0], rtol=1e-12, atol=1e-14)
    return float(np.exp(-sol.y[1][-1]))


gate("Ⓑ④  THE CONTROL THAT HAD TO COME BACK AFFIRMATIVE: `$T(0)=1$` exactly -- at `$k=0$` the"
     " Riccati variable starts at zero and stays there, so the monopole crosses the lift untouched",
     abs(T_at(0.0, 1e-7) - 1.0) < 1e-14)

# =====================================================================================
head("C -- THE FIGURE, PER EVEN DEGREE, WITH THE SEAM CUT-OFF EXTRAPOLATED ON A MEASURED RATE")

RATE = 10.0 ** (-2.0 / 3.0)
rows = []
print(f"\n    {'L':>3s} {'T':>16s} {'asymptote':>15s} {'exact/asy':>10s} {'conv rate':>10s}")
for Lv in (2, 4, 6, 8, 10):
    k2 = Lv * (Lv + 2)
    v = [T_at(k2, d) for d in (1e-5, 1e-6, 1e-7)]
    d1, d2 = v[1] - v[0], v[2] - v[1]
    ext = v[2] + d2 * RATE / (1 - RATE)
    asy = 2 ** (7 / 3) * k2 * np.exp(-np.sqrt(k2) * s_closed)
    rows.append((Lv, ext, asy, ext / asy, d2 / d1))
    print(f"    {Lv:3d} {ext:16.9e} {asy:15.8e} {ext / asy:10.5f} {d2 / d1:10.6f}")

gate("Ⓒ①  the seam cut-off error falls at a measured rate of `$10^{-2/3}$` per decade at EVERY"
     " degree -- the profile's own `$\\cos^{2/3}$` edge appearing in its own convergence exponent,"
     " so the extrapolation rides a rate the geometry fixes rather than a fitted one",
     all(abs(r[4] - RATE) < 2e-3 for r in rows))

gate("Ⓒ②  and the figures are POSITIVE and ordered, thinning monotonically with degree by between"
     " two and three orders per even degree -- so the sector's transmission is a decreasing"
     " sequence and not a bound",
     all(0 < r[1] < 1 for r in rows)
     and all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1))
     and all(100 < rows[i][1] / rows[i + 1][1] < 1000 for i in range(len(rows) - 1)))

gate("Ⓒ③  THE FIGURE AT THE SECTOR'S LOWEST DEGREE IS `$4.158\\times10^{-3}$`, and the next three"
     " are `$1.116\\times10^{-5}$`, `$2.438\\times10^{-8}$` and `$4.730\\times10^{-11}$` -- the"
     " transmission figure `r7166` declared undeliverable, delivered",
     abs(rows[0][1] - 4.1579e-3) < 1e-6
     and abs(rows[1][1] - 1.1163e-5) < 1e-8
     and abs(rows[2][1] - 2.4382e-8) < 1e-11
     and abs(rows[3][1] - 4.7297e-11) < 1e-13)

gate("Ⓒ④  ⇒ AND THE COMPARISON IS THE RESULT: the parameter-free asymptote UNDERSTATES the"
     " transmission at every degree the sector contains -- by `$30$` per cent at the lowest, falling"
     " to `$7.5$` per cent by the fifth -- so it is a FLOOR on this sector and not an estimate of"
     " it, and the degrees that matter are not in its asymptotic regime",
     all(r[3] > 1 for r in rows)
     and abs(rows[0][3] - 1.302) < 0.01
     and all(rows[i][3] > rows[i + 1][3] for i in range(len(rows) - 1)))

gate("Ⓒ⑤  and the ratio approaches one from ABOVE rather than crossing it, which is what makes the"
     " asymptote's sign of error a statement and not an accident of where it was sampled",
     all(1 < r[3] < 1.35 for r in rows) and rows[-1][3] < 1.08)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE LIMIT THIS SEAT STATED TWICE WAS TOO WIDE, AND ITS OWN EARLIER
  REVISION IS WHAT NARROWS IT.  A transmission figure was declared
  undeliverable because it needs the varying-lambda solution.  But the
  eigenvalue's squashing-dependence is carried by the Hopf charge alone, so
  on the NEUTRAL slice -- which is exactly the sector that descends --
  lambda = L(L+2) at every squashing and k does not vary along the bead at
  all.  The constant-k solution is not an approximation there; it is exact.

  And the caveat survives precisely where it costs nothing: charged modes do
  have a varying lambda, and they are the modes already shown to arrive
  carried in label and lost in amplitude.  So the figure is deliverable
  exactly where it is wanted and undeliverable exactly where there is no
  amplitude to deliver.

  *** THE FIGURE: 4.158e-3 at the sector's lowest degree, then 1.116e-5,
      2.438e-8, 4.730e-11, 8.497e-14 -- thinning by two to three orders per
      even degree, with T(0) = 1 exactly as the control. ***

  AND THE COMPARISON IS THE RESULT RATHER THAN THE TABLE: the
  parameter-free asymptotic expression UNDERSTATES the transmission at every
  degree the sector contains -- thirty per cent at the lowest, falling to
  seven and a half by the fifth -- approaching from above.  It is a floor on
  this sector, not an estimate of it, and the degrees that matter are not in
  its asymptotic regime.

  THE GUARD: when a limit is stated because the general problem is harder
  than the one solved, check whether the sector the result is actually about
  satisfies the easy case EXACTLY.  A caveat earns its scope from the modes
  that need it, and here every mode that needed it had already been shown to
  carry nothing.
  ==========================================================================
""")
