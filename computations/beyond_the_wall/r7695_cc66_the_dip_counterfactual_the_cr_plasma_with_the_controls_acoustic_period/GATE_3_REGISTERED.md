# `r7695` (cc66) — **GATE 3, AND THE `0.54` PER CENT QUESTION IS ANSWERED. REGISTERED BEFORE THE REBUILD IS LAUNCHED**

*Gates 1, 2a and 2b passed on the switch. Gate 3 — "the comb period in the output must come out at
the control's" — needs the rebuild. **That sentence has no content until it names WHICH period, in
WHICH coordinate, read by WHICH fitter**, so this is registered with the criterion and the tolerance
fixed in advance, and with the switch's value MEASURED rather than reasoned to.*

## ⛭⛭ ① **THE ORDER'S `0.54` PER CENT IS THE FITTED SOURCE-COMB PERIOD RATIO, NOT AN `r_s` RATIO — AND MY `0.82` WAS A DIFFERENT QUANTITY, NOT A CORRECTION**

At `r7695` I reported *"the stretch is `0.82` per cent on the banks I can read, not the `0.54` the
order states"*, and registered **which pair is `0.54` measured on?** as a question rather than
resolving it by picking the number that suited the file I was editing. ⇒ **It is measured on the same
two banks, by the statistic's own comb fitter:**

| quantity | value | per cent |
|---|---|---|
| `r_s(cr) / r_s(lcdm)` | `1.008188678` | **`+0.8189`** |
| the **source** comb's fitted period ratio `T_K(cr)/T_K(lcdm)` | `0.994591937` | **`−0.5408`** |
| the `D_l` comb's fitted period ratio `T_L(cr)/T_L(lcdm)` | `0.995293535` | `−0.4706` |

⇒ *** Both numbers were right about different objects, and NEITHER of us was wrong. *** *`0.82` is the
sound horizon's ratio; `0.54` is the ratio of the two arms' **fitted comb periods** in the coordinate
the retention statistic reads, `QK = k r_s / π`. ⌗ **And the gap between them is physics, not
bookkeeping: the comb does not sit exactly at `k r_s`.*** *Normalising by each arm's own `r_s` would
put both periods at the same value if it did; the fit says `T_K = 1.0170` on the control and `1.0115`
on the arm. `S_i²` is a SQUARE, so a period near `1` rather than `2` is the expected place for it;
what is not forced is that the two differ, and they differ by `0.54` per cent and not by `0.82`.*

## ⛔⛔ ② **SO THE SWITCH'S VALUE IS NOT THE ONE I ROUTED, AND THE DIFFERENCE IS 50 PER CENT OF THE CORRECTION**

`COMBRHO` multiplies the solver's `k`, so an oscillation of period `T_a` in `QK` comes out at
`T_a / ρ`. Matching the control wants **`ρ = T_a / T_c`**.

```
COMBRHO = T_K(cr) / T_K(lcdm) = 1.011500 / 1.017000 = 0.9945919371
```

⛔ *** Had I set it from the `r_s` ratio — `0.9918778` — I would have overshot the correction by half
again, and gate 3 would have caught it only AFTER a 1–1.5 hour rebuild. *** ⌗ *The `1.0081886775` of
gate 2b was a WIRING gate: "the output must move" is direction- and magnitude-agnostic, so that gate
was sound and tells me nothing about this number.* ⇒ **Arm ① of the registration again: establish what
a number is OF before building on it. Twice now in one revision it has changed the job.**

## ⚑ GATE 3, WITH ITS TOLERANCE TAKEN FROM THE FITTER AND NOT FROM ME

`fit_period` is a grid search, `np.linspace(0.90, 1.20, 1201)` ⇒ **its resolution is exactly
`2.5e-4`**, and the half-grid control (fitting each arm on alternate modes) spreads `0.00025` on the
control and `0.00000` on the arm.

| | |
|---|---|
| **the gate** | `T_K` of the rebuilt CR source, fitted by `own_comb.comb(QK, S_i²)`, equals the control's `1.017000` |
| **the tolerance** | `≤ 5e-4`, **two grid steps** of the fitter — not a number I chose for the answer |
| **the move it must make** | `1.011500 → 1.017000`, i.e. `+0.0055`, which is **22 ×** the fitter's own half-grid spread |
| **and a second gate** | the rebuilt bank's `r_s`, `D_M` and `l_A` must be **UNCHANGED** from the arm of record's |

⌗ *The second gate is what separates "the CR plasma with the control's acoustic period" from "a
different cosmology". `COMBRHO` is applied to the solver's `k` inside `hier_run` and to nothing else;
if the background moved, the counterfactual would be a different arm and not a re-combed one.*

## ⚑ A REGISTERED PREDICTION THAT GATE 3 DOES NOT COVER, AND IT IS THE INTERESTING ONE

The two sides' period ratios are **not equal**: `−0.5408` on the source, `−0.4706` on `D_l`. Gate 3
matches the SOURCE side exactly, by construction. **What happens to the `D_l` side is a measurement.**

⇒ **I register that `T_L` comes out at the control's to within the fitter's own two steps as well** —
*low-to-moderate confidence.* ⌗ *The licence either way:*
- **It does** ⇒ the `D_l` comb's period difference is **inherited from the plasma**, and the
  projection adds none of its own.
- **It does not** ⇒ **part of the `D_l` comb's period difference is the projection's geometry**
  (`l_A`, `D_M`) and not the plasma's, which would mean the own-comb statistic's `L`-side remap is
  correcting two things at once. ⛭ *That would be a finding about the statistic and not about this
  counterfactual, and it is worth more than the counterfactual's own answer.*

⌗ *Registered now because `0.4706` and `0.5408` differ by more than the fitter's resolution — so
there IS something to predict — and because the comfortable report is the one that mentions only the
side the gate covers.*

## WHAT IS BEING RUN

The **source-and-pairs** rebuild on the CR arm, which is what `_BR` — the dip test's own banks — is
built from: six `SRCSAVE` slices and six `SRCDEC` slices of 250 modes, `LSTEP=8 LMAXL=2000`, at the
arm of record's point with `LEAFREC=1`, and `COMBRHO=0.9945919371`. ⛔ **Banked under new stems**
(`r7695_source_cr_combrho`, `r7695_pairs_cr_combrho`) **and never over the arm of record's banks** —
a counterfactual that overwrote the thing it is a counterfactual TO would destroy its own comparison.
