# Inventory of P1 (`corpus/BH_causality_v2.tex`) against the Lean probes: refresh under `r7685+71.1` ②

*A reading, done by the method of `r7643_71_inventory/PREDICTION.md`, which is unchanged. P1 is read as it stands at
`4003e41f` (r7685), so its new attestations are included: the remark after `thm:metric-singularity` (l.140), Section
3's paragraph (l.228), the end of `lem:killing`'s proof (l.278), `rem:formalised`'s seventh family (l.313),
`cor:densities`' proof (l.325) and the end of `lem:alignment`'s proof (l.382). The probes are read through campaign
101. Campaign 93 is now counted (it was in progress at r7667). Campaign 102 ① (`SchwarzschildShellHorizon.lean`, the
frontier of `D` on the shell) is registered and not built, so it is not counted. Every Lean name below was checked by
grepping the probes for its declaration. The previous inventory is `r7667_71_inventory/INVENTORY.md`.*

**The marking rule (unchanged).**
- **BUILT**: the Lean covers the clause under hypotheses no stronger than P1's, and is non-vacuous.
- **BUILT IN PART**: the gap is named. It is a stronger hypothesis, a reduced setting (a chart, 2D), or a missing
  non-vacuity witness.
- **NOT BEGUN**.

A row whose mark moved since r7667 is tagged **⇧ moved**. A row whose mark stayed but whose gap changed is tagged
*(gap narrowed)*. Otherwise *(unchanged)*.

***One reading applied throughout: the radial plane.*** The Schwarzschild rows (3a, 3b, 8i, 8ii-a, 8ii-b) are proved
on the radial plane, with the angles suppressed. They are marked **BUILT (radial plane)** here, because:
- P1's own statements write them in `(v, r)` (l.221, l.340), and `lem:alignment` (i) names "the angle-suppressed
  radial picture" (l.351);
- P1 attests them "on the radial plane" (l.228, l.382), and 69's r7685 order calls 8ii-b "built in the setting P1
  states".

Under the strict reading, where 2D is a reduced setting, those five rows drop to BUILT IN PART, with one shared gap:
the 4D warped product `−F dU dV + r² dΩ²`. The summary gives both counts.

## The population

The grep for `\begin{theorem|proposition|lemma|corollary}` still finds the same **8**. The line numbers have moved:
- `thm:metric-singularity` (l.130);
- `cor:threefold` (l.166);
- the EF-degeneracy corollary (l.220, unlabelled);
- `lem:killing` (l.269);
- `cor:stationary` (l.283);
- `prop:causal-alignment` (l.302);
- `cor:densities` (l.320);
- `lem:alignment` (l.338).

No remark was added. The remark after the theorem (l.139) now cites the `ac_` theorems. `rem:formalised` is at l.310.

## What landed since r7667

| Campaign | Probe | Rows it moves |
|---|---|---|
| 93 | `GeneratorStretch.lean` (`gs_`), `Densities.lean` (`dn_`) | 6b-ii (gap), 7a, 7c |
| 94 | `AlongConnection.lean` (`ac_`), `KillingLocal.lean` (`kl_`) | 1b, 2iv-a, 1c (in part) |
| 95 | `KillingGenerator.lean` (`kg_`) | 4b, 4c |
| 96 | `KillingWhole.lean` (`kw_`) | 4d, and so 4a |
| 97 | `SchwarzschildKruskal.lean` (`sk_`), `SchwarzschildKilling.lean` (`sq_`) | 3a, 3b, 1c (in part) |
| 98 | `SchwarzschildEF.lean` (`se_`), `SchwarzschildAlign.lean` (`sa_`) | 8i, 8ii-a, 8ii-b (stationary) |
| 99 | `SchwarzschildRetarded.lean` (`sr_`) | 8ii-b: retarded refuted on the eternal exterior |
| 100 | `SchwarzschildConformal.lean` (`sx_`) | 8i with P1's own `𝓗⁺ = ∂J⁻(𝒥⁺)` |
| 101 | `SchwarzschildCollapse.lean` (`sv_`) | 8ii-b (retarded, on a collapse) |

*A name clash to know about:* `kw_` is used by two probes. In `KillingWitness.lean` (campaign 82) it is the
global-chart witness (`kw_lemma_killing_witness`, `kw_coincident_concrete`). In `KillingWhole.lean` (campaign 96) it is
the whole lemma (`kw_lemma_killing_whole`, `kw_witness`). Below, the file is named whenever it matters.

---

## 1. `thm:metric-singularity` (l.130)

**1a.** (a) `Δs² = 0` and (b) `Δx = 0` give `Δτ = 0`.
- **Lean:** `MetricSingularity.lean` · `ms_metric_singularity_scalar`, `ms_metric_singularity_vec`.
- **Mark: BUILT** (unchanged).

**1b.** The along-the-connection form, on 69's ruling 2 (r7669): `Δτ = ∫ N |dt(γ′)|`, the frame's temporal leg, with
the lapse `N` allowed to vanish.
- **Lean:** `AlongConnection.lean` · `ac_metric_singularity_along`. It takes an `AdaptedSplitting` along `γ` on an
  `MSpacetime` on any manifold, `g = h − N² dt ⊗ dt`, with `h(γ′, γ′) ≥ 0` and continuous. From (a) and (b) it gives
  `Δτ = 0`, and both legs vanish pointwise.
- **Companion:** `ac_lapse_pos_forces_point` (`N > 0` and `h` positive definite on `ker dt` force `γ 1 = γ 0`), with
  `ac_lapse_pos_nonvacuous`.
- **Witness:** `ac_witness`, a Rindler-horizon generator with `γ 0 ≠ γ 1`; and `ac_witness_no_positive_lapse`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). r7667's reading flag is settled by the ruling: the frame may be
  degenerate, and the witness has `p ≠ q`. P1 l.140 states exactly this.
- *Reading note:* the splitting is supplied, not derived from a foliation. That is the ruling's form of "(b)'s
  foliation".

**1c.** "…metrically coincident…while remaining, in general, topologically distinct and causally ordered" (l.136).
- **What it claims, formally:** "in general" makes it an existence claim. Some pair is metrically coincident,
  distinct, and causally ordered. Its whole formal content is one witness.
- **Lean:** the three properties exist, but never in one theorem.
  - `sk_cor_EF_events` (`SchwarzschildKruskal.lean`): on Schwarzschild, `(0, V₁) ≠ (0, V₂)`, `Cau`, `¬ Chr`, both on
    `S.H J` and at `r = 2M`. Not metric coincidence.
  - `sq_cor_EF_coincident` (`SchwarzschildKilling.lean`): the same coordinate pair is metrically coincident
    (`kg_Related`, `Δx = Δτ = 0`) and distinct. No causal relation: that probe has no `MSpacetime`.
  - `ac_witness`: metric coincidence and `γ 0 ≠ γ 1` on Rindler. No causal relation in that probe either.
- **Mark: BUILT IN PART ⇧ moved** (from NOT BEGUN).
- **What remains:** one theorem conjoining the three on one pair. Today the link between `sk_` and `sq_` is a shared
  formula (`sk_hRep`, `sq_metric_formula`), not a Lean term, because probes cannot import probes. See "Cheapest next
  row", rank 3.

## 2. `cor:threefold` (l.166)

P1's hypotheses: `γ` is a future null geodesic segment from `p` to `q`, with `q ∈ ∂J⁺(p)`.

**2i.** `p ≠ q`, so they are topologically distinguishable (l.170).
- **Mark: NOT BEGUN** (unchanged).
- ***Reading flag, new in this refresh: `p ≠ q` does not follow from the hypotheses as written.***
  - Take 2D Minkowski modulo the null translation `(t, x) ~ (t + 1, x + 1)`. It is smooth, Hausdorff, time-oriented
    and chronological, since a timelike curve cannot have the null displacement `(k, k)`. The null line through `p`
    closes.
  - Let `γ` be that closed null geodesic, from `p` back to `p`. In any spacetime `int J⁺(p) = I⁺(p)`, and `p ∉ I⁺(p)`
    here. So `q = p ∈ ∂J⁺(p)`, and every hypothesis holds with `p = q`.
  - So (i) needs either `p ≠ q` stated, or a causality condition (no closed causal curve). Both of P1's own settings
    supply one: the globally hyperbolic `D` and the Killing generators.
- **What remains:** a P1 decision first, for 69. Given `p ≠ q`, "distinguishable" is Mathlib's `t2_separation` and
  has no further content.

**2ii.** The strict null ordering `p ≺_∂ q`: `q ∈ ∂J⁺(p)`, and no event strictly between them lies in `I⁺(p)` (l.173).
- **Lean:** no theorem for a point. *Re-read:* every ingredient is on `N`, in the `ConeDisjoint.lean` line of
  probes:
  - `mk_pushup'` (`Chr x y`, `Cau y z` give `Chr x z`);
  - `mk_isOpen_Ifut` (`I⁺(x)` is open);
  - `chr_cau` (`Chr` gives `Cau`).
- **Mark: NOT BEGUN** (unchanged).
- **What remains:** the theorem, and a witness.
  - *The theorem:* if `q ∈ frontier {y | Cau p y}`, `Cau p r` and `Cau r q`, then `¬ Chr p r`. If `Chr p r`, push-up
    gives `Chr p q`, so `q` lies in the open `I⁺(p) ⊆ J⁺(p)`, hence in the interior, which a frontier point is not.
  - *The witness:* a pair on a null generator with `q` on the frontier of `J⁺(p)`, for instance `(0, 1)` and
    `(0, e)` on `Pt`, using `ch_cau_iff` and `ch_chr_iff`.
  - The theorem does not need `γ` to be a geodesic. "Between" can be read as "causally between", which covers the
    points of `γ`.
  - See "Cheapest next row", rank 2.

**2iii.** `g(γ̇, γ̇) = 0` along the whole segment.
- **Lean:** `ms_threefold_iii` (flat); `lb_energy_cons` and `lb_generator_null_geodesic` (one chart, a flow box).
  New, but not this clause: `kg_lemma_killing_generator` gives null along a whole *Killing orbit*, not along a
  geodesic.
- **Mark: BUILT IN PART** (unchanged). The gap: one chart, flow-box geodesics only, not on `N`.

**2iv-a.** Under (b), the pair is metrically coincident.
- **Lean:** `ac_metric_singularity_along`, with `ac_witness`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). Same reading as 1b.

**2iv-b.** Without (b), `τ(q) − τ(p)` has no invariant meaning.
- **Lean:** `ms_threefold_iv_noninvariance`.
- **Mark: BUILT IN PART** (unchanged). The gaps: flat `ℝ^{n+1}`, the surrogate `∂_t τ ≥ c`, support in a ball.

## 3. The EF-degeneracy corollary (l.220)

P1 l.228 attests 3a and 3b on the radial plane and calls the closing remark (3c) interpretive.

**3a.** Horizon events `p`, `q` on one generator lie on distinct points of the observer's `∂J⁻`. They are causally
ordered but null-related.
- **Lean:** `sk_cor_EF_events`. For `0 < V₁ < V₂`: both points are on `S.H J ∩ M`, distinct, `Cau`, `¬ Chr`, and
  both at `r = 2M`. Witness: `sk_nonvacuous`.
- **Mark: BUILT (radial plane) ⇧ moved** (from BUILT IN PART).
- *Note:* on `N = Pt`, `S.H J` also contains the white-hole singularity outside `M`. The points used lie in `M`. On
  EF's own domain `W`, `se_foundation` has `𝓗⁺ = {U = 0, V > 0} ⊆ M`.

**3b.** Both are at `r = r_h`, so (b) holds, and they are metrically coincident.
- **Lean:** `sq_cor_EF_coincident`. `χ = (V∂_V − U∂_U)/4M` is Killing for the actual `F` (`sq_lieDeriv`) and null on
  `U = 0` (`sq_normSq`). Through `kw_lemma_killing_whole` (`KillingWhole.lean`'s): (a), `kg_Related` both ways,
  `Δτ = 0`, and `Δx = 0` in the horizon splitting. The pair is distinct. Witness: `sq_FS_nonconst`.
- **Mark: BUILT (radial plane) ⇧ moved** (from NOT BEGUN).
- *Reading note:* (b) is carried by the Killing field's horizon splitting, not by the areal radius. P1 l.228 says
  "in the horizon's own splitting". Neither probe uses curvature.

**3c.** The vertical extent in the EF diagram encodes only causal order.
- **Mark: NOT BEGUN** (unchanged). **It is interpretive and has no formal content.** P1 l.228 says so.

## 4. `lem:killing` (l.269)

P1 l.278 cites `kg_lemma_killing_generator`, `kw_lemma_killing_whole` and `kw_witness`.

**4a.** Away from a bifurcation surface there are adapted coordinates with `χ = ∂_λ`, and `g` independent of `λ`.
- **Lean:** `ld_manifold_killingChart_lieDeriv` (gives a `LocalKillingChart` from `L_X g = 0` near `p`, with `X p ≠ 0`),
  `kl_lambda_indep_N`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART).
  - r7643's notes already said P1's smooth setting meets both hypotheses (a `C²` manifold, chart-form
    differentiability). So under the rule they were never gaps.
  - The open point was that no lemma used the chart. Now `kl_lemma_killing_local`, and through it
    `kg_lemma_killing_generator`, do.

**4b.** (a): along the generator `ds² = |χ|² dλ²`, so `|χ|² = 0` is forced.
- **Lean:** `kg_lemma_killing_generator` (`E` finite-dimensional, `N` a `C²` manifold, `X` `C¹` along `γ` and nowhere
  zero, `L_X g = 0` near each `γ t`, `γ` an integral curve, `X` null at one `t₀`). It gives `g(X, X) = 0` and
  `g(γ′, γ′) = 0` on `[a, b]`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). It is on the manifold, along a whole generator.
- *Hypothesis note:* `γ` is an integral curve on a neighbourhood of each parameter, endpoints included. P1's orbit
  extends past `p` and `q`, so this is no stronger.

**4c.** (b): the flow is an isometry carrying each generator into itself, so the transverse invariants are equal at
`p`, at `q` and between.
- **Lean:** `kg_Related` for every `t₁, t₂ ∈ [a, b]`. It gives a local isometry `F` with `F(γ t₁) = γ t₂`, carrying
  the generator into itself (`kg_shift_isometry`, `kg_curve_eq_orbit`, `kg_related_trans`, `kg_related_box`).
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). Two reading notes:
  - "So every invariant is equal" is the definition of an invariant under an isometry. P1 l.278 says it "follows
    classically and is not separately machine-checked".
  - P1's gloss "vanishing expansion and shear" is not stated in Lean. It is a consequence used in prose, not a
    premise.

**4d.** `p` and `q` are metrically coincident.
- **Lean:** `kw_lemma_killing_whole`. In the horizon splitting `kw_horizonSplitting` (lapse `|X|`, `dt(X) = 1`), it
  gives `Δx = 0` and `Δτ = 0` along the whole generator (`kw_split`, `kw_h_X`, `kw_metric_singularity_along`).
  Witness: `kw_witness` (Rindler, `[0, 10]`, `γ 0 ≠ γ 10`).
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). **`lem:killing` is whole.**
- *Reading note (ruling 2):* `h = g` on `γ`. It is non-negative on `γ′` but not positive semidefinite in every
  direction.

## 5. `cor:stationary` (l.283)

**5.** The event horizon of a stationary black hole is a metric singularity, by rigidity (l.288).
- **Lean:**
  - `KillingHorizon.lean` · `kh_cor_stationary` under `Rigidity n H`;
  - witness `KillingWitness.lean` · `kw_cor_stationary_witness`, `kw_rigidity`.

  All of this is in the old global `KillingChart` on `ℝ × E`. Nothing since campaign 83.
- **Mark: BUILT IN PART** (unchanged). Exactly what remains:
  1. **The corollary on `N`.** Its hypothesis is the conclusion of rigidity, stated on an `MSpacetime`: "`S.H J` is a
     Killing horizon", meaning a `C¹` field `χ` with `L_χ g = 0` near `𝓗⁺`, and through each non-bifurcation point
     of `𝓗⁺` an integral curve of `χ` inside `𝓗⁺`, null there. Then `kw_lemma_killing_whole` applies to any two
     points of one curve. Nothing like this is in a probe that has both `MSpacetime` and `kw_`. `SchwarzschildKilling.lean`
     and `KillingWhole.lean` have no `MSpacetime`.
  2. **A witness on an actual event horizon.** Schwarzschild's `𝓗⁺ = ∂J⁻(𝒥⁺)` on `W` (`sx_prop_causal_alignment`),
     with `sq_`'s `χ`. That needs `sq_lieDeriv` and the integral curve carried from the model `ℝ²` to the `Opens`
     subtype `W`.
  3. **Rigidity itself stays a hypothesis.** That is no stronger than P1, which cites it (l.288: Hawking, with
     analyticity). Proving it needs the Einstein equations, which are not in the kit. **This part is out of reach and
     is not a gap under the rule.**
  4. **"Stationary" has no formal content once rigidity is assumed.** P1 uses it only to invoke rigidity. This part
     is interpretive.

## 6. `prop:causal-alignment` (l.302)

Unchanged since r7667 except for 6b-ii and the witnesses.
- **The theorem:** `cd_prop_causal_alignment` (`ConeDisjoint.lean`), with `mx_H_eq_boundary`.
- **Its hypotheses against P1's:** unchanged; see r7667 §6.
- **The seventh witness family is new.** It is Schwarzschild's radial plane on `W`: `se_headline` (campaign 98), and
  `sx_prop_causal_alignment` (campaign 100), which is `cd_prop_causal_alignment` itself, through `sx_ext`, with
  `𝓗⁺ = ∂J⁻(𝒥⁺)` and `𝒥⁺` the plane's `r → ∞`. So the identification is now witnessed off flat space too, still in
  2D only. P1 l.313 says so.

| Row | Clause | Mark |
|---|---|---|
| 6a | No cone meets `𝓗⁺` (`cd_cone_disjoint`) | BUILT (unchanged) |
| 6b-i | Cones converge; the stretch extends without bound (`mc_cone_kuratowski_N`, `hs_stretch_N`) | BUILT (unchanged) |
| 6b-ii | …"to the future" along the generators | **BUILT IN PART** *(gap narrowed)* |
| 6c | Slices accumulate on `𝓗⁺` and nowhere else (`mh_causal_alignment_gh_N`) | BUILT (unchanged) |
| 6d | Finite slices lie in `D`, and meet `𝓗⁺` only in the limit (`mh_not_mem_D_of_H`) | BUILT (unchanged) |
| 6e | Tangency, conditional (`mc_tangency_N`, `tc_tendsto`) | BUILT (unchanged) |
| 6f | The headline (`cd_prop_causal_alignment`) | BUILT (unchanged) |

**6b-ii.**
- **Lean:** `GeneratorStretch.lean` · `gs_future_stretch`, `gs_segment_stretch`, from the named hypothesis
  `HasFutureGenerators`. It is discharged on the 4D witness (`gs_hasFutureGenerators`, `gs_witness`).
- **What remains:**
  - `HasFutureGenerators` is the achronal-boundary theorem's conclusion, a consequence of P1's setting taken as a
    hypothesis. Under the rule that is BUILT IN PART.
  - 69 ruled (r7669, ①(b) (ii)) to leave it there: the general proof's global temporal function is not P1's
    hypothesis, at 2500–6000 lines.
  - "Monotonically" is in P1's proof (l.307), not its statement. `rem:formalised` says the Lean gives eventual
    containment.

***`rem:formalised` against the Lean.*** Every name in l.311 and l.313 greps to a declaration. These include
`gs_segment_stretch`, `gs_future_stretch`, `gs_witness`, `se_headline`, `sx_prop_causal_alignment`, `cz_Ω_sq`,
`cz_Ω_nonconst` and `cz_exp_nonvacuous`. "No conformal extension … for the cylinder, the four-dimensional or the warped
family" still holds.

## 7. `cor:densities` (l.320)

P1 l.325 cites `dn_cor_densities` and `dn_witness`, and says the matter statements are not formalised.

**7a.** No finite exterior slice contains any part of the black-hole region `M ∖ J⁻(𝒥⁺)`.
- **Lean:** `Densities.lean` · `dn_BH_inter_slice`, on `N`, for every `Θ`, with no Cauchy hypothesis.
  Witness: `dn_witness`, where the BH region is the non-empty `{U ≥ 0}` (`dn_preimage_Jpast_scri`).
- **Mark: BUILT ⇧ moved** (from BUILT IN PART).

**7b.** …so none contains the horizon.
- **Lean:** `dn_slice_inter_frontier`, `dn_slice_inter_H`; also `mh_not_mem_D_of_H`.
- **Mark: BUILT** (unchanged).

**7c.** …or a curvature singularity the horizon encloses.
- **Lean:** `dn_subset_BH_inter_slice`: any set inside the BH region meets no slice.
- **Mark: BUILT IN PART ⇧ moved** (from NOT BEGUN), on the reading "the singularity lies in the BH region".
- **What remains is interpretive.** The kit has no notion of a curvature singularity. In standard GR a singularity
  is not a set of points of `M`: on `W`, `r = 0` is `UV = 1`, outside the manifold. Defining one (geodesic
  incompleteness, or a boundary construction) is far outside the kit.

**7d.** On every finite slice the collapsing matter lies outside `𝓗⁺`, finite in extent, each element still
approaching its own horizon event.
- **Lean:** none for the clause. *New since r7667:* a matter model exists. Campaign 101's `sv_S` is a thin ingoing
  null shell at `v = v₀`, flat for `v ≤ v₀` (`sv_flat_past`) and Schwarzschild after (`sv_vacuum`, `sv_Φ_gt_one`),
  with `D = M` (`sv_D`) and the retarded slicing Cauchy (`sv_cauchy`).
- **Mark: NOT BEGUN** *(gap narrowed)*. Exactly what remains:
  1. **Name the matter.** Define it as the shell set `{v = v₀} ∩ M`. This is a modelling choice: the kit has no
     stress-energy, so "the matter" is read off the metric's junction, not derived.
  2. **"Outside `𝓗⁺`" and "finite in extent".** For each `τ`, the slice meets the shell in exactly one point. There
     `r = (v₀ − ũ)/2 > 2M`, which is finite and outside `r_h`.
     - *Existence* needs the shell's null ray as an `InextCausalCurveIn D`, then `sv_cauchy`.
     - *Uniqueness* follows from temporality.
  3. **"Approaching its own horizon event".** The shell ray reaches `𝓗⁺` at `ũ = u_H`. That needs `𝓗⁺ ⊆ M`, which is
     campaign 102 ① (`sh_frontier`, registered, not built).
  4. **Limits:** the radial plane has one element. "Each infalling element" (the 2-sphere's points) is not modelled.
     And the flat past has no regular centre.

**7e.** The densities of the central singularity never form at any finite exterior time.
- **Mark: NOT BEGUN** (unchanged).
- **What remains:**
  - **Formal reading (A):** the densities form where the matter reaches `r = 0`, on the shell at `ũ = v₀`, which is
    in the BH region. With 7d's bound `r > 2M` on every slice, this is 7c applied to the shell's late part. About
    50–100 lines after 7d. **But its content is the identification of "densities" with a locus, which is
    interpretive.**
  - **Substantive reading (B):** a density, meaning a stress-energy, needs the Einstein tensor of the 4D metric.
    There is no curvature in the kit. More than 2000 lines, p about 0.15. P1's own proof leans on
    Oppenheimer–Snyder (l.325), whose dust interior is not modelled either.
  - **So say it plainly: without a stress-energy, 7e has no formal content beyond 7c and 7d.**

## 8. `lem:alignment` (Schwarzschild, l.338)

**8i.** The cones miss `𝓗⁺` and climb its generators, and `S_τ` accumulates (l.350).
- **Lean:**
  - `se_headline` (Cauchy `t` on region I, properness, both Kuratowski limits, disjointness, `𝓗⁺ = {U = 0, V > 0}`
    at `r = 2M`);
  - `se_stretch`;
  - `sx_prop_causal_alignment`, with `𝓗⁺ = ∂J⁻(𝒥⁺)`.
- **Mark: BUILT (radial plane) ⇧ moved** (from BUILT IN PART).
- *Note on "climbs":* `se_stretch` puts every compact `{U = 0, V ∈ [V₁, V₂]}` eventually in the stretch, and `V`
  parametrises the generator. So the climb needs no `HasFutureGenerators` here.

**8ii-a.** For the stationary and retarded slicings, the tangent hyperplanes become tangent to the generator.
- **Lean:** `sa_stationary_aligns` (rate `F(−U)/(2V) → 0`, limit `(F(q)/2) dU`), `sa_retarded_aligns` (every
  `a, η > 0`), `sa_nonvacuous`. At every future horizon point, with the actual `F`.
- **Mark: BUILT (radial plane) ⇧ moved** (from BUILT IN PART). r7667's second gap ("`−F dU dV` taken, not derived")
  is the Kruskal form of Schwarzschild, which is a standard definition. For spherically symmetric `Θ`,
  `dΘ(e_i) = 0`, so the angles add nothing to the criterion. They are still not machine-checked.

**8ii-b.** Both slicings are Cauchy temporal functions of `D` (l.382: "they are Cauchy surfaces of `D`"), and meet
`𝓗⁺` at no finite `Θ`.
- **Lean, stationary:** `se_cauchy`, `se_headline`.
- **Lean, retarded:**
  - *On the eternal exterior:* `sr_temporal` (`η ≤ 2`, sharp by `sr_not_temporal`) and `sr_future_diverges`. But
    `sr_not_isCauchy`: it is **not Cauchy there**. That is consistent with P1, which places it in a collapse
    exterior.
  - *On a collapse:* `sv_cauchy` and `sv_cauchy_D`, on the thin-shell model, for `0 < η ≤ 2`. With `sv_retarded_eq`,
    it equals `a(u + ηr)` on the vacuum exterior.
  - *Also:* `sv_eternal_cauchy`, a change in the past alone suffices on the eternal exterior.
- **Mark: BUILT (radial plane) ⇧ moved** (from BUILT IN PART). Model limits, as P1 l.382 states them:
  - the shell is thin, so `Φ` is only `C⁰`;
  - the 2D flat past has no regular centre;
  - inside the body `Θ` is a smooth continuation, not `a(u + ηr)`.

**8ii-c.** Stationary: `g^{ab}∇t∇t → −∞`, `N → 0`. **Lean:** `ss_static_gtt_tendsto` and others. **Mark: BUILT**
(unchanged).

**8ii-d.** Retarded: `g^{ab}∇Θ∇Θ → −2a²η`. **Lean:** `ss_ret_tendsto` and others. **Mark: BUILT** (unchanged).

**8ii-e.** The retarded slicing *accumulates on `𝓗⁺`* in a collapse exterior (l.359).
- **Mark: NOT BEGUN** *(gap narrowed)*. The Cauchy property is in hand (`sv_cauchy`). What remains:
  1. **`𝓗⁺` on the shell model.** In campaign 101, `M = D`, so `𝓗⁺` lies outside `M`. This is campaign 102 ①
     (`sh_frontier`: `∂D = {ũ = u_H} ⊆ M′`), registered and not built.
  2. **Running accumulation.** `mh_causal_alignment_gh_N` takes `LocallyOneChart`, a `C¹` metric in charts. The
     thin shell's `Φ′` has a kink, and campaign 102's registration states in advance that the machinery will not
     run. Two routes:
     - (a) a smoothed shell, which makes `r` an ODE solution;
     - (b) a version of the accumulation chain for a locally Lipschitz metric. `hl_pushup` already asks only
       `LocallyLipschitzOn`, and a piecewise-smooth kink is Lipschitz.

---

## Summary of the marks

| Statement | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| `thm:metric-singularity` | 1a, **1b** | **1c** | — |
| `cor:threefold` | **iv-a** | iii, iv-b | i, ii |
| EF corollary | **3a, 3b** | — | 3c |
| `lem:killing` | **4a, 4b, 4c, 4d** | — | — |
| `cor:stationary` | — | 5 | — |
| `prop:causal-alignment` | 6a, 6b-i, 6c, 6d, 6e, 6f | 6b-ii | — |
| `cor:densities` | **7a**, 7b | **7c** | 7d, 7e |
| `lem:alignment` | **i, ii-a, ii-b**, ii-c, ii-d | — | ii-e |

***Counts (34 rows).***

| | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| r7667 | 10 | 15 | 9 |
| **r7685 (this refresh)** | **22** | **6** | **6** |
| r7685, strict 2D reading | 17 | 11 | 6 |

***Mark moves since r7667 (all upward, none downward).***

| Row | From → to | Campaign(s) |
|---|---|---|
| 1b, 2iv-a | IN PART → BUILT | 94 (`ac_metric_singularity_along`, ruling 2) |
| 1c | NOT BEGUN → IN PART | 94, 97 (the halves, in different probes) |
| 3a | IN PART → BUILT (radial plane) | 97 (`sk_cor_EF_events`) |
| 3b | NOT BEGUN → BUILT (radial plane) | 97 (`sq_cor_EF_coincident`) |
| 4a | IN PART → BUILT | re-read; used by 94–96 |
| 4b, 4c | IN PART → BUILT | 95 (`kg_lemma_killing_generator`) |
| 4d | IN PART → BUILT | 96 (`kw_lemma_killing_whole`) |
| 7a | IN PART → BUILT | 93 (`dn_BH_inter_slice`) |
| 7c | NOT BEGUN → IN PART | 93 (`dn_subset_BH_inter_slice`, as read) |
| 8i | IN PART → BUILT (radial plane) | 98, 100 |
| 8ii-a | IN PART → BUILT (radial plane) | 98 (`sa_`) |
| 8ii-b | IN PART → BUILT (radial plane) | 98 (stationary), 99 (eternal refuted), 101 (`sv_cauchy`) |

*Gaps narrowed without a mark move:* 6b-ii (93, `gs_future_stretch`), 7d (101's matter model), 8ii-e (101's
Cauchy). *Unchanged:* 1a, 2i (with a new reading flag), 2ii, 2iii, 2iv-b, 3c, 5, 6a, 6b-i, 6c–6f, 7b, 7e, 8ii-c,
8ii-d.

***Statements whole.*** `lem:killing` and `prop:causal-alignment` (apart from 6b-ii, at 69's ruling) are whole. The
EF corollary is whole apart from its interpretive 3c. `lem:alignment` is whole on the radial plane apart from 8ii-e.

---

## Cheapest next row

These are the remaining BUILT IN PART and NOT BEGUN rows, ranked by estimated cost to **BUILT**. Cost is new lines;
the copied base is not counted. Rows with no formal content are listed last.

| Rank | Row | Lines | p | Interpretive? |
|---|---|---|---|---|
| 1 | **2i** | 10–40 after a ruling | 0.95 | **Yes, nearly.** Needs a P1 decision first |
| 2 | **2ii** | 100–200 | 0.85 | No |
| 3 | **1c** | 120–250 (Rindler); 150–300 (Schwarzschild) | 0.85 / 0.75 | No: a witness is its whole content |
| 4 | **2iii** | 250–400 | 0.65 | No |
| 5 | **7d** | 250–500, after campaign 102 | 0.55 | In part (naming the matter) |
| 6 | **5** | 300–600 | 0.6 | In part ("stationary"; rigidity cited) |
| 7 | **2iv-b** | 300–600 | 0.55 | No |
| 8 | **8ii-e** | 600–1500, after campaign 102 | 0.4 | No |
| 9 | **6b-ii** | 2500–6000 | 0.15–0.3 | No. Ruled to wait (r7669) |
| — | **7e** | (A) 50–100 after 7d; (B) > 2000 | (A) 0.9; (B) 0.15 | **(A) is interpretive** |
| — | **7c** remainder | > 3000 | < 0.1 | **Interpretive** as P1 states it |
| — | **3c** | — | — | **Interpretive. No formal content** |

### 1. 2i — `p ≠ q`
- **Needs beyond the probes:** a ruling on the reading flag in §2.
  - If 69 writes `p ≠ q` into (i)'s hypotheses, (i) is `t2_separation`, about 10–20 lines.
  - If it adds a causality condition, it needs a "closed causal curve" notion on `N`, about 150–300 lines, p 0.7.
- **Expected stop:** none.
- **Interpretive:** given `p ≠ q`, yes. It has no formal content beyond Hausdorffness. **Not recommended as a Lean
  row. Recommended as a question to 69.**

### 2. 2ii — the strict null ordering
- **Needs:** one theorem on `N` and one witness, in a copy of `Densities.lean` (which has `mk_pushup'`,
  `mk_isOpen_Ifut`, `chr_cau`, `ch_cau_iff` and `ch_chr_iff`).
  - *Theorem (about 40–80 lines):* define `J⁺(p) = {y | Cau p y}`. If `q ∈ frontier J⁺(p)`, `Cau p r` and `Cau r q`,
    then `¬ Chr p r`. The proof is push-up, openness of `I⁺(p)`, and `I⁺ ⊆ J⁺` ⊆ interior.
  - *Witness (about 60–120 lines):* on `Pt`, `p = (0, 1)` and `q = (0, e)` (or any `V₁ < V₂`), with `q` on the
    frontier of the quadrant `J⁺(p)`, and points strictly between.
- **Expected stop:** none in the theorem. The likeliest difficulty is computing `J⁺(p)` as the closed quadrant on the
  witness, if `ch_cau_iff` needs both points in one chart's source.
- **Interpretive:** no. Its content is push-up, which P1 uses silently.
- **After it:** 2ii is BUILT. The hypotheses are weaker than P1's: no geodesic is needed, and "between" covers all
  causally intermediate events.

### 3. 1c — distinct, ordered, and metrically coincident, in one theorem
- **Route A, Rindler (cheaper).** Add `AlongConnection.lean`'s `ac_` section (442 lines; its `MSpacetime` is
  textually the same as the kit's) to the probe of rank 2.
  - Restate `ac_witness` on `Pt` and conjoin `Cau`, `¬ Chr` and `∂J⁻` membership.
  - About 120–250 new lines, p 0.85.
  - **Expected stop:** moving `ac_witness` from the model `P` to the `Pt` synonym (`vel` through
    `extChartAt p₀`).
- **Route B, Schwarzschild (P1's exemplar).** Merge `SchwarzschildKilling.lean` (4155 lines) into a copy of
  `SchwarzschildConformal.lean`.
  - Exactly 8 top-level declarations clash. All are the same copied kit: `hRep`, `chartRep` and six `ld_` lemmas.
  - Then show `(sk_S hM).g = sq_g M` on `M`, and conjoin `sk_cor_EF_events` with `sq_cor_EF_coincident`.
  - About 150–300 new lines, p 0.75.
  - **Expected stop:** the two kits' `variable` contexts (`IsManifold 2` against `1` on `Pt`, `FiniteDimensional`).
- **Interpretive:** no, but its content is only a witness. "In general" makes 1c existential.

### 4. 2iii — null along any null geodesic, on `N`
- **Needs:** unchanged from r7667. A chart-wise geodesic on `N` and the chart invariance of `g(γ̇, γ̇)`.
- **Expected stop:** there is no Levi-Civita connection on `N` in the probes.
- **Interpretive:** no.

### 5. 7d — the matter on finite slices
- **Needs:** campaign 102 ① first (`𝓗⁺ ⊆ M′`). Then, in its probe:
  - the shell set;
  - the shell ray as an `InextCausalCurveIn D`;
  - one point per slice (`sv_cauchy`), at `r > 2M`;
  - the ray reaching `𝓗⁺` at `ũ = u_H`.
- **Expected stop:** building the shell ray as an inextendible causal curve in `D` and getting the slice point from
  the Cauchy property.
- **Interpretive:** in part. "The matter is the shell" is a modelling definition, and "each element" is a 2-sphere's
  worth that the radial plane does not carry.

### 6. 5 — `cor:stationary` on `N`
- **Needs:**
  - a manifold-level "`S.H J` is a Killing horizon" hypothesis and the corollary through `kw_lemma_killing_whole`,
    about 100–200 lines;
  - a witness on Schwarzschild's `∂J⁻(𝒥⁺)` on `W`, through route B's merge plus `sq_lieDeriv` and the integral curve
    carried to the `Opens` subtype, about 200–400 lines.
- **Expected stop:** that transport to the subtype. A witness on `Pt`'s `S.H J ∩ M` avoids it, at p 0.7, but it
  lacks the `∂J⁻(𝒥⁺)` identification.
- **Interpretive:** in part. Rigidity stays a hypothesis, which P1 cites and the kit cannot prove (no Einstein
  equations). "Stationary" carries no formal content once rigidity is assumed.

### 7–9. 2iv-b, 8ii-e, 6b-ii
- **2iv-b.** Needs the bump deformation on `N`, keeping `dτ` positive on the future cone over a compact support. The
  expected stop is the `C¹`-smallness estimate on `N`.
- **8ii-e.** Needs campaign 102, then either route: a smoothed shell (`r` an ODE solution), or a Lipschitz form of
  the accumulation chain. The expected stop is the kit's uses of `C¹` beyond push-up.
- **6b-ii.** Waits, by 69's ruling.

### Recommendation

**Take 2ii.** It costs about 100–200 new lines, at p 0.85, with no expected stop.
- It is the cheapest row with real formal content: push-up on `N`, which P1's (ii) uses without saying so.
- It needs no new kit and no dependency on campaign 102.
- **The natural extension:** add rank 3's route A in the same probe, for about 120–250 more lines (total about
  250–450, p 0.8). The witness pair is shared, and it moves 1c to BUILT too.
- **Put 2i to 69 alongside it.** Under the stated hypotheses, `p = q` is possible on a chronological spacetime with a
  closed null geodesic. So (i) needs `p ≠ q` stated, or a causality condition.
- **For 5 and 7d/7e, stated plainly:**
  - 5's remaining formal step is an application of the whole `lem:killing` on `N` (rank 6). Its rigidity part is
    cited, not provable here.
  - 7d is buildable on the shell model once campaign 102 lands (rank 5).
  - 7e has no formal content without a stress-energy.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
