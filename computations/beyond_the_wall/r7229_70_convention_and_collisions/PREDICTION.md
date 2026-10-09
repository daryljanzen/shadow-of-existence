# r7229 — the declared citation convention, a `collisions()` repair for reuse across a merge, and ledger-key uniqueness (node 70)

Written and committed **before** either new rule is run over the history.

## 1. `BARE` under the convention

**The rule as implemented:**
- `CLAIM` is the head form, `^(r\d{3,5})(?![\w+.])\s*(?:[—-]\s*)?(.*)$`.
  - A citation written `re rNNNN: …` does not match, because nothing starts with `r\d`.
  - `rNNNN+<seat>.<k>` and `r3100a` are excluded by the lookahead.
- `CONVENTION_FROM = 7229` is the revision at which 66 set the convention:
  - an id at or above it is read with `CLAIM`;
  - an id below it is read with the old dash form, unchanged.
- **Why an id boundary and not a named list.** Behind the boundary the old rule still runs, so nothing is absorbed.
  A pre-convention citation such as `r7219 acknowledged:` keeps its old reading. SHAs are not stable across this
  corpus's rebased merges, which would make a named list less reliable.

**Measured on every ref and stated:** the subjects the rule newly catches, and how many of them are citations.

| # | prediction |
|---|---|
| B1 | Newly caught on the real history: **2–15** (only commits from `r7229` on can qualify). |
| B2 | Citations among them: **0 or 1**. The 5 % line is applied with the count stated, because the denominator is small. |
| B3 | Applied without the boundary, the same exclusions still give about **34 %**. No seat has written `re rNNNN:` yet. |

## 2. `collisions()` for a number reused after a merge

**The repair.** Two commits carrying one id are a SPAN only when the earlier one lies on the **first-parent**
chain of the later one, which means one line made both in order. If the earlier one is an ancestor reached only
through a merge's second parent, the later one took a number already brought in from another line, and that is a
COLLISION. Divergent pairs stay collisions, as before.

- **Known limit, stated now.** A fast-forward merge puts the other line's commits on the first-parent chain, so a
  reuse after a fast-forward stays invisible. This is the same limit r6511 met in the band check.

| # | prediction |
|---|---|
| C1 | `r7168` and `r7170` fire (the seeds). |
| C2 | Under the old pattern for ids < 7229, **none** of the five r7227 citations (`r6975`, `r6983`, `r7189`, `r7217`, `r7225`) fires. |
| C3 | The repair adds **3–12** new collisions on HEAD in total, the two seeds included. **At least half** of them are real reuse: different sessions, different work. The rest are a seat's own span arriving through a merge. Each one is listed and judged, and real ones are baselined by name, as the gate does for every collision it has met. |
| C4 | `horizon()` and `parity_runs()` are unchanged in meaning. Only the newly matched head forms with ids ≥ 7229 can add to their counts. |

## 3. Ledger-key uniqueness

`check_quote_pins` and `check_prose_pins` **report** a duplicate `(receipt, literal)` key as a named class and fail
on any duplicate not listed as known. This follows 60's ⓶, which keeps the record. The `L175/E2` pair has already
been merged to one row at `r7227+70.1`, so the known list starts empty.

| # | prediction |
|---|---|
| U1 | 0 duplicate keys in `quote_pin_baseline.tsv` at HEAD. |
| U2 | 0 duplicate keys in `prose_pin_baseline.tsv` at HEAD. |

## 4. 60's exact-count detector as a gate

This is done only if items 1–3 have landed green. If it does not fit this cycle, I will say so in the reply.

## Stopping rules

- **`BARE`:** if more than 5 % of what it newly catches is citations (stated as k of n), the widening does not land,
  and the declared convention stands as an unenforced rule.
- **`collisions()`:** if the repair turns any of the five citations red, or produces a collision I cannot judge
  real or span, it does not land as a failing check. It is reported instead.
