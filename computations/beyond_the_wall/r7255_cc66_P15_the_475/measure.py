#!/usr/bin/env python3
"""r7255 order ②: MEASURE the 475 unverdicted quote-pin keys of receipts/P15_CR_cosmology
before adjudicating one of them.

Everything in MEASURED.tsv is a count or a boolean taken from the files, not a judgement.
The judgement columns are added by the adjudication pass and live in a separate file, so that
what was measured and what was decided never share a column.

Per key:
  occ_paper        occurrences in the corpus papers, GENERATED APPENDICES EXCLUDED
  occ_paper_flat   the same under the receipts' own whitespace normaliser
  occ_instr        occurrences in computations/beyond_the_wall/*.py, flattened
  occ_recpt        occurrences in receipts/**/*.py
  real_target      PAPER / SOURCE / ABSENT -- measured, not the ledger's target column, because
                   r7253+cc66.171 showed that column mislabels a SOURCE pin as PAPER whenever the
                   container trace names a .tex elsewhere in the same receipt
  tokenish         the literal is an IDENTITY BY SHAPE: an identifier, a LaTeX macro or label, a
                   number, a key=value, a dotted attribute
  shorter_uniq     ** the grain clause's limb two, made operational. ** TRUE iff some strictly
                   shorter CONTIGUOUS WORD-ALIGNED span of the literal occurs in the container at
                   MOST as often as the literal itself.  r7255+cc66.172 ① found limb two defeated
                   on the clause's own exemplar by a shorter span that occurred TWICE, so a
                   shortening that multiplies the sites turns a claim pin into a file pin.
  shorter_span     the longest such span, or '-'
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
PREFIX = 'receipts/P15_CR_cosmology'

SITE = re.compile(r'^\s*\[QUOTE-PIN\]\[(\w+)\]\[(\w+)\]\[([^\]]*)\]\s+(\S+):(\d+):(\d+)\s+(.*)$')
TOKENISH = re.compile(r'^(?:[A-Za-z_][\w.]*(?:=[-\w.]+)?|\\[A-Za-z@]+\{?[\w:.-]*\}?|[\w:.-]+:[\w:.-]+'
                      r'|\$?-?[\d.,]+\\?%?\$?|[A-Za-z_]\w*\(\)|\w+_\{?\w*\}?)$')


def flat(t):
    """the normaliser the P15 receipts use: one line, leading comment markers stripped."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def ledger():
    rows = [l.rstrip('\n').split('\t') for l in
            open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8')
            if l.strip() and not l.startswith('#')]
    return [r for r in rows if len(r) >= 7]


def word_spans(s):
    """every strictly shorter CONTIGUOUS WORD-ALIGNED span, longest first.

    Word-aligned per 60's r7253 limit: a span may start and end only at a word boundary of the
    literal.  Contiguous per this seat's own limit: a pin is a substring, so a mid-span excision
    is unreachable.  Together those leave exactly the spans you get by dropping whole words off
    one end or the other.
    """
    w = s.split(' ')
    out = []
    for i in range(len(w)):
        for j in range(len(w), i, -1):
            if i == 0 and j == len(w):
                continue
            out.append(' '.join(w[i:j]))
    return sorted(set(out), key=len, reverse=True)


def main():
    enum = sys.argv[1]
    led = ledger()
    want = {(r[0], r[1]): r for r in led
            if PREFIX in r[0] and r[5].startswith('UNADJUDICATED')}

    sites = {}
    for ln in open(enum, encoding='utf-8'):
        m = SITE.match(ln)
        if not m:
            continue
        tgt, tier, flags, path, line, col, lit = m.groups()
        sites[(path, lit.strip())] = (tgt, tier, flags, int(line), int(col))

    papers = [q for q in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
              if not os.path.basename(q).startswith('appendix_receipts')]
    TEX = ''.join(open(q, encoding='utf-8').read() for q in papers)
    TEXF = flat(TEX)
    INSTR = flat(''.join(open(q, encoding='utf-8').read()
                         for q in sorted(glob.glob(os.path.join(ROOT, 'computations', 'beyond_the_wall', '*.py')))))
    RECPT = ''.join(open(q, encoding='utf-8').read()
                    for q in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
                    if '__pycache__' not in q)

    out = []
    for (stem, lit), row in sorted(want.items()):
        tgt, tier, flags, line, col = sites[(stem, lit)]
        try:
            raw = json.loads(lit)
        except Exception:
            raw = lit.strip('"')
        op = TEX.count(raw)
        opf = TEXF.count(flat(raw))
        oi = INSTR.count(flat(raw))
        orc = RECPT.count(raw)
        real = 'PAPER' if (op or opf) else ('SOURCE' if (oi or orc) else 'ABSENT')
        container = TEX if real == 'PAPER' else (INSTR if oi else RECPT)
        base = max(op, opf) if real == 'PAPER' else max(oi, orc)
        span, uniq = '-', '0'
        if tier == 'SENTENCE' and ' ' in raw and base:
            probe = flat(raw) if (real == 'PAPER' and opf and not op) else raw
            cont = flat(container) if probe != raw else container
            for cand in word_spans(probe):
                if cand and cont.count(cand) and cont.count(cand) <= base:
                    span, uniq = cand, '1'
                    break
        out.append([stem, tgt, tier, flags, str(line), lit, real, str(op), str(opf), str(oi),
                    str(orc), uniq, json.dumps(span)])

    dest = os.path.join(HERE, 'MEASURED.tsv')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('# r7255 order ② -- the 475 unverdicted keys of receipts/P15_CR_cosmology, MEASURED.\n')
        fh.write('# counts and booleans only; no judgement in any column.\n')
        fh.write('# stem\tledger_target\ttier\tflags\tline\tliteral\treal_target\t'
                 'occ_paper\tocc_paper_flat\tocc_instr\tocc_recpt\tshorter_uniq\tshorter_span\n')
        for r in out:
            fh.write('\t'.join(r) + '\n')
    print(f'{len(out)} rows -> {dest}')


if __name__ == '__main__':
    main()
