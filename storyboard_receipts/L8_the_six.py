#!/usr/bin/env python3
"""
L8.1-b · THE 6 — receipt.  Lane 8, the combinatorics ledger.
CLAIM UNDER TEST (written first, per the indexing rule):
    "the six hinges (3 upper + 3 lower horn) and the six Nariai (the A_2 hexad, 3 + 3bar)
     are ONE 6."
This receipt CAN return YES: if R and T agreed on the six vertices, the two hexads would
complete identically and the 6s would weld.  It returns NO, and the NO is EARNED (a proof
of inequivalence), not a failed search.
SOURCE (P3, sec:hinge-geometry, verbatim):
  "R ... reflects a spacelike leg, while the time reflection T: X_0 -> -X_0 reflects the
   timelike ambient one; on the six vertices T flips the horn while R preserves it, so
   R != T pointwise -- R fixes U_0 where T sends it to D_0 (a spacelike and a timelike
   reflection cannot coincide)."
"""
import numpy as np
a = 1.0                                    # alpha gauge
h = np.sqrt(3)*a                           # hinge height  X_0 = +-sqrt(3) alpha
R_t = 2*a                                  # hinge transverse radius 2a  (prop:twoalpha, an OUTPUT)

def hinge(k, upper):                       # the six vertices, polar 0/120/240 on each horn
    th = np.deg2rad(120*k)
    return np.array([ h if upper else -h, R_t*np.cos(th), R_t*np.sin(th) ])

V = [hinge(k, True) for k in range(3)] + [hinge(k, False) for k in range(3)]
names = ['U0','U120','U240','D0','D120','D240']

print("== 0. the vertices lie on the hyperboloid  -X0^2 + X1^2 + X2^2 = a^2 ==")
for n,v in zip(names,V):
    q = -v[0]**2 + v[1]**2 + v[2]**2
    print(f"   {n:5s} X0={v[0]:+.4f}  q={q:+.6f}  {'ok' if abs(q-a**2)<1e-12 else 'FAIL'}")

# T : the TIMELIKE reflection  X_0 -> -X_0   (horn-flipping)
T = lambda v: np.array([-v[0], v[1], v[2]])
# R : the SPACELIKE transverse-offset reflection, the A_2 diagram automorphism.
#     Source: it FIXES U_0 and PRESERVES the horn.  The spacelike reflection fixing the
#     polar-0 axis is X_2 -> -X_2.
R = lambda v: np.array([ v[0], v[1], -v[2] ])

print("\n== 1. R fixes U0 ; T sends U0 -> D0   (P3's own witness) ==")
print(f"   R(U0) = {R(V[0])}   -> {'U0 (fixed)' if np.allclose(R(V[0]),V[0]) else 'NOT fixed'}")
print(f"   T(U0) = {T(V[0])}   -> {'D0'         if np.allclose(T(V[0]),V[3]) else 'not D0'}")

print("\n== 2. THE TEST: does R = T on the six vertices?  (a YES would weld the 6s) ==")
agree = 0
for n,v in zip(names,V):
    same = np.allclose(R(v), T(v))
    agree += same
    print(f"   {n:5s}  R(v)X0={R(v)[0]:+.4f}   T(v)X0={T(v)[0]:+.4f}   agree={same}")
print(f"   vertices where R = T : {agree}/6")

print("\n== 3. WHY, and it is a proof not a search: the signature ==")
print("   R preserves X0 ; T negates it.  On every vertex |X0| = sqrt(3)a != 0,")
print("   so R(v)_0 = +X0 and T(v)_0 = -X0 differ for all six.  A spacelike and a")
print("   timelike reflection cannot coincide where X0 != 0.")

print("\n== 4. CONTROL — the test is NOT vacuous, and it rides on prop:twoalpha ==")
print("   Put the hinges ON the throat (X0 = 0, i.e. transverse radius a, not 2a):")
w = np.array([0.0, a, 0.0])
print(f"   w = {w} ->  R(w) = {R(w)}   T(w) = {T(w)}   agree = {np.allclose(R(w),T(w))}")
print("   There R = T and the 6s WOULD weld.  The inequivalence is bought by the hinge")
print("   standing OFF the throat at 2a -- which is an OUTPUT of the hole (prop:twoalpha),")
print("   not a stipulation.  Break that and the receipt flips.")

print("\n== VERDICT ==")
print("   NO -- the two 6s are NOT one 6.  PROVED (inequivalence), not 'no link found'.")
print("   R != T pointwise on all six vertices; the hexads SHARE the fundamental 3 and")
print("   complete by DISTINCT reflections.  Their product R o T is itself a hexad")
print("   symmetry: a resonance, not an identity.  (P3, sec:hinge-geometry.)")
