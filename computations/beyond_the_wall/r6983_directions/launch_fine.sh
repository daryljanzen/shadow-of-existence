#!/bin/bash
# ** r6983 ⓵b -- THE SAME RUN, RE-SLICED TO FIT THE CHURN WINDOW, AND GAP-DRIVEN. **
#
#   ⚠ *** WHY THIS FILE EXISTS. ***  This seat's container is reclaimed every few minutes and the
#   window is not constant.  A slice that takes longer than the window never lands however many times
#   it is relaunched -- it restarts from zero each time -- so the three 250-mode slices below mode
#   index 750 landed first time while every one above it did not.  ⇒ ** The unit of work has to be
#   smaller than the window, and the window moves, so the launcher has to be able to re-slice what is
#   left without losing what is done. **
#
#   `KSLICE=lo:hi` is a plain index slice of the mode list, so ANY tiling of `[0, 2547)` into disjoint
#   contiguous spans sums to the same spectrum.  ** So this launcher does not carry a fixed tiling at
#   all: it reads the spans already BANKED, computes the gaps, and tiles only those, at `STEP` (default
#   50). **  Re-running it after any churn is safe and costs only the slice that was in flight; running
#   it at a different `STEP` is safe too, because the gaps are recomputed from what exists.
#
#   ⛔ **NOTHING ABOUT THE OPERATION MOVES**: same switches, same two coefficients, same
#   `LSTEP=1 LMAXL=2000` grid.  Every tag carries its own span (`_s<lo>_<hi>`), and `bank.py` asserts
#   the banked spans tile `[0, 2547)` exactly -- so a wrong tiling is caught at the bank and cannot be
#   read as a spectrum.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6983; mkdir -p $D/joint
NK=${NK:-2547}; STEP=${STEP:-50}; JOBS=${JOBS:-4}
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

# the gaps, computed from the spans actually on disk -- `_s<lo>_<hi>` carries its span, `_k<lo>` is a
# 250-mode slice from the first tiling.  ⌗ Printed so a reader can see what is left before it runs.
GAPS=$(NK=$NK STEP=$STEP python3 - <<'PY'
import os, re
D, NK, STEP = '/tmp/n66/r6983/joint', int(os.environ['NK']), int(os.environ['STEP'])
have = []
for f in os.listdir(D):
    if not f.endswith('.npz'):
        continue
    m = re.search(r'_s(\d+)_(\d+)\.npz$', f) or re.search(r'_k(\d+)\.npz$', f)
    if m:
        lo = int(m.group(1))
        have.append((lo, int(m.group(2)) if m.lastindex == 2 else lo + 250))
have.sort()
gaps, at = [], 0
for lo, hi in have:
    if lo > at:
        gaps.append((at, lo))
    at = max(at, hi)
if at < NK:
    gaps.append((at, NK))
out = []
for a, b in gaps:
    i = a
    while i < b:
        j = min(i + STEP, b)
        out.append(f'{i} {j}')
        i = j
import sys
print('\n'.join(out))
print(f'  banked spans: {have}', file=sys.stderr)
print(f'  gaps to fill: {gaps}  -> {len(out)} slice(s) at STEP={STEP}', file=sys.stderr)
PY
)
[ -z "$GAPS" ] && { echo "=== nothing to do: the banked spans already tile [0, $NK) ==="; exit 0; }

LIST=""
while read -r i j; do
  [ -z "$i" ] && continue
  LIST="$LIST
$D/joint joint_lcdm_s${i}_${j} $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=0.0001100877765 SRCTAPERS0=145.3465211 SRCTAPERNORM=1 DPSRC=0.8794 KSLICE=${i}:${j}"
done <<< "$GAPS"
printf '%s' "$LIST" | sed '/^$/d' | xargs -P "$JOBS" -I{} bash -c 'run {}'
echo "=== r6983 FINE LAUNCH PASS COMPLETE $(date -u) ==="
ls $D/joint/*.npz | wc -l
