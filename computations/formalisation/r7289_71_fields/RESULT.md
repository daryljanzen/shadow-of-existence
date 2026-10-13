# `r7289+71.4` — RESULT: G4 SPLITS — F1, F2, F3 all build, so the field equations, the wave operator and the covariant derivative of a tensor are statable with the connection and the background hypotheses; but `17` of `32` is under the pre-registered `22`. The remainder is NOT about the field equations: it is spectral theory and spin on a manifold (`12`, absent in both libraries) and G3 (`3`). The statable count still passes half: `69` of `111`

*Read against `PREDICTION.md` in this directory, pushed at `r7289+71.1` before any probe was written and before any
`mathlib` file was read for this order. The pre-registration is not revised. Landed in pieces:*
- *`+71.2` — F1;*
- *`+71.3` — F2;*
- *this result, with F3 and the search.*

*Runs: `PROBE_RUN_F1.txt`, `PROBE_RUN_F2.txt`, `PROBE_RUN_F1_F3.txt`. Search: `SEARCH_G4f_G4g.txt`. The probes are
the `r7289` sections of `lean/probes/CurvatureProbe.lean`.*

## ⛔ The negative — scored on the rule pushed at `+71.1`

| probe | what | builds | lines / budget | axioms |
|---|---|---|---|---|
| **F1** | Einstein tensor, `Ein + Λg = κT`, perfect fluid; **instance:** `Ein` of `covConf a` vanishes | **yes** | **48 / 150** | `[propext, Classical.choice, Quot.sound]` |
| **F2** | `Hess f`, `C^∞`-linear in both slots on a manifold; `□ = tr_g Hess`; **instance:** `□f = a⁻²(−f_ηη + f_xx)` | **yes** | **77 / 250** | the same |
| **F3** | `∇T(X;Y,Z)` for a `(0,2)` field, `C^∞`-linear in `X`, `Y`, `Z` | **yes** | **48 / 200** | the same |

| sub-class | count | state |
|---|---|---|
| G4a field equations | 9 | **statable** — F1 |
| G4b wave and mode operators | 4 | **statable** — F2; F3 for 65's operator on 2-tensors |
| G4c follow-on (67, 23) | 2 | **statable** by reading, over F1–F3 |
| G4d thermodynamic definitions | 2 | **statable** by reading: `κ` is G1, `T = κ/2π` a definition |
| **statable part** | **17** | **`< 22`** |
| G4e also needs G3 | 3 | unmeasured, with G3 |
| G4f spectral, heat-kernel, quantum | 9 | **THEORY** — absent in `mathlib` and `Physlib` (`SEARCH_G4f_G4g.txt`) |
| G4g spin | 3 | **THEORY** — absent in both |

***The rule: F1–F3 all build and the statable part is `17 < 22` → G4 SPLITS.***

***The order's question — is what blocks the rest about the FIELD EQUATIONS? No.***
- *The field equations themselves are statable: the Einstein tensor, `Λ`, a perfect-fluid source, the wave
  operator, and `∇` of a tensor.*
- *What is left is:*
  - *spectral theory of operators on a manifold — heat kernels, zeta functions, spectral decomposition;*
  - *spin geometry — spin structures, the spinor bundle, the Dirac operator;*
  - *and three receipts that wait on G3.*
- ***So the obstruction left in G4 is neither the field equations nor the geometry under them. It is analysis
  and representation theory ON a background*** — *quantum fields on curved space, not classical fields.*
  - *No layer has priced that kind of object. It is named here and not probed.*
  - *Its nearest relative in the record is T3b's `flow_hasFDerivAt`, also analysis.*

| | predicted | **measured** |
|---|---|---|
| F1 | 0.8 | **yes** |
| F2 | **0.55** | **yes** |
| F3 | 0.6 | **yes** |
| heat kernel / zeta on a manifold present | 0.1 | **absent** |
| spinor bundle / Dirac operator present | 0.1 | **absent** |
| G4 statable part | 17, band 12–22 | **17** ✔ |
| statable / splits / blocked | 0.15 / 0.6 / 0.25 | **splits** |

## What each probe holds, in terms

- **F1 (`CurvatureProbe.lean` l.519–566).** Over a fibre, from K3:
  - `trG` — the `g`-trace of a bilinear form, with `trG_eq_sum` (any basis, with its `g`-dual basis);
  - `einstein = ricci − ½ scal · g`;
  - `FieldEq R g Λ κ T :≡ Ein + Λ g = κ T`, with `κ` a parameter (`= 8πG`; `Real.pi` is not imported);
  - `perfectFluid g ρ p U = (ρ + p) U♭⊗U♭ + p g`.
  - ***Instance, `einstein_conf`:*** *the Einstein tensor of `covConf a` is `0`. In two dimensions `Ric = ½ R g`,
    and this is that fact on the programme's metric, from `ricci_conf` and `scal_conf`.*
- **F2 (l.567–643).**
  - On a manifold, for any `CovariantDerivative`: `hess cov f X Y = X(Yf) − (∇_X Y) f`.
  - `hess_smul_left` (`X` slot) is pointwise linearity.
  - `hess_smul_right` (`Y` slot) uses r7287's `mdiff_df_apply` and `mvfderiv_mul`.
  - `box` = `trG` of a Hessian.
  - ***Instance:*** `hessConf_eq` — the bilinear form `hessConf a f p` IS the Hessian of `f` for `covConf a` on
    constant fields (`f` `C²`). Then `box_conf`: `□ f = a⁻² (−f_ηη + f_xx)`. *The `φ′ f_η` terms of the two
    diagonal entries cancel — the conformal invariance of the 2D wave operator, on the programme's metric.*
- **F3 (l.644–691).**
  - `covT cov T X Y Z = X(T(Y,Z)) − T(∇_X Y, Z) − T(Y, ∇_X Z)`, `C^∞`-linear in `X`, `Y`, `Z`.
  - *The `Y` and `Z` slots carry `T(Y,Z)` differentiable at `x` as a hypothesis — the role `hg` played in
    layer 3.*
  - *Built the first time it ran.*

## Beside the score, said and not rounded

1. ***The pointwise packaging is still not built*** — the same caveat as `r7287` (1). F3's `∇T` and F2's `Hess` are
   `C^∞`-linear, but the divergence `∇^a T_ab` and `□` on a manifold take a trace of a pointwise tensor, which
   needs it. F2's `□` is built over a fibre and on `covConf`; on a general manifold it waits on the same `C²`
   `TensorialAt` PORT.
2. ***The contracted Bianchi identity `∇^a G_ab = 0` is not probed.*** *G4a's `div G` receipts (20, which is also
   G4e) state it.* It is a theorem about the Levi-Civita connection, so it sits behind the PORT. Statable, not
   proved.
3. ***Named metrics need a connection for that metric*** — the Levi-Civita PORT, or an explicit Christoffel form per
   metric. ***Statable, not proved***, as for G1 and G2.
4. ***G4c and G4d are classed by reading over F1–F3, not built.***

## The count, updated

| | `r7287` | **now** |
|---|---|---|
| statable now, of `111` | `52` | ***`69`*** (+ G4 `17`) — *`65` on measured machinery alone (the four volume-form receipts of G2)* |
| still unstatable, of `135` geometric | `59` | ***`42`*** — G3 `17`, G4 remainder `15` (G4e `3`, G4f `9`, G4g `3`), G5 `10` |

***`69` of `111` is past half, so the order's "majority within reach" holds — but by the count, not by the rule's
G4 verdict, which is SPLITS.***

## The order's other constraint

***The port is not begun.*** *Every probe takes the connection as a hypothesis, or uses `covConf`.*
