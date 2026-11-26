#!/bin/bash
# r7876+60, on order `r7875` item ③: ** THE CONTROL ARM WITH `NUPERT` ON, so `A` and `eps` can be
# refitted against CAMB on the epoch-consistent perturbations. **
#
# ⌗ NOT RETYPED: this is `r7874`'s own `gen_srcdec.sh` with `SRCDEC` dropped and `NUPERT` added,
#   which is `r7872`'s NUFD-off generator with the switch back on upstream of that.  `LMAXL`,
#   `LSTEP`, `HIER` and the control's four parameters are UNCHANGED, so the multipoles are the same
#   238 and `r7874`'s banked `lcdm_S000_tt.npz` serves as the zero leg without being recomputed.
#
# ⛔ WHY THE ZERO LEG IS NOT RE-RUN.  `NUFD` is itself gated on `MNU != 0`, so at the zero sum the
#   Fermi-Dirac factor is identically 1, `w_nu` is exactly `1/3`, and `NUPERT` is PROVABLY INERT --
#   which is also why it refuses to run there rather than pretending to.  The zero leg is therefore
#   the same spectrum with or without this revision's switch, and re-running it would only add a
#   second copy of it.
#
# ⌗ TWO SHEAR ARMS, because the approximation's one declared gap is the shear ladder:
#     `on`  -- the ladder as it stands, the relativistic shear at all epochs
#     `off` -- `NUSHOFF=1`, the species' shear off below `w_nu = 1/6`
#   The SPREAD between them is the approximation's own uncertainty on `A`, measured and reported.
# ⌗ IDEMPOTENT: a completed point is skipped.

set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/nupert"}
JOBS=${JOBS:-4}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."

LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965

run() {   # run <tag> <MNU> <NUSHOFF>
  local tag=$1 mnu=$2 shoff=$3
  local f="$OUT/lcdm_${tag}_tt.npz"
  if [ -s "$f" ]; then echo "  [have] $tag"; return 0; fi
  env BVEL=1 NUFD=1 NUPERT=1 NUSHOFF="$shoff" ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" \
      WBH2="$LC_WB" NS="$LC_NS" MNU="$mnu" \
      HIER=1 LMAXL=2000 LSTEP=8 \
      SAVE="$f" POLSAVE="$OUT/lcdm_${tag}_pol.npz" \
      python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_${tag}.log" 2>&1
  local rc=$?
  echo "  [$tag] rc=$rc"
  [ $rc -eq 0 ] || return 1
}

pids=()
for spec in "S030on 0.30 0" "S060on 0.60 0" "S030off 0.30 1" "S060off 0.60 1"; do
  set -- $spec
  run "$1" "$2" "$3" &
  pids+=($!)
  while [ "$(jobs -rp | wc -l)" -ge "$JOBS" ]; do wait -n; done
done
fail=0
for p in "${pids[@]}"; do wait "$p" || fail=1; done
echo "done fail=$fail" | tee "$OUT/done.txt"
exit $fail
