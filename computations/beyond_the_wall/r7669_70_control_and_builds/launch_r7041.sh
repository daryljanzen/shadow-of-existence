#!/bin/bash
# r7669+70 ③: the r7041 acceptance bank on the arm of record.
#   r7041_directions/launch_grid.sh's 24 GRIDSAVE runs (12 settings x 2 arms, LSTEP=8 LMAXL=2000) and the five
#   k0 slices bank_acceptance.py folds, built twice through the identical code:
#     lr0/  the recorded recipe verbatim + LEAFREC=0  -- the recipe check, scored against the namesake's own sha256s
#     lr1/  the arm of record: CR at the refit licensed point, LEAFREC=1; the control's recipe + LEAFREC=1
#   W is the k0 slice width; 250 is the historical width bank_acceptance's slices predate the __SLICE__ line with.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7669/r7041}
W=${W:-250}
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR0="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
AR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066"
SET=("base" "kfac26 KFAC=2.6" "kfac32 KFAC=3.2" "kfac40 KFAC=4.0" "nk15 NK=1274" "nk20 NK=1698"
     "nlos1120 NLOS=1120" "nlos2240 NLOS=2240" "nlosw9 NLOSW=9.0" "nlosw12 NLOSW=12.0" "nlosf90 NLOSF=0.90"
     "lstep4 LSTEP=4")
grid () { out=$1; tag=$2; shift 2; f=$out/$tag.npz
  [ -s "$f" ] && { echo "  skip $tag"; return 0; }
  t0=$(date +%s); env HIER=1 "$@" GRIDSAVE=$f python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$? wall=$(( $(date +%s)-t0 ))s" >> $out/$tag.log
  grep -q 'GRIDSAVE:' $out/$tag.log || echo "  ⛔ $tag: no GRIDSAVE line"; }
slice () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  t0=$(date +%s); env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$? wall=$(( $(date +%s)-t0 ))s" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f grid slice
L=""
for lr in 0 1; do
  mkdir -p $D/lr$lr/grid $D/lr$lr/k0
  if [ $lr = 0 ]; then C=$CR0; else C=$AR; fi
  for s in "${SET[@]}"; do set -- $s; sn=$1; shift
    L="$L
grid $D/lr$lr/grid g_lcdm_$sn $LCDM LSTEP=8 LMAXL=2000 $* LEAFREC=$lr
grid $D/lr$lr/grid g_cr_$sn $C LSTEP=8 LMAXL=2000 $* LEAFREC=$lr"
  done
  L="$L
slice $D/lr$lr/k0 real_cr_base_k0 $C LSTEP=8 LMAXL=2000 LEAFREC=$lr KSLICE=0:$W
slice $D/lr$lr/k0 real_cr_nk15_k0 $C LSTEP=8 LMAXL=2000 NK=1274 LEAFREC=$lr KSLICE=0:$W
slice $D/lr$lr/k0 real_cr_nk20_k0 $C LSTEP=8 LMAXL=2000 NK=1698 LEAFREC=$lr KSLICE=0:$W
slice $D/lr$lr/k0 inj_fixed_lcdm_nk15_k0 $LCDM LSTEP=8 LMAXL=2000 SRCINJ=fixed NK=1274 LEAFREC=$lr KSLICE=0:$W
slice $D/lr$lr/k0 inj_fixed_lcdm_nk20_k0 $LCDM LSTEP=8 LMAXL=2000 SRCINJ=fixed NK=1698 LEAFREC=$lr KSLICE=0:$W"
done
T0=$(date +%s)
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c '{}'
echo "=== r7041 builds COMPLETE $(date -u) total_wall=$(( $(date +%s)-T0 ))s ==="
