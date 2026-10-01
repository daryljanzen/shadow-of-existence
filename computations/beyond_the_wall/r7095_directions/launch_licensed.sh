#!/bin/bash
# ** r7095 Q3 -- THE LICENSED RUN: THE RULE'S OWN CONFIGURATION, WITH THE ONSET DISSOLVED. **
#
#   `r7095` adjudicated against `LEAFGEOM=1`: `P07`'s rate rule gives each quantity its own rate
#   EVERYWHERE -- "there is no locus at which the rate switches" -- and reading a STACKING quantity on
#   the leaf's is forbidden by name, with `D_M` named as stacking.  ** So two rates in one integral is
#   what the rule REQUIRES, and what one integral needs is one VARIABLE, not one rate. **
#
# ⛭ ** THE CONFIGURATION, AND IT IS REACHABLE FOR THE FIRST TIME AT THIS REVISION: **
#     LEAFGEOM=0   the geometry -- eta, chi, D_M and the kernel's x0 -- on the STACKING rate, the rule's
#     LEAFSCALES=1 r_s and r_D on the LEAF, the plasma's own
#     LEAFREC=1    recombination on the LEAF (the default since r7095+cc66.75, and the switch that
#                  made this configuration expressible: `LEAFGEOM` alone could not hold D_M on the
#                  stack AND recombination on the leaf)
#     VISLEAF=0    ⚠ the visibility's clock is NOT adjudicated and `r7095` holds it against `60` as
#                  much as against this seat.  *Run at the REPORTED configuration so the comparison is
#                  against the published baseline and the visibility question stays separable.*
#   ⌗ *And the Jacobian conversion `r7095`'s Q1 asks for is ALREADY in the instrument, measured at
#   `r7095+cc66.75` rather than assumed: `sound_phase` over the stacking variable equals the leaf r_s
#   increment to 9.8e-9 while the stacking value is 43 per cent away.  **It is not built again, because
#   that would apply the same correction twice -- the `GSRC`+`LEAFPERT` defect of r3737.**
#
# ⛭⛭ ** THE ONSET IS GONE RATHER THAN HELD, which is the other half of what makes this run new. **
#   `60` ruled it dissolved: the stacking ruler keeps a SQUARE-ROOT memory of its start (exponent
#   0.5008, 43.1 per cent of the integral still missing at z ~ 6.8e3) where the leaf ruler keeps a
#   LINEAR one (0.9983, 0.0064 per cent short at 3e7) -- ** a leaf-rate sound horizon has no lower
#   endpoint to place. **  ⇒ So the arm starts where the control starts, z = 3e7, and nothing is solved
#   anywhere: no `LATARG`, no `brentq`.  *That also removes the start-inside-the-horizon artefact --
#   k/(a H) = 1.53, 3.73, 5.67 at the old onset, all three outside at the control's start.*
#   ⇒ *** THE ACOUSTIC ANGLE IS THEREFORE AN OUTPUT AND THE COMB IS NOT PINNED TO ANYTHING. ***
#
# ⛭ ** NINE ARM RUNS, NOT EIGHTEEN, and the reason is checked rather than assumed. **  On the control
#   `Hleaf` and `Hphys` are character-identical, so `LEAFREC` is a provable no-op there and was verified
#   BIT-IDENTICAL; `LEAFGEOM=0` and `VISLEAF=0` are its defaults; and its start is already z = 3e7.
#   *So `refit_grid185/lcdm_*` IS the control at this configuration, exactly, and copying it is not an
#   approximation.*  Banked in that directory's shape so `70`'s `rigidity.py` reads it unchanged.
#
# ⚠ ** AND EVERY OUTPUT RECORDS ITS OWN SWITCHES **, because `70` reports that no banked spectrum does
#   and the census had to fingerprint configurations off `l_A` to answer what one saved dictionary
#   would have answered outright.  The stamp is read from each run's own `__SWITCHES__` marker, which
#   the instrument derives from its own source and cannot drift from.
#
# ** IDEMPOTENT AND RESUMABLE ** on each output's existence.  KFAC stays 2.0.  NK is not reduced.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/grid_licensed; mkdir -p $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1

run () {
  tag=$1; shift
  if [ -s "$D/$tag.npz" ]; then echo "  skip $tag (done)"; return 0; fi
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE=$D/$tag.npz \
    python3 -u ACOUSTIC_two_arm.py > $D/$tag.log 2>&1
  rc=$?
  python3 - "$D/$tag.npz" "$D/$tag.log" <<'PY'
import sys, numpy as np, os
npz, log = sys.argv[1], sys.argv[2]
if not os.path.exists(npz):
    raise SystemExit(0)
txt = open(log, encoding='utf-8', errors='replace').read()
sw = next((l.strip() for l in txt.split('\n') if l.startswith('__SWITCHES__')), '')
z = dict(np.load(npz)); z['switches'] = np.array(sw)
np.savez(npz, **z)
PY
  echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
}
export -f run; export D

# the arm, at refit_grid185's own parameters and steps, in the rule's configuration, onset dissolved
CR="ARM=cr CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"
JOBS=(
 "cr_base      $CR CRH0=68.60"
 "cr_H0p       $CR CRH0=70.60"
 "cr_H0m       $CR CRH0=66.60"
 "cr_OMp       ARM=cr CRH0=68.60 CROM=0.3123 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"
 "cr_OMm       ARM=cr CRH0=68.60 CROM=0.2823 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"
 "cr_WBp       $CR CRH0=68.60 WBH2=0.0232"
 "cr_WBm       $CR CRH0=68.60 WBH2=0.0216"
 "cr_NSp       $CR CRH0=68.60 NS=0.985"
 "cr_NSm       $CR CRH0=68.60 NS=0.945"
)
echo "resume at $(date -u): $(ls $D/cr_*.npz 2>/dev/null | wc -l)/9 arm runs already done"
printf '%s\n' "${JOBS[@]}" | xargs -P 4 -I{} bash -c 'run {}'

for t in base H0p H0m OMp OMm WBp WBm NSp NSm; do
  [ -s "$D/lcdm_$t.npz" ] || cp refit_grid185/lcdm_$t.npz "$D/lcdm_$t.npz"
done
echo "=== LICENSED GRID: $(ls $D/cr_*.npz 2>/dev/null | wc -l)/9 arm, $(ls $D/lcdm_*.npz 2>/dev/null | wc -l)/9 control, at $(date -u) ==="
