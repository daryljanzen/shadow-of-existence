"""The hinge span and the root span are orbits of ONE Z_3: the 120-degree rotation of the swing angle w.
r_k = (2/sqrt3) a sin(w_k),  2M = (2/3sqrt3) a sin(3w).  Check: same w-shift fixes M and permutes r."""
import numpy as np
al=1.0
r_of  = lambda w: (2/np.sqrt(3))*al*np.sin(w)
M2_of = lambda w: (2/(3*np.sqrt(3)))*al*np.sin(3*w)
for w in (0.3, 0.7, 1.1):
    ws=[w, w+2*np.pi/3, w+4*np.pi/3]
    rs=[r_of(x) for x in ws]; Ms=[M2_of(x) for x in ws]
    print("   w=%.2f : roots %s"%(w,'  '.join('%+.5f'%x for x in rs)))
    print("           2M    %s   -> all equal: %s"%('  '.join('%+.5f'%x for x in Ms), max(Ms)-min(Ms)<1e-12))
    print("           sum of roots %.1e (cubic has no r^2 term: %s)"%(sum(rs), abs(sum(rs))<1e-12))
print()
print("   => the SAME shift w -> w + 120deg fixes the mass and cyclically permutes the three roots.")
print("      The three hinges ARE the three 120deg-separated vantages (P3, sec:hinge-geometry).")
print("      So the hinge triple and the root triple are orbits of ONE Z_3 -- the swing.")
print()
print("   and the figure ties the scales: hinge circumradius 2a, throat = its INCIRCLE, radius a")
print("      (equilateral: circumradius = 2 x inradius, so 2a and a -- forced, not chosen)")
print("      root amplitude (2/sqrt3)a = %.5f, between the throat a and the hinge radius 2a"%(2/np.sqrt(3)))
