# `r7695+71.1` — PRE-REGISTRATION: campaign 109, `r7695`, **2iv-b on `N`: the temporal separation `τ(q) − τ(p)` is not fixed by the geometry. For any neighbourhood `V` of `q`, every value in an open interval about it is the separation of a temporal function equal to `τ` outside `V`. The construction is a local bump on `N`.** ⌗ `700` new lines (band 400–1300), p `0.4`. **Expected stop:** uniform positivity of `dτ` on the unit future cone over a compact neighbourhood. **Fallback** stated below

*Registered before any Lean. The new probe is `probes/ThreefoldLocal.lean`, a copy of campaign 104's
`ThreefoldDistinct.lean` (with `minkN`, `td_temporal_cstep`, `to_cor_1c` and the `ac_` section). Everything new is
prefixed `tl_`.*

## A reading flag for 69: "arbitrarily"

- **P1 says the separation "may be altered arbitrarily by smooth local deformations of `τ` in a neighbourhood of
  `γ`".**
- **A local deformation cannot move it arbitrarily far.** Let `τ′` be temporal and equal to `τ` outside `V`. Along any
  future causal curve that enters and leaves `V`, both functions increase. So `τ′ − τ` can rise inside `V` only by what
  it gives back before leaving `V`, and that is bounded by the rise of `τ` across `V`.
- **What a local deformation does give** is a whole open interval of separations: the value is not an invariant.
  Arbitrary positive values need a non-local reparametrisation, `φ ∘ τ`.
- **A suggested wording for (iv):** "is not fixed by the geometry: smooth local deformations of `τ` in a neighbourhood
  of `γ` alter it, while keeping `τ` temporal". The Lean below proves that wording.

## ① The bump on `N` — `450` lines, p `0.45`

The setting is an `MSpacetime` with `LocallyOneChart`, `τ` temporal on an open `U ⊆ M`, `q ∈ U`, and `V ∋ q` open.

- **The bump:** in the preferred chart at `q`, take a `ContDiffBump` `ψ`, supported in a ball whose closure lies in
  `V ∩ U ∩ (chart source)`, with `ψ(q) = 1`. Pull it back to `N`, so `ψ = 0` off `V`.
- **`tl_cone_pos`, the expected stop:** on the compact support `K`, there is `c > 0` with `dτ(v) ≥ c‖v‖_chart` for
  every future causal `v`.
  - The unit future causal vectors over `K` form a compact set, because `g` and `T` are continuous.
  - `dτ` is continuous and positive on that set.
- **`tl_bump_temporal`:** `‖dψ‖ ≤ C`, so for `|δ| < c/C`, `τ_δ = τ + δψ` is temporal on `U`.

## ② 2iv-b — p `0.6`, given ①

**`tl_cor_threefold_iv_b`:** take a causal chain from `p` to `q` with `p ∉ V`, which we may assume after shrinking `V`
because `p ≠ q` by 2i. Then for every `δ ∈ (−δ₀, δ₀)`:
- `τ_δ` is temporal;
- `τ_δ = τ` off `V`;
- `τ_δ(q) − τ_δ(p) = τ(q) − τ(p) + δ`.

So the separation takes every value in an open interval.

## ③ The witness — p `0.7`

**`tl_witness`:** on `Pt`, take `to_cor_1c`'s null pair `(0, 1)`, `(0, e)` and `τ = U + V`. Two temporal functions,
equal off a small ball about `q`, give different separations.

## The fallback, if ① stops on `N`

State and prove ① to ③ on a one-chart spacetime: `minkN` on `Pt`, or the model `P`. There the chart is global, and the
bump and the cone bound are in coordinates. Its mark would be IN PART: a witness on `N`, not the general theorem.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
