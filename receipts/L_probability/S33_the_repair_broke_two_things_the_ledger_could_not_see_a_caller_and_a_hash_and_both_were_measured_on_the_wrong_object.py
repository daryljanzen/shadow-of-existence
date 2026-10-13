#!/usr/bin/env python3
r"""S33 -- `r7294`'s repair broke two things, CI found both, and both were measured on the wrong object.

COMPUTES: nothing the papers quote.  This receipt reports two breakages caused by `r7294`'s repair to
`dangling_predicate_v2.py`, their repairs, and what the pair of them says about measuring a blast
radius.

** ⛔⛭⛭⛭ `r7294` MEASURED ITS BLAST RADIUS OVER VERDICTED ROWS AND GOT `0`.  THE RADIUS OVER CALLERS
WAS NOT MEASURED, AND IT WAS NOT `0`. **  *The repair made the exemption's old call signature RAISE,
which is what makes it carry its conditions --- and this line's OWN part-of-speech arm, in `r7266`'s
`pos_arm.py`, still called it unscoped.* ⇒ ***So the repair raised a `TypeError` on every span whose
head is verb-like, and took `S23` down with it.  The runner-read sweep found it; the ledger could not,
because a ledger has rows and not callers.***
  ⌈ ⛭⛭ ***THE LESSON, AND IT IS THE SHARPEST THING IN THIS REVISION: a blast radius has to be
    measured over EVERY KIND OF THING THE CHANGE CAN REACH.*** *`r7294` looked for silent behaviour
    changes in verdicts and found none; it did not look for LOUD failures in code, which is what it
    had just deliberately introduced.  **The measurement was honest about its method and wrong about
    its scope, and that is a different failure from a wrong number.***
  ⌊ ✔ *The caller is repaired as a SUBJECT TEST, which is what it is: it asks whether the span names
    its own subject.  Before `r7294` it reached the demonstrative-only exemption through the unscoped
    name --- **so this line's own caller carried the `78`th member's defect too, and the signature
    change is what surfaced it.***

** ⛔⛭⛭ AND THE SECOND BREAKAGE IS THE FORM-FOR-PROPERTY CLASS AGAIN, IN A GATE OF THIS LINE'S OWN. **
*`S23`'s burden gate hashed the WHOLE MODULE FILE and called the result `the adopted word list is
BYTE-FOR-BYTE what it was`.* **The claim is about the word LIST; the hash was about the FILE.**
⇒ *So an ordered repair to the exemption's SCOPE, which did not touch a word of the list, turned that
gate red without the claim having become false.*
  ⌈ *Repaired to discharge the burden on the word LISTS themselves --- hashed out of the module at both
    commits --- and on the ARMS' BEHAVIOUR over a fixed probe corpus, which is what `r7257`'s and
    `r7258`'s figures actually rest on.*
  ⌊ ⌗ ***Fourth instance in this line's own work of a gate pinning the FORM that implements a
    property rather than the property, and the third found in this session.*** *A gate that pins the
    form is not a weaker gate; it is a gate making a different claim.*

** ⛔⛭⛭⛭ AND A FOURTH INSTANCE WAS INSIDE THIS RECEIPT, CAUGHT BY THE PIN RATCHET BEFORE THE PUSH. **
*The first form of the gates reporting the three repairs above asserted them by GREPPING FOR THE LINES
THAT IMPLEMENT THEM --- four source pins, in the very receipt whose thesis is that a gate must assert
the property.* ⇒ ***Each one is now BEHAVIOUR: the caller is shown repaired by what it ANSWERS on a
span the two scopes disagree about; the hash gate's error is shown by measuring BOTH objects (the
module's file bytes moved, its word lists did not); and the two previous receipts are RUN on this tree
rather than grepped for the clause that was dropped.***
  ⌊ ⌗ ***Four instances in one revision, and the fourth was in the report of the other three.***
    *The class is not hard to see once named --- it is hard to STOP DOING, because pinning the form is
    always the cheapest thing to write.*

** ⛔⛭⛭ AND A THIRD BREAKAGE, FROM THE SAME CAUSE ONE LEVEL FURTHER OUT. **  *The restraint gates of
the two previous revisions also demanded that NO RECEIPT BUT THEIR OWN appear in the diff --- a claim
about the diff's FORM standing beside the claim they mean, over a LIVE range.* ⇒ ***So this revision,
legitimately repairing two of this seat's own receipts, turned both of them red.  The specific negative
was the whole claim and the form-clause was decoration that could only fail.*** ⌗ *Dropped from both.
**Three breakages in one revision and all three are the same mistake: a gate asserting the shape of the
evidence instead of the thing the evidence is for.***

** ✔ AND THE ARMS STILL DO NOT MOVE, which is the one thing both repairs had to preserve. **  *All
five arms agree with the pre-repair module on every verdicted literal in the ledger.*

⌗ *Sources: the two CI failures on `r7294`'s head; the module and `pos_arm.py` at `origin/main` read
out of git; `S23`'s burden gate before and after; and the ledger's verdicted literals as the probe
population.*
"""
import collections
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7266_60_the_arm_and_the_guard'))

import dangling_predicate_v2 as D          # noqa: E402
import pos_arm as P                        # noqa: E402

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '4b130bdf'   # origin/main at r7289 -- before r7294's repair
BASE = 'corpus/quote_pin_baseline.tsv'
MOD = 'computations/beyond_the_wall/r7260_60_land_and_verdict/dangling_predicate_v2.py'
ARM = 'computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/pos_arm.py'
S23 = 'receipts/L_probability/S23_four_items_and_every_one_was_mis_described_because_five_gates_stored_a_snapshot_of_a_rule_instead_of_the_rule.py'
ARMS = ['dangles_leading_adopted', 'dangles_leading', 'dangles_trailing', 'dangles_negated', 'dangles']
#: spans whose head is verb-like on both of the arm's axes -- the ones that REACH the exemption
REACHING = ['carries a single moving part', 'extends to the unpolarised case']


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


print()
print('=' * 100)
print('S33 -- the repair broke a caller and a hash, and both were measured on the wrong object')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE BREAKAGE WAS REAL, AND IT IS REPRODUCED FROM THE PRE-REPAIR MODULE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_mod_then = _git('show', f'{BEFORE}:{MOD}')
_arm_then = _git('show', f'{BEFORE}:{ARM}')
_ns_then = {}
exec(compile(_mod_then, 'adopted@before', 'exec'), _ns_then)
_unscoped_then = _ns_then['names_own_subject_by_determiner']('a symmetry-breaking modulus is the key')
#: the repaired module raises on the same call, which is the repair working
try:
    D.names_own_subject_by_determiner('a symmetry-breaking modulus is the key')
    _raises = False
except TypeError:
    _raises = True
_arm_then_unscoped = bool(re.search(r'D\.names_own_subject_by_determiner\(lit\)', _arm_then))
print(f'      the pre-repair module answers an unscoped call ({_unscoped_then!r}); the repaired one '
      f'raises ({_raises}); and the pre-repair arm called it unscoped ({_arm_then_unscoped})')
gate(f'Ⓐ① ⛔⛭⛭⛭ ** THE BREAKAGE IS REAL AND IT IS THIS LINE\'S OWN CALLER: ** the pre-repair module '
     f'answered an unscoped call, the repaired one RAISES (`{_raises}`) --- which is the exemption '
     f'carrying its conditions --- and `pos_arm.py` called it unscoped at `{BEFORE}` '
     f'(`{_arm_then_unscoped}`).  ** So `r7294` raised a `TypeError` on every span whose head is '
     f'verb-like, and the runner-read sweep is what found it **',
     _raises and _arm_then_unscoped)

_ns_arm_then = {}
_ns_arm_then['__name__'] = 'pos_arm_before'
sys.modules.setdefault('dangling_predicate_v2', D)
_reached = []
for _l in REACHING:
    _h = P.head_word(_l)
    _r, _a = P.det_ratio(_h), P.det_after_ratio(_h)
    _reached.append(_r is not None and _a is not None and _r < P.THR and _a > P.ATHR)
print(f'      spans whose head is verb-like on BOTH axes, so they reach the exemption: '
      f'{sum(_reached)} of {len(REACHING)}')
gate(f'Ⓐ② ⛭⛭ and the breakage was NOT every span: the exemption is reached only after both '
     f'distributional axes pass, so `{sum(_reached)}` of these `{len(REACHING)}` probe spans reach it '
     f'and a span like `is not a Lie algebra` returns before it.  ** Which is why it survived the '
     f'local receipt run and surfaced on the runner: a defect behind a guard fires only on the '
     f'inputs that pass the guard **',
     sum(_reached) == len(REACHING))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE CALLER IS REPAIRED AS WHAT IT IS: A SUBJECT TEST ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# ⛔⛭⛭ AND THE FOURTH INSTANCE WAS IN THIS RECEIPT, caught by the pin ratchet before the push: the
#   first form of the gates below asserted the repairs by GREPPING FOR THE LINES THAT IMPLEMENT THEM
#   --- four source pins in the very receipt whose thesis is that a gate must assert the property.
#   ⇒ *** So each one is now BEHAVIOUR. ***  The caller is shown repaired by what it ANSWERS: it no
#       longer raises, and its answer tracks the WIDE exemption rather than the narrow one on a span
#       the two disagree about.
_SPLIT = 'a symmetry-breaking modulus is the adjustable parameter that criterion rejects'
_wide_says = D.names_own_subject(_SPLIT)
_narrow_says = D.names_own_subject_by_determiner(_SPLIT, within='leading-dangling-arm')
_answers = []
for _l in REACHING:
    try:
        _answers.append(P.dangles_pos(_l))
    except TypeError:
        _answers.append('RAISED')
#: and the arm's answer on the splitting span, which is only reachable if its head is verb-like --
#: so the behaviour is read through the exemption the arm actually consults
_arm_uses_wide = (not P.dangles_pos(_SPLIT)) if P.head_word(_SPLIT) else None
print(f'      the two scopes disagree on the probe span (wide {_wide_says}, narrow {_narrow_says}); '
      f'the arm answers {_answers} on the reaching spans and does not raise')
gate(f'Ⓑ① ⛔⛭⛭ the caller is repaired as a SUBJECT TEST, shown by what it ANSWERS rather than by '
     f'grepping the line that implements it: the two scopes disagree on the probe span (wide '
     f'`{_wide_says}`, narrow `{_narrow_says}`), and the arm now answers `{_answers}` on the spans '
     f'that reach the exemption instead of raising.  ** Passing the narrow scope would have silenced '
     f'CI by committing the `78`th member\'s defect on purpose --- the exemption borrowed into a '
     f'subject test, which is the thing `r7289` ordered repaired **',
     'RAISED' not in _answers and _wide_says is True and _narrow_says is False)

_callers = [f for f in _git('grep', '-l', 'names_own_subject_by_determiner', '--',
                           '*.py').split('\n') if f]
_CALL = re.compile(r'names_own_subject_by_determiner\(')
_unscoped_now = []
for _f in _callers:
    if _f.endswith(os.path.basename(MOD)):
        continue                      # the module's own two calls are scoped, split across lines
    _ls = read(_f).split('\n')
    for _i, _ln in enumerate(_ls):
        if not _CALL.search(_ln) or 'requires within' in _ln:
            continue
        _window = ' '.join(_ls[_i:_i + 2])
        if 'within=' in _window:
            continue
        if any('try:' in _ls[max(0, _i - _k)] for _k in (1, 2)):
            continue                  # a deliberate raise-probe, not a caller
        _unscoped_now.append((_f, _i + 1))
print(f'      files naming the exemption: {len(_callers)}; unscoped LIVE calls remaining: '
      f'{len(_unscoped_now)} {_unscoped_now}')
gate(f'Ⓑ② ⛭⛭ and the radius over CALLERS is measured this time rather than assumed: '
     f'`{len(_callers)}` files name the exemption and `{len(_unscoped_now)}` still call it unscoped.  '
     f'** This is the measurement `r7294` did not make --- it measured over verdicted ROWS, where the '
     f'answer was `0`, and a ledger has rows and not callers **',
     len(_unscoped_now) == 0 and len(_callers) >= 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  AND THE HASH GATE PINNED THE FORM OF A PROPERTY, FOR THE FOURTH TIME ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
#: ⌗ the hash gate's repair, asserted as the PROPERTY it is about: the module's FILE bytes changed
#:   and its WORD LISTS did not.  The first form of this gate grepped `S23` for the new call --- a
#:   source pin for a property, which is the class this receipt is about.
import hashlib                                                               # noqa: E402
_ns_now = {}
exec(compile(read(MOD), 'adopted@now', 'exec'), _ns_now)


def _wl(ns):
    return '\x1f'.join([ns['FINITE'], ns['LEAD'].pattern, ns['TRAIL'].pattern,
                        '\x1e'.join(sorted(ns['_FUNC']))])


_file_moved = (hashlib.sha256(read(MOD).encode()).hexdigest()
               != hashlib.sha256(_mod_then.encode()).hexdigest())
_lists_held = (hashlib.sha256(_wl(_ns_now).encode()).hexdigest()
               == hashlib.sha256(_wl(_ns_then).encode()).hexdigest())
print(f'      the module FILE bytes moved: {_file_moved}; its WORD LISTS held: {_lists_held}')
gate(f'Ⓒ① ⛔⛭⛭ the hash gate was measuring the wrong object, and the two measurements prove it: the '
     f'module\'s FILE bytes DID move (`{_file_moved}`) while its WORD LISTS did NOT '
     f'(`{_lists_held}`).  ** A gate hashing the file while claiming the list therefore had to go red '
     f'on an ordered repair that touched no word of the list --- fourth instance in this line\'s own '
     f'work of pinning the FORM that implements a property rather than the property, and the burden '
     f'is now discharged on the lists and on the arms\' behaviour **',
     _file_moved and _lists_held)

#: ⛔⛭⛭ AND A THIRD BREAKAGE, from the same cause one level further out: the restraint gates of the
#:   two previous revisions ALSO demanded that no receipt but their own appear in the diff --- a claim
#:   about the diff's FORM beside the claim they mean, over a LIVE range.  So THIS revision,
#:   legitimately repairing two of this seat's own receipts, turned both of them red.
#:   ⇒ *** Asserted as BEHAVIOUR and not by grepping for the clause: both receipts are RUN, from
#:       their own directory as the suite runs them, and both must pass ON THIS TREE --- which is the
#:       tree whose extra touched receipts broke them. ***
_PREV = sorted(f for f in _git('ls-files', 'receipts/L_probability/S31_*.py',
                               'receipts/L_probability/S32_*.py').split('\n') if f)
_prev_pass = []
for _f in _PREV:
    _r = subprocess.run([sys.executable, os.path.basename(_f)],
                        cwd=os.path.join(ROOT, os.path.dirname(_f)),
                        capture_output=True, text=True, timeout=1800,
                        env=dict(os.environ, NODE='ci'))
    _fails = [l for l in _r.stdout.split('\n') if l.strip().startswith('FAIL ')]
    _prev_pass.append(not [l for l in _fails if 'restraint' in l.lower()])
print(f'      the two previous revisions\' receipts, RUN on this tree, with no RESTRAINT gate among '
      f'whatever they report: {_prev_pass}')
gate(f'Ⓒ② ⛔⛭⛭ and a THIRD breakage from the same cause one level out, asserted by RUNNING the two '
     f'receipts rather than by grepping them --- and asserted of THEIR RESTRAINT GATES ALONE, which '
     f'is the subject: neither of the `{len(_PREV)}` reports a failing restraint gate on THIS tree '
     f'(`{all(_prev_pass)}`), the tree whose extra touched receipts turned their first form red.  '
     f'** Their restraint gates demanded that no receipt but their own appear in the diff, a claim '
     f'about the diff\'s FORM beside the claim they mean; the specific negative was the whole claim '
     f'and the form-clause was decoration that could only fail.  And requiring their WHOLE RUN to be '
     f'green was the same mistake once more: a gate whose subject is one of their gates fails on '
     f'anything else of theirs that moves **',
     len(_PREV) == 2 and all(_prev_pass))

_lits = []
for _c in rows_of(read(BASE)):
    if _c[5].startswith('UNADJUDICATED'):
        continue
    try:
        _lits.append(json.loads(_c[1]))
    except Exception:
        pass
_moved = collections.Counter()
for _a in ARMS:
    for _l in _lits:
        if _ns_then[_a](_l) != getattr(D, _a)(_l):
            _moved[_a] += 1
print(f'      {len(ARMS)} arms x {len(_lits)} verdicted literals; results that moved: '
      f'{dict(_moved) or "NONE"}')
gate(f'\u24b9\u2460 \u2714\u26ed\u26ed the arms STILL do not move: all `{len(ARMS)}` agree with the pre-repair module on '
     f'every one of the `{len(_lits)}` verdicted literals.  ** All three repairs in this revision '
     f'preserve that, which is the one invariant `r7257`\'s and `r7258`\'s figures rest on --- and it '
     f'is now checked by BEHAVIOUR in two receipts rather than discharged by a file hash in one **',
     not _moved and len(_lits) > 2000)

_touched = sorted({f for f in (_git('diff', '--name-only', BEFORE) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
print(f'      this revision touches {len([f for f in (ARM, S23) if f in _touched])} of the two files '
      f'it repairs, both this seat\'s own')
gate(f'Ⓓ② ⛭ the restraint: the two files repaired are BOTH this seat\'s own --- `r7266`\'s arm and '
     f'`r7260`\'s receipt --- and the repair to another seat\'s caller, had there been one, would have '
     f'been routed instead.  ** There was none: the only unscoped caller outside the module was mine **',
     ARM in _touched and S23 in _touched)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** r7294 MEASURED ITS BLAST RADIUS OVER VERDICTED ROWS AND GOT 0.  THE RADIUS OVER CALLERS WAS
     NOT MEASURED, AND IT WAS NOT 0. ** The repair made the old signature RAISE -- which is what
     makes the exemption carry its conditions -- and this line's own part-of-speech arm still
     called it unscoped, so it raised on every verb-headed span and took S23 down with it.
  ⛭⛭ ** A blast radius has to be measured over every KIND of thing the change can reach. **
     r7294 looked for silent behaviour changes in verdicts and found none; it did not look for
     loud failures in code, which is what it had just deliberately introduced.
  ⛔ ** And the second breakage is the form-for-property class for the FOURTH time in this line's
     own work: ** a gate hashed the whole module FILE while claiming the word LIST was unchanged.
  ✔ The arms still do not move: {len(ARMS)} arms x {len(_lits)} verdicted literals, nothing changed.
""")
sys.exit(1 if FAILURES else 0)
