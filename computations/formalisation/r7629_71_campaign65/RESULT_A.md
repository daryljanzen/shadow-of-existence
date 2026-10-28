# `r7629+71.4` — RESULT: campaign 65, `r7629` ①, concatenation BUILT; past-inextendible limit curves BUILT (the no-endpoint form); the generator's hypotheses discharged IN PART. ⌗ `2364` lines in one probe (registered `900`, band 300–2500, stop 3500; the full copy of campaign 63 accounts for most of it). ⌗ p: concatenation `0.75` and inextendibility `0.4` came true; the hypotheses `0.25` came partly true

*Against `PREDICTION.md` (`r7629+71.1`). 71 re-ran `lake env lean probes/CausalConcat.lean`. It exits 0 with no
errors. All `49` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## ① Concatenation

***Built, with no extra hypotheses.***
- `cc_chord_split`: across a junction, a chord quotient is a convex combination of the two sub-chord quotients.
- `cc_coneCondOn_glue`: the cone condition glues, using monotonicity and convexity of `coneHull`.
- `cc_join_lipschitz`: the join is `2·max(L₁,L₂)`-Lipschitz.
- `cc_lstep_trans` and `cc_lstepIn_trans`: `LStep` is transitive, also inside `K`.
- `cc_lcau_iff` and `cc_lcau_eq_reflGen`: `LCau x y ↔ x = y ∨ LStep x y`, so `LCau = ReflGen LStep`.

## ② Past-inextendibility

***Definitions.***
- `PastCausal γ`: every unit piece of `γ` on `[0, ∞)`, run backwards, is Lipschitz causal.
- `PastInextendible γ`: the standard form, "`γ(t)` has no limit in `M` as `t → ∞`".
- `LeavesCompacts γ`: the stronger form.

***Built.***
- `cc_exists_exhaustion`: a compact exhaustion of `M` always exists.
- `cc_exit_step`: the approximants' last exits from the interior of a compact `C` converge, along a subsequence, to a
  point of `C ∖ int C`, joined by a piece inside `C`.
- `cc_past_chain`: the exit step is iterated over the exhaustion, refining the subsequence at each stage. This
  replaces the diagonal argument.
- **`cc_past_inextendible_limit`.** Take causal curves whose final points converge to `p` and whose initial points
  eventually leave every compact set. Then there is a `PastCausal`, `PastInextendible` curve from `p`, with
  piece `n` inside `K_{n+1}`.
- `cc_past_inextendible_of_lcau`: the same from `LCau` chains, using ①.

***Hypotheses.***
- An exhaustion `K_j`; one always exists.
- A time functional `τ_j` positive on the cones over each `K_j`. It is derived from `T` only for small sets, as in
  campaign 63.

***Finding.*** For the no-endpoint form, **non-imprisonment is not needed**, contrary to what the registration
expected.

***BUILT IN PART: the "leaves every compact" form.*** `cc_past_inextendible_limit_leaves` takes non-partial-imprisonment
as an explicit hypothesis. It is not derived from strong causality.

## ③ Discharging the generator's hypotheses, IN PART

***Built.***
- `cc_approximants`: from `p ∈ closure J⁻_Lip(A) ∖ closure A`, derive the approximating pieces `Pₙ → p`, with
  `Qₙ ∈ A`, inside `K`. This needs the causal diamond `J⁻(A) ∩ J⁺(U)` to lie in a compact `K`, for some
  neighbourhood `U` of `p`.
- `cc_boundary_generator_of_diamond`: campaign 63's generator, with its approximants hypothesis replaced by that
  diamond condition.

***Not built: a past-inextendible generator.*** As registered, the stop is uniformising `τ`, since one `τ` over the
diamond is still a hypothesis.

***First missing lemma.*** A past-extension of the generator inside `∂J⁻`: a limit of pieces from points beyond `p`,
using `cc_exit_step` with a `τ_j` for each compact set, and approximants in each `K_j`.

***Out of scope this campaign, per `r7629`.*** Geodesics of `g`.

No census row moves.
