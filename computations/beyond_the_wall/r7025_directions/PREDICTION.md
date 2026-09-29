# PRE-REGISTRATION — r7025+cc66.64

**Committed before any of `cc66.64` was computed.** *Nothing below was run first and written after.*

---

## ⛔ WHAT IS ALREADY IN HAND, SO IT IS NOT TABLED AS OPEN

*Three facts are settled and this file does not re-derive them. Stating them here is the discipline
`cc66.62` established: declare what is known before tabling what is not, so a "finding" cannot be a
fact I already had.*

1. **`P15` records that the contrast excess carries about three quarters of the likelihood's excess.**
2. **`cc66.63` located that cost at bands 4–7** — band 1 carries under one per cent and changes sign
   under shape absorption; bands 4–7 carry roughly six sevenths.
3. **`cc66.58` measured the excess at bands 2–7 featureless — a constant fits it — *on the band
   statistic*.** ⌗ *The band statistic has seven numbers across the range. The likelihood bins
   thirty-four times finer. "Featureless" is therefore a statement about the banding until it is
   asked again at the finer scale, which is `⓶`.*

⚠ ***AND `cc66.61`'s FLOOR AND THE BAND-1 RESULTS ARE FINISHED WORK.*** *They are landed. They are
not re-derived here, not restated as new, and not re-opened.*

---

## ⛭ THE DECOMPOSITION THIS REVISION USES, AND WHY IT REPLACES `cc66.63`'s

`cc66.63` read per-band excess by inverting each band's own covariance block. **Those contributions
did not sum to the total** — 287 against 322 — because the covariance couples bins across band
edges and each block was inverted alone. *I quoted that gap rather than eliding it, and it is a real
limitation of that estimator.*

⇒ **There is an exact alternative and this revision uses it.** With `r_a`, `r_c` the residuals of arm
and control against the data and `d` their fitted difference:

    r_a = r_c − d   ⇒   χ²(a) − χ²(c) = dᵀF d − 2 dᵀF r_c

**⇒ so the excess decomposes over bins EXACTLY, with no block inversion:**

    excess_i = d_i · ( F ( d − 2 r_c ) )_i        and        Σ_i excess_i = χ²(a) − χ²(c)  identically

⌗ *This also separates the two things the row has been confusing all along: `dᵀF d` is the separating
power squared, and `−2 dᵀF r_c` is the part that depends on where the data actually sits. **A
quantity can be large in the first and nothing in the second**, which is precisely `cc66.63`'s
finding stated algebraically.*

⛔ **AND THE NEW ESTIMATOR IS CHECKED AGAINST THE OLD, NOT SUBSTITUTED FOR IT SILENTLY.** *The
per-band sums of `excess_i` are reported next to `cc66.63`'s block-inverted numbers. If they
disagree beyond the coupling gap already quoted, that is a finding against this file and it is
reported as one.*

---

## ⚠ THE VOCABULARY TABLE, CARRIED FORWARD AND NOW THREE COLUMNS WIDE

*66 required this and it has now bitten three times, so it is stated before any number is produced.*

| quantity | what it is | where it lives |
|---|---|---|
| **SEPARATING POWER** | how well the data could tell two candidate spectra apart | `dᵀF d`, no reference to where the data sits |
| **SIGNIFICANCE** | the size of a departure against its own trend, in some metric | a ratio within one instrument |
| **EXCESS** | `χ²(arm) − χ²(control)` — what the data actually rejects the arm on | `dᵀF d − 2 dᵀF r_c` |

⛔ ***`⓵` IS SCORED ON THE THIRD, AND NO COLUMN IN THIS REVISION MIXES TWO.*** *A share below is a
ratio of two EXCESSES and of nothing else.*

---

## ⓵ THE CHANNELS SCORED AT BANDS 4–7, ON THE EXCESS

*Each channel `k` (window weighting, term mix, the realised JOINT pair) is a modified control
spectrum. Its excess decomposes the same way with `d_k = fit_k − fit_c`. The share at a band is
that channel's excess there over the arm's excess there.*

### ⛔ TABLED FIRST: THE OUTCOME THAT COSTS THIS SEAT MOST

***NO CHANNEL ACCOUNTS FOR THE COST.*** *Shares at bands 4–7 small, or sign-unstable, or wrong-signed
— the channels move the separating power (where `cc66.63` found all three matching the arm at 1.31,
0.86, 0.51) and move nothing where the data actually rejects the arm.*

⇒ ***THAT IS THE AMENDED CLAUSE MET AND IT CLOSES THE ROW.*** *`PO-56` now reads "terminates if no
quantity this construction fixes produces the contrast excess in the bands where the likelihood
rejects the arm." If the three channels this construction fixes account for none of it, the clause
is met and the row closes negative.*

⚠ ***AND THAT IS THE EXPENSIVE ANSWER FOR ME.*** *It retires three candidates I reported last
revision as the first ever to depart the arm's way, and it does so by saying the metric they matched
in was not the one that decides. **I am tabling it first for exactly that reason.***

### THE OUTCOME THAT ENDS THE ROW THE OTHER WAY

***A CHANNEL ACCOUNTS FOR THE COST*** — a share at bands 4–7 near unity, stable across bands and not
an artefact of one band. *Then the carrier is identified in the likelihood's own metric, which is
what the clause says would discharge it.*

### AND THE THIRD, WHICH IS NEITHER AND MUST BE SAYABLE

***THE SHARES ARE LARGE BUT THE PAIR CANCELS*** — singles accounting for much of the cost and the
realised `JOINT` accounting for little. *That is the cancellation this row has now measured twice
elsewhere appearing a third time, and it would make cancellation a property rather than a
coincidence. ⛔ It discharges nothing: a carrier that cancels is not a carrier.*

⌗ **The cancellation is MEASURED, not read off two significances** — singles against the realised
pair, with product, sum and quadrature all reported and none chosen in advance.

---

## ⓶ DOES THE EXCESS AT 4–7 HAVE ANY STRUCTURE IN THE LIKELIHOOD'S METRIC?

*`cc66.58` says featureless on seven band numbers. The likelihood's bins are a thirty-fourth of a
comb period. **This is the same question the step turned on, asked at the other end of the range.***

**Three tests, fixed now, none chosen after seeing the answer:**

1. **Against a constant** per bin across 4–7 — `cc66.58`'s claim at the finer scale.
2. **Against a smooth trend** in `ln ℓ` — because a slow gradient is not "structure" in the sense
   that matters, and must not be allowed to masquerade as one.
3. ⛭ **Against the acoustic comb** — project the per-bin excess onto `cos`/`sin` at the comb period
   in `q`, the same period the step lives at. *If the cost is modulated at the acoustic period, that
   is structure in the part that carries the cost, and the order is right that it is the most
   valuable thing available here.*

⛔ **AND THE CONTROL AGAINST FINDING STRUCTURE THAT IS NOT THERE.** *A χ²-like quantity summed over
many bins always has scatter, and a projection onto any smooth basis always returns something.*
⇒ ***The comb amplitude is scored against the amplitude the same projection returns at NEIGHBOURING,
WRONG periods*** — a null distribution built from the same data, so "structure" means an excess over
what the estimator produces on periods that carry no physics. *If band 1's lesson taught anything it
is that more freedom always produces a number.*

⚠ **AND IF THE ANSWER IS NO STRUCTURE, THAT IS THE RESULT AND IT IS REPORTED AS ONE.** *A featureless
excess at the bands carrying six sevenths of the cost says the rejection is a level, not a shape —
and a level is not something an acoustic construction produces.*

---

## ⓷ AND NOTHING ELSE

*No new candidate. No mechanism. No corpus edits — routed for 66 to place. `cc66.61`'s floor and the
band-1 results stay landed and are not re-derived. No basis and no aggregation chosen where the row
has been holding several.*

---

## ⛔ WHAT WOULD MAKE THIS FILE WRONG

* *If the exact decomposition disagrees with `cc66.63`'s block-inverted bands beyond the coupling gap
  already quoted, the new estimator is wrong or the old one was, and that is reported before
  anything is built on it.*
* *If a share at bands 4–7 depends on which shape-absorption order `n` is used, the share is not a
  property of the channel and must not be quoted as one.* ⌗ *This is `cc66.63`'s sign-flip lesson
  applied before it can bite rather than after.*
* *If the comb amplitude at 4–7 does not exceed what the same projection returns at wrong periods,
  there is no structure and the projection found its own noise.*
