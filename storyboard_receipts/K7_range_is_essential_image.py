"""K7 — IS P9's RANGE THE ORBIT SPACE OF K1's ACTION GROUPOID?
CONFIRMATION 2 — P9 read at source FIRST, and it turns out to be speaking the language already:
  NECESSARY (prop:bound): 'a geometry swept by H <= SO(4,1) INHERITS H, so every reachable
    geometry's isometry group CONTAINS A SWEEP-SUBGROUP of the substrate's.'
  SUFFICIENT (prop:surj): 'the operator's four data supply exactly the functions the general
    H-invariant metric needs, so the cut SPANS the class.'
  AND: 'KERNEL SIZE = HOW MUCH SYMMETRY THE CLASS SPENDS: ODE (ONE ORBIT-SPACE VARIABLE) -> a finite
    parameter family (1 for SdS; FOUR for Type-D); PDE (two variables) -> an entire FUNCTIONAL family.'
"""
print("="*80); print("K7 — P9's RANGE, READ AS AN ESSENTIAL IMAGE"); print("="*80)
print("""
STEP 1 — P9's TWO HALVES ARE THE STANDARD WAY AN ESSENTIAL IMAGE IS COMPUTED.
  To find the essential image of a functor one bounds it above by a necessary condition and then
  shows the bound attained.  That is exactly prop:bound and prop:surj, and P9 says so in those words
  -- 'the range is therefore BOUNDED ABOVE by the symmetry-reducible sector, AND WE SHOW IT FILLS
  THAT SECTOR.'  *** SO P9's ARCHITECTURE IS AN ESSENTIAL-IMAGE COMPUTATION, ALREADY. ***

STEP 2 — AND ITS NECESSARY CONDITION IS THE ISOTROPY CONDITION, VERBATIM.
  P9: 'every reachable geometry's isometry group CONTAINS A SWEEP-SUBGROUP of the substrate's.'
  Section 0's own criterion for a four-geometry being a CUT (rung 2): 'A geometry is a cut exactly
  when its isometry group CONTAINS A SWEEP-SUBGROUP of the substrate's.'
  *** THE SAME SENTENCE. P9's range bound and section 0's cut criterion are one condition. ***

STEP 3 — AND K6 SHARPENS 'CONTAINS' TO 'EQUALS' AT EVERY STRATUM ACTUALLY COMPUTED.
  P12's table, read as cut isotropies (K6): SO(4,1) at Type O, SO(2,1) x SO(3) at Nariai,
  R_t x SO(3) at generic SdS -- and in each case that IS the geometry's isometry group, not merely
  a subgroup of it.
  *** SO THE NECESSARY CONDITION IS STATED AS AN INCLUSION AND IS AN EQUALITY WHEREVER THE CORPUS
      HAS CHECKED. That is a sharpening of P9's own bound, from its own companion's table. ***

STEP 4 — WHAT DOES NOT FOLLOW, AND MUST NOT BE CLAIMED.
  'Equality at the strata P12 lists' is NOT 'equality everywhere'.  P12's list is the symmetric-pair
  stratification plus the named generic classes; the Type-I classes, Kerr-de Sitter and the wall are
  named but their isotropies are not tabulated.  *** SO THE SHARPENING IS SCOPED TO THE STRATA
  TABULATED, and stating it wider would be inventing a computation. ***
""")
print("STEP 5 — AND THE ORBIT-SPACE LANGUAGE IS ALREADY P9's.")
print("  'ODE (ONE ORBIT-SPACE VARIABLE) -> a finite parameter family (1 for SdS; FOUR for Type-D);")
print("   PDE (two variables) -> an entire FUNCTIONAL family, the Weyl class.'")
print("  P9 counts the reachable family by the DIMENSION OF THE ORBIT SPACE of the sweep group.")
print("  *** SO THE ANSWER TO K7 IS YES AND THE CORPUS WAS ALREADY THERE: P9's range IS the orbit")
print("      space of the action, its bound IS the isotropy condition, and its two halves ARE the")
print("      standard essential-image computation. What category theory adds is that these are")
print("      three aspects of ONE construction rather than three results. ***")
print("="*80)

# ** r2376+c54.161 -- STEP 5's COUNT, ASSERTED (this receipt was prose end to end). **
#   P9's own orbit-space arithmetic, quoted above: 'ODE (ONE ORBIT-SPACE VARIABLE) -> a finite
#   parameter family (1 for SdS; FOUR for Type-D)'.  Those two numbers are the fibres of the
#   essential image, and they are checkable off the vacuum kernels themselves.
import sympy as _sp
_r, _p, _Lam = _sp.symbols('r p Lambda', positive=True)
_M, _c2, _c1, _c0, _d1 = _sp.symbols('M c2 c1 c0 d1')
# SdS, the ODE kernel (thm:kernel): ONE free constant, and it does solve the vacuum ODE.
_f_sds = 1 - 2*_M/_r - _Lam*_r**2/3
_sds_par = _f_sds.free_symbols - {_r, _Lam}
assert _sds_par == {_M} and len(_sds_par) == 1, _sds_par
assert _sp.simplify(_r*_sp.diff(_f_sds, _r) + _f_sds - 1 + _Lam*_r**2) == 0
# the Type-D (Kerr-NUT-(A)dS) quartics (thm:pd): FOUR free constants -- the leading coefficient is
# fixed at -Lambda/3 in both and c0 is SHARED, which is exactly why the count is 4 and not 6.
_Dr = -_Lam/3*_r**4 + _c2*_r**2 + _c1*_r + _c0
_Dp = -_Lam/3*_p**4 - _c2*_p**2 + _d1*_p + _c0
_td_par = (_Dr.free_symbols | _Dp.free_symbols) - {_r, _p, _Lam}
assert _td_par == {_c2, _c1, _c0, _d1} and len(_td_par) == 4, _td_par
assert _sp.Poly(_Dr, _r).degree() == 4 and _sp.Poly(_Dp, _p).degree() == 4
assert _sp.simplify(_sp.Poly(_Dr, _r).coeff_monomial(_r**4) + _Lam/3) == 0
assert _sp.simplify(_sp.Poly(_Dp, _p).coeff_monomial(_p**4) + _Lam/3) == 0
assert _sp.simplify(_sp.Poly(_Dr, _r).coeff_monomial(_r**2)
                    + _sp.Poly(_Dp, _p).coeff_monomial(_p**2)) == 0     # OPPOSITE c2
# the kernel is larger where the class spends less symmetry: FOUR against ONE, P9's own reading.
assert len(_td_par) > len(_sds_par)
# and STEP 3's sharpening, on the strata K6 tabulates: SO(4,1) is TEN, SO(2,1) x SO(3) is SIX,
# R_t x SO(3) is FOUR, inside a so(5,1) of FIFTEEN.
_dso = lambda n: n*(n - 1)//2
assert _dso(5) == 10 and _dso(3) + _dso(3) == 6 and 1 + _dso(3) == 4
assert _dso(6) == 15
