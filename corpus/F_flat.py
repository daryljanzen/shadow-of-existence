"""(F, flattened) -- the cosmological bundle against path length in complex cosmic time.

The bead's tau~ path is two perpendicular straight legs joined by the lift, so its arc length s is
exact rather than numerical. With A = (2M a^2)^{1/3} = cbrt(2) a/sqrt3 at Nariai (2M = 2a/3sqrt3):

    s <= 0        collapse : Re tau~ = s,          Im tau~ = -pi a/3   ->  r = -A cosh^{2/3}(3s/2a)
    0 < s < pi/3  the LIFT : Re tau~ = 0,          Im tau~ = s - pi a/3 ->  r = -A sin^{2/3}(3(pi/3 - s)/2a)
    s >= pi/3     expansion: Re tau~ = s - pi a/3, Im tau~ = 0          ->  r = +A sinh^{2/3}(3(s - pi/3)/2a)

r(s) is single-valued, monotonic and smooth; nothing is projected and no r value is flattened.
The two bends ARE the two landmarks, and the derivatives match across both joints:
    turnaround (-cbrt(2) a/sqrt3) : dr/ds = 0      -> horizontal tangent (the collapse stops)
    r = 0                         : dr/ds -> inf   -> vertical tangent   (P7's bounded crossing)
The two seams are cbrt(2)-related to nothing accidental: turnaround -cbrt(2) a/sqrt3, seam +a/sqrt3.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt

plt.rcParams.update({'font.family': 'serif', 'font.size': 13, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
al = 1.0
A  = 2**(1/3) * al / np.sqrt(3)      # = (2M a^2)^{1/3} at Nariai, in alpha alone
P  = np.pi / 3                       # the lift's length in s

def r_of_s(s):
    s = np.asarray(s, float); out = np.empty_like(s)
    m1, m2, m3 = s <= 0, (s > 0) & (s <= P), s > P
    out[m1] = -A * np.cosh(1.5 * s[m1])**(2/3)
    out[m2] = -A * np.sin(1.5 * (P - s[m2]))**(2/3)
    out[m3] =  A * np.sinh(1.5 * (s[m3] - P))**(2/3)
    return out

fig, ax = plt.subplots(figsize=(6.4, 6.4))
ax.axvspan(0, P, color='0.95', zorder=0)
for seg, col in [((-2.0, 0), RED), ((0, P), RED), ((P, 2.6), BLUE)]:
    ss = np.linspace(*seg, 700); ax.plot(ss, r_of_s(ss), color=col, lw=3.4, zorder=3)
ax.axhline(0, color='0.85', lw=0.8, zorder=1)
ax.text(P/2, 2.42, 'the lift', fontsize=10.5, color='0.4', ha='center')
ax.text(P/2, 2.18, r'(no $\mathrm{Re}\,\tilde\tau$ advance)', fontsize=9.5, color='0.5', ha='center')

sSm = -(2/3)*np.arccosh(abs((-2/np.sqrt(3))/A)**1.5)      # back seam, on the collapse leg
sSp =  P + (2/3)*np.arcsinh(((1/np.sqrt(3))/A)**1.5)      # front seam, on the expansion leg
# each label: line 1 = name (value); dr/ds  |  line 2 = (tangent character)
pts = [(sSm, -2/np.sqrt(3), 'o', r'seam $(r=-2\alpha/\sqrt{3})$',                     None,                   (0.07, -0.08)),
       (0.0, -A,            's', r'turnaround $(r=-\sqrt[3]{2}\,\alpha/\sqrt{3})$; $dr/ds=0$', '(horizontal tangent)', (0.08, -0.07)),
       (P,    0.0,          'o', r'$r=0$; $dr/ds\to\infty$',                        '(vertical tangent)',   (0.09, -0.07)),
       (sSp,  1/np.sqrt(3), 'o', r'seam $(r=+\alpha/\sqrt{3})$',                       None,                   (0.08, -0.07))]
for x, y, mk, l1, l2, (dx, dy) in pts:
    ax.plot(x, y, mk, color='0.12', ms=7.5, zorder=6)
    ax.annotate(l1, xy=(x, y), xytext=(x+dx, y+dy), fontsize=9.5, ha='left', va='top', color='0.1', zorder=6)
    if l2:
        ax.annotate(l2, xy=(x, y), xytext=(x+dx, y+dy-0.185), fontsize=9.5, ha='left', va='top', color='0.1', zorder=6)

ax.text(-1.24, -0.42, 'antimatter black hole', color=RED,  fontsize=11, ha='center')   # s<0, r<0
ax.text(-1.24, -0.72, '(collapse)',            color=RED,  fontsize=11, ha='center')
ax.text( 1.78,  2.02, 'matter universe',       color=BLUE, fontsize=11, ha='center')   # s>pi/3, r>0
ax.text( 1.78,  1.72, '(expansion)',           color=BLUE, fontsize=11, ha='center')

ax.set_xlabel(r'$s/\alpha$', fontsize=13, labelpad=6)
ax.set_ylabel(r'$r/\alpha$', fontsize=13)
ax.set_xlim(-2.0, 2.6); ax.set_ylim(-2.6, 2.6)
ax.set_xticks([-2, -1, 0, P, 2]); ax.set_xticklabels(['$-2$', '$-1$', '$0$', r'$\pi/3$', '$2$'])
for sp in ['top', 'right']: ax.spines[sp].set_visible(False)
ax.text(0.0, 1.02, r'(F) the cosmological bundle, against path length in $\tilde\tau$', transform=ax.transAxes, fontsize=12, va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig('F_flat.pdf', bbox_inches='tight'); plt.savefig('F_flat.png', dpi=150, bbox_inches='tight')
print('ok')
