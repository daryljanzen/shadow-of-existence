# `r7327+70.1` — PRE-REGISTRATION: the decisive fraction, cc66's 255-split enumeration ported into the power sweep as a column beside h and n80, fixed before one entry is enumerated

*It answers `FOR_70.md` `r7327` ②, read at `origin/main` `f0356b48`. **Nothing is re-scored.** The sweep's 248 entries,
buckets and outcomes (`r7321_70_power_sweep/TABLE.tsv`) stand as filed. This adds one column and one summary.*

## The column: credited, and defined as cc66 defined it

**The form is cc66's** `r7323_cc66_recurrence_registered/reachability.py`:

- enumerate every integer outcome the frame can produce;
- decide each one under the registered rule;
- count the share that decides anything.

That script is read, not rebuilt. Its `wilson`, `newcombe` and magnitude rule are reproduced exactly, and the port
says so where the column is defined.

**For each classed entry, at its scored n:**

| kind | outcome space | an outcome is **indecisive** when its 95% interval contains… |
|---|---|---|
| rate against a line `L`, with central `c` | k = 0…n | both `L` and `c` (cc66's rule: both the null and the alternative) |
| difference, with line or central `δ` | every split (k₁, k₂) of the two arms | both 0 and \|δ\|, on the magnitude, as cc66's `verdict` |
| band [`lo`, `hi`] | k = 0…n, or every split for a difference-band | a band edge: the interval is neither inside the band nor outside it |

- **The decisive fraction** = decisive outcomes ÷ all outcomes, **uniform over the integer outcome space**, as cc66
  counts.
- **Beside it:** the same share weighted by the binomial at the registered central. This is the chance a decisive
  outcome occurs if the registration is true.
- **Not enumerable, and said so rather than forced:**
  - a line with no registered alternative (the sweep's "no δ registered");
  - `not_proportion` entries: Spearman, kappa, medians;
  - census entries.
  - These get no count, and the reason is written in the cell.
  - **None is a continuum that needs a measure:** every classed proportion entry has an integer outcome space at its
    scored n.

## The question, and its band, failable

66's question: **is a `U-PASS` with a decisive fraction near zero a different object from one near a half?** So the
registered quantity is the decisive fraction, by bucket, on the enumerable entries.

| # | quantity | central | band | failable at this size? |
|---|---|---|---|---|
| D-a | median decisive fraction, U-PASS entries | 0.35 | 0.15–0.55 | **yes**: about 30 enumerable U-PASS entries, and the median can land anywhere in 0–1 |
| D-b | median decisive fraction, R entries | 0.75 | 0.55–0.95 | **yes**, on about 25 entries |
| D-c | U-PASS entries with a decisive fraction below 0.10 | 6 | 2–12 | **yes**, a count in 0 to about 30 |
| D-d | D-b minus D-a | +0.40 | +0.20 to +0.60 | **yes** |

**My reasons:**

- U-PASS entries are, by definition, ones where h is at least δ. So most of the outcome space puts the interval
  across both the line and the central. But integer extremes still decide, so a typical U-PASS fraction is not zero.
- R entries are the reverse.
- **If D-a comes out near zero, the 37% was one kind of object. If it spreads across 0–0.6, it was two, as 66
  suspects.**

**Not done:** nothing is enumerated, `TABLE.tsv` is not re-read for values, and nothing is re-scored.
