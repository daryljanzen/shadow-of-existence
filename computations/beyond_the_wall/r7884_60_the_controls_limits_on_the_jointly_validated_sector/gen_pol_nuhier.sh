#!/bin/bash
# r7884+60, on order `r7879` item ③: ** THE CMB GRID WITH THE JOINTLY VALIDATED CLOSURE ON. **
#
# ⚑ NOT RETYPED: this is `r7870`'s own `gen_pol_nufd_only.sh` with the hierarchy switched ON, the
#   grid pinned to the two numbers `r7882`'s gates fixed, and the sum nodes narrowed to the ones the
#   hierarchy can run at.  Nothing else differs, so a difference between these points and `r7870`'s
#   is the CLOSURE and not the method.
#
# ⛔ ONLY THE FIVE POSITIVE SUM NODES ARE HERE, AND THAT IS NOT A SHORTCUT.  `PREDICTION.md`'s
#   structural read ③: the switch refuses a zero sum, because at zero sum the species is exactly
#   massless and there is no massive species for its hierarchy to describe.  So the eight
#   parameter-offset directions per arm -- EVERY ONE of which `r7870` runs at `MNU = 0.00` -- and the
#   zero node itself are the SAME spectra with the hierarchy on or off, and are carried from the
#   landed grid WITHOUT approximation.  The limit read checks each carried point's own recorded
#   config rather than assuming it.
#
# ⚠ AND THE TWO NEGATIVE NODES ARE ABSENT BECAUSE THEY CANNOT BE RUN AT ALL.  A negative sum is
#   not a mass: the per-node energy has no reading at `y² < 0`.  `PREDICTION.md` registers that as a
#   fork on where the profile's minimum falls, with NO LIMIT READ if it falls at a negative node.
#
# ⚑ OUTPUT IS KEYED BY CONFIGURATION, in the DIRECTORY and not only in a log.
# ⚑ IDEMPOTENT: a completed point is skipped.
set -u
OUT=${OUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/pol_grid_bvel1_nuhier"}
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
    env BVEL=1 NUFD=1 NUHIER=1 NQ=12 LMAXNU=12 QMAXNU=20 ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env BVEL=1 NUFD=1 NUHIER=1 NQ=12 LMAXNU=12 QMAXNU=20 ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
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
  for s in "0.06 S006" "0.15 S015" "0.30 S030" "0.45 S045" "0.60 S060"; do
    set -- $s
    JOBLIST+=("$arm $2 $1 $h0 $om $wb $ns")
  done
  #: ⛔ *the eight parameter-offset directions are NOT here: every one of them is at a ZERO
  #: sum, where the hierarchy is provably inert, so they are CARRIED from the landed grid
  #: without approximation rather than re-run.  See PREDICTION.md reads ③ and ④.*
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
