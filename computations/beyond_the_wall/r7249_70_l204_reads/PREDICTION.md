# `r7249+70.2` — PRE-REGISTRATION: the `L204_physics_reach` reads

*Committed before any of the prefix's receipts is opened for this batch. The claim is `corpus/pin_claims.tsv`
(`08401b88`).*

- **The population:** 99 `UNADJUDICATED` keys in 14 receipts. The prefix also carries 15 verdicted keys, which
  this batch does not touch: 10 `EXTENDED`, 2 `ENCODING-OK`, 2 `REPAIR-OWED` and 1 `DELIBERATE`.
- **The method:** read each key's assertion in its receipt and record one of the header's verdicts, with what was
  read. Then regenerate the board.
- **The base rate:** the corpus's verdicts so far, excluding `EXTENDED`, are `DELIBERATE` 74 per cent,
  `ALT-OK` 13 per cent, `NOT-A-PIN` 6 per cent, `ENCODING-OK` 4 per cent and `REPAIR-OWED` 3 per cent.
- **Why I expect more `DELIBERATE` than the base rate:** the prefix's stems are mostly claims that the corpus
  does or does not name something ("never mentions Unruh", "declined in print and never named"). For those
  receipts, the name is the claim.

| verdict | central | band |
|---|---|---|
| `DELIBERATE` | **65** | 45–85 |
| `ALT-OK` | **10** | 2–20 |
| `REPAIR-OWED` | **8** | 2–20 |
| `NOT-A-PIN` | **8** | 0–20 |
| `ENCODING-OK` | **5** | 0–12 |
| left `UNADJUDICATED` at the end | **0** | 0–10 |

⛔ **What would make me stop the batch:** if more than 30 keys come out `REPAIR-OWED`, the prefix is a repair
job and not a read. I would then report it as that before editing any receipt.
