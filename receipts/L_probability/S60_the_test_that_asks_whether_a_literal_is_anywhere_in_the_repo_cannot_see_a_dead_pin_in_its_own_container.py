#!/usr/bin/env python3
"""S60 -- A TEST THAT ASKS WHETHER A LITERAL IS ANYWHERE IN THE REPO CANNOT SEE A DEAD PIN IN ITS OWN
CONTAINER -- AND IT ALSO MANUFACTURES ABSENCES.  ⛭⛭⛭ *** `r7399` ① PUT THE DEAD ARM FIRST FOR THE FIFTH
REVISION.  THE ARM WAS DELETED AT `r7372`; WHAT GATES THE OTHER SEAT IS WHAT THE DELETION REMOVED -- THE
CONTAINER FROM THE KEY'S OWN TRACE -- AND THIS SUPPLIES IT FOR THE WHOLE `SOURCE` HALF. ***

** Ⓐ THE QUESTION, IN THE OTHER SEAT'S OWN WORDS. **  *`_present_at`'s `SOURCE` branch tests "anywhere
in the repo but this receipt", so "how many more dead pins would the mint find" needs the container from
the key's own trace.*  Its census scored that half **INVALID, not merely expensive**: the `PAPER` half
ran `1493` rows in `157.3` s and found `123` absent, while the `SOURCE` half projected `≈71` min **for a
test that asks the wrong question**.
  ⇒ *** THE ANSWER IS `94`. ***  *Of `112` keys absent from every container their own trace names, `94`
      are reported PRESENT by the repo-wide branch -- dead pins the instrument that exists cannot see.*

** Ⓑ THE TRACE SHAPE THAT YIELDS A CONTAINER, NAMED. **  `S17` reached its container as
`COMP = tsv('COMPARISON.tsv')`, with `tsv(name)` = `open(os.path.join(DIR, name))` and `DIR` a module
constant -- ** a basename literal in the trace joined to a directory bound in the same receipt **.  The
container is `computations/beyond_the_wall/r7254_60_mirror_cross_read/COMPARISON.tsv`, and `S17`'s own
module tree folds `DIR` to exactly that directory with nothing executed.
  ⛔ *** AND THE PREDICTION'S OWN PREMISE ABOUT IT IS REFUTED. ***  *It said that basename `is not a
      unique basename in this corpus`, so the archetype would need the directory constant.  It IS
      unique -- one path of `4,632` -- so the archetype resolves by basename alone and the phrase "from
      the key's own trace" buys nothing ON THE ARCHETYPE.*  ⇒ ** The class is real anyway, and the arm
      registered to find it is what shows that: `139` keys have NO repo-wide route to a container and
      resolve only through a directory their own receipt binds, because `PREDICTION.md` (`230` paths),
      `RESULT.md` (`88`) and `cost.py` (`14`) repeat once per computation directory. **

** Ⓒ RESOLVABILITY. **  `839` of `1198`.  A key the instrument files `SOURCE` names a file KIND by
construction -- that is how `R*` files it -- but ** naming a kind is not naming a container **:
`endswith('.tsv')` and a `*.py` glob name a kind and no file.  `234` name a file that resolves to
nothing; `125` name no file at all, and those are the keys the instrument could only file by hand.

** Ⓓ THE CENSUS FIGURE, and the registered REASON is refuted while the band holds. **  `112` of `839` =
`13.3` %, ABOVE the `PAPER` half's `8.2` % -- and the prediction said in as many words that it expected
LOWER, *because a `SOURCE` container is usually code or data in this programme's own tree, where a paper
sentence is owned by another seat and gets reworded.*  ⇒ ** The band is HIT and the reason under it is
WRONG, which by `r7372`'s rule is the half that matters: the next reader inherits the reason. **
  ⌗ *What the containers actually say, offered as a reading and not as a second prediction: the heaviest
    are this programme's own MOVING bookkeeping -- `THE_LIVE_ARC.md`, `kills/PO-7.md`, `PROTECTED_OPEN.md`,
    `THE_REGISTER.md` -- `57` of the container slots being root-level maps and ledgers against `19` in
    `corpus/`.  A paper is reworded by a seat; a ledger is rewritten every revision.*
  ⌗ *And `MEANING-HELD` is not `0` here, where the `PAPER` half measured `0` of `505`.*

** ⛔⛔ Ⓔ AND THE SOUNDNESS ARM IS REFUTED -- NOT IN THIS RESOLVER, IN THE INSTRUMENT IT WAS DERIVED
AGAINST. **  The relation registered was: a literal absent from the whole repo but its receipt is absent
from any container that is not its receipt, so repo-wide-absent must be a SUBSET of container-absent.
`1` of `50` sampled keys violates it -- present in its own container, reported ABSENT repo-wide.
  ⇒ *** THE CAUSE IS THAT THE REPO-WIDE BRANCH BUILDS ITS FILE LIST FROM THE LITERAL WITH THE
      BACKSLASHES DELETED. ***  `words = ' '.join(lit.split()[:3]).replace('\\\\', '')`, then
      `git grep -F` on the first word.  For `D1`'s `1+\\lambda\\phi` the needle becomes `1+lambdaphi`,
      which matches `0` files, while the literal itself matches `9`.  ⇒ ** So the branch is wrong in
      BOTH directions: it misses `94` dead pins, and it manufactures absences for the `51` of `1198`
      `SOURCE` keys whose first three words carry a backslash -- `4` of the `18` candidates it agreed
      with are in that class. **  *The one-line correction is ROUTED with its measurement, not applied:
      the gate is another seat's.*

** Ⓕ THE PRICE, machine named per `70`'s `r7371` rule. **  The census itself costs `14.0` s on this
container -- the mint `10.6`, resolution `0.6`, `H3` against the containers `2.8` -- against the
`157.3` s the `PAPER` half cost here and the `≈4,236` s the invalid test projected.  ⇒ ** The valid
instrument is an order of magnitude CHEAPER than the one it replaces, which is not the trade-off anyone
expected. **  *The repo-wide comparison is `168.3` s over `112` candidates and is priced apart, which is
why it is run over the candidates and never over the half.*

** Ⓖ THE SELF-INSTANCE, classified per `r7398`. **  *This receipt's own keys are minted at `HEAD` and
registered by this revision, while `⒞` is measured AT THE FRAME where this file does not exist -- so the
self-instance is unavoidable, is classified, and cannot change a verdict.*

    python3 receipts/L_probability/S60_the_test_that_asks_whether_a_literal_is_anywhere_in_the_repo_cannot_see_a_dead_pin_in_its_own_container.py
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BAR = '=' * 100

DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7400_60_the_container_from_the_keys_own_trace')
COST = os.path.join(DIR, 'cost.py')
RUN = os.path.join(DIR, 'container.txt')
PRED = 'computations/beyond_the_wall/r7400_60_the_container_from_the_keys_own_trace/PREDICTION.md'
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')
ANN = os.path.join(ROOT, 'corpus', 'target_annotations.tsv')

# the bands, as `PREDICTION.md` carries them at FRAME: (lo, hi, central)
BANDS = dict(a=(300, 1100, 870), b=(5, 300, 40), c=(10, 300, 60), d=(40, 100, 75))
PAPER_RATE = 8.2        # the other seat's measured PAPER-half rate, for the comparison Ⓒ② makes
PAPER_PRICE = 157.3     # and its price on this same container
# ⒟ is the expensive arm -- `_present_at` repo-wide at seconds a row -- so its figure is PINNED from the
#   recorded run and a SAMPLE of it is re-verified live here.  A re-run that moves the figure reds Ⓓ①.
GAP_PINNED = 94
SAMPLE = 6
# the key the soundness arm's refutation is located on, and the needle the branch actually searches for
VIOLATOR = 'receipts/L165_interacting_tower/D1_the_boundary_is_per_fibre_and_the_UV_is_over_fibres.py'
VIOL_LIT = '1+\\lambda\\phi'


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def head(t):
    print(f'\n  {"-" * 96}\n  {t}\n  {"-" * 96}')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace')


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def inband(x, k):
    lo, hi, _ = BANDS[k]
    return lo <= x <= hi


def klass(p):
    if p.startswith('receipts/'):
        return 'receipt source'
    if p.startswith('corpus/'):
        return 'corpus'
    if p.startswith('computations/'):
        return 'computation output'
    if p.startswith('scripts/'):
        return 'scripts'
    if re.match(r'FOR_[A-Za-z0-9_]+\.md$', p):
        return 'routing file'
    return 'root-level map or ledger'


def main():
    print(__doc__)
    C = load(COST, 'r7400_cost')
    run = open(RUN, encoding='utf-8').read()

    # ── Ⓐ the frame, and that the bands were registered BEFORE the scan ───────────────────────────
    head('Ⓐ  the frame resolves, it is an ancestor of HEAD, and it is the commit that ADDED the bands')
    _full = git('rev-parse', '--verify', '--quiet', f'{C.FRAME}^{{commit}}').stdout.strip()
    _anc = git('merge-base', '--is-ancestor', _full or 'HEAD', 'HEAD').returncode == 0 if _full else False
    _added = [ln for ln in git('show', '--name-status', '--format=', _full).stdout.split('\n')
              if ln.startswith('A\t') and ln.endswith(os.path.basename(PRED))]
    _at_frame = git('show', f'{_full}:{PRED}').stdout
    print(f'      FRAME {C.FRAME} -> {_full[:12]}, ancestor of HEAD: {_anc}, added the prediction: '
          f'{bool(_added)}, {len(_at_frame)} char(s) at the frame')
    check(f'Ⓐ① the frame resolves to a commit, is an ancestor of HEAD, and that commit ADDED the '
          f'prediction -- so the bands are registered before the scan and not beside it',
          bool(_full) and _anc and bool(_added) and len(_at_frame) > 2000)
    _arms = [m for m in ('⒜', '⒝', '⒞', '⒟', '⒠', '⒡') if m in _at_frame]
    _bands_there = all(str(lo) in _at_frame and str(hi) in _at_frame for lo, hi, _ in BANDS.values())
    check(f'Ⓐ② and all six arms are named at the frame with their bands -- {len(_arms)} of 6 markers '
          f'present and every band endpoint in the text: {_bands_there}',
          len(_arms) == 6 and _bands_there)

    # ── Ⓑ the archetype, from the receipt's own syntax tree ───────────────────────────────────────
    head('Ⓑ  the trace shape that yields a container -- and the premise about it that is refuted')
    _s17 = open(os.path.join(ROOT, C.ARCHETYPE_RECEIPT), encoding='utf-8').read()
    _dir = C.fold(_s17).get('DIR')
    _paths, _how = C.resolve(C.ARCHETYPE_RECEIPT, 'COMPARISON.tsv')
    _wide = C.BYBASE.get('COMPARISON.tsv', [])
    print(f'      S17 folds DIR -> {_dir}')
    print(f'      the basename resolves to {_paths} by {_how!r}; {len(_wide)} path(s) in the tree carry it')
    check(f'Ⓑ① the archetype\'s container comes out of the receipt\'s OWN module tree with nothing '
          f'executed: `DIR` folds to {_dir!r} and the container exists at the frame',
          _dir == C.ARCHETYPE_DIR and C.ARCHETYPE in C.TREESET and _paths == [C.ARCHETYPE])
    check(f'Ⓑ② ⛔ and the prediction\'s premise is REFUTED: that basename is UNIQUE among the '
          f'{len(C.TREE)} paths at the frame, so the archetype resolves by basename alone ({_how}) and '
          f'needs no directory constant -- the arm registered to find the class is what shows it',
          len(_wide) == 1 and _how == 'BASE')
    _rep = {b: len(C.BYBASE[b]) for b in ('PREDICTION.md', 'RESULT.md', 'cost.py')}
    check(f'Ⓑ③ while the basenames that DO force the receipt\'s own directory repeat once per '
          f'computation directory -- {_rep} -- so a repo-wide basename lookup decides nothing for them',
          all(v > 10 for v in _rep.values()) and _rep['PREDICTION.md'] > 100)

    # ── Ⓒ resolvability and the census, recomputed live at the frame ───────────────────────────────
    head('Ⓒ  how often a SOURCE key\'s own trace yields a container, and what is absent from it')
    _named, _sites = C.trace_names()
    _src = [r for r in C.ledger() if r[2] == 'SOURCE']
    _cof, _hof, _cls = {}, {}, Counter()
    for _r in _src:
        _toks = _named.get((_r[0], _r[1]), set())
        _g, _h = C.containers(_r[0], _toks)
        _cof[(_r[0], _r[1])], _hof[(_r[0], _r[1])] = _g, _h
        _cls['NO-NAME' if not _toks else ('RESOLVED' if _g else 'NAMED-UNRESOLVED')] += 1
    _resolved = [r for r in _src if _cof[(r[0], r[1])]]
    _dironly = [r for r in _resolved if _hof[(r[0], r[1])] == ['DIR']]
    print(f'      {_sites} site(s) minted; SOURCE half {len(_src)}; resolved {_cls["RESOLVED"]}, '
          f'named-unresolved {_cls["NAMED-UNRESOLVED"]}, named-nothing {_cls["NO-NAME"]}')
    check(f'Ⓒ① ⒜ {_cls["RESOLVED"]} of {len(_src)} SOURCE keys resolve to at least one container from '
          f'their own trace -- band {BANDS["a"][0]}-{BANDS["a"][1]}, central {BANDS["a"][2]}',
          inband(_cls['RESOLVED'], 'a'))
    check(f'Ⓒ② ⒝ {len(_dironly)} of them resolve ONLY through a directory the receipt itself binds, '
          f'with no repo-wide route at all -- band {BANDS["b"][0]}-{BANDS["b"][1]}, central '
          f'{BANDS["b"][2]}: the arm that says the key\'s own trace is NEEDED and not merely sufficient',
          inband(len(_dironly), 'b'))
    check(f'Ⓒ③ and the three classes PARTITION the half -- '
          f'{_cls["RESOLVED"]}+{_cls["NAMED-UNRESOLVED"]}+{_cls["NO-NAME"]} = {len(_src)} -- so no key '
          f'is counted twice and none is dropped',
          sum(_cls.values()) == len(_src) and _cls['NAMED-UNRESOLVED'] > 0)
    _annrows = {q[0] for q in (ln.split('\t') for ln in open(ANN, encoding='utf-8').read().split('\n'))
                if len(q) >= 3 and q[0] and not q[0].startswith('#')}
    _noname = [r for r in _src if not _named.get((r[0], r[1]), set())]
    _unann = [r for r in _noname if r[0] not in _annrows]
    check(f'Ⓒ④ and the {len(_noname)} keys whose trace names NO file are the keys the instrument could '
          f'only file by hand: {len(_noname) - len(_unann)} of {len(_noname)} sit in receipts the '
          f'annotation file names -- a cross-check on this harness, not a finding about the corpus',
          len(_noname) > 0 and len(_unann) * 4 <= len(_noname))

    _absent = [(r[0], r[1], r[3], r[4]) for r in _resolved
               if not C.present_in(r[1], r[0], _cof[(r[0], r[1])])]
    _rate = 100 * len(_absent) / max(1, len(_resolved))
    _byv = dict(Counter(x[3] for x in _absent))
    print(f'      absent from every resolved container: {len(_absent)} of {len(_resolved)} '
          f'= {_rate:.1f} %   by verdict {_byv}')
    check(f'Ⓒ⑤ ⒞ {len(_absent)} of {len(_resolved)} resolved keys are absent from every container their '
          f'trace names -- band {BANDS["c"][0]}-{BANDS["c"][1]}, central {BANDS["c"][2]}; CANDIDATES '
          f'and an UPPER BOUND, because the green-receipt filter is the other half of that order',
          inband(len(_absent), 'c'))
    check(f'Ⓒ⑥ ⛔ and the registered REASON is refuted while the band holds: {_rate:.1f} % is ABOVE the '
          f'PAPER half\'s {PAPER_RATE} %, and the prediction said it expected LOWER -- by r7372\'s rule '
          f'the reason is the half that matters, so it is corrected here and not quietly dropped',
          _rate > PAPER_RATE)
    _kc = Counter(klass(p) for x in _absent for p in _cof[(x[0], x[1])])
    print(f'      the containers, by class: {dict(_kc)}')
    check(f'Ⓒ⑦ and the reading under that: the heaviest containers are this programme\'s own MOVING '
          f'bookkeeping, {_kc["root-level map or ledger"]} root-level map-or-ledger slots against '
          f'{_kc["corpus"]} in `corpus/` -- a paper is reworded by a seat, a ledger every revision',
          _kc['root-level map or ledger'] > _kc['corpus'] and _byv.get('MEANING-HELD', 0) >= 1)

    # ── Ⓓ the figure the order asks for ───────────────────────────────────────────────────────────
    head('Ⓓ  of those, the ones the repo-wide branch calls PRESENT -- the dead pins it cannot see')
    _m = re.search(r'REPORTED PRESENT REPO-WIDE\s+(\d+) of (\d+)', run)
    _gap, _of = (int(_m.group(1)), int(_m.group(2))) if _m else (-1, -1)
    _frac = 100 * _gap / max(1, _of)
    print(f'      the recorded run reports {_gap} of {_of} = {_frac:.1f} %')
    check(f'Ⓓ① ⒟ {_gap} of {_of} candidates are reported PRESENT repo-wide -- {_frac:.1f} %, band '
          f'{BANDS["d"][0]}-{BANDS["d"][1]} %, central {BANDS["d"][2]} % -- and the pinned figure '
          f'{GAP_PINNED} matches a recorded run over the {len(_absent)} live candidates',
          _gap == GAP_PINNED and _of == len(_absent) and inband(_frac, 'd'))
    _rows = [ln.split('\t') for ln in run.split('\n') if ln.count('\t') >= 6]
    _gaprows = [r for r in _rows if r[6] == 'PRESENT-REPO-WIDE'][:SAMPLE]
    _again = [(r[0], C.present_repo_wide(json.loads(r[1]), r[0])) for r in _gaprows]
    check(f'Ⓓ② and a live sample of {len(_again)} of them is re-verified in THIS run rather than taken '
          f'from the record: {sum(1 for _, p in _again if p)} of {len(_again)} still reported present '
          f'repo-wide while absent from their own container',
          len(_again) == SAMPLE and all(p for _, p in _again))

    # ── Ⓔ the soundness arm, refuted, and the cause located ───────────────────────────────────────
    head('Ⓔ  the subset relation -- refuted, and NOT in this resolver')
    _selfcont = [(r[0], c) for r in _resolved for c in _cof[(r[0], r[1])] if c == r[0]]
    check(f'Ⓔ① ⒠i no resolved container is its own receipt, over all {len(_resolved)} resolved keys -- '
          f'which is `_present_at`\'s own rule, text from a file the receipt does not own',
          not _selfcont)
    _needle = ' '.join(VIOL_LIT.split()[:3]).replace('\\', '').split()[0]
    _mangled = [x for x in C.Q._git('grep', '-l', '-F', '-e', _needle, C.FULL, '--').stdout.split('\n')
                if ':' in x]
    _literal = [x for x in C.Q._git('grep', '-l', '-F', '-e', VIOL_LIT.split()[0], C.FULL,
                                    '--').stdout.split('\n') if ':' in x]
    _rw = C.present_repo_wide(VIOL_LIT, VIOLATOR)
    print(f'      needle {_needle!r} matches {len(_mangled)} file(s); the literal itself '
          f'{len(_literal)}; repo-wide verdict {_rw}')
    check(f'Ⓔ② ⛔ ⒠ii the point prediction of 0 violations is REFUTED at 1 of 50, and the cause is in '
          f'the instrument the relation was derived against: the repo-wide branch builds its file list '
          f'from the literal with the BACKSLASHES DELETED, so {_needle!r} matches {len(_mangled)} '
          f'file(s) where the literal matches {len(_literal)}, and the key is called absent',
          not _mangled and len(_literal) >= 1 and _rw is False)
    _exposed = [r for r in _src if '\\' in ' '.join(r[1].split()[:3])]
    _agreed = [r for r in _rows if r[6] == 'ABSENT-REPO-WIDE']
    _agreed_exposed = [r for r in _agreed if '\\' in ' '.join(json.loads(r[1]).split()[:3])]
    check(f'Ⓔ③ ⇒ so the branch is wrong in BOTH directions: it misses {GAP_PINNED} dead pins, and it '
          f'MANUFACTURES absences for the {len(_exposed)} of {len(_src)} SOURCE keys whose first three '
          f'words carry a backslash -- {len(_agreed_exposed)} of the {len(_agreed)} candidates it '
          f'agreed with are in that class.  The one-line correction is ROUTED, not applied',
          len(_exposed) >= 1 and len(_agreed_exposed) >= 1 and len(_agreed_exposed) < len(_agreed))

    # ── Ⓕ the price, and Ⓖ the self-instance ──────────────────────────────────────────────────────
    head('Ⓕ  the price on this container, and this receipt\'s own place in the population it measures')
    _census = re.search(r'⇒ THE CENSUS ITSELF\s+([\d.]+)s', run)
    _apart = re.search(r'repo-wide, \d+ candidate\(s\)\s+([\d.]+)s', run)
    _cs, _ap = (float(_census.group(1)) if _census else -1.0), (float(_apart.group(1)) if _apart else -1.0)
    print(f'      the census itself {_cs}s; the repo-wide comparison {_ap}s over the candidates only')
    check(f'Ⓕ① ⒡ the census itself costs {_cs:.1f}s on this container -- band 10-600 s, central 60 s -- '
          f'against the {PAPER_PRICE}s the PAPER half cost here, so the VALID instrument is cheaper '
          f'than the one it replaces by a factor of {PAPER_PRICE / max(1.0, _cs):.0f}',
          10 <= _cs <= 600 and _cs < PAPER_PRICE)
    check(f'Ⓕ② and the repo-wide comparison is {_ap:.1f}s, {_ap / max(1.0, _cs):.0f} times the census, '
          f'which is why it is run over the {len(_absent)} candidates and never over the half',
          _ap > _cs)
    _me = os.path.relpath(os.path.abspath(__file__), ROOT)
    _inledger = [r for r in _src if r[0] == _me]
    check(f'Ⓖ① the self-instance is CLASSIFIED and cannot change a verdict (r7398\'s rule): this '
          f'receipt mints {len([k for k in _named if k[0] == _me])} key(s) at HEAD and the SOURCE half '
          f'AT THE FRAME carries {len(_inledger)} of them, because the frame predates this file',
          not _inledger)
    check(f'Ⓖ② and this receipt is REGISTERED in the index so the suite runs it',
          os.path.basename(__file__) in open(INDEX, encoding='utf-8').read())

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ A TEST THAT ASKS WHETHER A LITERAL IS ANYWHERE IN THE REPO CANNOT SEE A DEAD PIN IN ITS')
    print(f'    OWN CONTAINER: {GAP_PINNED} of {len(_absent)} are invisible to it.  The container is')
    print('    available from the key\'s own trace for most of the half, a large minority of it only')
    print('    through a directory the receipt itself binds -- and the test it replaces is also wrong')
    print('    in the other direction, calling absent what its own mangled needle cannot find.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
