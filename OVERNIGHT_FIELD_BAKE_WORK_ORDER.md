---
name: overnight-field-bake-work-order
kind: METHOD
current: r3505
job: The self-driving procedure for running the eleven remaining field bakes to completion at the depth the three completed ones set. Written for a node to execute without further instruction.
sources: [chat]
---

# OVERNIGHT FIELD-BAKE WORK ORDER

> **▣ METHOD — run the remaining ELEVEN field bakes to completion**, *at the depth of the three
> already at 100%. **This is a procedure, not a target.** Run the loop until the queue is empty.*

**⌗ THE JOB'S SIZE.** *Eleven fields × seventeen papers = **187 paper-readings**. Most are short: a
field's vocabulary in a given paper is usually **homonymic**, and the reading takes one grep and one
passage. Perhaps a quarter yield a probe worth a receipt. Budget accordingly and keep moving.*

---

## ⌘ THE STANDARD

***A field is done when its subject is exhausted, judged by READING every one of the seventeen
papers.*** *Not when a probe count or a line count is hit.* ⌗ `THE_FIELD_BAKE_PLAN.md` *records why:
the bar in it was measured from ledgers that reach only **12–35%** of the corpus, so it counted their
length and never their reach. **Meeting it is necessary and never sufficient.***

⛔ ***Every paper ends in one of two states, BY NAME, in the ledger: WORKED, or CHECKED-NEGATIVE.
Never unmentioned.*** *The distinction between "not worked" and "not looked at" is the whole point;
it was blurred twice today and both fields had to be reopened.*

---

## ⌘ THE LOOP, PER FIELD

### STEP 1 — `R0` BASELINE, BEFORE ASSERTING ANY HOLE

*Grep the field's vocabulary across the seventeen paper bodies with comments stripped. For every term
over ~×20, **read three occurrences and classify the sense**. Write the baseline into the ledger as a
table: term, count, what it actually is.*

⇒ ***This routinely halves a field before any probe***: *spectral theory's `quantisation` ×66 was
**canonical** quantisation and `gap` ×30 mostly **physical** gaps.*

```python
cd /root/soe/repo/corpus && python3 - <<'PY'
import re, glob
V = [ ... ONE TERM PER PATTERN ... ]
for f in sorted(glob.glob('*.tex')):
    if f.startswith('appendix'): continue
    s = open(f, encoding='utf-8', errors='replace').read()
    s = '\n'.join(re.sub(r'(?<!\\)%.*$', '', l) for l in s.split('\n'))
    ...
PY
```

### STEP 2 — ESTIMATE ALL SEVENTEEN FROM CONTENTS

*Read each **abstract**. Rate **HIGH / MEDIUM / LOW** with a one-line **reason drawn from what the
paper is about**, not from its counts. Write the table into the ledger **before** working any of them,
then score it afterwards.*

⌗ *Today's ratings were usually right and their **reasons** wrong about half the time. **Both facts
are worth having on the record.***

### STEP 3 — WORK EVERY PAPER, HIGHEST ESTIMATE FIRST

*Per paper:*

1. **Grep** the field's tight vocabulary in that paper.
2. ***READ the passages, and READ THE SENTENCE AFTER EACH.*** **Do not stop at a full stop.**
3. **Decide:** is there a **checkable** claim — a number, an order, a dimension, a count, a
   classification, an inequality, a limit?
4. **If NO:** record the paper **CHECKED-NEGATIVE by name**, with a one-line table of what each
   candidate term turned out to be. *This is a result and takes two minutes.* Move on.
5. **If YES:** verify it — **symbolically** with sympy where possible, **numerically** where not, and
   ***always both when a simplifier is involved***.
6. **Write a receipt** in `storyboard_receipts/`, named `<PREFIX>_<probe>_<claim>.py`, with a
   docstring stating `LEVEL`, why the probe exists, what is claimed, what is shown, and ***what is
   NOT claimed***. **Real asserts.** Run it. It must print `ALL PASS`.
7. **Write the ledger entry:** the probe row in the lead register, and the finding below it, with the
   receipt named and marked **added and running**.
8. **Commit** with a substantive message, and **push**.

### STEP 4 — MEASURE THE BAR AND MOVE ON

*Lines, numbered probes, receipts running, papers, **reach**. Write it as **MEASURED**, never
asserted.* ⛔ ***Record SHORT if short. Never round up.***

---

## ⌘ THE ORDER

| # | field | at | notes |
|---|---|---|---|
| 1 | **complex analysis** | 6/17 | *continue with `P15` (×99, largest unread), then `P06` 58, `P14` 53, `P16` 39, `P08` 20, `P10` 19, `P11` 15, `P01` 10, `p0` 10, `P12` 9, `P09` 6, `P04`* |
| 2 | **category theory** | 2/17 | |
| 3 | **optics / lensing** | 3/17 | |
| 4 | **variational** | 4/17 | |
| 5 | **conformal geometry** | 4/17 | |
| 6 | **quadric geometry** | 5/17 | |
| 7 | **involution / real forms** | 6/17 | |
| 8 | **representation theory** | 6/17 | |
| 9 | **Cartan / holonomy** | 6/17 | |
| 10 | **statistics / inference** | 7/17 | |
| 11 | **combinatorics** | 6/17 | |

*Then **create ledgers for and throw** the three never thrown: **convexity/optimisation** (×143),
**algebraic geometry** (×57), **catastrophe/singularity theory** (×54).*
⌗ **Use `SPECTRAL_THEORY_LEDGER.md` as the template** — *it has the `R0` baseline, the estimate table,
the lead register and the measured bar in the right shape.*

---

## ⌘ WHAT COUNTS AS A FINDING

*The productive shapes, all of which recurred today:*

- ***THE CORPUS DOES IT AND DOESN'T NAME IT.*** *`kernel` ×147 in four senses; `elliptic` only in a
  bibliography title; **Shale's criterion** behind `P01`'s dismissal; **von Neumann's dimension
  count** behind `P06`'s constants claim; the Kretschmann scalar **meromorphic with poles of order
  twelve** where `P02` says "chain-rule artefact". **State the theorem, verify it, route the clause.***
- ***TWO PAPERS SAY ONE THING AND NEITHER CITES THE OTHER.*** *`P07`'s parameter form joined to
  `P10`'s spectrum floor; the tower's gap and the wall's gap; **Nariai and Petrov type D as one
  discriminant condition**; `P05`'s invertibility and `S7`'s no-degeneracy as **one Möbius map**.*
  **These are the best findings and are only visible across papers.**
- ***A DECLINED CLAIM THAT IS AVAILABLE.*** *`P10`'s "we record, **without claiming it**" turned out
  to be **entailed**. Look for hedges and test them.*
- ***A MISATTRIBUTION THAT LEAVES THE CONCLUSION INTACT.*** *`P11`'s $a^{-2}$ belongs to $W$ not $Q$;
  `P15`'s WKB residual is an **offset**, not an adiabatic error.* **Say plainly that the conclusion
  stands.**

---

## ⚠ TRAPS — EVERY ONE A REAL INCIDENT FROM TODAY

- ***Read one sentence further.*** *`P16`'s "an identification this paper does not establish" — the
  **next sentence** supplied the map.*
- ***Use the corpus's DERIVED quantity over the textbook one.*** *TT degeneracy: the textbook
  $2(n^2-1)$ vs the corpus's $2(n-1)(n+3)$. **The corpus is right.***
- ***One term per regex pattern.*** *`casus irreducibilis|discriminant` reported six hits under the
  first name when all six were the second.*
- ***Check simplifiers against a closed form.*** *sympy's `fu` and `TR8` **both silently failed** to
  expand $\sin^n$ into multiple angles; the binomial formula caught it. And sympy returns
  `oo + log(...)` rather than bare `oo` — test with `.has(oo)`, not `==`.*
- ***Sympy objects reject width format specifiers.*** *Use `str(x)` inside f-string field widths.*
- ***Prefix globs catch non-receipts.*** *`SP_own_terms_attempt.py` (r2419) does not print `ALL PASS`
  and is **not** a failure.*
- ***Homonyms are the norm.*** *`sheet` is a hyperboloid sheet; `residue` is a leftover; `extension`
  is generalisation; `domain` is domain-of-dependence; `completeness` is causal or group completeness;
  `spectrum` is usually the power spectrum.*
- ***A passing receipt beside an unreceipted sentence is how a small error lives long.*** *`P11`'s
  receipt covers its equation and not its decay claim.*

---

## ⌘ CROSS-FIELD CORRECTIONS — EXPECT THEM

*Four happened today: `F17`→`H20`, `F19`→`P11`, `S0′`→`H13`, `S8`→`H14`.*
⇒ ***When a field's reading contradicts another field's ledger entry, the reading wins if it is
verified.*** *Correct the **other** field's receipt **and** its ledger entry, **rerun** that receipt,
and **say so in the commit**. **Do not leave the contradiction for later.***

---

## ⛔ HARD RULES

1. ***Never edit a paper unattended.*** *Route every consequence with the exact clause written out.*
2. ***Never strike `OWED` 622 or any register row.*** *Striking is not a node's act — the row outlives the session that would strike it, and a node cannot see whether it is the last one owed.* ⌗ **Reworded r3564: this said "Daryl's call", which `check_deferrals` fails on since r1885 — *a written deferral outlives the moment and gets quoted back as authority*. The constraint is unchanged and stronger for resting on a reason rather than on a person.**
3. ***Never mark a field done on a count.*** *Measure, and record short if short.*
4. ***Say what was DONE, not only what was wrong*** — *when a ledger entry names a defect, the same
   entry states **that the fix landed and where**.*
5. ***Every receipt must run and print `ALL PASS`*** *before its ledger entry is written.*

---

## ⌘ WHEN THE QUEUE IS EMPTY

*Rewrite the whole-set table at the top of `THE_FIELD_BAKE_PLAN.md` with the new reach numbers, and
add a short section: **which fields closed**, **what was found that touches the physics** rather than
the bookkeeping, and **every cross-field correction made**.*
⛔ ***Leave `622` open, with its strike condition intact.***
