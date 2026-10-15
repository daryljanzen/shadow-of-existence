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


def sites(rel, sha=None):
    """every line of `rel` where a revision range's BASE is a ref name, with its spelling.

    ⌗ A comment line is not a site: the shape is named in prose all over this corpus, and a
      sentence about a defect is not the defect.  Blank-line and `#:`-prefixed forms are both cut.
    """
    out = []
    for i, ln in enumerate(text(rel, sha).split('\n'), 1):
        if ln.lstrip().startswith('#'):
            continue
        for name, rx in _SPELL:
            for m in rx.finditer(ln):
                if m.group(1) in REFS:
                    out.append((i, name, m.group(1), ln.strip()[:150]))
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
CLASS = {}

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
    _g = [p for p in gates(sha)
          if any(w in text(p, sha) for w in ('--not', 'merge-base', '..HEAD'))]
    print(f'    corpus/check_*.py gates testing a range base: {len(_g)} of {len(gates(sha))}'
          f"{' -- ' + ', '.join(os.path.basename(x) for x in _g) if _g else ''}")
    print(f'    distinct spellings among the MEASURING sites: '
          f'{sorted({n for _r, _l, n in meas})}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
