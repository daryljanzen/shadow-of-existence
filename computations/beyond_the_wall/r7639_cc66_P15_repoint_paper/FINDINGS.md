# `r7639+cc66` — ⑴ ATTEMPTED END TO END ON ONE RECEIPT, AND IT REVERTED. THE RULE NEEDS ONE AMENDMENT, AND `70` NEEDS FOUR MORE SPECTRA

*`r7639` ⑴ says: when you re-point a receipt, move the number(s) P15 prints from it in the same commit. I did
exactly that, for `monopole_zero_point`, through the paper, the PDF, the served page, the appendix and the
INDEX row — and then reverted the whole unit, because **the figure is jointly cited and the other citer
cannot carry it.** Everything below is measured; the tree is back at baseline, all gates green.*

## ⓵ WHAT I DID, AND IT WORKED AS FAR AS ONE RECEIPT GOES

`monopole_zero_point` re-pointed to the arm of record: `rc=0`, 22 PASS. Contrast **`1.04015 → 1.04403`**,
which is `70`'s independently reported `1.044` on a different code path, inside the `[1.02, 1.07]` band
`r7635+70` registered. Then, in the same working tree:

| what | change |
|---|---|
| `corpus/CR_cosmology.tex` l.1120 | *"This arm's acoustic oscillation is $1.040$ times the control's"* ⇒ **`1.044`** |
| `corpus/CR_cosmology.pdf` | rebuilt, `pdflatex` twice from `corpus/` — **324 pages, 0 errors** |
| `BOOK_INTRO_cosmiCave/paper_P15.html` | regenerated (`scripts/gen_paper_html.py P15`) |
| `receipts/INDEX.md` row 908 | *"the contrast against the **control** ($1.040$)"* ⇒ **`$1.044$` on the arm of record** |
| `corpus/appendix_receipts_{P15,corpus}.tex` | regenerated (`corpus/make_all_appendices.py`) |

⌗ **Row 908 carries three `1.040`-shaped figures and only one of them is the receipt's own.** The other two
are quotations and were left untouched: `cc66.36`'s *"`DPSRC=0` taking the arm's oscillation from `1.040` to
`1.828`"* — which `r7639` ⑵ makes **history** — and `cc66.35`'s `1.0401`. *Editing either would have
falsified a quotation to make a gate green.*

## ⓶ THREE GATES FIRED ON THE PAPER EDIT, AND EACH HAD A REMEDY I APPLIED

**None of these is visible to `turn_gates`** — all three are in CI's `fast` list, which is why the pre-push
set is now that list and not the lean batch.

**⒜ `check_pages_current`** — `paper_P15.html` behind its source. Regenerated. Green.

**⒝ `check_explainer_pins`** — `MOVED` on `[acoustic-run]`, `EXPLAINER.md` l.261, because the section it
watches (`CR_cosmology.tex#sec:refit-bound`, `\subsection{The acoustic comparison}`) changed. **My edit is
inside that section** — confirmed by reading the enclosing `\label`, not assumed. The gate's own standing
notice says `EXPLAINER.md` is under a full rewrite by `69` on Daryl's direction and **must not be repaired
in place**, and that a blocking fire may be restamped *provided a note records the reread as `69`'s*. ⇒ I
routed it in `FOR_69.md` and restamped, and the gate went green. ⌗ *Both the note and the restamp were then
reverted with the rest of the unit, since the tex edit that moved the section is reverted — the stamp
records a digest of text that no longer exists. **When you land the split in ⓹ I route and restamp then**,
and this paragraph is the record that the path is known and tested rather than guessed at.*

**⒞ `check_figures_pinned`** — and the first half of this one is a reusable finding.

The paper now printed `1.044`; my pin in the receipt was `abs(C_C - 1.04403) < 5.3e-4`, which I had set
from the pin rule's `max(0.5·10^-5, 5e-4·1.044) = 5.22e-4`. **The gate still called the figure unpinned,
and it was right.** A half-width of `5.3e-4` about `1.04403` admits up to `1.04456`, and *that rounds to
`1.045`, not to the `1.044` the paper prints.*

⇒ **The pin rule's `max(...)` is an upper bound on a tolerance, not a licence to use it.** A pin must also
not admit a value the paper would print differently. Tightened to `4e-4` — which keeps the whole interval
inside `1.044` — and that row cleared.

## ⛔ ⓷ AND THE ONE THAT COULD NOT BE FIXED: THE FIGURE IS JOINTLY CITED

After all of the above, exactly one row remained:

```
[UNPINNED] CR_cosmology.tex  1.044  cites P15_the_model_difference_is_an_acoustic_contrast_difference_…
[STALE]    CR_cosmology.tex  1.040  cites P15_the_model_difference_…  -- now pinned or gone; lower the row by 1
```

**P15 l.1120–1123 closes with TWO `\rcpt{}`s** — `the_model_difference_…` and `the_monopole_zero_point_…` —
and the gate's key is, in its own words, **`(population, paper, receipt, figure)`**. So one printed figure
beside two citations is **two sites**, and each needs *its own* receipt to pin it. `monopole` pins `1.044`.
`model_difference` cannot.

**And the baseline cannot absorb it:** the gate's design is that *"a NEW figure printed beside a receipt
that does not pin it fails, and a baselined one that comes to be pinned is STALE … so the baseline can only
shrink."* Adding a row would be hiding an unpinned figure.

The gate's three remedies are *pin it*, *cite the receipt that does pin it*, or *print fewer digits*:
- **pin it** — false. `model_difference` is on the old arm and computes `1.040`.
- **cite the receipt that does pin it** — that means splitting the sentence so the figure sits beside
  `monopole` and the `‖Δ‖²` clause stays with `model_difference`. **That is a structural edit to P15, which
  is yours to land, not mine.**
- **print fewer digits** — `1.04` loses the four-per-cent statement the sentence is making.

⇒ **The whole unit is reverted and the tree is back at baseline, all gates green.**

## ⛔ ⓸ WHY `model_difference` CANNOT BE RE-POINTED — A FOURTH BANK GAP, FOR `70`

Measured: **the four CAND knob pairs have no arm-of-record counterpart on either arm.**

| candidate pair | on disk | `_leafrec1` |
|---|---|---|
| `r6885_ln24_{lcdm,cr}` | yes | **no / no** |
| `r6885_noisw_{lcdm,cr}` | yes | **no / no** |
| `r6885_dre0_{lcdm,cr}` | yes | **no / no** |
| `r6885_drc0_{lcdm,cr}` | yes | **no / no** |
| `r6885_{los,losdp0,lossw0}_cr`, `r6889_nufs0_cr` | yes | yes (control side correctly absent — it does not move) |

Those four are read by section (c), *"THE THREE INSTRUMENTED CANDIDATES, each switched off on BOTH arms"*,
and compared against the arm. ⇒ **Re-pointing the arm while they stay on namesakes makes every candidate
comparison cross-arm.**

⚠⚠ **And it would go GREEN.** Under the dry re-point only ONE check in this receipt moved — the `DPSRC`
bit-identity — so a seat that re-pointed the arm and applied ⑵ would get a clean receipt whose section (c)
silently compares a **new-arm** base against **old-arm** candidates. *That is exactly the silent class I
reported at `r7637+cc66.1` ⓷, and it is why I did not take the green.*

## ⓹ WHAT I NEED FROM YOU — ONE AMENDMENT TO ⑴, AND A SENTENCE

**⑴ as written covers a figure one receipt carries.** It does not cover a figure **two** receipts are cited
for, because the gate keys per receipt and both must pin it. There are more of these: of my 44, **13 sit
beside a printed figure**, and l.1120 is not the only sentence closing with two `\rcpt{}`s.

**⇒ Proposed amendment, for every seat:** *when a sentence's printed figure is cited to more than one
receipt, the figure moves only when every cited receipt that computes it has been re-pointed; otherwise the
sentence is reported, not edited.*

**And the sentence, with my proposed wording** (l.1120–1123, `sec:refit-bound`):

> *current* — "This arm's acoustic oscillation is $1.040$ times the control's about its own envelope, and
> one direction built from the control alone---raise the oscillation at fixed envelope, with nothing
> fitted---carries half of $\lVert\Delta\rVert^{2}$\rcpt{…model_difference…}\rcpt{…monopole_zero_point…}."
>
> *proposed* — split so each figure sits beside the receipt that pins it:
> "This arm's acoustic oscillation is $1.044$ times the control's about its own
> envelope\rcpt{…monopole_zero_point…}. And one direction built from the control alone---raise the
> oscillation at fixed envelope, with nothing fitted---carries half of
> $\lVert\Delta\rVert^{2}$\rcpt{…model_difference…}."

`1.044` is measured (`1.04403`) and pinned to `4e-4`; the `‖Δ‖²` clause is untouched and stays with the
receipt that owns it. **On your word I land the receipt, the split and the PDF in one commit.**

---

# ⑶ IS APPLIED, AND THE BANK GAP IS MEASURED RATHER THAN DISCOVERED ONE RECEIPT AT A TIME

## ⑶ — PART 3 of the 133-bin receipt is HISTORICAL, on a measurement

The order's reason is the right one and it is now asserted in the file rather than taken on the word:

| | `max |dD_l|`, 68.60 leg against 68.62 leg |
|---|---|
| the namesakes | `2.4067e-04` — two runs, and PART 3 reads them |
| **the arm of record** | **`0.0000e+00` — one point** |

`r7635+70`'s manifest records the 68.62 leg as banked from the h686 run for exactly this reason. So the
`4.16`-against-`4.19` distinction is a property of the **superseded instrument state**. It stays recorded —
the provenance defect it found was real and the hardcoded literal it names is still in the other receipt's
source — and it is **not re-asserted** on the arm of record, because there is no second point there to
assert it against. PART 3's banner, the docstring map, the closing summary and the INDEX row all say so.

**The marking is itself a check, and it was perturbed until red.** The new assertion is that the pair is
two points on the namesakes AND one point on the arm of record, each on one `ell` grid:

```
AOR_8662 = 'cc66_lcdm'        # same 133-bin grid, different spectrum
  -> FAIL -- PART 3's historical marking rests on the pair being two points on the namesakes
             (2.4067e-04) and one on the arm of record (9.4260e-02), and it is not
```

⌗ *A first perturbation — pointing the leg at `cc66_r185_verify_cr_leafrec1` — went red on the `ell`-grid
guard instead, so it tested the wrong branch. Recorded because the weaker test is the one that would have
looked like a pass of the stronger.*

## AND THE REST OF THAT RECEIPT IS NOT RE-POINTED, FOR A STATED REASON

**It is a provenance record of three named banked files, not a live score.** PART 2 identifies
`cc66_cr_x_h686_pol` by reproducing the `556.7` `FOR_66` records for `cc66.7` — an identification of a
*file*, which cannot move with an arm. So its reads stay on their namesakes and its figures stay as
recorded, and what the arm of record says on the same bins is **reported**:

| | control | arm, namesake | arm, arm of record |
|---|---|---|---|
| 133-bin `chi^2` | `279.4200` | `556.6858` | **`447.3733`** |
| per bin | `2.100902` | `4.185607` | **`3.363709`** |
| ratio to the control | `1` | `1.992290` | **`1.601078`** |
| 185-bin `chi^2` | `695.9666` | `1169.8183` | **`938.3175`** |
| 185-bin per bin | `3.761981` | `6.323342` | **`5.071986`** |

**That changes what a sentence CLAIMS**, so under ⑴ it is reported and not edited. The sentence is
`CR_cosmology.tex` l.956, `sec:refit-bound`, and this receipt is its only citation for that clause:

> *current* — "…the same comparison unlensed over $133$ bins giving $279.4$ against $556.7$, a factor
> $1.98$; lensing is worth proportionally more to a spectrum whose peaks are already in
> place\rcpt{…133_bin_pair…}."

**The control's $279.4$ does not move** — the control does not move. The arm's two figures do, and the
factor with them. Three ways to land it, my recommendation first:

1. **Keep the sentence as the historical reading it is**, and say so: *"…giving $279.4$ against $556.7$, a
   factor $1.98$ on the configuration those spectra were banked in"*. Nothing moves, and the receipt that
   pins it is already marked as a record of those files. This is the honest reading, because the lensed
   `$550.5$` and `$2.57$` beside it at l.955 are **another receipt's** namesake figures and would still be
   on the old arm — moving mine alone would put two arms in one paragraph, which is the defect PART 3 of
   that very receipt exists to report.
2. Move it to the arm of record — *"$279.4$ against $447.4$, a factor $1.60$"* — **but only together with
   the lensed receipt**, so the paragraph stays on one arm.
3. Drop the clause.

⌗ *The other four citations of this receipt (l.922, l.955, l.962, l.1070) print figures that are either the
control's or other receipts', so they are unaffected. `4.16` and `4.19` appear in the paper only inside a
TeX comment at l.37.*

## THE BANK GAP, MEASURED ACROSS ALL 44 — FOR 70, SO IT CAN BE BANKED IN ONE PASS

`bank_gap_sweep.py` here, output in `bank_gap_sweep.txt`. **13 CR-arm bank spectra that my 44 read have no
`_leafrec1` counterpart, touching 11 of the 44.** This **supersedes the "three unbanked CR spectra" I
reported at `r7637`** — that count was what I had found by hand, receipt by receipt, and it was low.

| spectrum | readers |
|---|---|
| `r6893_switch_screen_cr` | 6 |
| `r6919_injected_cr` | 3 |
| `r6929_scan_cr` | 3 |
| `r6925_visleaf_cr` | 2 |
| `r6941_fine_cr_visleaf` | 2 |
| `r6885_ln24_cr`, `r6885_noisw_cr`, `r6885_dre0_cr`, `r6885_drc0_cr` | 1 each (`model_difference`) |
| `r6889_noop_cr`, `r6889_hdp0_cr`, `r6889_hsw0_cr` | 1 each (`source_decomposition`) |
| `r6893_fine_grid_cr` | 1 |

**Separately, four response-grid directories have no arm-of-record counterpart at all** — `refit_grid`,
`refit_grid185`, `r7093_directions/grid_oneclock`, `r7095_directions/grid_licensed` — read by
`full_range_refit`, `refit_leaves`, `no_fit_confrontation`, `refit_bound_figures`, `phase_slope` and
`de_tilted_peak_set`. That is the "response grids (6)" already on the list, now named by directory.

**The instrument, and why the first two versions of it were not one.** A receipt need never name a spectrum:
it loads `f'r6941_fine_{t}.npz'`. My first sweep read only literals and missed whole families. My second
matched each TEMPLATE as a regex against the bank and credited `r6941_fine_cr_visleaf` with **23** readers
where it has **2** — `r6941_fine_{t}` with `t` in `('lcdm','cr')` cannot produce that name, but a permissive
placeholder matches it — and attributed sixteen `cc66_cr_*` spectra to one receipt that **does not mention
any of them**. *That is the fifth time this campaign that an instrument which RUNS was not an instrument
which MEASURES, and it was caught by reading its own rows against a count I had already made by hand.*

So this sweep expands every template over the values its placeholder can actually take, and prints what it
cannot resolve. **And it is validated by tracing `np.load` through all eleven gap-carrying receipts:
24 of 24 (gap, reader) pairs are a real load, and the swept and traced sets agree exactly in nine of the
eleven.** The two that differ are one declared over-match — a dict-keyed suffix (`{arm}{AOR[arm]}`) expanded
as a cross product in `free_streaming`, naming two pairs the code never forms, both of which *do* have
`_leafrec1` and so are not false gaps. **The sweep over-counts and never under-counts, which is the safe
direction for a list someone else will work from.**

---

# ⑵ IS APPLIED TO BOTH RECEIPTS, AND IT REMOVES ITSELF AS A HOLD

## What was done

**Both receipts now load the historical comparison through a `hist` loader that reads the `LEAFREC=0`
namesakes and records what it read**, guarded by a check that asserts the two files *actually read* are
`cc66_r185_verify_{lcdm,cr}.npz`. Each carries a docstring paragraph naming the superseded state — the
instrument before `_SWSRC`/`_DPSRC` were wired into `_project` at `r6889+cc66.36` (`736f9399`). The P15
sentence classing is `P15_SENTENCES_dpsrc.md` beside this file.

In `source_decomposition` the pin covers **all three** uses of that pair — PART 1's `DPSRC=0` bit-identity,
PART 2's `r6889_noop` "bit-identical on both arms" default proof, and PART 2's "every newly wired switch
reaches the term it names" demonstration. All three are measurements of the r6885/r6889 tree.

## Perturbed with the re-point it exists to resist, and both go red

The perturbation is not an arbitrary substitution: it is **the per-arm suffix map a real re-point would
use**, `f"cc66_r185_verify_{t}{'_leafrec1' if t == 'cr' else ''}.npz"`.

| receipt | result |
|---|---|
| `source_decomposition` | `rc=1`, **3 FAILED** — the guard, PART 1's bit-identity, and PART 2's default proof |
| `model_difference` | `rc=1`, **2 FAILED** — the guard and part (b)'s bit-identity |

And the guard reports the cause rather than a verdict: *"the two files actually read are
`['cc66_r185_verify_lcdm.npz', 'cc66_r185_verify_cr_leafrec1.npz']`"*.

## ⚠ AND MY FIRST VERSION OF THAT GUARD WOULD HAVE LET THE RE-POINT THROUGH

The first guard asserted `'_leafrec1' not in NAMESAKE` — a check on the **constant**. The re-point above
never touches `NAMESAKE`; it changes what `hist` builds from it. So the guard would have passed while the
comparison it guards went cross-arm. Rewritten to **record what `hist` loaded and assert on that**.

*Sixth time this campaign that a check which RUNS was not a check which MEASURES — and this one was in my
own guard, written in the same revision that reported the other five.* ⌗ *What is left is the honest
residual: a re-point that replaces `hist` wholesale defeats any guard inside it. That is why the pin is not
the only protection — **the bit-identity check itself fails**, and it is that measurement, not the guard,
that makes the re-point impossible to take green.*

## The figures, in this receipt's own statistic

⌗ **A correction to my own earlier report.** At `r7637` I gave this comparison as *"`0.000e+00` on the old
arm and `2.270e-01` on the arm of record"*. That `2.270e-01` was in the dry-run sweep's own statistic, which
is not the one the receipt's check uses. In `max |dD_l|`, which is:

| comparison | `max |dD_l|` |
|---|---|
| `r6885_dp0_{lcdm,cr}` against the **namesake** base | **`0.000000e+00`** on both legs — the bit-identity |
| `r6885_dp0_cr` against the **arm-of-record** base (what a per-arm re-point produces) | `2.529416e-02` — cross-arm, measures nothing |
| `r6885_dp0_cr_leafrec1` against the **arm-of-record** base (both legs honest) | `9.466893e-02` — the knob **is** wired there |

⚠ **Note the third row: `r6885_dp0_cr_leafrec1` exists.** So this family *is* reachable on the arm of
record. What is **not** reachable there is the bit-identity, because on that arm there is nothing
bit-identical to measure. That is why ⑵ pins it rather than moving it.

## ⑵'s listing: no P15 sentence cites either receipt for the bit-identity

**Measured, not assumed:** `CR_cosmology.tex` contains no occurrence of `bit-identical`, `unwired`, `DPSRC`
or `not a null`. The three sentences that do cite these receipts cite them for other claims, and all three
are **CONSTRUCTION**:

| line | receipt | claim | status |
|---|---|---|---|
| l.1123 | `model_difference` (+ `monopole_zero_point`) | the `$1.040$` contrast and the half of `‖Δ‖²` one control-only direction carries | reported at `r7639+cc66.1` with a proposed split; `1.04403` measured |
| l.1147 | `model_difference` | the three features of this arm's residual are all `Δ`'s — incl. `$-1.074$` of `$-1.177$` in fifteen bins | held on the four `r6885` CAND knob pairs |
| l.1153 | `source_decomposition` | the contrast direction is the monopole/Doppler balance, bracketed by removing each and re-projecting on both paths | held on `r6889_{hdp0,hsw0}_cr` |

⇒ **Nothing leaves P15 and nothing is restated there.** The finding lives in the two receipts, in `FOR_66.md`
(`cc66.36`) and in `INDEX.md` row 908 as a *quotation* of `cc66.36`, and it is restated as history in all of
those places that this seat owns.

## And ⑵ removes itself as a hold

| receipt | before ⑵ | after ⑵ |
|---|---|---|
| `model_difference` | the DPSRC substitution **and** four unbanked knob pairs | the **four knob pairs only** |
| `source_decomposition` | the DPSRC substitution **and** `r6889_{noop,hdp0,hsw0}` | the **three `r6889` spectra only** |

The DPSRC substitution was a hold because re-pointing the base would have moved a historical comparison.
Pinning it to the namesakes removes that, and removes it in a way a later re-point cannot quietly undo.

---

# SET A: THE INSTRUMENT FIRST, AND IT IS VERIFIED BEFORE IT IS USED

`own_comb_kinds.py` here, output in `own_comb_kinds.txt`.

**Why a new instrument was needed at all.** `r7637+70`'s `band_excess_own` carries the arm onto the
control's comb coordinate before the seven bands are cut, which is what removes the beat. Its envelope is
the retention law's running arithmetic **mean**, lifted unchanged — and that is exactly **one** of the four
readings the step receipt uses to show the step is the excess's and not the estimator's. The other three are
a running **median**, a **Savitzky-Golay** fit, and a reading that needs **no envelope at all** (the
peak-to-trough depths between consecutive extrema).

⇒ **The carry is about the abscissa and the window width, not about the kind of envelope.** It maps the
arm's `x` to `u = T_c (x / T_a + Δφ/2π)` and widens the arm's window to one of *its own* periods,
`T_a / T_c`. Neither step mentions how the envelope is estimated, so it generalises to all four; the depths
reading carries by mapping the extrema's own `q`. *The generalisation is this seat's; the combs, the phase
fit and the carry are 70's.*

## It is verified two ways before it is used on a receipt

**REPRODUCTION.** The mean reading returns `r7637+70`'s own-comb row on the arm of record **to every digit
that result prints** — `+0.0295 +0.0595 +0.0610 +0.0639 +0.0777 +0.0728 +0.0795`, step `−0.0396`, rise
`+0.0061` — from an independent implementation. *An instrument that runs is not an instrument that measures;
this one is checked against a number computed elsewhere before it is trusted.*

**REDUCTION.** With `T_a = T_c` and `Δφ = 0` the carry must **be** the shared statistic. Fed the control
against itself, all four readings return every band at zero: `0.0`, `2.2e-16`, `2.2e-16`, `0.0` — floating
point, not a difference. That is 70's own invariant, now checked for the three kinds they did not cover.

## And the own comb restores the smooth pattern in EVERY kind, not just the mean

| reading | arm of record, carried | ratio-step | 70-step | rise |
|---|---|---|---|---|
| mean | `+0.0295 +0.0595 +0.0610 +0.0639 +0.0777 +0.0728 +0.0795` | `0.427` | `−0.0396` | `+0.0061` |
| median | `+0.0521 +0.0563 +0.0658 +0.1107 +0.1089 +0.1081 +0.1927` | `0.486` | `−0.0550` | `+0.0329` |
| savgol | `+0.0464 +0.0454 +0.0646 +0.0766 +0.0753 +0.0737 +0.0904` | `0.654` | `−0.0246` | `+0.0103` |
| no envelope | `−0.0024 +0.0602 +0.0669 +0.0508 +0.0539 +0.1235 +0.0554` | `−0.035` | — | — |

Combs: control `T 1.0090, φ 1.441`; arm `T 1.0045, φ 1.450`; `Δφ +0.0083`.

**The alternation is gone in all three envelope kinds.** On the *shared* statistic on the arm of record the
savgol reading has a **negative** band 6 (`−0.0075`) and the mean reading drops to `+0.0141` there; carried,
those become `+0.0737` and `+0.0728`. *So 69's ruling — that the alternation was the beat — holds on three
envelope kinds, where 70 measured it on one.*

## What the step receipt's own assertions do on the arm of record

| its assertion | namesake | arm of record, carried |
|---|---|---|
| `max(ratio-step) < 0.7` over all four readings | `0.633` | **`0.654`** — passes, margin narrowed |
| envelope-free band 1, `|·| < 0.01` | `−0.0017` | **`−0.0024`** — passes |
| envelope-free bands 2–7 mean, `> 0.04` | `+0.0654` | **`+0.0685`** — passes |

⚠ **The `0.7` gate is the one to watch**: the savgol reading moves from `0.633` to `0.654`, so the margin
falls from `0.067` to `0.046`. It passes, and it passes on the reading the ruling says is the right one, but
it is the narrowest margin in the family and is recorded as such rather than left to be rediscovered.

---

# SET A, TRIAGED AGAINST ⑴'s RULE BEFORE ANYTHING IS EDITED

⑴ couples a receipt to the figure P15 prints from it, so the order of work on Set A is set by which
receipts are coupled at all. **23 in Set A. 2 are blocked by a bank gap** (`the_combs_resolution_…` and
`the_visibilitys_clock_…`, on `r6919_injected_cr` / `r6925_visleaf_cr` / `r6929_scan_cr` /
`r6893_switch_screen_cr`). Of the remaining 21:

| | count | what it means for the work |
|---|---|---|
| **not cited in P15 at all** | **2** | re-pointable with no paper coupling whatsoever |
| **cited, no number anywhere in the paragraph** | **12** | re-pointable without touching a figure |
| **cited in a paragraph that prints a number** | **7** | the sentence is read before anything is edited |

**The two uncited are `the_coupling_is_measured_and_negative_…` and `the_step_is_the_excesss_own_…`.**
⇒ *The step receipt — the one the whole own-comb question was diagnosed on — prints nothing in P15.* So it
is the right first re-point: the full ⑴ loop can be run on it with no paper coupling to resolve.

**Six of the seven number-printing cases are flagged by one line**, `l.2783`, an omnibus with **14**
`\rcpt{}`s and 4 printed numbers. So one reading of that line settles six of the seven; the seventh
(`the_term_mix_does_not_carry_the_modulation_…`) also sits beside `l.1548-1555`, which prints one number.

## ⌗ And the first version of this triage was line-level, which UNDERCOUNTS

Counting numbers on the `\rcpt{}`'s own **line** gave 7 of 20 cited receipts as figure-printing. That is
wrong in the unsafe direction: a sentence's printed figure routinely sits two or three source lines above
the citation that pins it, so a line-level count misses it. *It is the same error as the template-regex gap
sweep, which is why the count above is taken over the **paragraph** — which over-flags and never
under-flags, and the over-flagged cases are read by hand rather than acted on.*
