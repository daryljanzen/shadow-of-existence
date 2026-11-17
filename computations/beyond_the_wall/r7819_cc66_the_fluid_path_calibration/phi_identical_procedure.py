#!/usr/bin/env python3
"""r7819 ⑦ (cc66): THE CONTROL'S PHASE BY THE SENTENCE'S OWN PROCEDURE.

P15 `sec:intro` prints the sky's quartet as *"$220.4$, $537.7$, $817.3$ and
$1123.9$"* -- **a parabolic fit to each hump of the `plik_lite` binned TT spectrum
above `l=100`** -- and then fits `l_n = l_A(n + phi/pi)` to the first three of
THOSE peaks.  So the sky's `-0.2404` is the parabolic quartet's own fit, and the
control's figure must come through the same two steps on the control's spectrum:
a parabolic fit to each of its first three humps, then the same three-peak fit.

⛔ ** AND THAT IS NEITHER OF THE TWO PROCEDURES I FIRST CONSIDERED. **  `r7819+cc66.1`
reported a fork between the raw cell maxima (`score()`, `-0.2379`) and P15's
matched locator (`-0.2295`), and chose the matched locator on the ground that it
is "identical in kind" for a binned sky and a computed spectrum.  Reading the
SENTENCE BEFORE settles it differently: the matched locator puts the sky's peaks
at `220.98 / 533.79 / 814.79 / 1121.85`, which is NOT the quartet the paragraph
prints, so pairing a matched control with the paper's sky would again be two
procedures.  The raw cell maxima are not it either -- `argrelextrema` returns grid
cells, not a parabolic fit.
  ⇒ *The identical procedure is the parabolic one, applied to the control.  It is
  computed here because nothing in the tree computes it: `r7819` ⑦'s trace found
  the printed `-0.2361` was written in at `r3005` and never produced.*
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
R7812 = os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass')

SKY_QUARTET = np.array([220.4, 537.7, 817.3, 1123.9])   # P15 sec:intro's own printed peaks


def parabolic_peaks(ls, Dl, n=3, order=3):
    """a parabolic fit to each of the first `n` humps -- the sentence's own locator.

    A three-point parabola through the local maximum and its neighbours, which is
    what "a parabolic fit to each hump" means on a sampled spectrum; the cell
    maximum itself is the zeroth-order version of it and is what `score()` uses.
    """
    from scipy.signal import argrelextrema
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0]:
        if len(out) == n:
            break
        if i == 0 or i + 1 >= len(Dl):
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2.0 * y1 + y2
        d = 0.0 if den == 0 else 0.5 * (y0 - y2) / den
        out.append(float(ls[i]) + d * float(ls[i] - ls[i - 1]))
    return np.array(out)


def fit_phase(peaks):
    """l_n = l_A (n + phi/pi) on n = 1..len(peaks); returns (l_A, phi/pi)"""
    n = np.arange(1, len(peaks) + 1, dtype=float)
    A = np.vstack([n, np.ones_like(n)]).T
    lA, b = np.linalg.lstsq(A, peaks, rcond=None)[0]
    return float(lA), float(b / lA)


BANKS = {
    "the control, un-refitted  (cc66_lcdm_L2000)":
        os.path.join(BW, 'spectra', 'cc66_lcdm_L2000.npz'),
    "the control, Planck 2018 published  ((a1)'s assembly)":
        os.path.join(R7812, 'out', 'r7812_control_step2_L2000_assembled.npz'),
}

lA_s, phi_s = fit_phase(SKY_QUARTET[:3])
print(f'  the sky, from P15\'s own printed quartet: l_A = {lA_s:.2f}, phi/pi = {phi_s:+.4f}')
assert abs(phi_s - (-0.2404)) < 5e-4, f"the paper's own -0.2404 does not reproduce: {phi_s:+.4f}"
print("  ✓ anchor held: the paper's -0.2404 reproduces from the quartet it prints\n")

out = {}
for tag, p in BANKS.items():
    z = np.load(p, allow_pickle=True)
    pk = parabolic_peaks(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    lA, phi = fit_phase(pk)
    out[tag] = phi
    print(f'  {tag}')
    print(f'      parabolic peaks {np.round(pk, 2)}  l_A = {lA:.2f}  phi/pi = {phi:+.4f}')
    print(f'      offset from the sky = {abs(phi_s - phi):.4f}  '
          f'-> {abs(phi_s - phi) / 0.615 * 1000:.0f} parts in a thousand of the 0.615 disagreement')

old, new = list(out.values())
print(f'\n  ⇒ the control\'s phase by the sentence\'s own procedure: {old:+.4f} -> {new:+.4f}')
print(f'    and the printed -0.2361 is neither, which is what "no producer" means in numbers')
sys.exit(0)
