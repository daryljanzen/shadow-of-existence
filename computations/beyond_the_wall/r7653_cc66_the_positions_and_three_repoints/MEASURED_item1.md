# `r7653` ⓵ — the arm of record's positions and heights by the matched locator (measured)

Raw measurements, banked here so they survive a container restart. The landed form is the pin in
`…at_its_own_preferred_H0…` and the table in `FOR_69.md`; this file is the working record.

## The locator is validated before anything is read off it

The matched locator run on the SKY returns **P₁/P₂ = 2.221, P₁/P₃ = 2.262** against the paper's own
published sky pair **2.217 / 2.277** (0.2 and 0.7 per cent). *A locator that could not find the sky's
own ratios would not be evidence about an arm.*

## Positions and heights, one procedure on all four rows (nW = 7 windows each)

| row | P₁/P₂ | P₁/P₃ | peaks (matched) |
|---|---|---|---|
| THE SKY, this locator | 2.221 | 2.262 | 220.98 / 533.79 / 814.79 / 1121.85 |
| control `L2000` | 2.204 | 2.225 | 220.44 / 537.29 / 811.06 / 1123.99 |
| namesake `L2000` | 2.274 | 2.336 | 221.11 / 538.63 / 815.49 / 1130.79 |
| **ARM OF RECORD, distances'** | **2.291** | **2.349** | 220.03 / 536.25 / 811.59 / 1125.11 |

Against the sky: control **−0.75 / −1.65** per cent; namesake **+2.40 / +3.24**; arm of record
**+3.16 / +3.82**.

## ⛭⛭ THE ASYMMETRY, which is the finding and not a figure

**The re-point moves the POSITIONS toward the sky and the HEIGHTS away from it.**

- the comb, by the procedure the sentence names: namesake **1 part in 134** → arm of record **1 part in
  429** — *better*;
- P₁/P₂ against the sky: namesake **+2.40%** → arm of record **+3.16%** — *worse*;
- and the CONTROL is nearer the sky than either arm on the heights (−0.75%), which is the direction
  l.146's "the heights are the path's and the positions are the construction's" already asserts.

## ⓵a The three statements, with each one's REFERENT established from the paper rather than assumed

⛔ *My registered prediction attached all three to arm-vs-sky. That was wrong for two of them, and the
error was in the referent and not the arithmetic. Recorded here rather than by editing the prediction.*

| statement | where it lives | what it actually compares | on the arm of record |
|---|---|---|---|
| "the first three peaks within a grid step of the measured ones" | l.148, the abstract | arm vs **sky**, first **three** peaks | ⛔ **FAILS**: offsets −0.95, **+2.46**, **−3.20** against a grid step of 2 |
| "within a multipole on every peak" | l.2074 | **hierarchy path vs line-of-sight path**, one arm | see ⓵c |
| "within one per cent on the heights" | l.2075 | the same two paths (2.273 vs 2.264 = 0.40%) | see ⓵c |

*So the second and third are two-instrument claims, not arm-vs-sky claims, and my prediction's ground
for the third — the namesake's 2.264 against the sky's 2.217 — was the wrong comparison entirely.*

## ⓵c The second instrument — ⛔ MY PREDICTION IS FALSIFIED, AND IT IS COMPUTABLE

I predicted the hierarchy path "CANNOT be" done on the arm of record for want of a bank. It is already
computed and pinned, in `…the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised`,
at `l_A = 302.9430505935752` — the distances' point exactly:

      hierarchy path, ARM OF RECORD   222.05 / 535.85 / 815.03 / 1129.74
      hierarchy path, namesake        221.96 / 536.10 / 815.40 / 1130.53

⌗ **Why I got it wrong, since the cause is reusable:** I searched `spectra/` by FILENAME PATTERN for
`*_leafrec1_distances` and reasoned from what the `h686` family happened to be called. The hierarchy
path's arm-of-record spectrum is not in `spectra/` at all — it is a GRID bank,
`refit_grid185_leafrec1_distances/cr_base.npz`, reached through that receipt's `GRIDS` map. **Keying the
search on a filename convention instead of on "which receipt computes this" is the same genus of error
as keying order detection on heading format**, which this seat has a standing warning about. My
falsifier was worded to match the convention too, so it would not have caught it either.

⌗ *And the two hier banks that ARE in `spectra/` (`r6784_cr_crossing_hier{,_leafrec1}.npz`) sit at
`l_A` ≈ 172 — the H0 = 73 crossing — so they are the wrong configuration for this table and are not it.*

## ⚠ One question for 69, flagged rather than asserted

On the **namesake**, the paper's own printed figures give hier-minus-LOS offsets of −0.04, **−1.90**,
**−2.60**, **−3.47** against l.2074's claim *"within a multipole on every peak"*. Read literally that is
already false in the sentence's own numbers. ⌗ *But the comparison basis is not obvious — sub-bin hier
against LSTEP=2 grid-snapped LOS is not clearly the comparison the claim intends — so I am NOT reporting
this as a defect until the basis is established. It is noted here so it is not lost.*

---

# `r7653` ⓵, part two — the table is PINNED, the second instrument is DONE, and the flagged question is ANSWERED

Landed in `…at_its_own_preferred_H0…` this turn. The locator now returns the parabola's **vertex value**
beside its vertex position, so the heights l.2075 claims come from the **same fit over the same seven
windows** as the positions l.148 claims, on the sky and on every arm.

## The whole table, one procedure, seven rows — every figure gated to its tabled digit

| row | peaks (matched locator) | comb 1–4 | 1–3 | φ/π 1–4 | 1–3 | P₁/P₂ | P₁/P₃ | geom ℓ_A |
|---|---|---|---|---|---|---|---|---|
| THE SKY | 220.98 / 533.79 / 814.79 / 1121.85 | 298.362 | 296.906 | −0.2448 | −0.2378 | 2.221 | 2.262 | — |
| the control, L2000 | 220.44 / 537.29 / 811.06 / 1123.99 | 298.441 | 295.308 | −0.2443 | −0.2292 | 2.204 | 2.225 | 301.375 |
| the namesake, L2000 | 221.11 / 538.63 / 815.49 / 1130.79 | 300.589 | 297.189 | −0.2494 | −0.2332 | 2.274 | 2.336 | 302.889 |
| **ARM OF RECORD** | **220.03 / 536.25 / 811.59 / 1125.11** | **299.057** | **295.782** | **−0.2488** | **−0.2331** | **2.291** | **2.349** | 302.889 |
| hier, the control | 220.45 / 537.31 / 811.04 / 1123.96 | 298.429 | 295.299 | −0.2442 | −0.2291 | 2.204 | 2.225 | 301.375 |
| hier, the namesake | 221.11 / 538.64 / 815.47 / 1130.76 | 300.578 | 297.180 | −0.2493 | −0.2331 | 2.274 | 2.335 | 302.889 |
| **hier, ARM OF RECORD** | **220.03 / 536.27 / 811.58 / 1125.02** | **299.029** | **295.773** | **−0.2486** | **−0.2330** | **2.291** | **2.348** | 302.889 |

φ/π is `fit_comb()[1] / π`, PART 1's own convention, so these rows and PART 1's are one quantity.

## ⓵c ANSWERED: the second instrument is computable and it is DONE

My prediction said it could not be; it is, through the **grid** bank
`refit_grid185_leafrec1_distances/cr_base.npz` (and `refit_grid185/{lcdm,cr}_base.npz` for the control
and the namesake), not through anything in `spectra/`. All three hierarchy rows are in the table above,
by the same locator as every other row.

## ⛭⛭⛭ AND THE QUESTION I FLAGGED FOR 69 IS ANSWERED IN THE CLAIM'S FAVOUR

l.2075 claims the two instrument paths agree **"within a multipole on every peak and within one per cent
on the heights"**. Read off the figures l.2072–2074 *prints* — hier `221.96 / 536.11 / 815.40 / 1130.53`
against "this path's" `222 / 538 / 818 / 1134` — the offsets are **−0.04, −1.90, −2.60, −3.47** and the
claim is false in its own numbers. That is what I flagged and declined to assert.

**The two are not one measurement.** The hier figures are located **sub-bin on a unit-step grid**; the
line-of-sight figures are **raw maxima on an LSTEP=2 grid, quantised to even ℓ**. The paper says so in
terms and then compares them anyway. ⇒ Put **both paths through the one matched locator** and they agree
to:

- **≤ 0.084 of a multipole** at every peak, on the namesake (`+0.00 +0.01 −0.02 −0.03`) and on the arm
  of record (`−0.00 +0.01 −0.02 −0.08`) alike;
- **0.011 %** on P₁/P₂ and **0.017 %** on P₁/P₃, on both arms.

⇒ **So the claim HOLDS, and comfortably — by more than a factor of ten on the positions and sixty on the
heights. What does not hold is the pair of figures offered as its evidence.** For 69: the repair is to
print the matched pair, or to say that the line-of-sight figures are grid-snapped and the comparison is
therefore an upper bound. *Neither is a defect in the physics; it is a mixed-basis comparison, which is
why it needed the basis establishing before it could be reported.*

## ⛔ THE LSTEP=2 TRAP, in its purest form, and it decides which figure l.813 can land

l.2073–2074 prints "this path's" peaks and heights from the **raw-grid** method `score()`. On the arm of
record that method gives:

| | peaks | comb | φ/π | P₁/P₂ | P₁/P₃ |
|---|---|---|---|---|---|
| the control | 220, 536, 814, **1128** | 297.0 | −0.2379 | 2.195 | 2.191 |
| namesake | 222, 538, 818, 1134 | 298.0 | −0.2349 | 2.264 | 2.298 |
| **ARM OF RECORD** | 220, 536, 814, **1130** | **297.0** | **−0.2379** | **2.281** | **2.312** |

**The arm of record's first three raw maxima land on the control's own LSTEP=2 cells**, so its three-peak
comb and its φ come out **bit-identical to the control's** while its heights do not, and only the fourth
peak separates them. ⇒ **So the arm-of-record figure for l.813's comb cannot come from this method.**
69's landed **299.1** is the matched locator's **299.057**, against the sky's matched **298.362** → 298.4
— a part in **429**, which is exactly the "part in four hundred" the order quotes. The raw grid's 297.0
is an artefact of where the cells fall.

## ⓺ l.2147's intercept, in the landed form

l.2147 prints **−0.2349 against the sky's −0.2405**. Those are the **namesake's raw-grid three-peak**
figures. The pair that goes with a landed comb of 299.1 is the **matched four-peak** one:
**−0.2488 on the arm of record against the sky's −0.2448** (three-peak: −0.2331 against −0.2378).
⇒ *For 69: item ⓵ and item ⓺ are one pair, as the order says, and they have to move to the same fit —
printing a four-peak comb beside a three-peak intercept would mix two fits inside one paragraph.*

## What PART 4B now does on 69's landing rather than before it

The provenance gate is a **disjunction over the two states l.813 can be in**, with the state PRINTED and
a figure that is neither failing:

- **ⓐ the namesake state** (today): l.813 prints `298.0`, which is the namesake's raw-grid three-peak
  comb; the finding stands that the matched locator gives 300.589 there, over two multipoles away, so the
  arm's half of the printed pair is not located by the named procedure at all;
- **ⓑ the landed state**: l.813 prints the matched locator's own `299.1` against the sky's `298.4`, the
  printed pair IS the named procedure on both halves, and the provenance finding is **resolved**.

l.945's locator is a disjunction over the two **wordings**, not just the two figures, because the landed
sentence prints "299.06 against the ruler's 302.89" — a different clause. Adjudicated `ALT-OK`.
