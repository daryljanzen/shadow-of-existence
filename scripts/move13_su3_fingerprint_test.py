# Move 13, first bite (c17): is the cubic's A_2 resonance the su(3) FINGERPRINT? (necessary, not sufficient)
# DO-NOT-ASSERT su(3). Manufactured-wall caution: the retracted rung-4 test checked su(3) c so(4,1)
# (wrong group, strawman). The CORRECT necessary condition is su(3) c (substrate COMPACT isometry).
# Built root data: Moves 6-7-11 (r210/r211/r214); algebroid_closure_consolidation.md sec 5,7.
import sympy as sp

print("=== 1. The cubic supplies the su(3) Cartan+Weyl skeleton (established, re-confirmed) ===")
r,al,M = sp.symbols('r alpha M', real=True, positive=True)
cubic = r**3 - al**2*r + 2*M*al**2
# coefficient of r^2 = 0  =>  sum of roots = 0  (a TRACELESS element = su(3) Cartan)
c2 = sp.Poly(cubic, r).coeff_monomial(r**2)
print(f"  SdS horizon cubic r^3 - a^2 r + 2 M a^2 : coeff of r^2 = {c2}  =>  roots sum to 0")
print("  3 roots summing to 0 = a Cartan (traceless-diagonal) element of su(3); S_3=Weyl(A_2) permutes them.")
print("  => the A_2 Cartan + Weyl SKELETON is geometrically present (the discrete shadow). [established]\n")

print("=== 2. The necessary condition for a CONTINUOUS su(3) isometry: su(3) c substrate compact isometry ===")
# su(3) irrep dims (Weyl dim formula): dim(p,q) = (p+1)(q+1)(p+q+2)/2
def su3dim(p,q): return (p+1)*(q+1)*(p+q+2)//2
irreps = {(p,q): su3dim(p,q) for p in range(3) for q in range(3)}
print("  su(3) irrep dims (p,q):", {k:v for k,v in sorted(irreps.items(), key=lambda x:x[1])})
# faithful real reps: (1,0)/(0,1) are the complex fundamental 3 -> real dim 6 (faithful);
# (1,1)=adjoint 8 is REAL but kernel = center Z_3 (NOT faithful). dim<=5 faithful real: NONE.
print("  fundamental (1,0)=3 is complex & faithful -> realification dim 6.  adjoint (1,1)=8 real but")
print("  kernel Z_3 (not faithful).  => SMALLEST FAITHFUL REAL rep of SU(3) has dim 6.")
print("  Hence SU(3) c SO(6) (acts on C^3=R^6 preserving the Hermitian form) and SU(3) NOT c SO(5)")
print("  (no faithful real rep of dim <=5).  [textbook floor; THE_PLAN: 'SU(3) c SO(6) is fact'].\n")

print("=== 3. The established substrate is dS_5; its compact isometry is SO(5) ===")
print("  Substrate dS_5 = SO(5,1)/SO(4,1); maximal compact (geometric/rotation) isometry = SO(5).")
print("  Test: su(3) c so(5)?  ->  NO (step 2: SU(3) needs >=6 real dims).")
print("  => on dS_5 the continuous su(3) is NOT realizable as a geometric isometry.\n")

print("=== 4. VERDICT (necessary-not-sufficient; do-not-assert held) ===")
print("  * The A_2 resonance IS the su(3) Cartan+Weyl skeleton (necessary piece) -- real, geometrically")
print("    grounded (the cubic's roots-sum-to-0 + S_3). NECESSARY condition: PRESENT.")
print("  * But on the established dS_5 substrate the SUFFICIENT step fails: su(3) NOT c so(5), so no")
print("    continuous su(3) geometric isometry exists there -- the skeleton is the DISCRETE Weyl(A_2)=S_3")
print("    SHADOW only.  => on dS_5: GRAVITY-MINIMAL (colour a shadow).")
print("  * A continuous su(3) (GAUGE-CAPABLE) requires the substrate to rise to dS_6/M^7 (SO(6) ⊃ SU(3)).")
print("    The resonance is NECESSARY-NOT-SUFFICIENT: it supplies the skeleton but does NOT FORCE the")
print("    dS_5->dS_6 rise. The dimensional horn stays OPEN, decided by INDEPENDENT grounds for dS_6,")
print("    NOT by the resonance. su(3) NOT asserted; and not refuted -- correctly located.")
