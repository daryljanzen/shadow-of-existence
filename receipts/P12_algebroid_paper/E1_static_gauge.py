"""E1 — WHY DOES A PROGRAMME BUILT ON CUTS CARRY NO EXTRINSIC CURVATURE?
BASELINE (checked against r1838, and one hit was my OWN r1908 insertion, excluded):
  HAS: foliation x233 · leaf/leaves x325 · lapse x118 · shift x90 · hypersurface x59 ·
       embedding x53 · ADM x25 · induced metric x6 · momentum constraint x5 · totally geodesic x2
  HAS NOT: second fundamental form x0 · extrinsic curvature x0 · K_{ab} x0 · Gauss-Codazzi x0 ·
       junction condition x0 · mean curvature x0 · shape operator x0
That is a great deal of ADM apparatus with none of ADM's central object.  WHY?
ORIGIN: storyboard_receipts/E1_static_gauge.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp
print("="*80); print("E1 — THE STATIC GAUGE IS WHY"); print("="*80)
print("""
STEP 1 — THE PUZZLE, stated exactly.
  In ADM the Hamiltonian constraint is  H = sqrt(h) ( K_ab K^ab - K^2 - R + 2 Lambda ) = 0,
  carrying BOTH the intrinsic curvature R and the extrinsic K_ab.
  But P12 anchors it purely intrinsically: 'ENERGY (the leaf) = the Hamiltonian constraint, matter
  the leaf's INTRINSIC-CURVATURE departure from the round substrate leaf.'
  *** SO WHERE DID THE K-TERMS GO? ***
""")
print("STEP 2 — COMPUTE K_ab FOR THE CORPUS'S OWN CUTS.")
t,r,th=sp.symbols('t r theta'); M,al=sp.symbols('M alpha', positive=True)
f=1-2*M/r-r**2/al**2
print("   P8's sector, in its own words: 'everything proven here is STATIC and spherically symmetric.'")
print(f"   ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2 ,  f = {f}")
print("   For the t = const leaves: lapse N = sqrt(f), shift N^i = 0, and h_ab is t-INDEPENDENT.")
print("   The ADM extrinsic curvature is  K_ab = (1/2N)( d_t h_ab - D_a N_b - D_b N_a ).")
print("     d_t h_ab = 0   (static: nothing depends on t)")
print("     N^i = 0        (no shift: the metric is diagonal, no dt dr or dt dphi cross term)")
print("   =>  K_ab = 0  IDENTICALLY on every leaf of the static slicing.")
print()
print("   *** SO FOR THE ENTIRE STATIC SECTOR THE EXTRINSIC CURVATURE VANISHES, THE HAMILTONIAN")
print("       CONSTRAINT REDUCES TO  R = 2 Lambda + 16 pi rho , AND P12's PURELY INTRINSIC ANCHOR")
print("       IS EXACTLY RIGHT. ***")
print("   And it explains two things the corpus states without connecting them:")
print("     - Q6/K9's 'Type O: the cut is TOTALLY GEODESIC' -- totally geodesic IS K_ab = 0;")
print("     - P8's scope line, 'everything proven here is static and spherically symmetric', is")
print("       precisely the condition under which the missing object is missing because it is ZERO.")
print("""
STEP 3 — AND THE COSMOLOGICAL SECTOR IS NOT STATIC, SO THE QUESTION RETURNS THERE.
  The observable cosmology is the sinh^{2/3} law: the leaves EXPAND, so K_ab != 0 on them.
  How does the corpus carry that without K?  BY THE LAPSE.  Section 1-LEVELS, L1: 'the FOLIATION
  STACKING RATE -- the existent's own geometric expansion', and P7: 'the LAPSE N is the existent's
  rate of advance, the foliation stacking rate the observable expansion rides.'
  *** SO THE CORPUS CARRIES THE EXPANSION IN THE LAPSE RATHER THAN IN THE EXTRINSIC CURVATURE. ***
  For an FLRW leaf those are the same information -- K = -3 H for the standard slicing, and H is the
  stacking rate -- so nothing is lost; it is carried in a different variable.
""")
H=sp.Function('H'); a=sp.Function('a'); tau=sp.Symbol('tau')
print("   Check the identification on FLRW: h_ij = a(tau)^2 delta_ij, N = 1, shift 0:")
print("     K_ij = (1/2) d_tau (a^2) delta_ij = a a' delta_ij ;  K = h^ij K_ij = 3 a'/a = 3H")
print("   -> the trace of the extrinsic curvature IS three times the stacking rate. Same content.")

# r2376+c54.158 -- E1 STATED all three of its steps and computed none of them.  The blocks below
# compute exactly the three printed sentences, from the metric, and pin them.
phi = sp.Symbol('phi')
def christoffel(gm, xs):
    n = len(xs); gi = gm.inv()
    return [[[sp.simplify(sum(gi[l, s]*(sp.diff(gm[s, i], xs[j]) + sp.diff(gm[s, j], xs[i])
                              - sp.diff(gm[i, j], xs[s])) for s in range(n))/2)
              for j in range(n)] for i in range(n)] for l in range(n)]

# STEP 2, from the 4-metric rather than from the words.  For the hypersurface-orthogonal static
# normal n_mu = (-sqrt(f), 0, 0, 0) the extrinsic curvature is K_ab = sqrt(f) Gamma^t_ab, so
# "K_ab = 0 on every leaf of the static slicing" is exactly the statement that every Christoffel
# symbol with an upper t and two SPATIAL lower indices vanishes.  Computed on
# g = diag(-f, 1/f, r^2, r^2 sin^2 th) with f = 1 - 2M/r - r^2/alpha^2: all 9 vanish, for every M
# and every alpha.  CONTROL: Gamma^t_{tr} = f'/2f is NOT zero -- the vanishing above is staticity
# and not an empty Christoffel array.
Gam4 = christoffel(sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2), [t, r, th, phi])
assert all(Gam4[0][i][j] == 0 for i in range(1, 4) for j in range(1, 4)), Gam4[0]
assert sp.simplify(Gam4[0][0][1] - sp.diff(f, r)/(2*f)) == 0 and Gam4[0][0][1] != 0

# STEP 2's consequence, the sentence "THE HAMILTONIAN CONSTRAINT REDUCES TO R = 2 Lambda".  With
# K_ab = 0 the constraint is R^(3) = 2 Lambda + 16 pi rho, so in vacuum the leaf's INTRINSIC scalar
# curvature must come out at 2 Lambda = 6/alpha^2 -- pinned to that figure, and note that M drops
# out entirely (a Schwarzschild slice is scalar-flat), which is why P12's intrinsic anchor can read
# matter as the leaf's DEPARTURE from the round substrate leaf.
h3 = sp.diag(1/f, r**2, r**2*sp.sin(th)**2); x3 = [r, th, phi]
C3 = christoffel(h3, x3); gi3 = h3.inv()
Ric3 = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        Ric3[i, j] = sp.simplify(sum(sp.diff(C3[l][i][j], x3[l]) - sp.diff(C3[l][i][l], x3[j])
                     + sum(C3[l][l][s]*C3[s][i][j] - C3[l][j][s]*C3[s][i][l] for s in range(3))
                     for l in range(3)))
R3 = sp.simplify(sum(gi3[i, j]*Ric3[i, j] for i in range(3) for j in range(3)))
assert sp.simplify(R3 - 6/al**2) == 0, R3
assert sp.simplify(sp.diff(R3, M)) == 0, R3

# STEP 3's identification, K = 3H.  h_ij = a(tau)^2 delta_ij, lapse 1, zero shift, so
# K_ij = (1/2) d_tau h_ij and its trace is h^ij K_ij.  Pinned to THREE times the stacking rate --
# the factor 3 is the leaf's dimension, and it is what makes "carried in the lapse" the same
# information rather than a weaker one.
hF = sp.diag(a(tau)**2, a(tau)**2, a(tau)**2)
Ktrace = sp.simplify(sum(hF.inv()[i, i]*sp.diff(hF[i, i], tau)/2 for i in range(3)))
assert sp.simplify(Ktrace - 3*sp.diff(a(tau), tau)/a(tau)) == 0, Ktrace
print("="*80)
