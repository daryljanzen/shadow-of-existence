# `r7707+cc66` — REGISTERED BEFORE ANY COMPUTATION

**The order** (`r7707`, 69, on `PO-87`): P15 now says the law carries the step's size and not its
sharpness — where the measurement steps, the law ramps. **Where is the sharpness made?** Read the same
sliding windows on ⒜ the source-side ratio (the η-integrated sources) and ⒝ each arm's own projected
spectrum, and say whether the step's sharp transition is already in the source, is made in the
projection, or is a property of each arm's spectrum that survives the arm/control ratio.

---

## WHAT THE THREE READINGS ARE, IN THE INSTRUMENT THAT ALREADY EXISTS

`own_comb_kinds.own_state(banks, kind, win)` already returns, separately for each side, the normalised
oscillatory residual `(y − e)/e` on the comb coordinate, and `_rms(xs, o, a, b)` is the band RMS of **one
side**. The step statistic is `Ra/Rc − 1` of those two. So:

| reading | what it is | cost |
|---|---|---|
| ⓵ the step as the paper has it | `Ra/Rc − 1`, slid | already built (`r7703`, `1.6` s) |
| ⓶ **each arm's own spectrum** | `Ra` and `Rc` slid **separately** | ~free: the same `st` |
| ⓷ **the source-side ratio** | the same construction fed `(k·r_s/π, S_i)` from `r6911_source_*` | new comb fits on 2547 / 1452 points |

## ⛔ THREE THINGS THAT MUST BE SAID BEFORE A NUMBER EXISTS

### ① THE TWO ABSCISSAE ARE THE SAME VARIABLE ONLY UNDER THE PROJECTION THE QUESTION IS ABOUT

The spectra are read on `q = ℓ/l_A`; the sources on `k·r_s/π`. These coincide because
`l_A = π·D_M/r_s` (checked on the banks: `π·13954.35/145.382 = 301.57` against `l_A = 301.54`), so
`ℓ/l_A = k·r_s/π` **exactly when `ℓ = k·D_M`** — the flat-sky identification, which is the very
projection whose role is in question. ⇒ **A window at the same number on the two abscissae is the same
ACOUSTIC PHASE, not the same set of modes.** Any sentence that slides from one to the other without
saying so is reading the projection's own approximation as a fact about where a feature lives.

### ② THE PROJECTION ONLY BROADENS, AND `r7703` MEASURED BY HOW MUCH

`r7703` measured the law's own transition as some **seven times broader** at fixed smoothing than the
step. A linear projection with a window of finite width cannot sharpen. ⇒ **This makes the question
genuinely decidable in one direction and not the other:**
- a step found **broad or absent in the source** and **sharp in the spectrum** cannot have been
  inherited, so the sharpness is made at or after the projection — *a localisation*;
- a step found **as sharp in the source as in the spectrum** would be in tension with `r7703`'s
  seven-fold width, and is to be reported as a tension to explain, **not** as "the source did it".

### ③ WHAT COUNTS AS CONSISTENCY AND WHAT WOULD COUNT AS ATTRIBUTION — AND ATTRIBUTION IS NOT AVAILABLE HERE

- **CONSISTENCY** is two readings agreeing in location and width. That is all a shape match buys.
  `r7695` is on record for what happens when a shape consistency is read as attribution: a 99.9 per
  cent fall that was a uniform level shift.
- **ATTRIBUTION** would need a build that **removes the sharpness and leaves the rest**. P15 says the
  step is "very largely shared" between the arms, and `r7703` recorded that **no build removes a step
  the arms share**. ⇒ ⛔ **No attribution is available in this revision, and I register that now rather
  than discovering it after the figures are in hand.** What is available is a **LOCALISATION**: an
  ordering statement about where in the chain the sharp transition first appears. Weaker than
  attribution, stronger than nothing, and it is what the answer will be worded as.

## REGISTERED PREDICTION

**The step is a property of each arm's own spectrum, not of the ratio.** `Ra` and `Rc` slid separately
will each show a transition near `q ≈ 1.78`, of comparable width, and the ratio's step will be what
survives their imperfect cancellation. *Reason it is predicted and not assumed: P15 already states the
step is "very largely shared" between the arms, and a feature shared by both sides of a ratio is a
feature of each side.* **If instead one side steps and the other does not, the step is an arm/control
contrast and "very largely shared" is the sentence that needs looking at.**

On the source: **the source-side ratio will show no sharp transition at `q ≈ 1.78`** — either no
transition or one materially broader. *Reason: P15 already says the excess is not in the source.*

## ⚠ ONE PRECONDITION TO BE TESTED, NOT ASSUMED

The normalisation `(y − e)/e` requires the running envelope `e` not to pass through zero. It is safe on
`D_ℓ`, which is positive. **`S_i` is a signed source and its envelope may cross zero**, in which case the
normalised residual blows up and the reading is meaningless rather than wrong-looking. The retention
statistic uses `S_i**2` for exactly this reason (`r7637`'s `S2 = source S_i**2`). ⇒ **Which of `S_i` and
`S_i**2` is read will be stated, the zero-crossing checked explicitly, and if both are readable both are
reported — they are different objects and a step in one is not a step in the other.**

## PRICE, AND WHERE THE BLOCK GOES

Registered: ⓶ is free and ⓷ is two comb fits plus one slide, so **under 10 s added** to
`P15_a_source_with_no_physics…` (whose `r7703` block is `1.6` s inside a `≈ 2` s receipt). If it lands
over that, the block takes its own receipt and pays the landing — the same rule as `r7703`, and the
baseline is measured first, into `BASELINE.md`.

## FAILABILITY

Each gate perturbed and the named check watched go red, over a **green control run first** — and a leg
reporting `0` FAIL means the perturbation went **towards** the gate, which is `r7705`'s leg A and
`r7703`'s leg B. ⛔ *The locator returns a window rather than a location when the curve it is given has
no transition (`r7703`'s withdrawal), so every "no transition here" below is to be established by the
TRANSLATION control — translate the read interval and see whether the located point moves — and never by
the locator returning a number.*
