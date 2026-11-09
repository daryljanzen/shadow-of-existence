# Survey for the fourth paper to formalise, and its inventory: `r7725+71.1`

*A survey and inventory, not a campaign. It reads the corpus at `4f9c725d` (r7725) and the probes through campaign
122 (`SlicingCurvature.lean`). The marking rule is the one used for P1–P3: **BUILT**, **BUILT IN PART** (gap
named), **NOT BEGUN**. Every Lean name below was grepped for its declaration.*

**Choice: P8, `corpus/slicing_operator.tex`.** First campaign (123): the vacuum kernel, which is rows 1b–1e and 2. It
is registered in `r7725_71_campaign123/PREDICTION.md`.

## The re-weighing after P3

`r7717_71_survey` ranked the papers by `\cite` count and fit. P3's closure changes nothing that decided the ranking.

| P | key | cites | stmts | fit | now |
|---|---|---|---|---|---|
| 7 | `JanzenCRframework` | 235 | 20 | Low | Unchanged. Mostly "ontological layers" and "projections", which are undefined |
| 14 | `JanzenMatter` | 162 | 2 | Low | Unchanged. Spinor zero-modes, "forced within CR" |
| 15 | `JanzenCRcosmology` | 146 | 7 | Low | Unchanged. Only `prop:throat` and `prop:flat` suit the kit |
| 13 | `JanzenBoundary` | 126 | 4 | Low | Unchanged. Standard Model gauge groups |
| 17 | `JanzenGeometricCore` | 114 | 2 | Low | Unchanged. `prop:unique` needs a classification Mathlib lacks |
| **8** | `JanzenOperator` | 95 | 5 | **Medium–high** | **Chosen.** All five are precise. Its core is P3's SdS family (`f = 1 − 2M/r − r²/α²`) derived, not assumed |
| 10 | `JanzenCanonicalTime` | 95 | **0** | — | No stated results (not scored in `r7699`) |
| 5 | `JanzenGroupoid` | 91 | 13 | Low–medium | Unchanged. The groupoid is undefined; its precise parts (σ, S₃) are now built in `SlicingCurvature.lean` and `Row18Monodromy.lean` |
| 16 | `JanzenCosmogenesis` | 87 | **0** | — | No stated results |

**Why P8.**
- **It has the highest fit among the remaining papers with more than two statements.** Every statement is precise:
  an ODE and its operator, two Einstein-tensor identities, a radial geodesic and its exact solution, and the
  hyperboloid's leaves.
- **It is P3's foundation.** `thm:kernel` derives the SdS family that P3's slicing curve assumes. Fifteen papers cite it
  as `JanzenOperator`, P2, P3, P7, P9 and P15 among them.
- **The kits fit it.**
  - The 1D calculus (`thm:kernel`, `prop:bend`, `prop:cosmo`'s solutions) is in Mathlib.
  - The Einstein-tensor rows have receipt-level proofs in the other engine (`SecondSeatStatic.lean`).
  - The probe chain has campaign 110's coordinate Riemann tensor, now exercised on 2-metrics by campaign 122
    (`sl_gauss_g2`).
- **Still not P7, despite its 235 citations.** Only two or three of its twenty statements are precise.

---

# Inventory of P8 (`corpus/slicing_operator.tex`)

The grep for `\begin{theorem|proposition|lemma|corollary}` finds **5** statements, split into **16 rows**.
- **The construction gauge** (eq. `gauge`) is `ds² = −f dt² + dr²/f + r²dΩ²`. `8πT^μ_ν = G^μ_ν + Λδ^μ_ν`.
- **Other-engine work counts as BUILT IN PART:** `SecondSeatStatic.lean` and `CurvatureInstances.lean` import
  `ShadowEngine`. The gap is that it is not in a Mathlib-only probe.

## 1. `thm:kernel` (l.206)

**1a.** The Einstein tensor of `diag(−A, 1/F, r², r² sin²θ)`:
- `G^t_t = (rF′ + F − 1)/r²`, with no `A` in it;
- `G^r_r = (rFA′/A + F − 1)/r²`;
- with `A = F`, `G^θ_θ = F″/2 + F′/r`.
- **Kit:** `static_Gtt_Grr`, `static_AeqF` (`SecondSeatStatic.lean`). **Mark: BUILT IN PART.**
- **Remains:** the same from the chain's coordinate Riemann tensor on `Fin 4` (`kr_Riem`), with a new Ricci
  contraction.
- **Price:** 400–800 lines, p 0.6. **Stop:** `fin_cases` over `Fin 4` with two general profiles.

**1b.** `T = 0 ⟺ (rf)′ = 1 − Λr²`. The angular equation follows by differentiating.
- **Mark: NOT BEGUN** (algebraic, given 1a's components). 40–80 lines, p 0.95.

**1c.** The general solution. On a preconnected `I ⊆ (0, ∞)`, a differentiable `f` solves the ODE iff
`f = 1 − 2M/r − Λr²/3` for one constant `M`.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.9.

**1d.** The operator `Lf = (rf)′` on `[r₁, r₂] ⊂ (0, ∞)`:
- `|Lf| ≤ |f| + r₂|f′|`, so `L` is bounded `C¹ → C⁰`;
- `ker L = span{1/r}`;
- every continuous `g` has the preimage `f = (1/r)∫_{r₁}^r g`.
- So `L` is onto with a one-dimensional kernel: index 1.
- **Mark: NOT BEGUN.** 150–300 lines, p 0.75. **Stop:** the fundamental theorem of calculus at the interval's ends.
- **Interpretive:** "the index is the mass" and its stability along Fredholm paths are a reading and a citation. The
  formal content is kernel and range.

**1e.** "Every density is realised by some cut" (the matter functional is onto). For continuous `ρ`,
`m(r) = ∫ 4πs²ρ` gives an `f` whose `8πT^t_t` is `−8πρ`.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.85.

## 2. `prop:bend` (l.237)

**2.** With `f = 1 − 2m(r)/r − Λr²/3` (eq. `massfn`), `8πT^t_t = (rf′ + f − 1)/r² + Λ = −2m′/r²`, so
`ρ = m′/4πr²`.
- **Kit:** `static_density` (other engine). **Mark: BUILT IN PART.** 30–60 lines, p 0.97.

## 3. `prop:lapse` (l.273)

**3a.** `T^t_t` is independent of `A`. **Kit:** `static_Gtt_Grr`. **Mark: BUILT IN PART.** It comes with 1a.

**3b.** `8π(T^r_r − T^t_t) = (f/r)(ln(A/f))′`.
- **Mark: BUILT IN PART** (the components are in the other engine; the identity is new). 40–80 lines, p 0.95.

**3c.** The lock `A = f` gives `p_r + ρ = 0`. **Mark: NOT BEGUN.** 10–30 lines, p 0.98.

## 4. `prop:cosmo` (l.339)

**4a.** Radial timelike geodesics of SdS conserve `E = f ṫ` and obey `(dr/dτ)² = E² − f`.
- **Kit:** campaign 110's `kr_Γ` on `Fin 2`, and campaign 113's geodesic pattern. **Mark: NOT BEGUN.**
- 200–400 lines, p 0.7.

**4b.** `E = 1`: `r(τ) = (2Mα²)^{1/3} sinh^{2/3}(3τ/2α)` solves `(dr/dτ)² = 2M/r + r²/α²` for `τ > 0`.
- **Kit:** `sinh23_flow` (`ShadowEngine.lean`). **Mark: BUILT IN PART.** 60–120 lines, p 0.9.

**4c.** `Λ = 0`: `r = (9M/2)^{1/3} τ^{2/3}` solves `(dr/dτ)² = 2M/r`.
- **Mark: NOT BEGUN.** 40–80 lines, p 0.9.
- **Interpretive:** "the flat ΛCDM scale factor" and "Oppenheimer–Snyder" are identifications by citation.

## 5. `prop:trichotomy` (l.419)

**5a.** The closed leaf. `X₀ = c` on the hyperboloid is the sphere `ΣX_i² = α² + c²`, a round `S³` of curvature
`1/(α² + c²)`.
- **Mark: NOT BEGUN.** 200–400 lines, p 0.7. **Stop:** the round `S³`'s coordinate Riemann tensor on `Fin 3`.

**5b.** The flat leaf, a horosphere of curvature 0.
- **Kit:** `horo_on_hyperboloid` (other engine). **Mark: BUILT IN PART.** 100–200 lines, p 0.8.

**5c.** The open leaf. `X₁ = b > α` gives `X₀² − ΣX_i² = b² − α²`, an `H³` of curvature `−1/(b² − α²)`.
- **Kit:** `open_leaf_curv` (other engine, scalar `−6/A²`). **Mark: BUILT IN PART.** 150–300 lines, p 0.75.

**5d.** "They carry `k = +1, 0, −1`." The normalisation of 5a–c's signs. **No formal core.**

## Totals

- **16 rows.** 1 has no formal core (5d).
- **Marks:** 0 BUILT; 7 BUILT IN PART (1a, 2, 3a, 3b, 4b, 5b, 5c); 8 NOT BEGUN.
- **No reading flags found so far.**
  - The kernel statement is precise as stated.
  - "Index 1" is `dim ker − codim range = 1 − 0`, which is correct.
- **Whole paper:** about 1,500–3,000 new lines.

## Campaign order

- **123:** the vacuum kernel: 1b, 1c, 1d, 1e and 2. Pure 1D calculus, in a standalone probe.
- **124:** 1a and 3a–c: the static Einstein tensor in the chain.
- **125:** 4a–c: the radial geodesic and its exact solutions.
- **126:** 5a–c: the three leaves.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
