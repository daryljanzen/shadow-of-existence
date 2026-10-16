# `r7411+71.11` — RESULT: campaign 23 BUILT. ⌗ `S³` in Euler angles is a non-diagonal `Fin 3` instance of the `r7351` engine: THE connection gives `R = 6` and `Ric = 2G` in the receipt's chart, the coframe's structure equations hold with their partials proved, and every frame-constant symmetric tensor is transverse (traceless when `H` is). ⌗ Row 67 → DONE. ⌗ `368` lines against `300` (band 180–600, ⛔ stop `750`): in the band

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.10`, before the build). It is not revised.
All 48 declarations of the new `section EulerS3` in `probes/NonDiag.lean` build with no warning; the 11 theorems
and key lemmas printed at the end of the file show `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`
(`PROBE_RUN_A.txt`). Built on Daryl's instruction.*

## ⛔ The stop, scored first

***Not fired.*** `368` lines (`841`–`1208`), under `750`. One import line was added at the file's head
(`Trigonometric.Bounds`, for `|sin x − sin y| ≤ |x − y|`).

## What was built

| piece | theorem(s) | what it proves |
|---|---|---|
| (A) | `GU_symm`, `GU_smooth`, `GU_fd1`, `GU_fd2`, `GU_nondeg` | `G = ¼(dψ² + dθ² + dφ² + 2C(θ) dψ dφ)` for ANY smooth `C` with `C² < 1`: symmetric, smooth, nondegenerate on all of `ℝ³`, partials of order 1 and 2 |
| (B) | `GiU_inv`, `D1U_tab`, `D2U_tab`, `GamU_tab`, `RicU_tab`, ***`euler_profile_scalar`*** | the tables in the profile's 2-jet, and THE connection's scalar curvature for every such profile: `R = −2(4C³C″ − C²C′² − 4CC″ − 3C′²)/(1 − C²)²` |
| (C) | ***`euler_s3_curvature`***, `cos_jet`, ***`euler_profile_exists`*** | where the jet is `cos`'s: `R = 6` and `Ric = 2G`. `C = cos` near `θ` gives that jet; and at every `θ` off the poles a profile exists (`cos(θ + a·arctan((s − θ)/a))`, `a = |sin θ|/2`), so the hypotheses are met |
| (D) | ***`euler_coframe`***, ***`euler_structure`***, `sig_hfd`, `sig_fd` | for the receipt's `σ¹ = (0, cos ψ, sin ψ sin θ)`, `σ² = (0, −sin ψ, cos ψ sin θ)`, `σ³ = (1, 0, cos θ)`: `G = ¼ Σ σᵃ ⊗ σᵃ` (at `C = cos`), `det σ = sin θ`, `det G = sin²θ/64`; and `∂ᵢσᵃⱼ − ∂ⱼσᵃᵢ = −Σ εₐbc σᵇᵢ σᶜⱼ` with every partial proved by `HasFDerivAt` |
| (E) | ***`euler_tt_trace`***, ***`euler_tt_transverse`***, `hE_fd` | for `hᵢⱼ = Σ Hₐb σᵃᵢ σᵇⱼ`: `G⁻¹·h = 0` when `H` is traceless, and `∇ⁱhᵢⱼ = 0` with `Γ` THE connection's (`lcGam`), its partials proved, for EVERY symmetric `H` |

- ***This is the instance rows 66 and 67 waited on*** ("a non-diagonal `Fin 3` instance"). The engine is the
  `r7351` `EngineG`, unchanged; `curvG_eq` carries it to THE connection.
- ***(E) is stronger than registered.*** Transversality does not use tracelessness: the divergence of a
  frame-constant symmetric tensor vanishes for any `H` (it is `ε_abc H_bc = 0`). The trace condition enters only
  `euler_tt_trace`. The theorem was stated without it once Lean reported the hypothesis unused.

## Caveats, beside the score

- ***The engine requires a form nondegenerate on all of `ℝ³`, and the Euler chart is not*** (it degenerates where
  `sin θ = 0`). So (B)–(C) and (E) are about any metric whose profile `C` has `C² < 1` everywhere and `cos`'s jet at
  the point. Curvature and `Γ` at a point see only that jet, so this is the Euler chart's value there, and
  `cos_jet` gives the jet from `C = cos` near the point. ***What is not proved is a germ-locality lemma for THE
  connection in general;*** the jet is all the statements use.
- ***The certificates for (E) were found by sympy.*** The trace and the three divergence components close by
  `linear_combination` against `sin² + cos² = 1` (twice), `u·(cos²θ − 1) = 1` and the symmetry of `H`. The
  coefficients were computed outside Lean by sequential division; Lean's `ring` checks every one, so nothing is
  trusted from the script.
- ***The structure equations are in the receipt's convention.*** My first σ ordering failed the sympy check
  before registration; the convention in the table is the one that passes, and it is the receipt's.
- ***Not built, as registered:*** the `ε`-series of `R(exp εH)` and the split algebra (row 66), the deficiency
  claim (prose), and the imported TT spectrum (the spectral library gap).

## Compile, against the `2–8` minutes registered

The section alone, with the engine it uses, builds in `≈ 25 s`. The whole of `probes/NonDiag.lean`, with the
squashed-`S⁵` and EF sections before it, takes `523 s` (`PROBE_RUN_A.txt`), which is dominated by those
older sections.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| (A)–(E) built under the stop | `0.50` | ***yes***, `368` |

## Census (moved in this push)

- ***Row 67*** `DONE (chartable half)` → ***`DONE`***. What remains is the imported TT spectrum (`10 = 5 + 5`),
  which no receipt computes. That is the spectral-theory library gap, already on the census, and not this row.
- ***Row 66*** stays `DONE (chartable half)`. The coordinate checks have moved out of its open half, which is now
  the `ε`-series and split algebra, the deficiency claim (prose), and the imported spectrum.
- ***Row 59*** stays `ORDER: ENGINE-REACHABLE`, with the instance and coframe named as built.

***Counts, checked:*** DONE ***`74`***, halves ***`2`*** (65, 66), ORDER (engine) `1` (59), LIMIT `10`, ROW `5`,
generic-metric `2`, library gap `17`. Total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
