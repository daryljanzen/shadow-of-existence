#!/usr/bin/env python3
"""check_pdf_current.py -- IS EVERY COMMITTED PAPER PDF AT LEAST AS NEW AS ITS SOURCE?

** r7265+70.1, on 66's r7265 ③: THE 65th MEMBER.  The corpus has `check_pages_current` for its served HTML,
`check_appendix_current` for its generated appendices, `check_depmatrix` for the matrix and its HTML companion --
and nothing for the PDFs, which are the artefacts a reader actually opens. **  The standing rule is that a touched
paper's PDF is compiled and committed WITH its source.  `check_compile` builds every paper into a scratch
directory and asserts that it builds; it never compares the committed artefact with its source.  Live at `r7262`:
`canonical_time.tex` and `cosmogenesis_paper.tex` changed and no PDF was committed for either.

** WHY THE CHECK IS ON HISTORY AND NOT ON BYTES -- MEASURED, NOT CHOSEN. **  The order's first design was
`check_compile`'s own comparison (rebuild, strip `/CreationDate`, `/ModDate` and the trailer `/ID`) made against the
committed file.  Measured at r7265+70.1 (computations/beyond_the_wall/r7265_70_n1_cite_pdf/pdf.txt): see that file
for whether two rebuilds on one machine agree, and whether a rebuild agrees with a PDF committed from another
machine.  The rule being enforced is the one 66 states -- "compiled and committed WITH its source" -- and that is a
fact about the HISTORY: ** the last commit that touched `<paper>.tex` -- OR ANY FILE IT `\input`s OR
`\includegraphics`es -- must be an ancestor of, or the same as, the last commit that touched `<paper>.pdf`. **
  ⌗ *The dependencies are not optional, and that was measured: with a fuller strip (dates, `/ID` AND the
    cross-reference data, whose offsets move with the date stamp's length -- `Z` on a UTC machine, `-06'00'` on the
    committer's) a rebuild here equals the committed PDF for 16 of the 18 papers.  The two that do not are
    `CR_cosmology` and `SdS-slicing-curve_v2`, whose GENERATED appendices (`appendix_receipts_P15`, `_P03`) were
    regenerated after the PDF was last built -- the `.tex` itself unchanged.  A check on the `.tex` alone passes
    both; this one names exactly those two, so the history instrument and the byte instrument AGREE.*  It needs no toolchain, so it runs in the `fast` job on every push, and
it cannot be fooled by a TeX version.
  ⌗ *What it does NOT establish, stated: that the committed PDF was built FROM that source.  A PDF committed later
    but built from an older `.tex` passes.  That is the byte question, and it is the `compile` job's to ask.*

** SEEDED BOTH WAYS ON THE REAL HISTORY. **  At `46d23b57^` -- the tree just before 66 rebuilt the two r7262
papers -- this check must name exactly `canonical_time.tex` and `cosmogenesis_paper.tex`; at `46d23b57` it must
name neither.  Full history is required (the `fast` job checks out at `fetch-depth: 0`); a shallow clone is
REFUSED, because on one commit every file's last change is the same commit and the check would pass by construction.

    python3 corpus/check_pdf_current.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKIP = re.compile(r'^(RETIRED_|arp_standalone)')          # check_compile's own exclusions
SEED = '46d23b57'                                          # r7265: 66 rebuilt canonical_time and cosmogenesis here
SEED_STALE = ['canonical_time.tex', 'cosmogenesis_paper.tex']
_INPUT = re.compile(r'\\(?:input|include)\{([^}]+)\}')
_GRAPHIC = re.compile(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}')


def _git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace')


def papers(rev=None):
    """the papers check_compile builds: a `.tex` in corpus/ carrying a \\documentclass, as of `rev`"""
    if rev is None:
        names = os.listdir(HERE)
        text = lambda f: open(os.path.join(HERE, f), encoding='utf-8', errors='replace').read()
    else:
        names = [os.path.basename(n) for n in _git('ls-tree', '--name-only', rev, 'corpus/').stdout.split()]
        text = lambda f: _git('show', f'{rev}:corpus/{f}').stdout
    return sorted(f for f in names if f.endswith('.tex') and not SKIP.match(f) and '\\documentclass' in text(f))


def _files(rev):
    if rev == 'HEAD':
        return {f for f in os.listdir(HERE)}
    return {os.path.basename(n) for n in _git('ls-tree', '--name-only', rev, 'corpus/').stdout.split()}


def deps(f, rev='HEAD'):
    """corpus files `f` reads: its `\\input`/`\\include`s and its `\\includegraphics`, commented lines excluded"""
    src = (open(os.path.join(HERE, f), encoding='utf-8', errors='replace').read() if rev == 'HEAD'
           else _git('show', f'{rev}:corpus/{f}').stdout)
    src = '\n'.join(ln for ln in src.split('\n') if not ln.lstrip().startswith('%'))
    have, out = _files(rev), []
    for m in _INPUT.finditer(src):
        n = m.group(1) if m.group(1).endswith('.tex') else m.group(1) + '.tex'
        if n in have:
            out.append(n)
    for m in _GRAPHIC.finditer(src):
        for c in (m.group(1), m.group(1) + '.pdf', m.group(1) + '.png', m.group(1) + '.jpg'):
            if c in have:
                out.append(c)
                break
    return sorted(set(out))


def stale(rev='HEAD'):
    """[(paper, newest_input, its_commit, pdf_commit or None)] for every paper whose PDF is older than its source or
    anything its source reads, at `rev`"""
    out = []
    for f in papers(None if rev == 'HEAD' else rev):
        p = _git('log', '-1', '--format=%H', rev, '--', f'corpus/{f[:-4]}.pdf').stdout.strip()
        for d in [f] + deps(f, rev):
            t = _git('log', '-1', '--format=%H', rev, '--', f'corpus/{d}').stdout.strip()
            if t and (not p or _git('merge-base', '--is-ancestor', t, p).returncode != 0):
                out.append((f, d, t, p or None))
                break
    return out


def main():
    print()
    print('  PDF CURRENCY -- is every committed paper PDF at least as new as its source?')
    print()
    if _git('rev-parse', '--is-shallow-repository').stdout.strip() == 'true':
        print('  ⛔ this is a SHALLOW clone: every file\'s last change is the same commit, so the check would pass')
        print('     by construction.  Fetch full history (`fetch-depth: 0`) and run again.')
        return 1
    seed_bad = []
    if _git('cat-file', '-e', f'{SEED}^{{commit}}').returncode == 0:
        before = {s[0] for s in stale(f'{SEED}^')}
        after = {s[0] for s in stale(SEED)}
        if not set(SEED_STALE) <= before:
            seed_bad.append(f'at {SEED}^ the check must name {SEED_STALE}; it names {sorted(before)}')
        if set(SEED_STALE) & after:
            seed_bad.append(f'at {SEED} the check must no longer name {SEED_STALE}; it names {sorted(after)}')
    else:
        seed_bad.append(f'the seed commit {SEED} is not in this history')
    if seed_bad:
        print('  ⛔ the seed lost a direction:')
        for b in seed_bad:
            print(f'      {b}')
        return 1
    print(f'    seeds hold: at {SEED}^ the two r7262 papers are named stale, and at {SEED}, where 66 rebuilt them, '
          'neither is')
    bad = stale()
    print(f'    {len(papers())} paper(s); {len(bad)} with a PDF older than its source or something it reads')
    if bad:
        print()
        for f, d, t, p in bad:
            print(f'    [STALE] {f}: {d if d != f else "its source"} last changed at {t[:8]}, PDF '
                  + (f'last changed at {p[:8]}, which is not after it' if p else 'never committed'))
        print()
        print('  ⛔ A PAPER WHOSE PDF IS OLDER THAN ITS SOURCE IS SERVED TO A READER AS SOMETHING IT NO LONGER SAYS.')
        print('     Compile it (pdflatex twice, from corpus/) and commit the PDF with the source -- and when a GENERATED')
        print('     input moved (an appendix), the PDF of every paper that reads it is owed with that regeneration.')
        return 1
    print('  every committed paper PDF is at least as new as its source.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
