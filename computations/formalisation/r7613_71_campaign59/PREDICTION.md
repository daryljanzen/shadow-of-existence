# `r7613+71.3` — PRE-REGISTRATION: campaign 59, `r7613` ②, `lem:killing` and `cor:stationary` (rigidity as a hypothesis). ⌗ `500` lines in one probe (band 200–1200), ⛔ stop `2000`. ⌗ p: forcing `0.85`, (b) as isometric transport `0.6`, `cor:stationary` `0.7`

*Under `r7613` ②. The source is `corpus/BH_causality_v2.tex`, lines 267–298. No Lean was written before this
registration. `ShadowFormal.LapKilling` may be imported.*

## ① The pieces (`probes/KillingHorizon.lean`)

***Setting.***
- The work is in an adapted chart: an open set of `ℝ × ℝⁿ` with coordinates `(λ, xⁱ)`, a smooth symmetric metric
  field `g`, and `χ = ∂_λ`.
- `χ` is Killing in this chart, stated as `∂_λ g_{ab} = 0`. This is the Killing equation in adapted coordinates.
- `𝒦` is a set of orbits on which `χ` is normal and null.
- Away from a bifurcation surface means `χ ≠ 0` there, as `dλ ≠ 0` along the orbit.

***Forcing.***
- Along an orbit `λ ↦ (λ, x₀)`, `ds² = g_{λλ} dλ² = |χ|² dλ²`.
- If that orbit is null with `dλ ≠ 0`, then `|χ|² = 0` along it.
- Since `|χ|²` is `λ`-independent, it vanishes at every point of the orbit.

***(b) as isometric transport.***
- The flow `Φ_s(λ, x) = (λ + s, x)` is an isometry: `Φ_s^* g = g`.
- `Φ_s` maps each orbit, and `𝒦`, into itself.
- For any transverse invariant `I`, meaning any function of the metric restricted to the cross-section through a
  point, `I(Φ_s p) = I(p)`. So the transverse invariants agree at `p`, at `q`, and at every point between them, and
  `Δx = 0` holds along the generator.
- Combined with campaign 57's theorem, the generator's events are metrically coincident, `Δτ = 0`.

***`cor:stationary`.***
- The rigidity theorem, that the event horizon of a stationary black hole is a Killing horizon, is a HYPOTHESIS
  (it needs analyticity). Under it, the conclusion of `lem:killing` holds on `𝓗⁺`.

***Failable:*** BUILT, BUILT IN PART, or REPORTED per piece.

***Reachable negative:*** the coordinate-free version (a Killing field on a Mathlib manifold, with its flow) may be
out of reach, because Mathlib's manifold flows and Lie derivatives of tensors are thin. If so, the adapted-chart
version is the result and the manifold version is REPORTED, with the first missing Mathlib piece named. The chart
version is the registered target, and the manifold version is a stretch.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
