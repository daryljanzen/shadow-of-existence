# `r7251+70.1` — results: `L204_physics_reach` re-read under the settled rule

*Pre-registered at `PREDICTION.md` (`dedfdc8f`). The new verdict for each key, with its ground, is in
`verdicts.tsv` and in the baseline, where it replaces the `r7249+70.2` text. The four baseline gates exit 0, and
the board is unchanged at 1,626 unverdicted, since the prefix was already off it.*

## Counts

| verdict | `r7249+70.2` (old rule) | predicted | **`r7251+70.1` (settled rule)** |
|---|---|---|---|
| `DELIBERATE` | 81 | 25 (15–40) | **19** |
| `REPAIR-OWED` | 6 | 62 (45–75) | **74** |
| `ENCODING-OK` | 12 | 6 (0–12) | **6** |

**All three bands held.** `DELIBERATE` came in 6 under its central guess, and `REPAIR-OWED` 12 over its own.
The refutation condition (`DELIBERATE` above 60) did not fire. **The settled rule moves 62 of this prefix's 81
`DELIBERATE` verdicts.** That is a direct measure of how much the old purpose ground was carrying.

## What survives as `DELIBERATE`, and why

The 19 are the keys whose literal a content-intact rewording **keeps**:

- 4 citation keys and register IDs, plus `JanzenDynamics`;
- 4 proper or field names;
- 2 named terms;
- 4 numbers;
- 2 tokens where the finding is about **naming** (`D/H`, `lithium`, under the receipt's own finding "one
  missing NAME");
- **one ② exception:** `C3`'s `Type I (Bianchi, dimension three`, where the finding is an overstatement audit
  of F12's quotation.

## What becomes `REPAIR-OWED`

- **43** paper sentences: ① fails, and the finding is about meaning.
- **17** `SOURCE` sentences: R-P station wordings, arc and ledger clauses, under the extension to target
  documents. 66 may overrule that extension. If it does, these 17 go back for 66's ruling, and the paper count
  stands.
- **3** formulas: the repair is cc66's normaliser form.
- **5** `ENCODING-OK` pairs that encoded one wording, not one fact: `(4/11)`, `3 nu`/`three neutrino`, and the
  right-handed-neutrino clause pair.
- **6** unchanged from `r7249+70.2`.

⇒ **The 43 paper sentences are exactly the population `r7251`'s main order asks about.** Whether
`REPAIR-OWED` on them names work that can be done is the question pre-registered at
`../r7251_70_meaning_pin_repair/`.

## cc66's `target` finding, measured on this prefix

**9 of this prefix's `SOURCE` keys are PAPER pins.**

- `P2` (2), `P3` (1) and `P7` (6) read `allp`.
- `allp` is built by a `papers()` glob over `corpus/*.tex` at runtime, so the static classifier never sees the
  path.
- **These 9 are cc66's misreading, reproduced on a second prefix.**
- Their verdicts above do not depend on the label: a sentence fails ① either way.
- **The `target` column itself is not repaired in this revision.** It is my instrument's, and the repair is
  the next item after the repair-form order.
