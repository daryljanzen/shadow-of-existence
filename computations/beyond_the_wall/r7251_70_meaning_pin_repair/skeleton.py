#!/usr/bin/env python3
"""r7251+70.2 -- the CONTENT-SKELETON repair form, tried on the three drawn members of 60's 162 PAPER/SENTENCE keys.

The form, as pre-registered: a sentence's finding is carried by its content tokens and its polarity markers, not
its prose.  The repaired gate asserts that ONE sentence of the paper (after a markup normaliser in cc66's spirit)
contains every skeleton token and the polarity marker.

Each member is run against: (a) the paper as it stands; (b) content-intact rewordings, which must stay GREEN;
(c) content-breaking edits, which must go RED.  The mutations are written out IN FULL below so a reader can judge
whether each (b) really keeps the content and each (c) really breaks it.  They were written after reading the
members -- the draw made that unavoidable -- and that is why they are published rather than generated.

Exit 0 always: this is a measurement, and its verdict is in the printed table, not in a pass/fail gate.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def norm(t):
    t = re.sub(r'\\(?:emph|textbf|textit)\{([^}]*)\}', r'\1', t)
    t = re.sub(r'[\\${}~]', ' ', t).replace('---', ' , ').replace('--', ' ')
    return re.sub(r'\s+', ' ', t).lower()


def sentences(t):
    return re.split(r'(?<=[.;:])\s+', norm(t))


def gate(text, skeleton, polarity):
    """GREEN iff one sentence carries every skeleton token and every polarity marker."""
    return any(all(k in s for k in skeleton) and all(re.search(r'\b' + p + r'\b', s) for p in polarity)
               for s in sentences(text))


def sentence_of(path, key):
    t = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', path), encoding='utf-8').read())
    i = t.find(key)
    assert i >= 0, (path, key)
    a, b = t.rfind('. ', 0, i) + 2, t.find('. ', i) + 1
    return t, t[a:b]


MEMBERS = []

# ---- member 1: B2, groupoid_paper.tex -- "only the order-two subgroup---complex conjugation of the pair---is
#      realised on the real structure" (over-critical regime).  Finding: a RESTRICTION (only Z2 of S3 is realised).
full, s = sentence_of('groupoid_paper.tex', 'complex conjugation of the pair')
MEMBERS.append(dict(
    name='B2 / complex conjugation of the pair', paper=full, sent=s,
    skeleton=['over-critical', 'order-two subgroup', 'complex conjugation', 'real structure'], polarity=['only'],
    keep=[  # (b) content-intact
        ('markup', s.replace('complex conjugation of the pair', r'\emph{complex conjugation} of the pair')),
        ('synonym', s.replace('is realised on', 'is represented on')),
        ('dash->comma', s.replace('---complex conjugation of the pair---', ', namely complex conjugation of the pair,')),
        ('reorder', s.replace('only the order-two subgroup---complex conjugation of the pair---is realised on the real structure',
                              'what is realised on the real structure is only the order-two subgroup, complex conjugation of the pair')),
        ('split', s.replace('whereas in the over-critical regime', '. In the over-critical regime, by contrast,')),
    ],
    break_=[  # (c) content-breaking
        ('polarity dropped', s.replace('only the order-two subgroup', 'the order-two subgroup')),
        ('object swapped', s.replace('only the order-two subgroup---complex conjugation of the pair---', 'only the order-three subgroup---the cyclic permutation of the roots---')),
        ('regimes exchanged', s.replace('under-critical', 'XX').replace('over-critical', 'under-critical').replace('XX', 'over-critical')),
        ('restriction inverted', s.replace('only the order-two subgroup---complex conjugation of the pair---is realised', 'all of $S_{3}$, and not only the order-two subgroup---complex conjugation of the pair---, is realised')),
    ]))

# ---- member 2: B8, matter_sector_paper.tex -- "the module the operator's colour structure acts on is the
#      branching rather than any bundle of the substrate".  Finding: an IDENTIFICATION with an exclusion.
full, s = sentence_of('matter_sector_paper.tex', "the module the operator's colour structure acts on is the branch")
MEMBERS.append(dict(
    name="B8 / the module ... is the branching", paper=full, sent=s,
    skeleton=['module', 'colour structure', 'branching', 'bundle of the substrate'], polarity=['rather than'],
    keep=[
        ('markup', s.replace('the branching', r'the \emph{branching}')),
        ('synonym', s.replace('acts on', 'acts upon')),
        ('reorder', s.replace("the module the operator's colour structure acts on is the branching rather than any bundle of the substrate",
                              "the branching, rather than any bundle of the substrate, is the module the operator's colour structure acts on")),
        ('not-X-but-Y', s.replace("is the branching rather than any bundle of the substrate",
                                  "is not any bundle of the substrate but the branching")),
    ],
    break_=[
        ('converse', s.replace("is the branching rather than any bundle of the substrate",
                               "is a bundle of the substrate rather than the branching")),
        ('polarity dropped', s.replace("rather than any bundle of the substrate", "and any bundle of the substrate")),
        ('object swapped', s.replace("is the branching", "is the wall kernel")),
    ]))

# ---- member 3: B37, geometric_core_paper.tex -- "the winding quantises without measuring, the flat bundle
#      selects without coupling, and the branch point filters without supplying".  Finding: three asymmetric pairs.
full, s = sentence_of('geometric_core_paper.tex', 'quantises without measuring')
MEMBERS.append(dict(
    name='B37 / quantises without measuring', paper=full, sent=s,
    skeleton=['winding', 'quantis', 'measur'], polarity=['without'],
    keep=[
        ('markup', s.replace('quantises without measuring', r'\emph{quantises} without measuring')),
        ('inflection', s.replace('the winding quantises without measuring', 'the winding does its quantising without measuring')),
        ('reorder', s.replace('the winding quantises without measuring', 'without measuring, the winding quantises')),
        ('synonym', s.replace('three verdicts reached separately', 'three verdicts arrived at independently')),
    ],
    break_=[
        ('converse', s.replace('the winding quantises without measuring', 'the winding measures without quantising')),
        ('polarity flipped', s.replace('quantises without measuring', 'quantises by measuring')),
        ('object swapped', s.replace('the winding quantises', 'the flat bundle quantises').replace('the flat bundle selects', 'the winding selects')),
    ]))

def gate_clause(text, skeleton, polarity):
    """VARIANT 1 (not registered): every token and marker inside ONE CLAUSE (split at , ; : and dashes)."""
    return any(all(k in c for k in skeleton) and all(re.search(r'\b' + p + r'\b', c) for p in polarity)
               for s in sentences(text) for c in re.split(r'\s*[,;:()]\s*', s))


def gate_ordered(text, skeleton, polarity):
    """VARIANT 2 (not registered): sentence scope, tokens in the ORDER the finding states them."""
    seq = skeleton[:]
    pat = '.*'.join(re.escape(k) for k in seq)
    return any(re.search(pat, s) and all(re.search(r'\b' + p + r'\b', s) for p in polarity) for s in sentences(text))


def run(g, label):
    print(f'\n  ** {label} **')
    print(f'  {"member":42s} {"(a)":4s} {"(b) green":10s} {"(c) red":9s}')
    tb = tbn = tc = tcn = npass = 0
    for m in MEMBERS:
        others = [x for x in re.split(r'(?<=[.;:])\s+', m['paper'])
                  if x.strip() and x not in m['sent'] and g(x, m['skeleton'], m['polarity'])]
        a = g(m['paper'], m['skeleton'], m['polarity'])
        kb = [(lab, g(m['paper'].replace(m['sent'], x), m['skeleton'], m['polarity'])) for lab, x in m['keep']]
        # a content-BREAKING edit must make the finding false in the PAPER, so every other sentence that states
        # it is removed for (c) -- otherwise the edit leaves the finding true and a green is correct
        broken = m['paper']
        for o in others: broken = broken.replace(o, ' ')
        kc = [(lab, g(broken.replace(m['sent'], x), m['skeleton'], m['polarity'])) for lab, x in m['break_']]
        nb, nc = sum(x for _, x in kb), sum(not x for _, x in kc)
        tb += nb; tbn += len(kb); tc += nc; tcn += len(kc)
        ok = a and nb == len(kb) and nc == len(kc); npass += ok
        print(f'  {m["name"]:42s} {"G" if a else "R":4s} {nb}/{len(kb):<8d} {nc}/{len(kc):<7d} '
              f'{"PASSES" if ok else "FAILS"}   (other stating sentences removed for (c): {len(others)})')
        for lab, x in kb:
            if not x: print(f'        (b) RED on a content-intact rewording: {lab}')
        for lab, x in kc:
            if x: print(f'        (c) GREEN on a content-breaking edit: {lab}')
    print(f'  members passing: {npass} of {len(MEMBERS)};  (b) green {tb}/{tbn};  (c) red {tc}/{tcn}')
    return npass, tb, tbn, tc, tcn


for m in MEMBERS:
    for lab, x in m['keep'] + m['break_']:
        assert x != m['sent'], f"{m['name']}: mutation '{lab}' did not apply"
R0 = run(gate, 'THE REGISTERED FORM: sentence scope, unordered')
R1 = run(gate_clause, 'VARIANT 1, not registered: clause scope, unordered')
R2 = run(gate_ordered, 'VARIANT 2, not registered: sentence scope, ordered')
