# Inventory of P1 (`corpus/BH_causality_v2.tex`) against the Lean probes: final refresh under `r7699+71.1` ①

*This reading follows the method of `r7643_71_inventory/PREDICTION.md`, which is unchanged. P1 is read as it stands
at `0a16a59a` (r7699). The probes are read through campaign 110. The previous refresh is
`r7685_71_inventory/INVENTORY.md`, which has the same 34 rows and the same marking rule. Every Lean name below was
checked by grepping its probe for a `theorem`, `lemma`, `def` or `structure` declaration. Every `\texttt{}` name in P1
is cross-checked in §"P1 against the Lean".*

**The marking rule (unchanged).**
- **BUILT**: the Lean covers the clause under hypotheses no stronger than P1's, and is non-vacuous.
- **BUILT IN PART**: the gap is named. It is a stronger hypothesis, a reduced setting (a chart, 2D), or a missing
  non-vacuity witness.
- **NOT BEGUN**.

Rows are tagged **⇧ moved** if their mark changed since r7685, and *(unchanged)* otherwise.

***The radial-plane reading (unchanged).*** Rows proved on Schwarzschild's radial plane are marked
**BUILT (radial plane)**. P1 writes those statements in `(v, r)` (l.223, l.343–344), and it attests them "on the radial
plane" (l.230, l.329, l.386). The summary also gives the strict count, which treats 2D as a reduced setting.

## What landed since r7685

All nine probes exit 0 under `lake env lean`. Each prints only `[propext, Classical.choice, Quot.sound]`. Each has no
`sorry` and no `axiom` (grep re-run for this refresh).

| Campaign | Probe | Prefix | Row(s) moved |
|---|---|---|---|
| 102 | `SchwarzschildShellHorizon.lean` | `sh_` | none on its own: it supplies `𝓗⁺ ⊆ M′` for 7d and 8ii-e |
| 103 | `ThreefoldOrder.lean` | `to_` | 2ii, 1c |
| 104 | `ThreefoldDistinct.lean` | `td_` | 2i |
| 105 | `ShellMatter.lean` | `sm_` | 7d |
| 106 | `StationaryHorizon.lean` | `st_` | 5 |
| 107 | `NullGeodesic.lean` | `ng_` | 2iii |
| 108 | `ShellAccumulation.lean` | `sa2_` | 8ii-e |
| 109 | `ThreefoldLocal.lean` | `tl_` | 2iv-b |
| 110 | `Kretschmann.lean` | `kr_` | 7c |

*Two name clashes to know about:*
- `kw_` is used by both `KillingWitness.lean` (campaign 82) and `KillingWhole.lean` (campaign 96). This inventory
  always means `KillingWhole.lean`.
- `sa_` (`SchwarzschildAlign.lean`) and `sa2_` (`ShellAccumulation.lean`) are different probes.

Probes copy each other, so many names live in several files. Only the probe named below is claimed.

---

## 1. `thm:metric-singularity` (l.130)

**1a.** (a) `Δs² = 0` and (b) `Δx = 0` give `Δτ = 0` (l.133–136).
- **Lean:** `ms_metric_singularity_scalar` and `ms_metric_singularity_vec`, both in `MetricSingularity.lean`.
- **Mark: BUILT** (unchanged).

**1b.** The along-the-connection form, `Δτ = ∫ N |dt(γ′)|`, with a lapse that may vanish (remark at l.139, text at
l.140).
- **Lean:** in `AlongConnection.lean`:
  - `ac_metric_singularity_along`;
  - `ac_lapse_pos_forces_point`;
  - the witnesses `ac_witness` and `ac_witness_no_positive_lapse`.
- **Mark: BUILT** (unchanged).

**1c.** "…metrically coincident … while remaining, in general, topologically distinct and causally ordered" (l.136).
- **Lean:** `to_cor_1c` (`ThreefoldOrder.lean`). On the Rindler-horizon generator on `Pt`, one pair is:
  - distinct;
  - `Cau` and `¬ Chr`, with the later point on `∂J⁺` of the earlier;
  - null along the generator;
  - assigned `Δx = Δτ = 0` by the adapted splitting with lapse 0.

  All of this is in one theorem, on one `MSpacetime`. Companion: `td_cor_1c_hyp` (`ThreefoldDistinct.lean`).
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). "In general" makes the clause existential, so one witness is its whole
  content.

## 2. `cor:threefold` (l.166)

P1's hypotheses (l.167) now include "no closed causal curves". P1 attests the whole corollary at l.188.

**2i.** `p ≠ q`, and they are topologically distinguishable (l.170–171).
- **Lean:** in `ThreefoldDistinct.lean`:
  - `td_ne_of_transGen` and `td_cor_threefold_i`, under `NoClosedCausal`, with `[T2Space N]` for the separation;
  - `td_transGen_of_cau_ne`.
- **The hypothesis holds in P1's settings:** `td_noClosed_of_temporal`, `td_noClosed_of_temporalOn`, `td_noClosed_D`
  and `td_minkN_noClosed`.
- **Mark: BUILT ⇧ moved** (from NOT BEGUN). r7685 flagged that `p = q` was possible under the old hypotheses. 69's
  ruling put "no closed causal curves" into l.167, and the Lean proves exactly that reading.

**2ii.** The strict null ordering `p ≺_∂ q` (l.173–174).
- **Lean:** in `ThreefoldOrder.lean`:
  - `to_strict_null_order`, with `to_Ifut_subset_interior` and `to_frontier_not_mem_Ifut`;
  - the witnesses `to_witness_order` and `to_witness_order_e`.
- **Mark: BUILT ⇧ moved** (from NOT BEGUN). The hypotheses are weaker than P1's: no geodesic is needed, and
  "between" means anything causally before `q`.

**2iii.** `g(γ̇, γ̇) = 0` along the whole segment (l.176–180).
- **Lean:** in `NullGeodesic.lean`:
  - `ng_energy_const` and `ng_cor_threefold_iii`, on `N`, along `IsGeodesicOn`;
  - the supporting `ng_Γ_exists`, `ng_Γ_unique` and `ng_geod_iff`;
  - the witness `ng_witness`, the Schwarzschild horizon generator in `∂J⁻(𝒥⁺)` on `W`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). The old gap (one chart, flow-box geodesics only) is closed: the
  theorem holds for any geodesic on `N`.

**2iv-a.** Under (b), the pair is metrically coincident (l.182–183, first sentence).
- **Lean:** `ac_metric_singularity_along` and `ac_witness` (`AlongConnection.lean`).
- **Mark: BUILT** (unchanged).

**2iv-b.** Without (b), `τ(q) − τ(p)` "is not fixed by the geometry" (l.183, last sentence).
- **Lean:** in `ThreefoldLocal.lean`:
  - `tl_cor_threefold_iv_b` and `tl_separation_interval`, on `N`;
  - the supporting `tl_iv_b`, `tl_bump`, `tl_bump_temporal` and `tl_cone_pos`;
  - the witness `tl_witness`, using `tl_minkN_temporal`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). It holds on the reading "not fixed by the geometry": the separation
  fills an open interval. P1 l.183 was reworded at r7697 from "altered arbitrarily" to match what is proved.
- *Hypotheses:* `[FiniteDimensional ℝ E]` and `[T2Space N]`. P1 l.188 states both.

**`cor:threefold` is whole.**

## 3. The EF-degeneracy corollary (l.222, unlabelled)

P1 l.230 attests 3a and 3b on the radial plane and calls 3c interpretive.

**3a.** `p` and `q` lie on distinct points of `∂J⁻` of the observer. They are causally ordered but null-related
(l.225, first sentence).
- **Lean:** `sk_cor_EF_events` and the witness `sk_nonvacuous`, both in `SchwarzschildKruskal.lean`.
- **Mark: BUILT (radial plane)** (unchanged).

**3b.** Both are at `r = r_h`, so they are metrically coincident (l.225, second and third sentences).
- **Lean:** in `SchwarzschildKilling.lean`:
  - `sq_cor_EF_coincident`;
  - `sq_lieDeriv` and `sq_normSq`;
  - the witness `sq_FS_nonconst`.
- **Mark: BUILT (radial plane)** (unchanged).

**3c.** The vertical extent in the EF diagram encodes only causal order (l.227).
- **Mark: NOT BEGUN** (unchanged).
- **Reason:** it is interpretive and has no formal content. P1 l.230 calls it "interpretive".

## 4. `lem:killing` (l.271)

P1 l.280 attests the lemma.

**4a.** Away from a bifurcation surface there are adapted coordinates with `χ = ∂_λ` (l.276).
- **Lean:** in `KillingLocal.lean`, `ld_manifold_killingChart_lieDeriv`, `kl_lambda_indep_N` and
  `kl_lemma_killing_local`.
- **Mark: BUILT** (unchanged).

**4b.** Along the generator `ds² = |χ|² dλ²`, so `|χ|² = 0` is forced (l.278–280).
- **Lean:** `kg_lemma_killing_generator` (`KillingGenerator.lean`).
- **Mark: BUILT** (unchanged).

**4c.** The flow is an isometry carrying each generator into itself (l.280).
- **Lean:** in `KillingGenerator.lean`, `kg_Related`, `kg_shift_isometry`, `kg_curve_eq_orbit`, `kg_related_trans`
  and `kg_related_box`.
- **Mark: BUILT** (unchanged). That every transverse invariant is equal is the definition of an invariant. P1 l.280
  says it "is not separately machine-checked".

**4d.** `p` and `q` are metrically coincident (l.272, l.280).
- **Lean:** in `KillingWhole.lean`:
  - `kw_lemma_killing_whole`;
  - `kw_horizonSplitting`, `kw_split` and `kw_h_X`;
  - the witness `kw_witness`.
- **Mark: BUILT** (unchanged).

**`lem:killing` is whole.**

## 5. `cor:stationary` (l.285)

**5.** The event horizon of a stationary black hole is a metric singularity (l.286, proof l.290, attested l.292).
- **Lean:** in `StationaryHorizon.lean`:
  - `st_cor_stationary`, on `N`, under `MSpacetime.IsKillingHorizon` (a `structure`, rigidity's conclusion);
  - `st_null_of_isKillingHorizon`;
  - the witness `st_witness`, with `st_isKillingHorizon`, `st_lieDeriv`, `st_hX` and `st_integral`. This is
    Schwarzschild's `𝓗⁺ = ∂J⁻(𝒥⁺)` on `W`, with `χ = ∂_t`.
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). It rests on the cited-rigidity reading:
  - Rigidity is the hypothesis, as P1 cites it (l.290: Hawking, with analyticity). That is no stronger than P1. The
    kit has no Einstein equations, so it cannot prove rigidity.
  - "Stationary" has no formal content beyond invoking rigidity.
  - The theorem is on `N` in any finite dimension. Only its witness is the radial plane, so 5 does not drop under the
    strict reading.

## 6. `prop:causal-alignment` (l.306)

P1 attests the proposition in `rem:formalised` (l.314, text l.315 and l.317). It has seven witness families.

| Row | Clause (all l.307) | Lean | Probe | Mark |
|---|---|---|---|---|
| 6a | No past cone meets `𝓗⁺` | `cd_cone_disjoint` | `ConeDisjoint.lean` | BUILT (unchanged) |
| 6b-i | The cones converge, and the stretch extends without bound | `mc_cone_kuratowski_N`; `hs_stretch_N` | `ConeDisjoint.lean`; `HorizonStretch.lean` | BUILT (unchanged) |
| 6b-ii | …"to the future" along the generators | `gs_segment_stretch`, `gs_future_stretch`, `gs_witness` | `GeneratorStretch.lean` | **BUILT IN PART** (unchanged) |
| 6c | The slices accumulate on `𝓗⁺` and nowhere else | `mh_causal_alignment_gh_N` | `ConeDisjoint.lean` | BUILT (unchanged) |
| 6d | Finite slices lie in `D` and meet `𝓗⁺` only in the limit | `mh_not_mem_D_of_H` | `ConeDisjoint.lean` | BUILT (unchanged) |
| 6e | Tangency, under the rate condition | `mc_tangency_N`, `tc_tendsto` | `ConeDisjoint.lean` | BUILT (unchanged) |
| 6f | The headline, with `𝓗⁺ = ∂J⁻(𝒥⁺)` | `cd_prop_causal_alignment`; `mx_prop_causal_alignment`, `mx_H_eq_boundary` | `ConeDisjoint.lean`; `ConformalBoundary.lean` | BUILT (unchanged) |

**6b-ii.**
- **The gap:** `gs_future_stretch` takes `HasFutureGenerators` (a `def` in `GeneratorStretch.lean`) as a hypothesis.
  That hypothesis is the achronal-boundary theorem's conclusion, so it is a consequence of P1's setting taken as given.
  It is discharged only on the 4D witness, by `gs_hasFutureGenerators` and `gs_witness`.
- **Why it waits:** 69 ruled (r7669, ①(b) (ii)) to leave it there. The general proof needs a global temporal function,
  which is not P1's hypothesis, and costs 2500–6000 lines.
- P1 l.315 states the gap ("which the formalisation does not include in general").

**`prop:causal-alignment` is whole apart from 6b-ii, which waits by ruling.**

## 7. `cor:densities` (l.324)

The statement is at l.325. P1 attests it at l.329.

**7a.** No finite exterior slice contains any part of the black-hole region.
- **Lean:** in `Densities.lean`:
  - `dn_cor_densities` and `dn_BH_inter_slice`;
  - the witness `dn_witness`, with `dn_preimage_Jpast_scri`.
- **Mark: BUILT** (unchanged).

**7b.** …so none contains the horizon.
- **Lean:** `dn_slice_inter_frontier` and `dn_slice_inter_H` (`Densities.lean`); `mh_not_mem_D_of_H`
  (`ConeDisjoint.lean`).
- **Mark: BUILT** (unchanged).

**7c.** …or a curvature singularity the horizon encloses.
- **Lean:** in `Kretschmann.lean`:
  - the main results `kr_schwarzschild` (`K = 48M²/r⁶`), `kr_blowup` and `kr_cor_densities_c`;
  - the supporting `kr_warped`, `kr_locus_BH`, `kr_slice_far`, `kr_BH_eq` and `kr_r_to_zero`;
  - the sanity checks `kr_K_const` and `kr_K_sphere`.

  Also `dn_subset_BH_inter_slice` (`Densities.lean`).
- **Mark: BUILT ⇧ moved** (from BUILT IN PART). It rests on the standard reading: the curvature singularity is the
  locus where the Kretschmann invariant diverges.
- *Setting:* the curvature is computed on the coordinate chart `(U, V, θ, φ)`, with the sphere factor written in, and
  away from the sphere chart's poles. It is not tied to the manifold `W`. The locus-and-slice half is on the radial
  plane `W`. P1 l.329 states both limits.

**7d.** On every finite slice the collapsing matter lies outside `𝓗⁺`, is finite in extent, and is still approaching
its own horizon event.
- **Lean:** in `ShellMatter.lean`:
  - `sm_slice_meets_matter`, `sm_outside_H`, `sm_finite` and `sm_approaches`;
  - the definitions `sm_matter` and `sm_curve`;
  - the witness `sm_nonvacuous`.

  It rests on `sh_headline_D` and `sh_cauchy_D` (`SchwarzschildShellHorizon.lean`).
- **Mark: BUILT (radial plane) ⇧ moved** (from NOT BEGUN). It holds on the modelling reading:
  - The matter is the thin null shell `{v = v₀}`. This is a definition, since the kit has no stress-energy.
  - The model has one infalling element, not a 2-sphere's worth.

  P1 l.329 states both.

**7e.** The densities of the central singularity never form at any finite exterior time.
- **Mark: NOT BEGUN** (unchanged).
- **Reason:** it is interpretive.
  - A density needs a stress-energy, and the kit has none. Getting one needs the Einstein tensor of a matter model.
  - Without a stress-energy, 7e has no formal content beyond 7c and 7d.
  - P1 l.329 says: "needs a model of those densities and is not formalised".

## 8. `lem:alignment` (l.342)

The hypotheses are at l.343–349. P1 attests the lemma at l.386.

**8i.** The cones miss `𝓗⁺` and climb its generators, and `S_τ` accumulates (l.354–355).
- **Lean:**
  - `se_headline` and `se_stretch` (`SchwarzschildEF.lean`);
  - `sx_prop_causal_alignment` (`SchwarzschildConformal.lean`).
- **Mark: BUILT (radial plane)** (unchanged).

**8ii-a.** For both slicings, the tangent hyperplanes become tangent to the generator (l.358).
- **Lean:** `sa_stationary_aligns`, `sa_retarded_aligns` and the witness `sa_nonvacuous`, all in
  `SchwarzschildAlign.lean`.
- **Mark: BUILT (radial plane)** (unchanged).

**8ii-b.** Both slicings are Cauchy temporal functions of `D`, and meet `𝓗⁺` only in the limit (l.358, l.363; "Cauchy
surfaces of `D`", l.386).
- **Lean, stationary:** `se_headline` and `se_cauchy` (`SchwarzschildEF.lean`).
- **Lean, retarded:**
  - on a collapse: `sv_cauchy`, `sv_cauchy_D` and `sv_retarded_eq` (`SchwarzschildCollapse.lean`);
  - with its frontier: `sh_headline_D`, `sh_H_r` and `sh_H_flat` (`SchwarzschildShellHorizon.lean`);
  - on the eternal exterior, where it is not Cauchy: `sr_temporal`, `sr_future_diverges` and `sr_not_isCauchy`
    (`SchwarzschildRetarded.lean`);
  - `sv_eternal_cauchy` (`SchwarzschildCollapse.lean`).
- **Mark: BUILT (radial plane)** (unchanged).
- *New since r7685:* campaign 102 identifies `D`, `𝓗⁺ = {ũ = u_H} ⊆ M′` and the Cauchy property on one spacetime
  (`sh_headline_D`).

**8ii-c.** For the stationary slicing, `g^{ab}∇t∇t → −∞` and `N → 0` (l.360–361).
- **Lean:** `ss_static_gtt_tendsto` (`SchwarzschildSlicing.lean`).
- **Mark: BUILT** (unchanged).

**8ii-d.** For the retarded slicing, `g^{ab}∇Θ∇Θ → −2a²η` (l.363).
- **Lean:** `ss_ret_tendsto` (`SchwarzschildSlicing.lean`).
- **Mark: BUILT** (unchanged).

**8ii-e.** The retarded slicing accumulates on `𝓗⁺` in a collapse exterior (l.363).
- **Lean:** in `ShellAccumulation.lean`:
  - `sa2_shell`;
  - `sa2_flat`, `sa2_flat_cones`, `sa2_flat_cone_disjoint`, `sa2_flat_cauchy`, `sa2_flat_locallyOneChart` and
    `sa2_O_adapted`;
  - the witness `sa2_nonvacuous`, a point on the part of `𝓗⁺` inside the body.

  It rests on `sh_frontier` (`SchwarzschildShellHorizon.lean`).
- **Mark: BUILT (radial plane) ⇧ moved** (from NOT BEGUN).
- *How:* accumulation is causal, so it is proved on the `C^∞` flat restriction and carried unchanged to the `C⁰`
  shell. Tangency is not claimed on the shell, and the lemma does not ask for it there. P1 l.386 says so.

**`lem:alignment` is whole on the radial plane.**

---

## P1 against the Lean

Each `\texttt{}` name in P1 is checked against the probe P1 names for it. P1 names a probe once per group, in the
form "(…, in `X.lean`)". Where a name has no "in `X.lean`" of its own, the check uses the probe P1 names nearest before
it for that prefix; these are marked *(implied)*. "Found" means a declaration (`theorem`, `lemma`, `def` or `structure`)
of that exact name at the start of a line in that probe. The probe line is given.

| P1 line | Name | Probe checked | Found | Decl, line |
|---|---|---|---|---|
| 140 | `ac_metric_singularity_along` | `AlongConnection.lean` | yes | theorem, 123 |
| 140 | `ac_lapse_pos_forces_point` | `AlongConnection.lean` | yes | theorem, 212 |
| 140 | `ac_witness` | `AlongConnection.lean` | yes | theorem, 341 |
| 140 | `ac_witness_no_positive_lapse` | `AlongConnection.lean` | yes | theorem, 373 |
| 188 | `td_ne_of_transGen` | `ThreefoldDistinct.lean` | yes | theorem, 7158 |
| 188 | `td_cor_threefold_i` | `ThreefoldDistinct.lean` | yes | theorem, 7165 |
| 188 | `td_noClosed_of_temporal` | `ThreefoldDistinct.lean` | yes | theorem, 7208 |
| 188 | `td_noClosed_D` | `ThreefoldDistinct.lean` | yes | theorem, 7220 |
| 188 | `to_strict_null_order` | `ThreefoldOrder.lean` | yes | theorem, 6895 |
| 188 | `ng_energy_const` | `NullGeodesic.lean` | yes | theorem, 13454 |
| 188 | `ng_cor_threefold_iii` | `NullGeodesic.lean` | yes | theorem, 13463 |
| 188 | `ng_witness` | `NullGeodesic.lean` | yes | theorem, 13597 |
| 188 | `to_cor_1c` | `ThreefoldOrder.lean` *(implied)* | yes | theorem, 7082 |
| 188 | `tl_cor_threefold_iv_b` | `ThreefoldLocal.lean` | yes | theorem, 7661 |
| 188 | `tl_separation_interval` | `ThreefoldLocal.lean` | yes | theorem, 7682 |
| 188 | `tl_witness` | `ThreefoldLocal.lean` | yes | theorem, 7732 |
| 230 | `sk_cor_EF_events` | `SchwarzschildKruskal.lean` | yes | theorem, 7840 |
| 230 | `sq_cor_EF_coincident` | `SchwarzschildKilling.lean` | yes | theorem, 3851 |
| 280 | `kg_lemma_killing_generator` | `KillingGenerator.lean` | yes | theorem, 2827 |
| 280 | `kw_lemma_killing_whole` | `KillingWhole.lean` | yes | theorem, 3251 |
| 280 | `kw_witness` | `KillingWhole.lean` | yes | theorem, 3314 |
| 292 | `st_cor_stationary` | `StationaryHorizon.lean` | yes | theorem, 12987 |
| 292 | `st_witness` | `StationaryHorizon.lean` | yes | theorem, 13210 |
| 315 | `cd_prop_causal_alignment` | `ConeDisjoint.lean` | yes | theorem, 5174 |
| 315 | `mx_prop_causal_alignment` | `ConformalBoundary.lean` | yes | theorem, 5046 |
| 315 | `mx_H_eq_boundary` (cited twice) | `ConformalBoundary.lean` | yes | theorem, 5024 |
| 315 | `cd_cone_disjoint` | `ConeDisjoint.lean` *(implied)* | yes | theorem, 5159 |
| 315 | `hs_stretch_N` | `HorizonStretch.lean` | yes | theorem, 6194 |
| 315 | `gs_segment_stretch` | `GeneratorStretch.lean` | yes | theorem, 6388 |
| 315 | `gs_future_stretch` | `GeneratorStretch.lean` | yes | theorem, 6409 |
| 315 | `gs_witness` | `GeneratorStretch.lean` *(implied)* | yes | theorem, 6457 |
| 315 | `hs_witness` | `HorizonStretch.lean` *(implied)* | yes | theorem, 6280 |
| 317 | `mx_witness_headline` | `ConformalBoundary.lean` *(implied)* | yes | theorem, 6088 |
| 317 | `cd_witness` | `ConeDisjoint.lean` *(implied)* | yes | theorem, 6269 |
| 317 | `mc_witness_tangency_fails` | none named; checked in `ConformalBoundary.lean` | yes | theorem, 5811 |
| 317 | `cz_witness_headline` | `Compactification.lean` | yes | theorem, 6456 |
| 317 | `cz_Ω_sq` (P1: `cz\_$\Omega$\_sq`) | `Compactification.lean` | yes | theorem, 6321 |
| 317 | `cz_Ω_nonconst` | `Compactification.lean` | yes | theorem, 6341 |
| 317 | `cz_witness_headline_F` | `Compactification.lean` *(implied)* | yes | theorem, 6702 |
| 317 | `cz_exp_nonvacuous` | `Compactification.lean` *(implied)* | yes | theorem, 6747 |
| 317 | `ct_witness_tangency_F` | `CurvedTangency.lean` | yes | theorem, 6970 |
| 317 | `ct_expV_differs` | `CurvedTangency.lean` | yes | theorem, 7117 |
| 317 | `cy_witness_headline` | `CylinderWitness.lean` | yes | theorem, 6112 |
| 317 | `cy_witness_tangency` | `CylinderWitness.lean` | yes | theorem, 6205 |
| 317 | `fd_witness_headline` | `FourDWitness.lean` | yes | theorem, 5937 |
| 317 | `fd_witness_tangency` | `FourDWitness.lean` | yes | theorem, 6031 |
| 317 | `ww_witness_headline` | `WarpedWitness.lean` | yes | theorem, 6121 |
| 317 | `ww_witness_tangency` | `WarpedWitness.lean` | yes | theorem, 6232 |
| 317 | `ww_cotton_ne_zero` | `WarpedWitness.lean` *(implied)* | yes | theorem, 6442 |
| 317 | `se_headline` | `SchwarzschildEF.lean` | yes | theorem, 8791 |
| 317 | `sx_prop_causal_alignment` | `SchwarzschildConformal.lean` | yes | theorem, 9578 |
| 329 | `dn_cor_densities` | `Densities.lean` | yes | theorem, 5295 |
| 329 | `dn_witness` | `Densities.lean` | yes | theorem, 6432 |
| 329 | `kr_schwarzschild` | `Kretschmann.lean` | yes | theorem, 14473 |
| 329 | `kr_blowup` | `Kretschmann.lean` | yes | theorem, 14543 |
| 329 | `kr_cor_densities_c` | `Kretschmann.lean` | yes | theorem, 14566 |
| 329 | `sm_slice_meets_matter` | `ShellMatter.lean` | yes | theorem, 11471 |
| 329 | `sm_outside_H` | `ShellMatter.lean` | yes | theorem, 11487 |
| 329 | `sm_finite` | `ShellMatter.lean` | yes | theorem, 11503 |
| 329 | `sm_approaches` | `ShellMatter.lean` | yes | theorem, 11523 |
| 386 | `sa_stationary_aligns` | `SchwarzschildAlign.lean` | yes | theorem, 8136 |
| 386 | `sa_retarded_aligns` | `SchwarzschildAlign.lean` | yes | theorem, 8303 |
| 386 | `se_headline` | `SchwarzschildEF.lean` *(implied, from l.317)* | yes | theorem, 8791 |
| 386 | `sr_temporal` | `SchwarzschildRetarded.lean` | yes | theorem, 9101 |
| 386 | `sr_future_diverges` | `SchwarzschildRetarded.lean` | yes | theorem, 9273 |
| 386 | `sr_not_isCauchy` | `SchwarzschildRetarded.lean` | yes | theorem, 9246 |
| 386 | `sv_cauchy` | `SchwarzschildCollapse.lean` | yes | theorem, 10674 |
| 386 | `sv_retarded_eq` | `SchwarzschildCollapse.lean` | yes | theorem, 10535 |
| 386 | `sh_headline_D` | `SchwarzschildShellHorizon.lean` | yes | theorem, 11244 |
| 386 | `sh_H_r` | `SchwarzschildShellHorizon.lean` | yes | theorem, 11213 |
| 386 | `sh_H_flat` | `SchwarzschildShellHorizon.lean` | yes | theorem, 11221 |
| 386 | `sa2_shell` | `ShellAccumulation.lean` | yes | theorem, 11903 |
| 386 | `sv_eternal_cauchy` | `SchwarzschildCollapse.lean` *(implied)* | yes | theorem, 10178 |

**Result: P1 makes 74 name citations, covering 72 distinct names. `mx_H_eq_boundary` is cited twice on l.315, and
`se_headline` is cited on l.317 and l.386. The table has 73 rows, and every one is found. There is no mismatch.** All
29 probe files that P1 names or implies exist under `lean/probes/`.

**Two notes. Neither is a mismatch.**
- **`mc_witness_tangency_fails` (l.317)** is the one name for which P1 names no probe, explicitly or by a group.
  - It is declared in 21 probes, including `ConformalBoundary.lean` and `ConeDisjoint.lean`, the two named nearest
    before it.
  - Its original home is `ManifoldCones.lean`.
- **Eleven names rely on an implied probe.** Each is present in the probe it is read against.

Two spot checks agree with what P1 says of the hypotheses:
- `td_ne_of_transGen` needs only `NoClosedCausal`;
- `st_cor_stationary` sits under `[FiniteDimensional ℝ E]` and `[IsManifold 𝓘(ℝ, E) 2 N]`, as P1 l.292 says ("in finite
  dimension and with a `C²` atlas").

---

## Summary of the marks

| Statement | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| `thm:metric-singularity` (l.130) | 1a, 1b, **1c** | — | — |
| `cor:threefold` (l.166) | **i, ii, iii**, iv-a, **iv-b** | — | — |
| EF corollary (l.222) | 3a, 3b | — | 3c |
| `lem:killing` (l.271) | 4a, 4b, 4c, 4d | — | — |
| `cor:stationary` (l.285) | **5** | — | — |
| `prop:causal-alignment` (l.306) | 6a, 6b-i, 6c, 6d, 6e, 6f | 6b-ii | — |
| `cor:densities` (l.324) | 7a, 7b, **7c, 7d** | — | 7e |
| `lem:alignment` (l.342) | i, ii-a, ii-b, ii-c, ii-d, **ii-e** | — | — |

Bold marks a move since r7685.

***Counts (34 rows).***

| | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| r7667 | 10 | 15 | 9 |
| r7685 | 22 | 6 | 6 |
| **r7699 (this refresh)** | **31** | **1** | **2** |
| r7699, strict 2D reading | 23 | 9 | 2 |

***The strict 2D reading.*** It treats the radial plane as a reduced setting. Eight rows rest on it, and they drop to
BUILT IN PART: 3a, 3b, 7c, 7d, 8i, 8ii-a, 8ii-b and 8ii-e. They share one gap, the 4D warped product
`−F dU dV + r² dΩ²` on a manifold.
- For 7c, the Kretschmann computation is already 4D, but only on a coordinate chart. Its locus-and-slice half is on
  the radial plane.
- 7d also needs "each element" over the 2-sphere.

Some rows are general theorems on `N` whose only witness is 2D: 1c, 2i, 2ii, 2iii, 2iv-b and 5. They do not drop,
because a 2D witness is a genuine instance of P1's hypotheses.

***Moves since r7685 (nine, all upward).***

| Row | From → to | Campaign |
|---|---|---|
| 1c | IN PART → BUILT | 103 (`to_cor_1c`) |
| 2i | NOT BEGUN → BUILT | 104 (`td_cor_threefold_i`), on the ruled "no closed causal curves" |
| 2ii | NOT BEGUN → BUILT | 103 (`to_strict_null_order`) |
| 2iii | IN PART → BUILT | 107 (`ng_cor_threefold_iii`) |
| 2iv-b | IN PART → BUILT | 109 (`tl_cor_threefold_iv_b`), on "not fixed by the geometry" |
| 5 | IN PART → BUILT | 106 (`st_cor_stationary`), with rigidity cited |
| 7c | IN PART → BUILT | 110 (`kr_cor_densities_c`), on the Kretschmann reading |
| 7d | NOT BEGUN → BUILT (radial plane) | 102, 105 (`sm_`), on the modelling reading |
| 8ii-e | NOT BEGUN → BUILT (radial plane) | 102, 108 (`sa2_shell`) |

***Statements whole.*** These statements are whole:
- `thm:metric-singularity`, `cor:threefold`, `lem:killing` and `cor:stationary` (rigidity cited);
- `lem:alignment` (radial plane).

These are whole apart from one row each:
- the EF corollary, apart from 3c;
- `prop:causal-alignment`, apart from 6b-ii;
- `cor:densities`, apart from 7e.

## What remains, and why

Three rows remain. None of them is a row that the next campaign should build.

- **6b-ii (BUILT IN PART).** The Lean proves the future stretch from `HasFutureGenerators`. That the generators of an
  achronal boundary are future-inextendible is taken as a hypothesis, and it is discharged only on the 4D witness. 69's
  r7669 ruling leaves it there. The general proof needs a global temporal function, which is not P1's hypothesis, and
  costs 2500–6000 lines. P1 l.315 states the gap.
- **3c (NOT BEGUN).** "The vertical extent in the EF diagram encodes only causal order" is a reading of a picture. It
  has no formal content, and P1 l.230 calls it interpretive.
- **7e (NOT BEGUN).** "The densities of the central singularity never form at any finite exterior time" needs a
  stress-energy. The kit has none. Without one, the clause adds nothing to 7c and 7d. P1 l.329 says it "is not
  formalised".

Several BUILT marks rest on stated readings, all of which P1 now prints:
- 2i: "no closed causal curves";
- 2iv-b: "not fixed by the geometry";
- 5: rigidity cited;
- 7c: the Kretschmann divergence, on a chart;
- 7d: the matter is the shell;
- the radial-plane rows.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
