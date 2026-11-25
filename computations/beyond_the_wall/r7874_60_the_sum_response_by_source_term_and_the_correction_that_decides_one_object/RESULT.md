---
kind: RESULT
revision: r7874
node: 60
order: r7873
---

# r7874 — THE ENVELOPE RULING RETIRED THIS LINE'S OWN HEADLINE, THE SHARPER TEST FOUND A REAL AMPLITUDE EXCESS, AND NO SINGLE SOURCE TERM CARRIES IT

**Registered first, twice.** `PREDICTION.md` was committed and pushed before any computation of
this revision existed. When Ⓐ⓪'s verdict then made a sharper arm worth adding, that arm was
registered in a **clearly-marked addendum, committed and pushed before it ran** — because a
registration edited after a result is not a registration.

**Three registered negatives fired in this revision, and one of them is this line's own landed
headline.**

---

## Ⓐ⓪ THE ENVELOPE RULING, SPENT ON `r7872`'s HEADLINE BEFORE ANYTHING NEW

The order relays `cc66`'s finding that CAMB's sum response at fixed parameters is an **oscillation**
whose ENVELOPE is what is monotone in the sum, and rules: *read your ratios against that envelope,
not against point values.* `r7872` reported the instrument's TT response at `ℓ = 100` as `1.77×`
CAMB's — a ratio of **point values**. So the ruling was spent there first.

### The measurement

Maximum departure over `ℓ = 100`–`212`, against the like-for-like **unlensed** leg, with the
oscillation's envelope over the same stretch beside it:

| block | Σ | departure | envelope | |
|---|---|---|---|---|
| TT | 0.06 | `0.00122` | `0.00447` | inside |
| TT | 0.30 | `0.00805` | `0.02207` | inside |
| TT | 0.60 | `0.03053` | `0.04508` | inside |
| EE | 0.06 | `0.00080` | `0.00598` | inside |
| EE | 0.30 | `0.00261` | `0.03273` | inside |
| EE | 0.60 | `0.01031` | `0.07054` | inside |

`r7872`'s headline re-read: the instrument returns `0.070234` at `ℓ = 100` against CAMB's
`0.039702`, which **is** the `1.769×` it reported — but the **gap** is `0.030531` against an
envelope of `0.045076`, i.e. `0.68×`.

⇒ **THE DEPARTURE IS NOT RESOLVED AS A DEPARTURE UNDER THE RULING.** `r7872`'s **numbers stand**,
and its receipt pins them correctly against the criterion that revision registered. **What does not
stand is the reading that a departure is LOCATED at `100`–`212`.** Said here rather than left for
another seat to find.

### Two things the order did not ask for, because a borrowed number has to be reproduced first

- **`cc66`'s envelopes were recomputed** from its own control, `τ`, `A_s`, `lmax` and CAMB leg.
  Worst relative difference **`1.06e-06`** — agreement to six significant digits, on six rows whose
  other five sit between `8e-09` and `2.7e-07`. ⚠ **The script's own gate was `1e-06` and prints
  NOT REPRODUCED. That gate is left UNMOVED:** it was this line's, it was set too tight for a figure
  CAMB reproduces to about a part in a million, and **the measurement is the number, not the
  threshold.** Said, not loosened.
- **The leg mismatch is named.** `cc66` computed on the **lensed** leg; the instrument's banked
  TT/EE/TE are **unlensed**. The envelope is leg-dependent, so an unlensed departure read against a
  lensed envelope mixes two objects. Both legs are reported, whole-band and local; the verdict is
  taken on the like-for-like one, and over this stretch the two agree to three digits anyway.

---

## Ⓕ④ THE SHIFT TEST — AND THE ENVELOPE TEST IS TOO LENIENT

**Why an arm was added at all**, stated in the addendum before its answer was known: the envelope is
the largest excursion of **one** curve; the departure is the largest pointwise difference between
**two**. One being smaller than the other is not by itself a reason to call the difference unreal.
What makes a pointwise difference between two oscillating curves spurious is the two being
**misregistered in ℓ**. ⇒ So the question is this line's own standing guard applied to the clock
that labels multipoles: *does the difference survive a change of clock?*

Two parameters, each with its own meaning, and no more: `r_inst(ℓ) ≈ A · r_camb(ℓ(1+ε))`.

**The allowance for a legitimate registration `ε` is measured, not chosen** — the instrument's own
sum-induced fractional peak shift from the bank's recorded `l_A`, against CAMB's from its own
`θ*`:

| Σ | instrument | CAMB | difference |
|---|---|---|---|
| 0.30 | `−4.163e-03` | `−4.419e-03` | `2.563e-04` |
| 0.60 | `−8.440e-03` | `−8.957e-03` | `5.170e-04` |

**The fits want three to four times more than that, and they want an amplitude:**

| block | Σ | best `ε` | `× allowance` | best `A` | `A` across the band | residual | raw |
|---|---|---|---|---|---|---|---|
| TT | 0.30 | `7.0e-04` | 2.7 | **`1.152`** | `[1.146, 1.153]` | `1.6e-03` | `2.7e-03` |
| TT | 0.60 | `−1.9e-03` | 3.7 | **`1.296`** | `[1.284, 1.298]` | `5.6e-03` | `1.0e-02` |
| EE | 0.30 | `−1.7e-03` | 6.6 | `1.014` | `[1.012, 1.016]` | `1.3e-03` | `1.5e-03` |
| EE | 0.60 | `−1.65e-03` | 3.2 | `1.046` | `[1.043, 1.049]` | `5.0e-03` | `6.3e-03` |

⇒ **AN AMPLITUDE DIFFERENCE, in every block and both sums.** The instrument's **TT** sum response
is **15 per cent larger** than CAMB's at `0.30` eV and **30 per cent larger** at `0.60`, `A` stable
across the whole near-best band, with a residual surviving. **EE matches to 1.4 and 4.6 per cent.**

⇒ **So the envelope test was too lenient for this purpose.** There is a real departure it could not
see. ⛔ **That is ROUTED to `69`, not asserted over the seat that ruled it** — and **Ⓐ⓪'s verdict is
not retracted.** The departure is inside the envelope, as measured; this arm says what being inside
the envelope does and does not establish.

### ⚠ A criterion of this line's misfired, and is recorded per row rather than deleted

The addendum's NOT SEPARABLE case is stated as *"`A` and `ε` trade off against each other across a
wide range at comparable residual."* The first cut coded the **`ε` band's width alone** — a proxy
for that clause, and not the clause: *a wide `ε` band with a stable `A` is an `ε` that is poorly
pinned and an `A` that is well pinned, which is no trade-off at all.* On the proxy all four rows
read NOT SEP; on the clause as written, with `A` measured **across** the band, all four read
AMPLITUDE. **Both verdicts are kept in the record, per row.**

---

## Ⓑ① THE DECOMPOSITION — NO SINGLE TERM CARRIES IT

**The order asks for a quantity the object does not have**, and the registration said so before any
of this ran: the `SRCDEC` block's own comment states that the source terms ADD but `D_ℓ` is
QUADRATIC in the transfer, *"so the projected pieces do not"*. What closes is the **bilinear**
decomposition — ten pairs, four of which involve `isw`.

**The closure is checked first:** the ten columns sum to the reported `D_ℓ` to `1.3e-15` relative at
every sum.

Each pair's share of the change in `D_ℓ` over `ℓ = 100`–`212`:

| pair | Σ = 0.30 | Σ = 0.60 |
|---|---|---|
| `sw*sw` | **`0.383`** | **`0.361`** |
| `sw*isw` | `0.342` | `0.342` |
| `isw*isw` | `0.198` | `0.219` |
| `dp*dp` | `0.043` | `0.039` |
| `sw*dp` | `0.022` | `0.020` |
| every other pair | under `0.003` | under `0.021` |

By term, summing every pair a term appears in — ⌗ **and these DOUBLE-COUNT the cross pairs, so they
are not a partition**: `sw` `0.746 / 0.721`, `isw` `0.551 / 0.580`, `dp` `0.080 / 0.081`, `pol`
`−0.001`.

⇒ **NO SINGLE TERM CARRIES IT.** The largest pair is `sw*sw` at both sums, but **it does not
dominate**: the **cross** pair `sw*isw` sits `1.12×` and `1.06×` behind it, and three pairs spanning
`sw` and `isw` are each above a tenth.

### ⚠ And the first cut's printed verdict said "the carrier is `sw*sw`"

That is an overreach of the same shape this line has corrected twice before —
calling the largest **the** carrier while a cross pair sat at ninety-five per cent of its share.
`PREDICTION.md` licenses naming *"the largest contributor and every contributor above a tenth"*; it
does not license naming a carrier. A **dominance test** is measured now and reported per sum, and
the verdict above is the corrected one.

⌗ *It coheres with Ⓕ④: `sw` and `isw` are both temperature-only terms, which is where an amplitude
excess in TT with EE nearly matching had to live.*

---

## Ⓓ③ THE CONDITION IS ANSWERED BOTH WAYS BY THE SAME MEASUREMENT

The order gates the epoch-dependent clustering fraction on *"① naming the ISW"*. The measurement:

- **the ISW is NOT the largest single pair** at either sum ⇒ **NOT MET**;
- **the ISW-involving pairs carry a MAJORITY** of the change, `0.551` and `0.580` ⇒ **MET**.

⛔ **The switch is NOT written, and both readings are ROUTED.** A conditional arm whose condition
the measurement answers both ways is a decision for the seat that wrote the condition, not a coin
for this one to toss.

## Ⓒ② NOT RUN UNDER ITS OWN GATE, AND THE GATE'S REASON IS DISSOLVED

`PREDICTION.md` says the correction arm does not run if Ⓐ⓪'s negative fires, *"because a correction
built from an unresolvable residual would decide 'one object' on noise."* Ⓐ⓪'s negative **did**
fire, so under the gate as written the arm does not run.

⚠ **But Ⓕ④ dissolves the gate's stated REASON:** the residual **is** resolvable — as an amplitude
difference of 15 to 30 per cent in TT. ⇒ So the arm is reported **NOT RUN under the gate**, the
dissolution is recorded, and **re-registration is routed rather than taken**. Running it on that
basis would be acting past a gate without re-registering it, which is the discipline this revision
has already spent one addendum to keep.

---

## WHAT THIS REVISION DOES NOT DO

- **The two-start basin test is `cc66`'s**, as the order assigns and as this line routed it.
- **No limit is read, and no envelope crossing appears in this record at all.**
- **No CAMB per-term figure is quoted**, because none exists; the order asks `cc66` for it.
- **No switch is written**, and **no other seat's receipt is edited.**

## FOUR THINGS IN THIS RECORD ARE THIS SEAT'S OWN

1. **The envelope ruling was spent on this line's own headline before anything new was measured**,
   and it retired that headline's reading. Doing it first was the point: a ruling applied to
   everyone else's numbers before one's own is not a ruling.
2. **A criterion of this line's misfired**, coding a proxy for a clause instead of the clause. Kept
   per row rather than deleted, because the proxy's disagreement with the clause is the useful part.
3. **A verdict of this line's overreached again** — "the carrier is `sw*sw`" — in the same shape as
   twice before. ⌗ *The pattern is worth more than the instance: the verdicts of this line's that
   FAILED were the ones that named a single cause, and the ones that held named what was ruled OUT.*
4. **The envelope test's leniency was found by asking what the test was a proxy for**, which is the
   same move that found the basin two revisions ago and the same move that corrected ③ here. ⚠ *And
   it cuts against this line's interest in both directions: it retired a headline this line wanted
   and then recovered a departure the ruling would have discarded.*
