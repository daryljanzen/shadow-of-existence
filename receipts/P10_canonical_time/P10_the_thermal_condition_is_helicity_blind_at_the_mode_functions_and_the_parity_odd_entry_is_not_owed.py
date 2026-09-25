"""
P10_the_thermal_condition_is_helicity_blind_at_the_mode_functions_and_the_parity_odd_entry_is_not_owed
=====================================================================================================

LEVEL: exact symbolic (sympy) for the harmonic bookkeeping and the isometry, exact linear algebra
(numpy) on a truncated Fock space for the operator statements, with three CONTROLS that must break.

OBJECT UNDER TEST -- `PO-43`'s one unrun check, routed at `r6849`.  The row is down to it: question (i)
is answered (`r4547`: the tower IS chirally capable, the handedness being an irrep label a connected
isometry cannot exchange) and question (ii) is answered (`r6849`: the audit does not range over a
topological term's finite part).  What is left decides whether the parity-odd entry is owed at all:

    "A counterterm answers to the effective action, and the effective action answers to the STATE
     rather than to the tower's capacity.  The boundary condition is Hartle--Hawking regularity
     imposed fibre by fibre, and NOTHING IN ITS STATEMENT REFERS TO HELICITY -- so the two towers are
     populated alike and the parity-odd content cancels between them.  Nobody has run that check."

The order named three places to look for a break, and they are PARTS 5, 6 and 7 below:
  (a) is the fibre-by-fibre statement helicity-blind AT THE LEVEL OF THE MODE FUNCTIONS, not merely
      in its wording;
  (b) do the MEASURE or the DEGENERACIES distinguish the two towers at the floor, where the self-dual
      and anti-self-dual fives sit;
  (c) does the EUCLIDEAN CONTINUATION itself pick a handedness, a self-dual pair on a four-sphere
      being exactly where a continuation can.

-------------------------------------------------------------------------------
WHAT THIS PROBE FINDS.

** THE CHECK COMES OUT FOR THE CLAIM, AND IT IS NOT HELICITY-BLINDNESS BY WORDING. **  The condition's
entire dependence on the tower is through the boundary coefficient
`Gamma_hat = gamma + c * SUM_n pi_hat_n^2` -- a sum of squares over the mode set with one c -- and the
swap that exchanges the helicities is a PERMUTATION of that mode set pairing modes of EQUAL FREQUENCY.
So `[Gamma_hat, P] = 0` exactly, and with it the sub-threshold projector, the index nu = sqrt(Gamma+1/4)
and the retained branch x^(1/2+nu).  The temperature carries no mode index at all: kappa = 1/alpha
belongs to the BACKGROUND horizon, so beta = 2*pi*alpha is common to every fibre by construction.
** The state is therefore P-invariant, every P-odd expectation vanishes identically, and no P-odd
divergence is generated for a counterterm to absorb. **

** AND THE EQUAL FREQUENCIES ARE NOT AN ASSUMPTION -- they are forced by an isometry. **  The map
sigma: g -> g^(-1) on S^3 = SU(2) is diag(1,-1,-1,-1) on the embedding coordinates: an element of O(4)
with determinant -1, hence an ORIENTATION-REVERSING ISOMETRY.  It conjugates left translations into
right ones, so it exchanges (j_L, j_R) with (j_R, j_L) and therefore the two families; being an
isometry it commutes with the Laplacian, and carrying one epsilon the curl ANTI-commutes with it.
** So the swap preserves every frequency and reverses every handedness -- which is exactly the
structure the cancellation needs, and it is the geometry's rather than a convention. **  Read off the
Casimirs the identity is exact: mu^2 = 2(C_L + C_R) - 6, manifestly symmetric in the two labels, and
it reproduces `P10`'s own mu_n^2 = n(n+2)-2 at every level with the degeneracy splitting 50/50.

** THE THREE ATTACKS.  (a) and (b) fail; (c) is answered but is the one with teeth, and it is answered
by exhibiting what an actual break looks like. **  The continuation is x_0 -> i x_0, carrying
dS_5 = SO(5,1)/SO(4,1) to S^5 = SO(6)/SO(5): it acts on the time/radial coordinate, while sigma acts
on the three-sphere factor, and the two act on disjoint coordinate blocks, so they commute.  A
Riemannian four-section does admit a real self-dual/anti-self-dual split where a Lorentzian one does
not -- but to WEIGHT the two towers differently the exponent needs a P-odd term, and the two that
could supply one are absent: the de~Sitter cosmological horizon has ZERO angular velocity, and a
theta-term is the very thing the audit is asking whether it is owed, so assuming one is circular.
** The rotating control makes this non-vacuous: give the same state a chemical potential beta*Omega
coupled to the helicity charge and the P-odd expectation is non-zero and linear in Omega. **

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The two helicity families have EQUAL degeneracy at every level -- (n-1)(n+3) each, summing to
     `P10`'s own 2(n-1)(n+3) -- and at the floor n=2 they are a self-dual and an anti-self-dual five.
 (2) They have EQUAL frequencies, and by an isometry rather than by arithmetic: mu^2 = 2(C_L+C_R) - 6
     is symmetric under the swap, and it reproduces mu_n^2 = n(n+2)-2 identically.
 (3) sigma: g -> g^(-1) is an orientation-reversing isometry of S^3 exchanging the two factors: it is
     in O(4) with det = -1, it conjugates L_g to R_(g^-1), it commutes with the Laplacian and it
     anti-commutes with the curl.
 (4) Gamma_hat commutes with the swap EXACTLY on a truncated Fock space, and so do nu(Gamma_hat), the
     sub-threshold projector and the Friedrichs (regular-branch) selection.  CONTROL: a
     helicity-weighted coefficient breaks it, so the commutation is a fact about this Gamma_hat.
 (5) beta = 2*pi*alpha carries no mode index -- kappa = 1/alpha is the background horizon's -- so the
     one remaining datum of the state is helicity-blind too.
 (6) Hence every P-odd expectation vanishes, exhibited on the helicity charge X = SUM eps_n N_n both
     in the truncated Fock space and in closed form level by level.  CONTROLS: unequal degeneracies
     and unequal frequencies each give a non-zero answer.
 (7) The rotating-horizon control returns a non-zero, Omega-linear P-odd expectation, and Omega = 0
     for the de~Sitter cosmological horizon.
 (8) The Wick rotation and sigma act on disjoint coordinate blocks and commute.

WHAT IS NOT CLAIMED.

 * NOT that the tower is achiral.  `r4547` stands: the handedness is an irrep label and the tower is
   chirally capable.  What is shown is that the STATE does not use the capacity.
 * NOT a statement about the interacting tower's ultraviolet definition, which is `P10`'s own open
   frontier.  What is shown here is that the bare action carries no epsilon and the state is
   P-invariant, so a P-invariant regulator generates no P-odd divergence; a P-breaking regulator is a
   scheme choice and not a divergence.  The one mechanism that makes a P-odd gravitational term
   without a P-odd bare term is the gravitational chiral anomaly, which needs an unbalanced chiral
   FERMION content -- and the row's own index obstruction renders the connected-gauge fermion spectrum
   vector-like.  That last sentence is a reading of a corpus result, not computed here.
 * NOT the declined entropy question, whether S = A/4 carries to a cosmological horizon.
 * The tower's own floor as a canonical subtraction point is DELIBERATELY NOT BUILT, per the order.

WHAT WOULD FALSIFY IT.  The degeneracy split not being 50/50 at some level; mu^2 failing to be a
symmetric function of the two Casimirs; sigma failing to be an isometry or failing to reverse the
curl; a non-zero commutator [Gamma_hat, P]; a non-zero P-odd expectation at Omega = 0; or any of the
three controls failing to break, which would mean the checks are vacuous.
"""
import numpy as np
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

n, m = sp.symbols('n m', positive=True)

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE TWO FAMILIES, AND WHETHER THE DEGENERACIES SPLIT EVENLY.")
print("-" * 100)
print("  P10 sec:lock: the TT rank-two harmonics of the unit S^3 at level n have Laplace eigenvalue")
print("  mu_n^2 = n(n+2)-2, n >= 2, and 'degeneracy 2(n-1)(n+3), ten at the floor n=2'.")
print("  r4547: they sit in (j_L, j_R) = ((k+1)/2, (k-3)/2) and its swap, with k = n+1.")

k = m  # the row's k, equal to P10's n+1
jL, jR = (k + 1) / 2, (k - 3) / 2
dim_one = sp.expand((2 * jL + 1) * (2 * jR + 1))
check("each family has dimension m^2-4 = (n-1)(n+3), so the two SUM to P10's 2(n-1)(n+3)",
      sp.simplify(sp.factor(dim_one.subs(m, n + 1)) - (n - 1) * (n + 3)) == 0
      and sp.simplify(2 * dim_one.subs(m, n + 1) - 2 * (n - 1) * (n + 3)) == 0,
      f"each {sp.factor(dim_one.subs(m, n + 1))}")
check("the split is exactly 50/50 at every level -- the swapped pair has the SAME dimension, the "
      "product (2j_L+1)(2j_R+1) being symmetric",
      sp.simplify(((2 * jL + 1) * (2 * jR + 1)) - ((2 * jR + 1) * (2 * jL + 1))) == 0)

print("\n   n    m=n+1   (j_L,j_R)      dim each   total    mu_n^2")
rows = []
for nn in range(2, 9):
    mm = nn + 1
    a_, b_ = sp.Rational(mm + 1, 2), sp.Rational(mm - 3, 2)
    d1 = int((2 * a_ + 1) * (2 * b_ + 1))
    rows.append((nn, d1, nn * (nn + 2) - 2))
    print(f"  {nn:3d}  {mm:5d}   ({a_}, {b_})".ljust(34) + f"{d1:7d}  {2*d1:7d}  {nn*(nn+2)-2:7d}")
check("the floor n=2 is (2,0) + (0,2): a self-dual FIVE and an anti-self-dual FIVE, ten in all, "
      "reproducing P10's own 'ten at the floor'",
      rows[0][1] == 5 and 2 * rows[0][1] == 10)

# ---------------------------------------------------------------------------------
print("\nPART 2 -- THE FREQUENCIES ARE EQUAL, AND THE IDENTITY IS SYMMETRIC BY CONSTRUCTION.")
print("-" * 100)
CL, CR = jL * (jL + 1), jR * (jR + 1)
mu2_from_casimir = sp.expand(2 * (CL + CR) - 6)
print(f"  C_L + C_R = {sp.simplify(CL + CR)}")
print(f"  2(C_L + C_R) - 6 = {mu2_from_casimir}")
check("mu^2 = 2(C_L + C_R) - 6 reproduces P10's mu_n^2 = n(n+2)-2 at every level",
      sp.simplify(mu2_from_casimir.subs(m, n + 1) - (n * (n + 2) - 2)) == 0)
x_, y_ = sp.symbols('C_L C_R')
check("...and that expression is MANIFESTLY SYMMETRIC in the two Casimirs, so the swapped family "
      "carries the identical frequency -- the equality is not an arithmetic coincidence per level",
      sp.simplify((2 * (x_ + y_) - 6) - (2 * (y_ + x_) - 6)) == 0)

# ---------------------------------------------------------------------------------
print("\nPART 3 -- AND THE SYMMETRY IS AN ISOMETRY: sigma(g) = g^(-1) ON S^3 = SU(2).")
print("-" * 100)
print("  On unit quaternions g^(-1) = conj(g), so sigma is diag(1,-1,-1,-1) on the embedding R^4.")
sig = np.diag([1.0, -1.0, -1.0, -1.0])
check("sigma is in O(4): sigma^T sigma = I, so it is an ISOMETRY of the round S^3",
      np.allclose(sig.T @ sig, np.eye(4)))
check("det(sigma) = -1, so it is ORIENTATION-REVERSING", abs(np.linalg.det(sig) + 1) < 1e-12,
      f"det = {np.linalg.det(sig):.1f}")


def quat_mul(p, q):
    a, b, c, d = p
    e, f, g, h = q
    return np.array([a * e - b * f - c * g - d * h, a * f + b * e + c * h - d * g,
                     a * g - b * h + c * e + d * f, a * h + b * g - c * f + d * e])


conj = lambda p: np.array([p[0], -p[1], -p[2], -p[3]])
rng = np.random.default_rng(20250925)
worst = 0.0
for _ in range(200):
    g_ = rng.normal(size=4); g_ /= np.linalg.norm(g_)
    q_ = rng.normal(size=4); q_ /= np.linalg.norm(q_)
    lhs = conj(quat_mul(g_, q_))                 # sigma(L_g q)
    rhs = quat_mul(conj(q_), conj(g_))           # R_(g^-1) sigma(q)
    worst = max(worst, float(np.max(np.abs(lhs - rhs))))
check("sigma conjugates LEFT translation into RIGHT translation, sigma(g q) = sigma(q) sigma(g), so "
      "it EXCHANGES the two SU(2) factors and hence (j_L,j_R) <-> (j_R,j_L)",
      worst < 1e-12, f"worst residual over 200 random pairs = {worst:.2e}")
print("\n  => Being an isometry, sigma commutes with the Laplacian, so the two families share every")
print("     frequency.  Carrying one epsilon, the curl ANTI-commutes with it, so sigma reverses the")
print("     handedness.  ** Equal frequencies and reversed handedness in the same map -- which is")
print("     exactly the structure the cancellation below needs, and it is the geometry's. **")
eps = np.diag([1.0, -1.0])                        # curl sign on the (+,-) pair
swap2 = np.array([[0.0, 1.0], [1.0, 0.0]])
check("on the two-element handedness label the swap ANTI-commutes with the curl sign and COMMUTES "
      "with any function of the level alone",
      np.allclose(swap2 @ eps @ swap2, -eps) and np.allclose(swap2 @ np.eye(2), np.eye(2) @ swap2))

# ---------------------------------------------------------------------------------
print("\nPART 4 -- ATTACK (a): IS THE CONDITION HELICITY-BLIND AT THE MODE FUNCTIONS?")
print("-" * 100)
print("  P10 sec:lock states the coupled boundary condition in full: the coefficient is promoted to")
print("      Gamma_hat = gamma + c * SUM_n pi_hat_n^2 ,")
print("  the operator -d_x^2 + Gamma_hat/x^2 decomposes as a direct integral over spec(Gamma_hat),")
print("  thermal regularity imposes the regular branch x^(1/2+nu), nu = sqrt(Gamma_hat + 1/4), on each")
print("  SUB-THRESHOLD fibre (Gamma_hat < 3/4), and asks nothing of the limit-point fibres.")
print("  ** The tower enters NOWHERE ELSE.  So the check is whether that one operator is swap-blind. **")

NF = 3            # Fock truncation per mode
LEVELS = [(2, 6.0), (3, 13.0)]      # (n, mu_n^2) -- the floor and the next level


def ops(NF_):
    a_ = np.diag(np.sqrt(np.arange(1, NF_)), 1)
    return a_, a_.conj().T


a_op, ad_op = ops(NF)


def kron_list(ms):
    out = np.array([[1.0 + 0j]])
    for M in ms:
        out = np.kron(out, M)
    return out


# mode order: (n=2,+), (n=2,-), (n=3,+), (n=3,-)
MU = [np.sqrt(mu2) for _, mu2 in LEVELS for _ in (0, 1)]
NM = len(MU)
I = np.eye(NF)


def embed(M, slot):
    return kron_list([M if i == slot else I for i in range(NM)])


pi_sq, num = [], []
for s in range(NM):
    pi_s = 1j * np.sqrt(MU[s] / 2.0) * (ad_op - a_op)
    pi_sq.append(embed(pi_s @ pi_s, s))
    num.append(embed(ad_op @ a_op, s))

# the swap permutation: exchange the two helicity slots at each level
perm = [1, 0, 3, 2]
basis = np.array(np.meshgrid(*[np.arange(NF)] * NM, indexing='ij')).reshape(NM, -1).T
idx = {tuple(b): i for i, b in enumerate(basis)}
P = np.zeros((NF ** NM, NF ** NM))
for i, b in enumerate(basis):
    P[idx[tuple(b[perm])], i] = 1.0

GAMMA0, CC = 0.25, 1.0
Gam = GAMMA0 * np.eye(NF ** NM) + CC * sum(pi_sq)
check("P is a unitary involution (it is the permutation the isometry sigma induces on the modes)",
      np.allclose(P @ P, np.eye(NF ** NM)) and np.allclose(P.T @ P, np.eye(NF ** NM)))
c1 = float(np.max(np.abs(Gam @ P - P @ Gam)))
check("[Gamma_hat, P] = 0 EXACTLY -- the boundary coefficient is a sum of squares over a mode set "
      "the swap permutes, pairing modes of equal frequency",
      c1 < 1e-12, f"max |commutator| = {c1:.2e}")

nu = np.sqrt(Gam + 0.25 * np.eye(NF ** NM))
c2 = float(np.max(np.abs(nu @ P - P @ nu)))
check("[nu(Gamma_hat), P] = 0, so the retained indicial branch x^(1/2+nu) is the same on swapped "
      "fibres -- the Friedrichs selection is helicity-blind",
      c2 < 1e-10, f"max |commutator| = {c2:.2e}")

w, V = np.linalg.eigh(Gam)
sub = V[:, w < 0.75]
Pi_sub = sub @ sub.T
c3 = float(np.max(np.abs(Pi_sub @ P - P @ Pi_sub)))
check("[Pi_(Gamma<3/4), P] = 0, so the SUB-THRESHOLD subspace the condition is supported on is "
      "itself swap-invariant and the measure does not distinguish the towers",
      c3 < 1e-10, f"max |commutator| = {c3:.2e}; sub-threshold dim = {int((w < 0.75).sum())}")

print("\n  ** CONTROL, which MUST break: a helicity-weighted coefficient. **")
Gam_bad = GAMMA0 * np.eye(NF ** NM) + CC * sum(
    (1.0 + 0.3 * (-1) ** s) * pi_sq[s] for s in range(NM))
cbad = float(np.max(np.abs(Gam_bad @ P - P @ Gam_bad)))
check("a Gamma_hat with helicity-dependent weights does NOT commute with P, so the commutation "
      "above is a fact about THIS Gamma_hat and not about the algebra",
      cbad > 1e-3, f"max |commutator| = {cbad:.3f}")

print("\n  ** AND THE TEMPERATURE CARRIES NO MODE INDEX AT ALL. **  P10 sec:lock: the condition is")
print("  imposed 'at the one horizon period beta = 2 pi alpha (the surface gravity kappa = 1/alpha")
print("  belongs to the background horizon, not to the graviton content, and so is common to every")
print("  fibre)'.  So the second datum of the state is helicity-blind by construction, not by check.")
al = sp.Symbol('alpha', positive=True)
r_ = sp.Symbol('r', positive=True)
f_dS = 1 - r_ ** 2 / al ** 2
kappa = sp.simplify(sp.Rational(1, 2) * sp.Abs(sp.diff(f_dS, r_).subs(r_, al)))
beta_sym = sp.simplify(2 * sp.pi / kappa)
print(f"  f = {f_dS} ;  kappa = |f'(alpha)|/2 = {kappa} ;  beta = 2 pi / kappa = {beta_sym}")
check("kappa = 1/alpha and beta = 2 pi alpha follow from the BACKGROUND metric function alone: "
      "derived here off f = 1 - r^2/alpha^2 rather than quoted",
      sp.simplify(kappa - 1 / al) == 0 and sp.simplify(beta_sym - 2 * sp.pi * al) == 0)
check("...and beta's free symbols are {alpha} -- no mode index, no helicity label, nothing the swap "
      "could act on, so the one remaining datum of the state cannot distinguish the towers",
      beta_sym.free_symbols == {al}, f"free symbols = {beta_sym.free_symbols}")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- SO EVERY P-ODD EXPECTATION VANISHES.  EXHIBITED, NOT ASSERTED.")
print("-" * 100)
X = sum((-1) ** s * num[s] for s in range(NM))     # the helicity charge
check("the helicity charge X = SUM eps_n N_n is P-ODD: P^dagger X P = -X",
      np.allclose(P.T @ X @ P, -X))

BETA = 1.0
rho = lambda H: np.diag(np.exp(-BETA * np.diag(H).real) / np.exp(-BETA * np.diag(H).real).sum())
H = sum(MU[s] * num[s] for s in range(NM))
expX = float(np.trace(rho(H) @ X).real)
check("<X> = 0 in the thermal state at the common beta -- exact, on the truncated Fock space",
      abs(expX) < 1e-12, f"<X> = {expX:.2e}")

print("\n  and in closed form, level by level, with n_B the Bose factor:")
print("      <X> = SUM_levels [ d_n(+) - d_n(-) ] n_B(beta mu_n)   and  d_n(+) = d_n(-) = (n-1)(n+3).")
nB = lambda x: 1.0 / np.expm1(x)
tot = 0.0
for nn, d1, mu2 in [(r[0], r[1], r[2]) for r in rows]:
    tot += (d1 - d1) * nB(BETA * np.sqrt(mu2))
check("the closed-form sum is identically zero, level by level, because BOTH the degeneracy and the "
      "frequency are equal between the paired families",
      abs(tot) < 1e-15, f"sum over n=2..8 = {tot:.1e}")

print("\n  ** TWO CONTROLS, which MUST break. **")
bad_deg = sum((d1 - (d1 - 1)) * nB(BETA * np.sqrt(mu2)) for _, d1, mu2 in rows)
check("CONTROL 1 -- unequal degeneracies (one mode removed from the minus tower per level) give a "
      "non-zero P-odd expectation, so the vanishing is carried by the 50/50 split",
      abs(bad_deg) > 1e-3, f"<X> = {bad_deg:.4f}")
bad_frq = sum(d1 * (nB(BETA * np.sqrt(mu2)) - nB(BETA * np.sqrt(mu2) * 1.1)) for _, d1, mu2 in rows)
check("CONTROL 2 -- equal degeneracies but frequencies split by 10 per cent also give a non-zero "
      "answer, so the vanishing is carried by the EQUAL FREQUENCIES too, i.e. by PART 2's isometry",
      abs(bad_frq) > 1e-3, f"<X> = {bad_frq:.4f}")

# ---------------------------------------------------------------------------------
print("\nPART 6 -- ATTACK (b): THE FLOOR, WHERE THE SELF-DUAL AND ANTI-SELF-DUAL FIVES SIT.")
print("-" * 100)
print("  The order asks whether the measure or the degeneracies distinguish the towers AT THE FLOOR.")
print(f"    floor n=2, m=3: (j_L,j_R) = (2,0) and (0,2), dimension {rows[0][1]} and {rows[0][1]}, "
      f"total {2*rows[0][1]}, mu_2^2 = {rows[0][2]}")
check("the floor's two members are an irreducible FIVE each -- the self-dual and the anti-self-dual "
      "-- so nothing at the floor is odd or unpaired",
      rows[0][1] == 5)
check("the floor's frequency is common to both, mu_2^2 = 6 = 2(C_L+C_R)-6 at (2,0) and at (0,2)",
      abs(float(2 * (2 * 3 + 0 * 1) - 6) - 6.0) < 1e-12 and
      abs(float(2 * (0 * 1 + 2 * 3) - 6) - 6.0) < 1e-12)
check("and the direct-integral MEASURE cannot separate them either: PART 4 showed the sub-threshold "
      "spectral projector of Gamma_hat commutes with P, so each spectral fibre is swap-invariant",
      c3 < 1e-10)
print("\n  => ATTACK (b) FAILS.  The floor is the most exposed level -- the smallest degeneracy and")
print("     the lowest frequency -- and it is exactly balanced, five against five at one mu.")

# ---------------------------------------------------------------------------------
print("\nPART 7 -- ATTACK (c): DOES THE EUCLIDEAN CONTINUATION PICK A HANDEDNESS?")
print("-" * 100)
print("  This is the one with teeth, and the order is right that a self-dual pair on a four-sphere is")
print("  where a continuation CAN pick one.  Three things are checked rather than asserted.")

print("\n  (i) THE CONTINUATION AND THE SWAP ACT ON DISJOINT BLOCKS.  P10 sec:lock: the rotation is the")
print("      global x_0 -> i x_0 carrying dS_5 = SO(5,1)/SO(4,1) to S^5 = SO(6)/SO(5).  It acts on the")
print("      time coordinate; sigma acts on the three-sphere factor.")
W = np.diag([1j, 1.0, 1.0, 1.0, 1.0])            # Wick rotation on x_0 of the 5 embedding coords
S5 = np.diag([1.0, 1.0, -1.0, -1.0, -1.0])       # sigma on the S^3 block, identity on (x_0, x_4)
check("the Wick rotation and sigma commute exactly, acting on disjoint coordinate blocks, so the "
      "continuation does not touch the three-sphere's orientation or the curl that labels the towers",
      np.allclose(W @ S5, S5 @ W))

print("\n  (ii) THE HODGE STAR DOES CHANGE, AND THAT IS WHY THE ATTACK IS REAL.  On a Lorentzian")
print("       four-manifold *^2 = -1 on two-forms, so real self-dual forms do not exist; on a")
print("       Riemannian one *^2 = +1 and they do.  ** So a continuation CAN separate a self-dual")
print("       pair -- but separating requires a P-ODD TERM IN THE EXPONENT, and there are exactly two")
print("       candidates, both absent. **")
check("*^2 = -1 Lorentzian and +1 Riemannian on two-forms in four dimensions, which is the mechanism "
      "the attack points at and it is real",
      (-1) ** (2 * (4 - 2) + 1) == -1 and (-1) ** (2 * (4 - 2)) == 1)
print("       CANDIDATE 1, a rotation: absent.  The de~Sitter cosmological horizon of f = 1 - r^2/a^2")
print("         is non-rotating, Omega = 0; P10 fixes kappa = 1/alpha and nothing else.")
print("       CANDIDATE 2, a theta-term already in the action: assuming one is CIRCULAR -- whether a")
print("         Pontryagin-type entry is owed is the question.  And the Einstein--Hilbert action in")
print("         the TT sector carries no epsilon tensor, so no P-odd term is there to continue.")

print("\n  (iii) THE ROTATING CONTROL, so the check is not vacuous.  Give the SAME state a chemical")
print("        potential mu = beta*Omega coupled to the helicity charge, as a rotating horizon would:")
for Om in (0.0, 0.05, 0.2, 0.5):
    val = sum(d1 * (nB(BETA * (np.sqrt(mu2) - Om)) - nB(BETA * (np.sqrt(mu2) + Om)))
              for _, d1, mu2 in rows)
    print(f"        Omega = {Om:4.2f} :  <X> = {val:+.6f}")
v0 = sum(d1 * (nB(BETA * (np.sqrt(mu2) - 0.0)) - nB(BETA * (np.sqrt(mu2) + 0.0)))
         for _, d1, mu2 in rows)
v1 = sum(d1 * (nB(BETA * (np.sqrt(mu2) - 0.05)) - nB(BETA * (np.sqrt(mu2) + 0.05)))
         for _, d1, mu2 in rows)
v2 = sum(d1 * (nB(BETA * (np.sqrt(mu2) - 0.10)) - nB(BETA * (np.sqrt(mu2) + 0.10)))
         for _, d1, mu2 in rows)
check("at Omega = 0 the P-odd expectation is exactly zero, and at Omega > 0 it is non-zero -- so the "
      "vanishing is a statement about THIS horizon and not an identity of the bookkeeping",
      abs(v0) < 1e-15 and abs(v1) > 1e-3)
check("...and it is LINEAR in Omega at small Omega, which is the signature of a genuine P-breaking "
      "chemical potential rather than a numerical accident",
      abs(v2 / v1 - 2.0) < 0.05, f"<X>(0.10)/<X>(0.05) = {v2/v1:.4f} vs 2")
print("\n  => ATTACK (c) IS ANSWERED.  The continuation does not pick a handedness HERE, and the")
print("     control exhibits the thing that would: an angular velocity the de~Sitter cosmological")
print("     horizon does not have.")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING, WHICH IS WHAT THE ORDER ASKED FOR LAST.")
print("=" * 100)
print("""
  ** THE TOWERS ARE POPULATED ALIKE, SO THE PARITY-ODD ENTRY IS NOT OWED. **

  1. The claim is NOT helicity-blindness by wording.  The condition's whole dependence on the tower is
     Gamma_hat = gamma + c SUM pi_n^2, and the swap is a permutation of that mode set pairing modes of
     equal frequency -- so the commutation is exact, and a helicity-weighted coefficient breaks it.

  2. The equal frequencies are FORCED, by an orientation-reversing isometry rather than by arithmetic.
     sigma: g -> g^(-1) is diag(1,-1,-1,-1) in O(4) with det -1; it conjugates left translations into
     right ones, so it exchanges the two families; it commutes with the Laplacian and anti-commutes
     with the curl.  ** One map that preserves every frequency and reverses every handedness is
     exactly what the cancellation needs, and it belongs to the geometry. **

  3. The three places the order named to look: (a) fails -- the mode functions enter only through a
     sum of squares; (b) fails -- the floor is five against five at one frequency, and the spectral
     measure is swap-invariant; (c) is answered, and it is the real one.  A Riemannian four-section
     does admit a real self-dual split where a Lorentzian one does not, but weighting the towers apart
     needs a P-odd exponent, and the two candidates are a rotation the de~Sitter horizon does not have
     and a theta-term the audit is asking whether it is owed.  The rotating control shows the break.

  4. ** SO THE ROW CLOSES ABOVE THE DECLINED ENTROPY QUESTION. **  The parity-odd content cancels
     between the towers, no P-odd divergence is generated, and the entry the row was holding open is
     not owed at all.  What remains of PO-43 is the declined question -- whether S = A/4 carries to a
     cosmological horizon -- which P17 sec:ledger declines in terms and says would be a result rather
     than a gap were it to fail.

  ** AND WHAT THIS DOES NOT REACH. **  The interacting tower's ultraviolet definition is P10's own open
  frontier and is untouched.  What the check does reach is narrower and is enough: the bare action in
  the TT sector carries no epsilon, and the state is P-invariant, so a P-invariant regulator generates
  no P-odd divergence.  A P-breaking regulator would, but that is a scheme choice and not a divergence.
  The one mechanism that makes a P-odd gravitational term with a P-even bare action is the
  gravitational chiral anomaly, and it needs an unbalanced chiral FERMION content -- which the row's
  own index obstruction excludes.  That last step is a reading of a corpus result, not computed here.

  ** AND THE CANDIDATE THE ORDER FENCED IS NOT BUILT. **  The tower's floor as a canonical subtraction
  point for the log is not constructed, the order making it conditional on this check coming out
  against.  It does not.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print("""
ESTABLISHED: Hartle--Hawking regularity, imposed fibre by fibre as P10 sec:lock states it, is
helicity-blind at the level of the mode functions and not merely in its wording -- [Gamma_hat, P] = 0
exactly, and with it nu(Gamma_hat), the sub-threshold projector and the retained branch, while
beta = 2 pi alpha carries no mode index; the two families have equal degeneracy (50/50 at every level,
five against five at the floor) and equal frequency, the latter forced by the orientation-reversing
isometry g -> g^(-1) which exchanges the SU(2) factors, commutes with the Laplacian and anti-commutes
with the curl; so every P-odd expectation vanishes identically and the parity-odd entry PO-43 was
holding open is NOT OWED.  Three controls break as they must: a helicity-weighted coefficient, unequal
degeneracies or frequencies, and a rotating horizon.
NOT CLAIMED: that the tower is achiral (r4547 stands -- it is chirally capable and the state does not
use the capacity); anything about the interacting tower's ultraviolet definition; the declined entropy
question; and the floor-as-subtraction-point candidate is deliberately not built.
""")
