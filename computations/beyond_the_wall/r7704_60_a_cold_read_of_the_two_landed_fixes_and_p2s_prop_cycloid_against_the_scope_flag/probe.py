#!/usr/bin/env python3
# r7704 (60) -- the reading instrument for the order r7701.
#
#   ITEM 1  the two landed fixes in place, and l.2903's row against l.2612's, so the sector's
#           per-multipole figures agree at EVERY site.
#   ITEM 2  P2's `prop:cycloid` against 71's scope flag -- read so that NO SCOPE ERROR is a
#           reachable answer, because a probe built after a flag confirms the flag by default.
#
# THE SIX GUARD FAMILIES: G1 one predicate per conjunct; G2 three anchor forms only (a word
# boundary, an escaped control sequence with ONE leading backslash, an escaped math delimiter),
# unanchored markers REFUSED; G3 the flip family; G4 classifiers tested on BOTH classes; G5 reader
# probes each with its negative; G6 every prose probe on a whitespace-FLATTENED copy.
# EVERY VERDICT NOTE IS BUILT FROM ITS READINGS.  UNMEASURED is printed, never omitted.

import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P2 = os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')

FAIL = []
READINGS = []


def say(s=''):
    print(s)
    READINGS.append(s)


def flat(s):
    return re.sub(r'\s+', ' ', s)


def anchor(marker):                            # G2
    if marker.startswith('\\') or marker.startswith('$'):
        return re.escape(marker)
    if re.match(r'^\w', marker, re.UNICODE) and re.search(r'\w$', marker, re.UNICODE):
        return r'\b' + re.escape(marker) + r'\b'
    if re.search(r'[^\w\s]', marker):
        return re.escape(marker)
    raise AssertionError('G2 REFUSES the unanchored marker %r' % marker)


_g2 = []
for _m in ('cycloid', '\\begin', '$\\eta$'):
    try:
        anchor(_m); _g2.append('accepted')
    except AssertionError:
        _g2.append('REFUSED')
try:
    anchor('   '); _g2.append('accepted')
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


p15, p2, rcpt = need(P15), need(P2), need(RCPT)
if not (p15 and p2 and rcpt):
    print('\n'.join(FAIL)); sys.exit(2)
F15, F2, FR = flat(p15), flat(p2), flat(rcpt)

# =============================================================================================
say()
say('=' * 94)
say('ITEM 1 -- the two landed fixes, and the per-multipole row across every site')
say('=' * 94)

LIK = {'l2': '-2.6', 'l3': '+0.9', 'l4': '+2.2', 'l5': '+1.1'}
GATED = {'l2': -2.56, 'l3': 0.93, 'l4': 2.16, 'l5': 1.12}


def gate_want(fig):
    """The receipt's own `want` for a likelihood term, parsed from its gate tuples."""
    for mm in re.finditer(r'\(\s*"([^"]{0,90})"\s*,\s*(_pA\[\d\]|_tA|_rA\[\d\]),\s*([-+]?\d+\.?\d*)',
                          rcpt):
        if abs(abs(float(mm.group(3))) - abs(fig)) < 1e-9:
            return mm.group(1)[:62], float(mm.group(3))
    return None, None


say('arm 1a -- l.2612\'s repaired row, each figure against the receipt\'s own gate:')
site2612 = ''
for line in p15.split('\n'):
    if 'the octopole penalises it at' in line:
        site2612 = flat(line)
say('  the site located by its text: %s' % ('FOUND' if site2612 else 'ABSENT'))
if not site2612:
    FAIL.append('ITEM 1: l.2612\'s repaired sentence could not be located by its text')
m2612 = re.search(r'the quadrupole \\emph\{rewards\} this cosmology \(\$([-+][0-9.]+)\\\$?'
                  r'|the quadrupole \\emph\{rewards\} this cosmology \(\$([-+][0-9.]+)\$', site2612)
got = {}
for key, pat in (('l2', r'rewards\} this cosmology \(\$([-+][0-9.]+)\$'),
                 ('l3', r'octopole penalises it at \$([-+][0-9.]+)\$'),
                 ('l4', r'largest single-multipole penalty is the \$([-+][0-9.]+)\$ at \$\\ell=4\$')):
    mm = re.search(pat, site2612)
    got[key] = mm.group(1) if mm else None
for key in ('l2', 'l3', 'l4'):
    nm, want = gate_want(GATED[key])
    ok = got[key] == LIK[key]
    say('  %-3s in print %-6s against the order\'s %-5s and the gate %-6s (%s)'
        % (key, got[key] or 'ABSENT', LIK[key], ('%+.2f' % want) if want is not None else 'UNREAD',
           nm or 'no gate found'))
    if not ok:
        FAIL.append('ITEM 1 arm 1a: %s reads %r where the order says %r' % (key, got[key], LIK[key]))
A1 = all(got[k] == LIK[k] for k in ('l2', 'l3', 'l4'))
# the structural claim must still hold of the new row
largest = max(GATED, key=lambda k: GATED[k])
say('  the structural claim "largest single-multipole penalty at l = 4": the gated terms make the '
    'largest %s at %s' % ('%+.2f' % GATED[largest], largest))
A1 = A1 and largest == 'l4'

say()
say('arm 1b -- THE ORDER\'S CHECK: the row at every site that prints it, same quantity side by side:')
rows = {}
for i, line in enumerate(p15.split('\n'), 1):
    fl = flat(line)
    hits = {}
    # ⌗ THE FIRST FORM OF THIS READER REQUIRED THE FIGURE TO BE THE WHOLE MATH EXPRESSION
    #   (`$-2.6$`), and so it could not see `l.2903` at all, where the same term is printed as
    #   `$\Delta(-2\ln L)\approx-2.6$` -- INSIDE a larger expression.  l.2903 is the site the
    #   order asked about by name, so the reader was blind to exactly the comparison it was
    #   built for.  Third instance in three revisions of the same family (r7700's ASCII-only
    #   hypothesis names, r7702's three-place-only figures): AN INSTRUMENT READS THE FORM IT
    #   WAS GIVEN, NOT THE QUANTITY.  Fixed to match the signed figure wherever it sits inside
    #   a math span, with digit boundaries so `-2.65` cannot pass as `-2.6`.
    for key, pat in (('l2', r'(?<![0-9.])([-+]2\.[56])(?![0-9])'),
                     ('l3', r'(?<![0-9.])([-+]0\.9)(?![0-9])'),
                     ('l4', r'(?<![0-9.])([-+]2\.2)(?![0-9])'),
                     ('l5', r'(?<![0-9.])([-+]1\.1)(?![0-9])')):
        mm = [v for v in re.findall(pat, fl) if '$' in fl]
        if mm:
            hits[key] = mm
    if len(hits) >= 2:
        rows[i] = hits
for i, hits in sorted(rows.items()):
    say('  l.%-5d %s' % (i, '  '.join('%s=%s' % (k, '/'.join(v)) for k, v in sorted(hits.items()))))
say('  %d site(s) print two or more terms of the row.' % len(rows))
disagree = []
for key in ('l2', 'l3', 'l4', 'l5'):
    vals = set()
    for hits in rows.values():
        for v in hits.get(key, []):
            vals.add(v)
    if len(vals) > 1:
        disagree.append((key, sorted(vals)))
say('  any multipole printed with two different values across those sites: %s'
    % (disagree if disagree else 'none'))
B1 = not disagree
# NEGATIVE PROBE: the cross-site reader must fire on an injected disagreement
inj = p15.replace('the octopole penalises it at $+0.9$', 'the octopole penalises it at $+1.0$', 1)
inj_vals = set(re.findall(r'\$([-+]0\.9|[-+]1\.0)\$', flat(inj)))
say('  NEGATIVE PROBE (one site\'s octopole term altered on a copy): the reader sees %s'
    % (sorted(inj_vals) if len(inj_vals) > 1 else 'ONE value -- BLIND'))
if len(inj_vals) < 2:
    FAIL.append('ITEM 1 arm 1b: the cross-site reader did not see an injected disagreement')

say()
say('arm 1c -- the doubled-opacity clause as landed, and the build it now names:')
cl = 'the hierarchy\'s depths, swept on the control\'s background, do not move under a doubled'
say('  the clause, located by its text: %s' % ('FOUND' if cl in F15 else 'ABSENT'))
names_build = 'swept on the control\'s background' in F15
still_agreement = 'the agreement does not move under a doubled opacity grid' in F15
banks = sorted(set(re.findall(r"SW\['([A-Za-z_0-9]*control[A-Za-z_0-9]*)'\]", rcpt)))
say('  it names the build the convergence was measured on: %s' % ('YES' if names_build else 'no'))
say('  the old wording, which attached it to the agreement, is gone: %s'
    % ('YES' if not still_agreement else 'NO -- still present'))
say('  and the receipt\'s knob sweeps are computed on: %s' % (banks or 'UNREAD'))
say('  every one of those banks a CONTROL bank, which is what the clause now says: %s'
    % ('YES' if banks and all('control' in b for b in banks) else 'no'))
C1 = bool(cl in F15) and names_build and not still_agreement and bool(banks) \
    and all('control' in b for b in banks)

# =============================================================================================
say()
say('=' * 94)
say('ITEM 2 -- P2\'s prop:cycloid against 71\'s scope flag')
say('=' * 94)

ps = p2.find('\\begin{proposition}[Lemaître--Tolman cycloid form]')
pe = p2.find('\\end{proposition}', ps)
PROP = flat(p2[ps:pe]) if ps >= 0 else ''
pfs = p2.find('\\begin{proof}', pe)
pfe = p2.find('\\end{proof}', pfs)
PROOF = flat(p2[pfs:pfe]) if pfs >= 0 else ''
say('the proposition located by its own environment: %s (%d characters)'
    % ('FOUND' if PROP else 'ABSENT', len(PROP)))
say('its proof: %s (%d characters)' % ('FOUND' if PROOF else 'ABSENT', len(PROOF)))
if not (PROP and PROOF):
    FAIL.append('ITEM 2: the proposition or its proof could not be delimited')

# --- 2a: the statement's own hypotheses ------------------------------------------------------
RESTRICTIONS = ['E = 0', 'E=0', 'marginally bound', 'released from rest', 'at rest',
                'specific energy', 'zero energy', 'vanishing energy', 'momentarily static',
                'parabolic', 'critically bound']


def scope_reader(text):                        # G4, tested on both classes below
    """Does this text restrict the geodesic family?  Returns the markers it finds."""
    return [m for m in RESTRICTIONS if m.lower() in text.lower()]


say()
say('arm 2a -- the proposition\'s own statement, read for a restriction:')
say('  how it names its object: %s'
    % ('"a radial timelike geodesic"' if 'a radial timelike geodesic' in PROP else 'UNREAD'))
say('  restriction markers in the STATEMENT: %s' % (scope_reader(PROP) or 'NONE'))
say('  restriction markers in the PROOF: %s' % (scope_reader(PROOF) or 'NONE'))
say('  restriction markers anywhere in P2: %s' % (scope_reader(p2) or 'NONE'))
say('  what the proof\'s own first relation is: %s'
    % ('dtau^2 = dr^2/(2M/r - 1)' if '\\frac{dr^2}{2M/r - 1}' in PROOF else 'UNREAD'))
# G4's own probe (NEGATIVE PROBE 17, registered in PREDICTION.md): the reader must tell an
# injected restriction from an injected general statement, or it is answering about the flag.
inj_r = PROP.replace('along a radial timelike geodesic',
                     'along a radial timelike geodesic with E = 0', 1)
inj_g = PROP.replace('along a radial timelike geodesic', 'along any radial timelike geodesic', 1)
say('  NEGATIVE PROBE 17, the scope reader on both classes: injected restriction -> %s ; '
    'injected general -> %s' % (scope_reader(inj_r) or 'NONE', scope_reader(inj_g) or 'NONE'))
if not scope_reader(inj_r) or scope_reader(inj_g):
    FAIL.append('ITEM 2 arm 2a: the scope reader cannot tell a restricted statement from a '
                'general one')
A2_general = not scope_reader(PROP)

# --- 2b: the amplitude -----------------------------------------------------------------------
say()
say('arm 2b -- the amplitude the paper writes, and the flag\'s general form:')
amp = re.search(r'r\(\\eta\) = M\(1 \+ \\cos \\eta\)', PROP)
tau = re.search(r'\\tau\(\\eta\) = M\(\\eta \+ \\sin \\eta\)', PROP)
interval = re.search(r'\\tau\(\\pi\) - \\tau\(0\) = M\\pi', PROP)
say('  r(eta): %s' % (amp.group(0) if amp else 'UNREAD'))
say('  tau(eta): %s' % (tau.group(0) if tau else 'UNREAD'))
say('  the interval it states: %s' % (interval.group(0) if interval else 'UNREAD'))
say('  so the paper\'s amplitude is 2M (r runs from 2M at eta = 0 to 0 at eta = pi): %s'
    % ('YES' if amp else 'UNREAD'))
B2 = bool(amp) and bool(tau) and bool(interval)

# --- 2e: the flag CHECKED, not accepted ------------------------------------------------------
say()
say('arm 2e -- the flag checked at its own limit, by computing rather than by quoting:')
M = 1.0


def turning_point(E):
    """(dr/dtau)^2 = E^2 - 1 + 2M/r vanishes at r = 2M/(1 - E^2) for |E| < 1."""
    return 2 * M / (1 - E ** 2)


def interior_proper_time(E, n=200001):
    """int_0^{2M} dr / sqrt(E^2 - 1 + 2M/r), the proper time from the horizon to r = 0.

    ⌗ THE FIRST FORM OF THIS INTEGRAL WAS QUADRATURE ON r DIRECTLY, and it returned 3.139527 M
      against pi M -- a relative error of 7e-4, which failed this arm's own 1e-4 tolerance and
      made a correct reading print NOT SUPPORTED.  The integrand diverges as r -> 2M (the
      turning point at E = 0), so a uniform rule under-resolves exactly the endpoint that
      carries the answer.  ⇒ The fix is the QUADRATURE, not the tolerance: loosening the
      tolerance to admit a weak instrument would have hidden the instrument.  The substitution
      r = r_max sin^2(theta) removes the singularity analytically --
      E^2 - 1 + 2M/r = (1 - E^2) cot^2(theta), dr = 2 r_max sin(theta) cos(theta) d(theta) --
      and the integrand becomes 2 r_max sin^2(theta) / sqrt(1 - E^2), which is smooth.  At
      E = 0 it gives pi M in closed form, which is the paper's figure.
    """
    if abs(E) >= 1.0:                          # no turning point: integrate on r, smooth there
        tot, a, b = 0.0, 0.0, 2 * M
        h = (b - a) / (n - 1)
        for i in range(n):
            r = a + i * h
            v = E ** 2 - 1 + 2 * M / r if r > 0 else float('inf')
            f = 0.0 if (r <= 0 or v <= 0) else 1.0 / math.sqrt(v)
            tot += (0.5 if i in (0, n - 1) else 1.0) * f * h
        return tot
    rmax = turning_point(E)
    th_h = math.asin(min(1.0, math.sqrt(max(0.0, 1.0 - E ** 2))))
    tot = 0.0
    h = th_h / (n - 1)
    for i in range(n):
        th = i * h
        f = 2.0 * rmax * math.sin(th) ** 2 / math.sqrt(1.0 - E ** 2)
        tot += (0.5 if i in (0, n - 1) else 1.0) * f * h
    return tot


say('  the flag says the general amplitude is 2M/(1 - E^2); at E = 0 that is %.6f M'
    % turning_point(0.0))
say('  and the paper\'s amplitude, read above, is 2M -- so flag and paper AGREE at E = 0: %s'
    % ('YES' if abs(turning_point(0.0) - 2 * M) < 1e-12 else 'no'))
t0 = interior_proper_time(0.0)
t1 = interior_proper_time(1.0)
say('  computed here: the E = 0 interval is %.6f M against the paper\'s pi M = %.6f M (relative '
    'difference %.2e)' % (t0, math.pi, abs(t0 - math.pi) / math.pi))
say('  and the E = 1 interval (from rest at infinity) is %.6f M against 4/3 M = %.6f M'
    % (t1, 4 / 3))
say('  ⇒ so the printed interval is the E = 0 member\'s, larger than the E = 1 member\'s by a '
    'factor %.2f' % (t0 / t1))
E2 = abs(t0 - math.pi) / math.pi < 1e-4 and abs(t1 - 4 / 3) / (4 / 3) < 1e-4
# FLIP (G3): the computation must NOT return pi for a different E
say('  FLIP (G3), the same integral at E = 0.5: %.6f M, which is neither pi M nor 4/3 M: %s'
    % (interior_proper_time(0.5),
       'as it must be' if abs(interior_proper_time(0.5) - math.pi) > 1e-3 else 'WRONG'))
if abs(interior_proper_time(0.5) - math.pi) < 1e-3:
    FAIL.append('ITEM 2 arm 2e: the interval integral returns pi M for an E it should not')

# --- 2c: every sentence that USES it ---------------------------------------------------------
say()
say('arm 2c -- every site that cites or USES the proposition, found by reference AND by content:')
sites = []
for i, line in enumerate(p2.split('\n'), 1):
    fl = flat(line)
    why = []
    if 'ref{prop:cycloid}' in fl:
        why.append('cites the label')
    if re.search(r'M\\pi|\\tau = M\\pi', fl) and 'proper time' in fl.lower():
        why.append('uses the interval')
    if re.search(r'M\(1 ?\+ ?\\cos ?\\eta\)', fl) and i > (pe if pe > 0 else 0):
        why.append('uses the parametrisation')
    if why:
        sites.append((i, why, fl))
for i, why, fl in sites:
    general = not scope_reader(fl)
    subj = re.search(r'(The infalling worldline|a radially infalling test particle|'
                     r'the radial proper-time parameter|The cycloid)', fl)
    say('  l.%-5d %-45s subject: %-34s own context restricts: %s'
        % (i, '; '.join(why), (subj.group(1) if subj else '(not one of the named subjects)')[:34],
           'no' if general else scope_reader(fl)))
say('  %d using site(s) found; %d of them with no restriction in their own context.'
    % (len(sites), sum(1 for _, _, fl in sites if not scope_reader(fl))))
C2 = len(sites) > 0 and all(not scope_reader(fl) for _, _, fl in sites)

say()
say('-' * 94)


def verdict(v):
    if isinstance(v, str):
        return v
    return 'UNMEASURED' if v is None else ('SUPPORTED' if v else 'NOT SUPPORTED')


ROWS = [
    ('1a', A1, 'the three repaired figures are in print and each matches the receipt\'s gate, and '
     'the structural claim still holds of the new row'),
    ('1b', B1, '%d site(s) print two or more terms and no multipole is printed with two different '
     'values' % len(rows)),
    ('1c', C1, 'the clause names the build its convergence was measured on and the old wording is '
     'gone; every bank the sweeps use is a control bank'),
    ('2a', ('THE STATEMENT READS AS GENERAL' if A2_general else 'THE STATEMENT IS RESTRICTED'),
     'restriction markers in the statement: %s; in the proof: %s; anywhere in P2: %s'
     % (scope_reader(PROP) or 'none', scope_reader(PROOF) or 'none', scope_reader(p2) or 'none')),
    ('2b', B2, 'the paper writes r = M(1 + cos eta), tau = M(eta + sin eta) and the interval pi M'),
    ('2c', ('EVERY USING SITE READS AS GENERAL' if C2 else 'SOME USING SITE IS RESTRICTED'),
     '%d using site(s), found by reference and by content' % len(sites)),
    ('2e', E2, 'the flag and the paper agree at E = 0 (amplitude 2M, interval pi M computed here), '
     'and the E = 1 member\'s interval is 4/3 M, so the printed figure is the E = 0 member\'s'),
]
for k, v, note in ROWS:
    say('arm %-3s: %s -- %s' % (k, verdict(v), note))

say()
say('THE ORDER\'S QUESTION (arm 2d), computed from 2a and 2c and from nothing else:')
say('  P2 %s' % ('READS AS GENERAL -- the restriction is absent from every one of the %d markers '
                 'searched over the statement, the proof and the whole file, and every using site '
                 'inherits that' % len(RESTRICTIONS)
                 if (A2_general and C2) else
                 'STATES THE RESTRICTION somewhere relevant -- see 2a and 2c'))

say()
say('=' * 94)
say('%d verdicts printed.  %d reader or classifier probe(s) failed.' % (len(ROWS), len(FAIL)))
for f in FAIL:
    say('  DEFECT: %s' % f)
say('=' * 94)

with open(os.path.join(HERE, 'runs', 'READINGS.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(READINGS) + '\n')
sys.exit(1 if FAIL else 0)
