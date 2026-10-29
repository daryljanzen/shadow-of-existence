# `r7637+cc66` — RESULT: the re-point of my share on the arm of record, receipt by receipt

*Every figure below is **re-derived on the instrument in this container**, not quoted from `DRYRUN.md`.
Versions match `requirements-ci.txt` exactly (`camb 2.0.4`, `numpy 2.4.6`, `scipy 1.17.1`,
`sympy 1.14.0`, `mpmath 1.3.0`). Each moved pin is **perturbed until it goes red** before it is reported.*

**How a re-point is expressed, and why.** Each receipt names its arm-of-record spectrum explicitly, via a
per-arm suffix map — `AOR = {'lcdm': '', 'cr': '_leafrec1'}` — rather than the namesake file being
overwritten. ⌗ *This is derived from the order rather than assumed: `r7637` asks for a **partial**
re-point — 18 now, 23 held until `r7637_70_own_comb_statistic` lands. A wholesale swap of the namesake
spectra cannot be partial, and would drag the held family onto the new arm too, which would defeat the
hold. So the move has to be per receipt.* The control carries no suffix because the control does not move.

---

## ⓵ `P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_trough_pattern_is_the_arms_alone`

**Re-pointed and green: `rc=0`, 14 PASS, 0 FAIL.** One pin moved; it is re-derived, tightened, and shown
failable twice.

| figure | old arm | arm of record |
|---|---|---|
| shared fraction | `73.1%` | **`71.8%`** |
| cosine of the whitened residuals | `+0.855` | **`+0.848`** |
| arm's excess over the control | `+105.08` | **`+109.02`** |
| of which the model difference carries | `77.3` | **`81.8`** |
| the cross term | `+27.8` | **`+27.2`** |
| arm chi² over 179 bins | `282.96` (`1.581`/bin) | **`286.89`** (**`1.603`**/bin) |
| ‖m_CR − m_control‖ | `8.79` | **`9.04`** |
| ‖r_CR‖ | `16.82` | **`16.94`** |
| ‖r_control‖ | `13.34` | `13.34` (the control does not move) |
| diagonal: corr / slope / **rms ratio** | `+0.8373` / `1.137` / `1.357` | **`+0.8240`** / **`1.145`** / **`1.388`** |
| whitened: corr / slope / rms ratio | `+0.8548` / `1.078` / `1.261` | **`+0.8478`** / **`1.076`** / **`1.269`** |
| peak/trough, diag · whitened | `+0.36/−0.51` · `+0.42/−0.52` | **`+0.38/−0.56`** · **`+0.42/−0.56`** |

**⛔ THE ONE PIN THAT MOVED, AND WHAT IT COSTS ME.** The receipt pinned *"the RMS RATIO reproduces (1.36
against 1.34)"* at `|x − 1.34| < 0.03`. On the arm of record the ratio is **`1.388`**, which is `0.048`
from `r6881`'s quoted `1.34` — **outside the band**. ⇒ *So of `r6881`'s four diagnostics, the one that
reproduced on the old arm no longer does, and **none of the four survives**.*

**I did not widen the tolerance to keep it green**, which is the one move this pin forbids. The claim is
re-worded to what is measured and the pin is re-cut on the measured value to `7e-4`
— `max(0.5·10^-3, 5e-4·1.388)`, the pin rule — **and** on its distance from `1.34`, so it cannot be
satisfied by a drift back toward the quoted number.

⇒ **This strengthens the receipt's verdict rather than weakening it**: its headline is that `r6881`'s
composite reading fails at its premise, and on the arm of record it fails more completely.

**PERTURBED UNTIL RED, twice and independently:**

| perturbation | rms ratio | pin |
|---|---|---|
| the pointer reverted to the old arm | `1.357` | **RED** |
| a shape tilt of `dn_s = +0.0005` on the arm only | `1.384` | **RED** |
| `dn_s = +0.001` | `1.380` | **RED** |
| a pure rescale of the arm by `×1.0012` | `1.388` | green — **correctly** |

⌗ *The rescale cannot move it and should not: the receipt re-fits the amplitude
(`A = mb·F·D / mb·F·mb`), so a multiplicative perturbation is degenerate and is absorbed. **A pin that
survives a rescale is not thereby a weak pin — it is a pin on shape**, and the tilt at `5e-4` shows how
tight it actually is. I record the degenerate direction because trying it and reporting only the
perturbation that worked would have overstated the test.*

**And the quoted claims were left alone.** `cc66.33`'s withdrawn sentence (*"73.1 per cent … is the
TRANSFER'S"*) and `r6881`'s quoted `corr 0.96, slope 1.28, rms ratio 1.34` are **historical quotations**;
only the receipt's own current measurements move. ⌗ *Six of the hardcoded `73.1`s in this file are
quotation and five are measurement, and editing the wrong ones would have falsified a withdrawal.*

---

## ⓶ `P15_the_monopole_zero_point_is_not_the_channel_and_the_two_residuals_point_opposite_ways`

**Re-pointed and green: `rc=0`, 22 PASS, 0 FAIL.** Two arm reads moved to `cc66_r185_verify_cr_leafrec1`;
the two control reads stay, because the control does not move.

| figure | old arm | arm of record |
|---|---|---|
| the contrast statistic, arm against control | `1.04015` | **`1.04403`** |
| the control against itself | `1.00000` | `1.00000` (exactly, both arms) |
| alternation `a` | — | `+0.031560` |

**⇒ Independent confirmation of `70`.** `r7635+70` registered the contrast ratio band `[1.02, 1.07]` and
reported `1.040 → 1.044`. Measured here from the bank on this receipt's own statistic: **`1.04403`**. ⌗
*Two seats, two code paths, the same number — which is the point of re-deriving rather than quoting.*

**The pin.** It asserted *"reproduces `cc66.35`'s `1.0401`"* at `< 0.0005`. On the arm of record the
contrast has **moved off that value by `0.0039`**, so the claim is re-worded to what is measured: the
statistic is still `cc66.35`'s — *the control against itself is still exactly one, which is the machinery
check that matters* — and it now reads `1.04403`, inside the band `70` registered. ⌗ *The tolerance is
unchanged: the pin rule gives `max(0.5·10^-5, 5e-4·1.044) = 5.3e-4`, which is the `5e-4` the old pin
already carried. **Only the centre moves**, so this is not a loosened pin.*

**PERTURBED UNTIL RED:** the pointer reverted to the old arm gives `1.04015` → **RED**. ⌗ *And that
number is `cc66.35`'s `1.0401` to five digits, so the perturbation also confirms the old pin was correct
for the old arm — the pin moved because the arm did, not because the statistic drifted.*

---

## ⓷ `P15_the_signature_collapses_at_the_adjudicated_ratio_and_the_endpoint_sets_its_sign`

**Re-pointed and green: `rc=0`, ALL CHECKS PASSED. No pin moved.**

| figure | old arm | arm of record |
|---|---|---|
| the base spectrum's `D_M` | `14011.5` | **`14134.0`** |
| its `l_A` | `301.80` | **`302.94`** |

⚠ **And what I deliberately did NOT move.** This receipt's analytic core runs `machinery()` at the
**adjudicated** background `(68.60, 0.2973)`, which is **a different object from the arm of record**
`(68.5707, 0.291246)`: the first is a corpus adjudication, the second a refit minimum. The receipt's whole
subject is *the ratio at the adjudicated background*. ⇒ **Re-pointing the spectrum it reads `D_M` and
`l_A` from is a re-point; moving the adjudicated point would change what the receipt is about**, so it is
left where it is and flagged here. If `69` wants the ratio re-derived **at** the arm of record that is a
new reading rather than a re-point, and I will take it as one on a word.

---

# ⛔ THREE FURTHER DEPENDENCIES, FOUND BY MEASURING AND NOT BY READING THE MAP

`r7637` asks for 18 of my 44 now. **Measurement cuts that to 12**, and the three reasons are each a gap in
something other than the §B spectra — none of them visible in `DRYRUN.md`.

## ⒜ THE REFIT RESPONSE GRIDS ARE NOT BANKED AT THE ARM OF RECORD — blocks 4

`computations/beyond_the_wall/refit_grid` (24 files) and `refit_grid185` (23 files) hold the local
response grids — `cr_base`, `cr_H0p/m`, `cr_OMp/m`, `cr_WBp/m`, `cr_NSp/m` — and **not one has a
`_leafrec1` counterpart**. Four of my receipts read one:
`P15_the_full_range_refit_…`, `P15_the_refit_leaves_…`, `P15_the_refit_bound_figures_…`,
`P15_the_no_fit_confrontation_…`.

⇒ The response model is on the **old** arm while the verify spectrum is on the **new** one, and that is
exactly what the `+11.1` in `P15_the_refit_leaves_…` is: *"the verified chi² is +11.1 from the model's"*
(`170.6` predicted, `181.7` measured). **A response grid centred on the old minimum is the wrong grid for
a minimum that has moved**, and rebuilding it is nine production runs per arm — `70`'s kind of work, not
a thing to fake from the files present. **Routed.**

## ⒝ TWO P15 FIGURES' BANKED NUMBERS ARE ON THE OLD ARM — blocks 3

`P15_three_quarters_…`, `P15_the_no_fit_confrontation_…` and `P15_the_phase_slope_…` each gate against a
banked figure-number file (`cc66_fig_acoustic_numbers.npz`, `nofit_figure_numbers.npz`) with a check whose
whole purpose is *"so the figure and this receipt cannot drift apart."* Re-point the receipt and the gate
correctly fires: `cr_chi2 282.95613` figure against `286.89412` receipt, and four more MISMATCHes.

⇒ Completing those re-points means **regenerating a P15 figure** and its banked numbers with
`corpus/make_fig_acoustic_two_arm.py`. The order ends *"No seat edits P15."* ⇒ **I am not regenerating a
paper figure on my own authority.** One word from `69` and it is half an hour's work. **Routed.**

## ⒞ ⚠⚠ ONE BANKED SPECTRUM IS A DIFFERENT MEASUREMENT FROM ITS NAMESAKE — blocks 2

This is the sharpest of the three and it is not an absence but a **substitution**.

`r6885_dp0_cr_leafrec1` was rebuilt from the recorded command in `r6885_directions/launch.sh`, which is
correct procedure. **But the instrument moved underneath that command.** Measured:

| run, against the plain refit spectrum | old arm | arm of record | |
|---|---|---|---|
| `r6885_dp0_cr` | **`0.000e+00`** | **`2.270e-01`** | ⚠ inert then, **ACTIVE now** |
| `r6885_los_cr` | `1.253e-01` | `1.251e-01` | unchanged |
| `r6885_losdp0_cr` | `2.565e-01` | `2.539e-01` | unchanged |
| `r6885_lossw0_cr` | `8.409e-01` | `8.410e-01` | unchanged |
| `r6889_nufs0_cr` | `1.345e-01` | `1.355e-01` | unchanged |

**Exactly one file, and the instrument's own source says why.** `ACOUSTIC_two_arm.py` l.1277: *"so
`DPSRC=0` there returned a BIT-IDENTICAL spectrum on both arms (r6885+cc66.35)"*; l.1782: *"`_SWSRC` and
`_DPSRC` **WIRED HERE at r6889+cc66.36**."* The namesake was banked at `r6885` — **before** the wiring, when
`HIER=1` did not take the path the switches sat on. The rebuild ran the same command through the
**post-wiring** instrument, so `DPSRC=0` now removes the Doppler dipole for real: `−10%` at `l=220`,
`−41%` at `540`, `−60%` at `1900`.

⇒ **`r6885_dp0_cr_leafrec1` is not the namesake moved to a new arm; it is a different measurement.** Two
of my receipts pin that bit-identity as *"the signature of an unwired knob"* — a **historical** finding
about the `r6885`-era instrument, which both receipts' own prose already documents the wiring of. **A pin
on history cannot be re-pointed onto a post-wiring run**, and restating it is a change of claim rather
than a re-point. ⇒ `P15_the_model_difference_…` and `P15_the_source_decomposition_…` **held for `69` to
rule.** ⌗ *The `6.8e-13` thread-count wobble `70` gated at `1e-11` is a different thing entirely; this is
`2.3e-1` and it is physics, not summation order.*
