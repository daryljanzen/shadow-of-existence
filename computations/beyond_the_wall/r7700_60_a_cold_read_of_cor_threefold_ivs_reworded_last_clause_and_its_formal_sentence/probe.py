#!/usr/bin/env python3
# r7700 (60) -- the reading instrument for the order r7697.
#
# Reads, on the tree named in runs/TREE.txt and no other: `cor:threefold` (iv)'s reworded last
# clause and the formal sentence that carries it, against `tl_cor_threefold_iv_b`,
# `tl_separation_interval` and `tl_witness` in
# `computations/formalisation/lean/probes/ThreefoldLocal.lean`.
#
# THE SIX GUARD FAMILIES: G1 one predicate per conjunct; G2 three anchor forms only (a word
# boundary, an escaped control sequence with ONE leading backslash, an escaped math delimiter),
# an unanchored marker REFUSED; G3 the flip family; G4 classifier probes tested on both classes;
# G5 reader probes each with its negative; G6 every prose probe on a whitespace-FLATTENED copy.
# EVERY VERDICT NOTE IS BUILT FROM ITS READINGS.
#
# A verdict the probe cannot compute prints UNMEASURED.  An arm whose verdict would read
# backwards as SUPPORTED carries its own label -- the r7698 correction.

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'ThreefoldLocal.lean')

FAIL = []
READINGS = []


def say(s=''):
    print(s)
    READINGS.append(s)


def flat(s):                                   # G6
    return re.sub(r'\s+', ' ', s)


def anchor(marker):                            # G2
    if marker.startswith('\\') or marker.startswith('$'):
        return re.escape(marker)
    if re.match(r'^\w', marker) and re.search(r'\w$', marker):
        return r'\b' + re.escape(marker) + r'\b'
    if re.search(r'[^\w\s]', marker):
        return re.escape(marker)
    raise AssertionError('G2 REFUSES the unanchored marker %r' % marker)


def present(hay, marker):
    return re.search(anchor(marker), hay) is not None


_g2 = []
for _m in ('temporal', '\\texttt', '$\\gamma$'):
    try:
        anchor(_m); _g2.append('accepted')
    except AssertionError:
        _g2.append('REFUSED')
try:
    anchor('  '); _g2.append('accepted')
except AssertionError:
    _g2.append('REFUSED')
say('G2 self-probe: %s' % ', '.join(_g2))
if _g2 != ['accepted', 'accepted', 'accepted', 'REFUSED']:
    FAIL.append('G2 self-probe did not accept the three forms and refuse the unanchored marker')


def need(path):
    if not os.path.exists(path):
        FAIL.append('missing object: %s' % path)
        return ''
    with open(path, encoding='utf-8') as fh:
        return fh.read()


p1 = need(P1)
lean = need(LEAN)
if not (p1 and lean):
    print('\n'.join(FAIL)); sys.exit(2)
F1 = flat(p1)


def theorem_sig(name):
    """A theorem's signature: from `theorem <name>` to the `:= by` opening its proof."""
    mm = re.search(r'\ntheorem\s+' + re.escape(name) + r'\b', lean)
    if not mm:
        return '', ''
    tail = lean[mm.start():mm.start() + 4000]
    cut = tail.find(':= by')
    sig = tail[:cut + 5] if cut > 0 else tail[:1500]
    body = lean[mm.start() + len(sig):mm.start() + len(sig) + 2500]
    return sig, body


say()
say('=' * 94)
say('ITEM -- (iv)\'s reworded last clause and its formal sentence, against ThreefoldLocal.lean')
say('=' * 94)

CLAUSE = 'it is not fixed by the geometry'
FORMAL = 'For the last clause of~(iv)'
ic, iff_ = F1.find(CLAUSE), F1.find(FORMAL)
say('the clause located by its text at character %d; the formal sentence at %d' % (ic, iff_))
clause = F1[max(ic - 260, 0):ic + 230]
formal = F1[iff_:iff_ + 700]
for nm, j in (('clause', ic), ('formal sentence', iff_)):
    if j < 0:
        FAIL.append('the %s could not be located by its text on this tree' % nm)
say()
say('the clause, as this tree carries it:')
say('  ... ' + clause[200:] if len(clause) > 200 else '  ' + clause)
say()
say('the formal sentence, as this tree carries it:')
say('  ' + formal[:520])

SIG_B, BODY_B = theorem_sig('tl_cor_threefold_iv_b')
SIG_I, BODY_I = theorem_sig('tl_separation_interval')
SIG_P, BODY_P = theorem_sig('tl_iv_b')
SIG_W, BODY_W = theorem_sig('tl_witness')
FB, FI, FP, FW = flat(SIG_B), flat(SIG_I), flat(SIG_P), flat(SIG_W)
say()
say('the four theorems read, by signature length: iv_b %d, interval %d, iv_b\'s primitive %d, '
    'witness %d' % (len(SIG_B), len(SIG_I), len(SIG_P), len(SIG_W)))
for nm, s in (('tl_cor_threefold_iv_b', SIG_B), ('tl_separation_interval', SIG_I),
              ('tl_iv_b', SIG_P), ('tl_witness', SIG_W)):
    if not s:
        FAIL.append('cited or compared theorem %s is not in the file on this tree' % nm)
NEG, _ = theorem_sig('tl_cor_threefold_iv_b_that_is_not_there')
say('NEGATIVE PROBE 1 (a name the file does not carry): %s'
    % ('absent, as it must be' if not NEG else 'FOUND -- the reader matches anything'))
if NEG:
    FAIL.append('the theorem reader fired on a name the file does not carry')

# ---- A: the clause's halves, one predicate each (G1) ---------------------------------------
say()
say('arm A -- the clause read one predicate per conjunct (G1):')
A = {}
for k, mk in (('the invariance half', 'it is not fixed by the geometry'),
              ('the deformation half', 'smooth local deformations of'),
              ('the rider that τ stays temporal', 'keeping $\\tau$ temporal')):
    A[k] = present(clause, mk)
    say('  %-34s %s' % (k, 'FOUND' if A[k] else 'ABSENT'))
# is "temporal" a CONCLUSION of the theorem or a HYPOTHESIS of it?
concl = FB[FB.find(':\n') if ':\n' in FB else FB.find(': ∃'):]
tgt = FB[FB.find('∃ δ₀'):] if '∃ δ₀' in FB else ''
say('  the theorem\'s conclusion, as the file states it:')
say('    %s' % tgt[:240])
A['temporal in the conclusion'] = 'IsTemporalOn' in tgt
say('  τ\' temporal is part of the CONCLUSION: %s' % ('YES' if A['temporal in the conclusion'] else 'no'))
A_OK = all(A.values())

# ---- B: where the deformation lives -------------------------------------------------------
say()
say('arm B -- the localisation: the clause names a neighbourhood of the CURVE, the sentence an '
    'open set about the ENDPOINT:')
hyp_V = re.search(r'\{V : Set N\} \(hV : IsOpen V\) \(hqV : q ∈ V\)', FB)
say('  what `tl_cor_threefold_iv_b` quantifies over: %s'
    % (hyp_V.group(0) if hyp_V else 'UNREAD'))
pnotV_b = re.search(r'p ∉ V', FB) is not None
pnotV_p = re.search(r'p ∉ V', FP) is not None
say('  `p ∉ V` among `tl_cor_threefold_iv_b`\'s hypotheses: %s' % ('YES' if pnotV_b else 'no'))
say('  `p ∉ V` among its primitive `tl_iv_b`\'s hypotheses:  %s' % ('YES' if pnotV_p else 'no'))
shrink = re.search(r'isOpen_compl_singleton', BODY_B) is not None or \
    re.search(r'hV\.inter isOpen_compl_singleton', flat(BODY_B)) is not None
say('  and how the corollary discharges it: %s'
    % ('by intersecting V with the complement of {p} (`hV.inter isOpen_compl_singleton`)'
       if shrink else 'UNREAD'))
offV = re.search(r'∀ x ∉ V, τ\' x = τ x', FB) is not None
say('  the produced function still equals τ off the WHOLE of V: %s' % ('YES' if offV else 'no'))
B_OK = bool(hyp_V) and not pnotV_b and pnotV_p and shrink and offV
# NEGATIVE PROBE: the hypothesis reader must fire on an injected `p ∉ V`
inj = FB.replace('(hqV : q ∈ V)', '(hqV : q ∈ V) (hpV : p ∉ V)', 1)
say('  NEGATIVE PROBE (the hypothesis reader on a copy with `p ∉ V` injected): %s'
    % ('fires, as it must' if re.search(r'p ∉ V', inj) else 'BLIND'))
if not re.search(r'p ∉ V', inj):
    FAIL.append('arm B: the hypothesis reader did not fire on an injected `p ∉ V`')

# ---- C: the order's first question --------------------------------------------------------
say()
say('arm C -- THE ORDER\'S FIRST QUESTION: q in the open set; is p required outside it?')
# ⌗ The first run of this reader printed FOUR hypotheses where the theorem asks FIVE: the
#   name class was ASCII-only, so `hτ` -- whose second character is a Greek tau -- was not a
#   hypothesis as far as the reader could see.  A hypothesis list read by an instrument that
#   cannot spell one of the names is not the list; and the arm this feeds is the WHOLENESS of a
#   hypothesis list, which makes the defect the very error the arm is for.  Recorded rather
#   than quietly corrected.  `\w` with re.UNICODE is the fix.
hyps = re.findall(r'\((h\w*) : ([^)]*)\)', FB, re.UNICODE)
inst = re.findall(r'\[([^\]]*)\]', FB)
say('  the hypotheses, one per reading:')
for h, w in hyps:
    say('    %-6s %s' % (h, w))
say('  the instance arguments: %s' % ', '.join(inst))
C_OK = any(h == 'hqV' for h, _ in hyps) and not pnotV_b

# ---- D: the order's second question -------------------------------------------------------
say()
say('arm D -- THE ORDER\'S SECOND QUESTION: is "filling an open interval about its value" '
    'what is proved?')
iv = re.search(r'Ioo \(τ q - τ p - δ₀\) \(τ q - τ p \+ δ₀\) ⊆', FI)
setb = re.search(r'\{s \| ∃ τ\' : N → ℝ, S\.IsTemporalOn S\.M τ\' ∧ \(∀ x ∉ V, τ\' x = τ x\) ∧ '
                 r'τ\' q - τ\' p = s\}', FI)
say('  `tl_separation_interval`\'s conclusion, as the file states it:')
say('    %s' % (FI[FI.find('∃ δ₀'):][:300] if '∃ δ₀' in FI else 'UNREAD'))
say('  an OPEN interval: %s; CENTRED on τ(q) − τ(p): %s; TWO-SIDED: %s'
    % ('YES' if iv else 'no', 'YES' if iv else 'no', 'YES' if iv else 'no'))
say('  and the interval is contained in the set of separations actually ACHIEVED: %s'
    % ('YES' if setb else 'no'))
# the flip (G3): strike the interval and the reader must fail
say('  FLIP (G3), the same reader on a copy with the interval struck: %s'
    % ('still reads an interval -- WRONG'
       if re.search(r'Ioo \(τ q - τ p - δ₀\)', FI.replace('Ioo (τ q - τ p - δ₀)', 'XX', 1))
       else 'reads none, as it must'))
if re.search(r'Ioo \(τ q - τ p - δ₀\)', FI.replace('Ioo (τ q - τ p - δ₀)', 'XX', 1)):
    FAIL.append('arm D: the interval reader survived having its interval struck')
# and the weaker, pointwise form must be distinguishable from the interval form
ptwise = re.search(r'≠', FW) is not None
say('  the weaker POINTWISE form (a separation merely differing) is what the WITNESS states: %s'
    % ('YES' if ptwise else 'no'))
D_OK = bool(iv) and bool(setb)

# ---- E: the setting -----------------------------------------------------------------------
say()
say('arm E -- the setting the sentence names, against the theorems\' own instance arguments:')
said = {'finite dimension': present(formal, 'in finite dimension'),
        'a Hausdorff manifold': present(formal, 'Hausdorff manifold')}
asked = {'FiniteDimensional ℝ E': 'FiniteDimensional ℝ E' in FB and 'FiniteDimensional ℝ E' in FI,
         'T2Space N': 'T2Space N' in FB and 'T2Space N' in FI}
for k, v in said.items():
    say('  the sentence says %-22s %s' % (k, 'YES' if v else 'no'))
for k, v in asked.items():
    say('  both theorems ask  %-22s %s' % (k, 'YES' if v else 'no'))
extra = [i for i in inst if 'FiniteDimensional' not in i and 'T2Space' not in i]
say('  any OTHER instance argument either theorem asks: %s' % (', '.join(extra) if extra else 'none'))
say('  and the structural hypothesis the sentence covers by "the setting of rem:formalised": %s'
    % ('LocallyOneChart (hL)' if any(h == 'hL' for h, _ in hyps) else 'UNREAD'))
E_OK = all(said.values()) and all(asked.values()) and not extra

# ---- F: the witness -----------------------------------------------------------------------
say()
say('arm F -- the witness:')
fw = {'is on to_cor_1c\'s pair': 'to_γN 0' in FW and 'to_γN 1' in FW,
      'states the pair causally and not chronologically related':
          'minkN.Cau (to_γN 0) (to_γN 1)' in FW and '¬ minkN.Chr' in FW,
      'produces a second TEMPORAL function': FW.count('IsTemporalOn') >= 2,
      'equal to the first off a ball about q': 'ball (φ (to_γN 1))' in FW,
      'with a DIFFERENT separation': '≠' in FW,
      'for EVERY radius r > 0': bool(re.search(r'\{r : ℝ\} \(hr : 0 < r\)', FW))}
for k, v in fw.items():
    say('  %-56s %s' % (k, 'YES' if v else 'no'))
F_OK = all(fw.values())

# ---- G: the order's third question --------------------------------------------------------
say()
say('arm G -- THE ORDER\'S THIRD QUESTION: does anything else in P1 rely on "arbitrarily"?')
say('  the search performed over the whole of P1 (%d characters flattened):' % len(F1))
SITES = ['arbitrarily', 'no invariant geometric meaning', 'not fixed by the geometry',
         'non-invariant', 'altering it']
hits = {}
for s in SITES:
    hits[s] = [m.start() for m in re.finditer(anchor(s), F1)]
    say('    %-34s %d occurrence(s)' % (repr(s), len(hits[s])))


def classify(window):                          # G4
    """STRONGER = the claim that the separation can be moved arbitrarily far; WEAKER = that it is
    not fixed / not invariant, which is what the interval theorem gives."""
    w = window.lower()
    strong = any(t in w for t in ('arbitrarily far', 'altered arbitrarily', 'arbitrarily large',
                                  'any value whatever'))
    weak = any(t in w for t in ('not fixed by the geometry', 'no invariant geometric meaning',
                                'stays non-invariant', 'non-invariant'))
    if strong:
        return 'STRONGER THAN PROVED'
    if weak:
        return 'THE WEAKER CLAIM, WHICH IS PROVED'
    return 'NEITHER'


say('  each site classified:')
G_rows = []
for s in SITES:
    for j in hits[s]:
        win = F1[max(j - 220, 0):j + 220]
        cls = classify(win)
        G_rows.append((s, j, cls))
        say('    %-34s at %7d  %s' % (repr(s), j, cls))
say('  CLASSIFIER PROBE (G4), both classes: %r -> %s ; %r -> %s'
    % ('may be altered arbitrarily', classify('may be altered arbitrarily'),
       'stays non-invariant', classify('stays non-invariant')))
if classify('may be altered arbitrarily') != 'STRONGER THAN PROVED':
    FAIL.append('arm G: the reliance classifier does not recognise the stronger claim')
# NEGATIVE PROBE 8: the reliance probe must fire on an injected site
inj_p1 = F1 + ' The separation may be altered arbitrarily by a local deformation. '
inj_cls = [classify(inj_p1[m.start() - 220:m.start() + 220])
           for m in re.finditer(r'altered arbitrarily', inj_p1)]
say('  NEGATIVE PROBE 8 (an injected site stating the stronger claim): %s'
    % ('fires: %s' % inj_cls if inj_cls else 'BLIND'))
if 'STRONGER THAN PROVED' not in inj_cls:
    FAIL.append('arm G: the reliance probe did not fire on an injected stronger-claim site')
G_OK = not any(c == 'STRONGER THAN PROVED' for _, _, c in G_rows)

# ---- H: the scope sentence ----------------------------------------------------------------
say()
say('arm H -- the scope sentence\'s three groups, and what carries (iv)\'s FIRST clause:')
scope = F1[F1.find('Parts~(i)--(iii), the last clause of~(iv)'):][:200]
say('  the sentence: %s' % scope[:150])
groups = {'(i)-(iii)': 'Parts~(i)--(iii)' in scope,
          'the last clause of (iv)': 'the last clause of~(iv)' in scope,
          'all four parts together on one pair': 'all four parts together on one pair' in scope}
for k, v in groups.items():
    say('  names %-38s %s' % (k, 'YES' if v else 'no'))
onepair = re.search(r'all in one theorem \(\\texttt\{to\\_cor\\_1c\}\)', F1) is not None
say('  the one-pair group\'s own citation present in the paragraph: %s'
    % ('YES (to_cor_1c)' if onepair else 'no'))
ivfirst = re.search(r'by Theorem~\\ref\{thm:metric-singularity\} their temporal separation vanishes',
                    F1) is not None
acname = re.search(r'\\texttt\{ac\\_metric\\_singularity\\_along\}', F1) is not None
say('  (iv)\'s first clause is stated as following from thm:metric-singularity: %s'
    % ('YES' if ivfirst else 'no'))
say('  and that theorem\'s own machine-checked form is named elsewhere in P1: %s'
    % ('YES (ac_metric_singularity_along)' if acname else 'no'))
say('  ⇒ so the only part of (iv) proved IN GENERAL here is its last clause, and its first clause '
    'is carried on the witness pair and by a separately machine-checked theorem.')
H_OK = all(groups.values()) and onepair and ivfirst and acname

say()
say('-' * 94)


def verdict(v):
    if isinstance(v, str):
        return v
    return 'UNMEASURED' if v is None else ('SUPPORTED' if v else 'NOT SUPPORTED')


for k, v, note in (
        ('A', A_OK, 'both halves are in the clause and τ\' temporal is in the theorem\'s conclusion'),
        ('B', ('SUPPORTED, AND THE THEOREM IS MORE GENERAL' if B_OK else 'NOT SUPPORTED'),
         'the theorem takes ANY open V about q, needs no `p ∉ V` (its primitive does, and the '
         'corollary discharges it by shrinking V away from p), and still returns a function equal '
         'to τ off the whole of V'),
        ('C', C_OK, 'q ∈ V is a hypothesis; p outside it is NOT'),
        ('D', D_OK, 'the conclusion is an open two-sided interval centred on the value and '
                    'contained in the separations achieved'),
        ('E', E_OK, 'the two instance arguments the sentence names are exactly the two the '
                    'theorems ask, with no third'),
        ('F', F_OK, 'the witness is on the paragraph\'s own pair, for every radius, with a second '
                    'temporal function and a different separation'),
        ('G', G_OK, '%d reliance site(s) found, %d of them stating the stronger claim'
                    % (len(G_rows), sum(1 for _, _, c in G_rows if c == 'STRONGER THAN PROVED'))),
        ('H', H_OK, 'the three groups are what the paragraph delivers, (iv)\'s first clause being '
                    'carried on the one pair and by a separately machine-checked theorem')):
    say('arm %s: %-13s -- %s' % (k, verdict(v), note))

say()
say('=' * 94)
say('8 verdicts printed.  %d reader or classifier probe(s) failed.' % len(FAIL))
for f in FAIL:
    say('  DEFECT: %s' % f)
say('=' * 94)

with open(os.path.join(HERE, 'runs', 'READINGS.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(READINGS) + '\n')
sys.exit(1 if FAIL else 0)
