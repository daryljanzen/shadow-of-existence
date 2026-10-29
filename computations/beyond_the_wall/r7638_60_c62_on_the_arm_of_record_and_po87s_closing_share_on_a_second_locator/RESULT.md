# r7638 (60) — RESULT: `PO-87`'s closing share survives a second locator on TT, is the sky source's in EE, and is not a quantity at all in TE

**Answering `r7637`.** Two steps were ordered: re-point `C62` on the arm of record and report old → new
for every figure; and check `PO-87`'s closing figure on a locator independent of `70`'s. Both are done.
`share.py` runs **17 checks, 0 failures**; the re-pointed `C62` runs **21 checks, 0 failures**.

---

## 1. THE REGISTERED LOCATOR CROSSED ITS CEILING — AND THE NEGATIVE IS SCORED AS ARRIVING

The locator registered at `r7638` was a Gaussian with a linear baseline anchored at the fixed window
centre. On TT it puts the share at **`1.023` to `1.030`** across all eighteen readings — six windows by
three sky sources — so it **crosses the registered `1.00`** everywhere. ⇒ **By the registration, the
figure is the locator's and not the spectra's, and this line's expectation that it would land inside
the band is a MISS, reported as one.**

## 2. AND THE NEGATIVE IS ADJUDICATED TO THE LOCATOR, MEASURED RATHER THAN ASSERTED

| locator | arm − control at ℓ₄ (TT) |
|---|---|
| raw grid extremum | **+1.000** |
| three-point parabola (`70`'s) | **+0.518** |
| parabola, `W` = 10 / 20 / 40 / 80 | **+0.524 / +0.541 / +0.607 / +0.914** |
| centroid, `W` = 40 / 80 | **+0.622 / +0.902** |
| **GAUSSIAN**, `W` = 25 / 40 / 60 / 120 | **−0.354 / −0.329 / −0.338 / −0.438** |

**Eight non-Gaussian readings across four families all give the displacement POSITIVE, around `70`'s
`+0.518`. The Gaussian alone reverses its sign**, and sits **six multipoles up-`$\ell$`** of all of
them on the same curve.

**The cause is measured, not guessed.** The Gaussian centre climbs **monotonically** with window on
**both** arms (`1135.530 → 1140.106` on the arm, `1135.884 → 1140.544` on the control) — the signature
of a symmetric model fitted to an asymmetric peak. ⌗ And the asymmetry is measured: the feature is
**`172`** multipoles wide at half maximum with half-widths of **`94` up and `78` down**, differing by
**nine per cent** of its width.

⌗ **The locator's own control had said in advance what it could not test.** It plants the locator's own
model — a symmetric bump on a straight line — so it validates the **fitter** and says nothing about
whether that model fits an acoustic peak. That limitation was written into the arm before the spectra
were read, and it is exactly where the registered locator failed.

## 3. THE SECOND LOCATOR THAT PASSES THE ADJUDICATION, AND IT IS STILL NOT `70`'s

**The centroid of band power above the window's own lower shoulder** — a weighted mean with **no shape
assumption at all**, neither a parabola nor a re-parameterisation of one. It **reproduces `70`'s
positions in all three spectra to under a multipole** (worst disagreement `0.794` at `W = 40`) and
agrees with `70` on the **sign** of the displacement in all three, where the Gaussian did not.

## 4. THE SHARE ON THAT LOCATOR

- **TT — the closing figure survives.** `0.843` to `0.927` across the registered windows and all three
  sky sources, around `70`'s `0.911`. ⇒ **`PO-87`'s closing outcome is reached on an instrument that is
  not `70`'s.**
- ⚠ **And it brushes the floor**, reported rather than trimmed: `0.749` against a registered `0.75` at
  the widest registered window. The share falls monotonically with window because the asymmetry pulls
  both positions down-`$\ell$` together, so **the figure is window-dependent at the third digit**.
- ⛔ **EE — one spectrum, one locator, two verdicts.** `0.780` to `0.785` against Planck, inside the
  band; `−1.179` to `−0.413` against ACT, outside it and negative. The two sources disagree by `10.6`
  multipoles against an arm-minus-sky residual of `1.2` to `1.9`. **This is the ambiguity the
  registration enumerated, and the two are reported apart and never averaged.**
- ⛔ **TE — the share is not a usable quantity.** The arm lands **`0.069` of a multipole** from the
  Planck sky value, so the ratio's **denominator all but vanishes**: the share runs from **`−51.4` to
  `+5.7`** across six windows. Against ACT it is `0.024` to `0.368`, below the floor. ⇒ **The
  registered negative arrives in TE, and its cause is the denominator, not a disagreement between the
  spectra.**
- ⛔ **And at `W = 100` and `120` the TT share breaks by the same mechanism** — none of those six
  readings is inside the band, and the smallest arm-minus-sky residual there is `0.107` of a multipole.
  ⇒ **So the reading that the wide windows are the better instrument, taken on a planted symmetric
  peak, is REFUTED on the real curve.** It was the fitter that improved with width, not the model. The
  verdict rests on the registered windows, and that is now measured rather than preferred.

⌗ **One trap named because this receipt's first pass fell into it:** **TE's fourth feature is a
MINIMUM**, not a maximum — TE changes sign under it — so a locator seeking a maximum does not find it
at all and wanders with the window. Every TE reading here is taken on the minimum.

---

## 5. `C62` RE-POINTED ON THE ARM OF RECORD — OLD → NEW, EVERY FIGURE

The four ISW spectra it reads are now their `_leafrec1` counterparts from `70`'s `r7635` bank. **All
`21` checks hold.** Exactly five printed figures move, and all five are in the ISW arm:

| figure | superseded arm | arm of record |
|---|---|---|
| ISW imprint, 100–300 (leaf / stacking) | `56.7%` / `22.6%` | **`51.9%` / `23.7%`** |
| ISW imprint, 300–700 | `3.1%` / `1.3%` | **`4.1%` / `2.1%`** |
| ISW imprint, 700–1300 | `1.4%` / `0.9%` | **`1.9%` / `1.1%`** |
| ISW significance, 100–1296 (133 bins) | `12.195` χ²/bin, `3.49` σ/bin | **`12.315`, `3.51`** |
| ISW significance, 700–1296 (66 bins) | `0.590` χ²/bin, `0.77` σ/bin | **`0.739`, `0.86`** |

**Nothing else moves**, and the reason is structural: the diffusion-scale figures, the shape residual,
the tilt costs and the injection recoveries are computed from the instrument rather than read from the
banked spectra, so the bank feeds only this receipt's ISW arm.

**⛭ THE ARM REGISTERED AT `r7636` IS SCORED, AND THE NEGATIVE DID NOT ARRIVE.** It was that *the early
ISW's reach into the multipoles the row asks about crosses the bound this receipt stated for it, or the
diffusion signature stops being a wash*. On the arm of record the high-`$\ell$` ISW is **`0.86`
σ/bin — still under one** — and the TT shape residual is still **under `0.6` σ/bin after the refit**.
⇒ **`C62`'s verdict holds on the arm of record, with narrower margins**, and the narrowing is reported:
the high-`$\ell$` ISW rose `0.77 → 0.86`, and the low-`$\ell$` multiplier fell `2.51 → 2.19` against an
assertion that requires it to exceed `2`.

⌗ **And one figure in `C62` was prose rather than computation.** The sentence *"the leaf assignment
makes the term `$1.52\times$` larger"* had no computation behind it in the file. **It is replaced by
the computed multiplier, which the receipt now prints**, so it cannot go stale again.

## 6. THE SECOND RECEIPT OF THIS SEAT'S SHARE, RUN RATHER THAN TAKEN FROM THE DRY RUN

`r7636` reported this seat's share as **one** receipt. **That was under-counted and the correction is
against this line:** a provenance cell naming only the order it answers — *Ordered: `r7221`* — names
this seat without naming it, and `r7221` is a section of `FOR_60.md`. `70`'s dry run had it right.
⇒ **The share is two receipts.**

The second, `P15_the_spacing_drift_is_made_in_the_projection…`, was run on both trees rather than taken
from the dry run: **`14` checks OK and `0` FAIL on both, with identical check outcomes**, and three
printed figures move — the sanity-of-spacing drift `D` goes `+0.56 → +0.53` (rms `3.18 → 3.12`), the
whole-monopole-source drift `+0.03 → +0.00` (rms `3.02 → 2.96`), and the re-projected own-source peaks
shift in the third digit with `D` `+2.57 → +2.55`. ⌗ **So `70`'s dry run was right that no check moves,
and incomplete in that figures do** — which is what `r7637` says the dry run is for.

⚠ **It cannot be run to completion in this container**, and identically so on both trees: it reads a
pinned commit through `git show`, which a shallow clone cannot serve, and it dies at the same line on
both sides. Everything above is measured up to that point.

## 7. ONE THING `r7637` NAMES THAT IS NOT IN THE TREE

`r7637` says *`dry/C62*.diff.txt` is a map of what moves*. **There is no such file.** The dry directory
holds `51` diffs and none is `C62`'s, which is consistent with the dry table listing only section-B
`P15` receipts while `C62` is a `C`-series receipt outside it. **Said rather than worked around**, and
the re-point was measured without it.
