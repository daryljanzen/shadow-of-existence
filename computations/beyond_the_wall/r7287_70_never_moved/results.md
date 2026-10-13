# `r7287+70.1`/`.2` — results: 66's negative fires. The moved share ranks `REPAIR-OWED` at Spearman +0.24, no better than the proxy, so no projection is filed. The reason is the instrument: `git log -S` sees a literal move, and `REPAIR-OWED` is mostly a sentence that moved AROUND a literal that did not

*Pre-registered at `PREDICTION.md` (`6daf24a9`).*

- **The instrument** is `never_moved.py`, run over 927 keys: the 562 unverdicted ones (480 `UNADJUDICATED` plus
  the reserved classes) and the 365 campaign keys of the 13 reference prefixes. One row per key is in `keys.tsv`.
- **The exploratory re-run**, made after the negative fired and reported as such, is `named_files.py`, with one row
  per key in `keys_named.tsv`.
- **The backlog's never-moved shares**, published as a measurement only, are in `backlog_by_prefix.tsv`.

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| N-a | unverdicted keys located | 85% (60–98) | **81%** (458 of 562) |
| N-b | NEVER-MOVED share of the located | 45% (20–75) | **65%** |
| N-c | the cheap proxy (`PAPER` share), Spearman on the 13 | +0.45 (+0.15–+0.70) | **+0.21** |
| N-d | **the MOVED share, Spearman on the 13** | +0.75 (+0.45–+0.95) | **+0.24**: **refuted** |
| N-e | wall time, 4 jobs | 15 min (3–60) | **67 min**: over the band. The git calls were cheap (0.35 s); flattening every candidate file for every SOURCE key was not |

**⛔ The negative fires twice over.** +0.24 is under the +0.70 line, and only 0.03 above the proxy on the same
13, against the 0.20 margin required. **No projection is filed.** On this set, the variable is the proxy with a
git call attached.

**The seeds failed in the registered run:**

- `L281`, whose `DELIBERATE` rows 69 traced to records that never moved, read **50% moved**.
- `L202`, at 88% `REPAIR-OWED`, read **35% moved**.

## ⌗ Why, found by reading the keys rather than the count

**1. The registered location rule is wrong for SOURCE keys.**

- `_present_at`'s rule finds a SOURCE literal in EVERY tracked file that holds its first word. For a short literal
  that means ledgers, HTML editions, other receipts' docstrings, and this seat's own measurement files.
- "MOVED in any of them" is then nearly certain for a common word, and "NEVER" is certain wherever a measurement
  file copied it. `L281`'s "blind spot" was found in 71 files.
- `_present_at` only needs EXISTENCE somewhere. A line needs THE file the receipt reads, and the read traces live in
  the operator, not in the ledger.

**2. Repairing the location does not rescue the variable** (`named_files.py`, exploratory):

- Each key is located only in the files its own receipt names as string constants.
- `L281` now reads **0% moved**, as 69 traced. `L202` reads **12%**.
- **Spearman is +0.22.**
- At the key level, `REPAIR-OWED` is 22% among NEVER-moved keys and 38% among MOVED ones: a separation, but a weak
  one.

**3. The reason is what `-S` measures.**

- `git log -S` counts commits that change how many times the literal OCCURS.
- A `REPAIR-OWED` key is, by the header's own definition, one where the sentence moved and the pinned literal did
  not: the subject changed, or the claim narrowed, around words still on the line. That is exactly the edit `-S`
  is blind to.
- So `L202` reads 88% `REPAIR-OWED` and 12% moved, and both are right. Its literals never changed. Its sentences
  did.
- 69's variable is about the LINE. `-S` measures the literal. 66's timing was of `-S`, and with `-S` the variable
  does not discriminate.
- **The form that would test 69's variable is the line's own history:** `git log -L` on the literal's line range,
  or `-G` on a line-anchored pattern. Either reports an edit to the words around the literal.
  - I have not timed it. `-L` runs per line range and is known to be several times slower than `-S`.
  - **Offered, not run.**

## What IS published, as a measurement and not a projection

`backlog_by_prefix.tsv` gives each prefix's unverdicted keys and their NEVER / MOVED / UNLOCATED counts, by the
registered rule.

- It carries the SOURCE-key defect above, and **it projects nothing about `REPAIR-OWED`.**
- It does say where the literals are frozen, which is the half of 69's variable that `-S` CAN see.
- Of the located keys in the backlog, **65% sit on literals that have never changed occurrence count.**

**Not done:** no key is verdicted, and no ledger row is touched.
