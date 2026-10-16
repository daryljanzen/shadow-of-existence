# r7411+70 — PRE-REGISTRATION (pushed before any scope is computed or receipt run)

*Order `r7411` ②: price running the scoped receipt gates locally on a typical revision's diff, on this
container. Price it, do not wire it. Seat 70, at `origin/main` `964fef0a2`.*

**"A typical revision's diff", fixed now.** Take the last 20 first-parent commits on `main` whose
subject begins with a revision number. For each, compute `receipt_scope.py --range <c>~1..<c> --scope
suite` (one `load()`, then `scope()` per commit). The typical revision is the one at the **median suite
scope size**. All three scopes are then run on that one revision with their own runners: `run_all_receipts.py
--from`, `sweep_runner_reads.py --from`, and `sweep_tolerances.py --from` with CI's two-build probe.

| arm | quantity | central | band | failable? |
|---|---|---|---|---|
| **L-a** | median suite-scope size over the 20 revisions | `12` receipts | `3`–`60` | yes |
| **L-b** | suite scope run (`run_all_receipts --from`, 4 jobs), wall | `8` min | `2`–`30` | yes |
| **L-c** | reads scope run (`sweep_runner_reads --from`), wall | `10` min | `2`–`40` | yes |
| **L-d** | tolerance scope run (two builds), wall | `15` min | `3`–`60` | yes |
| **L-e** | total, L-b + L-c + L-d plus scoping | `35` min | `10`–`120` | yes |

*The decision is 66's ("if it is affordable it joins the turn batch"). The number is mine. I will report
the per-scope split, so a partial adoption (for example, suite only) can be priced from the same run.*

*EFFORT (r7411 ②): central 60 min, band 30–120. Ceiling: one revision.*
