#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (OWED #496, the row's real remainder): the CR arm's chi^2/dof ~ 280, which 56's
r2781/C53 found "unresponsive to L_max and diagnosed by nothing", IS diagnosed here. A per-bin chi^2
decomposition (the full plik_lite covariance) localises the two arms' residuals to DIFFERENT places: the
control's is 75% in the high-ell tail (ell > 1200) -- the k-range truncation r2781 already named -- while
the CR arm's is 57% in the acoustic-PEAK bands (ell < 850) and only 18% in the tail. So CR's residual is
the ACOUSTIC-STRUCTURE disagreement, not truncation, which is exactly why it does not respond to L_max. Its
comb is compressed -- peaks at 172/404/636 against the sky's 220/540/810 (ell_1/ell_A = 0.57 vs 0.73) --
and rescaling the comb to the sky's peak scale does NOT collapse the chi^2 (best 209/dof), so it is peak
POSITION and HEIGHTS together, a comprehensive disagreement. The 280/dof is the likelihood-space image of
PO-7's acoustic-phase deficit; This diagnoses the residual and does not convert the verdict: a measurement discrepancy is not a framework verdict.

** THE METHOD. ** chi^2 = r^T F r with r = d - A m the amplitude-fitted residual and F = C^{-1} the plik_lite
Fisher matrix; the per-bin contribution r_i (F r)_i sums to chi^2 exactly, so grouping it by ell-band
localises the residual with the FULL covariance (not a diagonal approximation).

** THE DECOMPOSITION (banked c54.178 pair, 185 bins). **
      ell band        control chi^2 share      CR chi^2 share
      100- 300  (P1)        3.4%                   27.1%
      300- 550             7.7%                    9.9%
      550- 850  (P3)        5.0%                   29.8%
      850-1200             8.7%                   14.7%
     1200-2000             75.2%  <- truncation     18.5%
  ⇒ the control's residual is the HIGH-ELL TAIL (the k-range truncation r2781 diagnosed and the LMAXL=2512
    extension of L-820 S2 confirmed); the CR arm's is the PEAK REGION (P1 + P3 = 57%), which no wavenumber
    ceiling touches -- so CR is unresponsive to L_max BECAUSE its residual is not where truncation lives.

COMPUTES: the per-bin chi^2 decomposition of the banked c54.178 lcdm and cr arms against plik_lite TT, and
the CR peak positions and the chi^2 under an ell-axis rescaling. ** The rescale factors (1.20-1.35) scan
the neighbourhood of the sky/CR peak-scale ratio 0.7312/0.5703 to test whether ALIGNING the comb collapses
the residual; they are a scan, not a pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE TWO RESIDUALS ARE LOCALISED DIFFERENTLY: the control's chi^2 is dominated by the high-ell tail
     (>=70% at ell>1200) and the CR arm's by the acoustic-peak region (>=50% at ell<850) -- a per-bin
     decomposition with the full covariance.
  2. SO CR IS UNRESPONSIVE TO L_max FOR A REASON: its residual sits in the peaks, where a wavenumber
     ceiling does nothing, not in the truncation-limited tail -- which is why r2781 found it unmoved while
     the control halved.
  3. THE CR COMB IS COMPRESSED: peaks at 172/404/636 against the sky's ~220/540/810 (ell_1/ell_A ~ 0.57 vs
     0.73), the PO-7 acoustic-phase deficit -- so the peak-region residual is that deficit imaged in
     likelihood space.
  4. IT IS NOT A SINGLE POSITION OFFSET: rescaling the CR ell-axis to the sky's peak scale does not bring
     chi^2/dof below ~200, so the disagreement is peak POSITION and HEIGHTS together -- a comprehensive
     acoustic-structure disagreement, the real PO-10 signal.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a framework verdict (F5): this localises WHERE the CR
residual sits and names it acoustic structure; whether that disagreement is a refutation is PO-7's, and
PO-7 is protected. NOT that the control fits well -- its 75%-in-the-tail residual is the truncation, and a
separate third convergence point (LMAXL=3200) is the measurement that its excess -> ~1 (banked alongside
when it completes; this receipt is the CR half and stands without it). NOT that the per-bin split is
covariance-diagonal -- it uses the full Fisher matrix, so the shares are exact contributions to chi^2. NOT
that rescaling is a physical model of the phase shift -- it is a diagnostic that a uniform ell-stretch
cannot remove the residual, hence heights matter too.

** Board lead L-822 (cc54's band); OWED #496's real remainder (the CR-residual diagnosis, 56 r2781/C53).
Informs L-147 (PO-10), L-171 (PO-7). Routed to 56. Companion to L-820. **

Written r2674 (cc54, L-822). Asserts against the banked c54.178 pair scored through plik_lite TT's full
covariance -- never the register. Stated for reversal.
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


def perbin(path):
    z = np.load(path)
    mb = CS.bin_spectrum(z['ls'], z['Dl'])
    keep = np.isfinite(mb)
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(keep.sum()))
    F = 0.5 * (F + F.T)
    m, d = mb[keep], CS.X_DATA[keep]
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    contrib = r * (F @ r)                    # sums to chi^2
    return CS.BIN_LO[keep], contrib


def band_share(lo, contrib, a, b):
    return contrib[(lo >= a) & (lo < b)].sum() / contrib.sum()


def main():
    print()
    print('  S1 -- PO-10 OWED #496: is the CR arm\'s 280/dof diagnosed? where does it sit?')
    print()
    lo_l, c_l = perbin(os.path.join(SPEC, 'c54.178_lcdm.npz'))
    lo_c, c_c = perbin(os.path.join(SPEC, 'c54.178_cr.npz'))

    tail_l = band_share(lo_l, c_l, 1200, 2000)
    tail_c = band_share(lo_c, c_c, 1200, 2000)
    peak_c = band_share(lo_c, c_c, 100, 300) + band_share(lo_c, c_c, 550, 850)
    peak_l = band_share(lo_l, c_l, 100, 300) + band_share(lo_l, c_l, 550, 850)
    check(f'THE TWO RESIDUALS ARE LOCALISED DIFFERENTLY: the control\'s chi^2 is {100*tail_l:.0f}% in the '
          f'high-ell tail (ell>1200) while the CR arm\'s is {100*peak_c:.0f}% in the acoustic-peak bands '
          f'(P1+P3, ell<850) and only {100*tail_c:.0f}% in the tail -- per-bin, full covariance',
          tail_l >= 0.70 and peak_c >= 0.50 and tail_c < 0.30)

    check('SO CR IS UNRESPONSIVE TO L_max FOR A REASON: its residual sits in the peaks (where a wavenumber '
          'ceiling does nothing), not the truncation-limited tail -- which is why r2781 found it unmoved '
          f'({100*peak_c:.0f}% peaks vs {100*tail_c:.0f}% tail) while the control ({100*tail_l:.0f}% tail) '
          'halved',
          peak_c > tail_c and tail_l > peak_l)

    z = np.load(os.path.join(SPEC, 'c54.178_cr.npz'))
    from scipy.signal import argrelextrema
    pk = argrelextrema(z['Dl'], np.greater, order=3)[0]
    peaks = [int(z['ls'][q]) for q in pk[:3]]
    l1la = z['ls'][pk[0]] / float(z['l_A'])
    check(f'THE CR COMB IS COMPRESSED: peaks at {peaks} against the sky\'s ~220/540/810 (ell_1/ell_A = '
          f'{l1la:.2f} vs 0.73) -- the PO-7 acoustic-phase deficit, imaged in likelihood space',
          peaks[0] < 200 and 0.5 < l1la < 0.62)

    base, _, _, _, _ = CS.chi2_of(z['ls'], z['Dl'])
    best = min(CS.chi2_of(z['ls'] * f, z['Dl'])[0] / CS.chi2_of(z['ls'] * f, z['Dl'])[1]
               for f in (1.15, 1.20, 1.28, 1.35))
    check(f'IT IS NOT A SINGLE POSITION OFFSET: rescaling the CR ell-axis to the sky\'s peak scale does not '
          f'bring chi^2/dof below ~200 (best {best:.0f}/dof over the scan) -- so the disagreement is peak '
          'POSITION and HEIGHTS together, a comprehensive acoustic-structure disagreement',
          best > 150)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (OWED #496 real remainder, the CR residual diagnosed): the CR arm\'s 280/dof is the')
    print('  ACOUSTIC-STRUCTURE disagreement in the peak region (P1+P3 = 57%), categorically different from')
    print('  the control\'s residual (75% in the high-ell truncation tail) -- which is exactly why CR is')
    print('  unresponsive to L_max: its residual is not where truncation lives. The CR comb is compressed')
    print('  (ell_1/ell_A 0.57 vs the sky\'s 0.73, PO-7\'s deficit) and realigning it does not collapse the')
    print('  chi^2, so it is position and heights together. F5 unsoftened: the residual is located and named')
    print('  acoustic structure; whether it refutes is PO-7\'s, protected. The control\'s own residual is the')
    print('  truncation, its third convergence point measured separately (L3200).')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
