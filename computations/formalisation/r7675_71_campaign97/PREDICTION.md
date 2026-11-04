# `r7675+71.1` — PRE-REGISTRATION: campaign 97, `r7675`. **Schwarzschild as an `MSpacetime`, in Kruskal's radial plane, with 3a/3b built on it.** ⌗ ① the foundation and 3a: `800` new lines (band 400–2000), p `0.6`. ② 3b: `500` new lines (band 250–1200), p `0.6`. The whole: p `0.5`. **Expected stops:** ① `LocallyOneChart` and the causal transfer when `F` is C¹ and positive only on `M = {UV < 1}`; ② `L_χ g = 0` for `g = −F(UV) dU dV`, with `F` non-constant. **Curvature is not needed for either row.** Row 8 is priced at the end

*Under `r7675`. Two new probes, built in parallel:
- `probes/SchwarzschildKruskal.lean` for ①, from campaign 91's `CurvedTangency.lean` (the conformal-scaling kit
  `cz_scale`/`cz_minkF`) with campaign 80's `Kruskal` radius `r(U, V)` copied in;
- `probes/SchwarzschildKilling.lean` for ②, from campaign 96's `KillingWhole.lean` with the same `r(U, V)`.

No Lean was written before this registration.*

## Why Kruskal rather than ingoing EF

- The probes already have Kruskal's `r(U, V)`, the inverse of `(r/2M − 1) e^{r/2M} = −UV`, built in campaign 80
  (`TangencyCondition.lean`), together with `F = (32M³/r) e^{−r/2M}`.
- Campaign 90's `cz_scale` shows that rescaling `g` by a positive `F` leaves `TStep`, `CStep`, `I^±`, `J^±`, `D`,
  `H` and the Cauchy property unchanged.
- So Schwarzschild's causal structure is the flat one already built, now carrying Schwarzschild's actual `F`.
- EF `(v, r)` is a relabelling of the region `V > 0`. 3a's statement is chart-free, and RESULT gives the EF reading.

## ① The foundation and 3a

***The spacetime `sk_S`.***
- `N = Pt`, the two-chart null-coordinate plane, with `M = {UV < 1}`, i.e. `r > 0`.
- `g = −F(r(U, V)) dU dV` and `T = ∂_U + ∂_V`.
- **`LocallyOneChart`.** `F∘r` is C¹ on `M`, by the inverse function theorem on `h(r) = (r/2M − 1) e^{r/2M}`, whose
  derivative is `r e^{r/2M}/4M² > 0`.

***The observer and its horizon.***
- **The observer** is static at `r₀ > 2M`, on the hyperbola `UV = −c` with `c = (r₀/2M − 1) e^{r₀/2M}`,
  reparametrised so that it is adapted.
- **The horizon:**
  - `D = I⁻(O) = {U < 0} ∩ M`, regions I and IV;
  - `S.H J = {U = 0}`, a non-empty set lying in `M`;
  - on it, `r = r_h = 2M` (`sk_H_r`).
- **Stated in advance.** For the eternal Kruskal spacetime, the static observer's `∂J⁻` is the whole line `U = 0`.
  That is the event horizon of the extended spacetime, bifurcation point included. The future horizon of region I is
  the branch `U = 0, V > 0`.

***3a, `sk_cor_EF_events`.*** For `p = (0, V₁)` and `q = (0, V₂)` with `0 < V₁ < V₂`:
- `p, q ∈ ∂J⁻(O)`, the null boundary of the static observer's causal past;
- `p ≠ q`, so they are distinct;
- `S.Cau p q`, so they are causally ordered;
- `¬ S.Chr p q`, so they are null-related: `U` is constant, and `chr_lt` needs a strict increase;
- both are at `r = r_h`.

## ② 3b, on the same metric

***The metric and the Killing field.***
- The raw `g = −F(r(UV)) dU dV` on `ℝ²`, with the formula of ①.
- `χ = (1/4M)(V∂_V − U∂_U)`, the Schwarzschild time translation `∂_t` in Kruskal coordinates.

***What ② proves.***
- **`L_χ g = 0`.** `χ(UV) = 0`, so `χ(F) = 0`, and the boost terms cancel as in the flat case. This is the expected
  stop.
- **`χ` is null on `U = 0`**, and non-zero for `V ≠ 0`, which is away from the bifurcation point.
- **`sk_cor_EF_coincident`:** `kw_lemma_killing_whole` along the generator `(0, e^{s/4M})` gives `p = (0, V₁)` and
  `q = (0, V₂)` metrically coincident. That is (a), (b), `Δx = 0` and `Δτ = 0`, so they have no invariant temporal
  separation.
- **The link to ①.** The formula for `g` is the same expression in both files. Probes cannot import probes, so RESULT
  states the shared formula.

## Is curvature needed?

***No, for 3a/3b.***
- 3a is causal structure.
- 3b is the Killing field plus `lem:killing`.
- That the metric *is* Schwarzschild's is taken by definition of `F`, as in campaign 80. Vacuum, `Ric = 0`, is not
  checked and is not used.

***No, for 8 either.***
- 8i is accumulation and cones, which is causal.
- 8ii is tangency, campaign 80's computation in this plane.
- 8ii-c/d, the lapse limits, are already BUILT.

## Row 8, priced and not built here

***What it needs.*** P1's `D` is region I alone, `r > r_h`. In the eternal plane, the static observer's `I⁻` also
contains region IV, the white hole.
- So 8 needs `N` = the open set `{V > 0, UV < 1}`, regions I and II, which is exactly EF's domain, as a manifold in its
  own right (`TopologicalSpace.Opens` with its charted structure). Then `∂J⁻` is taken inside it.
- It also needs Schwarzschild `t` as a Cauchy temporal function on region I.

***The price.*** About `1500–2500` lines at p `0.35`. That is why 3a/3b go first.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED. Non-vacuity is mandatory.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
