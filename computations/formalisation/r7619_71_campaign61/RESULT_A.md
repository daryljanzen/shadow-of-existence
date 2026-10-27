# `r7619+71.4` — RESULT: campaign 61, `r7619` ①, the Lipschitz causal class, its bridge, the limit-curve lemma and the Arzelà–Ascoli corollary BUILT; null generators and tangency REPORTED. ⌗ `648` lines in one probe (registered `1200`, band 500–3000). ⌗ p: class + bridge `0.7` and limit lemma `0.55` came true; generators `0.15` and tangency `0.1` did not

*Against `PREDICTION.md` (`r7619+71.1`). 71 re-ran `lake env lean probes/LimitCurves.lean`. It exits 0 with no
errors. All `14` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The setting is campaign 60's,
copied verbatim.*

## The class (the cone form, as registered)

***Definitions.***
- The closed cone is `CC x = {v | g_x(v,v) ≤ 0, g_x(v,Tx) ≤ 0}`.
- A curve is `LipCausal` when it satisfies all three of:
  - it is `L`-Lipschitz on `[0,1]`;
  - it stays in `M`;
  - every chord quotient `(γt − γs)/(t − s)` lies in `closure(convexHull(⋃ CC y))`, the union taken over the
    `ε`-neighbourhood of the arc `γ([s,t])`, for every `ε > 0`.
- The `ε`-fattening absorbs the `o(t − s)` error, so the class carries no modulus, and the limit lemma needs no
  uniformity hypothesis.

***Faithfulness, proved rather than assumed.***
- `lc_reverse_cs` gives the reverse Cauchy–Schwarz inequality, so `lc_convex_cone`: `CC x` is convex.
- `lc_coneHat_eq_cone` (finite dimension): the infinitesimal hull is exactly `CC x`.
- `lc_c1_lipCausal_iff`: a C¹ curve is `LipCausal` if and only if its velocity is in `CC` throughout.
- `lc_velocity_mem_cone_fd`: every right derivative of a `LipCausal` curve is causal.

***Bridge.*** `lc_cstep_lstep` and `lc_cau_lcau` give campaign 60's `≤` ⊆ the Lipschitz relation. This uses
`lc_chord_mem_of_deriv_mem`, the mean value theorem in convex-hull form.

## The limit-curve lemma

***`lc_limit_curve`.***
- Take uniformly `L`-Lipschitz causal curves into a closed `K ⊆ M`, converging uniformly on `[0,1]`.
- Their limit is `L`-Lipschitz, lies in `K`, and is causal.

***`lc_arzela_ascoli`.*** With `K` compact, a subsequence converges to such a curve.

***`lc_lstep_of_limit`, the endpoint form.***
- Suppose `pₙ → p` and `qₙ → q`, and uniformly Lipschitz causal pieces in `K` join `pₙ` to `qₙ`.
- Then a causal piece in `K` joins `p` to `q`.

***Scope.*** The a.e.-velocity (Rademacher) form, and its equivalence with the cone form for general Lipschitz
curves, are not proved. Only the C¹ equivalence is.

## REPORTED: null generators of `∂J⁻(S)`, and the tangency clause

***First missing lemma: a uniform Lipschitz reparametrisation.***
- In a compact `K ⊆ M`, every causal segment in `K`, reparametrised by a fixed local time function, should be
  `L_K`-Lipschitz with one `L_K` for all curves.
- Without it, the curves from `pₙ` to `S` have no common bound to feed `lc_arzela_ascoli`. The pointwise
  ingredient, `lc_coercive`, is built.

***Further missing lemmas, after that one.***
- Push-up for the Lipschitz relation, `LCau q p → Chr p z → Chr q z`.
- `int J⁻ = I⁻` for that relation.
- For tangency in addition: geodesics of `g`, so that the generators can be shown to be null geodesics. These do
  not exist in this setting.

No census row moves.
