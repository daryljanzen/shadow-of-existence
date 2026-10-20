#!/usr/bin/env python3
"""PO-88 / r7399: the exact regulated peak -- how deep the compression runs on
the smooth substrate through the branch point.

The row's discharge is a concrete model's stress-energy carried THROUGH the
branch point as a dynamical problem.  This file does that for the one concrete
progenitor P16 itself names, and the number it delivers is the row's named step.

Nothing is taken on authority.  The substrate law is written down, its
near-branch-point limit is derived and then CHECKED against the independent
Oppenheimer-Snyder free-fall time, and every figure below is printed with the
expression that produced it.

  substrate law (P3 sec:lap, P16 eq. quoted at its line 547):
      r^3 = 2 M alpha^2 sinh^2(3 tau/(2 alpha)),      alpha = sqrt(3/Lambda)

  concrete model (P16 sec:abundances, its own worked progenitor):
      a closed dust + Lambda interior, M = 4.17e52 kg, turning around at z~1.5
"""
import math

# ---------------------------------------------------------------- constants
G     = 6.67430e-11          # m^3 kg^-1 s^-2
c     = 2.99792458e8         # m s^-1
LAM   = 1.1056e-52           # m^-2   (Planck 2018 Lambda)
M_SUN = 1.98892e30           # kg
MN_C2 = 938.272              # MeV, nucleon rest energy
MEV   = 1.602176634e-13      # J per MeV

def hdr(s):
    print()
    print("=" * 78)
    print("  " + s)
    print("=" * 78)

# ---------------------------------------------------------------- the model
M_kg  = 4.17e52                       # P16's own worked progenitor
M     = G * M_kg / c**2               # geometrised mass, metres
Rs    = 2 * M                         # horizon areal radius, metres
alpha = math.sqrt(3.0 / LAM)          # substrate's one invariant, metres

hdr("STEP 1 -- the concrete model, and whether it is even a progenitor")
print(f"  M              = {M_kg:.3e} kg   = {M_kg/M_SUN:.3e} M_sun")
print(f"  GM/c^2         = {M:.4e} m")
print(f"  R_s = 2GM/c^2  = {Rs:.4e} m   = {Rs/3.0857e22:.3f} Mpc")
print(f"  alpha=sqrt(3/L)= {alpha:.4e} m   = {alpha/3.0857e22:.3f} Mpc")
print()
print("  P16 sec:peak: a turnaround exists exactly when A <= 2 alpha / (3 sqrt 3),")
print("  which is identically the Nariai mass parameter.  With A = R_s:")
nariai = 2 * alpha / (3 * math.sqrt(3))
print(f"    A        = {Rs:.4e} m")
print(f"    Nariai   = {nariai:.4e} m")
print(f"    A/Nariai = {Rs/nariai:.4f}   sub-Nariai: {Rs < nariai}")
print("  ⌗ The paper's own progenitor is sub-Nariai by a few per cent, not by")
print("    orders -- so the model it hands this row sits just inside the one")
print("    condition that makes it a progenitor at all.")

# ---------------------------------------- the substrate law and its limit
hdr("STEP 2 -- the substrate law, its near-branch-point limit, and a CHECK")
def r_of_tau(tau):
    """tau in metres (geometrised proper time); r in metres."""
    return (2 * M * alpha**2 * math.sinh(3 * tau / (2 * alpha))**2) ** (1.0/3.0)

print("  r^3 = 2 M alpha^2 sinh^2(3 tau / 2 alpha)")
print("  Near tau -> 0:  sinh^2 -> (3 tau / 2 alpha)^2, so")
print("      r^3 -> 2 M alpha^2 * 9 tau^2 / (4 alpha^2) = (9/2) M tau^2")
print("      => tau(r) = (sqrt2 / 3) r^(3/2) / sqrt(M)")
def tau_of_r(r):
    return (math.sqrt(2) / 3.0) * r**1.5 / math.sqrt(M)
print()
print("  ** CHECK, against a result with no step in common: the")
print("     Oppenheimer-Snyder marginally-bound dust free-fall time from r to 0")
print("     is tau = (2/3) r^(3/2) / sqrt(2M).  Same thing? **")
osf = lambda r: (2.0/3.0) * r**1.5 / math.sqrt(2*M)
for rr in (Rs, Rs/1e3, 1.0):
    a_, b_ = tau_of_r(rr), osf(rr)
    print(f"    r = {rr:11.4e} m :  substrate {a_:.6e}   OS {b_:.6e}   "
          f"ratio {a_/b_:.12f}")
print("  ⇒ identical.  The substrate law's branch-point limit IS dust free-fall,")
print("    which is the consistency this computation needs before any number of")
print("    its own is worth printing.")
print()
print("  And the exact law against its limit, to see where the limit stops holding:")
for rr in (Rs, Rs/10, Rs/1e3):
    t_ex = None
    # invert the exact law numerically for tau at this r
    lo, hi = 0.0, 10*alpha
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if r_of_tau(mid) < rr: lo = mid
        else: hi = mid
    t_ex = 0.5*(lo+hi)
    print(f"    r = {rr:11.4e} m :  exact tau {t_ex:.6e} m   limit {tau_of_r(rr):.6e} m   "
          f"ratio {t_ex/tau_of_r(rr):.6f}")

# ---------------------------------------------- the matter carried through
hdr("STEP 3 -- the dust carried through: density, infall energy, and the clock")
def rho(r):
    """dust: rho r^3 = const, anchored on the ball's own mass"""
    return 3 * M_kg / (4 * math.pi * r**3)
def E_infall_MeV(r):
    """marginally bound: (1/2)v^2 = GM/r, so E per nucleon = m_N c^2 (GM/r c^2)"""
    return MN_C2 * (M / r)
rho_hor = rho(Rs)
print(f"  rho_hor = 3 M /(4 pi R_s^3) = {rho_hor:.4e} kg/m^3")
print(f"  P16's closed form 3 c^6/(32 pi G^3 M^2) = "
      f"{3*c**6/(32*math.pi*G**3*M_kg**2):.4e} kg/m^3   (agrees)")
rho_crit = 3*(67.4*1e3/3.0857e22)**2/(8*math.pi*G)
print(f"  present rho_crit (H0=67.4) = {rho_crit:.4e} kg/m^3")
print(f"  => rho_hor / rho_crit = {rho_hor/rho_crit:.3f}")
print("  ⌗ This is P16's reductio made arithmetic: for a progenitor this massive")
print("    the horizon-crossing average is of order the PRESENT cosmic density,")
print("    so a peak pinned there would put the hot dense era in our future.")
print(f"  E_infall at R_s = {E_infall_MeV(Rs):.1f} MeV = (1/2) m_N c^2, identically")
print(f"  proper time from R_s to the branch point = {tau_of_r(Rs)/c:.4e} s "
      f"= {tau_of_r(Rs)/c/3.156e16:.3f} Gyr")
print("  ⛔ So the crossing's APPROACH is not short.  Whatever the branch point")
print("     does in zero duration, the leg into it lasts gigayears of proper time.")

# ------------------------------------------------- the regulator, measured
hdr("STEP 4 -- WHAT REGULATES IT: the three candidates, on numbers")
print("  R1  the substrate's throat scale alpha/sqrt3:")
print(f"        alpha/sqrt3 = {alpha/math.sqrt(3):.4e} m  vs  R_s = {Rs:.4e} m")
print(f"        ratio = {(alpha/math.sqrt(3))/Rs:.4f}  "
      f"=> throat is {'LARGER' if alpha/math.sqrt(3) > Rs else 'smaller'} than the horizon")
print("        ⇒ a throat-regulated peak is LESS compressed than horizon crossing.")
print("          REJECTED, and on arithmetic rather than on wording.")
print()
r_R2 = (2 * M * alpha**2) ** (1.0/3.0)
print("  R2  the collapse branch's extremum, |r^3| = 2 M alpha^2:")
print(f"        r_min = {r_R2:.4e} m  vs  R_s = {Rs:.4e} m   ratio {r_R2/Rs:.3f}")
print(f"        reached at |tau| = pi alpha / 3 = {math.pi*alpha/3:.4e} m "
      f"= {math.pi*alpha/3/c/3.156e16:.3f} Gyr")
print("        ⇒ a de Sitter-scale time and a radius above the horizon: this is")
print("          the LAP's turnaround, not the matter's.  REJECTED.")
print()
print("  R3  nothing regulates it; the divergence is one instant of measure zero")
print("      and the crossing has no duration, so the peak is the last")
print("      compression of FINITE duration -- the infall-energy value.")
print(f"        but STEP 3 measured that leg at {tau_of_r(Rs)/c/3.156e16:.2f} Gyr of proper")
print("        time, during which the infall energy grows as 1/r without bound.")
print("        ⛔ REJECTED TOO: there is no shortage of time on the approach, so")
print("          'nothing can act' is false where R3 needs it to be true.")

# ------------------------------------------------------------ the answer
hdr("STEP 5 -- R4, WHICH THE PRICE DID NOT NAME: the proper-time budget")
print("  The compression is regulated where the time LEFT runs out, not where")
print("  the substrate bends.  Set tau(r) equal to a microphysical response time")
print("  and solve for r:   r = ( 3 tau sqrt(M) / sqrt2 )^(2/3)")
def r_of_budget(t_seconds):
    tau_geo = t_seconds * c
    return (3 * tau_geo * math.sqrt(M) / math.sqrt(2)) ** (2.0/3.0)
probes = (("strong interaction", 1e-23),
          ("weak, at 100 MeV",   1e-10),
          ("Planck time",        5.391e-44))
print()
print(f"  {'response':<22}{'t (s)':>12}{'r_min (m)':>14}{'rho_pk (kg/m^3)':>20}"
      f"{'E/nucleon (MeV)':>18}")
print("  " + "-" * 84)
rows = []
for name, tt in probes:
    rm = r_of_budget(tt)
    rows.append((name, tt, rm, rho(rm), E_infall_MeV(rm)))
    print(f"  {name:<22}{tt:>12.3e}{rm:>14.4e}{rho(rm):>20.4e}{E_infall_MeV(rm):>18.4e}")

hdr("STEP 6 -- AND THE PEAK DENSITY IS MASS-INDEPENDENT.  derived, then checked")
print("  r_min = (3 tau sqrt(M) / sqrt2)^(2/3)  so  r_min^3 = (9/2) tau^2 M,")
print("  and rho = 3 M_kg /(4 pi r_min^3) with M_kg = M c^2/G, so")
print("      rho_pk = 3 (M c^2/G) / (4 pi (9/2) tau^2 M) = c^2 / (6 pi G tau^2)")
print("  -- the mass cancels identically.  tau here is the geometrised response")
print("  time (t c), so in seconds:  rho_pk = 1/(6 pi G t^2).")
print()
print("  CHECK the closed form against the numbers STEP 5 computed from M:")
for name, tt, rm, rr, ee in rows:
    closed = 1.0 / (6 * math.pi * G * tt**2)
    print(f"    {name:<22} numeric {rr:.6e}   closed form {closed:.6e}   "
          f"ratio {rr/closed:.12f}")
print()
print("  CHECK the mass-independence directly, by varying M over 12 orders:")
for mult in (1e-6, 1e-3, 1.0, 1e3, 1e6):
    Mk = 4.17e52 * mult
    Mg = G * Mk / c**2
    tau_geo = 1e-23 * c
    rm = (3 * tau_geo * math.sqrt(Mg) / math.sqrt(2)) ** (2.0/3.0)
    print(f"    M = {Mk:.3e} kg :  r_min = {rm:.6e} m   "
          f"rho_pk = {3*Mk/(4*math.pi*rm**3):.6e} kg/m^3")
print()
print("  ⛭ So the regulated peak density is set by the RESPONSE TIME alone and is")
print("     free of the progenitor mass.")
print()
print("  ⛔ AND THE COUNT HAD TO BE READ RATHER THAN GUESSED, WHICH CHANGED IT.")
print("     A first draft of this file called it 'a third' on the strength of P16's")
print("     own sentence: 'What this does not show, and is asserted nowhere: that")
print("     either result implies the other, or that the pattern extends to a third")
print("     quantity.'  THE REGISTER SAYS OTHERWISE.  receipts/INDEX.md's")
print("     `sec:peak (mass-blindness)' row carries THREE -- two sharing the")
print("     amplitude-factorisation mechanism, one independent (the horizon")
print("     identity) -- and records that 'the r1619 third instance REVISED this")
print("     row's earlier no-extension-to-a-third-quantity claim'.")
print("     ⇒ This one is a FOURTH, and by a FOURTH mechanism: a proper-time")
print("       budget, which is neither an amplitude exponent nor a horizon")
print("       identity.  The grouping becomes 2-of-one-kind + 1 + 1.")
print()
print("  ⚠ AND THE SAME READ FOUND P16's OWN PARAGRAPH INCONSISTENT WITH ITSELF,")
print("     which is routed and NOT fixed here -- P16 is not this seat's file.")
print("     The disclaimer sentence above sits AFTER the paragraph that supplies")
print("     the third instance ('A third instance sharpens the grouping rather than")
print("     merely lengthening the list'), yet it still reads 'either result' and")
print("     'a third quantity'.  The register's own note says that revision")
print("     happened; the paper's sentence did not follow it.")
print()
print("  ⌗ And the temperature is NOT mass-blind, which separates the two:")
print("     E/nucleon at r_min = m_N c^2 (M/r_min) ∝ M / M^(1/3) = M^(2/3).")
for mult in (1e-3, 1.0, 1e3):
    Mk = 4.17e52 * mult
    Mg = G * Mk / c**2
    tau_geo = 1e-23 * c
    rm = (3 * tau_geo * math.sqrt(Mg) / math.sqrt(2)) ** (2.0/3.0)
    print(f"     M = {Mk:.3e} kg :  E/nucleon = {MN_C2*(Mg/rm):.4e} MeV")

HBAR = 1.054571817e-34       # J s
M_N  = 1.67262192e-27        # kg

hdr("STEP 7 -- THE FIXED-tau READING IS NOT SELF-CONSISTENT, and one column above is wrong")
print("  ⛔ TWO DEFECTS IN STEP 5, BOTH MINE, BOTH FOUND BY READING ITS OWN NUMBERS:")
print()
print("  ⛔ (i) The 'E/nucleon' column is NOT a temperature and must not be read as")
print("     one.  It is m_N c^2 (GM/rc^2), the marginally-bound NEWTONIAN infall")
print("     energy, and inside the horizon GM/rc^2 > 1/2 so the expression has left")
print("     the regime it was derived in.  At r_min it prints ~1e29 MeV, which is")
print("     the formula failing and not the matter getting hot.  It is kept in the")
print("     output rather than deleted because a deleted wrong column teaches")
print("     nothing; the temperature is NOT claimed here.")
print()
print("  ⛔ (ii) tau_response was held FIXED while rho ran over forty orders.  A")
print("     response time is a property of the state, so the condition is a")
print("     FIXED POINT and not a lookup.  The assumption-light response time is")
print("     causal: nothing acts faster than light crossing the mean nucleon")
print("     spacing d = (m_N/rho)^(1/3).")
print()
k = (4 * math.pi * M_N / (3 * M_kg)) ** (1.0/3.0)
print(f"  d = r * k with k = (4 pi m_N / 3 M_kg)^(1/3) = {k:.6e}")
print("  tau_avail(r) = (sqrt2/3) r^(3/2)/sqrt(M)  =  d = r k   gives")
print("      r_fp = (9/2) k^2 M")
r_fp = 4.5 * k**2 * M
print(f"      r_fp   = {r_fp:.4e} m")
print(f"      rho_fp = {rho(r_fp):.4e} kg/m^3")
rho_planck = c**5 / (HBAR * G**2)
l_planck = math.sqrt(HBAR * G / c**3)
print(f"      Planck length  = {l_planck:.4e} m      rho_Planck = {rho_planck:.4e} kg/m^3")
print(f"      r_fp / l_Planck = {r_fp/l_planck:.4e}   "
      f"rho_fp / rho_Planck = {rho(r_fp)/rho_planck:.4e}")
print("  ⇒ The causal fixed point sits ABOVE the Planck density by thirty-four")
print("     orders.  So the classical description fails before the causal response")
print("     bound bites: the time budget is not what stops the compression either.")

hdr("STEP 8 -- THE ANSWER, AND IT IS EXACT AND MASS-FREE")
t_planck = math.sqrt(HBAR * G / c**5)
print("  What the budget DOES deliver is the peak at the last epoch the classical")
print("  description is entitled to -- one Planck time of proper time remaining:")
print(f"      t_Planck = {t_planck:.6e} s")
print(f"      r_min    = {r_of_budget(t_planck):.6e} m")
num = rho(r_of_budget(t_planck))
closed = 1.0 / (6 * math.pi * G * t_planck**2)
print(f"      rho_pk   = {num:.6e} kg/m^3   (closed form {closed:.6e}, "
      f"ratio {num/closed:.12f})")
print()
print("  And the closed form collapses, because t_Planck^2 = hbar G / c^5:")
print("      rho_pk = 1/(6 pi G t_P^2) = c^5/(6 pi hbar G^2) = rho_Planck / (6 pi)")
print(f"      rho_Planck / (6 pi) = {rho_planck/(6*math.pi):.6e} kg/m^3")
print(f"      against rho_pk      = {closed:.6e} kg/m^3   "
      f"ratio {closed/(rho_planck/(6*math.pi)):.12f}")
print()
print("  ** THE REGULATED PEAK IS rho_Planck / 6 pi, EXACTLY, AND FREE OF THE")
print("     PROGENITOR MASS.  It is a number, which is what r7399 says this row's")
print("     discharge delivers. **")
print()
print("  ⌗ And it is reached rather than approached: the proper time from the")
print(f"     horizon to that radius is {tau_of_r(Rs)/c/3.156e16:.3f} Gyr, so the")
print("     through-crossing evolution has gigayears of freedom and is NOT")
print("     constrained to nothing by the two structural results.")
print("  ⇒ So the row does NOT terminate as a boundary, which is what this")
print("     computation's own pre-registration predicted it would.")
