# `r7251+70.2` — results: a string repair form for a paper-meaning pin does not exist in the skeleton family

*Pre-registered at `PREDICTION.md` (`dedfdc8f`). The draw is `draw.py` → `draw.txt`. The forms and every
mutation, written out in full, are in `skeleton.py` → `skeleton.txt`. The population's shape is `shape_count.py`
→ `shape_count.txt`.*

## The draw

The seed was `0x3bf0ac52`, taken from the order's commit. It drew 3 of the 162:

| member | literal | words | quartile | its receipt's share |
|---|---|---|---|---|
| `B2` | `complex conjugation of the pair` | 5 | Q1 | 6 / 162 |
| `B8` | `the module the operator's colour structure acts on is the branch` | 11 | Q4 | 5 / 162 |
| `B37` | `quantises without measuring` | 3 | Q1 | 2 / 162 |

The draws span two quartiles, so the fourth-draw rule did not fire.

## The measurement

Each member was run three ways:

- **(a)** on the paper as it stands;
- **(b)** on content-intact rewordings, which must stay green: markup, synonym, reorder, a split, and "not X
  but Y";
- **(c)** on content-breaking edits, which must go red: converse, polarity flipped or dropped, object swapped,
  regimes exchanged, restriction inverted.

For (c), every OTHER sentence that states the finding is removed too, so the edit really makes the finding false
in the paper. `matter_sector_paper.tex` states the `B8` finding twice.

| form | members passing (a)–(c) | (b) green | (c) red |
|---|---|---|---|
| **the registered skeleton** (sentence scope, unordered) | **0 / 3** | 13 / 13 | **4 / 10** |
| variant 1, not registered (clause scope, unordered) | 0 / 3 | 5 / 13 | 8 / 10 |
| variant 2, not registered (sentence scope, ordered) | 1 / 3 | 11 / 13 | 7 / 10 |

**Every gain in one column is paid for in the other.**

- **The registered form never reds on a rewording, and it misses 6 of 10 breaks.** It cannot see the
  converse ("is a bundle of the substrate rather than the branching", "the winding measures without
  quantising"). It cannot see exchanged regimes, or an inverted restriction. And it cannot see a polarity
  marker used elsewhere in the same sentence: "without" occurs three times in `B37`'s sentence, and "rather
  than" twice in `B8`'s.
- **Scoping to a clause** fixes the polarity scope but breaks `B2` outright. Its finding spans the dash-set
  apposition, so (a) is red.
- **Ordering the tokens** catches `B8`'s converse, but reds on content-intact reorderings ("without
  measuring, the winding quantises"), and it still misses `B2`'s inverted restriction.

## The predictions

| # | predicted | measured | |
|---|---|---|---|
| R1, members passing | 2 (1–3) | **0** | **REFUTED** |
| R2, (b) green rate | 90% (75–100) | 100% | held |
| R3, (c) red rate | 80% (60–100) | **40%** | **REFUTED LOW** |
| R4, failure shape | relational direction carried by word order | converse, regime and restriction inversions, **and** polarity scope | held, with a second shape I did not name |

## Is the failure structural? The count the pre-registration required

- **A bag of tokens cannot see a converse, by construction.** The converse has the same tokens and the same
  polarity.
- **A form that sees the converse must read word order or syntax.** The only order-reading form tried (variant
  2) reds on reorderings that keep the content, because English carries direction in syntax, not in token
  order.
- **So within string matching the trade-off is forced, and only a parser could escape it.** A parser was not
  tried, and nothing here rules one out.

**How much of the population has the shape:** `shape_count.py`, with its rule stated in the file.

- **105 of the 162 (65%)** carry an explicit polarity or contrast marker (63) or a copular identification (42).
- **Of the other 57**, a hand sample of 12 shows 9 with a directed verb ("designates", "generate", "returns",
  "fixing", "vanishes at"). Only 3 are bare noun phrases ("a domain wall", "the Cartan--Weyl skeleton").
- **Extrapolated, about 90% of the 162 state a directed relation.** About 10% are bare terms.

The bare terms are not really meaning pins. A content-intact rewording keeps a term, so under ① they behave as
`TOKEN` keys.

## The verdict: the reachable negative fires, inside the stated scope

**For about nine in ten of the 162, no string repair form exists that both survives a content-intact rewording
and reds when the finding goes false.** I tried three forms on a seeded draw. Each one fails in one direction or
the other. The failure is the converse, which keeps every token.

⇒ **On those keys, `REPAIR-OWED` names work no string gate can do. That is 66's 48th member: a classification
wearing an order's clothes.**

**What I propose, for 66 to decide:** a sixth verdict, **`MEANING-HELD`**, counted and not owed.

- The finding is about what a paper means, and it is held at its commit by L-249's historical half.
- The live string assertion is kept as a **READ TRIGGER**, not a guard. When it reds, someone reads the
  sentence. The red does not mean the finding is false.
- The roughly 10% bare-term keys go back to `TOKEN` treatment under ①.

**What this does NOT establish:**

- That a syntactic or semantic gate cannot exist. None was tried.
- That the other 159 behave like the three. The shape count is a lexical upper bound plus a sample of 12.

## Two harness defects, found and fixed before the numbers above

1. **The first run edited only the one sentence.** `B8`'s finding is stated twice, so its breaking edits
   left the finding true.
2. **My first fix for that split on `;` and `:`.** It deleted fragments of the edited sentence itself, which
   made two members look like passes.

The table above is from the run with both defects fixed. The registered form's first figures (2 of 3 passing,
(c) at 70%) were artefacts of defect 2.
