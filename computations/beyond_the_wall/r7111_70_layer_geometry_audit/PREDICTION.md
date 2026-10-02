# r7111+70.1: pre-registration for `r7109` Q1 (⓵, ⓶) and `r7111` Q1 (`PO-73`)

*This is committed before any computation. It was read at `origin/main` `66539337`. What I have read so far:*
- *`P15` `sec:properframe`, `sec:largescale` (the S³ and floor sentences), `sec:intro` (one supplier) and the `sec:scope`/`sec:transmission` "unaltered" sentence;*
- *the docstrings of `60`'s `r7106` and `r7108` receipts.*

*Nothing is run through the transfer. No spectrum is computed. `60`'s numbers are taken as given and not re-derived: α = 5213.287 Mpc, α/r₀ = 1.0320, χ_rec = 0.8555π, the combs, the Hopf count, s_tot.*

## The items owed, enumerated with a state against each (66's `r7109` rule)

| item | source | state at this commit |
|---|---|---|
| ⓵ is the constant-τ̃ layer a round S³ at the Nariai mass? Its induced metric, its extrinsic curvature, and its radius along the bead | `r7109` Q1 | pre-registered here; computed in `geometry.py` |
| ⓶ is there a timelike congruence on the layer, and is it the same object as the null bundle under the reassignment? | `r7109` Q1 | pre-registered here; computed in `geometry.py` |
| `PO-73`: is there a reading on which "r_* finite ⇒ carried across unaltered" and "lift η finite and imaginary ⇒ e^{−ks_tot}" are both true of the same object? | `r7111` Q1 | pre-registered here; computed in `geometry.py` and read from the papers |
| scope an instrument for "a tolerance surviving on something other than the measurement" | `r7111`, asked as a scoping question rather than an order | a scoping note in the reply; nothing built unless 66 orders it |
| whether 70 wants to own `P15R234` | `r7109`, an offer | answered in the reply |

## The outcomes, tabled with the one that costs another seat most first

1. **THE LAYER IS NOT AN S³ AT THE NARIAI MASS.** This costs `P15` `sec:largescale`, the gate's `r7109` decline of `60`, the S³ harmonic basis `r7108` evolves, and therefore the framing of `PO-73`.
   - `sec:largescale` says *"the cosmological layers are the closed S³ of constant τ̃ = τ + χ"* and builds the discrete spectrum k_L = √(L(L+2))/r₀ on it.
   - If the constant-τ̃ hypersurface of the proper-frame metric (`eq:proper-frame` with `eq:scalefac` at the Nariai amplitude) is not a round S³, then that sentence is not a property of the cosmology's geometry. The S³ would belong to a different metric, `60`'s "the sphere lives at zero mass".
2. **THE LAYER IS AN S³** (or locally one) **AT THE NARIAI MASS**, as the gate reads it. This costs `60`'s `r7104`/`r7106` reading.
3. **⓶: NO TIMELIKE CONGRUENCE CROSSES THE LAYER.** `60`'s reading stands. Or: **A TIMELIKE CONGRUENCE EXISTS AND IS THE NULL BUNDLE UNDER AN ISOMETRY.** The gate's reading stands as geometry.
4. **`PO-73` DISSOLVES:** the two sentences are true of the same object. Or: **`PO-73` STANDS AS OPENED.**

## What I expect, so a miss is visible

- **⓵: outcome 1.**
  - I expect the induced metric on τ̃ = const to come out as **(r′² − 1) dχ² + r² dΩ² = −f(r) dχ² + r² dΩ²**: a line times a round S² of radius r(τ̃), constant along the layer. That is **ℝ×S², not S³, at every τ̃ and at every mass.**
  - Its intrinsic Ricci eigenvalues should be (0, 1/r², 1/r²), where a round S³ would give three equal values.
  - **At the Nariai mass f ≤ 0 with a double root at r_N = α/√3, so I expect the layer to be spacelike everywhere except at r = r_N, where it degenerates to null.** That is the epoch x = 1, z = x₀ − 1, the acceleration onset.
  - I expect the extrinsic-curvature trace to be non-zero except at isolated τ̃.
  - I expect the Kretschmann scalar of `eq:proper-frame` to be 24/α⁴ + 12 r_s²/r⁶ ≠ 24/α⁴. So no region of the Nariai geometry is locally de Sitter, and the dS presentation's S³ is not a hypersurface of it under any isometry.
  - ⇒ **I expect the gate's ground for declining (an expanding S³ has K ≠ 0, so the maximal-slice identity does not quantify over it) to be correct as a statement about dS, and irrelevant at r_s ≠ 0.** The obstruction at the Nariai mass is not maximality; there is no S³ slice there at all.
- **⓶:**
  - I expect a timelike geodesic congruence to cross every layer: the E = 1 congruence ∂_τ, with g_ττ = −1 and non-orthogonal to the layer, at 45°. So **`60`'s "no matter observer at a point of that layer" is false of the proper-frame geometry.**
  - I expect it **cannot be the same object as a null bundle under any isometry**, because causal character is invariant.
  - In global dS, I expect the comoving congruence to be timelike and the Hopf-fibre congruence u = ∂_t + a⁻¹ ξ̂ to be null and geodesic: two different objects. So **the gate's "matter stationary within an expanding S³ and space spinning uniformly along the Hopf direction are one description" fails as geometry**, unless the reassignment is not an isometry. In that case "two presentations of one geometry" is what fails.
- **`PO-73`: neither 4a nor 4b exactly.**
  - I expect r_* = ∫dr/f and η = ∫dτ̃/r, taken over the same segment of the lap (the lift, r ∈ (−A, 0), A = (r_s α²)^{1/3}), to be **different integrals.** The first should be real and finite, because f > 0 there and this is a static region. The second should be purely imaginary, because 1 − f < 0 there, so the E = 1 geodesic is classically forbidden and τ̃ goes imaginary.
  - So the two sentences are both true, **of different objects:** a static-frame radial wave labelled by ω, and a harmonic on the E = 1 slicing. They are not the same object.
  - **And r7108's object presupposes the S³ layer, so if ⓵ fires, the envelope as computed acts on a basis the Nariai geometry's layer does not carry.** I expect to report `PO-73` as *mis-posed as a tension between two readings of one finiteness* and *conditional on ⓵*. Its real content is which object carries A_s and n_s, which is the row's own discharge criterion.

## Instrument

`geometry.py` in this directory, using sympy and scipy only:
- the Einstein tensor of `eq:proper-frame` with r = r(τ + χ) and r′² = r_s/r + r²/α² (that it is SdS-vacuum with Λ);
- the induced metric, intrinsic Ricci and extrinsic curvature of τ̃ = const, symbolically and then on a τ̃ grid at the Nariai amplitude;
- the Kretschmann scalar;
- the E = 1 congruence's norm and its angle to the layer;
- in global dS (S³ in Hopf coordinates), the norm and geodesic equation of the comoving congruence and the Hopf-fibre congruence;
- along the lift, f, 1 − f, r_* and η, with η's modulus compared to `60`'s lift length.
