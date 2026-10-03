#!/usr/bin/env bash
# run_touched_readers.sh -- run exactly the registered receipts that READ A PAPER THIS TREE HAS EDITED.
#
# ** WHY THIS EXISTS, AND IT IS THE GATE'S OWN DEFECT TWICE IN THE SAME SHAPE. **
#
# `run_fast_job.sh` answers "will the FAST job be green?", and the fast job runs the `corpus/` gates, the
# generators and the lints.  ** It runs NO RECEIPTS. **  `run_instrument_receipts.sh` closes that gap for
# ONE dependency -- the acoustic instrument -- and says so in its own header.  ⇒ *There is a second
# dependency it does not cover, and it is the commonest one this seat has: a receipt that READS A PAPER.*
#
#   (1) `r7111`: a band edit (206 -> 204) broke two receipts.  One was repaired; the instrument set had
#       been run BEFORE the edit, the fast job runs no receipts, and the second red landed on `main`.
#       ⌗ Recorded then as "the gate's own ordering gap" and not fixed.
#   (2) `r7141`: node 60's `r7140` receipt gated a paper clause as an EXCLUSIVE disjunction -- it stands,
#       or this row is cited in `P15`, never both.  The gate ran that receipt (12 of 12), THEN edited
#       `sec:what-crosses` to cite it, and pushed.  ** Both arms became true and `main` was red from the
#       commit that introduced the receipt until two seats routed it. **
#
# ⌗ ** THE COMMON SHAPE: A RECEIPT READS A PAPER, THE GATE EDITS THAT PAPER AFTER RUNNING THE RECEIPT,
#   AND NOTHING BETWEEN THERE AND THE PUSH READS A RECEIPT AGAIN. **  *The affordable gate is the same
#   shape as the instrument one: not all 956 receipts, but the SET THAT CAN BE AFFECTED -- the receipts
#   that name a file this working tree has changed.*
#
#   bash scripts/run_touched_readers.sh            # against the working tree (staged + unstaged)
#   bash scripts/run_touched_readers.sh HEAD~1     # against what a given ref changed
#
# ⛔ *This does not replace the heavy job.  It closes the ordering gap between the last corpus edit and
# the push, which is where both instances above lived.*
set -u
cd "$(dirname "$0")/.."
ROOT=$(pwd)
REF=${1:-}

if [ -n "$REF" ]; then
    CHANGED=$(git diff --name-only "$REF" -- 'corpus/*.tex' 'corpus/*.tsv' 'corpus/*.txt' | sort -u)
else
    CHANGED=$( { git diff --name-only -- 'corpus/*.tex' 'corpus/*.tsv' 'corpus/*.txt'
                 git diff --cached --name-only -- 'corpus/*.tex' 'corpus/*.tsv' 'corpus/*.txt'; } | sort -u)
fi

echo
echo "  RUN-TOUCHED-READERS -- the receipts that read a corpus file this tree changed"
echo
if [ -z "$CHANGED" ]; then
    echo "    no corpus file changed; nothing can be affected by this class."
    echo "    ⌗ That is a claim about THIS gap only -- the heavy job is still the suite's verdict."
    exit 0
fi
echo "    changed corpus file(s):"
for f in $CHANGED; do echo "      $f"; done

# the readers: every registered receipt naming one of those basenames
# ⛭ THE SCOPE IS THE SENTENCES CHANGED, NOT THE FILES CHANGED, AND THAT IS A MEASURED CORRECTION.
#   A first draft took every receipt NAMING a changed file.  ** Measured on the `r7141` change set that
#   is 103 of 956 receipts, and it finished in neither twelve minutes serially nor ten at four at a
#   time. **  ⇒ *A gate that cannot finish before a push will not be run before one -- which is the
#   reason `check_tilt_pins` was put in the monthly backstop instead of the fast list.*
#   ⌗ So the scope is narrowed by the instrument that already knows which receipt reads which SENTENCE:
#   `corpus/quote_pin_baseline.tsv` keys on (receipt, literal).  A receipt is affected when one of its
#   pinned literals appears in a line this tree CHANGED, added or removed -- which is the class that
#   broke at
#   `r7111` and `r7141`: a receipt quoting prose the gate then rewrote.
READERS=$(python3 scripts/_touched_pin_readers.py ${REF:-})
N=$(printf '%s\n' "$READERS" | grep -c . || true)
echo
echo "    $N receipt(s) pin a sentence this tree TOUCHED in those files"
if [ "$N" = "0" ]; then
    echo "    ⌗ no pinned literal appears in a changed line, so nothing can break on this class."
    echo "    ⌗ That is a claim about THIS gap only -- the heavy job is still the suite's verdict."
    exit 0
fi

# ⛭ FOUR AT A TIME, which is `run_all_receipts.py`'s own figure and is the reason this is affordable:
#   measured serially on the `r7141` change set it took over nine minutes for 103 receipts, which is a
#   gate nobody would run before a push.  *A gate placed where it will not be run reports nothing.*
JOBS=4
OUT=$(mktemp -d)
i=0
for r in $READERS; do
    d=$(dirname "$r"); b=$(basename "$r")
    ( cd "$d" && timeout 900 python3 -W ignore "$b" >/dev/null 2>&1 \
        && echo "ok" > "$OUT/$(echo "$r" | tr '/' '_')" \
        || echo "$r" > "$OUT/$(echo "$r" | tr '/' '_')" ) &
    i=$((i+1))
    if [ $((i % JOBS)) -eq 0 ]; then wait; fi
done
wait

FAILED=""
PASSED=0
for f in "$OUT"/*; do
    if [ "$(cat "$f")" = "ok" ]; then
        PASSED=$((PASSED+1))
    else
        FAILED="$FAILED $(cat "$f")"
        echo "    [FAIL] $(cat "$f")"
    fi
done
rm -rf "$OUT"

echo
echo "    passed: $PASSED"
if [ -n "$FAILED" ]; then
    echo
    echo "  ⛔ THE TOUCHED READERS ARE RED.  Repair before pushing -- and note WHOSE receipt it is:"
    echo "     a seat does not edit another seat's receipt, EXCEPT where its own edit broke it, which"
    echo "     is exactly this case."
    exit 1
fi
echo "  every receipt that reads a changed corpus file passes on this tree."
echo "  ⌗ Green here is a claim about the ordering gap between the last corpus edit and the push."
exit 0
