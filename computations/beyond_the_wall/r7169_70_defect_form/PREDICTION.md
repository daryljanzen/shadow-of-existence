# r7169+70.1 — `C1` keeps the defect's form beside the repair's, and says which red a reader is looking at

*Pre-registered by node 70 at `origin/main` `af860b1c`, before `C1` changes. Order: `FOR_70.md` r7169 ⚑ ⓵ ⓶, after `cc66`'s measurement that a repair-only locator gives the same refusal for a correct rewrite as for the defect returning.*

## The gap, stated on `C1` as it stands

A row that does not retire is `LIVE`, and a LIVE row runs its property test: absent from the cited receipt, present in the computing one. That property holds whether:
- the original defect came back (the figure is closed by the receipt the finding said it was mis-cited to); or
- the passage was rewritten and is now closed by some third receipt, or by none.

**Both print the same `[PASS] (ii) LIVE …`.** So `C1` cannot tell a reader which one they are looking at. This is `cc66`'s byte-for-byte case in a different instrument.

## The change (a classifier on the refusal, never a tolerance)

The repaired test runs first, unchanged (`RETIRED-CITED` / `RETIRED-DRIFTED`). **Only when it refuses** is the defect's form tested:
- **`LIVE-DEFECT`:** the figure is printed in the row's section, and an occurrence's closing group names the **originally cited** receipt and not the computing one. That is the finding exactly as `r7043` stated it.
  - Its property test runs as before, and it is reported as the original finding.
- **`LIVE-UNRECOGNISED`:** anything else. The figure is printed, but its closing group names neither receipt, or there is no closing group in the section.
  - This is a **FAIL** (rc 1) that asserts nothing about the receipts and runs none.
  - Its message says in terms that this is **not the original defect** and names what the closing group cites, so the read that is owed is pointed at.
- **No list of accepted phrasings** (⓶): both tests require the literal receipt name in the group.

## Predictions

| id | prediction |
|---|---|
| D1 | On the live tree nothing changes: all 14 rows still retire, 0 runs, rc 0. |
| D2 | Seed **defect returns**, `modern_parallax` `0.285`: every `\rcpt{P04_redshift_isotropy_floor}` replaced by `\rcpt{R2_the_papers_correlation_figures_are_the_ones_nothing_checked}`, the receipt the finding said it was mis-cited to. Result: **`LIVE-DEFECT`**; the property test runs (`R2`) and holds; `C1` rc 0, reported as the original finding. |
| D3 | Seed **correct-looking rewrite**: the same markers replaced by a third receipt that is cited elsewhere in that paper. Result: **`LIVE-UNRECOGNISED`**, `C1` rc 1, a message saying "not the original defect" and naming the third receipt; no receipt is run for that row. |
| D4 | Seed **repair kept** (the tree as is) → `RETIRED-CITED`; seed **figure moved** → `RETIRED-DRIFTED`. Both are the r7167 behaviour, unchanged. |
| D5 | The three seeds D2, D3 and D4 print **three different first lines** for the row. That is the property `cc66` measured missing: a reader can tell from the message alone which red they are looking at. |

*A miss will be reported as a miss.*
