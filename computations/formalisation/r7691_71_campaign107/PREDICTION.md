# `r7691+71.1` — PRE-REGISTRATION: campaign 107, `r7691`. **The four rows still in part priced, and the cheapest, 2iii, taken to BUILT: `g(γ̇, γ̇)` is constant along any geodesic on `N`, so a null geodesic segment is null throughout; witnessed on Schwarzschild's horizon generator in `∂J⁻(𝒥⁺)`.** ⌗ `400` new lines (band 200–900), p `0.65`. **Expected stop:** identifying the intrinsic `g(γ̇, γ̇)` with its chart expression along the curve, and the Christoffel algebra in a chart

*Registered before any Lean.*

## The prices

| Row | What BUILT needs | Lines | p | Expected stop |
|---|---|---|---|---|
| **2iii** | a chart-wise geodesic on `N`; energy conservation in each chart; gluing along `[a, b]` | 300–500 | 0.65 | the chart identity for `g(γ̇, γ̇)` |
| 2iv-b | P1 says "smooth **local** deformations of `τ` in a neighbourhood of `γ`". That needs a bump on `N` keeping `τ` temporal over a compact support | 500–900 | 0.4 | the uniform positivity of `dτ` on the future cone over the support |
| 6b-ii | the achronal-boundary theorem in general | 2500–6000 | 0.15–0.3 | waits, by your r7669 ruling |
| 7c | a curvature singularity needs curvature: the Kretschmann scalar of 4D Schwarzschild, computed by hand in coordinates | 1500–3000 | 0.15 | Riemann from second derivatives; no Levi-Civita on `N` |

***Two cheaper readings, which do not move a mark:***
- **2iv-b by reparametrisation, `φ ∘ τ`:** about 150 lines, p 0.9. Any positive value of `τ(q) − τ(p)` is reachable while `τ` is unchanged below `τ(p)`. But the change is global in space, not local to `γ`, so it is still IN PART.
- **7c on the locus reading:** about 150 lines, p 0.85. Read the singularity as `UV = 1`, outside `W`. Then no slice's closure meets it. This is interpretive, with no curvature.

***8ii-e, the price you asked for.*** The smoothed shell itself (`r` an ODE solution, with `C¹` dependence) is **1500–3000 lines, p 0.2**. **It is not needed.**
- Accumulation (`KLi = KLs = 𝓗⁺`) is causal. `cz_scale` preserves every causal notion, the slices, `D` and `𝓗⁺`.
- So run `mh_causal_alignment_gh_N` on the flat metric `−dũ dv` restricted to `M′`, which is `C^∞` and has `LocallyOneChart`, with campaign 102's `D`, `𝓗⁺` and Cauchy property.
- Then carry the conclusion to the `C⁰` shell `sh_S = flat.cz_scale Φ′` unchanged.
- **300–500 lines, p 0.65.** Its expected stop is the `cz_scale` transport of `SublevelProper` and the slices.

So 8ii-e is about as cheap as 2iii. I take 2iii as ordered, and offer 8ii-e next.

## Campaign 107: 2iii

*The new probe is `probes/NullGeodesic.lean`, a copy of campaign 106's `StationaryHorizon.lean` (with `ld_h_eq_hRep`,
`se_` on `W` and `sx_`). Everything new is prefixed `ng_`.*

***① The definition, p `0.75`.*** `S.IsGeodesicOn γ a b`. For every `t ∈ [a, b]`, in some preferred chart about
`γ t`, the chart curve `c` is `C²` near `t` and satisfies `c″ = −Γ(c)(c′, c′)`. Here `Γ` is the Christoffel map of
`hRep g` (Koszul: `g(Γ(u, v), w) = ½(Dg(u)(v, w) + Dg(v)(u, w) − Dg(w)(u, v))`), and the chart metric is `C¹` (from
`LocallyOneChart`).

***② Energy conservation, p `0.65`.***
- **`ng_energy_const`:** on a geodesic, `t ↦ g(γ t)(γ̇, γ̇)` is constant on `[a, b]`.
- **The proof:**
  - In each chart, `d/dt hRep(c)(c′, c′) = Dg(c′)(c′, c′) − 2g(Γ(c′, c′), c′) = 0`.
  - The intrinsic value equals the chart value.
  - A function with zero derivative on an interval is constant.

***③ 2iii, p `0.75`.*** **`ng_cor_threefold_iii`:** a geodesic segment that is null at one point is null along the
whole segment.

***④ The witness, p `0.55`.*** **`ng_witness`:** on Schwarzschild on `W`, the horizon generator `s ↦ (0, V₀ + s)`, in
`𝓗⁺ = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`), is an affinely parametrised null geodesic.
- On `U = 0`, `∂_V F = F′(r) r_V ∝ U = 0`, so `V″ = 0`.
- The fallback is flat `Pt` with `(0, V)`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
