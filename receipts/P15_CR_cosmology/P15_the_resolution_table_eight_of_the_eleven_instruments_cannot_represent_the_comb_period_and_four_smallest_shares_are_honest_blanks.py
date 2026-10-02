"""P15 -- THE RESOLUTION TABLE FOR `PO-56`'s ELEVEN INSTRUMENTS, BUILT ONCE AND IN ADVANCE (node 70, `r7029` item one).

** THE ROW HAS MET ONE INSTRUMENT LIMIT FOUR TIMES, EACH TIME AFTER A RESULT WAS STATED ON THE BANDED READING. **
This table is how a result meets its instrument's limit BEFORE it is stated.  For each of the eleven instruments
`cc66.62` enumerated, three columns:

  * the FINEST PERIOD it can resolve in q (comb period = 1.00), DERIVED from its own geometry on disk: the
    Nyquist period of its output sampling, and the transfer its averaging window imposes AT the comb period;
  * the SMALLEST SHARE it can detect, in its OWN units and under the noise model it ACTUALLY uses -- computed
    here where the model is the likelihood's covariance, quoted and text-gated where only `cc66`'s receipt
    derived it, and ** left BLANK WITH ITS REASON ** where it cannot be derived;
  * the CLASS OF FEATURE INVISIBLE TO IT -- the column the row keeps paying for.

** THE HEADLINE, DERIVED BELOW. **  Every banded instrument outputs one number per 0.70-wide band, so its output
series has a Nyquist period of 1.40: *** A MODULATION AT THE COMB PERIOD CANNOT BE REPRESENTED BY ANY OF THE
EIGHT, however it is aggregated *** -- and the boxcar a band applies passes only 0.37 of it before that.  The
likelihood bins at 0.030, a Nyquist period of 0.060 and a transfer of 0.9985 at the comb.  ** That single ratio
-- 1.40 against 0.060 -- is the four accidental discoveries, stated in advance. **

** THE BLANKS ARE FINDINGS, NOT GAPS. **  The contrast statistic, the bilinear decomposition and the
projection-width kernel carry NO statistical noise model -- their only scales are numerical or definitional
spreads, which are not detection floors.  The refit's floor cannot be derived because its inputs
(`/tmp/n66/...`) are not in the repository.  ⛔ *A guessed number in any of those cells would be worse than
the blank.*

⚠ ** SHARES IN DIFFERENT UNITS ARE NOT COMPARABLE. **  `cc66.61`'s 0.59 is a share of the STEP under an
empirical scatter of a noiseless spectrum; the likelihood's 0.055 is a share of the band-1 DIFFERENCE under
instrument noise.  The table sets them side by side and ranks neither against the other.

⛔ NOT CLAIMED: any statement about the physics, any channel or mechanism, any verdict on a result of `cc66`'s.
The table says what each instrument CAN see; it does not re-run or re-score what any of them DID see.
Nothing is solved; the only computation beyond geometry is the likelihood's per-band floor, on banks on disk.

Written r7029 by node 70.  Stated for reversal.
"""
import os
import re
import sys

import numpy as np
import scipy.linalg
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402

# ---------------------------------------------------------------------------- the sources it quotes
SRC = {
    'contrast':  'P15_the_acoustic_contrast_is_not_in_the_source_and_the_projection_makes_it_without_the_distance.py',
    'held':      'P15_the_surviving_step_is_amplitude_and_not_phase_and_the_candidate_shares_do_not_survive_the_change_of_denominator.py',
    'wfdepth':   'P15_the_step_is_the_excesss_own_and_it_sits_at_the_second_acoustic_peak_and_none_of_the_four_produces_it.py',
    'extremal':  'P15_the_window_free_reading_cannot_resolve_the_first_cycle_the_flatness_was_a_trend_and_nine_tenths_of_the_step_is_common_to_both_arms.py',
    'diff':      'P15_the_step_survives_a_differential_estimator_and_no_single_bilinear_term_carries_the_shared_step_though_the_doppler_leads_it.py',
    'srcdec':    'P15_the_cross_term_is_not_the_channel_and_every_projected_term_carries_the_excess.py',
    'phase':     'P15_no_statistic_this_construction_can_build_resolves_the_two_channels_and_the_phase_step_dies_on_a_matched_width_control.py',
    'kernel':    'P15_the_two_projection_widths_differ_by_the_jacobian_alone_and_the_channel_that_opens_is_a_quarter_of_the_excess.py',
    'locator':   'P15_the_contrast_excess_is_symmetric_about_the_envelope_and_the_troughs_are_where_the_sky_measures_it_best.py',
    'likelihood': 'P15_the_likelihood_sees_the_step_and_separates_the_two_channels_so_the_demonstration_does_not_cover_it.py',
    'refit':     'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase.py',
}
TXT = {}
for k, f in SRC.items():
    p = os.path.join(HERE, f)
    check(f"the source receipt for `{k}` is on disk", os.path.exists(p), f)
    TXT[k] = ' '.join(open(p, encoding='utf-8').read().split()) if os.path.exists(p) else ''
FOR66 = ' '.join(open(os.path.join(ROOT, 'FOR_66.md'), encoding='utf-8').read().split())
ENUM = ['the contrast statistic', 'the held-period amplitude', 'the window-free peak-to-trough depth',
        'the extremal envelope', 'the differential estimator', 'the bilinear decomposition `SRCDEC`',
        'the comb-phase projection', 'the projection-width kernel', 'the anchored peak/trough locator',
        '**`plik_lite` TT, the likelihood**', '**the refit $\\chi^2$ and its derivative grid**']
check("⛔ THE ELEVEN ARE `cc66.62`'s OWN ENUMERATION, not a list chosen here: every name is in `FOR_66.md`'s "
      "scope table", all(e in FOR66 for e in ENUM), f"{sum(e in FOR66 for e in ENUM)} of 11 found")
if FAILS:
    raise SystemExit(f"GATES: {len(FAILS)} FAILED before the table could be built")

# ---------------------------------------------------------------------------- the geometry, from disk
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
BW = float(np.median(np.diff(QE)))
check("the band edges are seven bands of 0.70", len(QE) == 8 and np.allclose(np.diff(QE), 0.70),
      f"edges {np.round(QE, 2).tolist()}")
fb = np.load(os.path.join(SP, 'r6941_fine_lcdm.npz'))
LS, DL, LA = fb['ls'].astype(float), np.asarray(fb['Dl'], float), float(fb['l_A'])
DQ_FINE = float(np.median(np.diff(LS))) / LA
LC, _ = CS.bin_center_and_fac()
MC = CS.bin_spectrum(LS, DL)
COVD = np.isfinite(MC)
WQ = float(np.median(((CS.BIN_HI - CS.BIN_LO + 1) / LA)[COVD]))
DQ8 = 8.0 / LA                                     # SRCDEC and the refit grid: ls step 8
EXT = np.sort(np.concatenate([argrelextrema(DL, np.greater, order=20)[0], argrelextrema(DL, np.less, order=20)[0]]))
QX = LS[EXT] / LA
DQX = float(np.median(np.diff(QX[(QX > QE[0]) & (QX < QE[-1])])))
NX1 = int(((QX >= QE[0]) & (QX < QE[1])).sum())
check("the extremum spacing -- what the window-free depth, the extremal envelope and the locator sample at -- is "
      "half a comb period", abs(DQX - 0.5) < 0.05, f"median {DQX:.3f} in q; {NX1} extremum inside band 1")


def sinc(w, p=1.0):
    """the transfer a boxcar of width w applies to a sinusoid of period p"""
    x = np.pi * w / p
    return abs(np.sin(x) / x)


print("\n" + "=" * 110)
print("  THE GEOMETRY EVERY ROW IS DERIVED FROM")
print("-" * 110)
print(f"    l_A (control) {LA:.3f};  fine bank dq {DQ_FINE:.5f};  step-8 grids dq {DQ8:.4f};  plik bin (median) "
      f"{WQ:.4f} = 1/{1 / WQ:.0f} of a period;  bands {BW:.2f};  extrema every {DQX:.3f}")
print(f"    boxcar transfer AT the comb period: band 0.70 -> {sinc(0.70):.3f};  held window 1.50 -> "
      f"{sinc(1.50):.3f};  locator +-40 ell ({80 / LA:.3f}) -> {sinc(80 / LA):.3f};  plik bin -> {sinc(WQ):.4f}")
check("⛭ THE HEADLINE: a band-per-number output has a Nyquist period of 1.40, so the comb period CANNOT be "
      "represented by any banded instrument; the likelihood's Nyquist period is 0.060",
      abs(2 * BW - 1.40) < 1e-9 and 2 * WQ < 0.07, f"banded {2 * BW:.2f} vs likelihood {2 * WQ:.3f}")
check("and before the output is sampled, a band's own boxcar passes only about a third of a comb-period "
      "modulation, where a likelihood bin passes all but a tenth of a per cent",
      sinc(0.70) < 0.40 and sinc(WQ) > 0.998, f"{sinc(0.70):.3f} vs {sinc(WQ):.4f}")

# ---------------------------------------------------------------------------- the likelihood's own floors
fl = np.load(os.path.join(SP, 'r6941_fine_cr.npz'))
MA = CS.bin_spectrum(fl['ls'].astype(float), np.asarray(fl['Dl'], float))
OK = np.isfinite(MC) & np.isfinite(MA)
for _fn in ('r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz'):
    _k = np.load(os.path.join(SP, _fn))
    OK &= np.isfinite(CS.bin_spectrum(_k['ls'].astype(float), np.asarray(_k['Dl'], float)))
QBIN = (LC / LA)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, ma, dat = MC[OK], MA[OK], CS.X_DATA[OK]
r = float((mc @ F @ dat) / (mc @ F @ mc)) * (ma - mc)


def band_S(lo, hi, v):
    m = (QBIN >= lo) & (QBIN < hi)
    c = COV[np.ix_(m, m)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(m.sum())))
    return float(np.sqrt(v[m] @ (0.5 * (f + f.T)) @ v[m])), int(m.sum())


SB = [band_S(a, b, r) for a, b in zip(QE[:-1], QE[1:])]
FLOORS = [2.0 / s for s, _ in SB]
check("the likelihood's band-1 floor REPRODUCES `cc66.62`'s: 2 / (band-1 sigma of the arm-control difference)",
      abs(SB[0][0] - 36.37) < 0.05 and abs(FLOORS[0] - 0.055) < 0.001,
      f"band-1 {SB[0][0]:.2f} sigma over {SB[0][1]} bins -> {FLOORS[0]:.4f}")
print("    likelihood smallest detectable share, per band (2 sigma of the band's arm-control difference): "
      + '  '.join(f'{x:.3f}' for x in FLOORS))

# ---------------------------------------------------------------------------- the quoted floors, text-gated
Q = {
    'contrast': 'floor is 0.6 per cent',
    'phase': '0.59',
    'locator_d': '0.0059', 'locator_h': '0.0114',
    'extremal_1363': '1.363', 'extremal_02': '0.02\\sigma',
}
check("every floor this table QUOTES is literally in the receipt that derived it",
      all([Q['contrast'] in TXT['contrast'], Q['phase'] in TXT['phase'], Q['locator_d'] in TXT['locator'],
           Q['locator_h'] in TXT['locator'], Q['extremal_1363'] in TXT['extremal'],
           Q['extremal_02'] in TXT['extremal']]),
      "0.6 per cent (cc66.40); 0.59 (cc66.61); 0.0059 / 0.0114 (cc66.46); 1.363 and 0.02 sigma (cc66.58)")
REFIT = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid', 'fit.py')
refit_src = open(REFIT, encoding='utf-8').read() if os.path.exists(REFIT) else ''
# ⛔⛭ FIXED AT r7099+cc66.82.  ** THE SECOND CLAUSE WAS `not os.path.exists('/tmp/n66')` -- a claim
# ** about the RUNNING MACHINE'S FILESYSTEM standing in for a claim about the REPOSITORY. **
# *`/tmp/n66` is this node's own scratch directory, so the check passed in CI (where it does not exist)
# and FAILED on `cc66`'s own machine whenever a run was in flight -- which is where it was first run,
# by `r7099`'s new `run_instrument_receipts.sh`.*
#   ⇒ *** The claim is "its inputs are not in the repository, so its floor cannot be re-derived here."
#     That is a property of the PATHS, not of what happens to be on disk: an absolute path under
#     `/tmp` cannot be a repository file, by construction.  Tested that way now, so it says the same
#     thing on every machine. ***
#   ⌗ *Fourth instance this round of a check asserting something adjacent to its subject rather than its
#   subject -- after `C41b`'s literal `8.2\%`, and `C63`'s and the one-fitted-number receipt's demands
#   for exact equality of a peak on a coarse grid.*
_tmp_inputs = re.findall(r"/tmp/[A-Za-z0-9_./-]+", refit_src)
check("⛔ THE REFIT'S BLANK IS FORCED, NOT CHOSEN: its fit reads inputs under /tmp that CANNOT be "
      "repository files -- an absolute path outside the tree -- so its floor cannot be re-derived here",
      bool(_tmp_inputs) and all(not p.startswith(ROOT) for p in _tmp_inputs),
      f"fit.py reads {len(_tmp_inputs)} path(s) under /tmp, none inside the repository: "
      f"{sorted(set(_tmp_inputs))[:3]}")
# ⚠ found by this gate's first version, which read "no covariance anywhere" and FAILED: the contrast receipt
#   does read COV_TT -- once, as `FISH`, the weight of the amplitude fit `fit4` that puts each spectrum on the
#   data's scale.  That is a FITTING WEIGHT, not a noise model: nothing is drawn from it and nothing is
#   propagated through it into the statistic.  So the claim is narrowed to what is true and gated as such.
NOISE = r'multivariate_normal|standard_normal|cholesky|default_rng|random\.|np\.random'
check("⛔ AND THE THREE NO-NOISE BLANKS ARE THE SOURCES' OWN: none of the three draws a noise realisation or "
      "propagates a covariance into its statistic -- no Monte Carlo, no random draw, in any of them",
      all(not re.search(NOISE, TXT[k]) for k in ('contrast', 'srcdec', 'kernel')),
      "no noise draw in any of the three")
check("⌗ and the ONE covariance any of them reads is the contrast receipt's amplitude-fit weight, used once to "
      "put a spectrum on the data's scale and never to put an error on the statistic",
      TXT['contrast'].count('COV_TT') == 1 and 'FISH = np.linalg.inv(CS.COV_TT' in TXT['contrast']
      and all('COV_TT' not in TXT[k] for k in ('srcdec', 'kernel')),
      "contrast: FISH in fit4 only; SRCDEC and the kernel: none")

# ---------------------------------------------------------------------------- the table
B = 2 * BW
TABLE = [
    ("1  the contrast statistic (r6911+cc66.40)",
     f"{B:.2f} as banded (Nyquist of 0.70 bands; boxcar passes {sinc(0.70):.2f} at 1.00); ORIGINALLY one "
     "regression over 0.85-5.75 -- no period at all",
     "BLANK: no noise model. Its 0.6 per cent is a NUMERICAL floor (self-null, round trips, injection), not a "
     "detection floor; the covariance it reads is only the weight of an amplitude fit",
     "anything finer than 1.40, including a comb-period modulation of the contrast; the overall level (osc is "
     "normalised by a 1.0-wide running envelope); sign and phase inside a band (a std)"),
    ("2  the held-period amplitude (cc66.60)",
     f"1.50 (its +-0.75 fit window; boxcar passes {sinc(1.50):.2f} at 1.00), and {B:.2f} once banded",
     "0.59 of the STEP (cc66.61's floor; this is the route that attains it), under an EMPIRICAL scatter of a "
     "noiseless spectrum",
     "amplitude structure narrower than 1.5; any oscillation at a period other than 1.00 (the fit fixes it); "
     "anything a quadratic baseline absorbs"),
    ("3  the window-free peak-to-trough depth (cc66.57)",
     f"1.00 as a datum series (one datum per half cycle, every {DQX:.2f} -- the comb period sits AT Nyquist), "
     f"{B:.2f} banded",
     f"band 1 holds {NX1} extremum and cc66.58 reads ONE transition there: 0.02 sigma from zero and 1.60 from "
     "the rest -- informative about neither. No band-1 floor can be formed from one datum",
     "everything between extrema; any envelope variation at period 1.00 or finer; band 1 in all but name"),
    ("4  the extremal envelope (cc66.58)",
     f"1.00 as an interpolated envelope (extrema every {DQX:.2f}), {B:.2f} banded",
     "undefined below q = 1.363, its first extremum pair: it covers 27 per cent of band 1 and interpolates "
     "ACROSS the step there",
     "73 per cent of band 1; structure between extrema, which it interpolates over"),
    ("5  the differential estimator (cc66.59)",
     f"{B:.2f} (band std of the arm/control ratio; boxcar passes {sinc(0.70):.2f} at 1.00)",
     "no better than 0.59 of the STEP: cc66.61 minimised the floor over this family's routes and the held "
     "amplitude attained it",
     "anything finer than 1.40; a raw band std samples 0.70 of a cycle, so amplitude and phase mix (cc66.60's "
     "correction to cc66.59)"),
    ("6  the bilinear decomposition SRCDEC (r6915+cc66.41)",
     f"{2 * DQ8:.3f} intrinsically (per multipole at step 8), but {B:.2f} AS READ -- every claim on it went "
     "through the band statistic",
     "BLANK: no noise model. Its cross-term span across windows is a definitional spread, not a floor",
     "as read: anything finer than 1.40; per-term cancellation inside a band"),
    ("7  the comb-phase projection (cc66.61)",
     f"{B:.2f} with its 0.70 stretches, 2.00 with its 1.00 stretches -- and ONLY at period 1.00 (it projects "
     "there and nowhere else)",
     "2 x its matched-width scatter = 0.015 rad at a 0.70 stretch (band 1 sits 1.52 scatters out); 0.002 rad "
     "over the whole upper range. Phase, not a share",
     "phase change inside a stretch; everything at a period other than 1.00; amplitude (it returns phase only)"),
    ("8  the projection-width kernel (cc66.52)",
     f"{B:.2f} (21 points averaged per band)",
     "BLANK: no noise model. The mean-vs-peak anchor spread (and its sign change) is the only scale it has",
     "anything finer than 1.40; its own sign, which depends on the anchor"),
    ("9  the anchored peak/trough locator (cc66.45/46)",
     f"positions: to a few hundredths of ell; amplitude: the +-40 ell window ({80 / LA:.3f} in q, passes "
     f"{sinc(80 / LA):.2f} at 1.00), BUT the depth it reports is a mean over three troughs spanning q 1.3-3.3",
     "2 x its COV_TT Monte Carlo spread: 0.012 on depth, 0.023 on height -- instrument noise",
     "amplitude at band 1 specifically (its first trough anchor sits inside band 1 and is averaged with two "
     "outside); everything away from an extremum"),
    ("10 plik_lite TT, the likelihood",
     f"{2 * WQ:.3f} (bins of {WQ:.4f}; a bin passes {sinc(WQ):.4f} at 1.00)",
     "per band, 2 sigma of the band's arm-control difference: " + ', '.join(f'{x:.3f}' for x in FLOORS)
     + " -- instrument noise (COV_TT)",
     "structure narrower than one bin (9 ell); a uniform rescaling (its fitted amplitude absorbs it); and "
     "LOCATION OF REJECTION versus separating power -- a band's sigma is not its share of the chi2 excess "
     "unless the exact d'F(d - 2r) split is used (cc66.63, cc66.64)"),
    ("11 the refit chi2 and its derivative grid (r6788+cc66.18)",
     f"{2 * WQ:.3f} (the likelihood's bins), on spectra sampled every {DQ8:.4f}",
     "BLANK: cannot be derived here -- its fit reads /tmp/n66 inputs not in the repository",
     "anything degenerate with its four parameter derivatives and the amplitude (fitted away); response "
     "beyond quadratic; off-diagonal curvature (not modelled)"),
]
print("\n" + "=" * 110)
print("  THE TABLE")
print("=" * 110)
for name, per, share, inv in TABLE:
    print(f"\n  {name}\n    finest period : {per}\n    smallest share: {share}\n    invisible     : {inv}")
check("⛭ THE TABLE HAS ELEVEN ROWS AND EVERY ROW HAS ALL THREE COLUMNS FILLED -- a blank is filled WITH ITS "
      "REASON, never left empty", len(TABLE) == 11 and all(all(len(c) > 20 for c in row) for row in TABLE),
      "11 x 3")
NBLANK = sum(row[2].startswith('BLANK') for row in TABLE)
check("⛔ FOUR SMALLEST-SHARE CELLS ARE HONEST BLANKS -- three for want of any noise model and one for want "
      "of its inputs -- and none is filled with a guess", NBLANK == 4, f"{NBLANK} blanks")
NBAND = sum(f"{B:.2f}" in row[1] for row in TABLE)
check("⛭ AND THE ROW'S FOUR ACCIDENTAL DISCOVERIES ARE ONE LINE OF THIS TABLE: every instrument whose finest "
      "period is 1.40 or coarser cannot see a comb-period feature, and they are the eight `cc66.62` found band",
      NBAND >= 8, f"{NBAND} rows carry the 1.40 banded limit")

print("\n" + "=" * 110)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
