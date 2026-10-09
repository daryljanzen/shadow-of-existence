# r7223+70.1 — results: the two detector blindnesses, repaired where they are mine and measured where they are not

*Pre-registered at `PREDICTION.md` (`4cc6442f`).  Logs: `keys_before.tsv`, `keys_after.tsv`, `keys_new.tsv`,
`r1_wrap_log.txt` and `r1_resplit_log.txt`.  The re-cut splits are in `wrap_tolerant_paper_reversal.tsv` and
`wrap_tolerant_source_270.tsv`.*

## ② The pinned read — repaired in the operator

- **The repair.**  `_READ` in `scripts/mutate_assertions.py` now recognises a `git show` read, whether inline (`'git',
  'show'` as adjacent list elements, or the string `git show`) or through a helper wrapping one.  Nothing else in the
  operator changed.
- **The seed.**  `--seed` gains `PINNED`: an inline pinned read, a helper-wrapped one, a plain `open()` read, and the
  `r7234` list form through a pinned read.  All five keys are found.  With the old pattern swapped back in, only the
  `open()` key is found, so the seed discriminates.
- **The count.**  `--quote` goes from 2,655 to 2,757 key rows.  That is **102 new `(receipt, literal)` keys**, and
  one existing key in `G50` is retargeted from `SOURCE` to `PAPER` because its trace now reaches the `.tex`.  None is
  lost.  76 of the 102 target a paper.  `r7234`'s three `_CLAUSES` are all among them.
- **The gate.**  The 102 enter the baseline in their own bucket, `UNADJUDICATED-PINNED`, with a ceiling of 102.  Their
  7 multi-site keys are counted apart, against a ceiling of 7.  This follows `r7201+70.1`'s list-key precedent:
  folding them in would read old pins newly seen as new work.  The existing counts are all unchanged: **2,167**
  unadjudicated against 2,287; **249** multi-site, 122/127; **60** list keys.

## ① The line wrap — not in `--quote`, which already compares collapsed; measured in `S7`/`S8`, which are `60`'s

`S7`/`S8` locate sites with a raw `find(lit)`, so a literal whose words a paper or source wraps across a line reads
as `ABSENT`.  I re-ran their own code through my loaders.  The literal's spaces matched any whitespace run, and
survival was compared on collapsed strings.  Every other rule was the shipped one.  As a sanity check, every key
whose sites did not change also kept its bucket.

| | shipped | wrap-tolerant | change |
|---|---|---|---|
| `S7` `ABSENT` (paper) | 218 | **98** | **−120** |
| `S7` `REVERSAL` | 442 | 475 | +33 |
| `S7` `DISCRIMINATING` | 279 | 324 | +45 |
| `S8` `ABSENT` (source) | 469 | 454 | −15 |
| `S8` `CODE` | 218 | 202 | −16 |
| `S8` `REVERSAL` + `PARTIAL` | 270 | 288 | +18 |

- **More than half of `S7`'s `ABSENT` was this blindness**: 120 of 218.  Paper bodies wrap their lines and the
  pins quote across the wraps.
- **The finding `60` led with survives, slightly strengthened.**  Paper 324/1,259 = 25.7% against source 65/353 =
  18.4%, z = 2.84, p = 0.0045.  Shipped: z = 2.77, p = 0.0057.  `One in four would notice` stays a fact about
  papers.
- **The 712 do not need re-cutting.**  Re-running `r7215`'s and `r7221`'s own D searches on the wrap-tolerant
  populations:
  - **paper**: 438 of the 442 are still present and 428 keep their class.  10 change class, all to a costlier one.
    4 leave, and 37 are new.  The split is 82 / 187 / 206 against 80 / 176 / 186.
  - **source**: 268 of the 270 are still present and 264 keep their class.  4 change class, all to a costlier one.
    2 leave, and 20 are new.  The split is 76 / 108 / 104 against 72 / 96 / 102.
  - Every class change is upward, because a newly visible wrapped site is one more site to cover.
  - ⇒ **The `EXTEND-SHORT` batch is 82 + 76 = 158 keys on the wrap-tolerant count.**  Six of the 152 banked
    `EXTEND-SHORT` keys are no longer short.

## Predictions against measurement

| | predicted | measured | |
|---|---|---|---|
| P1 new keys from the read repair | 60–250, guess 120 | **102** | hit |
| P2 most of them `PAPER` | > half | 76 of 102 | hit |
| P3 `r7234`'s three among them | all three | all three | hit |
| P4 `S7` `ABSENT` falls by 5–25 | 5–25 | **120** | **miss, by a factor of five** |
| P5 `S8` `ABSENT` falls by 0–10 | 0–10 | **15** (and `CODE` by 16) | **miss** |
| P6 the 2,167's existing keys unchanged | 0 | 0 | hit |

- **P4 is the miss that matters.**  I treated a wrapped quotation as rare.  In the paper half it was the commonest
  reason a pin read as absent.
- **P5 missed in a direction I did not consider.**  `CODE` fell too: 16 keys had a wrapped prose site as well as the
  code site the raw search found.

## What this does not do

- `S7` and `S8` are not edited.  Their raw `find` is `60`'s to change.  The one-line collapse `60` named is
  measured here, and its effect is the table above.
- No existing baseline verdict changes, and no receipt changes.
