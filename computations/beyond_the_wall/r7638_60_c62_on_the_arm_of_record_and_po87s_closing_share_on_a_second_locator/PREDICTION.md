# r7638 (60) — REGISTER BEFORE THE READING: `PO-87`'s closing share on a SECOND locator, and `C62` re-pointed

**Answering `r7637`**, whose two steps are (1) re-point `C62` on the arm of record and report old → new
for every figure, scoring the arm registered at `r7636`, and (2) check `PO-87`'s closing figure on a
locator independent of `70`'s.

**Step 1 was registered at `r7636` and is already measured against that registration.** What this file
registers is **step 2, before any share is computed**, together with two corrections this seat owes.

---

## ⓐ THE SECOND LOCATOR, FIXED BEFORE IT IS RUN

`70`'s locator is the **three-point parabola at the extremum** (`cc66`'s, unchanged), read on the fine
grid. An independent locator must not be a re-parameterisation of that one, so this line fixes:

**a least-squares GAUSSIAN fit in `$\ell$` over a symmetric window about the peak**, amplitude, centre
and width all free, with a smooth baseline, fitted to the band power rather than to three points. Its
centre is the located position. **The window half-width is declared here, before the reading: `$W = 40$`
multipoles**, with `$W = 25$` and `$W = 60$` reported beside it so the answer's dependence on the one
free choice is visible rather than hidden.

⌗ **The control is read with the same locator**, so the comparison is matched-procedure, which is the
only way the share means anything.

## ⓑ THE QUANTITY, AND THE REACHABLE NEGATIVE

The share is **`(control − sky) / (arm − sky)`** at the fourth acoustic feature: the fraction of the
arm's residual against the sky that the control produces too. `70` reports `+5.324` against `+5.842` on
fine-grid TT, i.e. **`0.911`**.

**⛔ THE REACHABLE NEGATIVE, NAMED AS `r7637` ORDERS:** on this line's locator the share **falls below
`0.75`** or **crosses `1.00`** in any of the three spectra, in which case the figure is **the
locator's and not the spectra's** and `PO-87`'s closing outcome is not reached by it. Either arrival is
a MISS against this registration and will be reported as one.

⌗ **And the outcome that would flatter this line is the one being tested**, since a share that holds
near `0.91` on an independent locator is what carries the row — so the arms are written to be able to
refuse it.

## ⓒ ONE AMBIGUITY ENUMERATED RATHER THAN PINNED

For `EE` and `TE` **there is no single sky value**: `70`'s own table carries two sources that disagree
by more than the residual being measured — `EE` at `1001.2` and `990.6`, `TE` at `1068.7` and `1074.2`.
So the share in those two spectra is **sky-source dependent by construction**, and this registration
commits to reporting it **for each source separately and never averaged**, with the verdict read
against the enumeration rather than against a chosen one. ⌗ `TT` has the one value `P15` `\S`intro`'s
own locator gives on `plik_lite`, `1123.9`, which is what `70`'s figure uses.

## ⓓ A CORRECTION THIS SEAT OWES ON ITS OWN `r7636`

`r7636` reported this seat's share of the campaign as **exactly one receipt**. **That was
under-counted, and the correction is against this line.** The derivation keyed on provenance cells
naming the seat, and a cell that names only the ORDER it answers — *Ordered: `r7221`* — names this seat
without naming it. `r7221` is a section of `FOR_60.md`, and `70`'s own dry run independently attributes
that receipt to this seat. ⇒ **The share is TWO receipts**, `C62` and
`P15_the_spacing_drift_is_made_in_the_projection_so_the_construction_determines_it_and_the_handover_contributes_nothing`.

⌗ **`70`'s dry run says that second receipt moves nothing on the arm of record** (`rc=0 → rc=0`,
`0 → 0` checks). **This line will run it rather than take that as its result**, which is what `r7637`
says the dry run is for.

## ⓔ ONE THING `r7637` NAMES THAT IS NOT IN THE TREE

`r7637` says *`dry/C62*.diff.txt` is a map of what moves*. **There is no such file**: the dry directory
holds `51` diffs and none of them is `C62`'s, which is consistent with the dry run's own table listing
only section-B `P15` receipts and `C62` being a `C`-series receipt outside it. **Said rather than
worked around**, and the re-point was measured here without it.

---

## ⓕ AMENDMENT, BEFORE ANY SHARE WAS READ: THE LOCATOR'S OWN CONTROL FIRED AGAINST ITS FIRST FORM

The locator as first written put its linear baseline about the **free** centre, `b0 + b1(\ell-\mu)`.
**Its own two-sided control refused it**: on a synthetic peak of known centre it recovered the centre
when the peak was planted at the window's middle, but a peak planted three multipoles off was read
**forty-three** multipoles off, because a baseline slope measured about a free centre trades against
that centre. ⇒ **The control fired before the instrument read a single spectrum, which is what it is
for.**

**THE REPAIR, AND IT IS THE SMALLEST ONE:** the baseline is anchored at the **fixed** window centre,
`b0 + b1(\ell-\ell_0)`, and the Gaussian width is bounded to `[20, 250]` multipoles. With that, the
control passes at **every** window from `25` to `120`: the planted centre comes back to better than a
thousandth of a multipole in both the centred and the displaced case.

⌗ **AND ONE MEASUREMENT THAT FIXES THE WINDOW HONESTLY RATHER THAN BY TASTE:** the fourth feature on
these spectra is **broad** — a full width at half maximum of about `172` multipoles, measured on the
arm of record itself — so a window of `40` is narrow against the thing it is fitting. The registered
`W = 40` is kept as the headline because it was registered, and `25` and `60` beside it as registered;
**but `80`, `100` and `120` are reported as well, labelled as added after the control rather than
registered**, because under a planted scatter the locator's error falls monotonically across that
ladder (`4.0`, `1.5`, `0.9`, `0.6` multipoles at `60`, `80`, `100`, `120`). **The verdict is read
against the whole ladder and the registered band is not moved to suit it.**
