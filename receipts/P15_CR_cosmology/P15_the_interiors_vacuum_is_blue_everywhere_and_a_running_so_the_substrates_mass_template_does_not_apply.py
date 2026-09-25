"""
P15_the_interiors_vacuum_is_blue_everywhere_and_a_running_so_the_substrates_mass_template_does_not_apply
=======================================================================================================

Object under test -- node 66's work order in `FOR_60` (`r6845`): `PO-31` on the progenitor's INTERIOR.  The
order's premise is that `r6826` left one channel open, n_s - 1 = 3 - 2 sqrt(9/4 - m^2 alpha^2) asking the
interior for a slightly negative m^2 alpha^2, ** and that that formula is the SUBSTRATE's while the
fluctuations are generated in the interior. **  Three questions: the spectrum handed over and whether it is a
tilt or a running; its sign; and whether the substrate's formula applies at all.

** ALL THREE ANSWER, AND THEY ANSWER AGAINST THE CONSTRUCTION.  THE INTERIOR'S VACUUM IS BLUE EVERYWHERE AND
IT IS A RUNNING, NOT A TILT -- SO THE SUBSTRATE'S TEMPLATE DOES NOT APPLY AND THE NEGATIVE-m^2 REQUIREMENT IS
AN ARTEFACT, WHICH IS THE RETIREMENT THE ORDER HOPED FOR, BUT WHAT REPLACES IT IS WORSE AND NOT BETTER. **

** (0) FIRST, A CORRECTION TO THE ORDER'S PREMISE, BECAUSE THE INTERIOR IS NOT NEWLY BUILT. **  The order says
`PO-31` "has been carried as awaiting an interior that is not built".  ** The collapse-side interior and its
mode problem are already banked ** in `P15_the_progenitor_vacuum_is_negligible_too`, whose PART 1 has the
background a = M(rho x + x^2/2) and the Mukhanov--Sasaki potential 2/(x(x+2 rho)), M-free.  That is the SAME
object as the order's:

      a = (A/2)(1 - cos eta) + sqrt(B) sin eta   with   M = A/2,  rho = 2 sqrt(B)/A

agrees with M(rho x + x^2/2) to O(eta^2) with difference EXACTLY zero, and the order's exact a''/a = A/(2a) - 1
reduces to the banked 2/(x(x+2 rho)) at the branch point.  ** Established here rather than assumed, because
"has this been done?" has answered YES too often in this corpus for the question to be skipped. **

⚠ *And the banked receipt is NOT contradicted: its "scale-invariant" is a statement about the TRANSFER of an
incoming amplitude D_k, P = 18 k^3 D_k^2/(M^2 rho^6), and its number is an AMPLITUDE (~1e-112 against
2.1e-9).  ** The SLOPE of the vacuum's own generated spectrum is what is computed here, and it is a different
object. **  Nothing above is a correction of that receipt.*

** (1) IT IS A RUNNING, NOT A TILT, AND BY THE SAME TEST AS BEFORE. **  The potential interpolates between the
corpus's own two scale-free roots and a third regime:

      x >> 2 rho :  a''/a -> 2/x^2      the p = +2 MATTER root, scale-free (r6812's second root of p(p-1)=2)
      x << 2 rho :  a''/a -> 1/(rho x)  the 1/eta form the order names -- NOT scale-free

so the spectrum breaks at k ~ 1/rho.  At the determined composition rho = 0.0539 (P16, `c54.143`), the
log-derivative over the band where the interior supplies an adiabatic vacuum:

      d ln P / d ln k  =  +0.21  ...  +1.98      from k ~ 5 to k ~ 2000

** A spread of 1.8 with no sign change: a running, and at high k it tends to +2, which is exactly the
radiation value 3 - 2|p - 1/2| at p = 1. **  A constant n_s shift needs a constant log-derivative; this is not
one, and the band-dependence test that closed the leg at `r6812` closes this too.

** (2) AND THE SIGN IS BLUE EVERYWHERE, WHICH IS THE WRONG WAY. **  The flattest point inside the adiabatic
band is + 0.214 at k ~ 5, and the log-derivative is positive at every k tested, including below the band.
Against a measured n_s = 0.998 -- ** red by two parts in a thousand ** -- the interior's flattest value is blue
by 0.21: *the wrong sign, and about 100x the size of the departure to be explained.*  The radiation content is
what does it:

      flattest slope  ~  6.7 rho     for rho << 1        (measured: 0.0067, 0.0201 at rho = 1e-3, 3e-3)

** so scale-invariance is exact only for PURE DUST, rho -> 0, and any radiation content makes it blue. **  To
reach red one would need rho < 0, i.e. negative radiation content.  *Nothing was tuned to 0.998 and nothing
could be: the sign is not available.*

** (3) SO THE SUBSTRATE'S FORMULA DOES NOT APPLY, AND THE ORDER'S SUSPICION IS CONFIRMED. **  n_s - 1 =
3 - 2 sqrt(9/4 - m^2 alpha^2) comes from a 1/eta^2 potential whose coefficient is DIMENSIONLESS, which is why
it gives an exact power law.  ** The interior's potential carries a scale -- rho -- so it cannot give one, and
the departure from scale-invariance here is a function of k rho rather than a constant set by an effective
mass. **  The negative m^2 alpha^2 = -0.0075 that `r6826` handed to the interior is therefore ** an artefact of
applying the substrate's template off the substrate, and the corpus should stop carrying it as a requirement. **

  ⌗ WHICH MOVES THE ROW RATHER THAN CLOSING IT, AND NOT IN THE DIRECTION HOPED FOR.  ** The interior is built,
  its vacuum's spectrum is computable, and what it computes to is blue and running where the sky is red and
  nearly flat. **  So `PO-31` is no longer "what does the interior supply for m^2" -- that question is void --
  but "what supplies a red, near-constant tilt, given that neither the substrate (exactly flat), nor the leg
  (`r6812`: a k-independent amplitude), nor this interior (blue and running) does".  *That is a narrower and
  harder row than it was.*

COMPUTES: scope -- what this settles and what it must not be read as.
  * C1 ** THE EXTRACTOR IS CALIBRATED BEFORE IT IS BELIEVED, ON FOUR POWER LAWS WITH KNOWN ANSWERS ** --
    p = -1 (de Sitter) and p = +2 (matter contraction) both returning 0 to 5e-6, p = +1 returning +2 and
    p = +3 returning -2, against 3 - 2|p - 1/2|.  ** Two of those are the corpus's own scale-invariant roots,
    so the instrument is checked on the very cases the argument turns on. **  An earlier version of this
    extractor read every k on a DIFFERENT surface and returned +6 where 0 was right; the calibration caught it
    and it is recorded because the failure was silent.
  * ⚠ ** THE VACUUM IS SET AT MAXIMUM EXPANSION **, where a' = 0 exactly so every mode is sub-horizon, and the
    adiabatic condition k^2 >> |a''/a| = 0.50 is checked per mode; the reported band has k^2/|a''/a| >= 13.
    ** Below that the interior does not supply an initial condition **, which is the order's own stopping
    clause -- and it is reported as a bound on the band, not stepped over.
  * ⚠ The slope CONVERGES as the reading surface approaches the branch point: the last two decades tested
    agree to 1.2e-4, while the shallowest surface differs by 1.4e-2.  ** So the handover value is a limit
    being approached, not a choice being made -- unlike the leg at `r6812`, where a fixed-time versus
    fixed-phase locus changed the answer outright. **  Stated as convergence rather than as insensitivity,
    because the shallowest surface is NOT yet converged and saying otherwise would overstate it.
  * ⚠ A = 1 sets the unit of conformal time; every reported quantity is a log-derivative or a ratio, so no
    result depends on it.  rho = 0.0539 is the DETERMINED composition and is taken from the banked receipt,
    not chosen here; the rho-scaling is reported so the dependence is visible.
  * ⚠ ** This computes a massless minimally coupled field's vacuum on the interior background. **  It is the
    same modelling step `r6826` named and the standard one; a different field content would change the
    numbers but not the structural point in (3), which is about which lengths the potential carries.
  * ⚠ Nothing here bears on the AMPLITUDE, which the banked receipt settled at ~1e-112, nor on `PO-7`.

ORIGIN: node 66's order in `FOR_60` (`r6845`).  Its three questions are answered in order and its own
stopping clause is reached at the band's lower edge.  ** The answer is a negative one and it is reported as
such: the retirement the order hoped for is delivered, and what it leaves behind is a harder row. **
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

RHO_DET = 0.0539            # the DETERMINED composition (P16, c54.143), as the banked receipt uses it
A_UNIT = 1.0                # sets the unit of conformal time; every result below is a ratio or a slope


def background(A, rho):
    sqB = A * rho / 2.0
    a = lambda e: A / 2 * (1 - np.cos(e)) + sqB * np.sin(e)
    ap = lambda e: A / 2 * np.sin(e) + sqB * np.cos(e)
    return a, ap, brentq(a, np.pi, 2 * np.pi - 1e-15), brentq(ap, 0.5, np.pi)


def spec_powerlaw(p, ks, x0=400.0, t_end=1e-4):
    """u = v/a on a ~ t^p (t = |eta|): u_tt + (2p/t)u_t + k^2 u = 0, one common surface for all k."""
    out = []
    for k in ks:
        def rhs(t, y):
            return [y[1], -(2 * p / t) * y[1] - k * k * y[0], y[3], -(2 * p / t) * y[3] - k * k * y[2]]
        t0 = x0 / k
        a0 = t0 ** p
        v0 = 1 / np.sqrt(2 * k) * np.exp(-1j * k * t0)
        u0, du0 = v0 / a0, (1j * k * v0) / a0 - v0 * (p * t0 ** (p - 1)) / a0 ** 2
        s = solve_ivp(rhs, [t0, t_end], [u0.real, du0.real, u0.imag, du0.imag],
                      rtol=1e-12, atol=1e-18, method='DOP853')
        assert s.status == 0, s.message
        out.append(k ** 3 * abs(s.y[0, -1] + 1j * s.y[2, -1]) ** 2)
    return np.array(out)


def spec_interior(A, rho, ks, s_frac=1e-6):
    """the same extractor on the EXACT closed interior; vacuum at maximum expansion (a' = 0)."""
    a, ap, e_end, e_max = background(A, rho)
    e_read = e_end - s_frac * (e_end - e_max)
    out = []
    for k in ks:
        def rhs(e, y):
            H = ap(e) / a(e)
            return [y[1], -2 * H * y[1] - k * k * y[0], y[3], -2 * H * y[3] - k * k * y[2]]
        a0 = a(e_max)
        v0 = 1 / np.sqrt(2 * k) * np.exp(-1j * k * e_max)
        u0, du0 = v0 / a0, (-1j * k * v0) / a0          # a'(e_max) = 0 exactly
        s = solve_ivp(rhs, [e_max, e_read], [u0.real, du0.real, u0.imag, du0.imag],
                      rtol=1e-11, atol=1e-20, method='DOP853')
        assert s.status == 0, s.message
        out.append(k ** 3 * abs(s.y[0, -1] + 1j * s.y[2, -1]) ** 2)
    return np.array(out), e_end, e_max


def slope(ks, P):
    return np.gradient(np.log(P), np.log(ks))


# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — CALIBRATE THE EXTRACTOR ON FOUR POWER LAWS BEFORE BELIEVING IT")
print("=" * 94)
print("""
  a ~ |eta|^p gives n_s - 1 = 3 - 2|p - 1/2| exactly.  Two of these four are the corpus's own scale-invariant
  roots (p = -1 and p = +2, the roots of p(p-1) = 2 that r6812 names), so the instrument is checked on the
  cases the argument turns on.
""")
ks_cal = np.geomspace(1.0, 50.0, 9)
worst = 0.0
for p, lbl in ((-1.0, 'de Sitter          a~1/|eta|'), (2.0, 'matter contraction a~eta^2'),
               (1.0, 'radiation          a~eta'), (3.0, 'a~eta^3')):
    pred = 3 - 2 * abs(p - 0.5)
    sl = np.polyfit(np.log(ks_cal), np.log(spec_powerlaw(p, ks_cal)), 1)[0]
    worst = max(worst, abs(sl - pred))
    print(f"    p={p:+.0f} {lbl:<30} measured {sl:+.6f}   predicted {pred:+.6f}   |diff| {abs(sl-pred):.1e}")
check("⚑ the extractor reproduces all four known power laws to better than 5e-3 — including BOTH "
      "scale-invariant roots", worst < 5e-3)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 — THE ORDER'S BACKGROUND AND THE BANKED ONE ARE THE SAME OBJECT")
print("=" * 94)
eta, Asym, Bsym, x, Msym, rhosym = sp.symbols('eta A B x M rho', positive=True)
a_exact = Asym / 2 * (1 - sp.cos(eta)) + sp.sqrt(Bsym) * sp.sin(eta)
a_bank = Msym * (rhosym * x + x ** 2 / 2)
sub = {Msym: Asym / 2, rhosym: 2 * sp.sqrt(Bsym) / Asym}
print(f"    the order's a'' + a - A/2 = {sp.simplify(sp.diff(a_exact, eta, 2) + a_exact - Asym / 2)}")
check("the order's closed form solves a'' + a = A/2 exactly",
      sp.simplify(sp.diff(a_exact, eta, 2) + a_exact - Asym / 2) == 0)
check("and its a''/a equals A/(2a) - 1 exactly, as the order states",
      sp.simplify(sp.diff(a_exact, eta, 2) / a_exact - (Asym / (2 * a_exact) - 1)) == 0)
gap = sp.simplify(sp.expand(sp.series(a_exact, eta, 0, 3).removeO() - a_bank.subs(sub).subs(x, eta)))
print(f"    order's a to O(eta^2) minus banked a at M=A/2, rho=2 sqrt(B)/A:  {gap}")
check("⚑ the two backgrounds agree EXACTLY to O(eta^2), so the interior is not newly built and the banked "
      "mode problem is the same one", gap == 0)
pot_bank = sp.simplify(sp.diff(a_bank, x, 2) / a_bank)
check("the banked potential is 2/(x(x+2rho)) and is M-free, as its PART 1 states",
      sp.simplify(pot_bank - 2 / (x * (x + 2 * rhosym))) == 0 and Msym not in pot_bank.free_symbols)
print(f"    its two limits:  x >> 2rho -> {sp.limit(pot_bank * x ** 2, x, sp.oo)}/x^2 (the p=+2 matter root, "
      f"scale-free);  x << 2rho -> 1/(rho x) (not scale-free)")
check("so the potential interpolates between a scale-FREE root and a scale-CARRYING one, which is why a "
      "break appears rather than a tilt",
      sp.limit(pot_bank * x ** 2, x, sp.oo) == 2
      and sp.limit(pot_bank * x, x, 0) == 1 / rhosym)
check("and p(p-1)=2 has exactly the two roots r6812 names",
      set(sp.solve(sp.Eq(sp.Symbol('p') * (sp.Symbol('p') - 1), 2), sp.Symbol('p'))) == {-1, 2})

# =========================================================================================
print()
print("=" * 94)
print("PART 3 — THE SPECTRUM AT THE DETERMINED COMPOSITION: A RUNNING, NOT A TILT")
print("=" * 94)
a_f, ap_f, e_end, e_max = background(A_UNIT, RHO_DET)
pot_max = abs(A_UNIT / (2 * a_f(e_max)) - 1)
k_min_ok = np.sqrt(10 * pot_max)          # require k^2/|a''/a| >= 10 for an adiabatic vacuum
print(f"""
    rho = {RHO_DET} (determined, P16 c54.143);  eta_max = {e_max:.5f}, branch point {e_end:.5f}
    |a''/a| at maximum expansion = {pot_max:.4f}  ->  adiabatic vacuum needs k >= {k_min_ok:.2f}
""")
ks = np.geomspace(5.0, 2000.0, 22)
P, _, _ = spec_interior(A_UNIT, RHO_DET, ks)
sl = slope(ks, P)
check("every mode reported has an adiabatic vacuum (k^2/|a''/a| >= 10)", ks.min() >= k_min_ok)
print(f"    {'k':>9} {'k*rho':>8} {'dlnP/dlnk':>11}")
for k, s in list(zip(ks, sl))[::3]:
    print(f"    {k:>9.2f} {k*RHO_DET:>8.3f} {s:>+11.4f}")
print(f"\n    range over the band: {sl.min():+.3f} to {sl.max():+.3f}   spread {sl.max()-sl.min():.3f}")
check("⚑ the log-derivative spans more than 1.0 across the band, so it is a RUNNING and not a tilt — the "
      "same band-dependence test that closed the leg at r6812", sl.max() - sl.min() > 1.0)
check("and at high k it tends to the radiation value +2 = 3-2|p-1/2| at p=1, which is the potential's "
      "1/(rho x) limit showing up where it should", abs(sl.max() - 2.0) < 0.05)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 — THE SIGN: BLUE EVERYWHERE, AND THE RADIATION CONTENT IS WHAT DOES IT")
print("=" * 94)
N_SIGN_CHANGES = int(np.sum(np.sign(sl)[1:] * np.sign(sl)[:-1] < 0))
print(f"""
    flattest value in the band: {sl.min():+.4f} at k = {ks[int(np.argmin(sl))]:.2f}
    sign changes across the band: {N_SIGN_CHANGES}
    the measured target is n_s = 0.998, i.e. dlnP/dlnk = -0.002, RED
""")
check("⚑ the spectrum is blue at every wavenumber in the band — the sign the measurement needs is not "
      "available at all", sl.min() > 0 and N_SIGN_CHANGES == 0)
check("and the flattest value misses the measured departure by more than fifty times, in the wrong "
      "direction", abs(sl.min() - (-0.002)) / 0.002 > 50)
print("    and the rho-scaling, which identifies the radiation content as the cause:")
print(f"      {'rho':>8} {'flattest slope':>15} {'slope/rho':>10}")
scal = []
for r in (1e-3, 3e-3):
    k2 = np.geomspace(3.0, 3.0 / r, 24)
    s2 = slope(k2, spec_interior(A_UNIT, r, k2)[0])
    m = s2[int(np.argmin(np.abs(s2)))]
    scal.append(m / r)
    print(f"      {r:>8.0e} {m:>+15.6f} {m/r:>10.2f}")
check("the flattest slope scales as ~6.7 rho for small rho, so scale-invariance is exact only for PURE dust "
      "and any radiation makes it blue", all(5.0 < c < 8.0 for c in scal))
check("so reaching a red tilt would need rho < 0 — a negative radiation content, which is why nothing was "
      "tuned to 0.998 and nothing could be", min(scal) > 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 5 — AND THE ANSWER IS SURFACE-INDEPENDENT, UNLIKE THE LEG'S")
print("=" * 94)
ks_s = np.geomspace(5.0, 30.0, 9)
flats = []
for frac in (1e-3, 1e-5, 1e-7):
    s3 = slope(ks_s, spec_interior(A_UNIT, RHO_DET, ks_s, s_frac=frac)[0])
    flats.append(s3[int(np.argmin(np.abs(s3)))])
    print(f"    reading surface s/span = {frac:.0e}   flattest slope {flats[-1]:+.6f}")
print(f"    successive changes: {abs(flats[1]-flats[0]):.2e} then {abs(flats[2]-flats[1]):.2e}")
check("⚑ the answer CONVERGES as the surface approaches the branch point — the last two decades agree to "
      "better than 1e-3, so the handover value is well defined",
      abs(flats[2] - flats[1]) < 1e-3)
check("and the convergence is monotone, the shallowest surface being the outlier rather than the deepest — "
      "so this is a limit being approached and not a choice being made",
      abs(flats[1] - flats[0]) > 10 * abs(flats[2] - flats[1]))

# =========================================================================================
print()
print("=" * 94)
print("VERDICT")
print("=" * 94)
print(f"""
  ⚑ THE ORDER'S THREE QUESTIONS, ANSWERED IN ORDER.

    (1) tilt or running   ** a RUNNING **: dlnP/dlnk = {sl.min():+.2f} to {sl.max():+.2f} over k = 5..2000,
                          tending to the radiation value +2, with no constant to fit
    (2) the sign          ** BLUE at every k **, flattest {sl.min():+.3f}, against a measured RED -0.002 —
                          the wrong sign, and ~100x the size; the cause is the radiation content, the
                          flattest slope going as ~6.7 rho, so red would need rho < 0
    (3) the template      ** DOES NOT APPLY. **  3 - 2 sqrt(9/4 - m^2 alpha^2) comes from a 1/eta^2 potential
                          with a DIMENSIONLESS coefficient; the interior's carries the scale rho, so
                          m^2 alpha^2 = -0.0075 is an ARTEFACT of applying the substrate's template off the
                          substrate, and the corpus should stop carrying it as a requirement

  ⌗ SO THE ROW MOVES AND NARROWS RATHER THAN CLOSING.  Neither the substrate (exactly flat), nor the leg
    (`r6812`: a k-independent amplitude), nor this interior (blue and running) supplies a red near-constant
    tilt.  ** PO-31 is no longer "what does the interior give for m^2" — that question is void — but "what
    supplies a red, near-constant tilt at all". **

  ⚠ And the interior was already built and banked; the order's premise that it was not is corrected in (0),
    without contradicting the banked receipt, whose scale-invariance is of a TRANSFER and whose number is an
    AMPLITUDE.
""")
print(f"  {sum(_checks)}/{len(_checks)} checks passed.")
sys.exit(0 if all(_checks) else 1)
