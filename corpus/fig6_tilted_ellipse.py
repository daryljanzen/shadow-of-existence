"""P3 fig6 -- the horizon locus.  alpha = 1."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

S3 = np.sqrt(3)
L = 1.5

fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.set_aspect('equal')

for r0 in np.linspace(-L, L, 2400):
    M2 = r0 - r0**3
    rts = np.roots([1.0, 0.0, -1.0, M2])
    rts = np.sort(rts[abs(rts.imag) < 1e-9].real)
    brk = np.unique(np.concatenate(([-L], rts[(rts > -L) & (rts < L)], [0.0], [L])))
    for lo, hi in zip(brk[:-1], brk[1:]):
        m = 0.5*(lo + hi)
        if abs(m) > 1e-9 and 1 - M2/m - m**2 < 0:
            ax.plot([r0, r0], [lo, hi], color='0.9', lw=1.3, solid_capstyle='butt', zorder=0)

t = np.linspace(0, 2*np.pi, 1500)
u, v = np.sqrt(2)*np.cos(t), np.sqrt(2/3)*np.sin(t)
ax.plot((u+v)/np.sqrt(2), (-u+v)/np.sqrt(2), 'k', label='horizons')
ax.plot([-L, L], [-L, L], 'k')

r0 = np.linspace(-L, L, 1500)
M2 = r0 - r0**3
ax.plot(r0, M2, 'k', ls='-', label='$r=2M$')
ax.plot(r0, 1.5*M2, 'k', ls='-.', label='$r=3M$')
ax.plot(r0, -np.cbrt(M2), 'k', ls='--', label='$r=(-2M)^{1/3}$')

for x, y in [(2/S3, -1/S3), (-2/S3, 1/S3)]:
    ax.plot(x, y, 'ko', ms=4)

ax.axhline(0, color='k', lw=0.5)
ax.axvline(0, color='k', lw=0.5)
ax.set_xlim(-L, L); ax.set_ylim(-L, L)
ax.set_xlabel('$r_0$'); ax.set_ylabel('$r$')
ax.legend(loc='lower left')

fig.savefig('figs/fig6_tilted_ellipse.pdf', bbox_inches='tight')
fig.savefig('fig6_restored_preview.png', dpi=170, bbox_inches='tight')
print("done")
