# r7639+cc66 ⑵ — every P15 sentence that cites the DPSRC pair, and what carries it

The two receipts are `P15_the_model_difference_is_an_acoustic_contrast_difference_and_it_is_not_one_skys_luck`
and `P15_the_source_decomposition_is_reachable_on_the_reporting_path_and_the_neutrinos_have_a_knob`. The
`DPSRC=0` bit-identity in each is now **pinned to the `LEAFREC=0` namesakes** by an explicit `NAMESAKE`
constant that does not move with the receipt's live base, guarded by a check of its own, and named as
history in a docstring. Line numbers are `corpus/CR_cosmology.tex` at `r7639`. Classed as `70` classed the
c54 family (`r7637_70_own_comb_statistic/C54_P15_SENTENCES.md`):

- **INSTRUMENT**: the claim is about that superseded instrument. It leaves P15 or is restated as history.
- **CONSTRUCTION**: the claim is about the construction. It is carried by the arm-of-record figure named below.

---

## 0. The bit-identity itself — **INSTRUMENT, and it is in NO P15 sentence.**

**Measured, not assumed.** `CR_cosmology.tex` contains no occurrence of `bit-identical`, `unwired`, `DPSRC`
or `not a null`, and the three sentences that cite either receipt (below) cite them for other claims. So:

- **Nothing leaves P15 and nothing is restated there.** The finding lives in the two receipts, in
  `FOR_66.md` (`cc66.36`), and in `receipts/INDEX.md` row 908 as a *quotation* of `cc66.36`.
- **It is restated as history where it does live** — both receipts now say that it is a measurement of the
  instrument *before* `_SWSRC`/`_DPSRC` were wired into `_project` at `r6889+cc66.36` (`736f9399`), and
  both pin it to the spectra that instrument made.
- ⌗ *Why the pin matters rather than being decoration*, in `max |dD_l|` — this receipt's own statistic:

  | comparison | `max |dD_l|` |
  |---|---|
  | `r6885_dp0_{lcdm,cr}` against the **namesake** base | **`0.000000e+00`** on both legs — the bit-identity |
  | `r6885_dp0_cr` against the **arm-of-record** base (what a per-arm re-point produces) | `2.529416e-02` — a cross-arm read, which measures nothing |
  | `r6885_dp0_cr_leafrec1` against the **arm-of-record** base (both legs honest) | `9.466893e-02` — the knob **is** wired there |

  So letting the comparison follow a re-pointed base would read as *a repair having failed* where what it
  records is *a repair having succeeded* — and it would read that way **green**, which is the silent class
  reported at `r7637+cc66.1`. ⚠ *And note the third row: `r6885_dp0_cr_leafrec1` exists, so the pair IS
  reachable on the arm of record. What is not reachable there is the bit-identity, because on that arm there
  is nothing bit-identical to measure — which is why ⑵ pins it rather than moving it.*

---

## 1. l.1123, `model_difference` (co-cited with `monopole_zero_point`).

> "This arm's acoustic oscillation is $1.040$ times the control's about its own envelope, and one direction
> built from the control alone---raise the oscillation at fixed envelope, with nothing fitted---carries half
> of $\lVert\Delta\rVert^{2}$."

- **Type:** CONSTRUCTION, both halves.
- **Carried by:** the `$1.040$` is `monopole_zero_point`'s and on the arm of record it is **`1.04403`**
  (measured at `r7639+cc66.1`, `rc=0`, 22 PASS, pinned to `4e-4`). The `‖Δ‖²` half is `model_difference`'s
  and **cannot be carried yet**: its four `r6885` CAND knob pairs have no arm-of-record counterpart.
- **Status:** reported at `r7639+cc66.1` with a proposed split, so each figure sits beside the receipt that
  pins it. `69`'s to land. *This is the sentence that found the structural cap: one printed figure beside two
  `\rcpt{}`s is two sites in `check_figures_pinned`'s key, and only one receipt can pin it.*

## 2. l.1147, `model_difference`.

> "And the three features this arm's residual shows and the control's does not are all $\Delta$'s: the
> peak-and-trough asymmetry, the $\ell\simeq1000$ trough where $\Delta$ carries $-1.074$ of the arm's
> $-1.177$ in fifteen bins, and the growth with multipole---which $\Delta$ does monotonically where neither
> residual does."

- **Type:** CONSTRUCTION. The claim is that the three features are properties of $\Delta$, the
  construction's own model difference, and not of either residual.
- **Carried by:** the same receipt on the arm of record, **once the four CAND pairs are banked**. The
  `$-1.074$` of `$-1.177$` are its own figures and move with the arm.
- **Status:** HELD, on `r6885_{ln24,noisw,dre0,drc0}_cr` (and their `_lcdm` legs). *Not held on the
  bit-identity:* ⑵'s pin makes part (b) immovable by construction, so it is no longer a reason this receipt
  cannot be re-pointed. **The knob pairs are the whole of the remaining block.**

## 3. l.1153, `source_decomposition`.

> "The channel is identified and the cause is not: the contrast direction is the balance between the
> monopole and the Doppler terms of the source, bracketed with opposite signs by removing each and
> re-projecting, on both instrument paths and with the same signs on both; and neither deletion returns the
> two arms to a common contrast, so what the bracket locates is where the difference enters rather than what
> produces it."

- **Type:** CONSTRUCTION. It is a statement about the construction's source decomposition — which channel
  carries the contrast — and the method by which the bracket is drawn.
- **Carried by:** the same receipt on the arm of record, **once `r6889_hdp0_cr` and `r6889_hsw0_cr` are
  banked**. `r6889_nufs0_cr_leafrec1` already exists; the other two legs of the bracket do not, and the
  bracket is exactly those two deletions.
- **Status:** HELD, on two spectra. ⌗ *"on both instrument paths" is the clause the `r6885` LOS pairs serve,
  and `r6885_{los,losdp0,lossw0}_cr_leafrec1` all exist — so the second path is already reachable. It is the
  hierarchy path's two deletions that are missing.*

---

## What ⑵ changes about the holds

| receipt | before ⑵ | after ⑵ |
|---|---|---|
| `model_difference` | held on the DPSRC substitution **and** four unbanked knob pairs | held on the **four knob pairs only** |
| `source_decomposition` | held on the DPSRC substitution **and** `r6889_{noop,hdp0,hsw0}` | held on the **three `r6889` spectra only** |

**The DPSRC substitution is no longer a hold on either receipt.** It was a hold because re-pointing the base
would have moved a historical comparison; pinning it to the namesakes removes that, and it removes it in a
way that cannot be undone by a later re-point, because the pin is a guarded constant and not a convention.
