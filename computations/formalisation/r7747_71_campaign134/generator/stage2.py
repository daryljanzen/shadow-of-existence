exec(open('gen2.py').read())
CL='simp only [Pi.mul_apply, Pi.add_apply, Pi.sub_apply, Pi.div_apply, Pi.pow_apply, Pi.neg_apply, Nat.cast_ofNat, Nat.add_one_sub_one, pow_one]; '
import pickle
fnargs.update(pickle.load(open('fa1.pkl','rb')))
def A2e(af):
  num,den=form(af); return num/den if den!=1 else num
UNF='simp only [kds_P, kds_D, kds_Q, kds_S, kds_X]'
# inverse defs
for (i,j) in [(0,0),(0,3),(3,3),(1,1),(2,2)]:
  emit_def(f'kds_i{i}{j}',A2e(atomize(gi[i,j])))
# Gamma defs (canonical B<=C)
names={}
for A in range(4):
  for B in range(4):
    for C in range(B,4):
      if G[A][B][C]!=0:
        nm=f'kds_G{A}{B}{C}'; e=A2e(atomize(G[A][B][C])); names[(A,B,C)]=(nm,e)
        emit_def(nm,e)
derivs=[]
for (A,B,C),(nm,e) in names.items():
  for v in (r,x):
    full_e=G[A][B][C]
    dv=sp.diff(full_e,v)
    if sp.simplify(dv)==0: continue
    de=A2e(atomize(dv))
    ln=emit_deriv(nm,e,v,de,'CLX'+'field_simp; UNFX; ring')
    if ln: derivs.append((nm,v,ln))
print('\n'.join(out))
pickle.dump((fnargs,names,derivs),open('fa2.pkl','wb'))
