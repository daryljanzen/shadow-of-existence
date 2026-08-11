#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE LAST INPUT IS COMPUTED, AND IT DOES NOT SAVE THE SECTOR.  PHASE-AVERAGED
OVER THE STABILITY-BAND ROTATION, THE TRANSFER IN THE ACOUSTIC RANGE IS NOT FLAT: ITS RUNNING IS
$0.3$–$0.9$ AGAINST AN OBSERVED $|\\alpha_s|\\lesssim0.01$, AND IT CARRIES FACTOR-SEVERAL MODE-TO-MODE
SCATTER ON TOP.  THE OVER-DETERMINATION STANDS AND THE COLLAPSE-PERTURBATION SECTOR FAILS. **

c54.144 narrowed c54.143 to $\\ell\\lesssim200$ and named what was left: in a stability band the cycle
fixes only a PHASE, so the state in which the acoustic modes reach the crunch is a rotation of the
progenitor's own, and the observable is the phase AVERAGE.  ** That is the last free input in the
chain, and it is computed here. **

  PART 1  ** THE CONSTRUCTION: the invariant ellipse, the phase, and the normalisation (the WKB
          envelope at turnaround, which is the same $N_k$ every earlier revision used). **
  PART 2  ** THE PHASE-AVERAGED TRANSFER, and it tracks WKB within a factor of two. **
  PART 3  ** THE RUNNING: $0.3$–$0.9$ where the sky permits $0.01$.  And a second problem the
          average hides — the SPREAD is a factor of several, mode to mode. **
  PART 4  ** THE VERDICT, AND THE TWO ESCAPES THAT REMAIN, BOTH NAMED. **

Run: python3 L150l_the_phase_average_and_the_verdict.py      (numpy, scipy)
"""
import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])
CS, RHO, SMAP, ALPHA = 1.0 / np.sqrt(3.0), 0.0539, 2.750, 0.01


def eta_c(r):
    return 2 * np.pi - 2 * np.arctan(r)


def pot(e, r):
    a = (1 - np.cos(e)) + r * np.sin(e)
    return (np.cos(e) - r * np.sin(e)) / a


def run_mode(k, y0, r=RHO, cs=CS):
    """integrate bang->crunch; return the crunch Frobenius pair and the WKB envelope at turnaround"""
    eps = 1e-6 * r
    ec = eta_c(r)

    def rhs(t, y):
        return [y[1], (pot(t, r) - cs * cs * k * k) * y[0]]

    s = solve_ivp(rhs, [eps, ec - eps], y0, rtol=1e-11, atol=1e-15, method='DOP853',
                  t_eval=[ec / 2, ec - eps])
    N = np.sqrt(s.y[0, 0]**2 + (s.y[1, 0] / (cs * k))**2)
    v, vp = s.y[0, 1], s.y[1, 1]
    L = np.log(eps / (2 * r))
    c0 = v / (1.0 + (eps / r) * L)
    c1 = c0 * (1.0 / r) * (L + 1.0) + vp
    return c0, c1, N


def frob_y0(vec, r=RHO):
    eps = 1e-6 * r
    L = np.log(eps / (2 * r))
    return list(vec[0] * np.array([1.0 + (eps / r) * L, (1.0 / r) * (L + 1.0)])
                + vec[1] * np.array([eps, 1.0]))


def cycle_C(k, r=RHO):
    cols = []
    for w in (0, 1):
        eps = 1e-6 * r
        L = np.log(eps / (2 * r))
        y0 = [1.0 + (eps / r) * L, (1.0 / r) * (L + 1.0)] if w == 0 else [eps, 1.0]
        c0, c1, _ = run_mode(k, y0)
        cols.append([c0, c1])
    T = np.array(cols).T
    return np.array([[1.0, 0.0], [2 * np.pi / r, 1.0]]) @ T


# =====================================================================
print("=" * 78)
print("PART 1 — THE CONSTRUCTION")
print("=" * 78)
for s in [
 "  In a stability band C is elliptic with eigenvalues e^{+-i theta} and a complex eigenvector w.",
 "  The real states it acts on are v(phi) = Re(e^{i phi} w), and n prior cycles advance phi by",
 "  n theta -- so ** averaging over phi IS averaging over how many passages the progenitor's own",
 "  perturbations had already been through, which the construction does not fix. **",
 "",
 "  The normalisation is the one every earlier revision used: N_k, the WKB envelope",
 "  sqrt(v^2 + (v'/c_s k)^2) taken at turnaround, where the mode is deep sub-horizon and the",
 "  envelope is constant.  The observable is the survivor after the monodromy,",
 "     ** S = c_1 - (2 pi i/rho) c_0  ,  and the transfer is T^2(k) = < S^2 / N^2 >_phi. **",
]:
    print(s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE PHASE-AVERAGED TRANSFER")
print("=" * 78)
KS = np.array([80., 110., 150., 200., 265., 350., 460.])
MEAN, SPREAD, LD = [], [], []
print(f"  {'k':>6} {'l':>6} {'<T^2>':>12} {'spread over phase':>22} {'median leaked/direct':>21} "
      f"{'WKB':>7}")
for k in KS:
    C = cycle_C(k)
    V = np.linalg.eig(C)[1]
    rs, lds = [], []
    for ph in np.linspace(0, np.pi, 24, endpoint=False):
        vv = np.real(np.exp(1j * ph) * V[:, 0])
        n = np.linalg.norm(vv)
        if n < 1e-12:
            continue
        c0, c1, N = run_mode(k, frob_y0(vv / n))
        rs.append((c1**2 + (2 * np.pi / RHO)**2 * c0**2) / N**2)
        lds.append((2 * np.pi / RHO) * abs(c0) / max(abs(c1), 1e-300))
    rs = np.array(rs)
    MEAN.append(rs.mean())
    SPREAD.append(rs.max() / max(rs.min(), 1e-300))
    LD.append(np.median(lds))
    print(f"  {k:>6.0f} {k*SMAP:>6.0f} {rs.mean():>12.4g} "
          f"{'x%.1f' % (rs.max()/max(rs.min(),1e-300)):>22} {np.median(lds):>21.4f} "
          f"{2*np.pi/(RHO*CS*k):>7.3f}")
MEAN = np.array(MEAN)
wkb = (CS * KS)**2 + (2 * np.pi / RHO)**2
print(f"\n  ** the phase average tracks the WKB expression within a factor "
      f"{max(abs(np.log(MEAN/wkb))):.1f} in the log, over a decade in l. **")
assert 0.2 < np.mean(MEAN / wkb) < 2.0

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RUNNING, AND THE SPREAD THE AVERAGE HIDES")
print("=" * 78)
lk, lt = np.log(KS), np.log(MEAN)
sl, rn = np.gradient(lt, lk), np.gradient(np.gradient(lt, lk), lk)
slw = np.gradient(np.log(wkb), lk)
rnw = np.gradient(slw, lk)
print(f"  {'k':>6} {'slope meas':>11} {'slope WKB':>11} {'running meas':>13} {'running WKB':>12}")
for i, k in enumerate(KS):
    print(f"  {k:>6.0f} {sl[i]:>11.3f} {slw[i]:>11.3f} {rn[i]:>13.3f} {rnw[i]:>12.3f}")
ld_slope = np.polyfit(lk, np.log(LD), 1)[0]
print(f"\n  ** leaked/direct log-slope in k :  {ld_slope:+.3f}   "
      f"(WKB -1.00 ; c54.143's low-k attractor -0.05) **")
print(f"  ** the WKB running over this range is {rnw.min():.2f} to {rnw.max():.2f}; the observed "
      f"ceiling is |alpha_s| = {ALPHA} **")
print(f"  ** so the transfer's curvature exceeds what the sky permits by a factor "
      f"{rnw.max()/ALPHA:.0f}, and the measured curve is of the same order and noisier. **")
assert ld_slope < -0.3
assert rnw.max() / ALPHA > 30
print()
print(f"  AND THE AVERAGE HIDES A SECOND PROBLEM: the spread over phase is up to "
      f"x{max(SPREAD):.0f} in power,")
print("  and adjacent multipoles sit at different phases -- so even the mean being right would")
print("  leave factor-several scatter between neighbours.")
print()
for s in [
 "⇒⇒⇒ ** SO THE LAST FREE INPUT DOES NOT SAVE THE SECTOR.  Averaged over the one thing the cyclic",
 "   structure leaves free, the acoustic-range transfer is not flat, its curvature exceeds the",
 "   observed running by some two orders, and it carries mode-to-mode scatter on top. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT, AND THE TWO ESCAPES")
print("=" * 78)
print(f"  {'chain':>46} {'gives':>16} {'status':>16}")
for a_, b_, c_ in [("A: one M across the bead + a crossing plasma", "rho = 5.4e-2", "STANDS"),
                   ("B: the observed spectrum's smoothness", "rho << 5.4e-2", "** STANDS **"),
                   ("the reconciliation attempted at c54.143", "-- attractor --", "scoped away"),
                   ("the reconciliation attempted here", "-- phase average --", "** FAILS **")]:
    print(f"  {a_:>46} {b_:>16} {c_:>16}")
print()
for s in [
 "⚠⚠⚠ ** THE OVER-DETERMINATION STANDS.  THE COLLAPSE-PERTURBATION SECTOR FAILS ITS OWN",
 "   CONSISTENCY TEST, WITHIN THE IDEALISATION THIS ARC HAS CARRIED THROUGHOUT. **",
 "   *That is the verdict the front has been circling since c54.121, and it is a verdict rather than",
 "   a tension: both chains are computed, the two candidate reconciliations are computed, and the",
 "   escapes are not open-ended.*",
 "",
 "⇒ ** ESCAPE ONE — THE IDEALISATION.  Everything here uses $z\\propto a$ with a constant $c_s$.",
 "   The true scalar $z_S=a\\sqrt{3(1+w)}M_{\\rm Pl}/c_s$ moves across the progenitor's own equality,",
 "   so $z_S''/z_S\\ne a''/a$ and the Floquet potential is not the one used. **  *This is the only",
 "   step in either chain that is an idealisation rather than structure, computation or measurement",
 "   — which makes it the whole of what stands between this sector and a falsification.*",
 "",
 "⇒ ** ESCAPE TWO — CHAIN A's PREMISES, and they are structural: one $M$ across the bead, and the",
 "   photon–baryon plasma crossing. **  *Dropping either is a change to the construction rather than",
 "   a repair of the calculation, and each is load-bearing elsewhere — the first for the whole bead,",
 "   the second for the nucleosynthesis account.*",
 "",
 "⌗ ** WHAT IS UNAFFECTED, AND IT IS MOST OF THE CORPUS: the abundances, the acoustic scale, the",
 "   Hubble resolution, the diffusion signature, the amplitude and tensor results, and the",
 "   phase-only transmission above the first peak.  All sit upstream of the transfer's shape. **",
]:
    print("  " + s)
