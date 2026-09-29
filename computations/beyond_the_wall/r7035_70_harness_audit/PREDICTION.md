# r7035 → 70: one pass on the instrument-noise null harness, now load-bearing for PO-56's exit: PRE-REGISTRATION

*Node 70. This file is committed before the audit script is written or run.*

## What was already in hand, declared rather than tabled as open

These are properties of the likelihood file and of receipts already on `main`. This audit measures none of them.

- **`COV_TT` has 215 bins.** The harness uses the `OK` subset.
- **Its correlation is NOT a lag-limited band.**
  - Mean correlation at lag 1 is 0.120.
  - At lags 2–15 it runs from 0.155 down to 0.139, and at lag 30 it is 0.112.
  - `cc66.62`'s "flat ≈0.15 floor at lags 1–7" is the start of a **long-range plateau that decays slowly**.
  - The smallest eigenvalue of the correlation matrix is 0.247.
- **Both flat-floor variants are positive-definite.** Setting every off-diagonal correlation to 0.15 gives a smallest eigenvalue of 0.850. Keeping 0.15 at lags 1–7 and 0 beyond gives 0.357.
- **The harness is `r7029`'s null (iii)**: control fit plus `N(0, COV)`, pushed through the whole estimator. `cc66.66`
  used it for three projections, with β and γ re-estimated on every draw:
  - ⓐ the term mix's own cost, clearing at 2.26× the null maximum;
  - ⓑ the arm's excess the term mix does not explain, at 2.83×;
  - ⓒ the part the term mix misplaces, at 1.44×.
- **`cc66.65`'s accounting instrument works at the SPECTRUM level.**
  - The spectrum difference is `d = shape_fit(m) − shape_fit(mc)`. Each `shape_fit` is the model times one scalar amplitude fitted to the data.
  - `d` therefore depends on the data only through two fitted scalars.
  - The window's +0.27 rad and ratio 0.264 were read off `d`.

## Item ⓐ: the assumption that the likelihood's `COV` is the noise

**Design, fixed now.**
- The **estimator is held fixed**: `F = COV⁻¹` stays the likelihood's own metric, as the paper defines the statistic.
- Only the **covariance the noise is DRAWN from** varies. The question is "what if the noise is not what the
  likelihood says it is", not "what if the statistic were defined differently".
- The variant where both change is a different statistic. It is NOT run, and is named here as not run.

**Variants**, each with 2,000 draws on one shared seed per variant:

| label | noise drawn from |
|---|---|
| V0 | the likelihood's `COV` (reproduces `r7029` and `cc66.66`) |
| V1 | the diagonal alone |
| V2 | the real diagonal with EVERY off-diagonal correlation at 0.15, the flat floor taken as a plateau |
| V3 | the real diagonal with correlation 0.15 at lags 1–7 and 0 beyond, the floor taken literally |
| V4 | `COV` rescaled by s = 0.5 and s = 2 |

**Expectation for V4, stated before running.** The noise-carrying cross term is linear in the residual. The null's
amplitudes should therefore scale as √s, with a small departure because the fitted scalars in `d` also move.
Measured, not assumed.

**Quantities scored in every variant:**
- the arm's `a(1.00)`, the `r7029` statistic;
- `cc66.66`'s ⓐ, ⓑ and ⓒ, with β and γ re-estimated per draw.

For each: the null's median, 99th percentile and maximum; the count at or above the observed value; and the ratio of the observed value to the null maximum.

**The margin, defined now.**
- For each quantity, `s*` = (observed ÷ V0 null max)² is the variance inflation at which the null maximum reaches the observed value.
- The structural variants are reported as the ratio of each variant's null maximum to V0's.
- **The repository-supported rescale** comes from the data itself. `ŝ = χ²/ν` of the data against the control fit, with its sampling width √(2/ν), is the one rescale the repository measures.

## Item ⓑ: can the harness give an uncertainty on a RATIO and on a PHASE OFFSET?

**The structural point, stated before any number.** A null is built with the signal ABSENT.
- A phase under the null is noise-only. It is expected to be uniform, and will be tested with a Rayleigh test.
- A ratio of two null amplitudes is a ratio of two noise draws.
- **So the null, as a null, CANNOT give the uncertainty of a ratio or phase measured on the observed signal.**

That needs a different use of the same noise model: a **parametric perturbation about the observed data**, `dat + L z`,
re-running the whole estimator. Its spread is the sampling spread wherever the estimator is locally linear. Linearity
is checked by drawing at half the noise and doubling the spread; the two must agree.

**Two levels, both measured:**

(1) **Spectrum level**, the accounting's own instrument.
- The amplitude and phase of `d` for the arm, the window and the term mix.
- The window-against-arm ratio and phase offset: the full perturbation distribution, validated against the published
  0.264 and +0.27 rad as centres.
- The term mix: **the spread only.**
- **Expected, stated as the outcome that costs `cc66` most:** `d` moves only through two fitted scalars, so these
  floors will be **very small**. Spectrum-level ratios and phases are then close to properties of the theories, and
  what bounds them is systematic, not statistical.

(2) **Excess (cost) level**, where the noise lives.
- The projected (cos, sin) coefficients of the arm's, the window's and the term mix's per-bin excess, with their
  joint 6×6 covariance under the perturbation.
- From that covariance, the floor on **any** linear residue `arm − k · channel` at fixed k, and delta-method floors on
  ratio and phase.
- Validated against the direct perturbation spread for the window.

## Outcome table, the outcome that costs another seat most tabled FIRST

| outcome | what it means |
|---|---|
| **a V1–V3 variant pushes a null maximum past an observed value** | that clearance rests on the assumption; routed to 66 |
| **spectrum-level floors are negligible** | `cc66.65`'s ratio and phase, and any share built on them, are theory statements with **no statistical floor**; their honest uncertainty is systematic and must be quoted as that |
| excess-level floors are finite and the delta method agrees with direct perturbation | `cc66` can quote a share and a phase at these floors |
| perturbation is nonlinear (half-noise ×2 ≠ full) | the floors are quoted as intervals from the perturbation, not as σ |
| the null's phases are not uniform | the null leaks structure; routed at once |

**Decision thresholds, fixed now:**
- "Survives the assumption" means that under every V1–V3 variant, 0 of 2,000 draws reach the observed value.
- "Linear" means the half-noise ×2 spread is within 10% of the full-noise spread.
- "Negligible" at the spectrum level means the phase-offset spread is below 0.01 rad and the ratio's relative spread is below 1%.
- "Delta method agrees" means within 15% of the direct perturbation spread.

## ⛔ NOT CLAIMED, whatever the outcome

- No accounting is run. **No central value of the term mix's ratio, phase or share is printed.** That is `cc66`'s,
  because `cc66` owns the instrument. Spreads only.
- No channel, mechanism, re-scoring, physics, or verdict on `cc66`'s results. A variant that moves a null maximum is
  reported and routed, not applied.
- No edit to any `cc66` receipt, bank or transfer.
