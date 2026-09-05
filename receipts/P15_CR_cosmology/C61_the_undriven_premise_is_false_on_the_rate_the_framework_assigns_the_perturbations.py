#!/usr/bin/env python3
r"""
C61 — ** PO-13's DIAGNOSIS RESTS ON A CROSSING CENSUS, AND THE CENSUS COMES OUT THE OTHER WAY ON THE
RATE THE FRAMEWORK ASSIGNS THE PERTURBATIONS.  ** The first peak's mode is SUPER-horizon at the onset
on the leaf rate and enters at $z=5590$, above the leaf's own equality at $z_{\rm eq}=3936$ --- so it
crosses while there is a plasma AND while radiation dominates, which is what the diagnosis says no mode
does.

** WHAT THE DIAGNOSIS SAYS. **  `P07` `sec:frontiers` (`corpus/CR_framework.tex`), in the paragraph that
opens "with the perturbations computed on the leaf congruence the framework assigns them to":

    *"the standard shift that carries it is universal only where every mode crosses the horizon while
    there is a plasma to be driven, and **on this rate the acoustic modes re-enter above the onset, so
    none of them does**."*

and `PO13_WORKING_STATE` states the same thing as the structural reason the arm cannot reach the sky:
*"the CR comb is UNDRIVEN by the established mechanism (modes sub-horizon at the late onset
$z_{\rm onset}\approx6797$, **never cross while there is a plasma** -> the undriven phase)."*

** WHY IT HAD TO BE CHECKED.  ** `r3409` made `LEAFPERT` the default: the perturbation sector runs on
the LEAF congruence, which is what `P15` `sec:properframe` and `P07`'s rate rule assign it --- *"a
process running in the content --- $r_s$, $r_D$, recombination, THE PERTURBATIONS --- takes the
leaf's"*.  ** And `Hleaf` carries the radiation term where the CR stacking rate does not. **  Horizon
crossing FOR THE DRIVING is a perturbation-sector event, so the census that decides the diagnosis has to
be run on the leaf rate.  `r4107` suspected the premise might not survive that and said so; this
measures it.

** THE CENSUS.  ** Both rates, same instrument, `ARM=cr`, everything from the instrument's own splines.

                                            leaf rate            stacking rate (L1)
      radiation in the rate                 YES                  no
      equality                              z_eq = 3936          NONE — there is no equality
      aH/c at the onset (1/Mpc)             0.01828              0.01109
      band entering AFTER the onset         l < 237.7            l < 144.2
      of those, entering in radiation       155.6 < l < 237.7    empty, necessarily
      the reported first peak, l_1 = 204    k/aH = 0.858         k/aH = 1.415
                                            SUPER-horizon,       SUB-horizon,
                                            enters at z = 5590   already inside at the onset

*** => THE TWO RATES GIVE OPPOSITE ANSWERS FOR THE SAME MODE, AND THE DIAGNOSIS IS STATED ON THE ONE
THE FRAMEWORK DOES NOT ASSIGN THE PERTURBATIONS. ***  *On the stacking rate the sentence is TRUE and
its "none of them does" is exact --- there is no equality on that background, so no mode can cross
during radiation domination at any onset.  On the leaf rate it is FALSE for a band that CONTAINS the
peak the arm reports.*

⌗ ** AND THIS REPRODUCES A NUMBER ALREADY IN THE RECORD WITHOUT ITS CONSEQUENCE BEING DRAWN. **
`r3733` measured that on the leaf the $\ell=220$ mode sits at $k/k_{\rm hor}=0.92$ --- outside the
horizon at the onset.  This receipt gets $0.926$.  ** That measurement is the premise's refutation and
was recorded as a caveat. **

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** This refutes a PREMISE.  It does not measure the driving's SIZE **, and it does not claim the
    acoustic residual is explained, reduced or removed.  The instrument's own `NODRIVE=1` subtraction
    is what measures the size and it is not run here.
  · ** It does not touch the position deficit itself. **  The converged CR arm reports
    $\ell_1/\ell_A=0.6764$ against the sky's $0.7312$; that number is what it is either way.
  · ** It is not a verdict on `P07`'s sentence. **  "This rate" is ambiguous in that paragraph between
    the stacking rate the section is about and the leaf rate the same paragraph names, and the sentence
    is true on the first.  What is established is that the reading which supports the diagnosis is the
    one the rate rule does not select.
  · NOT CLAIMED: anything about `z_onset` as a fitted parameter, about the alternation, or about the
    Hubble-tension join that `P07` makes in the next sentence.

** COMPUTES: on ARM=cr, from the instrument's own background splines -- the leaf and stacking comoving
  Hubble rates at the onset; the leaf background's matter-radiation equality; the multipole bands that
  enter the horizon after the onset on each rate; and, for the reported first peak, which side of the
  horizon it is on at the onset and its entry redshift against equality.  No Boltzmann evolution and no
  spectrum is computed here. **

STATUS: ✔✔
RUN: python3 C61_the_undriven_premise_is_false_on_the_rate_the_framework_assigns_the_perturbations.py
RUNTIME: ~20 s (background splines only)
ORIGIN: built r4124 (node 60) on PO-13 RUN 1, answering the question `PO13_RUN_SPEC_FOR_CC54` names as
  the most important the run can return.
"""
import io
import contextlib
import importlib.util
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78
FAIL = []


def check(cond, msg):
    print(("  ✔ " if cond else "  ✘ ") + msg)
    if not cond:
        FAIL.append(msg)


_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.normpath(os.path.join(_HERE, '..', '..'))
_INSTR = os.path.join(_ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
assert os.path.exists(_INSTR), _INSTR

# =====================================================================================
print(BAR); print("PART 1 — THE TWO SENTENCES, QUOTED FROM THE FILES THAT CARRY THEM"); print(BAR)
P07 = open(os.path.join(_ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8').read()
WS = open(os.path.join(_ROOT, 'PO13_WORKING_STATE.md'), encoding='utf-8').read()
q07 = ("crosses the horizon while there is a plasma to be driven, and on this rate the acoustic "
       "modes re-enter\nabove the onset, so none of them does.")
qws = "never cross while there is a plasma"
check(q07 in P07, "P07 sec:frontiers carries \"...on this rate the acoustic modes re-enter above the "
                  "onset, so none of them does\"")
check(qws in WS, f"PO13_WORKING_STATE carries {qws!r}")
check("the perturbations computed on the leaf\ncongruence the framework assigns them to" in P07,
      "and the SAME paragraph names the leaf congruence as where the framework puts the perturbations")

# =====================================================================================
print(); print(BAR); print("PART 2 — THE INSTRUMENT'S OWN BACKGROUND, ARM=cr"); print(BAR)
os.environ['ARM'] = 'cr'
os.environ.setdefault('NK', '260')
_spec = importlib.util.spec_from_file_location("ACOUSTIC_two_arm_c61", _INSTR)
AT = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(AT)

check(AT.LEAFPERT, "LEAFPERT is ON by default (r3409) — the perturbations run on the leaf congruence")
check(not AT.RAD_IN_RATE, "and RAD_IN_RATE is OFF on this arm — the STACKING rate is radiation-free")
# `Hleaf` is the leaf rate; it carries OR/a^4 where the CR stacking rate does not.  Read it, do not
# assume it: evaluate both at one early scale factor and see which one the radiation term moves.
_a = 1e-4
_leaf = float(AT.Hleaf(_a))
_stack = float(AT.H0 * np.sqrt(AT.OM / _a ** 3 + AT.OL))
check(abs(_leaf / _stack - 1.0) > 0.5,
      f"at a = 1e-4 the leaf rate is {_leaf/_stack:.3f}x the radiation-free rate — the leaf carries "
      f"the radiation term and the stack does not")

eg, ag = AT.eg, AT.ag
khL = np.asarray(AT.Hl_of(eg), float)          # comoving leaf Hubble aH/c, 1/Mpc
khS = np.asarray(AT.Hc_of(eg), float)          # comoving stacking Hubble
D = AT.D_M
z_eq = AT.OM / AT.OR - 1.0
e_eq = float(np.interp(1.0 / (1.0 + z_eq), ag, eg))
kON_L, kON_S = float(AT.Hl_of(AT.ETA_ON)), float(AT.Hc_of(AT.ETA_ON))
k_eq_L = float(AT.Hl_of(e_eq))

print(f"\n    onset:            z = {AT.Z_START:.0f}   eta_ON = {AT.ETA_ON:.2f} Mpc")
print(f"    leaf equality:    z_eq = Om/Or - 1 = {z_eq:.0f}   eta_eq = {e_eq:.2f} Mpc")
print(f"    aH/c at the onset:  leaf {kON_L:.5f}/Mpc    stack {kON_S:.5f}/Mpc   "
      f"(the leaf's is {kON_L/kON_S:.3f}x)")
check(AT.ETA_ON < e_eq,
      f"** THE ONSET PRECEDES EQUALITY ON THE LEAF BACKGROUND ** (eta {AT.ETA_ON:.1f} < {e_eq:.1f}), "
      f"so there is a radiation-dominated stretch of plasma at all")

# =====================================================================================
print(); print(BAR); print("PART 3 — THE CROSSING CENSUS, BOTH RATES"); print(BAR)
# ** aH/c FALLS through radiation and matter domination.  A mode is SUPER-horizon while k < aH/c and
#    ENTERS at the first eta where aH/c has fallen to k. **  Entry AFTER the onset therefore means
#    k < aH/c(eta_ON), which is the band this census is about.
print(f"\n    {'rate':>10} {'enters after the onset':>26} {'of those, in radiation':>26}")
print(f"    {'leaf':>10} {'l < %.1f' % (kON_L * D):>26} {'%.1f < l < %.1f' % (k_eq_L*D, kON_L*D):>26}")
print(f"    {'stack':>10} {'l < %.1f' % (kON_S * D):>26} {'EMPTY — no equality exists':>26}")
check(kON_L * D > 200.0,
      f"on the LEAF rate every multipole below l = {kON_L*D:.1f} enters AFTER the onset")
check(k_eq_L * D < 204.0 < kON_L * D,
      f"and the radiation-dominated crossing band {k_eq_L*D:.1f} < l < {kON_L*D:.1f} CONTAINS the "
      f"converged first peak at l_1 = 204")

print()
print(f"    {'l':>6} {'k (1/Mpc)':>11} {'k/aH(onset) leaf':>18} {'z_entry (leaf)':>16} {'in radiation?':>14}")
for l in (100, 155, 204, 220, 237, 300, 516, 828, 1188):
    k = l / D
    i = np.nonzero(khL <= k)[0]
    z_in = 1.0 / float(np.interp(eg[i[0]], eg, ag)) - 1.0 if len(i) else float('nan')
    e_in = float(eg[i[0]]) if len(i) else float('nan')
    tag = 'YES' if (e_in > AT.ETA_ON and e_in < e_eq) else ('before onset' if e_in <= AT.ETA_ON else 'no')
    print(f"    {l:>6} {k:>11.5f} {k/kON_L:>18.3f} {z_in:>16.0f} {tag:>14}")

k1 = 204.0 / D
i1 = np.nonzero(khL <= k1)[0][0]
z1 = 1.0 / float(np.interp(eg[i1], eg, ag)) - 1.0
check(k1 / kON_L < 1.0,
      f"l_1 = 204 on the LEAF rate: k/aH(onset) = {k1/kON_L:.3f} < 1 — SUPER-horizon at the onset, "
      f"so it enters while there is a plasma")
check(z1 > z_eq,
      f"and it enters at z = {z1:.0f}, ABOVE the leaf's equality z_eq = {z_eq:.0f} — "
      f"a radiation-dominated crossing")
check(k1 / kON_S > 1.0,
      f"l_1 = 204 on the STACKING rate: k/aH(onset) = {k1/kON_S:.3f} > 1 — SUB-horizon at the onset, "
      f"already inside, exactly as the diagnosis says")
# ** the stacking rate carries no radiation, so it has no equality.  Test that, do not say it:
#    H_stack^2/H0^2 must equal Om/a^3 + OL to machine precision at a scale factor where the
#    radiation term would dominate by two orders of magnitude if it were there. **
_a4 = 1e-6
_hs2 = (float(AT.Hphys(_a4)) / AT.H0) ** 2
_free2 = AT.OM / _a4 ** 3 + AT.OL
_rad_share = (AT.OR / _a4 ** 4) / _free2
check(abs(_hs2 / _free2 - 1.0) < 1e-12 and _rad_share > 100.0,
      f"the stacking rate at a = 1e-6 is Om/a^3 + OL to {abs(_hs2/_free2 - 1.0):.1e}, where a "
      f"radiation term would have been {_rad_share:.0f}x the rest — it carries none, so that "
      f"background has NO equality and no mode can cross in radiation on it at any onset")

# ⌗ r3733's number, reproduced rather than cited.
k220 = 220.0 / D
check(abs(k220 / kON_L - 0.92) < 0.02,
      f"r3733's leaf reading for l = 220 reproduces: k/k_hor = {k220/kON_L:.3f} against its 0.92")

# =====================================================================================
print(); print(BAR)
if FAIL:
    print(f"⛔ {len(FAIL)} CHECK(S) FAILED")
    for m in FAIL:
        print("   - " + m)
    print(BAR)
    sys.exit(1)
print("""VERDICT.  ** The premise the PO-13 diagnosis rests on is false on the rate the framework
assigns the perturbations. **  On the leaf congruence -- `LEAFPERT`, the default since r3409, and what
`P15` sec:properframe and `P07`'s rate rule both assign the perturbation sector -- the CR background
HAS a matter-radiation equality, at z = 3936; the onset at z = 6761 PRECEDES it; every multipole below
l = 238 is still super-horizon when the plasma starts; and the band 156 < l < 238, which contains the
first peak the converged arm reports at l = 204, enters the horizon while radiation still dominates.
** Those modes cross while there is a plasma to be driven, and they are driven. **

** THE SENTENCE IS TRUE ON THE OTHER RATE, AND THAT IS THE POINT. **  On the stacking rate there is no
equality at all, so "none of them does" is not merely true but necessary -- and l_1 is already inside
the horizon at the onset.  ** The diagnosis was stated on the rate that carries the ruler and tested
against a spectrum computed on the rate that carries the content. **

** WHAT IS NOT ESTABLISHED, AND IT IS THE NEXT MEASUREMENT. **  How large the driving these modes
receive actually is.  A premise refuted is not a mechanism measured: the instrument's `NODRIVE=1` guard
runs the same equations with the driving removed, and the difference between the two runs is the only
honest answer to that.  ** The position deficit itself is unmoved by anything here: the converged arm
reports l_1/l_A = 0.6764 against the sky's 0.7312 whichever way the premise falls. **""")
print(BAR)
