# r7468 — THE PROJECTION KERNEL'S PHASE IS A HALF CYCLE PER PEAK, WHICH IS AN ALTERNATION AND NOT A RUN. IT IS NOT THE CARRIER EITHER

**WHAT THIS READS, AND IT IS NOT A NEW INSTRUMENT.** `r6999`'s banked width filter builds the exact
kernel integral over the visibility with the leaf acoustic phase held and the spherical Bessel at
the instrument's own `ℓ`, `k` and `η₀` — **and takes `np.hypot` of the two quadratures every time it
is called.** The PHASE of that same complex integral is the projection's own contribution to the
acoustic phase. It has been in the banked instrument and nothing had read it.

**AGAINST WHAT.** `r7466`'s target, carried forward: **`+0.04628` cycles per peak**.

---

## ⌈ ① THE REGISTERED MEASUREMENT IS UNDETERMINED, AND NO REGISTERED CONTROL CAUGHT IT

At the comb's peaks the raw phase reads `−3.061, +0.122, −2.995, +0.149, −3.007` — **alternating
between about `−π` and about `0`, because `j_ℓ` changes sign between successive comb orders.**
Adjacent samples are `3.183` rad apart, **above `π`, which is the aliasing limit of an unwrap**.
⇒ Any multiple of half a cycle per peak may be added, and `np.unwrap` picks a branch rather than
finding one. It picked badly: the unwrapped series **jumps back** at `n = 5`.

**⛔ AND Ⓥ③ PASSED THROUGH IT.** Ⓥ③ refines the quadrature grid and requires the run to hold:
`−0.29785` against `−0.29786`, **`0.00` per cent change** — because *the same wrong branch is
perfectly reproducible*. ⇒ ***AGREEMENT OF AN INSTRUMENT WITH ITSELF IS NOT CORRECTNESS.*** This is
this seat's own generator in its mildest form, and the control that would have caught it is
**Ⓥ④, added here and said to be added**: adjacent raw samples must be closer than `π`.

---

## ⌈ ② RESOLVED BY SAMPLING DENSELY IN `ℓ`, AND THE NUMBER IS A HALF CYCLE PER PEAK

Sampled in steps of `0.05` and `0.02` in comb units and unwrapped there, the phase read at the
integer comb orders runs

| | run, cycles per peak | at the other step | share of target |
|---|---|---|---|
| `CR` arm | **`+0.50215`** | `+0.50215` | `+10.85` |
| control | **`+0.50159`** | `+0.50159` | `+10.84` |

**A half cycle per peak is the Bessel's own sign alternation** — `j_ℓ` flips sign between comb
orders — **and an alternation is a relabelling of the comb, not a run in it.** So the quantity that
could carry the drift is the **residual above the half cycle**:

> `CR` `+0.00215` — **`4.6` per cent of the target**  ·  control `+0.00159` — `3.4` per cent

⇒ **And the part that could be this construction's rather than any projection's is the difference:
`+0.00056`, `1.2` per cent of the target.** That one is **branch-invariant**: both arms are
unwrapped identically, so whatever branch the unwrap picks cancels out of it. *It is the only number
here that needed no choice at all.*

---

## ⌈ ③ AND THE RESIDUAL IS A STEP, WHICH IS `r7466`'s FINDING AGAIN ONE LEVEL DOWN

`r7466` made shape the discriminating question: the residual's drift is a **line**, and the model's
own per-peak phase is a **step** that beats a line by `5.8`. Read on the residual above the half
cycle here:

> `CR` `−0.00733, −0.00072, +0.00322, +0.00357, +0.00126` — **a step beats a line by `2.79`**
> control `−0.00626, +0.00020, +0.00268, +0.00323, +0.00016` — **by `4.03`**

⇒ **So the projection's phase contribution fails on both counts at once: it is twenty times too
small as a run, and what little it has is the wrong shape.** *The same step, at the same place, in
the projection as in the acoustic dynamics — which is worth noticing and is not explained here.*

---

## ⌈ ④ WHAT THIS LEAVES `PO-87`

⇒ **The drift is carried by neither of the row's located halves.** `r7466` priced out the acoustic
levers — the driving and the loading move the phase's offset and not its run, and every lever is
spent in `ℓ_A` before it arrives. **This prices out the projection kernel's phase: `4.6` per cent of
the target absolutely, `1.2` per cent differentially.**

⇒ **AND THAT SEPARATES TWO OBJECTS THE ROW CARRIES AS ONE.** Step ① locates the contrast excess
*"in the projection from wavenumber to multipole and not in the acoustic dynamics"*, and `r6999`
measured the projection WIDTH channel at *"at most a quarter"* of that excess. **The phase drift is
not that effect**: the projection's phase is a half cycle and an alternation. ⇒ ***The row's
workable half contains two effects and not one, and nothing had said so.***

⌗ **Supplied, NOT applied**: nothing is written to `THE_REGISTER` and no paper edit is owed.
⌗ **`PO-87`'s fourth-peak half is data-gated and is untouched.** ⌗ **No new spectrum**; the
visibility, the leaf phase, `η₀`, `r_s` and `ℓ_A` are the banked instrument's own.

---

## ⌈ ⑤ THE CONTROLS AND THE SCORECARD

**Ⓥ① SAME INSTRUMENT — PASS,** and at the strongest possible tolerance: `|I|` from this file's
complex integral equals `r6999`'s own `amp(ℓ, k, 1.0)` with a worst relative difference of
**exactly `0`**. *One copy of the kernel, loaded from its own file by `ast`.*
**Ⓥ② THE ANCHOR DROPS OUT — PASS,** `8.9e-16` rad between the mean- and peak-anchored phases at
`s = 1`, so `Ⓓ④`'s defect is checked and not assumed.
**Ⓥ③ NOT THE QUADRATURE'S — PASS, and the pass is the problem** (see ①).
**⛔ Ⓥ④ THE UNWRAP IS FORCED — ADDED, NOT REGISTERED, and it FIRES on the comb's peaks.**

| arm | predicted | measured | |
|---|---|---|---|
| `Ⓐ` the projection's run | non-zero, `|s| < 0.012` | `+0.50215` raw | **MISS** |
| | | decomposed: `1/2` alternation `+ 0.00215` | *the residual is inside the bound* |
| `Ⓑ` arm minus control | `|Δs| < 0.005` | `+0.00056` | **HIT** |
| `Ⓒ` the sign | positive on `CR` | positive | **HIT** |
| `Ⓔ` the shape | a line fits at least as well | line/step `0.00` on the full phase | **HIT** |
| `Ⓕ` the plane-wave proxy | `≥5×` and opposite sign | `−1.47300`, factor `2.93`, opposite sign | **MISS** |

**Three hits, two misses.** `Ⓐ`'s miss is the useful one: the prediction's *bound* was right and its
*statistic* was the wrong object, because a half-integer alternation is not a run and the prediction
did not think to say so. `Ⓕ` misses on the factor and holds on the sign — the superseded proxy is
wrong by `2.93×` on the phase where `r6999` measured `15×` on the modulus, so the two are not the
same failure and the proxy is less wrong here than there.

**THE PRICE:** `3.89`, `3.85`, `4.07` s.

---

*`PREDICTION.md` registered `305ae568` at `f91e3fdc`, before `phase_run.py` existed. The seed is
pinned per `L-249`'s repair rule: the historical digest at the commit it stood at, the bank's
present readability asserted separately, and the live check directional.*
