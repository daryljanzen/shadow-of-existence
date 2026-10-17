# `r7433` ② — THE DENOMINATOR, READ FROM THE `21` SOURCES: **`78` REFUSAL SITES, `7` WALKED**

*The order: enumerate each instrument's refusal SITES from its own source, statically, and carry
`paths walked / refusal sites` beside the grade. `sites.py` LOCATES; the count below is ADJUDICATED by
reading `sites_context.txt`, because a count produced by the locator alone is the `r7425` ② scrape one level
up — and the locator proved that in its own first pass (see ⒠).*

**THE UNIT, and the one exclusion.** A site is a branch that makes the instrument exit nonzero **for a
reason of its own, with its own printed address**. The final `if bad: return 1` is excluded: it propagates a
failure already set and names nothing.

## ⒜ THE TABLE

| register row | source | sites | walked |
|---|---|---|---|
| `check_prose_pins` | own | 5 | 1 (`.61`) |
| `check_quote_pins` | own | **14** | 1 (`.64`) |
| `check_open_references` | own | 3 | 0 |
| `check_open_item_coherence` | own | 2 | 0 |
| `check_exact_counts` | own | **6** | 2 (`r7429`) |
| `check_marker_transposition` | own | 5 | 0 |
| `check_tilt_pins` | own | 5 | 0 |
| `check_paper_pins_present` | own | 2 | 0 |
| `check_revision_collisions` | own | 6 *(4 verdict + 2 declaration aborts)* | 0 |
| `check_cannot_fail` | own | 4 | 1 (`r7429`) |
| `check_unread_figure` | own | 4 | 0 |
| `check_paper_pins_not_comment_only` | own | 3 | 0 |
| `check_figures_pinned` | own | 3 | 0 |
| `check_pin_board` | own | 3 | 0 |
| `check_pins_adjudicated_on_mint` | own | 3 | 1 (`.64`) |
| `ROWS.tsv : index` | `60`'s join gate | 8 *(a FLOOR: 2 relay a family)* | 0 |
| `ROWS.tsv : class` | — | **0 — nothing refuses** | n/a |
| `quote_pin_mint_held.tsv` | the mint gate — **same source as row 15** | (3, not additional) | (1, the same walk) |
| `check_view_tables : the debt file` | own | 2 | 1 (`.57`) |
| `red_carry : the carry ledger` | own | 3 *(all operational aborts, **0 verdict refusals**)* | 0 |
| `frontier_steps_history.tsv` | — | **0 — nothing refuses** | n/a |

**`81` summed over rows; `78` DISTINCT, because two rows share one instrument. `7` walked. ⇒ `9` %.**

## ⛔ ⒝ SO `8 of 21` WAS NEVER A READING OF THE POPULATION, AND THE ORDER'S OWN GUESS WAS LOW

*`r7433` ② put it at "if the `21` instruments carry `60` refusal paths, then `8 of 21` was never a reading of
the population".* **They carry `78`.** ⇒ *`8 of 21` instruments graded is `7 of 78` paths walked. The column
was reporting `38` % of instruments and `9` % of what it grades.*

## ⛔ ⒞ AND THE INSTRUMENT I WALKED MOST HAS SIX PATHS, NOT THREE — SO `r7433` ④'s "YOU WALKED THREE" IS TOO KIND

`check_exact_counts` refuses in **six** branches: a lost seeded direction, a missing baseline, duplicate
baseline keys, ⓵ a new EXPOSED site, ⓶ a stale entry, ⓷ the ceiling. ⇒ **I walked TWO** — ⓵ end to end and
⓷ to its silence. ⓶ I read in the source and never induced, and the other three I never touched. *`.78`
described three directions; the order read that as three walked. **Two.***

## ⛭ ⒟ THREE ROWS ARE NOT GRADEABLE AT ALL, WHICH THE RATCHET'S `21` WAS HIDING

- **`ROWS.tsv : class`** and **`frontier_steps_history.tsv`**: *no instrument refuses on either key* — `0`
  sites. Their `UNREAD` was a category error: `UNREAD` means *not walked yet*, and these can never be walked.
- **`red_carry : the carry ledger`**: `3` `raise SystemExit`s, all operational (a git call failed, the ref
  would not write) and **not one verdict about its key**. *The ledger records; it does not refuse.*

⇒ **The ratchet's honest population is `18` gradeable instruments, not `21`,** and the three above belong in a
state of their own. ⌗ *`quote_pin_mint_held.tsv` is a fourth irregular: its refusals are the mint gate's, so
summing sites per row double-counts. **A denominator summed over rows is not a denominator over instruments**
— which is this phase's own lesson arriving inside the fix for it.*

## ⛔ ⒠ AND TWO OF MY EIGHT GRADES DO NOT REST ON A WALK

*The register's own rule is `REACHABLE` only where this seat has walked the path.* **Audited against the
walked column: `6` of the `8` hold (`.57`, `.61`, `.64`×2, `r7429`×2). Two do not** —
`check_open_references` (*"this seat built both"* — authorship, not a walk) and `check_open_item_coherence`
(the gate's printed words, read not induced). ⇒ *They keep their grade with `0 of n` walked beside it, which
is now visible in the cell instead of inferable from a parenthesis.*

⛔ **And the locator missed an idiom on its first pass.** `PATTERNS` matched `bad += 1` and not `bad = True`,
so `check_paper_pins_present` came back with **one** candidate when it has three. *Found by reading the file
rather than by trusting the run, fixed in `sites.py` with the miss recorded in the source, and every count
above is from the second pass.* ⌗ *Same family as `r7425` ②, in the instrument built to measure that family.*

## ⌗ WHAT THIS IS NOT

*Not a claim that `78` is exact to the branch:* `ROWS.tsv : index`'s `8` is a floor (two of its `fail()` calls
relay messages built elsewhere), and `check_view_tables`' `1` `return 1` carries **two** printed reasons,
counted as `2`. *Both are recorded where they occur.* **Not a walk of anything new either: `7` walked is the
same `7`, now with a denominator under it.**
