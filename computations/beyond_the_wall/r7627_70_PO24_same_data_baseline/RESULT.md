# r7627+70 — RESULT: PO-24 on same-data baselines (registration in the r7627+70.1 commit)

**Run:**
- `ACT_SACC=… [BASE=…] python3 wfit_base.py MODE LMIN LMAX 0 ARM` for the 10 fits: 2 baselines, 2 sky fits on 700–1760 and 4 re-based mocks. The r7625 sky fits on 1000–2508 are reused.
- `python3 decide.py` applies the strict rule, with output in `decide.txt`.
- The fitter is r7625's `wfit_act.py` with two additions: the P-ACT off-tail cut (`pcut`), and a mock built from a chosen baseline (`BASE`).

| arm | window | baseline n_s (ℓ ≤ 800) | tail n_s (sky) | σ | M = sky − base | Δ = signature mock − base | Δ/σ | sky from no shift | **sky from the signature** | verdict (strict 2σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| Planck+ACT summed | 1000–2508 | 0.96240 | 0.97014 | 0.0087 | +0.0077 | +0.0282 | 3.26 | 0.89σ | **2.36σ** | against the signature |
| Planck+ACT summed | 700–1760 | 0.96240 | 0.96602 | 0.0065 | +0.0036 | +0.0194 | 3.01 | 0.56σ | **2.45σ** | against the signature |
| **ACT alone (P-ACT)** | **1000–2508** | 0.95917 | 0.97355 | 0.0094 | +0.0144 | +0.0277 | 2.93 | 1.52σ | **1.41σ** | **undecided: σ must shrink 1.31×** |
| **ACT alone (P-ACT)** | **700–1760** | 0.95917 | 0.96494 | 0.0084 | +0.0058 | +0.0203 | 2.41 | 0.69σ | **1.72σ** | **undecided: σ must shrink 1.16×** |

The baselines are 0.96240 ± 0.0062 (Planck ℓ ≤ 800 plus ACT 600–800) and 0.95917 ± 0.0064 (the P-ACT cut). Planck alone gives 0.96095.

## Scorecard
| arm | predicted | measured | verdict |
|---|---|---|---|
| J-1 sum baseline shift | −0.001 to +0.003 | +0.0015 | HOLDS |
| J-2 pcut baseline shift | −0.002 to +0.004 | −0.0018 | HOLDS |
| J-3 the baseline moves up by the ACT−Planck offset and the lean disappears | does not happen (p 0.85) | it does not; the lean holds | HOLDS |
| J-4 ACT alone on 1000–2508, sky from the signature | 1.2–1.8σ | 1.41σ | HOLDS |
| J-5 summed on 1000–2508 | 1.8–2.4σ | 2.36σ | HOLDS |
| J-6 deciding outcome reached in the ACT-alone arm | not reached (p 0.8) | not reached | HOLDS |
| J-7 700–1760 separation, sum / ACT alone | 1.8–2.8 / 1.3–2.3 | 3.01 / 2.41 | **FAILS high**: 700–1760 separates better than predicted |
| J-8 precision missing, ACT alone | 1.15–1.5 | 1.31 (1000–2508); 1.16 (700–1760) | HOLDS |

## The decision, and the precision still missing
1. **The same-data baseline does not move the test.**
   - ACT has 4 bins per spectrum below ℓ 800, so the baselines shift by +0.0015 and −0.0018.
   - ACT's higher n_s lives in its high-ℓ spectra, i.e. in the tail itself, so an ℓ ≤ 800 baseline cannot remove it.
   - **The ACT−Planck offset and the signature's shift are the same direction in the same multipoles.** A baseline from below ℓ 800 cannot separate them. That is a property of the data, not of the fit.
2. **In the arm that does not double-count the sky, the order's deciding arm, PO-24 is not decided.**
   - ACT alone sits 1.4σ (1000–2508) and 1.7σ (700–1760) from the signature, and 1.5σ and 0.7σ from no shift.
   - **The precision still missing is 1.16× on 700–1760**: σ(n_s) from 0.0084 to 0.0072. On 1000–2508 it is 1.31×.
   - That is within reach of the next ACT or SPT-3G data release, or of a proper joint Planck+ACT likelihood with the overlap handled.
3. **In the summed arm the test crosses 2σ against the signature in both windows** (2.36σ and 2.45σ), with no shift inside 1σ. That arm counts the shared sky twice. r7625 part 1's TT overlap correction is about 5 % on σ, which would leave it near 2.25σ and 2.33σ. That correction is a TT proxy, not a likelihood, so this is reported as **a lean past the line in the bounding arm and not a decision.**
4. **The 700–1760 window is the more decisive one with ACT** (J-7 failed high). Its separation is 3.0σ summed and 2.4σ for ACT alone, and it is the window where the missing precision is smallest.

## For 69 (census, r7577 rule)
- **PO-24's live half: undecided on the deciding arm, with the precision missing named.**
  - That arm is ACT alone on a same-data P-ACT baseline. The sky is 1.4–1.7σ from the signature.
  - The missing precision is 1.16× on 700–1760 and 1.31× on 1000–2508.
- **Planck+ACT summed, which double-counts the shared sky, passes 2σ against the signature** (2.4σ in both windows).
- **The same-data baseline was run and does not remove the ACT−Planck offset,** because that offset is in the tail's multipoles.
