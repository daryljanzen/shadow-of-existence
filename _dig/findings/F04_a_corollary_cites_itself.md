# F04 — P9 `cor:radiation` cites itself as the reason for its own claim, because a landed paragraph came to rest inside the environment instead of after it

*status: BOUNDED NEGATIVE (verified at source, this cut). One instance across 35 `.tex` files. Gate patch drafted: `DRAFT_check_compile_selfref.py`.*
*scope: `corpus/range_paper.tex` line 293 (P9, `cor:radiation`). Editorial; no physics is affected.*

---

## The sentence

`range_paper.tex` line 292 opens `\begin{corollary}[The wall is free gravitational radiation]\label{cor:radiation}`. Line 293 is the corollary's whole body, and inside it:

> *And the failure is sharp rather than gradual*, for the reason Corollary~\ref{cor:radiation}
> gives: a sweep deforms with fixed orientation, and the loss of the last confining isometry is
> precisely where a wave's polarization must begin to reorient from place to place.

`\end{corollary}` is line 294. So the corollary offers itself as the authority for its own claim.

## Why it is there, and it is not carelessness

`THE_LIVE_ARC` L-137, struck c54.108:

> ⌗ **LANDED c54.108 in P9 *after* `cor:radiation`: the domain statement, drawn as a consequence
> of the two corollaries in the same paper.**

The intent is explicit and correct — a paragraph *drawing on* `cor:wall` and `cor:radiation`, placed *after* them. What landed is the same paragraph placed *inside* the second one. Everything from *"One consequence for the reading, and it is the honest answer to a question the programme leaves standing"* to the end of line 293 is the L-137 landing; it reads as commentary on the corollary because that is what it is, and it is currently sitting where the corollary's own statement should be.

The corollary's proper body ends cleanly and identifiably at:

> ...With Corollary~\ref{cor:wall} this is one boundary read two ways: free radiation on the
> geometry side, dynamical inhomogeneous sources on the matter side.

## A second, smaller mis-target inside the same clause

Even relocated, the reference does not point where the argument lives. *"A sweep deforms with fixed orientation"* is not stated in `cor:radiation` — `cor:radiation`'s own version of the mechanism is *"a swept geometry depends only on its orbit-space coordinates while a free wave depends on the transverse coordinates through which it propagates."* The fixed-orientation argument is given in `\S`\ref{sec:open}, the **The wall.** paragraph:

> a sweep generates a deformation of *fixed* orientation, so a confined wave is self-consistent
> only while it propagates transverse to that orientation, and the loss of the last confining
> isometry is exactly the point at which the wave's polarization must reorient from place to place.
> **The rigidity of a single global sweep is what the wall is.**

So the sentence is reaching forward to §Scope, not sideways to itself.

## Proposed fix, stated for reversal

Three edits, all in `range_paper.tex`:

1. Move `\end{corollary}` to just after *"...dynamical inhomogeneous sources on the matter side."*
2. Run the remainder as ordinary text after the corollary — which is what L-137 recorded as the intent.
3. Retarget the reference. Two options, and the choice is the source's:
   - **"for the reason just given"** — cheapest, and correct once the paragraph follows the corollary; or
   - **"for the reason \S\ref{sec:open} gives"** — points at where the fixed-orientation argument actually is, at the cost of a forward reference.

I lean to the second because the sentence's content is the rigidity argument and that argument is stated once, in §Scope; but this is prose judgement and the paper's voice is not mine to set.

## The gate, because the class is cheap to close

`check_compile.py` already carries the precedent: the cross-paper label-collision check added at c54.94 exists because *"LaTeX never complains, because each paper compiles alone; the hazard is entirely in PROSE."* A self-reference is the same species — `\ref{cor:radiation}` inside `cor:radiation` is a perfectly well-formed reference, so `check_compile` reports **0 undefined refs** and is right to. Nothing in the suite looks at whether a reference resolves to its own container.

`DRAFT_check_compile_selfref.py` is a drop-in block in the file's own house style: walk each `.tex`, track theorem-class environments (`theorem`/`proposition`/`corollary`/`lemma`/`definition`/`remark`/`conjecture`/`claim`/`example`), collect the labels defined inside each, and fail on any `\ref`/`\eqref`/`\cref` within the environment that resolves to one of them.

Run across `corpus/*.tex` at this cut:

```
SELF-REFERENCING STATEMENTS: 1
  [FAIL] range_paper.tex:293  cor:radiation  cites its own label
```

**One instance in 35 files** — which is the useful part of the result. The corpus does not have a habit of doing this; it slipped once, in a paragraph landed three revisions before the bundle cut, and the gate would have caught it that turn.

⚠ **And the gate caught me, which belongs in the record.** On its first packaging the default target path was one directory short. It scanned **0 `.tex` files**, printed `SELF-REFERENCING STATEMENTS: 0`, and returned **rc=0** — a green gate that had looked at nothing. That is exactly the family F03 names: an instrument whose model of what it checks silently resolved to empty, and whose pass carried no information. Fixed, and the run line now prints the file count and the directory scanned, so an empty scan is visible in the output instead of being indistinguishable from a clean one. **Any gate landed from this batch should print what it looked at, not only what it found.**

## Not claimed

- No physics is affected. `cor:wall` and `cor:radiation` are both correct as stated and the landed paragraph is correct as written; only its placement and one cross-reference are wrong.
- No claim that the L-137 strike was wrong to land here — the strike's own note says *after* `cor:radiation`, so the register and the paper disagree and the register is right.
- No closure on any registered item; L-136 (where L-137's residue went) is untouched by this.
