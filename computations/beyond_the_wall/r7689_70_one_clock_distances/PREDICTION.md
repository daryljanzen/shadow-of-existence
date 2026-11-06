# r7689+70 — PREDICTION (registered before the runs)

**The run:** the hierarchy with `SPLITCLOCK` unset at the distances point (H0 68.60, Ωm 0.2973, ω_b 0.02237, radiation 4.1833e-5/h², `OBF`/`ORF` unset), both adjudicated tower builds (FROZEN_adjudicated_KLO_0_1, DECOUPLED_adjudicated_KLO_0_1_NS3_60000), through the receipt's arm-B harness exactly as r7683, with only `SPLITCLOCK=1` removed.

**LEAFREC:** with `ARM` unset and `SPLITCLOCK` unset, HIER runs one rate, the content-carrying leaf rate, for everything, so the ionisation history is already on the leaf rate. HIER reads no `LEAFREC` switch, and the bank records this.

**The bank:** `spectra/p15_lowell_depths_distances_oneclock_leafrec1.npz` (addition). It has rows `armB_frozen` and `armB_decoupled`, plus `ells`, and a `config` and `manifest` that record the point (H0, Om, WBH2, radiation) and `SPLITCLOCK=False` in the bank itself.

- **P1.** The one-clock leg reproduces the one-clock namesake `cc66_lowell_sweep.npz` at ℓ = 2–8 to ≤ 0.001 per multipole (FROZEN ℓ = 3 0.4304, DECOUPLED 0.4300). If it does, that bank's adjudicated rows sit at this point, which is now a record and not only a sentence.
- **P2.** Against arm A (0.4348 at ℓ = 3), the one-clock octopole sits **about 1% below** the exact transfer (−0.5% to −1.5%), not 5.5% above. The +5.5% is then the split clock's: the split's ℓ = 3 shift (+0.026 / +0.029, r7683) carries all of it and about 1% more.
- **P3.** Minimum at ℓ = 4, recovery (first ℓ ≥ 5 at depth ≥ 0.99) at ℓ = 8 on both rows.
- **Reachable negative.** If the one-clock ℓ = 3 comes out at or above 0.450 (≥ +3.5% over arm A), the clock does not carry the excess, and the attribution stays open.
- **Price.** About 12 min: FROZEN about 75 s, DECOUPLED about 10 min, run in parallel.
