#!/bin/bash
# r7866+60 ADDENDUM, on order `r7867` (69): THE CONTROL AT `DNEFF = +0.044`, NOT `+0.0293`.
#
# ⛔ WHY. `r7865` ordered the control at `+0.0293`, quoting the reference as `N_eff = 3.0293`.
#   `r7867` corrects it: cc66 read the CAMB object its reference actually builds and it is
#   `N_eff = 3.044000` -- the `3.0293` was the effective massless count plus the INTEGER massive
#   count, where CAMB's one massive state is worth `1.0147` in those units.  So the gap from this
#   instrument's `3.000` is `0.044`, and the order says to re-read the control at it.
#   ⇒ This revision's control ran at `+0.0293`, which is STATED in its record; this grid is the
#   re-read the order asks for, and ONLY the control arm needs it -- the arm of record carries no
#   `DNEFF` under either figure.
#
# ⌗ THIS FILE IS THIS REVISION'S OWN `nufd` GENERATOR WITH ONE NUMBER CHANGED AND THE OUTPUT
#   DIRECTORY KEYED TO IT, so the two settings cannot be confused for one another.
#
# —— what follows is this revision's own text, which is r7860's ——
# r7866+60, on order `r7865` item ③: THE SAME GRID AGAIN, ON THE REPAIRED NEUTRINO BACKGROUND.
#
# ⛔ WHY THIS EXISTS AND WHY IT IS A COPY, for the same reason `r7860`'s was.  `r7864` repaired
# the massive-neutrino background behind `NUFD`, and the switch changes the SOLVER at every
# epoch, so the grid has to be run again rather than scaled.  `r7865`'s ruling adds `DNEFF` for
# the CONTROL ONLY, to match the reference's `N_eff = 3.0293`; the arm of record is left alone,
# because the order says the arm's `N_eff` is a separate question it does not open.
#
# ⌗ THIS FILE IS `r7860`'s `gen_pol_bvel1.sh` WITH TWO CHANGES AND NOTHING ELSE: `NUFD=1` added
#   to both invocations, `DNEFF=0.044` added to the `lcdm` one, and the output directory keyed to
#   those switches.  The switch sets are not retyped, so nothing can drift between the two grids.
# ⌗ THE DIRECTORY SAYS WHICH BACKGROUND MADE IT, which is the whole point of `r7864`'s
#   precondition: the old bank could not say which background it was solved on, and this one can.
#
# —— what follows is `r7860`'s own text ——
# r7860+60, on order `r7857` item ④: THE SAME GRID, WITH `BVEL` ON.
#
# ⛔ WHY THIS EXISTS AND WHY IT IS A COPY.  The ordered control wants `BVEL`, `PRIMNORM` and
# `FOURPI` all on.  `FOURPI` is exactly twice the committed grid, measured at the bank's own reach
# (`doubling.py`), and `PRIMNORM` is a constant per point read from that point's own `n_s`.  `BVEL`
# is neither: it changes the SOLVER, so the grid has to be run again -- 32 points, one of them
# measured here at about 35 minutes on four cores.
#
# ⌗ THE SWITCH SETS BELOW ARE NOT RETYPED.  This file is `r7842`'s own `gen_pol_batched.sh` with
#   `BVEL=1` added to each invocation and the output directory keyed to that switch, so the two
#   grids cannot be confused for one another and nothing else can drift between them.
# ⌗ OUTPUT IS KEYED BY CONFIGURATION, in the DIRECTORY and not only in a log: a grid whose
#   filenames do not say which switches made it is the defect `r7805` measured.
# ⌗ IDEMPOTENT: a completed point is skipped, so a batch stopped at its time limit is restarted
#   and not redone.
set -u
OUT=${OUT:-"$(cd "$(dirname "$0")/../bank" && pwd)/pol_grid_bvel1_nufd_dneff044"}
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
    env BVEL=1 NUFD=1 DNEFF=0.044 ARM=lcdm LH0="$h0" LOM="$om" WBH2="$wb" NS="$ns" MNU="$mnu" \
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
