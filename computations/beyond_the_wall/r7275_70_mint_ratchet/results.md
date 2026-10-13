# `r7275+70.1` — results ①: the mint ratchet. One commit in 200 minted, and it was an instrument widening, so the shape that allows exactly that refuses nothing that cleared keys

*Pre-registered at `PREDICTION.md` (`8bb4f579`). The measurement is `history.py`, with its output in `history.txt`.*

| # | quantity | predicted | measured |
|---|---|---|---|
| M-a | commits touching the baseline, of the last 200 first-parent on `main` | 60 (30–120) | **47** |
| M-b | refused by V1, strict | 25 (8–60) | **1** |
| M-c | refused by V2, re-key allowance | 15 (4–45) | **1** |
| M-d | refused by V3, net per receipt | 12 (3–40) | **1** |
| M-e | clearing commits refused by the CHOSEN shape | 0 | **0** |
| M-f | largest single-commit mint | 40 (10–150) | **102** |

**The one minting commit is the whole story.** `36973e3d`, a merge of cc66's branch, added 102
`UNADJUDICATED-PINNED` keys across 39 receipts. **None of the 39 receipts changed in it.** The instrument did
(`mutate_assertions.py`, `check_quote_pins.py`). So it was an instrument WIDENING, which revealed pins that were
already there, and not a seat leaving its own pins unread.

In 200 commits no plain `UNADJUDICATED` key was minted at all. `check_quote_pins` already fails a NEW key that is
missing from the baseline, so every new pin has been entered with a verdict. **The refill 66 named has not been
happening by hand. It has been happening by instrument widening, and only into the reserved class.**

⛔ **66's wrong-shape negative does not fire.** None of the three shapes refuses a commit that lowered the
unadjudicated total. V1–V3 each refuse only the widening merge (2% of the 47), which is under the 10% too-strict
line, but refusing it would block the instrument from improving.

**The shape placed: `check_pins_adjudicated_on_mint`, in the fast job.** A minted unverdicted key is allowed only
when both of these hold:

- **(a)** it is in a reserved class (`-PINNED`, `-LIST`), a declared hold;
- **(b)** its receipt is unchanged in the range, so the pin pre-existed and only the instrument now sees it.

Everything else is refused, including a plain-class mint on an unchanged receipt. A receipt added or edited in the
range adjudicates its own pins in that range.

**Measured with the gate's own function over the same window: it refuses 0 of 47.** It allows the 102-key widening.
Its five seeds hold in both directions: a new receipt's plain mint is refused, an edited receipt's reserved mint is
refused, an unchanged receipt's plain mint is refused, an instrument widening is allowed, and an adjudicated mint is
allowed.

**The range:**

- on a branch or pull request, `merge-base(origin/main, HEAD)..HEAD`;
- on `main`, `HEAD^1..HEAD`, which for a merge is the whole merged branch;
- `MINT_RANGE` overrides both;
- a shallow clone is refused.

**What it does not do, stated.** It holds the reserved classes as declared holds and does not clear them. Clearing
them is the backlog campaign's work. What the gate stops is any new range adding to the backlog by any route except
an instrument that newly sees an old pin.
