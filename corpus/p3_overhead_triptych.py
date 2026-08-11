"""P3 overhead — the triptych. One construction, stamped three ways.

BASE (all panels): the equator (radius alpha); the circle of radius 2alpha through all three hinges;
the hinge triangle (hinges at 2alpha, azimuth 0/120/240) whose three sides are TANGENT to the equator
at their own midpoints (60/180/300), each side changing colour at its tangency.

THE PURPLE STAMP (everything belonging to the hinge at azimuth 0):
  * the THALES CIRCLE on the diameter origin->hinge. It passes through the origin, both tangent points,
    and the hinge, where its tangent is VERTICAL.
      - OUTSIDE the equator it pins the closest approach of the lines that MISS  -> no horizon -> OVERCRITICAL
      - INSIDE  the equator it is the locus of CHORD MIDPOINTS of the lines that CUT -> transverse -> UNDERCRITICAL
      - NARIAI is exactly where those two descriptions coincide: the chord has shrunk to the tangency.
    The dial reads round it: undercritical (far arc, through the origin) -> NARIAI (the two tangents)
    -> overcritical (near arc) -> VERTICAL (at the hinge).
  * the two hinge-to-pole lines: solid to (0.8,+-0.6) where they first meet the equator, dotted across
    the far side to the pole (0,+-1), dashed on past it (up the hyperboloid), and continued 1 alpha
    behind the hinge.
  * the horizontal: solid to (1,0), dotted across to the opposite tangent (-1,0), dotted on out left.
  * the vertical at the hinge: the END OF THE DIAL.
  * the 45-degree lines through the top and bottom of the Thales circle (1,+-1) -- closest approach
    sqrt2: they miss, and they are parallel to the 45-degree chords.
  * the 45-degree chords, pole to (-1,0). They meet there ORTHOGONALLY -- Thales on the pole diameter
    (any point of a circle sees a diameter at 90). Marked.

PANELS
  left   : the stamp alone.
  middle : the stamp, plus itself lifted and rotated 90, laid down at alpha 0.5.
  right  : the stamp, plus itself rotated 120 in RED and 240 in BLUE -- one per hinge.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
H = lambda d: 2*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))])
COL = {0: PURPLE, 120: RED, 240: BLUE}

def rot(deg):
    c, s = np.cos(np.deg2rad(deg)), np.sin(np.deg2rad(deg))
    return np.array([[c,-s],[s,c]])

def draw_base(ax, deg=0.0, al=1.0):
    th = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, alpha=al, zorder=2)             # the equator
    ax.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=1.8, alpha=al*0.55, zorder=1)     # radius 2
    for a, b in [(0,120), (120,240), (240,0)]:
        A, B = H(a+deg), H(b+deg); M = (A+B)/2
        ax.plot([A[0],M[0]], [A[1],M[1]], color=COL[a], lw=3.4, alpha=al, zorder=3)
        ax.plot([M[0],B[0]], [M[1],B[1]], color=COL[b], lw=3.4, alpha=al, zorder=3)
        ax.plot(*M, 'o', color=PURPLE, ms=8, alpha=al, zorder=6)
    for d in (0,120,240):
        ax.plot(*H(d+deg), 'D', color=COL[d], ms=14, alpha=al, zorder=7,
                markeredgecolor=('k' if al > 0.8 else 'none'), markeredgewidth=0.7)

def stamp(ax, deg=0.0, c=PURPLE, al=1.0):
    """everything belonging to the hinge at azimuth 0, rotated by deg."""
    R = rot(deg); P = lambda v: R @ np.asarray(v, float)
    seg = lambda a,b,**k: ax.plot(*np.array([P(a),P(b)]).T, color=c, alpha=al, **k)
    A = np.array([2.0,0.0])
    # the Thales circle (heavy + line), on the diameter origin->hinge
    t = np.linspace(0, 2*np.pi, 500); C = np.array([1+np.cos(t), np.sin(t)])
    Cr = R @ C
    ax.plot(Cr[0], Cr[1], color=c, alpha=al*0.32, lw=5.0, zorder=2)
    ax.plot(Cr[0], Cr[1], color=c, alpha=al, lw=2.0, zorder=3)
    # the vertical at the hinge: the end of the dial
    seg([2,-1.75],[2,1.75], lw=2.0, zorder=4)
    # the three lines from the hinge (two to the poles, one horizontal), + 1 alpha behind the hinge
    for i,(K,Pl) in enumerate([(np.array([0.8,0.6]), np.array([0.0,1.0])),
                               (np.array([0.8,-0.6]), np.array([0.0,-1.0])),
                               (np.array([1.0,0.0]), np.array([-1.0,0.0]))]):
        lw = 2.8 if i==2 else 1.9
        seg(A, K, lw=lw, zorder=4)                                        # near side: solid
        seg(K, Pl, lw=lw, ls=(0,(3,3)), zorder=4)                         # far side: dotted
        d = (A-K)/np.hypot(*(A-K)); seg(A, A+d, lw=lw, zorder=4)          # behind the hinge
        for q in (K,Pl): ax.plot(*P(q), 'o', color=c, alpha=al, ms=8, zorder=8)
        if i < 2:                                                          # dashed on past the pole
            e = (Pl-K)/np.hypot(*(Pl-K)); seg(Pl, Pl+1.55*e, lw=1.9, ls=(0,(6,4)), zorder=4)
    seg([-1,0], [-2.6,0], lw=2.8, ls=(0,(3,3)), zorder=4)                  # out to the left
    # the 45-degree lines through the top and bottom of the Thales circle: miss by sqrt2
    for sgn in (+1,-1):
        T = np.array([1.0, sgn*1.0]); d = (T-A)/np.hypot(*(T-A))
        seg(A - 1.0*d, A + 3.15*d, lw=1.9, zorder=4)
        ax.plot(*P(T), 'o', color=c, alpha=al, ms=8, zorder=8)
    # the 45-degree chords, meeting orthogonally at the back
    for sgn in (+1,-1): seg([0,sgn*1.0], [-1,0], lw=2.2, zorder=4)
    ax.plot(*P([-1,0]), 'D', color=c, alpha=al, ms=14, zorder=9, markerfacecolor='none', markeredgewidth=2.0)

fig, AX = plt.subplots(2, 2, figsize=(17.0, 17.0))
AX = AX.ravel()
for ax in AX:
    ax.set_aspect('equal'); ax.set_xlim(-4.0,4.0); ax.set_ylim(-4.0,4.0); ax.axis('off')

# (1) ONE stamp -- the construction belonging to a single hinge.
draw_base(AX[0]); stamp(AX[0])

# (2) THE PURPLE FAMILY'S QUARTER-TURN ORBIT: the stamp rotated three more times -- 0/90/180/270.
#     One family, four stamps. (Not the three hinges -- those are the OTHER two families.)
draw_base(AX[1])
for d in (0,90,180,270): stamp(AX[1], d, PURPLE)

# (3) THREE FAMILIES -- one colour per hinge.
draw_base(AX[2]); stamp(AX[2], 0, PURPLE); stamp(AX[2], 120, RED); stamp(AX[2], 240, BLUE)

# (4) THE CENTRAL FIGURE: all three families, stamped four times, all the same. No alpha.
#     4 quarter-turns x 3 hinges = 12 hinges every 30 degrees -- it closes, because 3 and 4 are coprime.
#     *** AND THIS IS DOUBLED: there is a BOTTOM. The hinges live at X0 = +-sqrt3 alpha; this is one. ***
for k in range(4):
    q = 90*k
    draw_base(AX[3], q)
    stamp(AX[3], q+0, PURPLE); stamp(AX[3], q+120, RED); stamp(AX[3], q+240, BLUE)

plt.tight_layout()
plt.savefig('p3_overhead_triptych.pdf', bbox_inches='tight')
plt.savefig('p3_overhead_triptych.png', dpi=120, bbox_inches='tight')
print('2x2: one stamp | three purple | three families | THE CENTRAL FIGURE (12 stamps, no alpha)')
print('NOTE: this is the TOP only. The hinges are at X0 = +-sqrt3 alpha -- there is a BOTTOM.')
