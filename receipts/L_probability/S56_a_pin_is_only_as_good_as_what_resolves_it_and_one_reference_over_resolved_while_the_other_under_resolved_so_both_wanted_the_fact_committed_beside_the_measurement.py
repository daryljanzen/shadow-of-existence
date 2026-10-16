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

** Ⓒ THE UNDER-RESOLVING HALF, AS MEASURED AT `r7374` AND REWRITTEN HERE AT `r7418`. **  `S39`'s
`Ⓑ①` had its shas PINNED correctly and read the fact off them -- each commit's session marker -- from
a map the collision gate fills with `git log --format=%h…` and then **looks a sha up in BY EXACT
STRING**.  ⛔ *`%h` is git's abbreviation and git picks its length from the object count: at this
clone's `8` all `6` of `S39`'s shas are found, and at `7`, `9` and `12` **none** is.  So the map has
no entry, the marker reads empty, and the gate fails -- on the runner and not here.*
  ⇒ *** A PIN KEYED BY AN ABBREVIATION IS KEYED BY SOMETHING THE ENVIRONMENT CHOOSES. ***
  ⌈ ⚠ *Not claimed: that the runner's length is any particular value — asserting that would be the
    same move being corrected.  What is claimed is that the lookup matches an exact string against a
    length the environment picks, wrong whatever that length is.*
  ⌊ ** The markers are stored beside the shas now.  Where the object IS reachable they are CHECKED
    against what the commit says, so the stored data cannot drift unchallenged; where it is not, the
    stored value carries the claim and the absence is REPORTED. **  `r7365` ②, for a fact rather than
  for a selector.

⛔⛭⛭ **KEPT AS THE RECORD OF A WRONG TURN AND NOT AS A CAUSE.**  *`r7370` wrote the cause above as a
shallow clone's horizon — "that gate's own comment records it once reporting green over 8 per cent of
the corpus's revision history" — and `r7374` measured that it cannot be that.*  ⒤ **No job that runs
a receipt is shallow** — every receipt-running job in `.github/workflows/gates.yml` checks out with
`fetch-depth: 0`, read at the commit the red was recorded against, at the commit carrying the second
repair, and re-read on the trunk at `r7418` (`3a922041`) rather than inherited; the one default-depth
checkout runs LaTeX and no receipts. ⒥ **All six shas are ancestors of the trunk**, so reachable at
any depth. ⒦ **The signature reproduces from the abbreviation above**, which has nothing to do with
depth and produces the identical symptom.
  ⌈ *`r7371` `②`'s rule narrows rather than falls: the container is not the instrument for what the
    runner HAPPENS to have, but it always is for what the code DEPENDS ON, which is a property of the
    code and readable wherever the code is.*
  ⌊ ⌗ **`r7374` appended that correction BELOW the cause it refuted, here and in `S39`, so a reader
    going top-down met the false cause first — `11` lines of a `367`-line file here and `14` of `305`
    there, and in `S39` a second carrier `37` lines BELOW the correction that the correction never
    reached.  `r7418` put the measurement where the cause is read.**

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

** ⛔⛭⛭⛭ Ⓓ④ AND THE SCAN FINDS THIS FILE, WHICH IS THE THIRD TIME THIS PHASE. **  *`4` of the live
sites are in this receipt, because a gate that re-measures a match must perform the match.*
  ⇒ *** A DETECTOR RUN OVER THE CORPUS WILL ALWAYS FIND THE RECEIPT THAT DESCRIBES ITS SUBJECT, AND
      IT CANNOT TELL A MEASUREMENT OF A SHAPE FROM AN INSTANCE OF IT. ***  *`r7368`'s reporting arms,
  `r7368`'s detector counting its own remedy as its disease, and now this.*
  ⌊ ** So the describing receipt is CLASSIFIED and never repaired -- removing the match would remove
    the measurement -- and `ABOUT` is a PROPERTY, the file that CONSUMES this computation, so it
    needs no hand entry and carries no date. **

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
import ast
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


#: ⛔⛭⛭ r7420: ** THE EXCLUSION LIST BELOW WAS A HAND-WRITTEN MEMBERSHIP TEST WITH ONE ENTRY, AND IT
#: MISSED TWO MEMBERS -- INCLUDING THE ONE CARRYING 74 PER CENT OF THIS FILE'S COST. **
#:   *`r7370` wrote `_NESTS = ('S55_',)` and `Ⓖ①` asserted that all five remaining members "run
#:   nothing themselves".  `S22` runs `I55` and `S23` runs `N1` and a `P03` receipt, so the clause was
#:   FALSE for two of its five -- and the list caught only the member it was written about.*
#:   ⇒ *** The rule `r7370` stated here is right and its LIST was the defect. ***  *That is `r7412`'s
#:       eighth-instance failure again -- a census whose membership test missed a member it was about
#:       -- and the first in this phase to REPEAT a reason rather than add one.*
#:
#: ⛔⛭⛭⛭ AND THE FIRST TWO REPLACEMENTS WERE BOTH WORSE, WHICH IS WHY THE TEST BELOW IS THREE-WAY.
#:   ⒤ *A detector keyed on a `sys.executable` subprocess carrying a resolvable `receipts/` string
#:     missed `S23`: its call is `run(_n1)`, a four-line LOCAL WRAPPER whose path is a PARAMETER, so no
#:     string appears at the call site or inside the wrapper.*  **Thirteenth instance of this phase's
#:     family, and a reason it did not have.**
#:   ⒥ ⛔ *Following the wrapper fixed `S23` and then dropped `S55` -- the one entry the hand-written
#:     list had RIGHT.  `S55` runs its receipts as `[sys.executable, os.path.basename(rel)]` with the
#:     directory in `cwd`, **which is this very file's own idiom**, so there is no `receipts/` string to
#:     match.  Run with that form, this file ran `S55` whole: `1,465` s plus `S55`'s own six, the cost
#:     becoming the product this section's rule exists to prevent.*  **Fourteenth instance, caught by
#:     RUNNING the repair rather than reasoning about it -- which is what the arm registered for it was
#:     for, and `r7406`'s rule in its cheapest form.**
#:   ⇒ *** A BASENAME CANNOT BE RESOLVED STATICALLY: the directory is in `cwd` at runtime, so the
#:       question is not answerable from the source and must be REPORTED undecidable, not guessed. ***
#:   ⌊ ⛭ **And the two errors are not symmetric, which decides the disposition**: excluding a receipt
#:     that does not nest costs one re-run the suite performs anyway, while including one that does
#:     risks the product cost.  *So `undecidable` joins the exclusion, and the asymmetry is the
#:     argument rather than a preference.*
def _nest_verdict(rel):
    """'yes' | 'no' | 'undecidable' -- does this receipt hand a receipt to the interpreter?

    Decided from the parse tree where the target is a literal path, and REPORTED UNDECIDABLE where it
    is a bare basename taken from a variable, because the directory is supplied via `cwd` at runtime
    and no reading of the source can settle it."""
    try:
        tree = ast.parse(open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read())
    except (SyntaxError, OSError):
        return 'undecidable'
    binds = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant) \
                and isinstance(n.value.value, str):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    binds[t.id] = n.value.value
    wrappers = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.FunctionDef):
            continue
        params = {a.arg for a in n.args.args} | ({n.args.vararg.arg} if n.args.vararg else set())
        for c in ast.walk(n):
            if isinstance(c, ast.Call) and "attr='executable'" in ast.dump(c) \
                    and any(isinstance(x, ast.Name) and x.id in params for x in ast.walk(c)):
                wrappers.add(n.name)
    verdict = 'no'
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        nm = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
        direct = (nm in ('run', 'check_output', 'Popen', 'check_call') and n.args
                  and "attr='executable'" in ast.dump(n.args[0]))
        if not (direct or nm in wrappers):
            continue
        strs, basename = [], False
        for a in n.args:
            for x in ast.walk(a):
                if isinstance(x, ast.Constant) and isinstance(x.value, str):
                    strs.append(x.value)
                elif isinstance(x, ast.Name) and x.id in binds:
                    strs.append(binds[x.id])
                elif isinstance(x, ast.Attribute) and x.attr == 'basename':
                    basename = True
        if any(re.search(r'(^|/)receipts/', t) for t in strs):
            return 'yes'
        if basename and not any(re.search(r'(^|/)(corpus|scripts)/', t) for t in strs):
            verdict = 'undecidable'
    return verdict


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
    #: ⛭⛭ r7370: the first form of this clause pinned `len(_stored) == 6` -- a COUNT of matches in
    #: another file's source, which is the prose-pin class and the second time this revision wrote
    #: one.  *The claim was never the count: it is that every sha the file PINS has a stored marker
    #: and every stored marker belongs to a pinned sha.*  ⇒ A CORRESPONDENCE, which is set equality
    #: and moves correctly if `PAIRS` ever grows or shrinks.
    _pinned_shas = set(re.findall(r"'([0-9a-f]{8})'", _s39[_s39.index('PAIRS = '):
                                                           _s39.index('SESSIONS = ')]))
    check(f'Ⓒ① the fact is COMMITTED BESIDE THE MEASUREMENT and checked against the commit wherever '
          f'this clone reaches it: {len(_stored)} marker(s) stored for the {len(_pinned_shas)} shas '
          f'the file pins -- a CORRESPONDENCE and not a count, so it moves with `PAIRS` -- and '
          f'{len(_agree)} verified here, so the stored data cannot drift unchallenged',
          {h for h, _m in _stored} == _pinned_shas and _pinned_shas
          and len(_agree) == len(_stored))
    #: ⛭⛭ r7418: this clause's own text named TWO mechanisms -- "a map a shallow clone truncates and
    #: a different abbreviation length empties (r7374)" -- citing the revision that refuted the first
    #: while still asserting it.  *A comment records a belief; an asserting clause states a property
    #: of the object, so the refuted half was being asserted and not merely remembered.*  ⇒ Only the
    #: measured mechanism is named now; the refuted one is kept in the header above, as a record.
    check('Ⓒ② ⇒ and the map it used to depend on is gone from the clause: the marker is read from '
          'the commit by id, which git resolves from any prefix, rather than out of a map KEYED BY '
          'AN ABBREVIATION -- a key whose length git picks from the object count, so a different '
          'length empties it (r7374)',
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
    check(f'Ⓓ④ ⛔⛭⛭⛭ AND THE SCAN FINDS THIS FILE: {R["A_LIVE_ABOUT"]} of the live sites are in '
          f'THIS receipt, which must perform the match to re-measure it.  ** A detector run over '
          f'the corpus will ALWAYS find the receipt that describes its subject, and it cannot tell '
          f'a measurement of a shape from an instance of it. **  ⇒ *Third time this phase: '
          f'`r7368`\'s reporting arms, `r7368`\'s detector counting its own remedy as its disease, '
          f'and now this -- so the describing receipt is CLASSIFIED and never repaired, because '
          f'removing the match would remove the measurement.*  ⌗ *`ABOUT` is a PROPERTY -- the file '
          f'that CONSUMES this computation -- so it needs no hand entry and carries no date*',
          R['A_LIVE_ABOUT'] == 4 and '_THIS in _t' in open(COST, encoding='utf-8').read())

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
    #: ⛔⛭⛭ r7370: ** AND "RUN HERE, NOT CITED" COMPOUNDS WHEN A RECEIPT THAT RUNS RECEIPTS IS
    #: ITSELF RUN. **  *The first form of this clause ran all six, and `S55` is one of them -- and
    #: `S55`'s own `Ⓖ①` runs six more, including `S51`.  So this file took `S55`'s whole cost plus
    #: five, the suite paid for `S51` three times over (directly, through `S55`, through here), and
    #: one receipt's run time became the product of a chain rather than the sum of a list.*
    #:   ⇒ *** The convention is right and its COST IS NOT LINEAR.  A receipt that runs receipts is
    #:       asserted on the CHANGE THIS REVISION MADE TO IT, not re-run whole: it is in the suite's
    #:       own scope and the suite runs it once, which is where running it belongs. ***
    #: ⌊ *So the five that run nothing are RUN, and `S55` is read for the one thing this revision
    #:   changed in it -- which is a stronger claim about this revision's work than its exit code.*
    _VERDICTS = {p: _nest_verdict(one(p)) for p in REDS + MORE}
    _NESTS = tuple(sorted(p for p, v in _VERDICTS.items() if v in ('yes', 'undecidable')))
    _rcs = {}
    for p in REDS + MORE:
        if p in _NESTS:
            continue
        rel = one(p)
        _rcs[p[:-1]] = subprocess.run([sys.executable, os.path.basename(rel)],
                                      cwd=os.path.join(ROOT, os.path.dirname(rel)),
                                      capture_output=True, text=True, errors='replace',
                                      timeout=2400).returncode
    _INDEX = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
    print(f'      run here, not cited: {_rcs}')
    print(f'      not re-run, COMPUTED from their own source rather than remembered: {list(_NESTS)} '
          f'-- each runs a receipt of its own, so running it here makes this file\'s cost a product '
          f'rather than a sum; each is registered in the index and the suite runs it once')
    check(f'Ⓖ① every member that runs nothing itself is RUN from its own directory and exits zero, '
          f'and the population is DERIVED from each file\'s parse tree rather than pinned: '
          f'{_rcs} against a nesting set of {list(_NESTS)}, {len(_rcs)} + {len(_NESTS)} = '
          f'{len(REDS + MORE)}',
          _rcs and all(v == 0 for v in _rcs.values())
          and len(_rcs) + len(_NESTS) == len(REDS + MORE)
          and all(_VERDICTS[p] == 'no' for p in REDS + MORE if p not in _NESTS))
    check(f'Ⓖ①ᵃ ⛭ and every member that DOES run a receipt is asserted on its registration rather '
          f'than re-run whole -- `r7370`\'s own rule, which it applied to one member and this file '
          f'now applies to all {len(_NESTS)} the parse tree finds: each is in the index, so the '
          f'suite runs it once, which is where running it belongs',
          len(_NESTS) >= 1
          and all(os.path.basename(one(p)) in _INDEX for p in _NESTS))
    check('Ⓖ①ᵇ ⛭ and `S55` keeps the specific form too: it is asserted on THE CHANGE THIS REVISION '
          'MADE TO IT -- its id filter is gone and its restraint reads the whole session-filtered '
          'range -- which is a stronger claim about this revision\'s work than its exit code',
          "_r68 = _own" in _s55 and "'r7368' in git(" not in _s55
          and os.path.basename(one('S55_')) in _INDEX)
    check(f'Ⓖ①ᶜ ⛔⛭ and the PREVIOUS form\'s hand-written list missed two of them: it carried '
          f'`S55` alone while the three-way test finds {len(_NESTS)}, so the clause asserting that '
          f'all five others "run nothing themselves" was FALSE for two -- `r7412`\'s membership-test '
          f'failure again, and the first in this phase to repeat a reason rather than add one.  '
          f'⛭ AND THE COMPUTED SET CONTAINS THE OLD ONE rather than contradicting it: {list(_NESTS)}',
          len(_NESTS) > 1 and 'S55_' in _NESTS)
    _undec = sorted(p for p, v in _VERDICTS.items() if v == 'undecidable')
    check(f'Ⓖ①ᵈ ⛔⛭⛭ and the test is THREE-WAY because a basename cannot be resolved from the '
          f'source: the directory is in `cwd` at runtime.  Undecidable: {_undec}; nesting: '
          f'{sorted(p for p, v in _VERDICTS.items() if v == "yes")}; clear: '
          f'{sorted(p for p, v in _VERDICTS.items() if v == "no")}.  ** Undecidable joins the '
          f'exclusion, and the ASYMMETRY is the argument: excluding a receipt that does not nest '
          f'costs one re-run the suite performs anyway, while including one that does risks the '
          f'product cost this section exists to prevent **',
          set(_VERDICTS.values()) <= {'yes', 'no', 'undecidable'}
          and all(p in _NESTS for p in _undec))

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
