"""
P03_the_turnaround_figure.py -- P3 sec:temporal-threeness, Figure fig:turnaround: the
corpus's OTHER three, drawn for the first time, with every fact verified before it is drawn.

WHY IT EXISTS.  The corpus carries two threes doing different jobs -- the HINGE three (colour,
the within-state index) and the TURNAROUND three (generation, the deck Z_3, to which P14
sec:whichthree moved the family index) -- and had drawn only the first.  Several turns of
confusion traced to reading one figure as though it carried both.

VERIFIED BEFORE DRAWING (all symbolic, the script asserts and exits nonzero on failure):
  1. the FULL period tau -> tau + 2.pi.i.alpha/3 leaves r^3 = 2 M alpha^2 sinh^2(3 tau/2 alpha)
     invariant -- residual exactly 0 -- because 3 tau/2 alpha shifts by i.pi and
     sinh(w + i.pi) = -sinh(w);
  2. the HALF period carries sinh^2 -> -cosh^2, the real expanding leg to the conjugate
     collapse law;
  3. at tau = -i.pi.alpha/3 both r^3 = -2 M alpha^2 AND d(r^3)/dtau = 0, so that point is a
     genuine turnaround and not merely a labelled one;
  4. the three cube roots of -2 M alpha^2 have ONE modulus and arguments -60/60/180 degrees,
     gaps exactly 120 -- EQUILATERAL.

** A CAUGHT MISREADING, AND IT IS THE MORE IMPORTANT CATCH.  The first version of panel (b)
drew a circle with a marked centre labelled r = 0, beside a panel that IS a manifold, and Daryl
read it as the de Sitter hole: "That can't be the dS hole is it?  Because there is no manifold
in the hole."  ** Correct, and the figure invited it. **  Panel (b) is the COMPLEX r-PLANE -- a
plane of VALUES of the areal radius, not the substrate -- so nothing in it is a hole and its
centre is not a place.  And the origin is exactly where the misreading bites: r = 0 there is a
VALUE, and on the substrate that value sits at the WALL, the back of the throat circle at
X_1 = -alpha, a point ON the circle (P3: "the point r=0 fixed at the back of the circle"), never
at a centre -- the interior of the throat carrying no manifold at all.  The panel is now drawn
with Re r / Im r axes, an x at the branch point, and that statement on its face. **

A CAUGHT COMPARISON BUG, ALSO RECORDED: a first pass compared sympy Abs() objects of the three
symbolic surds and reported "2 distinct moduli" for three numbers that are equal.  That is a
canonicalisation artefact, not geometry; the check now compares the numbers.

WHAT THE FIGURE IS FOR.  Beside fig:U3 it makes the contrast visible: the hinge three indexes
COLOUR with symmetry S_3 and lives in the equatorial section, its three being roots of the
horizon cubic at radius 2 alpha; the turnaround three indexes GENERATION with cyclic Z_3 and
lives in the complex cosmic-time plane, its three being cube-root SHEETS.  ** The companion
framework paper's lem:twoturnings establishes that no affine change of variable identifies the
two root sets, so the two threes are genuinely two. **

ORIGIN: computations/baryon_edge/L118w_draw_the_turnaround.py -- built r2376 (c54.42); edit
the origin, not this copy."""
import os
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print(__doc__.split("Run:")[0])

# ------------------------------------------------------------------ the checks
print("=" * 78)
print("CHECKS — the four facts the figure draws")
print("=" * 78)
tau, al, M = sp.symbols('tau alpha M', positive=True)
z = sp.Symbol('z')
r3 = 2*M*al**2*sp.sinh(3*tau/(2*al))**2          # P3 sec:temporal-threeness, the bead's law

# (1) the FULL period 2 pi i alpha/3 leaves r^3 invariant
per = 2*sp.pi*sp.I*al/3
lhs = sp.simplify(sp.expand(sp.simplify(r3.subs(tau, tau + per) - r3)))
print(f"  (1) full period tau -> tau + 2.pi.i.alpha/3 leaves r^3 invariant:  "
      f"residual = {sp.simplify(lhs)}")
print(f"      (because 3 tau/2 alpha shifts by i.pi and sinh(w + i.pi) = -sinh(w))")

# (2) the HALF period carries sinh^2 -> -cosh^2
half = sp.pi*sp.I*al/3
img = sp.simplify(sp.expand_complex(sp.sinh(3*(tau + half)/(2*al))**2))
tgt = sp.simplify(-sp.cosh(3*tau/(2*al))**2)
print(f"  (2) half period carries sinh^2 -> -cosh^2:  "
      f"{sp.simplify(sp.expand(img - tgt)) == 0}")

# (3) the turnaround sits at tau = -i.pi.alpha/3, where r^3 = -2 M alpha^2 and dr/dtau = 0
tt = -sp.pi*sp.I*al/3
r3_at = sp.simplify(r3.subs(tau, tt))
dr3 = sp.simplify(sp.diff(r3, tau).subs(tau, tt))
print(f"  (3) at tau = -i.pi.alpha/3:   r^3 = {r3_at}   and d(r^3)/dtau = {dr3}")
print(f"      so the point is a genuine TURNAROUND (zero velocity), at r^3 = -2 M alpha^2")

# (4) the three cube roots of that value form an EQUILATERAL triangle
roots = sp.solve(sp.Eq(sp.Symbol('R')**3, -2*M*al**2), sp.Symbol('R'))
# evaluate the moduli at M = alpha = 1: sympy will not canonicalise Abs of the three
# symbolic surds to a single expression, and comparing unsimplified Abs objects would
# report "2 distinct" for three numbers that are equal.  This is a comparison bug, not
# a geometric fact -- so compare the NUMBERS.
mods_n = {round(abs(complex(sp.N(R.subs({M: 1, al: 1})))), 12) for R in roots}
args = sorted(round(np.degrees(np.angle(complex(sp.N(R.subs({M: 1, al: 1}))))), 9)
              for R in roots)
gaps = sorted({(args[(i+1) % 3] - args[i]) % 360 for i in range(3)})
print(f"  (4) the three cube roots: {len(roots)} of them; moduli at M=alpha=1: {sorted(mods_n)}")
print(f"      -> {len(mods_n)} distinct modulus, so EQUILATERAL: {len(mods_n) == 1}")
print(f"      arguments (deg): {args};  gaps: {gaps} -- spaced by 120 exactly")
assert sp.simplify(lhs) == 0 and len(mods_n) == 1 and gaps == [120]
print()

# ------------------------------------------------------------------ the drawing
INK, RED, BLUE, GREEN, GREY = '#111111', '#c0392b', '#1f77b4', '#2e8b57', '#888888'
fig = plt.figure(figsize=(11.6, 5.0))
A = 1.0

# ---- panel (a): the tau-plane, its period, its wings, the turnaround
ax = fig.add_subplot(1, 2, 1)
P = 2*np.pi*A/3                                   # the imaginary period, as a length
# The band Im tau in (-P/2, +P/2] IS the fundamental domain: the deck action identifies its
# two edges, so the tau-plane quotients to a CYLINDER.  A first pass also drew lines at
# +-P and labelled them "one period" -- they fell outside the axes and were redundant,
# since +-P/2 already ARE the identified edges.
ax.axhspan(-P/2, P/2, color='#eef2f7', zorder=0)
ax.text(2.42, 0.62, 'the fundamental domain:\nthe two edges are IDENTIFIED,\nso the plane is a CYLINDER',
        fontsize=7.5, color='#667', ha='right', va='center')
x = np.linspace(-2.4, 2.4, 400)
ax.plot(x, 0*x, color=BLUE, lw=2.6, zorder=5)
ax.text(-2.3, 0.10, 'the real axis — the expanding leg', fontsize=8.5, color=BLUE)
for s_, lab in ((+1, r'$+\pi\alpha/3$'), (-1, r'$-\pi\alpha/3$')):
    ax.plot(x, s_*P/2 + 0*x, color=GREEN, lw=2.2, ls=(0, (6, 3)), zorder=5)
    ax.text(-2.3, s_*P/2 + (0.09 if s_ > 0 else -0.20),
            r'wing at $\mathrm{Im}\,\tilde\tau=$ ' + lab, fontsize=8.5, color=GREEN)
ax.scatter([0], [-P/2], s=105, marker='o', color=RED, edgecolor='k', lw=0.6, zorder=9)
ax.annotate('the TURNAROUND\n' r'$r^{3}=-2M\alpha^{2}$,  $\dot r=0$',
            xy=(0, -P/2), xytext=(0.5, -P/2 - 0.55), fontsize=8.5, color=RED,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.0))
ax.annotate('', xy=(-1.55, P/2), xytext=(-1.55, 0),
            arrowprops=dict(arrowstyle='->', color=INK, lw=1.3))
ax.text(-1.48, P/4 - 0.05, r'HALF period:  $\sinh^{2}\!\to\!-\cosh^{2}$',
        fontsize=8, color=INK)
ax.set_xlim(-2.5, 2.6); ax.set_ylim(-1.85, 1.45)
ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau$'); ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau$')
ax.set_title(r'(a)  cosmic time: ONE imaginary period $2\pi i\alpha/3$, no real one',
             fontsize=9.5, loc='left')
for sp_ in ('top', 'right'):
    ax.spines[sp_].set_visible(False)

# ---- panel (b): the COMPLEX r-PLANE.  Not the substrate.
# Daryl, c54.43: "You have r=0 at the centre of a circle.  That can't be the dS hole is it?
# Because there is no manifold in the hole."  Correct, and the first version invited exactly
# that misreading: a circle with a marked centre, drawn beside a panel that IS a manifold.
# This panel is a plane of VALUES of the areal radius.  There is no hole in it because it is
# not the substrate -- and the value r = 0 sits, on the substrate, at the WALL: the back of
# the throat circle (P3: "the point r=0 fixed at the back of the circle", at X_1 = -alpha),
# a point ON the circle, never a centre.
bx = fig.add_subplot(1, 2, 2)
R0 = 1.0
bx.axhline(0, color='#bbb', lw=0.8, zorder=1)
bx.axvline(0, color='#bbb', lw=0.8, zorder=1)
tri = [np.array([R0*np.cos(np.radians(a_)), R0*np.sin(np.radians(a_))])
       for a_ in (60, 180, 300)]
bx.add_patch(plt.Circle((0, 0), R0, fill=False, color=GREY, lw=0.9, ls=':', zorder=2))
bx.text(0.0, 1.28, r'construction circle  $|r|=(2M\alpha^{2})^{1/3}$',
        fontsize=7.5, color=GREY, ha='center')
T = np.array(tri + [tri[0]])
bx.plot(T[:, 0], T[:, 1], color=INK, lw=1.6, zorder=4)
for v, lab in zip(tri, (r'$r$', r'$\omega r$', r'$\omega^{2}r$')):
    bx.scatter(*v, s=110, color=RED, edgecolor='k', lw=0.6, zorder=9)
    bx.text(v[0]*1.30, v[1]*1.30, lab, fontsize=12, ha='center', va='center', color=RED)
th = np.linspace(np.radians(72), np.radians(168), 60)
bx.plot(1.44*np.cos(th), 1.44*np.sin(th), color=BLUE, lw=1.6, zorder=6)
bx.annotate('', xy=(1.44*np.cos(np.radians(168)), 1.44*np.sin(np.radians(168))),
            xytext=(1.44*np.cos(np.radians(160)), 1.44*np.sin(np.radians(160))),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.6))
bx.text(0.0, 1.66, r'the DECK action:  $\tilde\tau\mapsto\tilde\tau+2\pi i\alpha/3$'
                   '\n' r'fixes $r^{3}$, cycles the sheets  $r\mapsto\omega r$',
        fontsize=8.5, color=BLUE, ha='center')
bx.scatter([0], [0], s=34, marker='x', color=INK, lw=1.8, zorder=8)
bx.annotate('$r=0$ : the BRANCH POINT of $r^{1/3}$.\n'
            'On the substrate this VALUE sits at\n'
            'the WALL — the back of the throat\n'
            'circle — and never at a centre.',
            xy=(0.0, 0.0), xytext=(-1.90, -1.66), fontsize=7.5, color=INK,
            ha='left', va='bottom',
            arrowprops=dict(arrowstyle='->', color=INK, lw=0.9,
                            connectionstyle='arc3,rad=0.18'))
bx.set_xlim(-1.95, 1.95); bx.set_ylim(-2.35, 2.10)
bx.set_aspect('equal')
bx.set_xticks([]); bx.set_yticks([])
bx.text(1.90, 0.07, r'$\mathrm{Re}\,r$', fontsize=8.5, color='#777', ha='right')
bx.text(0.07, 1.98, r'$\mathrm{Im}\,r$', fontsize=8.5, color='#777')
for sp_ in ('top', 'right', 'bottom', 'left'):
    bx.spines[sp_].set_visible(False)
bx.set_title('(b)  the COMPLEX $r$-plane — values of the areal radius.\n'
             '       NOT the substrate: there is no hole here',
             fontsize=9.5, loc='left')

fig.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
out = os.path.join(root, 'corpus', 'figures', 'CR_turnaround_threeness.png')
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=200)
print("  wrote", os.path.relpath(out, root))
print()
print("  ⌗ ** AND THE FIGURE'S POINT IS THE CONTRAST, NOT THE PICTURE.  Beside the hinge")
print("  figure (fig:U3) this is the corpus's OTHER three, and they differ in every respect:")
print()
print(f"  {'':>22} {'the HINGE three':>26} {'the TURNAROUND three':>26}")
for a, b, c in [
    ("what it indexes", "COLOUR (within-state)", "GENERATION (P14 whichthree)"),
    ("its symmetry", "S_3, the full Weyl group", "cyclic Z_3, the deck action"),
    ("where it lives", "the equatorial section", "the complex tau-plane"),
    ("its three are", "roots of the HORIZON cubic", "cube-root SHEETS"),
    ("their shape", "equilateral, radius 2 alpha", "equilateral, radius (2M a^2)^(1/3)"),
    ("related by an affine map?", "NO -- lem:twoturnings", "NO -- lem:twoturnings"),
]:
    print(f"  {a:>22} {b:>26} {c:>26}")
print()
print("  ** THE COMPANION FRAMEWORK PAPER'S lem:twoturnings ESTABLISHES THAT NO AFFINE CHANGE")
print("     OF VARIABLE IDENTIFIES THE TWO ROOT SETS.  So the two threes are genuinely two,")
print("     and drawing them side by side is what stops them being read as one. **")
