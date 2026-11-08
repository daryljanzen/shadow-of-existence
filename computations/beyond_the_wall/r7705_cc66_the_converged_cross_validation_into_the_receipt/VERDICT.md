# `r7705+cc66` — VERDICT

Both items of the order are done. 70's figures all stand; what the read added is three gates and one
correction to a sentence in print.

## ITEM 1 — THE BLOCK IS IN, AND THE RECEIPT IS GREEN

`P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py` l.1027–1153, after the `(L)`
block and before the closing section, exactly where 70's routed diff put it.

| | baseline (`main 71f4c8f74`) | with the block |
|---|---|---|
| wall | `331` s | `338` s |
| checks | `90` OK, `0` FAIL | **`101` OK, `0` FAIL** |
| verdict | `ALL CHECKS PASSED` | `ALL CHECKS PASSED` |

### THE PRICE — THE REGISTERED WIRE FIRED, AND IT FIRED ON NOISE

Registered: **under 2 s added**, and *"if the receipt with the block lands more than 5 s above 331 s, the
cost is not the block's and I say what it is rather than charging it here."* It landed `+7` s, so the wire
fired, and the licence obliges an answer rather than a shrug.

⇒ **The block's own cost, measured in isolation against the same banks, five reps: `7.3` ms** (`6.9`–`7.5`).
Three orders of magnitude under the registered bound. So the `+7` s is run-to-run variation on a
CAMB-and-solver receipt — `2.1` per cent of its wall — which `BASELINE.md` named **in advance** as the
reason a single pair of timings could not resolve 2 s.

⚠ *I started two further baseline reps to put a number on that spread and then **stopped them**: once a
direct measurement of the block existed, an estimate of the noise around it was the weaker evidence and was
costing eleven minutes of the box. Measuring the thing beats bounding what surrounds it.*

## Q1 — ARE THE THREE KNOBS LIVE? *THEY ARE THREE DIFFERENT FACTS, AND ONE OF THEM IS NOT A CONVERGENCE*

| knob | DECOUPLED (L) | FROZEN (L) | what it licenses |
|---|---|---|---|
| `ntau_x2` (opacity grid doubled) | under the floor | **under the floor** | ⛔ *nothing about one build.* **Neither** moves above the bank's resolution, so the knob distinguishes nothing here. It is live in the INSTRUMENT — `HIER` reads `NTAU` as the opacity grid's point count — so this is a **limit of the bank**. |
| `ns3_half` (late step count halved) | under the floor | **`−10.04` per cent at `l = 4`** | ✔ **the control.** The same environment reaches both builds, `NS3` is in DECOUPLED's own `numerics` (`60000 → 30000`), and the build is **converged** in it. |
| `klo_0_02` (continuum five-fold deeper) | `0.360` per cent | `0.366` per cent | ✔ live, resolvable, and under the `0.4` per cent the routed bound asks. ⛔ *and it is a MOVE, which the paper currently calls a non-move.* |

**The registered prediction held** — FROZEN moving at least 1 per cent at `l = 4` under `ns3_half`; measured
`10.04` per cent, ten times the registered floor. **The third registered outcome is ruled out** for `NS3`:
it does enter the decoupled integrator and the build is converged in it. ⚠ **But the third outcome's SHAPE
turned up on a different knob in a different form** — not "the knob never arrived" but "the bank cannot
see it" — and `ntau_x2` is where it landed. *Registering a third outcome in advance is what made it
recognisable when it appeared somewhere I had not expected it.*

### AND THE BOUND ITSELF WAS FINER THAN ITS DATA

Every row in this bank family is stored to **four decimals** — measured, 182 values across the four banks.
So the finest move the bank can express at `l = 4` is `1e-4 / 0.3433 = 0.029` per cent, and the routed
`5e-5` bound is **5.8 times finer than that**: it could only ever pass as an exact equality of quantised
numbers. ⛔ **A tolerance finer than its data's last place is not a tolerance.** The three knobs are now each
stated at what this bank can say, and "under the floor" is written as EQUALITY of the stored rows, not as a
small number — *writing it as `< 0.5 × floor` would have reintroduced the sub-last-place bound the block
exists to correct.*

## Q2 — THE PAIRING, AND IT IS LARGER THAN I REGISTERED

Registered as "the refit rows are read without their pairing asserted". The read is worse than that:
**`r7697` put the question to arm A's bank and to that bank ALONE.** The hierarchy bank's `config` was never
opened by this receipt, so every DECOUPLED and FROZEN `(L)` row it reads — **the depths in print included** —
was being read on the strength of its key's spelling. The assertion now covers the hierarchy bank's three
rows, arm A's refit row, and the convergence bank's FROZEN rows. *One assertion per bank and per row, not
one per family.*

## FAILABILITY — NINE LEGS, EACH REDDENING THE CHECK IT NAMES, OVER A GREEN CONTROL

The block's source is **read out of the receipt**, not copied, so a passing leg is a statement about the text
in the tree. The harness's own control runs first — 11 checks, 0 red — because without it a leg's red is not
evidence.

⛔ **Leg A, written first as a scale of `1/1.04`, reported `0` FAIL.** Not a harness fault: converged FROZEN
sits `3.17` per cent **below** arm A at `l = 4`, so shrinking arm A shrank the departure to `+0.7` per cent
and the bound rightly held. *The leg was perturbing TOWARDS the gate. That is what a leg reporting nothing
always means, and `r7703`'s leg B is why it was read that way the first time instead of the fourth.*

## ITEM 2 — THE SCOPE SENTENCE

In `DRAFTS.md`, every figure with its licence. Two things 69 should see before landing:

1. ⛔ **One change is a CORRECTION, not a rewording.** The sentence in print says the hierarchy's depths
   *"do not move under a doubled opacity grid, a halved late step count, or a further-extended continuum"*.
   The further-extended continuum **does** move them, by `0.360` per cent — 70's own routed bound, twelve
   times the bank's resolution. The draft says "move by under four tenths of a per cent".
2. ⚠ **One figure I did not pin, so the draft does not print it.** The attribution "the frozen build's
   larger departure was its step count and not its treatment of the sectors" is carried by two pinned
   numbers (`3.23` per cent off its own limit; `3.17` per cent of arm A once converged). The figure that
   would state its size — the unconverged row's `6.2` per cent departure from arm A, 70's `r7695` figure —
   **is not computed by this receipt and is not in print.** If 69 wants the size stated, that has to be
   pinned first, and I have not pinned it.
