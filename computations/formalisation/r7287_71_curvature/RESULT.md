# `r7287+71.4` — RESULT: G2 is STATABLE — K1, K2 and K3 all build, so the curvature tensor is reachable with the connection a hypothesis, and the statable count goes from `26` to `52` of `111`. The deferred smoothness is a lemma on a chart, not a gap; G2 is NOT behind T3b's `flow_hasFDerivAt`. And the instance builds: the scalar curvature of `a(η)²(−dη² + dx²)` is `2 (log a)″ / a²`

*Read against `PREDICTION.md` in this directory, pushed at `r7287+71.1` before any probe was written and before
any `mathlib` file was read for this order. The pre-registration is not revised. Landed in pieces:*
- *`+71.2` — K2, and K1's `X` and `Y` slots;*
- *`+71.3` — K1 complete;*
- *this result, with K3 and K4.*

*Raw run: `PROBE_RUN_K1_K4.txt`. It supersedes the partial run landed at `+71.3`, which is in the history at that commit.*

## ⛔ The negative — scored on the rule pushed at `+71.1`

| probe | item | builds | lines / budget | axioms |
|---|---|---|---|---|
| **K1** | K-A, K-B: `curv`, and `C^∞`-linearity in `X`, `Y`, `Z` on a manifold | **yes** | **171 / 250** | `[propext, Classical.choice, Quot.sound]` |
| **K2** | K-C, and the smoothness DISCHARGED on `E` | **yes** | **114 / 250** | the same |
| **K3** | K-D, K-E: Ricci, scalar curvature | **yes** | **37 / 120** | the same |
| K4 | K-G: the instance, scored beside the rule | **yes** | **195 / 250** | the same |

***The rule: K1, K2 and K3 all build → G2 is STATABLE over the tree.*** *So the curvature tensor is reachable with
the connection a hypothesis, and the statable count of `r7285` goes from `26` to `52` of `111`.*

***The other branch of the order's negative is answered too: G2 is not behind T3b's gap.***
- *The smoothness `mathlib` defers ("`C^(k+1)` connection is `C^k`") is the class
  `ContMDiffCovariantDerivative cov ∞`. K1 carries it as a hypothesis, in ONE lemma, `covApply_smooth`.*
- *K2 PROVES it on `E` for any `C^∞` Christoffel form (`contMDiffCov_model`).*
- *Nothing in the four probes touches the flow, and nothing stopped.*
- ⇒ ***"Two strata behind one named gap" does not hold. G2 is behind no gap at the level of what can be STATED,
  and T3b's `flow_hasFDerivAt` stands alone.***

| | predicted | **measured** |
|---|---|---|
| K1 | 0.6 | **yes** |
| K2 | 0.55 | **yes** |
| K3 | 0.75 | **yes** |
| K4 | **0.35** | **yes** |
| statable / named gap / mixed | 0.4 / 0.35 / 0.25 | **statable** |

*Again a probed THEORY item went cheaper than I predicted. K4 was the one I rated least likely.*

## What each probe holds, in terms

- **K1 (`CurvatureProbe.lean` l.1–171).**
  - *Definition:* `curv cov X Y Z = ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_[X,Y] Z`, for any `CovariantDerivative` on `TM`.
  - *Hypotheses:* the smoothness class above, and `C^∞` fields `X, Y, Z` and function `f`.
  - *`X` and `Y` slots* (`curv_smul_left`, `curv_smul_middle`): Leibniz, `mlieBracket_smul_left`, and
    antisymmetry.
  - *`Z` slot* (`curv_smul_right`): needed two facts about functions on a manifold that `mathlib`'s
    `Geometry/` does not state.
    - ***(b) `mdiff_df_apply`*** — `y ↦ df(y)(Y y)` is differentiable. It is `ContMDiffAt.mfderiv_apply` with
      its two tangent coordinate changes cancelled by `coordChange_comp`/`coordChange_self`, in 26 lines.
    - ***(c) `jacobi_fun`*** — `(X(Yf) − Y(Xf) − [X,Y]f)·Z = 0`. It is NOT built by second derivatives in
      charts: it is `mathlib`'s Jacobi identity for `f • Z`, minus `f` times Jacobi for `Z`, with every bracket
      expanded by `mlieBracket_smul_right`.
- **K2 (l.172–285).** On `E` as its own model, with `∇_w (const u) = G x w u`:
  - **`cov_model`:** `∇_w σ = Dσ·w + G(w, σ)`. It is the tensorial `difference` of `cov` and the flat
    connection `σ ↦ Dσ` (`flat_isCov`), read off at a point — `mathlib`'s `IsCovariantDerivativeOn.difference`
    does the work.
  - **`curv_model` (K-C):** `R(u,v)w = (DG·u)(v,w) − (DG·v)(u,w) + G(u, G(v,w)) − G(v, G(u,w))`.
  - **`contMDiffCov_model`:** `G` `C^∞` ⇒ `ContMDiffCovariantDerivative cov ∞`.
- **K3 (l.286–322).** Over one fibre, for a curvature-type map `R`:
  - `ricci R u v = tr (w ↦ R(w,u)v)`;
  - `scal R g = tr (g⁻¹ ∘ Ric)`, basis-free, through `BilinForm.toDual` of a nondegenerate `g`;
  - **`scal_eq_sum`:** in any basis, `scal = Σᵢ Ric(bᵢ*, bᵢ)` with `b*` the `g`-dual basis — so the definition
    is the one used on paper.
- **K4 (l.323–517), the instance, on the programme's own metric.**
  - *R3's `covConf a` is copied in, about 80 lines.*
  - **`curv_conf`:** its curvature on constant fields is `R(u,v)w = (log a)″ (u₁v₂ − u₂v₁)(w₂, w₁)`. The `φ′²`
    terms cancel.
  - **`Rconf_eq_curv`:** the trilinear map `Rconf a p` IS that curvature.
  - **`ricci_conf`:** `Ric = (log a)″ (−dη² + dx²)`.
  - **`scal_conf`: `R = 2 (log a)″ / a²`** (`= 2(a a″ − a′²)/a⁴` by the quotient rule — *that form is not
    stated in Lean*). *The closed form was computed in `sympy` from
    the same conventions before the Lean statement was written, and the Lean proof agrees with it.*
  - *Hypotheses:* `(a′/a)` differentiable at `η` (for the curvature), and `a(η) ≠ 0` (for `g` nondegenerate).

## What "statable" holds here, and what it does not — in terms

1. ***`C^∞`-linearity, not yet a pointwise tensor.*** K1 proves `R(fX,Y)Z = R(X,fY)Z = R(X,Y)fZ = f·R(X,Y)Z` for
   `C^∞` data. Packaging `R` at `x` as a map on `T_xM` needs a three-slot `mkHom`.
   - *`mathlib`'s `TensorialAt` cannot do it as written:* it asks for linearity under functions merely
     differentiable AT `x`, and curvature's `Z` slot is false there, because it needs second derivatives.
   - *A `C²` variant of `Tensoriality.lean`, with smooth bump functions in place of its indicator, is a PORT by
     reading. Not built.*
   - *On `E`, `curv_model` gives the pointwise value directly.*
2. ***The smoothness hypothesis on a manifold.*** Discharged on `E`. On a manifold it is `mathlib`'s deferred
   theorem.
   - *By reading it is a PORT of K2's argument chart by chart: the difference with the chart's flat connection
     is tensorial, by `mathlib`'s own `difference`. Not built.*
3. ***Named metrics.*** The G2 receipts state curvature of NAMED metrics, mostly in dimension 4 and up. Each
   needs a connection for that metric:
   - the Levi-Civita existence PORT (`≈ 51` declarations, not begun), or
   - an explicit Christoffel form per metric — the R3/K4 pattern, `195` lines here for one 2D metric including
     the copy.
   - ***Statable, not proved — as for G1.***
4. ***Four of the `26` also need the volume form*** — the Pontryagin density (receipts 69, 89, 96) and the SdS
   Petrov invariant (110), which uses the dual Weyl tensor.
   - *The volume density is `r7267` B9, THEORY and unprobed.*
   - *The rule pushed at `+71.1` scores the stratum, and the count is `52`. On the measured machinery alone,
     by reading, it is `48`, with those four one item further.* ***Said, not rounded.***
5. ***Contractions past scalar curvature*** — Kretschmann `R_abcd R^abcd`, `Weyl²`, Gauss–Bonnet — are
   definitions over K3's `toDual` and K1's tensor. DEF by reading, not built.

## The count, updated

| | `r7285` | **now** |
|---|---|---|
| statable now, of `111` | `26` (G0 `12` + G1 `14`) | ***`52`*** (+ G2 `26`) — *`48` on measured machinery alone, see 4* |
| still unstatable, of `135` geometric | `85` | ***`59`*** — G3 `17`, G4 `32`, G5 `10`, all unmeasured |

## The order's other constraint

***The port is not begun.*** *Every probe takes the connection as a hypothesis, or, in K4, uses the one explicit
connection already in the tree. Nothing touches `LeviCivita.lean` or `Metric.lean`.*
