# `r7297+70.2` — PRE-REGISTRATION: the score a candidate `REPAIR-OWED` rule is judged by, fixed before any rule is drafted

*Committed before any candidate rule exists. It answers `FOR_70.md` `r7297` (YOUR NEXT ORDER), read at `origin/main`
`a51b0476`.*

**Seen before this file:**

- 66's `RESULT.md`, `THREE_READERS.tsv` and the 47-key 69/60 batch.
- The ledger's class counts.
- The four quantities below, computed from `THREE_READERS.tsv` by `power.py`:

| quantity | value |
|---|---|
| per-key mean pairwise agreement on the 44 | **0.636**, sd **0.354** |
| keys unanimous / two-of-three / all differ | 21 / 21 / 2 |
| that score by prefix | `L210` 0.47, `P14` 0.61, `L150` 0.70, `L803` 0.76 |
| pairwise disagreements (of 132 pairs) | 48, of which **38** have `REPAIR-OWED` on one side |

*(66's class table sums to 47. The 48th is one `DELIBERATE`/`ENCODING-OK` pair. The `REPAIR-OWED` count of 38
agrees.)*

## ① The calibration set, fixed by name

`CALIBRATION_21.tsv` lists the 21 keys on which 69, cc66 and 60 agreed blind: **12 `REPAIR-OWED`, 5 `MEANING-HELD`,
4 `DELIBERATE`.**

- **C1 — a candidate rule is REFUTED by the calibration set** when any one of the 21 keys is re-decided. Re-decided
  means 2 or more of the 3 scoring readers, each applying the rule, give a verdict other than the unanimous one.
- Each reader's single misses are reported but do not refute.
- **Why this guards against collapse:** the set is mostly `REPAIR-OWED`. A rule that shrinks `REPAIR-OWED` by
  folding it into a neighbour fails here before its convergence is looked at.
- **Who applies it:** where a seat is available, the calibration keys are applied by readers other than 69, cc66 and
  60, since those three have read these keys. When one of them must be used, their calibration read is marked "not
  blind" and the majority test is taken over the other two plus it, with the mark in the report.

## ② The score, and what a rule has to beat

**The score S** is the mean, over the held keys of an arm, of each key's mean pairwise agreement among three blind
readers. A key scores 1 when unanimous, ⅓ when two of three agree, and 0 when all differ.

- This is the "pairwise convergence" 66 named. It carries three comparisons per key where unanimity carries one, so
  the same number of reads detects a smaller difference.
- Unanimity and Fleiss' kappa are reported beside it.

**The baseline is a concurrent no-rule arm, not a fixed floor.** I argue against 47.7%:

- **Unanimity is a property of the keys drawn.** By prefix the score runs from 0.47 to 0.76, a 29-point spread, and
  unanimity from 20% to 64%. A fixed floor is beaten or missed by which keys are drawn, by more than any effect worth
  testing.
- **47.7% is the unanimity of three particular readers,** and the pairwise rates of reader pairs differ by up to
  9 points. The scoring readers will be different seats.
- **So the comparison is S_B − S_A**, between:
  - arm **A**: no rule, the current class definitions only;
  - arm **B**: the candidate rule;
  - both read by **the same three readers**, on keys **randomised between the arms within each prefix**.

**The design, fixed now:**

- **Eligible keys:** ledger keys whose verdict is `REPAIR-OWED`, `DELIBERATE`, `MEANING-HELD` or `ENCODING-OK`. That
  excludes the 65 keys already double-read and the 21 calibration keys.
- **The draw:**
  - Sort eligible keys by `sha256(salt | receipt | literal)` and take the first `2n`.
  - Within each prefix, alternate A, B in hash order. An odd key out goes to the smaller arm, A on a tie.
  - **The salt is the full sha of the commit that lands the candidate rule's text.** The drafter cannot know the held
    set while drafting.
- **The readers:**
  - three seats, none of them a drafter of the rule, each blind to the ledger's verdict column;
  - each reads arm A **before** seeing the rule;
  - then arm B with the rule;
  - then the 21 calibration keys with the rule.

**The decision, fixed now.** A rule **CONVERGES READERS** when all three hold:

1. **C1 is not refuted.**
2. **The one-sided 95% lower bound of S_B − S_A is above 0.** Welch, normal reference, as simulated in `power.py`.
3. **Fleiss' kappa in arm B is at least arm A's.** Raw agreement rising while kappa falls is the signature of a
   collapsed class, and it refutes even when (2) holds.

Otherwise the rule is **REFUTED**, and the report names which condition failed.

## ③ The sample size for the three-way read

**The effect worth detecting: δ = 0.15.**

- On the 44, settling every `REPAIR-OWED` dispute would raise S from 0.636 to **0.924**. That ceiling is +0.29.
- δ = 0.15 is about half of it. A rule that settles less than half of the disputes it was written for does not repay
  redefining a class that sits on 350 ledger rows.

**The numbers** (formula n = 2σ²(z_α + z_β)²/δ², σ = 0.354, one-sided α 0.05, power 0.80, checked by 20,000
simulated draws per row):

| comparison | δ | keys per arm | keys | three-way reads |
|---|---|---|---|---|
| **rule against no rule** (registered) | **0.15** | **69** | **138** | **414** |
| rule against no rule, finer claim | 0.10 | 155 | 310 | 930 |
| rule against no rule, coarser claim | 0.20 | 39 | 78 | 234 |
| **two candidate rules** (two-sided, 95%) | **0.15** | **88** | **264** with the no-rule arm | **792** |

- **Simulated power at the formula's n:** 0.81 at 69, 0.80 at 155, 0.83 at 39. The approximation holds.
- **σ is conservative for arm B.** A rule that works pushes scores toward 1 and shrinks the spread. Arm A's σ is the
  one that matters, and it is checked in N3.
- **A difference between two rules is believable** only with both rules in one draw, against one no-rule arm, read
  by one set of readers. Two rules scored in separate draws differ by their draws as much as by their merits.

## ④ The symmetric negative: when the score cannot discriminate

I report that **the convergence score cannot discriminate at this size, and the campaign needs a different
instrument**, if any of these holds in arm A:

- **N1, ceiling:** S_A ≥ 0.85. There is less than δ of room above the baseline, so no rule can show δ.
- **N2, the readers are the effect:** the three pairwise rates in arm A span more than 0.15. Which pair reads a key
  then moves agreement as much as the rule is asked to. A rule's gain cannot be told from a change in who reads.
- **N3, noise:** the per-key sd in arm A is above 0.45. The required n grows as σ², so it would then exceed 1.6
  times the registered 69. The recomputed n is reported, and no verdict is given at 69.

**The different instruments, named now:** more readers per key (five, which cuts the reader term); or a within-key
design, where the same keys are read without and with the rule by disjoint reader triples. That needs six seats per
key, more than are free today.

## ⑤ My predictions for arm A, so the 44 can be wrong about the corpus

| # | quantity | central | band |
|---|---|---|---|
| P-a | S_A on the held set | 0.64 | 0.52–0.76 |
| P-b | unanimity in arm A | 48% | 33–63% |
| P-c | Fleiss' kappa in arm A | +0.44 | +0.25–+0.60 |
| P-d | share of arm A's pairwise disagreements with `REPAIR-OWED` on one side | 79% | 60–95% |

**If P-d lands under 60%,** the 44 overstated how much of the disagreement is `REPAIR-OWED`'s, and a rule for that
class alone has a lower ceiling than ③ assumed. I would say so before any rule is scored.

**Not done:** no rule is drafted, no held key is drawn, and no verdict is read or changed.
