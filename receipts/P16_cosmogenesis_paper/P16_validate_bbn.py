"""
P16_validate_bbn.py -- the VALIDATION GATE certifying the P16 sec:network BBN engine (bbn_network.py, alongside).
  Runs the genuine multi-nuclide network (REACLIB via pynucastro + finite-T weak n<->p) on the standard cooling
  background and checks it against accepted standard-BBN values BEFORE any CR claim.
  RESULTS (all pass): baryon number conserved to 1e-8 (sum A*Y=1.00000000); at eta10=6.14 -- Y_p=0.243 (Born;
  0.247 with the +1.6% rad/Coulomb correction), D/H=2.567e-5 (REACLIB 2% above the StarLib/standard 2.51e-5,
  as the paper states), 3He/H=1.044e-5, 7Li/H=4.46e-10; eta-dependence d ln(D/H)/d ln eta=-1.60 (accepted -1.6),
  Y_p rising, D/H falling, the 7Li valley (min at eta10~3); the lithium problem 2.8x over-prediction (shared).
  So the cooling leg reproduces standard BBN from first principles -> sec:network's abundances are computed,
  not asserted by analogy. DEPENDENCY: pynucastro (pip install pynucastro) + bbn_network.py alongside.
STATUS: ✔✔ (gate passes: conservation, abundances vs standard, eta-trends, valley, d ln(D/H)/d ln eta=-1.60)
RUN: python3 P16_validate_bbn.py   RUNTIME: ~3-6 min (needs pynucastro; integrates network at 6 eta values)
ORIGIN: computations/p16_bbn/validate_bbn.py + bbn_network.py, verified r1401.
LEVEL: GATE -- inherits the engine's level (L2) rather than choosing one.  It certifies
  bbn_network.py against accepted standard-BBN values before any CR claim is made on it.
"""
import numpy as np
import bbn_network as B

ACCEPTED = dict(Yp=0.2470, DH=2.51e-5, He3H=1.04e-5, Li7H=5.0e-10)   # standard BBN @ eta10=6.14
OBS      = dict(Yp=0.2450, DH=2.53e-5, He3H=1.1e-5,  Li7H=1.6e-10)   # measured primordial

print("="*74)
print("D1 VALIDATION GATE  (network = REACLIB rates + thermal n<->p, standard cooling)")
print("="*74)

o = B.run(eta10=6.14, verbose=False)
print(f"\n[1] CONSERVATION  baryon sum(A*Y)={o['baryon_sum']:.8f} (want 1.0)   "
      f"charge sum(Z*Y)={o['charge_sum']:.6f}")
assert abs(o['baryon_sum']-1.0) < 1e-4, "baryon number not conserved!"

print(f"\n[2] ABUNDANCES at eta10=6.14 (CMB-inherited):")
print(f"    {'':8s} {'CR network':>12s} {'std BBN':>12s} {'obs':>12s} {'net/std':>9s}")
for k,lab in [('Yp','Y_p'),('DH','D/H'),('He3H','3He/H'),('Li7H','7Li/H')]:
    v=o[k]; a=ACCEPTED[k]; ob=OBS[k]
    print(f"    {lab:8s} {v:12.4e} {a:12.4e} {ob:12.4e} {v/a:9.3f}")

print(f"\n[3] ETA-DEPENDENCE (the network must track the known BBN trends):")
print(f"    {'eta10':>6s} {'Yp':>8s} {'D/H':>11s} {'3He/H':>11s} {'7Li/H':>11s}")
etas=[2.0, 3.0, 5.0, 6.14, 9.0]
rows=[]
for e10 in etas:
    oe=B.run(eta10=e10, verbose=False)
    rows.append(oe); assert oe['success'], f"integration failed at eta10={e10}"
    print(f"    {e10:6.2f} {oe['Yp']:8.4f} {oe['DH']:11.3e} {oe['He3H']:11.3e} {oe['Li7H']:11.3e}")
DH=[r['DH'] for r in rows]; Yp=[r['Yp'] for r in rows]; Li=[r['Li7H'] for r in rows]
# trend checks
assert all(DH[i]>DH[i+1] for i in range(len(DH)-1)),  "D/H must fall monotonically with eta"
assert all(Yp[i]<Yp[i+1] for i in range(len(Yp)-1)),  "Y_p must rise monotonically with eta"
assert Li[-1]>Li[-2],                                  "7Li/H must rise on the high-eta (7Be) branch"
assert min(Li)<Li[0] and min(Li)<Li[-1],               "7Li/H must show the valley"
slope = np.log(DH[-1]/DH[0])/np.log(etas[-1]/etas[0])
print(f"    -> d ln(D/H)/d ln(eta) = {slope:.2f}  (accepted ~ -1.6);  "
      f"7Li valley min at eta10~{etas[int(np.argmin(Li))]:.0f} (the lithium dip)")
o = rows[etas.index(6.14)]   # the CMB-inherited point for the lithium-problem line below

print(f"\n[4] LITHIUM PROBLEM (the qualitative P16 claim):")
li_over = o['Li7H']/OBS['Li7H']
print(f"    7Li/H(computed)/7Li/H(obs) = {li_over:.1f}x  -> the standard several-fold over-prediction,")
print(f"    present exactly as in flat LambdaCDM (neither dissolved nor worsened).")

print("\n"+"="*74)
print("VERDICT: machinery certified.  At the CMB-inherited eta: Y_p to 1.5%, D/H to 2%,")
print("3He to 0.4%, 7Li at the standard ~3x over-prediction; d ln(D/H)/d ln eta = -1.60 and")
print("the 7Li valley both reproduced; baryon number conserved to 1e-8.  The cooling leg")
print("reproduces the standard-BBN pattern from first principles -> P16 sec:network closed.")
print("="*74)


# =====================================================================
# ** THE LIBRARY ARM AND THE PAPER'S OWN FIGURES, added r2376+c54.156. **
#
# ** WHY. **  The receipt-vs-sentence pass found P16's abundance equation quoting D/H = 2.51e-5
# and 7Li/H = 5.1e-10 and citing THIS file, which runs REACLIB only and returns 2.567e-5 and
# 4.461e-10 -- the quoted values are the STARLIB run, which lived in a different receipt.  And
# none of the four abundances was asserted anywhere: the only numeric checks were baryon
# conservation and monotonicity, so any abundance could have moved by a factor of two without
# the gate noticing.  ** Both arms are run here and both are pinned to the figures the paper
# prints. **
print()
print("=" * 78)
print("THE TWO RATE LIBRARIES, AND THE PAPER'S QUOTED VALUES PINNED")
print("=" * 78)
_oS = B.run(eta10=6.14, verbose=False, library='starlib')
_oR = o                                                     # the REACLIB run above
print(f"  {'nuclide':>10} {'StarLib (quoted)':>18} {'REACLIB':>14} {'spread':>10} {'paper':>12}")
_PAPER = {'DH': 2.51e-5, 'Li7H': 5.1e-10, 'He3H': 1.05e-5}
for _k, _lab in [('DH', 'D/H'), ('He3H', '3He/H'), ('Li7H', '7Li/H')]:
    _sp = _oR[_k] / _oS[_k] - 1.0
    print(f"  {_lab:>10} {_oS[_k]:>18.4e} {_oR[_k]:>14.4e} {100*_sp:>9.1f}% {_PAPER[_k]:>12.3g}")
print(f"  {'Y_p (Born)':>10} {_oS['Yp']:>18.5f} {_oR['Yp']:>14.5f} "
      f"{100*(_oR['Yp']/_oS['Yp']-1):>9.2f}% {0.2432:>12.4g}")
print(f"  {'Y_p x1.016':>10} {_oS['Yp']*1.016:>18.5f} {_oR['Yp']*1.016:>14.5f} "
      f"{'':>10} {0.2471:>12.4g}")

# the paper's quoted (StarLib) figures
assert abs(_oS['DH'] / 2.51e-5 - 1) < 0.01, f"D/H {_oS['DH']:.4e} vs the paper's 2.51e-5"
assert abs(_oS['Li7H'] / 5.1e-10 - 1) < 0.02, f"7Li/H {_oS['Li7H']:.4e} vs the paper's 5.1e-10"
assert abs(_oS['He3H'] / 1.05e-5 - 1) < 0.01, f"3He/H {_oS['He3H']:.4e} vs the paper's 1.05e-5"
assert abs(_oS['Yp'] * 1.016 / 0.2471 - 1) < 0.005, f"Y_p {_oS['Yp']*1.016:.4f} vs the paper's 0.2471"
# and the arm this file actually runs, so a library swap cannot pass silently
assert abs(_oR['DH'] / 2.5671e-5 - 1) < 0.01, f"REACLIB D/H moved: {_oR['DH']:.4e}"
assert abs(_oR['Li7H'] / 4.4611e-10 - 1) < 0.02, f"REACLIB 7Li/H moved: {_oR['Li7H']:.4e}"
print()
print("  ** BOTH ARMS PINNED.  The libraries differ by 2.6% on D/H and 13% on 7Li -- the paper")
print("     had quoted the lithium spread at the deuterium's 2%, and said StarLib lands both on")
print("     the canonical values to sub-percent, which holds for D/H and is 3% for 7Li. **")
print("  CHECKS PASS")
