# `r7279+70.2` — results: the figure-pin detector is enriched and is placed as a ratchet. The finding behind it is the base rate: about four in five figures printed beside a citation are not held by the receipt cited

*Pre-registered at `PREDICTION.md` (`0a4ec067`).*

- The detector is `detector.py`.
- The blinded sample is `sample.tsv`, with its flag key `key.tsv` withheld from the tree until the reads returned
  (`c7d1a345`).
- The reads are `reads.tsv`.
- Site lists: `sites_v1.tsv` is the registered detector; `sites.tsv` is after the one repair below.
- The gate is `corpus/check_figures_pinned.py`, with `corpus/figure_pin_baseline.tsv`.

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| F-a | figure-bearing sites | 350 (200–600) | **343** (113 PROSE, 230 APPENDIX) |
| F-b | share FLAGGED | 70% (50–90) | **93.3%** (320): **refuted high** |
| F-c | **P**, precision | 75% (55–90) | **85%** (17 OVER, 3 WITHIN, 5 NOT-A-CLAIM) |
| F-d | **U**, OVER among unflagged | 20% (5–45) | **4.5%** (1 OVER, 21 WITHIN, 1 NOT-A-CLAIM): low, in band |
| F-e | NOT-A-CLAIM, pooled | 15% (5–35) | **12.5%** (6 of 48) |

**On the sample.** Only 23 sites were unflagged, against the 25 registered, so all 23 were read. They were
shuffled with the 25 flagged sites drawn at seed 7279, and the flag was stripped. Three read-only readers worked to
the rubric in the prediction. Before they started, the key and the site list were moved out of the tree. I re-read
four sites against the receipts, `F05`, `F15`, `F34` and `F45`, and all four reads held.

**The seeds.** Each holds in its registered direction:

- `N05` (`7.78` against `|l2−7.8|<0.3`) flags.
- `N13` (`207.8` against `< 348`) flags.
- `N07` (`0.315162424` to `1e-6`) passes.
- The synthetic tight pin passes.
- So do eleven unit seeds on built source.
- `N02` and `N18`, the two misses named in advance, both flag, as predicted.

## ✔ 66's negative does not fire

- **P − U = 80.5 percentage points,** against the 25 registered.
- **Fisher one-sided p = 7×10⁻⁸** on `[[17,3],[1,21]]`.

The wide census failed exactly this comparison, at 40% against 55%. This narrow detector's flags carry
information. With **P ≥ 70%, the rule fixed in advance places it as a ratchet.**

## ⛭ But the base rate is the finding, and it is the same finding as `r7267`'s, made sharper

The detector flags 93% of figure-bearing sites, and 85% of what it flags over-reaches. **So about 80% of the
figures the corpus prints beside a citation are not held by the receipt it cites:** 0.93 × 0.85 + 0.07 × 0.045 ≈
0.79.

- Most of these figures appear in the receipt only in a docstring, a comment or a `print`.
- The rest are gated one-sidedly or at a tolerance wider than the printed digits.

Against the trivial rule "flag every figure-bearing site", the detector's gain is real but small: 85% against about
79%. **Its value is not that it finds the over-reaching sites. Nearly all of them over-reach. Its value is that it
finds the 24 sites that DON'T, and it lets no new site join the 319.** The gate is built for that forward job.

## The false positives, by class

There are 3 among the 20 flagged claim sites.

| site | class | named in advance? |
|---|---|---|
| `F15` `151.2` | **SYMBOLIC pin**: an exact sympy identity, `−2π∛2/3` | yes (`N02`) |
| `F31` `2.60 2.95 2.7618` | **STRUCTURAL pin**: a band's emptiness `T[1]==[]` and a bound against a named neighbour | no, the `N18` derived-pin class widened |
| `F05` `0.31` | **FLOAT EDGE**: `abs(x+0.305)<0.005` is exactly at the allowance, and `|0.305−0.31|` computes to `0.005000000000000004` | no: a defect, **repaired** |

The one unflagged OVER is `F34`. There, `1.489` sits only as a **DIVISOR inside another quantity's pin**
(`abs(I/1.4890 − (−0.032312)) < 1e-6`) and is never computed. Under the registered rule, a constant anywhere inside
the `abs()` counts as held.

**On the `F05` repair, made after the read and reported as such.** A one-ulp slack (`× (1 + 1e-9)`) on both
comparisons. It moves exactly one site, `F05`'s, from flagged to unflagged, which is 320 → 319. It is seeded in both
the detector and the gate. The precision figures above are for the registered detector. Re-scored after the repair,
P is 17/19 = 89% and U is 1/23 = 4.3%.

**Not patched:**

- **The symbolic, derived and structural classes.** Pairing a printed decimal with a sympy expression or a derived
  quantity is a digit-coincidence question. The honest instrument for it is moving the figure, as `r7164` found.
- **The divisor class.** Narrowing `abs()` to its top-level subtraction would need a reading of which side is the
  computed quantity.

All four classes are stated in the gate's docstring.

## What went in

- **`corpus/check_figures_pinned.py`, in the `fast` job.** It is self-contained: it reads source only and runs in
  about 2 s. It carries the eleven unit seeds plus the percent-fraction seed.
  - A NEW `(population, paper, receipt, figure)` count above the baseline fails.
  - A STALE baselined count fails, so the baseline can only shrink.
  - Words in a sentence can change freely. Only a figure appearing or disappearing beside a receipt moves a key.
- **`corpus/figure_pin_baseline.tsv`:** 1,383 unpinned figures under 1,291 keys, at 319 sites. The gate and the
  detector agree key for key.
- **No paper sentence or receipt is edited.** The list is routed per paper in `FOR_66_FROM_70.md`.

## Where the 319 sit

- **P15 / `CR_cosmology` holds 257 of the 319:** 170 INDEX rows and 87 prose sites.
- P16 and `cosmogenesis_paper` hold 16.
- P14 holds 8.
- P3/P03 and `SdS-slicing-curve_v2` hold 8.
- `CR_framework` holds 4.
- 26 more are spread over the remaining papers and the unlabelled rows.

The over-reach is concentrated where the corpus prints the most numbers. It is a property of how the CMB sector
writes its rows: the figure from the run goes into the claim, and the receipt asserts a bound.
