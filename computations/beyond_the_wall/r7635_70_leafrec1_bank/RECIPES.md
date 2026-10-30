# Where each §B recipe came from (r7635+70)

The clone is shallow and the spectra arrived in one bulk commit, so history cannot recover a command; these come
from the corpus's own records, cross-checked against `r7095_70_artefact_configuration/check_banked_config_log.txt`
and `corpus/banked_config_manifest.json`.

| family | recipe on record | source | rebuilt here as |
|---|---|---|---|
| cc66_r185_verify, r6885 dp0/los/losdp0/lossw0, r6889 nufs0 | `HIER=1` (los: no HIER) `LSTEP=8 LMAXL=2000` + one switch, at r6941's point | `refit_grid185/verify.sh`, `r6885_directions/launch{,2}.sh`, `r6889_directions/launch.sh` | `launch_clean.sh` |
| r6911 source (+kcont), r6915 pairs, r6941 fine, r6959 eta | sliced `KSLICE` 250, `SRCSAVE`/`SRCXS`, `SRCDEC`, `LSTEP=1`, `SRCETA` | `r6911_directions/{launch,pass2}.sh`, `r6915_`, `r6941_`, `r6959_directions/launch_a.sh` | `launch_clean.sh`; `SRCXS` = 0.987293 |
| c54.175 / c54.177 | `ARM=cr NK=600 LMAXL=2000 ETAEND=4000` (line of sight), shear 8/9 / 16/15, single matter fluid | spectra/README.md:15-17 | + `BSPLIT=0`, c54.175 `POLC=8/9` |
| c54.178, c54.186 KCONT | F178 = `HIER=1 BSPLIT=1 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300` (+`KCONT=1`) | README:18-26 | same |
| c54.186 L3000, c54.191, c54.193, c54.195, item38 | F186 = `HIER=1 BSPLIT=1 NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300` + `CRPHI`/`NODRIVE`/`LATARG=340` | README:27, `_item38_seamphase_scan.sh`, the c54.191/193/195 receipts | same; item38 φ=0 and φ=π are banked from the c54.186 and c54.191 φ=π runs (their namesakes agreed to 4e-9 and bit for bit) |
| r4494 leaf/stack × ISW on/off | `ARM=cr LMAXL=1300 LSTEP=4` line of sight, `STACKPERT=1`, `NOISW=1` | the files' own keys; C62 receipt | same |
| r6784 hier / noCRIC / los, r6794 | F178 + `CRH0=68.62 CROM=0.2973 ZSTART=3e7` (± `CRIC=branchpoint`; los drops HIER); r6794 `NK=900 KBATCH=150 KCONT=1`, six `KSLICE` of 450 summed | README:47-50 | same, on the arm of record |
| cc66_cr_x_h686/h6862_pol, h686_L2000 | `HIER=1 LSTEP=2 LMAXL=1300` (2000) at CRH0 68.60 / 68.62, CROM 0.2973, `ZSTART=3e7 LEAFSCALES=1` | the anomalous-driving receipt:37-38; the 133-bin receipt | one run for both pol names: they differed only in CRH0 |
| cc66_refit_verify | `HIER=1 LSTEP=8 LMAXL=1300` at the cc66 refit minimum | `refit_grid/launch.sh` | same |
| cc66_cr_x_lstep1 | **none recorded** (FOR_66_FROM_70.md:6250); default background, `LMAXL=1300 LSTEP=1` | — | ⚠ low confidence: `HIER=1 LSTEP=1 LMAXL=1300` |

**What could not be held.** The c54/item38 files were made at `KFAC=1` (k_max = LMAXL/D_M), which today's alias gate
refuses; they are rebuilt at the default `KFAC=2`. Their point was the built-in default with the onset solved to
l_A = 301.6; on the arm of record the onset is `ZSTART=3e7`, except the l_A = 340 injection, which keeps `LATARG=340`
and so solves its onset. The r6784/r6794/cc66 files ran at `LEAFSCALES=0` or their own CRH0/CROM; all now carry the
arm of record. Every file's `manifest` key says which applies.

**r6911 is the one family whose CONTROL file moves too (r7639, cc66's note).** The control's `r6911_source_lcdm`
carries `Dl_swap`, its source projected through the ARM's distance, so its `SRCXS` (1.004492152) is a coefficient
solved from the arm.  Per-file map:

| namesake | arm-of-record counterpart | what moved |
|---|---|---|
| `r6911_source_cr` | `r6911_source_cr_leafrec1` | the arm, everything |
| `r6911_source_cr_kcont` | `r6911_source_cr_kcont_leafrec1` | the arm, everything |
| `r6911_source_lcdm` | `r6911_source_lcdm_leafrec1` | `Dl_swap` and `xswap` only (`SRCXS` 1.004492152 → 1.012870613); the control's own `D_l` identical to 0 |

The same holds for r6919's control `viswap` (the arm's visibility width, 43.591 → 43.957), banked at r7639.
