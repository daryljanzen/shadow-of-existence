# `r7856` (60) — the absolute scale located: **two factor-two errors that cancelled, and the repair broke the cancellation**

Order `r7853` (69) items ① – ④. `PREDICTION.md` registered and pushed at `ca690af46`, amended at
`fd524dd6c`, both before a line of the computation existed.

---

## ⇒ THE RESULT IN FIVE LINES

1. **The discrepancy is ONE NUMBER.** After `r7854`'s baryon repair the instrument-over-reference
   ratio is flat to `1.86` per cent across the nine bandpowers, against the landed instrument's
   `33.20`. The order's ① is answered: it is a normalisation and not a shape.
2. **The lensing path had no primordial normalisation,** and the missing factor is derivable from
   the instrument's own seed: `AMP = (4/9)·A_s·k_p^(1−ns) = 8.4042841352e-10`. ⇒ It agrees with the
   reference's own absolutely normalised Weyl power to **`0.13` per cent on the super-horizon
   modes**, with nothing fitted on either side.
3. **But the joint fit does not lack a normalisation — it hands over one that is twice too big.**
   `model6.pp_model` hands the lensing side `amp_cmb/T_CMB²·exp(+2τ) = 1.6664668460e-09`, which is
   `1.9829` times what the seed implies and `2.0412` times what the nine bandpowers want.
4. ⛔ **AND THE CARRIER IS THE CMB BANK, MEASURED AND NOT INFERRED: its binned TT at the derived
   normalisation is `0.504672` of CAMB's own, over `185` bins, range `0.500015` to `0.510557`.** A
   freely fitted amplitude cannot see a constant factor, which is why the CMB `χ²` has always read
   about `1.05` per bin.
5. ⇒ **So `r7852`'s cancellation is named in both of its factors.** The CMB bank is `2`× low, so its
   fitted amplitude is `2`× high, and the landed instrument's lensing power was `2`× low because the
   baryons never clustered. The two cancelled. `r7854` repaired the baryons, **the cancellation
   broke**, and the joint fit bought the excess lensing back with the only knob it has. ⇒ **That is
   `r7854`'s `598` meV, and it is an artefact and not a result.**

---

## Ⓞ⓪ Ⓞ⓪ᵇ — the controls, first

| | |
|---|---|
| this revision reproduces `r7854`'s landed fitted factor | `1.5768615382e-09`, to `<1e-6` |
| …and its landed per-dof | `2.1313389647`, to `<1e-6` |
| …and the repaired pair | `8.1642357010e-10`, `1.0533934590` |
| this revision reproduces `r7850`'s reference, nothing fitted | `8.8173475455` |
| …and with one amplitude fitted | `8.8074128365` at `1.0024938505` |
| `PRIMNORM` reads off when unset and on when set | `False` / `True` |

**Both hold.** So what follows reads the scale and not these files.

## Ⓐ① — the ratio is one number

| bin | `L_av` | repaired/ref | `r_i/r̄ − 1` | landed/ref | `r_i/r̄ − 1` |
|---|---|---|---|---|---|
| 1 | `28.1` | `1.229232e+09` | `+0.0089` | `8.139111e+08` | `+0.3320` |
| 5 | `195.3` | `1.218495e+09` | `+0.0001` | `5.792041e+08` | `−0.0521` |
| 9 | `377.3` | `1.200200e+09` | `−0.0150` | `5.431651e+08` | `−0.1111` |

worst `|r_i/r̄ − 1|`: **repaired `0.0186`**, landed `0.3320`, against a registered `< 0.10`.
⇒ **Ⓐ① PASSES AS REGISTERED.**

## Ⓐ①ᵇ — passed as registered, and vacuous in the direction it was aimed

`r̄ = 1.218428e+09` is not within ten per cent of `2`, so the arm passes — and the passing means
nothing: `r̄` is `1/`the fitted factor to `0.52` per cent, i.e. the instrument's missing
normalisation rather than a gap. ⌗ *The amendment at `fd524dd6c` registered that this would happen
before it was measured, and added `Ⓐ①ᵈ` as the arm this one was meant to be.*

## Ⓐ①ᶜ — ⚠ THE REGISTERED EXPECTATION IS REFUTED

Registered: *the repair moved the absolute scale AWAY from the reference.* **It moved it TOWARD.**

| | at the derived normalisation |
|---|---|
| landed | `0.5330` of the data |
| **repaired** | **`1.0294`** |

⌗ *`ratio.py` read it as "away" because all it could see was the raw vector growing by `1.9939`. The
raw vector did grow; what that growth DOES to the absolute scale could not be read until the
normalisation existed. The expectation is refuted and the criterion is unchanged.*

## Ⓐ①ᵈᵖʳᵉ — ⚠ THIS ARM'S CONCLUSION IS WITHDRAWN

The arm measured `A_cmb = 1.1111821251e+04` against `A_lens = 8.164235700977891e-10`, fifteen orders
apart, and concluded the two sides "were never put on one `AMP`". **The conclusion is withdrawn:**
`model6.pp_model` already hands one across and applies the `T_CMB²` conversion the arm omitted. The
sides *are* joined. ⌗ *`handover.py` carries the withdrawal in its own header rather than in a note,
and the arm's measured numbers stand — it is the reading of them that was wrong.*

## Ⓐ①ᵈ — one `AMP`, three readings

| | |
|---|---|
| ⑴ what the CMB side **hands over** | `1.6664668460e-09` |
| ⑵ what the instrument's **seed implies** | `8.4042841352e-10` |
| ⑶ what the nine bandpowers **want**, repaired | `8.1642357010e-10` |

`⑴/⑵ = 1.982878`,  `⑴/⑶ = 2.041179`,  **`⑵/⑶ = 1.029402`**.
⇒ **Ⓐ①ᵈ PASSES AS REGISTERED** (`|handed/wanted − 1| = 1.0412` against `0.10`).
⌗ *⑵ is the one of the three with an independent check behind it, so ⑴ is the reading that is out.*

## Ⓑ②ᵃ — the share bound holds and ⚠ THE ATTRIBUTION IS REFUTED

| `η` | `z` | radiation/matter | ratio over `k ≥ 0.02` |
|---|---|---|---|
| `500` | `482.203` | `0.14014` | `1.03498` |
| `1893` | `53.551` | `0.01582` | `1.04574` |
| `4000` | `12.833` | `0.00401` | `1.05211` |

The residual's share is **at most `0.0807`** of the gap, so the registered "less than a fifth"
**holds**. ⛔ **But a radiation-era residual dies with the radiation share and this one GROWS**, so
the candidate's attribution is refuted by the sign of its own trend.
⌗ *Its confound is bounded rather than ignored: the instrument's own `|Φ−Ψ|/Φ`, reconstructed from
the instrument's own line, reaches `0.00053` against a residual of `0.05211` — a hundredth of it —
so the residual is a measurement.*

## Ⓑ②ᵇ — the carrier, and its independent check

`AMP = (4/9)·A_s·k_p^(1−ns)`: the `(4/9)` from `|Φ| = (2/3)|ζ|` in the regime the instrument's own
seed sets (`Ph0 = −1`, `dg0 = −2·Ph0`, `dc0 = 0.75·dg0` at `ZSTART 3e7`), the pivot because this path
carries `k^(ns−1)` unpivoted.

| k [/Mpc] | repaired/reference | landed/reference |
|---|---|---|
| `0.0002` | **`1.0013`** | `1.0013` |
| `0.005` | `1.0416` | `0.8768` |
| `0.05` | `1.0596` | `0.4755` |
| `1.0` | `1.0495` | `0.5018` |

⇒ **`0.13` per cent super-horizon, nothing fitted on either side**, and the landed instrument's
sub-horizon deficit is a clean `0.500060`. Share: **`0.9193`**. ⇒ **Ⓑ②ᵇ HOLDS AS REGISTERED.**

## Ⓑ②ᶜ — passes, and ⚠ IT IS VACUOUS BY CONSTRUCTION

The pair sums to `1.0000` against a criterion of `0.80` — **an identity**, because
`share_normalisation` was formed as `1 − share_radiation_era`. ⌗ *The content is the two shares, each
measured, with nothing left unaccounted; the arm as coded could not have failed and is reported as
such rather than claimed.*

## Ⓒ③ Ⓒ③ᵇ — the repair, and ⛔ IT FAILS ITS REGISTERED BIN CLAUSE

`PRIMNORM=1` puts the derived constant inside `phiphi.clpp`; **default off**, so every banked grid is
byte-identical unset.

| scored on the nine bandpowers, **nothing fitted anywhere** | `χ²` |
|---|---|
| repaired shape × handed-over amplitude | `1551.7312` |
| landed shape × derived amplitude | `340.8400` |
| landed shape × handed-over amplitude | `30.2372` |
| **repaired shape × derived amplitude** | **`8.4297`** |
| the reference, nothing fitted | `8.8173` |

⇒ **For the first time this instrument lands on the nine bandpowers absolutely, with no fitted
amplitude, slightly better than the independent pipeline does.**

⛔ **And Ⓒ③ FAILS as registered: worst `|ratio − 1| = 0.1528` against a registered `0.10`.** The
criterion is **not moved**. What it asked for is tighter than the data can resolve: the deviations at
bins 4, 5, 6 and 8 are `+1.49`, `+1.60`, `+1.30` and `−1.29` in units of each bin's own sigma. The
`χ²` clause, which weights by those errors, passes at `1.1132` of the reference's — `11.3` per cent,
against a registered `20`.

**Ⓒ③ᵇ**: with one amplitude free the repaired vector scores `8.427148` at a factor `0.971437`, only
`0.0286` from one. ⇒ *The free amplitude is not what makes the repair land, and this row is refused
the claim: `Ⓒ③` is scored at a factor of exactly one.*

## Ⓓ④ᵃ — which side carries the two, measured and not inferred

The bank's binned TT at the derived normalisation, times `T_CMB²` and `exp(−2τ)`, against CAMB's own
lensed TT through the harness's own `plik_lite` windows at the same cosmology and `A_s`:

**geometric mean `0.504672` over `185` bins, range `0.500015` to `0.510557`.**

⇒ **The CMB bank is low by a factor of two and the lensing side is sound.**

## ⛔ Ⓓ④ — NOT ANSWERED, AND ROUTED AS THE FORK THIS REVISION REGISTERED

The registration said: *if `Ⓐ①` and `Ⓑ②` locate the scale but the repair at `Ⓒ③` is not reachable
within this revision — because it moves a quantity the CMB path shares — then this revision lands ①
and ② with the location named and the repair ROUTED as a fork, with both branches stated and this
seat's recommendation attached.*

**That is the case.** The lensing path's own repair is landed. The remaining factor two is in the
**shared CMB bank**, which every CMB score in the corpus reads, so fixing it is not "re-run the
control only" — it would move every `χ²` on this paper. ⇒ The fork is in `FOR_66_FROM_60.md`.

⌗ **And no limit is reported here.** A limit read off a configuration this revision is
simultaneously reporting as wrong by a factor two would not be a measurement, which is what `Ⓔ⑤`
registered.

## Ⓔ⑤ — what is and is not concluded

**Nothing is concluded about the neutrino mass sum.** `r7854`'s `598` meV is explained above as the
broken cancellation and is **withdrawn as a reading**; no replacement figure is offered. `P15` is
untouched by this revision, the arm of record is **NOT JUDGED**, and `72`'s batch still waits.
