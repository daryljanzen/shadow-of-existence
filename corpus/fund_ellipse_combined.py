"""
THE FUNDAMENTAL ELLIPSE (2012) + THE SLICING GEOMETRY, COMBINED  (r1108)

Daryl's 2012 thesis figure `fund_ellipse.png`, reproduced with everything it actually has
-- which is a great deal more than P3's fig6 carried forward:

    solid    r = 2M                 the Schwarzschild radius, across the whole family
    dash-dot r = 3M                 the photon sphere
    long-dash r = (-2M)^{1/3}       ** THE COMOVING TURNAROUND ** -- lem:twoturnings' OTHER
                                    cubic, r^3 = -2M alpha^2. On the page since 2012.
    dotted   horizons               g(r) = g(r0): the line r=r0 AND the ellipse r^2+rr0+r0^2=1
    SHADING  ** THE SIGN OF f **    decoded from the original's pixels at r1108:
                                    grey = 99.8% f<0 ; white = 99.8% f>0.
                                    f = 1 - 2M/r - r^2/alpha^2.

** SO THE 2012 FIGURE IS A MAP OF THE CAUSAL STRUCTURE OF THE WHOLE SdS FAMILY AT ONCE. **
Every point (r0, r) is A RADIUS IN A GEOMETRY, and the shading says which side of the
horizon you are standing on. P3's fig6 has the ellipse, the diagonal and the Nariai
tangents -- and no shading, no 2M, no 3M, no turnaround. It is this figure with the
physics taken out.

RIGHT PANEL: p3_overhead.py's slicing geometry, reproduced from its own code, with the
critical points marked and carried across.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
S3 = np.sqrt(3)
GOLD = '#b8860b'; GREEN = '#2e8b57'

fig = plt.figure(figsize=(18.5, 9.2))
gs = fig.add_gridspec(1, 2, width_ratios=[1.06, 1], wspace=0.14)

# =====================================================================
# LEFT — THE 2012 FUNDAMENTAL ELLIPSE, everything it has
# =====================================================================
ax = fig.add_subplot(gs[0, 0]); ax.set_aspect('equal')
L = 1.5
n = 900
R0g, Rg = np.meshgrid(np.linspace(-L, L, n), np.linspace(-L, L, n))
M2g = R0g - R0g**3
with np.errstate(divide='ignore', invalid='ignore'):
    fg = 1 - M2g/Rg - Rg**2                       # the SdS slicing function, alpha = 1
# ** THE SHADING: the sign of f. grey where f<0 -- inside a horizon, signature flipped. **
ax.contourf(R0g, Rg, (fg < 0).astype(float), levels=[0.5, 1.5], colors=['0.80'], zorder=0)

# --- the horizons: g(r)=g(r0) = (r-r0)(r^2+rr0+r0^2-1) ---
t = np.linspace(0, 2*np.pi, 900)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
ex, ey = (u + v)/np.sqrt(2), (-u + v)/np.sqrt(2)
ax.plot(ex, ey, color='k', lw=2.0, ls=':', zorder=5)
d = np.linspace(-L, L, 2)
ax.plot(d, d, color='k', lw=2.0, ls=':', zorder=5)

# --- the M curves ---
r0 = np.linspace(-L, L, 900); M2 = r0 - r0**3
ax.plot(r0, M2,        color='k', lw=1.8, ls='-',            zorder=6, label='$r=2M$')
ax.plot(r0, 1.5*M2,    color='k', lw=1.4, ls='-.',           zorder=6, label='$r=3M$')
ax.plot(r0, -np.cbrt(M2), color='k', lw=1.6, ls=(0,(7,4)),   zorder=6,
        label='$r=(-2M)^{1/3}$  — THE COMOVING TURNAROUND')
ax.plot([], [], color='k', lw=2.0, ls=':', label='horizons  $g(r)=g(r_0)$')
ax.plot([], [], color='0.80', lw=8, label='$f<0$  — inside a horizon, signature flipped')

# --- THE CRITICAL POINTS, marked ---
CP = [(0.0, 0.0, 'de Sitter\n$2M=0$', BLUE),
      (1/S3, 1/S3, 'NARIAI $w{=}30°$\n$r_0=r=1/\\sqrt{3}$\n$r_0$ IS its own horizon', PURPLE),
      (1.0, 0.0, 'chart-tangent $w{=}60°$\n$2M=0$ again', GREEN),
      (2/S3, -1/S3, 'NARIAI $w{=}90°$\nellipse VERTICAL TANGENT', RED)]
for x, y, lab, c in CP:
    ax.plot(x, y, 'o', color=c, ms=11, zorder=9, markeredgecolor='k', markeredgewidth=0.7)
    ax.axvline(x, color=c, lw=1.0, alpha=0.45, zorder=1)
# their mirror images through the origin (the outer Z2: (r0,r) -> (-r0,-r))
for x, y, lab, c in CP:
    if (x, y) != (0.0, 0.0):
        ax.plot(-x, -y, 'o', color=c, ms=7, zorder=8, alpha=0.5)
ax.annotate(CP[1][2], xy=(1/S3, 1/S3), xytext=(-1.45, 1.02), fontsize=8.2, color=PURPLE,
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=0.9))
ax.annotate(CP[3][2], xy=(2/S3, -1/S3), xytext=(0.30, -1.44), fontsize=8.2, color=RED,
            arrowprops=dict(arrowstyle='->', color=RED, lw=0.9))
ax.annotate(CP[2][2], xy=(1.0, 0.0), xytext=(1.02, 0.62), fontsize=8.2, color=GREEN,
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=0.9))
ax.annotate(CP[0][2], xy=(0, 0), xytext=(-0.75, 0.30), fontsize=8.2, color=BLUE,
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.9))
# where 2M is extremal
ax.plot(1/S3, (1/S3)-(1/S3)**3, 's', color=PURPLE, ms=7, zorder=9)
ax.text(1/S3+0.04, 0.40, '$2M$ MAX $=2/3\\sqrt{3}$', fontsize=7.6, color=PURPLE)

ax.axhline(0, color='k', lw=0.9, zorder=4); ax.axvline(0, color='k', lw=0.9, zorder=4)
ax.set_xlim(-L, L); ax.set_ylim(-L, L)
ax.set_xlabel('$r_0$'); ax.set_ylabel('$r$')
ax.legend(fontsize=8.2, loc='lower left', framealpha=0.94)
ax.set_title("THE FUNDAMENTAL ELLIPSE (Janzen 2012), reproduced — with everything it has.\n"
             "SHADING $=\\operatorname{sign}f$, decoded from the original's pixels: grey $=f<0$, "
             "inside a horizon.", fontsize=10.6)

# =====================================================================
# RIGHT — the slicing geometry
# =====================================================================
axR = fig.add_subplot(gs[0, 1]); axR.set_aspect('equal')
H = lambda dd: 2*np.array([np.cos(np.deg2rad(dd)), np.sin(np.deg2rad(dd))])
COL = {0: PURPLE, 120: RED, 240: BLUE}
th = np.linspace(0, 2*np.pi, 400)
axR.plot(np.cos(th), np.sin(th), color='0.55', lw=2.0, zorder=2)
axR.plot(2*np.cos(th), 2*np.sin(th), color=PURPLE, lw=2.0, alpha=0.75, zorder=1)
for a_, b_ in [(0, 120), (120, 240), (240, 0)]:
    A, B = H(a_), H(b_); M = (A + B)/2
    axR.plot([A[0], M[0]], [A[1], M[1]], color=COL[a_], lw=3.6, zorder=3)
    axR.plot([M[0], B[0]], [M[1], B[1]], color=COL[b_], lw=3.6, zorder=3)
    axR.plot(*M, 'o', color=PURPLE, ms=9, zorder=6)
for dd in (0, 120, 240):
    axR.plot(*H(dd), 'D', color=COL[dd], ms=16, zorder=7, markeredgecolor='k', markeredgewidth=0.8)
A = H(0)
for i, (K, P) in enumerate([(np.array([0.8, .6]), np.array([0., 1.])),
                            (np.array([0.8, -.6]), np.array([0., -1.])),
                            (np.array([1., 0.]), np.array([-1., 0.]))]):
    lw = 3.0 if i == 2 else 2.0
    axR.plot([A[0], K[0]], [A[1], K[1]], color=PURPLE, lw=lw, zorder=4)
    axR.plot([K[0], P[0]], [K[1], P[1]], color=PURPLE, lw=lw, ls=(0, (3, 3)), zorder=4)
    dd = (A - K)/np.hypot(*(A - K)); E = A + dd
    axR.plot([A[0], E[0]], [A[1], E[1]], color=PURPLE, lw=lw, zorder=4)
axR.plot([-1, -2.6], [0, 0], color=PURPLE, lw=3.0, ls=(0, (3, 3)), zorder=4)
_t = np.linspace(0, 2*np.pi, 500)
axR.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=2.2, zorder=3)
axR.plot(1 + np.cos(_t), np.sin(_t), color=PURPLE, lw=5.0, alpha=0.32, zorder=2)
axR.plot([2, 2], [-1.75, 1.75], color=PURPLE, lw=2.2, zorder=4)
for sgn in (+1, -1):
    T = np.array([1.0, sgn*1.0]); dd = (T - H(0))/np.hypot(*(T - H(0)))
    axR.plot(*(np.c_[H(0) - dd, H(0) + 3.15*dd]), color=PURPLE, lw=2.0, zorder=4)
    axR.plot(*T, 'o', color=PURPLE, ms=9, zorder=8)
    axR.plot([0, -1], [sgn*1.0, 0], color=PURPLE, lw=2.4, zorder=4)
axR.plot(-1, 0, 'D', color=PURPLE, ms=15, zorder=9, markerfacecolor='none', markeredgewidth=2.2)

MARK = [((-1., 0.), '$r=0$ — the BACK\nchirality flips', 'k'),
        ((0.5, .866), 'tangent $\\beta{=}60°$', PURPLE), ((0.5, -.866), '', PURPLE),
        ((0.8, .6), 'THE PIN $36.87°$\n$\\arctan(3/4)$ — RATIONAL', GOLD), ((0.8, -.6), '', GOLD),
        ((0., 1.), 'pole', GREEN), ((0., -1.), '', GREEN),
        ((1., 0.), 'front', '0.3')]
for P, lab, c in MARK:
    axR.plot(*P, 'o', color=c, ms=6, zorder=10)
    if lab:
        axR.annotate(lab, xy=P, xytext=(P[0] + (0.32 if P[0] > -0.5 else -0.95), P[1] + 0.34),
                     fontsize=8.0, color=c, arrowprops=dict(arrowstyle='-', color=c, lw=0.8))
axR.set_xlim(-3.35, 3.75); axR.set_ylim(-3.05, 3.05); axR.axis('off')
axR.set_title("THE SLICING GEOMETRY — $\\tt p3\\_overhead.py$, from its own code.\n"
              "Equator $\\alpha$ · hinges $2\\alpha$ · sides tangent at midpoints · "
              "Thales circle = the dial's track.", fontsize=10.6)

fig.suptitle("The 2012 fundamental ellipse and the slicing geometry — combined.    "
             "The shading is $\\operatorname{sign} f$; the turnaround $(-2M)^{1/3}$ has been on the page since 2012.",
             fontsize=13, y=0.965)
plt.savefig('fund_ellipse_combined.pdf', bbox_inches='tight')
plt.savefig('fund_ellipse_combined.png', dpi=150, bbox_inches='tight')
print("wrote fund_ellipse_combined.pdf / .png")

print()
print("="*80)
print("WHAT THE 2012 FIGURE HAS THAT P3's fig6 DOES NOT")
print("="*80)
for nm, has in [("the shading = sign f (the causal structure of the WHOLE family)", "2012 ONLY"),
                ("r = 2M   (the Schwarzschild radius across the family)", "2012 ONLY"),
                ("r = 3M   (the photon sphere)", "2012 ONLY"),
                ("r = (-2M)^{1/3}  (THE COMOVING TURNAROUND -- lem:twoturnings' cubic)", "2012 ONLY"),
                ("the horizon locus: line r=r0 + ellipse", "both"),
                ("the Nariai vertical tangents", "both")]:
    print(f"  {nm:<62} {has}")
print()
print("  >> ** P3's fig6 IS THE 2012 FIGURE WITH THE PHYSICS TAKEN OUT. **")
print()
print("="*80)
print("THE CRITICAL POINTS, AND WHAT THE TURNAROUND CURVE DOES AT THEM")
print("="*80)
print(f"  {'w':>4} {'r0':>9} {'2M':>9} {'3M':>9} {'(-2M)^(1/3)':>13}   note")
for w in (0, 30, 60, 90):
    x = (2/S3)*np.sin(np.radians(w)); m2 = x - x**3
    tw = -np.cbrt(m2)
    note = {0: 'de Sitter', 30: 'NARIAI — 2M max', 60: 'chart-tangent — 2M=0 again', 90: 'NARIAI M<0'}[w]
    print(f"  {w:>4} {x:>9.5f} {m2:>9.5f} {1.5*m2:>9.5f} {tw:>13.5f}   {note}")
print()
print("  ** AND THE BRIDGE, NOW PLOTTABLE: ** at Nariai, rho = 1/sqrt3 = 0.57735 is the")
print("  DOUBLE ROOT (the seam), and the turnaround amplitude is A = (2M)^{1/3} =")
print(f"  {np.cbrt(2/(3*S3)):.5f} = cbrt(2) x rho = {np.cbrt(2)*(1/S3):.5f}.")
print("  ** The dotted ellipse carries rho. The long-dash curve carries A. The cbrt(2) is")
print("     the VERTICAL GAP BETWEEN THEM AT THE NARIAI ORDINATE -- one_to_two.py's")
print("     'named, unrun' metric bridge, and it has been drawable on this figure since 2012. **")
