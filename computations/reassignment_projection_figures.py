"""
Rendering the reassignment/projection so it can be PICTURED (Daryl's hangup:
"I can picture both spacetimes but not the map between them").

Three panels, all from the corpus's own analytic apparatus:

 (A) THE ONE ANALYTIC EXPANSION, with the two rate-levels marked ON the curve.
     r(tilde-tau) = sinh^{2/3}((3/2) tilde-tau) is one analytic function
     (CR_cosmology eq:scalefac; slicing_operator eq:scalefactor).  The seam
     tilde-tau=0 is a branch point, not an r=0 wall.  The collapse excursion
     (tilde-tau<0, leaf-level, radiation-INCLUDED, BBN) and our expanding
     cosmology (tilde-tau>0, foliation-level, GEOMETRIC, recombination)
     are the two legs of the ONE curve.  This renders the P16 sec:scoping
     decision rule directly on the analytic object.

 (B) THE MAP = TWO SLICINGS OF ONE de SITTER HYPERBOLOID.
     Embedding -X0^2+X1^2+X2^2 = alpha^2 (slicing_operator sec:synchronous,
     sec:trichotomy).  ONE congruence, two synchronizations:
       - CLOSED slices  X0=const  -> the round S^3 ONTOLOGICAL layer (the existent);
       - FLAT slices  eta(X,B)=const, normal to the past null ruling B
         -> the flat-LCDM OBSERVED shadow the E=1 projection reads.
     The past null ruling B is (the common asymptote / big bang /
     antecedent collapse horizon).  This IS the reassignment: not two
     spacetimes, one geometry re-synchronized from the timelike vertical to
     the null ruling.

 (C) THE INVOLUTION sigma (root-exchange), the map's fixed-point structure.
     sigma(r0) = (-r0 + sqrt(4-3 r0^2))/2 (SdS-slicing-curve prop:involution;
     groupoid eq:f): swaps the two positive horizon roots, FIXES Nariai
     r0=1/sqrt3, exchanges endpoints 0<->1.  In the sky angle it is the
     reflection w <-> pi/3 - w about w=pi/6.  The cosmology is its fixed point.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from mpl_toolkits.mplot3d.art3d import Line3DCollection  # noqa

fig = plt.figure(figsize=(16.5, 5.6))

# ---------------------------------------------------------------------------
# (A) the one analytic expansion, rate-levels marked
# ---------------------------------------------------------------------------
axA = fig.add_subplot(1, 3, 1)
tt = np.linspace(-2.2, 2.2, 2000)
# r = sinh^{2/3}(1.5 tt); for tt<0 sinh<0 -> take signed magnitude for the real
# collapse leg (|r|), the conjugate-branch phase is noted in the caption.
s = np.sinh(1.5 * tt)
r_exp = np.power(np.abs(s), 2.0 / 3.0)            # magnitude of the areal radius
# our cosmology (expanding, tt>0)
axA.plot(tt[tt >= 0], r_exp[tt >= 0], color="#1f6feb", lw=3,
         label="our cosmology  (expanding leg)", zorder=5)
# progenitor collapse (tt<0), drawn as the mirror leg (the antecedent universe)
axA.plot(tt[tt <= 0], r_exp[tt <= 0], color="#d1495b", lw=3,
         label="progenitor collapse  (excursion leg)", zorder=5)
axA.axvline(0, color="#444", lw=1.1, ls=(0, (4, 3)))
axA.scatter([0], [0], s=70, color="black", zorder=6)
axA.annotate("seam  $\\tilde\\tau=0$\n(branch point, NOT an $r{=}0$ wall;\nthe correspondence locus)",
             xy=(0, 0), xytext=(0.05, 1.35), fontsize=8.4,
             ha="left", va="center")
# rate-level bands
axA.text(-1.55, 2.35, "LEAF-LEVEL\nlocal Friedmann,  radiation-INCLUDED\n"
                      "$\\mathcal{H}^2=\\frac{8\\pi G}{3}\\rho_{\\rm tot}+\\frac{\\Lambda}{3}$\n"
                      "self-gravitating; BBN window runs here",
         fontsize=7.8, ha="center", va="center", color="#a01c34",
         bbox=dict(boxstyle="round,pad=0.4", fc="#fdeef1", ec="#d1495b", lw=1))
axA.text(1.5, 2.35, "FOLIATION-LEVEL\nstacking rate,  GEOMETRIC\n"
                    "$H^2=\\frac{\\Lambda c^2}{3}\\coth^2(\\cdots)$  ($\\sinh^{2/3}$)\n"
                    "content read off the clock; recomb, $r_s$, $r_D$ here",
         fontsize=7.8, ha="center", va="center", color="#134a9c",
         bbox=dict(boxstyle="round,pad=0.4", fc="#eaf1fd", ec="#1f6feb", lw=1))
axA.set_xlabel("cosmic time  $\\tilde\\tau$  (one analytic parameter, $-\\infty\\to\\infty$)", fontsize=9)
axA.set_ylabel("areal radius  $r=\\sinh^{2/3}(\\frac{3}{2}\\tilde\\tau)$", fontsize=9)
axA.set_title("(A)  ONE analytic expansion; the decision rule lives ON the curve",
              fontsize=10, weight="bold")
axA.set_ylim(-0.15, 2.95)
axA.set_xlim(-2.3, 2.3)
axA.legend(loc="lower center", fontsize=7.6, framealpha=0.9)
axA.grid(alpha=0.25)

# ---------------------------------------------------------------------------
# (B) the map: two slicings of one de Sitter hyperboloid
# ---------------------------------------------------------------------------
axB = fig.add_subplot(1, 3, 2, projection="3d")
alpha = 1.0
u = np.linspace(-1.9, 1.9, 60)
phi = np.linspace(0, 2 * np.pi, 90)
U, PHI = np.meshgrid(u, phi)
X0 = np.sinh(U)
X1 = np.cosh(U) * np.cos(PHI)
X2 = np.cosh(U) * np.sin(PHI)
axB.plot_surface(X1, X2, X0, alpha=0.12, color="#9aa7b5",
                 rstride=3, cstride=3, linewidth=0, antialiased=True)

# CLOSED (ontological) slices: X0 = const  -> round circles (the S^3 layer)
for u0 in (-1.1, 0.0, 1.1):
    c = np.cosh(u0)
    th = np.linspace(0, 2 * np.pi, 220)
    axB.plot(c * np.cos(th), c * np.sin(th), np.sinh(u0) * np.ones_like(th),
             color="#1a7f37", lw=2.6, zorder=6)
axB.plot([], [], [], color="#1a7f37", lw=2.6,
         label="CLOSED slicing  $X_0{=}$const  →  ontological $S^3$ layer (the existent)")

# FLAT (shadow) slices: eta(X,B)=const with B=(1,0,1) null ruling -> X2 - X0 = c.
# Plane parallel to a ruling cuts the hyperboloid in a parabola; draw each as ONE
# connected curve (up the +X1 branch, back down the -X1 branch).
def horosphere(cval):
    X0h = np.linspace(-1.9, 1.9, 300)
    val = 1 - 2 * cval * X0h - cval**2
    m = val >= 0
    X0h = X0h[m]; X1h = np.sqrt(val[m]); X2h = X0h + cval
    xs = np.concatenate([X1h, -X1h[::-1]])
    ys = np.concatenate([X2h, X2h[::-1]])
    zs = np.concatenate([X0h, X0h[::-1]])
    return xs, ys, zs
for cval in (-0.9, 0.0, 0.9):
    xs, ys, zs = horosphere(cval)
    axB.plot(xs, ys, zs, color="#b8860b", lw=2.0, zorder=5)
axB.plot([], [], [], color="#b8860b", lw=2.0,
         label="FLAT slicing  $\\eta(X,B){=}$const  →  observed flat-$\\Lambda$CDM shadow")

# the past null ruling B (the common asymptote): a straight generator
sline = np.linspace(-1.75, 1.75, 50)
axB.plot(np.ones_like(sline), sline, sline, color="black", lw=3.2, zorder=9)
axB.plot([], [], [], color="black", lw=3.2,
         label="null ruling $B$  =  the null ruling the flat slicing synchronizes to")

axB.set_title("(B)  the MAP: ONE hyperboloid, two synchronizations of one congruence\n"
              "the reassignment re-synchronizes the flat slicing to the null ruling $B$",
              fontsize=9.2, weight="bold")
axB.set_xlabel("$X_1$", fontsize=8); axB.set_ylabel("$X_2$", fontsize=8)
axB.set_zlabel("$X_0$ (time)", fontsize=8)
axB.legend(loc="upper center", bbox_to_anchor=(0.5, -0.03), fontsize=7.0, framealpha=0.92)
axB.view_init(elev=10, azim=-72)
axB.set_box_aspect((1, 1, 1.2))

# ---------------------------------------------------------------------------
# (C) the involution sigma
# ---------------------------------------------------------------------------
axC = fig.add_subplot(1, 3, 3)
r0 = np.linspace(0, 2 / np.sqrt(3), 500)
sig = 0.5 * (-r0 + np.sqrt(np.clip(4 - 3 * r0**2, 0, None)))
axC.plot(r0, sig, color="#1f6feb", lw=2.6, label="$\\sigma(r_0)=\\frac{1}{2}(-r_0+\\sqrt{4-3r_0^2})$")
axC.plot(r0, r0, color="#888", lw=1.1, ls=(0, (4, 3)), label="identity")
nar = 1 / np.sqrt(3)
axC.scatter([nar], [nar], s=90, color="#d1495b", zorder=6)
axC.annotate("Nariai  $r_0=1/\\sqrt{3}$\n(FIXED point = the cosmology)",
             xy=(nar, nar), xytext=(nar + 0.18, nar - 0.28), fontsize=8.2,
             arrowprops=dict(arrowstyle="->", color="#d1495b"))
# endpoints swapped 0<->1
axC.scatter([0, 1], [1, 0], s=55, color="#1a7f37", zorder=6)
axC.annotate("$0\\leftrightarrow1$\n(de Sitter ↔ throat-tangent,\nswapped by $\\sigma$)",
             xy=(0, 1), xytext=(0.12, 0.78), fontsize=8.0)
# a generic two-cycle: pick r0=0.3 -> sigma(0.3), draw the swap
g = 0.3; sg = 0.5 * (-g + np.sqrt(4 - 3 * g**2))
axC.plot([g, sg], [sg, g], color="#6f42c1", lw=1.4, marker="o", ms=4, zorder=5)
axC.annotate("generic vantage:\ntwo-cycle (reassignment forbidden)",
             xy=(g, sg), xytext=(0.34, 1.02), fontsize=7.6, color="#6f42c1")
axC.set_xlabel("slicing parameter  $r_0$", fontsize=9)
axC.set_ylabel("$\\sigma(r_0)$  (the exchanged root)", fontsize=9)
axC.set_title("(C)  the involution $\\sigma$: cosmology = its fixed point",
              fontsize=10, weight="bold")
axC.set_xlim(-0.03, 1.20); axC.set_ylim(-0.03, 1.20)
axC.legend(loc="lower left", fontsize=7.6, framealpha=0.9)
axC.grid(alpha=0.25); axC.set_aspect("equal")

fig.suptitle("Cosmological Relativity — the reassignment/projection made analytic and pictured  "
             "(one geometry, two slicings; the rate-level rule lives on the curve)",
             fontsize=11.5, weight="bold", y=1.005)
fig.tight_layout(rect=(0, 0, 1, 0.98))
out = "/home/claude/cr/computations/reassignment_projection_map.png"
fig.savefig(out, dpi=155, bbox_inches="tight")
print("wrote", out)
