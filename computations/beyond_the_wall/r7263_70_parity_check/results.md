# `r7263+70.1` — results: `B1` ⓸ᵇ measured distance from `main`; it now judges the band of the node running it

*Pre-registered at `PREDICTION.md` (`9607d0c9`). The script is `seeds.py`, and its output is `seeds.txt`.*

## Six built repositories, OLD ⓸ᵇ against NEW

| seed | runner | commits on top | OLD | NEW |
|---|---|---|---|---|
| P1 | `60` | none | 0 | 0 |
| P2 | `60` | `r4000` | **1** | **0** |
| P3 | `60` | `r4000 r4002 r4004` | **3** | **0** |
| P4 | `60` | `r4000 r4002 r4003` | **2** | **1** (`r4003`) |
| P5 | `66` | `r4001 r4003` | 0 | 0 |
| P6 | `ci` | `r4000 r4002` | 2 | **None**, reported |

Every pre-registered row came out as stated.

- **The OLD count equals the even-commit count on every seed**, so it measured distance from `main`.
- **The NEW count is 0 on every in-band seed and flags exactly the one odd commit in P4**, which is the prevention
  firing.
- The negative does not fire.

## 60's case, reproduced on the real receipt

In a worktree of `origin/main` plus one empty commit `r7264` with no content, under `NODE=60`:

- the OLD `B1` fails ⓸ᵇ with **1 violation(s)**;
- the repaired `B1` passes with **0**.

## The repair

`B1` now captures the caller's `NODE` as `_RUNNER` before its own `NODE=60` override, which the seed needs. ⓸ᵇ
judges the live tree at `_PARITY_BY_NODE[_RUNNER]`. A runner with no half (`ci`, `70`, `cc66`, `71`, unset) is
reported, and nothing is asserted about the live tree. That matches what `band_violations` itself does, and the
prevention stays in the seeded repository below it.

Results on this tree:

| receipt | runs | gates |
|---|---|---|
| `B1` | `NODE=ci`, `60`, `70`, and unset | all green |
| `L261/A1` (shells out to `B1`) | `NODE=ci` | green |
| `L259/D1` | `NODE=ci` | green |

⌗ *The tolerance job's two reds were on 60's branch, and I cannot run that branch here. The reproduction above is the
same mechanism on the same file.*
