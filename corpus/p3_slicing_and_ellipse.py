"""
THE SLICING GEOMETRY AND THE ELLIPSE, TOGETHER (r1108).

Daryl: "Go and pull the actual figure from the overhead and work with it. THAT IS THE
SLICING GEOMETRY. Pull it and use it. That's 90% of the job... Actually look at the png
I told you to recreate and build it and build your stuff with it and combine it all."

LEFT  : p3_overhead.py's construction, REPRODUCED FROM ITS OWN CODE -- not a cartoon.
RIGHT : fig6_tilted_ellipse, REPRODUCED FROM P3's OWN PROPOSITION -- g(r)=g(r0) factoring
        into the line r=r0 and the ellipse r^2 + r r0 + r0^2 = 1.

AND THE THING THE FIGURE IS FOR: ** r0 read at every drawn point of the overhead. **

P3, sec:projection, verbatim -- and this is the reading the picture forces:
    "at offset r0 it meets the throat circle at TWO POINTS, A and B, with the point r=0
     FIXED AT THE BACK OF THE CIRCLE; these three special [points]"
So: ** THE THREE HORIZONS ARE THREE POINTS ON THE EQUATOR. ** A and B where the slicing
line cuts it, and r=0 at the back -- which in the drawn figure is (-1,0), the diamond,
and is ALSO one of the three tangent points. r=0 is where chirality flips to the left.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
S3 = np.sqrt(3)
H = lambda d: 2*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))])
COL = {0: PURPLE, 120: RED, 240: BLUE}

fig = plt.figure(figsize=(17.5, 9.4))
gs = fig.add_gridspec(2, 2, height_ratios=[3.0, 1.0], width_ratios=[1.12, 1], hspace=0.26, wspace=0.16)

# =====================================================================
# LEFT — p3_overhead.py, faithfully
# =====================================================================
ax = fig.add_subplot(gs[0, 0]); ax.set_aspect('equal')
th = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, zorder=2)                      # equator
ax.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=2.0, alpha=0.75, zorder=1)      # hinge circle

# the three sides: each tangent at its midpoint, colour changing there
for a, b in [(0, 120), (120, 240), (240, 0)]:
    A, B = H(a), H(b); M = (A + B)/2
    ax.plot([A[0], M[0]], [A[1], M[1]], color=COL[a], lw=3.6, zorder=3)
    ax.plot([M[0], B[0]], [M[1], B[1]], color=COL[b], lw=3.6, zorder=3)
    ax.plot(*M, 'o', color=PURPLE, ms=9, zorder=6)
for d in (0, 120, 240):
    ax.plot(*H(d), 'D', color=COL[d], ms=16, zorder=7, markeredgecolor='k', markeredgewidth=0.8)

# the purple lines from the hinge
A = H(0)
LINES = [(np.array([0.8, +0.6]), np.array([0.0, +1.0])),
         (np.array([0.8, -0.6]), np.array([0.0, -1.0])),
         (np.array([1.0,  0.0]), np.array([-1.0, 0.0]))]
for i, (K, P) in enumerate(LINES):
    lw = 3.0 if i == 2 else 2.0
    ax.plot([A[0], K[0]], [A[1], K[1]], color=PURPLE, lw=lw, zorder=4)
    ax.plot([K[0], P[0]], [K[1], P[1]], color=PURPLE, lw=lw, ls=(0, (3, 3)), zorder=4)
    d = (A - K)/np.hypot(*(A - K)); E = A + d
    ax.plot([A[0], E[0]], [A[1], E[1]], color=PURPLE, lw=lw, zorder=4)
    ax.plot(*K, 'o', color=PURPLE, ms=9, zorder=8); ax.plot(*P, 'o', color=PURPLE, ms=9, zorder=8)
ax.plot([-1.0, -2.6], [0, 0], color=PURPLE, lw=3.0, ls=(0, (3, 3)), zorder=4)

# the Thales circle + the overcritical arc
_t = np.linspace(0, 2*np.pi, 500)
ax.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=2.2, zorder=3)
ax.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=5.0, alpha=0.32, zorder=2)
ax.plot([2, 2], [-1.75, 1.75], color=PURPLE, lw=2.2, zorder=4)                       # the dial's end
for sgn in (+1, -1):                                                                  # the 45-deg lines
    T = np.array([1.0, sgn*1.0]); d = (T - H(0))/np.hypot(*(T - H(0)))
    ax.plot(*(np.c_[H(0) - 1.0*d, H(0) + 3.15*d]), color=PURPLE, lw=2.0, zorder=4)
    ax.plot(*T, 'o', color=PURPLE, ms=9, zorder=8)
ax.plot(-1, 0, 'D', color=PURPLE, ms=15, zorder=9, markerfacecolor='none', markeredgewidth=2.2)
for sgn in (+1, -1):
    ax.plot([0, -1], [sgn*1.0, 0], color=PURPLE, lw=2.4, zorder=4)

# ---------- r0 AT EVERY DRAWN POINT ----------
# P3: the slicing line at offset r0 meets the equator at A,B; r=0 is FIXED at the back.
# So r on the equator is measured FROM THE BACK. Daryl: "a parametric length along the ray
# that hits the equator and then goes around it" -- and the chord reading: chord from the
# back = 2|cos(beta/2)|, which is 0 at the back and 2 at the front.
BACK = np.array([-1.0, 0.0])
def chord_from_back(P):  return np.linalg.norm(np.asarray(P) - BACK)
def arc_from_back(P):
    b = np.degrees(np.arctan2(P[1], P[0])) % 360
    return np.radians(min((b - 180) % 360, (180 - b) % 360))     # arc length on the unit circle

PTS = [((-1.0,  0.0),  'the BACK · $r=0$\nchirality flips here', 'k'),
       (( 0.5,  0.866),'tangent pt $\\beta{=}60°$', PURPLE),
       (( 0.5, -0.866),'tangent pt $\\beta{=}300°$', PURPLE),
       (( 0.8,  0.6),  'THE PIN\n$\\arctan(3/4){=}36.87°$', '#b8860b'),
       (( 0.8, -0.6),  '', '#b8860b'),
       (( 0.0,  1.0),  'pole', '#2e8b57'),
       (( 0.0, -1.0),  '', '#2e8b57'),
       (( 1.0,  0.0),  'front of the equator', '0.35')]
print("="*86)
print("r0 AT EVERY DRAWN POINT OF THE OVERHEAD — read from the BACK, where P3 fixes r=0")
print("="*86)
print(f"  {'point':>16} {'azimuth β':>10} {'CHORD from back':>16} {'ARC from back':>14}   lands on?")
CRITVALS = {0.0: '$0$ — de Sitter', 1/S3: '$1/\\sqrt{3}$ — NARIAI', 1.0: '$1$ — chart-tangent',
            2/S3: '$2/\\sqrt{3}$ — NARIAI, ellipse vert. tangent', np.sqrt(2): '$\\sqrt{2}$ — the ellipse major semi-axis',
            S3: '$\\sqrt{3}$', 2.0: '$2$ — the diameter'}
for P, lab, c in PTS:
    b = np.degrees(np.arctan2(P[1], P[0])) % 360
    ch, ar = chord_from_back(P), arc_from_back(P)
    hit = [v for k, v in CRITVALS.items() if abs(ch - k) < 1e-6]
    print(f"  {str(P):>16} {b:>10.2f} {ch:>16.6f} {ar:>14.6f}   {hit[0] if hit else ''}")
    if lab:
        ax.annotate(lab, xy=P, xytext=(P[0]+(0.30 if P[0] > -0.5 else -0.85), P[1]+0.30),
                    fontsize=8.2, color=c, ha='left',
                    arrowprops=dict(arrowstyle='-', color=c, lw=0.8))
    ax.plot(*P, 'o', color=c, ms=5, zorder=10)
ax.set_xlim(-3.35, 3.75); ax.set_ylim(-3.05, 3.05); ax.axis('off')
ax.set_title("THE SLICING GEOMETRY — $\\tt p3\\_overhead.py$, reproduced from its own code.\n"
             "Equator at $\\alpha$; hinges at $2\\alpha$; sides tangent at their midpoints; "
             "the Thales circle through the origin and the hinge.", fontsize=10.5)

# =====================================================================
# RIGHT — the fundamental ellipse, from P3's proposition
# =====================================================================
axE = fig.add_subplot(gs[0, 1]); axE.set_aspect('equal')
t = np.linspace(0, 2*np.pi, 700)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
ex = (u + v)/np.sqrt(2); ey = (-u + v)/np.sqrt(2)
axE.plot(ex, ey, color=PURPLE, lw=2.6, zorder=4)
lin = np.linspace(-1.55, 1.55, 2)
axE.plot(lin, lin, color='0.5', lw=1.8, ls='--', zorder=3)
axE.plot(lin, -lin, color='0.82', lw=1.0, ls=':', zorder=2)
axE.text(1.18, 1.30, '$r=r_0$\nthe trivial root', fontsize=8.4, color='0.4')
axE.text(-1.52, 1.22, 'ellipse\n$r^2{+}rr_0{+}r_0^2{=}1$', fontsize=8.4, color=PURPLE)
axE.text(-1.55, -1.42, 'major axis $r=-r_0$\nTHE BACKWARD RADIAL', fontsize=7.8, color='0.55')
for sgn in (+1, -1):
    axE.plot(sgn*2/S3, -sgn/S3, 'o', color=RED, ms=10, zorder=7)
    axE.axvline(sgn*2/S3, color=RED, lw=1.0, ls=':', zorder=2)
axE.annotate('NARIAI\n$(2/\\sqrt{3},\\,-1/\\sqrt{3})$\nvertical tangent', xy=(2/S3, -1/S3),
             xytext=(0.62, -1.48), fontsize=8.2, color=RED,
             arrowprops=dict(arrowstyle='->', color=RED, lw=0.9))

# every critical r0 as a vertical line + its three horizons
CRIT = [(0, 0.0, 'de Sitter', BLUE), (30, 1/S3, 'NARIAI', PURPLE),
        (60, 1.0, 'chart-tangent', '#2e8b57'), (90, 2/S3, 'NARIAI $M{<}0$', RED)]
for w, r0, lab, col in CRIT:
    axE.axvline(r0, color=col, lw=1.4, alpha=0.5, zorder=2)
    for rt in np.roots([1, 0, -1, r0 - r0**3]):
        if abs(rt.imag) < 1e-9:
            axE.plot(r0, rt.real, 's', color=col, ms=6, zorder=6)
    axE.text(r0, 1.60, f'$w={w}°$', fontsize=8, color=col, ha='center', rotation=90)
axE.axhline(0, color='0.85', lw=0.7); axE.axvline(0, color='0.85', lw=0.7)
axE.set_xlabel('$r_0$'); axE.set_ylabel('$r$')
axE.set_xlim(-1.75, 1.75); axE.set_ylim(-1.75, 1.85); axE.grid(alpha=0.12)
axE.set_title("THE FUNDAMENTAL ELLIPSE — $g(r)=g(r_0)$, $g(t)=t^3-t$.\n"
              "A vertical line at $r_0$ meets the locus in THREE HORIZONS.", fontsize=10.5)

# =====================================================================
# BOTTOM — the dial axis
# =====================================================================
axD = fig.add_subplot(gs[1, :])
ws = np.linspace(0, 90, 900); r0s = (2/S3)*np.sin(np.radians(ws))
axD.plot(r0s, r0s - r0s**3, color='k', lw=2.2,
         label='$2M=r_0-r_0^3=(2/3\\sqrt{3})\\sin 3w$   — FOLDS')
axD.plot(r0s, ws/90*0.42, color=BLUE, lw=1.6, ls='--', label='$w$ (rescaled) — MONOTONE in $r_0$')
for w, r0, lab, col in CRIT:
    axD.axvline(r0, color=col, lw=1.4, alpha=0.55)
    axD.plot(r0, r0 - r0**3, 'o', color=col, ms=8, zorder=6)
    axD.annotate(f'$w={w}°$ · {lab}', xy=(r0, r0 - r0**3),
                 xytext=(r0, (r0 - r0**3) + (0.11 if w in (0, 60) else (0.09 if w == 30 else -0.16))),
                 ha='center', fontsize=8.2, color=col)
axD.axhline(0, color='0.8', lw=0.8)
axD.set_xlabel('$r_0$ — THE OFFSET AXIS'); axD.set_ylabel('$2M$')
axD.set_xlim(-0.03, 1.25); axD.set_ylim(-0.40, 0.56); axD.grid(alpha=0.14); axD.legend(fontsize=8.4)
axD.set_title("THE DIAL ON THE $r_0$ AXIS.   $w$ and $r_0$ are ONE axis (monotone, invertible).  "
              "$2M$ FOLDS at $w{=}30°$ — the involution $w\\mapsto60°{-}w$: past it, the geometry repeats.",
              fontsize=10)

fig.suptitle("The slicing geometry and the fundamental ellipse — combined, with the dial axis.",
             fontsize=13, y=0.98)
plt.savefig('p3_slicing_and_ellipse.pdf', bbox_inches='tight')
plt.savefig('p3_slicing_and_ellipse.png', dpi=150, bbox_inches='tight')
print("\nwrote p3_slicing_and_ellipse.pdf / .png")
