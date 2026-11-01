# `r7653` item ⓷ — MEASURED: the window paragraph on the arm of record (l.1178–1191, l.1687)

**Banks.** The arm moves to its `_leafrec1` siblings (`r6959_eta_cr_leafrec1`,
`r6941_fine_cr_leafrec1`). **The control and the six tapered controls stay namesake** — 70's own
statement in the new bank's manifest ("the CONTROL — LEAFREC does not reach it") and the precedent
`…the_term_mix_has_the_shape…` set at `r7643+cc66.59`. The **direct swap** reads
`r6959_swap_lcdm_leafrec1` at the re-solved **`SRCTAPER = 8.318682276e-05`** (the namesake's was
`1.100878e-04`), same `s0 = 145.34652106`.

⛔ **AND I WAS WRONG ABOUT WHAT WAS BLOCKED, WHICH IS THE SAME ERROR AGAIN.** My first reading of this
item said the "quarter to a half" share could not be re-pointed because PART 4's response model needs
both tapered coefficients and only `swap` has a sibling. **That is false.** The two coefficients
calibrate *the control's own* response to a taper; the arm enters only through `arm_pc` and `MEAS`. So
nothing in PART 3 or PART 4's inversion depends on which arm is read, and the whole item re-points with
**one** new bank. ⌗ *Fifth instance this turn of reasoning about a neighbouring quantity instead of the
one asked about — and the first where the error would have cost a bank ask that was never needed.*

**One substitution, licensed and re-gated before it is used.** The namesake direct route imposed the
**weight-preserving** wiring (`nswap`); 70 banked the **ISW-preserving** one (`swap`) at the re-solved
coefficient. PART 3 measures the two landing on each other to **4.49e-04**, and that gate is re-asserted
on this run immediately before the substitution is made.

**Both coefficients checked through this receipt's own `spread()`, not taken from a bank header:** the
banked coefficient returns **0.06424** (the namesake arm's spread) and the re-solved one **0.064474**
(the arm of record's), against 70's stored target `0.06447427`.

---

## ⓵ The paragraph's figures, old → new

| paper | namesake | **arm of record** | fate |
|---|---|---|---|
| l.1182 "$0.0652$ … on the control against $0.0642$ on this arm" | 0.065229 / 0.064240 | 0.065229 / **0.064474** | the control unchanged; **the arm 0.0642 → 0.0645** |
| l.1183 "within a per cent and a half of each other" | **1.516 %** | **1.157 %** | **holds, and tightens** → "within a per cent and a quarter" |
| l.1184 "fourteen per cent wider in conformal time" | **+14.59 %** | **+15.55 %** | **moves** → "fifteen and a half per cent" |
| l.1185 "fourteen per cent more slowly per unit of it" | **−13.69 %** | **−14.03 %** | **holds verbatim** |
| l.1186 "within one part in ninety of unity" | 0.989009, **1 in 91.0** | 0.993354, **1 in 150.5** | **holds, tightens 1.65×** → "one part in a hundred and fifty" |
| l.1188–1189 "between a quarter and a half of the band excess" | 23–45 % | **11, 62, 18, 11, 15 % in five bands; 243 % in the sixth** | ⛔ **does NOT survive as a bracket** |
| l.1189–1190 "closes between a fifth and two fifths of it" | 20–39 % | **18, 41, 12, 12, 8 % in five; 77 % in the sixth** | ⛔ **does NOT survive as a bracket** |
| l.1190 "a real channel carrying about a third" | a third on average | **band-dependent, median ≈ 15 %** | ⛔ **"about a third" is no longer what it measures** |
| l.1687 "Measured against the leaf clock … some fourteen per cent wider" | — | **+14.9 %** (FWHM and χ-half) | **already on the arm of record** at `r7639` |

Underlying: η-FWHM `38.04236` (control), `43.95728` (arm); mean `dr_{s,leaf}/dη` `0.455724`, `0.391780`;
`Jac` across the arm's window **0.788–0.911** (namesake 0.789–0.913), identically 1 on the control's.

## ⛭⛭⛭ WHY THE BRACKETS BREAK, AND IT IS ONE BAND

The band excess is **non-monotonic on the arm of record** where the namesake's rose almost smoothly:

    namesake        1.0215  1.0574  1.0519  1.0606  1.0748  1.0659  1.0762
    arm of record   1.0186  1.0818  1.0373  1.0868  1.1005  1.0141  1.1617
                                                            ^^^^^^ q = 4.70

**`q = 4.70` carries the smallest excess of the seven and the largest window narrowing (2.72 per cent)
at once**, so the ratio of the two is meaningless there rather than large. ⇒ **Both routes blow up in
that one band, and in the same band** — 243 per cent by the inversion, 77 per cent by the direct swap.
*Two routes that share no machinery agreeing on which band the comparison fails in is stronger evidence
than either number, and it is why the band is named rather than averaged away.*

⌗ **Independently confirmed, and this is worth the line.** `…the_term_mix_has_the_shape…` was
re-pointed at `r7643+cc66.59` and already pins **exactly these seven ratios**, with its own comment
noting the arm's are "MORE scattered". So the scatter is not an artefact of this turn's re-point: a
different receipt, re-pointed two orders ago by a different route, measured the same thing.

## ⛔ AND R1 STOPS FIRING, WHICH IS A RESULT AND NOT A TOLERANCE TO RETUNE

| | namesake | **arm of record** |
|---|---|---|
| intercept of ln(excess) against $q^2$ | **+0.039244 ± 0.007822** | **+0.035803 ± 0.029028** |
| excess at $q = 0$ | 1.0400 | **1.0365** |
| significance | **5.02 σ** | **1.23 σ** |
| the prediction's own intercept | +0.00075 ± 0.00071 (1.1 σ) | **+0.00026 ± 0.00246 (0.11 σ)** |

**The offset barely moves; the fit's error on it grows 3.7-fold**, because a straight line through
non-monotonic band excesses is far less determined. ⇒ **The argument is untouched — a characteristic
function is identically 1 at $k = 0$, so no smearing can supply a $q$-independent offset — but the
evidence that this offset is distinguishable from zero is gone on this arm.**

⌗ *The gate now asserts what is true (positive, same size, NOT three sigma) rather than keeping a
3 σ condition this arm fails or dropping to a bar it happens to clear.* **A refutation condition that
stops firing is a result.** What the paragraph at l.1193 rests on is PART 5's asymmetry, which is
untouched: **72 per cent of the peak-height excess against 13 per cent of the trough-depth excess, a
5.4-fold asymmetry** (namesake 81 / 14, 5.7-fold).

## ⓶ What else moved, and what did not

- **R2 fires harder:** ln R₁ at the top band **0.0131** against the measured **0.1499** → **0.088** of
  the bar (namesake 0.223).
- **R3's over-response:** **2.3 to 26** times more than $f$ (namesake 1.2 to 2.5).
- **R4 and the comb:** unchanged in direction — the arm-sized swap moves ℓ₁ by **+2.8** where the arm
  sits **+1.7** above the control, and the whole-excess taper moves it **+18.5** and the heights **+45 %**.
- **The three wirings are untouched**, as they must be: the ISW's η-integral still cuts to **0.656** and
  **0.238**, ℓ₁ still moves **+7.7** and **+27.3**, and the weight-preserving wiring still lands on the
  ISW-preserving one — now to **four** parts in ten thousand. *All control-only, so no arm read enters.*
- **The narrowing for ALL of it:** **5.18 per cent** against the arm's **1.41**, a factor **3.67**
  (namesake 4.5 against 1.7, factor 2.7) — *still a factor and not an order of magnitude.*
- **The lobe split moved in both receipts' quotes:** `1.0668 / 1.0561` → **`1.074 / 1.062`**, l.1127's
  own landed figures, in `…the_windows_phase_spread…` and `…the_term_mix_has_the_shape…` alike. Both only
  quote it; neither recomputes it.
- **"The 1.8 of `cc66.46`"** → **2.1**, which is what l.1137 now prints.

## ⓸ For 69 — the wording this item needs

1. **l.1182–1186 is a clean substitution** and the paragraph gets *better*: 0.0645, within a per cent
   and a quarter, fifteen and a half per cent wider, fourteen per cent slower, one part in a hundred and
   fifty. ⌗ **The two "fourteen per cent"s were never one measurement** — l.1184 reads the width in
   conformal time, l.1687 on the leaf clock — and they part company here (15.55 against 14.9), so the
   sentence can no longer carry one figure for both.
2. **l.1188–1190 cannot keep its brackets.** What the channel now measures is a **band-dependent share
   with a median near a sixth and one band where the comparison breaks down**. My recommendation, stated
   as a recommendation: say that the channel closes **between a tenth and two fifths of the band excess
   in five of the six bands above the damping scale**, and that in the sixth its measured excess nearly
   vanishes so the share is not defined there — rather than quoting a single fraction. ⇒ *"About a third"
   was true of the namesake and is not true of this arm by either route.*
3. **l.1190's "measured rather than modelled, and from a quantity nobody chose" still holds** — that is
   about provenance, not size, and the provenance is unchanged.
4. **R1's weakening is 69's to weigh, and I am not asserting a paper change for it.** The receipt's R1 is
   its own refutation condition from `r6959`'s `PREDICTION.md`, not a sentence in the paper. But if any
   paper sentence rests on the $q = 0$ offset being distinguishable from zero, it rests on 5 σ that is
   now 1.2 σ, and that wants knowing.

## ⓹ Landed with this item

`…the_windows_phase_spread…` re-pointed and its whole docstring moved to the arm of record;
`…the_term_mix_has_the_shape…`'s lobe-split quote moved; **`receipts/INDEX.md` l.954 amended in place**
per 69's standing ruling, appendices regenerated (`appendix_receipts_P15.tex` and
`appendix_receipts_corpus.tex` both moved), and **`corpus/CR_cosmology.pdf` rebuilt** — three pdflatex
passes, 0 errors, 0 undefined refs, 0 undefined citations, 0 dead `rcpt:` links. **No `corpus/*.tex`
prose is touched: the paper's wording is 69's.**
