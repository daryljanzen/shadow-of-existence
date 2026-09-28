#!/bin/bash
# ** r6975 ⓷ -- THE TERM-MIX SWAP, ON A KNOB THAT IS ALREADY WIRED. **
#
#   `cc66.47` measured the arm holding more of its window's power in the monopole in every band.  `DPSRC`
#   scales the Doppler term and nothing else, wired to the hierarchy path at r6889+cc66.36, and scaling it
#   by c scales its power by c^2 -- so the c that gives the control the arm's monopole fraction is fixed
#   by the SRCETA profiles.  Solved band by band it spans 0.860 to 0.897: ** one constant does it to two
#   per cent **, which is what makes this a one-parameter operation.
#
#   Two coefficients, so the response can be calibrated and inverted as cc66.47's taper response was:
#   the arm-matching 0.8794, and 0.60 as the larger excursion.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6975; mkdir -p $D/mix
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
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 DPSRC=0.8794 || ok=0
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 DPSRC=0.60   || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

LIST=""
add () { tag=$1; nk=$2; shift 2
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/mix ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
add mix_lcdm  2547 $LCDM LSTEP=1 LMAXL=2000 DPSRC=0.8794
add mixb_lcdm 2547 $LCDM LSTEP=1 LMAXL=2000 DPSRC=0.60
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6975 LAUNCH COMPLETE $(date -u) ==="
ls $D/mix/*.npz | wc -l
