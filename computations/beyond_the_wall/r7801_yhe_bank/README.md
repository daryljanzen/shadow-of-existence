# `r7801+70` — PO-24's Y_He response bank

*`r7801`'s second item: after N_eff, Y_He, which also acts on the damping tail through the diffusion.*

| file | what it does |
|---|---|
| `../ACOUSTIC_two_arm.py`, `YHE` | **the knob, added for this bank.** It replaces the coded `_YP = 0.2454` in the ionisation history and n_H, the only place helium enters the instrument, so it acts through the opacity and the diffusion damping. **Unset, the output is byte-identical.** It is recorded in each save's `config` as `YHE`. |
| `launch.sh` | Five Y_He (0.2054, 0.2254, 0.2454, 0.2654, 0.2854) on the control at `r6897`'s refit background, `LSTEP=8 LMAXL=2000`, each summed over eleven `KSLICE` pieces. The same design as `../r7801_neff_bank/launch.sh`. |
| `bank.py` | Folds the slices into `spectra/r7801_yhe_response_lcdm.npz` in the same layout (`ls__`, `Dl__`, … per Y_He, plus `yhe`). It checks the centre against `r6897`'s centre. |

**Checked before launch** (control, `LSTEP=64 LMAXL=2000`):
- `YHE=0.2454` against unset: max |relative difference| **0.0**.
- `YHE=0.2854`, as a ratio to the centre: 0.999 at ℓ≈200, 0.995 at 600, 0.984 at 1000, 0.966 at 1400, 0.963 at 1800, 0.949 at 1990. That is a damping-tail suppression, with the low multipoles untouched.

**The receipts** `P15_the_free_streaming_knob_...` (switch count 86, `YHE` named) and `P15_the_fitted_comb_moves_...` (the AST strip now covers `YHE` too) both pass.
