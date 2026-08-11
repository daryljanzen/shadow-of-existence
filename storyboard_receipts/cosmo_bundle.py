"""The cosmological bundle on the negative-imaginary branch, and the EXACT 2:1 of the seam points.
Bead: r^3 = 2M a^2 sinh^2(w), w = 3 tau~/2a, A=(2M a^2)^{1/3}. sinh(w) = (r/A)^{3/2}.
Cosmological bundle = arg r = +pi branch (NEGATIVE Im tau~):
  collapse run : |sinh|=u>1 -> Im tau~ = -pi/3 (fixed), Re tau~ = -(2/3)arccosh(u)
  the LAP lift : u<=1       -> Re tau~ = 0,              Im tau~ = -(2/3)arcsin(u): -pi/3 -> 0
  matter univ. : r>0        -> Im tau~ = 0,              Re tau~ = +(2/3)arcsinh((r/A)^{3/2})
=> collapse (run + lift) and cosmology (single real curve) are STRUCTURALLY DIFFERENT curves.
The lap is the LIFT -- unfurled here, not flattened to one X0."""
import numpy as np, sympy as sp
al=1.0; M2=2/(3*np.sqrt(3)); A=(M2*al**2)**(1/3)
def cosmo(r):
    if r>=0: return (2/3)*np.arcsinh((r/A)**1.5), 0.0
    u=abs(r/A)**1.5
    if u<=1: return 0.0, -(2/3)*np.arcsin(u)
    return -(2/3)*np.arccosh(u), -np.pi/3
# the boing roots / seam points land on clean sinh values
for lbl,r in [('r=-2a/sqrt3',-2/np.sqrt(3)),('r=0',0.0),('r=+a/sqrt3',1/np.sqrt(3))]:
    x,y=cosmo(r); u=abs(r/A)**1.5 if r else 0.0
    print(f"{lbl:12s}: |sinh|={u:.4f}  Re tau~={x:+.4f}  Im tau~={y/(np.pi/3):+.3f}*pi/3")
# THE 2:1, exactly:  Re tau~(-2a/sqrt3) = -(2/3)arccosh(2);  Re tau~(+a/sqrt3) = +(2/3)arcsinh(1/sqrt2)
a=sp.asinh(1/sp.sqrt(2)); b=sp.acosh(2)
assert abs(float(b-2*a))<1e-30      # arccosh(2) = 2 arcsinh(1/sqrt2)  EXACTLY
print("\narccosh(2) = 2*arcsinh(1/sqrt2) exactly:  2ln((1+sqrt3)/sqrt2) = ln((4+2sqrt3)/2) = ln(2+sqrt3)")
print("=> the two Nariai seam points sit at Re tau~ = -2d and +d  (d=(2/3)arcsinh(1/sqrt2)): the 2:1 (120/240),")
print("   here as a LENGTH RATIO along the unfurled time axis.")
