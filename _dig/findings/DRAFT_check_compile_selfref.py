#!/usr/bin/env python3
"""DRAFT — a block for corpus/check_compile.py, in that file's house style.

--- SELF-REFERENCING STATEMENTS (drafted r2376+c54.1xx) ----------------------------------------
A \\ref inside a theorem-class environment that resolves to that environment's OWN label is a
perfectly well-formed reference, so LaTeX is silent and `check_compile` correctly reports zero
undefined refs.  The hazard is entirely in PROSE: a corollary offering itself as the authority
for its own claim reads as an argument and is not one.

It exists because P9's `cor:radiation` acquired one at c54.108.  THE_LIVE_ARC's own strike note
for L-137 says the paragraph was to land "in P9 AFTER `cor:radiation`" -- it landed INSIDE it,
and the sentence "for the reason Corollary~\\ref{cor:radiation} gives" became a self-citation.
The register recorded the right placement and the paper did not, and nothing compared them.

Same species as the cross-paper label collision added at c54.94, and gated the same way.

Standalone runner included at the bottom so this can be exercised before it is merged.
"""
import os, re, sys, glob

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)))

_THMENVS = ('theorem', 'proposition', 'corollary', 'lemma', 'definition',
            'remark', 'conjecture', 'claim', 'example')
_BEGIN = re.compile(r'\\begin\{(' + '|'.join(_THMENVS) + r')\}')
_END   = re.compile(r'\\end\{('   + '|'.join(_THMENVS) + r')\}')
_LABEL = re.compile(r'\\label\{([^}]+)\}')
_REF   = re.compile(r'\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}')


def _self_references(where=None):
    """every \\ref inside a theorem-class environment that points at that environment's own label"""
    bad = []
    root = where or HERE
    for f in sorted(glob.glob(os.path.join(root, '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        lines = [l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')]
        open_at = None; labels = set(); body = []
        for i, l in enumerate(lines, 1):
            if l.lstrip().startswith('%'):
                continue
            if open_at is None and _BEGIN.search(l):
                open_at = i; labels = set(); body = []
            if open_at is not None:
                body.append((i, l)); labels |= set(_LABEL.findall(l))
                if _END.search(l):
                    for ln, bl in body:
                        for r in _REF.findall(bl):
                            if r in labels:
                                bad.append((os.path.basename(f), open_at, ln, r))
                    open_at = None
    print(f"\n  SELF-REFERENCING STATEMENTS: {len(bad)}")
    for f, st, ln, r in bad:
        print(f"    [FAIL] {f}:{ln}  (environment opens line {st})  cites its own label {r}")
    if bad:
        print("\n  A statement may not be the authority for itself.  LaTeX cannot see this --"
              "\n  the reference resolves.  Check where the paragraph was meant to land.")
    return len(bad)


# --- in check_compile.py this goes at module level, next to the other two blocks: ---
#
# _nself = _self_references()
# if _nself:
#     print(f"\n  SELF-REFERENCE FAILURE: {_nself} statement(s) cite their own label.")
#     sys.exit(1)


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'corpus')
    target = os.path.abspath(target)
    n_files = len(glob.glob(os.path.join(target, '*.tex')))
    print(f"  scanning {n_files} .tex under {target}")
    n = _self_references(target)
    print()
    sys.exit(1 if n else 0)
