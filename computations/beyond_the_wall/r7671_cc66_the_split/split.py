#!/usr/bin/env python3
"""r7671 (cc66) -- THE RE-GROUND / REBUILD SPLIT ON PO-87's THIRTY, READ PER SENTENCE.

** THE ORDER (r7671, 69) item 1: ** "Finish the split ... Classify each as RE-GROUND or REBUILD,
with the reason taken from the sentence."  Items 3-4 route the RE-GROUND sentences to 69 in ONE
batch and the REBUILD list to 70 as spectrum paths with their configurations.

** THE DEFINITIONS ARE r7669's, VERBATIM, AND THEY ARE NOT MINE TO WIDEN. **
  RE-GROUND -- "the sentence is legitimately about the namesake or superseded configuration, or its
               claim does not depend on which arm it was read on."
  REBUILD   -- "the sentence's claim is about the arm of record and needs its figure from an
               arm-of-record spectrum."
  and item 3's standing bar: "do not count a control-only read as REBUILD until [70] reports."

⛔ ** WHAT THIS FILE IS, AND WHAT IT IS NOT. **  The verdicts below are a READING, declared by this
seat.  No regex produced them -- a regex over the sentence's words is the cheap signal that has
failed six times in four revisions and `ITEM2_TRIAGE.md` says so in its own header.  What the gates
assert is therefore not the reading but its DISCIPLINE:
  Ⓐ①  every one of the thirty has exactly one verdict, and no item outside the thirty has one;
  Ⓐ②  no item whose every remaining namesake read is a CONTROL leg is called REBUILD;
  Ⓐ③  every reason's anchor is a VERBATIM fragment of that item's own precise sentence;
  Ⓐ④  every declared spectrum path exists on disk, or is declared absent;
  Ⓐ⑤  every item declared CONTROL-READ has an arm-of-record read in its live source, and every
       item declared NAMESAKE-READ has none -- so the declaration is checked against the receipt.
⇒ A verdict I invented would fail Ⓐ③; a verdict whose load story I got backwards fails Ⓐ⑤.

** THE STRUCTURAL FINDING THIS READING PRODUCED, which the order does not anticipate. **  r7635 and
r7643 moved each receipt's CR legs onto the arm of record and left the CONTROL legs where they were,
because -- by `r7669`'s own measurement -- NO arm-of-record grid carries a control leg, in any of
four families.  ⇒ So a large part of PO-87's list is not a rebuild backlog at all: it is the control
side of two-arm reads, whose fate 70's measurement of whether LEAFREC reaches the control decides
in one stroke.  That is counted below rather than asserted.

Registered at PREDICTION.md in this directory, in its own commit (`r7671+cc66.3`), pushed before a
line of this file existed.
"""
import collections
import contextlib
import importlib.util
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


def _load(name, path):
    """import an instrument without re-printing it, and WITHOUT swallowing its verdict."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    green = True
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            spec.loader.exec_module(mod)
        except SystemExit:
            green = False
    return mod, green


CEN, CEN_OK = _load('census_r7667', os.path.join(BW, 'r7667_cc66_po87_the_unfiltered_list',
                                                 'census.py'))
CLS, CLS_OK = _load('classify_r7669', os.path.join(BW, 'r7669_cc66_reading_the_undecidable',
                                                   'classify.py'))
sys.path.insert(0, os.path.join(BW, 'r7667_cc66_po87_the_unfiltered_list'))
from sentence import sentences_citing            # noqa: E402

BODY = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
_NUM = re.compile(r'\d+\.\d+|\b\d{2,}\b')

#: the four verdicts, and what each one MEANS for the two routings
REGROUND = 'RE-GROUND'      # -> 69, with a proposed wording
REBUILD = 'REBUILD'         # -> 70, with spectrum paths and configurations
HELD = 'HELD'               # -> nobody yet: the order's item 3 bar, 70's measurement decides

#: ** THE READING. **  key = the receipt's base name.
#:   verdict   -- one of the three above
#:   why       -- 'ctrl-read'  a TWO-ARM receipt whose CR legs moved to the arm of record, leaving
#:                              the control leg as its only namesake read (Ⓐ② applies)
#:                'ctrl-only'  the receipt reads NOTHING BUT control spectra -- no arm leg to move
#:                'ctrl-figure' the sentence's own printed figures are all the control's
#:                'namesake-pin' the receipt pins the namesake DELIBERATELY and says so
#:                'method'     the claim is a method or instrument property, arm-independent
#:                'arm-figure' the sentence prints a figure of THIS arm off a namesake
#:   anchor    -- a VERBATIM fragment of the item's own precise sentence (Ⓐ③)
#:   traced    -- True only where the printed figure is followed THROUGH the receipt to a
#:                namesake load.  False where the receipt's arm legs are already arm-of-record
#:                and the namesake read is an auxiliary -- ** the receipt-level limit named at
#:                r7669, not a verdict dressed as a measurement. **
#:   spectra   -- for REBUILD: the namesake spectra, relative to the repo root
V = {
 'P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_at_the_visibility': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor='which on this arm runs $0.789$ to $0.913$',
    reason='the Jacobian in print is this arm\'s and is the LEAFREC quantity itself: the sentence '
           'gives d(eta_leaf)/d(eta_stack) running 0.789 to 0.913 on this arm against identically '
           'one on the control, and the receipt reads every leg -- injected, geometry, noop, '
           'source, screen -- on the namesake side with no `_leafrec1` anywhere in its live source',
    spectra=['computations/beyond_the_wall/spectra/r6919_injected_cr.npz',
             'computations/beyond_the_wall/spectra/r6919_geometry.npz',
             'computations/beyond_the_wall/spectra/r6919_noop.npz',
             'computations/beyond_the_wall/spectra/r6911_source_cr.npz',
             'computations/beyond_the_wall/spectra/r6893_switch_screen_cr.npz']),
 'P15_derived_lensing_on_the_lcdm_arm': dict(
    verdict=HELD, why='ctrl-only', traced=True,
    anchor='about $989$ of the $1320$ survives it',
    reason='the one spectrum it reads is the control leg `c54.178_lcdm.npz`, and `r7669`\'s item 4 '
           'already measured that `c54.178_lcdm_leafrec1.npz` does not exist -- so there is nothing '
           'to rebuild it against and 70\'s measurement decides whether anything needs to be',
    spectra=['computations/beyond_the_wall/spectra/c54.178_lcdm.npz']),
 'P15_the_1p57_has_no_parameter_address_because_the_arms_tt_minimum_sits_on_its_own_bao_minimum_while_the_controls_pays_fifteen_in_chi2_to_leave_planck': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='the control settles at $1.01$ in $\\chi^{2}$ per bin',
    reason='the arm\'s verification point is read from `cc66_r185_verify_cr_leafrec1.npz`, named in '
           'the receipt\'s own `ARMNPZ`; the only namesake read left is `refit_grid185/verify_lcdm'
           '.npz`, the control leg, which no arm-of-record grid carries',
    spectra=['computations/beyond_the_wall/refit_grid185/verify_lcdm.npz']),
 'P15_the_acceptance_does_not_move_under_refinement_and_three_of_the_twelve_axes_could_not_have_moved_it': dict(
    verdict=REGROUND, why='method', traced=False,
    anchor="a wider $\\chi$-extent narrows the kernel's acceptance in wavenumber",
    reason='the clause this receipt carries is the law\'s physical reading and its stability under '
           'refinement -- a property of the kernel\'s acceptance integral, which the sentence '
           'states without reference to an arm. The four `r7041_accept_*` digests it reads carry no '
           'arm in their names and no `_leafrec1` counterpart was ever built for any of them',
    spectra=[]),
 'P15_the_acoustic_contrast_is_not_in_the_source_and_the_projection_makes_it_without_the_distance': dict(
    verdict=REBUILD, why='arm-figure', traced=False,
    anchor="this arm retaining $1.054$ times as much of its own source oscillation as the control does",
    reason='the retention ratio in print is this arm\'s. ⚠ UNTRACED: the receipt\'s source and '
           'verification legs are already arm-of-record (`_SRC[cr]`, `_VER[cr]`), so the two '
           'namesake reads that remain -- the no-physics projection and the screened switch -- may '
           'be auxiliaries rather than the figure\'s source. 70 should price them, not assume them',
    spectra=['computations/beyond_the_wall/spectra/r6911_noop.npz',
             'computations/beyond_the_wall/spectra/r6893_switch_screen_cr.npz']),
 'P15_the_contrast_excess_is_symmetric_about_the_envelope_and_the_troughs_are_where_the_sky_measures_it_best': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='the control lands on the measured trough depths at five hundredths of a standard deviation',
    reason='every figure-bearing CR leg moved: `r6941_fine_cr_leafrec1`, `r6929_scan_cr_leafrec1`, '
           '`r6929_geometry_leafrec1`. The two namesake CR files it still opens are declared gates '
           '-- `r6929_geometry.npz` "read ONLY to gate the convention" and `r6941_fine_cr.npz` read '
           'to measure the provenance -- so the only namesake FIGURE read is the control\'s fine bank',
    spectra=['computations/beyond_the_wall/spectra/r6941_fine_lcdm.npz']),
 'P15_the_control_entered_the_regime_and_the_arm_did_not_move': dict(
    verdict=HELD, why='ctrl-figure', traced=True,
    anchor="it was $78\\%$ of the control's remaining $\\chi^{2}$",
    reason='all three figures the sentence prints are the control\'s -- 78 per cent of the '
           'control\'s remaining chi^2, the control at 1.18 per degree of freedom, a reference 1.01 '
           '-- so whether the sentence needs an arm-of-record figure at all is 70\'s question. '
           '⚠ And `c54.178` and `c54.186` are both among the twelve today\'s instrument aborts on, '
           'so a rebuild has no path even if 70 says the switch reaches the control',
    spectra=['computations/beyond_the_wall/spectra/c54.178_lcdm.npz',
             'computations/beyond_the_wall/spectra/c54.186_lcdm_L3000.npz']),
 'P15_the_controls_base_log_is_banked_beside_the_grids_and_the_peak_heights_concur_with_the_three_rigidity_statistics': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor="$\\chi^{2}=186.135$, level with the control's own value",
    reason='the three rigidity statistics in print -- chi^2 186.135, 87 sign changes, a longest run '
           'of 8 -- are read off the three namesake CR grids in the receipt\'s own `GRIDS` table, '
           'and the sentence attributes them to the leaf-rate rebuild. Each of the three grids has '
           'a `_leafrec1` sibling carrying `cr_base.npz`, so this one repoints',
    spectra=['computations/beyond_the_wall/refit_grid185/cr_base.npz',
             'computations/beyond_the_wall/r7095_directions/grid_licensed/cr_base.npz',
             'computations/beyond_the_wall/r7093_directions/grid_oneclock/cr_base.npz']),
 'P15_the_cross_term_is_not_the_channel_and_every_projected_term_carries_the_excess': dict(
    verdict=REBUILD, why='arm-figure', traced=False,
    anchor='$1.017$ with a spread of $0.010$',
    reason='the intercept and spread in print are measured across this arm\'s twelve settings. '
           '⚠ UNTRACED for the same reason as the contrast receipt: `_PAIRS[cr]` and `_SRC[cr]` are '
           'already arm-of-record, so the namesake reads left are the no-physics pair and the '
           'screened switch',
    spectra=['computations/beyond_the_wall/spectra/r6915_noop.npz',
             'computations/beyond_the_wall/spectra/r6893_switch_screen_cr.npz']),
 'P15_the_de_tilted_peak_set_is_the_phase_observable_the_slope_was_not_and_it_separates_the_baryon_direction_from_a_tilt_by_twenty_but_the_driving_half_needs_its_own_pair': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='$11.7$ and $18.3$ on this arm and $11.4$ and $22.6$ on the control',
    reason='the receipt separates the arms by directory and by file -- `GO[cr]` and `GL[cr]` are the '
           '`_leafrec1` grids and its driving pair is `c54.186_cr_L3000_leafrec1` -- so this arm\'s '
           'factors are already arm-of-record and the control\'s are the namesake read',
    spectra=['computations/beyond_the_wall/r7093_directions/grid_oneclock/lcdm_base.npz',
             'computations/beyond_the_wall/spectra/c54.186_lcdm_L3000.npz',
             'computations/beyond_the_wall/spectra/c54.193_lcdm_nodrive_L3000.npz']),
 'P15_the_fit_has_the_controls_freedom_and_the_contrast_the_data_ask_for_lies_outside_every_direction_it_has': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor="while the control's $87$ sits inside one standard deviation of it",
    reason='`_grid_for(tag)` sends every `cr*` leg to `refit_grid185_leafrec1` and the control to '
           '`refit_grid185`, and the receipt\'s own comment says why: the arm-of-record grid has no '
           '`lcdm_base.npz` to read. ⌗ Its other namesake token, `cc66_lens_ratio.npz`, is not in '
           'this checkout at all and the live branch is the registered CAMB fallback at the '
           'control\'s parameters, imposed on both arms alike -- so it is not a namesake dependency',
    spectra=['computations/beyond_the_wall/refit_grid185/lcdm_base.npz']),
 'P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma': dict(
    verdict=HELD, why='ctrl-only', traced=True,
    anchor='seven tenths at $1.0926$',
    reason='the one spectrum it reads is the control leg `L820_lcdm_L2512_nk800.npz`. ⌗ The '
           'sentence\'s own claim -- "a property of the shapes and not of the size" -- reads as '
           'arm-independent on its face, so this one may well leave the list outright once 70 '
           'reports; that is not called here',
    spectra=['computations/beyond_the_wall/spectra/L820_lcdm_L2512_nk800.npz']),
 'P15_the_kernels_phase_difference_between_the_arms_is_four_orders_below_the_residual_so_the_projection_is_cleared_and_a_fifth_of_the_scale_is_common_mode': dict(
    verdict=REGROUND, why='method', traced=False,
    anchor="the instrument's own documented aliasing failure",
    reason='the figure in print -- a difference 74 times the true one at under two points per '
           'Bessel period -- is an ALIASING ARTEFACT of the Bessel route against the window route, '
           'which the sentence names as such. An instrument\'s sampling failure is the same on '
           'either arm, so no re-derivation on the arm of record moves it',
    spectra=[]),
 'P15_the_licensed_configuration_moves_neither_statistic_and_the_swing_was_read_above_where_it_converges': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor="the specified configuration's run grows $9$, $9$, $9$, $16$",
    reason='the run lengths at four reading ceilings are computed in PART B off `cr_base.npz` in '
           'the three NAMESAKE grid directories `refit_grid185`, `grid_licensed` and '
           '`grid_oneclock` -- the receipt\'s `BANKED`/`LICENSED`/`ONECLOCK` constants -- and the '
           'sentence reports them as the configurations\' own. All three have `_leafrec1` siblings',
    spectra=['computations/beyond_the_wall/refit_grid185/cr_base.npz',
             'computations/beyond_the_wall/r7095_directions/grid_licensed/cr_base.npz',
             'computations/beyond_the_wall/r7093_directions/grid_oneclock/cr_base.npz']),
 'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor='$\\approx0.487$, $0.435$, $0.359$ and $0.666$ of the flat-$\\Lambda$CDM expectation',
    reason='the four deficits in print are this construction\'s own low-multipole floor and come '
           'straight out of `cc66_lowell_sweep.npz`, the receipt\'s single spectrum read. ⚠ But the '
           'sweep has NO `_leafrec1` sibling and its keys carry no LEAFREC dimension at all '
           '(FROZEN/DECOUPLED x control/adjudicated x KLO/NS3/NTAU) -- so whether LEAFREC has a '
           'referent here is a question for 70 before any build',
    spectra=['computations/beyond_the_wall/spectra/cc66_lowell_sweep.npz']),
 'P15_the_lowell_sweep_is_reproduced_by_a_producer_in_the_repository_and_the_bank_is_that_producers_output_rounded': dict(
    verdict=REGROUND, why='method', traced=False,
    anchor='the hierarchy agrees to three per cent at every multipole',
    reason='this receipt\'s claim is PROVENANCE -- the bank is its producer\'s output rounded, and '
           'the two independent Boltzmann treatments agree. A cross-validation between two '
           'implementations is a statement about the instruments, not about which arm either was '
           'run on, so the agreement figure does not move with LEAFREC',
    spectra=[]),
 'P15_the_model_difference_is_an_acoustic_contrast_difference_and_it_is_not_one_skys_luck': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor="$\\Delta$ carries $-1.056$ of the arm's $-1.159$ in fifteen bins",
    reason='the trough figure in print is this arm\'s residual against the control\'s, and the '
           'line-of-sight family it is built from -- `r6885_los_cr`, `r6885_losdp0_cr`, '
           '`r6885_lossw0_cr` -- is read on the namesake side; only the verification bank moved to '
           '`cc66_r185_verify_cr_leafrec1`. The receipt\'s own note says the family is reachable on '
           'the arm of record, and each of the three has a `_leafrec1` sibling',
    spectra=['computations/beyond_the_wall/spectra/r6885_los_cr.npz',
             'computations/beyond_the_wall/spectra/r6885_losdp0_cr.npz',
             'computations/beyond_the_wall/spectra/r6885_lossw0_cr.npz']),
 'P15_the_monopole_zero_point_is_not_the_channel_and_the_two_residuals_point_opposite_ways': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor="itself $1.044$ times the control's about its own envelope",
    reason='the oscillation ratio in print is this arm\'s about its own envelope and is computed '
           'from `r6897_fields.npz` and `r6897_noop.npz`, both namesake reads. ⌗ The receipt '
           'already reads `r6893_switch_screen_cr` on BOTH sides deliberately, so the move is '
           'available and partly done; the fields and no-op legs are what is left',
    spectra=['computations/beyond_the_wall/spectra/r6897_fields.npz',
             'computations/beyond_the_wall/spectra/r6897_noop.npz']),
 'P15_the_no_fit_confrontation_is_three_per_bin_and_its_residual_carries_a_nine_sigma_modulation_at_the_combs_own_period_which_binning_at_that_period_cancels': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='the control stands at $1.13$ per bin',
    reason='its `SPEC` table is explicit: `nofit_cr` is `refit_grid185_leafrec1/cr_base.npz` and '
           '`refit_cr` is `cc66_r185_verify_cr_leafrec1.npz`, both arm-of-record. The two namesake '
           'entries are `nofit_lcdm` and `refit_lcdm`, the control legs',
    spectra=['computations/beyond_the_wall/refit_grid185/lcdm_base.npz',
             'computations/beyond_the_wall/spectra/cc66_r185_verify_lcdm.npz']),
 'P15_the_peak_plane_survives_the_merge_the_sky_lands_within_one_sigma_of_the_control_and_a_full_driving_unit_is_thirteen_but_half_the_draws_lose_the_fourth_peak': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor='$11.7$ and $18.3$ on this arm',
    reason='this receipt reads the one-clock and licensed grids and the loading lever with NO '
           'per-arm split -- nothing in its live source names a `_leafrec1` path -- so the arm '
           'factors in print are namesake reads throughout. ⌗ Every one of the five has a '
           '`_leafrec1` sibling directory, the lever\'s four included, so this item repoints',
    spectra=['computations/beyond_the_wall/r7093_directions/grid_oneclock/cr_base.npz',
             'computations/beyond_the_wall/r7095_directions/grid_licensed/cr_base.npz',
             'computations/beyond_the_wall/r7201_cc66_loading_lever/cr_nodrive.npz',
             'computations/beyond_the_wall/r7201_cc66_loading_lever/cr_rb0.5.npz',
             'computations/beyond_the_wall/r7201_cc66_loading_lever/cr_rb1.5.npz']),
 'P15_the_phase_is_the_driving_and_the_undriven_arms_agree': dict(
    verdict=HELD, why='ctrl-figure', traced=True,
    anchor="moves the control's first peak from $220$ to $274$",
    reason='both figures the sentence prints are the CONTROL\'s -- its first peak moving 220 to 274 '
           'and its l_1/l_A by 0.1792 -- so the order\'s item-3 bar holds even though the receipt '
           'reads both arms\' `c54.186`/`c54.193` namesakes. ⛭ 69 asked for this one in the batch '
           'anyway because its header guard already states the namesake, so a proposed wording is '
           'carried in SPLIT.md and 69 can land it without waiting for 70',
    spectra=['computations/beyond_the_wall/spectra/c54.186_lcdm_L3000.npz',
             'computations/beyond_the_wall/spectra/c54.193_lcdm_nodrive_L3000.npz']),
 'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='the control settles at $1.01$ in $\\chi^{2}$ per bin',
    reason='`GRIDS[cr]` is `refit_grid_leafrec1_distances` and `_VER[cr]` is '
           '`cc66_refit_verify_cr_leafrec1.npz`; what stays on the namesake side is `GRIDS[lcdm]` '
           'and `cc66_refit_verify_lcdm.npz`, the control legs',
    spectra=['computations/beyond_the_wall/refit_grid/lcdm_base.npz',
             'computations/beyond_the_wall/spectra/cc66_refit_verify_lcdm.npz']),
 'P15_the_residual_does_not_sit_at_ell_A_it_sits_four_per_cent_off_and_the_visibility_width_candidate_predicts_an_ell_dependence_the_ratio_does_not_have': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor='from $3.3$ on $100$--$700$ to $1.7$ on $1300$--$1900$',
    reason='the arm-to-control ratio in print falls across the bands, and both figures come out of '
           '`r7183_nofit_figure/nofit_figure_numbers.npz`, the receipt\'s single read. ⚠ That is a '
           'derived FIGURE-NUMBERS product, not a spectrum, and it is the only file in its '
           'directory: moving it means re-running its producer on the arm of record, which is a '
           'different job from repointing a spectrum',
    spectra=['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.npz']),
 'P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_and_the_law_has_no_fitted_coefficient': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor="this arm's visibility is the $14.6$ per cent wider in $\\chi$",
    reason='this is the receipt that SUPPLIES the sentence\'s two figures -- the 14.6 per cent '
           'wider chi-extent and the sound horizon held to 0.08 per cent -- and it reads '
           '`r7041_accept_{lcdm,cr}` and `r6919_injected_{lcdm,cr}` with no `_leafrec1` anywhere. '
           '⚠ `r6919_injected_cr_leafrec1.npz` is banked but `r7041_accept_cr_leafrec1.npz` is not, '
           'so this one is half a repointing and half a build',
    spectra=['computations/beyond_the_wall/spectra/r7041_accept_cr.npz',
             'computations/beyond_the_wall/spectra/r6919_injected_cr.npz']),
 'P15_the_selection_does_not_truncate_so_the_thirteen_sigma_stands_at_twelve_point_nine_and_the_peak_that_goes_missing_is_the_third_not_the_fourth': dict(
    verdict=REBUILD, why='arm-figure', traced=True,
    anchor='one full unit of the driving is $12.5$ standard deviations',
    reason='the driving unit and the observed point are read off the receipt\'s own '
           '`CRON`/`CROFF` pair -- `grid_oneclock/cr_base.npz` against '
           '`r7201_cc66_loading_lever/cr_nodrive.npz` -- both namesake, with no per-arm split in '
           'the live source. Both directories have a `_leafrec1` sibling, so this one repoints',
    spectra=['computations/beyond_the_wall/r7093_directions/grid_oneclock/cr_base.npz',
             'computations/beyond_the_wall/r7201_cc66_loading_lever/cr_nodrive.npz']),
 'P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_trough_pattern_is_the_arms_alone': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='The control already fits these bins at $0.99$ per bin',
    reason='`BANK[cr]` is `cc66_r185_verify_cr_leafrec1.npz`, labelled THE ARM OF RECORD in the '
           'receipt itself; the only namesake read is `BANK[lcdm]`, the control leg',
    spectra=['computations/beyond_the_wall/spectra/cc66_r185_verify_lcdm.npz']),
 'P15_the_spacing_drift_is_made_in_the_projection_so_the_construction_determines_it_and_the_handover_contributes_nothing': dict(
    verdict=REBUILD, why='arm-figure', traced=False,
    anchor="this arm returns $+4.38$ against the control's $+4.42$",
    reason='the drift in print is this arm\'s against the control\'s. ⚠ UNTRACED: the receipt\'s '
           'own note records that its source and ladder legs already moved to '
           '`r6911_source_cr_kcont_leafrec1`, `c54.186_cr_KCONT_leafrec1` and '
           '`c54.186_cr_L3000_leafrec1` and that "the finding stands and its figures move", so the '
           'namesake grid and lever reads that remain may not carry the +4.38',
    spectra=['computations/beyond_the_wall/r7093_directions/grid_oneclock/cr_base.npz',
             'computations/beyond_the_wall/r7201_cc66_loading_lever/cr_nodrive.npz']),
 'P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_damping_envelope': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='the offset falling from $1.1$ to $0.2$ of that spread',
    reason='`BANK[cr]` is `cc66_r185_verify_cr_leafrec1.npz`, "named explicitly rather than '
           'templated" in the receipt\'s own words, so the arm\'s offset is arm-of-record. Its '
           'namesake CR read at the end is a deliberate namesake-against-arm-of-record comparison, '
           'and the remaining namesake FIGURE read is the control leg',
    spectra=['computations/beyond_the_wall/spectra/cc66_r185_verify_lcdm.npz']),
 'P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_position_not_amplitude': dict(
    verdict=HELD, why='ctrl-read', traced=True,
    anchor='$1.7$ of $287$ is under one per cent',
    reason='`_AOR[cr]` is `cc66_r185_verify_cr_leafrec1`; the namesake `cc66_r185_verify_cr.npz` is '
           'opened once for the K185 comparison and the remaining namesake figure read is '
           '`_AOR[lcdm]`, the control leg',
    spectra=['computations/beyond_the_wall/spectra/cc66_r185_verify_lcdm.npz']),
 'P15_where_the_likelihood_sits': dict(
    verdict=REGROUND, why='namesake-pin', traced=True,
    anchor="the control returns $\\chi^{2}=214.1$, or $1.16$ per bin",
    reason='this receipt PINS the namesake deliberately and says so in its own header -- "the arm '
           'of record is LEAFREC=1 ... they are NOT what this receipt pins" -- and its guard asserts '
           'every CR file it reads is the LEAFREC=0 namesake with a counterpart beside it. It scores '
           'the `c54.178` and `c54.177` pairs, which are the superseded configurations by '
           'construction. ⇒ The sentence is legitimately about the namesake and wants wording that '
           'says which arm it was read on, which is 69\'s own reading of it',
    spectra=['computations/beyond_the_wall/spectra/c54.178_cr.npz',
             'computations/beyond_the_wall/spectra/c54.178_lcdm.npz',
             'computations/beyond_the_wall/spectra/c54.177_cr.npz',
             'computations/beyond_the_wall/spectra/c54.177_lcdm.npz']),
}

# ══ the population, joined to the two instruments that produced it ══════════════════════════════
head('Ⓐ  THE THIRTY, AND THE READING CHECKED RATHER THAN TRUSTED')
ITEMS = sorted(CEN.prints_fig)
BASES = [os.path.basename(p)[:-3] for p in ITEMS]
print(f'      `r7667/census.py` ran green: {CEN_OK};  `r7669/classify.py` ran green: {CLS_OK}')
print(f'      figure-printing items on PO-87\'s list: {len(ITEMS)};  verdicts declared: {len(V)}')
_missing = [b for b in BASES if b not in V]
_extra = [b for b in V if b not in BASES]
if _missing:
    print(f'      ⛔ NO VERDICT: {_missing}')
if _extra:
    print(f'      ⛔ VERDICT FOR AN ITEM NOT ON THE LIST: {_extra}')
check(f'Ⓐ① EVERY one of the {len(ITEMS)} items has exactly one verdict and no item outside the '
      f'list has one, and both producing instruments are confirmed green rather than assumed -- '
      f'census {CEN_OK}, classify {CLS_OK}',
      CEN_OK and CLS_OK and not _missing and not _extra and len(V) == len(ITEMS),
      f'{len(V)} verdicts for {len(ITEMS)} items; {len(_missing)} missing, {len(_extra)} extra')

#: the control bar, applied mechanically to what I DECLARED, not to what I concluded
_ctrl = [b for b in BASES if V[b]['why'] in ('ctrl-read', 'ctrl-only', 'ctrl-figure')]
_ctrl_rebuild = [b for b in _ctrl if V[b]['verdict'] == REBUILD]
print(f'      items whose remaining namesake reads or printed figures are the CONTROL\'s: '
      f'{len(_ctrl)};  of them called REBUILD: {len(_ctrl_rebuild)}')
check(f"Ⓐ② ⛭⛭ THE ORDER'S OWN BAR IS ENFORCED BY THE GATE AND NOT BY MY CARE: of the {len(_ctrl)} "
      f'items resting on a control leg or printing only control figures, {len(_ctrl_rebuild)} are '
      f'called REBUILD.  r7669 item 3: "do not count a control-only read as REBUILD until [70] '
      f'reports"',
      len(_ctrl_rebuild) == 0 and len(_ctrl) > 0, f'{len(_ctrl)} control-side, 0 called REBUILD')

#: ⛭⛭ ARM ⑤: the reason is TAKEN FROM THE SENTENCE, and that is checkable.
_sent = {}
for p, b in zip(ITEMS, BASES):
    ss = [s for f, l in CEN.body_cited[p].items() for s in l if _NUM.search(s)]
    _sent[b] = list(dict.fromkeys(ss))
_unanchored = [b for b in BASES if not any(V[b]['anchor'] in s for s in _sent[b])]
if _unanchored:
    print('      ⛔ ANCHOR NOT FOUND IN THE ITEM\'S OWN SENTENCE:')
    for b in _unanchored:
        print(f'        {b[:84]}')
        print(f'          anchor: {V[b]["anchor"]!r}')
check(f'Ⓐ③ ⛭⛭ EVERY REASON IS ANCHORED IN ITS OWN SENTENCE: {len(BASES) - len(_unanchored)} of '
      f'{len(BASES)} verdicts quote a fragment that appears VERBATIM in one of that item\'s own '
      f'precise citing sentences.  ⇒ A verdict I invented rather than read would fail here, which '
      f'is the only check that reaches the reading itself',
      not _unanchored, f'{len(BASES) - len(_unanchored)} of {len(BASES)} anchored')

#: Ⓐ④ every path routed to 70 is real, or declared absent
_absent = sorted({q for b in BASES for q in V[b]['spectra']
                  if not os.path.exists(os.path.join(ROOT, q))})
print(f'      distinct spectrum paths named across all verdicts: '
      f'{len({q for b in BASES for q in V[b]["spectra"]})};  not on disk: {len(_absent)}')
for q in _absent:
    print(f'        ABSENT {q}')
check(f'Ⓐ④ every spectrum path named in a verdict EXISTS on disk, so 70 is not sent a path that is '
      f'already gone: {len(_absent)} absent',
      not _absent, f'{len(_absent)} absent paths')

#: ⛭⛭ Ⓐ⑤ THE DECLARATION IS CHECKED AGAINST THE RECEIPT.  An item I called `ctrl-read` must have an
#:   arm-of-record read in its LIVE source -- that is what makes the control leg the only namesake
#:   left.  An item I called `arm-figure` with `traced=True` must read a namesake CR spectrum.
GUARD = 'no arm-of-record counterpart'


def live_aor(pth):
    """does this receipt name a `_leafrec1` path in live code (not its docstring, not the guard)?"""
    import ast
    t = ast.parse(open(os.path.join(ROOT, pth), encoding='utf-8', errors='replace').read())
    skip = {id(t.body[0].value)} if (t.body and isinstance(t.body[0], ast.Expr)
                                    and isinstance(t.body[0].value, ast.Constant)) else set()
    for x in ast.walk(t):
        if isinstance(x, ast.Constant) and isinstance(x.value, str) and id(x) not in skip:
            if 'leafrec1' in x.value and GUARD not in x.value and len(x.value) < 160:
                return True
    return False


_aor_live = {b: live_aor(p) for p, b in zip(ITEMS, BASES)}
#: ⛔ THE FIRST FORM OF THIS GATE WAS TOO STRONG AND IT CAUGHT TWO ITEMS THAT ARE NOT MISTAKES.
#:   `derived_lensing_on_the_lcdm_arm` and `the_joint_fit_leaves_the_gaussian` read ONE control
#:   spectrum and nothing else: there is no arm leg in them to have moved, so requiring a live
#:   `_leafrec1` read of them asserted something false.  ⇒ The two grounds are now separate --
#:   `ctrl-read` (a two-arm receipt whose CR legs moved) MUST name an arm-of-record path, and
#:   `ctrl-only` (nothing but control spectra) must name NONE and every path it declares must be a
#:   control leg.  *Both halves are asserted, so neither class can absorb the other's items.*
_CTRLNAME = re.compile(r'lcdm|control', re.I)
_bad5 = [b for b in BASES if V[b]['why'] == 'ctrl-read' and not _aor_live[b]]
_bad5 += [b for b in BASES if V[b]['why'] == 'ctrl-only'
          and (_aor_live[b] or not V[b]['spectra']
               or not all(_CTRLNAME.search(os.path.basename(q)) for q in V[b]['spectra']))]
_n_cr = sum(1 for b in BASES if V[b]['why'] == 'ctrl-read')
_n_co = sum(1 for b in BASES if V[b]['why'] == 'ctrl-only')
if _bad5:
    print(f'      ⛔ the declared load story does not match the source: {_bad5}')
check(f'Ⓐ⑤ ⛭⛭ THE LOAD STORY IS CHECKED AGAINST THE SOURCE, BOTH WAYS: each of the {_n_cr} '
      f'`ctrl-read` items names a `_leafrec1` path in its LIVE code -- which is WHY the control leg '
      f'is the only namesake read left -- and each of the {_n_co} `ctrl-only` items names none and '
      f'declares nothing but control spectra.  {len(_bad5)} fail.  ⇒ If I had the direction '
      f'backwards on one of them, the control bar would be shielding an arm figure, and this is '
      f'where that shows',
      not _bad5, f'{len(_bad5)} mis-declared of {_n_cr} ctrl-read + {_n_co} ctrl-only')

# ══ the arms ════════════════════════════════════════════════════════════════════════════════════
head('Ⓑ  THE REGISTERED ARMS, SCORED')
_by = collections.Counter(V[b]['verdict'] for b in BASES)
_why = collections.Counter(V[b]['why'] for b in BASES)
print(f'      {REGROUND}: {_by[REGROUND]}   {REBUILD}: {_by[REBUILD]}   {HELD}: {_by[HELD]}')
print(f'      by ground: {dict(_why)}')

#: ⛔⛭⛭ ARM ① OVERSHOT, AND IN THE DIRECTION THAT MATTERS FOR THE ORDER.
_cr = sum(1 for b in BASES if V[b]['why'] == 'ctrl-read')
_cf = sum(1 for b in BASES if V[b]['why'] == 'ctrl-figure')
check(f'Ⓑ① ⛔⛭⛭ ARM ① IS FALSIFIED ON THE HIGH SIDE: I registered 4 to 10 of the thirty held as '
      f'control-only.  {_cr} rest on a CONTROL LEG and {_cf} more print only the control\'s own '
      f'figures, so {_cr + _cf} are held.  ⇒ ** The cause is structural and it is `r7669`\'s own '
      f'finding turned round: ** r7635/r7643 moved each receipt\'s CR legs to the arm of record and '
      f'COULD NOT move the control legs, because no arm-of-record grid has one.  So the namesake '
      f'reads left on PO-87\'s list are mostly the control side of two-arm reads, and 70\'s one '
      f'measurement decides them together',
      _cr + _cf > 10, f'{_cr} control-leg + {_cf} control-figure = {_cr + _cf} held, '
                      f'against a registered 4-10 -> FALSIFIED high')

check(f'Ⓑ② ARM ② SCORED: I registered at least 12 of the thirty as REBUILD; {_by[REBUILD]} are.  '
      f'*The number 70 is sized by, and it is the one arm of the five that did not move under the '
      f'reading*',
      _by[REBUILD] >= 12, f'{_by[REBUILD]} REBUILD against a registered >= 12 -> HIT')

#: ⛭⛭ ARM ③ -- THE CHEAP SIGNAL, SCORED AS A FALSIFICATION TARGET AND NOT AS A CLASSIFIER.
_WORD = re.compile(r'this arm|crossing arm|the arm of record|arm of record', re.I)


def regex_verdict(b):
    """what a regex over the sentence's WORDS would say -- the discriminator ITEM2_TRIAGE.md
    already called worthless.  Scored here so the claim is a measurement."""
    return REBUILD if any(_WORD.search(s) for s in _sent[b]) else REGROUND


_disagree = [b for b in BASES if regex_verdict(b) != V[b]['verdict']]
print(f'      the wording regex agrees with the read verdict on {len(BASES) - len(_disagree)} of '
      f'{len(BASES)}, and disagrees on {len(_disagree)}:')
for b in _disagree:
    print(f'        regex says {regex_verdict(b):9s} / read says {V[b]["verdict"]:9s}  {b[:60]}')
check(f'Ⓑ③ ⛭⛭ THE WORDING REGEX IS FALSIFIED A SIXTH TIME, and registered in the direction that '
      f'cost me: I registered at least 5 disagreements and there are {len(_disagree)} of '
      f'{len(BASES)}.  ⇒ Every one of them is a sentence that SAYS "this arm" while the figure in '
      f'print is the control\'s, or says nothing of the kind while printing an arm figure.  *If it '
      f'had agreed everywhere, six revisions of mine would have been over-reading a working signal*',
      len(_disagree) >= 5, f'{len(_disagree)} disagreements of {len(BASES)} '
                           f'against a registered >= 5 -> HIT')

_method = [b for b in BASES if V[b]['why'] == 'method']
check(f'Ⓑ④ ARM ④ SCORED: I registered at least 3 items whose sentence is still RE-GROUND because '
      f'the figure it prints is a METHOD or INSTRUMENT property no re-derivation would move.  '
      f'{len(_method)} are: {", ".join(b.split("_")[1][:14] + "..." for b in _method)}.  *This is '
      f'the open question I put to 69 at `r7671+cc66.1`, now a count rather than an opinion*',
      len(_method) >= 3, f'{len(_method)} method-property RE-GROUNDs against a registered >= 3')

# ══ what the two routings actually contain ══════════════════════════════════════════════════════
head('Ⓒ  THE TWO ROUTINGS, AND THE LIMIT OF THE SECOND')
_rg = [b for b in BASES if V[b]['verdict'] == REGROUND]
_rb = [b for b in BASES if V[b]['verdict'] == REBUILD]
_hd = [b for b in BASES if V[b]['verdict'] == HELD]
_untraced = [b for b in _rb if not V[b]['traced']]
_paths = sorted({q for b in _rb for q in V[b]['spectra']})


def has_sibling(rel):
    d, f = os.path.split(rel)
    return (os.path.exists(os.path.join(ROOT, d + '_leafrec1', f))
            or os.path.exists(os.path.join(ROOT, d, f.replace('.npz', '_leafrec1.npz'))))


_repoint = [q for q in _paths if has_sibling(q)]
_build = [q for q in _paths if not has_sibling(q)]
print(f'      to 69 (RE-GROUND, one batch) : {len(_rg)} sentences')
print(f'      to 70 (REBUILD)              : {len(_rb)} items over {len(_paths)} distinct spectra '
      f'-- {len(_repoint)} already banked on the arm of record, {len(_build)} to build')
print(f'      held pending 70\'s measurement: {len(_hd)}')
for q in _build:
    print(f'        TO BUILD  {q}')
check(f'Ⓒ① THE REBUILD ROUTING IS PRICED RATHER THAN LISTED: {len(_rb)} items over {len(_paths)} '
      f'distinct namesake spectra, {len(_repoint)} of which have an arm-of-record sibling already '
      f'banked and {len(_build)} of which do not.  ⌗ *That split is 70\'s, not mine -- it is the '
      f'bank\'s state, and `r7667`\'s Ⓒ② already found no item is cheap END TO END*',
      len(_repoint) + len(_build) == len(_paths) and len(_build) > 0,
      f'{len(_repoint)} repoint, {len(_build)} build')

#: ⛔⛭⛭ AND THE LIMIT OF THE REBUILD LIST IS STATED AS A COUNT, not admitted in a footnote.
check(f'Ⓒ② ⛔⛭⛭ THE RESOLUTION THIS READING DOES NOT HAVE IS COUNTED: {len(_rb) - len(_untraced)} '
      f'of the {len(_rb)} REBUILD items are TRACED -- the figure in print followed through the '
      f'receipt to a namesake load -- and {len(_untraced)} are UNTRACED, where the receipt\'s own '
      f'arm legs are already arm-of-record and the namesake reads that remain may be auxiliaries.  '
      f'⇒ ** This is the receipt-level-versus-site-level limit named at `r7669`, and it is why 70 '
      f'is sent a priced list with the untraced items flagged rather than a build order. **',
      len(_untraced) > 0 and all(V[b]['why'] == 'arm-figure' for b in _untraced),
      f'{len(_rb) - len(_untraced)} traced, {len(_untraced)} untraced')

#: ⛭ the structural fact that makes "its sentence" ambiguous, measured so 69 can see it
_multi = [b for b in BASES if any(len(re.findall(r'\\rcpt\{', s)) > 1 for s in _sent[b])]
print(f'      items at least one of whose citing sentences carries MORE THAN ONE `\\rcpt`: '
      f'{len(_multi)} of {len(BASES)}')
check(f'Ⓒ③ ⛭ WHY "ITS SENTENCE" IS NOT ALWAYS ONE RECEIPT\'S: {len(_multi)} of {len(BASES)} items '
      f'are cited in a sentence that cites OTHERS too, so the figure in print may be a co-cited '
      f'receipt\'s rather than this one\'s.  *Stated as a count because it is the reason some '
      f'reasons below name which receipt supplies the figure instead of assuming this one does*',
      len(_multi) > len(BASES) / 3, f'{len(_multi)} of {len(BASES)} multi-cited')

# ══ THE SPLIT ═══════════════════════════════════════════════════════════════════════════════════
head('THE SPLIT -- every item, its verdict, its anchor in its own sentence, and its reason')
for n, (p, b) in enumerate(zip(ITEMS, BASES), 1):
    d = V[b]
    print(f'  [{n:02d}] {d["verdict"]:9s} ({d["why"]}{"" if d["traced"] else ", UNTRACED"})  {b}')
    print(f'       lines: {sorted({BODY[:m.start()].count(chr(10)) + 1 for m in re.finditer(re.escape(chr(92) + "rcpt{" + b + "}"), BODY)})}')
    print(f'       anchor: "{d["anchor"]}"')
    print(f'       reason: {d["reason"]}')
    for q in d['spectra']:
        print(f'       spectrum: {q}  '
              f'{"[arm-of-record sibling banked]" if has_sibling(q) else "[NO sibling -- to build]"}')
print()
print(f'  TOTALS: {len(_rg)} RE-GROUND to 69, {len(_rb)} REBUILD to 70 '
      f'({len(_rb) - len(_untraced)} traced / {len(_untraced)} untraced), {len(_hd)} HELD pending '
      f'70\'s control measurement.  {len(_paths)} distinct spectra: {len(_repoint)} repoint, '
      f'{len(_build)} build.')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)
