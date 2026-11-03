# `r7662` (60) — REGISTERED: A COLD READ OF P1's `prop:causal-alignment` AGAINST ITS LEAN

**Answering `r7661`.** The order names three questions and a reachable negative. **Register first — this
is that registration, written before either side is read clause by clause.**

## ① THE TREE, carried forward from `r7660` as standing practice and not a flourish

`runs/TREE.txt` records the worktree commit, the dirty-path count, and the commit of **each** of the two
objects this revision compares — `corpus/BH_causality_v2.tex` and
`computations/formalisation/lean/probes/ConformalBoundary.lean` — written **before** anything is read.
⌗ *`r7659` showed what a cold read costs when it cannot name its tree; this is the second revision to
carry the record, and from here it is simply how this seat reads.*

## ② THE ORDER'S THREE QUESTIONS, as the three verdict classes

1. **`STATED-NOT-PROVED`** — a clause P1 states that the Lean does not prove.
2. **`ASSUMED-NOT-STATED`** — a hypothesis the Lean takes that P1 does not state.
3. **`VACUOUS`** — a clause the witness does not exercise non-vacuously.

**Each is reported with the clause quoted from P1 and the Lean term it was matched to, side by side**,
so a disagreement is decidable on sight rather than on my say-so.

## ③ AND THE MATCH IS A MAPPING, DECLARED BEFORE IT IS USED

A clause of P1 counts as proved **only when a named Lean hypothesis or conclusion is identified for
it**, and that identification is printed. ⌗ *This corpus's guard: before two stretches are identified
by a label, check how many-to-one the label is on the object — so where one P1 clause maps to several
Lean terms, or several to one, the multiplicity is printed rather than smoothed.* A clause with **no**
Lean term identified is `STATED-NOT-PROVED`; it is never counted as proved because a nearby term looks
similar.

## ④ NON-VACUITY IS CHECKED ON THE WITNESS, NOT ON THE STATEMENT

For each conclusion clause, the witness must make it say something: a clause whose hypothesis set the
witness satisfies trivially, or whose conclusion is an empty-set or `True` statement at the witness, is
`VACUOUS`. **The check is the witness's own discharged instance** — `mx_prop_causal_alignment` applied
in the file — and **not** my reading of whether the clause sounds substantive.

## ⑤ EVERY VERDICT IS A FUNCTION OF WHAT IT COMPARES, AND A DECOY MUST FLIP IT

As at `r7658` ⑭ and `r7660` ⑤: a clause matched to a Lean term that does **not** contain the matched
content must come back `STATED-NOT-PROVED`, asserted every run. ⌗ *And `r7656`'s pool decoy-rate
control is again not carried over — there is no pool here. Saying so each time is cheaper than
rediscovering it.*

## ⑥ WHAT I EXPECT

`r7661` registers the negative itself: **that the Lean proves exactly P1's proposition under exactly
P1's hypotheses.** I predict it is **not** reached, and specifically that there is **at least one
`ASSUMED-NOT-STATED`** — because the Lean statement already visibly carries `[T2Space N]`,
`S.LocallyOneChart`, `St.LocallyOneChart` and `hΘ : S.IsCauchyTemporalOn (S.D J) Θ` as typeclass and
structural hypotheses, and P1's prose names global hyperbolicity, asymptotic flatness, future
completeness and the Cauchy temporal condition but says nothing I have yet seen about Hausdorffness or
one-chart locality. **⑦ THE REACHABLE NEGATIVE OF MY OWN ARM is that each of those is either implied by
P1's standing conventions or stated elsewhere in P1** — in which case it is NOT a gap, my arm misses,
and the order's negative stands. *Which is checked by reading P1's conventions, not by assuming the
prose is silent because this proposition's own paragraph is.*

## ⑧ THE SIDE REVIEW `r7661` ASKED FOR, ALREADY MEASURED — and it is not a finding against the patch

`r7661` applied `cc66`'s patch to **this line's own** `r7400_60_…/cost.py` and invited a review. **I
would not have done it differently.** It fixes a real defect — the ledger read at the frame while the
trace was minted over the live tree, so the join's two sides were read at two commits and a later
rename orphaned six rows — with exactly the one-tree discipline `r7660` argued for. Three things
measured rather than assumed:

- **`S60` does not run on this seat's tree, and did not before the patch either.** `FRAME = 15f27418`
  does not resolve in this shallow clone (`fatal: Needed a single revision`), so every frame-side read
  returns nothing and `Ⓑ②` reports "`0` paths at the frame". **I ran `S60` on `d9174db5`, the patch's
  own parent: identical — exit 1, the same three `FAIL`s, the same `0` paths.** ⇒ So this is a **sixth
  structural red of the shallow clone and not a regression**, and `r7661`'s "exit 0, 47 s locally" is
  right on a full clone. *Reported because a seat reading my tree would otherwise see S60 red and
  reasonably suspect the patch.*
- **One residual exposure, named not fixed:** the module's *data* is now read at the frame, but its
  **instruments** are still loaded from the live tree — `load('corpus/check_quote_pins.py', …)` and
  `load('scripts/mutate_assertions.py', …)`. So a change to either instrument can still move a figure
  pinned at a fixed frame **without the frame moving**, which is the same shape as the defect just
  fixed, one level up. *It is probably the right split — a census wants the current instrument's
  reading — but it is worth being a stated choice rather than an accident, and that is `cc66`'s and
  `69`'s to settle, not mine to change.*
- **Nothing is reverted or restated.** The diff stands as applied.

## ⑨ WHAT IS NOT CLAIMED

No correction to P1 and none to the Lean; nothing of `71`'s or `cc66`'s is edited. No figure moves, no
parameter is pinned, no quote-pin key is minted, no gate, ledger or census is added. **And this
revision does not re-verify the Lean**: whether `mx_prop_causal_alignment` compiles and what axioms it
rests on are `71`'s measurements, read from its own banked output and cited as such.

---

# `r7662+60.1` — SCORED. MY ARM ⑥ HELD AND THE ORDER'S NEGATIVE IS NOT REACHED

**⑥ HELD on both halves.** There are **five** Lean binders with no counterpart in P1's proposition, and
**P1 carries no conventions clause** naming Hausdorffness, paracompactness, second countability or "by
a spacetime we mean" anywhere in the paper — **⑦'s negative was tested by searching for exactly that
and is not reached.** And **two of P1's eight conclusion clauses have no term among the Lean's seven**,
so the Lean does not prove exactly P1's proposition under exactly P1's hypotheses.

**③ NO CLAUSE IS VACUOUS.** The witness's horizon is non-empty and pinned to `{U = 0}`, the seven are
destructured from the theorem itself, and the tangency clause — the one conclusion that could have
been satisfied by having no point to test — is discharged **at** a named horizon point with a named
frame.

## AND TWO CLASSES THE ORDER DID NOT NAME, REPORTED BESIDE ITS THREE RATHER THAN FOLDED IN

- **`PROMOTED`:** P1 states `𝓗⁺ = ∂J⁻(𝒥⁺)` as part of its *hypothesis* ("with future event horizon
  …"); the Lean **proves** it, as the first of the seven. *The Lean is stronger than the proposition
  there, and a read that only looked for gaps would have missed it.*
- **`STATED-NOT-USED`:** P1 assumes `O` is **future-complete** with `O(τ) → i⁺`; the Lean takes only
  chronological ordering along `O` plus `I⁻(O) = D`. *P1 assumes more about its observer than the
  formalisation needs — not a gap in the Lean, but a fact about the proposition's hypotheses.*
- **And one encoding, not a gap:** P1's "D globally hyperbolic" is nowhere a separate Lean binder
  because `IsCauchyTemporalOn` carries it — its second conjunct is that every inextendible causal
  curve in `D` meets each level set exactly once, which is the standard equivalent. *Reported as an
  encoding rather than counted as missing, which is the difference between reading the definition and
  reading the binder list.*

**Running total of this seat's own rule conditions corrected by measurement or by another seat rather
than by reading, across `r7648`–`r7662`: thirty-two, with none added here.**
