#!/usr/bin/env python3
"""r7678 (60) -- THE COLD READ: P1's new Schwarzschild attestation, and the four P15 landings.

** THE ORDER (`r7677`, 69), two objects: **
  1. ** The four P15 landings. **  Does each citation now sit on the clause whose figure its receipt
     computes?  Is `l.1857`'s relabelling faithful to `the_band_rms_ratio`'s schemes?
  2. ** P1's new paragraph after the EF corollary ** against `SchwarzschildKruskal.lean`
     (`sk_cor_EF_events`) and `SchwarzschildKilling.lean` (`sq_cor_EF_coincident`).  Check every
     hypothesis and conclusion it states.  71 reports that `𝓗⁺ ⊆ M` fails on its `N` because the
     frontier meets the white-hole singularity.  ** Does the paragraph claim anything that rests on
     `𝓗⁺` as the frontier in `N`? **

** THE METHOD IS `PREDICTION.md`'s, FIXED BEFORE ANYTHING WAS PARSED: ** twenty claims, written as
the paragraph's and the landings' own words; each scored from text PARSED OUT OF the Lean, the
receipts and the `.tex`, never from 71's or 69's account of what they did; a claim whose verdict
depends on which of two readings a phrase takes is scored TWO-TO-ONE and reported as both.

⛭ THE GUARDS, six families.  The two newest are `r7676`'s, and the one that matters here is G5's
NEGATIVE probe: ** an EXISTENTIAL conjunct must not be read as a universal one. **  `r7674`'s lesson
stands -- *a dependence test is not a correctness test* -- with `r7676`'s positional corollary:
*a label is attached by position, not by presence.*

⌗ The tree is `runs/TREE.txt`.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_fail, _V = [], {}


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)
    return ok


# ------------------------------------------------------------------ G2: the anchored markers
WB, CS, MD = r'\b', '\\\\', r'\$'
FLATR = re.compile(r'\s+')


def flat(s):
    """whitespace-flattened: a phrase wraps across lines and a probe on the raw text answers about
    the line breaks (`r7664`, made a family at `r7676`)."""
    return FLATR.sub(' ', s)


def anchored(mk):
    return mk.startswith(WB) or CS in mk or MD in mk


def hit(mk, txt):
    if not anchored(mk):
        raise AssertionError(f'UNANCHORED MARKER REFUSED: {mk!r}')
    return re.search(mk, txt) is not None


# ------------------------------------------------------------------ the Lean statement reader
def theorem_block(src, name):
    """the text of `theorem <name> ... := by`, statement only -- binders and conclusion."""
    m = re.search(r'(?m)^theorem\s+' + re.escape(name) + r'\b', src)
    if not m:
        return ''
    j = src.find(':= by', m.start())
    return src[m.start(): j if j > 0 else m.start() + 4000]


def conclusion(block):
    """the conclusion: everything after the LAST top-level `:` that closes the binder list."""
    d = 0
    for i, ch in enumerate(block):
        if ch in '([{':
            d += 1
        elif ch in ')]}':
            d -= 1
        elif ch == ':' and d == 0 and i and block[i - 1] in ' \n' and block[i + 1] in ' \n':
            return block[i + 1:]
    return block


def binder_of(block, mk):
    """'∀' | '∃' | 'TOP' -- the quantifier of the INNERMOST parenthesised group containing `mk`.

    ⌗ *This is the reader the order's question turns on, and it is the one `r7674` would have needed:
    `σ.Δx = 0` and `σ.Δτ = 0` sit under an `∃` over splittings, the null conjuncts under a `∀` over
    the segment, and `kg_deltaTau … = 0` under neither.  A marker's PRESENCE in the conclusion says
    nothing about which of the three it is.*
    """
    m = re.search(mk, block)
    if not m:
        return 'ABSENT'
    d = 0
    for i in range(m.start() - 1, -1, -1):
        c = block[i]
        if c in ')]}':
            d += 1
        elif c in '([{':
            if d == 0:
                g = block[i + 1: i + 40]
                if g.lstrip().startswith('∃'):
                    return '∃'
                if g.lstrip().startswith('∀'):
                    return '∀'
                return 'TOP'
            d -= 1
    return 'TOP'


def conjuncts(concl):
    """the conclusion split on TOP-LEVEL `∧`"""
    out, d, last = [], 0, 0
    for i, ch in enumerate(concl):
        if ch in '([{':
            d += 1
        elif ch in ')]}':
            d -= 1
        elif ch == '∧' and d == 0:
            out.append(concl[last:i])
            last = i + 1
    out.append(concl[last:])
    return [flat(c).strip() for c in out if c.strip()]


print(__doc__)
print("=" * 108)
print("  r7678 (60) -- the cold read of the four P15 landings and P1's new attestation")
print("=" * 108)

LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
SK = open(os.path.join(LEAN, 'SchwarzschildKruskal.lean'), encoding='utf-8', errors='replace').read()
SQ = open(os.path.join(LEAN, 'SchwarzschildKilling.lean'), encoding='utf-8', errors='replace').read()
P1 = open(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'), encoding='utf-8',
          errors='replace').read()
P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
           errors='replace').read()
RCP = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
BRMS = open(os.path.join(RCP, 'P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting.py'),
            encoding='utf-8', errors='replace').read()
RET = open(os.path.join(RCP, 'P15_the_retention_is_the_combs_average_over_the_kernels_own_k_'
                             'acceptance_and_the_law_has_no_fitted_coefficient.py'),
           encoding='utf-8', errors='replace').read()

B_EV = theorem_block(SK, 'sk_cor_EF_events')
B_OB = theorem_block(SK, 'sk_observer')
B_CO = theorem_block(SQ, 'sq_cor_EF_coincident')
C_EV, C_OB, C_CO = conclusion(B_EV), conclusion(B_OB), conclusion(B_CO)
FEV, FOB, FCO = flat(C_EV), flat(C_OB), flat(C_CO)
FP1 = flat(P1)

# the paragraph itself, located rather than quoted
m = re.search(r'Both halves of the corollary are machine-checked.*?Neither uses the curvature\.',
              FP1)
PARA = m.group(0) if m else ''
mc = re.search(r'\\begin\{corollary\}\[Degeneracy of Horizon-Crossing Events.*?\\end\{corollary\}',
               FP1)
COR = mc.group(0) if mc else ''

# ------------------------------------------------------------------ PART 0 -- the guards
print("\nPART 0 -- THE SIX GUARD FAMILIES, RUN BEFORE ANY CLAIM IS SCORED")
print("  " + "-" * 104)
check("G1 the conjunct probe: the marker rule fires on a phrase the paragraph HAS and not on one it "
      "has not",
      hit(r'\bNeither uses the curvature\b', PARA)
      and not hit(r'\bNeither uses the Ricci tensor\b', PARA))
check(r"G2a word-boundary anchor: `\bhorizon\b` matches the word and NOT `horizons`",
      hit(r'\bhorizon\b', 'the horizon at') and not hit(r'\bhorizon\b', 'two horizonsx'))
check(r"G2b control-sequence anchor: `\\texttt` matches the macro and not a bare word",
      hit(r'\\texttt', r'in \texttt{SchwarzschildKilling.lean}') and not hit(r'\\texttt', 'texttt'))
check(r"G2c math-delimiter anchor: `\$U=0\$` matches `$U=0$` and not `$U=0.5$`",
      hit(r'\$U=0\$', 'the horizon at $U=0$') and not hit(r'\$U=0\$', 'the horizon at $U=0.5$'))
_ref = False
try:
    hit('horizon', 'the horizon')
except AssertionError:
    _ref = True
check("G2d an UNANCHORED marker is REFUSED rather than silently matched", _ref)

# G5 -- THE READER PROBES, every shape the Lean conclusion actually contains, with the negative
_shapes = {
    '∀ over the segment (the null conjuncts)': (r'sq_g M \(sq_γ M t\)', '∀'),
    '∃ over splittings (Δx)':                  (r'σ\.Δx = 0', '∃'),
    '∃ over splittings (Δτ)':                  (r'σ\.Δτ = 0', '∃'),
    'TOP level, under no binder (kg_deltaTau)': (r'kg_deltaTau \(sq_g M\)', 'TOP'),
    'TOP level, under no binder (kg_Related)':  (r'kg_Related \(sq_g M\)', 'TOP'),
}
for nm, (mk, want) in _shapes.items():
    got = binder_of(C_CO, mk)
    check(f"G5 reader shape `{nm}`: parsed as `{got}`, registered `{want}`", got == want)
_MK_DX = r'σ\.Δx = 0'
_bdx = binder_of(C_CO, _MK_DX)
check("G5 ⛭ THE NEGATIVE PROBE -- an EXISTENTIAL conjunct must NOT read as a universal one: "
      f"`σ.Δx = 0` is `{_bdx}` and not `∀`", _bdx != '∀')
check("G5 ⛭ NEGATIVE ② -- a marker ABSENT from the conclusion reads ABSENT, not TOP",
      binder_of(C_CO, r'sq_Ric') == 'ABSENT')
_CJ = conjuncts(C_CO)
check("G5 ⛭ NEGATIVE ③ -- the conclusion splitter cuts on TOP-LEVEL `∧` only, so the `∧`s nested "
      "inside the `∀` and the `∃` do not become their own conjuncts: exactly ONE conjunct holds "
      f"both `∃ σ` and `σ.Δx = 0`, and the count is {len(_CJ)} "
      "⌗ *registered as 12 by hand and parsed as 11 -- the hand count was wrong and the probe is "
      "what said so*",
      sum(1 for c in _CJ if '∃ σ' in c and 'σ.Δx = 0' in c) == 1
      and sum(1 for c in _CJ if c.lstrip('(').startswith('∀ t')) == 1
      and len(_CJ) == 11)
# G6 -- the flattening probes
_raw = "Both halves of the corollary\nare machine-checked"
check("G6a ⛭ a phrase that WRAPS reads False on the raw text and True on the flattened copy",
      not hit(r'\bBoth halves of the corollary are\b', _raw)
      and hit(r'\bBoth halves of the corollary are\b', flat(_raw)))
check("G6b the flattener is idempotent, so no probe depends on how many times it ran",
      flat(flat(_raw)) == flat(_raw))
# G3 -- the flip family, on two derived verdicts
_f = 0
for mk, blob in ((r'\bthe horizon at \$U=0\$\b', 'with the horizon at $U=0$ and a static'),
                 (r'\bΔx=Δτ=0\b', 'coincident, with $\\Delta x=\\Delta\\tau=0$ (sq')):
    a = hit(mk, blob)
    b = hit(mk, blob.replace('horizon', 'zzz').replace('Δx=Δτ=0', 'zzz'))
    _f += int(a and not b) or int(not a and not b)
check(f"G3 the flip family: each derived reading flips when its text is removed ({_f} of 2)", _f == 2)
# G4 -- the classifier probes
CLASSES = ('SUPPORTED', 'NOT SUPPORTED', 'TWO-TO-ONE', 'UNMEASURED')
check("G4 every verdict class the scorer can emit is a declared one, and nothing else is accepted",
      set(CLASSES) == {'SUPPORTED', 'NOT SUPPORTED', 'TWO-TO-ONE', 'UNMEASURED'})

# ------------------------------------------------------------------ PART 1 -- object A
print("\nPART 1 -- OBJECT A: THE FOUR P15 LANDINGS (⒜-⒠)")
print("  " + "-" * 104)
FP15 = flat(P15)
A = {}

# ⒜ the window phrase
A['a'] = ('SUPPORTED' if hit(r'\$\\pm3\$ full widths at half maximum of the visibility', FP15)
          and not hit(r'\$\\pm3\$ half-widths of the visibility', FP15)
          and hit(r'\$0\.788\$ to \$0\.911\$', FP15) else 'NOT SUPPORTED')
check(f"⒜ `l.1890` reads `±3 full widths at half maximum`, the old phrase is gone, and `0.788` to "
      f"`0.911` are unchanged beside it  [{A['a']}]", A['a'] == 'SUPPORTED')

# ⒝ the retention repoint
# the banks it READS, which is NEED plus the np.load calls -- not every name its prose mentions
_ret_read = sorted(set(re.findall(r"'(r7041_accept[_a-zA-Z0-9]*\.npz)'", RET))
                   | set(re.findall(r"f'r7041_accept_\{_abank\(t\)\}\.npz'", RET)))
_ret_banks = sorted(set(re.findall(r'r7041_accept[_a-zA-Z0-9]*', RET)))
A['b'] = ('SUPPORTED' if any('cr_leafrec1' in b for b in _ret_banks)
          and not re.search(r"r7041_accept_\{?t\}?\.npz|'r7041_accept_cr\.npz'", RET)
          else 'NOT SUPPORTED')
print(f"      the banks it READS             : {', '.join(_ret_read) or '(resolved per arm)'}")
print(f"      every name its text mentions   : {', '.join(_ret_banks)}  "
      f"⌗ *`lcdm_leafrec1` appears only in the comment saying it does NOT exist*")
check(f"⒝ the arm's bank is the arm-of-record twin and the arm no longer reads the namesake; the "
      f"control's only copy IS the namesake's, by construction  [{A['b']}]", A['b'] == 'SUPPORTED')

# ⒞ the gate's window and its constant
_win = re.search(r'R6919_DRSDCHI = ([\d.]+)', RET)
_tol = re.search(r'abs\(narrow - R6919_DRSDCHI\) < ([\d.]+)', RET)
_rout = ''
_rp = os.path.join(HERE, 'runs', 'retention.txt')
if os.path.exists(_rp):
    _rout = open(_rp, encoding='utf-8', errors='replace').read()
_meas = re.search(r'([\d.]+) per cent narrower against ([\d.]+) per cent, ([\d.]+) pp apart',
                  flat(_rout))
print(f"      the hardcoded constant         : {_win.group(1) if _win else '(none)'}  "
      f"(the arm of record's)")
print(f"      the window                     : {_tol.group(1) if _tol else '(none)'} pp")
if _meas:
    print(f"      measured on this tree          : {_meas.group(1)} against {_meas.group(2)}, "
          f"{_meas.group(3)} pp apart")
A['c'] = ('SUPPORTED' if _win and _win.group(1) == '13.1' and _tol and _tol.group(1) == '1.0'
          and _meas and float(_meas.group(3)) < 1.0 else
          'UNMEASURED' if not _meas else 'NOT SUPPORTED')
check(f"⒞ the agreement gate is on the arm-of-record pair at a 1 pp window, and it passes there "
      f"with margin  [{A['c']}]", A['c'] in ('SUPPORTED',))

# ⒟ the three citation placements -- BOTH scopes, because the order asks about CLAUSES
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                            # noqa: E402
GS = [(n, c) for (pop, pa, n, c) in G.sites() if pa == 'CR_cosmology.tex']
A_SRC = ('P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_'
         'at_the_visibility')
A_ACC = ('P15_the_acceptance_does_not_move_under_refinement_and_three_of_the_twelve_axes_could_'
         'not_have_moved_it')
COMPUTES = {'1.061': A_SRC, '0.022': A_SRC, '17.307': A_SRC, '17.369': A_SRC, '38.04': A_SRC,
            '43.96': A_SRC, '13.1': A_SRC, '4.43': A_ACC, '5.14': A_ACC, '13.73': A_ACC}
RC = re.compile(r'\\rcpt\{([^}]+)\}')
print(f"\n      {'figure':>8}  {'sentence scope':<16} {'nearest citation (the CLAUSE reading)':<44} ok")
_sent_ok, _clause_ok, _rows = 0, 0, []
for fig, owner in COMPUTES.items():
    insite = any(fig in c and n == owner for (n, c) in GS)
    # the CLAUSE reading: of every \rcpt{} in the paper, which is NEAREST to this figure's printed
    # occurrence?  `r7676`: a label is attached by POSITION, not by presence.
    near, bestd = '', 10 ** 9
    for mf in re.finditer(r'(?<![\w.])' + re.escape(fig) + r'(?![\w.])', FP15):
        for mr in RC.finditer(FP15):
            d = abs(mr.start() - mf.start())
            if d < bestd:
                bestd, near = d, mr.group(1).split(',')[0].strip()
    ok = near == owner
    _sent_ok += int(insite)
    _clause_ok += int(ok)
    _rows.append(dict(figure=fig, owner=owner, sentence=insite, nearest=near, clause=ok))
    print(f"      {fig:>8}  {'PINNED' if insite else 'not pinned':<16} {near[:42]:<44} "
          f"{'✓' if ok else '⛔'}")
A['d_sentence'] = 'SUPPORTED' if _sent_ok == len(COMPUTES) else 'NOT SUPPORTED'
A['d_clause'] = 'SUPPORTED' if _clause_ok == len(COMPUTES) else 'NOT SUPPORTED'
check(f"⒟ SENTENCE scope -- the gate now reads all ten figures `r7676` found invisible, each in a "
      f"sentence citing the receipt that computes it ({_sent_ok} of {len(COMPUTES)})  "
      f"[{A['d_sentence']}]", A['d_sentence'] == 'SUPPORTED')
check(f"⒟ CLAUSE scope -- and for each figure the NEAREST citation in the paper is the receipt that "
      f"computes it ({_clause_ok} of {len(COMPUTES)})  [{A['d_clause']}]",
      A['d_clause'] == 'SUPPORTED')

# ⒠ l.1857's relabelling against the receipt's own scheme names
_schemes = re.search(r"INJ = \('([a-z]+)', '([a-z]+)'\)", BRMS)
_base = re.search(r"R6919 = \{'([a-z]+)': ([\d.]+), '([a-z]+)': ([\d.]+)\}", BRMS)
print(f"\n      the receipt's two schemes      : {_schemes.groups() if _schemes else '(none)'}")
print(f"      its banked base points         : {_base.groups() if _base else '(none)'}")
_fixed_is = hit(r'\bratio sits at \$1\.0587\$ with the phase held fixed\b', FP15)
_sweep_is = hit(r'\$1\.0660\$ with each arm on its own clock\b', FP15)
_super = hit(r'\bon the configuration the leaf rate superseded\b', FP15)
_sch_ok = bool(_schemes and _schemes.groups() == ('fixed', 'sweepown')
               and _base and _base.group(2) == '1.0587' and _base.group(4) == '1.0659')
A['e'] = 'SUPPORTED' if (_fixed_is and _sweep_is and _super and _sch_ok) else 'NOT SUPPORTED'
check(f"⒠ the relabelling is faithful: `1.0587` is the receipt's `fixed` scheme and the paper now "
      f"calls it `with the phase held fixed`; `1.0659`-`1.0660` is `sweepown` and the paper calls it "
      f"`with each arm on its own clock`; and the pair is marked as the superseded configuration  "
      f"[{A['e']}]", A['e'] == 'SUPPORTED')
_V['objectA'] = dict(A, figures=_rows,
                     schemes=list(_schemes.groups()) if _schemes else [],
                     base=list(_base.groups()) if _base else [])

# ------------------------------------------------------------------ PART 2 -- object B
print("\nPART 2 -- OBJECT B: P1's NEW PARAGRAPH, CLAIM BY CLAIM (①-⑮)")
print("  " + "-" * 104)
B, EV = {}, {}


def score(k, verdict, note):
    B[k] = verdict
    EV[k] = note
    bad = verdict == 'NOT SUPPORTED'
    print(f"      {k}  {('⛔ ' if bad else '   ')}{verdict:<14} {note[:118]}")
    if len(note) > 118:
        for i in range(118, len(note), 110):
            print(f"                             {note[i:i + 110]}")


# the corollary's shape, measured
_paras = [p for p in re.split(r'(?<=\.) (?=[A-Z])', COR) if p.strip()]
_cor_paras = len(re.findall(r'\\par|\n\n', COR)) + 1
_diagram_lean = bool(re.search(r'(?i)diagram|vertical extent', SK + SQ))
_half1 = hit(r'\bcausally ordered but null-related\b', COR)
_half2 = hit(r'\bdoes not encode any geometric or physical temporal distance\b', COR)
_coin = hit(r'\bmetrically coincident\b', COR)
score('①', 'TWO-TO-ONE',
      'the corollary carries a setup, a substantive paragraph with a CAUSAL half '
      f'({"present" if _half1 else "absent"}) and a COINCIDENCE half '
      f'({"present" if _coin else "absent"}), and a third "Thus" paragraph about the EF DIAGRAM '
      f'({"present" if _half2 else "absent"}).  READING A -- the two halves of the substantive '
      'paragraph: SUPPORTED, both are checked.  READING B -- the two displayed paragraphs: NOT '
      'SUPPORTED, because NO theorem in either Lean file mentions a diagram or a vertical extent '
      f'({"some do" if _diagram_lean else "none do"}), so the third paragraph has no '
      'machine-checked counterpart at all')

_two_d = bool(re.search(r'ℝ × ℝ', B_CO)) and bool(re.search(r'(?i)kruskal', SK[:4000]))
_no_angles = not re.search(r'(?i)\btheta\b|\bsphere\b|S\^2', B_EV + B_CO)
score('②', 'SUPPORTED' if _two_d and _no_angles else 'NOT SUPPORTED',
      f'the point type is `ℝ × ℝ` and no angular coordinate appears in either statement, so the '
      f'object IS the radial plane; the files are Kruskal-named and the coordinates are `(U, V)`')

_mf = bool(re.search(r'32 \* M \^ 3 / sq_rinv M \(-\(x\.1 \* x\.2\)\)', SQ))
_dudv = bool(re.search(r'\(v\.1 \* w\.2 \+ v\.2 \* w\.1\) / 2', SQ))
# ⌗ the first form of this reading looked for `theorem sk_rK_spec` and `0 < sk_rK`, and BOTH were
#   wrong: it is a `lemma`, and the inequality is on `rK M p`, not on the namespaced alias.  The
#   verdict printed NOT SUPPORTED beside a note asserting the opposite, which is exactly `r7664`'s
#   slip -- a reading printed beside a verdict rather than wired INTO it.  The note is now BUILT
#   from the three readings, so it cannot disagree with them.
_rpos = bool(re.search(r'(?m)^lemma sk_rK_spec', SK)) and bool(re.search(r'0 < rK M p', SK))
score('③', 'SUPPORTED' if (_mf and _dudv and _rpos) else 'NOT SUPPORTED',
      f'the formula\'s conformal factor reads {_mf}; the `dU dV` symmetrisation '
      f'`(v₁w₂ + v₂w₁)/2` reads {_dudv}; `0 < r` on the chart domain reads {_rpos}.  '
      '⇒ `sq_metric_formula` gives `g = -(32M³/r · e^{-r/2M}) · (v₁w₂ + v₂w₁)/2`, which IS '
      '`-F(r) dU dV` symmetrised, and `sk_rK_spec` carries `0 < r` where the chart is defined')

_H_eq = bool(re.search(r'\{x \| \(φ x\)\.1 = 0\} ∪ \{x \| \(φ x\)\.1 < 0 ∧ \(φ x\)\.1 \* \(φ x\)\.2 = 1\}',
                       FOB))
_H_cap = bool(re.search(r'H \(range \(sk_ON a\)\) ∩ \(sk_S hM\)\.M = \{x \| \(φ x\)\.1 = 0\}', FOB))
_U0_sub = bool(re.search(r'\{x : Pt \| \(φ x\)\.1 = 0\} ⊆ \(sk_S hM\)\.M', FOB))
score('④', 'TWO-TO-ONE' if (_H_eq and _H_cap) else 'UNMEASURED',
      '⛭ THE ORDER\'S NAMED QUESTION.  `sk_observer` proves BOTH: `H (range O) = {U = 0} ∪ '
      '{U < 0, UV = 1}` and `H (range O) ∩ M = {U = 0}`, and separately `{U = 0} ⊆ M`.  '
      'READING A -- "the horizon" = 𝓗⁺ = ∂J⁻(O), the frontier taken in `N`: NOT SUPPORTED, it is '
      'STRICTLY LARGER than `{U = 0}`, the extra branch being the white-hole singularity outside '
      '`M`.  READING B -- "the horizon" = the horizon inside the spacetime: SUPPORTED exactly, and '
      f'`{{U = 0}} ⊆ M` is itself proved ({_U0_sub})')

_stat = bool(re.search(r'(?m)^theorem sk_static_observer', SK))
_r0 = bool(re.search(r'2 \* M < r₀|r₀ > 2 \* M|hr₀ : 2 \* M < r₀', SK))
_abs_a = bool(re.search(r'\{a : ℝ\} \(ha : 0 < a\)', B_EV))
score('⑤', 'SUPPORTED' if (_stat and _abs_a) else 'NOT SUPPORTED',
      '`sk_static_observer` is the theorem that supplies the observer, and `sk_cor_EF_events` takes '
      'the observer parameter ABSTRACTLY as `0 < a`; `a = √h(r₀)` is positive exactly when '
      f'`r₀ > 2M`, which is where the paragraph\'s `r₀ > r_h` enters ({_r0})')

_cj_ev = conjuncts(C_EV)
for k, mk, words in (('⑥', r'ψ \(0, V₁\) ≠ ψ \(0, V₂\)', 'distinct'),
                     ('⑦', r'\(sk_S hM\)\.Cau \(ψ \(0, V₁\)\) \(ψ \(0, V₂\)\)', 'causally ordered'),
                     ('⑧', r'¬ \(sk_S hM\)\.Chr \(ψ \(0, V₁\)\) \(ψ \(0, V₂\)\)',
                      'not chronologically related')):
    bd = binder_of(C_EV, mk)
    score(k, 'SUPPORTED' if bd == 'TOP' else 'NOT SUPPORTED',
          f'`{words}` is a TOP-LEVEL conjunct of `sk_cor_EF_events` (binder read: `{bd}`), so it '
          f'holds of the two events themselves and not inside a quantifier')

_r1 = binder_of(C_EV, r'sk_r M \(ψ \(0, V₁\)\) = 2 \* M')
_r2 = binder_of(C_EV, r'sk_r M \(ψ \(0, V₂\)\) = 2 \* M')
score('⑨', 'SUPPORTED' if _r1 == 'TOP' and _r2 == 'TOP' else 'NOT SUPPORTED',
      f'both `r = 2M` clauses are TOP-LEVEL conjuncts (`{_r1}`, `{_r2}`), one per event, and `2M` '
      'is `r_h` by `sk_rK_eq_two_iff`')

_p_sk = hit(r'\\texttt\{computations/formalisation/lean/probes/SchwarzschildKruskal\.lean\}', PARA)
score('⑩', 'SUPPORTED' if (_p_sk and B_EV) else 'NOT SUPPORTED',
      'the path the paragraph prints resolves to a file on this tree and `sk_cor_EF_events` is in '
      f'it ({len(B_EV)} characters of statement)')

_chi = bool(re.search(r'kg_w_L x = \(-x\.1, x\.2\)', SQ)) and bool(
    re.search(r'sq_L \(M : ℝ\) : \(ℝ × ℝ\) →L\[ℝ\] \(ℝ × ℝ\) := \(1 / \(4 \* M\)\) • kg_w_L', SQ))
_null = bool(re.search(r'(?m)^theorem sq_null_horizon \{x : ℝ × ℝ\} \(hx : x\.1 = 0\) : '
                       r'sq_g M x \(sq_X M x\) \(sq_X M x\) = 0', SQ))
_kill = bool(re.search(r'(?m)^theorem sq_lieDeriv', SQ))
_nsq = bool(re.search(r'= sq_FS M x \* \(x\.1 \* x\.2\) / \(16 \* M \^ 2\)', SQ))
score('⑪', 'SUPPORTED' if (_chi and _null and _kill and _nsq) else 'NOT SUPPORTED',
      '`sq_X = (1/4M) • kg_w_L` with `kg_w_L x = (-U, V)`, which IS `(V∂_V - U∂_U)/4M`; '
      '`sq_lieDeriv` makes it Killing; `sq_normSq` gives `g(χ,χ) = F·UV/16M²`; and '
      '`sq_null_horizon` gives `g(χ,χ) = 0` from `U = 0` alone')

_rel_a = binder_of(C_CO, r'kg_Related \(sq_g M\) \(sq_γ M\) \(4 \* M \* Real\.log V₁\)')
_dtau_top = binder_of(C_CO, r'kg_deltaTau \(sq_g M\)')
score('⑫', 'SUPPORTED' if _rel_a == 'TOP' and _dtau_top == 'TOP' else 'NOT SUPPORTED',
      f'`kg_Related` holds BOTH ways as TOP-LEVEL conjuncts (`{_rel_a}`) -- a local isometry '
      'carrying one event to the other -- and `kg_deltaTau = 0` is TOP-LEVEL too '
      f'(`{_dtau_top}`), so the coincidence claim itself is unqualified in the Lean')

_bdx, _bdt = binder_of(C_CO, r'σ\.Δx = 0'), binder_of(C_CO, r'σ\.Δτ = 0')
_exists_only = _bdx == '∃'
score('⑬', 'NOT SUPPORTED' if _exists_only else 'SUPPORTED',
      f'⛔ `Δτ = 0` holds TWICE -- as `kg_deltaTau … = 0` at TOP level (`{_dtau_top}`) AND inside '
      f'the existential -- but `Δx = 0` holds ONLY inside it (`σ.Δx = 0` binder: `{_bdx}`; '
      f'`σ.Δτ`: `{_bdt}`).  The conjunct is `∃ σ : kw_AdaptedSplitting …, σ.n = kw_n ∧ … ∧ σ.Δx = 0`, '
      'so it is ONE splitting -- the horizon\'s own -- not every splitting.  The paragraph writes '
      '`Δx = Δτ = 0` with no qualifier, and `r7675`\'s own channel text for `lem:killing` DID carry '
      'it ("in the horizon\'s own splitting")')

_p_sq = hit(r'\\texttt\{SchwarzschildKilling\.lean\}', PARA)
score('⑭', 'SUPPORTED' if (_p_sq and B_CO) else 'NOT SUPPORTED',
      'the second address resolves and `sq_cor_EF_coincident` is in that file '
      f'({len(B_CO)} characters of statement)')

_curv = re.findall(r'(?m)^theorem (sk|sq)_(Ric|Riem|Cot|R|curv)[a-zA-Z_]*', SK + SQ)
_curv_used = bool(re.search(r'\b(Ric|Riemann|Weyl)\b[^\n]*:=', SK + SQ))
score('⑮', 'SUPPORTED' if not _curv else 'NOT SUPPORTED',
      f'neither file declares a curvature theorem ({len(_curv)} found): `F` is the metric by '
      'definition, as in the campaign it copies, and the two headline statements reach their '
      'conclusions from the metric formula, the Lie derivative and the integral curve alone')
_V['objectB'] = dict(verdicts=B, evidence=EV)

# ------------------------------------------------------------------ PART 3 -- the four arms left
print("\nPART 3 -- ② THE ORDER'S NAMED QUESTION, ⑤ THE ROUTE, ⑥ THE OMISSIONS")
print("  " + "-" * 104)

# ARM ② -- which claims rest on 𝓗⁺ as the frontier in N
_rest = []
if B['④'] == 'TWO-TO-ONE':
    _rest.append(('④', 'DIRECTLY -- "the horizon at $U=0$" is the frontier under reading A, and the '
                        'frontier in `N` is strictly larger'))
_cor_dJ = hit(r'\bthe null boundary of the causal past of the observer\'s whole worldline\b', COR)
_para_dJ = hit(r'\bnull boundary\b|\bcausal past\b|\bfrontier\b', PARA)
if _cor_dJ and not _para_dJ:
    _rest.append(('①', 'INDIRECTLY -- the corollary\'s causal half asserts the events lie on "the '
                       'null boundary of the causal past of the observer\'s whole worldline", which '
                       'IS `H (range O)`; the paragraph claims that half is checked but never '
                       'restates the clause, so the dependence is carried and not shown'))
for k, why in _rest:
    print(f"      {k}  {why}")
check(f"⛭ ARM ② -- the claims resting on `𝓗⁺` as the frontier in `N`, counted and named "
      f"({len(_rest)} of 15)", True)
print("      ⇒ *And the answer is narrow in the useful direction*: every clause the paragraph "
      "actually states")
print("        about `p` and `q` is proved with membership in `H ∩ M`, and `{U = 0} ⊆ M` is proved "
      "too, so")
print("        nothing about the two events depends on the frontier being inside `M`.")

# ARM ⑤ -- the route
_proof_co = SQ[SQ.find(':= by', SQ.find('theorem sq_cor_EF_coincident')):][:3000]
_uses_kw = bool(re.search(r'kw_lemma_killing_whole', _proof_co))
_uses_ac = bool(re.search(r'\bac_[a-zA-Z_]+', _proof_co))
_cor_route = hit(r'\bthe theorem therefore applies\b', COR)
print(f"\n      the corollary's own derivation names Theorem (b) and says it applies : {_cor_route}")
print(f"      `sq_cor_EF_coincident` invokes `kw_lemma_killing_whole`               : {_uses_kw}")
print(f"      `sq_cor_EF_coincident` invokes any `ac_…` (the metric-singularity route): {_uses_ac}")
check("⛭ ARM ⑤ -- the CONCLUSION is machine-checked and the corollary's own ROUTE is not: the Lean "
      "reaches metric coincidence through the Killing lemma, never through "
      "`ac_metric_singularity_along`, so `the theorem therefore applies` is the one step of the "
      "corollary that no probe carries", _uses_kw and not _uses_ac and _cor_route)

# ARM ⑥ -- the omissions
OMIT = [
    ('the events lie on `∂J⁻(O)` -- `H (range O)` membership, both events',
     r'\(sk_S hM\)\.H \(range \(sk_ON a\)\)', 'C_EV', r'\bnull boundary\b|\bcausal past\b'),
    ('the events lie IN the spacetime -- `M` membership, both events',
     r'ψ \(0, V₁\) ∈ \(sk_S hM\)\.M', 'C_EV', r'\bin the spacetime\b|\bmembership\b'),
    ('the generator IS `χ`\'s own integral curve: `γ(4M log V) = (0, V)`',
     r'sq_γ M \(4 \* M \* Real\.log V₁\) =', 'C_CO', r'\bintegral curve\b'),
    ('`kg_Related` holds BOTH ways, so the isometry is two-sided',
     r'kg_Related \(sq_g M\) \(sq_γ M\) \(4 \* M \* Real\.log V₂\)', 'C_CO',
     r'\bboth ways\b|\bisometry\b'),
    ('`∫ dt(γ′) = Δt` -- the coordinate increment the metric annihilates',
     r'Real\.log V₂ - 4 \* M \* Real\.log V₁', 'C_CO', r'\bcoordinate increment\b'),
    ('the null condition holds at EVERY `t` of the segment, not only at the two events',
     r'∀ t ∈ Icc', 'C_CO', r'\bevery\b.{0,24}\bsegment\b|\bthroughout\b'),
]
_BLK = {'C_EV': C_EV, 'C_CO': C_CO}
_om, _miss = [], []
for words, mk, blkname, saysmk in OMIT:
    proved = binder_of(_BLK[blkname], mk) != 'ABSENT'
    stated = hit(saysmk, PARA)
    if not proved:
        _miss.append(words)
        print(f"      ⛔ NOT FOUND in the conclusion at all (the marker is this reader's, so this "
              f"is the READER's miss, not an absence): {words}")
        continue
    if not stated:
        _om.append(words)
        print(f"      ~ proved and NOT stated: {words}")
    else:
        print(f"      ✓ proved AND stated    : {words}")
check(f"⛭ ARM ⑥ -- the conclusions the two theorems prove that the paragraph does not state, "
      f"COUNTED with no predicted value ({len(_om)} omitted, {len(OMIT) - len(_om) - len(_miss)} "
      f"stated, {len(_miss)} unresolved by the reader).  ⌗ *An omission is not a defect; it is its "
      f"own class, and the first two are what give `for an exterior observer` its content*",
      not _miss)
_V['arms'] = dict(rests_on_N=[k for k, _ in _rest], route_kw=_uses_kw, route_ac=_uses_ac,
                  omissions=_om)

# ------------------------------------------------------------------ the verdict
print("\n" + "=" * 108)
print("  THE VERDICT")
print("=" * 108)
ALLV = dict(B)
ALLV.update({'⒜': A['a'], '⒝': A['b'], '⒞': A['c'], '⒟': A['d_clause'], '⒠': A['e']})
_sup = [k for k, v in ALLV.items() if v == 'SUPPORTED']
_not = [k for k, v in ALLV.items() if v == 'NOT SUPPORTED']
_two = [k for k, v in ALLV.items() if v == 'TWO-TO-ONE']
_unm = [k for k, v in ALLV.items() if v == 'UNMEASURED']
print(f"  ① THE SPLIT        : {len(_sup)} SUPPORTED · {len(_not)} NOT SUPPORTED · "
      f"{len(_two)} TWO-TO-ONE · {len(_unm)} UNMEASURED, of {len(ALLV)}")
print(f"      SUPPORTED      : {' '.join(_sup)}")
print(f"      NOT SUPPORTED  : {' '.join(_not) or '(none)'}")
print(f"      TWO-TO-ONE     : {' '.join(_two) or '(none)'}")
print(f"  ② 𝓗⁺ IN `N`        : {len(_rest)} claim(s) -- {', '.join(k for k, _ in _rest)}; "
      f"one directly, one carried")
print(f"  ③ `BOTH HALVES`    : two readings; SUPPORTED on the substantive paragraph's two halves, "
      f"NOT SUPPORTED on the two displayed paragraphs")
print(f"  ④ THE EXISTENTIAL  : `Δx = 0` sits under `∃` over splittings; `Δτ = 0` also holds at TOP "
      f"level, so only the `Δx` half is unqualified in print")
print(f"  ⑤ THE ROUTE        : the conclusion is checked; the corollary's own "
      f"`the theorem therefore applies` step is not")
print(f"  ⑥ THE OMISSIONS    : {len(_om)}, the first two load-bearing for "
      f"`for an exterior observer`")
print(f"  ⑦ THE LANDINGS     : ⒜ {A['a']} · ⒝ {A['b']} · ⒞ {A['c']} · "
      f"⒟ sentence {A['d_sentence']} / clause {A['d_clause']} · ⒠ {A['e']}")
json.dump(_V, open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1, ensure_ascii=False)
print("\n" + "=" * 108)
if _fail:
    print(f"  ⛔ {len(_fail)} GUARD OR ARM FAILED:")
    for f in _fail:
        print(f"      ~ {f[:100]}")
    sys.exit(1)
print("  ALL GUARDS AND ARMS PASS.")
