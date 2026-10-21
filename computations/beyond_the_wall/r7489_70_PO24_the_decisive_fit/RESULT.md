# r7489+70 — RESULT: PO-24 ①, the decisive fit (registration `a017b6479`)

**Run:** `python3 wfit.py MODE LMIN LMAX PROFILE`, with output in `w_*.json`.
- Planck 2018 `plik_lite` TT/TE/EE, keeping only the bins inside each window, plus Planck 2018 lensing and the τ prior.
- Flat ΛCDM with **all six parameters free, ω_b included**, plus A_planck.
- **⛔ One defect of mine, found and fixed before any verdict.** The first null mock applied the signature, because the switch tested `S is None` and the null mode passed `False`.
  - That run is kept as `bug_*`, and its number is the signature mock's, not a null.
  - The null was then re-run.

| arm | registered | measured | verdict |
|---|---|---|---|
| **D-0** null mock | M = 0 to < 0.1σ | **M = −0.00000** (χ² 0.00) | **HOLDS**: the pipeline is unbiased |
| **D-1** Δ_full/Δ on 1000–2508 | 0.6 (0.2–1.1) | **0.86** (+0.0253 against +0.0293) | **HOLDS** |
| **D-2** σ_W on 1000–2508 | 0.012 (0.007–0.022) | **0.0158** (profile; Fisher 0.0155) | **HOLDS** |
| **D-3** M(1000–2508) on the sky | 0.000 (±0.020) | **+0.0030** | **HOLDS** |
| **D-4** verdict | UNDECIDED 45 % | **UNDECIDED** | **HOLDS** |
| **D-5** σ_W on 1400–2508 | 0.020 (0.010–0.040) | **0.0264** | **HOLDS** |
| EFFORT | 2 h (1–4) | ≈ 1.5 h | holds |

## Per window (M = n_s(W) − 0.9611; σ = the window's own)

| window | n_s(W) | σ | M | Δ_full (mock) | Δ (receipt) | \|M\|/σ | \|M−Δ_full\|/σ | \|Δ_full\|/σ | class |
|---|---|---|---|---|---|---|---|---|---|
| 700–1760 | 0.9650 | 0.0095 | +0.0040 | +0.0184 | +0.0181 | 0.42 | 1.52 | **1.94** | UNDECIDED |
| 1000–1760 | 0.9650 | 0.0182 | +0.0041 | +0.0225 | +0.0267 | 0.22 | 1.01 | 1.24 | UNDECIDED |
| **1000–2508** (decisive) | **0.9639** | **0.0158** | **+0.0030** | **+0.0253** | +0.0293 | **0.19** | **1.42** | **1.61** | **UNDECIDED** |
| 1400–2508 | 0.9577 | 0.0264 | −0.0032 | +0.0218 | +0.0444 | 0.12 | 0.95 | 0.83 | UNDECIDED |

All four fits have a positive-definite Hessian, and their χ² per bin runs 1.01–1.13.

## What it says
1. **The decisive window is UNDECIDED by the registered rule.** The like-for-like predicted shift (+0.025) is 1.6σ of the tail-only precision (0.016), short of the 2σ the rule needs to separate the two predictions. The sky's tail n_s is 0.9639 ± 0.0158.
2. **No window decides.** The nearest is 700–1760, where the separation is 1.94σ, just under the line.
3. **Every window leans the same way:** the sky sits 0.1–0.4σ from no shift and 1.0–1.5σ from the construction's. The windows overlap, so they are not combined, as registered. But the lean is uniform and nowhere toward the signature.
4. **Freeing ω_b and the rest absorbs part of the shift, and less than I predicted.** Δ_full/Δ runs 1.01 (700–1760), 0.85, 0.86, and 0.49 (1400–2508, the narrowest).

## What it narrows
- **Off the tail,** n_s is known to ±0.0063 (r7471).
- **On the tail alone** it is known only to ±0.009–0.026, and the construction's like-for-like shift is +0.018–0.025.
- **So the question is no longer whether there is an independent measure. It is whether the tail can be measured about 1.3× better than Planck does.**
  - At σ ≈ 0.012 on 1000–2508, or a 3 % improvement on 700–1760, the same rule would decide.
- **That precision is a data question, not a computation this programme can do with Planck alone.** It is the row's honest state.

## Scope
- This is `plik_lite` (compressed, foregrounds marginalised).
- The mock is noise-free and starts from the off-tail best fit.
- The signature is applied to TT, TE and EE alike.
- Lensing and τ are not windowed and enter every fit.
