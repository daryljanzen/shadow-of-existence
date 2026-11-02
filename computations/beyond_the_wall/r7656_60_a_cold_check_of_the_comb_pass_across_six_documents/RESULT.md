# `r7656` (60) — A COLD CHECK OF THE COMB PASS ACROSS SIX DOCUMENTS

**Answering `r7655`.** 34 sites, 95 figures, 100 candidate receipts (99 ran), six documents.

## THE HEADLINE: **85 of 95**, with 9 unestablished, 1 exception and 0 absent

| verdict | n | what it means | this rung's own decoy rate |
|---|---|---|---|
| `VERBATIM` | 81 | a receipt prints **that string**, both sides through the gate's extractor | **10.5 %** |
| `EXACT-VALUE` | 4 | a receipt prints the **same float**, rendered with a different digit count | **14.7 %** |
| `UNESTABLISHED` | 9 | would be carried by the **rounding** rung, which is **withheld** | 25.3 % — **over** |
| `GATE-ONLY` | 1 | inside the gate's allowance, **not** the digit the paper prints | — it *is* the exception |
| `ABSENT` | 0 | | |
| `UNRUN` | 0 | | |

⌗ **The tolerance reading of this same data was 95 of 95 — and it is discarded.** A decoy control,
written before that number was judged, moved every figure **forty times its own allowance** and found
that **41.1 %** of the decoys "reproduced" too. *A 95-of-95 at a 41 % false-positive rate measures the
window and not the corpus.*

## THE ORDER'S THREE EXPOSED CLAIMS — one holds unlocated, two fail

Their quantities are **in words**, so no gate of this corpus is watching any of them, and the figure
check above could not reach them either: the sentences carrying them contribute `2.35`, `1.60`,
`299.1`, and those score green.

**A — "the first three peaks within three and a quarter multipoles of the measured ones"** (P15 l.136,
l.149, l.886; P7 l.1812) → **UNLOCATED.** It *holds*: max |residual| over peaks 1–3 is **2.27 ≤ 3.25**.
But **nothing in the bank produces 3.25**; the bound is loose by **1.43×** the measured maximum.

**B — "and the fourth a third of a per cent high"** (P7 l.1812) → **FAILS.** Every reading the bank
supports is larger: **0.520 %** (sub-bin vs the sky's 1123.9), **0.699 %** (sub-bin vs `PO-47`'s
1121.9), **0.899 %** and **1.079 %** (raw grid). The nearest is **1.56×** the claim, and the stated
0.333 % is 3.75 multipoles — a value no reading returns. *Put 0.520 % through the same verdict function
and it REPRODUCES, so this is the bank disagreeing with the paper and not a test nothing could pass.*

**C — "what remains at the peaks is between one and three multipoles"**, tested **at each peak** (P15
l.136, l.2067, l.2788; P7 l.1863) → **FAILS AT "EACH" UNDER EVERY READING, each at a different peak:**

| reading | ℓ₁ | ℓ₂ | ℓ₃ | ℓ₄ | fails at |
|---|---|---|---|---|---|
| cumulative spacing error (l.2067's own derivation, 0.7/period) | 0.70 | 1.40 | 2.10 | 2.80 | **peak 1** |
| measured sky residual, \|arm − sky\| | 1.65 | 1.85 | 2.27 | **5.84** | **peak 4** |
| arm − control, what belongs to the construction | 1.70 | **0.44** | **0.70** | **0.52** | **2, 3, 4** |

⌗ **So the word carrying the claim is "each".** Two of the three readings hold at *three* of the four
peaks, which is why the sentence reads as true and is not. **The corpus's own guard applies:** *before
two stretches are identified by a label, check how many-to-one the label is on the object.*

## THE INSTRUMENT, AND WHY EACH RUNG IS REPORTED OR WITHHELD

Four readings of one data set, each with its **own measured false-positive rate** against the **20 %
registered at `+60.3` and never moved**:

```
tolerance window   41.1 %   DISCARDED   -- the reading that returned 95 of 95
rounding           25.3 %   WITHHELD    -- its 9 figures are UNESTABLISHED, not reproduced
exact value        14.7 %   reportable  -- the headline's own rung
verbatim           10.5 %   reportable
```

The order of the four is the one their definitions predict. **`cold_check.py` does not hold the
withholding as a constant — it reads `controls.json` and withholds the rung itself**, so the verdict
cannot drift from the control that licenses it, and a missing control is a hard stop.

**And the 25.3 % is diagnosed, by a hypothesis registered before it was tested.** The rounding rung's
reach is a function of the figure's **precision**, not of the corpus:

```
<=2 significant digits   100.0 %   (2 decoys)
 3 significant digits     90.9 %   (11 decoys)
>=4 significant digits    14.6 %   (82 decoys)  <- under the threshold
```

All nine withheld figures carry ≥4 digits — `1125.1`, `811.6`, `0.4390` — so they are
**conditionally established at that precision and at that measured rate**, on their own line, and
**never folded into the 85**.

⌗ **The caveat is stated rather than elided.** What is measured here is a **pool search** — any of 99
receipts' numbers against one target. `check_figures_pinned` compares **one** receipt to **one**
baseline, so the gate's own rate is **not** 90 % and is **not claimed**. It is routed as a question
with the instrument that would answer it.

## THE ONE EXCEPTION

`1.4011` at **P15 l.2792**. The nearest value any of the 99 banked outputs prints is `1.401`, **2.00
half-units** out, and the next nearest, `1.40097`, renders to `1.4010`. It is inside the gate's 0.05 %
allowance and is **not the digit the paper prints**. Registered at `+60.5` as a band of 1–3 members;
**measured 1**, so it is an incident and not a class.

## WHAT IS NOT CLAIMED

Not that the receipt behind the three sentences is wrong — it is not this seat's, it is not edited, and
its own numbers are what every verdict is read *from*. Not a correction to any of the three sentences:
that needs the configuration each was written in. Not that the nine unestablished figures are absent —
they are neither reproduced nor absent, and saying so is the point.

## THE RECORD OF THIS REVISION'S OWN MISSES

Two registered conditions **failed and are kept with the readings they broke**: **⑫** the tolerance
matcher's decoy rate at **41.1 %** against 20 %, and **㉑** the rounding matcher's at **25.3 %**. Each
had its consequence written down *before the number existed*, and each consequence was applied.

⌗ **The lesson, stated against myself:** *I built the window, then the verbatim matcher, then the
rounding matcher, and each time the thing I had to measure was not the corpus but the instrument I had
just reached for.* **The only reason any rung here is reportable is that the decoy control was written
before the first of them produced a number** — and the one check in `exposed.py` that compared a value
to itself was caught and replaced, which is the same mistake committed a sixth time and found.
