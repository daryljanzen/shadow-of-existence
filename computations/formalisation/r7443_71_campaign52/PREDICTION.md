# `r7443+71.61` — PRE-REGISTRATION: campaign 52, programme stage P1 — integration on S³ and the symmetry of `∇²`. ⌗ `700` lines (band 400–1400), ⛔ stop `2000`. ⌗ p `0.45`

*The first stage of `r7443_71_pw_programme/PROGRAMME.md`. No Lean was written before this registration.*

## ① The piece: `probes/S3Integration.lean`

1. ***The measure.*** `σ` is the surface measure on the unit sphere of `ℝ⁴`: Mathlib's `Measure.toSphere`, or the
   pushforward that defines it. It is finite and nonzero.
2. ***Invariance.*** For every unit quaternion `g`, the right translation `q ↦ q·g` is a linear isometry of `ℝ⁴`
   preserving the sphere, and `σ` is invariant under it. The left translations likewise.
3. ***The frame fields integrate to zero.*** For every `C¹` function `f` on a neighbourhood of the sphere,
   `∫ (E_a f) dσ = 0`, where `E_a f (q) = d/dt f(q·exp(t u_a))|₀` is campaign 51's frame derivation. Proved by
   differentiating `t ↦ ∫ f(q·exp(t u_a)) dσ`, which is constant by item 2, under the integral sign.
4. ***Integration by parts.*** `∫ (E_a f) g dσ = −∫ f (E_a g) dσ`. ***Consequences:***
   - for tensor fields with `C²` components, `∫ ⟨∇²h, k⟩ dσ = ∫ ⟨h, ∇²k⟩ dσ`;
   - `∫ ⟨−∇²h, h⟩ dσ = Σ_a ∫ |∇_a h|² dσ ≥ 0`.

   Both use the connection terms `ε_abc` from campaign 51, and their antisymmetry.
5. ***A sanity instance.*** For polynomial `f`, item 3 checked against campaign 51's `D a` on `ℂ[x₀..x₃]`. That ties
   the analytic derivation to the algebraic one.

***Failable:*** BUILT, BUILT IN PART (items 1–3 without 4, or 4 for functions but not tensors), or REPORTED, with
the blocking Mathlib step named. p `0.45`. ***Risks:***
- differentiating under the integral sign on the sphere measure;
- the unit quaternions acting as `LinearIsometryEquiv`;
- `toSphere`'s API.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
