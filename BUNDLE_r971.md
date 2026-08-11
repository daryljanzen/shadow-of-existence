# Bundle r971 — the P7 synthesis figure, corrected and completed (2×3)

r971 supersedes r970's synthesis figure. r970 delivered the figure but got the reassignment physics
wrong/incomplete in two ways caught in review; r971 fixes both and restructures to the layout that
actually carries the whole tale.

## The correction (the important part)

The causal reassignment is **not** a map between two null bundles — it is a **permutation of causal
character across four structures**, and it reassigns *space* as a corollary (P15 §L174: "the synchronous
space *is* the second ruling"; the τ–χ derivation §L134/§L258–260). The r970 figure drew only one ruling
and showed the swap nowhere. Corrected four-fold picture, now in the figure:

| structure (on dS₄) | de Sitter | → reassigned | in (τ,χ) |
|---|---|---|---|
| null ruling A (red) | null | timelike fundamental worldlines (sinh^{2/3}) | vertical, constant χ |
| null ruling B (green) | null | flat Euclidean synchronous space | horizontal, constant τ |
| at-rest cosh worldlines (blue) | timelike | null photon congruence | the null cone |
| the S³ spheres (purple) | spacelike | spacelike (cosmological layers) | diagonal, constant τ̃=τ+χ |

Two null bundles go timelike and spacelike; the timelike bundle goes null; the universe stays space in both.

## The figure (corpus/dS-SdS-synthesis.pdf; receipt corpus/synthesis_figure.py)

2×3 vector plate, figure-wide colour key (red=fundamental/timelike, green=flat space, blue=null/photon,
purple=S³ layers; grey neutral):
- **(a)** dS₄ hyperboloid — all four structures in their de Sitter character.
- **(b)** the reassigned (τ,χ) frame — the same four after the character swap (both representations
  together are what make the swap legible; this restores what the old two-panel figure's τ–χ inset carried
  and r970 dropped).
- **(c)** the lap — one analytic r(τ̃) through the branch-point seam, τ̃ from −∞.
- **(d)** why Nariai — the horizon trichotomy (double root at r=1/√3, 2M_N=2/(3√3), verified).
- **(e)** the layered handoff — leaf-rate inward / stacking-rate outward, ρ_r/ρ_m and η deposited, BBN on
  the cooling leg.
- **(f)** one Λ, two slicings — flat Euclidean constant-τ slices (Ω_k=0 distances) vs closed S³ constant-τ̃
  layers (curvature); the spatial reassignment at the observational rung.

## Wired into P7

CR_framework's `fig:dS_SdS` at `\textwidth` with a six-part caption spelling out the four-fold swap.
P7 recompiles clean (37 pp, 0 undefined). All 17 papers compile clean.

## Prior work carried

r970 (figure v1), r969 (external references pass), r968 (P-symbol canon + coherence cleanup). See those
changelogs. Bundle excludes only regenerable compiled *paper* PDFs and LaTeX build cruft; all figures
(incl. the synthesis PDF + receipt) are present, so the corpus compiles as shipped.
