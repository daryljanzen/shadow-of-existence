# Scoping study: carrying `hl_causal_alignment_gh` onto the manifold layer of campaigns 66/68

*Read-only study. No Lean was written or built. Sources: `probes/HeadlineHypotheses.lean` (campaign 81, 2243 lines),
`probes/FlowManifold.lean` (66, 1543 lines), `probes/LieDerivManifold.lean` (68, 2081 lines),
`r7645_71_campaign81/RESULT_A.md`, `r7643_71_inventory/INVENTORY.md`, `corpus/BH_causality_v2.tex` (P1).*

## 0. Answer in one paragraph

The causal layer **does not exist at all** on the manifold layer. 66/68 provide a manifold `N`, raw vector fields,
`chartRep`, `hRep`, `mfderiv`, flows and flow boxes, the Lie derivative and `LocalKillingChart`. They provide no
Lorentzian/time-oriented structure on `N`, no causal vectors, no causal curves, no `≪`/`≤`, no `D`, `𝓗⁺`, slices or
temporal functions. The first piece that does not exist is **the manifold timelike step `TStep` on `N`** (a `C¹` curve
`ℝ → N` whose `mfderiv` velocity is future-timelike for a metric section `g` and orientation `T` on `N`), **together
with its chart transfer**: `TStep_N x y ↔ TStep_V (φ x) (φ y)` for the chart spacetime `g̃ = hRep g p`, `T̃ = chartRep T p`.
That transfer cannot be stated today. The V-side `Spacetime` needs `g` and `T` continuous, and `g` locally Lipschitz,
on **all of `V`**. `hRep`/`chartRep` are only meaningful (and continuous) on the chart target. So the first concrete
blocker sits on the V side: weaken `cont_g`, `cont_T` and `hL` to `M`.

**Recommendation: route (c), "global-chart transport".** It is one campaign of about 1,000–1,500 new lines (plus about
100 changed). It states the headline on a Mathlib manifold `N` whose region `M` lies in one atlas chart, and proves it
by transporting to the existing V theorem. It does not re-prove the causal chain. That covers every spacetime whose `M`
fits in one chart, which (as a topological fact, not formalised) includes P1's Kruskal and Oppenheimer–Snyder
exemplars. The general multi-chart case (route b) is 2,000–3,500 lines over 3–5 campaigns. Its hard core is one
missing theorem: **inextendible extension of causal curves on a manifold** (V's polygonal past extension uses straight
segments and the norm).

## 1. Inventory of the causal layer under `hl_causal_alignment_gh`

The headline (`HeadlineHypotheses.lean:1576`) is `hl_causal_alignment_gh₀` with `hcl := hl_hcl`, `hint := hl_hint`.
`gh₀` = `hl_causal_alignment` ∘ `hl_futCauchy_of_cauchy_D` (②). `hl_causal_alignment` = `hl_sublevelProper` +
`hl_slice_kuratowski`.

Legend: **L** = uses the linear/normed structure of `V` essentially (straight lines, `+`, `•`, norms, `deriv` of
curves into `V`). **C** = uses only `C¹`-calculus that has a direct chart-invariant analogue (`deriv` → `mfderiv`).
**T** = topology / order / relations only.

| Ingredient (line) | Kind | What it uses | Manifold analogue |
|---|---|---|---|
| `Spacetime` (70): `M ⊆ V` open, `g : V → V →L V →L ℝ`, `T : V → V`, `cont_g`, `cont_T` **global on V**, `T_timelike`, `pos_on_perp` on `M` | L/C | `g`, `T` as functions on `V`. **Global continuity on `V` is an artefact.** Only points of `M` are ever used. | Sections over `N` (`Π x, T_xN →L T_xN →L ℝ`, `Π x, T_xN`), as in 68's `hRep`/`chartRep` inputs. **Absent.** |
| `FutTimelike`/`FutCausal` (85) | C (pointwise algebra) | `g x v v`, `g x v (T x)` | Same formula on `T_xN`. Chart-invariant: `ld_h_eq_hRep`, `ld_chartRep_apply_chart`. |
| `TStep`/`CStep` (90) | C | `γ : ℝ → V`, `ContDiff ℝ 1` **on all ℝ**, `deriv γ t` on `[0,1]`, `γ t ∈ M` only on `[0,1]` | `γ : ℝ → N`, `ContMDiff 𝓘(ℝ) 𝓘(ℝ,E) 1`, `mfderiv γ t 1`. Transfer needs a squash reparametrisation (§3). |
| `Chr`/`Cau` (100) | T | `TransGen`/`ReflTransGen` of steps | Verbatim. |
| `Ipast`/`Jpast`/`IpastSet`/`JpastSet`, `D`, `H := frontier`, `slice` (105–506) | T | sets, `frontier` **in V** | Verbatim, `frontier` in `N`. Caveat in §3(c). |
| `KLi`/`KLs` (514) | T | `𝓝` filters only (already `omit [NormedSpace]`) | Generalise to `[TopologicalSpace X]`; free. |
| `isOpen_timelikePairs`, `tube` (117–130) | T (+ `cont_g`, `cont_T`) | continuity of `(x,v) ↦ g x v v` on `V × V` | Chart-local only (open set in `TN`). |
| `tstep_start_eventually` / `tstep_end_eventually` (137, 713) ⇒ `hl_isOpen_Ipast`/`Ifut` | **L** | perturbs the whole curve by `γ t + (1−t)•(p'−p)`: a global affine shift in `V` | Chart-local: split the step (free, since `Chr` is `TransGen`), shift only the first/last short piece inside one chart. |
| `quad_le`, `local_pushup` (195, 209) | **L** | `LipschitzOnWith K g N`, `‖a‖`, `dist`, the perturbed curve `α(s+r(t−s)) + l r(t−s)•T(α s)` | Chart-local at `α s` (one chart, a short arc). Needs `g̃` locally Lipschitz in that chart. |
| `pushup_cstep`, `hl_pushup` (326, 368) | T | `sInf` argument on `[0,1]`, continuity of `α`, openness of `I⁻(z)` | Verbatim given chart-local `local_pushup` and openness. |
| `rev`, `rev_*_iff`, `hl_pushup'` (377–448) | C | `T ↦ −T`, `t ↦ 1−t` | Verbatim with `mfderiv`. |
| `IsTemporal` (461), `temporal_curve`, `hl_temporal_chr` | C | `ContDiffOn ℝ 1 τ M`, `fderiv ℝ τ x v`, chain rule | `ContMDiffOn`, `mfderiv τ x v`; chain rule via `mfderiv_comp`. |
| `restrict`, `Dsp` (604, 632) | T | change `M` only | Verbatim. |
| `InextCausalCurve`, `FutInextCurve`, `PastInextCurve`, `IsCauchyTemporal`, `Fut/PastCauchyTemporal` | C/T | `DifferentiableAt ℝ γ t`, `deriv`, `Tendsto γ atTop (𝓝 p)` in `V` | `MDifferentiableAt`, `mfderiv`, `Tendsto` in `N`. |
| `hl_D_of_chr`, `tstep_tail`, `tstep_in_D`, `tstep_Dsp`, `hl_temporalD_chr` (640–695) | C | sub-curves of a step (affine reparametrisation) | Verbatim with `mfderiv` (affine reparametrisation is chart-free). |
| `seg q r := q + r•T q`, `seg_timelike`, `seg_tstep`, `hl_seg_timelike2`, `hl_future_step`/`hl_past_step` (746–1515) | **L** | straight segment along `T(q)` | Chart-local at `q` (segment in the chart at `q`). |
| `hl_curve` (813): `γ t = q − ε e^{−t} T(q)` | **L** | straight line, `Metric`, limit `→ q` | Chart-local at `q`: one chart contains the whole curve (`r ∈ [−ε,0]`). Cheap. |
| `hl_blowup_cauchy`, `hl_sublevelProper`, `hl_mem_KLi_slice`, `hl_slice_lower/upper_limit`, `hl_slice_kuratowski`, `hl_causal_alignment` (878–970) | T | filters, closure, openness of `I⁺`, monotonicity of `Θ` | Verbatim. |
| `Safe`, `safe_uniform`, `pvert`, `ppiece`, `ppoly`, **`hl_past_extension`** (979–1230) | **L, essentially** | dyadic safe length of straight segments; **inextendibility proved metrically**: `‖X(k+1) − X k‖ = ℓ_k‖T(X k)‖ → 0` vs `‖T(X k)‖ → ‖T q‖ > 0` | **No chart-local version.** Vertices wander through many charts. `chartAt` gives no coherent choice and no uniform bound. This is the hard piece (§4). |
| `hl_futCauchy_of_cauchy` (②), `hl_future_extension`, `hl_pastCauchy_of_cauchy`, `hl_cauchy_iff` | T, given extension | gluing a curve to the extension, `strictMonoOn_of_brk` | Verbatim given a manifold extension theorem. |
| `hl_JpastSet_subset_M`, `hl_hint`, `hl_hcl` (1526–1566) | T | short steps + dual push-up | Verbatim given chart-local short steps and push-up. |
| `hL : LocallyLipschitz S.g` (on **all of V**) | **L** | Lipschitz in the norm of `V →L V →L ℝ` | Only meaningful in a chart. Invariant under `C^{1,1}`/`C²` chart changes, not under `C¹` ones. On `N`: state as "`hRep g p` is `C¹` (or locally Lipschitz) on the chart target". P1's `g` is smooth. |
| `Model` (1592–) | L | `ℝ × ℝ` constant metric | Witness: the model space as its own manifold (`chartAt = refl`), or a transported instance. |

Summary: everything **L** except the past/future extension is *local*: one short arc in one chart. The relations are
global, but they are `TransGen` closures, so concatenation is free.

## 2. What the manifold layer of 66/68 provides

Setting: `{E} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]`,
`{N} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]` (some sections use `2`).

- `chartRep X p y = mfderiv (extChartAt p) (φ⁻¹ y) (X (φ⁻¹ y))`. Lemmas: `ld_chartRep_inv`,
  `ld_chartRep_apply_chart`, `ld_chartRep_eq_triv`, `ld_chartRep_contDiffAt_of_section`,
  `ld_chartRep_contDiffOn_of_section` (C²), `ld_chartRep_ne_zero`.
- `hRep h p y = h(φ⁻¹y)(Dφ⁻¹ ·, Dφ⁻¹ ·)`, `ld_hRep_apply`, `ld_h_eq_hRep` (the tensor-transport identity),
  `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`, `ld_mdifferentiableAt_symm`.
- Flows: `FlowData`, `fm_local_flow`, `fm_flowData_exists_of_contDiffOn`, uniform time on a ball, `C¹` flow, flow box
  `ld_manifold_flowBox(_section)`.
- `lieDerivForm`, `IsKilling`, `constExt`, `lieDeriv`, its chart formula and chart independence (C²),
  `LocalKillingChart`, `ld_manifold_killingChart_lieDeriv`, `ld_metric_N`.

**Not provided:** a Lorentzian metric on `N` as a structure (68's `g` is a raw `Π x, T_x →L T_x →L ℝ` with no signature
or nondegeneracy; campaign 83 notes that `LocalKillingChart` assumes no nondegeneracy either), a time orientation, a
time-oriented spacetime structure, causal/timelike vectors, causal curves, `≪`, `≤`, `I^±`, `J^±`, `D`, `𝓗⁺`, temporal
or Cauchy functions, inextendibility. No probe combines `ChartedSpace` with `TStep`/`Chr`/`Timelike`: a grep over all
14 `ChartedSpace` probes finds none. **The causal layer on `N` is zero lines.**

## 3. What is missing to state the headline on `N`, and the routes

### Statement-level pieces (needed by every route)

1. `LorentzSpacetime N` (name provisional): `M : Set N` open, `g : Π x, T_xN →L T_xN →L ℝ`, `T : Π x, T_xN`,
   symmetry, `T_timelike`, `pos_on_perp` on `M`, and regularity in charts: `∀ p, ContinuousOn (hRep g p) (φ_p '' (M ∩ src))`
   and the same for `chartRep T p`. Bundle-section continuity would need Mathlib's hom-bundle API. Chart form is
   honest and matches 66/68.
2. `FutTimelike`, `FutCausal`, `TStep`, `CStep` with `mfderiv 𝓘(ℝ,ℝ) 𝓘(ℝ,E) γ t 1`. Then `Chr`, `Cau`, `Ipast`, …, `D`,
   `H := frontier` in `N`, `slice`, `KLi`/`KLs` (generalised), `IsTemporal` (`ContMDiffOn` + `mfderiv`),
   `InextCausalCurve`, `IsCauchyTemporal`, `restrict`, `Dsp`, `SublevelProper`. About 150–250 lines, all definitions.
3. A regularity hypothesis replacing `hL`: "`hRep g p` is `C¹` (or locally Lipschitz) on the chart target" for the
   relevant chart(s). This holds for P1's smooth `g` in a smooth atlas.

### Chart invariance of the V statement (point 3 of the brief)

- `frontier`, `closure`, `KLi`/`KLs`, `SublevelProper`, `Chr`/`Cau` as relations, `D`: topological or relational. They
  are invariant under homeomorphisms, **with one caveat**: in V, `H = frontier_V J⁻(J)` is computed in the ambient `V`.
  If `M` sits in a chart image `φ(U) ⊊ V`, `frontier_V` can gain points of `∂φ(U)`: limits of sequences escaping `N`.
  An example is the past singularity of maximal Kruskal in a badly chosen chart. Then `hHM : H ⊆ M` fails in V even
  though `𝓗⁺_N ⊆ M_N`. So the V statement is chart-invariant only for charts with `closure_V φ(J⁻J) ⊆ φ(U)`. The clean
  fix is a localized V headline (§3(c) below).
- `FutTimelike`/`FutCausal`: pointwise tensor algebra. Invariant when `g`, `T` transform as tensors (`hRep`, `chartRep`).
- `TStep`/`CStep`: `C¹` curves with `deriv`. Invariant under `C¹` diffeomorphisms by the chain rule. The "`ContDiff` on
  all ℝ" clause is not invariant as stated, because a curve may leave the chart outside `[0,1]`. A squash
  reparametrisation fixes this: `σ(t) = ½ + c·tanh(k(t−½))` with `σ(0)=0`, `σ(1)=1`, `σ' > 0`,
  `σ(ℝ) ⊂ (−δ, 1+δ)`.
- `IsTemporal`, `InextCausalCurve`, `IsCauchyTemporal`: `C¹`/piecewise-`C¹` notions and `Tendsto`. Invariant under `C¹`
  diffeomorphisms (homeomorphism on the source for the limits; inextendibility asks only about limits in `M` ⊆ source).
- `LocallyLipschitz g`: the coordinate expression involves `Dφ`. It is invariant under `C^{1,1}`/`C²` chart changes
  only. Global-on-`V` Lipschitz/continuity is not invariant at all, because `hRep` blows up or is junk off the target.
  **So the V `Spacetime` must be refactored to require `ContinuousOn` of `g` and `T` on `M`, and local Lipschitz at
  points of `M`.** The proofs only ever use `g`, `T` at points of `M` (checked: `cont_gvw` at `α s ∈ M`, `cont_T.tendsto q`
  at `q ∈ M`, `safe_uniform` near `x ∈ M`, `hL (α s)` with `α s ∈ M`). The refactor is mechanical.

### Route (a): full lift

Define the layer on `N` (items 1–3) and re-prove the whole chain with `mfderiv`. The **L** ingredients (tube lemma,
push-up estimates, segments, `hl_curve`, polygon) have no coordinate-free proof without a connection or exponential
map, which Mathlib lacks. So (a) collapses into (b) with extra cost.
**Estimate: 3,000–5,000+ new lines, 4–6 campaigns. Not recommended.**

### Route (b): localization (general multi-chart `N`)

Use the refactored V `Spacetime` as a *chart-local spacetime*: for each `p`, the `Spacetime E` with
`M̃ = φ_p(M ∩ src_p)`, `g̃ = hRep g p`, `T̃ = chartRep T p`. Then:
- **chart-transfer lemma**: a `TStep` whose curve lies in `src_p` ↔ a `TStep` of the chart-local spacetime (squash plus
  chain rule); 250–400 lines;
- sub-curve/splitting lemmas (`TStep` ⇒ `TransGen` of short steps, each in one chart, via the Lebesgue number of the
  chart cover of `γ[0,1]`); 100–200;
- openness of `I^±` (split, then the local tube lemma in the first/last chart); 100–200;
- push-up on `N`: `pushup_cstep`'s `sInf` argument verbatim, with `local_pushup` in the chart at `α s`; the endpoint
  perturbation lives in that chart; 200–300;
- short steps, `hl_curve`, `hint`, `hcl`: chart-local; 150–250;
- temporal monotonicity, `strictMono` along inextendible curves (`mfderiv` chain rule); 100–150;
- topological layer (`D`, `H`, slices, `KLi`, properness, Kuratowski): copy with `V ↦ N`; 250–400 (mostly copied);
- **past/future inextendible extension on `N`** (needed by ②, two-sided ⇒ future form): **does not exist; hard**.
  V's proof is metric. A manifold proof: build the polygon from integral-curve pieces of `−T` (needs `T` `C¹`, true for
  P1), with intrinsic flow-time safe lengths. Get a uniform safe length near `q` from 66's `FlowData` in the chart at
  `q`. Rule out convergence to `q` with the temporal `Θ` that ② already has: each step lowers `Θ` by
  `≥ min(ℓ, τ′)·m > 0`, which contradicts continuity of `Θ` at `q`. This avoids uniqueness of integral curves and any
  complete Riemannian metric. 500–900 lines, the main risk;
- headline and witness: 150–250.

**Estimate: 2,000–3,500 new lines (about 400 of them copied), 3–5 campaigns.** Risks: the extension theorem; chart-cover
/ Lebesgue-number plumbing; `mfderiv` of curves (`𝓘(ℝ,ℝ)`) vs `deriv`; heartbeats on `TangentSpace` defeq.

### Route (c): reduction / global-chart transport (recommended)

Hypothesis: `M ⊆ (chartAt E p₀).source` for one `p₀`. That is exactly "`M` fits in one atlas chart"; P1's examples
satisfy it after a suitable atlas choice. Using `chartAt` rather than an arbitrary maximal-atlas chart keeps every 68
lemma usable verbatim. Build `S_V : Spacetime E` with `M_V = φ(M)`, `g_V = hRep g p₀`, `T_V = chartRep T p₀`. Then
transport, without re-proving any causal argument:
1. **V refactor** (prerequisite): `cont_g`, `cont_T` → `ContinuousOn … M`; `hL` → `∀ x ∈ M, ∃ K, ∃ U ∈ 𝓝 x,
   LipschitzOnWith K g U`. Touches `cont_gvw`, `isOpen_timelikePairs`, `tube`, `local_pushup`, `rev`, `restrict`,
   `safe_uniform`, `hl_past_extension` (one `cont_T.tendsto` at `q ∈ M`), `Model`. About 60–150 changed lines in a copy
   of `HeadlineHypotheses.lean`.
2. **Localized V headline**: replace `hHM : H ⊆ M` by `hHM' : H ∩ W ⊆ M` for an open `W ⊇ M` (the chart target). The
   conclusions become `KLi ∩ W = H ∩ W`, `KLs ∩ W = H ∩ W`, and properness relative to `W`. The lower limit only uses
   points of `M`; the upper limit and `hint` do not use `hHM`; properness uses blow-up at `p ∈ H`, which holds for
   `p ∈ W`. This removes the ambient-frontier caveat with no chart hypothesis. 100–200 lines.
3. Manifold definitions (items 1–3): 150–250 lines.
4. Transport lemmas: `FutTimelike`/`FutCausal` ↔ (about 30, from `ld_h_eq_hRep`, `ld_chartRep_apply_chart`);
   `TStep`/`CStep` ↔ (squash plus `mfderiv` chain rule, both directions; 200–350); `Chr`/`Cau`/`Ipast`/`D`/`JpastSet` images
   (`TransGen` map; about 80); `frontier`/`closure`/`KLi` in `N` vs `V ∩ target` (`e` is a homeomorphism of the source
   onto the open target; about 80); `IsTemporal`, `InextCausalCurve`, `IsCauchyTemporal` of `Dsp` ↔ (150–250);
   regularity (`ContDiffOn (hRep g p₀)` ⇒ local Lipschitz via `ContDiffAt.exists_lipschitzOnWith`; about 30).
5. The manifold headline `hl_causal_alignment_gh_N` and a witness: the Rindler model on `N = ℝ×ℝ` as its own manifold,
   or better a non-identity chart. 120–200 lines.

**Estimate: 1,000–1,500 new lines, plus about 100 changed. One campaign (stop at about 2,200), possibly split as
(c1 = refactor + localized V headline) and (c2 = manifold layer + transport).** Risks, in order:
- the squash reparametrisation and `ContMDiff` ↔ `ContDiff` of `φ ∘ γ` on all of ℝ;
- `mfderiv 𝓘(ℝ,ℝ) … γ t 1` vs `deriv` bookkeeping, and `TangentSpace` defeq/heartbeats (66/68 already solved the
  pattern);
- the localized V headline may need more than "replace `hHM`" if some step silently uses `H ⊆ M` off `W` (none seen);
- the witness could be trivial if `N` = model space. A non-identity chart makes the transport actually exercised.

**What (c) honestly gives.** "The headline holds on every Mathlib manifold spacetime whose region `M` lies in a single
chart, with `g` `C¹` in that chart." It does **not** formalise that P1's Kruskal/OS spacetimes admit such a chart. That
is a topological fact the inventory already records: `{UV<1} × S² ≅ ℝ² × S² ≅ ℝ × (ℝ³∖0) ⊂ ℝ⁴`, and OS is likewise an
open subset of `ℝ⁴`. The fact is standard but stays unformalised. The general asymptotically flat case (P1's
proposition is stated "for any asymptotically flat spacetime whose exterior domain is globally hyperbolic") still needs
route (b). P1's own exemplars do not.

## 4. The first missing piece, precisely

1. **On the V side (blocks any transport):** `Spacetime.cont_g : Continuous g`, `cont_T : Continuous T` and
   `hL : LocallyLipschitz S.g` are on all of `V`. A chart representative `hRep g p` cannot satisfy them, so no manifold
   spacetime can be instantiated as a V `Spacetime` without a cutoff (which would shrink `M` and need a
   restriction-invariance lemma). The fix is to weaken them to `M`.
2. **On the manifold side (the first thing that does not exist):** the manifold timelike step
   `TStep_N x y := ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ,ℝ) 𝓘(ℝ,E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧ ∀ t ∈ [0,1], γ t ∈ M ∧
   FutTimelike (γ t) (mfderiv γ t 1)`, over a `LorentzSpacetime N` (`g`, `T` sections), and its chart transfer
   `TStep_N x y ↔ (chartSpacetime p).TStep (φ_p x) (φ_p y)` for curves in `src_p`.
3. **The deepest missing piece (route b only):** past/future inextendible extension of a timelike curve on a manifold
   (V: `hl_past_extension`, metric proof). It is needed for two-sided ⇒ future Cauchy (②). Proposed proof: integral
   curves of `−T` via 66's `FlowData`, inextendibility via the temporal `Θ`.

## 5. Proposed campaign (route c)

*"Campaign N+1: the headline on a manifold with a global chart."*
- New probe `probes/ChartHeadline.lean`: copies `HeadlineHypotheses.lean` (with the `cont_g`/`cont_T`/`hL` → on-`M`
  refactor and the localized `hHM'` headline) and the needed 68 lemmas (`chartRep`, `hRep`, `ld_h_eq_hRep`,
  `ld_chartRep_apply_chart`, `ld_mfderiv_*_chart`, `ld_mdifferentiableAt_symm`), since probes cannot import probes.
  Note: this copy is large (about 2,000 copied lines plus 1,000–1,500 new).
- Registered targets: ① refactor re-checks (`hl_model_headline` unchanged); ② `hl_causal_alignment_gh_loc` (localized
  `hHM'`); ③ `LorentzSpacetime N` plus definitions; ④ `tstep_chart_iff`, `cstep_chart_iff`, `chr/cau_chart_iff`,
  `isCauchyTemporal_chart_iff`, `frontier_chart`, `KLi_chart`; ⑤ `hl_causal_alignment_gh_N` with hypotheses `hglob`,
  `hgC1`, `hOD`, `hmono`, `hJM`, `hHM` (in `N`), `hΘ`, `hadapt`; ⑥ a witness with a non-identity chart.
- Predicted: 1,000–1,500 new lines, band 700–2,200, stop at 2,600 new. p(① 0.9, ② 0.8, ④ 0.65, ⑤ 0.6, ⑥ 0.7).
- Failable: REPORTED with the step that stopped. The likeliest stop is ④'s `TStep` transfer (squash/`ContMDiff`).

Then route (b)'s extension theorem is the named remaining gap, as its own campaign (about 500–900 lines). It is
followed by the localization campaigns (about 1,500–2,500), and only if the general asymptotically flat case is wanted.
