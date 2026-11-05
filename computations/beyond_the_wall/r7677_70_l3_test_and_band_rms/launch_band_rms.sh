#!/bin/bash
# r7677+70 item 2: r7041's injection sweep (r7041_directions/launch_sliced.sh's `inj` set) on the arm of record.
#   CR legs: the refit licensed point, LEAFREC=1 -- 2 injections x 10 settings (nk15/nk20 are `base` on the arm by
#   construction). Control legs: the recorded control point with LEAFREC=1 -- 2 x 12 (NK is real there).
#   LSTEP=8 LMAXL=2000 HIER=1. SLICED on KSLICE (250 wide), each slice declaring `__SLICE__ lo:hi` in its log, so
#   r7041_directions/fold.load tiles it and a container restart costs at most one slice per worker.
#   (The first, unsliced, launch lost every run in flight to a container restart at about 100 min.)
#   Mode counts are the configurations' own, from spectra/r7041_accept_Al_leafrec1.npz (same points, same code).
#   Four at a time, longest configuration first, idempotent: re-run it after any restart.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7677/inj}
mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 LEAFREC=1"
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1"
W=250
run () { tag=$1; lo=$2; hi=$3; shift 3
  t=${tag}_k$lo
  [ -s "$D/$t.npz" ] && grep -q '^__DONE__ rc=0' "$D/$t.log" 2>/dev/null && return 0
  t0=$(date +%s); env HIER=1 "$@" KSLICE=$lo:$hi SAVE=$D/$t.npz python3 -u ACOUSTIC_two_arm.py > $D/$t.log 2>&1
  rc=$?
  if [ $rc -ne 0 ] || [ ! -s "$D/$t.npz" ]; then rm -f "$D/$t.npz"; echo "__FAILED__ rc=$rc" >> $D/$t.log; echo "  FAILED $t"; return 0; fi
  echo "__SLICE__ $lo:$hi" >> $D/$t.log; echo "__DONE__ rc=0 wall=$(( $(date +%s)-t0 ))s" >> $D/$t.log; }
export -f run; export D
NM=$(python3 -c "
import numpy as np
z=np.load('spectra/r7041_accept_Al_leafrec1.npz')
for a in ('cr','lcdm'):
    for t in ('base','kfac26','kfac32','kfac40','nk15','nk20','nlos1120','nlos2240','nlosw9','nlosw12','nlosf90','lstep4'):
        print(a, t, int(z[f'{a}_{t}_n'][0]))")
declare -A N; while read -r a t n; do N[$a.$t]=$n; done <<< "$NM"
SET=("kfac40 KFAC=4.0" "nk20 NK=1698" "kfac32 KFAC=3.2" "nlos2240 NLOS=2240" "lstep4 LSTEP=4" "nk15 NK=1274"
     "kfac26 KFAC=2.6" "nlos1120 NLOS=1120" "nlosw12 NLOSW=12.0" "nlosw9 NLOSW=9.0" "nlosf90 NLOSF=0.90" "base")
L=""
for s in "${SET[@]}"; do set -- $s; sn=$1; shift; se="$*"
  for inj in "fixed SRCINJ=fixed" "sweepown SRCINJ=sweep SRCINJRS=own"; do set -- $inj; in=$1; shift; ie="$*"
    for arm in lcdm cr; do
      case "$arm.$sn" in cr.nk15|cr.nk20) continue;; esac
      [ $arm = cr ] && E="$AR" || E="$LCDM"
      n=${N[$arm.$sn]}; lo=0
      while [ $lo -lt $n ]; do hi=$((lo+W)); [ $hi -gt $n ] && hi=$n
        L="$L
inj_${in}_${arm}_${sn} $lo $hi $E LSTEP=8 LMAXL=2000 $ie $se"; lo=$hi; done
    done; done; done
echo "  $(printf '%s' "$L" | sed '/^$/d' | wc -l) slices queued $(date -u +%H:%M:%S)"
T0=$(date +%s)
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7677 band-RMS builds COMPLETE $(date -u) total_wall=$(( $(date +%s)-T0 ))s ==="
