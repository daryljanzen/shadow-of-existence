#!/usr/bin/env python3
r"""S36 -- TWO MORE FACES OF THE LIVE-SUBJECT FAMILY, AND NEITHER WAS FOUND BY READING.

** THE FAMILY. **  A gate whose subject is a LIVE quantity goes red, or worse, when the work it
watches SUCCEEDS.  This line has now found it seven ways.  *Two more arrived in one session, and the
interesting half is not the defects: it is that each needed a DIFFERENT widening of what gets RUN.*

** \u2468 THE CRASH ON AN EMPTIED DENOMINATOR (`r7304`). **  `S2` reports the live quote-pin backlog as a
SHARE of the receipts carrying it.  *`r7300`'s `47` keys plus the trunk's landings took the bare
`UNADJUDICATED` bucket to ZERO, and a share has no denominator at zero.*
  => *** So the receipt DIED on a `ZeroDivisionError` rather than going red.  The quantity in the
      denominator IS the thing the ordered work removes, so the report is undefined exactly when the
      work is DONE. ***
  \u2308 \u26d4 ** And `cc66` had already repaired that gate's PREDICATE for this exact reason, with a note
    saying in terms that *a ratio needs a denominator and completing an order removes it*. **  The
    line beside it that says `printed and not asserted` went on dividing.
  \u230a => *** `S32` was the same fault the other way round -- the prose honest and the predicate not --
      so the pair gives the rule: THE TWO HALVES OF A GATE MUST BE REPAIRED TOGETHER, BECAUSE THE
      UNREPAIRED HALF IS THE ONE THAT DECIDES. ***

** \u2469 THE PREDICTION LEFT STANDING AS A BOUND (`r7306`). **  `S12`'s `\u24b6\u2462` asserted its own
pre-registered figure -- *the loss side is under `10`* -- on the one count in the receipt that only
ANOTHER seat can move: the claim-sites inside this seat's directories whose LAST WRITER is not this
seat.  ** It measures `14`, and no work of this seat's can lower it. **
  => *** A PREDICTION IS SCORED, NOT ASSERTED FOREVER.  The claim is the COMPARISON and that is kept
      live; the band is reported against the measurement. ***

** \u26d4\u26ed\u26ed\u26ed AND THE METHOD FINDING, WHICH IS WHY THIS RECEIPT EXISTS. **  *The first was found by CI.
The second COULD NOT HAVE BEEN: the scoped suite reads only what a push CAN HAVE CHANGED, and the
push that broke `S12` was another seat's.*
  => *** A receipt that breaks because ANOTHER seat moved its subject is outside every scope keyed on
      this seat's diff, CI's included, until something unrelated happens to touch it.  That is
      `r7298`'s lesson one level out: measure the radius over every KIND of thing a change can reach,
      and the kind still missing was SOMEONE ELSE'S change. ***

\u26a0 WHAT THIS CANNOT SETTLE is at the foot.
"""
import collections
import io
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


S2_BEFORE = 'bdb9a4dc'    # the last commit carrying S2's dividing report
S12_BEFORE = 'e9ea6dd8'   # the last commit carrying S12's standing bound
AFTER = 'a4b6c0e9'        # the commit that carried this revision -- the 71st member's corollary
BASE = 'corpus/quote_pin_baseline.tsv'
S2 = 'receipts/L_probability/S2_the_quote_pin_backlog_falls_by_sixty_six_on_this_lines_own_two_receipts_and_every_verdict_names_what_was_read_and_the_re_check_it_owes.py'
S12 = 'receipts/L_probability/S12_ownership_makes_the_class_larger_and_the_path_scope_was_too_narrow_as_well_as_impure.py'


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


def run_from_git(sha, path, tag):
    """Write the file as it stood at `sha` into THIS directory under a scratch name and RUN it from
    here, as the runner runs a receipt.  *Asserted by behaviour rather than by grepping the line
    that was changed -- which is the form `r7298` had to be taught.*"""
    src = _git('show', f'{sha}:{path}')
    # ⛔⛭ r7316+60: the suffix is NOT `.py`.  A receipt that leaves a `.py` file in a receipts
    #   directory, even for the seconds this one exists, is a file another receipt's restraint
    #   gate can catch in its diff -- `S39`'s did -- and one the tree's own receipt-shape gates
    #   have to be asked to ignore.  *`python3` runs a file by its contents and not by its
    #   extension, and `ROOT` is computed from `__file__`, so the probe still runs from HERE
    #   and resolves the tree correctly.*
    tmp = os.path.join(HERE, f'_s36_probe_{tag}.probe')
    with io.open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(src)
    try:
        r = subprocess.run([sys.executable, os.path.basename(tmp)], cwd=HERE, capture_output=True,
                           text=True, timeout=1200, env=dict(os.environ, NODE='ci'))
        return r.returncode, (r.stdout + r.stderr)
    finally:
        os.remove(tmp)


def run_live(path):
    r = subprocess.run([sys.executable, os.path.basename(path)], cwd=os.path.join(ROOT, os.path.dirname(path)),
                       capture_output=True, text=True, timeout=1200, env=dict(os.environ, NODE='ci'))
    return r.returncode, (r.stdout + r.stderr)


print()
print('=' * 100)
print('S36 -- two more faces of the live-subject family, and each needed a different widening')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE EMPTIED DENOMINATOR: A CRASH AND NOT A RED, REPRODUCED FROM THE PRE-REPAIR SOURCE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_led = rows_of(_git('show', f'{AFTER}:{BASE}'))
_bare = [c for c in _led if c[5] == 'UNADJUDICATED']
_pinned = [c for c in _led if c[5].startswith('UNADJUDICATED') and c[5] != 'UNADJUDICATED']
_bare_live = [c for c in rows_of(read(BASE)) if c[5] == 'UNADJUDICATED']
print(f'      at this revision: {len(_bare)} bare UNADJUDICATED, {len(_pinned)} suffixed; '
      f'live now: {len(_bare_live)} bare')
gate(f'Ⓐ① ⛭⛭⛭ ** THE BARE BUCKET IS EMPTY: `{len(_bare)}` bare `UNADJUDICATED` rows at this '
     f'revision\'s own commit and `{len(_pinned)}` that carry a suffix. ** *That is the campaign\'s '
     f'figure and not this seat\'s -- and it is the condition under which the report below has no '
     f'denominator.*  ⌗ The live arm is REPORTED (`{len(_bare_live)}`) and not asserted, because a '
     f'bare key is MINTED by an instrument and the bucket may rise again',
     len(_bare) == 0 and len(_pinned) > 0)

#: ⛭⛭ NOTHING HERE MATCHES A SENTENCE.  The first form of these two gates asserted the exception's
#:   NAME in the probe's output and another seat's repair NOTE in the source -- two quote pins, in a
#:   receipt whose own subject is gates that assert the wrong object.  *A CRASH is fully characterised
#:   without naming the exception: a non-zero exit, no gate reporting a failure, and a run that STOPS
#:   EARLY.*  ** So it is counted instead: gates reported before the exit, against the repaired run's. **
def _gate_lines(out):
    return [l for l in out.split('\n') if '[PASS]' in l or '[FAIL]' in l]


def _last_exception(out):
    tail = [l for l in out.rstrip().split('\n') if l.strip()]
    return bool(tail) and bool(re.match(r'^[A-Za-z_][A-Za-z0-9_.]*(Error|Exception)\b', tail[-1]))


_rc_before, _out_before = run_from_git(S2_BEFORE, S2, 's2')
_rc_after, _out_after = run_live(S2)
_g_before, _g_after = _gate_lines(_out_before), _gate_lines(_out_after)
_raised = _last_exception(_out_before)
# ⛭ r7649 (69): ONE of the pre-repair source's gates reads a DATA literal that moved under it -- `S2`'s
#   `Ⓒ③` looks for the optical-depth family row's `221.93`, and the P15 landing moved that row to the arm
#   of record's `222.02`.  That gate going red on the old source is the data moving, not the crash this
#   part characterises, so it is set aside BY NAME and every other gate is still required to pass.
_MOVED = ('Ⓒ③',)
_g_before_kept = [l for l in _g_before if not any(m in l for m in _MOVED)]
_failed_a_gate = any('[FAIL]' in l for l in _g_before_kept)
print(f'      the pre-repair source on THIS tree: rc={_rc_before}, ended on an exception={_raised}, '
      f'gates reported {len(_g_before)} with any FAIL={_failed_a_gate};  '
      f'the repaired source: rc={_rc_after}, gates reported {len(_g_after)}')
gate(f'Ⓐ② ⛔⛭⛭⛭ and it is a CRASH and not a red, shown by RUNNING the pre-repair source out of git on '
     f'this tree rather than by reading the line that changed --- and characterised WITHOUT naming '
     f'the exception: it exits `{_rc_before}`, ends on an exception class (`{_raised}`), reports NO '
     f'failing gate at all (`{not _failed_a_gate}`), and STOPS EARLY at `{len(_g_before)}` gates '
     f'against the repaired run\'s `{len(_g_after)}`.  ** A red names its gate and a crash names '
     f'nothing, so the only thing that catches one is something that RUNS the file and reads its exit '
     f'code --- `r7297` read that face in `S28`\'s `TypeError` **',
     _rc_before != 0 and _raised and not _failed_a_gate and len(_g_before) < len(_g_after)
     and _rc_after == 0)

_still_divides = re.search(r'/ len\(CARRY\)(?!\s*:\.\d)', read(S2).replace('if CARRY', ''))
print(f'      of the {len(_g_before)} gates the pre-repair run DID reach, '
      f'{sum(1 for l in _g_before if "[PASS]" in l)} passed; unguarded division remaining: '
      f'{bool(_still_divides)}')
gate(f'Ⓐ③ ⛔⛭⛭ and the two halves of that gate were repaired APART, which is the finding --- counted '
     f'rather than quoted: every one of the `{len(_g_before)}` gates the pre-repair run reached '
     f'PASSED, so the CONDITION was already sound, and the run died on the REPORT beside it; the '
     f'repaired source carries no unguarded division (`{not bool(_still_divides)}`).  ** The '
     f'condition had been made monotone for exactly this reason, which is why it passed.  `S32` was '
     f'the same fault reversed, the prose honest and the predicate not.  ⇒ The two halves of a gate '
     f'have to be repaired together, because the unrepaired half is the one that decides **',
     len(_g_before_kept) > 0 and all('[PASS]' in l for l in _g_before_kept)
     and len(_g_before) - len(_g_before_kept) <= len(_MOVED) and not _still_divides)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE PREDICTION LEFT STANDING AS A BOUND, ON A COUNT ONLY ANOTHER SEAT MOVES ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rc12_before, _out12_before = run_from_git(S12_BEFORE, S12, 's12')
#: ⌗ `69`'s rule, step 1: *a pattern that reads a NUMBER out of a tool's output* is `NOT-A-PIN`.
#:   The two readers below take figures out of the probe's own stdout and are adjudicated as such in
#:   the baseline rather than left to raise the unadjudicated ceiling.
_m = re.search(r'path-scope sites NOT owned:\s*(\d+)', _out12_before)
_loss = int(_m.group(1)) if _m else -1
_split = dict(collections.Counter(re.findall(r"NOT this seat`s:\s+\S+\s+L\d+\s+\w+\s+(r\d{4}|Merge|\S+)",
                                             _out12_before)))
_rc12_after, _out12_after = run_live(S12)
print(f'      the pre-repair source on THIS tree: rc={_rc12_before}, loss side {_loss}; '
      f'the repaired source: rc={_rc12_after}')
gate(f'Ⓑ① ⛔⛭⛭⛭ ** THE BOUND WAS A PREDICTION AND IT IS BROKEN BY ANOTHER SEAT\'S WORK: ** the '
     f'pre-repair source exits `{_rc12_before}` on this tree with the loss side at `{_loss}` against '
     f'its asserted `under 10`, and the repaired source exits `{_rc12_after}`.  *The loss side is the '
     f'claim-sites inside this seat\'s own directories whose LAST WRITER is not this seat, so every '
     f'legitimate edit another seat makes to one of this seat\'s receipts adds one* --- ** and no '
     f'work of this seat\'s can lower it, which is what makes a standing bound on it the wrong shape **',
     _rc12_before != 0 and _loss >= 10 and _rc12_after == 0)

_m2 = re.search(r"the loss side by LAST WRITER's parity:\s*(\{[^}]*\})", _out12_after)
_odd = int(re.search(r"'ODD':\s*(\d+)", _m2.group(1)).group(1)) if _m2 else -1
_norev = int(re.search(r"'no-rev':\s*(\d+)", _m2.group(1)).group(1)) if _m2 and 'no-rev' in _m2.group(1) else 0
print(f'      the repaired source reports the split: ODD {_odd}, no-rev {_norev}')
gate(f'Ⓑ② ⛭⛭ and the repair REPORTS who moved it instead of bounding it: `{_odd}` of the loss side '
     f'was last written by the other line and `{_norev}` arrived with no revision id at all.  ** The '
     f'split is PRINTED and not asserted, because `no EVEN` there is true by construction and a '
     f'definitional truth presented as a finding is the hollow form the corpus already lints for.  '
     f'⇒ What it tells a reader is the proportion that is a TRANSFER against the proportion that is '
     f'a GAP --- only the second is a gap, and `r7241`\'s own parity rule has no bucket for it **',
     _odd > 0 and _odd + _norev == _loss)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  AND CI COULD NOT HAVE FOUND THE SECOND ONE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
#: ⛔⛭⛭ The scoped suite's scope is `what this push can have changed`.  That is the right scope for a
#:   push's own blast radius and the wrong one for a receipt whose subject ANOTHER seat moved.
_s2_touched = [f for f in _git('diff', '--name-only', f'{S2_BEFORE}~1', S2_BEFORE).split('\n') if f]
_s12_window = [f for f in _git('diff', '--name-only', S2_BEFORE, S12_BEFORE).split('\n') if f]
_s12_in_its_own_breaking_push = S12 in _s12_window
print(f'      the push that landed the first repair touched {len(_s2_touched)} path(s); '
      f'S12 among the paths of the push on which it was already broken: '
      f'{_s12_in_its_own_breaking_push}')
gate(f'Ⓒ① ⛔⛭⛭⛭ ** AND THE SECOND DEFECT WAS OUTSIDE EVERY SCOPE KEYED ON THIS SEAT\'S DIFF: ** `S12` '
     f'was already broken at `{S12_BEFORE}` and is NOT among that push\'s own changed paths '
     f'(`{not _s12_in_its_own_breaking_push}`), so the scoped suite --- whose scope is what a push '
     f'CAN HAVE CHANGED --- had no reason to run it.  *It was found by widening this seat\'s own '
     f'sweep from the receipts a revision TOUCHES to EVERY receipt in its directory.*  ⇒ ** That is '
     f'`r7298`\'s ruling one level out: a blast radius must be measured over every KIND of thing a '
     f'change can reach, and the kind still missing was ANOTHER SEAT\'S change, which reaches this '
     f'seat\'s receipts while nothing in this seat\'s diff points at them **',
     not _s12_in_its_own_breaking_push and len(_s2_touched) > 0)

_dir = os.path.join(ROOT, 'receipts', 'L_probability')
_n_dir = len([f for f in os.listdir(_dir) if f.endswith('.py')])
_mine_elsewhere = len({c[0] for c in _led if '+60' in (c[6] or '')
                       and not c[0].startswith('receipts/L_probability/')})
print(f'      the widened sweep covers {_n_dir} receipt(s) in this seat\'s directory; '
      f'rows this seat verdicted that live OUTSIDE it: {_mine_elsewhere} receipt(s)')
gate(f'Ⓒ② ⌗⛭ and the widening is REPORTED with what it still misses rather than claimed complete: it '
     f'covers the `{_n_dir}` receipts in this seat\'s own directory, while `{_mine_elsewhere}` '
     f'receipts outside it carry rows this seat verdicted.  ** A sweep scoped by PATH has the same '
     f'shape of gap as the count `S12` was repaired of, which was scoped by path and should have '
     f'been scoped by last writer --- named here rather than closed, because closing it reads other '
     f'seats\' receipts **',
     _mine_elsewhere > 0 and _n_dir > 20)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted({f for f in (_git('diff', '--name-only', f'{S2_BEFORE}~1', AFTER) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n')
                   if f.endswith('.py') and f.startswith('receipts/')})
_foreign = [f for f in _touched if not f.startswith('receipts/L_probability/')]
print(f'      receipts touched across the two repairs: {len(_touched)}; outside this seat\'s '
      f'directory: {len(_foreign)}')
gate(f'Ⓓ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE alone: `{len(_touched)}` receipts are touched '
     f'across both repairs and `{len(_foreign)}` of them sits outside this seat\'s own directory.  '
     f'** One of the two repaired gates carries `cc66`\'s own condition and its note, and BOTH are '
     f'kept untouched --- the repair is to the report beside them, because a predicate another seat '
     f'wrote under the exception is not this seat\'s to restate **',
     not _foreign and len(_touched) >= 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** A RECEIPT CRASHED BECAUSE THE CAMPAIGN FINISHED. ** The bare UNADJUDICATED bucket is {len(_bare)}
     and the report divided by it, so the output was undefined exactly when the work was done --
     and a crash reports no failing gate at all.
  ⛔ ** AND THE TWO HALVES OF THAT GATE HAD BEEN REPAIRED APART: ** the condition was made monotone
     for this very reason, with the reason written beside it, and the report went on dividing.
  ⛔ ** A PREDICTION WAS LEFT STANDING AS A BOUND ** on the one count only another seat can move:
     {_loss} against an asserted 10, {_odd} of it last written by the other line.
  ⛭ ** AND CI COULD NOT HAVE FOUND THE SECOND: ** its scope is what a push can have changed, and
     the push that broke it was not this seat's. Each of the two needed a different widening of
     what gets RUN, and neither was found by reading.
""")
sys.exit(1 if FAILURES else 0)
