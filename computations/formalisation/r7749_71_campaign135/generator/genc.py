import sympy as sp, pickle
r,p,L=sp.symbols('r p L')
Sg,R,R1,R2,Pp,P1,P2=sp.symbols('Sg R R1 R2 Pp P1 P2')
atom_poly={Sg:r**2+p**2}
lean_atom={Sg:'car_S r p',R:'R r',R1:'R1 r',R2:'R2 r',Pp:'P p',P1:'P1 p',P2:'P2 p'}
hyp_nz={Sg:'hS',R:'hR0',Pp:'hP0'}
FUNS=[R,R1,R2,Pp,P1,P2]; FN={R:'R',R1:'R1',R2:'R2',Pp:'P',P1:'P1',P2:'P2'}
atom_d={r:{Sg:2*r,R:R1,R1:R2}, p:{Sg:2*p,Pp:P1,P1:P2}}
dterm={(Sg,r):'(car_S_dr r p)',(Sg,p):'(car_S_dp r p)',(R,r):'(hR r)',(R1,r):'(hR1 r)',(Pp,p):'(hP p)',(P1,p):'(hP1 p)'}
dhyp={(R,r):('hR','(hR : ∀ t, HasDerivAt R (R1 t) t)'),(R1,r):('hR1','(hR1 : ∀ t, HasDerivAt R1 (R2 t) t)'),
      (Pp,p):('hP','(hP : ∀ t, HasDerivAt P (P1 t) t)'),(P1,p):('hP1','(hP1 : ∀ t, HasDerivAt P1 (P2 t) t)')}
ATOMS=list(lean_atom)
def isatom(e): return e in lean_atom
def tolean(e):
  if isatom(e): return lean_atom[e]
  nn,dd=sp.fraction(e)
  if dd!=1: return f"({tolean(nn)} / {tolean(dd)})"
  if e.is_Symbol: return str(e)
  if e.is_Integer: return f'({e}:ℝ)' if e<0 else str(e)
  if e.is_Rational: return f'(({e.p}:ℝ)/{e.q})'
  if e.is_Add: return '('+' + '.join(tolean(t) for t in e.args)+')'
  if e.is_Mul: return '('+' * '.join(tolean(t) for t in e.args)+')'
  if e.is_Pow:
    assert e.exp.is_Integer and e.exp>0, e
    return f'({tolean(e.base)} ^ {e.exp})'
  raise Exception(e)
def dep(e,v): return bool(e.free_symbols & ({v}|set(atom_d[v])))
def tree(e,v):
  if not dep(e,v): return ('c',e)
  n,d=sp.fraction(e)
  if d!=1: return ('div',tree(n,v),tree(d,v))
  if e==v: return ('v',)
  if isatom(e): return ('A',e)
  if e.is_Add or e.is_Mul:
    ts=[tree(t,v) for t in e.args]; nn=ts[0]
    for t in ts[1:]: nn=('add' if e.is_Add else 'mul',nn,t)
    return nn
  if e.is_Pow: return ('pow',tree(e.base,v),int(e.exp))
  raise Exception(e)
def tprint(n):
  k=n[0]
  if k=='c': return tolean(n[1])
  if k=='v': return 'VAR'
  if k=='A': return lean_atom[n[1]]
  if k in('add','mul','div'): return f"({tprint(n[1])} {dict(add='+',mul='*',div='/')[k]} {tprint(n[2])})"
  if k=='pow': return f'({tprint(n[1])} ^ {n[2]})'
def nz_expr(e):
  if e.is_Number: return '(by norm_num)'
  if e in hyp_nz: return hyp_nz[e]
  if e.is_Pow: return f'(pow_ne_zero {e.exp} {nz_expr(e.base)})'
  if e.is_Mul:
    a=list(e.args); s=nz_expr(a[0])
    for t in a[1:]: s=f'(mul_ne_zero {s} {nz_expr(t)})'
    return s
  raise Exception(e)
def nz(n):
  k=n[0]
  if k=='c': return nz_expr(n[1])
  if k=='A': return hyp_nz[n[1]]
  if k=='pow': return f'(pow_ne_zero {n[2]} {nz(n[1])})'
  if k=='mul': return f'(mul_ne_zero {nz(n[1])} {nz(n[2])})'
  raise Exception(n)
def tproof(n,v,used):
  k=n[0]
  if k=='c': return f'(hasDerivAt_const {v} ({tolean(n[1])} : ℝ))'
  if k=='v': return f"(hasDerivAt_id' {v})"
  if k=='A':
    if (n[1],v) in dhyp: used.add((n[1],v))
    return dterm[(n[1],v)]
  if k=='add': return f'({tproof(n[1],v,used)}.fun_add {tproof(n[2],v,used)})'
  if k=='mul': return f'({tproof(n[1],v,used)}.fun_mul {tproof(n[2],v,used)})'
  if k=='pow': return f'({tproof(n[1],v,used)}.fun_pow {n[2]})'
  if k=='div': return f'({tproof(n[1],v,used)}.fun_div {tproof(n[2],v,used)} {nz(n[2])})'
def atomize(e):
  e=sp.factor(sp.together(e))
  if e==0: return sp.Integer(0)
  n,d=sp.fraction(e)
  def conv(q):
    c,fl=sp.factor_list(sp.expand(q)); c=sp.Rational(c); out=sp.Integer(1)
    for f,k in fl:
      if sp.expand(f-atom_poly[Sg])==0: out*=Sg**k
      elif sp.expand(f+atom_poly[Sg])==0: out*=Sg**k; c*=(-1)**k
      else: out*=f**k
    return c,out
  cn,fn=conv(n); cd,fd=conv(d)
  num=(cn/cd)*fn
  return num/fd if fd!=1 else num
def chain(e,v):
  d=sp.diff(e,v)
  for A,dv in atom_d[v].items(): d+=sp.diff(e,A)*dv
  return d
def expand_atoms(e): return e.subs(atom_poly)
ORD=[R,R1,R2,Pp,P1,P2,r,p]
def args_of(e):
  fs=set(e.free_symbols)
  if Sg in fs: fs|={r,p}
  res=[]
  for s in ORD:
    if s in fs: res.append(s)
  for A in [R,R1,R2]:
    if A in fs: res.append(r) if r not in res else None
  for A in [Pp,P1,P2]:
    if A in fs: res.append(p) if p not in res else None
  return [s for s in ORD if s in res]
def argstr(ag,rr='r',pp='p'):
  return ' '.join(FN[s] if s in FN else {r:rr,p:pp}[s] for s in ag)
def binder(ag):
  fs=[FN[s] for s in ag if s in FN]; vs=[str(s) for s in ag if s in (r,p)]
  out=[]
  if fs: out.append(f"({' '.join(fs)} : ℝ → ℝ)")
  if vs: out.append(f"({' '.join(vs)} : ℝ)")
  return ' '.join(out)
