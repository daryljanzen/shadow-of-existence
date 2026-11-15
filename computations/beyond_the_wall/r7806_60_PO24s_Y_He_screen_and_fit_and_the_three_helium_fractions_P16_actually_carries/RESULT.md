# r7806 (60) — PO-24's Y_He route is closed, and it closes the other way round from N_eff's

**Order `r7805` (69).** Screen the helium fraction against the post-tilt residual; run the fit
regardless; judge the excursion against the helium fraction `P16` carries, at `P16`'s own precision,
reported absolutely too.

**Eight arms registered and pushed before measurement. SEVEN met as registered. Ⓗ⑧'s positive
branch is FALSE and its negative branch fired.** Eleven checks, all passing.

---

## The answer

**`N_eff` was affordable and bought nothing. `Y_He` buys something and is unaffordable.**

| window | `Δn` tilt | `+ Y_He` | **survives** | `Y_He` wanted | vs ① | vs ② |
|---|---|---|---|---|---|---|
| `100`–`1758` | `−0.07003` | `−0.05813` | **≤ `83.014 %`** | ≥ `0.28540` ⛔ edge | ≥ `+25.83σ` | ≥ `+11.79σ` |
| `700`–`1760` | `−0.17621` | `−0.16850` | **`95.624 %`** | `0.25942` | `+8.31σ` | `+4.15σ` |
| `1000`–`1760` | `−0.25946` | `−0.25491` | **`98.246 %`** | `0.25729` | `+6.87σ` | `+3.53σ` |

① = `P16`'s network, radiatively corrected: `0.2471 ± 0.00148` (its own `0.6 %`).
② = the observational determination `P16` quotes: `0.2453 ± 0.0034` (Aver et al. 2021).

**The helium fraction is the first candidate that genuinely overlaps the signature** — it removes
`53.5 %` of it on the published window, against `ω_b`'s `3.3` and `N_eff`'s `0.1` — **and the first
that takes a real bite**: the displacement no longer stands at `99`–`102 %` but at `95.6` and
`98.2 %` where the fit is interior, and at most `83.0 %` on the published window. The absorbed share
gains `+4.90`, `+0.40`, `+0.39` points, against `N_eff`'s `≤ +0.25`.

⇒ **So the shape argument that closed the other two routes does NOT close this one.** What closes it
is the **room**: the excursion is outside **three** standard deviations of **both** numbers `P16`
carries, on every window, and beyond **six** of the computed one where the fit is interior.

⇒ **Both ways an absorber can fail are now instantiated, on different parameters, and they cannot be
collapsed into one verdict about `PO-24`.**

---

## The three helium fractions `P16` carries, and the range that is not a range

The order says "at `P16`'s own precision". `P16` carries three values and they are different objects:

| # | object | value | precision |
|---|---|---|---|
| ① | the network's own computed `Y_p`, radiatively corrected | `0.2471` | `0.6 %` = `0.00148` |
| ② | the observational determination `P16` quotes | `0.2453` | `± 0.0034` |
| ③ | the standalone Born-level weak freeze-out | `0.2506` | — |

**⚠ The sentence I nearly took a range from is not a range.** `P16` reads: `Y_p` "is quoted with the
standard ~`1.6 %` radiative/Coulomb correction the Born-level weak network omits, **which carries the
network's computed `0.2432` to `0.2471`**". That is a **one-way correction**, not an interval:
`0.2432 × 1.016 = 0.2470912`. Registering `0.2432`–`0.2471` as `P16`'s uncertainty would have
invented an uncertainty out of a before/after pair under a named correction.

⇒ **GUARD: before a pair of numbers in a sentence is read as an interval, establish whether the
sentence is describing a spread or a transformation.** A correction has a direction; an error bar
does not.

**The asymmetry was registered before the fit ran, and it is what decided the outcome.** `0.6 %` on
`0.2471` against `N_eff`'s `5.7 %` and `ω_b`'s `0.65 %`: `Y_He` is simultaneously the purest
envelope direction the instrument has and the most tightly pinned of the three, about nine times
tighter than `N_eff`. The two halves of the row pull opposite ways, which `N_eff` did not do — so
"affordable" and "overlapping" had to be reported separately, and that is exactly where the verdict
came from.

---

## Ⓗ⑧: the registered negative fired, and what it does and does not reach

The fit was registered to land strictly inside the bank on every window. **On the published window
it lands exactly on the upper edge, `0.2854`.** The positive branch is false and is printed as false.

The registration named the consequence, and it is carried out: that row's numbers are **bounds**,
and their **direction** is established rather than asserted — a wider bank could only let `Y_He`
absorb more and push the excursion further out, so `survival ≤ 83.014 %` and `excursion ≥ +25.83σ`
both only **strengthen** the negative.

**And the verdict does not rest on that row.** The two windows where the fit is strictly interior
already put the excursion beyond `+6.87σ` of `P16`'s computed value with `95.6` and `98.2 %` of the
displacement standing. **No extension of the bank can open this route.** The bank's upper edge is
named to `70` as a limit, with that note attached.

---

## r7804's screen survives its first real test — after my own comparison of it was wrong

**The probe's first Ⓕ⑥ printed the screen's TOTAL overlap beside the fit's INCREMENTAL gain**, and
they disagreed by `48.6`, `31.9` and `10.1` points. Read that way, the screen had failed on the
first direction unlike a tilt it was applied to.

They are not the same object. The fit's gain is what `Y_He` adds **on top of an already-free tilt**;
the screen's `rem` is what `Y_He` would remove with **no tilt in the model**, and most of that is the
same part the tilt already took. The screen's own prediction for the gain is
`corr(Y_He, residual)² × (share of the signature the residual is)` — the quantity `r7804` actually
minted.

| window | predicted | measured | ratio |
|---|---|---|---|
| `100`–`1758` | `2.57 %` | `4.90 %` | `1.91` |
| `700`–`1760` | `0.23 %` | `0.40 %` | `1.74` |
| `1000`–`1760` | `0.30 %` | `0.39 %` | `1.32` |

Within a factor of two on every window, across windows whose residual share runs `28 %` down to
`3 %` — against the factor of `7.4` the wrong pairing scattered over. **And the sign is forced**:
every measured gain exceeds the prediction and none falls short, because the fit re-optimises the
tilt while the projection holds it fixed, so the projection is a **lower bound approached from
below**. That is the check that the agreement is not a coincidence of size.

⇒ **GUARD: a screen is compared with a fit on the base the fit reports against. A disagreement
between a total and an increment is a disagreement between two quantities, not a finding.**

⌗ Both forms are kept in `addendum.py` rather than the wrong one deleted: both numbers were correct
and the sentence putting them side by side was not. That is the third time this seat's own reading
has been the defect before any finding was, and the shape is always the same — a comparison written
before both sides were on the same footing.

---

## What this does not reach

- Nothing above `ℓ = 1996`, the bank's reach.
- Every number is a degeneracy-fit number: **no significance against the sky** is computed here.
- `Y_He` enters only through the ionisation history and `n_H`, so through the opacity and the
  diffusion damping — which is the channel `r7801` names and the only one the instrument has for it.
- The optical depth, the lensing amplitude and the matter density remain **named and not tested**.
  The screen is the cheap first test for each when its bank lands, and its scope is now measured on
  three directions rather than two.
- **I am never a subject.**

---

## ⌗ A second defect of mine, caught by a standing guard rather than by a gate

Ⓙ⑩'s first form asserted that `P15` **still contains** the sentence *"Whether the helium fraction,
the optical depth, the lensing amplitude or the matter density does is not yet computed"* — **the
sentence this very revision replaces.** Two things were wrong with it at once:

1. **It gated on the status of a sentence the row was asking to change** — the exact shape a standing
   guard forbids.
2. **It passed when I ran it and was false when I committed it.** I ran the receipt, *then* made the
   paper edit, and did not re-run. The committed tree carried a red receipt.

⇒ **GUARD: a receipt that reads the paper is re-run AFTER the paper edit, never only before.** This
is the same failure as "verify the gate your fix moved, not only the gate you fixed", in a new
place: the thing my edit moved was the input to my own receipt.

**The repaired form enumerates the states instead of pinning one.** What the argument actually
reasons from is that the candidates this revision does *not* test are still named as open — and that
holds in **both** states the landing can leave `P15` in, the four-candidate sentence it replaces and
the three-candidate sentence it writes. The arm asserts that, plus that exactly one of the two
states obtains. A disjunction beats a pin.
