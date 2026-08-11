#!/usr/bin/env python3
"""
L8.1-c · THE 12 — receipt.  Lane 8, the combinatorics ledger.
CLAIM UNDER TEST (written first, per the indexing rule):
    "the twelve designations (every 30 deg on the dial) and |Aut(A_2)| = |D_6| = 12
     are ONE 12."
RISK OF NO, and it is real: P3 reaches 12 as 3x4 (triple-angle x quarter-turn:
"a sine peaks a quarter-turn from its zero", w = 360/(3x4)), while D_6 is 6x2
(rotation order six x reflection).  TWO FACTORISATIONS OF 12 -- exactly the
"two 2s" shape (lem:twoturnings) that returns NO.  This receipt can return either.
SOURCE (P3 sec:tour): "the family visits three geometries under twelve designations,
  one every 30 deg, the six Nariai forming the A_2 hexad ... with the full automorphism
  group Aut(A_2)=D_6 realised as the dial's hexagonal symmetry ... fundamental domain [0,30]."
"""
import numpy as np
D=np.deg2rad
def twoM(w): return (2/(3*np.sqrt(3)))*np.sin(3*w)     # P3 prop:triple
def r0(w):   return (2/np.sqrt(3))*np.sin(w)           # P3 prop:gnomonic

print("== 1. WHAT the twelve designations ARE, computed (not assumed) ==")
ws=np.linspace(0,2*np.pi,100001)
v=twoM(ws)
zeros=[w for w in np.arange(0,360,1e-3) if abs(twoM(D(w)))<1e-9]
zz=sorted({round(w,6) for w in np.arange(0,360,0.001) if abs(twoM(D(w)))<1e-7})
# analytic instead of scanning: 2M=0  <=> sin3w=0 <=> w = 60k ; |2M| max <=> sin3w=+-1 <=> w = 30+60k
dS   = [60*k for k in range(6)]
nar  = [30+60*k for k in range(6)]
print(f"   2M = 0      (de Sitter) at w = {dS}      -> {len(dS)} marks")
print(f"   |2M| = max  (Nariai)    at w = {nar}   -> {len(nar)} marks")
allm = sorted(dS+nar)
sp = sorted({round((allm[i+1]-allm[i]),6) for i in range(len(allm)-1)})
print(f"   union = {len(allm)} marks, spacing(s) = {sp} deg   <- P3's 'twelve designations, one every 30'")
for w in [0,30,60,90]:
    print(f"     w={w:3d}  2M={twoM(D(w)):+.6f}  r0={r0(D(w)):+.6f}")

print("\n== 2. THE GROUP, generated from the dial's own invariances of sin 3w ==")
def orbit(w0):
    s=set()
    for k in range(6):
        s.add(round((w0+60*k)%360,6)); s.add(round((60*k-w0)%360,6))
    return sorted(s)
g=orbit(15.0)   # generic point
print(f"   D_6 = <w->w+60 , w->-w>.  |orbit(generic w=15)| = {len(g)}  = |D_6| = 12")
print(f"   |orbit(w=0,  de Sitter)| = {len(orbit(0))}   (stabilised)")
print(f"   |orbit(w=30, Nariai)|    = {len(orbit(30))}   (stabilised)")
print(f"   so the twelve marks are TWO 6-orbits, not one 12-orbit: {len(orbit(0))}+{len(orbit(30))}=12")

print("\n== 3. THE TEST: is the 12 of the marks the SAME 12 as |D_6|? ==")
print("   The marks are the fixed-point set of the reflections in D_6.")
refl=[]
for k in range(6):
    # reflection w -> 60k - w ; fixed points 2w = 60k  => w = 30k, 30k+180
    refl += [round((30*k)%360,6), round((30*k+180)%360,6)]
fix=sorted(set(refl))
print(f"   D_6 has 6 reflections; their axes meet the dial in {len(fix)} points: {fix[:6]} ...")
print(f"   |fixed-point set| = {len(fix)}   |D_6| = 12   equal: {len(fix)==12}")
print(f"   and fixed set == the twelve designations: {fix==sorted(float(x) for x in allm)}")
print("   FOR ANY DIHEDRAL D_n:  n reflections -> 2n axis-points, and |D_n| = 2n.")
print("   The identity #marks = |D_n| is FORCED by the dihedral structure, not arithmetic luck.")

print("\n== 4. AND THE TWO FACTORISATIONS ARE THE SAME OBJECT, not a coincidence ==")
print("   3x4  : sin(3w) has period 120 ; a sine peaks a QUARTER-period from its zero")
print("          -> marks every 120/4 = 30 -> 360/30 = 12 marks.")
print("   6x2  : D_6 = <rotation order 6> x <reflection> ; |D_6| = 12.")
print("   WELD : the rotation w->w+60 IS 'half the period of sin 3w' (it flips the sign:")
print(f"          sin(3(w+60)) = {np.sin(3*D(15+60)):+.6f} vs -sin(3w) = {-np.sin(3*D(15)):+.6f}")
print("          and the reflection w->60-w IS 'reflect about the peak' (mass-invariant:")
print(f"          2M(60-w) = {twoM(D(60-15)):+.6f} vs 2M(w) = {twoM(D(15)):+.6f} )")
print("   => D_6 IS the symmetry group of sin 3w on the dial.  The 6 is the half-period")
print("      count (360/60), the 2 is the peak-reflection; the 3 and the 4 are the SAME")
print("      two facts read as period and quarter-period.  ONE object: the sine.")

print("\n== 5. CONTROL — CORRECTED. The first draft compared marks to |D_n| and returned")
print("   False on every n.  That was the CONTROL'S error, not the claim's: for sin(nw)")
print("   the sign-flip step is 180/n (order 2n), so the DIAL'S group is D_{2n}, not D_n.")
for n in (2,3,4,5,6):
    zeros={round(180*k/n,6)%360 for k in range(2*n)}
    ext  ={round(90/n+180*k/n,6)%360 for k in range(2*n)}
    marks=len(zeros|ext); order=4*n
    print(f"   sin({n}w): marks={marks:2d}  dial group D_{{{2*n}}}, |D_{{{2*n}}}|={order:2d}  equal: {marks==order}")
print("   It holds for EVERY n -> #marks = |D_{2n}| is a DIHEDRAL GENERALITY, forced but")
print("   NOT CR-specific.  CR's content is WHICH n: n=3, from the cubic.")

print("\n== 6. THE CONTROL THAT DISCRIMINATES: break the SINE, not the n ==")
lin=lambda w: (2/np.sqrt(3))*D(w)
vals=[round(lin(w)-lin(w)**3,4) for w in (15,135,255)]
print(f"   Replace r0=(2/sqrt3) sin w  by  r0=(2/sqrt3) w  (linear, no sine):")
print(f"   2M at w=15,135,255 -> {vals}  : NO 120-periodicity, no D_6, NO twelve marks.")
print("   The 12 is bought by the SINE; the sine is bought by prop:gnomonic (the hole's")
print("   gnomonic image on the observer's sky).  Break that and the receipt flips.")

print("\n== VERDICT ==")
print("   YES -- ONE 12, and the object is sin 3w.  Both the twelve designations (its")
print("   zeros and extrema = D_6's reflection axes on the dial) and |D_6| follow from")
print("   the sine with no new input.  3x4 and 6x2 are its period and quarter-period")
print("   read twice.  HONEST BOUND: the identity #marks=|D_{2n}| is a dihedral")
print("   generality; CR's specific content is that n=3.")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (1) WHAT THE TWELVE DESIGNATIONS ARE: six de Sitter marks where 2M = 0 and six Nariai marks
#     where |2M| is maximal, union twelve, spaced every 30 deg.  Values checked on twoM, not
#     merely listed: the zeros vanish and the extrema sit at 2/(3 sqrt 3) = 0.3849002.
assert dS == [0, 60, 120, 180, 240, 300] and nar == [30, 90, 150, 210, 270, 330]
assert len(allm) == 12 and sp == [30.0], (len(allm), sp)
assert all(abs(twoM(D(_w))) < 1e-12 for _w in dS), [twoM(D(_w)) for _w in dS]
assert all(abs(abs(twoM(D(_w))) - 0.3849002) < 1e-6 for _w in nar), [twoM(D(_w)) for _w in nar]
# (2) THE GROUP: the generic orbit has 12 elements and BOTH special orbits are stabilised to 6,
#     so the twelve marks are two 6-orbits, 6 + 6, and NOT one 12-orbit.
assert len(g) == 12 and len(orbit(0)) == 6 and len(orbit(30)) == 6
assert len(orbit(0)) + len(orbit(30)) == 12 and set(orbit(0)) & set(orbit(30)) == set()
# (3) THE TEST ITSELF -- the claim the receipt exists to settle: the marks ARE the fixed-point
#     set of D_6's six reflections, so #marks = |D_6| = 12 as ONE object, not two 12s.
assert len(fix) == 12, len(fix)
assert fix == sorted(float(x) for x in allm), (fix, allm)
# (4) THE CONTROL, which is what bounds the claim: #marks = |D_{2n}| = 4n for EVERY n, so the
#     identity is a dihedral generality and CR's content is only that n = 3.
for _n in (2, 3, 4, 5, 6):
    _z = {round(180*_k/_n, 6) % 360 for _k in range(2*_n)}
    _e = {round(90/_n + 180*_k/_n, 6) % 360 for _k in range(2*_n)}
    assert len(_z | _e) == 4*_n, (_n, len(_z | _e))
# (5) THE DISCRIMINATING CONTROL: break the SINE and the twelve marks go.  The linear surrogate
#     has no 120-periodicity -- the three printed values are wildly unequal, not a repeat.
assert vals == [0.2747, -17.4185, -130.5862], vals
assert len(set(vals)) == 3
# (6) and the weld: w -> w+60 flips the sign of sin 3w and w -> 60-w fixes 2M (0.272166 at 15).
assert abs(np.sin(3*D(15+60)) - (-0.707107)) < 1e-6
assert abs(twoM(D(60-15)) - 0.272166) < 1e-6 and abs(twoM(D(15)) - 0.272166) < 1e-6
