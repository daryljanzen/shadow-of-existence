# r7843+cc66.1 — P18 §10's counts, measured with a stated convention

**Order:** 69's `r7843`. ① state the counting convention each sentence means, read off the
sentence and its section; ② count it live with a receipt that measures as it runs; ③ print the
measured figures with the convention named, cite the receipt, pin each at the printed precision.

**Receipt:** `receipts/P18_CR_synthesis/P18_section_tens_counts_measured_four_hold_under_the_papers_own_convention_and_two_have_no_enumerable_subject.py`
— 29 arms, all pass.

---

## ⛭ THE HEADLINE, AND IT IS NOT WHAT `r7841+cc66.1` EXPECTED

**Four of the six counts are RIGHT. Two of them are exactly right.**

`r7841+cc66.1` reported this cluster as unfixable and, in doing so, called it *understated* —
by analogy with the receipts figure it had just corrected from "several hundred" to a live
1202. **That analogy was wrong, and this revision records it as wrong.** The counts were not
stale; they were *unsourced*. Those are different defects, and only the second one was real.

| the count | convention | live | verdict |
|---|---|---|---|
| "some two hundred environments" | formal environments the papers declare with `\newtheorem` and use | **202** | **right** |
| "fourteen named theorems" | `theorem` environments, named = amsthm's bracketed title | **14** | **exactly right** |
| "on six axioms" | `axiom` environments | **6** | **exactly right** |
| "over twelve hundred receipts" | receipt files / INDEX rows | **1204 / 1208** | right, as set at `r7841` |
| "roughly seventy-five results carrying a hard register" | register-tag census, register *leads with* one of the five | **78** | **right** |
| "nine structural recoveries" | — | — | ⛔ **no enumerable subject** |
| "forty-four proved classical-geometry identities" | — | — | ⛔ **no enumerable subject** |

## The conventions are the paper's own, and two of them are provable from provenance

This matters because a convention I *chose* would be an imposition dressed as a measurement.

- **The environments.** The retired document that carried this whole cluster says *"**196
  formal environments.** Fourteen named theorems and six axioms"* — in one breath, which is
  this exact measurement when it was written. Live 202, so **+6 of accretion**. The convention
  is confirmed by its own provenance rather than by my choosing it.
- **The hard register.** `SYNTHESIS_HARVEST.md` — which the figure's own entry names as its
  source (*"② REGISTER — COUNT, from the Phase 3 gather and the register-tag census"*) —
  printed *"thirteen rows against roughly **seventy-four** hard-tagged results"* when it minted
  the figure. Live 78.
- **The theorems and axioms** need no provenance argument: the figures are exact, all 14
  theorems carry a bracketed name with **zero** unnamed, and all 6 axioms sit in one paper, so
  "six axioms" names a single axiom set rather than a sum.

## ⛔ The registered negative fired twice, and both are recorded

The pre-registration required each count to be computed under a **competing** convention too,
with the rule that *a competing convention landing on the paper's printed figure is evidence
the paper's convention was the competing one and mine is the imposition.*

1. **The environments.** Dropping `remark` as "not claim-bearing" — **the reading I would have
   chosen**, and the one my own registered governing reading pointed at — gives **118**, barely
   half of "some two hundred". **So the paper counts remarks, and my instinct was wrong.**
2. **The hard register.** Requiring the tag to be *exactly* one of the five gives **56**, not
   "roughly seventy-five". **So the paper's reading is the leading-word one** — allowing
   "Propositions, proved", "Theorem and corollary", "Receipt-anchored computation" — **and the
   strict reading is mine.**

I registered that I would report this even where it cost me the finding. It cost me the finding
twice.

## ⛔⛔ Two counts have no enumerable subject — reported, not invented

**"Nine structural recoveries"** and **"forty-four proved classical-geometry identities"**.

Searched: every one of the 36 ledgers, `THE_REGISTER`, `CORPUS_MAP`, `THE_WEAVE`, `THE_PLAN`,
the harvest, and the papers. `structural recover*` occurs only as prose, one or two to a file,
never as a list. `identity/identities` occurs **148 times across 36 ledgers** as prose mentions
with **no entry-level tag** a convention could count. **P18 itself names five exemplars of the
recoveries and calls them *"an illustration of the class and not the case"*** — which is a hand
count of an unregistered class.

The one numeric near-miss was **chased and rejected**: `FOR_69.md` carries *"44 of 44
bit-identical"*, which is the `r6925_geometry` bank's arm keys — a coincidence of the number.

⇒ **The registered bound predicted exactly this** — *"at least one of the five cannot be
measured without inventing its subject"* — **and it is two.** Both phrases are left exactly as
printed and carry no convention phrase, because inventing one is the thing this revision argues
against.

## What P18 gained

Not a new number — the figures were right. It gained the **convention** and the **citation**:

- `sec:displace` → *"a formal spine of some two hundred environments —**the formal environments
  the papers declare and use, remarks included**— with fourteen named theorems on six axioms,
  **each the bracketed title of a `theorem` and an `axiom` environment**"* + `\rcpt`
- `sec:frontier` → *"...receipt-anchored, **counted off the register-tag census on the results
  whose register leads with one of those five**"* + `\rcpt`

## ⌗ A structural change for 69 to confirm or reverse

**P18 now carries its first receipts appendix.** It had none by design — `r7841+cc66.1`
established that 0 `\rcpt` sites against 343 `\cite` sites is *why* the chain is P18 → companion
→ receipt — and both `make_all_appendices` and `check_appendix_current` stopped at P17 for that
reason.

But **a figure is pinned in this corpus by a `\rcpt` site that `check_figures_pinned` can
read** (its own site definition: *"every `\rcpt{X}` in a non-appendix paper"*), so an order to
*pin* these counts cannot be met without one. Both ranges go 17 → 18 with the reason recorded
beside them, `appendix_receipts_P18.tex` is generated (4 receipts), and `CR_synthesis.tex`
`\input`s it beside the ledger appendix it already had. **Reversible:** drop the ranges back and
remove the `\input`.

## Node 60 raised this, and declined to patch it

At `r7748` node 60 found this figure standing on no receipt and wrote: *"No patch pressed: **a
count of the hard register is a judgement about which results carry it, and that is yours to
define before it can be receipted.**"* This revision is that definition, and **60's reading is
confirmed**: the figure stood on a census nobody cited. 60 also noted the numerator moving
4 → 3; it has since moved to 2 while the denominator never moved — and now the denominator is
measured and the convention named.

## Prediction score

| | prediction | outcome |
|---|---|---|
| ① | all four unstated counts stale **LOW** | ⛔ **MISSED** — three are right, two exactly |
| ② | `nine recoveries` band 9–20 | **not engaged** — unmeasurable |
| ③ | `two hundred environments` band 250–290 | ⛔ **MISSED** — 202 under the paper's convention |
| ④ | theorems **above** 14, axioms exactly 6 | **split** — axioms exactly 6 ✓, theorems exactly 14 ✗ |
| ⑤ | `twelve hundred receipts` still correct | **HIT** |
| ⑥ | `forty-four identities` band 44–80 | **not engaged** — unmeasurable |
| ⑦ | `seventy-five results` band 75–200 | **HIT** at the bottom — 78 |
| **the bound** | at least one count unmeasurable without inventing its subject | **HIT, and it is two** |

**The scoring is mostly misses, and the misses are the result.** I predicted staleness and
found soundness. My `r7841` measurement of "263 spine environments" — which fed prediction ③ —
was counting **Lean declarations**, a different object entirely from the LaTeX environments the
sentence means; the live Lean spine is 410 declarations outside the vendored probes, and 50,054
inside them. **Having a number is not having the right number**, and the number I carried
forward from my own previous revision was the wrong object.
