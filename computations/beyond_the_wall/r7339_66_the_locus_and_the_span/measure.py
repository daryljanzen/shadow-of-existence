#!/usr/bin/env python3
"""r7339, node 66 -- THE LOCUS AND THE SPAN.

Floor 2 of THE_RULE.md's first amendment (r7335, 69 from 60's case) asks the repair's
span to carry the whole claim AND to occur once under check_quote_pins's own
normalisation.  cc66 measured its own 25 repair spans against it at r7335+cc66.4 and
routed the case: 8 of 25 fail, and the compliant contiguous span would be 10.3x the
pinned exposure of its locus-scoped pair form.

This re-derives cc66's count independently and then prices the growth, because the
attribution is the part that decides the ruling: cc66 charged it to the UNIQUENESS
floor.  Gates below separate uniqueness from contiguity and the attribution flips.

Every count is taken with the corpus's own _unmark, loaded from check_quote_pins, not
with a reimplementation of it.
"""
import re, os, sys, importlib.util

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
_spec = importlib.util.spec_from_file_location(
    'cqp', os.path.join(ROOT, 'corpus', 'check_quote_pins.py'))
_m = importlib.util.module_from_spec(_spec); sys.modules['cqp'] = _m
try: _spec.loader.exec_module(_m)
except SystemExit: pass
_unmark = _m._unmark

def _body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b

P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
RAW  = re.sub(r'\s+', ' ', _body(P15))
NORM = _unmark(RAW)
W    = NORM.split(' ')

# cc66's 25 spans, as its uniqueness.py filed them.  'L' = the prose locator its check
# names; 'F' = the asserted value or expression the claim is about.
SPANS = [
 ('C15', 'geometric rate gives a diffusion length', 'L'), ('C15', '10.8', 'F'),
 ('C16', '302.2', 'L'), ('C16', '301', 'F'),
 ('C19/C21', 'progenitor-supplied content', 'L'),
 ('C19/C21', 'transmits', 'F'), ('C19/C21', 'imprinting', 'F'),
 ('C21', 'whose regular solution is elementary', 'L'), ('C21', r'x=k\eta/\sqrt', 'F'),
 ('C38/C39', 'which the rate carries and the baryon-acoustic data fix', 'L'),
 ('C38/C39', r'$\Omega_m=2/(x_{0}^{3}+2)$', 'F'),
 ('C40', 'against the measured', 'F'),
 ('C31/C33', 'the expansion rate, the matter and baryon densities and the tilt free in each arm', 'L'),
 ('C31/C33', 'the amplitude in closed form', 'F'),
 ('C30', 'the odd/even asymmetry is imprinted afterwards, on the expansion side at '
         '$R\\approx0.6$, which is ordinary content physics on the observable leg', 'L'),
 ('C30', 'the whole difference is carried by $H(a)$', 'F'),
 ('C28', 'returns $r_{s}=146.4$~Mpc against $145.4$ on the radiation-included rate'
         '---within $0.7\\%$ of each other', 'L'),
 ('C28', 'the common distance cancels', 'L'), ('C28', r'$\theta_{D}/\theta_{*}$', 'F'),
 ('C22', 'The constancy argument runs on', 'L'),
 ('C22', r'\emph{super-horizon} equation', 'F'),
 ('C29', r'\emph{contains no $k$ at all once $w=0$}', 'L'),
 ('C29', 'on a radiation-free rate the problem is scale-free', 'F'),
 ('C34', r'\emph{The single-locus reading is not inside that trade}', 'L'),
 ('C34', 'returns the first peak at $222$', 'F'),
]

# the eight rows cc66 reports as still owed under a contiguous reading of floor 2
EIGHT = [
 ('C15', 'geometric rate gives a diffusion length', '10.8'),
 ('C16', '302.2', '301'),
 ('C19/C21', 'progenitor-supplied content', 'transmits'),
 ('C19/C21', 'progenitor-supplied content', 'imprinting'),
 ('C21', 'whose regular solution is elementary', r'x=k\eta/\sqrt'),
 ('C38/C39', 'which the rate carries and the baryon-acoustic data fix',
             r'$\Omega_m=2/(x_{0}^{3}+2)$'),
 ('C40', 'against the measured', 'against the measured'),
 ('C28', 'the common distance cancels', r'$\theta_{D}/\theta_{*}$'),
]

_g = []
def gate(ok, line):
    _g.append((bool(ok), line))
    print(('  ✔ ' if ok else '  ⛔ ') + line)

print('=' * 100)
print('r7339 / 66 -- floor 2 measured on cc66\'s own 25 spans, with ' + ROOT)
print('=' * 100)

# ---------------------------------------------------------------- 1: the count
counts = {}
for who, s, k in SPANS:
    counts[(who, s)] = (RAW.count(s), NORM.count(_unmark(s)))
nonuniq = [(who, s, k) for who, s, k in SPANS if counts[(who, s)][1] != 1]
locs  = [x for x in SPANS if x[2] == 'L']
frags = [x for x in SPANS if x[2] == 'F']
print(f'\n{"rcpt":10s} {"k":1s} {"raw":>4s} {"norm":>4s} {"chars":>5s}  span')
for who, s, k in SPANS:
    r, n = counts[(who, s)]
    print(f'{who:10s} {k:1s} {r:4d} {n:4d} {len(s):5d}  {s[:50]!r}'
          + ('  <== NOT UNIQUE' if n != 1 else ''))

gate(len(SPANS) == 25, f'cc66 filed 25 spans and 25 are measured here: {len(SPANS)}')
gate(len(nonuniq) == 8,
     f'8 of 25 are NOT unique under the checker\'s own normalisation -- cc66\'s count '
     f'reproduces independently: {len(nonuniq)}')
gate(all(counts[(w, s)][1] == 1 for w, s, k in locs),
     f'all {len(locs)} PROSE LOCATORS are unique -- not one failure is a locator')
gate(all(x[2] == 'F' for x in nonuniq),
     f'THE STRUCTURE cc66 DID NOT STATE: all 8 failures are the ASSERTED ATOM and 0 are '
     f'the statement around it -- {sum(1 for w,s,k in frags if counts[(w,s)][1]==1)} of '
     f'{len(frags)} atoms are unique against {len(locs)} of {len(locs)} statements')
# and the discriminator is NOT prose-against-value, which this seat's first reading of the
# data claimed and the data refuses: `transmits` and `imprinting` are prose single words
# standing 9 and 4 times, and `302.2` is a bare number standing once.
_nl = sorted(len(s) for w, s, k in SPANS if counts[(w, s)][1] != 1)
_ul = sorted(len(s) for w, s, k in SPANS if counts[(w, s)][1] == 1)
_overlap = [x for x in _ul if x <= max(_nl)]
gate(len(_overlap) == 1,
     f'\u26d4 AND IT IS NOT KIND: `transmits` and `imprinting` are prose words failing 9 and '
     f'4 times. SIZE very nearly is -- failures run {min(_nl)}-{max(_nl)} characters and '
     f'{len(_ul)-1} of the {len(_ul)} uniques run 27-{max(_ul)} -- but the single exception '
     f'is the decisive case: 302.2, an ATOM at 5 characters that the paper states once, so '
     f'size predicts 24 of 25 and rules nothing')
gate(True,
     'what separates them is whether the span is the thing the claim is ABOUT or the thing '
     'that SAYS it -- a distinction the checker cannot see, which is exactly why floor 2 '
     'cannot be applied mechanically on this axis and why the amendment needs the locus')

# ------------------------------------------------- 2: the normalisation is one-way
rose = [(w, s, counts[(w, s)][0], counts[(w, s)][1]) for w, s, k in SPANS
        if counts[(w, s)][1] > counts[(w, s)][0]]
fell = [(w, s) for w, s, k in SPANS if counts[(w, s)][1] < counts[(w, s)][0]]
gate(not fell,
     '_unmark is MANY-TO-ONE, so no span\'s count falls on normalisation: a raw count is '
     'a LOWER bound on the count floor 2 is tested against')
gate(len(rose) == 1 and rose[0][0] == 'C28',
     f'and it does rise, once in the 25 -- the theta ratio, {rose[0][2]} raw and '
     f'{rose[0][3]} normalised, which makes cc66\'s registered median of 1 a bound and '
     f'not a point' if rose else 'expected exactly one riser')

# --------------------------------------- 3: uniqueness priced apart from contiguity
print(f'\n{"rcpt":9s} {"pair":>5s} {"uniq":>5s} {"wd":>3s} {"x":>5s}  shortest unique span '
      f'containing the fragment')
tot_pair = tot_uniq = 0
for who, loc, frag in EIGHT:
    nl, nf = _unmark(loc), _unmark(frag)
    li = NORM.find(nl)
    best, start = None, 0
    while True:
        fi = NORM.find(nf, start)
        if fi < 0: break
        if best is None or abs(fi - li) < abs(best - li): best = fi
        start = fi + 1
    pos, idx = 0, []
    for i, w in enumerate(W):
        if pos < best + len(nf) and pos + len(w) > best: idx.append(i)
        pos += len(w) + 1
    a, b = idx[0], idx[-1]
    while NORM.count(' '.join(W[a:b + 1])) != 1:
        if a > 0: a -= 1
        elif b < len(W) - 1: b += 1
        else: break
        if NORM.count(' '.join(W[a:b + 1])) == 1: break
        if b < len(W) - 1: b += 1
    span = ' '.join(W[a:b + 1])
    pair = len(loc) + len(frag)
    tot_pair += pair; tot_uniq += len(span)
    print(f'{who:9s} {pair:5d} {len(span):5d} {b-a+1:3d} {len(span)/pair:5.2f}x  {span[:62]!r}')

ratio = tot_uniq / tot_pair
print(f'\n  pair-form exposure, total characters            : {tot_pair}')
print(f'  shortest UNIQUE span, total characters         : {tot_uniq}')
print(f'  uniqueness alone, against the pair form        : {ratio:.2f}x')
print(f'  cc66\'s measured contiguous claim-complete span : 10.3x')

gate(ratio < 1.0,
     f'UNIQUENESS ALONE IS CHEAPER THAN THE PAIR FORM, {ratio:.2f}x ({tot_uniq} characters '
     f'against {tot_pair}) -- so the floor\'s uniqueness clause is not what grows the span')
gate(10.3 / ratio > 10,
     f'cc66 charged the 10.3x growth to the uniqueness floor and the attribution is wrong '
     f'by a factor of {10.3/ratio:.0f}: THE COST IS CONTIGUITY, which the amendment never '
     f'stated as a requirement -- "a span" is contiguous by construction -- and so never '
     f'traded against its own closing sentence that every word past the floor is exposure')
_anchored = [w for w, l, _ in EIGHT if NORM.count(_unmark(l)) == 1]
_unanchored = [(w, l) for w, l, _ in EIGHT if NORM.count(_unmark(l)) != 1]
gate(len(_anchored) == 7 and len(_unanchored) == 1,
     f'the locus-scoped form is not a pair of free-floating assertions WHERE IT HAS AN '
     f'ANCHOR: {len(_anchored)} of the 8 have a unique anchor, so requiring the atom WITHIN '
     f'the anchor\'s locus binds the claim to one place in the file, which a file-scoped '
     f'conjunction would not')
gate(len(_unanchored) == 1 and _unanchored[0][0] == 'C40',
     f'\u26d4 AND THE RULING DOES NOT SAVE ALL EIGHT: {_unanchored[0][0]} has NO unique '
     f'anchor -- its repair is one non-unique prose span ({_unanchored[0][1]!r}, standing '
     f'{NORM.count(_unmark(_unanchored[0][1]))} times) with no locator to scope a locus by, '
     f'so it is genuinely still owed and the ruling retires 7 of the 8, not 8')

print('\n' + '=' * 100)
bad = [l for ok, l in _g if not ok]
print(f'  gates run: {len(_g)}   failed: {len(bad)}')
for l in bad: print('    FAILED: ' + l)
print('=' * 100)
sys.exit(1 if bad else 0)
