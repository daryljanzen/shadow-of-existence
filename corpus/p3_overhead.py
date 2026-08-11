"""P3 overhead — the hinge triangle, its tangent null rulings, and the hinge-to-pole lines.

GEOMETRY (all computed, all exact):
  equator            : unit circle, radius alpha
  hinges             : radius 2 alpha, azimuth 0 / 120 / 240  -- an equilateral triangle
  the triangle's sides are TANGENT to the equator, and each tangent point IS the side's MIDPOINT,
  at azimuth 60 / 180 / 300. Hinge triangle and crossing triangle are DUAL: rotated 60, scaled 2:1.
  each side changes colour at its tangent point -- where the two rulings cross on their way across.
  hinge-to-pole line : from hinge(0)=(2,0) to the pole (0,+-1). Solves 5t^2-8t+3=0:
                       it meets the circle at (0.8, +-0.6) -- azimuth +-36.87 -- then again at the pole.
                       solid to the first hit (near side), dotted from there to the pole (far side).
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
H = lambda d: 2*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))])
COL = {0: PURPLE, 120: RED, 240: BLUE}

fig, ax = plt.subplots(figsize=(9.2, 9.2))
th = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, zorder=2)                # the equator
ax.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=2.0, alpha=0.75, zorder=1)   # radius 2: through all three hinges

# --- the three sides: each tangent at its midpoint, changing colour there ---
for a, b in [(0,120), (120,240), (240,0)]:
    A, B = H(a), H(b); M = (A+B)/2
    ax.plot([A[0],M[0]], [A[1],M[1]], color=COL[a], lw=3.6, zorder=3)
    ax.plot([M[0],B[0]], [M[1],B[1]], color=COL[b], lw=3.6, zorder=3)
    ax.plot(*M, 'o', color=PURPLE, ms=9, zorder=6)

# --- the hinges ---
for d in (0,120,240):
    ax.plot(*H(d), 'D', color=COL[d], ms=16, zorder=7, markeredgecolor='k', markeredgewidth=0.8)

# --- the purple lines from the hinge: two to the poles, one horizontal ---
A = H(0)
LINES = [(np.array([0.8, +0.6]), np.array([0.0, +1.0])),      # to the top pole
         (np.array([0.8, -0.6]), np.array([0.0, -1.0])),      # to the bottom pole
         (np.array([1.0,  0.0]), np.array([-1.0, 0.0]))]      # horizontal: to the opposite tangent
for i,(K,P) in enumerate(LINES):
    lw = 3.0 if i == 2 else 2.0
    ax.plot([A[0],K[0]], [A[1],K[1]], color=PURPLE, lw=lw, zorder=4)                        # near: solid
    ax.plot([K[0],P[0]], [K[1],P[1]], color=PURPLE, lw=lw, ls=(0,(3,3)), zorder=4)          # far: dotted
    d = (A-K)/np.hypot(*(A-K)); E = A + d                                                    # behind the hinge, +1 alpha
    ax.plot([A[0],E[0]], [A[1],E[1]], color=PURPLE, lw=lw, zorder=4)
    ax.plot(*K, 'o', color=PURPLE, ms=9, zorder=8); ax.plot(*P, 'o', color=PURPLE, ms=9, zorder=8)
ax.plot([-1.0,-2.6], [0,0], color=PURPLE, lw=3.0, ls=(0,(3,3)), zorder=4)                    # out to the left, dotted


# --- the locus of lowest points: the FULL Thales circle on the diameter origin->hinge ---
# through the origin, both tangent points (0.5,+-sqrt3/2), and the hinge (vertical tangent there).
_t = np.linspace(0, 2*np.pi, 500)
ax.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=2.2, zorder=3)
# the OVERCRITICAL arc (P7: "no horizon (overcritical)") = the lines that MISS the equator:
#   the Thales arc from tangent(60) -> TOP -> the HINGE -> bottom -> tangent(300), i.e. 240..120
#   through 0. The dial runs UNDERCRITICAL (transverse, the far arc through the origin) -> NARIAI
#   (tangent, at 120/240) -> OVERCRITICAL (no horizon) -> VERTICAL (at the hinge, arc position 0).
_o = np.linspace(0, 2*np.pi, 500)
ax.plot(1 + np.cos(_o), np.sin(_o), color=PURPLE, lw=5.0, alpha=0.32, zorder=2)

# --- the vertical purple line at the hinge: THE END OF THE DIAL (the Thales tangent there) ---
ax.plot([2,2], [-1.75, 1.75], color=PURPLE, lw=2.2, zorder=4)

# --- the 45-degree lines from the hinge, through the top and bottom of the Thales circle ---
# closest approach sqrt(2): they MISS the equator -> NO HORIZON -> OVERCRITICAL. The top of the
# Thales circle sits INSIDE the overcritical arc. Parallel to the 45-deg chords.
for sgn in (+1,-1):
    T = np.array([1.0, sgn*1.0]); d = (T - H(0))/np.hypot(*(T-H(0)))
    E = H(0) + 3.15*d; B = H(0) - 1.0*d
    ax.plot([B[0],E[0]], [B[1],E[1]], color=PURPLE, lw=2.0, zorder=4)
    ax.plot(*T, 'o', color=PURPLE, ms=9, zorder=8)

# --- the two 45-deg chords meet ORTHOGONALLY at the back: Thales on the pole diameter ---
ax.plot(-1, 0, 'D', color=PURPLE, ms=15, zorder=9, markerfacecolor='none', markeredgewidth=2.2)

# --- the 45-degree chords: pole to the left of the circle ---
for sgn in (+1,-1):
    ax.plot([0,-1], [sgn*1.0, 0], color=PURPLE, lw=2.4, zorder=4)

# --- the hinge-to-pole lines continued past the pole, dashed: up the hyperboloid ---
for sgn in (+1,-1):
    K = np.array([0.8, sgn*0.6]); P = np.array([0.0, sgn*1.0])
    d = (P-K)/np.hypot(*(P-K)); E = P + 1.55*d
    ax.plot([P[0],E[0]], [P[1],E[1]], color=PURPLE, lw=2.0, ls=(0,(6,4)), zorder=4)


ax.set_aspect('equal'); ax.set_xlim(-3.35,3.75); ax.set_ylim(-3.05,3.05); ax.axis('off')
plt.savefig('p3_overhead.pdf', bbox_inches='tight')
plt.savefig('p3_overhead.png', dpi=150, bbox_inches='tight')
print('hinges 2a at 0/120/240 · sides tangent at 60/180/300 (the midpoints) · pins at (0.8,+-0.6) and (0,+-1)')
