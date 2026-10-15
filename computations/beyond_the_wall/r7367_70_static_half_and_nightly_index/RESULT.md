# r7367+70 — RESULT (registration `506f3f61`; the change at `1e861909`)

| arm | registered | measured | verdict |
|---|---|---|---|
| **W-a** ledger `suite` scope, structural form, at HEAD | `50` (`45`–`60`) | **`50`** | **HOLDS** |
| **W-b** that scope, form as committed (control) | `5` (`5`–`5`) | **`5`** | **HOLDS** |
| **W-c** min-of-3 `load()`, structural / committed | `1.18` (`1.05`–`1.35`) | **`1.03`** (2.55 s / 2.49 s) | **REFUTED LOW** |
| **W-d** `index` job runner time, first nightly | `46` min (`35`–`70`) | *unrun; scored by the 11:00 UTC nightly read* | — |
| **W-e** heavy wall that night | `101` (`90`–`115`) | *unrun; same* | — |
| EFFORT (r7367 ③–④) | `40` min (`20`–`90`) | **≈ 41 min** (15:38 → 16:19 UTC) | holds |

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
