# `r7273+71.5` — RESULT: the negative against the gate's ruling does NOT fire. Layer 3 has THEORY `0` on `I20`'s path, and every ON item that is not already present is proved by a probe. The PORT's `32` does not survive contact: about `51`

*Read against `PREDICTION.md` in this directory, pushed at `r7273+71.1` before any search. The pre-registration
is not revised. The list of eighteen is the list, and the ON/OFF path marks are the ones pushed before the
search. Raw probe runs: `PROBE_RUN_Q1_Q3.txt` and `PROBE_RUN_Q4_Q5.txt`. Landed in pieces, as the standing
order asks: `+71.2` (Q1–Q3), `+71.3` (Q4, B8), `+71.4` (B7), and this result.*

## ⛔ The reachable negative — NOT FIRED

***ON-path THEORY = `0`.*** Of the ten ON-path items:
- **A1, A2 and A7 are present.**
- **B1, B4, B5, B6, B7 and B8 are DEF by measurement:** each was written against `mathlib` `4e6064a4` and
  builds with no `sorryAx`.
- **B2 is the PORT** already classed at `r7267+71.2`, and re-costed below.

*The order's condition — "if layer 3 comes back with a non-zero ON-path THEORY count, 'a port and a coercion
discipline' must be withdrawn" — is **not** met. **The gate's account stands on three layers rather than two.***

***What this does NOT cover.*** Layers 4–5 are not measured: the geodesic equation `D/dt γ̇ = 0`, the null
condition, and the charge. *B6 gives `D/dt`, and B7 and B8 give the two identities the charge's one-line proof
uses. **Assembling that proof is layer 5, not claimed here.***

## The count

| | central | band | **measured** |
|---|---|---|---|
| A present (of 7) | 7 | 6–7 | **7** ✔ |
| B present (of 11) | 0 | 0–1 | **0** ✔ |
| present / 18 | 39 % | 30–50 % | **7 / 18 = 39 %** ✔ |
| absent classed THEORY, all | 5 | 3–7 | **2** ✘ — *below the band, a miss in the cheap direction* |
| **absent classed THEORY, ON the path** | **1** | 0–3 | **0** ✔ — *below central* |
| Q1 builds | 0.9 | — | **yes** |
| Q2 builds in 200 lines | 0.6 | — | **yes** |
| Q3 builds | 0.85 | — | **yes** |
| Q4 builds in 150 lines | **0.4** | — | **yes, 14 lines** |
| Q5 builds in 200 lines | **0.3** | — | **yes, 166 lines** |
| the negative fires | 0.55 | — | **NOT FIRED** |

***The miss below the THEORY band is reported, not absorbed.*** *I expected the along-curve cluster to be
where `mathlib` stopped, because its connection files work on sections over `M` and not along a map. **It was
not:** the local-frame API (`LocalFrame.lean`) made `D/dt` a 14-line definition, and its two defining identities
proved in 166 lines.*

### A — 7 of 7 present (ON: A1, A2, A7)

| # | path | place in `mathlib` `4e6064a4` |
|---|---|---|
| A1 | ON | `CovariantDerivative` — `VectorBundle/CovariantDerivative/Basic.lean` l.366; `IsCovariantDerivativeOn` (`add`, `leibniz`) l.92; `congr_of_eventuallyEq` l.188 |
| A2 | ON | `CovariantDerivative.torsion`, `torsion_apply` — `CovariantDerivative/Torsion.lean` l.119, l.122 |
| A3 | OFF | `CovariantDerivative/Metric.lean` |
| A4 | OFF | `CovariantDerivative/LeviCivita.lean` |
| A5 | OFF | the Koszul formula, `LeviCivita.lean` l.212 |
| A6 | OFF | `VectorBundle/Tensoriality.lean` |
| A7 | ON | `mfderiv 𝓘(ℝ,ℝ) I γ t` (the probe's `vel` is one line over it) |

### B — 0 of 11 present

*Searched over `Geometry/` and `Topology/VectorBundle` for
`along (a|the) (curve|path|map)|covariant derivative along|alongCurve|VectorFieldAlong|pullbackSection|curvature|parallel transport|parallelTransport|christoffel`.
The one hit is `Metric.lean` l.34: "When Mathlib has a notion of parallel transport, prove the equivalence …" —
the absence, stated by the library itself. The smooth pullback bundle exists (`VectorBundle/Pullback.lean`
l.39); no connection on it does.*

| # | path | class | how |
|---|---|---|---|
| **B1** | **ON** | **DEF — measured (Q1)** | `IsCompatible g cov x` |
| **B2** | **ON** | **PORT** | Levi-Civita existence for a nondegenerate form. Classed at `r7267+71.2`; re-costed below; **not begun** |
| B3 | OFF | **PORT** | uniqueness. The Riemannian proof is the Koszul formula plus `injective_inner_*` (`LeviCivita.lean` l.96, l.109), which is the one positivity use, and has a nondegenerate replacement |
| **B4** | **ON** | **DEF — measured (Q2)** | `lieDerivForm_eq_cov`: `(𝓛_X g)(Y,Z) = g(∇_Y X, Z) + g(Y, ∇_Z X)` for ANY torsion-free `g`-compatible `cov` |
| **B5** | **ON** | **DEF — measured (Q3)** | `conformalKilling_cov`: conformal Killing in `∇` form, from Q2 and the `r7269` predicate |
| **B6** | **ON** | **DEF — measured (Q4)** | `covDerivAlong`: frame coefficients at `γ t`, differentiated along `γ`, plus `cᵢ ∇_γ̇ sᵢ`. *That it is the right definition is witnessed by B7 and B8, not asserted.* |
| **B7** | **ON** | **DEF — measured (Q5)** | `covDerivAlong_compat`: `d/dt g(V,W) = g(DV/dt, W) + g(V, DW/dt)` for fields ALONG `γ`, not only restrictions |
| **B8** | **ON** | **DEF — measured (Q5)** | `covDerivAlong_comp`: `D/dt (X ∘ γ) = ∇_γ̇ X` |
| B9 | OFF | **THEORY** | parallel transport needs existence for a linear ODE along `γ` through the trivialisations. `mathlib`'s `Metric.lean` names it as absent. |
| B10 | OFF | **THEORY** | curvature as a tensor needs `∇_Y Z` to be a smooth section. `Basic.lean` l.108's docstring defers that ("We will prove in a later file …"), so there is no proof to port. |
| B11 | OFF | **DEF** | Christoffel symbols = `localFrameCoeff` of `cov sⱼ x (sᵢ x)`, with no proof obligation |

**Absent: 11 — 7 DEF, 2 PORT, 2 THEORY, both THEORY OFF the path.**

## The probes — imported by nothing; the connection is a HYPOTHESIS throughout

*`lean/probes/ConnectionProbe.lean` (Q1–Q3, 5 s) and `lean/probes/AlongCurveProbe.lean` (Q4–Q5, 7 s).
**No existence theorem for any connection is used**: every statement takes a `CovariantDerivative` `cov`,
with `cov.torsion = 0` and `IsCompatible g cov` as hypotheses. So the Levi-Civita port is not begun, and
nothing touches `LeviCivita.lean`, `Metric.lean` or the layer-1 probe.*

```
'ShadowProbe.lieDerivForm_eq_cov' depends on axioms: [propext, Classical.choice, Quot.sound]
'ShadowProbe.conformalKilling_cov' depends on axioms: [propext, Classical.choice, Quot.sound]
'ShadowProbe.covDerivAlong_comp' depends on axioms: [propext, Classical.choice, Quot.sound]
'ShadowProbe.covDerivAlong_compat' depends on axioms: [propext, Classical.choice, Quot.sound]
```

***Last cycle's B6 is this cycle's B4, and it is now proved.*** *At `r7269+71.2`, "Killing ⇔ `∇X` skew" was
classed THEORY, OFF-path and unprobed, because the rule classes a theorem with no proof in `mathlib` as THEORY.
**Its content is Q2: about twenty lines from `torsion_apply` and `IsCompatible`.** That cycle's count is not
revised. A probed THEORY item turning out cheap is what the rule is built to show, and this is the second time
it has gone that way.*

***How it got built.*** *Eleven elaboration rounds: two for Q1–Q3 and nine for Q4–Q5. The causes:*
- *the `TangentSpace`/`E` coercion again;*
- *`set_option backward.isDefEq.respectTransparency false`, which `mathlib` itself uses for the same
  instance-transparency trouble, needed once for `HasMFDerivAt` on `ℝ`;*
- *two misnamed lemmas (`fderiv_apply_one_eq_deriv`, the root-namespace `contMDiffAt_localFrameCoeff`);*
- *one missing import (`Deriv.Add`, `Deriv.Mul`);*
- *summation order (`Finset.sum_comm`).*

***No round stopped on a missing lemma.*** *The coercion discipline the gate named is still the cost.*

***What the probes hold, in terms.***
- **Pointwise, at one `x` or `t`.** Hypotheses where used: `C¹` test fields, `γ` differentiable at `t`, and
  frame coefficients of `V`, `W` differentiable at `t`.
- **`hg` in B7** — `g(Y,Z)` differentiable for `C¹` `Y`, `Z` — is a hypothesis standing in for "`g` is a `C¹`
  field of forms". *Packaging it with the layer-1 structure is the port's business.*
- **`D/dt` is defined through the trivialisation at `γ t` only.** Frame-independence is not stated. *B8 is the
  form in which it matters: for fields that extend, `D/dt` is the frame-free `∇_γ̇ X`.*

## ② The PORT's `32` — does NOT survive contact: about `51`

*Re-costed by reading, not by porting. **The port is not begun.***

| piece | declarations | file |
|---|---|---|
| `LeviCivita.lean` — every declaration, all in a `RiemannianBundle` context | **24** | *(was counted 22: the first `grep` missed `public`/`private` declarations)* |
| `CovariantDerivative/Metric.lean` | **10** | |
| `IsContMDiffRiemannianBundle` and its `of_le`, its five order instances, the instance from the structure, and the six `MDifferentiable*`/`ContMDiff*` `inner_bundle` smoothness lemmas the two files call | **14** | `Geometry/Manifold/VectorBundle/Riemannian.lean` |
| a bundle class registering `g` without a norm, and one continuity lemma | **2** | `Topology/VectorBundle/Riemannian.lean` |
| a continuous `toDual` for a nondegenerate form in finite dimension (`BilinForm.toDual` is a `LinearEquiv` into `Module.Dual`) | **1** | new |
| **total** | **≈ 51** | **2 files beyond the two** |

| quantity | central | band | measured |
|---|---|---|---|
| re-costed PORT | 45 | 32–80 | **≈ 51** ✔ |
| files beyond `LeviCivita.lean`, `Metric.lean` | 1 | 0–3 | **2** ✔ |

- ***What moved it:*** `+2` from the regex, and `+17` from the bundle-level smoothness API that the first count
  could not see from inside the two files.
- *The new count is a reading, good to a few declarations either way. Nothing the layer-3 probes needed is in
  it.* **The probes needed none of the 51**, because a connection taken as a hypothesis does not have to exist.
- ⇒ ***The port is the price of EXISTENCE, not of the identities.*** *I20's path needs existence once, to say
  "the" geodesics of `g`.*
