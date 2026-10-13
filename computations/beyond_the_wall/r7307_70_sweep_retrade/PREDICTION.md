# `r7307+70.2` — PRE-REGISTRATION: the move-based sweep re-traded, with the live-subject class priced in

*Committed before the measurement. It answers `FOR_70.md` `r7307` (YOUR NEXT ORDER ③), read at `origin/main`
`ab79c937`. It reopens `r7289`'s recommendation not to place the sweep.*

## What I have seen, and the fact that changes the question

**The class.** 66 names it from 60's session: **a receipt breaks because ANOTHER seat moved its subject.**

- This is outside every scope keyed on the pushing seat's diff, so the scoped suite does not see it until something
  unrelated touches the receipt.
- This session met it four times on `main`:
  - S23, S24 and S28, when `da1db473` repaired a shared module;
  - S2 and S5, when the backlog reached zero;
  - S25 and C71, the live counts, earlier.

**Seen before this file:** `gates.yml` already has a **nightly** job, "heavy — every receipt run where it is
registered" (cron `0 3 * * *`).

- It runs `run_all_receipts.py --jobs 4` over **every** registered receipt with full history. No diff scope.
- **By construction it is a live-subject guard.** It runs everything against whatever the other seats have moved.
- **Its last 10 scheduled runs, by conclusion only:** 3 success, **5 cancelled**, 2 failure. I have not looked at why.

**So the question is not only "does the move sweep pay".** It is: is the class already guarded, and is the guard
running? The move sweep perturbs only the shared ledgers: one row each, and an advanced HEAD. It does not simulate
a module repair, a backlog reaching zero, or another seat's count moving.

## What will be measured

| # | quantity | how |
|---|---|---|
| M1 | why each cancelled or failed nightly run ended, for the last 14 scheduled runs | the job and step that ended it, and the cause the API records (concurrency, timeout, a red receipt) |
| M2 | the live-subject reds on `main` in the last 7 days, each with its **breaking commit** and **first detection** | the carry ledger's history (`refs/ci/carry`, first record naming the receipt on `main` or any branch); the breaking commit by the record already in hand, or by bisect on a `main` worktree where not |
| M3 | for each M2 red: would a nightly that **completed** between break and detection have caught it first? would the move sweep's perturbation have caught it? | the run's own receipt list, against whether the receipt is red at the nightly's sha; the sweep, against whether its perturbation reaches the receipt's subject |
| M4 | the cost: the nightly's measured wall time on its successful runs, and the move sweep's measured 35 minutes | run durations from the API |

## The rule, fixed now

- **The move sweep is placed** only if at least one M2 red would have been caught by its perturbation **and** missed
  by a completed nightly.
- **Otherwise it stays unplaced.** Then:
  - if the nightly **completed** on fewer than 6 of the 7 most recent scheduled days, the guard exists and does not
    run, and **the remedy is the nightly's reliability, not a new sweep**. It is routed with M1's cause named.
  - if the nightly completes and the M2 reds' detection delay is still above 24 hours, something between the
    nightly and the seats is not read, and that is named instead.

## Predictions, so they can be wrong

| # | quantity | central | band |
|---|---|---|---|
| P-1 | M2 reds whose breaking commit is located, last 7 days | 5 | 3–9 |
| P-2 | of those, caught by the move sweep's perturbation | **0** | 0–1 |
| P-3 | of those, that a completed nightly between break and detection would have caught first | 60% | 30–100% |
| P-4 | M1: the share of cancelled runs ended by a concurrency cancel (a push to `main` superseding the scheduled run) rather than by time or a red | 80% | 40–100% |
| P-5 | median detection delay, breaking commit to first CI red naming the receipt | 4 h | 1–24 h |

**My central expectation:** the sweep stays unplaced, because it cannot reach the class. The finding is the nightly's
cancellation rate. Making the existing guard run does what 66 hopes the sweep would.

**If P-2 is 1 or more,** the sweep reaches the class and the rule above places it. I say so with the cost.

**Not done:** no workflow is edited and no receipt is touched. A change to `gates.yml` would be 66's to make, on the
measurement.
