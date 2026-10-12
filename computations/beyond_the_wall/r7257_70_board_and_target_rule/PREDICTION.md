# `r7257+70.0` — PRE-REGISTRATION: the pin board's staleness, and the `target` trace rule

*Committed before either change is made or measured. It answers `FOR_70.md` `r7257`, read at `origin/main`
`2654cd0b`.*

## ① The board: the gate regenerates; the committed copy is retired

**Why not "put the generator in the fast job".** In CI a generator can only run with `--check`, and `--check` fails on
exactly the staleness we have now, only earlier. The defect is not that nobody calls the generator. It is that a
**committed copy of a pure function of two committed files** goes stale whenever two branches adjudicate in parallel and
merge: each regenerated on its own base, and the merge of two current boards is not current. No CI wiring fixes a
merge race.

**So the board stops being a committed file.**

- `check_pin_board` regenerates it in memory, every run, from the baseline and the claims ledger.
- It keeps checks (a) (void claims), (c) (expiry) and (d) (seeds).
- It drops (b)'s staleness half, because there is no copy left to be stale. (b)'s total check becomes a seeded
  property of `generate` itself.
- `gen_pin_board.py` still writes the board for a seat to read, to the same path, which becomes git-ignored.
- **The claims ledger stays hand-kept and committed:** that is the half a generated file cannot hold, as at `r7247`.

| # | quantity | predicted |
|---|---|---|
| B1 | a seeded merge race (two branches each adjudicate and regenerate, then merge) fails the OLD gate | yes |
| B2 | the same seeded race passes the NEW gate | yes |
| B3 | a void double claim still fails the new gate | yes |

## ② The `target` rule

**The candidate rule R\*.** Take the set of file kinds the WIDE trace names: `.tex`, `.py`, `.md`, `.json`, `.tsv`,
`.txt`, `.csv`, `.yml` and `.log`.

- `{tex}` only → `PAPER`.
- No `tex` → `SOURCE`.
- `tex` plus anything else → **UNDECIDED**, because the static trace names both a paper and a non-paper.

R\* is compared with the baseline's hand-corrected column (after `r7251`'s 29 and `r7255`'s 20), and with the current
rule.

| # | quantity | central | band |
|---|---|---|---|
| T1 | live keys R\* leaves UNDECIDED | **300** | 100–700 |
| T2 | decided keys where R\* says `PAPER` and the baseline says `SOURCE` | **15** | 0–60 |
| T3 | decided keys where R\* says `SOURCE` and the baseline says `PAPER` | **15** | 0–60 |
| T4 | keys where the CURRENT rule disagrees with the baseline (the 20 `ACOUSTIC` keys at least) | **20** | 15–40 |

## ⛔ The reachable negative on ②, as 66 states it

**If T1 is large, `target` cannot be derived from a static trace**, and it becomes a measured annotation. I set
"large" in advance at **more than 10 per cent of the live keys**, which is 278 of 2,775. The rule then goes in for the
decidable keys, and the UNDECIDED ones keep their hand-kept value under a gate that names them, as a two-file
arrangement.

**If T1 is small**, R\* replaces the rule, and the UNDECIDED keys are hand-kept by a short named list.
