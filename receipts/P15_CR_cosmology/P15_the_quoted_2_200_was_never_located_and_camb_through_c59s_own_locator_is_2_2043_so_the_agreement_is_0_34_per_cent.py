#!/usr/bin/env python3
r"""P15 sec:coherence -- THE `2.200` AT `l.857` WAS A HARDCODED LITERAL AND NOTHING EVER LOCATED IT.
CAMB AT `C59`'S OWN POINT, THROUGH `C59`'S OWN LOCATOR, RETURNS $2.2043$, SO THE AGREEMENT IS
$0.34\%$ AND NOT $0.14\%$.

** WHY IT EXISTS.  ** *** `l.857` prints the control's $P_1/P_2=2.1969$ "against a standard code's
$2.200$---agreement to $0.14\%$", and `C59` line 116 is `CAMB_R2 = 2.200`: a LITERAL.  No CAMB is run
in that receipt and no locator touches that number. ***  So the agreement compared a LOCATED
instrument figure against a QUOTED one -- the same defect `r7813+70` measured away at the CALIBRATED
configuration (CAMB $2.2123$ through P15's matched locator, against a printed $2.200$ there too).

⛭ AND THE TWO SENTENCES ARE THE SAME PATH IN TWO CONFIGURATIONS, WHICH IS WHY BOTH NEEDED DOING.
`l.877` says in as many words that the $0.14\%$ *"belong[s] to a different run and not to this one"*:
`l.857` is `C59`'s own `LMAXL=900, NK=280` run at the instrument's UN-REFITTED default point, `l.877`
the calibrated configuration at Planck~2018's published point.  Both are the POLARISATION path -- the
instrument says so at its own line 97 and `PO13_WORKING_STATE` at l.332, l.553 and l.623.  *The order
that handed this over read `l.857` as the FLUID path; the sentence's own opening clause, which names
the polarisation source the projection carries, settles it the other way.*

WHAT IS NOT CLAIMED.  Not that `C59`'s $2.1969$ is re-run -- it is `C59`'s, and this receipt supplies
only the number it should have been compared against.  Not that the LENSED comparison is the right
one: the instrument's hierarchy output is unlensed, so the like-for-like figure is CAMB's unlensed
$2.2043$, and the lensed $2.2122$ is reported beside it rather than used.

COMPUTES: CAMB once at `C59`'s point; the locator is `C59`'s own, re-expressed.  rc=0 on success.
"""
import os
import re
import sys

import numpy as np
from scipy.signal import argrelextrema

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                    # noqa: E402

with open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8') as _f:
    SRC = _f.read()
C59 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation.py')
with open(C59, encoding='utf-8') as _f:
    C59SRC = _f.read()

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


def paper_one(pattern, what):
    m = re.findall(pattern, SRC)
    assert len(m) == 1, f'{what}: the paper carries {len(m)} match(es), not one'
    return float(m[0])


#: `C59`'s point, read off the instrument's control default (`ACOUSTIC_two_arm` l.149-151 and l.93):
#: `C59` sets only ARM, NK and LMAXL, so H0/Omega_m/omega_b/n_s are the UN-REFITTED literals.
H0, OM, OMBH2, NS = 67.40, 0.3150, 0.0224, 0.965
OMCH2 = OM * (H0 / 100.0) ** 2 - OMBH2
#: `C59`'s reported grid verbatim: `np.arange(100, int(AT.LMAXL), int(LSTEP))` at LMAXL=900, LSTEP=8.
LS = np.arange(100, 900, 8)


def located(cl_tt):
    """`C59`'s locator verbatim -- RAW CELL MAXIMA, which is why its peaks print as grid cells."""
    Dl = np.asarray([cl_tt[int(l)] for l in LS], float)
    pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
    assert len(pk) >= 3, f'fewer than three peaks: {pk}'
    return ([float(LS[q]) for q in pk[:3]],
            float(Dl[pk[0]] / Dl[pk[1]]), float(Dl[pk[0]] / Dl[pk[2]]))


print()
print('  P15 -- the quoted 2.200 was never located, and what the locator returns instead')
print()

check('⓵ `C59` holds its standard-code figure as a LITERAL, with no CAMB run and no locator on it: '
      'that is what makes the printed agreement a comparison of unlike things',
      re.search(r'^CAMB_R2 = 2\.2\d*$', C59SRC, re.M) is not None
      and 'import camb' not in C59SRC)
check('   and its locator is RAW CELL MAXIMA on its own reported grid, which this receipt reuses',
      'argrelextrema(Dl, np.greater, order=3)' in C59SRC
      and "np.arange(100, int(AT.LMAXL), int(os.environ.get('LSTEP', '8')))" in C59SRC)

p = camb.set_params(H0=H0, ombh2=OMBH2, omch2=OMCH2, ns=NS, tau=0.0544, As=2.1e-9,
                    mnu=0.0, num_massive_neutrinos=0, omk=0, lmax=1500)
cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=1500)
pk_u, r2_u, r3_u = located(cl['unlensed_scalar'][:, 0])
pk_l, r2_l, r3_l = located(cl['total'][:, 0])
print(f'    ⌗ the point: H0 {H0}  Omega_m {OM}  omega_b {OMBH2} -> omega_c {OMCH2:.5f}  n_s {NS}')
print(f'    ⌗ CAMB unlensed  peaks {[int(x) for x in pk_u]}  P1/P2 = {r2_u:.4f}  P1/P3 = {r3_u:.4f}')
print(f'    ⌗ CAMB   lensed  peaks {[int(x) for x in pk_l]}  P1/P2 = {r2_l:.4f}  P1/P3 = {r3_l:.4f}')

#: ⛭ the locator is CONFIRMED rather than assumed: run on CAMB it returns `C59`'s own printed triple.
check('⓶ the reconstructed locator returns `C59`\'s own peak triple 220 / 540 / 812 when run on CAMB, '
      'so the grid and the locator are its, not a re-derivation of them',
      [int(x) for x in pk_u] == [220, 540, 812] and [int(x) for x in pk_l] == [220, 540, 812])

check(f'⓷ CAMB\'s unlensed first-to-second height ratio through that locator is {r2_u:.4f}, and the '
      f'instrument\'s output is unlensed too, so this is the like-for-like figure',
      abs(r2_u - 2.2043) < 5e-5)
check(f'   the lensed one is {r2_l:.4f}, reported beside it and not used',
      abs(r2_l - 2.2122) < 5e-5)
check('   ⇒ and NEITHER is the quoted 2.200 to the three decimals the sentence printed it to',
      abs(r2_u - 2.200) > 2e-3 and abs(r2_l - 2.200) > 2e-3)

_INSTR = paper_one(r'first-to-second height ratio of \$(2\.1969)\$', "the instrument's ratio")
_CAMB = paper_one(r"standard code's \$(2\.2043)\$", "the located standard-code figure")
_PCT = paper_one(r'agreement to \$(0\.34)\\%\$', 'the restated agreement')
_got = abs(_INSTR - r2_u) / r2_u * 100.0
print(f'    ⌈ the paper prints {_INSTR} against {_CAMB}, agreement {_PCT} per cent')
check(f'⓸ the agreement the sentence prints is what this receipt computes: {_got:.2f} per cent',
      abs(_CAMB - r2_u) < 5e-5 and abs(_PCT - round(_got, 2)) < 5e-3
      and abs(_got - 0.34) < 5e-3 and abs(_INSTR - 2.1969) < 5e-5)
check('   ⇒ and it is LARGER than the 0.14 the quoted figure gave, so replacing an unlocated number '
      'by a located one moves the agreement in the UNFAVOURABLE direction',
      _got > abs(_INSTR - 2.200) / 2.200 * 100.0)

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭ ** THE 2.200 WAS NEVER LOCATED.  CAMB at the same point through the same locator returns')
print('     2.2043 unlensed, and the agreement is 0.34 per cent -- larger than the 0.14 the quoted')
print('     figure gave, and the locator is confirmed by its returning C59\'s own 220 / 540 / 812. **')
sys.exit(0)
