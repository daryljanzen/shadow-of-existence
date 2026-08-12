# F06 — P16's displayed abundance equation cites the one receipt that does not produce it, and the rate-library spread is twice the theory error it is said to sit inside

*status: BOUNDED NEGATIVE (verified at source, this cut). Every number below re-derived from the receipts' own printed output.*
*scope: `corpus/cosmogenesis_paper.tex` §sec:network eq. at lines 566–574; `receipts/P16_cosmogenesis_paper/P16_theory_error_and_likelihood.py`; `receipts/P16_cosmogenesis_paper/P16_validate_bbn.py`.*
*found by: a prototype gate that runs every receipt and checks the numbers quoted beside each `\rcpt{}` against that receipt's own output — 15 flags across ~250 citations, of which this is the one that survived triage.*

---

## A. The pointer

P16 §sec:network displays the headline result:

> Y_p = 0.247 (obs 0.245), D/H = 2.51×10⁻⁵ (obs 2.53×10⁻⁵),
> ³He/H = 1.05×10⁻⁵, ⁷Li/H = 5.1×10⁻¹⁰ (obs 1.6×10⁻¹⁰),
>
> *these being the values a genuine multi-nuclide network`\rcpt{P16_validate_bbn}` returns when
> integrated explicitly on the cooling history … **not read off the standard-BBN correspondence
> alone**.*

`P16_validate_bbn.py`, run at this cut, prints:

```
D1 VALIDATION GATE  (network = REACLIB rates + thermal n<->p, standard cooling)
[2] ABUNDANCES at eta10=6.14 (CMB-inherited):
               CR network      std BBN          obs   net/std
    Y_p        2.4322e-01   2.4700e-01   2.4500e-01     0.985
    D/H        2.5671e-05   2.5100e-05   2.5300e-05     1.023
    3He/H      1.0439e-05   1.0400e-05   1.1000e-05     1.004
    7Li/H      4.4611e-10   5.0000e-10   1.6000e-10     0.892
```

The cited receipt's **computed** column is 2.5671e-5 and 4.4611e-10. The paper's displayed values
are 2.51e-5 and 5.1e-10 — which sit in that table's **`std BBN` reference column**, in a sentence
whose entire point is that they are *not* read off the standard-BBN correspondence. Read alone,
the citation makes the paper look like it quoted its own reference column.

**It did not, and the corpus is clean on the physics.** `P16_theory_error_and_likelihood.py` runs
the same network on the *other* library and prints:

```
[X] RATE-LIBRARY CROSS-CHECK at eta10=6.13:
    StarLib : D/H=2.505e-05  7Li/H=5.127e-10   (evaluated light-nuclide rates)
    REACLIB : D/H=2.574e-05  7Li/H=4.446e-10   (independent compilation)
[B] COMPUTED at eta10=6.13 (Planck):  Y_p=0.2432 (Born) / 0.2471 (+QED corr)
    D/H=2.505e-05   3He/H=1.048e-05   7Li/H=5.127e-10
```

**All four displayed numbers are produced exactly, by that receipt, at StarLib** — 0.2471 → 0.247,
2.505e-5 → 2.51e-5, 1.048e-5 → 1.05e-5, 5.127e-10 → 5.1e-10. The paper even says so one sentence
later (*"the evaluated light-nuclide set (StarLib, quoted)"*), and the receipt appendix carries
the note *"StarLib headline quoted, REACLIB=code"*.

So this is a **pointer defect, not a numbers defect**: the equation cites the sibling receipt.
The fix is one label — cite `P16_theory_error_and_likelihood`, or cite both with the library named.

`check_receipts` cannot see it: the citation resolves to an INDEX row and a file on disk, which
is exactly what that gate checks. Nothing in the suite asks whether the cited receipt *produces
the number standing next to it*.

## B. The spread, and it is bigger than the budget it is filed under

Same receipt, two blocks apart:

```
[A] THEORY-ERROR BUDGET (fractional):  D/H : 1.1%   3He/H : 2.5%   7Li/H : 6.6%   Y_p : 0.6%
[X] ... spread  : D/H 2.8%  -- within the theory-error budget above
```

Recomputed from the receipt's own printed values:

| | StarLib | REACLIB | spread | budget | spread ÷ budget |
|---|---|---|---|---|---|
| D/H | 2.5050e-5 | 2.5740e-5 | **2.8 %** | 1.1 % | **2.50 ×** |
| ⁷Li/H | 5.1270e-10 | 4.4460e-10 | **13.3 %** | 6.6 % | **2.01 ×** |

The 2.8 % D/H spread is **not** within the 1.1 % D/H budget — it is two and a half times it. And
the ⁷Li spread, which the receipt does not report at all and the paper does not mention, is 13.3 %
against a 6.6 % budget: the same factor of two, on the abundance the paper's one open edge lives on.

The paper's prose carries the D/H half at half size (*"an independent compilation gives D/H 2 %
higher — a spread inside the propagated nuclear-rate theory error"*) and is silent on lithium.

## C. What it costs, computed rather than asserted

Re-running the receipt's own likelihood arithmetic on both libraries (my reproduction returns
−0.54σ and +7.80σ on StarLib, against the receipt's printed −0.5σ and +7.8σ, so the method is
matched):

| | library | computed | σ_theory | σ_obs | tension |
|---|---|---|---|---|---|
| D/H | StarLib | 2.5050e-5 | 2.755e-7 | 3.00e-7 | **−0.54 σ** |
| D/H | REACLIB | 2.5740e-5 | 2.831e-7 | 3.00e-7 | **+1.14 σ** |
| ⁷Li/H | StarLib | 5.1270e-10 | 3.384e-11 | 3.00e-11 | **+7.80 σ** |
| ⁷Li/H | REACLIB | 4.4460e-10 | 2.934e-11 | 3.00e-11 | **+6.78 σ** |

Two consequences, and they pull opposite ways:

**The lithium claim is already right and the paper got it right for the right reason.** P16 states
the tension as **6–8 σ**, and the two libraries give 6.8 and 7.8 — the range is a range because
the library spread is real, and the paper's phrasing already spans it. Nothing to fix.

**The concordance claim is stated one notch tighter than the libraries support.** The receipt's
verdict reads *"D/H and Y_p CONCORDANT (<1 sigma)"*. On REACLIB, D/H is +1.14 σ. The *concordance*
is untouched — both are comfortably inside 2 σ and the joint fit at one inherited η stands — but
the parenthetical **"<1 σ"** is a StarLib-only statement presented as the result.

That is a small correction and it makes the claim more robust, not less: *D/H and Y_p land within
about a sigma of the measured primordial values on either published rate library* is both true and
stronger than a number that moves when the library does.

## Recommended, and stated for reversal

1. Repoint the equation's `\rcpt` to `P16_theory_error_and_likelihood` (or cite both, naming the
   library on each). One label.
2. In `P16_theory_error_and_likelihood.py`, fix the `[X]` block's own sentence — the 2.8 % D/H
   spread is 2.5× the 1.1 % budget printed in `[A]`, not inside it — and report the ⁷Li spread,
   which is the larger of the two and currently unstated.
3. Soften the receipt's `<1 sigma` verdict to the library-robust form, and add the ⁷Li spread to
   the paper's library sentence. The 6–8 σ range already covers it; the sentence just doesn't say
   why the range is a range, and it turns out to have a good reason.

## The gate this wants

Fourth member of the family F01/F03/F04 named: **each gate models a document as its text, and the
defect lives in what the document depends on.** `check_receipts` checks that a citation *resolves*.
Nothing checks that the cited receipt *computes the number beside it*.

`DRAFT_check_numbers_at_citations.py` is the prototype that found this: run every receipt once,
cache stdout, then for each `\rcpt{}` in the papers pull the numeric literals from the preceding
prose and check each against the receipt's output *at the quoted precision and at any power of
ten* (so 5.7 matches 5.68e-14 and 145.7 matches 145.72 Mpc). Across ~250 citations it flags **15**;
triaged, fourteen are context bleed from an adjacent sentence or a number the receipt takes as
input, and this is the one that is real. That hit rate is too noisy to run as a failing gate today
— it wants a way to bound the prose window to the sentence rather than a character count — so it
is offered as a **reporting** tool, with the honest note that a 1-in-15 signal is still worth one
pass per major revision.

## Not claimed

- No physics is wrong. Every displayed number is produced by a receipt in the tree, at the library
  the prose names.
- No claim that REACLIB is the right library or that StarLib is. The paper's choice
  (*"the evaluated light-nuclide set … quoted"*) is defensible and stated; the finding is that the
  spread between them is larger than the budget it is filed under.
- The lithium verdict is untouched, and the ⁷Li line is the part of the paper that already handles
  the library spread correctly.
- No closure on any registered item.
