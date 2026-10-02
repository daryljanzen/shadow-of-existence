#!/usr/bin/env python3
"""label_pin.py -- ** A CHECK WHOSE LABEL AND CONDITION ASSERT OPPOSITE THINGS. **

Built r7129+cc66.99 by node 66's code seat, on node 66's r7129 order; pre-registered at
computations/beyond_the_wall/r7129_cc66_label_pin/PREDICTION.md BEFORE this ran on the tree.

** THE CLASS. **  Every operator in this family keys on the EXPRESSION -- `PROSE-PIN` on counted
matches, `TILT` on whether a pin moves with its data, `REGRID` on whether a window is finer than its
abscissa, `QUOTE-PIN` on a literal from a sentence another seat owns.  *** None of them reads the
label, so none of them can see a check whose label and condition point opposite ways. ***  Four real
instances were found by hand at r7125+cc66.98, three of them in one file.

** WHY IT SURVIVES. **  A passing check with a confident label is the least likely thing in a corpus
to be read twice: the label is what a reader believes and the condition is what the gate enforces,
and nothing compares them.

** ⛔ THE TWO STAGES, AND THE SECOND IS THE WHOLE DESIGN. **  The naive signal -- an absence word in
the label against a condition asserting presence -- fires on the commonest LEGITIMATE idiom in this
corpus, the regression guard on an absence that ENDED ("X is NO LONGER at zero -- supplied at
c54.205", asserting `> 0`).  Sixteen of those were verdicted DELIBERATE at r7125+cc66.98.
  ⇒ *So stage 2 is a NEGATION-OF-THE-ABSENCE detector, and a label carrying one is not flagged.*
  ⌗ *The pre-registration says plainly that stage 2 is where this is expected to be wrong, in both
  directions, and that every survivor needs a human read.*

** WHAT IT CANNOT SEE, as pre-registered: ** a label that is wrong without being OPPOSITE (stale
figures, superseded prose -- most rot is this); an absence word that arrives at runtime through a
variable; a condition whose polarity is indirect through a helper; and the judgement itself, since no
regex settles whether a sentence claims an absence or its end.
"""
import argparse
import ast
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: stage 1 -- the label claims an absence.  Word-boundaried, because `no` inside `now`/`north` and
#: `not` inside `nothing`/`note` are the obvious ways a substring test would lie here.
#: ⛔ r7129+cc66.99, AFTER THE FIRST RUN: `no` and `not` are REMOVED from this list.  *They were in the
#: pre-registered design and they are the reason it failed: 389 of 453 survivors on the tree came from
#: them, because "is not a dichotomy", "does not use" and "the check is not vacuous" are ordinary
#: English and not claims about an absence in the corpus.*  ⇒ **The pre-registration predicted stage 2
#: would be where this was wrong.  It was stage 1, and that is recorded rather than quietly fixed.**
#:   ⌗ *`non-zero`/`nonzero` are excluded explicitly: they are the OPPOSITE of an absence claim and
#:   several receipts say "NON-zero away from zero, so the check is not vacuous".*
#:   ⌗ *`no` returns only as a PHRASE -- `in no paper`, `in no <noun>`, `no paper names` -- because
#:   "STATED IN NO PAPER" is a genuine absence claim about the corpus while the bare word is not.
#:   **Dropping the bare word cost recall 4/4 -> 3/4 and the phrase restores it**, which is the
#:   measurement that chose this form.*
ABSENCE = re.compile(r'(?<![a-z-])(zero|never|nowhere|absent|absence|none|unnamed|undeclared|'
                     r'unmentioned)(?![a-z])'
                     r'|in no [a-z]+|no paper|not named|not mentioned|not in print', re.I)

#: stage 2 -- the label NEGATES that absence, which is the regression-guard idiom and is not a defect.
NEGATED = re.compile(r'no longer|is not at zero|not at zero|ended|now named|now carries|now in print|'
                     r'in print now|is in print|supplied at|filled|discharged|closed|'
                     r'where it was|when this receipt was written|regression guard|'
                     r'has since|since developed|now names|no longer at|'
                     r'is now|are now|now a|was at zero|at zero when', re.I)

#: the condition asserts PRESENCE or a positive count.
PRESENT = re.compile(r'>\s*0|>=\s*1|!=\s*0|>\s*[1-9]')
#: ...or asserts nothing at all (the related kind: r7125+cc66.98's `n >= 0`).
VACUOUS = re.compile(r'>=\s*0|<=\s*-1|\bTrue\b\s*\)?$')


def label_of(node):
    """The literal text of a check/gate call's first argument, f-strings flattened to their
    constant parts.  *A label whose absence word arrives through a variable is invisible here and
    the pre-registration says so.*"""
    if not node.args:
        return None
    a = node.args[0]
    if isinstance(a, ast.Constant) and isinstance(a.value, str):
        return a.value
    if isinstance(a, ast.JoinedStr):
        return ' '.join(v.value for v in a.values
                        if isinstance(v, ast.Constant) and isinstance(v.value, str))
    return None


def sites(path):
    src = open(path, encoding='utf-8', errors='replace').read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id in ('check', 'gate') and len(n.args) >= 2):
            continue
        lab = label_of(n)
        if lab is None:
            continue
        cond = ast.get_source_segment(src, n.args[1]) or ''
        cond = re.sub(r'\s+', ' ', cond).strip()
        out.append((n.lineno, lab, cond))
    return out


def classify(lab, cond):
    """-> (flag, why) or (None, why-not).  *Stage 2 decides almost everything.*"""
    if VACUOUS.search(cond) and not PRESENT.search(cond):
        return 'VACUOUS', 'the condition asserts nothing of its own'
    _lab = re.sub(r'non-?zero', ' ', lab, flags=re.I)          # the opposite of an absence claim
    _lab = re.sub(r'asserted nowhere|printed and asserted nowhere', ' ', _lab, flags=re.I)
    m = ABSENCE.search(_lab)
    if not m:
        return None, 'no absence claim in the label'
    if NEGATED.search(_lab):
        return None, f'absence word {m.group(0)!r} is NEGATED in the label (regression-guard idiom)'
    if not PRESENT.search(cond):
        return None, f'absence word {m.group(0)!r} but the condition does not assert presence'
    return 'OPPOSED', f'label claims absence ({m.group(0)!r}) and the condition asserts presence'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--files', nargs='*')
    ap.add_argument('--counts', action='store_true', help='population figures only')
    a = ap.parse_args()
    files = a.files or sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    keys, flagged, naive, recv = set(), [], set(), 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        has_abs = False
        for ln, lab, cond in sites(f):
            keys.add((rel, lab, cond))
            if ABSENCE.search(lab):
                has_abs = True
                if PRESENT.search(cond):
                    naive.add((rel, lab, cond))
            flag, why = classify(lab, cond)
            if flag:
                flagged.append((flag, rel, ln, lab, cond, why))
        recv += 1 if has_abs else 0
    print()
    print('  LABEL-PIN -- does any check\'s LABEL assert the opposite of its CONDITION?')
    print()
    print(f'    receipts scanned: {len(files)};  distinct (receipt, label, condition) key(s): {len(keys)}')
    print(f'    receipts with at least one absence-word label: {recv}')
    print(f'    stage 1 only (naive: absence word + presence condition): {len(naive)} site(s)')
    print(f'    stage 2 survivors -- REPORTED: {len(flagged)} site(s)')
    print(f'    ⌗ counted as distinct keys and not file lines, which is what a gate would count')
    if not a.counts:
        print()
        for flag, rel, ln, lab, cond, why in sorted(flagged):
            print(f'    [{flag:<8}] {rel}:{ln}')
            print(f'               label: {lab[:150]}')
            print(f'               cond : {cond[:150]}')
            print(f'               why  : {why}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
