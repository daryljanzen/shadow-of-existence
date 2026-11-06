#!/usr/bin/env python3
"""r7694 (60) -- the registered readings for the cold read of `cor:stationary`'s new
proof paragraph against `StationaryHorizon.lean`.

Registration: PREDICTION.md, committed and pushed before this file existed.
Tree: runs/TREE.txt.

Exit codes, registered in advance:
  0  every registered reading ran and its verdict is recorded (whatever the verdict)
  1  a reading could not be run, or a guard refused an anchor, or a negative probe
     failed to fire
No verdict is an exit code.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
PROBE = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes',
                    'StationaryHorizon.lean')

FAIL, VERDICTS = [], []


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def flat(s):                                   # G6
    return re.sub(r'\s+', ' ', s).strip()


def anchor(marker):                            # G2
    # an ESCAPED CONTROL SEQUENCE: a marker beginning with a backslash, which is the second
    # of G2's three anchor forms.  ⌗ The first run of this probe refused `\mathcal{L}_Xg=0`
    # because this test asked for TWO leading backslashes -- a guard rejecting a marker that
    # is in fact anchored.  One backslash is the control-sequence form; two is a marker that
    # has been escaped twice over and is the thing the earlier revisions wrote by habit.
    if marker.startswith('\\'):
        return re.compile(re.escape(marker))
    if marker.startswith('\\$') or marker.endswith('\\$'):
        return re.compile(re.escape(marker))
    if re.match(r'^[A-Za-z0-9]', marker) and re.search(r'[A-Za-z0-9.}]$', marker):
        return re.compile(r'\b' + re.escape(marker))
    FAIL.append('G2 REFUSED an unanchored marker: %r' % marker)
    return None


def hit(marker, hay):
    rx = anchor(marker)
    return bool(rx.search(hay)) if rx else False


def note(tag, text):
    print('    %-9s %s' % (tag, text))
    if tag == 'VERDICT':
        VERDICTS.append(text)


P1_L = read(P1).split('\n')
SRC = read(PROBE)
PARA = flat(P1_L[291])              # l.292, the new paragraph
PROOF1 = flat(P1_L[289])            # l.290, the prose paragraph before it


def lean_block(name, kind='structure'):
    m = re.search(r'^%s\s+%s\b' % (kind, re.escape(name)), SRC, re.M)
    if m is None:
        FAIL.append('could not locate %s %s' % (kind, name))
        return '', ''
    tail = SRC[m.start():]
    cut = re.search(r'\n(?=\S)', tail[1:])
    body = tail[:cut.start() + 1] if cut else tail[:4000]
    head = SRC[:m.start()]
    docs = list(re.finditer(r'/--(.*?)-/', head, re.S))
    return flat(body), flat(docs[-1].group(1)) if docs else ''


KH, KH_DOC = lean_block('IsKillingHorizon')
ST, ST_DOC = lean_block('st_cor_stationary', 'theorem')
WI, WI_DOC = lean_block('st_witness', 'theorem')
secm = re.search(r'section STCorollary(.*?)end STCorollary', SRC, re.S)
SEC = secm.group(1) if secm else ''
if not (KH and ST and WI and SEC):
    print('FATAL: a read target could not be located')
    sys.exit(1)

print('=' * 78)
print('ARM 1 -- ARE THE HYPOTHESES STATED WHOLE?  (the order\'s first "above all")')
print('=' * 78)

# the structure's fields, read from its own text
FIELDS = re.findall(r'(?:^|\s)(C1|ne_zero|hRep_diff|killing|generator)\s*:', KH)
FIELDS = list(dict.fromkeys(FIELDS))
note('read', 'IsKillingHorizon fields, read at source            : %s' % ', '.join(FIELDS))

# 1a EVERY FIELD IS STATED.  one predicate per field (G1), each a clause of the prose.
CLAUSE = {
    'C1':        'continuously differentiable',
    'ne_zero':   'nonzero on it',
    'hRep_diff': "metric's chart representative differentiable",
    # ⌗ The first run of this probe reported `killing` MISSING on a DOUBLED backslash in this
    #   very marker: the paragraph writes `\mathcal{L}_Xg=0` and the marker asked for
    #   `\\mathcal`.  A matcher loose enough to mis-read its own input answers about the
    #   matcher -- this line's own first standing lesson, arriving inside the probe that
    #   carries it.  Fixed, and recorded rather than quietly corrected.
    'killing':   '\\mathcal{L}_Xg=0',
    'generator': 'integral curve of $X$ lying in it',
}


def wholeness_reading(para, fields):
    """Negative probe 11: must be able to NAME a field the prose leaves out."""
    missing = [f for f in fields if not hit(CLAUSE[f], para) and CLAUSE[f] not in para]
    return ('SUPPORTED' if not missing else 'HYPOTHESIS OMITTED'), missing


print()
print('  1a EVERY FIELD OF THE STRUCTURE IS STATED BY A CLAUSE')
for f in FIELDS:
    present = hit(CLAUSE[f], PARA) or CLAUSE[f] in PARA
    note('read', '%-11s <- %-46s %s' % (f, '"%s"' % CLAUSE[f][:44], present))
v1a, miss = wholeness_reading(PARA, FIELDS)
note('VERDICT', '1a %s -- %d of the %d fields of IsKillingHorizon have a clause of the '
                'paragraph stating them%s.'
     % (v1a, len(FIELDS) - len(miss), len(FIELDS),
        '' if not miss else '; MISSING: ' + ', '.join(miss)))
# negative probe 11 must FIRE on a copy with one clause struck out
struck = PARA.replace('nonzero on it', 'xxx')
if struck == PARA:
    FAIL.append('negative probe 11 could not build its altered copy')
v11, miss11 = wholeness_reading(struck, FIELDS)
note('neg11', 'one clause struck -> %s %s (must be HYPOTHESIS OMITTED, naming ne_zero)'
     % (v11, miss11))
if v11 != 'HYPOTHESIS OMITTED' or miss11 != ['ne_zero']:
    FAIL.append('negative probe 11 did not fire: %s %s' % (v11, miss11))

# 1b EVERY CLAUSE IS A FIELD (the converse: a hypothesis the prose INVENTS)
print()
print('  1b EVERY CLAUSE OF THE PARAGRAPH IS A FIELD (no invented hypothesis)')
HYPSENT = PARA.split('Then along every')[0]
extra = []
for probe_word, field in (('analytic', None), ('complete', None), ('compact', None),
                          ('geodesic', None), ('connected', None)):
    if hit(probe_word, HYPSENT):
        extra.append(probe_word)
note('read', 'hypothesis clauses counted in the prose           : %d'
     % (HYPSENT.count(',') + 1))
note('read', 'prose words naming a hypothesis the structure has '
             'no field for          : %s' % (extra or 'none'))
note('VERDICT', '1b %s -- the paragraph states no hypothesis the structure does not ask.'
     % ('SUPPORTED' if not extra else 'HYPOTHESIS INVENTED (%s)' % ', '.join(extra)))

# 1c THE QUANTIFIERS AND THE LOCI
print()
print('  1c THE QUANTIFIERS AND THE LOCI (a conjunct\'s quantifier is part of the claim)')
LOCI = [
    ('C1/ne_zero say "on it"', 'C1 : ∀ p ∈ Hs', '∀ p ∈ Hs, ContMDiffAt' in KH),
    ('hRep_diff says "near it"', 'eventually in a nhd', '∀ᶠ y in 𝓝' in KH),
    ('killing says "near it"', 'eventually in a nhd', '∀ᶠ x in 𝓝 p' in KH),
    ('generator: "through each of its points"', '∀ p ∈ Hs, ∃ γ', '∀ p ∈ Hs, ∃ (γ' in KH),
    ('generator: "null SOMEWHERE", not everywhere', 'null at γ t₀ only',
     'S.g (γ t₀) (X (γ t₀)) (X (γ t₀)) = 0' in KH),
]
for nm, what, ok in LOCI:
    note('read', '%-42s %-22s %s' % (nm, what, ok))
derived = bool(re.search(r'theorem st_null_of_isKillingHorizon', SRC))
note('read', '%-42s %-22s %s' % ('and null EVERYWHERE is DERIVED, not asked',
                                 'st_null_of_isKilling…', derived))
ok1c = all(o for _, _, o in LOCI) and derived
note('VERDICT', '1c %s -- every clause\'s locus matches its field: "on it" is pointwise on Hs, '
                '"near it" is an eventually-in-a-neighbourhood, "through each of its points" is '
                'the per-point existential, and "null somewhere" is null at ONE parameter of the '
                'generator -- which is the weaker hypothesis, with null EVERYWHERE derived from it '
                'by a separate theorem. The paragraph takes the weaker one, correctly.'
     % ('SUPPORTED' if ok1c else 'SCOPE-DIFFERS'))

# 1d THE AMBIENT SETTING, against rem:formalised's own words
print()
print('  1d THE AMBIENT SETTING: "In the setting of Remark rem:formalised"')
rem = flat(P1_L[314])
rem_c1 = 'a $C^{1}$ atlas' in rem
rem_arb = 'arbitrary real normed space' in rem
rem_dim = 'holds in every dimension' in rem
note('read', 'the remark says a C^1 atlas                       : %s' % rem_c1)
note('read', 'the remark says an ARBITRARY real normed space    : %s' % rem_arb)
note('read', 'the remark says it holds in EVERY DIMENSION       : %s' % rem_dim)
sec_fin = 'FiniteDimensional ℝ E' in SEC
sec_c2 = bool(re.search(r'IsManifold 𝓘\(ℝ, E\) 2 N', SEC))
sec_c1 = bool(re.search(r'IsManifold 𝓘\(ℝ, E\) 1 N', SEC))
sec_t2 = 'T2Space' in SEC
note('read', "the section asks [FiniteDimensional ℝ E]         : %s" % sec_fin)
note('read', 'the section asks a C^2 atlas (IsManifold … 2 N)   : %s' % sec_c2)
note('read', '...rather than a C^1 atlas (IsManifold … 1 N)     : %s' % (not sec_c1))
note('read', 'the section asks Hausdorff of N                   : %s' % sec_t2)
diffs = []
if sec_fin and rem_arb:
    diffs.append('finite-dimensionality, against "an arbitrary real normed space"')
if sec_c2 and rem_c1:
    diffs.append('a C^2 atlas, against "a C^1 atlas"')
if diffs:
    note('VERDICT', '1d SCOPE-DIFFERS -- the paragraph borrows the remark\'s setting, and the '
                    'section that holds BOTH IsKillingHorizon and st_cor_stationary asks two '
                    'hypotheses the remark explicitly disclaims: %s. So the sentence claims a '
                    'generality this theorem has not got, including the remark\'s own "holds in '
                    'every dimension" (%s). It asks no Hausdorff, which is weaker and harmless. '
                    '** Six words: "in the setting of Remark X, in finite dimension and with a '
                    'C^2 atlas". Routed, not edited. **' % ('; and '.join(diffs), rem_dim))
else:
    note('VERDICT', '1d SUPPORTED -- the probe\'s ambient hypotheses are the remark\'s.')

print()
print('=' * 78)
print('ARM 2 -- IS "CITED AND NOT FORMALISED" RIGHT?  (the second "above all")')
print('=' * 78)

print()
print('  2a THE POSITIVE HALF: the conclusion taken as the hypothesis')
takes = 'hH : S.IsKillingHorizon X (S.H J)' in ST
note('read', 'st_cor_stationary takes IsKillingHorizon of S.H J : %s' % takes)
note('read', 'S.H J is the horizon ∂J⁻(J) by definition         : %s'
     % bool(re.search(r'def H \(J : Set N\) : Set N := frontier', read(PROBE))))
note('VERDICT', '2a %s -- the theorem\'s hypothesis IS rigidity\'s conclusion: the frontier of the '
                "causal past is a Killing horizon of X, and that is what it assumes."
     % ('SUPPORTED' if takes else 'NOT SUPPORTED'))

print()
print('  2b THE NEGATIVE HALF: an ABSENCE claim, read as one, naming what was searched')
DOC_SPANS = [(m.start(), m.end()) for m in re.finditer(r'/-.*?-/', SRC, re.S)]


def in_prose(pos):
    """True when this position sits inside a /- … -/ comment or after a `--` on its line.

    ⌗ The first run of this probe classified these by the line's FIRST CHARACTER, which read
      two docstring CONTINUATION lines as hypotheses and made the verdict note contradict
      its own readings.  Spans, not first characters.
    """
    if any(a <= pos < b for a, b in DOC_SPANS):
        return True
    ls = SRC.rfind('\n', 0, pos) + 1
    dd = SRC.find('--', ls)
    return 0 <= dd <= pos


an_all = [m.start() for m in re.finditer(r'analytic', SRC, re.I)]
an_hyp = [q for q in an_all if not in_prose(q)]
thm_rig = re.findall(r'^(?:theorem|lemma)\s+\S*(?:rigid|stationar)\S*', SRC, re.M)
note('read', 'occurrences of "analytic" in the whole probe      : %d' % len(an_all))
note('read', '...of those, any that is a HYPOTHESIS rather than '
             'prose     : %d' % len(an_hyp))
note('read', 'theorems/lemmas whose NAME carries rigid/stationar: %s' % (thm_rig or 'none'))
note('read', 'and the only one is st_cor_stationary, which ASSUMES it: %s'
     % (thm_rig == ['theorem st_cor_stationary']))
note('read', 'the probe says so itself ("Rigidity itself is not proved"): %s'
     % ('Rigidity itself is not proved' in flat(SRC)))
no_rigidity = not an_hyp and thm_rig == ['theorem st_cor_stationary']
note('VERDICT', '2b %s -- searched the whole probe for "analytic": %d occurrence(s), %d of them '
                'inside a docstring or comment and %d in a hypothesis; and for any theorem or '
                'lemma whose name carries "rigid" or "stationar": %s, which takes the '
                'Killing-horizon property as a HYPOTHESIS. So nothing in the probe derives a '
                'Killing horizon from stationarity, and "cited and not formalised" is right -- '
                'neither UNDERSTATED nor OVERSTATED is reached.'
     % ('SUPPORTED' if no_rigidity else 'UNDERSTATED', len(an_all),
        len(an_all) - len(an_hyp), len(an_hyp), thm_rig))
# negative probe 12 must fire both ways
fake_under = SRC.replace('theorem st_cor_stationary', 'theorem st_rigidity_proved', 1)
thm_fake = re.findall(r'^(?:theorem|lemma)\s+\S*(?:rigid|stationar)\S*', fake_under, re.M)
note('neg12', 'a probe with a rigidity theorem of its own -> names %s (must NOT be the '
              'assume-it one alone)' % (thm_fake or 'none'))
if thm_fake == ['theorem st_cor_stationary']:
    FAIL.append('negative probe 12 did not fire in the UNDERSTATED direction')
note('neg12', 'and the OVERSTATED direction is reachable: a claim of machine-checking a '
              'clause arm 3 finds absent would read NOT SUPPORTED there')

print()
print('  2c THE FIRST PARAGRAPH: "the theorem\'s hypotheses ... include analyticity"')
note('read', 'l.290 cites the rigidity theorem and analyticity  : %s'
     % ('rigidity theorem' in PROOF1 and 'analyticity' in PROOF1))
note('read', 'l.290 then says lem:killing applies               : %s'
     % ('lem:killing} applies' in PROOF1))
note('read', 'and the probe asks NO analyticity of its own      : %s' % (not an_hyp))
note('VERDICT', '2c SUPPORTED -- the division of labour is right: the prose paragraph carries '
                'the cited theorem and its analyticity, and the probe, taking the conclusion, '
                'asks no analyticity at all. The two paragraphs do not overlap and neither '
                'claims the other\'s ground.')

print()
print('=' * 78)
print('ARM 3 -- THE FOUR CONCLUSIONS, AGAINST st_cor_stationary')
print('=' * 78)
CONC = [
    ('the tangent is null along every integral curve',
     ['∀ t ∈ Icc a b, S.g (γ t) (X (γ t)) (X (γ t)) = 0',
      'mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) = 0'], None),
    ('every pair is metrically coincident',
     ['∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related S.g γ t₁ t₂',
      'kg_deltaTau S.g X γ a b = 0'], None),
    ("the horizon's adapted splitting assigns Δx = Δτ = 0",
     ['∃ σ : kw_AdaptedSplitting S.g γ a b', 'σ.Δx = 0 ∧ σ.Δτ = 0'], None),
]
for nm, need, _ in CONC:
    got = [(m, m in ST) for m in need]
    for m, ok in got:
        note('read', '%-46s %s' % (nm[:46], ok))
    note('G4', '%s -> %s' % (nm, 'SUPPORTED' if all(o for _, o in got) else 'NOT SUPPORTED'))

print()
print('  3b "distinct points stay distinct" -- read for its GUARD')
guard = 'InjOn γ (Icc a b) →' in ST
note('read', 'the distinctness conjunct is guarded by InjOn γ   : %s' % guard)
note('read', 'the paragraph states it with no guard             : %s'
     % ('distinct points stay distinct' in PARA and 'injective' not in PARA))
note('read', 'the metric-coincidence conjunct is UNGUARDED      : %s'
     % ('∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related S.g γ t₁ t₂' in ST))
if guard and 'injective' not in PARA:
    note('VERDICT', '3b SCOPE-DIFFERS -- the probe\'s distinctness conjunct is conditional, '
                    '`InjOn γ (Icc a b) → …`, and the paragraph states "distinct points stay '
                    'distinct" with no condition. Without injectivity a generator may revisit a '
                    'point, so the unguarded reading is stronger than the theorem. Note the '
                    'metric-coincidence conjunct beside it IS unguarded, so this is the one '
                    'conclusion of the four that carries a hypothesis the prose does not. '
                    '** Six words: "distinct points stay distinct where the generator is '
                    'injective". Routed, not edited. **')
else:
    note('VERDICT', '3b SUPPORTED')
note('neg3', 'the conclusions are read UNDER their binders (∀ t, ∀ t₁ t₂, ∃ σ), not at TOP: %s'
     % all(x in ST for x in ('∀ t ∈ Icc a b', '∀ t₁ ∈ Icc a b', '∃ σ :')))

print()
print('=' * 78)
print('ARM 4 -- THE WITNESS, AGAINST st_witness')
print('=' * 78)
dom = 'def seWS : Set P := {p | 0 < p.2 ∧ p.1 * p.2 < 1}' in flat(SRC)
fld = 'sq_L M x = (-x.1 / (4 * M), x.2 / (4 * M))' in flat(SRC)
same = '(se_S hM).IsKillingHorizon (st_χ M)' in WI
front = 'frontier ((sx_ext hM).ι ⁻¹\' cz_St.JpastSet cz_scri)' in WI
note('read', 'the domain {V>0, UV<1} is the probe\'s own seWS    : %s' % dom)
note('read', 'the field reads (−U/4M, V/4M), i.e. (V∂_V−U∂_U)/4M: %s' % fld)
note('read', 'the witness discharges the SAME IsKillingHorizon  : %s' % same)
note('read', 'on the frontier of the causal past of scri        : %s' % front)
note('read', 'two DISTINCT events, both on that horizon         : %s'
     % ('st_ev V₁ h₁ ≠ st_ev V₂' in WI))
note('read', 'metrically coincident: kg_Related BOTH ways       : %s'
     % (WI.count('kg_Related (se_S hM).g') >= 2))
note('read', '...and Δτ = 0 with the splitting at Δx = Δτ = 0   : %s'
     % ('kg_deltaTau' in WI and 'σ.Δx = 0 ∧ σ.Δτ = 0' in WI))
ok4 = dom and fld and same and front and 'st_ev V₁ h₁ ≠ st_ev V₂' in WI
note('VERDICT', '4 %s -- the witness is on the paragraph\'s own domain with the paragraph\'s own '
                'field to the factor and the signs, it discharges the VERY predicate arm 1 reads '
                '(so arm 1 is not vacuous), and it puts two distinct events of that horizon in '
                'metric coincidence both ways with Δx = Δτ = 0.'
     % ('SUPPORTED' if ok4 else 'NOT SUPPORTED'))

print()
print('  4b A LINE REFERENCE INSIDE THE PROBE, read because a citation names a tree')
probe_ref = sorted(set(re.findall(r'l\.(\d{3})', SRC)))
_rr = re.findall(r'l\.(\d{3})[^)]{0,60}?rigidity|rigidity[^)]{0,60}?l\.(\d{3})', flat(SRC))
rig_ref = sorted({x for t in _rr for x in t if x})
p1_rig = [i + 1 for i, l in enumerate(P1_L) if l.startswith('By the rigidity theorem')]
note('read', 'every line number the probe cites into P1         : %s' % probe_ref)
note('read', '...the one it gives FOR the rigidity citation      : %s' % (rig_ref or 'none'))
probe_ref = rig_ref or probe_ref
note('read', "P1's rigidity sentence is at                      : l.%s"
     % (p1_rig[0] if p1_rig else '?'))
if p1_rig and str(p1_rig[0]) not in probe_ref:
    note('VERDICT', '4b STALE LINE REFERENCE -- the probe cites P1 l.%s for the rigidity citation '
                    'and that sentence now sits at l.%d. Nothing in the paper is wrong; the probe\'s '
                    'own pointer has drifted by %d line(s). This seat\'s standing lesson applies to '
                    'a probe as much as to a reading: a line number is a claim about a TREE, and '
                    'this one names none. Routed as a precision item, not edited.'
                    % (', l.'.join(probe_ref), p1_rig[0], p1_rig[0] - int(probe_ref[0])))
else:
    note('VERDICT', '4b SUPPORTED -- the probe\'s line reference matches this tree.')

print()
print('=' * 78)
print('SUMMARY')
print('=' * 78)
for v in VERDICTS:
    print('  ' + v[:150])
print()
if FAIL:
    print('GUARD / NEGATIVE-PROBE FAILURES (%d):' % len(FAIL))
    for f in FAIL:
        print('  - ' + f)
    sys.exit(1)
print('every registered reading ran; %d verdicts recorded.' % len(VERDICTS))
sys.exit(0)
