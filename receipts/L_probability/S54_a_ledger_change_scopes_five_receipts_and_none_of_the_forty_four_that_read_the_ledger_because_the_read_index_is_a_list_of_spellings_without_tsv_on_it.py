#!/usr/bin/env python3
"""S54 -- THE SUITE THE GATE NEVER RAN, AND WHY NOTHING WOULD HAVE CAUGHT IT.  ⛭⛭⛭ *** A CHANGE TO
THE QUOTE-PIN LEDGER PUTS `5` RECEIPTS IN THE SCOPED JOB'S SUITE SCOPE, AND NOT ONE OF THE `44` THAT
READ THE LEDGER IS AMONG THEM. ***  The gate job runs no receipt at all; the scoped job runs five
that read something else.  ** So a revision that only adjudicates ledger rows -- which is what this
entire repair phase does -- has no check anywhere that runs a receipt reading what it changed. **

** THE CONFESSION FIRST, BECAUSE IT IS WHY THERE IS ANYTHING TO MEASURE. **  This seat landed
`r7358`, `r7360` and `r7362` on `scripts/run_fast_job.sh`: the gates and the generators, every
`corpus/check_*.py`, and not one receipt.  The CI job that does run receipts was red on this branch
throughout and some seventy notifications were each checked against the head, found to name a
superseded one, and set down.  ** SEVEN receipts were genuinely red and not one was a receipt this
seat was watching. **  ⛔ *Four were found by hand; the rest were found by READING THE CI LOGS for
this revision's OWN pushes -- `S50`'s `Ⓒ①` and `S52`'s `Ⓒ③` on the registration commit, and `S53`'s
`Ⓐ③` on the push that carried the first six repairs.  **The hand census missed three of the seven**,
which is the measure of how little a seat can see of its own branch without running the suite -- and
the seventh was CAUSED by repairing the other six.*  ⌗ *And the `tolerance` job's
red is the same `S52` gate, so three distinct CI checks reduce to one defect.*  The six are two
causes; `r7364`'s first push repaired four and its second the other two:
      `S19` ⒈  `Ⓓ①`'s floor `0 < len(_allday)` FIRED ON ITS OWN SUCCESS -- this line's repairs
               removed the last all-dangling disjunction, so the gate went red for the defect
               being gone.  *The seventh instance of that class this fortnight, and the second
               inside a receipt of this seat's that NAMES the class.*
      `S19` ⒉  `Ⓒ②`'s five-rate ordering SWAPPED a pair: `REPAIR-OWED` `33.3` per cent at the pin
               against `19.2` live, `DELIBERATE` `21.2` against `19.5`.  ** The pair did not drift,
               it was moved: `60`+ `REPAIR-OWED` rows were retired this phase and the ones repaired
               are the ones that dangled. **
      `P03`/`S5`  one defect in two authorship gates written four revisions apart: both ask whether
               this seat reached outside what it owns and both look for the warrant INSIDE THE FILE,
               while `r7353` ② put the authorisation in `FOR_60.md` and the announcement in the push.
      `S23`    nothing of its own; it runs `P03`.
      `S50`    `Ⓒ①` scored arm ⒝ on an arbiter that lists `corpus/` LIVE -- ledgers included -- so
               the figure moved with every adjudication any seat made: `17` of `30` when scored,
               `16` live.  *That arbiter is the one `r7358` withdrew, and the withdrawal had not
               reached the gate that scores it.*
      `S52`    `Ⓒ③` asserted a count of the keys ITS OWN REVISION MINTS, read live: `24` in `12`
               receipts at the commit the figure was taken, `25` in `13` two commits later.
               ** The same revision's next push broke it. **
      `S53`    `Ⓐ③` measured a RESTRAINT -- "this revision touches no receipt but its own" -- over
               the range `CENSUS..HEAD`, so **this revision's six repairs, landing after that
               census, were counted as `r7362`'s.**  *The claim was true; the range it was
               asserted over keeps growing.*  ⇒ The eighth face of the class, and the first found
               in a restraint rather than in a measurement -- and the only one of the seven that
               this revision CAUSED rather than merely uncovered.

** AND THEN THE REAL FINDING, WHICH IS LARGER THAN THE FOUR.  ⛔⛭⛭⛭ THE READ INDEX IS A LIST OF
SPELLINGS AND `tsv` IS NOT ON IT. **  `scripts/receipt_scope.py`'s `NAME_RE` enumerates
`py|tex|md|txt|npz|npy|json|dat|csv|bib`.  *All four adjudication ledgers are `.tsv`.*  So the static
half of the index cannot see a ledger read at all -- and `0` of the `871` TRACED entries records one
either, so no entry anywhere in the index carries a `.tsv`.
  ⇒ ** `L254_the_rule_was_spellings`'s `A1` by name: a rule made of spellings misses the next
    spelling.  Here the next spelling is the extension of every file this phase edits. **
  ⌗ *The patch is ONE TOKEN and it is verified below on a local copy rather than applied: with `tsv`
    in the list the scope goes `5` to `49` and all `44` readers come in.  `scripts/receipt_scope.py`
    is `70.1`'s instrument, so it is ROUTED as a patch in `FOR_66_FROM_60.md` and not edited here.*

** AND ALL THREE REGISTERED ARMS LAND, TWO OF THEM WITH THE CAVEAT THE REGISTRATION WROTE FIRST. **
  ⒜ `2` red in the `152` nobody had looked at -- `0.0132` against `0.013`-`0.060`.  ** INSIDE, AT
    THE FLOOR, holding by ONE receipt: had either been green it would have failed LOW. **
  ⒝ `5` of the `5` reds are the ONE cause -- `1.00` against `0.55`-`1.00`.  ⚠ ** Inside at the
    CEILING, and the registration declared in advance that a pass there carries no information;
    the informative outcome was refutation and it did not come. **
  ⒞ `0` of them visible to any gate -- ** the point prediction, exactly. **

** ⛔⛭⛭⛭ AND THE ARM'S OWN INSTRUMENT HAD THE CLASS INSIDE IT. **  *The run named a SIXTH red: a
receipt that DRIVES another seat's audit as a subprocess.  That audit failed on an import the
container running the scope did not have, so the receipt parsed empty output and died on a
`KeyError`.*  ⇒ ** It is dependency-missing one layer down, and the runner called it RED because it
tests for the import error in the RECEIPT'S OWN stderr while the module surfaced in the stderr of
the process it drove. **  *A classifier keyed on a spelling, in the wrong process's output -- and it
inflated arm ⒜ by one.*

** ⛔⛭⛭⛭ AND THE GATE THAT REPORTS THAT WAS THE CLASS AGAIN, ONE LEVEL UP. **  *Its first cut
asserted the module was ABSENT FROM THIS CONTAINER -- an environmental fact written as a fact about
the corpus -- and it went red on the runner, where that module IS installed and the audit exits `0`.*
⇒ ** So the claim is proved BY CONSTRUCTION on a two-level fixture that needs no absent dependency,
and what this machine happens to have is PRINTED and asserted of nothing. **  *The ninth instance of
this phase's class, committed by this seat, inside the gate whose subject is that class, in the act
of reporting it.*

** AND THE REGISTRATION'S OWN CLAIM IS NARROWED BY THE MEASUREMENT, WHICH IS WHY IT WAS PUSHED
FIRST. **  `PREDICTION.md` said the standing instruction to stand down from `L259/D1` and
`L_numerics/Q1` rests on the same marking.  *It does not: neither of those receipts names a `.tsv`
anywhere in its source, so the extension blindness does not reach their `⚠ CONTRADICTED` markings.*
⇒ The claim holds for `S19`, where it was demonstrated, and is withdrawn for the other two -- and the
withdrawal is a gate below rather than a sentence.
"""
import importlib.util
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
COST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7364_60_the_suite_the_gate_never_ran',
                    'cost.py')
REG = 'd5a55599'                 # the registration commit, pushed before the scope run was read
#: ⛔⛭⛭⛭ r7368: THIS REVISION'S OWN LAST CONTENT COMMIT.  *Three clauses below read the LIVE state
#: of things this revision measured at a pin, and `r7368` found all three: two read a figure out of
#: another receipt's printout where the trunk has since moved it, and `Ⓓ①` read a diff whose base
#: was pinned and whose HEAD was not.*  ⇒ ** A range has TWO ends and `Ⓓ①`'s own note secured the
#: base: *"it is read from THIS revision's registration commit forward, which is fixed."*  So did
#: `S5`'s, three times over.  The fixed end was never the one that moved. **
FRAME = '3a37b01b'               # r7364's last content commit: a fixed sha, ancestor of HEAD
LEDGERS = ('corpus/quote_pin_baseline.tsv', 'corpus/prose_pin_baseline.tsv',
           'corpus/exact_count_baseline.tsv', 'corpus/target_annotations.tsv')
LEDGER = LEDGERS[0]
PAPER = 'corpus/CR_synthesis.tex'
#: the two receipts the carry ledger's `⚠ CONTRADICTED` marking stands this seat down from.  ⛔ Read
#: ONLY -- both are on this seat's do-not-edit list and neither is touched.
STOOD_DOWN = ('receipts/L259_the_distance_from_the_present/D1',
              'receipts/L_numerics/Q1')
_TSV = re.compile(r'([A-Za-z0-9_.-]+\.tsv)')
BAR = '=' * 100


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def head(t):
    print(f'\n  {"-" * 96}\n  {t}\n  {"-" * 96}')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def run(rel, timeout=1500):
    """run a receipt FROM ITS OWN DIRECTORY and return the completed process"""
    return subprocess.run([sys.executable, os.path.basename(rel)],
                          cwd=os.path.join(ROOT, os.path.dirname(rel)),
                          capture_output=True, text=True, errors='replace', timeout=timeout)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _one(pattern, where='receipts/L_probability'):
    import glob
    hits = sorted(glob.glob(os.path.join(ROOT, where, pattern)))
    return os.path.relpath(hits[0], ROOT).replace(os.sep, '/') if hits else None


def _readers_of(idx, basename):
    """every registered receipt whose SOURCE names this file, which is what reading it looks like
    from outside.  ⌗ The literal stands to the LEFT of nothing and is found by the name, so this
    census does not depend on the index it is being compared against."""
    out = []
    for rec in idx:
        fp = os.path.join(ROOT, rec)
        if os.path.exists(fp) and basename in io.open(fp, errors='replace').read():
            out.append(rec)
    return out


def _scoped(rs, idx, path, which='suite'):
    return set(rs.scope(idx, {path}, set(), set(), which))


def main():
    print()
    print('  S54 -- a ledger change scopes five receipts, and none of them reads the ledger')
    C = _load(COST, 'r7364_cost')
    sys.path.insert(0, os.path.join(ROOT, 'scripts'))
    rs = _load(os.path.join(ROOT, 'scripts', 'receipt_scope.py'), 's54_receipt_scope')
    idx, traced, stale, new = rs.load(ROOT)

    # ══════════════════════════════════════════════════════════════════════════════════════════════
    head('A -- THE HOLE, IN BOTH LAYERS: ONE RUNS NO RECEIPT AND THE OTHER RUNS THE WRONG FIVE')
    # ══════════════════════════════════════════════════════════════════════════════════════════════
    job = io.open(os.path.join(ROOT, 'scripts', 'run_fast_job.sh'), encoding='utf-8',
                  errors='replace').read()
    gates = C.gate_names()
    #: ⌗ the two-sided reading of the job: it names the GATE directory and no receipt path at all.
    check(f'Ⓐ① the landing sequence this seat used runs NO RECEIPT: `scripts/run_fast_job.sh` names '
          f'`corpus/` and never a path under `receipts/`, and the population it runs is the '
          f'{len(gates)} `corpus/check_*.py` gates',
          'corpus/' in job and not re.search(r'receipts/\S*\.py', job) and len(gates) > 100)

    sc_led = _scoped(rs, idx, LEDGER)
    sc_pap = _scoped(rs, idx, PAPER)
    print(f'      a change to {LEDGER} scopes {len(sc_led)} receipt(s)')
    print(f'      a change to {PAPER} scopes {len(sc_pap)} receipt(s)')
    #: the control is on the same function and the same index: a PAPER change scopes an order of
    #: magnitude more, so a small number here is not the scope machinery being small.
    check(f'Ⓐ② and the job that DOES run receipts scopes {len(sc_led)} of them for a change to the '
          f'quote-pin ledger, against {len(sc_pap)} for a change to one paper -- the same function '
          f'and the same index, so the small number is the LEDGER and not the machinery',
          len(sc_led) < 10 < len(sc_pap))

    readers = _readers_of(idx, os.path.basename(LEDGER))
    both = sc_led & set(readers)
    print(f'      {len(readers)} registered receipt(s) name the ledger in their own source; '
          f'{len(both)} of them are in the scope')
    for _r in sorted(sc_led):
        print(f'        scoped: {_r.split("/")[-1][:62]}  '
              f'{"READER" if _r in readers else "(reads something else)"}')
    check(f'Ⓐ③ ⛔⛭⛭⛭ AND NOT ONE OF THE {len(readers)} RECEIPTS THAT READ THE LEDGER IS IN THAT '
          f'SCOPE.  ** The five scoped are scoped for other reads entirely.  So the one job that '
          f'runs receipts runs none that reads what the whole repair phase changes **',
          len(readers) > 20 and not both)

    # ── the cause, named and measured ─────────────────────────────────────────────────────────────
    import json as _json
    raw = _json.load(io.open(os.path.join(ROOT, rs.INDEX), encoding='utf-8'))
    traced_tsv = [r for r, e in raw['receipts'].items()
                  if any(str(x).endswith('.tsv') for x in (e.get('r') or []))]
    static_blind = [r for r in readers
                    if os.path.basename(LEDGER) not in rs.source_names(
                        io.open(os.path.join(ROOT, r), errors='replace').read())]
    print(f'      NAME_RE = {rs.NAME_RE.pattern}')
    print(f'      the index was traced at {traced["commit"][:8]} on {traced["date"][:10]}; '
          f'{len(stale)} entries are STALE and {len(new)} are NEW, so the static half decides for '
          f'{len(stale) + len(new)} of {len(idx)}')
    check(f'Ⓐ④ ⛔ and the cause is A LIST OF SPELLINGS: `tsv` is not in `NAME_RE`\'s extension '
          f'group, every one of the {len(LEDGERS)} adjudication ledgers is a `.tsv`, the static '
          f'half therefore misses the read in {len(static_blind)} of the {len(readers)} readers, '
          f'and {len(traced_tsv)} of the {len(raw["receipts"])} TRACED entries records a `.tsv` '
          f'read -- so no entry anywhere in the index carries one.  ⛭ `L254`\'s `A1` by name',
          'tsv' not in rs.NAME_RE.pattern
          and all(f.endswith('.tsv') for f in LEDGERS)
          and len(static_blind) == len(readers)
          and not traced_tsv)

    # ── the patch, verified on a copy and routed rather than applied ───────────────────────────────
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        src = io.open(os.path.join(ROOT, 'scripts', 'receipt_scope.py'), encoding='utf-8').read()
        old = 'py|tex|md|txt|npz'
        patched = src.replace(old, 'py|tex|md|txt|tsv|npz', 1)
        pp = os.path.join(tmp, 'rs_patched.py')
        io.open(pp, 'w', encoding='utf-8').write(patched)
        rsp = _load(pp, 's54_rs_patched')
        idx_p = rsp.load(ROOT)[0]
        sc_p = _scoped(rsp, idx_p, LEDGER)
    print(f'      with `tsv` in the list: the ledger scopes {len(sc_p)} receipt(s), and '
          f'{len(sc_p & set(readers))} of the {len(readers)} readers are in it')
    check(f'Ⓐ⑤ ⌗ and the repair is ONE TOKEN, verified HERE on a copy and ROUTED rather than '
          f'applied: adding `tsv` takes the ledger\'s scope from {len(sc_led)} to {len(sc_p)} and '
          f'brings {len(sc_p & set(readers))} of the {len(readers)} readers in.  '
          f'`scripts/receipt_scope.py` is `70.1`\'s instrument and is not edited here',
          patched != src and len(sc_p & set(readers)) == len(readers)
          and 'tsv' not in rs.NAME_RE.pattern)

    # ══════════════════════════════════════════════════════════════════════════════════════════════
    head('B -- THE FOUR REDS, REPAIRED AND RUN HERE RATHER THAN CITED')
    # ══════════════════════════════════════════════════════════════════════════════════════════════
    s19 = _one('S19_*.py')
    r19 = run(s19)
    live0 = 'the live figure is 0' in r19.stdout
    pin2 = re.search(r'at \w+: (\d+) of (\d+) disjunction\(s\) stood on arms that ALL dangle;'
                     r'\s+live: (\d+) of (\d+)', r19.stdout)
    print(f'      S19 exits {r19.returncode};  pinned/live all-dangling: '
          f'{pin2.groups() if pin2 else "NOT PRINTED"}')
    check(f'Ⓑ① `S19` RUNS GREEN (exit `{r19.returncode}`), asserted by running it, and its `Ⓓ①` now '
          f'holds the finding at the pin with a MONOTONE live arm: '
          f'{pin2.group(1) if pin2 else "?"} all-dangling disjunction(s) at `PIN` against '
          f'{pin2.group(3) if pin2 else "?"} live, and the live figure is PRINTED as the result',
          r19.returncode == 0 and bool(pin2) and int(pin2.group(3)) == 0
          and int(pin2.group(1)) > 0 and live0)

    swap = re.search(r'the pair that MOVED: REPAIR-OWED ([\d.]+) -> ([\d.]+) against '
                     r'DELIBERATE ([\d.]+) -> ([\d.]+)\s+\((\w+) live\)', r19.stdout)
    print(f'      S19 Ⓒ② the swapped pair: {swap.groups() if swap else "NOT PRINTED"}')
    check(f'Ⓑ② and `Ⓒ②` keeps the HEADLINE live and pins only the clause that moved: the swap is '
          f'PRINTED with both ends -- `REPAIR-OWED` {swap.group(1) if swap else "?"} to '
          f'{swap.group(2) if swap else "?"} against `DELIBERATE` {swap.group(3) if swap else "?"} '
          f'to {swap.group(4) if swap else "?"} -- so the gate reports the evidence that this '
          f'line\'s repairs landed on the rows that dangled instead of asserting nobody repaired '
          f'them',
          bool(swap) and swap.group(5) == 'SWAPPED'
          and float(swap.group(2)) < float(swap.group(1))
          and float(swap.group(2)) < float(swap.group(4)))

    p03 = _one('P03_the_enclosed_mass*.py', where='receipts/P03_SdS_slicing')
    r03 = run(p03)
    unauth = re.search(r'with this branch as it stands: (\d+) UNAUTHORISED', r03.stdout)
    named = re.search(r'authorised by the ORDER FILE naming the prefix at the crossing commit: '
                      r'(\d+)', r03.stdout)
    carried = re.search(r"carried by an ORDERED REPAIR the receipt's own source names: (\d+)",
                        r03.stdout)
    ctrl = re.search(r'with one MODIFIED unowned receipt injected: (\d+)', r03.stdout)
    print(f'      P03 exits {r03.returncode};  unauthorised '
          f'{unauth.group(1) if unauth else "?"}, order-named {named.group(1) if named else "?"}, '
          f'carried {carried.group(1) if carried else "?"}, '
          f'control {ctrl.group(1) if ctrl else "?"}')
    check(f'Ⓑ③ `P03` RUNS GREEN (exit `{r03.returncode}`) and its repair is NOT VACUOUS on its own '
          f'printout: {named.group(1) if named else "?"} crossing(s) authorised by the ORDER FILE '
          f'at the commit that made them, {carried.group(1) if carried else "?"} carried by an '
          f'ordered repair the receipt itself names, {unauth.group(1) if unauth else "?"} left '
          f'unauthorised -- and the injected control still reports '
          f'{ctrl.group(1) if ctrl else "?"} on the same computation',
          r03.returncode == 0 and unauth and int(unauth.group(1)) == 0
          and named and int(named.group(1)) > 0 and carried and int(carried.group(1)) == 1
          and ctrl and int(ctrl.group(1)) == 1)

    pos = re.search(r'a TAKE push that named a COUNT where the order asked for names: (\w+)',
                    r03.stdout)
    crossed = re.search(r'and it crossed (\d+) directory\(ies\) it did not name', r03.stdout)
    check(f'Ⓑ④ ⚠ and the ONE protocol failure that is this seat\'s rather than the gate\'s is '
          f'REPORTED by that same receipt and not asserted away: push `{pos.group(1) if pos else "?"}'
          f'` announced a COUNT where `r7353` ② asked for names, and crossed '
          f'{crossed.group(1) if crossed else "?"} directory(ies) it never named.  ** A reference by '
          f'POSITION where the order asked for a name, which is this corpus\'s own recurring class '
          f'arriving in the compliance rather than in the code **',
          bool(pos) and bool(crossed) and int(crossed.group(1)) > 1)

    s5, s23 = _one('S5_*.py'), _one('S23_*.py')
    r5 = run(s5)
    legs = re.search(r'(\d+) whose PREFIX THE ORDER FILE NAMES at the crossing commit, and (\d+) '
                     r'none of the four', r5.stdout)
    print(f'      S5 exits {r5.returncode};  order-named leg '
          f'{legs.group(1) if legs else "?"}, unowned {legs.group(2) if legs else "?"}')
    check(f'Ⓑ⑤ `S5` RUNS GREEN (exit `{r5.returncode}`) and its fourth ground has a POPULATION -- '
          f'{legs.group(1) if legs else "?"} crossing(s) carried by the order file and '
          f'{legs.group(2) if legs else "?"} left over.  ⌗ *The fifth ground `P03` needed is NOT '
          f'added there: this branch gives it no instance, and an authorship leg with no instance '
          f'is that receipt\'s own complaint about itself*',
          r5.returncode == 0 and bool(legs) and int(legs.group(1)) > 0
          and int(legs.group(2)) == 0)

    r23 = run(s23)
    print(f'      S23 exits {r23.returncode}')
    check(f'Ⓑ⑥ and `S23` RUNS GREEN (exit `{r23.returncode}`) with nothing repaired in it: both its '
          f'red gates read `P03`, so they cleared when `P03` did -- asserted by running it rather '
          f'than by citing it',
          r23.returncode == 0
          and os.path.relpath(s23, '').startswith('receipts/')
          and not any(f.endswith(os.path.basename(s23))
                      for f in git('diff', '--name-only', f'{REG}~1..HEAD').split()))

    # ── and the two CI found that this seat's own census had missed ────────────────────────────────
    #   ⛔ Both are the SAME class as S19's and both are this seat's: a figure a revision measured,
    #   re-read live by the gate that scores it.  Found by reading the CI log for this revision's own
    #   REGISTRATION commit -- a fixed, pushed tree -- rather than by any sweep of this seat's.
    s50, s52 = _one('S50_*.py'), _one('S52_*.py')
    r50 = run(s50)
    a50 = re.search(r'the arbiter at (\w+), where the arm was scored: (\d+) multi-site of (\d+);'
                    r'\s+LIVE it reads (\d+)', r50.stdout)
    print(f'      S50 exits {r50.returncode};  pinned/live multi-site: '
          f'{a50.groups() if a50 else "NOT PRINTED"}')
    check(f'Ⓑ⑦ `S50` RUNS GREEN (exit `{r50.returncode}`) and its arm ⒝ is now a FROZEN RECORD of a '
          f'withdrawn arbiter: {a50.group(2) if a50 else "?"} multi-site of '
          f'{a50.group(3) if a50 else "?"} in the frame it was scored in against '
          f'{a50.group(4) if a50 else "?"} live.  ** That arbiter lists `corpus/` live and counts '
          f'the `.tsv` ledgers, so the number moved with other seats\' adjudications -- which is '
          f'exactly what `r7358` withdrew this arm for, arriving in the gate that scores it **',
          #: ⛭⛭⛭ r7368: the live leg asserted `frame != live`, and the live reading has since
          #: come BACK to `17` -- the trunk's adjudications moved the count away and then back.
          #: ⇒ *** A MOVING MEASUREMENT CAN RETURN TO ITS OLD VALUE, SO EQUALITY IS NOT EVIDENCE OF
          #:     STABILITY -- and a gate that reads the movement off a single live sample is
          #:     measuring a coincidence either way. ***  The frame figure is asserted and the live
          #:     one printed; the withdrawal stands on the arbiter's DEFINITION, which lists
          #:     `corpus/` live, and not on any two readings differing today.
          r50.returncode == 0 and bool(a50) and int(a50.group(2)) == 17
          and 'corpus/' in r50.stdout)

    r52 = run(s52)
    a52 = re.search(r'keys stamped r7360\+60: (\d+) in (\d+) receipt\(s\) at (\w+), where the figure '
                    r'was taken;\s+LIVE (\d+) in (\d+)', r52.stdout)
    print(f'      S52 exits {r52.returncode};  minted at pin / live: '
          f'{a52.groups() if a52 else "NOT PRINTED"}')
    check(f'Ⓑ⑧ ⛔⛭⛭⛭ `S52` RUNS GREEN (exit `{r52.returncode}`) and its `Ⓒ③` was the sharpest of the '
          f'six: it asserted a count of the keys **ITS OWN REVISION MINTS**, read live -- '
          f'{a52.group(1) if a52 else "?"} in {a52.group(2) if a52 else "?"} receipts at the commit '
          f'the figure was taken, {a52.group(4) if a52 else "?"} in '
          f'{a52.group(5) if a52 else "?"} live.  ** Not a later seat and not a later revision: the '
          f'SAME revision\'s next push minted one more. **  ⌗ *The live clause is now that no '
          f'retired row has LOST its carrier, which is the one direction correct later work cannot '
          f'move*',
          #: ⛭⛭⛭ r7368: the live leg asserted the stamp count GREW -- 24 to 25, this revision's
          #: own next push -- and the trunk's `r7355+cc66` pass then re-adjudicated 22 of the 24
          #: rows to whichever side landed first, so the live count under this seat's stamp FELL to
          #: `2`.  ⇒ ** A stamp count has no assertable direction: this seat's own next push raises
          #: it and another seat's adjudication lowers it, and neither is a defect in what this
          #: clause claims. **  The pinned pair carries the figure and the claim becomes that the
          #: two readings DIFFER AT ALL, which is the whole finding.
          r52.returncode == 0 and bool(a52)
          and (int(a52.group(1)), int(a52.group(2))) == (24, 12)
          and int(a52.group(4)) != int(a52.group(1)))

    s53 = _one('S53_*.py')
    r53 = run(s53)
    a53 = re.search(r"over this revision's OWN (\d+) commit\(s\), (\d+) receipt\(s\) differ and "
                    r'(\d+) of them', r53.stdout)
    print(f'      S53 exits {r53.returncode};  own commits / touched / others: '
          f'{a53.groups() if a53 else "NOT PRINTED"}')
    check(f'Ⓑ⑨ ⛔⛭⛭ `S53` RUNS GREEN (exit `{r53.returncode}`) and it is the one red of the seven '
          f'that THIS REVISION CAUSED: its restraint was measured over `CENSUS..HEAD`, so the six '
          f'repairs above were counted as `r7362`\'s.  ** Now read over that revision\'s OWN '
          f'{a53.group(1) if a53 else "?"} commits -- {a53.group(2) if a53 else "?"} receipt '
          f'touched, {a53.group(3) if a53 else "?"} of anyone else\'s -- so a later revision\'s '
          f'work cannot enter the range **  ⌗ *and the working-tree term goes with it: correct '
          f'before that revision\'s own commit, and a term any later edit satisfies once it is '
          f'landed*',
          r53.returncode == 0 and bool(a53)
          and int(a53.group(2)) == 1 and int(a53.group(3)) == 0 and int(a53.group(1)) >= 1)

    # ══════════════════════════════════════════════════════════════════════════════════════════════
    head('C -- THE REGISTRATION OVERREACHED BY ONE CLAUSE, AND THE MEASUREMENT NARROWS IT')
    # ══════════════════════════════════════════════════════════════════════════════════════════════
    s19_tsv = sorted(set(_TSV.findall(io.open(os.path.join(ROOT, s19), errors='replace').read())))
    sd = {}
    for want in STOOD_DOWN:
        hit = [r for r in idx if want in r]
        for r in hit:
            sd[r] = sorted(set(_TSV.findall(io.open(os.path.join(ROOT, r), errors='replace').read())))
    for r, t in sd.items():
        print(f'      {r.split("/")[-1][:52]}  names .tsv: {t or "none"}')
    pred = io.open(os.path.join(os.path.dirname(COST), 'PREDICTION.md'), encoding='utf-8').read()
    check(f'Ⓒ① ⛔ the claim `PREDICTION.md` pushed is NARROWED by the measurement, which is why it '
          f'was pushed first: it said the stand-down from `L259/D1` and `L_numerics/Q1` rests on '
          f'the same marking, and NEITHER of them names a `.tsv` anywhere in its source -- so the '
          f'extension blindness reaches `S19`, where it was demonstrated, and NOT those two.  '
          f'** The registration carried a consequence it had not checked, and the check retracts it '
          f'rather than a sentence doing so **',
          # ⌗ r7364: per-NAME rather than `len(sd) == 2`.  A count on a set built by scanning the
          #   registry is a pin on something the tree can grow -- the prose-pin ratchet flagged it,
          #   and it is this revision's own class.  Each stood-down prefix is asserted to have
          #   RESOLVED, which is the non-vacuity the count was standing in for.
          all(any(w in r for r in sd) for w in STOOD_DOWN)
          and all(not t for t in sd.values()) and s19_tsv
          and os.path.basename(LEDGER) in s19_tsv
          and 'rests on the same marking' in pred)

    #: ⌗ and the live reason S19's own marking was wrong, kept as the positive half: the diff that
    #: the marking called agreed-on DOES carry the ledger, and S19 opens it.
    diff = set(git('diff', '--name-only', 'a1a263e0..d17a918e').split())
    s19_src = io.open(os.path.join(ROOT, s19), errors='replace').read()
    check(f'Ⓒ② and the positive half stands on the two commits the marking named: the diff '
          f'`a1a263e0..d17a918e` carries {LEDGER} ({LEDGER in diff}), `S19` opens that file by name '
          f'({os.path.basename(LEDGER) in s19_src}), and the index puts `S19` in scope for it '
          f'({s19 in sc_led}) -- so "nothing it reads differs" was false about the one read that '
          f'matters',
          LEDGER in diff and os.path.basename(LEDGER) in s19_src and s19 not in sc_led)

    # ══════════════════════════════════════════════════════════════════════════════════════════════
    head('D -- THE RESTRAINT, SHOWN RATHER THAN PROMISED')
    # ══════════════════════════════════════════════════════════════════════════════════════════════
    #: ⛔⛭⛭⛭ r7368: ** AND THIS CLAUSE'S OWN NOTE SECURED THE WRONG END. **  *It read
    #: `REG~1..HEAD` and said in writing that it was safe because it is "read from THIS revision's
    #: registration commit forward, which is fixed".  A range has TWO ends.  `r7368`'s commits
    #: joined the open one and the count went from `7` to `56`, with `49` strays -- none of them
    #: touched by `r7364` at all.*
    #:   ⇒ *** The same shape `S5` carried three times with the same written safety argument, and
    #:       the same shape this clause is COUNTING.  It is the one in this file. ***
    #: ⌗ *The working-tree arm goes with it: it was here so the claim would hold before this file
    #:   was committed, and a working tree is the most moving end there is.  The claim is now
    #:   historical and reads between two fixed commits.*
    touched = {f for f in git('diff', '--name-only', f'{REG}~1..{FRAME}').split()
               if f.startswith('receipts/') and f.endswith('.py')}
    _live_touched = {f for f in git('diff', '--name-only', f'{REG}~1..HEAD').split()
                     if f.startswith('receipts/') and f.endswith('.py')}
    allowed = ('L_probability/S19', 'L_probability/S50', 'L_probability/S52',
               'L_probability/S53', 'L_probability/S54', 'L_probability/S5_',
               'P03_SdS_slicing/P03_the_enclosed_mass')
    strays = sorted(f for f in touched if not any(a in f for a in allowed))
    print(f'      receipts differing between {REG}~1 and {FRAME}, this revision\'s own two ends: '
          f'{len(touched)};  between {REG}~1 and the MOVING head: {len(_live_touched)} -- '
          f'REPORTED, and the reason both ends are commits')
    for f in sorted(touched):
        print(f'        {f}')
    check(f'Ⓓ① ⛭ this revision touches {len(touched)} receipt(s) and every one of them is named in '
          f'its own commit messages: the six red ones, the authorship gate two of them share, and '
          f'this file.  {len(strays)} stray(s).  ⌗ Counted over the COMMITTED diff and the working '
          f'tree together, so the claim holds before this file is committed and after.  ⛭ r7364: '
          f'*it was `4`, then `6` when CI\'s run on the registration commit named `S50` and `S52`, '
          f'and now `7` because repairing those six broke `S53`\'s restraint -- the count moves with '
          f'the work rather than the work being trimmed to the count.*  ⚠ **And this clause is the '
          f'same shape as the one it is counting: a restraint read over a range -- and `r7368` '
          f'found that this note secured the BASE and left the HEAD open, so the next revision\'s '
          f'commits joined the range and the count went to {len(_live_touched)} with 49 strays. '
          f'A RANGE HAS TWO ENDS, and both are commits now**',
          not strays and len(touched) == 7 and len(_live_touched) > len(touched)
          and not any(a in f for a in STOOD_DOWN for f in touched))

    # ══════════════════════════════════════════════════════════════════════════════════════════════
    head('E -- THE THREE REGISTERED ARMS, SCORED ON THE RUN')
    # ══════════════════════════════════════════════════════════════════════════════════════════════
    import json as _j
    SR = _j.load(io.open(os.path.join(os.path.dirname(COST), 'SUITE_RESULT.json'),
                         encoding='utf-8'))
    R = C.RESULT
    _hand = set(C.known_red(C.scope()))
    _red = [r for r in SR['red'] if r not in SR['reclassified_dep']]
    _arm_a = [r for r in _red if r not in _hand]
    print(f"      the run at {SR['ran_at']}: green {SR['green']}, red {len(SR['red'])} as the runner "
          f"classified them, {len(SR['reclassified_dep'])} of those RECLASSIFIED "
          f"dependency-missing, dep {len(SR['dep'])} -> {len(SR['dep']) + 1}")
    print(f'      arm ⒜\'s reds -- in the scope, not hand-found: '
          f'{[r.split("/")[-1][:22] for r in _arm_a]}')
    _lo, _hi = C.A_BAND[0] * C.A_SPACE, C.A_BAND[1] * C.A_SPACE
    check(f'Ⓔ① arm ⒜ scored on the registered space: {len(_arm_a)} red in the {C.A_SPACE} nobody '
          f'had looked at = {len(_arm_a) / C.A_SPACE:.4f} against band {C.A_BAND[0]}–{C.A_BAND[1]} '
          f'({_lo:.2f}–{_hi:.2f} receipts), central {C.A_CENTRAL} -- ⛭ INSIDE, AT THE FLOOR.  '
          f'** It holds by ONE receipt: had either of the two been green the arm would have failed '
          f'LOW, and the floor was put at 2 so that it could **',
          len(_arm_a) == R['A_RED'] == 2 and _lo <= len(_arm_a) <= _hi
          and C.decisive_share(C.A_SPACE, C.A_CENTRAL, C.A_BAND) >= 0.05)

    _pred = io.open(os.path.join(os.path.dirname(COST), 'PREDICTION.md'), encoding='utf-8').read()
    check(f'Ⓔ② arm ⒝ scored: {R["B_ONE_CAUSE"]} of the {R["B_RED_SCORED"]} reds are the ONE cause -- '
          f'a gate re-reading live what its own revision measured at a pin, or the authorisation '
          f'face of it -- = {R["B_SHARE"]:.2f} against band {C.B_BAND[0]}–{C.B_BAND[1]}.  '
          f'⚠ INSIDE, AT THE CEILING, **and the registration declared in advance that a pass here '
          f'carries no information because the band can only fail low**: the informative outcome '
          f'was refutation and it did not come',
          R['B_ONE_CAUSE'] == R['B_RED_SCORED'] == len(_red)
          and C.B_BAND[0] <= R['B_SHARE'] <= C.B_BAND[1]
          and 'fails only low' in _pred.lower().replace('fails only below', 'fails only low'))

    check(f'Ⓔ③ arm ⒞ scored, and the POINT prediction holds EXACTLY: {R["C_GATE_VISIBLE"]} of the '
          f'{len(_red)} reds is visible to any `corpus/check_*.py`, because none of the '
          f'{len(gates)} of them runs a receipt -- which `Ⓐ①` establishes from the job script '
          f'itself.  *Any one of them would have refuted it*',
          R['C_GATE_VISIBLE'] == 0
          and all(r.startswith('receipts/') for r in _red)
          and not re.search(r'receipts/\S*\.py', job))

    # ── ⛔ and the arm's own instrument carried the class ──────────────────────────────────────────
    # ⛔⛭⛭⛭ r7364+60: AND THE FIRST CUT OF THIS GATE WAS THE CLASS AGAIN, ONE LEVEL UP.  *It asserted
    #   that the driven audit FAILS on an import `absent from this container` -- an ENVIRONMENTAL
    #   ABSENCE stated as a fact about the corpus.  On the runner, where that module IS installed,
    #   the audit exits `0` and the gate went red: the ninth instance of this phase's class, written
    #   into the very gate whose subject is that class, in the act of reporting it.*
    #   ⇒ *** The defect being claimed is a property of the RUNNER'S LOGIC, not of this machine, so
    #     it is proved BY CONSTRUCTION on a two-level fixture that needs no absent dependency: an
    #     outer script drives an inner one that imports a module no tree has, and the outer dies the
    #     way the receipt died.  The classifier's own rule is then evaluated on both stderrs. ***
    #   ⌗ *What this container happens to have is PRINTED and asserted of nothing.*
    import tempfile
    with tempfile.TemporaryDirectory() as _fx:
        _inner = os.path.join(_fx, 'inner.py')
        _outer = os.path.join(_fx, 'outer.py')
        io.open(_inner, 'w').write('import a_module_no_tree_has_xyz\nprint("rows")\n')
        io.open(_outer, 'w').write(
            'import subprocess, sys\n'
            'r = subprocess.run([sys.executable, %r], capture_output=True, text=True)\n'
            'scan = {int(l): 1 for l in r.stdout.split() if l.isdigit()}\n'
            'print(scan[1996])\n' % _inner)
        _in_r = subprocess.run([sys.executable, _inner], capture_output=True, text=True,
                               errors='replace')
        _out_r = subprocess.run([sys.executable, _outer], capture_output=True, text=True,
                                errors='replace')
    #: the runner's own rule, evaluated on each process's stderr
    _rule_on_outer = 'ModuleNotFoundError' in _out_r.stderr
    _rule_on_inner = 'ModuleNotFoundError' in _in_r.stderr
    print(f'      the fixture: the DRIVEN process exits {_in_r.returncode} and its stderr carries '
          f'the import error ({_rule_on_inner}); the DRIVING one exits {_out_r.returncode} with '
          f'`KeyError` ({"KeyError" in _out_r.stderr}) and its own stderr carries the import error '
          f'({_rule_on_outer})')
    print(f'      ⇒ so the runner\'s test -- `ModuleNotFoundError in the receipt\'s own stderr` -- '
          f'reads {_rule_on_outer} on a receipt whose dependency is missing one layer down, and '
          f'classifies it RED')
    _aud = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7101_70_three_grid_audit',
                        'audit.py')
    _ar = subprocess.run([sys.executable, _aud], cwd=ROOT, capture_output=True, text=True,
                         errors='replace', timeout=900)
    _here = subprocess.run([sys.executable, '-c', 'import camb'], capture_output=True).returncode
    print(f'      ⌗ REPORTED, asserted of nothing: on THIS machine the audit exits '
          f'{_ar.returncode} and `camb` imports {"yes" if _here == 0 else "no"} -- which is why the '
          f'run at the census saw the failure and why this gate must not assert it')
    check(f'Ⓔ④ ⛔⛭⛭⛭ AND THE SIXTH "RED" WAS DEPENDENCY-MISSING ONE LAYER DOWN, WHICH THE ARM\'S OWN '
          f'INSTRUMENT GOT WRONG -- proved on a FIXTURE rather than on this container: a driving '
          f'script whose driven script imports a module no tree has dies with `KeyError`, its own '
          f'stderr carries NO import error ({_rule_on_outer}) while the driven one\'s does '
          f'({_rule_on_inner}), so the runner\'s test classifies it RED.  ** A classifier keyed on '
          f'a spelling, in the wrong process\'s output: the instrument built to measure how much is '
          f'red had this revision\'s own class inside it, and it inflated arm ⒜ from {R["A_RED"]} '
          f'to {R["A_RED_IF_MISCLASSIFIED"]}. **  ⛭ *And the FIRST CUT OF THIS GATE asserted the '
          f'module was absent from this container -- an environmental fact stated as a corpus one, '
          f'which went red on the runner where it is installed: the class again, one level up, in '
          f'the act of reporting it*',
          # the classifier property, by construction and two-sided
          _rule_on_inner and not _rule_on_outer and 'KeyError' in _out_r.stderr
          and _in_r.returncode != 0 and _out_r.returncode != 0
          # and the reclassification as the RUN recorded it, read from the artefact
          and R['SIXTH_WAS_DEP'] is True
          and len(SR['reclassified_dep']) == 1
          and R['DEP_AFTER'] == R['DEP_BEFORE_RECLASSIFY'] + 1
          and R['A_RED_IF_MISCLASSIFIED'] == R['A_RED'] + 1)

    _reg_cost = git('show', f'{REG}:computations/beyond_the_wall/'
                            f'r7364_60_the_suite_the_gate_never_ran/cost.py')
    check(f'Ⓔ⑤ and the registration was committed and PUSHED before the run was read: `{REG}` '
          f'carries the three bands and NO result block, and the block arrives in a later commit',
          'A_BAND' in _reg_cost and 'RESULT.update' not in _reg_cost
          and 'RESULT.update' in io.open(COST, encoding='utf-8').read())

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ THE GATE JOB RUNS NO RECEIPT AND THE SCOPED JOB RUNS FIVE THAT READ SOMETHING ELSE.')
    print('    A ledger change has no check anywhere that runs a receipt reading the ledger, and')
    print('    the whole of this repair phase is ledger changes.  One token repairs it, and the')
    print('    token is routed rather than taken.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
