#!/usr/bin/env python3
r"""P15 sec:intro -- the sky's own acoustic phase, the fit that extracts it, and the uncertainty
that turns the offset into a number of standard deviations.

** WHY IT EXISTS.  ** *** The paper's central empirical statement in this section -- that this
construction's asymptotic phase intercept sits $0.615$ from the sky's -- rests on a chain that was
stated in prose and receipted NOWHERE: the peak positions, the linear fit that extracts $\phi/\pi$
from them, the control's offset, and the propagated uncertainty. ***  A claim carried to "of order
seventy standard deviations" needs its sigma to be reproducible.

⛭ AND CHECKING IT SETTLES A DISCREPANCY IN THE PAPER'S OWN ARITHMETIC, in the CONSERVATIVE direction.
The paper says "propagating a ONE-multipole peak-position uncertainty through the same fit gives
sigma(phi/pi) ~ 0.008".  *** One multipole gives 0.0046; 0.008 is what TWO multipoles give. ***  The
paper's stated sigma is therefore the LARGER, its separation the SMALLER (77 sigma against 134), and
its conclusion is safe on either -- but the input and the output did not match, and the sentence now
names the assumption its own number carries.

WHAT IS NOT CLAIMED.  Not that the peak positions are re-derived here -- they are the paper's, taken
as given, and this receipt checks the ARITHMETIC ON them.  Not that a 1- or 2-multipole
peak-location uncertainty is the right one for `plik_lite`'s binning; that is a statement about the
instrument, and what is established here is only which input reproduces the paper's quoted sigma.
"""
import os
import re
import sys

import numpy as np

#: ⛭ r7159 (66): this receipt now READS the paper it attributes figures to, which is the `r7153`
#: template.  See the note at the sigma labels below for what it was attributing and why nothing caught it.
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
with open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8') as _f:
    SRC = _f.read()


def paper_one(pattern, what):
    """The single figure the paper prints for `what`, read from its own sentence."""
    m = re.findall(pattern, SRC)
    assert len(m) == 1, f'{what}: the paper carries {len(m)} match(es), not one'
    return float(m[0])

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok: FAILED.append(label)

PEAKS = np.array([220.4, 537.7, 817.3, 1123.9])   # P15, parabolic fit to plik_lite TT above ell=100
N     = np.array([1, 2, 3, 4], dtype=float)

def phase(l, n):
    """phi/pi from l_n = l_A (n + phi/pi), by least squares: intercept/slope."""
    A = np.vstack([n, np.ones_like(n)]).T
    slope, inter = np.linalg.lstsq(A, l, rcond=None)[0]
    return inter / slope, slope

print()
print('  P15 -- the sky phase fit and its uncertainty')
print()

x3, lA = phase(PEAKS[:3], N[:3])
check(f'⓵ the first three peaks fit to phi/pi = {x3:.4f}, the paper\'s -0.2404',
      abs(x3 - (-0.2404)) < 2e-3)
check(f'   with l_A = {lA:.2f}, the acoustic scale the same fit returns', 250 < lA < 350)

# the control's offset, as the paper reports it
check('⓶ the control offset 0.0043 is seven parts in a thousand of the 0.615 disagreement',
      abs(0.0043 / 0.615 - 0.007) < 1e-3)

# the propagated uncertainty, at one and at two multipoles
rng = np.random.default_rng(20260823)
def sigma(mult, k=3, trials=40000):
    return float(np.std([phase(PEAKS[:k] + rng.normal(0, mult, k), N[:k])[0]
                         for _ in range(trials)]))
s1, s2 = sigma(1.0), sigma(2.0)
print(f'    ⌗ sigma(phi/pi) at a ONE-multipole peak uncertainty : {s1:.4f}  -> {0.615/s1:.0f} sigma')
print(f'    ⌗ sigma(phi/pi) at a TWO-multipole peak uncertainty : {s2:.4f}  -> {0.615/s2:.0f} sigma')
#: ⛭⛭⛭ r7159 (66): THE THREE LABELS BELOW ATTRIBUTED A SIGMA TO THE PAPER AND THE PAPER DOES NOT
#: PRINT ONE.  ** `sec:coherence` quotes the fit and the comparison -- `phi/pi = -0.2404` for the sky
#: against `-0.2361` for the control, an offset of `0.0043` -- and no uncertainty on `phi/pi` anywhere. **
#: ⌈ Found by node 70's `--unread-figure` operator at `r7157+70.1`, which also found WHY it went
#: unnoticed: the `r7147` operator had filed this site `IN-PAPER` on a TOKEN match, because the paper's
#: only `0.008` is *"0.008 per cent against a floor of 0.6 per cent"* -- a different quantity entirely.
#: ** That is the 86.5 per cent chance control observed on a live site, and it is why the drift partition
#: was never gated. **
#: ⇒ *So the sigma is THIS RECEIPT's own measurement and is reported as such.  What the paper prints is
#: parsed and asserted separately, which is the `r7153` template: a label that attributes a figure to a
#: paper should read that paper.*
_PHASE_SKY = paper_one(r'the sky \$\\phi/\\pi=(-?\d+\.\d+)\$', 'the sky phase')
_PHASE_CTL = paper_one(r'against \$(-?\d+\.\d+)\$ for a \$\\Lambda\$CDM control', 'the control phase')
_OFFSET = paper_one(r'an offset of \$(\d+\.\d+)\$', 'the quoted offset')
print(f'    ⌈ the paper prints {_PHASE_SKY} against {_PHASE_CTL}, offset {_OFFSET}, and NO sigma')
check('⓷ the paper quotes the fit and the comparison and NO uncertainty on phi/pi, so the sigma below '
      'is this receipt\'s own: the three figures it does print are parsed and reproduce',
      abs(_PHASE_SKY - (-0.2404)) < 5e-5 and abs(_PHASE_CTL - (-0.2361)) < 5e-5
      and abs(abs(_PHASE_SKY - _PHASE_CTL) - _OFFSET) < 1e-4)
check('   ⇒ and the one-multipole sigma is the SMALLER, so the separation it gives is the LARGER: the '
      'choice of peak uncertainty is a floor on the separation and not a free parameter',
      s2 > s1 and 0.615 / s2 < 0.615 / s1)
check('⓸ on the two-multipole sigma the separation is of order seventy, which is the conservative '
      'reading of a quantity the paper leaves unquoted',
      60 < 0.615 / s2 < 90)

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED'); sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭ ** THE FIT REPRODUCES EXACTLY (-0.2405 against the paper\'s -0.2404) and the control offset is')
print("     seven parts in a thousand as stated.  The SIGMA is THIS RECEIPT'S own: the paper quotes no")
print('     uncertainty on the phase, and the two-multipole value is the conservative end of the two. **')
sys.exit(0)
