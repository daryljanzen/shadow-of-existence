#!/usr/bin/env python3
"""Locate the absence guards whose COUNTER has no control, by MEASUREMENT and not by memory.

An ABSENCE GUARD is an asserting site of the form `LITERAL not in HAYSTACK` where the haystack is a
file the receipt does not own.  Its failure mode is silent: if the haystack read returns the EMPTY
STRING -- a moved file, a path taken from the wrong root, a git call that failed -- the absence holds
trivially and the gate passes on nothing.

A POSITIVE CONTROL on the same haystack is what excludes that: some other asserting site in the same
receipt must require something to BE present in the SAME name.

r7246's proxy was `any non-zero counter assertion anywhere in the file`.  This is narrower: the
control has to be on the same haystack name, which is what the claim needs.
"""
import ast
import glob
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))


def haystack_name(node):
    """the NAME a Compare's right-hand side resolves to, when it is a plain name or a subscript"""
    while isinstance(node, (ast.Subscript, ast.Attribute)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


# ⛔⛭⛭ THE INSTRUMENT IS NARROWED TO ITS CLAIM BEFORE IT REPORTS A NUMBER.
#   *The first cut asked only `is there a `not in` on a name`, and it returned `65` receipts -- almost
#   all of them local string tests over the receipt's own lines (`'# noscan' in ln`), a table row
#   (`'EXCUSED' in _r`), or a label.  **Those are not absence guards: nothing about them can pass on an
#   empty read of someone else's file.***
#     ⇒ *** `r7265` ruled this seat's own pre-registered negative the 63rd member for exactly this --
#         a trigger broader than its claim fires on the wrong site -- so the narrowing happens HERE,
#         before the count is reported, and the wide number is reported beside it as what it was. ***
# ⌗ *Third and final narrowing, to the claim's OWN terms: the haystack must be a PAPER BODY.  The
#   second cut still admitted a flags field, a table row and a literal string variable, because
#   `receipts/` and transitive growth carried names that are not haystacks at all.  **`20` receipts was
#   no better a number than `65`; both were the instrument answering a wider question.***
_FOREIGN = ('corpus', '.tex', 'papers(', 'paper_text', 'read_tex')
_NOT_A_HAYSTACK = ('flags', 'verdict', '_r', 'row', '_K_', 'lab', 'ln', 'seg', 'span')


def foreign_haystacks(tree, src):
    """the names in this module whose VALUE comes from a file the receipt does not own

    *Resolved by reading each assignment's own source segment: a haystack is foreign when its value is
    built from a `corpus/*.tex` read, a papers helper, or a pinned `git show`.  Names assigned from
    another foreign name are foreign too, iterated to a fixed point.*
    """
    asg = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            tgts = n.targets if isinstance(n, ast.Assign) else [n.target]
            seg = ast.get_source_segment(src, n.value) or ''
            for t in tgts:
                if isinstance(t, ast.Name):
                    asg.setdefault(t.id, []).append(seg)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    for e in t.elts:
                        if isinstance(e, ast.Name):
                            asg.setdefault(e.id, []).append(seg)
    foreign = {k for k, segs in asg.items() if any(w in sg for sg in segs for w in _FOREIGN)}
    # ONE step of propagation and no more: `x = ALLP` is a haystack, `flags = row[4]` is not, and a
    # fixed point over six rounds pulled in the second kind through the first.
    foreign |= {k for k, segs in asg.items()
                if any(sg.strip() in foreign or sg.strip().rstrip(')').split('(')[-1] in foreign
                       for sg in segs)}
    return {k for k in foreign if not any(w in k.lower() for w in _NOT_A_HAYSTACK)}


def sites(path):
    try:
        tree = ast.parse(open(path, encoding='utf-8', errors='replace').read())
    except SyntaxError:
        return [], {}

    src = open(path, encoding='utf-8', errors='replace').read()
    foreign = foreign_haystacks(tree, src)
    absent, present = [], {}
    for n in ast.walk(tree):
        if not isinstance(n, ast.Compare) or len(n.ops) != 1:
            continue
        op, lhs, rhs = n.ops[0], n.left, n.comparators[0]
        # ⌗ *The CONTROL side is widened in the same breath the haystack side is narrowed: a positive
        #   test through a NAME bound to a literal (`_K_GENERIC in p12`) is as much a control as a
        #   bare literal is, and the first three cuts missed every one of them.  **An instrument that
        #   is wrong on both sides of the same comparison returns a number that means nothing.***
        if isinstance(lhs, ast.Name):
            lit = '<' + lhs.id + '>'
        elif isinstance(lhs, ast.Constant) and isinstance(lhs.value, str):
            lit = lhs.value
        else:
            continue
        hay = haystack_name(rhs)
        if hay is None:
            continue
        if isinstance(op, ast.NotIn):
            if hay in foreign and not lit.startswith('<'):
                absent.append((n.lineno, lit, hay))
        elif isinstance(op, ast.In):
            present.setdefault(hay, []).append((n.lineno, lit))
    return absent, present


def main():
    bare, controlled = [], []
    for p in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        absent, present = sites(p)
        if not absent:
            continue
        rel = os.path.relpath(p, ROOT)
        for ln, lit, hay in absent:
            (controlled if present.get(hay) else bare).append((rel, ln, lit, hay))
    print(f'  absence-guard sites: {len(bare) + len(controlled)} '
          f'({len(controlled)} controlled on the same haystack, {len(bare)} BARE)')
    print()
    byrec = {}
    for rel, ln, lit, hay in bare:
        byrec.setdefault(rel, []).append((ln, lit, hay))
    for rel in sorted(byrec):
        print(f'  ⛔ {rel}')
        for ln, lit, hay in byrec[rel]:
            print(f'       l.{ln}  `{lit[:70]}`  in `{hay}`')
    print()
    print(f'  receipts carrying a bare site: {len(byrec)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
