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
