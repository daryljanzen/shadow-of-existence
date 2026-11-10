# `r7733+cc66` — THE `P15` SENTENCE, AND WHY IT DOES NOT CONTRADICT WHAT IS ALREADY PRINTED

Order `r7733` item ②.  The drafted sentence is in §3.  §1 is the apparent contradiction stated
plainly, §2 is the measurement that resolves it, §4 is what `69` needs in order to land it, §5 is
item ③'s one line on `PO-87`.

---

## ① THE APPARENT CONTRADICTION, STATED WITHOUT SOFTENING IT

`P15`'s step paragraph prints, at `corpus/CR_cosmology.tex` l.1404:

> *And the located transition belongs to the contrast between the arms and not to their sources*:
> read in the same sliding windows, the ratio of this arm's spectrum to the control's carries the
> transition, while the same reading of the two arms' `$\eta$`-integrated sources returns a ratio
> near zero throughout […]

And `r7731`'s verdict says both the kernel difference **and the source difference** contribute to the
located step **at unit amplitude**.  ⇒ Read carelessly, the second says the sources carry the step and
the first says they do not.

## ② WHY IT IS NOT A CONTRADICTION — TWO DISTINCTIONS, AND THE SECOND IS MEASURED

**⒜ The two sentences are about DIFFERENT OBJECTS, and this half is definitional, not measured.**
`P15`'s exclusion is about the **ratio of the two arms' `$\eta$`-integrated sources**, read in sliding
windows: a one-dimensional object in wavenumber, taken *before* the projection.  `r7731`'s `a_src` is
the coefficient on the **source difference after the Bessel projection**, on the `$(\ell,k)$` plane.
⇒ A quantity can be flat before projection and enter the projected swap at full weight, because the
projection is not a rescaling.  *So the first distinction alone already removes the contradiction.*

⛔ **But it removes it by saying the two statements never meet, which a reader is entitled to find
unsatisfying** — it leaves open whether, had `P15` asked its question on the projected plane, the
answer would have gone the other way.  So the second distinction is the one that does the work.

**⒝ "Unit amplitude" is a statement about the COEFFICIENT, not about the share of the LOCATED step —
and that is measured, in `structure.py`, pinned in the receipt.**

A located transition is a feature **at an `$\ell$`**.  A template that is *constant in `$\ell$`*
cannot make one, however large it is: it moves every multipole by the same factor.  Split each
template against the fit's own weighted norm into its `$k$`-only part (its weighted mean over
`$\ell$`) and the remainder:

| | kernel template | source template |
|---|---|---|
| rms, primary binning | `0.21883` | **`0.27808`** — the source template is the LARGER |
| `$\ell$`-structured fraction, primary | **`97.93 %`** | **`22.39 %`** |
| `$\ell$`-structured fraction, secondary | `97.98 %` | `21.09 %` |
| share of the fitted model's `$\ell$`-structured variance, primary | **`93.6 %`** | `7.8 %` (cross `−1.4 %`) |
| …secondary | `93.0 %` | `12.7 %` (cross `−5.7 %`) |
| the kernel's `$\ell$`-structure, in rms | `3.46×` the source's (primary), `2.71×` (secondary) | |

⇒ *** The source difference enters the exchange at full weight, and more than three quarters of what
it contributes is a featureless rescaling across wavenumber.  Of the part that can place a feature at
a located multipole, the kernel contrast carries about nineteen twentieths. ***

⛭ **AND THIS LANDS ON A DISTINCTION THE PARAGRAPH ALREADY DRAWS.**  Two sentences later `P15` prints
*"The step's size, by contrast, is in both arms: what only the contrast resolves is where the step
falls and how sharp it is."*  ⇒ The new result is that same split one level down — **weight in the
exchange is shared; the location is the contrast's.**  *The sentence therefore refines a distinction
already in print rather than qualifying one.*

⛔ **MY OWN EXPECTATION GOING IN WAS WRONG, IN THE OPPOSITE DIRECTION**, and it is recorded in
`structure.py`'s own head: I expected the source template to be *small*, so that unit amplitude on it
would be unit amplitude on a small thing.  It is the **larger** of the two.  The resolution is shape
and not size, and had I drafted from the expectation the sentence would have been false.

⚠ **The split is not unique.**  "Constant in `$\ell$`" is one choice of featureless direction and a
different one would apportion differently.  It is the choice the printed sentence is about: the
transition is **located**, at an `$\ell$`, and a template flat in `$\ell$` is exactly what cannot
locate one.

---

## ③ THE DRAFTED SENTENCE

To sit **immediately after** the printed source-exclusion clause at l.1404 and **before** *"The step's
size, by contrast, is in both arms"*:

> \emph{And that exclusion is about the sources' own ratio, not about their difference once it is
> projected}: read on the $(\ell,k)$ plane that the projection actually builds, the exchange of
> kernels and the exchange of sources each enter the full swap at unit amplitude---$1.0076$ and
> $1.0035$, each beyond its own null interval under two null constructions and two binnings---so the
> source difference is not absent from the step. \emph{But only one of the two is structured in
> multipole}: $97.93$ per cent of the kernel template varies with $\ell$ against $22.39$ per cent of
> the source template, the rest of which is a featureless rescaling across wavenumber; so of the
> $\ell$-varying variance, which is the only part that can place a feature at a located multipole,
> the kernel exchange carries $93.6$ per cent\rcpt{P15_both_mechanisms_contribute_at_unit_amplitude_and_the_located_step_is_the_kernels_because_the_source_template_is_flat_in_ell}.

⇒ And then the printed *"The step's size, by contrast, is in both arms"* follows as the same
distinction in the paper's own existing words, which is why no further clause is needed.

### ⛔ WHAT THE SENTENCE DELIBERATELY DOES NOT SAY

* not *"the source difference carries the step"* — it carries **weight in the exchange**;
* not *"the swap is exhausted by these two mechanisms"* — the residual is about four per cent of the
  signal rms on the model's own object, and the receipt measures it rather than asserting it away;
* not that the two amplitudes are **equally determined** — `a_src`'s null interval is `8.6` times
  `a_ker`'s, so the sentence prints both figures and claims exclusion, not equal precision;
* not a word about the **sources' own ratio**, whose exclusion `r7721`'s receipt pins and which this
  sentence explicitly sets aside rather than re-litigating.

---

## ④ WHAT `69` NEEDS TO LAND IT

1. **Every figure in the drafted sentence is pinned two-sidedly by the new receipt**, so
   `check_figures_pinned` takes it with **no baseline entry**: `1.0076` and `1.0035` (gate ⓵),
   `97.93` and `22.39` (gate ⓸), `93.6` (gate ⓹).  *If the wording is changed, keep those five
   figures at those digits or the gate will want re-reading.*
   > ⛔ **AND THE FIRST FORM OF THIS CLAIM WAS FALSE, which the gate caught and I did not.**  The
   > receipt pinned the three percentages as **fractions** (`0.97933`, `0.223855`, `0.935623`) while
   > the sentence and the INDEX row print them as **per cent** — and `check_figures_pinned` reads
   > `97.93` as ninety-seven, not as `0.9793`, so a pin on the fraction pins nothing that is printed.
   > It flagged all four percentage figures as UNPINNED and the baseline would have risen by four.
   > ⇒ The receipt now carries the same four comparisons **in per cent as well**.  *The lesson is the
   > session's own recurring one in miniature: a pin on one object is not a pin on another, and
   > "pinned" has to mean pinned in the unit the paper prints.*
2. The `\rcpt{}` marker is `69`'s to place; the receipt's INDEX row is in, with its `sec:refit-bound`
   / step-paragraph anchor.
3. ⛔ **One correction `69` should carry before printing anything built on `0.46`** — see the receipt's
   gate ⓷ and this seat's reply at `FOR_66.md`.  `r7731`'s `0.4642` is the **unbinned, equal-weight**
   residual ratio; the model is fitted **binned and weighted**, where the ratio is `0.0444`.  The
   licence *"not exhausted by these two"* survives; *"INCOMPLETE, not merely imperfect"* does not, and
   nothing printed in `P15` should rest on the `46 %`.

## ⑤ `PO-87` — ITEM ③, IN ONE LINE

**It does not close with this sentence: one step remains, and it is the row's own live clause —** the
verdict names *which contrast* carries the located step's `$\ell$`-structure (the projection's, at
`93.6 %`) but **not which term of the projection's acceptance does it**, which is what `r7499` left
live and what `PO-87` asks for; the kernel template is still one object here, and splitting it into
the acceptance's named terms is the step.
