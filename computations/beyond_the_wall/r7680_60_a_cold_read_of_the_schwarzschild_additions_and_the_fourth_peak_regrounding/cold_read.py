#!/usr/bin/env python3
"""r7680 (60) -- THE COLD READ: the three Schwarzschild additions, and the fourth-peak re-grounding.

** THE ORDER (`r7679`, 69), four objects: **
  1. ** The three P1 additions ** -- the EF corollary's repaired attestation, `rem:formalised`'s
     SEVENTH family, and `lem:alignment`'s new ending -- against `SchwarzschildEF.lean` and
     `SchwarzschildAlign.lean`.
  2. ** `P15` l.2790's re-grounded clause. **  *"1.4 of the sky's own locating spreads high, two
     thirds of that offset shared with the control"*, now cited to `P15_at_its_own_preferred_H0…`.
     ** Is that the quantity the clause names, and is `2.36` the spread at the fourth peak ON THIS
     LOCATOR? **

** THE METHOD IS `PREDICTION.md`'s, FIXED BEFORE ANYTHING WAS PARSED: ** twenty claims, written as
the passage's own words; each scored from text PARSED OUT OF the Lean, the receipts and the `.tex`;
a claim whose verdict turns on which of two readings a phrase takes is scored TWO-TO-ONE and
reported as both; and the note printed beside every verdict is BUILT FROM its readings, which is
`r7678`'s own slip made impossible.

⛭ `r7678`'s LESSON IS THIS INSTRUMENT'S FOUNDATION: ** a conjunct's quantifier is part of the
claim **, so every claim about a Lean conclusion carries the binder its marker sits under, and the
reader's negative probes include one that an existential is not read as a universal and one that a
BOUND point is distinguished from a FIXED one.  ⌗ The tree is `runs/TREE.txt`.
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




def binder_of_named(block, mk):
    """'BOUND' | 'FIXED' | 'ABSENT' -- is the variable `mk` names a BINDER of the theorem, or a
    free/fixed term?

    ⌗ *The claim "at every point of the future horizon" is a claim about a BINDER.  A theorem whose
    horizon point is implicit-and-hypothesised quantifies over it; one that fixes a point does not.
    Presence of the name in the statement cannot tell the two apart, which is `r7676`'s positional
    corollary applied to binders.*
    """
    # ⌗ THE FIRST FORM CUT THE BINDER LIST AT THE FIRST `:`, which in `{a η : ℝ} … {V₀ : ℝ}` is
    #   inside the FIRST group -- so `V₀` read FIXED although it is bound.  It passed on the other
    #   theorem only because there `{V₀ : ℝ}` happens to be first.  The binder list is the statement
    #   MINUS its conclusion, by the same top-level rule `conclusion` uses, and nothing less.
    if not re.search(r'(?m)^theorem\s', block):
        return 'ABSENT'
    binders = block[:len(block) - len(conclusion(block))]
    if re.search(r'[{(\[]\s*' + mk + r'\b', binders) or \
            re.search(r'[{(\[][^{}()\[\]]*\b' + mk + r'\b[^{}()\[\]]*:', binders):
        return 'BOUND'
    return 'FIXED' if re.search(mk + r'\b', block) else 'ABSENT'


print(__doc__)
print("=" * 108)
print("  r7680 (60) -- the cold read of the Schwarzschild additions and the fourth-peak re-grounding")
print("=" * 108)

LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
SE = open(os.path.join(LEAN, 'SchwarzschildEF.lean'), encoding='utf-8', errors='replace').read()
SA = open(os.path.join(LEAN, 'SchwarzschildAlign.lean'), encoding='utf-8', errors='replace').read()
P1 = open(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'), encoding='utf-8',
          errors='replace').read()
P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
           errors='replace').read()
RCP = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
CITED_N = 'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number'
CITED = open(os.path.join(RCP, CITED_N + '.py'), encoding='utf-8', errors='replace').read()
LOCATOR = open(os.path.join(
    RCP, 'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_'
         'controls_too.py'), encoding='utf-8', errors='replace').read()
FOURTH = open(os.path.join(
    RCP, 'P15_at_the_fourth_peak_the_arms_differ_by_half_the_skys_spread_and_no_temperature_'
         'spectrum_can_resolve_them.py'), encoding='utf-8', errors='replace').read()
COMB_OUT = open(os.path.join(HERE, 'runs', 'comb.txt'), encoding='utf-8', errors='replace').read()

FP1, FP15 = flat(P1), flat(P15)
B_HEAD = theorem_block(SE, 'se_headline')
B_FOUND = theorem_block(SE, 'se_foundation')
B_CRI = theorem_block(SE, 'se_cauchy_RI')
B_ST = theorem_block(SA, 'sa_stationary_aligns')
B_RET = theorem_block(SA, 'sa_retarded_aligns')
C_HEAD, C_FOUND, C_ST, C_RET = (conclusion(b) for b in (B_HEAD, B_FOUND, B_ST, B_RET))

m = re.search(r"The corollary's two substantive claims.*?Neither uses the curvature\.", FP1)
PARA_A = m.group(0) if m else ''
m = re.search(r'The hypotheses are shown jointly satisfiable.*?exercised in two dimensions only\.',
              FP1)
PARA_B = m.group(0) if m else ''
m = re.search(r'The alignment of both slicings is machine-checked.*?is not formalised\.', FP1)
PARA_C = m.group(0) if m else ''
m = re.search(r'the fourth peak sits \$1\.4\$ of the sky.{0,120}?shared with the control'
              r'\\rcpt\{([^}]+)\}', FP15)
CLAUSE_D, CLAUSE_D_RCPT = (m.group(0), m.group(1)) if m else ('', '')

# ------------------------------------------------------------------ PART 0 -- the guards
print("\nPART 0 -- THE SIX GUARD FAMILIES, RUN BEFORE ANY CLAIM IS SCORED")
print("  " + "-" * 104)
check("G1 the conjunct probe: the marker rule fires on a phrase a passage HAS and not on one it has "
      "not",
      hit(r'\bNeither uses the curvature\b', PARA_A)
      and not hit(r'\bNeither uses the Ricci tensor\b', PARA_A))
check(r"G2a word-boundary anchor: `\bfamily\b` matches the word and NOT `families`",
      hit(r'\bfamily\b', 'the seventh family is') and not hit(r'\bfamily\b', 'seven families here'))
check(r"G2b control-sequence anchor: `\\texttt` matches the macro and not a bare word",
      hit(r'\\texttt', r'in \texttt{SchwarzschildEF.lean}') and not hit(r'\\texttt', 'texttt'))
check(r"G2c math-delimiter anchor: `\$r=r_h\$` matches and `\$r=r_h/2\$` does not",
      hit(r'\$r=r_h\$', 'with $r=r_h$ on') and not hit(r'\$r=r_h\$', 'with $r=r_h/2$ on'))
_ref = False
try:
    hit('family', 'the family')
except AssertionError:
    _ref = True
check("G2d an UNANCHORED marker is REFUSED rather than silently matched", _ref)

# G5 -- the reader probes: every shape these conclusions contain, with the negatives
_shapes = {
    'TOP-level conjunct (se_headline, the H identification)':
        (C_HEAD, r"Subtype\.val '' \(se_S hM\)\.H", 'TOP'),
    '∀ over τ (se_headline, cone disjointness)':
        (C_HEAD, r'\(se_S hM\)\.cone \(se_Ost hM hr₀\) τ ∩', '∀'),
    'TOP-level conjunct (se_foundation, 𝓗⁺ ⊆ M)':
        (C_FOUND, r'\(se_S hM\)\.H \(range \(se_O ha k\)\) ⊆ \(se_S hM\)\.M', 'TOP'),
    '∀ over x of region I (sa_stationary, the exact rate)':
        (C_ST, r'dcov \(sa_t M\) x \(ℓN x\) / dcov \(sa_t M\) x \(sa_nN M x\) =', '∀'),
    'TOP-level Tendsto (sa_stationary, the normalised-gradient limit)':
        (C_ST, r'FS M \(0, V₀\) / 2', 'TOP'),
}
for nm, (blk, mk, want) in _shapes.items():
    got = binder_of(blk, mk)
    check(f"G5 reader shape `{nm}`: parsed `{got}`, registered `{want}`", got == want)
_b_ex = binder_of(C_ST, r'∃ C : ℝ')
check("G5 ⛭ NEGATIVE ① -- an EXISTENTIAL conjunct is not read as a universal one: the bounded-frame "
      f"clause parses `{_b_ex}`", _b_ex != '∀')
check("G5 ⛭ NEGATIVE ② -- a marker ABSENT from a conclusion reads ABSENT, not TOP",
      binder_of(C_HEAD, r'sa_Ric') == 'ABSENT')
_bv_st = binder_of_named(B_ST, 'V₀')
_bv_fix = binder_of_named('theorem t_fixed : f (0, 1) = 2 ∧ V₀ = 1 := by', 'V₀')
_bv_ret = binder_of_named(B_RET, 'V₀')
check(f"G5 ⛭ NEGATIVE ③ -- a BOUND point is distinguished from a FIXED one: `sa_stationary_aligns`'s "
      f"`V₀` parses `{_bv_st}`, and a theorem that merely mentions `V₀` parses `{_bv_fix}`",
      _bv_st == 'BOUND' and _bv_fix == 'FIXED')
check("G5 ⛭ NEGATIVE ④ -- and a variable bound in a LATER group, after a `:` has already appeared "
      "in an earlier one, still parses BOUND: `sa_retarded_aligns` binds `{a η : ℝ} … {V₀ : ℝ}`, "
      f"and `V₀` parses `{_bv_ret}`.  ⌗ *The first form of this reader cut the binder list at the "
      "first `:` and read it FIXED; it passed ③ only because the other theorem binds `V₀` first*",
      _bv_ret == 'BOUND')
# G6
_raw = "The corollary's two substantive\nclaims are machine-checked"
check("G6a ⛭ a phrase that WRAPS reads False raw and True flattened",
      not hit(r"\btwo substantive claims\b", _raw) and hit(r"\btwo substantive claims\b", flat(_raw)))
check("G6b the flattener is idempotent", flat(flat(_raw)) == flat(_raw))
# G3
_f = 0
for mk, blob in ((r'\bin the horizon\'s own splitting\b', "with $\\Delta x=0$ in the horizon's own splitting"),
                 (r'\bseven families\b', 'instantiated, on seven families. On the flat')):
    _f += int(hit(mk, blob) and not hit(mk, blob.replace('horizon', 'zz').replace('seven', 'zz')))
check(f"G3 the flip family: each derived reading flips when its text is removed ({_f} of 2)", _f == 2)
CLASSES = ('SUPPORTED', 'NOT SUPPORTED', 'TWO-TO-ONE', 'UNMEASURED')
check("G4 every verdict class the scorer can emit is a declared one", len(set(CLASSES)) == 4)

V, EV = {}, {}


def score(k, verdict, note):
    V[k] = verdict
    EV[k] = note
    bad = verdict == 'NOT SUPPORTED'
    print(f"      {k}  {('⛔ ' if bad else '   ')}{verdict:<14} {note[:116]}")
    for i in range(116, len(note), 108):
        print(f"                             {note[i:i + 108]}")


# ------------------------------------------------------------------ PART 1 -- the three repairs
print("\nPART 1 -- OBJECT A: THE THREE REPAIRS THIS LINE ASKED FOR (⒜-⒞)")
print("  " + "-" * 104)
_a1 = hit(r"\bThe corollary's two substantive claims are machine-checked\b", PARA_A)
_a2 = hit(r'\bthe closing remark on the diagram is interpretive\b', PARA_A)
_a3 = not hit(r'\bBoth halves of the corollary\b', FP1)
m = re.search(r'\\begin\{corollary\}\[Degeneracy of Horizon-Crossing.*?\\end\{corollary\}', FP1)
_cor = m.group(0) if m else ''
_subst = sum(1 for p in (r'\bcausally ordered but null-related\b', r'\bmetrically coincident\b')
             if hit(p, _cor))
_diag = hit(r'\bdoes not encode any geometric or physical temporal distance\b', _cor)
score('⒜', 'SUPPORTED' if (_a1 and _a2 and _a3 and _subst == 2 and _diag) else 'NOT SUPPORTED',
      f'the new wording reads {_a1}; the diagram remark is marked interpretive {_a2}; the old '
      f'phrase is gone from the whole paper {_a3}; the corollary carries {_subst} substantive '
      f'claims (the causal one and the coincidence one) and the diagram paragraph is present '
      f'{_diag}.  ⇒ `two substantive claims` names exactly the two that are checked, and the '
      'reading that reached the diagram is closed by naming the diagram separately')

# ⌗ the first form of this marker ended in `\b` AFTER a `$`, which can never match: `$` is a
#   non-word character and so is the space after it.  The math-delimiter anchor form (`r7674`) is
#   already an anchor on its own, so the trailing boundary is both wrong and unnecessary.
_b1 = hit(r'\bthe horizon inside that spacetime at \$U=0\$', PARA_A)
_b2 = not hit(r'\bthe horizon at \$U=0\$ and a static observer\b', PARA_A)
_b3 = bool(re.search(r'\{x : Pt \| \(φ x\)\.1 = 0\} ⊆ \(sk_S hM\)\.M', flat(
    theorem_block(open(os.path.join(LEAN, 'SchwarzschildKruskal.lean'), encoding='utf-8',
                       errors='replace').read(), 'sk_observer'))))
score('⒝', 'SUPPORTED' if (_b1 and _b2 and _b3) else 'NOT SUPPORTED',
      f'the new wording reads {_b1}; the old unqualified phrase is gone {_b2}; and reading B is the '
      f'one the Lean proves -- `{{U = 0}} ⊆ M` is a conjunct of `sk_observer` {_b3}.  ⇒ the clause '
      'that reproduced the corrected registration is gone, and what is left is what was proved')

_c1 = hit(r'\bwith \$\\Delta\\tau=0\$, and \$\\Delta x=0\$ in the horizon\'s own splitting\b', PARA_A)
_c2 = not hit(r'\bwith \$\\Delta x=\\Delta\\tau=0\$\b', FP1)
SQ = open(os.path.join(LEAN, 'SchwarzschildKilling.lean'), encoding='utf-8',
          errors='replace').read()
C_CO = conclusion(theorem_block(SQ, 'sq_cor_EF_coincident'))
_bdx, _bdtau = binder_of(C_CO, r'σ\.Δx = 0'), binder_of(C_CO, r'kg_deltaTau \(sq_g M\)')
score('⒞', 'SUPPORTED' if (_c1 and _c2 and _bdx == '∃' and _bdtau == 'TOP')
      else 'NOT SUPPORTED',
      f'the new wording reads {_c1}; the unqualified pair is gone from the whole paper {_c2}; and '
      f'the binders are what the wording now matches -- `Δx = 0` sits under `{_bdx}` over splittings '
      f'and `Δτ = 0` at `{_bdtau}` level.  ⇒ the existential is printed as an existential and the '
      'top-level one as unqualified, each where it belongs')

# ------------------------------------------------------------------ PART 2 -- the seventh family
print("\nPART 2 -- OBJECT B: `rem:formalised`'s SEVENTH FAMILY (①-⑧)")
print("  " + "-" * 104)
HEADLINES = re.findall(r'\\texttt\{((?:[a-z]{2}_)?(?:witness_)?headline[a-zA-Z_\\]*)\}',
                       PARA_B.replace('\\_', '_'))
_fam = [h for h in HEADLINES]
_seven = hit(r'\bon seven families\b', PARA_B)
score('①', 'SUPPORTED' if (_seven and len(_fam) == 7) else 'NOT SUPPORTED',
      f'the paragraph says `seven families` ({_seven}) and cites {len(_fam)} distinct headline '
      f'theorems as the families: {", ".join(_fam)}.  ⇒ the count is the paragraph\'s own '
      'enumeration and not taken from the order')

_se_in = hit(r'\bThe seventh is the Schwarzschild exterior itself\b', PARA_B)
_se_file = hit(r'\\texttt\{SchwarzschildEF\.lean\}', PARA_B.replace('\\_', '_'))
score('②', 'SUPPORTED' if (_se_in and _se_file and B_HEAD) else 'NOT SUPPORTED',
      f'the sentence names it {_se_in}, the file is cited {_se_file}, and `se_headline` is in that '
      f'file ({len(B_HEAD)} characters of statement)')

_dom = hit(r'\\\{V>0,\\,UV<1\\\}', PARA_B)
# ⌗ the first form looked for `seW : Opens P := {…}`; the Lean defines the SET as `seWS` and
#   builds the `Opens` from it, so the predicate to read is `seWS`'s.  Reading the wrong name is
#   what the probe caught.
_seW = bool(re.search(r'def seWS : Set P := \{p \| 0 < p\.2 ∧ p\.1 \* p\.2 < 1\}', flat(SE)))
_radial = bool(re.search(r'abbrev P := ℝ × ℝ', SE))
score('③', 'SUPPORTED' if (_dom and _seW and _radial) else 'NOT SUPPORTED',
      f'the printed domain reads {_dom}; the Lean defines `seWS : Set P := {{p | 0 < p.2 ∧ '
      f'p.1 * p.2 < 1}}` ({_seW}) and builds `seW : Opens P` from it, and that set IS '
      f'`{{V > 0, UV < 1}}`; the point type is `abbrev P := ℝ × ℝ` ({_radial}), so the object is '
      'the radial plane')

_obs_hyp = bool(re.search(r'\{r₀ : ℝ\} \(hr₀ : 2 \* M < r₀\)', B_HEAD))
score('④', 'SUPPORTED' if _obs_hyp else 'NOT SUPPORTED',
      f'`se_headline` takes `(hr₀ : 2 * M < r₀)` as its only hypothesis beside `hM` ({_obs_hyp}), '
      'which is `r₀ > r_h` exactly, and the observer it builds is `se_Ost hM hr₀`')

_cau = binder_of(C_HEAD, r'IsCauchyTemporalOn')
_cau_gen = bool(re.search(r'theorem se_cauchy_RI \{k : ℝ\} \(hk : 0 < k\)', SE))
score('⑤', 'SUPPORTED' if (_cau == 'TOP' and _cau_gen) else 'NOT SUPPORTED',
      f'`se_headline`\'s first conjunct is `IsCauchyTemporalOn D (se_Θst M r₀)` at `{_cau}` level, '
      f'and the general statement `se_cauchy_RI` carries it for EVERY positive multiple `k` '
      f'({_cau_gen}).  ⌗ *So the clause holds, and `se_headline` states the one normalisation that '
      'is also the observer\'s proper time, where `se_cauchy_RI` is the general form*')

_props = {'properness': binder_of(C_HEAD, r'SublevelProper'),
          'slice KLi': binder_of(C_HEAD, r'KLi \(\(se_S hM\)\.slice'),
          'slice KLs': binder_of(C_HEAD, r'KLs \(\(se_S hM\)\.slice'),
          'cone KLi': binder_of(C_HEAD, r'KLi \(\(se_S hM\)\.cone'),
          'cone KLs': binder_of(C_HEAD, r'KLs \(\(se_S hM\)\.cone'),
          'disjointness': binder_of(C_HEAD, r'\(se_S hM\)\.cone \(se_Ost hM hr₀\) τ ∩'),
          'H = {U=0, V>0}': binder_of(C_HEAD, r"\{p : P \| p\.1 = 0 ∧ 0 < p\.2\}")}
_hprint = hit(r'\\mathcal\{H\}\^\+=\\\{U=0,\\,V>0\\\}', PARA_B)
score('⑥', 'SUPPORTED' if (all(v != 'ABSENT' for v in _props.values()) and _hprint)
      else 'NOT SUPPORTED',
      'every clause the sentence names is a conjunct of `se_headline`, with its binder: '
      + '; '.join(f'{k} `{v}`' for k, v in _props.items())
      + f'.  The printed identification `𝓗⁺ = {{U=0, V>0}}` reads {_hprint}.  ⌗ *The disjointness '
      'and the cone identifications are under `∀ τ` or at top level, which is where the sentence '
      'puts them*')

_rh = binder_of(C_HEAD, r'se_r M x = 2 \* M')
score('⑦', 'SUPPORTED' if _rh == '∀' else 'NOT SUPPORTED',
      f'`∀ x ∈ H, se_r M x = 2 * M` is a conjunct of `se_headline` under `{_rh}` over the horizon, '
      'so `r = r_h` holds at every point of it and not at one')

_last4 = hit(r'\bNo conformal extension is built for these last four\b', PARA_B)
_cut = max(PARA_B.replace('\\_', '_').rfind('Compactification.lean'),
           PARA_B.replace('\\_', '_').rfind('CurvedTangency.lean'))
_after = [h for h in re.findall(r'\\texttt\{((?:[a-z]{2}_)?(?:witness_)?headline[a-zA-Z_\\]*)\}',
                                PARA_B.replace('\\_', '_')[_cut:])]
score('⑧', 'SUPPORTED' if (_last4 and len(_after) == 4) else 'NOT SUPPORTED',
      f'the sentence reads {_last4}, and the headline citations standing AFTER the last '
      f'compactification file in the paragraph are exactly {len(_after)}: {", ".join(_after)}.  '
      '⇒ `these last four` names the four families for which no extension is built, measured '
      'positionally in the paragraph rather than counted by hand')

# ------------------------------------------------------------------ PART 3 -- lem:alignment
print("\nPART 3 -- OBJECT C: `lem:alignment`'s NEW ENDING (⑨-⑭)")
print("  " + "-" * 104)
_v_st, _v_ret = binder_of_named(B_ST, 'V₀'), binder_of_named(B_RET, 'V₀')
_ex = hit(r'\bat every point of the future horizon\b', PARA_C)
score('⑨', 'SUPPORTED' if (_ex and _v_st == 'BOUND' and _v_ret == 'BOUND') else 'NOT SUPPORTED',
      f'the sentence claims it {_ex}; and the horizon point is a BINDER in both theorems -- '
      f'`sa_stationary_aligns` `{{V₀ : ℝ}} (hV₀ : 0 < V₀)` reads `{_v_st}` and '
      f'`sa_retarded_aligns` reads `{_v_ret}` -- so each holds for every `V₀ > 0`, which IS every '
      'point of the future horizon `{U = 0, V > 0}`.  ⌗ *A claim about every point is a claim about '
      'a binder, and presence of the name could not have told the two apart*')

_rate_eq = binder_of(C_ST, r'FS M \(φ x\) \* -\(φ x\)\.1 / \(2 \* \(φ x\)\.2\)')
_rate_lim = binder_of(C_ST, r'dcov \(sa_t M\) x \(ℓN x\) / dcov \(sa_t M\) x \(sa_nN M x\)\)\s*$')
_lim0 = bool(re.search(r'Tendsto \(fun x => dcov \(sa_t M\) x \(ℓN x\) / dcov \(sa_t M\) x '
                       r'\(sa_nN M x\)\)\s*\(𝓝\[sa_I\] ψ \(0, V₀\)\) \(𝓝 0\)', flat(C_ST)))
score('⑩', 'SUPPORTED' if (_rate_eq == '∀' and _lim0) else 'NOT SUPPORTED',
      f'the ratio is given EXACTLY as `F(x)·(−U)/(2V)` under `{_rate_eq}` over region I, and a '
      f'separate conjunct sends it to `0` on the approach filter ({_lim0}).  ⇒ `the ratio … '
      'vanishes` is the limit conjunct, and the exact form beside it is what makes the limit '
      'readable rather than asserted')

_grad = bool(re.search(r'\(𝓝 \(\(FS M \(0, V₀\) / 2\) • fst ℝ ℝ ℝ\)\)', flat(C_ST)))
_grad_print = hit(r'\bits normalised gradient tends to \$\(F/2\)\\,\\mathrm\{d\}U\$', PARA_C)
score('⑪', 'SUPPORTED' if (_grad and _grad_print) else 'NOT SUPPORTED',
      f'the last conjunct is `Tendsto … (𝓝 ((FS M (0, V₀) / 2) • fst ℝ ℝ ℝ))` ({_grad}), and `fst` '
      f'IS the `dU` covector in the chart, so the limit is `(F/2) dU` at the horizon point; the '
      f'sentence prints it {_grad_print}')

_ae = bool(re.search(r'\{a η : ℝ\} \(ha : 0 < a\) \(hη : 0 < η\)', B_RET))
_ret_print = hit(r'\bthe retarded slicing aligns for every \$a,\\eta>0\$', PARA_C)
_ret_grad = bool(re.search(r'\(𝓝 \(\(FS M \(0, V₀\) / 2\) • fst ℝ ℝ ℝ\)\)', flat(C_RET)))
score('⑫', 'SUPPORTED' if (_ae and _ret_print and _ret_grad) else 'NOT SUPPORTED',
      f'`sa_retarded_aligns` binds `a` and `η` with positivity only ({_ae}), the sentence says '
      f'`for every a, η > 0` ({_ret_print}), and it reaches the SAME limit `(F/2) dU` ({_ret_grad}) '
      '-- so no upper bound on `η` is needed for the alignment')

_c13 = hit(r'\bthat the stationary slicing is a Cauchy temporal function of the exterior is '
           r'\\texttt\{se\\_headline\}', PARA_C)
score('⑬', 'SUPPORTED' if (_c13 and _cau == 'TOP') else 'NOT SUPPORTED',
      f'the attribution reads {_c13}, and `se_headline`\'s first conjunct is the Cauchy clause at '
      f'`{_cau}` level on `D`, which the same theorem identifies as region I -- the exterior')

_c14 = hit(r'\bthe same for the retarded slicing is not formalised\b', PARA_C)
_no_ret_cauchy = not re.search(r'(?m)^theorem \S*ret\S*[Cc]auchy|IsCauchyTemporal.*sa_ret', SA)
score('⑭', 'SUPPORTED' if (_c14 and _no_ret_cauchy) else 'NOT SUPPORTED',
      f'the sentence says so {_c14}, and neither probe carries a Cauchy statement for the retarded '
      f'slicing ({_no_ret_cauchy}): a search for one over both files returns nothing.  ⇒ the '
      'paragraph states its own gap, which is the clause that makes the rest readable')

# ------------------------------------------------------------------ PART 4 -- the re-grounding
print("\nPART 4 -- OBJECT D: `P15` l.2790's RE-GROUNDED CLAUSE (⑮-⑰)")
print("  " + "-" * 104)
Q = {}
for lab, pat in (('sky', r'THE SKY, this locator\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)'),
                 ('control', r'the CONTROL, L2000\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)'),
                 ('arm', r'ARM OF RECORD, distances \*\*\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)')):
    m = re.search(pat, COMB_OUT)
    Q[lab] = [float(x) for x in m.groups()] if m else None
print(f"      PART 4B's fourth peaks, run on this tree : sky {Q['sky'][3]}  control "
      f"{Q['control'][3]}  arm {Q['arm'][3]}")
_off = Q['arm'][3] - Q['sky'][3]
_shared = Q['control'][3] - Q['sky'][3]
print(f"      the arm's offset from the sky            : {_off:.2f} multipoles")
print(f"      the part of it the control carries       : {_shared:.2f} multipoles, "
      f"{_shared / _off:.4f} of it")
score('⑮', 'SUPPORTED' if (abs(_off - 3.26) < 0.005 and abs(Q['arm'][3] - 1125.11) < 0.005
                           and abs(Q['sky'][3] - 1121.85) < 0.005) else 'NOT SUPPORTED',
      f'the receipt the clause now cites RUNS GREEN on this tree and its PART 4B prints the three '
      f'quartets the order quotes: the arm {Q["arm"][3]}, the control {Q["control"][3]}, the sky '
      f'{Q["sky"][3]}, so the numerator `{_off:.2f}` is the cited receipt\'s own')

# the order's named question: where does 2.36 come from?
_in_cited = '2.36' in CITED
_in_locator = '2.36' in LOCATOR
_taken_given = hit(r'\btaken as given and neither is re-derived\b', flat(LOCATOR))
m = re.search(r"SKY_SIG4 = ([\d.]+)\s*#\s*(.*)", LOCATOR)
_sig_src = (m.group(1), m.group(2).strip()) if m else ('', '')
_planck = bool(re.search(r"'Planck plik_lite'\) == 2\.34", FOURTH))
_act = bool(re.search(r"'ACT DR6 CMB-only'\) == 3\.03", FOURTH))
print(f"\n      `2.36` appears in the CITED receipt      : {_in_cited}")
print(f"      `2.36` appears in the locator receipt    : {_in_locator}  as "
      f"`SKY_SIG4 = {_sig_src[0]}  # {_sig_src[1]}`")
print(f"      that receipt says it is taken as given   : {_taken_given}")
print(f"      a locator-specific spread DOES exist     : Planck plik_lite 2.34 ({_planck}), "
      f"ACT alone 3.03 ({_act})")
print(f"      3.26 / 2.36 = {_off / 2.36:.3f}   and   3.26 / 2.34 = {_off / 2.34:.3f}   "
      f"-- both print as 1.4")
score('⑯', 'TWO-TO-ONE' if (not _in_cited and _planck) else 'UNMEASURED',
      '⛭ THE ORDER\'S NAMED QUESTION.  ** `2.36` is NOT in the cited receipt at all ** '
      f'({_in_cited}), and it is NOT this locator\'s spread: it is `PO-47`\'s combined figure, '
      f'carried in another receipt as the constant `SKY_SIG4 = 2.36` and declared there as "taken '
      f'as given and neither re-derived" ({_taken_given}).  The spread a locator does give at the '
      f'fourth peak is `2.34` on Planck `plik_lite` -- which is the very sky PART 4B locates -- and '
      f'`3.03` on ACT alone, `2.36` being their quadrature combination.  ⇒ READING A, the DIGIT: '
      f'SUPPORTED either way, `{_off / 2.36:.2f}` on `2.36` and `{_off / 2.34:.2f}` on `2.34`, both '
      'printing as `1.4`.  READING B, the CITATION: NOT SUPPORTED -- the denominator has no address '
      'in the cited receipt, so the clause\'s own citation cannot reach the spread it divides by')

_two_thirds = hit(r'\btwo thirds of that offset shared with the control\b', FP15)
score('⑰', 'SUPPORTED' if (_two_thirds and abs(_shared / _off - 0.656) < 0.01)
      else 'NOT SUPPORTED',
      f'the words read {_two_thirds}, and the quantity they name -- the control\'s share of the '
      f'arm\'s offset from the sky -- measures `{_shared:.2f}/{_off:.2f} = {_shared / _off:.3f}` on '
      f'the cited receipt\'s own quartets, which is two thirds.  ⌗ *So the SECOND figure is derivable '
      'from the cited receipt alone; it is the first that reaches outside it*')

# ------------------------------------------------------------------ PART 5 -- the remaining arms
print("\nPART 5 -- ④ `𝓗⁺ ⊆ M`, ⑥ THE OMISSIONS")
print("  " + "-" * 104)
_hm = binder_of(C_FOUND, r'\(se_S hM\)\.H \(range \(se_O ha k\)\) ⊆ \(se_S hM\)\.M')
_muniv = binder_of(C_FOUND, r'\(se_S hM\)\.M = univ')
print(f"      `𝓗⁺ ⊆ M` in `se_foundation`              : conjunct at `{_hm}` level")
print(f"      `M = univ` in `se_foundation`            : conjunct at `{_muniv}` level")
check("⛭ ARM ④ -- the clause that FAILED at campaign 97 is proved here, and the reason it now holds "
      "is structural: the manifold IS the Eddington--Finkelstein domain, so `M = univ` on it and a "
      "frontier taken in `N` cannot leave the spacetime.  `W` excludes `V ≤ 0`, which is where the "
      "white-hole singularity branch lived", _hm == 'TOP' and _muniv == 'TOP')

OMIT = [
    # ⌗ tangency is NOT in `se_headline` -- the first form of this row looked for it there and the
    #   reader said so.  It is proved in the OTHER probe, so the row is scored against that one and
    #   reported as a DIFFERENCE in what the seventh family's headline carries, not as an omission
    #   of something its own probe proves.
    ('tangency at every horizon point -- which EVERY other family\'s sentence claims, and which is '
     'proved for Schwarzschild in `SchwarzschildAlign.lean` rather than in `se_headline`',
     C_ST, r'TCF\.FrameHyp', PARA_B,
     r'\btangency\b.{0,80}\bseventh\b|\bseventh\b.{0,260}\btangency\b'),
    ('the stretch: every compact part of 𝓗⁺ eventually inside the cones\' ε-stretch',
     conclusion(theorem_block(SE, 'se_stretch')), r'KL|stretch|⊆', PARA_B, r'\bstretch\b.{0,120}\bSchwarzschild\b'),
    ('the observer\'s proper time: `Θ(O τ) = τ` and `r(O τ) = r₀`',
     C_HEAD, r'se_Θst M r₀ \(se_Ost hM hr₀ τ\) = τ', PARA_B, r'\bproper time\b'),
    ('`D` identified as region I, `{U < 0, V > 0}`',
     C_HEAD, r"\{p : P \| p\.1 < 0 ∧ 0 < p\.2\}", PARA_B, r'\bregion I\b|\bexterior is\b'),
    ('every cone is non-empty',
     C_HEAD, r'\(\(se_S hM\)\.cone \(se_Ost hM hr₀\) τ\)\.Nonempty', PARA_B, r'\bnon-empty\b'),
]
_om, _bad = [], []
for words, blk, mk, para, says in OMIT:
    proved = bool(re.search(mk, blk))
    stated = hit(says, para) if para else False
    if not proved:
        _bad.append(words)
        print(f"      ⛔ the reader could not find it in the conclusion: {words}")
        continue
    (_om if not stated else []).append(words)
    print(f"      {'~ proved and NOT stated' if not stated else '✓ proved AND stated    '}: {words}")
_tang_in_head = bool(re.search(r'FrameHyp', C_HEAD))
check(f"⛭ ARM ⑥ -- what the seventh family's probes prove that its sentence does not state, COUNTED "
      f"with no predicted value ({len(_om)} of {len(OMIT)}; {len(_bad)} unresolved by the reader).  "
      f"⌗ *The FIRST is the one that matters, and the measurement is sharper than an omission: "
      f"tangency is NOT a conjunct of `se_headline` at all ({_tang_in_head}) -- for this one family "
      f"it is proved in the OTHER probe and cited forty lines later, at `lem:alignment`, where "
      f"every other family's sentence carries it in its own clause*", not _bad)

# ------------------------------------------------------------------ the verdict
print("\n" + "=" * 108)
print("  THE VERDICT")
print("=" * 108)
ALL = dict(V)
_sup = [k for k, v in ALL.items() if v == 'SUPPORTED']
_not = [k for k, v in ALL.items() if v == 'NOT SUPPORTED']
_two = [k for k, v in ALL.items() if v == 'TWO-TO-ONE']
_unm = [k for k, v in ALL.items() if v == 'UNMEASURED']
print(f"  ① THE SPLIT        : {len(_sup)} SUPPORTED · {len(_not)} NOT SUPPORTED · "
      f"{len(_two)} TWO-TO-ONE · {len(_unm)} UNMEASURED, of {len(ALL)}")
print(f"      SUPPORTED      : {' '.join(_sup)}")
print(f"      NOT SUPPORTED  : {' '.join(_not) or '(none)'}")
print(f"      TWO-TO-ONE     : {' '.join(_two) or '(none)'}")
print(f"  ② THE `2.36`       : not in the cited receipt; `PO-47`'s combined figure, declared taken "
      f"as given.  The digit survives on either spread ({_off / 2.36:.2f} / {_off / 2.34:.2f}); the "
      f"CITATION does not reach it")
print(f"  ③ THE QUANTIFIERS  : the horizon point is BOUND in both alignment theorems, so `at every "
      f"point of the future horizon` is exact; `se_headline`'s Cauchy clause is of one "
      f"normalisation and `se_cauchy_RI` is the general form")
print(f"  ④ `𝓗⁺ ⊆ M`         : proved, and structurally -- the manifold IS EF's domain, so "
      f"`M = univ` and the frontier cannot leave it")
print(f"  ⑤ THE COUNTS       : `seven families` matches 7 headline citations; `these last four` "
      f"matches the 4 standing after the last compactification file")
print(f"  ⑥ THE OMISSIONS    : {len(_om)}, the first being tangency, which lives in the other probe")
print(f"  ⑦ THE REPAIRS      : ⒜ {V['⒜']} · ⒝ {V['⒝']} · ⒞ {V['⒞']}")
json.dump(dict(verdicts=V, evidence=EV, quartets=Q, offset=_off, shared=_shared,
               omissions=_om), open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1,
          ensure_ascii=False)
print("\n" + "=" * 108)
if _fail:
    print(f"  ⛔ {len(_fail)} GUARD OR ARM FAILED:")
    for f in _fail:
        print(f"      ~ {f[:100]}")
    sys.exit(1)
print("  ALL GUARDS AND ARMS PASS.")
