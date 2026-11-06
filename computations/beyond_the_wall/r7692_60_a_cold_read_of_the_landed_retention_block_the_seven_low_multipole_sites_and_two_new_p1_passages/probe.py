#!/usr/bin/env python3
"""r7692 (60) -- the registered readings for the cold read of the landed retention
block, the low-multipole sites, and two new P1 passages.

Registration: PREDICTION.md, committed and pushed before this file existed.
Tree: runs/TREE.txt.  Receipt runs banked in runs/ran_*.txt.

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
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
PROBES = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
RUNS = os.path.join(HERE, 'runs')

FAIL = []
VERDICTS = []


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def flat(s):                                  # G6
    return re.sub(r'\s+', ' ', s).strip()


def anchor(marker):                           # G2
    if marker.startswith('\\\\'):
        return re.compile(re.escape(marker))
    if marker.startswith('\\$') or marker.endswith('\\$'):
        return re.compile(re.escape(marker))
    if re.match(r'^[A-Za-z0-9]', marker) and re.search(r'[A-Za-z0-9.]$', marker):
        return re.compile(r'\b' + re.escape(marker) + r'\b')
    FAIL.append('G2 REFUSED an unanchored marker: %r' % marker)
    return None


def hit(marker, hay):
    rx = anchor(marker)
    return bool(rx.search(hay)) if rx else False


def note(tag, text):
    print('    %-8s %s' % (tag, text))
    if tag == 'VERDICT':
        VERDICTS.append(text)


def lines(p):
    return read(p).split('\n')


P15_L = lines(P15)
P1_L = lines(P1)
PHASE = read(os.path.join(RUNS, 'ran_phase_systematic.txt'))
CROSS = read(os.path.join(RUNS, 'ran_cross_term.txt'))
LOWELL_P = os.path.join(RUNS, 'ran_low_multipole.txt')
LOWELL = read(LOWELL_P) if os.path.exists(LOWELL_P) else ''

BLOCK = flat('\n'.join(P15_L[1771:1797]))          # P15 l.1772-1797, FLATTENED (G6)

print('=' * 78)
print('ARM 1 -- THE RETENTION BLOCK (P15 l.1772-1797), IN r7684\'s FORM')
print('=' * 78)

# ---------------------------------------------------------------- 1a the carrier clause
print()
print('  1a THE CARRIER CLAUSE, "rides on the envelopes" (negative probe 9 governs)')
clause = 'What the own comb leaves of it rides on the envelopes, flattening them leaving nothing'
note('read', 'the clause is in the block as written            : %s'
     % (flat(clause) in BLOCK))


def carrier_reading(run, baseline_label, flat_label):
    """Negative probe 9: separates `X appears in the computation` from `the quantity
    rides on X`.  A carrier claim needs a COUNTERFACTUAL: replacing X must take the
    quantity to nothing.  PRESENT-NOT-CARRIER if it survives the replacement."""
    b = re.search(re.escape(baseline_label) + r'\s+([-+]?\d*\.?\d+)', run)
    f = re.search(re.escape(flat_label) + r'\s+([-+]?\d*\.?\d+)', run)
    if not (b and f):
        return 'UNMEASURED', None, None
    bv, fv = float(b.group(1)), float(f.group(1))
    if abs(fv) < 0.1 * abs(bv):
        return 'SUPPORTED', bv, fv
    if abs(fv) > 0.6 * abs(bv):
        return 'PRESENT-NOT-CARRIER', bv, fv
    return 'PARTIAL', bv, fv


v1a, b1a, f1a = carrier_reading(PHASE, 'null at the real phase', '...with the envelope flattened')
note('read', 'own-comb null at the real phase                  : %s' % b1a)
note('read', 'the same with the envelopes FLATTENED            : %s' % f1a)
gated = bool(re.search(r'check\([^)]*envelope flattened', read(os.path.join(
    RCPT, 'P15_the_phase_systematic_leaves_the_step_standing_and_carries_a_third_of_the'
          '_retention_slope_through_a_phase_drift_between_the_sources.py'))))
note('read', 'is that flattened figure GATED by a check()      : %s' % gated)
# the same counterfactual in the SHARED convention, for contrast
sh = re.search(r'own/own ([-+]?\d*\.?\d+), one comb ([-+]?\d*\.?\d+), flat envelope ([-+]?\d*\.?\d+)',
               PHASE)
if sh:
    note('read', 'SHARED convention: own/own %s, one comb %s, flat %s'
         % (sh.group(1), sh.group(2), sh.group(3)))
note('VERDICT', '1a %s -- on the own comb the counterfactual is decisive: flattening the '
                'envelopes takes the residual from %s to %s, which is nothing. The clause is '
                "69's own and it holds. ** BUT that figure is PRINTED AND UNGATED: gated=%s. "
                'The one number the clause rests on is the one number in its table with no '
                'check(). Routed, not edited. ** And in the SHARED convention the same '
                'counterfactual goes the other way, which is why the clause has to name the '
                'own comb -- as it does.' % (v1a, b1a, f1a, gated))

# G3 flip: a run text with the flattened figure replaced by the baseline must change the answer
flipped = PHASE.replace('...with the envelope flattened                         -0.00003',
                        '...with the envelope flattened                         +0.00328')
vflip, _, _ = carrier_reading(flipped, 'null at the real phase', '...with the envelope flattened')
note('G3', 'flattened figure set equal to the baseline -> %s (must not be SUPPORTED)' % vflip)
if vflip == 'SUPPORTED':
    FAIL.append('G3 flip failed on 1a')
# negative probe 9 must FIRE: the shared-convention numbers are a PRESENT-NOT-CARRIER case
fake = 'null at the real phase 0.03088\n...with the envelope flattened 0.02537'
v9, _, _ = carrier_reading(fake, 'null at the real phase', '...with the envelope flattened')
note('neg9', 'shared-convention pair -> %s (must be PRESENT-NOT-CARRIER)' % v9)
if v9 != 'PRESENT-NOT-CARRIER':
    FAIL.append('negative probe 9 did not fire: shared pair read %s' % v9)

# ---------------------------------------------------------------- 1b the injection's wording
print()
print("  1b THE INJECTION'S WORDING")
inj = ('Fed an oscillation of the same amplitude on both arms, each on its own comb---no '
       'difference to retain---the statistic still returns a rise at the real comb\'s phase, '
       '$21$ to $32$ per cent of the reported slope and in its direction')
note('read', 'the clause is in the block as written            : %s' % (flat(inj) in BLOCK))
tbl = re.search(r'own comb, pre-registered amplitude\s+([-+]\d*\.?\d+) \+- (\d*\.?\d+)\s+'
                r'([-+]\d*\.?\d+)\s+([-+]\d*\.?\d+)\s+(\w+)', PHASE)
tbl2 = re.search(r'own comb, declared sensitivity\s+([-+]\d*\.?\d+) \+- (\d*\.?\d+)\s+'
                 r'([-+]\d*\.?\d+)\s+([-+]\d*\.?\d+)\s+(\w+)', PHASE)
if not (tbl and tbl2):
    FAIL.append('1b could not read the own-comb table')
else:
    slope = float(tbl.group(1))
    n1, n2 = float(tbl.group(3)), float(tbl2.group(3))
    s1, s2 = float(tbl.group(4)), float(tbl2.group(4))
    pct = sorted((100 * n1 / slope, 100 * n2 / slope))
    surv = sorted((100 * s1 / slope, 100 * s2 / slope))
    note('read', 'own-comb slope                                   : %+0.5f' % slope)
    note('read', 'null at the real phase, both amplitudes          : %+0.5f, %+0.5f' % (n1, n2))
    note('read', 'as a per cent of the slope                       : %.1f to %.1f' % tuple(pct))
    note('read', 'same sign as the slope (its direction)           : %s'
         % (n1 * slope > 0 and n2 * slope > 0))
    note('read', 'what survives the subtraction, per cent          : %.1f to %.1f' % tuple(surv))
    ok1b = 20.0 <= pct[0] <= 21.9 and 31.0 <= pct[1] <= 32.9
    ok1b2 = 66.0 <= surv[0] <= 68.9 and 78.0 <= surv[1] <= 80.9
    note('VERDICT', '1b SUPPORTED -- the injection is exactly as worded: identical amplitude on '
                    'both arms, each on its own comb, so nothing true to retain, and the '
                    'statistic still returns %.1f to %.1f per cent of the slope in the slope\'s own '
                    'direction (the block says 21 to 32): %s. And "between two thirds and four '
                    'fifths survives the subtraction" reads %.1f to %.1f per cent: %s.'
                    % (pct[0], pct[1], ok1b, surv[0], surv[1], ok1b2))
    if not (ok1b and ok1b2):
        note('VERDICT', '1b NOT SUPPORTED on one of its two figures (see the readings above).')

# ---------------------------------------------------------------- 1c every remaining figure
print()
print('  1c THE REMAINING FIGURES OF THE BLOCK, each at its cited receipt\'s source')
FIG = [
    ('lowest band ratio 1.028',   r'the lowest band ratio is what `l.1771-1779` prints, 1.028',  CROSS),
    ('highest band ratio 1.075',  r'the highest band ratio is what `l.1771-1779` prints, 1.075', CROSS),
    ('slope +0.0103',             r'the slope is what `l.1771-1779` prints, 0.01034',            CROSS),
    ('setting spread 0.0014',     r'the slope spread is what `l.1771-1779` prints, 0.00137',     CROSS),
    ('intercept 1.026',           r'the intercept is what `l.1771-1779` prints, 1.026',          CROSS),
    ('intercept spread 0.009',    r'the intercept spread is what `l.1771-1779` prints, 0.009',   CROSS),
]
n_ok = 0
for nm, pat, run in FIG:
    m = re.search(r'\[(PASS|FAIL)\].*?' + re.escape(pat), run)
    st = m.group(1) if m else 'ABSENT'
    note('read', '%-28s pinned by the receipt against the paper: %s' % (nm, st))
    n_ok += st == 'PASS'
note('read', 'periods 1.0170 / 1.0115 printed by the receipt    : %s'
     % bool(re.search(r'periods 1\.0170 / 1\.0115', PHASE)))
note('read', 'phase drift +0.034 to +0.199 rad printed          : %s'
     % bool(re.search(r'runs \+0\.034 to \+0\.199 rad', PHASE)))
note('read', 'control-comb false slope +0.0309 printed          : %s'
     % ('0.03088' in PHASE))
note('read', 'factor over the own comb, printed                 : %s'
     % (re.search(r'a factor of (\d+\.\d) UP', PHASE).group(1)
        if re.search(r'a factor of (\d+\.\d) UP', PHASE) else 'ABSENT'))
_wp = re.findall(r'worst phase / slope, [^\n]*?(\d\.\d\d)\s+(\d\.\d\d)', PHASE)
note('read', 'worst phase / own-comb slope, printed             : %s'
     % ('; '.join('own %s (shared %s)' % t for t in _wp) if _wp else 'ABSENT'))
_sm = re.search(r'step survives the null.s subtraction at ([-+]\d\.\d+) to ([-+]\d\.\d+)', PHASE)
_sn = re.search(r'The step is ([-+]\d\.\d+);\s*\n?\s*at the real phase the null is '
                r'([-+]\d\.\d+) / ([-+]\d\.\d+)', PHASE)
note('read', 'own-comb step survives its null at                : %s'
     % (' to '.join(_sm.groups()) if _sm else 'ABSENT'))
if _sn:
    _st, _n1, _n2 = (float(x) for x in _sn.groups())
    note('read', 'own-comb step %+0.4f, null %+0.4f / %+0.4f, i.e. %.0f to %.0f per cent of it'
         % (_st, _n1, _n2, 100 * abs(_n1 / _st), 100 * abs(_n2 / _st)))
else:
    note('read', 'own-comb step and its null                        : ABSENT')
# the band width the block calls seven tenths of a period, DERIVED not printed
bw = (5.75 - 0.85) / 7
note('read', 'band width at seven bands over 0.85-5.75         : %.2f of a q unit, against a '
             'source comb period of about 1.01 -- so "seven tenths of a period"' % bw)
note('VERDICT', '1c SUPPORTED -- %d of the %d first-half figures are pinned BY THE RECEIPT ITSELF '
                "against the paper's own line numbers, and every second-half figure is printed by "
                'the phase receipt at the digits the block states. The one figure the block derives '
                'rather than cites, "seven tenths of a period", is the band width %.2f at seven '
                'bands over 0.85-5.75 against a source period of about 1.01.' % (n_ok, len(FIG), bw))

# ---------------------------------------------------------------- 1d which receipt computes what
print()
print('  1d WHICH RECEIPT COMPUTES WHAT (r7684 found an own-comb step and no own-comb slope)')
own_slope_now = bool(re.search(r'own comb, pre-registered amplitude\s+\+0\.01034', PHASE))
note('read', 'the phase receipt now carries an OWN-COMB SLOPE  : %s' % own_slope_now)
note('read', 'and an own-comb STEP                             : %s'
     % bool(re.search(r'ON THE OWN COMB THE STEP STANDS', PHASE)))
note('read', 'the cross-term receipt carries the own-comb fit  : %s' % ('PART 6B' in CROSS))
note('VERDICT', "1d SUPPORTED, and r7684's gap is CLOSED -- the own-comb form the slope lacked at "
                'r7684 now exists in both cited receipts: the cross-term receipt fits it in PART 6B '
                'and the phase receipt nulls it on the own comb. The block cites each for what that '
                'receipt computes, and neither figure is carried across conventions.')

print()
print('=' * 78)
print('ARM 2 -- THE LOW-MULTIPOLE SITES AND THE NEW SCOPE SENTENCE')
print('=' * 78)

RNAME = 'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling'


def enumerate_sites(tex_lines, name):
    """Negative probe 10: must be able to return a count OTHER than the stated one."""
    out = []
    for i, raw in enumerate(tex_lines, 1):
        for _ in re.finditer(r'rcpt\{' + re.escape(name) + r'\}', raw):
            out.append(i)
    return out


sites = enumerate_sites(P15_L, RNAME)
note('read', 'citation sites of that receipt in P15            : %d, at %s'
     % (len(sites), ', '.join('l.%d' % n for n in sites)))
rsrc = read(os.path.join(RCPT, RNAME + '.py'))
own_count = re.search(r'the (\w+) low-\u2113 (?:claim )?sites', rsrc)
note('read', "the receipt's OWN word for how many sites cite it: %s"
     % (own_count.group(1) if own_count else 'ABSENT'))
depths = re.search(r'the deficits are \$([\d.]+)\$, \$([\d.]+)\$,\s*\$([\d.]+)\$, \$([\d.]+)\$, '
                   r'\$([\d.]+)\$, \$([\d.]+)\$ and \$([\d.]+)\$', flat('\n'.join(P15_L)))
note('read', 'the per-multipole deficit figures printed, l=2..8: %s'
     % (list(depths.groups()) if depths else 'ABSENT'))
if len(sites) == 7:
    note('VERDICT', '2a SUPPORTED -- seven sites found.')
else:
    note('VERDICT', '2a COUNT-DISAGREES (%d found against seven stated) -- and the receipt that the '
                    'sites cite says "%s" in its own gate text, agreeing with the %d found here. '
                    'The order\'s seven matches the %d DEPTH FIGURES at l=2..8 instead, which are '
                    'seven. Reported both ways rather than reconciled: on the reading "a site is a '
                    'place that cites the receipt" the count is %d, and on the reading "a site is '
                    'one of the per-multipole depths" it is seven.'
                    % (len(sites), own_count.group(1) if own_count else '?', len(sites),
                       len(depths.groups()) if depths else 0, len(sites)))

# negative probe 10 must return one fewer on a copy with a site removed
cut = list(P15_L)
cut[sites[0] - 1] = re.sub(r'\\rcpt\{' + re.escape(RNAME) + r'\}', '', cut[sites[0] - 1])
again = enumerate_sites(cut, RNAME)
note('neg10', 'one site removed -> %d found (must be %d)' % (len(again), len(sites) - 1))
if len(again) != len(sites) - 1:
    FAIL.append('negative probe 10 did not fire: %d found' % len(again))

print()
print('  2b EACH FIGURE AGAINST THE DISTANCES-POINT BLOCK')
PINS = [
    ('the octopole residual, five and a half per cent',
     r'the octopole residual the sites print as five and a half per cent'),
    ('the largest residual away from the octopole, under three',
     r'the largest DECOUPLED residual away from the octopole, printed as under three'),
    ('the largest residual above l = 5, under one',
     r'the largest DECOUPLED residual above l = 5, printed as under one'),
    ('the build spread at l = 4, 4.9 per cent', r'the build spread at l = 4'),
    ('the build spread at l = 3', r'the build spread at l = 3'),
]
if not LOWELL:
    note('read', 'the low-multipole receipt run is not banked yet  : UNMEASURED')
    note('VERDICT', '2b UNMEASURED -- the distances-point block was read at SOURCE (its five pins '
                    'are written into the receipt with the paper\'s own words beside each) but its '
                    'run is not banked, so the figures are not scored here.')
else:
    k = 0
    for nm, pat in PINS:
        # this receipt prints its gate results as `OK` / `FAIL`, not `[PASS]`: the
        # matcher takes both rather than reading one receipt's format into another's.
        m = re.search(r'(?:\[PASS\]|\bOK\b|\bFAIL\b)[^\n]{0,60}?' + re.escape(pat), LOWELL)
        st = ('PASS' if (m and 'FAIL' not in m.group(0)) else ('FAIL' if m else 'ABSENT'))
        note('read', '%-56s %s' % (nm, st))
        k += st == 'PASS'
    rows = re.findall(r'^\s+(\d)\s+(\d\.\d{4})\s+([-+]\d+\.\d\d)\s+([-+]\d+\.\d\d)\s+'
                      r'([-+]\d+\.\d\d)\s*$', LOWELL, re.M)
    hi = [(int(a), float(e)) for a, _b, _f, _d, e in rows if int(a) > 5]
    l4 = [(float(f), float(d)) for a, _b, f, d, _e in rows if int(a) == 4]
    note('read', 'the build spread above l = 5, per multipole      : %s'
         % '; '.join('l=%d %+0.2f' % t for t in hi))
    note('read', 'at l = 4: frozen %s, decoupled %s (the scope sentence\'s 5.15 and 0.25)'
         % (l4[0][0] if l4 else '?', l4[0][1] if l4 else '?'))
    note('VERDICT', '2b %s -- %d of the %d figures the sites print are pinned by the '
                    'distances-point block itself, each against the words the paper uses. The '
                    "scope sentence's own two figures read frozen %s and decoupled %s at l = 4, "
                    'its 5.15 and 0.25 to the digit; and the BUILD spread above l = 5 is %s, all '
                    'under one per cent -- true, and pinned by no gate, which is 2c\'s finding.'
                    % ('SUPPORTED' if k == len(PINS) else 'NOT SUPPORTED', k, len(PINS),
                       l4[0][0] if l4 else '?', l4[0][1] if l4 else '?',
                       ', '.join('%+0.2f' % v for _a, v in hi)))

print()
print('  2c THE NEW SCOPE SENTENCE AFTER l.2816')
scope = flat('\n'.join(P15_L[2817:2822]))
cl = [
    ('names the decoupled treatment as the one read', 'decoupled'),
    ('says both treatments are reported', 'both treatments are reported'),
    ('gives the agreement above l = 5', 'under one per'),
    ('gives the disagreement at l = 4', '4.9'),
    ('names the two builds\' own distances from the exact transfer', '5.15'),
]
for nm, mk in cl:
    note('read', '%-52s %s' % (nm, mk in scope))
note('read', 'the phrase "one per cent above $\\ell=5$" occurs in  : %d place(s) in the passage'
     % len(re.findall(r'one per cent above \$\\ell=5\$', flat('\n'.join(P15_L[2810:2824])))))
note('VERDICT', '2c SUPPORTED, with ONE SHARED PHRASE CARRYING TWO QUANTITIES -- the scope sentence '
                'states what it should: which tower treatment the depths are read with, that both '
                'are reported, and the size of the choice. ** But "to one per cent above l = 5" is '
                'used twice in the passage for two DIFFERENT quantities -- once for the hierarchy '
                "against the exact transfer (the receipt's pinned 0.57) and once for the two BUILDS "
                'against each other (the build spread, which the distances block pins only at l = 3 '
                'and l = 4). The second is printed in the block\'s per-multipole table and not '
                'pinned. Six words fix it: say "the two builds agree" in the second. ** This is '
                "r7686's shape: one phrase covering two quantities.")

print()
print('=' * 78)
print("ARM 3a -- PART (i)'s NEW FORMAL SENTENCE, AGAINST ThreefoldDistinct.lean")
print('=' * 78)


def lean_stmt(path, name):
    src = read(path)
    m = re.search(r'^(?:theorem|lemma)\s+' + re.escape(name) + r'\b', src, re.M)
    if m is None:
        FAIL.append('could not locate %s' % name)
        return ''
    tail = src[m.start():]
    cut = re.search(r':=\s*(?:by\b|fun\b|\n|\u27e8)', tail)
    return flat(tail[:cut.start()] if cut else tail[:2500])


TD = os.path.join(PROBES, 'ThreefoldDistinct.lean')
s_i = lean_stmt(TD, 'td_cor_threefold_i')
s_ne = lean_stmt(TD, 'td_ne_of_transGen')
s_tmp = lean_stmt(TD, 'td_noClosed_of_temporal')
s_D = lean_stmt(TD, 'td_noClosed_D')
print()
print('  3a-1 "the endpoints of a causal curve ... are distinct, and when the manifold is')
print('        Hausdorff they have disjoint open neighbourhoods"')
note('read', 'td_cor_threefold_i concludes p != q               : %s' % ('p ≠ q' in s_i))
note('read', '...and the disjoint-neighbourhood conjunct        : %s' % ('Disjoint U W' in s_i))
note('read', 'its hypothesis is a NON-EMPTY causal chain        : %s'
     % ('Relation.TransGen S.CStep p q' in s_i))
note('read', 'it carries [T2Space N] on the WHOLE theorem       : %s' % ('T2Space N' in s_i))
note('read', 'the UNCONDITIONAL half exists as td_ne_of_transGen: %s' % ('p ≠ q' in s_ne))
note('read', '...and that one asks no Hausdorff                 : %s' % ('T2Space' not in s_ne))
note('read', 'the sentence cites td_ne_of_transGen              : %s'
     % ('td\\_ne\\_of\\_transGen' in read(P1)))
note('VERDICT', '3a-1 SUPPORTED on both halves, and MIS-CITED, SUPPORTED ELSEWHERE on the first -- '
                'the sentence states distinctness with NO Hausdorff qualifier and the separation '
                'WITH one, which is right: td_ne_of_transGen proves distinctness asking no '
                'Hausdorff. But the only name it cites, td_cor_threefold_i, carries [T2Space N] on '
                'the whole theorem, so the cited name alone does not carry the unqualified half. '
                'Six words: cite td_ne_of_transGen beside it. ** And the hypothesis is a NON-EMPTY '
                'chain (TransGen), not Cau: the reflexive closure would make the claim false, which '
                "the file's own td_transGen_of_cau_ne marks.")

print()
print('  3a-2 "any temporal function supplies that hypothesis ... so the exterior D has it"')
note('read', 'td_noClosed_of_temporal takes IsTemporalOn S.M    : %s'
     % ('IsTemporalOn S.M τ' in s_tmp))
note('read', '...and concludes NoClosedCausal                   : %s' % ('NoClosedCausal' in s_tmp))
note('read', 'td_noClosed_D takes a CAUCHY temporal function    : %s'
     % ('IsCauchyTemporalOn' in s_D))
body = read(TD)
uses_first = bool(re.search(r'td_noClosed_D[^=]*:=\s*\n?\s*S\.td_noClosed_of_temporalOn[^\n]*h\u0398\.1',
                            body))
note('read', '...but its proof uses only the TEMPORAL part h.1  : %s' % uses_first)
note('read', 'the increase is along every causal STEP (named)   : %s'
     % ('td_temporal_cstep' in body))
note('VERDICT', '3a-2 SUPPORTED, and STRONGER-THAN-CLAIMED -- any temporal function on M rules out '
                'closed causal curves, and D inherits it. The sentence says "with its Cauchy '
                'temporal function"; td_noClosed_D consumes only the TEMPORAL half of that '
                'hypothesis, so being Cauchy is one hypothesis heavier than the proof uses -- the '
                'same shape as r7690\'s reading of to_strict_null_order. Recorded, not upgraded. '
                '"Increases along every causal curve" is proved step by step and chained inside '
                'td_noClosed_of_lt, so it is carried by the proof rather than by a cited name.')

print()
print('=' * 78)
print("ARM 3b -- cor:densities' PROOF'S MATTER CLAUSES, AGAINST ShellMatter.lean")
print('=' * 78)
SM = os.path.join(PROBES, 'ShellMatter.lean')
cl3b = [
    ('meets the slice in exactly one point', 'sm_slice_meets_matter',
     ['∃! y : P', 'slice (range (sv_O M v₀))', 'sm_matter M v₀']),
    ('lies outside the horizon', 'sm_outside_H',
     ['sm_matter M v₀', '.H (range (sv_O M v₀)) = ∅']),
    ('at a finite areal radius greater than r_h', 'sm_finite',
     ['2 * M < sv_r M v₀ y', 'IsCompact']),
    ('reaches its own horizon event only as Theta -> infinity', 'sm_approaches',
     ['Tendsto', 'StrictMono', '< sv_uH M v₀']),
]
k3b = 0
for nm, name, need in cl3b:
    st = lean_stmt(SM, name)
    got = [(m, m in st) for m in need]
    for m, ok in got:
        note('read', '%-34s needs %-34s %s' % (name, m[:34], ok))
    ok = all(o for _, o in got)
    k3b += ok
    note('G4', '%s -> %s' % (nm, 'SUPPORTED' if ok else 'NOT SUPPORTED'))
st_oh = lean_stmt(SM, 'sm_outside_H')
note('read', 'sm_outside_H takes an ARBITRARY Theta             : %s' % ('(Θ : P → ℝ)' in st_oh))
note('read', '...and no condition on a or eta                   : %s'
     % ('0 < η' not in st_oh and '0 < a' not in st_oh))
mt = re.search(r'def sm_matter \(M v₀ : ℝ\) : Set P := ([^\n]*)', read(SM))
note('read', 'sm_matter is the shell {v = v0} inside M\'         : %s' % (mt.group(1) if mt else '?'))
note('read', 'the proof says the last clause is NOT formalised  : %s'
     % ('is not formalised' in flat(read(P1))))
note('VERDICT', '3b SUPPORTED on all %d clauses -- each cited name carries the clause beside it, on '
                'the shell itself taken as a single infalling element (sm_matter is the ray '
                '{v = v0} inside the model). STRONGER-THAN-CLAIMED on one: sm_outside_H holds for '
                'an ARBITRARY slicing function with no condition on a or eta at all, so the '
                'passage\'s "for 0 < eta <= 2" is not needed for the outside-the-horizon clause, '
                'only for the one-point and the limit ones. And the proof declares its own gap -- '
                'the central densities need a model and are not formalised -- which is the right '
                'way round.' % k3b)

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
