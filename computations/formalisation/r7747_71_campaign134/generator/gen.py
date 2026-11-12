import sympy as sp, itertools, sys
r,x,a,M,L=sp.symbols('r x a M L')
P,D,Q,S,X=sp.symbols('P D Q S X')  # atoms
atom_poly={P:r**2+a**2*x**2, D:(r**2+a**2)*(1-L*r**2/3)-2*M*r, Q:1+L*a**2*x**2/3, S:1-x**2, X:1+L*a**2/3}
atom_lean={P:'kds_P a r x',D:'kds_D a M L r',Q:'kds_Q a L x',S:'kds_S x',X:'kds_X a L'}
atom_hyp={P:'hP',D:'hD',Q:'hQ',S:'hS',X:'hX'}
# derivative of atoms (as polys in r,x)
atom_d={r:{P:2*r,D:sp.diff(atom_poly[D],r)}, x:{P:2*a**2*x,Q:sp.diff(atom_poly[Q],x),S:-2*x}}
coords=[None,r,x,None]
def expand_atoms(e): return e.subs(atom_poly)

def atomize(e):
  """polynomial-rational e -> expression in atoms: const * prod(factors) / prod(atoms^k)"""
  e=sp.factor(sp.together(e))
  if e==0: return sp.Integer(0)
  n,d=sp.fraction(e)
  def conv(p):
    c,fl=sp.factor_list(sp.expand(p))
    out=[]; c=sp.Rational(c)
    fl=dict(fl)
    # combine x-1,x+1 into S
    if (x-1) in fl and (x+1) in fl:
      k=min(fl[x-1],fl[x+1]); fl[x-1]-=k; fl[x+1]-=k; out.append((S,k)); c*=(-1)**k
    for f,k in fl.items():
      if k==0: continue
      hit=None
      for A,pp in atom_poly.items():
        q=sp.cancel(f/pp)
        if q.free_symbols==set() : hit=(A,q);break
      if hit: out.append((hit[0],k)); c*=hit[1]**k
      else: out.append((f,k))
    return c,out
  cn,fn=conv(n); cd,fd=conv(d)
  for f,k in fd: assert f in atom_poly, ('den not atom',f)
  return (cn/cd, fn, fd)

def tolean(e):
  nn,dd=sp.fraction(e)
  if dd!=1: return f"({tolean(nn)} / {tolean(dd)})"
  """print sympy expr (poly in r x a M L and atom symbols)"""
  if e in atom_lean: return atom_lean[e]
  if e.is_Symbol: return str(e)
  if e.is_Integer: return f'({e}:ℝ)' if e<0 else str(e)
  if e.is_Rational: return f'(({e.p}:ℝ)/{e.q})'
  if e.is_Add: return '('+' + '.join(tolean(t) for t in e.args)+')'
  if e.is_Mul: return '('+' * '.join(tolean(t) for t in e.args)+')'
  if e.is_Pow:
    assert e.exp.is_Integer and e.exp>0, e
    return f'({tolean(e.base)} ^ {e.exp})'
  raise Exception(e)

# ---- tree for HasDerivAt
# nodes: ('c',expr) ('v',) ('A',atom) ('add',n1,n2) ('mul',n1,n2) ('pow',n,k) ('div',n,d)
def tree(e,v):
  if e.is_Number or (e.is_Symbol and e not in atom_lean and e!=v): return ('c',e)
  if e==v: return ('v',)
  if e in atom_lean:
    if e in atom_d[v]: return ('A',e)
    return ('c',e)
  if not (e.free_symbols & ({v}|{A for A in atom_d[v]})): return ('c',e)
  if e.is_Add:
    ts=[tree(t,v) for t in e.args]; n=ts[0]
    for t in ts[1:]: n=('add',n,t)
    return n
  if e.is_Mul:
    ts=[tree(t,v) for t in e.args]; n=ts[0]
    for t in ts[1:]: n=('mul',n,t)
    return n
  if e.is_Pow: return ('pow',tree(e.base,v),int(e.exp))
  raise Exception(e)
def tprint(n,v):
  k=n[0]
  if k=='c': return tolean(n[1])
  if k=='v': return str(v)
  if k=='A': return atom_lean[n[1]]
  if k=='add': return f'({tprint(n[1],v)} + {tprint(n[2],v)})'
  if k=='mul': return f'({tprint(n[1],v)} * {tprint(n[2],v)})'
  if k=='pow': return f'({tprint(n[1],v)} ^ {n[2]})'
  if k=='div': return f'({tprint(n[1],v)} / {tprint(n[2],v)})'
def nz(n):
  k=n[0]
  if k=='A' or (k=='c' and n[1] in atom_hyp): return atom_hyp[n[1]]
  if k=='pow': return f'(pow_ne_zero {n[2]} {nz(n[1])})'
  if k=='mul': return f'(mul_ne_zero {nz(n[1])} {nz(n[2])})'
  raise Exception(n)
def tproof(n,v):
  k=n[0]
  if k=='c': return f'(hasDerivAt_const {v} ({tolean(n[1])} : ℝ))'
  if k=='v': return f'(hasDerivAt_id\' {v})'
  if k=='A': return f'(kds_{n[1]}_d{v} a M L r x)'
  if k=='add': return f'({tproof(n[1],v)}.fun_add {tproof(n[2],v)})'
  if k=='mul': return f'({tproof(n[1],v)}.fun_mul {tproof(n[2],v)})'
  if k=='pow': return f'({tproof(n[1],v)}.fun_pow {n[2]})'
  if k=='div': return f'({tproof(n[1],v)}.fun_div {tproof(n[2],v)} {nz(n[2])})'

def form(af):
  """atomized -> sympy num expr, den list -> build tree-able structure"""
  c,fn,fd=af
  num=c
  for f,k in fn: num=num*f**k if k!=1 else num*f
  den=sp.Integer(1)
  for f,k in fd: den=den*f**k if k!=1 else den*f
  return num,den
def body_tree(af,v):
  num,den=form(af)
  if den==1: return tree(num,v)
  return ('div',tree(num,v),tree(den,v))
def body_print(af):
  num,den=form(af)
  # print via a tree with v=None-ish: use tprint with dummy var
  t=body_tree(af,r)
  return tprint(t,r)

def nz_expr(e):
  if e.is_Number: return '(by norm_num)'
  if e in atom_hyp: return atom_hyp[e]
  if e.is_Pow: return f'(pow_ne_zero {e.exp} {nz_expr(e.base)})'
  if e.is_Mul:
    args=list(e.args); s=nz_expr(args[0])
    for t in args[1:]: s=f'(mul_ne_zero {s} {nz_expr(t)})'
    return s
  raise Exception(e)
def nz(n):
  k=n[0]
  if k=='c': return nz_expr(n[1])
  if k=='A': return atom_hyp[n[1]]
  if k=='pow': return f'(pow_ne_zero {n[2]} {nz(n[1])})'
  if k=='mul': return f'(mul_ne_zero {nz(n[1])} {nz(n[2])})'
  raise Exception(n)
dl={(P,r):'(kds_P_dr a r x)',(P,x):'(kds_P_dx a r x)',(D,r):'(kds_D_dr a M L r)',(Q,x):'(kds_Q_dx a L x)',(S,x):'(kds_S_dx x)'}
def tproof(n,v):
  k=n[0]
  if k=='c': return f'(hasDerivAt_const {v} ({tolean(n[1])} : ℝ))'
  if k=='v': return f"(hasDerivAt_id' {v})"
  if k=='A': return dl[(n[1],v)]
  if k=='add': return f'({tproof(n[1],v)}.fun_add {tproof(n[2],v)})'
  if k=='mul': return f'({tproof(n[1],v)}.fun_mul {tproof(n[2],v)})'
  if k=='pow': return f'({tproof(n[1],v)}.fun_pow {n[2]})'
  if k=='div': return f'({tproof(n[1],v)}.fun_div {tproof(n[2],v)} {nz(n[2])})'

# ---- geometry
Lam=L
s2=1-x**2
rho2=atom_poly[P]; Dr=atom_poly[D]; Dt=atom_poly[Q]; Xi=atom_poly[X]
g=sp.zeros(4)
g[0,0]=(-Dr+Dt*s2*a**2)/(rho2*Xi**2)
g[0,3]=g[3,0]=(Dr*a*s2-Dt*s2*a*(r**2+a**2))/(rho2*Xi**2)
g[3,3]=(-Dr*a**2*s2**2+Dt*s2*(r**2+a**2)**2)/(rho2*Xi**2)
g[1,1]=rho2/Dr
g[2,2]=rho2/(Dt*s2)
Xc=[sp.Symbol('t'),r,x,sp.Symbol('phi')]
gi=g.inv(); gi=gi.applyfunc(lambda e: sp.factor(sp.cancel(e)))
G=[[[sp.factor(sp.cancel(sp.Rational(1,2)*sum(gi[A,Dd]*(sp.diff(g[Dd,C],Xc[B])+sp.diff(g[Dd,B],Xc[C])-sp.diff(g[B,C],Xc[Dd])) for Dd in range(4)))) for C in range(4)] for B in range(4)] for A in range(4)]

_tree_old=tree
def tree(e,v):
  if not (e.free_symbols & ({v}|{A for A in atom_d[v]})): return ('c',e)
  n,d=sp.fraction(e)
  if d!=1:
    return ('div',_tree_old2(n,v),_tree_old2(d,v))
  return _tree_old2(e,v)
def _tree_old2(e,v):
  if e.is_Number or (e.is_Symbol and e not in atom_lean and e!=v): return ('c',e)
  if e==v: return ('v',)
  if e in atom_lean:
    if e in atom_d[v]: return ('A',e)
    return ('c',e)
  if not (e.free_symbols & ({v}|{A for A in atom_d[v]})): return ('c',e)
  if e.is_Add:
    ts=[tree(t,v) for t in e.args]; nn=ts[0]
    for t in ts[1:]: nn=('add',nn,t)
    return nn
  if e.is_Mul:
    ts=[tree(t,v) for t in e.args]; nn=ts[0]
    for t in ts[1:]: nn=('mul',nn,t)
    return nn
  if e.is_Pow: return ('pow',tree(e.base,v),int(e.exp))
  raise Exception(e)
