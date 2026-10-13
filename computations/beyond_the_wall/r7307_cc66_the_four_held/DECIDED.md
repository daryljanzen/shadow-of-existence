# The four held rows, against the grounds that now exist

**The order** (`r7307` item ②): *"They leave the list when they are decided with a ground, and the two
grounds that now exist (`69`'s `G1`–`G7` and your own two ruled clauses) are the material to decide them
with. If any of the four falls to a ground already written, say which ground and it is decided; if none does,
that is the finding."*

**Result: three of the four are decided, one of them against this seat's own verdict, and the fourth falls to
no written ground for a reason that can be stated exactly.**

| # | key | was | decided | ground |
|---|---|---|---|---|
| 1 | `RESTATES THE RULE IT GUARDS` (`L270/V1`) | mine `REPAIR-OWED`, `69` `DELIBERATE` | **`DELIBERATE`** | **step 2**, third branch — **`69` is right** |
| 2 | `WHAT IT CANNOT DO` (`L280/D1`) | mine `REPAIR-OWED`, `69` `DELIBERATE` | **`REPAIR-OWED`** | **Test 2**, the pronoun `IT` |
| 3 | `load-bearing claim from a passing remark` (`L280/D1`) | mine `REPAIR-OWED`, `69` `DELIBERATE` | **held** | **none — this is the finding** |
| 4 | `ARITHMETIC OF THE OLD PROBE` (`L561/C1`) | mine `REPAIR-OWED`, `69` `DELIBERATE` | **`REPAIR-OWED`** | **Test 5**, a ground neither seat cited |

Every claim below is read from the receipt itself, which is what the rule requires: *"The claim is the
receipt's, never the reader's."* Each literal's occurrence count and count history were measured, because
step 2's exemption is conditioned on a single stable line.

| key | site | raw count | commits touching the file | distinct counts over history |
|---|---|---|---|---|
| `RESTATES THE RULE IT GUARDS` | `corpus/check_glyph_coverage.py` | 1 | 2 | `[1]` |
| `WHAT IT CANNOT DO` | `corpus/decidable_claims.py` | 1 | 1 | `[1]` |
| `load-bearing claim…` | `corpus/decidable_claims.py` | 1 | 1 | `[1]` |
| `ARITHMETIC OF THE OLD PROBE` | `…L207_the_bend/W1_…py` | 1 | 8 | `[0, 1]` |

**All four meet step 2's line condition, so none of them escapes step 2 on the count** — which means each is
decided by what its own receipt claims, and nothing else.

---

## 1. `RESTATES THE RULE IT GUARDS` — `DELIBERATE`. I was wrong

`V1`'s claim for this key: **`'⓷ᵈ and the finding is recorded IN THE GATE, not only here'`**.

Step 2's third branch: *"a live tool's own words, when the claim is about the words: the check says the tool
`states`, **`records`**, `prints`, or `was left untouched` — then the unchanged text is exactly the claim."*
**The claim's verb is `recorded`, which step 2 names.** One stable line, count 1 at both commits that ever
touched the file.

My `r7293` reading — *DANGLING at ⓵, the span opens on the finite verb `RESTATES` and its subject `A GATE
THAT` is outside* — **is correct as grammar and is not the question.** Step 2 is reached **before** step 3's
tests, and a span whose claim is only that this text stands where it stands never reaches the subject rule.

⌗ **This is the same error I corrected at `r7289`, running the other way.** There I let a valid `held at`
decide a row the ordered test disposes of first; here I let the ordered test decide a row the rule's own
*order* disposes of first. The lesson generalises past both: **a test is only reached if nothing earlier
decides.**

## 2. `WHAT IT CANNOT DO` — `REPAIR-OWED` by Test 2, and step 2 cannot reach it

`D1`'s claim: **`'⓵ᵇ and it says so in its own head: it cannot tell a true claim from a false one, nor a
load-bearing one from a passing remark'`** — it names **two propositions**, and this span is the section
**heading above them**, which is neither of them.

So step 2's governing condition — *"and the claim is only that this text stands where it stands"* — **fails
however the heading's own status is read**, because the claim is about two sentences and this is not one of
them. Test 2 then fires squarely: *"a pronoun: **it**, they, them…"* — the subject of `cannot do` is `IT` and
its antecedent, the instrument, is outside the span. Test 5 fires as well (three arms required together on
`dc_src`, nothing joining them).

⌗ **Step 1 was considered and declined.** It exempts *"a pattern that **finds** a structure — a heading, a
label…"*, and `D1` does not locate anything with this string; it asserts that the instrument says it. The
pin's **role** is assertive, and step 1 is about role, not about whether the text happens to be a heading.

## 3. `load-bearing claim from a passing remark` — held, and the question is nameable

**This span IS one of the two propositions the claim names**, so unlike its sibling arm it *does* reach step
2's third branch. Whether step 2 exempts it turns on a question `THE_RULE.md` does not settle:

> **When a claim has the form `the tool SAYS <proposition>`, is that a claim about the TEXT or about the
> PROPOSITION?**

- **About the text** → step 2 exempts → `DELIBERATE`, which is `69`'s call.
- **About the proposition** → step 2's condition fails → **Test 1's first bullet fires**, because `it cannot
  tell a` — the subject and the finite verb — is outside the span.

Both readings are available on the written text and nothing in the rule chooses. **That is the finding for
this row**, and it is one question rather than a dispute: answer it once and this row and a class of others
go with it.

⌗ Test 1's **third** bullet was considered and does **not** fire. `cannot` governs the span from outside, but
the bullet requires the span *read alone* to assert what the sentence denies, and two bare noun phrases
assert nothing.

## 4. `ARITHMETIC OF THE OLD PROBE` — `REPAIR-OWED` by Test 5, which neither seat cited

`C1`'s claim: **`'⓹ W1 carries the corrected claim-level measurement AND the old verbatim count BESIDE IT,
so the error is legible rather than erased'`**. The check:

```python
'CORRECTED c54.228 (`L-561`), AND THE CORRECTION IS A' in w1 and 'ARITHMETIC OF THE OLD PROBE' in w1
```

**`BESIDE IT` is the whole of the claim, and two disjoint membership tests on one file cannot establish
adjacency** — the two strings could sit in unrelated paragraphs and the check would still pass. That is Test
5 verbatim: *"Two or more pieces are required together and nothing joins them."* And Test 5 overrides the
name exemption in its own words: *"the repair is owed on **every** piece, including a piece that would be a
name or a value on its own."*

Step 2 does not reach it: the claim is not that this text stands where it stands, but that **two** texts stand
beside each other.

⇒ **By Test 5's own wording the repair is owed on the OTHER arm too, which no seat has flagged.** That arm is
reported here rather than re-verdicted, because it is not one of the four.

---

## What this says about the two seats' disagreement

`r7303`'s pooled measurement put this seat `15` points more `REPAIR-OWED` than either other, one-sidedly.
**On these four the written grounds split `2`–`1`–`1`: two my way, one `69`'s way, one open.** The one that
went `69`'s way went there because I applied a test the rule's *order* had already foreclosed — which is a
threshold difference with a mechanism, not a taste. **Of the two that went my way, one rests on a test
neither seat had cited.** So the gap is not simply this seat reading harder: on these four it is two seats
each reaching for the test they drafted and neither working the order.
