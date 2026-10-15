# r7368 (60) — THE BASE THAT MOVED — registered before the measuring pass

**Registered at this commit, before the scan is run.** The three repairs that found the class are
already in the tree and are not what this registers; what is registered is **how far the shape
reaches**, which nothing has counted yet.

## The finding this proceeds from

A gate measuring a population over a git revision range must name the range's base. Two of this
seat's receipts named it `origin/main` — `P03`'s restraint and `S5`'s authorship bound. `r7364`
landing on the trunk moved that ref, and the population fell from **52** of this seat's commits to
**2** with no edit anywhere in the tree. Five gates across four receipts went red on a **merge**.

`S5` carries the repair note three times over — `r7214` (the trunk moving), `r7222` (this seat
adding a file), `r7245` (another seat's work entering the range) — and each one states the same
safety argument in writing:

> *monotone in the safe direction: as the trunk absorbs this work the set SHRINKS.*

**Shrinking is the safe direction for the restraint and the fatal one for the restraint's own
non-vacuity, and both were read off one population.** The restraint says nothing in the range is
unauthorised, which an empty range satisfies. The non-vacuity control says the range holds
crossings at all, which an empty range makes false. So the previous repair's own written safety
argument is the defect, stated in the direction it was proved safe in.

`S23`'s `Ⓕ①` had already adopted the right property — *a base must be a literal sha that resolves
and is an ancestor of `HEAD`* — and checked it as the single expression `merge-base HEAD
origin/main` on the two receipts the shape was found in. It walked past that control into `P03` and
`S5` under the spelling `--not`.

## The arms

### ⒜ the population — how many MEASURING sites beyond the two known

Every site under `receipts/` where a revision range's **base end** is a ref name, classified
`MEASURING` / `FIXTURE` / `ABOUT`; only `MEASURING` counts. `P03` and `S5` are the two known, and
are excluded from the figure.

- central **3**, band **1–7**, two-sided.
- *Reasoning*: 19 files mention `origin/main`; most bind a literal sha to a constant and name the
  ref only in a comment, which is the repaired form. The spelling that hid from `S23`'s control was
  `--not`, and `--not` is rare. I expect a handful and not a sweep.
- A result of **0** would say the two were the whole class and that `S23`'s one-expression control
  was adequate after all. A result above **7** would say the property was never enforced anywhere.

### ⒝ the gate layer — how many `corpus/check_*.py` test a range's base

- central **0**, band **0–0**, a point prediction.
- *Reasoning*: the same shape as `r7364`'s arm ⒞, which was also a point prediction at 0 and was
  exact. The gate layer reads spellings and ledgers; nothing in it has ever been shown to read a
  revision range at all.

### ⒞ the spellings — how many distinct ones the MEASURING sites use

- central **2**, band **1–4**, two-sided.
- *Reasoning*: `S23`'s control covers exactly one (`merge-base`). `--not` is the second, found here.
  `<ref>..` is the obvious third. More than four would mean the detector is matching prose.

## What is not claimed

**Not that a pinned base is always right** — a restraint about *work not yet landed* is correctly
live, and shrinking is correctly safe for it; the defect is reading the non-vacuity off the same
population. **Not that the detector is complete** — it reads four spellings on non-comment lines and
will miss a base built by string arithmetic, which is stated rather than ruled out. **Not that the
classification is mechanical** — `MEASURING` / `FIXTURE` / `ABOUT` is assigned by hand, committed in
`cost.py`, and an unclassified site defaults to `MEASURING`, which is the direction that counts
against me.

Written r7368 on the sweep's own finding. Stated for reversal.
