import numpy as np
print("="*70); print("(6) THE su(3)/A2 READING — turnaround = canonical fundamental-weight triangle"); print("="*70)
# both cubics are zero-sum (no r^2 term) -> both are A2 weight triples (sum=0)
# turnaround r^3 = -2M : the three cube roots. fundamental 3 of su(3) has weights on an
# equilateral triangle centred at 0. check the turnaround roots ARE that equilateral triangle,
# and that +M vs -M (mass reflection R) gives 3 vs 3bar (rotated by 60deg / conjugated).
for lbl,twoM in [("+M (fundamental 3)", +2/(3*np.sqrt(3))), ("-M (antifund. 3bar)", -2/(3*np.sqrt(3)))]:
    roots = np.roots([1,0,0,twoM])   # r^3 + 2M = 0
    ang = np.sort(np.round(np.angle(roots,deg=True),3))
    mods = np.round(np.abs(roots),4)
    print(f"  {lbl}: |roots|={set(mods)}  angles(deg)={list(ang)}")
    # equilateral test: all equal modulus, 120deg apart
    print(f"     equal-modulus: {np.allclose(mods,mods[0])} ; 120deg-spaced: {np.allclose(np.diff(ang),120,atol=1e-6)}")
print("  -> +M and -M turnaround triangles are the SAME equilateral triangle rotated 60deg")
print("     (r -> -r, the mass-reflection parity R) = the 3 <-> 3bar of su(3). The turnaround")
print("     cubic realises the fundamental/antifundamental weight triangles DIRECTLY in the r-plane.")
print()
# horizon roots for the SAME +M : colinear-real (the same A2 weights, broken to the real axis)
twoM=2/(3*np.sqrt(3)); hroots=np.roots([1,0,-1,twoM])
print(f"  horizon roots (+M, r^3-r+2M): {np.round(np.sort(hroots.real),4)}  (all real, sum={hroots.sum().real:.1e})")
print(f"  turnaround roots (+M) real parts: {np.round(np.sort(np.roots([1,0,0,twoM]).real),4)}  (sum={np.roots([1,0,0,twoM]).sum().real:.1e})")
print("  => BOTH zero-sum A2 triples. Horizon = REAL/colinear leg (casus irreducibilis, the physical")
print("     horizons, S3-permuted); turnaround = COMPLEX/equilateral leg (the canonical su(3) 3-triangle).")
print("     Related by the -alpha^2 r flat term: it is the 'breaking' that projects the equilateral 3")
print("     onto the real axis as the physical horizon triple. THE REAL AND COMPLEX LEGS, one A2.")

print("="*70); print("(7) THE TURNAROUND CURVE vs THE ELLIPSE in the (r0,r) plane"); print("="*70)
r0 = np.linspace(-1.3,1.3,20)
rTA = np.cbrt(r0**3 - r0)
# fundamental ellipse r^2 + r r0 + r0^2 = 1 : its r-extent at each r0
disc = 1 - 0.75*r0**2
print("  turnaround curve r_TA(r0)=cbrt(r0^3-r0): odd, zeros r0=0,+-1, extrema r0=+-1/sqrt3.")
print("  r0=+-1 (2M=0, de Sitter/massless): r_TA=0 = the ellipse's own r0=+-1 crossing (both at origin-line).")
print("  the curve is INSIDE the ellipse's r-band |r|<~1 for |r0|<1, touching r=0 exactly where the")
print("  ellipse meets the r0-axis (r0=+-1). A distinct cubic-root curve threaded through the ellipse's")
print("  axis-crossings, extremal at the Nariai slicing. (Full tangency/inscription: plot below.)")

# save a figure
import matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
r0f=np.linspace(-1.25,1.25,400)
fig,ax=plt.subplots(figsize=(6,6))
th=np.linspace(0,2*np.pi,400)
# ellipse r^2+r r0+r0^2=1 param: solve for r vs r0
r0g=np.linspace(-2/np.sqrt(3),2/np.sqrt(3),400)
rp=(-r0g+np.sqrt(np.clip(4-3*r0g**2,0,None)))/2; rm=(-r0g-np.sqrt(np.clip(4-3*r0g**2,0,None)))/2
ax.plot(r0g,rp,'b-',lw=1.2,label='fundamental ellipse (horizon roots)')
ax.plot(r0g,rm,'b-',lw=1.2)
ax.plot(r0f,r0f,'g--',lw=1,label='designated root r=r0 (line)')
ax.plot(r0f,np.cbrt(r0f**3-r0f),'r-',lw=1.8,label='turnaround r_TA(r0)=cbrt(r0^3-r0)')
for x in [1/np.sqrt(3),-1/np.sqrt(3)]: ax.axvline(x,color='0.8',lw=0.7)
ax.axhline(0,color='k',lw=0.5); ax.axvline(0,color='k',lw=0.5)
ax.set_xlabel('r0 (slicing offset)'); ax.set_ylabel('r'); ax.legend(fontsize=8); ax.set_title('Turnaround curve vs fundamental ellipse')
ax.set_aspect('equal'); plt.tight_layout(); plt.savefig('/home/claude/cr/work/turnaround_ellipse.png',dpi=110)
print("  [figure saved: turnaround_ellipse.png]")
