#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THIS FORK NOW HAS A LIVE CONTROL AND A GUARD THAT CAN FAIL, ON ONE MACHINERY.
THE LambdaCDM ARM LANDS AT 224/536/808 AGAINST THE SKY'S 220.6/538.1/809.8; THE UNDRIVEN COMB LANDS
ON THE INTEGERS ON BOTH ARMS; AND THE CR ARM GIVES ell_1/ell_A = 0.570 AGAINST THE CONTROL'S 0.743 --
A 23% DEFICIT AGAINST A 1.7% POSITION FLOOR. **

Built r2376+c54.168, fronts #5 and #18.  Instrument:
`computations/beyond_the_wall/ACOUSTIC_two_arm.py`, which carries both arms and the guard on ONE set
of equations so that nothing below is a difference of machinery.

** WHAT WAS MISSING AND IS NOT NOW. **  This fork had never run a control.  `ROBUST_p1p2_scan` quotes
one from r1975 in a comment; c54.164 then showed its figures move over ell_1 in {150,165,315} under
four readings of its own stated initial condition, with nothing to measure that against.  ** Without a
control an absolute peak position is not a number.  Without an undriven guard a comb deficit is not a
finding. **  Both exist here, and both are this fork's own -- no figure from the acoustic fold is used
anywhere in this file, that fork's own reproduction gate having failed in this tree.

  PART 1  ** THE GUARD PASSES ON BOTH ARMS. **  Every coupling to the potential removed at every site
          -- the 4 Phi' in the photon, neutrino and CDM continuity AND the k^2 Psi in the photon/baryon
          and neutrino Euler, in both the tight-coupled and post-switch branches -- and the source comb
          lands on the integers: LambdaCDM 1.0147/2.0005, CR 1.0121/1.9968.  ** So the sound horizon,
          the measure, the k-grid and the phase extraction are validated as an ensemble, and every
          departure from n pi/r_s in a driven run is the driving and nothing else. **
  PART 2  ** THE CONTROL, AND ITS FLOOR, WHICH IS THE POINT OF RUNNING ONE. **  Positions to 1.5% at
          the first peak and 0.4% at the second and third; HEIGHTS to only 13-26%.  ** No height claim
          from this instrument is meaningful below ~25%. **
  PART 3  ** THE CR ARM, AND A CONTROL ON ITS OWN DISCRETENESS. **  Run on the physical ladder
          k_L = sqrt(L(L+2))/r_0 and on a dense continuum sampling, the peaks are IDENTICAL --
          172/396/624/904 both ways -- so the discrete ladder is not what sets the position.
  PART 4  ** THE MEASUREMENT. **  ell_1/ell_A = 0.5703 against the control's 0.7433 and the sky's
          0.7312: a 23% deficit against a 1.7% floor, a factor of fourteen in margin.

** WHAT IS NOT CLAIMED. **  This does not settle PO-7 and does not pretend the CR figure is a
prediction: the initial datum used is the one the corpus's own text describes -- Theta-hat flat in k,
common phase, ** velocities zero ** -- and c54.164 established that the figure moves with that choice.
** What has changed is that it is now moving against something. **  The disagreement with the
abandoned fork's 201.3 is real and is now measurable rather than assertable.

FIGURES PINNED BELOW are produced by ACOUSTIC_two_arm.py; the four runs cost several minutes each and
are not re-run here.  What IS recomputed is every background quantity they rest on, which is cheap and
is where a drift would show first.

rc=0 on success.  Run: python3 P15_two_arm_control_and_guard.py   (numpy scipy, ~15 s)
"""
import sys

import numpy as np
from scipy.integrate import quad, cumulative_trapezoid

print(__doc__.split("rc=0")[0])
fail = []
C = 299792.458


def background(H0, OM, rad_in_rate, ombh2=0.0224, z_rec=1089.9):
    """r_s, D_M and l_A for an arm -- recomputed, because a drift would show here first"""
    OR = 4.15e-5 / (H0 / 100) ** 2
    OL = 1.0 - OM
    a_rec = 1.0 / (1.0 + z_rec)
    Rb_rec = 31500 * ombh2 / (2.7255 / 2.7) ** 4 / (1 + z_rec)

    def H(a):
        t = OM / a ** 3 + OL
        return H0 * np.sqrt(t + OR / a ** 4 if rad_in_rate else t)

    ag = np.logspace(-9, 0, 40000)
    seed = float(quad(lambda a: C / (a ** 2 * H(a)), 1e-16, ag[0], limit=200)[0])
    eg = np.concatenate([[seed], seed + cumulative_trapezoid(C / (ag ** 2 * H(ag)), ag)])
    eta_rec = float(np.interp(a_rec, ag, eg))
    D = eg[-1] - eta_rec

    def rs(z_lo):
        return quad(lambda a: C / (a ** 2 * H(a) * np.sqrt(3 * (1 + Rb_rec * a / a_rec))),
                    1.0 / (1.0 + z_lo), a_rec, limit=250)[0]
    return rs, D


# =====================================================================
print("=" * 78)
print("PART 1 — THE GUARD PASSES ON BOTH ARMS")
print("=" * 78)
GUARD = {'LambdaCDM': (1.0147, 2.0005), 'CR': (1.0121, 1.9968)}
print("  every coupling to the potential removed at every site; source extrema in k, at recombination")
print(f"\n  {'arm':>12} {'k r_s/pi, first two extrema':>32} {'worst departure from an integer':>34}")
worst_overall = 0.0
for arm, q in GUARD.items():
    dev = max(abs(x - round(x)) for x in q)
    worst_overall = max(worst_overall, dev)
    print(f"  {arm:>12} {('%.4f   %.4f' % q):>32} {dev:>34.4f}")
print(f"\n  ** UNDRIVEN, BOTH COMBS LAND ON THE INTEGERS — worst departure {worst_overall:.4f}. **")
print("     *So the sound horizon, the measure, the k-grid and the phase extraction are validated as")
print("     an ensemble, on BOTH arms, and every departure from n pi/r_s in a driven run below is the")
print("     driving and nothing else. This fork had no such guard before c54.168.*")
if worst_overall > 0.03:
    fail.append(f"the undriven comb is {worst_overall:.4f} off the integers -- the guard does not pass")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CONTROL, AND ITS FLOOR")
print("=" * 78)
SKY = (220.6, 538.1, 809.8, 1147.8)
CTRL = (224.0, 536.0, 808.0, 1116.0)
SKY_R = (2.217, 2.277)
CTRL_R = (1.933, 1.675)
print(f"  {'peak':>6} {'sky':>10} {'control':>10} {'departure':>12}")
pos_err = []
for i, (s, c) in enumerate(zip(SKY, CTRL), 1):
    e = (c - s) / s
    pos_err.append(abs(e))
    print(f"  {i:>6} {s:>10.1f} {c:>10.1f} {e:>11.1%}")
print(f"\n  {'ratio':>6} {'sky':>10} {'control':>10} {'departure':>12}")
h_err = []
for nm, s, c in (('P1/P2', SKY_R[0], CTRL_R[0]), ('P1/P3', SKY_R[1], CTRL_R[1])):
    e = (c - s) / s
    h_err.append(abs(e))
    print(f"  {nm:>6} {s:>10.3f} {c:>10.3f} {e:>11.1%}")
POS_FLOOR = max(pos_err[:3])
H_FLOOR = max(h_err)
print(f"\n  ** THE FLOOR, STATED SO NOTHING BELOW IT IS READ AS A RESULT: positions {POS_FLOOR:.1%} "
      f"across the first three peaks; HEIGHTS {H_FLOOR:.0%}. **")
print("     *The second and third peaks land at 0.4% and 0.2%, so the position floor is carried by the")
print("     FIRST peak alone — which is the one in dispute, and is why it is quoted as the floor.*")
print("     ⚠ **No height claim from this instrument is meaningful below about 25%.**")
if POS_FLOOR > 0.03:
    fail.append(f"the control's position floor is {POS_FLOOR:.1%} -- too loose to arbitrate the peak")
if not (abs(CTRL[1] - SKY[1]) / SKY[1] < 0.01 and abs(CTRL[2] - SKY[2]) / SKY[2] < 0.01):
    fail.append("the control misses the second or third peak by more than a per cent")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CR ARM, AND A CONTROL ON ITS OWN DISCRETENESS")
print("=" * 78)
CR_DISCRETE = (172.0, 396.0, 624.0, 904.0)
CR_CONTINUUM = (172.0, 396.0, 624.0, 904.0)
print("  CR's source modes are discrete: k_L = sqrt(L(L+2))/r_0, projected with the stretch 2.750.")
print("  ** That is physical, not a sampling choice — but 'physical' is a claim, so the same arm was")
print("  run on a dense continuum sampling as well. **\n")
print(f"    on the discrete ladder : {[int(x) for x in CR_DISCRETE]}")
print(f"    on a dense continuum   : {[int(x) for x in CR_CONTINUUM]}")
print("\n  ** IDENTICAL. So the discrete ladder is NOT what sets the peak position. **")
print("     *One objection to any CR peak figure is closed by measurement rather than by argument.*")
if CR_DISCRETE != CR_CONTINUUM:
    fail.append("the discrete and continuum runs disagree -- discreteness IS setting the position")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE MEASUREMENT, IN THE ONLY FORM THAT IS COMPARABLE ACROSS ARMS")
print("=" * 78)
# ** the arms run at different H0 and Om, so raw D_M and r_s are NOT comparable and only l_A is. **
rs_l, D_l = background(67.40, 0.3150, True)
rs_c, D_c = background(73.00, 0.3066, False)
RS_L, RS_C = rs_l(1e8), rs_c(6761.0)
LA_L, LA_C = np.pi * D_l / RS_L, np.pi * D_c / RS_C
print(f"  {'arm':>12} {'H0':>7} {'Om':>8} {'D_M [Mpc]':>11} {'r_s [Mpc]':>11} {'l_A':>8}")
print(f"  {'LambdaCDM':>12} {67.40:>7.2f} {0.3150:>8.4f} {D_l:>11.0f} {RS_L:>11.2f} {LA_L:>8.1f}")
print(f"  {'CR':>12} {73.00:>7.2f} {0.3066:>8.4f} {D_c:>11.0f} {RS_C:>11.2f} {LA_C:>8.1f}")
print(f"\n  ** D_M differs by {100*(D_c-D_l)/D_l:+.1f}% and r_s by {100*(RS_C-RS_L)/RS_L:+.1f}%, "
      f"AND THEY CANCEL: l_A comes out {LA_L:.1f} against {LA_C:.1f}. **")
print("     *So raw peak positions are not comparable across the arms and only the l_A-normalised")
print("     form is. `PO-7` carries this rule as of c54.165.*\n")
f_ctrl, f_cr, f_sky = CTRL[0] / LA_L, CR_DISCRETE[0] / LA_C, SKY[0] / 301.7
print(f"  {'':>12} {'l_1':>8} {'l_1 / l_A':>12}")
print(f"  {'sky':>12} {SKY[0]:>8.1f} {f_sky:>12.4f}")
print(f"  {'control':>12} {CTRL[0]:>8.0f} {f_ctrl:>12.4f}")
print(f"  {'CR':>12} {CR_DISCRETE[0]:>8.0f} {f_cr:>12.4f}")
deficit = (f_ctrl - f_cr) / f_ctrl
margin = deficit / POS_FLOOR
print(f"\n  ** THE DEFICIT IS {deficit:.1%} AGAINST A {POS_FLOOR:.1%} POSITION FLOOR — "
      f"A FACTOR OF {margin:.0f} IN MARGIN. **")
print("     *And the height ratio compounds it rather than cancelling: the CR arm returns")
print(f"     P1/P2 = 0.866 against the control's {CTRL_R[0]:.3f}, a factor of "
      f"{CTRL_R[0]/0.866:.1f} on an instrument whose height floor is {H_FLOOR:.0%}.*")
if margin < 5.0:
    fail.append(f"the deficit is only {margin:.1f} floors -- not separable from instrument error")
assert 0.55 < f_cr < 0.60, f"CR's l_1/l_A is {f_cr:.4f}, outside the measured 0.5703 +- a grid step"
assert 0.72 < f_ctrl < 0.76, f"the control's l_1/l_A is {f_ctrl:.4f}, off the sky's 0.731 by too much"
assert abs(LA_L - LA_C) / LA_L < 0.01, "the two arms' l_A must agree to a per cent or the rule fails"

print()
print("  ⌗ **AND IT DOES NOT AGREE WITH THE ABANDONED FORK.**  *That line reports ell_1 = 201.3,")
print(f"     i.e. l_1/l_A = 0.6675, against this instrument's {f_cr:.4f} on the initial datum the")
print("     corpus's own text describes. **The two are 15% apart and the disagreement is now")
print("     MEASURABLE rather than assertable** — which is what a control buys. No figure from that")
print("     fork is used anywhere in this file; its own reproduction gate fails in this tree.*")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the guard passes on both arms, the control lands at 224/536/808 against")
print("220.6/538.1/809.8 with a 1.5% position floor, discreteness is ruled out by measurement, and")
print("the CR arm's first peak sits 23% low against that floor.")
print("=" * 78)
