---
kind: WALK
row: PO-91
revision: r7489+cc66.2
---

# `PO-91` — the substrate does not display the discriminant, and the whole of it sits in one term

*Everything numeric below is printed by `substrate.py` in this directory, whose output is
`substrate_out.txt`: 36 checks, 0 failures. The Christoffels, the Riemann tensor, the four
invariants and every orthonormal-frame component are built from the metrics written in that file,
so a reader who distrusts a number can distrust the metric instead. No curvature result is quoted.*

## The question, and what was already the corpus's before I started

`r7489` ①: do the de Sitter substrate's own invariants display the `r7463` ⒟ tidal discriminant?

⚠ **`P3` §`sweep` already answers the structural question in ink, and the honest source check found
it before this file was written** — recorded in `PREDICTION.md` before any computation existed, so
it cannot be reported here as a finding: *"The substrate is maximally symmetric, everywhere finite
and smooth, and `r=0` is a regular point of it — a point **on** the throat circle, at
$X_{1}=-\alpha$"*; the two critical points are *"topologically identical on the substrate"* and the
lopsidedness is *"a feature of the vantage-dependent description, not of the substrate."*

**What `P3` nowhere does is compute it at the quantity the row turns on.** This file computes the
substrate's own invariants and a falling observer's tidal tensor **on the substrate**, and that is
all it claims: a confirmation of `P3`'s claim at the row's own quantity, plus one decomposition
that is this file's.

## ⒜ The substrate's Riemann is the constant-curvature form, at both dimensions

Built from the metric at $D=4$ and $D=5$ — because `P3` §`slicing` makes the substrate proper
$\mathrm{dS}_{5}=SO(5,1)/SO(4,1)$ while the paper *"works the equatorial section throughout"*, so a
statement true only at the section's dimension would not be the substrate's:

$$R_{abcd}=\frac{1}{\alpha^{2}}\left(g_{ac}g_{bd}-g_{ad}g_{bc}\right),$$

**0 deviations in all 256 components at $D=4$ and all 625 at $D=5$.**

⛔ **This check failed first, on exactly one component of each, and the failure was mine and not the
geometry's.** $R_{r\varphi\varphi\theta}$ came back as
$r(\sin 2\theta\tan\theta+\cos 2\theta-1)/(2\tan\theta)$, whose numerator is identically zero by
hand ($\sin2\theta\tan\theta=2\sin^{2}\theta$, $\cos2\theta-1=-2\sin^{2}\theta$) and which sympy's
`simplify` would not normalise against the double angle. **The repair is a stronger exact
normalisation, not a loosened check and not a whitelisted component** — the note sits at the
function that caused it, and every step in it is an exact rewrite, so it can only find zeros that
are there. *Had the verdict been written before the output was read, this is the line that would
have been glossed.*

## ⒝ Every local scalar invariant is one constant, as an identity and not a sample

| | $D=4$ | $D=5$ |
|---|---|---|
| $R$ | $12/\alpha^{2}$ | $20/\alpha^{2}$ |
| $R_{\mu\nu}R^{\mu\nu}$ | $36/\alpha^{4}$ | $80/\alpha^{4}$ |
| Kretschmann $K$ | $24/\alpha^{4}$ | $40/\alpha^{4}$ |
| Weyl$^{2}$ | $0$ | $0$ |

⇒ **0 of 4 depend on position**, each derivative taken with respect to **every** coordinate and
identically zero. *The absence is established as an identity in the coordinates, never by agreement
at two sampled points — a sampled answer to an algebraic question is this corpus's own named error,
and sampling cannot prove an absence at all.*

## ⒞ The falling observer's tidal tensor on the substrate

Same machinery as `r7463`, legs written out rather than inlined because the swapped-leg bug that
file caught is invisible in $R_{\hat t\hat r\hat t\hat r}$ and shows only in the siblings:

$$R_{\hat t\hat r\hat t\hat r}=-\frac{1}{\alpha^{2}},\qquad
  R_{\hat t\hat a\hat t\hat a}=-\frac{1}{\alpha^{2}},\qquad
  R_{\hat r\hat a\hat r\hat a}=+\frac{1}{\alpha^{2}},$$

identical at $D=4$ and $D=5$, **rapidity-independent, position-independent, and isotropic**
($R_{\hat t\hat r\hat t\hat r}=R_{\hat t\hat a\hat t\hat a}$, so no direction is picked out). Every
component was transformed through the boost and simplified; nothing is asserted from a symmetry
property of the metric.

## ⇒ ⒟ THE ANSWER: the substrate does not display it, so the row takes the FIRST exit

No local polynomial curvature invariant of the substrate, and no orthonormal tidal component of its
own Riemann tensor in a radially boosted frame, takes different values at the two critical points —
**because each is one constant over the whole manifold, so no pair of points whatever is separated
by one**, these two included and wherever they sit. ⇒ `PO-91` **discharges on the order's first
exit**: the asymmetry is observationally real and the symmetric substrate alone does not display it.

## ⛭ And the whole discriminating content is one term — computed, not asserted

The control run hands the same frame machinery the swept SdS chart, and its two components come
back as the substrate's own constant **plus** a term carrying $M$ and nothing else:

$$R_{\hat t\hat r\hat t\hat r}\Big|_{\rm swept}=\underbrace{-\frac{1}{\alpha^{2}}}_{\text{the substrate's, }⒞}-\frac{2M}{r^{3}},
\qquad
R_{\hat t\hat\theta\hat t\hat\theta}\Big|_{\rm swept}=\underbrace{-\frac{1}{\alpha^{2}}}_{\text{the substrate's, }⒞}+\frac{M}{r^{3}}.$$

Since the substrate's part is the *same* constant at both critical points, **the entire difference
between them is the $M/r^{3}$ term.** ⌗ *Scope, exactly: this is an identity between these two frame
components in these coordinates, verified symbolically. It is **not** promoted to a general
decomposition of the swept geometry's curvature into substrate and cut — that is the operator
paper's object, not this file's.*

The cut's side carries the same term as `P3`'s own $K_{G}=-f'(r)/2r=1/\alpha^{2}-M/r^{3}$, confirmed
identically here rather than quoted: **finite** at the horizon critical point,
$K_{G}(2M)=1/\alpha^{2}-1/8M^{2}$; **divergent**, $-\infty$, at $r=0$; and the $M$-term **absent
identically** at $M=0$, where $K_{G}$ reduces to the substrate's own $1/\alpha^{2}$.

⚠ **No attribution beyond that is claimed, and the bound is `P3`'s own.** §`sweep` settles by
computation that the term does **not** track the *selected* off-axis point — three offsets
($r_{0}=-1.125419,\,0.338936,\,0.786483$ at $2M=0.30$) return one $K_{G}$ — and proves that whether
it tracks the cut's being off-axis **at all** is *undecidable*, since $2M=r_{0}-r_{0}^{3}$ makes mass
and offset vanish together. **So this file does not say the discriminant is "the pivot's."**

## The controls, and they are what license the silence

| control | required | returned |
|---|---|---|
| ① the swept SdS chart through the **same** machinery | must **distinguish** | $-2M/r^{3}-1/\alpha^{2}$, position-dependent, $\dd/\dd r=6M/r^{4}$; and the $\alpha\to\infty$ limit reproduces `r7463` **exactly**, $-2M/r^{3}$ and $+M/r^{3}$ |
| ② a position-dependent quantity on the substrate | must read as position-dependent | it does ⌗ *weak by construction, and named so in the pre-registration; ① and ③ carry the load* |
| ③ a non-maximally-symmetric metric, and the Weyl machinery | must **distinguish**, and Weyl must be **validated against a known non-zero** | Schwarzschild: Kretschmann $=48M^{2}/r^{6}$, and Weyl$^{2}=48M^{2}/r^{6}=K$ on a Ricci-flat metric — **so the vanishing Weyl on the substrate cannot be a sign error in the decomposition** |

⇒ The instrument is shown able to return *distinguishes*, on the very discriminant in question. Its
silence on the substrate therefore measures the substrate and not the instrument.

## Scoring against the pre-registration

| # | priced | measured | verdict |
|---|---|---|---|
| ⒜ | constant-curvature form, 0 position-dependent components, at $D=4$ and $5$ | 0 deviations of 256 and of 625 | **held** |
| ⒝ | 0 of 4 invariants position-dependent, band 0–1 | **0 of 4** | **held, central value** |
| ⒞ | isotropic, $w$- and position-independent; 0 discriminating components, band 0–2 | **0**, and isotropic | **held, central value** |
| ⒟ | the first exit | the first exit | **held** |
| ⒠ | $K_{G}$ finite at $r=2M$, divergent at $0$, $M$-term identically absent at $M=0$ | all three | **held** |

⌗ **Where I said I was least sure, ⒞, the prediction held** — and the reason it held is the one I
named: isotropy makes the boost act trivially. *That is one price coming in right after `r7463`'s
⒟ came in wrong, and it is worth no more than that: the band was 0–2 and the measurement sat at an
end of it.* ⛔ **And the scope limit I pre-registered stands and is not quietly dropped:** the
verdict is over **local** polynomial curvature invariants and the boosted-frame tidal components.
A quantity distinguishing the two loci **non-locally** — curve-relative or embedding-relative — is
not ruled out here and is not claimed either way.

## The row after this revision

- **Discharged, on the order's first exit.** The substrate read on its own does not display the
  discriminant, at the row's own quantity and at both relevant dimensions.
- **Settled, and this file's own:** the entire difference between the two critical points, in the
  measured frame components, is the $M/r^{3}$ term; the substrate contributes the same constant to
  both.
- **Confirmed, and `P3`'s:** $K_{G}$'s two terms are the substrate's $1/\alpha^{2}$ and the cut's
  $-M/r^{3}$, the second absent identically at $M=0$.
- **Not claimed:** that the discriminant is the pivot's (`P3` proves that undecidable); any general
  substrate-plus-cut decomposition of the swept curvature; and anything over non-local invariants.
- **At weight:** this closes a structural question the row posed. It is not a new observable — that
  tidal forces diverge where the sweep pivots and stay finite at the horizon is the standard
  reading, and the corpus already reads the divergence as the sweep's shadow. The result is that
  the substrate's own invariants are now *measured* to be silent on it, not assumed to be.
