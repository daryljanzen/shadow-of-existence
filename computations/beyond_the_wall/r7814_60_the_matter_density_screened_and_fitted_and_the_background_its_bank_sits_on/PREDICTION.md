# r7814 (60) — PRE-REGISTRATION: ω_m screened, fitted, and judged on both rulers

**Order `r7813` (69):** *"ω_m now. It is `spectra/r7809_omm_response_lcdm.npz`: Ω_m at fixed h,
±4 and ±8 per cent, centre equal to `r6897`'s (70, `r7811`+70.1). Judge it on both rulers, as
registered. If it closes, write the `sec:coherence` sentence that PO-24 waits on data alone, as
one state."*

This file is committed and pushed **before** the screen or the fit is run.

---

## 0. What is ALREADY READ, and is therefore not predicted

The bank was opened to confirm it exists and to establish its conventions. These are
**measurements already on the screen**, recorded here so that nothing below can be mistaken for
a prediction that was written afterwards:

| read | value |
|---|---|
| grid, `omega_m` | `0.129526, 0.135158, 0.140790, 0.146421, 0.152053` |
| its own `Omega_m` column | `0.28503902, 0.29743298, 0.30982694, 0.32221869, 0.33461265` |
| centre **by value** | `omega_m = 0.140790` (`config.bank.LOM_centre = 0.309826`) |
| offsets from that centre | `−8.0006, −4.0003, 0, +3.9996, +7.9999` per cent |
| the bank's own background | `LH0 = 67.410309`, `WBH2 = 0.021966`, `NS = 0.954248` |
| `config.bank.what` | *"Omega_m at fixed h, so Omega_Lambda and D_M move with it), control (lcdm) at r6897 refit background"* |
| ℓ grid | `100 … 1996`, step `8`, `238` points |

⌗ **The `r7812` hazard is checked and NOT instantiated here**: this grid has five values and is
symmetric about its centre, so the midpoint *by index* and the centre *by value* coincide. The
arm below asserts that they coincide, as a number on the record, and every pick is still taken
by value — the point of that guard is that "they happen to coincide" is a fact to be measured,
not a reason to stop measuring it.

⌗ **And the convention that is NOT in the array, for the fourth bank running.** This bank holds
an `Omega_m` column, and that column is *not* the arm's Ω_m. It is `omega_m / h²` at the bank's
own `h = 0.674103`, which is `r6897`'s refit background — **not** the published arm's
`(68.60, 0.2973)` that `r7810` established as where the spectra are computed. So the bank's
centre and the arm's own point are two different points, and an excursion quoted from one is
not an excursion from the other.

---

## 1. The referents, fixed before the fit (all from `r7810`, which established them)

| | |
|---|---|
| the arm's own BAO minimum | `Ω_m = 0.2974` at `H₀ = 68.62` |
| its rounding, which the spectra use | `Ω_m = 0.2973` at `H₀ = 68.60` |
| the arm's ruler | `σ(ω_m) = 0.004543` |
| the control's ruler | `Ω_m = 0.2971 ± 0.0085` |
| the arm's own TT minimum | `Ω_m = 0.2912`, **`−0.673σ`** from its own BAO minimum, paying `Δχ² = +0.524` |

**The standing disagreement is the thing this revision must be read against.** For `ω_b`,
`N_eff`, `Y_He` and `A_L` the corpus had no competing preference in the parameter being freed.
Here it has two, and they already disagree by `−0.673σ`. A fit that wants `ω_m` **lower** moves
*toward* the arm's own TT preference and *away* from its BAO one; a fit that wants it **higher**
moves away from both.

---

## 2. THE ARMS — each a comparison, each with a reachable negative

**Ⓐ① The bank moves the acoustic scale, and all three of its measures.**
`ℓ_A`, `r_s` and `D_M` each vary across the grid by more than one part in a thousand.
*Negative, reachable:* any of the three flat to that precision, as `Y_He` and `A_L` were at
**exactly** zero on all three. If this fires, `ω_m` enters the same class as those two and the
ratio-to-centre treatment is the wrong one.

**Ⓑ② The centre by value equals the midpoint by index on this grid, and both are `0.140790`.**
*Negative, reachable:* they differ, as they did on `r7805`'s seven-value grid, where the
midpoint was `1.1` and the centre `1.0`.

**Ⓒ③ The bank's background is NOT the arm's published background, and the gap is stateable.**
The bank's centre `ω_m = 0.140790` against the arm's published point `0.2973 × 0.6860²`.
*Negative, reachable:* they agree to within a tenth of `σ(ω_m)`, in which case the distinction
this revision is about does not arise.

**Ⓓ④ The Ω_m ruler cannot be applied without first declaring an h, and the ambiguity is not
small.** The same fitted `ω_m` converts to two different `Ω_m` — one at the bank's
`h = 0.674103`, one at the arm's `h = 0.6860` — and the two differ by more than `σ(Ω_m) = 0.0085`.
*Negative, reachable:* the difference comes out below that σ, in which case the choice of h is
immaterial and the control's ruler can be applied directly.
⇒ If this arm holds, **the honest judgement is on `ω_m`, which is h-free**, and the `Ω_m`
statement is a derived one that carries its h with it.

**Ⓔ⑤ The screen, run BEFORE the fit** (`r7804`'s): `corr(direction, residual-the-tilt-leaves)`
on each window, beside the four already banked — `N_eff −0.034/+0.134/+0.180`,
`ω_b −0.343/−0.096/+0.134`, `Y_He +0.303/+0.176/+0.306`, `A_L +0.359/+0.427/+0.160`.
**Registered as a comparison, not a prediction of sign or size:** either `ω_m` reaches the
`0.35` that `A_L` was the first to cross on the published window, or it does not, and **both
outcomes are reported as measured**. What is predicted is only that the screen is run and read
first, and that a direction scoring near zero against the residual cannot then buy much in the
fit.

**Ⓕ⑥ The fit, on the three published windows** `(100,1758)`, `(700,1760)`, `(1000,1760)`.
*Registered before it runs:* if the fitted `ω_m` lands on the grid's edge (`±8 %`) it is a
**BOUND and not a fit**, and must be reported as one — the `r7808` lesson, which `r7812` then
turned into a fit when the grid widened. *Negative, reachable:* an interior optimum, which is
a fit.

**Ⓖ⑦ The screen's incremental prediction is a lower bound on the fit's gain, for INTERIOR fits.**
`corr(dir, residual)² × (1 − corr(sig, tilt)²) × 100` against the measured `a₃ − a₂`.
This is `r7806`'s claim, scope-cut to interior fits at `r7808` and confirmed on all three
windows at `r7812`. *Negative, reachable:* an interior window whose measured gain falls below
its prediction, which would break the claim on its fourth test rather than its first.

**Ⓗ⑧ The excursion, reported absolutely and on both rulers, with its direction named.**
The fitted `ω_m` in absolute units; its distance from the arm's published point in units of
`σ(ω_m) = 0.004543`; its `Ω_m` at each of the two h's with the h stated; and whether it moves
toward or away from the arm's own TT minimum at `−0.673σ`.
*Negative, reachable:* a fit so close to the centre that no direction is resolvable.

**Ⓘ⑨ The verdict on PO-24's inherited-parameter route.** If `ω_m` is the fifth candidate to
fail — by not overlapping the residual, or by overlapping it and being unaffordable, or by
being affordable and buying little — then the route is closed and the row stands data-gated.
*Negative, reachable, and it is the one that would matter most:* `ω_m` overlaps the residual,
is affordable on both rulers, and absorbs a large share. **That outcome would not close the
row; it would terminate PO-24 the other way**, and it is reported as such if it happens.

---

## 3. Arm count

**Nine arms are registered above.** The receipt asserts at its end that it ran exactly nine and
reports any that failed **as failed**, with the criteria as written here and not rewritten.

## 4. What this revision does NOT do

It does not touch another seat's receipt, the instrument, or any gate. It does not write a
tracked artefact from the receipt (`r7812`'s defect). It does not rewrite `sec:coherence`'s
closing sentence unless Ⓘ⑨ actually closes the route — and if it closes it, that sentence is
written **as one state**, which is the form `69` has now corrected into this seat three times.
