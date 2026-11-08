# `r7709+cc66` ITEM 2 — THE SENTENCE FOR THE STEP PARAGRAPH, EACH FIGURE WITH ITS LICENCE

The site is `corpus/CR_cosmology.tex` l.1397–1408, the paragraph beginning *"Located rather than merely
noticed, the step sits at the second acoustic peak."* **One sentence is added and nothing in print moves.**

## WHERE IT GOES

Immediately after the acceptance-law sentence (*"…while the law's own transition across the same windows is
resolved where the measurement's is not"*) and before *"So the excess in the first acoustic cycle runs
between a third and two thirds of its size in every cycle above."*

## THE DRAFT

> \emph{And the located transition is a property of the contrast and not of the source}: swept in the same
> windows, the arm-to-control ratio's transition is the one the locator finds and follows under
> translation, while the same reading of the two $\eta$-integrated sources returns a ratio near zero
> throughout, in which a transition of the measured size would have stood at four times its own scatter and
> at eleven at the broadest smoothing. \emph{The step's size, by contrast, is in both arms}---it is the
> location and the sharpness that only the contrast
> resolves\rcpt{P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_at_the_visibility}\rcpt{P15_the_window_free_reading_cannot_resolve_the_first_cycle_the_flatness_was_a_trend_and_nine_tenths_of_the_step_is_common_to_both_arms}.

## LICENCES, FIGURE BY FIGURE

| figure or clause | licence |
|---|---|
| "the arm-to-control ratio's transition is the one the locator finds and follows under translation" | ✔ **PINNED** (`r7707`, host receipt): half-rise `1.783`, and the translation control — `+0.15` and `+0.30` in `q` move it by the same amount to within `0.004`, while the source ratio's does not move at all. |
| "returns a ratio near zero throughout" | ✔ **PINNED**: the source ratio runs `−0.0068` to `−0.0043`, its own low-to-high change `+0.002`, **under one standard deviation of its own scatter at every smoothing**. |
| "would have stood at four times its own scatter and at eleven at the broadest smoothing" | ✔ **PINNED** as the exclusion: a step of the spectra's size against the source ratio's own scatter is `3.8`, `6.6`, `11.8` sd at the three smoothings. ⌗ *Printed as "four … and eleven" — the two ends, rounded down and up from `3.8` and `11.8`, so neither is overstated.* |
| "The step's size, by contrast, is in both arms" | ✔ **PINNED** (`…nine_tenths…`, run at `r7709`): both arms step upward at band 1 against their own bands 2–7 trend on all four bases and both contrasts, sixteen figures of sixteen, the arm's shallower by `8.2`–`11.5` per cent. |
| "it is the location and the sharpness that only the contrast resolves" | ✔ **LICENSED, and by the paper's own figures as much as mine**: each arm's own step stands at `2.5`–`4.5` times its own upper-band spread and the ratio's at `7.2`–`8.5`, which `l.1610` already prints as "some seven times … where each arm's own step stands at four". |
| ⛔ **not** said: that the projection makes the sharpness | **WITHHELD.** `r7707` registered that this cannot be separated here: whether the projection creates the two per cent relative difference or merely fails to cancel something the source contrast hides under its own scatter is not decided by any reading available. The draft says *where* the transition is resolvable and not *what makes it*. |
| ⛔ **not** said: anything about attribution | **WITHHELD**, unchanged: no build removes a step the arms share. |

## WHAT THE LANDING MINTS — *named in advance, as at `r7705` and `r7707`*

1. **Two new worded figures** enter `CR_cosmology.tex`: *"four times its own scatter"* and *"at eleven at
   the broadest smoothing"*. Both are pinned by a COMPARISON in the `r7707` block of
   `P15_a_source_with_no_physics…` (`3.8` / `6.6` / `11.8` sd against the printed bound), not by a regex
   over digits — so `check_figures_pinned` has what it asks. **The `corpus/figure_pin_baseline.tsv` rows go
   in the pass that lands the prose.**
2. **No new quote-pin key**, and **no absent-paper pin**: nothing in the draft is forward-looking, and the
   sentence is prose rather than a quoted source line. ⌗ *To be confirmed by running the two gates in the
   landing pass rather than reasoned, which is `r7705`'s lesson.*
3. **No prose-reading receipt is pinned to this paragraph's wording** — the same enumeration as at `r7707`:
   every assertion either prose-reading receipt makes against this file sits at `l.2603`, `l.2619`,
   `sec:largescale`'s quadruple or the likelihood total, all outside l.1397–1408.

## ⚠ ONE THING FOR 69 TO DECIDE, AND IT IS NOT MINE

The paragraph at l.1411 **already defines** the band-average statistic (*"A candidate's step is its lowest
band's departure from the trend its own upper bands set, read on four bases"*) four lines below where this
sentence would sit. ⇒ **A reader meeting "the located transition" and "a candidate's step" four lines apart
could take them for one statistic — which is precisely the confusion my `r7707` ⓶ fell into.** The draft
above says "located transition" and "the step's size" to keep them apart, but if you want the distinction
named outright, the place is this paragraph and not mine to choose.
