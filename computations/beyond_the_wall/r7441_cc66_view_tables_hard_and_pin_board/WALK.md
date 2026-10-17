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

---

# r7441 ② ③ — THE REST OF THE CHEAPEST TIER: `check_exact_counts` AND `check_marker_transposition` CLOSED

Both were at 3 pending.  Both are now **fully accounted**, and all six paths were **REACHABLE BY DATA**.

## ② `check_exact_counts` — the three baseline-shape refusals.  `5 walked + 1 self-ref = 6 of 6` ✔

The gate is green at exactly its ceiling (`21 unadjudicated against a ceiling of 21`, 60 EXPOSED keys, 60
baseline rows), which is why the ceiling branch is the one that is `ONE STEP FROM A WALL`.

**(i) NO BASELINE** — the file moved away:

```
  ⛔ no baseline at corpus/exact_count_baseline.tsv -- this gate has no record to ratchet.
```

**And the address here is the file's EXISTENCE, not its content** — which is worth separating, so I measured
where taking it lands.  Put back a baseline carrying **one** real row and the gate does not go green; it moves
straight onto a different site:

```
    60 distinct EXPOSED (receipt, comparison) key(s); the baseline carries 1
  ⛔ 59 NEW EXPOSED exact count(s) -- an equality on a set another seat can move:
```

So the chain is `181 → 200`, measured rather than assumed, and `⓵`'s three addresses (monotone, read at a PIN,
or adjudicate) are where the *content* is adjudicated.  A refusal whose address is another refusal is still
reachable; it is just not one step.

**(ii) A DUPLICATED KEY** names the offending key exactly:

```
  ⛔ 1 baseline key(s) carry more than one row: [('receipts/L147_two_arm/B3_...', 'len(r) == 9')]
```

**(iii) A STALE ENTRY** names the row and its remedy in the same line, and I took it to exit 0:

```
  ⛔ 1 STALE baseline entr(y/ies) -- no longer an EXPOSED site, so remove the row:
      [STALE] receipts/L999_not_a_receipt/Z9_a_row_for_a_site_that_is_not_exposed.py  assert len(x) == 3
```

Transcripts `exact_counts_0_clean.txt` … `exact_counts_5_address_taken_GREEN.txt`.
`corpus/exact_count_baseline.tsv` restored byte-exact after each of four inductions.

## ③ `check_marker_transposition` — the three that remained.  `4 walked + 1 self-ref = 5 of 5` ✔

**(i) BASELINE ABSENT** — `corpus/marker_transposition_baseline.tsv is absent; the baseline is data and must
exist`.  It names the file and what kind of thing it is.

**(ii) A NEW FLAG names TWO addresses**, and that is the point of the walk.  Induced the honest way — by
**un-adjudicating a committed key** rather than planting a fake one, so the flag the gate raises is a real
detection:

```
  ⛔ 1 NEW TRANSPOSITION FLAG(S):
    [FAIL] CR_cosmology.tex:597  301.76 -- none of the group closing it carries it; H0_acoustic_angle_and_seam (cited at line 768) does
     ⌗ Put the marker beside the number it computes, or -- if this is not a
       transposition -- adjudicate it in the baseline with what was read and why.
```

The first address is editing the paper (another seat's); **the second is adjudicating in the baseline, and I
took that one to exit 0.**

**(iii) A STALE ENTRY** names the row, the remedy and the reason together: *"the flag no longer fires, so REMOVE
the entry … A fixed site left in the baseline is a silent permission to regress there (r7069)."*

Transcripts `marker_0_clean.txt` … `marker_4_address_taken_GREEN.txt`.
`corpus/marker_transposition_baseline.tsv` restored byte-exact after each of three inductions.

## THE COUNT AFTER ② AND ③

| | `.84` | after ① | after ② ③ |
|---|---|---|---|
| **walked** | 22 | 24 | **30** |
| self-referential | 10 | 11 | 11 |
| pending | 49 | 46 | **40** |
| walked | 27.2 % | 29.6 % | **37.0 %** |
| fully accounted | 7 | 9 | **11** |

`30 + 11 + 40 = 81`, by `tally.py`'s running total.

**Cheapest still pending:** `red_carry` 3 (three operational aborts, not verdict refusals) ·
`check_prose_pins` 4 · `check_unread_figure` 4 · `check_tilt_pins` 5 · `check_revision_collisions` 5 ·
`ROWS.tsv : index` 7 · `check_quote_pins` 12 (last, as ordered).

---

# r7441 ④ ⑤ ⑥ — TWO MORE RATCHETS CLOSED, THE CEILING CLASS TESTED TWICE MORE, AND `red_carry`'s ABORTS

## ④ `check_prose_pins` — `5 of 5` ✔, and the **ceiling class holds on its third member**

`.61` had walked the new-site branch.  The four that remained are all **REACHABLE BY DATA**:

- **NO BASELINE** — `no baseline at corpus/prose_pin_baseline.tsv -- this gate has no record to ratchet`:
  word for word the sentence `check_exact_counts` prints, which is itself worth noticing — the ratchets share a
  refusal *idiom*, not just a shape.
- **A DUPLICATED KEY** names the key, the line, and **two** addresses: *"merge the rows into one that records
  both, or name the key in `KNOWN_DUPLICATE_KEYS` with why."*
- **A STALE ENTRY** names the row, the remedy and the reason together, and I took it to exit 0.
- **⚖ THE CEILING** — the third member of the `r7439` ceiling class to be walked, and **the first walked since
  the class was claimed.**  The ceiling here is **0** against 161 sites read, so flipping **one** committed row
  to `UNADJUDICATED` fires it:

```
  ⛔ THE UNADJUDICATED COUNT ROSE: 1 against the declared ceiling 0.
     ⌗ The bucket means work and the ratchet is that it only shrinks.  Lowering the
       ceiling is the point; raising it is an edit to this gate and must be argued.
```

**The prediction holds exactly as written**: the first address (raise the ceiling) is forbidden by the
instrument's own text, and the second (verdict the site) is a judgement.  `ONE STEP FROM A WALL`.

## ⑥ `check_unread_figure` — `4 of 4` ✔, and **the ceiling class holds on a fourth, with a sub-distinction the claim did not predict**

- **NO BASELINE**, the same shared sentence again.
- **A NEW KEY names FOUR addresses in four lines** — read the figure from the paper, say what *this* receipt
  computed and drop the attribution, or record it as `NOT-A-PAPER-FIGURE` with what was read.  Induced the
  honest way, by **un-recording a live key** (`L165_interacting_tower/S7`), so the flag is a real detection.
- **A STALE ENTRY** names the row and the direction: *"fewer live sites than recorded.  Lower or remove the
  row."*  Induced by raising a recorded count above the live one.
- **⚖ THE CEILING, and here is the finding.**  I raised `owed` from 16 to 23 against a ceiling of 22 by
  flipping seven not-owed verdicts.  The refusal is **one line, with no address at all**:

```
  ⛔ THE OWED COUNT ROSE: 23 against the declared ceiling 22.
```

Compare `check_prose_pins`, four paragraphs up, which names **both** prongs inside the refusal.  **So the nine
ceiling branches are not uniform in what they SAY, only in what they ARE.**

**And it is still not a `WALL`**, which I established rather than argued: the only-falls rule is in this
instrument's **title line**, in its `⓷`, and in every run's `OWED: n ** may only fall **` printed four lines
above the refusal; and the remedy is reachable — **one** verdict took `OWED` from 23 to 22 and the gate to exit
0.  A judgement, not a record.  Grade `ONE STEP FROM A WALL`; the class survives its fourth test.

⇒ **4 of the 9 ceiling branches are now walked, 5 remain a prediction.**  Nothing yet refutes it.

## ⑤ `red_carry` — 2 of its 3, and **the address belongs to another tool**

`red_carry`'s three sites are **operational aborts, not verdict refusals**: they say the instrument could not
run, never that the tree is bad.  All three are reachable only **BY ENVIRONMENT**, and I induced them in an
**isolated temp remote** — the live `refs/ci/carry` was never written, and `--remote` never pointed at `origin`.

- **`cannot read refs/ci/carry from <remote>`**, by pointing `--remote` at a path that is not a repository.  It
  relays git's own words: *"does not appear to be a git repository."*
- **the generic `git <args>: <stderr>` abort**, by building a bare remote that **has** the ref, on a commit with
  **no `carry.json`**: `git show <sha>:carry.json: fatal: path 'carry.json' does not exist in '<sha>'`.

**⚠ Both name the failed command and git's reason and no remedy of their own.**  The address is in another
tool's voice, and in CI it is the runner's to supply, not this seat's — which is a different thing from either
end of the existing ladder, and is recorded as such rather than forced into `REACHABLE`.

The third (`could not write REF in TRIES tries`) needs **six** rejected pushes.  It is running against a bare
remote whose `pre-receive` hook rejects every push; the first attempt confirmed the loop turns —
`red_carry: another job moved the ledger first -- re-reading and re-applying` — but each iteration re-reads the
`PO-68` history, so six of them outran a 420 s timeout.  Re-running with room.  **Reported as in flight, not as
walked**, by the rule `.83` set when the `--unshallow` take failed.

## THE COUNT AFTER ④ ⑤ ⑥

| | `.84` | now |
|---|---|---|
| **walked** | 22 | **40** |
| self-referential | 10 | 11 |
| pending | 49 | **30** |
| walked | 27.2 % | **49.4 %** |
| fully accounted | 7 | **13** |
| `ONE STEP FROM A WALL` cells | 3 | **5** |

`40 + 11 + 30 = 81`.

**Still pending:** `check_tilt_pins` 5 · `check_revision_collisions` 5 · `ROWS.tsv : index` 7 ·
`check_quote_pins` 12 (last, as ordered) · `red_carry` 1 (in flight).

Every baseline induced in this cycle — `exact_count`, `marker_transposition`, `prose_pin`, `unread_figure`,
`pin_claims`, and `regen_frontier.py`'s `GROUP` — was restored **byte-exact**; `git status` on `corpus/` and
`scripts/` is clean.

---

# r7441 ⑦ — `check_tilt_pins` CLOSED WITHOUT DUPLICATING ITS SWEEP, AND A REFUSAL THAT WARNS AGAINST ITS OWN REMEDY

`5 of 5` ✔.  This one needed care, because **the instrument declares its own cost in its own source**:

> *Its cost is one receipt run per site — node 70's own figure … So it belongs in the monthly backstop beside
> that sweep and not in the fast list, whose budget is 420s per gate.*  ⛔ *A gate placed where it cannot finish
> is a gate that reports the clock instead of the tree.*

69 sites at ~11 s each is ~13 minutes.  By `r7271` ⒜ and ⒝ — **CI is the suite and is read, not duplicated;
nothing long runs in the chat container** — I did not run the full sweep here.

**Two of the five refuse BEFORE the expensive run**, which is why they were free:

- **NO BASELINE** — the shared ratchet sentence again.
- **THE SCOPED LIST MISSING** — `the instrument's scoped list is missing at …/r7119_70_tilt_coverage/tilt_list.txt`,
  with the rule in the next line: *"This gate runs 70's operator over ITS OWN list and does not invent a scope."*
  **That file is 70's**, so this one grades `REACHABLE BUT ELSEWHERE` — an address that exists and is another
  seat's to supply, never this one's.

**The other three were induced on a ONE-SITE scope**, by reducing the gate's own list file — which is *data*,
not the instrument.  One site, one run, 1 s per invocation:

- **A NEW DETACHED SITE** names its remedy: *"READ IT AND RECORD A VERDICT."*  Induced by un-adjudicating `B4`.
- **⛭ THE STALE BRANCH IS THE ONLY REFUSAL IN THIS REGISTER THAT WARNS AGAINST ITS OWN REMEDY**, and this is
  the find of the section:

```
  ⛔ 1 STALE BASELINE ENTR(Y/IES) -- no longer reported, so the adjudication
     describes nothing.  REMOVE the entry:
     ⛔ AND THIS REMEDY IS DESTRUCTIVE, SO READ WHAT IT RESTS ON FIRST (r7341): it is
        correct only if the run above measured the TREE. ... If DETACHED above is ZERO
        while the baseline is not, suspect the run before you suspect the baseline.
```

**And my own induction is exactly the case it warns about.**  I reduced the scope, so `DETACHED: 1` fell below
`the baseline carries 2` *because the RUN changed, not the tree* — and following the printed remedy would have
deleted a correct adjudication, which is what happened at `r7341` with a stale cache path.  The warning is
confirmed by an induction it did not anticipate.  **A refusal that tells you to distrust it is the opposite of
a wall and the ladder has no rung for it.**

- **THE CEILING** — the **fifth** member of the `r7439` class walked.  One line, **no address**, exactly like
  `check_unread_figure`'s and unlike `check_prose_pins`':

```
  ⛔ THE OWED COUNT ROSE: 1 against the declared ceiling 0.
```

Not a wall: the only-falls rule prints in the same run — `OWED: 0 ** the only bucket that means work, and it
may only fall **` — and one verdict took `OWED` from 1 to 0 and that line to green.  (The run stayed red for
the *stale* reason the reduced scope had induced, which is correct; the ceiling line cleared, which is what was
being measured.  Reported as what it is.)

⇒ **5 of the 9 ceiling branches walked, 4 still a prediction, and the sub-distinction now has 2 members
against 1**: two ceiling refusals print nothing, one prints both prongs.

The baseline and 70's list file were both restored **byte-exact** (`git status` clean).

## THE COUNT AFTER ⑦

**45 walked, 11 self-referential, 25 pending of 81 — 55.6 %.  14 instruments fully accounted.  6 cells at
`ONE STEP FROM A WALL`.**  `45 + 11 + 25 = 81`.

**Still pending:** `check_revision_collisions` 5 · `ROWS.tsv : index` 7 · `check_quote_pins` 12 (last, as
ordered) · `red_carry` 1 (in flight).
