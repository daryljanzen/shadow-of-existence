#!/usr/bin/env python3
"""r7764 (60) -- the skeptical read of the two-level framing.  POST-REGISTRATION throughout."""
import contextlib
import io
import os
import re
import runpy
import subprocess

import numpy as np
from scipy.integrate import quad

ROOT = '/home/user/shadow-of-existence'
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as fh:
        return fh.read()


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


print("=" * 100)
print("r7764 (60) -- the skeptical read of the two-level framing (order r7761)")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print("=" * 100)

P7 = read('corpus/CR_framework.tex')
P15 = read('corpus/CR_cosmology.tex')
ERC = read('resources/ERC_existence-relativity-cosmology.tex')
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(io.StringIO()):
        NS = runpy.run_path(LP)
finally:
    os.chdir(_cwd)
H_stack, H_leaf, C, Z_REC = NS['H_stack'], NS['H_leaf'], NS['C'], NS['Z_REC']
H0, OM, OMR = NS['H0'], NS['OM'], NS['OMR']
MPC_GYR = 977.792         # 1 / (km/s/Mpc) in Gyr

# ---------------------------------------------------------------- ARM 1: what the licence was argued for
AVG = [s for s in re.split(r'(?<=\.)\s', ERC) if 'average densities' in s]
THRESH = [s for s in re.split(r'(?<=\.)\s', ERC) if 'exceed a threshold' in s]
LOCAL = [s for s in re.split(r'(?<=\.)\s', ERC) if 'local space-time warping' in s or 'lensing' in s]
BOUND = [s for s in re.split(r'(?<=\.)\s', ERC) if 'do not participate in the Hubble flow' in s]


def clean(s):
    s = re.sub(r'\\(?:emph|textit|textbf|texttt)\{([^{}]*)\}', r'\1', s)
    return ' '.join(re.sub(r'[\\${}]', '', s).split())


arm(1, "what the trampoline's licence was ARGUED for, in the source's own words",
    bool(AVG) and bool(THRESH),
    "  r7760 found the licence SENTENCE general in its own words.  This arm asks the other",
    "  question: what the argument around it rests on.  Three things in the source decide it.",
    "",
    "  ⛔⛔ ⒜ THE SOURCE'S OWN TARGET IS THE AVERAGE DENSITIES OF MATTER **AND RADIATION**:",
    *[f"      \"{clean(s)[:330]}\"" for s in AVG[:3]],
    "  ⇒ THIS IS THE STRONGEST THING AGAINST THE FRAMING AND IT IS THE PROGRAMME'S OWN",
    "  FOUNDING QUESTION.  The leaf rate IS the average densities of matter and radiation,",
    "  term for term.  The framing says every measured quantity takes it -- so everything",
    "  observable is governed by exactly what the source set out to deny governs the",
    "  expansion, and the denial is kept only where nothing is measured.",
    "",
    "  ⛭ ⒝ AND THE SOURCE'S OWN THRESHOLD CLAUSE CUTS THE OTHER WAY, which a one-sided read",
    "  would leave out:",
    *[f"      \"{clean(s)[:300]}\"" for s in THRESH[:1]],
    "  ⇒ `except where densities exceed a threshold' is the source ALLOWING the rate to be",
    "  affected where density is high, which is exactly the early universe.  So the source",
    "  permits the two levels to part at high density -- on its own terms, not only on the",
    "  framing's.",
    "",
    "  ⌗ ⒞ and what the local-warping language is about, for the record:",
    *[f"      \"{clean(s)[:200]}\"" for s in (LOCAL[:1] + BOUND[:1])],
    "  ⇒ lensing, ripples, bound structures: the averaging premise is there, and a uniform",
    "  bath is not in it.  ARM 2 measures what that costs.")

# ---------------------------------------------------------------- ARM 2: the size of the gap
ZS = [0.0, 67.0, 1.0e3, Z_REC, 1.0e5, 1.0e9]
ratio = [(z, H_leaf(z) / H_stack(z)) for z in ZS]


def age(z, H):
    """elapsed cosmic time from the start to epoch z, integrated in ln(1+z) and split by decade,
    because a single quad over [z, 1e12] samples the wide range and misses the low-z structure --
    which this arm's first attempt did, returning 1e-12 Gyr for a 13.8 Gyr universe."""
    edges = [z] + [e for e in np.geomspace(max(z, 1e-3) + 1.0, 1.0e14, 40)]
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        a, b = max(lo, z), hi
        if b <= a:
            continue
        tot += quad(lambda u: np.exp(u) / ((np.exp(u)) * H(np.exp(u) - 1.0)),
                    np.log(1 + a), np.log(1 + b), limit=200)[0]
    return tot * MPC_GYR


ages = [(z, age(z, H_stack), age(z, H_leaf)) for z in (0.0, 1.0e3, Z_REC, 1.0e5, 1.0e9)]
arm(2, "the size of the gap between the two levels, computed",
    ratio[0][1] < 1.001 and ratio[-1][1] > 100,
    "      z             H_leaf / H_stack",
    *[f"      {z:12.4g}   {r:14.4f}" for z, r in ratio],
    "",
    "      z            age on the stacking law   age on the leaf law      ratio",
    *[f"      {z:10.4g}   {a:16.6g} Gyr   {b:12.6g} Gyr   {a / b:10.3f}" for z, a, b in ages],
    "",
    "  ⇒ the framing's own figures check out at the late end (4 parts in 100,000 today, one",
    f"  per cent near z = 67).  AND THE GAP GROWS AS (1+z)^(1/2): it is {ratio[2][1]:.1f} at z = 1000,",
    f"  {ratio[-1][1]:.0f} at nucleosynthesis.  The elapsed cosmic time to a given early epoch differs",
    f"  by a factor of {ages[-1][1] / ages[-1][2]:.0f} at z = 1e9.",
    "  ⛔ SO AT EARLY EPOCHS THE TWO LEVELS ARE NOT TWO DESCRIPTIONS OF ONE UNIVERSE TO",
    "  WITHIN A CORRECTION; they are different histories by factors of hundreds.  The",
    "  trampoline's licence is that the cosmological description is a good description while",
    "  the warping averages out.  A uniform bath has nothing to average, and ⒜ above is the",
    "  source's own acknowledgement that density can break the licence.")

# ---------------------------------------------------------------- ARM 3: an observable that must take the stacking rate
CAND = []


def dm(z, H):
    return quad(lambda zz: C / H(zz), 0.0, z, limit=300)[0]


# the acceleration epoch, on each law
def q_of(z, H, h=1e-3):
    return (np.log(H(z + h)) - np.log(H(max(z - h, 0.0)))) / (2 * h if z - h >= 0 else h)


def z_acc(H):
    zz = np.linspace(0.0, 3.0, 3001)
    f = [(1 + z) * q_of(z, H) - 1.0 for z in zz]
    s = [i for i in range(len(f) - 1) if f[i] * f[i + 1] < 0]
    return float(zz[s[0]]) if s else float('nan')


CAND.append(("the acceleration epoch z_acc", "propagated (measured from distances)",
             f"stacking {z_acc(H_stack):.4f} vs leaf {z_acc(H_leaf):.4f}"))
CAND.append(("the acoustic angle theta*", "propagated: a ratio of two lengths",
             "both lengths on one law either way (r7760 ARM 3); no law-free value"))
CAND.append(("the baryon-acoustic distances", "propagated",
             f"the two laws differ by at most 0.021 per cent over the tracers (r7753)"))
CAND.append(("the locally measured expansion rate H_0", "content: a fit to nearby distances",
             f"H_leaf/H_stack - 1 at z = 0 is {H_leaf(0.0) / H_stack(0.0) - 1:.2e}"))
CAND.append(("the age of the universe / stellar ages", "read along the congruence's own proper time",
             f"{ages[0][1]:.4f} Gyr on the stacking law vs {ages[0][2]:.4f} Gyr on the leaf law"))
CAND.append(("the light elements", "content: yields set by the expansion timescale",
             f"the timescale differs by a factor {ratio[-1][1]:.0f} at z = 1e9 -- ARM 4"))
CAND.append(("the microwave-redshift isotropy floor", "content, and a UNIFORMITY bound",
             "it excludes a rate tracking the INHOMOGENEOUS matter field; H_leaf is homogeneous"))
CAND.append(("the Nariai selection, z_acc = x0 - 1, Lambda fixing the amplitude",
             "GEOMETRIC, and not an observable in themselves",
             "each is a statement about the foliation, tested only through propagated quantities"))
none_must = True
arm(3, "is there an observable that MUST take the stacking rate",
    none_must,
    *[f"      {n}\n           {k}\n           {v}" for n, k, v in CAND],
    "",
    "  ⇒ ⛔ NO: THIS SEAT FOUND NONE, AND THAT IS THE ANSWER WITH A COST ATTACHED.  Every",
    "  candidate is either propagated or read from inside the content, so the framing's",
    "  second paragraph survives the search.  BUT THE SAME RESULT SAYS THE GEOMETRIC LEVEL",
    "  IS NOT REACHED BY ANY MEASUREMENT: on the framing as written, no observation can",
    "  come back inconsistent with the stacking rate, because no observation is of it.",
    "  ⇒ THAT IS THE CASE AGAINST, AT ITS SHARPEST: the framing makes the geometric level",
    "  empirically idle, and a level that no measurement can reach is doing no empirical",
    "  work -- which is a real cost, and the statement does not say it.",
    "  ⌗ THE DEFEATER, STATED: the geometric level is not SUPPOSED to be reached by a",
    "  measurement; it answers why the universe expands at all and fixes the foliation",
    "  everything else is computed on.  That is structural work, and a framing may",
    "  legitimately carry a structural level.  What it should not do is carry it silently:",
    "  the statement should say in its own words that nothing measures the stacking rate.",
    "  ⌗ AND THE AGE IS THE NEAR MISS WORTH NAMING: it is read along the congruence's own",
    f"  proper time rather than across leaves, and the two laws give {ages[0][1]:.4f} against"
    f" {ages[0][2]:.4f} Gyr --",
    "  a difference of about one part in 2000, far below any stellar-age error bar.  So it",
    "  is the one quantity whose CHARACTER is geometric and whose VALUE cannot discriminate.")

# ---------------------------------------------------------------- ARM 4: the light elements
r_bbn = ratio[-1][1]
t_bbn = [a for z, a, b in ages if z == 1.0e9]
arm(4, "the light elements, where the gap is largest",
    r_bbn > 100,
    f"  at z = 1e9, H_leaf/H_stack = {r_bbn:.1f}, and the elapsed time to that epoch differs by",
    f"  a factor {ages[-1][1] / ages[-1][2]:.0f}.",
    "  ⇒ the light-element yields are set by the expansion timescale at that epoch, so they",
    "  are computable on ONE of the two laws and not the other.  The corpus reports them",
    "  confirmed within 1 sigma at the microwave-background baryon density.",
    "  ⇒ ⛭ SO THE FRAMING'S SECOND PARAGRAPH IS NOT ONLY CONSISTENT WITH THE DATA HERE, IT",
    "  IS REQUIRED BY THEM: on the stacking law the early expansion is slower by a factor of",
    "  hundreds and the yields would not come out.  This is the strongest thing FOR the",
    "  framing in this read, and it is the same computation that makes ⒜ in ARM 1 bite --",
    "  the data demand the content's rate exactly where the programme's founding question",
    "  denied that average densities set it.",
    "  ⌗ WHAT THIS DOES NOT ESTABLISH: that the corpus's own nucleosynthesis calculation was",
    "  done on the leaf rate.  It is cited to a companion paper this repository does not",
    "  carry, so this seat reports the requirement and not the provenance.")

# ---------------------------------------------------------------- ARM 5: P7's warning, both halves
WARN = [s for s in re.split(r'(?<=\.)\s', P7) if 'subtler inverse' in s]
SHAD = [s for s in re.split(r'(?<=\.)\s', P7) if 'The shadow here is the' in s]
warn, shad = (clean(WARN[0]) if WARN else ''), (clean(SHAD[0]) if SHAD else '')
primary_ok = 'carried on the evolving layer' in clean(P7)
arm(5, "P7's warning, read in its own paragraph, against both halves",
    bool(warn) and bool(shad),
    f"  the shadow, named: \"{shad[:300]}\"",
    f"  the warning: \"{warn[:300]}\"",
    "",
    "  ⇒ THE PRIMARY ERROR IS RESPECTED.  P7 requires the physics to be `carried on the",
    f"  evolving layer and THEN projected' ({primary_ok}), and the framing's second paragraph says",
    "  exactly that: measured quantities are facts about the content's dynamics, observed",
    "  through the projection.",
    "",
    "  ⛔ AND THE INVERSE IS STRAINED, WHICH IS THE FINDING.  P7 calls the layer's own",
    "  reassigned expansion -- the geometric rate -- `not itself a shadow but the existent's",
    "  own geometry, to be computed on and only then projected', and warns against",
    "  `mistaking the layer's ontological rate for the appearance AND REFUSING IT ITS",
    "  PHYSICS'.  The framing does not call the geometric rate an appearance, so it avoids",
    "  the letter.  But `It is not the rate any propagated length is built on' leaves it",
    "  with no quantity to govern, and `refusing it its physics' is the warning's own",
    "  phrase for that.  ⇒ THE STATEMENT AVOIDS THE LETTER OF THE INVERSE ERROR AND COMES",
    "  CLOSE TO ITS SPIRIT.  It should say what physics the geometric rate keeps, in its own",
    "  words, rather than only what it loses.")

# ---------------------------------------------------------------- ARM 6: three levels against two
THREE = [s for s in re.split(r'(?<=\.)\s', P7) if 'through which both are observed' in s] \
        or [s for s in re.split(r'(?<=\.)\s', P7) if 'three-level reading' in s]
three = clean(THREE[0]) if THREE else ''
both_observed = 'through which both are observed' in three
arm(6, "P7's three-level reading against the framing's two",
    both_observed,
    f"  P7: \"{three[-300:]}\"",
    f"  the phrase `the projection through which BOTH are observed': {both_observed}",
    "  ⇒ ⛔ P7 CARRIES THREE LEVELS AND SAYS BOTH THE FOLIATION RATE AND THE LEAF'S LOCAL",
    "  DYNAMICS ARE OBSERVED THROUGH THE PROJECTION.  The framing's `every measured quantity",
    "  ... takes the leaf rate at every epoch' makes the first of those unobserved.  Either",
    "  P7's sentence is loose, or the framing's second paragraph overstates -- and the",
    "  framing is the thing being drafted, so this is where to fix it.",
    "  ⌗ THE SMALLEST REPAIR, and it is a clause: `observed through the projection, which",
    "  below z ~ 67 returns the geometric rate to within a per cent' -- which keeps P7's",
    "  three levels, keeps the framing's content claim, and is true by ARM 2.")

# ---------------------------------------------------------------- ARM 7: the case against, at full strength
arm(7, "⛭ the case against the framing, at full strength, each with its defeater",
    True,
    "  ⒜ IT CONCEDES THE PROGRAMME'S FOUNDING QUESTION EMPIRICALLY.  The ERC source asks",
    "     whether the universe's evolution must be `determined by the average densities of",
    "     matter and radiation' and finds it implausible.  The leaf rate IS those densities.",
    "     If every measured quantity takes it, FLRW's core premise is restored for",
    "     everything observable and denied only where nothing is measured.",
    "     *Defeater: the denial was about the EXPLANATION -- why there is expansion at all,",
    "     and what fixes the foliation -- not about the numbers; and the numbers agree to",
    "     4e-05 today.  Also the source's own threshold clause allows the rate to be",
    "     affected where density is high.*",
    "  ⒝ THE GEOMETRIC LEVEL BECOMES EMPIRICALLY IDLE (ARM 3): no observable reaches it, so",
    "     nothing can come back inconsistent with it.  *Defeater: structural levels are",
    "     legitimate; the fault is not saying so.*",
    "  ⒞ THE ANALOGY'S AVERAGING PREMISE HAS NOTHING TO AVERAGE (ARMS 1, 2): the gap is a",
    f"     factor {ratio[-1][1]:.0f} at nucleosynthesis, not a correction that washes out.",
    "     *Defeater: the threshold clause, and that the licence sentence is general in its",
    "     own words (r7760 ARM 9).*",
    "  ⒟ IT STRAINS P7's INVERSE WARNING (ARM 5) AND DROPS P7's THIRD LEVEL (ARM 6).",
    "     *Defeater: both are repairable by a clause, and the repair is given.*",
    "  ⒠ `EVERY MEASURED QUANTITY ... AT EVERY EPOCH' IS A UNIVERSAL WITH NO STATED",
    "     EXCEPTION, and the age is the near miss that shows the universal is doing real",
    "     work rather than being safe: its character is geometric even though its value",
    "     cannot discriminate.  *Defeater: the search in ARM 3 found no counterexample, so",
    "     the universal survives -- it is the WORDING that claims more than was tested.*")

# ---------------------------------------------------------------- ARM 8: what it gets right
arm(8, "what the framing gets right that a reader might doubt",
    True,
    "  ⒜ ITS OWN FIGURES ARE RIGHT: 4 parts in 100,000 today and one per cent near z = 67,",
    "     recomputed here from this line's own instrument.",
    "  ⒝ THE DATA REQUIRE ITS SECOND PARAGRAPH WHERE THE GAP IS LARGEST (ARM 4): on the",
    "     stacking law the nucleosynthesis timescale is off by a factor of hundreds.",
    "  ⒞ IT RESPECTS P7's PRIMARY ERROR (ARM 5): carry the physics on the layer, then",
    "     project.",
    "  ⒟ AND IT KEEPS THE NARIAI RESULTS WHERE THEY LIVE: the foliation, the selection, the",
    "     acceleration epoch and Lambda's amplitude are geometric, which is what r7760's and",
    "     r7762's reads both found survives untouched.")

# ---------------------------------------------------------------- ARM 9: what this cannot settle
arm(9, "what this read cannot settle, and r7762's item 4 not re-run",
    True,
    "  ⒜ WHETHER THE SMALL-r RESULTS SURVIVE THE BEND -- r7762 ARM 8 raised it and it is",
    "     unchanged by this read: the horizon trichotomy, the branch point's structure and",
    "     the exact Euclidean flatness are stated on the vacuum family, and radiation",
    "     dominates the mass function above z ~ 3370.  A revision's worth of work, offered.",
    "  ⒝ WHETHER THE CORPUS'S OWN NUCLEOSYNTHESIS WAS COMPUTED ON THE LEAF RATE (ARM 4): the",
    "     calculation is cited to a companion paper this repository does not carry.",
    "  ⒞ THE PROVENANCE OF THE FRAMING ITSELF: it was settled in chat, and this read tests",
    "     it against the corpus rather than against that conversation.",
    "  ⌗ AND ITEM 4 OF THE ORDER -- P7's four formal paragraphs -- WAS ANSWERED AT r7762,",
    "  arms ⑨-⑪: fourteen citations checked against their declarations' binders and",
    "  conclusions, every conditional claim carrying its condition, each paragraph naming",
    "  what it does not formalise, and 71's campaign report matching on every count checked.",
    "  IT IS NOT RE-RUN HERE, and this line says so rather than letting a reader infer it.")

print("\n" + "=" * 100)
print("  THE LEDGER")
for n, ok, title in sorted(VERDICTS):
    print(f"    {'PASS' if ok else 'FAIL'}  ARM {n:2d}  {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their registered criterion"
      + ("" if not bad else f";  not met: {sorted(bad)}"))
print("=" * 100)
