#!/bin/bash
# ** r7041 ⓒ AND ⓐ, SLICED -- because this container restarts faster than an unsliced run finishes. **
#
# ⛔ ** THE DEFECT THIS REPLACES IS MINE AND IT IS A REAL ONE. **  `launch_c.sh` ran each configuration
#   UNSLICED, one process for the whole k axis, for a bookkeeping reason: `KFAC` and `NK` are settings
#   under test and they move the mode count, so asserting a slice tiling needs that count.
#     ⇒ *** THAT MADE EVERY RUN AN ALL-OR-NOTHING 28-MINUTE UNIT. ***  This container restarted three
#       times during the revision -- 77 minutes, then 10 -- and a 28-minute unit cannot complete inside
#       a 10-minute window, so stage ⓒ sat at 5 of 48 while relaunching did nothing.  *`r6911` and
#       `r6919` both sliced, and this is why: a slice is 40 s to 2 min and saves ITSELF.*
#
# ⛭ ** AND THE BOOKKEEPING OBJECTION DISSOLVES, MEASURED RATHER THAN ARGUED. **
#   ① An out-of-range slice is SAFE: `kk = kk[_lo:_hi]` clamps, the run exits 0, and its `Dl` is
#     **exactly zero** (verified: `max|Dl| = 0.0`), so it adds nothing to the slice sum.
#   ② The instrument PRINTS its own mode count -- `modes = 2547` in the header -- so the launcher READS
#     the count instead of re-deriving the formula.  *A copy of a computation is a claim about it, which
#     is the same lesson `scripts/run_fast_job.sh` teaches about copying a list.*
#   ⇒ Two phases: every configuration's slice 0 first, in parallel; then the rest, sized from what each
#     slice-0 log reported.
#
# ** IDEMPOTENT AND RESUMABLE at SLICE granularity, which is the whole point. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
# ⛔⛔ ** ONE LAUNCHER AT A TIME, AND THIS IS NOT A PRECAUTION -- IT HAPPENED. **
# *Two instances of this script ran together at r7041+cc66.70, each with its own `xargs -P 4`, and both
# picked up `inj_fixed_cr_nlos2240_k0`: TWO PROCESSES WRITING ONE `.npz`.  The cause was a kill-and-relaunch
# cycle that let a waiting `resume.sh` start a second launcher while the first was still going.*
#   ⇒ ** A half-written `.npz` would then be vouched for by its own `__DONE__` marker **, which is the worst
#   shape a bank can be in: present, plausible, and wrong.  *An idempotent launcher is not a safe one unless
#   it is also exclusive.*
exec 9>/tmp/n66/.r7041_launch.lock
if ! flock -n 9; then
  echo "  ⛔ another launcher holds the lock -- exiting rather than racing it for the same slices."
  exit 0
fi
D=/tmp/n66/r7041; mkdir -p $D/inj $D/real
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
W=250
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
SET=(
  "base    " "kfac26  KFAC=2.6" "kfac32  KFAC=3.2" "nlos1120 NLOS=1120"
  "nlos2240 NLOS=2240" "nlosw9  NLOSW=9.0" "nlosf90 NLOSF=0.90" "lstep4  LSTEP=4"
  "nlosw12 NLOSW=12.0" "kfac40  KFAC=4.0" "nk15    NK=1274" "nk20    NK=1698"
)
# the configuration table: outdir | tag | env  -- settings outermost so a partial read is a partial SEQUENCE
# ⛭⛭ ** EVERY INJECTION SLICE BEFORE ANY REAL-ARM SLICE, AND THAT IS A MEASURED DECISION. **
# *A first version interleaved them per setting.  An injection slice skips the solver and costs 40 s to 2
# min; a REAL slice carries the solver and costs several minutes.  Interleaved, the cheap stage ⓒ work
# queued behind expensive stage ⓐ work -- measured: one 25-minute window produced 6 completed slices,
# because four real slices held the four cores for most of it.*
#   ⇒ ** Stage ⓒ is the order's own sharpest handle AND the cheap one, so it finishes first. **  With this
#   container restarting every 10 to 25 minutes, the thing that matters is that SOMETHING completes and can
#   be reported, not that everything advances evenly.
CFG=""
for s in "${SET[@]}"; do
  set -- $s; sn=$1; shift; se="$*"
  for inj in "fixed SRCINJ=fixed" "sweepown SRCINJ=sweep SRCINJRS=own"; do
    set -- $inj; in=$1; shift; ie="$*"
    CFG="$CFG
$D/inj|inj_${in}_lcdm_${sn}|$LCDM LSTEP=8 LMAXL=2000 $ie $se
$D/inj|inj_${in}_cr_${sn}|$CR LSTEP=8 LMAXL=2000 $ie $se"
  done
done
for s in "${SET[@]}"; do
  set -- $s; sn=$1; shift; se="$*"
  CFG="$CFG
$D/real|real_lcdm_${sn}|$LCDM LSTEP=8 LMAXL=2000 $se SRCSAVE=$D/real/real_lcdm_${sn}_src.npz
$D/real|real_cr_${sn}|$CR LSTEP=8 LMAXL=2000 $se SRCSAVE=$D/real/real_cr_${sn}_src.npz"
done
CFG=$(printf '%s' "$CFG" | sed '/^$/d')
# ⛔⛭ ** THE ARM'S `NK` AXIS IS NOT A CONVERGENCE AXIS, AND ITS RUNS ARE NOT QUEUED. **  Measured, not
# argued, and the measurement is upstream of any spectrum: `GRIDSAVE` writes the k axis and the visibility
# grid a configuration will use, and on the ARM `nk15` and `nk20` write a k axis **byte-identical to
# `base`** -- 1452 modes in all three, `np.array_equal` true on `k` AND on `eta`.  *The reason is in the
# instrument: on the arm the ladder is `sqrt(L(L+2))*stretch` out to `KMAXL` and `NK` is only a decimation
# cap that is never reached.*
#   ⇒ ** CONFIRMED AT THE SPECTRUM, on slices already banked: ** `real_cr_nk15_k0` and `real_cr_nk20_k0`
#   against `real_cr_base_k0` give `max|Dl| = 0.000e+00`, identical `ls`, on all of `Dl, ls, r_s, l_A, D_M`;
#   and `inj_fixed_cr` / `inj_sweepown_cr` at `nk15` vs `nk20` are equal on every array.
#   ⇒ ** AND THE CONTROL MOVES, which is what makes the arm's silence a reading and not a broken test: **
#   on `lcdm`, `NK` takes 2547 modes to 3822 to 5094 and the `nk15` / `nk20` spectra differ outright.
# ⛔ *** SO THE ARM'S `NK` SEQUENCE WOULD HAVE BEEN THE SAME COMPUTATION THREE TIMES, and reporting it as
#   "the arm does not move with NK, therefore converged in NK" would be vacuous -- the input never moved.
#   That is the corpus's own recurring defect: an instrument not matching the question it is asked.***
#   It is reported as INERT BY CONSTRUCTION, never as converged; the control's `NK` sequence stands and is
#   the one that carries the question.  *The already-banked arm slices are kept as the evidence above.*
CFG=$(printf '%s\n' "$CFG" | grep -vE '\|(inj_fixed|inj_sweepown|real)_cr_nk(15|20)\|')
# ⛭ ** A CONFIGURATION ALREADY FINISHED UNSLICED IS HONOURED, NOT REDONE. **  Five configurations
# completed under `launch_c.sh` before the restarts made that scheme unworkable, and an unsliced `.npz`
# IS the sum its slices would produce -- so dropping them would discard about two and a half hours of
# finished compute to buy nothing.  *The fold reads whichever form is present; see `bank_sliced.py`.*
KEEP=""; DROP=0
while IFS='|' read -r o t e; do
  if [ -s "$o/$t.npz" ] && [ -s "$o/$t.log" ] && grep -q '^__DONE__' "$o/$t.log"; then
    echo "  keep (unsliced, already complete) $t"; DROP=$((DROP+1)); continue
  fi
  KEEP="$KEEP
$o|$t|$e"
done <<< "$CFG"
CFG=$(printf '%s' "$KEEP" | sed '/^$/d')
echo "  $DROP configuration(s) already complete unsliced and left alone"
echo "--- PHASE 1: slice 0 of $(printf '%s\n' "$CFG" | wc -l) configurations, to read each mode count ---"
printf '%s\n' "$CFG" | while IFS='|' read -r o t e; do
  echo "$o ${t}_k0 $e KSLICE=0:$W"
done | xargs -P 4 -I{} bash -c 'run {}'
echo "--- PHASE 2: the remaining slices, sized from what each slice-0 log reported ---"
LIST=""
while IFS='|' read -r o t e; do
  n=$(grep -oE 'modes = [0-9]+' "$o/${t}_k0.log" 2>/dev/null | head -1 | grep -oE '[0-9]+')
  [ -z "$n" ] && { echo "  ⚠ $t: slice 0 did not report a mode count -- its remaining slices are NOT queued"; continue; }
  i=$W
  while [ "$i" -lt "$n" ]; do
    LIST="$LIST
$o ${t}_k$i $e KSLICE=$i:$((i+W))"
    i=$((i+W))
  done
done <<< "$CFG"
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7041 SLICED LAUNCH COMPLETE $(date -u) ==="
