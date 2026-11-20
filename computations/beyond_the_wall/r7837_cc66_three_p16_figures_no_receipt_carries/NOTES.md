# r7837 — working notes

## order of work
1. Located all three sites **before** predicting anything about them, because the order names
   `πα/3` and the paper also carries `πα/√3` at `:294`. They are different lengths (ratio `√3`)
   and conflating them was the likeliest way to get ① wrong. An arm now asserts the distinction.
2. `PREDICTION.md` pushed in its own commit (`d34f10379`) before a line of computation existed.
3. Computed item ③ first, because it was where I had registered a contradiction with `60`.

## what the three item scripts are
- `item3_dissociation.py` — the two photodissociation criteria, kept apart.
- `item1_regulated_peak.py` — `Λ(H₀,Ω_m)`, `α`, `πα/3`, the Nariai cap, the extremum in `R_s`.
- `item2_band_period.py` — the closed-form closed dust+radiation interior and the two integrals.
  (Uses `scipy`; the receipt re-implements bisection and Simpson by hand so it has no new
  dependency and the arithmetic is visible in the receipt itself.)

## things that went wrong, and what they cost
- **`60`'s receipt reads from a hardcoded `LAM = 1.1056e-52`** with no derivation from any
  `(H₀, Ω_m)`. I nearly reported that figure as "the standard model's" without checking what
  background it corresponds to. It needs `Ω_m = 0.3050` at `H₀ = 67.36`, which is not Planck's
  `(67.36, 0.3153)` — that gives `1.0891e-52`. So the receipt's `Λ` is not identified with a
  published background either, and I say only that it is not what P16's own numbers give.
- **My first failability test proved nothing.** I copied the receipt to the scratchpad and
  perturbed it; all three perturbed copies "passed" with zero red pins. They had crashed at
  import, because the receipt resolves the paper relative to `__file__`. A perturbation that
  cannot reach the pins looks exactly like a pin that does not fail. Re-run with an absolute
  path, each perturbation reddens 3–5 pins and the control stays green.
  ⇒ *GUARD: a failability probe needs a positive control — the unperturbed copy must pass by the
  same route the perturbed one fails.*
- **I registered `≥10⁴` for `r/R_s`** without evaluating it once. It is `1.8895`.

## what is NOT claimed
- `c_s = 0.018` at turnaround is used as the **input** that fixes `A/√B`, not as an independent
  check. Three of the four printed band-period figures are therefore derived from the fourth, and
  I have not derived `0.018` itself from the progenitor's radiation content. Stated as a limit.
- The NSE calculation uses the standard Saha-type criterion with order-one statistical weights
  (`g_D = 3`, `g_He4 = 1`) and `η = 6.09e-10`. It is a threshold estimate, not a network run, and
  the fork for `69` does not turn on its third digit.
- Nothing is asserted about which criterion `sec:network` *should* mean. Two numbers are supplied.
