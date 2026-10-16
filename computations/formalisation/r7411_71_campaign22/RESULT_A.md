# `r7411+71.9` — RESULT: campaign 22 BUILT. ⌗ Row 95 is DONE under THE connection: SdS's three `so(3)` fields are Killing, the scalar wave operator separates on spherical harmonics for any `F`, and the receipt's nine harmonics are associated Legendre functions with `L = ℓ(ℓ + 1)`, their derivatives proved. ⌗ `394` lines against `380` (band 220–700, ⛔ stop `850`): in the band. ⌗ `31 s`

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.8`, before the build). It is not revised.
All 23 declarations print `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` and no warning
(`PROBE_RUN_A.txt`). New file: `probes/Row95Wave.lean`. Built on Daryl's instruction.*

## ⛔ The stop, scored first

***Not fired.*** `394` lines, under `850`.

## What was built

| piece | theorem(s) | what it proves |
|---|---|---|
| (A) | `so3_killing` (with `killF95_model`, `rotA_fd`, `rotB_fd`, `cot_has`) | on `−F dt² + dr²/F + P(dθ² + S dφ²)`, `S = sin²θ` near the point, any `F`, `P`: `∂_φ`, `sin φ ∂_θ + cot θ cos φ ∂_φ` and `cos φ ∂_θ − cot θ sin φ ∂_φ` have Killing form `0` on all 16 coordinate pairs, off the poles |
| (B) | `sph_wave_sep` (with `cSph_d1`, `sep4_fd`, `sep4_d2`) | `boxD(T R Θ Φ) = TΘΦ (w²R/F + FR″ + (F′ + 2F/r)R′ − LR/r²)` for `T″ = −w²T`, `Φ″ = −m²Φ` and `Θ` associated Legendre of eigenvalue `L`, with `P = r²` near the point |
| (C) | `harm_1_0` … `harm_3_3` | the receipt's nine harmonics satisfy the eigen-equation with `L = 2, 6, 12`. Each `Θ` is an explicit function and its two derivatives are computed by proof, not supplied |
| (D) | `s3_levels` | `L(L + 2) = 4j(j + 1)` at `j = L/2` |

- ***(B) with (C) is the receipt's "no θ or φ remains, the same operator for every m".*** The radial operator
  depends on `ℓ` only through `L`. So `op(ℓ = 2) − op(ℓ = 1) = −(6 − 2)R/r²` is the difference of two instances.
- ***Real harmonics stand for the receipt's complex ones:*** `cos mφ` (or `sin mφ`) for `e^{imφ}`, and `cos wt` for
  `e^{−iωt}`. The separation is linear, so the complex statement is two copies of the real one.

## Caveats, beside the score

- ***Two of the receipt's checks were wrong in my first draft, and the build caught them.*** My hand-written second
  derivatives for `Θ₃₁` and `Θ₃₂` were wrong. Sympy regenerated them, and the final file proves every derivative
  from the function, so no supplied value is trusted.
- ***Not built, as registered:*** the receipt's Hopf-fibre part (four ad hoc expressions with hand-assigned `m`),
  and its text pins.
- ***(A) is checked on the 16 coordinate pairs.*** The Killing form is bilinear, so that is the whole statement. It
  is not phrased as the vanishing of a Lie derivative of the metric, which the receipt computes in coordinates;
  under THE connection the two are the same object.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| (A)–(D) built under the stop | `0.55` | ***yes***, `394` |

## Census (moved in this push)

Row 95 `ORDER: ENGINE-REACHABLE` → ***`DONE`***. ***Counts, checked:*** DONE ***`73`***, halves `3` (65, 66, 67),
ORDER (engine) ***`1`*** (59), LIMIT `10`, ROW `5`, generic-metric `2`, library gap `17`. Total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
