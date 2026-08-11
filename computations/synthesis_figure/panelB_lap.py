"""Panel B — the lap / branch-point seam.  r(tau)=A[sinh((3/2)H tau)]^{2/3}, one analytic curve."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})

s = np.linspace(-2.3, 2.3, 1400)                 # s=(3/2)H tau
r = np.sinh(s.astype(complex))**(2/3)
Re, Im = r.real, r.imag
ex, co = s > 0, s < 0

fig = plt.figure(figsize=(6.0,5.0)); ax = fig.add_subplot(111, projection='3d')
# faint real plane (Im r = 0)
ss, rr = np.meshgrid(np.linspace(-2.3,2.3,2), np.linspace(-1.6,3.4,2))
ax.plot_surface(ss, rr, np.zeros_like(ss), color='0.5', alpha=0.05, linewidth=0)
# expansion leg (real floor)
ax.plot(s[ex], Re[ex], Im[ex], color='#c0392b', lw=3.0, zorder=5)
# conjugate/prior-collapse leg (lifts out of plane, phase 2pi/3)
ax.plot(s[co], Re[co], Im[co], color='#2471a3', lw=3.0, zorder=5)
# drop-lines: show the conjugate branch is OFF the real floor
for i in range(0,co.sum(),90):
    idx=np.where(co)[0][i]
    ax.plot([s[idx],s[idx]],[Re[idx],Re[idx]],[0,Im[idx]], color='#2471a3', lw=0.6, alpha=0.33)
# forced-real projection = the fake cusp
ax.plot(s[co], -np.abs(r[co]), np.zeros(co.sum()), color='#7f8c8d', lw=1.5, ls=(0,(5,3)), zorder=4)
# seam / branch point
ax.scatter([0],[0],[0], color='k', s=48, zorder=8)
# direction arrows along each leg
ax.quiver(s[ex][450],Re[ex][450],0, 0.9,Re[ex][480]-Re[ex][450],0, color='#c0392b', length=0.5, arrow_length_ratio=0.6, lw=2)
# leg labels placed on the curves
ax.text(1.9, Re[ex][-1]*0.9, 0.15, 'expansion\n$\\sinh^{2/3}$', color='#c0392b', fontsize=9, ha='center')
ax.text(-2.15, Re[co][0], Im[co][0]+0.15, 'prior collapse\n(conjugate branch,\nphase $2\\pi/3$)', color='#2471a3', fontsize=8.6, ha='center')
ax.text(-1.4, -1.4, 0.0, 'forced-real:\nthe fake cusp', color='#555', fontsize=8, ha='center')
# seam annotation, parked clear of the geometry, with a leader
ax.text(-0.15, 1.7, 2.35, 'seam  $\\tilde\\tau=0,\\ r\\to0$:\nfinite-curvature branch point\n(Nariai degenerate horizon)\n— not the singularity',
        fontsize=8.2, ha='center', va='center')
ax.plot([0,-0.1],[0,1.5],[0,1.95], color='k', lw=0.6)

ax.set_xlabel(r'$\tilde\tau$', labelpad=2); ax.set_ylabel(r'$\mathrm{Re}\,r$', labelpad=6); ax.set_zlabel(r'$\mathrm{Im}\,r$', labelpad=2)
ax.text2D(0.0, 0.98, 'B', transform=ax.transAxes, fontsize=15, fontweight='bold')
ax.text2D(0.05, 0.98, r'The lap: one analytic $r(\tilde\tau)$ through the seam', transform=ax.transAxes, fontsize=10.5, va='top')
ax.view_init(elev=17, azim=-40); ax.set_box_aspect((2.3,1.5,1.15))
ax.xaxis.pane.set_alpha(0.02); ax.yaxis.pane.set_alpha(0.02); ax.zaxis.pane.set_alpha(0.02)
ax.grid(True, alpha=0.22)
plt.subplots_adjust(left=0.02,right=0.86,top=0.9,bottom=0.06)
plt.savefig('panelB_lap.png', dpi=160, bbox_inches='tight', pad_inches=0.35); plt.savefig('panelB_lap.pdf', bbox_inches='tight')
print("ok")
