# `r7639+71.4` — RESULT: campaign 76, `r7639` ②–③. The near-conoid estimate is BUILT in its registered annulus form, the causal-`P` bootstrap is BUILT for causal curves that are C¹ at `p`, and the generators of `𝓗⁺` are null geodesics with campaign 73's `Q = 0` and future-pointing hypotheses removed. Differential tangency is BUILT IN PART (the generator is tangent to the regular conoid) and otherwise REPORTED at the registered blocker. ⌗ `3370` lines in one probe (about `730` new, band 250–3000 new). ⌗ p: near-conoid estimate `0.35` came true in its registered alternative form; bootstrap and generators as null geodesics `0.3` came true under a C¹-start hypothesis; differential tangency `0.12` did not

*Against `PREDICTION.md` (`r7639+71.2`). 71 re-ran `lake env lean probes/ConoidBootstrap.lean`. It exits 0 with no
errors; the 8 warnings are linter notes. All `49` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.
The forbidden-token grep is clean. The probe is campaign 73's, copied in under `ShadowProbe.ConoidBootstrapProbe`
with the prefix `cb_`.*

## ① The near-conoid estimate — BUILT, in the registered annulus form

- `cb_near_conoid`: for `w ∈ CC x`, `2·(−g(P,T))·g(P,w) ≤ (−g(w,T))·g(P,P)`. This is reverse Cauchy–Schwarz with a
  defect term.
- `cb_near_conoid_P`: on the normal ball, wherever `g(P,T) < 0`, `g(P,w) ≤ C(x)·max(Q,0)·‖w‖`, with
  `C(x) = ‖g‖‖T‖/(2(−g(P,T)))`.
- `cb_P_p`: `P p = 0`, so no uniform `C` exists at the vertex, as registered.

## ② The bootstrap — BUILT for curves C¹ at the start; the Lipschitz start REPORTED

- `cb_gronwall_step` handles the step away from `t = 0`.
- `cb_small_t` is the separate small-`t` argument. It runs an iteration `Q ≤ r t² ⇒ Q ≤ (5/6) r t²`, and needs
  `γ′ → u` at `0` with `g_p(u,T) < 0`.
- `cb_causal_in_conoid`: `P(γ t)` lies in the closed future cone, and `Q ∘ γ ≤ 0` on `[0,1]`.
- `cb_H_generator_null_geodesic`: campaign 73's generator theorem with its `Q ∘ γ = 0` and future-pointing hypotheses
  **removed**. Both are now derived:
  - `cb_generator_Q_zero` uses achronality of `𝓗⁺`;
  - `cb_orient_chart` carries the time orientation.
- **The gap.** For a merely Lipschitz start, the iteration needs `limsup (−g(γ′,T))/(−g(P,T)/t) < 2`, which a
  Lipschitz bound does not give. There, the bootstrap holds only from a time where `P ∈ CC` is already known.

## ③ Differential tangency — BUILT IN PART, the rest REPORTED

- `cb_generator_conoid_tangent` is BUILT. At every `t ∈ (0,1]`: `Q = 0`, `DQ ≠ 0`, `DQ(P) = 0`, `P` is null and
  future, and `γ′ ∥ P` a.e. So the generator is tangent to the regular conoid of `p`.
- Tangency of the slices of `𝓗⁺` is REPORTED. Two pieces are missing:
  - **The reverse inclusion.** Locally `𝓗⁺` would have to equal an earlier point's conoid, but only
    `generator ⊆ conoid` is available.
  - **The registered blocker.** A gradient bound on `Θ` near `𝓗⁺` is not implied by the hypotheses.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
