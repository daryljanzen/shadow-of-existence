#!/usr/bin/env python3
"""
Figure generation for the scalar-perturbation / CMB paper (P12,
scalar_perturbations_paper.tex, "What the seam transmits").

Three figures, each tied to a load-bearing claim, all grounded in the cold
verification (computations/perturbation_verify/) and the paper's propositions:

  fig:seam-merger        -- the SdS metric function f(r) and the Nariai merger:
                            the cosmogenesis seam is the DEGENERATE double root
                            (kappa = 0), the geometry the transmission proof rests on
                            [Prop. throat]
  fig:transmission       -- the transmission dichotomy: a non-degenerate horizon's
                            EXPONENTIAL approach (a thermal scale -> imprints n_s->1)
                            vs the Nariai double root's POWER-LAW approach (no scale ->
                            transmits the progenitor spectrum) [Prop. transmission, transmit]
  fig:lowL-floor         -- the parameter-free low-multipole discreteness floor
                            ell_L = sqrt(L(L+2)) D_C / r_0, lowest mode L=2 -> ell~8,
                            quasi-continuous by L~20 [Sec. largescale]

Output: PNGs written next to the .tex (corpus/), bare-filename includes, matching
the corpus convention (cf. P9's {dS-SdS.png}).
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- house style: clean, serif to sit with LaTeX body type -----------------
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.linewidth": 0.8,
    "axes.labelsize": 12,
    "legend.frameon": False,
    "legend.fontsize": 10,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
})

OUT = os.path.join(os.path.dirname(__file__), "..", "corpus")
OUT = os.path.abspath(OUT)

C_DS = "#1f6f8b"   # de Sitter / substrate-determined
C_MASS = "#c0392b" # mass / perspectival
C_NAR = "#000000"  # the Nariai seam
C_GREY = "#888888"


# ============================================================================
# Figure 1 -- the seam: f(r) and the Nariai merger (units alpha = 1)
#   f(r) = 1 - 2m/r - r^2,   Lambda G^2 M^2 / c^4 = 3 m^2 (alpha=1)
#   Nariai: 3 m^2 = 1/9  => m = 1/(3 sqrt3) ~ 0.1925, double root r_* = 1/sqrt3
# ============================================================================
def fig_seam_merger():
    r = np.linspace(0.06, 1.25, 800)

    def f(r, m):
        return 1.0 - 2.0 * m / r - r ** 2

    m_under = 0.15            # under-critical: two positive horizons
    m_nar = 1.0 / (3 * np.sqrt(3))   # Nariai: double root
    m_over = 0.25             # over-critical: no real positive horizon
    r_star = 1.0 / np.sqrt(3)

    fig, ax = plt.subplots(figsize=(5.4, 3.9))
    ax.axhline(0, color=C_GREY, lw=0.8, zorder=1)

    ax.plot(r, f(r, m_under), color=C_DS, lw=1.8,
            label=r"under-critical ($\Lambda G^2M^2/c^4<\frac{1}{9}$): two horizons")
    ax.plot(r, f(r, m_nar), color=C_NAR, lw=2.2,
            label=r"Nariai ($=\frac{1}{9}$): merged double root, $\kappa=0$")
    ax.plot(r, f(r, m_over), color=C_MASS, lw=1.8, ls="--",
            label=r"over-critical ($>\frac{1}{9}$): no horizon")

    # mark the merged double root r_* = alpha/sqrt3 = 1/sqrt(Lambda)
    ax.plot([r_star], [0], marker="o", ms=6, color=C_NAR, zorder=5)
    ax.annotate(r"$r_\star=\alpha/\sqrt{3}=1/\sqrt{\Lambda}$",
                xy=(r_star, 0), xytext=(r_star + 0.12, 0.22),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color=C_GREY, lw=0.7))

    ax.set_xlabel(r"areal radius $r/\alpha$")
    ax.set_ylabel(r"$f(r)=1-2GM/c^2r-r^2/\alpha^2$")
    ax.set_xlim(0, 1.25)
    ax.set_ylim(-0.7, 0.55)
    ax.legend(loc="lower left")
    ax.set_title(r"The cosmogenesis seam is the degenerate Nariai double root",
                 fontsize=11)
    fig.savefig(os.path.join(OUT, "seam-merger.png"))
    plt.close(fig)
    return r_star, m_nar


# ============================================================================
# Figure 2 -- the transmission dichotomy
#   tortoise r_* = int dr/f.
#   simple root  f ~ 2 kappa (r-r_h)   ->  r_* ~ (1/2kappa) ln(r-r_h)
#                                       ->  (r-r_h) ~ exp(2 kappa r_*)  EXPONENTIAL
#                                          (a thermal scale kappa; imprints n_s->1)
#   double root  f ~ Lambda (r-r_*)^2  ->  r_* ~ -1/[Lambda (r-r_*)]
#                                       ->  (r-r_*) ~ -1/(Lambda r_*)   POWER-LAW
#                                          (no scale; transmits the progenitor spectrum)
# ============================================================================
def fig_transmission():
    # use the tortoise coordinate r_* running to -infinity at the horizon.
    rstar = np.linspace(-7.0, -0.4, 600)

    kappa = 0.6
    delta_simple = np.exp(2 * kappa * rstar)        # exponential approach
    Lam = 1.0
    delta_degen = -1.0 / (Lam * rstar)              # power-law approach (1/|r_*|)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(7.6, 3.5))

    # left: the approach delta = (r - r_h) on a log axis vs tortoise
    axL.semilogy(rstar, delta_simple, color=C_MASS, lw=2.0,
                 label=r"simple horizon ($\kappa>0$): $e^{2\kappa r_*}$")
    axL.semilogy(rstar, delta_degen, color=C_DS, lw=2.0,
                 label=r"Nariai double root ($\kappa=0$): $\propto 1/|r_*|$")
    axL.set_xlabel(r"tortoise coordinate $r_*=\int dr/f$")
    axL.set_ylabel(r"approach $(r-r_h)$")
    axL.legend(loc="lower right")
    axL.set_title("approach to the horizon", fontsize=10.5)

    # right: the "approach rate" d ln(delta)/d r_*  -- the SCALE
    #   simple:   constant 2 kappa   (a thermal scale -> imprints scale-invariance)
    #   degenerate: -1/r_* -> 0      (no scale -> scale-free, transmits)
    rate_simple = np.full_like(rstar, 2 * kappa)
    rate_degen = -1.0 / rstar
    axR.plot(rstar, rate_simple, color=C_MASS, lw=2.0,
             label=r"simple: $2\kappa$ (a thermal scale)")
    axR.plot(rstar, rate_degen, color=C_DS, lw=2.0,
             label=r"Nariai: $-1/r_*\to0$ (no scale)")
    axR.set_xlabel(r"tortoise coordinate $r_*$")
    axR.set_ylabel(r"approach rate $\;d\ln(r-r_h)/dr_*$")
    axR.legend(loc="upper right")
    axR.set_ylim(0, 2 * kappa * 1.6)
    axR.set_title("the scale, or its absence", fontsize=10.5)

    # annotations: imprint vs transmit
    axR.text(-6.6, 2 * kappa * 1.02, "imprints  $n_s\\to1$", color=C_MASS,
             fontsize=9.5, va="bottom")
    axR.text(-6.6, 0.06, "transmits the progenitor spectrum", color=C_DS,
             fontsize=9.5, va="bottom")

    fig.suptitle(r"The transmission dichotomy: a horizon imprints a thermal scale; "
                 r"a degenerate seam does not", fontsize=10.8, y=1.02)
    fig.savefig(os.path.join(OUT, "transmission-dichotomy.png"))
    plt.close(fig)


# ============================================================================
# Figure 3 -- the low-multipole discreteness floor
#   ell_L = sqrt(L(L+2)) * D_C / r_0,  D_C ~ 13927 Mpc, r_0 ~ 5064 Mpc
#   (verify_numeric.py anchor 6).  Lowest physical mode L=2 -> ell ~ 7.8;
#   quasi-continuous (spacing < 1) by L ~ 20.  Parameter-free from Lambda.
# ============================================================================
def fig_lowL_floor():
    D_C = 13927.0
    r0 = 5064.0
    ratio = D_C / r0
    L = np.arange(2, 31)
    ellL = np.sqrt(L * (L + 2.0)) * ratio

    fig, ax = plt.subplots(figsize=(5.4, 3.7))

    # the observed large-angle deficit region, lightly shaded
    ax.axvspan(2, 5, color=C_GREY, alpha=0.12, lw=0)
    ax.text(3.3, ellL.max() * 0.93, "observed large-\nangle deficit",
            fontsize=8.5, color=C_GREY, ha="center", va="top")

    ax.stem(L, ellL, linefmt=C_DS, markerfmt="o", basefmt=" ")
    # recolor stems/markers cleanly
    for art in ax.lines:
        art.set_color(C_DS)
    ax.plot(L, ellL, color=C_DS, lw=0.0)  # no connecting line; stems only

    # the floor: lowest physical mode L=2
    ax.axhline(ellL[0], color=C_NAR, lw=0.8, ls=":")
    ax.annotate(r"$\ell_2\simeq%.1f$ (no power below)" % ellL[0],
                xy=(2, ellL[0]), xytext=(6.0, ellL[0] - 6),
                fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=C_GREY, lw=0.7))

    ax.set_xlabel(r"closed-$S^3$ mode degree $L$")
    ax.set_ylabel(r"projected multipole $\ell_L=\sqrt{L(L+2)}\,D_C/r_0$")
    ax.set_xlim(0, 31)
    ax.set_ylim(0, ellL.max() * 1.05)
    ax.set_title(r"The low-$\ell$ discreteness floor (parameter-free from $\Lambda$)",
                 fontsize=10.8)
    fig.savefig(os.path.join(OUT, "lowL-floor.png"))
    plt.close(fig)
    return ratio, ellL[0]


if __name__ == "__main__":
    r_star, m_nar = fig_seam_merger()
    fig_transmission()
    ratio, ell2 = fig_lowL_floor()
    print("Wrote figures to:", OUT)
    print("  seam-merger.png        Nariai double root r_* = %.4f (=1/sqrt3), m_N=%.4f" % (r_star, m_nar))
    print("  transmission-dichotomy.png")
    print("  lowL-floor.png         D_C/r_0 = %.3f, ell_2 = %.2f" % (ratio, ell2))
