#!/bin/bash
# ** r7091 ⓐ -- THE ONE-CLOCK RUN, AND ITS BEFORE IS ALREADY BANKED. **
#
#   The BEFORE is `/tmp/n66/refit/verify_cr.npz` and `verify_lcdm.npz` -- the refit's own VERIFIED
#   minimum, run at the best-fit parameters on the reporting path.  ** The arm's default output is
#   BIT-IDENTICAL under this revision's patch (checked, not assumed), so the banked before is the
#   before and nothing is re-run to produce it. **
#
#   ⛭ ** ONE RUN IS NEEDED: the arm with `LEAFGEOM=1`, at the SAME parameters. **  The parameters are
#   the STACKING-geometry best fit, and they are deliberately not refitted: holding them fixed makes
#   the comparison an isolation of the CLOCK and nothing else, and it disadvantages the after if it
#   disadvantages either.  *A refit under the new geometry is a second question and `70` is auditing
#   the rigidity that would decide it.*
#
#   ⌗ The control needs no run at all: `Hleaf` and `Hphys` are character-identical there, so
#   `LEAFGEOM` is a provable no-op -- verified bit-identical at LMAXL=300 before this was launched.
#
# IDEMPOTENT on each run's own __DONE__ marker.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7091; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"

run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__' "$D/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }

# the AFTER: one clock end to end -- leaf geometry, leaf scales, leaf perturbations
run cr_oneclock $CR LEAFGEOM=1
# ⌗ and the BEFORE re-run under THIS revision, to prove the banked one is reproducible rather than
#   merely assumed bit-identical -- cheap beside the point it secures.
run cr_before   $CR
# ⛭ ** AND THE CONTROL'S NO-OP ON THE REPORTING PATH, not only at the cheap setting. **  The argument
#   that `LEAFGEOM` cannot touch the control is textual -- `Hleaf` and `Hphys` are character-identical
#   when `RAD_IN_RATE` is true -- and a textual argument about a switch is exactly what the knob-shadow
#   practice says to check at the path that reports.  *These two must come back BIT-identical.*
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
run lcdm_before   $LCDM
run lcdm_oneclock $LCDM LEAFGEOM=1
