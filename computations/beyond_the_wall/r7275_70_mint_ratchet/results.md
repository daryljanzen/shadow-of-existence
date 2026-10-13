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

# `r7275+70.2` — results ②: 69's two operator-flag gaps

| # | quantity | predicted | measured |
|---|---|---|---|
| G-a | live keys newly flagged `OPEN` by the widened marker list | 6 (1–30) | **4**, all one phrase: `no third mechanism has been named`, in `U2`, `B17`, `M1`, `A3` |
| G-b | live `PAPER` keys matching ONLY inside LaTeX comments | 4 (0–20) | **2** |
| G-c | live `PAPER` keys matching inside a comment at all | 30 (5–150) | **79** of 1,602 |

**G-a, the widening.** `_OPEN_WORDS` now carries `no … has been named/found/identified/given`, `has not been …` and
`not yet named`. The plain `the mechanism has been named` does not flag, as checked. The four receipts that count
OPEN keys (`S3`, `S7`, `S17`, `C64`), `check_quote_pins` and `check_pin_board` are all green with it.

**G-b decides 66's question, on the rule fixed in advance: 2 is at most 5, so this is a one-site repair list, not
a member.** The two keys:

- `L222…/W1_what_remains_between_the_wall_and_a_curve_dynamics` `"until r2376+c54.179"`, in a comment of
  `slicing_operator.tex` (`UNADJUDICATED`);
- `…/S1_three_of_eight_stations_are_already_held…` `"THE RECEIPT WAS MORE HONEST THAN THE PAPER"`, in a comment of
  `matter_sector_paper.tex` (`UNADJUDICATED`).

Both are unadjudicated and both belong to other seats. They are routed in `FOR_66_FROM_70.md` and not edited.

**G-c is the exposure, stated as context and not as a member.** 79 keys match a comment as well as the body.
69's own exemplar is one of them: `C1_conformal_vs_isometric` is both in `P5`'s line-7 comment and in its body
`\rcpt{}` at l.681. For each of the 79, deleting the body sentence would NOT fail the pin, because the comment still
satisfies it.

The structural repair would be for `PAPER` pins to read the paper with comments stripped. That is a change to every
receipt's reading helper, not to the operator, so I name it and do not make it.
