# `r7315+70.2` — PRE-REGISTRATION: the WIDENS arm re-registered on a subject that is a property of the text. It reads each applier's own text-alone stratum, and attributes a widening to the text only through a crossover that holds the reader fixed and varies the text

*It answers `FOR_70.md` `r7315` (YOUR NEXT ORDER ②), read at `origin/main` `619a4753`.*

- *It applies to the next text scored after the second redraft (`6bef6fd5`). No such text exists when this is
  committed.*
- ***`r7311_70_redraft2_score/PREDICTION.md` is not revised.** It is the record of the second round, and is scored as
  written in `RESULT.md` beside it.*
- *Everything in it carries over except the WIDENS arm and N-J, which this file replaces.*

## Why the drift guard 66 suggests cannot be the guard

**Per applier, the text-alone share on the keys both decide is exactly 100 minus that applier's flag rate.** On the
second redraft:

- 71's text-alone stratum widened +20.6 (66's ruling ③);
- 71's flag rate fell −20.6, which fires my N-J.

**They are one number read twice.** A drift guard on each applier's flag rate, set beside a per-applier widening,
vetoes every widening it would otherwise credit. **What separates text from habit has to come from outside the flag
count.**

There are two such sources:

1. **Agreement on the stratum.** A reader who flags less from habit moves harder keys into its text-alone stratum, and
   its agreement with the other reader there falls. A text that settles them does not lower it.
2. **A crossover.** The same reader, at the same time, applies the previous text to fresh keys. Habit is then held,
   and only the text varies.

## The arm, fixed now

**For each applier `w`:**

- **`T_w`** is the share of the keys both decide that `w` decides without flagging judgement.
- **`A_w`** is the owedness agreement between the two appliers on `T_w`'s keys.
- Both are reported for each applier, with the union and the intersection (S0) beside them.

| | condition |
|---|---|
| **WIDENS for `w`** | the Wilson **lower** bound of `T_w` is above `w`'s second-redraft point: **70 at 40.0%, 71 at 80.0%** |
| **NARROWS for `w`** | the Wilson **upper** bound of `T_w` is below that point |
| **HOLDS for `w`** | the Wilson lower bound of `A_w` is above **73.8%** |
| **DILUTES for `w`** | the Wilson lower bound of `A_w` is 73.8% or below |

## The crossover, which attributes it

**Who and what:**

- Each applier applies the **previous** text (`6bef6fd5`) to **40 crossover keys**.
- The keys are drawn by `r7303_70_redraft_score/draw.py`'s rule with the salt `<next text's sha>|crossover`. They are
  disjoint from the held set and from every earlier draw.

**Order:**

1. The crossover is applied **first** and committed **before** the applier opens the new text.
2. For 70, fresh applier agents carry no memory either way.
3. For 71, applying the old text first means the new text cannot leak into it.

**The quantity:**

- **`X_w`** = `w`'s flag rate on its decided crossover keys under the old text, minus `w`'s flag rate on the decided
  held keys under the new text.
- It is read by the **Newcombe** 95% interval for a difference of two proportions, built from the two Wilson
  intervals.
- **At 40 keys against 65,** a 40% versus 20% difference gives an interval of 2.3 to 37.3, so it can be shown.

**The verdict:**

| | condition |
|---|---|
| **TEXT** | the Newcombe interval of `X_w` lies above 0: the new text needs less judgement from the same reader |
| **NOT ATTRIBUTED** | it contains 0 |
| **AGAINST** | it lies below 0 |

**The verdict for each applier reads off the triple:**

| verdict | condition |
|---|---|
| **WIDENED BY THE TEXT AND HELD** | WIDENS, TEXT, HOLDS |
| **WIDENED, NOT ATTRIBUTED** | WIDENS and HOLDS, but the crossover cannot separate text from habit |
| **WIDENED BUT DILUTED** | WIDENS and DILUTES |
| **NOT WIDENED / NARROWED** | as read |

**What replaces N-J:** an applier is reported as **HABIT** when its flag rate on held keys moves by more than 20
points between rounds while `X_w` is NOT ATTRIBUTED. That means the reader moved and the text did not move it.

## Predictions, so they can be wrong

| # | quantity | central | band |
|---|---|---|---|
| W-a | `T_70` | 45% | 33–58% |
| W-b | `T_71` | 82% | 70–92% |
| W-c | `X_70` | +5 pts | −10 to +20 |
| W-d | `X_71` | +5 pts | −10 to +20 |
| W-e | `A_w`, both appliers | 95% | 88–100% |
| W-f | verdict | **NOT WIDENED** for both, HOLDS for both | — |

**My reasons:**

- 71's silent places are mostly decided in writing now, so 71 is near its ceiling.
- 70's flags are about what a claim is, not about where the text is silent. A redraft aimed at silences moves 70
  little.
- The crossover difference should therefore be small for both.

**Not done:** nothing is drawn, since the salt does not exist. Nothing is applied, and no ledger row is read.
