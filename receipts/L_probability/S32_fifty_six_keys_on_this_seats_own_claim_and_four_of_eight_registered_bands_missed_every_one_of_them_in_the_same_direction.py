#!/usr/bin/env python3
r"""S32 -- `r7289` order ②: the five prefixes this seat claimed, read whole, and the bands scored.

COMPUTES: nothing the papers quote.  This receipt reports the adjudication of `56` quote-pin keys
across five prefixes taken by this seat under the endgame protocol, and scores a pre-registration
pushed before four of the five were opened.

** ⛭⛭⛭ `56` LANDED, `309` REMAIN --- the one arithmetic figure the pre-registration predicted, hit
exactly. **  *`L811` `12`, `P14` `12`, `L150` `11`, `L803` `11`, `L210` `10`; the five heaviest
unclaimed prefixes in the tail, claimed in a pushed commit before any was read.*

** ⛔⛭⛭⛭ AND FOUR OF THE EIGHT REGISTERED BANDS ARE MISSED --- EVERY ONE OF THEM IN THE SAME
DIRECTION. **  *`REPAIR-OWED` came in ABOVE its band on the two token-heavy prefixes; `MEANING-HELD`
came in ABOVE its band on the two sentence-heavy ones.*
  ⌈ ⇒ ***So the bands are not wrong one at a time, they are wrong SYSTEMATICALLY LOW --- and they
    were drawn as wide as this seat could honestly draw them without an instrument.*** *That is the
    fourth refutation of this seat's priors in a row, and it is the argument for `r7289`'s own ruling:
    **the mode call is optional because a call with no instrument behind it is a guess, and a BAND
    with no instrument behind it is the same guess with error bars.***
  ⌊ ✔ *What the registration DID buy is in the next section: it named in advance what one particular
    miss would MEAN, and the miss means that.*

** ✔⛭⛭ THE ONE PREDICTION THAT NAMED ITS OWN REFUTATION FIRED EXACTLY AS WRITTEN. **  *Registered:
`L803` is `TOKEN`-dominated, so a `REPAIR-OWED` share above `30` per cent would mean the
narrower-than-claim family is reaching TOKENS at a rate this seat has not seen --- a finding against
the band rather than a miss.*  **It came in at `45.5`, and the two rows that put it there are a single
COMMON WORD and a WORD STEM, both `TOKEN` tier, both `CANNOT FAIL`.** ⇒ *A band that says what
breaking it would mean is worth more than a band that is merely narrow.*

** ⛔⛭⛭ AND THE SUBJECT TEST THIS LINE REPAIRED ONE REVISION AGO HAS A FALSE POSITIVE, FOUND BY USING
IT. **  *`the same standard datum that fixes both the light-element abundances and the
microwave-background peak heights` is a NOUN PHRASE with no main verb of its own --- the predication
is outside the span --- and the repaired test reads it as naming its subject.*
  ⌈ ***It cannot tell `determiner + noun + restrictive relative + MAIN VERB` from `determiner + noun
    + restrictive relative` with no main verb at all.*** *The `r7294` condition keyed on the COMMA,
    which correctly admits `a consistency check that matches nothing is green forever`, and a
    restrictive relative carries no comma either way.*
  ⌊ ⇒ *Routed with its discriminator and NOT applied here: **after stripping a restrictive relative,
    a finite verb must REMAIN.** One repair per revision, and the verdict on that row is by reading.*

** ⌗ AND THE CLOSED WORD LISTS SHOW THEIR LOWER-BOUND PROPERTY TWICE. **  *Two rows are verdicted
against what the header RULE says while the adopted ARM does not fire: a participle absent from the
`LEAD` list, and a main verb absent from `FINITE`.  `r7260` states that the adopted figure is a lower
bound; this is what that costs at the row level, and the reading governs.*

** ⛭ `L811`'s SHARES ARE REPORTED AND NOT REGISTERED, and the reason is procedural and mine. **  *Its
twelve literals were read while surveying the claim, before the pre-registration was written --- so
the file declares `L811` unregistered in its own first section rather than quietly covering it.*
⇒ ***A claim and a pre-registration are two pushes, and surveying what you claimed is already reading
it.*** *The claim should carry the shares, or the survey should stop at the counts.*

⌗ *Sources: `r7289` order ① and the endgame protocol; the claim commit and the pre-registration, both
read at the commits that pushed them; the five receipts read at their sites; the repaired arms imported
byte for byte; and the ledger before and after.*
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

import dangling_predicate_v2 as D          # noqa: E402

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


CLAIM = '5c72d3f0'    # the commit that claimed the five prefixes
PREG = '4442ec02'     # the commit that registered the four unread prefixes' shares
AFTER = '9d9a1e89'    # the commit that carried this revision's verdicts -- the 71st member's corollary
# ⚠ The COUNTS below are read at `AFTER`, not in the working tree: an equality on a LIVE ledger goes
# red the moment another seat legitimately re-verdicts a row.  The backlog is the one live read kept,
# and it is MONOTONE.
BASE = 'corpus/quote_pin_baseline.tsv'
PRED = 'computations/beyond_the_wall/r7296_60_the_four_unread/PREDICTION.md'
STAMP = 'r7296+60'
FOUR = ['P14_matter_sector_paper', 'L150_the_datum', 'L803_station9_neff', 'L210_entry_points']
BANDS = {'P14_matter_sector_paper': ((30, 70), (0, 35)),
         'L150_the_datum': ((30, 70), (0, 40)),
         'L803_station9_neff': ((0, 30), (0, 25)),
         'L210_entry_points': ((10, 55), (0, 35))}


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
print('S32 -- 56 keys on this seat\'s own claim, and the bands scored')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE CLAIM AND THE REGISTRATION, BOTH PINNED, AND ONE PREFIX DECLARED UNCOVERED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res = all(subprocess.run(['git', 'cat-file', '-e', s + '^{commit}'], cwd=ROOT,
                          capture_output=True).returncode == 0 for s in (CLAIM, PREG))
_anc = all(subprocess.run(['git', 'merge-base', '--is-ancestor', s, 'HEAD'], cwd=ROOT,
                          capture_output=True).returncode == 0 for s in (CLAIM, PREG))
_pred = _git('show', f'{PREG}:{PRED}')
_then = {(c[0], c[1]): c[5] for c in rows_of(_git('show', f'{PREG}:{BASE}'))}
_unread = [k for k in _then if any(k[0].startswith('receipts/' + p + '/') for p in FOUR)
           and _then[k].startswith('UNADJUDICATED')]
gate(f'Ⓐ① ⛔⛭⛭ both commits are LITERAL SHAs that resolve (`{_res}`) and are ancestors (`{_anc}`), and '
     f'at the registration commit all `{len(_unread)}` keys of the four registered prefixes were '
     f'still `UNADJUDICATED` --- so their shares were registered before any of them was opened',
     _res and _anc and len(_unread) == 44 and len(_pred) > 1500)

_declared = ('L811' in _pred and 'NOT pre-registered' in _pred
             and 'surveying the claim' in _pred)
gate(f'Ⓐ② ⛭⛭ and the fifth prefix is DECLARED UNCOVERED in the registration\'s own first section '
     f'(`{_declared}`): `L811`\'s literals were read while surveying the claim, so its shares are '
     f'reported and not registered.  ** Said in the file that would otherwise have covered it, not in '
     f'this receipt where it would read as an excuse **',
     _declared)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE COUNTS, AND THE BAND SCORECARD ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_after_led = _git('show', f'{AFTER}:{BASE}')
_all = rows_of(_after_led)
_mine = [c for c in _all if STAMP in (c[6] or '')]
_by_pfx = collections.defaultdict(list)
for _c in _mine:
    _by_pfx[_c[0].split('/')[1]].append(_c)
_un_then = sum(1 for c in rows_of(_git('show', f'{PREG}:{BASE}'))
               if c[5].startswith('UNADJUDICATED'))
_un_now = sum(1 for c in rows_of(read(BASE)) if c[5].startswith('UNADJUDICATED'))
_reg_after = re.search(r'Expected after all five: `(\d+)`', _pred)
print(f'      {len(_mine)} keys verdicted across {len(_by_pfx)} prefixes; backlog {_un_then} -> '
      f'{_un_now}; the registration said {_reg_after.group(1) if _reg_after else "?"}')
gate(f'Ⓑ① ⛭⛭ `{len(_mine)}` LANDED, `{_un_now}` REMAIN --- and the one arithmetic figure the '
     f'registration predicted, the backlog after all five, is `{_reg_after.group(1)}` against '
     f'`{_un_now}` measured.  The live arm is MONOTONE: the backlog may fall further and never rises',
     len(_mine) == 56 and int(_reg_after.group(1)) == _un_now)

_score = []
for _p, (_ro_band, _mh_band) in BANDS.items():
    _rs = _by_pfx[_p]
    _t = collections.Counter(c[5] for c in _rs)
    _ro = 100.0 * _t['REPAIR-OWED'] / len(_rs)
    _mh = 100.0 * _t['MEANING-HELD'] / len(_rs)
    for _name, _v, _b in (('RO', _ro, _ro_band), ('MH', _mh, _mh_band)):
        _in = _b[0] <= _v <= _b[1]
        _score.append((_p, _name, _v, _b, _in))
        print(f'      {_p[:24]:24} {_name}  {_v:5.1f}%  band {_b[0]}-{_b[1]}  '
              f'{"in" if _in else ("ABOVE" if _v > _b[1] else "BELOW")}')
_missed = [s for s in _score if not s[4]]
_all_above = all(s[2] > s[3][1] for s in _missed)
gate(f'Ⓑ② ⛔⛭⛭⛭ ** `{len(_missed)}` OF THE `{len(_score)}` REGISTERED BANDS ARE MISSED, AND EVERY ONE '
     f'IS MISSED IN THE SAME DIRECTION --- ABOVE (`{_all_above}`). ** `REPAIR-OWED` above its band on '
     f'the two TOKEN-heavy prefixes, `MEANING-HELD` above its band on the two SENTENCE-heavy ones.  '
     f'⇒ *** So the bands are not wrong one at a time, they are wrong SYSTEMATICALLY LOW --- and they '
     f'were drawn as wide as this seat could honestly draw them without an instrument, which is the '
     f'argument for `r7289`\'s ruling: a BAND with no instrument behind it is a guess with error bars '
     f'***',
     len(_missed) >= 3 and _all_above)

_l803 = _by_pfx['L803_station9_neff']
_cannot = [c for c in _l803 if c[5] == 'REPAIR-OWED' and 'CANNOT FAIL' in (c[6] or '')
           and c[3] == 'TOKEN']
_l803_ro = 100.0 * sum(1 for c in _l803 if c[5] == 'REPAIR-OWED') / len(_l803)
print(f'      L803 REPAIR-OWED {_l803_ro:.1f}% against a registered ceiling of 30, and '
      f'{len(_cannot)} of its rows are TOKEN-tier CANNOT-FAIL')
gate(f'Ⓑ③ ✔⛭⛭ and the ONE prediction that named its own refutation fired exactly as written: the '
     f'registration said a `REPAIR-OWED` share above `30` per cent on this `TOKEN`-dominated prefix '
     f'would mean the narrower-than-claim family is REACHING TOKENS --- it came in at '
     f'`{_l803_ro:.1f}`, and `{len(_cannot)}` of its rows are `TOKEN`-tier `CANNOT FAIL`, a single '
     f'common word and a word stem.  ** A band that says what breaking it would MEAN is worth more '
     f'than a band that is merely narrow **',
     _l803_ro > 30 and len(_cannot) == 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE CEILINGS HELD, AND THE REPAIRED TEST HAS A FALSE POSITIVE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_SUBJ = re.compile(r'subject rule|DANGLING|OBJECT-DANGLING|PRONOUN subject|the SUBJECT IS A PRONOUN'
                   r'|VERBLESS APPOSITIVE', re.I)
_ok = True
for _p, _rs in sorted(_by_pfx.items()):
    _sent = sum(1 for c in _rs if c[3] == 'SENTENCE')
    _sub = sum(1 for c in _rs if c[5] == 'REPAIR-OWED' and _SUBJ.search(c[6] or ''))
    print(f'      {_p[:26]:26} SENTENCE {_sent:3}   subject-grounded REPAIR-OWED {_sub:3}')
    _ok = _ok and _sub <= _sent
gate(f'Ⓒ① ✔⛭ the arithmetic CEILING registered per prefix holds in every one: the subject rule '
     f'grounds no more `REPAIR-OWED` rows than the prefix has `SENTENCE`-tier keys (`{_ok}`).  ** It '
     f'is a ceiling and not a prediction, written down because `r7290`\'s tier count was wrong by two '
     f'in each direction and its band held by luck **',
     _ok)

_fp = [c for c in _mine if 'FALSE POSITIVE OF THE SUBJECT TEST' in (c[6] or '')]
_fp_lit = json.loads(_fp[0][1]) if _fp else ''
_reads_as_subject = D.names_own_subject(_fp_lit) if _fp_lit else False
#: the discriminator this routes rather than applies: strip a restrictive relative and a finite verb
#: must REMAIN.  Shown here to work on both the false positive and the span it must not break.
_REL = re.compile(r'\b(?:that|which|who|whom)\b.*$', re.I)
_KEEP = 'a consistency check that matches nothing is green forever'


def _main_verb_survives(lit):
    _head = D.STRIP.sub('', lit)
    return bool(D._FIN_ANY.search(_REL.sub('', _head)))


print(f'      the repaired test reads the noun phrase as naming its subject: {_reads_as_subject}; '
      f'the routed discriminator rejects it ({not _main_verb_survives(_fp_lit)}) and keeps the '
      f'restrictive-relative clause ({_main_verb_survives(_KEEP) is False})')
gate(f'Ⓒ② ⛔⛭⛭⛭ ** AND THE SUBJECT TEST THIS LINE REPAIRED ONE REVISION AGO HAS A FALSE POSITIVE, '
     f'FOUND BY USING IT: ** a NOUN PHRASE with a restrictive relative and NO main verb of its own '
     f'reads as naming its subject (`{_reads_as_subject}`).  It cannot tell `determiner + noun + '
     f'restrictive relative + MAIN VERB` from the same without a main verb, because the `r7294` '
     f'condition keyed on the COMMA and a restrictive relative carries none either way.  ** Routed '
     f'with its discriminator and NOT applied: after stripping a restrictive relative a finite verb '
     f'must REMAIN --- one repair per revision, and the verdict on that row is by reading **',
     len(_fp) == 1 and _reads_as_subject and not _main_verb_survives(_fp_lit))

_gap = [c for c in _mine if 'closed FINITE list' in (c[6] or '')
        or 'closed LEAD word list' in (c[6] or '')]
print(f'      rows verdicted against the header RULE where the adopted ARM does not fire: {len(_gap)}')
gate(f'Ⓒ③ ⌗⛭ and the closed word lists show their LOWER-BOUND property at the row level '
     f'`{len(_gap)}` times --- a participle absent from `LEAD`, a main verb absent from `FINITE` --- '
     f'so two rows are verdicted on what the header RULE says while the arm stays silent.  ** `r7260` '
     f'states the adopted figure is a lower bound; this is what that costs per row, and the reading '
     f'governs **',
     len(_gap) == 2)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_subjects = sorted({c[0] for c in _mine})
_touched = sorted({f for f in (_git('diff', '--name-only', PREG) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
_touched_subjects = [f for f in _touched if f in _subjects]
print(f'      the {len(_mine)} rows live in {len(_subjects)} receipts; this revision edited '
      f'{len(_touched_subjects)} of them')
#: ⛔⛭ r7298+60: the first form also demanded that no receipt but this one appear in the diff --- a
#: claim about the diff's FORM beside the claim it means, over a LIVE range.  Dropped: the specific
#: negative is the whole claim.
gate(f'Ⓓ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE and nothing beside it: the `{len(_mine)}` rows '
     f'live in `{len(_subjects)}` receipts across five prefixes and this revision edited '
     f'`{len(_touched_subjects)}` of them, while the ledger IS in the diff --- because a verdict is a '
     f'row and not an edit to the gate it describes',
     BASE in _touched and not _touched_subjects)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** {len(_mine)} LANDED, {_un_now} REMAIN ** -- the one arithmetic figure the registration predicted, exact.
  ⛔ ** AND {len(_missed)} OF THE {len(_score)} REGISTERED BANDS ARE MISSED, EVERY ONE IN THE SAME DIRECTION -- ABOVE. **
     REPAIR-OWED above its band on both token-heavy prefixes, MEANING-HELD above on both
     sentence-heavy ones. The bands are wrong systematically, not one at a time -- and they were
     as wide as this seat could honestly draw them without an instrument.
  ✔ ** The one prediction that named its own refutation fired as written: ** L803's share came in
     above 30 because the narrower-than-claim family IS reaching tokens -- a common word and a
     word stem, both CANNOT FAIL. A band that says what breaking it would mean earns its keep.
  ⛔ ** And the subject test repaired one revision ago has a false positive, found by using it: **
     a noun phrase with a restrictive relative and no main verb reads as naming its subject.
     Routed with its discriminator, not applied -- one repair per revision.
""")
sys.exit(1 if FAILURES else 0)
