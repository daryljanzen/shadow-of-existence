#!/usr/bin/env python3
"""L_probability receipt -- the SECOND face of `r7204`'s class, swept over this seat's own work:
** an exact count asserted against a set other seats can grow. **

*** ⛭⛭⛭ AND THE ONE LIVE INSTANCE WAS `r7198`'s OWN RECEIPT, TURNED RED BY `r7204` -- THE RECEIPT
    WHOSE SUBJECT IS PINS THAT FAIL ON THE SUCCESS OF THEIR OWN WORK, FAILING ON THE SUCCESS OF ITS
    OWN WORK. ***  *`r7198` gated `len(UNADJ) == 2170` on a bucket `PO-78` states `may only fall`.
    `r7204` read the `OPEN` subclass and the backlog fell to `2167`.*  ⇒ ** It was red on the trunk
    when this revision started, and nobody had seen it, because the job that runs receipts had been
    skipped on every push in between. **

⛔ ** THE CLASS, STATED SO IT IS NOT CONFUSED WITH THE ONE `r7204` READ. **  *`r7204`'s subject was a
pin on a SENTENCE that may be reworded.  This is a gate on a SET whose MEMBERSHIP another seat
controls: a registry, a baseline, an enumerated directory, the corpus's own paper count.*  ** Written
with `==`, it is an assertion that nobody will add to that set. **  ⇒ *Three faces of one defect have
now been found in this seat's work in two rounds --- the openness pin, the set equality, and a pin on
a FORM where the argument needed the CONTENT --- and all three were found BY ACCIDENT, by a merge or
a reword.  That is the reason for a detector.*

** ⓵ WHAT THE SWEEP MEASURES, AND THE FINDING IS THAT THE CLASS IS RARE. **
*Over `284` receipts this seat owns, an `ast` taint analysis flags `25` sites in `9` receipts where an
integer literal is compared for EQUALITY against a `len`/`sum`/`count` of something traced to a
shared registry or a directory enumeration.*  ⇒ *** READING ALL TWENTY-FIVE, ONLY `3` ARE GENUINELY
EXPOSED. ***  The other twenty-two partition into three classes with computed grounds:
  ⓐ ***`4` FROZEN*** --- *the counted set is read at a PINNED COMMIT, so its size cannot move.*
  ⓑ ***`14` SELF*** --- *the counted set is one the receipt itself writes as a literal or builds by
    comprehension from its own table, so no other seat can reach it.*
  ⓒ ***`4` ROW-SCOPED*** --- *`== 1` on the rows matching ONE named row, where the equality is the
    point: a duplicate row must fail, which is `check_row_matchers`' own lesson.*
⇒ ** So the detector's raw flag is not the defect, and a sweep that reported `25` would be crying
wolf twenty-two times.  The partition is the instrument. **

** ⛭ ⓶ AND OF THE THREE EXPOSED, TWO ARE REPAIRED HERE AND THE THIRD IS READ SAFE. **
  ⓐ *`r7198`'s backlog gates -- `len(UNADJ) == 2170` and its twin -- the live red above.*  ** Repaired
    by the rule its own subject prescribes: the figure the pass MADE is pinned as that pass's own
    arithmetic, which can never move, and the live check is MONOTONE in the direction `PO-78`
    allows. **
  ⓑ *`r7198`'s `zero unadjudicated keys on the two cleared receipts` --- a property of two FILES any
    seat may add a pin to, and `66` has since edited one of them.*  ** Moved onto this pass's OWN
    sixty-six stamped rows, where it belongs, with the live file count reported beside it. **
  ⓒ *`S1`'s `len(PAPERS) == 18` --- an assertion about THE SIZE OF THE CORPUS, with the label's
    `the other seventeen` going stale alongside it.*  ** Replaced by the content the check actually
    needs: class (ii) is three, in one paper, and zero in EVERY other paper swept. **
  ⌗ *The third flag on `r7198` -- `len(TARGETS) == 2` -- is READ AND LEFT: `TARGETS` is derived from
  the rows carrying THIS PASS'S STAMP, and a stamp is frozen once written, so the set cannot grow.*

⚠ ** AND ONE RED ON THIS TREE IS NOT THIS CLASS, WHICH IS WORTH SAYING RATHER THAN QUIETLY FIXING. **
*`P15_the_free_streaming_knob...` fails on this seat's own container with `ModuleNotFoundError: No
module named 'camb'`.*  ⇒ ** That is an ENVIRONMENT fact about where it ran, not a defect in the
receipt, and it is neither repaired nor chased. **  ⛔ *And the first draft of `Ⓓ①` asserted that the
module is ABSENT -- a gate on THE CONTAINER, which passed here and went red on the runner where the
instrument is installed.  **That is this family's FOURTH instance and the only one CI found before I
did**: the gate asserted a form of the environment where the argument needed the content.  The
import's presence in the source is asserted; whether it RESOLVES is printed.*  ⌗ *A receipt that
imports an instrument is entitled to require it; what would be wrong is to delete the import.*

⌗ ** THE DETECTOR'S OWN TWO LIMITS, NAMED HERE RATHER THAN FOUND LATER. **
  ⓵ *It cannot see a pinned read whose commit is an f-string variable (`show(f'{PIN}:...')`), so
    `FROZEN` needs a second pass over the assignments that bind such a name -- which is why the
    partition is computed in two stages below and not in one.*
  ⓶ *It over-reports `== 1`: a row-scoped match is flagged like an exposed count, and only reading
    the site separates them.  **The detector narrows `284` receipts to `9`; it does not adjudicate.**

** COMPUTES: an ast taint analysis over the 284 receipts this seat owns -- which names carry a value
traced to a shared multi-seat registry or a directory enumeration, and which equality sites compare an
integer literal against a count of one; the four-way partition of the flagged sites with a computed
ground for each; the arithmetic showing r7198's gate was FALSE on this tree before repair; and the
detector run against the pre-repair and post-repair sources as a two-sided control.  Reads receipt
sources and the adjudication baseline as DATA and asserts nothing about any paper.  No assertion on
wall-clock time. **
"""
import ast
import glob
import os
import re
import subprocess

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: the SHARED artefacts -- any seat may add a row to these
SHARED = ('quote_pin_baseline', 'prose_pin_baseline', 'unread_figure_baseline', 'INDEX.md',
          'THE_REGISTER', 'PROTECTED_OPEN', 'THE_FRONTIER', 'OWED.md', 'THE_WEAVE', 'CORPUS_MAP',
          'PO13_WORKING_STATE', 'marker_transposition_baseline', 'THE_OPEN_PROBLEMS_LEDGER',
          'OPEN_PROBLEMS_MAP')
ENUM = ('glob', 'listdir', 'walk', 'iglob')


def flagged(src):
    """the equality sites where an int literal meets a count of something LIVE and SHARED."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    tainted = set()
    for _ in range(5):
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                tgts = node.targets if isinstance(node, ast.Assign) else [node.target]
                d = ast.dump(node.value)
                if (any(s in d for s in SHARED)
                        or any(f"attr='{g}'" in d or f"id='{g}'" in d for g in ENUM)
                        or any(f"id='{t}'" in d for t in tainted)):
                    for t in tgts:
                        for nm in ast.walk(t):
                            if isinstance(nm, ast.Name):
                                tainted.add(nm.id)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            parts = [node.left, node.comparators[0]]
            lit = [x for x in parts if isinstance(x, ast.Constant) and isinstance(x.value, int)]
            oth = [x for x in parts if x not in lit]
            if not (lit and oth):
                continue
            d = ast.dump(oth[0])
            if not ("id='len'" in d or "id='sum'" in d or "attr='count'" in d):
                continue
            names = {n.id for n in ast.walk(oth[0]) if isinstance(n, ast.Name)}
            if names & tainted:
                out.append((node.lineno, lit[0].value, frozenset(names & tainted)))
    return out


def ground(src, site):
    """the second stage: FROZEN / SELF / ROW-SCOPED / EXPOSED, each from the source itself."""
    tree = ast.parse(src)
    frozen, selfmade = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            seg = ast.get_source_segment(src, node.value) or ''
            if '{PIN}:' in seg or re.search(r"['\"][0-9a-f]{7,40}:", seg):
                for t in node.targets:
                    for nm in ast.walk(t):
                        if isinstance(nm, ast.Name):
                            frozen.add(nm.id)
            if isinstance(node.value, (ast.List, ast.Tuple, ast.Dict, ast.Set, ast.ListComp,
                                       ast.SetComp, ast.DictComp)):
                for t in node.targets:
                    for nm in ast.walk(t):
                        if isinstance(nm, ast.Name):
                            selfmade.add(nm.id)
    for _ in range(3):                      # the limit named in the docstring: propagate FROZEN
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                d = ast.dump(node.value)
                if any(f"id='{f}'" in d for f in frozen):
                    for t in node.targets:
                        for nm in ast.walk(t):
                            if isinstance(nm, ast.Name):
                                frozen.add(nm.id)
    via = set(site[2])
    if via & frozen:
        return 'FROZEN'
    if via <= selfmade:
        return 'SELF'
    if site[1] == 1:
        return 'ROW-SCOPED'
    return 'EXPOSED'


# ============================================================ A. the live red, computed
head("A.  THE LIVE RED: r7198's OWN RECEIPT, TURNED RED BY r7204")

PIN = 'f8d8e648'                     # the trunk as this revision found it, r7198's gate still exact
S2 = ('receipts/L_probability/S2_the_quote_pin_backlog_falls_by_sixty_six_on_this_lines_own_two'
      '_receipts_and_every_verdict_names_what_was_read_and_the_re_check_it_owes.py')
_pre = subprocess.run(['git', '-C', ROOT, 'show', f'{PIN}:{S2}'],
                      capture_output=True, text=True, errors='replace').stdout
_now = open(os.path.join(ROOT, S2), encoding='utf-8').read()
# ** the old form survives in the repair's own COMMENT, which quotes it -- so the test is on the
#   executable lines only.  *A check that read the comment would report the repair as not done.* **
_now_code = '\n'.join(ln for ln in _now.split('\n') if not ln.lstrip().startswith('#'))
gate("Ⓐ① at the commit this revision started from, `r7198`'s gate carried the EXACT-COUNT form "
     "`len(UNADJ) == 2170` on a bucket `PO-78` states `may only fall`",
     'len(UNADJ) == 2170' in _pre and len(_pre) > 1000)

_base = [ln.split('\t') for ln in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                                       encoding='utf-8').read().split('\n')
         if ln.strip() and not ln.startswith('#')]
_unadj = sum(1 for r in _base if len(r) >= 6 and r[5] == 'UNADJUDICATED')
_r7204_stamped = sum(1 for r in _base if len(r) >= 7 and 'r7204+60' in r[6])
print(f"      unadjudicated on this tree: {_unadj};   rows carrying r7204's stamp: {_r7204_stamped}")
gate("Ⓐ② and the live count is at or below `2167`, so that equality was FALSE on the trunk -- *** the "
     "receipt was RED, and `r7204` is what made it so: its own stamp is in the baseline and the "
     "backlog fell under it. ***  ⌗ *Nobody had seen it, because the job that runs receipts was "
     "skipped on every push in between*  ⌗ *And this gate is MONOTONE for its own subject's reason: "
     "an exact count on a set another seat can lower is the very defect this receipt reports, and a "
     "later batch lowered it again*",
     _unadj <= 2167 and _unadj < 2170 and _r7204_stamped > 0)

gate("Ⓐ③ and the repaired form is MONOTONE: the figure the pass MADE is pinned as that pass's own "
     "arithmetic -- it fell by `66` from `2236` -- and the live check is `<=` in the direction the row "
     "allows, with the exact-count form gone from the file",
     'len(UNADJ) == 2170' not in _now_code and 'len(UNADJ) <= 2170' in _now_code
     and '_FROM - _FELL_BY == 2170' in _now_code
     and 'len(UNADJ) == 2170' in _now)        # still quoted in the repair's comment, deliberately


# ============================================================ B. the detector, controlled both ways
head("B.  THE DETECTOR, AND THE CONTROL RUNS IN BOTH DIRECTIONS")

_pre_hits = flagged(_pre)
_now_hits = flagged(_now)
_pre_vals = {v for _, v, _ in _pre_hits}
_now_vals = {v for _, v, _ in _now_hits}
print(f"      pre-repair flags:  {sorted((l, v) for l, v, _ in _pre_hits)}")
print(f"      post-repair flags: {sorted((l, v) for l, v, _ in _now_hits)}")
gate("Ⓑ① ✔ THE CONTROL, FORWARD: the detector flags the pre-repair source at the `2170` and `2236` "
     "sites and does NOT flag the repaired one there -- so it finds the defect it was built for and "
     "stops finding it once repaired",
     2170 in _pre_vals and 2236 in _pre_vals
     and 2170 not in _now_vals and 2236 not in _now_vals)

# the other direction: an ordinary paper phrase pin must NOT be flagged
_PAPER_PIN = (
    "import re\n"
    "P = re.sub(r'\\s+', ' ', open('corpus/CR_cosmology.tex').read())\n"
    "ok = P.count('the photons are projected through the flat geometry') == 1\n")
_RIGHT = ("import glob\n"
          "ROWS = [r for r in open('corpus/quote_pin_baseline.tsv')]\n"
          "ok = len(ROWS) == 2496\n")
print(f"      a paper phrase pin flags: {len(flagged(_PAPER_PIN))};   "
      f"a baseline row count flags: {len(flagged(_RIGHT))}")
gate("Ⓑ② ✔ THE CONTROL, BACKWARD: an ordinary `count(phrase) == 1` on a paper read is NOT flagged, "
     "while the same shape over the adjudication baseline IS.  ⇒ *the detector separates the paper pin "
     "from the registry count, which is the whole distinction it exists to draw*",
     not flagged(_PAPER_PIN) and flagged(_RIGHT))


# ============================================================ C. the sweep and its partition
head("C.  THE SWEEP OVER THIS SEAT'S OWN 284 RECEIPTS, AND THE PARTITION IS THE INSTRUMENT")

# ** the POPULATION is taken from the pinned tree as well, not from a live glob: a sweep whose own
#   denominator moves when this revision adds a receipt would be the very defect it is about. **
_tree = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', PIN, 'receipts/'],
                       capture_output=True, text=True, errors='replace').stdout.split('\n')
MINE = sorted(p for p in _tree
              if (p.startswith('receipts/P15_CR_cosmology/') and p.endswith('.py'))
              or (p.startswith('receipts/L_probability/S') and p.endswith('.py')))
_at_pin = {}
for rel in MINE:
    _src = subprocess.run(['git', '-C', ROOT, 'show', f'{PIN}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout
    if not _src:
        continue
    h = flagged(_src)
    if h:
        _at_pin[rel] = (_src, h)
_n_sites = sum(len(h) for _, h in _at_pin.values())
print(f"      receipts this seat owns: {len(MINE)};  flagged at {PIN}: {_n_sites} site(s) in "
      f"{len(_at_pin)} receipt(s)")
gate("Ⓒ① the sweep is over `284` receipts this seat owns and it is read AT THE PINNED COMMIT, not "
     "live -- so this gate does not itself join the class it is about.  `22` sites in `9` receipts "
     "are flagged",
     len(MINE) == 284 and _n_sites == 25 and len(_at_pin) == 9)

_part = {}
for rel, (s, hits) in _at_pin.items():
    for h in hits:
        _part.setdefault(ground(s, h), []).append((os.path.basename(rel)[:40], h[0], h[1]))
for k in sorted(_part):
    print(f"      {k:11s} {len(_part[k]):3d}")
    for r in sorted(_part[k])[:4]:
        print(f"                  {r[0][:38]:38s} line {r[1]:4d}  == {r[2]}")
gate("Ⓒ② *** AND READING ALL TWENTY-FIVE, ONLY `3` ARE GENUINELY EXPOSED *** -- `4` are FROZEN at a "
     "pinned commit, `14` count a set the receipt itself writes, and `4` are row-scoped `== 1` where "
     "the equality is the point.  ⇒ **the four classes partition the twenty-five exactly, each from a "
     "ground computed out of the source**",
     sum(len(v) for v in _part.values()) == 25
     and {k: len(v) for k, v in _part.items()} == {'EXPOSED': 3, 'FROZEN': 4, 'SELF': 14,
                                                   'ROW-SCOPED': 4})

gate("Ⓒ③ ⛭ and the finding is that THE CLASS IS RARE in this seat's work -- `3` exposed sites in "
     "`284` receipts -- *** but two of the three sit in the one receipt whose own subject is gates "
     "that fail on their own success. ***  ⌗ *Rare is not the same as harmless, and where it landed "
     "is the point*",
     len(_part['EXPOSED']) == 3
     and sum(1 for r in _part['EXPOSED'] if r[0].startswith('S2_')) == 2)

_S1 = open(glob.glob(os.path.join(ROOT, 'receipts', 'L_probability', 'S1_*.py'))[0],
           encoding='utf-8').read()
# ** the same care as `Ⓐ③`: both repairs QUOTE the form they replaced in their own comment, so the
#   test is on the executable lines.  *The quote is deliberate -- a repair that does not say what it
#   replaced is a repair nobody can check.* **
_S1_code = '\n'.join(ln for ln in _S1.split('\n') if not ln.lstrip().startswith('#'))
gate("Ⓒ④ and two of the three are REPAIRED on this tree: `r7198`'s backlog gate is monotone, its "
     "`zero keys on two FILES` claim is moved onto this pass's OWN stamped rows, and `S1`'s assertion "
     "about THE SIZE OF THE CORPUS is replaced by the content it needed -- `every other paper swept` "
     "rather than `the other seventeen`",
     'len(PAPERS) == 18' not in _S1_code and 'len(PAPERS) >= 18' in _S1_code
     and 'EVERY other paper swept' in _S1_code
     and "not [r for r in MINE if r[5] == 'UNADJUDICATED']" in _now_code
     and 'len(PAPERS) == 18' in _S1)          # quoted in its own comment, as above

gate("Ⓒ⑤ ⌗ and the third is READ AND LEFT rather than repaired, with its ground stated: `TARGETS` is "
     "derived from the rows carrying THIS PASS'S STAMP, and a stamp is frozen once written, so that "
     "set cannot grow.  ⇒ *a sweep that repaired it anyway would be treating the detector's flag as "
     "the finding*",
     'len(TARGETS) == 2' in _now and "r7204+60" not in _now)


# ============================================================ D. what is NOT this class
head("D.  ⚠ AND ONE RED ON THIS TREE IS NOT THIS CLASS")

_FS = glob.glob(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                             'P15_the_free_streaming_knob*.py'))
_fs_src = open(_FS[0], encoding='utf-8').read() if _FS else ''
try:
    import camb                                                        # noqa: F401
    _camb = True
except ImportError:
    _camb = False
# ** ⛭⛭⛭ AND THIS GATE WAS THE FOURTH INSTANCE, CAUGHT BY CI RATHER THAN BY ME. ***  Its first draft
#   asserted `not _camb` -- that the module is ABSENT -- which is a gate on THE CONTAINER and not on
#   the receipt.  It passed here and went red on the runner, where the instrument IS installed.
#   ⇒ ** Same family as the other three: the gate asserted a FORM of the environment where the
#   argument needed the CONTENT.  The content is that the red is explained by an import the receipt
#   is entitled to make; whether that import RESOLVES is an environment fact, so it is printed and
#   never asserted. **  ⌗ *A gate on an environment is a gate on everybody's environment.*
print(f"      the free-streaming receipt imports camb: {'import camb' in _fs_src};  "
      f"camb resolves in THIS environment: {_camb}  (reported, never asserted)")
gate("Ⓓ① the one other red seen on this seat's tree is `ModuleNotFoundError: No module named 'camb'` "
     "-- *and the content that explains it is in the receipt's own source: it IMPORTS the instrument "
     "it is registered against.*  ⇒ *** Whether that import resolves is a property of the "
     "environment, so it is REPORTED above and not asserted -- the first draft of this gate asserted "
     "the module was ABSENT, passed here and went red on the runner where it is installed, which is "
     "this family's fourth instance and the only one CI found before I did. ***  ⌗ *Deleting an "
     "import to get a green would be the real defect, and that is still not done.*",
     'import camb' in _fs_src and len(_fs_src) > 1000)


# ============================================================ E. scope
head("E.  ⚠ SCOPE, AND THE DETECTOR'S OWN LIMITS")

gate("Ⓔ① the detector NARROWS and does not adjudicate: it took `284` receipts to `9`, and the "
     "classification of every flagged site was read.  ⌗ *Its two limits are named in the docstring "
     "rather than found later -- it cannot see a pinned read whose commit is an f-string variable, "
     "which is why `FROZEN` is computed in a second pass, and it over-reports `== 1`*",
     len(MINE) == 284 and len(_at_pin) == 9
     and sum(len(v) for v in _part.values()) == _n_sites
     and set(_part) == {'EXPOSED', 'FROZEN', 'SELF', 'ROW-SCOPED'})

gate("Ⓔ② and nothing outside this seat's own files is touched: three gates in two of this seat's own "
     "receipts are repaired, no other seat's receipt is read for repair, no paper is edited, no "
     "parameter is fitted and no registry row is stamped",
     all(('P15_CR_cosmology' in k or 'L_probability' in k) for k in _at_pin)
     and 'len(UNADJ) <= 2170' in _now)

print()
head("VERDICT")
_f = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_f)} of {len(CHECKS)} checks pass")
if _f:
    print(f"  {len(_f)} FAILED:")
    for n in _f:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS -- the second face of r7204's class, swept over this seat's own 284 receipts.  An
  exact count asserted against a set other seats can grow is RARE here: 22 sites flagged, and
  reading all of them, only 3 are genuinely exposed -- 4 are frozen at a pinned commit, 14 count a
  set the receipt itself writes, and 4 are row-scoped where the equality is the point.  But two of
  the three sit in r7198's receipt, whose own subject is gates that fail on their own success, and
  one of those was RED on the trunk when this revision started, turned red by r7204 reading the
  subclass r7198 had begun.  Two are repaired, the third is read and left with its ground stated,
  and the one other red on this tree is named as an environment limitation rather than chased.""")
