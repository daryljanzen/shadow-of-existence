#!/bin/bash
# r7870+60, on order `r7869` item ②: ** THE SEPARATING GRID -- THE REPAIR ON, AND NO OFFSET AT
# ALL. **
#
# ⛔ WHY THIS GRID EXISTS.  `r7866`'s re-solve changed TWO things at once: it put the spectra on
# the repaired Fermi-Dirac background AND it added the ruling's `N_eff` offset to the control.  The
# unreadable minimised profile that came back could not be attributed to either, and this grid is
# the third rung that separates them -- the repair ON, the offset UNSET on both arms.
#
# ⚠ ** AND IT IS RUN WITH ITS OWN PREMISE UNDER DOUBT, WHICH IS STATED HERE RATHER THAN LEFT TO A
# READER. **  `r7870` measured that the unreadability is explained by the PROFILER mixing two
# basins: the lower basin reaches five nodes, the dip at the top node was the basin switch, and on
# a one-basin envelope the profile is monotonic and the limit reads.  *If that holds, the
# unreadability is neither the repair nor the ruling, and the fork this grid was ordered to settle
# has no slot for the answer.*  ⇒ The grid is run anyway, for two reasons that do not depend on
# the fork: the order ruled it, and the four-rung decomposition it completes -- the landed bank,
# this grid, the repair at `+0.0293`, the repair at `+0.044` -- is wanted whatever carried the
# unreadability.  *The doubt is routed to `69` in the channel, with this grid named as running so
# it can be stopped.*
#
# ⌗ NOT RETYPED: this is `r7866`'s own generator with the offset REMOVED from the control's
#   invocation and the output directory keyed to that, so nothing else can drift between the rungs.
# ⌗ OUTPUT IS KEYED BY CONFIGURATION, in the DIRECTORY and not only in a log.
# ⌗ IDEMPOTENT: a completed point is skipped.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/pol_grid_bvel1_nufd_only"}
JOBS=${JOBS:-4}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

CR_H0=68.570730; CR_OM=0.291246; CR_WB=0.021643; CR_NS=1.015066
LC_H0=67.40;     LC_OM=0.3150;   LC_WB=0.0224;   LC_NS=0.965
S_H0=2.0; S_OM=0.0150; S_WB=0.0008; S_NS=0.020

run() {   # run <arm> <tag> <MNU> <H0> <OM> <WB> <NS>
  local arm=$1 tag=$2 mnu=$3 h0=$4 om=$5 wb=$6 ns=$7
  local f="$OUT/${arm}_${tag}.npz"
  if [ -s "$f" ]; then echo "  [have] $arm $tag"; return 0; fi
  if [ "$arm" = cr ]; then
    env BVEL=1 NUFD=1 ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env BVEL=1 NUFD=1 ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LMAXL=2000 LSTEP=8 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  fi
  echo "  $arm $tag rc=$?" >> "$OUT/done.txt"
  echo "  [done] $arm $tag"
}

JOBLIST=()
for arm in lcdm cr; do
  if [ "$arm" = cr ]; then h0=$CR_H0; om=$CR_OM; wb=$CR_WB; ns=$CR_NS
  else h0=$LC_H0; om=$LC_OM; wb=$LC_WB; ns=$LC_NS; fi
  # the sum's own grid, at the centre
  for s in "-0.12 Sm12" "-0.06 Sm06" "0.00 S000" "0.06 S006" "0.15 S015" "0.30 S030" "0.45 S045" "0.60 S060"; do
    set -- $s
    JOBLIST+=("$arm $2 $1 $h0 $om $wb $ns")
  done
  # the four banked directions, at zero sum
  JOBLIST+=("$arm H0p 0.00 $(python3 -c "print($h0+$S_H0)") $om $wb $ns")
  JOBLIST+=("$arm H0m 0.00 $(python3 -c "print($h0-$S_H0)") $om $wb $ns")
  JOBLIST+=("$arm OMp 0.00 $h0 $(python3 -c "print($om+$S_OM)") $wb $ns")
  JOBLIST+=("$arm OMm 0.00 $h0 $(python3 -c "print($om-$S_OM)") $wb $ns")
  JOBLIST+=("$arm WBp 0.00 $h0 $om $(python3 -c "print($wb+$S_WB)") $ns")
  JOBLIST+=("$arm WBm 0.00 $h0 $om $(python3 -c "print($wb-$S_WB)") $ns")
  JOBLIST+=("$arm NSp 0.00 $h0 $om $wb $(python3 -c "print($ns+$S_NS)")")
  JOBLIST+=("$arm NSm 0.00 $h0 $om $wb $(python3 -c "print($ns-$S_NS)")")
done

MAXB=${MAXB:-0}; B=0
# ⌗ FILTER TO WHAT IS OUTSTANDING BEFORE BATCHING.  The first form counted a batch of four
#   already-banked points as a batch, so `MAXB=1` stopped having run nothing at all.
TODO=()
for j in "${JOBLIST[@]}"; do
  set -- $j
  [ -s "$OUT/$1_$2.npz" ] || TODO+=("$j")
done
echo "  ${#JOBLIST[@]} point(s) in the list, ${#TODO[@]} outstanding"
JOBLIST=("${TODO[@]:-}")
[ ${#TODO[@]} -gt 0 ] || { echo "  nothing outstanding"; exit 0; }
echo "  ${#JOBLIST[@]} point(s) to run, $JOBS at a time, into $OUT"
i=0
while [ $i -lt ${#JOBLIST[@]} ]; do
  pids=()
  for _ in $(seq 1 "$JOBS"); do
    [ $i -lt ${#JOBLIST[@]} ] || break
    set -- ${JOBLIST[$i]}
    run "$1" "$2" "$3" "$4" "$5" "$6" "$7" & pids+=($!)
    i=$((i+1))
  done
  for p in "${pids[@]}"; do wait "$p"; done
  B=$((B+1)); if [ "$MAXB" -gt 0 ] && [ "$B" -ge "$MAXB" ]; then echo "  stopping after $B batch(es), as asked"; break; fi
done
echo "ALL DONE"; ls "$OUT"/*.npz 2>/dev/null | grep -vc "_tt" | sed 's/^/  polarisation banks: /'
