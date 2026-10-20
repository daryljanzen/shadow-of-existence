"""
LEVEL: exact symbolic for every identity, with two numeric readings and a CONTROL
that must break the mass-independence.

WHY THIS PROBE EXISTS.  P16 sec:peak states that the exact regulated peak -- "how deep
the compression runs on the smooth substrate through the branch point" -- REMAINS OPEN,
and the frontier carries it as the named step of the row on the field evolution of a
concrete matter model through the branch point.  The peak the paper does give,
Tpk ~ 174 MeV from the infall energy, is argued from an energy budget rather than
computed from the substrate law, and the paper says so.

WHAT IS CLAIMED.
  (1) The substrate law r^3 = 2 M alpha^2 sinh^2(3 tau / 2 alpha) has, at the branch
      point, exactly the Oppenheimer-Snyder marginally-bound dust free-fall time
      tau = (2/3) r^(3/2)/sqrt(2M).  Identically, not to leading order in a fit.
  (2) The dust ball's mean density at horizon crossing is P16's own closed form
      3 c^6 / (32 pi G^3 M^2).  Identically.
  (3) The compression is regulated by the PROPER-TIME BUDGET and not by any feature of
      the substrate: the throat radius alpha/sqrt3 and the collapse branch's extremum
      (2 M alpha^2)^(1/3) both exceed the horizon radius for the paper's own progenitor,
      so a peak at either is LESS compressed than horizon crossing.
  (4) Equating the time remaining with a response time t gives a peak density
      rho = 1/(6 pi G t^2), in which the progenitor mass CANCELS IDENTICALLY.
  (5) Evaluated at one Planck time of remaining proper time -- the last epoch the
      classical description is entitled to -- that is exactly rho_Planck / (6 pi).

WHAT IS NOT CLAIMED.  No temperature.  The Newtonian infall-energy expression
m_N c^2 (GM/r c^2) leaves its regime inside the horizon, so this probe asserts a density
and not a Tpk, and P16's 174 MeV is neither confirmed nor contradicted here.  Nothing
about what happens below the Planck density, which is where (5) stops.  And NOT that
the corpus's recorded mass-blindnesses imply this one.  The count was READ and not
guessed, which changed it: receipts/INDEX.md's `sec:peak (mass-blindness)' row carries
THREE already -- two sharing the amplitude-factorisation mechanism and one independent
(the horizon identity) -- so this is a FOURTH, and by a fourth mechanism, a proper-time
budget.  It is asserted separately as a new instance, never as a pattern.

WHAT WOULD FALSIFY IT.  (1) or (2) failing as symbolic identities; the paper's own
progenitor turning out super-Nariai, so that it is not a progenitor; the mass failing to
cancel in (4); the Planck identity in (5) being approximate; or -- the discriminator --
the CONTROL below failing to break the mass-independence, which would show that the
cancellation is an accident of arithmetic rather than a consequence of the dust equation
of state meeting a free-fall law that goes as r^(3/2)/sqrt(M).
"""
import math
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print("=" * 78)
print("  P16 -- THE REGULATED PEAK IS THE PLANCK DENSITY OVER SIX PI")
print("=" * 78)

# ---- (1) the substrate law's branch-point limit is OS free-fall -------------
M, alpha, tau, r = sp.symbols('M alpha tau r', positive=True)
r3 = 2 * M * alpha**2 * sp.sinh(3 * tau / (2 * alpha))**2
lim = sp.simplify(sp.series(r3, tau, 0, 4).removeO())
check("the substrate law's leading branch-point behaviour is r^3 = (9/2) M tau^2",
      sp.simplify(lim - sp.Rational(9, 2) * M * tau**2) == 0, sp.simplify(lim))

tau_sub = sp.solve(sp.Eq(sp.Rational(9, 2) * M * tau**2, r**3), tau)
tau_sub = [t for t in tau_sub if sp.simplify(t.subs({M: 1, r: 1})) > 0][0]
tau_os = sp.Rational(2, 3) * r**sp.Rational(3, 2) / sp.sqrt(2 * M)
check("and it equals the Oppenheimer-Snyder marginally-bound free-fall time exactly",
      sp.simplify(sp.simplify(tau_sub) - sp.simplify(tau_os)) == 0,
      f"substrate {sp.simplify(tau_sub)}  vs  OS {sp.simplify(tau_os)}")

# ---- (2) the horizon-crossing density is P16's closed form ------------------
G, c, Mk = sp.symbols('G c M_kg', positive=True)
Rs = 2 * G * Mk / c**2
rho_hor = 3 * Mk / (4 * sp.pi * Rs**3)
p16_form = 3 * c**6 / (32 * sp.pi * G**3 * Mk**2)
check("rho_hor = 3 M /(4 pi R_s^3) is identically P16's 3 c^6/(32 pi G^3 M^2)",
      sp.simplify(rho_hor - p16_form) == 0, sp.simplify(rho_hor))

# ---- (3) the substrate's own features are too LARGE to regulate -------------
G_n, c_n = 6.67430e-11, 2.99792458e8
LAM = 1.1056e-52
M_kg = 4.17e52                      # P16 sec:abundances, its own worked progenitor
Mg = G_n * M_kg / c_n**2
Rs_n = 2 * Mg
al = math.sqrt(3.0 / LAM)
nariai = 2 * al / (3 * math.sqrt(3))
check("the paper's own progenitor is SUB-NARIAI, so it is a progenitor at all",
      Rs_n < nariai, f"A/Nariai = {Rs_n/nariai:.4f}")
check("CONTROL: a mass 10 per cent larger is SUPER-Nariai and is not one",
      1.1 * Rs_n > nariai, f"A/Nariai = {1.1*Rs_n/nariai:.4f}")
check("the throat radius alpha/sqrt3 EXCEEDS the horizon radius",
      al / math.sqrt(3) > Rs_n, f"ratio = {(al/math.sqrt(3))/Rs_n:.4f}")
check("the collapse branch's extremum (2 M alpha^2)^(1/3) EXCEEDS it too",
      (2 * Mg * al**2) ** (1.0/3.0) > Rs_n,
      f"ratio = {((2*Mg*al**2)**(1.0/3.0))/Rs_n:.4f}")
tau_ff = (math.sqrt(2) / 3.0) * Rs_n**1.5 / math.sqrt(Mg) / c_n
check("and the approach from the horizon to the branch point is GIGAYEARS, so "
      "'no interval in which anything could act' is false on the approach",
      tau_ff / 3.156e16 > 1.0, f"{tau_ff/3.156e16:.3f} Gyr")

# ---- (4) the time-budget peak density is mass-free -------------------------
t = sp.Symbol('t', positive=True)
# tau_avail(r) = (sqrt2/3) r^(3/2)/sqrt(M_geo) in geometrised length; set = t*c
Mgeo = G * Mk / c**2
r_min = sp.solve(sp.Eq(sp.sqrt(2) / 3 * r**sp.Rational(3, 2) / sp.sqrt(Mgeo), t * c), r)[0]
rho_pk = sp.simplify(3 * Mk / (4 * sp.pi * r_min**3))
check("the mass cancels identically in the budget-regulated peak density",
      Mk not in rho_pk.free_symbols, f"rho_pk = {rho_pk}  free: {rho_pk.free_symbols}")
check("and the closed form is rho_pk = 1/(6 pi G t^2)",
      sp.simplify(rho_pk - 1 / (6 * sp.pi * G * t**2)) == 0, sp.simplify(rho_pk))

# ---- (5) at one Planck time it is rho_Planck / 6 pi ------------------------
hbar = sp.Symbol('hbar', positive=True)
t_P = sp.sqrt(hbar * G / c**5)
rho_at_tP = sp.simplify((1 / (6 * sp.pi * G * t**2)).subs(t, t_P))
rho_P = c**5 / (hbar * G**2)
check("at one Planck time of remaining proper time the peak is rho_Planck/(6 pi)",
      sp.simplify(rho_at_tP - rho_P / (6 * sp.pi)) == 0, sp.simplify(rho_at_tP))
hbar_n = 1.054571817e-34
num = 1.0 / (6 * math.pi * G_n * (hbar_n * G_n / c_n**5))
check("numerically 2.7347e95 kg/m^3, and free of the progenitor mass",
      abs(num / 2.734732e95 - 1) < 1e-5, f"{num:.6e} kg/m^3")

# ---- the FIGURES this result's INDEX row prints, pinned here ---------------
# check_figures_pinned caught that the row printed five figures beside a receipt
# that asserted only INEQUALITIES about them.  An inequality does not fail when a
# value is wrong by a factor, so each printed figure is pinned to within half its
# last printed digit.  The gate was right and this is the repair it asked for.
print()
print("  THE FIGURES THE INDEX ROW PRINTS, PINNED TO HALF THEIR LAST DIGIT:")
print("  ⌗ Written as explicit literal comparisons, one per figure, and not as a")
print("    loop over a table: the gate parses this source, and a tolerance held in")
print("    a loop variable is not a pin it can see.  That is the gate being right")
print("    about its own reach, not a limitation worth arguing with.")
ratio_nariai   = Rs_n / nariai
ratio_throat   = (al / math.sqrt(3)) / Rs_n
ratio_extremum = ((2 * Mg * al**2) ** (1.0/3.0)) / Rs_n
lap_gyr        = (math.pi * al / 3) / c_n / 3.156e16
approach_gyr   = tau_ff / 3.156e16

check("PINNED  A / A_Nariai = 0.9768",
      abs(ratio_nariai - 0.9768) <= 0.00005, f"{ratio_nariai:.6f}")
check("PINNED  throat / R_s = 1.54",
      abs(ratio_throat - 1.54) <= 0.005, f"{ratio_throat:.6f}")
check("PINNED  collapse-branch extremum / R_s = 1.92",
      abs(ratio_extremum - 1.92) <= 0.005, f"{ratio_extremum:.6f}")
check("PINNED  lap turnaround pi alpha / 3 = 18.2 Gyr",
      abs(lap_gyr - 18.2) <= 0.05, f"{lap_gyr:.6f}")
check("PINNED  approach, R_s to the branch point = 4.364 Gyr",
      abs(approach_gyr - 4.364) <= 0.0005, f"{approach_gyr:.6f}")

# ---- the CONTROL: the cancellation must be breakable -----------------------
print()
print("  CONTROL -- the mass-independence must FAIL for a law of a different exponent,")
print("  or the cancellation is arithmetic luck and not a consequence of dust meeting")
print("  free fall.")
n = sp.Symbol('n', positive=True)
for expo, label in ((sp.Rational(3, 2), 'r^(3/2)/sqrt(M)  (free fall -- the real one)'),
                    (sp.Integer(1), 'r^1/sqrt(M)      (control)'),
                    (sp.Integer(2), 'r^2/sqrt(M)      (control)')):
    rm = sp.solve(sp.Eq(r**expo / sp.sqrt(Mgeo), t * c), r)[0]
    rr = sp.simplify(3 * Mk / (4 * sp.pi * rm**3))
    free = Mk in rr.free_symbols
    print(f"    tau ∝ {label:<42} mass present in rho_pk: {free}")
    if expo == sp.Rational(3, 2):
        check("CONTROL baseline: the free-fall exponent cancels the mass", not free)
    else:
        check(f"CONTROL: exponent {expo} does NOT cancel the mass", free,
              f"free symbols {rr.free_symbols}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The substrate law's branch-point limit IS dust free-fall,")
print("  identically, and the dust ball's horizon-crossing density IS P16's closed form.")
print("  Neither the throat nor the collapse branch's extremum can regulate the")
print("  compression -- both exceed the horizon radius for P16's own progenitor -- and")
print("  the approach lasts gigayears, so the crossing's zero duration does not")
print("  constrain it either.  What regulates it is the proper-time budget, giving")
print("  rho_pk = 1/(6 pi G t^2), MASS-FREE, and at one Planck time exactly")
print("  rho_Planck/(6 pi) = 2.7347e95 kg/m^3.  The control confirms the cancellation")
print("  is the dust equation of state meeting an r^(3/2)/sqrt(M) free-fall law and not")
print("  arithmetic luck.  It is the FOURTH mass-blindness at this seam on the")
print("  register's own count, by a fourth mechanism.  Every figure the INDEX row")
print("  prints is pinned here to half its last digit, which is the repair")
print("  check_figures_pinned asked for and was right to ask for.")
print("  NO TEMPERATURE IS CLAIMED.")
print("=" * 78)
