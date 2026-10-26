# `r7613+cc66` — the spectral-triple route, priced before a line of it is computed

`r7613` assigns the fourth route of `B59`'s enumeration: **can a real spectral triple
$(\mathcal A,\mathcal H,D,J,\gamma)$ be assembled from pieces the corpus already carries, with
$\mathcal A$ acting on $\mathcal H$ — and if so, do the inner fluctuations $A=\sum a[D,b]$ define a
connection whose curvature does not vanish identically?**

This file is committed **before** any computation of mine exists, as `r7611`'s was, so nothing below
can later be reported as a result.

---

## ⓵ The source question, run against the RECEIPTS and not only the papers

`L-276`'s rule, which paid twice in `PO-95` and again in `r7611`. **Every row here is somebody
else's and is recorded so it cannot be reported as mine.**

| source | what it already establishes |
|---|---|
| `L221`/`B61` | ⛭ **the grading axiom is already SATISFIED and that is not a CR fact**: $\gamma^2=1$ and $\gamma D=-D\gamma$ verified for $\gamma^5$ against every $\gamma^\mu$. *What CR supplies is that $R=\gamma^5$ is **derived** (`r2779`) rather than posited — the corpus's own chirality operator **is** the grading a spectral triple requires.* |
| `L221`/`B61` | the index obstruction's **load-bearing hypotheses are compactness and a continuous isometry**, and the spectral route meets neither — inner fluctuations come from the **algebra**, using no isometry. So the obstruction is stated against isometry routes and this is not one; the paper's own "known escapes" clause **does not classify** it, because it never considered it. ⇒ *a gap in coverage, not a hole in the argument* |
| `L221`/`B61` | ⛔ **and B61 names exactly what is untested: the real structure $J$ and the order-one condition $[[D,a],Jb^*J^{-1}]=0$ — "either can kill it".** B61 explicitly does **not** claim the route works. |
| `L221`/`B59` | the routes are **enumerated**, three of five closed, and the spectral route is **named only as unexamined and taken nowhere**; $M_3(\mathbb C)$ is available as a **Wedderburn factor of the order-27 holonomy group algebra** |
| `P14` sec:chirality | the three wall monodromies with the hinge 3-cycle generate a **finite group of order 81 in $U(3)$**, determinant-one part **$\Delta(27)$, lying in $SU(3)$** |
| `P14` sec:count | the three wall modes are **the kernel of ONE Dirac operator**, of one chirality: $\dim\ker_+=3$, $\dim\ker_-=0$, the count a $\gamma^5$-graded index |
| `P14` / `P14_leaf_compactness` | **the leaf is COMPACT** — finite total length in its proper measure, horizon turning points at finite proper distance, the $r=0$ crossing an integrable $\sqrt{\;}$-singularity — **so the Dirac operator on it carries a finite analytical index $\dim\ker$**, exactly where the bulk index on the tortoise measure is obstructed |
| `P13` §face-status | the face is **obstructed twice**: $\su(3)$ admits no equivariant map down to the cosmological three-sphere; and **the round five-sphere carries a full tower but NO Dirac zero modes at all**, so there is no massless content for it to act on. The face is **not** an internal space attached to a spacetime — *"it is the same manifold on its other real form, so a field there is related to one on the Lorentzian substrate by **continuation**, not by reduction"* |
| `r7611+cc66` (mine, already landed) | $E=\pi_*(\text{mode bundle})$ is **flat**, and $H^1(G,\su(3))=0$ on the order-27 group — so the bulk object has no local degree of freedom |

⇒ **AND ONE MEASURED ABSENCE, which is the reason this row is not a literature review.** The corpus
carries **no Connes real structure and no KO-dimension**: every occurrence of "real structure" in
`corpus/*.tex` is about **real roots or real forms** (`P14` sec on the centraliser, `groupoid_paper`
on the root labelling, `geometric_core_paper`), and "order-one condition" occurs in no paper at all.
*So $J$ and the order-one condition are not merely untested, as `B61` says — there is nothing in the
corpus to test. Whatever I write about them is mine and is the row's exposure.*

---

## ⓶ The five axioms against what the corpus supplies

| axiom | supplied? | by what, and over what locus |
|---|---|---|
| $\gamma$ (grading) | **yes** | `B61`: $\gamma^5$, verified, and **derived** in CR rather than posited |
| $\mathcal H$ (Hilbert space) | **yes, over the LEAF** | `P14`: the leaf is compact of finite length; $L^2$ of its spinors, with the **wall kernel** $(\dim\ker_+,\dim\ker_-)=(3,0)$ as a finite-dimensional subspace |
| $D$ (Dirac operator) | **yes, over the LEAF** | `P14`: the Dirac operator on the compact leaf, finite analytical index |
| $\mathcal A$ (algebra) | **the finite part, yes** | $M_3(\mathbb C)$, a Wedderburn factor of the order-27 group algebra (`B59`); $\Delta(27)\subset SU(3)$ (`P14`) |
| $J$ (real structure) | ⛔ **NO — absent from the corpus** | measured above: nothing to inherit, and `B61` says it can kill the route |

---

## ⓷ TWO FORKS, and the second one is not in the order

**⒜ The order's own fork, stated in it and accepted here.** *"A finite algebra alone fluctuates $D$
into scalar fields and not a gauge field; a gauge field needs the algebra's continuous part over the
face, $C^\infty(\text{face})\otimes M_3(\mathbb C)$."* So whether that tensor product is available,
and whether it satisfies the order-one condition, is part of the question.

⛭ **⒝ AND A SECOND FORK THE SOURCE QUESTION TURNED UP: THE PIECES THE CORPUS CARRIES AND THE LOCUS
THE BAR DEMANDS ARE DIFFERENT OBJECTS.** `P14`'s $\mathcal H$ and $D$ are over the **leaf** — a
compact *one*-dimensional domain inside the Lorentzian substrate. The bar `r7611` fixed, and which
this row inherits unchanged, asks for a curvature **on the compact face or on $E=\pi_*(\text{mode
bundle})$**. ⇒ *A triple assembled from `P14`'s pieces is a triple over the leaf, and its inner
fluctuations are a field on the leaf.* Whether that reaches the face is not a detail of the
construction, it is whether the construction answers the question asked. And `P13` §face-status says
the face **carries no Dirac zero modes at all**, so the obvious repair — build the triple over the
face instead — is where the corpus states an obstruction rather than supplies a piece.

⚠ **AND THE TRAP IN ⒝, NAMED NOW SO I CANNOT WALK INTO IT LATER.** The $(3,0)$ chirality imbalance is
a property of **$\ker D$**, not of $\mathcal H$. On the full $L^2$ of the leaf's spinors the grading
is balanced and the imbalance argument does not apply. *Which object the label is about has to be
established before the identity is treated as an obstruction* — my own guard, and this is exactly
where it bites. So the imbalance is a candidate obstruction **only** on the reading where
$\mathcal H=\ker D$, and that reading has to be earned, not assumed.

---

## ⓸ The questions, and what would rule each IN or OUT — fixed before computing

| # | question | ruled the route IN by | ruled the route OUT by | confidence it closes | band |
|---|---|---|---|---|---|
| ⑴ | is there a real structure $J$ on $\mathcal H$ at all? | an explicit antilinear $J$ with $J^2=\pm1$ satisfying the axioms of **some** admissible KO-dimension, exhibited on the corpus's own $\mathcal H$ | the axiom set the construction needs forcing $J\gamma=-\gamma J$ — i.e. $J$ exchanging the $\gamma$-eigenspaces — while the space it must land on is trivial **on the reading where $\mathcal H=\ker D$** | **medium** it closes here | — |
| ⑵ | is $C^\infty\otimes M_3(\mathbb C)$ available, and over **which** locus? | the continuous part existing over the **face** or over $E$, with $\mathcal A$ acting on an $\mathcal H$ there | the continuous part existing only over the **leaf**, so the fluctuation's curvature lives on a locus the bar excludes | **medium-high** it closes here | — |
| ⑶ | does the order-one condition hold? | $[[D,a],Jb^*J^{-1}]=0$ verified on the assembled triple | an explicit pair $a,b$ violating it | **low-medium** it closes here | — |
| ⑷ | if a triple assembles: do the inner fluctuations have non-vanishing curvature? | $F\neq0$ identically, computed, from data the corpus has and not from an isometry | $F\equiv0$, or the fluctuation being a scalar/Higgs-like field with no two-form to carry | **medium** it closes here | — |

**Overall: I price the route at ~0–1 of 4 questions answered in its favour**, i.e. more likely closed
than open, as `r7611`'s three were.

⌗ **WHERE I AM LEAST SURE, AND IT IS A PREDICTION THAT CAN BE WRONG IN A NAMED WAY.** `B61` priced
the risk as **$J$ or the order-one condition** — *"either can kill it"*. **I price it differently: I
expect the route to close on ⑵, the LOCUS, before $J$ is ever reached**, because the corpus's
$\mathcal H$ and $D$ are the leaf's and the bar is the face's. *If $J$ turns out to be the killer and
the locus is bridgeable, `B61` was right and I was wrong, and I will say so in those words rather
than reporting a closure as if I had predicted its reason.*

---

## ⓹ The controls, and what each is for

1. **A positive control on the triple-assembly test itself.** Run the axiom checks on a triple
   **known** to satisfy them — the canonical commutative triple on a circle, $(C^\infty(S^1),
   L^2(S^1),-i\dd/\dd\theta)$ with its standard $J$ — so a verdict of "an axiom fails" is a finding
   about the corpus's pieces and not about my checker. *If the checker cannot certify a triple that
   is one, its refusals measure the checker.*
2. **A negative control on the fluctuation test.** On a **finite** algebra with no continuous part,
   the inner fluctuations must come back as a **scalar** with no two-form — which is the order's own
   stated fork, so the test must be able to see the distinction it turns on.
3. **A positive control on the curvature test**, inherited from `r7611` and re-run here rather than
   quoted: the Hopf connection on $S^2$ returning $c_1=1$, so a verdict of "flat" is about the
   candidate.
4. **An order-one control**: a pair known to violate the condition must be reported as violating it.
5. **The grading re-derived, not quoted**: $\gamma^2=1$ and $\gamma D=-D\gamma$ recomputed here, so
   `B61`'s row is checked rather than inherited.

---

## ⓺ Outcomes, pre-registered, mapped onto the order's three

1. **A non-vanishing curvature** → the gauge half's test is met on this route. I will state
   explicitly whether a **coupling** follows, since `B59` warns that is `PO-5`'s and a connection
   without a dimensionless kinetic coefficient is **half** the named test.
2. **A piece the construction cannot supply** → the route is closed and the composite route is the
   one left. I name **which** piece and over which locus, and whether the closure is `B61`'s
   predicted reason or mine.
3. **The fluctuations come out flat** → closed on a computed reason, as `r7611`'s three were.
4. **If the examination shows `B59`'s or `B61`'s own statements are incomplete or wrong** → that is
   larger than this row and is **routed**, not claimed.

---

## ⓻ Scope, and one constraint I found rather than was given

**No paper is edited**: `P13`, `P14`, `P18` are untouched and the register row is 69's. Instruments
stay frozen per `r7577`, which `r7613` does not lift. `PO-5` is not this row: a connection is not a
coupling. Nothing from `L221`, `B59`, `B61`, `P13` or `P14` is reported as mine.

⛔ **AND A CONSTRAINT ON HOW THIS MAY LAND, which `r7613` put into `B59` and did not say to me.**
`B59` now reds if **any** `corpus/*.tex` contains `Connes` or `inner fluctuation`, or any sentence
containing "spectral triple" that does not also say it is unexamined. *So the words this row's
result is about cannot enter a paper without `B59` going red* — which is correct of `B59` while the
route is unexamined, and becomes 69's to amend if this row examines it. My own prose therefore goes
to the receipt and to `appendix_receipts_*` only, which `B59` skips by name, and never to a paper.
