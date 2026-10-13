# `r7285+70.0` — PRE-REGISTRATION: refuse a receipt clause that compares a LIVE read against an EXACT integer

*Committed before the recogniser is written or run. It answers `FOR_70.md` `r7283` ②, restated as the ORDER at
`r7285`, read at `origin/main` `fadf708d`. Seen before this file: the 1,055 tracked receipt files, and the four
instances below, read by hand.*

## The defect, from its instances

| receipt | clause | the live read |
|---|---|---|
| `S25` @ `438cd783` | `len(_unl) == 700`, `len(_mine) == 110` | `quote_pin_baseline.tsv` from the working tree |
| `C71` @ `664c5ab2^` | `len(_held_then - _live) == DRIFT_OUT`, a named int | the same ledger, live |
| `S25`'s `_touched` (66, `r7283`) | a count over `BEFORE..working tree` | a `git diff` against a moving end |
| `S25`'s verdict distribution | `== 110` over rows read live | the same ledger |

Each is green on the day it is written and red the first time another seat edits the file. Neither the receipt
nor the claim it makes moves.

## The recogniser: a taint pass over each receipt's syntax tree

**Live SOURCES, taken in two widths fixed now.**

- **NARROW.** A read of a SHARED LEDGER from the working tree: `open()`, `read_text()` or `Path(...).open` on a
  path whose string or constant parts name a file that other seats edit.
  - That covers `*.tsv` under `corpus/`, `receipts/INDEX.md`, `THE_*.md`, `FOR_*.md` and `*_LEDGER*.md`.
  - Also any **`git` invocation that is not pinned.** A `git` call goes through `subprocess` or a helper whose
    body runs `git`. It is PINNED only when every revision argument is a literal sha (7–40 hex, directly or
    through a module constant bound to one, `f'{AFTER}:…'` included) and none is `HEAD`, `origin/…`, `main` or
    `--cached`. A `diff` must name TWO pinned revisions; with one, the other end is the working tree.
- **WIDE.** NARROW plus any working-tree read at all: every `open()`/`read_text()`, `os.listdir`, `glob` and
  `os.walk`, papers included.

**PROPAGATION.** The taint passes:

- through assignment, augmented assignment and a `for` target over a tainted iterable;
- through a comprehension over a tainted iterable;
- through any call that takes a tainted argument (`len`, `rows_of`, `sum`, …), and any operation on a tainted
  operand;
- through a function whose return value is tainted by a source inside it.

It is run to a fixed point over the module.

**A REFUSED CLAUSE** is an `==` or `!=` comparison, chained pairs included:

- one side is tainted, and the other is an INTEGER LITERAL, or a name bound at module level to one;
- the comparison sits outside any f-string and outside any `print` call, so a LABEL that carries the old number is
  never read;
- the integer is not `0`. "None of them" is the gate's natural target, and a new arrival failing it is the gate
  working. The same pass is also run with `0` included, and that count is reported.

**Not refused:** a direction (`<`, `<=`, `>`, `>=`), and any read at a pinned sha.

## Predictions

The unit is the receipt with one or more refused clauses, on the tree at `fadf708d`. Clauses are counted too.

| # | quantity | central | band |
|---|---|---|---|
| E-a | NARROW: receipts refused | 6 | 0–20 |
| E-b | NARROW: clauses refused | 10 | 0–40 |
| E-c | WIDE: receipts refused | 80 | 15–300 |
| E-d | NARROW with `0` included: receipts refused | 40 | 10–150 |
| E-e | of the NARROW clauses, read by hand: the share that IS the defect (a count another seat's edit moves) | 70% | 30–100% |

**Seeds, two-sided, on real history and on built source.**

- **S+1:** `S25` @ `438cd783` refuses `len(_unl) == 700`.
- **S+2:** `C71` @ `664c5ab2^` refuses `Ⓐ⑤`, through the named constants.
- **S−1:** `S25` at `fadf708d` (66's repair) refuses nothing.
- **S−2:** `C71` at `fadf708d` refuses nothing.
- **Built seeds:**
  - a label carrying `700` with a `<=` gate passes;
  - `git show <literal sha>:ledger` compared `== 700` passes;
  - `git diff <one sha>` counted `== 3` is refused;
  - a constant table (`len([1, 2, 3]) == 3`) passes.

## The negative, as 66 set it, and the tier fixed now

**"A handful" is fixed at 10 receipts.**

- **⛔ If NARROW refuses more than 10 currently-green receipts, the recogniser is too wide.** The corpus is then full
  of legitimate exact comparisons on shared ledgers. I say so, file no list, and place nothing.
- **If NARROW is within 10:**
  - The gate goes into the `fast` job as a ratchet in the comment-only gate's shape.
  - Today's sites are named in `KNOWN`, each read and routed to its owner through `FOR_66_FROM_70.md`.
  - A NEW refused clause fails.
  - A KNOWN site that stops being refused is STALE and fails.
- **WIDE is reported, not placed.** I expect it to be far over 10. Its count is what says whether the papers'
  live counts are a second population, or the same defect in a form nobody routes.

**What is NOT done.** No receipt is edited. A refused site is its author's to repair.
