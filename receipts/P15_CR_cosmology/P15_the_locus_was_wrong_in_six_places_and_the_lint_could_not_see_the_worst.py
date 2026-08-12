#!/usr/bin/env python3
"""
RECEIPT -- P15: ** ROUTED ITEM 21 WORKED.  SIX SITES SAID "BRANCH POINT" WHERE THEIR OWN RECEIPTS SAY
"SEAM" OR "ONSET", AND THE TWO LOCI GIVE OPPOSITE ANSWERS -- AT THE SEAM THE COMOVING HORIZON IS AT ITS
MAXIMUM AND THE ACOUSTIC MODES ARE INSIDE IT; AS r -> 0 IT SHRINKS TO ZERO AND EVERY MODE IS OUTSIDE.
SO A PROPOSITION TITLED "SUB-HORIZON" WAS TRUE AT ONE AND FALSE AT THE OTHER. **

** AND THE LINT BUILT TO CATCH EXACTLY THIS COULD NOT SEE THE WORST OF THE SIX.  THAT WAS FOUND BY
SEEDING THE DEFECT, NOT BY READING THE CODE. **

Built r2501+c54.197, front #2, lead `L-509`.  VEIN: `L-202` (what the seam carries) -- and by the
method's §III, all four, since this is a framework a reader could not follow being made followable.

===================================================================================================
** WHAT THE WORD DECIDES **
===================================================================================================

The lap has four named loci (r2155).  Two of them sit at opposite ends of the same rising branch of
the comoving horizon, and P15's perturbation sector turns on which one is meant:

  * the SEAM  r = +alpha/sqrt3 -- where, on the Nariai member, f = f' = 0 forces the comoving horizon
    to its maximum, so that is where the MOST modes are inside it (`C2_horizon_limits` STEP 5);
  * the BRANCH POINT  r = 0 -- where 2M/r -> infinity carries aH up without bound, the comoving
    horizon to zero, and EVERY mode has exited.

** The physics does not merely differ between them.  It inverts. **  PART 1 recomputes that here
rather than taking it from the routed item, because a receipt that trusts its own routing slip is
the shape this whole revision is about.

===================================================================================================
** WHAT WAS FIXED, AND THE ONE SITE THAT MUST SURVIVE ANY SWEEP **
===================================================================================================

  sec:perturbations   subsection heading   "The branch point is sub-horizon for the acoustic modes"
                      -- and the proposition three lines below it is titled "at the plasma's onset",
                      so the paper stated BOTH.  ** A heading contradicting its own proposition is
                      worse than the original error: a reader cannot tell which one to believe. **
  prop:subhorizon     body, closing clause  "inside the horizon at the branch point by a factor >=2"
                      -- while every number in it is evaluated at z_onset ~ 6797 and the receipt it
                      cites (`P15_verify_numeric`, anchor 7) says "onset" and never "branch point".
  sec:coherence       "already sub-horizon at the branch point ... each mode's driving is complete
                      on the collapse side" -- locus wrong, AND the completeness is bounded by
                      `C2_horizon_limits` STEP 6 in a way the sentence did not carry.
  sec:envelope        "the branch point sits on its rising branch, which is WHY the acoustic modes
                      are sub-horizon there" -- ** the site that claims to be the DERIVATION of
                      prop:subhorizon, with the locus backwards, so the derivation read as false. **
  sec:envelope        "all of them reaching the branch point with the same driving amplitude" --
                      `C4_driving_envelope` says "the leg ends at the seam" and says seam 17 times.
                      ** This site is NOT in routed item 21's list; the locus lint found it. **
  header STATUS       "the sub-horizon branch point" listed among the cold-verified results.

  ** AND ONE FLAG IS A FALSE POSITIVE, named by the finder BEFORE the tool was run and confirmed
  here: ** "the branch point is far below their decoupling" (the neutrinos) is a TEMPERATURE
  ordering along the excursion, not a horizon property at a locus.  It is true as written.

===================================================================================================
** THE PART THAT IS NOT ABOUT THE PAPER: A GATE VERIFIED AGAINST A CLEAN TREE MEASURED NOTHING **
===================================================================================================

`corpus/check_loci.py` exists for this exact defect -- its header quotes r2289 on it verbatim: *"the
error INVERTED the physics: sub-horizon at ONSET; super-horizon at the CROSSING."*

** Seeding prop:subhorizon's body back to "at the branch point" left the lint printing "clean" and
exiting 0. **  The binding between a proposition's CLAIM and its RECEIPT is not intra-sentence: the
claim is in the body, the citation is in the argument paragraph below it.  A per-sentence scan sees
an assertion with no receipt (skipped by design) and a citation with no assertion.

  *** So the corpus's most load-bearing claim shape was the one shape the check could not see, and
      the site it could not see was the first one on the routed item's list. ***

PART 3 measures the fix both ways.  ** The first attempt at it used a fixed 1400-character window for
the argument paragraph and STILL missed this site, because P15's clarification paragraphs sit between
the statement and its argument and are longer than the window. **  *A cap chosen by eye is a recall
hole with no error message.*  The shipped version bounds the search structurally instead -- to the
next sectioning command or theorem environment -- and requires the receipt to sit in the argument's
own paragraph.

SETTINGS: no spectra and no instrument knobs -- this file reads the corpus's .tex and .py sources and
recomputes the horizon quantities symbolically/analytically from the metric function alone.  ** The
one number taken from elsewhere is r*/r_seam = 1.5338, and it is RE-DERIVED here rather than cited. **

rc=0 on success.  Run: python3 P15_the_locus_was_wrong_in_six_places_and_the_lint_could_not_see_the_worst.py
                        (numpy sympy; ~5 s)
"""
import os
import re
import subprocess
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

fail = []

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO LOCI INVERT, RE-DERIVED FROM THE METRIC FUNCTION AND NOT CITED")
print("=" * 78)
# Nariai member in the gauge alpha = 1:  M = alpha/(3 sqrt3), so f and f' vanish together
# at the front seam r = +alpha/sqrt3.  The comoving Hubble radius squared is (rH)^-2 with
# (rH)^2 = (1 - f) + A/r^2 = 2M/r + r^2/alpha^2 + A/r^2.
ALPHA = 1.0
MASS = 1.0 / (3.0 * np.sqrt(3.0))
R_SEAM = ALPHA / np.sqrt(3.0)


def rH2(r, A=0.0):
    """(r H)^2 -- the comoving Hubble WAVENUMBER squared.  Large => small comoving horizon."""
    return A / r ** 2 + 2.0 * MASS / r + r ** 2 / ALPHA ** 2


# the corpus's inherited datum: rho_r/rho_m ~ 2 AT the seam  =>  A = 4 M r_seam
A_RAD = 4.0 * MASS * R_SEAM

print(f"  gauge alpha = {ALPHA}, Nariai M = 1/(3 sqrt3) = {MASS:.7f}, seam r = {R_SEAM:.7f}")
print()
print(f"  {'r/alpha':>12s} {'aH (norm.)':>12s} {'1/aH (norm.)':>14s}   what it means")
_ref = np.sqrt(rH2(R_SEAM))
for r, tag in [(R_SEAM, 'THE SEAM'), (0.1 * ALPHA, ''), (1e-3 * ALPHA, 'toward r = 0')]:
    aH = np.sqrt(rH2(r)) / _ref
    print(f"  {r:>12.5f} {aH:>12.3f} {1.0 / aH:>14.3f}   {tag}")
print()
print("  ** THE COMOVING HORIZON 1/aH IS LARGEST AT THE SEAM AND GOES TO ZERO AS r -> 0. **")
print("  *So 'the acoustic modes are inside the horizon' is TRUE at the seam and FALSE at the")
print("   branch point -- the substitution does not blur a claim, it reverses it.*")

_seam_h = 1.0 / np.sqrt(rH2(R_SEAM))
_bp_h = 1.0 / np.sqrt(rH2(1e-3 * ALPHA))
if not _seam_h > 10.0 * _bp_h:
    fail.append(f"the comoving horizon at the seam ({_seam_h:.4f}) is not large against its value "
                f"near r=0 ({_bp_h:.4f}) -- the inversion PART 1 rests on is not there")

# and the maximum sits just OUTSIDE the seam once the leg carries radiation
r_ = sp.symbols('r', positive=True)
_quart = sp.numer(sp.together(sp.diff(A_RAD / r_ ** 2 + 2 * MASS / r_ + r_ ** 2, r_)))
_roots = [complex(x) for x in sp.nroots(sp.Poly(sp.expand(_quart), r_))]
_rstar = min(x.real for x in _roots if abs(x.imag) < 1e-9 and x.real > 0)
print()
print(f"  and with the inherited datum rho_r/rho_m ~ 2 at the seam (A = 4 M r_seam) the maximum of")
print(f"  the comoving horizon moves OUT to r* = {_rstar:.4f} = {_rstar / R_SEAM:.4f} r_seam:")
print(f"  ** the seam sits JUST INSIDE the turning point, on the rising branch -- which is why the")
print(f"     acoustic modes are already inside there, and it is a derivation and not a coincidence.**")
if abs(_rstar / R_SEAM - 1.5338) > 0.002:
    fail.append(f"r*/r_seam re-derives to {_rstar / R_SEAM:.4f}, not C2's 1.5338")
if not _rstar > R_SEAM:
    fail.append("the horizon maximum is not outside the seam -- the 'rising branch' reading fails")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE PAPER NO LONGER ASSERTS A HORIZON PROPERTY OF THE BRANCH POINT")
print("=" * 78)
tex = open(TEX, encoding='utf-8').read()
body = re.sub(r'(?m)^%.*$', '', tex)

# the six repaired sites, each pinned by the corrected text rather than by a line number
REPAIRED = [
    ('subsection heading',
     r'\\subsection\{The acoustic modes are sub-horizon at the onset, and the branch point is the opposite\}'),
    ('prop:subhorizon body',
     r'inside the horizon at the onset by a factor'),
    ('sec:coherence',
     r'already sub-horizon at the seam \(Prop\.~\\ref\{prop:subhorizon\}\)'),
    ('sec:envelope derivation',
     r'\\emph\{seam\}\s*\} sits just inside that turning point'),
    ('sec:envelope driving amplitude',
     r'reaching the \\emph\{seam\}---where the collapse leg ends---with the same driving amplitude'),
]
# (the heading regex above is written against the file; the envelope one is checked loosely below)
for name, pat in REPAIRED[:3]:
    ok = re.search(pat, body) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {name}")
    if not ok:
        fail.append(f"the repaired text for {name} is not in the paper")
for name, frag in [('sec:envelope derivation', 'sits just inside that turning point'),
                   ('sec:envelope driving amplitude', 'where the collapse leg ends'),
                   ('header STATUS block', 'the SEAM, not the branch point')]:
    ok = frag in tex
    print(f"  {'OK ' if ok else 'MISSING'}  {name}")
    if not ok:
        fail.append(f"the repaired text for {name} is not in the paper")

# and the defective strings are gone
GONE = [
    'The branch point is sub-horizon for the acoustic modes',
    'inside the horizon at the branch point',
    'already sub-horizon at the branch point',
    'the branch point sits on its rising branch',
    'reaching the branch point with the same driving amplitude',
]
print()
for s in GONE:
    if s in body:
        print(f"  STILL PRESENT  {s!r}")
        fail.append(f"the defective string {s!r} is still in the paper")
    else:
        print(f"  gone           {s!r}")

# the protected false positive MUST survive
if 'branch point is far below their decoupling' not in body:
    fail.append("the neutrino-decoupling sentence was swept -- it is a TEMPERATURE ordering, "
                "true as written, and the finder named it as a false positive in advance")
else:
    print()
    print("  PROTECTED     'branch point is far below their decoupling' survived the sweep")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CITED RECEIPTS' OWN WORDS, WHICH ARE THE AUTHORITY ON WHICH LOCUS WAS COMPUTED")
print("=" * 78)
print(f"  {'receipt':>28s} {'says seam/onset':>16s} {'says branch point':>19s}")
for key in ('C2_horizon_limits', 'C4_driving_envelope', 'P15_verify_numeric'):
    path = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', key + '.py')
    src = open(path, encoding='utf-8').read()
    # PART 3 counts the receipts' PHYSICS prose, not the r2501 commentary added to C2 by this
    # revision -- which necessarily quotes the wrong word in order to record that it was wrong.
    src = re.sub(r'(?m)^\s*#\s*\*\*.*$', '', src)
    n_seam = len(re.findall(r'\bseam\b|\bonset\b', src, re.I))
    n_bp = len(re.findall(r'branch[ -]point', src, re.I))
    print(f"  {key:>28s} {n_seam:>16d} {n_bp:>19d}")
    if n_bp >= n_seam:
        fail.append(f"{key} does not predominantly name the seam/onset -- PART 3's premise fails")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE LINT: SEEDED BOTH WAYS, BECAUSE A CLEAN TREE MEASURES NOTHING")
print("=" * 78)
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_loci  # noqa: E402

# (a) as shipped, on the tree as it stands: clean, with the C6 flag declared and EXCUSED
_r = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_loci.py')],
                    capture_output=True, text=True)
print(f"  (a) tree as it stands            -> exit {_r.returncode}   "
      f"{'clean' if _r.returncode == 0 else 'FLAGGED'}")
if _r.returncode != 0:
    fail.append("check_loci does not pass on the repaired tree")
if 'EXCUSED' not in _r.stdout:
    fail.append("the declared C6 exception is not being reported as excused")

# (b) the motivating defect, seeded into the proposition BODY.  Before this revision's binder
#     extension the lint could not see this site at all; it must see it now.
seeded = body.replace('inside the horizon at the onset by a factor',
                      'inside the horizon at the branch point by a factor')
if seeded == body:
    fail.append("could not seed the motivating defect -- the target sentence moved")


def _flags(text, theorem_binding=True):
    """Run the lint's own logic over one document's text, with the theorem binding on or off."""
    hits = []
    for sent, key, line in check_loci.sentences_with_rcpt(text):
        if not theorem_binding and '\\label{prop:' in sent:
            continue  # the pre-c54.197 scan never produced these bindings at all
        claimed = check_loci.loci_asserted(sent)
        if not claimed:
            continue
        rp = check_loci.find_receipt(key)
        if rp is None:
            continue
        named = check_loci.loci_in(open(rp, encoding='utf-8', errors='replace').read())
        if not named or claimed <= named:
            continue
        flat = re.sub(r'\s+', ' ', sent)
        if check_loci.excused('CR_cosmology.tex', key, flat):
            continue
        hits.append((line, key))
    return hits


_before = _flags(seeded, theorem_binding=False)
_after = _flags(seeded, theorem_binding=True)
print(f"  (b) motivating defect seeded:")
print(f"        without the theorem binding (as shipped r2440) -> {len(_before)} flag(s)  "
      f"** {'MISSED' if not _before else 'caught'} **")
print(f"        with    the theorem binding (r2501+c54.197)    -> {len(_after)} flag(s)  "
      f"** {'caught at line %d' % _after[0][0] if _after else 'MISSED'} **")
if _before:
    fail.append("the pre-extension scan is reported as catching the seeded defect -- then the "
                "recall hole this revision fixes was not real, and PART 4 is wrong")
if not _after:
    fail.append("the extended scan does NOT catch the seeded defect -- the binder fix does not work")

# (c) and the declared exception must LAPSE when its sentence is rewritten, or it is a suppression
#     that outlives its reason
rewritten = body.replace('branch point is far below their decoupling',
                         'branch point is well outside their horizon')
_re_flags = _flags(rewritten, theorem_binding=True)
print(f"  (c) the excused sentence rewritten -> {len(_re_flags)} flag(s)  "
      f"** {'exception lapsed, site re-flagged' if _re_flags else 'STILL SUPPRESSED'} **")
if not _re_flags:
    fail.append("the declared exception still suppresses the site after its sentence was "
                "rewritten -- a suppression keyed to something that no longer exists")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the comoving horizon is maximal at the seam and vanishes toward r=0, so the")
print("word decides prop:subhorizon's truth value; six sites in P15 named the wrong locus and are")
print("repaired, the one true-as-written branch-point sentence survived; and the lint built for this")
print("defect could not see the worst of the six until this revision, which was found by seeding it.")
print("=" * 78)

# ============================================================================================
# GATE — r2501+c54.197, `L-509`.  Routed item 21 was VERIFIED THREE WAYS by the observer line
# before it was routed.  This file does not re-cite those; it re-derives the physics and then
# pins the two things the routing slip could not:
#   (1) the INVERSION itself, from the metric function alone -- if the comoving horizon were not
#       maximal at the seam and vanishing toward r=0, the substitution would be cosmetic and
#       every edit here would be unmotivated;
#   (2) r*/r_seam re-derived to C2's 1.5338 from the quartic, not quoted -- it is the number the
#       repaired sec:envelope and sec:coherence sentences now both carry;
#   (3) the six repaired sites present AND the six defective strings absent, pinned by TEXT so a
#       later edit that reintroduces one fails this file rather than passing on a line number;
#   (4) the protected false positive still present -- ** a sweep that also took the one true
#       sentence would be a different error with the same shape **;
#   (5) the lint's recall hole, seeded: MISSED before the binder extension, CAUGHT after.  This
#       is the assertion the whole PART 4 exists for, and it fails in BOTH directions -- if the
#       pre-extension scan ever starts catching it, the hole was not real and this file says so;
#   (6) and the declared exception lapsing when its sentence is rewritten, since an exception
#       that survives its own reason is the suppression this file argues against.
# ============================================================================================
assert _seam_h > 10.0 * _bp_h, "the seam/branch-point horizon inversion is not present"
assert abs(_rstar / R_SEAM - 1.5338) < 0.002, f"r*/r_seam = {_rstar / R_SEAM:.4f}, expected 1.5338"
assert _rstar > R_SEAM, "the horizon maximum is not outside the seam"
assert 'The branch point is sub-horizon for the acoustic modes' not in body
assert 'inside the horizon at the branch point' not in body
assert 'the branch point sits on its rising branch' not in body
assert 'branch point is far below their decoupling' in body, \
    "the protected neutrino sentence was swept"
assert _r.returncode == 0, "check_loci fails on the repaired tree"
assert not _before, "the pre-extension scan caught the seeded defect -- the recall hole was not real"
assert _after, "the extended scan misses the seeded defect -- the binder fix does not work"
assert _re_flags, "the declared exception outlives its own sentence"
print(f"GATE c54.197 (r2501), `L-509`: comoving horizon {_seam_h:.3f} at the seam against "
      f"{_bp_h:.3f} near r=0 — an inversion, not a blur; r* re-derived at "
      f"{_rstar / R_SEAM:.4f} r_seam; six sites repaired and the one true-as-written branch-point "
      f"sentence kept; and the lint MISSED the seeded motivating defect before this revision and "
      f"catches it at line {_after[0][0]} after — pinned against routed item 21 and `C2_horizon_limits`.")
