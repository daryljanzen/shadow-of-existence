# `r7253+70.1` — results: the `MEANING-HELD` gate, the `target` column, and the grain re-read

*Pre-registered at `PREDICTION.md` (`a5755e75`). The gate is in `corpus/check_quote_pins.py`. The negative's
measurement is `discriminate.py` → `discriminate.txt`.*

## ① The gate

- **The vocabulary is closed.** Before this revision, ANY verdict string counted as adjudicated. Now an unknown
  verdict fails the ratchet.
- **A `MEANING-HELD` row must name `held at <sha>`.** The gate then checks:
  - **H1:** the sha resolves to a commit;
  - **H2:** that commit is an ancestor of HEAD;
  - **H3:** the literal is in what the key reads at that commit. The text is whitespace-normalised, because a paper
    sentence wraps across lines, and a regex literal is matched as a regex;
  - **H4:** the key is a `SENTENCE`;
  - **H5:** the held commit changed the receipt.
- **Counting:** held rows are reported as held, not owed, and never counted as a discharge of `UNADJUDICATED`.
- **Seeds, run on every pass:** a valid row is held. No sha, a bad sha, an absent literal, a `TOKEN`, and a HEAD
  stamp each fail.

### The reachable negative, measured in three stages

| stamp on 571 unread `PAPER`/`SENTENCE` keys | gate | pass |
|---|---|---|
| HEAD | H1–H4 | **560 (98.1%)** — M1, predicted ≥ 95%, held |
| HEAD | H1–H5 | **0 (0%)** — M2, predicted 0%, held |
| **each key's own receipt's last commit** (not pre-registered) | H1–H5 | **560 (98.1%)** |

⛔ **The negative fires in its strong form.** A verdict-writer who knows the rules can stamp an unread key with its
own receipt's last commit, and the gate passes it. H5 stops only the careless stamp.

- **No content check or provenance check can prove a key was READ.** At a commit where the receipt was green, the
  sentence is present by construction.
- **The same holds for every other verdict in the baseline.** `DELIBERATE`, `REPAIR-OWED` and `NOT-A-PIN` carry no
  mechanical check at all. A row's honesty rests on its reason text and on cross-reads.
- **So `MEANING-HELD`, gated, is the only verdict with any mechanical check.** It is weaker than the standard 66
  named, and stronger than every sibling.

**What the gate does secure:**

- every held finding is reproducible: check out the sha, and the sentence is there;
- a typo, or a verdict invented to escape the ratchet, now fails.

**My recommendation is to keep the adoption with this gate, and audit `MEANING-HELD` the way every verdict is
audited, by sampled blind cross-read.** The cc66–60 cross-read is the instrument that measures reading. A gate is
not.

## ② The `target` column

- **The 29 `FLIPS.tsv` rows are applied to the baseline.**
- **Receipts reading the baseline that went red:** 2, against a prediction of 1 (band 1–3, held). Both are cc66's,
  and both pinned the column's defect in its as-found state:
  - **`C64` Ⓔ.** As ordered, it is converted in this commit.
  - **`C66` E.** A newer receipt asserting the same defect. It is converted under the same standing rule, because my
    edit is what broke it.

**How both were converted:**

- The original assertion now runs against the as-found column, read from my published `FLIPS.tsv`: a listed key
  was `SOURCE` before the repair. That keeps `C66` inside its own standard-library import scope; a `git show`
  version broke its scope gate.
- The repair is asserted beside it.
- **Results:** in `C64`, all 15 rows were `SOURCE` before; now 13 of the 13 whose literal is in the four papers read
  `PAPER`, and the 2 remaining read a non-paper source. In `C66`, 13 were misfiled before and 0 are now.
- **Both receipts are green.** Each label says that node 70 converted it and why.

## ③ `L204` against the grain clause

| # | predicted | measured |
|---|---|---|
| G1, verdicts the grain clause moves | 1 (0–4) | **1**: `C3`'s `Type I (Bianchi, dimension three`. `Type I (Bianchi` is a strictly shorter span that carries the label claim, so it moves from `DELIBERATE` to `REPAIR-OWED` |
| G2, `REPAIR-OWED` → `MEANING-HELD` | 62 (55–64) | **61** |
| M3, converted rows that pass H1–H5 | 62 (58–62) | **61 of 61** |

**The one meaning pin left `REPAIR-OWED`** is `P3`'s `CR is a \emph{selection-rule}`. It is the arm of a
disjunction that its target never carried; the live arm is `SELECTION-RULE`. So there is no commit at which it holds,
and it stays owed.

**The other 18 survivors are confirmed.** They are citation keys, register IDs, names, named terms and numbers, each
the shortest span that carries an identity.

**`L204` now stands at:**

| verdict | count |
|---|---|
| `MEANING-HELD` | 61 |
| `DELIBERATE` | 18 |
| `REPAIR-OWED` | 14 |
| `ENCODING-OK` | 6 |

The `REPAIR-OWED` 14 are: 3 formulas, 3 code spellings, 1 coined phrase, 4 vacuous pins, 2 as-found defects, and
the arm above.
