"""JINT — the normalization integral of the LambdaCDM growth factor, read geometrically,
and the family it belongs to.  (Janzen 2025, Res. Notes AAS 9 350, doi:10.3847/2515-5172/ae2fdf.)

THE INTEGRAL.  J(Om) = int_0^inf dz (1+z)/[Om(1+z)^3+1-Om]^{3/2} is the factor that normalises the
linear growth factor to D_1(0)=1.  Janzen (2025) notes J(Om*)=1 at Om* = 0.315162, and that dropping
the factor biases growth-based inference toward Om*, while leaving purely geometric probes untouched.

*** 1.  WHAT IT IS GEOMETRICALLY. ***  Substituting (1+z)=1/a, dz = da/a^2:
        J = int_0^1 da / (a E)^3 = int_0^1 da [ H_0/(aH) ]^3 ,
i.e. THE CUBE OF THE COMOVING HUBBLE RADIUS, INTEGRATED OVER THE SCALE FACTOR, in Hubble-length
units.  J = 1 says that accumulates to exactly one Hubble volume.  (Identity verified numerically.)

*** 2.  WHY IT CAN APPEAR ELSEWHERE. ***  The growth equation D'' + 2HD' - (3/2)Om H0^2 a^-3 D = 0 has
H(a) as its DECAYING solution, so the growing one is D+ ~ H int da/(aH)^3 by reduction of order.  Any
second-order equation with 2H friction inherits the same integral -- it is not specific to growth.

*** 3.  IN CR: THE COMOVING HUBBLE RADIUS PEAKS AT THE NARIAI RADIUS, EXACTLY. ***  With
H = (c/alpha) sqrt(1+2/x^3) and x = x0 a,
        R_H = c/(aH) = alpha x0 sqrt( x/(x^3+2) ),
        d/dx[x/(x^3+2)] = 0  =>  (x^3+2) - 3x^3 = 0  =>  x^3 = 1  =>  x = 1 ,
with NO dependence on x0 or alpha.  x=1 IS the Nariai radius, and R_H there is alpha x0/sqrt3, so the
PHYSICAL Hubble radius at that moment is exactly alpha/sqrt3 = r_N.

*** 4.  THE FAMILY.  I_n(Om) = int_0^1 da [H_0/(aH)]^n .  I_1 = H_0 t_0 (the dimensionless age);
    I_3 = J.  Solving I_n = 1: ***
        n=1  Om=0.262875  x0=1.7767
        n=2  Om=0.292494  x0=1.6913
        n=3  Om=0.315162  x0=1.6319   <- J (Janzen 2025);  0.70 sigma from DESI's x0
        n=4  Om=0.333333  x0=1.5874   <- EXACTLY 1/3, i.e. x0^3 = 4;  1.66 sigma
        n=5  Om=0.348380  x0=1.5524
*** I_4 = 1 at Om = 1/3 is EXACT, in two lines: *** with Om=1/3, (aE)^4 = (1/9a^2)(1+2a^3)^2, so the
integrand is 9a^2/(1+2a^3)^2; with u = 1+2a^3 it is (3/2) int_1^3 du/u^2 = (3/2)(1-1/3) = 1.

*** 5.  AND THE HONEST TEMPERING. ***  The family SWEEPS Om from 0.263 to 0.348 across n=1..5, so it
STRADDLES the observed value rather than singling it out.  J=1 is the member closest to Planck; I_4=1
is the member with a closed form.  Neither fact makes the other one evidence.
"""
import numpy as np, sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
E=lambda a,Om: np.sqrt(Om/a**3+(1-Om))
Jz=lambda Om: quad(lambda z:(1+z)/(Om*(1+z)**3+1-Om)**1.5,0,np.inf,limit=300)[0]
I =lambda n,Om: quad(lambda a: 1.0/(a*E(a,Om))**n,1e-12,1.0,limit=400)[0]
x_of=lambda Om:(2*(1-Om)/Om)**(1./3)

print("  1. IDENTITY  J(z-form) == int_0^1 da [H0/(aH)]^3")
for Om in (0.25,0.3024,0.3152,0.40):
    assert abs(Jz(Om)-I(3,Om))<1e-8
    print("       Om=%.4f   %.6f  ==  %.6f"%(Om,Jz(Om),I(3,Om)))
print()
r=minimize_scalar(lambda x:-x/(x**3+2),bounds=(0.05,6),method='bounded')
print("  3. comoving Hubble radius maximal at x = %.6f  (Nariai, x=1 EXACTLY, parameter-free)"%r.x)
assert abs(r.x-1.0)<1e-4
print("     R_H/(alpha x0) there = %.6f = 1/sqrt3"%np.sqrt(1/3.))
print()
print("  4. I_n = 1:")
for n in (1,2,3,4,5):
    Om=brentq(lambda O: I(n,O)-1.0,0.02,0.97)
    print("       n=%d  Om=%.6f  x0=%.4f"%(n,Om,x_of(Om)))
    if n==4: assert abs(Om-1/3.)<1e-6, "I_4=1 must be exactly Om=1/3"
a=sp.symbols('a',positive=True)
val=sp.integrate(sp.simplify(1/(a*sp.sqrt(sp.Rational(1,3)/a**3+sp.Rational(2,3)))**4),(a,0,1))
print("     symbolic I_4(1/3) = %s  (exact)"%sp.simplify(val))
assert sp.simplify(val)==1
print()
print("  5. DESI DR2: x0 = 1.6648 +- 0.0467  ->  J=1 at %.2f sigma; x0^3=4 at %.2f sigma"
      %(abs(1.6319-1.6648)/0.0467, abs(4**(1/3.)-1.6648)/0.0467))
