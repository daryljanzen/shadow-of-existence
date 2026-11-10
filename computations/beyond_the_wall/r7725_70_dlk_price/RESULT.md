# r7725+70 — RESULT: the price of retaining Δ_ℓ(k) on the real source

**Headline:**
- **The price is inside a nightly-class budget:** at most **3.3 core-hours** for every integer ℓ in the window, both arms (≈ 0.8 h wall on 4 cores), and at most 8.8 core-hours if every ℓ from 100 to 1999 is kept, with no instrument edit.
- **But the order's "one shared k grid" cannot be met without changing the instrument's numerics**, which the order forbids. The CR arm's k grid is the arm's discrete mode ladder, not a quadrature choice.
- **So it is priced and not built.** Three rulings are needed first, listed below.
- **And `Dlk_samp` is not what `r7723+cc66` reported:** two of the three objections are misreadings of the bank, and the third holds.

## ⒜ `Dlk_samp`, read directly (registered at `r7725+70.0`)

| `r7723+cc66` said | the bank says |
|---|---|
| sampled ℓ 20…205, q 0.066–0.677, entirely below the window | `samp` holds **indices** into `ls`. The sampled ℓ are **260, 468, 684, 892, 1100, 1308, 1524, 1732** (q 0.86–5.74), and **four lie inside q ∈ [0.80, 3.10]** |
| the arms share 4 of 8 sampled ℓ | **all 8** are the same ℓ in both arms |
| the row sums do not reproduce the banked spectra | under the transfer's own definition, **ℓ(ℓ+1) Σ_k P·Δ² = D_ℓ to ≤ 4.4×10⁻¹⁶** in all four blocks (2 arms × 2 injections); each save's `closes` is 0 |
| the k grids differ (2547 against 1452) | ✓ true, and see ⒞ |

⛔ **It still does not serve, for a reason the r7723 note did not give.** It comes from the r7039 runs, which replace the plasma source with an analytic injection (`SRCINJ`). Under `fixed`, Δ_ℓ(k) factorises exactly, so it is the factorised object again. **A real-source run is needed, as the order says.**

## ⒝ The price, measured

Configuration: the reported r6911 one (`HIER=1 LMAXL=2000 KFAC=2`, both arms at their leafrec1 points), run in k-slices of 250 modes with `DLKSAVE`. Every run's retained Δ closes on its own C_ℓ to **0.000e+00**. Logs are in `logs/`.

| run (two jobs concurrent) | ℓ projected | wall |
|---|---|---|
| ΛCDM slice 0:250 (lowest k), `LSTEP=8` | 238 | 31 s |
| CR slice 0:250, `LSTEP=8` | 238 | 41 s |
| ΛCDM slice 2250:2500 (highest full), `LSTEP=8` / `16` | 238 / 119 | **268 / 147 s** |
| CR slice 1250:1452 (last, 202 modes), `LSTEP=8` / `16` | 238 / 119 | **223 / 126 s** |

**The most expensive slice, split into fixed cost and per-ℓ cost:**
- ΛCDM: **26 s** of solve and overhead per slice, plus **1.02 s per ℓ**.
- CR: **29 s** plus **0.82 s per ℓ** at 202 modes, which is about 1.0 s per ℓ for a full 250.
- The per-ℓ cost rises with k: on the lowest slice it is about 20× cheaper. The window's ℓ (241–935) sit in the cheaper half of 100–1999. A microbenchmark of the Bessel step at ℓ = 241, 588 and 935 on the top slice gives 0.23, 0.56 and 0.91 s.

**Totals.** ΛCDM has 11 slices (10 full plus 47 modes) and CR has 6 (5 full plus 202). The upper bound charges every slice at the top slice's cost; the second column assumes a linear ramp in k.

| ℓ retained | upper bound | linear ramp |
|---|---|---|
| **every integer ℓ in q ∈ [0.80, 3.10]**, ≈ 695 per arm (needs an output-only ℓ-range knob) | **3.3 core-h**, ≈ 0.8 h wall on 4 cores | ≈ 1.8 core-h, ≈ 0.45 h |
| every ℓ 100–1999 (`LSTEP=1`, no instrument edit) | 8.8 core-h, ≈ 2.2 h wall | ≈ 4.6 core-h, ≈ 1.2 h |
| ⌗ two rows per ℓ-pair (`LSTEP=2`), against the 142-component structure | half of each row | |

**Against a nightly-class budget (about 3 h wall on 4 workers): inside, on every line.**
- P1 is refuted, and favourably: a slice is 0.5–4.5 min, not 5–20.
- P2 and P3 hold.

**Size:**
- window only, float64: **14.2 MB (ΛCDM) + 8.1 MB (CR)**;
- every ℓ 100–1999: 39 + 22 MB.
- That is about forty times anything `spectra/` tracks, so it cannot be a tracked bank, and `bank_thin.py` says why.

## ⒞ Why the "shared k grid" is a numerics change, measured in the source

`ACOUSTIC_two_arm.py` builds k from `lL / D_M`:
- **ΛCDM:** `lL = linspace(12, KMAXL, 3·NK)`, an even continuum.
- **CR, unless `KCONT=1`:** `lL = √(L(L+2))·stretch` over integer L, the arm's own discrete ladder of modes.
- So the 2547-against-1452 difference is the arms' different physics, not a resolution choice.

A shared grid can be had three ways, and each is a ruling, not a build step:

| route | what it does | why it needs a ruling |
|---|---|---|
| (S1) native grids, then interpolate onto one | no instrument change | Δ_ℓ(k) is sampled at 4.0 points per Bessel period (the run's own print). Interpolation error enters the plane a 142-component fit reads, and the order forbids changing numerics |
| (S2) CR on `KCONT=1` (continuum) | the same grid kind as the control | replaces the arm's ladder; r6794 measured that the ladder run's spectrum "depends weakly" on this, so it is a different computation of the arm |
| (S3) both arms native, no shared grid | cheapest, exact, closes | does not meet the order's "shared k grid" |

## ⒟ And what "the four combinations" would need

The real transfer Δ_ℓ(k) = ∫ S(k, η) j_ℓ(k x0(η)) dη fuses source and kernel. **A native run of each arm gives the two diagonal combinations only.**
- The off-diagonal ones (one arm's S(k, η) through the other's kernel and visibility) need the source fields carried across arms.
- `SRCXS` does this for the distance only, and `SRCSAVE` writes the fields.
- That roughly doubles the price: four runs, not two, still inside the budget.

## What I need, as three rulings

1. **The grid:** (S1), (S2) or (S3).
2. **The combinations:** the two diagonal ones, or all four (cross-arm via the saved source fields).
3. **Storage:** 22–61 MB of arrays. Untracked plus a thin tracked summary is the r7041 precedent; a `refs/ci/*` blob is the dense-ℓ precedent.

**With those, the build is about 0.5–2.5 h of wall** and goes the same night. Nothing in the instrument changes for (S1) or (S3). (S2) and the window-only ℓ knob each take a gate with byte-identity when unset.
