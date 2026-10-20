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
#   bash scripts/run_touched_readers.sh                  # against the working tree (staged + unstaged)
#   bash scripts/run_touched_readers.sh HEAD~1           # against what a given ref changed
#   bash scripts/run_touched_readers.sh 'abc123^..abc123'  # against exactly what ONE commit changed
#
# ⛭ `r7453` ④ ADDED A SECOND CLASS, AND ITS OWN HEADER IS BELOW AT `CLASS TWO`: the GATES that read a
#   DATA FILE this tree changed, derived by `grep` and not from any list in this script.  The verdict
#   is the conjunction of the two classes; each class names what it excluded and why.
#
# ⛔ *This does not replace the heavy job.  It closes the ordering gap between the last corpus edit and
# the push, which is where both instances above lived.*
set -u
cd "$(dirname "$0")/.."
ROOT=$(pwd)
REF=${1:-}

# ===== CLASS ONE: receipts that pin a sentence in a touched corpus file =====
class_one() {

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
    return 0
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
    return 0
fi

# ⛭ FOUR AT A TIME, which is `run_all_receipts.py`'s own figure and is the reason this is affordable:
#   measured serially on the `r7141` change set it took over nine minutes for 103 receipts, which is a
#   gate nobody would run before a push.  *A gate placed where it will not be run reports nothing.*
JOBS=4
OUT=$(mktemp -d)
i=0
# ⛭⛭ EACH RECEIPT'S OWN DECLARED BUDGET, AND A TIMEOUT IS REPORTED AS A TIMEOUT.
#   ** This gate hardcoded `timeout 900` and reported a kill as `[FAIL]`. **  `r7155` hit it: a corpus
#   edit pulled `P15_the_one_fitted_number_moves_the_scale_and_not_the_peak.py` into scope, which
#   `run_all_receipts.py`'s `LONG` table declares at `1500`s on measurement -- so the gate killed it at
#   `900` and called the kill a red.  ⇒ *An instrument that reports a red which is not one is the defect
#   this whole arc is about, and a gate nobody believes is a gate nobody runs.*
#   ⌈ `run_instrument_receipts.sh` already solved this by EXCLUDING the declared-long set.  Excluding is
#   wrong here: the affected set is the point of this gate, so the budget is READ instead and the outcome
#   named.  *A timeout is counted apart and does not fail the gate, because a receipt that did not finish
#   has not contradicted anything -- and the heavy job runs it on its own budget.*
BUDGETS=$(python3 - <<'PY'
import io, re
s = io.open('scripts/run_all_receipts.py', encoding='utf-8').read()
i = s.find('LONG = {'); j = s.find('\n}', i)
for m in re.finditer(r"^\s*'([^']+)':\s*(\d+)", s[i:j], re.M):
    print(m.group(1), m.group(2))
PY
)
budget_for() {
    local b="$1" line
    line=$(printf '%s\n' "$BUDGETS" | awk -v f="$b" '$1 == f {print $2; exit}')
    if [ -n "$line" ]; then echo "$line"; else echo 900; fi
}

for r in $READERS; do
    d=$(dirname "$r"); b=$(basename "$r")
    t=$(budget_for "$b")
    ( cd "$d" && timeout "$t" python3 -W ignore "$b" >/dev/null 2>&1
      rc=$?
      if [ "$rc" = "0" ]; then echo "ok" > "$OUT/$(echo "$r" | tr '/' '_')"
      elif [ "$rc" = "124" ]; then echo "TIMEOUT ${t}s $r" > "$OUT/$(echo "$r" | tr '/' '_')"
      else echo "$r" > "$OUT/$(echo "$r" | tr '/' '_')"; fi ) &
    i=$((i+1))
    if [ $((i % JOBS)) -eq 0 ]; then wait; fi
done
wait

FAILED=""
PASSED=0
TIMEDOUT=0
for f in "$OUT"/*; do
    v=$(cat "$f")
    case "$v" in
        ok) PASSED=$((PASSED+1)) ;;
        TIMEOUT*) TIMEDOUT=$((TIMEDOUT+1)); echo "    [over its declared budget, counted apart] $v" ;;
        *) FAILED="$FAILED $v"; echo "    [FAIL] $v" ;;
    esac
done
rm -rf "$OUT"

echo
echo "    passed: $PASSED"
if [ "$TIMEDOUT" != "0" ]; then
    echo "    over budget: $TIMEDOUT   ⌈ not a red: a receipt that did not finish has contradicted nothing,"
    echo "                         and the heavy job runs it on its own budget."
fi
if [ -n "$FAILED" ]; then
    echo
    echo "  ⛔ THE TOUCHED READERS ARE RED.  Repair before pushing -- and note WHOSE receipt it is:"
    echo "     a seat does not edit another seat's receipt, EXCEPT where its own edit broke it, which"
    echo "     is exactly this case."
    return 1
fi
echo "  every receipt that reads a changed corpus file passes on this tree."
echo "  ⌗ Green here is a claim about the ordering gap between the last corpus edit and the push."
return 0
}

# ===== CLASS TWO: the GATES that READ a data file this tree changed  (r7453 ④) =====
#
# ** WHY THIS EXISTS, AND IT IS THIS SEAT'S OWN DEFECT THREE TIMES IN THREE PUSHES. **
#
# Class one asks "which RECEIPT pins prose I rewrote?".  There is a second reader class and it is the
# one that broke: *a GATE that reads a DATA FILE I edited.*  `r7441+cc66.92` removed two rows from
# `corpus/quote_pin_baseline.tsv`; `corpus/paper_pins_absent.tsv` separately LISTED one of those rows
# as a deliberate absence, so `check_paper_pins_present` went red on `main`.  ⌗ Eight `corpus/check_*`
# gates read that baseline.  **The seat had validated three — from memory — and the five it missed
# included the one that broke.**
#
# ⇒ `r7453` ④: *"a remedy that depends on remembering to apply it is not a remedy; it is the same
# error with a note attached."*  So the reader set is DERIVED HERE, every run, by `grep` over the gate
# sources -- ** there is no list of readers in this script **, for `turn_gates.sh`'s own reason:
# *** a copy of a list is a claim about the list at the moment it was copied. ***  A gate that starts
# reading a data file joins this class the day it lands, with nobody editing anything.
#
# ** EXCLUSIONS ARE NAMED WITH A REASON AND PRINTED EVERY RUN ** (the `turn_gates.sh` convention: an
# exclusion is a question not asked, never a question answered).  Two kinds occur here:
#   (a) NOT A GATE -- the grep also returns generators and instruments (`gen_pin_board.py` WRITES the
#       file; `_touched_pin_readers.py`, `double_read_agreement.py`, `regen_frontier.py` read it and
#       assert nothing).  Running them proves nothing, so they are named and not run.
#   (b) MEASURED COST -- `check_quote_pins` is 947 s measured (`r7343`), which `turn_gates.sh` already
#       excludes for the same reason: *a gate that cannot finish before a push will not be run before
#       one, and a gate placed where it will not be run reports nothing.*  `sweep_gates.sh` asks it
#       when the ledger moves, and the PR's CI run asks it on every push.
export NODE="${NODE:-ci}"
GATE_TIMEOUT="${GATE_TIMEOUT:-280}"

# name:reason -- a cost exclusion is printed, so it cannot be silent.
COST_EXCLUDE="check_quote_pins"
cost_reason_for() {
    case "$1" in
        check_quote_pins) echo "947s measured (r7343); turn_gates.sh excludes it for the same reason, sweep_gates.sh asks it when the LEDGER moves, and CI asks it on every push" ;;
        *)                echo "no reason recorded -- THIS IS A DEFECT, add one" ;;
    esac
}
notgate_reason_for() {
    case "$1" in
        scripts/gen_pin_board.py)          echo "generator: it WRITES this file rather than asserting about it" ;;
        scripts/_touched_pin_readers.py)   echo "instrument: class one's own derivation, asserts nothing" ;;
        scripts/double_read_agreement.py)  echo "instrument: reports agreement, asserts nothing" ;;
        scripts/regen_frontier.py)         echo "generator: regenerates THE_FRONTIER, asserts nothing" ;;
        *)                                 echo "not a corpus/check_* gate: reads the file but asserts nothing (name it here with its own reason if that is wrong)" ;;
    esac
}

class_two() {
    local changed f base hits g gates notgates excl rc t0 secs failed timedout passed

    if [ -n "$REF" ]; then
        changed=$(git diff --name-only "$REF" -- '*.tsv' '*.json' '*.csv' '*.txt' | sort -u)
    else
        changed=$( { git diff --name-only -- '*.tsv' '*.json' '*.csv' '*.txt'
                     git diff --cached --name-only -- '*.tsv' '*.json' '*.csv' '*.txt'; } | sort -u)
    fi

    echo
    echo "  CLASS TWO -- the gates that READ a data file this tree changed"
    echo
    if [ -z "$changed" ]; then
        echo "    no data file changed; nothing can be affected by this class."
        echo "    ⌗ That is a claim about THIS class only -- the PR's CI run is the whole-job gate."
        return 0
    fi
    echo "    changed data file(s):"
    for f in $changed; do echo "      $f"; done

    gates=""; notgates=""
    for f in $changed; do
        base=$(basename "$f"); base=${base%.*}
        hits=$(grep -lF "$base" corpus/check_*.py scripts/*.py 2>/dev/null | sort -u)
        for g in $hits; do
            case "$g" in
                corpus/check_*.py) gates="$gates $g" ;;
                *)                 notgates="$notgates $g" ;;
            esac
        done
    done
    gates=$(printf '%s\n' $gates | sort -u); notgates=$(printf '%s\n' $notgates | sort -u)

    echo
    echo "    the grep over 'corpus/check_*.py scripts/*.py' returns:"
    for g in $notgates; do echo "      [not a gate, named not run] $g -- $(notgate_reason_for "$g")"; done

    passed=0; failed=""; timedout=0; excl=""
    for g in $gates; do
        base=$(basename "$g" .py)
        case " $COST_EXCLUDE " in
            *" $base "*) excl="$excl $base"; echo "      [excluded, measured cost] $base -- $(cost_reason_for "$base")"; continue ;;
        esac
        t0=$(date +%s)
        ( cd "$(dirname "$g")" && timeout "$GATE_TIMEOUT" python3 -W ignore "$(basename "$g")" >/dev/null 2>&1 )
        rc=$?
        secs=$(( $(date +%s) - t0 ))
        if [ "$rc" = "0" ]; then
            passed=$((passed+1)); echo "      [ok   ${secs}s] $g"
        elif [ "$rc" = "124" ]; then
            timedout=$((timedout+1)); echo "      [over the ${GATE_TIMEOUT}s budget, counted apart] $g -- not a red: a gate that did not finish has contradicted nothing, and CI runs it on its own budget"
        else
            failed="$failed $g"; echo "      [FAIL ${secs}s rc=$rc] $g"
        fi
    done

    echo
    echo "    ran: $passed   failed: $(printf '%s\n' $failed | grep -c . || true)   over budget: $timedout"
    [ -n "$excl" ] && echo "    excluded by measured cost (named above):$excl"
    if [ -n "$failed" ]; then
        echo
        echo "  ⛔ A GATE THAT READS A DATA FILE THIS TREE CHANGED IS RED.  Repair before pushing:"
        echo "     this class exists because that red reached \`main\` three times in three pushes."
        return 1
    fi
    echo "  every gate that reads a changed data file passes on this tree."
    echo "  ⌗ Green here is a claim about THIS class -- the PR's CI run is the whole-job gate."
    return 0
}

# ===== THE TWO CLASSES, AND THE VERDICT IS THE CONJUNCTION =====
class_one; RC1=$?
class_two; RC2=$?
echo
if [ "$RC1" = "0" ] && [ "$RC2" = "0" ]; then
    echo "  BOTH CLASSES GREEN: no receipt that pins touched prose and no gate that reads a touched"
    echo "  data file is red on this tree.  ⌗ Neither claim is the suite's verdict; CI is."
    exit 0
fi
echo "  ⛔ NOT GREEN -- class one rc=$RC1, class two rc=$RC2.  The named line above says which."
exit 1
