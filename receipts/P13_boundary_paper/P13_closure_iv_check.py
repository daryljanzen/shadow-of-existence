"""
P13_closure_iv_check.py -- verifies prop:closure(iv): R:r->-r is an INVOLUTION whose fixed set is exactly
  {r=0}, which IS the bead's branch point. Precise statement (correcting 'R carries one leg to the other'):
  R FIXES the locus r=0 the bead passes through; the bead's two halves sit in R-conjugate regions, and the
  collapse(cosh)/expansion(sinh) asymmetry (Nariai 1/3 vs 2/3) is the symmetry-breaking content, not a
  blemish. THE CONJUGATION'S FIXED POINT IS THE COSMOGENESIS'S BRANCH POINT. [P13 boundary_paper prop:closure]
STATUS: ✔✔   ORIGIN: storyboard_receipts/closure_iv_check.py, verified r1381.

ATTACKING prop:closure (iv), r1088. The place I said I'd go first.

MY CLAIM (iv): "R ... carries the bead's expansion leg onto its conjugate branch."
And the headline built on it: "The operation that conjugates the representation IS the
operation that runs the bead through its branch point."

THE WORRY: R is an INVOLUTION (a reflection, R^2 = 1). The bead's passage through r=0 is
a CONTINUATION (a path). A map is not a path. If (iv) conflates them, the closure's spine
is bent -- so ask the geometry, not the prose.
"""
import numpy as np

alpha, M2 = 1.0, 0.3849001794597505      # Nariai
A = (M2*alpha**2)**(1/3)

print("="*78)
print("(1)  The two legs of the bead, in cosmic time -- are they MIRRORS under r -> -r?")
print("="*78)
print("  From the bead's own arc-length reading (F_flat / P7 fig. panel F):")
print("     collapse  (s <= 0)      r = -A cosh^(2/3)(3s/2a)")
print("     the lift  (0..pi/3)     r = -A sin^(2/3)(3(pi/3 - s)/2a)")
print("     expansion (s >= pi/3)   r = +A sinh^(2/3)(3(s - pi/3)/2a)")
print()
print("  If the conjugate branch were the areal reflection r -> -r OF THE EXPANSION LEG")
print("  as a CURVE, then -expansion(x) would equal collapse(-x). Test it:")
print(f"  {'x':>6} {'+A sinh^2/3 (expansion)':>24} {'-A cosh^2/3 (collapse)':>24}   equal?")
for x in (0.3, 0.8, 1.5, 2.5):
    exp_r = A*np.sinh(1.5*x/alpha)**(2/3)
    col_r = -A*np.cosh(1.5*x/alpha)**(2/3)
    print(f"  {x:>6.2f} {-exp_r:>24.6f} {col_r:>24.6f}   {'YES' if abs(-exp_r-col_r)<1e-9 else 'NO'}")
print()
print("  >> NO. sinh != cosh. The legs are NOT mirror images.")
print("  >> AND P7'S OWN FIGURE CAPTION ALREADY SAYS SO, verbatim:")
print('       "The two legs are structurally distinct curves, a run and a lift against')
print('        a single real curve, NOT MIRRORS."')
print("  >> So r -> -r does NOT map the expansion leg onto the collapse leg. (iv), as I")
print("     wrote it, is FALSE -- and P7 contradicts it in its own caption.")

print()
print("="*78)
print("(2)  Then what IS the relation? Ask what R actually does to the bead.")
print("="*78)
print("  R : r -> -r. It is an INVOLUTION. Its fixed set is exactly {r = 0}.")
print(f"     R(r) = -r  =>  fixed iff r = -r  =>  r = 0.   fixed point: r = 0")
print()
print("  The bead's branch point -- where the slicing continues onto the conjugate")
print("  branch, and where species flips -- is r = 0 (P7, thm:bead).")
print()
print("  >> ** R'S FIXED POINT IS THE BEAD'S BRANCH POINT. **")
print("     Not 'R carries one leg to the other' -- R FIXES the locus the bead passes")
print("     THROUGH, and EXCHANGES THE TWO REGIONS the bead's halves occupy.")
print()
print("  Check the regions (not the curves):")
print(f"     expansion leg occupies r > 0 :  {A*np.sinh(1.5*0.8)**(2/3):+.4f}, {A*np.sinh(1.5*2.0)**(2/3):+.4f}  ...")
print(f"     conjugate branch occupies r < 0: {-A*np.cosh(1.5*0.8)**(2/3):+.4f}, {-A*np.cosh(1.5*2.0)**(2/3):+.4f}  ...")
print("     R maps the region r>0 onto the region r<0, bijectively.       YES")
print("     R maps the CURVE in r>0 onto the CURVE in r<0.                NO")
print()
print("  And species is sign(r) -- a REGION label, not a curve shape. So:")
print("     the two halves carry CONJUGATE SPECIES because they occupy R-conjugate")
print("     REGIONS -- which is true, and needs no mirror symmetry of the curves.")

print()
print("="*78)
print("(3)  Does this break the closure, or sharpen it?")
print("="*78)
print("  BROKEN, as written: 'R carries the expansion leg onto its conjugate branch' and")
print("  'the operation that conjugates the representation IS the operation that runs the")
print("  bead through its branch point'. R RUNS NOTHING. It is a reflection; the bead's")
print("  passage is a continuation. I wrote a map and a path as the same thing.")
print()
print("  SURVIVES, and it is the sharper statement:")
print("     ** THE BEAD'S BRANCH POINT IS THE CONJUGATION'S FIXED POINT. **")
print("     The bead passes THROUGH the one locus R fixes, and in doing so passes from")
print("     the region R labels 3 to the region R labels 3bar. The conjugation and the")
print("     cosmogenesis are not the same OPERATION -- they are CO-LOCATED: one map's")
print("     fixed point is the other's branch point, and that is why the bead's two")
print("     halves are species-conjugate.")
print()
print("  This is WEAKER than what I wrote and STRONGER than a rhyme, and it is what the")
print("  corpus actually licenses. It also explains the antimatter-progenitor theorem")
print("  correctly: not 'R maps our leg to the progenitor's', but 'the bead crosses R's")
print("  fixed point, so its two halves sit in R-conjugate regions'.")
print()
print("  AND IT SURVIVES THE 'NOT MIRRORS' FACT INTACT -- indeed it NEEDS it: if the legs")
print("  were mirrors, the bead would be R-symmetric and there would be no asymmetry to")
print("  break. The collapse leg (cosh) and the expansion leg (sinh) being structurally")
print("  DIFFERENT is exactly what makes the crossing an EVENT rather than a symmetry.")
print("  ** The asymmetry is not a blemish on the conjugation; it is its content. **")
print("  (Daryl, r1078: 'it is asymmetric -- Nariai, 1/3 vs 2/3. The asymmetry IS the")
print("   symmetry-breaking, not a footnote to it.')")

# r2376+c54.158 -- this receipt printed its table inside the print statements and kept nothing.
# The block below recomputes exactly what it prints and pins it.
#   (1) THE NEGATIVE (1) turns on -- the two legs are NOT mirrors under r -> -r.  At the four
#       tabulated x the expansion leg's -A sinh^{2/3} and the collapse leg's -A cosh^{2/3} are
#       different numbers: -0.436815 vs -0.776531 at x = 0.30, still -5.580487 vs -5.584603 at
#       x = 2.50.  The gap SHRINKS monotonically -- 0.3397, 0.1234, 0.0304, 0.0041 -- and never
#       reaches zero, so "sinh != cosh" is not a large-x artefact and cannot be tuned away.  Were
#       these equal the bead would be R-symmetric and (iv) would have no symmetry-breaking content.
#       The Nariai amplitude they are measured in is pinned with them: A = (2M a^2)^{1/3} =
#       0.7274157573.
#   (2) WHAT (iv) SURVIVES AS: R : r -> -r exchanges the two REGIONS, sign +1 for the expansion
#       leg and -1 for the collapse leg at every sampled point, while fixing r = 0 alone.
assert abs(A - 0.7274157573144809) < 1e-12, A
_tab = [(A*np.sinh(1.5*x/alpha)**(2/3), -A*np.cosh(1.5*x/alpha)**(2/3)) for x in (0.3, 0.8, 1.5, 2.5)]
assert abs(-_tab[0][0] - (-0.436815)) < 5e-7 and abs(_tab[0][1] - (-0.776531)) < 5e-7
assert abs(-_tab[3][0] - (-5.580487)) < 5e-7 and abs(_tab[3][1] - (-5.584603)) < 5e-7
_gap = [abs(-e - c) for e, c in _tab]
assert all(g > 0 for g in _gap) and _gap == sorted(_gap, reverse=True), _gap
assert abs(_gap[0] - 0.339716) < 5e-7 and abs(_gap[3] - 0.004117) < 5e-7, _gap
assert all(np.sign(e) == 1 and np.sign(c) == -1 for e, c in _tab)
assert [x for x in (-2.0, -0.5, 0.0, 0.5, 2.0) if -x == x] == [0.0]   # R's fixed set is {r=0}
