#!/usr/bin/env python3
"""S58 -- THE KEY THE ENVIRONMENT CHOOSES.  ⛭⛭⛭ *** `r7370` REPAIRED `S39`'s `Ⓑ①` AND WROTE THE CAUSE
BESIDE IT TWICE OVER -- IN `S39` AND IN `S56` -- AS A SHALLOW CLONE'S HORIZON.  THE REPAIR IS RIGHT.
THE REASON IS FALSE. ***

** Ⓐ NO JOB THAT RUNS A RECEIPT IS SHALLOW. **  Read out of `.github/workflows/gates.yml` at the
commit the red was recorded against, at the commit that carried the second repair, and at the trunk:
every receipt-running job checks out with `fetch-depth: 0`.  *The one default-depth checkout is
`compile`, which runs LaTeX and no receipts -- so the clause is two-sided: a shallow checkout DOES
exist in this workflow, and it is not one that can have run `S39`.*

** Ⓑ AND ALL SIX PINNED SHAS ARE ANCESTORS OF THE TRUNK, ** so `git log` from `HEAD` reaches them at
any depth on any branch based on it.  *Whatever emptied that map, it was not the horizon.*

** Ⓒ THE SIGNATURE REPRODUCES HERE, FROM A VARIABLE WITH NOTHING TO DO WITH DEPTH. **  The gate builds
its map with `git log --format=%h…` and looks a sha up in it by EXACT STRING.  `%h` is **git's**
abbreviation, and git picks its length from the object count unless told otherwise.  Running the
gate's own map-building command at four lengths:

      core.abbrev   key length   of the six pinned shas, found
      unset             8            6 of 6
      7                 7            0 of 6
      9                 9            0 of 6
      12               12            0 of 6

  ⇒ *** A PIN KEYED BY AN ABBREVIATION IS KEYED BY SOMETHING THE ENVIRONMENT CHOOSES. ***  *Same tree,
      same commits, nothing edited -- and the map misses ALL SIX the moment the length is not this
      clone's.  That is exactly "the map has no entry for them", and the match here is an accident of
      this environment rather than a property of the pin.*
  ⌊ ⚠ *NOT claimed: that the runner's abbreviation length is `7`, or any value.  It cannot be seen from
    here, and asserting it would be the same move being corrected.  What is claimed is that the lookup
    matches an exact string against a length the environment picks -- wrong whatever that length is,
    and the only mechanism `Ⓐ` and `Ⓑ` leave standing.*

** ⛭⛭ Ⓓ AND IT NARROWS A RULE RATHER THAN A COMMENT. **  `r7371` `②` recorded, from `r7370`'s own line,
that *"the container is not the instrument for a claim about the runner"*.  Both halves of this claim
about the runner were decidable in the container: the workflow file names every checkout's depth, and
`core.abbrev` reproduces the failure on this tree.
  ⇒ *** THE RULE HOLDS FOR WHAT THE RUNNER HAPPENS TO HAVE AND NOT FOR WHAT THE CODE DEPENDS ON. ***
      *The second is a property of the code and is readable wherever the code is.*

** ⛔ Ⓔ THE ARM AS REGISTERED CANNOT BE MEASURED, AND THE WAY IT CANNOT IS THE FINDING. **  Arm ⒜ asked
for sites that take git's abbreviated OUTPUT and match it as a string.  A WINDOW form returned **`18`**
and over-counted -- it took `--abbrev-ref`, which abbreviates a REF and has no environment-chosen
length, and a line whose `==` compares a COUNT.  A STRUCTURAL form, the abbreviation flowing into a
comparison or lookup against a pinned abbreviation in the same file, returned **`0`** and missed the
one site that fired.
  ⇒ ** Both fail for one reason: THE TWO ENDS OF THE KEY ARE IN DIFFERENT FILES. **  *The gate BUILDS
    the map and takes the sha as a parameter; the receipt SUPPLIES the pinned abbreviation from another
    file, across a function boundary and across seats.  A locality detector cannot see a defect whose
    halves nobody owns together -- which is why it stood for five pushes with a green receipt and a red
    runner.*
  ⌊ *So the measurable unit is the PAIRING: `1` map keyed by an abbreviation, `1` caller, and the caller
    no longer DEPENDS on it.  Both detector forms are kept in `cost.py`, because a detector whose
    predecessor's figure cannot be reproduced cannot be shown to have improved.*

** Ⓕ ONE ASYMMETRY WORTH THE LINE. **  Of the corpus's `163` pinned abbreviations, `133` are `8`
characters and `30` are not.  *All `105` of this seat's are `8` -- this clone's own auto-length, which
every one of its `5,539` revision-numbered commits renders at, and no other.*

    python3 receipts/L_probability/S58_the_repair_was_right_and_the_reason_written_beside_it_was_false_because_a_pin_keyed_by_an_abbreviation_is_keyed_by_a_length_the_environment_picks.py
"""
import ast
import importlib.util
import io
import os
import re
import subprocess
import sys
import tokenize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BAR = '=' * 100

COST = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7374_60_the_key_the_environment_chooses', 'cost.py')
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')
#: the two names `Ⓔ②` reads off S39's syntax tree: its own definition, and the
#: instrument's method it checks that definition against
LOCAL = 'same_line'
ATTR = '_same_line'


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
    C = load(COST, 'r7374_cost')
    _src = open(os.path.abspath(__file__), encoding='utf-8').read()

    # ── Ⓐ the workflow, read rather than remembered ───────────────────────────────────────────────
    head('Ⓐ  no job that runs a receipt is shallow, at three pinned commits')
    _d = {sha: C.depths(sha) for sha in (C.RED_AT, C.REPAIR_AT, C.TRUNK)}
    _default = {sha: sorted(j for j, v in d.items() if v == 'default') for sha, d in _d.items()}
    _runs = {sha: {j: C.runs_receipts(sha, j) for j in js} for sha, js in _default.items()}
    for sha, d in _d.items():
        print(f'      {sha}: {len(d)} checkout(s), '
              f'{sum(1 for v in d.values() if v == "full")} full, default {_default[sha]} '
              f'-- runs receipts: {_runs[sha]}')
    check(f'Ⓐ① at all three pinned commits every default-depth checkout runs NO receipt, so no job '
          f'that could have run `S39` was shallow: {_runs}',
          len(_d) == 3 and all(d for d in _d.values())
          and all(not any(r.values()) for r in _runs.values()))
    check(f'Ⓐ② and the clause is TWO-SIDED rather than vacuous -- a default-depth checkout DOES exist '
          f'in this workflow at every one of the three commits, it is just not one that runs a '
          f'receipt: {sorted({j for js in _default.values() for j in js})}',
          all(len(js) >= 1 for js in _default.values()))

    # ── Ⓑ reachability ────────────────────────────────────────────────────────────────────────────
    head('Ⓑ  all six pinned shas are ancestors of the pinned trunk')
    _anc = [p for p in C.PINS_S39 if C.subprocess.run(
        ['git', '-C', ROOT, 'merge-base', '--is-ancestor', p, C.TRUNK],
        capture_output=True).returncode == 0]
    _live = git('rev-parse', '--short=8', 'origin/main').strip()
    print(f'      {len(_anc)} of {len(C.PINS_S39)} on the pinned trunk {C.TRUNK}')
    print(f'      the live trunk reads {_live} -- REPORTED, asserted of nothing (r7368 ②)')
    check(f'Ⓑ① every one of the {len(C.PINS_S39)} pinned shas is reachable from the pinned trunk, so '
          f'the horizon cannot be what emptied the map: {len(_anc)} of {len(C.PINS_S39)}',
          len(_anc) == len(C.PINS_S39) and len(C.PINS_S39) == 6)

    # ── Ⓒ the reproduction ────────────────────────────────────────────────────────────────────────
    head('Ⓒ  the signature reproduces here, from the abbreviation length')
    _found, _lens = {}, {}
    for ab in C.ABBREVS:
        keys = C.map_at(ab)
        _found[ab] = sum(1 for p in C.PINS_S39 if p in keys)
        _lens[ab] = sorted({len(k) for k in keys})
        print(f'      core.abbrev={str(ab):5} key length(s) {_lens[ab]:} '
              f'-> {_found[ab]} of {len(C.PINS_S39)} found')
    #: ⛔⛭⛭⛭ r7398: ** THESE TWO CLAUSES WERE KEYED TO THIS CONTAINER'S ABBREVIATION LENGTH, WHICH IS
    #: THE DEFECT THIS RECEIPT REPORTS -- THE FIFTH INSTANCE OF THE CLASS AND THE FIRST THAT WAS FALSE
    #: RATHER THAN MERELY SELF-REFERENTIAL. **  *`Ⓒ①` asserted that at the unset length all six pins are
    #: found and `Ⓒ②` that the map's key length EQUALS the pins' -- both true here, where git's
    #: auto-choice is `8`, and both FALSE wherever it is not.  CI's carry named exactly these two
    #: gates, and forcing `core.abbrev=7` in this container reproduces it: `0 of 6` at every length.*
    #:   ⇒ ** THE ENVIRONMENT-INDEPENDENT CLAIM IS THE ONE THE FINDING ACTUALLY MAKES: the pins are
    #:     found at a tested length EXACTLY WHEN that length equals the pins' own. **  *That is a
    #:     statement about string equality, true in every environment, and it is what "a pin keyed by
    #:     an abbreviation is keyed by a length the environment picks" means.  The container's own
    #:     length is MEASURED and REPORTED rather than assumed -- `r7365` ①'s rule, which this gate
    #:     was breaking while its own docstring cited it.*
    _pin_len = sorted({len(p) for p in C.PINS_S39})
    _here_len = _lens[None]
    print(f'      this clone`s own key length: {_here_len} -- MEASURED, not assumed; '
          f'the pins are {_pin_len} long')
    _iff = {ab: (_found[ab] == len(C.PINS_S39)) == (_lens[ab] == _pin_len) for ab in C.ABBREVS}
    check(f'Ⓒ① at every tested length the pins are found EXACTLY WHEN that length equals their own '
          f'-- a property of string equality, true in any environment, and the whole of what "keyed '
          f'by a length the environment picks" means: {_iff}, found {_found}, lengths '
          f'{ {k: v for k, v in _lens.items()} }',
          all(_iff.values()) and len(C.ABBREVS) >= 4
          and any(_lens[ab] != _pin_len for ab in C.ABBREVS))
    check(f'Ⓒ② and the map\'s keys are UNIFORM in length at every tested setting, which is what makes '
          f'the lookup all-or-nothing rather than partial -- so a length that is not the pins\' misses '
          f'ALL of them and not some: {[(ab, _lens[ab], _found[ab]) for ab in C.ABBREVS]}',
          all(len(_lens[ab]) == 1 for ab in C.ABBREVS)
          and all(_found[ab] in (0, len(C.PINS_S39)) for ab in C.ABBREVS))

    # ── Ⓓ the correction is written where the reason was ──────────────────────────────────────────
    head('Ⓓ  the correction is in both receipts, and the repair is unchanged')
    _s39, _s56 = src('S39_'), src('S56_a_pin_is_only')
    _said = 'keyed by an abbreviation is keyed by something the environment chooses'
    check(f'Ⓓ① both receipts that carry the false reason now carry the correction beside it, naming '
          f'this revision: S39 {("r7374" in _s39)}, S56 {("r7374" in _s56)}',
          'r7374' in _s39 and 'r7374' in _s56
          and _said in _s39.lower() and _said in _s56.lower())
    check('Ⓓ② and the repair itself is UNCHANGED and immune to both causes: the marker is read off '
          'the commit by id, which git resolves from any prefix, and the abbreviated map is not '
          'consulted for it',
          'def session_of' in _s39 and '_SESSION.get' not in _s39)
    print(f'      and the same two facts off the tree rather than the text: `session_of` defined '
          f'{"session_of" in {n.name for n in ast.parse(_s39).body if isinstance(n, ast.FunctionDef)}}')

    # ── Ⓔ the class, as a pairing ─────────────────────────────────────────────────────────────────
    head('Ⓔ  the class: one map keyed by an abbreviation, one caller, and no dependence')
    R = C.measure()
    print(f'      gate-layer maps: {R["gates"]}')
    print(f'      the gate\'s readers of it: {R["readers"]}')
    print(f'      callers reaching them with a pinned abbreviation: {sorted(R["callers"])}')
    check(f'Ⓔ① the class is CLOSED at one map and one caller: {len(R["gates"])} gate keys a map by an '
          f'abbreviation and {len(R["callers"])} file reaches it carrying a pinned one',
          len(R['gates']) == 1 and len(R['callers']) == 1
          and any('S39_' in os.path.basename(k) for k in R['callers']))
    #: ⛭⛭ *The first form of this clause read the shape off the SOURCE TEXT with
    #: `re.search(r'if\\s+G\\._same_line\\(...\\)\\s*!=')`, and that is a pin on another receipt's
    #: FORMATTING: a line break between the call and the operator, or an intermediate variable, breaks
    #: it while the claim stays true.  ⇒ Read off the SYNTAX TREE instead -- a comparison whose
    #: operator is `!=` and one of whose sides calls `_same_line` on the instrument -- which is this
    #: revision's own lesson spent on its own gate, and the third time in two receipts.*
    _t39 = ast.parse(_s39)
    _defs = {n.name for n in _t39.body if isinstance(n, ast.FunctionDef)}

    def _checked_against(attr):
        for node in ast.walk(_t39):
            if not (isinstance(node, ast.Compare) and any(isinstance(o, ast.NotEq) for o in node.ops)):
                continue
            for side in [node.left, *node.comparators]:
                for sub in ast.walk(side):
                    if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) \
                            and sub.func.attr == attr:
                        return True
        return False

    print(f'      S39 module-level defs: {sorted(_defs)[:12]}')
    print(f'      the instrument`s verdict is compared against the local one: {_checked_against(ATTR)}')
    check(f'Ⓔ② and the caller no longer DEPENDS on it -- it defines the fact itself and calls the '
          f'instrument only to CHECK its own verdict, so a map emptied by any cause changes no claim '
          f'here.  Read off S39`s SYNTAX TREE and not its formatting: defs carry `{LOCAL}` '
          f'{LOCAL in _defs}, and a `!=` comparison calls `{ATTR}` {_checked_against(ATTR)}',
          LOCAL in _defs and _checked_against(ATTR))

    # ── Ⓕ the arm that could not be measured, with both forms reproducible ────────────────────────
    head('Ⓕ  the arm as registered, and why neither form of it is the measurement')
    print(f'      window form {len(R["window"])} site(s), of which {len(R["refhits"])} on '
          f'`--abbrev-ref`; structural form {len(R["consuming"])}')
    check(f'Ⓕ① both detector forms are REPRODUCIBLE from the committed module and they disagree, '
          f'which is what makes the tightening checkable rather than narrated: window '
          f'{len(R["window"])} against structural {len(R["consuming"])}',
          len(R['window']) > len(R['consuming']) and len(R['window']) >= 10)
    check(f'Ⓕ② and the over-count is DEMONSTRATED rather than asserted: the window form takes at '
          f'least one site on `--abbrev-ref`, which abbreviates a REF to a branch name and has no '
          f'length the environment picks: {len(R["refhits"])}',
          len(R['refhits']) >= 1)

    # ── Ⓖ the pin-length asymmetry ────────────────────────────────────────────────────────────────
    head('Ⓖ  the pins, and whose agree with this environment')
    _hist = {}
    for _r, _n, v in R['consts']:
        _hist[len(v)] = _hist.get(len(v), 0) + 1
    print(f'      {len(R["consts"])} pinned abbreviations in all; length histogram '
          f'{dict(sorted(_hist.items()))}')
    print(f'      {len(R["mine"])} are this seat\'s, of which {len(R["not8"])} are not 8 characters')
    check(f'Ⓖ① as a PROPERTY over all {len(R["mine"])} of this seat\'s pins: not one is at a length '
          f'other than this clone\'s own, so every pin this seat has written agrees with this '
          f'environment and with no other',
          R['not8'] == [] and len(R['mine']) >= 40)
    check(f'Ⓖ② and the corpus does NOT agree with it -- asserted in DIRECTION only, because the '
          f'population is other seats\' and may move: at least one pinned abbreviation in the tree '
          f'is at a different length ({sum(n for k, n in _hist.items() if k != 8)} of '
          f'{len(R["consts"])}), so the agreement in Ⓖ① is this seat\'s habit and not the corpus\'s',
          sum(n for k, n in _hist.items() if k != 8) >= 1)

    # ── Ⓗ the detector is consumed, not restated ──────────────────────────────────────────────────
    head('Ⓗ  every figure read from the computation')
    _toks = [t for t in tokenize.generate_tokens(io.StringIO(_src).readline)
             if t.type in (tokenize.NAME, tokenize.OP)]
    _names = sorted(n for n, v in vars(C).items()
                    if n.isupper() and isinstance(v, str) and re.fullmatch(r'[0-9a-f]{7,12}', v))

    def _via(i):
        return i >= 2 and _toks[i - 1].string == '.' and _toks[i - 2].string == 'C'

    _hits = [(i, t.string) for i, t in enumerate(_toks) if t.string in _names]
    _bare = sorted({n for i, n in _hits if not _via(i)})
    print(f'      pinned constants the computation defines: {_names}')
    print(f'      named bare here: {_bare}')
    check(f'Ⓗ① every pinned sha is read from the computation and none is bound here -- a PROPERTY over '
          f'this file\'s TOKEN STREAM, whose names come from the module by the shape of their values, '
          f'so it cannot match its own prose (S57\'s lesson): {len(_bare)} bare of {len(_names)}',
          _bare == [] and len(_names) >= 3 and 'C.measure(' in _src)
    check(f'Ⓗ② and this receipt is REGISTERED in the index so the suite runs it',
          os.path.basename(__file__) in open(INDEX, encoding='utf-8').read())

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ THE REPAIR WAS RIGHT AND THE REASON WRITTEN BESIDE IT WAS FALSE.  A pin keyed by an')
    print('    abbreviation is keyed by a length the environment picks -- and the container could')
    print('    decide it, because what the code DEPENDS ON is always readable where the code is.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
