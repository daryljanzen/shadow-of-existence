exec(open('gen2.py').read())
CL='simp only [Pi.mul_apply, Pi.add_apply, Pi.sub_apply, Pi.div_apply, Pi.pow_apply, Pi.neg_apply, Nat.cast_ofNat, Nat.add_one_sub_one, pow_one]; '
# hand metric
gh={'kds_g00':(a**2*Q*S-D)/(P*X**2),'kds_g03':a*S*(D-Q*(r**2+a**2))/(P*X**2),'kds_g33':S*(Q*(r**2+a**2)**2-a**2*S*D)/(P*X**2),'kds_g11':P/D,'kds_g22':P/(Q*S)}
for k,e in gh.items(): emit_def(k,e)
for k,e in gh.items():
  for v in (r,x):
    emit_deriv(k,e,v,chain(e,v),'CLX'+'field_simp; ring')
print('\n'.join(out))
import pickle; pickle.dump(fnargs,open('fa1.pkl','wb'))
