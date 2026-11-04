# `r7669` (cc66) ITEM 2 — TRIAGE FOR THE RE-GROUND / REBUILD SPLIT

⛔ **THIS IS A SORTING AID AND NOT A VERDICT, and the distinction is the point.**
The order asks, for every surviving item, which of RE-GROUND or REBUILD it is **and why from the
sentence**. That is a judgement about what a sentence CLAIMS, and the discriminator below is a
regex over the sentence's words (`this arm`, `crossing arm`, `the arm of record`).

⇒ **A regex over wording is precisely the cheap signal that has now failed five times in three
revisions** — strings the paper could not contain, a `{base}` match hitting `\rcptlabel`, a
filename where the tree keys on a path, a token where the question is what the code loads, and a
receipt that *mentions* `leafrec1` rather than loading it. **So no row below is a verdict.** The
table sorts 53 items so that the per-item reading has somewhere to start, and names the one class
it CAN decide mechanically: a control-only namesake read, which is the order's item 3.

**Tree `5e2eb9658`.** Counts: **53** surviving figure-printing items; **4** control-only
namesake reads (item 3); **34** whose sentence uses arm-of-record wording; **17** that also load
the arm of record, where the sentence decides which figure is in print.

```
SURVIVING FIGURE-PRINTING ITEMS NEEDING AN ITEM-2 VERDICT: 53

  of them: control-only namesake reads = 4   sentence claims 'this arm' = 34   also load AoR = 17

[01] REBUILD?       P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two
      loads: ['r6919_geometry.npz  computations/beyond_the_wall/spectra', 'r6919_noop.npz  computations/beyond_the_wall/spectra', 'r6919_injected_ .npz r6919_injected_ .npz  computations/beyond_the_wal']
      sent : "\emph{The sound speed the kernel sees is therefore $0.455$ on the control and $0.397$ here}, and a difference in that ratio is term-independent by construction, grows with wavenumber, and vanishes for"
[02] REBUILD?       P15_all_three_projections_clear_the_instrument_noise_null_so_the
      loads: ['r6941_fine_lcdm.npz', 'r6941_fine_cr.npz', 'r6975_mix_lcdm.npz']
      sent : "\emph{A null built instead from the same data at neighbouring frequencies cannot be used for the question at all}, its amplitudes carrying the feature they are meant to score: over this range such an "
[03] REBUILD?       P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoust
      loads: ['cc66_ .npz cc66_ .npz  computations/beyond_the_wall/spectra', '']
      sent : "\emph{So the acoustic scale is computed rather than accommodated}, and it is the comb of the computed spectrum that carries it: fitted to those peaks by the procedure this paper runs on the sky, it is"
[04] ITEM3-CONTROL  P15_derived_lensing_on_the_lcdm_arm.py
      loads: ['computations beyond_the_wall spectra c54.178_lcdm.npz']
      sent : "\emph{Most of the fitted headroom is recovered by a genuine lensing, and about $989$ of the $1320$ survives it}: the verdict of the last paragraph stands from the derived side, lensing real and not th"
[05] REBUILD?       P15_the_133_bin_pair_is_computed_and_asserted_and_the_hardcoded_
      loads: ['.npz  computations/beyond_the_wall/spectra', '.npz  computations/beyond_the_wall/spectra', '.npz  computations/beyond_the_wall/spectra']
      sent : "The $133$-bin unlensed one is where the shape rejection is quoted, and its control sits at $2.10$ per bin because the ceiling cuts the damping tail\rcpt{P15_the_133_bin_pair_is_computed_and_asserted_a"
[06] ITEM3-CONTROL  P15_the_1p57_has_no_parameter_address_because_the_arms_tt_minimu
      loads: ['cr verify_ .npz verify_ .npz  computations/beyond_the_wall/spectra/cc6', 'verify_lcdm.npz  computations/beyond_the_wall/refit_grid185', 'computations/beyond_the_wall/spectra/cc66_r185_verify_cr_leafrec1.npz']
      sent : "\emph{And the spectrum's own parameters are refitted, which is the comparison the standard model is usually judged by.} With the expansion rate, the matter and baryon densities and the tilt free in ea"
[07] REBUILD?       P15_the_acceptance_does_not_move_under_refinement_and_three_of_t
      loads: ['r7041_accept_digest.npz  computations/beyond_the_wall/spectra', 'r7041_accept_Al.npz  computations/beyond_the_wall/spectra', 'r7041_accept_sample.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{Read physically the law says one thing}: a wider $\chi$-extent narrows the kernel's acceptance in wavenumber, so less of an acoustic period is averaged over and more of the comb survives; this a"
[08] REBUILD?       P15_the_acoustic_contrast_is_not_in_the_source_and_the_projectio
      loads: ['r6911_source_cr_kcont_leafrec1.npz  computations/beyond_the_wall/spect', 'r6911_noop.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra']
      sent : "\emph{Nor is it the distance}: the two arms' comoving distances to last scattering differ by $0.449$ per cent with this arm's the larger, their acoustic angles agreeing to $0.085$ per cent, and projec"
[09] REBUILD?       P15_the_anomalous_driving_belonged_to_the_pin_and_not_to_the_con
      loads: ['cc66_ .npz cc66_ .npz  computations/beyond_the_wall/spectra']
      sent : "\emph{The second is not a worse measurement of the first's quantity}: it is a different configuration, chosen for the comparison it makes, and the two sit beside each other rather than one superseding"
[10] RE-GROUND?     P15_the_carrier_separation_on_L_p_is_the_combs_peak_count_not_th
      loads: ['cr_base.npz  computations/beyond_the_wall/r7093_directions/grid_oneclo', '']
      sent : "\emph{So the two halves of this comparison want opposite binnings}---the comb wants points the correlation above shows it cannot use, and the locator wants the bank merged, which costs exactly those p"
[11] REBUILD?       P15_the_combs_resolution_is_four_multipoles_and_the_skys_own_val
      loads: ['r6929_scan_cr .npz r6929_scan_cr .npz  computations/beyond_the_wall/sp', 'r6929_geometry .npz r6929_geometry .npz  computations/beyond_the_wall/', 'r6929_noop.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{And the motion the alternative produces is separable into its causes}, the projection of an analytic oscillating source with no plasma dynamics in it isolating them: about a third is the visibil"
[12] REBUILD?       P15_the_contrast_excess_is_symmetric_about_the_envelope_and_the_
      loads: ['r6941_fine_cr_visleaf_leafrec1.npz  computations/beyond_the_wall/spect', 'r6929_scan_cr_leafrec1.npz  computations/beyond_the_wall/spectra', 'r6929_geometry_leafrec1.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{And the depths are the one statistic in this comparison whose residual is not shared}: the control lands on the measured trough depths at five hundredths of a standard deviation while this arm s"
[13] REBUILD?       P15_the_control_entered_the_regime_and_the_arm_did_not_move.py
      loads: ['computations/beyond_the_wall/spectra', '.npz  ../../computations/beyond_the_wall/spectra']
      sent : "\emph{And the truncation's removal is measured on the arm whose answer is known}: it was $78\%$ of the control's remaining $\chi^{2}$, and taking it out brings the control to $1.18$ per degree of free"
[14] ITEM3-CONTROL  P15_the_controls_base_log_is_banked_beside_the_grids_and_the_pea
      loads: ['', '', '/tmp/n66/r7109_control/lcdm_base.npz']
      sent : "\emph{Built instead with the projection's distance on the leaf rate it closes the whole of it}: $\chi^{2}=186.135$, level with the control's own value; sign changes landing on the control's own $87$; "
[15] RE-GROUND?     P15_the_cross_term_is_not_the_channel_and_every_projected_term_c
      loads: ['r6915_noop.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra']
      sent : "\emph{The intercept of that rise covers one across the same twelve settings}, $1.017$ with a spread of $0.010$, so what is established is the growth with wavenumber and not a constant offset: \emph{wh"
[16] RE-GROUND?     P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_
      loads: ['.npz  computations/beyond_the_wall/spectra', '']
      sent : "\emph{The fourth peak's excess reproduces there too}, so it is a property of the spectrum rather than of either implementation---and on that path, where the sub-bin location is available on both arms,"
[17] REBUILD?       P15_the_fit_has_the_controls_freedom_and_the_contrast_the_data_a
      loads: ['cr_base.npz  computations/beyond_the_wall/refit_grid185_leafrec1', 'computations/beyond_the_wall/spectra/cc66_lens_ratio.npz', '.npz .npz']
      sent : "\emph{And the leftover is not noise}: in $\ell$ order this arm's residual changes sign $54$ times against $88\pm10$ for correlated draws of the likelihood's own covariance with the same five direction"
[18] REBUILD?       P15_the_floor_is_a_distance_between_models_not_a_number_from_the
      loads: ['c54.186_lcdm_L3000.npz  computations/beyond_the_wall/spectra', 'c54.186_cr_L3000.npz  computations/beyond_the_wall/spectra', '.npz  ../../computations/beyond_the_wall/spectra']
      sent : "\emph{And the motion the alternative produces is separable into its causes}, the projection of an analytic oscillating source with no plasma dynamics in it isolating them: about a third is the visibil"
[19] REBUILD?       P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switc
      loads: ['r6893_slice_check.npz  computations/beyond_the_wall/spectra', 'r6893_full_reach_nulls_lcdm.npz  computations/beyond_the_wall/spectra', 'r6893_switch_screen_ .npz r6893_switch_screen_ .npz  computations/beyo']
      sent : "\emph{The two sides of that agreement are computed independently}: the reported scale reaches the transfer nowhere---no source term, no projection and no solver reads it---so the comb it is compared a"
[20] REBUILD?       P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and
      loads: ['cr_x_h686_L2000_leafrec1_distances', 'lcdm_L2000', 'cc66_ .npz cc66_ .npz  computations/beyond_the_wall/spectra']
      sent : "\emph{The two sides of that agreement are computed independently}: the reported scale reaches the transfer nowhere---no source term, no projection and no solver reads it---so the comb it is compared a"
[21] REBUILD?       P15_the_full_range_refit_holds_the_background_and_the_phase_resi
      loads: ['cr_base.npz cr  computations/beyond_the_wall/refit_grid185_leafrec1_di', 'r6941_fine_cr_leafrec1.npz  computations/beyond_the_wall/spectra', 'cc66_lens_ratio.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{And the spectrum's own parameters are refitted, which is the comparison the standard model is usually judged by.} With the expansion rate, the matter and baryon densities and the tilt free in ea"
[22] ITEM3-CONTROL  P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not
      loads: ['computations beyond_the_wall spectra L820_lcdm_L2512_nk800.npz']
      sent : "\emph{And the tilt takes a fixed share of it rather than a variable one}: seven tenths at the adjudicated ratio and seven tenths at $1.0926$, so what the refit can and cannot do is a property of the s"
[23] RE-GROUND?     P15_the_kernels_phase_difference_between_the_arms_is_four_orders
      loads: ['computations/beyond_the_wall/r7093_directions/grid_oneclock_leafrec1/c', '.npz .npz  computations/beyond_the_wall/r7093_directions/grid_oneclock']
      sent : "\emph{And the Bessel route reaches that answer only when it is sampled finely enough}: at under two points per Bessel period it manufactures a difference between the arms $74$ times the true one, whil"
[24] REBUILD?       P15_the_laws_six_of_seven_is_five_at_the_quoted_floor_which_is_o
      loads: ['r7041_accept_ .npz r7041_accept_ .npz  computations/beyond_the_wall/sp']
      sent : "\emph{Read physically the law says one thing}: a wider $\chi$-extent narrows the kernel's acceptance in wavenumber, so less of an acoustic period is averaged over and more of the comb survives; this a"
[25] REBUILD?       P15_the_licensed_configuration_moves_neither_statistic_and_the_s
      loads: ['refit_grid185_leafrec1 cr_base.npz  computations/beyond_the_wall', 'r7095_directions grid_licensed_leafrec1 cr_base.npz  computations/beyo', 'cr_base.npz']
      sent : "\emph{The control's own coefficient is identical across all three grids}, which is what says the move belongs to this arm and not to the method\rcpt{P15_the_licensed_configuration_moves_neither_statis"
[26] RE-GROUND?     P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks
      loads: ['r6941_fine_cr_visleaf_leafrec1.npz  computations/beyond_the_wall/spect', 'r6929_scan_cr_leafrec1.npz  computations/beyond_the_wall/spectra', 'r6929_geometry_leafrec1.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{The fourth peak's excess reproduces there too}, so it is a property of the spectrum rather than of either implementation---and on that path, where the sub-bin location is available on both arms,"
[27] RE-GROUND?     P15_the_low_multipole_depth_gap_closes_and_two_defects_were_canc
      loads: ['cc66_lowell_sweep.npz  computations/beyond_the_wall/spectra']
      sent : "Carried out with the exact transfer (gate-validated: the continuum reproduces the code's own $C_\ell$ to four figures; and the $r_0$ sensitivity is measured rather than assumed: the \emph{shape} is st"
[28] RE-GROUND?     P15_the_lowell_sweep_is_reproduced_by_a_producer_in_the_reposito
      loads: ['computations/beyond_the_wall/spectra/cc66_lowell_sweep.npz', 'utf-8   computations/beyond_the_wall/r7109_directions/lowell_rederive.']
      sent : "\emph{The two independent Boltzmann treatments cross-validate the depth as well as the shape} once each carries the late integrated Sachs--Wolfe term to the present: on the exact transfer the deficit "
[29] REBUILD?       P15_the_model_difference_is_an_acoustic_contrast_difference_and_
      loads: ['', '', 'computations/beyond_the_wall/spectra']
      sent : "And one direction built from the control alone---raise the oscillation at fixed envelope, with nothing fitted---carries over half of $\lVert\Delta\rVert^{2}$\rcpt{P15_the_model_difference_is_an_acoust"
[30] REBUILD?       P15_the_monopole_zero_point_is_not_the_channel_and_the_two_resid
      loads: ['r6897_fields.npz  computations/beyond_the_wall/spectra', 'r6893_switch_screen_cr_leafrec1.npz  computations/beyond_the_wall/spec', 'r6893_switch_screen_cr.npz  computations/beyond_the_wall/spectra']
      sent : "And one direction built from the control alone---raise the oscillation at fixed envelope, with nothing fitted---carries over half of $\lVert\Delta\rVert^{2}$\rcpt{P15_the_model_difference_is_an_acoust"
[31] REBUILD?       P15_the_no_fit_confrontation_is_three_per_bin_and_its_residual_c
      loads: ['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.n', '']
      sent : "\emph{And the spectrum's own parameters are refitted, which is the comparison the standard model is usually judged by.} With the expansion rate, the matter and baryon densities and the tilt free in ea"
[32] RE-GROUND?     P15_the_peak_statistic_cannot_be_pointed_at_the_observed_spectru
      loads: ['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.n', '', '']
      sent : "\emph{The loading is separated from a reparametrization of the clock as well, by a factor of six; the driving is not}, sitting within a sixth of the largest clock reading and inside the spread of the "
[33] RE-GROUND?     P15_the_period_difference_null_is_not_significant_because_the_co
      loads: ['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.n']
      sent : "\emph{What could carry a running phase at correct spacing is therefore the driving and the baryon loading, and that is named rather than measured}\rcpt{P15_the_residual_does_not_sit_at_ell_A_it_sits_f"
[34] RE-GROUND?     P15_the_phase_is_the_driving_and_the_undriven_arms_agree.py
      loads: ['computations/beyond_the_wall/spectra', '.npz  ../../computations/beyond_the_wall/spectra']
      sent : "\emph{The second is not a worse measurement of the first's quantity}: it is a different configuration, chosen for the comparison it makes, and the two sit beside each other rather than one superseding"
[35] REBUILD?       P15_the_phase_slope_does_not_separate_the_loading_from_the_drivi
      loads: ['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.n', 'cr_base.npz  computations/beyond_the_wall/r7095_directions/grid_licens', '']
      sent : "\emph{What could carry a running phase at correct spacing is therefore the driving and the baryon loading, and that is named rather than measured}\rcpt{P15_the_residual_does_not_sit_at_ell_A_it_sits_f"
[36] RE-GROUND?     P15_the_phase_systematic_leaves_the_step_standing_and_carries_a_
      loads: ['computations/beyond_the_wall/spectra', 'r6959_eta_cr_leafrec1.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra']
      sent : "\emph{And the statistic's phase systematic is what limits both}, carrying three to three and a half independent modes across the seven bands where its noise response carries nearly seven---\emph{the s"
[37] REBUILD?       P15_the_refit_leaves_the_background_where_the_distances_put_it_a
      loads: ['', '_base.npz _base.npz tag tag', 'computations/beyond_the_wall/spectra']
      sent : "\emph{And the spectrum's own parameters are refitted, which is the comparison the standard model is usually judged by.} With the expansion rate, the matter and baryon densities and the tilt free in ea"
[38] RE-GROUND?     P15_the_residual_does_not_sit_at_ell_A_it_sits_four_per_cent_off
      loads: ['computations/beyond_the_wall/r7183_nofit_figure/nofit_figure_numbers.n']
      sent : "The same candidate fails a second way: a wider visibility is Silk damping, which acts strongly at high multipole and barely at low, so it predicts an arm-to-control ratio that climbs with $\ell$---and"
[39] RE-GROUND?     P15_the_residual_is_contrast_and_the_lensing_potential_is_derive
      loads: ['computations beyond_the_wall spectra c54.178_lcdm.npz', 'computations/beyond_the_wall/spectra/c54.182_clpp.npz']
      sent : "\emph{Most of the fitted headroom is recovered by a genuine lensing, and about $989$ of the $1320$ survives it}: the verdict of the last paragraph stands from the derived side, lensing real and not th"
[40] REBUILD?       P15_the_resolution_table_eight_of_the_eleven_instruments_cannot_
      loads: ['r6941_fine_lcdm.npz  computations/beyond_the_wall/spectra', 'r6941_fine_cr_leafrec1.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra']
      sent : "\emph{A null built instead from the same data at neighbouring frequencies cannot be used for the question at all}, its amplitudes carrying the feature they are meant to score: over this range such an "
[41] REBUILD?       P15_the_retention_is_the_combs_average_over_the_kernels_own_k_ac
      loads: ['r7041_accept_ .npz r7041_accept_ .npz  computations/beyond_the_wall/sp', 'r6919_injected_ .npz r6919_injected_ .npz  computations/beyond_the_wal']
      sent : "\emph{Read physically the law says one thing}: a wider $\chi$-extent narrows the kernel's acceptance in wavenumber, so less of an acoustic period is averaged over and more of the comb survives; this a"
[42] REBUILD?       P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_t
      loads: ['computations/beyond_the_wall/spectra']
      sent : "\emph{That fraction is not an attribution, and reading it as one would be an error}: both arms are fitted to the same bandpowers, so their residuals differ by the model difference alone and the fracti"
[43] RE-GROUND?     P15_the_shear_coefficient_derived_not_remembered.py
      loads: ['.npz .npz  computations/beyond_the_wall/spectra']
      sent : "\emph{The polarisation correction itself, which is the quantity in dispute, is a factor $1.1996$ against $6/5$: three parts in ten thousand.} Both absolute values sit about half a per cent low by an a"
[44] REBUILD?       P15_the_source_decomposition_is_reachable_on_the_reporting_path_
      loads: ['cc66_r185_verify_ .npz cc66_r185_verify_ .npz', '', 'r6885_dp0_lcdm.npz']
      sent : "\emph{One systematic is stated rather than minimised}: the envelope's abscissa moves the measured depth by about a third of that spread across the admissible acoustic scales. \emph{And the three featu"
[45] REBUILD?       P15_the_spacing_drift_is_made_in_the_projection_so_the_construct
      loads: ['source_combs.json utf-8   computations/beyond_the_wall/r7234_60_is_the', 'computations/beyond_the_wall/spectra/r6911_source_cr_kcont_leafrec1.np', '']
      sent : "\emph{So the drift is a parameter-free prediction of the spectrum and no test at all of the rate split}: this arm returns $+4.38$ against the control's $+4.42$, with every peak position agreeing to be"
[46] REBUILD?       P15_the_term_mix_does_not_carry_the_modulation_and_it_survives_i
      loads: ['r6941_fine_lcdm.npz', 'r6941_fine_cr.npz', 'computations/beyond_the_wall/spectra']
      sent : "\emph{A null built instead from the same data at neighbouring frequencies cannot be used for the question at all}, its amplitudes carrying the feature they are meant to score: over this range such an "
[47] REBUILD?       P15_the_third_peak_deficit_is_radiation_driving_and_both_routes_
      loads: ['cc66_ .npz cc66_ .npz  computations/beyond_the_wall/spectra']
      sent : "\emph{Each is worth a factor on its own and neither alone reaches the answer}: the height ratio runs from $2.721$ at an $\ell$-equivalent cutoff of $900$ to $2.393$ at $2400$, so a cutoff set at the r"
[48] RE-GROUND?     P15_the_three_instruments_with_no_noise_model_one_can_be_given_a
      loads: ['r6915_pairs_lcdm.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra', 'r6959_eta_cr_leafrec1.npz  computations/beyond_the_wall/spectra']
      sent : "\emph{Which is why the rejection this section closes on is read in the likelihood and not here}: the whole-range contrast is what this instrument supports, and the band-by-band structure is a property"
[49] RE-GROUND?     P15_the_tilt_off_the_tail_cannot_decide_the_signature_on_plancks
      loads: ['fit_primary.json', 'fit_control.json', 'w_null_1000_2508.json']
      sent : "\emph{No window of Planck's decides}: separating the two predictions needs $2\sigma$, the nearest window, $\ell=700$--$1760$, reaches $1.65$, and each of the four windows sits $0.1$--$0.4\sigma$ from "
[50] REBUILD?       P15_the_two_readings_are_different_quantities_and_the_projection
      loads: ['r6897_fields.npz  computations/beyond_the_wall/spectra', '.npz  computations/beyond_the_wall/spectra', '.npz  computations/beyond_the_wall/spectra']
      sent : "A ratio of band-integrated powers mixes the two and reads the opposite sign on the same spectra---\emph{so the two readings are different quantities and not a disagreement about one}, and the one this"
[51] REBUILD?       P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_da
      loads: ['cc66_r185_verify_cr.npz  computations/beyond_the_wall/spectra', 'computations/beyond_the_wall/spectra', '']
      sent : "\emph{So the arm sits about one of the locator's own window-to-window spreads from the sky on the one fit and on the sky's value in the other}, the offset falling from $1.1$ to $0.2$ of that spread wh"
[52] RE-GROUND?     P15_three_quarters_of_the_arms_residual_is_the_controls_and_what
      loads: ['computations/beyond_the_wall/spectra/cc66_fig_acoustic_numbers.npz', '.npz  computations/beyond_the_wall/spectra', 'cc66_r185_verify_cr.npz  computations/beyond_the_wall/spectra']
      sent : "It is small: the rescale is under a multipole at the fourth peak, and $1.7$ of $287$ is under one per cent\rcpt{P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_position_not"
[53] REBUILD?       P15_where_the_likelihood_sits.py
      loads: ['lcdm.json   computations/planck_tt_likelihood', '.npz .npz  computations/beyond_the_wall/spectra', '.npz .npz  computations/beyond_the_wall/spectra']
      sent : "\emph{The two sides of that agreement are computed independently}: the reported scale reaches the transfer nowhere---no source term, no projection and no solver reads it---so the comb it is compared a"
```
