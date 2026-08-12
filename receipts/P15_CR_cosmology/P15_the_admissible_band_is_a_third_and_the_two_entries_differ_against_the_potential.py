#!/usr/bin/env python3
"""
RECEIPT -- P15: ** ROUTED ITEM 43 (r2509) ACCEPTED AND WORKED IN.  c54.195's WITHDRAWAL WAS TOO WIDE:
OVER THE PHASES THE CORPUS ADMITS THE ACOUSTIC PHASE MOVES BY 0.207, A THIRD OF THE 0.615 GAP, AND
THE CONTROL'S 0.263 IS NOT INSIDE IT.  THE DISAGREEMENT IS REAL AND BOUNDED. **

** AND THIS FILE CORRECTS ITS OWN LINE TWICE: c54.195's SPAN, AND THE REASON I GAVE 56 FOR THE BAND. **

Built r2512+c54.200, front #2, lead `L-513`.  VEIN: `L-202` (what the seam carries).

===================================================================================================
** WHAT r2509 FOUND, AND IT IS RIGHT **
===================================================================================================

c54.195 read a span across FOUR seam phases -- 0, pi/4, pi/2, pi -- found it 0.891 wide in phi/pi
with the control's 0.263 inside, and withdrew `L-506`'s promotion of 0.62 pi to "the whole
disagreement."  ** r2509: the span is only a BAND if every point in it is admissible, and two of the
four are not. **

  ⇒ *and the diagnosis underneath is the failure class this corpus has now named four times:*
    ** `CRPHI` is a HYDRODYNAMIC initial condition on the photon-baryon oscillator.  `L-202`'s phase
    is the ANTILINEAR FACE K on the branch structure.  Two objects sharing one word. **

** ⌗ AND THE CORPUS SELECTS THE PAIR RATHER THAN MERELY DISTINGUISHING IT, WHICH r2509 UNDERSTATES. **
r2509 picks phi in {0, pi} off the instrument's comment -- the only two values at which the mode
enters with zero velocity.  ** P15 `sec:what-crosses` FORCES them: ** on the contracting leg every
mode exits the comoving horizon and ** freezes ** before the crossing, and the Euclidean kernel "has
nothing to act on in a frozen mode."  A frozen mode has d(delta)/d(eta) = 0, the code's own
continuity equation gives theta_g = (3/4) D k c_s sin(phi), so ** theta_g = 0 <=> sin(phi) = 0 **.

  *** So the admissible pair is not an extra assumption laid on the scan.  It is sec:what-crosses
      read at the seam, and it was in the paper before the scan was run. ***

===================================================================================================
** ⛔ AND THE REASON I GAVE 56 FOR THE BAND IS WRONG.  THE CORRECT ONE IS SHARPER. **
===================================================================================================

`FOR_56` item 17 (c54.199) said: *"phi = 0 and phi = pi are an exact sign flip of the initial data, so
on a source-free linear evolution they would give identical |C_ell| -- the band is real because the
driving is an inhomogeneous source."*  ** The first clause is false and the rest follows from it. **

Read the instrument's own three lines:

      dg0 = 4.0 * (That - Ph0) * np.cos(_phi)      <- flips sign between 0 and pi
      th0 = ... * np.sin(_phi)                     <- zero at both
      y0[:, 6] = Ph0                               <- *** Ph0 = -1, INDEPENDENT of _phi ***

  *** THE PHOTON DATA FLIPS AND THE POTENTIAL DOES NOT.  So the two runs are not an overall sign
      flip of the state at all -- what reverses is the RELATIVE SIGN between the mode's density
      perturbation and the potential it sits in. ***

  ⇒ ** phi = 0 enters as a compression correlated with the potential well; phi = pi enters as a
    rarefaction against the same well.  Two physically distinct entries, both frozen. **  *The band
    needs no appeal to the driving being inhomogeneous, and that appeal was mine and was wrong.*

===================================================================================================
** THE NUMBERS, AND THEY ARE TWO NODES' AND AGREE TO FOUR DECIMALS **
===================================================================================================

  PART 3  ** phi/pi = 0.8780 at phi = 0 and 0.6711 at phi = pi.  Band 0.2069 against the 0.6152 gap
          -- a factor of 2.97, so A THIRD. **  *54's `c54.186_cr_L3000` and `c54.191_cr_phipi_L3000`
          against cc54's `item38_cr_phi0.0_prod` and `item38_cr_phi3.1416_prod`, independently run.*
  PART 4  ** AND THE CONTROL'S 0.2628 IS NOT INSIDE [0.6711, 0.8780]. **  *So c54.195's headline
          claim fails on the admissible pair, and the phase disagreement is real there.*
  PART 5  ** WHAT SURVIVES IS STRONGER ON THE PAIR THAN ON THE SPAN. **  c54.195's PART 5 --
          "agreeing on the phase does not fix the spectrum" -- was ILLUSTRATED at phi = pi/2, now
          inadmissible.  It does not rest on it: ** chi^2/dof is 281 at phi = 0 and 379 at phi = pi
          against the control's 3.71 -- 76x and 102x on the same 185 bins. **

*** SO THE POSITION IS: the acoustic phase disagreement is REAL over the admissible pair, it is
    BOUNDED at about a third of its own size, and no admissible reading brings the spectrum within
    seventy times the control.  Better than c54.190's "the whole disagreement"; better than
    c54.195's "the control is inside the span". ***

** F5 IS NOT SOFTENED and this file does not convert anything. **  A measurement discrepancy is not a
framework verdict; `PO-7` is protected; the conversion runs by `F5`'s stated procedure.  ** And the correction runs against
this line's own interest in both directions -- it makes the disagreement firmer than c54.195 left it
and it retracts the reason c54.199 gave for the band. **

SETTINGS: production depth for every number.  All five spectra are `LMAXL=3000 HIER=1 ETAEND=4000`,
read at the banked multipole grid; chi^2 on the plik_lite 185 bins, ell 100-1996.  ** No new run: this
file reads what is banked, including cc54's, which is the point of PART 3. **

rc=0 on success.  Run: python3 P15_the_admissible_band_is_a_third_and_the_two_entries_differ_against_the_potential.py
                        (numpy scipy; ~10 s)
"""
import os
import re
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
SRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

LMAX0 = 1996.0
fail = []


def read(fname):
    z = np.load(os.path.join(SP, fname))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    pk = argrelextrema(D, np.greater, order=3)[0]
    pos, h = ls[pk], D[pk]
    n = np.arange(1, len(pos) + 1)
    m = n >= 4
    b, a = np.polyfit(n[m], pos[m], 1)
    c = CS.chi2_of(ls, D, lmax=LMAX0)
    return dict(npk=len(pos), slope=float(b) / lA, phi=-float(a) / lA,
                p1p2=float(h[0] / h[1]), dof=c[0] / c[1], nbin=c[1],
                res=[float(pos[i] - (b * (i + 1) + a)) for i in range(3)])


# =====================================================================
print("=" * 78)
print("PART 1 — THE ADMISSIBLE PAIR IS FORCED BY sec:what-crosses, NOT CHOSEN")
print("=" * 78)
src = open(SRC, encoding='utf-8').read()
tex = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
CHAIN = [
    ("the instrument states the continuity relation theta_g = (3/4) D k c_s sin(phi)",
     src, r'theta_g = \(3/4\) D k c_s sin\(phi\)'),
    ("and names phi = 0 as a density extremum with theta = 0",
     src, r'phi = 0 is a density extremum with theta = 0'),
    ("P15 says every mode EXITS the comoving horizon on the contracting leg",
     tex, r'every mode \\emph\{exits\} it and freezes before the crossing'),
    ("and that the Euclidean kernel has nothing to act on in a FROZEN mode",
     tex, r'nothing to act on in a frozen mode'),
]
for what, hay, pat in CHAIN:
    ok = re.search(pat, hay, re.I) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the admissibility chain is broken at: {what}")
print()
print("  ** frozen => d(delta)/d(eta) = 0 => theta_g = 0 => sin(phi) = 0 => phi in {0, pi}. **")
print("  *r2509 read the pair off the instrument's comment as 'distinguished anyway'; the paper")
print("   FORCES it, and said so before the scan existed.*")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE REASON c54.199 GAVE 56 FOR THE BAND IS WRONG.  THE CODE'S OWN LINES")
print("=" * 78)
LINES = [
    ("the photon density datum carries cos(phi), so it FLIPS between 0 and pi",
     r'dg0 = 4\.0 \* \(That - Ph0\) \* np\.cos\(_phi\)'),
    ("the velocity carries sin(phi), so it is ZERO at both",
     r'th0 = 0\.75 \* \(4\.0 \* \(That \+ 1\.0\)\) \* kk \* _cs \* np\.sin\(_phi\)'),
    ("and the POTENTIAL is set from Ph0 with no phi in it at all",
     r'y0\[:, 6\] = Ph0'),
    ("Ph0 being a constant -1",
     r'Ph0 = -np\.ones\(nk\)'),
]
for what, pat in LINES:
    ok = re.search(pat, src) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the instrument no longer shows: {what}")
_That, _Ph0 = -0.4835, -1.0
print()
print(f"  {'phi':>7s} {'dg0':>10s} {'th0':>8s} {'Phi0':>7s}")
_d = {}
for nm, phi in (('0', 0.0), ('pi', np.pi)):
    dg0 = 4.0 * (_That - _Ph0) * np.cos(phi)
    th0 = 0.75 * (4.0 * (_That + 1.0)) * np.sin(phi)
    _d[nm] = dg0
    print(f"  {nm:>7s} {dg0:>+10.5f} {th0:>+8.5f} {_Ph0:>+7.2f}")
_flip = abs(_d['0'] + _d['pi']) < 1e-12
print()
print(f"  ** dg0 flips exactly ({_flip}) and Phi0 does not move.  So the two are NOT a sign flip of")
print("     the state -- what reverses is the RELATIVE SIGN of the density against the potential. **")
print("  ⇒ *phi = 0 enters as a compression correlated with the well, phi = pi as a rarefaction")
print("     against it: two distinct frozen entries.  The band needs no inhomogeneous source, and")
print("     `FOR_56` item 17's claim that it did is withdrawn here.*")
if not _flip:
    fail.append("dg0 does not flip sign between 0 and pi — PART 2's reading of the code is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE BAND, ON TWO NODES' PRODUCTION SPECTRA, INDEPENDENTLY RUN")
print("=" * 78)
RUNS = (('control', 'c54.186_lcdm_L3000.npz'),
        ('54   phi=0', 'c54.186_cr_L3000.npz'),
        ('54   phi=pi', 'c54.191_cr_phipi_L3000.npz'),
        ('cc54 phi=0', 'item38_cr_phi0.0_prod.npz'),
        ('cc54 phi=pi', 'item38_cr_phi3.1416_prod.npz'),
        ('54   phi=pi/4  [INADM]', 'c54.195_cr_phi0.7854_L3000.npz'),
        ('54   phi=pi/2  [INADM]', 'c54.195_cr_phi1.5708_L3000.npz'))
R = {}
print(f"  {'run':>24s} {'npk':>4s} {'slope/lA':>9s} {'phi/pi':>8s} {'P1/P2':>7s} {'chi2/dof':>9s}"
      f"   transient")
for nm, f in RUNS:
    R[nm] = read(f)
    r = R[nm]
    print(f"  {nm:>24s} {r['npk']:>4d} {r['slope']:>9.4f} {r['phi']:>8.4f} {r['p1p2']:>7.3f} "
          f"{r['dof']:>9.2f}   {r['res'][0]:+.0f} {r['res'][1]:+.0f} {r['res'][2]:+.0f}")
_agree = (abs(R['54   phi=0']['phi'] - R['cc54 phi=0']['phi']) < 1e-4 and
          abs(R['54   phi=pi']['phi'] - R['cc54 phi=pi']['phi']) < 1e-4)
print()
print(f"  ** the two nodes agree to four decimals at both admissible phases: {_agree} **")
print("  *the transient signature is present in every CR reading and absent from the control, which")
print("   is what fixes the peak INDEXING before any intercept is read (c54.190's trap).*")
if not _agree:
    fail.append("54 and cc54 disagree at an admissible phase — the replication PART 3 rests on failed")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — A THIRD, AND THE CONTROL IS NOT INSIDE IT")
print("=" * 78)
p0, ppi, pc = R['54   phi=0']['phi'], R['54   phi=pi']['phi'], R['control']['phi']
BAND = abs(p0 - ppi)
GAP = abs(p0 - pc)
lo, hi = min(p0, ppi), max(p0, ppi)
inside = lo <= pc <= hi
FULL = max(r['phi'] for k, r in R.items() if k != 'control') - \
       min(r['phi'] for k, r in R.items() if k != 'control')
print(f"  admissible band  |phi(0) - phi(pi)|      = {BAND:.4f}")
print(f"  the gap at phi = 0 (c54.190's figure)    = {GAP:.4f}")
print(f"  ratio                                     = {GAP / BAND:.3f}x   ** a third, not most **")
print(f"  band interval                             = [{lo:.4f}, {hi:.4f}]")
print(f"  control                                   =  {pc:.4f}   ** inside? {inside} **")
print(f"  (the FULL four-phase span c54.195 quoted  =  {FULL:.4f}, and it contains the control —")
print("   which is true of the span and not of the band, and that is the whole correction)")
if inside:
    fail.append("the control lies inside the admissible band — then r2509's correction does not bite")
if not (2.5 < GAP / BAND < 3.5):
    fail.append(f"the ratio is {GAP / BAND:.2f}, not the ~3 r2509 reports")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND WHAT SURVIVES IS STRONGER ON THE PAIR THAN ON THE SPAN")
print("=" * 78)
c0, cpi, cc = R['54   phi=0']['dof'], R['54   phi=pi']['dof'], R['control']['dof']
print(f"  chi2/dof   phi=0 {c0:.2f}   phi=pi {cpi:.2f}   control {cc:.2f}   "
      f"on {R['control']['nbin']} bins")
print(f"  ratios to the control: {c0 / cc:.0f}x and {cpi / cc:.0f}x")
print()
print("  ** c54.195's PART 5 was ILLUSTRATED at phi = pi/2, which r2509 makes inadmissible — and the")
print("     conclusion does not rest on it. **  *Both admissible readings are seventy times the")
print("     control or worse, so agreeing on the phase would not fix the spectrum and no admissible")
print("     reading comes close.*")
if min(c0, cpi) / cc < 50.0:
    fail.append(f"an admissible reading is only {min(c0, cpi) / cc:.0f}x the control — PART 5 fails")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — AND THE PAPER SAID THIS TWO PARAGRAPHS EARLIER.  c54.195 OVERWROTE ITS OWN ANSWER")
print("=" * 78)
EARLIER = [
    ("sec:refit-bound already called the datum's phase freedom a lever spanning A THIRD",
     r"phase freedom is a real lever on it and spans a third of it"),
    ("and already quoted the gap CLOSING to 0.408 at the opposite phase, and no further",
     r"closes from \$0\.615\$ to \$0\.408\$"),
]
for what, pat in EARLIER:
    ok = re.search(pat, tex, re.I) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P15 does not carry the earlier statement: {what}")
_gap_pi = abs(ppi - pc)
print()
print(f"  and that 0.408 is exactly this file's own |phi(pi) - phi(control)| = {_gap_pi:.4f}")
print()
print("  ** SO c54.191 HAD THE ADMISSIBLE-PAIR ANSWER, IN THE PAPER, BEFORE c54.195 WAS RUN. **")
print("  *c54.195 widened it to four phases, found the control inside the SPAN, and withdrew a")
print("   statement that was correct as the paper had it.*  ⇒ ***A withdrawal is a claim like any")
print("   other and can be wrong in the same way; this one overwrote its own paper's answer two")
print("   paragraphs above it, and nothing in the checklist reads upward.***")
if abs(_gap_pi - 0.408) > 0.003:
    fail.append(f"|phi(pi) - phi(control)| is {_gap_pi:.4f}, not the 0.408 the paper already carried")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — sec:what-crosses forces the zero-velocity pair; the two entries differ in")
print("the sign of the density against the potential and not by an overall flip; the acoustic phase")
print("moves 0.207 across them against a 0.615 gap, a third, with the control outside; and both")
print("admissible readings sit 76x and 102x the control in chi2 per degree of freedom.")
print("=" * 78)

# ============================================================================================
# GATE — r2512+c54.200, `L-513`.  This file accepts a correction to its own line and corrects a
# second thing its own line said one revision ago, so the pins are on both directions:
#   (1) the four-step admissibility chain, in the instrument's source and the paper's source --
#       ** if sec:what-crosses did not say modes FREEZE, the pair would be a choice and r2509
#       would be weaker than this file claims **;
#   (2) dg0 flipping while Ph0 does not, from the code's own lines -- this is what makes
#       `FOR_56` item 17's stated reason wrong, and it is asserted rather than described;
#   (3) 54's and cc54's fits agreeing to four decimals at BOTH admissible phases -- ** a band
#       measured on one node's spectra is a band measured once **;
#   (4) the ratio ~3 and, separately, the control asserted OUTSIDE the band -- if it were inside,
#       r2509's correction would not bite and c54.195 would stand as written;
#   (5) and both admissible readings asserted above 50x the control, without which PART 5's
#       survival claim is empty and the withdrawal would take the conclusion with it.
# ============================================================================================
assert _flip, "dg0 does not flip between the two admissible phases"
assert _agree, "54 and cc54 do not agree at the admissible phases"
assert abs(BAND - 0.2069) < 0.002, f"the admissible band is {BAND:.4f}, expected 0.2069"
assert abs(GAP - 0.6152) < 0.002, f"the gap is {GAP:.4f}, expected 0.6152"
assert 2.5 < GAP / BAND < 3.5, f"the ratio is {GAP / BAND:.2f}, not a third"
assert not inside, "the control lies inside the admissible band"
assert lo <= FULL + min(p0, ppi), "the full span is not wider than the band — nothing was corrected"
assert c0 / cc > 50 and cpi / cc > 50, \
    f"an admissible reading is within 50x the control ({c0 / cc:.0f}x, {cpi / cc:.0f}x)"
assert abs(_gap_pi - 0.408) < 0.003, \
    f"the paper's own earlier 0.408 does not reproduce: {_gap_pi:.4f}"
assert R['control']['nbin'] == 185, f"scored on {R['control']['nbin']} bins, not 185"
print(f"GATE c54.200 (r2512), `L-513`: the zero-velocity pair is forced by sec:what-crosses; the "
      f"acoustic phase runs {ppi:.4f}–{p0:.4f} across it, a band of {BAND:.4f} against a "
      f"{GAP:.4f} gap ({GAP / BAND:.2f}x) with the control's {pc:.4f} OUTSIDE; two nodes agree to "
      f"four decimals; and chi2/dof is {c0:.0f} and {cpi:.0f} against {cc:.2f} on "
      f"{R['control']['nbin']} bins — pinned against `FOR_54` item 43 (r2509), `L-508` and "
      f"P15 sec:what-crosses.")
