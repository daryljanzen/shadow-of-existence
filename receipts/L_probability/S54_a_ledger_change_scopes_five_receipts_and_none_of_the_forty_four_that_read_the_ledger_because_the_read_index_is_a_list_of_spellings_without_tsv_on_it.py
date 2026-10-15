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
superseded one, and set down.  ** SIX receipts were genuinely red and not one was a receipt this
seat was watching. **  ⛔ *Four were found by hand; the last two were found by READING the CI log for
this revision's own REGISTRATION commit -- `S50`'s `Ⓒ①` and `S52`'s `Ⓒ③`, both this seat's, both the
same class as `S19`'s.  **The hand census missed a third of them**, which is the measure of how
little a seat can see of its own branch without running the suite.*  ⌗ *And the `tolerance` job's
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
          r50.returncode == 0 and bool(a50)
          and int(a50.group(2)) != int(a50.group(4)) and int(a50.group(2)) == 17)

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
          r52.returncode == 0 and bool(a52)
          and (int(a52.group(1)), int(a52.group(2))) == (24, 12)
          and int(a52.group(4)) > int(a52.group(1)))

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
          len(sd) == 2 and all(not t for t in sd.values()) and s19_tsv
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
    touched = {f for f in git('diff', '--name-only', f'{REG}~1..HEAD').split()
               if f.startswith('receipts/') and f.endswith('.py')}
    touched |= {l[3:].strip() for l in git('status', '--porcelain').split('\n')
                if l[3:].strip().startswith('receipts/') and l.strip().endswith('.py')}
    allowed = ('L_probability/S19', 'L_probability/S50', 'L_probability/S52',
               'L_probability/S54', 'L_probability/S5_',
               'P03_SdS_slicing/P03_the_enclosed_mass')
    strays = sorted(f for f in touched if not any(a in f for a in allowed))
    print(f'      receipts differing over this revision and its working tree: {len(touched)}')
    for f in sorted(touched):
        print(f'        {f}')
    check(f'Ⓓ① ⛭ this revision touches {len(touched)} receipt(s) and every one of them is named in '
          f'its own commit messages: the four red ones, the authorship gate two of them share, and '
          f'this file.  {len(strays)} stray(s).  ⌗ Counted over the COMMITTED diff and the working '
          f'tree together, so the claim holds before this file is committed and after.  ⛭ r7364: '
          f'*it was `4` until CI\'s own run on the registration commit named two more reds this '
          f'seat\'s census had missed -- `S50` and `S52`, both the same class -- and the count moves '
          f'with the work rather than the work being trimmed to the count*',
          not strays and len(touched) == 6
          and not any(a in f for a in STOOD_DOWN for f in touched))

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
