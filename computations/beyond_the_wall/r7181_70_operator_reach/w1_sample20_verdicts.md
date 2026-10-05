# C3 — a seeded sample of 20 of W1's newly SLACK sites (`random.seed(7181)`, `w1_sample20.tsv`), read by hand

The verdicts are the r7179 ones.
- **GENUINE**: the paper prints this figure for this quantity, and the width is unargued.
- **COINCIDENTAL**: the matched paper prints the number for something else, or the literal is not a paper figure.
- **ARGUED**: the width is justified, or a tight pin on the same quantity stands beside it.

| # | site | L | matched in | verdict |
|---|---|---|---|---|
| 1 | `P15_the_acoustic_contrast…:422` | 1.04 | CR_cosmology | COINCIDENTAL: an injected test contrast, not a paper figure |
| 2 | `P15_the_fit_has_the_controls_freedom…:313` | 88 | canonical_time | COINCIDENTAL: a noise mean, matched in an unrelated paper |
| 3 | `P15_the_licensed_rebuild…:110` | 278.8 | CR_cosmology | GENUINE (x2) |
| 4 | `P15_the_retention_is_the_combs_average…:215` | 12.8 | CR_cosmology | GENUINE (x100; "two routes to one quantity", width unargued) |
| 5 | `LIFT_adiabatic_correction:32` | 3.338738 | CR_cosmology | GENUINE (x20) |
| 6 | `P15_the_transmission_figure…:198` | 2.4382e-8 | — | COINCIDENTAL: **a false match from the absolute-1e-9 bug**; unanchored under relative matching |
| 7 | `P16_theory_error_and_likelihood:113` | 0.5 (D/H sigma) | cosmogenesis | GENUINE (x3) |
| 8 | `P15_the_licensed_configuration…:282` | -0.0636 | CR_cosmology | GENUINE (x10) |
| 9 | `S1_the_banked_spectra…:102` | 5.7 | CR_cosmology | COINCIDENTAL: the paper's 5.7 is a per-cent excess, not points per period |
| 10 | `P15_the_fit_has_the_controls_freedom…:296` | 56.4 | CR_cosmology | GENUINE (x30) |
| 11 | `P15_the_shared_fraction…:261` | 0.66 | cosmogenesis | COINCIDENTAL: `width=0.66\textwidth` |
| 12 | `S1_the_third_point…:124` | 3.4 | boundary_paper | COINCIDENTAL: a bibliography `\S3.4` |
| 13 | `P15_zonset_determinations:51` | 301.76 | CR_cosmology | GENUINE (x2) |
| 14 | `B4_the_intercept_is_a_phase…:172` | 0.62 | matter_sector | COINCIDENTAL: `width=0.62\textwidth` |
| 15 | `P03_the_interior_mass_function…:310` | 0.01 | CR_synthesis | COINCIDENTAL: an exact ratio identity |
| 16 | `P16_the_interior_to_observed_mode_map:54` | 7.8 | cosmogenesis | GENUINE (x6) |
| 17 | `P15_the_licensed_configuration…:282` | -0.0075 | CR_cosmology | GENUINE (x10) |
| 18 | `P02_the_approach_is_mass_free:153` | 3.32 | CR_framework | GENUINE (x4) |
| 19 | `P15_verify_coherence_comb:59` | 296 | CR_cosmology | ARGUED: `abs(_dell - 296.29) < 0.05` stands one line above |
| 20 | `P15_the_fit_has_the_controls_freedom…:290` | 278.8 | CR_cosmology | GENUINE (x30) |

**Totals: 11 GENUINE, 8 COINCIDENTAL, 1 ARGUED.**  That is 40% COINCIDENTAL, against the 25% "cheap" bound fixed
in `PREDICTION.md`.  Three of the eight are layout or bibliography numbers (`\textwidth`, `\S`), which a context
filter could drop.  *That observation is post hoc.  It is not tested here, and it is named only as the next measurement.*
