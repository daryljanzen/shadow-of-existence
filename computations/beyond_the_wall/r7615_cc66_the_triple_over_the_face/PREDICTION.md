# `r7615+cc66` — the almost-commutative triple over the face, priced before a line of it exists

`r7615` assigns the fifth and last structural route: build $(\mathcal A,\mathcal H,D,J,\gamma)$ with
$\mathcal A=C^\infty(\text{face})\otimes M_3(\mathbb C)$, $\mathcal H=\text{spinors}\otimes\mathbb C^3$,
$D=D_{\text{face}}\otimes1$, and answer ⑴ whether $J$, the order-one condition and the first-order
inner fluctuations hold, and ⑵ **the real test** — whether the construction fixes either the
fluctuation or the coupling, given that the spectral action's Yang–Mills coefficient carries a free
moment of the cutoff function.

Committed **before** any computation of mine exists, as `r7611`'s and `r7613`'s were.

---

## ⓵ The source question, and this time the corpus answers more of it than I expected

| source | what it already establishes — **read, not recalled** |
|---|---|
| `P13` §face-status | ⛭ **the face is ODD-DIMENSIONAL and the paper says so in those words**: *"compact, connected, spin, non-abelian continuous isometry, **and odd-dimensional**, being the five-sphere"* — and draws the consequence I need: *"the equivariant index it kills is that of a $\mathbb Z_2$-graded operator, and **the grading exists only in even dimension**"* |
| `P13` §face-status | **the Dirac spectrum on the round face of radius $\alpha$ is $\pm(\tfrac52+k)/\alpha$, least eigenvalue $5/2\alpha$, no zero modes**, with its own receipt `P13_the_compact_face_is_odd_dimensional` |
| `P13` §face-status | and why that is **not** a closure of this route — 69's correction to my `r7613`: the sentence is about **massless content**, and a triple needs a Dirac **operator**, which the gapped face has |
| `P14_quantisation_not_strength` | **a topological label supplies quantisation and NEVER strength**; ⇒ *"if a coupling is to come from this geometry it must come from the **bundle** and not from the **label**"* |
| `L221`/`B59` | `PO-5` owns the coupling, and **a connection without a dimensionless kinetic coefficient is HALF the named test** |
| `L221`/`B61` | the index obstruction's hypotheses do not cover this route; $\gamma^5$ meets the grading axioms **where a grading exists**; $J$ and order-one named untested |
| `r7611+cc66` (mine) | $E=\pi_*(\text{mode bundle})$ is flat and $H^1(G,\su(3))=0$ — the **walls'** bundle has no moduli |
| `r7613+cc66` (mine) | the leaf route is closed by the two-form count; **the face was never mine to close** |

⇒ **AND THE MEASURED ABSENCE, which is where this row's exposure sits.** The vocabulary ⑵ turns on —
**`spectral action`, `cutoff function`, `Yang–Mills coefficient`** — occurs in **no corpus paper and in
no receipt but `B61`**, and there only inside `B61`'s own list of terms it tests for the *absence* of.
*So the cutoff, its moments, and any $\Lambda$ are entirely mine, exactly as $J$ was at `r7613`. There
is nothing to inherit and nothing to check my arithmetic against.*

---

## ⓶ What ⑴ most likely is, and the one part of it the corpus has already decided

**$\gamma$ does not exist, and that is not a defect of the construction — it is the face's dimension,
and `P13` states it.** An odd-dimensional manifold gives an **odd** triple. So "$J$ and $\gamma$ as the
face's dimension allows" resolves to: **$\gamma$ — none; $J$ — yes, in the KO-dimension an odd
5-manifold carries.** *I register that as a reading of `P13`'s own sentence rather than as a result of
mine, and the computation's job is to verify the $J$ axioms that remain ($J^2$'s sign, $JD=DJ$) rather
than to rediscover the absence of a grading.*

---

## ⓷ The questions, with rule-in/rule-out fixed before computing

| # | question | ruled IN by | ruled OUT by | confidence | 
|---|---|---|---|---|
| ⑴ᵃ | does a real structure $J$ exist on $\mathcal H$? | an explicit antilinear $J$ with the right $J^2$ and $JD=DJ$, exhibited | no consistent sign assignment in any admissible KO-dimension | **high** it holds |
| ⑴ᵇ | does the order-one condition hold? | $[[D,a],Jb^*J^{-1}]=0$ verified on the assembled triple | an explicit violating pair | **high** it holds |
| ⑴ᶜ | do the inner fluctuations give $\su(3)$-valued one-forms with non-zero curvature? | $F\neq0$ identically on a generic fluctuation, computed | the fluctuations collapsing to scalars, or $F\equiv0$ | **high** it holds |
| ⑵ | **does CR fix the fluctuation or the coupling?** | something in CR ($\beta=2\pi\alpha$, the radius $\alpha$, the walls' flat bundle) fixing the Yang–Mills coefficient or selecting the field | the coefficient remaining a free moment of the cutoff, and each CR datum failing on a stated ground | **medium-high** it does NOT |

**Why I expect ⑵ to fail, stated now so it cannot be discovered conveniently later.** A coupling is
**dimensionless**. $\alpha$ is a length and $\beta=2\pi\alpha$ is a length, so neither fixes a
dimensionless number alone; and the walls' bundle is **flat with $H^1=0$** (my own `r7611`), so it has
no moduli to supply one — which is `P14_quantisation_not_strength`'s point in its own words, arriving
here from a different direction.

⌗ **WHERE I AM LEAST SURE, AND IT IS THE ONE THING THAT COULD RULE ⑵ IN.** $\beta=2\pi\alpha$ makes
$\beta/\alpha=2\pi$ — **a pure number the construction fixes exactly.** *That is the only
dimensionless quantity I know of in the corpus that is not an input, and if a cutoff moment can be
tied to it the route would fix a coupling.* I do not expect it to (a ratio of lengths is not a moment
of a cutoff function), but **I am registering it as the candidate to test rather than the objection to
wave away**, because dismissing the one case that could overturn the verdict is how a pre-registration
becomes decoration.

---

## ⓸ Controls — and the first one failed twice at `r7613`, so it is built first

1. **A positive control on the triple checker**, reusing the form that finally worked at `r7613`: the
   two-point **bimodule** triple, algebra on the left factor and its opposite on the right through
   $J$, with $[D,a]\neq0$ so the order-one arm is not vacuous. *At `r7613` my first two attempts at
   this control were both wrong — the wrong axiom, then a triple that genuinely violates order-one —
   and each failure was caught by the control refusing to pass. It is built before anything else here.*
2. **A positive control on the curvature test**: a known Yang–Mills fluctuation must return
   $F\neq0$, so a verdict of "flat" is about the candidate and not my test.
3. **The face's Dirac spectrum reproduced**: $\pm(\tfrac52+k)/\alpha$ with least $5/2\alpha$, read
   from `P13` **and** recomputed, so the operator this triple is built on is the paper's.
4. **An order-one violation shown visible**, as at `r7613`.
5. ⛭ **A DIMENSIONAL control, because ⑵'s whole argument is dimensional:** the checker must be shown
   able to tell a dimensionless quantity from a dimensionful one — $\beta/\alpha$ from $\beta$ — or
   "a length cannot fix a coupling" is rhetoric rather than a measurement.

---

## ⓹ Outcomes, pre-registered, mapped onto the order's three

1. **The construction fixes a field strength or a coupling** → the gauge half's test is met on this
   route. I state explicitly which, and whether it is `PO-5`'s coupling or only a connection.
2. **The fluctuations are a free field with a free coupling** → *the route supplies a gauge sector the
   construction does not determine*, which is a **result about the rhyme** and is to be stated as
   such — not as a closure and not as a success.
3. **A piece is missing** → the route closes on that piece and the composite route is the one left.
4. **If `P13`, `B59` or `B61`'s own statements turn out incomplete** → larger than this row, and
   **routed**, not claimed.

---

## ⓺ Scope, and two constraints I found rather than was given

**No paper edited**: `P13`, `P14`, `P18` untouched, the register row is 69's, instruments stay frozen
per `r7577`. **`PO-5` is not this row** — but ⑵ *touches* it, so if the answer is "nothing fixes the
coupling" that is a statement about `PO-5`'s question and I will name it as `PO-5`'s rather than
annexing it.

⛔ **AND `B61` NOW TESTS FOR THE ABSENCE OF EXACTLY THIS ROW'S VOCABULARY.** Its list is
`inner fluctuation`, `spectral triple`, `Connes`, `almost-commutative`, `spectral action`, and a
corpus paper containing any of them outside the set-aside phrasings (*"unexamined"*, *"over the leaf"*,
*"one-dimensional leaf"*) makes `B61` red. ⇒ *So if this row examines the face, `B61`'s set-aside list
needs a third entry, and that is 69's amendment to make — it has made two already, at `r7613` and
`r7615`. My own prose goes to the receipt and to `appendix_receipts_*`, which `B61` excludes by name,
and never to a paper.*
