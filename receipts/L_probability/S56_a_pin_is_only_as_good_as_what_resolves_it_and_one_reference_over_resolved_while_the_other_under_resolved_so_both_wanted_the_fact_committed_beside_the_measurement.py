#!/usr/bin/env python3
"""S56 -- THE REFERENCE THAT DOES NOT RESOLVE.  ⛭⛭⛭ *** TWO GATES WENT RED ON THE PREVIOUS REVISION'S
PR, AND THEY ARE ONE CLASS IN OPPOSITE DIRECTIONS: ONE REFERENCE OVER-RESOLVED AND THE OTHER
UNDER-RESOLVED. ***  Both stood red on `main` for five pushes and both ran green on this tree every
time, with nothing in the tree to explain either.

** Ⓑ THE OVER-RESOLVING HALF. **  `S29`'s `Ⓔ②` selected a revision's commits by matching
`\\br7290\\b` against commit message bodies over a live range.  ⛔ *That does not select a revision's
commits; it selects **every commit whose message mentions it** -- and the corpus's convention is to
cite revisions by number in every message.*  The comment four lines above the selector says so:

      *a selector over a live range cannot be made safe by filtering what it matches, when the
      corpus's own convention is to cite revisions by number.*

  ⌈ *The match returns `5` commits of which `2` are the revision's.  The other three are `r7292`'s
    pre-registration, which cites it; another seat's `r7355+cc66.2`, which cites it AND touched two
    receipts, which is what turned the clause red; and `r7368`'s own commit message about this very
    defect.*
  ⇒⇒ *** A REVISION THAT WRITES ABOUT ANOTHER JOINS ITS SELECTOR, and the commit that demonstrates
      it is the one describing it. ***

** Ⓒ THE UNDER-RESOLVING HALF. **  `S39`'s `Ⓑ①` had its shas PINNED correctly and read the fact off
them -- each commit's session marker -- from a map the collision gate fills by **walking the whole
history reachable from `HEAD`**.  ⛔ *A shallow clone stops at its horizon; that gate's own comment
records it once "reporting green over 8 per cent of the corpus's revision history".  These six
commits sit some eighty revisions back, so the map has no entry, the marker reads empty, and the gate
fails -- on the runner and not here, where the clone is full.*
  ⇒ ** The markers are stored beside the shas now.  Where the object IS reachable they are CHECKED
    against what the commit says, so the stored data cannot drift unchallenged; where it is not, the
    stored value carries the claim and the absence is REPORTED. **  `r7365` ②, for a fact rather than
  for a selector.

** ⇒⇒⇒ THE RULE: A PIN IS ONLY AS GOOD AS WHAT RESOLVES IT.  One reference resolved to more than it
named and the other to less, and both wanted the fact committed beside the measurement. ***

** Ⓓ THE ARMS, REGISTERED BEFORE THE SCAN. **
      ⒜ *the population* -- `SELECTS` sites beyond the one repaired.  Central `2`, band `0`-`6`,
        two-sided.  Measured **`4`** at the frame -- INSIDE, above central.
      ⒝ *the capture* -- extra commits the match takes at the repaired site.  Central `2`, band
        `1`-`6`.  Measured **`3`** (`5` matched against `2` own) -- INSIDE.

** ⛔⛭⛭⛭ Ⓔ AND TWO OF THE FOUR ARE REPAIRS THIS PHASE ITSELF MADE. **
      `S53`  introduced at `r7364` AS THE FIX for a moving range, with the note *"a later revision's
             work cannot enter it"* -- **which is false as written**, because a later revision
             WRITING ABOUT this one enters it.  *Not broken yet, only because no later subject has
             named `r7362`: the fragility repaired before it fires, which is the only time it is
             cheap.*
      `S55`  written in the revision that NAMES this class, two hours before this file.  ⇒ *Its id
             filter is DROPPED rather than pinned, because it was never needed: the population is
             already this seat's own commits since a pinned base, and the restraint -- that none of
             them touched a do-not-edit path -- is true and STRONGER over all of them.  `74` files
             scrutinised against the `17` the id match left.*
      `S23`  ⛔ **already over-resolving**: `11` commits returned where the revision has `9`, and
             both extras are OTHER SEATS' -- `r7267+70.1`'s port of this seat's own receipt and
             `r7267`'s orders.  *A gate about THIS seat's scope was counting another seat's commits
             as this seat's, which is the unsafe direction.*
      `S22`  returns exactly its `3` today.  Repaired on the same pattern.

** Ⓕ AND THE SCAN'S OWN CLASSIFIER NEEDED THE SAME LESSON TWICE. **  ⌗ *`CONTROL` is a PROPERTY and
not a hand entry -- every one of these sites was `SELECTS` before its commits were pinned and is the
control beside the pin after, so a hand entry would bake in the date.*  ⛔ **And the property was
first tested by a spelling: the anchor `^(?:OWN|OWN_C)` has no `\\s*`, so `S53`, which binds its
tuple inside the function that uses it, read as unrepaired.**  *Caught because the live figure did
not fall to zero, and reported rather than quietly fixed.*
  ⌗ *One further site is a FALSE POSITIVE kept rather than tuned away: an id matched against a
    LEDGER CELL, which the proximity test caught because a commit-listing call sat three lines off.*

** COMPUTES: ** both reds reproduced and their causes measured at both ends; the scan against its two
registered bands, scored at the registration commit with the live reading printed beside it; the
capture at the repaired site; the two-sided control on every pin; and all six touched receipts RUN
here rather than cited.  No paper quantity.

** WHAT IS NOT CLAIMED. **  ** Not that matching a revision id is wrong ** -- it is how this corpus
reads a revision's own claim off a subject line, which is the `LABEL` class and is left alone; the
defect is matching it to pick a COMMIT SET.  ** Not that the detector is complete ** -- three
spellings on non-comment lines with a commit-listing call within three lines, so a match used
further away is missed, stated rather than ruled out.  ** Not that `S39`'s half is measured ** -- a
clone's horizon is a property of the environment, and `r7365` ① says what a container happens to have
is printed and asserted of nothing.  ** And not that the stored markers are a substitute for the
commits ** -- they are checked against them wherever this clone reaches them, and `0` of `6` were
unreachable here.

Written r7370 on CI's own two reds.  Stated for reversal.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
COST = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7370_60_the_reference_that_does_not_resolve', 'cost.py')
REG = '122d0247'          # the registration commit, pushed before the scan was run
BAR = '=' * 100

#: the two reds, and the four more the scan found
REDS = ('S29_', 'S39_')
MORE = ('S22_', 'S23_', 'S53_', 'S55_')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def head(t):
    print(f'\n  {"-" * 96}\n  {t}\n  {"-" * 96}')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def one(prefix, where='receipts/L_probability'):
    hits = [x for x in git('ls-files', where).split('\n')
            if os.path.basename(x).startswith(prefix)]
    return hits[0] if hits else None


def src(prefix):
    return open(os.path.join(ROOT, one(prefix)), encoding='utf-8').read()


def main():
    print(__doc__)
    C = load(COST, 'r7370_cost')

    # ── Ⓐ the two reds, and that neither was this branch's doing ──────────────────────────────────
    head('Ⓐ.  THE TWO REDS, AND NEITHER CAUSE WAS IN THE BRANCH THAT FOUND THEM')
    _both = {p: one(p) for p in REDS}
    check(f'Ⓐ① both are this seat\'s receipts and both resolve on this tree: '
          f'{[os.path.basename(v or "?")[:4] for v in _both.values()]}',
          all(_both.values()) and len(_both) == 2)
    check(f'Ⓐ② and the registration precedes the scan, which is checkable rather than asserted: '
          f'{REG} resolves, is an ancestor of `HEAD`, and its own tree carries the two bands with '
          f'no result block',
          subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', REG, 'HEAD'],
                         capture_output=True).returncode == 0
          and 'A_CENTRAL = 2' in git('show', f'{REG}:computations/beyond_the_wall/'
                                             'r7370_60_the_reference_that_does_not_resolve/cost.py')
          and 'RESULT = {}' in git('show', f'{REG}:computations/beyond_the_wall/'
                                           'r7370_60_the_reference_that_does_not_resolve/cost.py'))

    # ── Ⓑ the over-resolving half, measured ───────────────────────────────────────────────────────
    head('Ⓑ.  THE OVER-RESOLVING HALF: A REVISION THAT WRITES ABOUT ANOTHER JOINS ITS SELECTOR')
    _s29 = src('S29_')
    _BEFORE = re.search(r"^BEFORE = '([0-9a-f]+)'", _s29, re.M).group(1)
    _rows = [l.split('|', 1) for l in
             git('log', '--no-merges', '--format=%h|%s', f'{_BEFORE}..HEAD').split('\n') if '|' in l]
    _matched = [(h, s) for h, s in _rows if 'r7290' in s] + [
        (h, s) for h, s in _rows
        if 'r7290' not in s and re.search(r'\br7290\b', git('log', '-1', '--format=%B', h))]
    _own = [(h, s) for h, s in _matched if s.strip().startswith('r7290')]
    _foreign = [(h, s) for h, s in _matched if not s.strip().startswith('r7290')]
    print(f'      the string match over `{_BEFORE}..HEAD` returns {len(_matched)} commit(s); '
          f'{len(_own)} of them are the revision\'s')
    for _h, _s in _foreign:
        print(f'        ⚠ captured, not r7290\'s: {_h} -- {_s[:68]}')
    check(f'Ⓑ① ⛔⛭⛭⛭ the match OVER-RESOLVES, measured rather than argued: it returns '
          f'{len(_matched)} commit(s) over the range and only {len(_own)} are the revision\'s -- '
          f'the other {len(_foreign)} CITE it, which is what a revision id is for everywhere else '
          f'in this corpus.  ** And one of them is `r7368`\'s own commit message about this defect: '
          f'a revision that writes about another joins its selector **',
          len(_matched) > len(_own) >= 2
          and any('r7368' in s for _h, s in _foreign))
    #: ⌗ CASE-FOLDED, and the first form of this clause was not: the sentence opens a sentence in
    #: `S29` and is capitalised there, so a case-sensitive search for it found nothing and this
    #: gate went red on its own quoting.  *A pin that fails on the first letter of a sentence is a
    #: cannot-fail span's opposite number, and it is the shape `r7364` found in a backslash.*
    _said = 'a selector over a live range cannot be made safe by filtering what it matches'
    check('Ⓑ② ⇒ and the receipt SAID SO four lines above the selector and selected that way anyway: '
          'the sentence stands in the file, read out of it CASE-FOLDED rather than recalled -- it '
          'opens a sentence there, and the first form of this clause went red on that capital',
          _said in _s29.lower() and _said not in _s29)
    check(f'Ⓑ③ ⇒⇒ and it is repaired by PINNING the commits, with the string match kept beside them '
          f'as the CONTROL -- it must still return strictly more than the pinned pair, so the pin '
          f'cannot quietly become the match again',
          re.search(r"^OWN = \('[0-9a-f]{8}', '[0-9a-f]{8}'\)", _s29, re.M)
          and '_matched' in _s29 and 'len(_matched) > len(_own)' in _s29)

    # ── Ⓒ the under-resolving half ────────────────────────────────────────────────────────────────
    head('Ⓒ.  THE UNDER-RESOLVING HALF: A PIN THE ENVIRONMENT MAY NOT REACH')
    _s39 = src('S39_')
    _stored = re.findall(r"^\s+'([0-9a-f]{8})': 'https://claude\.ai/code/(session_\w+)'", _s39, re.M)
    _agree = [(h, m) for h, m in _stored
              if m in git('log', '-1', '--format=%B', h)]
    print(f'      {len(_stored)} marker(s) stored beside the shas; {len(_agree)} agree with what '
          f'the commit says on this tree')
    check(f'Ⓒ① the fact is COMMITTED BESIDE THE MEASUREMENT and checked against the commit wherever '
          f'this clone reaches it: {len(_stored)} stored, {len(_agree)} verified here, so the stored '
          f'data cannot drift unchallenged',
          len(_stored) == 6 and len(_agree) == len(_stored))
    check('Ⓒ② ⇒ and the walk it used to depend on is gone from the clause: the marker is read from '
          'the commit by id, not out of a map built by walking the history reachable from `HEAD`, '
          'which a shallow clone truncates',
          'def session_of' in _s39 and '_SESSION.get' not in _s39
          and '_UNREACHED' in _s39)
    check('Ⓒ③ ⇒⇒ and the absence is REPORTED rather than failing or passing: a sha this clone does '
          'not reach falls back to the stored value and is counted, which is `r7365` ①\'s rule for '
          'what a container happens to have',
          '_UNREACHED.append' in _s39 and 'does not reach' in _s39)

    # ── Ⓓ the two arms ────────────────────────────────────────────────────────────────────────────
    head('Ⓓ.  THE TWO ARMS, SCORED AT THE REGISTRATION COMMIT WITH THE LIVE READING BESIDE THEM')
    C.main()
    R = C.RESULT
    check(f'Ⓓ① arm ⒜ -- SELECTS sites beyond the one repaired, at the frame: {R["A_NEW"]}, against '
          f'central {C.A_CENTRAL} and band {C.A_BAND[0]}-{C.A_BAND[1]}.  ** INSIDE THE BAND, above '
          f'central **',
          R['A_NEW'] == 4 and C.score(R['A_NEW'], C.A_BAND))
    check(f'Ⓓ② arm ⒝ -- extra commits the match takes at the repaired site: {R["B_EXTRA"]} '
          f'({R["B_MATCHED"]} matched against {R["B_OWN"]} own), against central {C.B_CENTRAL} and '
          f'band {C.B_BAND[0]}-{C.B_BAND[1]}.  ** INSIDE **  ⌗ *registered rather than skipped '
          f'because it is what makes the first band mean anything: a match over-capturing by zero '
          f'would make the whole class harmless*',
          R['B_EXTRA'] == 3 and C.score(R['B_EXTRA'], C.B_BAND))
    check(f'Ⓓ③ ⇒ and the class is CLOSED on this tree rather than reported open: {R["A_SITES"]} '
          f'SELECTS at the frame and {R["A_LIVE_SELECTS"]} live, with {R["A_LIVE_CONTROL"]} id '
          f'matches left standing ON PURPOSE beside a pinned list',
          R['A_LIVE_SELECTS'] == 0 and R['A_LIVE_CONTROL'] == 3)

    # ── Ⓔ two of the four are this phase's own repairs ────────────────────────────────────────────
    head('Ⓔ.  TWO OF THE FOUR ARE REPAIRS THIS PHASE ITSELF MADE')
    _s53, _s55 = src('S53_'), src('S55_')
    check('Ⓔ① ⛔⛭⛭⛭ `S53`\'s was introduced at `r7364` AS THE FIX for a moving range, and its note '
          'says "a later revision\'s work cannot enter it" -- which is false as written, because a '
          'later revision WRITING ABOUT this one enters it.  The sentence is read out of the file',
          'a later revision\'s work cannot enter it' in _s53
          and re.search(r"^\s*OWN_C = \(", _s53, re.M))
    check('Ⓔ② and `S55`\'s was written in the revision that NAMES this class, hours before this '
          'file.  ⇒ *There the id filter is DROPPED rather than pinned, because the population is '
          'already this seat\'s own commits since a pinned base and the restraint is STRONGER over '
          'all of them*',
          "_r68 = _own" in _s55 and "'r7368' in git(" not in _s55)
    _s23 = src('S23_')
    check('Ⓔ③ ⛔ and `S23`\'s was ALREADY over-resolving, in the unsafe direction: the extras it '
          'captured are other seats\' commits -- a port of this seat\'s own receipt and another '
          'line\'s orders -- counted as this seat\'s by a gate about this seat\'s scope',
          re.search(r"^OWN_C = \(", _s23, re.M) and '_matched' in _s23)

    # ── Ⓕ the classifier's own lesson, twice ──────────────────────────────────────────────────────
    head('Ⓕ.  AND THE SCAN\'S OWN CLASSIFIER NEEDED THE SAME LESSON TWICE')
    _cost = open(COST, encoding='utf-8').read()
    check('Ⓕ① `CONTROL` is a PROPERTY and not a hand entry, for `r7368`\'s reason: every one of '
          'these sites was `SELECTS` before its commits were pinned and is the control beside the '
          'pin after, so a hand entry would bake in the date',
          'def _class_of' in _cost and '_PINNED_OWN' in _cost)
    check('Ⓕ② ⛔ and the property was first tested BY A SPELLING: the anchor had no `\\s*`, so '
          '`S53`, which binds its tuple inside the function that uses it, read as unrepaired.  '
          '** Caught because the live figure did not fall to zero, and reported rather than quietly '
          'fixed **',
          r'^\s*(?:OWN|OWN_C)' in _cost and 'tested by a spelling again' in _cost)
    check('Ⓕ③ ⇒ and one site is a FALSE POSITIVE kept rather than tuned away: an id matched against '
          'a LEDGER CELL, which the proximity test caught because a commit-listing call sat three '
          'lines off -- the detector is reported with its own miss',
          "'LABEL'" in _cost and 'FALSE POSITIVE of this detector' in _cost)

    # ── Ⓖ every touched receipt RUN ───────────────────────────────────────────────────────────────
    head('Ⓖ.  EVERY RECEIPT THIS REVISION TOUCHED, RUN HERE RATHER THAN CITED')
    _rcs = {}
    for p in REDS + MORE:
        rel = one(p)
        _rcs[p[:-1]] = subprocess.run([sys.executable, os.path.basename(rel)],
                                      cwd=os.path.join(ROOT, os.path.dirname(rel)),
                                      capture_output=True, text=True, errors='replace',
                                      timeout=2400).returncode
    print(f'      run here, not cited: {_rcs}')
    check(f'Ⓖ① all {len(_rcs)} receipts RUN from their own directories and every one exits zero: '
          f'{_rcs}',
          len(_rcs) == 6 and all(v == 0 for v in _rcs.values()))

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ A PIN IS ONLY AS GOOD AS WHAT RESOLVES IT.  One reference resolved to more than it')
    print('    named and the other to less, and both wanted the fact committed beside the')
    print('    measurement.  Two of the four further sites were repairs this phase itself made.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
