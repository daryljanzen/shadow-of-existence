#!/bin/bash
# ** r7203+cc66 -- THE THREE RUNS 66 APPROVED, AND ONLY THOSE THREE. **
#
#   `r7201` granted ten.  Four landed, the cost test the order attached was tripped at 38% over
#   (the control arm solves 2547 modes against the CR arm's 1452, which is what the per-run time
#   tracks -- NOT the contention I first blamed), and the order's stop-and-say clause fired.
#   `r7203` approved option 2: `cr_rb1.5`, `cr_nodrive`, `lcdm_nodrive`.
#
# ⛔ ** THIS IS DELIBERATELY NOT `launch_ten.sh`. **  That launcher is idempotent and would skip the
#   four already banked -- but it would then run `lcdm_rb1.5`, `cr_rb2.0` and `lcdm_rb2.0`, which
#   `r7203` did NOT approve.  An idempotent launcher only protects against repeating work, never
#   against doing work nobody ordered.  So the ordered set is enumerated here explicitly.
#
# ⌗ Everything else is `launch_ten.sh`'s verbatim: each arm at its OWN banked base's configuration
#   (the control is `ARM=lcdm` and nothing else, per `r7109_directions/launch_control_base.sh`),
#   `KFAC` at the corpus default 2.0, `NK` not reduced, one thread each, serial so the per-run cost
#   is clean, resumable on output existence, and the configuration stamped into the bank from the
#   run's own `__SWITCHES__` line rather than from this script.
#
# ** COSTED AT 1.33h: ** cr_rb1.5 ~1266s + cr_nodrive ~1266s + lcdm_nodrive ~2242s = 4774s.
#   `r7203` says to stop and say so again if the three cost materially more than that.  The live
#   uncertainty is whether NODRIVE changes the mode count -- that is what set the CR/control split,
#   and it is not visible from the switch lines, which is exactly how the first cost went wrong.
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
  n=$(grep -oE 'modes = [0-9]+' "$D/$tag.log" | head -1)
  echo "  done $tag rc=$rc in $(( $(date +%s) - s ))s  [$n]  $(date -u +%H:%M:%S)"
}

# the one loading point that gives the curve a central difference about RBFAC=1
run cr_rb1.5 $CR RBFAC=1.5

# the driving pair -- the half no banked file can serve, and the whole reason ten was asked for
run cr_nodrive   $CR NODRIVE=1
run lcdm_nodrive $LC NODRIVE=1

echo "== LAUNCHER FINISHED: $(ls -1 "$D"/*.npz 2>/dev/null | wc -l) of 7 outputs present (4 banked + 3 ordered) =="
