#!/usr/bin/env python3
r"""B7 -- FOR_54 item 38, answered at production depth: the seam phase MOVES the asymptotic acoustic
intercept, so the 0.62pi disagreement is not a parameter-free structural prediction.

** Board lead L-171 (does the 0.62pi hold against the sky?); informs vein L-202 (what the seam
carries). The measurement a persistent session can do and the chat line cannot. **

** THE QUESTION (item 38). ** After c54.190 the whole front-#2 disagreement is the asymptotic acoustic
phase, fitted on peaks 4-8: phi/pi = 0.878 (CR) against 0.263 (LCDM), a difference of 0.62pi. That fit
rests on ONE pair of spectra. The one freedom known to move things -- the seam phase CRPHI, which
c54.187 showed is ASSIGNED rather than derived and moves l_1/l_A by 2.21x -- was only ever scanned at
LMAXL=1000 (3-4 peaks), so it was never tested against the peaks-4-8 fit. Item 38: does CRPHI move the
ASYMPTOTIC intercept? "If it does not move, the 0.62pi is structural; if it does, the disagreement is a
datum statement after all."  ** State no expected outcome; report what the intercept does. **

** THE RUN. ** Three seam phases {0, pi/2, pi} at production depth, settings matched EXACTLY to
c54.186_cr_L3000 (HIER=1 BSPLIT=1 NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300). Spectra:
item38_cr_phi{0.0,1.5708,3.1416}_prod.npz.
  ** CONTROL: ** phi=0 reproduces c54.186_cr_L3000 to the digit (8 peaks, slope 0.9761, phi/pi 0.878).
  A first attempt at default NK=260 aliased -- phi=0 -> 1.0053 with 10 spurious peaks, no guard fires --
  and was discarded. (Depth/NK-aliasing artefact, filed as a lead: a production spectrum at default NK
  silently aliases at production LMAX and returns a plausible-but-wrong intercept.)

** THE READING. ** The seam phase shifts the LOW peaks hard (phi=pi/2's first peak jumps 172->388,
dropping the count to 7), so a raw peaks-index-4-8 fit conflates that low-l shift with the asymptotic
phase. The clean read assigns each peak its acoustic order n=round(l/lA) and fits the SHARED orders
n=4..7 across all three -- apples to apples, separating the asymptotic phase from the transient.

** THE RESULT (matched acoustic orders 4-7): **
    phi=0    : phi/pi = -0.066   (peaks 1204 1500 1796 2092)
    phi=pi/2 : phi/pi = +0.066   (peaks 1164 1460 1756 2052)
    phi=pi   : phi/pi = -0.244   (peaks 1244 1540 1828 2124)
  span 0.31 of l_A, spacing held at ~0.97 l_A throughout. The order-4..7 peaks shift 70-80 l across
  the seam phase. The acoustic-order fit over l>900 gives span 0.36; the (contaminated) raw-index fit
  0.81 -- all three agree the intercept MOVES, the defensible estimate ~0.31-0.36, about HALF the 0.615
  disagreement.

** THE VERDICT (item 38's second horn). ** The asymptotic intercept MOVES with the seam phase, by about
half the disagreement, while the spacing does not. So the 0.62pi is NOT a parameter-free structural
prediction. It is correct at the paper's default CRPHI=0 (the verified 0.878/0.615 stands there), but a
substantial fraction is carried by the seam-phase datum, which is assigned and not yet derived. Until
CRPHI is fixed from the progenitor, the disagreement carries a datum-uncertainty band comparable to
itself, so the 0.62pi cannot yet be read as a structural falsification against the sky.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that the CR construction is wrong, and not that the default reading is wrong ** -- CRPHI=0
  gives the verified 0.878/0.615 and that stands. ** Not the full CRPHI dependence ** -- three phases,
  and the movement is non-monotonic (-0.066 -> +0.066 -> -0.244), so what is established is THAT it
  moves, not its functional form. ** Not that the 0.62pi is refuted ** -- it is shown datum-contingent,
  which is item 38's own "datum statement" horn, not a refutation. The conversion of any of this to a
  verdict on PO-7 is Daryl's; F5 unsoftened.

Written r2502 (cc54, production run). Stated for reversal.
"""
import os
import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def peaks(name):
    z = np.load(os.path.join(SP, name + '.npz'))
    ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
    return ls[argrelextrema(Dl, np.greater, order=3)[0]], lA


def b4_index(name):
    pk, lA = peaks(name)
    n = np.arange(1, len(pk) + 1)
    m = (n >= 4) & (n <= 8)
    a, b = np.polyfit(n[m], pk[m], 1)
    return len(pk), a / lA, -b / lA


def fit_orders(name, orders=(4, 5, 6, 7)):
    pk, lA = peaks(name)
    ln = pk / lA
    chosen = np.array([pk[np.argmin(np.abs(ln - n))] for n in orders])
    a, b = np.polyfit(np.array(orders), chosen, 1)
    return a / lA, -b / lA


def main():
    print()
    print('  B7 -- does the seam phase move the asymptotic acoustic intercept? (item 38)')
    print()

    # ** control: phi=0 at production settings reproduces the front's c54.186 baseline **
    npk0, s0, phi0 = b4_index('item38_cr_phi0.0_prod')
    npkc, sc, phic = b4_index('c54.186_cr_L3000')
    check('CONTROL: phi=0 at production settings reproduces c54.186_cr_L3000 '
          '(8 peaks, slope ~0.976, phi/pi ~0.878) -- the scan is trustworthy',
          npk0 == 8 and npkc == 8 and abs(phi0 - phic) < 5e-3 and abs(phi0 - 0.878) < 5e-3)

    # ** the matched-order asymptotic fit across the three seam phases **
    ph = {p: fit_orders(f'item38_cr_phi{p}_prod') for p in ['0.0', '1.5708', '3.1416']}
    span = max(ph[p][1] for p in ph) - min(ph[p][1] for p in ph)
    check('the ASYMPTOTIC intercept (matched acoustic orders 4-7) MOVES across the seam phase: '
          f'span = {span:.3f} of l_A, which is substantial (> 0.25)',
          span > 0.25)
    check('and it is about HALF the 0.615 CR-vs-LCDM disagreement '
          f'({span:.3f}/0.615 = {span/0.615:.2f})',
          0.4 < span / 0.615 < 0.7)
    check('while the acoustic SPACING does not move -- it holds at ~0.97 l_A for every phase',
          all(0.95 < ph[p][0] < 0.99 for p in ph))

    # ** the individual intercepts, for the record **
    check('phi=0 -> ~-0.066, phi=pi/2 -> ~+0.066, phi=pi -> ~-0.244 (matched orders)',
          abs(ph['0.0'][1] + 0.066) < 0.02 and abs(ph['1.5708'][1] - 0.066) < 0.02
          and abs(ph['3.1416'][1] + 0.244) < 0.03)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (item 38, second horn -- a MEASUREMENT, not a framework verdict):')
    print('  ** The seam phase MOVES the asymptotic intercept by ~0.31 l_A (half the 0.615')
    print('     disagreement) while the spacing holds. So the 0.62pi is NOT a parameter-free')
    print('     structural prediction: it is correct at the default CRPHI=0 (the verified 0.878/0.615')
    print('     stands there) but a substantial part is carried by the seam-phase datum, which is')
    print('     assigned and not yet derived. **')
    print('  ⇒ Until CRPHI is fixed from the progenitor, the disagreement carries a datum-uncertainty')
    print('    band comparable to itself, so the 0.62pi cannot yet be read as a structural')
    print('    falsification against the sky. Informs L-202 (what the seam carries); answers L-171.')
    print('    F5 unsoftened, PO-7 protected, the conversion is Daryl\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
