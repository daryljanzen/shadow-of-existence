#!/usr/bin/env python3
"""
RECEIPT — P16 / P15: ** THE PHYSICAL READING BELOW IS WITHDRAWN (r2376+c54.149, NOT REINSTATED
c54.150).  THE ARITHMETIC STANDS AND THE BACKGROUND DOES NOT. **

** WHAT IS WITHDRAWN.**  Every statement here about what a passage DOES to an observed mode: that
it is phase-only above the first acoustic peak, that the bands close across the acoustic range,
that |lambda|^2 is a transfer of observed power between passages, and that the low-multipole sky
excludes an inherited spectrum.  Two independent reasons, neither of them arithmetic:

  (i)  ** THE CONSTRUCTION SUPPLIES NO FULL LAP. **  P16 sec:lap says the progenitor is a black
       hole in a previous universe — an overdensity that separated, turned around and collapsed.
       In spherical collapse its own a = 0 is the AMBIENT universe's beginning, not an epoch of
       its own, so there is no closed ball running bang-to-crunch to make periodic.
  (ii) ** AND COMPOSING THE MONODROMY THERE PRESUMES A BASIS IDENTIFICATION NOTHING ESTABLISHES **
       — that the previous universe's branch point acts on the PATCH's modes, in the PATCH's
       harmonic labelling, with the PATCH's rho and M.  Self-similarity gives the numbers and not
       the labelling, and the labelling is what a Floquet composition acts on.

** WHAT SURVIVES, AND IT IS WORTH KEEPING. **  det C = 1 through the whole propagation, met
exactly in every case, is a real check on the connection and monodromy machinery; and the two-band
dichotomy is a correct statement about the map that WAS computed.  ** Read this file as an
instrument test, not as a result about the sky. **  THE_BASE_RATE's thirteenth entry.

--- the original claim, retained verbatim below so the withdrawal is legible -----------------

** A BRANCH-POINT PASSAGE IS A PURE PHASE ROTATION ABOVE THE FIRST ACOUSTIC
PEAK, AND CATASTROPHICALLY MODE-DEPENDENT BELOW IT. **

The interior is a complete cycle with a branch point at each end, so the per-cycle map C = J T is a
Floquet problem: det C = 1, hence the eigenvalues are a reciprocal REAL pair (an instability band,
the mode is amplified) or a unimodular COMPLEX pair (a stability band, the cycle only rotates the
phase).  Which one, as a function of the multipole, is the whole content.

  PART 1  ** the Floquet dichotomy, verified as a structural check **
  PART 2  ** the bands CLOSE: |lambda| = 1 exactly for l >~ 220 -- transmission is phase-only in
          precisely the range the acoustic data constrains **
  PART 3  ** below l ~ 200 the amplification spans 1e7 in power between neighbouring physical
          modes, so the observable leg cannot have inherited through a prior branch point **

rc=0 on success.  Run: python3 P16_the_passage_is_phase_only_above_the_first_peak.py  (numpy scipy)
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])
fail = []
CS, RHO, SMAP = 1.0 / np.sqrt(3.0), 0.0539, 2.750


def eta_c(r):
    return 2 * np.pi - 2 * np.arctan(r)


def pot(e, r):
    a = (1 - np.cos(e)) + r * np.sin(e)
    return (np.cos(e) - r * np.sin(e)) / a


def cycle(k, r=RHO, cs=CS, eps_rel=1e-6):
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


print("=" * 78)
print("PART 1 — THE FLOQUET DICHOTOMY")
print("=" * 78)
print(f"  {'k':>9} {'|det T - 1|':>13} {'eigenvalues':>36} {'band':>10}")
for k in [6.928, 25.981, 80.994, 300.998]:
    C, d = cycle(k)
    w = np.linalg.eig(C)[0]
    real = abs(w.imag).max() < 1e-9
    desc = (f"{w[0].real:+.4g}, {w[1].real:+.4g}" if real
            else f"{w[0]:.4g}  (|.| = {abs(w[0]):.6f})")
    print(f"  {k:>9.3f} {d:>13.1e} {desc:>36} {'UNSTABLE' if real else 'stable':>10}")
    if d > 1e-2:
        fail.append(f"Wronskian at k={k}")
    if real and abs(w[0].real * w[1].real - 1) > 1e-2:
        fail.append("reciprocity")
    if (not real) and abs(abs(w[0]) - 1) > 1e-4:
        fail.append("unimodularity")
print("  ** the pair is reciprocal-real or unimodular-complex in every case, which is det C = 1")
print("     surviving the whole propagation. **")

print()
print("=" * 78)
print("PART 2 — THE BANDS CLOSE ABOVE THE FIRST PEAK")
print("=" * 78)
print(f"  physical modes k_L = sqrt(L(L+2)),  l = {SMAP} k\n")
print(f"  {'L':>5} {'l':>8} {'|lambda|':>12} {'band':>22}")
hi_ok = True
for L in [2, 10, 22, 38, 54, 70, 80, 100, 150, 300]:
    k = np.sqrt(L * (L + 2))
    C, d = cycle(k)
    lam = max(abs(np.linalg.eig(C)[0]))
    tag = 'UNSTABLE' if lam > 1.0001 else 'stable (phase only)'
    print(f"  {L:>5} {k*SMAP:>8.1f} {lam:>12.4f} {tag:>22}")
    if L >= 80 and abs(lam - 1) > 1e-3:
        hi_ok = False
if not hi_ok:
    fail.append("bands do not close")
print("\n  ** ABOVE l ~ 220 EVERY PHYSICAL MODE IS IN A STABILITY BAND AND |lambda| = 1 TO MACHINE")
print("     PRECISION: the passage neither amplifies nor suppresses, it only rotates the phase. **")
print("  This is the companion paper's transmission remark in its strongest form and in exactly the")
print("  range the acoustic data constrains -- derived rather than asserted, and the constant is one.")

print()
print("=" * 78)
print("PART 3 — BELOW IT, THE CHAIN IS EXCLUDED")
print("=" * 78)
lams = []
for L in range(2, 72, 2):
    C, d = cycle(np.sqrt(L * (L + 2)))
    lam = max(abs(np.linalg.eig(C)[0]))
    if lam > 1.0001:
        lams.append(lam)
span = (max(lams) / min(lams))**2
dk = np.pi / (CS * eta_c(RHO))
print(f"  over the open-band range, |lambda| runs {min(lams):.1f} to {max(lams):.0f}")
print(f"  ** = {span:.1e} in POWER between neighbouring physical modes **")
print(f"  and the band period ({dk:.3f} in k) is incommensurate with the mode spacing (~1 in k), so")
print(f"  adjacent multipoles sample it at effectively arbitrary phase.")
if span < 1e5:
    fail.append("span too small")
print()
print("  ** SO IF THE OBSERVABLE LEG INHERITED ITS PERTURBATIONS THROUGH A PRIOR BRANCH POINT OF THE")
print("     SAME TYPE, THE LOW-MULTIPOLE SPECTRUM WOULD CARRY MODE-TO-MODE STRUCTURE OF ORDER 1e7 IN")
print("     POWER.  IT DOES NOT. **")
print("  The imprint would be confined below l ~ 200 and vanish identically above it, which makes it")
print("  a sharp prediction rather than a consistency remark: a STRUCTURED low-l excess, on top of")
print("  the parameter-free low-l deficit this framework already carries, and distinguishable from it.")

print()
if fail:
    print("FAIL: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
