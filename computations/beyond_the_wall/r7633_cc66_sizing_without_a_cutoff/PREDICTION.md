# `r7633+cc66` — sizing the dimension-six term **without a cutoff**

**Registered before a line of the computation exists.** Every figure quoted below is landed where it
is cited; nothing here is computed.

## The order

> *"Size the term without a cutoff. In a continuation the dimension-six term enters with its
> renormalised coefficient, the coupling, and a renormalisation scale in its logarithm. So: ⑴ from
> P10, say what multiplies the dimension-six invariant in the effective action on this background —
> the coupling's power, the background curvature's power, and what sits in the logarithm. ⑵ Size its
> effect relative to the dimension-four terms on each observable the construction reads (the rate,
> the acoustic scale, the tilt, the tensor amplitude), at each observable's epoch. Use the
> gravitational coupling as measured, and say so: it is an inherited datum, not a cutoff. ⑶ Set each
> against the measured precision."*

⌗ `PO-89`'s clause is now *"TERMINATES IF the dimension-six term's effect on every observable is
shown below what measurement resolves, **sized by the scales the construction does carry rather than
by a cutoff it does not have**."* So this row has no free `Λ`, and that is the point: `r7631` ② found
the regulator is a spectral continuation with **no cutoff parameter at all**.

## ⑴ What P10 already says, located — this is the whole of step ⑴ and it is a READ, not a derivation

| statement | where |
|---|---|
| **"in the reduced theory the only scales are `a` and the Planck length"**, so the vacuum energy is **`a^{-1} Σ_j f_j (ℓ_P/a)^j`** against **a polynomial in `ln(a/ℓ_P)`**; the power is `1+j`, **one vertex pair costs `ℓ_P²`**, and the interaction enters at **`j ≥ 2`** | `canonical_time` l.1621–1623 |
| ⚠ **`ℓ_P` is "a gauge-combination rather than a second physical length"**, so a cutoff "is not smuggling a scale in either" | `canonical_time` l.484 |
| the spectral zeta has a **pole at `s = −1` of residue `15/4`**, so the renormalised energy carries a **`ln a`**, and the trace is `Θ = ρ − 3p ∝ (15/4) a^{-4}`, **independent of the renormalisation scale** — scheme-independent, which is what an anomaly is | `canonical_time` l.583–585 |
| the dimension-six obstruction coefficient is **`6023/20160`** | `canonical_time` l.1283 (`r7601`, carried by this seat at `r7629`) |

⇒ **So the three things step ⑴ asks for are already in the paper and I expect to report them rather
than derive them:**

- **the coupling's power** — one factor of **`ℓ_P²`** per vertex pair, so dimension six sits **one
  vertex pair above** dimension four;
- **the background curvature's power** — on this background the only length is `a`, so an operator
  two dimensions higher carries **two more inverse powers of `a`**;
- **what sits in the logarithm** — **`ln(a/ℓ_P)`**, a ratio of the construction's own two scales.
  ⚠ **Not a cutoff.** This is the substantive content of "without a cutoff": the logarithm's argument
  is fixed by the theory, not chosen.

⇒ **Hence the dimensionless suppression of dimension six against dimension four is `(ℓ_P/a)²`**,
times a rational coefficient of order one, times a logarithm. **That product is the deliverable.**

## ⚠ WHERE I EXPECT TO LAND, AND IT MISSES THE ORDER'S REACHABLE NEGATIVE

**The reachable negative the order names:** an observable on which the term is within reach.

⚠ **I expect to miss it, and by a margin so large that the interesting part is not the number but
whether the sizing is honest.** `(ℓ_P/a)²` at the present epoch is of order `(10^{-35}\,\mathrm{m} /
10^{26}\,\mathrm{m})² ≈ 10^{-122}` — the familiar number — and at recombination the layer was ~`10³`
times smaller, which buys back only ~`6` orders. Against measured precisions between `10^{-2}` and
`2.9×10^{-4}` that leaves **a margin of order `110`–`120` orders on every observable**.

⇒ **So I expect the exit to FIRE, decisively, and with no cutoff anywhere in the argument.** I
register that in advance because it is the outcome that closes `PO-89`, and because a margin that
large is exactly the kind of result that invites a sloppy derivation — the number is not in doubt, so
the only thing worth computing carefully is whether each factor is the construction's own.

⌗ **And what WOULD fire it, named so the miss is a measurement and not a shrug:** the term reaches a
measured precision only where `(ℓ_P/a)² ≳ 10^{-4}`, i.e. `a ≲ 10²·ℓ_P`. **That is the Planck era, and
no observable the construction reads sits there** — the four all read epochs from recombination
onward. So the negative is unreachable for a structural reason, not a numerical one.

## The control the order names, and what it is for

> *"the control: the same sizing applied to the dimension-four logarithm, whose coefficient `15/4`
> P10 carries, giving its known order."*

The dimension-four trace anomaly is `Θ ∝ (15/4) a^{-4}` (l.583–585). Sized against the classical
background density by the **same** estimator, it must return the **known** order of a one-loop
graviton correction on this background, `~(ℓ_P/a)²` — the `10^{-122}` of the present epoch. ⇒ **If the
estimator returns that for a term whose order is independently known, it is measuring something; if
it does not, the dimension-six number below is worthless.** That is the control's whole purpose and I
will report it before the dimension-six table, not after.

⚠ **And the trap in it:** `15/4` is **scheme-independent** (it is an anomaly) while a *logarithm's*
value is not, so the control may only check the **order**, never a digit. I will not quote the
dimension-four number to a precision the scheme does not support.

## The questions, priced before computing

| # | question | confidence |
|---|---|---|
| ① | is the suppression of dimension six against dimension four exactly `(ℓ_P/a)²` on this background? | **high YES** — l.1621–1623 gives the expansion in `(ℓ_P/a)` with `ℓ_P²` per vertex pair |
| ② | is the logarithm's argument `a/ℓ_P`, with no cutoff? | **high YES** — stated at l.1621 |
| ③ | does the control return the known `~(ℓ_P/a)²` for the dimension-four anomaly? | **medium-high YES** — and if it does not, ① and ② do not save the row |
| ④ | is the term within reach on ANY of the four observables? | **high NO** — ~`110`–`120` orders short at every epoch |
| ⑤ | can the rational coefficients change that? | **high NO** — `6023/20160 ≈ 0.3` and `15/4 = 3.75` are order one; `120` orders is not reachable by a rational |

⌗ **Where I am least sure, and it is ① rather than ④.** The suppression is `(ℓ_P/a)²` *if* the
dimension-six invariant on this background really carries two more inverse powers of `a` and no
hidden power of the coupling. P10 says at l.1283 that **on the one-parameter family the five
dimension-six scalars collapse** — two vanish identically and the rest are pure powers, rank one — so
*which* invariant is being sized is itself delicate, and `r7629` already established that
`6023/20160` is an **obstruction to covariance** rather than an invariant's coefficient. ⇒ **So the
row must say what it is sizing, and if the construction does not name a dimension-six invariant on
this background, I must report the suppression as attaching to the obstruction's magnitude rather
than invent an invariant for it to multiply.** That distinction is the one I would most easily blur
in the direction that makes the row look cleaner than it is.

## The controls

1. **The dimension-four control above**, reported first, so the estimator is validated on a term of
   known order before it is trusted on one that is not.
2. **Each factor traced to the paper**, with its line, so "the construction's own scales" is checkable
   rather than asserted — and `ℓ_P` carried as the **measured** gravitational coupling, an inherited
   datum, with that said in the output and not only here.
3. **A cutoff-shaped quantity shown ABSENT**: the row must contain no free `Λ`, and I will check that
   by perturbing — a sizing that silently depends on a cutoff would move when one is varied, and this
   one must not move at all.
4. **Each observable at its own epoch**, with the epoch declared, rather than one number for all four.
5. **The margin reported in orders of magnitude**, since `a` at each epoch carries cosmological
   inputs, and checked across a decade of each so a factor of a few cannot move the verdict.

## Outcomes, pre-registered

- **The term is within reach on some observable:** the reachable negative fires, `PO-89` does not
  close, and I report which observable and at what epoch.
- **The term is below measurement on all four:** the exit fires and `PO-89` closes as its clause now
  reads — sized by the construction's own scales and not by a cutoff. *This is what I expect.*
- **The construction does not name a dimension-six invariant on this background:** then the sizing
  attaches to the obstruction's magnitude, I say so, and I do **not** manufacture an invariant.
