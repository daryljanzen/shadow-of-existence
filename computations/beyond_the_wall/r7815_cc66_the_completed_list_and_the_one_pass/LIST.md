# `r7815+cc66` — THE COMPLETED LIST: every printed figure that rests on the ΛCDM control at its un-refitted point

*Registered in `PREDICTION.md` before the extended swap, the verdicts or any new value existed.
Order: `FOR_CC66.md` §`r7815` (69) — "Complete the list by **reading every sentence that names the
control or presents a standard-model figure**, in P15, P7, P18 and EXPLAINER.md, not only by
matching swap logs."*

**Reported before any edit, as ordered.** Nothing in `corpus/` is touched by this revision.

---

## 0. How the list was built, and the two halves it has

`r7812`'s list read the **swap logs** of five receipts. 69's ruling is that this is correct for what
it reads and incomplete for the pass. The completion has two halves, and they are built by different
means because they *are* different:

| half | how it is found | what it covers |
|---|---|---|
| **the cited half** | `scan.py` → `cross.py`: each sentence's `\rcpt{}` resolved to its receipt, each receipt's banks resolved **by path** and classified by the bank's own stored `(r_s, D_M)` | a figure whose provenance the paper itself declares |
| **the uncited half** | hand-read: the quantity the sentence prints is identified, and the receipt or run that owns **that quantity** is named | exactly the figures 69's ruling says the swap-log list missed |

`scan.py` reads **128 candidate sentences** out of the four documents — every sentence that names the
control in any of the corpus's spellings, or prints one of the figures `r7815`, `r7813` and `r7809`
name. `cross.py` traces 44 of them to a bank and leaves **84 citing no receipt**.

⛔ **`r7812`'s lesson is binding throughout: a number is not its quantity.** Matching a printed
figure to a measured one by value alone gave 26 false landing sites there. Every match below is by
quantity, with the receipt that owns it named.

---

## 1. ⛭ TWO CORRECTIONS TO THE ORDER'S LIST, BOTH MEASURED

### ⒜ Two of the four items named as missing are **not printed in any paper body**

69 asks for **the control's folded harmonic (1.80σ → 1.59σ)** and **the sky–control agreement
(0.79σ → 0.62σ)**, "wherever printed". Searched across `corpus/*.tex` and `EXPLAINER.md`:

- **`1.80`** occurs only in `corpus/appendix_receipts_P15.tex` l.1552 and its corpus-wide twin —
  inside the **generated** receipt blurb for the no-fit receipt (`0.2028\pm0.1126` (`1.80\sigma`)).
- **`0.79`** likewise occurs only in generated appendix blurbs.

On `r7667`'s distinction, kept at `r7809` and `r7811`, **a receipt cited in
`appendix_receipts_*.tex` is cited by construction and is not a sentence printing a figure.** So
these two are not prose edits at all: they follow the receipts' own pins and land through
`corpus/make_all_appendices.py`. They must still be *regenerated*, and that is a different operation
from re-wording a sentence — which is why saying so matters for a one-pass edit.

⇒ **But the harmonic's amplitude IS printed**, at P15 `l.1091`, as the control's
`$0.20\pm0.11$`. That is the same quantity at the precision the body prints it, and it moves
(`0.2028±0.1126` → `0.1734±0.1088`, i.e. `0.20±0.11` → **`0.17±0.11`**). So the harmonic is on the
list — as an amplitude in the body and a significance in the appendix, not as the `1.80` 69 named.

### ⒝ A landing site the order does not name: **P15 `l.293`, the control's θ\* pull, 4.94 → 1.97**

The sentence reads *"that angle is the standard model's own expression at the same background, so the
standard model pays the same pull there: **at its own background, before refitting, it sits `4.94`
standard deviations high**, and refitting relieves the two by over two standard deviations each."*

`r7805`'s receipt measures that `4.944` at `(67.40, 0.3150, 0.02237)` — the point it labels
"Planck's un-refitted point", and the very point `r7807+cc66` showed is **not** Planck 2018's
published best fit (implied ω_c `0.120727` against the published `0.1200`). So it is a control
figure at the un-refitted point.

`theta_at_planck.py` re-derives it through the **same functions the receipt uses**, and reproduces
the receipt's own `4.944` at the old point first, as its anchor:

| point | 100θ\* | pull |
|---|---|---|
| the corpus control point `(67.40, 0.3150)` | 1.04238 | **+4.944 σ** |
| Planck 2018 published `(67.36, Ω_m 0.313772)` | 1.04146 | **+1.973 σ** |
| | | **−2.970** |

⛔ **And the consequence is a clause, not a number.** The same sentence says refitting *"relieves the
two by over two standard deviations each"*. The control's own 185-bin refit minimum is `+2.643` on
this definition and **does not move with the point** (a minimum does not depend on where the search
started). So at Planck's point the control's un-refitted `1.973` is **lower** than its refitted
`2.643`: refitting no longer relieves the control, it costs it `0.67`. **That clause cannot be
re-pointed by changing a figure, and I am not the seat that rewrites it.** It is reported here so 69
reads it before the pass rather than after.

---

## 2. The calibration, restated through one procedure

69's ruling: *"every calibration sentence restates through one procedure"*, citing 70's receipt
`P15_at_plancks_point_the_control_returns_p1_p2_2_203_against_cambs_2_212_…`, and *"State it as what
the calibration is. It is not a correction to report."*

70's measurement, at Planck's point through P15's own matched locator: the instrument's
**P1/P2 = 2.2026**, CAMB's **2.2123**, the agreement **0.44 %**; KFAC 3.0 moves P1/P2 by −0.00014 %.
The extended swap independently reads the control's P1/P2 moving **2.204 → 2.203** under the
re-pointing, so the ratio itself is nearly point-independent; what changes is the **reference** it is
set against.

**The calibration sentences, all of them:**

| site | prints now | restates as |
|---|---|---|
| P15 `l.877` (`sec:refit-bound`) | "a first-to-second height ratio of `2.195` at peaks `220`, `536` and `814`, against a standard code's `2.200`—`0.23\%`" | the instrument's `2.203` against CAMB's `2.212` through one locator, **`0.44 %`** |
| P15 `l.150` (abstract) | "validated on its control to `0.23\%` in the first-to-second height ratio" | `0.44 %` |
| P15 `l.2827` (`sec:scope`, item 1) | "validated on its control to `0.23\%`" | `0.44 %` |
| P15 `l.857` | "a first-to-second height ratio of `2.1969` against a standard code's `2.200`—agreement to `0.14\%`" | the `0.14 %` is the *other* configuration's; see the note below |
| P7 `l.1869` (`frontier:scalar`) | "reproducing a standard code's first-to-second height ratio to `0.23\%` at peaks `220`, `536` and `814`" | `0.44 %` |
| P18 `l.1517` (`sec:acoustic`) | "reproduces a standard code to `0.23\%`" | `0.44 %` |
| P18 `l.1837` (`tab:required`) | "the control reproducing a standard code to `0.23\%`" | `0.44 %` |
| P18 `l.3066` (`sec:displace`) | "the control reproduces a standard code to `0.23\%`" | `0.44 %` |

⛔ **The `0.14 %` at `l.857` needs its own read and I flag it rather than fold it in.** P15 already
distinguishes the two: `l.877` says *"the closer `0.14\%` belonging [to the other path]"*. 70's
measurement is on the **polarisation path**, which is `l.877`'s. Whether `l.857`'s `0.14 %` restates
through the same one procedure is a second measurement (its own path's CAMB number through the same
locator), and 70's receipt does not carry it. **It is on the list as owed, not as answered.**

---

## 3. The cited half — measured by the extended swap

`r7809`'s `repoint.py` swapped **5** receipts. **21** receipts load a swappable control bank
(`refit_grid185/lcdm_base.npz`, `r7093_directions/grid_oneclock/lcdm_base.npz`,
`r7095_directions/grid_licensed/lcdm_base.npz`). The swap is extended to all 21. Every pair is
grid-identical, asserted before anything runs, so the swap moves the **point** and nothing else.

*(table filled from `swap_01_02.txt` and `swap_03_21.txt` — see §6 for its current state)*

---

## 4. The uncited half — the owners, and what each needs

Each printed figure below cites no receipt in its own sentence. The **quantity** was identified by
hand and its owner named; `owners.py` then reports that owner's own banks and their point classes,
so "it moves" is a statement about a stored background and not about my recollection.

| printed figure | site(s) | owner | owner's control bank | needs |
|---|---|---|---|---|
| `0.918` the no-fit ratio | P15 `l.143`, `l.577`; P7 `l.1880`; P18 `l.1546`, `l.1846`; EXPLAINER `l.257` | `P15_with_the_projection_distance_on_the_leaf_rate_…`, `P15_the_po87_list_is_14_repoints_…` | `spectra/cc66_lcdm_L2000.npz` **UNREFIT** | the **step-2 assembled bank**; `0.964` as measured is step-8 against step-2 |
| `1.13` per bin, arm `2.65`, factor `2.35` | P15 `l.1082`; P18 `l.1547`, `l.1856` | `P15_the_no_fit_confrontation_…` | `refit_grid185/lcdm_base.npz` **UNREFIT** | **measured**: `1.13` → `1.08` (`r7812`) |
| the control's folded harmonic `0.20±0.11` | P15 `l.1091` | `P15_the_no_fit_confrontation_…` | same | **measured**: → `0.17±0.11` |
| `1.18` per d.o.f. full range, `78 %`, reference `1.01` | P15 `l.920`, `l.930` | `P15_the_control_entered_the_regime_and_the_arm_did_not_move` | `spectra/c54.175/177/178_lcdm.npz`, `c54.186_lcdm_L3000.npz` — all **UNREFIT** | **a run**: no swap reaches these grids. 69's `(4d)` ruling already has it re-derived in the pass |
| `1.16` per bin lensed | P15 `l.2087`; P18 `l.1547`, `l.3066` | `P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and_the_control_is_nearly_camb` | builds `cc66_{tag}.npz` at runtime → `spectra/cc66_lcdm*` **UNREFIT** | the **step-2 assembled bank** |
| `2.10` per bin, 133-bin unlensed | P15 `l.939`; P18 `l.1548` | `P15_the_133_bin_pair_is_computed_and_asserted_…` | reads `spectra/*` by tag, **UNREFIT** | a run in the 133-bin unlensed configuration |
| `1.77`, `1.35`, `2.09` the separation measures | P18 `l.1550` | `P15_the_two_measures_of_the_separation_are_pinned_…` | `spectra/cc66_lcdm_L2000.npz` **UNREFIT** | the **step-2 assembled bank** |
| `1320` → `921`, `1320` → `989` lensing scan | P15 `l.765`, `l.772` | `P15_derived_lensing_on_the_lcdm_arm`, `P15_what_is_left_is_lensing_and_not_reionisation` | `spectra/c54.178_lcdm.npz` **UNREFIT** | a run on that configuration |
| the control `1.2` σ high of the located sky | P15 `l.909` | `P15_the_skys_own_fourth_peak_…` (in the 21) | swappable | the extended swap |
| `ℓ_A` `301.375` | P15 `l.1975` | `P15_at_its_own_preferred_H0_…` | swappable | **measured**: → `301.602` |
| the control's comb `297.0` / `296.0`, ratios `2.195` / `2.191` | P15 `l.2108` | `P15_at_its_own_preferred_H0_…`, `P15_the_monopole_zero_point_…` | the first swappable; the second **REFIT185** | the extended swap; the `2.191` does not move |
| `φ/π = −0.2361` for the control | P15 `l.164` | `P15_the_sky_phase_fit_and_its_uncertainty` — **parses the paper's own numbers** | none | the figure's own producer is not that receipt; traced in §5 |
| `186.007` / `186.135` / `186.85` / `186.51` | P15 `l.2004`, `l.2006` | `P15_the_fit_has_the_controls_freedom_…` | `refit_grid185/lcdm_base.npz` **UNREFIT** + refitted banks | the extended swap, and the refitted ones are immune |

---

## 5. What stays where it is, and why — the `(b)` and refitted populations

### ⒜ Refitted figures are immune, and this is structural rather than observed

Every figure taken **at a refit minimum** cannot move with the control's starting point, because a
minimum of the fit does not depend on where the search began. That reaches `1.002` (P15 `l.577`,
P7 `l.1880`, P18 `l.1546`, EXPLAINER `l.257`), the control's refitted `1.01` against the arm's
`1.61`, the tilt `0.954`, the contrast coefficient `−0.0075±0.0083`, the refitted `186.51`, and the
sign-change count `87`. `r7809` item ③ showed this for the `1.002`; the extended swap is the test of
it for the rest, and a move in any of them would mean the discriminator is wrong, not that the
figure moves.

### ⒝ P15's **fourth feature** does not move, and this was `r7809`'s headline

`pol_lcdm.npz` stores `(145.382039, 13954.353506)` — the 185-bin refit minimum, bit-identical to
`spectra/cc66_r185_verify_lcdm.npz`. So the one-rate differences `0.00` / `0.18` / `0.21`
(P15 `l.896`) read the **refitted** control and are untouched. `r7809`'s order listed them wrongly
and `r7813` took the correction.

### ⒞ The mechanism block (`fig:acoustic-nofit` → `eq:acceptance-law`) reads other banks entirely

The retention, acceptance, sound-speed and window figures — `1.054`, `1.028`→`1.075`, `1.026`,
`1.061`, `0.455`/`0.395`, `4.43`/`5.14`, `0.0652`/`0.0645` — trace to `r6893`, `r6911`, `r6915`,
`r6919`, `r7041` banks, classified **NOBG** or **REFIT185**. None is at the un-refitted point. On
`r7811`'s `(b)` ruling they would stay in any case, the control there being an instrument and not
the comparison; the bank classification says they *cannot* move, which is the stronger statement.

### ⒟ Within-control differences stay, per `r7811`'s `(b)`

The driving subtraction `0.1792` (P15 `l.973`, P7 `l.1875`, P18 `l.1829`), the visibility-width
experiment `15.5 %` and its harmonic `0.3704` → `0.3633` (P15 `l.2124`, `l.2128`), and the
no-drive/no-Π/tilt/NS± variants are differences **within** the control family. Their sentences were
read for 69's `(b)` test — *"its sentence must not present the number as the standard model's at
Planck's point"* — and **none of them does**: each is phrased as a subtraction or a swap performed on
the control, not as a standard-model value.

---

## 6. State of this revision

| item | state |
|---|---|
| `scan.py`, `cross.py`, `owners.py`, `theta_at_planck.py` | banked and pushed |
| the extended swap, receipts 1–2 of 21 | `swap_01_02.txt` — 11 moved, 0 moved |
| the extended swap, receipts 3–21 | running |
| `(a1)` slice 4 of 4 (`2250:2547`) | running |
| the step-2 assembly, and the figures that wait on it | after slice 4 |
