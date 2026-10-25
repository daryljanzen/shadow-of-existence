"""The norm of the cosmic layer's ordering direction along the lap -- companion panel to F_triptych.

In the proper-frame chart ds^2 = -dtau^2 + (d_chi r)^2 dchi^2 + r^2 dOmega^2, r = r(tau + chi), the field
K = d_chi - d_tau is Killing, lies in every layer tt = tau + chi = const, and has |K|^2 = (dr/dtt)^2 - 1 = -f(r).
This plots -f along the bead's contour in complex cosmic time (same segments, same path length s, same
colours and shading as F_triptych.py), Nariai member, alpha = 1:

    s <= 0        collapse : r = -A cosh^{2/3}(3s/2)
    0 < s < pi/3  the LIFT : r = -A sin^{2/3}(3(pi/3-s)/2)
    s >= pi/3     expansion: r = +A sinh^{2/3}(3(s-pi/3)/2)        A = (2M)^{1/3} = cbrt(2)/sqrt3

The three dashed levels are the three causal characters as values of ONE function: |K|^2 = 0 (the layer
null: a seam), -1 (K unit timelike: the turnaround), -2 (the Euclidean null).  Landmarks are ASSERTED.
Receipts: receipts/P07_CR_framework/LAP_killing_order.py (symbolic), and the Lean module
computations/formalisation/lean/ShadowFormal/LapKilling.lean (closed-form core, machine-checked).
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.optimize import brentq

M2 = 2 / (3 * np.sqrt(3))                       # 2M at Nariai, alpha = 1
A = M2 ** (1 / 3); P = np.pi / 3
SEG = {'collapse': lambda s: -A * np.cosh(1.5 * s) ** (2 / 3),
       'lift':     lambda s: -A * np.sin(1.5 * (P - s)) ** (2 / 3),
       'expand':   lambda s:  A * np.sinh(1.5 * (s - P)) ** (2 / 3)}
f = lambda r: 1 - M2 / r - r ** 2
K2 = lambda seg, s: -f(SEG[seg](np.asarray(s, float)))

sSm = -(2 / 3) * np.arccosh((2 / np.sqrt(3) / A) ** 1.5)          # back seam
sTA = 0.0                                                          # turnaround
sSp = P + (2 / 3) * np.arcsinh((1 / np.sqrt(3) / A) ** 1.5)       # front seam
sL = brentq(lambda x: K2('lift', x) + 2.0, 1e-6, P - 1e-6)         # Euclidean null

# ---------------------------------------------------------------- the verdicts
assert abs(K2('collapse', sSm)) < 1e-12,              'back seam: |K|^2 = 0 (layer null)'
assert abs(K2('collapse', sTA) + 1) < 1e-12,          'turnaround: |K|^2 = -1'
assert abs(K2('lift', 1e-9) + 1) < 1e-6,              'turnaround from the lift side: |K|^2 = -1'
assert abs(SEG['lift'](sL) + 0.344142) < 1e-5,        'Euclidean null radius'
assert abs(K2('expand', sSp)) < 1e-12,                'front seam: |K|^2 = 0 (layer null)'
assert K2('lift', P - 1e-7) < -1e3,                   'branch point: |K|^2 -> -inf from the lift'
assert K2('expand', P + 1e-7) > 1e3,                  'branch point: |K|^2 -> +inf on the expansion leg'
assert K2('collapse', sSm - 0.2) > 0 > K2('collapse', sSm + 0.2), 'back seam: |K|^2 changes sign (transversal)'
assert K2('expand', sSp - 0.1) > 0 and K2('expand', sSp + 0.1) > 0, 'front seam: |K|^2 touches 0 from above'
# surface gravity kappa = f'/2 at each seam (f' = 2M/r^2 - 2r)
fp = lambda r: M2 / r ** 2 - 2 * r
assert abs(fp(-2 / np.sqrt(3)) / 2 - 3 * np.sqrt(3) / 4) < 1e-12, 'back seam kappa = 3 sqrt3/4'
assert abs(fp(1 / np.sqrt(3)) / 2) < 1e-12,                       'front seam kappa = 0'

# ---------------------------------------------------------------- the figure
plt.rcParams.update({'font.family': 'serif', 'font.size': 13, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
XLO, XHI, YLO, YHI = -2.0, 2.6, -4.0, 2.2
fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.axvspan(0, P, color='0.95', zorder=0)
for x in (sSm, sTA, P, sSp):
    ax.axvline(x, color='0.72', lw=0.9, ls=(0, (2, 2.5)), zorder=1)
for y in (0, -1, -2):
    ax.axhline(y, color='0.55', lw=1.0, ls=(0, (4, 3)), zorder=2)
for seg, (a, b), col in [('collapse', (XLO, 0), RED), ('lift', (1e-6, P - 1e-6), RED), ('expand', (P + 1e-6, XHI), BLUE)]:
    ss = np.linspace(a, b, 4000); yy = K2(seg, ss)
    yy = np.where((yy < YLO) | (yy > YHI), np.nan, yy)
    ax.plot(ss, yy, color=col, lw=3.0, zorder=3)
for spn in ['top', 'right']: ax.spines[spn].set_visible(False)

ax.plot(sSm, 0, 'o', color='0.12', ms=7.5, zorder=6)
ax.annotate('back seam: layer null,\n$\\kappa=3\\sqrt{3}/4\\alpha$', xy=(sSm, 0), xytext=(sSm + 0.10, 0.62), fontsize=9.5, ha='left', color='0.1')
ax.plot(sTA, -1, 's', color='0.12', ms=7.5, zorder=6)
ax.annotate('turnaround:\n$K$ unit timelike', xy=(sTA, -1), xytext=(sTA - 0.12, -1.75), fontsize=9.5, ha='right', color='0.1')
ax.plot(sL, -2, 'D', color='0.12', ms=7.0, zorder=6)
ax.annotate('Euclidean null', xy=(sL, -2), xytext=(sL - 0.08, -2.55), fontsize=9.5, ha='right', color='0.1')
ax.annotate(r'$-\infty\,|\,+\infty$ at $r=0$', xy=(P, YLO), xytext=(P + 0.08, -3.6), fontsize=9.5, ha='left', color='0.1')
ax.plot(sSp, 0, 'o', color='0.12', ms=7.5, zorder=6)
ax.annotate('front seam: layer null,\n$\\kappa=0$ (touched)', xy=(sSp, 0), xytext=(sSp + 0.08, -0.75), fontsize=9.5, ha='left', color='0.1')
ax.text(XLO + 0.05, 0.12, 'layer spacelike', fontsize=9, color='0.4', va='bottom')
ax.text(XLO + 0.05, -0.12, 'layer timelike', fontsize=9, color='0.4', va='top')

ax.set_ylabel(r'$|K|^{2}=-f$', fontsize=13); ax.set_ylim(YLO, YHI)
ax.set_xlabel(r'$s/\alpha$', fontsize=13, labelpad=6); ax.set_xlim(XLO, XHI)
ax.set_xticks([-2, -1, 0, P, 2]); ax.set_xticklabels(['$-2$', '$-1$', '$0$', r'$\pi/3$', '$2$'])
plt.tight_layout()
plt.savefig('F_killing.pdf', bbox_inches='tight'); plt.savefig('F_killing.png', dpi=150, bbox_inches='tight')
print(f"ok | back seam s={sSm:+.5f}  Euclidean null s/P={sL/P:.5f} r={SEG['lift'](sL):+.6f}  front seam s={sSp:.5f}")
