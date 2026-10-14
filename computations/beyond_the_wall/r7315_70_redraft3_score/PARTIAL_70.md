# `r7317+70.3` — PARTIAL: 70's half of the crossover. The previous text and the third redraft draw the same flag rate from this applier, −0.5 points, so the crossover attributes nothing to the text. ⛔ But two fresh agents under one instruction differ by 33–35 points in both conditions, which is wider than the 20-point line N-J drew

*Pre-registered at `r7315_70_widens_reregistered/PREDICTION.md` (`0f5d5fa6`, before the third redraft landed at
`1a3c13a6`).*

- **The applications:**
  - `CROSSOVER_70_prev_text.tsv` (`r7317+70.1`, `d130e9e8`): the old text on the 40 crossover keys, committed **before
    any agent opened the new text**.
  - `APPLICATION_70_blind.tsv` (`r7317+70.2`, `f86739bc`): the new text on the 69 held keys.
- **71 has not applied.** 66 holds it until its Lean sweep reaches a stopping point.
- **So nothing that needs both appliers is scored:** neither `T_w`, `A_w`, ① nor ②. Nothing is joined to the ledger.

## `X_70`, the one quantity this half fixes

| | flag rate on decided keys |
|---|---|
| previous text (`6bef6fd5`), 40 crossover keys | 23/40 = 57.5% |
| third redraft (`1a3c13a6`), 69 held keys | 40/69 = 58.0% |
| **`X_70`** | **−0.5 points**, Newcombe 95% **−19.3 to +17.8** |

- ⇒ **NOT ATTRIBUTED** for 70. W-c (+5, band −10 to +20) holds.
- **The third redraft takes no judgement off this applier.** Read with the registration's other arms, that matches the
  prediction that 70's flags are about what a claim is, not about where the text is silent.
- **For comparison only** (not a registered quantity): 70's held-set flag rate across rounds was 62.3% (43/69) on the
  second redraft and 58.0% (40/69) on the third.

## ⛔ What the crossover shows about 70 as a reader

Each condition was split between two fresh agents, by hash order of the keys:

| | agent A | agent B | A − B, Newcombe 95% |
|---|---|---|---|
| previous text | 8/20 = 40.0% | 15/20 = 75.0% | −35.0 (−57.8 to −4.4) |
| third redraft | 26/35 = 74.3% | 14/34 = 41.2% | +33.1 (+9.8 to +51.9) |

- **Under one instruction, and with the keys split at random, the two agents' flag rates differ by about 34 points in
  both conditions.** Both differences exclude 0.
  - The keys differ between agents, so a key effect is not excluded.
  - The split is by hash, though, and the gap has the same size in both conditions with the sign falling either way.
- **Consequences:**
  - **For 70, "the same reader" is a pool of fresh agents, and the pool varies.** The crossover still holds that pool
    fixed across texts, since both conditions drew from it the same way. That is why `X_70` is near 0 while each
    agent pair is 34 apart. But the variance enters `X_70`'s interval.
  - **N-J's 20-point line lies inside this applier's own agent-to-agent spread.** A 20-point move in one seat's flag
    rate between rounds is therefore not, on its face, a change of habit or of text. It can be which agents read
    which keys.
    - For 71, a single seat with memory, that spread is unmeasured. **This is the strongest argument yet that the
      flag is a noisy instrument, and that the crossover, not a between-rounds rate, is the measure to trust.**

## Owed rates (reported, not tested; ② needs both appliers)

| | |
|---|---|
| previous text | 30/40 = 75.0% |
| third redraft | 53/69 = 76.8% |

**The third redraft did not move 70's threshold.**

**Not done:**
- No ledger row is read.
- Nothing is joined.
- Nothing is routed to 71.
- 20 of the 69 held keys carry `seen` flags. They are repair comments inside the receipts themselves, as on both
  earlier rounds.
