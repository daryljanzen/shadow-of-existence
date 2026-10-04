"""
P15_expansion_law.py -- verifies the P15 sec:properframe/sec:flatlcdm derivation core SYMBOLICALLY (sympy):
  eq:amplitude, eq:scalefac (the sinh^{2/3} law solving the E=1 radial geodesic), eq:rate (Friedmann coth^2
  form), eq:omega-ratio (csch^2), with a wrong-exponent CONTROL that forces the 2/3 power.
STATUS: ✔✔ (all symbolic; wrong-exponent control forces 2/3)   RUN: python3 P15_expansion_law.py   RUNTIME: ~3s
ORIGIN: built new r1397 (the derivation was prose+cite JanzenModernParallax/Janzen2015, unreceipted here).
"""
import sympy as sp
def ok(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
G,M,Lam,c,tau,r=sp.symbols('G M Lambda c tau r',positive=True)
#: ⛭ r7157+cc66.115: the paper's own display equation was CARRIED HERE AS A LITERAL and attributed to
#: its label.  It is PARSED from the paper now, so a move in the paper lands here as a failure.
#: *`paper_formula` asserts the label occurs exactly once (`r7153`'s control), refuses a fragment
#: its dialect cannot carry rather than guessing, and the parse is checked against the expression
#: this file carried before the repair.*
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus'))
import paper_formula as pf
#: ⛔ AND THE RECEIPT OPENS THE PAPER ITSELF rather than handing a PATH to the helper.
#: `check_unread_figure` decides READS-PAPER from THIS file's own source, so a read delegated
#: to `paper_formula` is invisible to it -- the repair would have left the site reading the
#: paper and still counting as NO-READ.  *Found because `P15_expansion_law` stayed NO-READ
#: after its figures were parsed.*  `paper_formula` takes the TEXT, so the open stays here
#: where the instrument can see it and the parse stays there.
_P15F_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus',
                   'CR_cosmology.tex')
_P15F = open(_P15F_PATH, encoding='utf-8').read()
allpass=True
print("="*72); print("P15 derivation core -- amplitude, sinh^{2/3} scale factor, Friedmann forms"); print("="*72)

# (1) eq:amplitude: at Nariai M = c^2/(3 sqrt(Lambda) G), (6GM/Lambda c^2)^{1/3} = 2^{1/3}/sqrt(Lambda)
M_nariai=c**2/(3*sp.sqrt(Lam)*G)
amp=(6*G*M/(Lam*c**2))**sp.Rational(1,3)
amp_nariai=sp.simplify(amp.subs(M,M_nariai))
_AMP = pf.rhs(_P15F, 'eq:amplitude', {'G': G, 'M': M, 'Lambda': Lam, 'c': c})
allpass&=ok(f"eq:amplitude: (6GM/Lambda c^2)^{{1/3}} at Nariai = {_AMP}  -- PARSED from the paper",
            sp.simplify(amp_nariai-_AMP)==0)

# (2) eq:scalefac solves the E=1 radial geodesic. In geometric units (c=1) the E=1 equation is
#     (dr/dtau)^2 = 1 - V_eff = 2GM/r + (Lambda/3) r^2   [V_eff=(r-2GM-(Lambda/3)r^3)/r].
#     Claimed solution r = A sinh^{2/3}(B tau), A=(6GM/Lambda)^{1/3}, B=(1/2)sqrt(3 Lambda).
A=(6*G*M/Lam)**sp.Rational(1,3); B=sp.sqrt(3*Lam)/2
r_sol=A*sp.sinh(B*tau)**sp.Rational(2,3)
lhs=sp.diff(r_sol,tau)**2
rhs=2*G*M/r_sol+(Lam/3)*r_sol**2
allpass&=ok("eq:scalefac: r=A sinh^{2/3}(B tau) solves (dr/dtau)^2 = 2GM/r + (Lambda/3)r^2  (E=1 geodesic)",
            sp.simplify(sp.expand_trig(lhs-rhs))==0)

# (2-control) a WRONG exponent p!=2/3 must NOT solve it
p=sp.Rational(1,2)
r_bad=A*sp.sinh(B*tau)**p
allpass&=ok("CONTROL: r=A sinh^{1/2}(B tau) does NOT solve the E=1 equation (the 2/3 power is forced)",
            sp.simplify(sp.expand_trig(sp.diff(r_bad,tau)**2-(2*G*M/r_bad+(Lam/3)*r_bad**2)))!=0)

# (3) eq:rate: H = rdot/r = (2B/3) coth(B tau); with the paper's B=(1/2)sqrt(3 Lambda) c, H^2=(Lambda c^2/3)coth^2
Bc=sp.sqrt(3*Lam)*c/2                       # paper's argument coefficient (with c)
H=sp.Rational(2,3)*Bc*sp.coth(Bc*tau)       # H = (2B/3) coth(B tau) for r ~ sinh^{2/3}(B tau)
#: ⛭ r7157+cc66.116: the Friedmann form was TYPED here as `(Lam*c**2/3)*coth(Bc*tau)**2`.  It is
#: PARSED from `eq:rate` now, including the coth's own argument, so the paper's prefactor AND its
#: argument coefficient both land here if either moves.  ⌗ `\coth^{2}(x)` means `(\coth x)^{2}` for a
#: named function, which is a convention and not a guess -- `paper_formula` translates it on that
#: ground and leaves `f^{-1}` alone.
#: ⌗ `eq:rate` is a CHAIN -- H^2 = (Lambda c^2/3) coth^2(..) = (1/3)(8 pi G rho + Lambda c^2) -- so
#: every side is parsed and the middle one is the form this check compares.  `H` is supplied as this
#: file's own expression for it, which is what lets the strict naming check pass the left side.
_RATE_SIDES = pf.sides(_P15F, 'eq:rate',
                       {'H': H, 'Lambda': Lam, 'c': c, 'tau_tilde': tau, 'G': G,
                        'rho': sp.Symbol('rho')})
_RATE_COTH = _RATE_SIDES[1]
allpass&=ok(f"eq:rate PARSED: H^2 = {_RATE_COTH}",
            sp.simplify(H**2-_RATE_COTH)==0)

# (4) eq:omega-ratio: coth^2 = 1 + csch^2 => H^2 = Lambda c^2/3 + (Lambda c^2/3) csch^2;
#     the Lambda c^2/3 is the Lambda term, (Lambda c^2/3)csch^2 the matter term => Omega_m/Omega_L = csch^2
x=sp.symbols('x')
allpass&=ok("coth^2 = 1 + csch^2 (splits H^2 into Lambda term + matter term)",
            sp.simplify(sp.coth(x)**2-(1+sp.csch(x)**2))==0)
Lam_term=Lam*c**2/3; mat_term=(Lam*c**2/3)*sp.csch(Bc*tau)**2
_OMR = pf.rhs(_P15F, 'eq:omega-ratio',
              {'Lambda': Lam, 'c': c, 'tau_tilde': tau,
               'Omega_m': sp.Symbol('Omega_m'), 'Omega_Lambda': sp.Symbol('Omega_Lambda')})
allpass&=ok(f"eq:omega-ratio PARSED: Omega_m/Omega_Lambda = matter_term/Lambda_term = {_OMR}",
            sp.simplify(mat_term/Lam_term-_OMR)==0)
# and H^2 = (1/3)(8 pi G rho + Lambda c^2) form: the Lambda term is exactly (1/3)Lambda c^2
allpass&=ok("H^2 late-time -> (1/3)Lambda c^2 (the standard rate (1/2)sqrt(3 Lambda) c as tau->inf)",
            sp.simplify(sp.limit(H**2,tau,sp.oo)-Lam*c**2/3)==0)
print("="*72)
print("RESULT:", "ALL PASS -- amplitude, the sinh^{2/3} scale factor (E=1 geodesic, 2/3 forced by the control),\n         the Friedmann coth^2 rate, and the csch^2 density-ratio all verified symbolically." if allpass else "SOME FAILED")
print("="*72)
# ** THIS FILE COULD NOT FAIL ITS CALLER UNTIL r2376+c54.179, AND ITS VERDICT WAS UNCONDITIONAL. **
# `allpass` was accumulated through every check and then never read: the RESULT line printed
# "ALL PASS" as a literal, and the process exited 0 whether the symbolic identities held or not.
# ** Breaking the late-time-rate claim printed two FAILs and still returned rc=0. **
# It was masked because `scripts/lint_assertions.py` counted the presence of `allpass &=` as a check
# in itself; the two-part rule adopted in the same revision -- a failure-collection idiom AND a
# non-zero exit path -- is what surfaced it.  *An instrument that accepts the bookkeeping for the
# acting will pass a receipt that does neither.*
if allpass:
    print("RESULT: ALL PASS -- amplitude, the sinh^{2/3} scale factor (E=1 geodesic, 2/3 forced by")
    print("        the control), the Friedmann coth^2 rate, and the csch^2 density-ratio, all")
    print("        verified symbolically.")
else:
    print("RESULT: FAILED -- one or more symbolic identities above did not hold.")
print("="*72)
raise SystemExit(0 if allpass else 1)
