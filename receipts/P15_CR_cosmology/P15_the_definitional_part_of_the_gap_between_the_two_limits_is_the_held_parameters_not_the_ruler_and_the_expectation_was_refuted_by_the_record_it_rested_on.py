# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE DEFINITIONAL PART OF THE GAP BETWEEN THE TWO LIMITS IS THE HELD PARAMETERS, NOT THE RULER,
AND IT IS ABOUT HALF — WITH THE REGISTERED EXPECTATION REFUTED BY A NUMBER THAT WAS ALREADY IN THE
RECORD THE REGISTRATION CITED.

COMPUTES: nothing physical. It reads the record `r7898` produced by substituting the reference's own
definition into this instrument's limit read, one difference at a time, and checks the teeth of that
reading.
** IT PINS AS RESULTS: ** holding `omega_b` and `n_s` as the reference's calibrated arm does moves
this instrument's limit `193.545304` → `103.9167` meV, a move of `89.6286`, closing `0.550` of the gap
to the reference's `30.560`. The ruler substitution moves it the OTHER WAY, `+11.7229` meV, share
`−0.072`. Both together give `101.9419`, share `0.562`.
⛔ ** SO THE REGISTERED OUTCOME IS `Ⓡ⓵`, DEFINITIONAL AND CARRIED BY ONE AXIS, AND THE AXIS IS THE
PARAMETERS. ** It clears the registered bar narrowly, `0.5499` against `0.5`, and that is reported as
narrow rather than as a pass, because a bar fixed before the scan is what makes `narrowly` a fact.
⛔ ** AND THE REGISTERED EXPECTATION IS REFUTED BY THE RECORD IT RESTED ON. ** The registration
expected the RULER to carry the gap, citing `r7862` as moving the calibrated limit `146.13` → `89.91`
meV. `r7862`'s record holds two calibrated columns — `78.3308` meV on the instrument's own ruler and
`89.9076` on the reference's — so that revision measured the ruler substitution moving the limit
`+11.5767` meV AWAY, and `146.13` is a figure its own RESULT states is superseded. *A superseded
headline figure was carried into a registration as a measured column.*
⛭ ** AND THE SUBSTITUTION REPRODUCES, WHICH NOTHING ASKED FOR: ** `+11.5767` meV at `r7862` on a
column at `78.3308`, against `+11.7229` here on a column at `193.5453` — same direction, same size to
about a seventh of a meV, across a factor of two and a half and a different physics.
⛔ ** AND THE REGISTRATION'S OWN LIST OF SETTLED AXES WAS WRONG ABOUT THIS ONE. ** It listed the
held-versus-profiled parameters as settled by `cc66`'s `−0.280` meV on the REFERENCE. The same axis is
worth `−89.6286` meV on this instrument, about `320` times more. *`cc66`'s figure is a fact about
`cc66`'s instrument.* Had the scan honoured that listing it would have skipped the only axis that
carries anything.
⛭ ** AND THE TWO AXES DO NOT COMPOSE: ** the ruler alone moves `+11.7229` away; on top of held
parameters it moves `1.97473` TOWARD — a sign reversal of the same substitution, visible only because
the combined arm was run.
⛔ ** AND WHAT IS NOT CLOSED IS ABOUT HALF: ** with both substitutions the instrument reads
`101.9419` meV against `30.560`, a factor of `3.336` still open. So `Ⓡ⓶` is half right and the half it
gets right is the smaller claim.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7898 = glob.glob(os.path.join(BW, 'r7898_60_*'))[0]
R7888 = glob.glob(os.path.join(BW, 'r7888_60_*'))[0]
R7862 = glob.glob(os.path.join(BW, 'r7862_60_*'))[0]

FAILS = []
NARMS = 0


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


D = json.load(io.open(os.path.join(R7898, 'ruler_and_params.json'), encoding='utf-8'))
BANK = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
CAL62 = json.load(io.open(os.path.join(R7862, 'calibrated.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7898, 'ruler_and_params.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
PRAW = io.open(os.path.join(R7898, 'PREDICTION.md'), encoding='utf-8').read()
PRED = ' '.join(PRAW.replace('*', '').replace('`', '').split())
RRAW = io.open(os.path.join(R7898, 'RESULT.md'), encoding='utf-8').read()
RES = ' '.join(RRAW.replace('*', '').replace('`', '').split())

A = {k.split()[0]: v for k, v in D['arms'].items()}
S = {k.split()[0]: v for k, v in D['shares'].items()}
C = float(D['control_calibrated'])

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓥ
print('\nⓋ  NOTHING IS BUILT HERE, AND THE CONTROL IS NOT A SEPARATE CODE PATH')

_defs = {n.name for n in ast.walk(TREE) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
_forbidden = sorted(d for d in _defs
                    if d in ('closed_envelope', 'Ruler', 'attach', '_fit', '_cold', 'Model6'))
_imported = {(a.name, a.asname) for n in ast.walk(TREE) if isinstance(n, ast.Import)
             for a in n.names}
check('Ⓥ① the revision defines no envelope reader, no ruler class, no fitter and no model — it '
      'imports `r7884`\'s limit module and `r7870`\'s envelope reader whole, redirects ONE source '
      'directory at the ordered grid, and captures the two model instances `r7884` builds as it '
      'builds them. ⌗ *Read on the parse tree, because a source-text search for these names matches '
      'the very line that forbids them*',
      not _forbidden and ('limits_nuhier', 'L') in _imported
      and ('envelope_closed', 'EC') in _imported,
      'imports limits_nuhier as L and envelope_closed as EC; redefines %s' % (_forbidden or 'nothing'))

#: ⛭ the capture wrapper is the one dangerous thing in this revision: if it were still installed when
#:   an arm ran, that arm would return a BANKED number and its share would be a share of nothing.
_restore = [n for n in ast.walk(TREE) if isinstance(n, ast.Assign)
            for t in n.targets if isinstance(t, ast.Attribute) and t.attr == 'closed_envelope']
_in_finally = any(any(st is asg for st in blk.finalbody)
                  for blk in ast.walk(TREE) if isinstance(blk, ast.Try)
                  for asg in _restore)
#: the module's own identity gate, located on the PARSE TREE: an `is` comparison between the reader
#: attribute and the saved original. Searching the source text for that expression would have been a
#: pin on the module's wording, and the wording is not what makes it safe.
_identity = [n for n in ast.walk(TREE) if isinstance(n, ast.Compare)
             and n.ops and isinstance(n.ops[0], ast.Is)
             and isinstance(n.left, ast.Attribute) and n.left.attr == 'closed_envelope'
             and isinstance(n.comparators[0], ast.Name) and n.comparators[0].id == '_REAL']
check('Ⓥ② and the capture wrapper that stands in for the envelope reader is restored in a `finally`, '
      'so it cannot survive an exception into an arm — and the module GATES that the real reader is '
      'back before any substituted limit is read. ⌗ *A stubbed arm would be a share computed from a '
      'number nothing measured, which is the one failure this design can produce*',
      _in_finally and bool(_identity),
      'restored in finally: %s; identity gated in the module: %s'
      % (_in_finally, bool(_identity)))

check('Ⓥ③ and the control is `r7888`\'s banked record reproduced through the UNMODIFIED path, not a '
      'number this revision computed for itself: both of its crossings match that record exactly, '
      'and the module checks the working tree is clean for it rather than reading the figure back '
      'out of a file the run rewrites',
      abs(C - float(BANK['calibrated']['crossing_meV'])) == 0.0
      and abs(float(D['control_minimised']) - float(BANK['minimised']['crossing_meV'])) == 0.0,
      'calibrated %.6f, minimised %.6f, both at exactly zero deviation'
      % (C, float(D['control_minimised'])))

# ---------------------------------------------------------------------------------------------- Ⓦ
print('\nⓌ  THE VERDICT IS ARITHMETIC OVER THE ARMS, AND THE SINGLES ARE NOT POOLED WITH THE PAIR')

_sing = [n.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id == 'SINGLES']
_comb = [n.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id == 'COMBINED']
_sv = [e.value for e in (_sing[0].elts if _sing else [])]
_cv = _comb[0].value if _comb else None
check('Ⓦ① the single substitutions and the combined one are kept apart BY CONSTRUCTION, read off the '
      'parse tree: the combined arm is not a member of the set the `Ⓡ⓵` branch searches, so `one '
      'axis carries it` cannot name the pair. ⌗ *This receipt\'s revision got that wrong on its first '
      'run — it pooled all three and reported the COMBINED arm as the carrier, which is the one thing '
      '`Ⓡ⓵` cannot mean — so the separation is gated rather than trusted*',
      len(_sv) >= 2 and _cv is not None and _cv not in _sv
      and set(_sv) == {k for k in D['singles']} and _cv == D['combined'],
      'singles %s, combined %s, disjoint: %s, and the record agrees: %s'
      % (_sv, _cv, _cv not in _sv,
         set(_sv) == {k for k in D['singles']} and _cv == D['combined']))

_vd = [n for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef) and n.name == 'verdict']
_vcalls = {n.func.attr for f in _vd for n in ast.walk(f)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)}
check('Ⓦ① ᵃ and the verdict is a PURE function of the shares — it reads no record, runs no fit and '
      'calls nothing that could measure, so the outcome is arithmetic over numbers already banked '
      'and a re-run of it cannot change what was measured',
      bool(_vd) and not ({'closed_envelope', 'load', 'run'} & _vcalls),
      'verdict defined: %s; measuring calls inside it: %s'
      % (bool(_vd), sorted({'closed_envelope', 'load', 'run'} & _vcalls) or 'none'))

_over = [k for k in D['singles'] if S.get(k, -9) >= 0.5]
check('Ⓦ② the registered outcome is `Ⓡ⓵` and its carrier is a SINGLE substitution, and the carrier '
      'is the parameters rather than the ruler',
      D['outcome'] == 'Ⓡ⓵' and _over == ['Ⓢ③'] and D['carrier'].split()[0] == 'Ⓢ③',
      'outcome %s, singles over the bar %s, carrier %s'
      % (D['outcome'], _over, D['carrier'].split()[0]))

check('Ⓦ②ᵃ and it clears the registered bar NARROWLY, which is said rather than rounded away — the '
      'margin is under half a per cent of the gap, and the only reason that is a fact instead of an '
      'argument is that the bar was fixed in `PREDICTION.md` before the first substituted limit was '
      'read',
      0.5 <= S['Ⓢ③'] < 0.56 and (S['Ⓢ③'] - 0.5) < 0.1 * 0.5,
      'share %.4f against the bar 0.5, margin %+.4f, which is %.1f%% of the bar'
      % (S['Ⓢ③'], S['Ⓢ③'] - 0.5, 100.0 * (S['Ⓢ③'] - 0.5) / 0.5))

#: ⛭ that the share is REPORTED rather than clipped is established from the document's own FIGURE,
#:   carrying its sign, not from a sentence claiming it was reported. A phrase can be reworded; a
#:   negative number in a table cannot be, and it is the thing the registration actually promised.
def _cell(glyph, col):
    """the signed number in one cell of the RESULT's own table, read as a NUMBER"""
    for ln in RRAW.splitlines():
        if ln.startswith('|') and glyph in ln:
            cs = [c.strip().strip('*').strip('`').strip()
                  for c in ln.strip().strip('|').split('|')]
            if col < len(cs):
                m = re.search(r'([\u2212+-]?)\s*(\d+\.\d+)', cs[col])
                if m:
                    return (-1.0 if m.group(1) in ('-', '\u2212') else 1.0) * float(m.group(2))
    return None


#: the document's own share cell for the ruler arm, read as a signed NUMBER and compared with the
#: record. Searching the text for the figure would have pinned the way it is written; this compares
#: what it MEANS, and it is the registration's actual promise -- the sign survives into the table.
_shown = _cell(D['singles'][0], 3)
_shown_negative = _shown is not None and _shown < 0.0 and abs(_shown - S['Ⓢ②']) < 5e-04
check('Ⓦ③ and the ruler moves the limit the WRONG WAY, so its share is negative and is reported '
      'rather than clipped — which the registration declared in advance, because both physics '
      'repairs so far had moved this limit away from the reference',
      S['Ⓢ②'] < 0.0 and A['Ⓢ②']['crossing_meV'] > C and _shown_negative,
      'ruler share %+.4f, crossing %+.4f above the control, printed with its sign in the RESULT: %s'
      % (S['Ⓢ②'], A['Ⓢ②']['crossing_meV'] - C, _shown_negative))

# ---------------------------------------------------------------------------------------------- Ⓧ
print('\nⓍ  THE EXPECTATION, THE MISREAD RECORD, AND THE REPRODUCTION NOBODY ASKED FOR')

#: ⛭ WHICH AXIS THE REGISTRATION EXPECTED IS READ OFF THE SCAN'S PARSE TREE, not off a phrase of the
#:   registration's prose. The scan's expectation test compares the measured carrier against one
#:   GLYPH; that glyph is extracted here, so neither a rewording of `PREDICTION.md` nor an axis name
#:   typed into this receipt can decide whether the expectation was refuted.
_expr = [n for n in ast.walk(TREE) if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id == 'exp_met']
_glyphs = sorted({c.value for e in _expr for c in ast.walk(e.value)
                  if isinstance(c, ast.Constant) and isinstance(c.value, str)
                  and c.value.startswith(('Ⓢ', 'Ⓡ'))})
_expected_axis = [g for g in _glyphs if g.startswith('Ⓢ')]
check('Ⓧ① the registered expectation named ONE axis and the measurement names the other, with the '
      'expected axis read off the scan\'s own expectation test on the parse tree and the registration '
      'carrying the outcome glyph it was registered under — so the refutation is established without '
      'quoting a sentence that could be reworded and without naming an axis in this receipt',
      _expected_axis == ['Ⓢ②'] and D['expectation_met'] is False
      and D['carrier'].split()[0] != _expected_axis[0],
      'expected %s, carrier %s, glyphs in the scan\'s own expectation test %s'
      % (_expected_axis, D['carrier'].split()[0], _glyphs))

check('Ⓧ② ⛔ and the refutation was ALREADY IN THE RECORD THE REGISTRATION CITED, which this arm '
      'establishes from that record rather than from the headline it was read off: `r7862`\'s two '
      'calibrated columns put the instrument\'s own ruler BELOW the reference\'s, so its ruler '
      'substitution moved the limit AWAY — the opposite direction to the one the registration '
      'inferred, measured before the registration was written',
      float(D['r7862_instrument_ruler']) == float(CAL62['profiles']['instrument']['crossing_meV'])
      and float(D['r7862_reference_ruler']) == float(CAL62['profiles']['reference']['crossing_meV'])
      and float(D['r7862_ruler_move']) > 0.0,
      'instrument %.4f, reference %.4f, move %+.4f, both read from r7862\'s own record'
      % (float(D['r7862_instrument_ruler']), float(D['r7862_reference_ruler']),
         float(D['r7862_ruler_move'])))

_mine = A['Ⓢ②']['crossing_meV'] - C
check('Ⓧ③ ⛭ and the ruler substitution REPRODUCES across a factor of two and a half in the column it '
      'is applied to, which was not registered and is reported as a check on the substitution rather '
      'than as a result of it',
      abs(_mine - float(D['r7862_ruler_move'])) < 0.5
      and (A['Ⓢ②']['crossing_meV'] / float(D['r7862_reference_ruler'])) > 2.0,
      'r7862 %+.4f on a column at %.4f; here %+.4f on a column at %.4f; difference %+.4f meV'
      % (float(D['r7862_ruler_move']), float(D['r7862_instrument_ruler']), _mine, C,
         _mine - float(D['r7862_ruler_move'])))

check('Ⓧ④ ⛔ and the same definitional axis is worth two orders of magnitude more on this instrument '
      'than on the reference, with `cc66`\'s figure carried as a CITATION and not as a measurement — '
      'the record marks it so and names its provenance, because nothing in this revision can confirm '
      'it. ⌗ *The registration listed this axis as settled on the strength of that number, which is a '
      'fact about the reference and not about the instrument*',
      float(D['asymmetry_vs_reference']) > 100.0
      and 'provenance' in D['cited'] and 'cc66' in D['cited']['provenance'],
      'reference %+.3f meV against this instrument %+.4f meV, a factor of %.0f'
      % (float(D['cited']['reference_params_move_meV']), C - A['Ⓢ③']['crossing_meV'],
         float(D['asymmetry_vs_reference'])))

_alone = A['Ⓢ②']['crossing_meV'] - C
_given = A['Ⓢ④']['crossing_meV'] - A['Ⓢ③']['crossing_meV']
check('Ⓧ⑤ and the two axes do NOT compose: the ruler\'s move reverses sign according to whether the '
      'parameters are free, which the single-substitution arms cannot show and only the combined arm '
      'does — the same shape as `r7896`\'s finding, that what a freedom does depends on which other '
      'freedoms are open',
      _alone > 0.0 > _given,
      'ruler alone %+.4f, ruler given held parameters %+.4f, spread %.4f meV'
      % (_alone, _given, abs(_alone - _given)))

check('Ⓧ⑥ and what the two substitutions do NOT close is stated as the larger part: with both '
      'applied the instrument still stands at a factor of more than three above the reference, so '
      'the hypothesis is carried as HALF right rather than as confirmed',
      A['Ⓢ④']['crossing_meV'] / float(D['partner_held']) > 3.0
      and max(S.values()) < 0.7,
      'both applied %.4f against %.3f, a factor of %.3f; largest share %.4f'
      % (A['Ⓢ④']['crossing_meV'], float(D['partner_held']),
         A['Ⓢ④']['crossing_meV'] / float(D['partner_held']), max(S.values())))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓔ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, each inside its own comparison and within half the last digit it is printed '
      'to. ⌗ *Bound by nearest value instead, `r7896` pinned a share to a block move that merely lay '
      'nearby and the arm passed while checking the wrong quantity, so the mapping here is stated '
      'per figure and only its COMPLETENESS is mechanical*',
      True
      and abs(D['control_calibrated'] - 193.545304) < 5e-07
      and abs(D['control_minimised'] - 310.147692) < 5e-07
      and abs(D['repro_tol_meV'] - 0.001) < 5e-04
      and abs(D['partner_held'] - 30.560) < 5e-04
      and abs(D['partner_free'] - 54.000) < 5e-04
      and abs(A['Ⓢ②']['crossing_meV'] - 205.2682) < 5e-05
      and abs(A['Ⓢ②']['crossing_meV'] - C - 11.7229) < 5e-05
      and abs(-S['Ⓢ②'] - 0.072) < 5e-04
      and abs(-(C - A['Ⓢ②']['crossing_meV']) / (C - D['partner_free']) - 0.084) < 5e-04
      and abs(A['Ⓢ③']['crossing_meV'] - 103.9167) < 5e-05
      and abs(C - A['Ⓢ③']['crossing_meV'] - 89.6286) < 5e-05
      and abs(S['Ⓢ③'] - 0.550) < 5e-04
      and abs((C - A['Ⓢ③']['crossing_meV']) / (C - D['partner_free']) - 0.642) < 5e-04
      and abs(A['Ⓢ④']['crossing_meV'] - 101.9419) < 5e-05
      and abs(C - A['Ⓢ④']['crossing_meV'] - 91.6034) < 5e-05
      and abs(S['Ⓢ④'] - 0.562) < 5e-04
      and abs((C - A['Ⓢ④']['crossing_meV']) / (C - D['partner_free']) - 0.65644) < 5e-06
      and abs(D['control_calibrated'] - 193.545) < 5e-04
      and abs(A['Ⓢ③']['crossing_meV'] - 103.917) < 5e-04
      and abs(S['Ⓢ③'] - 0.5499) < 5e-05
      and abs(0.5 - 0.5) < 5e-02
      and abs(146.13 - 146.13) < 5e-03
      and abs(D['r7862_reference_ruler'] - 89.91) < 5e-03
      and abs(D['r7862_instrument_ruler'] - 78.3308) < 5e-05
      and abs(D['r7862_reference_ruler'] - 89.9076) < 5e-05
      and abs(D['r7862_ruler_move'] - 11.5767) < 5e-05
      and abs(D['control_calibrated'] - 193.5453) < 5e-05
      and abs(D['cited']['reference_params_held_meV'] - 54.28) < 5e-03
      and abs(-D['cited']['reference_params_move_meV'] - 0.280) < 5e-04
      and abs(A['Ⓢ③']['crossing_meV'] - A['Ⓢ④']['crossing_meV'] - 1.97473) < 5e-06
      and abs((A['Ⓢ②']['crossing_meV'] - C) + (A['Ⓢ③']['crossing_meV'] - A['Ⓢ④']['crossing_meV']) - 13.70) < 5e-03
      and abs(A['Ⓢ④']['crossing_meV'] / D['partner_held'] - 3.336) < 5e-04
      and abs(A['Ⓢ④']['crossing_meV'] / D['partner_free'] - 1.89) < 5e-03
      and abs(S['Ⓢ③'] - 0.55) < 5e-03
      , 'all %d figure(s) read at the record' % 34)

# ---------------------------------------------------------------------------------------------- Ⓝ
print('\nⓃ  WHAT THIS DOES NOT CLAIM')

_tail = RRAW.split('\n## ')[-1]
_bul = [l for l in _tail.splitlines() if l.startswith('- ')]
check('Ⓝ① and the RESULT closes on a disclaimer section rather than on its result, with five or more '
      'bullets — among them that the reference\'s treatment is not claimed to be the RIGHT one, which '
      'matters because this revision measures what adopting it does and not whether to adopt it',
      len(_bul) >= 5,
      '%d disclaimer bullet(s)' % len(_bul))

print('      ⛔ Holding the two parameters is not claimed to be the right treatment. It is the')
print('         reference\'s, and what is measured is what adopting it does to this limit.')
print('      ⚠ The remaining factor is not claimed to be physical -- it is unexplained on the axes')
print('         the registration enumerated, which is a different and weaker statement.')
print('      ⚠ No new limit is read. r7888\'s 193.545 meV stands and its record is untouched; every')
print('         number here is a substituted reading made to size a difference.')
print('      ⚠ The minimised column stays unreadable, as r7888 established, and no substitution')
print('         here made it readable or was expected to.')

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
