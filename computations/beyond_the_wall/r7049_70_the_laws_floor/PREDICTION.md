# r7049 → 70: the floor under the acceptance law's test — PRE-REGISTRATION

*Node 70. Committed before the audit script exists and before any number below the "declared" line is computed.*

## The claim audited, as landed (`P15` `sec:refit-bound`, and the receipt's gate ⓸)

> "…holds on both arms to within ten per cent everywhere, worst deviation 6.7 per cent, six of the seven bands on each
> arm landing inside the measuring statistic's own 3.74 per cent accuracy on a known injected comb…"

The receipt is `P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_and_the_law_has_no_fitted_coefficient`
(`cc66`'s). **It is read and imported. It is not edited, and its gate ⓪ is not re-run as a verdict on `cc66`.**

## Declared, because scoping ran the receipt once to read its reported figures

- **Gate ⓪'s known input.**
  - A single comb: constant amplitude 0.5, period 1.0347, phase 0.7.
  - It is built on the **control's** envelope and `q` grid only.
  - Recovered: 0.4972, 0.4834, 0.4947, 0.4836, 0.4830, 0.4977, 0.4813. **All seven are low**, worst −3.74 %.
- **Gate ⓸'s law/measured ratios.**
  - lcdm: 1.063, 1.011, 0.990, 1.012, 1.042, 1.016, 1.017.
  - cr: 1.067, 1.015, 0.990, 1.012, 1.044, 1.018, 1.016.
- **What the gate counts.** It counts bands with |ratio − 1| < **0.05**, while its label says 3.74 %. At 3.74 % the printed
  ratios put **five** of seven inside on each arm; the band at 3.65–4.35 sits at 4.2 / 4.4 %.
  - This is declared as seen. It is scored below as outcome ②, and it is not re-discovered.
- **The two arms' ratio patterns look nearly identical** band by band. This is declared as seen, and it is measured in M3.

## What is measured (the instrument is the receipt's own `osc`, `fit_period` and `band_amp`, imported unchanged)

**M1 — the literal count.** Bands inside 3.74 %, and inside 5 %, on each arm. Read from the receipt's own ratios.

**M2 — does the 3.74 % transfer to where the real bands are?** A known comb is injected **on each arm's own envelope
and `q` grid**, with:
- amplitude **profile = that arm's own law `A_l(q)`**, varying within and across bands, as the real comb does;
- period = that arm's own fitted period;
- phase scanned over 24 values in [0, 2π), plus the arm's own fitted phase.

Per band, the recovery error is e = measured / (band mean of the injected `A_l`) − 1. Reported:
- **F_t**, the worst |e| over bands and phases, per arm. This is the floor where the real bands are.
- e at the arm's own phase, per band.
- **The corrected ratio.** The law against the real measurement once the instrument's own error at that band is
  divided out: r_c = law × (1 + e_own) / measured. If the real comb were exactly the law's comb, r_c would be 1 up to
  the instrument's residual, so |r_c − 1| is the deviation **the instrument cannot account for**.

**M3 — how many independent measurements is "six of seven"?**
- (a) **Coverage.** The fit range's width, in comb periods, and each band's width in periods.
- (b) **The measurements proper.** White noise is added to the injected spectrum (400 draws per arm), the full
  instrument is run, and the 7×7 correlation of the band amplitudes is taken. Reported as N_eff = (Σλ)² / Σλ² of that
  matrix, per arm.
- (c) **The instrument's systematic.** The 7×7 correlation of e across the 24 phases, with its N_eff.
- (d) **Between arms.** The correlation of the two arms' 7-vectors of (ratio − 1), and of their e at their own phases.

## Outcome table — the one costing another seat most FIRST

| | outcome | what it would mean |
|---|---|---|
| ① | **F_t > 10 % at some band, or \|r_c − 1\| > 10 % at some band** | the "within ten per cent everywhere" sentence is not supported by the instrument at the real bands |
| ② | **fewer than six of seven inside 3.74 % on an arm** (M1; declared seen: five) | "six of the seven … inside … 3.74 per cent" is false as worded. The count that holds is named (six inside 5 %) |
| ③ | **F_t outside [2.5 %, 5.0 %]** | the 3.74 % is a floor measured where the real bands are not, and the transferred figure is named |
| ④ | **N_eff (b) ≤ 5 on an arm, or between-arm correlation (d) > 0.9** | "six of seven on each arm" counts fewer independent tests than it reads as, and the number is named |
| ⑤ | none of ①–④ | the sentence stands as written |

These outcomes are not exclusive; every one that fires is reported.

## Gates — the finding, not the symptom

- The gates are on the instrument's behaviour (F_t, e, r_c, N_eff, the correlations) and on the receipt's own printed
  ratios, recomputed through its imported functions.
- **The paper's wording is reported, never required.** If 66 corrects the sentence, this receipt stays green.
- The receipt's own gate ⓸ is **reported** (it counts at 5 %), never required to change.

## ⛔ NOT CLAIMED

- No verdict on the law's physics or on `cc66`'s convergence sweep.
- No re-run of `cc66`'s gate as a judgement on it, and no edit to its receipt.
- No prose edited. Everything is routed to 66.
- No new noise model for the spectra. The noise in M3(b) is a probe of the instrument's coupling, not a claim about
  the data.

## And the second item in `r7049`: `P15_verify_lowell_boltzmann`

**Disposal: the header names the superseded depths, and it is not brought current.**
- Bringing it current would move its background to the adjudicated one. That would move the r0-stability table,
  and the paper cites that table (15 % at ℓ = 4).
- Its role in the citation group is the four-figure gate and the r0 drift, not the quartet.
- The header and the printed verdict will therefore say:
  - its depths are on the **control** background (H0 = 67.4, r0 = 5064);
  - the current quartet (0.487 / 0.435 / 0.359 / 0.666) is computed by `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling`'s
    arm A on the adjudicated background.
- A gate will check that the superseding receipt exists and carries that arm.
- **No physics number in the file changes.**
