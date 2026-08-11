"""L-163 build, step 3: solve the six components for the second time-derivatives, and identify."""
import sympy as sp, pickle
t,z = sp.symbols('t z', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z)
om =sp.Function('omega')(t,z); R  =sp.Function('R')(t,z)
Lam=sp.Symbol('Lambda', positive=True)
D=pickle.load(open('eqs.pkl','rb')); EQ=D['EQ']
E=sp.exp
comps=[EQ[0,0],EQ[0,1],EQ[1,1],EQ[2,2],EQ[2,3],EQ[3,3]]
unk=[sp.Derivative(psi,(t,2)), sp.Derivative(om,(t,2)),
     sp.Derivative(R,(t,2)),   sp.Derivative(gam,(t,2))]
sol=sp.solve([sp.numer(sp.together(sp.simplify(c))) for c in comps], unk, dict=True)
print("solutions found:", len(sol))
s=sol[0]
for k in unk:
    print("\n===", k, "=")
    sp.pprint(sp.simplify(sp.expand(s[k])))
pickle.dump(s, open('sol.pkl','wb'))
