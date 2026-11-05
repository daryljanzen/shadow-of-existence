#!/bin/bash
# r7682 (60) -- THE A/B DISTRIBUTION, the one registered arm.
#
# `N` trials of the receipt UNSEEDED, then `N` SEEDED, SEQUENTIAL, one process at a time, cores
# otherwise idle, the scoped suite's own child environment (`run_all_receipts.run_one`'s
# `_ONE_THREAD` plus `PYTHONUNBUFFERED=1`, with `NODE` UNSET), and the same 900 s cap on each --
# the budget the receipt crossed on the runner.  Each trial's exit code and wall are APPENDED as it
# completes, so a trial killed at the cap is recorded and not lost with the harness.
#
# ⌗ THE SEEDED ARM IS THE RECEIPT AS IT NOW STANDS.  The unseeded arm is built by STRIPPING the
#   r7682 block out of it, into a sibling file, because the receipt resolves the corpus root from
#   its own `__file__` three directories up and cannot be run from anywhere else.  The sibling is
#   removed again at the end: an unregistered `.py` under `receipts/` is itself a gate red.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../../.." && pwd)
D=$ROOT/receipts/P15_CR_cosmology
R=P15_the_four_dimensional_treatment_keeps_the_economy_and_keeps_more_of_it_but_in_the_sphere_label_so_the_bridge_exists_only_on_the_squashing_free_sector.py
U=_r7682_unseeded.py
N=${N:-30}
OUT=${OUT:-$HERE/runs/ab.txt}

# the unseeded arm: the receipt with the r7682 import, comment block and seed call removed
python3 - "$D/$R" "$D/$U" <<'PY'
import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
out = re.sub(r'import sympy\.core\.random as _sprandom\n\n(?:#.*\n)+_sprandom\.seed\(\d+\)\n', '', src)
assert out != src and '_sprandom' not in out, 'the r7682 block did not strip cleanly'
open(sys.argv[2], 'w', encoding='utf-8').write(out)
PY
trap 'rm -f "$D/$U"' EXIT

cd "$D"
: > "$OUT"
for arm in UNSEEDED SEEDED; do
  [ "$arm" = UNSEEDED ] && F=$U || F=$R
  for i in $(seq 1 "$N"); do
    t0=$(date +%s)
    env -u NODE OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
        VECLIB_MAXIMUM_THREADS=1 PYTHONUNBUFFERED=1 timeout 900 python3 "$F" >/dev/null 2>&1
    rc=$?; echo "$arm $i rc=$rc wall=$(( $(date +%s) - t0 ))" >> "$OUT"
  done
done
