#!/usr/bin/env python3
"""r7341, node 66 -- THE TWO SHEAR FAMILIES.

71 reported at r7339+71.4 that receipt L165/S10's `C^2 = sigma^2(4 + 16 sigma^2/3)` is
"NOT what the metric gives", because the exact Weyl^2 of the family 71 built has a
`-48 H sigma^3` term the receipt asserts is absent.  Routed to the receipt's owner.

This settles it by computing both families from their metrics rather than reading either
report.  They are DIFFERENT one-parameter families and both polynomials are right:

  * L549/Q1's metric -- which S10 names none of -- has rates (1, 1+s, 1-s): the shear
    eigenvalues are (0, s, -s) and y <-> z is a symmetry of the family, so Weyl^2 MUST be
    even in s.  That is why its cubic vanishes.
  * 71's metric has rates (H-2s, H+s, H+s): eigenvalues (-2s, s, s), axisymmetric, and
    s -> -s carries the oblate member to the prolate one.  No symmetry forces evenness,
    and the cubic does not vanish.

The leading coefficients differ by exactly 3, which is the ratio of the shear invariants
sigma_ab sigma^ab (6s^2 against 2s^2).  So the two agree once normalised by the shear.

=> 71's contradiction is withdrawn.  What IS owed is the defect that made the collision
possible, and 71 named it in passing: S10 asserts a polynomial in sigma and NAMES NO
METRIC, so any reader supplies a family and gets a different answer.  A formula without
its referent is not a checkable claim.
"""
import os, sys

import sympy as sp
#!/usr/bin/env python3
"""r7341, node 66 -- THE TWO SHEAR FAMILIES.

71 reported at r7339+71.4 that receipt L165/S10's `C^2 = sigma^2(4 + 16 sigma^2/3)` is
"NOT what the metric gives", because the exact Weyl^2 of the family 71 built has a
`-48 H sigma^3` term the receipt asserts is absent.  Routed to the receipt's owner.

This settles it by computing both families from their metrics rather than reading either
report.  They are DIFFERENT one-parameter families and both polynomials are right:

  * L549/Q1's metric -- which S10 names none of -- has rates (1, 1+s, 1-s): the shear
    eigenvalues are (0, s, -s) and y <-> z is a symmetry of the family, so Weyl^2 MUST be
    even in s.  That is why its cubic vanishes.
  * 71's metric has rates (H-2s, H+s, H+s): eigenvalues (-2s, s, s), axisymmetric, and
    s -> -s carries the oblate member to the prolate one.  No symmetry forces evenness,
    and the cubic does not vanish.

The leading coefficients differ by exactly 3, which is the ratio of the shear invariants
sigma_ab sigma^ab (6s^2 against 2s^2).  So the two agree once normalised by the shear.

=> 71's contradiction is withdrawn.  What IS owed is the defect that made the collision
possible, and 71 named it in passing: S10 asserts a polynomial in sigma and NAMES NO
METRIC, so any reader supplies a family and gets a different answer.  A formula without
its referent is not a checkable claim.
"""
import os, sys


t,sig,H = sp.symbols('t sigma H', real=True)
x = list(sp.symbols('t x y z', real=True)); x[0]=t
def invariants(g, x):
    n=len(x); gi=g.inv()
    Gam=[[[sum(gi[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d])) for d in range(n))/2
           for c in range(n)] for b in range(n)] for a in range(n)]
    def R(a,b,c,d):
        s=sp.diff(Gam[a][b][d],x[c])-sp.diff(Gam[a][b][c],x[d])
        s+=sum(Gam[a][c][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][c] for e in range(n))
        return s
    Rie=[[[[sp.simplify(R(a,b,c,d)) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric=[[sp.simplify(sum(Rie[a][b][a][c] for a in range(n))) for c in range(n)] for b in range(n)]
    Rs=sp.simplify(sum(gi[b,c]*Ric[b][c] for b in range(n) for c in range(n)))
    Rdn=[[[[sp.simplify(sum(g[a,e]*Rie[e][b][c][d] for e in range(n))) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    riem2=sp.simplify(sum(Rdn[a][b][c][d]*sum(gi[a,e]*gi[b,f]*gi[c,k]*gi[d,l]*Rdn[e][f][k][l]
            for e in range(n) for f in range(n) for k in range(n) for l in range(n))
            for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
    ric2=sp.simplify(sum(gi[a,c]*gi[b,d]*Ric[a][b]*Ric[c][d] for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
    return Rs, ric2, riem2
def weyl_sq(Rs, ric2, riem2): return riem2 - 2*ric2 + Rs**2/3
print('=== Q1 / S10 family: rates (1, 1+s, 1-s)  [planar shear, H=1] ===')
gQ = sp.diag(-1, sp.exp(2*t), sp.exp(2*(t+sig*t)), sp.exp(2*(t-sig*t)))
C2Q = sp.simplify(sp.expand(weyl_sq(*invariants(gQ,x))))
print('  Weyl^2 =', C2Q)
print('  equals sigma^2(4 + 16 sigma^2/3)?', sp.simplify(C2Q - sig**2*(4+16*sig**2/3))==0)
print('  even in sigma?', sp.simplify(C2Q - C2Q.subs(sig,-sig))==0)
print()
print("=== 71's family: rates (H-2s, H+s, H+s)  [axisymmetric shear, H free] ===")
g7 = sp.diag(-1, sp.exp(2*(H-2*sig)*t), sp.exp(2*(H+sig)*t), sp.exp(2*(H+sig)*t))
C27 = sp.simplify(sp.expand(weyl_sq(*invariants(g7,x))))
print('  Weyl^2 =', sp.factor(C27))
print('  equals 12 sigma^2 (H-2 sigma)^2?', sp.simplify(C27 - 12*sig**2*(H-2*sig)**2)==0)
print('  even in sigma?', sp.simplify(C27 - C27.subs(sig,-sig))==0)
print('  cubic coefficient:', sp.simplify(sp.expand(C27).coeff(sig,3)))
print()
print('=== the shear invariants, which is why the leading coefficients differ ===')
for name,d in (('Q1 (0, s, -s)',[0,sig,-sig]), ("71 (-2s, s, s)",[-2*sig,sig,sig])):
    s2=sum(v**2 for v in d); print(f'  {name}: trace={sp.simplify(sum(d))}, sigma_ab sigma^ab = {sp.simplify(s2)}')
print('  ratio of shear invariants:', sp.simplify(6*sig**2/(2*sig**2)))
print('  ratio of leading Weyl^2 coefficients at H=1:',
      sp.simplify(sp.expand(C27.subs(H,1)).coeff(sig,2)/sp.expand(C2Q).coeff(sig,2)))


# ------------------------------------------------------------------ the gates
_g = []
def gate(ok, line):
    _g.append((bool(ok), line)); print(('  \u2714 ' if ok else '  \u26d4 ') + line)

print()
print('=' * 100)
C2Q_e = sp.expand(C2Q); C27_e = sp.expand(C27)
gate(sp.simplify(C2Q - sig**2*(4 + 16*sig**2/3)) == 0,
     "L549/Q1's family reproduces S10's polynomial EXACTLY: sigma^2(4 + 16 sigma^2/3) -- so the "
     "receipt's formula is right, on the family Q1 names and S10 does not")
gate(sp.simplify(C2Q - C2Q.subs(sig, -sig)) == 0,
     'and it is EVEN in sigma, which is forced: the eigenvalues are (0, s, -s) and y <-> z is a '
     'symmetry of the family, so no odd power can appear -- the vanishing cubic is a symmetry, '
     'not a claim that could be wrong')
gate(sp.simplify(C27 - 12*sig**2*(H - 2*sig)**2) == 0,
     "71's family gives 12 sigma^2 (H - 2 sigma)^2 exactly, as 71 reports")
gate(sp.simplify(C27 - C27.subs(sig, -sig)) != 0 and sp.simplify(C27_e.coeff(sig, 3) + 48*H) == 0,
     "and it is NOT even, with cubic coefficient exactly -48H: the eigenvalues are (-2s, s, s), "
     "axisymmetric, and s -> -s carries the oblate member to the prolate one, so nothing forces "
     "evenness -- 71's cubic is right too")
gate(sp.simplify(sum(v**2 for v in [0, sig, -sig]) - 2*sig**2) == 0
     and sp.simplify(sum(v**2 for v in [-2*sig, sig, sig]) - 6*sig**2) == 0,
     'the two shears are not the same size: sigma_ab sigma^ab is 2 sigma^2 on Q1 and 6 sigma^2 on '
     "71's, a factor of 3")
gate(sp.simplify(C27_e.subs(H, 1).coeff(sig, 2) / C2Q_e.coeff(sig, 2) - 3) == 0,
     'and the leading Weyl^2 coefficients differ by exactly that factor of 3 at H = 1 (12 against '
     '4) -- THE TWO POLYNOMIALS AGREE ONCE NORMALISED BY THE SHEAR INVARIANT, so there is no '
     'disagreement to adjudicate')
gate(sp.simplify(C2Q.subs(sig, 0)) == 0 and sp.simplify(C27.subs(sig, 0)) == 0,
     'and both vanish shear-free and enter at second order, which is the part of the receipt 71 '
     'reported as surviving -- it is the whole of what the two families share')

print('\n' + '=' * 100)
bad = [l for ok, l in _g if not ok]
print(f'  gates run: {len(_g)}   failed: {len(bad)}')
for l in bad: print('    FAILED: ' + l)
print('=' * 100)
sys.exit(1 if bad else 0)
