#!/bin/bash
# r7872+60, on order `r7871` item ①: ** THE CONTROL ARM WITH THE FERMI-DIRAC REPAIR EXPLICITLY
# OFF, SO "NUFD OFF" IS A LABELLED STATE AND NOT A PROVENANCE CLAIM. **
#
# ⛔ WHY THIS GRID EXISTS, AND WHY THE LANDED BANK COULD NOT SERVE AS THE OFF ARM.  The order says
# the response is already in the banks, and the ON side is: `pol_grid_bvel1_nufd_only` carries
# `NUFD: true` at every non-zero sum.  The OFF side is NOT there.  Two separate reasons, each
# sufficient:
#   ① The landed bank `pol_grid_bvel1` carries NO `NUFD` key and no `MNU` key at all -- it predates
#      the switch, which is `r7864`'s own recorded finding ("the gate is that the key is ABSENT...
#      these banks cannot say, and that is the finding").  Calling it "off" would be reading a
#      state off provenance that its own record refuses to state.
#   ② And it would not isolate `NUFD` even if it did: that bank also carries no `BVEL` and no
#      `FOURPI` key, so landed-against-separating changes more than one thing.  `r7869`'s whole
#      fork existed because a re-solve changed two things at once; this file exists so that this
#      comparison changes exactly one.
# ⇒ So the off arm is RUN, from `r7870`'s own generator with `NUFD=1` replaced by `NUFD=0` and the
#   output directory keyed to that.  `MNU` still enters: with the repair off the mass still leaves
#   the clustering matter (`OCDM = OM - OB - ONU`), so there is a sum response to measure.  What is
#   off is the background's Fermi-Dirac density and its running `w_nu`, and that alone.
#
# ⌗ OUTPUT IS KEYED BY CONFIGURATION, in the DIRECTORY and not only in a log.
# ⌗ IDEMPOTENT: a completed point is skipped.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/pol_grid_bvel1_nufd_off"}
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
    env BVEL=1 NUFD=0 ARM=cr CRH0="$h0" CROM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LEAFGEOM=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  else
    env BVEL=1 NUFD=0 ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
        HIER=1 LMAXL=2000 LSTEP=8 \
        SAVE="$OUT/${arm}_${tag}_tt.npz" POLSAVE="$f" \
        python3 ACOUSTIC_two_arm.py > "$OUT/${arm}_${tag}.log" 2>&1
  fi
  echo "  $arm $tag rc=$?" >> "$OUT/done.txt"
  echo "  [done] $arm $tag"
}

JOBLIST=()
# ⛔ NARROWED TO WHAT ITEM ① NEEDS, AND NARROWED RATHER THAN RE-AIMED: the CONTROL arm only, and
#   only the four sums the order names plus the zero the ratio divides by.  The arm of record is
#   not run here -- order `r7871` puts it behind ①.  Everything else in this file is `r7870`'s
#   separating-grid generator unedited, with ONE switch flipped, so nothing but `NUFD` can differ
#   between this bank and that one.
h0=$LC_H0; om=$LC_OM; wb=$LC_WB; ns=$LC_NS
for s in "0.00 S000" "0.06 S006" "0.30 S030" "0.60 S060"; do
  set -- $s
  JOBLIST+=("lcdm $2 $1 $h0 $om $wb $ns")
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
