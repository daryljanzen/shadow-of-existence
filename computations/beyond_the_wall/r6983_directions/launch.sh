#!/bin/bash
# ** r6983 ⓵ -- THE JOINT RUN: BOTH CHANNELS AT THEIR OWN MEASURED SIZES, TOGETHER. **
#
#   The row's question is no longer which channel carries the excess but how two channels compose.  Both
#   knobs are already wired and both individual responses are banked, so this adds ONE spectrum and no new
#   machinery: the window's spread matched to the arm's and weight-preserving (`SRCTAPER` with
#   `SRCTAPERNORM=1`, the coefficient solved at r6959) TOGETHER WITH the arm's monopole fraction imposed
#   (`DPSRC=0.8794`, solved at r6975).  Neither coefficient is re-chosen here.
#
#   `LSTEP=1 LMAXL=2000` is `r6941_fine_*`'s own grid, so the joint response is read against the same
#   baselines with the same locator as each channel alone.  Sliced and idempotent.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6983; mkdir -p $D/joint
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"

run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the instrument's switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
  [ $rc -eq 0 ] || { echo "  ⛔ $tag FAILED"; return 1; }; }
export -f run; export D

echo "=== the standing switch guard, on every distinct environment, before the set goes out ==="
ok=1
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 \
    SRCTAPER=0.0001100877765 SRCTAPERS0=145.3465211 SRCTAPERNORM=1 DPSRC=0.8794 || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

LIST=""
add () { tag=$1; nk=$2; shift 2
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/joint ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
add joint_lcdm 2547 $LCDM LSTEP=1 LMAXL=2000 \
    SRCTAPER=0.0001100877765 SRCTAPERS0=145.3465211 SRCTAPERNORM=1 DPSRC=0.8794
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6975 LAUNCH COMPLETE $(date -u) ==="
ls $D/joint/*.npz | wc -l
