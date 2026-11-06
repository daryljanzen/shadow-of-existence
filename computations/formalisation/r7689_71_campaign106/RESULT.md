# `r7689+71.2` — RESULT: campaign 106, **row 5 BUILT: `cor:stationary` on `N`. If `S.H J` is a Killing horizon (rigidity's conclusion, the hypothesis P1 cites), the whole `lem:killing` gives metric coincidence along every generator. The witness is Schwarzschild's `𝓗⁺ = ∂J⁻(𝒥⁺)` on `W`, with `χ = ∂_t`.** ⌗ `13667` lines in one probe (about `390` new, band 300–1200). ⌗ p: ① `0.85` came true; ② `0.5` came true, on `W` itself, with no fallback. The expected stop (`lieDeriv` on the `Opens` subtype) was not hit

*Against `PREDICTION.md` (`r7689+71.1`). 71 re-ran `lake env lean probes/StationaryHorizon.lean`. It exits 0 with no
errors and no warnings. All `401` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The
forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

*The probe copies campaign 100's `SchwarzschildConformal.lean` and campaign 96's `KillingWhole` kit (`ld_`, `kl_`,
`kg_`, `kw_`). Eight declarations clashed, all textually identical apart from their docstrings, and one copy of each is
kept. It also takes four `sq_` lemmas from `SchwarzschildKilling.lean`: the boost generator `sq_L`.*

## ① The corollary on `N` — BUILT

***`MSpacetime.IsKillingHorizon S X Hs`*** is rigidity's conclusion, on an `MSpacetime`. It asks that:
- `X` is `C¹` as a section at points of `Hs`, and non-zero on `Hs`;
- `hRep g` is differentiable near `Hs`;
- `L_X g = 0` near `Hs`;
- through each point of `Hs` there is an integral curve of `X` inside `Hs`, null somewhere on it.

***`st_null_of_isKillingHorizon`:*** `X` is then null at every point of `Hs`.

***`st_cor_stationary`:*** under `S.IsKillingHorizon X (S.H J)`, take any integral curve `γ` of `X` on `[a, b]` inside
`𝓗⁺`. Then:
- `γ′ = X`, and `g(X, X) = g(γ′, γ′) = 0`;
- `kg_Related` holds for every pair, which is metric coincidence;
- it is injective, so distinct points stay distinct;
- `kg_deltaTau = 0`;
- the horizon's adapted splitting has `h = g` and `h(γ′, γ′) = 0` along `γ`, with `Δx = 0` and `Δτ = 0`.

Its docstring states that **rigidity is the hypothesis**, as P1 cites it (l.290: Hawking, with analyticity). The kit
cannot prove rigidity, having no Einstein equations.

## ② The witness on an event horizon — BUILT, on `W`

- **`st_isKillingHorizon`:** on Schwarzschild on `W`, `S.H J` is a Killing horizon for `χ = (V∂_V − U∂_U)/4M = ∂_t`.
  - **`st_lieDeriv`:** `L_χ g = 0` on all of `W`. `ld_lieDeriv_chart_self` holds on any manifold, and `W`'s chart is the
    inclusion (`se_dchart`). `χ(F) = 0` follows from `F`'s boost invariance.
  - **`st_hX`:** `χ` is `C¹` as a section.
  - **`st_integral`:** `γ(s) = (0, V₁ e^{s/4M})` is an integral curve inside `𝓗⁺`.
- **`st_witness`:** for `0 < V₁ < V₂`:
  - `S.H J = ∂J⁻(𝒥⁺)`, through `sx_ext`;
  - `(0, V₁) ≠ (0, V₂)`, both on `𝓗⁺`, joined by the generator over `[0, 4M log(V₂/V₁)]`;
  - `kg_Related` both ways, `kg_deltaTau = 0`, and a splitting with `Δx = Δτ = 0`.

## Stated plainly

- **Rigidity stays a hypothesis.**
- **"Stationary" has no formal content beyond invoking it.**
- The witness is the radial plane.

## Marks

- **5 → BUILT, on the cited-rigidity reading.**
- The inventory is now **27 / 4 / 3**.
- **Left in part:** 2iii, 2iv-b, 6b-ii and 7c.
- **Not begun:** 3c and 7e, which are interpretive, and 8ii-e, which needs a smoothed shell.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
