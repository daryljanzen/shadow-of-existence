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
#: ⛭ r7161+cc66.127: ** `H`'S LEADING 2/3 WAS A TYPED LITERAL AND IS NOW DERIVED. **  `H` is
#: `d(ln r)/dtau` for the scale factor this file already verifies, so typing `2/3` beside it asserted
#: by hand a number the file computes two checks earlier.  ⌈ The `2/3` that remains is the EXPONENT of
#: the scale factor, and that one is not a free literal: check (2) proves `r = A sinh^{2/3}(B tau)`
#: solves the `E=1` radial geodesic and its CONTROL proves `1/2` does not, so the power is forced by
#: the geodesic rather than assumed here.  *This is the round's own rule applied to my own file: a
#: coefficient the receipt can derive should not be carried beside the thing it derives from.*
#: ⌗ It also removes the quantity the CI diagnostic found disagreeing -- `Hc`, `H`'s own coefficient,
#: came back `3/4` in CI while `sp.Rational(2,3)` in the same process came back `2/3` and a rebuild
#: from it came back correct.  **That reading is reported to 66 as a fact about the runner and not
#: repaired here, because a receipt cannot repair a runner; what IS repaired here is the literal.**
_r_c = A * sp.sinh(Bc * tau) ** sp.Rational(2, 3)   # the verified law, in the paper's c-carrying argument
H = sp.simplify(sp.diff(_r_c, tau) / _r_c)          # H = d(ln r)/dtau, DERIVED -- no typed prefactor
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
#: ⛭ r7161+cc66.118: ** A CHECK THAT FAILS ONLY WHERE I CANNOT RUN IT MUST SAY WHAT IT GOT. **
#: This receipt is red in CI's `scoped — the plain suite` and green here on the same tree -- measured
#: standalone, in a clean worktree at each failing head, twelve times over, under CI's own child
#: environment, and inside the same parallel batch on the same scope; same pins (sympy 1.14.0,
#: mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1), same sympy ground types, same camb/pynucastro/matplotlib.
#: ⛔ ** AND THE SUITE'S REPORT NAMED NEITHER A CHECK NOR A VALUE. **  `run_all_receipts` keeps a
#: failing receipt's LAST THREE non-blank lines, which here were the RESULT banner and its rules --
#: so three CI runs said `FAILED` and nothing else, and the diagnosis cost four heads and three wrong
#: readings before the job log was read at all.  *A receipt whose only failing output is its verdict
#: can be debugged only where it can be run, which is exactly not where it fails.*
#: So the evidence is carried here, in two parts, because the two readers are different:
#:   • the long block below, for a human running this file directly; and
#:   • ** THREE COMPACT LINES PRINTED LAST, AFTER the closing banner **, because the last three are
#:     the only ones the suite keeps -- a diagnostic printed before the banner is invisible in CI,
#:     which is the mistake this block was one edit away from repeating.
#: Both print only on failure.
if not allpass:
    import platform, hashlib
    try:
        _gt = sp.external.gmpy.GROUND_TYPES
    except Exception as _e:                                            # noqa: BLE001
        _gt = 'unreadable(%s)' % type(_e).__name__
    #: the fifth field is `want_zero`: False for the CONTROL, whose whole point is a NON-zero residual
    _DIAG = [
        ('eq:amplitude',   _AMP,       amp_nariai,        sp.simplify(amp_nariai - _AMP), True),
        ('eq:scalefac',    None,       None,
         sp.simplify(sp.expand_trig(lhs - rhs)), True),
        ('CONTROL',        None,       None,
         sp.simplify(sp.expand_trig(sp.diff(r_bad, tau)**2
                                    - (2*G*M/r_bad + (Lam/3)*r_bad**2))), False),
        ('eq:rate[1]',     _RATE_COTH, H**2,              sp.simplify(H**2 - _RATE_COTH), True),
        ('coth2=1+csch2',  None,       None,
         sp.simplify(sp.coth(x)**2 - (1 + sp.csch(x)**2)), True),
        ('eq:omega-ratio', _OMR,       mat_term/Lam_term,
         sp.simplify(mat_term/Lam_term - _OMR), True),
        ('late-time',      None,       None,
         sp.simplify(sp.limit(H**2, tau, sp.oo) - Lam*c**2/3), True),
    ]
    _BAD = [(n, r) for n, _p, _m, r, _wz in _DIAG if (r != 0) == _wz]
    _ENV = ('python %s sympy %s ground %s tex %dch/%s'
            % (platform.python_version(), sp.__version__, _gt, len(_P15F),
               hashlib.sha256(_P15F.encode('utf-8')).hexdigest()[:12]))
    print("-"*72)
    print("  DIAGNOSTIC -- what THIS run got, because the verdict alone does not carry it:")
    print("    " + _ENV)
    print("    paper " + _P15F_PATH)
    for _n, _p, _m, _r, _wz in _DIAG:
        print("    %-16s residual=%r   (want %s)" % (_n, _r, '0' if _wz else 'non-zero'))
        if _p is not None:
            print("      PARSED from the paper : %s" % (_p,))
            print("      this file's own form  : %s" % (_m,))
    print("    eq:rate sides parsed: %d -> %s" % (len(_RATE_SIDES), _RATE_SIDES))
    print("-"*72)
print("="*72)
if allpass:
    print("RESULT: ALL PASS -- amplitude, the sinh^{2/3} scale factor (E=1 geodesic, 2/3 forced by")
    print("        the control), the Friedmann coth^2 rate, and the csch^2 density-ratio, all")
    print("        verified symbolically.")
else:
    print("RESULT: FAILED -- one or more symbolic identities above did not hold.")
print("="*72)
if not allpass:
    #: ⛔ ** THESE THREE LINES ARE LAST BECAUSE THE SUITE KEEPS ONLY THE LAST THREE, **
    #: joined and cut at 300 characters.  ⌘ r7161+cc66.119: the first version printed the residual
    #: EXPRESSIONS and the cut ate them -- CI reported `eq:rate[1]=17*Lambda*c**2*coth(sqrt(3)*sqrt(Lam`
    #: and stopped there.  *A diagnostic sized for a budget it has not measured is the same mistake as a
    #: pin.*  So what goes in the budget now is the decisive SCALARS: every coefficient below is an exact
    #: rational, each a handful of characters, and between them they separate "the parse moved" from
    #: "this file's own `H` is not what it reads as" without any expression surviving the cut.
    #: ⌘ r7161+cc66.120: ** THE FIRST SET OF COEFFICIENTS WAS ARITHMETICALLY IMPOSSIBLE, AND THAT IS
    #: THE FINDING. **  CI returned `R23=2/3 Bc2=3/4 H2=27/64`.  But `H2` is *defined* as
    #: `H**2/(Lam c^2 coth^2)` and `H` is *defined* as `R23*Bc*coth`, so `H2` is forced to be
    #: `R23^2 * Bc2` = `(2/3)^2 * (3/4)` = `1/3`.  **27/64 is `(3/4)^2 * (3/4)`** -- exactly what this
    #: file produces when `sp.Rational(2,3)` in `H` is replaced by `sp.Rational(3,4)`, which is how I
    #: forced a failure to test this block.  *And `R23`, evaluated in the SAME process, prints `2/3`.*
    #: ⛔ So either the source CI executes is not the blob CI reports -- every git object I can read,
    #: including `refs/pull/261/merge`, says `Rational(2,3)` -- or `H**2` is not `(R23*Bc*coth)**2`
    #: there.  **`R23` was useless for telling those apart: it is a constant written HERE, not `H`'s
    #: own coefficient.**  A diagnostic that reports a quantity nothing depends on is decoration.
    #: So two discriminators, and they are the whole point of this revision:
    #:   • `Hc` reads the coefficient OUT OF `H` itself -- if it is `3/4` while `R23` is `2/3`, the
    #:     executed source is not the blob, which is a fact about CI and not about this receipt; and
    #:   • `H2r` REBUILDS `H` here from `R23` and `Bc` and asks the same question of the rebuild -- if
    #:     `H2r` is `1/3` while `H2` is `27/64`, then the two `H`s differ and `Hc` says how.
    _C = lambda e: sp.simplify(e)
    _Hr = sp.Rational(2, 3)*Bc*sp.coth(Bc*tau)          # H, rebuilt here from the same two factors
    _COEF = [
        ('R23',  sp.Rational(2, 3)),                                     # want 2/3
        ('Bc2',  _C(Bc**2 / (Lam*c**2))),                                # want 3/4
        ('Hc',   _C(H / (Bc*sp.coth(Bc*tau)))),                          # want 2/3 -- H's OWN coef
        ('H2',   _C(H**2 / (Lam*c**2*sp.coth(Bc*tau)**2))),              # want 1/3
        ('H2r',  _C(_Hr**2 / (Lam*c**2*sp.coth(Bc*tau)**2))),            # want 1/3 -- the rebuild
        ('lim',  _C(sp.limit(H**2, tau, sp.oo) / (Lam*c**2))),           # want 1/3
        ('rate', _C(_RATE_COTH / (Lam*c**2*sp.coth(Bc*tau)**2))),        # want 1/3
    ]
    print("\u26d4 FAILING: %s" % ('; '.join(n for n, _r in _BAD)
                             or 'none isolated -- a check failed that this block does not cover'))
    print("\u26d4 COEFS: %s" % ' '.join('%s=%s' % (n, v) for n, v in _COEF))
    print("\u26d4 ENV: %s" % _ENV)
raise SystemExit(0 if allpass else 1)
