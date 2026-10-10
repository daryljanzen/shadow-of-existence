# `r7251+70.0` — PRE-REGISTRATION: does a repair form exist for a paper-meaning pin?

*Committed before any of 60's `REPAIR-OWED` literals or reading notes is opened. Only counts have been taken.*

## The population, and a difference from the order's number

The order says **171**. In the baseline at `origin/main` `3bf0ac52`, 60's `r7252` `REPAIR-OWED` verdicts on
`L221_the_bridge` are **171 = 162 `PAPER`/`SENTENCE` + 9 `PAPER`/`TOKEN`**. A further 2 `PAPER`/`SENTENCE` keys
were verdicted by `r7135+70.1`, which was this seat.

- **The meaning-pin population is the 162 `PAPER`/`SENTENCE` keys.**
- **The 9 `TOKEN` keys are the formula case**, which cc66's normaliser already answers. They are out of scope.

## How the member is picked, and why that is not "the easiest"

**I do not pick. A seeded draw does.**

- **The draw:** `random.Random(0x3bf0ac52)`, the first 8 hex digits of the `origin/main` commit this order arrived
  in. It draws **3** of the 162 without replacement, from the keys sorted by (receipt, literal).
- **Why three:** attempting the form on all three means a form that works only on the most tractable member shows
  up as one of three, not as one of one.
- **The representativeness check, stated before the draw:**
  - Each drawn literal's word count is reported against the population's quartiles.
  - So is its receipt's share of the 162.
  - If all three fall in one quartile, I add a 4th draw from the same RNG stream, and say that I did.

## The candidate form, named before it is tried

**A CONTENT SKELETON, the sentence analogue of cc66's normaliser.** A sentence's finding is carried by:

- its content-bearing tokens: named objects, symbols, numbers;
- its polarity markers: *not, no, never, only, without*.

The prose around them is not the finding. The repaired gate asserts that **one sentence of the paper contains
every skeleton token together with the polarity**, after cc66's markup normaliser.

It is accepted on a member if, over seeded mutations of the paper sentence:

| | mutation class | the gate must |
|---|---|---|
| (a) | the original paper | stay GREEN |
| (b) | content-intact rewordings: synonym swaps of non-skeleton words, clause reordering, markup changes, sentence split at a clause boundary | stay GREEN on ≥ 90 per cent |
| (c) | content-breaking edits: polarity flipped, a skeleton object swapped for another the paper names, a number changed | go RED on ≥ 90 per cent |

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| R1 | members of the 3 on which the skeleton form passes (a)–(c) | **2** | 1–3 |
| R2 | (b) green rate over all three | **90%** | 75–100 |
| R3 | (c) red rate over all three | **80%** | 60–100 |
| R4 | the failure shape, if a member fails | **a RELATIONAL claim whose direction or kind is carried by word order or a verb**, such as "X is a case of Y" against "Y is a case of X" | — |

## ⛔ The reachable negative, which the order names

**If the form fails (c) on a member**, the skeleton cannot tell the finding from its negation or its
converse. That member's meaning then cannot be gated without pinning its wording.

- **The 48th member and a sixth verdict** are reported if the failure is **structural**: if it holds for every
  relational sentence of the shape R4 names.
- **They are not reported if it is incidental**, meaning one more skeleton token would fix it.
- **To keep the result from being re-run until it passes:** I will check whether the failing shape is
  structural by counting how many of the 162 share it, and that count is reported either way.
