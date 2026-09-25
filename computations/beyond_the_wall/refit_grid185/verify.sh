#!/bin/bash
# ** VERIFY THE 185-BIN MINIMUM WITH REAL RUNS, r6825+cc66.25. **  The response model says where to
# go; a full run says what is there.  Lensed best fits from /tmp/n66/refit185/best_*_L.npy.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/refit185
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && { echo "  skip $tag"; return 0; }
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
printf '%s\n' \
 "verify_lcdm  ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248" \
 "verify_cr    ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== VERIFICATION COMPLETE $(date -u) ==="
