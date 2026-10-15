#!/usr/bin/env python3
r"""S29 -- `L271_the_statistics_bake` read on this seat's own pick, with the mode called in advance.

COMPUTES: nothing the papers quote.  This receipt reports the adjudication of `29` quote-pin keys and
scores a pre-registration pushed before the first of them was opened.

** CROSS-REF: the pre-registration is `computations/beyond_the_wall/r7290_60_the_tier_mix/PREDICTION.md`,
pushed at `20135e9c` BEFORE any key was read, and this receipt reads its numbers OUT of that file
rather than restating them. **

** ⛔⛭⛭⛭ THE HEADLINE CALL IS REFUTED, AND IT IS THE OUTCOME THE PRE-REGISTRATION NAMED AS THE ONE
AGAINST THIS SEAT: `17.2` PER CENT `REPAIR-OWED` AGAINST A CALLED `50` OR ABOVE. **  *This seat
corrected at `r7288` the very application the crossed read found it under-applying, then picked its own
prefix, called HIGH in advance, and came back in its own low mode anyway.* ⇒ ***So `r7288`'s
explanation for the seat effect is removed rather than confirmed: the under-application was real and
it was not what produced the mode.***

** ⛭⛭⛭ BUT THE MECHANISM IS VISIBLE HERE AND IT IS NOT THE READER: `23` OF THE `29` KEYS CANNOT TAKE
`REPAIR-OWED` BY CONSTRUCTION. **  *`12` are read at a LITERAL COMMIT (`48e55a6b^`, `r4111`'s parent)
and `11` assert that a term is ABSENT from the seventeen paper bodies.  **No seat can move a read at a
literal commit, and no reword can break an absence probe.***
  ⌈ ⛭⛭ ***AND THE PIN IS THE REPAIR, LANDED IN ADVANCE RATHER THAN OWED:*** *`11` of those `12`
    literals are GONE from the live paper, which was restated out from under this receipt at `r4111`.
    **The receipt would be red today on every one of them if it had not pinned.**  A `REPAIR-OWED`
    verdict on those rows would name work that is already done.*
  ⌊ ⇒ ***So there is a THIRD explanation for the mode, and neither `r7283`'s (a property of the
    corpus) nor `r7285`'s (a property of the seat) can see it: the share of a prefix's keys that are
    STRUCTURALLY unable to take the verdict.*** *Both earlier designs were measured on prefixes of
    live reads, where that share is near zero.*

** ⛔⛭⛭⛭ AND THE PREDICTOR THAT WOULD HAVE EXPLAINED IT IS REFUTED AT SPEARMAN `-0.02` ACROSS `28`
PREFIXES --- IN THIS REVISION, BEFORE IT WAS EVER CLAIMED. **  *The ledger's own `PINNED` flag share
does not predict the mode: `L207_the_bend` is the highest `REPAIR-OWED` prefix in the corpus at `76.9`
per cent and carries one of the highest `PINNED` shares at `35.0`.*
  ⌈ ⌗ ***Third mechanical predictor to fail on this problem*** --- *after `was the paper rewritten
    under this prefix` (`r7284`, this seat's) and the `PAPER`/`SOURCE` column (`r7287`, at Spearman
    `+0.49`).*  **And the first this line refuted in the revision that built it rather than in the one
    after**, which is the only thing that keeps the count from being three mistakes.
  ⌊ ⛔ *What survives is narrower and is not a predictor: `L271` is low because of what its
    receipts DO, and that fact does not generalise to a prefix whose reads are live.*

** ⛔⛭⛭ AND THE PRE-REGISTRATION IS REFUTED TWICE MORE, ON ITS OWN TERMS. **  *① Its tier arithmetic
was wrong: it claimed `22` `TOKEN` and `7` `SENTENCE` where the ledger carries `20` and `9` --- the
count the whole argument rested on, wrong by two in each direction, with the band holding by luck.
② And it missed the prefix's LARGEST class entirely: `NOT-A-PIN` at `37.9` per cent appears in none of
its four bands.* ⇒ ***A pre-registration that names the wrong classes cannot be scored on the class
that turns out to matter, and that is a defect in the registration and not in the result.***

** ⛔⛭⛭ AND A SIXTH INSTANCE OF THIS LINE'S OWN FAIL-ON-SUCCESS CLASS, FOUND BY THIS REVISION
BREAKING THE PREVIOUS ONE'S GATE. **  *`r7288`'s restraint gate selected its revision's commits by
searching their messages for its own revision NUMBER.  **This revision cited `r7288` in a commit
message --- the ordinary thing to do in this corpus --- and so entered that filter, putting this
receipt into `r7288`'s file set and turning its restraint red.***
  ⌈ ⇒ ***A selector over a LIVE RANGE cannot be made safe by filtering what it matches, when the
    corpus's own convention is to cite revisions by number.*** *The repair in both receipts is to stop
    selecting commits at all and state the claim as the SPECIFIC NEGATIVE it always was: **none of the
    receipts whose rows this revision verdicted was touched.** That cannot be broken by a later
    revision landing its own receipt.*
  ⌊ ⌗ *Twice in one gate inside two revisions --- a dropped record separator, then a citation --- and
    both times the claim was weaker than the sentence describing it. The sentence was always the
    better gate.*

⌗ *`29` landed, `502` remain.  The prefix was picked by this seat with the reason stated, no order
being outstanding; the three called numbers are read out of the pushed file at the commit that pushed
it, and the second call --- that the subject rule would reach at most a sixth of the prefix --- held
for the stronger reason that it reached NONE of it: every one of the `5` `REPAIR-OWED` rows is a
narrower-than-claim ground.*
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

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '20135e9c'   # the commit that PUSHED the pre-registration, before the first key was opened
AFTER = 'db791aad'    # the commit that carried this revision's verdicts -- the 71st member's corollary
# ⚠ Every COUNT below is read at `AFTER` rather than in the working tree: an equality on a LIVE
# ledger goes red the moment another seat legitimately re-verdicts any row, which is the class
# `check_exact_counts` exists for.  The pre-registration is read at `BEFORE`, where it was pushed.
# The one live read kept is the backlog, and it is MONOTONE.
PIN = '48e55a6b^'     # the commit L271/S2 reads its superseded figures at -- r4111's parent
BASE = 'corpus/quote_pin_baseline.tsv'
PRED = 'computations/beyond_the_wall/r7290_60_the_tier_mix/PREDICTION.md'
PFX = 'receipts/L271_the_statistics_bake/'


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 6 and c[0].startswith('receipts/')]


def flat(t):
    return re.sub(r'\s+', ' ', t)


print()
print('=' * 100)
print("S29 -- L271 read on this seat's own pick, and the mode called in advance was wrong again")
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE PRE-REGISTRATION CAME FIRST, AND IT IS READ RATHER THAN RESTATED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                      capture_output=True).returncode == 0
_anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                      capture_output=True).returncode == 0
_pred_then = _git('show', f'{BEFORE}:{PRED}')
_before_rows = {(c[0], c[1]): c[5] for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))}
_keys = [k for k in _before_rows if k[0].startswith(PFX) and _before_rows[k].startswith('UNADJUDICATED')]
gate(f'Ⓐ① ⛔⛭⛭ the pre-registration EXISTS at a literal sha (`{BEFORE}`, resolves `{_res}`, ancestor '
     f'`{_anc}`) and at that commit all `{len(_keys)}` of this prefix\'s keys were still '
     f'`UNADJUDICATED` --- so the call was made before the read and not after it, which is the whole '
     f'design and is checkable by anyone from the history alone',
     _res and _anc and len(_pred_then) > 2000 and len(_keys) == 29)

# the called values, parsed OUT of the pushed file
_called = {
    'overall': re.search(r'overall `REPAIR-OWED` share \| \*\*HIGH --- at or above `(\d+)` per cent',
                         _pred_then.replace('—', '---')),
    'subject': re.search(r'\*\*at or below `(\d+)` per cent of the `29`\*\*', _pred_then),
    'held': re.search(r'\*\*BELOW `(\d+)` per cent\*\*', _pred_then),
}
_tier_claim = re.search(r'\*\*`(\d+)` of the `29` are `TOKEN` tier and `(\d+)` are `SENTENCE`\*\*',
                        _pred_then)
gate(f'Ⓐ② ✔⛭ and the three called numbers are READ out of that commit\'s copy of the file --- '
     f'overall at or above `{_called["overall"].group(1) if _called["overall"] else "?"}` per cent, '
     f'subject-rule at or below `{_called["subject"].group(1) if _called["subject"] else "?"}`, '
     f'`MEANING-HELD` below `{_called["held"].group(1) if _called["held"] else "?"}` --- rather than '
     f'retyped into this docstring where they could be adjusted after the fact',
     all(_called.values()) and _tier_claim is not None)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE SCORE, AND THE HEADLINE CALL IS REFUTED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_after_led = _git('show', f'{AFTER}:{BASE}')
_now = {(c[0], c[1]): (c[5], c[6] if len(c) > 6 else '') for c in rows_of(_after_led)}
_mine = {k: _now[k] for k in _keys}
_tally = collections.Counter(v[0] for v in _mine.values())
_n = len(_mine)
_ro = 100.0 * _tally['REPAIR-OWED'] / _n
_mh = 100.0 * _tally['MEANING-HELD'] / _n
_de = 100.0 * _tally['DELIBERATE'] / _n
_na = 100.0 * _tally['NOT-A-PIN'] / _n
print(f'      {_n} keys: ' + ', '.join(f'{k} {v}' for k, v in sorted(_tally.items())))
print(f'      REPAIR-OWED {_ro:.1f}%  MEANING-HELD {_mh:.1f}%  DELIBERATE {_de:.1f}%  '
      f'NOT-A-PIN {_na:.1f}%')
_called_floor = float(_called['overall'].group(1))
gate(f'Ⓑ① ⛔⛭⛭⛭ ** THE HIGH CALL IS REFUTED: `{_ro:.1f}` PER CENT `REPAIR-OWED` AGAINST A CALLED '
     f'`{_called_floor:.0f}` OR ABOVE ** --- and the pre-registration named this outcome as the one '
     f'that goes against this seat: ** it removes the explanation `r7288` offered. ** This seat '
     f'corrected the very application the crossed read found wrong, picked its own prefix, called '
     f'HIGH, and came back in its own low mode anyway',
     _ro < _called_floor)

_sub = [k for k, v in _mine.items() if v[0] == 'REPAIR-OWED' and 'subject rule' in v[1]
        and 'NOT owed on the subject rule' not in v[1]]
_grounds = collections.Counter(
    ('CO-OCCURRENCE' if 'CO-OCCURRENCE' in v[1] else
     'UNDECIDING-ALT' if 'UNDECIDING ALT' in v[1] else
     'PROXY' if 'PROXY' in v[1] else 'OTHER')
    for k, v in _mine.items() if v[0] == 'REPAIR-OWED')
_sub_share = 100.0 * len(_sub) / _n
print(f'      the {_tally["REPAIR-OWED"]} REPAIR-OWED rows by ground: ' +
      ', '.join(f'{k} {v}' for k, v in sorted(_grounds.items())))
gate(f'Ⓑ② ⛭⛭ and the SECOND call holds for a reason worth more than the band: the subject-rule share '
     f'is `{_sub_share:.1f}` per cent against a called `at or below '
     f'{_called["subject"].group(1)}` --- ** NOT ONE of the `{_tally["REPAIR-OWED"]}` `REPAIR-OWED` '
     f'rows is owed on the subject rule. ** Every one is a narrower-than-claim ground: '
     f'{", ".join(f"{k} {v}" for k, v in sorted(_grounds.items()))}',
     _sub_share <= float(_called['subject'].group(1)) and len(_sub) == 0
     and _grounds['OTHER'] == 0)

gate(f'Ⓑ③ ✔⛭ and the two remaining bands hold: `MEANING-HELD` `{_mh:.1f}` per cent against a called '
     f'below `{_called["held"].group(1)}`, `DELIBERATE` `{_de:.1f}` inside `10`-`45` --- so the call '
     f'was wrong on its headline and right on its structure, which is the shape a pre-registration '
     f'is for',
     _mh < float(_called['held'].group(1)) and 10 <= _de <= 45)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  AND THE MECHANISM IS NOT THE READER: 23 OF THE 29 CANNOT TAKE THE VERDICT AT ALL ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_pinned = [k for k, v in _mine.items() if v[0] == 'DELIBERATE' and 'PINNED COMMIT' in v[1]]
_absence = [k for k, v in _mine.items() if v[0] == 'NOT-A-PIN' and 'ABSENCE PROBE' in v[1]]
_unreachable = len(_pinned) + len(_absence)
print(f'      pinned reads {len(_pinned)}, absence probes {len(_absence)}, '
      f'unreachable by REPAIR-OWED {_unreachable} of {_n}')
gate(f'Ⓒ① ⛔⛭⛭⛭ ** `{_unreachable}` OF THE `{_n}` CANNOT TAKE `REPAIR-OWED` BY CONSTRUCTION ** --- '
     f'`{len(_pinned)}` are read at a LITERAL COMMIT, which no seat can move, and `{len(_absence)}` '
     f'assert a term is ABSENT, which no reword can break.  ⇒ *** So this prefix\'s low mode is a '
     f'property of its RECEIPTS and not of its reader --- a third explanation, and neither '
     f'`r7283`\'s (the corpus) nor `r7285`\'s (the seat) can see it, because both were measured on '
     f'prefixes of LIVE reads ***',
     _unreachable >= 20 and len(_pinned) == 12 and len(_absence) == 11)

# and the pin is the repair, landed in advance -- shown by the paper having moved out from under it
_lits = [json.loads(k[1]) for k in _pinned]
_then = flat(_git('show', f'{PIN}:corpus/CR_cosmology.tex'))
_live = flat(read('corpus/CR_cosmology.tex'))
_at_pin = [l for l in _lits if flat(l) in _then]
_gone = [l for l in _lits if flat(l) not in _live]
_still = [l for l in _lits if flat(l) in _live]
print(f'      of the {len(_lits)} pinned literals: {len(_at_pin)} present at the pin, '
      f'{len(_gone)} absent from the LIVE paper')
gate(f'Ⓒ② ⛔⛭⛭⛭ and the pin is THE REPAIR, landed in advance rather than owed: all `{len(_at_pin)}` '
     f'of the `{len(_lits)}` pinned literals are present at `{PIN}` --- an immovable read --- while '
     f'`{len(_gone)}` of them are GONE from the live paper, which was restated out from under this '
     f'receipt at `r4111`.  ** A `REPAIR-OWED` verdict on these rows would name work already done: '
     f'the receipt would be red today on every one of them if it had not pinned **',
     len(_at_pin) == len(_lits) and len(_gone) >= 10)
print(f'      the {len(_still)} still live: {", ".join(_still) or "none"} --- flagged MULTI/SECSHARED '
      f'in the ledger, so it occurs in another section too')

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE THIRD MECHANICAL PREDICTOR, REFUTED BEFORE IT WAS CLAIMED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_all = rows_of(_after_led)
_per = collections.defaultdict(list)
for _r in _all:
    _per[_r[0].split('/')[1]].append(_r)
_pts = []
for _p, _rs in sorted(_per.items()):
    _v = [r for r in _rs if not r[5].startswith('UNADJUDICATED')]
    if len(_v) < 10:
        continue
    _pts.append((_p,
                 100.0 * sum(1 for r in _rs if 'PINNED' in (r[4] or '')) / len(_rs),
                 100.0 * sum(1 for r in _v if r[5] == 'REPAIR-OWED') / len(_v)))


def _rank(a):
    _s = sorted(range(len(a)), key=lambda i: a[i])
    _out = [0] * len(a)
    for _k, _i in enumerate(_s):
        _out[_i] = _k
    return _out


_rx, _ry = _rank([p[1] for p in _pts]), _rank([p[2] for p in _pts])
_m = len(_pts)
_rho = 1 - 6 * sum((_rx[i] - _ry[i]) ** 2 for i in range(_m)) / (_m * (_m * _m - 1))
_top = max(_pts, key=lambda p: p[2])
print(f'      {_m} prefixes with 10+ verdicted keys; Spearman(PINNED share, REPAIR-OWED share) '
      f'= {_rho:+.2f}')
print(f'      the highest REPAIR-OWED prefix is {_top[0]} at {_top[2]:.1f}% with a PINNED share of '
      f'{_top[1]:.1f}%')
gate(f'Ⓓ① ⛔⛭⛭⛭ ** THE PINNED-SHARE PREDICTOR IS REFUTED AT SPEARMAN `{_rho:+.2f}` ACROSS `{_m}` '
     f'PREFIXES, AND IT IS REFUTED HERE BEFORE IT WAS EVER CLAIMED. ** *`{_top[0]}` is the highest '
     f'`REPAIR-OWED` prefix in the corpus at `{_top[2]:.1f}` per cent AND carries one of the highest '
     f'`PINNED` shares at `{_top[1]:.1f}`* --- so what explains `L271` does not generalise.  ⇒ '
     f'*** THIRD mechanical predictor to fail on this problem, and the first this line refuted in '
     f'the revision that built it rather than in the one after ***',
     abs(_rho) <= 0.25 and _m >= 20)

_tok = sum(1 for k in _keys if _before_rows and True)
_tiers = collections.Counter(c[3] for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))
                             if (c[0], c[1]) in set(_keys))
_claimed_tok, _claimed_sent = int(_tier_claim.group(1)), int(_tier_claim.group(2))
print(f'      the tier mix as the ledger carries it: ' +
      ', '.join(f'{k} {v}' for k, v in sorted(_tiers.items())) +
      f'  --- the pre-registration claimed TOKEN {_claimed_tok}, SENTENCE {_claimed_sent}')
gate(f'Ⓓ② ⛔⛭⛭ and the pre-registration is refuted a SECOND time, on its own arithmetic, exactly as '
     f'it said it could be: it claimed `{_claimed_tok}` `TOKEN` and `{_claimed_sent}` `SENTENCE` '
     f'where the ledger carries `{_tiers["TOKEN"]}` and `{_tiers["SENTENCE"]}`.  ** The count was '
     f'wrong by two in each direction, and it was the count the whole argument rested on ** --- the '
     f'band still held, which is luck and is said here rather than left to be noticed',
     _tiers['TOKEN'] != _claimed_tok and _tiers['SENTENCE'] != _claimed_sent
     and _tiers['TOKEN'] + _tiers['SENTENCE'] == 29)

gate(f'Ⓓ③ ⛭⛭ and a THIRD thing the call missed entirely: the prefix\'s single largest class is '
     f'`NOT-A-PIN` at `{_na:.1f}` per cent, `{_tally["NOT-A-PIN"]}` of `{_n}` --- ** a class the '
     f'pre-registration\'s four bands do not mention at all. ** A pre-registration that names the '
     f'wrong classes cannot be scored on the class that turns out to matter, and that is a defect '
     f'in the registration and not in the result',
     _tally['NOT-A-PIN'] > max(_tally['REPAIR-OWED'], _tally['MEANING-HELD'])
     and 'NOT-A-PIN' not in _pred_then)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE BACKLOG, AND THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_un_before = sum(1 for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))
                 if c[5].startswith('UNADJUDICATED'))
_un_now = sum(1 for c in _all if c[5].startswith('UNADJUDICATED'))
print(f'      backlog {_un_before} -> {_un_now}, landed {_un_before - _un_now}')
gate(f'Ⓔ① ⛭⛭ `{_un_before - _un_now}` LANDED, `{_un_now}` REMAIN --- read against the pinned '
     f'`{BEFORE}`, and the live arm is MONOTONE: the backlog may fall further and never rises, so '
     f'another seat\'s work cannot turn this row red',
     _un_before - _un_now >= 29 and _un_now <= _un_before)

# ⛔⛭⛭⛭ r7370: ** AND THE SELECTOR WAS A STRING MATCH ON COMMIT MESSAGES. **  *`\br7290\b` over
#   `BEFORE..HEAD` does not select this revision's commits; it selects EVERY COMMIT WHOSE MESSAGE
#   MENTIONS IT -- and the corpus's convention is to cite revisions by number in every message, which
#   the comment four lines above this one says in so many words and then did not act on.*
#   ⌈ *Measured: the match returned `5` commits of which `2` are this revision's.  The other three
#     are `r7292`'s pre-registration, which cites `r7290`; another seat's `r7355+cc66.2`, which cites
#     it AND touched two receipts, which is what turned this clause red; and `r7368`'s own commit
#     message about this very defect.*
#   ⇒ *** A REVISION THAT WRITES ABOUT ANOTHER JOINS ITS SELECTOR.  The gate was red five pushes
#       running and the commit that demonstrates it is the one describing it. ***
#   ⌊ *The commits of a revision are a historical fact and are PINNED, exactly as `BEFORE` beside
#     them is -- and the string match is kept as the CONTROL: it must return strictly more than the
#     pinned pair, so the pin cannot silently become the match again.*
OWN = ('dc5e48dc', 'db791aad')      # this revision's own two commits, pinned
_own = [c for c in OWN if _git('cat-file', '-t', c).strip() == 'commit']
assert len(_own) == len(OWN), f'{OWN} do not all resolve in this clone: {_own}'
_matched = []
for _rec in _git('log', '--format=%H%x1f%B%x1e', f'{BEFORE}..HEAD').split('\x1e'):
    _rec = _rec.strip()
    if _rec and '\x1f' in _rec and re.search(r'\br7290\b', _rec.split('\x1f', 1)[1]):
        _matched.append(_rec.split('\x1f', 1)[0])
print(f'      the pinned commits: {len(_own)};  what the string match returns now: '
      f'{len(_matched)} -- REPORTED, and the control below')
_touched = sorted({f for _h in _own for f in _git('show', '--name-only', '--format=', _h).split('\n')
                   if f})
if not _touched:
    _touched = sorted({f for f in (_git('diff', '--name-only', BEFORE) + '\n'
                                   + _git('ls-files', '--others', '--exclude-standard')).split('\n')
                       if f})
_rcpt = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')]
print(f'      touched {len(_touched)} file(s), {len(_rcpt)} of them receipts')
# ⌗ THE CLAIM IS STATED AS THE SPECIFIC NEGATIVE IT IS: none of the receipts whose rows this
#   revision verdicted was touched.  The range form of this claim broke twice in `r7288` -- once on a
#   dropped record separator and once because `r7290` CITED `r7288` by number in a commit message and
#   so entered its filter.  ** A selector over a live range cannot be made safe by filtering what it
#   matches, when the corpus's own convention is to cite revisions by number. **
_subjects = sorted({k[0] for k in _keys})
_touched_subjects = [f for f in _touched if f in _subjects]
print(f'      the {len(_keys)} rows live in {len(_subjects)} receipt(s); this revision touched '
      f'{len(_touched_subjects)} of them')
gate(f'Ⓔ② ⛭⛭ the restraint, as the SPECIFIC NEGATIVE: the `{len(_keys)}` rows live in '
     f'`{len(_subjects)}` receipts of `L271` and this revision touched `{len(_touched_subjects)}` of '
     f'them, while the ledger IS in the diff --- because a verdict is a row and not an edit to the '
     f'gate it describes.  ** Stated this way it cannot be broken by a later revision landing its own '
     f'receipt, which is how the range form of the same claim broke twice in `r7288` **',
     BASE in _touched and not _touched_subjects
     and all(f.endswith(os.path.basename(__file__)) for f in _rcpt)
     # ⛭⛭⛭ r7370: and the string match that USED to select these commits is kept as the control --
     # it returns strictly MORE than the pinned pair, because later commits cite the revision by
     # number, so the pin cannot quietly become the match again without this failing.
     and len(_matched) > len(_own)
     and all(any(m.startswith(c) for m in _matched) for c in _own))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** THE HIGH CALL IS REFUTED: {_ro:.1f} PER CENT AGAINST A CALLED {_called_floor:.0f} OR ABOVE. **
     This seat corrected the application r7288 found wrong, picked its own prefix, called HIGH,
     and came back in its own low mode -- which removes r7288's explanation for the seat effect.
  ⛭⛭ ** BUT THE MECHANISM IS NOT THE READER: {_unreachable} OF THE {_n} CANNOT TAKE REPAIR-OWED AT ALL. **
     {len(_pinned)} are read at a literal commit and {len(_absence)} assert a term is absent. The pin IS the repair,
     landed in advance: {len(_gone)} of the {len(_lits)} pinned literals are GONE from the live paper.
  ⛔ ** AND THE PREDICTOR THAT WOULD EXPLAIN IT IS REFUTED AT SPEARMAN {_rho:+.2f} BEFORE BEING CLAIMED. **
     Third mechanical predictor to fail on this problem, and the first refuted in the revision
     that built it. The pre-registration is also wrong on its own tier arithmetic, and missed
     the prefix's largest class entirely.
  ⛭ {_un_before - _un_now} landed, {_un_now} remain.
""")
sys.exit(1 if FAILURES else 0)
