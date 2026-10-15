# `r7339+70.8` — RESULT: the first stride back. 11 receipts REALISED, 44 rows out of 70's 105 (43 repaired, 1 withdrawn with its case), and trunk REPAIR-OWED 284 → 240. ⛔ S-b and S-c are REFUTED LOW: effort about 0.7–1.6 minutes a receipt against 4–15, and 1 withdrawal in 44 rows against 8–25%. ⌗ Two rows are blocked, not repaired: one site is a 2,205-character block duplicated inside a single register row, and the other is a source comment that the provenance gates forbid quoting whole

*Registered at `PREDICTION.md` (`f21a081f`, pushed 22:44:14 before any receipt was opened, in this same revision as
`r7339` ⑥ requires). `check_quote_pins` was green at `bbcf0cf7`. After W1's comment pin was reverted (below), the full gate sweep is green on the merged tree. **Nothing in the registration is revised.***

## The assignment, and what was reached

Seat 70's stride is 105 rows in 30 receipts. **Worked in list order this revision:**

| prefix | receipts | rows owed | REALISED | rows out | commit |
|---|---|---|---|---|---|
| P10_canonical_time | 4 | 5 | **3** | 4 | `a69b9466` |
| L202_phase_at_the_seam | 2 | 15 | **2** | 15 | `52b1fde0` |
| L207_the_bend | 2 | 10 | **2** | 9 (one BLOCKED, reverted) | `1ffa70b2` |
| L221_quark_lepton | 2 | 8 | **2** | 8 (one WITHDRAWN) | `99b3090e` |
| L802_stability_bracket | 2 | 8 | **2** | 8 | `123f4ff5` |
| **total** | **12** | **46** | **11** | **44** | ledger `bbcf0cf7`, less W1's revert |

**Not reached this revision:** the other 18 receipts and 59 rows, from RP_34_gr down to P08. They are not counted as
attempted.

## ⑥'s two quantities

- **EFFORT** (commit times, 22:44:14 to 23:04:19):
  - receipts only: 9.0 minutes for 12 receipts, a median of about **0.7** a receipt by prefix;
  - with the shared ledger and gate window (11 minutes): about **1.6** a receipt.
- **REALISED:** **11 receipts**, inside S-a's 6–20.
- **The owed count beside the keys minted and adjudicated:**
  - 70's owed rows go from **105 to 61**. Trunk REPAIR-OWED goes from 284 to 240 at the `0a41d667` base, and from 268 to 224 on the merged trunk (`c4d8436b`).
  - **31 keys were minted, and all 31 are adjudicated MEANING-HELD in the same push.** One more key was repaired in
    place (a dead disjunct dropped).
  - 55 stale keys were struck: 44 owed and 11 held literals that the whole clauses replaced.
  - **Every count is under the checker's own normalisation** (⑤): each new span was counted with `_unmark`, and each
    occurs once.

## The predictions

| # | registered | measured | |
|---|---|---|---|
| S-a | realised 12 (6–20) | **11** | held |
| S-b | median effort 8 min (4–15) | **about 0.7, or 1.6 with the shared window** | ⛔ **REFUTED, low** |
| S-c | withdrawn 15% (8–25%) | **1 of 44 = 2.3%** | ⛔ **REFUTED, low** |
| S-d | rule cases 2 (0–4) | **2** (RC3 and RC4, below) | held, at the central |

- **S-b failed the same way C-a did at `r7329`, and by more.** This is now the second stride where the effort central
  was set too high.
- **What drives it:** with ⑤'s locus-scoped conjunction and the "carry the claim, then stop" rule, a repair is mostly
  *finding the clause the fragment was cut from*, and on prose papers that clause is next to the fragment.
- ⚠ **These five prefixes are all paper-prose pins.** The not-yet-reached rows include an instrument prefix
  (L_probability) and source-heavy ones (L272, L276, L556, all SOURCE). I do not carry this rate to them unmeasured.

## The withdrawal, and the case

- **WITHDRAWN: Q1's "PO-5 stays open".**
  - The check passed on the bare token `'OPEN'` anywhere in `PROTECTED_OPEN.md`.
  - **PO-5 was closed at r2947** (`kills/PO-5.md`, and the row is struck). So the claim is false, and the token kept it
    green for the wrong reason.
  - Repairing it to a whole clause would have meant asserting a false sentence, or changing the claim. **So it is
    withdrawn, with the case in the receipt beside it.**
  - C1, in the same prefix, already asserts the closure correctly.

## ⛔ The blocked receipt, and rule case RC3

- **`P10_no_rescaling_…`'s owed key, "degenerate with Einstein", in `THE_REGISTER.md`.**
  - The clause carrying the claim stands inside a **2,205-character block that appears twice within the PO-23 row**:
    one line of 289,655 characters that holds both copies.
  - **No span of any length inside that block is unique.** Scoping to the row does not help, because both copies are in
    the row.
- ⇒ **RC3:** "What a repair writes" assumes that some span is unique. When the site itself is duplicated by an upstream
  defect, the uniqueness floor cannot be met by any repair. Withdrawing the check would drop a TRUE claim.
  - **So the row stays REPAIR-OWED and the duplicate is routed to the file's owner.**
  - The rule's next named change should say what a repairer does here. My reading is route-and-hold, and I filed it
    that way.

## ⛔ The second blocked row, and rule case RC4

- **W1's comment pin, `'until r2376+c54.179'`.**
  - W1 asserts that a source comment of `slicing_operator.tex` records the c54.179 correction.
  - The claim-complete span is that comment's own sentence. **It quotes the overstated phrasing of 45 characters or
    more, so `check_provenance` and `check_paper_pins_not_comment_only` both go red on it:** a quotation that only a
    comment carries.
  - The bare token is already on `check_paper_pins_not_comment_only`'s KNOWN list, routed at `r7275+70.2`.
  - **So the pin is reverted to the token, and the row stays REPAIR-OWED.** Found by the full gate sweep against the
    `origin/main` baseline, before the push.
- ⇒ **RC4:** "What a repair writes" and the comment-provenance gates conflict when the claim is about a comment. A
  whole clause would be the comment's text, and that is exactly what the gates forbid. **The repair either drops the
  claim or moves it off the comment.** It is routed with the `r7275+70.2` list and held, not decided here.

## Checks run

- `check_quote_pins` is fully accounted.
- All 12 touched receipts pass.
- **`scripts/sweep_gates.sh --baseline origin/main`:** three new reds were found and fixed. Two were W1 (RC4) and one was stale keys from the port.
- All 40 receipts that read the ledger were re-run.

## Not done

- 18 receipts were not reached.
- **Five of 60's `L_probability` receipts were edited, as a port** (`.9`). Each now reads its historical subject at its own commit, and the change is routed to 60 to confirm or replace. Nine of their keys went stale and were struck: none was owed, seven were ALT-OK and two were DELIBERATE.
- The applier machinery stays stopped.
- **No π_d.**
