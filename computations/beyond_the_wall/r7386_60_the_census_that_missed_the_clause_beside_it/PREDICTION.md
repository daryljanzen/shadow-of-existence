# r7386 (60) — THE CENSUS THAT MISSED THE CLAUSE BESIDE IT — registered before the scan

**Registered at this commit, before the scan is run.** The `S54` `Ⓑ⑥` repair is already in the working
tree, verified, and is not what this registers; what is registered is **how many more clauses of that
shape the corpus holds, and how many of them sit in a file that already carries the pin to fix them.**

## The finding this proceeds from

`r7383` `③` routes `70`'s ported fix to `S54` back to this seat to confirm or replace. **`70`'s form is
right and is confirmed** — it reads `scripts/receipt_scope.py` at the pinned commit `3f30509e` instead
of live, which is `r7368` `②`'s ratified rule, and `70` states it exits `0` before and after its own
change with all five `Ⓐ` checks `OK`.

⛔ **But the receipt was still red, on a clause `70`'s change never touched.** The trunk's own
`refs/ci/carry` ledger named `S54` with gate `Ⓑ⑥`, and the cascade is three deep: the runner-read sweep
failed → `S54` failed on exactly one gate → that gate runs `S23` and asserts it exits `0`. **`S23` is
green.** The failing conjunct is the third one:

```python
and not any(f.endswith(os.path.basename(s23))
            for f in git('diff', '--name-only', f'{REG}~1..HEAD').split())
```

*A range whose **base** is pinned and whose **head** is live. `r7370` pinned `S23`'s commit tuple, and
the clause went red for a later revision having done work — the gate failing on another revision's
success.*

⇒ ***AND `r7368` ALREADY FOUND AND REPAIRED THIS SHAPE IN THIS FILE.*** *The note it left four lines
above the constants says so in as many words:*

> *Three clauses below read the LIVE state of things this revision measured at a pin, and `r7368`
> found all three … and `Ⓓ①` read a diff whose base was pinned and whose HEAD was not. ⇒ **A range has
> TWO ends.***

**`Ⓑ⑥` is a fourth clause of that shape, and the note recording the census says "three".** It is four
lines of code from the pin that fixes it, in a file whose own docstring names the class.
  ⇒ *** A CENSUS OF A SHAPE INSIDE ONE FILE MISSED AN INSTANCE OF IT. ***  *Which is `r7368`'s own
      `S24` lesson one level up: there the repair and the diagnosis sat in the same gate and only one
      was applied; here the repair was applied to three gates and not to the fourth beside them.*

## The arms

Scoped to the tree at this commit, under `receipts/` and `corpus/`, over non-comment lines.

### ⒜ BASE-PINNED, HEAD-LIVE ranges — the shape itself

A git range whose left end is a pinned sha (a hex literal, or a name bound to one in the same file)
and whose right end is `HEAD` or a ref.

- central **8**, band **2–30**, two-sided.
- *Reasoning*: `r7368` repaired three here and `r7374` found the class closed at one map, so this seat's
  own receipts are mostly repaired. What I do not know is how many stand in the receipts this phase
  never touched, and the corpus has over twelve hundred files. Eight is a guess at one or two per
  prefix that uses pinned ranges at all.
- A result of **2** says `Ⓑ⑥` was nearly the last of it. Above **30** says the shape is the house habit
  and the repair belongs in a gate rather than in receipts one at a time.

### ⒝ the sharp one — of those, how many sit in a file that ALREADY binds a pin

- central **3**, band **1–10**, two-sided.
- *Reasoning*: this is the subset where the fix costs one identifier, because the file already carries
  a frame constant and simply does not use it on that clause. `Ⓑ⑥` is one and is certain, so the floor
  is **1**. ⇒ **This is the figure that says whether `Ⓑ⑥` is a slip or a pattern**: a high count means
  seats reach for the pin on the clause they are repairing and not on its neighbours.

### ⒞ the control — ranges with BOTH ends pinned

- central **20**, band **5–80**, two-sided.
- *Reasoning*: registered so ⒜ means something. If the repaired form dominates, the shape is residual
  and the repair is local; if the two are comparable, `r7368`'s rule has not reached the fingers.

### ⒟ `S54` itself — clauses of the shape it still holds after this repair

- **exact 0**, point prediction.
- *Reasoning*: the repair is in the tree and verified, so a non-zero result means I repaired the clause
  CI named and left another beside it — **the very defect this revision is about, committed by the
  revision reporting it.** It is registered precisely because that would be the worst outcome and must
  be checked rather than assumed.

## What is not claimed

**Not that `70`'s fix was wrong** — it is confirmed, and `r7383` `③` is answered by confirming it.
**Not that `Ⓑ⑥`'s claim was wrong** — the claim is historical, that `r7364` repaired nothing in `S23`,
and it is true; what was wrong is the range it was read over. **Not that a live range is always wrong** —
a restraint about work not yet landed is correctly live, which is `r7368` `②`'s own carve-out, so the
classification turns on whether the clause states a historical fact. **And not that the detector is
complete** — it reads range expressions on non-comment lines, so a range assembled by string arithmetic
two functions away is missed, which is stated rather than ruled out.

Written r7386 on `r7383` `③` and on the trunk's own carried red. Stated for reversal.
