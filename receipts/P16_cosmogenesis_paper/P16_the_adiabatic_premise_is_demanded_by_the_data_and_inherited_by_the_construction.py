#!/usr/bin/env python3
"""
RECEIPT -- P16: ** ITEM 56 WORKED.  cc54's NUMBER REPRODUCED INDEPENDENTLY ON THIS LINE'S INSTRUMENT,
AND THE PREMISE ITEM 32 NAMED AS UNSTATED HAS TWO SUPPORTS RATHER THAN NONE: THE DATA DEMAND IT AT
Delta chi^2 ~ 3e5, AND THE CONSTRUCTION INHERITS IT RATHER THAN SEEDING IT. **

Built r2552+c54.206, lead `L-528`.  VEIN: `L-202` (what the seam carries).

===================================================================================================
** THE SEQUENCE, BECAUSE IT IS THE POINT AS MUCH AS THE NUMBER IS **
===================================================================================================

  * ** item 32 ** -- the progenitor-composition derivation rests on ADIABATICITY and never said so.
    Applied at c54.204: the algebra named where the derivation is made.
  * ** 54 then named the generator ** -- the CMB literature's standard objection to any
    non-inflationary coherence mechanism is the ISOCURVATURE bound, and item 32 had just made the
    corpus's premise explicit, so the field's standard question and a premise the corpus now names
    were the same object.
  * ** cc54 computed it ** (r2549).  ** This file reproduces it, independently, on 54's own
    instrument path ** -- and that matters because the number is the whole item.

===================================================================================================
** PART 1 -- THE PEAKS, FROM A BOLTZMANN CODE ON ONE COSMOLOGY AND TWO INITIAL CONDITIONS **
===================================================================================================

  ** adiabatic              ell_1 = 220 **  (and 536, 813, 1126)
  ** pure CDM isocurvature  ell_1 = 294 **
  *** displacement +74, and it is the sin-against-cos phase of the acoustic oscillation. ***

  ⌗ *cc54 reports 220 and 294.  ** This line ran CAMB itself, from a fresh parameter set, and gets
  the same two integers. **  Two nodes, one number.*

===================================================================================================
** PART 2 -- AND THE LIKELIHOOD, ON THE CORPUS'S OWN plik_lite PATH **
===================================================================================================

  ** adiabatic              chi^2 =    206 over 215 bins  (chi^2/dof = 0.96) **
  ** pure CDM isocurvature  chi^2 = 327150 over 215 bins **
  *** Delta chi^2 = 3.3e5. ***

⚠ ** AND THE AMPLITUDE IS FITTED IN CLOSED FORM IN BOTH CASES, WHICH IS THE PART THAT MATTERS. **
The instrument solves A = (m^T F d)/(m^T F m) at every evaluation, so ** the isocurvature figure is
already amplitude-marginalised **.  *The obvious objection -- "rescale it" -- is not answered by this
file; it is pre-empted by the instrument, because the peaks are in the wrong PLACE and no scaling
moves a peak.*

===================================================================================================
** ⛭⛭ PART 3 -- AND THE DISARMING MOVE WAS ALREADY IN P16, VERBATIM **
===================================================================================================

P16, two sentences above the one this revision replaces: *"the progenitor ... is an overdensity in a
universe like this one, so what it carries into collapse is a nearly scale-invariant adiabatic
spectrum processed by ordinary structure formation -- ** a fully specified input, available from
standard cosmology, and not an idealisation to be chosen **."*

  ⇒ *** The standard objection kills mechanisms that SEED isocurvature.  This construction does not
      seed a spectrum; it INHERITS one.  So the objection does not reach it -- and that is a
      different thing from answering it. ***

  ⌗ ** So the premise has two independent supports and the paper stated neither beside the
    objection: ** the DATA demand it, and the CONSTRUCTION inherits it.

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that the framework PREDICTS adiabaticity ** -- it inherits it, which is weaker and is the
point, and the written paragraph says so in the paper's own voice.  ** Not that this bears on
`PO-7` ** -- that is a separate measurement on a different instrument and is untouched.  ** `F1`
untouched. **  ** And not that a pure-isocurvature universe is the only alternative **: the bound
quoted for admixtures is Planck's, cited as theirs, and is not computed here.

⌗ *The sentence this replaces -- "this paper draws no bound from it in either direction" -- ** was
correct when written **.  It is replaced because a bound now exists, not because it was wrong.*

SETTINGS: CAMB 2.0.1 at the Planck 2018 base cosmology (H0 = 67.36, ombh2 = 0.02237, omch2 = 0.1200,
tau = 0.0544, As = 2.1e-9, ns = 0.9649), lmax 2500 with lensing; scored on the corpus's own
`chi2_of_spectrum` over the full 215 plik_lite TT bins.  ** The only thing varied between the two runs
is `scalar_initial_condition`. **

rc=0 on success.  Run: python3 P16_the_adiabatic_premise_is_demanded_by_the_data_and_inherited_by_the_construction.py
                        (camb numpy scipy; ~4 min)
LEVEL: NO RATE -- this receipt uses no expansion rate at all, so no level applies.  Recorded
  rather than left blank, so a later reader does not have to re-derive the absence.
"""
import os
import re
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                                # noqa: E402

fail = []
LMAX_SCORE = 2600.0


def spectrum(ic):
    p = camb.CAMBparams()
    p.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544)
    p.InitPower.set_params(As=2.1e-9, ns=0.9649)
    p.set_for_lmax(2500, lens_potential_accuracy=1)
    p.scalar_initial_condition = ic
    res = camb.get_results(p)
    D = res.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total'][:, 0]
    return np.arange(D.shape[0], dtype=float), D


def peaks(ls, D):
    m = (ls >= 30) & (ls <= 2000)
    return ls[m][argrelextrema(D[m], np.greater, order=12)[0]]


# =====================================================================
print("=" * 78)
print("PART 1 — ONE COSMOLOGY, TWO INITIAL CONDITIONS, AND ONLY THE MODE CHANGED")
print("=" * 78)
RES = {}
for ic, nm in (('initial_adiabatic', 'adiabatic'), ('initial_iso_CDM', 'pure CDM isocurvature')):
    ls, D = spectrum(ic)
    pk = peaks(ls, D)
    c = CS.chi2_of(ls, D, lmax=LMAX_SCORE)
    RES[nm] = dict(ls=ls, D=D, pk=pk, chi2=c[0], nbin=c[1])
    print(f"  {nm:>24s}  first peaks: {[int(x) for x in pk[:4]]}")
_l1a = int(RES['adiabatic']['pk'][0])
_l1i = int(RES['pure CDM isocurvature']['pk'][0])
print()
print(f"  ** first peak {_l1a} -> {_l1i}, displacement {_l1i - _l1a:+d} **   "
      f"— the sin-against-cos acoustic phase")
print("  *cc54 reports 220 and 294.  This line ran the code itself, from a fresh parameter set.*")
if _l1a != 220:
    fail.append(f"the adiabatic first peak is {_l1a}, not the sky's 220 — the baseline is wrong")
if not (280 <= _l1i <= 310):
    fail.append(f"the isocurvature first peak is {_l1i}, outside cc54's reported 294")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE LIKELIHOOD, WITH THE AMPLITUDE FITTED IN CLOSED FORM IN BOTH CASES")
print("=" * 78)
for nm in ('adiabatic', 'pure CDM isocurvature'):
    r = RES[nm]
    print(f"  {nm:>24s}  chi^2 = {r['chi2']:12.1f}  over {r['nbin']} bins   "
          f"chi^2/dof = {r['chi2'] / r['nbin']:.2f}")
_d = RES['pure CDM isocurvature']['chi2'] - RES['adiabatic']['chi2']
print()
print(f"  ** Delta chi^2 = {_d:,.0f}  ({_d:.1e}) **")
print("  ⚠ *The instrument solves A = (m^T F d)/(m^T F m) at every evaluation, so the isocurvature")
print("     figure is ALREADY amplitude-marginalised.  The 'rescale it' objection is pre-empted by")
print("     the instrument rather than answered by this file: no scaling moves a peak.*")
_amp_fit = 'm^T F d' in open(os.path.join(ROOT, 'computations', 'planck_tt_likelihood',
                                          'chi2_of_spectrum.py'), encoding='utf-8').read()
print(f"  closed-form amplitude fit present in the instrument's own header: {_amp_fit}")
if not _amp_fit:
    fail.append("the instrument does not document a closed-form amplitude fit — then PART 2's "
                "pre-emption of the rescaling objection is not established")
if _d < 1e5:
    fail.append(f"Delta chi^2 is {_d:.3g}, below the 1e5 the item rests on")
if RES['adiabatic']['chi2'] / RES['adiabatic']['nbin'] > 1.2:
    fail.append("the adiabatic baseline does not fit — the comparison has no validated arm")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE DISARMING MOVE WAS ALREADY IN P16, VERBATIM")
print("=" * 78)
P16 = open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'), encoding='utf-8').read()
CHECKS = [
    ("P16 already says the progenitor carries a nearly scale-invariant ADIABATIC spectrum",
     r'nearly scale-invariant adiabatic spectrum processed by ordinary structure formation'),
    ("and calls it a fully specified input rather than an idealisation to be chosen",
     r'a fully specified input, available from standard cosmology, and not an idealisation to be chosen'),
    ("the replaced sentence is gone", None),
    ("the number is now in the paper", r'\\chi\^\{2\}=3\.3\\times10\^\{5\}'),
    ("with the amplitude fit stated so the rescaling objection is visibly pre-empted",
     r'amplitude is fitted in closed form in both cases'),
    ("and the inherit-not-predict limit stated in the paper's own voice",
     r'not claimed is\s*\n?that the framework predicts adiabaticity'),
]
for what, pat in CHECKS:
    if pat is None:
        ok = 'draws no bound from it in either direction' not in P16
    else:
        ok = re.search(pat, P16, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P16 check failed: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the adiabatic first peak is the sky's 220 and the isocurvature one 294 on the")
print("same cosmology; the likelihood separates them by 3e5 with the amplitude fitted in closed form,")
print("so no rescaling closes it; and P16 already carried the sentence that puts the standard objection")
print("outside this construction's reach, two sentences above the one it can now replace.")
print("=" * 78)

# ============================================================================================
# GATE — r2552+c54.206, `L-528`.  The item IS the number, so this file's job is to be a second
# instrument on it rather than a restatement:
#   (1) the adiabatic first peak asserted at exactly 220 -- ** the validated baseline.  If this arm
#       did not land on the sky's value, the comparison would have no calibrated side and the
#       isocurvature figure would mean nothing **;
#   (2) the isocurvature first peak asserted in cc54's reported band -- ** this is the
#       reproduction, and it is the reason to run it at all **;
#   (3) Delta chi^2 asserted above 1e5, and the adiabatic arm asserted to FIT (chi^2/dof < 1.2) --
#       both, because a huge separation from an unfitting baseline is not a bound;
#   (4) the closed-form amplitude fit asserted present in the instrument, ** without which the
#       'just rescale it' objection stands and the number does not carry what the paragraph says **;
#   (5) and P16's prior sentence asserted present plus the replaced one asserted GONE -- the
#       disarming move must be the paper's own, not this file's.
#   NOT gated: Planck's beta_iso bound, which is cited as theirs and not computed here.
# ============================================================================================
assert _l1a == 220, f"the adiabatic baseline peaks at {_l1a}, not 220"
assert 280 <= _l1i <= 310, f"the isocurvature peak is {_l1i}, outside the reproduced band"
assert _d > 1e5, f"Delta chi^2 is only {_d:.3g}"
assert RES['adiabatic']['chi2'] / RES['adiabatic']['nbin'] < 1.2, "the adiabatic arm does not fit"
assert _amp_fit, "no closed-form amplitude fit in the instrument"
assert 'draws no bound from it in either direction' not in P16, "the replaced sentence is still there"
assert re.search(r'nearly scale-invariant adiabatic spectrum processed by ordinary structure formation',
                 P16), "P16 no longer carries the inherit-not-seed sentence"
print(f"GATE c54.206 (r2552), `L-528`: adiabatic ell_1 = {_l1a} and isocurvature ell_1 = {_l1i} on one "
      f"cosmology; chi^2 = {RES['adiabatic']['chi2']:.0f} against "
      f"{RES['pure CDM isocurvature']['chi2']:.0f} over {RES['adiabatic']['nbin']} plik_lite bins with "
      f"the amplitude fitted in closed form, so Delta chi^2 = {_d:.2e} and no rescaling closes it — "
      f"cc54's r2549 numbers reproduced on this line's own instrument path, pinned against `FOR_54` "
      f"item 56 and item 32's named premise.")
