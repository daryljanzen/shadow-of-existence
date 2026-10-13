# Test 6 asks after a bad arm, and the defect is a good arm too few

**What this is.** A coverage check on `THE_RULE.md` as redrafted at `96fc83f1`, run because that commit
wrote a **bound** into Test 1: *"Nothing else outside the quotation makes the repair owed under this test.
That the sentence goes on to say more, or that the receipt's claim is broader than the quoted words, is not
a ground here."* The narrower-than-claim family is exactly that shape, so the question is whether Tests 2–7
still catch its members once Test 1 no longer can.

**Four of the five members are caught, and one is not.** This document is the one that is not. It reports a
measurement on three live ledger rows, the ablation that confirms them, and a one-sentence repair to Test 6.

---

## 1. The family against the bounded rule

| member | shape | caught by |
|---|---|---|
| ⓐ | the PROXY — a name standing for a proposition | Test 3 when it is a tool's identifier; Test 4 when the name repeats; **step 4's `DELIBERATE` branch otherwise** |
| ⓑ | **the disjunction pinning a conjunction** | **nothing — this document** |
| ⓒ | the DEAD or UNDECIDING ALT arm | Test 6 |
| ⓓ | the arm behind a vacuous guard | Test 7 |
| ⓔ | a complete clause that drops its own condition | Test 1, second bullet |

ⓐ's residue is the NAME rule already filed and awaiting a ruling; it is not re-opened here. The bound makes
it live rather than academic, because the residue now lands on `DELIBERATE` by the rule's own step 4.

## 2. Of the nine disjunction rows in the ledger, Test 6 catches six

`corpus/quote_pin_baseline.tsv`, the 350 rows verdicted `REPAIR-OWED`, the nine whose reason names a
disjunction:

- **six are caught.** `3.3`, `rescal`, `scanner`, `CR/LCDM`, `INPUT`, `WITHDRAWN` — each a vacuous or
  never-true arm, which is Test 6's own wording: *"true for a reason unrelated to the claim (a bare label,
  a common word) or can never be true."*
- **three are not.** The `L147_two_arm/B10` pair and the `B3` row — *"the PROXY case of
  narrower-than-claim: the label claims a CONJUNCTION and the check is a DISJUNCTION of two P1 sentences,
  so either alone passes it."*

So the gap is specific, not a blanket: Test 6 works on five of the six arms it was drafted from and misses
a sixth shape.

## 3. The three rows, with every test run

The site, `receipts/L147_two_arm/B10_the_thermal_mechanism_needs_an_exponential_approach.py:179`:

```python
check('and it says the two readings are not reconciled there, and claims the coincidence rather '
      'than a value',
      'What is claimed is the coincidence and not a value' in allp
      or 'the two readings are not reconciled here' in allp)
```

The claim is read from the check's own label, as the rule's *"What the words mean here"* prescribes. The
label is a **conjunction**. The code is a **disjunction**.

- **Step 1** — wording read as a statement. It is a pin.
- **Step 2** — not a fixed record quoted as itself: a live paper, and the claim is not that the text merely
  stands where it stands.
- **Test 1** — silent. The subject (*the two readings*) is inside; no condition is dropped; the negation is
  inside. And the new bound forecloses the only other reading, which is this row's actual defect.
- **Test 2** — silent. *the two readings* is a noun phrase beginning with "the" that names its thing in its
  own words, which the rule says explicitly does not owe the repair; *readings* is not among the head nouns
  that name nothing.
- **Test 3** — silent. No tool behaviour is claimed.
- **Test 4** — silent, **measured**: each literal occurs **once**, in `BH_causality_v2.tex`, which is P1 and
  is what the claim concerns. The count was `1` at **every one of the 17 commits** that touch that path and
  `0` before `0d38a5bf3754` introduced it, so no bullet of Test 4 fires.
  (`git log -S` finds nothing for these literals because they span a newline in the source and exist only in
  the receipt's flattened read; the counts above are measured on the flattened read, as the receipt reads it.)
- **Test 5** — silent, and it is the mirror of the defect. It requires *"several quoted pieces in one file"*
  required **together**; a disjunction requires nothing together, so the test cannot reach it.
- **Test 6** — silent. Both arms are live sentences of P1, each bearing on the claim. Neither is vacuous,
  neither can never be true.
- **Test 7** — silent. No guard passes on nothing.
- **⇒ Step 4** — *"a complete sentence or clause that names its own subject and carries the claim"* →
  **`MEANING-HELD`**.

**The bounded rule verdicts `MEANING-HELD` where the ledger has `REPAIR-OWED`, on three rows.**

## 4. The ablation, which is why the ledger is right

Delete one arm from P1 and ask what the check does:

| P1 | the check, as written | the label, as stated |
|---|---|---|
| untouched | `True` | `True` |
| arm A deleted | `True` | **`False`** |
| arm B deleted | `True` | **`False`** |
| both deleted | `False` | `False` |

**The check passes while the label it prints is false.** That is a repair owed on any reading, and no test
in 1–7 asks for it.

## 5. The scope defect is not the catch, and the counterfactual shows it

The check searches `allp` — every paper concatenated — while the claim is about P1. The receipt's own `r4022`
comment names that class. A reader *might* stretch Test 4's fourth bullet (*"the claim is about one row or one
section and the check searches the whole file"*) from one-section-of-a-file to one-file-of-a-corpus and catch
the row there.

It would catch it for the wrong reason, and the counterfactual settles it: narrow `allp` → `p1` and **either
arm alone still passes**, measured. The or-for-and defect is independent of the scope and survives its repair.
After a scope fix, nothing in Tests 1–7 reaches these rows at all.

## 6. The population, as a ceiling and not a count

An AST sweep of all **1,071** receipts for `check(label, cond)` where the label is a static string containing
*and* and `cond` is a top-level `or`: **67 sites**.

**67 is a ceiling, not a count.** A conjunctive-sounding label is not automatically defective — most of the 67
use *and* as discourse glue (*"⇒ and it reports the state disagreement"*), not as a claim-level conjunction of
the two arms the `or` offers. **Three are confirmed by the ablation above; 64 are unread.** Separating them
needs the arms' literals resolved against the files they are tested in, which is `measure()`'s job and not a
static read. The sweep is one script and reproduces from this document.

## 7. The repair, which is one sentence

Test 6 is drafted around a **bad arm**. The defect here is a **good arm too few**. Adding a second limb covers
it and moves no verdict Test 6 already makes:

> **Test 6 — A choice between alternatives, where the weaker one decides alone, or where the claim needs both.**
> … *The repair is also owed when the check accepts `this or that` and the claim it serves requires both, whether
> or not either alternative is vacuous: a disjunction cannot carry a conjunction, and either arm alone leaves the
> claim unestablished.*

Nothing else in the rule changes. Tests 1–5 and 7, the four steps and the `ENCODING-OK` border are untouched.

**Not scored, and not tuned.** `70`'s row-level result was not opened, and no key of the 47 was read. The
redraft follows from the bound `96fc83f1` wrote and from the three rows above, not from which keys would move.
