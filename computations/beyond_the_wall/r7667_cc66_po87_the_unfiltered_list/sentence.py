#!/usr/bin/env python3
"""THE SENTENCE TEST, IN ONE PLACE -- `r7671+cc66.4`.

⛔ ** WHY THIS FILE EXISTS. **  Three instruments carried their own copy of "which sentence cites
this receipt": `r7667/census.py`, `r7669/classify.py` and `r7669/sentence_at.py`.  They drifted, and
the drift cost a merged headline: the census said PO-87's list was 48 items on a sentence test that
bounded a span at the nearest `. `, which in LaTeX runs into neighbouring sentences and counts their
figures as the citing sentence's.  The precise test says 30.  `classify.py` still carried the crude
one afterwards, so its own subset counts inherited the same inflation.

⇒ ** One definition, imported by all three. **  A copy that cannot drift is the only fix that holds;
anything else is the same correction waiting to be made a fourth time.
"""
import re

#: ⛭⛭ r7671+cc66.4 -- CUT 6, AND IT MOVES THE SENTENCES WITHOUT MOVING THE LIST.  Cut 5 bounded a
#:   sentence at brace depth ZERO, which is right for body prose and wrong inside a `\caption{...}`:
#:   there every period sits at depth >= 1, so no boundary was ever found and the span ran over the
#:   WHOLE `figure` environment, and the enclosing-group search compounded it by asking for the
#:   wrong depth on the CLOSING brace -- so the three citations inside Fig.~\ref{fig:acoustic-nofit}'s
#:   caption each came back as a "sentence" of ** 80,085 characters, measured. **  And `\emph{A whole sentence.} The next one` was not split either,
#:   because that period is inside the `\emph` group.
#:   ⇒ A boundary is a period, plus any run of closing braces, before whitespace, whose depth AFTER
#:     those braces equals the depth AT THE CITATION -- and the search is confined to the brace
#:     group that directly encloses the citation, so a caption's sentence cannot leak out of it.
#:   ** The figure-printing count is 30 before and after, and no span fails the
#:   contains-its-own-citation test.  So cut 6 is a correction to what 69 READS and not to what the
#:   list SAYS -- which is the convergence Ⓒ④ claims, tested by a change that could have broken it.
_DCACHE = {}
_BND = re.compile(r'\.\}*(?=\s)')


def _depth_map(txt):
    """([depth before each char], [in-math before each char], [(period, after-braces) pairs])"""
    if id(txt) in _DCACHE:
        return _DCACHE[id(txt)]
    d, math, D, M = 0, False, [], []
    for ch in txt:
        D.append(d)
        M.append(math)
        if ch == '{':
            d += 1
        elif ch == '}':
            d -= 1
        elif ch == '$':
            math = not math
    bnd = [(m.start(), m.end()) for m in _BND.finditer(txt)]
    _DCACHE[id(txt)] = (D, M, bnd)
    return D, M, bnd


def _enclosing(txt, D, i):
    """(lo, hi) of the brace group that DIRECTLY contains index i; the whole text at depth 0."""
    d0 = D[i]
    if d0 <= 0:
        return 0, len(txt)
    lo, hi = 0, len(txt)
    for k in range(i, -1, -1):
        if txt[k] == '{' and D[k] == d0 - 1:
            lo = k + 1
            break
    #: ⛔ the CLOSING brace of that group carries depth d0, not d0-1: `D[k]` is the depth BEFORE
    #:   character k, so the `{` that opens a depth-d0 group reads d0-1 and the `}` that closes it
    #:   reads d0.  Asking for d0-1 on both ends found no closing brace at all, and a caption's
    #:   enclosing group ran to the end of the file -- which is how a 341 kB "sentence" was
    #:   produced for the citations inside Fig.~\ref{fig:acoustic-nofit}'s caption.
    for k in range(i, len(txt)):
        if txt[k] == '}' and D[k] == d0:
            hi = k
            break
    return lo, hi


def sentences_citing(txt, base):
    """every sentence of txt carrying \\rcpt{base}, bounded at the CITATION's own brace depth."""
    pat = '\\rcpt{' + base + '}'
    D, M, bnd = _depth_map(txt)
    out = []
    for m in re.finditer(re.escape(pat), txt):
        i = m.start()
        d0 = D[i]
        lo, hi = _enclosing(txt, D, i)
        ok = [(a, b) for a, b in bnd
              if lo <= a and b <= hi and not M[a] and (D[b] if b < len(D) else 0) == d0]
        pre = [b for a, b in ok if b <= i]
        post = [a for a, b in ok if a >= i]
        start = max(pre) if pre else lo
        end = (min(post) + 1) if post else hi
        if pat in txt[start:end]:
            out.append(re.sub(r'\s+', ' ', txt[start:end]).strip())
    return out


#: ⛭⛭ `r7675+cc66` -- THE WHOLE-TEXT SPLIT, ADDED HERE AND NOT IN THE INSTRUMENT THAT NEEDED IT.
#:   `r7675`'s item 3 reads the sites where a figure is printed one sentence away from its
#:   citation, which needs every depth-0 sentence in order rather than only the citing ones.  ⛔ A
#:   second splitter in the reading instrument would be the FOURTH copy of the boundary definition,
#:   which is the drift this file was created to end.  ⇒ It is built on `_depth_map` and `_BND`,
#:   the same boundary `sentences_citing` uses, and the spans are cut the same way: from the end of
#:   the previous boundary's closing-brace run to the period that ends this one.
def depth0_sentences(txt):
    """every sentence of txt bounded at brace depth ZERO, in order, as (line_number, text)."""
    D, M, bnd = _depth_map(txt)
    ok = [(a, b) for a, b in bnd if not M[a] and (D[b] if b < len(D) else 0) == 0]
    out, start = [], 0
    for a, b in ok:
        if a + 1 > start:
            out.append((txt[:start].count('\n') + 1,
                        re.sub(r'\s+', ' ', txt[start:a + 1]).strip()))
        start = b
    return out
