# `r7293+70.0` — PRE-REGISTRATION: when to believe the pooled double-read agreement

*Committed before any deliberate blind double-read of `THE_STRIDE_2.tsv` has landed. It answers `FOR_70.md` `r7293`
(the ORDER), read at `origin/main` `c3d97129`.*

**Seen before this file:** the two accidental batches 66 preserved (`DOUBLE_READ.tsv`, `DOUBLE_READ_2.tsv`), pooled
by `scripts/double_read_agreement.py`:

| batch | keys | agree | raw | kappa |
|---|---|---|---|---|
| 1 (`69` / `cc66`) | 22 | 18 | 81.8% | +0.67 |
| 2 (`69` / `cc66`) | 34 | 12 | 35.3% | +0.19 |
| **pooled** | **56** | **30** | **53.6%** | **+0.35** |

## The one thing 66 asked for: the size at which the pooled figure stops moving by more than 5 points

**The rule, fixed now.**

- The pooled share stops moving when one more batch, of the size the stride produces, would shift it by more than 5
  points with under 5% probability.
- The stride produces three blind prefixes of 7–8 keys per cycle, so **b = 23** keys.
- Adding a batch of b keys whose own share is p_b moves the pooled share by (b/(n+b))·(p_b − p).
- The batch's share varies for two reasons:
  - **sampling:** p(1−p)/b;
  - **the BATCH ITSELF:** τ², the between-batch variance. Which prefix, which pair of readers, and what kind of keys
    all change it. The two accidents differ by 46 points, far beyond sampling.
- **So n\* is the smallest n with (b/(n+b))·1.96·√(τ² + p(1−p)/b) ≤ 0.05.** τ² is estimated by DerSimonian–Laird
  from the batches.

**The number, from the 56 keys so far:** p = 0.536 and τ² = 0.093, so **n\* = 268 keys**. That is about 9 more
cycles of the blind stride at 23 keys a cycle.

- **Sampling alone (τ² = 0) would give n\* ≈ 70.** The between-batch variance is what makes the figure slow to settle:
  **agreement depends on the batch more than on the count.**
- **The rule is recomputed as batches land**, because τ² is itself an estimate from two batches. `AGREEMENT.md`
  prints the current n\* every time.

**What would make me wrong, fixed now:**

- **If τ² falls below 0.02 once 4 or more batches have landed,** the two accidents were the outliers, not the
  distribution, and n\* collapses toward the sampling-only value of about 70. I will say so.
- **If any batch after 268 pooled keys moves the pooled share by more than 5 points,** the rule under-counted the
  heterogeneity, and I will say that too.

## What else is published, and why kappa as well

- **Cohen's kappa** is printed per batch and pooled.
- The pooled raw share is 53.6%, but the verdict classes are unbalanced, mostly `DELIBERATE`, `REPAIR-OWED` and
  `MEANING-HELD`. So agreement by chance alone is 28.9%, and the pooled kappa is +0.35: "fair" agreement, not
  "moderate". **The raw share sits about 25 points above chance (53.6 against 28.9), and the kappa is what says how much of it is agreement.**
- **Per batch:** keys, agree, raw share, a 95% Wilson interval and kappa.
- **Cumulatively:** pooled keys, agree, share, and how far the pooled share moved since the previous batch.
- **A batch's own `AGREE` column is never trusted.** Agreement is recomputed from the two verdict strings, and any
  mismatch is flagged.

## The input convention (for the seats filing the blind reads)

- A batch is one tracked file `DOUBLE_READ*.tsv` or `BLIND_READ*.tsv` anywhere under `computations/`.
- One row per key: `receipt <TAB> literal <TAB> verdict (first reader) <TAB> verdict (second reader)`.
- That is the shape 66's two files already use, so nothing about them changes.
- Batches are ordered by the commit that first added the file.

**Not done:** no verdict is read or adjudicated here. The 26 named disagreements are 66's, as ruled.
