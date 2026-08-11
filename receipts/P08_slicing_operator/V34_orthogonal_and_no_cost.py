"""V3 — IS THE LEFTWARD READING INCOMPATIBLE WITH AN ACTION PRINCIPLE, OR ORTHOGONAL TO ONE?
V4 — WHAT DOES TAKING THE DIRAC ALGEBRA WITHOUT A LEGENDRE TRANSFORM COST?
CONFIRMATION 2 first, and it moves both answers.
ORIGIN: storyboard_receipts/V34_orthogonal_and_no_cost.py -- registered r2376 (c54); edit the origin, not this copy."""
print("="*80); print("V3 — ORTHOGONAL, NOT INCOMPATIBLE"); print("="*80)
print("""
  WHAT THE CORPUS SAYS THE LEFTWARD READING IS, at source:
    P8: 'READ THE FRIEDMANN EQUATION LEFTWARD (derived here, not asserted): coth^2 = 1 + csch^2
         splits H^2 into Lambda (pure de Sitter, the unbent expansion) and a pressureless dust --
         THE BEND.  The cut is the primary object and RHO IS THE NAME OF ITS BEND, NOT ITS CAUSE.'
    P15: '...and EMPIRICALLY FORCED rather than modelled: the microwave-redshift isotropy floor
         forces uniform expansion to some three orders of magnitude.'
    P4:  'the alternative the isotropy rejects, a rate tracking the lumpy, radiation-carrying matter
         content, is exactly the mis-reading that would source that rate from the content, AND THE
         SKY FORBIDS IT by three orders of magnitude.'

  SO THE DIRECTION IS MEASURED, NOT POSITED.  Now the variational question, sharply:

  *** AN ACTION PRINCIPLE PRODUCES AN EQUALITY.  Varying the Einstein--Hilbert action gives
      G_ab + Lambda g_ab = 8 pi T_ab -- AND AN EQUALITY HAS NO DIRECTION. ***
  Which side is the existent and which the name of its bend is not a question the variation asks or
  answers; it is settled here by P4's isotropy floor, which is data.
  *** SO V3's ANSWER IS ORTHOGONAL, NOT INCOMPATIBLE: an action would return the same field
      equations and would leave the reading exactly where it is.  Nothing in the leftward reading
      forbids an action, which is why Daryl's 'all absences so far are circumstantial' is right
      here specifically and not only in general. ***
""")
print("="*80); print("V4 — THE DIRAC ALGEBRA WITHOUT A LEGENDRE TRANSFORM COSTS NOTHING, AND P12 SAYS SO")
print("="*80)
print("""
  The Dirac (hypersurface-deformation) algebra is normally OBTAINED by Legendre transform from the
  Einstein--Hilbert action.  The corpus never performs one -- 'Legendre' appears zero times.

  BUT P12's OWN FRAMING SETTLES WHAT THAT COSTS:
    'the claim is A RECOGNITION, NOT AN ADDITION: the algebroid was already there, IN GR's OWN
     CONSTRAINT ALGEBRA, waiting for the base.'
    'The constraint algebra is GR's own (Dirac/ADM), UNCHANGED.  The thesis is NOT "CR adds an
     algebroid" but "GR's hypersurface-deformation algebra WAS ALWAYS a Lie algebroid -- structure
     functions, not constants -- lacking a base and a section; the substrate supplies both."'

  *** SO P12 INHERITS THE ALGEBRA EXPLICITLY AND CLAIMS NOTHING ABOUT ITS DERIVATION.  A recognition
      about the structure of an object one takes as given owes no derivation of that object. ***
  The Legendre transform would be owed only if P12 claimed to DERIVE the algebra, or claimed a
  property that depends on how it was obtained.  It claims neither: base and section are supplied,
  the brackets are GR's.
  *** V4's ANSWER: NO COST, and the honest scope is already written into the paper. ***
""")
print("="*80)

# ** r2376+c54.161 -- THE TWO QUOTED GROUNDS, ASSERTED (this receipt was prose end to end). **
import sympy as _sp
_tau, _u = _sp.symbols('tau u', positive=True)

# V3's premise -- the leftward reading an action would return unchanged.  On the E=1 SdS cosmology
# with alpha=1 (so Lambda/3 = 1) and 2M = 1, a(tau) = sinh^{2/3}(3 tau/2), and the corpus's split
#     H^2 = coth^2(3 tau/2) = 1 + csch^2(3 tau/2)
# separates Lambda/3 (pure de Sitter, the UNBENT expansion) from the bend.
_a = _sp.sinh(3*_tau/2)**_sp.Rational(2, 3)
_H2 = _sp.simplify(_sp.diff(_a, _tau)**2/_a**2)
assert _sp.simplify(_H2 - _sp.coth(3*_tau/2)**2) == 0
assert _sp.simplify((_sp.coth(_u)**2 - 1 - _sp.csch(_u)**2).rewrite(_sp.exp)) == 0
# AND THE BEND IS A PRESSURELESS DUST, which is what gives 'rho is the name of the bend' content:
# 8 pi rho/3 = H^2 - Lambda/3 = csch^2(3 tau/2) = 1/a^3, so rho a^3 is CONSTANT at
# 3/(8 pi) = 0.1193662073189... -- no pressure, and no direction in the equality.
_rho = _sp.simplify(3*(_H2 - 1)/(8*_sp.pi))
_rho_a3 = _sp.simplify(_rho*_a**3)
assert _sp.simplify(_sp.diff(_rho_a3, _tau)) == 0, _rho_a3
assert _sp.simplify(_rho_a3 - 3/(8*_sp.pi)) == 0, _rho_a3
_num = float(_rho_a3.subs(_tau, _sp.Rational(7, 10)))
assert abs(_num - 0.1193662073189215) < 1e-13, _num

# V4's ground -- P12's 'structure FUNCTIONS, not constants', the one property that makes the
# inherited Dirac algebra an ALGEBROID and so needs a base rather than a Legendre transform.  The
# bracket {H(N),H(M)} = D_a( q^{ab}(N d_b M - M d_b N) ) closes on q^{ab}, which on a flat slice
# q_ab = a^2 delta_ab is a^{-2}: it is 1 at a = 1 and 0.25 at a = 2, so the 'constants' are not
# constant and the closure is on phase-space functions.
_av = _sp.Symbol('a', positive=True)
_sc = 1/_av**2
_sc1 = float(_sc.subs(_av, 1))
_sc2 = float(_sc.subs(_av, 2))
assert abs(_sc1 - 1.0) < 1e-12 and abs(_sc2 - 0.25) < 1e-12, (_sc1, _sc2)
assert abs(_sc1 - _sc2) > 0.5      # NOT a structure constant: it moved with the phase-space point
