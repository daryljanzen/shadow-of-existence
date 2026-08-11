"""
P08_lapse_split.py -- verifies prop:lapse (Leaf and stacking) by DERIVING the Einstein tensor of the
  two-function metric ds^2=-A(r) dt^2+dr^2/f(r)+r^2 dOmega^2 (lapse A, spatial profile f, independent):
    (i)  8pi T^t_t = (r f'+f-1)/r^2 + Lambda -- INDEPENDENT of A (density is the leaf alone; rho=m'/4pi r^2);
    (ii) the radial equation of state 8pi(T^r_r - T^t_t)=8pi(p_r+rho) = (f/r) d/dr ln(A/f) -- carried by the
         divergence of the lapse A from the curve f;
    (iii)the lock A=f annihilates the log => p_r+rho=0 (the construction-gauge identity).
  [P8 slicing_operator sec:lapse]
STATUS: ✔✔   RUN: python3 P08_lapse_split.py   RUNTIME: ~9s
CONTROL: A=f*g(r) with g non-constant gives p_r+rho = (f/r) g'/g != 0 -- general radial pressure, fixed by
  the RATE of the lapse's divergence; A=f (g=const) returns p_r=-rho.
ORIGIN: built new r1360 (P8 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
t,r,th,ph,Lam = sp.symbols('t r theta phi Lambda', real=True)
A=sp.Function('A')(r); f=sp.Function('f')(r)
x=[t,r,th,ph]; n=4
g=sp.diag(-A, 1/f, r**2, r**2*sp.sin(th)**2); gi=g.inv()
Gamma=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def ricci(b,c):
    return sp.simplify(sum(sp.diff(Gamma[a][b][c],x[a]) for a in range(n))
                       - sum(sp.diff(Gamma[a][b][a],x[c]) for a in range(n))
                       + sum(Gamma[a][a][d]*Gamma[d][b][c] for a in range(n) for d in range(n))
                       - sum(Gamma[a][c][d]*Gamma[d][b][a] for a in range(n) for d in range(n)))
Ric=sp.Matrix(n,n, lambda i,j: ricci(i,j)); Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
Gud=sp.simplify(gi*(Ric - Rs*g/2))
fp,Ap=sp.diff(f,r),sp.diff(A,r)
print("="*70); print("P08 lapse split (two-function metric, Einstein tensor DERIVED)"); print("="*70)
# (i) G^t_t independent of A
Gtt=sp.simplify(Gud[0,0])
ok&=check("G^t_t = (r f'+f-1)/r^2  -- INDEPENDENT of A (density = the leaf f alone)",
          sp.simplify(Gtt-(r*fp+f-1)/r**2)==0 and A not in Gtt.free_symbols and sp.diff(Gtt,r).has(Ap)==False)
ok&=check("=> 8pi T^t_t=(r f'+f-1)/r^2+Lambda, so rho depends on f alone (eq:rho-B)",
          sp.simplify((Gtt+Lam) - ((r*fp+f-1)/r**2+Lam))==0)
# (ii) G^r_r and the equation of state
Grr=sp.simplify(Gud[1,1])
ok&=check("G^r_r = (r f A'/A + f - 1)/r^2", sp.simplify(Grr-(r*f*Ap/A+f-1)/r**2)==0)
eos=sp.simplify(Grr-Gtt); target=sp.simplify((f/r)*sp.diff(sp.log(A/f),r))
ok&=check("8pi(T^r_r - T^t_t)=8pi(p_r+rho) = (f/r) d/dr ln(A/f)  (eq:prho, EoS)", sp.simplify(eos-target)==0)
# (iii) the lock A=f => p_r+rho=0
ok&=check("lock A=f annihilates the log => p_r+rho=0 (construction-gauge identity)",
          sp.simplify(eos.subs(A,f).doit())==0)
# CONTROL: A=f*g(r), g non-constant -> p_r+rho = (f/r) g'/g != 0
gfun=sp.Function('g')(r)
eos_g=sp.simplify(eos.subs(A, f*gfun).doit())
ok&=check("CONTROL: A=f*g(r) -> p_r+rho = (f/r) g'/g (general pressure; =0 iff g constant)",
          sp.simplify(eos_g-(f/r)*sp.diff(gfun,r)/gfun)==0)
print("="*70)
print("RESULT:", "ALL PASS -- density is the leaf (f) alone, independent of the lapse A; the radial equation\n         of state is (f/r) d/dr ln(A/f), the lapse's divergence from the curve; A=f returns p_r=-rho." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   AND THE DERIVED TENSOR EVALUATED ON A CONCRETE CUT, which is what makes 'density is the leaf
#   alone' a number rather than a shape.  On the vacuum leaf f = 1 - 2M/r - Lambda r^2/3 the
#   derived G^t_t collapses to -Lambda EXACTLY (so 8 pi T^t_t = G^t_t + Lambda = 0), whatever the
#   lapse A is; at Lambda = 12/100 that is -0.12.
_M, _L = sp.symbols('M_pin Lambda_pin', positive=True)
_f_vac = 1 - 2*_M/r - _L*r**2/3
_Gtt_vac = sp.simplify(Gtt.subs(f, _f_vac).doit())
assert sp.simplify(_Gtt_vac + _L) == 0, _Gtt_vac
_num = float(_Gtt_vac.subs({_L: sp.Rational(12, 100), _M: sp.Rational(2, 5), r: 3}))
assert abs(_num - (-0.12)) < 1e-12, _num
#   and the equation of state on a DIVERGENT lapse A = f*r (g = r, so g'/g = 1/r) is p_r + rho =
#   f/r^2, which at M = 2/5, Lambda = 12/100, r = 3 is 0.04148148148148148 and NOT zero -- the
#   lock A = f is what kills it.
_eos_r = sp.simplify(eos.subs(A, f*r).doit())
assert sp.simplify(_eos_r - f/r**2) == 0, _eos_r
_eosnum = float(_eos_r.subs(f, _f_vac).subs({_L: sp.Rational(12, 100), _M: sp.Rational(2, 5), r: 3}))
assert abs(_eosnum - 0.04148148148148148) < 1e-12, _eosnum
assert sp.simplify(eos.subs(A, f).doit()) == 0          # and the lock returns p_r = -rho exactly
