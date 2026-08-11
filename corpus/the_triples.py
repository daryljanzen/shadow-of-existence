"""
THE MAPPING, FROM P3's OWN ANALYTIC RELATION (r1108). No pixels, no invented palette.

prop:triple, verbatim:
  "With r0 = (2/sqrt3) sin w, the horizon relation 2M = r0 - r0^3 is the pure triple-angle
   relation 2M = (2/3sqrt3) sin 3w ... ** THE THREE ROOTS OF THE HORIZON CUBIC ARE THE
   THREE PREIMAGES w, pi/3 - w, -pi/3 - w OF 3w UNDER THE SINE. ** The involution is, in
   the sky angle, the reflection w <-> pi/3 - w."

** THE MAPPING: **
   a slicing line at sky angle w (SIGNED -- w<0 is the hinge's LEFT HAND, and r0<0)
      -> offset D = 2 alpha sin w        (plain geometry: |OH| sin w, hinge at 2 alpha)
      -> r0 = D/sqrt3 = (2/sqrt3) sin w  (** P3's own relation **)
   and its THREE HORIZONS are  r_k = (2/sqrt3) sin(theta_k),  theta_k in {w, 60-w, -60-w}.

** AND EACH OF THOSE THREE IS ITSELF THE OFFSET OF A LINE. ** So a triple is THREE LINES
in the overhead, all with the SAME 2M -- because sin3(60-w) = sin(180-3w) = sin 3w and
sin3(-60-w) = sin 3w. ONE GEOMETRY, THREE DESIGNATIONS, and each designation is a line
you can draw. P3: "each geometry is met at several r0-values -- ONE PER ROOT IT MAY
DESIGNATE -- while the swing angle w places each geometry ONCE."

** SO THE THREE r0's OF A TRIPLE *ARE* THE THREE ROOTS. ** That is the colour code:
ONE COLOUR PER TRIPLE. Three lines on the left; three verticals on the right; and every
one of those verticals meets the locus at the SAME three heights.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'cm'})
S3 = np.sqrt(3); RHO = 2/S3
H0 = np.array([2.0, 0.0])
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)

r0_of_w = lambda w: RHO*np.sin(np.radians(w))
M2_of_w = lambda w: (2/(3*S3))*np.sin(np.radians(3*w))
triple   = lambda w: (w, 60.0-w, -60.0-w)          # ** prop:triple **

# ---- THE TRIPLES, one colour each ----
TRIPLES = [(  0.0, '#2471a3', 'DE SITTER'),
           ( 30.0, '#8e44ad', 'NARIAI'),
           (-30.0, '#c0392b', 'NARIAI, $M<0$'),
           ( np.degrees(np.arctan2(1,2)), '#d4a017', 'THE PIN LINE $\\arctan\\frac12$'),
           ( 45.0, '#2e8b57', '$45°$')]

print("="*104)
print("THE TRIPLES — from prop:triple.  theta_k in {w, 60-w, -60-w};  r_k = (2/sqrt3) sin theta_k")
print("="*104)
for w, c, nm in TRIPLES:
    th = triple(w); rs = [r0_of_w(t) for t in th]
    roots = np.sort(np.roots([1, 0, -1, M2_of_w(w)]).real)
    print(f"\n  {nm:<26} w = {w:+8.3f}    2M = {M2_of_w(w):+.5f}")
    print(f"     the three sky angles : {th[0]:+8.3f} {th[1]:+8.3f} {th[2]:+8.3f}")
    print(f"     -> r_k = (2/√3)sinθ  : {rs[0]:+8.5f} {rs[1]:+8.5f} {rs[2]:+8.5f}")
    print(f"     the cubic's roots    : {roots[0]:+8.5f} {roots[1]:+8.5f} {roots[2]:+8.5f}")
    print(f"     SAME SET? {np.allclose(np.sort(rs), roots, atol=1e-9)}    sum = {sum(rs):+.1e}")

fig = plt.figure(figsize=(26, 13.5))
gs = fig.add_gridspec(1, 2, width_ratios=[1.40, 1], wspace=0.08)

# =====================================================================
# LEFT — the overhead. Each triple = THREE LINES, one colour.
# =====================================================================
ax = fig.add_subplot(gs[0, 0]); ax.set_aspect('equal')
th_ = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(th_), np.sin(th_), color='0.5', lw=2.4, zorder=3)             # the throat
ax.plot(2*np.cos(th_), 2*np.sin(th_), color='0.75', lw=1.4, zorder=1)        # the hinge circle
ax.plot(1+np.cos(th_), np.sin(th_), color='0.62', lw=1.8, ls='-', zorder=2)  # the Thales circle
ax.text(1.0, -1.16, 'the THALES circle — the locus of the FEET', fontsize=9, color='0.45', ha='center')
ax.text(0, 1.07, 'THE THROAT $r=\\alpha$', ha='center', fontsize=10, color='0.4', style='italic')
ax.plot(*H0, 'D', color='k', ms=15, zorder=10)
ax.text(2.06, -0.22, 'THE HINGE', fontsize=10)

for w, c, nm in TRIPLES:
    for k, t in enumerate(triple(w)):
        a = np.radians(t)
        d = np.array([-np.cos(a), np.sin(a)])                  # from the hinge into the field
        P = H0 + np.linspace(-1.0, 4.2, 2)[:, None]*d
        ax.plot(P[:, 0], P[:, 1], color=c, lw=2.6 if k == 0 else 1.7,
                alpha=1.0 if k == 0 else 0.62, ls='-' if k == 0 else (0, (6, 3)), zorder=5)
        s = -(H0 @ d); F = H0 + s*d                            # the foot = the horizon
        ax.plot(*F, 'o', color=c, ms=11 if k == 0 else 8, zorder=9,
                markeredgecolor='k', markeredgewidth=0.7)
ax.plot([], [], color='k', lw=2.6, label='the designated line, $w$  (solid)')
ax.plot([], [], color='k', lw=1.7, ls=(0, (6, 3)), label='its two partners, $60°{-}w$ and $-60°{-}w$  (dashed)')
ax.plot([], [], 'o', color='k', ms=8, label='the FEET = the three horizons; they lie on the Thales circle')
ax.legend(fontsize=10, loc='lower left', framealpha=0.95)
ax.set_xlim(-2.9, 3.0); ax.set_ylim(-2.5, 2.5); ax.axis('off')
ax.set_title("THE OVERHEAD — each TRIPLE is THREE LINES through the hinge, at $w$, $60°{-}w$, $-60°{-}w$.\n"
             "All three have the SAME $2M$.  $w<0$ is the hinge's LEFT HAND, and $r_0<0$.", fontsize=14, pad=12)

# =====================================================================
# RIGHT — the (r0, r) plane. Each triple = THREE VERTICALS, same colour.
# =====================================================================
axE = fig.add_subplot(gs[0, 1]); axE.set_aspect('equal')
L = 1.45; n = 700
R0g, Rg = np.meshgrid(np.linspace(-L, L, n), np.linspace(-L, L, n))
with np.errstate(divide='ignore', invalid='ignore'):
    fg = 1 - (R0g - R0g**3)/Rg - Rg**2
axE.contourf(R0g, Rg, (fg < 0).astype(float), levels=[.5, 1.5], colors=['0.87'], zorder=0)
t = np.linspace(0, 2*np.pi, 900)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
axE.plot((u+v)/np.sqrt(2), (-u+v)/np.sqrt(2), color='k', lw=2.0, ls=':', zorder=5)
dd = np.linspace(-L, L, 2); axE.plot(dd, dd, color='k', lw=2.0, ls=':', zorder=5)
axE.text(0.96, 1.16, '$r=r_0$', fontsize=9, color='0.3')

for w, c, nm in TRIPLES:
    rs = [r0_of_w(t) for t in triple(w)]
    for k, rk in enumerate(rs):
        axE.axvline(rk, color=c, lw=2.4 if k == 0 else 1.5,
                    alpha=0.95 if k == 0 else 0.55, ls='-' if k == 0 else (0, (6, 3)), zorder=3)
        for rr in rs:                                    # every vertical meets the SAME three heights
            axE.plot(rk, rr, 'o', color=c, ms=9 if (k == 0) else 6, zorder=8,
                     markeredgecolor='k', markeredgewidth=0.5)
axE.axhline(0, color='k', lw=0.8); axE.axvline(0, color='k', lw=0.8)
axE.set_xlim(-L, L); axE.set_ylim(-L, L)
axE.set_xlabel('$r_0$', fontsize=13); axE.set_ylabel('$r$', fontsize=13)
axE.set_title("THE $(r_0,r)$ PLANE — a triple is THREE VERTICALS, and each meets the locus\n"
              "at the SAME three heights.  ** The three $r_0$'s ARE the three roots. **", fontsize=14, pad=12)

fig.suptitle("The mapping, from $\\tt prop{:}triple$:  the three roots are the three preimages "
             "$w$, $60°{-}w$, $-60°{-}w$ of $3w$ under the sine.   One colour per TRIPLE.",
             fontsize=15.5, y=0.955)
plt.savefig('the_triples.pdf', bbox_inches='tight'); plt.savefig('the_triples.png', dpi=140, bbox_inches='tight')
print("\nwrote the_triples.pdf / .png")
print()
print("="*104)
print("THE THING THAT FALLS OUT — and it is P3's own sentence, drawn")
print("="*104)
print("  P3: 'each geometry is met at SEVERAL r0-VALUES -- ONE PER ROOT IT MAY DESIGNATE --")
print("       while the swing angle w places each geometry ONCE.'")
print()
print("  ** THE THREE r0's OF A TRIPLE ARE THE THREE ROOTS. ** Verified above, every triple.")
print("     So on the right, a triple is three verticals AT the three roots, and each meets")
print("     the locus at those same three heights: a 3x3 lattice, and the diagonal r=r0 picks")
print("     out which root is DESIGNATED.")
print("  ** AND ON THE LEFT, THE THREE FEET ARE THE THREE HORIZONS, AND THEY LIE ON THE")
print("     THALES CIRCLE -- which is why the Thales circle is in the figure at all. **")
print()
print("  AND THE INVOLUTION, w <-> 60-w, IS VISIBLE: w=0 and w=60 are the SAME triple.")
for w in (0.0, 60.0):
    print(f"     w={w:>5.1f}:  r0 = {r0_of_w(w):+.5f}   roots = "
          f"{np.sort([r0_of_w(t) for t in triple(w)]).round(5)}")
print("     ** Same roots. Same geometry. Two designations. That is de Sitter, twice. **")
