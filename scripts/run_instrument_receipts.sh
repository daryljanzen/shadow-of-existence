#!/usr/bin/env bash
# run_instrument_receipts.sh -- run exactly the registered receipts that READ THE ACOUSTIC INSTRUMENT.
#
# ** WHY THIS EXISTS, AND IT IS THE GATE'S OWN DEFECT THREE TIMES IN ONE ROUND. **
#
# `run_fast_job.sh` answers one question honestly -- "will the FAST job be green?" -- and the fast job
# runs the `corpus/` gates, ten generators and two lints.  ** It runs NO RECEIPTS. **  CI has a separate
# `heavy` job for those (`run_all_receipts.py`), and the gate was pushing on the strength of the fast
# job alone.  ⇒ At `r7097`/`r7099` three separate reds reached CI through that gap, all of one kind:
#
#   (1) `LEAFREC` became the first clock switch in `ACOUSTIC_two_arm.py` whose default is ON, so three
#       receipts that run the instrument FRESH compared a new clock against numbers measured before the
#       split.  The delivering seat found them with a scoped run and said in terms that the fast job
#       could not see a red of this kind.
#   (2) A load-bearing helper (`r7091_directions/shape.py`) carried an ABSOLUTE PATH into one
#       container's home directory, so the decisive Q3 receipt passed where it was written and raised
#       everywhere else -- including here and including CI.
#   (3) A gate the chat seat re-pointed at `r7095` asserted a state that the SAME revision commissioned
#       the fix for, and went red one round later on the tree that satisfies it.
#
# ⌗ ** THE COMMON SHAPE: THE INSTRUMENT MOVES AND ITS READERS HAVE TO FOLLOW, and no gate in the fast
#   job reads the instrument at all. **  *Running all 934 registered receipts before every push is not
#   affordable -- two of them take six and eight minutes each -- so the affordable gate is the SET THAT
#   CAN BE AFFECTED, which is the set that reads the instrument.*
#
# ⛔ ** AND THE SET IS DERIVED, NEVER LISTED. **  `run_fast_job.sh`'s own header records why: a copy of a
#   list is a claim about the list at the moment it was copied, and that claim went stale twice.  So this
#   script greps the tree for the instrument's own names and runs whatever it finds.  A receipt that
#   starts reading the instrument tomorrow is picked up tomorrow, by nobody.
#
# ⌗ ** WHAT IT DOES NOT COVER IS NAMED IN ITS OWN OUTPUT, because a coverage claim that overstates
#   itself is worse than none. **  *Two exclusions, both deliberate and both printed every run:*
#     - ** the DECLARED-LONG receipts ** (`--quick`), which carry their own measured cost in their source
#       and run for tens of minutes each.  *One of them alone exceeds the whole wall this script gives
#       the set, so including it by default would mean the run never completes and the gate is ignored.*
#       `--all` includes them; CI's heavy job runs them regardless.
#     - ** `P16_the_window_is_crossed_twice...` **, which imports `pynucastro`.  *That is in
#       `requirements-ci.txt` and installed in CI, not here; its red is an environment gap and not a
#       finding, and leaving it in would train the reader to ignore a red.*
#
# Usage:  bash scripts/run_instrument_receipts.sh [--all] [extra args for run_all_receipts.py]
# Exit 0 if every affected receipt passes, 1 otherwise.
set -uo pipefail
cd "$(dirname "$0")/.."

SEL='ACOUSTIC_two_arm|refit_grid185|r7091_directions|beyond_the_wall/spectra|planck_tt_likelihood'
LIST="$(mktemp)"
trap 'rm -f "$LIST"' EXIT

SKIPLONG=1
if [ "${1:-}" = "--all" ]; then SKIPLONG=0; shift; fi

grep -rlE "$SEL" receipts/*/*.py 2>/dev/null | sort > "$LIST"
N=$(wc -l < "$LIST" | tr -d ' ')
# the CI-only dependency, excluded by name with the reason in the header above
grep -v 'P16_the_window_is_crossed_twice' "$LIST" > "$LIST.f" && mv "$LIST.f" "$LIST"
# ⌗ ** THE DECLARED-LONG SET IS READ OUT OF `run_all_receipts.py`'s OWN `LONG` TABLE, not listed here
#   and not taken from `--quick`. **  *`--quick` filters a different set (`SLOW`) and leaves the longest
#   receipts in, so the first writing of this script printed that they were excluded while they ran --
#   a coverage claim that overstated itself, which is the one thing this file's header says not to do.*
if [ "$SKIPLONG" = "1" ]; then
  python3 - "$LIST" <<'PY'
import io, re, sys
src = io.open('scripts/run_all_receipts.py', encoding='utf-8').read()
blk = src[src.index('LONG = {'):]
blk = blk[:blk.index('\n}')]
names = set(re.findall(r"'([A-Za-z0-9_]+\.py)'\s*:", blk)) | set(
    re.findall(r'"([A-Za-z0-9_]+\.py)"\s*:', blk))
keep = [l for l in io.open(sys.argv[1], encoding='utf-8').read().splitlines()
        if l.strip() and l.rsplit('/', 1)[-1] not in names]
io.open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(keep) + '\n')
print(f"    {len(names)} receipt(s) declare a long runtime in run_all_receipts.py's LONG table")
PY
fi
M=$(wc -l < "$LIST" | tr -d ' ')

echo
echo "  RUN-INSTRUMENT-RECEIPTS -- the set is DERIVED from the tree, never listed"
echo "    selector: $SEL"
echo "    $N registered receipt(s) read the acoustic instrument or its banked inputs"
echo "    $((N - M)) excluded for a CI-only dependency (pynucastro), named in this file's header"
[ "$SKIPLONG" = "1" ] && echo "    and those are excluded here too (--all includes them); CI's heavy job runs them regardless"
echo "    ⌗ this is the set a change to ACOUSTIC_two_arm.py can break, and the fast job reads none of it"
echo

if [ "$M" = "0" ]; then
  echo "  ⛔ the selector matched nothing, which means the selector is wrong rather than the tree clean."
  exit 2
fi

python3 scripts/run_all_receipts.py --from "$LIST" --jobs 4 --timeout 900 "$@"
RC=$?

echo
if [ "$RC" = "0" ]; then
  echo "  every receipt that reads the instrument passes on this tree."
  echo "  ⌗ Green here is NOT green on the heavy job: this is the affected set minus the exclusions above."
else
  echo "  ⛔ at least one receipt that reads the instrument is red -- see above."
  echo "  ⌗ This is the class that reached CI three times at r7097/r7099 through the fast job's blind spot."
fi
exit $RC
