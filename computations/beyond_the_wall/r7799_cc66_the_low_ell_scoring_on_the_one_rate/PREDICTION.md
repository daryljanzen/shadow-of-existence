# `r7799+cc66` — REGISTRATION ONLY: the low-ℓ sector's scoring on the one-rate depths

**Registered before any of the three computations exists.** What is read at registration time is the
existing instruments' source and the banked legs — not their output on the one rate.

69's order: ① re-score the low multipoles on the one-rate depths with the same exact cosmic-variance
likelihood (Δ(−2 ln L) over 2–8 and 2–10, its range across the octopole estimator, per-multipole
ℓ = 2…5); ② the quadrupole-only statistic on the one rate beside ΛCDM's 6.7 %; ③ the frozen build on
the one rate, converged in its late step count, against the exact transfer and the decoupled build.

---

## ① The scoring

The instrument is `computations/perturbation_verify/verify_lowell_likelihood_v2.py`, whose one
declared law is
`Δ(−2 ln L)_ℓ = (2ℓ+1)[ r_ℓ (1/d_ℓ − 1) + ln d_ℓ ]`, `r_ℓ = observed/ΛCDM`, summed ℓ = 2…10, with
`obs_central = {2: 0.20, 3: 0.75, 4: 0.70, ≥5: 1.0}` and the octopole bracket `0.60 / 0.95`.

### R1 — the paper's printed figures are the ARM OF RECORD's, not the cited receipt's

**PREDICT** that running that instrument's own source with only its `depth` dict replaced by the
arm-of-record (L) depths reproduces the paper's printed set: per-multipole **−2.56, +0.93, +2.16,
+1.12** (printed −2.6, +0.9, +2.2, +1.1), total **+1.717** (printed +1.72), octopole range
**+0.384 … +3.494** (printed +0.4 … +3.5).

⛔ **And that the receipt `P15_verify_lowell_likelihood_v2.py` cited beside those figures pins a
DIFFERENT set** — `−2.63 / +1.31 / +2.10`, total `+1.80`, range `+0.29 … +3.82` — because it still
runs on the older **control** depths `0.473 / 0.410 / 0.356 / 0.676`. *So the receipt named beside the
paper's scoring does not compute the paper's scoring.* **FAILS IF** either set is not reproduced, or
if the two turn out to agree after all.

### R2 — the one-rate scoring

**PREDICT** on the one-rate depths: per-multipole **−2.53, +0.99, +2.02, +1.03**, total **+1.573**,
range **+0.210 … +3.391**. ⇒ **The net IMPROVES by 0.14**, from +1.72 to **+1.57**: the one rate is
*less* disfavoured, not more. **FAILS IF** any figure moves, or if the net worsens.

### R3 — why 2–8 and 2–10 give the same number, which is a reason and not a coincidence

**PREDICT** the two ranges agree **exactly** on both clocks, because `d_ℓ = 1` and `r_ℓ = 1` at
ℓ = 9, 10 make those terms identically zero. **FAILS IF** they differ at any printed precision, or if
the ℓ = 9, 10 terms are not exactly zero.

---

## ② The quadrupole-only statistic

The instrument is `P15_the_selective_quadrupole_suppression_is_the_skys_own_and_lcdm_carries_it_at_the_same_size.py`:
`R = (Ĉ₂/C₂^ΛCDM)/(Ĉ₃/C₃^ΛCDM)` on Gaussian isotropic skies, `R/(d₂/d₃) ~ F(5,7)` exactly, observed
`R = 0.20/0.84`.

### R4 — the one-rate share

**PREDICT** `p_CR = 0.0531` on the one-rate depths — **5.3 %** — against ΛCDM's `0.0667`, **6.7 %**,
which is the figure the paper prints and which does not move because it is the `d₂ = d₃ = 1` case.
**FAILS IF** either moves, or if ΛCDM's turns out to depend on the depths.

### R5 — ⛔ and the paper prints TWO values for this one statistic

**PREDICT** `sec:largescale` carries `$p=0.056$` while `sec:scope` carries `$5.4$ per cent`, and that
they differ because they are evaluated on **different depth inputs**: `0.056` is what the receipt gets
from the paper's own **two-decimal** sentence (`0.48 / 0.44` → `0.0564`), while `5.4` matches the
**`0.487 / 0.435`** adjudicated-background set (`0.0537`). The arm-of-record four-decimal depths give
`0.0555`, i.e. **5.6 %, which is neither printed value**.
*So one statistic is printed twice, on two inputs — the same class as the comb and the 1.06/1.4967.*
**FAILS IF** the paper does not carry both, or if some single depth set yields both.

---

## ③ The frozen build on the one rate

### R6 — the (L) baseline the paper prints

**PREDICT** the paper's `3.2` and `1.9` are the **h2** (most converged) frozen leg at the
**distances** point under (L): against arm A's exact transfer **3.17 %** (max over ℓ = 2…8, at ℓ = 4)
and against the decoupled build **1.81 %** (at ℓ = 3). **FAILS IF** either differs, or if the figures
turn out to be the refit point's.

### R7 — ⛔ THE ONE-RATE CONVERGED LEG IS NOT BANKED, and this row says so before measuring

**PREDICT** that `p15_lowell_depths_frozen_converged_leafrec1.npz` carries converged **(L)** legs at
the distances and refit points but its **one-clock** legs only at the **control** point
(`NS3_900 / 1800 / 2400 / h2`) — so **there is no converged one-rate frozen leg at the distances
point**, and ③ cannot be answered from the bank alone.

⇒ **What I will do instead, declared now rather than improvised later:** measure the convergence
correction on the one clock at the control point (`NS3_900 → h2`), measure the (L) correction at the
distances point (`NS3_1800 → h2`), and test whether the correction is clock-stable. **If it is**,
carry it onto the banked unconverged one-rate distances leg and report the result **as a carry,
labelled, with the correction's own size beside it**. **If it is not**, report that ③ needs an
instrument run and do not manufacture a figure.
**FAILS IF** I report a converged one-rate figure without either a banked leg or a measured and
declared carry.

### R8 — what is NOT claimed

No likelihood beyond the one the paper already uses; no new instrument run in this receipt; no claim
about which depths the paper *should* score on, or which of its two quadrupole-only values is the
right one to keep — both are 69's.

## Failability

To be **measured**, not asserted: perturbing the depth inputs must move the scoring rows and leave
the paper-parse and law-structure rows green.
