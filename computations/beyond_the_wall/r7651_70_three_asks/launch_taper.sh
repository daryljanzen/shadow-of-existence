#!/bin/bash
# r7651+70 ①: r6959_directions/launch_b.sh's swap_lcdm verbatim (its run function and switch-line guard), at the
# re-solved SRCTAPER from taper.json; SRCTAPERS0 the banked one.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank7}; mkdir -p $D
rd () { python3 -c "import json;print('%.10g'%json.load(open('r7651_70_three_asks/taper.json'))['$1'])"; }
AL=$(rd alpha); S0=$(rd s0)
echo "  the swap at the arm of record's spread: SRCTAPER=$AL at SRCTAPERS0=$S0"
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
LIST=""; i=0
while [ $i -lt 2547 ]; do j=$((i+250)); LIST="$LIST
$D swap_lcdm_k${i} $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AL SRCTAPERS0=$S0 KSLICE=${i}:${j}"; i=$j; done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7651 TAPER COMPLETE $(date -u) ==="
