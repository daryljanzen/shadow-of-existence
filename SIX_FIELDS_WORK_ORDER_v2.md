---
name: six-fields-work-order-v2
kind: METHOD
current: r3658
job: The field-bake procedure, rewritten after running integrable systems end to end at 17/17. Supersedes SIX_FIELDS_WORK_ORDER.md, which was written before the method was known.
sources: [chat]
---

# FIELD-BAKE ORDER v2 — FOR 60, FOR THE LAST FIVE FIELDS

**⛔ THIS SUPERSEDES `SIX_FIELDS_WORK_ORDER.md`.** *That order was written after four turns of a field and
it was wrong about the method. This one is written after one field carried to **17 of 17** with the locator
scored, and every change below is from a failure or a result in that run, cited.*

---

## 0. WHAT v1 GOT WRONG, SO YOU DO NOT INHERIT IT

| v1 said | what happened | v2 says |
|---|---|---|
| `R0` baseline first: grep the field's vocabulary, then probe | **`P02` scores ZERO on every term in this field's vocabulary and is the field's founding example.** A term list is a list of what you already know the field to contain; grepping it returns only that | **`R0` is a MEASUREMENT, not a starting point.** Pass A comes first and reads abstracts |
| rate papers `HIGH`/`MEDIUM`/`LOW` | a rank is a licence to skip; four papers worked, thirteen written off in one-line rows | **no ranking.** The abstract **LOCATES**: it names sections and states a prediction that can be scored wrong |
| "a bounce is a result", "three of four owing nothing is the expected shape" | **offramps.** Read at scale they authorise cheap `CHECKED-NEGATIVE` rows | *deleted.* A negative is written **only** with the reason it is negative and what was read to establish it |
| — | **I landed 14 probes and wrote 0 receipts.** Every verification was in-session and is now gone | **§4 is a hard requirement, not a step** |

---

## 1. THE THREE PASSES. NO PAPER LEAVES PASS B UNREAD.

### PASS A — LOCATE (all 17 abstracts, before any grep)

*Read each abstract. From **what the paper is about**, name the `\label`ed sections where this field's
content would live, and state **what would be there** if the field is relevant. Write the whole table into
the ledger **before working any paper**.*

⌗ **The prediction must be falsifiable.** *"This field may be relevant" is not a prediction. "The dial's
three coupled projections are an action-angle description, in `sec:params`" is one — and it was **wrong**,
which is how it earned its place.*

### PASS B — READ (every named section, every paper)

*Open every named section and read it. Read the sentence after each passage; do not stop at a full stop.*

**Verdict, one of five:**

| | |
|---|---|
| **CONFIRMED** | the content is there and in the section named |
| **REDIRECTED** | the content is there, in a section you did **not** name — record which. *Expect this: 2 of 17 in the run, and both were address misses on a correct paper* |
| **REFUTED** | the prediction was wrong |
| **CHECKED-NEGATIVE** | nothing for this field — **and you say why, and what you read to establish it** |
| **ALREADY LANDED** | a neighbouring field got there first. *`P05` was this; it is not the same as empty and the row must say which* |

### PASS C — WORK, RECEIPT, LAND, MARK

*See §4. Nothing is finished at pass B.*

---

## 2. ⛔⛔ THE RULE THE RUN PRODUCED, AND IT IS THE MOST IMPORTANT LINE HERE

### ***A PREDICTION OF EMPTINESS GETS MORE SCRUTINY, NOT LESS.***

*The locator carried exactly one prediction that a paper was genuinely empty — `P06`, "no dynamics" — and
flagged at the time that it had to be tested rather than assumed.* ⛔ ***It was the single REFUTED
prediction of seventeen.*** *`P06` carries the field's sharpest connection: its least-arbitrariness
argument and the substrate's maximal superintegrability are **one property read epistemically and
dynamically**, joined at transitivity of the group action.*

⌗ ***AND ALL FOUR PAPERS A VOCABULARY SCREEN WOULD HAVE SCORED EMPTY CARRIED SOMETHING:***

| | why a screen would miss it | what it carried |
|---|---|---|
| **`P02`** | ×0 on every term in the field's vocabulary | **the field's founding example** — its circle is a phase portrait, its cycloid a harmonic oscillator |
| **`P04`** | came back empty on **all six** of your fields | its path integral **is** a first integral; the null-cone restriction is why its measurement works |
| **`P06`** | philosophy, no equations | least-arbitrariness **is** superintegrability |
| **`P01`** | causal structure, not motion | the horizon is a **fixed point** and its eigenvalue is the surface gravity |

⇒ ***Three of those four produced a finding that changed how another paper reads.*** **A paper that looks
empty is the one to read hardest.**

---

## 3. WHAT PASS B ACTUALLY DOES — five things a grep cannot

*Every one of these is from the run, and none is reachable by a term list.*

1. **Finds the field's object under another name.** *`P02` never writes "oscillator"; it writes
   $r''=-(r-M)$ and calls the locus a geometric circle. **That circle is the phase portrait**, its
   "homogeneity" is a level set of the conserved energy, and its two critical points are turning points.*
2. **Finds one paper's fact explaining another paper's choice.** *`P12` lists isotropy dimensions; read as
   a count of linear first integrals, **Kerr–de Sitter is short by one** — which is exactly the deficit
   `P09`'s Killing tensor makes up. Neither paper says the first is the reason for the second.*
3. **Finds the qualifier a claim needs.** *`P08`: "run inward, the closed member is the cycloid" — exact at
   $\Lambda=0$, a small-$r$ reading otherwise, the omitted term's weight $0.27$ at $r/\alpha=0.3$.*
4. **Finds the wrong name for a right computation.** *`P10` calls its correction "adiabatic" and checks
   that $\int\omega\,\dd s$ converges. Both are right and they are different questions: the adiabatic
   parameter **diverges** at the branch point. `P15` names the same object correctly, as WKB.*
5. **Finds canon rows.** *`integrable` carries **six** senses and `wall` **three objects** — and in each
   case **one paper carries two of them**, which is what misleads a reader. **Canon rows come out of
   reading, never out of counting**, and they go to `ONTOLOGY_FOUNDATION_INDEX` §0, not to a paper.*

---

## 4. ⛔⛔ RECEIPTS — THE REQUIREMENT I FAILED, WRITTEN AS A GATE ON YOURSELF

***I landed fourteen probes in this field and wrote zero receipts.*** *Every verification was symbolic,
correct, and run in-session — and it is **gone**. Not reproducible, not checkable by you, not runnable by
any gate. **You wrote and registered receipts for your six fields and I did not for mine; do not copy my
practice.***

**PER FIELD, NOT NEGOTIABLE:**

- ***Every landed probe that asserts a computation gets a receipt.*** *Not two per field — **one per
  computational claim**. If the clause you land says a thing is identical, divergent, elementary, short by
  one, or not shape-invariant, that is a receipt.*
- **Real asserts, and the receipt must be able to fail.** *`lint_assertions` catches `expr == True`; it
  caught one in a receipt of **every single one of your six fields**. Pin a measured value.*
- **Register it in `receipts/INDEX.md` in the same commit.** *An unregistered receipt is invisible to the
  appendix rails and to `check_receipt_orphans`.*
- **Run it. It must print `ALL PASS`.**

⌗ *Backfilling mine is `59`'s job and is being done in pass C of this field; the five fields ahead of you
should not need backfilling.*

---

## 5. VERIFICATION — three rules, each from an error

1. **Verify symbolically before writing, and check your own convention against the paper's.** *I computed
   the slicing potential as $V=-f/2$ and got a **minimum** at Nariai — the opposite conclusion. `P03`'s own
   formula carries a $\operatorname{sgn}f$ and the uniform potential is $-\lvert f\rvert/2$. **The paper's
   expression was the check on my arithmetic.***
2. **State what you are NOT claiming.** *Least-arbitrariness and superintegrability share a root; the
   modulus count does **not** equal the integral deficit ($15\to4$ against $0\to1$), and the ledger says so
   explicitly.*
3. **Compile after every landing.** *`\dd` is undefined in `P04` and `P08`. It broke both, twice, in the
   same way — the second time after I had already recorded the first.*

---

## 6. THE ORDER, AND WHAT IS ALREADY DONE

| # | field | state |
|---|---|---|
| 1 | **integrable systems** | ⛭ **17/17 pass B, 14 probes, `59`. Receipts in progress.** Do not re-run |
| 2 | **differential topology / index theory** | ⟐ **YOURS, and first.** `Atiyah` ×17; `P13`'s obstruction and `P14`'s leaf index, which its own text marks *traced rather than computed* — the most load-bearing untested step in the matter sector |
| 3 | **information theory** | ⟐ screen `entropy` hard; horizon thermodynamic entropy is a homonym for this field's object |
| 4 | **number theory** | ⟐ screen `zeta` |
| 5 | **numerical analysis** | ⟐ its real target is the corpus's computational receipts, not its prose |
| 6 | **probability / stochastic** | ⟐ thinnest — **and after `P06`, "thinnest" is not a licence** |

⌗ *Your six ledgers are merged and nothing in them is struck. Where a v2 pass finds more, the row is
**updated**, not replaced — and where your reach table scored nine papers in one row on a screen, that row
is where a v2 pass starts.*

---

## 7. THE PACE, AND WHY IT IS NOT NEGOTIABLE

**One paper per turn.** *`reach_baseline.py` made the measurement instant and it earned that immediately —
`Lax` reads ×112 raw across fifteen papers and **×0 word-bounded**, the raw hits being `\Lambda` splitting
under the search. The `\ldg` rail removed the landing lag. **Neither touched the reading.***

⌗ ***A read that sharpens a QUESTION rather than producing a claim is a legitimate outcome.*** *`I4` is
one: `P11` carries two conserved quantities, names them with two different words, and never asks whether
its sector is Liouville-integrable; `P10` then **scoped** the question rather than answering it, because
the radial lift is 1 DOF with 1 integral and the question is empty there. **Recording that is worth more
than manufacturing an answer.***

⌗ **Score the locator at the end**, as a table: right on paper, right on address, redirected, refuted,
checked-negative. *This run: 16/17 paper, 14/17 address, 2 redirected, 1 refuted, 1 already-landed.*
**A locator that never misses is not locating anything.**

⌗ *Run `bash scripts/sweep_gates.sh` before every push. It is specified — `NODE=ci`, 420s — and reports a
delta. It sits at **94 pass, 0 fail, 1 unrun**.*
