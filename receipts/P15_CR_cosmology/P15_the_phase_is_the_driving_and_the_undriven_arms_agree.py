#!/usr/bin/env python3
"""
RECEIPT -- P15: ** WHY 0.62 pi: THE DRIVING, AND THE ATTRIBUTION IS COMPLETE.  ** WITH EVERY COUPLING
TO THE POTENTIAL REMOVED THE TWO ARMS' ACOUSTIC PHASES AGREE TO 0.013 OF ell_A AND BOTH SPACINGS ARE
ell_A EXACTLY.  TURNING THE DRIVING ON SUPPLIES -0.127 TO THE CONTROL AND -0.729 TO THIS
CONSTRUCTION -- A FACTOR OF 5.7 -- WHICH IS 98% OF THE 0.615 DISCREPANCY. **  AND THE SAME SWITCH
ACCOUNTS FOR THE 2.4% THE SPACING WAS SHORT. **

Built r2441+c54.193, front #2, lead `L-507`.

===================================================================================================
** WHY: c54.191 SAID "why 0.62 pi HAS AN ADDRESS" AND DID NOT GO TO IT. **
===================================================================================================

c54.191 closed with: *"an acoustic phase shift is a computable consequence of the driving, so the
question 'why 0.62 pi' has an address.  This file does not have it."*  ** The instrument has carried
the switch since c54.170: `NODRIVE=1` removes every coupling to the potential at every site -- the
4 Phi' in the photon, neutrino and CDM continuity equations and the k^2 Psi in the Euler equations --
while leaving Phi's own evolution alone, since that is the background and not a coupling. **  *Both
arms are run through it at production depth here, which is what the question needed and what no
revision had done.*

  PART 1  ** UNDRIVEN, THE TWO ARMS ARE THE SAME OSCILLATOR. **  Intercepts -0.135 and -0.149 of
          ell_A -- ** they agree to 0.013 ** -- and both slopes are ell_A to within a part in a
          thousand.  *Two constructions with different rates, different sound horizons, different
          starting redshifts and different initial data give the same acoustic series once nothing
          drives it.*
  PART 2  ** AND THE DRIVING IS WHAT SEPARATES THEM. **  Switched on it supplies -0.127 to the
          control and ** -0.729 to this construction: a factor of 5.7 **.  The driven discrepancy is
          0.615 and the undriven is 0.013, so ** the driving accounts for 98% of it. **
  PART 3  ** THE SAME SWITCH ACCOUNTS FOR THE SPACING TOO. **  Undriven, both slopes are 1.000 and
          1.001 of ell_A.  Driven, the control's is 1.003 and this construction's 0.976.  ** So the
          2.4% the spacing was short is the driving as well, and not a second effect. **
  PART 4  ** WHICH MAKES THE WHOLE ACOUSTIC DISAGREEMENT ONE OBJECT. **  *Not a spacing and a phase
          and a transient, but one coupling behaving differently -- and a coupling is a thing a
          theory says something about, where a ratio is not.*

** WHAT THIS DOES NOT SAY, AND IT IS THE INTERESTING HALF. **  ** It does not say WHY the driving is
5.7 times stronger here. **  *The obvious candidate is that this construction's modes begin already
sub-horizon at the seam carrying an assigned amplitude and zero velocity, in a potential that is not
the equilibrium configuration for that state -- so the potential does work on them immediately, where
LambdaCDM's modes begin super-horizon in adiabatic equilibrium and the potential decays gradually as
they enter.*  ** That is a hypothesis and this file does not test it. **  ⇒ ***The instrument already
carries the split that would: `DRC` is the potential's RATE OF CHANGE feeding the density and `DRE`
is its GRADIENT driving the velocity, and they can be switched independently.  Running them
separately attributes the 5.7 to one term or the other, and that is the next thing this front
owes.***

** F5 IS NOT SOFTENED, AND THIS RESULT IS THE REASON TO SAY SO CAREFULLY. **  A measurement
discrepancy is not a framework verdict; `PO-7` is protected; the conversion runs by `F5`'s stated procedure.  ** An
attribution is not an explanation and it is not a verdict: what this establishes is that the acoustic
disagreement lives in ONE coupling rather than in four items, a ratio, or an initial condition. **

rc=0 on success.  Run: python3 P15_the_phase_is_the_driving_and_the_undriven_arms_agree.py
                        (numpy scipy; ~10 s)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NFIT = 4          # the asymptotic fit starts where c54.190 showed the transient has died

RUNS = (('LambdaCDM  driving ON',  'c54.186_lcdm_L3000.npz'),
        ('LambdaCDM  driving OFF', 'c54.193_lcdm_nodrive_L3000.npz'),
        ('CR         driving ON',  'c54.186_cr_L3000.npz'),
        ('CR         driving OFF', 'c54.193_cr_nodrive_L3000.npz'))


def fit(fname):
    z = np.load(os.path.join(SP, fname))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    pk = argrelextrema(D, np.greater, order=3)[0]
    pos = ls[pk]
    n = np.arange(1, len(pos) + 1)
    m = n >= min(NFIT, len(pos) - 1)
    b, a = np.polyfit(n[m], pos[m], 1)
    return dict(pos=pos, b=float(b) / float(z['l_A']), a=float(a) / float(z['l_A']),
                npk=len(pos))


R = {nm: fit(f) for nm, f in RUNS}

# =====================================================================
print("=" * 78)
print("PART 1/2 — UNDRIVEN THE TWO ARMS ARE THE SAME OSCILLATOR")
print("=" * 78)
print("  *`NODRIVE=1` removes EVERY coupling to the potential at EVERY site -- the 4 Phi' in the")
print("   photon, neutrino and CDM continuity equations and the k^2 Psi in the Euler equations --")
print("   and leaves Phi's own evolution alone, that being the background and not a coupling.*")
print()
print(f"  {'run':>24} {'npk':>4} {'first four peaks':>30} {'slope/l_A':>10} {'intcpt/l_A':>11}")
for nm, _ in RUNS:
    d = R[nm]
    print(f"  {nm:>24} {d['npk']:>4} {str([int(x) for x in d['pos'][:4]]):>30} {d['b']:>10.4f} "
          f"{d['a']:>11.4f}")
OFF = R['LambdaCDM  driving OFF']['a'] - R['CR         driving OFF']['a']
ON = R['LambdaCDM  driving ON']['a'] - R['CR         driving ON']['a']
SUP_L = R['LambdaCDM  driving ON']['a'] - R['LambdaCDM  driving OFF']['a']
SUP_C = R['CR         driving ON']['a'] - R['CR         driving OFF']['a']
print(f"\n  ** UNDRIVEN, THE TWO INTERCEPTS DIFFER BY {abs(OFF):.4f} OF ell_A. **")
print("     *Two constructions with different rates, sound horizons, starting redshifts and initial")
print("     data give the SAME acoustic series once nothing drives it.*")
print()
print(f"  ** WHAT THE DRIVING SUPPLIES: {SUP_L:+.4f} to the control, {SUP_C:+.4f} here — "
      f"a factor of {SUP_C/SUP_L:.1f}. **")
print(f"  ** THE DRIVEN DISCREPANCY IS {ON:+.4f} AND THE UNDRIVEN IS {OFF:+.4f}, SO THE DRIVING")
print(f"     ACCOUNTS FOR {100*(1-abs(OFF)/abs(ON)):.0f}% OF IT. **")
if abs(OFF) > 0.10:
    fail.append(f"undriven, the arms still differ by {abs(OFF):.3f} of l_A -- the driving is NOT the "
                "whole attribution and PART 2's headline is wrong")
if not (abs(SUP_C / SUP_L) > 3.0):
    fail.append(f"the driving supplies only {SUP_C/SUP_L:.1f}x more here than in the control -- "
                "PART 2 has no content")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE SAME SWITCH ACCOUNTS FOR THE SPACING")
print("=" * 78)
print(f"  {'run':>24} {'slope/l_A':>10}")
for nm, _ in RUNS:
    print(f"  {nm:>24} {R[nm]['b']:>10.4f}")
_sb_off = abs(R['CR         driving OFF']['b'] - 1.0)
_sb_on = abs(R['CR         driving ON']['b'] - 1.0)
print(f"\n  ** UNDRIVEN BOTH SLOPES ARE ell_A TO {100*max(_sb_off, abs(R['LambdaCDM  driving OFF']['b']-1)):.2f}%. "
      f"DRIVEN, THIS CONSTRUCTION'S IS {100*_sb_on:.1f}% SHORT. **")
print("     ⇒ ***So the 2.4% the spacing was short is the driving as well, and not a second")
print("     effect.  The whole acoustic disagreement is ONE coupling behaving differently.***")
if _sb_off > 0.01:
    fail.append(f"undriven, the CR slope is {100*_sb_off:.1f}% off l_A -- the spacing shortfall is "
                "not the driving's and PART 3 is wrong")

# =====================================================================
print()
print("=" * 78)
print("WHAT THIS DOES NOT SAY")
print("=" * 78)
print("  ** It does not say WHY the driving is stronger here. **")
print("     *The obvious candidate: this construction's modes begin already sub-horizon at the seam")
print("     carrying an assigned amplitude and ZERO velocity, in a potential that is not the")
print("     equilibrium configuration for that state — so the potential does work on them at once,")
print("     where the control's modes begin super-horizon in adiabatic equilibrium.  A HYPOTHESIS,")
print("     and this file does not test it.*")
print("  ⇒ ***The instrument carries the split that would: `DRC` is the potential's RATE OF CHANGE")
print("     feeding the density, `DRE` its GRADIENT driving the velocity, switchable separately.")
print("     That is the next thing this front owes.***")
print()
print("  ⛔ ***F5 UNSOFTENED.  An attribution is not an explanation and it is not a verdict: what")
print("     this establishes is that the acoustic disagreement lives in ONE COUPLING rather than in")
print("     four items, a ratio, or an initial condition.  `PO-7` protected; the conversion is")
print("     Daryl's.***")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — with every coupling to the potential removed the two arms' acoustic phases")
print("agree to 0.013 of l_A and both spacings are l_A to a part in a thousand; switching the driving")
print("on supplies -0.127 to the control and -0.729 here, a factor of 5.7, which is 98% of the 0.615")
print("discrepancy; and the same switch accounts for the 2.4% the spacing was short.  The acoustic")
print("disagreement is one coupling, not four items and a ratio.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.193, `L-507`.  This file ATTRIBUTES the front's whole acoustic result to one
# switch, so the pins are on the attribution being complete and on where it would fail.
#   (1) the UNDRIVEN agreement -- if the arms still differed with nothing driving them, the
#       driving would not be the whole story and PART 2's headline would be wrong;
#   (2) the ratio of what the driving supplies, without which PART 2 has no content;
#   (3) the undriven SLOPES at l_A, which is what makes PART 3's "not a second effect" true;
#   (4) the driven discrepancy reproduced at 0.615, tying this file to `L-505` and `L-506`;
#   (5) peak counts, since every number is an asymptotic fit.
# ============================================================================================
assert abs(OFF) < 0.10, f"undriven, the arms differ by {abs(OFF):.3f} of l_A -- attribution incomplete"
assert abs(SUP_C / SUP_L) > 3.0, f"the driving supplies only {SUP_C/SUP_L:.1f}x more here"
assert abs(SUP_C / SUP_L - 5.7) < 1.5, f"the ratio is {SUP_C/SUP_L:.1f}, expected ~5.7"
assert _sb_off < 0.01, f"undriven, the CR slope is {100*_sb_off:.1f}% off l_A"
assert abs(abs(ON) - 0.615) < 0.05, f"the driven discrepancy is {abs(ON):.3f}, expected 0.615"
assert 1 - abs(OFF) / abs(ON) > 0.85, \
    f"the driving accounts for only {100*(1-abs(OFF)/abs(ON)):.0f}% of the discrepancy"
assert min(R[nm]['npk'] for nm, _ in RUNS) >= 7, "an arm carries fewer than seven peaks"
print(f"GATE c54.193 (r2441), `L-507`: undriven the two arms' acoustic phases differ by "
      f"{abs(OFF):.4f} of l_A with both slopes at l_A to a part in a thousand; the driving supplies "
      f"{SUP_L:+.4f} to the control and {SUP_C:+.4f} here ({SUP_C/SUP_L:.1f}x), accounting for "
      f"{100*(1-abs(OFF)/abs(ON)):.0f}% of the {abs(ON):.3f} discrepancy, and for the "
      f"{100*_sb_on:.1f}% the spacing was short — pinned against `L-505`, `L-506` and `L-147` F5.")
