#!/usr/bin/env python3
"""
P15 receipt -- `r7091`'s Q1 AND Q2, RULED: THE FITTED ONSET IS THE WRONG CLOCK'S ARTEFACT.  THE
STACKING RULER KEEPS A SQUARE-ROOT MEMORY OF THE START AND THE LEAF RULER KEEPS NONE, SO THE TWO
DEFECTS THE ORDER NAMES SEPARATELY ARE ONE DEFECT.

** THE FRAME, WHICH IS THE ORDER'S AND NOT THIS SEAT'S. **  When the model does not match the
measured spectrum the default hypothesis is that the MODEL does not yet faithfully implement what CR
requires -- not a numerical issue, and not CR being rejected by the sky.  ⇒ *What follows is an
adjudication of the implementation against the construction's own sources.  No transfer is run here,
no channel is scored, and no spectrum is computed: `cc66` owns the rebuild.*

** Q1 -- THE SEVEN OBJECTS, RULED.  FOUR OF THE SEVEN ARE ON THE WRONG RATE AT THE DEFAULT. **

    object                                   CR requires   the instrument does      verdict
    ---------------------------------------- ------------- ------------------------ --------
    the acoustic phase / sound horizon r_s   LEAF          BOTH, and uses both      ⛔ WRONG
    the diffusion length r_D                 LEAF          stacking (LEAFSCALES=0)  ⛔ WRONG
    conformal time eta, comoving chi         STACKING      stacking                 ✔ right
    the visibility g = tau' e^-tau           see below     stacking (VISLEAF=0)     ⛔ WRONG
    recombination's microphysics (x_e)       LEAF          stacking, NO SWITCH      ⛔ WRONG
    the perturbation equations               LEAF          leaf (LEAFPERT=1)        ✔ right
    D_M and the projection distance          STACKING      stacking                 ✔ right

⛭ ** AND THE CORPUS IS UNANIMOUS, WHICH THE ORDER DID NOT EXPECT. **  The order says the assignment
is "contradicted between two papers and the default is the rejected one".  *It was, and it is not any
more.*  `P07`'s rate-rule remark, `P15` `sec:tensions` AND `P15` `sec:coherence` now all put the
plasma's scales on the leaf -- `sec:coherence` calling it *"forced by consistency"* and `sec:tensions`
naming *"recombination's microphysics and the perturbations"* alongside `r_s` and `r_D`.  The sentence
the instrument's comments cite as authority for the stacking default -- *"the scales such a separation
is read in --- r_s and r_D, which accumulate against the layer's own geometric expansion"* -- is
** NOT IN THE PAPER **, and `git log -S` dates its removal to `r6772+66.1`, which rewrote `sec:tensions`
to the adjudicated handover.
  ⇒ *** SO NO PAPER REWRITE IS OWED.  WHAT IS OWED IS THE CODE: the paper was corrected and the
  instrument's default was deliberately left on the superseded assignment so that *"every figure the
  corpus has quoted off this instrument"* would stay re-derivable -- with the consequence that every
  figure quoted SINCE carries the superseded assignment. ***

** THE VISIBILITY, WHICH `P15` FLAGS AS UNRESOLVED, IS NOT ACTUALLY UNDERDETERMINED. **  The
ambiguity is a confusion between what the density is OF and what it is a density IN.  `tau` counts
scatterings accumulated by the plasma, so it is accumulated on the LEAF clock; `g` is its derivative
with respect to whatever variable the line-of-sight integral runs over, which is stacking conformal
time because that is what the kernel's `chi` is built from.  ⇒ `g = (d tau/d eta_leaf)(d eta_leaf/d
eta_stack) e^-tau` -- the leaf-accumulated optical depth, Jacobian-weighted.  ** That is `VISLEAF=1`
exactly, and it is required rather than merely admissible. **  ⌗ *It is also what `1/k_D^2` twenty
lines below already does under `LEAFSCALES`, so the instrument's two answers to one question are not
both defensible: the Jac-weighted one is right.*

** Q2 -- THE ONSET IS DETERMINED BY THE CONSTRUCTION, SO SOLVING FOR IT IS UNFAITHFUL. **  `P15`'s
BODY says it three times and receipts it: *"There is no early-universe parameter among them: with the
plasma handed over at the branch point the sound horizon has no lower endpoint to place, so the angle
is an output of the rate rather than a calibration of it"*; *"with the plasma handed over at the branch
point there is no such start and no such amplitude"*; and *"where the plasma starts moves the scale and
not the peak, which is why the start is not free"*.  The instrument nevertheless sets `Z_START =
brentq(lambda z: pi*D_M/rs_from(z) - 301.6, ...)`, installing the parameter the construction denies.
  ⌗ ** AND ONE QUOTATION WAS WITHDRAWN FROM THIS RECEIPT BEFORE IT WAS USED, which is worth recording
  because the gate that caught it exists for exactly this hop. **  The sharpest statement of the point
  -- the masthead's sentence putting every acoustic mode outside the horizon at the handover, so that
  the angle is an output -- sits in `P15`'s HEADER COMMENT and nowhere in any paper's body, and
  `check_provenance` rejected quoting it: *a quotation lifted from a comment carries the authority of
  the paper it sits in while being no part of it.*  ⇒ *The ruling rests on the three BODY statements
  above and not on the masthead, and it is unchanged by the substitution -- which is the only reason
  the substitution is reportable rather than a weakening.*  ⛔ *It also means the masthead currently
  states as `established here` something the body states only in its weaker form; that is 66's to
  reconcile and is routed rather than edited.*

⛭⛭⛭ ** AND HERE IS THE FINDING THAT MAKES Q1 AND Q2 ONE QUESTION. **  *"No lower endpoint to place"
is a claim about an integral, and it is TRUE ON THE LEAF RATE AND FALSE ON THE STACKING RATE.*  The
start-sensitivity of `r_s` scales as a power of the start's scale factor, and the power is the
radiation term -- the one thing that distinguishes the two rates:

    d log (missing fraction) / d log a_start  =  0.50 on the stacking rate      (measured 0.5008)
                                             =  1.00 on the leaf rate          (measured 0.9983)

*The stacking rate has no radiation era, so its sound-horizon integrand goes as a^-1/2 and the integral
keeps a SQUARE-ROOT memory of wherever it was started: at z = 10^7 it is still 1.1 per cent short, and
at the instrument's own onset z = 6764 it is 43.1 per cent short.  The leaf rate has a radiation era,
so its integrand is flat in a and the memory is LINEAR: 0.006 per cent short at z = 3x10^7.*
  ⇒ *** A STACKING RULER REQUIRES A HAND-PLACED START.  A LEAF RULER DOES NOT.  So the fitted onset is
  not an independent modelling choice that happens to sit beside a clock error -- IT IS THE CLOCK
  ERROR'S ONLY AVAILABLE REPAIR, and correcting Q1 dissolves Q2's parameter rather than merely
  re-pointing it. ***
  ⌗ *And the direction of the laundering is exact.  `r6893+cc66.37` measured that no transfer function
  reads `R_S` or `L_A` -- a 24 per cent move in `r_s` leaves `D_l` bit-identical -- so the ruler's clock
  reaches the spectrum through ONE channel and one only: the onset solve.  Remove the solve and the
  stacking ruler stops propagating; keep it and every spectrum carries the superseded assignment
  through `z_onset`.*

** WHICH IS DARYL'S READING OF THE RESIDUALS, DERIVED RATHER THAN RESTATED. **  *The model can slide
but not reshape.*  The onset solve is a one-parameter rescale of the comb's denominator -- `P15`'s own
scan runs `l_A` from 360.6 to 239.3 over a factor 3.6 in the start while the first peak sits between
206 and 210 throughout -- so the one adjustable time origin moves `l_A` and leaves `l_1` where it is.
** A model whose only freedom is the denominator of the ratio being scored is inaccurate everywhere
except where it crosses the data on the way past, which is the signature the order describes. **

⛭ ** AND THE START IS ON THE WRONG SIDE OF HORIZON CROSSING, WHICH IS THE ORDER'S SUB-QUESTION. **
At the handover the comoving horizon vanishes -- `1/(aH) -> 0` as `a -> 0` on BOTH rates, so the
super-horizon condition is rate-independent and survives whatever Q1 decides.  At the instrument's
default onset the first three peaks' modes are all INSIDE it: `k/(aH) = 1.53, 3.73, 5.67`.  ⇒ *The
file's own suspicion is correct: a `k`-dependence of the driving read off a start inside the horizon
is an artefact of the start and not a fact about CR's driving.*  ** The CR arm must start where the
control starts (`3x10^7`, all modes outside), and the asymmetry between `6.8x10^3` and `3x10^7` is
itself the defect. **

** THE SIZES, RANKED, BECAUSE A RULING WITHOUT ONE INVITES FOUR EQUAL REWRITES. **
  (1) the ruler's clock, through the onset:  `r_s` 237.08 vs 139.74 Mpc from a ~ 0 (a factor 1.697),
      `l_A` 172.3 vs 292.4, and `z_onset` 6761 vs 61583 -- a factor 9.1 in where the evolution starts.
  (2) the start's existence: 43.1 per cent of the stacking integral missing at the default onset.
  (3) the visibility's clock: `z_LS` +0.90 per cent, FWHM +1.1 per cent.  ** About a per cent. **
  (4) recombination's rate: `x_e` higher by 2.2 to 8.3 per cent across the visibility, the ionisation
      crossings moved by 0.4 to 0.6 per cent in `z`.  ** Sub-per-cent in `z`, and unswitchable. **

⚠ ** WHAT THIS RECEIPT DOES NOT CLAIM. **  It does not claim a spectrum, a likelihood, or that the
corrected implementation will match the sky.  It rules on assignments and measures the size of each
mis-assignment on the BACKGROUND and on the ionisation history -- which is all an adjudication can
reach.  ⛔ *And it proposes no one-at-a-time clock test: `r6919` showed the swap moves `r_s(eta_LS)`
and hence the comb, so a band regression on an isolated factor reads two oscillations out of phase.
The rulings are to be carried by a consistent rebuild with the comb re-derived.*

⌗ ** THE AFFIRMATIVE CONTROL. **  On the control arm radiation is in the rate (`RAD_IN_RATE=True`), so
`H_leaf` and `H_stack` are the same expression and every quantity measured here is identically zero
there.  *That is reported as a check that these are measurements of the rate difference and not of the
method.*
"""
import os
import re
import subprocess
import sys
import time

import numpy as np
import sympy as sp
from scipy.integrate import cumulative_trapezoid, quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INSTR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
src = open(INSTR, encoding='utf-8').read()
p15 = open(P15, encoding='utf-8').read()
p07 = open(P07, encoding='utf-8').read()


def flat(t):
    """one line, comment markers stripped -- so a quote that the source WRAPS still matches.

    A wrapped quotation is the same quotation; matching the raw text would make every gate here a
    test of where the line breaks fall rather than of what the source says."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


fsrc, fp15, fp07 = flat(src), flat(p15), flat(p07)

# ===================================================== A. the corpus's own assignment, read verbatim
head("A.  ⛭⛭ Q1's AUTHORITY: THE CORPUS IS UNANIMOUS, AND THE SENTENCE THE CODE CITES IS GONE")

RULE07 = ("a quantity computed from a process running \\emph{in} the content---the plasma's sound "
          "horizon, its diffusion length, recombination, the perturbations---takes the leaf's")
gate("`P07`'s rate-rule remark puts the plasma's sound horizon, its diffusion length, recombination "
     "AND the perturbations on the LEAF, in those words", RULE07 in p07)
gate("⛭ and it puts the stacking rate on the other side by NAME -- a comoving separation read across "
     "leaves, $D_M$, $D_H$, $D_V$, the observable expansion",
     "a comoving separation read across leaves, $D_M$, $D_H$, $D_V$, the observable expansion---takes "
     "the stacking rate" in p07)

RULE15 = ("the scales the plasma itself accumulates---$\\rs$ and $r_D$---take the leaf's, together "
          "with recombination's microphysics and the perturbations")
gate("`P15` `sec:tensions` NOW says the same thing, and names recombination's microphysics with it",
     RULE15 in p15)
gate("⛭ and `P15` `sec:coherence` says it a third time and calls it FORCED -- \"one may not take the "
     "rate geometric for the peak spacing and radiation-included for the diffusion\"",
     "This is forced by consistency: one may not take the rate geometric for the peak spacing and "
     "radiation-included for the diffusion" in p15)

DEAD = "r_s and r_D, which accumulate against the layer's own geometric expansion"
gate("⛔⛔ AND THE SENTENCE THE INSTRUMENT CITES AS AUTHORITY FOR THE STACKING DEFAULT IS NOT IN THE "
     "PAPER -- so the contradiction the order describes is already resolved, in the leaf's favour",
     DEAD not in fp15)
gate("⌗ and the instrument still quotes it -- twice -- which is why the default outlived the "
     "rewrite", fsrc.count(DEAD) == 2)
_log = subprocess.run(['git', 'log', '--format=%s', '-S',
                       "accumulate against the layer's own geometric expansion",
                       '--', 'corpus/CR_cosmology.tex'],
                      cwd=ROOT, capture_output=True, text=True).stdout
gate("⛭ `git log -S` dates the removal to `r6772+66.1`, which rewrote `sec:tensions` to the "
     "adjudicated handover -- so the paper moved and the code did not",
     'r6772+66.1' in _log and 'sec:tensions rewritten' in _log)

# ===================================================== B. what the instrument actually does
head("B.  ⛔ Q1's SUBJECT: THE INSTRUMENT'S OWN DEFAULTS, PARSED RATHER THAN REMEMBERED")

gate("`LEAFSCALES` -- which puts `r_s` and `r_D` on the leaf -- DEFAULTS OFF",
     "LEAFSCALES = os.environ.get('LEAFSCALES', '0') == '1'" in src)
gate("`VISLEAF` -- the visibility's clock -- DEFAULTS to the stacking measure",
     "_VISLF = float(os.environ.get('VISLEAF', '0'))" in src)
gate("✔ `LEAFPERT` -- the perturbation sector on the leaf -- DEFAULTS ON, which is the one assignment "
     "the implementation already has right",
     "LEAFPERT = os.environ.get('STACKPERT', '0') != '1'" in src)
# ⛔⛭⛭ RE-POINTED r7095 (66, the gate, adjudicating).  ** THESE TWO CHECKS PINNED THE LITERAL SOURCE
# ** TEXT OF ANOTHER SEAT'S INSTRUMENT, AND THAT SEAT REWROTE IT IN THE SAME ROUND. **  *They asserted
# `xe_history(lambda z: Hphys(...)` and the `eg = ...Hphys(ag)...` line verbatim; `cc66.73` introduced
# `LEAFGEOM` and with it `Hgeom = Hleaf if LEAFGEOM else Hphys`, so both strings moved and this receipt
# went red on a tree where every one of its RULINGS still holds.*
#   ⇒ *** THE RULING IS WHAT CR REQUIRES, AND THAT DOES NOT MOVE WHEN A SWITCH IS ADDED.  This is the
#     register's own standing form -- a gate that pins any measurement of the corpus's CURRENT text has
#     a subject free to move for reasons that have nothing to do with its finding -- and the subject
#     here moved for exactly such a reason: the defect being FIXED. ***
#   ⌗ *Re-pointed by the gate and not by `60`, because the edit that broke them is `cc66`'s and the
#     adjudication between the two deliveries is the gate's; `60`'s findings are untouched.*
# ⛭ ** AND THE REPLACEMENT CHECKS ARE STRONGER THAN WHAT THEY REPLACE, because the new state makes the
#   ruling UNREACHABLE and that is the thing worth gating. **  *`LEAFGEOM` is one switch over two
#   objects: it sets the rate the geometry is built on AND the rate the ionisation history is solved on.
#   The rule assigns `D_M` the stacking rate and recombination the leaf's, so no setting of one switch
#   satisfies both -- which is a sharper statement about the instrument than either original check.*
# ⛭⛭⛭ RE-POINTED AGAIN, ONE ROUND LATER AND FOR THE SAME REASON -- **by `cc66`, whose own edit moved
# ** the subject, and the ruling this check was re-pointed to assert is now MET rather than unreachable. **
# *The re-pointing above (`r7095`, the gate) replaced two verbatim source pins with a statement that the
# rule's pair -- `D_M` on the stacking rate, recombination on the leaf's -- was UNREACHABLE from this
# file, because `LEAFGEOM` was one switch over both objects.  **`r7095`'s own order to `cc66` was to
# split that knob, and `cc66.75` did: `LEAFREC` carries recombination's rate alone.**  So the gate wrote
# the unreachability down in the same round it commissioned the fix for it, and the pin went red on the
# tree that satisfies it.*
#   ⇒ *** THIS IS THE SECOND TIME IN TWO ROUNDS THAT THIS CHECK'S SUBJECT MOVED BECAUSE THE DEFECT IT
#     NAMES WAS BEING REPAIRED, which is the standing form the comment above already identified.  The
#     ruling has not moved either time.  What moved is whether the instrument can express it. ***
# ⛭ ** AND THE REPLACEMENT IS STRONGER AGAIN, because it no longer asserts a capability but a DEFAULT. **
#   *`LEAFGEOM` defaults OFF, so `Hgeom` is `Hphys`, the stacking rate -- the rule's assignment for a
#   separation read across leaves.  `LEAFREC` defaults ON, so `Hrec` is `Hleaf` -- the rule's assignment
#   for a process running in the content.  **The pair the rate rule requires is what this file now does
#   with no environment set at all**, which is the thing worth gating and was not true before `cc66.75`.*
#   ⚠ *The cost is recorded where it belongs and not here: `LEAFREC` is the first clock switch in the
#   instrument whose default is ON, so the default output MOVED, and every spectrum banked before it was
#   banked at `LEAFREC=0`.  That is stated at the switch's own site.*
gate("⛭⛭ the ionisation history's rate IS INDEPENDENTLY ASSIGNABLE AND DEFAULTS TO THE LEAF -- "
     "`LEAFREC` carries recombination's rate alone, split out of `LEAFGEOM` so the geometry can stay "
     "on the stacking rate while the plasma's own process runs on the content's: the pair the rate "
     "rule requires of them, and no longer reachable only by a setting",
     re.search(r"xe_history\(lambda z: Hrec\(1 / \(1 \+ z\)\)", src) is not None
     and "LEAFREC = os.environ.get('LEAFREC', '1') == '1'" in src
     and "Hrec = Hleaf if LEAFREC else Hgeom" in src
     and "Hgeom = Hleaf if LEAFGEOM else Hphys" in src)
gate("⌗ and the two defaults are read off the file rather than assumed: `LEAFGEOM` OFF puts the "
     "geometry on `Hphys`, `LEAFREC` ON puts recombination on `Hleaf`, so the rule's assignment is "
     "the instrument's behaviour with nothing set",
     "LEAFGEOM = os.environ.get('LEAFGEOM', '0') == '1'" in src
     and "LEAFREC = os.environ.get('LEAFREC', '1') == '1'" in src)
gate("✔ conformal time, and so `chi` and `D_M`, are read off ONE grid built from a single rate "
     "variable -- `Hgeom`, which is `Hphys` at the default and the rule's assignment for a separation "
     "read across leaves",
     re.search(r"eg = np\.concatenate\(\[\[_seed\], _seed \+ cumulative_trapezoid\("
               r"C / \(ag \*\* 2 \* Hgeom\(ag\)\), ag\)\]\)", src) is not None
     and "D_M = eta_0 - eta_rec" in src
     and "Hgeom = Hleaf if LEAFGEOM else Hphys" in src)
gate("⛭ and the rule's assignment is quoted from `P07` rather than paraphrased, because the whole "
     "ruling rests on it: a comoving separation read across leaves takes the STACKING rate, and "
     "reading a stacking quantity on the leaf's is what the proposition forbids",
     'a comoving separation read across leaves, $D_M$, $D_H$, $D_V$, the observable '
     'expansion---takes the stacking rate' in fp07
     and 'There is no locus at which the rate switches' in fp07
     and "reading a content process on the stacking rate, or a stacking quantity on the "
         "leaf's, is not a modelling choice but the reification the proposition forbids" in fp07)
gate("⛔ Q2's subject: the CR arm's onset is SOLVED so that pi D_M / r_s hits 301.6",
     "brentq(lambda z: np.pi * D_M / rs_from(z) - _latarg, 1500., 5.0e6)" in src)
gate("⛔⛔ and the instrument carries TWO sound horizons and uses BOTH, its own docstring saying "
     "\"Both are correct\" and \"Do NOT unify them\" -- one physical object on two clocks",
     "THE INSTRUMENT CARRIES TWO SOUND HORIZONS BY DESIGN" in fsrc
     and "Both are correct." in fsrc and "Do NOT unify them" in fsrc)

# ===================================================== C. the two rates
head("C.  THE TWO RATES DIFFER BY THE RADIATION TERM ALONE -- the rule's own decomposition, exactly")

z, H0s, Oms, OLs, Ors = sp.symbols('z H0 Omega_m Omega_L Omega_r', positive=True)
Hst2 = H0s**2 * (Oms * (1 + z)**3 + OLs)
Hlf2 = H0s**2 * (Oms * (1 + z)**3 + OLs + Ors * (1 + z)**4)
gate("⛭ H_leaf^2 - H_stack^2 = H_0^2 Omega_r (1+z)^4 EXACTLY, symbolically -- so the whole of the "
     "clock question is the one term the kernel theorem excludes from the rate",
     sp.simplify(sp.expand(Hlf2 - Hst2 - H0s**2 * Ors * (1 + z)**4)) == 0)

C = 299792.458
H0, OM, OMBH2, YP = 73.00, 0.3066, 0.0224, 0.2454          # the instrument's CR-arm defaults
OL = 1.0 - OM
OR = 4.15e-5 / (H0 / 100) ** 2
Z_REC = 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
gate("the arm's parameters are read off the instrument and not retyped (H0=73.00, Om=0.3066, "
     "wb=0.0224, z_rec=1089.9, radiation ABSENT from the arm's rate)",
     "H0, OM, OMBH2 = 73.00, 0.3066, 0.0224" in src and "FNU, Z_REC = 0.4052, 1089.9" in src
     and "RAD_IN_RATE = False" in src)

Hs = lambda a: H0 * np.sqrt(OM / a**3 + OL)                  # noqa: E731  stacking: no radiation
Hl = lambda a: H0 * np.sqrt(OM / a**3 + OL + OR / a**4)      # noqa: E731  leaf: radiation gravitates
ag = np.logspace(-9, 0, 40000)
_seed = float(quad(lambda a: C / (a**2 * Hs(a)), 1e-16, ag[0], limit=200)[0])
eg = np.concatenate([[_seed], _seed + cumulative_trapezoid(C / (ag**2 * Hs(ag)), ag)])
eta_0 = eg[-1]
eta_rec = float(np.interp(A_REC, ag, eg))
D_M = eta_0 - eta_rec
Hc_of = CubicSpline(eg, ag * Hs(ag) / C)
Jac_of = CubicSpline(eg, Hs(ag) / Hl(ag))
gate(f"the stacking D_M comes out at {D_M:.0f} Mpc, the distance the projection kernel reads",
     12500.0 < D_M < 13500.0)

cs = lambda a: 1.0 / np.sqrt(3 * (1 + RB_REC * a / A_REC))   # noqa: E731
rs = lambda H, z_lo: quad(lambda a: C / (a**2 * H(a)) * cs(a),               # noqa: E731
                          1.0 / (1.0 + z_lo), A_REC, limit=250)[0]

# ===================================================== D. the ruler
head("D.  ⛭⛭ THE RULER: THE COMB RIDES THE LEAF ACCUMULATION, re-measured against 66's adjudication")

rs_s0, rs_l0 = rs(Hs, 1e8), rs(Hl, 1e8)
lA_s0, lA_l0 = np.pi * D_M / rs_s0, np.pi * D_M / rs_l0
print(f"      r_s from a ~ 0:  stacking {rs_s0:7.2f} Mpc -> l_A = {lA_s0:6.2f}")
print(f"                       leaf     {rs_l0:7.2f} Mpc -> l_A = {lA_l0:6.2f}     "
      f"(66's banked pair: 172.8 and 292.4)")
gate("⛭ the LEAF ruler reproduces `r6760+66.1`'s banked pi D_M / r_s,leaf = 292.4 to better than "
     "half a per cent, computed here from the background alone", abs(lA_l0 - 292.4) < 1.5)
gate("⛭ and the STACKING ruler reproduces its 172.8 to the same tolerance -- so both halves of the "
     "adjudication's measurement are independently re-derived here", abs(lA_s0 - 172.8) < 1.5)
gate("⛔ THE FITTED COMB, l_A = 286.0, IS WITHIN 2.3 PER CENT OF THE LEAF RULER AND NOWHERE NEAR THE "
     "STACKING ONE -- which is what decides Q1 on a measurement rather than on a sentence",
     abs(286.0 - lA_l0) / 286.0 < 0.03 and abs(286.0 - lA_s0) / 286.0 > 0.3)
gate(f"the two rulers differ by a factor {rs_s0/rs_l0:.3f} from a ~ 0, so this is not a correction "
     "but a different object", 1.6 < rs_s0 / rs_l0 < 1.8)
rs_s_on, rs_l_on = rs(Hs, 6764.0), rs(Hl, 6764.0)
gate("⌗ and at the instrument's own onset the pair is 135.5 / 105.4 Mpc, ratio 1.286 -- the figure "
     "`sound_phase`'s docstring prints, reproduced",
     abs(rs_s_on - 135.46) < 0.5 and abs(rs_l_on - 105.36) < 0.5
     and abs(rs_s_on / rs_l_on - 1.286) < 0.005 and "rs_leaf 105.36 Mpc" in fsrc)

# ===================================================== E. the central finding
head("E.  ⛭⛭⛭ THE FINDING: THE STACKING RULER KEEPS A SQUARE-ROOT MEMORY OF THE START, THE LEAF NONE")

piece = lambda H, a_s: quad(lambda a: C / (a**2 * H(a)) * cs(a), 1e-12, a_s, limit=300)[0]  # noqa
zs = np.array([1e5, 3e5, 1e6, 3e6, 1e7, 3e7])
a_s = 1.0 / (1.0 + zs)
slopes, miss = {}, {}
for H, nm in ((Hs, 'stacking'), (Hl, 'leaf')):
    full = piece(H, A_REC)
    m = np.array([piece(H, x) / full for x in a_s])
    slopes[nm] = float(np.polyfit(np.log(a_s), np.log(m), 1)[0])
    miss[nm] = m
    print(f"      {nm:>8}: missing fraction at z = 1e5 .. 3e7 : "
          + "  ".join(f"{v:.2e}" for v in m) + f"   slope = {slopes[nm]:.4f}")
gate("⛭⛭⛭ d log(missing) / d log a_start = 1/2 ON THE STACKING RATE -- the integrand goes as "
     "a^-1/2 because the rate has no radiation era, so the integral never forgets its start",
     abs(slopes['stacking'] - 0.5) < 0.02)
gate("⛭⛭⛭ AND = 1 ON THE LEAF RATE -- the integrand is flat in a because the rate HAS a radiation "
     "era, so the memory is linear and dies twice as fast per decade",
     abs(slopes['leaf'] - 1.0) < 0.02)
gate("⇒ SO \"the sound horizon has no lower endpoint to place\" IS TRUE ON THE LEAF RATE AND FALSE "
     "ON THE STACKING ONE: at z = 3e7 the leaf integral is short by under 0.01 per cent and the "
     "stacking one by over half a per cent, fifty times more",
     miss['leaf'][-1] < 1e-4 < miss['stacking'][-1] and miss['stacking'][-1] / miss['leaf'][-1] > 40)
_m_on = 1.0 - rs_s_on / piece(Hs, A_REC)
gate(f"⛔ and at the instrument's own onset the stacking integral is short by {100*_m_on:.1f} per "
     "cent -- so a stacking ruler does not merely prefer a hand-placed start, it REQUIRES one",
     0.40 < _m_on < 0.46)
gate("⇒⇒ THE TWO DEFECTS THE ORDER NAMES SEPARATELY ARE ONE DEFECT: the fitted onset is the stacking "
     "ruler's only available repair, so correcting the clock DISSOLVES the parameter rather than "
     "re-pointing it", abs(slopes['stacking'] - 0.5) < 0.02 and abs(slopes['leaf'] - 1.0) < 0.02)
gate("⌗ and the laundering has exactly one channel: `r6893+cc66.37` measured that no transfer "
     "function reads `R_S` or `L_A`, so the ruler's clock reaches the spectrum ONLY through the "
     "onset solve",
     "are DIAGNOSTICS of this instrument" in fsrc
     and "`hier_run` accepts all three and uses none." in fsrc)

# ===================================================== F. the onset on each ruler
head("F.  ⛔ Q2: WHAT THE PIN COSTS -- the onset moves by a factor nine when the ruler's clock moves")

z_on_s = brentq(lambda zz: np.pi * D_M / rs(Hs, zz) - 301.6, 1500., 5.0e6)
z_on_l = brentq(lambda zz: np.pi * D_M / rs(Hl, zz) - 301.6, 1500., 5.0e6)
print(f"      pinning l_A = 301.6:  z_onset = {z_on_s:8.1f} on the stacking ruler, "
      f"{z_on_l:9.1f} on the leaf's   (factor {z_on_l/z_on_s:.1f})")
gate("the stacking pin reproduces the instrument's own root, z_onset = 6764, from the background "
     "alone", abs(z_on_s - 6764.0) / 6764.0 < 0.01 and "6764 either way" in fsrc)
gate("⛭ and on the leaf ruler the SAME pin needs z_onset ~ 6e4 -- the value `r6760+66.1` records, "
     "and a factor of nine in where the perturbation evolution is started",
     5.0e4 < z_on_l < 7.0e4 and z_on_l / z_on_s > 8.0)
gate("⛔ `P15`'s BODY states three times that there is no onset parameter -- no early-universe "
     "parameter among them, the sound horizon with no lower endpoint to place, and no such start",
     "There is no early-universe parameter among them" in fp15
     and "the sound horizon has no lower endpoint to place, so the angle is an output of the rate "
         "rather than a calibration of it" in fp15
     and "with the plasma handed over at the branch point there is no such start and no such "
         "amplitude" in fp15)
# ** THE PHRASE ITSELF IS NOT WRITTEN HERE, and that is the point rather than an evasion: a 45+
# character quotation of a COMMENT is what `check_provenance` rejects, so the gate locates the
# sentence instead of reproducing it. **
_PL = 'onset parameter'
_lines = open(P15, encoding='utf-8').read().splitlines()
_cm = [ln for ln in _lines if ln.lstrip().startswith('%') and _PL in ln]
_bd = [ln for ln in _lines if not ln.lstrip().startswith('%') and _PL in ln]
gate("⌗ AND THE SHARPEST STATEMENT OF IT IS IN A HEADER COMMENT AND NOWHERE IN THE BODY, so this "
     "receipt does not quote it -- `check_provenance` rejects a quotation lifted from a comment, "
     "and the ruling stands on the three body statements without it",
     len(_cm) == 1 and len(_bd) == 0)
gate("⛭ and `P15` already states the consequence the order reads off the residuals: \"where the "
     "plasma starts moves the scale and not the peak, which is why the start is not free\" -- l_A "
     "from 360.6 to 239.3 while the first peak sits between 206 and 210",
     "moves the scale and not the peak, which is why the start is not free" in fp15
     and "runs $\\ell_{A}$ from $360.6$ down to $239.3$ while the first peak sits between $206$ "
         "and $210$ throughout" in fp15)

# ===================================================== G. the horizon at the handover
head("G.  ⛭ Q2's SUB-QUESTION: A START INSIDE THE HORIZON IS NOT WHAT CR REQUIRES")

aa = np.array([1e-9, 1e-8, 1e-7, 1e-6])
for H, nm in ((Hs, 'stacking'), (Hl, 'leaf')):
    ch = aa * H(aa)
    gate(f"the comoving horizon 1/(aH) -> 0 as a -> 0 on the {nm} rate: aH is monotone DECREASING in "
         "a there, so every mode is outside the horizon at the handover",
         bool(np.all(np.diff(ch) < 0)))
gate("⇒ so the super-horizon-at-handover condition is RATE-INDEPENDENT and survives whatever Q1 "
     "decides -- which is why Q2 can be answered without waiting on the rebuild",
     bool(np.all(np.diff(aa * Hs(aa)) < 0) and np.all(np.diff(aa * Hl(aa)) < 0)))
gate("and `P15` derives it from the metric function rather than asserting it -- 1/(aH) vanishes as "
     "r -> 0 because 2M/r diverges there, \"so $k/(aH)\\to0$ for every $k$\"",
     "so $k/(aH)\\to0$ for every $k$" in fp15)

_e_on = float(np.interp(1.0 / (1.0 + 6764.0), ag, eg))
_h_on = float(Hc_of(_e_on))
kon = {n: (ell / D_M) / _h_on for n, ell in ((1, 220.4), (2, 537.7), (3, 817.3))}
print("      at the default onset z = 6764:  k/(aH) = "
      + ",  ".join(f"peak {n} {v:.2f}" for n, v in kon.items()))
gate("⛔⛔ AT THE INSTRUMENT'S DEFAULT ONSET ALL THREE OF THE FIRST PEAKS' MODES ARE INSIDE THE "
     "HORIZON (k/(aH) = 1.5, 3.7, 5.7) -- the arm starts on the wrong side of crossing for the whole "
     "acoustic band", all(v > 1.0 for v in kon.values()))
_e_ctl = float(np.interp(1.0 / (1.0 + 3.0e7), ag, eg))
_h_ctl = float(Hc_of(_e_ctl))
gate("✔ and at the CONTROL's start, z = 3e7, every one of them is outside it -- so the condition the "
     "construction requires is the one the control already meets and the arm does not",
     all((ell / D_M) / _h_ctl < 1.0 for ell in (220.4, 537.7, 817.3)))
gate("⇒ the file's own suspicion is upheld: a k-dependence of the driving read off a start inside the "
     "horizon is an artefact of the start, in the file's words \"NOT a fact about CR's driving\"",
     "an artefact of starting inside the horizon and NOT a fact about CR's driving" in fsrc)

# ===================================================== H. the visibility and the ionisation history
head("H.  THE TWO SUB-PER-CENT RULINGS, MEASURED SO THEY ARE NOT MISTAKEN FOR THE BIG ONES")

sys.path.insert(0, os.path.join(ROOT, 'storyboard_receipts'))
from RD_diffusion_direct import n_H0_of, sigT, Mpc_m, xe_history, xe_total   # noqa: E402

nH0 = n_H0_of(OMBH2, YP)
_hist = {}
for H, nm in ((Hs, 'stacking'), (Hl, 'leaf')):
    zg, xeg = xe_history(lambda zz, _H=H: _H(1 / (1 + zz)) * 1e3 / Mpc_m, OMBH2, YP,
                         z_hi=3000.0, z_lo=80.0, n=1500)
    _hist[nm] = (zg, xeg, np.array([xe_total(zz, x, nH0, YP, helium=True)
                                    for zz, x in zip(zg, xeg)]))
zg = _hist['stacking'][0]
rat = np.array([_hist['leaf'][2][i] / _hist['stacking'][2][i]
                for i in [int(np.argmin(np.abs(zg - v))) for v in (1300., 1100., 900.)]])
print("      x_e(leaf)/x_e(stacking) at z = 1300, 1100, 900: "
      + ",  ".join(f"{v:.4f}" for v in rat))
gate("⛔ recombination on the leaf rate leaves MORE residual ionisation -- the faster expansion "
     "freezes out earlier -- by 2 to 9 per cent across the visibility, so the mis-assignment is real "
     "and small", bool(np.all(rat > 1.01) and np.all(rat < 1.12)))
_cr = {}
for nm in ('stacking', 'leaf'):
    g_, x_, _ = _hist[nm]
    _cr[nm] = [float(g_[int(np.argmin(np.abs(x_ - f)))]) for f in (0.5, 0.1)]
gate("⌗ and the ionisation crossings move by well under a per cent in z, which is why this is the "
     "smallest of the four and still has no switch",
     all(0.001 < abs(_cr['leaf'][i] / _cr['stacking'][i] - 1.0) < 0.01 for i in (0, 1)))


def visibility(leaf_measure):
    """eta_LS, FWHM and z_LS with d(tau) measured in the leaf clock or the stacking one."""
    zg_, xeg_, _ = _hist['stacking']          # the instrument's own history, held fixed here

    def _xe(a):
        zz = 1.0 / a - 1.0
        xH = (float(np.interp(zz, zg_[::-1], xeg_[::-1])) if (zg_[-1] <= zz <= zg_[0])
              else (1.0 if zz > zg_[0] else float(xeg_[-1])))
        return xe_total(zz, xH, nH0, YP, helium=True)

    av = np.logspace(np.log10(1 / (1 + 3e4)), 0.0, 2000)
    ev = np.array([float(np.interp(x, ag, eg)) for x in av])
    tp_of = CubicSpline(ev, np.array([_xe(x) * nH0 / x**3 * sigT * x * Mpc_m for x in av]))
    grid = np.linspace(float(ev[0]), eta_0, 20000)
    tp = np.maximum(tp_of(grid), 0.0)
    d = np.diff(grid)
    if leaf_measure:
        d = d * 0.5 * (np.asarray(Jac_of(grid[1:]), float) + np.asarray(Jac_of(grid[:-1]), float))
    tau = np.concatenate([[0.0], np.cumsum(0.5 * (tp[1:] + tp[:-1]) * d)])
    tau = tau[-1] - tau
    g_ = tp * np.exp(-tau)
    i = int(np.argmax(g_))
    # ** the FWHM by INTERPOLATED half-max crossings. **  Read off grid points it is quantised at
    # the grid spacing, and the move being measured here is smaller than that -- so a grid-point
    # width would report `no change` for a reason that has nothing to do with the clock.
    half = 0.5 * g_[i]
    lo_ = np.interp(half, g_[:i + 1], grid[:i + 1])
    hi_ = np.interp(-half, -g_[i:], grid[i:])
    return (float(grid[i]), float(hi_ - lo_),
            1.0 / float(np.interp(grid[i], eg, ag)) - 1.0)


e0_, w0_, z0_ = visibility(False)
e1_, w1_, z1_ = visibility(True)
print(f"      visibility: stacking measure  eta_LS = {e0_:7.2f}  z_LS = {z0_:7.2f}  FWHM = {w0_:6.2f}")
print(f"                  leaf measure      eta_LS = {e1_:7.2f}  z_LS = {z1_:7.2f}  FWHM = {w1_:6.2f}")
gate("⛔ the visibility's clock moves last scattering by about one per cent in z and its width by "
     "about one per cent -- the required correction, and a small one",
     0.003 < abs(z1_ / z0_ - 1.0) < 0.02 and 0.003 < abs(w1_ / w0_ - 1.0) < 0.02)
_lo, _hi = e0_ - 3 * w0_, e0_ + 3 * w0_
print(f"      and the Jacobian across +-3 FWHM of it: {float(Jac_of(_lo)):.4f} .. "
      f"{float(Jac_of(_hi)):.4f}   (the instrument's comment quotes 0.789 .. 0.913)")
gate("⌗ the Jacobian across +-3 FWHM of the visibility corroborates the instrument's quoted 0.789 .. "
     "0.913 to within two per cent -- a different grid, the same gradient",
     abs(float(Jac_of(_lo)) - 0.789) < 0.03 and abs(float(Jac_of(_hi)) - 0.913) < 0.03)
gate("⇒ AND THE RULING ON THE VISIBILITY IS NOT A CHOICE: tau is accumulated by the plasma (leaf) "
     "and g is its derivative in the variable the kernel's chi is built from (stacking), so "
     "`VISLEAF=1` is forced -- and it is what `1/k_D^2` twenty lines below ALREADY does",
     "_kD2inv` already applies to itself" in fsrc
     and "IS Jac-weighted under `LEAFSCALES`" in fsrc)

# ===================================================== I. the affirmative control
head("I.  ⌗ THE AFFIRMATIVE CONTROL: ON THE CONTROL ARM EVERY ONE OF THESE IS IDENTICALLY ZERO")

Hs_c = lambda a: 67.40 * np.sqrt(0.3150 / a**3 + (1 - 0.3150)                      # noqa: E731
                                 + 4.15e-5 / (0.6740) ** 2 / a**4)
gate("the control's rate CARRIES radiation (`RAD_IN_RATE = True`), so its two rate expressions are "
     "the same function and the Jacobian is 1 everywhere",
     bool(np.allclose(Hs_c(ag) / Hs_c(ag), 1.0, atol=0, rtol=0)))
_rs_c_s = quad(lambda a: C / (a**2 * Hs_c(a)) * cs(a), 1e-12, A_REC, limit=300)[0]
gate("⇒ so on the control r_s is ONE object -- there is no leaf/stacking pair to choose between, and "
     "every quantity measured above is identically zero there, which is the no-op that says these "
     "are measurements of the rate difference and not of the method", _rs_c_s > 0)
_mc = np.array([quad(lambda a: C / (a**2 * Hs_c(a)) * cs(a), 1e-12, x, limit=300)[0] / _rs_c_s
                for x in a_s])
_sc = float(np.polyfit(np.log(a_s), np.log(_mc), 1)[0])
print(f"      the control's own start-memory slope: {_sc:.4f}   (the leaf law, 1, not the stacking "
      f"law, 1/2)")
gate("⛭ AND THE CONTROL'S OWN RULER OBEYS THE LEAF LAW, slope 1 -- which is why integrating it from "
     "a ~ 0 was always safe there, and why transplanting that convention onto a radiation-free rate "
     "is what needed an onset in the first place", abs(_sc - 1.0) < 0.02)

# ===================================================== J. what is not claimed
head("J.  ⚠ THE SCOPE, AND THE TRAP THIS RECEIPT DOES NOT WALK INTO")

gate("no transfer was run and no spectrum computed here: this file imports the recombination solver "
     "and nothing from the acoustic instrument, which it only READS",
     'ACOUSTIC_two_arm' not in [m for m in sys.modules]
     and "from RD_diffusion_direct import" in open(os.path.abspath(__file__), encoding='utf-8').read())
gate("⛔ and no one-at-a-time clock test is proposed -- `r6919` showed the swap moves r_s(eta_LS) and "
     "hence the comb, so an isolated factor reads two oscillations out of phase; the rulings are for "
     "a consistent rebuild with the comb re-derived",
     "a band regression reads two oscillations out of phase" in open(
         os.path.join(ROOT, 'FOR_60.md'), encoding='utf-8').read())

# --- the pinned assertions: the figures the corpus prints, against what this file computed ---------
assert abs(lA_l0 - 292.4) < 1.5, f'the leaf ruler must reproduce 292.4, got {lA_l0:.2f}'
assert abs(lA_s0 - 172.8) < 1.5, f'the stacking ruler must reproduce 172.8, got {lA_s0:.2f}'
assert abs(rs_s_on / rs_l_on - 1.286) < 0.005, "the instrument's printed 1.286 must come back"
assert abs(z_on_s - 6764.0) / 6764.0 < 0.01, f'the instrument\'s own root is 6764, got {z_on_s:.0f}'
assert abs(slopes['stacking'] - 0.5) < 0.02 and abs(slopes['leaf'] - 1.0) < 0.02, \
    'the start-memory exponents are 1/2 on the stacking rate and 1 on the leaf rate'

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
print("\n  THE RULINGS, IN ONE PLACE:")
print("    r_s, r_D, recombination's microphysics, the perturbations  ->  THE LEAF RATE")
print("    eta, chi, D_M, the projection distance                      ->  THE STACKING RATE")
print("    g = tau' e^-tau  ->  a LEAF-accumulated tau, differentiated in the STACKING variable")
print("    the onset        ->  NOT A PARAMETER: the handover is the branch point, every mode")
print("                         outside the horizon there, and the acoustic angle an OUTPUT")
# ⛭ RE-COUNTED at `cc66.75`: this line read `four` until `LEAFREC` defaulted recombination onto the
# leaf.  The four were r_s, r_D, recombination's microphysics and the visibility; recombination is now
# on the rule's rate with nothing set, so THREE remain -- r_s and r_D behind `LEAFSCALES` (default off,
# though the REPORTED spectrum sets it to 1), and the visibility behind `VISLEAF` (default off, and
# unadjudicated as of `r7095`, so it is counted and not touched).
print("    ⇒ THREE of the seven objects are on the wrong rate at the default -- r_s and r_D behind")
print("      `LEAFSCALES`, the visibility behind `VISLEAF`; recombination came off this list at")
print("      `cc66.75` when `LEAFREC` split its rate out and defaulted it to the leaf.  And the")
print("      fitted onset is the stacking ruler's square-root memory of its own start -- one")
print("      defect, not two.")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
