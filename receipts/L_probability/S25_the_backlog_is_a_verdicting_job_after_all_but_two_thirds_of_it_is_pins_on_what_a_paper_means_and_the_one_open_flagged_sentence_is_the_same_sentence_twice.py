#!/usr/bin/env python3
r"""S25 -- `r7269`'s order ①: the quote-pin backlog, `L175` and `L211` verdicted, with the count.

COMPUTES: nothing the papers quote.  This receipt measures the corpus's own quote-pin ledger -- a
population of `110` keys in `15` receipts across two prefixes -- and the instruments are the pin
operator's own listing and the verdict vocabulary `r7253` closed.

** ⛭⛭ THE BURDEN FIRST, BECAUSE THE ORDER SETS IT: `110` LANDED, `700` REMAIN. **  *`810` before this
revision, `700` after, measured by the instrument and not by this seat's count: the whole of
`L175_dimensional_descent` and `L211_closure_adjacency`.*

** ✔ AND THE ORDER'S OWN NEGATIVE DOES NOT FIRE, WHICH IS THE ANSWER TO ITS QUESTION. **  *`r7269`
set it: if `REPAIR-OWED` comes back far above the old era's `2.5` per cent, the backlog is a
REWRITING job wearing a verdicting one and `810` is the wrong unit.*
  ⇒ *** `3` of `110`, which is `2.7` per cent -- the old era's rate, not a multiple of it. **So the
      backlog is a verdicting job**, and the row's countable half is countable. ***

** ⛔⛭⛭⛭ BUT THIS SEAT'S OWN BAND BREAKS BY A FACTOR OF THREE, AND THE MISS IS THE FINDING. **  *I
pre-registered `MEANING-HELD` at `6` of `110`, ceiling `20`.  **Measured `62`.***
  ⇒ *** TWO THIRDS OF THIS POPULATION IS PINS ON WHAT ANOTHER PAPER *MEANS*, not on how it words
      anything -- so `MEANING-HELD` is not the rare verdict the vocabulary's framing suggests, it is
      the DEFAULT for a receipt that reads another paper's statement. ***
  ⌈ *The reason is structural and the two prefixes show it from both sides: `L-211` is an ADJACENCY
    procedure -- it exists to read what one paper says and ask which gap in another that answers --
    and `L-175` is a NARROWING row whose receipts quote the register's own guard back at it.  **A
    receipt whose subject is another document's claim cannot pin anything but a meaning.***
  ⌊ ✔ *And the held rows are not a weaker verdict: each names a commit that CHANGED the receipt while
    the target carried the literal, which the instrument's five `r7253` gates check -- so a held row
    proves it was read where an unverdicted one proves nothing.*

** ✔⛭⛭ AND THE SECOND NEGATIVE DOES NOT FIRE, BY SIX. **  *I set it as: if more than `55` of the
`110` cannot be verdicted from the literal and its assertion alone, the cost per key is a passage and
not a string.*  ⇒ *Measured `49`: for that many the FILE THE KEY READS is not derivable from the
literal and the paths its own receipt names -- the read is set up through a variable, a helper or a
path the assertion never spells.*  ⌈ ** And the first pass of this very measurement said `61`, by
looking only at `corpus/` and `receipts/` paths and missing the register files. **  *The number that
counts is the one with the wider instrument, and the earlier figure is left here because a count that
moved when the instrument widened is the kind of thing this line keeps finding.*  ⌊ *So the unit is
closer to right than I expected: a bare majority of these keys can be verdicted from the literal and
its assertion, and `49` of `110` cannot.*

** ⛔⛭⛭⛭ AND THE THIRD FIRES TOO: THE TWO `OPEN`-FLAGGED KEYS ARE ONE SENTENCE PINNED TWICE. **
*`The substrate route is closed; the progenitor route is open`, asserted bare in `A3` and again in
`A5`, read out of a forward file.*
  ⇒ *** That is a LATENT MEMBER of the blindness family, not an unverdicted row: the day the
      progenitor route closes -- which is the work those receipts point AT succeeding -- both gates go
      red on the success.  Neither carries a disjunction over the two states, so neither can tell
      `the route closed` from `the file was reworded`. ***
  ⌊ *Verdicted `REPAIR-OWED` at both sites with one repair named for both, and NOT taken here: the
    sentence is another seat's forward file, and the repair is a disjunction or a held finding rather
    than a rewording this seat may make.*

⌗ *The third `REPAIR-OWED` is this seat's own class arriving in someone else's receipt: a ONE-WORD
arm, `observed`, conjoined to a long clause -- it matches almost anywhere in the capstone, so the
conjunction is weaker than it looks and the arm cannot fail for the right reason.*

⌗ *Sources: the pin operator's own `--list` at `a2dfa7ab` and live; `PREDICTION.md`, pushed before any
site was read; the vocabulary `r7253` closed and `r7269`'s ruling ② on the `NOT-A-PIN` discriminator;
and `70`'s `r7137` encoding class, which is what `19` of these keys turned out to be.*
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
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7270_60_the_backlog_two_prefixes')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED arms, byte-for-byte

CHECKS = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


# ⛔⛭⛭ THE REFERENCE COMMIT IS A LITERAL SHA WITH A RESOLVE-AND-ANCESTOR GUARD -- the form r7267
#   ruled better than a bare sha, because a bad pin fails LOUDLY instead of silently reading HEAD.
BEFORE = 'a2dfa7ab'      # this revision's pre-registration, before any of the 110 sites was read
# ⛔⛭⛭⛭ r7280 (60): AND EVERY GATE BELOW READ THE LEDGER *LIVE*, WHICH IS THE 71st MEMBER IN THIS
#   RECEIPT'S OWN FORM.  *A revision's report is a claim about the state its own work produced; read
#   live, it goes false the moment the NEXT revision verdicts a key -- and `r7280` verdicted `71` and
#   retired two of these very rows, so SEVEN of this receipt's thirteen gates failed on work of this
#   line's own succeeding.*
#   ⇒ *** So the AFTER state is pinned at this revision's own landing commit, exactly as the BEFORE
#       state was, and the live ledger is read only where the claim is MONOTONE: the backlog may
#       only fall.  `L-249` applied to a count rather than to a sentence. ***
AFTER = '438cd783'       # this revision's own landing commit: the state these numbers describe
SELF_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, '/')
BASE = 'corpus/quote_pin_baseline.tsv'
PREFIXES = ('receipts/L175_dimensional_descent/', 'receipts/L211_closure_adjacency/')


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def before_resolves():
    ok = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                        capture_output=True).returncode == 0
    anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                         capture_output=True).returncode == 0
    return ok, anc


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    out = []
    for line in text.split('\n'):
        c = line.split('\t')
        if len(c) >= 6 and c[0].startswith('receipts/'):
            out.append(c)
    return out


print()
print('=' * 100)
print("S25 -- r7269's order: the quote-pin backlog, L175 and L211, with the count the order asks for")
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE REFERENCE COMMIT, ASSERTED BEFORE ANYTHING IS READ THROUGH IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res, _anc = before_resolves()
_base_b = _git('show', f'{BEFORE}:{BASE}')
_base_l = _git('show', f'{AFTER}:{BASE}')      # the state this revision produced
_base_now = read(BASE)                          # live, for the MONOTONE arm only
gate(f'Ⓐ① ⛔⛭⛭ the reference is a LITERAL SHA (`{BEFORE}`), it RESOLVES (`{_res}`), it is an ANCESTOR '
     f'of `HEAD` (`{_anc}`), and the ledger comes back from it DIFFERING from the working tree --- '
     f'so the before-and-after below is two states of one file and not one state read twice',
     _res and _anc and bool(_base_b) and bool(_base_l) and _base_b != _base_l)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE BURDEN: THE COUNT THAT LANDED AND THE COUNT THAT REMAINS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rb, _rl = rows_of(_base_b), rows_of(_base_l)
_unb = [r for r in _rb if r[5] == 'UNADJUDICATED']
_unl = [r for r in _rl if r[5] == 'UNADJUDICATED']
_mine = [r for r in _rl if len(r) > 6 and 'r7270+60' in r[6]]
_in_prefix = [r for r in _mine if r[0].startswith(PREFIXES)]
_was_unadj = {(r[0], r[1]) for r in _unb}
_landed = [r for r in _mine if (r[0], r[1]) in _was_unadj]
print(f'      UNADJUDICATED at {BEFORE}: {len(_unb)};  live: {len(_unl)};  '
      f'rows this revision verdicted: {len(_mine)} ({len(_in_prefix)} in the two prefixes)')
gate(f'Ⓑ① ⛭⛭ ** `{len(_landed)}` LANDED AND `{len(_unl)}` REMAIN ** --- the burden `r7269` sets, read '
     f'off the ledger at the pinned commit and live rather than counted by this seat: '
     f'`{len(_unb)}` before, `{len(_unl)}` after, and every one of the `{len(_mine)}` rows this '
     f'revision wrote was UNADJUDICATED at that commit',
     len(_unb) - len(_unl) == len(_landed) == len(_mine) == 110 and len(_unl) == 700
     # ⌗ and the LIVE arm is the only one read live, because it is the only MONOTONE claim: the
     #   backlog may fall further -- `r7280` took it to 598 -- and may never rise.
     and len([r for r in rows_of(_base_now) if r[5] == 'UNADJUDICATED']) <= len(_unl))

gate(f'Ⓑ② ✔ and the fall is the WHOLE of both prefixes: `{len(_in_prefix)}` of the `110` sit in '
     f'`L175_dimensional_descent` and `L211_closure_adjacency`, and NO key of either prefix is left '
     f'unadjudicated',
     len(_in_prefix) == 110
     and not [r for r in _unl if r[0].startswith(PREFIXES)])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE DISTRIBUTION, PARSED OUT OF THE LEDGER ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_dist = collections.Counter(r[5] for r in _mine)
for _v, _n in _dist.most_common():
    print(f'      {_v:14} {_n}')
gate(f'Ⓒ① ⛭ the verdicts are `{dict(_dist)}`, and every one is in the CLOSED vocabulary `r7253` '
     f'fixed --- no new verdict and no typo, which was an exemption until that revision',
     set(_dist) <= {'DELIBERATE', 'ALT-OK', 'REPAIR-OWED', 'NOT-A-PIN', 'ENCODING-OK', 'EXTENDED',
                    'MEANING-HELD'}
     and sum(_dist.values()) == 110)

_held = [r for r in _mine if r[5] == 'MEANING-HELD']
_stamped = [r for r in _held if re.search(r'held at [0-9a-f]{8,40}', r[6])]
gate(f'Ⓒ② ⛔⛭⛭ every one of the `{len(_held)}` `MEANING-HELD` rows NAMES THE COMMIT its finding is '
     f'held at (`{len(_stamped)}`), which is what `r7253` put the five gates on --- a held row must '
     f'prove it was READ, and the instrument fails it for a bad sha, an absent literal, a TOKEN or a '
     f'`HEAD` stamp',
     len(_held) == 62 and len(_stamped) == len(_held))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE BANDS, SCORED AS A SET, AND THREE OF THEM BREAK ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PRED = read('computations/beyond_the_wall/r7270_60_the_backlog_two_prefixes/PREDICTION.md')
_ROWRE = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROWRE.finditer(_PRED)]
_measured = [_dist.get('REPAIR-OWED', 0), _dist.get('DELIBERATE', 0), _dist.get('ALT-OK', 0),
             _dist.get('NOT-A-PIN', 0), _dist.get('MEANING-HELD', 0), 0, 0]
_broke = []
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m = _measured[_i] if _i < len(_measured) else None
    _in = _m is not None and _lo <= _m <= _hi
    if not _in:
        _broke.append(_i)
    print(f'      {"✔" if _in else "⛔"} {_name[:62]:62} {_c} in {_lo}-{_hi}, measured {_m}'
          f'{"" if _in else "   BREAKS"}')
gate(f'Ⓓ① ⛭⛭ the bands are PARSED out of the pushed pre-registration --- `{len(_bands)}` rows ---',
     len(_bands) == 7)

gate(f'Ⓓ② ⛔⛭⛭ and `{len(_broke)}` BREAK, at indices `{_broke}`, asserted as a SET so a break is '
     f'REPORTABLE rather than a gate failure and a band that broke silently would turn this red: '
     f'`DELIBERATE` and `ALT-OK` come in BELOW their floors and `MEANING-HELD` comes in at `62` '
     f'against a ceiling of `20`.  ** The last is the finding: two thirds of this population is a '
     f'pin on what a paper MEANS **',
     _broke == [1, 2, 4])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE ORDER\'S OWN NEGATIVE, SCORED WITH ITS ARITHMETIC ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_ro = _dist.get('REPAIR-OWED', 0)
_share = 100.0 * _ro / 110
_all_ro = len([r for r in _rl if r[5] == 'REPAIR-OWED'])
_verdicted = len([r for r in _rl if not r[5].startswith('UNADJUDICATED')])
print(f'      REPAIR-OWED here {_ro}/110 = {_share:.1f}%;  ledger-wide {_all_ro}/{_verdicted} '
      f'verdicted = {100.0 * _all_ro / _verdicted:.1f}%')
gate(f'Ⓔ① ✔⛭⛭⛭ `r7269`\'s negative DOES NOT FIRE: `REPAIR-OWED` is `{_ro}` of `110`, '
     f'`{_share:.1f}` per cent, against the old era\'s `2.5` and the ledger\'s current '
     f'`{100.0 * _all_ro / _verdicted:.1f}`.  ** So the backlog is a VERDICTING job and not a '
     f'rewriting job wearing one, and `{len(_unl)}` is a unit that can be driven down ** --- which is '
     f'the question the order asked and the one number it could not get',
     _share < 5.0 and _ro == 3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE SECOND NEGATIVE: THE UNIT COUNTS STRINGS AND THE WORK IS READS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PATHLIT = re.compile(r"'((?:corpus|receipts|kills)/[^']+|[A-Z][A-Z0-9_]*\.md)'")
_unresolved = 0
for _r in _mine:
    _lit = json.loads(_r[1])
    _src = read(_r[0])
    _named = set(_PATHLIT.findall(_src))
    _found = False
    for _p in _named:
        _fp = os.path.join(ROOT, _p)
        if not os.path.exists(_fp):
            continue
        try:
            if _lit in read(_p):
                _found = True
                break
        except Exception:                                  # noqa: BLE001  a binary or absent file
            continue
    if not _found:
        _unresolved += 1
print(f'      keys whose read is NOT derivable from the literal and the paths its receipt names: '
      f'{_unresolved} of 110')
gate(f'Ⓕ① ✔⛭⛭ the second negative DOES NOT FIRE, and it is close: for `{_unresolved}` of the `110` '
     f'the FILE THE KEY READS is not derivable from the literal and the paths its own receipt names '
     f'--- the read is set up through a variable, a helper, or a path the assertion never spells --- '
     f'against the `55` I set as the threshold.  ** It misses by `{55 - _unresolved}`, and the first '
     f'pass of this measurement said `61` because it looked only at `corpus/` and `receipts/` paths '
     f'and not at the register files; the number that counts is the one with the wider instrument **',
     _unresolved <= 55)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓖ  THE THIRD NEGATIVE: THE TWO `OPEN` KEYS ARE ONE SENTENCE, PINNED BARE, TWICE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted(set(f for f in _git('diff', '--name-only',
                                      f'{BEFORE}..{AFTER}').split('\n') if f))
_OPENLIT = 'The substrate route is closed; the progenitor route is open'
_open_rows = [r for r in _mine if json.loads(r[1]) == _OPENLIT]
_sites = sorted(r[0] for r in _open_rows)
_bare = []
for _p in _sites:
    _src = read(_p)
    for _line in _src.split('\n'):
        if _OPENLIT in _line and ' in ' in _line:
            _bare.append(' or ' not in _line)
print(f'      the OPEN literal is pinned in {len(_sites)} receipt(s): '
      + '; '.join(s.split('/')[-1][:34] for s in _sites))
print(f'      each assertion carries NO disjunction over the two states: {_bare}')
gate(f'Ⓖ① ⛔⛭⛭⛭ the third negative FIRES: both `OPEN`-flagged keys of this population are THE SAME '
     f'SENTENCE, pinned in `{len(_sites)}` receipts, and each is a BARE `in` test with no disjunction '
     f'(`{_bare}`) --- so neither can tell `the route closed` from `the file was reworded`, and the '
     f'day the progenitor route closes both go red ON THE WORK SUCCEEDING.  ** A latent member of '
     f'the blindness family, not an unverdicted row **',
     len(_open_rows) == 2 and len(_sites) == 2 and _bare and all(_bare)
     and all(r[5] == 'REPAIR-OWED' for r in _open_rows))

gate('Ⓖ② ✔⛭ and the repair is NAMED in both rows and NOT TAKEN: each reason names the disjunction '
     'that would repair it, and NEITHER receipt is in this revision\'s diff --- the sentence is '
     'another seat\'s forward file, so the repair is routed in the reply rather than made in the turn',
     all('disjunction' in r[6] for r in _open_rows)
     and not [f for f in _touched if f in _sites])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓗ  THE RESTRAINT, AND THE DANGLING TEST ON THIS RECEIPT\'S OWN KEYS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rcpt_touched = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')]
print(f'      this revision touched {len(_touched)} file(s), {len(_rcpt_touched)} of them receipts')
gate(f'Ⓗ① ⛭ the restraint: this revision changed the LEDGER and its own receipt and NO receipt of '
     f'either prefix --- `{len(_rcpt_touched)}` receipt file(s) touched, and a verdict is a row in '
     f'the ledger rather than an edit to the gate it describes',
     BASE in _touched
     and not [f for f in _rcpt_touched if f.startswith(PREFIXES)])

_KEYS = [_OPENLIT, 'observed', 'r7270+60, L-211 backlog', 'r7270+60, L-175 backlog']
_dangling = [_k for _k in _KEYS if D.dangles(_k)]
print(f'      {len(_KEYS)} literal(s) this receipt pins, {len(_dangling)} dangling: {_dangling}')
gate(f'Ⓗ② ✔⛭ the literals this receipt pins are run through the ADOPTED dangling arms before being '
     f'written and `{len(_dangling)}` dangle --- `r7257`\'s standing order, with the arms imported '
     f'byte-for-byte rather than restated',
     not _dangling)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = [l for l, ok in CHECKS if not ok]
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** {len(_landed)} LANDED, {len(_unl)} REMAIN. **  The whole of L175 and L211.
  ✔ ** THE ORDER'S NEGATIVE DOES NOT FIRE: ** REPAIR-OWED is {_ro} of 110, {_share:.1f} per cent,
     the old era's rate -- so the backlog is a VERDICTING job and the unit can be driven down.
  ⛔ ** BUT MEANING-HELD IS 62 OF 110 AGAINST A CEILING OF 20. **  Two thirds of this population
     is a pin on what another paper MEANS, which no string form can repair -- the default for a
     receipt whose subject is another document's claim, not the rare verdict the vocabulary suggests.
  ✔ ** AND THE SECOND NEGATIVE MISSES BY SIX: ** for {_unresolved} of 110 the file the key reads is
     not derivable from the literal and the paths its own receipt names, against a threshold of 55.
  ⛔ ** AND THE TWO OPEN-FLAGGED KEYS ARE ONE SENTENCE PINNED BARE IN TWO RECEIPTS **, which goes
     red the day the route it calls open closes.  One repair, routed, not taken.
""")
sys.exit(1 if _fail else 0)
