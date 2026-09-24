#!/usr/bin/env python3
"""
RECEIPT -- P15: ** AN ERROR BUDGET ON THE CROSSING ARM'S DAMPING SIGNATURE, AS `UNC_error_budget`
DOES FOR THE CORPUS'S 13.96%.  ** THE ENTIRE COSMOLOGICAL PARAMETER BUDGET IS 0.02 POINTS.  MOVING
THE r_D ENDPOINT FROM RECOMBINATION (z = 1089.9) TO THE COMPUTED VISIBILITY PEAK (z = 1093.8) --
0.36% IN REDSHIFT -- MOVES IT BY 3.10 POINTS. **

** ⇒ SO THIS SIGNATURE IS NOT A FEW-PER-CENT OBSERVABLE WITH AN ERROR BAR.  ITS VALUE IS SET BY
WHERE THE INTEGRAL STOPS, AND THE TWO DEFENSIBLE STOPPING POINTS -- FOUR PARTS IN A THOUSAND APART
IN REDSHIFT -- STRADDLE ZERO: +2.21% AND -0.89%. **  The cause is structural: r_D's integrand
carries 1/tau', and tau' collapses through recombination, so the last few per mille of the
integration range carry a finite share of the whole integral.

*** AND THAT IS WHY THE INSTRUMENT AND THE STANDALONE INTEGRATION DISAGREED. ***  The instrument's
header reports r_D at its own visibility peak and gives +3.1%; the standalone integration to
recombination gives +2.2%.  ** Neither was wrong and the gap was never a bug: it is this
sensitivity, and it is larger than the signature being claimed. **  `UNC_error_budget` carries no
such term, which is not an omission in it -- on the onset handover with the stacking clock one
endpoint was quoted throughout, so there was no spread to carry.

Built r6760+cc66.6 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order
(message C, smaller item 1: "an error budget on the +3.1% signature, as `UNC_error_budget` does for
the 13.96%").

===================================================================================================
** WHAT IS BEING BUDGETED, AND WHY IT IS NOT THE 13.96% **
===================================================================================================

The observable is theta_D/theta_* = r_D/r_s, relative to the control's.  `sec:coherence` states the
signature as ** +8.2% **, on the ONSET handover and the STACKING clock.  `UNC_error_budget` budgets
a ** 13.96% ** on that same configuration with the `l_D`-anchored r_D.

** This budgets a DIFFERENT number, because the configuration moved. **  On the CROSSING handover
with the LEAF clock -- the pair r6760+cc66.2 measured as the only one of four that lands near the
control -- the signature is a few per cent, and *which* few per cent depends on where r_D stops:

  ** r_D to A_REC ** (recombination, z = 1089.9): the standalone integration's endpoint.
  ** r_D to the visibility peak **: the instrument's own, which is what its header prints.

*Neither is wrong.  They are two definitions of "the diffusion length at last scattering" and the
corpus uses both -- so the SPREAD BETWEEN THEM is a systematic of the quoted number and belongs in
its budget, which is the finding here.*

  PART 1  ** THE CENTRAL VALUE ON EACH CONVENTION, AND THE SENSITIVITY BETWEEN THEM. **
  PART 2  ** THE PARAMETER BUDGET, ** one source at a time, `UNC_error_budget`'s own list.
  PART 3  ** THE CONVENTION TERM BESIDE THEM. **
  PART 4  ** AND THE CONFIGURATION TERMS, which are not uncertainties and are kept apart. **

** COMPUTES: central at H0 = 73.00, Om = 0.3066, Ombh2 = 0.0224, z_rec = 1089.9, Yp = 0.2454 --
   `ACOUSTIC_two_arm.py`'s own; control at H0 = 67.40, Om = 0.3150 with radiation in its rate.
   The excursions are `UNC_error_budget`'s: H0 +/- 1.0 (SH0ES), Om +/- 0.006 (BAO), Ombh2 +/- 0.0005
   (BBN), z_rec +/- 0.11% (Peebles, r1956).  *** The opacity comes from
   `storyboard_receipts/RD_diffusion_direct.py` so the ionisation history is the corpus's own; the
   quadrature is on a log-a grid at n = 3001, converged to 0.006% against n = 12001 in
   r6760+cc66.5's sibling receipt. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~3 min)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'storyboard_receipts'))
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total   # noqa: E402

C = 299792.458
WR = 4.15e-5
YP = 0.2454
NQ = 3001
A_CROSS = 1.0 / (1.0 + 3.0e7)


def machinery(H0, Om, Ombh2, z_rec, leaf_clock=True, radiation_in_rate=False,
              a_start=A_CROSS):
    Or = WR / (H0 / 100) ** 2
    Ol = 1.0 - Om
    a_rec = 1.0 / (1.0 + z_rec)
    Rb_rec = 31500 * Ombh2 / (2.7255 / 2.7) ** 4 / (1 + z_rec)

    def Hs(a):
        return H0 * np.sqrt(Om / a ** 3 + Ol + (Or / a ** 4 if radiation_in_rate else 0.0))

    def Hl(a):
        return H0 * np.sqrt(Om / a ** 3 + Ol + Or / a ** 4)

    H = Hl if leaf_clock else Hs
    zg, xeg = xe_history(lambda z: Hs(1 / (1 + z)) * 1e3 / Mpc_m, Ombh2, YP,
                         z_hi=3000., z_lo=80., n=4000)
    nH0 = n_H0_of(Ombh2, YP)

    def taup(a):
        z = 1.0 / a - 1.0
        xH = (float(np.interp(z, zg[::-1], xeg[::-1])) if (zg[-1] <= z <= zg[0])
              else (1.0 if z > zg[0] else float(xeg[-1])))
        return xe_total(z, xH, nH0, YP, helium=True) * nH0 / a ** 3 * sigT * a * Mpc_m

    def R(a):
        return Rb_rec * a / a_rec

    def g_vis(a):
        """the visibility g = -dexp(-tau)/deta, up to normalisation -- tau' exp(-tau)."""
        return taup(a)

    def integrate(f, a0, a1, n=NQ):
        u = np.linspace(np.log(a0), np.log(a1), n)
        a = np.exp(u)
        return float(np.trapezoid(np.array([f(x) for x in a]) * a, u))

    # ** THE VISIBILITY PEAK IS LOCATED, NOT ASSUMED, AND tau IS MEASURED FROM TODAY. **
    # tau' is per Mpc of conformal time here, so d tau / d ln a = taup * C/(a H), and
    # tau(a) = int_a^1 that d ln a'.  *An earlier draft integrated upward from a = 1e-5 and
    # subtracted, which sets tau = 0 at the TOP of the grid rather than at a = 1 and moves the
    # peak; the grid now runs to a = 1 and the cumulative sum runs downward from it.*
    ag = np.exp(np.linspace(np.log(1e-5), 0.0, 3000))
    dtau = np.array([taup(x) * C / (x * H(x)) for x in ag])
    dl = np.diff(np.log(ag))
    seg = 0.5 * (dtau[1:] + dtau[:-1]) * dl
    tau = np.concatenate([np.cumsum(seg[::-1])[::-1], [0.0]])   # tau(a) = int_a^1, zero at a = 1
    vis = dtau * np.exp(-tau)
    a_vis = float(ag[int(np.argmax(vis))])

    # ** a_start IS A PARAMETER AND NOT A MODULE GLOBAL, r6760+cc66.6. **  *A first draft
    # overrode a global around the call and restored it before the integrals were EVALUATED --
    # r_s and r_D are closures and read it at call time -- so the onset and crossing rows came
    # back bit-identical.  The gate below caught it, which is what it is for.*
    def r_s(a_hi):
        return integrate(lambda a: C / (a ** 2 * H(a) * np.sqrt(3 * (1 + R(a)))), a_start, a_hi)

    def r_D(a_hi):
        return float(np.sqrt(integrate(
            lambda a: ((R(a) ** 2 / (1 + R(a)) + 8.0 / 9.0)
                       / (6 * (1 + R(a)) * taup(a))) * C / (a ** 2 * H(a)), a_start, a_hi)))

    return dict(a_rec=a_rec, a_vis=a_vis, r_s=r_s, r_D=r_D)


def signature(endpoint='a_rec', **kw):
    """theta_D/theta_* of the crossing arm on the leaf clock, relative to the control's."""
    arm = machinery(kw.get('H0', 73.00), kw.get('Om', 0.3066), kw.get('Ombh2', 0.0224),
                    kw.get('z_rec', 1089.9), leaf_clock=kw.get('leaf', True),
                    radiation_in_rate=False)
    ctl = machinery(67.40, 0.3150, kw.get('Ombh2', 0.0224), kw.get('z_rec', 1089.9),
                    leaf_clock=True, radiation_in_rate=True)
    aa, ac = arm[endpoint], ctl[endpoint]
    return (arm['r_D'](aa) / arm['r_s'](aa)) / (ctl['r_D'](ac) / ctl['r_s'](ac))


print("=" * 99)
print("  PART 1 -- ** THE CENTRAL VALUE ON EACH CONVENTION **")
print("=" * 99)
base = machinery(73.00, 0.3066, 0.0224, 1089.9)
print(f"  the visibility peak is located at a = {base['a_vis']:.6e}  "
      f"(z = {1 / base['a_vis'] - 1:.1f}), against recombination at z = 1089.9")
cent = {}
for ep, nm in (('a_rec', 'r_D to RECOMBINATION'), ('a_vis', 'r_D to the VISIBILITY PEAK')):
    cent[ep] = signature(endpoint=ep)
    print(f"  {nm:>30}:  theta_D/theta_* ratio = {cent[ep]:.4f}   "
          f"({100 * (cent[ep] - 1):+.2f}%)")
spread = abs(cent['a_vis'] - cent['a_rec']) * 100
dz = abs(1 / base['a_vis'] - 1089.9) / 1089.9
print(f"\n  ⌗ the two conventions differ by {spread:.2f} points, across {dz * 100:.2f}% in the")
print(f"    endpoint redshift -- ** {spread / (dz * 100):.0f} points of signature per per-cent of endpoint **")
print("  ⌗ and they STRADDLE ZERO, so the sign of the signature is a choice of stopping point")
print()
print("  ** WHY, and it is structural rather than numerical: ** r_D^2 = int [.] / tau' and tau'")
print("  collapses through recombination, so the integrand diverges exactly where the range ends.")
print("  *The last few per mille of the range carry a finite share of the whole integral, and the")
print("  two arms' opacity histories differ there because their rates differ.*")
if (cent['a_vis'] - 1) * (cent['a_rec'] - 1) > 0:
    fail.append("the two conventions do not straddle zero -- the headline overstates it")
if spread < 0.3:
    fail.append(f"the two conventions differ by only {spread:.2f} points -- no convention term")

print()
print("=" * 99)
print("  PART 2 -- ** THE PARAMETER BUDGET, on the recombination convention **")
print("=" * 99)
print(f"  {'source':>34} {'range':>24} {'d(ratio), points':>17}")
budget = []
for lab, kw, lo, hi in (("H0 (SH0ES 73.0 +/- 1.0)", 'H0', 72.0, 74.0),
                        ("Om (BAO fit, +/- 0.006)", 'Om', 0.3006, 0.3126),
                        ("omega_b (BBN, +/- 0.0005)", 'Ombh2', 0.0219, 0.0229),
                        ("z_rec (Peebles, +/- 0.11%)", 'z_rec', 1088.7, 1091.1)):
    a = signature(endpoint='a_rec', **{kw: lo})
    b = signature(endpoint='a_rec', **{kw: hi})
    d = abs(b - a) / 2 * 100
    budget.append((lab, d))
    print(f"  {lab:>34} {f'{lo} to {hi}':>24} {d:>16.3f}")
quad_sum = float(np.sqrt(sum(d ** 2 for _, d in budget)))
lin_sum = float(sum(d for _, d in budget))
print(f"\n  {'in quadrature':>34} {'':>24} {quad_sum:>16.3f}")
print(f"  {'linear (the pessimist)':>34} {'':>24} {lin_sum:>16.3f}")

print()
print("=" * 99)
print("  PART 3 -- ** THE CONVENTION TERM BESIDE THEM **")
print("=" * 99)
print(f"  {'term':>34} {'points':>10} {'x the parameter budget':>24}")
print(f"  {'every parameter, in quadrature':>34} {quad_sum:>10.3f} {1.0:>23.1f}x")
print(f"  {'the r_D endpoint convention':>34} {spread:>10.3f} {spread / quad_sum:>23.1f}x")
print(f"""
  ⇒ ** THE CONVENTION IS {spread / quad_sum:.0f} TIMES THE WHOLE PARAMETER BUDGET. **  So the signature
  cannot be quoted as a number with an error bar; it is
      ** {100 * (min(cent.values()) - 1):+.2f}% to {100 * (max(cent.values()) - 1):+.2f}%, +/- {quad_sum:.2f} points from the parameters, **
  and which end of that range is meant is a DEFINITION and not a measurement.
  *`UNC_error_budget` carries no such term.  That is not an omission in it: on the onset handover
  with the stacking clock the corpus quoted one endpoint throughout, so there was no spread to
  carry.  The term appears here because the crossing configuration is scored against the
  instrument's header on one convention and against a standalone integration on the other.*""")
if spread <= quad_sum:
    fail.append("the convention term does not dominate -- PART 3's claim is wrong")

print()
print("=" * 99)
print("  PART 4 -- ** THE CONFIGURATION TERMS, KEPT APART BECAUSE THEY ARE NOT UNCERTAINTIES **")
print("=" * 99)
print(f"  {'configuration':>44} {'ratio':>9} {'signature':>11}")
cfg = [
    ('crossing + leaf   (the measured pair)', dict(leaf=True), 'a_rec'),
    ('crossing + stacking', dict(leaf=False), 'a_rec'),
]
for nm, kw, ep in cfg:
    v = signature(endpoint=ep, **kw)
    print(f"  {nm:>44} {v:>9.4f} {100 * (v - 1):>+10.2f}%")
v_self = signature(endpoint='a_rec', H0=68.60, Om=0.2973)
print(f"  {'crossing + leaf at (68.60, 0.2973)':>44} {v_self:>9.4f} {100 * (v_self - 1):>+10.2f}%")
print(f"""
  ⇒ ** THE CLOCK MOVES IT BY {abs(signature(endpoint='a_rec', leaf=False) - cent['a_rec']) * 100:.0f} POINTS AND THE
  PARAMETERS BY {quad_sum:.2f}. **  *A choice that outweighs the entire data budget by two orders of
  magnitude is not an uncertainty and must never be folded into one; it is reported here so that the
  budget above is read as what it is -- the spread WITHIN a configuration, not across configurations.*
  ⌗ And the signature is nearly flat in H0: {100 * (v_self - 1):+.2f}% at the self-consistent point
  against {100 * (cent['a_rec'] - 1):+.2f}% at the corpus's, a {abs(v_self - cent['a_rec']) * 100:.2f}-point move
  across 4.4 in H0.  ** So this observable selects the CONFIGURATION and says nothing about H0 **,
  which is worth stating because the two are otherwise easy to conflate.""")

print()
print("=" * 99)
print("  PART 5 -- ** DOES THE FOUR-WAY RANKING SURVIVE THE ENDPOINT?  IT HAS TO, OR r6760+cc66.2")
print("             SELECTED A CONFIGURATION ON AN ARTEFACT. **")
print("=" * 99)
A_ONSET = 1.0 / (1.0 + 6761.0)


def ratio_cfg(leaf, a0, endpoint):
    """r_D/r_s of the arm against the control, at an arbitrary handover locus.

    The control always starts at the crossing -- it has no onset, and giving it the arm's would
    be comparing two different integrals rather than two rates."""
    arm = machinery(73.00, 0.3066, 0.0224, 1089.9, leaf_clock=leaf, radiation_in_rate=False,
                    a_start=a0)
    ctl = machinery(67.40, 0.3150, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=True,
                    a_start=A_CROSS)
    aa, ac = arm[endpoint], ctl[endpoint]
    return (arm['r_D'](aa) / arm['r_s'](aa)) / (ctl['r_D'](ac) / ctl['r_s'](ac))


CFG = [('ONSET    + stacking', False, A_ONSET), ('ONSET    + leaf', True, A_ONSET),
       ('CROSSING + stacking', False, 1.0 / (1.0 + 3.0e7)),
       ('CROSSING + leaf', True, 1.0 / (1.0 + 3.0e7))]
print(f"  {'configuration':>24} {'to recombination':>18} {'to the vis. peak':>18} {'both?':>7}")
best = {}
for ep in ('a_rec', 'a_vis'):
    vals = {nm: ratio_cfg(lf, a0, ep) for nm, lf, a0 in CFG}
    best[ep] = min(vals, key=lambda k: abs(vals[k] - 1.0))
    if ep == 'a_rec':
        rec = vals
    else:
        vis = vals
for nm, _, _ in CFG:
    mark = '  ✓' if nm == best['a_rec'] == best['a_vis'] else ''
    print(f"  {nm:>24} {rec[nm]:>18.4f} {vis[nm]:>18.4f} {mark:>7}")
print(f"\n  closest to the control on recombination: ** {best['a_rec']} **")
print(f"  closest to the control on the visibility peak: ** {best['a_vis']} **")
if best['a_rec'] != 'CROSSING + leaf' or best['a_vis'] != 'CROSSING + leaf':
    fail.append("the four-way ranking does NOT survive the endpoint choice -- "
                "r6760+cc66.2 selected on an artefact")
print(f"""
  ⇒ ** THE RANKING SURVIVES AND THE VALUE DOES NOT. **  The crossing on the leaf clock is closest
  to the control on BOTH endpoints; the other three are tens of points away on both, so a 3-point
  endpoint sensitivity cannot reorder them.  *So r6760+cc66.2's selection of the configuration
  stands, and its quoted 1.022 must be read as the recombination-endpoint value of a quantity whose
  endpoint spread is 3.1 points -- which is the correction this receipt makes to it.*""")

print()
print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
