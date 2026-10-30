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

---

## ⓸ `P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switch_sweep_finds_no_further_shadow`

**Re-pointed and green: `rc=0`, 46 PASS, 0 FAIL, GATES ALL PASS.** Two pins moved; **both were absolute
numbers cut to the old arm, and both are re-cut SCALE-FREE rather than widened.**

| figure | old arm | arm of record |
|---|---|---|
| largest band-by-band shift difference | `0.174` multipoles | **`0.1853`** (bound `< 0.20`, unchanged) |
| extremum-averaged `d_l/l_A` difference | `1.70e-4` | **`3.9213e-4`** |
| the shift itself, `d_l/l_A` | `0.032543` | `0.032543` (control) / **`0.032151`** (arm) |
| envelope rise, control / arm | — | `1.257337` / **`1.259682`**, difference **`+2.3447e-3`** |
| **contrast** difference — the quantity Delta IS | — | **`−6.80e-4`** |

**⇒ The claim survives, and the pins were the wrong shape.** *"The free-streaming shift is common to the
two arms, so it is not a candidate for Delta"* is a statement about **smallness relative to the shift**,
but the pin read `_fd < 2e-4` — an absolute number that happened to fit the old arm. On the arm of record
the arms' shifts agree to **`3.9213e-4`, which is `1.2%` of the `0.03254` shift**, and the envelope
difference is **`0.9%` of the `0.257` rise**.

⌗ **So this is not a loosened pin, it is a corrected one.** Each is now pinned BOTH on the measured value
to the pin rule (`2e-7` and `1.2e-6`) **and** on the scale-free inequality (`< 2%` of the shift, `< 1%` of
the rise). ⇒ *The absolute tolerance it replaces was `2e-4`; the new pin on the same quantity is `2e-7`,
a thousand times tighter.* The **contrast** difference keeps its absolute bound untouched, because that is
the quantity the claim is actually about and it has not changed character (`−6.8e-4` against the stated
`6e-4`, and the receipt's prose is corrected to `6.8e-4`).

**PERTURBED UNTIL RED:** the pointer reverted to the old arm gives `_fd = 1.70e-4` and both pins go
**RED**. ⌗ *And `1.70e-4` is inside the old `2e-4` bound — so the perturbation also confirms the old pin
was correct for the old arm.*

**⚑ And it IMPROVED the corpus's pin coverage.** `check_figures_pinned` then reported
`[STALE] P15 0.0004 cites …the_free_streaming_knob… -- now pinned or gone`: P15 prints `0.0004` beside
this receipt, and the tightened pin now **covers** it where nothing did before. The gate's own rule is
that *"a baselined one that comes to be pinned is STALE and fails, so the baseline can only shrink"*, so
`--write-baseline` was run **after reading the one row it names**: `1383 → 1382`, one row deleted.

---

# ⛔ THE HELD SET: `41` OF `44`, EVERY ONE WITH A NAMED REASON AND A ROUTER

| n | held on | receipts |
|---|---|---|
| **23** | `r7637_70_own_comb_statistic` — **as ordered** | the band-ratio / band-1-step family |
| **6** | **the response grids, not banked at the arm of record** | `de_tilted`, `full_range_refit`, `no_fit_confrontation`, `phase_slope`, `refit_leaves`, `refit_bound_figures` |
| **3** | **three `cr` spectra not in the bank** | `a_source_with_no_physics`, `contrast_excess_is_symmetric`, `locator_is_good` |
| **3** | **the comb-period mechanism, reaching past the family** | `acoustic_contrast`, `there_is_no_phase_residual`, `cross_term` |
| **2** | **a spectrum that is a different measurement** (`DPSRC` wired after its namesake was banked) | `model_difference`, `source_decomposition` |
| **2** | **the re-point dissolves the receipt's own subject** | `crossing_spectrum`, `133_bin_pair` |
| **2** | **P15 prints the figure, and no seat edits P15** | `monopole_zero_point`, `three_quarters` |

## ⛔ THE COUPLING THAT CAPS THIS ORDER: A RECEIPT'S FIGURES AND P15's ARE ONE OBJECT

**Measured, not argued.** `40` of my `44` are cited in `corpus/CR_cosmology.tex`, and for **13** of them the
citing sentence **prints a figure**. `check_figures_pinned` enforces the join: *"does a figure a citing
sentence prints fail its receipt when it is wrong?"*

I found this the hard way and report it as such. **`monopole_zero_point` was re-pointed GREEN — `rc=0`, 22
PASS — and it still had to be reverted**, because P15 prints `1.040` citing it, the arm of record makes
that `1.044`, and moving the receipt's pin left the paper's sentence unpinned:

```
[UNPINNED] P15              1.040  cites P15_the_monopole_zero_point_…  (+2)
[UNPINNED] CR_cosmology.tex 1.040  cites P15_the_monopole_zero_point_…
1386 unpinned figure(s) …; baseline 1383
```

⇒ **A green receipt is not a completed re-point.** The honest options were to print `1.044` in P15 — which
*"No seat edits P15"* forbids — or to pin `1.040`, which is **false** on the arm of record. So the receipt
is reverted and held. ⌗ *`free_streaming` shows the benign direction of the same coupling: there the
re-point made the paper's figure MORE pinned, and the baseline shrank.*

⇒ **This is the cap on step ⑴, and it is structural rather than a shortfall of effort.** The arm of record
moves figures the paper prints; the receipts and the paper have to move together, and only one seat can
authorise the second half.

## ⌗ TWO SMALLER THINGS FOR `70`

- **`r6784_cr_crossing_hier_leafrec1`'s manifest `held` note says *"here the arm of record (68.62,
  0.2973)"*.** Its own `point` and `switches` say `CRH0 = 68.570730`, `CROM = 0.291246`. The parenthetical
  names the crossing configuration's background, not the arm of record — a wording slip in the manifest,
  not a wrong run.
- **`r6911_source` is the one family where the CONTROL also moves** (the `SRCXS` re-point), so a receipt
  reading it needs a **per-file** map and not the per-arm `AOR` the others use. Worth a line in
  `RECIPES.md` so no seat applies `{'lcdm': '', 'cr': '_leafrec1'}` to it by habit.

## ⌗ AND ONE INSTRUMENT I BUILT, TRIED AND THREW AWAY

To predict *which* of the 13 figure-printing receipts the coupling would block, I wrote a cheap test:
does a figure P15 prints appear in the receipt's old output but not its new one? **It reported "no printed
figure left the output" for `monopole_zero_point` — the one case I had already PROVEN blocked**, by
running the gate and watching it go from `1383` to `1386`.

⇒ **The test was blind, and in the one direction that mattered.** It checks whether a literal string moves
in the output; the gate checks whether the **receipt still pins the figure**, and a figure can sit in the
prose as a quoted reference while the pin underneath it moves. ⇒ *Discarded, and recorded here so no seat
reaches for it.* **The only valid test is the empirical one: re-point, run `check_figures_pinned`, read
the verdict** — which is what each of the four re-point attempts above went through.

⌗ *Third blind instrument caught this revision, after the shallow-clone `--follow` at `r7635` and the
dry-run `[FAIL]` column above. All three were caught the same way: by asking whether the answer **varied**
where it should, not whether the thing ran.*

---

# ⛔ CORRECTION: `shared_fraction` IS REVERTED TOO. THE COMPLETED COUNT IS `2`, NOT `3`

**I reported three receipts re-pointed green. It is two.** `shared_fraction` had to come back out, for the
same reason as `monopole_zero_point`, and CI caught it where my pre-push set could not.

**What failed.** `fast` → **`check_marker_transposition`** on head `fefb48bbe`, with **2 NEW
TRANSPOSITION FLAG(S)** against a baseline of 61:

```
[FAIL] CR_cosmology.tex:1101  105 -- none of the group closing it carries it
```

**Why, read off the paper's own line.** `CR_cosmology.tex` l.1098–1101 says *"this arm exceeds it by
$105$ in $\chi^{2}$ and the model difference alone carries $77$ of that … and the factor of $1.3$"* and
closes that sentence with `\rcpt{P15_the_shared_fraction_…}` — **citing the very receipt I re-pointed.**
The old receipt carried `105.1` twice; mine carried it **zero** times, because the arm of record moves the
excess to `109.02` and the model difference to `81.8`. ⇒ **The paper's `105` was left computed nowhere**,
which is precisely what that gate is for.

⇒ Completing this re-point needs P15 to print `109` and `82`. *"No seat edits P15."* ⇒ **Reverted**, and it
joins the figure-coupled hold.

**So the cap is not an edge case: it blocked 3 of the 4 receipts I could otherwise have finished** —
`monopole_zero_point` (caught by `check_figures_pinned`), `shared_fraction` (caught by
`check_marker_transposition`), `three_quarters` (caught before editing). **Question ⑴ to `69` — may the
figures P15 prints move with the arm — is the gate on this whole order, not a side request.**

## ⚠ AND WHY MY PRE-PUSH SET DID NOT CATCH IT — THE REAL LESSON OF THIS REVISION

**`check_marker_transposition` is LEAN-skipped by `turn_gates.sh`** (*"heavy, and CI's fast job asks it on
every push"*) **and, run locally, it DECLINED outright:**

```
[FAIL] the calibration commits are not in this clone -- a gate that cannot re-find the
       two errors that made it does not pass.  (CI checks out with fetch-depth 0.)
```

⇒ So the gate was invisible twice over: not in the lean batch, and unable to answer on a shallow clone.
**My pre-push set held ~10 gates; CI's `fast` job runs 63.** That gap is the whole explanation.

**Both halves are now fixed, not noted:**

⓵ **The clone is unshallowed** — `git fetch --unshallow`, **612 → 6626 commits**. Every gate in the
standing "known environment class, red locally and green in CI because this clone is shallow" now
*answers* here: `check_marker_transposition`, `check_pdf_current`, `check_pins_adjudicated_on_mint`,
`check_quote_pins`'s history seed.

⓶ **The pre-push set is now CI's own list.** All **63** of `fast`'s gates run locally, each on its own exit
code, as the workflow runs them (`NODE=ci`): **ran 63, ALL GREEN** on this head with the revert in.

⌗ *`check_marker_transposition` re-measured after the revert: `rc=0`, **61 flags against 61 adjudicated** —
baseline restored, and on a gate that could not previously be asked here at all.*

## ⚑ AND THE AUTHORSHIP LIMITATION I FLAGGED TWICE IS NOW CLOSED

At `r7635` and again at `r7637+cc66.1` I reported that `git log --follow` was **blind** in this container —
it returned the seat `71` for all 66 receipts because the clone was shallow — and that the provenance
column was therefore *"the only instrument that works here."* **With full history it works, and it
agrees:**

| | |
|---|---|
| census receipts cross-checked | **66** |
| **AGREE** with the provenance column | **45** |
| **DISAGREE** | **0** |
| creating commit carries no `+seat` tag | 21 |

Creating-commit tags: **`cc66` 42**, `70` 3, untagged 21. Of the untagged, I claim exactly **2** —
`133_bin_pair` (`r7109`, added in a **merge** commit, which is why `--diff-filter=A` skipped it) and
`crossing_spectrum` (`r6788`, and `r6788+cc66.17/.18` appears elsewhere in the corpus). ⇒ **42 + 2 = 44,
with zero conflicts.** The share `69` ruled and I derived from the provenance column is confirmed by a
second, independent instrument.

⌗ **And my first run of that cross-check was itself a blind instrument**, which is worth recording because
it nearly went into a reply: it tested `seat == 'cc66'` against strings like `cc66.42`, so it reported
**42 disagreements** where there were none. Caught by reading the rows it printed — every "DISAGREE" line
said `--follow=cc66.NN` beside `provenance=mine`, which is agreement. ⇒ *Fourth blind instrument this
revision. A checking script is not exempt from the rule it is checking.*

## ⚑ AND THE STANDING LOCAL "BASELINE" OF TWO FAILURES WAS NEVER A STATE — IT WAS THE CLONE

Every revision this seat has reported `turn_gates` as **`PASS=121 FAIL=2`**, calling
`check_branches` + `check_pins_adjudicated_on_mint` *"the shallow-clone pair"* and treating it as the
tree's baseline. On the unshallowed clone, same tree, same head:

```
turn batch (lean): ran 123 of 123 expected
PASS=123  FAIL=0  UNRUN=0
```

⇒ **Both were artefacts of the clone and neither was ever a real failure.** The lean batch is green for
the first time, and the useful consequence is that **a FAILURE in it now means something**: the rule
*"a third failure is new"* can be replaced with *"any failure is new."*

⌗ *This is the cost of a declining gate being filed as a baseline rather than as an unanswered question.
Two gates spent weeks counted as known-red when the honest reading was "this container cannot ask them."*
