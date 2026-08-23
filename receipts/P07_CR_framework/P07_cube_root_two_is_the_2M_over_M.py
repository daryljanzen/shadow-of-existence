#!/usr/bin/env python3
"""P07_cube_root_two_is_the_2M_over_M -- the cube-root-two between the two turnings, derived.

THE UNDECIDED THIS CLOSES.  COMBINATORICS_LEDGER carried, as its one live UNDECIDED,
"A = cbrt(2) . rho ties the comoving turnaround's scale to a horizon root -- well-posed,
unattempted", with both cheap answers forbidden: the credulous one ("the cbrt2 ties the two
turnings") and the sceptical one ("lem:twoturnings killed it", which is false -- that lemma
denies an identification of the two Z3 SYMMETRIES and says nothing about a ratio of radii).

WHAT IS ASSERTED.  The ratio is exact, it holds for every M and alpha, its cause is one
factor of two inside one cube root, and its tie to a HORIZON ROOT is particular to the
Nariai member.  So the relation is real and shallow -- neither cheap answer.

FAILURE PATH.  Any of the four assertions failing exits 1.
"""
import sys
from sympy import symbols, solve, simplify, sqrt, Rational, diff, Symbol

M = Symbol('M', positive=True)
a = Symbol('alpha', positive=True)
r = Symbol('r')
f = 1 - 2*M/r - r**2/a**2

bad = 0

# 1. the comoving turnaround is 1-f=0, i.e. r^3 = -2 M alpha^2
ta_cubic = simplify((1 - f) * r)                     # 2M + r^3/alpha^2
TA = (2*M*a**2)**Rational(1, 3)
ok1 = simplify((2*M/(-TA) + TA**2/a**2)) == 0
print(f"  1. turnaround at |r| = (2M alpha^2)^(1/3), from 1-f=0        : {'OK' if ok1 else 'FAIL'}")
bad |= (not ok1)

# 2. the Hubble-Eddington / static radius is f'=0, i.e. r^3 = M alpha^2
HE = solve(diff(f, r), r)[0]
ok2 = simplify(HE - (M*a**2)**Rational(1, 3)) == 0
print(f"  2. static radius r_HE = (M alpha^2)^(1/3), from f'=0         : {'OK' if ok2 else 'FAIL'}")
bad |= (not ok2)

# 3. the ratio is exactly cbrt(2), for every M and alpha
ratio = simplify(TA/HE)
ok3 = simplify(ratio - 2**Rational(1, 3)) == 0
print(f"  3. TA / r_HE = {ratio}  -- exact, M- and alpha-free       : {'OK' if ok3 else 'FAIL'}")
bad |= (not ok3)

# 4. only at Nariai is the f'=0 locus ALSO a root of f
Mn = a/(3*sqrt(3))
ok4a = simplify(f.subs({M: Mn, r: HE.subs(M, Mn)})) == 0
generic = simplify(f.subs(r, HE))                     # f at r_HE for general M
ok4b = simplify(generic.subs(M, Mn)) == 0 and simplify(generic) != 0
print(f"  4. at Nariai r_HE is a root of f (the double root)           : {'OK' if ok4a else 'FAIL'}")
print(f"     and NOT a root of f on a generic member                   : {'OK' if ok4b else 'FAIL'}")
bad |= (not (ok4a and ok4b))

print()
print("  ** THE VERDICT, and it is neither cheap answer. **")
print("     The relation is REAL: A / r_HE = 2^(1/3) exactly, for every M and alpha.")
print("     Its CAUSE is shallow: 1-f=0 carries 2M/r while f'=0 balances 2M/r^2 against")
print("     2r/alpha^2, so the conditions differ by one factor of two -- and one factor of")
print("     two inside one cube root IS the cube root of two.  Nothing deeper is present.")
print("     Its tie to a HORIZON ROOT is Nariai-only: f and f' vanish together at the double")
print("     root, so only there is the f'=0 locus a root of f.  Off the forced member the")
print("     ratio is unchanged and the quantity tied to is the static radius, not a horizon.")
print("  ** lem:twoturnings is untouched: it denies an identification of the two Z3")
print("     SYMMETRIES; this is a ratio of two radii, a different object. **")
sys.exit(1 if bad else 0)
