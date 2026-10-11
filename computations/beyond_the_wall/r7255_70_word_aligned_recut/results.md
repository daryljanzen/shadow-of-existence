# `r7255+70.1` — results: the 46 re-cut word-aligned, still breaking every declared reversal; 20 targets re-filed

*Pre-registered at `PREDICTION.md` (`810a8c12`). The scripts are `recut.py` (measurement), `apply_recut.py` (token
edits, run, keyed, or reverted) and `sixty_alignment.py` (60's own test, lifted from `S18`). Their outputs are
`recut.txt`, `apply_log.txt` and `sixty_alignment.txt`. The edits are in `ledger.json`, and the target flips in
`TARGET_FLIPS.tsv`.*

## ① and ②: the re-cut, and what it costs

**The re-cut.** Each re-cut is the shortest contiguous, word-aligned span that contains the original reversal-blind
phrase and appears in no declared reversal of today's clause. The clause and the reversals come from S7's own
`clause_at` and `reversals`.

| # | predicted | measured |
|---|---|---|
| R1, re-cuts that still break every declared reversal of today's clause | 46 (43–46) | **46** |
| R2, minimal re-cut ≠ plain word-boundary expansion | 5 (0–15) | **0** |
| R3, characters added | median 2 (1–6) | **median 2**, range 1–10 |
| R4, receipts green after the edit, with the new literal keyed | 46 (44–46) | **46**, none reverted |

**60's own test on the 46:** before the re-cut, 46 were `CLIPPED`. After it, **46 are `ALIGNED`, 0 `CLIPPED` and 0
not in the papers.**

⛔→✔ **The reachable negative does not fire.** Word-alignment costs the extensions nothing: every one still breaks
every reversal it was built to break.

**This was structural, and stated before measuring.**

- The word-boundary expansion contains the clipped span. If it appeared inside a reversal, so would the clipped
  span, and the clipped span was built to appear in none.
- So **the clause and the operator reconcile, and the `EXTENDED` class needs no exemption.**
- The measurement adds two things the argument could not:
  - **Today's clauses still give the same reversals.** All 46 clipped spans still break today, so no paper moved
    under them.
  - **The minimal word-aligned window is always the plain expansion** (R2 = 0). A shorter word-aligned cut on the
    other side never existed.

The typical re-cut restores the word the character window had split, usually the negation: "`… is n`" becomes
"`… is not`", and "`t interchangeable`" becomes "`not interchangeable`". The span carries its polarity as a word,
which is what makes the clause able to ratify it.

## ③ The `target` column, `PAPER` → `SOURCE`

- **20 rows re-filed** (predicted 19, band 10–30). These are the 24 that cc66's `READING.tsv` says read
  `SOURCE/ACOUSTIC_two_arm.py`, less 4 already filed `SOURCE`.
- **Receipts reading the baseline that went red on this edit: 0** (T2, predicted 0). The re-cut is a different
  story; see below.
- **The operator's trace rule is not changed.** It still files these as `PAPER` when it is re-run. That direction
  of the rule's error is now recorded in the baseline, not repaired in the instrument.

## One gate converted, because the re-key broke it

**60's `S18` Ⓒ④** asserts that all 64 of its `EXTENDED` rows still read `EXTENDED`. The re-key changed 46 of their
literals, so its lookup failed.

- **Converted by node 70**, under the same standing rule as `C64`/`C66`: my edit is what broke it.
- The claim is unchanged. It now looks each row up under its re-cut literal where my published `ledger.json`
  records one.
- **All 64 still read `EXTENDED`, and the gate is green.**

## Checks

- `check_quote_pins`, `check_prose_pins`, `check_pin_board`, `check_exact_counts` and `check_cannot_fail` all
  exit 0.
- Every receipt that reads the baseline or `EXTENDED_ALIGNMENT.tsv` exits 0.
- The 32 `L221` receipts that carry the 46 re-cuts each ran green after the edit.
