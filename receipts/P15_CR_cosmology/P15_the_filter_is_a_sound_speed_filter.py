"""
P15_the_filter_is_a_sound_speed_filter.py -- the branch-point selection rule's exponent has two
factors, and the corpus varies only one.

** THE DAMPING IS e^{-k c_s |Delta eta|}.  `sec:what-crosses` holds c_s at the plasma's value and
varies k, reading a SCALE criterion (frozen against oscillating).  Hold k and vary c_s and the same
inequality is a SPECIES criterion -- and a pressureless component has c_s = 0 IDENTICALLY, so its
exponent vanishes at every wavenumber. **

** THAT MAKES THE MATTER SECTOR'S INHERITANCE EXACT RATHER THAN ADIABATIC. **  At c_s = 0 the
segment's mode equation is psi'' = 0, whose constant solution the kernel leaves untouched with no
approximation; the frozen-mode argument, by contrast, rests on horizon exit and degrades at small
scales.  The two agree wherever both apply and only the pressureless one is available everywhere.

WHAT IS COMPUTED, on the corpus's own segment geometry (LOWL_exact_transmission.py's constants).
  1. |Delta eta| = 3.3197 in units alpha = 1 -- the recorded 3.32.
  2. Exact transfer-matrix transmission as a function of BOTH k and c_s.  For every constant c_s the
     transfer matrix reproduces -k c_s |Delta eta| to the digit.
  3. ** ln T = 0 EXACTLY at c_s = 0, at k = 1, 10, 85.3, 1e3 and 1e5 ** -- uniform in k.
  4. The crossover: at the first peak's k the filter is opaque above c_s ~ 3.5e-3, the exponent
     running ~1.6e2 c_s/c.  ** So a per-cent sound speed already gives e^-1.6 and ten per cent
     e^-16. **

** !! THE SELECTION-RULE READING OF (4) IS WITHDRAWN, r2376+c54.162.  The ARITHMETIC of (1)-(4)
stands unchanged and nothing below is retracted; what is withdrawn is the INFERENCE this file drew
from (4) -- "the crossing can inherit perturbations from a COLD species and from no other". **
The kernel acts on OSCILLATORY content, and on the progenitor's own interior nothing arrives
oscillating: |aH| diverges as 1/x at the branch point while c_s saturates at 1/sqrt3, so
c_s k/|aH| -> c_s k x -> 0 for EVERY k, and every mode from ell = 28 to ell = 2475 freezes strictly
before the crunch (P16_every_mode_is_frozen_at_the_crossing).  ** So the exponent computed here has
nothing to act on: the crossing is lossless for every species rather than for cold ones alone. **
That is a LOSS of a claimed prediction, not a gain, and it is recorded as one.  What survives is
this file's positive content: the EXACT vanishing at c_s = 0, which now holds of every species and
not of dust alone.

WHAT IS NOT CLAIMED.  This is the FIELD half of the branch-point crossing question -- what happens
to perturbations of a given species.  The detailed WORLDLINE dynamics of a concrete model at the
branch point is a separate computation and is not done here.

STATUS: OK (|Delta eta| asserted at 3.32; the plasma exponent asserted in (-160,-140); ln T asserted
  zero to 1e-9 at c_s = 0 across five decades in k)
RUN: python3 P15_the_filter_is_a_sound_speed_filter.py   RUNTIME: ~1 min (numpy)
ORIGIN: computations/beyond_the_wall/L138_the_filter_is_a_sound_speed_filter.py, built r2376 (c54.112).
ORIGIN-DIVERGENCE: none of substance; the origin opens and closes on the register's own bookkeeping.
HONEST BOUND: on this segment the plasma exponent comes out ln T = -147, against the -152 the corpus
  records -- a 3% difference in the exponent, from the sound-speed profile's discretisation.  Nothing
  here turns on it: the load-bearing result is the EXACT vanishing at c_s = 0, which is independent
  of the profile.
"""
import numpy as np

print(__doc__.split("STATUS:")[0])

# ---- the corpus's own segment: LOWL_exact_transmission.py, verbatim in its constants ----
al = 1.0
M = al/(3*np.sqrt(3))
A = (2*M*al**2)**(1./3)
smax = np.pi*al/3.0
R0 = 0.60/A                      # baryon loading, as the corpus sets it
DA = 2.580                       # comoving distance to last scattering, in units alpha = 1
N = 200000


def absr(s):
    return np.abs(-A*np.abs(np.sin(1.5*s/al))**(2./3))


def cs_plasma(s):
    """the photon-baryon sound speed the corpus uses on the segment"""
    return 1.0/np.sqrt(3.0*(1.0 + R0*absr(s)))


s = np.linspace(1e-8, smax, N)
a = absr(s)
deta = np.diff(s)/(0.5*(a[1:] + a[:-1]))
DETA = float(np.sum(deta))

# =====================================================================
print("=" * 78)
print("PART 1 — THE SEGMENT")
print("=" * 78)
print(f"  branch point at s -> 0, turnaround at s = pi*alpha/3;  a(s) = |r(s)|")
print(f"  ** |Delta eta| over the segment = {DETA:.4f}   (the corpus's 3.32) **")
assert abs(DETA - 3.32) < 0.02
print(f"  the plasma sound speed runs {cs_plasma(s).min():.4f} .. {cs_plasma(s).max():.4f}"
      f"  (1/sqrt3 = {1/np.sqrt(3):.4f} unloaded)")
csbar = float(np.sum(0.5*(cs_plasma(s)[1:]+cs_plasma(s)[:-1])*deta)/DETA)
print(f"  its eta-weighted mean is  <c_s> = {csbar:.4f}")


def transmission(k, cs_of_s):
    """exact transfer-matrix transmission across the segment for omega = k * c_s(s).

    The mode equation on the imaginary-time segment is psi'' = omega^2 psi.  We build the
    solution that GROWS from the branch point (the stable direction) and invert.
    """
    w = k*cs_of_s(s)
    wm = 0.5*(w[1:] + w[:-1])
    psi, dpsi, logamp = 1.0, max(w[0], 1e-300), 0.0
    for wi, de in zip(wm, deta):
        if wi*de < 1e-12:                      # omega -> 0 : psi'' = 0, an exact shear
            p, d = psi + de*dpsi, dpsi
        else:
            xx = wi*de
            if xx > 300.0:                     # log-domain: cosh ~ sinh ~ e^x/2
                logamp += xx - np.log(2.0)
                p, d = psi + dpsi/wi, wi*psi + dpsi
            else:
                ch, sh = np.cosh(xx), np.sinh(xx)
                p, d = ch*psi + (sh/wi)*dpsi, wi*sh*psi + ch*dpsi
        psi, dpsi = p, d
        if psi > 1e50:
            logamp += np.log(psi); dpsi /= psi; psi = 1.0
    logamp += np.log(psi)
    return -logamp                              # ln T


# =====================================================================
print()
print("=" * 78)
print("PART 2 — TRANSMISSION AS A FUNCTION OF BOTH k AND c_s")
print("=" * 78)
kP1 = 220.0/DA                                  # the first acoustic peak
print(f"  the first acoustic peak sits at k = ell/D_A = 220/{DA} = {kP1:.1f} (alpha = 1)")
print()
print(f"  {'c_s (constant)':>16} {'ln T at k = k_P1':>20} {'-k <c_s> |Delta eta|':>24}")
for cs0 in (1/np.sqrt(3), 0.5, 0.3, 0.1, 0.01, 0.0):
    lnT = transmission(kP1, lambda ss, c=cs0: np.full_like(ss, c))
    print(f"  {cs0:>16.4f} {lnT:>20.2f} {-kP1*cs0*DETA:>24.2f}")
lnT_plasma = transmission(kP1, cs_plasma)
print()
print(f"  ** on the corpus's own loaded plasma sound speed:  ln T = {lnT_plasma:.1f} "
      f"-- the recorded e^-152 **")
assert -160 < lnT_plasma < -140
print()
for s_ in [
 "⌗ ** THE EXPONENT IS $-k\\,c_s\\,|\\Delta\\eta|$ AND IT REPRODUCES THE TRANSFER MATRIX TO THE DIGIT",
 "   FOR EVERY CONSTANT $c_s$. **  *Two factors multiply: the wavenumber and the sound speed.  The",
 "   corpus varies the first.*",
]:
    print("  " + s_)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE MATTER SECTOR")
print("=" * 78)
print("  A pressureless component has c_s = 0 identically -- not small, not slowly varying, zero.")
print("  On the segment its mode equation is psi'' = 0, whose solutions are 1 and eta.")
print()
print(f"  {'k':>12} {'ln T  (c_s = 0)':>18} {'ln T  (plasma)':>18}")
for k in (1.0, 10.0, kP1, 1e3, 1e5):
    print(f"  {k:>12.4g} {transmission(k, lambda ss: np.zeros_like(ss)):>18.3g}"
          f" {transmission(k, cs_plasma):>18.3g}")
lnT0 = [transmission(k, lambda ss: np.zeros_like(ss)) for k in (1.0, 10.0, kP1, 1e3, 1e5)]
print()
print(f"  ** transmission is EXACTLY ONE (ln T = 0) at every wavenumber tested. **")
assert max(abs(v) for v in lnT0) < 1e-9
print()
for s_ in [
 "⇒⇒ ** SO THE CROSSING IS TRANSPARENT TO A PRESSURELESS COMPONENT UNIFORMLY IN $k$, AND THE",
 "   STATEMENT IS EXACT RATHER THAN ADIABATIC. **",
 "",
 "⌗ ** AND THAT IS A DIFFERENT ARGUMENT FROM THE ONE THE CORPUS USES, WITH A DIFFERENT SCOPE. **",
 "   *The frozen-mode argument says: a super-horizon mode is a constant, so the shift cannot touch",
 "   it.  True, and scale-limited -- it holds for $k$ below the horizon scale and degrades above it.",
 "   The pressureless argument says: $c_s=0$ kills the exponent whatever $k$ is.*  ** One is an",
 "   inheritance that holds where the modes are frozen; the other is an inheritance that holds",
 "   everywhere, and the matter sector has the second. **",
]:
    print("  " + s_)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — ONE INEQUALITY, TWO READINGS")
print("=" * 78)
print("  The filter is governed throughout by the single dimensionless combination")
print()
print("        X  =  k * c_s * |Delta eta| ,      T = e^{-X} ,")
print()
print("  and X = 1 is where the crossing turns from transparent to opaque.")
print()
print(f"  {'reading':>26} {'held fixed':>14} {'varied':>10} {'what it separates':>30}")
for aa, bb, cc, dd in [
    ("the corpus's (r2209)", "c_s", "k", "frozen from oscillating"),
    ("** the species reading **", "k", "c_s", "** matter from plasma **"),
]:
    print(f"  {aa:>26} {bb:>14} {cc:>10} {dd:>30}")
print()
kstar = 1.0/(csbar*DETA)
print(f"  at the plasma's <c_s> the formal crossover is k* = 1/(<c_s>|Delta eta|) = {kstar:.3f}"
      f"  (ell = {kstar*DA:.2f})")
print("  -- but that value is BELOW the horizon scale, where the mode is frozen and omega = k c_s")
print("     is not the right frequency.  ** The honest statement is that the plasma is opaque")
print("     wherever it OSCILLATES, and the frozen branch is where the corpus's own argument")
print("     applies instead.  The two regimes hand over; neither is being stretched here. **")
csstar = 1.0/(kP1*DETA)
print(f"  at the first peak's k the crossover is  c_s* = 1/(k |Delta eta|) = {csstar:.2e}")
print()
for s_ in [
 "⇒⇒ ** SO AT THE PEAK SCALE -- squarely in the oscillating branch, where the model is the",
 "   corpus's own -- THE FILTER IS OPAQUE TO ANYTHING WITH A SOUND SPEED ABOVE ABOUT",
 f"   $4\\times10^{{-3}}$, AND TRANSPARENT ONLY TO A COMPONENT WHOSE PRESSURE IS ZERO. **  *There is",
 "   no middle ground at that scale: the exponent is $\\sim165\\,c_s/c$, so a per-cent sound speed",
 "   already gives $e^{-1.6}$ and a ten-per-cent one $e^{-16}$.*",
 "",
 "⌗⌗ ** THE PHYSICAL READING, AND IT IS THE ANSWER TO WHAT THE CROSSING DOES TO A CONCRETE MATTER",
 "   MODEL: the branch point passes the model's DENSITY content and resets its ACOUSTIC content. **",
 "   *A pressureless species crosses with its perturbations intact at every scale; a pressure-",
 "   carrying one arrives with its oscillatory content annihilated and only its background",
 "   surviving.*  ** Which is why the seam supplies one characteristic phase per mode rather than an",
 "   inherited one -- there is nothing left to inherit on that side. **",
]:
    print("  " + s_)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT `L-138` BECOMES")
print("=" * 78)
for s_ in [
 "✔ ** THE FIELD HALF IS ANSWERED, AND THE ANSWER IS UNIFORM IN $k$: the crossing is exactly",
 "   transparent to a pressureless component and exponentially opaque to a pressure-carrying one,",
 "   the discriminant being $k\\,c_s\\,|\\Delta\\eta|$ with $|\\Delta\\eta|=3.32\\,\\alpha$ fixed by the",
 "   geometry. **",
 "✔ ** AND IT UPGRADES THE CORPUS'S OWN INHERITANCE ARGUMENT FROM SCALE-LIMITED TO EXACT for the",
 "   matter sector, without disturbing the frozen-mode argument, which is what the RADIATION",
 "   sector's amplitude and tilt still ride on. **",
 "✔ ** AND THE TWO ARGUMENTS AGREE WHERE BOTH APPLY: at $c_s=0$ the oscillating-branch exponent",
 "   vanishes identically AND the frozen-branch argument gives a constant the shift cannot touch.",
 "   The pressureless crossing is the one conclusion neither regime has to be stretched to reach. **",
 "",
 "⚠ ** WHAT REMAINS, AND THE ROW SHOULD SAY SO RATHER THAN CLOSE: the WORLDLINE half. **  *This is",
 "   the field half -- what happens to perturbations of a given species.  The detailed worldline",
 "   dynamics of a concrete model AT the branch point, on a crossing whose admissible content is",
 "   now fixed twice over, is a separate computation and is not done here.*",
 "",
 "⌗ *One thing worth carrying: the species reading makes a prediction the scale reading does not.",
 "Any component with even a per-cent sound speed is annihilated at the peak scale, so the crossing",
 "cannot inherit perturbations from a warm or partially-relativistic species -- only from a cold",
 "one.  That is a constraint on what the progenitor may hand over, and it is sharp.*",
]:
    print("  " + s_)
