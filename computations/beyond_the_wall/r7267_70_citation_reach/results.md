# `r7267+70.1` — results: the citation-reach census. 66's negative fires: over-reach is the base rate, not a site defect

*Pre-registered at `PREDICTION.md` (`2b5b27a6`). The census is `census.py`, which writes `census.tsv`. The fixed-seed
sample is `sample.tsv` and the 70 reads are in `reads.tsv`.*

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| — | PROSE population | 580 | **768**: my pre-registered count was taken with `grep -c`, which counts LINES; several lines carry two citations |
| R-a | PROSE sites resolving to a receipt | 95% | **100%** (768 of 768) |
| R-b | PROSE flagged by SCOPE | 15% (5–35) | **9.8%** (75) |
| R-c | APPENDIX flagged by SCOPE | 20% (5–40) | **11.6%** (120 of 1,031 rows) |
| R-d | flagged by NUMBER, both populations | 25% (10–50) | **7.3%** (131): refuted low |
| R-e | SCOPE precision, 30 read | 40% (15–70) | **40%** (12 OVER, 6 WITHIN, 12 NOT-A-CLAIM) |
| R-f | NUMBER precision, 20 read | 20% (5–50) | **80% strict / 30% lenient**: see below |
| R-g | over-reach among 20 UNFLAGGED prose sites | **1** (0–4) | **11**: refuted, high and far outside the band |
| R-h | over-reaching share of PROSE citations | 8% (3–25) | **≈ 55%**, interval ≈ 35–72%: refuted high |

**The seeds.**

- **S+1 (`I55`, the sentence before 60's repair) flags on SCOPE**: `at every … term`. It flagged only after the
  reach was REVISED to what the receipt's checks can reach (parsed string literals and identifiers, with comments
  and docstrings excluded) and read at the seed's own commit. The first form searched the whole file and missed,
  because the words were in the receipt's prose and not its checks. **The revision was made after the seed failed,
  and is reported as such.**
- **S+2 (`P15R22`) does NOT flag on NUMBER, and cannot.** Every figure in the old row IS in the receipt; the defect
  is the reverse, the receipt's figure presented as the PAPER's. That is a row-against-paper comparison, not a
  claim-against-receipt one. This arm cannot see it, and I report it as a structural miss.
- **Both negative controls are clean.**

**On the NUMBER reading.** Ten of its 16 OVER rows compute and print the right figure but check it only against a
loose bound: `|Δ|<2` for a printed `+1.58`, `14<|wA|<17` for `15.4648`. If "the receipt would fail if the figure
were wrong" means the PRINTED figure, those ten are OVER. If it means the claim's direction, they are WITHIN and the
precision is 30%. Both are reported. The other six never compute the figure, or compute it in another
configuration.

## ⛔ The negative 66 set fires, and it fires for the reason 66 named

**The detector's flags are not ENRICHED.** Precision on SCOPE flags is 40%, and the over-reach rate among sites it
did NOT flag is 55% (11 of 20). An instrument whose positives are no more often right than its negatives is
measuring the base rate, not a defect. So the census cannot be a gate, and no per-site list is filed.

**The base rate is the finding.** About half of the prose citations attach to sentences claiming more than the
receipt can fail on. The 20-site sample gives 34–74% at 95%. The convention `X would FAIL if the claim were false`
(`r2376+c54.166`) **was never the practice**: the corpus cites a receipt for the computation that SUPPORTS a
sentence, not for one that would REFUTE it.

**What the over-reach looks like, read rather than counted.** It has four recurring shapes, each seen several
times in 70 reads:

1. **A universal over a sample.** "At every D" for `D ∈ 4..8` (S16, confirmed). "The only antilinear symmetry" with
   four candidates tried (S20, confirmed). "Every mode" with six `k` (U15).
2. **A figure printed, not pinned.** The printed value is right, and the gate is a loose bound or a threshold (N01,
   N04, N05, N11–N15, N20).
3. **A check that holds by construction.** `WICK = 3` then `WICK == 3` (U16, confirmed). A count asserted as the
   `len()` of a hard-coded list (U03). A first integral built into the ODE it is checked along (U02).
4. **An interpretation cited as a computation.** "Not a coincidence", "not a tuning", "one object described twice"
   (U07, U12), where the receipt checks an algebraic equality and the sentence adds the reading.

**Shapes 1 to 3 are mechanically detectable, each on its own; shape 4 is not.** Shape 3 is the cannot-fail
operator's class arriving through citations. Shape 2 is a figure-pin with a tolerance looser than its printed
precision. Shape 1 needs the claim's quantifier set against the receipt's loop range, which is the SCOPE arm made
specific. These are three narrow detectors, each with a clean seed above. None is the one wide census this order
asked for, and the measurement says the wide one does not discriminate.

## What is NOT done

- No site is repaired or routed. 66's rule for this negative was to file no thousand repairs, and the census
  supports no site list: a flagged site is no likelier than an unflagged one to over-reach.
- The 70 reads were made by three read-only agents, against the rubric written into their prompts. I re-read four of
  them against the receipts (S16, S20, U15, U16), and all four held. The reads are a sample with its interval, not a
  census.
