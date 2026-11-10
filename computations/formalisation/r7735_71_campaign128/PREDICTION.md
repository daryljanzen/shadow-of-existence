# `r7735+71.1` — PRE-REGISTRATION: campaign 128, **P5's morphism group and the completeness of ⟨σ, τ⟩ (rows 1 and 5), plus the P8 join declaration and 60's two cosmetic items**. ⌗ `550` new lines (band 300–900), p `0.45`. **Expected stop:** the branch argument at a crossing point

*Registered before any Lean.*
- **P5's rows go into `probes/Groupoid.lean`,** P5's citable file, prefix `gp_`.
- **The P8 items go into `probes/StaticEinstein.lean`,** P8's citable file.

## P5 rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 1 | `gp_s3 : ℝ/2πℤ → ℝ` is `w ↦ sin 3w` (well defined). `gp_Mor` is the subgroup of `Perm (ℝ/2πℤ)` of continuous `g` with `gp_s3 ∘ g = gp_s3`. It is closed under inverses because a continuous bijection of the compact circle is a homeomorphism | 60–120 | 0.85 |
| 5 | **`gp_Mor = ⟨σ, τ⟩`.** Hence `gp_Mor ≃* D₃ ≃* S₃` (with `gp_D3`, `gp_S3`) | 300–650 | 0.45 |

**Row 5's proof, as planned.**
- **Lift to `ℝ`:** `G(t) = g(↑t)`. By `sin a = sin b`, at every `t` either `3(G t − t) = 0` (set `Sa`) or
  `3(G t + t) = π` (set `Sb`) in the circle. Both sets are closed.
- **Constancy:** on a preconnected subset of `Sa`, `G t − t` takes values in the finite set of 3-torsion points, so
  it is constant. On `Sb`, `G t + t` takes values in the three solutions of `3v = π`, so it is constant too.
- **Interiors:** `int Sa` and `int Sb` are disjoint, because `Sa ∩ Sb` is the discrete set `{π/6 + kπ/3}`. They
  cover `ℝ`:
  - at a point outside `Sa ∩ Sb`, the other set's complement is a neighbourhood;
  - at a crossing point `t₀`, each one-sided interval of length `π/6` lies in one set;
  - if the two sides differ, then `G(t₀ + s) = G(t₀ − s)` for small `s > 0`, which contradicts injectivity.
- **Conclusion:** by connectedness of `ℝ`, `G t − t` or `G t + t` is constant on all of `ℝ`, so `g` is a rotation by
  a 3-torsion point or a reflection `w ↦ −w + c` with `3c = π`. Either way `g ∈ range gp_φ = ⟨σ, τ⟩`.

## P8 items (`StaticEinstein.lean`)

| Item | Statement | Lines | p |
|---|---|---|---|
| `es_kernel_join` | On `(a, b)` with `0 ≤ a`, `f` twice differentiable and `f ≠ 0`: `G^μ_ν + Λδ^μ_ν = 0` for all 16 `(μ, ν)` at every point with `r ∈ (a, b)` and `sin θ ≠ 0` ⟺ `rf′ + f − 1 + Λr² = 0` on `(a, b)`. One statement for `thm:kernel`'s `T_{μν} = 0`, joining `es_` and `ok_` | 50–120 | 0.75 |
| 60's ⓵ | `lf_open`'s indices renamed `(a b e d)`, as in `lf_closed` | 2 | 1 |
| 60's ⓶ | `lf_witness`'s docstring: one sense of witness (a curvature value for the two curved leaves; the flat leaf's value is `lf_flat`'s identity, and the witness shows its chart non-empty) | 3 | 1 |

**Non-vacuity:**
- **P5:** `gp_Mor` contains `σ ≠ 1` and has 6 elements.
- **P8 join:** SdS satisfies both sides wherever `f ≠ 0`, by `ok_sds_solves`.

**The expected stop** is row 5's crossing-point case: the one-sided intervals, constancy on them, and the
injectivity contradiction. **The fallback** is to prove completeness for maps `g` that are a single branch near
every point, and mark row 5 BUILT IN PART with the crossing case named. **Interpretive:** "the groupoid" as a
category of vantages (row 1's objects).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
