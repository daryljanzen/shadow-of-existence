import sympy as sp
# FORCE-vs-ADMIT bite 2: is the physical period (the graviton mode action of the lock, P8 sec:lock)
# a SYMMETRIC/monodromy-invariant function (-> ADMIT) or does it depend on the INDIVIDUAL monodromic
# horizon root (-> candidate FORCE)?  Allowed to return ADMIT.
M, alpha, T, n = sp.symbols('M alpha T n', positive=True)
r = sp.symbols('r')

# the monodromic object: the horizon cubic's roots r_i(M) (M = modulus, monodromy around Nariai M_N)
cubic = r**3 - alpha**2*r + 2*M*alpha**2
print("monodromic data = roots of the horizon cubic:", cubic, "= 0  (S_3 deck, branched at Nariai in M)")
print("  -> roots r_i depend on M; encircling M_N permutes them (bite 1).")

# the physical period data (P8 sec:lock, read at source):
mu2 = n*(n+2) - 2                      # S^3 TT-Laplacian eigenvalue
a   = alpha*sp.cosh(T/alpha)           # layer radius (reassigned pure-Lambda dS background)
# mode action integrand (the oint p dq data): S_n = 1/2 int a^3 (phidot^2 - mu^2/a^2 phi^2)
print("\nphysical period data (graviton mode action S_n):")
print("  mu_n^2 =", mu2, "   (depends on harmonic index n only)")
print("  a(T)   =", a,   "   (depends on the scale alpha only -- the round-S^3 radius)")

# THE TEST: does the period data depend on the modulus M (the monodromic variable)?
dmu_dM = sp.diff(mu2, M); da_dM = sp.diff(a, M)
print("\n  d(mu_n^2)/dM =", dmu_dM, "   d(a)/dM =", da_dM)
print("  -> the period data is INDEPENDENT of M: it is a function of (alpha, n) only.")
print("     alpha = sqrt(3/Lambda) is the single SYMMETRIC scale (a coefficient of the cubic, S_3-invariant);")
print("     n is the harmonic index. Neither is an individual monodromic root.")

# where the ONLY M-dependence in the lock object lives (P8 l.177): the projected matter term
print("\nthe only M-dependence in the whole lock object (P8 l.177):")
print("  the observer-attributed matter density  2M/a^3  -- present ONLY in the representational")
print("  flat-LambdaCDM projection, ABSENT from the ontological pure-Lambda background the tower lives on.")

print("""
VERDICT (bite 2) -- ADMIT, not FORCE; bounded; do-not-assert on unexamined routes.
- The physical period (graviton action, the oint p dq the quantization conditions) is monodromy-INVARIANT:
  a function of the symmetric scale alpha and the index n, with ZERO dependence on the individual,
  monodromic horizon root. The S_3 cover's monodromy therefore obstructs nothing on the physical phase
  space -- there is no multi-valued period, hence no forced integrality condition.
- The monodromy lives ENTIRELY in the representational/vantage layer (which-horizon, the projected matter
  2M/a^3) -- exactly 'the vantage is gauge by the axioms' (THE_VISION s4). Gauge carries no FORCE.
- The tower's discreteness is a COMPACTNESS effect of the closed S^3 (P8: 'the closed topology enters as
  the discreteness'), not a monodromy-forced quantization. The geometry ADMITS the quantization cleanly;
  the discrete skeleton does NOT force it.
- Bounded: this closes the discrete-skeleton/cover-monodromy FORCE route. Do-not-assert on any unexamined
  route (e.g. the background-sector half-line self-adjoint extension -- a separate, choice-flavored question,
  itself ADMIT-leaning). The universal 'nothing forces quantum structure' stays do-not-assert both ways.
""")
