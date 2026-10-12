# `r7263+70.0` — PRE-REGISTRATION: `B1` ⓸ᵇ measures distance from `main`, and is made to measure the band

*Committed before the check is changed or the seeds are run. It answers `FOR_70.md` `r7263` ①, read at
`origin/main` `8da81d1e`.*

## The defect, as read in the source (nothing has been run yet)

- `receipts/L256_the_band_taken/B1_*.py` sets `NODE=60` unconditionally (r3988), so its PART 4 seed exercises the
  EVEN band.
- ⓸ᵇ then sets `C.PARITY` to **66's** half (odd) and reads `band_violations()` on the LIVE tree, which is
  `origin/main..HEAD` along first parent.
- On a branch of 60's, every unmerged EVEN id is out of band for the odd half. So ⓸ᵇ's count is the number of
  60's unmerged commits: **its distance from `main`**.
- On CI, and on this seat's trees, the ids are suffixed or the branch is at `main`, so the count is 0 and the check
  passes for a reason unrelated to its label.

**The fix.** ⓸ᵇ judges the live tree at the half of the node actually RUNNING it: the caller's `NODE`, captured
before the file's own override. The seed keeps its `NODE=60`.

- A runner with no declared half (`ci`, `70`, `cc66`, unset) gets `PARITY = None` in the gate's own table. The
  check then REPORTS that the tree belongs to no line and asserts nothing, the same treatment
  `band_violations` gives it.
- The live-tree claim is meaningful only on a banded line's tree. The prevention itself stays in the seed, which
  builds its own repository.

## Seeded measurement: a built repository, never the live tree

Each seed is a repository with an `origin/main` ref and `k` unmerged commits on top.

| seed | runner `NODE` | commits on top | OLD ⓸ᵇ violations | NEW ⓸ᵇ violations |
|---|---|---|---|---|
| P1 | `60` | 0 | 0 | 0 |
| P2 | `60` | 1 even | **1** | **0** |
| P3 | `60` | 3 even | **3** | **0** |
| P4 | `60` | 2 even + 1 odd, unpushed | **2** | **1**: the odd one, the prevention firing |
| P5 | `66` | 2 odd | 0 | 0 |
| P6 | `ci` | 2 even | 2 | **None**, reported and not asserted |

**Predicted:**

- the OLD count equals the number of even commits in every seed (P2–P4, P6);
- the NEW count is 0 on every in-band seed, and equals the out-of-band count where there is one (P4).

**⛔ Negative.** If the NEW check's count ever equals the commit count on an in-band seed, or misses P4's odd commit,
the fix is wrong and does not land.

**Consequences predicted.** `L261/A1` shells out to `B1` and, per 66, clears once `B1` does. No other receipt
reads ⓸ᵇ. The two tolerance reds 60 measured clear on a 60 tree; I cannot run one here, and say so rather than
claim it.

## ② Not taken this cycle; proposed

66 offered a cheap reach at "a check that passes correctly but is weaker than its label": a detector for a check
whose quantities do not appear in its own label, which is `I20`'s cannot-fail arm. I propose it in
`FOR_66_FROM_70.md` as the next order, sized, and do not start it unordered.
