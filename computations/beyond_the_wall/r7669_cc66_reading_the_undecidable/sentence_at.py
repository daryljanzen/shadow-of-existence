#!/usr/bin/env python3
"""`r7669` (cc66) -- print the sentence(s) of `corpus/CR_cosmology.tex` that cite a receipt.

A reading aid for the RE-GROUND wordings, used to quote a sentence rather than to count one.

⛔ ** r7671+cc66.4: THIS FILE USED TO CARRY ITS OWN COPY OF THE SENTENCE TEST, and it was the THIRD
copy. **  The three copies -- `r7667/census.py`, `r7669/classify.py` and this one -- drifted, and the
drift cost a merged headline: PO-87's list was reported at 48 items on a span bounded by the nearest
`. `, which in LaTeX runs into neighbouring sentences.  It is 30.
⇒ ** One definition, imported: ** `r7667/sentence.py`, cut 6, which bounds a sentence at the depth of
its own citation inside the brace group that encloses it.  *A copy that cannot drift is the only fix
that holds.*
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7667_cc66_po87_the_unfiltered_list'))
from sentence import sentences_citing            # noqa: E402

TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()
base = sys.argv[1]
pat = '\\rcpt{' + base + '}'
lines = [TEX[:m.start()].count('\n') + 1 for m in re.finditer(re.escape(pat), TEX)]
sents = sentences_citing(TEX, base)
print(f'  {base}')
print(f'  cited at line(s): {lines};  sentences recovered: {len(sents)}')
for ln, s in zip(lines, sents):
    #: the span must CONTAIN its own citation -- the property the crude test did not guarantee
    print(f'\n  line {ln}  contains-its-own-citation={pat in s}  chars={len(s)}')
    print('   ' + s)
