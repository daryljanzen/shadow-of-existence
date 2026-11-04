# `r7671+71.2` — RESULT: campaign 95, `lem:killing` stage 2. **(a) null along the whole generator, (b) a local isometry between any two generator points carrying the generator into itself, and (c) distinctness are BUILT. `Δτ = 0` is BUILT. `Δx = 0` holds box by box only, so (d) is BUILT IN PART.** The registered expected stop was not hit: a clopen induction on `[a, b]` replaced the Lebesgue-number chain. ⌗ `3207` lines in one probe (`711` new, band 600–3000). ⌗ p: (a) `0.85` came true; (b) `0.45` came true; the whole stage `0.4` came true except for global `Δx`

*Against `PREDICTION.md` (`r7671+71.1`). 71 re-ran `lake env lean probes/KillingGenerator.lean`. It exits 0 with no
errors and no warnings. All `172` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `125` are
copied and `47` are new. The forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE. The
probe copies campaign 94's `KillingLocal.lean` and adds Mathlib's `IntegralCurve.ExistUnique`.*

## `kg_lemma_killing_generator`

***Setting.*** `E` is finite-dimensional, and `N` is a C² manifold.

***Hypotheses.***
- `X` is C¹ along `γ`.
- `X (γ t) ≠ 0` on `[a, b]`, which is away from bifurcation.
- `g` is differentiable in charts near `γ`.
- `L_X g = 0` near each `γ t`.
- `γ` is an integral curve of `X` at every `t ∈ [a, b]` (`IsMIntegralCurveAt`).
- `X` is null at `γ t₀`.

***Conclusions.***
1. `mfderiv γ t 1 = X (γ t)` on `[a, b]`.
2. **(a)** `g(X, X) = 0`, and `ds² = g(γ′, γ′) = 0`, at every `γ t`. **BUILT.**
3. **(b)** For all `t₁, t₂ ∈ [a, b]`, `kg_Related g γ t₁ t₂`. **BUILT.** This means there are an open `U ∋ γ t₁` and an
   `F` with:
   - `F (γ t₁) = γ t₂`;
   - `F` differentiable on `U`, with `g_{F x}(DF v, DF w) = g_x(v, w)` there;
   - `F (γ s) = γ (s + t₂ − t₁)` for `s` near `t₁`.

   So every invariant of `g` at a point is equal at `γ t₁` and at `γ t₂`.
4. **(c)** If `γ` is injective, distinct parameters give distinct points. **BUILT.**
5. **(d)** `Δτ = ∫ |X| |dλ(γ′)| = 0`, with lapse `√(max 0 (−g(X, X)))`. **BUILT.** `Δx = 0` is shown in each box, on its
   slice `h = 0`. There is no global spatial splitting along `γ`, so global `Δx` is **REPORTED**.

## How (b) went

- **One box.** `kg_shift K δ = ψ ∘ (· + (δ, 0)) ∘ ψ⁻¹` is an isometry (`kg_shift_isometry`, via `kl_lambda_indep_N`).
  This needed the flow box's C¹ inverse. Stage 1 had discarded it, so it is re-proved (`kg_flowBox_killing_symm`,
  `kg_restrict`).
- **Uniqueness.** `kg_curve_eq_orbit` identifies `γ` with each box's orbit, using Mathlib's local uniqueness
  (`isMIntegralCurveAt_eventuallyEq_of_contMDiffAt_boundaryless`). It needs no Hausdorff assumption.
- **All pairs.** `kg_related_trans` composes related pairs, and `kg_related_box` relates every pair within one box.
  `IsPreconnected.induction₂'` on `[a, b]` then gives every pair. (a) is the same induction applied to `|X|²`.

## The witness, `kg_witness`

***The setting.***
- `N = ℝ²` with `g = −dU dV`, which is shown Lorentzian.
- `χ = (−U, V)`, with `L_χ g = 0` through the registered `lieDeriv`.
- `γ(s) = (0, e^s)` for `s ∈ [0, 10]`, an integral curve of `χ`.

***What it shows.***
- `g(χ, χ) = UV`, so `χ` is null on `U = 0`.
- **`γ 0 = (0, 1) ≠ (0, e¹⁰) = γ 10`.**
- `kg_Related 0 10` and `kg_Related 10 0` both hold.
- `Δτ = 0`.

## Hypotheses beyond the registration

- `γ` is an integral curve on a neighbourhood of each parameter, endpoints included. That is slightly stronger than
  the registered velocity condition, which is now conclusion 1, and is needed for local uniqueness at `a` and `b`.
- `X` needs to be C¹ only along `γ`, which is weaker than registered.
- `T2Space N` is not needed.

## Marks

***4b and 4c → BUILT on the manifold, along a whole generator.***
- 4b: `ds² = |χ|² dλ² = 0`, forced along the generator.
- 4c: the flow is a local isometry carrying the generator into itself, so the transverse invariants are equal at `p`,
  at `q`, and between them.

***4d → BUILT IN PART.***
- `p` and `q` are metrically coincident in (a), (b) and `Δτ = 0`.
- `Δx = 0` along the whole generator is box-local only.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
