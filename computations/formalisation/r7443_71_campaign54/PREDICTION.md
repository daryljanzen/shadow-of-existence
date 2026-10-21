# `r7443+71.63` — PRE-REGISTRATION: campaign 54, programme stage P3 — polynomial tensor fields are dense on S³. ⌗ `350` lines (band 150–800), ⛔ stop `1200`. ⌗ p `0.60`

*The third stage of `r7443_71_pw_programme/PROGRAMME.md`. No Lean was written before this registration.*

## ① The piece: `probes/S3Density.lean`

1. The restrictions to the unit sphere `S³ ⊂ ℝ⁴` of real polynomials in `x₀..x₃` form a subalgebra of `C(S³, ℝ)`. It
   separates points and contains the constants. By Stone–Weierstrass it is dense in the sup norm.
2. Hence it is dense in `L²(σ)` for the sphere measure `σ` (finite on a compact set), via density of `C(S³)` in
   `L²` (`ContinuousMap.toLp_denseRange` or equivalent).
3. The same componentwise for symmetric traceless 2-tensor fields in the left-invariant frame. The frame components
   of a polynomial tensor are polynomial, because the frame is linear in `q`. The same holds for the traceless
   projection.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. p `0.60`. ***Risk:*** how `σ` is presented (`Measure.toSphere`
or a subtype measure) and which `Lp` density lemma applies to it.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
