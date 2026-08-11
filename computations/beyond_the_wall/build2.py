"""L-163 build, step 2: recognise the equations. Wave map into H^2, plus area, plus constraints."""
import sympy as sp, pickle
t,z = sp.symbols('t z', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z)
om =sp.Function('omega')(t,z); R  =sp.Function('R')(t,z)
Lam=sp.Symbol('Lambda', positive=True)
D=pickle.load(open('eqs.pkl','rb')); EQ=D['EQ']; g=D['g']
E=sp.exp
# standard Gowdy wave-map coordinates
P = 2*psi - sp.log(R); Q = om
dt=lambda e: sp.diff(e,t); dz=lambda e: sp.diff(e,z)

AREA = dt(dt(R)) - dz(dz(R)) - 2*Lam*R*E(2*(gam-psi))
WAVEP = dt(R*dt(P)) - dz(R*dz(P)) - R*E(2*P)*(dt(Q)**2 - dz(Q)**2)
WAVEQ = dt(R*E(2*P)*dt(Q)) - dz(R*E(2*P)*dz(Q))

def red(e): return sp.simplify(sp.expand(sp.powsimp(sp.expand(e), force=True)))

# --- AREA: from the (x,y)-block trace.  Try  g^{AB} EQ_AB  over A,B in {2,3}
gi=sp.simplify(g.inv())
trxy = red(sum(gi[a,b]*EQ[a,b] for a in (2,3) for b in (2,3)))
print("g^{AB} EQ_AB over the torus block, reduced:")
print("   ", sp.simplify(trxy))
cand = red(sp.simplify(trxy) * (-R*E(2*(gam-psi))))
print("\n  times -R e^{2(gam-psi)} :"); print("   ", sp.simplify(cand))
print("\n  ** equals the AREA equation? **", red(cand - AREA)==0, " | ratio-check:",
      sp.simplify(sp.cancel(sp.simplify(cand)/sp.simplify(AREA))) if sp.simplify(AREA)!=0 else None)
