#!/bin/bash
# ** r7049's OBSERVATION, TAKEN UP BECAUSE IT TURNED OUT TO BE FREE. **
#
#   66, offering and not directing: *"A_l is a sharper probe of the same thing and it is now free: it is
#   built from W_l = G_l^2 dk/k over the k-grid, so truncating k_max truncates the window the law integrates
#   over -- and A_l carries no fitted amplitude to absorb the truncation, where a height ratio does."*
#   ⌗ *"If it costs a re-run, it is not worth one."*
#
# ⇒ ** IT COSTS 1.45 SECONDS PER CONFIGURATION. **  `A_l` needs only the background -- the visibility, the
#   kernel's argument, the k axis and its measure, and r_s* -- none of which needs the solver or the
#   projection.  `GRIDSAVE` writes exactly those and returns before either.
#     ⇒ *** SO THE ACCEPTANCE CONVERGENCE CAN BE READ WITHOUT THE SWEEP, AND WITHOUT WAITING FOR IT. ***
#     That is a convergence statement about the operation the row is actually about, where the heights are
#     a statement about their quotient.
#
# ** 48 runs at about 1.5 s each.  No lock needed and no restart can cost more than one of them. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7041/grid; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
SET=(
  "base    " "kfac26  KFAC=2.6" "kfac32  KFAC=3.2" "kfac40  KFAC=4.0"
  "nk15    NK=1274" "nk20    NK=1698" "nlos1120 NLOS=1120" "nlos2240 NLOS=2240"
  "nlosw9  NLOSW=9.0" "nlosw12 NLOSW=12.0" "nlosf90 NLOSF=0.90" "lstep4  LSTEP=4"
)
n=0
for s in "${SET[@]}"; do
  set -- $s; sn=$1; shift; se="$*"
  for a in "lcdm $LCDM" "cr $CR"; do
    set -- $a; an=$1; shift; ae="$*"
    f=$D/g_${an}_${sn}.npz
    [ -s "$f" ] && { echo "  skip g_${an}_${sn}"; continue; }
    env HIER=1 $ae LSTEP=8 LMAXL=2000 $se GRIDSAVE=$f python3 -u ACOUSTIC_two_arm.py \
        > $D/g_${an}_${sn}.log 2>&1
    grep -q 'GRIDSAVE:' "$D/g_${an}_${sn}.log" && { echo "  done g_${an}_${sn}"; n=$((n+1)); } \
      || echo "  ⚠ FAILED g_${an}_${sn} -- see $D/g_${an}_${sn}.log"
  done
done
echo "=== $n grid(s) written $(date -u) ==="
