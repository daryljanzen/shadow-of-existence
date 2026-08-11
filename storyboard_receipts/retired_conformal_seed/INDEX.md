# RETIRED — the conformal-time seeding defect (r2350)

These 70 receipts build their background as `ag = np.logspace(-5, 0, ...)` with the conformal time
`eg` **seeded at zero**, omitting the 4.596 Mpc already elapsed from a = 0.  In radiation domination
H ∝ a⁻² makes the integrand c/(a²H) constant, so the omitted piece is a_min/(H₀√Ω_r) — a fixed offset
at every epoch: 0.03% of η₀, but 12% of η at z = 10⁴.

**What that means for reading them.**  Late-time results here are unaffected — the acoustic scale, the
peak positions and the peak ratios are insensitive to a constant η offset.  Early-time quantities, and
any comparison against a second code, are not.  The signature is a smooth, monotone, k-growing amplitude
error, because the potential decays more steeply at larger k.

**They are stored as built and used, not retroactively corrected**, so the record of what was actually run
stays honest.  None is cited by the corpus and none is imported by anything that is; the three files that
were live (`HIER_photon_hierarchy`, `C11TEST_radiation_zeroed`, `ROBUST_p1p2_scan`) were fixed at
r2349–r2350 and remain in `storyboard_receipts/`.

| receipt | what it was |
|---|---|
| `BASE_baseline_subtracted` | CRRUN — THE SAME INTEGRATOR ON CR |
| `BRACKET_datum_family` | CRRUN — THE SAME INTEGRATOR ON CR |
| `BUMP_reionisation_rescatter` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `CAP_stability_cap` | CRRUN — THE SAME INTEGRATOR ON CR |
| `COMPLETE_two_constraint` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CONT_continuum_ab_test` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRFINAL_pole_free_spectrum` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN10_exact_constraint` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN11_discrete_source` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN2_constraint_attempt` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN3_one_datum` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN4_valid_range` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN5_leg_state_seam_data` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN6_full_constraint` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN7_two_branch` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN8_radiation_corrected` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN9_continuity_matched` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRRUN_first_attempt` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CRSHAPE_spectrum_shape` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CTRL_low_ell_control` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `CTRL_rate_radiation` | CRRUN — THE SAME INTEGRATOR ON CR |
| `CTRL_same_machinery_on_lcdm` | CTRL — THE IDENTICAL MACHINERY ON LambdaCDM |
| `DETERMINED_seam_datum` | CRRUN — THE SAME INTEGRATOR ON CR |
| `DRIVETEST_psi_driving` | CRRUN — THE SAME INTEGRATOR ON CR |
| `ENV2_amplitude_envelope` | CRRUN — THE SAME INTEGRATOR ON CR |
| `ENV_envelope_test` | CRRUN — THE SAME INTEGRATOR ON CR |
| `ETAPHASE_uncontaminated` | CRRUN — THE SAME INTEGRATOR ON CR |
| `EXTREMA_correct_statistic` | CRRUN — THE SAME INTEGRATOR ON CR |
| `FIXISW_phi_rec_per_mode` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `FULLRANGE_validation_curve` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `GATEALL_psi_gated` | CRRUN — THE SAME INTEGRATOR ON CR |
| `HEIGHTS_cr_vs_lcdm` | CRRUN — THE SAME INTEGRATOR ON CR |
| `HIER_CR` | HIER — THE PHOTON BOLTZMANN HIERARCHY |
| `HYBK_hybrid_k_grid` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `INSTR2_collapse_profile` | CRRUN — THE SAME INTEGRATOR ON CR |
| `INSTR_localise_divergence` | CRRUN — THE SAME INTEGRATOR ON CR |
| `ISW3_full_projection` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `LATE_isw_factorised` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `LCDMBA_own_envelope` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `LCDMPSI_control_potential` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `LEAF_spectrum_first_principles` | LEAF — THE CR SPECTRUM ON THE LEAF RATE, FROM FIRST PRINCIPLES |
| `LEGKS_corrected_horizon` | CRRUN — THE SAME INTEGRATOR ON CR |
| `LNA_log_a_stepping` | CRRUN — THE SAME INTEGRATOR ON CR |
| `LOGK_log_k_grid` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `LOS_visibility_control` | LOS — THE VISIBILITY-WEIGHTED LINE-OF-SIGHT CONTROL |
| `NOLATE_isw_off` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `NONU_neutrinos_off` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PEAKMAKE_source_growth` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PHASEMEAS_driving_shift` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PHASE_source_vs_acoustic` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PHIOWN_constant_potential` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PROJGEN_projection_generic` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `PROJ_line_of_sight` | PROJ — THE LINE-OF-SIGHT PROJECTION, per A |
| `PSICHECK_baseline_vs_amplitude` | CRRUN — THE SAME INTEGRATOR ON CR |
| `PSISCAN_amplitude` | CRRUN — THE SAME INTEGRATOR ON CR |
| `RECON_heights_from_source` | CRRUN — THE SAME INTEGRATOR ON CR |
| `REION_optical_depth` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `RESET_theta_phase` | CRRUN — THE SAME INTEGRATOR ON CR |
| `RK4_fixed_step` | CRRUN — THE SAME INTEGRATOR ON CR |
| `SCAN_datum_specification` | CRRUN — THE SAME INTEGRATOR ON CR |
| `SEAMCTRL_seam_start_control` | ISW2 — THE ISW TERM ADDED TO THE PROJECTION |
| `SEAMTEST_lseam_scaling` | CRRUN — THE SAME INTEGRATOR ON CR |
| `SQ_source_comb_spacing` | CRRUN — THE SAME INTEGRATOR ON CR |
| `SRC_source_across_cliff` | CRRUN — THE SAME INTEGRATOR ON CR |
| `TC10_neutrino_hierarchy` | TC10 — THE NEUTRINO HIERARCHY ADDED, per A |
| `TC11_neutrino_diagnostic` | TC10 — THE NEUTRINO HIERARCHY ADDED, per A |
| `TC8_psi_evolved` | TC8 — Psi EVOLVED FROM ITS OWN EQUATION, NOT IMPOSED |
| `TC9_two_component` | TC9 — THE TWO-COMPONENT SYSTEM |
| `VEC_vectorised_modes` | CRRUN — THE SAME INTEGRATOR ON CR |
| `WHERE_power_in_k` | CRRUN — THE SAME INTEGRATOR ON CR |
