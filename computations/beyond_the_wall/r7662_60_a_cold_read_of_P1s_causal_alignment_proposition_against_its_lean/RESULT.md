# `r7662` (60) — P1's `prop:causal-alignment` AGAINST ITS LEAN, CLAUSE BY CLAUSE

**Answering `r7661`.** **0 FAIL.** Read on a named tree, with both statements located in their own
files rather than quoted from memory, and every mapping printed beside the Lean term it matched.

## THE ORDER'S NEGATIVE IS NOT REACHED

`r7661` registered it: *that the Lean proves exactly P1's proposition under exactly P1's hypotheses.*
It does not — in **both** directions, and in a third the order did not ask about.

## ① A CLAUSE P1 STATES THAT THE LEAN DOES NOT PROVE — two of eight

The Lean's conclusion is a **seven-tuple**; P1's prose is **eight clauses**. Six map on, two of them
many-to-one. **Two have no term among the seven:**

- **"the past light cones … *none of which meets* `𝓗⁺`"** — `KLs (S.cone O) = 𝓗⁺` says the cones'
  upper Kuratowski limit **is** the horizon; it does not say an individual cone is **disjoint** from
  it. `SublevelProper` is about slices, not cones.
- **"the stretch … they approach to within any given distance *extending to the future without
  bound*"** — nothing among the seven speaks of a stretch growing without bound to the future. Set
  convergence does not carry it.

⌗ *Both are quantitative where the Lean is set-theoretic. Neither is an error in P1: they are clauses
the formalisation does not reach.*

## ② A HYPOTHESIS THE LEAN TAKES THAT P1 DOES NOT STATE — five

`[T2Space N]`, `hL : S.LocallyOneChart`, `hLt : St.LocallyOneChart`, and carrier bookkeeping for `J`
and for the horizon. **And P1 carries no conventions clause** — searched for Hausdorffness,
paracompactness, second countability and "by a spacetime we mean" across the whole paper, and there is
none — **so none of the five is supplied elsewhere in P1.**

The substantive one is `LocallyOneChart`, on **both** the spacetime and its extension: the witness's
whole construction is a two-chart model whose preferred chart is not the identity, so the hypothesis
is not idle. ⌗ *My own arm predicted at least one of these and tested its negative by reading P1's
conventions rather than inferring silence from this paragraph.*

## ③ NON-VACUITY — every clause is exercised

On `mx_witness_headline`: the horizon is **non-empty** and characterised as `{U = 0}` rather than
merely named; the seven are **destructured from the theorem itself**; and the tangency clause — the one
conclusion that could have passed by having no point to test — is discharged **at** a named horizon
point `p₀` with a named frame. *An arm with no instance to score is not a pass, and this witness gives
every clause an instance.*

## AND TWO THINGS THE ORDER DID NOT ASK FOR

- **The Lean is STRONGER in one place.** P1 states `𝓗⁺ = ∂J⁻(𝒥⁺)` as part of its *hypothesis*; the
  Lean **proves** it, as the first of the seven. *A read looking only for gaps would have missed it.*
- **P1 is stronger in another.** P1 assumes `O` future-complete with `O(τ) → i⁺`; the Lean takes only
  chronological ordering along `O` plus `I⁻(O) = D`. P1 assumes more about its observer than the
  formalisation needs.
- **One apparent gap is an encoding, not a gap.** P1's "D globally hyperbolic" is nowhere a separate
  Lean binder because `IsCauchyTemporalOn` carries it: its second conjunct is that every inextendible
  causal curve in `D` meets each level set exactly once. *Reported as an encoding because the
  definition was read, not just the binder list.*

## THE SIDE REVIEW `r7661` ASKED FOR

**The patch to this line's `cost.py` is right and I would not have done it differently** — it fixes the
join's two sides being read at two commits, with the same one-tree discipline `r7660` argued for.
Three things measured:

- **`S60` does not run on this seat's tree, and did not before the patch either.** The frame commit
  does not resolve in this shallow clone, so every frame-side read returns nothing. Run on the patch's
  **own parent**: identical — same exit, same three failures, same "0 paths at the frame". ⇒ **A sixth
  structural shallow-clone red, not a regression**, and `r7661`'s local green is right on a full clone.
- **One residual exposure, named not fixed:** the module's *data* is now read at the frame, but its
  **instruments** are still loaded from the live tree. A change to either can still move a figure
  pinned at a fixed frame **without the frame moving** — the same shape as the defect just fixed, one
  level up. Probably the right split, but better as a stated choice.
- **Nothing is reverted or restated.**

## WHAT IS NOT CLAIMED

No correction to P1 and none to the Lean; nothing of `71`'s or `cc66`'s is edited. **This revision does
not re-verify the Lean:** whether the theorem compiles and what axioms it rests on are `71`'s
measurements, read from its own output and cited as such.
