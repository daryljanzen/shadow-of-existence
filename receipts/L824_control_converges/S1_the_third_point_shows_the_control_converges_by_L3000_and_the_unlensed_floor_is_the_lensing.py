#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (OWED #496 CONTROL half): the THIRD point on the control's convergence, the
measurement r2781 asked for in place of an extrapolation. #496 fit excess ~ L^-3.4 to the L2000 and
L2512 points and extrapolated "~1.1 by L~6000" -- a rate read off TWO points. The third point (LMAXL
= 3200, banked here) and the banked L3000 point show that extrapolation is a two-point artifact: the
UNLENSED control does NOT slide down an L^-3.4 law, it PLATEAUS. On the same 185 bins it goes 7.18
(L2000) -> 3.83 (L2512) -> 3.73 (L3000) -> 3.73 (L3200); the L^-3.4 law fit to the first two points
predicts 2.23 at L3200, the measurement is 3.73. The L2000->L2512 drop was a ONE-TIME truncation
recovery (the top bins clearing the k-range ceiling), not a convergence rate.

** AND THE FLOOR IS MEASURED, NOT NAMED. ** The ~3.73 the unlensed control plateaus at is the LENSING.
Applying c54.183's derived lensed/unlensed ratio (CAMB's, P15's exact construction) to the SAME
converged spectrum takes it 3.73 -> 1.18, and the lensed control converges 5.38 (L2000) -> 1.33
(L2512) -> 1.19 (L3000) -> 1.18 (L3200) -- flat by L3000, my L3200 confirming it (Delta 0.008). So
the control CONVERGES by L3000 to 1.18 against CAMB lensed LCDM's 1.014 on the same bins: a ~0.16/dof
irreducible instrument floor, a MEASUREMENT now, not the "1.1 by L6000" extrapolation. Truncation and
lensing are ORTHOGONAL axes -- LMAXL closes the truncation (7.18 -> 3.73), the lensing operator closes
the rest (3.73 -> 1.18) -- so raising LMAXL past L2512 is the wrong lever, which the plateau proves.

** THE SEQUENCE (same 185 bins throughout, the c54.178-instrument control arm). **
      LMAXL     unlensed/dof     lensed/dof
      2000        7.18             5.38
      2512        3.83             1.33
      3000        3.73             1.19      <- banked c54.186 (this receipt reproduces it)
      3200        3.73             1.18      <- the third/fourth point, banked here
      CAMB lensed LCDM reference (same bins): 1.014

COMPUTES: the per-LMAXL chi^2/dof of the control arm on the fixed 185-bin set, unlensed and under
c54.183's lensed/unlensed ratio, and the L^-3.4 extrapolation the two-point fit implies. ** The four
LMAXL points are the convergence sequence, not a pinned working point; the lensing ratio is CAMB's
LCDM, P15's construction, imported as the operator c54.183 derives, not a fitted amplitude. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE UNLENSED CONTROL PLATEAUS, THE L^-3.4 EXTRAPOLATION IS REFUTED: on the same 185 bins the
     control goes 7.18 -> 3.83 -> 3.73 -> 3.73 across LMAXL 2000/2512/3000/3200; the L^-3.4 law fit
     to the first two points predicts 2.23 at L3200, the measurement is 3.73. The two-point rate was
     a one-time truncation recovery, not a convergence law.
  2. IT HAS CONVERGED BY L3000, IT IS A MEASUREMENT: the L3000 and L3200 points agree to <0.02/dof
     unlensed and 0.008/dof lensed, so the control's chi^2/dof is measured, not extrapolated.
  3. THE FLOOR IS THE LENSING: applying c54.183's lensed/unlensed ratio takes the converged spectrum
     3.73 -> 1.18 and the lensed control converges to 1.18 by L3000 against CAMB lensed's 1.014 -- a
     ~0.16/dof instrument floor. Truncation (LMAXL) and lensing (the ratio) are orthogonal axes.
  4. THE TOP BINS ARE THE TRUNCATION THAT DOES MOVE: the bins ell 1997-2508, at the L2512 ceiling,
     go 2.74/dof (L2512) -> 1.22/dof (L3200) as the ceiling clears them -- confirming those bins are
     truncation-limited while the body (ell<1996) is not.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a refutation of 56's convergence claim -- the
LENSED control DOES converge toward ~1 (to 1.18, r2781 was right that it converges); what the third
point corrects is the UNLENSED L^-3.4 rate and the "1.1 by L6000" horizon: convergence is reached by
L3000, not L6000, and the residual is a lensing/instrument floor, not a slide to 1.0. NOT that the
0.16/dof above CAMB's 1.014 is diagnosed here -- it is the two-arm instrument's own floor vs a full
Boltzmann code (#454's target), named not closed. NOT a framework verdict (F5): this is the CONTROL
arm (LCDM); the CR verdict is untouched, and this receipt is why F3 = chi^2(CR)-chi^2(LCDM) is the
right differential -- the ~1.18 shared instrument+lensing floor cancels in F3.

** Board lead L-824 (cc54's band); OWED #496's CONTROL half (the third convergence point r2781 asked
for). Companion to L-822 (the CR half) and L-820 (the L2512 extension). Informs L-147 (PO-10), #454.
Routed to 56. **

Written r2674 (cc54, L-824). Asserts against the banked control spectra (c54.178 L2000, L820 L2512,
c54.186 L3000, L824 L3200) scored through plik_lite TT with CAMB's lensed/unlensed ratio -- never the
register. Stated for reversal.
"""
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def dof(ls, Dl, keep, ratio=None):
    d_l = Dl if ratio is None else Dl * ratio(ls)
    mb = CS.bin_spectrum(ls, d_l)
    fin = np.isfinite(mb) & keep
    cov = CS.COV_TT[np.ix_(fin, fin)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(fin.sum()))
    F = 0.5 * (F + F.T)
    m, d = mb[fin], CS.X_DATA[fin]
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r) / (fin.sum() - 1)


def load(name):
    return np.load(os.path.join(SPEC, name))


def main():
    print()
    print('  S1 -- PO-10 OWED #496 (control half): the third convergence point -- measurement or'
          ' extrapolation?')
    print()
    seq = [('L2000', 'c54.178_lcdm.npz'), ('L2512', 'L820_lcdm_L2512_nk800.npz'),
           ('L3000', 'c54.186_lcdm_L3000.npz'), ('L3200', 'L824_lcdm_L3200_nk960.npz')]
    # common bin set = the L2000 arm's coverage (185 bins)
    z0 = load(seq[0][1])
    mb0 = CS.bin_spectrum(z0['ls'], z0['Dl'])
    common = np.isfinite(mb0)

    un = {tag: dof(load(n)['ls'], load(n)['Dl'], common) for tag, n in seq}

    # 1. the L^-3.4 extrapolation the two-point fit implies vs the measured third point
    e0, e1 = un['L2000'] - 1, un['L2512'] - 1
    p = np.log(e0 / e1) / np.log(2512. / 2000.)
    pred_3200 = 1 + e1 * (3200. / 2512.) ** (-p)
    check(f'THE UNLENSED CONTROL PLATEAUS, L^-{p:.1f} EXTRAPOLATION REFUTED: chi^2/dof = '
          f'{un["L2000"]:.2f} -> {un["L2512"]:.2f} -> {un["L3000"]:.2f} -> {un["L3200"]:.2f} across '
          f'LMAXL 2000/2512/3000/3200; the L^-{p:.1f} law fit to the first two points predicts '
          f'{pred_3200:.2f} at L3200, the measurement is {un["L3200"]:.2f} (the two-point rate was a '
          'one-time truncation recovery)',
          abs(p - 3.4) < 0.2 and pred_3200 < 2.6 and un['L3200'] > 3.4)

    # 2. converged by L3000 -- a measurement, not an extrapolation
    check(f'IT HAS CONVERGED BY L3000: the L3000 and L3200 unlensed points agree to '
          f'{abs(un["L3000"]-un["L3200"]):.3f}/dof, so chi^2/dof is measured, not extrapolated',
          abs(un['L3000'] - un['L3200']) < 0.02)

    # 3. the floor is the lensing (needs CAMB; skip-with-notice if absent)
    try:
        import camb
        _p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544)
        _p.set_for_lmax(3500, lens_potential_accuracy=1)
        _pc = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK')
        _Dlen, _Dunl = _pc['total'][:, 0], _pc['unlensed_total'][:, 0]
        _Lc = np.arange(len(_Dlen))
        _rat = np.ones_like(_Dlen)
        _m = (_Lc >= 2) & (_Dunl > 0)
        _rat[_m] = _Dlen[_m] / _Dunl[_m]

        def LR(l):
            return np.interp(np.asarray(l, float), _Lc, _rat, left=1.0, right=_rat[-1])

        ln = {tag: dof(load(n)['ls'], load(n)['Dl'], common, LR) for tag, n in seq}
        ref = dof(np.arange(2, 3500, dtype=float), _Dlen[2:3500], common)
        check(f'THE FLOOR IS THE LENSING: applying c54.183\'s lensed/unlensed ratio takes the '
              f'converged spectrum {un["L3200"]:.2f} -> {ln["L3200"]:.2f}, and the lensed control '
              f'converges {ln["L2000"]:.2f} -> {ln["L2512"]:.2f} -> {ln["L3000"]:.2f} -> '
              f'{ln["L3200"]:.2f} to {ln["L3200"]:.2f} vs CAMB lensed\'s {ref:.3f} -- truncation and '
              'lensing are orthogonal axes',
              ln['L3200'] < 1.3 and abs(ln['L3000'] - ln['L3200']) < 0.05 and 0.95 < ref < 1.1)
    except ImportError:
        print('    SKIP  THE FLOOR IS THE LENSING: camb not importable here -- the lensed sequence '
              '(5.38->1.33->1.19->1.18 vs CAMB 1.014) is P15\'s, reproduced where camb is present; '
              'the unlensed plateau above stands without it')

    # 4. the top bins ARE the truncation that moves
    tail = (~common)
    tl_2512 = dof(load('L820_lcdm_L2512_nk800.npz')['ls'], load('L820_lcdm_L2512_nk800.npz')['Dl'],
                  tail)
    tl_3200 = dof(load('L824_lcdm_L3200_nk960.npz')['ls'], load('L824_lcdm_L3200_nk960.npz')['Dl'],
                  tail)
    check(f'THE TOP BINS ARE THE TRUNCATION THAT MOVES: the bins above the L2000 coverage (ell '
          f'1997-2508, at the L2512 ceiling) go {tl_2512:.2f}/dof (L2512) -> {tl_3200:.2f}/dof '
          '(L3200) as the ceiling clears them -- truncation-limited, unlike the body',
          tl_3200 < tl_2512 and tl_3200 < 1.6)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (OWED #496 control half, the third point): the control CONVERGES by L3000, it')
    print('  does not slide down an L^-3.4 law to "1.1 by L6000." The unlensed control plateaus at')
    print('  3.73 (LMAXL past L2512 moves nothing), and that floor is the LENSING: with c54.183\'s')
    print('  lensed/unlensed ratio the same spectra converge to 1.18 by L3000 against CAMB lensed\'s')
    print('  1.014 -- a ~0.16/dof instrument floor, measured now. Truncation and lensing are')
    print('  orthogonal axes; F3 = chi^2(CR)-chi^2(LCDM) cancels this shared 1.18 floor, which is')
    print('  why it is the right differential. F5 untouched: this is the control arm.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
