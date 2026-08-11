# Polarized Gowdy-dS edge — canonical structure (rung 1), consolidated r191.
# The four named field equations + the gamma-equation ARE the vacuum-Lambda Einstein
# content G_ab + Lambda g_ab = 0, verified with ALL-ZERO residuals.
# Move 2 re-verification, 2026-06-12 (r190). The original canonical_1.py has SIGN/FACTOR
# TYPOS IN ITS PRINTED CHECK-LINES (it prints 2x or -1x the target instead of 0); the
# physics is exact. This check confirms the same content with ALL-ZERO residuals:
#   MOMENTUM=E_tz*R ; AREA=(E_tt-E_zz)*R ; ENERGY=(E_tt+E_zz)*R ;
#   gamma-eq=-E_yy*e^{2gam}/R^2 ; WAVE=(E_xx_core+R*gameq)/2  modulo AREA.

import sympy as sp
t,z,x,y,Lam = sp.symbols('t z x y Lambda', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z); R=sp.Function('R')(t,z)
coords=[t,z,x,y]
A=sp.exp(2*(gam-psi))
g=sp.diag(-A, A, sp.exp(2*psi), R**2*sp.exp(-2*psi))
gi=g.inv(); n=4
Gamma=[[[0]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
 for b in range(n):
  for c in range(n):
   s=0
   for d in range(n):
    s+=gi[a,d]*(sp.diff(g[d,b],coords[c])+sp.diff(g[d,c],coords[b])-sp.diff(g[b,c],coords[d]))
   Gamma[a][b][c]=sp.simplify(s/2)
Ric=sp.zeros(n,n)
for b in range(n):
 for c in range(n):
  s=0
  for a in range(n):
   s+=sp.diff(Gamma[a][b][c],coords[a])-sp.diff(Gamma[a][b][a],coords[c])
   for d in range(n):
    s+=Gamma[a][a][d]*Gamma[d][b][c]-Gamma[a][c][d]*Gamma[d][b][a]
  Ric[b,c]=sp.simplify(s)
Rs=sp.simplify(sum(gi[a,b]*Ric[a,b] for a in range(n) for b in range(n)))
Ein=sp.zeros(n,n)
for a in range(n):
 for b in range(n):
  Ein[a,b]=sp.simplify(Ric[a,b]-sp.Rational(1,2)*g[a,b]*Rs + Lam*g[a,b])
Rt,Rz=sp.diff(R,t),sp.diff(R,z); Rtt,Rzz,Rtz=sp.diff(R,t,t),sp.diff(R,z,z),sp.diff(R,t,z)
pt,pz=sp.diff(psi,t),sp.diff(psi,z); gt,gz=sp.diff(gam,t),sp.diff(gam,z)
src=R*sp.exp(2*(gam-psi))
AREA  = Rtt-Rzz - 2*Lam*src
WAVE  = sp.diff(R*pt,t)-sp.diff(R*pz,z) - Lam*src
ENERGY= 2*(Rt*gt+Rz*gz)-(Rtt+Rzz) - 2*R*(pt**2+pz**2)
MOM   = Rt*gz+Rz*gt-Rtz - 2*R*pt*pz
gameq = sp.diff(gam,t,t)-sp.diff(gam,z,z)+pt**2-pz**2 - Lam*sp.exp(2*(gam-psi))
E_tt,E_zz,E_tz,E_xx,E_yy = (sp.simplify(Ein[0,0]),sp.simplify(Ein[1,1]),
                            sp.simplify(Ein[0,1]),sp.simplify(Ein[2,2]),sp.simplify(Ein[3,3]))
print("MOMENTUM = E_tz*R                :", sp.simplify(E_tz*R - MOM))
print("AREA     = (E_tt-E_zz)*R         :", sp.simplify((E_tt-E_zz)*R - AREA))
print("ENERGY   = (E_tt+E_zz)*R         :", sp.simplify((E_tt+E_zz)*R - ENERGY))
print("gamma-eq = -E_yy*e^{2*gam}/R^2     :", sp.simplify(-E_yy*sp.exp(2*gam)/R**2 - gameq))
Exx_core = sp.simplify(E_xx*R*sp.exp(2*gam-4*psi))
print("WAVE: (E_xx_core + R*gameq)/2 - WAVE, modulo AREA:",
      sp.simplify((Exx_core + R*gameq)/2 - WAVE + AREA/2))
