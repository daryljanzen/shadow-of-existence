"""
P15_verify_throat_tower.py -- verifies the P15 sec:throat mode tower + no-hair isotropization. On the Nariai
  near-horizon dS_2 x S^2 (both radii 1/sqrt(Lambda)), a scalar splits in S^2 harmonics: degree-l -> dS_2
  field of mass m^2=l(l+1)/r_star^2, so m^2/H_dS2^2=l(l+1). dS_2 index nu^2=1/4-m^2/H^2: l=0 gives nu^2=+0.25
  (nu=1/2, scale-invariant base, survives); every l>=1 has l(l+1)>=2 so nu^2<0 (heavy principal series,
  oscillates & DECAYS). => the throat isotropizes: only the isotropic monopole survives. Grounded in the de
  Sitter no-hair theorem (Wald 1983) on the dS_2 factor, not a bare reading. GUARD (load-bearing, held): the
  throat l is the S^2 degree at areal radius 1/sqrt(Lambda), NOT the observable CMB multipole (which lives at
  D_C) -- the map is sec:largescale, not an identity.
STATUS: ✔✔ (tower algebra + the l=0-survives / l>=1-decays split; no-hair grounded; CMB-multipole guard held)
RUN: python3 P15_verify_throat_tower.py   RUNTIME: <1s
ORIGIN: computations/perturbation_verify/verify_throat_tower.py, verified r1397.
"""
import numpy as np
print("dS_2 x S^2 throat tower (radii equal = 1/sqrt(Lambda)):")
print(" l    m^2/H^2=l(l+1)   nu^2=1/4-l(l+1)   series           fate through throat")
for l in range(0,6):
    m2=l*(l+1); nu2=0.25-m2
    if nu2>=0: series,fate="complementary","survives (no-hair base)"
    else:      series,fate="principal (heavy)","oscillates & DECAYS"
    tag="  <- isotropic monopole" if l==0 else ""
    print(f" {l}        {m2:>3d}            {nu2:+.2f}          {series:18s} {fate}{tag}")
print("\nSPLIT: l=0 alone has nu^2>=0 (the scale-invariant base, nu=1/2); EVERY l>=1 has nu^2<0")
print("(heavy principal series). Anisotropy is the heavy tower -> damped through the dS_2 throat.")
print("GROUNDING: this is the de Sitter no-hair theorem (Wald 1983) on the throat's dS_2 factor,")
print("not a bare reading. GUARD held: throat l (S^2 degree at 1/sqrt(Lambda)) =/= CMB multipole (at D_C).")

# =====================================================================
# ** CHECKS, added r2376+c54.154.  This file was PRINT-ONLY: it enumerated l = 0..5 and selected
#    the words "survives"/"DECAYS" by the sign of nu^2, so its OK certified that Python exited
#    zero.  The audit at c54.153 found the sentence it supports asserts EVERY l >= 1, which six
#    integers cannot establish.  It is proved here for all l, symbolically. **
import sympy as _sp
_l = _sp.symbols('l', integer=True, positive=True)
_nu2 = _sp.Rational(1, 4) - _l * (_l + 1)
_fail = []
# for every integer l >= 1, l(l+1) >= 2 > 1/4, so nu^2 <= 1/4 - 2 < 0.  Proved, not sampled.
if not _sp.ask(_sp.Q.negative(_nu2.subs(_l, 1))) and _nu2.subs(_l, 1) >= 0:
    _fail.append("nu^2 at l=1")
_worst = _sp.simplify(_nu2.subs(_l, 1))                      # the LEAST negative member
assert _worst == _sp.Rational(-7, 4), f"l=1 gives nu^2 = {_worst}, expected -7/4"
# monotone: d/dl [1/4 - l(l+1)] = -(2l+1) < 0 for l >= 1, so l=1 is the maximum over the tower
_dnu2 = _sp.simplify(_sp.diff(_nu2, _l))
assert _sp.simplify(_dnu2.subs(_l, 1)) == -3 and _sp.simplify(_dnu2 + (2 * _l + 1)) == 0, \
    "nu^2 must be strictly decreasing in l"
# and the monopole is the complementary-series base with nu = 1/2 exactly
assert _sp.simplify(_nu2.subs(_l, 0) - _sp.Rational(1, 4)) == 0, "l=0 must give nu^2 = 1/4"
print()
print("  ** PROVED FOR EVERY l, NOT SAMPLED: nu^2(l) = 1/4 - l(l+1) is strictly decreasing "
      "(d nu^2/dl = -(2l+1)),")
print("     so its maximum over the tower l >= 1 is at l = 1, where nu^2 = -7/4 < 0.  EVERY l >= 1 "
      "is heavy")
print("     principal series; l = 0 alone has nu^2 = 1/4, nu = 1/2, the scale-invariant base. **")
if _fail:
    print("FAILED: " + "; ".join(_fail))
    raise SystemExit(1)
print("  CHECKS PASS")
