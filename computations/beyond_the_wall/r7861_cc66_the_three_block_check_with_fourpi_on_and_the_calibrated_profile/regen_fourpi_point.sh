#!/bin/bash
# r7861+cc66 item ③: regenerate ONE point of the CMB bank -- the lcdm control at Sum = 0 -- with
# POLSAVE on, so the factor two can be checked against the bank's DEFINITION and not against a
# cache the repository does not hold.
#
# ⛔ WHY THIS EXISTS.  model3 reads the bank from POL_DIR, default /tmp/claude-0/pol_grid, which
# this container has lost.  ratio_grid3.npz beside it carries only sum-dependence RATIOS, so the
# absolute normalisation is not in the repository at all.  This re-runs the instrument for the one
# point item ① needs, with the switch values copied from 60's own gen_pol_batched.sh.
#
# ⌗ THE OUTPUT GOES IN THE REPOSITORY, NOT UNDER /tmp.  Three banks have now been lost to /tmp
# defaults on this line (r7847's 555-bin mask, r7851's Phi bandpowers, this grid).
# ⌗ IDEMPOTENT: a completed point is skipped, so a restart re-runs only what is missing.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${OUT:-$HERE/bank_fourpi}"
SOLVER="$(cd "$HERE/.." && pwd)"
mkdir -p "$OUT"

POL="$OUT/lcdm_S000.npz"
if [ -s "$POL" ]; then echo "  [have] lcdm S000 -- $(du -h "$POL" | cut -f1)"; exit 0; fi

cd "$SOLVER"
echo "  running the lcdm control at Sum = 0, POLSAVE on, into $OUT"
env ARM=lcdm LH0=67.40 LOM=0.3150 WBH2=0.0224 NS=0.965 MNU=0.00 \
    HIER=1 LMAXL=2000 LSTEP=8 FOURPI=1 \
    SAVE="$OUT/lcdm_S000_tt.npz" POLSAVE="$POL" \
    python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_S000.log" 2>&1
rc=$?
echo "  rc=$rc"
[ -s "$POL" ] && echo "  wrote $(basename "$POL") -- $(du -h "$POL" | cut -f1)" || echo "  ⛔ NO OUTPUT"
tail -3 "$OUT/lcdm_S000.log" 2>/dev/null
exit $rc
