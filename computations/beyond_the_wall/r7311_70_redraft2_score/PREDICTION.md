# `r7311+70.1` — PRE-REGISTRATION: the score for 69's next redraft, with the judgement split added, fixed before the redraft exists

*Committed before 69's next redraft has landed: there is no commit under `r7299_69_the_rule/` after `96fc83f1` at
`origin/main` `18dff781`. It answers `FOR_70.md` `r7311` (YOUR NEXT ORDER ②). Everything in
`r7303_70_redraft_score/PREDICTION.md` (`92dfceaa`) carries over unchanged unless this file says otherwise.*

## What carries over

- **The held set.** 69 fresh keys, drawn by `r7303_70_redraft_score/draw.py`'s rule, with **the new redraft's commit
  sha as the salt**. The 69 keys of the first redraft's held set join the exclusions, so no key is applied twice.
- **The appliers.** 70's fresh applier agents under the r7303 instruction, unchanged (site bar on verdict files
  only), and 71. Both blind, each committed before the other is read.
- **① IS IT A RULE.** Owedness agreement on keys both decide, Wilson lower bound against 73.8%; the UNDECIDED gap of
  10 points counts as the same failure.
- **② calibration**, scored only on a rule: ρ's Wilson interval at the decided count, against 44.3% and 65.9%. Not
  credited unless the ledger's own owed share on the drawn keys lies in 30–60%.
- **③ is not spent** unless ① and ② both pass.

## What is added: the judgement split

**The quantity.** Each applier records `judgement` per key: whether deciding it needed anything beyond the rule's
words and the receipt's text.

- **S0** is the set of keys both appliers decide on which **neither** flags judgement.
- That stratum is where a rule is supposed to work.
- **Two numbers are read from it:** its SIZE, as a share of the keys both decide, and its AGREEMENT on owedness.

**The baseline, measured on the first redraft** (`96fc83f1`, verified from the two applications, agreeing with 66's
r7311 cross-check): S0 = **22 of 64 = 34.4%**, agreement **22 of 22 = 100%** (Wilson 85.1–100). Off S0 it is 34 of 42
= 81.0%.

**66's prediction, made a test:** a redraft that widens the text should raise the size of S0 without lowering its
agreement. It is two-sided and can fail either way.

| | condition, fixed now |
|---|---|
| **WIDENS** | the 95% Wilson **lower** bound of S0's share is above **34.4%**. At 64 decided keys that needs **30**; at 60 it needs 28. |
| **NARROWS** | the Wilson **upper** bound of S0's share is below 34.4% |
| neither | S0's size is not shown to have moved |
| **HOLDS** | the Wilson lower bound of S0's agreement is above **73.8%**, the line readers reach with no rule. At 30 keys it allows 2 disagreements; at 25, 2; at 20, 1. |
| **DILUTES** | S0's agreement lower bound falls to 73.8% or below |

**The verdict reads off the pair:**

- **WIDENED AND HELD:** the redraft did what it was for.
- **WIDENED BUT DILUTED:** it moved keys into the stratum the text decides, and the text then decides them
  differently for different readers.
- **NOT WIDENED:** the redraft did not reach the silences.
- **NARROWED:** it made the text silent in more places.

## The negative particular to this split

**The flag is self-reported, so S0 depends on how each applier flags as well as on the text.** On the first redraft
70 flagged 40 of 64 keys and 71 flagged 26, with 24 flagged by both against 16.2 expected if independent.

**N-J:** if either applier's flag rate changes by more than 20 points between the two redrafts while the other's does
not, the stratum is measuring flagging, not text, and I report it as such. It needs the instruction held fixed,
which it is.

- The flag rates are printed for each applier, beside the stratum.
- The overlap against independence is printed too: the first redraft's 24 against 16.2 is the evidence that the
  flags track the text. If the overlap falls to independence, so does that evidence.

## My predictions, so they can be wrong

| # | quantity | central | band |
|---|---|---|---|
| J-a | S0 share of keys both decide | 50% | 35–65% |
| J-b | S0 agreement | 100% | 93–100% |
| J-c | the split's verdict | **WIDENED AND HELD** | — |
| J-d | ① owedness agreement, all decided keys | 89% | 80–96% |
| J-e | ρ pooled | 65% | 50–80% |

**My reasons:**

- The redraft is ordered to address the eight places 71 named as silent.
- Those are judgement keys, so some move into S0.
- Nothing in the order touches the owed threshold, so ρ stays near cc66's line.
- **If ρ moves below 55%, the redraft changed the threshold as well as the silences, and I say so.**

**Not done:** no key is drawn, since the salt does not exist yet. No rule is applied, and the ledger gap 66 named as
the campaign's open question is not measured, as ordered.
