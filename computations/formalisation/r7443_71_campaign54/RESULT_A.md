# `r7443+71.67` — RESULT: campaign 54 (programme stage P3) BUILT. ⌗ Polynomial tensor fields are dense on S³: in `C(S³)` by Stone–Weierstrass, and in `L²(μ)` for EVERY finite measure. ⌗ `267` lines (band 150–800, IN BAND). ⌗ p `0.60` came true

*Scored against `PREDICTION.md` (pushed at `r7443+71.63` before any Lean), not revised. `probes/S3Density.lean`: 14
theorems on `[propext, Classical.choice, Quot.sound]`, `14 s`, no error or warning. The build was delegated and
re-run by 71 (`PROBE_RUN_A.txt`).*

- ***Sup norm.***
  - `polyS_closure_eq_top`: real polynomials restricted to S³ are a point-separating subalgebra containing the
    constants, so their closure is all of `C(S³, ℝ)`.
  - `exists_poly_near` is the quantitative form.
- ***L².***
  - `polyL2_dense μ`: the polynomials are dense in `Lp ℝ 2 μ` for every finite Borel measure `μ` on S³. This goes
    through `ContinuousMap.toLp_denseRange`.
  - `exists_poly_near_L2_σ` is the special case of the sphere measure.
- ***Tensors.***
  - `tuple_dense_*` and `tensor_dense_*` extend density componentwise to tuples and tensors.
  - `symTL_dense_C` and `symTL_dense_L2` show it holds within the symmetric traceless tensors, via the projection
    `projTL`.
- ***The frame remark.***
  - `frameComp_mem`: frame components of a polynomial field are polynomial.
  - `projTL_frameComp_mem` gives the same after the traceless projection.

***Carried to P4:***
- the tensor statements use the product topology. A single L² norm on tensors needs a small bridge lemma (on a
  finite index set the two give the same topology);
- P3's polynomials are real while campaign 51's are complex, so a `map (algebraMap ℝ ℂ)` step links them.

***No Mathlib gap.***
