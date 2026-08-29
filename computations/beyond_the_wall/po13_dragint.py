#!/usr/bin/env python3
"""TEST 1 -- THE DRAG INTEGRAL.  The last term in the baryon Euler oscillator:
   S'' + (H R/(1+R)) S' + k^2 c_s^2 S = forcing.
R is identical in both arms; the wells (r3540) are ~1.  The ONLY remaining arm-difference is H in the
drag coefficient -- CR's geometric (radiation-free) comoving rate vs the control's radiation-included one.

Integrate the drag coefficient D = H_comov * R/(1+R) over the mode's sub-horizon history to
recombination, both arms, on the matched acoustic-phase clock, modes q=1,2,3.  Report CR/control.
This is the damping the oscillator actually experiences (amplitude ~ exp(-1/2 INT D deta)).
"""
import sys, numpy as np
from scipy.integrate import cumulative_trapezoid

SD = sys.argv[1] if len(sys.argv) > 1 else '.'
C = 299792.458
OMBH2, Z_REC = 0.0224, 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)

# per-arm background: drag H is Hc_of = a*Hphys(a)/C.  CR = geometric (no OR); control = full (with OR).
PAR = dict(cr=dict(H0=73.00, OM=0.3066, rad=False),
           lcdm=dict(H0=67.40, OM=0.3150, rad=True))


def Hcomov(a, p):
    OM, OL = p['OM'], 1.0 - p['OM']
    OR = 4.15e-5 / (p['H0'] / 100) ** 2
    t = OM / a ** 3 + OL + (OR / a ** 4 if p['rad'] else 0.0)
    return a * p['H0'] * np.sqrt(t) / C            # comoving Hubble 1/Mpc


def load(f):
    d = np.load(f)
    return dict(eta=d['eta'], a=d['a'], phi=d['phi'], q=d['qpk'], k=d['kpk'],
                erec=float(d['eta_rec']), arm=str(d['arm']))


def drag_metrics(D, i, p):
    eta, a, k = D['eta'], D['a'], float(D['k'][i])
    R = RB_REC * a / A_REC
    H = Hcomov(a, p)
    drag = H * R / (1.0 + R)                         # the oscillator friction coefficient
    cs = 1.0 / np.sqrt(3.0 * (1.0 + R))
    rs = np.concatenate([[0.0], cumulative_trapezoid(cs, eta)])
    phase = k * rs
    m = (k * eta > 1.0) & (eta <= D['erec'])
    e, ph, dr = eta[m], phase[m], drag[m]
    return dict(Dint_eta=np.trapezoid(dr, e),                       # accumulated drag INT D deta
                Dbar_ph=np.trapezoid(dr, ph) / (ph[-1] - ph[0]),   # phase-avg (matched clock)
                Dbar_et=np.trapezoid(dr, e) / (e[-1] - e[0]),
                Hentry=float(H[m][0]), Hrec=float(H[m][-1]))


cr = load(f"{SD}/cr_wi.npz")
ct = load(f"{SD}/lcdm_wi.npz")
print("=" * 84)
print("  TEST 1 -- DRAG INTEGRAL  D = H R/(1+R)  over the oscillation history to recombination")
print("  H_drag: CR = geometric (radiation-free) ; control = radiation-included ; R identical")
print("=" * 84)
print(f"  {'peak(q)':>8} | {'INT D deta CR':>14}{'CTL':>12}{'RATIO':>8} |"
      f"{'<D>phase RATIO':>16}{'<D>eta RATIO':>14} | {'H_entry CR/CTL':>15}")
for i in range(3):
    mc = drag_metrics(cr, i, PAR['cr'])
    mt = drag_metrics(ct, i, PAR['lcdm'])
    r_int = mc['Dint_eta'] / mt['Dint_eta']
    r_ph = mc['Dbar_ph'] / mt['Dbar_ph']
    r_et = mc['Dbar_et'] / mt['Dbar_et']
    print(f"  {float(cr['q'][i]):>8.2f} | {mc['Dint_eta']:>14.4e}{mt['Dint_eta']:>12.4e}{r_int:>8.3f} |"
          f"{r_ph:>16.3f}{r_et:>14.3f} | {mc['Hentry']/mt['Hentry']:>15.3f}")
print()
print("  drag ratio < 1  => CR experiences LESS drag (its geometric H is lower); drag FIGHTS the")
print("                     suppression, doesn't cause it -- the 2x must be even larger than measured.")
print("  drag ratio ~ 2  => CR experiences ~2x the drag; the damping is the effective-load source.")
