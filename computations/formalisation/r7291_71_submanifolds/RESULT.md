# `r7291+71.4` — RESULT: G3 is STATABLE — S1 and S2 both build, so the induced metric of a map and the second fundamental form are statable with the connection and the metric hypotheses, and the statable count goes from `69` to `88` of `111`. No third kind of obstruction. ⌗ But the order's "the residual is the two absences" does NOT hold as stated: the residual is `23`, and `10` of it is G5, which no layer has measured

*Read against `PREDICTION.md` in this directory, pushed at `r7291+71.1` before any probe was written and before any
`mathlib` file was read for this order. The pre-registration is not revised. Landed in pieces:*
- *`+71.2` — S2;*
- *`+71.3` — S1;*
- *this result, with S3 and the search.*

*Runs: `PROBE_RUN_S2.txt`, `PROBE_RUN_S1.txt`, and `PROBE_RUN_S1_S3.txt`, which supersedes them both. Search:
`SEARCH_G3.txt`. The probes are the `r7291` sections of `lean/probes/CurvatureProbe.lean`.*

## ⛔ The negative — scored on the rule pushed at `+71.1`

| probe | what | builds | lines / budget | axioms |
|---|---|---|---|---|
| **S1** | `pullG φ g`, the induced metric along a map; symmetric; `(ψ ∘ φ)*g = φ*(ψ*g)`; **instance:** the flat slicing of 2D de Sitter | **yes** | **93 / 250** | `[propext, Classical.choice, Quot.sound]` |
| **S2** | `sff cov g N X Y = g(∇_X N, Y)`, `C^∞`-linear in `X` and `Y`; symmetric for a torsion-free, compatible `cov` with `N` normal and `[X, Y]` tangent | **yes** | **44 / 200** | the same |
| S3 | the instance, scored beside the rule: the slices `η = const` of `covConf a` | **yes** | **44 / 150** | the same |

***The rule: S1 and S2 both build → G3 STATABLE.*** *The count becomes `69 + 17 + 2 = 88` of `111`. G4e's 20 and 58
are unblocked by S2; 46 is not, because it needs an area.*

***The order's other branch does not fire.*** *Nothing stopped, so no lemma names a third kind of obstruction about
submanifolds.*

| | predicted | **measured** |
|---|---|---|
| S1 | 0.6 | **yes** |
| S2 | 0.65 | **yes** |
| S3 | 0.5 | **yes** |
| `mathlib` has a second fundamental form | 0.1 | **absent** (`SEARCH_G3.txt`) |
| G3 statable | 0.65 | **statable** |

*Again every probe came in under budget. S1's instance, which I named as the cost, took 53 of S1's 93 lines.*

## ⌗ The order's symmetric negative, read in full — what the residual actually is

*The order: "if G3 is statable then ~89 are statable and the residual is the two absences."*

- **The count is `88`, not `89`.** *This was pre-registered at `+71.1`: receipt 46 needs the volume form, not G3.*
- **The residual is `111 − 88 = 23`, and it is not only the two absences:**

  | residual | count | state |
  |---|---|---|
  | G4f — spectral, heat-kernel, quantum | 9 | **absent** in `mathlib` and `Physlib` (`r7289`) |
  | G4g — spin | 3 | **absent** in both (`r7289`) |
  | G4e-46 — horizon areas | 1 | the volume form, THEORY since `r7267` B9 |
  | **G5 — global or topological identification** | **10** | ***unmeasured*** — *no layer has probed it, and no search has been run for it* |

- ***So "the residual is the two absences" holds for G4's remainder and fails for the whole.***
  - *G5 is `10` receipts that are neither absences nor measured. Examples: branched coverings, deck groups, coset
    spaces, `dS₂ × S²` identifications, Wick rotation.*
  - *My own `+71.1` text made the same omission: it named the residual as "spectral theory, spin and the volume
    form" and left out G5. **That is corrected here and not in the pre-registration.***
- ***What G3's result does establish:*** *every receipt outside G5 that is not statable is blocked by a named
  absence (spectral theory, spin) or a named THEORY item (the volume form).* ***No unnamed obstruction is left
  outside G5.***

## What each probe holds, in terms

- **S1 (`CurvatureProbe.lean` l.741–833).** Between any two manifolds:
  - `pullG φ g x = g_{φ x}(dφ ·, dφ ·)` — a `LinearMap.BilinForm` on `T_xM`, built with `compl₁₂` over
    `mfderiv`. It is the same type as K3's `gB`, so `scal` and `ricci` take it as they stand.
  - **`pullG_symm`** — the pullback of a symmetric form is symmetric.
  - **`pullG_comp`** — pulling back along `ψ ∘ φ` is pulling back twice, given both maps are differentiable. *So a
    slice of a slice is a slice.*
  - ***Instance, receipt 50 in 1+1:***
    - `dsFlat α (τ, x) = (α sinh(τ/α) + x² e^{τ/α}/2α, α cosh(τ/α) − x² e^{τ/α}/2α, x e^{τ/α})`, with `sinh` and
      `cosh` written through `exp`.
    - **`dsFlat_on`** — it lies on `−X₀² + X₁² + X₂² = α²`.
    - **`dsFlat_pull`** — the pullback of `−dX₀² + dX₁² + dX₂²` is `−dτ² + e^{2τ/α} dx²`.
    - *The derivative is assembled by `HasFDerivAt` combinators. Its value on `T_pM` goes through
      `mfderiv_eq_fderiv`, whose `fromTangentSpace` casts are identities by `rfl`. A `sympy` division found the one
      `linear_combination` coefficient, `−u₁v₁`, against `e^{τ/α} e^{−τ/α} = 1`.*
- **S2 (l.698–739).**
  - `sff` is `C^∞`-linear in `X` and `Y` (`sff_smul_X`, `sff_smul_Y`). ***It is pointwise in both outright:*** it
    reads `X x` and `Y x` only. *So, unlike curvature (`r7287` (1)), it needs no tensorial packaging in those slots.
    It differentiates `N`, which is the point.*
  - **`sff_symm`:**
    - *Hypotheses:* `cov.torsion = 0`; `N` `g`-normal to `X` and `Y` everywhere; `[X, Y]` `g`-normal to `N` at `x`;
      and compatibility along `X` and `Y` on the two functions `g(N, Y)` and `g(N, X)`, as `hcX`, `hcY`.
    - *Proof:* the two derivatives vanish because the functions are `0`. Then `mathlib`'s `torsion_eq_zero_iff`
      turns `∇_X Y − ∇_Y X` into `[X, Y]`, and `linarith`.
- **S3 (l.836–879), on the programme's metric.**
  - `gConf a = a(η)²(−dη² + dx²)`, `nConf a = a⁻¹ ∂_η`, `dx = ∂_x`.
  - **`nConf_unit`** — `g(N, N) = −1` and `g(N, ∂_x) = 0`, given `a(η) ≠ 0`.
  - **`sff_conf`** — `K(∂_x, ∂_x) = a′(η)` for `covConf a`, given `a` differentiable at `η` and `a(η) ≠ 0`.
    - *`D N · ∂_x = 0` because `N` depends on `η` alone, read off `HasDerivAt.inv` composed with `fst`.*
    - *The rest is R3's Christoffel form: `Γ(∂_x, N) = (a′/a²) ∂_x`.*
    - *On the unit tangent `e_x = a⁻¹ ∂_x` this is `a′/a² = H`, the Hubble rate of the slicing.*

## Beside the score, said and not rounded

1. ***Named induced metrics still need a connection to have curvature.*** G3a's 52 and 108, and all five of G3b,
   apply G2 to an induced metric. S1 puts that metric in K3's type, but the curvature needs a connection for it:
   - either the Levi-Civita PORT;
   - or an explicit Christoffel form per metric, as in R3 and K4.
   - ***Statable, not proved — as for G1 and G2.***
2. ***`sff_symm`'s compatibility is two hypotheses, not a structure.***
   - *`hcX` and `hcY` are compatibility on two specific functions. They are what the Levi-Civita connection
     gives, so on a named metric they are discharged by the PORT, or per instance as in S3.*
   - *S3 does not use `sff_symm`. With one tangent direction, symmetry is vacuous.*
3. ***S1 is a pullback along ANY map. Whether it is a metric is per instance.***
   - *It does not use `mathlib`'s `IsImmersionAt`, and it does not prove the pullback nondegenerate.*
   - *For the de Sitter instance, `dsFlat_pull` exhibits `−dτ² + e^{2τ/α}dx²`, which is nondegenerate by
     inspection. That is not stated in Lean.*
4. ***The instance is receipt 50 in 1+1, not in its own dimension.*** *The 3+1 flat slicing adds two more `xᵢ`
   with the same structure. Read, not built.*
5. ***G3d (receipt 107, a foliation as an object) is classed by reading:*** *level sets of a function with
   nonvanishing differential. `mathlib` has `Submersion.lean`, and no foliation.*
6. ***The extrinsic curvature on a general slice needs the unit normal as a field.*** *S2 and S3 take `N` as given.
   Building `N` from a hypersurface needs the metric's `toDual` of `dt`, normalised. That is K3's `toDual`
   pointwise, plus a square root. DEF by reading, not built.*

## The count, updated

| | `r7289` | **now** |
|---|---|---|
| statable now, of `111` | `69` | ***`88`*** (+ G3 `17`, + G4e `2`) — *`84` on measured machinery alone (the four volume-form receipts of G2)* |
| still unstatable, of `111` | `42` | ***`23`*** — G4f `9` and G4g `3` (**absent**), G4e-46 `1` (the volume form), G5 `10` (**unmeasured**) |

## The order's other constraint

***The port is not begun, and nothing here begins it.*** *S1 needs no connection. S2 takes the connection as a
hypothesis. S3 uses `covConf`, the one explicit connection in the tree.*
