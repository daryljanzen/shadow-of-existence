---
kind: WALK
row: PO-91
revision: r7463+cc66.3
---

# `PO-91` — the vantage-dependence, and the axis that is measured rather than chosen

*Everything numeric below is printed by `vantage.py` in this directory, whose output is
`vantage_out.txt`.  The Riemann tensor, the Kretschmann scalar and the orthonormal-frame
components are built from the metric written in that file; no standard result is quoted,
so a reader who distrusts a number can distrust the metric instead.*

## The row's question, and the premise both its horns share

`P2` §*Construction, not error*: two analytically identical metric singularities are charted
into a sharply asymmetric pair — one passed through smoothly, one ringed with a divergent
curvature invariant — and **"whether that work is purely an artefact of the vantage, or whether
the vantage-dependence itself encodes something physical about how such geometries are observed,
is a question this construction raises and leaves open."**

⛭ **The finding is that neither horn holds, because both presuppose that the vantage is chosen.**
It is not. The one place the asymmetry enters — which critical point the profile is swept about —
is fixed by a measurement, and the measurement is the area of a sphere.

## ⒜ The counterfactual chart does not exist

A sweep is a reduction by an `SO(3)` isometry whose orbits are the swept 2-spheres; its axis is
the locus those orbits degenerate at, so the orbit area must vanish there. The orbit area is

$$A(r) = 4\pi r^2,$$

whose only zero is $r=0$, double. The cycloid profile $r_N(z)=2M\cos^2(z/2)$ has two
non-degenerate critical points, and they sit at

| critical point | chart label | orbit area $A$ | admissible as a sweep axis |
|---|---|---|---|
| $z=0$ | $r=2M$ | $16\pi M^2$ | **no** |
| $z=\pi$ | $r=0$ | $0$ | yes |

⇒ **Chart H — the same profile swept about the other critical point — is not disfavoured but
inadmissible.** There is no second chart, so there is nothing for "purely an artefact of the
vantage" to be an artefact *of*.

⚠ **And the easy form of that argument is wrong, which the file says against itself.** In the
maximal Schwarzschild *manifold* the `SO(3)` action has **no fixed point at all**: on the chart's
own domain $r>0$ the solution set of $A=0$ is empty. The axis is a *boundary* locus the orbits
shrink toward, not a point sitting inside the spacetime — it is `P2`'s **spatial** sweep that has
an axis in the ordinary sense. The criterion survives in the form "the locus the orbit area
degenerates at", and it is still unique; but a reading that calls $r=0$ a fixed point of the
spacetime's isometry group has helped itself to a point the spacetime does not contain.

## ⒞ The asymmetry is invariant, and the invariant is *which sector collapses*

Computed from Killing-vector norms and orbit areas — scalars, so no labelling can move them:

| critical point | $\lvert\xi\rvert^2$ | orbit area | $K$ | collapsing sector |
|---|---|---|---|---|
| $z=0$ ($r=2M$) | $0$ | $16\pi M^2$ | $3/4M^4$ | the stationary generator, in the $(t,r)$ block |
| $z=\pi$ ($r=0$) | diverges | $0$ | $\infty$ | the angular 2-sphere |

⇒ **Different sectors collapse at the two critical points.** The pair is therefore invariantly
distinguishable and the asymmetry is not a labelling. *That is the half of the row that is
settled: it does not terminate as a stated limit, and the frontier's "likely exit on this
corpus's own reading" is the wrong exit.*

## ⒝ The chain-rule story is about a function, not about two charts

Measured both ways:

```
K[r_N](z)  ->  z=0: 3/(4*M**4)      z=pi: oo
K[r_H](z)  ->  z=0: oo              z=pi: 3/(4*M**4)
```

So the divergence does sit wherever the profile's zero sits — but $r_H$ is not a chart of this
spacetime (⒜), so **there is no second spacetime for the swapped answer to be true of.** The
statement is about composing a smooth function with $48M^2/r^6$ and nothing more.

## ⒟ There *is* an observational discriminant, and my own price said there would not be

The quantity an observer measures is the tidal tensor in their own frame. Derived here rather
than assumed: the orthonormal components are

$$R_{\hat t\hat r\hat t\hat r} = -\frac{2M}{r^3},\qquad
  R_{\hat t\hat\theta\hat t\hat\theta} = \frac{M}{r^3},\qquad
  R_{\hat r\hat\theta\hat r\hat\theta} = -\frac{M}{r^3},\qquad
  R_{\hat\theta\hat\varphi\hat\theta\hat\varphi} = \frac{2M}{r^3},$$

and a radial boost of rapidity $w$ leaves the first two **$w$-independent** — computed by
transforming every component and simplifying, not asserted from the type-D property. At the two
critical points:

| critical point | $R_{\hat t\hat r\hat t\hat r}$ | $R_{\hat t\hat\theta\hat t\hat\theta}$ |
|---|---|---|
| $z=0$ ($r=2M$) | $-1/4M^2$ | $+1/8M^2$ |
| $z=\pi$ ($r=0$) | $-\infty$ | $+\infty$ |

⇒ **A worldline tells the two critical points apart by a measurement**, in a frame whose answer
does not depend on how fast it is falling. ⛔ *My pre-registered ⒟ was 0 discriminants with band
0–1; the measurement is 1, so the central value is wrong and only the band holds.*

## ⛔ What is NOT established here, and why the row does not discharge

The row's discharge condition is an account on which the asymmetry predicts something about
observation **that the symmetric substrate alone does not display**. ⒟ supplies the first half.
The second half needs the substrate's own invariants — and that the substrate is the de Sitter
manifold is the corpus's claim (`P3`, the slicing companion), not this file's. **This file computes
the swept chart and nothing else.** A seat closing its own row by computing another paper's object
is the reach this corpus punishes, so that step is routed and not claimed.

## ⇒ The row after this revision

- **Settled:** the asymmetry is not exhausted by the chart (⒞), and the vantage is not free (⒜) —
  so `PO-91` does **not** terminate as an `r7013` kind-2 stated limit.
- **Settled:** an observational discriminant exists between the two critical points (⒟).
- **Open, and now a single computation rather than a question:** whether the substrate's own
  invariants fail to display that discriminant. That is the slicing companion's object.
- **Correction to the row's framing:** both of its horns assume a chosen vantage. The asymmetry is
  **downstream** of a measurement — the 2-sphere area that picks the axis — not upstream of one.
