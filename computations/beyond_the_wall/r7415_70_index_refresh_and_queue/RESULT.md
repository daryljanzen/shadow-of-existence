# r7415+70 — RESULT (registration `e7c5dffe`)

## ① The index, refreshed, and the gate wired

The artifact `READ_INDEX` comes from nightly run `38870027067`, traced at `615a6ef6` on 2026-10-15. It was
committed as `receipts/READ_INDEX.json`: **871 → 1107 receipts**, with `red_under_trace 1` (L257 V1) and
`timeouts 0`. `check_index_coverage` now reports **NEW 0, GONE 0**, against 1107 registered, and exits 0. It
joins the fast job's text-gates loop in the same commit (`r7415+70.1`). The tolerance stays at `25`.

⌗ From now on the gate turns red when nobody commits a nightly artifact for about two days at the measured
growth rate. That is the failure it exists to catch, and the remedy it prints is still the right one.

## ③ The fast-tier re-measure

| | band | measured | verdict |
|---|---|---|---|
| **Q-a** median minutes to `fast` complete | `6`–`20` | **`154.9`** for the last 30 overall; **`70.2`** for the 8 created after #463 | **REFUTED HIGH** |
| **Q-b** worst | `15`–`60` | **`178.1`** after #463 (`295.3` overall) | **REFUTED HIGH** |
| **Q-c** never concluded, of 30 | `0`–`3` | **`0`** | **HOLDS** |

The raw runs are in `QUEUE_RUN.txt` (the r7383 instrument, unchanged) and `QUEUE_SPLIT.txt` (`queue_split.py`).
The split adds the cut at #463's merge (01:07:54 UTC) and the wait from run creation to the fast job's start.

**What the numbers say.**

1. **r7383's "9 of 30 never" were backlog, not losses.** All nine concluded, the last of them after waits of
   4–5 hours (`7e4cd48b`: 277.7 min queued, done at 294.6). `main` never cancels a run, so a backlog on `main`
   drains one run at a time and every run in it waits behind the rest. Q-c holds for that reason. Nothing was
   dropped.
2. **The "after #463" median of 70.2 is mostly the pre-fix backlog draining.** The first post-merge run
   waited 161 min. Waits then fell monotonically: 94, 93, 81, 35, 1.6, 4.9, 0.0. The **three runs created
   after the queue emptied (04:13–05:05 UTC) completed in 11.6, 15.7 and 11.0 min**, inside Q-a's band. I
   registered the band over the whole 30-run window, so it is refuted as written. The steady-state reading
   is `n = 3` and is reported, not scored.
3. **Not measured yet:** the steady state under contention. No push reached `main` between 05:05 and the
   nightly's 07:53 start, so this window says nothing about a push landing while the heavy and index jobs
   hold runners. The next re-measure should be taken after a working day that crosses the nightly.

**The cost of `main` never cancelling is now measured, and it is a ruling, not a fix.** Yesterday evening 22 runs reached `main` between 18:12 and 23:53 UTC, about 4 an hour, faster than they drained. It did not clear until about
4 h after the pushes stopped. Cancelling superseded `main` runs would have bounded that, but the standing rule
forbids it, and I am not changing the rule.

## EFFORT

The pre-registration said 15 min. The measured span was about 30 min, 11:16 → ~11:45 UTC. The extra
time went to the split script, which became necessary once the raw median turned out to mix two regimes.
