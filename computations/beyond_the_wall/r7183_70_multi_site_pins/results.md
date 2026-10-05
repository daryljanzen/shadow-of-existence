# r7183+70.1 — results against `PREDICTION.md`

## Answer

**About one receipt literal pin in five is a pin on its FILE and not its CLAIM**: 139 of the 722 pins present in
their paper occur twice or more.
- **Hand-read sample of 20:** 8 are AMBIGUOUS (the copies make different claims) and 12 are RESTATEMENTS.  7 of the 8
  AMBIGUOUS are short or generic strings.
- **The explainer is worse in proportion: 8 of its 18 literals are MULTI-SITE**, including, before `r7183`, the
  `by three independent routes` pin that stayed green (D1).

## Section or neighbourhood? Measured, both

| | MULTI-SITE | SECTION-UNIQUE (every copy in a different section) | SECTION-SHARED (two copies in one section) |
|---|---|---|---|
| receipt pins | 139 | 65 (47%) | 74 (53%) |
| explainer pins | 8 | 5 | 3 |

⇒ **A section-scoped pin would make about half of them single-site.**  The other half repeat inside one section, so
only a neighbourhood (the sentence or paragraph, as `P1`'s sentence-scoped anchor does) separates them.  *A section
scope is necessary for this class, but it is not sufficient.*

## Scored

| | predicted | measured | |
|---|---|---|---|
| D1 recall at `7a31b31f^` | the stale explainer pin flagged | `by three independent routes`: 2 occurrences, flagged | held |
| D2 receipt pin population | 1,500-4,000 | **1,046** | **MISSED** (low) |
| D2 MULTI-SITE share | 10-25% | 19.3% (139 of 722 present) | held |
| D3 AMBIGUOUS in 20 | 8-14 | 8 | held (at the edge) |
| D4 explainer MULTI-SITE | 1-5 | **8 of 18** | **MISSED** (high) |

## Not a finding

- 324 of the 1,046 receipt pins are not found by this counter.  Its normalisation (whitespace collapsed, comments
  stripped) is not each receipt's own, so **those 324 are not claimed to be absent from their papers**.  They are
  outside this measurement.
- No pin, receipt or marker is edited.
