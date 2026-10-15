# `r7355+cc66.37` — the three limit figures re-measured on the merged trunk: **`80`, `13`, `11` — all three unchanged**, and the reason is that the night's repairs and the invisible population are DISJOINT

*`r7355` ④: **"Those three numbers were measured before `157` rows were repaired across three seats.
Re-measure all three on the merged trunk and report them beside the `r7351` figures."** This is that
re-measurement. No instrument change is landed.*

## ① THE RESULT, BESIDE THE `r7351` FIGURES

| | `r7351` | merged trunk (`cdc164106`) |
|---|---|---|
| frozen population | `117` | `117` surfaced, **`0` lost** |
| PIN / NON-PIN (frozen labels) | `80` / `37` | `80` / `37` |
| the declared rule excludes | `24` | **`24`** |
| **genuine keys forgone** | `0` | **`0`** |
| ⇒ **genuine pins that stay invisible** | **`80`** | **`80`** |
| ⇒ **non-pins no stated rule excludes** | **`13`** | **`13`** |
| ⇒ **of those, trace names nothing to test** | **`11`** | **`11`** |

⇒ ***Not one of the three moved.*** **And the reason is sharper than the figures: all `117` keys surface
with the same `(receipt, literal)` they had at `7db5db61c`, so `157` rows of repair across three seats
touched NONE of them.** *The repair campaign and the invisible population are disjoint sets.*

⌗ *`0` of the `117` appear in the live `quote_pin_baseline.tsv` — none became visible under its own key.*

## ② ⛭ WHAT THAT SAYS ABOUT THE ZERO, WHICH IS WHAT ④ ASKED

`r7355` ④: *"The phase is about to report zero owed; the invisible count is what says whether that zero
means anything."*

⇒ **The zero is worth exactly what it was worth at `r7351`, neither more nor less.** *`REPAIR-OWED` went
`159` → `2` without moving the invisible count by one, because a row the ratchet can see and a pin it
cannot are different populations and the stride only ever worked the first.* **That is not an argument
against the zero — it is the boundary the zero is true inside, and it is now measured on both sides of a
`157`-row campaign rather than asserted once.**

## ③ ⛔ THE HOP'S PATCH WAS NEVER COMMITTED, AND THAT IS WHY THIS NEEDED A METHOD

*The `r7341` hop was measured four times — `r7341`, `r7343`, `r7345`, `r7351` — and **its code is nowhere
in the tree**. `r7341_cc66_the_narrowed_hop/` holds `MEASURED.md`, `REGISTRATION.md` and `deadpin.py`; the
only trace of the hop's implementation anywhere is `split_patch.py`'s two anchor strings, which reference a
`_hop_ok` that does not exist. **So the population four revisions of argument stood on could be re-derived
only from a prose description.***

⇒ ⛭ **`follow_patch.py` is committed here so the next re-measurement is a re-run and not a
reconstruction.** *That is the whole remedy and it is three lines.*

**⛔ AND THE GATE IS DELIBERATELY NOT RECONSTRUCTED.** *`r7341` ① states three conditions that decide WHICH
keys the hop mints. Rebuilding them from prose would give a population *almost* the frozen one, and every
figure above would then differ from `r7351`'s by an unknown amount — which is the one thing a
re-measurement must not do.* ⇒ **Membership is already frozen in `new117.tsv`, so the gate is not needed:
what is needed is the hop's FOLLOW, which is one line, and the frozen list selects from the superset it
mints.** ⌗ *The faithfulness check is stated in advance and it is binding: the follow must surface **all**
`117`. It surfaces `117`.*

## ④ ⛔ AND ONE ERROR OF MINE, CAUGHT BEFORE IT WAS REPORTED

*My first pass tested survival the cheap way — is the frozen literal a substring of the receipt today —
and it said **`3` literals were gone**, one of them a genuine pin. **That would have made figure 1 `79`
and it would have been wrong.***

⇒ ***A live keyed literal need not appear contiguously in its source.*** *All three are **implicit
concatenations** — adjacent string literals the parser joins — so the AST constant the instrument keys is
assembled and never exists as one span of text. `C33`'s `'the expansion rate, the matter and baryon
densities and the tilt free '`, `S10`'s `'"{}"'`, `S3`'s `P15` path.*

⌗ **The class is the one this phase keeps logging: a check that tests something other than what it
claims.** *Substring presence in raw source is not liveness, and the extractor is the only authority on
what it keys. Caught because the two measurements disagreed and the disagreement was worth one minute.*

## ⑤ WHAT IS HERE

`follow_patch.py` (the two patches, committed for reuse), `relimit.py` (the scorer; the rule transcribed
from `DECLARATION.md` ② unaltered), `relimit.txt` (the run), `survive.txt` (the superseded substring pass,
kept because ④ above is a correction and a correction needs its wrong number in the open).

*Verified end to end from a clean copy of the instrument: `follow_patch.py` then `relimit.py` reproduces
`117 / 24 / 0 / 80 / 13 / 11`.*
