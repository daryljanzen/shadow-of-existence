# `r7249+70.2` — results: `L204_physics_reach` read, 99 of 99

*Pre-registered at `PREDICTION.md` (`aa0346e8`). The verdict for each key, with what was read, is in
`verdicts.tsv`, and the same text is in `corpus/quote_pin_baseline.tsv`. The claim (`08401b88`) is released
as done.*

## Counts

| | before | after |
|---|---|---|
| `L204_physics_reach` unverdicted | 99 | **0** |
| board total unverdicted | 2,082 in 342 receipts | **1,983 in 328** |
| `UNADJUDICATED` | 1,922 | **1,823** |

`check_quote_pins`, `check_prose_pins`, `check_pin_board` and `check_exact_counts` all exit 0. No receipt was
edited.

## The verdicts against the pre-registration

| verdict | predicted (band) | measured | |
|---|---|---|---|
| `DELIBERATE` | 65 (45–85) | **81** | inside the band, and 16 above the central guess |
| `ENCODING-OK` | 5 (0–12) | **12** | at the top of the band |
| `REPAIR-OWED` | 8 (2–20) | **6** | holds |
| `ALT-OK` | 10 (2–20) | **0** | **REFUTED LOW** |
| `NOT-A-PIN` | 8 (0–20) | **0** | holds, at the floor |
| left unread | 0 (0–10) | **0** | holds |

**5 of 6 bands held, and `ALT-OK` was refuted.** The miss has one cause. These receipts' disjunctions are
not over paper states. All 12 of them are spellings of one fact: `Y_p`/`Yp`, `nu_R`/`\nu_R`,
`3 nu`/`three neutrino`, `decouple`/`decoupling`, and a full clause against its suffix. So every one is
`ENCODING-OK`, and none is `ALT-OK`. The base rate I used came from prefixes whose receipts repair other
seats' sentences in place.

**The stop rule (more than 30 `REPAIR-OWED`) did not fire.**

## The six `REPAIR-OWED`, by what each is owed

1. **`C3` `"JanzenRange"` and `"The isotropy dimensions are the Killing-vector counts the construction
   establishes"`.** These pin the as-found citation the receipt reports as the defect: a citation for a
   fact the cited paper never states. Re-pointing it is the repair, and these conjuncts then go red.
   **What is owed (L-249):** pin the as-found state at its commit, and assert the current citation
   separately.
2. **`P5` `"dS"`, `"throat"` and `"S^2"`.** These are **vacuous**. They test a two-letter token and a
   two-way disjunction against all of `THE_LIVE_ARC.md`: 1.1 million characters, with 54, 21 and 19
   occurrences. So they cannot fail, whatever L-519's row says. **What is owed:** one pin anchored to
   the row's own throat clause.
3. **`P10` `"neutrino"`.** This is a **vacuous arm**. The third disjunct of `nu_R` or `\nu_R` or
   `neutrino` passes in any paper that mentions neutrinos. **What is owed:** drop the arm.

All six receipts are other seats' receipts, so I have not edited them. They are on the record for the seat
that owns each one.

## Why so much `DELIBERATE`

Every receipt in this prefix is a station walk. Each one names its station in R-P's own words, then quotes
the corpus sentences the answer rests on. Most of those sentences have already been re-pinned once for
innocent moves, under class (c).

The quotes are evidence the result asks no change to. That is the header's `DELIBERATE`: the wording is
the claim.

The weakest of them are `P12`'s four bare figures (`206`, `220`, `294`, `327`). Each occurs 1 to 3 times in
the file they read, and none is anchored to its line. That is not vacuous, so they are recorded as
`DELIBERATE`, with the weakness written into the verdict.
