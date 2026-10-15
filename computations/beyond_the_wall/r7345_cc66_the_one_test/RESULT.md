# ⛔ `r7345+cc66.5` — THE ONE TEST IS SCORED AND THE RULE FAILS: `0` genuine keys forgone on held-out `B`, but `7` non-pins kept. ⛭ AND THE FAILURE IS SYMMETRIC — `6` in `A`, `7` in `B` — so it is NOT overfitting; it is under-coverage with ONE named cause. ⇒ THE HOP IS ABANDONED PER ⒞, AND THE LIMIT IS `13` KEYS AND NOT `118`

*Scored once, against the rule frozen in `DECLARATION.md` (commit `5d45a20e0`) and the labels frozen in
commit `7db5db61c`. `score.py` in this directory reproduces every number from those two commits alone.*

## ① THE SCORE

| half | keys | rule excludes | ⛔ **genuine forgone** | ⛔ **non-pins kept** |
|---|---|---|---|---|
| `A` (declaration) | `58` | `15` | **`0`** | `6` |
| **`B` (held out)** | **`59`** | **`9`** | **`0`** | ⛔ **`7`** |

**Bar ⒟, both halves required:** *zero genuine keys forgone* — ✔ **PASSES, on both halves**; *every
imprecise key individually named and excluded* — ⛔ **FAILS: `7` non-pins kept in `B`.**

⇒ ***`r7345` ⒞: "If it fails on the held-out half, the hop is abandoned with its measurement." IT FAILED.
THE HOP IS ABANDONED.*** *I am not going to argue with the ruling after the fact, and ⒞ said in advance
that this outcome is acceptable rather than a failure. What follows is the measurement it is abandoned
with.*

## ② ⛭ THE FAILURE IS SYMMETRIC, WHICH REFUTES THE DIAGNOSIS THE WHOLE TEST WAS DESIGNED AROUND

**`6` of `58` in `A` against `7` of `59` in `B` — `10.3 %` against `11.9 %`.** *A rule fitted to `A`'s
residue would have scored near-perfectly on `A` and badly on `B`. This one scores the same on both.*

⇒ ⛭ ***So the thing that defeats the container rule is NOT the fitting I diagnosed at `r7343` and `66`
ratified at `r7345` ①. The four narrowings were fits, and stopping them was right, but they were not what
was failing here: this rule, declared once and never tuned, fails by UNDER-COVERAGE at the same rate on
data it was written from and data it never saw.***

## ③ AND THE UNDER-COVERAGE HAS ONE CAUSE, COUNTED

Over both halves, `13` non-pins are kept. **`11` of the `13` have an EMPTY narrow kind set** — the trace
names no file at all — and **every exclusion in the declaration is gated on kinds**, so no container rule
can reach them:

| | kinds | key |
|---|---|---|
| ⛔ | *none* | `S10` `'"{}"'`, `'_FELL_BY, _FROM = 66, 2236'`, `'len(UNADJ) <= 2170'` |
| ⛔ | *none* | `S25`/`S32`/`S37`/`S38` `'r7270+60'`, `'r7296+60'`, `'r7310+60'`, `'r7312+60'` |
| ⛔ | *none* | `S36` `'+60'`, `C65` `'r7247+cc66.167'` |
| ⛔ | *none* | `C60` `'Hl_of(e) if LEAFPERT else Hc_of(e)'`, `V1` `'PO-'` |
| ⌗ | `md,py` | `C1` `'C1_…_why.py'` — a filename; container is an `INDEX.md` row |
| ⌗ | `tsv` | `S3` the ledger **key-column** path |

*Only the last two are residuals a container rule could in principle reach, and both were already named in
`READING.md` ③ before this test existed.*

⌗ **And the empty-kind class is where the non-pins live: of the `28` keys with no kind, `11` are non-pins —
`39 %`, against `37` of `117` = `32 %` corpus-wide for the whole population.** *The class is not merely
unreachable; it is slightly enriched in exactly what needs excluding.*

## ④ ⛭⛭ THE STATED LIMIT, WHICH IS `13` KEYS AND NOT `118`

⒞ said the invisible pins become a stated limit. **Stated as precisely as I can:**

- **The hop makes `117` keys visible on the frozen population** (`121` on the merged tree). By the frozen
  labels, **`80` are genuine pins and `37` are not.**
- **The declared container rule excludes `24` of the `37`, forgoing `0` genuine pins.** *That half of the
  bar held on both halves, which is the result worth keeping: a container rule CAN be stated that takes no
  real pin with it.*
- **It leaves `93` keys: `80` genuine and `13` not** — and `11` of those `13` **have no container to test**,
  so they are not a tuning problem and no fifth narrowing could reach them.

⇒ ***THE LIMIT: `80` genuine pins stay invisible to the ratchet, and the price of making them visible is
`13` keys that no stated container rule excludes, `11` of them because the instrument's own trace names
nothing to test.*** **That is the number this four-revision campaign produces, and it is a trade someone
can now decide in one line instead of a fifth measurement.**

⌗ *Not in the test, reported as `DECLARATION.md` ① said: the `4` keys the merged tree mints beyond the
`117` — three in `60`'s new `S48` (`'ABSENT from the file'`, `'FRAGMENT THE INSTRUMENT EXTRACTS'`,
`'r7338+60'`) and one more. **Their labels would have been written after the rule, so they are excluded
from every number above.***
