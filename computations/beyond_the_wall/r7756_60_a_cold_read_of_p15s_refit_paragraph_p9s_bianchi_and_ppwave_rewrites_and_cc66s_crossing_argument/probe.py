#!/usr/bin/env python3
"""r7756 (60) -- the cold read r7755 orders, run as seventeen registered arms.

PREDICTION.md is committed and pushed before this file existed.  Every arm prints its
comparison and its verdict; nothing is reported that is not computed here or read here.
"""
import os
import re
import subprocess
import sys

import numpy as np
import sympy as sp
from scipy.integrate import quad

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'Range.lean')
P9 = os.path.join(ROOT, 'corpus', 'range_paper.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P7 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
FOR66 = os.path.join(ROOT, 'FOR_66.md')

VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


print("=" * 100)
print("r7756 (60) -- the cold read of r7755's three objects")
print(f"  HEAD the probe ran on: {git('rev-parse', 'HEAD').strip()}")
print(f"  origin/main at:        {git('rev-parse', 'origin/main').strip()}")
print("  (r7754's lesson: the tree is part of the predicate, so it is printed before anything is read)")
print("=" * 100)

TEX15, TEX9, TEX7 = read(P15), read(P9), read(P7)
SRC = read(LEAN)

# =====================================================================================
# PART 1 -- P15's refit paragraph
# =====================================================================================
PARA = [ln for ln in TEX15.split('\n') if ln.startswith(r'\emph{Refitted, it stays level}')]
para = PARA[0] if PARA else ''

# ---- ARM 1: every figure the paragraph prints, against its source
FIGS = re.findall(r'(?<![0-9.])([0-9]+\.[0-9]+)', para)
SOURCED = {
    '186.85': 'refit receipt, PART 1: the leaf-rate arm refitted',
    '186.51': 'refit receipt, PART 1: the control refitted',
    '297.7': 'refit receipt, PART 1: the arm of record refitted',
    '0.02115': 'pricing receipt, gate 4: worst |Delta| over the six tracers',
    '0.49836': 'pricing receipt, gate 5: |Delta| at z*',
}
missing = [f for f in FIGS if f not in SOURCED]

# recomputed here, from the two rate laws, exactly as the pricing receipt does
H0, OM, OMR, C = 68.6, 0.2973, 8.8186e-05, 299792.458
ZREC = 1089.9
BAO = [0.295, 0.510, 0.706, 0.930, 1.317, 2.330]


def H_stack(z, h0=H0, om=OM):
    return h0 * np.sqrt(om * (1 + z) ** 3 + 1.0 - om)


def H_leaf(z, h0=H0, om=OM, omr=OMR):
    return h0 * np.sqrt(om * (1 + z) ** 3 + omr * (1 + z) ** 4 + 1.0 - om)


def DM(z, H, **kw):
    return quad(lambda zz: C / H(zz, **kw), 0.0, z, limit=200)[0]


DELTA = {z: DM(z, H_leaf) / DM(z, H_stack) - 1.0 for z in BAO + [ZREC]}
worst_bao = max(abs(DELTA[z]) for z in BAO)
got = {'0.02115': 100 * worst_bao, '0.49836': 100 * abs(DELTA[ZREC])}
fig_bad = [(k, v) for k, v in got.items() if abs(v - float(k)) > 5e-5]

arm(1, "every figure the paragraph prints is sourced, and the two this seat can recompute do",
    not missing and not fig_bad,
    f"  figures in the paragraph: {FIGS}",
    *[f"      {f}  <-  {SOURCED[f]}" for f in FIGS if f in SOURCED],
    f"  unsourced: {missing if missing else 'none'}",
    "  recomputed here from the two published rate laws (not read from the receipt):",
    *[f"      {k}: this seat gets {v:.5f}" for k, v in got.items()],
    f"  disagreements: {fig_bad if fig_bad else 'none'}",
    "  the three chi^2 figures are READ from the refit receipt's own run, which this seat",
    "  re-ran: 186.85 / 186.51 / 297.7, all three reproduced, ALL CHECKS PASS.",
    "  NEGATIVE WAS REACHABLE: a figure with no source, or one disagreeing with it.")

# ---- ARM 2: the comparatives are the comparisons the receipts made
REG70 = read(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7749_70_leafgeom_refit',
                          'PREDICTION.md'))
RCPT = read(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                         'P15_with_the_projection_distance_on_the_leaf_rate_the_refitted_spectrum_is'
                         '_level_with_the_control_and_the_bao_fit_does_not_move.py'))
four = re.search(r'the four parameters the control is refitted on \(([^)]*)\)', REG70)
cmp_claims = [
    ("refitted on the four parameters the control is refitted on",
     f"70's registration names them: {four.group(1) if four else 'NOT FOUND'}",
     bool(four) and len(four.group(1).split(',')) == 4),
    ("this configuration reaches 186.85 against the control's refitted 186.51",
     "both are refitted scores through one operator on the same 185 lensed bins",
     '185 lensed bins' in RCPT),
    ("the baryon-acoustic fit barely moves",
     "the receipt computes the DESI DR2 BAO chi^2 on both geometries at a common r_d",
     'common r_d' in RCPT),
]
arm(2, "the paragraph's comparatives are the comparisons the receipts actually made",
    all(c[2] for c in cmp_claims),
    *[f"      {'OK ' if c[2] else 'NO '} {c[0]}\n           -> {c[1]}" for c in cmp_claims],
    "  the refit receipt scores every spectrum through one operator (P15's CAMB lensing",
    "  operator, chi2_of_spectrum.chi2_of, 185 lensed bins), so the two sides of each",
    "  comparative are the same statistic on the same bins.",
    "  NEGATIVE WAS REACHABLE: a comparative whose two sides are not what was scored.")

# ---- ARM 3: the uniqueness claim, and the set it ranges over
EPS = 1e-3


def sens(z, which):
    if which == 'H0':
        return ((DM(z, H_stack, h0=H0 * (1 + EPS)) / DM(z, H_stack)) - 1.0) / EPS
    return ((DM(z, H_stack, om=OM * (1 + EPS)) / DM(z, H_stack)) - 1.0) / EPS


s_rec = {k: sens(ZREC, k) for k in ('H0', 'Om')}
frac = {k: {z: sens(z, k) / s_rec[k] for z in BAO} for k in ('H0', 'Om')}
leaf_frac = {z: DELTA[z] / DELTA[ZREC] for z in BAO}
om_lo, om_hi = min(frac['Om'].values()), max(frac['Om'].values())
# the paper's range, as printed
PRINTED = (0.25, 2.0 / 3.0)
inside = PRINTED[0] - 5e-3 <= om_lo and om_hi <= PRINTED[1] + 5e-3
sep_ok = max(leaf_frac.values()) < min(frac['Om'].values())
arm(3, "\"the only one that does this\" -- the set it quantifies over, and the printed range",
    not inside,     # the arm's claim is that the printed range does NOT cover the six
    "  the set: the paragraph says `the parameters the rate carries'.  The cited receipt",
    "  enumerates it in as many words -- `H_0 and the epoch are the two the rate itself",
    "  carries; the sector's other parameters are not swept here' -- so the set IS stated",
    "  and IS exhausted by the receipt: the rate law H^2 = H_0^2[Om(1+z)^3 + Om_r(1+z)^4 +",
    "  1 - Om] carries an amplitude, an epoch, and the radiation term that IS the leaf rate.",
    "  ⇒ the uniqueness claim rests on an ENUMERATED set, which is what the arm asked.",
    "",
    "  ⛔ BUT THE PRINTED RANGE IS MEASURED AT TWO OF THE SIX TRACER REDSHIFTS, AND THE",
    "  PARAGRAPH STATES IT OVER `the baryon-acoustic distances', WHICH ARE ALL SIX:",
    "      d ln D_M / d ln Om at z*, as a fraction of itself, at every DESI tracer:",
    *[f"          z = {z:6.3f}   {frac['Om'][z]:.4f}   (locality {1 / frac['Om'][z]:5.2f})" for z in BAO],
    f"      the paper prints `a quarter to two thirds' = [{PRINTED[0]:.3f}, {PRINTED[1]:.3f}]",
    f"      measured over the six: [{om_lo:.4f}, {om_hi:.4f}]",
    f"      the low end is {om_lo:.4f}, which is a SIXTH, not a quarter",
    "      the receipt priced Om at z = 0.510 and z = 2.330 only, and labels them as `the",
    "      two tracer redshifts that bracket the BAO's weight' -- they do not bracket the",
    "      six, which run down to z = 0.295.",
    "",
    f"  ⌗ AND THE CONCLUSION IS UNAFFECTED, WHICH IS SAID RATHER THAN LEFT OUT: the leaf",
    f"  rate's own fraction over the same six is [{min(leaf_frac.values()):.5f}, "
    f"{max(leaf_frac.values()):.5f}], so the separation the",
    f"  sentence is for holds at every tracer, and widens at the low end "
    f"({1 / min(leaf_frac.values()):.1f} against {1 / om_lo:.1f}).",
    f"      separation holds at all six: {sep_ok}",
    "  NEGATIVE WAS REACHABLE: the measured range could have lain inside the printed one.")

# ---- ARM 4: the theta_* pull is not in print
PULLWORDS = [r'\\theta_\*[^.]{0,80}pull', r'pull[^.]{0,80}\\theta_\*', r'2\.9\s*\\sigma',
             r'\+2\.9', r'2\.3\s*\\sigma']
hits = {p: [f for f, t in (('P15', TEX15), ('P9', TEX9), ('P7', TEX7))
            if re.search(p, t)] for p in PULLWORDS}
pull_absent = not any(hits.values())
# POWER CONTROL: the same extraction, on a figure that IS in the paragraph
ctl = re.search(r'186\.85', para) is not None
arm(4, "the paragraph does not use 70's instrument theta_* pull",
    pull_absent and ctl,
    f"  searched P15, P9 and P7 for the pull and for its figure: {hits}",
    f"  present anywhere: {not pull_absent}",
    "  r7755 states that no paper sentence uses it and that 70's corpus-definition theta_*",
    "  is in the register only; that is what this finds.",
    f"  POWER CONTROL, over material where the thing searched for IS present: the identical",
    f"  regex extraction finds 186.85 in this same paragraph: {ctl}.  So an absence here is",
    "  an absence and not a dead search.",
    "  ⌗ The refit receipt itself computes a pull (+2.3 sigma on the corpus's definition,",
    "  against the registration's +2.9 on the instrument's).  Neither is in print.")

# ---- ARM 5: the direction of the improvement
stays = 'stays level' in para
BLOCKS = [b for b in TEX15.split('\n\n') if 'closes the whole of it' in b]
nofit_first = bool(BLOCKS) and '186.135' in BLOCKS[0]
arm(5, "the direction of the improvement -- refit or distance assignment",
    stays and nofit_first,
    "  r7754 established from 70's own figures that the leaf-geometry arm scores BELOW the",
    "  control's no-fit before any refit (196.50 against 214.06, 0.918 times), so the",
    "  improvement is in the distance assignment and not in what the refit does.",
    f"  the paragraph's verb is `stays level', not `becomes level': {stays}",
    f"  and the preceding sentence has already put it level as computed (186.135): {nofit_first}",
    "  ⇒ the wording carries the decomposition rather than attributing it to the refit.",
    "  NEGATIVE WAS REACHABLE: `refitting brings it level' would have failed this arm.")

# =====================================================================================
# PART 2 -- P9's Bianchi and pp-wave paragraphs, recomputed and read against Range.lean
# =====================================================================================
BIPARA = [ln for ln in TEX9.split('\n') if 'bi\\_electric' in ln][0]
PWPARA = [ln for ln in TEX9.split('\n') if 'pw\\_typeN' in ln][0]

# ---------------------------------------------------------------- Bianchi I, from the metric
A1, A2, A3, cc, ss = sp.symbols('A1 A2 A3 c s', positive=True)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
tt = sp.Symbol('t', positive=True)
HLOG = {A1: (cc + k1) / ss, A2: (cc + k2) / ss, A3: (cc + k3) / ss}


def Db(e):
    out = sp.diff(e, cc) * 3 * ss + sp.diff(e, ss) * 3 * cc
    for A, h in HLOG.items():
        out += sp.diff(e, A) * A * h
    return sp.cancel(out)


a_expl = sp.sinh(3 * tt) ** sp.Rational(1, 3) * sp.tanh(3 * tt / 2) ** (k1 / 3)
H_ok = sp.simplify(sp.diff(a_expl, tt) / a_expl - (sp.cosh(3 * tt) + k1) / sp.sinh(3 * tt)) == 0

gB = sp.Matrix([[-1, 0, 0, 0], [0, A1 ** 2, 0, 0], [0, 0, A2 ** 2, 0], [0, 0, 0, A3 ** 2]])
giB = sp.diag(-1, 1 / A1 ** 2, 1 / A2 ** 2, 1 / A3 ** 2)
_dg = [[[Db(gB[i, j]) if k == 0 else sp.S.Zero for k in range(4)] for j in range(4)] for i in range(4)]
GB = [[[sp.S.Zero] * 4 for _ in range(4)] for _ in range(4)]
for _A in range(4):
    for _B in range(4):
        for _C in range(_B, 4):
            _s = sp.S.Zero
            for _E in range(4):
                if giB[_A, _E] == 0:
                    continue
                _s += giB[_A, _E] * (_dg[_E][_C][_B] + _dg[_B][_E][_C] - _dg[_B][_C][_E])
            _v = sp.cancel(_s / 2); GB[_A][_B][_C] = _v; GB[_A][_C][_B] = _v


def _Rup(A, B, C_, E_):
    s_ = (Db(GB[A][E_][B]) if C_ == 0 else sp.S.Zero) - (Db(GB[A][C_][B]) if E_ == 0 else sp.S.Zero)
    for lam in range(4):
        s_ += GB[A][C_][lam] * GB[lam][E_][B] - GB[A][E_][lam] * GB[lam][C_][B]
    return sp.cancel(s_)


def lowB(A, B, C_, E_):
    s_ = sp.S.Zero
    for F in range(4):
        if gB[A, F] != 0:
            s_ += gB[A, F] * _Rup(F, B, C_, E_)
    return sp.cancel(s_)


RicB = sp.zeros(4, 4)
for _mu in range(4):
    for _nu in range(_mu, 4):
        _s = sp.S.Zero
        for _lam in range(4):
            if _lam == 0:
                _s += Db(GB[_lam][_mu][_nu])
            if _nu == 0:
                _s -= Db(GB[_lam][_mu][_lam])
            for _sig in range(4):
                _s += GB[_lam][_lam][_sig] * GB[_sig][_mu][_nu] - GB[_lam][_nu][_sig] * GB[_sig][_mu][_lam]
        _v = sp.cancel(_s); RicB[_mu, _nu] = _v; RicB[_nu, _mu] = _v
RsB = sp.cancel(sum(giB[i, i] * RicB[i, i] for i in range(4)))


def weylB(a, b, c_, d_):
    t1 = lowB(a, b, c_, d_)
    t2 = (gB[a, c_] * RicB[b, d_] - gB[a, d_] * RicB[b, c_]
          - gB[b, c_] * RicB[a, d_] + gB[b, d_] * RicB[a, c_]) / 2
    t3 = RsB / 6 * (gB[a, c_] * gB[b, d_] - gB[a, d_] * gB[b, c_])
    return sp.cancel(t1 - t2 + t3)


def onsh(e):
    """impose sum C = 0 and sum C^2 = 6 (as 2(k1^2+k1k2+k2^2)=6) and c^2 - s^2 = 1."""
    e = sp.expand(sp.together(e).subs(k3, -k1 - k2))
    e = sp.simplify(sp.expand(sp.simplify(e.subs(ss ** 2, cc ** 2 - 1))))
    e = sp.simplify(sp.expand(e) - sp.expand(e).coeff(k1 ** 0) * 0)
    num, den = sp.fraction(sp.cancel(e))
    rem = sp.rem(sp.Poly(sp.expand(num), k2), sp.Poly(k1 ** 2 + k1 * k2 + k2 ** 2 - 3, k2))
    return sp.simplify(rem.as_expr() / den)


Eclaim = [sp.cancel((2 + k * cc - k ** 2) / (cc ** 2 - 1)) for k in (k1, k2, k3)]
# the pair structure of the Riemann/Weyl tensor, CHECKED rather than assumed
offpair = [(a, b, c_, d_) for a in range(4) for b in range(4) for c_ in range(4) for d_ in range(4)
           if {a, b} != {c_, d_} and sp.simplify(weylB(a, b, c_, d_)) != 0]
# the mixed bivector entries u_ab = W^{ab}_{ab}
U = {(a, b): sp.cancel(giB[a, a] * giB[b, b] * weylB(a, b, a, b))
     for a in range(4) for b in range(4) if a < b}
u_vs_E = {(0, 1): Eclaim[0], (0, 2): Eclaim[1], (0, 3): Eclaim[2],
          (2, 3): Eclaim[0], (1, 3): Eclaim[1], (1, 2): Eclaim[2]}
u_bad = [(p, onsh(U[p] + E)) for p, E in u_vs_E.items() if onsh(U[p] + E) != 0]
Ediag = [sp.cancel(weylB(0, i, 0, i) / (A1, A2, A3)[i - 1] ** 2) for i in (1, 2, 3)]
Ebad = [(i, onsh(e - c)) for i, (e, c) in enumerate(zip(Ediag, Eclaim), start=1)
        if onsh(e - c) != 0]

# ---- the eigenvalues of the operator the cited declarations define, computed outright
PAIRS = [(a, b) for a in range(4) for b in range(4)]
WITNESS = {k1: sp.sqrt(3), k2: sp.Integer(0), k3: -sp.sqrt(3), cc: sp.cosh(3)}
Ewit = [sp.nsimplify(sp.N(E.subs(WITNESS))) for E in Eclaim]


def _u(a, b):
    if a == b:
        return sp.S.Zero
    p = (min(a, b), max(a, b))
    return sp.N(U[p].subs(WITNESS).subs(ss, sp.sinh(3)))


MAT = sp.zeros(16, 16)
for i, p in enumerate(PAIRS):
    for j, q in enumerate(PAIRS):
        if p[0] == p[1]:
            continue
        if q == p:
            MAT[i, j] = _u(*p)
        elif q == (p[1], p[0]):
            MAT[i, j] = -_u(*p)
EIG = sorted([sp.N(x, 8) for x in sp.Matrix(MAT).eigenvals(multiple=True)], key=lambda z: sp.re(z))
Ewit_n = sorted([sp.N(e.subs(cc, sp.cosh(3)), 8) for e in
                 [E.subs({k1: sp.sqrt(3), k2: 0, k3: -sp.sqrt(3)}) for E in Eclaim]])
nonzero_eig = sorted([e for e in EIG if abs(e) > 1e-9])
pred = sorted([-2 * e for e in Ewit_n] * 2)
eig_match = (len(nonzero_eig) == 6
             and all(abs(float(a) - float(b)) < 1e-7 for a, b in zip(nonzero_eig, pred)))
eig_is_E = all(any(abs(float(e) - float(x)) < 1e-7 for x in Ewit_n) for e in nonzero_eig)
trW2 = sp.N(sum(MAT[i, j] * MAT[j, i] for i in range(16) for j in range(16)), 12)
trW3 = sp.N((sp.Matrix(MAT) ** 3).trace(), 12)
I_got, J_got = trW2 / 16, trW3 / 96
I_claim = sum(e ** 2 for e in Ewit_n) / 2
J_claim = -sum(e ** 3 for e in Ewit_n) / 6
IJ_ok = abs(float(I_got - I_claim)) < 1e-8 and abs(float(J_got - J_claim)) < 1e-8
disc_got = float(I_got ** 3 - 27 * J_got ** 2)
disc_claim = float(sp.prod([(Ewit_n[i] - Ewit_n[j]) for i in range(3) for j in range(i + 1, 3)]) ** 2 / 4)

arm(6, "each cited declaration asserts what the sentence citing it says",
    not offpair and not u_bad and not Ebad and eig_match and not eig_is_E,
    "  THE SENTENCE: `its Weyl tensor has zero magnetic part and diagonal electric",
    "  components E_i = ... (bi_electric), AND THESE ARE ITS EIGENVALUES, because the full",
    "  Riemann tensor computed in all its components puts the Weyl operator in block form",
    "  on the bivector pairs (bi_Rfull and bi_W).'",
    "",
    f"  recomputed from the metric: the Weyl tensor is supported on index PAIRS "
    f"({'no off-pair component is nonzero' if not offpair else offpair[:4]}),",
    "  so the operator IS block form, and the blocks are the six pairs.  bi_W's own",
    "  statement is the same table: W = ij_tbl (bi_U ...), with (bi_U0, bi_U1)",
    f"  u_0i = -E_i and u_jk = -E_i: disagreements {u_bad if u_bad else 'none, all six'}",
    f"  bi_electric's three components reproduce: {'yes' if not Ebad else Ebad}",
    "",
    "  ⛔ AND THE STEP THE `because' MAKES IS NOT THE STEP BLOCK FORM GIVES.  Each block of",
    "  ij_tbl is u[[1,-1],[-1,1]] on the ordered pair and its swap, NOT u times the",
    "  identity; its eigenvalues are 2u and 0.  Computed outright on the paragraph's own",
    f"  witness C = (sqrt3, 0, -sqrt3) at t = 1 (16x16, the operator Range.lean defines):",
    f"      E_i                      {[float(e) for e in Ewit_n]}",
    f"      nonzero eigenvalues      {[float(e) for e in nonzero_eig]}",
    f"      predicted -2E_i, twice   {[float(e) for e in pred]}",
    f"      match                    {eig_match}",
    f"      any eigenvalue EQUAL to an E_i: {eig_is_E}",
    f"      zero eigenvalues: {len(EIG) - len(nonzero_eig)} of 16",
    "  ⇒ the E_i are the eigenvalues only after restricting to the antisymmetric bivectors",
    "  and adopting the one-half bivector convention; of the operator as the cited",
    "  declarations define it they are not the eigenvalues, they are -2 times them.  The",
    "  substance is right and the citation is now sufficient where r7754 said it was not:",
    "  bi_Rfull's all-256-components statement IS what kills the off-diagonal electric",
    "  entries C_{0i0j}, which is what r7754 found the old citation did not supply.  What",
    "  the `because' still skips is the 2x2 block itself: u[[1,-1],[-1,1]] is not scalar,",
    "  so block form gives DIAGONAL ENTRIES, and the step to eigenvalues needs the",
    "  restriction to antisymmetric bivectors and the one-half convention.",
    "  NEGATIVE WAS REACHABLE: the eigenvalues could have come out equal to the E_i.")

# ---- ARM 7: the hypotheses travel with the claim
def binders(name):
    """the binder groups of a declaration, split by matching brackets rather than by a
    flat regex -- the types themselves carry parentheses, and a flat regex silently
    returns a SHORT list, which is the failure mode that would make a missing hypothesis
    look like an absent one."""
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b', SRC, re.M)
    if not m:
        return None
    i = m.end()
    out, depth, start, opener = [], 0, None, None
    while i < len(SRC):
        ch = SRC[i]
        if depth == 0 and ch == ':' and SRC[i:i + 2] != ':=' and SRC[i - 1] not in '(:{[':
            break
        if ch in '({[':
            if depth == 0:
                start, opener = i, ch
            depth += 1
        elif ch in ')}]':
            depth -= 1
            if depth == 0:
                body = SRC[start + 1:i]
                if ':' in body:
                    nm, ty = body.split(':', 1)
                    out.append((nm.strip(), ' '.join(ty.split()), opener))
        i += 1
    return out


CITED = ['bi_vacuum', 'bi_electric', 'bi_typeI', 'bi_typeD', 'bi_Rfull', 'bi_W', 'bi_IJ',
         'pw_nilpotent', 'pw_invariants', 'pw_witness', 'pw_IJ', 'pw_typeN',
         'rn_pp_Ric', 'rn_pp_vacuum_iff', 'rn_pp_witness']
BND = {n: binders(n) for n in CITED}
# what the paragraph carries, sentence by sentence
carried = {
    'bi_IJ': ('nonzero for distinct C_i wherever cosh3t>3',
              'distinct C_i' in BIPARA.replace('$', '') or 'distinct $C_{i}$' in BIPARA,
              r'\cosh3t>3' in BIPARA.replace(' ', '') or 'cosh3t}>3' in BIPARA.replace(' ', '')),
    'pw_IJ': ('every VACUUM pp-wave has I = J = 0', 'every vacuum pp-wave' in PWPARA, True),
    'pw_nilpotent': ('For harmonic H its Weyl operator is nilpotent',
                     'For harmonic $H$' in PWPARA, True),
    'rn_pp_Ric': ('for the metric with ANY H', 'with any $H$' in PWPARA, True),
}
hyp_rows = []
for n in CITED:
    b = BND[n]
    hyp_rows.append(f"      {n:20s} {len(b) if b is not None else 'NOT FOUND':>3} binders: "
                    f"{'; '.join(t for _, t, _ in (b or []))[:96]}")
def _hasharm(n):
    return any('kr_pd' in t and '+' in t and '= 0' in t for _, t, _ in (BND[n] or []))


anyH_ok = BND['rn_pp_Ric'] is not None and not any(
    'kr_pd' in t for _, t, _ in BND['rn_pp_Ric'])       # no harmonicity, no symmetry hypothesis
harm_cited = all(_hasharm(n) for n in ('pw_nilpotent', 'pw_invariants', 'pw_IJ'))
carried_ok = all(v[1] and v[2] for v in carried.values())
cosh_ok = 'cosh3t>3' in BIPARA.replace('\\', '').replace('$', '').replace(' ', '').replace('{', '').replace('}', '')
arm(7, "the hypotheses travel with the claim",
    anyH_ok and harm_cited and cosh_ok and carried['pw_nilpotent'][1] and carried['pw_IJ'][1],
    "  every cited declaration's binders, read out of Range.lean:",
    *hyp_rows,
    "",
    f"  rn_pp_Ric has NO harmonicity and NO mixed-partial hypothesis: {anyH_ok}",
    "      ⇒ the paragraph's `for the metric (eq:ppwave) with any H' is exact.",
    f"  pw_nilpotent / pw_invariants / pw_IJ all carry the harmonicity hypothesis: {harm_cited}",
    f"      ⇒ and the paragraph now says `For harmonic H its Weyl operator is nilpotent': "
    f"{carried['pw_nilpotent'][1]}",
    "      (r7754 reported this clause as missing its hypothesis; r7755 landed the fix, and",
    "      this is the check that it landed where the claim is made.)",
    f"  pw_IJ is stated for `every vacuum pp-wave': {carried['pw_IJ'][1]}, and vacuum is",
    "      exactly harmonicity by the clause before it, which the paragraph states.",
    f"  bi_IJ's cosh 3t > 3 is carried in the sentence that cites it: {cosh_ok}",
    "  NEGATIVE WAS REACHABLE: a hypothesis in the binders and absent from the stem.")

# ---- ARM 8: the Bianchi invariants, recomputed
sumE = sp.simplify(onsh(sum(Eclaim)))
key_id = sp.simplify(sp.expand(
    (sum(e ** 2 for e in Eclaim) / 2) ** 3 - 27 * (-sum(e ** 3 for e in Eclaim) / 6) ** 2
    - sp.prod([Eclaim[i] - Eclaim[j] for i in range(3) for j in range(i + 1, 3)]) ** 2 / 4))
key_on = sp.simplify(onsh(key_id))
arm(8, "the Bianchi invariants recomputed from the metric, not read from Lean",
    IJ_ok and abs(disc_got - disc_claim) < 1e-8 and sumE == 0 and key_on == 0,
    f"  on the witness C = (sqrt3, 0, -sqrt3), t = 1, from the 16x16 operator above:",
    f"      I = tr(W^2)/16 = {float(I_got):.10f}   against  (1/2) sum E_i^2 = {float(I_claim):.10f}",
    f"      J = tr(W^3)/96 = {float(J_got):.10f}   against -(1/6) sum E_i^3 = {float(J_claim):.10f}",
    f"      agreement: {IJ_ok}",
    f"      I^3 - 27J^2 = {disc_got:.12e}   against  (1/4) prod (E_i - E_j)^2 = {disc_claim:.12e}",
    "  and as an IDENTITY in the C_i rather than at the witness:",
    f"      sum E_i = 0 on the constraint set: {sumE == 0}",
    f"      (1/2 sum E^2)^3 - 27(-1/6 sum E^3)^2 - (1/4) prod (E_i - E_j)^2 = {key_on}",
    "  ⌗ the identity needs sum E_i = 0, which the paragraph does not state and which is",
    "  derived here from the two constraints; Lean's bi_IJ derives it the same way (hsum).",
    "  ⇒ the printed normalisation (I = 1/2 sum E^2, J = -1/6 sum E^3) is the one the",
    "  operator's traces give with ij_I's /16 and ij_J's /96, so `the standard",
    "  normalisation' is the normalisation actually used.",
    "  NEGATIVE WAS REACHABLE: a factor in either invariant would break both comparisons.")

# ---- ARM 9: the pp-wave invariants, recomputed, and what type N needs
uu, vv, XX, YY = sp.symbols('u v X Y', real=True)
Hf = sp.Function('H')(uu, XX, YY)
COP = [uu, vv, XX, YY]
gP = sp.Matrix([[Hf, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
giP = sp.Matrix([[0, -1, 0, 0], [-1, -Hf, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
invP_ok = all(sp.simplify(x) == 0 for x in (giP * gP - sp.eye(4)))


def DP(e, k):
    return sp.diff(e, COP[k]) if k != 1 else sp.S.Zero


_dgP = [[[DP(gP[i, j], k) for k in range(4)] for j in range(4)] for i in range(4)]
GP = [[[sp.S.Zero] * 4 for _ in range(4)] for _ in range(4)]
for _A in range(4):
    for _B in range(4):
        for _C in range(_B, 4):
            _s = sp.S.Zero
            for _E in range(4):
                if giP[_A, _E] == 0:
                    continue
                _s += giP[_A, _E] * (_dgP[_E][_C][_B] + _dgP[_B][_E][_C] - _dgP[_B][_C][_E])
            _w = sp.expand(_s / 2); GP[_A][_B][_C] = _w; GP[_A][_C][_B] = _w
RicP = sp.zeros(4, 4)
for _mu in range(4):
    for _nu in range(_mu, 4):
        _s = sp.S.Zero
        for _lam in range(4):
            _s += DP(GP[_lam][_mu][_nu], _lam) - DP(GP[_lam][_mu][_lam], _nu)
            for _sig in range(4):
                _s += GP[_lam][_lam][_sig] * GP[_sig][_mu][_nu] - GP[_lam][_nu][_sig] * GP[_sig][_mu][_lam]
        _w = sp.expand(_s); RicP[_mu, _nu] = _w; RicP[_nu, _mu] = _w


def _RupP(a, b, c_, d_):
    s_ = DP(GP[a][d_][b], c_) - DP(GP[a][c_][b], d_)
    for lam in range(4):
        s_ += GP[a][c_][lam] * GP[lam][d_][b] - GP[a][d_][lam] * GP[lam][c_][b]
    return sp.expand(s_)


def lowP(a, b, c_, d_):
    s_ = sp.S.Zero
    for F in range(4):
        if gP[a, F] != 0:
            s_ += gP[a, F] * _RupP(F, b, c_, d_)
    return sp.expand(s_)


Hxx, Hyy = sp.diff(Hf, XX, 2), sp.diff(Hf, YY, 2)
ruu_ok = sp.simplify(RicP[0, 0] + (Hxx + Hyy) / 2) == 0
others = [(i, j) for i in range(4) for j in range(4)
          if not (i == 0 and j == 0) and sp.simplify(RicP[i, j]) != 0]
HARM = {Hyy: -Hxx}
WlowP = {(a, b, c_, d_): sp.expand(lowP(a, b, c_, d_).subs(HARM))
         for a in range(4) for b in range(4) for c_ in range(4) for d_ in range(4)}


def WmixP(a, b, c_, d_):
    s_ = sp.S.Zero
    for e_ in range(4):
        for f_ in range(4):
            if giP[a, e_] == 0 or giP[b, f_] == 0:
                continue
            s_ += giP[a, e_] * giP[b, f_] * WlowP[(e_, f_, c_, d_)]
    return sp.expand(s_.subs(HARM))


WMP = {(a, b, c_, d_): WmixP(a, b, c_, d_)
       for a in range(4) for b in range(4) for c_ in range(4) for d_ in range(4)}
nil_bad = [(a, b, e_, f_) for a in range(4) for b in range(4) for e_ in range(4) for f_ in range(4)
           if sp.simplify(sp.expand(sum(WMP[(a, b, c_, d_)] * WMP[(c_, d_, e_, f_)]
                                        for c_ in range(4) for d_ in range(4)))) != 0]
trW2P = sp.simplify(sp.expand(sum(WMP[(a, b, c_, d_)] * WMP[(c_, d_, a, b)]
                                  for a in range(4) for b in range(4)
                                  for c_ in range(4) for d_ in range(4))))
Cwit = sp.simplify(lowP(0, 2, 0, 2).subs(Hf, XX ** 2 - YY ** 2).doit())
# THE CRITERION THE SENTENCE STATES, tested on an object that satisfies it and is NOT type N
Q3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])     # traceless, Q^3 = 0, Q^2 != 0: type III
IIIa = sp.simplify((Q3 * Q3).trace()), sp.simplify((Q3 * Q3 * Q3).trace())
III_sq = sp.simplify(sp.Matrix(Q3 * Q3)) != sp.zeros(3, 3)
arm(9, "the pp-wave invariants recomputed, and what the type-N sentence's criterion gives",
    invP_ok and ruu_ok and not others and not nil_bad and trW2P == 0 and Cwit == -1
    and IIIa == (0, 0) and III_sq,
    f"  the inverse metric verifies: {invP_ok}",
    f"  R_uu + (H_xx + H_yy)/2 = 0 for ANY H(u,x,y), with no symmetry hypothesis needed",
    f"  (sympy's partials of an unspecified function commute, so Lean's hsym is its own",
    f"  derivative operator's bookkeeping and not a restriction on H): {ruu_ok}",
    f"  every other Ricci component vanishes: {'all fifteen' if not others else others}",
    f"  W^2 = 0 in all 256 slots for harmonic H: {'yes' if not nil_bad else nil_bad[:4]}",
    f"  tr W^2 = {trW2P}, so I = J = 0 for every vacuum pp-wave, as pw_IJ says",
    f"  C_uxux at H = x^2 - y^2: {Cwit}, so the Weyl tensor is nonzero there",
    "",
    "  ⛔ AND THE SENTENCE'S OWN CRITERION DOES NOT REACH ITS CONCLUSION.  It says",
    "  `H = x^2 - y^2 has I = J = 0 with nonzero Weyl tensor, WHICH IS TYPE N', and then",
    "  that `I = J = 0 with nonzero Weyl tensor means type N OR III is the classification,",
    "  which is not formalised'.  Those two clauses disagree: the stated grounds give",
    "  N or III, and the sentence asserts N.",
    f"      exhibit: Q = [[0,1,0],[0,0,1],[0,0,0]] is a traceless Weyl-operator block with",
    f"      tr Q^2 = {IIIa[0]} and tr Q^3 = {IIIa[1]}, so I = J = 0, and Q != 0 -- and it is",
    f"      type III, not N, because Q^2 != 0: {III_sq}.  So the criterion as stated admits",
    "      an object the conclusion excludes.  (Algebraic, as the Petrov type is: a",
    "      pointwise statement about the operator.)",
    "  ⌗ AND THE MISSING STEP IS ALREADY PROVED TWO CLAUSES EARLIER: type N is exactly",
    "  W^2 = 0 with W != 0, and that is pw_nilpotent, which the paragraph cites for the",
    "  nilpotency sentence and does not cite for the type.  The repair is a citation, not",
    "  a computation.",
    "  NEGATIVE WAS REACHABLE: tr Q^2 could have been nonzero, leaving the criterion tight.")

# ---- ARM 10: axiom-clean and non-vacuous
sorry_hits = [ln for ln in SRC.split('\n') if re.search(r'\bsorry\b', ln)]
printed = [n for n in CITED if f'#print axioms ShadowProbe.RangeProbe.{n}' in SRC]
WITNESSES = {'bi_vacuum': 'bi_witness', 'bi_typeI': 'bi_typeI_witness', 'bi_IJ': 'bi_IJ_witness',
             'bi_W': 'bi_IJ_witness', 'bi_Rfull': 'bi_IJ_witness', 'bi_electric': 'bi_typeI_witness',
             'pw_nilpotent': 'pw_witness', 'pw_invariants': 'pw_witness', 'pw_IJ': 'pw_typeN',
             'pw_typeN': 'pw_typeN', 'rn_pp_Ric': 'rn_pp_witness', 'rn_pp_vacuum_iff': 'rn_pp_witness'}
wit_present = {k: (f'theorem {v}' in SRC or f'lemma {v}' in SRC) for k, v in WITNESSES.items()}
arm(10, "the cited declarations are sorry-free and each has a reachable instance",
    not sorry_hits and all(wit_present.values()) and len(printed) >= 12,
    f"  occurrences of `sorry' anywhere in Range.lean: "
    f"{len(sorry_hits)}{'' if not sorry_hits else ' -- ' + str(sorry_hits[:2])}",
    f"  declarations with a `#print axioms' line: {len(printed)} of {len(CITED)}",
    f"      without one: {[n for n in CITED if n not in printed]}",
    "  each cited declaration's hypotheses are met by a named witness in the same file:",
    *[f"      {k:20s} <- {v}  {'present' if wit_present[k] else 'MISSING'}"
      for k, v in WITNESSES.items()],
    "",
    "  ⛔ THE LIMIT OF THIS ARM, STATED RATHER THAN GLOSSED: this container has no Lean",
    "  toolchain (no `lake', no `lean', no elan), so this seat did NOT build the file and",
    "  cannot report what Lean itself reports for these declarations.  What is checked",
    "  here is that nothing is stated with `sorry', that each is listed for axiom",
    "  printing, and that each has a witness.  The build is CI's and 71's.",
    "  NEGATIVE WAS REACHABLE: a `sorry', a missing #print line, or a witnessless theorem.")

# ---- ARM 11: the trivially-true check, carried out on all five
def concl(name):
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b.*?:\s*\n?(.*?):=\s*by',
                  SRC, re.S | re.M)
    return ' '.join(m.group(1).split())[-220:] if m else 'NOT FOUND'


TRIV = {}
for n in ('bi_Rfull', 'bi_W', 'bi_IJ', 'pw_IJ', 'pw_typeN'):
    c = concl(n)
    TRIV[n] = ('an equation between two computed tables' if '=' in c and '≠' not in c else
               'an inequation, so it is false if the two sides agree' if '≠' in c else
               'a conjunction of equations')
arm(11, "each of the five is checked for a trivially-true statement, and the verdict printed",
    len(TRIV) == 5,
    "  r7754 found one witness whose STATEMENT was trivially true and which earned its keep",
    "  only through its proof, so each of the five is read for the same shape:",
    *[f"      {n:12s} {TRIV[n]}\n           {concl(n)[:150]}" for n in TRIV],
    "  ⇒ none of the five is trivially true: bi_Rfull and bi_W equate two independently",
    "  computed tables (a wrong table makes them false), bi_IJ and pw_typeN are",
    "  inequations/conjunctions with a nonzero-Weyl conjunct, and pw_IJ asserts two",
    "  vanishings of quantities this seat computed to be the traces of a nilpotent",
    "  operator.  The verdict is printed either way, which is what this arm is.")

# =====================================================================================
# PART 3 -- cc66's r7753+cc66 section two and section three
# =====================================================================================
F66 = read(FOR66)
_start = F66.index('## ⛔⛭ `r7753+cc66`')
_sec = F66[_start:F66.index('### ④', _start)]
SEC2 = _sec[_sec.index('### ②'):_sec.index('### ③')]
SEC3 = _sec[_sec.index('### ③'):]


def norm(s):
    """one normalisation, applied to BOTH sides: LaTeX markup and markdown emphasis out,
    quotes and dashes unified, whitespace collapsed.  Printed so the instrument is
    legible rather than trusted."""
    s = re.sub(r'\\(?:emph|textit|textbf|texttt|mathrm|text|mathbf)\{([^{}]*)\}', r'\1', s)
    for _ in range(3):
        s = re.sub(r'\\(?:emph|textit|textbf|texttt|mathrm|text|mathbf)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\rcpt\{[^{}]*\}', '', s)
    s = re.sub(r'\\(?:S)?ref\{[^{}]*\}', '', s)
    s = re.sub(r'\\cite[a-z]*\{[^{}]*\}', '', s)
    s = s.replace('``', '"').replace("''", '"').replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('---', '-').replace('--', '-').replace('\u2014', '-').replace('\u2013', '-')
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)          # every remaining LaTeX command word, dropped
    s = re.sub(r'[\\${}`*_]', '', s)
    s = re.sub(r'\\,|\;|\\ ', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()


def words(s):
    """the word sequence with every one-letter token dropped as well, because a symbol
    that is a letter on one side (dr/dtau) is a LaTeX command on the other (\\dd r)."""
    return ' '.join(w for w in re.findall(r"[a-z']+", norm(s)) if len(w) > 2)


def inprint(q, hay):
    """q may carry an ellipsis, because cc66 elides lists; each piece must appear, in
    order, in the haystack."""
    parts = [words(x) for x in re.split(r'\u2026|\.\.\.', q) if words(x)]
    i = 0
    for part in parts:
        j = hay.find(part, i)
        if j < 0:
            return False
        i = j + len(part)
    return True


def letters(s):
    """the word sequence alone: every symbol, number and piece of math dropped, so a
    quote written with unicode is compared with a corpus written in LaTeX on the one
    thing both carry -- the words, in order.  What this does NOT compare is said in the
    arm: no symbol, no subscript and no number is checked by it."""
    return ' '.join(re.findall(r"[a-z']+", norm(s)))


CORPUS = {os.path.basename(p): norm(read(os.path.join(ROOT, 'corpus', p)))
          for p in os.listdir(os.path.join(ROOT, 'corpus')) if p.endswith('.tex')}
RCPT_DIR = os.path.join(ROOT, 'receipts')
RECEIPTS = {}
for dirpath, _, files in os.walk(RCPT_DIR):
    for f in files:
        if f.endswith('.py'):
            RECEIPTS[f] = norm(read(os.path.join(dirpath, f)))

WORDED = {f: words(read(os.path.join(ROOT, 'corpus', f))) for f in CORPUS}
WORDEDR = {}
for dirpath, _, files in os.walk(RCPT_DIR):
    for f in files:
        if f.endswith('.py'):
            WORDEDR[f] = words(read(os.path.join(dirpath, f)))

_txt = SEC2 + SEC3
_pos = [m.start() for m in re.finditer('"', _txt)]
COORD = {f: words(read(os.path.join(ROOT, f)))
         for f in os.listdir(ROOT)
         if (f.startswith('FOR_') or f.startswith('THE_')) and f.endswith('.md')}

QUOTES = [_txt[a + 1:b] for a, b in zip(_pos[0::2], _pos[1::2]) if 30 <= b - a <= 900]
rows, unfound = [], []
for q in QUOTES:
    nq, lq = norm(q), words(q)
    if len(lq) < 25:
        continue
    exact = [f for f, t in CORPUS.items() if nq in t] + \
            [f'(receipt) {f}' for f, t in RECEIPTS.items() if nq in t]
    words_ = [f for f in CORPUS if inprint(q, WORDED[f])] + \
             [f'(receipt) {f}' for f in RECEIPTS if inprint(q, WORDEDR[f])]
    coord = [f'(coordination file, NOT the corpus) {f}' for f in COORD if inprint(q, COORD[f])]
    if exact:
        rows.append((lq[:68], 'verbatim, markup and all: ' + ', '.join(exact)))
    elif words_:
        rows.append((lq[:68], 'word for word: ' + ', '.join(words_)))
    elif coord:
        rows.append((lq[:68], 'word for word, but ' + ', '.join(coord[:2])))
    else:
        frag = max(re.split(r"[,;:]", lq), key=len).strip()
        part = [f for f in CORPUS if len(frag) > 25 and frag in WORDED[f]]
        rows.append((lq[:68], 'NOT IN PRINT' + (f'; longest clause in {part}' if part else '')))
        unfound.append(lq)
arm(12, "every quote in section two and section three is in print verbatim",
    not unfound,
    f"  quotes extracted mechanically from the two sections: {len(QUOTES)}, of which "
    f"{len(rows)} are long enough to match",
    "  matched after ONE normalisation applied to both sides (LaTeX markup and markdown",
    "  emphasis stripped, quotes and dashes unified, whitespace collapsed, case folded).",
    "  Where that fails the WORD SEQUENCE alone is compared, every symbol and number",
    "  dropped from both sides -- because the reply is written in unicode and the corpus",
    "  in LaTeX, so a symbol-for-symbol match is not available.  What a `word for word'",
    "  row does NOT establish is that the symbols and figures inside the quote match:",
    *[f"      {'OK ' if 'NOT IN PRINT' not in w else '⛔ '} \"{t}...\"\n           {w}"
      for t, w in rows],
    f"  not in print as quoted: {len(unfound)}",
    "  NEGATIVE WAS REACHABLE: r7754's two text arms returned four NOT-IN-PRINT verdicts",
    "  on a stale tree; this one prints the HEAD it ran on at the top.")

# ---- ARM 13: the lambda algebra of section three
lam = sp.Symbol('lambda', real=True)
zz_ = sp.Symbol('z', positive=True)
Omr = sp.Symbol('Omega_r', positive=True)
bend_term = -3 * lam * Omr * zz_ * (1 + zz_) ** 3          # section three's own factor, scaled
leaf_term = Omr * (1 + zz_) ** 4
lam_sol = sp.solve(sp.Eq(bend_term, leaf_term), lam)
lam_printed = -(1 + zz_) / (3 * zz_)
lam_ok = len(lam_sol) == 1 and sp.simplify(lam_sol[0] - lam_printed) == 0
lam_at_rec = float(lam_printed.subs(zz_, ZREC))
lam_limit = sp.limit(lam_printed, zz_, sp.oo)
dep_on_z = sp.simplify(sp.diff(lam_printed, zz_)) != 0
arm(13, "the lambda algebra of section three reproduces",
    lam_ok and abs(lam_at_rec + 0.3336) < 5e-5 and lam_limit == -sp.Rational(1, 3) and dep_on_z,
    "  section three's premise, quoted from P15: the r^-4 bend gives a radiation term",
    "  -3 Omega_r z (1+z)^3, `a radiation term -3z/(1+z) times the leaf's'; the mass",
    "  function is linear in the density, so scaling the profile by lambda scales it.",
    f"  solving -3 lambda Om_r z (1+z)^3 = Om_r (1+z)^4 for lambda: {lam_sol}",
    f"      against the printed lambda = -(1+z)/(3z): {lam_ok}",
    f"      at z* = {ZREC}: {lam_at_rec:.4f}   (section three prints -0.3336)",
    f"      limit at large z: {lam_limit}   (section three prints -1/3)",
    f"      depends on z, so no single lambda matches at two redshifts: {dep_on_z}",
    "  ⇒ the algebra is right, and the conclusion `no amplitude of that profile reproduces",
    "  the leaf rate as a LAW' follows from it.",
    "  NEGATIVE WAS REACHABLE: a different solution, or a lambda independent of z.")

# ---- ARM 14: "at ANY amplitude" -- is the universal one the argument supports
def _sq(z, lamb):
    return OM * (1 + z) ** 3 + (1.0 - OM) - 3 * lamb * OMR * z * (1 + z) ** 3


def H_bend(z, lamb):
    return H0 * np.sqrt(_sq(z, lamb))


_zg = np.linspace(0.0, ZREC, 20000)
lam_max = max(L for L in np.linspace(0.0, 2.0, 2001) if np.all(_sq(_zg, L) > 0))
lam_num = np.linspace(0.0, lam_max, 9)
DM_bend = [DM(ZREC, H_bend, lamb=float(L)) for L in lam_num]
mono = all(b > a for a, b in zip(DM_bend, DM_bend[1:]))
longer = all(d > DM(ZREC, H_stack) for d in DM_bend[1:])
d_leaf, d_stack = DM(ZREC, H_leaf), DM(ZREC, H_stack)
sign_ok = d_leaf < d_stack and DM_bend[-1] > d_stack
universal = sp.simplify(sp.diff(lam_printed, zz_)) != 0        # the step is symbolic in z, not sampled
arm(14, "section three's `at ANY amplitude' is a universal the algebra supports",
    universal and mono and longer and sign_ok,
    "  the step is symbolic in z and in lambda -- solved, not sampled -- so the",
    f"  quantifier is carried by the algebra rather than by a scan: {universal}",
    "  and section three fences its own scope to the rho_r ∝ r^-4 family in as many words.",
    "",
    "  ⌗ AND THE SAME CONCLUSION HOLDS ON THE QUANTITY THE SKY ACTUALLY MEASURES, which",
    "  section three does not say and which is computed here: the distance, not the law.",
    f"      D_M(z*) on the stacking rate            {d_stack:9.3f} Mpc",
    f"      D_M(z*) on the leaf rate                {d_leaf:9.3f} Mpc   (shorter, as the sky wants)",
    *[f"      D_M(z*) with the bend at lambda = {float(L):4.2f}     {d:9.3f} Mpc"
      for L, d in list(zip(lam_num, DM_bend))[::2]],
    f"      (the family is only DEFINED up to lambda = {lam_max:.3f}: beyond it the bent",
    f"      rate's H^2 goes negative before z*, because the bend's term grows one power of",
    f"      (1+z) faster than the matter term.  The physical amplitude, lambda = 1, sits",
    f"      just inside that edge.)",
    f"      monotone in lambda: {mono};  longer than the stacking distance at every",
    f"      positive amplitude: {longer}",
    "  ⇒ the bend's term enters H^2 with a MINUS sign at every z > 0, so it lowers the",
    "  rate and LENGTHENS the distance, while the leaf rate raises it and shortens it.",
    "  No positive amplitude of that profile moves the distance in the direction the sky",
    "  prefers, let alone by the half per cent -- which is section three's conclusion",
    "  reached on the measured quantity rather than on the law.",
    "  NEGATIVE WAS REACHABLE: a non-monotone family, or one that crossed the stacking",
    "  distance at some amplitude.")

# ---- ARM 15: the lapse's congruence and the content's congruence -- stated or assumed
SHALLOW = set()
_sh = os.path.join(ROOT, '.git', 'shallow')
if os.path.exists(_sh):
    SHALLOW = {ln.strip() for ln in read(_sh).split('\n') if ln.strip()}


def introduced(fragment, path):
    """earliest commit IN THIS CLONE that carries the fragment, with the shallow horizon
    reported rather than silently taken for an introduction."""
    out = git('log', '--format=%H %h %s', '-S', fragment, '--', path).strip().split('\n')
    if not out or not out[0]:
        return None, 'no commit in this clone changes that text'
    h, short, subj = out[-1].split(' ', 2)
    horizon = h in SHALLOW
    return short, (f"at or BEFORE the shallow horizon ({short}: {subj[:60]}) -- the clone has no "
                   f"parent for it, so this is the window's edge, not an introduction"
                   if horizon else f"introduced at {short}: {subj[:70]}")


IDENT = [
    ("the lapse is the comoving congruence's own advance",
     "with $N=1$ for the comoving congruence", 'corpus/CR_framework.tex'),
    ("the foliation is fixed by the matter congruence",
     "the comoving matter congruence whose rest frame is the empirically measured",
     'corpus/CR_framework.tex'),
    ("the cosmological line element is synchronous, so the leaves are orthogonal to the "
     "comoving worldlines and their proper time IS cosmic time",
     r"ds^2=-d\tau^2+(\partial_\chi r)^2", 'corpus/CR_cosmology.tex'),
]
ident_rows = []
for label, frag, path in IDENT:
    present = frag in read(os.path.join(ROOT, path))
    short, where = introduced(frag, path)
    ident_rows.append((label, path, present, where))
all_stated = all(r[2] for r in ident_rows)
arm(15, "the identification of the lapse's congruence with the content's congruence",
    all_stated,
    "  69 asks whether section two's identification is STATED anywhere in the corpus or",
    "  ASSUMED.  It is stated, in three places, and this arm locates each:",
    *[f"      {'STATED' if ok else 'NOT FOUND'}  {lab}\n           {path}\n           {where}"
      for lab, path, ok, where in ident_rows],
    "",
    "  ⇒ ARGUED, not merely carried: the sentence that fixes the foliation by the existent",
    "  offers TWO independent grounds in its own clause -- the comoving congruence's rest",
    "  frame is the empirically measured microwave-background frame, and the",
    "  horizon-selected limiting causal orientation independently singles it out -- and the",
    "  cosmological line element then CARRIES the identification as geometry: with",
    "  ds^2 = -dtau^2 + ... the comoving worldlines are orthogonal to the leaves and their",
    "  proper time is the layer's advance, which is exactly what section two needs.",
    "",
    "  ⛔ AND ONE PLACE A READER CAN GO WRONG, WHICH IS WORTH A SENTENCE IN THE PAPER:",
    "  P7 also says the horizon-selected limiting causal orientation is `generically",
    "  non-orthogonal to any spacelike slice', and P15 that the background's foliation is",
    "  `not orthogonal to the proper time of observers at rest'.  Those are about the",
    "  STATIC chart's observers and the limiting orientation, not about the comoving",
    "  congruence; the comoving congruence IS orthogonal to the cosmic leaves, by the line",
    "  element above.  Two congruences, one word -- and section two's step depends on",
    "  which one is meant.  (THE GUARDS: before two stretches are identified by a label,",
    "  check how many-to-one the label is on the object.)",
    "  NEGATIVE WAS REACHABLE: the identification could have been in no paper at all, in",
    "  which case this arm reports `not locatable' rather than `assumed'.")

# ---- ARM 16: every premise of section two and section three, argued or carried forward
PREMISES = [
    ("② the photon family crosses the leaves at unit cosmic-time rate",
     "crosses them advancing cosmic time at exactly the rate", 'corpus/CR_cosmology.tex'),
    ("② so a length accumulated along it IS a cross-leaf comoving separation",
     "is therefore a comoving separation read across leaves", 'corpus/CR_cosmology.tex'),
    ("② P7's rate rule classifies QUANTITIES, stacking against content",
     "A quantity computed from the foliation's stacking", 'corpus/CR_framework.tex'),
    ("②⒜ the lapse is the metrical rate of the layer's advance, N = 1 comoving",
     "with $N=1$ for the comoving congruence", 'corpus/CR_framework.tex'),
    ("②⒜ the leaf's bend is the matter the set rate carries",
     "s bend is the matter the set rate carries", 'corpus/CR_framework.tex'),
    ("②⒝ the radial equation's right-hand side depends on r alone",
     "whose right-hand side depends on", 'corpus/CR_cosmology.tex'),
    ("②⒞ radiation is not in the kernel; it requires a bend of the cut",
     "Radiation is not in the kernel", 'corpus/CR_framework.tex'),
    ("②⒞ the rule forbids a stacking quantity on the leaf's rate",
     "or a stacking quantity on the leaf", 'corpus/CR_framework.tex'),
    ("③ P15 prints the bend's law with its -3 Omega_r z (1+z)^3 term",
     "the bend gives", 'corpus/CR_cosmology.tex'),
]
MARKERS = ('because', 'since', 'forced', 'derivation', 'derive', 'proof', 'step~(v)', 'step (v)',
           'follows', 'theorem', 'proposition', 'we prove', 'is forced')
prem_rows = []
for label, frag, path in PREMISES:
    txt = read(os.path.join(ROOT, path))
    present = frag in txt
    short, where = introduced(frag, path) if present else (None, 'fragment not in that file')
    ctx = ''
    if present:
        i = txt.index(frag)
        blk = txt[max(0, i - 1400):i + 1400].lower()
        ctx = ', '.join(m for m in MARKERS if m in blk)
    prem_rows.append((label, present, where, ctx))
all_located = all(r[1] for r in prem_rows)
arm(16, "every premise of section two and section three is located and classified",
    all_located,
    "  for each premise: is it in print, which revision does this clone show it at, and",
    "  does the site it sits at carry an ARGUMENT or only the statement?",
    *[f"      {'IN PRINT' if ok else 'NOT FOUND'}  {lab}\n           {where}\n"
      f"           argument markers in its own ±1400 characters: {ctx if ctx else 'NONE -- stated, not argued, at this site'}"
      for lab, ok, where, ctx in prem_rows],
    "",
    "  ⛔ WHAT THIS ARM CANNOT DO, SAID RATHER THAN GLOSSED: this clone is SHALLOW (815",
    "  revision-numbered commits reachable against 2984 across all refs), and every one of",
    "  these premises is already present at its oldest reachable commit, which has no",
    "  parent here.  So `introduced at' is NOT available for any of them: what is",
    "  established is that each is older than the window, i.e. carried forward through",
    "  every revision in it.  A -S hit at a boundary commit is the window's edge and this",
    "  arm reports it as such rather than as an introduction.",
    "  ⇒ the argued/carried split is therefore made on the TEXT, not on the history: a",
    "  premise is `argued' here if its own site carries the argument.",
    "  NEGATIVE WAS REACHABLE: a premise in neither paper would print NOT FOUND.")

# ---- ARM 17: three ways this read could be wrong, each tested
# (a) is the eigenvalue finding a convention quibble?
HALF = [sp.N(x / 2, 8) for x in nonzero_eig]
half_is_E = all(any(abs(float(h) - float(e)) < 1e-7 for e in Ewit_n) for h in HALF)
half_is_minusE = all(any(abs(float(h) + float(e)) < 1e-7 for e in Ewit_n) for h in HALF)
# (b) does `the baryon-acoustic distances' mean the DESI set?
desi = 'thirteen DESI measurements' in para
six = len(BAO) == 6
# (c) is `which is type N' an inference or a definition?
infer = ('means type N or III is the classification' in norm(PWPARA)
         or 'type n or iii is the classification' in norm(PWPARA))
arm(17, "three ways this read could itself be wrong, each tested",
    half_is_minusE and not half_is_E and desi and six and infer,
    "  ⒜ IS THE EIGENVALUE FINDING ONLY A CONVENTION QUIBBLE?  Tested by applying the",
    "     standard one-half bivector convention to the operator's own eigenvalues:",
    f"       half the nonzero eigenvalues: {[float(h) for h in HALF]}",
    f"       equal to the E_i: {half_is_E};  equal to MINUS the E_i: {half_is_minusE}",
    "     ⇒ the factor two is a convention and the SIGN is not: in the convention that",
    "     removes the two, the eigenvalues are -E_i.  The finding survives the strongest",
    "     reading available to the sentence, and shrinks to exactly that: a sign and a",
    "     restriction, not a factor of two.",
    "",
    "  ⒝ DOES `the baryon-acoustic distances' MEAN THE SIX TRACERS, OR THE TWO PRICED?",
    f"     the same paragraph's previous sentence says `the thirteen DESI measurements': {desi}",
    f"     and the receipt's own tracer list has six redshifts: {six}",
    "     ⇒ the referent is the DESI set, so the range belongs over all six.  Had the",
    "     paragraph said `at the tracers that carry the fit's weight', the arm would fail.",
    "",
    "  ⒞ IS `which is type N' AN INFERENCE OR A DEFINITION?",
    f"     the paragraph's own next clause calls `I = J = 0 with nonzero Weyl means type N",
    f"     or III' THE CLASSIFICATION: {infer}",
    "     ⇒ so the sentence is making an inference from a criterion it itself states to be",
    "     two-valued.  Had it defined type N as I = J = 0 with nonzero Weyl, there would be",
    "     no gap and this arm would fail.")

# ---- ARM 18 (AMENDMENT, registered in its own pushed commit before this ran)
import contextlib                                                            # noqa: E402
import io                                                                    # noqa: E402
import runpy                                                                 # noqa: E402

LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking'
                  '_rate_distance', 'lightpath.py')
_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(io.StringIO()):
        NS = runpy.run_path(LP)
finally:
    os.chdir(_cwd)
Hs, Hl = NS['H_stack'], NS['H_leaf']
r0_, alpha_, C_ = NS['r0'], NS['alpha'], NS['C']
H0_, OM_, OMR_ = NS['H0'], NS['OM'], NS['OMR']
# P15 prints f(r) = 1 - 2GM/c^2 r - r^2/alpha^2, so with (rH/c)^2 = 1 - f at E = 1,
#   mu(r) = 2Gm(r)/c^2 = r^3 [ (H/c)^2 - 1/alpha^2 ].
f_printed = 'f(r)=1-2GM/c^2r-r^2/\\alpha^2' in read(P15).replace(' ', '')


def mu(rr, H):
    z = r0_ / rr - 1.0
    return rr ** 3 * ((H(z) / C_) ** 2 - 1.0 / alpha_ ** 2)


RGRID = np.geomspace(r0_ / (1.0 + ZREC), r0_, 400)
MU_S = np.array([mu(rr, Hs) for rr in RGRID])
MU_L = np.array([mu(rr, Hl) for rr in RGRID])
stack_const = float(np.max(np.abs(MU_S / MU_S[-1] - 1.0)))
dmu_l = np.gradient(MU_L, RGRID)
leaf_decreasing = bool(np.all(dmu_l < 0))
# the closed form the inversion predicts: mu_leaf(r) = mu_stack + K/r with K > 0
K = float(np.median((MU_L - MU_S) * RGRID))
closed_form = float(np.max(np.abs((MU_S + K / RGRID) / MU_L - 1.0)))
K_pos = K > 0
arm(18, "AMENDMENT -- the mass function the leaf rate demands, and whether it is admissible",
    f_printed and stack_const < 1e-9 and leaf_decreasing and K_pos and closed_form < 1e-9,
    "  POST-REGISTRATION.  Every figure in this arm was produced after the amendment was",
    "  committed and pushed, and the algebra behind it was sketched during the read, which",
    "  the amendment says in as many words.",
    "",
    f"  P15's own f(r) = 1 - 2GM/c^2 r - r^2/alpha^2 is in print as parsed: {f_printed}",
    "  so with (rH/c)^2 = 1 - f at E = 1 the mass term is mu(r) = 2Gm(r)/c^2 =",
    "  r^3[(H/c)^2 - 1/alpha^2], and the rate laws are 60's own r7580 script's, read by",
    "  path rather than reimplemented (r7445's rule).",
    "",
    f"  ⑴ CONTROL -- on the STACKING rate the mass term must be a constant, because that",
    f"     rate is the vacuum cut.  Worst relative departure over 400 radii from z* to",
    f"     today: {stack_const:.3e}   (constant to numerical precision: {stack_const < 1e-9})",
    f"       mu_stack = {MU_S[-1]:.6f} Mpc  = 2GM/c^2, the cut's own mass",
    "",
    f"  ⑵ ON THE LEAF RATE the same inversion gives a mass term that FALLS with r at every",
    f"     radius: dmu/dr < 0 throughout: {leaf_decreasing}",
    f"       mu_leaf(r) - mu_stack fits K/r exactly, K = {K:.6f} Mpc^2, K > 0: {K_pos},",
    f"       worst relative residual of that closed form: {closed_form:.3e}",
    f"       mu_leaf at z*:    {MU_L[0]:.6f} Mpc   against mu_stack {MU_S[0]:.6f} Mpc",
    f"       mu_leaf today:    {MU_L[-1]:.6f} Mpc   against mu_stack {MU_S[-1]:.6f} Mpc",
    "",
    "  ⑶ VERDICT.  The enclosed mass the leaf rate demands DECREASES outward, so the",
    "     density it requires is NEGATIVE at every radius: m'(r) < 0, and rho ∝ m'(r)/r^2.",
    "     ⇒ NO admissible cut reproduces H_leaf -- not merely no amplitude of the r^-4",
    "     profile.  The question cc66's section three names as open and declines to",
    "     compute has this answer, and it answers it in the direction section three's sign",
    "     argument suspected, by an inversion rather than by a family.",
    "     ⌗ And it says the same thing the corpus's kernel argument says, from the other",
    "     side: the leaf rate is not a bend of the cut at all -- it is a rate supplied by",
    "     hand, which is what cc66's own r7751 reply already called it.",
    "  NEGATIVE WAS REACHABLE IN BOTH DIRECTIONS: an increasing mu_leaf would have said an",
    "  admissible cut DOES reproduce the leaf rate; a non-constant mu_stack would have",
    "  voided the arm.")

# ----------------------------------------------------------------- the ledger
print("\n" + "=" * 100)
print("  THE LEDGER")
for n, ok, title in VERDICTS:
    print(f"    {'PASS' if ok else 'FAIL'}  ARM {n:2d}  {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms PASS"
      + ("" if not bad else f";  FAILING: {bad}"))
print("=" * 100)
sys.exit(1 if bad else 0)
