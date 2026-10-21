# `r7443+71.45` — RESULT: campaign 47 BUILT. ⌗ Row 101's last check: the `23.254 %` ratio `∫_{π/4}^{π/2} sin^{−2/3} / ∫_0^{π/2} sin^{−2/3}` lies in `[0.2325252, 0.2325550]`, inside the receipt's `|frac − 23.254| < 0.002`. ⌗ `431` lines (band 250–1100, IN BAND). ⌗ p `0.40` came true. ⌗ Row 101 → `DONE`; LIMIT → `0`

*Scored against `PREDICTION.md` (pushed at `r7443+71.43` before any Lean), not revised. `probes/Row101Ratio.lean`
builds with no error and no warning, and both theorems print `[propext, Classical.choice, Quot.sound]`
(`PROBE_RUN_A.txt`, `90 s`). No `native_decide`. The build was done by a delegated agent and re-run by 71.*

***Proved.***
- `row101_ratio`: `g = sin^{−2/3}` is interval-integrable on `[0, π/2]`, and the ratio lies strictly inside
  `(0.23252, 0.23256)`.
- `row101_frac`: the receipt's own form, `|100·ratio − 23.254| < 0.002`.

***Route, which is not the registered one and is better.*** No sines, no π and no convexity are used.
- Two exact substitutions, by Mathlib's `integral_image_eq_integral_abs_deriv_smul`, send both pieces to smooth
  integrals on `[0, 1]`:
  - `w = π/2 − arctan u` gives `∫_{π/4}^{π/2} g = ∫_0^1 (1+u²)^{−2/3}`;
  - `w = arctan v³` gives `∫_0^{π/4} g = 3∫_0^1 (1+v⁶)^{−2/3}`.
- Integrability carries across the substitution (`integrableOn_image_iff_integrableOn_abs_deriv_smul`), which
  disposes of the singularity at `0`.
- Both integrands decrease, so `AntitoneOn.integral_le_sum` and `AntitoneOn.sum_le_integral` with `n = 5000` give
  the brackets.
- Each sample is bracketed by a cube condition over ℕ, checked by `decide +kernel` in chunks of 1000.

***Register risk:*** realised and handled. The first build peaked at 10 GB; chunking and narrowing the imports
brought it to 3.7 GB.
