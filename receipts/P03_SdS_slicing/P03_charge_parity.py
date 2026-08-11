"""
P03_charge_parity.py -- verifies P3 sec:charge (the one charged computation; all other P3 receipts are
  vacuum), by DECOMPOSING the Reissner-Nordstrom-de Sitter slicing function under the mass-reflection R:
    [P3 SdS-slicing-curve_v2 sec:charge eq:RNdS/eq:RNsplit; the vacuum split is sec:two-readings L444]
    (i)   f = 1 - 2M/r + Q^2/r^2 - r^2/alpha^2 splits under R (2M -> -2M) as
            f = [1 - r^2/alpha^2 + Q^2/r^2]  (R-EVEN, invariant)  +  [-2M/r]  (R-ODD, sign-flipped),
          so MASS is R-odd (perspectival) and CHARGE is R-even (joins the invariant de Sitter geometry);
    (ii)  vacuum Q=0: de Sitter 1-r^2/alpha^2 is R-even, Schwarzschild -2M/r is R-odd (sec:two-readings);
    (iii) charge conjugation Q -> -Q leaves f IDENTICAL (f depends on Q only through Q^2), so every turning
          point (root of the horizon quartic) is fixed -- the geometric face of charge being field-level;
    (iv)  the charged horizon relation -r^4/alpha^2 + r^2 - 2M r + Q^2 = 0 carries Q only as +Q^2;
    (v)   with Q != 0, Q^2/r^2 dominates as r->0 so f -> +infinity (an inner Cauchy horizon, r=0 a timelike
          RN singularity) -- NOT the vacuum branch point where f -> -infinity.
  [P3 SdS-slicing-curve_v2 -- the charged extension: mass R-odd, charge R-even, C its field-level closure]
STATUS: ✔✔   RUN: python3 P03_charge_parity.py   RUNTIME: ~3s
COMPUTES: the R even/odd projection of f; the Q->-Q invariance; the quartic; the r->0 limits (vacuum vs charged).
CONTROL: vacuum (Q=0) f -> -infinity as r->0 (the branch point onto the conjugate branch); charged (Q!=0)
  f -> +infinity (Cauchy horizon). The R-odd part is the mass term ALONE -- drop the mass and f is R-even.
BOUND: all other P3 receipts are vacuum SdS; this is the sole charged computation (sec:charge), establishing
  the discrete-symmetry parity of charge (R-even) vs mass (R-odd). C's full antilinear closure is field-level
  (JanzenBoundary), off the slicing geometry; this receipt does the geometric ledger (the even Q->-Q degeneracy).
ORIGIN: built new (fork) -- P3 completeness re-audit finding A; charge uncovered by every vacuum receipt.
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, M, Q, alpha = sp.symbols('r M Q alpha', positive=True)
f = 1 - 2*M/r + Q**2/r**2 - r**2/alpha**2
print("="*74); print("P03 charge parity -- RNdS f split under the mass-reflection R (2M -> -2M)"); print("="*74)

# (i) R even/odd decomposition under 2M -> -2M
R = lambda expr: expr.subs(M, -M)
f_even = sp.simplify((f + R(f))/2)
f_odd  = sp.simplify((f - R(f))/2)
ok&=check("R-even part = 1 - r^2/alpha^2 + Q^2/r^2  (de Sitter + charge)",
          sp.simplify(f_even - (1 - r**2/alpha**2 + Q**2/r**2))==0)
ok&=check("R-odd part = -2M/r  (the mass term ALONE -> mass is R-odd, charge is R-even)",
          sp.simplify(f_odd - (-2*M/r))==0)

# (ii) vacuum Q=0: de Sitter even, Schwarzschild odd (sec:two-readings)
fv = f.subs(Q,0)
ok&=check("vacuum Q=0: R-even = 1 - r^2/alpha^2 (de Sitter), R-odd = -2M/r (Schwarzschild)",
          sp.simplify((fv+R(fv))/2 - (1-r**2/alpha**2))==0 and sp.simplify((fv-R(fv))/2 - (-2*M/r))==0)

# (iii) charge conjugation Q -> -Q leaves f identical (Q^2 only)
ok&=check("Q -> -Q leaves f IDENTICAL (f depends on Q only through Q^2)", sp.simplify(f.subs(Q,-Q) - f)==0)
# every root of the horizon quartic is therefore fixed under Q->-Q
quartic = sp.simplify((f*r**2*(-alpha**2)).expand())     # clear denominators: -alpha^2 r^2 f
ok&=check("charged horizon quartic  r^4/alpha^2 ... carries Q only as +Q^2 (so Q->-Q fixes every root)",
          sp.simplify(quartic.subs(Q,-Q) - quartic)==0)
# show the quartic is -r^4/alpha^2 + r^2 - 2M r + Q^2 (up to the overall clearing)
horizon_poly = sp.expand(-alpha**2 * (r**2 * f))         # = -r^4/alpha^2*alpha^2 ... build canonical
ok&=check("horizon relation  -r^4/alpha^2 + r^2 - 2M r + Q^2 = 0  (from f=0)",
          sp.simplify(sp.expand(r**2*f) - (r**2 - 2*M*r + Q**2 - r**4/alpha**2))==0)

# (v) r -> 0 limits: charged f -> +oo (Cauchy horizon), vacuum f -> -oo (branch point)
ok&=check("charged (Q!=0): f -> +infinity as r->0 (Q^2/r^2 dominates: Cauchy horizon, timelike RN singularity)",
          sp.limit(f, r, 0, '+') == sp.oo)
ok&=check("CONTROL vacuum (Q=0): f -> -infinity as r->0 (the -2M/r branch point onto the conjugate branch)",
          sp.limit(fv, r, 0, '+') == -sp.oo)
# CONTROL: the R-odd part is the mass alone -- with M=0 (and Q free) f is fully R-even
ok&=check("CONTROL: M=0 => f is R-even (no odd part); the odd part is sourced by the mass only",
          sp.simplify((f.subs(M,0) - R(f.subs(M,0))))==0)

# r2376+c54.159 -- (a) the receipt's own PASS/FAIL flag, which was only printed; and (b) a pin of
# this receipt's own claim, INDEPENDENT of that flag: the CHARGED horizon quartic at alpha=1,
# 2M=0.3, Q^2=0.01 has THREE positive roots -- an inner Cauchy horizon at r=0.03818709 strictly
# inside the event horizon 0.28985091, plus the cosmological 0.80053368 -- while the vacuum cubic
# at the same 2M has only TWO, its third root sitting AT r=0 (the branch point).  That is the
# geometric content of "charge is R-even": Q enters only as +Q^2 and it opens a horizon at the
# origin where the vacuum has a branch point.  Q -> -Q leaves every one of those roots fixed.
assert ok, "P03_charge_parity: a check() line FAILED -- see the PASS/FAIL column above"
def _roots_of(Qv):                 # turning points of THIS receipt's f, at alpha=1, 2M=0.3
    p = sp.Poly(sp.expand(quartic.subs({alpha: 1, M: sp.Rational(3, 20), Q: Qv})), r)
    return sorted(float(sp.re(z)) for z in sp.nroots(p) if abs(sp.im(z)) < 1e-9 and sp.re(z) > 1e-9)
_chg = _roots_of(sp.Rational(1, 10))            # Q^2 = 0.01
_vac = _roots_of(sp.Integer(0))                 # the vacuum control
assert len(_chg) == 3 and len(_vac) == 2, (_chg, _vac)
assert abs(_chg[0] - 0.03818709) < 1e-7, _chg          # the inner Cauchy horizon Q opens
assert abs(_chg[1] - 0.28985091) < 1e-7, _chg          # event
assert abs(_chg[2] - 0.80053368) < 1e-7, _chg          # cosmological
assert abs(_vac[0] - 0.33893624) < 1e-7, _vac          # vacuum: no inner horizon at all
assert max(abs(a - b) for a, b in zip(_chg, _roots_of(sp.Rational(-1, 10)))) < 1e-12, _chg

print("="*74)
print("RESULT:", "ALL PASS -- RNdS f splits under R into an even part (de Sitter + charge Q^2/r^2) and an odd\n"
      "         part (-2M/r): mass is R-odd, charge R-even. Q->-Q fixes f and every turning point (field-level C).\n"
      "         Charged r=0 is a +oo Cauchy horizon, not the vacuum -oo branch point."
      if ok else "SOME FAILED")
print("="*74)
