"""P3 rem:dimension -- THE SINGLE-HARMONIC FORM EXISTS EXACTLY IN FOUR AND FIVE DIMENSIONS, AND THE PROOF IS A
COEFFICIENT FORMULA, NOT A COUNT.

In D-dimensional Schwarzschild--de Sitter (gauge alpha = 1) the mass at a root is 2M = r0^(D-3) - r0^(D-1).
With r0 = rho sin w, the harmonic (D-1-2j)w (j >= 1) receives a contribution from both powers, with the same
sign, and its coefficient vanishes exactly when

        rho^2 = 4 j (D-1-j) / ((D-1)(D-2)).

The right-hand side increases strictly in j for j < (D-1)/2, so one scale clears all the lower NON-CONSTANT
harmonics only when there is exactly one, j = 1: that is D = 4 and D = 5, at rho^2 = 4/(D-1).  For D >= 6 the
conditions at j = 1 and j = 2 ask for different scales (equal only at D = 4).  At D = 4 the result has zero
mean, 2M = (2/(3 sqrt3)) sin 3w; at D = 5 it carries a constant, 2M = (1 - cos 4w)/8.
This receipt checks the formula against a direct harmonic expansion for D = 4..14, and the verdict at each D.
"""
import sympy as sp
w=sp.symbols('w',real=True); rho=sp.symbols('rho',positive=True); z=sp.symbols('z')
def harmonics(D):
    # exact: sin w = (z - 1/z)/(2i), z = e^{iw}; the coefficient of z^m + its conjugate gives harmonic m
    s_=(z-1/z)/(2*sp.I)
    P=sp.expand((rho*s_)**(D-3)-(rho*s_)**(D-1))
    c={}
    for m in range(0,D):
        cp=sp.expand(sp.Poly(sp.expand(P*z**(D-1)),z).coeff_monomial(z**(m+D-1)))
        c[m]=sp.simplify(cp)          # amplitude of e^{imw}; nonzero iff harmonic m present
    return c
verdict={}
for D in range(4,15):
    n=D-1
    expr=(rho*sp.sin(w))**(D-3)-(rho*sp.sin(w))**(D-1)
    c=harmonics(D)
    lower=[n-2*j for j in range(1,(n+1)//2) if n-2*j>=1]       # non-constant lower modes
    sols=None
    for j in range(1,(n+1)//2):
        m=n-2*j
        if m<1: continue
        coeff=c[m]
        roots=[x for x in sp.solve(sp.Eq(coeff,0),rho) if x.is_positive]
        r2={sp.nsimplify(x**2) for x in roots}
        assert r2=={sp.Rational(4*j*(n-j),n*(n-1))}, (D,j,r2)        # the coefficient formula
        sols=r2 if sols is None else sols & r2
    ok=bool(sols)
    verdict[D]=ok
    assert ok==(D in (4,5)), (D,sols)
    if ok:
        (r2,)=sols; assert r2==sp.Rational(4,n)
        val=sp.simplify(expr.subs(rho,sp.sqrt(r2)))
        if D==4: assert sp.simplify(val-2/(3*sp.sqrt(3))*sp.sin(3*w))==0
        if D==5: assert sp.simplify(val-(1-sp.cos(4*w))/8)==0
    print(f"D={D:2d}: lower non-constant harmonics {lower}; one scale clears them: {ok}")
print("formula rho^2 = 4j(D-1-j)/((D-1)(D-2)) confirmed for every lower harmonic, D = 4..14")
print("ALL PASS")
