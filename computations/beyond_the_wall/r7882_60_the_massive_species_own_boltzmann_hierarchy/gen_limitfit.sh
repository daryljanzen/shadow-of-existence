#!/bin/bash
# r7882+60 arm Ⓠ⓸ᵇ: ** THE MASSLESS LIMIT READ ON WHAT THE FIT ACTUALLY READS. **
#
# ⌗ NOT RETYPED: this is `r7876`'s own `gen_nupert.sh` with the two shear arms replaced by the
#   hierarchy on/off pair and the two sums replaced by the two LIMIT sums.  `LMAXL`, `LSTEP`,
#   `HIER` and the control's four parameters are UNCHANGED, so the multipoles are the bank's own
#   and `r7874`'s banked `lcdm_S000_tt.npz` serves as the zero leg without being recomputed.
#
# ⛔ THE SLOTS CARRY THE LIMIT SUMS, AS `PREDICTION.md` DECLARES BEFORE THESE LEGS WERE BUILT.
#   `shift.py`'s slots ARE the validation sums and it fits against CAMB at those sums, so there is
#   no CAMB target at 1e-3 or 1e-4.  The arm is a DIFFERENCE at a FIXED target -- on against off on
#   legs that share it -- so the target cancels and need not be the right one for the sum in the
#   slot.  `A` from these legs is NOT a validation number and is not reported as one.
#     S030  <-  Sigma = 1e-3        S060  <-  Sigma = 1e-4        S000  <-  r7874's zero leg
#
# ⛔ WHY THE ZERO LEG IS NOT RE-RUN.  `NUHIER` REFUSES a zero sum by design (it needs NUFD=1 and
#   MNU != 0), so the zero leg is the same spectrum with the switch on or off and re-running it
#   would only add a second copy of it.  Same reason `r7876` gave, for the same structure.
#
# ⌗ IDEMPOTENT: a completed point is skipped.  ⌗ The wall time of these legs IS the cost
#   measurement the declared risk asks for -- they are the first banked-resolution legs with the
#   hierarchy on, where the state vector is 176 per mode rather than 20.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/limitfit"}
JOBS=${JOBS:-4}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

run() {   # run <bank> <tag> <MNU> <NUHIER>
  local bank=$1 tag=$2 mnu=$3 hier=$4
  local d="$OUT/$bank"
  mkdir -p "$d"
  local f="$d/lcdm_${tag}_tt.npz"
  if [ -s "$f" ]; then echo "  [have] $bank/$tag"; return 0; fi
  local t0=$SECONDS
  env BVEL=1 NUFD=1 NUHIER="$hier" ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" \
      WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 \
      SAVE="$f" POLSAVE="$d/lcdm_${tag}_pol.npz" \
      python3 ACOUSTIC_two_arm.py > "$d/lcdm_${tag}.log" 2>&1
  local rc=$?
  echo "  [$bank/$tag] rc=$rc  wall=$((SECONDS-t0))s" | tee -a "$OUT/COST.txt"
  [ $rc -eq 0 ] || return 1
}

pids=()
for spec in "off S030 1e-3 0" "off S060 1e-4 0" "on S030 1e-3 1" "on S060 1e-4 1"; do
  set -- $spec
  run "$1" "$2" "$3" "$4" &
  pids+=($!)
  while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do wait -n; done
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=1; done
# ⛔ NO ZERO LEG IS PLACED HERE.  `shift.py` opens one file per slot under a BARE name and the
#   bank writes `_tt`/`_pol` pairs, so the fit cannot read a bank directory directly: `limitfit.py`
#   assembles its own leg directory, as `r7876`'s `legs()` does for the same fit, and takes the zero
#   leg from the LANDED bank there.  *This tail first copied `r7874`'s zero leg into each bank,
#   which the fit never reads — removed rather than left as a file that looks load-bearing.*
echo "done fail=$fail" | tee "$OUT/done.txt"
exit $fail
