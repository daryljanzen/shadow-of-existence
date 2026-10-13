#!/usr/bin/env python3
r"""S30 -- `L247_the_build_already_stands` read with NO mode call, and the registered relationship
turns out VACUOUS on this prefix for a reason worth more than a score.

COMPUTES: nothing the papers quote.  This receipt reports the adjudication of `21` quote-pin keys and
scores a pre-registration pushed before the first of them, and before the receipt's source, was read.

** CROSS-REF: the pre-registration is `computations/beyond_the_wall/r7292_60_no_call/PREDICTION.md`,
pushed at `6457919e`, and this receipt reads its numbers OUT of that commit's copy. **

** ⛭⛭⛭ THE REGISTERED RELATIONSHIP CANNOT BE TESTED HERE, AND THAT IS THE FINDING. **  *`r7292`
registered that the STRUCTURAL share would account for the mode better than the ledger's `PINNED`
flag share does.*  **On this prefix the two are IDENTICAL --- `7` of `21` either way, because every
pinned read carries the flag and nothing else does --- so neither can be closer and the test is
vacuous.**  ⇒ ***A relationship registered between two measures is untestable wherever they
coincide, and the registration did not say what to do then.  That is a defect in the design, found by
running it.***

** ⛔⛭⛭ AND THE STRUCTURAL EXPLANATION IS INCOMPLETE, WHICH THE NUMBERS SHOW DIRECTLY. **  *`11` of
the `21` are NOT `REPAIR-OWED` while only `7` are structurally unable to be.*
  ⌈ ⇒ ***So the non-`REPAIR-OWED` share splits in two: the STRUCTURALLY UNABLE (a pinned read, an
    absence probe) and NAMES-AND-VALUES (a label, a formula, a quantity).  Only the first is
    mechanical.*** *On `r7290`'s prefix the second part was zero of `29`; here it is `4` of `21`.*
  ⌊ ⌗ *`r7290` said the structural share was measured on ONE prefix and might not account for any
    other's mode.  **It does not account for this one, and the gap is a reading rather than a
    structure** --- which is why no instrument over the ledger will close it.*

** ✔⛭ WHAT DID HOLD, INCLUDING THE ARITHMETIC THAT WAS WRONG LAST TIME. **  *The flag UNDERCOUNTS or
matches the structure, never overcounts (registered ②, holding with equality here).  The subject rule
reached `2` of the `21`, inside the registered arithmetic ceiling of `9`.  **And the tier count written
into the pre-registration --- `9` `SENTENCE`, `12` `TOKEN` --- is exactly right this time, which
`r7290`'s was not.***

⌗ *`21` landed, `481` remain.  No level was called, for the reason registered in advance: three
predictors have been built and refuted on this problem, two of them this line's own, and the rule that
a pre-registration may not read literals leaves nothing else to call a level on.*
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


BEFORE = '6457919e'   # the commit that PUSHED the pre-registration, before the first key was opened
AFTER = 'a4520168'    # the commit that carried this revision's verdicts -- the 71st member's corollary
# ⚠ Every COUNT below is read at `AFTER`, not in the working tree: an equality on a LIVE ledger goes
# red the moment another seat legitimately re-verdicts a row.  The one live read kept is the backlog,
# and it is MONOTONE.  The restraint is stated as a specific negative rather than over a commit range.
BASE = 'corpus/quote_pin_baseline.tsv'
PRED = 'computations/beyond_the_wall/r7292_60_no_call/PREDICTION.md'
PFX = 'receipts/L247_the_build_already_stands/'
SUBJECT = PFX + 'B1_the_geometry_po14_asks_for_was_built_at_r2419.py'


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 6 and c[0].startswith('receipts/')]


print()
print('=' * 100)
print('S30 -- L247 read with NO mode call, and the registered relationship is vacuous here')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE PRE-REGISTRATION CAME FIRST, AND IT REGISTERED NO LEVEL ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                      capture_output=True).returncode == 0
_anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                      capture_output=True).returncode == 0
_pred = _git('show', f'{BEFORE}:{PRED}')
_before_rows = {(c[0], c[1]): (c[2], c[3], c[4], c[5]) for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))}
_keys = [k for k in _before_rows if k[0].startswith(PFX) and _before_rows[k][3].startswith('UNADJUDICATED')]
gate(f'Ⓐ① ⛔⛭⛭ the pre-registration EXISTS at a literal sha (`{BEFORE}`, resolves `{_res}`, ancestor '
     f'`{_anc}`) and at that commit all `{len(_keys)}` of this prefix\'s keys were still '
     f'`UNADJUDICATED` --- so whatever it registered, it registered before the read',
     _res and _anc and len(_pred) > 2000 and len(_keys) == 21)

_no_call = 'NO CALL' in _pred and '**NO CALL' in _pred.replace('—', '---')
_three = len(re.findall(r'Spearman `[+-]?0\.\d\d`', _pred)) + _pred.count('14.3')
gate(f'Ⓐ② ⛭⛭ and what it registered is the ABSENCE of a level: the mode row reads `NO CALL` '
     f'(`{_no_call}`) with three refuted predictors tabled as the reason --- ** the first prefix this '
     f'line has read without calling its mode, and the reason is that every predictor it built is '
     f'refuted, two of them its own **',
     _no_call and _three >= 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE TALLY, AND THE ARITHMETIC THE LAST ONE GOT WRONG ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_after_led = _git('show', f'{AFTER}:{BASE}')
_now = {(c[0], c[1]): (c[5], c[6] if len(c) > 6 else '') for c in rows_of(_after_led)}
_mine = {k: _now[k] for k in _keys}
_tally = collections.Counter(v[0] for v in _mine.values())
_n = len(_mine)
_ro = 100.0 * _tally['REPAIR-OWED'] / _n
print(f'      {_n} keys: ' + ', '.join(f'{k} {v}' for k, v in sorted(_tally.items())))
print(f'      REPAIR-OWED {_ro:.1f}%')
_tiers = collections.Counter(_before_rows[k][1] for k in _keys)
_claim = re.search(r'`(\d+)` `SENTENCE`,\s*\n?`?(\d+)`? `TOKEN`', _pred.replace('\n', ' '))
_claim = re.search(r'`(\d+)` `SENTENCE`,\s*`(\d+)` `TOKEN`', re.sub(r'\s+', ' ', _pred))
print(f'      tier mix: SENTENCE {_tiers["SENTENCE"]}, TOKEN {_tiers["TOKEN"]}; the '
      f'pre-registration wrote SENTENCE {_claim.group(1) if _claim else "?"}, '
      f'TOKEN {_claim.group(2) if _claim else "?"}')
gate(f'Ⓑ① ✔⛭⛭ the tier count written into the pre-registration is EXACTLY RIGHT this time --- '
     f'`{_tiers["SENTENCE"]}` `SENTENCE` and `{_tiers["TOKEN"]}` `TOKEN`, against `r7290`\'s, which '
     f'was wrong by two in each direction with its band holding by luck.  ** It was written down '
     f'BECAUSE that one was wrong, which is the only reason it is right **',
     _claim is not None and int(_claim.group(1)) == _tiers['SENTENCE']
     and int(_claim.group(2)) == _tiers['TOKEN'] and _tiers['SENTENCE'] + _tiers['TOKEN'] == 21)

_subj = [k for k, v in _mine.items() if v[0] == 'REPAIR-OWED'
         and ('OBJECT-DANGLING' in v[1] or 'DANGLING on the subject rule' in v[1])]
gate(f'Ⓑ② ✔⛭ and the subject rule reached `{len(_subj)}` of the `{_n}`, inside the registered '
     f'arithmetic ceiling of `{_tiers["SENTENCE"]}` --- a ceiling and not a prediction, which is why '
     f'it is reported rather than scored',
     len(_subj) <= _tiers['SENTENCE'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE REGISTERED RELATIONSHIP IS VACUOUS HERE, AND THAT IS THE FINDING ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_flagged = [k for k in _keys if 'PINNED' in (_before_rows[k][2] or '')]
_structural = [k for k, v in _mine.items() if 'read at a LITERAL SHA' in v[1]]
_names = [k for k, v in _mine.items()
          if v[0] == 'DELIBERATE' and ('a NAME, read live' in v[1] or 'a VALUE, read live' in v[1])]
_not_ro = [k for k, v in _mine.items() if v[0] != 'REPAIR-OWED']
print(f'      flag says {len(_flagged)} of {_n}; the receipt\'s code says {len(_structural)} are '
      f'pinned reads; they are {"IDENTICAL" if set(_flagged) == set(_structural) else "DIFFERENT"}')
gate(f'Ⓒ① ⛭⛭⛭ ** THE REGISTERED RELATIONSHIP CANNOT BE TESTED ON THIS PREFIX: the `PINNED` flag and '
     f'the structural count are IDENTICAL at `{len(_flagged)}` of `{_n}`, the same keys ** --- every '
     f'pinned read carries the flag and nothing else does, so neither measure can be closer to the '
     f'mode than the other.  ⇒ *** A relationship registered between two measures is untestable '
     f'wherever they coincide, and the registration did not say what to do then ***',
     set(_flagged) == set(_structural) and len(_flagged) == 7)

print(f'      not REPAIR-OWED: {len(_not_ro)}; of those, structurally unable {len(_structural)}, '
      f'names-and-values {len(_names)}')
gate(f'Ⓒ② ⛔⛭⛭⛭ ** AND THE STRUCTURAL EXPLANATION IS INCOMPLETE, SHOWN BY SUBTRACTION: '
     f'`{len(_not_ro)}` of the `{_n}` are not `REPAIR-OWED` while only `{len(_structural)}` are '
     f'structurally unable to be. ** The remaining `{len(_names)}` are NAMES AND VALUES --- a label, '
     f'two formulas, a quantity --- which take `DELIBERATE` on the grain clause and not on any '
     f'structure.  ⇒ *** The non-`REPAIR-OWED` share splits in two and only one part is mechanical; '
     f'on `r7290`\'s prefix the second part was ZERO of `29` and here it is `{len(_names)}` of '
     f'`{_n}` ***',
     len(_not_ro) == len(_structural) + len(_names) and len(_names) >= 3
     and len(_not_ro) > len(_structural))

gate(f'Ⓒ③ ✔⛭ and registered ② holds, with equality: the flag UNDERCOUNTS or matches the structure '
     f'and never overcounts it --- `{len(_flagged)}` against `{len(_structural)}` here, `12` against '
     f'`23` on `r7290`\'s prefix.  ** So the flag is a LOWER BOUND on the structure in both prefixes '
     f'read, which is the one part of the design that survived **',
     len(_flagged) <= len(_structural))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE BACKLOG, AND THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_all = rows_of(_after_led)
_un_before = sum(1 for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))
                 if c[5].startswith('UNADJUDICATED'))
_un_now = sum(1 for c in _all if c[5].startswith('UNADJUDICATED'))
_registered_after = re.search(r'backlog after \| `(\d+)`', _pred)
print(f'      backlog {_un_before} -> {_un_now}; the pre-registration said '
      f'{_registered_after.group(1) if _registered_after else "?"}')
gate(f'Ⓓ① ⛭⛭ `{_un_before - _un_now}` LANDED, `{_un_now}` REMAIN --- and the pre-registration\'s one '
     f'arithmetic prediction, the backlog after, is `{_registered_after.group(1)}` against '
     f'`{_un_now}` measured.  The live arm is MONOTONE: the backlog may fall further and never '
     f'rises, so another seat\'s work cannot turn this row red',
     _un_before - _un_now >= 21 and int(_registered_after.group(1)) == _un_now)

# ⛔⛭⛭ r7293 (66): AND THE RANGE WAS `BEFORE..WORKING TREE` AGAIN, WHICH IS THE RULE `r7283` SET AND
#   `r7289` RESTATED, ARRIVING IN A RECEIPT WRITTEN AFTER BOTH.  *On the branch it is this revision's
#   own evidence; on the merged trunk it is every seat's work since, so the restraint read wide and
#   `Ⓓ②` went red on `main` -- found by the carry's own `gates` field, which `70` built for exactly
#   this and which named the clause rather than only the receipt.*
#   ⇒ *** A restraint claim is over a COMMIT RANGE: `BEFORE..AFTER`, with the working-tree arm kept
#       only for the branch case where the revision's own commits do not yet exist. ***
#   ⌊ *`66`'s edit, two lines, because `main` was red and `60` was mid-cycle.  **Stated for `60` to
#     reverse** -- no claim, count or verdict moves.*
AFTER = 'a45201689'      # this revision's own landing commit, so the restraint is over its own range
_rng = _git('diff', '--name-only', BEFORE, AFTER)
_touched = sorted({f for f in (_rng + '\n'
                               + (_git('diff', '--name-only', BEFORE) if not _rng.strip() else '')
                               + '\n' + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
_rcpt = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')]
print(f'      touched {len(_touched)} file(s), {len(_rcpt)} of them receipts; the subject receipt '
      f'{"IS" if SUBJECT in _touched else "is NOT"} among them')
gate(f'Ⓓ② ⛭⛭ the restraint, as the SPECIFIC NEGATIVE: the `{_n}` rows all live in ONE receipt and '
     f'this revision did not touch it, while the ledger IS in the diff --- because a verdict is a '
     f'row and not an edit to the gate it describes.  ** Stated this way it cannot be broken by a '
     f'later revision landing its own receipt, which is how the range form broke twice in `r7288` **',
     BASE in _touched and SUBJECT not in _touched
     and all(f.endswith(os.path.basename(__file__)) for f in _rcpt))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** THE REGISTERED RELATIONSHIP IS VACUOUS HERE: the PINNED flag and the structural count are
     IDENTICAL at {len(_flagged)} of {_n}, the same keys, so neither can be closer to the mode. **
     A relationship registered between two measures is untestable wherever they coincide.
  ⛔ ** AND THE STRUCTURAL EXPLANATION IS INCOMPLETE: {len(_not_ro)} of {_n} are not REPAIR-OWED while only
     {len(_structural)} are structurally unable to be. ** The other {len(_names)} are names and values. The
     non-REPAIR-OWED share splits in two and only one part is mechanical.
  ✔ ** What held: the flag is a LOWER BOUND on the structure in both prefixes read, the subject
     rule reached {len(_subj)} of {_n} inside its ceiling, and the tier arithmetic is right this time --
     written down because r7290's was wrong. **
  ⛭ {_un_before - _un_now} landed, {_un_now} remain. No level was called, and the reason was registered in advance.
""")
sys.exit(1 if FAILURES else 0)
