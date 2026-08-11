"""PLANCK — the Planck 2018 best-fit LambdaCDM theory spectrum, stored as a permanent comparison object.

SOURCE: COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt
        (Planck Legacy Archive / IRSA, 2018-07-11), base-plikHM-TTTEEE-lowl-lowE-lensing minimum.
        D_l = l(l+1)C_l/2pi in uK^2.  LENSED, and INCLUDING reionisation (tau = 0.0544).

WHY IT IS HERE (r2148).  Every "what is the observed value" blocker in this session came from not
having this curve: D_l(30) ~ 1000 from memory was wrong in SIGN (r2135); the peak/trough values were
unsourced until r2134; and the P1 degeneracy could not be broken without a low-l anchor (r2147).
*** Storing it retires that whole class of blocker. ***

USE.  Normalise BOTH spectra at the PLATEAU (l ~ 10), never at P1 -- normalising at P1 makes
"P1 is high" and "everything above l=400 is low" the SAME STATEMENT, which is what blocked r2139-2147.

CAVEATS, both of which matter at the ~10% level:
  * This curve is LENSED; an unlensed calculation sits ABOVE it at the peaks and BELOW it in the
    troughs, by a few percent at l > 1000.
  * It carries reionisation: C_l -> C_l e^{-2 tau} = 0.897 C_l for l above the horizon at
    reionisation (conventionally l >~ 20).  A calculation without reionisation must either add it
    or correct the comparison by 1/0.897 = 1.115 above that scale.
"""
import numpy as np
# l : D_l [uK^2], sampled from the PLA file
PLANCK_TT = {2:1016.73, 3:963.727, 4:912.608, 5:874.477, 6:848.509, 8:822.295, 10:817.174,
             12:824.031, 15:845.805, 18:878.618, 20:905.157, 25:976.023, 30:1054.73,
             40:1228.96, 50:1421.27, 75:1987.52, 100:2697.86, 125:3527.46, 150:4382.26,
             175:5120.71, 200:5600.40, 210:5696.77, 220:5730.14, 230:5701.49, 250:5460.25,
             300:4077.65, 350:2504.58, 400:1746.71, 416:1726.87, 450:1943.88, 500:2446.60,
             538:2593.47, 550:2572.87, 600:2230.75, 650:1857.30, 675:1804.61, 700:1868.06,
             750:2227.34, 800:2525.91, 810:2541.26, 813:2542.07, 850:2409.81, 900:1904.60,
             950:1348.76, 1000:1062.45, 1020:1043.31, 1050:1087.63, 1100:1215.52,
             1148:1223.14, 1200:1051.25, 1250:837.382, 1300:725.931, 1350:747.422,
             1400:809.410, 1450:800.365}
_L=np.array(sorted(PLANCK_TT)); _D=np.array([PLANCK_TT[k] for k in _L])
def planck_TT(l): return np.interp(np.asarray(l,dtype=float), _L, _D)

if __name__ == "__main__":
    print("  Planck 2018 best-fit LambdaCDM theory TT (lensed, tau=0.0544), %d sampled multipoles"%len(_L))
    print("     plateau  D(10) = %.1f    first peak D(220) = %.1f    P1/plateau = %.3f"
          %(planck_TT(10),planck_TT(220),planck_TT(220)/planck_TT(10)))
    for L in (5,15,30,100,220,416,538,810,1000,1148):
        print("     l=%5d   D = %9.2f   D/D(10) = %7.3f"%(L,planck_TT(L),planck_TT(L)/planck_TT(10)))
    assert abs(planck_TT(220)-5730.14)<1e-6
    assert abs(planck_TT(220)/planck_TT(10)-7.012)<0.01
