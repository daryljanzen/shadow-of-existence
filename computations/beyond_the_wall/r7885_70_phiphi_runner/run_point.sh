#!/bin/bash
# r7885+70: run ONE point of 60's lensing grid on a GitHub runner, through 60's generator UNCHANGED.
#
#   run_point.sh <arm> <tag> <outdir>
#
# ⚑ NOT A RETYPE OF THE GENERATOR.  `gen_phiphi_nuhier.sh` (r7884, 60's) has no single-point switch, and it
#   is idempotent: a point whose `<arm>_<tag>.json` exists and is non-empty is skipped.  So every OTHER point
#   of its list is seeded with a placeholder, the generator runs at JOBS=1 and finds exactly one point
#   outstanding, and the placeholders are removed before anything is gated or banked.  The command, the
#   switches and the point list are the generator's own, byte for byte.
# ⛔ The placeholder is the literal `{"placeholder": true}`, so a reader that ever met one would refuse it
#   (no `bandpowers`), and `gate.py` refuses any record carrying the key.
set -euo pipefail
arm=$1; tag=$2; out=$3
HERE="$(cd "$(dirname "$0")" && pwd)"
GEN="$HERE/../r7884_60_the_controls_limits_on_the_jointly_validated_sector/gen_phiphi_nuhier.sh"
mkdir -p "$out"
seeded=()
while read -r a t; do
  [ "$a" = "$arm" ] && [ "$t" = "$tag" ] && continue
  printf '{"placeholder": true}\n' > "$out/${a}_${t}.json"; seeded+=("$out/${a}_${t}.json")
done < <(python3 "$HERE/gate.py" --list)
echo "  seeded ${#seeded[@]} placeholder(s); running $arm $tag alone"
t0=$(date +%s)
PPOUT="$out" JOBS=1 bash "$GEN"
t1=$(date +%s)
rm -f "${seeded[@]}"
python3 - "$out" "$arm" "$tag" "$t0" "$t1" <<'PY'
import json, os, sys, platform
out, arm, tag, t0, t1 = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
rec = dict(arm=arm, tag=tag, wall_s=t1 - t0, nproc=os.cpu_count(), machine=platform.machine(),
           runner=os.environ.get('RUNNER_NAME'), run_id=os.environ.get('GITHUB_RUN_ID'),
           sha=os.environ.get('GITHUB_SHA'))
json.dump(rec, open(os.path.join(out, f'{arm}_{tag}.timing.json'), 'w'), indent=1, sort_keys=True)
print(f'  {arm} {tag}: wall {t1 - t0} s on {os.cpu_count()} cores')
PY
