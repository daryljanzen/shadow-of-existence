# r7737+70 — PREDICTION: Tier 1 (the distance map) and Tier 2 (the visibility), priced and registered before any build

Order: `FOR_70.md` `r7737`, which carries cc66's `r7735+cc66` request in `FOR_66.md`. Both tiers are `PO-87`'s last step. This file is pushed before any build.

## ⓪ Two facts measured before registering

1. **Tier 2 needs no instrument edit.**
   - `ACOUSTIC_two_arm.py` already has `GRIDSAVE` (r7049+cc66.71). It writes the visibility `vis` = g(η) on the line-of-sight grid, plus `x0`, `k`, `dk`, `P`, `r_s`, `l_A`, `eta_ls`, `eta_ls_w` and `eta_0`. It returns before any solve.
   - Run here for both arms in the r6911 configuration, its `eta` and `x0` are **bit-identical** to the `SRCFIELD` fields'.
   - So the "one more output line" the order anticipates exists already. There is no new switch, no byte-identity gate and no re-bank.
2. **The distance map is affine with unit slope on both arms,** `x0 = eta_0 − eta` exactly (the instrument's l.1374, measured: `eta + x0` is constant to the last bit on each arm).
   - So the map's "shape" in η is the same on both arms. A map swap is defined entirely by **how η_A is paired with η_B**, and that pairing is what I declare.

## ① The declared pairing: by grid index, which is the same position relative to each arm's own last scattering

- **Both grids follow one rule** (the instrument's l.2099–2102): 420 points uniform on `[eta_ls − 6W, eta_ls + 6W)`, then 140 to `ETA_END`.
- **Measured:** neither arm's window is clipped by `ETA_ON` (`e_lo == eta_ls − 6W` on both).

| arm | η_LS | W | e_lo | η_0 |
|---|---|---|---|---|
| lcdm | 281.748 | 38.042 | 53.494 | 14236.19 |
| cr | 492.792 | 43.957 | 229.048 | 14624.51 |

- **What index i means:**
  - in the window, η_B[i] = η_LS,B + (W_B/W_A)(η_A[i] − η_LS,A);
  - in the tail, the same fraction of each arm's tail.
- **No interpolation is involved:** `x0_B[i]` is read at the same index.
- **What the swap therefore exchanges:**
  - the distance at last scattering: x0_B at the peak index is D_M,B;
  - **the visibility's extent as the kernel sees it:** the window spans W_B/W_A = **1.1555** times as much χ. That is cc66's 15.5%.
- **The rejected alternative is the same conformal time,** x0_B(η_A) = η_0,B − η_A. The arms' clocks differ (η_LS 282 against 493), so at η_LS,A it reads 14342.8, which is 211 Mpc past D_M,cr. It pairs no physical moment, so it is not built.

## ② Tier 1 — the four combinations with the other arm's map

- **The computation:** transfer(S_A, η_A, x0_B[i], k) on CR's ladder (the r7729 grid, k ∈ [0.00095, 0.2829], 1450 nodes, ℓ 242–939). xs = 1. The ΛCDM source is splined onto the ladder as in r7729.
- **Closures (each a refusal):**
  - **C1–C4 as r7729**, C1 at its registered 1e-10 (r7733: no cross-machine bar).
  - **C5, new:** the hybrid with x0_B := x0_A returns the diagonal Δ_ℓ(k) **bit for bit** (`np.array_equal`), on both arms, at three ℓ (first, middle, last).
- **Price, measured from r7729's projection:** about 7.5 min of wall per combination on 4 workers. Two cross combinations, plus the two diagonals for C5 and `native_lcdm` for C3, is **≤ 3.5 core-h, ≤ 1 h wall**. Nightly-class.
- **Output:** `refs/ci/r7737_xmap`, holding `Dlk__S_*__X_*` (698 × 1450 per combination), `Dl__*`, `ls`, `k`, the pairing record and `closure.json`. About 32 MB.

## ③ Tier 2 — the visibility exchange

- **The computation:** G_ℓ(k) = ∫ g_A(η_A) j_ℓ(k·x0_B[i]) dη_A for the four (g, χ) combinations, on the same ladder and the same ℓ, with the same pairing.
- **Then:** W_ℓ = G²dk/k, and A_ℓ = |Σ W e^{2ik r_s}| / Σ W with each arm's r_s (the comb period), giving **8 A_ℓ curves** (2 g × 2 χ × 2 r_s) and the acceptance width. These are the corpus's own definitions, `r7041_directions/acceptance_convergence.py::acceptance`.
- **Closures (each a refusal):**
  - **T2-C1:** (g_A, χ_A) on the ladder against the same arm's G and A_ℓ on its own native k grid: A_ℓ ≤ 1e-3 at every ℓ, on the ΛCDM arm (the analogue of C3). On the CR arm it is identity, because the ladder is its grid; ≤ 1e-12.
  - **T2-C2:** the hybrid with χ_B := χ_A returns the diagonal G bit for bit.
  - **T2-C3:** ∫ g dη over the grid is recorded per arm: 0.99977 on both, measured.
- **Price:** each G has the transfer's cost without the source multiply. Six G arrays at about 7 min each is **≤ 3 core-h, ≤ 1 h wall**. Nightly-class. No solves are needed, so the runner job skips `launch.sh`.
- **Output:** `refs/ci/r7737_vis`, holding `G__g_*__X_*`, `A__g_*__X_*__rs_*`, the widths, `ls`, `k`, the pairing record and `closure.json`.

## ④ Expectations (registered)

- **E1:** C1–C5 and T2-C1 to C3 pass. C5 and T2-C2 are bit-identity, so they pass or the code is wrong.
- **E2:** both tiers are inside the prices above.
- **E3 (Tier 1, the one with content):**
  - The map swap differs from r7729's scalar swap. The scalar swap rescales x0 by 1.0129 everywhere; the map swap holds D_M,B at the peak and stretches the window's χ by 1.1555.
  - **I expect the map-swap cross term to differ from the scalar-swap cross term by more than 1% in D_ℓ somewhere in the window.** 70%.
  - I make no sign or size claim beyond that: the reading is cc66's.
- **E4 (Tier 2):** exchanging χ alone moves A_ℓ by less than exchanging g alone. The law's extent lives in g, and χ carries the extent only through the window's χ span. 60%.

## ⑤ Storage and runs

- **The workflow:** `dlk-split.yml`, on `dlk.yml`'s pattern:
  - push on this branch's `computations/beyond_the_wall/r7737_70_dlk_split/LAUNCH`, plus `workflow_dispatch`;
  - a job-level `if:` on this ref;
  - `cancel-in-progress: false`;
  - `contents: write` at job level.
- **The jobs:** two, in parallel.
  - `xmap`: `launch.sh` (the r7729 SRCFIELD solves), then Tier 1.
  - `vis`: `GRIDSAVE` on both arms, then Tier 2.
- **Tier 1 first:** if only one is had, Tier 1, per cc66.
