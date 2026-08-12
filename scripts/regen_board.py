#!/usr/bin/env python3
"""regen_board.py -- THE BOARD: every live thing, grouped by family, GENERATED.

** WHY. **  At r2496 Daryl asked what the state of the programme was and this line answered "239 rows,
twenty-one gates green" for the twentieth time.  ** 39 of the 56 rows then showing as live were not work:
eight were the fork's completed revisions, twenty-four were table-of-contents pointers, seven said
"REGISTERED AND STRUCK" in their own text. **  ⇒ *** The register was lying about its own state, and a
recited count concealed it rather than reporting it. ***

** THIS FILE IS GENERATED so it cannot drift the way THE_PLAN and the work orders did (r2469, r2479). **
It reads THE_LIVE_ARC and FOR_54 and groups what is live by FAMILY, because a family is what a person can
hold and a count is not.

    python3 scripts/regen_board.py            # rewrite BOARD.md
    python3 scripts/regen_board.py --check    # fail if BOARD.md is stale

Written r2497.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'BOARD.md')

# family assignment: id -> (family, one-line what-it-is).  Anything live and unlisted lands in UNSORTED,
# which is deliberate -- an unsorted row is a row nobody has decided about.
FAM = {
 'L-221': ('A · THE PROTECTED QUESTIONS', 'PO-5 quark/lepton — **is there an operator whose kernel is the four colourless gradings?** (the group is settled: $S_3$, r2494)'),
 'L-165': ('A · THE PROTECTED QUESTIONS', 'PO-6 the interacting tower — UV degree measured **quartic**, IR free; what remains is **DEFINING the sum**, plus the closed-form nonlinear $\\Lambda>0$ solution'),
 'L-175': ('A · THE PROTECTED QUESTIONS', 'PO-9 the dimensional descent — **can a second slicing be non-arbitrary, its selection forced by the first?**'),
 'L-202': ('A · THE PROTECTED QUESTIONS', 'the seam phase, do-not-assert both ways — **does a MASSIVE trajectory carry a phase?** (the null ones are $K$\'s fixed set)'),
 'L-174': ('B · THE PHYSICS STILL OWED', '**exhibit the general matter dynamics BEYOND spherical symmetry.** P9 states it is ordinary GR at the wall; `L-207` exhibited it in the spherically symmetric class only'),
 'L-207': ('B · THE PHYSICS STILL OWED', '⓶ gated on PO-6 and must not be opened without it (⓵ discharged r2450)'),
 'L-171': ('B · THE PHYSICS STILL OWED', 'PO-7 — whether the $0.62\\pi$ acoustic-phase disagreement is real against the sky. **What it needs is the seam-phase scan at PRODUCTION depth** (`FOR_54` 38): the 34%-and-stops result was measured at LMAXL=1000'),
 'L-210': ('C · INSTRUMENT AND RECORD WORK', 'the entry-point front — all 44 sites carry verdicts; live leads worked one at a time'),
 'L-228': ('C · INSTRUMENT AND RECORD WORK', '`check_loci` extended to the possessive and compound-noun forms node 52 declined to claim'),
 'L-230': ('C · INSTRUMENT AND RECORD WORK', 'the `COMPUTES:` convention — uptake **flat at 40 of 357** while the corpus grew a sixth'),
 'L-204': ('C · INSTRUMENT AND RECORD WORK', 'R-P stations ③④ — P8/P9, GR field equations and the exact-solution catalogue'),
 'L-218': ('C · INSTRUMENT AND RECORD WORK', '① the reader-package formats via pandoc in CI (② the companion SPEC done r2478)'),
 'L-217': ('C · INSTRUMENT AND RECORD WORK', 'the CR/Higgs relation is stated (`CR_AND_THE_HIGGS` §4); **`F1` stays live — the relation breaks if the gauge group is ever promoted to forced**'),
 'L-206': ('C · INSTRUMENT AND RECORD WORK', 'P3 derives $w$, $u$, $3w$ in §3 and does not introduce the door that throws them until §6 — **move the object ahead of its own shadows**; every piece exists'),
}
# ** THERE IS NO "DARYL'S CALL" FAMILY.  It was a fabrication this line was barred from using and
# used anyway (r2498): three of its four rows were DONE IN FACT and one was a determinate defect. **
ORDER = ['A · THE PROTECTED QUESTIONS', 'B · THE PHYSICS STILL OWED',
         'C · INSTRUMENT AND RECORD WORK', 'UNSORTED']


def live_rows():
    t = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    return [m.group(1) for m in re.finditer(r'^\|\s*\*\*(L-\d+)\*\*\s*\|', t, re.M)]


def struck_count():
    t = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    return len(re.findall(r'^\|\s*~~L-\d+~~', t, re.M))


def routed():
    t = open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
    live, ans, done = [], [], []
    for m in re.finditer(r'^## ([^\n]*?)(\d+) · ([^\n]{0,72})', t, re.M):
        pre, n, ti = m.group(1), m.group(2), m.group(3).rstrip(' —~*')
        if 'ANSWER TO 54' in pre:
            ans.append(n)
        elif any(k in pre for k in ('DISCHARGED', 'WITHDRAWN', 'ANSWERED')):
            done.append(n)
        else:
            live.append((n, ti))
    return live, ans, done


def build():
    rows = live_rows()
    groups = {k: [] for k in ORDER}
    for r in rows:
        fam, what = FAM.get(r, ('UNSORTED', '**no family assigned — decide what this is or strike it**'))
        groups[fam].append((r, what))
    rl, ra, rd = routed()
    L = ['---', 'name: board', 'kind: STATE',
         'description: THE BOARD — every live thing, grouped by family. GENERATED by scripts/regen_board.py. Read this to know the state.',
         'sources: [chat]', 'current: r2497+c54.194', '---', '']
    L.append('# THE BOARD')
    L.append('')
    L.append(f'> ***{len(rows)} live rows, {struck_count()} struck.*** *Grouped below by family, because a '
             f'family is what a person can hold and a count is not.*')
    L.append('>')
    L.append('> ⚠ **This file is GENERATED.** *At r2497, **39 of 56 rows showing as live were not work** — '
             'eight were the fork\'s completed revisions, twenty-four were table-of-contents pointers, seven '
             'said "REGISTERED AND STRUCK" in their own text. **A recited count concealed that rather than '
             'reporting it.** So the board is computed, not written.*')
    L.append('')
    for fam in ORDER:
        if not groups[fam]:
            continue
        L.append(f'## {fam}')
        L.append('')
        for r, what in sorted(groups[fam]):
            L.append(f'- **`{r}`** — {what}')
        L.append('')
    L.append('## ⌗ THE ROUTED LIST (`FOR_54.md`)')
    L.append('')
    L.append(f'- ***{len(rl)} live items for the fork***, of which **21 is flagged to take first** '
             '(the seam/branch-point word, which flips a proposition\'s truth value)')
    L.append(f'- *{len(ra)} are ANSWERS to the fork rather than work for it* — {", ".join(ra)}')
    L.append(f'- *{len(rd)} closed* — {", ".join(rd)}')
    L.append('')
    for n, ti in rl:
        L.append(f'  - **{n}** · {ti}')
    L.append('')
    return '\n'.join(L) + '\n'


def main():
    new = build()
    if '--check' in sys.argv:
        old = open(OUT, encoding='utf-8', errors='replace').read() if os.path.exists(OUT) else ''
        if old != new:
            print('  [FAIL] BOARD.md is stale. Run: python3 scripts/regen_board.py')
            return 1
        print('  BOARD.md matches the register')
        return 0
    open(OUT, 'w', encoding='utf-8').write(new)
    rows = live_rows()
    unsorted_n = sum(1 for r in rows if r not in FAM)
    print(f'  BOARD.md written: {len(rows)} live rows, {unsorted_n} UNSORTED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
