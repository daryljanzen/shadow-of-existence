# `r7613+71.4` — PRE-REGISTRATION: campaign 60, `r7613` ③, the causal-structure layer, then `prop:causal-alignment` and `cor:densities`. ⌗ `1500` lines in up to three probes (band 600–4000), ⛔ stop `5000`. ⌗ p: definitions `0.85`, openness of `I±` `0.6`, disjointness and slices `0.7` (given openness), `cor:densities` `0.8`, tangency clause `0.1`

*Under `r7613` ③, the substantive stage. The source is `corpus/BH_causality_v2.tex`, lines 300–328. No Lean was
written before this registration.*

## ① The definitions (`probes/CausalStructure.lean`)

***Setting.***
- The work is in a single chart: `M` is an open subset of `ℝ^{n+1}`.
- `g` is a continuous field of Lorentzian bilinear forms, of signature `(−,+,…,+)`.
- `T` is a continuous timelike vector field fixing the time orientation.
- A Mathlib-manifold version is not attempted. RESULT will say so.

***Defined objects.***
- Causal and timelike vectors, future-directed by `g(v, T) < 0`.
- Future-directed timelike and causal curves, taken piecewise C¹.
- `I±(p)`, `J±(p)`, and `I±(S)`, `J±(S)` for sets.
- A temporal function, meaning C¹ with past-directed timelike gradient.
- A Cauchy temporal function, where each level set is met exactly once by every inextendible causal curve.
- Global hyperbolicity, as the existence of a Cauchy temporal function. This is Bernal–Sánchez's equivalent form,
  taken as the definition, and RESULT says so.

***Null infinity.*** `𝒥⁺` is a HYPOTHESIS-SUPPLIED set, because a conformal completion is out of reach.
- `𝒥⁺` is any set, and we work with `I⁻(𝒥⁺)` and `J⁻(𝒥⁺)`.
- The exterior is `D = I⁻(𝒥⁺)` and the horizon is `𝓗⁺ = ∂J⁻(𝒥⁺)`.
- The paper's hypothesis `J⁻(𝒥⁺)` ⊆ closure of `I⁻(𝒥⁺)` is a stated assumption if it is needed, and RESULT names it.

## ② The theorems (`probes/CausalAlignment.lean`)

- ***Openness.*** `I±(p)` is open, and so is `I±(S)`. The proof perturbs the last piece of a timelike curve. If
  needed, it uses constant-coefficient light cones in a small ball, with continuity of `g`.
- ***Push-up, the elementary half.*** `I⁻ ⊆ J⁻`, and `I⁻(S)` is open, so `I⁻(S) ∩ ∂J⁻(S) = ∅` provided
  `I⁻(S) ⊆ int J⁻(S)`, which openness gives.
- ***`prop:causal-alignment`, elementary clauses.***
  - For every exterior event `p ∈ D`, `p ∉ 𝓗⁺`.
  - `I⁻(p) ∩ 𝓗⁺ = ∅`.
  - `J⁻(p) ∩ 𝓗⁺ = ∅`, using `J⁻(p) ⊆ I⁻(𝒥⁺)` when `p ∈ I⁻(𝒥⁺)`. That uses push-up `J⁻(I⁻) ⊆ I⁻`, the
    concatenation lemma.
  - So no past light cone `∂J⁻(O(τ))` meets `𝓗⁺`.
  - Every finite-`Θ` slice `S_τ = Θ⁻¹(τ)` of a function `Θ : D → ℝ` lies in `D`.
- ***`cor:densities`.***
  - The black-hole region `M ∖ J⁻(𝒥⁺)` is disjoint from `D`.
  - So it is disjoint from every finite slice.

***Failable:*** each of the above is BUILT, BUILT IN PART, or REPORTED.

## ⛔ The registered reachable negative: the tangency clause

The clause that the `∂J⁻(O(τ))` converge to `𝓗⁺`, and that the `S_τ` accumulate asymptotically tangent to it,
needs limit-curve machinery.
- That means the limit-curve theorem: a sequence of causal curves through a convergent sequence of points has a
  causal limit curve.
- It also needs the null-generator structure of achronal boundaries: `∂J⁻(S) ∖ S` is ruled by past-inextendible
  null geodesics.
- p that it lands here is `0.1`. If it does not, RESULT REPORTS it as the split: the elementary clauses as built,
  and the first missing lemma for the tangency clause named.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
