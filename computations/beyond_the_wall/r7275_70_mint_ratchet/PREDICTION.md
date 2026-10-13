# `r7275+70.0` — PRE-REGISTRATION: the ratchet that refuses minting an unadjudicated quote-pin key, and `69`'s two operator-flag gaps

*Committed before any history is measured. It answers `FOR_70.md` `r7271` ① and ② (live at `r7275`), read at
`origin/main` `1b5193e4`.*

## ① `check_pins_adjudicated_on_mint`

**Definition.** A commit range MINTS a key when `corpus/quote_pin_baseline.tsv` at the range's tip carries a
`(receipt, literal)` key that its base does not, with a verdict in `UNVERDICTED` (`UNADJUDICATED`,
`UNADJUDICATED-LIST` or `UNADJUDICATED-PINNED`, `check_pin_board`'s own tuple).

**Three shapes, measured against the last 200 commits on `main`** (first parent, each against its own parent):

| shape | refuses |
|---|---|
| **V1, strict** | any minted key, any class |
| **V2, re-key allowance** | as V1, except that a minted key does not count when the same commit RETIRES an `UNVERDICTED` key of the same receipt: a literal edited in place, so the backlog does not grow |
| **V3, net per receipt** | a commit only if, for some receipt, its count of `UNVERDICTED` keys RISES |

The two reserved classes (`-LIST`, `-PINNED`) are measured inside each shape and also on their own, so whether they
may stand as declared holds is decided on the count.

| # | quantity | central | band |
|---|---|---|---|
| M-a | commits in the last 200 that touch the baseline at all | 60 | 30–120 |
| M-b | commits V1 refuses | 25 | 8–60 |
| M-c | commits V2 refuses | 15 | 4–45 |
| M-d | commits V3 refuses | 12 | 3–40 |
| M-e | **commits that LOWER the unadjudicated total (the clearing commits) that the CHOSEN shape refuses** | **0** | 0–0 |
| M-f | the largest single-commit mint, in keys | 40 | 10–150 |

**⛔ The reachable negative, as 66 sets it.** A shape is the WRONG SHAPE if it refuses ANY commit that lowered the
unadjudicated total. Those are the commits that cleared the 1,335 keys. If every shape does, that is reported as the
finding and nothing is placed.

**⚠ Too strict to land:** a shape that refuses more than 10% of the commits that touch the baseline. Those are
mostly receipts landing with their pins, and a gate that stops one in ten of them is a toll, not a ratchet. The
chosen shape is the strictest one that passes both tests.

**The range in CI.** On a pull request it is `origin/main...HEAD`, merge-base to tip. On a push to `main` it is the
push's own `before..after`. A shallow clone is refused.

## ② The two gaps

| # | quantity | central | band |
|---|---|---|---|
| G-a | live quote-pin keys newly flagged `OPEN` when the marker list gains `has been named`, `has not been named`, `no … has been named`, `not yet named` | 6 | 1–30 |
| G-b | live `PAPER` keys whose literal matches ONLY inside LaTeX comments of the files it reads | 4 | 0–20 |
| G-c | live `PAPER` keys whose literal matches inside a comment at all | 30 | 5–150 |

**The rule 66 fixed, kept.** G-b decides whether "a pin satisfied by text the paper does not render" is a member,
on the count. More than 5 is a class; 5 or fewer is a one-site repair list. G-c is context only.

**Landing in pieces, per the standing order:** this file first, then the measurement, then the gate, then ②, each
pushed when green.
