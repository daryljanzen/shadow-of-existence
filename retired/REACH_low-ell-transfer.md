> **⌖ RETIRED r1552.** This was the low-ℓ transfer reach (r506). **Landed:** built in P15 on a genuine Boltzmann transfer; A1.2 struck DONE r1006.
> Kept as record; **do not work from it.**


# Reach investigation — the low-ℓ transfer (P12 §5)

*Started r504, 2026-06-29. The first reach-grind target: pin the §5 low-ℓ floor's flagged "O(1) ambiguity" as far as we can ourselves, before the council. Do-not-assert holds where flagged.*

## The question
§5 projected the discrete closed-S³ modes to angular multipole at leading order,
`ℓ_L ≃ √(L(L+2)) · D_C / r_0`, and flagged a "genuine O(1) ambiguity in r_0 (areal vs
curvature radius) and the discrete-to-continuous map." Two distinct worries hid inside:
the **radius** (which length is r_0?) and the **projection** (arc vs chord — flat-sky
ℓ≈kD_C, or closed-universe ℓ≈√(L(L+2)) sin χ_LSS?).

## Findings (grounded at P9 source)
1. **Radius — resolved.** P9 (line 446) takes "the radius of the expanding 3-sphere" as
   the coordinate; the cosmological layer is that round S³. So r_0 is the S³ **curvature
   radius itself**, not an areal radius of a chosen 2-sphere. The eigenvalue L(L+2) and the
   projection share one length. The "areal vs curvature" parenthetical was wrong; removed.

2. **Projection — flat, not closed-lensed.** Prop:flat: the distance (constant-τ) slice is
   flat ℝ³, isotropic ⇒ transverse = radial = D_C at **every** wavelength. So the
   discreteness lives in the **source** (k_L = √(L(L+2))/r_0 on the closed-S³ layer), and the
   **projection** is the flat-sky ℓ ≃ k_L D_C — *not* the closed-universe sin χ_LSS lensing.
   - High-stakes: χ_LSS = D_C/r_0 ≈ 2.75, so flat ⇒ ℓ_2≈7.8, closed-lensed ⇒ √8·sin(2.75)≈1.1.
     A ~7× fork; Prop:flat selects the flat branch.

3. **Consistency check (verified, this session).** The *same* flat projection returns the
   validated acoustic scale: ℓ_A = π D_C / r_s ≈ 303 (observed ~301; P9 banks this). That
   anchor is short-wavelength, but the transverse flatness it rests on (Prop:flat) is
   wavelength-independent, so it supports the flat projection at the floor too.

4. **Residual — narrowed.** Only the few-percent eigenvalue convention remains: √(L(L+2))
   vs β=L+1 is 6% at L=2, ~0 by L~10. So the floor **location** ℓ_2≈8 is robust to ~10%,
   not order-level.

## Status
- **Located (robust ~10%):** the floor at ℓ_2≈8 — flat projection, curvature radius,
  acoustic-anchored. §5/caption/abstract tightened from "O(1) / leading-order" to this.
- **OPEN — the next reach target:** the exact large-angle **shape**. Each discrete S³ mode
  spreads into a C_ℓ profile through its hyperspherical-harmonic window Φ^β_ℓ(χ), carried
  across the **full non-synchronous transfer** (the τ̃=τ+χ map between the closed-S³ source
  layer and the flat observation slice). This broadens the floor into a profile *without
  moving its location*, and computing it would also **confirm** the long-wavelength flat
  projection (the one step argued from Prop:flat but not yet computed mode-by-mode).
  Do-not-assert on the profile until built.

## The one unproven step (held honest)
The flat-sky projection ℓ≈k_L D_C at long wavelength (λ~D_C~r_0) is *argued* from Prop:flat
+ the acoustic anchor, not *computed* mode-by-mode. The shape computation (item above) is
what would close it. Until then: location grounded, shape open.

---

## CORRECTION (r505) — after reading Janzen2015's appendix at source

Daryl pointed to Janzen2015 (`resources/JanzenFQXi2012.tex`, §sec_CSdSCS) where the
projection geometry is derived algebraically. It **overturns the r504 flat-sky reading.**

- The fundamental **background is a closed S³** (de Sitter); the anisotropic SdS proper
  frame is the moving observers' *description* of it — the anisotropy an artifact of their
  motion along null lines in the **one** χ-direction; the (θ,φ) 2-sphere is the direction
  they are *not* moving through (genuinely isotropic).
- So the CMB projection is the **closed-S³ hyperspherical-harmonic transfer**, NOT the
  flat-sky ℓ≈k·D_C used in r504. At low ℓ they differ qualitatively: a degree-L mode feeds
  ℓ≤L, so the lowest mode L=2 feeds the **quadrupole** — the discreteness sits at ℓ~2–3
  (where the observed deficit is), not a "floor at ℓ≈8."
- r504's "floor located ~10% via the flat projection" was a hasty over-claim on the wrong
  instrument. **Reverted** §5/caption/abstract to honest-open (the pre-r504 text already
  named the right computation). The flat-sky ℓ_2≈8 is an order-level placeholder only.

### CORRECTION (r506) — the "sharp question" was a manufactured tension; P9 §691 settles it
Grounded at P9 source (§691): **D_M, the comoving distance to last scattering, IS the
flat-ΛCDM observable** — a robust ingredient *in hand*, not open. The single open
early-universe parameter is z_onset (in r_s); ℓ_A≈301 is reproduced at the directly-measured
H₀. There is no second distance and **no ℓ_A≈110**.

The "ℓ_A≈110 / D_M=r_0 vs D_C" framing recorded above was a chimera: it conflated two
different lengths doing two different jobs.
- **r_0 ≈ 5065 Mpc** = areal/curvature radius of the layer = the **S³ size** → sets the
  *source* mode quantization k_L = √(L(L+2))/r_0.
- **D_M ≈ 13900 Mpc** = comoving distance to last scattering = the **projection distance to
  the sky** (P9's flat-ΛCDM observable).
Calling r_0 "the angular-diameter distance" crossed them. Their ratio ~2.75 is not a tension;
it is the line-of-sight distance over the curvature radius, as in any large closed universe.
The acoustic sector is exactly where P9 banks it — untouched. (GUARD held, late: the tension
I felt was the model defending an invented flaw.)

### What genuinely remains open (narrow, grounded)
The low-ℓ **C_ℓ shape** via the closed-S³ hyperspherical transfer — a degree-L mode feeds
ℓ≤L — carried through the τ̃=τ+χ non-synchronous geometry, using **D_M = the flat-ΛCDM
observable** (P9 §691) as the projection distance, NOT a new distance. The distance is
settled; the transfer/mode-function shape is the open piece.
