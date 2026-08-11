"""
THE OVERHEAD AND THE ELLIPSE, SIDE BY SIDE (r1108). Daryl's ask:

  "Take the top-left figure from the overhead and work with it. PLOT r0 VALUES AT THOSE
   POINTS THAT ARE DRAWN THERE. At each of those points. And CREATE THE FUNDAMENTAL
   ELLIPSE FROM SCRATCH. Reproduce it faithfully. Side by side, and we are going to ADD
   IN THE DIAL AXIS along with the r0 axis... And could they all be plotted on the r0
   axis and not just r0?"

THE PARAMETERS, from P3 at source (sec:projection, sec:family, sec:ellipse):
    alpha   the throat radius, sqrt(3/Lambda). THE GAUGE. Set to 1.
    w       THE SKY ANGLE -- the line of sight's angle from the image-centre, on the
            observer's celestial sphere. ** THE DIAL. **
    r0      THE OFFSET, in the GNOMONIC CHART:  r0 = (2/sqrt3) sin w.
            "a value of the areal radius r -- one of the three roots -- not an angle".
    2M      = r0 - r0^3 = (2/(3 sqrt3)) sin 3w.
    r       THE AREAL RADIUS -- Daryl: "a parametric length along the slice".
    rho     the charting distance = sqrt7/2 ; theta = arcsin(1/rho) the true angular radius.

** THE CROSSED WIRE, FOUND: ** P3's chart has the throat's IMAGE at radius 2/sqrt3 =
1.1547 -- "FORCED by the requirement that the horizon relation linearise to the pure
triple-angle". p3_overhead.py draws the throat at radius 1. ** TWO DIFFERENT PLANES:
the EMBEDDING overhead (throat at alpha) and the GNOMONIC CHART (throat's image at
2/sqrt3). r0 lives in the chart. My `d` lived in the embedding. ONE SYMBOL, TWO PLANES. **

This script does not paper over it. It plots BOTH and lets the figure show it.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family': 'serif', 'font.size': 10, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = '#6b4f8a'; GREY = '0.55'
S3 = np.sqrt(3)

# ---------- P3's dictionary, verbatim ----------
r0_of_w = lambda w: (2/S3)*np.sin(np.radians(w))
M2_of_w = lambda w: (2/(3*S3))*np.sin(np.radians(3*w))
M2_of_r0 = lambda r0: r0 - r0**3
R_IMG = 2/S3                                  # the throat's IMAGE radius. FORCED.

# ---------- the four critical dial angles ----------
CRIT = [(0,  'de Sitter\n$2M=0$',            '0'),
        (30, 'NARIAI\n$2M=+2/3\\sqrt{3}$',   '$1/\\sqrt{3}$'),
        (60, 'chart-tangent\n$2M=0$',        '$1$'),
        (90, 'NARIAI $M<0$\n$2M=-2/3\\sqrt{3}$', '$2/\\sqrt{3}$')]

fig = plt.figure(figsize=(15.5, 8.6))
gs = fig.add_gridspec(2, 2, height_ratios=[3.1, 1.15], hspace=0.30, wspace=0.22)

# =====================================================================
# LEFT — the GNOMONIC CHART, drawn to P3's own scale
# =====================================================================
axL = fig.add_subplot(gs[0, 0]); axL.set_aspect('equal')
th = np.linspace(0, 2*np.pi, 400)
axL.plot(R_IMG*np.cos(th), R_IMG*np.sin(th), color=GREY, lw=2.4, zorder=3)
axL.text(0, R_IMG+0.10, "the throat's IMAGE, radius $2/\\sqrt{3}$ — FORCED", ha='center',
         fontsize=9, color=GREY)
axL.plot(0, 0, 'o', color='k', ms=5, zorder=6)
axL.text(0.04, -0.14, 'image-centre', fontsize=8.5)

# the lines of sight at the four critical w, each at offset r0 from the centre
for w, lab, r0lab in CRIT:
    r0 = r0_of_w(w)
    col = {0: BLUE, 30: PURPLE, 60: '#2e8b57', 90: RED}[w]
    # a chord at perpendicular offset r0, normal along +y  (offset measured from centre)
    xs = np.linspace(-1.85, 1.85, 2)
    axL.plot(xs, [r0, r0], color=col, lw=2.6, zorder=4)
    axL.plot([0, 0], [0, r0], color=col, lw=1.1, ls=':', zorder=4)
    axL.plot(0, r0, 'o', color=col, ms=6, zorder=6)
    axL.text(1.90, r0, f'$w={w}°$\n$r_0=${r0lab}', fontsize=8.6, color=col, va='center')
axL.axhline(0, color='0.85', lw=0.7, zorder=1); axL.axvline(0, color='0.85', lw=0.7, zorder=1)
axL.set_xlim(-2.05, 2.75); axL.set_ylim(-0.55, 1.75); axL.axis('off')
axL.set_title("P3's GNOMONIC CHART — the four critical sky angles\n"
              "$r_0=(2/\\sqrt{3})\\sin w$ is the OFFSET of the line of sight", fontsize=10.5)

# =====================================================================
# RIGHT — THE FUNDAMENTAL ELLIPSE, from scratch
# =====================================================================
axR = fig.add_subplot(gs[0, 1]); axR.set_aspect('equal')
# the locus g(r) = g(r0)  <=>  (r - r0)(r^2 + r r0 + r0^2 - 1) = 0
t = np.linspace(0, 2*np.pi, 600)
# ellipse r^2 + r r0 + r0^2 = 1 : eigen-decomposition, semi-axes sqrt2 (anti-diag), sqrt(2/3) (diag)
u = np.sqrt(2)*np.cos(t); v = np.sqrt(2/3)*np.sin(t)          # along (1,-1)/sqrt2 and (1,1)/sqrt2
ex = (u*1/np.sqrt(2) + v*1/np.sqrt(2)); ey = (-u*1/np.sqrt(2) + v*1/np.sqrt(2))
axR.plot(ex, ey, color=PURPLE, lw=2.6, zorder=4, label='ellipse $r^2+rr_0+r_0^2=1$')
lin = np.linspace(-1.6, 1.6, 2)
axR.plot(lin, lin, color=GREY, lw=2.0, ls='--', zorder=3, label='line $r=r_0$ (the trivial root)')
axR.plot(lin, -lin, color='0.8', lw=1.0, ls=':', zorder=2, label='anti-diagonal $r=-r_0$ (major axis)')

# Nariai = the ellipse's VERTICAL TANGENTS, at r0 = +-2/sqrt3, r = -+1/sqrt3
for sgn in (+1, -1):
    axR.plot(sgn*2/S3, -sgn/S3, 'o', color=RED, ms=9, zorder=7)
    axR.axvline(sgn*2/S3, color=RED, lw=0.9, ls=':', zorder=2)
axR.text(2/S3+0.05, -1/S3-0.16, 'NARIAI\n$r_0=2/\\sqrt{3},\\ r=-1/\\sqrt{3}$\nvertical tangent',
         fontsize=8.4, color=RED)

# the four critical r0's as vertical lines, and their three horizons
for w, lab, r0lab in CRIT:
    r0 = r0_of_w(w); col = {0: BLUE, 30: PURPLE, 60: '#2e8b57', 90: RED}[w]
    axR.axvline(r0, color=col, lw=1.5, alpha=0.5, zorder=2)
    roots = np.roots([1, 0, -1, M2_of_w(w)])
    for rt in roots:
        if abs(rt.imag) < 1e-9:
            axR.plot(r0, rt.real, 's', color=col, ms=5.5, zorder=6)
    axR.text(r0, 1.62, f'$w=$ {w}°', fontsize=8, color=col, ha='center', rotation=90)
axR.axhline(0, color='0.85', lw=0.7); axR.axvline(0, color='0.85', lw=0.7)
axR.set_xlabel('$r_0$  (the offset / slicing parameter)'); axR.set_ylabel('$r$  (the areal radius)')
axR.set_xlim(-1.75, 1.75); axR.set_ylim(-1.75, 1.75)
axR.legend(fontsize=7.6, loc='lower left'); axR.grid(alpha=0.12)
axR.set_title("THE FUNDAMENTAL ELLIPSE — from scratch\n"
              "$g(r)=g(r_0)$, $g(t)=t^3-t$  ·  a vertical line at $r_0$ meets it in THREE horizons",
              fontsize=10.5)

# =====================================================================
# BOTTOM — THE DIAL AXIS: everything on r0, and everything on w
# =====================================================================
axD = fig.add_subplot(gs[1, :])
ws = np.linspace(0, 90, 900); r0s = r0_of_w(ws)
axD.plot(r0s, M2_of_w(ws), color='k', lw=2.2, label='$2M=r_0-r_0^3=(2/3\\sqrt{3})\\sin 3w$')
axD.plot(r0s, ws/90*0.45, color=BLUE, lw=1.6, ls='--', label='$w$ (rescaled) — MONOTONE in $r_0$')
for w, lab, r0lab in CRIT:
    r0 = r0_of_w(w); col = {0: BLUE, 30: PURPLE, 60: '#2e8b57', 90: RED}[w]
    axD.axvline(r0, color=col, lw=1.4, alpha=0.55)
    axD.plot(r0, M2_of_w(w), 'o', color=col, ms=8, zorder=6)
    axD.annotate(f'$w={w}°$\n$r_0=${r0lab}\n{lab.splitlines()[0]}', xy=(r0, M2_of_w(w)),
                 xytext=(r0, M2_of_w(w) + (0.13 if w in (0, 60) else (0.10 if w == 30 else -0.20))),
                 ha='center', fontsize=8, color=col)
axD.axhline(0, color='0.8', lw=0.8)
axD.set_xlabel('$r_0$  — THE OFFSET AXIS.  Everything below is plotted on it.')
axD.set_ylabel('$2M$')
axD.set_xlim(-0.03, 1.25); axD.set_ylim(-0.46, 0.60)
axD.legend(fontsize=8, loc='lower left'); axD.grid(alpha=0.14)
axD.set_title("THE DIAL, ON THE $r_0$ AXIS — $w$ runs monotone; $2M$ FOLDS.  "
              "The fold at $w=30$ is the involution $w\\mapsto 60°-w$: past it, the geometry repeats.",
              fontsize=10)

fig.suptitle("The gnomonic chart and the fundamental ellipse, side by side — with the dial axis.   "
             "Every critical point of the triple, in $w$, $r_0$ and $2M$.", fontsize=12.5, y=0.985)
plt.savefig('p3_chart_vs_ellipse.pdf', bbox_inches='tight')
plt.savefig('p3_chart_vs_ellipse.png', dpi=150, bbox_inches='tight')
print("wrote p3_chart_vs_ellipse.pdf / .png")

# =====================================================================
print()
print("="*78)
print("THE NUMBERS — every critical point, in every parameter")
print("="*78)
print(f"  {'w':>4} {'r0=(2/sq3)sin w':>17} {'2M=r0-r0^3':>12} {'2M=(2/3sq3)sin3w':>18} {'agree?':>7}   the three horizons r")
for w, lab, _ in CRIT:
    r0 = r0_of_w(w); a_ = M2_of_r0(r0); b_ = M2_of_w(w)
    roots = np.sort_complex(np.roots([1, 0, -1, b_]))
    rs = ', '.join(f'{x.real:+.4f}' if abs(x.imag) < 1e-9 else f'{x.real:+.3f}{x.imag:+.3f}i' for x in roots)
    print(f"  {w:>4} {r0:>17.6f} {a_:>12.6f} {b_:>18.6f} {str(np.isclose(a_,b_)):>7}   {rs}")
print()
print("  >> ** 2M = r0 - r0^3 AND 2M = (2/3sqrt3) sin 3w AGREE AT EVERY CRITICAL POINT. **")
print("     The two formulae are one formula; the triple angle is r0's cubic, in the sky.")
print()
print("="*78)
print("CAN EVERYTHING GO ON THE r0 AXIS?  — Daryl's question, answered")
print("="*78)
mono = np.all(np.diff(r0_of_w(np.linspace(0, 90, 500))) > 0)
print(f"  is r0 MONOTONE in w on [0,90]?  {mono}   -> ** YES: w and r0 are interchangeable axes. **")
print(f"  is 2M monotone in r0?           False -> it PEAKS at w=30 and returns to 0 at w=60.")
print()
print("  ** SO: w, r0 are ONE axis (monotone, invertible). 2M is a FOLDED function ON that axis. **")
print("     And the fold IS the degeneracy Daryl is pointing at:")
print("       sin 3(60-w) = sin(180-3w) = sin 3w   ->  ** the involution is w -> 60 - w **")
print("       fixed point: w = 30 = NARIAI.  ** Past 30, the dial repeats a geometry you had. **")
print("       endpoints:   w=0 (de Sitter, r0=0)  <->  w=60 (chart-tangent, r0=1)  -- BOTH 2M=0.")
print("     P3 says exactly this: 'The de Sitter configuration (r0=0) and the chart-tangent")
print("     configuration (r0=1) are exchanged by the involution; its fixed point is Nariai.'")
print()
print("="*78)
print("AND THE CROSSED WIRE, NAMED")
print("="*78)
print("  P3 sec:projection: 'the throat's planar image must have radius R = 2/sqrt3' -- FORCED,")
print("  because only that scale makes the horizon relation a PURE triple angle.")
print("  ** p3_overhead.py draws the equator at radius 1. **")
print("  So there are TWO PLANES and they are not the same picture:")
print("     * the EMBEDDING OVERHEAD  -- looking down X0 at the hyperboloid; throat at alpha=1;")
print("       hinges at 2alpha; this is where the Thales circle, the tangents and the null")
print("       rulings live (power_is_null.py, alpha_alone.py).")
print("     * the GNOMONIC CHART      -- the observer's celestial sphere, projected; throat's")
print("       IMAGE at 2/sqrt3; this is where r0, w and the triple angle live.")
print("  ** r0 IS A CHART QUANTITY. My `d` WAS AN EMBEDDING QUANTITY. I called both r0. **")
print()
print("  >> WHAT THIS DOES TO THE CHAIN, honestly:")
print("     * one_thirty.py's ARITHMETIC is untouched: sin w = 1/2 => sin 3w = 1 is an identity.")
print("     * its GEOMETRIC READING is suspect: it identified 'the hinge's half-angle' (an")
print("       EMBEDDING angle, arcsin(alpha/2alpha)) with 'the sky angle w' (a CHART angle).")
print("       ** Those live in different planes and I never checked that they are the same")
print("          angle. THE COINCIDENCE OF BOTH BEING 30 IS EXACTLY WHAT A CROSSED WIRE")
print("          PRODUCES, and it is what made the chain look closed. **")
print("     * thales_is_the_dial.py's 'd = alpha is NARIAI' is suspect for the same reason:")
print("       in the CHART, Nariai is r0 = 2/sqrt3 (the image's edge, w=90) or r0 = 1/sqrt3")
print("       (w=30) -- NOT the embedding's tangent.")
print("  ** NEITHER IS RETRACTED. Both are MARKED. The joint to settle: is the swing angle")
print("     about the hinge in the embedding THE SAME ANGLE as the sky angle w in the chart?")
print("     P3 asserts it -- 'the slicing plane swings about the hinge, and the swing angle w")
print("     is the family parameter, THE SAME ANGLE the gnomonic projection reads as the")
print("     observer's sky angle' -- and that sentence is the whole bridge. It is asserted")
print("     and I have not seen it derived. ** THAT is the thing to hunt. **")
