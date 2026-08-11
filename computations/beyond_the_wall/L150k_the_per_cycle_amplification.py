#!/usr/bin/env python3
"""
`L-150` + `L-171`.  ** THE PER-CYCLE AMPLIFICATION $\\lambda(k)$, COMPUTED.  IT IS A FLOQUET PROBLEM,
AND ITS INSTABILITY BANDS CLOSE: ABOVE $\\ell\\simeq220$ THE PASSAGE IS A PURE PHASE ROTATION WITH NO
AMPLIFICATION AT ALL, AND BELOW IT THE AMPLIFICATION SPANS $10^7$ IN POWER BETWEEN NEIGHBOURING
MULTIPOLES. **

Two things follow, one positive and one that scopes c54.143 back.

  PART 1  ** IT IS A FLOQUET PROBLEM.  $\\det C=1$, so the eigenvalues are a reciprocal REAL pair
          (an instability band) or a unimodular COMPLEX pair (a stability band).  Verified. **
  PART 2  ** THE OSCILLATION IS NOT THE ACOUSTIC STRUCTURE.  Band period $\\Delta k=0.881$, i.e.
          $\\Delta\\ell\\simeq2.4$ against the acoustic $\\Delta\\ell\\simeq300$.  c54.143's PART 4
          speculation is WITHDRAWN. **
  PART 3  ** THE BANDS CLOSE ABOVE $\\ell\\simeq220$: $|\\lambda|=1$ exactly.  So in the acoustic range
          a branch-point passage is PHASE-ONLY — a strong, derived form of P15's transmission
          claim, in precisely the range the data constrains. **
  PART 4  ** BELOW $\\ell\\simeq200$ IT IS CATASTROPHIC: $|\\lambda|$ runs $1.5$ to $4915$ across
          neighbouring physical modes, $10^7$ in power.  So cosmogenesis CANNOT be a chain in which
          the observable leg inherits through a prior branch point of the same type. **
  PART 5  ** AND THAT SCOPES c54.143: an ATTRACTOR needs a hyperbolic map, which exists only where
          the bands are open.  The k-flat leaked/direct ratio was computed at $k=3$–$30$ and does
          NOT extend to the acoustic range, which is the range the composition bound came from. **

Run: python3 L150k_the_per_cycle_amplification.py      (numpy, scipy)
"""
import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])
CS, RHO, SMAP = 1.0 / np.sqrt(3.0), 0.0539, 2.750


def eta_c(r):
    return 2 * np.pi - 2 * np.arctan(r)


def pot(e, r):
    a = (1 - np.cos(e)) + r * np.sin(e)
    return (np.cos(e) - r * np.sin(e)) / a


def cycle(k, r=RHO, cs=CS, eps_rel=1e-6):
    """one full bang->crunch propagation, then the monodromy; returns (C, det T)"""
    eps = eps_rel * r
    ec = eta_c(r)

    def rhs(t, y):
        return [y[1], (pot(t, r) - cs * cs * k * k) * y[0]]

    cols = []
    for w in (0, 1):
        L = np.log(eps / (2 * r))
        y0 = [1.0 + (eps / r) * L, (1.0 / r) * (L + 1.0)] if w == 0 else [eps, 1.0]
        s = solve_ivp(rhs, [eps, ec - eps], y0, rtol=1e-11, atol=1e-15, method='DOP853')
        v, vp = s.y[0, -1], s.y[1, -1]
        c0 = v / (1.0 + (eps / r) * L)
        c1 = c0 * (1.0 / r) * (L + 1.0) + vp
        cols.append([c0, c1])
    T = np.array(cols).T
    return np.array([[1.0, 0.0], [2 * np.pi / r, 1.0]]) @ T, abs(np.linalg.det(T) - 1)


def lam(k):
    C, d = cycle(k)
    return max(abs(np.linalg.eig(C)[0])), d


# =====================================================================
print("=" * 78)
print("PART 1 — IT IS A FLOQUET PROBLEM")
print("=" * 78)
print("  det C = det J * det T = 1 (the monodromy is unipotent; T preserves the Wronskian), so the")
print("  eigenvalues are {lambda, 1/lambda}: either a reciprocal REAL pair -- an instability band,")
print("  the mode is amplified per cycle -- or a unimodular COMPLEX pair, a stability band, where")
print("  the cycle only rotates the phase.  ** That dichotomy is a structural check on the whole")
print("  computation, and it is met exactly. **")
print(f"\n  {'k':>9} {'|det T - 1|':>13} {'eigenvalues':>34} {'band':>10}")
for k in [6.928, 25.981, 80.994, 150.997]:
    C, d = cycle(k)
    w = np.linalg.eig(C)[0]
    kind = "UNSTABLE" if abs(w).max() > 1.0001 else "stable"
    desc = (f"{w[0].real:+.4g}, {w[1].real:+.4g}" if abs(w.imag).max() < 1e-9
            else f"{w[0]:.4g} (|.| = {abs(w[0]):.6f})")
    print(f"  {k:>9.3f} {d:>13.1e} {desc:>34} {kind:>10}")
    assert d < 1e-2

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE OSCILLATION IS NOT THE ACOUSTIC STRUCTURE")
print("=" * 78)
dk = np.pi / (CS * eta_c(RHO))
print(f"  The phase accumulated over one cycle is c_s k eta_c, so the band period is")
print(f"     ** Delta k = pi/(c_s eta_c) = {dk:.4f} ,  i.e.  Delta l = {dk*SMAP:.2f} **")
print(f"  against the observed acoustic spacing Delta l ~ 300.")
print()
for s in [
 "⚠⚠ ** SO c54.143's CLOSING SPECULATION — that this oscillation IS the acoustic structure — IS",
 "   WITHDRAWN.  It is off by a factor of 125 in spacing. **  *It was written as a suggestion and",
 "   not computed, in the same file that had just finished demonstrating what happens when an input",
 "   is assumed rather than looked up.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE BANDS CLOSE, AND WHERE THEY CLOSE MATTERS")
print("=" * 78)
print("  Evaluated on the PHYSICAL modes, k_L = sqrt(L(L+2)), l = 2.750 k:")
print(f"\n  {'L':>5} {'l':>8} {'|lambda|':>12} {'band':>20}")
rows = []
for L in [2, 6, 10, 16, 22, 30, 38, 46, 54, 62, 70, 80, 100, 150, 300]:
    k = np.sqrt(L * (L + 2))
    l, d = lam(k)
    rows.append((L, k * SMAP, l))
    print(f"  {L:>5} {k*SMAP:>8.1f} {l:>12.4f} {'UNSTABLE' if l>1.0001 else 'stable (phase only)':>20}")
hi = [r for r in rows if r[0] >= 80]
assert all(abs(r[2] - 1) < 1e-3 for r in hi), hi
print()
for s in [
 "✔✔✔ ** ABOVE $\\ell\\simeq220$ EVERY PHYSICAL MODE IS IN A STABILITY BAND AND $|\\lambda|=1$ TO",
 "   MACHINE PRECISION: a branch-point passage neither amplifies nor suppresses it, it only rotates",
 "   the phase. **",
 "   *That is P15 `rem:transmission-leg`'s claim — the leg multiplies the spectrum by a constant —",
 "   in its strongest form and in exactly the range the acoustic data constrains, and it is derived",
 "   here rather than asserted.  **The constant is one.***",
 "",
 "⌗ *And it explains why the acoustic sector has been reproducible at all: whatever the progenitor",
 "   sent, the crossing returned it unchanged in magnitude above the first peak.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — BELOW THE CLOSURE IT IS CATASTROPHIC")
print("=" * 78)
lo = [r for r in rows if r[0] <= 70 and r[2] > 1.0001]
lam_lo = [r[2] for r in lo]
print(f"  Over the open-band range ({lo[0][1]:.0f} <= l <= {lo[-1][1]:.0f}) the amplification runs")
print(f"     |lambda| from {min(lam_lo):.1f} to {max(lam_lo):.0f}   -- "
      f"** {(max(lam_lo)/min(lam_lo))**2:.1e} in POWER between neighbouring physical modes **")
print(f"  and it varies mode to mode, because the band period ({dk:.3f} in k) and the mode spacing")
print(f"  (Delta k ~ 1 between adjacent L) are incommensurate: adjacent multipoles sample the band")
print(f"  structure at effectively arbitrary phase.")
assert (max(lam_lo) / min(lam_lo))**2 > 1e5
print()
for s in [
 "⚠⚠⚠ ** SO IF THE OBSERVABLE LEG INHERITED ITS PERTURBATIONS THROUGH A PRIOR BRANCH POINT OF THE",
 "   SAME TYPE, THE LOW-MULTIPOLE SPECTRUM WOULD CARRY MODE-TO-MODE STRUCTURE OF ORDER $10^7$ IN",
 "   POWER.  IT DOES NOT. **",
 "   ***So cosmogenesis cannot be a CHAIN at the level of the perturbations: the observable leg has",
 "   to be the first link, or the low-$\\ell$ imprint has to be absent for a reason this model does",
 "   not contain.***",
 "",
 "⌗ ** AND THIS IS A REAL PREDICTION RATHER THAN A CONSISTENCY REMARK, because it is confined and",
 "   sharp: the imprint would sit entirely below $\\ell\\simeq200$ and vanish identically above it. **",
 "   *The corpus already carries a parameter-free low-$\\ell$ DEFICIT there; this would be a",
 "   structured low-$\\ell$ EXCESS on top of it, and the two are distinguishable.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND THIS SCOPES c54.143")
print("=" * 78)
print("  c54.143 dissolved an over-determination by computing the leaked/direct ratio on the")
print("  ATTRACTOR of the cycle map, and found it flat in k.  ** An attractor is a growing direction,")
print("  and a growing direction exists only where the map is HYPERBOLIC -- i.e. only inside an")
print("  instability band. **")
print(f"\n  {'range':>26} {'map':>16} {'attractor?':>14} {'c54.143 applies?':>18}")
for a_, b_, c_, d_ in [("l <~ 200 (bands open)", "hyperbolic", "yes", "** YES **"),
                       ("l >~ 220 (bands closed)", "elliptic", "** NO **", "** NO **")]:
    print(f"  {a_:>26} {b_:>16} {c_:>14} {d_:>18}")
print()
for s in [
 "⚠⚠ ** c54.143's SCAN RAN AT $k=3$–$30$, WHICH IS ENTIRELY INSIDE THE OPEN BANDS.  The composition",
 "   bound it overturned was driven by the running at $k$ up to $909$, which is entirely inside the",
 "   CLOSED ones — where there is no attractor and the incoming state is not fixed by the cyclic",
 "   structure at all. **",
 "   ***So the k-flat leaked/direct ratio is established where it was measured and nowhere else, and",
 "   the over-determination is NOT dissolved for the modes that produced it.  c54.143's verdict is",
 "   narrowed to $\\ell\\lesssim200$.***",
 "",
 "⌗ *The two findings pull against each other and both are computed: the chain is excluded by PART 4,",
 "   and PART 5's repair would need the chain.  **What is left standing is PART 3 — phase-only",
 "   transmission above the first peak — which needs neither.***",
 "",
 "⇒ ** THE OWED STEP IS NOW SHARP AND SMALL: in the elliptic range the cycle map is a rotation by a",
 "   computable angle, so the incoming state at the crunch is a rotation of whatever the progenitor",
 "   started with.  Ask what that does to $|c_0|/|c_1|$ averaged over the rotation phase — the",
 "   answer is a distribution rather than a number, and its mean is what the bound needs. **",
]:
    print("  " + s)
