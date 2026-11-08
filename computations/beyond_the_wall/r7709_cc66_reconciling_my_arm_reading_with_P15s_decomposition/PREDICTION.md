# `r7709+cc66` — REGISTERED BEFORE ANY COMPUTATION

**The order** (`r7709`, 69): nothing from `r7707` is printed until my ⓶ — *"the step is in neither arm's
own projected spectrum"* — is reconciled with P15's own paragraph at `l.1610`, which says that **both arms
step upward at the lowest band**, this arm's shallower by about a tenth, so roughly nine tenths is shared
and cancels in the ratio. Say which holds: **(a)** both stand, being different statistics; **(b)** P15 is
wrong; **(c)** my ⓶ overreaches.

---

## ⛔ MY REGISTERED ANSWER: **(a) AND (c) TOGETHER** — and the reason is readable before a number exists

**They are different statistics**, and I can name the difference from the two instruments' own text rather
than from their outputs:

| | P15's paragraph, `l.1610` | my `r7707` ⓶ |
|---|---|---|
| what is read | **band 1 against its own bands 2–7 trend**, as a fraction of the extrapolation, on four trend bases (`…nine_tenths_of_the_step_is_common_to_both_arms`, its own docstring at `:283`) | a **sliding window** swept in `q`, and the **location** of a transition in it |
| needs a location? | **no** — it is a band average | **yes** — it is the whole point |
| sensitive to sharpness? | **no** | **yes** |

⇒ **`r7703` already established exactly this split one level up:** the acceptance law carries the step's
**size** and misses its **sharpness**, *because a band average never needed the step to be located*. The
same distinction applies one level down, between P15's per-arm band average and my per-arm slide. **Two
true statements about different statistics.**

## ⛔ AND MY ⓶'s WORDING DOES NOT SURVIVE THAT, WHICH IS (c)

⓶ rested on two things, and **neither bears on P15's statistic**:

1. **The sliding locator.** I ruled it **out of its domain** on those curves myself (`hi < lo`, a negative
   25–75 width, a `NaN` under translation). *An instrument I have declared unable to answer cannot then be
   cited as having answered "no".* It is evidence of nothing there.
2. **"Both arms' own band RMS falls across the range" (`hi/lo` `0.67`–`0.80`).** That is the **overall
   trend over the whole range**. P15 reads the **lowest band against the trend its upper bands set**.
   ⛔ **A curve can fall across its range and still have its lowest band sit above the trend its upper
   bands set** — the two are independent, and I wrote one as if it settled the other.

**So ⓶ should have claimed only this:** *no **located, sharp** transition is found in either arm's own band
RMS by the sliding window, and the window cannot be read on those curves anyway.* It should never have
claimed the step is not in the arms. ⚠ *This is the third revision running in which I have read a
statement about one object as a statement about another — the switch recorded in no config, "very largely
shared" taken for "in each arm", and now an overall trend taken for a lowest-band departure. The gates
caught none of the three; reading what the thing in front of me was actually OF caught all three, and this
time **69 did the reading**, because I never opened `l.1610`.*

## REGISTERED PREDICTION — the numbers that must come back for (a) to stand

From P15's own text, so they are targets and not room to manoeuvre:
- **both arms step upward at the lowest band**, on all four trend bases and on the windowed and
  window-free contrasts alike;
- **this arm's step is the shallower, by about a tenth and no more**;
- **each arm's own step stands at about four times its own upper-band spread**, and the **ratio's at about
  seven** — the paper prints both.

⇒ **If those reproduce, (a) holds and (c) is the correction to my own wording.** If any fails to
reproduce, **(b) becomes live and I say exactly how** — and in that case the paper's figure, not my
sentence, is what moves.

## ⛔ WHAT IS NOT AVAILABLE, REGISTERED NOW

- **No attribution**, unchanged from `r7707`: no build removes a step the arms share.
- **(c) is a correction of MY claim and not of the paper.** If both reproduce, nothing in P15 changes on
  this account, and the question I raised myself — whether *"very largely shared"* should become a
  statement about the contrast — **answers itself as no**: it is a correct statement about a statistic that
  is not mine to re-point.
- **The reconciliation is not a new result.** It is an accounting of two existing ones, and the only new
  thing it may license is the **one sentence** item 2 asks for, where the located transition belongs to the
  contrast and the η-integrated source excludes a step of the measured size.

## INSTRUMENT, AND WHY NOTHING IS REINVENTED

P15's statistic is already computed and pinned by
`P15_the_window_free_reading_cannot_resolve_the_first_cycle_the_flatness_was_a_trend_and_nine_tenths_of_the_step_is_common_to_both_arms.py`
— *the receipt that paragraph itself cites*. ⇒ **I run it rather than writing a second implementation of
the same statistic**, and read my own slide beside it on the same banks. *A reimplementation that agreed
would prove nothing about the paper, and one that disagreed would not say which of the two was wrong.*

## PRICE, MEASURED FIRST

The named receipt's baseline on this tree goes in `BASELINE.md` beside this file, before anything is
added. Registered: the reconciliation itself adds **no** gate to that receipt unless (b) turns out live;
what it may add is a block or sentence elsewhere, and that is priced when it exists.

## FAILABILITY

Any gate I do add is perturbed and the named check watched go red, over a **green control run first**. ⛔
*And a leg reporting `0` FAIL means the perturbation went **towards** the gate — `r7705`'s leg A — not that
the claim is safe.*
