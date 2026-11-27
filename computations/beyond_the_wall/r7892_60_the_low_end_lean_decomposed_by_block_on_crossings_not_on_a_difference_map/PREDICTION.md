---
kind: PREDICTION
revision: r7892+60
origin: this seat's own, following r7866's unexplained remainder and r7890's result — not an order
status: REGISTERED BEFORE ANY PROFILE IS RUN
---

# r7892 — REGISTERED BEFORE THE DECOMPOSITION

**The standing question.** `r7866` located the low-end lean: removing the same thirty-six bins moves
the instrument's crossing by **`−20.09` meV** against the reference's `−0.12`, a factor of `162` on
identical bins. It then tested the order's three candidates and **two thirds of that move has no
named mechanism**: the `τ` prior is out *structurally* (the score the limit is read through carries no
`τ`), the late ISW is **unreadable on this mask** (only `13` TT bins sit below the first peak), and
the lensing-amplitude handover carries **`33` per cent**, leaving `67` per cent standing.

**Why this is the next step, and why it is shaped this way.** `r7890` showed that the per-band
*difference map* cannot be used to localise anything: the same-clock operator converges to the exact
derivative in **no band**, settling to a band-dependent signed offset, and in the band `r7866` picked
out that offset is **seven times** the signal. ⇒ *So the remaining two thirds cannot be chased through
a per-bin difference.* But `r7866`'s `−20.09` meV is a **crossing computed from profiles**, which
`r7890` explicitly left untouched. **So the decomposition must be built out of crossings.**

⛔ **This file is committed and pushed BEFORE any profile is run.**

## ⓵ THE MEASUREMENT

The thirty-six are **the twelve lowest bandpowers of each of the three blocks**. So the move can be
decomposed by block, each arm a crossing and not a difference:

| removal | what it isolates |
|---|---|
| all thirty-six | `r7866`'s `−20.09` meV, reproduced as the control |
| the twelve lowest of **TT** only | TT's share |
| the twelve lowest of **TE** only | TE's share |
| the twelve lowest of **EE** only | EE's share |

Each is `inst_profile` over the four parameters at the seven banked sums, then `cross_of`. `r7866`'s
`same_bins.py` is **imported** and its mask builder, profiler and crossing reader reused; nothing is
retyped.

## ⓶ THE OUTCOMES, FIXED NOW

Write `M₃₆` for the all-three move and `M_TT`, `M_TE`, `M_EE` for the single-block moves. The
registered question is **how the three relate to the whole**:

| | condition | what it means | verdict |
|---|---|---|---|
| **Ⓚ⓵ ADDITIVE** | `\|M_TT + M_TE + M_EE − M₃₆\|` is under `10` per cent of `\|M₃₆\|` | the blocks act independently, so the lean is a **sum of per-block effects** and the largest single block names where it lives | **LOCALISED by block** |
| **Ⓚ⓶ CONCENTRATED** | one block alone carries `≥ 80` per cent of `M₃₆` | the lean is **one block's**, whatever the others do | **LOCALISED to that block** |
| **Ⓚ⓷ NON-ADDITIVE** | neither of the above | the blocks interact through the shared four-parameter profile, so no per-block attribution is available and the next instrument must break the parameters rather than the bins | **NOT localisable this way, and that is the finding** |

⛔ **These are not exclusive by construction and I am not pretending they are:** a single block could
carry `≥ 80` per cent *and* the three could still sum to `M₃₆`. If both fire, **both are reported**, and
`Ⓚ⓶` is the stronger statement. *What is excluded is choosing between them after the numbers are
seen.*

## ⓷ MY REGISTERED EXPECTATION, WHICH CAN BE REFUTED

⚠ **I expect `Ⓚ⓷`, non-additive, and I expect to be wrong about which block dominates if it is not.**
The reasoning: the four parameters are re-profiled at every sum for every mask, so removing bins from
one block changes what the profile does with the others — and `r7866` already measured that parameter
freedom alone accounts for `28.11` meV of a `−48.20` meV move. ⇒ *An effect that large passing through
a shared profile is the signature of interaction, not of independent blocks.*

⌗ *If the three DO sum to the whole, that refutes the expectation and is the better outcome, because
it hands the next step a named block instead of a harder instrument.*

**AND A SECOND EXPECTATION, SEPARATELY REGISTERED:** if any one block dominates, I expect it to be
**EE** rather than TT, because `r7866`'s banded exact derivative has `EE 208`–`500` at `−21.77`, the
largest-magnitude single band anywhere in its table, while `TT 100`–`207` is `+20.50` of the opposite
sign. *That is a reading of a neighbouring band and not of the removed bins, so it is a weak
expectation and labelled as one.*

## ⓸ WHAT WOULD MAKE THIS REVISION REFUSE

- **The all-three control failing to reproduce `r7866`'s `−20.09` meV** within `0.5` meV — then this
  seat is not running the instrument that revision ran and no decomposition of it is comparable.
- **Any profile failing to produce a crossing at all** on the seven banked sums, which `cross_of`
  reports as `None`. A missing crossing is not a zero move and will not be read as one.
- **The thirty-six not being twelve per block**, read off the mask rather than assumed.

## ⓹ WHAT THIS REVISION WILL NOT CLAIM

- ⛔ **Nothing about the reference.** Its `−0.12` meV is a different pipeline and this decomposes only
  the instrument's own move. The `162`× stands as `r7866` measured it.
- **No limit is read**, and `r7888`'s `193.545` meV is untouched.
- **Nothing about `τ`, the ISW or the amplitude beyond what `r7866` measured.** This asks *which
  block*, not *which physics*; a block is not a mechanism, and naming one would leave the mechanism
  still owed.
- **Nothing about the fork routed at `r7888`.** `r7890` removed one piece of evidence that looked like
  it bore on it; this adds none either way.
