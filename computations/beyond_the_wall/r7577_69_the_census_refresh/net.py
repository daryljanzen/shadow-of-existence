#!/usr/bin/env python3
"""r7577 -- THE NET, factored out so the census and the gate extract the SAME candidates.

The papers list, the openness pattern, the body extraction and the marker-sentence rule are
`r7371_cc66_the_coherence_key/key.py`'s verbatim (themselves 69's `extract.py`), moved here so
`check_open_item_coherence` can re-extract the current papers and compare keys instead of trusting a
frozen file.  Nothing in the net is changed: a sentence the net catches is a CANDIDATE, and whether a
candidate states anything open is a reading, recorded in `items_keyed.tsv` beside it.
"""
import os, re

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




def candidates(root):
    """every (paper, marker sentence) the net catches in the current papers, in paper order"""
    out = []
    for num, stem in PAPERS:
        t = body(os.path.join(root, 'corpus', stem + '.tex'))
        for p in re.split(r'\n\s*\n', t):
            flat = re.sub(r'\s+', ' ', p)
            if PAT.findall(flat):
                out.append((num, marker_sentence(flat)))
    return out
