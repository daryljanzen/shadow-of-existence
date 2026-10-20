"""Figures for EXPLAINER.md. Every number is computed here from alpha = sqrt(3/Lambda)
(H0 = 68.6, Omega_Lambda = 0.703) or quoted from the paper section named beside it."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import os
OUT = os.path.dirname(os.path.abspath(__file__))
BLUE, RED, INK, MUTED, GRID, SHADE = '#2a6fdb', '#d64545', '#1f2328', '#6b7280', '#e5e7eb', '#eef0f3'
plt.rcParams.update({'font.size': 11, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK,
    'xtick.color': MUTED, 'ytick.color': MUTED, 'text.color': INK, 'axes.spines.top': False,
    'axes.spines.right': False, 'font.family': 'DejaVu Sans'})
c = 299792.458; H0, OL = 68.6, 0.703
alpha_Gly = c/(H0*np.sqrt(OL))*3.26156e-3          # Mpc -> Gly
aT = alpha_Gly                                        # alpha/c in Gyr (1 Gly / c = 1 Gyr)
R = 2**(1/3)*alpha_Gly/np.sqrt(3)                     # amplitude = |turnaround radius|
rN = alpha_Gly/np.sqrt(3)
def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)

# ---------- F2: the lap ----------
lift = np.pi*aT/3
u = np.linspace(-40, 0, 800)                           # collapse leg, real part of cosmic time
r_col = -R*np.cosh(3*u/(2*aT))**(2/3)
s = np.linspace(0, lift, 400)                          # lift, imaginary part runs
r_lift = -R*np.cos(3*s/(2*aT))**(2/3)
t = np.linspace(0, 30, 800)                            # expansion leg
r_exp = R*np.sinh(3*t/(2*aT))**(2/3)
u_bs = -brentq(lambda x: R*np.cosh(3*x/(2*aT))**(2/3) - 2*alpha_Gly/np.sqrt(3), 0, 60)
t_fs = 2*aT/3*np.arcsinh(1/np.sqrt(2)); x0 = 1.68
t_now = 2*aT/3*np.arcsinh((x0*rN/R)**1.5)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw={'width_ratios': [1.7, 1]})
ax.axvspan(0, lift, color=SHADE, zorder=0)
ax.axhline(0, color=GRID, lw=1, zorder=1)
ax.plot(u, r_col, color=RED, lw=2); ax.plot(s, r_lift, color=RED, lw=2, ls=(0, (4, 2)))
ax.plot(lift + t, r_exp, color=BLUE, lw=2)
pts = [(u_bs, -2*alpha_Gly/np.sqrt(3), 'back seam\n−19.6 Gly', 'left'), (0, -R, 'turnaround\n−12.4 Gly', 'left'),
       (lift, 0, 'branch point\nr = 0', 'right'), (lift+t_fs, rN, 'front seam\n+9.8 Gly', 'left'),
       (lift+t_now, x0*rN, 'today\n+16.5 Gly', 'left')]
for x, y, lab, ha in pts:
    ax.plot(x, y, 'o', ms=7, color='white', mec=INK, mew=1.5, zorder=5)
    dx = -1.2 if ha == 'left' else 1.2
    ax.annotate(lab, (x, y), xytext=(x+dx, y+(2.2 if y >= 0 else -4.4)), ha='right' if ha == 'left' else 'left', fontsize=9.5, color=INK)
ax.text(lift/2, 34, 'the lift\nimaginary time:\nthe real clock stands still', ha='center', va='top', fontsize=9.5, color=MUTED)
ax.annotate('', xy=(0, -26), xytext=(u_bs, -26), arrowprops=dict(arrowstyle='<->', color=MUTED))
ax.text(u_bs/2, -27.8, f'{-u_bs:.1f} Gyr', ha='center', va='top', fontsize=9, color=MUTED)
ax.annotate('', xy=(lift+t_fs, -6), xytext=(lift, -6), arrowprops=dict(arrowstyle='<->', color=MUTED))
ax.text(lift+t_fs/2, -7.3, f'{t_fs:.1f} Gyr', ha='center', va='top', fontsize=9, color=MUTED)
ax.text(-38, -3, 'collapse\n(antimatter side, r < 0)', color=RED, fontsize=9.5, va='top')
ax.text(lift+17, -12, 'our expansion\n(matter side, r > 0)', color=BLUE, fontsize=9.5)
ax.set_xlim(-40, lift+30); ax.set_ylim(-31, 36)
ax.set_xlabel('along the lap: cosmic time on the real legs, imaginary time across the lift (billions of years)')
ax.set_ylabel('signed radius of the layer (billions of light-years)')
ax.set_title('(a) The lap, one strand of it', loc='left', fontsize=12)
# panel b: the circuit
th = np.linspace(0, 2*np.pi, 400); bx.plot(np.cos(th), np.sin(th), color=GRID, lw=1)
def P(deg):  # 0 deg (branch point) at the bottom, increasing anticlockwise
    a = np.radians(deg - 90); return np.cos(a), np.sin(a)
def arc(d0, d1, **kw):
    d = np.linspace(d0, d1, 200); a = np.radians(d - 90); bx.plot(np.cos(a), np.sin(a), **kw)
tdeg = -2*np.pi*2**(1/3)/3*180/np.pi
arc(-240, tdeg, color=RED, lw=3); arc(tdeg, 0, color=RED, lw=3, ls=(0, (3, 2))); arc(0, 120, color=BLUE, lw=3)
for deg, lab, off in [(0, 'branch point  0°', (0, -0.2)), (tdeg, f'turnaround  {tdeg:.0f}°', (-0.05, -0.12)),
                      (120, 'front seam  +120°\n= back seam  −240°', (0.08, 0.1))]:
    x, y = P(deg); bx.plot(x, y, 'o', ms=8, color='white', mec=INK, mew=1.5, zorder=5)
    bx.text(x+off[0], y+off[1], lab, ha='center' if deg == 0 else ('right' if x < 0 else 'left'), fontsize=9.5)
bx.text(0, 0.05, 'one turn\n120° expanding (blue)\n240° collapsing (red)', ha='center', va='center', fontsize=9.5, color=MUTED)
bx.set_aspect('equal'); bx.axis('off'); bx.set_xlim(-1.6, 1.9); bx.set_ylim(-1.45, 1.45)
bx.set_title('(b) The same lap as one circuit', loc='left', fontsize=12)
save(fig, 'F2_lap.png')

# ---------- F3: the triangle in conformal time ----------
from scipy.special import beta
c0 = 2/(np.sqrt(3)*2**(1/3)); col, lif, exp_ = c0*beta(1/3, 1/6)/4, c0*beta(1/6, 1/2)/2, c0*beta(1/3, 1/6)/2
fig, ax = plt.subplots(figsize=(6.4, 4.6))
ax.plot([0, col, col, 0], [0, 0, lif, 0], color=INK, lw=0)
ax.plot([0, col], [0, 0], color=RED, lw=3); ax.plot([col, col], [0, lif], color=RED, lw=3, ls=(0, (4, 2)))
ax.plot([0, col], [0, lif], color=BLUE, lw=3)
ax.plot([col-0.12, col-0.12, col], [0, 0.12, 0.12], color=MUTED, lw=1)
ax.text(col/2, -0.18, f'collapse  {col:.3f}  (1)', ha='center', va='top', color=RED)
ax.text(col+0.1, lif/2, f'lift  {lif:.3f}  (√3)\nimaginary', va='center', color=RED)
ax.text(col/2-0.25, lif/2+0.15, f'expansion  {exp_:.3f}  (2)', ha='right', rotation=np.degrees(np.arctan(lif/col)), rotation_mode='anchor', color=BLUE)
ax.text(0.25, 0.08, '60°', fontsize=9, color=MUTED); ax.text(col-0.35, lif-0.75, '30°', fontsize=9, color=MUTED)
ax.set_xlim(-0.3, col+1.4); ax.set_ylim(-0.5, lif+0.3); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('The lap in conformal time (units of α): a 30-60-90 triangle', loc='left', fontsize=12)
save(fig, 'F3_triangle.png')

# ---------- F5: what crosses ----------
L = [0, 1, 2, 4, 6, 8, 10]; T = [1, 8.97e-2, 4.158e-3, 1.116e-5, 2.438e-8, 4.730e-11, 8.497e-14]   # CR_cosmology sec:throat
fig, ax = plt.subplots(figsize=(7, 4.4))
ax.semilogy(L, T, color=BLUE, lw=1.2, zorder=1)
ax.semilogy(L[0], T[0], 'o', ms=9, color=BLUE, zorder=3)
ax.semilogy(L[2:], T[2:], 'o', ms=8, color=BLUE, mec='white', mew=1.5, zorder=3)
ax.semilogy(L[1], T[1], marker='v', ms=10, color=BLUE, zorder=3)
for l, v, lab in [(0, 1, 'overall size: exactly 1'), (1, 8.97e-2, 'lopsided: at most 0.09'), (2, 4.158e-3, 'squeeze: 0.004'),
                  (6, 2.438e-8, '10⁻⁸'), (10, 8.497e-14, '10⁻¹³')]:
    ax.annotate(lab, (l, v), xytext=(8, 4), textcoords='offset points', fontsize=9.5)
ax.set_xticks(range(0, 11)); ax.set_xlabel('degree of the pattern on the layer (L)')
ax.set_ylabel('fraction that crosses the lift'); ax.grid(axis='y', color=GRID, lw=0.8); ax.set_ylim(1e-15, 5)
ax.set_title('What crosses the lift: only the overall size survives', loc='left', fontsize=12)
save(fig, 'F5_transmission.png')

# ---------- F6: holding radius against mass ----------
G, Msun, ly = 6.674e-11, 1.989e30, 9.4607e15
Lam = 3/(alpha_Gly*1e9*ly)**2
def rHE(M): return (3*G*M/(Lam*(c*1e3)**2))**(1/3)/ly        # light-years
def M_of(r_ly): return (r_ly*ly)**3*Lam*(c*1e3)**2/(3*G)/Msun
pts = [('Milky Way', M_of(3.5e6)), ('Local Group', M_of(4.8e6)), ('Virgo cluster', M_of(35e6))]
MN = (c*1e3)**2/(3*G*np.sqrt(Lam))/Msun
M = np.logspace(10, 24, 200)
fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.loglog(M, rHE(M*Msun)/1e6, color=BLUE, lw=2)
for name, m in pts + [('the universe\n(mass where the horizons merge)', MN)]:
    y = rHE(m*Msun)/1e6; ax.plot(m, y, 'o', ms=8, color='white', mec=INK, mew=1.5, zorder=3)
    off, ha = ((10, -26), 'left') if name == 'Milky Way' else ((-10, 6), 'right')
    ax.annotate(f'{name}\n{y:,.1f} Mly' if y < 1e3 else f'{name}\n{y/1e3:.1f} Gly', (m, y), xytext=off, textcoords='offset points', ha=ha, fontsize=9.5)
ax.set_xlabel('mass (solar masses)'); ax.set_ylabel('holding radius (millions of light-years)')
ax.grid(color=GRID, lw=0.8, which='major'); ax.set_xlim(1e10, 1e24)
ax.set_title('One rule at every scale: r = (3GM / Λc²)^(1/3)', loc='left', fontsize=12)
ax.text(1.5e20, 2, 'slope 1/3: eight times the mass,\ntwice the radius', fontsize=9.5, color=MUTED)
save(fig, 'F6_holding_radius.png')

# ---------- F7: the expansion curve and the slice's curvature ----------
tt = np.linspace(0.01, 30, 600); rr = R*np.sinh(3*tt/(2*aT))**(2/3); K = 1 - (rN/rr)**3
fig, (ax, bx) = plt.subplots(2, 1, figsize=(7.2, 6.4), sharex=True, gridspec_kw={'height_ratios': [1.4, 1]})
for a_ in (ax, bx): a_.axvline(t_fs, color=GRID, lw=1.2)
ax.plot(tt, rr, color=BLUE, lw=2); ax.plot(t_fs, rN, 'o', ms=8, color='white', mec=INK, mew=1.5)
ax.plot(t_now, x0*rN, 'o', ms=8, color='white', mec=INK, mew=1.5)
ax.annotate('inflection: 9.8 Gly, 7.5 Gyr\n(redshift 0.68)', (t_fs, rN), xytext=(t_fs+1, rN-6), fontsize=9.5)
ax.annotate('today', (t_now, x0*rN), xytext=(t_now+0.8, x0*rN-2.5), fontsize=9.5)
ax.text(2, 22, 'slowing', color=MUTED); ax.text(20, 22, 'speeding up', color=MUTED)
ax.set_ylabel('radius of the layer (Gly)'); ax.grid(axis='y', color=GRID, lw=0.8)
ax.set_title('The bend is the acceleration', loc='left', fontsize=12)
bx.axhline(0, color=MUTED, lw=1); bx.plot(tt, K, color=INK, lw=2)
bx.fill_between(tt, K, 0, where=K < 0, color=RED, alpha=0.12); bx.fill_between(tt, K, 0, where=K > 0, color=BLUE, alpha=0.12)
bx.set_ylim(-3, 1.3); bx.set_ylabel('curvature of the slice\nK, in units of 1/α²')
bx.set_xlabel('cosmic time since the beginning (billions of years)')
bx.text(4.6, -2.4, 'saddle-curved: the expansion slows', fontsize=9.5, color=RED)
bx.text(16, 0.55, 'sphere-curved: it speeds up', fontsize=9.5, color=BLUE)
save(fig, 'F7_bend.png')

# ---------- F4: flat and closed ----------
fig = plt.figure(figsize=(12, 5.2))
ax = fig.add_subplot(1, 2, 1, projection='3d')
def hopf_circle(theta, phi, n=300):   # fibre over base point (theta, phi), stereographic to R^3
    t = np.linspace(0, 2*np.pi, n); a = np.cos(theta/2); b = np.sin(theta/2)
    z1 = a*np.exp(1j*t); z2 = b*np.exp(1j*(t+phi))
    X = np.stack([z1.real, z1.imag, z2.real, z2.imag]); d = 1 - X[3]
    return X[0]/d, X[1]/d, X[2]/d
for i, phi in enumerate(np.linspace(0, 2*np.pi, 17)[:-1]):
    x, y, z = hopf_circle(np.pi/2, phi); ax.plot(x, y, z, color=BLUE, lw=1.3, alpha=0.85)
x, y, z = hopf_circle(0.0, 0.0); ax.plot(x, y, z, color=MUTED, lw=1.6)
ax.plot([0, 0], [0, 0], [-2.5, 2.5], color=MUTED, lw=1.6)
ax.set_box_aspect((1, 1, 1)); ax.set_axis_off(); ax.view_init(elev=62, azim=-60)
lim = 2.5; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
ax.set_title('(a) Circles that fill the three-sphere, every pair linked once\n(the Hopf fibration, drawn in ordinary space)', loc='left', fontsize=11)
bx = fig.add_subplot(1, 2, 2)
for v in np.arange(-4, 5, 1): bx.axvline(v, color=BLUE, lw=1.2, alpha=0.8)
for h in np.arange(-4, 5, 1): bx.axhline(h, color=MUTED, lw=1, alpha=0.7)
for k in np.arange(-8, 9, 1):
    xx = np.linspace(-4.5, 4.5, 10); bx.plot(xx, k - xx, color=RED, lw=1.6, alpha=0.85)
bx.set_xlim(-4.5, 4.5); bx.set_ylim(-4.5, 4.5); bx.set_aspect('equal')
bx.set_xlabel('χ  (the observers\' own direction across space)'); bx.set_ylabel('τ  (the observers\' own clocks)')
bx.set_xticks([]); bx.set_yticks([])
bx.set_title('(b) The observers\' chart', loc='left', fontsize=11)
from matplotlib.lines import Line2D
bx.legend(handles=[Line2D([], [], color=BLUE, lw=1.5, label='matter at rest'), Line2D([], [], color=MUTED, lw=1.2, label='flat slices: where clocks agree'),
                   Line2D([], [], color=RED, lw=1.6, label='the layer: what exists, at 45°')], loc='upper center', bbox_to_anchor=(0.5, -0.09), ncol=3, frameon=False, fontsize=9)
save(fig, 'F4_flat_and_closed.png')

# ---------- F8: the sound on the sky ----------
d = np.loadtxt(os.path.join(OUT, '../../../computations/planck_tt_likelihood/data/planck2018_plik_lite/cl_cmb_plik_v22.dat'))[:215]
ell, cl, sig = d[:, 0], d[:, 1], d[:, 2]; f = ell*(ell+1)/(2*np.pi)
fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.errorbar(ell, cl*f, yerr=sig*f, fmt='o', ms=2.6, color=INK, ecolor=MUTED, elinewidth=0.6, capsize=0)
peaks = [220.4, 537.7, 817.3, 1123.9]                     # CR_cosmology sec:intro, located on this spectrum
for p in peaks: ax.axvline(p, color=BLUE, lw=1, alpha=0.6, ls=(0, (4, 3)))
for a_, b_ in zip(peaks[:-1], peaks[1:]):
    ax.annotate('', xy=(b_, 6150), xytext=(a_, 6150), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1))
    ax.text((a_+b_)/2, 6250, f'{b_-a_:.0f}', ha='center', fontsize=9, color=BLUE)
ax.text(1180, 5000, 'peaks near an even grid: the comb,\nspacing 298. Where each tooth sits\nagainst that grid is its phase.', fontsize=9.5, color=BLUE)
ax.set_xlim(0, 2000); ax.set_ylim(0, 6700); ax.grid(axis='y', color=GRID, lw=0.8)
ax.set_xlabel('multipole: how finely the pattern divides the sky (about 180° ÷ its angular size)')
ax.set_ylabel('strength of the pattern (μK²)')
ax.set_title('The sound on the sky: the microwave background, measured by Planck', loc='left', fontsize=12)
save(fig, 'F8_sound.png')
print('alpha', alpha_Gly, 'R', R, 'lift', lift, 'back seam->turnaround', -u_bs, 't_fs', t_fs, 't_now', t_now, 'M_N', MN)
