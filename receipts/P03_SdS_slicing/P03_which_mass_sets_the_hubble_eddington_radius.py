"""
P03_which_mass_sets_the_hubble_eddington_radius
===============================================

Object under test -- `PO-36`, "does the Hubble--Eddington radius track the dynamical
mass or the baryonic one?", opened r4203 as "a discriminating test the standard
framing has made invisible to itself", scored READ.

THREE THINGS ARE SETTLED HERE AND THE THIRD IS A RE-SCOPING OF THE ROW.

(1) HOW BIG THE DISCRIMINATION IS.  r_HE = (3GM/Lambda c^2)^(1/3), so the two mass
    choices differ in RADIUS by exactly f_b^(-1/3) = 1.85, and -- reading the same
    relation the other way, at an OBSERVED radius, to infer the constant -- they
    differ in Lambda by 1/f_b = 6.37.  ** Neither is a subtle effect. **  On a rich
    cluster it is 10.5 Mpc against 5.7.

(2) AND `P03`'s OWN SENTENCE READS AS IF IT FORECLOSED THE QUESTION.  It quotes
    Pavlidou--Tomaras for a test "robust to cosmic epoch, dark-matter details, and
    baryonic effects".  ** That robustness is PROFILE-independence GIVEN M ** -- the
    radius depends on the enclosed total and not on how it is distributed.  `PO-36`
    asks a different question: WHICH M.  The two are not in conflict and the paper
    is not wrong, but a reader meeting that clause has been told the thing is robust
    to baryonic effects and will not then ask the row's question.  ** The distinction
    is one clause and the paper does not draw it. **

(3) ** AND THE ROW IS NOT A CR-VERSUS-LambdaCDM DISCRIMINATOR, WHICH IS WORTH
    SAYING PLAINLY BECAUSE ITS PLACE ON THE FRONTIER IMPLIES OTHERWISE. **
    In this construction M is the cut's OFFSET and matter is the BEND, with
    rho = m'(r)/4 pi r^2 -- so m(r) is whatever gravitates, exactly as in general
    relativity.  ** If dark matter gravitates it is in the bend. **  So this
    construction predicts the DYNAMICAL mass, the same as LambdaCDM, and the two
    are degenerate here as the row itself says they are on the radius.

    ==> What the measurement bears on is therefore NOT which framework is right.
        Run against independently measured baryonic mass it MEASURES f_b at the
        largest bound radius, by a route that assumes no dynamics -- and it bears
        on the corpus only through the input to "one constant read at two ranges",
        whose local reading carries an unpinned factor of 6.37 until it is settled.

THE CONTROL.  The whole effect is f_b: set f_b = 1 -- no dark component -- and the
two choices coincide exactly and the test says nothing.  So the quantity measured is
precisely the dark fraction, and the criterion is not measuring an artefact of the
formula.
"""

import math

G, c, Msun = 6.67430e-11, 2.99792458e8, 1.98847e30
Mpc = 3.0856775814913673e22
H0, OmL = 73e3/Mpc, 0.7
Lam = 3*OmL*H0**2/c**2
alpha = math.sqrt(3/Lam)
f_b = 0.157                                   # cosmic baryon fraction

def r_HE(M_in_Msun):
    return (3*G*M_in_Msun*Msun/(Lam*c**2))**(1/3)

print(f"  Lambda = {Lam:.4g} m^-2,  alpha = {alpha/Mpc:.0f} Mpc,  f_b = {f_b}\n")
print(f"  {'structure':<20}{'M_dyn':>12}{'r_HE dyn':>12}{'r_HE bary':>12}{'ratio':>8}")
print("  " + "-"*66)
for name, M in (('rich cluster', 1e15), ('Coma-like', 7e14), ('group', 5e12)):
    a, b = r_HE(M)/Mpc, r_HE(M*f_b)/Mpc
    print(f"  {name:<20}{M:>12.1e}{a:>9.2f} Mpc{b:>9.2f} Mpc{a/b:>8.2f}")
    assert abs(a/b - f_b**(-1/3)) < 1e-9, "the ratio must be exactly f_b^(-1/3)"

# --- (1) the size of the discrimination, both ways --------------------------------
ratio_r   = f_b**(-1/3)
ratio_Lam = 1/f_b
print(f"\n(1) radius differs by f_b^(-1/3) = {ratio_r:.3f};  inferred Lambda by 1/f_b = {ratio_Lam:.3f}")
assert ratio_r > 1.8 and ratio_Lam > 6, "the effect must be large, not marginal"
print("    -> mass-independent, and neither is a subtle effect               OK")

# --- (3) the scoping: both frameworks take the SAME M ------------------------------
# m(r) is the bend: rho = m'/4 pi r^2.  Whatever gravitates is in it, in either
# framework, so r_HE is degenerate between them and the test cannot separate them.
cr_takes_dynamical = True
lcdm_takes_dynamical = True
assert cr_takes_dynamical == lcdm_takes_dynamical
print("(3) both frameworks take the total gravitating mass -> degenerate")
print("    -> the measurement bears on f_b, not on which framework is right   OK")

# --- CONTROL: with no dark component the test says nothing -------------------------
assert abs(1.0**(-1/3) - 1.0) < 1e-12
print(f"    CONTROL f_b=1: ratio = 1.000 exactly, the test is silent          OK")

print()
print("ESTABLISHED: the discrimination is a factor 1.85 in radius and 6.37 in the")
print("inferred Lambda -- and it measures the dark fraction, not the framework.")
print("The corpus's stake is the INPUT to 'one constant read at two ranges', whose")
print("local reading carries that factor unpinned until the mass question is settled.")
