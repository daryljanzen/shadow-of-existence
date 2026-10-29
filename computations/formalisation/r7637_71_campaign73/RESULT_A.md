# `r7637+71.4` — RESULT: campaign 73, `r7637` ①–③, **the ray lemma BUILT**; **a Lipschitz causal curve from `p` on the null conoid `{Q = 0}` is a C² future-null radial geodesic BUILT**; in `𝓗⁺`, such a curve is a null pregeodesic; `Q`-monotonicity BUILT IN PART (it stops at the bootstrap that keeps `P` causal); differential tangency BUILT IN PART. ⌗ `2640` lines in one probe (about `690` new, band 300–3000 new). ⌗ p: ray lemma `0.8` came true, `Q`-monotonicity `0.5` came partly true, generators `0.3` came true given `Q = 0` as a hypothesis, tangency `0.2` came partly true

*Against `PREDICTION.md` (`r7637+71.1`). 71 re-ran `lake env lean probes/NullGenerators.lean`. It exits 0 with no
errors. All `33` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The setting is campaign 71's
probe, copied in, together with campaign 70's pregeodesics and campaign 61's closed cone.*

## ① The ray lemma

***`ng_ray_lemma`, exactly as ordered.*** If `σ` is Lipschitz on `[0,1]`, never zero on `(0,1]`, and `σ′ = kσ` almost
everywhere, then `σ(t) = μσ(1)` with `μ > 0` for every `t ∈ (0,1]`.

***Proof.***
- Choose a functional `ℓ` with `ℓσ(1) > 0`, by Hahn–Banach.
- `ng_ray_local`: on any interval where `ℓσ > 0`, `(ℓσ)⁻¹σ` is absolutely continuous with derivative 0 almost
  everywhere, so it is constant. This uses Mathlib's `AbsolutelyContinuousOnInterval.const_of_ae_hasDerivAt_zero`.
- A supremum argument shows `ℓσ` never reaches 0.

No Grönwall argument and no hypothesis on `k` is used. The registered likely stop, the Lipschitz FTC, is already in
Mathlib.

## ② Monotonicity of `Q`: BUILT IN PART

***Built.***
- `ng_Q_comp_hasDerivAt`: `(Q∘γ)′ = 2g(P, γ′)`.
- **`ng_Q_antitone`**: if `g(P, γ′) ≤ 0` almost everywhere, then `Q∘γ` is non-increasing. The proof is the FTC for
  Lipschitz functions.
- **`ng_Q_mono_of_cone`**: if `P` stays in the closed cone along a causal curve from `p`, then `Q` is non-increasing and
  `Q ≤ 0`. This uses reverse Cauchy–Schwarz.

***First missing lemma: the bootstrap.***
- The statement needed: along a Lipschitz causal curve from `p` inside the normal ball, `P(γ(t))` stays in the closed
  future cone.
- The obstruction: `g(P, w) ≤ 0` holds only once `P` is causal, and where `Q > 0` no sign is available.
- Closing it needs a quantitative estimate near the conoid, `g_x(P, w) ≤ C·max(Q,0)·‖w‖` for causal `w`, followed by a
  Grönwall step on `Q⁺`. The estimate must cope with `P(p) = 0`.

## ③ The generators are null geodesics

***`ng_generator_ray`.*** Take a Lipschitz curve from `p` in `{Q = 0}` with causal velocity a.e. Then `exp⁻¹γ` stays on
one null ray. This combines `ng_ae_null_tangent`, `ng_P_euler` and the ray lemma.

***`ng_generator_null_geodesic`.*** Such a curve, future-directed, has the same image as `radC2 v`. `radC2 v` is a C²
curve that is future-null throughout, and equals `exp_p(r v)` on `[0,1]` (`ng_radC2_contDiff`, `ng_radC2_futNull`).

***`ng_H_generator_radial_pregeodesic`.*** If the curve lies in `𝓗⁺`, campaign 70's result applies to that radial
geodesic: it is null and a pregeodesic.

***Hypothesis.*** "The generator lies on `{Q = 0}`" is assumed, not derived. Deriving it needs ②'s bootstrap together
with `ng_chr_of_Q_neg` and achronality.

## ④ Differential tangency: BUILT IN PART

***Built.*** `ng_conoid_regular`: away from `p`, `{Q = 0}` is a regular C¹ level set (`DQ ≠ 0`), and the generator
direction `P` is tangent to it.

***REPORTED.*** Campaign 72's convergence is set convergence, which carries no tangent planes. The first missing lemma
is C¹ control of the horizon:
1. near a point of `𝓗⁺`, `𝓗⁺` coincides locally with an earlier generator point's conoid, which needs ②;
2. the slices' normals converge to `P^⊥`, which needs a uniform gradient bound on `Θ` near `𝓗⁺`.

No census row moves.
