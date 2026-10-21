# `r7443+71.60` — PROGRAMME: completeness of the TT spectrum of S³, the one statement rows 65 and 66 stop at

*Daryl's instruction in this session, after `r7471`'s list was worked to its end: build the Peter–Weyl-side piece
rather than stand by. This file fixes the route. Each stage is a campaign of its own, registered with a band and a
p before any Lean, as the standing rules require.*

## The target, stated exactly

***T★.*** Let `h` be a smooth, symmetric, traceless, divergence-free 2-tensor field on the unit S³, written in the
left-invariant frame, with `−∇²h = λh`. Then:
- `λ = m² − 3` for some `m ≥ 3`;
- `h` lies in the span of campaign 51's level-`m` eigen-tensors;
- that eigenspace has real dimension exactly `2(m² − 4)`.

Campaign 51 (`probes/S3TTSpectrum.lean`) proved the lower bound: `2(m² − 4)` independent eigen-tensors at every
level. T★ is the matching upper bound, which is completeness.

## The route: not Peter–Weyl in full, only what T★ needs

| stage | campaign | piece | Mathlib it stands on |
|---|---|---|---|
| P1 | 52 | ***Integration on S³.*** The sphere measure `σ` is invariant under the isometries `q ↦ q·exp(t u_a)`. Differentiating at `t = 0` gives `∫ E_a f dσ = 0` for `C¹` functions `f`. Hence integration by parts for the frame derivatives, `∇²` symmetric on tensor fields, and `−∇² ≥ 0` | `Measure.toSphere`, invariance of `volume` under `LinearIsometryEquiv`, differentiation under the integral sign |
| P2 | 53 | ***The polynomial spectrum.*** On the symmetric traceless tensor fields with polynomial components of degree `≤ d` (finite-dimensional, preserved by `∇²`): the eigenvalues of `−∇²` are the values of the two `sl₂` Casimirs; every eigenvector at eigenvalue `λ` has degree bounded by a function of `λ`; and the TT part at `m² − 3` has dimension exactly `2(m² − 4)` | `IsSl2Triple`, finite-dimensional `Module.End` eigenspaces, the harmonic decomposition counted directly |
| P3 | 54 | ***Density.*** Polynomial tensor fields are dense in `C(S³)` and hence in `L²(σ)` | `ContinuousMap.starSubalgebra_topologicalClosure_eq_top_of_separatesPoints` (Stone–Weierstrass), `ContinuousMap.toLp_denseRange` |
| P4 | 55 | ***Assembly.*** Project `h` onto the degree-`≤ d` polynomial tensors in `L²(σ)`. By P1 the projection commutes with `∇²`, so it is a `λ`-eigenvector. By P2 it lies in a fixed finite-dimensional space, independent of `d`. By P3 the projections converge to `h`, so `h` lies in that space: it is polynomial, and P2 counts it | finite-dimensional orthogonal projection, `L²` convergence |

***Why this order.*** P1 is the analytic foundation, and the most likely to expose a real Mathlib limit. P2 is the
largest, and pure algebra. P3 is short. P4 is the theorem.

***What is NOT built, by design:*** Peter–Weyl for compact groups in general, and `L²(SU(2))` as a Hilbert direct
sum of matrix coefficients. T★ needs neither.

***Census on completion:*** rows 65 and 66 → `DONE`, both open halves closed, and the census at `111` DONE.
