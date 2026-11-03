# `r7665+71.3` — RESULT: campaign 92, both pieces **BUILT**, and no registered stop was hit. ① The unbounded-stretch clause (`RESULT_1.md`). ② `ℝ³` with `−dU dV + e^{2UV} dy²` carries every conclusion and tangency, and **its Cotton tensor is proved non-zero in Lean** from the coordinate definitions. "Not conformally flat" follows modulo the standard invariance theorem, which was not attempted, as registered. ⌗ ① `260` and ② about `1075` new lines, both inside their bands. ⌗ p: ① `0.8`, ② causal `0.6` and Cotton `0.4`, all came true; invariance `0.05`, not attempted

*Against `PREDICTION.md` (`r7665+71.1`). 71 re-ran both probes. Each exits 0 with no errors and no warnings, and every
`#print axioms` line reads `[propext, Classical.choice, Quot.sound]` (`82` in `HorizonStretch.lean`, `87` in
`WarpedWitness.lean`). The forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE.*

## ① — see `RESULT_1.md`

## ② The warped witness

The probe copies campaign 91's general theory and drops its `FourD` witness.

***Part A, causal — BUILT.***
- **The space:** `N = E = (ℝ × ℝ) × ℝ` with `g = −dU dV + e^{2UV} dy²`, `T = ∂_U + ∂_V`, and a Rindler observer at
  `y = 0`.
- **`ww_witness_headline` discharges** `finrank 3`, `LocallyOneChart`, `hOD`, `hmono`, `hJM`, and the Cauchy property
  of `Θ = −log(−U) + V` on `D`.
- **It establishes** `D = {U < 0}` and `𝓗⁺ = {U = 0}`, which is non-empty and lies in `M`.
- **It concludes** properness, `KLi = KLs = 𝓗⁺` for the slices and for the cones, and every slice non-empty.

***How part A goes through.***
- **`D`:** a straight step to the observer, with the warp bounded along it (`ww_seg_bound`).
- **Cauchy, by the registered projection:**
  - `ww_lip`: `c·|Δy| ≤ Δ(U+V)/2` wherever `e^{UV} ≥ c`;
  - `ww_converge_future` and `ww_converge_past`: continuity of `e^{UV}` at the limit point replaces the planned
    compact neighbourhood.
- **`ww_witness_tangency q`, at every horizon point:**
  - the frame is `ℓ = ∂_V`, `n = 2∂_U`, with the transverse unit vector `e^{−UV}∂_y`;
  - the rate is `→ 0`, and the limit is `½ dU`;
  - `ww_tangency_point` instantiates it at `(0, 1, 5)`.

***Part B, the Cotton tensor — BUILT.***
- **The definitions,** built from the metric components in the global chart `(U, V, y)`, with `∂_i` as `deriv` along
  coordinate lines:
  - the metric `g_ij`, with `g_UV = −½` and `g_yy = e^{2UV}`;
  - its inverse (`ww_ginv_spec`);
  - the Christoffel symbols `Γ` and the Riemann tensor;
  - the Ricci tensor and scalar curvature `R`;
  - the Schouten tensor `S = Ric − R g/4`;
  - `∇_k S_ij`;
  - `C_ijk = ∇_k S_ij − ∇_j S_ik`.
- **The closed forms proved** match `cotton_check.py`:
  - all 27 `Γ` (`ww_Γ_eq`);
  - `Ric` (`ww_Ric_eq`);
  - `R = 8(UV + 1)` (`ww_R_eq`);
  - `S` (`ww_Sch_eq`);
  - **all 27 Cotton components** (`ww_Cot_eq`).
- **`ww_cotton_ne_zero`:** `C_{UUV} = −2V` everywhere, so `C_{UUV}(0, 1, 0) = −2 ≠ 0`.
- **`ww_gco_bridge`:** the coordinate `g_ij` is part A's `ww_S.gE` on the coordinate basis, so part B is about the
  same metric as part A.
- **The registered stop, third derivatives, was not hit.**

***REPORTED, as registered.*** The invariance theorem was not attempted: that conformal flatness implies `C = 0`, under
conformal rescaling and diffeomorphism. So the witness is proved to have a non-zero Cotton tensor. "Not conformally
flat" is that fact plus the standard theorem.

## What the remark can now say

- **The unbounded-stretch clause is formalised** for every compatible distance, as (S1) and (S2). The futureward
  direction is shown on the 4D witness. So **every clause of `prop:causal-alignment` is now in a formal statement.**
- **What is not:** the futureward direction in general, which needs the generators' inextendibility; and "monotonically
  from outside" in the proof.
- **Its closing sentence** could become: "a witness whose metric is not conformally flat, $-\mathrm{d}U\,\mathrm{d}V + e^{2UV}\mathrm{d}y^{2}$, is built, its Cotton tensor proved non-zero; that this excludes conformal flatness rests on the standard invariance of the Cotton tensor, which is not formalised."

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
