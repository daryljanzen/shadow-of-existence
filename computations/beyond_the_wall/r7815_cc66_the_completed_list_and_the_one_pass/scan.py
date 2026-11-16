#!/usr/bin/env python3
"""r7815 (cc66) item ②: the COMPLETED list of printed figures that rest on the
LambdaCDM control at its un-refitted point.

r7812's sentence_list.py read SWAP LOGS -- the five receipts whose banks the
re-pointing harness could swap.  69's r7815 ruling: that is correct for what it
reads and incomplete for the pass, because some control figures were measured by
other means and never passed through a swappable bank.  So this scan reads the
DOCUMENTS instead: every sentence in P15, P7, P18 and EXPLAINER.md that names
the control or presents a standard-model figure.

It is a CANDIDATE GENERATOR, not an adjudicator.  Every candidate is verdicted by
hand in LIST.md; the script's job is to make the hand-read exhaustive rather than
recalled.  A candidate it drops is a site that cannot be read, so the two filters
are deliberately wide and are printed with their counts.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
DOCS = [('P15', 'corpus/CR_cosmology.tex'),
        ('P7',  'corpus/CR_framework.tex'),
        ('P18', 'corpus/CR_synthesis.tex'),
        ('EXPLAINER', 'EXPLAINER.md')]

# filter A -- the sentence names the control, in any of the corpus's spellings
NAMES = re.compile(r'\b(control|controls)\b'
                   r'|\\Lambda(?:\{\})?\s*(?:\\mathrm\{)?CDM'
                   r'|\bLCDM\b|\bLambdaCDM\b'
                   r'|standard model|standard code|standard cosmolog'
                   r'|\bCAMB\b|\bCLASS\b|concordance', re.I)

# filter B -- the figures 69 named at r7815, and the ones r7809/r7813 pinned,
# caught WHEREVER printed even if the sentence does not name the control.
FIGURES = [r'0\.918', r'0\.957', r'0\.964', r'1\.18\b', r'2\.200\b', r'2\.195\b',
           r'2\.203\b', r'2\.2026', r'2\.212', r'0\.23\s*(?:\\?%|per cent)',
           r'1\.80\s*\\?sigma', r'1\.80\b', r'301\.375', r'301\.6', r'0\.79\b',
           r'1\.13\b', r'0\.76\b', r'12\.6\b', r'13864', r'144\.52', r'13894']
FIG = re.compile('|'.join(FIGURES))

NUM = re.compile(r'(?<![\w.])(\d+\.\d+|\d{2,})(?![\w.])')

# a sentence must carry a FIGURE to be a landing site: prose that names the
# control without printing a number has nothing to re-point.
def sentences(text, md):
    """Split into sentences, each tagged with the source line it STARTS on and
    the nearest \\label{} at or before it.

    LaTeX comments are dropped (they are not printed) but \\rcpt{} and inline
    math are kept, because a figure can sit inside either.  The line number and
    the label are carried forward as the lines are walked, rather than recovered
    afterwards by searching the joined text -- a joined sentence that spans
    source lines cannot be found in the file it came from.
    """
    out, buf, start, label = [], [], 1, '-'
    for i, raw in enumerate(text.splitlines(), 1):
        if not md and raw.lstrip().startswith('%'):
            continue
        body = raw if md else re.sub(r'(?<!\\)%.*$', '', raw)
        for m in re.finditer(r'\\label\{([^}]+)\}', body):
            label = m.group(1)
        if not buf:
            start = i
        buf.append((body, label))
        joined = ' '.join(b for b, _ in buf)
        pieces = re.split(r'(?<=[.!?])\s+(?=[A-Z\\$])', joined)
        if len(pieces) > 1 or not body.strip():
            lab0 = buf[0][1]
            for p in pieces[:-1]:
                if p.strip():
                    out.append((start, lab0, p.strip()))
            tail = pieces[-1].strip()
            buf = [(tail, label)] if tail else []
            start = i                      # the tail begins on THIS line
    if buf and ' '.join(b for b, _ in buf).strip():
        out.append((start, buf[0][1], ' '.join(b for b, _ in buf).strip()))
    return out


def main():
    total = 0
    for paper, rel in DOCS:
        path = os.path.join(ROOT, rel)
        text = open(path, encoding='utf-8').read()
        md = rel.endswith('.md')
        hits = []
        for ln, lab, s in sentences(text, md):
            named = bool(NAMES.search(s))
            figure = bool(FIG.search(s))
            if not (named or figure):
                continue
            nums = NUM.findall(s)
            if not nums and not figure:
                continue          # names the control, prints nothing
            why = ('names+figure' if named and figure else
                   'names' if named else 'figure')
            hits.append((ln, why, lab, s))
        print(f'=== {paper}  {rel}  --  {len(hits)} candidate sentence(s)')
        for ln, why, lab, s in hits:
            flat = re.sub(r'\s+', ' ', s)
            print(f'  [{paper} l.{ln}] ({why}) <{lab}>')
            print(f'      {flat[:400]}')
        print()
        total += len(hits)
    print(f'TOTAL {total} candidate sentence(s) across {len(DOCS)} documents')

if __name__ == '__main__':
    sys.exit(main())
