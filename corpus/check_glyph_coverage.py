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
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: the documents whose glyphs reach the generated appendices, or the rows that feed them
SURVEYED = [
    'THE_LIVE_ARC.md',
    'receipts/INDEX.md',
    'THE_MATHEMATICS_REACH.md',
    'THE_PHYSICS_REACH.md',
    'OWED.md',
]
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
def uni_table():
    """the GENERATOR'S OWN table, imported -- a copy here would drift and go green while it failed"""
    path = os.path.join(ROOT, 'corpus', 'make_receipt_appendix.py')
    spec = importlib.util.spec_from_file_location('_mra_for_coverage', path)
    mod = importlib.util.module_from_spec(spec)
    saved_argv, saved_path = sys.argv, list(sys.path)
    sys.argv = ['make_receipt_appendix.py', '-', '-']   # it reads argv at module scope
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
    """does the GENERATOR'S OWN escape refuse this character?  no threshold is restated here"""
    try:
        mod.tex_escape(ch)
    except SystemExit:
        return True
    except Exception:
        return True
    return False


def main():
    print()
    print('  check_glyph_coverage -- is a glyph sitting in a register document with no translation?')
    print()
    mod = uni_table()
    uni = getattr(mod, '_UNI', None) if mod else None
    if not uni or not hasattr(mod, 'tex_escape'):
        print('    ⛔ [FAIL] could not import the generator\'s escape.  The gate is not measuring.')
        print()
        return 1
    print(f'    generator escape imported: _UNI carries {len(uni)} entries')
    # ** THE CONTROL. **  *a glyph the generator does not know must be REFUSED, and one it does know
    #   must pass -- otherwise this gate reports an empty set and calls it clean.*
    if not (refused(mod, chr(0x1F600)) and not refused(mod, chr(0x2317))):
        print('    ⛔ [FAIL] the CONTROL did not fire: the imported escape neither refuses an')
        print('       unknown glyph nor accepts a known one.  The gate is not measuring.')
        print()
        return 1
    print('    control: an unknown glyph is refused, a known one accepted — fires.')

    missing, files, scanned = collections.Counter(), {}, 0
    for fn in SURVEYED:
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        text = open(p, encoding='utf-8', errors='replace').read()
        scanned += 1
        verdict = {}
        for ch in text:
            if ord(ch) < 0x80:
                continue
            if ch not in verdict:
                verdict[ch] = refused(mod, ch)
            if verdict[ch]:
                missing[ch] += 1
                files.setdefault(ch, fn)
    print(f'    documents surveyed       : {scanned} of {len(SURVEYED)}')
    print()
    # ** a survey that read nothing must FAIL: an empty scan is green forever **
    if scanned == 0:
        print('    ⛔ [FAIL] no surveyed document was found.  An empty survey is green forever.')
        print()
        return 1
    if not missing:
        print('    every glyph in the surveyed documents has a translation.')
        print()
        return 0
    print(f'    ⛔ {len(missing)} glyph(s) with no translation, '
          f'{sum(missing.values())} occurrence(s):')
    for ch, n in missing.most_common():
        print(f'      U+{ord(ch):04X}  {ch!r:>8}  ×{n:<5d} first seen in {files[ch]}')
    print()
    print('    ⛭ ** A translation table validated only against what it was asked to render carries')
    print('       its next failure already in the tree. **  *Each of these is a build break waiting')
    print('       for the row that happens to reach for it.*')
    print('    ⌷ Add the glyph to `_MARKERS` in `corpus/make_receipt_appendix.py` with a stated')
    print('      translation -- nothing for a structural bullet, the LaTeX for real mathematics.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
