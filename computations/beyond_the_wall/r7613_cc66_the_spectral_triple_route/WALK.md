# `r7613+cc66` — the walk: what was computed, what it cost, and how the pre-registration scored

`spectral.py` — **22 checks, all pass, 2 s.** Output in `spectral_out.txt`.

---

## The result

**The spectral-triple route is closed on the pieces the corpus supplies, and it closes on the LOCUS,
before the real structure is ever reached.**

`P14` supplies `H` and `D` over the **leaf** — read from the paper, not recalled: *"the leaf is
compact and the Dirac operator on it carries a `\emph{finite}` analytical index"*. The leaf is a
compact **one**-dimensional domain. A gauge curvature is a **two-form on its base**, and the space of
two-forms over a one-dimensional base is **zero**-dimensional — counted by solving
$M+M^{\mathsf T}=0$ for the free entries, never by quoting $\binom p2$, with the counter returning
**1, 3 and 10** at $p=2,3,5$ so the zero is the leaf's dimension and not the counter's. ⇒ *So a
connection built over the leaf has no object a field strength could be, whatever its inner
fluctuations are.*

And the obvious repair is where the corpus states an obstruction rather than supplies a piece:
building the triple over the **face** needs a Dirac operator there, and `P13` §face-status says in
its own words — read here — *"the round face carries no Dirac zero modes, so there is no massless
content for it to act on"*.

**On the kernel reading the route closes twice over.** `P14` states $\dim\ker_+=3$, $\dim\ker_-=0$,
so a real structure anti-commuting with the grading would have to carry a 3-dimensional eigenspace
onto a 0-dimensional one: the gap is **3** and an antilinear bijection cannot close it. The control is
a **construction**, not an assertion — on a balanced $(3,3)$ space the gap is 0 and the $J$ is
exhibited, anti-commuting with the grading and squaring to $+1$. And on the kernel $D$ is zero by
construction, so every inner fluctuation $a[D,b]$ vanishes: the fluctuation span has rank **0**,
against rank **11** for the same expression on the circle triple.

⚠ **The reading this does NOT close, named in `PREDICTION.md` before it was computed and held to
here.** The $(3,0)$ count belongs to $\ker D$, **not** to $\mathcal H$. On the full $L^2$ of the
leaf's spinors the grading is balanced and the chirality obstruction does not apply. So question ⑴ is
closed on the **kernel** reading and **open** on the $L^2$ reading — and question ⑵, the locus, is
what decides the latter. *The file says this in its own output rather than letting one reading stand
in for both.*

⛔ **Not claimed:** that no route exists — `B59`'s **composite/emergent** route is untouched and
unexamined, and it is now the one left; that a **coupling** follows (`PO-5`, a different row); that
`B61` is weakened — its rows are read, not re-derived, except the grading, recomputed here so nothing
is inherited on trust.

---

## How the pre-registration scored

| registered | outcome |
|---|---|
| band: **0–1 of 4** questions answered in the route's favour | **1 of 4** — question ⑶ (order-one) answers in its favour and **buys it nothing**, holding vacuously because $[D,a]=0$ on a kernel. Inside the band, at its top edge. |
| ⑴ $J$: **medium** it closes | closed on the kernel reading, **open** on the $L^2$ reading — as the registered trap said it would be |
| ⑵ locus: **medium-high** it closes | **closed**, and it is the obstruction that fires first |
| ⑶ order-one: **low-medium** it closes | **does not close it** — passes vacuously |
| ⑷ fluctuations: **medium** it closes | **closed** on the kernel reading (rank 0) |
| pre-registered **outcome 2** — "a piece the construction cannot supply" | **this one**, and the piece is named: a two-form over the carrier the corpus's $H$ and $D$ live on |

⛭ **AND THE NAMED PREDICTION HELD, WHICH IS WORTH MORE THAN THE VERDICT.** `B61` priced the risk as
**$J$ or the order-one condition** — *"either can kill it"*. `PREDICTION.md` priced it as the
**locus**, reached first, and said: *"if $J$ turns out to be the killer and the locus is bridgeable,
`B61` was right and I was wrong, and I will say so in those words."* **The locus fired. The order-one
condition did not close the route — it passes.** So the registered call holds and `B61`'s expected
killer is not the one that fired. *That is a prediction that could have come out the other way and is
reported as scored rather than as confirmed.*

---

## Faults, and the control caught me twice before it passed

⛔ **Control 1 failed twice, and both failures were mine.** A control that cannot fail licenses every
verdict under it, so this is the part of the walk that matters most.

1. **The first version asserted the wrong axiom.** `A = C(S^1)` on $L^2(S^1)$, $D=-i\dd/\dd\theta$,
   $J$ = complex conjugation, asserting $JD=DJ$. It failed — **correctly**: for that $D$, conjugation
   gives $JDJ^{-1}=-D$, so plain conjugation is not a real structure for that operator. *I had
   written down the wrong axiom, and had the check been written the other way it would have passed
   and certified nothing.*
2. **The repair was also wrong, and more interestingly.** The two-point space taken naively —
   $\mathcal A=\mathbb C\oplus\mathbb C$ acting **diagonally** on $\mathbb C^2$, $D$ purely
   off-diagonal — asserting the order-one condition. It failed too, and again correctly: **that
   triple genuinely violates order-one**, the defect being $60.1$ at $a=b=\operatorname{diag}(2,-3)$.
   *Which is exactly why the Standard Model's finite triple is built as a **bimodule** and not like
   that.*
3. **The passing form is the one the condition is actually about:** the algebra on the left tensor
   factor, its opposite on the right through $J$, $D=D_1\otimes1+1\otimes D_1$ with $D_1$ real
   symmetric so $D$ is $J$-symmetric. Then $J^2=+1$, $JD=DJ$, $\|[D,a]\|$ up to $17.0$ so the
   order-one arm is **not** vacuous, and the order-one defect is $0$ **exactly**.

⌗ *The circle is kept as a second control whose job is now to come back the other way: it reports
$\|JDJ^{-1}-D\|=26.98$ against $\|JDJ^{-1}+D\|=0$, so the checker distinguishes a real structure from
something that merely looks like one — the distinction my first version got wrong.* And `CONTROL 2`
shows the order-one expression **can** fail on a generic non-commutative pair, so the vacuous pass in
question ⑶ is a measurement and not a tautology of my checker.

⌗ *And the paper-reads are reads: four literals opened from `corpus/matter_sector_paper.tex` and
`corpus/boundary_paper.tex` rather than recalled — the defect `check_unread_figure` named in this
seat's work twice, at `r7577+cc66.4` and `r7611`.*

---

## Routed, not claimed

1. **`B59`'s composite/emergent route is now the only one left** of the five, and it is unexamined.
   Four of five are closed: three by `r7611`, this one here, and the isometry route long since walled.
2. **The $L^2$ reading of question ⑴ is open and the locus is what closes it, not $J$.** If a carrier
   of dimension $\geq2$ ever appears for the corpus's $H$ and $D$ — a leaf *family* rather than one
   leaf — then $J$ on the balanced $L^2$ grading becomes the live question and `B61`'s pricing becomes
   the right one. *That is a conditional worth keeping rather than a closure.*
3. **The order-one condition holding vacuously on a kernel is a general fact about this construction**,
   not a feature of this row: any question asked of $\mathcal A$ and $D$ on $\ker D$ answers trivially,
   because $D$ is zero there. *A row that wants content from the wall kernel has to take $\mathcal H$
   larger than the kernel, and then the locus question is the one it meets.*
