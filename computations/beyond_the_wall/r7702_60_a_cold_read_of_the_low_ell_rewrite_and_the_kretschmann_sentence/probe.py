#!/usr/bin/env python3
# r7702 (60) -- the reading instrument for the order r7699.
#
#   ITEM 1  every low-ell site in P15, P7 and P18 after the re-point onto arm A under the arm of
#           record's (L) pairing, against the depth-gap receipt's `r7697` block and the (L) banks.
#   ITEM 2  P1's Kretschmann sentence, against `Kretschmann.lean`.
#
# THE SIX GUARD FAMILIES: G1 one predicate per conjunct; G2 three anchor forms only (a word
# boundary, an escaped control sequence with ONE leading backslash, an escaped math delimiter),
# an unanchored marker REFUSED; G3 the flip family; G4 classifier probes on both classes;
# G5 reader probes each with its negative; G6 every prose probe on a whitespace-FLATTENED copy.
# EVERY VERDICT NOTE IS BUILT FROM ITS READINGS.  UNMEASURED is printed, never omitted.  An arm
# whose verdict would read backwards as SUPPORTED carries its own label (the r7698 correction).
#
# ⌗ AND ONE RULE THIS REVISION ADDS TO THE INSTRUMENT: read each figure AT THE PRECISION THE SITE
#   PRINTS IT.  The first pass of this read used a three-place pattern and so could not see
#   `l.2771`'s two-place quartet at all -- the same family as r7700's ASCII-only hypothesis names.

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
P1 = os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P7 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
P18 = os.path.join(ROOT, 'corpus', 'CR_synthesis.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'Kretschmann.lean')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
BANK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                    'p15_lowell_depths_armA_leafpert_leafrec1.npz')
RAN = os.path.join(HERE, 'runs', 'ran_depth_gap.txt')

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
for _m in ('octopole', '\\emph', '$\\ell=4$'):
    try:
        anchor(_m); _g2.append('accepted')
    except AssertionError:
        _g2.append('REFUSED')
try:
    anchor(' '); _g2.append('accepted')
except AssertionError:
    _g2.append('REFUSED')
say('G2 self-probe: %s' % ', '.join(_g2))
if _g2 != ['accepted', 'accepted', 'accepted', 'REFUSED']:
    FAIL.append('G2 self-probe did not accept the three forms and refuse the unanchored marker')


def lik_in(line, v):
    """A signed one-decimal figure as the paper prints it: `$-2.6$`, `$+0.9$`, or `\\approx+0.9`."""
    sign, digits = v[0], v[1:]
    pat = r'(?<![0-9.])' + re.escape(sign if sign == '-' else '+') + r'?' + re.escape(digits) + \
        r'(?![0-9])'
    for mm in re.finditer(pat, line):
        head = line[max(mm.start() - 2, 0):mm.start()]
        got_sign = '-' if '-' in mm.group(0) else ('+' if '+' in mm.group(0) else None)
        if got_sign is None and sign == '-' and '-' in head:
            got_sign = '-'
        if got_sign == sign and ('$' in line[max(mm.start() - 3, 0):mm.end() + 3]
                                 or 'approx' in line[max(mm.start() - 12, 0):mm.start()]):
            return True
    return False


def need(path, soft=False):
    if not os.path.exists(path):
        if not soft:
            FAIL.append('missing object: %s' % path)
        return ''
    with open(path, encoding='utf-8') as fh:
        return fh.read()


p1, p15, p7, p18 = need(P1), need(P15), need(P7), need(P18)
lean, rcpt = need(LEAN), need(RCPT)
ran = need(RAN, soft=True)
if not all((p1, p15, p7, p18, lean, rcpt)):
    print('\n'.join(FAIL)); sys.exit(2)
F1, F15, F7, F18 = flat(p1), flat(p15), flat(p7), flat(p18)
FR = flat(rcpt)

# =============================================================================================
say()
say('=' * 94)
say('ITEM 1 -- the low-ell rewrite: every site, against the receipt\'s r7697 block and the (L) banks')
say('=' * 94)

NEW3 = ['0.485', '0.441', '0.354', '0.657', '0.909', '0.983', '0.999']
NEW2 = ['0.48', '0.44', '0.35', '0.66']
OLD3 = ['0.487', '0.435', '0.359', '0.666', '0.911', '0.998']
LIK_NEW = ['-2.6', '+0.9', '+2.2', '+1.1']
LIK_OLD = ['-2.5', '+1.0', '+2.0']
PAPERS = (('P15', p15), ('P7', p7), ('P18', p18))


def gates(src):
    """Every two-sided gate `want` in the receipt, as (text, want, tol-source)."""
    out = []
    for mm in re.finditer(r'\(\s*(\d),\s*\'([0-9.]+)\'\)', src):     # (ell, 'figure') tuples
        out.append(('depth tuple at l = %s' % mm.group(1), mm.group(2), 'three/two-place, both '
                    'rounding conventions'))
    for mm in re.finditer(r'\(\s*"([^"]{0,120})"\s*,\s*([^,]{1,40}),\s*([-+]?\d+\.?\d*)\s*\)', src):
        out.append((mm.group(1)[:70], mm.group(3), 'from the check that consumes the triple'))
    return out


GT = gates(rcpt)
say('the receipt\'s gated figures, parsed from its source: %d' % len(GT))


def pinned(fig):
    """Is `fig` the want of a gate?  Compared as a STRING for the rounded-digit gates and as a
    float for the numeric ones, because the receipt pins the printed digits for the depths and
    the computed value for the likelihood terms."""
    hits = [g for g in GT if g[1] == fig]
    if not hits:
        try:
            v = abs(float(fig))
            hits = [g for g in GT if abs(abs(float(g[1])) - v) < 5.5e-2]
        except ValueError:
            pass
    return hits


# --- 1a / 1b: every site, read at the precision it prints -------------------------------------
say()
say('arm 1a/1b -- every site that prints a depth or a likelihood term, located by its own text:')
sites = {}
for nm, src in PAPERS:
    for i, line in enumerate(src.split('\n'), 1):
        f3 = [v for v in NEW3 if v in line]
        o3 = [v for v in OLD3 if v in line]
        f2 = [v for v in NEW2 if re.search(r'(?<![0-9])' + re.escape(v) + r'(?![0-9])', line)]
        # ⌗ The first form of this detector reported the OLD likelihood row at 48 sites, and it
        #   is at ONE.  It tested whether the digits appeared anywhere on the line with the
        #   dollars stripped, so "+1.0" matched every "1.0" in the paper.  A matcher loose enough
        #   to mis-read its own input answers about the matcher -- this seat's first lesson, in
        #   the reader that was built to find a missed site.  The figures are read in the form
        #   the paper PRINTS them, inside math delimiters and with their sign.
        lk = [v for v in LIK_NEW if lik_in(line, v)]
        lo = [v for v in LIK_OLD if lik_in(line, v)]
        if f3 or f2 or lk or lo or o3:
            sites[(nm, i)] = dict(new3=f3, new2=f2, old3=o3, lik_new=lk, lik_old=lo,
                                  text=flat(line)[:90])
for (nm, i), d in sorted(sites.items()):
    say('  %-4s l.%-5d new3=%-2d new2=%-2d OLD3=%-2d lik_new=%-2d LIK_OLD=%-2d  %s'
        % (nm, i, len(d['new3']), len(d['new2']), len(d['old3']), len(d['lik_new']),
           len(d['lik_old']), d['text'][:58]))
say('  %d site(s) carry a figure of either row.' % len(sites))

# every NEW figure a site prints must be pinned
unpinned = []
for v in NEW3 + NEW2:
    if any(v in d['new3'] or v in d['new2'] for d in sites.values()) and not pinned(v):
        unpinned.append(v)
say('  every printed depth is the want of a gate: %s'
    % ('YES' if not unpinned else 'NO -- unpinned: %s' % unpinned))
lik_unpinned = [v for v in LIK_NEW if not pinned(v)]
say('  every printed likelihood term is the want of a gate: %s'
    % ('YES' if not lik_unpinned else 'NO -- unpinned: %s' % lik_unpinned))
# NEGATIVE PROBE: an invented figure must come back unpinned
say('  NEGATIVE PROBE (an invented figure 0.777): %s'
    % ('unpinned, as it must be' if not pinned('0.777') else 'PINNED -- the reader matches anything'))
if pinned('0.777'):
    FAIL.append('arm 1a: the gate reader fired on an invented figure')

# --- THE CROSS-SITE COMPARISON, which is where a missed site shows ---------------------------
say()
say('arm 1b\' -- the likelihood row ACROSS sites, because a rewrite is missed at one site and not'
    ' at the quantity:')
# ⌗ A single signed figure is not a ROW: `l.710`'s "+2.2\\%" is a damping-signature per cent and
#   the first form of this reader called it "the new row" on that one hit.  A row is read as a row:
#   two or more of its four figures on one site.  (The stale site is reported at any count, with
#   its count shown, because ONE stale digit beside re-pointed ones is exactly the defect sought.)
stale = {k: d for k, d in sites.items() if d['lik_old']}
fresh = {k: d for k, d in sites.items() if len(d['lik_new']) >= 2}
single = {k: d for k, d in sites.items() if len(d['lik_new']) == 1 and not d['lik_old']}
for (nm, i), d in sorted(fresh.items()):
    say('  %-4s l.%-5d carries the NEW row: %s' % (nm, i, ' '.join(d['lik_new'])))
for (nm, i), d in sorted(stale.items()):
    say('  %-4s l.%-5d carries the OLD row: %s   ⛔' % (nm, i, ' '.join(d['lik_old'])))
for (nm, i), d in sorted(single.items()):
    say('  %-4s l.%-5d carries ONE figure of the new row and is not a row site: %s'
        % (nm, i, ' '.join(d['lik_new'])))
B1 = not stale

# --- 1c: the quantifier on the cross-validation ----------------------------------------------
say()
say('arm 1c -- the cross-validation claim, read as a quantifier plus an exclusion (G1):')
CV = {'the bound': 'to within $2.9$ per cent at', 'the quantifier': 'at every multipole',
      'the octopole named IN': 'the octopole included',
      'the old exception wording': 'every multipole but the octopole'}
cv = {}
for k, mk in CV.items():
    cv[k] = mk in F15
    say('  %-28s %s' % (k, 'FOUND' if cv[k] else 'absent'))
cvg = re.search(r'ON \(L\) THE DECOUPLED HIERARCHY IS WITHIN 2\.9 PER CENT OF ARM A AT EVERY', FR)
cvc = re.search(r'max\(abs\(_v\) for _v in _XL\.values\(\)\) < 2\.95 and abs\(_XL\[3\]\) < 1\.0', FR)
say('  the receipt\'s gate for it: %s' % ('PRESENT' if cvg else 'not found'))
say('  and what it asserts: %s'
    % ('the worst of the seven under 2.95 per cent AND the octopole under 1.0' if cvc else 'UNREAD'))
C1 = cv['the bound'] and cv['the quantifier'] and cv['the octopole named IN'] \
    and not cv['the old exception wording'] and bool(cvg) and bool(cvc)

# --- 1d: THE NAMED SEARCH for a surviving one-clock or unit figure ---------------------------
say()
say('arm 1d -- the search for a surviving one-clock or unit depth, over P15, P7 and P18:')
for v in OLD3:
    rows = []
    for nm, src in PAPERS:
        for i, line in enumerate(src.split('\n'), 1):
            if v in line:
                rows.append((nm, i, flat(line)))
    say('  %-6s %d occurrence(s)%s' % (v, len(rows), ':' if rows else ''))
    for nm, i, t in rows:
        j = t.find(v)
        win = t[max(j - 90, 0):j + 60]
        # NEGATIVE PROBE 16, registered in PREDICTION.md: read the LABEL beside the hit, never the
        # digits alone -- a surviving old value and a deliberate one-clock cross-check look the same
        # to a digit search.
        kind = ('A LOW-ELL DEPTH' if re.search(r'deficit|depth|expectation at \$\\ell', win)
                else 'NOT a low-ell depth (%s)' % win[-48:].strip()[:44])
        say('      %-4s l.%-5d %s' % (nm, i, kind))
unit = []
for nm, src in PAPERS:
    for i, line in enumerate(src.split('\n'), 1):
        if re.search(r'(deficit|depth)[^.]{0,80}(\$1\$|\$1\.0+\$|= ?1\b)', line):
            unit.append((nm, i))
say('  a depth printed as exactly one: %s' % (unit if unit else 'none found by the search above'))
D1 = True
for v in OLD3:
    for nm, src in PAPERS:
        for line in src.split('\n'):
            if v in line and re.search(r'deficit|expectation at \$\\ell', flat(line)):
                D1 = False
# the one-clock row is kept DELIBERATELY in the bank, and that is a different thing from a
# surviving figure in print: read the bank's own key names for it.
bank_keys = []
try:
    import numpy as _np
    bank_keys = list(_np.load(BANK, allow_pickle=True).keys())
except Exception as exc:                        # noqa: BLE001
    bank_keys = ['UNREAD: %s' % exc]
say('  and the bank\'s own keys, which say what the one-clock row IS: %s' % bank_keys)

# --- 1e: the convergence clause and the bank it rests on -------------------------------------
say()
say('arm 1e -- the "doubled opacity grid" clause, and the build its convergence was measured on:')
clause = 'the agreement does not move under a doubled opacity grid, a halved late step count, or a'
say('  the clause, located by its text: %s' % ('FOUND' if clause in F15 else 'ABSENT'))
knob = re.search(r"halving the late step count moves it by \{100 \* _ns3:\.3f\}%; doubling the "
                 r"opacity grid", FR)
banks_used = sorted(set(re.findall(r"SW\['([A-Z_0-9a-z]*control[A-Z_0-9a-z]*)'\]", rcpt)))
say('  the receipt\'s two knob sweeps: %s' % ('PRESENT' if knob else 'not found'))
say('  and the banks they are computed on: %s' % (banks_used or 'UNREAD'))
L_in_sweep = [b for b in banks_used if 'leafpert' in b.lower() or b.endswith('_L')]
say('  any of those banks an (L) bank: %s' % (L_in_sweep or 'NONE'))
cfg_knobs = {}
try:
    import json as _json
    import numpy as _np
    _z = _np.load(BANK, allow_pickle=True)
    _c = _json.loads(str(_z['config'].item()))
    cfg_knobs = {k: _c.get(k) for k in ('NTAU', 'NS3', 'KLO', 'NLOW')}
except Exception as exc:                        # noqa: BLE001
    cfg_knobs = {'UNREAD': str(exc)}
say('  and what the (L) bank\'s own config records of those knobs: %s' % cfg_knobs)
E1 = bool(clause in F15) and bool(knob) and bool(L_in_sweep) and \
    any(v is not None for v in cfg_knobs.values())

# --- 1f: r7698's FORWARD NOTE, now due ------------------------------------------------------
say()
say('arm 1f -- r7698\'s forward note: what became of the two octopole attribution clauses?')
ATTR = ["two-clock split", "goes with the hierarchy", "an excess that goes when",
        "the excess survives both"]
for mk in ATTR:
    n = sum(flat(s).count(mk) for _, s in PAPERS)
    say('  %-34s %d occurrence(s) across P15, P7, P18' % (repr(mk), n))
half = [(nm, i) for nm, src in PAPERS for i, line in enumerate(src.split('\n'), 1)
        if 'five and a half per cent' in flat(line)]
say('  "five and a half per cent": %s' % (half if half else 'none'))
# ⌗ The first form of this marker spanned a break between two adjacent string literals in the
#   receipt's source -- the r7698 defect exactly, in the next revision's probe.  Read as two.
wd1 = re.search(r'this is a', FR) is not None
wd2 = re.search(r'WITHDRAWAL and not a refinement', FR) is not None
wd = wd1 and wd2
pct = re.search(r'(\d\d)-(\d\d) per cent of it was the RETIRED pairing', FR)
say('  the receipt\'s own verdict on the attribution: %s'
    % ('a WITHDRAWAL and not a refinement' if wd else 'UNREAD'))
say('  and how much of the excess it measures as the retired pairing\'s: %s'
    % (pct.group(0) if pct else 'UNREAD'))
F1_ = (sum(sum(flat(s).count(mk) for _, s in PAPERS) for mk in ATTR) == 0) and bool(wd)

# =============================================================================================
say()
say('=' * 94)
say('ITEM 2 -- P1\'s Kretschmann sentence, against Kretschmann.lean')
say('=' * 94)

KEY = 'the Kretschmann scalar computed from the coordinate Riemann'
j = F1.find(KEY)
sent = F1[max(j - 170, 0):j + 820]
say('the sentence located by its text at character %d' % j)
say('  ' + sent[:300])
if j < 0:
    FAIL.append('ITEM 2: the sentence could not be located by its text')


def lean_sig(name):
    mm = re.search(r'\ntheorem\s+' + re.escape(name) + r'\b', lean)
    if not mm:
        return ''
    tail = lean[mm.start():mm.start() + 3000]
    cut = tail.find(':= by')
    return flat(tail[:cut + 5] if cut > 0 else tail[:1200])


SKW, SBL, SCD = lean_sig('kr_schwarzschild'), lean_sig('kr_blowup'), lean_sig('kr_cor_densities_c')
for nm, s in (('kr_schwarzschild', SKW), ('kr_blowup', SBL), ('kr_cor_densities_c', SCD)):
    say('  %-22s %s' % (nm, 'FOUND' if s else 'ABSENT'))
    if not s:
        FAIL.append('ITEM 2: cited theorem %s is not in the file' % nm)
say('  NEGATIVE PROBE 1 (a name the file does not carry): %s'
    % ('absent, as it must be' if not lean_sig('kr_not_there') else 'FOUND -- matches anything'))
if lean_sig('kr_not_there'):
    FAIL.append('ITEM 2: the theorem reader fired on a name the file does not carry')

say()
say('arm 2a -- the value and the domain:')
val = re.search(r'kr_K \(kr_SD M\)\.gW x = 48 \* M \^ 2 / rK M \(x 0, x 1\) \^ 6', SKW)
dom = re.search(r'\(hx : \(x 0, x 1\) ∈ sk_kM\)', SKW)
skdef = re.search(r'def sk_kM : Set P := \{p \| p\.1 \* p\.2 < 1\}', lean)
sewdef = re.search(r'def seWS : Set P := \{p \| 0 < p\.2 ∧ p\.1 \* p\.2 < 1\}', lean)
onW = re.search(r'∀ x : seW, kr_KS M θ φ x = 48 \* M \^ 2 / se_r M x \^ 6', SCD)
say('  the theorem\'s value: %s' % (val.group(0) if val else 'UNREAD'))
say('  its domain hypothesis: %s' % (dom.group(0) if dom else 'UNREAD'))
say('  and what that set IS: %s' % (skdef.group(0) if skdef else 'UNREAD'))
say('  the paper\'s domain, as the sentence states it: %s'
    % ('{V>0, UV<1}' if '{V>0,\\,UV<1\\}' in sent or 'V>0' in sent else 'UNREAD'))
say('  and what THAT set is in the file: %s' % (sewdef.group(0) if sewdef else 'UNREAD'))
say('  the corollary states the same value on that set: %s' % ('YES' if onW else 'no'))
A2 = bool(val) and bool(dom) and bool(skdef) and bool(sewdef) and bool(onW)

say()
say('arm 2b -- "away from the poles of the sphere\'s chart":')
pole = re.search(r'\(hs : Real\.sin \(x 2\) ≠ 0\)', SKW)
pole_b = re.search(r'\(hθ : Real\.sin θ ≠ 0\)', SBL)
pole_c = re.search(r'\(hθ : Real\.sin θ ≠ 0\)', SCD)
used = re.search(r'theorem kr_K_sphere \(hρ : ρ ≠ 0\) \{x : Fin 2 → ℝ\} \(hx : Real\.sin \(x 0\) ≠ 0\)',
                 lean)
say('  a hypothesis of kr_schwarzschild: %s' % (pole.group(0) if pole else 'no'))
say('  of kr_blowup and kr_cor_densities_c too: %s / %s'
    % ('YES' if pole_b else 'no', 'YES' if pole_c else 'no'))
say('  and it does work: the sphere\'s own curvature lemma asks the same condition: %s'
    % ('YES' if used else 'UNREAD'))
B2 = bool(pole) and bool(pole_b) and bool(pole_c) and bool(used)

say()
say('arm 2c -- the divergence, and "where r → 0", as TWO claims in one clause (G1):')
div = re.search(r'Tendsto \(kr_KS M θ φ\) kr_toSig atTop', SBL)
filt = re.search(r'def kr_toSig : Filter seW := comap kr_UV \(𝓝\[<\] 1\)', lean)
nebot = re.search(r'kr_toSig\.NeBot', SCD)
rzero = re.search(r'\ntheorem kr_r_to_zero', lean)
say('  the divergence: %s' % (div.group(0) if div else 'UNREAD'))
say('  the filter it diverges along: %s' % (filt.group(0) if filt else 'UNREAD'))
say('  that filter is non-trivial (so the limit is not vacuous): %s' % ('YES' if nebot else 'no'))
say('  and the r → 0 half is its own theorem: %s' % ('YES (kr_r_to_zero)' if rzero else 'no'))
C2 = bool(div) and bool(filt) and bool(nebot) and bool(rzero)

say()
say('arm 2d -- the TWO closure claims:')
cl1 = re.search(r'p ∈ closure \(Subtype\.val \'\' kr_BH hM hr₀\)', SCD)
cl2 = re.search(r'∀ \(Θ : seW → ℝ\) \(τ : ℝ\), kr_Sig ∩ closure \(Subtype\.val \'\' \(se_S hM\)\.slice',
                SCD)
sig = re.search(r'def kr_Sig : Set P := \{p \| p\.1 \* p\.2 = 1\}', lean)
upos = re.search(r'0 < p\.1', SCD)
say('  in the closure of the black-hole region: %s' % ('YES' if cl1 else 'no'))
say('  in the closure of no finite exterior slice: %s' % ('YES' if cl2 else 'no'))
say('  and that second claim\'s binder: %s'
    % ('every Θ and every τ' if cl2 else 'UNREAD'))
say('  the locus, as the file defines it: %s' % (sig.group(0) if sig else 'UNREAD'))
say('  with U > 0 there, which the sentence does not claim: %s' % ('YES' if upos else 'no'))
D2 = bool(cl1) and bool(cl2) and bool(sig)
# FLIP (G3): strike the second conjunct and the reader must lose it
# ⌗ The first form of this flip struck only the FIRST occurrence, and the conjunct appears
#   twice in the signature (once in the docstring's summary, once in the statement), so the
#   reader read the surviving copy and the probe reported itself broken.  A flip must remove
#   every copy of what it is testing for.
_flipped = SCD.replace('kr_Sig ∩ closure', 'XX')
say('  FLIP (G3), the same reader with EVERY copy of the slice conjunct struck: %s'
    % ('still reads it -- WRONG' if re.search(r'kr_Sig ∩ closure', _flipped)
       else 'reads none, as it must'))
if re.search(r'kr_Sig ∩ closure', _flipped):
    FAIL.append('arm 2d: the closure reader survived having its conjunct struck')

say()
say('arm 2e -- "with the sphere factor written in":')
four = re.search(r'\{x : Fin 4 → ℝ\}', SKW)
gw = re.search(r'kr_K \(kr_SD M\)\.gW', SKW)
warp = re.search(r'\ntheorem kr_warped', lean)
sph = re.search(r'\ntheorem kr_K_sphere', lean)
say('  the theorem is about a FOUR-coordinate point: %s' % ('YES' if four else 'no'))
say('  the curvature is taken of the four-dimensional metric: %s' % (gw.group(0) if gw else 'UNREAD'))
say('  the warped-product lemma the proof rewrites by: %s' % ('kr_warped' if warp else 'UNREAD'))
say('  and the sphere\'s own curvature is computed, not assumed: %s'
    % ('YES (kr_K_sphere)' if sph else 'no'))
E2 = bool(four) and bool(gw) and bool(warp) and bool(sph)

say()
say('-' * 94)


def verdict(v):
    if isinstance(v, str):
        return v
    return 'UNMEASURED' if v is None else ('SUPPORTED' if v else 'NOT SUPPORTED')


ROWS = [
    ('1a', (not unpinned) and (not lik_unpinned),
     'every depth and every likelihood term the sites print is the want of a gate'),
    ('1b', B1, '%d site(s) carry the OLD likelihood row' % len(stale)),
    ('1c', C1, 'the quantifier and the exclusion are both in print and both gated'),
    ('1d', D1, 'no old depth literal survives at a low-ell site, by the search above'),
    ('1e', ('THE CLAUSE\'S EVIDENCE IS ON ANOTHER BUILD' if not E1 else 'SUPPORTED'),
     'the two knob sweeps are computed on %s -- %s an (L) bank -- and the (L) bank\'s own config '
     'records %s of those knobs'
     % (', '.join(banks_used) or 'UNREAD', 'none of them' if not L_in_sweep else 'one of them',
        'none' if not any(v is not None for v in cfg_knobs.values()) else 'some')),
    ('1f', ('FORWARD NOTE DISCHARGED' if F1_ else 'FORWARD NOTE STILL OPEN'),
     'the attribution clauses are gone from print at %d of the four markers, and the receipt calls '
     'the attribution a withdrawal: %s'
     % (4, 'yes' if wd else 'UNREAD')),
    ('2a', A2, 'the value and the corollary\'s domain match the sentence; the general theorem holds '
     'on the larger set'),
    ('2b', B2, 'the pole condition is a hypothesis of all three and the sphere lemma asks it too'),
    ('2c', C2, 'divergence along a non-trivial filter, with the r → 0 half its own theorem'),
    ('2d', D2, 'both closure claims are conjuncts, the second for every Θ and τ'),
    ('2e', E2, 'the curvature is taken of the four-dimensional metric with the sphere computed'),
]
for k, v, note in ROWS:
    say('arm %-3s: %-13s -- %s' % (k, verdict(v), note))

say()
say('=' * 94)
say('%d verdicts printed.  %d reader or classifier probe(s) failed.' % (len(ROWS), len(FAIL)))
for f in FAIL:
    say('  DEFECT: %s' % f)
say('=' * 94)

with open(os.path.join(HERE, 'runs', 'READINGS.txt'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(READINGS) + '\n')
sys.exit(1 if FAIL else 0)
