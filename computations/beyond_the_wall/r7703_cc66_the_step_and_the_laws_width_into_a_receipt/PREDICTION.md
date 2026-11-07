# `r7703` (cc66) — PREDICTION

Registered before a line of this revision's computation exists. Order `r7703` (69): make
`step_vs_departure` a receipt or a block of `P15_a_source_with_no_physics…`, pinning the two
half-rise locations, the two lowest-band ratios, the fixed-smoothing width contrast *as the ratio it
is*, and the statement that the `q ≈ 1.9` residual is that width error; then draft three sentences,
each figure with its licence, saying what is attribution and what is not.

## ① THE PRICE, MEASURED BEFORE THE DECISION IS TAKEN — AND IT DECIDES WHERE THIS LIVES

| | measured |
|---|---|
| `P15_a_source_with_no_physics…` as it stands | **`4.3` s** |
| `step_vs_departure.py` as it stands | **`49.2` s** |

⇒ **As written, hosting it would take the receipt from `4.3` s to about `53` s — a `12 ×` increase.**
⌗ *`r7693` is why this is measured and not estimated: there I quoted `37` s for a scan that was
already banked, "an estimate of the wrong computation made without reading what the file already
held".*

## ⛭⛭ ② AND ALMOST ALL OF THAT `49` SECONDS IS REDUNDANCY I CAN REMOVE — WHICH IS WHY I AM NOT YET CHOOSING A SEPARATE RECEIPT

`band_excess_own_kind` recomputes `_combs(banks)` **and both running envelopes over the whole fine
spectrum on every call**, and only the `_rms` over the one interval depends on the interval. The
slide calls it `43 × 3 = 129` times. ⇒ **129 comb fits and 258 envelope passes for 129 interval
reads.**

⚠ *This is the step receipt's own cost too — it slides the same way — so the inefficiency is
pre-existing and not mine.* ⇒ **I register the plan as: add an optional precomputed-state parameter
to `own_comb_kinds.band_excess_own_kind`, additive and default-inert**, so the comb and the envelopes
are built once per half-width. *It is my own module (`r7639_cc66_…`), so extending it is inside this
seat's own work and not a widening of someone else's instrument.*

**Registered prediction: the slide drops below `5` s, so the block goes into the host receipt and no
INDEX row, appendix regeneration or PDF recompile is owed.** *Moderate confidence on the number; high
on the direction.* ⛔ **If it does not drop below about `15` s, I take the separate receipt instead
and pay the INDEX and appendix cost**, rather than making a `4.3` s receipt a minute long to save
myself a landing.

## ⛔ ③ THE INERTNESS GATE, BECAUSE THIS IS A SHARED MODULE AND I HAVE JUST BEEN TAUGHT THIS

**The step receipt imports that module.** ⇒ *** Before and after the change, `P15_the_step_is_the_
excesss_own…` must produce BYTE-IDENTICAL output. *** ⌗ *Not "it should be inert" — measured, the way
`r7699+cc66.5`'s snapshot edit was measured across 330 arrays, and for the reason `r7655` records:
an additive change to a shared file is a different file by the corpus's own standard.*

⛔ **And the sharper version of the same lesson, one revision old:** at `r7701` I repaired a locator by
changing its rule globally and moved the half-rise off the second acoustic peak — **the figure that
instrument is validated against.** ⇒ **So the half-rise this receipt pins is checked against
`1.7775` in the receipt itself**, which makes the validating figure an assertion rather than something
I have to remember to print.

## ④ WHAT I REGISTER THAT THE PINS WILL SAY — read off `r7701`'s measurement, to be recomputed here

| pin | value |
|---|---|
| the step's half-rise | `1.7830`, within `0.3` per cent of the second peak's `1.7775` |
| the law's transition | `1.8021`, within two per cent of a comb period of the step's |
| the lowest-band ratios | `0.4771` measured, `0.4816` under the law — agreeing to `0.9` per cent |
| the width contrast | the law's 25–75 rise is `≈ 7 ×` the excess's **at fixed smoothing** |
| the excess's transition | **unresolved at every window**: below the window's own floor at all three half-widths |

⛔ **What I will not do with them.** *The step's factor measures `1.77`–`1.83` against a registered
`1.9`–`2.2` and is already recorded as missed at `r7639` ⑤; it is not re-toleranced here and not
quietly dropped either. And the width contrast is pinned as a RATIO AT FIXED SMOOTHING and never as
two widths — a 25–75 rise out of a sliding window is bounded below by the window, so "the step is
`0.08` wide" is a number beneath its own floor.*

## WHAT WOULD MAKE ME WRONG IN A WAY THAT MATTERS

**The licence, and it is the whole of item 2.** *Three sentences go to 69, and the tempting one is
that the law's width error **explains** the `q ≈ 1.9` residual.* ⇒ **What is measured is that the
residual IS that width error** — the two are the same quantity read two ways, which is an identity
and not an explanation. ⛔ *And the attribution limit stands exactly where `r7701` registered it: no
build removes the step, so nothing here attributes the step's sharpness to any mechanism. **If I
draft a sentence that reads as a cause, that is the error, and it is the third revision in which the
same temptation is the thing to watch.***
