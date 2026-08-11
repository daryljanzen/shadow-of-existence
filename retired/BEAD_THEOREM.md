> **⌖ RETIRED r1550.** This was closing the bead into a theorem, with derivation (r974). **Landed:** `thm:bead` is P7's central theorem (×6) — one closed object on one smooth manifold, the substrate C^∞ across r=0.
> Kept as record; **do not work from it.**


# Closing the bead into a theorem — derivation record (r974, Arthur)

*The mathematical content that promotes `conj:bead` from conjecture to theorem. Receipt: `computations/bead_contour.py` (clean). Stated for reversal.*

## What was already proven (P3, not mine)
The **geometric closure** is a theorem of P3 `SdS-slicing-curve_v2.tex` §sec:seam + §sec:lap:
- The slicing curve `dr/dl=√|f|`, `f=1−2M/r−r²/α²`, with `r` a **signed** areal radius (`g_θθ=r²` insensitive to sign).
- At the equatorial seam `X=α` the curve is tangent to the throat; the continuation `θ↦π/2+iψ` joins the Riemannian inner piece `r=α sinθ` to the Lorentzian cosmological piece `r=α coshψ` as **one analytic function** (`sin(π/2+iψ)=coshψ`), `C¹` at the seam. Prop `prop:flip`.
- Run inward through the seam and **backward through r=0** (a branch point, not a barrier — the substrate is one smooth `C∞` de Sitter manifold across the locus the chart labels `r=0`), the curve **closes on the backward-radial root**. For the Nariai member the lap runs through `+α/√3, 0, −2α/√3` (fig:conjwave). **"The slicing curve, run forward through the seam and backward through r=0, is one closed object on one manifold."**

So the closed geometric loop, and the two readings (inward = collapse, outward = expansion), are **established geometry**. This is the load-bearing half, and it is P3's.

## What I computed (the cosmic-time contour — the conjecture's stated open core)
The cosmology reads the same signed-r range in **cosmic time** τ̃, via the E=1 master equation
`(dr/dτ̃)² = 1−f = 2M/r + r²/α²`, whose r>0 solution is the flat-ΛCDM law `r=(2Mα²)^{1/3} sinh^{2/3}(3τ̃/2α)`.
Integrating `τ̃(r)=∫ dr/√(2M/r+r²/α²)` (principal complex √) around the full lap, on the **actual Nariai cut** (receipt verifies numerically; `arcsinh` gives it analytically):

| segment | r | τ̃ |
|---|---|---|
| expansion leg | r > 0 | **real** |
| near lap | 0 → −A | **pure imaginary**, \|Im τ̃\| growing 0 → πα/3 |
| turnaround (boing's back) | r = −A ≡ −(2Mα²)^{1/3} = −0.727α | \|Im τ̃\| = **πα/3** exactly (where 1−f=0) |
| collapse leg | r < −A | \|Im τ̃\| **locked at πα/3**, Re τ̃ grows (prior universe's own cosmic time) |

- **r stays real and signed throughout; τ̃ is what goes complex** — exactly `conj:bead`'s framing, now concrete.
- The excursion is **bounded**: `|Im τ̃| ≤ πα/3`. The lock value πα/3 is **A-independent** (a property of the 2/3 exponent: (2/3)(π/2)=π/3), and is **not** the de Sitter thermal period 2πα (6× larger — the earlier "β=2πα pins the contour" claim was noise, retracted r974).
- The previous node's "60° phase = obstruction" was a **misread**: the π/3 is the finite imaginary displacement of cosmic time, not a phase of r and not a pathology.

## The one real subtlety (nailed, not a contradiction)
The slicing curve (`dr/dl=√|f|`) turns at the **horizons** (f=0: α/√3, −2α/√3); the cosmic-time reading (`dr/dτ̃=√(1−f)`) turns at the **comoving turnaround** (1−f=0: r=−A). They turn at different r **because they are different parametrizations of the same geometry** — expected, not a conflict. Consequently the **geometry closes** (the loop, P3) while the **cosmic-time reading is open** (two infinite legs joined through the imaginary boing — each universe carries its own infinite cosmic time). The theorem must state both precisely: *closed as geometry, read as the boing in cosmic time.*

## Status: no obstruction — the theorem holds.
- Geometric closure: P3 theorem. ✓
- Cosmic-time contour: computed + analytically characterized, bounded, r real. ✓ (receipt clean)
- Only genuinely-open item: whether the **spacetime** (not merely the slicing curve) extends through r=0 — a **P2 scope caveat**, explicitly left open there, **not** a conjecture-blocker.

**⇒ `conj:bead` is promotable to a theorem** (geometric closure + the cosmic-time boing contour), with the spacetime-extension as a stated scope caveat rather than an open conjecture item.

## Remaining to actually close it in the corpus
1. Draft the precise **theorem statement** for P7 (recast `conj:bead` → `thm:bead`): the closed slicing curve (P3) + the bounded cosmic-time contour (this receipt), two readings, r real, spacetime-extension the scope caveat.
2. Then the **deep baking** — weave the closed bead into every paper in its own voice, each telling its own tale, every paper citing P7.
3. Then graph.
