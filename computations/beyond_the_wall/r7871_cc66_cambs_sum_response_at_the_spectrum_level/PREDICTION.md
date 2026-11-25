# `r7871+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7871` (69), item ⑩: **CAMB's sum response at the spectrum level, at fixed other
parameters.** `D_ℓ(Σ)/D_ℓ(0) − 1` for TT, TE and EE at `Σ = 0.06`, `0.30` and `0.60` eV, on 60's
multipoles, **unbinned**, from CAMB with its standard massive-neutrino treatment; then the same with
CAMB's neutrino perturbations held as in 60's instrument **if CAMB exposes a way** — and if it does
not, say so and **do not build one**.

⌗ **Reconnaissance run before this file, declared so nothing reads as a prediction confirmed.** Two
facts had to be established before a band could be written at all:
- **60's control is theirs, not a choice of mine.** `model3.py` declares the `lcdm` arm's centre as
  `H0 = 67.40`, `OM = 0.3150`, `WB = 0.0224`, `NS = 0.965`, and the instrument's four fitted
  parameters are offsets from it. **τ is NOT among them** — 60 profile it over `[0.0, 0.40]` — so
  there is no control τ to read, and one must be fixed here and declared.
- **CAMB 2.0.4 does expose a perturbation knob:** `CAMBparams.MassiveNuMethod`, accepting
  `Nu_int`, `Nu_trunc`, `Nu_approx` and `Nu_best` (the default). That is a choice among **CAMB's
  own** treatments.

---

## THE BANDS

- **Ⓐ① The control is read, not chosen.** The four values above come out of 60's own module at run
  time rather than being retyped here, and the run asserts them. τ is fixed at `0.054` and **that
  choice is declared in the output**, because 60 profile τ and so supply none.
- **Ⓑ② THE RATIO IS READABLE WHERE `r7869`'s SHARE WAS NOT.** This is the band the order's own
  reasoning rests on, so it is registered sharply: raising CAMB's `lens_potential_accuracy` from `1`
  to `3` moves every ratio by **less than `1e-3` absolute** at all three sums in all three spectra.
  ⚠ If this fails, the ratio is as unreadable as the share was and item ⑩ delivers nothing — that is
  the honest failure condition and it is registered as one.
- **Ⓒ③ τ-insensitivity.** Moving τ by `±0.01` about `0.054` moves every ratio by **less than
  `5e-3` absolute** above `ℓ = 100`. Registered because 60 pin no τ, so the deliverable must not
  turn on mine. ⌗ *Below `ℓ = 100` it may well not hold — τ is what reionisation does to low `ℓ` —
  and the band is therefore written for the range 60 actually score.*
- **Ⓓ④ Sign and growth.** Every ratio is **negative** (the sum suppresses) at `ℓ > 100`, and
  `|ratio|` is **monotone increasing** in `Σ` at fixed `ℓ` across `0.06 → 0.30 → 0.60`.
- **Ⓔ⑤ The suppression grows with `ℓ` in TT** across `ℓ = 100 → 1996`, at every sum.
- **Ⓕ⑥ The three spectra do not agree.** At `Σ = 0.60` the TT and EE ratios differ by more than
  `1e-3` somewhere above `ℓ = 1000`, so "the sum suppresses the spectrum" is not one number.

## ⛔ Ⓖ⑦ THE SECOND HALF, AND I EXPECT TO REFUSE IT

`MassiveNuMethod` exists, so the literal answer to "does CAMB expose a way" is **yes, it exposes a
choice among its own four treatments**. But the order asks for CAMB's perturbations held **as in 60's
instrument**, and that is a different thing: 60's instrument counts the mass as matter at every epoch
(`r7862`), with `NUFD` supplying a Fermi–Dirac **background** — it solves no neutrino hierarchy at
all. None of `Nu_int`, `Nu_trunc`, `Nu_approx` is that.

⇒ **Registered intent: report the four-way spread as a BOUND on how much the perturbation treatment
can matter, and refuse to construct the instrument's treatment inside CAMB,** which is what the order
forbids. The band: the spread across the four settings is **smaller than the TT–EE disagreement of
`Ⓕ⑥`** at `Σ = 0.60`, so the treatment is not where the instrument's `81.94 → 185.96` meV move can
come from. ⚠ **If the spread is LARGER than that, the refusal is still right but the bound is
useless, and I will say so** rather than present a bound that bounds nothing.

## ⌗ WHAT IS NOT ASKED AND NOT DONE

No limit, no `χ²`, no binning, no instrument run, and no comparison against 60's own ratios — 69 has
60 supplying those from their banks with `NUFD` on and off. This revision supplies CAMB's side only.
