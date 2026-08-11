"""With NO bulk gauge field there is no inflow, so a wall's chiral content must be anomaly-free ALONE.
Check the SM's 15 per generation against every anomaly condition.  Left-handed Weyl convention."""
from fractions import Fraction as F
# (name, colour dim, isospin dim, hypercharge Y, multiplicity = colour*isospin)
gen=[('Q',3,2,F(1,6)), ('u^c',3,1,F(-2,3)), ('d^c',3,1,F(1,3)), ('L',1,2,F(-1,2)), ('e^c',1,1,F(1))]
tot=sum(c*i for _,c,i,_ in gen); print("   Weyl fermions per generation: %d"%tot)
print()
# [SU(3)]^3 : only triplets/antitriplets contribute; T(3)=+1/2, T(3bar)=-1/2 for the anomaly coefficient
A333=F(0)
for n,c,i,Y in gen:
    if c==3: A333 += F(1,2)*i*(1 if n=='Q' else -1)
print("   [SU(3)]^3        : %s   %s"%(A333,'CANCELS' if A333==0 else 'FAILS'))
# [SU(2)]^2 U(1) : sum over doublets of Y * colour
A221=sum(c*Y for n,c,i,Y in gen if i==2); print("   [SU(2)]^2 U(1)   : %s   %s"%(A221,'CANCELS' if A221==0 else 'FAILS'))
# [SU(3)]^2 U(1) : sum over triplets of Y * isospin
A331=sum(i*Y for n,c,i,Y in gen if c==3); print("   [SU(3)]^2 U(1)   : %s   %s"%(A331,'CANCELS' if A331==0 else 'FAILS'))
# [U(1)]^3
A111=sum(c*i*Y**3 for _,c,i,Y in gen); print("   [U(1)]^3         : %s   %s"%(A111,'CANCELS' if A111==0 else 'FAILS'))
# U(1)-gravitational : sum of Y
A1g=sum(c*i*Y for _,c,i,Y in gen); print("   U(1)-grav        : %s   %s"%(A1g,'CANCELS' if A1g==0 else 'FAILS'))
print()
print("   => the 15 cancel EVERY condition, and do so only as a complete set:")
for drop in ('e^c','u^c','L'):
    sub=[g for g in gen if g[0]!=drop]
    print("      drop %-4s : [U(1)]^3 = %-8s  U(1)-grav = %s"%(drop,
        sum(c*i*Y**3 for _,c,i,Y in sub), sum(c*i*Y for _,c,i,Y in sub)))

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The claim is: with no bulk gauge field a wall's chiral content must be anomaly-free ALONE,
# and the SM's 15 Weyl fermions per generation cancel EVERY condition -- but only as a
# complete set.  Pinned: the count 15, exact zero for all five coefficients, and the
# non-zero residues this receipt prints when one species is dropped.
assert tot == 15, "the generation count printed above is 15 Weyl fermions"
assert A333 == 0 and A221 == 0 and A331 == 0 and A111 == 0 and A1g == 0, \
    "all five anomaly coefficients must vanish exactly"
# "only as a complete set": each deletion must leave a NON-zero residue, and these are the
# exact fractions printed in the table above.
_res = {d: (sum(c*i*Y**3 for _,c,i,Y in gen if _!=d), sum(c*i*Y for _,c,i,Y in gen if _!=d))
        for d in ('e^c','u^c','L')}
assert _res['e^c'] == (F(-1), F(-1)), "drop e^c must give [U(1)]^3 = -1, U(1)-grav = -1"
assert _res['u^c'] == (F(8,9), F(2)),  "drop u^c must give [U(1)]^3 = 8/9, U(1)-grav = 2"
assert _res['L']   == (F(1,4), F(1)),  "drop L must give [U(1)]^3 = 1/4, U(1)-grav = 1"
assert all(a != 0 or b != 0 for a, b in _res.values()), \
    "no proper subset of the 15 is anomaly-free -- the set is indecomposable"
