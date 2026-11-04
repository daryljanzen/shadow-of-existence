#!/bin/bash
# r7677+70 item 2: r7041's injection sweep (r7041_directions/launch_sliced.sh's `inj` set) on the arm of record.
#   CR legs: the refit licensed point, LEAFREC=1 -- 2 injections x 10 settings (nk15/nk20 are `base` on the arm by
#   construction, gated in the fold). Control legs: the recorded control point with LEAFREC=1 -- 2 x 12 (NK is real
#   there). LSTEP=8 LMAXL=2000 HIER=1, each run UNSLICED (fold.load reads `<tag>.npz` + a `__DONE__` log).
#   Four at a time, longest-first, idempotent.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7677/inj}
mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 LEAFREC=1"
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1"
run () { tag=$1; shift
  [ -s "$D/$tag.npz" ] && grep -q '^__DONE__ rc=0' "$D/$tag.log" 2>/dev/null && { echo "  skip $tag"; return 0; }
  t0=$(date +%s); env HIER=1 "$@" SAVE=$D/$tag.npz python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  echo "__DONE__ rc=$? wall=$(( $(date +%s)-t0 ))s" >> $D/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
SET=("kfac40 KFAC=4.0" "nlos2240 NLOS=2240" "lstep4 LSTEP=4" "nk20 NK=1698" "kfac32 KFAC=3.2" "nk15 NK=1274"
     "nlos1120 NLOS=1120" "kfac26 KFAC=2.6" "nlosw12 NLOSW=12.0" "nlosw9 NLOSW=9.0" "nlosf90 NLOSF=0.90" "base")
L=""
for s in "${SET[@]}"; do set -- $s; sn=$1; shift; se="$*"
  for inj in "fixed SRCINJ=fixed" "sweepown SRCINJ=sweep SRCINJRS=own"; do set -- $inj; in=$1; shift; ie="$*"
    L="$L
inj_${in}_lcdm_${sn} $LCDM LSTEP=8 LMAXL=2000 $ie $se"
    case $sn in nk15|nk20) ;; *) L="$L
inj_${in}_cr_${sn} $AR LSTEP=8 LMAXL=2000 $ie $se";; esac
  done; done
T0=$(date +%s)
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7677 band-RMS builds COMPLETE $(date -u) total_wall=$(( $(date +%s)-T0 ))s ==="
