"""(F, in three panels) -- the bead's position, rate and acceleration against path length in complex
cosmic time.  Panel (a) IS F_flat.py, unchanged; (b) and (c) are its first and second derivatives.

    s <= 0        collapse : r = -A cosh^{2/3}(3s/2a)
    0 < s < pi/3  the LIFT : r = -A sin^{2/3}(3(pi/3-s)/2a)
    s >= pi/3     expansion: r = +A sinh^{2/3}(3(s-pi/3)/2a)

with A = (2M a^2)^{1/3} = cbrt(2) a/sqrt3 at Nariai.

THE DERIVATIVES ARE NOT TRANSCRIBED BY HAND. They are differentiated symbolically from the three
segment expressions and lambdified, so the drawn curve cannot disagree with the algebra -- a
hand-copied d2r/ds2 carried an extra chain-rule factor of 3/2 and a wrong trig form for the lift
(caught r1426 by Daryl: the curve missed its own marked points), and the figure had no way to fail.
The landmark values are ASSERTED below, so a wrong curve now stops the script.

The four loci are distinguished by the derivatives, and they are NOT alike:
    back seam   r=-2a/sqrt3   : r' = 1 EXACTLY, crossed TRANSVERSALLY (r'' = -1.29904, non-zero)
    turnaround  r=-cbrt2 a/sq3: r' = 0 ; r'' JUMPS -1.5A -> +1.5A -- the tau~ contour's 90-degree corner
    EUCLIDEAN NULL r=-0.344142: f = 2 EXACTLY, dr/dtau = +-i; r' = 1, TRANSVERSAL [s/P = 0.78899]
    r = 0                     : r' -> inf ; r'' -> +inf then -inf -- the areal coordinate's degeneracy
    front seam  r=+a/sqrt3    : r' = 1 EXACTLY, touched TANGENTIALLY (r'' = 0, its minimum)
Both seam values are exact: cosh(3s/2)=2 at the back seam; cosh(2v)=2 gives sinh v = 1/sqrt2 at the
front, whence r = A 2^{-1/3} = a/sqrt3.  THE NULL CONDITION dr/ds = 1 THEREFORE HOLDS THREE TIMES ON
THE LAP, and the two seams are distinguished from each other NOT by presence/absence of a feature but
by ORDER OF CONTACT -- transversal on the collapse leg, tangential on the expansion leg.  An earlier
caption read "at the back seam there is no feature at all", which concealed exactly what the seams
share (corrected r2118).  The third crossing, interior to the LIFT, was unmarked and unnamed until
r2118; the lift's physics is an open item of the programme, not a mere "stretch where Re tau~ does
not advance".  r=0 IS NOT A SEAM: it is the branch point at the lift's close.
"""
import numpy as np, sympy as sp, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt

# ---------------------------------------------------------------- symbolic segments and derivatives
S  = sp.symbols('s', real=True)
Ae = 2**sp.Rational(1, 3) / sp.sqrt(3)          # A = (2M a^2)^{1/3} at Nariai, in alpha alone
Pe = sp.pi / 3                                   # the lift's length in s
EXPR = {'collapse': -Ae * sp.cosh(sp.Rational(3, 2) * S)**sp.Rational(2, 3),
        'lift':     -Ae * sp.sin(sp.Rational(3, 2) * (Pe - S))**sp.Rational(2, 3),
        'expand':    Ae * sp.sinh(sp.Rational(3, 2) * (S - Pe))**sp.Rational(2, 3)}
FN = {k: [sp.lambdify(S, sp.diff(e, S, n), 'numpy') for n in (0, 1, 2)] for k, e in EXPR.items()}
A  = float(Ae); P = float(Pe)

def on(seg, n, s):                                # nth derivative on one segment, real part
    return np.real(np.asarray(FN[seg][n](np.asarray(s, dtype=complex)), dtype=complex))

# the four loci, in s
sSm = -(2/3)*np.arccosh(abs((-2/np.sqrt(3))/A)**1.5)      # back seam,   r = -2a/sqrt3
sTA = 0.0                                                  # turnaround,  r = -cbrt2 a/sqrt3
sZ  = P                                                    # conjugation, r = 0
sSp = P + (2/3)*np.arcsinh(((1/np.sqrt(3))/A)**1.5)       # front seam,  r = +a/sqrt3
from scipy.optimize import brentq                           # the third unit-speed point, interior to the LIFT
sL  = brentq(lambda x: float(np.real(complex(FN['lift'][1](complex(x))))) - 1.0, 1e-6, P - 1e-6)
rL  = float(on('lift', 0, sL))

# ---------------------------------------------------------------- the verdicts, inside the receipt
eps = 1e-9
assert abs(on('collapse', 0, sTA) + A) < 1e-12,             'turnaround radius'
assert abs(on('collapse', 0, sSm) + 2/np.sqrt(3)) < 1e-9,   'back seam radius'
assert abs(on('expand',   0, sSp) - 1/np.sqrt(3)) < 1e-9,   'front seam radius'
assert abs(on('collapse', 1, sTA)) < 1e-12,                 'turnaround: dr/ds = 0'
assert abs(on('lift',     1, eps)) < 1e-8,                  'turnaround: dr/ds = 0 from the lift side'
assert abs(on('collapse', 2, sTA) + 1.5*A) < 1e-12,         "turnaround: r'' = -1.5A"
assert abs(on('lift',     2, eps) - 1.5*A) < 1e-7,          "turnaround: r'' = +1.5A (the jump)"
assert abs(on('expand',   1, sSp) - 1.0) < 1e-9,            'front seam: dr/ds = 1 exactly'
assert abs(on('expand',   2, sSp)) < 1e-9,                  "front seam: r'' = 0 (the inflection)"
assert abs(on('collapse', 2, sSm)) > 0.5,                   "back seam: r'' non-zero, no feature"
assert on('lift',   2, P - 1e-6) > 1e3,                     "lift: r'' -> +inf at r=0"
assert on('expand', 2, P + 1e-6) < -1e3,                    "expansion: r'' -> -inf at r=0"
assert on('collapse', 1, sSm) < on('collapse', 1, sSm - 0.3), 'collapse leg: dr/ds monotone through the back seam'
assert abs(on('collapse', 1, sSm) - 1.0) < 1e-9,            'back seam: dr/ds = 1 EXACTLY (same null value as the front)'
assert abs(on('lift', 1, sL) - 1.0) < 1e-9,                 'lift: the third unit-speed point'
assert abs(rL + 0.344142) < 1e-5,                           'lift unit-speed radius'
assert on('lift', 2, sL) > 1.0,                             'lift unit-speed point: transversal (r-double-prime non-zero)'

# ---------------------------------------------------------------- the figure
plt.rcParams.update({'font.family': 'serif', 'font.size': 13, 'mathtext.fontset': 'cm'})
BLUE, RED = '#2471a3', '#c0392b'
XLO, XHI = -2.0, 2.6
SEGS = [('collapse', (XLO, 0), RED), ('lift', (1e-6, P - 1e-6), RED), ('expand', (P + 1e-6, XHI), BLUE)]

fig, axes = plt.subplots(3, 1, figsize=(6.4, 13.2), sharex=True)
axA, axB, axC = axes
for ax in axes:
    ax.axvspan(0, P, color='0.95', zorder=0)
    for x in (sSm, sTA, sZ, sSp):
        ax.axvline(x, color='0.72', lw=0.9, ls=(0, (2, 2.5)), zorder=1)
    ax.axhline(0, color='0.85', lw=0.8, zorder=1)
    for spn in ['top', 'right']: ax.spines[spn].set_visible(False)

def draw(ax, n, ylim, lw):
    for seg, rng, col in SEGS:
        ss = np.linspace(*rng, 4000); yy = on(seg, n, ss)
        yy = np.where(np.abs(yy) > ylim, np.nan, yy)
        ax.plot(ss, yy, color=col, lw=lw, zorder=3)

# (a) position -- F_flat, unchanged
draw(axA, 0, 1e9, 3.4)
axA.text(P/2, 2.42, 'the lift', fontsize=10.5, color='0.4', ha='center')
axA.text(P/2, 2.18, r'(no $\mathrm{Re}\,\tilde\tau$ advance; physics open)', fontsize=9.5, color='0.5', ha='center')
pts = [(sSm, -2/np.sqrt(3), 'o', r'back seam $(r=-2\alpha/\sqrt{3})$',                              None,                   (0.07, -0.08)),
       (sTA, -A,            's', r'turnaround $(r=-\sqrt[3]{2}\,\alpha/\sqrt{3})$; $dr/ds=0$', '(horizontal tangent)', (0.08, -0.07)),
       (sZ,   0.0,          'o', r'$r=0$ (branch point)',                                      '(vertical tangent)',   (0.11,  0.62)),
       (sSp,  1/np.sqrt(3), 'o', r'front seam $(r=+\alpha/\sqrt{3})$',                         None,                   (0.08, -0.07)),
       (sL,   rL,           'D', r'the Euclidean null $(f=2)$',                                 r'$(r=-0.3441\alpha)$', (0.14, -0.30))]
for x, y, mk, l1, l2, (dx, dy) in pts:
    axA.plot(x, y, mk, color='0.12', ms=7.5, zorder=6)
    axA.annotate(l1, xy=(x, y), xytext=(x+dx, y+dy), fontsize=9.5, ha='left', va='top', color='0.1', zorder=6)
    if l2:
        axA.annotate(l2, xy=(x, y), xytext=(x+dx, y+dy-0.185), fontsize=9.5, ha='left', va='top', color='0.1', zorder=6)
axA.text(-1.24, -0.42, 'antimatter black hole', color=RED,  fontsize=11, ha='center')
axA.text(-1.24, -0.72, '(collapse)',            color=RED,  fontsize=11, ha='center')
axA.text( 1.78,  2.02, 'matter universe',       color=BLUE, fontsize=11, ha='center')
axA.text( 1.78,  1.72, '(expansion)',           color=BLUE, fontsize=11, ha='center')
axA.set_ylabel(r'$r/\alpha$', fontsize=13); axA.set_ylim(-2.6, 2.6)
axA.text(0.0, 1.02, r'(a) position $r$', transform=axA.transAxes, fontsize=12, va='bottom', fontweight='bold')

# (b) rate
draw(axB, 1, 4.0, 3.0)
axB.plot(sTA, 0.0, 's', color='0.12', ms=7.5, zorder=6)
axB.annotate(r'$dr/ds=0$: the collapse stops', xy=(sTA, 0), xytext=(sTA+0.10, 0.42), fontsize=9.5, ha='left', color='0.1', zorder=6)
axB.axhline(1.0, color='0.55', lw=1.0, ls=(0, (4, 3)), zorder=2)
axB.text(XLO+0.06, 1.12, r'the null condition $dr/ds=1$: met three times', fontsize=9.2, color='0.35', ha='left', zorder=6)
axB.plot(sSm, 1.0, 'o', color='0.12', ms=7.5, zorder=6)
axB.annotate('back seam:\ntransversal', xy=(sSm, 1.0), xytext=(sSm-0.10, 2.30), fontsize=9.5, ha='right', color='0.1', zorder=6)
axB.plot(sL, 1.0, 'D', color='0.12', ms=7.0, zorder=6)
axB.annotate('Euclidean null:\n$dr/d\\tilde\\tau=\\pm i$', xy=(sL, 1.0), xytext=(sL-0.10, 2.95), fontsize=9.5, ha='right', color='0.1', zorder=6)
axB.plot(sSp, 1.0, 'o', color='0.12', ms=7.5, zorder=6)
axB.annotate('front seam: tangential (minimum)', xy=(sSp, 1.0), xytext=(sSp+0.10, 0.52), fontsize=9.5, ha='left', color='0.1', zorder=6)
axB.annotate(r'$\to\infty$ at $r=0$', xy=(sZ, 4.0), xytext=(sZ+0.10, 3.70), fontsize=9.5, ha='left', color='0.1', zorder=6)
axB.set_ylabel(r'$dr/ds$', fontsize=13); axB.set_ylim(-0.35, 4.0)
axB.text(0.0, 1.02, r'(b) rate $dr/ds$', transform=axB.transAxes, fontsize=12, va='bottom', fontweight='bold')

# (c) acceleration
YC = 4.0
draw(axC, 2, YC, 3.0)
jm, jp = float(on('collapse', 2, sTA)), float(on('lift', 2, eps))
axC.plot([sTA, sTA], [jm, jp], color='0.12', lw=0.9, ls=(0, (1, 1.6)), zorder=5)
axC.plot(sTA, jm, 's', color='0.12', ms=6.5, zorder=6, mfc='white')
axC.plot(sTA, jp, 's', color='0.12', ms=6.5, zorder=6)
axC.annotate(r'jump $\mp\frac{3}{2}(2M\alpha^{2})^{1/3}$: the contour turns', xy=(sTA, jp), xytext=(sTA+0.12, 2.55),
             fontsize=9.5, ha='left', color='0.1', zorder=6)
axC.plot(sSp, 0.0, 'o', color='0.12', ms=7.5, zorder=6)
axC.annotate('expansion leg reaches\n$dr/ds=1$ tangentially', xy=(sSp, 0), xytext=(sSp+0.10, -1.20), fontsize=9.5, ha='left', color='0.1', zorder=6)
axC.plot(sSm, float(on('collapse', 2, sSm)), 'o', color='0.12', ms=7.5, zorder=6)
axC.annotate('back seam crosses\n$dr/ds=1$ transversally', xy=(sSm, float(on('collapse', 2, sSm))), xytext=(sSm+0.14, -2.10), fontsize=9.5, ha='left', color='0.1', zorder=6)
axC.plot(sL, float(on('lift', 2, sL)), 'D', color='0.12', ms=7.0, zorder=6)
axC.annotate(r'$\pm\infty$ at $r=0$', xy=(sZ, 0), xytext=(sZ+0.16, 3.30), fontsize=9.5, ha='left', color='0.1', zorder=6)
axC.set_ylabel(r'$d^{2}r/ds^{2}$', fontsize=13); axC.set_ylim(-YC, YC)
axC.text(0.0, 1.02, r'(c) acceleration $d^{2}r/ds^{2}$', transform=axC.transAxes, fontsize=12, va='bottom', fontweight='bold')

axC.set_xlabel(r'$s/\alpha$', fontsize=13, labelpad=6)
axC.set_xlim(XLO, XHI)
axC.set_xticks([-2, -1, 0, P, 2]); axC.set_xticklabels(['$-2$', '$-1$', '$0$', r'$\pi/3$', '$2$'])
plt.tight_layout()
plt.savefig('F_triptych.pdf', bbox_inches='tight'); plt.savefig('F_triptych.png', dpi=150, bbox_inches='tight')
print(f"ok | turnaround jump {jm:+.6f} -> {jp:+.6f}   (= mp 1.5A = {-1.5*A:+.6f} -> {1.5*A:+.6f})")
print(f"   | front seam  r={float(on('expand',0,sSp)):.6f}  r'={float(on('expand',1,sSp)):.6f}  r''={float(on('expand',2,sSp)):.2e}")
print(f"   | back seam   r'={float(on('collapse',1,sSm)):.6f}  r''={float(on('collapse',2,sSm)):+.6f}  (unit speed, TRANSVERSAL)")
print(f"   | lift  unit  s/P={sL/P:.5f}  r={rL:+.6f}  r'={float(on('lift',1,sL)):.6f}  r''={float(on('lift',2,sL)):+.5f}")
