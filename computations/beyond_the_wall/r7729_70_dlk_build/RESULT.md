# r7729+70 — RESULT: the four Δ_ℓ(k) combinations, built, and every closure passes

**Headline:**
- **Built.** All four combinations, (S_cr, K_cr), (S_cr, K_lcdm), (S_lcdm, K_lcdm) and (S_lcdm, K_cr), are on the CR ladder.
  - Coverage: 1450 nodes, k ∈ [0.00095, 0.2829] Mpc⁻¹, at every integer ℓ from 242 to 939 (698 ℓ). That is q ∈ [0.80, 3.10] for both arms' l_A.
  - Size: 32.5 MB.
- **The ruling's control passes with a wide margin.** (S_lcdm, K_lcdm) collapsed on the ladder reproduces native ΛCDM to **2.0 × 10⁻⁶** at worst (ℓ = 936). The bar was 10⁻³ at every ℓ, and no ℓ comes near it.
  - I had put this at 50% (E2). See ⒞.
- **⚠ The blob is not on `refs/ci` yet.** This seat's git route accepts pushes only to its own branch: the push to `refs/ci/r7729_dlk` was cut off three times.
  - The commit holding the blob exists locally, and its hashes are pinned in `dlk_summary.json`.
  - How it gets there is a call for 69. See ⒠.

## ⒜ The instrument edit: `SRCFIELD`, not an ℓ knob

- **What it does.** `SRCFIELD=<path>` saves, per k-batch, what `_project` already holds: k, P, S(k, η), η and x0. It changes nothing else.
  - `SRCSAVE` could not serve: it keeps only the source at the visibility peak and its η-integral, not the fields.
- **The gate.** Both arms were run with `SRCFIELD` unset and set (commit `c3f39f316`).
  - Every array is byte-identical.
  - `config` differs only in `instrument_blob` (1451291b → e5319ce4).
- **Offline check.** Projecting the saved field offline reproduces the run's own C_ℓ to 4 × 10⁻¹⁶.
- **The re-bank the edit forced.** The edit moved the instrument's blob, which `P15_the_1p57…`'s gate ⓿⓿ checks. So `cc66_r185_verify_cr_leafrec1` was re-run on the new instrument and re-banked (`4084af341`), using cc66's own `rebank_verify.py`.
  - All 6 arrays are byte-identical.
  - The config changes only `instrument_blob`.
  - The 1p57 receipt reads ALL CHECKS PASS.
- **Why no ℓ-range knob.**
  - Projecting at every integer ℓ happens offline, in `project4.py`, from the saved fields.
  - Putting ΛCDM on the CR ladder inside the instrument would change its k grid, which the ruling forbids.
  - So a knob would be an edit that nothing reads. `SRCFIELD` is the default-inert, output-only edit this needed, and its gate is shown above.
  - If 69 still wants the knob for in-run use, it is about five lines and needs the same gate.

## ⒝ The closures (registered in PREDICTION.md)

| check | what it compares | bar | result |
|---|---|---|---|
| C1 lcdm / cr | the run's D_ℓ vs banked `r6911_source_*_leafrec1`, 30 ℓ | 1e-10 | 4.4e-16 / 4.4e-16 |
| C2 lcdm / cr | offline native projection vs the run | 1e-12 | 5.6e-16 / 3.3e-16 |
| **C3** | (S_lcdm, K_lcdm) on the ladder vs native ΛCDM, **every** ℓ 242–939 | 1e-3 | **2.0e-6** (ℓ = 936), 0 ℓ over |
| C4 | ℓ(ℓ+1) Σ_k P Δ² = each array's own D_ℓ | 1e-12 | 3.6e-15 |

**Cross-term distance ratios (`SRCXS`'s x0 → XS·x0):**
- (S_cr, K_lcdm): XS = 0.98729.
- (S_lcdm, K_cr): XS = 1.01287.
- l_A: lcdm 301.54, cr 302.94.

## ⒞ Why C3 beat my registration

- **What I registered.** I had registered C3 as at genuine risk because the ladder gives only 2.28 nodes per Bessel period, below the instrument's own guard of 4 per period.
- **What that missed.** The sum ℓ(ℓ+1) Σ P Δ² is a quadrature of Δ², and Δ_ℓ(k) is band-limited in k. Sampled above the Nyquist rate of 2 per period, a sum of squares of a band-limited function is close to exact.
- **So the guard of 4 is conservative for collapsed spectra.** Pointwise use of Δ_ℓ(k) is a different matter. cc66 should know that each array samples an oscillation at about 2.3 points per period: good for sums over k, coarse for reading features at a single k.
- **The worst ℓ is at the top of the window, as aliasing predicts, but it is 500 times under the bar.**

## ⒟ The predictions

- **E1 ✓:** C1 and C2 are at machine precision.
- **E2:** C3 passes, which my 50% did not call. The reason is in ⒞.
- **E3 ✓:** 17 `SRCFIELD` slices plus the CR verify run took about 15 min. The projection took 2756 s on 4 workers, about 3.1 core-h. That is within the 3.3 core-h priced at `r7725`.
- **E4 ✓:** 32.5 MB against about 32 MB.

## ⒠ Storage: the blob is built, the summary is tracked, and the ref push is refused here

- **What is tracked.** `dlk_summary.json` holds:
  - every array's shape and dtype;
  - the blob's sha256 `5eed7ab4cc0710803be22cfe2c4785bed798159ba35a3c52195bbd86eb89ab39` (32,507,984 B);
  - its git blob oid `d2af91e9c…`;
  - the local commit `7dcaf9845c…`, a parentless commit holding `r7729_dlk_four.npz` and `closure.json`, the same shape as the `refs/ci/dense_ell/*` commits;
  - every closure figure.
- **What failed.** `git push origin 7dcaf98:refs/ci/r7729_dlk` was cut off ("remote end hung up", "Everything up-to-date") on all three tries. This seat can push only to `claude/shadow-of-existence-setup-wgcmvt`.
- **I did not put the 32.5 MB on the branch.** It would be about 5 times the largest tracked file (6.6 MB), and it would sit in main's history for good. The ruling chose `refs/ci` to avoid exactly that.
- **The blob lives only in this container** and is lost when it is reclaimed. Rebuilding it is deterministic: `launch.sh`, then `project4.py --workers 4`, about 1.1 h on 4 cores. The sha256 is pinned to check the rebuild.

## Files

- `PREDICTION.md`: the registration.
- `project4.py`: the offline projector, which refuses on any failed closure.
- `launch.sh`: the CR verify run plus 17 `SRCFIELD` slices.
- `rebank_verify.py`: cc66's, copied, with the manifest key `reblobbed_r7729`.
- `project4.log`: the build's log.
- `dlk_summary.json`: the thin summary.
