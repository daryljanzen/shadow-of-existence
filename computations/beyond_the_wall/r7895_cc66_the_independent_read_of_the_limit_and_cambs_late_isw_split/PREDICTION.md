---
kind: PREDICTION
revision: r7895+cc66
order: r7895 (69) item ⑱
---

# r7895+cc66 — REGISTERED BEFORE READING: THE BAND ON THE LIMIT, THE DEFINITION OF MY 30.56, AND THE LATE-ISW SPLIT

Order `r7895` (69) item ⑱, four parts. ⑱① says in its own words: **"Register your band from your
own reproduction history before reading."** This file is that registration. **No line of the
computation exists at this commit**, and the limit has not been read.

## Ⓐ① THE INPUTS, NAMED SO THEY CANNOT BE SWAPPED LATER

- the ten lensing points: `refs/ci/r7884_phiphi` at **`133e612fe`**, from run **`46016816497`**.
- `60`'s method and registration: `computations/beyond_the_wall/r7884_60_the_controls_limits_on_the_jointly_validated_sector/`
  (which registered the split and **did not** read the limit) and `r7888_60_the_limit_read_on_the_runners_complete_grid/`
  (which read it).
- `60`'s figure under test: **`193.545` meV**, calibrated column, hierarchy ON, envelope CLOSED.
  Its stated controls: `185.95834` raw / `185.95842` env on `r7870`'s rung with the hierarchy OFF,
  so closure contributes `+0.00008` meV and the remaining `+7.587` meV is the hierarchy's.

## Ⓑ② THE BAND — AND IT IS DERIVED, NOT CHOSEN

Two sources of spread, and they are **not** the same thing. Registering both separately is the point:

**⒜ Reproduction spread (mine against myself).** My limit reader is `limit95` — the first
interpolated crossing of `Δχ² = 2.71` on a `200001`-point grid between the extreme sums. Re-reading
the same points with the same method is exact: `r7853` produced `30.560000000000002` and `r7863`
carried `54.00000000000001`, i.e. agreement to `~1e-14`. The grid's own resolution is
`(Σmax − Σmin)/200000`, which for any sum range in play here is **below `0.001` meV**.
⇒ **Reproduction spread cannot account for a disagreement above `0.01` meV.**

**⒝ Instrument spread (mine against `60`'s).** My fitter has reproduced `60`'s **amplitudes** to
`3e-06` (`r7875`), `8.818e-06` (`r7877`), `1.039197e-05` (`r7879`) and `6.998106e-06` (`r7885`) —
worst relative `1.04e-05` over `32` fits. A limit is a crossing, not an amplitude, so that figure
does not transfer directly; it bounds how far my spectra sit from `60`'s, not how far the crossing
moves. I will not pretend it converts. **So the band is set by ⒜ and widened once, for the
crossing's first-order sensitivity to a χ² offset, to `1.0` meV — about `0.5` per cent of `193.545`.**

⇒ **REGISTERED BAND: `|mine − 193.545| ≤ 1.0` meV is agreement.** Above that is disagreement and the
finding is mine to state. ⌗ *I register the band this tight ON PURPOSE. `60`'s number sits `6.333 ×`
my `30.56`; a band loose enough to absorb a `6 ×` discrepancy would make the test vacuous, and a
band at the reproduction floor is the only one that can tell "the same quantity, computed twice"
from "two different quantities".*

## ⛔ Ⓒ③ THE DEFINITIONAL MISMATCHES, REGISTERED IN ADVANCE AS NOT-A-DISAGREEMENT

Read from my own records **before** reading the limit. If the comparison fails, these are candidate
causes that are **not** a disagreement about the physics — and naming them now is what stops me
attributing a definitional gap to the repair later, or excusing a real gap as definitional:

| | mine, from my record | `60`'s |
|---|---|---|
| bins | **full `613` plik_lite bins**; `r7847`'s own note: *"60's own 555-bin mask is NOT reproducible here"* | `555`-bin mask |
| Δχ² baseline | `base = pts[0][1]` — the **lowest-sum point** of the set (`r7863`'s `limit95`) | `calibrated` and `minimised` columns |
| τ | **profiled** by `minimize_scalar` | per `r7884`'s registration |
| amplitude | plik_lite's **closed-form single amplitude** | same half, per `r7847` |
| ruler | `rd_camb` → `30.56`; `rd_min` → `54.00` | `calibrated` / `minimised` |

⇒ **Ⓒ③ fires if** my read lands outside the band AND the `613`/`555` bin sets differ on these ten
points. Then the honest verdict is *"not the same quantity"*, which is `60`'s Ⓡ⓶ question, and
**not** a refutation of `193.545`.

## Ⓓ④ WHAT ⑱② OWES, FROM THE RECORD AND NOT RECONSTRUCTED

`30.56` meV is `uncut_meV.rd_camb` and `54.00` meV is `uncut_meV.rd_min` in
`r7863/cuts_and_node.json`, both originating in `r7853/likeforlike.json` against the corpus's
published `64.2`. **They are the same likelihood, bins and covariance and differ only in the ruler.**
Likelihood: `60`'s own CMB half (`score_ttteee.chi2_of` — plik_lite 2018 TT/TE/EE, their covariance,
their closed-form single amplitude) **plus** `lensing_like` **plus** a τ prior
(`LL.chi2_tau`, mean `TAU_MEAN`, sigma `TAU_SIGMA`). Σ is the scanned parameter.

## Ⓔ⑤ THE LATE-ISW SPLIT, REGISTERED BEFORE IT RUNS

TT at `ℓ = 100–207`, with and without the late-time ISW contribution, at `Σ = 0, 0.06, 0.30, 0.60` eV
on the reference's parameters. **Registered in advance:** the split is computed by CAMB's own source
terms, not by a hand-subtraction, and the no-ISW leg must differ from the full leg **somewhere** in
`100–207` or the split is inert and I report it as inert rather than as a measurement. A leg pair
that comes back bit-identical is the `r7879` ⑯ signature — three settings on one code path — and I
will claim only the weaker reading if it appears.

## Ⓕ⑥ ⑱④ IS A READING AND IS ANSWERED AS ONE

`60`'s `r7892` observes that `12` of the `13` sub-peak TT bins where the late ISW could not be read
are exactly the `12` carrying the low-end move. I will state whether I read that as `60` does or as
over-reading, **with the overlap recomputed from the bin lists rather than taken on report**, and I
will say which it is even if it is the less useful answer.

## Ⓖ⑦ WHAT WOULD MAKE THIS REVISION WRONG

- the limit read and reported without the band above having been registered first — this file;
- agreement claimed on a band widened after seeing the number;
- the `613`/`555` difference discovered after the fact and used to explain a gap it was not
  measured to cause;
- a bit-identical ISW leg pair reported as a measured split.
