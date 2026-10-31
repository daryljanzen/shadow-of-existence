# r7647+70 — PREDICTION (pushed before any run)

**`r6893_slice_check` at the arm of record.** The namesake is `r6893_directions/step0b.sh` folded by `bank2.py`'s
step 0b: a WHOLE run at `HIER=1 LSTEP=64 LMAXL=2000` against the sum of its 250-mode `KSLICE` pieces, per arm. The
arm-of-record version runs that recipe verbatim with `$CR` → the arm of record (68.570730 / 0.291246 / 0.021643 /
1.015066, ZSTART 3e7, LEAFSCALES 1) and `LEAFREC=1` set: `whole_cr` and `k0…k1250_cr` (six slices, the namesake's
own count).

**Bank form: an ADDITION, not a re-key** (69's r7647 convention). `spectra/r6893_slice_check_leafrec1.npz` carries
the namesake's twelve keys unchanged and adds `nsl__cr_leafrec1`, `amax__cr_leafrec1`, `rmax__cr_leafrec1`,
`ls__cr_leafrec1`, `Dl_whole__cr_leafrec1`, `Dl_sliced__cr_leafrec1`, with `config` and `manifest`. The control
(`__lcdm`) is not re-run: LEAFREC does not reach it (r7641: 3.6e-16).
- Readers run before the push: every file that names `r6893_slice_check` (by stem, not file name), and the touched-
  readers gate.

**Predictions.**
- Six slices tile the arm-of-record k range (the r7641 fineB slices at this point tiled 0–1452 in six), and
  `rmax__cr_leafrec1` < 1e-14, as the namesake's 1.9e-16 and the receipt's own gate. Reachable negative: ≥ 1e-14
  — slicing does not add at the arm of record, and every sliced bank on it (fineB, visleaf, r6941) is in question.
- `Dl_whole__cr_leafrec1` differs from the namesake's `Dl_whole__cr` (the point moved): max relative |Δ| in
  [1e-3, 1e-1].

**EFFORT.** 7 runs at LSTEP=64, ~15 min wall.
