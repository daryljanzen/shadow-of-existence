"""
THE MAPPING, PROPERLY (r1108) — p3_overhead.py RESTORED, whole, big; and the FULL r0 range.

Two things were wrong and both were mine:
  1. I replaced the actual overhead with a stick diagram of a few lines through a circle.
     ** The figure's OWN LINES ARE THE SLICING LINES. ** It was already the thing I was
     trying to draw. Restored, entire, from its own code.
  2. I plotted only r0 > 0. The ellipse is symmetric under (r0,r) -> (-r0,-r) -- the outer
     Z2, 2M -> -2M, THE BACKWARD RADIAL. Half the diagram was missing, and the missing half
     is the half the mass reflection lives in.

AND WHAT RESTORING IT SHOWS -- the figure's own lines, read as slicings (D = the signed
perpendicular offset from the centre; r0 = D/sqrt3, the reading P3's own sentence forces):

    the HORIZONTAL  (1,0)-(-1,0)   D = 0        r0 = 0        ** DE SITTER **
    the TRIANGLE'S SIDES           D = +-1      r0 = +-1/sqrt3 ** NARIAI **
    the HINGE-TO-POLE lines        D = +-2/sqrt5 r0 = +-0.5164
    the 45-degree lines            D = +-sqrt2  r0 = +-0.8165
    the VERTICAL at the hinge      D = 2        r0 = 2/sqrt3  ** NARIAI, the OTHER designation **

** THE HINGE TRIANGLE'S SIDES ARE THE NARIAI CUTS. ** And the vertical at the hinge is
Nariai too, at the other r0. P3: "The same Nariai geometry is met at |r0|=2/sqrt3 with the
lone root designated and the other two merging: ONE GEOMETRY UNDER TWO DESIGNATIONS."
** The triangle and the vertical are that one geometry, drawn twice, in one figure. **
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
S3 = np.sqrt(3); GOLD = '#d4a017'; GREEN = '#2e8b57'
H = lambda d: 2*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))])
COL = {0: PURPLE, 120: RED, 240: BLUE}

fig = plt.figure(figsize=(26, 14.5))
gs = fig.add_gridspec(1, 2, width_ratios=[1.42, 1], wspace=0.07)

# =====================================================================================
# LEFT — p3_overhead.py, RESTORED WHOLE, from its own code
# =====================================================================================
ax = fig.add_subplot(gs[0, 0]); ax.set_aspect('equal')
th = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, zorder=2)
ax.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=2.0, alpha=0.75, zorder=1)

for a, b in [(0, 120), (120, 240), (240, 0)]:
    A, B = H(a), H(b); M = (A+B)/2
    ax.plot([A[0], M[0]], [A[1], M[1]], color=COL[a], lw=3.6, zorder=3)
    ax.plot([M[0], B[0]], [M[1], B[1]], color=COL[b], lw=3.6, zorder=3)
    ax.plot(*M, 'o', color=PURPLE, ms=9, zorder=6)
for d in (0, 120, 240):
    ax.plot(*H(d), 'D', color=COL[d], ms=16, zorder=7, markeredgecolor='k', markeredgewidth=0.8)

A = H(0)
LINES = [(np.array([0.8, +0.6]), np.array([0.0, +1.0])),
         (np.array([0.8, -0.6]), np.array([0.0, -1.0])),
         (np.array([1.0,  0.0]), np.array([-1.0, 0.0]))]
for i, (K, P) in enumerate(LINES):
    lw = 3.0 if i == 2 else 2.0
    ax.plot([A[0], K[0]], [A[1], K[1]], color=PURPLE, lw=lw, zorder=4)
    ax.plot([K[0], P[0]], [K[1], P[1]], color=PURPLE, lw=lw, ls=(0, (3, 3)), zorder=4)
    d = (A-K)/np.hypot(*(A-K)); E = A + d
    ax.plot([A[0], E[0]], [A[1], E[1]], color=PURPLE, lw=lw, zorder=4)
    ax.plot(*K, 'o', color=PURPLE, ms=9, zorder=8); ax.plot(*P, 'o', color=PURPLE, ms=9, zorder=8)
ax.plot([-1.0, -2.6], [0, 0], color=PURPLE, lw=3.0, ls=(0, (3, 3)), zorder=4)

_t = np.linspace(0, 2*np.pi, 500)
ax.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=2.2, zorder=3)
ax.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=5.0, alpha=0.32, zorder=2)
ax.plot([2, 2], [-1.75, 1.75], color=PURPLE, lw=2.2, zorder=4)
for sgn in (+1, -1):
    T = np.array([1.0, sgn*1.0]); d = (T - H(0))/np.hypot(*(T-H(0)))
    E = H(0) + 3.15*d; B_ = H(0) - 1.0*d
    ax.plot([B_[0], E[0]], [B_[1], E[1]], color=PURPLE, lw=2.0, zorder=4)
    ax.plot(*T, 'o', color=PURPLE, ms=9, zorder=8)
ax.plot(-1, 0, 'D', color=PURPLE, ms=15, zorder=9, markerfacecolor='none', markeredgewidth=2.2)
for sgn in (+1, -1):
    ax.plot([0, -1], [sgn*1.0, 0], color=PURPLE, lw=2.4, zorder=4)
for sgn in (+1, -1):
    K = np.array([0.8, sgn*0.6]); P = np.array([0.0, sgn*1.0])
    d = (P-K)/np.hypot(*(P-K)); E = P + 1.55*d
    ax.plot([P[0], E[0]], [P[1], E[1]], color=PURPLE, lw=2.0, ls=(0, (6, 4)), zorder=4)

# ---- WHAT EACH OF THE FIGURE'S OWN LINES IS, AS A SLICING ----
def r0_of_D(D): return D/S3
ANN = [((-1.7, 0.13), '$D=0$   $r_0=0$\n** DE SITTER **', BLUE),
       ((-2.15, 1.28), 'THE TRIANGLE\'S SIDES are TANGENT:\n$D=\\pm1$,  $r_0=\\pm1/\\sqrt{3}$\n** NARIAI **', GREEN),
       ((2.12, 1.90), 'THE VERTICAL:\n$D=2$,  $r_0=2/\\sqrt{3}$\n** NARIAI — the OTHER\ndesignation **', RED),
       ((1.35, -2.35), 'the hinge-to-pole lines\n$D=\\pm2/\\sqrt{5}$,  $r_0=\\pm0.5164$', GOLD),
       ((-2.9, -1.85), 'the $45°$ lines\n$D=\\pm\\sqrt{2}$,  $r_0=\\pm0.8165$', '#e07b39')]
for xy, s, c in ANN:
    ax.text(*xy, s, fontsize=10.5, color=c, ha='left', va='center',
            bbox=dict(fc='white', ec=c, alpha=0.86, lw=1.0, boxstyle='round,pad=0.32'))

PTS = [((-1., 0.), '$r=0$ — THE BACK\nchirality flips', 'k', 10),
       ((0.8, 0.6), 'THE PIN $(4/5,3/5)$\n** THE PYTHAGOREAN POINT **\nthe only RATIONAL point,\non the dS horizon', GOLD, 11),
       ((0.8, -0.6), '', GOLD, 9),
       ((0., 1.), 'the POLE', GREEN, 9), ((0., -1.), '', GREEN, 9)]
for P, lab, c, ms in PTS:
    ax.plot(*P, 'o', color=c, ms=ms, zorder=11, markeredgecolor='k', markeredgewidth=0.6)
    if lab:
        ax.annotate(lab, xy=P, xytext=(P[0]+(0.42 if P[0] > -0.5 else -1.55), P[1]+0.52),
                    fontsize=9.5, color=c, arrowprops=dict(arrowstyle='-', color=c, lw=0.9))
ax.text(0, 1.10, 'THE THROAT $r=\\alpha$   **IS**   THE DE SITTER HORIZON', ha='center',
        fontsize=11.5, color='0.3', style='italic')
ax.set_xlim(-3.35, 3.75); ax.set_ylim(-3.05, 3.05); ax.axis('off')
ax.set_title("THE SLICING GEOMETRY — restored whole.   Its own lines ARE the slicings.\n"
             "$D$ = signed perpendicular offset from the centre;   $r_0 = D/\\sqrt{3}$.",
             fontsize=14, pad=14)

# =====================================================================================
# RIGHT — the (r0,r) plane, THE FULL RANGE, both halves
# =====================================================================================
axE = fig.add_subplot(gs[0, 1]); axE.set_aspect('equal')
L = 1.55; n = 800
R0g, Rg = np.meshgrid(np.linspace(-L, L, n), np.linspace(-L, L, n))
with np.errstate(divide='ignore', invalid='ignore'):
    fg = 1 - (R0g - R0g**3)/Rg - Rg**2
axE.contourf(R0g, Rg, (fg < 0).astype(float), levels=[.5, 1.5], colors=['0.84'], zorder=0)
t = np.linspace(0, 2*np.pi, 900)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
axE.plot((u+v)/np.sqrt(2), (-u+v)/np.sqrt(2), color='k', lw=2.2, ls=':', zorder=5)
dd = np.linspace(-L, L, 2); axE.plot(dd, dd, color='k', lw=2.2, ls=':', zorder=5)
axE.plot(dd, -dd, color='0.72', lw=1.0, ls='-.', zorder=1)
r0c = np.linspace(-L, L, 800); M2c = r0c - r0c**3
axE.plot(r0c, M2c, color='k', lw=1.9, zorder=6)
axE.plot(r0c, 1.5*M2c, color='k', lw=1.2, ls='-.', zorder=6)
axE.plot(r0c, -np.cbrt(M2c), color='k', lw=1.6, ls=(0, (7, 4)), zorder=6)

# ** THE FULL RANGE: every line, BOTH SIGNS **
MAP = [('$D=0$ — DE SITTER', 0.0, BLUE),
       ('triangle sides — NARIAI', 1.0, GREEN),
       ('hinge-to-pole', 2/np.sqrt(5), GOLD),
       ('$45°$ lines', np.sqrt(2), '#e07b39'),
       ('the VERTICAL — NARIAI', 2.0, RED)]
for nm, D, c in MAP:
    for s in ((+1, -1) if D != 0 else (+1,)):
        r0 = s*r0_of_D(D)
        axE.axvline(r0, color=c, lw=2.2 if s > 0 else 1.6, alpha=0.9 if s > 0 else 0.55, zorder=3)
        for rt in np.roots([1, 0, -1, r0 - r0**3]):
            if abs(rt.imag) < 1e-9:
                axE.plot(r0, rt.real, 'o', color=c, ms=9 if s > 0 else 7, zorder=8,
                         markeredgecolor='k', markeredgewidth=0.6)
for sgn in (+1, -1):
    axE.plot(sgn*2/S3, -sgn/S3, '*', color=RED, ms=20, zorder=10, markeredgecolor='k', markeredgewidth=0.5)
    axE.plot(sgn/S3, sgn/S3, '*', color=GREEN, ms=17, zorder=10, markeredgecolor='k', markeredgewidth=0.5)
axE.text(1.19, -0.46, 'NARIAI\n$2/\\sqrt{3}$', fontsize=9, color=RED, ha='center')
axE.text(-1.19, 0.46, 'NARIAI\n$-2/\\sqrt{3}$', fontsize=9, color=RED, ha='center')
axE.text(0.60, 0.76, 'NARIAI\n$1/\\sqrt{3}$\n(on the diagonal:\n$r_0$ IS its own\nhorizon)', fontsize=8.6, color=GREEN)
axE.text(-1.50, 1.34, '$r{=}2M$ solid · $r{=}3M$ dash-dot\n$r{=}(-2M)^{1/3}$ dashed — THE TURNAROUND\nhorizons dotted · grey $= f<0$', fontsize=8.6)
axE.text(-1.50, -1.44, 'The whole plane: $(r_0,r)\\mapsto(-r_0,-r)$ is\nTHE OUTER $\\mathbb{Z}_2$ — $2M\\mapsto-2M$,\nthe BACKWARD RADIAL. Left half $=$ the\nmirror lines, below the axis.', fontsize=8.6)
axE.axhline(0, color='k', lw=0.9); axE.axvline(0, color='k', lw=0.9)
axE.set_xlim(-L, L); axE.set_ylim(-L, L)
axE.set_xlabel('$r_0$', fontsize=13); axE.set_ylabel('$r$', fontsize=13)
axE.set_title("THE FUNDAMENTAL ELLIPSE (Janzen 2012) — the FULL range.\n"
              "Each slicing line $\\mapsto$ a vertical at its $r_0$; its horizons $\\mapsto$ the intersections.",
              fontsize=14, pad=14)

fig.suptitle("The slicing geometry and the fundamental ellipse — the full mapping, both halves.    "
             "The triangle's sides are the NARIAI cuts; the vertical is NARIAI again, at the other designation.",
             fontsize=16, y=0.955)
plt.savefig('the_mapping_full.pdf', bbox_inches='tight')
plt.savefig('the_mapping_full.png', dpi=140, bbox_inches='tight')
print("wrote the_mapping_full.pdf / .png")
print()
print("="*96)
print("THE FIGURE'S OWN LINES, READ AS SLICINGS — the full range, both signs")
print("="*96)
print(f"  {'the line in the figure':<34} {'D':>10} {'r0=D/sq3':>10} {'2M':>10} {'|r0|':>8}  what it is")
for nm, D, c in MAP:
    for s in ((+1, -1) if D != 0 else (+1,)):
        r0 = s*D/S3; m2 = r0 - r0**3
        what = ('** DE SITTER **' if abs(m2) < 1e-12 else
                '** NARIAI **' if abs(abs(r0) - 1/S3) < 1e-9 or abs(abs(r0) - 2/S3) < 1e-9 else
                'undercritical' if abs(r0) < 2/S3 else 'overcritical')
        print(f"  {nm.replace('$','').replace('\\\\',''):<34} {s*D:>10.5f} {r0:>10.5f} {m2:>10.5f} {abs(r0):>8.5f}  {what}")
print()
print("  >> ** THE HINGE TRIANGLE'S SIDES ARE THE NARIAI CUTS. ** They are tangent to the")
print("     throat, so D = alpha, so r0 = 1/sqrt3 -- and 1/sqrt3 is where r0 IS its own")
print("     horizon: the point ON THE DIAGONAL where the ellipse meets the line r=r0.")
print("  >> ** AND THE VERTICAL AT THE HINGE IS NARIAI TOO, at r0 = 2/sqrt3 -- the ellipse's")
print("     VERTICAL TANGENT. ** P3: 'The same Nariai geometry is met at |r0|=2/sqrt3 with")
print("     the lone root designated and the other two merging: ONE GEOMETRY UNDER TWO")
print("     DESIGNATIONS, which is the content of the involution.'")
print("     ** THE TRIANGLE AND THE VERTICAL ARE THAT ONE GEOMETRY, DRAWN TWICE, IN ONE")
print("        FIGURE -- and the involution that relates them is the figure's own. **")
