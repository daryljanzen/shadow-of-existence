#!/bin/bash
# ** r6885+cc66.35, SECOND BATCH -- the LINE-OF-SIGHT path, because `DPSRC`/`SWSRC` are a KNOB
#    SHADOW on the hierarchy path: they are read only by `los_spectrum`'s source() (line 923-925),
#    and `HIER=1` takes the path at line 1238, which carries `_ISW` and NOT the other two.
#    DPSRC=0 on the refit configuration returns a BIT-IDENTICAL spectrum on both arms, which is the
#    signature of an unwired knob and not a null.  So the Doppler/monopole SHAPE is read on the path
#    where the switch reaches, with its own base for comparison.
# ** IDEMPOTENT AND RESUMABLE. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6885
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && { echo "  skip $tag"; return 0; }
  env "$@" LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "los_lcdm     $LCDM" \
 "los_cr       $CR" \
 "losdp0_lcdm  $LCDM DPSRC=0" \
 "losdp0_cr    $CR DPSRC=0" \
 "lossw0_lcdm  $LCDM SWSRC=0" \
 "lossw0_cr    $CR SWSRC=0" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6885 LOS BATCH COMPLETE $(date -u) ==="
