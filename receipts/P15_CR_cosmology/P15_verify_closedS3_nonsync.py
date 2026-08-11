"""
P15_verify_closedS3_nonsync.py -- verifies the P15 sec:largescale low-ell floor MECHANISM + LOCATION: the CR
  transfer is the DISCRETE closed-S^3 source (k_L=sqrt(L(L+2))/r0, L>=2, hard lowest mode L=2) projected
  through the FLAT spherical Bessel j_ell(k_L D_C) -- not the hyperspherical transfer of a literal closed
  universe (which CR's flat distance slicing does not have). C_ell = sum_{L>=2} w_L j_ell^2(k_L D_C),
  w_L=(L+1)/(L(L+2)). The stretch chi=D_C/r0=2.75 pushes L=2 to ell~7.8, starving ell<~8.
  RESULT: ell(ell+1)C_ell = 0.121/0.104/0.199/0.649/0.916/0.986/0.998 at ell=2..8, recovered by ell~8 --
  the paper's 'falls below the plateau for ell<~7, recovers by ell~8'.
  DISCRIMINATING CONTROL: the flat-limit chi->0 must give flat power -- verified (chi=0.1 -> all ~1.00).
  HONEST BOUND: ordinary SW only (no ISW), so this SW-only deficit (0.12 at ell=2) is DEEPER than the exact
  Boltzmann transfer's (0.47, verify_lowell_boltzmann); this receipt fixes the mechanism + geometric LOCATION,
  the depth is the Boltzmann receipt's. Weight convention cross-checked in verify_lowell_exact_measure.
STATUS: ✔✔ (mechanism + location; flat-limit control passes; depth deferred to Boltzmann receipt)
RUN: python3 P15_verify_closedS3_nonsync.py   RUNTIME: ~5s
ORIGIN: computations/perturbation_verify/verify_closedS3_nonsync.py, verified r1394.
"""
import numpy as np
from scipy.special import spherical_jn

r0 = 5064.0          # present S^3 areal/curvature radius [Mpc]  (sets the SOURCE quantization)
D_C = 13927.0        # flat comoving (= angular-diameter) distance to LSS [Mpc] (the PROJECTION)

def Cl_CR(ells, Lmax, chi=D_C/r0):
    """chi = D_C/r0 controls the discreteness: chi->0 = continuum (flat limit); chi~2.75 = CR."""
    out = np.zeros(len(ells))
    for L in range(2, Lmax+1):
        kL_DC = np.sqrt(L*(L+2))*chi
        w = (L+1)/(L*(L+2))
        out += w*np.array([spherical_jn(int(l), kL_DC)**2 for l in ells])
    return out

def Dl_norm(Cl, ells):
    D = ells*(ells+1)*Cl
    return D/np.mean(D[ells >= 25])

if __name__ == "__main__":
    ells = np.arange(2, 31)
    print("="*66)
    print("CR NON-SYNCHRONOUS transfer: discrete closed-S^3 source, FLAT j_ell projection")
    print("="*66)
    print("[flat-limit test] ell(ell+1)C_ell must be flat as chi=D_C/r0 -> 0:")
    for chi in (0.1, 0.5):
        D = Dl_norm(Cl_CR(ells, 4000, chi), ells)
        print(f"   chi={chi:.2f}: l2={D[0]:.3f} l5={D[3]:.3f} l10={D[8]:.3f} l20={D[18]:.3f}  (flat=1)")
    print("\n[CR RESULT] chi=D_C/r0=2.75, ell(ell+1)C_ell normalised to ell=25-30:")
    D = Dl_norm(Cl_CR(ells, 4000), ells)
    for i, l in enumerate(ells):
        if l <= 12 or l in (15, 20):
            print(f"   ell={l:2d}: {D[i]:.3f}  {'#'*int(round(D[i]*40))}")
    print("\n[READING] strong low-ell deficit below ell~7-8, recovered by ell~8 -- the eq:lowell")
    print(" floor vindicated for the right reason (flat projection of discrete closed source).")
    print(" Resolves the r521 'no suppression': that was the standard-closed (wrong) object.")
    print(" CAVEATS: ordinary SW only; weight convention to be cross-checked; P12 cold read owed.")
    print("="*66)

# =====================================================================
# ** CHECKS, added r2376+c54.154.  Print-only until now: the deficit, its recovery and the
#    chi -> 0 control were all read off printed columns by eye. **
_D = Dl_norm(Cl_CR(ells, 4000), ells)
_d = {l: _D[i] for i, l in enumerate(ells)}
_fail = []
if not all(_d[l] < 0.7 for l in (2, 3, 4) if l in _d):
    _fail.append("no deficit at ell = 2,3,4")
if not (l_rec := next((l for l in sorted(_d) if l >= 6 and _d[l] > 0.95), None)):
    _fail.append("never recovers")
elif not 7 <= l_rec <= 9:
    _fail.append(f"recovery at ell = {l_rec}, expected 7-9")
_flat = Dl_norm(Cl_CR(ells, 4000, chi=0.10), ells)
if max(abs(v - 1.0) for v in _flat[:6]) > 0.05:
    _fail.append("the chi -> 0 control is not flat, so the deficit is the machinery not the stretch")
print()
print(f"  ** CHECKS (c54.154): deficit asserted below 0.7 at ell = 2,3,4 (got "
      f"{_d.get(2, float('nan')):.3f}/{_d.get(3, float('nan')):.3f}/{_d.get(4, float('nan')):.3f}); "
      f"recovery asserted in 7 <= ell <= 9 (got {l_rec}); and the chi -> 0 control asserted flat to "
      f"5%, which is what makes the deficit the STRETCH rather than the machinery. **")
if _fail:
    print("FAILED: " + "; ".join(_fail))
    raise SystemExit(1)
print("  CHECKS PASS")
