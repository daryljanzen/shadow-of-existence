# `r7727+71.1` — PRE-REGISTRATION: campaign 124, **P8's static Einstein tensor from the coordinate Riemann tensor: rows 1a and 3a–c, delivering eq. `Ttt`, `Ttheta`, `rho-B` and `prho`**. ⌗ `650` new lines (band 450–1000), p `0.55`. **Expected stop:** the Christoffel table and Ricci assembly for `diag(−A, 1/F, r², r² sin²θ)` with two general profiles

*Registered before any Lean.*
- **The probe** is `probes/StaticEinstein.lean`. It is a copy of campaign 123's `OperatorKernel.lean`, so P8's
  names stay in one file, plus campaign 110's coordinate-curvature sections, `KrCurvature` and `KrTrig`, copied
  verbatim from `SlicingCurvature.lean`. It does not copy the whole chain, since no other part of the chain is
  needed.
- **Prefix:** everything new is `es_`, in `section EsStatic`.
- **The Einstein tensor** is formed from `kr_Riem`:
  - Ricci `R_{bd} = Σ_a R^a_{bad}`;
  - scalar `R = Σ g^{bd} R_{bd}`;
  - mixed `G^b_c = Σ_d g^{bd} R_{dc} − ½ δ^b_c R`.
- **8πT is `G + Λ`.**

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 1a | For `g = diag(−A(r), 1/F(r), r², r² sin²θ)`, at a point where `A, F, r, sin θ ≠ 0`, with `A, F` differentiable near `r` and `A′, F′` differentiable at `r`: `G^t_t = (rF′ + F − 1)/r²`, `G^r_r = (rFA′/A + F − 1)/r²`, and `G^θ_θ = G^φ_φ = FA″/2A − FA′²/4A² + F′A′/4A + FA′/2rA + F′/2r` | 450–850 | 0.55 |
| 1a, `A = F` | **eq. `Ttt`:** `G^t_t = G^r_r = (rf′ + f − 1)/r²`. **eq. `Ttheta`:** `G^θ_θ = G^φ_φ = f″/2 + f′/r`. With `+Λ`, these are P8's `8πT^t_t = 8πT^r_r` and `8πT^θ_θ = 8πT^φ_φ` | 40–80 | 0.8 |
| 3a | eq. `rho-B`: `G^t_t` has no `A` in it | (in 1a) | — |
| 3b | eq. `prho`: `G^r_r − G^t_t = (F/r)(A′/A − F′/F)`, which is `(F/r)(ln(A/F))′` where `A/F > 0` | 30–60 | 0.9 |
| 3c | The lock `A = F` gives `G^r_r = G^t_t`, so `p_r + ρ = 0` | 10–20 | 0.98 |
| non-vacuity | SdS (`A = F = 1 − 2M/r − Λr²/3`) at any point with `f ≠ 0`, `r > 0`, `sin θ ≠ 0`: the hypotheses hold, and with `ok_sds_solves`, `G^t_t + Λ = G^r_r + Λ = G^θ_θ + Λ = 0`. The vacuum, from the Riemann tensor itself | 40–80 | 0.8 |

**Scope.** Only the diagonal mixed components are claimed, which is what eq. `Ttt`–`Ttheta` list. That the
off-diagonal components vanish is not claimed.

**When this lands,** "given the matter functional" can come off `thm:kernel`'s formal sentence. P8 eq. `Ttt` and
eq. `Ttheta`, which `ok_vacuum_iff_ode` took as input, are then theorems from the metric.

**The expected stop** is the 64-entry Christoffel table and the 16 Riemann components behind the Ricci diagonal,
with `A`, `F` general. The plan is to name each Christoffel entry as a function of one variable, so that each
`kr_pd` reduces to a single `deriv`, and to use `kr_pd_congr` on the open set where the table holds. **The
fallback** is `A = F` only: 1a with `A = F` built, 3a–c left BUILT IN PART.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
