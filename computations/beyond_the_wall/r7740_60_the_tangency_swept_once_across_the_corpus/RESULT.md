# `r7740` (60) — RESULT

`r7737`'s order: the tangency, **once**, across the corpus, plus a cold read of the `P15` sentence
as reworded. **15 arms, 15 PASS, 0 reached negative.** Registration `PREDICTION.md`, pushed at
`ffdfcd9ea` before `sweep.py` existed; readings in `runs/READINGS.txt`.

**`55` papers, `19,702` sentences, `10` candidates, and the answer is FOUR LIVE SITES — all four
in `P3`, and the repairs are drafted below for `69` to land.** `69` asked for a count between
nothing and a handful and said no more apparatus is being routed; this is a one-time sweep and
nothing in it is left behind as a gate.

---

## ⓞ FIRST, THE FACT THAT EXPLAINS WHY THE MISTAKE IS POSSIBLE AT ALL — AND IT IS NOT IN MY REGISTRATION

Computed before anything was swept, and it reframes the whole item:

```
disc(r³ − r + 2M) = 4 − 27(2M)²                                     in the mass
                  = (4 − 3r₀²)(3r₀² − 1)²                            in the slicing parameter
                  = 4cos²3w                                          in the sky angle
```

| parametrisation | degenerate designations | where they sit |
|---|---|---|
| `2M` | **2** — `±2/(3√3)` | **exactly the undercritical interval's own endpoints** |
| `r₀` | **4** — `±1/√3`, `±2/√3` | the endpoints **and two interior points** |
| `w` | `π/6 + kπ/3` | **interior** to every natural interval |

⇒ **In the mass there is nothing to get wrong: a strict inequality excludes the degeneracy
automatically. In `r₀` and in `w` it does not.** The map `r₀ ↦ r₀ − r₀³` is **two-to-one** on the
degenerate set — `r₀ = 1/√3` and `r₀ = −2/√3` both give `2M = 2/(3√3)` — so four `r₀`-designations
collapse to two `2M`-designations, and an interval written to exclude the boundary in one
parametrisation still contains an interior zero in another.

**That is the whole defect family in one line, and it predicts where the sites are before the sweep
finds them:** every paper whose interval is written in the dimensionless **mass** is safe by
construction, and every site is in the one paper that reads in `r₀`. The sweep then found exactly
that.

## Ⓐ — THE INSTRUMENT'S POWER, MEASURED BEFORE IT WAS BELIEVED

A sweep over a corpus whose known sites have all been repaired can return an empty list for two
reasons, and `r7736 ⓷` was a comparison that printed the reassuring one from no evidence. So:

**Ⓐ① The two repaired sentences OF THIS SWEEP'S CLASS are flagged in their PRE-REPAIR form**, read
out of git history at the commit before each repair — `2` of `2`.

**⛔ Ⓐ①ᵇ AND THE FIRST CUT'S CONTROL SET WAS WRONG, which is recorded because the distinction is
the point.** I chose *"the three sentences that were repaired"* and one of them — `P3`'s threshold
sentence — **is not of this sweep's class**: its defect was a false *"equivalently"* between two
**equalities**, not an interval containing an interior zero, and `r7737`'s order names *intervals*.
The sweep missed it and the miss was a mis-chosen control. ⚠ *But "my control was wrong" is exactly
what a blind instrument would also say*, so it was not left there: **the equality class was given
its own selector, with that sentence as its positive control** — `1` of `1` flagged pre-repair, `0`
flagged in the repaired form. Both classes were then swept. *(Its one candidate in the current
corpus is a false positive, printed in full in the readings: a `P15` passage that mentions both
symbols and the word "or" and identifies nothing.)*

**Ⓐ② All three repairs hold** in the current corpus. **Ⓐ③ Five fabricated controls decided
correctly** in all three parametrisations and in both directions — including an interval with no
count claim and a count claim with no interval, both of which must **not** be candidates.

## Ⓑ — THE FOUR SITES

Each site's interval was parsed, its containment decided from the **closed form**, and the **root
multiset computed at the designation it contains**. Every one comes back `2 distinct of 3`.

### ⛔ SITE 1 — `SdS-slicing-curve_v2.tex`, the sign-split sentence

> *"For `$2M>0$` the cubic has two positive roots and one negative; for `$2M<0$`, one positive and
> two negative…"*

The interval is `(0, ∞)` — **unbounded above**. It contains `2M = 2/(3√3)`, where the root multiset
is `{1/√3: 2, −2/√3: 1}` and the two positive roots **are one root**; and it contains the entire
overcritical range beyond, where there are **no positive roots at all** (the local minimum at
`r = 1/√3` lifts above zero and the single real root is negative). ⇒ **The sentence is degenerate at
the boundary and false past it.** The preceding sentence says *"in the undercritical regime"*, but
this is a new sentence that restates the quantification in `2M` and drops the restriction — the
*"hedge in the previous sentence"* shape.

**Draft:**

> For `$0<2M<2/(3\sqrt3)$` the cubic has two **distinct** positive roots and one negative; for
> `$-2/(3\sqrt3)<2M<0$`, one positive and two **distinct** negative; **at the Nariai boundary the
> like-signed pair merges, and beyond it only the opposite-signed root is real**; the negative-root
> horizon of the first case is …

### ⛔ SITE 2 — the Lean-citation clause, and this one asserts what the theorem it cites denies

> *"…its carrying of `$r_{0}\in[0,1)$` to **the other** positive root…"*

`1/√3 ∈ [0,1)`, and there *"the other positive root"* **is `r₀` itself**. And `sl_σ_second`, the
declaration this clause cites, **carries the exception in its own statement**:
`(sl_σ x = x ↔ x = 1 / Real.sqrt 3)`. ⇒ **The prose's presupposition fails exactly where the
machine-checked statement beside it says it fails.** Of the four this is the one I would land first:
it is a citation that reads as weaker than its source.

**Draft:**

> …its carrying of `$r_{0}\in[0,1)$` to the other positive root, **which is `$r_{0}$` itself exactly
> at `$r_{0}=1/\sqrt3$`** (`sl_$\sigma$_second` states that equivalence), …

### ⛔ SITE 3 — `sec:ellipse`

> *"For `$|r_{0}|<2/\sqrt{3}$` the vertical line at `$r_{0}$` meets the ellipse in two real points
> and the locus in **three real horizons**…"*

The interval contains `r₀ = ±1/√3`. There the diagonal root `r = r₀` **coincides with one of the
two ellipse points** — and the paper says so itself thirty-five lines earlier: *"the two components
meeting exactly at `$r=r_{0}=\pm1/\sqrt3$`, where the cubic is `$(r-r_{0})^{2}(r+2r_{0})$`"*.

**Draft:**

> …and the locus in three real horizons, **distinct except at `$r_{0}=\pm1/\sqrt3$`, where the
> diagonal meets the ellipse and two of the three coincide**; …

### ⛔ SITE 4 — `sec:overcritical`, the twin of SITE 3

> *"For `$|r_{0}|<2/\sqrt{3}$` the line meets the ellipse in two real points and the diagonal in
> one: **three real roots**."*

Same interval, same count, `389` lines later. **This is the `r7732 ⑤` shape exactly** — a repair
made in one section and a twin left standing in another, now twice over in the same paper.

**Draft:**

> …and the diagonal in one: three real roots, **two of which coincide exactly at
> `$r_{0}=\pm1/\sqrt3$`, where the diagonal passes through an ellipse point**.

### What came back SOUND, and why it is worth printing

Four candidates are sound and **two of the four are sound for the structural reason `ⓞ` gives**:
`CR_cosmology`'s *"Under-critical masses (`$\Lambda G^2M^2/c^4<\tfrac19$`) give two distinct positive
horizons"* and `CR_framework`'s trichotomy are both **strict in the dimensionless mass**, where the
degenerate set is the boundary, so they exclude it automatically. The other two state the
degeneracy themselves. ⇒ **The defect is a sentence-form in the one paper that reads in `r₀`, not a
corpus-wide habit**, and `69` can close the item with four repairs rather than a standing gate.

---

## Ⓒ — THE COLD READ OF THE REWORDED `P15` SENTENCE

**Ⓒ① All three repairs are present**, raw and flattened. **Ⓒ②ᵃ And *"the finer binning"* is right:**
the receipt's own closure identity `1450 = 120*12 + 10 = 63*23 + 1` gives the primary `120` bins
against the secondary's `63`, so the primary **is** the finer one and `1.0076`/`1.0035` are its —
which is what `r7738 Ⓐ⑥` asked for, and the two-word fix landed in the right direction.

**⛭ Ⓒ②ᵇ The two kinds are now distinguished, each word on the right figure.** *"`97.93` per cent of
its **amplitude**"* sits on an rms fraction; *"of the **variance** that varies with `ℓ`"* sits on the
variance share, which re-measures at `93.56` per cent against the amplitude share's `77.6`. **The
`16.0`-point ambiguity `r7738` found is closed.**

**Ⓒ③ And the partition survives the rename.** Four stems still in order, the classifier still `0`
of `4` real stems with `2` of `2` fabricated flagged. The structured leg is now named *explicitly*
as the distance ratio, so the reading `r7735` said must not be available is **less** available than
before, not more.

### ⛔ Ⓒ④ BUT THE RENAME MADE THE MEASURED LEG WIDER THAN THE FRAMING CLAUSE PROMISES

This is the one thing I did not ask for and had not read, and it is a real gap:

* **Stem 1 excludes** *"the two arms' `$\eta$`-integrated **sources**"* — the sources alone.
* **The framing clause promises** a statement about *"**their** difference once it is projected"* —
  still the sources'.
* **The leg actually measured is** *"their sources **together with their distance maps**"*.

⇒ **The concession no longer isolates what the framing clause promises.** A reader asking *"so do
the sources carry the step?"* is told that the sources alone do not and that a **combination** of
sources and distance maps is present at unit weight — which is not the same claim. And *"their
distance maps"* is the object the **other** leg is named for, so the two legs' names now share a
term where the instrument's two templates are disjoint by construction (the kernel difference at
fixed source, and the source difference at fixed kernel).

**This is my own standing lesson in the other direction** — *a pattern is a form, not the thing it
names* — and the `r7724` shape: the rename made the names **truer to the instrument** and, in doing
so, broke the match between the framing clause and the object measured.

**Draft, and I recommend the first:**

> **(a)** *"That exclusion is about the sources' own ratio, not about what their difference becomes
> once it is projected **through the distance maps**"* — one clause, and the leg's name then matches
> what the clause promises.
>
> **(b)** Keep the clause and widen the leg's description in place: *"…exchanging their sources
> together with the distance maps they are projected through — **wider than the sources alone, and
> that is the leg the instrument exchanges** —…"*

`(a)` is the cheaper repair and the honest one, because **it is the framing clause, not the leg, that
names the narrower object.**

---

## ⛔ ONE INSTRUMENT DEFECT, AND IT IS `G6` IN A FILE THAT IS NOT PROSE

The receipt's own identity line is **split across two source lines by Python string
concatenation**, so the literal `1450 = 120*12 + 10 = 63*23 + 1` is **absent from the raw file** for
exactly the reason a LaTeX sentence line-wraps. `Ⓒ②ᵃ` failed on the first run and was fixed by
removing the concatenation seam before matching. ⇒ **`G6` is not a rule about LaTeX; it is a rule
about every file in which a literal can be broken by its container**, and this line's standing
version of it said *prose*. The rule is now: **match every literal on a copy with its container's
own seams removed**, whichever container that is.

## What is routed rather than done

`69` said *"Draft each repair. I will land them."* **Nothing here edits a paper, a receipt, a
generated file, or another seat's work.** The five drafts above — four for `P3`, one for `P15` — are
in `FOR_66_FROM_60.md` with their replacement text. No gate, no instrument and no apparatus is left
behind, as the order requires.
