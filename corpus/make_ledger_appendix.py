#!/usr/bin/env python3
"""make_ledger_appendix.py -- generate 'Appendix L -- The Knowledge Ledgers' from corpus/ledgers_registry.md.

Single source of truth: a paper's Appendix L can never drift from the index, because it is
regenerated.  This is the make_receipt_appendix.py rail for a different artefact, and it is built
with that generator's three scars already closed rather than waiting to acquire them:

  1. NO PREFIX ROW-FILTER.  make_receipt_appendix lost rows to `ln.startswith('| P')` three separate
     times -- the backtick format at c54.36, lowercase `p0` at c54.203, an em-dash paper cell at
     c54.222 -- each time silently, each time dropping receipts that were registered and on disk.
     Rows here are every pipe-row of the table after the separator, with no predicate on their
     content.
  2. REFUSE UNRESOLVABLE ROWS.  That generator emitted a row's status cell as a verdict without
     looking for the file, and printed `[OK]` beside computations that had never existed.  A
     generated appendix inherits the index's errors and dresses them as verification.  A row whose
     ledger is not on disk is refused, loudly, and the run fails.
  3. FAIL ON DUPLICATE KEYS.  A dict keyed by stem silently overwrote, and eighteen receipt rows
     collapsed to whichever appeared later, with file order deciding which.  A repeated key here is
     an error, not a last-write-wins.

Usage:  python3 make_ledger_appendix.py <PAPER|corpus> <out.tex>
  <PAPER>  e.g. P17 -> only the ledgers that paper's .tex actually cites with \\ldg{}
  corpus   -> every row in the index (the book appendix)
Each row -> a labelled \\item[...]{ldg:<key>} so \\ldg{<key>} in the body links to it.
"""
import sys, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INDEX = os.path.join(HERE, 'ledgers_registry.md')

PAPER_FILES = {
    'P1': 'BH_causality_v2.tex', 'P2': 'janzen_circle_v3.tex',
    'P3': 'SdS-slicing-curve_v2.tex', 'P4': 'modern_parallax.tex',
    'P5': 'groupoid_paper.tex', 'P6': 'shadow_of_existence.tex',
    'P7': 'CR_framework.tex', 'P8': 'slicing_operator.tex',
    'P9': 'range_paper.tex', 'P10': 'canonical_time.tex',
    'P11': 'dynamics_paper.tex', 'P12': 'algebroid_paper.tex',
    'P13': 'boundary_paper.tex', 'P14': 'matter_sector_paper.tex',
    'P15': 'CR_cosmology.tex', 'P16': 'cosmogenesis_paper.tex',
    'P17': 'geometric_core_paper.tex', 'p0': 'geometric_core_paper.tex',
}

LDG = re.compile(r'\\ldg\{([^}]*)\}')

# an internal revision reference: r1234, optionally suffixed (r3560b), or the fork's c54.N
REVREF = re.compile(r'\b(?:r\d{3,4}[a-z]?|c54\.\d+)\b')


UNI = {'\u2014': '---', '\u2013': '--', '\u00d7': r'$\times$', '\u2018': '`',
       '\u2019': "'", '\u201c': '``', '\u201d': "''", '\u00f6': r'\"o',
       '\u00e9': r"\'e", '\u2192': r'$\to$', '\u2317': '', '\u2026': r'\dots{}'}


def tex_escape(s):
    for a, b in (('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'), ('$', r'\$'),
                 ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}'),
                 ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')):
        s = s.replace(a, b)
    for a, b in UNI.items():
        s = s.replace(a, b)
    # The ledgers' frontmatter is prose written for humans, not for TeX.  Anything still
    # non-ASCII would compile to a silent wrong glyph or break the build, so it is caught
    # here rather than discovered in a PDF.
    left = sorted({c for c in s if ord(c) > 127})
    if left:
        sys.stderr.write('\n  UNMAPPED NON-ASCII in an index row: %s (%s)\n'
                         % (''.join(left), ', '.join(hex(ord(c)) for c in left)))
        sys.stderr.write('     Add it to UNI in this file.  A generator that emits a byte the\n'
                         '     build cannot set produces a wrong glyph without saying so.\n\n')
        sys.exit(2)
    return s


def parse_index(path):
    """Every pipe-row after the header separator.  No predicate on the row's content -- that is
    exactly the filter that cost the receipt generator three separate silent losses."""
    rows, seen, started = [], {}, False
    for lineno, ln in enumerate(open(path, encoding='utf-8'), 1):
        s = ln.strip()
        if not s.startswith('|'):
            continue
        if set(s) <= set('|-: '):
            started = True
            continue
        if not started:
            continue                                  # the header row itself
        cells = [c.strip() for c in s.strip('|').split('|')]
        if len(cells) < 4:
            continue
        key = cells[0].strip('`')
        if key in seen:
            sys.stderr.write(
                '\n  DUPLICATE KEY %r at corpus/ledgers_registry.md line %d (first seen line %d).\n'
                '  A dict keyed by slug would silently keep the later row and the earlier\n'
                '  ledger would vanish from every appendix, with file order deciding which.\n'
                % (key, lineno, seen[key]))
            sys.exit(2)
        seen[key] = lineno
        rows.append({'key': key, 'file': cells[1].strip('`'),
                     'kind': cells[2], 'what': cells[3], 'line': lineno})
    return rows


def resolve(rows):
    missing = [r for r in rows if not os.path.exists(os.path.join(ROOT, r['file']))]
    if missing:
        sys.stderr.write('\n  REFUSING TO EMIT %d ROW(S) WHOSE LEDGER IS NOT ON DISK:\n' % len(missing))
        for r in missing:
            sys.stderr.write('     corpus/ledgers_registry.md line %d: %s\n' % (r['line'], r['file']))
        sys.stderr.write('     An appendix that points a reader at a file nobody has is not a\n'
                         '     reference; it is a claim of provenance the corpus cannot honour.\n\n')
        sys.exit(2)

    # ⛔⛭⛭ SCAR FOUR, ADDED r3564 (node 60), AND IT ARRIVED WITHIN A DAY OF THE RAIL SHIPPING.
    #   This module opens by naming the receipt generator's three scars and closing them "rather
    #   than waiting to acquire them".  It then acquired a fourth of its own, from a direction
    #   neither generator had met: ** the descriptions are copied from each ledger's frontmatter,
    #   and a ledger's frontmatter is written for an INTERNAL reader. **  Two of them say "thrown
    #   r3437", "the r3453 measure", "verified at r3438" -- and the generator wrote those straight
    #   into EIGHT published paper appendices, where check_revleak found them.
    #     ⇒ *** A generator that spans two audiences IS a boundary, and an internal revision number
    #         is exactly what does not survive one.  The registry's own header promises the
    #         description "cannot drift from the file" -- which is true, and is why the leak
    #         PROPAGATES rather than staying put. ***
    #   ⌗ REFUSED rather than STRIPPED, deliberately and in this module's own idiom: silently
    #     rewriting a description would make the appendix disagree with the registry it claims to
    #     be generated from, which is scar (2) wearing different clothes.  The author rewords it.
    leaky = [(r, sorted(set(REVREF.findall(r.get('what', '')))))
             for r in rows if REVREF.search(r.get('what', ''))]
    if leaky:
        sys.stderr.write('\n  REFUSING TO EMIT %d ROW(S) WHOSE DESCRIPTION CARRIES AN INTERNAL\n'
                         '  REVISION REFERENCE:\n' % len(leaky))
        for r, refs in leaky:
            sys.stderr.write('     corpus/ledgers_registry.md line %d: %s  -> %s\n'
                             % (r['line'], r['key'], ', '.join(refs)))
        sys.stderr.write('     These become published paper prose.  A revision number is this\n'
                         '     corpus talking to itself, and check_revleak fails on it in any\n'
                         '     paper body.  Reword the ledger frontmatter the registry copies --\n'
                         '     the fact usually survives without the number ("thrown after the\n'
                         '     Phase 4 survey").\n\n')
        sys.exit(3)
    return rows


def cited_by(paper):
    fn = PAPER_FILES.get(paper)
    if not fn:
        return None
    body = open(os.path.join(HERE, fn), encoding='utf-8', errors='replace').read()
    body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith('%'))
    return set(LDG.findall(body))


def emit(rows, scope, out):
    L = [r'\clearpage',
         r'\section*{Appendix L\quad The Knowledge Ledgers}\label{app:ledgers}',
         r'\addcontentsline{toc}{section}{Appendix L: The Knowledge Ledgers}',
         r'\small\noindent Each claim marked \ldgmarker\ in the text rests on a field bake or the '
         r'figure--theorem bake recorded in the named ledger, which ships with this work and carries '
         r'the probes, the receipts, and the three registers kept apart --- what bit, what bounced, '
         r'and where the boundary is. A ledger is working apparatus, not a publication, and is cited '
         r'here rather than in the bibliography. This appendix is generated from the ledger index, '
         r'not maintained by hand.\par\medskip',
         r'\begingroup\renewcommand{\arraystretch}{1.25}',
         r'\begin{description}']
    for r in rows:
        L.append(r'\item[\label{ldg:%s}\texttt{%s}]\hfill\textsf{[%s]}\\'
                 % (r['key'], tex_escape(r['file']), tex_escape(r['kind'])))
        L.append(r'%s' % tex_escape(r['what']))
    L += [r'\end{description}', r'\endgroup']
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('  Appendix L: %d ledger(s) emitted for %s -> %s' % (len(rows), scope, out))


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    scope, out = sys.argv[1], sys.argv[2]
    rows = resolve(parse_index(INDEX))
    if scope != 'corpus':
        keys = cited_by(scope)
        if keys is None:
            sys.stderr.write('  unknown paper %r\n' % scope)
            return 1
        unknown = keys - {r['key'] for r in rows}
        if unknown:
            sys.stderr.write('\n  %s cites %d ledger key(s) not in the index: %s\n'
                             % (scope, len(unknown), ', '.join(sorted(unknown))))
            sys.stderr.write('     A marker that resolves to nothing is a dangling link in the\n'
                             '     built PDF and is silent in the source.\n\n')
            return 2
        rows = [r for r in rows if r['key'] in keys]
    emit(rows, scope, out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
