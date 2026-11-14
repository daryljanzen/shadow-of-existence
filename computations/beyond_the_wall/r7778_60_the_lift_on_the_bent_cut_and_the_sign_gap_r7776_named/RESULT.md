# r7778 (60) — RESULT

**The remainder of `r7763`'s item ② on the bent cut: the lap's middle segment, and the gap `r7776`
named rather than closed.**

**ELEVEN arms, registered and pushed before anything was measured. EIGHT meet their criterion — and
two of the three failures are the result, not an accident of it.**

* **⒜ `r7776`'s sign fork is DISSOLVED.** The sign it worried about lives in `μ`, and of the six
  conditions the bead imposes, **none uses `μ` alone**; in every place the bead does use the mass
  function the radiation term is **even**.
* **⒝ And in closing that gap the lift turns out not to respect the bound `thm:bead` prints.**
  `|Im τ̃| ≤ πα/3` is exact on the vacuum bead — reproduced here to `2.3e-29` — and on the bent cut
  the same accumulation is **larger**, by `1.66690 Mpc`, `+3.0533e-4` relative. *The registration
  predicted the other direction.*

Every constant derived in the probe from the published pair and `ω_γ`: `α = 5213.287`,
`r₀ = 5051.488`, `2M = 2006.5950`, `K = 3006.658 Mpc²`, and the vacuum comoving turnaround
`r_t = (2Mα²)^{1/3} = 3792.226904 Mpc`. Measured on the **full** clone (`8012` commits from `HEAD`).

---

## Ⓐ The fork, and why it was posed about the wrong object

### ① Of the six conditions, none is a condition on `μ`

| the condition | how the mass function enters |
|---|---|
| the Nariai condition `ΛG²M²/c⁴ = 1/9` | **does not involve `μ` at all** — it fixes `2M` from `Λ` |
| the unit-speed seams `f = 0` | `μ/r` |
| the comoving turnaround `1 − f = 0` | `μ/r` |
| the Euclidean null `f = 2` | `μ/r` |
| the contour radicand `(dr/dτ̃)² = 1 − f` | `μ/r` |
| the rate `h² = μ/r³ + 1/α²` | `μ/r³` |

**Bare-`μ` conditions among the six: zero.** ⌗ *Measured by differentiating each condition with
respect to `μ` and finding the power of `r` that clears the result of `r`, not by reading the
formulae. The claim is scoped to exactly those six.*

### ② The radiation term the contour uses is EVEN

`1 − f = μ/r + r²/α² = 2M/r + K/r² + r²/α²`, and under `r ↦ −r`:

* **`K/r²` is unchanged — radiation enters the comoving velocity with the same sign on both branches;**
* `2M/r` flips — the dust term is the odd one.

### ③ And so is radiation's contribution to the rate

`K/r⁴`, even and positive at `+|r|` and `−|r|` alike, at every radius sampled. **⇒ `r7776`'s *"a
negative radiation term is not radiation"* was a fact about `μ`'s bookkeeping in a SIGNED
coordinate, and not about a density.**

### ④ ⛔ FAILS as registered — on its control, not on its finding

* **The finding holds:** the symbolic residual of `r = −(2Mα²)^{1/3}cosh^{2/3}(3τ̃/2α)` against
  `(dr/dτ̃)² = 2M/r + r²/α²` with **`2M` POSITIVE** is **exactly `0`**, and `5.7e-15` numerically
  across nine samples of the collapse leg. **`thm:bead`'s continuation signs `r` and keeps `2M`.**
* And the corpus's `R = γ⁵` — `r ↦ −r`, **`2M ↦ −2M`**, the `A₂` diagram automorphism — is carried by
  five other sentences, none of them the theorem's continuation sentence. **Two maps, and `r7776`
  read the second into the first.**
* **⛔ The arm fails because the control I registered was the MINIMUM relative residual over the
  samples under `2M → −2M`, and it came out `4.9e-5`.** The minimum falls at `τ̃ = 4α`, where
  `|r| = 130433 Mpc` and the mass term carries **`2.46e-5`** of the sum — so the control was
  evaluated where the term it was meant to discriminate is negligible. Post-hoc, and declared as
  post-hoc: the **maximum** is `0.9972`, which is what a control should have read.
* **⇒ THE GUARD THIS OFFERS: *a control evaluated where the discriminating term is negligible
  discriminates nothing.*** The arm stays failed; the criterion is not rewritten.

**⇒ ①–④ together: the fork is dissolved rather than decided.** Both outcomes were reachable, and
the one that would have stood as a real gap — a bead condition that sees the bare sign — is not there.

---

## Ⓑ What the bend does to the lift

### ⑤ The lift acquires an inner boundary, and it is `K/2M`

On the vacuum cut the radicand is negative on exactly `−r_t < r < 0`, so the lift runs **to the
branch point**. On the bent cut, with `r = −s`, the radicand is `−2M/s + K/s² + s²/α²`, whose zeros
are the roots of

> `s⁴/α² − 2M s + K = 0`

and there are **exactly two** positive ones:

| root | value (Mpc) | against |
|---|---|---|
| inner | `1.498387999` | `K/2M = 1.498388`, **ratio `1.000000000`** |
| outer | `3791.727309` | `r_t = 3792.226904` |

**⇒ the imaginary excursion is an interval strictly inside `(−r_t, 0)`: on the bent cut the lift
does not reach the branch point.**

### ⑥ The outer root moves inward, by a part in eight thousand

`0.499594 Mpc`, `1.3174e-4` relative — inward, and below the registered `1e-2` ceiling.

### ⑦ ⛔ FAILS, and the failure is the finding: the bend EXCEEDS the printed bound

`thm:bead` prints `|Im τ̃| ≤ πα/3`, *"fixed by the exponent and independent of `M`"*.

| cut | `|Im τ̃|` accumulated across the lift (Mpc) | against `πα/3 = 5459.341081456372` |
|---|---|---|
| vacuum | `5459.341081456372` | **`−2.3e-29` relative** — the printed bound, reproduced |
| bent | `5461.007981063637` | **`+3.0533e-4` relative, `+1.66690 Mpc`** |

*Computed twice: `scipy` quadrature in the probe and `mpmath` at 50 digits in the addendum, with
both simple zeros substituted away (`u² = |s − s_end|`); the two agree, and the same machinery
returns `πα/3` on the vacuum cut to 29 digits.*

**The registration predicted strictly LESS than `πα/3`. It is more.** And the mechanism is the even
term from ②:

* the lift is **shorter** in `r` by `1.997982 Mpc` (both ends pulled in), **but**
* `K/s²` **reduces** `|radicand|` across the interior — at the midpoint `s = 1896.613` it falls from
  `0.9256356` to `0.9247998`, `−9.030e-4` relative — so `1/√|radicand|` **rises**,
* and the integrand's rise beats the interval's shortening.

**⇒ The clause is a property of the VACUUM bead, exact there, and it does not survive the bend.**
⌗ *`thm:bead` is not contradicted: it is a theorem about the vacuum slicing curve, and that is what
it remains. What does not stand is the inherited reading that the lap's imaginary excursion is
bounded by `πα/3` for the history the content actually rides.*

### ⑧ The lap gains a segment: three becomes four

| cut | the conjugate side, `|r|` | the radicand |
|---|---|---|
| vacuum | `(0, 3792.226904)` | **negative — the lift, all the way to the branch point** |
| vacuum | above | positive |
| bent | `(0, 1.498388)` | **POSITIVE — `Re τ̃` advances** |
| bent | `(1.498388, 3791.727309)` | negative — the lift |
| bent | above | positive |

**⇒ on the bent cut the branch point is reached in REAL cosmic time from the conjugate side.** The
lap's segments go from three (collapse, lift, expansion) to four.

### ⑨ And that approach is radiation's, on this side too

`d ln|r| / d ln|τ̃| = 0.499978` between `1e-4` and `1e-3` Mpc, with the radicand positive across the
whole interval — against `0.500022` which `r7776` measured on the **matter** branch over the same
decade. **The same exponent on both branches, which is what ② requires.**

### ⑩ ⛔ FAILS on its own number, and the number was mine to get right

| `|r|` (Mpc) | `h²(+|r|)` | `h²(−|r|)` | relative difference |
|---|---|---|---|
| `1e-3` | `3.008664e+15` | `3.004651e+15` | **`1.3339e-3`** |
| `1` | `5.013253e+03` | `1.000063e+03` | `0.80052` |
| `r_t` | `7.360250e-08` | `1.453807e-11` | `0.99980` |

The registration said *"better than `1e-8` at `|r| = 1e-3`"*. **The exact relative difference is
`2(2M/K)|r|`** — `1.3348e-3` at `1e-3 Mpc`, matching the measurement — so `1e-8` is reached only
below `|r| ≈ 7.5e-9 Mpc`. **The threshold was arithmetic I could have done before registering, and
did not.** The qualitative half stands: radiation even, dust odd, order unity at `r_t`.

---

## Ⓒ ⑪ The honest form of the fork

**One sentence in the eight regions searched assigns content to the collapse leg** — the
`fig:dS_SdS` panel (C) caption: *"content processes---the cooling leg's nucleosynthesis, the plasma's
sound horizon and diffusion---run on the leaf's rate"*. ⌗ *Regions searched: the theorem, its proof,
`rem:head-admissible`, the scope paragraph, `lem:twoturnings`, both figure captions, and
`sec:lift-initial-rate`. Nothing is claimed about the rest of the corpus.*

**⛔ And the registration called those "seven places" and then listed eight.** Eight were searched
and the count is recorded here, because an arm that searches a set is worth nothing if the set's size
is not the one declared.

**⇒ Nothing measured here says the progenitor's branch CARRIES radiation. It says no sign obstruction
forbids it.** So the fork's honest form is a **disjunction over the progenitor's content**, not a sign
contradiction — and the text's one assignment is to the *cooling* leg, which is the collapse leg read
forward, so the disjunction can be narrowed from the text but not closed by it.

---

## What this adds to the small-r sort

`r7765` recorded `r7768`'s sort: three results stand on the bent cut (the trichotomy and the Nariai
selection, the flatness, the photon-family translate), and one does not (`P15 sec:scope`'s
radial-profile sentence). **This adds a second non-survivor and a fourth survivor:**

| the result | on the bent cut |
|---|---|
| the horizon trichotomy and the Nariai selection | **stands** (`r7768`) — properties of `f`, which carries no `K` |
| the exact Euclidean flatness of the constant-`τ` slices | **stands** (`r7768`) — any profile |
| the photon-family translate property | **stands** (`r7768`) — to `2.1e-13` |
| **the branch point's reachability in finite proper time** | **stands** — exponent `1/2` instead of `2/3`, both legs (`r7776`, and ⑨ here on the conjugate side) |
| `P15 sec:scope`'s radial-profile sentence | **does not stand** (`r7768`) — ⛭ **and `r7767` REMOVED it: discharged, see below** |
| **`thm:bead`'s `|Im τ̃| ≤ πα/3` as a bound on the actual history** | **⛔ does not stand** — exceeded by `3.05e-4` (⑦) |

**And one structural change the sort had no row for: the lap's segment count rises from three to
four, and the lift detaches from the branch point at `K/2M = 1.4984 Mpc` (⑤, ⑧).**

## Routed, not decided here

1. **Whether the corpus wants the lap's imaginary bound restated with `K`,** or whether `πα/3` is
   meant as a vacuum-only statement and the actual history's excursion is simply a different number.
   *This read cannot choose: it is a question about what the clause is for.*
2. **`r7776`'s fork is withdrawn as dissolved** — and `r7776` is not yet merged, so the withdrawal
   reaches the register with the finding rather than after it.
3. **The disjunction over the progenitor's radiation content** stays open, narrowed by the one
   caption sentence and closed by nothing.

## The guards this revision offers

* **A control evaluated where the discriminating term is negligible discriminates nothing.** (④)
* **Before a sign is treated as an obstruction, find the object the argument actually uses it in.**
  (①–③: the fork was about `μ`; every bead condition uses `μ/r` or `μ/r³`.)


---

## ⛭ Added after `r7767`, which landed while this revision sat on its branch

`r7767` (69) rewrote `P15` on one rate. This line's three live probes were re-run against the new
wording, because they read the corpus text and a rewrite can break a read that was sound against the
old:

| probe | against the rewritten papers |
|---|---|
| `r7776` | **10 of 10**, unchanged |
| `r7778` (this one) | **8 of 11**, the same three failures, unchanged |
| `r7768` | 11 of 12, arm 6 still FAIL — **but its subject is gone** |

**The sec:scope non-survivor in the table above is DISCHARGED.** Measured on the two commits: the
clause *"Nor does putting radiation into the cut supply the leaf rate"* and the phrase *"taken as the
radial profile"* each occur **once** before `r7767` and **not at all** after. The rewrite reached the
one site the correction had not reached, and the patch this line routed is spent.

**⇒ So the sort's second non-survivor is the only live one: `thm:bead`'s imaginary bound read as a
statement about the actual history (⑦).**

⌗ *And `r7768`'s arm 6 cannot say any of that itself: its gate includes finding the sentences, so it
returns the same FAIL with them gone, and its prose is printed unconditionally — a re-run now asserts
"the paragraph has not been reached by the correction" beside a measurement that located no sentence.
**GUARD: a verdict that cannot distinguish the defect is present and wrong from the defect's subject
is absent reports the same word for a live fault and a fixed one.** Recorded in full in
`ADDENDUM_r7778_ITS_SUBJECT_WAS_REMOVED.md` beside `r7768`, whose probe is deliberately left as it
ran.*

⌗ *The fast job is green on the merged tree: every step passes, on the lists read from the workflow.*
