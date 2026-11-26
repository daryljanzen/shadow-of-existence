#!/bin/bash
# r7878+60, on order `r7877` items ① and ②: ** THE THREE CHANGES ONE AT A TIME, AND THE EXACT
# ADIABATIC SOUND SPEED WITH ALL THREE. **
#
# ⌗ NOT RETYPED: this is `r7876`'s own `gen_nupert.sh` with the shear arm dropped -- that arm is
#   settled, `0.0037550` and `0.0036366` in `A`, two per cent of the overshoot -- and `NUPARTS`
#   added. `LMAXL`, `LSTEP`, `HIER` and the control's four parameters are UNCHANGED, so the
#   multipoles are the same 238 and the landed `lcdm_S000.npz` still serves as the zero leg.
#
# ⛔ WHY THE ZERO LEG IS NOT RE-RUN, unchanged from `r7876`: `NUFD` is gated on `MNU != 0`, so at
#   the zero sum the Fermi-Dirac factor is identically 1, `w_nu` is exactly `1/3`, and every switch
#   in this family is PROVABLY INERT -- which is also why they refuse to run there.
#
# ⌗ EIGHT POINTS, and the ninth and tenth wait on ①'s verdict by design: the subset for ② is named
#   from ① before its `A` is quoted, so the choice cannot be read off the answer.
#     W / C / E     -- one change each, at both sums                         (six)
#     A1 (= WCE with NUCA=1) -- the exact adiabatic sound speed, all three   (two)
# ⌗ IDEMPOTENT: a completed point is skipped.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/parts"}
JOBS=${JOBS:-4}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

run() {   # run <tag> <MNU> <NUPARTS> <NUCA>
  local tag=$1 mnu=$2 parts=$3 nuca=$4
  local f="$OUT/lcdm_${tag}_tt.npz"
  if [ -s "$f" ]; then echo "  [have] $tag"; return 0; fi
  env BVEL=1 NUFD=1 NUPERT=1 NUPARTS="$parts" NUCA="$nuca" ARM=lcdm \
      LH0="$LC_H0" LOM="$LC_OM" WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 \
      SAVE="$f" POLSAVE="$OUT/lcdm_${tag}_pol.npz" \
      python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_${tag}.log" 2>&1
  local rc=$?
  echo "  [$tag] rc=$rc"
  [ $rc -eq 0 ] || return 1
}

# ⌘ r7878 ②: the subset legs are appended AFTER `SUBSET_NAMED.md` named the subset and was
#   committed and pushed — `CE`, by exclusion of the one member ① condemns.  The naming is in
#   the record before these two lines existed, which is what the registration asks of the ordering.
SPECS=${SPECS:-"S030W 0.30 W 0|S060W 0.60 W 0|S030C 0.30 C 0|S060C 0.60 C 0|S030E 0.30 E 0|S060E 0.60 E 0|S030A1 0.30 WCE 1|S060A1 0.60 WCE 1|S030CE 0.30 CE 1|S060CE 0.60 CE 1"}

pids=()
IFS='|' read -ra LIST <<< "$SPECS"
for spec in "${LIST[@]}"; do
  set -- $spec
  run "$1" "$2" "$3" "$4" &
  pids+=($!)
  while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do wait -n; done
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=1; done
echo "done fail=$fail" | tee "$OUT/done.txt"
exit $fail
