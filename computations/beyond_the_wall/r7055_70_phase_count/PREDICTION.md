# r7055 Q1 → 70: the phase systematic's effective count against the slope and the step — PRE-REGISTRATION

*Node 70. Committed before the measuring script exists. Scoping read the two receipts' statistics and ran the step
receipt once for its printed values; those are declared below and not tabled as open.*

## Declared from scoping

**The 2.3 / 2.5 modes do not carry over.** `r7049+70.1` measured them for `cc66`'s `band_amp`, a per-band sinusoid
fit with the period held. Neither ordered claim uses that statistic:
- **The step** (`P15_the_step_is_the_excesss_own…`, `band_excess('mean')`): per band, the RMS of `osc` on the
  `r6941_fine` banks, arm over control, minus one. The band edges are `r6959_eta_cr.npz` `q_edges`: seven bands,
  0.85–5.75, each 0.70 wide.
  - Printed: +0.0215, +0.0574, +0.0519, +0.0606, +0.0748, +0.0659, +0.0762.
  - Step ratio 0.333, so band 1 departs from the band 2–7 mean by −0.043.
- **The slope** (`P15_the_cross_term_is_not_the_channel…`, `retained`): per band, the D_ℓ-oscillation RMS over the
  source-oscillation RMS, arm over control, with a straight line fitted in q.
  - The paper's `+0.0139` comes with `0.0021`. That figure is the spread over **twelve envelope settings** (four
    windows × three band counts). **It is not a regression error**; no regression error is quoted.
- **Both statistics are arm/control ratios.** A phase error common to both arms therefore divides out, to the extent
  that the statistic's phase response is the same on both. `r7049+70.1` measured the two arms' band-fit errors
  correlating at 0.9986. **So the count asked for is the count of the systematic that survives the ratio**, and that
  is what is measured.

## What is measured — each statistic's own functions, lifted from its receipt by syntax tree and run unchanged

For each statistic, a **null injection** is built on every bank it reads:
- a comb E(1 + 0.5 cos(2πq/T + φ₀ + φ)), with E the bank's own window-1.0 running-mean envelope;
- T and φ₀ are that bank's own fitted period and phase, found with `cc66`'s `fit_period` and the phase fit of
  `r7049+70.1`;
- **identical amplitude on both arms, so the true excess is zero in every band and the true slope is zero**;
- φ is a **common** shift over 24 values in [0, 2π). For the slope it is applied to the D_ℓ and source sides alike.

What comes out, per statistic:
- **e_b(φ)**, the per-band value, which is pure systematic because the truth is zero.
- **N_eff** = (Σλ)² / Σλ² of the 7×7 correlation of e across φ. This is the ordered "effective count".
- **For the slope:**
  - the fitted slope's spread over φ, σ_s;
  - the regression error a 7-point iid fit would claim from the same residuals, σ_OLS;
  - n_slope = 7 · (σ_OLS / σ_s)², the number of independent points the slope actually has against this systematic;
  - the slope's signal-to-systematic, 0.0139 / σ_s, with σ_s also set against the 0.0021 setting spread.
- **For the step:**
  - s(φ) = e₁ − mean(e₂…₇), its spread σ_step, and its worst |s|;
  - the step's signal-to-systematic, 0.043 / σ_step.
- **At the real phase (φ = 0):** e_b, the false slope and the false step.
- **Differential phase:** the fitted phase difference between the arms, reported. It is not scanned unless it
  exceeds 0.05 rad.

## Outcome table — the one costing another seat most FIRST

| | outcome | what it would mean |
|---|---|---|
| ① | the step's or slope's worst false value over φ reaches half its reported size | the finding is within reach of the statistic's own phase systematic; routed first |
| ② | n_slope < 4, or N_eff < 4 for either statistic | the band-resolved claim has materially fewer independent points than seven, and the number is named |
| ③ | ① and ② clear, but N_eff < 7 | fewer than seven modes, and still no cost to the findings; said in writing |
| ④ | N_eff ≥ 6 and signal-to-systematic > 10 for both | **unchanged, which costs the sector nothing**; stated so it is in writing |

## Gates

- They are on the measured quantities, and the lifted functions are checked to be the receipts' own.
- The paper's wording is **reported and never required**.

## ⛔ NOT CLAIMED

- Nothing about the likelihood, which bins at a thirty-fourth of a period (`r7033`'s split stands). Nothing
  reopened.
- No edit to either receipt, and no prose edited.
- A null injection measures the statistic's response to phase. It is not a claim about what the real spectra's
  phase error is beyond φ = 0.
