import numpy as np
# The claim to TEST (carefully, as material, not to assert a closure):
# Rem A: three horizon roots are preimages of 3w under sine: w, w+120, w+240.
#        cross-ratio of the three with the centre = e^{i pi/3} (equianharmonic, j=0).
# Rem B (sec:deck): the cover that carries the deck S_3 is 3-sheeted over the 2M-plane,
#        branched at the two Nariai values 2M = ±2/(3 sqrt3) (alpha=1).
# Paper: "different degree over a different base with a different branch set" -> not shown one.
#
# I am NOT trying to show they ARE one (that would be exactly the resonance-forcing error).
# I want to see PRECISELY what is independent and what is shared, as sharpening material.

print("="*70)
print("(1) The two covers, stated as maps, over what base, branched where")
print("="*70)
print("""  COVER-A (equianharmonic / j=0), Rem A's object:
     the map is  s = sin(3w)  from the w-line to the s-line (sky observable).
     degree 3 (three w per s), branch where d/dw sin3w = 0 i.e. 3cos3w=0
       -> 3w = pi/2 mod pi -> the turning values s = sin(3w) = +-1.
     So COVER-A: 3-sheeted, base = s=sin3w line, branch points s = +-1.

  COVER-B (deck), sec:deck's object:
     3-sheeted over the 2M-plane, branched at the two Nariai 2M = +- 2/(3 sqrt3).
     roots r of r^3 - r + 2M = 0 ; branch where discriminant vanishes.
""")
# Check: is the s=+-1 branch of cover A the SAME event as the 2M=Nariai branch of cover B?
# horizon cubic (alpha=1): f=1-2M/r-r^2=0 -> r^3 - r + 2M = 0  (multiply by -r, sign conv)
# Actually f=0: 1 - 2M/r - r^2 = 0 -> r - 2M - r^3 = 0 -> r^3 - r + 2M = 0. Good.
# Nariai = double root: discriminant of r^3 + p r + q, p=-1, q=2M: Delta = -4p^3-27q^2 = 4-27(2M)^2=0
Mn = np.sqrt(4/27)/2
print(f"  Nariai 2M (double root of cubic): 2M = ±{2*Mn:.6f} = ±2/(3√3) = ±{2/(3*np.sqrt(3)):.6f}  [check]")

print("="*70)
print("(2) THE SHARED DIAL: both are really about the SAME w, via P3's sin(3w).")
print("="*70)
print("""  P3 forces the three roots to be r_k = (2/sqrt3) sin(w + 120k)  [the triple-angle sol].
  The cubic's control parameter and the sky angle are ONE dial: 2M and w are tied by
     2M = (the product/elementary-symmetric data of the three sines) = a function of 3w.
  Let me verify 2M is a function of 3w alone (so the 2M-plane base and the s=sin3w base
  are the SAME base up to the map), which is the concrete bridge the two remarks leave implicit.""")
# r_k = (2/sqrt3) sin(w+120k). Product r0 r1 r2 = ?  For r^3 - r + 2M=0, product of roots = -2M.
for w in np.linspace(0.05, np.pi/3-0.05, 6):
    r = (2/np.sqrt(3))*np.sin(w + np.deg2rad(120)*np.arange(3))
    prod = np.prod(r); s = np.sum(r); s2 = r[0]*r[1]+r[1]*r[2]+r[0]*r[2]
    twoM = -prod
    # is 2M a clean function of sin(3w)? triple angle: sin3w = 3 sinw -4 sin^3 w
    # claim from P3: 2M = (2/(3sqrt3)) sin(3w)?
    pred = (2/(3*np.sqrt(3)))*np.sin(3*w)
    print(f"  w={w:5.3f}: sum={s:+.2e} sum2={s2:+.3f} 2M=-prod={twoM:+.6f}  (2/(3√3))sin3w={pred:+.6f}  match={np.isclose(twoM,pred)}")
print("""
  If 2M = (2/(3√3)) sin(3w) holds, then:
   - the 2M-plane (cover B's base) and the s=sin3w line (cover A's base) are the SAME base,
     related by the constant 2/(3√3);
   - cover B's branch 2M=±2/(3√3) is exactly cover A's branch s=±1  (sin3w=±1) -- SAME branch set;
   - both are degree 3 over that one base.
  => The 'different base / different branch set' in the remark is a DESCRIPTION difference
     (2M vs sin3w), not a structural one: they are the same 3-sheeted cover of the sky dial.
  What stays genuinely open (and the remark is right to hold) is the SECOND cover it names:
     the j=0 elliptic DOUBLE cover branched at FOUR points (the three roots + centre),
     which is a different object (degree 2, four branch points) and is where CM by omega lives.
  So there are really THREE things, not two, and separating them is the sharpening:
     (A1) the 3-sheeted sky cover  =  (B) the 3-sheeted 2M cover     [SAME, once 2M=(2/3√3)sin3w]
     (A2) the 2-sheeted j=0 elliptic cover branched at 4 points      [genuinely different; CM lives here]
  The remark conflates A1 and A2 under 'the equianharmonic cover' and then compares A2 to B.""")
