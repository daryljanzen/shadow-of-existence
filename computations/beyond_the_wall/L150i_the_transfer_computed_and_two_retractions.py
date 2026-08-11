#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE COMPOSITION BOUND HAS NOW BEEN ARGUED FOUR TIMES AND COMPUTED ZERO.  HERE
IT IS COMPUTED — ONE INTEGRATION, AT FIXED INCOMING AMPLITUDE, NO VACUUM ANYWHERE — AND IT FORCES TWO
RETRACTIONS: c54.133's CRITERION WAS THE WRONG OBSERVABLE, AND c54.139's RETRACTION OF c54.138 WAS
ITSELF WRONG. **

The mode equation on the collapse leg is $v''+(c_s^2k^2-2/(x(x+2\\rho)))v=0$ with $x=|\\eta-\\eta_c|$.
** Rescaling $x=\\xi/(c_sk)$ leaves it depending on $u\\equiv c_sk\\rho$ ALONE. **  So the entire
family is one function, computed once:

    ** P_out(k) = c_s^2 k^5 |g(u)|^2 N_k^2 / (2 pi^2 M^2 rho^2),      u = c_s k rho **

with $N_k$ the incoming sub-horizon amplitude — quantum, classical, anything — and $g$ the survivor
coefficient $c_1-(2\\pi i/\\rho)c_0$ in rescaled units.

  PART 1  ** g(u), COMPUTED, and its three regimes **
  PART 2  ** the checks: it must reproduce c54.137's flat vacuum spectrum and the k^4 direct
          branch, and it does **
  PART 3  ** THE OBSERVABLE IS THE RUNNING.  A tilt is absorbable by the inherited spectrum; the
          curvature is not.  rho <= 6.7e-5. **
  PART 4  ** TWO RETRACTIONS, and the second is mine from one revision ago **
  PART 5  ** the corrected bracket, and the strain in the network's own variable **

Run: python3 L150i_the_transfer_computed_and_two_retractions.py      (numpy, scipy)
"""
import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])

MPC, LAM = 3.0857e22, 1.1056e-52
G, C = 6.674e-11, 2.99792458e8
HBARC, JperGeV = 1.0545718e-34 * C, 1.602176634e-10
alpha = np.sqrt(3.0 / LAM) / MPC
M_nar = alpha / (3 * np.sqrt(3))
A_NAR = 2 * M_nar
CS, K_MAX = 1.0 / np.sqrt(3.0), 909.0
ALPHA_RUN = 0.01
R0, Z_EQ = 5065.0, 3399.0

# =====================================================================
print("=" * 78)
print("PART 1 — g(u), COMPUTED")
print("=" * 78)


def g_of_u(u, n_osc=600.0):
    """survivor coefficient at fixed unit incoming amplitude; function of u = c_s k rho alone"""
    xi_f = 1e-6 * u

    def rhs(t, y):
        pot = 2.0 / (t * (t + 2.0 * u))
        return [y[1], (pot - 1.0) * y[0], y[3], (pot - 1.0) * y[2]]

    xi_i = max(n_osc, 60.0 * u)
    y0 = [np.cos(xi_i), -np.sin(xi_i), np.sin(xi_i), np.cos(xi_i)]     # v = e^{i xi}
    s = solve_ivp(rhs, [xi_i, xi_f], y0, rtol=1e-13, atol=1e-18, method='DOP853')
    v = s.y[0, -1] + 1j * s.y[2, -1]
    vp = s.y[1, -1] + 1j * s.y[3, -1]
    L = np.log(xi_f / (2 * u))
    c0 = v / (1.0 + (xi_f / u) * L)                 # the x ln x term subtracted
    c1 = c0 * (1.0 / u) * (L + 1.0) - vp
    return abs(c1 - 2j * np.pi / u * c0)            # v_0 -> v_0 + 2 pi i p v_1, p = -1/rho


US = np.geomspace(3e-3, 3e2, 46)
GS = np.array([g_of_u(u) for u in US])
LU, LG = np.log(US), np.log(GS)
SL = np.gradient(LG, LU)
print(f"  {'u':>10} {'|g(u)|':>14} {'dln|g|/dlnu':>14} {'P slope 5+2s':>14} {'regime':>22}")
for u, g, s_ in zip(US, GS, SL):
    if u < 6e-3 or 0.8 < u < 1.4 or u > 150:
        reg = ("exits in matter" if u < 0.1 else
               "the knee" if u < 5 else "sub-horizon to the crunch")
        print(f"  {u:>10.4g} {g:>14.6g} {s_:>14.4f} {5+2*s_:>14.4f} {reg:>22}")
print()
print(f"  {'regime':>26} {'|g|':>16} {'P_out at fixed N':>20}")
for nm, gg, pp in [("u << 1 (exits in matter)", "6 pi/u^2", "∝ k"),
                   ("u ~ 1 (the knee)", "--", "steepening"),
                   ("u >> 1 (never exits)", "-> const", "∝ k^5")]:
    print(f"  {nm:>26} {gg:>16} {pp:>20}")
assert abs(SL[0] + 2.0) < 0.01, SL[0]
assert abs(SL[-1]) < 0.10, SL[-1]
print()
for s in [
 "⇒ ** THE WHOLE TRANSFER IS ONE CURVE AND IT HAS ONE FEATURE — a knee at $u\\sim1$, i.e. at",
 "   $k\\sim1/(c_s\\rho)$, where the mode's horizon exit moves from the progenitor's matter era to",
 "   its radiation era.  Across it the output slope runs from $k^1$ to $k^5$ at fixed incoming",
 "   amplitude. **",
 "   ***And nothing in that statement mentions the vacuum.  $N_k$ was set to unity, not to",
 "   $1/\\sqrt{2c_sk}$.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CHECKS")
print("=" * 78)
print("  The curve must reproduce what the vacuum calculations already found, as a special case.")
print(f"\n  {'incoming N_k':>22} {'regime':>16} {'predicted P_out':>18} {'banked':>22}")
for nm, reg, pred, bank in [("vacuum, 1/sqrt(2 c_s k)", "u << 1", "k^5 * u^-4 / k = k^0",
                             "c54.137: FLAT"),
                            ("vacuum, 1/sqrt(2 c_s k)", "u >> 1", "k^5 * 1 / k = k^4",
                             "c54.132: the k^4 branch"),
                            ("any N_k", "u << 1", "k * N_k^2", "c54.137's transfer law")]:
    print(f"  {nm:>22} {reg:>16} {pred:>18} {bank:>22}")
sl_small = 5 + 2 * SL[0] - 1
sl_big = 5 + 2 * SL[-1] - 1
print(f"\n  measured on the curve: vacuum slope at u -> 0 is {sl_small:+.3f} (want 0), "
      f"at u -> inf is {sl_big:+.3f} (want 4)")
assert abs(sl_small) < 0.02 and abs(sl_big - 4) < 0.25
print("  ** both reproduced, so the curve is the same object those revisions computed — and it now")
print("     carries the general incoming amplitude they did not. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE OBSERVABLE IS THE RUNNING")
print("=" * 78)
print("  The incoming spectrum is free, so a TILT from this transfer is degenerate with the")
print("  inherited one and constrains nothing.  ** Its CURVATURE is not absorbable. **")
RUN = 2 * np.gradient(SL, LU)
u_max = np.exp(np.interp(ALPHA_RUN, RUN[:25], LU[:25]))
print(f"\n  {'u':>10} {'P log-slope':>14} {'running d^2lnP/dlnk^2':>24}")
for u, s_, r in zip(US, SL, RUN):
    if u < 0.25:
        print(f"  {u:>10.4g} {5+2*s_:>14.4f} {r:>24.5f}")
print(f"\n  ** the running reaches the observational ceiling |alpha_s| = {ALPHA_RUN} at "
      f"u = {u_max:.4g} **")
rho_max = u_max / (CS * K_MAX)
print(f"  ** so with c_s = 1/sqrt3 at the crunch and the observed range reaching interior mode "
      f"{K_MAX:.0f}: **")
print(f"\n     ***  rho  <=  {rho_max:.2e}  ,  i.e.  rho_r/rho_m|max  <=  {rho_max**2/4:.2e}  ***")
assert 1e-5 < rho_max < 3e-4

# =====================================================================
print()
print("=" * 78)
print("PART 4 — TWO RETRACTIONS")
print("=" * 78)
print(f"  {'revision':>10} {'criterion':>44} {'gave':>14} {'verdict':>12}")
for a_, b_, c_, d_ in [("c54.132", "L = l, and the crossover position", "1.5e-3", "superseded"),
                       ("c54.133", "the crossover k_x lies above the range", "1.2e-2", "** WRONG OBSERVABLE **"),
                       ("c54.138", "the knee at k = 1/rho lies above the range", "1.1e-3", "** RIGHT, mis-argued **"),
                       ("c54.139", "-- withdrew c54.138 --", "1.2e-2", "** RETRACTION WRONG **"),
                       ("this", "the running stays below alpha_s", f"{rho_max:.1e}", "computed")]:
    print(f"  {a_:>10} {b_:>44} {c_:>14} {d_:>12}")
print()
for s in [
 "⚠⚠ ** RETRACTION ONE: c54.133's CRITERION ASKED WHERE THE KNEE SITS.  The sky does not measure",
 "   where a knee sits; it measures the curvature the knee puts in the spectrum, and a knee outside",
 "   the observed range still curves inside it. **  *That is why the bound moves by 180x on the",
 "   same physics.*",
 "",
 "⚠⚠⚠ ** RETRACTION TWO, AND IT IS MINE FROM ONE REVISION AGO.  c54.138 found a break at",
 "   $k=1/\\rho$; c54.139 withdrew it on the ground that 'a flat branch is what vacuum data",
 "   manufacture'.  ** THE WORDING WAS VACUUM-SPECIFIC AND THE SUBSTANCE WAS NOT. ** *The slope",
 "   change at the knee is a property of the TRANSFER — of $g(u)$, computed above at unit incoming",
 "   amplitude — and it survives any normalisation whatever.  **c54.138's bound was right and its",
 "   justification was wrong, and I retracted the bound instead of repairing the justification.***",
 "",
 "⌗⌗ ** AND THE METHODOLOGICAL POINT IS THE ONE WORTH KEEPING: I CHECKED A CLAIM'S WORDING AGAINST",
 "   A RETIRED ASSUMPTION INSTEAD OF RECOMPUTING IT.  The recomputation is a single integration and",
 "   would have taken one turn. **  ***A retraction needs the same standard of evidence as the",
 "   claim it retracts, and this one did not have it.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE BRACKET, AND THE STRAIN")
print("=" * 78)


def T_eq_GeV(rho, gstar, A=A_NAR):
    a_eq = A * rho**2 / 4.0 * MPC
    u_ = (3 * C**2 * (A * MPC) / (8 * np.pi * G * a_eq**3)) * C**2
    return (30 * u_ * HBARC**3 / (np.pi**2 * gstar))**0.25 / JperGeV


def rho_for_Teq(target, gstar):
    lo, hi = 1e-12, 1e2
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        lo, hi = (mid, hi) if T_eq_GeV(mid, gstar) > target else (lo, mid)
    return np.sqrt(lo * hi)


print("  The BBN floor also needs a correction: c54.137 evaluated g_* at 106.75 for a threshold")
print("  that sits AT an MeV, where g_* = 10.75.")
for gs, nm in [(106.75, "c54.137, the full SM"), (10.75, "** correct at 1 MeV **")]:
    print(f"     g_* = {gs:>7.2f} :  rho floor = {rho_for_Teq(1e-3, gs):.3e}   {nm}")
rho_bbn = rho_for_Teq(1e-3, 10.75)
print(f"\n     ***  {rho_bbn:.1e}  <=  rho  <=  {rho_max:.1e}  ***   -- a window "
      f"{rho_max/rho_bbn:.0f}-fold wide")
print(f"     ***  {rho_bbn**2/4:.1e}  <=  rho_r/rho_m at maximum expansion  <=  "
      f"{rho_max**2/4:.1e}  ***")
assert rho_bbn < rho_max

a_eq_ours = R0 / Z_EQ
rho_faithful = np.sqrt(4 * a_eq_ours / A_NAR)
T_check = T_eq_GeV(rho_faithful, 3.36) * 1e9
print(f"\n  ** AND THE STRAIN, IN THE VARIABLE THE TWO UNIVERSES SHARE. **")
print(f"  If the content crosses faithfully the parent's equality is ours, which needs "
      f"rho = {rho_faithful:.4f}.")
print(f"  {'quantity':>50} {'value':>16}")
for nm, v in [("cross-check: T_eq at that rho [eV], vs 0.80 measured", T_check),
              ("the parent's T_eq at the bound [eV]", T_eq_GeV(rho_max, 3.36) * 1e9),
              ("gap in rho", rho_faithful / rho_max),
              ("gap in matter-per-photon", T_eq_GeV(rho_max, 3.36) / T_eq_GeV(rho_faithful, 3.36))]:
    print(f"  {nm:>50} {v:>16.4g}")
assert abs(T_check - 0.80) < 0.06
print()
for s in [
 "✔ ** THE CROSS-CHECK IS WHAT MAKES THE COMPARISON LEGITIMATE: feeding the corpus's own $A=2M$ and",
 "   our own $r_0/(1+z_{\\rm eq})$ into the PARENT's formula returns $T_{\\rm eq}=0.80$ eV against a",
 "   measured $0.80$.  The two universes' variables are commensurable, so the gap below is physics",
 "   and not units. **",
 "",
 "⚠⚠⚠ ** THE GAP IS $\\sim800$ IN $\\rho$ AND $\\sim2\\times10^4$ IN MATTER-PER-PHOTON, AND IT CANNOT GO",
 "   INTO THE BARYONS: primordial deuterium pins $\\eta$ to about a per cent and P16's own network",
 "   runs at the measured value. **  *So either the branch point is not content-preserving in the",
 "   non-baryonic sector, or the observed spectrum's smoothness is not the constraint it looks like.",
 "   **That is front #1, stated in numbers for the first time.***",
 "",
 "⌗ *The bound goes to P16 as a result.  The strain stays in the register: what is established is a",
 "   gap, not its resolution.*",
]:
    print("  " + s)
