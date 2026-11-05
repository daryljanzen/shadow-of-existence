#!/bin/bash
# r7682 (60) -- ARM ②, THE VERDICT TEXT.  A dedicated pass that KEEPS stdout, which `ab.sh`
# discards by design so that nothing it writes competes with the trial it is timing.
#
# `N` trials each way, same protocol as `ab.sh`.  Each trial's output has its ONE wall-time line
# normalised to `[WALL]` and the rest digested, so the comparison is on the verdict text and
# nothing else -- and a SLOW trial is compared on exactly the same footing as a fast one, which is
# the reading that matters: an unlucky draw must not be allowed to move a printed figure.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../../.." && pwd)
D=$ROOT/receipts/P15_CR_cosmology
R=P15_the_four_dimensional_treatment_keeps_the_economy_and_keeps_more_of_it_but_in_the_sphere_label_so_the_bridge_exists_only_on_the_squashing_free_sector.py
U=_r7682_unseeded.py
N=${N:-10}
OUT=${OUT:-$HERE/runs/ident.txt}

python3 - "$D/$R" "$D/$U" <<'PY'
import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
out = re.sub(r'import sympy\.core\.random as _sprandom\n\n(?:#.*\n)+_sprandom\.seed\(\d+\)\n', '', src)
assert out != src and '_sprandom' not in out, 'the r7682 block did not strip cleanly'
open(sys.argv[2], 'w', encoding='utf-8').write(out)
PY
trap 'rm -f "$D/$U"' EXIT

cd "$D"
W=$(mktemp -d); : > "$OUT"
for arm in UNSEEDED SEEDED; do
  [ "$arm" = UNSEEDED ] && F=$U || F=$R
  for i in $(seq 1 "$N"); do
    t0=$(date +%s)
    env -u NODE OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
        VECLIB_MAXIMUM_THREADS=1 PYTHONUNBUFFERED=1 timeout 900 python3 "$F" > "$W/$arm.$i.out" 2>&1
    rc=$?
    d=$(sed -E 's/\[[0-9]+\.[0-9]+s\]/[WALL]/g' "$W/$arm.$i.out" | sha256sum | cut -c1-16)
    echo "$arm $i rc=$rc wall=$(( $(date +%s) - t0 )) lines=$(wc -l < "$W/$arm.$i.out") digest=$d" >> "$OUT"
  done
done
rm -rf "$W"
