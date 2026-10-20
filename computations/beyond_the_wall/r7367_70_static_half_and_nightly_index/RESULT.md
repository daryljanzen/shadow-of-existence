# r7367+70 — RESULT (registration `506f3f61`; the change at `1e861909`)

| arm | registered | measured | verdict |
|---|---|---|---|
| **W-a** ledger `suite` scope, structural form, at HEAD | `50` (`45`–`60`) | **`50`** | **HOLDS** |
| **W-b** that scope, form as committed (control) | `5` (`5`–`5`) | **`5`** | **HOLDS** |
| **W-c** min-of-3 `load()`, structural / committed | `1.18` (`1.05`–`1.35`) | **`1.03`** (2.55 s / 2.49 s) | **REFUTED LOW** |
| **W-d** `index` job runner time, first nightly | `46` min (`35`–`70`) | **`81`** min (run `38870027067`, 07:53:05 → 09:14:25 UTC) | **REFUTED HIGH** |
| **W-e** heavy wall that night | `101` (`90`–`115`) | **`113`** min (07:53:05 → 09:46:21 UTC; `RUN_RESULT` 1100 pass, 1 fail, 6 over timeout, 6601 s) | **HOLDS** (under the `127` budget) |
| EFFORT (r7367 ③–④) | `40` min (`20`–`90`) | **≈ 41 min** (15:38 → 16:19 UTC) | holds |

**W-d/W-e, scored at the r7415 nightly read (11:00 UTC 2026-10-16).** The `index` job ran 81 min against a band
drawn as half a heavy run. The band was wrong because a trace runs every receipt under instrumentation; it does not
run the cheap half. The job's conclusion was `failure` because its one traced red, L257 V1 (cc66's, already routed),
carries through. Its artifact was uploaded anyway, and that is what the job is for. Committed at `r7415+70.1`:
index **871 (`404bc95b`, 2026-09-28) → 1107 (`615a6ef6`, 2026-10-15)**, `red_under_trace 1`, `timeouts 0`. The heavy
job running alongside it took 113 min and stayed inside its budget, so running the two together costs no deadline.

**The second nightly, read at `r7439+70.1` (11:10 UTC 2026-10-17); a record, not a re-score.** Run `39013928966`
at `b7095942`. The `index` job took **115.6** min (07:31:08 → 09:26:44 UTC). That is the second reading above the
registered band, and the trace grows with the receipt count. Its conclusion is `failure` for the same reason as
before: the sweep step carries L257 V1's red. The artifact was uploaded and committed here: index **1107
(`615a6ef6`, 2026-10-15) → 1109 (`b7095942`, 2026-10-16)**, `red_under_trace 1`, `timeouts 0`. The heavy job took
**103.5** min wall (07:31:08 → 09:14:39; `RUN_RESULT` 1107 pass, 1 fail, 1 over timeout, 6015 s). That is
inside `90`–`115` and under the `127` budget.

**Nightlies three to five, read together at `r7453+70` (16:00 UTC 2026-10-20), because this seat's tools were down for all three; a record, not a re-score.**
- **The same tree three nights running.** `main` did not move between 2026-10-17 16:48 and the three cron runs, so all three ran at `b57bfc6e`. The spread below is the runner's, not the suite's.

| run | night | heavy wall | index wall | compile |
|---|---|---|---|---|
| `39108912198` | 10-18 | 80.0 min | 111.3 min | 7.0 min |
| `39223045983` | 10-19 | 94.3 min | 116.7 min | 8.1 min |
| `39391528454` | 10-20 | 65.5 min | 116.0 min | 7.9 min |

- **Heavy:** on one tree the wall spans **65.5–94.3 min, a 29-minute spread**. That is a runner-variance figure the `127` budget has to cover. It is not a growth figure.
  - `refs/ci/nightly` landed for the 10-20 run at `b57bfc6e`.
  - `RUN_RESULT`: **1108 pass, 0 fail, 1 over timeout, 3814 s**. The over-timeout is the P15 runtime tail, already routed at `r7349`.
  - The job reads `failure` because `check_receipts_run` fails on that one UNRUN receipt. Its log says "1 receipt(s) exceeded the per-receipt timeout and are UNRUN". Nothing failed for a reason inside the corpus.
- **⛔ Index:** **111.3 / 116.7 / 116.0 min against its 120-minute job limit, leaving a 3.3-minute margin at the worst.** Five readings now (81, 115.6, 111.3, 116.7, 116.0), all above the registered `35`–`70` band.
  - The next index job that runs four minutes slow is cancelled. Under r7432 that leaves no artifact, and the index ages silently toward its 35-day limit.
  - The budget is 66's call, and it is routed in the reply, not applied.
- **Index refreshed from the 10-20 artifact:** **1109 (`b7095942`, 2026-10-16) → 1109 (`b57bfc6e`, 2026-10-17)**.
  - NEW 0, GONE 0, `red_under_trace 1 → 0`, `timeouts 0`.
  - The 645 entries that differ differ only in their timing field.
  - `check_index_coverage` exits 0. It is already wired.

**W-a/W-b.** Measured with `measure_w.py` (kept in the session scratchpad, not committed). It loads the
committed and the new `receipt_scope.py` side by side against one index, takes three timed `load()`
calls each, and calls `scope(idx, {'corpus/quote_pin_baseline.tsv'}, ∅, ∅, 'suite')`. Static names
carried: 2324 → 2504. That is 180 more, where 60 counted 179 at `r7366`; the tree has moved since.

**W-c refuted low, and the reason is mine.** 60's `+18 %` was measured on 60's container. I drew the
band from it without asking whether a load-time ratio transfers across machines. It does not: here the
regex is a smaller share of `load()` than the git calls around it, so `+0.06` s replaces 60's `+0.53`.
The price written beside the change is therefore **"+0.06 s a read here, +0.53 s on 60's machine; at most
+3.2 s a push"**, the upper of the two. *A ratio of wall times is a property of the machine whose costs
it divides, and here they differ by a factor of six.*

**Which form, and why.** I took the structural form, as ordered, and my own reading agrees with 60's.
`repo_names` already bounds both uses (`emit` line 208, `load` line 271), so an explicit extension list
adds no safety. The `21` extra names are files the tree does have. The minimal form fixes `tsv` and
leaves the next missing extension to the next receipt that finds it.

**The ported fix in S54 (60's, routed to confirm or replace).** S54 asserts, of the instrument read
live, that no ledger reader is in the scope (Ⓐ③) and that the `tsv` patch changes the source (Ⓐ⑤).
The repair it routes and r7367 ③ orders falsifies both: fail-on-success. It now reads
`scripts/receipt_scope.py` at its own commit `3f30509e`, where those claims are historical. The index
it loads is still the tree's. Runs: exit `0` before the change and exit `0` after; all five Ⓐ checks
OK. The gates that read the receipts and the workflow are green, except `check_quote_pins`, which is
red on 2 NEW keys in **S55**. S55 is 60's and arrived with `main`; it is not this change's.

**The index job (④).** The heavy tier runs no tracer, so "no extra runner time" was not on offer. The
`index` job is the backstop's ⓶ trace, `emit` and artifact upload, lifted unchanged. It runs on the
`0 3 * * *` cron only, with no `needs:`. The trace-and-emit commands were smoke-tested here on two
receipts, and the result is a valid header with commit, date and tree digest. YAML parses with 8 jobs.
**It lands tonight only if merged before 03:00 UTC.**
