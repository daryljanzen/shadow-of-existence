"""Given su(3)xsu(2)xu(1) and one generation's MULTIPLET STRUCTURE (Q,u^c,d^c,L,e^c),
do the anomaly conditions DETERMINE the hypercharges?  Solve for them rather than assuming."""
import sympy as sp
q,u,d,l,e = sp.symbols('q u d l e', rational=True)
# [SU(3)]^2 U(1):  2q - u - d = 0      (Q is an isodoublet -> weight 2; u^c,d^c singlets)
A1 = 2*q - u - d
# [SU(2)]^2 U(1):  3q + l = 0          (colour 3 for Q, 1 for L)
A2 = 3*q + l
# [U(1)]^3     :  6q^3 - 3u^3 - 3d^3 + 2l^3 - e^3 = 0   (with c^c conjugates entering with -Y)
A3 = 6*q**3 + 3*(-u)**3 + 3*(-d)**3 + 2*l**3 + (-e)**3
# U(1)-grav    :  6q - 3u - 3d + 2l - e = 0
A4 = 6*q + 3*(-u) + 3*(-d) + 2*l + (-e)
# Yukawa terms must exist:  Q u^c H, Q d^c H, L e^c H  with one Higgs of hypercharge h
h = sp.symbols('h', rational=True)
Y1 = q - u + h      # Q u^c H~   (conventions absorbed into signs of u,d,e as conjugates)
Y2 = q - d - h
Y3 = l - e - h
sol = sp.solve([A1,A2,A4,Y1,Y2,Y3], [u,d,l,e,h], dict=True)
print("   solving the LINEAR conditions ([SU3]^2U1, [SU2]^2U1, U1-grav, three Yukawas):")
for s in sol:
    print("     ", {str(k):v for k,v in s.items()}, " in terms of q")
    sub={**s}
    print("      check [U(1)]^3 :", sp.simplify(A3.subs(sub)))
print()
print("   with q = 1/6 (the conventional normalisation):")
for s in sol:
    sub={k:v.subs(q,sp.Rational(1,6)) for k,v in s.items()}
    print("      Q=%s  u^c=%s  d^c=%s  L=%s  e^c=%s"%(sp.Rational(1,6),-sub[u],-sub[d],sub[l],-sub[e]))

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# THE CLAIM: the anomaly conditions plus the three Yukawas DETERMINE the hypercharges, up to
# the single overall normalisation q.  So exactly ONE solution, and it is the printed one.
assert len(sol)==1, len(sol)
_s = sol[0]
assert sp.simplify(_s[u] - 4*q)==0 and sp.simplify(_s[d] + 2*q)==0
assert sp.simplify(_s[l] + 3*q)==0 and sp.simplify(_s[e] + 6*q)==0
assert sp.simplify(_s[h] - 3*q)==0
# AND THE PART THAT MAKES IT A DERIVATION RATHER THAN A SUBSTITUTION: the CUBIC anomaly
# [U(1)]^3 was NOT among the equations solved -- only the linear ones and the Yukawas were --
# and it vanishes identically on the solution.  Fires if any coefficient of A3 is perturbed.
assert sp.simplify(A3.subs(_s))==0, sp.simplify(A3.subs(_s))
# and the printed q=1/6 column IS the Standard Model's hypercharge assignment.
_at = {k: v.subs(q, sp.Rational(1,6)) for k,v in _s.items()}
assert (-_at[u], -_at[d], _at[l], -_at[e]) == (sp.Rational(-2,3), sp.Rational(1,3),
                                               sp.Rational(-1,2), sp.Integer(1)), _at
