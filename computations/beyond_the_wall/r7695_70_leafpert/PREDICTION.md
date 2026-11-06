# r7695+70 — PREDICTION, step 1 (registered before the edit and the runs)

**The build:** HIER under (L), the arm of record's own construction.
- **Switch:** a new value `SPLITCLOCK=L`. `SPLITCLOCK=1` stays as it is (the stacking-rate perturbations, the pairing ACOUSTIC retired as `STACKPERT=1`), so the banked r7675–r7689 rows stay reproducible. ACOUSTIC keeps `STACKPERT` for the same reason.
- **What `SPLITCLOCK=L` does:** everything `SPLITCLOCK=1` does (grid, `eta_onset`, `rs_f` and `DM` on the stacking rate; `xe_history` on the leaf rate). In addition, the perturbation dynamics run on the leaf rate and are chain-ruled onto the stacking grid, as in `ACOUSTIC_two_arm.py` under `LEAFPERT` (:934, :974, :1512, :1555):
  - `_rhs`, both its full branch and its decoupled (`ETADEC`) branch, reads the leaf conformal Hubble rate `Hl = a H_leaf / c` in place of `Hc_of`, and its output is multiplied by `Jac = H_stack / H_leaf`;
  - the onset data read the leaf ℋ: `Hcs` in the neutrino-shear seed, and the radiation-era θ₀ = k²η/2 Ψ with η → 1/ℋ_leaf(onset), the leaf conformal time in radiation domination;
  - the stored tight-coupling slip reads the leaf ℋ, because it rebuilds a dynamical variable.
- **What stays on the stacking rate, mirroring ACOUSTIC exactly:**
  - the source assembly's Ψ = Φ − 6ℋ²(…)/k², which ACOUSTIC's `_project` (:1761–1767) also reads on `Hc_of`;
  - the visibility measure, τ = ∫τ′ dη_grid (ACOUSTIC's `VISLEAF=0` default);
  - the multipole closures `(l+1)/η` on the grid time, as in ACOUSTIC's.
- **Content fractions:** on the leaf total, unchanged, as in both instruments.

**Gate (G1/G2), before any run:**
- G1: with `SPLITCLOCK` unset, `=1`, and `=1` with `SPLITIC=cr`, the 19 hashed quantities are bitwise equal to the pre-edit file, at the default and at the adjudicated environment.
- G2: with `SPLITCLOCK=L`, the background, the ionisation history and `DM` equal `SPLITCLOCK=1`'s bitwise, and only `evolve()`'s output moves.

**Runs:** the sweep's two adjudicated builds (FROZEN, DECOUPLED) at both points, through the receipt's arm-B harness exactly as r7675/r7683:
- the refit point: 68.570730 / 0.291246, ω_b 0.021643, radiation 4.15e-5/h²;
- the distances point: 68.60 / 0.2973, ω_b 0.02237, radiation 4.1833e-5/h².

They are banked as `spectra/p15_lowell_depths_leafpert_leafrec1.npz` (addition), with rows per point and build and the pairing recorded per row.

**Expectations, at the distances point.** For reference: one clock gives 0.4304 / 0.4300; the split under `SPLITCLOCK=1` gives 0.4560 / 0.4589; arm A gives 0.4348.
- **P1 (structural).** Under (L) the dynamics are the one-clock ODE in leaf time; only the time label, the closures and the onset's η differ. The states at a given a should match the one-clock run closely. So what (L) adds over one clock is the projection share: D_M, χ(η) and the visibility measure on the stacking rate, plus the stacking Ψ.
- **P2 (the separation).** The +0.026 / +0.029 at ℓ = 3 splits into a dynamics share and a projection share. I expect **the dynamics share to be the larger: (L) ℓ = 3 below 0.443 on FROZEN and below 0.444 on DECOUPLED**, that is, less than half the split's shift surviving. The reasoning: the retired pairing's Poisson source is short by 1.33 at recombination, which reshapes the potentials' early evolution at the scales the low-ℓ ratio and its ℓ 25–40 plateau normalisation read. I hold this with low confidence; the reachable negative is (L) ℓ = 3 ≥ 0.443, a projection-dominated shift.
- **P3.** (L) ℓ = 3 lies inside [0.425, 0.465] on both builds and both points.
- **P4.** Minimum at ℓ = 4 and recovery (first ℓ ≥ 5 at depth ≥ 0.99) at ℓ = 8 on every row.
- **P5.** At the refit point the separation is the same within 0.005 in each share.
- **Price:** about 10 lines across 6 sites; gate about 10 min; runs about 30 min (FROZEN about 80 s and DECOUPLED about 12 min per point, four at a time).
