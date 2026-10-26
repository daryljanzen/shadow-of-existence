# `r7615+cc66` — the walk: what was computed, how the pre-registration scored, and the one correction I owe the order

`face.py` — **19 checks, all pass, 8 s.** Output in `face_out.txt`.

---

## The result

**⑴ The order's Hilbert space admits no real structure, and the route survives the correction.**

`r7615` specifies $\mathcal H=\text{spinors}\otimes\mathbb C^3$. A real structure needs
$Ja^*J^{-1}$ to lie in the algebra's **commutant** — and $M_3(\mathbb C)$ acts **irreducibly** on
$\mathbb C^3$, so its commutant is the scalars: **dimension 1**, computed by solving $[X,m]=0$ for
every generator rather than quoted. *There is nowhere for the opposite action to live.* On the
bimodule $\mathcal H=\text{spinors}\otimes M_3(\mathbb C)$ the commutant is **9** and there is room.

⌗ *This is a correction to the specification and **not** a closure of the route — and it is exactly
the lesson `r7613`'s control taught me after failing twice: the algebra on the left factor, its
opposite on the right through $J$. The control earned its keep a second time, one row later, by
catching the same shape in the order itself.*

**$\gamma$ does not exist at all**, and that is `P13`'s own sentence rather than a finding of mine:
the face is *"odd-dimensional, being the five-sphere"* and *"the grading exists only in even
dimension"* — both read from the paper here.

**⑴ᶜ The face carries what the leaf did not.** The same two-form counter, in the same shape as
`r7613`'s, returns **10** over the five-dimensional face against **0** over the one-dimensional leaf.
⇒ *That contrast is the whole relation between the two rows: `r7613` closed because $p=1$ gives
zero, and this route is open because $p=5$ gives ten.* A generic $\su(3)$-valued one-form has
non-vanishing curvature, computed from $F=\dd A+A\wedge A$, with a constant commuting one-form
returning identically zero as the control.

**⑵ The real test answers against the construction.** A gauge **field** is there. But:

| | |
|---|---|
| is any power of $\alpha$ or $\beta$ dimensionless? | **no** — the exponents are forced to $p_\alpha=-p_\beta$, solved rather than asserted |
| so the only dimensionless monomial is | a power of the **ratio** $\beta/\alpha$ |
| and that ratio is | $\beta/\alpha=2\pi$ **exactly**, fixed by the construction |
| but a ratio of lengths is | **not a moment of a cutoff function**, and nothing in CR supplies $f$ |

⇒ **THE ROUTE SUPPLIES A GAUGE SECTOR THE CONSTRUCTION DOES NOT DETERMINE** — pre-registered
outcome 2, *a result about the rhyme*, and the coupling half is `PO-5`'s row, named rather than
annexed.

**And the face's operator is derived, not quoted:** Friedrich's bound on $S^5$'s own scalar curvature
is **saturated exactly at $k=0$**, which is what makes $5/(2\alpha)$ the *least* eigenvalue and
matches `P13`'s printed spectrum.

---

## How the pre-registration scored

| registered | outcome |
|---|---|
| ⑴ᵃ $J$ exists — **high** | **split, and the split is the finding**: not on the order's $\mathcal H$ (commutant 1), yes on the bimodule (commutant 9) |
| ⑴ᵇ order-one holds — **high** | **holds on the repaired triple, and is unwriteable on the order's own** — one cause for both: order-one defect **exactly 0** over all 81 generator pairs on the bimodule, **3.536** on $\mathbb C^3$, with $\lVert[D,a]\rVert=4.33$ asserted so neither number is vacuous |
| ⑴ᶜ non-zero curvature — **high** | **holds**: 10 two-forms, $F\neq0$ on a generic field, $F\equiv0$ on the control |
| ⑵ CR does **not** fix the coupling — **medium-high** | **holds**, and the candidate I named as the one that could overturn it was evaluated: $\beta/\alpha=2\pi$ is real and fixed, and is still not a cutoff moment |
| pre-registered **outcome 2** | **this one** |

⛭ **The registered least-sure item did its job.** `PREDICTION.md` named $\beta/\alpha=2\pi$ as *"the
one candidate that could rule ⑵ in"* and committed to evaluating rather than dismissing it. It is
computed here, it is exactly $2\pi$, and the verdict turns on a distinction that survives it — a
pure number the geometry fixes is not a functional of a cutoff. *Had I dismissed it in prose the
verdict would read the same and be worth less.*

---

## Two faults, both caught by controls, and the second is the worse one

⛔ **⒜ A false premise about the spheres.** The first version of `CONTROL 2` asserted that $S^4$
would **not** saturate Friedrich's bound, so that saturation would look like a property of $S^5$.
**It failed, correctly: the round sphere is the equality case of Friedrich's inequality in *every*
dimension** — the classical theorem, not an accident of $n=5$. ⌗ *So the discriminating comparison is
not between spheres; it is between the **least** eigenvalue and the others on this one: saturated at
$k=0$, strictly exceeded at $k=1$ and $k=2$.*

⛔ **⒝ A VACUOUS OPERATOR, and this one would have shipped a meaningless pass.** Question ⑴ᵇ's first
version took $\Delta=\operatorname{diag}(0,1,2,3)$ and called it a derivative. **It is a
multiplication operator** — diagonal, so it commutes with the diagonal function $f$, so
$[D,a]=0$ identically, and the order-one condition then "held" on the bimodule **and** on
$\mathbb C^3$ for the empty reason that both sides vanish. *The control I had written to separate
the two cases is what exposed it: it came back zero where it had to come back non-zero.* ⇒ **That is
the same vacuity `r7613` recorded on a kernel — a condition met because both sides are zero
constrains nothing — and I failed to carry my own guard across one row.** $\Delta$ is now the
hermitian part of a cyclic shift, a genuine difference operator, and $\lVert[D,a]\rVert\neq0$ is
**asserted** so the block can never pass that way again.

⇒ **In both rows now, a control has caught a false premise of mine before it reached a verdict, and
that is the only reason the verdicts under them are worth reading.** ⌗ *⒝ is the more instructive of
the two: ⒜ was a wrong fact about geometry, which a reader could have caught; ⒝ was a test that could
not fail, which only a control can catch.*

---

## Routed, not claimed

1. **Which $\mathcal H$ the register row should name is 69's call.** I computed both and report the
   bimodule as the repair, but the order specifies $\mathbb C^3$ and I am not rewriting an order.
2. **⑵'s answer is a statement about `PO-5`'s question**, not an annexation of it: if nothing fixes
   the coupling, that is `PO-5`'s row speaking, and `B59` already warned that a connection without a
   dimensionless kinetic coefficient is **half** the named test.
3. **`B61` will red if this reaches a paper.** Its absence list now covers `almost-commutative` and
   `spectral action`, with set-asides only for *"unexamined"*, *"over the leaf"* and
   *"one-dimensional leaf"*. A third set-aside is needed and it is 69's amendment, as the two before
   it were.
4. **`B59`'s composite/emergent route is now the only one of the five untouched** — four closed or
   answered, this one answered as outcome 2.
