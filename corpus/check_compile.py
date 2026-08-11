#!/usr/bin/env python3
"""check_compile.py -- L-43: the corpus did not compile for an unknown span and nothing
checked it per turn.  144 errors were found at c54.9 by accident.  This is the fourth gate.

Compiles every paper with a \documentclass and fails on any LaTeX error, undefined citation
or undefined reference.  Run it every turn; it is the cheapest gate the corpus has.
"""
import glob, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = re.compile(r'^(RETIRED_|arp_standalone)')
def main():
    papers = sorted(f for f in os.listdir(HERE)
                    if f.endswith('.tex') and not SKIP.match(f)
                    and '\\documentclass' in open(os.path.join(HERE, f),
                                                  encoding='utf-8', errors='replace').read())
    bad = []
    print(f"  compiling {len(papers)} papers")
    for f in papers:
        subprocess.run(['pdflatex', '-interaction=nonstopmode', f], cwd=HERE,
                       capture_output=True)
        p = subprocess.run(['pdflatex', '-interaction=nonstopmode', f], cwd=HERE,
                           capture_output=True, text=True, errors='replace')
        log = p.stdout
        errs = len(re.findall(r'(?m)^! ', log))
        cites = len(re.findall(r'Citation .* undefined', log))
        refs = len(re.findall(r'Reference .* undefined', log))
        # r2376+c54.36: a \rcpt{} marker whose Appendix-R label is missing renders as a DEAD
        # LINK and warns as 'Hyper reference' -- lowercase, so the refs regex above never saw
        # it.  105 of them had accumulated across twelve papers because the appendix generator
        # had not been re-run since the receipts were added.  It is generated; regenerate it.
        dead = len(re.findall(r"Hyper reference `rcpt:", log))
        if errs or cites or refs or dead:
            bad.append((f, errs, cites, refs))
            print(f"    [FAIL] {f}: {errs} errors, {cites} undefined citations, "
                  f"{refs} undefined refs, {dead} dead receipt links"
                  + ("  <- run make_all_appendices.py" if dead else ""))
    print()
    if bad:
        print(f"  COMPILE FAILURES: {len(bad)} of {len(papers)}")
        return 1
    print(f"  All {len(papers)} papers compile at 0 errors, 0 undefined citations, "
          "0 undefined refs, 0 dead receipt links.")
    return 0

# --- CROSS-PAPER LABEL COLLISION (added r2376+c54.94) ---------------------------------------
# The fold of the open-problems map into the lead register put the supersession scan across every
# paper at once, and it immediately conflated TWO DIFFERENT PROPOSITIONS both labelled prop:wall
# -- P11's wall of inhomogeneity and P14's throat wall.  LaTeX never complains, because each
# paper compiles alone; the hazard is entirely in PROSE and in the registers, where "prop:wall"
# reads as a unique name and is not one.  P11's was renamed prop:radiative-wall at c54.94.
#
# Generic SECTION names colliding (sec:intro in eleven papers) are harmless and are reported
# only.  THEOREM-CLASS labels -- prop/thm/lem/cor/defn -- are cited as if unique and FAIL.
def _label_collisions():
    import collections
    owner = collections.defaultdict(set)
    for _t in sorted(glob.glob(os.path.join(HERE, '*.tex'))):
        if 'appendix_receipts' in os.path.basename(_t):
            continue
        _b = '\n'.join(l for l in open(_t, encoding='utf-8', errors='replace').read().split('\n')
                        if not l.lstrip().startswith('%'))
        for _m in re.finditer(r'\\label\{([^}]+)\}', _b):
            owner[_m.group(1)].add(os.path.basename(_t).replace('.tex', ''))
    coll = {k: sorted(v) for k, v in owner.items() if len(v) > 1}
    thm = {k: v for k, v in coll.items()
           if k.split(':')[0] in ('prop', 'thm', 'lem', 'cor', 'defn')}
    print(f"\n  CROSS-PAPER LABEL COLLISIONS: {len(coll)} total, "
          f"{len(thm)} of theorem class")
    for k, v in sorted(coll.items()):
        tag = '[FAIL]' if k in thm else '[note]'
        print(f"    {tag} {k:<26} {len(v)} papers: {', '.join(v)}")
    if thm:
        print("\n  A theorem-class label is cited by bare name in prose and in the registers, so a"
              "\n  collision there is a real ambiguity even though LaTeX never sees it.")
    return len(thm)

_ncoll = _label_collisions()
if _ncoll:
    print(f"\n  COLLISION FAILURE: {_ncoll} theorem-class label(s) defined in more than one paper.")
    sys.exit(1)


# --- CAPTION-ONLY CORRECTIONS (added r2376+c54.103) --------------------------------------------
# THE_BASE_RATE.md fourth entry: at r2204 P15's low-multipole depth was corrected -- new numbers, a
# new qualitative feature (the minimum at ell=4), and an explicit "is superseded" -- INSIDE A FIGURE
# CAPTION, and nowhere else.  The body, abstract, results list, sec:scope and summary went on saying
# the superseded figure for a hundred and seventy revisions.  A caption is the one place in a paper
# that is neither argument nor summary: no gate reads it as prose and no reader reaches it before the
# sentence it contradicts.  So: a caption may RESTATE a number the body carries; it may not be the
# only place a corrected number lives.
_CORRECTION = re.compile(r'\b(supersed\w+|is corrected|now reads|no longer\s+(?:the|holds)'
                         r'|revised from|earlier figure|older figure)\b', re.I)
_NUM = re.compile(r'(?<![\d.])(0\.\d{2,3})(?![\d])')

def _captions(t):
    """yield the brace-balanced body of every \\caption{...}"""
    for m in re.finditer(r'\\caption\*?\s*\{', t):
        i = m.end(); d = 1
        while i < len(t) and d:
            if t[i] == '{' and t[i-1] != '\\':
                d += 1
            elif t[i] == '}' and t[i-1] != '\\':
                d -= 1
            i += 1
        yield m.start(), t[m.end():i-1]

def _caption_only_corrections():
    bad = []
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        t = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                      if not l.lstrip().startswith('%'))
        caps = list(_captions(t))
        if not caps:
            continue
        body = t
        for st, c in caps:                       # the body is the paper MINUS its captions
            body = body.replace(c, ' ')
        for st, c in caps:
            if not _CORRECTION.search(c):
                continue
            orphans = sorted({n for n in _NUM.findall(c) if n not in body})
            if orphans:
                bad.append((os.path.basename(f), sorted(set(_CORRECTION.findall(c)))[:2], orphans))
    print(f"\n  CAPTION-ONLY CORRECTIONS: {len(bad)} caption(s) assert a correction whose figures "
          f"the body does not carry")
    for f, words, orph in bad:
        print(f"    [FAIL] {f:<28} correction language {words} ; body lacks {orph}")
    if bad:
        print("\n  A caption may restate what the body says.  It may not be the only place a"
              "\n  corrected number lives -- see THE_BASE_RATE.md, fourth entry.")
    return len(bad)

_ncap = _caption_only_corrections()
if _ncap:
    print(f"\n  CAPTION FAILURE: {_ncap} correction(s) live only in a figure caption.")
    sys.exit(1)

if __name__ == '__main__':
    sys.exit(main())
