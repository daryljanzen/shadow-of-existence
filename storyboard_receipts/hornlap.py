import numpy as np
np.set_printoptions(precision=4, suppress=True)
# GOAL: derive the CONTINUOUS horn->lap mechanism, not describe endpoints.
# Setup: the slicing curve / bead on the SdS geometry, areal radius r(l) along the curve,
# with the embedding boing X1(r) and cosmic-time phase tau~(r). Trace ONE bead from the horn
# (large r, real tau~, straight ruling) inward THROUGH r=0, and watch (a) the ruling direction,
# (b) where tau~ goes complex, (c) the species/wrap-sense flip.
#
# Bead law (2M=1, alpha=1):  r = sinh^{2/3}(3 tau~/2).  Invert on the real matter leg, then continue.
# tau~(r) = (2/3) arcsinh(r^{3/2}).  Continue r downward through 0 onto r<0.

def tau_of_r(r):
    # r^{3/2} as a complex-analytic continuation (principal branch)
    s = (complex(r))**1.5
    return (2.0/3.0)*np.arcsinh(s)

print("Trace the bead inward:  r : +horn -> 0 -> -horn.  Watch Im(tau~) and the wrap.")
print(" r        tau~ = Re + i Im            |  Im(tau~)   phase(r^{3/2})/deg")
for r in [2.0, 1.0, 0.5, 0.2, 0.05, 0.0, -0.05, -0.2, -0.5, -1.0, -2.0]:
    t = tau_of_r(r) if r!=0 else 0j
    s = (complex(r))**1.5
    print(f"{r:+.2f}   {t.real:+.4f} {t.imag:+.4f} i      |  {t.imag:+.4f}    {np.degrees(np.angle(s)):+.1f}")

print()
print("--- the mechanism, read off the continuation ---")
# On the horn (r>0): r^{3/2} real positive -> arcsinh real -> tau~ REAL. Ruling runs straight, real time.
# As r->0+: r^{3/2}->0, tau~->0 (the seam approaches).
# Cross to r<0: r = |r| e^{i pi}, so r^{3/2} = |r|^{3/2} e^{i 3pi/2} = -i|r|^{3/2} -> PURELY IMAGINARY.
#   arcsinh(-i x) = -i arcsin(x): tau~ becomes purely IMAGINARY -> the phase e^{i pi} of r (the wrap)
#   is what pushes tau~ off the real axis. The 'wrap' is r acquiring phase pi; tau~ answering with i.
print("On r>0: r^{3/2} real  -> tau~ real            (straight ruling on the horn, real cosmic time)")
print("At r=0: r^{3/2}=0     -> tau~=0               (the seam / the pivot; all sheets meet)")
print("On r<0: r=|r|e^{i.pi} -> r^{3/2}=-i|r|^{3/2}  -> tau~ purely imaginary (the lap: the wrap IS r's phase pi,")
print("        and tau~ going imaginary IS the equatorial lap. arcsinh(-ix) = -i arcsin(x).)")
print()
# So the CONTINUOUS mechanism: taking r from +horn to -horn forces r to travel through the phase
# from 0 to pi. THAT phase travel is the wrap around the equator; tau~ tracks it into the imaginary
# direction (the lap). r=0 is where the phase passes... let's confirm the wrap is monotone & the
# species (sign of the REAL r reached) flips exactly at the r=0 pivot.
print("Check: is the 'wrap' (accumulated phase of r^{3/2}) continuous & monotone from horn to horn?")
for r in [1.0,0.3,0.05,-0.05,-0.3,-1.0]:
    s=(complex(r))**1.5
    print(f"  r={r:+.2f}: phase(r^{{3/2}})={np.degrees(np.angle(s)):+7.1f} deg   (0 on +horn, ->  -270=+90 region as r<0)")
