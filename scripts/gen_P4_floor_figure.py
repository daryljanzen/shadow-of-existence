"""P4 Figure fig:floor (written to corpus/fig_floor.pdf and .png): angular power the matter-tracking hypothesis
predicts, against Planck's measured TT spectrum.
It computes nothing: it plots the curves P04_the_floor_exceeds_..._large_smoothing.py writes (floor_curves.npz,
  R = 4, 8, 20 h^-1 Mpc) against planck_TT_full.txt, both in units of (Delta T/T)^2 with T0 = 2.7255 K."""
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
T0 = 2.7255e6
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
here = os.path.join(ROOT, "receipts", "P04_modern_parallax", "P04_floor_data")
out = os.path.join(ROOT, "corpus", "fig_floor")
d = np.load(os.path.join(here, "floor_curves.npz")); ells = d["ells"]
obs = np.loadtxt(os.path.join(here, "planck_TT_full.txt")); l, Dl, lo, hi = obs.T
fig, ax = plt.subplots(figsize=(6.4, 4.2))
for R, ls in ((4, ":"), (8, "-"), (20, "--")):
    C = d[f"R{R}"]
    ax.plot(ells, ells*(ells+1)*C/(2*np.pi), ls, color="#b5341f", lw=1.6,
            label=rf"matter-tracking expansion, $R={R}\,h^{{-1}}$Mpc")
ax.errorbar(l[::1], Dl/T0**2, yerr=[lo/T0**2, hi/T0**2], fmt=".", ms=1.5, color="#2b5d8a",
            ecolor="#9bb7d0", elinewidth=0.4, alpha=0.8, label="Planck 2018, measured TT")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(2, 2600); ax.set_ylim(1e-12, 1e-3)
ax.set_xlabel(r"multipole $\ell$")
ax.set_ylabel(r"$\ell(\ell+1)C_\ell/2\pi$  [$(\Delta T/T)^2$]")
ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.5), frameon=False)
fig.tight_layout(); fig.savefig(out + ".pdf"); fig.savefig(out + ".png", dpi=200)
print("ok")
