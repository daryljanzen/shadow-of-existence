#!/usr/bin/env python3
"""
L-152w — `H·1`, THE CORPUS-WIDE FIGURE SWEEP.  THE SWEEP IS MINE TO RUN; THE FIGURES ARE NOT MINE TO
MAKE, AND THE ITEM SAYS SO IN ITS OWN TEXT.

`H·1`: *"a systematic pass over all fourteen papers for where a NEW figure would earn its place --
for completeness, for visualisability, and (the non-cosmetic reason) because a figure can surface
structure the prose alone hides."*  And, in the same item: ** *"New conceptual figures are Daryl's to
call/supply, not gate-generated (the r548 discipline)."* **

** SO THE DELIVERABLE IS THE PASS AND A RANKED CANDIDATE LIST WITH THE REASON EACH IS NON-COSMETIC --
not figures.  A node that answered this item by drawing things would be violating the item. **

  PART 1  The inventory: which papers carry figures and which carry none.
  PART 2  ** THE SIGNAL: where prose is doing a figure's job, measured rather than felt. **
  PART 3  ** THE RANKED CANDIDATES, each with what the figure would SHOW that the prose hides. **
  PART 4  What `L-152` becomes.

Run: python3 L152w_the_figure_sweep.py
"""
import glob
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')

PAPERS = sorted(p for p in glob.glob(os.path.join(CORPUS, '*.tex'))
                if not os.path.basename(p).startswith('appendix_receipts'))


def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    return t.split(r'\begin{thebibliography}')[0]


# =====================================================================
print("=" * 78)
print("PART 1 — THE INVENTORY")
print("=" * 78)
inv = {}
for p in PAPERS:
    t = body(p)
    inv[os.path.basename(p)[:-4]] = (len(re.findall(r'\\begin\{figure\}', t)), len(t))
print(f"  {'paper':>26} {'figures':>8} {'kchars':>8} {'chars per figure':>18}")
for name, (nf, n) in sorted(inv.items(), key=lambda kv: (kv[1][0], -kv[1][1])):
    per = '--' if nf == 0 else f'{n//nf//1000}k'
    print(f"  {name:>26} {nf:>8} {n//1000:>8} {per:>18}")
unfig = [n for n, (nf, _) in inv.items() if nf == 0]
print()
print(f"  ** {len(unfig)} of {len(inv)} papers carry NO figure at all: {', '.join(sorted(unfig))} **")
assert len(unfig) >= 8
print()
for s in [
 "⌗ ** THE INVENTORY IS NOT ITSELF AN ARGUMENT.  A paper with no figure may not need one -- a",
 "   classification result or an algebraic derivation often reads better without. **  *What the",
 "   column does is tell the sweep where to look; the reason has to come from the prose.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SIGNAL: WHERE PROSE IS DOING A FIGURE'S JOB")
print("=" * 78)
# Three measurable signals, each a different reason a figure earns its place.
SIG = {
 # (a) the paper asks the reader to HOLD A CONFIGURATION: positions, angles, adjacency
 'configuration': r'(azimuth|antipodal|\b120\^?\\?circ|\bat 60|equidistant|adjacent to|opposite the'
                  r'|lies (?:at|on|between)|the three [a-z]+ (?:at|sit|lie)|vertices|hexagon'
                  r'|equilateral|the twelve|three-fold|\bcrest\b)',
 # (b) the paper narrates a PATH OR SEQUENCE: something moves through stages
 'trajectory':    r'(turnaround|re-?expan|the (?:in|out)ward leg|traverses|crosses (?:the|from)'
                  r'|runs from .{0,30} to|approaches the|down the .{0,20} branch|lap|winding)',
 # (c) the paper SAYS the reader should picture it
 'deixis':        r'(picture|visuali[sz]|as drawn|read off the|one can see|the reader (?:may|can)'
                  r'|schematically|sketch)',
}
score = {}
for p in PAPERS:
    name = os.path.basename(p)[:-4]
    t = body(p)
    per_k = {k: 1000.0*len(re.findall(v, t, re.I))/max(1, len(t)) for k, v in SIG.items()}
    score[name] = per_k
print(f"  density per 1000 characters (a paper's own prose, comments and bibliography removed)")
print(f"  {'paper':>26} {'figs':>5} {'config':>8} {'traject':>8} {'deixis':>7} {'sum':>7}")
ranked = sorted(score, key=lambda n: -sum(score[n].values()))
for name in ranked:
    d = score[name]
    print(f"  {name:>26} {inv[name][0]:>5} {d['configuration']:>8.2f} {d['trajectory']:>8.2f}"
          f" {d['deixis']:>7.2f} {sum(d.values()):>7.2f}")
print()
for s in [
 "⌗ ** THE COLUMN THAT MATTERS IS `figs` AGAINST `sum`: a paper high in the configuration and",
 "   trajectory signals and at zero figures is asking its reader to build a picture from sentences",
 "   -- which is the item's own non-cosmetic reason, stated as a measurement. **",
 "",
 "⚠ *And the signal is a POINTER, not a verdict.  `deixis` in particular flags papers that already",
 "tell the reader to picture something; whether the picture is worth drawing is a judgement the",
 "sweep is not entitled to make.*",
]:
    print("  " + s)

print()
print("  ── THE TWO AXES READ SEPARATELY, because they are different reasons ──")
print()
print("  (a) CONFIGURATION -- 'hold this arrangement in your head', the axis a diagram is FOR:")
for name in sorted(score, key=lambda n: -score[n]['configuration'])[:5]:
    nf, n = inv[name]
    per = 'never' if nf == 0 else f'{n//nf//1000}k chars/fig'
    print(f"        {name:>26} {score[name]['configuration']:>6.2f}   figures: {nf}  ({per})")
print()
print("  (b) TRAJECTORY -- 'something moves through stages', the axis a PLOT is for:")
for name in sorted(score, key=lambda n: -score[n]['trajectory'])[:5]:
    nf, n = inv[name]
    per = 'never' if nf == 0 else f'{n//nf//1000}k chars/fig'
    print(f"        {name:>26} {score[name]['trajectory']:>6.2f}   figures: {nf}  ({per})")
print()
for s in [
 "⌗⌗ ** AND THE TWO AXES DISAGREE, WHICH IS THE USEFUL PART. **",
 "   *On the raw SUM the strongest un-figured paper is `slicing_operator`; on CONFIGURATION alone it",
 "   is `matter_sector_paper`, which is third in the corpus on that axis and dead last on figure",
 "   density -- **one figure in 113k characters, the worst ratio anywhere here**.*",
 "   ** So the sum ranks papers that NARRATE and the configuration column ranks papers that ASK THE",
 "   READER TO ASSEMBLE something -- and only the second is a job prose is bad at. **  *A narrated",
 "   trajectory can be followed sentence by sentence; a configuration cannot.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RANKED CANDIDATES")
print("=" * 78)
CAND = [
 ("P14 `matter_sector_paper`", "the equatorial section's transverse geometry: three hinges at "
  "120 degrees, three walls antipodal to them, twelve null legs",
  "THE CORPUS'S MOST CONFIGURATIONAL OBJECT AND IT IS CARRIED ENTIRELY IN SENTENCES.  Hinges at "
  "transverse radius 2 alpha and azimuths 0/120/240, walls at 60/180/300 each antipodal to its "
  "hinge, twelve null legs as three graze points times four -- a reader who mis-assembles this "
  "mis-reads the whole sector, and the paper's ONE figure is elsewhere."),
 ("P14 `matter_sector_paper`", "the A_2 weight plane: three signed areal radii as the weight "
  "system of the fundamental",
  "The three r_j are linear forms of rank two, 120 degrees apart, summing to zero -- and the "
  "claim that the Z_3-fixed centre is the weight ORIGIN, with no zero weight in the 3, is a "
  "statement about a picture.  It is the sector's central identification and it is unillustrated."),
 ("P9 `range_paper`", "the wall: the onset of free gravitational radiation",
  "ALREADY FLAGGED in the item.  P9 is the range of the slicing operator and the wall is where the "
  "range ENDS; the paper carries the boundary in prose and the reader has no picture of what is "
  "inside it.  A figure would show the reachable sector and its edge as one object."),
 ("P8 `slicing_operator`", "the trichotomy: closed, flat and open leaves as one congruence at "
  "three energies",
  "Three constant-curvature leaves from one SdS congruence via -k = E^2 - 1.  A single diagram "
  "carries what the proposition states three times."),
 ("P11 `dynamics_paper`", "the two walls, now that they are named apart",
  "c54.94 renamed prop:wall to prop:radiative-wall precisely because TWO different walls wore one "
  "label.  A figure placing the wall of inhomogeneity against the throat wall would make the "
  "distinction structural rather than nomenclatural -- and the collision that forced the rename is "
  "the evidence that prose alone did not carry it."),
 ("P10 `canonical_time`", "the Euclidean segment: imaginary time between the legs",
  "The segment where Re tau does not advance is the corpus's most counter-intuitive object and the "
  "one most often mis-stated by working nodes.  P13's Plate does part of this job for a different "
  "paper."),
 ("P12 `algebroid_paper`", "the orbit-type stratification",
  "A stratification is a picture of which strata bound which.  P12 carries it as a list."),
 ("P5 `groupoid_paper`", "the sigma-pairing of vantages, with Nariai as the unique fixed point",
  "The paper's own argument is that generic vantages fall into sigma-pairs while the Nariai member "
  "is the lone fixed point in a degenerate orbit.  That is an orbit diagram."),
]
print("  Ordered by the CONFIGURATION axis first -- the job prose is bad at -- and by the item's\n  own flag second.")
print()
print(f"  {'paper':>28} {'candidate':>62}")
for i, (paper, what, _why) in enumerate(CAND, 1):
    print(f"  {i}. {paper:>25} {what:>62}")
print()
for i, (paper, what, why) in enumerate(CAND, 1):
    print(f"  ── {i}. {paper} — {what}")
    for line in re.findall(r'.{1,88}(?:\s|$)', why):
        print(f"       {line.strip()}")
    print()

# =====================================================================
print("=" * 78)
print("PART 4 — WHAT `L-152` BECOMES")
print("=" * 78)
for s in [
 "⇒ ** THE PASS IS DONE AND IT IS THE WHOLE OF WHAT THIS ITEM MAY DELIVER FROM THIS SIDE. **",
 "   *The item reserves the figures themselves: 'New conceptual figures are Daryl's to call/supply,",
 "   not gate-generated (the r548 discipline).'  A node that answered `H·1` by drawing eight figures",
 "   would be violating the item while appearing to discharge it.*",
 "",
 "⌗ ** WHAT THE SWEEP ADDS BEYOND THE ITEM'S OWN ONE FLAGGED CANDIDATE (P9's wall): seven more, and",
 "   the top two are in P14 -- the corpus's most configurational sector, carried in sentences, with",
 "   its single figure elsewhere. **",
 "",
 "⚠ ** AND ONE CANDIDATE IS EVIDENCED RATHER THAN ARGUED: P11's two walls. **  *The label collision",
 "   `check_compile` caught at c54.94 -- two different propositions named `prop:wall` in two papers,",
 "   one the wall of INHOMOGENEITY and one the THROAT wall -- is direct evidence that prose alone",
 "   did not keep them apart, in a corpus that had every reason to.*",
]:
    print("  " + s)
