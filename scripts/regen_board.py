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
# ** THE VEINS -- held open to be known inside and out.  See THE_METHOD.md. **
# (id, short name, MAPPED, DARK)
VEINS = {
 'L-221': ("PO-5 \u00b7 WHAT MAY EXIST, AND WHY THESE",
   "the split is **specified** (12 coloured / 3 colourless, 4 with $\\nu_R$); the coloured three are the **index of "
   "a Dirac operator** and cross to fields **by being a kernel**; the colourless four are the $D_6$ representations "
   "trivial on the deck; the group acting is **$S_3$**",
   "**no operator whose kernel is the four** \u2014 and nothing yet says whether *kernel* is the only bridge from a "
   "grading to a field"),
 'L-165': ("PO-6 \u00b7 WHAT A QUANTUM OF THIS GEOMETRY IS",
   "the boundary condition closes **per fibre** and cannot be broken by the number of fibres; the clause `c54.129` "
   "answered was **the one the argument does not need**; the UV degree is **quartic**, the ordinary zero-point "
   "degree; compactness buys the **IR free**",
   "**defining the sum**; the closed-form nonlinear $\\Lambda>0$ solution; and whether a theory with **one "
   "dimensionful constant** can regulate at all; and \u2014 r2505 \u2014 **what selects among five-component shears WITHOUT assuming vacuum**, since the corpus\u2019s only shear-selection principle (Goldberg\u2013Sachs) is vacuum-bound"),
 'L-175': ("PO-9 \u00b7 WHAT FIXES THE SUBSTRATE'S DIMENSION",
   "the cut is four and **says nothing about the substrate**; a descent from $D>5$ must be **multi-step**; the "
   "construction is **single-step by design** and one-step-ness is governed by **Rule 2**, not taste",
   "**whether a second slicing could be non-arbitrary, its selection forced by the first** \u2014 and the substrate "
   "stays bounded **below only**"),
 'L-202': ("p0 item 4 \u00b7 WHAT THE SEAM CARRIES",
   "the phase is the **antilinear face $K$**; reality admits **exactly two values**; $K$ acts trivially on the "
   "reality set while **$R$ exchanges the branches**; off-real, $K$ **swaps the two wings of the lap** and "
   "$R\\circ K$ **closes charge conjugation**; $K$ **fixes the photon congruence**",
   "**whether a MASSIVE trajectory carries a phase** \u2014 the null ones are $K$'s fixed set"),
}

# ** THE LEADS -- everything noticed that could inform a vein.  (id, what, veins it informs,
# GROUNDED 0-3: how solid the footing is, INFORMS 0-3: how much a vein would learn). **
# ** A lead with NO vein links is instrument work.  It is not counted as progress on the map. **
LEADS = {
 'L-174': ("\u2714 **\u24f5 CLOSED AT LINEAR ORDER r2514**: data with $\\sigma^{TT}\\ne0$ on the de Sitter "
   "leaf evolves by ordinary GR in closed form, with the momentum constraint **conserved** and the count of "
   "**two** arriving from the evolution. **What remains: does the NONLINEAR evolution keep "
   "$\\sigma^{TT}$ free?** \u2014 where the $\\sigma^2$ back-reaction first appears, and it is second order "
   "so it is invisible in the linear exhibition",
   ['L-165','L-175'], 3, 3),
 'L-207': ("\u24f6 the confined/branch-point exhibition \u2014 **gated on PO-6 and must not be opened without "
   "it** (\u24f5 discharged r2450)",
   ['L-165'], 1, 3),
 'L-510': ("**the unworked stratum's free shear is TWO, not five** \u2014 the momentum constraint owns three "
   "under the York split, and **P9 already names the remaining two as the graviton's polarizations**. So the "
   "Killing vectors buy 1-of-2, and the dark interior is **how the transverse 2-plane turns over the leaf**, "
   "not which of a five-dimensional family",
   ['L-165','L-175'], 3, 2),
 'L-511': ("**two objects, one word**: Goldberg--Sachs governs the **optical** shear of a null congruence "
   "(2 real, an invariant); `I3`'s $\\sigma_{ij}$ is the **ADM** shear of a leaf (5 real, foliation-bound). "
   "Schwarzschild is Type D in every slicing while its leaf shear is $0$ on static slices and $3M/r^3$ on "
   "Painlev\u00e9--Gullstrand ones \u2014 and the whole difference is longitudinal, so **both r2505 and "
   "`L-510` stand and neither answers the other**",
   ['L-165','L-175'], 3, 2),
 'L-513': ("**the admissible band**: `sec:what-crosses` FORCES $\\phi\\in\\{0,\\pi\\}$ (what crosses is "
   "frozen, so $\\theta_\\gamma=0$), and across that pair the acoustic phase moves **0.207 against a 0.615 "
   "gap — a third — with the control OUTSIDE it**. So the disagreement is real and bounded, and both "
   "admissible readings sit 76x and 102x the control in $\\chi^2$/dof",
   ['L-202'], 3, 3),
 # ** L-171 REWRITTEN r2512+c54.200 BY THE FORK.  The row it replaces asked for an experiment ALREADY
 # ** RUN (the production-depth seam-phase scan, `L-508`) and named a quantity that scan then bounded.
 # ** It sat high on a board an unattended node works top-down, so a stale premise sends the next node
 # ** to finished work.  Disclosed in FOR_56; reverse freely.
 'L-171': ("**PO-7** \u2014 whether the acoustic disagreement is real against the sky. \u26ed *Sharpened "
   "at c54.200 (`L-513`): over the phases `sec:what-crosses` ADMITS, the acoustic phase moves **0.207 "
   "against a 0.615 gap \u2014 a third \u2014 with the control OUTSIDE it**, so the disagreement is real "
   "and bounded rather than a free choice.* \u21d2 **What is open is the confrontation itself: both "
   "admissible readings sit 76x and 102x the control, so something other than the seam phase carries the "
   "bulk of it \u2014 and the SPACING, robust to 1.9%, is what does not move**",
   ['L-202'], 2, 3),
 'L-204': ("R-P stations \u2462\u2463 \u2014 P8/P9, GR field equations and the exact-solution catalogue",
   ['L-165','L-175'], 3, 2),
 'L-217': ("the CR/Higgs relation is stated; **`F1` stays live \u2014 the relation breaks if the gauge group is "
   "ever promoted to forced**", ['L-221'], 2, 2),
 'L-230': ("the `COMPUTES:` convention \u2014 uptake **flat at 40 of 357** while the corpus grew a sixth; a "
   "receipt that declares what it computed is a receipt a vein can be excavated through", ['L-165','L-221'], 3, 1),
 'L-210': ("the entry-point front \u2014 all 44 sites carry verdicts; **live leads are where a paper's own text "
   "points at an unexplored interior**", ['L-202','L-221','L-175'], 2, 2),
 'L-508': ("**what the seam datum CARRIES, measured**: across four production-depth seam phases the acoustic "
   "phase spans 0.891 in $\\phi/\\pi$ and the peak heights 0.483\u20131.618, **the control's values inside both** "
   "\u2014 a bounded negative that charts the vein's perimeter (\u00a7IV) rather than closing anything",
   ['L-202'], 3, 2),
 'L-509': ("P15 asserted a horizon property of the **branch point** at six sites where its own receipts say "
   "**seam**/**onset**, and the two invert \u2014 repaired; **and `check_loci`, built for exactly this defect, "
   "could not see the worst of them until this revision** (a proposition's receipt binding lives in its argument "
   "paragraph). Found by seeding, not by reading",
   ['L-202'], 3, 1),
 'L-514': ("**nothing in the tree reads UPWARD**: c54.195's withdrawal contradicted text two paragraphs "
   "above it in the same section, which had carried the right answer since c54.191. A withdrawal is the edit "
   "for which that matters most. Second instance of the class after the c54.182/c54.184 duplicate",
   [], 2, 0),
 'L-512': ("`check_receipt_prefixes` \u2014 the receipt-prefix namespace collided twice in two revisions and "
   "reached `main`; bands proposed in the register's own order (56 1-49, 54 50-79, cc54 80-99), **grandfathered "
   "so nothing has to move**. Fails on a duplicate, only REPORTS out-of-band", [], 3, 0),
 'L-218': ("\u24f5 the reader-package formats via pandoc in CI", [], 3, 0),
 'L-228': ("`check_loci` extended to the possessive and compound-noun forms node 52 declined to claim", [], 3, 0),
}


def score(k):
    _, veins, grounded, informs = LEADS[k]
    # ** grounded x informs, with an unlinked lead scored ZERO on the map: it is instrument work. **
    return (grounded * informs, len(veins), grounded)


ORDER = None



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
        # ** 'APPLIED' added r2501+c54.197.  FOR_54's OWN frontmatter says "items are dropped from
        # ** this file the revision they are applied" -- so APPLIED is the word the file's rule uses,
        # ** and it was the one word this parser did not know.  Item 21 was applied at c54.197 and
        # ** kept reporting as LIVE. **
        elif any(k in pre for k in ('DISCHARGED', 'WITHDRAWN', 'ANSWERED', 'APPLIED')):
            done.append(n)
        else:
            live.append((n, ti))
    return live, ans, done


def build():
    rows = live_rows()
    known = set(VEINS) | set(LEADS)
    unsorted = [r for r in rows if r not in known]
    L = ['---', 'name: board', 'kind: STATE',
         'description: THE BOARD \u2014 the veins held open, and every lead ordered against them. GENERATED by '
         'scripts/regen_board.py. Read THE_METHOD.md first.',
         'sources: [chat]', 'current: r2500+c54.194', '---', '',
         '# THE BOARD', '',
         '> ***Read `THE_METHOD.md` first.*** *The short form: **the VEINS are areas held open to be known inside '
         'and out — never crossed out. The LEADS are everything noticed that could inform one.** Work the top lead, '
         'gather what it turns up, re-order, repeat.*',
         '>',
         f'> *{len(rows)} live rows: **{len([r for r in rows if r in VEINS])} veins**, '
         f'**{len([r for r in rows if r in LEADS])} leads**. {struck_count()} struck.*', '']

    # ---- the veins
    L.append('# I \u00b7 THE VEINS \u2014 held open, to be known inside and out')
    L.append('')
    L.append('> \u26d4 ***A vein is not protected because it is fragile. It is protected because collapsing it '
             'would destroy the only thing that tells you which specific questions are worth asking.*** *It closes '
             'FROM WITHIN, when its interior is completely known — never from outside by a verdict.*')
    L.append('')
    for k in sorted(VEINS):
        if k not in rows:
            continue
        name, mapped, dark = VEINS[k]
        n_leads = sum(1 for x in LEADS if k in LEADS[x][1] and x in rows)
        L.append(f'## `{k}` \u00b7 {name}')
        L.append('')
        L.append(f'- **MAPPED** \u2014 {mapped}')
        L.append(f'- \u26d4 **DARK** \u2014 {dark}')
        L.append(f'- *{n_leads} live lead(s) inform this vein*')
        L.append('')

    # ---- the leads, ordered
    live_leads = [k for k in LEADS if k in rows]
    live_leads.sort(key=score, reverse=True)
    L.append('# II \u00b7 THE LEADS \u2014 ordered by how grounded and how informative')
    L.append('')
    L.append('> *Order is **re-computed every time this file is generated**, because a landed lead changes what the '
             'next one is worth.* \u26a0 ***A lead informing NO vein is instrument work. It is listed last and '
             'scores zero on the map — real work, but not progress on the excavation.***')
    L.append('')
    L.append('| # | row | informs | grounded | informs-how-much | what |')
    L.append('|---|---|---|---|---|---|')
    for n, k in enumerate(live_leads, 1):
        what, veins, g, inf = LEADS[k]
        vs = ' '.join(f'`{v}`' for v in veins) if veins else '*\u2014 instrument work*'
        L.append(f'| **{n}** | **`{k}`** | {vs} | {g}/3 | {inf}/3 | {what} |')
    L.append('')
    if live_leads:
        top = live_leads[0]
        L.append(f'> \u26ed\u26ed **TAKE `{top}` NEXT** \u2014 *highest grounded\u00d7informative, and it informs '
                 f'{len(LEADS[top][1])} vein(s).*')
        L.append('')

    # ---- the routed list
    rl, ra, rd = routed()
    L.append('# III \u00b7 THE ROUTED LIST (`FOR_54.md`) \u2014 leads handed to the working fork')
    L.append('')
    # ** DERIVED r2501+c54.197, previously HARDCODED as "21 is flagged to take first". **  Item 21
    # ** was applied at c54.197 and this line went on naming it as the standing edge -- a generated
    # ** file asserting a stale fact in its own summary, which is the class the whole board exists
    # ** to stop.  Now it reads the flag out of FOR_54 and says so when there is none.
    _first = [(n, ti) for n, ti in rl if 'TAKE THIS ONE FIRST' in ti.upper()]
    if _first:
        L.append(f'- ***{len(rl)} live for the fork***, of which **{_first[0][0]} is flagged to take '
                 f'first** \u2014 {_first[0][1]}')
    else:
        L.append(f'- ***{len(rl)} live for the fork***, and \u26a0 ***none is currently flagged '
                 '"take this one first"*** \u2014 the standing edge is whatever the LEADS table above ranks')
    L.append(f'- *{len(ra)} are ANSWERS to the fork rather than work for it* \u2014 {", ".join(ra)}')
    L.append(f'- *{len(rd)} closed* \u2014 {", ".join(rd)}')
    L.append('')
    for n, ti in rl:
        L.append(f'  - **{n}** \u00b7 {ti}')
    L.append('')
    if unsorted:
        L.append('# \u26a0 UNSORTED \u2014 rows nobody has decided about')
        L.append('')
        for r in unsorted:
            L.append(f'- **`{r}`** \u2014 ***is this a vein, a lead, or done? Decide or strike it.***')
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
    unsorted_n = sum(1 for r in rows if r not in (set(VEINS) | set(LEADS)))
    print(f'  BOARD.md written: {len([r for r in rows if r in VEINS])} veins, '
          f'{len([r for r in rows if r in LEADS])} leads, {unsorted_n} UNSORTED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
