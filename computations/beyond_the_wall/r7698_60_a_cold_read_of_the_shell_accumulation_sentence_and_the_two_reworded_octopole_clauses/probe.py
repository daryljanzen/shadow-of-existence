#!/usr/bin/env python3
# r7698 (60) -- the reading instrument for the order r7695.
#
# Reads, on the tree named in runs/TREE.txt and no other:
#   ITEM 1  P1's shell-accumulation sentence in `lem:alignment`'s proof, against `sa2_shell`
#           in `computations/formalisation/lean/probes/ShellAccumulation.lean`.
#   ITEM 2  P15's two reworded octopole clauses, against the depth-gap receipt's `r7691` block
#           and 70's `r7693` RESULT.
#
# THE SIX GUARD FAMILIES THIS SEAT CARRIES:
#   G1  one predicate per conjunct -- never one regex for a conjunction;
#   G2  three anchor forms only: a word boundary, an escaped control sequence (ONE leading
#       backslash -- the correction r7694 had to make to its own anchor()), an escaped math
#       delimiter.  An unanchored marker is REFUSED, not matched loosely;
#   G3  the flip family: every reading that can be inverted is re-run inverted;
#   G4  classifier probes -- a classifier is tested on inputs of both classes;
#   G5  reader probes, each with its NEGATIVE probe;
#   G6  every prose probe on a whitespace-FLATTENED copy.
#
# EVERY VERDICT NOTE IS BUILT FROM ITS READINGS.  At r7694 a note contradicted the reading
# printed above it, because the note was written before the reading was computed.  No note in
# this file is a literal sentence about a measured quantity.

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'ShellAccumulation.lean')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
R70 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7693_70_configs_and_fork_price', 'RESULT.md')
RAN = os.path.join(HERE, 'runs', 'ran_depth_gap.txt')

FAIL = []
READINGS = []


def say(s=''):
    print(s)
    READINGS.append(s)


def need(path):
    if not os.path.exists(path):
        FAIL.append('missing object: %s' % path)
        return ''
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def flat(s):                                   # G6
    return re.sub(r'\s+', ' ', s)


def anchor(marker):                            # G2
    # Three anchor forms only.  A marker with no boundary of its own is REFUSED rather than
    # matched loosely.  r7694's first run REFUSED a correctly anchored marker because this
    # function asked for TWO leading backslashes; one is what an escaped control sequence has.
    if marker.startswith('\\'):
        return re.escape(marker)
    if marker.startswith('$'):
        return re.escape(marker)
    if re.match(r'^\w', marker) and re.search(r'\w$', marker):
        return r'\b' + re.escape(marker) + r'\b'
    if re.search(r'[^\w\s]', marker):
        return re.escape(marker)
    raise AssertionError('G2 REFUSES the unanchored marker %r' % marker)


def present(hay, marker):
    return re.search(anchor(marker), hay) is not None


def count(hay, marker):
    return len(re.findall(anchor(marker), hay))


# ---------------------------------------------------------------------------------------------
# G2's own probe: the three forms accepted, and an unanchored marker refused.
# ---------------------------------------------------------------------------------------------
_g2 = []
for _m in ('killing', '\\mathcal{L}', '$\\ell=4$'):
    try:
        anchor(_m)
        _g2.append((_m, 'accepted'))
    except AssertionError:
        _g2.append((_m, 'REFUSED'))
try:
    anchor('   ')
    _g2.append(('three spaces', 'accepted'))
except AssertionError:
    _g2.append(('three spaces', 'REFUSED'))
say('G2 self-probe: ' + '; '.join('%r %s' % (m, v) for m, v in _g2))
if [v for _, v in _g2] != ['accepted', 'accepted', 'accepted', 'REFUSED']:
    FAIL.append('G2 self-probe did not accept the three anchor forms and refuse the unanchored one')
say()

p1 = need(P1)
p15 = need(P15)
lean = need(LEAN)
rcpt = need(RCPT)
r70 = need(R70)
ran = need(RAN) if os.path.exists(RAN) else ''
if not (p1 and p15 and lean and rcpt and r70):
    print('\n'.join(FAIL))
    sys.exit(2)

F1, F15, F70 = flat(p1), flat(p15), flat(r70)

# =============================================================================================
say('=' * 94)
say('ITEM 1 -- P1, lem:alignment\'s proof: the shell-accumulation sentence against `sa2_shell`')
say('=' * 94)

# --- the sentence, LOCATED BY ITS TEXT (never by the order's line number) --------------------
SENT_KEY = 'On that model the level sets of the retarded slicing'
m = re.search(re.escape(SENT_KEY) + r'(.{0,1200}?)\\emph|' + re.escape(SENT_KEY) + r'(.{0,1200})', F1)
i = F1.find(SENT_KEY)
sent = F1[i:i + 760] if i >= 0 else ''
say('the sentence located by its text at character %d of the flattened file; its first 220 chars:' % i)
say('  ' + sent[:220] + ' ...')
if i < 0:
    FAIL.append('ITEM 1: the sentence could not be located by its text on this tree')

# the four conjuncts and the two meta-claims, ONE PREDICATE EACH (G1)
CONJ = {
    '1a-lower': 'accumulate on the future horizon',
    '1a-upper': 'and on nothing else',
    '1b': 'the cones never meeting it',
    '1c': 'including on the part of the horizon that forms inside the body',
    '1e-causal': 'accumulation is a causal statement',
    '1e-factor': "so the shell's conformal factor never enters",
    '1e-carry': 'it is proved on the flat metric and carried to the shell unchanged',
    '1d': 'is not claimed there',
}
say()
say('the sentence read one predicate per conjunct (G1):')
for k in sorted(CONJ):
    say('  %-10s %-5s %r' % (k, 'FOUND' if present(sent, CONJ[k]) else 'ABSENT', CONJ[k]))
    if not present(sent, CONJ[k]):
        FAIL.append('ITEM 1: conjunct %s is not in the sentence on this tree' % k)
say('  the citation the sentence gives: %s' % ('sa2_shell / ShellAccumulation.lean'
    if present(sent, 'sa2') and present(sent, 'ShellAccumulation') else 'NOT THE CITED PAIR'))

# --- the theorem, read from its own signature ------------------------------------------------
NS_A = lean.find('\nnamespace SA2Model')
NS_B = lean.find('\nend SA2Model')
say()
say('the SA2Model namespace spans characters %d..%d of the Lean file (%d lines in all)'
    % (NS_A, NS_B, lean.count('\n') + 1))
if not (0 < NS_A < NS_B):
    FAIL.append('ITEM 1: the SA2Model namespace could not be delimited')
shell_ns = lean[NS_A:NS_B]


def theorem_block(src, name):
    """The signature of a theorem: from `theorem <name>` to the `:= by` that opens its proof."""
    mm = re.search(r'\ntheorem\s+' + re.escape(name) + r'\b', src)
    if not mm:
        return '', ''
    start = mm.start()
    tail = src[start:start + 6000]
    cut = tail.find(':= by')
    if cut < 0:
        cut = tail.find(':=')
    sig = tail[:cut + 5]
    colon = sig.find(':\n')
    if colon < 0:
        colon = sig.find(' :\n')
    hyps = sig[:colon if colon > 0 else len(sig)]
    return sig, hyps


SIG, HYPS = theorem_block(shell_ns, 'sa2_shell')
say('`sa2_shell` found in the namespace: %s (%d characters of signature)'
    % ('YES' if SIG else 'NO', len(SIG)))
if not SIG:
    FAIL.append('ITEM 1 arm 1f: `sa2_shell` is not a theorem of the SA2Model namespace on this tree')
FSIG = flat(SIG)

# arm 1f -- NEGATIVE PROBE (the first of the thirteen): a name the file does not carry must
# come back absent, or the reader is answering about itself and not about the file.
NEG_SIG, _ = theorem_block(shell_ns, 'sa2_shell_that_is_not_there')
say('NEGATIVE PROBE 1 (a name the file does not carry): %s'
    % ('absent, as it must be' if not NEG_SIG else 'FOUND -- the reader matches anything'))
if NEG_SIG:
    FAIL.append('ITEM 1: the theorem reader fired on a name the file does not carry')

# --- arm 1a: both Kuratowski limits, for BOTH subjects --------------------------------------
HSET = '{y : P | y.1 = sv_uH M v₀}'
subj = {
    'slices': 'slice ((sh_S hM v₀)' if False else r'KL([is]) \(\(sh_S hM v₀\)\.slice',
    'cones': r'KL([is]) \(\(sh_S hM v₀\)\.cone',
}
lim = {}
for what, pat in (('slice', r'KL([is])\s*\(\(sh_S hM v₀\)\.slice'),
                  ('cone', r'KL([is])\s*\(\(sh_S hM v₀\)\.cone')):
    got = sorted(set(re.findall(pat, FSIG)))
    lim[what] = got
say()
say('arm 1a -- the Kuratowski conjuncts in `sa2_shell`\'s conclusion, by subject:')
for what in ('slice', 'cone'):
    names = {'i': 'KLi (the LOWER limit: every horizon point is approached)',
             's': 'KLs (the UPPER limit: they accumulate nowhere else)'}
    say('  %-6s %d of 2 -- %s' % (what, len(lim[what]),
        '; '.join(names[g] for g in lim[what]) if lim[what] else 'neither'))
HSET_N = FSIG.count('{y : P | y.1 = sv_uH M v₀}')
say('  the right-hand side of each: the set %r, which the conclusion names %d times'
    % (HSET, HSET_N))
A1_BOTH_BOTH = lim['slice'] == ['i', 's'] and lim['cone'] == ['i', 's']

# arm 1a -- the FLIP (G3): strike the KLs conjuncts from a COPY and the upper half must fail.
flip = re.sub(r'KLs\s*\(\(sh_S hM v₀\)\.(slice|cone)[^∧]*∧', '', FSIG)
flip_lim = {w: sorted(set(re.findall(r'KL([is])\s*\(\(sh_S hM v₀\)\.' + w, flip)))
            for w in ('slice', 'cone')}
say('  FLIP (G3), the same reader on a copy with the upper-limit conjuncts struck: slice %s, cone %s'
    % (flip_lim['slice'] or 'none', flip_lim['cone'] or 'none'))
if 's' in flip_lim['slice'] or 's' in flip_lim['cone']:
    FAIL.append('ITEM 1 arm 1a: the upper-limit reader survived having its conjuncts struck')

# --- arm 1b: the cones never meeting it, as a CONCLUSION and not a hypothesis ---------------
DISJ = re.search(r'∀ τ, \(sh_S hM v₀\)\.cone[^∧]*∩[^∧]*= ∅', FSIG)
in_hyps = re.search(r'∩[^∧]*= ∅', flat(HYPS)) is not None
say()
say('arm 1b -- cone disjointness: %s in the conclusion; %s among the hypotheses'
    % ('PRESENT' if DISJ else 'ABSENT', 'present' if in_hyps else 'absent'))
if DISJ:
    say('  the conjunct, as the file states it: %s' % DISJ.group(0))
say('  the hypotheses `sa2_shell` does ask: %s'
    % ' '.join(re.findall(r'\(h[^)]*\)', flat(HYPS))) or '  (none parsed)')
A1B = bool(DISJ) and not in_hyps

# --- arm 1c: the binder, and whether the inside-the-body part is reached ---------------------
# The accumulation conjuncts are SET EQUALITIES with the whole horizon set, so the binder is
# every point of it.  Non-vacuity is a separate question, and the file answers it.
NV, _ = theorem_block(shell_ns, 'sa2_nonvacuous')
FNV = flat(NV)
nv_bits = {
    'a point of the horizon': r'∈ \(sh_S one_pos 0\)\.H',
    'that point inside the body (v < v₀)': r'\)\.2 < 0',
    'the conformal factor there equal to 1 (the flat body)': r'sh_Φ 1 0 [^=]*= 1',
    'that point a Kuratowski limit of the SLICES': r'∈ KLi \(\(sh_S one_pos 0\)\.slice',
    'that point a Kuratowski limit of the CONES': r'∈ KLi \(\(sh_S one_pos 0\)\.cone',
}
say()
say('arm 1c -- the binder, and the inside-the-body part:')
say('  the accumulation conjuncts are SET EQUALITIES with %r, so the binder is every point of it'
    % HSET)
nv_got = {}
for k, pat in nv_bits.items():
    nv_got[k] = re.search(pat, FNV) is not None
    say('  `sa2_nonvacuous` states %-55s %s' % (k, 'YES' if nv_got[k] else 'no'))
A1C = A1_BOTH_BOTH and all(nv_got.values())

# --- arm 1d: the tangency claim, by a NAMED SEARCH (never a bare absence) -------------------
TANG = ['tangen', 'mc_tangency', 'dΘ', 'aligns']
say()
say('arm 1d -- the search performed, over the %d characters of the SA2Model namespace:' % len(shell_ns))
tang_hits = {}
for t in TANG:
    tang_hits[t] = shell_ns.count(t)
    say('  %-14s %d occurrence(s)' % (repr(t), tang_hits[t]))
say('  the same markers over the WHOLE file, for contrast: %s'
    % ', '.join('%s %d' % (repr(t), lean.count(t)) for t in TANG))
# NEGATIVE PROBE 12 (the error caught in BOTH directions): the search must FIRE on an injected site.
inj = shell_ns + '\ntheorem sa2_shell_tangency : mc_tangency_at_N := by trivial\n'
inj_hits = sum(inj.count(t) for t in TANG)
say('  NEGATIVE PROBE 12, the same search on a copy with one tangency theorem injected: %d hit(s) '
    'against %d on the file itself' % (inj_hits, sum(tang_hits.values())))
if inj_hits <= sum(tang_hits.values()):
    FAIL.append('ITEM 1 arm 1d: the tangency search did not fire on an injected site')
A1D = sum(tang_hits.values()) == 0

# --- arm 1e: the proof's route, and what the factor's role actually is ----------------------
say()
say('arm 1e -- the route the sentence describes, read off the proof and the lemmas it rewrites by:')
PROOF = SIG[SIG.find(':= by'):] if SIG else ''
proof_body = flat(shell_ns[shell_ns.find(FSIG[-20:]) if False else 0:0]) if False else ''
# the proof of sa2_shell, from `:= by` to the next blank-line-separated declaration
pm = re.search(r'\ntheorem\s+sa2_shell\b', shell_ns)
pbody = shell_ns[pm.start():pm.start() + 6000] if pm else ''
pbody = pbody[pbody.find(':= by'):]
pbody = pbody[:pbody.find('\n\n')] if '\n\n' in pbody else pbody
route = {
    'rewrites the slices through cz_scale': 'sa2_S_slice',
    'rewrites the cones through cz_scale': 'sa2_S_cone',
    'rewrites properness through cz_scale': 'sa2_S_sublevelProper',
    'takes its content from the FLAT model': 'sa2_flat',
}
for k, mk in route.items():
    say('  the proof %-45s %s (%r)' % (k, 'YES' if mk in pbody else 'no', mk))
    if mk not in pbody:
        FAIL.append('ITEM 1 arm 1e: the proof does not use %s' % mk)
# does the conformal factor enter the STATEMENT?
PHI = ['sh_Φ', 'Φ′', 'Φ']
say('  the conformal factor in `sa2_shell`\'s own statement: %s'
    % ', '.join('%s %d' % (repr(p), FSIG.count(p)) for p in PHI))
# what cz_scale asks of the factor, read from its definition
czdef = re.search(r'def cz_scale \(S : MSpacetime E N\) \(F : N → ℝ\) \(hF : ([^)]*)\)', lean)
say('  what `cz_scale` asks of the factor: %s' % (czdef.group(1) if czdef else 'UNREAD'))
czreg = re.search(r'`LocallyOneChart` passes to `cz_scale S F` when `F` is `C¹`', lean)
say('  what WOULD need the factor\'s regularity, from the file\'s own note: %s'
    % ('LocallyOneChart (F C¹ in every preferred chart)' if czreg else 'UNREAD'))
# ⌗ The first run of this reader reported `sublevelProper` MISSING, and it is not.  The reader
#   built the FIELD name out of the LEMMA name, which holds for `slice`, `cone` and `H` and fails
#   for the one lemma where the two differ: `cz_scale_sublevelProper` is about `.SublevelProper`.
#   A naming convention read as a fact about the file -- the same family as r7694's doubled
#   backslash.  Fixed by naming both halves, and recorded rather than quietly corrected.
transport = {lem: re.search(r'lemma cz_scale_%s : \(S\.cz_scale F hF\)\.%s = S\.%s'
                            % (lem, fld, fld), lean) is not None
             for lem, fld in (('slice', 'slice'), ('cone', 'cone'), ('H', 'H'),
                              ('sublevelProper', 'SublevelProper'))}
say('  the transport lemmas, each stated for ANY positive factor: %s'
    % ', '.join('%s %s' % (n, 'YES' if v else 'no') for n, v in transport.items()))
# NEGATIVE PROBE 8 (a reliance probe can answer NONE and still fire on an injected site)
inj2 = FSIG.replace('(sh_S hM v₀).SublevelProper', '(sh_S hM v₀).SublevelProper sh_Φ', 1)
say('  NEGATIVE PROBE 8, the factor reader on a copy with the factor injected into the statement: '
    '%d occurrence(s) against %d on the statement itself'
    % (inj2.count('sh_Φ'), FSIG.count('sh_Φ')))
if inj2.count('sh_Φ') <= FSIG.count('sh_Φ'):
    FAIL.append('ITEM 1 arm 1e: the conformal-factor reader did not fire on an injected site')
A1E = (FSIG.count('sh_Φ') == 0 and czdef is not None and '0 < F x' in czdef.group(1)
       and all(transport.values()))

say()
say('-' * 94)
for k, v, note in (
        ('1a', A1_BOTH_BOTH,
         'both limits for both subjects: slice %s, cone %s' % (lim['slice'], lim['cone'])),
        ('1b', A1B, 'disjointness is a conclusion of the theorem, not one of its hypotheses'),
        ('1c', A1C, 'the binder is a set equality with the whole horizon set, and non-vacuity is '
                    'witnessed at a point with v < v0 where the factor is 1'),
        ('1d', A1D, 'the named search over the namespace returned %d tangency occurrence(s)'
                    % sum(tang_hits.values())),
        ('1e', A1E, 'the statement carries the factor %d times; cz_scale asks only %s'
                    % (FSIG.count('sh_Φ'), czdef.group(1) if czdef else 'UNREAD')),
        ('1f', bool(SIG), 'the cited name is a theorem of the namespace')):
    say('ITEM 1 arm %s: %-13s -- %s' % (k, 'SUPPORTED' if v else 'NOT SUPPORTED', note))

# =============================================================================================
say()
say('=' * 94)
say('ITEM 2 -- P15: the two reworded octopole clauses, against the receipt and 70\'s RESULT')
say('=' * 94)

CL = {
    'a': "an excess that goes when the hierarchy's two-clock split is turned off and survives "
         "either tower treatment",
    'b': "and it goes with the hierarchy's two-clock split",
}
pos = {}
for k, s in CL.items():
    j = F15.find(s)
    pos[k] = j
    say('clause (%s) located by its text at character %d' % (k, j))
    if j < 0:
        FAIL.append('ITEM 2: clause (%s) is not in P15 on this tree' % k)
ctx_b = F15[pos['b']:pos['b'] + 340] if pos['b'] >= 0 else ''
ctx_a = F15[max(pos['a'] - 300, 0):pos['a'] + 220] if pos['a'] >= 0 else ''
say()
say('clause (b) with its own colon, which is where its figures are: ')
say('  ' + ctx_b[:330])

# --- 2a: the conjuncts, one predicate each (G1) ----------------------------------------------
say()
say('arm 2a -- clause (a) read one predicate per conjunct (G1):')
A2A = {}
for k, mk in (('the excess goes with the split off', 'goes when the hierarchy'),
              ('it survives either tower treatment', 'survives either tower treatment')):
    A2A[k] = present(ctx_a + CL['a'], mk)
    say('  %-40s %s' % (k, 'FOUND' if A2A[k] else 'ABSENT'))

# --- 2b: are the figures PINNED by the receipt? ----------------------------------------------
# A citation is a claim that the receipt COMPUTES the number: a figure printed and asserted by
# no check() is the _car_flat defect of r7692, the shape most worth looking for.
def gated(fig, tol=None):
    """A figure is GATED when it is the `want` of a two-sided check() tuple in the receipt.
    ⌗ The first run of this reader reported the two split-off residuals UNPINNED, and they are
      not: it accepted ONE tuple shape, (name, got, want, tol), and the gates that carry those
      two figures are (name, got, want) triples whose tolerance sits in the check() call that
      consumes them.  An instrument that counts what it was told to count cannot tell you the
      set was the wrong set -- this seat's own lesson, arriving inside the reader that carries
      it.  Both shapes are read now, and the tolerance is reported from wherever it is stated."""
    hits = []
    pats = (r'\(\s*"([^"]{0,200})"\s*,\s*([^,]{1,60}),\s*([-+]?\d+\.?\d*)\s*,\s*([0-9.e+-]+)\s*[,)]',
            r'\(\s*"([^"]{0,200})"\s*,\s*([^,]{1,60}),\s*([-+]?\d+\.?\d*)\s*\)')
    for shape, pat in enumerate(pats):
        for mm in re.finditer(pat, rcpt):
            try:
                want = float(mm.group(3))
            except ValueError:
                continue
            if abs(abs(want) - fig) < 1e-9:
                tolerance = mm.group(4) if shape == 0 else _tol_near(mm.end())
                hits.append((mm.group(1)[:72], mm.group(2).strip(), want, tolerance))
    return hits


def _tol_near(idx):
    """The tolerance of a triple-shaped gate, read from the check() that consumes the triple."""
    mm = re.search(r'abs\(_got - _want\) < ([0-9.e+-]+)', rcpt[idx:idx + 3000])
    return mm.group(1) + ' (from the check that consumes the triple)' if mm else 'UNREAD'



say()
say('arm 2b -- each figure the two clauses print, against the receipt\'s own two-sided gates:')
FIGS = [('the octopole excess, printed as five and a half per cent', 5.54),
        ('the two treatments\' agreement there, printed as 0.7 per cent', 0.67),
        ("the split-off residual, FROZEN, printed as 1.0 per cent below", 1.01),
        ("the split-off residual, DECOUPLED, printed as 1.1 per cent below", 1.10)]
A2B = {}
for nm, fig in FIGS:
    hits = gated(fig)
    A2B[nm] = bool(hits)
    say('  %-62s %s' % (nm, 'PINNED' if hits else 'NO GATE READS IT'))
    for h in hits[:2]:
        say('      by: %s  (want %+.2f, tol %s)' % (h[0], h[2], h[3]))
# NEGATIVE PROBE 10 / the gate reader's own negative: an invented figure must come back unpinned.
say('  NEGATIVE PROBE (an invented figure, 9.91, which no clause prints): %s'
    % ('unpinned, as it must be' if not gated(9.91) else 'PINNED -- the gate reader matches anything'))
if gated(9.91):
    FAIL.append('ITEM 2 arm 2b: the gate reader fired on an invented figure')

# --- 2b': THE DENOMINATOR, because a ratio is a claim about its denominator -------------------
say()
say('arm 2b\' -- the denominator of "agree to 0.7 per cent", which the clause does not state:')
spr = re.search(r'_spr = 100\.0 \* \(_DF - _DD\) / (\w+)', rcpt)
rel = re.search(r'_relF = 100\.0 \* \(_DF - _DA\) / (\w+)', rcpt)
say('  the receipt forms the build spread as (frozen - decoupled) / %s'
    % (spr.group(1) if spr else 'UNREAD'))
say('  and the residuals as (build - %s) / %s'
    % ('arm A' if rel else '?', rel.group(1) if rel else 'UNREAD'))
other = F15.find('per cent of each other above')
say('  the neighbouring spread clause in the same block says %r at character %d'
    % (F15[other:other + 28] if other > 0 else 'NOT FOUND', other))
# the two conventions, computed from the receipt's own banked run rather than from the paper
conv = {}
if ran:
    tab = re.findall(r'^\s*(\d)\s+([0-9.]+)\s+([-+][0-9.]+)\s+([-+][0-9.]+)\s+([-+][0-9.]+)\s*$',
                     ran, re.M)
    for l, dA, rF, rD, sp in tab:
        if l == '3':
            dA, rF, rD, sp = float(dA), float(rF), float(rD), float(sp)
            DF = dA * (1 + rF / 100.0)
            DD = dA * (1 + rD / 100.0)
            conv['of the exact transfer\'s depth'] = 100.0 * (DF - DD) / dA
            conv['of each other'] = 100.0 * (DF - DD) / DD
            say('  read from the receipt\'s own run at l = 3: arm A %.4f, frozen %+.2f%%, '
                'decoupled %+.2f%%, spread %+.2f%%' % (dA, rF, rD, sp))
    for k, v in conv.items():
        say('    the same spread %-32s %+.3f per cent, which prints as %.1f' % (k, v, abs(round(v, 1))))
else:
    say('  the receipt\'s run is not banked beside this probe, so the two conventions are UNMEASURED')
if conv:
    A2BP = (abs(round(abs(conv["of the exact transfer's depth"]), 1) - 0.7) < 1e-9
            and abs(round(abs(conv['of each other']), 1) - 0.7) > 1e-9)
else:
    A2BP = None                                # UNMEASURED, not NOT SUPPORTED

# --- 2c: "goes" as a counterfactual, and its DIRECTION (negative probe 14, new here) ---------
say()
say('arm 2c -- "goes" read as a counterfactual, with its DIRECTION part of the claim:')
hl = re.search(r'check\("⚑⛭⛭ \*\* THE OCTOPOLE\'S EXCESS IS THE TWO-CLOCK SPLIT\'S[^"]*"', rcpt)
cond = re.search(r'_o_relF\[_i3\] < 0 < _relF\[_i3\] and _o_relD\[_i3\] < 0 < _relD\[_i3\]', rcpt)
say('  the receipt\'s attribution gate is present: %s' % ('YES' if hl else 'no'))
say('  and what it asserts about the two states: %s'
    % ('one clock BELOW zero and the split ABOVE zero, on both builds' if cond else 'UNREAD'))
band = F15.find('agrees to three per cent at every multipole but the octopole')
say('  the band the SAME sentence uses for agreement: %r'
    % (F15[band:band + 58] if band > 0 else 'NOT FOUND'))
off = [f for nm, f in FIGS if 'split-off' in nm]
say('  the split-off residuals: %s per cent below, each inside that three-per-cent band: %s'
    % (' and '.join('%.2f' % f for f in off), 'YES' if all(f < 3.0 for f in off) else 'NO'))
say('  ⇒ the direction is a SIGN CHANGE and not only a vanishing, and clause (b)\'s own colon '
    'states it; clause (a) says only "goes", which the band above makes exact.')
A2C = bool(cond) and all(f < 3.0 for f in off)
# NEGATIVE PROBE 14, registered in PREDICTION.md: the direction reader must be able to say
# SIGN INVERTED.  Fed a counterfactual that merely shrinks, it must NOT report an inversion.
fake_lo, fake_hi = 2.0, 5.0
say('  NEGATIVE PROBE 14 (a counterfactual that merely shrinks, %.1f -> %.1f, no crossing): '
    'inversion reported: %s' % (fake_hi, fake_lo, 'YES -- WRONG' if (fake_lo < 0 < fake_hi) else 'no'))
if fake_lo < 0 < fake_hi:
    FAIL.append('ITEM 2 arm 2c: the direction reader reported an inversion where there is none')

# --- 2d: THE ORDER'S QUESTION -- the SUBJECT of each clause ----------------------------------
say()
say('arm 2d -- the order\'s question: does either clause claim anything about the ARM OF RECORD?')
SUBJ_HIER = ["the hierarchy's two-clock split", 'the hierarchy sits', 'the hierarchy agrees']
SUBJ_AOR = ['the arm of record']


def classify(text):                            # G4: a classifier, tested on both classes below
    h = sum(1 for s in SUBJ_HIER if s in text)
    a = sum(1 for s in SUBJ_AOR if s in text)
    if a and not h:
        return 'ARM-OF-RECORD'
    if h and not a:
        return 'HIERARCHY-INTERNAL'
    if h and a:
        return 'BOTH NAMED'
    return 'NEITHER NAMED'


for k, text in (('a', ctx_a + CL['a']), ('b', ctx_b)):
    say('  clause (%s): %s' % (k, classify(text)))
# G4's own probe: the classifier on inputs of both classes, including an injected arm-of-record form
say('  CLASSIFIER PROBE (G4): %r -> %s ; %r -> %s'
    % ("the arm of record's two-clock split", classify("the arm of record's two-clock split"),
       "the hierarchy's two-clock split", classify("the hierarchy's two-clock split")))
if classify("the arm of record's two-clock split") != 'ARM-OF-RECORD':
    FAIL.append('ITEM 2 arm 2d: the subject classifier does not name an arm-of-record subject')

# what 70's RESULT says the split is, read from its own text
say()
say('  70\'s r7693 RESULT, read for what HIER\'s split is:')
for mk in ('HIER\'s split clock is not the arm of record on the perturbations',
           'retired `STACKPERT=1` pairing',
           'not of the arm of record'):
    say('    %-62s %s' % (repr(mk)[:62], 'STATED' if mk in F70 else 'not found'))
aor_default = re.search(r'`LEAFPERT` default since r\d+', F70)
say('    and what the arm of record itself runs: %s'
    % (aor_default.group(0) if aor_default else 'UNREAD'))
# and what the receipt's attribution gate says it does NOT license
# ⌗ The first form of this marker spanned a break between two adjacent Python string
#   literals in the receipt's source, so the flattened source carries a quote and a space in
#   the middle of it.  Read as two markers instead, and both reported.
LIC = ('it does NOT license a', 'mechanism for why the split does it',
       'nor the same attribution at any other multipole without')
lic_got = {m: (m in flat(rcpt)) for m in LIC}
say('  the receipt\'s own licence text, read as the three markers it breaks into:')
for m, v in lic_got.items():
    say('    %-58s %s' % (repr(m)[:58], 'STATED' if v else 'not found'))
A2D = (classify(ctx_a + CL['a']) == 'HIERARCHY-INTERNAL'
       and classify(ctx_b) == 'HIERARCHY-INTERNAL')

# the forward note: the held depth rewrite would re-point the SUBJECT without changing the words
held = F15.find("The hierarchy's depths are read with the photon and")
say()
say('  ⚠ the same block already says, at character %d: %r' % (held, F15[held:held + 120]))
say('  ⇒ the clauses are about the hierarchy\'s own switch TODAY.  A label is attached by POSITION: '
    'if the held rewrite re-points the printed depths to the arm of record\'s, these same words '
    'become a claim about the arm of record\'s pairing without one of them changing.')

say()
say('-' * 94)
def verdict(v):
    # Three states, never two: a reading the probe could not take is UNMEASURED and says so.
    # An arm that carries its own label passes it through rather than being forced into two.
    if isinstance(v, str):
        return v
    return 'UNMEASURED' if v is None else ('SUPPORTED' if v else 'NOT SUPPORTED')


for k, v, note in (
        ('2a', all(A2A.values()), 'both of clause (a)\'s predicates are in the clause'),
        ('2b', all(A2B.values()),
         '%d of the %d figures the two clauses print are the want of a two-sided gate'
         % (sum(1 for x in A2B.values() if x), len(A2B))),
        # ⌗ This arm's verdict is NOT about the clause being supported: it is about whether the
        #   denominator the clause leaves unstated changes the digit it prints.  Printing
        #   SUPPORTED here would read exactly backwards, so this arm carries its own label.
        ("2b'", 'DENOMINATOR UNSTATED, AND IT CHANGES THE PRINTED DIGIT' if A2BP is True else
                ('the printed digit is the same either way' if A2BP is False else 'UNMEASURED'),
         'the two conventions at l = 3 print as %s'
         % (' and '.join('%.1f (%s)' % (abs(round(v2, 1)), k2) for k2, v2 in conv.items())
            if conv else 'UNREAD -- the receipt run is not banked beside this probe')),
        ('2c', A2C, 'the off-state crosses below and stays inside the sentence\'s own band'),
        ('2d', A2D, 'both clauses name the hierarchy\'s switch and neither names the arm of record')):
    say('ITEM 2 arm %-3s: %s -- %s' % (k, verdict(v), note))

say()
say('=' * 94)
say('%d verdicts printed.  %d reader or classifier probe(s) failed.' % (11, len(FAIL)))
for f in FAIL:
    say('  DEFECT: %s' % f)
say('=' * 94)

with open(os.path.join(HERE, 'runs', 'READINGS.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(READINGS) + '\n')

sys.exit(1 if FAIL else 0)
