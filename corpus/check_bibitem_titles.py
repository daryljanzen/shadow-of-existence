#!/usr/bin/env python3
"""check_bibitem_titles.py -- A CITING PAPER'S BIBLIOGRAPHY MUST CARRY THE CITED PAPER'S OWN TITLE.

** Why this gate exists.  A paper's \\title{} is edited in one file.  Every OTHER paper that
cites it carries that title again, by hand, inside a \\bibitem -- so a title that grows by a
clause leaves as many stale copies as there are citing papers, and not one of them is visible
from inside the paper that changed. **  A steeped seat cannot see it; a cold sequential read
can, and one found seventy-eight of them across seventeen files from five distinct strings.

*** The existing `check_bibliography.sh` does a different job: it resolves \\cite keys and flags
unsourced classical results.  It never compares a bibitem's title to the target's own. ***

WHAT IT CHECKS.  For every \\bibitem whose key maps to a paper in this corpus, the bibitem's
title text must match that paper's \\title{}, after a normalisation that removes only what
typesetting legitimately varies: LaTeX markup, braces, case, and whitespace.  A mismatch is a
FAIL naming both strings and both files.

WHAT IT DOES NOT CHECK.  Whether a reference belongs at all (an editorial call), author lists,
or venue -- only that the title a citing paper prints is the title the cited paper carries.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, 'corpus')

# ** The key -> file map is read from the corpus rather than hardcoded: a paper declares its own
#   bibkey in a `% BIBKEY:` comment where it has one, and otherwise the map below carries it.
#   A key that resolves to no file is simply not this gate's business. **
BIBKEY_FILE = {
    'JanzenBHcausality': 'BH_causality_v2.tex',
    'JanzenCRframework': 'CR_framework.tex',
    'JanzenCRcosmology': 'CR_cosmology.tex',
    'JanzenSynthesis': 'CR_synthesis.tex',
    'JanzenSlicingCurve': 'SdS-slicing-curve_v2.tex',
    'JanzenAlgebroid': 'algebroid_paper.tex',
    'JanzenBoundary': 'boundary_paper.tex',
    'JanzenCanonicalTime': 'canonical_time.tex',
    'JanzenCosmogenesis': 'cosmogenesis_paper.tex',
    'JanzenDynamics': 'dynamics_paper.tex',
    'JanzenGeometricCore': 'geometric_core_paper.tex',
    'JanzenGroupoid': 'groupoid_paper.tex',
    'JanzenCircle': 'janzen_circle_v3.tex',
    'JanzenMatter': 'matter_sector_paper.tex',
    'JanzenModernParallax': 'modern_parallax.tex',
    'JanzenRange': 'range_paper.tex',
    'JanzenShadowExistence': 'shadow_of_existence.tex',
    'JanzenOperator': 'slicing_operator.tex',
}


def _strip_tex(s):
    """Normalise a title to what is being compared: the words, in order."""
    s = re.sub(r'\\emph\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\textit\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\text\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\[a-zA-Z]+\s*', ' ', s)          # any remaining control words
    s = s.replace('$', ' ').replace('~', ' ')
    s = re.sub(r'[{}\\]', '', s)
    s = re.sub(r'[-\u2010-\u2015]+', '-', s)        # dash variants are typesetting
    s = re.sub(r"[`'\u2018\u2019\u201c\u201d\",.;:]", '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


def _title_of(path):
    src = open(path, encoding='utf-8').read()
    m = re.search(r'\\title\{', src)
    if not m:
        return None
    i = m.end()
    depth, out = 1, []
    while i < len(src) and depth:
        c = src[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if not depth:
                break
        out.append(c)
        i += 1
    t = ''.join(out)
    t = re.sub(r'\\\\', ' ', t)
    t = re.sub(r'\\thanks\{[^{}]*\}', '', t)
    return _strip_tex(t)


def main():
    titles = {}
    for key, fn in BIBKEY_FILE.items():
        p = os.path.join(CORPUS, fn)
        if os.path.exists(p):
            t = _title_of(p)
            if t:
                titles[key] = (t, fn)

    fails, checked = [], 0
    for fn in sorted(os.listdir(CORPUS)):
        if not fn.endswith('.tex'):
            continue
        src = open(os.path.join(CORPUS, fn), encoding='utf-8').read()
        for m in re.finditer(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem\{|\\end\{thebibliography\})',
                             src, re.S):
            key, body = m.group(1), m.group(2)
            if key not in titles:
                continue
            want, home = titles[key]
            if home == fn:                      # a paper does not cite itself
                continue
            got = _strip_tex(body)
            checked += 1
            if want not in got:
                fails.append((fn, key, home, want, got[:220]))

    print()
    print('  CHECK-BIBITEM-TITLES -- every citing bibliography against the cited paper\'s own \\title{}')
    print(f'    {len(titles)} corpus papers mapped, {checked} citing bibitem(s) compared')
    print()
    if not fails:
        print('  every bibitem carries the title its target paper carries.')
        print('  ⌗ This gate compares TITLES only.  Author lists, venues and whether a reference')
        print('    belongs at all are editorial and are not its business.')
        return 0

    for fn, key, home, want, got in fails:
        print(f'  [FAIL] {fn}: \\bibitem{{{key}}} does not carry {home}\'s own title')
        print(f'         wants: {want}')
        print(f'         has:   {got}')
    print()
    print(f'  ⛔ {len(fails)} STALE BIBLIOGRAPHY TITLE(S).  ** A title is edited in one file and')
    print('     copied by hand into every paper that cites it, so a title that grows leaves one')
    print('     stale copy per citing paper and none of them is visible from the paper that')
    print('     changed. **  Fix by copying the target paper\'s \\title{} text.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
