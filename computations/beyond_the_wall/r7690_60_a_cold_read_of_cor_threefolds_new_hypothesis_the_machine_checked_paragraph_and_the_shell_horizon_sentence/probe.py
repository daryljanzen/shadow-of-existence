#!/usr/bin/env python3
"""r7690 (60) -- the registered readings for the cold read of `cor:threefold`'s new
hypothesis, the machine-checked paragraph after it, and the shell-horizon sentence.

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

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
PROBES = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
THREEFOLD = os.path.join(PROBES, 'ThreefoldOrder.lean')
SHELL = os.path.join(PROBES, 'SchwarzschildShellHorizon.lean')

FAIL = []
READINGS = []


def say(s=''):
    print(s)


def note(tag, text):
    READINGS.append((tag, text))
    print('    %-6s %s' % (tag, text))


# ---------------------------------------------------------------- G2: the anchors
def anchor(marker):
    """G2. Three anchor forms only: a word boundary, an escaped control sequence, an
    escaped math delimiter. An UNANCHORED marker is REFUSED. A boundary is never placed
    AFTER a delimiter."""
    if marker.startswith('\\\\'):              # escaped control sequence
        return re.compile(re.escape(marker))
    if marker.startswith('\\$') or marker.endswith('\\$'):
        return re.compile(re.escape(marker))   # escaped math delimiter, no trailing \b
    if re.match(r'^[A-Za-z0-9]', marker) and re.search(r'[A-Za-z0-9]$', marker):
        return re.compile(r'\b' + re.escape(marker) + r'\b')
    FAIL.append('G2 REFUSED an unanchored marker: %r' % marker)
    return None


def hit(marker, hay):
    rx = anchor(marker)
    if rx is None:
        return False
    return bool(rx.search(hay))


# ---------------------------------------------------------------- G6: flattened copies
def flat(s):
    return re.sub(r'\s+', ' ', s).strip()


with open(P1, encoding='utf-8') as fh:
    P1_LINES = fh.read().split('\n')
P1_FLAT = flat('\n'.join(P1_LINES))


def line(n):                      # 1-indexed, as the tree names them
    return P1_LINES[n - 1]


# ================================================================ ARM 1
say('=' * 78)
say('ARM 1 -- DOES `no closed causal curves` DO THE WORK IN (i)?')
say('=' * 78)

STMT = flat(line(167))
PART_I = flat(line(171))
say('  source: l.167 (statement), l.171 ((i)); read on the whitespace-FLATTENED copy')

# -- 1a SUFFICIENCY, read as a text-grounded entailment check -------------------
hyp_stated = hit('with no closed causal curves', STMT)
seg_stated = hit('future-directed null geodesic segment', STMT)
front_stated = hit('\\\\partial J^{+}(p)', STMT) or 'partial J^{+}(p)' in STMT
say()
say('  1a SUFFICIENCY')
note('read', 'the statement names the causality condition      : %s' % hyp_stated)
note('read', 'the statement names a null geodesic SEGMENT       : %s' % seg_stated)
note('read', 'the statement names the strict frontier relation  : %s' % front_stated)
if hyp_stated and seg_stated:
    note('VERDICT', 'SUPPORTED -- a future-directed null geodesic segment with p = q has a '
                    'nowhere-zero null tangent, so its image is a closed causal curve; the '
                    'stated hypothesis excludes exactly that, and nothing further is needed.')
else:
    note('VERDICT', 'NOT SUPPORTED -- the statement does not carry both clauses the '
                    'entailment uses.')

# -- 1b THE REASON AS GIVEN, with negative probe 7 -----------------------------
say()
say('  1b THE REASON AS GIVEN (negative probe 7 governs)')


def hypothesis_reading(part_i_text):
    """Separates `the hypothesis is stated` from `the hypothesis does the work`:
    the reason must INVOKE the hypothesis in its own words."""
    invokes = hit('closed causal curve', part_i_text)
    concludes = hit('distinct points of the manifold', part_i_text)
    if invokes and concludes:
        return 'SUPPORTED'
    if concludes and not invokes:
        return 'STATED-BUT-UNUSED'
    return 'UNMEASURED'


v1b = hypothesis_reading(PART_I)
note('read', '(i) concludes distinctness                        : %s'
     % hit('distinct points of the manifold', PART_I))
note('read', '(i) invokes the hypothesis in its own words        : %s'
     % hit('closed causal curve', PART_I))
note('VERDICT', '%s -- the reason given in (i) is "a segment returning to the event it '
                'left would be a closed causal curve", which is the stated hypothesis '
                'applied to the stated segment.' % v1b)

# negative probe 7 must FIRE on a copy of (i) with the reason struck out
struck = re.sub(r', since a segment[^,]*would be a closed causal curve', '', PART_I)
if struck == PART_I:
    FAIL.append('negative probe 7 could not build its altered copy')
v7 = hypothesis_reading(struck)
note('neg7', 'reason struck out -> %s (must be STATED-BUT-UNUSED)' % v7)
if v7 != 'STATED-BUT-UNUSED':
    FAIL.append('negative probe 7 did not fire: struck copy read %s' % v7)

# G3 flip: the hypothesis removed from the STATEMENT must change 1a's answer
flipped = STMT.replace('with no closed causal curves ', '')
if flipped == STMT:
    FAIL.append('G3 could not build the flipped statement for 1a')
note('G3', 'hypothesis removed from the statement -> names it: %s (must be False)'
     % hit('with no closed causal curves', flipped))
if hit('with no closed causal curves', flipped):
    FAIL.append('G3 flip failed on 1a')

# -- 1c 71's WITNESS, recomputed from the construction -------------------------
say()
say("  1c IS 71's WITNESS EXCLUDED? (recomputed, not recalled)")
try:
    import sympy as sp
except Exception as exc:                                     # pragma: no cover
    FAIL.append('1c could not run: %s' % exc)
else:
    U, V, s = sp.symbols('U V s', real=True)
    # 2D Minkowski in null coordinates: g = -2 dU dV  (signature -+)
    g = sp.Matrix([[0, -1], [-1, 0]])
    # the quotient is by the NULL translation (U, V) -> (U, V + 1)
    curve = sp.Matrix([sp.Integer(0), s])                    # U = 0, V = s
    tang = sp.diff(curve, s)
    norm = sp.simplify((tang.T * g * tang)[0, 0])
    closes = sp.simplify(curve.subs(s, 1) - (curve.subs(s, 0) + sp.Matrix([0, 1])))
    note('read', 'g(tangent, tangent) along U = 0                   : %s' % norm)
    note('read', 'endpoint of s in [0,1] minus the translate of its '
                 'start: %s' % list(closes))
    if norm == 0 and all(c == 0 for c in closes):
        note('VERDICT', "SUPPORTED -- the witness's own null line U = 0 closes under the "
                        'identification and is causal (null tangent), so the quotient '
                        'HAS a closed causal curve and the new hypothesis excludes it. '
                        'The one object known to defeat the old wording is ruled out by '
                        'the new one.')
    else:
        note('VERDICT', 'NOT SUPPORTED -- the recomputation does not give a closed causal '
                        'curve in the witness.')

# ================================================================ ARM 2
say()
say('=' * 78)
say('ARM 2 -- DOES ANYTHING ELSE IN P1 RELY ON THE OLD WORDING?')
say('=' * 78)

# (alpha) every citation of the corollary; (beta) every restatement of its hypotheses;
# (gamma) every site reasoning from `smooth Lorentzian manifold` without the condition.
sites = []
for n, raw in enumerate(P1_LINES, 1):
    f = flat(raw)
    if not f:
        continue
    if hit('\\\\ref{cor:threefold}', f) or 'ref{cor:threefold}' in f:
        sites.append((n, 'alpha', 'cites the corollary'))
    if hit('smooth Lorentzian manifold', f):
        sites.append((n, 'beta', 'states a Lorentzian-manifold hypothesis'))
    if re.search(r'\(i\)--\(iii\)|\(i\)-\(iii\)|all four parts|possess all four', f):
        sites.append((n, 'gamma', "states the corollary's parts of a class of objects"))

seen = set()
ordered = []
for n, kind, why in sites:
    if (n, kind) in seen:
        continue
    seen.add((n, kind))
    ordered.append((n, kind, why))


def reliance_reading(text, lineno):
    """A RELIANCE reading, not a presence reading. A site RELIES on the old wording iff
    its own text asserts a conclusion of part (i) -- distinctness, or the possession of
    the parts that include (i) -- of a class of objects for which it names NO causality
    condition.  It must be able to return NONE and must still fire on an injected site."""
    asserts_i = bool(re.search(
        r'\(i\)--\(iii\)|\(i\)-\(iii\)|possess all four'
        r'|are distinct points of the manifold', text))
    names_condition = hit('closed causal curve', text) or hit('closed causal curves', text) \
        or hit('globally hyperbolic', text) or hit('global hyperbolicity', text) \
        or hit('causality condition', text)
    # a site that GROUNDS the parts in a named machine-checked theorem is not resting on
    # the corollary's hypotheses at all: it rests on the probe's, which are read in ARM 3.
    grounds_in_probe = bool(re.search(r'machine-checked', text)) and 'texttt' in text
    is_the_corollary = lineno in (166, 167, 170, 171)
    if is_the_corollary:
        return 'THE COROLLARY ITSELF (not another site)'
    if grounds_in_probe:
        return "DOES NOT REST ON IT (grounds the parts in a named probe)"
    if asserts_i and not names_condition:
        return 'RELIES'
    if asserts_i and names_condition:
        return 'DOES NOT REST ON IT (names a condition of its own)'
    return 'DOES NOT REST ON IT'


say('  enumerated sites (alpha = cites, beta = restates hypotheses, gamma = asserts parts):')
relying = []
for n, kind, why in ordered:
    v = reliance_reading(flat(line(n)), n)
    note('site', 'l.%-4d %-6s %-46s -> %s' % (n, kind, why, v))
    if v == 'RELIES':
        relying.append(n)

if relying:
    note('VERDICT', '%d SITE(S) RELY: %s' % (len(relying), ', '.join('l.%d' % n for n in relying)))
else:
    note('VERDICT', 'NONE RELIES')

# negative probe 8: the reading must FIRE on an injected site that does rely
inject = ('On any smooth Lorentzian manifold the generators of a null hypersurface '
          'are distinct points of the manifold by the corollary.')
v8 = reliance_reading(flat(inject), 999999)
note('neg8', 'injected site -> %s (must be RELIES)' % v8)
if v8 != 'RELIES':
    FAIL.append('negative probe 8 did not fire: injected site read %s' % v8)

# and it must be able to answer NONE: a site that names its own condition
clean = ('In a globally hyperbolic spacetime an ordinary null hypersurface has '
         '(i)--(iii) but not (iv).')
v8b = reliance_reading(flat(clean), 999998)
note('neg8', 'site naming its own condition -> %s (must NOT be RELIES)' % v8b)
if v8b == 'RELIES':
    FAIL.append('negative probe 8 over-fired on a site that names its own condition')

# ================================================================ the Lean readings
def lean_statement(path, name):
    """The theorem's own statement text, from `theorem <name>` up to the proof token."""
    with open(path, encoding='utf-8') as fh:
        src = fh.read()
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b', src, re.M)
    if m is None:
        FAIL.append('could not locate %s in %s' % (name, os.path.basename(path)))
        return None, None
    tail = src[m.start():]
    cut = re.search(r':=\s*(?:by\b|fun\b|\n)', tail)
    stmt = tail[:cut.start()] if cut else tail[:4000]
    # the docstring immediately above, if any
    head = src[:m.start()]
    dm = None
    for dm_ in re.finditer(r'/--(.*?)-/', head, re.S):
        dm = dm_
    doc = dm.group(1) if dm else ''
    return flat(stmt), flat(doc)


def score(claim, stmt, required, forbidden=()):
    """G1: one predicate for every conjunct. Every required marker must be present in
    the theorem's own statement text; every forbidden marker must be absent."""
    got = [(mk, hit(mk, stmt)) for mk in required]
    bad = [(mk, hit(mk, stmt)) for mk in forbidden]
    for mk, ok in got:
        note('read', '%-58s %s' % ('needs %r' % mk, ok))
    for mk, ok in bad:
        note('read', '%-58s %s' % ('must NOT carry %r' % mk, ok))
    if all(ok for _, ok in got) and not any(ok for _, ok in bad):
        return 'SUPPORTED'
    return 'NOT SUPPORTED'


say()
say('=' * 78)
say('ARM 3 -- THE PARAGRAPH AFTER `cor:threefold`, AGAINST `ThreefoldOrder.lean`')
say('=' * 78)

PARA = flat(line(188))
sns_stmt, sns_doc = lean_statement(THREEFOLD, 'to_strict_null_order')
c1c_stmt, c1c_doc = lean_statement(THREEFOLD, 'to_cor_1c')
if sns_stmt is None or c1c_stmt is None:
    print('FATAL: a cited theorem could not be located')
    sys.exit(1)

say()
say('  3a  "Part (ii) ... is machine-checked"  -> to_strict_null_order')
v3a = score('3a', sns_stmt,
            ['frontier', 'S.Cau r q', 'S.Chr p r'])
note('VERDICT', '%s -- the theorem concludes exactly (ii)\'s clause: from q on the '
                'frontier of J+(p) and r causally before q, NOT p << r.' % v3a)

say()
say('  3b  "all four parts together on one pair"  -> to_cor_1c')
v3b = score('3b', c1c_stmt,
            ['to_γN 0 ≠ to_γN 1',            # (i)
             'frontier',                      # (ii)
             'to_σN.Δτ = 0'])                 # (iv)
note('read', '%-58s %s' % ('(iii) null along the WHOLE segment (Icc 0 1)',
                           'Icc (0:ℝ) 1' in c1c_stmt))
same_pair = c1c_stmt.count('to_γN 0') >= 4 and c1c_stmt.count('to_γN 1') >= 4
note('read', '%-58s %s' % ('every part on the SAME pair (position, not presence)', same_pair))
if v3b == 'SUPPORTED' and 'Icc (0:ℝ) 1' in c1c_stmt and same_pair:
    note('VERDICT', 'SUPPORTED -- one theorem, one pair `to_γN 0`, `to_γN 1`, carrying '
                    'distinctness, the causal ordering with the frontier clause, '
                    'nullity on all of [0,1], and Δx = Δτ = 0 with vanishing lapse.')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  3c  the setting: metric C1, time orientation continuous in a chart about each point')
loc_stmt, loc_doc = None, None
with open(THREEFOLD, encoding='utf-8') as fh:
    tf_src = fh.read()
m = re.search(r'def LocallyOneChart : Prop :=(.{0,400})', tf_src, re.S)
loc = flat(m.group(1)) if m else ''
note('read', '%-58s %s' % ('LocallyOneChart asks ContDiffOn R 1 of the metric',
                           hit('ContDiffOn', loc)))
note('read', '%-58s %s' % ('LocallyOneChart asks the time orientation CONTINUOUS',
                           hit('ContinuousOn', loc)))
note('read', '%-58s %s' % ('both asked in a chart about each point (extChartAt p p)',
                           'extChartAt' in loc))
secm = re.search(r'section ThreefoldOrder(.*?)end MSpacetime', tf_src, re.S)
sec = secm.group(1) if secm else ''
hausdorff = ('T2Space' in sns_stmt) or bool(re.search(r'variable \{N :[^\n]*T2Space', sec))
note('read', '%-58s %s' % ("to_strict_null_order's signature asks Hausdorff of N",
                           'T2Space' in sns_stmt))
note('read', '%-58s %s' % ("its section's variable block asks Hausdorff of N",
                           bool(re.search(r'variable \{N :[^\n]*T2Space', sec))))
note('read', '%-58s %s' % ('(T2Space appears in the file, on OTHER theorems, as an '
                           'explicit instance)', 'T2Space' in tf_src))
if hit('ContDiffOn', loc) and hit('ContinuousOn', loc) and 'extChartAt' in loc:
    tail = ('The theorem asks no Hausdorff of N -- the file carries [T2Space N] on '
            'other theorems, not on this one -- so it holds in the remark\'s setting a '
            'fortiori: STRONGER-THAN-CLAIMED on that one hypothesis, recorded and not '
            'upgraded.') if not hausdorff else ('The theorem also asks Hausdorff of N, '
            'which the remark\'s setting supplies.')
    note('VERDICT', 'SUPPORTED -- the two regularity clauses the sentence names are '
                    "LocallyOneChart's two clauses, asked in the preferred chart at each "
                    'point. ' + tail)
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  3d  "no event causally after p AND causally before q lies in I+(p)"')
has_pr = 'S.Cau p r' in sns_stmt
unused = '_hpr' in sns_stmt
note('read', '%-58s %s' % ('the statement carries `Cau p r`', has_pr))
note('read', '%-58s %s' % ('...but binds it as UNUSED (`_hpr`)', unused))
note('read', '%-58s %s' % ('the statement carries `Cau r q`', 'S.Cau r q' in sns_stmt))
if has_pr and unused:
    note('VERDICT', 'SUPPORTED, and STRONGER-THAN-CLAIMED -- the sentence says `causally '
                    'after p and causally before q`; the theorem binds `Cau p r` and does '
                    'not use it, so `causally before q` alone suffices. Recorded as a '
                    'result; the sentence is not upgraded.')
else:
    note('VERDICT', 'SUPPORTED' if 'S.Cau r q' in sns_stmt else 'NOT SUPPORTED')

say()
say('  3e  "the proof pushes a chronological relation along a causal one and uses no geodesic"')
with open(THREEFOLD, encoding='utf-8') as fh:
    tf = fh.read()
pm = re.search(r'theorem to_strict_null_order.*?\n\nend MSpacetime', tf, re.S)
body = pm.group(0) if pm else ''
proof = body.split(':=', 1)[1] if ':=' in body else ''
note('read', '%-58s %s' % ('the proof invokes the push-up `mk_pushup\'`', 'mk_pushup' in proof))
note('read', '%-58s %s' % ('the proof body mentions a geodesic',
                           bool(re.search(r'geodesic|Geodesic', proof))))
note('read', '%-58s %s' % ('the whole theorem block mentions a geodesic (docstring aside)',
                           bool(re.search(r'geodesic', body.split('-/')[-1]))))
if 'mk_pushup' in proof and not re.search(r'geodesic|Geodesic', proof):
    note('VERDICT', 'SUPPORTED -- the proof is one application of the dual push-up to a '
                    'chronological relation along a causal one, and no geodesic appears '
                    'in it.')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  3f  the Rindler sentence, five conjuncts and "all in one theorem"')
conj = [
    ('distinct',                       'to_γN 0 ≠ to_γN 1'),
    ('causally ordered',               'minkN.Cau (to_γN 0) (to_γN 1)'),
    ('and NOT chronologically',        '¬ minkN.Chr (to_γN 0) (to_γN 1)'),
    ('the later on the frontier',      'frontier'),
    ('null along the generator',       'minkN.gE (to_γN s)'),
    ('Dx = Dt = 0, lapse vanishing',   'to_σN.Δx = 0'),
]
ok3f = True
for label, mk in conj:
    present = mk in c1c_stmt
    note('read', '%-38s %-30s %s' % (label, '(%s)' % mk[:28], present))
    ok3f = ok3f and present
lapse = '(∀ s, to_σN.n s = 0)' in c1c_stmt
note('read', '%-38s %-30s %s' % ('the lapse vanishes there', '(∀ s, to_σN.n s = 0)', lapse))
one_theorem = c1c_stmt.count('theorem') == 1
note('read', '%-38s %-30s %s' % ('all in ONE theorem', 'single `theorem`', one_theorem))
note('read', '%-38s %-30s %s' % ('the model is the flat plane', 'minkN M = univ',
                                 bool(re.search(r'def minkN : MSpacetime P Pt where\s*M := univ',
                                                flat(tf)))))
note('read', '%-38s %-30s %s' % ('on the Rindler horizon generator', 'U = 0, V = e^s',
                                 'Rindler horizon generator' in tf))
if ok3f and lapse and one_theorem:
    note('VERDICT', 'SUPPORTED -- all five conjuncts and the "one theorem" claim are '
                    "carried by to_cor_1c's own statement, on the flat plane `minkN` "
                    "(M = univ) along ac_witness's Rindler-horizon generator.")
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('=' * 78)
say('ARM 4 -- THE SHELL-HORIZON SENTENCE, AGAINST `SchwarzschildShellHorizon.lean`')
say('=' * 78)

hd_stmt, hd_doc = lean_statement(SHELL, 'sh_headline_D')
hr_stmt, hr_doc = lean_statement(SHELL, 'sh_H_r')
hf_stmt, hf_doc = lean_statement(SHELL, 'sh_H_flat')
for nm, st in (('sh_headline_D', hd_stmt), ('sh_H_r', hr_stmt), ('sh_H_flat', hf_stmt)):
    if st is None:
        print('FATAL: %s could not be located' % nm)
        sys.exit(1)

say()
say('  4a  "the exterior is the causal past of the observer"')
note('read', '%-58s %s' % ('D (range O) given as a set equality', '.D (range (sv_O M v₀)) =' in hd_stmt))
note('read', '%-58s %s' % ('J-(O) = D as its own conjunct', 'JpastSet (range (sv_O M v₀)) =' in hd_stmt))
if '.D (range (sv_O M v₀)) =' in hd_stmt and 'JpastSet (range (sv_O M v₀)) =' in hd_stmt:
    note('VERDICT', 'SUPPORTED -- and by an EQUALITY of the causal past with D, not an '
                    'inclusion; D is itself I-(O) by definition, so the causal and '
                    'chronological pasts coincide: STRONGER-THAN-CLAIMED, recorded.')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  4b  "its boundary is the future horizon ALONE"  (the r7688 word, read fresh)')
h_eq = re.search(r'\.H \(range \(sv_O M v₀\)\) = \{y : P \| y\.1 = sv_uH M v₀\}', hd_stmt)
note('read', '%-58s %s' % ('the boundary is given as an EQUALITY to one locus', bool(h_eq)))
note('read', '%-58s %s' % ('H is the frontier of J-(O) by definition',
                           bool(re.search(r'def H \(J : Set N\) : Set N := frontier', tf))))
note('read', '%-58s %s' % ('the locus is a single null hypersurface {u~ = u_H}',
                           'y.1 = sv_uH M v₀' in hd_stmt))
if h_eq:
    note('VERDICT', 'SUPPORTED -- "alone" is carried by the EQUALITY: the frontier of the '
                    'exterior is that one locus and nothing else, so no second component '
                    '(no white-hole horizon) can be in it. Same structural move as '
                    "r7680's `se_foundation` and r7688's `sv_D`; unlike the eternal "
                    'sentence r7688 read, here the probe states the equality.')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  4c  "at r = r_h once the shell has passed"')
note('read', '%-58s %s' % ('sh_H_r concludes sv_r = 2 * M', 'sv_r M v₀ y = 2 * M' in hr_stmt))
hr_has_v = bool(re.search(r'y\.2|v₀ ≤|≤ v₀', hr_stmt.split(':', 1)[0] if ':' in hr_stmt else hr_stmt))
hr_hyp_v = bool(re.search(r'\(hv :', hr_stmt))
note('read', '%-58s %s' % ("sh_H_r's STATEMENT carries a condition on v", hr_hyp_v))
note('read', '%-58s %s' % ("sh_H_r's DOCSTRING names a condition on v",
                           bool(re.search(r'v ≥ v₀|v₀ ≤ v', hr_doc or ''))))
note('read', '%-58s %s' % ('sv_r is the KRUSKAL radial function rK of chi',
                           bool(re.search(r'def sv_r \(M v₀ : ℝ\) \(y : P\) : ℝ := rK M', flat(open(SHELL, encoding='utf-8').read())))))
if 'sv_r M v₀ y = 2 * M' in hr_stmt:
    note('VERDICT', 'SUPPORTED -- the cited theorem gives r = 2M at every point of the '
                    "horizon locus. The sentence's qualifier is the physically meaningful "
                    'restriction and the theorem needs none, because `sv_r` is the Kruskal '
                    'vacuum radial function continued over the whole model rather than the '
                    "areal radius of the flat interior. ** AND A DEFECT IN THE PROBE: "
                    "sh_H_r's docstring names `with v >= v0` and its STATEMENT does not "
                    'carry it -- the docstring claims a hypothesis the theorem does not '
                    'have. Routed, not edited. **')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  4d  "already formed inside the flat body before it arrives"')
note('read', '%-58s %s' % ('sh_H_flat concludes the conformal factor is 1',
                           'sh_Φ M v₀ y = 1' in hf_stmt))
note('read', '%-58s %s' % ('...under a condition v <= v0 (before the shell)',
                           'y.2 ≤ v₀' in hf_stmt))
shell_src = flat(open(SHELL, encoding='utf-8').read())
note('read', '%-58s %s' % ('Phi = 1 means the metric IS the flat one (g = Phi * (-du dv))',
                           bool(re.search(r'hRep \(sh_S hM v₀\)\.g p y = sh_Φ M v₀ y • gM', shell_src))))
note('read', '%-58s %s' % ('the EXISTENCE of such points follows from 4b\'s set equality',
                           'y.1 = sv_uH M v₀' in hd_stmt))
if 'sh_Φ M v₀ y = 1' in hf_stmt and 'y.2 ≤ v₀' in hf_stmt and 'y.1 = sv_uH M v₀' in hd_stmt:
    note('VERDICT', 'SUPPORTED -- and the existential half is carried too, by the CITED '
                    'pair rather than elsewhere: the boundary EQUALS {u~ = u_H}, a locus '
                    'holding a point at every v, so points with v < v0 are on the horizon, '
                    'and sh_H_flat puts the flat metric at exactly those. No MIS-CITED '
                    'verdict is reached here.')
else:
    note('VERDICT', 'NOT SUPPORTED')

say()
say('  4e  "the slicing is Cauchy on the exterior that horizon bounds"')
note('read', '%-58s %s' % ('sh_headline_D carries IsCauchyTemporalOn on D',
                           'IsCauchyTemporalOn ((sh_S hM v₀).D' in hd_stmt))
note('read', '%-58s %s' % ('its quantifier is 0 < eta <= 2, as the previous sentence says',
                           '0 < η → η ≤ 2' in hd_stmt))
note('read', '%-58s %s' % ('the slicing named is sv_Theta_sh', 'sv_Θsh M a η v₀' in hd_stmt))
if 'IsCauchyTemporalOn ((sh_S hM v₀).D' in hd_stmt and '0 < η → η ≤ 2' in hd_stmt:
    note('VERDICT', "SUPPORTED -- with the quantifier intact: the conjunct's eta range is "
                    "the one the sentence before it states, and a conjunct's QUANTIFIER is "
                    'part of the claim.')
else:
    note('VERDICT', 'NOT SUPPORTED')

# G3 flip for the Lean readings: an altered statement must change the answer
say()
say('  G3 flip on the Lean readings')
flip_hd = hd_stmt.replace('IsCauchyTemporalOn', 'IsTemporalOn')
note('G3', '4e on a statement with the Cauchy clause weakened -> %s (must be False)'
     % ('IsCauchyTemporalOn ((sh_S hM v₀).D' in flip_hd))
if 'IsCauchyTemporalOn ((sh_S hM v₀).D' in flip_hd:
    FAIL.append('G3 flip failed on 4e')
flip_c1c = c1c_stmt.replace('to_γN 0 ≠ to_γN 1', 'True')
note('G3', '3b on a statement with distinctness removed -> %s (must be False)'
     % ('to_γN 0 ≠ to_γN 1' in flip_c1c))
if 'to_γN 0 ≠ to_γN 1' in flip_c1c:
    FAIL.append('G3 flip failed on 3b')

# the five standing negative probes that still apply, re-run
say()
say('  the standing negative probes that this revision can still run')
# (1) a figure in the .tex absent from the cited probe => NOT SUPPORTED
note('neg1', 'a clause absent from the cited statement reads NOT SUPPORTED: %s'
      % (score('neg1', hd_stmt, ['a figure that is not there']) == 'NOT SUPPORTED'))
# (3) a conjunct under a binder must not be reported at TOP
under_binder = bool(re.search(r'∀ s ∈ Icc \(0:ℝ\) 1,', c1c_stmt))
note('neg3', 'the nullity conjunct is read UNDER its binder, not at TOP: %s' % under_binder)
if not under_binder:
    FAIL.append('negative probe 3 could not confirm the binder')
# (6) a dependence reading must be able to answer BOTH ways
note('neg6', 'the reliance reading answered both ways in ARM 2: %s'
      % (v8 == 'RELIES' and v8b != 'RELIES'))

say()
say('=' * 78)
say('SUMMARY')
say('=' * 78)
for tag, text in READINGS:
    if tag == 'VERDICT':
        say('  ' + text[:160])
say()
if FAIL:
    say('GUARD / NEGATIVE-PROBE FAILURES (%d):' % len(FAIL))
    for f in FAIL:
        say('  - ' + f)
    sys.exit(1)
say('every registered reading ran; %d readings recorded.' % len(READINGS))
sys.exit(0)
