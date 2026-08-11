# Bundle r970 — the P7 grand synthesis figure (fig:dS_SdS, rebuilt)

r970 replaces P7's co-opted BST reassignment diagram with a purpose-built **2×2 synthesis plate** that
delivers the causal reassignment *without flattening the big bang* — the thing the old figure structurally
could not do (its hyperboloid and τ–χ inset both drew the bang as an edge, not the branch point the single
closed lap passes through).

## The figure (corpus/dS-SdS-synthesis.pdf; receipt corpus/synthesis_figure.py)

Vector, 97 KB, four panels, one continuous story; red = timelike/expansion/fundamental, blue = null/collapse/photon.

- **(A) Causal reassignment on the dS₄ hyperboloid** (a symmetry-breaking cut of the dS₅ = SO(5,1)/SO(4,1)
  substrate). The future-directed null **rulings (red)** → the timelike fundamental worldlines (areal radius
  reads sinh^{2/3} along a reassigned ruling); the **at-rest comoving worldlines (blue)**, timelike on the
  expanding S³ leaves (R=α cosh(T/α)), → the null photon congruence. The two congruences trade causal
  character; the waist S³ is the comoving sphere. *(Correctness note: an earlier draft drew the blue family
  as a second ruling — wrong; cross-checking §L532 vs §L722 fixed it to the cosh meridian worldlines.)*
- **(B) The lap** — one analytic r(τ̃) in (τ̃, Re r, Im r), from τ̃=−∞ on the conjugate prior-collapse branch
  (phase 2π/3), through the branch point at τ̃=0 where r→0 (finite-curvature Nariai degenerate horizon, **not**
  the singularity), onto the real sinh^{2/3} expansion. Forcing r real (dashed) manufactures the fake cusp.
- **(C) Why Nariai** — the horizon trichotomy on f(r)=1−2M/r−r²/α²: transverse (two horizons) / tangent
  (merged double root, Nariai) / none. A collapse forms a horizon and the limiting orientation is tangent,
  so Nariai is forced, fixed by Λ alone. (Double root at r=1/√3, 2M_N=2/(3√3) — verified.)
- **(D) The layered handoff at the seam** — inward the leaf's local rate governs (radiation gravitates);
  outward the foliation stacking rate governs (radiation-free sinh^{2/3}). The handover deposits ρ_r/ρ_m≈2
  (acoustic scale) and η (composition); infall heats above the deuterium bottleneck, the cooling leg runs
  standard BBN.

## Wired into P7

CR_framework's `fig:dS_SdS` now `\includegraphics{dS-SdS-synthesis.pdf}` at `\textwidth`, with a new
four-part caption. The old BST `dS-SdS.png` (shrunk to 1000px this session) stays archived in
`resources/PhD_thesis/`. P7 recompiles clean (37 pp, 0 undefined). No citation changes (caption is prose).

## Also carried (this session's prior work)

- r969: external references pass (~60 verified citations; every strong flag closed; zero undefined corpus-wide).
- r968: P-symbol canon (R=mass-reflection/γ⁵, P=spatial parity, T=time); coherence cleanup (P9 Type-D ratio,
  p0 L630, the P7 dependency matrix + figure refresh).

## State

All 17 papers compile clean. The bundle excludes only the regenerable compiled *paper* PDFs and LaTeX build
cruft; every figure (including the new synthesis PDF and its receipt) is present, so the corpus compiles
as shipped. See BUNDLE_README.md.
