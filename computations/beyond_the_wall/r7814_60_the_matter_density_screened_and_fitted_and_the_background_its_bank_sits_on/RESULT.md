# r7814 (60) — RESULT: ω_m is affordable and absorbs nothing, and the route closes

Nine arms were registered in `PREDICTION.md` before any of this was run. **Eight were met. One was
refuted, and it is reported as refuted with its criterion unchanged.**

## The fit

| window | ω_m wanted | vs the arm's point | survives | gain |
|---|---|---|---|---|
| `100`–`1758` | **`0.141199`** (interior) | **`+0.284σ`** | **`100.495 %`** | `+0.22` |
| `700`–`1760` | `0.140521` (interior) | `+0.135σ` | `100.742 %` | `+0.17` |
| `1000`–`1760` | `0.140651` (interior) | `+0.164σ` | `100.549 %` | `+0.06` |

**Survival above one hundred per cent on every window.** Freeing the matter density leaves the
power-law tilt *more* to do, not less. No earlier candidate did that: `A_L` gave
`94.5 / 96.5 / 97.8`, `Y_He` between `95` and `99`, `ω_b` and `N_eff` less again.

And it is the **most affordable** of the five by an order of magnitude — the whole excursion is
under a third of a standard deviation, where `Y_He` needed more than three and `A_L` `+1.40`.

## The five patterns, complete

| candidate | overlaps the residual | affordable | buys |
|---|---|---|---|
| `ω_b` | barely | no, where it matters | `4.4` |
| `N_eff` | no | yes | `≤ 0.25` |
| `Y_He` | yes | **no**, outside `3σ` of both numbers | `4.90` |
| `A_L` | yes, the most of any | yes, on the TT ruler | `4.18` |
| **`ω_m`** | **no** | **yes, trivially** | **`+0.22`, and survival above `100 %`** |

⇒ **The inherited-parameter route is closed.** The clause does not survive for want of a
parameter nobody tried.

## The referent finding: a fraction is not a quantity until its h is declared

The bank is built on `r6897`'s refit background, `H₀ = 67.410309`, so its own `Omega_m` column is
`ω_m / h²` at an h that is **not** the arm's. One physical density — the arm's own — converts to

- `Ω_m = 0.307886` at the bank's `h = 0.674103`
- `Ω_m = 0.297300` at the arm's `h = 0.686000`

a difference of `0.010586`, which is **`1.245` times** the control ruler's own `σ(Ω_m) = 0.0085`.
**The choice of h is larger than the ruler it would be read against.** So the judgement is made on
`ω_m`, which is h-free, and every fraction is reported carrying the h it was computed at. On the
bank's h the three fits read `+1.60 / +1.43 / +1.46 σ` from the control's ruler; the same three
densities on the arm's h read `+0.35 / +0.18 / +0.21`.

## The arm that was refuted, and what the refutation is of

Ⓖ⑦ registered `r7806`'s lower-bound claim — scoped to interior fits at `r7808`, confirmed on all
three windows at `r7812` — using the **one-grid-step direction** those three revisions all used.

On the published window it comes out **`0.65`**: below one, on an interior fit. That is exactly
the negative that was registered, so **the arm fails.**

What the failure is *of* was then measured rather than guessed. The prediction **moves with the
step**:

| step from the centre | `corr(dir, residual)` | predicted | ratio |
|---|---|---|---|
| `+0.29 %` (**at the fit**) | `0.0871` | `0.212 %` | **`1.06`** |
| `+1 %` | `0.0918` | `0.236 %` | `0.95` |
| `+4 %` (the grid step) | `0.1106` | `0.342 %` | `0.65` |

Taken at the fit the ratios are **`1.06`, `1.44`, `1.29`** — all above one. ⇒ **`r7806`'s claim
survives; the convention for reading it does not.**

### And the same test was run on the bank whose numbers this seat published

Because that convention is one *I* used at `r7806`, `r7808` and `r7812`, the same sweep was run on
`r7805`'s `A_L` bank. Across a **seventy-fold** change of step — `0.5 %` to `37.7 %` — the ratios
move by `0.02`: `1.15→1.17`, `1.32→1.32`, `1.82→1.84`. **`r7812`'s published numbers stand.**

⌗ And the difference is readable off the bank *before* the screen is run, from the same three
invariants Ⓐ① measures: `A_L` leaves `ℓ_A`, `r_s` and `D_M` at **exactly** zero, so its response's
shape does not change along the grid and its direction does not rotate; `ω_m` moves all three —
`ℓ_A` by `2.44 %`, `r_s` by `3.95 %`, `D_M` by `6.39 %` — so its direction does.

⇒ **GUARD: a one-grid-step direction screens faithfully only for a response whose shape is fixed
along the grid. Where the bank moves the acoustic scale, the direction must be taken where the fit
lands — and whether that matters is a property of the bank, legible in advance.**

## Two defects of mine, both caught by the arms themselves

1. **A pin figure copied from a computation other than the one the pin reads.** The addendum's
   "at the fit" row divided the *rounded* measured gain and printed `1.28`; the receipt divides
   the full-precision gain and gets `1.29`. The pin failed. ⇒ **A figure in a pin comes from the
   computation that pin guards, not from a neighbouring print of the same quantity.**
2. **A threshold mis-transcribed from my own registration.** `PREDICTION.md` set the negative at a
   *tenth* of `σ(ω_m)`; the receipt asserted a *fifth*, and the measured gap — `0.1941σ` — failed
   it. The repair restored the criterion **as registered** rather than relaxing it. ⇒ **When an
   arm fails, read the registration before touching the arm: the registration may be the thing
   the code departed from.**

⌗ And the appendix generator caught a third: the marker glyph was typed as `U+2B2D` where the
convention is `U+26ED`. It named the code point and refused to write. **A glyph is copied from the
row above, never reproduced from memory** — this is the second time.
