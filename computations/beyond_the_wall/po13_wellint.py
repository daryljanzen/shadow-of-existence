#!/usr/bin/env python3
"""THE WELL-INTEGRAL THE BARYONS SEE.  Make the effective-load claim a NUMBER.

The code's photon/baryon Euler equation (ACOUSTIC_two_arm.py out[:,3]) reduces to the acoustic
oscillator  S'' + (H R/(1+R)) S' + k^2 c_s^2 S = forcing,  S = delta_g/4 = Theta_0, whose baryon-
loaded zero-point is  S_eq = -(1+R) Psi.  The BARYON part of that offset, -R*Psi, is the term that
carries R and Phi together and sets the compression/rarefaction (odd-even) asymmetry -- distinct from
the Phi'*theta driving work (already shown to be OUT).

R(a) = RB_REC * a/A_REC is IDENTICAL in both arms (same OMBH2, same Z_REC), so in the CR/control ratio
the whole R-normalisation cancels and what remains is the WELL history the baryons ride.  The test:
the effective-load multiplier PREDICTED here (offset ratio) vs the 1.82-2.00 MEASURED from the heights.

Integrand: O(eta) = R(eta) * |Phi(eta)|  (Psi ~ Phi; shear correction few %, common to both arms).
History = sub-horizon oscillation, k*eta > 1 up to recombination.  Averaged over ACOUSTIC PHASE
phi = k*rs (the clock MATCHED between arms for a matched mode q = k rs/pi) so the ratio is clock-clean;
eta-average and eta-integral reported alongside for robustness.
"""
import sys, numpy as np
from scipy.integrate import cumulative_trapezoid

SD = sys.argv[1] if len(sys.argv) > 1 else '.'

# constants (identical both arms): RB_REC = 31500 OMBH2 /(2.7255/2.7)^4 /(1+Z_REC); A_REC=1/(1+Z_REC)
OMBH2, Z_REC = 0.0224, 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)


def load(f):
    d = np.load(f)
    return dict(eta=d['eta'], a=d['a'], phi=d['phi'], dg=d['dg'], tg=d['tg'],
                q=d['qpk'], k=d['kpk'], erec=float(d['eta_rec']), es=float(d['eta_s']),
                arm=str(d['arm']))


def well_metrics(D, i):
    """for mode i: return dict of offset metrics over the sub-horizon oscillation history."""
    eta, a, phi, k = D['eta'], D['a'], D['phi'][i], float(D['k'][i])
    R = RB_REC * a / A_REC
    cs = 1.0 / np.sqrt(3.0 * (1.0 + R))
    rs = np.concatenate([[0.0], cumulative_trapezoid(cs, eta)])   # sound horizon on this grid
    phase = k * rs                                                # acoustic phase k*rs
    O = R * np.abs(phi)                                           # baryon zero-point offset  R*|Phi|
    # sub-horizon oscillation window: k*eta>1 up to recombination
    m = (k * eta > 1.0) & (eta <= D['erec'])
    if m.sum() < 5:
        return None
    e, ph, o, aphi, Rw = eta[m], phase[m], O[m], np.abs(phi[m]), R[m]
    # phase-averaged offset (matched clock), eta-averaged offset, eta-integral, well-only average
    Obar_ph = np.trapezoid(o, ph) / (ph[-1] - ph[0])
    Obar_et = np.trapezoid(o, e) / (e[-1] - e[0])
    Oint_et = np.trapezoid(o, e)
    Wbar_ph = np.trapezoid(aphi, ph) / (ph[-1] - ph[0])              # <|Phi|> phase-avg (well only)
    return dict(Obar_ph=Obar_ph, Obar_et=Obar_et, Oint_et=Oint_et, Wbar_ph=Wbar_ph,
                phi0=float(np.abs(phi[np.argmax(k*eta > 1.0)])),  # |Phi| at horizon entry
                phirec=float(aphi[-1]), Rrec=float(Rw[-1]),
                nph=float(ph[-1] - ph[0]), neta=float(e[-1] - e[0]))


cr = load(f"{SD}/cr_wi.npz")
ct = load(f"{SD}/lcdm_wi.npz")
print("=" * 82)
print("  WELL-INTEGRAL THE BARYONS SEE  --  offset  R*|Phi|  over the oscillation history")
print("  STACKPERT=1 GSRC=1 HIER KCONT ; matched peak modes ; R(a) identical -> cancels in ratio")
print("=" * 82)
print(f"  arms: CR eta_s={cr['es']:.1f} eta_rec={cr['erec']:.1f} q={[round(float(x),2) for x in cr['q']]}"
      f"  |  CTL eta_s={ct['es']:.1f} eta_rec={ct['erec']:.1f} q={[round(float(x),2) for x in ct['q']]}")
print(f"  R_rec = RB_REC = {RB_REC:.4f}  (same both arms)")
print()
print(f"  {'peak':>5}{'q_CR':>7}{'q_CT':>7} | {'<R|Phi|>ph CR':>14}{'CTL':>10}{'RATIO':>8} |"
      f"{'<R|Phi|>et RATIO':>18}{'INTeta RATIO':>14}")
rows = []
for i in range(3):
    mc, mt = well_metrics(cr, i), well_metrics(ct, i)
    if mc is None or mt is None:
        print(f"  {i+1:>5}   (window too short)"); rows.append(None); continue
    r_ph = mc['Obar_ph'] / mt['Obar_ph']
    r_et = mc['Obar_et'] / mt['Obar_et']
    r_int = mc['Oint_et'] / mt['Oint_et']
    rows.append((r_ph, r_et, r_int, mc, mt))
    print(f"  {i+1:>5}{float(cr['q'][i]):>7.2f}{float(ct['q'][i]):>7.2f} | "
          f"{mc['Obar_ph']:>14.4e}{mt['Obar_ph']:>10.4e}{r_ph:>8.3f} |"
          f"{r_et:>18.3f}{r_int:>14.3f}")
print()
print("  the PREDICTED effective-load multiplier is the phase-averaged offset ratio <R|Phi|>ph CR/CTL.")
print("  MEASURED (independent, RBFAC scan r3539): effective-R multiplier at PHYSICAL R=1.0 is x2.00")
print("  (it climbs x1.82->2.00 across R=0.5->1.0; the axis is R, NOT peak number).")
print()
print(f"  {'peak':>5}{'PRED mult (ph)':>16}{'|Phi|_entry CR/CTL':>20}{'|Phi|_rec CR/CTL':>18}")
for i in range(3):
    if rows[i] is None:
        continue
    r_ph, _, _, mc, mt = rows[i]
    print(f"  {i+1:>5}{r_ph:>16.3f}{mc['phi0']/mt['phi0']:>20.3f}"
          f"{mc['phirec']/mt['phirec']:>18.3f}")
print(f"\n  PREDICTED (wells) ~= {min(good_pre:=[rows[i][0] for i in range(3) if rows[i]]):.2f}"
      f"-{max(good_pre):.2f}   vs   MEASURED (heights) = 2.00   at physical R=1.0")
print()
# trend
good = [rows[i][0] for i in range(3) if rows[i] is not None]
if len(good) >= 2:
    print(f"  PRED multiplier trend across peaks: {[round(x,3) for x in good]}  "
          f"({'RISES' if good[-1] > good[0] else 'FALLS/FLAT'} q1->q3)")
print()
print("  VERDICT LOGIC:")
print("   ratio ~2 and matches 1.82-2.00  -> chain CLOSED: Phi-decay = effective load = alternation.")
print("   ratio ~1                         -> wells are NOT the load; ~2x has another source.")
print("   ratio rises q1->q3 like measured -> also accounts for the ~10% multiplier climb.")
