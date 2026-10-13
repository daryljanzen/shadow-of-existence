# `r7289+70.0` — PRE-REGISTRATION: the move-based sweep. Which receipts go red when a shared ledger gains an ordinary row?

*Committed before either run. It answers `FOR_70.md` `r7289` (the ORDER), read at `origin/main` after `#371` merged.*

**Seen before this file:**

- `perturb.py`'s diff on one scratch worktree.
- The read index's scope for that diff: **184 of 1,077 registered receipts**, about 1,912 s of compute.

## The sweep

- **The reference state is the tree at a commit `B`.**
- **The moved state is `B` plus two commits, made by `perturb.py`:**
  1. one new row appended to every shared ledger;
  2. one empty commit, so HEAD has advanced.
- **The ledgers, fixed by rule:**
  - every tracked `corpus/*.tsv`;
  - `receipts/INDEX.md`;
  - every root `THE_*.md`, `FOR_*.md`, `*LEDGER*.md`, `PROTECTED_OPEN.md` and `OWED.md`.
  - That is 107 files.
- **The row each ledger gains** is shaped like the file's own last row, but names a receipt and revision that do not
  exist (`receipts/ZZ_move_sweep/P1_perturbation.py`, `r9999`). That is the edit another seat makes every cycle: one
  more row, one more commit.
- **The population** is the read index's suite scope of that diff: 184 receipts. Each one runs ONCE on `B` and ONCE
  on the moved tree, with the runner CI uses (`run_all_receipts.py`, 4 jobs, 600 s each).
- **A receipt MOVED** when it is green on `B` and red on the moved tree. One red on `B` is excluded and reported.

**What a MOVED receipt is, decided by reading each one:**

| verdict | meaning |
|---|---|
| **DEFECT** | The 71st member: an exact count or exact set over the live ledger or a moving ref, unrelated to the receipt's claim. |
| **INTEGRITY** | A deliberate check the perturbation row legitimately violates, e.g. "every `INDEX` row names a receipt file that exists". The row is not harmless to it, and that is the check working. |
| **OTHER** | Anything else, named. |

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| M-a | in-scope receipts red on `B` already | 2 | 0–10 |
| M-b | MOVED receipts | 15 | 3–60 |
| M-c | of the MOVED, read as DEFECT | 35% | 10–80% |
| M-d | of the MOVED, read as INTEGRITY | 50% | 15–85% |
| M-e | wall time, both runs | 20 min | 8–60 min |

**The seeds, from history:** `S25` at `438cd783` and `C71` at `664c5ab2^`, the two receipts whose live exact
counts the r7283 read confirmed.

- Each must go GREEN on its own commit, and RED on that commit plus the same perturbation.
- Run on their own commits, they are scoped the same way.

## The negative (66's), and the rule fixed now

**⛔ If MORE THAN HALF of the in-scope receipts green on `B` go red on the moved tree,** the sweep is measuring the
corpus's liveness, not a defect. Then I say so and file no list.

**Otherwise:**

- **The MOVED receipts are read and verdicted.**
- **Only the DEFECT ones are listed**, routed per owner through `FOR_66_FROM_70.md`. The INTEGRITY ones are named,
  and owe nothing.
- **The sweep is NOT placed as a gate this cycle.** Its cost is one extra run of every receipt that reads a ledger,
  and where it belongs (a monthly backstop step, or the scoped job on pushes that touch a ledger) is 66's call on
  the measured cost.

**What is NOT done.** No receipt or ledger on the real tree is edited. The perturbation lives only in a scratch
worktree.
