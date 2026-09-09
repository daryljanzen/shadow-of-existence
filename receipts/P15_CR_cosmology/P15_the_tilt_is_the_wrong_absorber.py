"""
P15_the_tilt_is_the_wrong_absorber
==================================

Object under test -- `PO-24`, whose remaining discharge reads: "whether a
displacement of that size in the inferred tilt is a tension -- a statement about a
joint fit, which is the whole of what remains", after r4505 found that a refit of
amplitude and tilt absorbs the diffusion-scale signature almost entirely in shape at
the cost of Delta n_s = -0.0304 against sigma = 0.00323.

** THE QUESTION AS POSED PRESUMES THE DISPLACEMENT IS A NUMBER.  IT IS A LOCAL SLOPE
   OF A CURVE, AND THE CURVE'S SLOPE VARIES BY A FACTOR OF SEVEN THOUSAND OVER THE
   DATA THE FIT IS SCORED ON. **

The signature is exp[-(l/l_D)^2 (r^2 - 1)] -- a Gaussian in l.  A tilt is a power
law.  So the tilt the signature LOCALLY mimics is

        dn_eff(l) = d ln(ratio) / d ln l = -2 (r^2 - 1) (l / l_D)^2

which is exact, and is not a constant: it grows as l^2.  Across plik_lite's own
declared span, l = 30 to 2508, it runs from -0.0002 to -1.31.

    ==> A single tilt is a ONE-PARAMETER fit to a function whose logarithmic slope
        varies by ~7000x over the fitted data.  ** Absorption is therefore necessarily
        WINDOW-LOCAL, and the fitted Delta n_s is a range-weighted average of a
        quantity that is nowhere equal to it. **

WHAT THAT DOES TO THE ROW'S QUESTION, and it dissolves rather than answers it:

  * ** "Is a displacement of that size a tension?" is not well posed against a
    constant-tilt prior. **  A joint fit does not encounter a shifted tilt; it
    encounters a residual whose SHAPE is Gaussian in l, and no tilt removes a
    Gaussian.  What the joint fit will weigh is that residual, which r4505 already
    bounds from above at 0.26 sigma per bin -- and that bound, not the displacement,
    is the thing with a verdict attached.

  * ** And a displacement in n_s is not by itself a tension here, because n_s is not
    predicted. **  `P15` states A_s and the tilt n_s are "inherited as boundary data
    exactly as flat LambdaCDM inherits the baryon-to-photon ratio".  A different
    value of an inherited input is a different input, not a conflict.  What could be
    a conflict is a constraint on n_s that does NOT run through the damping tail --
    the low-to-mid-l shape, TE/EE, lensing -- which is precisely what "a joint fit"
    means and is the row's own discharge, now with its reason attached.

WHY THE ABSORPTION LOOKED GOOD, mechanically: over the fitted window ln(ratio) is
small -- 0.1% at l=100, 2.6% at l=500 -- and only becomes large where the window
ends.  ** The window the refit used is the one where dn_eff is smallest. **

NOT A FINDING, and recorded because it nearly was: "the fitted range stops short of
where the signature lives" is ALREADY WORKED.  `C51` establishes that the thirty
bins the arm drops are l = 1759-2508 and ARE the damping tail, and it is DISCHARGED
at r2780 -- the LMAXL=2512 extension was run, recovered them, and moved the verdict
in the disfavouring direction.  ** Reading one more receipt in the same directory is
what stopped that being reported as new. **

CONTROL.  At r = 1 -- no signature -- dn_eff vanishes identically at every l and the
whole construction is silent, so what is measured is the signature and not an
artefact of writing a Gaussian in logarithmic variables.
"""

import numpy as np

r, lD = 1.0926, 1362.0          # P15's damping ratio and damping multipole
k = r**2 - 1
LMIN, LMAX = 30, 2508           # plik_lite TT's own declared span
CEILING = 1759                  # where the 185-bin arm stops (C51)


def suppression(l, ratio=r):
    return np.exp(-(ratio**2 - 1)*(l/lD)**2)


def dn_eff(l, ratio=r):
    """d ln(ratio)/d ln l -- the tilt the signature LOCALLY mimics.  Exact."""
    return -2*(ratio**2 - 1)*(l/lD)**2


# --- the profile ----------------------------------------------------------------
print(f"  r = {r}, r^2-1 = {k:.4f}, l_D = {lD:.0f}\n")
print(f"  {'l':>6}{'suppression':>14}{'dn_eff':>11}")
print("  " + "-"*33)
for l in (30, 100, 300, 500, 1000, 1296, CEILING, 2200, LMAX):
    mark = "   <- 185-bin ceiling" if l == CEILING else ""
    print(f"  {l:>6}{suppression(l):>14.4f}{dn_eff(l):>11.4f}{mark}")

# --- (1) the slope is not a constant, by a factor of ~7000 -----------------------
swing = dn_eff(LMAX)/dn_eff(LMIN)
assert abs(swing - (LMAX/LMIN)**2) < 1e-9, "the swing is exactly (l_max/l_min)^2"
print(f"\n(1) dn_eff runs {dn_eff(LMIN):.5f} -> {dn_eff(LMAX):.4f} over l={LMIN}-{LMAX}")
print(f"    a factor of {swing:.0f}, exactly (l_max/l_min)^2                OK")
assert swing > 1000, "a single tilt cannot represent this"

# --- (2) the fitted window is where the slope is smallest ------------------------
assert abs(dn_eff(CEILING)) < abs(dn_eff(LMAX)), "the ceiling truncates the steep part"
print(f"(2) at the ceiling dn_eff = {dn_eff(CEILING):.4f}; beyond it it reaches"
      f" {dn_eff(LMAX):.4f}")
print(f"    the window used is where the mimicked tilt is smallest       OK")

# --- (3) the reported displacement lies inside the range it averages -------------
reported = -0.0304
assert dn_eff(LMAX) < reported < dn_eff(LMIN), \
    "the reported Delta n_s must lie between the endpoint slopes"
lo = np.sqrt(abs(reported)/(2*k))*lD
print(f"(3) the reported Delta n_s = {reported} equals dn_eff at l = {lo:.0f} only")
print(f"    -- one multipole out of {LMIN}-{LMAX}                          OK")

# --- CONTROL: no signature, no slope ---------------------------------------------
assert all(dn_eff(l, ratio=1.0) == 0.0 for l in (30, 500, 2508))
print("    CONTROL r=1: dn_eff vanishes at every l, the test is silent   OK")

print()
print("ESTABLISHED: the signature's mimicked tilt varies by ~7000x across the data,")
print("so absorption by a single tilt is window-local and the fitted displacement is")
print("a range-weighted average equal to the true slope at ONE multipole.")
print("SO the row's question is not well posed against a constant-tilt prior: a joint")
print("fit meets a Gaussian-shaped residual, not a shifted tilt -- and n_s is")
print("INHERITED here, so a displacement in it is not by itself a conflict.")
