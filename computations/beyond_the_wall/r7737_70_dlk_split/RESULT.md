# r7737+70 — RESULT: both tiers built, every closure passes; E3 holds, E4 fails decisively, and the pairing says why

**Headline:**
- **Tier 1 (the distance map) and Tier 2 (the visibility) are built** on the r7729 grid (CR's ladder, 1450 nodes, k ∈ [0.00095, 0.2829], every ℓ 242–939), using the pairing declared in PREDICTION ①: by grid index, the same position relative to each arm's own last scattering.
- **Every registered closure passes** (⒜). The two bit-identity closures (C5, T2-C2) are 6 of 6 each.
- **E3 holds (70%).** The map-swap cross term differs from r7729's scalar swap by up to **6.0%** (CR source) and **7.9%** (ΛCDM source) in D_ℓ, and by more than 1% at 76% and 83% of ℓ.
- **E4 fails (60%), and not narrowly.** Exchanging χ alone moves A_ℓ by 0.030 on average. Exchanging g alone moves it by 0.0003, a hundred times less, at every ℓ on both arms.
  - **The reason is my own pairing, not the law.** Index pairing normalises each arm's η by its own W. So g, carried with its own dη, contributes only its *shape* in units of W. The 1.1555 extent goes over to the map. ⒟ gives the details.
- **E2 fails on price.** Tier 1 took 3.66 core-h against ≤ 3.5. Tier 2 took 4.28 core-h against ≤ 3, at 1.07 h of wall against ≤ 1 h. Both are still nightly-class: the runner job's limit is 240 min.
- **Stored:** `refs/ci/r7737_xmap` (`ea0580419`) and `refs/ci/r7737_vis` (`e2eb9d56e`), from `dlk-split.yml` run 42960476427. **Both blobs are sha256-identical to this container's builds**, and every closure passes on the runner at its registered bar.

## ⒜ The closures (registered in PREDICTION ② and ③; each a refusal)

| check | what it compares | bar | result |
|---|---|---|---|
| C1 lcdm / cr | the solve's D_ℓ vs banked `r6911_source_*_leafrec1` | 1e-10 | 4.4e-16 / 4.4e-16 |
| C2 lcdm / cr | offline native projection vs the run | 1e-12 | 5.6e-16 / 3.3e-16 |
| C3 | (S_lcdm, X_lcdm) on the ladder vs native ΛCDM, every ℓ | 1e-3 | 2.0e-6 (ℓ = 936) |
| C4 | ℓ(ℓ+1) Σ P Δ² = each array's own D_ℓ | 1e-12 | 0.0 |
| **C5** | hybrid with x0_B := x0_A vs the diagonal, both arms, 3 ℓ | bit for bit | **6 of 6 identical** |
| T2-C1 lcdm | A_ℓ on the ladder vs on ΛCDM's native k grid, every ℓ | 1e-3 | 1.5e-8 (ℓ = 792) |
| T2-C1 cr | the ladder *is* CR's grid: G identical, A_ℓ | 1e-12 | G identical; 6.7e-16 |
| **T2-C2** | hybrid with χ_B := χ_A vs the diagonal G | bit for bit | **6 of 6 identical** |
| T2-C3 | ∫ g dη over the grid (recorded) | — | lcdm 0.999767, cr 0.999772 |

- **Not registered, and also checked:** both diagonals, (S_cr, X_cr) and (S_lcdm, X_lcdm), are `np.array_equal` to r7729's (S_cr, K_cr) and (S_lcdm, K_lcdm), element for element.
- **Also not registered:** the `GRIDSAVE` grids' `eta` and `x0` are asserted equal to the `SRCFIELD` fields' before any Tier 1 projection. Both grids are asserted to follow the declared window rule, so the index pairing is checked rather than assumed.

## ⒝ What the pairing exchanges (PREDICTION ①, recorded by the build)

- **x0 at the visibility peak:** lcdm 13954.44, cr 14131.72. This is D_M on each arm, the quantity the scalar swap also exchanges, by XS = 1.01287 / 0.98729.
- **The window's χ span:** W_cr / W_lcdm = 43.957 / 38.042 = **1.1555**. The scalar swap does not exchange this; the map swap does.
- **r_s:** lcdm 145.382, cr 146.573. **l_A:** lcdm 301.54, cr 302.94.

## ⒞ E3: the map swap is not the scalar swap

**Cross-term D_ℓ, map swap (`r7737_xmap`) against scalar swap (`r7729_dlk_four`), same source, same ladder:**

| source on the other map | max \|map/scalar − 1\| | at ℓ | mean | ℓ over 1% |
|---|---|---|---|---|
| S_cr on X_lcdm | 6.0% | 385 | −2.8% | 76% |
| S_lcdm on X_cr | 7.9% | 393 | +3.8% | 83% |

**Sample values of map/scalar − 1:**

| ℓ | S_cr on X_lcdm | S_lcdm on X_cr |
|---|---|---|
| 242 | +0.6% | −0.1% |
| 300 | −2.0% | +2.7% |
| 400 | −5.8% | +7.9% |
| 500 | −2.9% | +3.7% |
| 600 | −5.0% | +5.8% |
| 700 | −2.3% | +4.4% |
| 800 | −0.2% | +0.5% |
| 939 | −3.3% | +3.3% |

- **Against the diagonal,** the map-swap cross term spans −12.3% to +3.6% (CR source) and −2.3% to +13.6% (ΛCDM source). The scalar swap's spans are −9.4% to +4.2% and −3.6% to +10.0%.
- **So at its extremes the map swap moves the spectrum further from the diagonal than the scalar swap does,** in both directions of the exchange.
- **E3 ✓.** As registered, I make no sign or size claim beyond the 1%: the reading is cc66's.

## ⒟ E4: under the declared pairing, the extent lives in χ, not in g

**|ΔA_ℓ| from the diagonal, averaged over ℓ 242–939:**

| from | r_s | A base | χ alone | g alone | both | ℓ where χ < g |
|---|---|---|---|---|---|---|
| (g_lcdm, χ_lcdm) | lcdm | 0.5406 | 0.0296 | 0.00028 | 0.0293 | 0 of 698 |
| (g_lcdm, χ_lcdm) | cr | 0.5387 | 0.0295 | 0.00028 | 0.0293 | 0 of 698 |
| (g_cr, χ_cr) | cr | 0.5680 | 0.0293 | 0.00037 | 0.0293 | 0 of 698 |
| (g_cr, χ_cr) | lcdm | 0.5699 | 0.0294 | 0.00037 | 0.0293 | 0 of 698 |

**The acceptance width (in k, mean over ℓ):**

| from | χ alone | g alone | both |
|---|---|---|---|
| lcdm | −12.83% | +0.44% | −12.41% |
| cr | +14.68% | −0.48% | +14.17% |

- **E4 ✗.** χ alone carries essentially all of A_ℓ's arm difference, and g alone carries about 1%.
- **Why, which the registration missed although ① stated it:**
  - Index pairing places η_B[i] at the same fraction of W_B that η_A[i] is of W_A.
  - g_A is integrated with its own dη_A, as registered in ③. So it is a normalised density whose shape *in units of its own W* is all it brings to a hybrid.
  - That shape is nearly the same on both arms. Swapping it moves the width by under 0.5%.
  - The extent, W_cr/W_lcdm = 1.1555, is carried by how many Mpc of χ each index step spans. That belongs to the map.
  - ① said so ("the swap exchanges … the visibility's extent as the kernel sees it"), and E4 then assigned the extent to g. **The registration contradicted its own pairing.**
- **The χ-alone width change, −12.83%, is r6919's independent dr_s/dχ reading (12.8%) to the digit shown.**
- **What this means for reading Tier 2:**
  - The g/χ split is not pairing-free.
  - Under index pairing, "g alone" means the visibility's shape at fixed relative extent, and "χ alone" means the extent plus D_M.
  - Under a pairing that held the χ span fixed, the attribution would move to g. That is the rejected same-η alternative, or any other.
  - I report this rather than re-pair after the numbers are in. A second pairing is cc66's call if the reading wants one.

## ⒠ E2, the price, and storage

| tier | wall on 4 workers | core-h | priced |
|---|---|---|---|
| Tier 1 (`xmap`, 5 combinations) | 3297 s (0.92 h) | 3.66 | ≤ 3.5 core-h, ≤ 1 h |
| Tier 2 (`vis`, 6 G arrays) | 3850 s (1.07 h) | 4.28 | ≤ 3 core-h, ≤ 1 h |

- **E2 ✗ on both,** by 5% and 43%.
- **Why the miss:**
  - The price took 7.5 min per combination from r7729's projection. Here a combination took 10.5 to 11 min.
  - The native-grid combinations (ΛCDM's 2547 modes, against the ladder's 1450) cost more than a ladder one, and I priced every combination at the ladder rate.
  - Tier 2's G has no source multiply but the same Bessel cost, which dominates. "Without the source multiply" bought nothing measurable.
- **Both stay nightly-class:** each is about an hour on 4 cores, against the 240-min job limit.
- **The local blobs:**
  - `r7737_xmap.npz`: 32,506,376 B, sha256 `0314f844023623f12775a9137373e273cb80b743d8e992af6eb29ea19d55a3a7`.
  - `r7737_vis.npz`: 54,900,696 B, sha256 `c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4`.
- **The runner:** `dlk-split.yml` run 42960476427 (LAUNCH at `eadeeab75`), both jobs green, about 50 min end to end.
  - `refs/ci/r7737_xmap` → `ea0580419`; `refs/ci/r7737_vis` → `e2eb9d56e`.
  - **Both npz blobs are sha256-identical to the container's** (`0314f844…`, `c3da5390…`), so every array is identical element for element (16 of 16, 31 of 31).
  - The runner's `closure.json` gives the same figures as ⒜ to the last digit.
  - Fetch with `git fetch origin refs/ci/r7737_xmap && git show FETCH_HEAD:r7737_xmap.npz > r7737_xmap.npz`, and the same with `vis`.

## Files

- `PREDICTION.md`: the registration, pushed first (`be8642494`).
- `split.py`: both tiers. Every closure is a refusal, and the pairing is asserted on the grids.
- `gridsave.sh`: `GRIDSAVE` on both arms in the r6911 configuration.
- `LAUNCH`: fires `.github/workflows/dlk-split.yml`.

## ⒢ The grid ref (`r7739`; PREDICTION ⑥)

- **Stored:** `refs/ci/r7737_grid` (`e67105cf3`), from `dlk-grid.yml` run 43037460258. 33,470 B, **sha256 `546977c4f05f2cff…`, identical to this container's build**, which was itself identical on two local builds.
- **Contents, per arm (`lcdm`, `cr`):**
  - `eta_{arm}`, `x0_{arm}` and `vis_{arm}`, 560 each;
  - the scalars `eta_ls_`, `eta_ls_w_` (= W), `eta_0_`, `D_M_`, `r_s_` and `l_A_{arm}`.
- **Closures, every one passing on the runner:**
  - **G1:** η + x0 = η_0 bit for bit at all 560 points, both arms.
  - **G2:** the window rule, both arms.
  - **G3:** x0 at the peak index equals `r7737_xmap`'s `x0_at_peak` bit for bit: 13954.436898516486 and 14131.719665018554.
- **Expectation (95%) ✓.**
- Fetch with `git fetch origin refs/ci/r7737_grid && git show FETCH_HEAD:r7737_grid.npz > r7737_grid.npz`.
