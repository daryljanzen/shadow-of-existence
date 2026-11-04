# `r7671+71.1` — PRE-REGISTRATION: campaign 95, `r7671`, `lem:killing` stage 2. Campaign 94's local lemma is glued along a whole generator, so that every pair of points on a generator of a Killing horizon, away from a bifurcation surface, is metrically coincident. Rows 4b–4d go to BUILT. ⌗ `1500` new lines (band 600–3000), ⛔ stop `3500`. ⌗ p: (a) null along the whole generator `0.85`; (b) a local isometry carrying `p` to `q` and the generator into itself `0.45`; the whole stage `0.4`. **Expected stop: composing the flow-box isometries along a chain of boxes.** That needs uniqueness of integral curves on `N`, so that each box's orbit is the generator. Second likeliest: the Lebesgue-number chain over the compact parameter interval

*Under `r7671`. A new probe, `probes/KillingGenerator.lean`, from campaign 94's `KillingLocal.lean`. No Lean was written
before this registration.*

## The statement

***Hypotheses, as in stage 1, extended along the generator.***
- `N` is a C² manifold, Hausdorff and boundaryless, as Mathlib's uniqueness of integral curves needs.
- `X` is a C¹ vector field.
- `g` is differentiable in charts.
- `L_X g = 0` on a neighbourhood of the generator.
- `γ` is an integral curve of `X` on `[a, b]`: `mfderiv γ t 1 = X (γ t)`.
- `X ≠ 0` along `γ`. This is "away from a bifurcation surface".
- `g(X, X) = 0` at one point `γ t₀`.

***`kg_lemma_killing_generator`.*** For all `t₁, t₂ ∈ [a, b]`:
1. **(a)** `g(X, X) = 0` at every `γ t`, so `ds² = |X|² dλ² = 0` along the whole generator.
2. **(b)** there is an open `U ∋ γ t₁` and a map `F : U → N` with:
   - `F (γ t₁) = γ t₂`;
   - `F` an isometry: `g_{F x}(DF v, DF w) = g_x(v, w)` on `U`;
   - `F` carrying the generator into itself: `F (γ s) = γ (s + t₂ − t₁)` for `s` near `t₁`.
   So every transverse invariant built from `g` and `X` at a point is equal at `γ t₁` and `γ t₂`, and at every point
   between them.
3. **(c)** if `γ` is injective on `[a, b]` and `t₁ ≠ t₂`, then `γ t₁ ≠ γ t₂`.
4. **The separations:** `Δx = 0` and `Δτ = 0`, read through campaign 94's ① on the ruled reading, with
   `Δτ = ∫ |χ| dλ = 0` along `γ`.

***Route.***
- **(a)** Stage 1's `kl_normSq_orbit_const` makes `|X|²∘γ` locally constant on `[a, b]`. `[a, b]` is connected, so it
  is constant.
- **(b)**
  - Within one box, `F_δ = ψ ∘ (shift by δ) ∘ ψ⁻¹` is an isometry, because the components depend only on the
    transverse coordinate (`kl_lambda_indep_N`).
  - A Lebesgue number for the compact `γ([a, b])` gives a finite chain of boxes, with consecutive boxes overlapping
    on `γ`.
  - Composing the `F_δ` gives `F`.
  - Uniqueness of integral curves (Mathlib's `IsMIntegralCurveOn` uniqueness) identifies each box's orbit with `γ`.
    This is the expected stop.

## The witness

The Rindler horizon generator `γ(s) = (0, e^s)` on `s ∈ [0, 10]`, with the boost `χ = V∂_V − U∂_U`:
- `χ` is Killing, by campaign 94's `ac_boost_isometry`;
- `χ` is null and non-zero on `U = 0`, `V > 0`, which is away from the bifurcation point `(0, 0)`;
- `γ` is injective;
- so `γ 0 = (0, 1)` and `γ 10 = (0, e^{10})` are distinct and metrically coincident.

## What stays out

- **Analyticity and rigidity** (`cor:stationary`) stay as campaign 59's hypothesis.
- **Closed generators** are excluded by the injectivity hypothesis in (c).
- **The bifurcation surface itself** is excluded by `X ≠ 0`.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED. If (b) stalls, (a), (c) and the witness land, and the
gap is named.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
