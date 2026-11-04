# `r7675+71.3` — RESULT: campaign 97. **① Schwarzschild in Kruskal's radial plane as an `MSpacetime`, with 3a BUILT** (`RESULT_1.md`; one registered clause corrected). **② 3b BUILT**: Schwarzschild's `∂_t = χ = (V∂_V − U∂_U)/4M` is Killing for the actual `F`, is null on the horizon, and makes two horizon events metrically coincident. Neither registered stop was hit. ⌗ ① `765` new lines; ② about `590` new lines plus headers. ⌗ p: ① `0.6` came true apart from the corrected clause; ② `0.6` came true

*Against `PREDICTION.md` (`r7675+71.1`). 71 re-ran `lake env lean probes/SchwarzschildKilling.lean`. It exits 0 with
no errors and no warnings. All `238` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `182`
copied and `56` new. The forbidden-token grep is clean, and the probe imports only Mathlib. `check_no_sorry.py` reports
ALL 29 THEOREMS COMPILE.*

## ② 3b — `SchwarzschildKilling.lean`

***The metric.***
- `sq_g M x = F(x) · (−dU dV)`, where `F = 32M³/r · e^{−r/2M}` and `r = rinv(−UV)`.
- `sq_metric_formula` states this formula explicitly. It is the same formula as ①'s `sk_hRep`.
- `sq_lorentzian`: it is Lorentzian on `{UV < 1}`.

***The Killing field — the registered stop, not hit.***
- `χ = (−U/4M, V/4M)`.
- `sq_chi_UV`: `χ(UV) = 0`, so `χ(F) = 0` (`sq_chi_F`).
- The flat boost terms cancel.
- **`sq_lieDeriv`: `L_χ g = 0` on `{UV < 1}`**, through the registered `lieDeriv`.

***Its norm.***
- `sq_normSq`: `g(χ, χ) = F · UV / 16M²`.
- So `χ` is null on `U = 0`, timelike in region I, and non-zero for `V ≠ 0`, which keeps it away from the bifurcation
  point.

***The generator.*** `γ(s) = (0, e^{s/4M})` is an integral curve of `χ` itself, so `s` is Schwarzschild `t`.

***`sq_cor_EF_coincident`.*** For `0 < V₁ < V₂`, `kw_lemma_killing_whole` along `γ` on `[4M log V₁, 4M log V₂]` gives:
- (a): null along the generator;
- (b): `kg_Related` both ways;
- `Δτ = 0`, and `Δx = 0` in the horizon splitting;
- `∫ dt(γ′) = Δt`;
- `(0, V₁) ≠ (0, V₂)`, both at `r = 2M`.

**So the two horizon events are metrically coincident, with no invariant temporal separation.**

***Non-vacuity.*** `sq_FS_nonconst`: `F = 8M²e⁻²` at `r = 4M`, against `16M²e⁻¹` on the horizon.

## Marks

***3a → BUILT, on Schwarzschild** (`sk_cor_EF_events`).* The two horizon events are:
- distinct;
- causally ordered but not chronologically related;
- both on the static observer's `∂J⁻` within `M`;
- both at `r_h`.

In EF they sit at `v = 4M log V`.

***3b → BUILT, on Schwarzschild** (`sq_cor_EF_coincident`).* They are metrically coincident.

***The link between the two files.*** It is the shared explicit formula for `g` (`sq_metric_formula` and `sk_hRep`).
Probes cannot import probes.

***3c*** (the EF diagram's vertical extent) is interpretive and stays NOT BEGUN.

## Carried forward

- ①'s correction: `S.H J` in the full `Pt` also contains the white-hole singularity. So `𝓗⁺ ⊆ M` fails, and the
  headline's limits are not run on `sk_S`.
- The fix is `N = M`, or EF's domain `{V > 0, UV < 1}`, as a manifold in its own right. That is row 8's foundation, at
  about `1500–2500` lines and p `0.35`.
- Curvature was neither checked nor used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
