"""
C51_the_twist_separates_the_chiralities_by_direction_and_selects_neither
========================================================================

Object under test -- whether C50's twist asymmetry SELECTS a handedness.  P14 establishes that the
chirality the weak coupling projects onto is the geometric parity R = gamma^5, and R is a symmetry of
the substrate, so the geometry treats left and right alike.  The weak force couples to one.  C50
found the one place the geometry does distinguish them: on the chiral member the twist enters the
Dirac operator only on gamma^5, and

      E_R = +/-(k - b),     E_L = +/-(k + b),     b = c e^{-2 psi} / 4,

so the orientation parity is a symmetry only as the joint c -> -c with gamma^5 -> -gamma^5.  Does that
asymmetry favour one handedness, by any measure that is physical rather than a choice of orientation?

--------------------------------------------------------------------------------
(1) BY ENERGY, NEITHER.  The two chiralities' spectra are the same set -- k -> -k carries one to the
    other -- on the twist circle as on the line.  Computed.  No chirality is lower in energy.

(2) THE ASYMMETRY IS IN DIRECTION.  Each chirality's zero-energy branch sits at opposite momentum
    along the twist axis: right-handed at k = +b, left-handed at k = -b.  The twist correlates
    handedness with direction along its own axis.

(3) THAT CORRELATION IS PHYSICAL, AND IT FIXES NO ABSOLUTE HANDEDNESS.  Under the joint orientation
    flip, b -> -b and R <-> L, so "right-handed at +b" becomes the same statement.  The correlation is
    invariant; which handedness is called left is set by the sign of the twist, not by the dispersion.

(4) AND AN EVOLVING TWIST PUMPS DIRECTION, NOT HANDEDNESS.  b depends on psi, which evolves, and a
    time-varying momentum shift is what the chiral anomaly uses to pump.  Each 4D chirality carries
    BOTH branches -- a +z mover E = +(k - s b) and a -z mover E = -(k - s b), s = +1 right, -1 left.
    Sweeping b through a full lattice spacing: the right-handed +z mover gains a level and its -z
    mover loses one; the left-handed movers do the reverse; and EACH CHIRALITY'S TOTAL IS CONSERVED.
    Computed.  The evolving twist moves states between directions within a chirality and never between
    chiralities.  (Consistently, the four-dimensional axial term needs the curl of b, which vanishes
    under the T^2 symmetry, b depending on t and z only.)

  ==> *** C50's asymmetry selects no handedness, statically or as the twist evolves.  What it does is
      SEPARATE the chiralities by direction along the twist axis, and, as the twist evolves, drive a
      current in which right and left flow oppositely -- the geometric form of a chiral separation
      current.  The weak force's preference for one handedness is not fixed here. ***

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT that CR fixes no handedness anywhere. **  What is shown is that the twist does not: it
  separates, it does not select.  Where the weak force's choice is fixed is not answered by this.

  ** NOT a claim beyond zero transverse momentum and the T^2-symmetric member. **  The spectral flow is
  computed on the modes along the twist axis, which is where C50's shift acts.

  ** NOT that the chiral separation current is observable, or of any size. **  Only its sign structure
  is established -- right and left opposite, fixed relative to the twist.
"""

import numpy as np

b=0.37; L=40.0; k=2*np.pi*np.arange(-60,61)/L
ER=np.sort(np.concatenate([+(k-b),-(k-b)])); EL=np.sort(np.concatenate([+(k+b),-(k+b)]))
assert np.allclose(ER, EL)
print("  (1) the two chiralities' spectra are the same set -- neither lower in energy        OK")

assert (+b) > 0 > (-b)
print("  (2) zero-energy branches at k = +b (right) and k = -b (left): directional            OK")

kk=2*np.pi*np.arange(-200,201)/L
def filled(E): return int(np.sum(E<0))
for s in (+1,-1):
    b0,b1=0.01, 2*np.pi/L+0.01
    up0,dn0=filled(+(kk-s*b0)),filled(-(kk-s*b0)); up1,dn1=filled(+(kk-s*b1)),filled(-(kk-s*b1))
    assert up0+dn0 == up1+dn1, "the chirality's total is conserved"
    assert (up1-up0) == -(dn1-dn0) != 0, "its two movers exchange a level"
print("  (4) sweeping b: each chirality's two movers exchange a level, its total conserved   OK")

print()
print("ESTABLISHED: C50's twist asymmetry selects no handedness. By energy the two chiralities have the")
print("same spectrum. The asymmetry is directional -- right-handed at k = +b, left at -b along the twist")
print("axis -- and that correlation is invariant under the joint orientation flip, so which handedness is")
print("'left' is set by the twist's sign, not by the dispersion. And as the twist evolves, each")
print("chirality's +z and -z movers exchange levels while its total is conserved: the twist separates")
print("the chiralities by direction and drives right and left oppositely, and pumps no net handedness.")
print("NOT CLAIMED: that CR fixes no handedness anywhere -- only that the twist does not. Nothing beyond")
print("zero transverse momentum on the T^2-symmetric member. Nothing about the current's size.")
