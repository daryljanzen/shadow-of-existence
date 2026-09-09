"""
P03_the_charged_collapse_does_not_form_the_eternal_inner_horizon
================================================================

Object under test -- `PO-25`, whose step is stated as a computation:

    "`P03`'s charged case is the ETERNAL Reissner--Nordstroem--de Sitter slicing
     function, a stationary geometry ... The question is whether a collapse of
     charged matter forms the eternal inner horizon at all --- real collapses are
     widely held not to, the inner horizon being unstable --- in which case the
     branch point survives dynamically and the charged case rejoins the bead."

"Widely held" is not a computation, and the corpus's setting is Lambda > 0, where
the answer is NOT the textbook Lambda = 0 one: with a cosmological horizon the
exterior perturbations decay EXPONENTIALLY rather than by Price power-law tails, so
the Cauchy horizon CAN survive, and near extremality it does.

** COMPUTES: the blueshift-versus-decay ratio beta = alpha / kappa_minus at the inner
horizon, across the charge range, against a threshold of 1/2 -- with alpha_max = 1/(4 M)
held as a GENEROUS CEILING on the spectral gap rather than a fitted value, so a beta below
threshold is an upper bound failing and not a tuned one, and with the near-extremal case
run as a CONTROL because there the Cauchy horizon is expected to survive.  Nothing here is
fitted to make the horizon form or not form.  Scope: the eternal Reissner-Nordstroem-de
Sitter slicing function at Lambda > 0; it does not reach the collapse dynamics itself. **

THE CRITERION.  The horizon's fate is a competition between the blueshift of
infalling perturbations, going as exp(kappa_- v), and their decay, exp(-alpha v),
with alpha the spectral gap.  The ratio

        beta = alpha / kappa_-

decides it.  beta > 1/2: the horizon survives with locally square-integrable
Christoffels, the eternal structure is reached.  beta < 1/2: the blueshift wins and
the eternal inner horizon is NOT formed.

COMPUTED HERE on the corpus's own progenitor, in BOTH charge readings the row
carries -- the row does not settle which is right and routes that fork to `PO-13`:

    r_-      = Q^2 / 2M                      inner horizon, small-Q limit
    kappa_-  = (r_+ - r_-) / 2 r_-^2         |f'(r_-)|/2 for RN
    alpha   <= 1/(4M)                        a GENEROUS ceiling on the spectral gap

The ceiling is deliberately generous: a smaller alpha only lowers beta, so the
verdict is an upper bound on the horizon's chances.

RESULT.  beta is below threshold by 250 orders on the intensive reading and 14 on
the extensive one.  ** The eternal Cauchy horizon is not formed, and the answer does
not depend on which reading of the charge is right. **  That DECOUPLES this row's
dynamical step from the datum fork `PO-13` carries.

WHAT THIS DOES NOT ESTABLISH, and the row must not be read as if it did.  Strong
cosmic censorship HOLDING means the maximal development is inextendible at the
Cauchy horizon.  That says the ETERNAL structure `P03` uses is not what a charged
collapse produces; it does NOT deliver a spacelike r=0 for the signed radius to pass
through.  ** So "the branch point survives dynamically" does not follow from this. **
What does follow is narrower and is the useful half: the obstruction `PO-25` records
is a property of a stationary solution the dynamical problem does not reach.  What
stands in its place -- the null weak singularity of mass inflation, and whether a
spacelike r=0 forms behind it -- is a numerical-relativity question and is NOT
computed here.

CONTROL.  The criterion must be able to return the other answer or it measures
nothing.  Near extremality kappa_- -> 0 and beta -> infinity, so the same formula
puts a near-extremal hole ABOVE threshold.  The progenitor is 4 orders (extensive)
to 63 orders (intensive) from extremal, so that regime is nowhere near -- but it
exists, and the check fires on it.
"""

import math

G, c, e = 6.67430e-11, 2.99792458e8, 1.602176634e-19
k_e, Msun, lP = 8.9875517873681764e9, 1.98847e30, 1.616255e-35

Q_per_e   = e*math.sqrt(G*k_e/c**4)        # one elementary charge, in metres
M_geo     = G*(2.33e23*Msun)/c**2          # P16's progenitor, in metres
alpha_max = 1/(4*M_geo)                    # generous ceiling on the spectral gap
THRESHOLD = 0.5


def inner_horizon(Qg, M=M_geo):
    """r_- = M - sqrt(M^2 - Q^2), written so it does not cancel.

    ** The naive form returns EXACTLY ZERO here and the receipt divides by it. **
    At Q/M ~ 1e-63 the subtraction M - sqrt(M^2 - Q^2) loses every significant
    digit in double precision.  The algebraically identical Q^2/(M + sqrt(...))
    has no cancellation at all.  Same class as the growing-mode potential's 0/0
    at small y, and the reason this receipt asserts against the row's own two
    published figures: an r_- that silently came out zero would have sailed
    through a check that only compared beta to a threshold.
    """
    d = M*M - Qg*Qg
    return Qg*Qg/(M + math.sqrt(d)) if d >= 0 else None


def kappa_minus(Qg, M=M_geo):
    r_m = inner_horizon(Qg, M)
    return math.sqrt(M*M - Qg*Qg)/(r_m*r_m)      # (r_+ - r_-)/2 r_-^2, uncancelled


READINGS = (('intensive', 1.0), ('extensive', 1e59))

print("  reading      Q/e        Q/M        r_- (m)      r_-/lP      beta        verdict")
print("  " + "-"*84)
for name, n in READINGS:
    Qg, r_m = n*Q_per_e, inner_horizon(n*Q_per_e)
    beta = alpha_max/kappa_minus(Qg)
    print(f"  {name:<11}{n:>7.0e}{Qg/M_geo:>11.2e}{r_m:>15.3e}{r_m/lP:>12.2e}"
          f"{beta:>12.2e}   {'CH survives' if beta > THRESHOLD else 'CH DESTROYED'}")
    assert beta < THRESHOLD, f"{name}: SCC must hold here"

for name, n in READINGS:
    Qg = n*Q_per_e
    assert abs(inner_horizon(Qg) - Qg**2/(2*M_geo))/inner_horizon(Qg) < 1e-6
print("\n  small-Q limit r_- = Q^2/2M agrees with the exact root to <1e-6     OK")

assert 1e19 < inner_horizon(1e59*Q_per_e) < 1e20, "extensive: the row's ~1e19 m"
assert 1e-65 < inner_horizon(Q_per_e)/lP < 1e-63, "intensive: the row's ~1e-64 lP"
print("  reproduces the row's own r_- figures, 1e19 m and 1e-64 lP          OK")

beta_ne = alpha_max/kappa_minus(0.9999*M_geo)
assert beta_ne > THRESHOLD, "the criterion must be non-vacuous"
print(f"  CONTROL near-extremal Q/M=0.9999: beta = {beta_ne:.3g} > 1/2 -> survives  OK")

print()
print("ESTABLISHED: on the corpus's own progenitor the eternal Cauchy horizon is NOT")
print("formed, in BOTH charge readings, by 250 and 14 orders -- so this row's")
print("dynamical step does not depend on the datum fork PO-13 carries.")
print("NOT ESTABLISHED: that a spacelike r=0 replaces it.")
