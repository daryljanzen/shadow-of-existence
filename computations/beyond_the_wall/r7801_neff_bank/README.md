# `r7801+70` — PO-24's N_eff response bank

*`r7801`'s order (69, routing 60's `r7800`): PO-24's damping signature is an envelope in ℓ, and ω_b, a peak-phase direction, cannot absorb it. N_eff is the one inherited parameter that acts on the damping envelope. So build its response bank first, in the mould of `r6897`'s five-point ω_b set, where 60's harness reads.*

| file | what it does |
|---|---|
| `../ACOUSTIC_two_arm.py`, `DNEFF` | **the knob, added for this bank.** It adds ΔN_eff to the neutrino density at fixed photon density, then re-forms Ω_r and FNU from the two. The expansion rate's radiation term, z_eq and the free-streaming fraction therefore move together, which is what a change of N_eff at fixed T_CMB means. `ORFAC` is not this: it scales Ω_r at fixed FNU. The coded N0 is FNU/(1−FNU)/0.2271 = 3.000. **Unset, nothing runs, and the output is byte-identical.** It is recorded in each bank's `config` as `DNEFF` (None when unset). |
| `launch.sh` | Five ΔN_eff (−0.5, −0.25, 0, +0.25, +0.5, so N_eff 2.5 to 3.5) on the control at `r6897`'s refit background (`LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248`). The resolution is `LSTEP=8 LMAXL=2000`, each value summed over eleven `KSLICE` pieces of 250 on `KBATCH` boundaries. It is idempotent and resumable. |
| `bank.py` | Folds the slices into `spectra/r7801_neff_response_lcdm.npz` in `r6897_wb_response_lcdm.npz`'s layout (`ls__`, `Dl__`, `nsl__`, `lA__`, `rs__`, `DM__` per N_eff, plus `neff` and `missing`). It checks the centre against `r6897`'s banked centre, which is the same run but for the knob. |

**Checked before the bank was launched** (control, `LSTEP=64 LMAXL=2000`):
- `DNEFF=0` against unset: max |relative difference| **0.0**.
- `DNEFF=+0.5`: Ω_r 9.1326e-05 → 9.7495e-05, z_eq 3391.5 → 3176.9, l_A 301.54 → 306.55, and the tail moves by several per cent.

**Two receipts are updated for the new knob:**
- `P15_the_free_streaming_knob_...` counts the instrument's switches. Its count is 85 now, with `DNEFF` named, by its own convention.
- `P15_the_fitted_comb_moves_...` pinned the working tree to the blob of its `LEAFGEOM=1` leg. It now also accepts a tree that differs from that blob only by the `DNEFF` block and its config key, checked by AST. Any other difference keeps it red.
