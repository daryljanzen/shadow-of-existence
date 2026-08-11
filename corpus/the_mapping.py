"""
THE MAPPING (r1108) — every point of note on the slicing chart, carried to the (r0, r) plane.

THE DICTIONARY, and it is the thing the figure is for:
  * a SLICING LINE through the hinge, at perpendicular offset D from the centre,
    maps to a VERTICAL LINE at r0 in the (r0,r) plane.
  * where that line CUTS THE EQUATOR are horizons; they map to where the vertical line
    meets the locus g(r)=g(r0)  =  the diagonal r=r0  and  the ellipse r^2+rr0+r0^2=1.
  * P3 fixes r=0 at the BACK of the circle.

** THE OPEN JOINT, MARKED NOT HIDDEN: ** what is r0 in terms of the overhead's offset D?
    reading A:  r0 = D          -> the TANGENT (D=1) is r0=1, 2M=0, P3's "chart-tangent"
    reading B:  r0 = D/sqrt3    -> the TANGENT (D=1) is r0=1/sqrt3, NARIAI, and then the
                                   overhead's swing angle IS P3's sky angle w, which is
                                   what P3's own sentence asserts.
Both are plotted. The figure shows what each does. I am not choosing by preference.

THE POINTS OF NOTE, all of them:
  the BACK (-1,0)          r=0. Chirality flips. ALSO a tangent point of the hinge triangle.
  THE PIN (4/5, 3/5)       ** THE PYTHAGOREAN POINT ** -- 3-4-5, the only RATIONAL point in
                           a figure of surds. On the throat, which IS the de Sitter horizon.
  the POLE (0,1)           where the arctan(1/2) line ends. Also on the dS horizon.
  tangent pts (1/2,+-r3/2) where the hinge triangle touches. beta = 60, 300.
  the front (1,0)          chord from the back = 2 = THE DIAMETER (Daryl's fold).
  the hinge (2,0)          the observer. X0 = sqrt3 alpha. power 3 alpha^2.
  Thales top/bottom (1,+-1) where the 45-degree lines touch the Thales circle.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams.update({'font.family': 'serif', 'font.size': 10.5, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
S3 = np.sqrt(3); GOLD = '#d4a017'; GREEN = '#2e8b57'; ORANGE = '#e07b39'
H = np.array([2.0, 0.0])

# ---------------- the lines of note: (name, angle at hinge, colour) ----------------
LINES = [('through the centre — the axis',       0.0,            BLUE),
         ('NARIAI line  ($\\sin\\theta=1/2\\sqrt{3}$)', np.degrees(np.arcsin(1/(2*S3))), PURPLE),
         ('THE PIN LINE $\\arctan(1/2)$',        np.degrees(np.arctan2(1, 2)), GOLD),
         ('THE TANGENT — touches the throat',    30.0,           GREEN),
         ('the $45°$ line',                      45.0,           ORANGE),
         ('the VERTICAL — the dial\'s end',      90.0,           RED)]

print("="*100)
print("THE LINES, AND WHERE THEY LAND UNDER EACH READING")
print("="*100)
print(f"  {'line':<40} {'θ':>7} {'D=2sinθ':>9} | {'A: r0=D':>8} {'2M':>8} | {'B: r0=D/√3':>11} {'2M':>8}")
rows = []
for nm, th, c in LINES:
    D = 2*np.sin(np.radians(th))
    rA, rB = D, D/S3
    mA, mB = rA - rA**3, rB - rB**3
    rows.append((nm, th, D, rA, mA, rB, mB, c))
    print(f"  {nm.replace('$','').replace('\\\\','')[:40]:<40} {th:>7.3f} {D:>9.5f} | "
          f"{rA:>8.5f} {mA:>8.5f} | {rB:>11.5f} {mB:>8.5f}")

fig = plt.figure(figsize=(19, 9.6))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1], wspace=0.13)

# =====================================================================
# LEFT — the slicing chart, SAME SPAN as the ellipse
# =====================================================================
ax = fig.add_subplot(gs[0, 0]); ax.set_aspect('equal')
th_ = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(th_), np.sin(th_), color='0.35', lw=2.6, zorder=3)
ax.text(0, 1.06, 'THE THROAT $r=\\alpha$  —  **IS** THE DE SITTER HORIZON', ha='center',
        fontsize=8.6, color='0.3')
ax.plot(0, 0, '+', color='0.4', ms=9, zorder=3)

# the slicing lines
for nm, thd, D, rA, mA, rB, mB, c in rows:
    a = np.radians(thd)
    d = np.array([-np.cos(a), np.sin(a)])            # from the hinge, into the field
    P = H + np.linspace(-0.9, 3.6, 2)[:, None]*d
    ax.plot(P[:, 0], P[:, 1], color=c, lw=2.0, alpha=0.9, zorder=4)
    # its perpendicular foot (the offset)
    t = -(H @ d); F = H + t*d
    ax.plot([0, F[0]], [0, F[1]], color=c, lw=0.9, ls=':', zorder=4)
    ax.plot(*F, 'o', color=c, ms=4.5, zorder=6)
ax.plot(*H, 'D', color=PURPLE, ms=15, zorder=9, markeredgecolor='k', markeredgewidth=0.8)
ax.text(2.02, -0.20, 'THE HINGE\n$2\\alpha$ · $X_0{=}\\sqrt{3}\\alpha$\npower $3\\alpha^2$',
        fontsize=8, color=PURPLE)

# the Thales circle
ax.plot(1 + np.cos(th_), np.sin(th_), color=PURPLE, lw=1.6, alpha=0.75, zorder=2)
ax.text(1.0, -1.22, 'the THALES circle = the dial\'s track', fontsize=7.6, color=PURPLE, ha='center')

# ---- THE POINTS OF NOTE ----
PTS = [((-1., 0.),   '$r=0$ — THE BACK\nchirality flips\n(also a tangent pt)', 'k',    9),
       ((0.8, 0.6),  'THE PIN  $(4/5,\\,3/5)$\n** THE PYTHAGOREAN POINT **\nthe only RATIONAL point', GOLD, 10),
       ((0.8, -0.6), '', GOLD, 8),
       ((0., 1.),    'the POLE $(0,1)$', GREEN, 8),
       ((0., -1.),   '', GREEN, 8),
       ((0.5, 0.866),'tangent pt $(\\frac{1}{2},\\frac{\\sqrt{3}}{2})$', PURPLE, 8),
       ((0.5, -0.866),'', PURPLE, 8),
       ((1., 0.),    'the front — chord from back $=2$\n(the DIAMETER: Daryl\'s fold)', '0.35', 8)]
for P, lab, c, ms in PTS:
    ax.plot(*P, 'o', color=c, ms=ms, zorder=10, markeredgecolor='k', markeredgewidth=0.5)
    if lab:
        dx = 0.34 if P[0] > -0.4 else -1.30
        ax.annotate(lab, xy=P, xytext=(P[0]+dx, P[1]+0.30), fontsize=7.6, color=c,
                    arrowprops=dict(arrowstyle='-', color=c, lw=0.7))
ax.set_xlim(-1.55, 2.55); ax.set_ylim(-1.55, 1.65)
ax.set_xlabel('the overhead — offsets $D$ measured from the centre'); ax.set_yticks([])
ax.set_title("THE SLICING GEOMETRY — every point of note.\n"
             "The throat is $r=\\alpha$, and $r=\\alpha$ IS the de Sitter horizon.", fontsize=11)

# =====================================================================
# RIGHT — the (r0, r) plane, SAME SPAN
# =====================================================================
axE = fig.add_subplot(gs[0, 1]); axE.set_aspect('equal')
L = 1.55; n = 700
R0g, Rg = np.meshgrid(np.linspace(-L, L, n), np.linspace(-L, L, n))
with np.errstate(divide='ignore', invalid='ignore'):
    fg = 1 - (R0g - R0g**3)/Rg - Rg**2
axE.contourf(R0g, Rg, (fg < 0).astype(float), levels=[.5, 1.5], colors=['0.83'], zorder=0)
t = np.linspace(0, 2*np.pi, 800)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
axE.plot((u+v)/np.sqrt(2), (-u+v)/np.sqrt(2), color='k', lw=2.0, ls=':', zorder=5)
dd = np.linspace(-L, L, 2); axE.plot(dd, dd, color='k', lw=2.0, ls=':', zorder=5)
r0c = np.linspace(-L, L, 700); M2c = r0c - r0c**3
axE.plot(r0c, M2c, color='k', lw=1.7, zorder=6)
axE.plot(r0c, -np.cbrt(M2c), color='k', lw=1.5, ls=(0, (7, 4)), zorder=6)
axE.text(-1.5, 1.36, '$r{=}2M$ (solid) · $r{=}(-2M)^{1/3}$ (dashed)\nhorizons (dotted) · grey $=f{<}0$',
         fontsize=7.6)

# ---- THE LINES, MAPPED OVER, under BOTH readings ----
for nm, thd, D, rA, mA, rB, mB, c in rows:
    # reading B (solid) : r0 = D/sqrt3
    axE.axvline(rB, color=c, lw=2.0, alpha=0.85, zorder=3)
    for rt in np.roots([1, 0, -1, mB]):
        if abs(rt.imag) < 1e-9:
            axE.plot(rB, rt.real, 'o', color=c, ms=7.5, zorder=8, markeredgecolor='k', markeredgewidth=0.5)
    # reading A (faint dashed) : r0 = D
    if rA <= L:
        axE.axvline(rA, color=c, lw=1.2, ls='--', alpha=0.35, zorder=2)
axE.plot([], [], color='0.3', lw=2.0, label='reading B: $r_0=D/\\sqrt{3}$  (solid) — makes $\\theta=w$')
axE.plot([], [], color='0.3', lw=1.2, ls='--', alpha=0.5, label='reading A: $r_0=D$  (dashed)')

# the two Nariai points
for sgn in (+1, -1):
    axE.plot(sgn*2/S3, -sgn/S3, '*', color=RED, ms=15, zorder=9)
axE.text(1.17, -0.52, 'NARIAI\n$(2/\\sqrt{3},-1/\\sqrt{3})$', fontsize=7.4, color=RED)
axE.text(-1.5, -1.45, 'de Sitter: $r_0{=}0$ and $r_0{=}1$\nboth $2M{=}0$; horizons $-1,0,+1$', fontsize=7.4)
axE.axhline(0, color='k', lw=0.8); axE.axvline(0, color='k', lw=0.8)
axE.set_xlim(-L, L); axE.set_ylim(-L, L)
axE.set_xlabel('$r_0$'); axE.set_ylabel('$r$')
axE.legend(fontsize=7.4, loc='lower right', framealpha=0.95)
axE.set_title("THE $(r_0,r)$ PLANE — each slicing line is a VERTICAL LINE at its $r_0$;\n"
              "its horizons are where that line meets the locus.", fontsize=11)

fig.suptitle("The mapping: every slicing line ↦ a vertical line at $r_0$; every horizon ↦ an intersection.   "
             "Colour-coded across, at matched scale.", fontsize=12.5, y=0.975)
plt.savefig('the_mapping.pdf', bbox_inches='tight'); plt.savefig('the_mapping.png', dpi=150, bbox_inches='tight')
print("\nwrote the_mapping.pdf / .png")
print()
print("="*100)
print("WHICH READING? — the discriminator P3 itself supplies")
print("="*100)
print("  P3: 'the slicing plane swings about the hinge, and THE SWING ANGLE w IS THE FAMILY")
print("  PARAMETER -- THE SAME ANGLE the gnomonic projection reads as the observer's sky angle.'")
print()
print(f"  {'θ (overhead swing)':>20} {'D=2sinθ':>9} {'B: r0=D/√3':>11} {'w from r0=(2/√3)sin w':>22}  θ=w?")
for nm, th, c in LINES:
    D = 2*np.sin(np.radians(th)); rB = D/S3
    w = np.degrees(np.arcsin(np.clip(rB*S3/2, -1, 1)))
    print(f"  {th:>20.3f} {D:>9.5f} {rB:>11.5f} {w:>22.3f}  {np.isclose(th, w)}")
print()
print("  >> ** READING B GIVES θ = w EXACTLY, AT EVERY LINE. ** That is P3's own sentence,")
print("     satisfied identically. Reading A does not.")
print("  >> AND THEN: the TANGENT (θ=30) is r0 = 1/√3 = NARIAI -- which is what")
print("     one_thirty.py claimed and I marked SUSPECT. ** Reading B restores ⊢4. **")
print("  >> AND P3's 'chart-tangent (r0=1)' is θ=60, D=√3 -- a line that MISSES the")
print("     overhead's equator entirely. So 'meets the throat at a single point' is NOT a")
print("     tangency in the overhead: it is r0 = α, the cut's radius EQUALLING the throat's.")
print("     ** Two different senses of 'tangent', and that is the crossed wire. **")
