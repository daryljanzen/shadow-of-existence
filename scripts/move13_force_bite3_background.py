import sympy as sp
# FORCE-vs-ADMIT bite 3 (the held-open route): the background scale-factor sector.
# H_phys = (2pi/3) p_a^2/a - (Lambda/8pi) a^3  on L^2(half-line, a>0). P8 sec:deparam.
# Does its half-line self-adjoint extension FORCE quantum structure, or is it a CHOICE (ADMIT)?
a, x, c, Lam, E = sp.symbols('a x c Lambda E', positive=True)

# Liouville transform: kinetic -(c/a) d^2/da^2  ->  -d^2/dx^2.  Need (da/dx)^2 (c/a) = 1.
# => da/dx = sqrt(a/c) => x = 2 sqrt(c) sqrt(a) => a = x^2/(4c).
a_of_x = x**2/(4*c)
print("Liouville map a(x) =", a_of_x, "  (x = 2 sqrt(c a), c = 2pi/3)")
# the potential V = -(Lambda/8pi) a^3 in the x-variable:
V = -(Lam/(8*sp.pi)) * a_of_x**3
print("V(x) = -(Lambda/8pi) a^3 =", sp.simplify(V), "   ->  V ~ -x^6 at large x")

print("""
LIMIT-POINT / LIMIT-CIRCLE classification (Weyl) of  -d^2/dx^2 + V(x),  x in (0, infinity):

[endpoint x -> infinity]  V ~ -x^6  (beta = 6 > 2).
  WKB: p(x) ~ sqrt(E + x^6) ~ x^3 ; both solutions ~ p^{-1/2} exp(+- i int p) ~ x^{-3/2} oscillatory.
  |psi|^2 ~ x^{-3}, and int^infty x^{-3} dx CONVERGES => BOTH solutions are L^2 near infinity
  => LIMIT CIRCLE at infinity => a boundary condition at large scale factor is REQUIRED.

[endpoint x -> 0]  V -> 0 (regular finite endpoint); -psi'' = E psi has sin, cos -> both L^2 near 0
  => LIMIT CIRCLE at 0 => a boundary condition at the origin is REQUIRED.

=> deficiency indices (2,2): a U(2) (four-parameter) FAMILY of self-adjoint extensions.
""")
print("VERDICT (bite 3) -- ADMIT, not FORCE; the strongest ADMIT of the three routes.")
print("""
- A consistent unitary quantization EXISTS (self-adjoint extensions exist: equal deficiency indices).
  Sufficiency holds -- ADMIT confirmed.
- It is NOT unique: a U(2) family of boundary-condition CHOICES. Non-uniqueness is the antithesis of
  forcing -- the classical theory does not pick one; physical input (a choice) does.
- FORCE's only prerequisite -- a classical INCOMPLETENESS that quantization must resolve -- is ABSENT:
  CR cosmology is non-singular (P8 sec:deparam, sourced to BH_causality + CRcosmology); the classical
  layer is complete, so no boundary condition is forced 'for consistency.' Any discreteness a chosen BC
  induces is choice-dependent, hence not a forced quantization of the dust energy rho_d.
- Same root as the whole programme: the geometry is complete on its own, so it ADMITS quantum structure
  (uniquely on the propagating tower, as a U(2)-choice on the background) but FORCES none.
- Bound held: this closes the background-sector route too. The universal 'nothing forces quantum structure'
  stays do-not-assert (an unexamined CR-native route could still exist); but both concrete candidate
  routes -- discrete skeleton (r326) and background sector (here) -- return ADMIT, one root.
""")
