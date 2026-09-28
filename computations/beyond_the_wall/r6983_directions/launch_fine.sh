#!/bin/bash
# ** r6983 ⓵b -- THE SAME RUN, RE-SLICED FINER, FOR AN OPERATIONAL REASON AND NOT A PHYSICAL ONE. **
#
#   ⚠ *** WHY THIS FILE EXISTS. ***  This seat's container is reclaimed every ten to twenty minutes, and
#   a 250-mode slice above k-index 750 takes longer than that -- so those slices were restarting from
#   zero at every churn and would never have landed, while the three below 750 (which take three to six
#   minutes) landed first time.  ⇒ ** The fix is to make each unit of work smaller than the churn
#   window, not to change what is computed. **
#
#   `KSLICE=lo:hi` is a plain index slice of the mode list, so ANY tiling of `[0, 2547)` into disjoint
#   contiguous spans sums to the same spectrum.  This file tiles `[750, 2547)` at 100 modes; the three
#   already-banked slices carry `[0, 750)` at 250.  `bank.py` verifies the tiling rather than assuming a
#   fixed step, which is what makes the change safe to make midway.
#
#   ⛔ **NOTHING ABOUT THE OPERATION MOVES**: same switches, same coefficients, same `LSTEP=1 LMAXL=2000`
#   grid.  The tags carry their span (`_s<lo>_<hi>`) so a slice can never be confused with the coarse
#   `_k<lo>` slice that covers a different range under a similar name.
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

LIST=""
i=750
while [ $i -lt 2547 ]; do
  j=$((i+100)); [ $j -gt 2547 ] && j=2547
  LIST="$LIST
$D/joint joint_lcdm_s${i}_${j} $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=0.0001100877765 SRCTAPERS0=145.3465211 SRCTAPERNORM=1 DPSRC=0.8794 KSLICE=${i}:${j}"
  i=$j
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6983 FINE LAUNCH COMPLETE $(date -u) ==="
ls $D/joint/*.npz | wc -l
