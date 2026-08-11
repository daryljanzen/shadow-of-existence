import numpy as np
# Parametrize by the PHYSICAL variable (cosmic time tau~), which makes the bead smooth,
# and let tau~ carry the phase (r stays real, per thm:bead). r = sinh^{2/3}(3 tau~/2).
# Matter horn = real tau~. To reach r<0 we need sinh^{2/3} negative-real => 3tau~/2 must gain
# an imaginary part. Solve: for real r<0, what Im(tau~) is forced?

# r>0 (matter): tau~ real, Im=0.
# r<0 (antimatter): write r = -|r|. Need sinh^{2/3}(w) = -|r|  (real negative), w=3tau~/2.
#   sinh(w) = (-|r|)^{3/2} on the branch that lands sinh^{2/3} on the NEGATIVE real axis.
#   The two such branches give the TWO wings (conjugate). Track Im(tau~) across the lap.
def wings(r):
    # for r<0, the physical continuations: w such that sinh^{2/3}(w)=r (real<0), two conjugate roots
    # sinh(w) = r^{3/2} with r^{3/2} taken as |r|^{3/2} e^{i*(+-)pi/2}? -> gives w = (2/3)*... ; do numerically:
    target = complex(r)  # want sinh^{2/3}(w)=target
    # solve sinh(w) = target^{3/2} for the two conjugate branches
    base = abs(r)**1.5
    outs=[]
    for sgn in (+1,-1):
        s = 1j*sgn*base            # r^{3/2} placed on +-imaginary axis -> sinh^{2/3} lands on neg-real
        w = np.arcsinh(s)
        outs.append((2.0/3.0)*w)   # tau~ = (2/3) w
    return outs

print("Im(tau~) across the lap, BOTH wings (the continuous sweep, r real throughout):")
print("  r        wing+ Im(tau~)/ (pi/3)   wing- Im(tau~)/(pi/3)")
for r in [-0.02,-0.1,-0.3,-0.6,-1.0,-1.5,-3.0]:
    a,b = wings(r)
    print(f" {r:+.2f}     {a.imag/(np.pi/3):+.4f}              {b.imag/(np.pi/3):+.4f}")
print()
print("=> both wings sweep Im(tau~): 0 at r=0  ->  saturating at  -/+ pi/3  by r=-1 (=|r|^{3/2}=1),")
print("   then the antimatter horn runs at fixed Im(tau~)=-/+ pi/3 with Re(tau~) growing.")
print()
print("MECHANISM (derived, continuous): the straight ruling on the matter horn runs at Im(tau~)=0.")
print("It cannot cross the r=0 branch point staying real (r<0 would need sinh^{2/3} on the neg-real")
print("axis, impossible for real tau~). So at r=0 the bead LIFTS into imaginary tau~ -- that lift IS")
print("the equatorial lap/wrap -- sweeping to Im(tau~)=+-pi/3 (the two wings), and re-emerges as a")
print("straight ruling on the conjugate (antimatter) sheet, species flipped. The wrap is the")
print("branch-point detour forced at r=0; the horn is straight because there tau~ is real.")
print("dr/dtau~ -> 0 at r=0 (the pivot is a smooth stall, not a corner, in the tau~ parametrization).")
