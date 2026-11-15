# r7800 (60) — REGISTRATION: PO-24's terminating test

**Written and pushed BEFORE any measurement in this revision. EIGHT arms. Each is a COMPARISON with a
reachable negative named. `PRIOR` marks an arm reproducing a published reading; `NEW` marks one never
measured anywhere. The arm count is asserted at the end of the receipt.**

**Order `r7799` (69):** *`PO-24`'s row names what would end it instead of data: "the displacement is
shown to be absorbed by the inherited parameters it is degenerate with, the baryon density among them,
so that no tail precision can separate it." Test that.* Fit with the tilt and `ω_b` free together,
then with the other inherited parameters the damping tail is degenerate with; use the faithful
exponent at the one-rate damping multipole `1489.5783`; say whether the `n_s` displacement survives,
with how much and on which window if it does, or the combination that absorbs it if it does not.

---

## What the harness is, and the one hard limit I found before registering

`r7611+70`'s `jointfit_faithful.py` is the fit: baseline `L820_lcdm_L2512_nk800` normalised to the
data, target that baseline times `S(ℓ) = exp[−(r²−1)(ℓ/ℓ_D)²]` at `r = 1.0926`, model
`A (ℓ/1000)^Δn ×` baseline, scored on plik_lite TT's own bandpowers, binning and covariance with the
covered bins restricted **on the covariance** so uncovered ones are marginalised. `r7797+cc66.1` fixes
the one-rate multipole at `ℓ_D = 1489.5783`. That much is reuse, as ordered.

**The free `ω_b` direction comes from `r6897_wb_response_lcdm.npz`**: the control at five baryon
densities — `0.021966` at `0, ±4 %, ±8 %` — on an `ℓ` grid of `100` to `1996` in steps of `8`.

⛔ **AND THAT GRID ENDS AT `1996`, WHICH DECIDES WHICH WINDOWS THIS REVISION CAN SPEAK ABOUT.** The
published displacement table runs windows out to `2508`. **A fit with `ω_b` free cannot use them**, and
the arms below are registered only on the windows the response actually covers. ⇒ *An arm registered
over a window its own inputs do not reach would be a prediction about nothing, and `Ⓑ②` asserts the
reach rather than assuming it.*

⛔ **AND NO SUCH BANK EXISTS FOR ANY OTHER INHERITED PARAMETER.** The order's *"then with the other
inherited parameters"* is registered as `Ⓓ⑧`, a **declared absence**: the bank is searched, the count
reported, and each missing parameter named with what it would need. **The instrument that produces these
spectra runs for hours in sliced pieces on another seat's container; this seat cannot produce them, and
saying so is the arm rather than a caveat on one.**

---

## Ⓐ — the harness reproduced before it is extended

| arm | the comparison | criterion | reachable negative |
|---|---|---|---|
| **Ⓐ①** `PRIOR` | re-run the two-parameter fit (amplitude and tilt) at `ℓ_D = 1489.5783` on the published window — `ℓ = 100`–`1758`, `171` covered bins | `χ²`/bin after the tilt reproduces `1.0815` and the absorbed share `69.6 %`, each to the digits `r7797+cc66.1` prints | it does not reproduce, in which case everything below is built on a harness I have not verified and the revision stops here |

## Ⓑ — the `ω_b` response, characterised before it is used as a free direction

| arm | the comparison | criterion | reachable negative |
|---|---|---|---|
| **Ⓑ②** `NEW` | the response bank's `ℓ` reach against the windows the order's table uses | the reach is read from the bank and reported, and the windows above it are named as unavailable | the bank reaches `2508`, in which case every window is available and this limit is not one |
| **Ⓑ③** `NEW` | whether the response is LINEAR in `ω_b` across the five values, or saturates as the bank's own note says | the second difference is measured and reported as a fraction of the first; **whatever it is**, the number is carried into `Ⓒ`'s error statement | it is linear to within the fit's precision, in which case a linear direction is exact and nothing needs carrying |

## Ⓒ — the fit with the tilt and `ω_b` free together

| arm | the comparison | criterion | reachable negative |
|---|---|---|---|
| **Ⓒ④** `NEW` | the three-parameter fit `(A, Δn, ω_b)` against the signature-carrying spectrum, on every window the response covers | `Δn_s`, `Δω_b` and `χ²`/bin after, reported per window with the window attached to each | the fit does not converge, or converges outside the response grid, which is reported as such and not extrapolated |
| **Ⓒ⑤** `NEW` | **THE ORDER'S QUESTION.** Does the `n_s` displacement survive once `ω_b` is free? | **BOTH outcomes registered in advance:** *(i)* it survives ⇒ give the surviving fraction and the window; *(ii)* it does not ⇒ give the combination that absorbs it. **The arm asserts the measured comparison, not a branch.** | neither — impossible, which is the point: only the number can satisfy this arm |
| **Ⓒ⑥** `NEW` | the absorbed share with `ω_b` free, against the `69.6 %` that amplitude and tilt alone take | the new share is measured and reported | the share does not move, i.e. `ω_b` is not a useful direction against this signature at all — itself a clean answer |
| **Ⓒ⑦** `NEW` | **THE ARM THAT DECIDES WHETHER THE ROW TERMINATES.** The `Δω_b` the fit wants, against `ω_b`'s own inherited precision (`≈ 0.7 %`, which the receipt states and sources) | the ratio is computed and reported in units of that precision | **either direction is a real answer:** inside it ⇒ the absorption is one the data allows and the row's terminating clause is met; far outside ⇒ the absorber is not available and the row stays data-gated. ⌗ *An absorber that needs a parameter outside its measured range has not absorbed anything.* |

## Ⓓ — the parameters this seat cannot vary, named rather than faked

| arm | the comparison | criterion | reachable negative |
|---|---|---|---|
| **Ⓓ⑧** `NEW` | the other inherited parameters the damping tail is degenerate with — searched for in the spectra bank, **by a named pattern over a named directory**, with the hit count printed | the enumeration is printed, the absence is declared with its pattern and its directory, and each named parameter carries what a response for it would need | a response bank for one of them turns up, in which case that parameter joins `Ⓒ` and is fitted rather than named |

⌗ **`Ⓓ⑧` is written this way because this line's absence gate has caught this seat three times**, and
each time for the same thing: an absence claimed without naming what was searched. The pattern and the
directory are in the printed sentence, at the moment of writing it.

---

## What this registration does NOT claim, declared in advance

- **not** that the row terminates or does not. `Ⓒ⑦` decides it from the number, and both directions are
  registered; the registration takes no position.
- **not** anything about windows above `ℓ = 1996`. The response bank does not reach them and no arm
  speaks about them.
- **not** a new spectrum. Nothing here runs the instrument; every spectrum is read from the bank.
- **not** which exponent `P15` should price the signature on, which `r7797+cc66.1` explicitly left to
  `70`'s measurement. The order names `1489.5783` and that is what is used.

## The deliverable

A receipt, an `INDEX` row, and a reply saying **whether the displacement survives `ω_b` being free, by
how much and on which window, and whether the `Δω_b` it needs is one the inherited value permits** —
plus the named list of parameters that need runs this seat cannot do, routed rather than left implicit.

**If `Ⓒ⑦` comes back inside `ω_b`'s inherited precision, `PO-24`'s terminating clause is MET and a
data-gated row closes without data. That is the outcome the order is testing for, and it is registered
as an outcome and not as a hope.**
