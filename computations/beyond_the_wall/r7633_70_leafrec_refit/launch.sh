#!/bin/bash
# r7633+70: r6941's 185-bin refit grid for the CR arm, at the ruled LEAFREC=1 (the instrument default), based at
# r6941's own best point.  Same steps, same switches as refit_grid185/launch.sh.  Idempotent: skips a finished run.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/refit1}; mkdir -p $D
B="ARM=cr ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && { echo "  skip $tag"; return 0; }
  env OMP_NUM_THREADS=2 "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
H=68.581133; O=0.297209; W=0.021524; N=0.997952
printf '%s\n' \
 "cr_base $B CRH0=$H CROM=$O WBH2=$W NS=$N" \
 "cr_H0p $B CRH0=70.581133 CROM=$O WBH2=$W NS=$N" "cr_H0m $B CRH0=66.581133 CROM=$O WBH2=$W NS=$N" \
 "cr_OMp $B CRH0=$H CROM=0.312209 WBH2=$W NS=$N" "cr_OMm $B CRH0=$H CROM=0.282209 WBH2=$W NS=$N" \
 "cr_WBp $B CRH0=$H CROM=$O WBH2=0.022324 NS=$N" "cr_WBm $B CRH0=$H CROM=$O WBH2=0.020724 NS=$N" \
 "cr_NSp $B CRH0=$H CROM=$O WBH2=$W NS=1.017952" "cr_NSm $B CRH0=$H CROM=$O WBH2=$W NS=0.977952" \
 | xargs -P 2 -I{} bash -c 'run {}'
echo "=== GRID COMPLETE $(date -u) ==="
