# ⛔⛔ `r7345+cc66.2` — RULING ⒝ DOES NOT LAND CORPUS-WIDE AND MY OWN RECOMMENDATION FOR IT IS REFUTED: THE `_SELF` SIBLING DROPS `485` EXISTING KEYS, `334` OF THEM ADJUDICATED `DELIBERATE`. IT IS CLEAN HOP-SCOPED — `9` CAUGHT, `0` OVER-CAUGHT — AND SHOULD LAND WITH THE HOP, NOT BEFORE IT

*`r7345` ⒝ ordered this landed: **"It completes a filter already adjudicated rather than proposing a fifth
narrowing, so it is not another fit and needs no held-out test. Land it."** I implemented it, measured it
against the whole corpus as I said at `READING.md` ⑥ ① was the first thing to do, and it fails `r7345`'s
own ⒟ bar by a wide margin. **Nothing is landed in `scripts/`. The measurement is the deliverable.***

## ① ⛔ FIRST, THE CLAIM OF MINE THAT FALLS

`READING.md` ⑥ ①: *"This is worth doing **whether or not the hop lands**: it is a hole in the instrument as
it stands today, not an artefact of the hop. `14` keys here; **its effect on the existing `2772` is
unmeasured and is the first thing to measure.**"* ⇒ **I measured it, and the sentence before it is wrong.
It is not worth doing whether or not the hop lands. It is only coherent inside the hop.**

## ② THE RULE, STATED AS THREE MECHANISM TESTS

`_SELF` excludes a container that reads the receipt's **own** source (`open(__file__)`). The sibling
excludes one that reads **another receipt's source as text**:

| | test | why |
|---|---|---|
| ⓐ | the narrow trace's kinds are **exactly** `{py}` | `tex` or `md` beside it is `_rstar`'s own `UNDECIDED` shape, so decide nothing |
| ⓑ | the trace shows a **text read** — `splitlines`, `split('\n')`, `readlines`, `open(`, `cat-file`, `git('show'`, `git('grep'` | a source read as text, not as a module |
| ⓒ | **not** an import (`ModuleType`, `exec_module`, `spec_from_file_location`, `importlib`) and **not** a path used only as a dict **key** (`[... '.py']`) | an imported module's namespace is not source text, and a path used as a key is not a file this container reads |

*All three are tests on the **narrow** trace, the object that decides key-hood — which is available, per
this phase's `CORRECTION.md`.*

## ③ ⛭ HOP-SCOPED IT IS CLEAN, AND BETTER THAN ANY SHAPE RULE MEASURED SO FAR

Scored against the hand-judged class of `14`, on the hop population of `121`:

| rule | caught | hit | over-caught | missed |
|---|---|---|---|---|
| narrow kinds `== {py}` alone | `11` | `9` | `2` | `5` |
| `{py}` + linewise | `9` | `8` | `1` | `6` |
| `py ∈ kinds` + linewise | `11` | `9` | `2` | `5` |
| `({py}` or no kind`)` + linewise/blob | `36` | `12` | ⛔ `24` | `2` |
| **ⓐ∧ⓑ∧ⓒ above** | **`9`** | **`9`** | **`0`** | `5` |

⇒ ***`0` genuine keys forgone, which is exactly the half of your ⒟ bar that cannot be bought by tuning.***
**The `5` residual keys, named as ⒟ requires:**

- `C1_the_uptake_is_falling…`, `'C1_…_why.py'` — ⛔ **misfiled by me, not missed by the rule.** Its
  container is an `INDEX.md` row, not a source; the key is imprecise because *a filename is not a
  quotation*, which is a literal judgement and not a container one. **It does not belong in class ⒜.**
- `S10_the_sweep…` ×`3` and `C60_the_hier…` ×`1` — the container's path is a **variable** (`S2REL`,
  `_INSTR`) that the narrow trace does not resolve at its depth of `3`. *A stated mechanical limit of the
  trace, not a disagreement about the keys.*

## ④ ⛔⛔ AND CORPUS-WIDE IT IS A DISASTER, WHICH IS WHY IT CANNOT LAND AS ORDERED

The filter is not hop-scoped by construction: it tests the container, so it applies to **every** key. On
the base extractor — the one the ratchet actually reads, since the hop is reverted — it drops **`485` of
`2736`** existing keys, `17.7 %` of the ledger. **By current verdict:**

| verdict | keys dropped |
|---|---|
| ⛔ `DELIBERATE` | **`334`** |
| `EXTENDED` | `55` |
| `REPAIR-OWED` | `47` |
| `NOT-A-PIN` | `16` |
| `ALT-OK` | `16` |
| `MEANING-HELD` | `9` |
| `ENCODING-OK` | `8` |

*All `485` are `SOURCE` target: `312` `SENTENCE`, `173` `TOKEN`.* ⇒ ***It would delete `334` keys the corpus
has explicitly adjudicated as deliberate pins, against `16` it has called `NOT-A-PIN`.*** Reading them
settles it — they are other receipts' **stated claims**, quoted as wording: *`'the corpus's colour is the
CENTRE and its structure…'`, `'reached three independent ways'`, `'nothing in the identity says which of
them…'`, `'THE TOWER IS INFINITE: one bound zero-mode…'`.* **That is a seat's prose, and it is pinned 485
times.**

⇒ ⛭ ***So `_SELF`'s asymmetry is not an oversight, and that is the thing I had wrong: `_SELF` excludes a
receipt reading its OWN source because self-reference proves nothing. Reading ANOTHER receipt's source is a
legitimate cross-check, and the corpus does it `485` times.*** **The two are not siblings. They are
opposites that happen to share a mechanism.**

## ⑤ WHAT I RECOMMEND

**⒝ is sound exactly where it was found and nowhere else.** ⇒ ⑴ **Scope it to the hop** — apply it only
where a key exists *because* the hop created it, where it is `9` caught, `0` over-caught, `5` named; ⑵ ⛔
**therefore land it WITH the hop and not before**: the hop is reverted, so a corpus-wide filter has no hop
keys to act on and only the `485` to destroy; ⑶ ⌗ *and the `485` are a result of their own, independent of
the hop: **`485` keys pin another receipt's prose, `334` of them deliberately.** That is a population no
one has named, and it is the obvious held-out candidate for ⒞ — a corpus-wide class the container rule was
never fitted to.*

⛔ **Conflict named rather than resolved by me:** ⒝ says land it, ⒟ says zero genuine keys forgone, and
corpus-wide those two cannot both hold. *I have landed nothing and the numbers are above.*
