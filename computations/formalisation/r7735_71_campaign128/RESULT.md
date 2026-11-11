# `r7735+71.2` — RESULT: campaign 128, **P5's morphism group and its completeness are BUILT (rows 1 and 5): `gp_Mor = ⟨σ, τ⟩ ≃* D₃`. The P8 join `es_kernel_join` is built, and 60's two cosmetic items are made.** ⌗ `+321 / −13` lines, inside the registered band of 300–900 (point `550`). ⌗ p `0.45` came true. The expected stop, the crossing-point case, fell, and no fallback was used

*Against `PREDICTION.md` (`r7735+71.1`). 71 ran `lake env lean` on both files. Both exit 0 with no errors and no
warnings.*
- **`probes/Groupoid.lean`:** `41` `#print axioms` lines (`11` new), all `[propext, Classical.choice, Quot.sound]`.
- **`probes/StaticEinstein.lean`:** `61` (`2` new), all standard.
- **Other checks:** the forbidden-token grep is clean, both files import only Mathlib, and `check_no_sorry.py` reads
  ALL 29 THEOREMS COMPILE.

## P5 (`Groupoid.lean`)

- **Row 1, `gp_Mor`:** the continuous bijections `g` of `ℝ/2πℤ` with `sin 3g(w) = sin 3w`. `gp_sin3` is `sin 3w`
  on the circle, well defined. They form a subgroup of `Perm (ℝ/2πℤ)`. Inverses are continuous because a continuous
  bijection of the compact circle is a homeomorphism.
- **Row 5, `gp_completeness`:** `gp_Mor = ⟨σ, τ⟩`. With the earlier results this gives `gp_Mor_D3 : gp_Mor ≃* D₃`
  and `gp_Mor_card`: order 6, non-trivial.
- **The proof:**
  - `G(t) = g(↑t)` on `ℝ`.
  - By `gp_branch`, at every `t` either `3(G t − t) = 0` or `3(G t + t) = π` (closed sets `Sa`, `Sb`).
  - On a preconnected piece of either set, `G t ∓ t` takes values in a three-point set (`gp_tors0`, `gp_torsπ`),
    so it is constant (`gp_const`).
  - The interiors of `Sa` and `Sb` are disjoint, because the crossing points `π/6 + kπ/3` are `π/3` apart
    (`gp_cross_sep`, `gp_six`). The interiors cover `ℝ`.
  - At a crossing point `t₀`, each side of length `π/6` lies in one branch. If the sides differ, then
    `G(t₀ + π/12) = G(t₀ − π/12)`, which contradicts injectivity. This is `prop:completeness`'s fold argument
    exactly.
  - By connectedness of `ℝ`, one branch holds everywhere, so `g` is `r i` or `sr i` of `gp_φ`.
- **Reading:** the paper's proof is right as written, invertibility included. No flag.

## P8 (`StaticEinstein.lean`)

- **`es_kernel_join`:** on `(a, b)` with `0 ≤ a`, `f` twice differentiable and `f ≠ 0`, all sixteen components
  `G^μ_ν + Λδ^μ_ν` of `diag(−f, 1/f, r², r² sin²θ)` vanish at every point with `r ∈ (a, b)` and `sin θ ≠ 0`
  ⟺ `rf′ + f − 1 + Λr² = 0` on `(a, b)`.
  - It joins `es_construction_gauge`, `es_G_offdiag` and `ok_vacuum_iff_ode` through `es_hyp_of_interval`.
  - `es_sds_vacuum_full` is the SdS instance.
- **60's ⓵:** `lf_closed` and `lf_open` now bind their indices with the same letters, `(i j k l)`. `b` could not
  be used in `lf_open`, where it names the leaf's `X₁ = b`.
- **60's ⓶:** `lf_witness`'s docstring now uses one sense of witness. It gives each leaf's curvature value at a
  concrete point of a non-empty chart, and for the flat leaf points to `lf_flat`'s identity.

## Marks (P5's inventory, `r7733_71_survey/SURVEY.md`)

- **Built (9):** 1, 2a, 2c, 3, 4, 5, 7b, 8 and 13.
- **Built in part (6):** 2b, 7a, 9, 10, 11b and 12a, in other probes.
- **Not begun (2):** 11a and 12b.
- **No formal core (1):** 6.

**Next (campaign 129):** 11 and 12, the monodromy (copying `Row18Monodromy`'s covering) and the deck group.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
