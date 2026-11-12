HEAVY={('kds_G233','x')}
exec(open('gen.py').read())
ARGS=[a,M,L,r,x]
def args_of(e):
  fs=set()
  e2=e
  for A in atom_poly:
    if e.has(A): fs|=atom_poly[A].free_symbols
  fs|=e.free_symbols - set(atom_poly)
  return [s for s in ARGS if s in fs]
def chain(e,v):
  d=sp.diff(e,v)
  for A,dv in atom_d[v].items(): d+=sp.diff(e,A)*dv
  return d
def full(e): return e.subs(atom_poly)
out=[]
fnargs={}
def emit_def(name,e):
  ag=args_of(e); fnargs[name]=ag
  t=tree(e,r)  # tree just for printing
  out.append(f"noncomputable def {name} ({' '.join(map(str,ag))} : ℝ) : ℝ :=\n  {tprint(t,r)}\n")
def call(name,rr='r',xx='x'):
  return '('+name+' '+' '.join({r:rr,x:xx}.get(s,str(s)) for s in fnargs[name])+')'
def hyps_for(e):
  hs=[]
  for A in [P,D,Q,S,X]:
    if e.has(A): hs.append(A)
  return hs
def hyp_binders(hs):
  return ' '.join(f'({atom_hyp[A]} : {atom_lean[A]} ≠ 0)' for A in hs)
def emit_deriv(name,e,v,dexpr,close):
  # lemma name_dv
  ag=fnargs[name]
  lam = call(name, rr='t') if v==r else call(name, xx='t')
  n=tree(e,v)
  if n[0]=='c':
    return None
  hs=hyps_for(e)  # only denominators really needed; keep all appearing atoms in denominators
  num,den=sp.fraction(e)
  hs=hyps_for(den)
  # lemma args: all of a M L r x that appear in function args plus v
  la=[s for s in ARGS if s in ag or s==v]
  ks=set()
  def walk(m):
    ks.add(m[0] if m[0]!='pow' else ('pow',m[2]))
    for c in m[1:]:
      if isinstance(c,tuple): walk(c)
  walk(n)
  sl=[]
  if any(isinstance(k,tuple) for k in ks): sl.append('Nat.cast_ofNat')
  ats=[A for A in [P,D,Q,S,X] if e.has(A) or dexpr.has(A)]
  close=close.replace('UNFX','simp only ['+', '.join(atom_lean[A].split()[0] for A in ats)+']')
  close=close.replace('CLX', 'simp only ['+', '.join(sl)+']; ' if sl else '')
  hb='set_option maxHeartbeats 1000000 in\n' if (name,str(v)) in HEAVY else ''
  out.append(hb+f"lemma {name}_d{v} ({' '.join(map(str,la))} : ℝ) {hyp_binders(hs)} :\n    HasDerivAt (fun t => {lam}) {tolean(dexpr)} {v} := by\n  have h := {tproof(n,v)}\n  exact h.congr_deriv (by {close})\n")
  return f'{name}_d{v}'
