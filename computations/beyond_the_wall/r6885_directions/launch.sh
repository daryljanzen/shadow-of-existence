#!/bin/bash
# ** r6885+cc66.35 -- the candidate DIRECTIONS for Delta, each ONE knob off the arms' OWN 185-bin
#    minima (refit_grid185/verify.sh), so every difference is a shape at the place Delta is defined.
# ** IDEMPOTENT AND RESUMABLE **: skips any output already on disk.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6885
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && { echo "  skip $tag"; return 0; }
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
# priority order: the neutrino truncation first, because it can falsify ||Delta||^2 itself
printf '%s\n' \
 "ln24_lcdm    $LCDM LN=24" \
 "ln24_cr      $CR LN=24" \
 "dp0_lcdm     $LCDM DPSRC=0" \
 "dp0_cr       $CR DPSRC=0" \
 "noisw_lcdm   $LCDM NOISW=1" \
 "noisw_cr     $CR NOISW=1" \
 "dre0_lcdm    $LCDM DRE=0" \
 "dre0_cr      $CR DRE=0" \
 "drc0_lcdm    $LCDM DRC=0" \
 "drc0_cr      $CR DRC=0" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6885 DIRECTIONS COMPLETE $(date -u) ==="
