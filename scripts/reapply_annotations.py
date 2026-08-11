#!/usr/bin/env python3
"""reapply_annotations.py -- re-apply this line's annotations to FORK-OWNED rows after an absorption.

** THE MERGE LOST THREE ANNOTATIONS AND THE LOSS IS STRUCTURAL, NOT CARELESS. **

Absorption takes the working fork's version of the files the fork owns -- THE_LIVE_ARC above all,
since the fork owns the register.  This line's own ROWS survive, because they are new lines that get
re-inserted.  But an annotation this line writes INTO one of the fork's existing rows does not: the
fork's row comes back as the fork wrote it, and the annotation is gone with no trace.

Found at r2385 by `id_space_census --check`, which went from rc=0 to naming two namespaces:

    PROTECTED_OPEN: PO-4 unfolded   <- L-164's "this row IS PO-4" alias annotation, lost
    OPEN_PROBLEMS_MAP: A·2 unfolded <- L-136's canonical-alias fix (A2 -> A·2), lost

** So the loss is invisible in the diff and visible only in a gate. **  A repair to a file the fork
does not touch survives by luck of ownership; an annotation to a row the fork owns is guaranteed to
be dropped, every single time, forever.

THE FIX, and it is the only one that scales: the annotations are DECLARED here, as (anchor, text)
pairs, and re-applied after every absorption.  Absorption step 3 therefore covers annotations and
not only repairs.  Idempotent -- an annotation already present is skipped -- so it is safe to run
at any time, and `--check` reports any that are missing without writing.

    python3 scripts/reapply_annotations.py            # apply the missing ones
    python3 scripts/reapply_annotations.py --check     # exit 1 if any are missing

Written r2385.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# Each entry: (file, unique anchor in the fork's text, the annotation, a token proving presence)
ANNOTATIONS = [
    ('THE_LIVE_ARC.md',
     '| ~~L-164~~ | ',
     '| ~~L-164~~ | ⌗⌗ **PROTECTED ALIAS (observer line): THIS ROW IS `PROTECTED_OPEN` `PO-4`** — '
     '*colour and isospin as structures on the cut.* ⚠ ***The c54.128 strike reasoned, correctly on the '
     'letter, that "`L-164` appears nowhere in `PROTECTED_OPEN`" — and the object was a protected one '
     'under another name. Tested since: the strike is a BOUNDED negative on named routes (holonomy, '
     'isometry), which the rules permit, so `check_kills` passed for the right reason.*** *The bar is '
     'now alias-matched, so a future strike on this row trips `PO-4`\'s own authorisation requirement.* '
     '**`PO-4` still stands OPEN there; nothing here closes it.** ',
     'PROTECTED ALIAS (observer line): THIS ROW IS'),

    ('THE_LIVE_ARC.md',
     '| **L-165** | ',
     '| **L-165** | ⌗ **PROTECTED ALIAS (observer line): THIS ROW IS `PROTECTED_OPEN` `PO-6`** — '
     '*the interacting tower. `PO-6` lists three clauses and **one is answered** (c54.129: '
     '$\\hat\\Gamma$ **is** bounded below, by the deparametrization); the other two stand.* ',
     'PROTECTED ALIAS (observer line): THIS ROW IS `PROTECTED_OPEN` `PO-6`'),

    # ** r2393: THE REGISTRY WAS TOO NARROW AND THE c54.163 ABSORPTION PROVED IT. **
    # It covered THE_LIVE_ARC only.  But P7's frontier list carries FOUR alias comments this line
    # wrote at r2378 -- and CR_framework.tex is a fork-owned file, so taking the fork's version
    # dropped all four, exactly as the register annotations were dropped at r2385.
    # ** The rule is about OWNERSHIP, not about which file. **  Every annotation this line writes
    # into any file the fork owns belongs here, or it is lost at the next absorption with no trace
    # in the diff.  Caught by `id_space_census --check` flipping to "P7 sec:frontiers: 4 of 4
    # unfolded" INSIDE the verification of the cut -- which is why the cut is verified.
    ('corpus/CR_framework.tex',
     '\\item\\label{frontier:inherited}',
     '%  r2378 REGISTER ALIAS, re-applied r2393 after absorption: the inherited datum -- register '
     '`L-150`, family 3.\n\\item\\label{frontier:inherited}',
     'REGISTER ALIAS, re-applied r2393 after absorption: the inherited datum'),
    ('corpus/CR_framework.tex',
     '\\item\\label{frontier:scalar}',
     '%  r2378 REGISTER ALIAS, re-applied r2393: the scalar sector to a verdict -- register '
     '`L-147`, family 5.\n\\item\\label{frontier:scalar}',
     'the scalar sector to a verdict -- register `L-147`'),
    ('corpus/CR_framework.tex',
     '\\item\\label{frontier:sm}',
     '%  r2378 REGISTER ALIAS, re-applied r2393: the SM fermion and gauge sector -- register '
     '`PO-4` (protected), family 6.\n\\item\\label{frontier:sm}',
     'the SM fermion and gauge sector -- register `PO-4`'),
    ('corpus/CR_framework.tex',
     '\\item\\label{frontier:quantum}',
     '%  r2378 REGISTER ALIAS, re-applied r2393: the interacting quantum tower -- register '
     '`L-165` = `PO-6` (protected), family 8.\n\\item\\label{frontier:quantum}',
     'the interacting quantum tower -- register `L-165` = `PO-6`'),

    ('THE_LIVE_ARC.md',
     '`OPEN_PROBLEMS_MAP` A2 ',
     '`OPEN_PROBLEMS_MAP` A·2 ',
     '`OPEN_PROBLEMS_MAP` A·2'),
]


def main():
    check = '--check' in sys.argv
    missing, applied, present = [], [], []
    for rel, anchor, text, token in ANNOTATIONS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            missing.append((rel, token, 'file absent'))
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        if token in t:
            present.append((rel, token))
            continue
        n = t.count(anchor)
        if n != 1:
            missing.append((rel, token, f'anchor matches {n} time(s), needs exactly 1'))
            continue
        if check:
            missing.append((rel, token, 'missing, anchor found'))
            continue
        open(p, 'w', encoding='utf-8').write(t.replace(anchor, text, 1))
        applied.append((rel, token))

    print()
    print('  FORK-ROW ANNOTATIONS -- this line\'s notes inside rows the fork owns')
    print()
    print(f'  {len(ANNOTATIONS)} declared: {len(present)} present, '
          f'{len(applied)} applied, {len(missing)} missing.')
    for rel, token in applied:
        print(f'    [applied] {rel}: {token[:60]}')
    for rel, token, why in missing:
        print(f'    [MISSING] {rel}: {token[:50]} -- {why}')
    print()
    if missing:
        print('  ** An annotation to a row the FORK owns is dropped by every absorption **, because')
        print('     absorption takes the fork\'s version of the fork\'s files.  The loss is invisible')
        print('     in the diff and visible only in a gate -- at r2385 `id_space_census --check` went')
        print('     from rc=0 to naming PO-4 and A·2 unfolded, which is how these were found.')
        print('     Fix the anchor above or re-declare the annotation; do not hand-edit the row.')
        return 1
    print('  Every declared annotation is in place.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
