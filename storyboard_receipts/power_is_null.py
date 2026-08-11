"""
THE KEYSTONE (r1107) — c40's claim, verified from scratch.

I found: power = |X|^2 - alpha^2 = X0^2 on the hyperboloid. An identity.
c40 took the step I did not:

    "power = X0^2 isn't a curiosity. IT'S THE NULL CONDITION.
     The tangent length L = sqrt(power) = |X0|. A null line in the embedding has
     spatial length = time drop. The tangent from the hinge runs sqrt(3) alpha
     across and drops sqrt(3) alpha down. ds^2 = -dX0^2 + L^2 = 0 exactly.
     THE TANGENT LINES ARE NULL BECAUSE THE POWER IS X0^2. Power-of-a-point in
     the overhead IS the null condition in the embedding -- the same equation.
     So when Daryl said 'it's all optics' -- it isn't a metaphor. The sightlines
     from the hinge are LIGHT RAYS. The whole kaleidoscope is the hinge's causal
     past and future, projected."

Two claims, and they are different sizes:
  (i)  the TANGENT length from any point equals |X0| of that point;
  (ii) therefore the tangent lines are NULL in the embedding.
(i) is a two-line identity. (ii) is a claim about ds^2 and must be checked as one,
because "spatial length = time drop" is only the null condition if the spatial
length in question is the length of the ACTUAL segment in the embedding.
"""
import numpy as np

a = 1.0

def X0_of(R):
    """height on the hyperboloid -X0^2 + |X|^2 = a^2 at overhead radius R"""
    return np.sqrt(R**2 - a**2)

print("="*78)
print("(i)  TANGENT LENGTH = |X0| ?   Checked at every height, not just the hinge.")
print("="*78)
print(f"  {'R (overhead)':>13} {'X0 = sqrt(R^2-a^2)':>20} {'L = sqrt(power)':>17}  equal?")
for R in (1.2, 1.5, 2.0, 2.5, 3.0, 5.0):
    X0 = X0_of(R)
    L = np.sqrt(R**2 - a**2)              # tangent length from external point to circle
    print(f"  {R:>13.3f} {X0:>20.6f} {L:>17.6f}  {np.isclose(X0, L)}")
print()
print("  Both are sqrt(R^2 - a^2). It is an IDENTITY, not a coincidence:")
print("    tangent length^2 = |P|^2 - a^2   (Euclid: the tangent-secant theorem)")
print("    X0^2             = |X|^2 - a^2   (the hyperboloid's own equation)")
print("  SAME RIGHT-HAND SIDE.  >> (i) CONFIRMED, at every height.")

print()
print("="*78)
print("(ii) ARE THE TANGENT LINES NULL?  This is the real claim. Check ds^2 properly.")
print("="*78)
print("  Set up the actual segment in the embedding R^{1,2}, not a slogan.")
print("  The hinge H sits at overhead radius R=2a, height X0 = sqrt(3) a.")
print("  Its tangent to the throat touches at T, which sits ON the throat: X0(T) = 0.")
print()
R = 2*a
X0_H = X0_of(R)
# overhead geometry: tangent point T on the circle of radius a, from external P at distance R
# |PT| = sqrt(R^2 - a^2), and OT _|_ PT
theta_T = np.arccos(a/R)                      # angle at O between OP and OT
H_over = np.array([R, 0.0])
T_over = np.array([a*np.cos(theta_T), a*np.sin(theta_T)])
L_spatial = np.linalg.norm(H_over - T_over)
dX0 = X0_H - 0.0
print(f"  H (overhead) = ({H_over[0]:.4f}, {H_over[1]:.4f})   X0 = {X0_H:.6f} = sqrt(3) a")
print(f"  T (overhead) = ({T_over[0]:.4f}, {T_over[1]:.4f})   X0 = 0        (on the throat)")
print()
print(f"  SPATIAL separation |H - T| in the overhead plane : {L_spatial:.6f}")
print(f"  TIME drop          |X0(H) - X0(T)|              : {dX0:.6f}")
print(f"  equal?  {np.isclose(L_spatial, dX0)}")
print()
ds2 = -dX0**2 + L_spatial**2
print(f"  ds^2 = -dX0^2 + |dX|^2 = -{dX0**2:.6f} + {L_spatial**2:.6f} = {ds2:.2e}")
print(f"  >> NULL?  {np.isclose(ds2, 0.0)}   ** (ii) CONFIRMED. **")

print()
print("="*78)
print("(iii) IS IT AN ACCIDENT OF THE HINGE'S HEIGHT? Test every external point.")
print("="*78)
rng = np.random.default_rng(5)
worst = 0.0
for _ in range(600):
    R = rng.uniform(1.0001, 12.0)
    X0 = X0_of(R)
    th = np.arccos(a/R)
    P = np.array([R, 0.0]); T = np.array([a*np.cos(th), a*np.sin(th)])
    ds2 = -X0**2 + np.linalg.norm(P - T)**2
    worst = max(worst, abs(ds2))
print(f"  600 random external points, tangent to the throat: max |ds^2| = {worst:.2e}")
print("  >> NULL FOR EVERY POINT AT EVERY HEIGHT. Not the hinge's accident.")
print()
print("  ** THEOREM (c40's, verified): on the de Sitter hyperboloid, the TANGENT LINE")
print("     from any point to the throat is a NULL line of the embedding. **")
print("     Proof, and it is two lines:")
print("       tangent length^2 = |X|^2 - a^2   (Euclid, in the overhead projection)")
print("       X0^2             = |X|^2 - a^2   (the hyperboloid, in the embedding)")
print("       => (spatial length)^2 = (time drop)^2  =>  ds^2 = -dX0^2 + dX^2 = 0.")
print("     THE POWER OF A POINT AND THE NULL CONDITION ARE THE SAME EQUATION.")

print()
print("="*78)
print("(iv) WHAT IT MEANS — and the one place I will not follow c40 without a check")
print("="*78)
print("  EARNED: 'it's all optics' is NOT a metaphor. A sightline from the hinge to the")
print("  throat IS a light ray. The construction's tangency conditions ARE null")
print("  conditions. That is why a hole, a point and a swing generate the whole figure:")
print("  ** the point's optical power and its height are ONE NUMBER, so its optics and")
print("     its causal structure are the SAME construction. **")
print()
print("  AND IT EXPLAINS THE HINGES, which were previously a stipulation: the storyboard")
print("  says 'a hinge at X = 2a, which on the hyperboloid FORCES X0 = +/- sqrt(3) a'.")
print("  Now: the hinge's tangent length IS sqrt(3) a IS its height IS its power's root.")
print("  Three statements, one fact. The 2a placement was never a choice about optics --")
print("  it is a choice about HEIGHT, and the optics follows.")
print()
print("  NOT YET CHECKED, and c40 asserts it: 'the whole kaleidoscope is the hinge's")
print("  CAUSAL PAST AND FUTURE, projected.' The tangents are null -- verified. That the")
print("  FIGURE is the hinge's light cone requires that the construction's OTHER lines")
print("  (the 45-deg chords, the pin, the hinge triangle's edges) are also null, and they")
print("  are NOT all tangents. A tangent is null; a secant is not. So the claim is right")
print("  for the tangent lines and is NOT established for the figure as a whole.")
print("  ** The sightlines that TOUCH are light rays. The ones that CUT are not. **")
print("  (Which is itself interesting: the power theorem is about SECANTS -- PX.PY --")
print("   and the null condition is the DEGENERATE case where X=Y. The tangent is where")
print("   the secant's two points merge, and that is exactly where the light cone is.)")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  The file printed booleans and a max; nothing could fail.  Note
# also that (i)'s table compares X0_of(R) with np.sqrt(R**2 - a**2) -- the same expression twice
# -- so the first block below re-derives the TANGENT LENGTH by a route that does not mention the
# hyperboloid at all: bisect (T - P).T = 0 for the tangency point on the throat, then measure
# |P - T|.  That is Euclid's side; X0_of(R) is the embedding's side; the claim is that they
# agree.  Then (ii)'s hinge ds^2 = 0 and (iii)'s 600-point maximum are pinned to the figure the
# paper prints, 5.7e-14.
def _bisect(g, lo, hi, n=200):
    for _ in range(n):
        mid = 0.5*(lo + hi)
        if g(lo)*g(mid) <= 0: hi = mid
        else: lo = mid
    return 0.5*(lo + hi)
for R_a in (1.2, 1.5, 2.0, 2.5, 3.0, 5.0):
    th_a = _bisect(lambda th: a*a - a*R_a*np.cos(th), 0.0, np.pi/2)   # tangency: (T - P).T = 0
    T_a = np.array([a*np.cos(th_a), a*np.sin(th_a)])
    L_a = np.linalg.norm(T_a - np.array([R_a, 0.0]))                  # Euclid's tangent length
    assert abs(L_a - X0_of(R_a)) < 1e-9                               # = the embedding height
    assert abs(-X0_of(R_a)**2 + L_a**2) < 1e-9                        # so the segment is NULL
assert abs(L_spatial - 1.7320508) < 1e-6 and abs(dX0 - 1.7320508) < 1e-6   # sqrt(3) alpha
assert abs(L_spatial - dX0) < 1e-12                                   # Euclid = hyperboloid
assert abs(ds2) < 1e-12                                               # (ii) the hinge is null
assert 5.675e-14 < worst < 5.690e-14                                  # (iii) the paper's 5.7e-14
# CONTROL: a SECANT, not a tangent, is not null -- the aim that cuts the throat at impact
# parameter alpha/2 has ds^2 = -X0^2 + |P - X|^2 far from zero, so the test can fail.
R_c = 2*a; b_c = a/2
t_c = np.sqrt(R_c**2 - b_c**2) - np.sqrt(a**2 - b_c**2)               # to the NEAR intersection
assert abs(-X0_of(R_c)**2 + t_c**2) > 0.5
print()
print(f"  [r2376+c54.161] asserted: tangent length (bisected tangency, Euclid) = X0 at six radii,")
print(f"  ds^2 = 0 at the hinge, max |ds^2| over the 600 heights = {worst:.2e} (the paper's 5.7e-14),")
print("  and a SECANT control that is NOT null.")
