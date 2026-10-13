# `r7281+70.1` — results: the carry ledger gains `gates`. The field is not decoration: every reproducible red named a gate, and `S14`'s two-way red is exactly what it now records

*Pre-registered at `PREDICTION.md` (`ea97ef12`). The code is in `scripts/red_carry.py`.*

- The receipts re-run are listed in `reruns_list.txt`, and their scores are in `reruns.json`.
- The two re-run harnesses are `rerun_own_runner.sh` (each commit's own runner) and `rerun_current_runner.sh`
  (today's runner copied into each commit's worktree).

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| L-a | live `suite` entries gaining a label | 3 (2–3) | **3**: `S14` ×2 → `[Ⓑ①, Ⓔ③]`, and `S19` → `[Ⓒ②]` |
| L-b | historical `suite` additions in a whole-scope event | 40 (0–171) | **64**: one event, `main` at `97636d38`, +64 at once |
| L-c | rule-1 share among the rest (registered marker) | 70% (50–90) | **70%** (14 of 20 reproducible reds, today's runner) |
| L-d | rule-2-only share | 25% (8–45) | **5%** (1 of 20, a `FileNotFoundError @ L190`): **refuted low** |
| L-e | historical `suite` reds that would gain a label | 80% (50–95) | **≈ 62%** registered, **≈ 82%** revised (below) |

**How L-c and L-d were measured.**

- I took 30 of the 296 named historical additions whose red commit is in this clone, drawn at seeds 7281 and
  72812. I re-ran each one at its own red commit.
- **10 of the 30 PASS there.** Six of them are `D1_a_check_pinned_to_a_distance_from_the_present`, a receipt
  pinned to the date. They were red in CI for a reason that cannot be re-created now, and they are excluded as
  unreproducible, not counted as nameless.
- That leaves 20 reproducible reds. Together with the 3 live ones, that is 23.

**On L-e, as registered:** (360 − 64) × (14 + 1) / 20 / 360 ≈ 62%, which is above the 50% line. **66's negative
does not fire.**

## ⌗ Two measurement facts that moved the design, stated as they happened

**1. The runner matters more than the receipt.**

- Re-run with each commit's OWN runner, only 5 of the 20 named a gate under the registered rule. Runners before
  `r7163` kept three lines at 300 characters, joined with ` / `, and dropped the tags.
- With TODAY's runner copied into each worktree, 14 of the 20 named one.
- **The field reads what the current runner keeps.** That is the forward case, and it is what L-c reports. Old
  entries cannot be labelled retroactively from logs: they are gone, and the old logs held almost nothing anyway.

**2. The registered marker missed a third gate-printer form. It is REVISED after the measurement.**

- Six of the 20 print gates in a COLUMN, `FAIL  Ⓐ③ …` (`OK    ⓷ …` when green), with no bracket and no colon.
- The marker now takes `^FAIL\s{2,}` as well. **Under it, 20 of 20 reproducible reds name a gate**, so L-e is
  ≈ 82%.
- The same read found a hazard. A gate with no glyph id is labelled by its text, and that text carries counts
  that move between runs: `R1` printed `twenty-six (26 …` at one commit and `thirty-five (33 …` at another.
  Labelled raw, a moved count would read as a NEW gate.
  - The text label is now its first 40 characters with digit runs masked to `#`.
  - Both changes are seeded.

## What went in

All of it is in `scripts/red_carry.py`. No receipt is touched.

- **`gates`** is written beside `since` and `run` on every `suite` entry. It is a sorted list of labels from the
  run that last found the receipt red.
- **The label rule:**
  1. A gate line: `[FAIL]`, `FAIL:`/`FAILED:`, or the column `FAIL  `. The label is the glyph id (`Ⓑ①`, `⓸ᵇ`), or
     else the first 40 characters with digits masked.
  2. Otherwise a traceback: `<Exception> @ L<n>`, from the receipt's own innermost frame.
  3. Otherwise `[]`. A banner (`RESULT: FAILED`, `1 GATE(S) FAILED`) is not a gate.
- **A whole-scope carry** writes `[]` for each receipt. **An entry with no key** reads as UNRECORDED, which is not
  the same as `[]`. Old entries are not migrated, and the next red run fills them in.
- **A carried receipt red again** is recorded in one of three ways:
  - `= still red`, when its labels are unchanged; nothing is written.
  - `= still red, on fewer gates`, when one of two gates is repaired. **This is `S14`'s case at `r7277`.** The
    entry stays, with the other label, and is not cleared.
  - **`≠ red for a NEW gate`**, when a label appears that was not there before.
  - In the last two cases the ledger is now WRITTEN, with a `~ receipt old -> new` line in the commit. Today it is
    not written at all.
- The `union` step prints each carried receipt's gates, or "the run named no gate".
- **Seeds:** the 11 PO-65 seeds are unchanged and OK. There are 11 new `L` seeds on a built suite log and the same
  `apply` that CI calls:
  - two labels for two gates;
  - an assert labelled by its line;
  - a banner is not a gate;
  - a timeout names none;
  - the column form;
  - count masking;
  - one of two repaired → still red;
  - a new gate → `≠`;
  - red on the same gates → no write;
  - unrecorded → filled, not flagged;
  - a set-evidence class writes no field.
- `--seed-history` is OK.

## Not done, and stated

- **`tolerance` and `reads` gain no field.** Their evidence is per-site: a `tolerance` `FLAG`/`FLIP` row already
  names a `site`. Carrying that site is the same change in `reds_tolerance` and is the obvious next step, but it
  is not this order.
- **A timeout (`[slow]`) names no gate,** because the receipt never reached its verdict. The entry records `[]`,
  and the `PO-67` limits in the docstring stand.
