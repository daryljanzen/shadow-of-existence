#!/usr/bin/env python3
"""r7371 ⑥ -- THE KEY, and the re-keying of `69`'s adjudication onto it before the window shuts.

`r7371` ⑥ ②: *"This gate's whole difficulty is … what is the stable identity of an 'open item' such
that a baseline can ratchet on it?  A paragraph hash moves when a paper is reworded … An item title is
prose.  **Name the key you choose and say what moves it and what does not** — that statement is the
deliverable as much as the gate is."*

⛭ THE KEY: **`(paper, normalised marker SENTENCE)`** -- and it is not invented here.  It is
`check_prose_pins`' own rule one level up, quoted from `corpus/prose_pin_baseline.tsv`:

    ** THE KEY IS (receipt, expression) AND NOT A LINE NUMBER, DELIBERATELY. **  A line-keyed
    baseline goes stale … An expression that is reworded is a NEW site and must be read again,
    which is correct.

WHAT DOES NOT MOVE IT: paragraph reflow and rewrapping; whitespace of any kind; paragraphs added or
removed ANYWHERE else in the paper; section renumbering or retitling; other paragraphs reworded; the
paper gaining or losing unrelated content; the file being renamed (the paper's `P*` label is the
first half of the key, not its stem).

WHAT DOES MOVE IT: rewording the sentence that states the openness.  ⛭ *And that is CORRECT rather
than a defect, for the reason the prose-pin rule gives: a statement of openness that has been
rewritten must be read again before it is credited.*

⛔ WHY NOT `69`'s `(paper, paragraph index)`, measured rather than asserted: one paragraph inserted at
the top of `P1` moves **all 257** candidate keys, and the median paper moves **166**.  A key that
`100` per cent of a single edit invalidates cannot carry a ratchet.

⛔ AND WHY THIS RUNS NOW: `69`'s `items.tsv` records its reading against the positional key, and that
key still RESOLVES today -- the extraction reproduces `257` candidates in the same order.  *The moment
any paper moves, `69`'s 257 adjudications become unattachable to the text they were made about.*  ⇒
**This re-keys an existing adjudication; it does not make one.  No class in `items.tsv` is changed,
and `r7371` ⑥ ④ is why: deciding whether an item is open is a reading and it is `69`'s.**

    python3 -I key.py <repo-root> > items_keyed.tsv
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
CENSUS = os.path.join('computations', 'beyond_the_wall', 'r7367_69_the_register_census', 'items.tsv')

# ⌗ PAPERS and PAT are `69`'s extract.py verbatim -- the extraction is not the work and is not changed.
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]
PAT = re.compile(
    r"(remains? open|stays? open|left open|is open\b|are open\b|still open|open (?:question|problem"
    r"|edge|item)s?|not yet|has not been|have not been|is not derived|not derived here|not computed"
    r"|is owed|are owed|\bowed\b|outstanding|unresolved|unanswered|undetermined|undelivered|unbuilt"
    r"|not built|remains to be|remain to be|future work|is not settled|not settled|we do not claim"
    r"|we claim no|not claimed|conjectur|would settle|what would|is not fixed|not fixed by|frontier"
    r"|we have not|does not yet|do not yet|cannot yet|is pending|is missing|are missing)", re.I)

_SENT = re.compile(r'(?<=[.!?])\s+')


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def marker_sentence(flat):
    """the SENTENCE that carries the openness marker -- the claim, not the paragraph around it"""
    m = PAT.search(flat)
    if not m:
        return ''
    for s in _SENT.split(flat):
        if PAT.search(s):
            return ' '.join(s.split())
    return ' '.join(flat.split())


cands = []
for num, stem in PAPERS:
    t = body(os.path.join(ROOT, 'corpus', stem + '.tex'))
    for p in re.split(r'\n\s*\n', t):
        flat = re.sub(r'\s+', ' ', p)
        if PAT.findall(flat):
            cands.append((num, marker_sentence(flat)))

rows = [l.split('\t') for l in open(os.path.join(ROOT, CENSUS), encoding='utf-8').read().split('\n')
        if '\t' in l]
head, data = rows[0], [r for r in rows[1:] if r and r[0].isdigit()]

assert len(cands) == len(data), (
    f'⛔ THE WINDOW HAS SHUT: extraction yields {len(cands)} candidates but 69 adjudicated '
    f'{len(data)}.  The positional key no longer resolves, so this re-keying is NOT safe and must '
    f'not be forced -- 69 has to re-read, which is exactly the cost this key exists to prevent.')
# ⛔ r7371+cc66: JOIN ON THE CAND VALUE, NOT THE ROW POSITION.  `items.tsv`'s rows are NOT in cand
#   order -- 205 of 257 sit at a position that is not their cand number (cand 9 is displaced later).
#   Joining by enumeration order would have attached 69's classifications to the WRONG sentences,
#   silently, for most of the file.  Caught by the assertion below, which is why it is written as a
#   join check and not as a formatting check.
byc = {}
for r in data:
    n = int(r[0])
    assert n not in byc, f'⛔ items.tsv has cand {n} twice'
    byc[n] = r
assert sorted(byc) == list(range(len(cands))), (
    f'⛔ items.tsv cand values are not exactly 0..{len(cands) - 1}; the join is unsafe')
data = [byc[i] for i in range(len(cands))]

# the paper column is the INDEPENDENT check that the join is right: 69 recorded it per candidate,
# and the extraction derives it separately, so agreement on all 257 is not an assumption.
for i, r in enumerate(data):
    assert r[1] == cands[i][0], (
        f'⛔ paper mismatch at cand {i}: items.tsv says {r[1]}, extraction says {cands[i][0]} -- '
        f'the orders have diverged and the join is unsafe')

empty = [i for i, (_, s) in enumerate(cands) if not s]
assert not empty, f'⛔ {len(empty)} candidate(s) yielded no marker sentence: {empty[:5]}'
keys = [(c[0], c[1]) for c in cands]
dup = len(keys) - len(set(keys))

print('# THE OPEN-ITEM KEY -- (paper, normalised marker sentence).  r7371+cc66 ⑥.')
print('# 69\'s reading from r7367_69_the_register_census/items.tsv, RE-KEYED off the paragraph index')
print('# onto a key a ratchet can hold.  No class, topic, register pointer or note is changed here:')
print('# deciding whether an item is open is a reading and it is 69\'s (r7371 ⑥ ④).')
print(f'# {len(keys)} rows, {dup} duplicate key(s).  Regenerate with key.py; never edit by hand.')
print('# paper <TAB> marker sentence <TAB> class <TAB> topic <TAB> register <TAB> note')
for (paper, sent), r in zip(keys, data):
    print('\t'.join([paper, sent] + [(r[i] if i < len(r) else '') for i in (2, 3, 4, 5)]))
