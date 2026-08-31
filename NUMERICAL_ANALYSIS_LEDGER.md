---
name: numerical-analysis-ledger
kind: FIELD-BAKE
current: r3724
job: The numerical-analysis field-bake ledger — what bit, what bounced, and where the boundary is. The one field whose target was the receipts rather than the prose.
sources: [chat]
---

> ⛭ **`Q1`'s RECEIPT — named here at r3660, because it was named nowhere.** *`receipts/L_numerics/Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py`* — *a stated tolerance is a request and the corpus answers it.* ⌗ *It ran and was registered; **the ledger whose probe it settles did not name it**, so the computation had no argument attached. `check_citation_chain` now fails on that.*

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

---
---

# ⛭⛭⛭ THE v2 PASS — r3712, AND IT OPENS ON THE ITEM THE v1 PASS DECLARED TOO BIG TO SHIP

> ⛭ ***THE v1 PASS OF THIS FIELD IS THE STRONGEST OF THE SIX AND ITS REACH TABLE IS NOT WHERE THIS
> ONE STARTS.*** *It read the receipts as a **population** — every ODE call located, every
> float-equality site read individually, four whole receipts re-run under a patched solver — which
> is the method §0 asks for, applied to the right layer, before the order said to.*
>
> ⛔ ***SO THE v2 PASS STARTS AT `Q5`, WHICH IS OPEN AND WHICH THE v1 CLOSE DECLINED WITH A REASON:***
> *"688 sites in 210 files is beyond what this pass can read, and a sampling verdict would be a
> census that is not one … **that needs a mutation harness, not a reading**, and building one is a
> larger instrument than a field bake should ship."*
> ⇒ ***THE ITEM IS SPECIFIED — "mutate the asserted quantity by the tolerance and require the
> assertion to fail" — AND THE ONLY REASON GIVEN FOR NOT DOING IT IS SIZE.*** *That is not a
> boundary; it is a cost. **The v2 pass pays it.**  ⌗ And the stake is exact: 688 assertions none of
> which has ever been shown able to fail is the receipt layer's own `check(..., True, ...)`.*
>
> ⌗ *Nothing below is struck. `Q1`–`Q4` stand.*

## ⌗ PASS A — THE LOCATOR. **Written from the seventeen abstracts and section lists, before any
paper or receipt was opened for this pass.** *For this field a row must name where a **computed
number** lives, because the question is not whether the field's words are present but whether the
numbers know what they are worth.*

| # | paper | sections named | ⌗ **the prediction — falsifiable** |
|---|---|---|---|
| 1 | **`P05`** | `sec:deck` (`prop:monodromy`, `rem:monodromy-group`) | ⛭⛭ ***A CONTINUATION THAT STEPS TOO COARSELY MISLABELS SHEETS, AND THIS ONE IS THE COMPUTATION THE WHOLE $S_3$ RESTS ON.*** *`prop:monodromy` says "(Verified numerically by continuation in the complex $2M$-plane)" and `rem:monodromy-group` says outright that the generation claim **"is a computation"** whose alternative was real — had the same pair collided at both points, the group would be $\mathbb{Z}_2$. **Prediction: the continuation's STEP SIZE and its LOOP RADIUS are not swept, so the two transpositions are asserted at one discretisation and never shown stable under refinement.*** ⛔ *Wrong if a refinement or radius sweep is in the receipt* |
| 2 | **`P15`** | `sec:instrument` · `sec:diffusion-scale` · `sec:residual-decomposition` | *`Q2` landed the margin. **Prediction: the remaining exposure is that the validation is a POINT CHECK** — one reference code, one parameter point — so what is established is agreement THERE and not a convergence or a parameter-range statement.* ⛔ *Wrong if the comparison sweeps cosmological parameters* |
| 3 | **`P16`** | `sec:network` | *`bbn_network.py` is one of only four receipts in the corpus carrying convergence language. **Prediction: the convergence check is on the INTEGRATION and not on the NETWORK TRUNCATION** — how many species and reactions are carried — so the controlled error is the solver's and the uncontrolled one is the model's.* ⛔ *Wrong if species count is swept* |
| 4 | **`P03`** | `sec:tour` · `rem:dimension` | ⛭ ***THIS ROW IS THE HARNESS'S OWN CONTROL, AND IT IS WRITTEN BEFORE THE HARNESS.*** *`rem:dimension` reports the dial positions and the quartic's roots "agreeing to machine precision". **Prediction: these are EXACT identities evaluated in floating point, so their assertions are correctly insensitive** — mutating them by many tolerances still passes, and a mutation harness that calls that a defect is measuring its own arithmetic.* ⛔ *If `Q5` finds these flagged, the harness is wrong and not the receipt* |
| 5 | **`P02`** | `sec:ring` · `sec:kretschmann` | *`P02_ring_lambda_limit` takes a $\Lambda\to0$ limit. **Prediction: it samples a decreasing sequence and asserts the endpoint, with no Richardson or order check** — so the limit is exhibited rather than measured* |
| 6 | **`P11`** | `sec:gowdy` · `sec:nonlinear` | *A Cauchy evolution is where step size bites. **Prediction: stated `rtol`/`atol` (as `Q1` found for all 24) and NO grid-refinement check on the spatial discretisation*** |
| 7 | **`P10`** | `sec:lock` | *The paper says the ultraviolet definition of the tower sums is the open frontier. **Prediction: any numerical tower sum uses a mode cutoff whose dependence is not swept**, which is the honest state of an open frontier and not a defect — the row exists to check that it is SAID* |
| 8 | **`P14`** | `sec:chirality` · `sec:count` | *The zero-mode is "an exact solution, not an assertion". **Prediction: its receipts nevertheless carry `abs(...) < tol` on quantities that are exact** — the harmless end of `Q5`, and the second control the harness needs* |
| 9 | **`P04`** | `sec:floor` | *The $10^{-3}$ against $3\times10^{-6}$ is called a **floor**, and every choice biases it downward. **Prediction: its assertion is a deliberately WIDE inequality** — insensitive by design and correct practice. **A harness that cannot tell this from a loose tolerance is not measuring anything*** |
| 10 | **`p0`** | `sec:ledger` · `sec:power` | *The constant ledger is powers of $1/\alpha^{2}$. **Prediction: exact/symbolic, no tolerance**, and `P17_no_second_scale_on_either_face` is an algebraic statement rather than a numerical one* |
| 11 | **`P08`** | `sec:kernel` · `sec:bend` | *The vacuum kernel is a first-order linear ODE solved in closed form. **Prediction: symbolic, tolerance-free**, and any float there is a display* |
| 12 | **`P12`** | `sec:bracket` · `sec:weyl-a3` | *`GROUP_full_order48` and `EMBEDDING_is_Td_equals_WA3` are finite-group computations. **Prediction: exact integer arithmetic throughout, zero tolerances** — and if a tolerance appears in a finite-group receipt it is a finding* |
| 13 | **`P13`** | `sec:cascade` · `sec:a2` | *Rank counts and subalgebra inclusions. **Prediction: exact integers**, and the one place a float could enter — a numerical check that $\su(3)\not\subset\so(5,1)$ — would be the wrong instrument for the claim* |
| 14 | **`P09`** | `sec:pd` · `sec:surj` | *Separability and a surjectivity argument. **Prediction: symbolic verification, and the tolerances present are on the residuals of symbolic substitutions** — i.e. exactly the correctly-insensitive class again* |
| 15 | **`P01`** | `sec:3` · `sec:5` | *Predict NO computation of this field's kind. Test named: **whether the asymptotic-alignment claim is supported by a limit taken numerically**, in which case its rate matters* |
| 16 | **`P06`** | `sec:engine` · `sec:reflexive` | ⛔ ***AND THIS ROW GETS THE HARDEST READ, BY RULE AND BY PRECEDENT.*** *§2, and `P06` was the one REFUTED prediction of the integrable-systems seventeen. **Predict: no number of this field's kind anywhere.** The test is specific: **does any historiographic claim carry a quantity — a count of episodes, a base rate, a reliability estimate — that a computation would have to support?** The paper argues against reliability estimates built from one's own successes, so a number there would be self-undercutting and worth finding* |
| 17 | **`P07`** | `sec:frontiers` · `sec:applications-synthesis` | *A synthesis quotes its companions' numbers. **Prediction: every number in `P07` traces to a companion's receipt, and the test is whether any does not*** |

### ⌗ AND THE ROWS THAT ARE NOT PAPERS — **the receipts population, which is this field's real target**

| # | target | ⌗ **the prediction — falsifiable** |
|---|---|---|
| **R1** | ***`Q5`: the 688 `abs(...) < tol` assertions*** | ⛭⛭ ***PREDICTION: A MEASURABLE FRACTION ARE INSENSITIVE — the assertion still passes when the asserted quantity is moved by several times its own tolerance — and the insensitive ones split into TWO KINDS that must not be confused: **EXACT** comparisons (rows 4, 8, 9, 12, 14 above: correctly insensitive, and flagging them is the harness's error) and **LOOSE** ones (a tolerance far wider than the quantity's actual accuracy, which is the real gap).*** ⛔ *Wrong if essentially every assertion is sensitive, in which case `Q5` closes as a CONFIRMATION exactly as `Q1` did — **and that is the outcome this pass should most want, not least*** |
| **R2** | ***the harness itself*** | *A mutation harness is an instrument and instruments are where this line's errors live. **Prediction: it will need two controls before any verdict it prints can be believed — a deliberately loosened assertion it MUST flag, and a deliberately exact one it MUST NOT.*** ⛔ *If it cannot be made to do both, its output is a census that is not one and the honest close is to say so and leave `Q5` open* |

⌗ ***THE LOCATOR PREDICTS: one paper carrying a genuine open numerical question (`P05`), two
carrying stated-but-unswept approximations (`P15`, `P16`), and fourteen empty on the prose side —
with the field's actual content in `R1`.*** *Scored at the close either way.*

---

## ⌗ PASS B / PASS C — `Q5` IS CLOSED, AND THE QUESTION IT ASKED HAD A FALSE PREMISE

### ⛭⛭⛭ `Q50` — **THE MUTATION HARNESS, BUILT — `scripts/tolerance_audit.py`**

| | |
|---|---|
| **row** | **R1** and **R2** of the locator |
| **verdict** | ⛭⛭ **CONFIRMED on enforcement — and `R1`'s "a measurable fraction are insensitive" is REFUTED, which the row said in advance was the outcome to want** |
| **landed** | `P15` `sec:diffusion-scale`, extending `Q2`'s own sentence — `\ldg{numerical_analysis}` |
| **the receipt** | `receipts/L_numerics/Q50_the_tolerance_comparisons_gate_the_verdict_and_a_third_of_them_are_not_tolerances.py` |
| **the instrument** | `scripts/tolerance_audit.py` — three AST rewrites, five controls of its own |

**THE HARNESS.** *Three AST rewrites of every `abs(E) < T` site, each run from the receipt's own
directory exactly as `run_all_receipts.py` does:* **MARGIN** *(semantics-preserving; records
$\lvert E\rvert/T$)*, **MUTATE-UP** *(`abs(E+3T) < T`; catches the assert shape)*, **MUTATE-DOWN**
*(`abs(E)\*0 < T`; catches the guard shape, where the failure lives on the `<` branch)*.

| the measurement | over **269 files** and **1116 static sites** |
|---|---|
| ⛭ **faithfulness, first** | *the margin transform reproduces the baseline verdict on **269 of 269 files** — the whole population run twice, not a synthetic control* |
| ⛭⛭ **enforcement** | **245 files pass at baseline; 243 of them (99.2%) have at least one tolerance comparison that GATES THE EXIT** |
| ⌗ **the two that do not** | ***both correct***: `P14_lambda_spectrum`'s `abs(lv) <= 4` is a **display filter**; `L562/P1` **skips with a printed reason** — its banked logs are not on this tree — and names `L-830` as the gated self-contained substitute |
| ⛔ **and the premise fails** | *of the **918 sites that execute**: **210 (22.9%) sit at exactly zero**, 82 more at ulp level, 422 in the accuracy band, 150 load-bearing within one order, and **54 (5.9%) sit AT OR OVER their own tolerance** — real-root counters, degeneracy guards, `"NULL" if abs(fv)<1e-12 else "spacelike"` classifiers* |

⇒ ***`Q5` ASKED WHETHER THE TOLERANCES ARE "LOOSE ENOUGH TO PASS ANYTHING", AND THAT QUESTION
PRESUPPOSES EVERY `abs(E) < T` IS AN ACCURACY ASSERTION. MEASURED, A THIRD OF THEM ARE NOT.***
*Two of the five bands are working exactly as intended **by being nowhere near their tolerance**.
A single verdict over 1116 sites would have been meaningless because the sites are not one kind of
thing — and only the measurement could have shown that.*

⛔⛭⛭ ***THE HARNESS'S FIRST PASS REPORTED FOUR DEFECTS AND ALL FOUR WERE ITS OWN BLIND SPOTS.***
*Up-mutation alone left four files exiting 0. **Read one at a time rather than counted**: `L265`'s
`abs(lv) < 3/4` is a threshold predicate on an **integer**; `P14_lambda_spectrum`'s is a display
filter; and `P15_which_coupling`'s two are **guards** whose failure branch is the `<` side, which an
upward kick can only silence.* ⇒ ***A one-sided mutation cannot test a two-sided guard, and
`abs(E) < T` is not always a tolerance. Publishing the four would have been the instrument
reporting its own limits as the corpus's.*** *The down-kick was built from those four and recovers
two of them; `INVARIANT 4` of the receipt fires if anyone removes it.*

⌗ ***AND THE HARNESS BROKE THE FILES IT WAS MEASURING, ONCE.*** *The margin preamble was first
prepended as **text**, which displaced each module's docstring and set `__doc__` to `None`; eleven
receipts that print and split their own docstring died with `AttributeError` and the harness
reported that as **their** result.* ⇒ ***The baseline mode exists because of that: a verdict about
a mutated run is worth nothing without the un-mutated one beside it.***

### ⌗ THE PROSE SIDE — the seventeen locator rows, scored

| # | paper | verdict |
|---|---|---|
| 1 | **`P05`** | ⛭⛭ ***CONFIRMED, AND IT IS THIS FIELD'S ONE REMAINING OPEN QUESTION.*** *`prop:monodromy` is "verified numerically by continuation in the complex $2M$-plane" and `rem:monodromy-group` says the generation claim **is a computation** whose alternative was real. **No step-size or loop-radius sweep appears**, so the two transpositions are established at one discretisation. `X5_monodromy_group` is registered and gated; what is not shown is stability under refinement.* ⌗ *Named as open rather than worked: it is a probe with a real failure mode and it wants its own receipt* |
| 2 | **`P15`** | ⛭ **CONFIRMED** — *the CAMB comparison is a **point check**: one reference, one parameter point. `Q2` landed the margin; the range is still one point* |
| 3 | **`P16`** | ⛭ **CONFIRMED** — *`bbn_network.py`'s convergence language is on the **integration**; the species/reaction truncation is the uncontrolled approximation and is not swept* |
| 4 | **`P03`** | ⛭⛭ **CONFIRMED, AND IT WAS THE HARNESS'S CONTROL BEFORE THE HARNESS EXISTED** — *the "machine precision" agreements are exact identities in floating point, and the margin run puts **210 sites at exactly zero and 82 more at ulp level**. Written into the locator at Pass A, measured at Pass C* |
| 5–14 | **`P02` `P11` `P10` `P14` `P04` `p0` `P08` `P12` `P13` `P09`** | ⛭ **CHECKED-NEGATIVE on the prose, ten times** — *and each is now **measured** on the receipts side rather than screened: every one of their receipt files appears in the 269 and in the enforcement count* |
| 15–17 | **`P01` `P06` `P07`** | ⛭ **CHECKED-NEGATIVE** — *`P06` got the hard read the rule requires: **no historiographic claim carries a quantity a computation would have to support**, and the paper argues explicitly against reliability estimates built from one's own successes, so a number there would have been self-undercutting. There is none* |

---

## ⛭⛭⛭ THE REACH CLOSE — the v2 §5b template, four blocks

### 1 · THE SEVENTEEN, BY NAME — *and the population beside them*

| verdict | papers | count |
|---|---|---|
| ⛭ **LANDING** | `P15` — `Q50`'s clause in `sec:diffusion-scale`, extending `Q2`'s own sentence | **1** |
| ⛭ **WORKED, EARLIER** | `P15` — `Q2`, from the v1 pass, in the same sentence | **—** |
| ⛭ **CONFIRMED, NOTHING OWED** | `P16` *(truncation not swept, and it is honest about it)* · `P03` *(the exactness class, and it became the harness's control)* | **2** |
| ⟐ **OPEN, WITH ITS CHECK NAMED** | `P05` — *the monodromy continuation is unswept in step size and radius* | **1** |
| ⛭ **CHECKED-NEGATIVE on the prose, each measured on the receipts side** | the other thirteen | **13** |

⌗ ***AND THE POPULATION IS THE ROW THAT MATTERS***: *269 receipt files, 1116 sites, run four times
each — **1076 subprocess runs**, against the v1 pass's four.*

### 2 · THE BAR, MEASURED

| | |
|---|---|
| papers read, by name | **17 of 17** |
| receipt files run | **269**, in four modes each |
| Pass A predictions written **before** any work | **19** (17 papers + `R1` + `R2`), committed at **r3712** |
| receipts written by THIS pass | **2** — `Q50` and `Q51` |
| instruments built | **1** — `scripts/tolerance_audit.py`, with five controls of its own |
| clauses landed | **2** — `P15` and `P05`, each with its `\rcpt`, its `\ldg`, and its naming here |
| `\ldg{numerical_analysis}` markers in papers | **3** — `P15` ×2 and `P05` (r3724) |
| ⛔ **locator predictions REFUTED** | **1** — `R1`'s "a measurable fraction are insensitive" |
| ⌗ **harness defects found by the harness's own output** | **2** — *the docstring displacement, and the one-sided mutation* |

### 3 · WHAT IS STILL OPEN, SAID SHORT

* ~~⟐ ***`P05`'s MONODROMY CONTINUATION IS UNSWEPT.***~~ ⛭⛭ ***DONE at r3724, `Q51`.***
  *This block said the check was small and named it rather than doing it. **It was small — and
  scoping it out was the wrong call, so the sentence is kept and the work is done.*** The sweep is
  8 step counts × 6 radii at both branch points: **one transposition each, $(1\,2)$ and $(0\,1)$,
  differing, generating $S_3$** — so `prop:monodromy` stands and now stands on a sweep.
  ⛔ ***And it found two preconditions the sentence does not state, both of which fail SILENTLY:***
  *a loop wider than the branch-point separation $4/(3\sqrt3)=0.7698$ returns the **3-cycle** — the
  product of the two, a correct monodromy of a different loop; and a two-sample loop at large radius
  returns the **identity**, which would make the deck structure vacuous.* **Neither raises an error,
  because nearest-neighbour matching always succeeds — correctly or not.**
  ⌗ *`receipts/L_numerics/Q51_the_monodromy_continuation_is_stable_and_it_has_two_preconditions_neither_stated.py`,
  landed in `P05` `prop:monodromy`.*
* ⟐ ***`P15`'s VALIDATION IS A POINT CHECK.*** *One reference code, one parameter point. `Q2` fixed
  what the word "validated" carries; **what it ranges over is still one point.***
* ⟐ ***THE 54 OVER-TOLERANCE SITES WERE SAMPLED, NOT ENUMERATED.*** *Four were read and all four
  are classifiers. **The other fifty are inferred to be the same kind and that inference is not a
  measurement** — said here rather than left for a later reader to discover.*

### 4 · WHAT THE FIELD CHANGED, ONE LINE PER PAPER

| paper | what changed |
|---|---|
| **`P15`** | *gained the second half of the sentence `Q2` started: **what a stated tolerance carries anywhere in this corpus is now measured rather than assumed*** |
| **`P05`** | *nothing landed — and it acquired a **named open numerical question** where it had none* |
| **`P03`** | *nothing owed — and it supplied the class that kept the harness honest* |
| **the other fourteen** | *nothing owed on the prose, **and every one of them is now inside a measured population** rather than inside a screened row* |

⇒ ⛔ ***READ AS A LIST: THIS FIELD DID NOT FIND A DEFECT, TWICE.*** *`Q1` confirmed the tolerances
are honest; `Q50` confirms they are enforced. **Both times the field went looking for a failure and
measured a success instead**, and both times the measurement was worth more than the suspicion —
because before them, "the corpus's numerics are careful" was a thing nobody had checked.*
⌗ ***The two defects this pass DID find were in the instrument.***

---

## ⛭ THE BOUNDARY, RE-STATED — the v1 block stands and gains one line

> *v1: **the papers contain no numerical analysis and the receipts contain a great deal of it, done
> well**, and a field bake reading only the seventeen bodies would have reported the field absent.*

⛭⛭ ***AND THE v2 PASS ADDS WHAT THAT ASYMMETRY COSTS: the computational layer is where the
corpus's care lives and it is the layer with no reviewer.*** *A paper's claim is read by whoever
reads the paper. **A receipt's `abs(x-y) < 1e-9` is read by nobody, and until this pass nothing had
ever established that it could fail.*** ⇒ *That is why the field's two findings are both
confirmations and why both were worth the run: **an unexamined success is not the same thing as a
success**, and the difference is exactly one instrument.*
