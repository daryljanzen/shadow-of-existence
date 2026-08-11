"""
STEP 1 (r1108) — p3_overhead.py, RESTORED. Rays cut to 4 alpha. Every intersection marked.

DARYL'S CONVENTIONS, read off his own code and KEPT:
    COLOUR = WHOSE IT IS.   PURPLE = hinge 0 and everything it draws.  RED = hinge 120.
                            BLUE = hinge 240.  The triangle's sides change colour AT the
                            tangent point -- "where the two rulings cross on their way across".
    STYLE  = WHERE IT IS.   solid       = hinge -> FIRST HIT      (the near side)
                            dotted(3,3) = first hit -> onward     (the far side)
                            dashed(6,4) = past the pole           ("up the hyperboloid")

CHANGES THIS STEP, and only these:
    * every ray from the hinge is cut to EXACTLY 4 alpha.
    * EVERY intersection is computed and marked -- lines x equator, lines x Thales,
      lines x each other, lines x the hinge circle.
NOTHING recoloured. Nothing invented. The numbers are printed so they can be checked.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from itertools import combinations

plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
S3 = np.sqrt(3)
H = lambda d: 2*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))])
COL = {0: PURPLE, 120: RED, 240: BLUE}
A0 = H(0)
RAY = 4.0                                    # ** 4 alpha. all of them. **

fig, ax = plt.subplots(figsize=(15.5, 15.5)); ax.set_aspect('equal')
th = np.linspace(0, 2*np.pi, 500)

# ---- the circles, as his ----
ax.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, zorder=2)                    # equator
ax.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=2.0, alpha=0.75, zorder=1)    # hinge circle
ax.plot(1+np.cos(th), np.sin(th), color=PURPLE, lw=2.2, zorder=3)                  # Thales
ax.plot(1+np.cos(th), np.sin(th), color=PURPLE, lw=5.0, alpha=0.32, zorder=2)      # overcritical arc

# ---- the three sides: tangent at midpoints, colour changing there ----
for a, b in [(0, 120), (120, 240), (240, 0)]:
    A, B = H(a), H(b); M = (A+B)/2
    ax.plot([A[0], M[0]], [A[1], M[1]], color=COL[a], lw=3.6, zorder=4)
    ax.plot([M[0], B[0]], [M[1], B[1]], color=COL[b], lw=3.6, zorder=4)
for d in (0, 120, 240):
    ax.plot(*H(d), 'D', color=COL[d], ms=16, zorder=9, markeredgecolor='k', markeredgewidth=0.8)

# ---- hinge-0's rays, ALL 4 alpha, his styles ----
def unit(v): return v/np.hypot(*v)
RAYS = [('to the +pole',  np.array([0.8, +0.6]), np.array([0.0, +1.0])),
        ('to the -pole',  np.array([0.8, -0.6]), np.array([0.0, -1.0])),
        ('the horizontal', np.array([1.0, 0.0]), np.array([-1.0, 0.0]))]
for nm, K, P in RAYS:
    u = unit(K - A0)
    tK, tP = np.dot(K-A0, u), np.dot(P-A0, u)
    lw = 3.0 if 'horiz' in nm else 2.0
    ax.plot(*np.c_[A0, A0+tK*u], color=PURPLE, lw=lw, zorder=5)                       # solid: near
    ax.plot(*np.c_[A0+tK*u, A0+tP*u], color=PURPLE, lw=lw, ls=(0,(3,3)), zorder=5)    # dotted: far
    ax.plot(*np.c_[A0+tP*u, A0+RAY*u], color=PURPLE, lw=lw, ls=(0,(6,4)), zorder=5)   # dashed: beyond
    ax.plot(*np.c_[A0, A0-1.0*u], color=PURPLE, lw=lw, zorder=5)                      # behind the hinge
for sgn in (+1, -1):                                                                   # the 45-deg rays
    u = unit(np.array([1.0, sgn*1.0]) - A0)
    ax.plot(*np.c_[A0, A0+RAY*u], color=PURPLE, lw=2.0, zorder=5)
    ax.plot(*np.c_[A0, A0-1.0*u], color=PURPLE, lw=2.0, zorder=5)
ax.plot([2, 2], [A0[1]-RAY/2, A0[1]+RAY/2], color=PURPLE, lw=2.2, zorder=5)            # the vertical
for sgn in (+1, -1):                                                                   # the 45-deg chords
    ax.plot([0, -1], [sgn*1.0, 0], color=PURPLE, lw=2.4, zorder=5)
ax.plot(-1, 0, 'D', color=PURPLE, ms=15, zorder=10, markerfacecolor='none', markeredgewidth=2.2)

# =====================================================================
# EVERY INTERSECTION
# =====================================================================
def line_circle(P, u, C, R):
    f = P - C; b = 2*np.dot(f, u); c = np.dot(f, f) - R*R; disc = b*b - 4*c
    if disc < 0: return []
    return [P + t*u for t in ((-b-np.sqrt(disc))/2, (-b+np.sqrt(disc))/2)]
def line_line(P1, u1, P2, u2):
    A_ = np.array([u1, -u2]).T
    if abs(np.linalg.det(A_)) < 1e-12: return None
    t = np.linalg.solve(A_, P2 - P1); return P1 + t[0]*u1

# the full set of straight lines in the figure, as (name, point, direction)
LN = []
for nm, K, P in RAYS: LN.append((nm, A0, unit(K - A0)))
for sgn in (+1, -1): LN.append((f'45° {sgn:+d}', A0, unit(np.array([1.0, sgn*1.0]) - A0)))
LN.append(('the vertical', A0, np.array([0.0, 1.0])))
for a, b in [(0, 120), (120, 240), (240, 0)]: LN.append((f'side {a}-{b}', H(a), unit(H(b)-H(a))))
for sgn in (+1, -1): LN.append((f'45° chord {sgn:+d}', np.array([0.0, sgn*1.0]), unit(np.array([-1.0, -sgn*1.0]))))

pts = []
for nm, P, u in LN:
    for C, R, cn in [(np.zeros(2), 1.0, 'equator'), (np.array([1.0, 0.0]), 1.0, 'Thales'),
                     (np.zeros(2), 2.0, 'hinge circle')]:
        for X in line_circle(P, u, C, R): pts.append((X, f'{nm} × {cn}'))
for (n1, P1, u1), (n2, P2, u2) in combinations(LN, 2):
    X = line_line(P1, u1, P2, u2)
    if X is not None and np.hypot(*X) < 3.4: pts.append((X, f'{n1} × {n2}'))

uniq = []
for X, lab in pts:
    if not any(np.allclose(X, Y, atol=1e-6) for Y, _ in uniq): uniq.append((X, lab))
for X, lab in uniq:
    on_eq = abs(np.hypot(*X) - 1) < 1e-6
    ax.plot(*X, 'o', color=('k' if on_eq else '0.45'), ms=6.5 if on_eq else 4.0,
            zorder=11, markeredgecolor='w', markeredgewidth=0.6)

ax.set_xlim(-3.4, 3.9); ax.set_ylim(-3.4, 3.4); ax.axis('off')
ax.set_title("STEP 1 — the figure, restored.  Every ray $4\\alpha$.  Every intersection marked.\n"
             "BLACK $=$ on the throat.  GREY $=$ elsewhere.   Colours and styles are the figure's own.",
             fontsize=13, pad=14)
plt.savefig('step1_all_points.pdf', bbox_inches='tight')
plt.savefig('step1_all_points.png', dpi=145, bbox_inches='tight')

print(f"{len(uniq)} distinct intersections\n")
print("="*88)
print("ON THE THROAT — these are the ones that can be horizons")
print("="*88)
onthroat = [(X, l) for X, l in uniq if abs(np.hypot(*X)-1) < 1e-6]
for X, lab in sorted(onthroat, key=lambda z: np.degrees(np.arctan2(z[0][1], z[0][0])) % 360):
    b = np.degrees(np.arctan2(X[1], X[0])) % 360
    rat = all(abs(v*5 - round(v*5)) < 1e-9 for v in X)
    print(f"  ({X[0]:+.5f}, {X[1]:+.5f})   β = {b:7.3f}°   {'** RATIONAL **' if rat else ''}   {lab}")
print()
print("="*88)
print("OFF THE THROAT")
print("="*88)
for X, lab in sorted([(X, l) for X, l in uniq if abs(np.hypot(*X)-1) >= 1e-6],
                     key=lambda z: np.hypot(*z[0])):
    print(f"  ({X[0]:+.5f}, {X[1]:+.5f})   |X| = {np.hypot(*X):.5f}   {lab}")
