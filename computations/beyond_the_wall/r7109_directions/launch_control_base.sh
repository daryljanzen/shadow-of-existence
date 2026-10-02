#!/bin/bash
# ** r7109 ⓶ -- THE CONTROL'S BASE RUN AT THE GRIDS' OWN SETTINGS, so the peak-height cell beside
#    the three grids is a SIGN rather than an empty cell. **
#
#   `70`'s three-grid audit closes with the one thing the banked set could not say: *"the control's
#   base has no log banked beside the grids; its peak ratios are not compared here."*  The arm's two
#   logs are banked (`cr_base.log` in each grid) and print `P1/P2 = 2.283` licensed and `2.199`
#   forbidden -- but with no control row, a reading that the forbidden configuration's HEIGHTS look
#   better cannot be told apart from the forbidden configuration's heights being THE CONTROL'S, which
#   is what its chi^2, its crossings and its longest run already are.
#
# ⛭ ** WHY THE CONTROL HAS NO LOG IN THE FIRST PLACE, AND IT IS NOT AN OVERSIGHT. **  Both grid
#   launchers COPY the control's nine spectra from `refit_grid185/` rather than re-running them --
#   `LEAFGEOM` and `LEAFREC` are provable no-ops on the control (`Hleaf` and `Hphys` are
#   character-identical when radiation is in the rate) and the copy was verified BIT-IDENTICAL.  *The
#   copy carried the spectrum and not the stdout, and the peak table is printed to stdout.*
#
# ⚠ ** SO THE LOG THAT DESCRIBES THE BANKED CONTROL ALREADY EXISTS and this run does not replace it. **
#   `refit185/lcdm_base.log` is the ORIGINAL stdout of the run whose `.npz` IS the banked file, md5
#   `5df16bcd401dcd2a624fb230313c97f7` on all three grids.  *A re-run's log would describe a re-run;
#   the original describes the artefact, which is the stronger record and is the one banked.*
#   ⇒ ** THIS RUN IS THE INDEPENDENT CHECK, which is what the order's "one run" buys: that the
#   instrument AS IT IS NOW still returns that spectrum at the control's own settings. **  It is also
#   the live re-proof of the `LEAFREC` no-op, because `LEAFREC` defaults to 1 since r7095+cc66.75 and
#   the banked control predates that flip -- so a reproduction here is the no-op measured, not argued.
#
# ⌗ ** THE .npz WILL NOT BE BYTE-IDENTICAL AND THAT IS EXPECTED, NOT A FAILURE. **  The config writer
#   (r7109 ⓵) adds a `config` key no banked grid file carries, so the comparison is on the ARRAYS --
#   `ls`, `Dl`, `l_A`, `D_M`, `r_s` -- and the receipt makes it there rather than on bytes.
#
# ** IDEMPOTENT AND RESUMABLE ** on the output's existence.  KFAC stays 2.0.  NK is not reduced.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7109_control; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

# the control at `refit_grid185/launch.sh`'s own lcdm_base line, verbatim: ARM=lcdm and nothing else,
# under the grids' shared HIER=1 LSTEP=8 LMAXL=2000
if [ -s "$D/lcdm_base.npz" ]; then
  echo "  skip lcdm_base (done)"
else
  env ARM=lcdm HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/lcdm_base.npz \
    python3 -u ACOUSTIC_two_arm.py > $D/lcdm_base.log 2>&1
  echo "  done lcdm_base rc=$? $(date -u +%H:%M:%S)"
fi
echo "=== r7109 CONTROL BASE: $(ls $D/lcdm_base.npz 2>/dev/null | wc -l)/1 at $(date -u) ==="
