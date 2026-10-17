# r7441 ① — THE TWO CHEAPEST INSTRUMENTS, CLOSED; AND A SECOND DEFECT IN MY OWN TALLY

**Order.** `r7439` ⑤: *"Keep walking, cheapest first, `check_quote_pins`' `14` last."*  Cheapest by pending
count were `check_view_tables : the debt file` (1 pending) and `check_pin_board` (2).  Both are now **fully
accounted**, which takes the register from **22 of 81** to **24 of 81** and the fully-accounted set from 7 to 9.

Every number below is `tally.py`'s, read off the register's own cells — not a hand sum.  `.84` exists because
I hand-summed this table once.

---

## ① `check_view_tables` — one `return 1`, two reasons, two DIFFERENT grades

The locator found **one** `return 1` (line 138) and the denominator credited the instrument with **2 sites**,
because that one statement is reached by two independent conditions: `if hard_fail or soft_rise`.  `.57` walked
`soft_rise`.  This cycle walks `hard_fail`.

**Induced by DATA.**  The gate finds row-keyed tables in `scripts/*.py` and `corpus/*.py` and classifies each by
**how the code reads it** — subscript or membership is `HARD`, `.get` is `SOFT`.  Three HARD tables exist
(`regen_frontier.py`'s `EST`, `GROUP`, `ORDER`), each covering 10 of 10 live rows.  I removed `'PO-50': 'D'` —
one **live** row — from `GROUP`:

```
    regen_frontier.py            GROUP        HARD  9/10  1 missing

  ⛔ 1 HARD table(s) missing a live row -- the row RAISES or does NOT RENDER:
    [FAIL] regen_frontier.py:GROUP -- PO-50
     A row needs EVERY hard table to reach a reader.  Add it, in the same revision.
```

**The address is this seat's and it was taken to exit 0.**  Adding the row back returns the gate to exit 0 and
the file to its committed bytes (`git status` clean).  So this reason is **REACHABLE**, where `soft_rise` is
**ONE STEP FROM A WALL** — the register's nearest member to a wall.  One site, two grades: the shape `r7429`
first found in `check_exact_counts`, now with a second member.

**⛭ And I did not take the gate's word for its own severity.**  The gate *derives* `HARD` from the source
rather than declaring it, and the whole claim rests on a missing row really raising.  With `PO-50` gone,
`regen_frontier.py` itself dies:

```
  File "/home/user/shadow-of-existence/scripts/regen_frontier.py", line 10803, in main
    if GROUP[p] != g or p not in live:
       ~~~~~^^^
KeyError: 'PO-50'
```

The derived severity is confirmed by measurement, in the generator's own voice.  (`GROUP`'s source comment, put
there at `r6549`, says "a row missing here raises" — and it does.)

Transcripts: `view_tables_0_clean.txt`, `view_tables_1_HARD_missing_RED.txt`,
`view_tables_2_generator_with_the_row_missing.txt`, `view_tables_3_address_taken_GREEN.txt`.

---

## ② `check_pin_board` — (a) walked on both its reasons, and (b) measured UNREACHABLE BY DATA

Three sites: `215` (a lost seeded direction, already marked SELF-REFERENTIAL at `r7437` ④), `228` (b), `232` (a).

### (a) the VOID claim — REACHABLE, both reasons

Appending a second `CLAIM` on a prefix an earlier claim still holds:

```
  ⛔ (a) VOID claim: L280_the_decidable_claims by cc66 at r7300 -- cc66 holds it until r7304
```

and the same site's other reason, a row whose revision field is unreadable:

```
  ⛔ (a) VOID claim: L999_a_prefix_with_no_revision by cc66 at rNone -- no revision id or no prefix
```

**A distinction worth the column.**  The refusal names **the holder and the deadline**, or **the field** — it
does not print a remedy.  The remedy is one hop away, in the claims file's own header: *"To give a prefix up
early, append a RELEASE row."*  Graded **REACHABLE** (I took the second address to exit 0 by writing a readable
revision), with the hop recorded rather than smoothed over.

**⌗ And a sentence of the gate's own, checked rather than assumed.**  The run that voids the `r7300` claim
prints, four lines later, `RELEASED  L280_the_decidable_claims … -- claimable again`.  Read together those two
lines look like a contradiction.  They are not — they are about different revisions — but the only way to know
is to try it, so I did: a `CLAIM` on that same prefix **at the trunk revision r7439** is accepted, `1 live, 3
RELEASED`, **exit 0**.  The gate honours its own sentence.  The pair is what establishes it; the green alone
would not have.

### (b) the board-vs-ratchet total — a SECOND self-referential branch, by measurement

`(b)` is `if total_board != total_base`.  Both sides are computed **in the same run from the same baseline**:
`generate()` calls `counts()` itself and emits exactly one row per key carrying that key's own count.  A row can
only be lost to the `not x.startswith('#')` filter — and `counts()` skips any baseline line starting with `#`,
so no key can start with one.

I did not stop at that argument.  `probe_b.py` runs **15 adversarial baselines** through the instrument's own
`counts()` and `generate()` — empty, comments only, a receipt field starting with `#`, containing `#`, empty, all
spaces, CRLF and trailing blanks, a 6-field row exactly, a 5-field row, a verdicted row, every UNVERDICTED
verdict at once, 250 keys under one receipt, mixed.  **0 of 15 made (b) fire.**

**And the source says so itself**, in `(b)`'s own docstring: *"a seeded property of `generate`, checked on the
board this gate generates.  (Its staleness half went with the committed copy at `r7257+70.1`.)"*  The half that
could differ was a **committed** board going stale.  `r7257+70.1` deleted the committed copy and made the gate
regenerate the board every run — which removed the only way the two numbers could ever disagree.  The seeded
property is checked at line 199, inside `_seeds()`; line 228 re-checks it on data that cannot differ.

So `(b)` is **SELF-REFERENTIAL** by `r7437` ④ — in the denominator, out of the numerator, explained rather than
pending.  `check_pin_board` is **fully accounted**: 1 walked + 2 self-referential = 3 of 3.  The
self-referential class rises from **10** to **11**.

⚠ This is a statement about **what can reach the branch**, not that the check is wrong.  A branch that cannot
fire is still the cheapest possible guard against a future edit to `generate()`.  It is catalogued, not faulted.

Transcripts: `pin_board_0_clean.txt`, `pin_board_1_VOID_claim_RED.txt`,
`pin_board_2_reclaim_at_trunk_GREEN.txt`, `pin_board_3_no_revision_id_RED.txt`,
`pin_board_4_address_taken_GREEN.txt`, `probe_b.py`, `probe_b_out.txt`.

`corpus/pin_claims.tsv` was appended to and restored **byte-exact** four times (`git status` clean after each).
Nothing it claims was ever pushed, so no other seat saw a claim this seat does not hold.

---

## ③ ⛭ A SECOND DEFECT IN MY OWN TALLY, FOUND BY USING IT — AND IT IS THE SAME DEFECT AS `.84`'S

`tally.py` was built at `r7439` because I hand-summed this table and got `78` for `81`.  Its grade counters were

```python
len(re.findall('SELF-REFERENTIAL', f[7]))
```

— occurrences of the **phrase**, one per branch by convention.  I then wrote a cell saying `⌗ 2
SELF-REFERENTIAL, now a PAIR`: **two branches, one occurrence.**  It counted **1**, and `check_pin_board` read
`2 of 3` instead of `3 of 3` — it was not in the fully-accounted list and the self-referential class still read
`10`.

**A counter that depends on how a sentence is spelled is the same defect as the hand sum it replaced**: both
read a number off prose and both can be off by one without saying so.  So I fixed the instrument rather than
reshaping the cell to suit it — `graded()` reads an explicit leading integer when present and counts a bare
phrase as 1 — and recorded the miss **in `tally.py`'s own docstring**, by the rule that put `sites.py`'s missed
`bad = True` idiom in its source.  The new counter carries a 7-case self-test (bare, `1 N`, `2 N`, two bares,
mixed, `10 N`, absent) in `tally_selftest.txt`.

I report it because I found it, and because the register's whole worth is that its numbers are not prose.

---

## THE COUNT AFTER THIS CYCLE (`tally.py`, running total, `tally_after_r7441.txt`)

| | before (`.84`) | after |
|---|---|---|
| distinct sources | 18 | 18 |
| refusal sites | 81 | 81 |
| **walked** | **22** | **24** |
| self-referential | 10 | **11** |
| pending | 49 | **46** |
| walked | 27.2 % | **29.6 %** |
| fully accounted | 7 | **9** |
| ONE STEP FROM A WALL cells | 3 | 3 |

`24 + 11 + 46 = 81`, printed by the instrument, not by me.

**Cheapest still pending**, in order, with `check_quote_pins`' 12 last by the standing order:
`check_exact_counts` 3 · `check_marker_transposition` 3 · `red_carry` 3 · `check_prose_pins` 4 ·
`check_unread_figure` 4 · `check_tilt_pins` 5 · `check_revision_collisions` 5 · `ROWS.tsv : index` 7 ·
`check_quote_pins` 12.

**The ceiling class stays a prediction**: 7 of its 9 branches are unwalked, and one printed address refutes it.
