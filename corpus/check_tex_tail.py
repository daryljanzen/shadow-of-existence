#!/usr/bin/env python3
r"""check_tex_tail.py -- no paper carries prose AFTER its own `\end{document}`.

** THIS EXISTS BECAUSE IT HAD ALREADY HAPPENED, AND THE LINE THAT DID IT FOUND IT
   TWENTY-SEVEN REVISIONS LATER WHILE LOOKING FOR SOMETHING ELSE. **  At `r4549` this
line appended three paragraphs to `CR_cosmology.tex` -- the `PO-13` result that the peak-to-scale
ratio is a source-frame quantity, that the two arms' difference is a convention rather than a rate,
and that one asymmetry survives and is not yet a physical number.  ** The append landed at the end
of the FILE, which is eight lines past the end of the DOCUMENT. **  LaTeX reads to `\end{document}`
and stops, so the three paragraphs have never once appeared in the paper, in any build, since.

  ⇒ *** AND THE REVISION THAT WROTE THEM REPORTED "P15 compiles at 94 pages, zero errors and zero
      undefined references". ***  ** It did.  A paper compiles perfectly with text stranded past its
      own end -- the condition is INVISIBLE to the compiler by construction **, because trailing
      matter is not an error in LaTeX, it is the normal way a file ends.

⌗ ** WHY NO EXISTING GATE SEES IT, WHICH IS THE ARGUMENT FOR A SEPARATE FILE. **
  · `check_compile` is the strongest gate in the corpus and is exactly the wrong instrument here:
    the text it cannot see is the text LaTeX does not read.  *A green compile is evidence FOR the
    defect's invisibility, not against its presence.*
  · `check_citations` / `check_citations_resolve` walk `\rcpt{}` and `\cite{}` occurrences in the
    source.  A stranded paragraph's citations resolve perfectly well -- *in the source.*
  · Every per-row and per-claim check in `corpus/` asks a question about a row or a sentence.
    ** This is a property of a FILE'S SHAPE, and a per-row check cannot see a whole-file property **
    -- the lesson `r3564` wrote down and this is its second instance.

⚠ ** AND IT IS THE EXACT FAILURE MODE THE WORK ORDER AT `r6435` NAMED **: *"a result that lands in a
register and not in its paper is the failure this session found twice."*  Here the result landed in
`THE_REGISTER.md`, in `CR_synthesis.tex`'s frontier table, and in a `.tex` file inside `corpus/` --
*and still not in the paper.*  A grep for the sentence finds it; a reader never does.

** WHAT IS ALLOWED AFTER `\end{document}`, STATED SO THE GATE IS NOT MERELY STRICT. **  Comments are
fine: `%`-lines are how a file records provenance, and they are no more visible to a reader than the
prose is -- but they are not CLAIMS, and nothing downstream cites them.  Blank lines are fine.
** Anything else is content that someone wrote to be read and that no one can read. **

⌗ Anchored to the first `\end{document}` in the file, since that is where LaTeX stops.  A file with
no `\end{document}` (an `\input`-fragment, an appendix body) is not a document and is skipped.

⌗ ** Calibrated against a known instance before being believed **, per the corpus's own rule that a
detector is not trusted until it has been shown to fire: `--selftest` seeds a paragraph past the end
of a synthetic document and requires the detector to flag it, and seeds the same paragraph BEFORE
the end and requires it not to.  *A gate written for a defect that is being fixed in the same
revision would otherwise pass for the wrong reason -- it would pass because the tree is clean, which
is indistinguishable here from passing because it cannot see.*

Exit 0 clean, 1 if any corpus `.tex` strands content past its own end.
"""

import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
END = r'\end{document}'


def strayed(text):
    r"""Non-blank, non-comment lines after the first `\end{document}`, as (lineno, text)."""
    lines = text.split('\n')
    for i, ln in enumerate(lines):
        if ln.strip().startswith(END):
            return [(j + 1, s) for j, s in enumerate(lines)
                    if j > i and s.strip() and not s.strip().startswith('%')]
    return []                                    # not a document; nothing to strand text past


def selftest():
    """The detector is shown to FIRE and shown to STAY QUIET, before its zero is believed."""
    body = '\\documentclass{article}\n\\begin{document}\nHello.\n'
    para = '\\emph{A result nobody can read.}\n'
    ok = True
    after = strayed(body + END + '\n\n' + para)
    print(f"    {'OK  ' if after else 'FAIL'}  seeded past the end -> flagged "
          f"({len(after)} line(s))")
    ok &= bool(after)
    before = strayed(body + para + END + '\n')
    print(f"    {'OK  ' if not before else 'FAIL'}  seeded before the end -> not flagged")
    ok &= not before
    comment = strayed(body + END + '\n\n% a provenance note, and not a claim\n')
    print(f"    {'OK  ' if not comment else 'FAIL'}  a trailing %-comment -> not flagged")
    ok &= not comment
    nodoc = strayed('\\section{A fragment}\nNo document here.\n')
    print(f"    {'OK  ' if not nodoc else 'FAIL'}  a file with no \\end{{document}} -> skipped")
    ok &= not nodoc
    return ok


def main():
    print()
    print('  check_tex_tail -- prose stranded past a paper\'s own \\end{document}')
    print()
    if '--selftest' in sys.argv:
        print('  CALIBRATION (the detector shown to fire before its zero is believed):')
        rc = 0 if selftest() else 1
        print()
        return rc

    bad = {}
    scanned = 0
    for path in sorted(glob.glob(os.path.join(HERE, '*.tex'))):
        text = open(path, encoding='utf-8', errors='replace').read()
        if END not in text:
            continue
        scanned += 1
        after = strayed(text)
        if after:
            bad[os.path.basename(path)] = after

    if bad:
        for name, after in bad.items():
            print(f'  ⛔ {name}: {len(after)} line(s) of content after \\end{{document}} -- '
                  f'written to be read, and unreadable')
            for lineno, s in after[:4]:
                print(f'        line {lineno}:  {s[:88]}')
            if len(after) > 4:
                print(f'        ... and {len(after) - 4} more')
        print()
        print('  ⇒ Move it INTO the document, or delete it.  A paper that compiles is not')
        print('    evidence the text is in it: LaTeX stops reading at \\end{document}, so')
        print('    this condition is invisible to check_compile by construction.')
        print()
        return 1

    print(f'  {scanned} document(s) scanned; none strands content past its own end.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
