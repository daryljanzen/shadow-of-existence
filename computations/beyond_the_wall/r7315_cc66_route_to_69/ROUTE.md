# For `69`: one clause in Test 5, and the three rows it decides

**Routed at `r7315` by order of the gate.** Self-contained: nothing here needs the earlier documents, and
the one measurement it rests on reproduces from one script in this repository.

**Measured against `THE_RULE.md` at `6bef6fd5`**, the second redraft, which is the live text — unchanged
since. `sweep_and_ablate.py` asserts that and exits `1` if the routing step, Test 5's antecedent or Test 6's
antecedent moves, so this document cannot quietly go stale.

---

## 1. What is asked

**One clause added to Test 5.** Test 6 needs no change. Nothing else in the rule changes, and no verdict
either test already makes is moved.

> **Test 5 — Two or more pieces are required together and nothing joins them.**
> The check requires several quoted pieces in one file, and they could sit in unrelated paragraphs while the
> check still passes; ***or the claim needs all of them and the check accepts any one — a disjunction cannot
> carry a conjunction.*** The repair is owed on every piece, including a piece that would be a name or a
> value on its own: half of a joint requirement does not carry the claim.

## 2. Why Test 5 and not Test 6 — your own second redraft is the reason

`r7307` proposed this as a second limb on **Test 6**. **That was the wrong place, and the second redraft is
what showed it.** You added a routing step to step 2:

> *"When one check requires several quoted pieces, read its claim before step 2. If the claim says something
> about the pieces together — that they are beside each other, that between them they state one thing, that
> one cites the other — step 2 reaches none of them, and **Test 5 decides**."*

**That step does the hard half correctly.** It identifies a claim that speaks of its pieces together and
sends the arms onward. **The gap is that it sends them to a Test 5 that cannot receive them:** Test 5's
antecedent is *"required **together**"*, and a disjunction requires nothing together.

⇒ **So the routing already exists and already fires. One clause widens its destination to match what it
hands over.** Putting it in Test 6 instead would leave the routing step pointing at a test that still
refuses the case, and would duplicate in Test 6 a condition step 2 has already evaluated.

## 3. The three rows

Two in `receipts/L147_two_arm/B10_the_thermal_mechanism_needs_an_exponential_approach.py` at line 179:

```python
check('and it says the two readings are not reconciled there, and claims the coincidence rather '
      'than a value',
      'What is claimed is the coincidence and not a value' in allp
      or 'the two readings are not reconciled here' in allp)
```

and one in `receipts/L147_two_arm/B3_a_dichotomy_stated_is_not_a_dichotomy_proved.py` — `21.8%`, the other
arm of the same shape.

**The label is a conjunction. The code is a disjunction.** The claim is read from the check's own label, as
the rule prescribes.

## 4. The measurement, and it is also the proof that Test 5 cannot reach it

**The ablation.** Delete one arm from P1 and ask what the check does:

| P1 | the check | the label, as stated |
|---|---|---|
| untouched | `True` | `True` |
| arm A deleted | `True` | **`False`** |
| arm B deleted | `True` | **`False`** |
| both deleted | `False` | `False` |

**The check passes while the label it prints is false, in 2 of 4 states.** And the same table is why Test 5's
present antecedent fails: **if deleting either arm leaves the check passing, the two arms are not required
together.** The measurement that shows the defect shows why the test the rule routes it to cannot decide it.

**Every other test was run and each is silent**, by measurement rather than by reading:

- **Test 1** — subject inside, no condition dropped, the negation inside. (Your widened condition list —
  *if, when, unless, provided, only, given, with, for, on, under, at, in the case of* — reaches none of it.)
- **Test 2** — the subjects are `the two readings` and `What is claimed`; no pronoun, demonstrative,
  quantifier or pointing word, and none of your newly-covered inner clauses or possessives.
- **Test 3** — no tool behaviour is claimed.
- **Test 4** — **measured:** one occurrence of each literal, in `corpus/BH_causality_v2.tex`, which is the
  paper the claim concerns, and the count was `1` at **every one of the 17 commits** that touch that path
  and `0` before the commit that introduced it. No bullet fires.
- **Test 6** — both arms are live sentences of P1, each bearing on the claim. Neither is vacuous and neither
  can never be true, so Test 6's own antecedent is false. **Test 6 is not the right home for this.**
- **Test 7** — no guard passes on nothing.

⌈ Worth knowing on its own: `git log -S` finds **nothing** for these literals, because they span a newline
in the source and exist only in the receipt's flattened read. The counts above are measured on the flattened
read, as the receipt reads it. A count history taken with `-S` would have reported them absent. ⌋

## 5. What the rule gives today, and why the third row is the sharpest

With the routing dead-ended, all three fall through to **step 4**:

| row | step 4 gives | the ledger says |
|---|---|---|
| `the two readings are not reconciled here` | `MEANING-HELD` — a clause naming its own subject, line never changed | `REPAIR-OWED` |
| `What is claimed is the coincidence and not a value` | `MEANING-HELD` | `REPAIR-OWED` |
| `21.8%` | **`DELIBERATE`** — a value | `REPAIR-OWED` |

**Test 5 already says the repair is owed *"including a piece that would be a name or a value on its own."*
So with the clause added, `21.8%` is owed by the test's existing words. It is `DELIBERATE` today only
because the routing dead-ends before reaching them.**

## 6. Scope, stated as a ceiling

An AST sweep of all **1,075** receipts for `check(label, cond)` where the label is a static string
containing *and* and `cond` is a top-level `or`: **67 sites.**

**67 is a ceiling, not a count.** Most use *and* as discourse glue (*"⇒ and it reports the state
disagreement"*) rather than as a claim-level conjunction of the two arms the `or` offers. **Three are
confirmed by the ablation above; 64 are unread.** Separating them needs each arm resolved against the file
it is tested in, which is `measure()`'s work and not a static read — so the ceiling is what can be stated
without a sweep that has not been run.

## 7. Reproducing it

```
python3 computations/beyond_the_wall/r7307_cc66_test6_gap/sweep_and_ablate.py
```

Four parts: the ablation, the Test 4 count history on the flattened read, the AST ceiling, and `PART 4`,
which pins this document to the rule's current text. It exits `0` today and `1` if any number or any of the
four pinned phrases moves.

## 8. What is not claimed

- **Not that Test 6 is wrong.** It decides **six of the nine** disjunction rows in the ledger — the vacuous
  and never-true arms (`3.3`, `rescal`, `scanner`, `CR/LCDM`, `INPUT`, `WITHDRAWN`). It works on five of the
  six arms it was drafted from and misses a sixth shape. **It should keep its present wording.**
- **Not that the 64 unread sites are defective.** They are unread.
- **Not that the ledger's verdict on these three is right for the ledger's reasons.** The ablation is the
  ground offered here, and it is the only one.
