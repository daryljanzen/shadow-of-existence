"""M1 — WHAT DOES 'MEASURE-COLLAPSE' ACTUALLY MEASURE?
Section 0 uses it as the discriminator for the FINITE-CURVATURE species: the wall is
'metric NON-DEGENERATE (det g = -1, no measure-collapse -> not the finite-curvature species)'.
P1 states the same species INVARIANTLY, in separations: 'a null hypersurface along whose generators
THE SPATIAL EXTENT HAS, IN ADDITION, CONTRACTED TO ZERO'.
ARE THESE THE SAME CONDITION?  Compute."""
import sympy as sp
r,th,M=sp.symbols('r theta M', positive=True)
print("="*80); print("M1 — det g AT THE HORIZON"); print("="*80)
f=1-2*M/r
g=sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
d=sp.simplify(g.det())
print(f"\n  Schwarzschild, standard coordinates:  det g = {d}")
print(f"  at the horizon r = 2M:  det g = {sp.simplify(d.subs(r,2*M))}")
print("  *** NOT ZERO.  The 4-volume element does NOT collapse at the horizon, even in the chart")
print("      where g_tt vanishes -- because g_rr blows up and the product is finite: g_tt g_rr = -1. ***")
print(f"    check: g_tt . g_rr = {sp.simplify(g[0,0]*g[1,1])}  for every r")
print("""
  SO THE TWO CONDITIONS ARE NOT THE SAME:
    * 'det g = 0' is FALSE at the horizon, in this chart and in Kruskal alike.
    * P1's criterion IS satisfied there: horizon-crossing events on a common generator occur at the
      SAME AREAL RADIUS r_h, so their spatial separation vanishes, and the theorem forces the
      temporal one to vanish too.
  *** THEREFORE 'measure-collapse' CANNOT MEAN 'the 4-volume element degenerates'. ***
""")
print("  WHAT IT DOES MEAN, read off P1's own sentence:")
print("    every null hypersurface has a degenerate INDUCED metric -- that is what null means, and")
print("    it does not distinguish a horizon from an ordinary light cone.")
print("    P1's word is 'IN ADDITION': the SPATIAL EXTENT ALONG THE GENERATORS contracts to zero.")
print("    On a light cone, events on one generator sit at DIFFERENT radii -- extent nonzero.")
print("    On the horizon, they sit at the SAME r_h -- extent zero.")
print("  *** SO THE COLLAPSE IS OF THE TRANSVERSE EXTENT ALONG A GENERATOR, NOT OF THE 4-VOLUME. ***")
print()
print("  AND THE WALL'S EXCLUSION SURVIVES EITHER WAY, which is why nothing downstream is wrong:")
u,v,x,y,H=sp.symbols('u v x y H')
gb=sp.Matrix([[H,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
print(f"    Brinkmann ds^2 = 2 du dv + H du^2 + dx^2 + dy^2 :  det g = {sp.simplify(gb.det())}")
print("    a plane-fronted wave's generators carry CONSTANT transverse extent (dx^2 + dy^2 is flat")
print("    and u-independent), so the extent does not contract either.  The wall is excluded by the")
print("    invariant criterion as well as by the determinant, and prop:wall is untouched.")
print("="*80)
print("RESULT M1: section 0's shorthand 'det g = -1, no measure-collapse' is SOUND AS A CHECK ON THE")
print("  WALL -- a non-degenerate determinant does rule out a collapse -- but it is NOT the definition")
print("  of the species, and read as one it would exclude the event horizon, which is the corpus's")
print("  own flagship instance.  *** THE DEFINITION IS P1's, AND IT IS ABOUT SEPARATIONS ALONG A")
print("  GENERATOR.  Sharpen the shorthand so it cannot be read as the criterion. ***")
print("="*80)
