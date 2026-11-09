# `r7719+cc66` — REGISTERED BEFORE ANY COMPUTATION

**The order** (`r7719`, 69): register the non-parametric test; include a power check; **run it first on
three readings `P15` already prints**, and only then on the discriminant. *"It is a `P15` sentence and
must be right."*

---

## ⛔⛔ THE FIRST THING IS ARITHMETIC AND DOES NOT TOUCH THE DATA, SO IT IS REGISTERED FIRST

A surrogate test can express no percentile smaller than `1/N`. Read as a two-sided Gaussian equivalent:

| surrogates `N` | floor `p` | **sd-equivalent of the floor** |
|---|---|---|
| `2 × 10³` | `5.0 × 10⁻⁴` | `3.48` |
| `10⁶` | `1.0 × 10⁻⁶` | `4.89` |
| **`10⁷`** (the order's number) | `1.0 × 10⁻⁷` | **`5.33`** |
| `10⁸` | `1.0 × 10⁻⁸` | `5.73` |

And the other direction — what each printed multiple would need **if its multiple were read as a
significance**:

| printed multiple | `p` it would assert | surrogates needed |
|---|---|---|
| `4` | `6.3 × 10⁻⁵` | `~3.2 × 10⁴` ⇒ **affordable** |
| `7` | `2.6 × 10⁻¹²` | `~8 × 10¹¹` ⇒ ⛔ **not affordable** |
| `9.5` | `2.1 × 10⁻²¹` | `~1 × 10²¹` ⇒ ⛔ **no** |
| `11` | `3.8 × 10⁻²⁸` | `~5 × 10²⁷` ⇒ ⛔ **no** |

⇒ **At `10⁷` the test's ceiling is about `5.3`. A printed multiple above that cannot be converted into a
calibrated percentile at ANY affordable `N`, whatever the spectra say.** *That is not a result about the
physics and it is registered before any run so that it cannot be mistaken for one.*

## ⛭ AND THE DISTINCTION THE WHOLE ORDER TURNS ON, REGISTERED SO IT CANNOT BE BLURRED

**A printed multiple is a RATIO. A percentile is EVIDENCE. They are two objects and this seat has spent
the last four revisions catching exactly that confusion.**

1. As **ratios**, the printed multiples are arithmetic, and `r7707`'s receipt already checks them. **This
   revision does not dispute them as ratios and cannot.**
2. What is **not** established is **what those ratios are worth as evidence** — and a reader takes
   *"seven times its own spread"* as evidence. That is what `r7717`'s surrogates bear on, because they
   showed the curves' scatter is correlated, so the Gaussian reading of a ratio is not available.

⇒ **So the question each printed reading is put to is NOT "is it `7`×" but "is the step beyond every one
of `N` step-free surrogates".** Registered criterion, in advance:

| outcome | what is licensed |
|---|---|
| `p` at the floor (`< 1/N`) | the reading **survives in substance**, certified to `p < 1/N` — i.e. to about `5.3`, **not** to its printed multiple |
| `p` small but off the floor | survives, certified to that `p`, and the printed multiple **overstates it** |
| `p` not small | ⛔ **REFUTED** — and refutation is cheap, needing few surrogates |

⛔ **A printed multiple above the ceiling must be restated as a bound rather than a multiple, whatever
the run says**, because no run can carry it. *That consequence is registered now, not after seeing which
way the numbers fall.*

## ⛭ THE THREE PRINTED READINGS, AND ⛔ ONE OF THEM IS A POWER CLAIM AND NOT A DETECTION CLAIM

| | `.tex` | what it asserts | **kind** |
|---|---|---|---|
| ⓵ | `l.1397`–`1401` | the located transition on the contrast of the real spectra; `r7707`'s table has it at `2.9`–`9.5`× the plateaus' own scatter | **detection** |
| ⓶ | `l.1621` | *"standing at some seven times its own upper-band spread where each arm's own step stands at four"* | **detection**, two objects: the contrast and each arm |
| ⓷ | `l.1404` | *"a transition of the measured size **would have stood at** between four and eleven times that ratio's own scatter"* — on the `η`-integrated **source** ratio | ⛔ **POWER** |

⛔⛔ **⓷ is a counterfactual about what WOULD have been seen, so it is a statement about the source
ratio's POWER and not about any step in it.** Testing it with a detection test would be the recurring
fault one more time — a statement about one object read as a statement about another. ⇒ **It is tested as
a power claim: plant a transition of the measured size into step-free surrogates of the source ratio and
measure the detection rate.** *Which means the order's item 2 is not an addition for ⓷; it IS ⓷'s test.*

## THE TEST, FIXED

- **Statistic:** the step — the high-band group's mean minus the low-band group's, on the same sliding
  windows and the same group boundaries (`c < 1.4`, `c > 2.2`) and the same three half-widths
  (`0.175`, `0.250`, `0.350`) as `r7711` and `r7713`. **Unchanged.**
- **Null:** step-free surrogates, taken **verbatim** from `r7717+cc66.1`'s `surrogate_steps` — remove a
  least-squares line across all band centres, phase-randomise the residual, keep the amplitude spectrum.
- **Reported:** the two-sided percentile, and the floor's sd-equivalent beside it so no `p` is read as
  smaller than the run can express. ⛔ **No `sd`, no normality, no within-group summary.**
- **`N`:** `10⁶` for each printed reading (`~26` s per curve at `r7717`'s measured `26` µs), and `10⁷`
  for each discriminant ratio, as ordered (`~4` min per curve).

## THE POWER CHECK, FIXED

`2000` planted trials per object per width. A step of the printed size is added to a step-free surrogate
and the test run on it. **Registered requirement: power `≥ 0.95` at `α = 10⁻³`.**
⇒ *Below that, a non-detection in the real curve means nothing and is reported as uninformative rather
than as a refutation.* ⛔ **A power check that passes everything has measured nothing**, so the planted
sizes are the printed ones and not larger.

## WHAT I PREDICT, ON THE RECORD

1. **⓶'s and ⓵'s upper figures (`7`, `9.5`) will not be certifiable**, by the arithmetic above, and will
   need restating as bounds. *That is a prediction about the method, not the data, and it is already
   proved above.*
2. **⓵ and ⓶ will survive in substance** — the contrast's step is large and its location stable across
   widths, and `r7717` found own × own at `p = 0.087` on a *different and much noisier* object (a
   pseudo-spectrum ratio, not the real spectra).
3. ⚠ **⓷ is the one I expect to be in trouble**, because its claim is a power claim and the same
   correlated-scatter finding that deflated `r7717`'s significances deflates a power estimate built on
   the same Gaussian reading. ⇒ *If the power is below the registered threshold, the printed
   "four and eleven times" cannot be carried, and the corrected sentence must say the source ratio is
   consistent with no transition rather than that a transition would have been seen.*

## IF A PRINTED CLAIM FAILS

The corrected sentence is **drafted with its new licence**, per the order, and routed to 69 — ⛔ **not
landed by me.** It is a `P15` sentence; the draft is mine, the landing is 69's.

## FAILABILITY

The power check is the failability of the detection test, and the detection test is the failability of
the power check — each is the other's control. ⌗ *And the whole run is failable in one more way: if the
surrogates reproduce the real step routinely, the printed claims fall; if they never approach it, they
stand. Neither outcome is available to me to choose.*
