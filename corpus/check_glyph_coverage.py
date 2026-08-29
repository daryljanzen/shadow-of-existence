#!/usr/bin/env python3
"""check_glyph_coverage.py -- A GLYPH IN A REGISTER DOCUMENT WITH NO TRANSLATION IS A BUILD BREAK
WAITING FOR THE ROW THAT CARRIES IT.

** ⛔⛭⛭ WHY.  TWO CORRECT REPAIRS THAT NEVER ASKED THE QUESTION UNDERNEATH. **

  * *`L-262` made `make_receipt_appendix` REFUSE, loudly and by name, on a glyph it cannot render --
    a real repair, and it has fired since.*
  * *`L-267` found that refusal being swallowed by a shell idiom, and built `gate_sweep` so a
    generator failure can no longer print a pass -- also a real repair.*
  ⇒ ** Both treat the failure as an EVENT.  Neither asks how many are already sitting in the tree. **
  ⇒ *** Asked, r3158: EIGHTEEN glyphs, 182 occurrences, across the five register and reach
      documents.  `⌷` alone appears seventy-one times. ***
  ⇒ *** A TRANSLATION TABLE VALIDATED ONLY AGAINST WHAT IT WAS ASKED TO RENDER CARRIES ITS NEXT
      FAILURE ALREADY IN THE TREE. ***  *`★` did not become a problem when it was written; it became
      one when a row happened to reach for it, eighteen occurrences later.*

** ⌗ WHAT THIS CHECKS. **  Every character above ASCII in the surveyed documents is looked up in
`make_receipt_appendix`'s own `_UNI` table -- *the real table, imported, not a copy* -- and any
character with no entry is reported with its codepoint, its count, and a file that carries it.

  ⌷ ** IT IMPORTS THE TABLE IT MEASURES. **  *A gate carrying its own copy of the vocabulary would
    drift from the generator and go green while the generator failed -- which is the whole class
    this gate exists inside.*
  ⚠ ** WHAT IT CANNOT DO. **  *It measures COVERAGE, not correctness: a glyph mapped to the wrong
    LaTeX passes here and comes out wrong in the PDF.  And it surveys the documents named in
    `SURVEYED`, so a glyph in a file outside that list is outside its reach.*
  ⛭ ** AND THE LOUD REFUSAL STAYS. **  *This gate is the early warning; the generator's refusal is
    the backstop.  A wide table that silently dropped an unsurveyed glyph would be worse than a
    build that stops.*

    python3 corpus/check_glyph_coverage.py

Written r3158 (`L-270`).  Stated for reversal.
"""
import collections
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: the documents whose glyphs reach the RECEIPT appendices, or the rows that feed them
SURVEYED = [
    'THE_LIVE_ARC.md',
    'receipts/INDEX.md',
    'THE_MATHEMATICS_REACH.md',
    'THE_PHYSICS_REACH.md',
    'OWED.md',
]
#: ⛔⛭⛭ ** AND THERE ARE TWO RAILS, AND THIS GATE COULD SEE ONE OF THEM -- found r3584. **
#:   *The header above says the gate imports the table it measures, because a copy would drift
#:   from the generator and go green while the generator failed.* ⇒ *** It imported ONE of two
#:   generators.  `\ldg` shipped at r3523, three hundred and sixty revisions after this gate was
#:   written, with its OWN `tex_escape` and its OWN twelve-entry table -- and nothing surveyed it,
#:   so the whole class this gate exists inside had reopened on a rail it could not see. ***
#:   ⌗ **What that cost, measured before it was fixed:** *four ledgers' frontmatter carried `⟺`
#:   twice, `ω` and `Ⓒ` -- every one already translated on the OTHER rail -- and the registry
#:   copies its descriptions from that frontmatter.*  ** So the `\ldg` rail was one copy-paste
#:   from `sys.exit(2)`, and the survey that would have said so did not reach it. **
#:   ⚠ *A rail is a GENERATOR plus the documents that feed IT.  Adding the ledger files to
#:   `SURVEYED` would have measured them with the wrong escape and reported the wrong answer --
#:   which is the restatement failure this gate threw away its threshold to avoid.*
#: ⛔⛭ ** THE FIRST FORM OF THIS GATE SET ITS OWN THRESHOLD, AND MEASURED A DIFFERENT THING. **
#:   *It flagged every character above `U+00A0` with no `_UNI` entry and reported TEN, of which SIX
#:   were the accented letters in author names -- `ö é î ü`, `¶`, `÷` -- which the generator passes
#:   through happily, because `pdflatex` handles Latin-1 and its refusal fires only above `U+00FF`.*
#:   ⇒ *** A GATE THAT RESTATES THE RULE IT GUARDS INSTEAD OF RUNNING IT MEASURES ITS OWN RESTATEMENT
#:       -- and it fails in whichever direction the copy drifted, here toward false alarm and next
#:       time toward silence. ***
#:   ⌷ ** So the gate no longer has a threshold. **  *It calls the generator's own `tex_escape` on
#:     each distinct character and records which ones that function refuses.  There is nothing left
#:     to keep in step, because the measurement IS the thing enforced.*
def uni_table(script='make_receipt_appendix.py', argv=('-', '-')):
    """the GENERATOR'S OWN table, imported -- a copy here would drift and go green while it failed"""
    path = os.path.join(ROOT, 'corpus', script)
    spec = importlib.util.spec_from_file_location('_gen_for_coverage_' + script, path)
    mod = importlib.util.module_from_spec(spec)
    saved_argv, saved_path = sys.argv, list(sys.path)
    sys.argv = [script] + list(argv)                   # it reads argv at module scope
    # ** the generator imports its siblings by bare name, so its own directory must be on the path
    #   -- as it is when the generator is run directly, and as it is NOT when it is imported. **
    sys.path.insert(0, os.path.dirname(path))
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass                                            # its own family guards, or its arg parse
    except Exception as exc:                            # a generator that will not import at all
        print(f'    \u26d4 [FAIL] the generator did not import: {type(exc).__name__}: {exc}')
        return None
    finally:
        sys.argv, sys.path = saved_argv, saved_path
    return mod


def refused(mod, ch):
    """does the GENERATOR'S OWN escape refuse this character?  no threshold is restated here

    *A generator that refuses may also EXPLAIN itself on stderr -- the ledger rail does -- and this
    is called once per distinct glyph, including on the control.  The explanation is that
    generator talking to whoever ran IT; here it would be a wall of text under a gate that is
    about to print the same finding properly.  Swallowed, never the return value.*
    """
    err = sys.stderr
    try:
        sys.stderr = io.StringIO()
        try:
            mod.tex_escape(ch)
        except BaseException:
            return True
        return False
    finally:
        sys.stderr = err


def ledger_feeders():
    """** the LEDGER rail's feeders, taken from the generator rather than restated. **

    *The generator escapes the cells `parse_index` returns; the registry copies those cells from
    each ledger's own frontmatter.  So the feeders are the ROWS (not the whole registry, whose
    header prose carries glyphs no row ever sees) and the FRONTMATTER BLOCK of each ledger the
    rows name (not the bodies, which are prose the generator never reads).*
      ⌷ *Returned as (label, text) so the report can name a file a reader can open.*
    """
    mod = uni_table('make_ledger_appendix.py', ('P3', '-'))
    if mod is None or not hasattr(mod, 'parse_index'):
        return None, []
    reg = os.path.join(ROOT, 'corpus', 'ledgers_registry.md')
    if not os.path.exists(reg):
        return mod, []
    try:
        rows = mod.parse_index(reg)
    except BaseException:
        return mod, []
    out = []
    for r in rows:
        cells = ' '.join(str(r.get(k, '')) for k in ('key', 'file', 'kind', 'what'))
        out.append((f"corpus/ledgers_registry.md ({r.get('key', '?')})", cells))
    for r in rows:
        f = os.path.join(ROOT, str(r.get('file', '')))
        if not os.path.exists(f):
            continue
        text = open(f, encoding='utf-8', errors='replace').read()
        m = re.match(r'---\n(.*?)\n---\n', text, re.S)
        if m:
            out.append((f"{r.get('file')} (frontmatter)", m.group(1)))
    return mod, out


def receipt_feeders():
    """the register documents, whole: any glyph in one of them may end up in a row"""
    mod = uni_table()
    out = []
    for fn in SURVEYED:
        p = os.path.join(ROOT, fn)
        if os.path.exists(p):
            out.append((fn, open(p, encoding='utf-8', errors='replace').read()))
    return mod, out


#: ⌷ ** A RAIL IS A GENERATOR PLUS THE DOCUMENTS THAT FEED IT, and each is measured with ITS OWN
#:   escape. **  *`known` is a glyph that rail must ACCEPT -- without it a broken import reports an
#:   empty set of failures and calls the rail clean.*
RAILS = [
    {'name': 'receipts (\\rcpt)', 'feeders': receipt_feeders, 'known': '\u2317',
     'fix': 'Add the glyph to `_MARKERS` in `corpus/make_receipt_appendix.py`'},
    {'name': 'ledgers  (\\ldg)', 'feeders': ledger_feeders, 'known': '\u2014',
     'fix': 'Add the glyph to `UNI` in `corpus/make_ledger_appendix.py`.\n'
            'And if the OTHER rail already translates it, carry THAT entry across rather than\n'
            'spelling the same glyph a second way -- two rails disagreeing is the defect that\n'
            'put this rail one copy-paste from a build stop.'},
]


def survey(rail):
    """returns (ok, missing, first_seen, n_feeders, note) -- ok False means the rail is NOT measured"""
    mod, feeders = rail['feeders']()
    uni = getattr(mod, '_UNI', None) or getattr(mod, 'UNI', None) if mod else None
    if not mod or not uni or not hasattr(mod, 'tex_escape'):
        return False, None, None, 0, 'could not import the generator\'s escape'
    # ** THE CONTROL, PER RAIL. **  *a glyph the generator does not know must be REFUSED, and one
    #   it does know must pass -- otherwise this rail reports an empty set and calls it clean.*
    if not (refused(mod, chr(0x1F600)) and not refused(mod, rail['known'])):
        return False, None, None, 0, ('the CONTROL did not fire: the imported escape neither '
                                      'refuses an unknown glyph nor accepts a known one')
    # ** a survey that read nothing must FAIL: an empty scan is green forever **
    if not feeders:
        return False, None, None, 0, 'no feeding document was found.  An empty survey is green forever'
    missing, first, verdict = collections.Counter(), {}, {}
    for label, text in feeders:
        for ch in text:
            if ord(ch) < 0x80:
                continue
            if ch not in verdict:
                verdict[ch] = refused(mod, ch)
            if verdict[ch]:
                missing[ch] += 1
                first.setdefault(ch, label)
    return True, missing, first, len(feeders), f'{len(uni)} entries'


def main():
    print()
    print('  check_glyph_coverage -- is a glyph sitting in a register document with no translation?')
    print()
    rc, reports = 0, []
    for rail in RAILS:
        ok, missing, first, n, note = survey(rail)
        if not ok:
            print(f"    \u26d4 [FAIL] {rail['name']}: {note}.  The gate is not measuring this rail.")
            rc = 1
            continue
        print(f"    {rail['name']:<20} escape imported ({note}); {n:>3} feeding document(s); "
              f"{len(missing)} glyph(s) with no translation")
        if missing:
            reports.append((rail, missing, first))
            rc = 1
    print()
    if not reports and rc == 0:
        print('    every glyph on both rails has a translation in the table that rail uses.')
        print()
        return 0
    for rail, missing, first in reports:
        print(f"    \u26d4 {rail['name']}: {len(missing)} glyph(s), "
              f"{sum(missing.values())} occurrence(s):")
        for ch, n in missing.most_common():
            print(f'      U+{ord(ch):04X}  {ch!r:>8}  \u00d7{n:<5d} first seen in {first[ch]}')
        for i, line in enumerate(rail['fix'].split('\n')):
            print(('    \u2337 ' if i == 0 else '      ') + line.strip())
        print('      Give it a STATED translation -- nothing for a structural bullet, the LaTeX')
        print('      for real mathematics.')
        print()
    print('    \u26ed ** A translation table validated only against what it was asked to render carries')
    print('       its next failure already in the tree. **  *Each of these is a build break waiting')
    print('       for the row that happens to reach for it.*')
    print('    \u26a0 ** And a rail this gate cannot SEE is the same failure with nothing to report it:')
    print('       the \\ldg rail ran for sixty revisions unsurveyed because it arrived after the')
    print('       survey and nobody widened the survey to meet it. **')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
