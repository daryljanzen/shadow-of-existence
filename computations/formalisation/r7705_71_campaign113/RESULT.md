# `r7705+71.2` — RESULT: campaign 113, **2a BUILT in all four stages. The interior chart maps into Schwarzschild's manifold and pulls its metric back to P2's interior metric. The cycloid is a geodesic of `se_S` itself, for every `t₀`, unit timelike with Killing energy zero.** ⌗ `16460` lines in one probe (`486` new, just under the registered band of 500–850). ⌗ p `0.5` for the whole came true. The expected stop at ②-ii did not occur. ②-i went through its registered fallback

*Against `PREDICTION.md` (`r7705+71.1`). 71 ran `lake env lean probes/CircleChart.lean`. It exits 0 with no errors
and no warnings. All `574` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `544` inherited and
`30` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 112's `CircleCycloid.lean`. The manifold is campaign 98's `se_S` on
`W = {V > 0, UV < 1}`.*

## ① The chart — BUILT

- **`cc_Φ`:** `Φ(η, t) = (s e^{−t/4M}, s e^{t/4M})`, with `s = sin(η/2)·e^{r/4M}` and `r = M(1 + cos η)`.
  **`cc_hK`:** `hK(r) = −s²`, so no square root is needed.
- **`cc_Φ_mem`:** for `0 < η < π`, `Φ(η, t)` lies in `W` with `U > 0`, and `rK(Φ) = M(1 + cos η)`.
- **`cc_Φ_inj`:** `Φ` is one-to-one on `(0, π) × ℝ`.
- **`cc_pullback`:** with `∂_ηΦ` and `∂_tΦ` given as `HasDerivAt` (`cc_dη`, `cc_dt`), and reading through
  `se_hRep`:
  - `g(∂_η, ∂_η) = −(M(1 + cos η))²`;
  - `g(∂_t, ∂_t) = (1 − cos η)/(1 + cos η)`;
  - `g(∂_η, ∂_t) = 0`.

  So `Φ*g` is exactly campaign 112's `cy_g`, which is `−4M²cos⁴(η/2) dη² + tan²(η/2) dt²` by
  `cy_interior_forms`.

## ② The geodesic — BUILT

- **②-i, `cc_η_contDiffOn`:** `η(τ)` is `C²` on `(0, Mπ)`. This went through the registered fallback: from
  `η′ = 1/(M(1 + cos η))`, applying `contDiffOn_succ_iff_deriv_of_isOpen` twice.
- **`cc_unit`:** `F(r)·S′² = 1` along `S = s ∘ η`.
- **`cc_scalar`:** `F S″ + D S′² = 0`, where `D = −F′(r) S/hK′(r)`. It comes from differentiating `F(r) S′² = 1` and
  `hK(r) = −S²`.
- **`cc_dF`:** `∂_U F` and `∂_V F`, from `kr_comp_U` and `kr_comp_V`.
- **`cc_isGeodesicOn`:** for every `t₀` and every `[a, b] ⊂ (0, Mπ)`, `γ(τ) = Φ(η(τ), t₀)` satisfies
  **`(se_S hM).IsGeodesicOn γ a b`**. This is the kit's geodesic predicate on the manifold: Koszul form for
  `g = F·gM`, in `W`'s chart. The boost fallback was not needed; the identity holds for every `t₀` directly.

## ③ Unit speed and E = 0 on the manifold — BUILT

**`cc_unit_energy`:** `g(γ′, γ′) = −1`. For the boost Killing field `χ = (−U/4M, V/4M)` (`sq_L`, the push-forward of
`∂_t` by `Φ`), `g(γ′, χ) = 0`, so the Killing energy is `E = 0`.

## What this lifts in P2

The paragraph after `prop:cycloid` (l.139) ends "The chart is not pulled back from the Kruskal manifold here." With
`cc_pullback` and `cc_isGeodesicOn`, it can now say instead that:
- the chart is pulled back from the Kruskal manifold (`cc_pullback`);
- the fixed-`t` cycloid is a geodesic of the Schwarzschild metric on that manifold (`cc_isGeodesicOn`);
- that geodesic is unit timelike with zero Killing energy (`cc_unit_energy`).

## Limits

- **The radial plane only.** `se_S` is the radial plane, so the angular sphere is not part of the manifold, as
  throughout the kit.
- **The black-hole interior only.** The chart covers the black-hole interior `{U, V > 0}`, not the white-hole
  interior.

## Marks (P2's inventory)

- **BUILT (15):** 1a, now on the manifold as well; 1b; 2a; 2b; 3; 4a; 5a; 6a; 6c; 7a–7e; 8a.
- **Not built (3 formal):** 4b (the exterior pullback; the same method applies), 5b (`r < 0` as a geometry) and 6b
  (the four `r ≥ 0` patches are exactly Kruskal).
- **Interpretive:** 6d and 8b.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
