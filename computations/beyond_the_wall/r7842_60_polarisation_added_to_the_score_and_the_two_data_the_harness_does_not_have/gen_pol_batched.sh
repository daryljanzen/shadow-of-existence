#!/bin/bash
# r7842+60: the two arms' TT, TE and EE spectra, on order r7841 item ①.
#
# POLSAVE (r7631+70) is off by default, so EVERY point the fit needs has to be regenerated with it
# on: the sum's grid AND the four banked directions' plus and minus points, on both arms.  The
# switch values are the banked grid's own centre and step, read from `r7749_70_leafgeom_refit`'s
# CENTRE/STEP rather than retyped from a note, and the form switches are the ones whose cr run
# reproduced the banked base to one part in 1e12 at r7838.
#
# ⌗ A completed point is SKIPPED, so a batch stopped at its time limit is restarted and not redone.
# ⌗ Four at a time on a four-core box; POLSAVE reuses the Bessel pass, so it costs no second one.
set -u
OUT=${OUT:-/tmp/claude-0/pol_grid}
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
    env ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
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
echo "  ${#JOBLIST[@]} point(s) in the list, $JOBS at a time, into $OUT"
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
