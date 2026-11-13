exec(open('genc.py').read())
import sys
tau,sig=sp.symbols('tau sigma')
X=[tau,sig,r,p]
gh={(0,0):(R-Pp)/Sg,(0,1):-(R*p**2+Pp*r**2)/Sg,(1,1):(R*p**4-Pp*r**4)/Sg,(2,2):Sg/R,(3,3):Sg/Pp}
g=sp.zeros(4)
for (i,j),e in gh.items(): g[i,j]=g[j,i]=expand_atoms(e)
def D(e,c):
  if c in (0,1): return sp.Integer(0)
  return chain(e,X[c])
gi=g.inv().applyfunc(lambda e: sp.factor(sp.cancel(e)))
G=[[[sp.factor(sp.cancel(sp.Rational(1,2)*sum(gi[A,Dd]*(D(g[Dd,C],B)+D(g[Dd,B],C)-D(g[B,C],Dd)) for Dd in range(4)))) for C in range(4)] for B in range(4)] for A in range(4)]
def Ric(b,d):
  return sum(D(G[A][d][b],A)-D(G[A][A][b],d)+sum(G[A][A][E]*G[E][d][b]-G[A][d][E]*G[E][A][b] for E in range(4)) for A in range(4))
out=[]; fnargs={}
def emit_def(name,e,doc=None):
  ag=args_of(e); fnargs[name]=ag
  if doc: out.append(f'/-- {doc} -/')
  out.append(f"noncomputable def {name} {binder(ag)} : ℝ :=\n  {tprint(tree(e,r)).replace('VAR','r')}\n")
def call(name,rr='r',pp='p'):
  return '('+name+' '+argstr(fnargs[name],rr,pp)+')'
def emit_deriv(name,e,v,dexpr,unfold):
  n=tree(e,v)
  if n[0]=='c': return None
  used=set(); term=tproof(n,v,used)
  num,den=sp.fraction(e)
  nzs=[A for A in [Sg,R,Pp] if den.has(A)]
  ag=fnargs[name]; la=[s for s in ORD if s in ag or s==v]
  # function args needed by hyps
  for (A,vv) in used:
    for s in ([R,R1,R2] if A in (R,R1) else [Pp,P1,P2]):
      if s in (A, {R:R1,R1:R2,Pp:P1,P1:P2}[A]) and s not in la: la.append(s)
  for A in nzs:
    if A in FN and A not in la: la.append(A)
  for s in ([r] if any(A in (Sg,R) for A in nzs) else [])+([p] if any(A in (Sg,Pp) for A in nzs) else []):
    if s not in la: la.append(s)
  la=[s for s in ORD if s in la]
  hb=' '.join(dhyp[k][1] for k in sorted(used,key=lambda k:str(k)))
  nb=' '.join(f"({hyp_nz[A]} : {lean_atom[A]} ≠ 0)" for A in nzs)
  lam=call(name, rr='t') if v==r else call(name, pp='t')
  ks=set()
  def walk(m):
    ks.add(m[0] if m[0]!='pow' else 'pow')
    for c in m[1:]:
      if isinstance(c,tuple): walk(c)
  walk(n)
  pre='simp only [Nat.cast_ofNat]; ' if 'pow' in ks else ''
  unf='; simp only [car_S]' if (unfold and (e.has(Sg) or dexpr.has(Sg))) else ''
  close=f'{pre}field_simp{unf}; ring'
  out.append(f"lemma {name}_d{v} {binder(la)} {hb} {nb} :\n    HasDerivAt (fun t => {lam}) {tolean(dexpr)} {v} := by\n  have h := {term.replace('VAR',str(v))}\n  exact h.congr_deriv (by {close})\n")
  hyps=[dhyp[k][0] for k in sorted(used,key=lambda k:str(k))]+[hyp_nz[A] for A in nzs]
  return (name,v,la,hyps)
def A(e): return atomize(e)
# metric defs (hand forms)
MN={(0,0):'car_g00',(0,1):'car_g01',(1,1):'car_g11',(2,2):'car_g22',(3,3):'car_g33'}
for k,nm in MN.items(): emit_def(nm,gh[k])
mder=[]
for k,nm in MN.items():
  for v in (r,p):
    res=emit_deriv(nm,gh[k],v,chain(gh[k],v),False)
    if res: mder.append(res)
IN={(0,0):'car_i00',(0,1):'car_i01',(1,1):'car_i11',(2,2):'car_i22',(3,3):'car_i33'}
for k,nm in IN.items(): emit_def(nm,A(gi[k]))
GN={}
for a in range(4):
  for b in range(4):
    for c in range(b,4):
      if G[a][b][c]!=0:
        nm=f'car_G{a}{b}{c}'; e=A(G[a][b][c]); GN[(a,b,c)]=(nm,e); emit_def(nm,e)
gder=[]
for (a,b,c),(nm,e) in GN.items():
  for v in (r,p):
    dv=sp.cancel(sp.together(chain(expand_atoms(e),v)))
    if dv==0: continue
    print("G",nm,v,flush=True); res=emit_deriv(nm,e,v,A(dv),True)
    if res: gder.append(res)
RN={}
for b in range(4):
  for d in range(b,4):
    print("ric",b,d,flush=True); e=A(sp.cancel(sp.together(Ric(b,d))))
    RN[(b,d)]=e
    if e!=0: emit_def(f'car_Ric{b}{d}',e)
open('part1.lean','w').write('\n'.join(out))
pickle.dump((fnargs,mder,gder,{k:v[0] for k,v in GN.items()},{k:(v!=0) for k,v in RN.items()}),open('p1.pkl','wb'))
print(len(mder),len(gder),[k for k,v in RN.items() if v!=0])
for k,v in RN.items(): print(k, len(str(v)))
