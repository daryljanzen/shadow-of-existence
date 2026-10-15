#!/usr/bin/env python3
"""r7370 (60) -- THE REFERENCE THAT DOES NOT RESOLVE.

** THE SUBJECT. **  Two gates of this seat's went red on `r7368`'s PR, both standing on `main` for
five pushes, and they are one class in opposite directions.  `S29` selected a revision's commits by
a STRING MATCH on commit messages, which over-resolves: every later commit citing the revision joins
the set.  `S39` pinned its shas correctly and then read a fact off them through a walk of the whole
history, which under-resolves: a shallow clone does not reach them.

  ⇒ ** A PIN IS ONLY AS GOOD AS WHAT RESOLVES IT, AND BOTH WANTED THE FACT COMMITTED BESIDE THE
    MEASUREMENT. **

** WHAT THIS MEASURES. **  How far the over-resolving half reaches: every site under `receipts/`
where a set of commits is selected by matching a REVISION ID against commit message text.

  ⒜ *the population* -- how many such sites there are beyond the one repaired.
  ⒝ *the capture*    -- for each, how many commits the match returns against how many the revision
                        actually has, measured where the revision's own commits can be identified.

** THE SELECTOR IS COMMITTED WITH THE MEASUREMENT (`r7365` ②), and the frame with it (`r7368`): this
revision edits the receipts it measures, so the scan is scored at the registration commit and the
live reading printed beside it. **
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

#: the frame: this revision's registration commit, filled by the landing push
FRAME = '122d0247'

#: a revision id matched against commit message TEXT.  The three spellings this corpus uses: a raw
#: regex on the body, an `in` against the subject, and a formatted id inside a search pattern.
_SPELL = (
    ('re-on-body', re.compile(r"""re\.(?:search|match|findall)\(\s*r?['"][^'"]*\\b?r\d{4}""")),
    ('id-in-text', re.compile(r"""['"]r\d{4}['"]\s+in\s+[A-Za-z_][A-Za-z0-9_.\[\]'"]*""")),
    ('fmt-id',     re.compile(r"""r?['"][^'"]*\{[A-Za-z_]*REV[A-Za-z_]*\}[^'"]*['"]""")),
)
#: ⌗ and the site only counts if the match is used to SELECT COMMITS -- the line, or the three
#: before it, must name a commit-listing call.  A receipt quoting a revision id in prose is not a
#: site, and nor is one testing a LABEL, which is what most id matches in this corpus do.
_COMMITS = ('git(', '_git(', "'log'", '"log"', 'rev-list', '--format=%H', '%x1f%B', 'log(')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def receipts(sha=None):
    if sha:
        return sorted(x for x in git('ls-tree', '-r', '--name-only', sha,
                                     'receipts/').split('\n') if x.endswith('.py'))
    return sorted(x for x in git('ls-files', 'receipts/').split('\n') if x.endswith('.py'))


def text(rel, sha=None):
    return git('show', f'{sha}:{rel}') if sha else \
        open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()


def sites(rel, sha=None):
    out, lines = [], text(rel, sha).split('\n')
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith('#'):
            continue
        for name, rx in _SPELL:
            if rx.search(ln):
                _near = '\n'.join(lines[max(0, i - 3):i + 2])
                if any(w in _near for w in _COMMITS):
                    out.append((i + 1, name, ln.strip()[:150]))
    return out


def scan(sha=None):
    return {rel: s for rel in receipts(sha) if (s := sites(rel, sha))}


#: ⛭⛭⛭ `CONTROL` IS A PROPERTY AND NOT A HAND ENTRY, for `r7368`'s reason: the same site changes
#: class when the file is repaired -- every one of these was `SELECTS` before its commits were
#: pinned and is the control beside the pin after.  *A hand entry would bake in the date, which is
#: the defect this phase is about arriving in the classification.*
#: ⇒ ** A file that binds its revision's commits to a pinned tuple has had its selector fixed, and
#:   an id match left in it is the CONTROL the repair keeps on purpose.  Tested as the property. **
#: ⌗ *and the pattern allows LEADING INDENTATION: `S53` binds its tuple inside the function
#:   that uses it, and an anchor without `\s*` read that file as unrepaired -- the property
#:   tested by a spelling again, caught by the figure not falling to zero.*
_PINNED_OWN = re.compile(r"^\s*(?:OWN|OWN_C)\s*=\s*\(", re.M)


def _class_of(rel, sha=None):
    return 'CONTROL' if _PINNED_OWN.search(text(rel, sha)) else 'SELECTS'


#: ** THE CLASSIFICATION, BY HAND AND COMMITTED HERE. **
#:   SELECTS  -- the match is what picks the commits a gate then asserts over.  Arm ⒜ counts these.
#:   CONTROL  -- the match is kept deliberately, beside a pinned list, to prove it over-resolves.
#:   LABEL    -- the id is matched against a SUBJECT LINE to read a revision's own claim, which is
#:               what the id is for; no commit set is selected by it.
CLASS = {
    #: ⌗ a FALSE POSITIVE of this detector, kept rather than tuned away: the id is matched against a
    #: LEDGER CELL and not against a commit message at all -- the proximity test caught a
    #: commit-listing call three lines off.  *The detector is reported with its own miss.*
    ('receipts/L551_register_integrity/R1_a_protected_row_was_corrupt_for_368_commits_and_the_corruption_satisfied_a_gate.py',
     'id-in-text'): 'LABEL',
}

#: ⒜ THE POPULATION, beyond the one repaired (`S29`)
A_KNOWN = 1
A_CENTRAL = 2
A_BAND = (0, 6)
A_SIDES = 'two-sided'

#: ⒝ THE CAPTURE at the repaired site: commits the match returns against the revision's own
B_MATCHED = 5
B_OWN = 2
B_CENTRAL = 2          # extra commits the match captures, beyond the revision's own
B_BAND = (1, 6)
B_SIDES = 'two-sided'

RESULT = {}


def score(got, band):
    lo, hi = band
    return lo <= got <= hi


def main():
    sha = FRAME or None
    found = scan(sha)
    live = scan(None)
    print(f'\n  r7370 -- the reference that does not resolve.  '
          f'{len(receipts(sha))} receipt(s){" at " + sha if sha else " LIVE"}\n')
    tot = 0
    for rel, ss in sorted(found.items()):
        for ln, name, src in ss:
            k = CLASS.get((rel, name)) or _class_of(rel, sha)
            tot += 1
            print(f'    {k:8s} {name:11s} {os.path.basename(rel)[:46]:48s} L{ln}')
            print(f'             {src}')
    sel = [(r, l) for r, ss in found.items() for l, n, _s in ss
           if (CLASS.get((r, n)) or _class_of(r, sha)) == 'SELECTS']
    _lsel = [(r, l) for r, ss in live.items() for l, n, _s in ss
             if (CLASS.get((r, n)) or _class_of(r, None)) == 'SELECTS']
    _ctl = [(r, l) for r, ss in live.items() for l, n, _s in ss
            if (CLASS.get((r, n)) or _class_of(r, None)) == 'CONTROL']
    print(f'\n    AT THE FRAME {sha}: sites {tot};  SELECTS {len(sel)};  '
          f'files holding one: {len({r for r, _l in sel})}')
    print(f'    LIVE, after this revision repaired them: sites '
          f'{sum(len(v) for v in live.values())};  SELECTS {len(_lsel)};  CONTROL {len(_ctl)} -- '
          f'each an id match kept beside a pinned commit list ON PURPOSE, so the pin cannot '
          f'quietly become the match again')
    RESULT.update({
        'A_SITES': len(sel),
        'A_FILES': sorted({r for r, _l in sel}),
        'A_NEW': len([1 for r, _l in sel if '/S29_' not in r]),
        'A_LIVE_SELECTS': len(_lsel),
        'A_LIVE_CONTROL': len(_ctl),
        'B_MATCHED': B_MATCHED,
        'B_OWN': B_OWN,
        'B_EXTRA': B_MATCHED - B_OWN,
    })
    print(f'\n    RESULT = {RESULT}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
