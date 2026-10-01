# r7083 (70) — how many retired ledger rows are invisible to the parsers, and does any live check depend on one?

*Pre-registered before any parser is read in detail, and before the count. The order is `FOR_70.md` `r7083` Q1. **Count and report; no sweep.** No line of `corpus/open_ledger.txt` is edited.*

## What is measured

1. **The true count.** Every comment line of `corpus/open_ledger.txt` that carries a ledger id (10 hex characters, followed by ` | <paper> | <verdict> |`) is counted, in either form:
   - **id-first:** `# <id> | …`
   - **prefixed:** `# ⌗ RETIRED (…): <id> | …`, or any other text before the id.

   For each, I report the lines, the distinct ids, and any id that is also live (an uncommented row), which would be retired and live at once. The figure `check_open_ledger` itself prints for retired rows is set beside it.
2. **The consumers.** These are every `.py` file outside `.git` that reads `open_ledger.txt`. For each I record how it parses comment lines, and whether it uses retired rows at all. If it does, I record what it misses when a retirement is in the prefixed form.
3. **The consequence**, per consumer that uses retired rows:
   - **MISSES:** it reads retired rows, and a prefixed one changes its answer. Each is shown by a scratch-copy run with the prefixed lines converted to id-first, comparing the output. The ledger itself is not edited.
   - **BLIND BUT UNAFFECTED:** it reads retired rows, but no prefixed id is one it would act on today.
   - **DOES NOT USE RETIRED ROWS:** nothing to miss.

## Outcomes, the one that costs another seat most first

1. **A live gate or registered receipt MISSES.** In particular, a re-emission guard that would let a retired row come back as new without failing. This would make the 208 lines a defect, not a tidy. **Predicted: at least one consumer reads retired ids for re-emission or duplicate detection** (`check_open_ledger`, `check_protected_dupes` or `check_withdrawals`). Whether it actually misses today is predicted **yes, for at least one prefixed id**. This is a guess.
2. **Ids both retired and live.** **Predicted: zero to a few.** The reworded-sentence retirements (`cowork review, sentence reworded or removed`) are the likely source, since a rewording can re-hash.
3. **The count.** `r7083` gives 214 non-id-first comment lines against 70 visible. **Predicted:** the distinct prefixed ids number fewer than 214, because some lines are prose without an id or are repeats.
