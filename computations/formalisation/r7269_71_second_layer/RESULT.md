# `r7269+71.2` — RESULT: THE NEGATIVE FIRES. Layer 2 on `I20`'s path has THEORY `0`, and its one theorem — `∂_η` is conformal Killing for `a(η)²(−dη² + dx²)` with `σ = a′/a` — is PROVED against `mathlib` as it stands

*Read against `PREDICTION.md` in this directory, pushed at `r7269+71.1` before any search. The pre-registration
is not revised. The list of eighteen is the list, and the ON/OFF path marks are the ones pushed before the
search. Raw probe run: `PROBE_RUN.txt` beside this file.*

## ⛔ The reachable negative — FIRED, scored on the path fixed before the search

***ON-path THEORY = `0`.*** Of the seven ON-path items:
- **A1, A2, A3 are present.**
- **B1, B4, B5 and B8 are DEF by measurement:** each was written against `mathlib` `4e6064a4` and builds with no
  `sorryAx`.

*Per the order: if layer 2 also comes back DEF-or-PORT on `I20`'s path, then `the geometric core is not
formalisable this year` is **a sentence about a horizon and not a wall**, and the gate withdraws it. **The
condition is met as written.***

***And what this does NOT cover, said here so it cannot be mistaken for more.*** *`I20.lean`'s layers 4 and 5
— null geodesics, and the conservation of `g(ξ, γ̇)` along them — are not measured. Layer 2 was the order. The
geodesic equation needs a connection, so on the pseudo-Riemannian side it runs through the Levi-Civita PORT
costed at `r7267+71.2`. **This seat makes no claim about layers 4 and 5.***

## The count

| | central | band | **measured** |
|---|---|---|---|
| A present (of 8) | 7 | 6–8 | **6** ✔, at the floor |
| B present (of 10) | 0 | 0–1 | **0** ✔ |
| present / 18 | 39 % | 30–50 % | **6 / 18 = 33 %** ✔ |
| absent classed THEORY, all | 4 | 2–6 | **5** ✔ |
| **absent classed THEORY, ON the path** | **1** | 0–2 | **0** ✔ — *below central* |
| P1 builds, no `sorryAx` | yes, 0.85 | — | **yes** ✔ |
| P2 builds, no `sorryAx` | yes, 0.85 | — | **yes** ✔ |
| P3 builds, no `sorryAx`, inside 150 lines | 0.45 | — | **yes, 83 lines** ✔ |
| the negative fires | 0.45 | — | **FIRED** |

### A — built FROM: 6 of 8 present

| # | path | declaration, place in `mathlib` `4e6064a4` | |
|---|---|---|---|
| A1 | ON | `VectorField.mlieBracket` — `Geometry/Manifold/VectorField/LieBracket.lean` l.70 | present |
| A2 | ON | `VectorField.lieBracket` — `Analysis/Calculus/VectorField.lean` l.59; `mlieBracketWithin_eq_lieBracketWithin` — `LieBracket.lean` l.89 | present |
| A3 | ON | `mfderiv`, with `mfderiv_eq_fderiv` on model spaces — `MFDeriv/NormedSpace.lean` l.625 | present |
| A4 | OFF | `exists_isMIntegralCurveAt_of_contMDiffAt` — `IntegralCurve/ExistUnique.lean` l.66 | present |
| A5 | OFF | a flow with a group law | **absent → THEORY** |
| A6 | OFF | pullback of a field of bilinear forms | **absent → DEF** |
| A7 | OFF | `CovariantDerivative/Torsion.lean` | present |
| A8 | OFF | `CovariantDerivative/Metric.lean` | present |

- *A5: searched `grep -rniE "def (flow\|mflow)\|localFlow\|IsMFlow"` over `Geometry/Manifold`: zero hits.
  Integral curves exist; a flow with a group law needs the curves to depend smoothly on their initial point,
  and `mathlib` has no proof of that to port. ⇒ THEORY.*
- *A6: `VectorField.mpullback` (`VectorField/Pullback.lean` l.106) is the vector-field version. The
  bilinear-form version is `LinearMap.compl₁₂` (`LinearAlgebra/BilinearMap.lean` l.330) applied pointwise
  through `mfderiv`, with no proof obligation. ⇒ DEF.*

### B — the layer: 0 of 10 present

*Searched `grep -rliE "lieDeriv|lie derivative|LieDerivative|killing.?vector|isKilling|conformal.?killing|KillingField"`
over `Geometry/` and `Analysis/Calculus/`. The one hit is `CovariantDerivative/Metric.lean` l.61, prose calling
`df(X x)` "the Lie derivative of the function". It is a comment about a function, not a tensor, and is not a
declaration. `LieDerivation` (`Algebra/Lie/Graded.lean`) is an algebraic derivation of a Lie algebra and is not
this.*

| # | path | class | why |
|---|---|---|---|
| **B1** | **ON** | **DEF — by measurement (P1)** | `lieDerivForm g X Y Z x = X(g(Y,Z)) − g([X,Y],Z) − g(Y,[X,Z])`, one `def` over A1 and A3 |
| B2 | OFF | **PORT** | tensoriality. `Geometry/Manifold/VectorBundle/Tensoriality.lean` (`TensorialAt`, `mkHom₂`) and the bracket's Leibniz rules `mlieBracket_smul_right` / `_left` (`LieBracket.lean` l.481, l.505) are the ingredients `LeviCivita.lean` already uses for terms of the same shape, `X⟪Y,Z⟫` and `⟪[X,Y],Z⟫` (`tensorialAt_leviCivitaAuxInner₁/₃`). |
| B3 | OFF | **THEORY** | the flow definition needs A5 |
| **B4** | **ON** | **DEF — by measurement (P2)** | `IsKilling` = `IsConformalKilling` with factor `0`; `isKilling_iff` proved |
| **B5** | **ON** | **DEF — by measurement (P2)** | `IsConformalKilling g X σ x`: for all `C¹` test fields, `𝓛_X g = 2σ g` |
| B6 | OFF | **THEORY** | *no proof to port. The argument is short algebra from A7 and A8 plus Levi-Civita, but the rule fixed at `+71.1` classes a theorem with no proof in `mathlib` as THEORY, and it is classed so.* |
| B7 | OFF | **THEORY** | needs `𝓛_{[X,Y]} = [𝓛_X, 𝓛_Y]` on tensors. `leibniz_identity_mlieBracket` (`LieBracket.lean` l.1153) is the vector-field case only. |
| **B8** | **ON** | **DEF — by measurement (P3)** | the instance, proved; see below |
| B9 | OFF | **THEORY** | needs A5 |
| B10 | OFF | **PORT** | `mpullback_mlieBracket` (`LieBracket.lean` l.907) is the vector-field naturality, plus A6 (DEF) |

**Absent: 12 — 5 DEF, 2 PORT, 5 THEORY, all 5 THEORY OFF the path.**

## The probes — `computations/formalisation/lean/probes/LieDerivProbe.lean`, imported by nothing

*Run: `lake env lean probes/LieDerivProbe.lean`, exit 0, 6 s.*

```
'ShadowProbe.isKilling_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'ShadowProbe.xi_isConformalKilling' depends on axioms: [propext, Classical.choice, Quot.sound]
```

***P3 states this:***

```lean
theorem xi_isConformalKilling (a : ℝ → ℝ) (p : ℝ × ℝ) (hd : DifferentiableAt ℝ a p.1)
    (ha : a p.1 ≠ 0) :
    IsConformalKilling (gConf a) xi (fun q => deriv a q.1 / a q.1) p
```

- `gConf a p = a(p.1)² · (−dη² + dx²)`, and `xi = ∂_η`.
- ***This is `I20`'s check ① with `I20.lean`'s "Not reached: layer 2" removed.*** The expression is now
  `𝓛_ξ g` by definition, through `mlieBracket` and `mfderiv` on the manifold `ℝ × ℝ`. It is no longer the one
  surviving component of a coordinate formula.
- *The two terms `lie_eta_component` had to drop as "properties of the chart" are computed here: the bracket
  of a constant field (`hbr`, through `mlieBracketWithin_eq_lieBracketWithin`), and the product rule on the
  form.*

***What P3 holds, and what it does not, said in terms.***
- **Pointwise.** At every point where `a` is differentiable and nonzero. Those are the hypotheses, stated
  where they are used.
- **`C¹` test fields.** `mathlib` has the model-space bridge for `ContMDiff` sections
  (`contMDiffAt_vectorSpace_iff_contDiffAt`, `VectorBundle/Tangent.lean` l.476) and not for `MDifferentiable`
  ones. So `IsConformalKilling` quantifies over `C¹` fields. *By B2's tensoriality, which is a PORT, the
  identity at a point depends only on the fields' values there, so nothing is lost. But B2 is not proved here,
  and I say so rather than lean on it.*
- **A field of bilinear forms, not the layer-1 structure.** `gConf a` is not packaged as the layer-1
  `ContMDiffPseudoRiemannianMetric`. Its nondegeneracy where `a ≠ 0` is layer 1's B8 (DEF), and the statement
  does not need it.
- **Two dimensions, as `I20` is.** Higher dimensions change `minkForm` and nothing in the argument.

***How it got built, because "83 lines" hides the route.*** *Three elaboration rounds for P1–P2 and seven for P3. Every fix was a coercion
between `TangentSpace 𝓘(ℝ, E) x` and `E`, or a rewrite blocked by it: `show ℝ from`, `obtain ⟨Y', rfl⟩`, `set`
before `rw`, plus one `2 − 1` in an exponent. **No round stopped on a missing lemma.** The mathematical
ingredients — the model-space bracket, `mfderiv_eq_fderiv`, `HasFDerivAt.mul`, the `C^n` bridge — were all
present on the first search.*

## The order's other constraint

***The Levi-Civita port is not begun.*** *Nothing here touches `LeviCivita.lean`, `Metric.lean` or the
layer-1 probe. P1–P3 use a bare field of bilinear forms.*

## Omission, recorded and not counted

*An item I would add now:* **the `MDifferentiable` form of the model-space bridge** (`MDiffAt (T% V) x ↔
DifferentiableAt V x` for vector fields on `E`). Its absence is why B5 quantifies over `C¹` fields. It is not on
the list, so it is not in the count.
