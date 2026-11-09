"""Figure for the standalone circle paper: the areal radius and the Kretschmann scalar along the one analytic curve.

Path parameter u, M = 1:
  u < 0        back arm   z = pi + i|u|   r = 1 - cosh u      (r < 0)
  0 <= u <= pi interior   z = pi - u      r = 1 - cos u       (0 <= r <= 2)
  u > pi       front arm  z = i(u - pi)   r = 1 + cosh(u-pi)  (r > 2)
Both critical points (u = 0: r = 0; u = pi: r = 2M) have dr/du = 0.  K M^4 = 48/r^6.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt

def r_of(u):
    u = np.asarray(u, float); out = np.empty_like(u)
    b = u < 0; i = (u >= 0) & (u <= np.pi); f = u > np.pi
    out[b] = 1 - np.cosh(u[b]); out[i] = 1 - np.cos(u[i]); out[f] = 1 + np.cosh(u[f] - np.pi)
    return out

h = 1e-6
for u0, rv in [(0.0, 0.0), (np.pi, 2.0)]:
    assert abs(r_of([u0])[0] - rv) < 1e-12
    assert abs((r_of([u0 + h])[0] - r_of([u0 - h])[0]) / (2*h)) < 1e-5, 'flat tangent at the critical point'
assert abs(48/2**6 - 0.75) < 1e-15   # K at the horizon = 3/(4M^4)

plt.rcParams.update({'font.family': 'serif', 'font.serif': ['STIXGeneral', 'DejaVu Serif'], 'font.size': 11, 'mathtext.fontset': 'stix', 'pdf.fonttype': 42})
u = np.concatenate([np.linspace(-2.2, -1e-3, 800), np.linspace(1e-3, np.pi, 800), np.linspace(np.pi, np.pi + 2.2, 800)])
r = r_of(u)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.2, 6.4), sharex=True)
cols = {'back': '#c0392b', 'int': '0.15', 'front': '#2471a3'}
for m, c, lab in [(u < 0, cols['back'], r'$z=\pi+i\rho\prime$ ($r<0$)'),
                  ((u >= 0) & (u <= np.pi), cols['int'], r'$z$ real (interior)'),
                  (u > np.pi, cols['front'], r'$z=i\rho$ ($r>2M$)')]:
    a1.plot(u[m], r[m], color=c, lw=2.4, label=lab)
    K = 48 / r[m]**6
    a2.semilogy(u[m], K, color=c, lw=2.4)
for x, y, t in [(0, 0, r'$r=0$'), (np.pi, 2, r'$r=2M$')]:
    a1.plot(x, y, 'o', color='k', ms=6, zorder=5)
    a1.annotate(t, (x, y), xytext=(x + 0.12, y + 0.35), fontsize=10)
for ax in (a1, a2):
    ax.axvline(0, color='0.75', lw=0.8, ls=':'); ax.axvline(np.pi, color='0.75', lw=0.8, ls=':')
    for sp_ in ('top', 'right'): ax.spines[sp_].set_visible(False)
a1.axhline(0, color='0.85', lw=0.8)
a1.set_ylabel(r'$r/M$'); a1.set_ylim(-4, 6); a1.legend(frameon=False, fontsize=9, loc='upper left')
a2.axhline(0.75, color='0.6', lw=0.8, ls='--'); a2.text(np.pi + 0.1, 1.1, r'$3/4$ at the horizon', fontsize=9, color='0.35')
a2.set_ylabel(r'$K M^4$'); a2.set_ylim(1e-3, 1e6)
a2.set_xlabel(r'path parameter along the curve ($z=\pi-u$ on the interior arc)')
a2.set_xticks([0, np.pi]); a2.set_xticklabels([r'$z=\pi$', r'$z=0$'])
a1.text(0.0, 1.02, '(a)', transform=a1.transAxes, fontweight='bold'); a2.text(0.0, 1.02, '(b)', transform=a2.transAxes, fontweight='bold')
plt.tight_layout(); plt.savefig('fig_circle.pdf', bbox_inches='tight'); plt.savefig('fig_circle.png', dpi=150, bbox_inches='tight')
print('ok')
