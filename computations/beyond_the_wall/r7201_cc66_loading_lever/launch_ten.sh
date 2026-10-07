#!/bin/bash
# ** r7201+cc66 -- THE TEN RUNS 66 GRANTED: EIGHT `RBFAC` AND THE `NODRIVE` PAIR. **
#
#   `cc66.156` established the de-tilted peak set as a phase observable and asked for ten runs, not
#   the eight `cc66.155` costed, because the CR arm's banked driving-ON spectrum has no
#   integer-spaced peak series.  `r7201` granted all ten.
#
# ⚠ ** EACH ARM IS RUN AT ITS OWN BANKED BASE'S CONFIGURATION, NOT AT ONE COMMON LINE. **  The order
#   names `ZSTART=3e7`, and the CR grid carries it -- but the control's banked `lcdm_base.npz` is
#   `ARM=lcdm HIER=1 LSTEP=8 LMAXL=2000` and NOTHING else, documented verbatim at
#   `r7109_directions/launch_control_base.sh` ("ARM=lcdm and nothing else").  Adding `ZSTART` to the
#   control would make these runs incomparable with the base they are differenced against, which is
#   the whole point of them.  ** So each arm matches its own base; the divergence from the order's
#   wording is deliberate and is reported rather than taken. **
#
# ** IDEMPOTENT AND RESUMABLE ** on the output's existence, so a container reclaim costs at most the
#   in-flight run.  KFAC stays at the corpus default 2.0.  NK is not reduced.  One thread each, so
#   `--jobs` would mean cores; these run SERIALLY because the point is a clean per-run cost.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/home/user/shadow-of-existence/computations/beyond_the_wall/r7201_cc66_loading_lever
mkdir -p "$D"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1

CR="ARM=cr CRH0=68.60 CROM=0.2973 LEAFGEOM=1 LEAFSCALES=1 ZSTART=3e7"
LC="ARM=lcdm"

run () {
  tag=$1; shift
  if [ -s "$D/$tag.npz" ]; then echo "  skip $tag (done)"; return 0; fi
  s=$(date +%s)
  env "$@" HIER=1 LSTEP=8 LMAXL=2000 SAVE="$D/$tag.npz" \
    python3 -u ACOUSTIC_two_arm.py > "$D/$tag.log" 2>&1
  rc=$?
  # ⌗ stamp the configuration INTO the bank from the run's own marker line, never from this script
  python3 - "$D/$tag.npz" "$D/$tag.log" <<'PY'
import sys, os, numpy as np
npz, log = sys.argv[1], sys.argv[2]
if not os.path.exists(npz):
    raise SystemExit(0)
txt = open(log, encoding='utf-8', errors='replace').read()
sw = next((l.strip() for l in txt.split('\n') if l.startswith('__SWITCHES__')), '')
z = dict(np.load(npz))
z['switches'] = np.array(sw)
np.savez(npz, **z)
PY
  echo "  done $tag rc=$rc in $(( $(date +%s) - s ))s $(date -u +%H:%M:%S)"
}

# ---- the eight RBFAC runs: four values per arm, bracketing the banked default RBFAC=1.0 and
#      reaching the no-loading limit, which PO13 already has a g2/g1 gate at (1.065 vs 0.897).
for v in 0.0 0.5 1.5 2.0; do
  run "cr_rb${v}"   $CR RBFAC=$v
  run "lcdm_rb${v}" $LC RBFAC=$v
done

# ---- the NODRIVE pair, at the same per-arm base
run cr_nodrive   $CR NODRIVE=1
run lcdm_nodrive $LC NODRIVE=1

echo "== LAUNCHER FINISHED: $(ls -1 "$D"/*.npz 2>/dev/null | wc -l) of 10 outputs present =="
