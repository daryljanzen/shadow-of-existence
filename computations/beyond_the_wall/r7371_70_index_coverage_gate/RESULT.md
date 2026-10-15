# r7371+70 — RESULT (registration `ab85053e`)

| arm | registered | measured | verdict |
|---|---|---|---|
| **Y-a** gate wall, min of 5 | `0.05` s (`0.01`–`0.5`) | **`0.19`** s (max 0.38) | **HOLDS** (in band, 4× the central: it imports the runner to list registered receipts) |
| **Y-b** tree receipts the index lacks | `221` (`200`–`240`) | **`232`** NEW, **`0`** GONE | **HOLDS**. 66's `233` was 232 + 1; there were no renames to pair, so my "less 12" reasoning was wrong and the band carried it |
| **Y-c** most receipts added to `main` in one UTC day, 30 days | `25` (`10`–`60`) | **`25`** (2026-09-28 and 09-29; 27 days, 326 receipts, mean 12.1) | **HOLDS, at the central** |
| **Y-d** the gate on today's tree and index | RED | **RED**: NEW 232 > 25 | **HOLDS** |
| **Y-e** ④ a cheaper exact route exists | yes | **yes** (below) | **HOLDS** |
| EFFORT (r7371 ⑤ ② + ④) | `45` min (`20`–`90`) | **≈ 5 min** (18:12 → 18:17 UTC, by the commit and system clocks) | **REFUTED LOW**: the measurements were cheaper than the band assumed, mainly because the API history and `load()` answered the premise directly |

## ⛔ The premise of ⑤ measured, and it is two findings, neither of them the one stated

**1. The 232 are under-scoped, not invisible.** `scope()` iterates `idx`, but `idx` is `load()`'s output,
and `load()` walks the **registered** receipts (`registered(root)`, line 262), not the index. A receipt
the index lacks gets an entry built from its **static names**: its source's file names and imports,
bounded by `repo_names`. Measured: `load()` returns **1103** entries for 1103 registered receipts.
For S55 and S56:
- **in idx:** True;
- **a push editing the receipt scopes it:** True;
- **a ledger edit scopes it:** False. Neither names the ledger in source.

What the lag loses is a receipt's **traced** reads: run-time paths, glob membership, and modules
imported by modules. That is a real gap, which the coverage gate now bounds, but it is not a fifth of
the corpus outside CI.

**2. What let S55's and S56's keys reach the trunk is a skipped step, not the index.**
- `check_quote_pins` runs in the **fast** job on every push, and it reads no index.
- The fast job has two steps: "the register and view checks" (the regen `--check`s), then "the text
  gates", which holds `check_quote_pins` and ~120 others. The second step had no `if:`, so it ran only
  on `success()`.
- `regen_grain_currency` went stale at **`5d3d40b6` (15:38 UTC today)**. From that push on, every main
  push reads `failure/skipped`: `5d3d40b6`, `688a59fc`, `0aa2f781`. Before it, `b4eb552a` reads
  `success/success`.
- **So no text gate has run in CI since 15:38**, and S55 and S56 landed in that window. *It is r2692's
  lesson one level up:* the regen step collects its failures so that one red hides none of the rest,
  and the step boundary hid all of them.
- **Fixed here:** `if: success() || failure()` on the text-gates step. Both steps run, and the job
  still fails if either does. The stale grain-currency block itself is not mine: it is red on `main`
  and routed to 66.

## The coverage gate (② as ordered), `corpus/check_index_coverage.py`

- **The test:** NEW (registered, not indexed) and GONE (indexed, not registered).
- **The tolerance:** a **count, 25 each**. The judgement: a day's additions, not a push's. The index
  can be no fresher than its nightly refresh plus the commit after it, so a correct process lags by up
  to one day's additions, and the measured daily maximum is 25. A day bound would be the header's own
  `max_age_days` note again.
- **Price:** 0.19 s here (Y-a). Per W-c's rule, that is a property of this container.
- **Not wired into the fast job yet.** It is red today by design (Y-d). Wiring it now would turn every
  seat's fast job red for a cause tonight's index removes. It is wired in the **same commit that lands
  the refreshed index**, by the 11:00 UTC nightly read, and only if it reads green against that index.

## ④ — yes, a cheaper exact route

`_present_at` starts one `git show` per (commit, file) and, for a non-PAPER key, one `git grep` per key
and commit. A census over all 2,656 keys should:
- group the keys by the commit they are held at;
- read each distinct target file **once per commit** through a single `git cat-file --batch` process;
- answer every key against that in-memory, `_flat`-normalised text.

At HEAD it needs no git at all: read the working tree. Each check stays exact; the saving is in
subprocess starts and repeated reads, not in what is compared. *Not timed here: this answers whether a
cheaper exact route exists, it does not price it.*
