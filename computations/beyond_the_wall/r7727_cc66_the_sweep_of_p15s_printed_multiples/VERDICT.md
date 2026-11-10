# `r7727+cc66.2` VERDICT — **the sweep finds NO P15 printed claim that fails. One receipt wording defect, found and fixed.**

The search ran exactly as `PREDICTION.md` registered it. `73` candidate lines, bucketed **mechanically** so
the classification could not be hand-picked. Outputs in `sweep_output.txt`, `classify_output.txt`,
`sensitivity_output.txt`.

---

## ① THE SWEEP, all `73` bucketed

| bucket | n | why |
|---|---|---|
| **SETTLED** (registered exclusion ⒜) | `2` | lines `1401`, `1404` — the located step and the narrowed source exclusion, this sweep's **precedent** and not new findings |
| **IN SCOPE by wording** | `6` | `957`, `1779`, `1826`, `1862`, `1863`, `2059` |
| OUT: quoted or external error | `10` | the denominator is a `\pm` measurement error, the sky's own precision, or a noise expectation — **fails criterion 2** |
| OUT: no multiple formed | `55` | a `\sigma` figure not divided by a correlated-family spread |

⌗ *Three of the six in-scope sites (`1826`, `1863`, `2059`) I had **missed** when I filtered by reading
before writing the classifier. That is why the registration said the patterns' union is the list.*

## ② THE SIX, READ SITE BY SITE

| line | verdict |
|---|---|
| `957` | ⛔ **not a multiple** — *"is spread across the range"* is a verb phrase describing the disagreement's distribution, not a denominator |
| `1826` | ⛔ **not a multiple** — *"multipoles spread across the reported range"* describes where they lie |
| `1862` / `1863` | ⛭ **"a ratio, not tested"** — the **seven-band** family, registered exclusion ⒝: `7! = 5040` floors at `3.72` sd-equivalent. And no evidential multiple is printed anyway; the claim rests on a **count** (*"six of the seven bands inside"*) |
| **`1779`** | ⛭ **a genuine multiple**: `+0.0103` slope over a `0.00137` spread across **twelve envelope settings** = **`7.55`**, printed as *"seven and a half times its own spread across those settings"* |
| **`2059`** | ⛭ **two genuine multiples**: **`2.23`** of its own band spread and **`5.14`** of its own regression error, over a **six-member** family |

## ③ DOES THE CALIBRATED TEST APPLY? — **NO, at both live sites, and that is reported rather than improvised**

`r7717`'s ruled test calibrates **a step on an autocorrelated curve** against step-free phase-randomised
surrogates. At `1779` the statistic is a **slope across acoustic bands** with a **setting-spread**
denominator; at `2059` it is a **difference of fitted slopes across a one-parameter family** with a **fit
error**. ⇒ **Different statistic, different denominator. The ruled test does not reach either.**

⛔ **`PREDICTION.md` §5 forbids improvising a replacement, so none is built.** What *is* applied is
`r7717`'s own form — report the figure under each admissible denominator — using only values the cited
receipts already **gate**.

## ④ WHAT THAT FORM SHOWS

| | printed | at the family's other end |
|---|---|---|
| `2059` level | **`2.23`** (band residual `0.00949`, the minimum) | **`0.50`** — *below one* (at `f=0`, `0.04252`) |
| `2059` slope | **`5.14`** (fit s.e. `0.00303`, the minimum) | **`1.15`** (at `f=0`, `0.01358`) |

And the ceilings, by the `r7719` arithmetic: a **six**-member family admits `720` permutations ⇒ **`3.20`**
sd-equivalent; **twelve** settings admit `12!` ⇒ **`5.99`**. ⇒ **Read as significances, both `5.14` and
`7.55` exceed their own families' ceilings.**

## ⑤ ⛔ AND YET NO CORRECTION IS OWED — because both sentences name their denominator AND their anchor

- `1779` prints *"seven and a half times **its own spread across those settings**"*.
- `2059` prints *"`2.23` of **its own band spread across the family**"* and *"`5.14` of **its own
  regression error over that family**, **each error taken at the parameter where the two arms' combs
  align**."*

⇒ By **69's own `r7721` ruling** on the both-arms ratios — *"the sentence states a ratio and makes no
probability claim; the ceiling is a fact about what that statistic can carry as evidence, not an error in
the sentence"* — **neither printed figure is an error.** The ceilings in ④ are reported and are **not**
grounds for a correction.

⚠ **I nearly reported one anyway.** I had written that `2059`'s wording *"does not say the error is the
family's minimum"* — and then re-read the sentence, which ends *"each error taken at the parameter where
the two arms' combs align"*, i.e. **exactly where the minimum is**. ⇒ The paper discloses the anchor; my
summary of it did not. ⌗ *Seventh instance of the recurring fault, and caught by reading the sentence
instead of my note about it.*

⇒ **Step 4 of the order produces nothing, because its condition — "only where the printed claim does not
survive" — is not met at any site.**

## ⑥ ⛭ THE ONE REAL DEFECT, FOUND AND FIXED

`1779`'s receipt read *"`+0.01034 ± 0.00137` at **`7.6` sigma** of its own setting spread"*.

⛔ **A setting spread is a ROBUSTNESS measure, not an error.** It measures how far the slope moves when the
analysis choice moves, and carries no sampling distribution. ⇒ Calling it a *sigma* names the right
denominator and **the wrong kind of quantity** — and `7.6` is above the `5.99` ceiling twelve settings
could express if it *were* a significance.

⇒ **Fixed in that receipt**, which is this seat's own, with the reason recorded beside it. **36 PASS, 0
FAIL, rc=0.** ⌗ *The paper's wording at that site was already correct; it is the receipt that overstated.
Third revision running in which a receipt's prose claimed more than its computation supports.*

## ⑦ ⛔ THE SEARCH'S OWN BLIND SPOT, declared

The registered patterns require a **numeral**. ⇒ **Spelled-out multiples are missed.** One such site exists
and I saw it only by reading the file before writing the classifier: **line `2206`**, *"inside the spread
of the three"* — a consistency claim over a **three**-member family, whose ceiling is `3! = 6` ⇒
**`1.38`** sd-equivalent.

⛔ **The registration says the patterns' union IS the list, so `2206` is not added to it.** It is named here
instead, with the sweep declared **incomplete in that one stated way**. ⌗ *A sweep whose blind spot is
named is worth more than one that quietly had none.*

---

# ⛭ ADDENDUM `r7729+cc66.1` — **the declared gap is closed. `l.2206` makes NO probability claim, so no correction is owed and the sweep is COMPLETE.**

⌗ *No new registration: the order says "classify it the same way", so `PREDICTION.md` §3's three criteria are
applied unchanged to one further site. Nothing about the test is redefined.*

## The sentence, verbatim

> *"The loading is separated from a reparametrization of the clock as well, **by a factor of six**; the
> driving is not, sitting **within a sixth of the largest clock reading** and **inside the spread of the
> three**."*

and the sentence before it supplies what "the three" and "a factor of six" are: the plane's discriminant
sits at `0.185` for the driving and `1.096` for the loading — *"a factor of `5.9` apart"*.

## The classification, against the registered criteria

| | |
|---|---|
| criterion 1 — P15's own measurement | ✔ |
| criterion 2 — an empirical spread over a correlated family | ✔ *"the spread of the three"* is three clock readings on the same plane |
| criterion 3 — used as evidence | ✔ as evidence of **NON**-separation |
| ⛔ **but: is a MULTIPLE formed?** | **NO** |

Its three quantities are **a ratio** (`1.096/0.185 = 5.92`, printed as "a factor of six"), **a ratio**
(*"within a sixth of"*), and a **containment** (*"inside the spread"*). ⇒ **Not one of them is a quantity
divided by a spread and read as a significance.** There is no `sigma`, no significance, no percentile.

## ⇒ THE VERDICT: the `1.38` sd-equivalent ceiling does not bear on it

A family of three admits `3! = 6` permutations, floor `p = 0.167`, so **`1.38` sd-equivalent**. ⛭ **That
ceiling constrains what a three-member family can carry as a SIGNIFICANCE — and this sentence asserts
none.** ⇒ By the `r7721` ruling, *"the sentence states a ratio and makes no probability claim"*, so **no
correction is owed and none is drafted.**

⛭ **And the direction is worth recording, because it is the opposite of a defect.** A containment claim
against a three-member spread is the **conservative** use of it: *"inside the spread"* cannot overstate,
because it asserts the weaker thing. ⚠ *Had the sentence said "**outside** the spread of the three" as
evidence that the driving **is** separated, that WOULD have been the overstatement the ceiling catches —
`1.38` sd-equivalent is almost no evidence at all.* ⇒ The sentence uses a tiny family in the only way a
tiny family can honestly be used.

## ⇒ THE SWEEP IS NOW COMPLETE

Every site the registered patterns returned is classified, and the one site they structurally could not
reach — spelled-out numerals — is classified too. **No printed P15 claim of this form fails.** The sweep's
only defect was in a receipt, and it is fixed.
