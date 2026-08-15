#!/usr/bin/env python3
r"""S1 -- cc54, PO-11 (L-813's flagged next: enumerate the discrete tower): the count is ZERO. L-813
delivered the radial-Dirac SUSY barrier V_pm = W^2 +- dW/dx (W = lambda sqrt(f)/r, W=0 at both SdS
horizons) and left the explicit discrete-tower COUNT unrun, flagging that a naive finite box gives a
count that grows with the box (a continuum-discretisation artefact). Here the count is settled: it is
ZERO. The reason is SUSY POSITIVITY -- V_pm = W^2 +- W' factorises as A^(dagger)A with A = d/dx + W, so
BOTH partners have spectrum >= 0 and there is no state below the continuum threshold at omega^2 = 0.
The zero-energy candidate exp(-int W dx) is non-normalisable (L-813 check 4, int W finite), so omega^2
= 0 carries no bound state either. Hence the bound tower is EMPTY -- consistent with SdS stability
(no growing mode) -- and the physical discrete content is the QNM RESONANCE spectrum (complex omega,
Im < 0), which is SHARED by the partners because they are iso-scattering (L-813 check 3).

** THE NUMERICS THAT CONFIRM IT. ** A finite-difference discretisation of both partners on the tortoise
line, at boxes L = 10, 20, 40:
    * NO NEGATIVE EIGENVALUE at any box for either partner (min eigenvalue > 0 throughout);
    * the min eigenvalue -> 0 like ~1/L^2 (0.037 -> 0.0076 -> 0.0017 as L doubles) -- the box's own
      threshold mode, NOT a bound state pulled below zero;
    * the count of near-zero "levels" GROWS with the box (1 -> 2 -> 5) -- the continuum density of
      states, the artefact L-813 flagged, not a physical tower;
    * the factorisation V_pm = W^2 +- W' holds to 1e-4 (W' by an independent gradient), so the SUSY
      form -- hence positivity -- is not an assumption but a checked identity.

COMPUTES: the FD spectrum of V_pm on the SdS tortoise line at three box sizes, the min-eigenvalue
scaling, the near-zero level count vs box, and the V_pm = W^2 +- W' factorisation. ** The member
(alpha=1, M=0.10, lambda=1) is L-813's representative sub-Nariai point; the ZERO count is member-
independent -- it rests on the SUSY factorisation (W=0 at the horizons), not the member. **

** WHAT THIS RECEIPT ASSERTS. **
  1. NO BOUND STATES, BY SUSY POSITIVITY: V_pm = W^2 +- W' = A^(dagger)A >= 0 (A = d/dx + W); numerically
     neither partner has a negative eigenvalue at any box, and the factorisation identity holds -- so
     the discrete tower below the continuum is EMPTY (count = 0).
  2. THE NAIVE BOX 'TOWER' IS THE ARTEFACT L-813 NAMED: the near-zero level count grows with box
     (1->2->5 for L=10->20->40) and the min eigenvalue -> 0 like ~1/L^2, both signatures of the
     continuum density of states, not physical levels.
  3. THE PHYSICAL DISCRETE CONTENT IS RESONANCES, SHARED: with no bound states the tower is the QNM
     spectrum (poles of the transmission amplitude, complex omega, Im<0 for decay), shared by the
     partners because they are iso-scattering (|T+|^2=|T-|^2, L-813) -- so it is one shared resonance
     tower, the continuum face of isospectrality.

** WHAT IS NOT CLAIMED, stated for reversal. ** The explicit QNM FREQUENCIES are NOT pinned here: a
direct complex-omega integration of the outgoing amplitude is unstable (it did not converge to a pole),
and a stabilised Leaver/continued-fraction solve is the right tool, flagged not run -- this receipt
settles the BOUND count (zero) and the resonance CHARACTER (shared), not the resonance frequencies.
NOT a claim that SdS is stable from here -- stability is the framework's (no omega^2<0 is what SUSY
positivity shows, consistent with it); this is the spectral statement, not a stability proof. NOT a
framework verdict (F5): PO-11's row is the observer line's; this supplies the count L-813 flagged.

** Board lead L-827 (cc54's band); completes L-813's flagged enumeration (the discrete-tower count).
Informs L-175/family-6, PO-11. Routed to 56. **

Written r2674 (cc54, L-827). Asserts against a live FD spectral computation on the SdS tortoise line
-- never the register. Stated for reversal.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal

ALPHA, M, LAM = 1.0, 0.10, 1.0
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2 * M / r - r ** 2 / ALPHA ** 2


def fp(r):
    return 2 * M / r ** 2 - 2 * r / ALPHA ** 2


RB = brentq(f, 0.05, 0.5)
RC = brentq(f, 0.5, 2.0)
R0 = 0.5 * (RB + RC)


def Wr(r):
    return LAM * np.sqrt(np.clip(f(r), 0.0, None)) / r


def dWdx(r):                                     # = f dW/dr, stable (no 1/sqrt(f))
    fr = np.clip(f(r), 0.0, None)
    return LAM * (np.sqrt(fr) * fp(r) / (2 * r) - fr ** 1.5 / r ** 2)


def Vpm(r, s):
    return Wr(r) ** 2 + s * dWdx(r)


def r_of_x(L, n):
    xs = np.linspace(0, L, n)

    def ev(xm, xe):
        return solve_ivp(lambda x, r: [np.clip(f(r[0]), 0, None)], [0, xm], [R0],
                         t_eval=xe, rtol=1e-11, atol=1e-13).y[0]
    rp = np.clip(ev(L, xs), RB + 1e-14, RC - 1e-14)
    rm = np.clip(ev(-L, -xs), RB + 1e-14, RC - 1e-14)
    return np.concatenate([-xs[::-1][:-1], xs]), np.concatenate([rm[::-1][:-1], rp])


def spectrum(L, s, n=4000):
    x, r = r_of_x(L, n)
    xu = np.linspace(-L, L, 4000)
    ru = np.interp(xu, x, r)
    h = xu[1] - xu[0]
    V = Vpm(ru, s)
    w = eigh_tridiagonal(2 / h ** 2 + V, -1 / h ** 2 * np.ones(len(xu) - 1),
                         select='i', select_range=(0, 30))[0]
    return w


def main():
    print()
    print('  S1 -- PO-11: the Dirac barrier\'s discrete tower -- how many bound states?')
    print()
    boxes = (10, 20, 40)
    mins, negs, nearc = {}, {}, {}
    for L in boxes:
        for s in (+1, -1):
            w = spectrum(L, s)
            mins[(L, s)] = w[0]
            negs[(L, s)] = int((w < -1e-6).sum())
            nearc[(L, s)] = int((w < 0.05).sum())

    no_neg = all(v == 0 for v in negs.values())
    all_pos_min = all(mins[k] > -1e-6 for k in mins)
    check(f'NO BOUND STATES, BY SUSY POSITIVITY: V_pm = W^2 +- W\' = A(dag)A >= 0; neither partner has a '
          f'negative eigenvalue at L=10/20/40 (min eig V+ = {mins[(10,1)]:.4f}/{mins[(20,1)]:.4f}/'
          f'{mins[(40,1)]:.4f}, all > 0), so the tower below the continuum is EMPTY (count = 0)',
          no_neg and all_pos_min)

    # min eig -> 0 like ~1/L^2 (box threshold, not a bound state)
    ratio = mins[(10, 1)] / mins[(40, 1)]
    check(f'THE MIN EIGENVALUE -> 0 LIKE ~1/L^2 (box threshold, not a pulled-down bound state): V+ min '
          f'{mins[(10,1)]:.4f} (L=10) -> {mins[(40,1)]:.4f} (L=40), ratio {ratio:.1f} ~ (40/10)^2=16 '
          'for a continuum threshold mode',
          8 < ratio < 30)

    grow = nearc[(10, 1)] < nearc[(20, 1)] < nearc[(40, 1)]
    check(f'THE NAIVE BOX "TOWER" IS THE ARTEFACT L-813 NAMED: the near-zero (<0.05) level count GROWS '
          f'with box -- V+ {nearc[(10,1)]}->{nearc[(20,1)]}->{nearc[(40,1)]} for L=10->20->40 (the '
          'continuum density of states), so those are not physical levels',
          grow)

    # factorisation identity, W' by independent gradient
    x, r = r_of_x(12, 6000)
    Wx = Wr(r)
    Wp = np.gradient(Wx, x)
    m = np.abs(x) < 8
    errp = np.abs(Vpm(r, +1) - (Wx ** 2 + Wp))[m].max()
    errm = np.abs(Vpm(r, -1) - (Wx ** 2 - Wp))[m].max()
    check(f'THE SUSY FACTORISATION IS A CHECKED IDENTITY, NOT AN ASSUMPTION: V_pm = W^2 +- W\' (W\' by '
          f'an independent gradient) holds to max err {max(errp, errm):.1e} on |x|<8 -- so positivity, '
          'hence the zero count, is structural',
          max(errp, errm) < 1e-3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-11, L-813\'s flagged enumeration): the Dirac barrier\'s discrete BOUND tower is')
    print('  EMPTY -- count ZERO -- by SUSY positivity (V_pm = A(dag)A >= 0), confirmed numerically (no')
    print('  negative eigenvalue at any box; the near-zero count grows with the box, the artefact L-813')
    print('  named). The physical discrete content is the QNM resonance spectrum (complex omega, Im<0),')
    print('  shared by the partners via iso-scattering; its frequencies need a stabilised Leaver solve,')
    print('  flagged. cc54 supplied the count, not a verdict on the row (F5, PO-11 the observer line\'s).')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
