"""PROJ — THE PROJECTION GATE.  Run this before trusting any C_l from this machinery.

WHAT IT TESTS.  C_l = sum_k P(k) Delta_l(k)^2 is L3 -- the E=1 projection, the one layer P6's Rule 1
exists to hold apart from the geometry.  It had never been validated, only converged.

THE CLOSED FORM.  For a DELTA-FUNCTION source (Delta_l = j_l(kD)) and a scale-invariant spectrum,
        int dk k^{-1} j_l(kD)^2 * k = 1 / (2 l (l+1))       exactly,
so l(l+1)C_l MUST come out FLAT.  There is no physics in this test: any tilt is the projection's.

*** WHAT IT CAUGHT (r2125). ***  The k-sum was truncated at kD = 900 for l up to 899, which LOOKS safe
and is not: j_l(x) carries substantial weight well above x = l, and the captured fraction depends only
on kD_max / l --
        kD_max/l :   2      3      4      6      8
        captured : 86.6%  94.3%  96.8%  98.6%  99.2%      (identical for l=220..899)
so a FIXED cutoff cannot serve all l and always bites hardest at the top.  At kD=900 the gate read
0.969 / 0.802 / 0.428 at l = 220 / 536 / 813 -- a factor 25 tilt across the range, with EXACTLY the
k^2-deficit shape of a physical damping term.  It survived four rounds of physics hypotheses (r_D, the
envelope convention, the visibility, the ionisation tail, the tight-coupling validity, radiation
driving) because it is formally indistinguishable from suppression -- P6's point precisely: a
perspectival artefact is real as a fact about pi, and formal likeness does not sort the classes.
Only exhibiting pi against a case where pi is known in closed form does.

USE.  Raise KMAXL until the gate is flat to the tolerance you need at your highest l.  A real source is
damped, so the physics converges sooner than the bare gate: the photon hierarchy converged by
kD ~ 1800-2600 (P1/P3 changing 2.432 -> 2.415) while the gate at kD=2600 still reads 0.903 at l=1120.
"""
import numpy as np
from scipy.special import spherical_jn
D = 13865.0
print("  DELTA-SOURCE PROJECTION GATE:  l(l+1)C_l must be FLAT  (n_s = 1)")
print("     kD_max      l=220     l=536     l=813    l=1120")
for KM in (900., 1800., 2600., 4000.):
    Ls = np.arange(2, int(KM/2.75)+4); lL = np.sqrt(Ls*(Ls+2))*2.75
    kk = lL[lL <= KM]/D; P = kk**0/kk*np.gradient(kk)
    row = [np.sum(P*spherical_jn(l, kk*D)**2)/(1.0/(2*l*(l+1))) for l in (220,536,813,1120)]
    print("   %7.0f   "%KM + "  ".join("%8.3f"%v for v in row))
    if KM == 900.:
        assert row[2] < 0.5, "the r2125 defect should read ~0.43 at l=813"
    if KM == 4000.:
        assert min(row) > 0.95, "kD=4000 should be flat to better than 5% out to l=1120"
print()
print("  capture fraction depends only on kD_max/l:")
for l in (220, 536, 813):
    x = np.linspace(1e-3, 40000., 400000); I = spherical_jn(l, x)**2/x; tot = np.trapezoid(I, x)
    print("    l=%4d  "%l + "  ".join("%.1f%%"%(100*np.trapezoid(I[x<=m*l], x[x<=m*l])/tot) for m in (2,3,4,6,8)))
print("            (kD_max/l =  2      3      4      6      8)")
