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
 # ** A IS A FRAMING SET, NOT A QUEUE. **  Each entry reports (the vein, what is MAPPED, where the interior
 # is still DARK) -- because these rows are held open to be KNOWN COMPLETELY and closed from within, so the
 # useful report is the shape of the map, never a question awaiting an answer.  ** They are protected against
 # FLATTENING: against a premature door closure, a papering-over, a sweep under the rug.  Every turn's work is
 # held up against them and asked which vein it probes. **
 'L-221': ('A \u00b7 THE HELD-OPEN VEINS',
   '**PO-5 \u00b7 WHAT MAY EXIST, AND WHY THESE.** *Mapped:* the split is **specified** (12 coloured / 3 '
   'colourless, 4 with $\\nu_R$); the coloured three are the **index of a Dirac operator** and cross to fields '
   '**by being a kernel**; the colourless four are the $D_6$ representations trivial on the deck; the group '
   'acting is **$S_3$**, settled r2494. *Dark:* **no operator whose kernel is the four** \u2014 and nothing yet '
   'says whether *kernel* is the only bridge from a grading to a field'),
 'L-165': ('A \u00b7 THE HELD-OPEN VEINS',
   '**PO-6 \u00b7 WHAT A QUANTUM OF THIS GEOMETRY IS.** *Mapped:* the boundary condition closes **per fibre** '
   'and cannot be broken by the number of fibres; the clause `c54.129` answered was **the one the argument does '
   'not need**; the UV degree is **quartic \u2014 the ordinary zero-point degree** \u2014 and compactness buys '
   'the **IR free**. *Dark:* **defining the sum**; the closed-form nonlinear $\\Lambda>0$ solution; and whether a '
   'theory with **one dimensionful constant** can regulate at all'),
 'L-175': ('A \u00b7 THE HELD-OPEN VEINS',
   "**PO-9 \u00b7 WHAT FIXES THE SUBSTRATE'S DIMENSION.** *Mapped:* the cut is four and **says nothing about the "
   "substrate**; a descent from $D>5$ must be **multi-step**; the construction is **single-step by design** and "
   "one-step-ness is governed by **Rule 2**, not by taste. *Dark:* **whether a second slicing could be "
   "non-arbitrary, its selection forced by the first** \u2014 and the substrate stays bounded **below only**"),
 'L-202': ('A \u00b7 THE HELD-OPEN VEINS',
   "**p0 item 4 \u00b7 WHAT THE SEAM CARRIES.** *Mapped:* the phase is the **antilinear face $K$**; reality "
   "admits **exactly two values**; $K$ acts trivially on the reality set while **$R$ exchanges the branches**; "
   "off-real, $K$ **swaps the two wings of the lap** and $R\\circ K$ **closes charge conjugation**; and $K$ "
   "**fixes the photon congruence**. *Dark:* **whether a MASSIVE trajectory carries a phase** \u2014 the null "
   "ones are $K$'s fixed set"),
 'L-174': ('B \u00b7 THE PHYSICS STILL OWED',
   '**exhibit the general matter dynamics BEYOND spherical symmetry.** P9 states it is ordinary GR at the wall; '
   '`L-207` exhibited it in the spherically symmetric class only'),
 'L-207': ('B \u00b7 THE PHYSICS STILL OWED',
   '\u24f6 gated on PO-6 and must not be opened without it (\u24f5 discharged r2450)'),
 'L-171': ('B \u00b7 THE PHYSICS STILL OWED',
   'PO-7 \u2014 whether the $0.62\\pi$ acoustic-phase disagreement is real against the sky. **What it needs is '
   'the seam-phase scan at PRODUCTION depth** (`FOR_54` 38): the 34%-and-stops result was measured at '
   'LMAXL = 1000'),
 'L-204': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   'R-P stations \u2462\u2463 \u2014 P8/P9, GR field equations and the exact-solution catalogue'),
 'L-206': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   'P3 derives $w$, $u$, $3w$ in \u00a73 and does not introduce the door that throws them until \u00a76 \u2014 '
   '**move the object ahead of its own shadows**; every piece exists'),
 'L-210': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   'the entry-point front \u2014 all 44 sites carry verdicts; live leads worked one at a time'),
 'L-217': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   'the CR/Higgs relation is stated (`CR_AND_THE_HIGGS` \u00a74); **`F1` stays live \u2014 the relation breaks '
   'if the gauge group is ever promoted to forced**'),
 'L-218': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   '\u24f5 the reader-package formats via pandoc in CI (\u24f6 the companion SPEC done r2478)'),
 'L-228': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   '`check_loci` extended to the possessive and compound-noun forms node 52 declined to claim'),
 'L-230': ('C \u00b7 INSTRUMENT AND RECORD WORK',
   'the `COMPUTES:` convention \u2014 uptake **flat at 40 of 357** while the corpus grew a sixth'),
}

ORDER = ['A \u00b7 THE HELD-OPEN VEINS', 'B \u00b7 THE PHYSICS STILL OWED',
         'C \u00b7 INSTRUMENT AND RECORD WORK', 'UNSORTED']


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
    VEIN_PREAMBLE = [
        '',
        "> ## \u26ed\u26ed WHAT FAMILY A IS, because it is not a queue and must not be read as one",
        '>',
        "> ***These are the question families that have not yet been exhaustively explored to a full map of the "
        "interior.*** *They are held above the rest because they set the problem's main veins.*",
        '>',
        "> **\u2337 PROTECTED AGAINST CLOSURE \u2014 and specifically against FLATTENING:** *against a premature "
        "door closure, a papering-over, a sweep under the rug.* ***A vein is not protected because it is fragile. "
        "It is protected because collapsing it would destroy the only thing that tells you which specific "
        "questions are worth asking.***",
        '>',
        "> **\u2337 WORKED DELIBERATELY EVERY TURN, and the direction is inward:** *every action facilitates "
        "closure of the arc while keeping the general question open. Specific probes are asked **against** the "
        "vein \u2014 they go at its nooks and crannies and uncover what it actually is.*",
        "> \u21d2 ***So a vein closes FROM WITHIN, when its interior is completely known \u2014 not from outside "
        "by a verdict. And \u201cexhaustively earned\u201d is the only condition that ends one.***",
        '>',
        "> **\u2337 AND THAT IS WHY THE REPORT BELOW IS *MAPPED* AND *DARK* RATHER THAN A QUESTION:** *the useful "
        "state of a vein is the shape of its map \u2014 what the interior is now known to contain, and where it "
        "is still dark.* ***A vein reported as a single open question has already been flattened by the "
        "reporting.***",
        '>',
        "> \u2337 *Hold each turn's work up against these four and ask **which vein it probes**. Work that probes "
        "none is instrument work \u2014 family C \u2014 and that is fine, but it should be known as that.*",
        '',
    ]
    for fam in ORDER:
        if not groups[fam]:
            continue
        L.append(f'## {fam}')
        if fam.endswith('THE HELD-OPEN VEINS'):
            L.extend(VEIN_PREAMBLE)
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
