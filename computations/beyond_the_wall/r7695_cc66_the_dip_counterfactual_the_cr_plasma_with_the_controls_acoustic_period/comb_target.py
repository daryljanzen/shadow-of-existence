"""r7695+cc66 -- WHAT `COMBRHO` MUST BE SET TO, MEASURED ON THE BANKS THE STATISTIC READS.

Gate 3 is "the comb period in the output must come out at the control's".  That sentence has no
content until it names WHICH period, in WHICH coordinate, read by WHICH fitter -- so this script
reads them, from the banks and the fitter the dip test itself uses, before the rebuild is launched.

  * the statistic's source-side coordinate is `QK = k * r_s / pi`, each bank by its OWN `r_s`;
  * the comb is `own_comb.comb(QK, S_i**2)`, whose `[1]` is the fitted PERIOD in that coordinate;
  * `COMBRHO` multiplies the solver's `k`, so an oscillation of period `T_a` in `QK` becomes one of
    period `T_a / rho`.  Matching the control therefore wants `rho = T_a / T_c`.

NOTHING HERE IS DERIVED FROM `r_s` ALONE.  The r_s ratio (1.0081886775) is what the comb period
WOULD be if the source oscillated exactly as cos(k r_s); the fitted periods say whether it does.
The gate reads the fit, so the switch is set from the fit.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(BW, 'r7637_70_own_comb_statistic'))
import own_comb as OC                                                              # noqa: E402

PR = {t: dict(np.load(os.path.join(SP, n))) for t, n in
      (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
SO = {t: dict(np.load(os.path.join(SP, n))) for t, n in
      (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', 'r6911_source_cr_leafrec1.npz'))}
QL = {t: PR[t]['ls'].astype(float) / float(PR[t]['l_A']) for t in PR}
QK = {t: SO[t]['k'] * float(SO[t]['r_s']) / np.pi for t in SO}
B = {t: dict(QL=QL[t], QK=QK[t], Dl=np.asarray(PR[t]['Dl'], float),
             S2=np.asarray(SO[t]['S_i'], float) ** 2) for t in PR}

C = OC.retention_combs(B)
print("  THE FITTED COMBS ON THE BANKS THE DIP TEST READS")
print("    side   coordinate        control        arm (CR)      arm/control")
for s, nm in (('K', 'QK = k r_s/pi'), ('L', 'QL = l/l_A  ')):
    Tc, pc = C['lcdm'][s]
    Ta, pa = C['cr'][s]
    print(f"    {s}      {nm}    T={Tc:.6f}     T={Ta:.6f}     {Ta/Tc:.9f}")
    print(f"                             phi={pc:+.5f}    phi={pa:+.5f}    "
          f"dphi={(pa - pc + np.pi) % (2*np.pi) - np.pi:+.5f}")

TKc, TKa = C['lcdm']['K'][0], C['cr']['K'][0]
TLc, TLa = C['lcdm']['L'][0], C['cr']['L'][0]
rs = float(SO['cr']['r_s']) / float(SO['lcdm']['r_s'])
print()
print(f"  the r_s ratio                        {rs:.9f}   ({100*(rs-1):+.4f} per cent)")
print(f"  the SOURCE comb's period ratio       {TKa/TKc:.9f}   ({100*(TKa/TKc-1):+.4f} per cent)")
print(f"  the D_l comb's period ratio          {TLa/TLc:.9f}   ({100*(TLa/TLc-1):+.4f} per cent)")
print()
print(f"  ⇒ COMBRHO = T_K(arm)/T_K(control) =  {TKa/TKc:.10f}")
print(f"    and gate 3's TARGET is T_K(arm, rebuilt) = {TKc:.6f}, the control's own fitted period,")
print(f"    which the rebuild must reach from {TKa:.6f} -- a move of {TKa-TKc:+.6f}.")
print()
print("  ⌗ the fitter's own resolution, so the gate has a tolerance it did not invent:")
for t in ('lcdm', 'cr'):
    _x, _y = B[t]['QK'], B[t]['S2']
    _T = OC.comb(_x, _y)[1]
    _h = [OC.comb(_x[i::2], _y[i::2])[1] for i in (0, 1)]
    print(f"    {t:5s} T={_T:.6f}; on the two half-grids {_h[0]:.6f} / {_h[1]:.6f} "
          f"(spread {abs(_h[0]-_h[1]):.6f})")
