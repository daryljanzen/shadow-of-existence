# r7811 — the 37 non-control-proper banks, classified (a)/(b) by reading each citing sentence

Registered in `PREDICTION_r7811.md` before any of this was read. Written by `cc66`.

69's ruling: **(a)** a variant bank whose printed figure is an arm-against-standard-model comparison
gets its own run at Planck's point; **(b)** one whose printed figure is a within-control difference
stays, and its sentence must not present the number as the standard model's; **(c)** the 8 beyond
every re-pointed bank's ℓ reach are classified the same way, naming the reach any (a) needs.

⛔ **The split is decided by reading the citing sentence and never by the bank's filename** — the
filename says which switch the bank carries and says nothing about what its sentence claims. That is
`r7807`'s attribution lesson carried from recipes over to prose, registered in advance as (4e).

## ⛔ A CORRECTION TO THE ORDER'S FRAMING: 20 of the 37 are not on the printed list at all

The ruling's (a)/(b) presumes each of the 37 *has* a printed figure to classify. Most do not. Keyed
on `check_figures_pinned.sites()`'s own `PROSE` population — a citation in a paper **body**, never the
generated appendix lists (`r7667`'s distinction, kept) — **20 of the 31 distinct basenames covering
the 37 are reached by no body sentence that prints a figure.** They are instrument banks: the `NS±`
derivative grids, `lcdm_0.700/0.800/0.900/1.100/1.200/1.300`, the `DAMPX` pairs, `L824_L3200`,
`L820` guardfail and nk600, `cc66_lcdm_fluid`, `cc66_lcdm_nodrive_pol`, `c54.178_noPi`,
`c54.178_noBsplit`, `refit_grid/lcdm_base` and `cc66_refit_lcdm_base`.
⇒ **Nothing is owed for those: no figure moves if they stay exactly as they are.**

## ⛭ AND ONE BASENAME SPANNED TWO TIERS, WHICH MY OWN CENSUS'S GATE WAS TOO COARSE TO CATCH

`lcdm_base.npz` exists at four paths carrying `dev = [0.0, 0.007286]` — three control-proper grids
and the variant `refit_grid/lcdm_base.npz`. My `r7809` census refuses a basename whose paths span two
**point** classes, and all four share the point, so the gate passed them; the ambiguity that matters
here is **tier**, which is finer than the gate I built. Said plainly because it is my instrument's
defect and the second time this round the basename has been the hazard.
**Resolved by reading each receipt's own path construction rather than its basename:** both receipts
that name it build `refit_grid185/lcdm_base.npz` explicitly — one via
`_matched('refit_grid185/lcdm_base.npz')`, one via `os.path.join(G185, 'lcdm_base.npz')` with
`G185 = .../refit_grid185`. ⇒ **Both reads are CONTROL-PROPER**, and the variant `refit_grid` copy is
cited by nothing.

## The 10 reached variant / beyond-reach banks

### (a) — an arm-against-standard-model comparison ⇒ its own run at Planck's point

| bank | tier | why (a) |
|---|---|---|
| `spectra/cc66_lcdm.npz` | VARIANT, dev `7.4e-03`, ℓ≤1298 | Its sentences are arm-against-control throughout, one of them saying so in as many words: *"the spectrum's own parameters are refitted, which is **the comparison the standard model is usually judged by** … the control settles at $1.01$ in $\chi^2$ per bin and this arm at $1.61$"*. Also prints the control's $2.10$ per bin, $214.1$ vs $502.1$, $279.4$ vs $584.0$ and the refit minima. |
| `spectra/c54.175_lcdm.npz` | VARIANT, dev `0.997`, ℓ≤1996 | *"The sky's own value … is $P_1/P_2=2.2564\pm0.0772$, and **flat $\Lambda$CDM's is $2.200$**; what this construction returns for the same quantity is $2.264$"* — a control number presented **as the standard model's** and compared against the construction's. |

⛭ **The (a) run needs ℓ ≤ 1996 at most, so no high-ℓ run is required**, and `cc66_lcdm.npz`'s own
reach (ℓ≤1298) is a subset of the `LSTEP=2` grid already in flight.

### (b) — a within-control difference ⇒ stays where it is

`c54.177_lcdm`, `c54.178_lcdm`, `c54.186_lcdm_L3000`, `c54.193_lcdm_nodrive_L3000`,
`r7201/lcdm_nodrive`, `lcdm_0.859`, `lcdm_1.000`, `L820_lcdm_L2512_nk800` — eight.
Their figures are differences taken inside the control family: the driving removed (first peak
$220\to274$, $\ell_1/\ell_A$ by $0.1792$), the de-tilted peak set's separation factors ($11.7$,
$18.3$), the bootstrap threshold reading ($0.953$, $12.6$, $0.76$), and the shear coefficient
($1.1996$ against $6/5$) whose sentence states outright that the common normalisation *"cancels in
the ratio"*. In each the control is the instrument and not the comparison.

### (c) — the 8 beyond ℓ reach

Reached by a printed figure: `L820_lcdm_L2512_nk800` (ℓ≤2508), `c54.186_lcdm_L3000` and
`c54.193_lcdm_nodrive_L3000` (ℓ≤2996) — **all three are (b)**. The other five
(`L824_lcdm_L3200`, `r4494_DAMPX×2`, `r7099_DAMPX×2`) are on no printed list.
⇒ **No (a) lies beyond ℓ reach, so no high-ℓ run is needed at all.**

## ⛭ (4d) — the (b) sentences that present a control number as the standard model's

One sentence, shared by `c54.175`, `c54.177`, `c54.178` and `c54.186_L3000`, is a (b) by its
construction and still prints the control's absolute goodness of fit:

> *"it was 78 % of the control's remaining $\chi^2$, and taking it out brings **the control to
> $1.18$ per degree of freedom over the full range** against a reference $1.01$."*

The comparison is the control before against the control after a truncation is removed — within-control,
so (b). But `1.18 per degree of freedom over the full range` reads as the standard model's fit
quality, and at Planck's point it would not be `1.18`. **Reported, not edited: it is 69's sentence to
land.** Every other (b) sentence read above states its quantity as a difference or a ratio and does
not present a standard-model number.

## ⛭ A landing consequence 69 needs before the one pass: four receipts pin the OLD `D_M` as a literal

`13864.6627` — the un-refitted `D_M` — appears as a hardcoded literal in
`P15_the_no_fit_confrontation_…`, `P15_the_background_returns_the_larger_stretch_…`,
`P15_the_wrap_fix_is_applied_…` and `L147_two_arm/B1_the_control_separates_prediction_…`.
Those pins stay **true** while the old bank stays on disk, because re-pointing adds a bank rather than
mutating one. But **each read that is re-pointed needs its literal moved to `13894.421`** in the same
pass, or the receipt asserts a `D_M` its new bank does not have. Named here so the one-pass landing
does not discover it as a red.

## Predictions: how they fared

* **(4a) FAILED in shape.** I predicted 19–26 of 29 in (b) and 3–10 in (a). The real split is
  **2 (a), 8 (b) and 20 not on the printed list at all** — a category the order's (a)/(b)/(c) has no
  slot for, and the reason my band was meaningless rather than merely wrong.
* **(4b) HELD, partly.** `cc66_lcdm.npz` is an (a) as predicted. But `refit_grid/lcdm_base.npz` and
  `cc66_refit_lcdm_base.npz`, which I also named, are cited by **nothing**, and `c54.175` — which I
  listed only as a "possibly" — is the second (a). **No `NS±`, tilt, `nodrive`, `noPi`, `noBsplit`
  or `fluid` bank landed in (a)**, so the ruling's boundary is where I expected it.
* **(4c) FAILED.** I predicted 1–3 of the beyond-reach 8 in (a), needing ℓ ≥ 3000. **None is an (a)**,
  so no high-ℓ run is needed.
* **(4d) HELD at the central guess.** Predicted 0–3 such sentences, central 1; **measured 1.**
* **(4e) EARNED ITS KEEP.** The filename would have put `c54.175_lcdm` with its sibling variants in
  (b); its sentence is what makes it an (a). And the `lcdm_base` tier ambiguity was resolved by path
  construction, not by name.
