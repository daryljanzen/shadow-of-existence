# `r7613+71.8` — RESULT: campaign 60, `r7613` ③, the causal layer BUILT; `prop:causal-alignment`'s elementary clauses and `cor:densities` BUILT; the tangency clause REPORTED as registered. ⌗ `757` lines in one probe (registered `1500`, band 600–4000). ⌗ every registered p for a built piece came true; tangency (p `0.1`) did not land, as expected

*Against `PREDICTION.md` (`r7613+71.4`). 71 re-ran `lake env lean probes/CausalStructure.lean`. It exits 0 with
no errors. All `25` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## Definitions (single chart, as registered)

***Spacetime.***
- A `Spacetime V` over any real normed space consists of:
  - an open `M`;
  - a continuous symmetric `g`;
  - a continuous `T` with `g(T, T) < 0`;
  - `g` positive definite on `T^⊥`, so the signature is `(−,+,…,+)`.
- No Mathlib-manifold version is attempted.

***Vectors and curves.***
- Future timelike and future causal vectors are defined against `T`.
- A timelike or causal step is a C¹ curve `γ : ℝ → V` inside `M` on `[0,1]`, with future timelike or future causal
  velocity there.
- `≪` is the transitive closure of timelike steps. `≤` is the reflexive-transitive closure of causal steps. So
  `I±` and `J±` are endpoints of piecewise-C¹ curves.
  - Caveat: a C¹ piece on `[0,1]` is assumed to extend C¹ to `ℝ`.
  - Caveat: curves stay in `M`, endpoints included.

***Temporal functions and global hyperbolicity.***
- `IsTemporal` is C¹ with `dτ(v) > 0` on future-causal `v`.
- `IsCauchyTemporal` requires every inextendible piecewise causal curve to meet each level set exactly once.
- `GloballyHyperbolic` is the existence of a Cauchy temporal function. This is the Bernal–Sánchez equivalent, taken
  as the definition; the equivalence is not proved.

***Null infinity is HYPOTHESIS-SUPPLIED.***
- `𝒥⁺` is an arbitrary set `J`.
- `D = I⁻(J)`, `𝓗⁺ = frontier J⁻(J)`, and the black-hole region is `M ∖ J⁻(J)`.
- No conformal completion is built.

## Theorems

| result | what it says | status |
|---|---|---|
| `cs_chr_trans`, `cs_cau_trans`, `cs_chr_cau` | `≪` and `≤` are transitive, and `≪ ⊆ ≤` | BUILT |
| `cs_pushup`, `cs_pushup_set`, `cs_pushup'` | push-up `q ≤ p ≪ z ⟹ q ≪ z`, its set form, and the time-reversed form `q ≪ p ≤ z ⟹ q ≪ z` | BUILT, for **locally Lipschitz `g`** |
| `cs_isOpen_Ipast`, `cs_isOpen_Ifut`, `cs_isOpen_IpastSet`, `cs_isOpen_IfutSet` | `I±(p)` and `I±(S)` are open | BUILT (genuine C¹ pieces, a compactness argument on `[0,1]`, continuity of `g` only) |
| `cs_D_open`, `cs_D_subset_interior`, `cs_D_inter_H` | `D` is open, lies in the interior of `J⁻(𝒥⁺)`, and misses `𝓗⁺` | BUILT |
| `cs_Ipast_inter_H` | `I⁻(p) ∩ 𝓗⁺ = ∅` for `p ∈ D` | BUILT |
| `cs_Jpast_inter_H` | `J⁻(p) ∩ 𝓗⁺ = ∅` for `p ∈ D` (via push-up) | BUILT |
| `cs_lightcone_inter_H` | `∂J⁻(p) ∩ 𝓗⁺ = ∅`, with closedness of `J⁻(p)` as a hypothesis | BUILT |
| `cs_worldline_cones`, `cs_observer_Ipast` | no past cone of the observer's worldline meets `𝓗⁺` | BUILT |
| `cs_slice_subset_D`, `cs_slice_subtype` | every finite-`Θ` slice lies in `D` | BUILT |
| `cs_BH_inter_D`, `cs_BH_inter_slice`, `cs_BH_inter_slice_subtype` (`cor:densities`) | the black-hole region misses `D`, and so misses every finite slice | BUILT |
| `cs_temporal_chr`, `cs_GH_chronological` | a temporal function increases along `≪`; global hyperbolicity rules out `x ≪ x` | BUILT (extra) |

Notes on two of the rows:
- **The Lipschitz hypothesis on push-up** is a hypothesis the paper does not state. It is needed, because push-up
  fails for merely continuous metrics (the causal bubbles of Chruściel–Grant 2012). The paper's smooth `g`
  satisfies it.
- **Closedness of `J⁻(p)`** is used by the light-cone clause. It follows from global hyperbolicity classically, but
  it is not derived from the definition here.

## ⛔ REPORTED, as registered: the tangency/convergence clause

***First missing lemma: the limit-curve lemma.***
- It says that a uniform limit of uniformly Lipschitz future-causal curves is a future-causal Lipschitz curve.
- Mathlib has Arzelà–Ascoli (`BoundedContinuousFunction.arzela_ascoli`), `LipschitzWith.uniformEquicontinuous` and
  Rademacher (`LipschitzWith.ae_differentiableAt`). What it lacks is the closure of the causal condition under
  uniform limits: the closed-cone characterisation of difference quotients.
- It also needs causal curves recast as Lipschitz curves with velocity causal almost everywhere, because the
  C¹-chain class is not closed under such limits.

***Next missing lemma: the null-generator structure of `∂J⁻(S) ∖ S`.***
- This needs geodesics of `g`, achronality, and the lemma above.

The split is the registered one: openness and disjointness are elementary and built, and the tangency clause waits
on the limit-curve lemma. No census row moves.
