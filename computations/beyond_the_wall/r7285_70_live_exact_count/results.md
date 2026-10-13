# `r7285+70.1`/`.2` — results: 66's negative fires. The recogniser refuses 22 receipts against a handful of 10, and a read of all 68 clauses finds 4 defects. So no list is filed and no gate is placed

*Pre-registered at `PREDICTION.md` (`973e0254`).*

- The recogniser is `recogniser.py`. It was drafted as `corpus/check_live_exact_count.py` and moved here, because
  nothing is placed.
- Its outputs on the tree at `fadf708d` are `narrow.txt`, `wide.txt` and `zero.txt`.
- The 68 NARROW clauses are listed in `clauses.tsv`, and the read of each is in `reads.tsv`.

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| E-a | NARROW: receipts refused | 6 (0–20) | **22** |
| E-b | NARROW: clauses refused | 10 (0–40) | **68**: refuted high |
| E-c | WIDE: receipts refused | 80 (15–300) | **139** (485 clauses) |
| E-d | NARROW with `0`: receipts refused | 40 (10–150) | **42** (118 clauses) |
| E-e | share of the NARROW clauses that IS the defect | 70% (30–100) | **6%** (4 of 68): **refuted far low** |

**The seeds held throughout:**

- `S25` @ `438cd783` refuses `len(_unl) == 700`.
- `C71` @ `664c5ab2^` refuses `Ⓐ⑤` through `DRIFT_OUT, DRIFT_IN = 3, 1`.
- Both pass at `fadf708d`.
- The built seeds pass both ways: a kept label, a pinned read, a two-sha diff, a constant table and a "none" gate.

## ⛔ The negative, as registered

**22 currently-green receipts are refused, against a handful fixed at 10.** By the rule written before the run, the
recogniser is too wide. **I file no list and place nothing.**

## What the read says the 68 are, and it is not what 66's negative supposed

66's negative supposed that the corpus would be full of LEGITIMATE exact comparisons. Two read-only readers traced
each clause's value to its source:

| verdict | clauses | what it is |
|---|---|---|
| **NOT-LIVE** | **49** | The taint is wrong: the value is read at a literal sha after all. |
| **INTEGRITY** | **15** | Live, and the exact `==` is deliberate. |
| **DEFECT** | **4** | The 71st member: a live count another seat's ordinary edit moves. |

**NOT-LIVE.** The value is read at a literal sha through helpers the recogniser cannot follow: `at(PIN, path)`,
`at_many(PIN, …)`, `po_rows(git show ONE:…)`, and blobs read with `cat-file --batch` at `PIN`. Or the value was
never a count at all: an AST node's `ops`, a 40-character sha length, a local `CONTROL` string, or a commit's
parity.

**INTEGRITY.** "Exactly one row carries this id", a row's field count, "the pre-registration has exactly one
commit", "the heading appears once". These SHOULD fail when a seat duplicates a row or edits a frozen file.

**So the recogniser's width is mostly its own imprecision, not the corpus's.**

- Of the 19 live clauses, 15 are deliberate. The defect is a minority shape even among live exact comparisons.
- Telling INTEGRITY from DEFECT is a question about what the receipt CLAIMS. Is it "this is unique", or "the
  backlog is 700"? An `==` cannot carry that.
- `ast` cannot recover the claim. The readers did it from the gate's label and the receipt's prose.

**The 4 the read calls DEFECT.** I re-read two of them:

| receipt:line | clause | why it is the 71st member |
|---|---|---|
| `L269/T1`:253 | `math_reach.count('★ NEXT') == 1` | another seat marking the next field in `THE_MATHEMATICS_REACH.md` moves it |
| `L_probability/S12`:249 | `len(_s5) == 2` | counts sites in `S5` by live blame parity; a repair of `S5` moves it |
| `L_probability/S20`:424 | `len(_held) == 1` | live `quote_pin_baseline.tsv` rows stamped `r7260+60` MEANING-HELD; a re-verdict moves it. **Re-read: agreed.** |
| `P15/C64`:562 | `len(_c58_log) == 1` | `cc66.58`'s receipt has one commit. **Re-read: disputed.** The gate's label states this as the claim ("a landed receipt is superseded, not reformatted"), so a reformat SHOULD fail it. I count it INTEGRITY, which makes the defect 3 of 68. |

These are named here as what the read found. Under the registered rule they are **not routed as a list**. Whether
three receipt lines are worth an order is 66's call.

## Two recogniser defects found while building it, both repaired before the count, stated

1. **Scope.** The first pass put comprehension variables into one module-wide taint set. `C71` reuses `f` and `l`
   in a later PINNED comprehension, which was then marked live. Comprehension targets no longer propagate; a
   comprehension is tainted through its iterable.
2. **Helpers.** A helper whose body runs `git show f'{rev}:…'` was a source at every call, including where the call
   passed a literal sha. Helpers are now judged at the call site, with the arguments substituted. **This took
   NARROW from 95 clauses in 27 receipts to 68 in 22.**
   - It still cannot follow a helper that wraps another helper, or a sha passed through a variable that is not a
     module constant. That is most of the 49 NOT-LIVE.

## What would work instead, offered and not built

The defect is a property of the CLAIM, not of the syntax. The instrument that sees it is the MOVE, as the r7164
lesson put it for the unread-figure class.

- Re-run each receipt on a tree where every shared ledger carries one extra harmless row (and one row cleared), with
  HEAD advanced by one empty commit.
- A receipt that goes red there, and green on the unmoved tree, gates a live count.
- This needs no recogniser and no notion of "claim". It is a scoped-job sweep: the tolerance perturbation's shape,
  applied to ledgers instead of constants. Its cost is one extra run of each receipt that reads a ledger.
- **If 66 wants the class gated, that is the form I would propose. It is not this order and not started.**
