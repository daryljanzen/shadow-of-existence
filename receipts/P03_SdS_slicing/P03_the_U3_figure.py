"""
P03_the_U3_figure.py -- P3 Figure~\\ref{fig:U3}: the hinge structure entire.

WHAT THIS RECEIPT IS FOR.  A figure is a claim, and this one makes four at once -- the
3x2 puncture count, the twelve legs on three graze points, the incircle/two-to-one
projection, and the ANTIPODAL hinge-to-wall map with its 1+2 consequence.  A drawing can
be wrong in a way prose cannot: it can be *drawn* right and *described* wrong, or drawn
from coordinates nobody checked.  So the builder verifies every fact it draws before it
draws it, and this receipt is that verification.

VERIFIED EXACTLY (all residuals at machine zero; the script asserts and exits nonzero):
  1. TANGENCY.  Each of the six chords U_i -> D_j (i != j) meets the throat |X|=alpha at
     its own MIDPOINT, and meets it tangentially: the midpoint has |m| = alpha, m_0 = 0,
     and the chord direction is orthogonal to the radius there.
  2. THE CAUSAL TRICHOTOMY, on all fifteen pairs of the six punctures, with the sign
     convention stated rather than assumed: on dS two points are null-separated iff
     X.Y = alpha^2, timelike-separated iff X.Y > alpha^2, spacelike iff X.Y < alpha^2.
     Same hinge gives 7 alpha^2, same horn -5 alpha^2, neither exactly alpha^2, whence
       timelike <=> same hinge (3)   spacelike <=> same horn (6)   null <=> neither (6),
     agreeing pairwise with the labels.  (This is P03_hexagon_null_triple's result, re-run
     here in floating point as an independent check of the figure's own coordinates.)
  3. THE WALL ASSIGNMENT.  w_k is placed ANTIPODAL to h_k -- azimuths 180/300/60 against
     hinges at 0/120/240 -- and the twelve legs are then found to graze at exactly those
     three points, with hinge k grazing at {the other two} and NEVER at its own w_k.

** A CAUGHT ERROR, RECORDED BECAUSE THE GATE IS ONLY WORTH ITS CATCHES.  The first run of
the builder classified the trichotomy with the inequality REVERSED (timelike iff
X.Y < alpha^2), and returned timelike 6 / spacelike 3 -- the two classes swapped, the null
class unaffected.  The null count being right is exactly why this had to be checked rather
than eyeballed: the equality case is insensitive to the error that breaks the other two. **

WHAT THE FIGURE DOES NOT CLAIM.  No Standard Model correspondence is drawn or implied; the
colours are labels for horn and object, not for colour charge.  The u/d assignment cannot
be read off the figure at all -- the symmetry group is transitive on the six punctures, so
an absolute assignment is FORBIDDEN, not merely absent (P03_hexagon_null_triple).

PROVENANCE NOTE.  The figure was built at c54.35 and NOT LANDED: it was written to the
repository root's figures/, which pdflatex never reads, and was cited by no paper.  The
arc's row was struck anyway.  Built ~= landed, and the strike was premature; the row is
corrected and this receipt is the standing check that the figure the paper includes is the
figure whose facts were verified.

ORIGIN: computations/baryon_edge/L106_build_U3.py -- built r2376 (c54.36); edit the
origin, not this copy."""

import os
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

a = 1.0
ANG = [0, 120, 240]
S3 = np.sqrt(3)

# ------------------------------------------------------------------ the objects
def pol(deg, rad=1.0, z=0.0):
    return np.array([rad*np.cos(np.radians(deg)), rad*np.sin(np.radians(deg)), z])

P = {f"{nm}{k}": pol(A, 2*a, s*S3*a)
     for k, A in enumerate(ANG) for s, nm in ((1, 'U'), (-1, 'D'))}
# a hinge's wall is ANTIPODAL to it on the throat: hinge k at A -> wall at A+180.
WALL = {k: pol(A + 180, a, 0.0) for k, A in enumerate(ANG)}   # 180, 300, 60 degrees
CHORD = [(f"U{i}", f"D{j}") for i in range(3) for j in range(3) if i != j]

# ------------------------------------------------------------------ the checks
print("=" * 74)
print("CHECKS — the figure draws nothing it has not verified")
print("=" * 74)

# (1) every chord is tangent to the throat at its own midpoint
worst = 0.0
for u, d in CHORD:
    m = 0.5*(P[u] + P[d])
    worst = max(worst, abs(np.hypot(m[0], m[1]) - a), abs(m[2]))
    # tangency: the chord direction is orthogonal to the radius at the midpoint
    t = P[d] - P[u]
    worst = max(worst, abs(np.dot(t[:2], m[:2])))
print(f"  (1) six chords tangent to the throat at their midpoints   max residual {worst:.2e}")

# (2) the causal trichotomy on all fifteen pairs of ends
eta = np.diag([1.0, 1.0, -1.0])          # (X1,X2,X0) with X.Y = X1Y1 + X2Y2 - X0Y0
cls = {'timelike': 0, 'spacelike': 0, 'null': 0}
ok = True
for x, y in itertools.combinations(sorted(P), 2):
    dot = float(P[x] @ eta @ P[y])
    same_hinge = x[1] == y[1]
    same_horn = x[0] == y[0]
    # on dS: null iff X.Y = alpha^2; timelike separated iff X.Y > alpha^2 (same hinge,
    # 7 alpha^2); spacelike iff X.Y < alpha^2 (same horn, -5 alpha^2).
    kind = ('null' if abs(dot - a*a) < 1e-9 else
            'timelike' if dot > a*a else 'spacelike')
    cls[kind] += 1
    ok &= (kind == 'timelike') == same_hinge
    ok &= (kind == 'spacelike') == same_horn
print(f"  (2) trichotomy {cls}   labels agree: {ok}")

# (3) the wall of a hinge is where the OTHER TWO hinges' legs graze, never its own
own = {k: set() for k in range(3)}
for u, d in CHORD:
    m = 0.5*(P[u] + P[d])
    w = min(WALL, key=lambda k: np.linalg.norm(WALL[k] - m))
    own[int(u[1])].add(w); own[int(d[1])].add(w)
print(f"  (3) hinge k grazes at walls  " +
      "  ".join(f"{k}->{sorted(own[k])}" for k in range(3)) +
      f"   own excluded: {all(k not in own[k] for k in range(3))}")
assert worst < 1e-9 and ok and all(k not in own[k] for k in range(3))
print()

# ------------------------------------------------------------------ the drawing
BLUE, GREEN, ORANGE, RED, INK = '#1f77b4', '#2e8b57', '#e08a1e', '#c0392b', '#111111'
fig = plt.figure(figsize=(11.6, 5.3))

# ---- panel (a): the substrate, in 3D
ax = fig.add_subplot(1, 2, 1, projection='3d')
u = np.linspace(-np.arcsinh(2.5), np.arcsinh(2.5), 60)
v = np.linspace(0, 2*np.pi, 120)
U, V = np.meshgrid(u, v)
R = a*np.cosh(U)
ax.plot_surface(R*np.cos(V), R*np.sin(V), a*np.sinh(U), alpha=0.10, color='#5b7fa6',
                linewidth=0, antialiased=True, zorder=0)
th = np.linspace(0, 2*np.pi, 300)
ax.plot(a*np.cos(th), a*np.sin(th), 0*th, color=RED, lw=2.2, zorder=6)
for k, A in enumerate(ANG):
    x, y = 2*a*np.cos(np.radians(A)), 2*a*np.sin(np.radians(A))
    ax.plot([x, x], [y, y], [-2.6, 2.6], color=INK, lw=2.4, zorder=8)
    ax.text(x*1.10, y*1.10, 2.75, f"$h_{k}$", fontsize=10, color=INK)
for uu, dd in CHORD:
    A, B = P[uu], P[dd]
    ax.plot(*zip(A, B), color=ORANGE, lw=1.4, alpha=0.95, zorder=7)
for nm, p in P.items():
    ax.scatter(*p, s=42, color=(BLUE if nm[0] == 'U' else GREEN),
               edgecolor='k', linewidth=0.5, zorder=10, depthshade=False)
for k in WALL:
    ax.scatter(*WALL[k], s=80, marker='s', color=RED, edgecolor='k',
               linewidth=0.6, zorder=11, depthshade=False)
ax.set_xlim(-2.7, 2.7); ax.set_ylim(-2.7, 2.7); ax.set_zlim(-2.7, 2.7)
ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=16, azim=34)
ax.set_xlabel('$X_1$', labelpad=-6); ax.set_ylabel('$X_2$', labelpad=-6)
ax.set_zlabel('$X_0$', labelpad=-6)
ax.tick_params(labelsize=7, pad=-2)
ax.grid(False)
for pane in (ax.xaxis, ax.yaxis, ax.zaxis):
    pane.pane.set_alpha(0.02)
ax.text2D(0.02, 0.95, r'(a)  in the substrate', transform=ax.transAxes, fontsize=11)

# ---- panel (b): the true orthographic projection to X0 = 0
bx = fig.add_subplot(1, 2, 2)
bx.add_patch(plt.Circle((0, 0), a, fill=False, color=RED, lw=2.2, zorder=5))
tri = np.array([pol(A, 2*a) for A in ANG] + [pol(ANG[0], 2*a)])
bx.plot(tri[:, 0], tri[:, 1], color='#888', lw=1.0, ls='--', zorder=3)
# the six chords project two-to-one onto the three sides; draw hinge 0's pair thick
for uu, dd in CHORD:
    A, B = P[uu][:2], P[dd][:2]
    mine = (uu[1] == '0' or dd[1] == '0')
    bx.plot([A[0], B[0]], [A[1], B[1]], color=(ORANGE if mine else '#c9a86a'),
            lw=(2.6 if mine else 1.0), alpha=(1.0 if mine else 0.55),
            zorder=(6 if mine else 4))
for k, A in enumerate(ANG):
    v = pol(A, 2*a)
    bx.scatter(v[0], v[1], s=70, color=INK, zorder=9)
    bx.text(v[0]*1.10, v[1]*1.10, f"$h_{k}$", fontsize=11, ha='center', va='center')
    w = WALL[k]
    bx.plot([v[0], w[0]], [v[1], w[1]], color='#999', lw=0.9, ls=':', zorder=2)
    bx.scatter(w[0], w[1], s=95, marker='s', color=RED, edgecolor='k',
               linewidth=0.6, zorder=10)
    bx.text(w[0]*1.42, w[1]*1.42, f"$w_{k}$", fontsize=11, color=RED,
            ha='center', va='center')
bx.set_xlim(-2.75, 2.75); bx.set_ylim(-2.55, 2.55)
bx.set_aspect('equal'); bx.axis('off')
bx.text(0.02, 0.95, r'(b)  projected to $X_{0}=0$', transform=bx.transAxes, fontsize=11)
bx.text(0.02, 0.03,
        'hinge $h_{0}$\'s two legs (thick) graze at $w_{1},w_{2}$ — never at its own $w_{0}$',
        transform=bx.transAxes, fontsize=8.5, color='#444')

fig.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
for out in (os.path.join(root, 'corpus', 'figures', 'CR_hinge_substrate_U3.png'),
            os.path.join(root, 'figures', 'U3_hinge_structure.png')):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=200)
    print("  wrote", os.path.relpath(out, root))
print(f"\n  3 hinges · {len(P)} punctures · {len(CHORD)} chords = {2*len(CHORD)} legs · "
      f"{len(WALL)} walls · grazing at 3 points")
