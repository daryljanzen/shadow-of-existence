# r7095 (70) — configuration as a property of the artefact; the locator's substrate; the default-model figures by figure

*Pre-registered before any count, backfill or re-validation is computed. The order is `FOR_70.md` `r7095`, Q1–Q3. **Nothing is run through the transfer.** No prose is edited, no other seat's receipt is touched, and `ACOUSTIC_two_arm.py` is not changed: the save-time half of Q1 is **specified**, not edited in.*

## Q1 — the specification, and its cost on the existing bank

**Measured:**
- the banked artefacts in the repository: 215 `.npz`, being 175 in `spectra/`, 20 in `refit_grid/` and 20 in `refit_grid185/`;
- for each, whether it carries a switch set;
- whether it can be backfilled, graded by source:
  - **COMMAND**: a launcher or a README row names its exact command;
  - **FINGERPRINT-ONLY**: ℓ_A and r_s place it in a configuration, but no command exists;
  - **NONE**.

A prototype gate, `check_banked_config.py` beside this file, applies the proposed rule in report mode. It is **not** registered, since registering a gate is 66's call.

**Predicted:**
- **all 215 fail** the proposed gate today, because no `.npz` records switches (already seen);
- backfill by **COMMAND for 80–90 %**, **FINGERPRINT-ONLY for 5–15 %**, and **NONE for under 5 %**;
- `cc66_cr_x_lstep1` among the NONE or FINGERPRINT-ONLY;
- the non-spectrum `.npz` (`r6959_eta_cr`, `cc66_fig_acoustic_numbers`, the `r7041_accept_*` digests and the like) cannot be fingerprinted on ℓ_A, so they fall to COMMAND or NONE.

## Q2 — the locator, on a re-derivable substrate

The validation is `P15_the_full_range_refit_…`'s step (a): the sub-bin locator on a fine-grid spectrum, compared with the same spectrum decimated ×2, ×4 and ×8. **The conclusion under test:** "at the grid the refit runs on, the RAW locator errs by about 3 in ℓ and the refined one by under 0.2."

The candidate substrate is a banked spectrum **with a launcher** at the finest ℓ spacing available, read for its spacing first. The order's suggestion, a refit-grid base, is at LSTEP = 8, so it cannot be decimated to the ×8 test of an LSTEP = 1 base. That is checked, not assumed.

**Predicted:** a recorded-command fine-grid spectrum exists (`r6941_fine_*` is the likely one), and **the conclusion is unchanged on it**: raw error > 2 and refined error < 0.2 at ×8. If the finest recorded substrate is coarser than LSTEP = 2, **the test cannot be reproduced at ×8**, and I will say so.

## Q3 — the 13 default-model figures, by figure

For each of the census's 13 rows: the figure as printed, the receipt that **carries** it (source, or output on a fresh run of the cited receipts — they read banks only), whether it is a CR-arm figure on model A or a control figure (no CR switch applies), and whether `P15` compares it **against** a figure from the reported model B.

**Predicted:**
- most of the 13 are **control figures** or **window artefacts** of the `r7043` marker rule (numbers from the adjacent "two likelihood configurations" paragraph, which is B and the control);
- **at most four are model-A CR figures**: the polarisation pulls 10.9 % and 26.9 %, and the closed-form k-dependence;
- **zero to two are compared against a model-B figure.**
