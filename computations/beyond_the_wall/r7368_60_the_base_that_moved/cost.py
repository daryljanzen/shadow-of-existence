#!/usr/bin/env python3
"""r7368 (60) -- THE BASE THAT MOVED.

** THE SUBJECT. **  A gate that measures a population over a git revision range has to name the
range's BASE.  Two of this seat's receipts named it `origin/main`.  That is a ref, not a commit, and
`r7364` landing on the trunk moved it -- so the population fell from 52 of this seat's commits to
`2` with no edit anywhere in the tree, and five gates across four receipts went red on a MERGE.

** WHAT THIS MEASURES. **  How far the shape reaches: every site under `receipts/` where a
revision range's BASE END is a ref name rather than a commit, classified by what the site is FOR.

  ⒜ *the population*  -- how many MEASURING sites there are beyond the two already known.
  ⒝ *the gate layer*  -- how many of the corpus's own `corpus/check_*.py` gates test a range's base.
  ⒞ *the spellings*   -- how many distinct spellings the measuring sites use, against the ONE that
                         `S23`'s `Ⓕ①` adopted the property under and controlled.

** THE SELECTOR IS COMMITTED WITH THE MEASUREMENT (`r7365` ②), and that is the point of this
revision: the defect being measured IS a selector that was in the file and still not committed,
because it named a ref.  The file list, the ref vocabulary and the per-site classification are all
in this file. **
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

#: the frame: this revision's registration commit, filled by the landing push
FRAME = ''

#: ** THE REF VOCABULARY. **  A name that resolves differently on two days.  `HEAD` is included
#: because `HEAD` AS A BASE is the same defect -- as the right-hand end of a range it is correct and
#: is not a site.
REFS = ('origin/main', 'origin/master', 'origin/HEAD', 'origin/trunk',
        'refs/remotes/origin/main', 'main', 'master', 'trunk', 'HEAD')

#: the four spellings a base can be written in, as Python source
_SPELL = (
    ('--not',      re.compile(r"""['"]--not['"]\s*,\s*['"]([^'"]+)['"]""")),
    ('dotdot',     re.compile(r"""['"]\{?[A-Za-z_]*\}?([A-Za-z0-9_/\-]+)\.\.""")),
    ('merge-base', re.compile(r"""['"]merge-base['"][^)\]]*?['"]([^'"]+)['"]\s*[)\]]""")),
    ('triple-dot', re.compile(r"""['"]([A-Za-z0-9_/\-]+)\.\.\.""")),
)

#: ⛔⛭⛭ THE DETECTOR'S OWN DEFECT, FOUND BY USING IT AND REPORTED RATHER THAN QUIETLY FIXED.
#: *The first form scored `22` sites and `18` of them were `merge-base --is-ancestor <PIN> HEAD` --
#: which is not the defect but ** the REPAIRED form verifying its own pin, ** the exact property
#: `S23`'s `Ⓕ①` adopted.  The trailing `'HEAD'` was read as the base of a range that has no base.*
#: ⇒ *** A detector for `a ref where a commit belongs` that counts the check FOR that property as an
#:     instance of it is reading its own remedy as its disease -- and it is this revision's third
#:     shape at one remove: the arm that measured the workflow (`r7358`), the construction that
#:     stopped demonstrating (`S51` `Ⓒ③`), and now the instrument that counts the fix. ***
#: ⌊ `--is-ancestor` takes a rev and a rev and asserts an ORDER; a base belongs to a RANGE.  The
#:   two-rev `merge-base` form is the site; the `--is-ancestor` form is excluded BY NAME, and the
#:   exclusion is controlled below on a line of each kind.
_NOT_A_RANGE = ('--is-ancestor', 'is_ancestor')

#: the ancestry test's argument, and a base named by a VARIABLE rather than a literal
_ANC_RX = re.compile(r'''['"]--is-ancestor['"]\s*,\s*([A-Za-z_][A-Za-z0-9_]*)''')
_BASE_NAME_RX = re.compile(r'''['"]--not['"]\s*,\s*([A-Za-z_][A-Za-z0-9_]*)''')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def receipts(sha=None):
    """every `.py` under `receipts/`, at `sha` if given and live otherwise"""
    if sha:
        return sorted(x for x in git('ls-tree', '-r', '--name-only', sha,
                                     'receipts/').split('\n') if x.endswith('.py'))
    return sorted(x for x in git('ls-files', 'receipts/').split('\n') if x.endswith('.py'))


def gates(sha=None):
    if sha:
        return sorted(x for x in git('ls-tree', '-r', '--name-only', sha,
                                     'corpus/').split('\n')
                      if os.path.basename(x).startswith('check_') and x.endswith('.py'))
    return sorted(x for x in git('ls-files', 'corpus/').split('\n')
                  if os.path.basename(x).startswith('check_') and x.endswith('.py'))


def text(rel, sha=None):
    return git('show', f'{sha}:{rel}') if sha else \
        open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()


def _line_is_site(ln):
    """the (spelling, ref) pairs this ONE line holds -- the whole detector, so the control below
    exercises the same code the scan does and not a copy of it."""
    if ln.lstrip().startswith('#') or any(w in ln for w in _NOT_A_RANGE):
        return []
    return [(name, m.group(1)) for name, rx in _SPELL for m in rx.finditer(ln)
            if m.group(1) in REFS]


def sites(rel, sha=None):
    """every line of `rel` where a revision range's BASE is a ref name, with its spelling.

    ⌗ A comment line is not a site: the shape is named in prose all over this corpus, and a
      sentence about a defect is not the defect.  Blank-line and `#:`-prefixed forms are both cut.
    """
    out = []
    for i, ln in enumerate(text(rel, sha).split('\n'), 1):
        for name, ref in _line_is_site(ln):
            out.append((i, name, ref, ln.strip()[:150]))
    return out


def scan(sha=None):
    return {rel: s for rel in receipts(sha) if (s := sites(rel, sha))}


#: ** THE CLASSIFICATION, BY HAND AND COMMITTED HERE. **  A site is one of three things, and only
#: the first is what arm ⒜ counts:
#:   MEASURING -- the range bounds a population a gate then asserts something about.
#:   FIXTURE   -- the ref is written or read inside a constructed shadow tree, as a control.
#:   ABOUT     -- the site is a STRING naming the shape, in a gate whose subject IS the shape.
#: ⚠ Filled by the measuring pass and committed with it; a site the pass finds and this map does
#:   not name is counted MEASURING, which is the unsafe-for-me direction and the right default.
CLASS = {
    #: the CONTROL STRING both receipts carry: `S23`'s `Ⓕ①` and `S24`'s inherit of it assert that
    #: neither of two repaired receipts contains this expression.  The shape is the SUBJECT here,
    #: written as a literal inside a gate about it -- not a range anything measures.
    'receipts/L_probability/S23_four_items_and_every_one_was_mis_described_because_five_gates_stored_a_snapshot_of_a_rule_instead_of_the_rule.py:404': 'ABOUT',
    'receipts/L_probability/S24_a_gate_on_a_repair_has_a_subject_another_seat_may_rewrite_so_all_three_of_mine_went_red_and_the_selector_two_of_them_were_about_was_still_reading_the_commit_body.py:185': 'ABOUT',
    #: ⛔⛭⛭⛭ THE ONE REMAINING MEASURING SITE, AND IT IS IN THE RECEIPT THAT DIAGNOSED THIS FAILURE
    #: IN ITS OWN PROSE.  *`S24`'s `Ⓔ①` reads: "the commits that crossed them having merged out of
    #: the range the gate reads" -- so that receipt NAMED the merge emptying the range, repaired the
    #: PIN leg it was about, and left the range itself bounded by `origin/main`.*
    #:   ⇒ *** The repair and the diagnosis were in the same gate and only one of them was applied. ***
    'receipts/L_probability/S24_a_gate_on_a_repair_has_a_subject_another_seat_may_rewrite_so_all_three_of_mine_went_red_and_the_selector_two_of_them_were_about_was_still_reading_the_commit_body.py:347': 'MEASURING',
}

#: ⒜ THE POPULATION, beyond the two already known (`P03`, `S5`)
A_KNOWN = 2
A_CENTRAL = 3
A_BAND = (1, 7)
A_SIDES = 'two-sided'

#: ⒝ THE GATE LAYER: how many `corpus/check_*.py` test a revision range's base at all
B_CENTRAL = 0
B_BAND = (0, 0)
B_SIDES = 'point'

#: ⒞ THE SPELLINGS among the MEASURING sites, against the ONE `S23`'s `Ⓕ①` controlled
C_CENTRAL = 2
C_BAND = (1, 4)
C_SIDES = 'two-sided'

RESULT = {}


def score(got, band):
    lo, hi = band
    return lo <= got <= hi


def main():
    sha = FRAME or None
    found = scan(sha)
    print(f'\n  r7368 -- the base that moved.  scanned {len(receipts(sha))} receipt(s)'
          f"{' at ' + sha if sha else ' LIVE'}\n")
    tot = 0
    for rel, ss in sorted(found.items()):
        for ln, name, ref, src in ss:
            k = CLASS.get(f'{rel}:{ln}', 'MEASURING')
            tot += 1
            print(f'    {k:9s} {name:11s} {ref:24s} {os.path.basename(rel)[:46]:48s} L{ln}')
            print(f'              {src}')
    meas = [(rel, ln, name) for rel, ss in found.items() for ln, name, _r, _s in ss
            if CLASS.get(f'{rel}:{ln}', 'MEASURING') == 'MEASURING']
    print(f'\n    sites in all: {tot};  MEASURING: {len(meas)};  '
          f'files holding a MEASURING site: {len({r for r, _l, _n in meas})}')
    #: ⒝ AS REGISTERED: a gate TESTS a range's base if it asserts the property -- that the base
    #: resolves and is an ancestor -- which is spelled `--is-ancestor`.  ⌗ *The first form of this
    #: read grepped for `--not` / `merge-base` / `..HEAD`, which counts a gate that USES a range and
    #: not one that TESTS a base.  Both are printed; the arm is scored on the registered one.*
    #: ⛔ AND THE ARM HAD TO BE READ AS ITS OWN WORDS, NOT AS THE FIRST DETECTOR TO HAND.
    #: *The registration asked how many gates TEST A RANGE'S BASE.  Four of the 129 assert the
    #: ancestry property -- `merge-base --is-ancestor <x> HEAD` -- but on a PIN, never on a base;
    #: seven USE a rev-range and not one tests the base of the range it uses.  All three numbers are
    #: printed and the arm is scored on the registered question, which is the strictest of them.*
    #: ⇒ ** A gate tests a range's base if the value it applies the ancestry test to is ALSO used as
    #:   a base of a rev-range in the same file.  That conjunction is what the words name, and it is
    #:   the whole reason a base could carry a ref for four revisions after `S23` adopted the
    #:   property: the property was enforced on PINS and never once on a BASE. **
    _all = gates(sha)
    _asserts, _tests, _uses = [], [], []
    for _p in _all:
        _t = text(_p, sha)
        _names = set(_ANC_RX.findall(_t))
        if _names:
            _asserts.append(_p)
        _based = set()
        for _ln in _t.split('\n'):
            if _ln.lstrip().startswith('#'):
                continue
            _based |= {_r for _n, _r in _line_is_site(_ln)}
            _based |= set(_BASE_NAME_RX.findall(_ln))
        if _names & _based:
            _tests.append(_p)
        if any(_w in _t for _w in ('--not', 'merge-base', '..HEAD')):
            _uses.append(_p)
    print(f"    corpus/check_*.py that TEST A RANGE'S BASE (the registered question): "
          f"{len(_tests)} of {len(_all)}"
          + (' -- ' + ', '.join(os.path.basename(x) for x in _tests) if _tests else ''))
    print(f"    ... that assert the ANCESTRY PROPERTY at all, on a PIN and not on a base: "
          f"{len(_asserts)} of {len(_all)} -- "
          + ', '.join(os.path.basename(x) for x in _asserts))
    print(f"    ... that merely USE a rev-range: {len(_uses)} of {len(_all)} -- "
          + ', '.join(os.path.basename(x) for x in _uses))
    #: the exclusion, controlled two-sidedly on one line of each kind
    _ctl_fix = "anc = run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'])"
    _ctl_bad = "for c in run(['git', 'log', '--not', 'origin/main']):"
    print(f"    the `--is-ancestor` exclusion, controlled two-sidedly: the repaired form is NOT a "
          f"site ({not _line_is_site(_ctl_fix)}) and a `--not <ref>` line IS "
          f"({bool(_line_is_site(_ctl_bad))})")
    print(f'    distinct spellings among the MEASURING sites: '
          f'{sorted({n for _r, _l, n in meas})}')
    RESULT.update({
        'A_SITES': len(meas),
        'A_FILES': sorted({r for r, _l, _n in meas}),
        'A_NEW': len([1 for r, _l, _n in meas
                      if 'P03_the_enclosed_mass' not in r and '/S5_the_set_shaped' not in r]),
        'B_TESTS': len(_tests),
        'B_ASSERTS_ON_A_PIN': len(_asserts),
        'B_USES': len(_uses),
        'C_SPELLINGS': sorted({n for _r, _l, n in meas}),
        'SITES_BEFORE_DETECTOR_REPAIR': 22,
        'SITES_THE_REPAIR_REMOVED': 18,
    })
    print(f'\n    RESULT = {RESULT}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
