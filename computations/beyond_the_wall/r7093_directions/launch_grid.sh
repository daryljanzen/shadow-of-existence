#!/bin/bash
# ** r7093 -- THE ONE-CLOCK REFIT GRID, IN THE SHAPE `refit_grid185/` USES, so `70`'s own
#    `r7091_70_fit_rigidity/rigidity.py` reads it with no new instrument. **
#
#   `r7093` names the number the rebuild has to move: the coefficient c on the contrast template once
#   the five declared directions are fitted -- c = -0.0636 +- 0.0085 on the arm against -0.0075 +- 0.0083
#   on the control, i.e. ** the data ask THIS ARM's acoustic contrast to be 6.4 +- 0.9 per cent lower and
#   ask the control for nothing. **  That coefficient needs the four parameter gradients, so it needs a
#   GRID and not a spectrum.
#
# ⛭ ** ONLY THE ARM IS REBUILT: NINE RUNS, NOT EIGHTEEN. **  `LEAFGEOM` is a provable no-op on the
#   control -- `Hleaf` and `Hphys` are character-identical when radiation is in the rate -- and that was
#   verified BIT-IDENTICAL on the reporting path at `r7091+cc66.73`, not argued.  *So the control's nine
#   banked spectra are the control's one-clock spectra, and copying them is exact rather than approximate.*
#   ⌗ The copy is made here so one directory holds a complete pair of arms, which is what `build(arm)` wants.
#
# ⚠ ** AND THE CONFIGURATION IS RECORDED IN THE BANK ITSELF, which is what `r7093` asked for ** -- `70` is
#   auditing which published figure came from which configuration precisely because the existing banks do
#   not all say.  Every output carries `switches` (the instrument's own `__SWITCHES__` marker line, which is
#   read off its source and cannot drift from it) and `oneclock` (the `__ONECLOCK__` gate line).
#
# ** IDEMPOTENT AND RESUMABLE ** on the output's existence, so a container reclaim costs at most the
#   in-flight batch.  KFAC stays at the corpus default 2.0.  NK is not reduced.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/grid_oneclock; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

run () {
  tag=$1; shift
  if [ -s "$D/$tag.npz" ]; then echo "  skip $tag (done)"; return 0; fi
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 LEAFGEOM=1 SAVE=$D/$tag.npz \
    python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  rc=$?
  # ⌗ stamp the configuration INTO the bank, from the run's own markers rather than from this script
  python3 - "$D/$tag.npz" "$D/$tag.log" <<'PY'
import sys, numpy as np, os, re
npz, log = sys.argv[1], sys.argv[2]
if not os.path.exists(npz):
    raise SystemExit(0)
txt = open(log, encoding='utf-8', errors='replace').read()
sw = next((l.strip() for l in txt.split('\n') if l.startswith('__SWITCHES__')), '')
oc = next((l.strip() for l in txt.split('\n') if '__ONECLOCK__' in l), '')
z = dict(np.load(npz))
z['switches'] = np.array(sw); z['oneclock'] = np.array(oc)
np.savez(npz, **z)
PY
  echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
}
export -f run; export D

# the arm's nine, at `refit_grid185/launch.sh`'s own parameters and steps, plus LEAFGEOM=1
CR="ARM=cr CROM=0.2973 ZSTART=3e7 LEAFSCALES=1"
JOBS=(
 "cr_base      $CR CRH0=68.60"
 "cr_H0p       $CR CRH0=70.60"
 "cr_H0m       $CR CRH0=66.60"
 "cr_OMp       ARM=cr CRH0=68.60 CROM=0.3123 ZSTART=3e7 LEAFSCALES=1"
 "cr_OMm       ARM=cr CRH0=68.60 CROM=0.2823 ZSTART=3e7 LEAFSCALES=1"
 "cr_WBp       $CR CRH0=68.60 WBH2=0.0232"
 "cr_WBm       $CR CRH0=68.60 WBH2=0.0216"
 "cr_NSp       $CR CRH0=68.60 NS=0.985"
 "cr_NSm       $CR CRH0=68.60 NS=0.945"
)
echo "resume at $(date -u): $(ls $D/cr_*.npz 2>/dev/null | wc -l)/9 arm runs already done"
printf '%s\n' "${JOBS[@]}" | xargs -P 4 -I{} bash -c 'run {}'

# the control's nine, copied exactly -- LEAFGEOM is bit-identical there
for t in base H0p H0m OMp OMm WBp WBm NSp NSm; do
  [ -s "$D/lcdm_$t.npz" ] || cp refit_grid185/lcdm_$t.npz "$D/lcdm_$t.npz"
done
echo "=== GRID: $(ls $D/cr_*.npz 2>/dev/null | wc -l)/9 arm, $(ls $D/lcdm_*.npz 2>/dev/null | wc -l)/9 control, at $(date -u) ==="
