---
name: numerical-analysis-ledger
kind: FIELD-BAKE
current: r3616
job: The numerical-analysis field-bake ledger — what bit, what bounced, and where the boundary is. The one field whose target was the receipts rather than the prose.
sources: [chat]
---

# THE NUMERICAL ANALYSIS LEDGER — the field aimed at the computational layer, not the papers

> **▣ THE ORDER SAID SO IN ADVANCE AND IT WAS RIGHT.** *"Screen `convergence`; causal convergence
> dominates. **This field's real target is the corpus's computational receipts, not its prose.**"*
> ⇒ *The prose side returned essentially nothing, as predicted. **The receipts side returned the
> only quantitative audit of the corpus's numerics that has ever been run on it.***

---

## ⛭ R0 — THE BASELINE, BOTH SIDES

### ⛔ THE PROSE SIDE: THE FIELD'S VOCABULARY IS ABSENT AND ITS FOOTPRINT IS FOUR HOMONYMS

| term | count | what it actually is |
|---|---|---|
| `resolution` | ×39 | ⛔ **resolving a problem** — *"the resolution of the Hubble tension"*, *"a device that permits a resolution"*, *"the per-root resolution of a square root"*. ⌗ *Two of `P15`'s nine are genuine **measurement** resolution — "not a resolution effect", "equal to the resolution at which they are read" — and neither is grid resolution* |
| `truncation` | ×17 | **a one-hinge truncation** (a physical restriction), a **minisuperspace truncation**, a series truncation. *Not truncation error* |
| `convergence` | ×15 | ⛔ **epistemic** — *"the convergence of its several descriptions on one existent"*, *"four idioms converging"*. **The corpus's own word for its central method** |
| `stability` | ×12 | **future stability of de~Sitter** (Friedrich; Andréasson--Ringström), nonlinear PDE stability. *Not numerical stability* |
| `converge` | ×48 raw | **×9 word-bounded** — the rest inside *convergent*, *converges*, *convergence* |
| `discretisation` · `step size` · `stiff` · `tolerance` · `round-off` · `floating point` · `Runge` · `finite difference` · `interpolation` | | **all ×0** |

### ⛭⛭ THE RECEIPTS SIDE, WHICH IS WHERE THE FIELD ACTUALLY LIVES — 658 files measured

| what was counted | number |
|---|---|
| files integrating an ODE (`solve_ivp` / `odeint`) | **24** |
| ... **stating an explicit `rtol` and `atol`** | ⛭ **24 of 24 — not one relies on a solver default** |
| ... containing any convergence / refinement / Richardson language | ⛔ **4 of 24** |
| files with an `abs(...) < tol` assertion | 210 (×688) |
| files seeding a generator | 39 |
| files comparing a float to a literal with `==` | 12 (×20) — *read; all are exact-zero or loop-parameter comparisons* |

⇒ ***THE DISCIPLINE IS BETTER THAN MOST PUBLISHED COMPUTATIONAL WORK, and it is incomplete in one
specific way: the tolerances are STATED and almost never VERIFIED.***

---

## ⌗ THE PROBE REGISTER

| # | probe | verdict |
|---|---|---|
| **`Q1`** | *`rtol=1e-10` **asks** the solver for ten digits. **Does the corpus get them?*** | ⛭⛭ **CONFIRMED, BY RE-RUNNING — and the answer is yes.** *`scipy.integrate.solve_ivp` patched to run every call at **100× tighter** tolerance; four receipts re-run unmodified in subprocesses; **every one still passes its own assertions**.* ⇒ ***The unverified tolerances are honest ones: the corpus asked for more precision than it needed, which is the safe direction.*** **Control**: a deliberately under-resolved stiff integration through the same harness DOES move, so the patch applies and the comparator sees |
| **`Q2`** | *`P15` writes "validated against a Boltzmann reference … $\rs=144.0$ vs CAMB $144.4$". **Is that a validation?*** | ⛔⛭ **BITE — a validation without a stated criterion is two numbers side by side.** *Measured: the disagreement is $0.28\%$ and the signature it feeds is $8.2\%$, so ***the reference agrees to thirty times the effect***.* ⇒ **The margin, not the agreement, is what the word "validated" is carrying — and the sentence did not say it.** **LANDED** in `P15` with `\ldg{numerical_analysis}` |
| **`Q3`** | *`convergence` ×15, `stability` ×12, `truncation` ×17, `resolution` ×39 — is any of it numerical?* | ⛭ **SCORED — essentially none.** *Epistemic convergence, de~Sitter's future stability, a one-hinge truncation, resolving a tension.* ⌗ ***Four homonyms in one field, and unlike `bit` or `congruence` every one passes the word-boundary screen intact*** — they are real words used in full, in another sense |
| **`Q4`** | *float-equality comparisons — the classic defect* | ⛭ **SCORED — 20 sites in 12 files, and NONE is a defect.** *Read: exact zeros from `sympy` differentiation, loop parameters compared to the literals they were set from, and pinned figures. **The one that looked worst — array selection by `XS == 1.000` — indexes a grid built from those exact literals*** |
| **`Q5`** | *are the `abs(...) < tol` tolerances meaningful, or loose enough to pass anything?* | ⟐ **HELD — 688 sites in 210 files is beyond what this pass can read, and a sampling verdict would be a census that is not one.** *Recorded as the field's one open item, with the shape of the check it needs: **mutate the asserted quantity by the tolerance and require the assertion to fail***. `check_receipts`' hollow-assertion lint is the existing half of this |

---

## ⛭ THE REACH REGISTER — **17 of 17 on the prose side, 658 files on the receipts side**

| paper | verdict | what was read |
|---|---|---|
| **`P15`** | ⛭ **WORKED — the only paper with a numerical claim, and it owed the margin** | *The CAMB-comparison passage read in full.* **The corpus's one validation against a reference implementation**, and `Q2` names its margin. Its `resolution` ×9 splits between resolving a tension and instrumental resolution |
| **`P07`** | ⛭ **CHECKED-NEGATIVE — and it owns the biggest homonym** | `resolution` ×15 and `convergence` ×5, ***every one epistemic***: the framework's own word for several descriptions meeting on one object |
| **`P11`** | ⛭ **CHECKED-NEGATIVE** | `stability` ×5 is Friedrich's nonlinear stability of de~Sitter and cosmic no-hair — **a theorem, not a solver property** |
| **`P06`** | ⛭ **CHECKED-NEGATIVE** | `convergence` ×4, epistemic |
| **`P10`** · **`P14`** · **`P16`** · **`P03`** · **`p0`** | ⛭ **CHECKED-NEGATIVE, all five** | `truncation` in the minisuperspace and one-hinge senses; `P16`'s `convergence` ×2 is the nucleosynthesis network settling, which is **its own receipt's business and is checked there** |
| **`P01`** · **`P02`** · **`P04`** · **`P05`** · **`P08`** · **`P09`** · **`P12`** · **`P13`** | ⛭ **CHECKED-NEGATIVE, all eight** | *Screened on all eighteen field terms.* **No numerical-analysis content in any of them** |

⌗ ***AND THE RECEIPTS SIDE WAS READ AS A POPULATION, WHICH IS THE ONLY WAY 658 FILES CAN BE READ
HONESTLY***: every ODE call located and its tolerances extracted mechanically, every float-equality
site read individually, and four whole receipts re-run under a patched solver.

---

## ⛭⛭⛭ THE THREE REGISTERS

### ⌗ WHAT BIT — one, and one confirmation

| # | what the field found | where it landed |
|---|---|---|
| **`Q2`** | ***"validated" was carrying a margin it did not state*** — $0.28\%$ against an $8.2\%$ signature, adequate by thirty times | `P15`, `\ldg{numerical_analysis}` |
| **`Q1`** | ***CONFIRMATION, not a bite***: 24 of 24 ODE receipts state their tolerances, and on a re-run at 100× tighter every sampled conclusion survives unchanged | the receipt itself; no paper claims it |

### ⌗ WHAT BOUNCED — two, with their blind spots

| # | why it bounced | **what the test that killed it was blind to** |
|---|---|---|
| `Q3` | four homonyms, none numerical | ⛔ ***Every one PASSES the word-boundary screen.*** *`bit` and `congruence` were caught by counting properly; these cannot be. **A screen that measures spelling cannot see sense, and this field is where that stops being a caveat and becomes the whole answer.*** |
| `Q4` | the float comparisons are all sound | *A regex for `== <float>` finds the SHAPE of the defect and says nothing about whether the operands are exact. **Twenty hits, twenty reads, zero defects** — and the only way to know that was twenty reads.* |

### ⌗ THE BOUNDARY

***THE PAPERS CONTAIN NO NUMERICAL ANALYSIS AND THE RECEIPTS CONTAIN A GREAT DEAL OF IT, DONE WELL.***
*That asymmetry is the field's finding: the corpus's computational care lives entirely in a layer the
papers do not describe, and a field bake that read only the seventeen bodies would have reported this
field absent.*

⛔ ***WHAT THIS FIELD CANNOT REACH.*** *`Q5` — whether 688 `abs(...) < tol` assertions carry
meaningful tolerances. **That needs a mutation harness, not a reading**, and building one is a
larger instrument than a field bake should ship. Recorded with the shape of the check it wants.*

---

## ⌗ THE LEAD REGISTER · THE LANDING TABLE

| register | verdict | destination | state |
|---|---|---|---|
| `Q1` | **CONFIRMED** — the tolerances are honest | the receipts layer; no paper claims it | **LANDED** as a receipt |
| `Q2` | BITE — the unstated margin | `P15` `sec:diffusion-scale` | **LANDED** |
| `Q3` | BOUNCED — four homonyms that pass every screen | — | **CHECKED-NEGATIVE** |
| `Q4` | BOUNCED — twenty float comparisons, zero defects | — | **CHECKED-NEGATIVE** |
| `Q5` | ⟐ **HELD** — 688 tolerance assertions, unaudited | a mutation harness | **OPEN, with its check specified** |

⌗ ***DEPTH BESIDE COVERAGE.*** **Coverage: 17 of 17 papers by name, and 658 receipt files as a population.**
**Depth: 1 bite, 1 confirmation, 2 bounces, 1 held — sixteen of seventeen papers owed nothing.**
---

## ⛭⛭⛭ THE ESTIMATE FROM CONTENTS — **the step this bake SKIPPED, run at r3622**

> ⛔ ***`OVERNIGHT_FIELD_BAKE_WORK_ORDER.md` STEP 2 requires all seventeen ABSTRACTS read and rated
> HIGH/MEDIUM/LOW from what each paper is ABOUT, written into the ledger BEFORE any paper is worked.***
> *59 skipped it; I skipped it after them. **Skipping it is the whole failure: a field's term list is a
> list of what I already know the field to contain, so grepping it returns only that.** It cannot return
> the thing the field would see that the corpus has no word for.*
> ⌗ *Written here **after** the term-side pass rather than before it, which is the honest order to record
> and the wrong order to have worked in. **Where the estimate and the term pass disagree, the disagreement
> is kept in the table rather than resolved silently.***

| paper | estimate | reason, from subject matter — **not from counts** |
|---|---|---|
| **`P15`** | **HIGH** | *a full perturbation sector confronted with data — Boltzmann integration, a reference-code comparison, banked spectra* |
| **`P16`** | **HIGH** | *a nucleosynthesis network integrated to relic abundances; every number is computed* |
| **`P04`** | MEDIUM | *a floor computed from an integral over the path* |
| **`P11`** | MEDIUM | *a Cauchy problem and a propagating mode* |
| **`P14`** | MEDIUM | *a bound-state spectrum and a threshold* |
| **`P10`** | MEDIUM | *self-adjoint extensions and a spectral condition* |
| **`P03`** | MEDIUM | *angles and roots computed in closed form* |
| **`P09`** | LOW | *a range theorem* |
| **`P05`** | LOW | *a groupoid* |
| **`P02`** | LOW | *one curve* |
| **`P01`** | LOW | *a theorem* |
| **`P06`** | LOW | *epistemology* |
| **`P07`** | LOW | *synthesis* |
| **`P08`** | LOW | *an operator, derived not integrated* |
| **`P12`** | LOW | *an algebroid* |
| **`P13`** | LOW | *a boundary argument* |
| **`p0`** | LOW | *the substrate* |

⌗ **2 rated HIGH from contents.** *Scored against the term-side pass below.*

### ⛭ SCORING THE ESTIMATE AGAINST THE TERM-SIDE PASS

| | estimate | term-side verdict | outcome |
|---|---|---|---|
| `P15` | **HIGH** | WORKED — `Q2` landed | agreed |
| **`P16`** | **HIGH** | ⛔ **CHECKED-NEGATIVE** on the prose | ⚠ ***DISAGREES on the prose and AGREES on the substance*** |
| the other fifteen | MEDIUM / LOW | CHECKED-NEGATIVE | agreed |

⇒ *`P16` integrates a nucleosynthesis network to relic abundances, so from contents it is as high as `P15`.*
⌗ ***And it was in fact read — as one of the 658 receipt files***, where `bbn_network.py` is one of the four
receipts in the whole corpus carrying a convergence check. **The term-side prose verdict and the population
read disagreed, and the population read was the right one.** *That is an argument for this field's target
being the receipts, made by the estimate rather than by me.*
