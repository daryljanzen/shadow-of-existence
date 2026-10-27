"""r7611+70: P15_the_tilt_is_the_wrong_absorber on the faithful exponent.  dn_eff(l) = -2*ALPHA*(r^2-1)*(l/1951.9)^2
against the as-built -2*(r^2-1)*(l/1362)^2.  Exact arithmetic; nothing fitted."""
import numpy as np
r, k = 1.0926, 1.0926 ** 2 - 1
ALPHA, LF, LD0 = 1.70, 1951.9, 1362.0
LEFF = LF / ALPHA ** 0.5
def dn(l, ld): return -2 * k * (l / ld) ** 2
print(f"  l_eff = {LEFF:.1f};  s = (1362/l_eff)^2 = {(LD0 / LEFF) ** 2:.4f}")
print(f"  {'l':>6}{'as built':>11}{'faithful':>11}")
for l in (30, 100, 500, 1000, 1759, 2508):
    print(f"  {l:>6}{dn(l, LD0):>11.4f}{dn(l, LEFF):>11.4f}")
print(f"  swing over 30-2508: as built {dn(2508, LD0) / dn(30, LD0):.0f}, faithful {dn(2508, LEFF) / dn(30, LEFF):.0f}")
for ld, lab in ((LD0, 'as built'), (LEFF, 'faithful')):
    print(f"  {lab}: the reported -0.0304 equals dn_eff at l = {np.sqrt(0.0304 / (2 * k)) * ld:.0f} only")
