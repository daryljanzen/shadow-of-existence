# r7374 (60) — THE KEY THE ENVIRONMENT CHOOSES — registered before the scan

**Registered at this commit, before the scan is run.** `r7370`'s repair to `S39` is already in the
tree, is correct, and is not what this registers. What is registered is **the reason written beside
it, which is false, and how far the real mechanism reaches.**

## The finding this proceeds from

`r7370` repaired `S39`'s `Ⓑ①` and wrote the cause beside it, twice over, in `S39` and in `S56`:

> *`Ⓑ①` below took each commit's session marker out of `G._SESSION`, which the collision gate fills
> by WALKING THE WHOLE HISTORY REACHABLE FROM `HEAD`. On a shallow clone that walk stops at the
> horizon … these six commits sit some eighty revisions back. So the map has no entry for them.*

**Three measurements say that cannot be what reddened it.**

* ⒤ **No job that runs a receipt is shallow.** Read out of `.github/workflows/gates.yml` at the
  commit the red was recorded against (`cdc16410`), at the commit that carried the second repair
  (`4cb449fe`), and on `origin/main` now: `fast`, `receipts`, `index`, `backstop`, `scope-suite`,
  `scope-reads` and `scope-tolerance` all check out with `fetch-depth: 0`. The one default-depth
  checkout is `compile`, which runs LaTeX and no receipts.
* ⒥ **All six pinned shas are ancestors of the trunk**, so they are reachable from `HEAD` at any
  depth on any branch based on it.
* ⒦ **The signature reproduces here, from a different variable.** The gate builds `_SESSION` with
  `git log --format=%h…` and looks a sha up in it by exact string. `%h` is *git's* abbreviation, and
  git picks its length from the object count unless `core.abbrev` says otherwise. Running the gate's
  own map-building command at four lengths:

  | `core.abbrev` | key length | of the six pinned shas, found |
  |---|---|---|
  | unset (this clone) | 8 | **6 of 6** |
  | 7 | 7 | **0 of 6** |
  | 9 | 9 | **0 of 6** |
  | 12 | 12 | **0 of 6** |

⇒ *** A PIN KEYED BY AN ABBREVIATION IS KEYED BY SOMETHING THE ENVIRONMENT CHOOSES. *** *Same tree,
same commits, nothing edited — and the map misses **all six** the moment the length is not this
clone's. That is exactly "the map has no entry for them", produced by a variable that has nothing to
do with depth.*

⌗ **And it corrects a rule, not just a comment.** `r7371` `②` recorded, from `r7370`'s own line, that
*"the container is not the instrument for a claim about the runner."* The claim about the runner was
decidable in the container twice over: the workflow file names every checkout's depth, and
`core.abbrev` reproduces the failure signature on this tree. ⇒ **The rule holds for a claim about
what the runner HAPPENS to have; it does not hold for a claim about what the code DEPENDS ON.** The
second is a property of the code and is always readable where the code is.

⚠ **What this does not claim**: *that the runner's abbreviation length is `7`, or any value.* I cannot
see it from here, and asserting it would be the very move being corrected. The defect is that the
lookup is an exact string match against a length the environment picks — which is wrong whatever
that length turns out to be, and which the two independent measurements above leave as the only
mechanism still standing.

## The arms

Scoped to the tree at this commit, under `receipts/` and `corpus/`.

### ⒜ CONSUMING sites — code that takes git's abbreviated OUTPUT and matches it as a string

A site that passes a short sha *to* git is safe: git resolves a prefix. The defect is consuming
`%h`, `--short` or `--abbrev` output and then comparing it to a literal, keying a dict by it, or
looking one up in such a dict.

- central **3**, band **1–10**, two-sided.
- *Reasoning*: the collision gate's `_SESSION` is one and is the one that fired. The house habit in
  this corpus is to pass a short sha as an argument and let git resolve it, which is why the class
  has survived unnoticed; I expect a small number of consumers and would not be surprised by one.
- A result of **1** says the gate was the whole class. Above **10** says consuming `%h` is the house
  habit and the repair belongs in a gate rather than in receipts.

### ⒝ the gate layer — `corpus/check_*.py` that key a map by an abbreviated sha

- **exact 1**, point prediction.
- *Reasoning*: `check_revision_collisions.py` is the one I have read. A second would mean the class
  is in the gate layer rather than in one gate, which changes who owns the repair.

### ⒞ this seat's own pinned sha constants — how many are NOT 8 characters

- **exact 0**, point prediction.
- *Reasoning*: every pin this seat has written was copied from this clone's `%h`, and this clone
  renders all 5,539 revision-numbered commits at length 8 — uniformly, with no other length
  anywhere in the log. So the pins agree with this environment and with no other, which is the
  finding stated as a property of the corpus rather than of one gate. A non-zero result would mean
  some pin was written from a different source and is worth knowing about.

### ⒟ the control — sites that pass a short sha to git as an ARGUMENT

- central **40**, band **15–120**, two-sided.
- *Reasoning*: registered so ⒜ means something. If the immune form outnumbers the vulnerable one by
  a wide margin, the class is narrow and the repair is local; if the two are comparable, the habit
  is not what I think it is and the finding is larger than one gate.

## What is not claimed

**Not that `r7370`'s repair was wrong** — it reads each marker off the commit by id and never touches
the abbreviated map, so it is immune to this and to depth alike. The claim is narrower and worse: it
worked for a reason other than the one written beside it, and the written reason is in two receipts.
**Not that abbreviating a sha is wrong** — it is how this corpus cites commits, and as a git argument
it is exact. The defect is in consuming git's abbreviation as a key. **Not that the detector is
complete** — it reads a fixed set of spellings on non-comment lines, so a consumer that routes the
output through a variable two functions away is missed, which is stated rather than ruled out.
**And not that the classification is mechanical** — `CONSUMING` / `ARGUMENT` / `ABOUT` is assigned by
a committed rule in `cost.py`, and an unclassified site defaults to `CONSUMING`, the direction that
counts against this seat.

Written r7374, on the trunk's own carried red for `S39`. Stated for reversal.
