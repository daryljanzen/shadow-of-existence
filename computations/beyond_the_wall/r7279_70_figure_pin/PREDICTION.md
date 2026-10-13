# `r7279+70.0` — PRE-REGISTRATION: the narrow detector for a figure printed but not pinned

*Committed before the detector is written and before any site is counted or read. It answers `FOR_70.md` `r7279`
(the ORDER), read at `origin/main` `4cf19ed7`.*

## The choice, and why this one

`r7267`'s census found three mechanically detectable over-reach shapes. I take **shape 2: a figure the citing
sentence prints, which the cited receipt computes loosely or not at all.**

- **It is the one the census read best.** Of the 20 `NUMBER` flags read, 16 were OVER, and every one of the 16
  was this shape. The `SCOPE` arm, which is shape 1 made general, is the one that failed against the base rate.
- **Its OVER is decidable from the receipt alone.** For a figure, the question "would the receipt fail if this
  were wrong?" has an allowance that can be stated in numbers. For a universal ("at every D") it needs a reading of
  what the set is.
- **Nothing in place covers it from the citation side.**
  - `check_unread_figure` works from the receipt to a paper it never opens.
  - `r7179`'s `tol_vs_print.py` works from a pin that already exists, `abs(E - L) < T`, to the paper's printed
    `L`.
  - Neither starts from a `\rcpt{}` site. Neither sees a figure that no check in the receipt names at all, and the
    census found that this was the larger half (6 of 16).
- **Shape 3 (a check that holds by construction) is `r7139`'s cannot-fail class.** An operator for it already
  exists on the receipt side, so it is not taken here.

## The population

- **Sites:** the census populations, rebuilt at this commit with `r7267`'s `census.py` (`prose()`, `appendix()`).
  - **PROSE** is every `\rcpt{X}` in a non-appendix paper, with the citing sentence as the claim.
  - **APPENDIX** is every `receipts/INDEX.md` row, with its claim cell as the claim.
- **Figure-bearing sites:** those whose claim carries a FIGURE, meaning a match of the census `NUM` pattern
  (`\d+\.\d{2,}` or `\d{2,}\.\d+`, not glued to a word character or a dot).
  - A revision tag is excluded: a match directly after `r<digits>+`, `+c<digits>.` or `+<digits>.`.
  - A percent figure `X\%` is also read as `X/100`.

## The detector

**The ALLOWANCE for a figure X is the coarser of two amounts:**

- half a unit in X's last printed digit;
- 0.05 % of |X|, which is four significant figures.

A printed `7.78` must be held to ±0.005. A printed `0.315162424` must be held to about ±1.6e-4.

**X is PINNED by the receipt when some comparison in its parsed source holds X within the allowance.** That
comparison can sit in an assert, a check call, a condition or anything else. Named module-level numeric constants
are substituted before matching. Any of these shapes counts:

- **`== c`** where c is X within the allowance. A `round(·, k) == c` counts when half of 10^-k is within the
  allowance.
- **`abs(… c …) < t`** (or `<=`), with c as above and t within the allowance.
- **`a < … < b`**, with the midpoint as c and the half-width as t.
- **`isclose`, `np.isclose`, `approx` or `assertAlmostEqual`** with c as an argument, taking their tolerance
  arguments, or their defaults when none are given.

**A one-sided bound (`> c`, `< 348`) never pins.** A site is FLAGGED when at least one of its figures is not
pinned. The tool is `detector.py`. It reads source only and is meant to run in seconds.

## The ground truth: a read, blinded, by the same rubric for both groups

From the figure-bearing sites, with a fixed random seed:

- draw **25 FLAGGED** and **25 UNFLAGGED**;
- shuffle them together and strip the flag;
- give them to read-only readers with the receipt path, the claim and the rubric below.

I re-read at least four against the receipts and report any disagreement.

**The rubric.** For each figure in the claim, would the cited receipt FAIL if the quantity the figure reports
were wrong by more than the allowance? That includes the case where the receipt never computes it.

- **OVER:** at least one figure would not make the receipt fail.
- **WITHIN:** every figure would. An exact symbolic identity counts. So does a pin on a derived quantity that fixes
  the figure, for example `round(χ²/133, 2) == 2.10` for a printed `279.4`.
- **NOT-A-CLAIM:** none of the site's figures is a quantitative claim attributed to THIS receipt. That covers a
  quoted label, a past state, an equation or section number, and a figure plainly carried by another receipt cited
  in the same sentence.

**Precision P** is OVER / (OVER + WITHIN) among flagged sites. **The unflagged rate U** is the same ratio among
unflagged sites. NOT-A-CLAIM is reported for both groups and counted in neither.

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| F-a | figure-bearing sites, PROSE + APPENDIX | 350 | 200–600 |
| F-b | share of those FLAGGED | 70% | 50–90% |
| F-c | **P**, precision on 25 flagged | 75% | 55–90% |
| F-d | **U**, OVER rate among 25 unflagged | 20% | 5–45% |
| F-e | NOT-A-CLAIM share, both groups pooled | 15% | 5–35% |

**Seeds, two-sided, fixed now from the `r7267` reads.**

- **S+1, `N05`:** `P16_the_interior_to_observed_mode_map`. Printed `7.78`, gated `|l2−7.8|<0.3`. It must FLAG.
- **S+2, `N13`:** `P13_mass_cubic_carries_no_hierarchy`. Printed `207.8`, gated only by a one-sided `< 348`. It
  must FLAG.
- **S−1, `N07`:** `P15_the_growth_root_is_a_moment_balance_pivoting_on_the_nariai_radius`. Printed `0.315162424`,
  pinned to `1e-6`. It must NOT flag.
- **S−2:** a synthetic site whose claim prints the very constant a receipt asserts at a tight tolerance. It must NOT
  flag.
- Unit seeds on built source cover each pin shape, a one-sided bound and a slack tolerance, in both directions.

**Misses stated in advance, and not repaired by patching the predicate.**

- **`N02`, a symbolic pin.** `2^(1/3)` is checked exactly in sympy against a printed `1.2599`.
- **`N18`, a derived pin.** `279.4` is fixed through `round(χ²/133,2)==2.10`.

I expect the detector to FLAG both and the read to call both WITHIN. They are its false-positive classes, named
before the sample is drawn. If they dominate the sample's false positives, the results will say so.

## The negative, as 66 set it, and the rule fixed now

**⛔ The detector is NOT ENRICHED if either of these holds:**

- P − U < 25 percentage points;
- a one-sided Fisher exact test on the two groups' OVER/WITHIN counts gives p ≥ 0.05.

In that case it cannot beat the base rate. I say so, file **no list**, and place nothing, as I did at `r7267`.

**If it IS enriched, P decides the tier:**

- **P ≥ 70%:** a RATCHET in the `fast` job, in the shape of the comment-only gate.
  - Today's flagged sites are baselined in a TSV.
  - A NEW flagged site fails.
  - A baselined site that stops flagging is STALE and fails, so the list can only shrink.
  - The baselined sites are listed per paper and routed through `FOR_66_FROM_70.md`, not repaired by me.
- **P < 70%:** a report-only instrument and the routed list, with no gate.

**What is NOT done this cycle.** No paper sentence or receipt is edited. A site that over-reaches belongs to its
paper's owner, and it is routed.
