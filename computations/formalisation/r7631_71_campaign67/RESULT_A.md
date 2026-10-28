# `r7631+71.3` — RESULT: campaign 67, `r7631` ①, closedness of the causal relation on any compact set BUILT, with a C¹ time function in place of the linear `τ`; the ∂J⁻ generator BUILT through the exhaustion, future-inextendible or ending on `closure A`, with no compactness hypothesis; generators null where C¹, pregeodesics REPORTED. ⌗ `3273` lines in one probe (`2364` copied from campaign 65, about `909` new against the registered `1200`; band 400–3500). ⌗ p: `①` `0.5` came true, `②` `0.3` came true, `③` `0.1` came partly true

*Against `PREDICTION.md` (`r7631+71.1`). 71 re-ran `lake env lean probes/CausalGenerator.lean`. It exits 0 with no
errors. All `77` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## A correction to the registration

`PREDICTION.md` asked for a *past*-directed generator from `p`. A generator of `∂J⁻(A)` runs from `p` toward `A`,
which lies to `p`'s future, so the correct form is *future*-directed: it ends on `closure A`, or it is
future-inextendible. That is the standard statement, and it is what was built.

## ① A time function in place of the linear `τ`

***Route.*** This is not the registered per-ball Lebesgue-number gluing. The hypothesis is instead a `C¹` function `θ`
with `dθ_x(v) > 0` on the nonzero closed cones over `K`. This is the kind of temporal function global hyperbolicity
supplies.

***The pieces.***
- `cg_coercive_family`: compactness gives `‖v‖ ≤ c·dθ_x(v)` for cones near `K`.
- `cg_mvt_segment` and `cg_chord_bound_local`: the mean value theorem, then a local chord bound.
- `cg_chord_bound_temporal`: one constant `c` for every causal curve in `K`, obtained by cutting into short sub-arcs
  and telescoping.

***Results.***
- `cg_uniform_pieces_temporal`: one Lipschitz constant for the reparametrised curves over `K`.
- **`cg_isClosed_lstepIn_temporal`**: the causal relation is closed inside any compact `K ⊆ M`.
- `cg_temporal_of_linear`: campaign 63's linear `τ` is the special case.

## ② The generator through the exhaustion

***Machinery.***
- `cg_exit_step_closed`, `cg_past_chain_closed` and `cg_past_inextendible_limit_closed` are campaign 65's machinery,
  with closedness replacing a `τ_j` for each compact set.
- `rev` is time reversal, `T ↦ −T`, with the lemmas carrying causal curves, pieces and closedness across it.
  `cg_future_inextendible_limit` follows.

***`cg_generator`.***
- **Hypotheses:** locally Lipschitz `g`, and a global `C¹` `θ` with `dθ > 0` on the nonzero cones over `M`.
- **Conclusion:** every `p ∈ ∂J⁻_Lip(A) ∖ closure A`, with `p ∈ M`, has an achronal causal curve from `p` lying in
  `∂J⁻_Lip(A)` that is either:
  - a curve on `[0,1]` ending on `closure A` at a point other than `p`; or
  - a future-causal, future-inextendible curve on `[0,∞)`.
- **No diamond or compactness hypothesis remains.** The approximants are derived. The proof splits on whether they
  stay in one compact set of the exhaustion.

## ③ Geodesics: BUILT IN PART

***Built.*** `cg_not_timelike_of_achronal` and `cg_null_of_achronal`: wherever an achronal curve is C¹ with
velocity in the closed cone, the velocity is null. So the generators are null wherever they are C¹.

***Not built: the pregeodesic equation.***
- **First missing lemma:** a C² null curve that is not a pregeodesic of the Levi-Civita connection has two points
  joined by a timelike curve. This is the variational "corner-cutting" lemma. It needs a C¹ metric, Christoffel
  symbols in the chart, and a timelike variation field.
- **Before that:** the regularity of the generators. They are built as Lipschitz curves.

***Tangency.*** The tangency clause of `prop:causal-alignment` waits on these two.

No census row moves.
