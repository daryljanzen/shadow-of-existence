---
kind: PREDICTION
row: PO-91
revision: r7489+cc66.1
---

# `PO-91` — does the de Sitter substrate's own invariants display the tidal discriminant?

*Written before `substrate.py` exists. Nothing below is a result. The scoring is in `WALK.md`
and the receipt, against these numbers and bands and not against a reconstruction of them.*

## The order, and the one thing it asks

`r7489` ①: **compute whether the de Sitter substrate's own invariants display that tidal
discriminant** — whether the substrate, read on its own, tells the two critical points apart as
the falling observer of `r7463` ⒟ does.

- **If it does not:** the asymmetry predicts something about observation the symmetric substrate
  alone does not display, and `PO-91` discharges on its first exit.
- **If it does:** say what the substrate's invariant is, and the row becomes a statement of which
  object carries the discriminant.

The discriminant to be matched is `r7463` ⒟'s, on the swept chart: the orthonormal components
$R_{\hat t\hat r\hat t\hat r}=-2M/r^{3}$ and $R_{\hat t\hat\theta\hat t\hat\theta}=M/r^{3}$, both
**independent of the infall rapidity** $w$, reading $-1/4M^{2}$ and $+1/8M^{2}$ at $z=0$ ($r=2M$)
against $\mp\infty$ at $z=\pi$ ($r=0$).

## ⚠ The source question first, and it partly answers the order

**`P3` §`sweep` already says the substrate does not distinguish them, in ink:** *"The substrate is
maximally symmetric, everywhere finite and smooth, and `r=0` is a regular point of it — a point
**on** the throat circle, at $X_{1}=-\alpha$"*; the two critical points are *"topologically
identical on the substrate"*, *"emphatically **not** metrically identical"* on the swept geometry,
and the lopsidedness is *"a feature of the vantage-dependent description, not of the substrate."*

**So this file is not permitted to report that as its own discovery.** What `P3` asserts is the
substrate's regularity and the topological identity; what it does **not** do anywhere is compute
the substrate's own curvature invariants, or a falling observer's tidal tensor **on the substrate**,
at the two loci, and show they fail to separate them. That computation is this file's, and the
verdict it licenses is a confirmation of `P3`'s claim at the one quantity the row turns on — not a
new fact about the substrate.

## ⚠ And `P3` §`sweep` bounds the attribution half in advance

Its own two questions, with different answers, and both are its results and not mine:

1. *Does the inverse-cube term track the **selected** off-axis point?* **No — settled by
   computation.** Three offsets ($r_{0}=-1.125419,\ 0.338936,\ 0.786483$ at $2M=0.30$) return one
   $K_{G}$, because $K_{G}=-f'(r)/2r$ and $f$ carries the mass and the throat scale and nothing else.
2. *Does it track the cut's being off-axis **at all**?* **Undecidable, provably so** — since
   $2M=r_{0}-r_{0}^{3}$, mass and offset vanish together, so no configuration has an off-axis cut at
   zero mass or an on-axis cut at non-zero mass.

⇒ **This file may not claim the discriminant is "the pivot's".** The most it may say about
attribution is what `P3` licenses: the term is the reflection-odd part of the slice's own curvature,
blind to which root the cut sits on, vanishing exactly when the cut sits on the axis.

## What will be computed, and in what order

⒜ **The substrate's Riemann tensor, from the metric and not quoted.** De Sitter at scale $\alpha$,
in static coordinates, symbolically, at **general dimension $D$** rather than only $D=4$ — because
`P3` §`slicing` says the substrate proper is $\mathrm{dS}_{5}=SO(5,1)/SO(4,1)$ and that it *"works
the equatorial section throughout"*, so a result that held only at the section's dimension would
not be the substrate's.

⒝ **Every local polynomial curvature invariant that is cheap:** $R$, $R_{\mu\nu}R^{\mu\nu}$, the
Kretschmann $K$, and the Weyl square. Each evaluated as a function of position.

⒞ **The falling observer's tidal tensor on the substrate**, built the same way `r7463` built it:
an orthonormal frame, a radial boost of rapidity $w$, every component transformed and simplified —
not asserted from a symmetry property.

⒟ **The two loci.** Evaluated at the substrate counterparts of the two critical points, and —
because an evaluation at two points cannot establish an absence (a sampled answer to an algebraic
question is this corpus's own named error) — **the position-independence is to be established
symbolically, as an identity in the coordinate, not by agreement at two sampled points.**

⒠ **The cut's side**, for the "which object" half only: $K_{G}=1/\alpha^{2}-M/r^{3}$ at the two
critical points, and that the $M$-term is absent identically at $M=0$. `P3`'s, cited.

## The predictions, at the weight I actually hold them

| # | prediction | my confidence | band |
|---|---|---|---|
| ⒜ | the substrate's Riemann is the constant-curvature form $R_{abcd}=\alpha^{-2}(g_{ac}g_{bd}-g_{ad}g_{bc})$, identically in position, at every $D$ tested | high | holds at $D=4$ and $D=5$; 0 position-dependent components |
| ⒝ | **0 of the 4 invariants depend on position** — each a constant in $\alpha$ and $D$ | high | 0 of 4; band 0–1 |
| ⒞ | the falling observer's tidal tensor on the substrate is **isotropic, $w$-independent and position-independent** | medium-high | 0 discriminating components of the 4 `r7463` measured; band 0–2 |
| ⒟ | **⇒ the substrate does not display the discriminant**, so the row discharges on its **first** exit | medium-high | — |
| ⒠ | the discriminating term sits on the cut: $K_{G}$ finite at $r=2M$, divergent at $r=0$, and the $M$-term identically absent at $M=0$ | high | — |

⌗ **Where I am least sure, named now rather than after:** ⒞. I expect isotropy to make the boost
act trivially, but `r7463`'s own $w$-independence came out of transforming every component and was
**not** what its price predicted, so the same price here is worth no more than the band. And I am
*not* confident I can rule out a substrate quantity that distinguishes the loci **non-locally** —
a curve-relative or embedding-relative quantity. **That is a scope limit, not a result**, and ⒟ will
be stated over local invariants only, with the quantifier written out.

⚠ **What would falsify ⒟:** any substrate-local invariant, or any frame component of the substrate's
own tidal tensor, that takes different values at the two loci. One such quantity and the row takes
the order's **second** exit instead, and the verdict inverts.

## The control, and what it is for

An instrument that returns *"does not distinguish"* is worthless until it is shown it **can** return
*"distinguishes"*. Three controls, and a failure of any one voids the run rather than being noted:

1. **The swept SdS chart, $M\neq0$**, through the same frame machinery: must return
   **distinguishes**, reproducing `r7463`'s $-2M/r^{3}$ against a finite value at $r=2M$. If the
   machinery cannot see the discriminant that is known to be there, its silence on the substrate
   measures the machinery and not the substrate.
2. **A position-dependent scalar on the substrate itself** (the areal radius): must come back
   **position-dependent**, so that "constant" is a finding about the invariants and not about the
   evaluator.
3. **A metric that is not maximally symmetric**, handed to the invariant comparator: must return
   **distinguishes**, so that constancy is not what the comparator says about everything.

## Scope, stated before the fact

- **`P2` and `P3` are not edited.** `r7489` ② — the paper text is the chat seat's.
- The verdict's quantifier is **local polynomial curvature invariants of the substrate, and the
  orthonormal tidal components of its own Riemann tensor in a radially boosted frame**. Nothing is
  claimed over non-local or curve-relative quantities, and the claim will say so in those words.
- No attribution of the discriminant to the pivot, per `P3` §`sweep`'s own undecidability above.
