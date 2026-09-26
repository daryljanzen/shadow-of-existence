"""
P15_the_interiors_transfer_imprints_its_own_running_so_the_channel_hunt_answered_the_wrong_question
==================================================================================================

LEVEL: the banked instrument re-run as the gate (DOP853, rtol 1e-12) and then pointed at a
different object; exact linearity and starting-convention controls before any slope is believed.

OBJECT UNDER TEST -- `PO-31`, `r6911` item ⓵.  The order, verbatim:

    "The transfer law is exactly scale-invariant on vacuum data, and the paper says why: the
     k^3 cancels the k^-3 of D_k = sqrt(hbar/2) k^-3/2.  ⚠ That cancellation is a property of
     the vacuum normalisation, not of the transfer. ... Applied to an arbitrary input spectrum
     rather than to vacuum data, does the interior's transfer act as a scale-free multiplier,
     or does it imprint its own running on whatever enters?"

    Scale-free   => the observed tilt is the progenitor's own, the channel hunt is over.
    Imprints     => "no input can give a red near-constant tilt through this interior,
                     whatever the progenitor supplies", and the row becomes a statement about
                     the interior model.

-------------------------------------------------------------------------------
** IT IMPRINTS, AND THE ORDER'S DIAGNOSIS OF WHY IS EXACTLY RIGHT. **

  ⓵ ** THE TRANSFER IS NOT A SCALE-FREE MULTIPLIER AND IS NOT EVEN A POWER LAW. **  Measured on
      UNIT incoming amplitude, so that what comes out is the multiplier itself:

        d ln T / d ln k   runs from  -0.866  at k = 7   to  -0.010  at k = 1400

      a spread of 0.856 across the observed band.  ** What it adds to any spectrum's tilt is
      twice that: -1.73 to -0.02. **

  ⓶ ** AND THE BANKED EXACT SCALE-INVARIANCE IS THE LOW-k LIMIT OF THAT SAME FUNCTION. **  As
      k falls below the break the transfer becomes a clean power law:

        d ln T / d ln k  ->  -1   (-0.9992 at k = 0.3),   and  k T(k) -> 27.86, a constant

      and P ~ k^3 |c_0|^2 is scale-invariant exactly when d ln T/d ln k = -1.  ** So the banked
      cancellation is not a coincidence of the vacuum normalisation meeting a scale-free
      transfer -- it is the vacuum normalisation meeting the transfer's low-k power law, and it
      holds only where that power law does. **  The decomposition is an identity:

        s(k) = d ln(|c_0| k^{3/2})/d ln k = d ln T/d ln k + 1

      -- the whole k-DEPENDENCE is the transfer's and the CONSTANT is the normalisation's,
      which is what the order proposed and what this confirms.  It reproduces `r6898`'s
      +0.134 at k = 7 and +0.990 at k = 1400 from the transfer alone.

  ⓷ ** AND IT IS THE SAME FUNCTION FOR EVERY INPUT, WHICH IS WHAT LICENSES THE PHRASE
      "WHATEVER THE PROGENITOR SUPPLIES". **  Five inputs -- including one that is deliberately
      NOT a power law -- give output-slope-minus-input-slope agreeing to 4e-13.  Linearity is
      verified to 7e-15 rather than invoked.

⛔ ** AND ONE CORRECTION TO THE ORDER'S OWN STATEMENT OF ITS SECOND OUTCOME. **  The order says
   "no input can give a red near-constant tilt through this interior, whatever the progenitor
   supplies".  ** As written that is too strong, and the computation is what shows it: ** an
   input whose own running is the transfer's negated comes out red and near-constant by
   construction.  What is true is the weaker and sharper statement:

     * ** no POWER-LAW progenitor spectrum can **, because a constant input tilt plus a running
       transfer is a running output; and
     * the input that would work is a SPECIFIC computed function -- it must itself run by 1.71
       across the band, in the opposite sense to the transfer.  ** That is a REQUIREMENT on the
       progenitor, not a result about it **, and it is reported here as one.

   ⌗ *Which is the same shape as `r6826`'s m^2 alpha^2 = -0.0075, a requirement this line later
   withdrew for being an artefact of the wrong template.  Naming it a requirement at the outset
   is the lesson from that, applied.*

⇒ ** SO THE CHANNEL HUNT IS OVER EITHER WAY, WHICH IS WHAT THE ORDER WANTED. **  Five channels
  were closed -- substrate, collapse leg, finite duration, interior vacuum, transfer -- and each
  answered "what tilt does the VACUUM give?" while `P15` holds the perturbations are classical
  and non-vacuum.  ** The row stops being a channel hunt and becomes a statement about the
  interior model plus one computed requirement on its input. **

COMPUTES: scope -- what this settles and what it must not be read as.
  * ** THE CALIBRATION IS THE GATE. **  PART 1 re-runs the banked check at the banked rho and k.
    Everything below is that same instrument pointed at a different object, so if
    3/(2 sqrt 2) does not reproduce there, nothing below may be read.
  * ⚠ ** THE BAND IS BOUNDED AT k < 2783 AND THE BOUND IS THE PREMISE, NOT THE ARITHMETIC. **
    The incoming mode is started at x_i = 300/k, which is outside the potential's break only
    while 300/k > 2 rho.  Above that the mode starts INSIDE the radiation era and "enters from
    the matter contraction" is false -- so no high-k asymptote is claimed here.  An earlier pass
    read T rising above 1 at k = 1e5 and that number is discarded as a misplaced initial
    condition rather than reported as a limit.
  * ** THE SLOPE IS WHAT IS CLAIMED, AND THE AMPLITUDE IS NOT. **  |T| carries a ~1% dependence
    on the reading surface x_f; a common multiplicative bias cancels in a log-slope, and the
    slope is shown stable across three decades of x_f.  No amplitude is asserted.
  * ** NOTHING HERE BEARS ON A_s. **  `r6898`'s 10^103 shortfall is a statement about VACUUM
    data; a classical non-vacuum input's amplitude is free and is not addressed.
  * ** NO PROGENITOR INTERIOR IS BUILT **, as the order required.  The background, the potential
    and rho = 0.0539 are taken from banked receipts; what is new is the object measured.
  * ** PO-31 IS NOT CLOSED. **  The order said it was not expected to close, and it does not.

rc=0 on success.  Run: python3 P15_the_interiors_transfer_imprints_its_own_running_so_the_channel_hunt_answered_the_wrong_question.py
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


RHO = 0.0539                       # the DETERMINED composition (P16, c54.143) -- taken
TARGET = 3.0 / (2.0 * np.sqrt(2.0))
K_PREMISE = 300.0 / (2 * RHO)      # above this, x_i = 300/k lands inside the radiation era


def residue(k, rho=RHO, amp=1.0, n_osc=300.0, x_i=None, xf_frac=1e-4, rtol=1e-12):
    """|c_0| at the crunch for an incoming sub-horizon mode of amplitude `amp`.

    With x_i = n_osc/k the initial phase is e^{i n_osc}, the SAME for every k -- which is what
    makes the k-comparison clean.  PART 2 varies n_osc and PART 3 replaces the convention
    outright, because a phase artefact here would look exactly like a running.
    """
    x_f = xf_frac * rho

    def rhs(xx, y):
        pot = 2.0 / (xx * (xx + 2.0 * rho))
        return [y[1], (pot - k**2) * y[0], y[3], (pot - k**2) * y[2]]

    xi = n_osc / k if x_i is None else x_i
    y0 = [amp * np.cos(k * xi), -amp * k * np.sin(k * xi),
          amp * np.sin(k * xi), amp * k * np.cos(k * xi)]
    s = solve_ivp(rhs, [xi, x_f], y0, rtol=rtol, atol=1e-16, method='DOP853')
    v = s.y[0, -1] + 1j * s.y[2, -1]
    vx = s.y[1, -1] + 1j * s.y[3, -1]
    c0 = (v - vx * x_f) / (1.0 + x_f * np.log(x_f / (2 * rho)) / rho)
    return abs(c0)


def vac(k, rho=RHO, **kw):
    """The banked convention: vacuum-normalised incoming amplitude (2k)^{-1/2}."""
    return residue(k, rho=rho, amp=1.0 / np.sqrt(2.0 * k), **kw)


def cslope(f, ks, i):
    """Centred log-slope of f over a log-spaced grid."""
    lk = np.log(ks)
    return (np.log(f[i + 1]) - np.log(f[i - 1])) / (lk[i + 1] - lk[i - 1])


# =============================================================================================
head("PART 1 (C1) -- THE BANKED CHECK, AT THE BANKED COMPOSITIONS, BEFORE ANYTHING ELSE")

print(f"  {'rho':>9} {'k':>7} {'|c0| k^1.5 rho':>17} {'3/(2 sqrt 2)':>14} {'departure':>11}")
worst = 0.0
for rho in [1e-3, 1e-4]:
    for k in [2.0, 10.0, 30.0]:
        val = vac(k, rho=rho) * k**1.5 * rho
        d = abs(val / TARGET - 1)
        worst = max(worst, d)
        print(f"  {rho:>9.0e} {k:>7.1f} {val:>17.6f} {TARGET:>14.6f} {d*100:>10.3f}%")
check(worst < 0.03,
      f"the banked scale-invariance reproduces at the banked rho and k -- worst {worst*100:.2f}%")

# =============================================================================================
head("PART 2 -- LINEARITY AND PHASE, VERIFIED RATHER THAN INVOKED")

print("  The mode equation is linear, so T(k) must not depend on the incoming amplitude.")
print("  ** That is exactly what licenses the order's phrase 'whatever the progenitor")
print("     supplies', so it is measured and not asserted. **")
print(f"  {'k':>8} {'|c0| @ amp=1':>18} {'|c0| @ amp=7.3':>18} {'ratio':>10}")
worst_lin = 0.0
for k in [5.0, 50.0, 500.0]:
    a, b = residue(k, amp=1.0), residue(k, amp=7.3)
    worst_lin = max(worst_lin, abs((b / a) / 7.3 - 1))
    print(f"  {k:>8.1f} {a:>18.10e} {b:>18.10e} {b/a:>10.6f}")
check(worst_lin < 1e-10,
      f"the transfer is exactly linear in the incoming amplitude -- worst {worst_lin:.1e}")

print()
print("  And the starting phase: x_i = n_osc/k fixes it at e^{i n_osc} for every k, so a")
print("  dependence on n_osc would be a phase artefact masquerading as a running.")
print(f"  {'k':>8} {'n_osc=300':>17} {'n_osc=500':>17} {'n_osc=900':>17} {'spread':>10}")
worst_ph = 0.0
for k in [5.0, 50.0, 500.0]:
    vals = [residue(k, n_osc=n) for n in (300.0, 500.0, 900.0)]
    sp_ = (max(vals) - min(vals)) / float(np.mean(vals))
    worst_ph = max(worst_ph, sp_)
    print(f"  {k:>8.1f} " + " ".join(f"{v:>17.10e}" for v in vals) + f" {sp_:>10.2e}")
check(worst_ph < 1e-4,
      f"|c_0| is insensitive to where the mode is started -- worst spread {worst_ph:.1e}")

# =============================================================================================
head("PART 3 -- AND THE CONVENTION REPLACED OUTRIGHT, PLUS THE PREMISE'S OWN BOUND")

print(f"  2 rho = {2*RHO:.4f}, so x_i = 300/k is outside the potential's break only while")
print(f"  300/k > 2 rho, i.e. ** k < {K_PREMISE:.0f} **.  Above that the mode starts INSIDE the")
print("  radiation era and the incoming-from-the-matter-contraction premise is FALSE.")
print("  ⌗ An earlier pass read T rising above 1 at k = 1e5 and traced it to exactly that:")
print("     the number was tolerance-converged to 2e-10 and still meaningless, because what")
print("     was misplaced was the initial condition and not the integration.")
print()
print(f"  {'k':>8} {'slope, x_i=300/k':>19} {'slope, x_i=30 fixed':>21} {'difference':>12}")
worst_conv = 0.0
for k in [7.0, 20.0, 100.0, 1000.0, 2000.0]:
    a1, b1 = residue(0.9 * k), residue(1.1 * k)
    a2, b2 = residue(0.9 * k, x_i=30.0), residue(1.1 * k, x_i=30.0)
    s1 = np.log(b1 / a1) / np.log(1.1 / 0.9)
    s2 = np.log(b2 / a2) / np.log(1.1 / 0.9)
    worst_conv = max(worst_conv, abs(s1 - s2))
    print(f"  {k:>8.1f} {s1:>19.6f} {s2:>21.6f} {abs(s1-s2):>12.2e}")
check(worst_conv < 1e-3,
      f"the slope survives replacing the starting convention -- worst {worst_conv:.1e}")

print()
print("  And the slope CONVERGES in the reading surface, where the AMPLITUDE does not:")
print(f"  {'k':>8} {'slope @ xf=1e-3':>18} {'slope @ xf=1e-4':>18} {'slope @ xf=1e-5':>18}")
worst_xf = 0.0          # the two DEEPEST surfaces, which are the converged pair
worst_shallow = 0.0     # and the shallowest, reported rather than asserted on
for k in [7.0, 50.0, 1000.0]:
    row = []
    for f in (1e-3, 1e-4, 1e-5):
        a, b = residue(0.9 * k, xf_frac=f), residue(1.1 * k, xf_frac=f)
        row.append(np.log(b / a) / np.log(1.1 / 0.9))
    worst_xf = max(worst_xf, abs(row[2] - row[1]))
    worst_shallow = max(worst_shallow, abs(row[1] - row[0]))
    print(f"  {k:>8.1f} " + " ".join(f"{v:>18.6f}" for v in row))
check(worst_xf < 1e-4,
      f"the two deepest surfaces agree on the slope to {worst_xf:.1e} -- a common "
      "multiplicative bias cancels in a log-slope")
print(f"  ⚠ and the SHALLOWEST surface (xf = 1e-3) differs by up to {worst_shallow:.1e}, at k = 1000")
print("     where the slope is itself only -0.015.  ** Stated as CONVERGENCE and not as")
print("     insensitivity, because the shallowest surface is not yet converged -- the same")
print("     clause r6846 attached to its own reading surface. **  The running claimed below")
print(f"     is {0.856:.3f}, so even the unconverged surface sits {0.856/worst_shallow:.0f}x below it.")

# =============================================================================================
head("PART 4 -- THE TRANSFER ITSELF: NOT SCALE-FREE, AND NOT EVEN A POWER LAW")

ks = np.array([5.0, 7.0, 10.0, 20.0, 50.0, 100.0, 300.0, 1000.0, 1400.0, 2000.0])
T = np.array([residue(k) for k in ks])
print(f"  rho = {RHO}, break at x ~ 2 rho = {2*RHO:.4f}, k_break = {1/(2*RHO):.2f}")
print(f"  {'k':>8} {'T(k) = |c0|':>17} {'d lnT/d lnk':>14} {'added to a tilt':>17}")
sl = {}
for i in range(len(ks)):
    if 0 < i < len(ks) - 1:
        sl[ks[i]] = cslope(T, ks, i)
        print(f"  {ks[i]:>8.1f} {T[i]:>17.8e} {sl[ks[i]]:>14.6f} {2*sl[ks[i]]:>17.6f}")
    else:
        print(f"  {ks[i]:>8.1f} {T[i]:>17.8e}")
lo, hi = sl[7.0], sl[1400.0]
check(abs(hi - lo) > 0.5,
      f"the transfer's log-slope RUNS across the band: {lo:+.4f} to {hi:+.4f}, spread {abs(hi-lo):.4f}")
check(lo < -0.5 and hi > -0.1,
      "so it is neither a constant multiplier nor a power law -- both would give a flat slope")
print(f"  ** what the transfer adds to any spectrum's tilt runs from {2*lo:+.4f} to {2*hi:+.4f}. **")

# =============================================================================================
head("PART 5 -- AND THE BANKED SCALE-INVARIANCE IS THE LOW-k LIMIT OF THAT SAME FUNCTION")

kl = np.array([0.2, 0.3, 0.5, 0.8, 1.2, 2.0, 3.0, 5.0])
Tl = np.array([residue(k) for k in kl])
print(f"  {'k':>8} {'T(k)':>17} {'k T(k)':>13} {'d lnT/d lnk':>14}")
slo = {}
for i in range(len(kl)):
    if 0 < i < len(kl) - 1:
        slo[kl[i]] = cslope(Tl, kl, i)
        print(f"  {kl[i]:>8.2f} {Tl[i]:>17.8e} {kl[i]*Tl[i]:>13.5f} {slo[kl[i]]:>14.6f}")
    else:
        print(f"  {kl[i]:>8.2f} {Tl[i]:>17.8e} {kl[i]*Tl[i]:>13.5f}")
check(abs(slo[0.3] + 1.0) < 5e-3,
      f"d lnT/d lnk -> -1 as k falls below the break ({slo[0.3]:+.4f} at k = 0.3)")
kT = kl * Tl
check((kT.max() - kT.min()) / kT.mean() < 0.06 and abs(kT[0] / kT[1] - 1) < 1e-3,
      f"and k T(k) flattens to a constant ~{kT[0]:.2f} -- which IS the power law T ~ 1/k")
print()
print("  P ~ k^3 |c_0|^2 is scale-invariant exactly when d lnT/d lnk = -1, so:")
print("  ** the banked cancellation is the vacuum normalisation meeting the transfer's LOW-k")
print("     POWER LAW, and it holds only where that power law does. **")
print()
print("  The decomposition, as an identity rather than an argument:")
print("      s(k) = d ln(|c0| k^{3/2})/d ln k  =  d lnT/d lnk  +  1")
print("  -- the k-DEPENDENCE is the transfer's, the CONSTANT is the normalisation's.")
print(f"  {'k':>8} {'d lnT/d lnk + 1':>18} {'s(k) measured':>16} {'r6898 banked':>14}")
ok_id = True
for k, banked in ((7.0, 0.1337), (1400.0, 0.9895)):
    a, b = vac(0.9 * k), vac(1.1 * k)
    smeas = np.log((b * (1.1*k)**1.5) / (a * (0.9*k)**1.5)) / np.log(1.1 / 0.9)
    a2, b2 = residue(0.9 * k), residue(1.1 * k)
    pred = np.log(b2 / a2) / np.log(1.1 / 0.9) + 1.0
    ok_id &= abs(pred - smeas) < 2e-3 and abs(smeas - banked) < 2e-2
    print(f"  {k:>8.1f} {pred:>18.6f} {smeas:>16.6f} {banked:>14.4f}")
check(ok_id,
      "the identity holds and reproduces r6898's +0.134 and +0.990 from the transfer alone")

# =============================================================================================
head("PART 6 -- THE SAME RUNNING FOR EVERY INPUT, ONE OF THEM NOT A POWER LAW")

inputs = {
    "vacuum   A ~ k^-3/2": lambda k: k**-1.5,
    "         A ~ k^-1  ": lambda k: k**-1.0,
    "         A ~ k^-2  ": lambda k: k**-2.0,
    "         A ~ const ": lambda k: 1.0 + 0 * k,
    "NOT a power law    ": lambda k: k**-1.5 * (1.0 + 0.3 * np.sin(np.log(k))),
}
mid = ks[1:-1]
rows = {}
for name, f in inputs.items():
    amps = np.array([f(k) for k in ks])
    out = np.array([residue(k, amp=a) for k, a in zip(ks, amps)])
    rows[name] = np.array([cslope(out, ks, i) - cslope(amps, ks, i)
                           for i in range(1, len(ks) - 1)])
print(f"  {'input':<22}" + " ".join(f"{k:>8.0f}" for k in mid))
for name, d in rows.items():
    print(f"  {name:<22}" + " ".join(f"{v:>8.4f}" for v in d))
ref = rows["vacuum   A ~ k^-3/2"]
worst_ind = max(float(np.max(np.abs(d - ref))) for d in rows.values())
check(worst_ind < 1e-8,
      f"output slope minus input slope is the SAME function of k for every input -- {worst_ind:.1e}")
print("  ** including the non-power-law one, which is the case the phrase 'whatever the")
print("     progenitor supplies' actually needs. **")

# =============================================================================================
head("PART 7 -- SO WHAT WOULD AN INPUT HAVE TO BE?  A REQUIREMENT, REPORTED AS ONE")

print("  n_s^out - 1 = (n_s^in - 1) + 2 d lnT/d lnk.  For a measured -0.005 throughout:")
print(f"  {'k':>8} {'2 d lnT/d lnk':>16} {'required n_s^in - 1':>21}")
req = []
for k in mid:
    req.append(-2 * sl[k] - 0.005)
    print(f"  {k:>8.1f} {2*sl[k]:>16.6f} {req[-1]:>21.6f}")
spread_req = max(req) - min(req)
check(spread_req > 1.0,
      f"the required input is NOT a power law -- its own tilt must run by {spread_req:.3f}")
print()
print("  ⛔ ** WHICH CORRECTS THE ORDER'S SECOND OUTCOME AS WRITTEN. **  'No input can give a")
print("     red near-constant tilt, whatever the progenitor supplies' is too strong: the input")
print("     above does, by construction.  What is true is that ** no POWER-LAW progenitor")
print("     spectrum can **, and that the input which would is a specific computed running.")
print("     ⌗ That is a REQUIREMENT on the progenitor and not a result about it -- the same")
print("       shape as r6826's m^2 alpha^2 = -0.0075, which this line later withdrew.")

# =============================================================================================
head("VERDICT")

print(f"""
  ⇒ ** THE INTERIOR'S TRANSFER IMPRINTS ITS OWN RUNNING.  IT IS THE ORDER'S SECOND OUTCOME,
       AND THE ORDER'S DIAGNOSIS OF THE MECHANISM IS CONFIRMED EXACTLY. **

     * on unit incoming amplitude the multiplier's log-slope runs {lo:+.4f} to {hi:+.4f}, a spread
       of {abs(hi-lo):.3f}, so it is neither scale-free nor a power law across the observed band;
     * the same function for every input, to {worst_ind:.0e}, linearity exact to {worst_lin:.0e};
     * and the banked exact scale-invariance is that function's LOW-k limit -- d lnT/d lnk
       -> -1 and k T(k) -> {kT[0]:.2f} -- so the cancellation the paper reports is the vacuum
       normalisation meeting a power law that only holds below the break.

  ** s(k) = d lnT/d lnk + 1 is the whole story: the k-dependence was always the transfer's
     and the constant was always the normalisation's, exactly as the order proposed. **

  ⇒ ** AND THE CHANNEL HUNT IS OVER. **  Five channels were closed and all five answered
    "what tilt does the vacuum give?", while `P15` holds twice over that the perturbations are
    classical and non-vacuum.  The five results stand; the question was mis-aimed.  `PO-31`
    is now a statement about the INTERIOR MODEL plus one computed requirement on its input,
    and it is no longer a search for a channel.

  ⛔ WITH ONE CORRECTION TO THE ORDER'S OWN WORDING, because the computation will not support
    the stronger form: an input whose running is the transfer's negated DOES come out red and
    near-constant.  ** No power-law progenitor spectrum can **, and the input that would is a
    specific function that must run by {spread_req:.2f} across the band.  A requirement, not a result.

  ⌗ WHAT THIS DOES NOT DO.  It does not close `PO-31` -- the order said it would not. It builds
    no progenitor interior, asserts no amplitude, and says nothing about A_s, whose 10^103
    shortfall is a VACUUM statement. ⚠ And the band is bounded at k < {K_PREMISE:.0f}, where the
    incoming mode still starts outside the break: no high-k asymptote is claimed.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
