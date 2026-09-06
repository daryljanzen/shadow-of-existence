#!/usr/bin/env python3
"""check_source_hygiene -- what the .tex source would expose if a paper were submitted.

WHY THIS GATE EXISTS.  arXiv distributes the LaTeX SOURCE of every submission, not
only the PDF: anyone can download the author's original file, comments included.
Every other check in this corpus reads what PRINTS.  No gate reads comments, and
the compile never shows them, so a comment is the one part of a paper that no
instrument looks at and every reader of a submission can see.

The class was found the only way it could be -- by reading.  A working handle in
CR_framework.tex named the lapse-shift proposition with an epithet aimed at the
field the paper is addressed to (r4051).  It did not print.  It would have shipped.

WHAT THIS GATE IS NOT.  It does not strip anything, and it must not.  The comments
carry the corpus's own working apparatus -- revision markers, provenance notes,
scope warnings a later reader needs -- and that apparatus is load-bearing for the
work.  Deleting it to protect against a submission that has not happened would
damage the working corpus to buy nothing.

So this gate REPORTS.  It is a submission checklist, run when a paper is about to
go out, and its output is the list of comment lines that would become public.
Whether any given line goes is decided at submission, once, with the list in hand --
not by a standing edit to the source.

EXIT STATUS.  Always 0 for the apparatus classes: they are expected and are not
defects.  Non-zero ONLY for the epithet class, which is never appropriate in a
file that may be published and which has one instance in the corpus's history.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --- the one class that is a defect wherever it appears -----------------------
EPITHET = re.compile(
    r"\b(idiot|stupid|fuck\w*|shit|moron|imbecile|cretin|clueless|"
    r"incompeten\w+|lazy|fraud|charlatan|hack\b)\b", re.I)

# --- classes that are apparatus: reported, never failed on --------------------
APPARATUS = [
    ("workflow",   re.compile(r"\b(cold node|the node|a node|nodes|spin-?up|changelog)\b", re.I)),
    ("attribution", re.compile(r"\bDaryl\b", re.I)),
    ("revision",   re.compile(r"\br\d{3,4}\b")),
    ("marker",     re.compile(r"\b(TODO|FIXME|XXX|HACK)\b")),
]


def comment_lines(path):
    """Yield (lineno, text) for whole-line LaTeX comments.

    Inline comments are not scanned: a trailing % on a content line is almost
    always a line-break control in this corpus, and treating those as prose
    produced nothing but noise when it was tried.
    """
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("%"):
            yield n, line.strip()


def main():
    papers = sorted(p for p in HERE.glob("*.tex")
                    if not p.name.startswith("appendix_"))
    epithets = []
    counts = {name: 0 for name, _ in APPARATUS}
    per_paper = {}

    for path in papers:
        total = 0
        for n, text in comment_lines(path):
            total += 1
            if EPITHET.search(text):
                epithets.append((path.name, n, text))
            for name, rx in APPARATUS:
                if rx.search(text):
                    counts[name] += 1
        if total:
            per_paper[path.name] = total

    print("\n  check_source_hygiene -- what a submission's .tex would expose")
    print("  " + "-" * 66)
    print(f"  {sum(per_paper.values())} comment lines across {len(per_paper)} papers.\n")

    for name, _ in APPARATUS:
        print(f"    {name:12s} {counts[name]:4d} line(s)")

    print("\n  These are APPARATUS, not defects.  They are the corpus's working")
    print("  record and they stay.  The list matters at one moment only -- when a")
    print("  paper is about to be submitted -- and the decision then is the")
    print("  author's, made once with the list in hand.")
    print("\n  To see the lines for one paper before sending it:")
    print("    grep -n '^\\s*%' corpus/<paper>.tex\n")

    if epithets:
        print("  [FAIL] language that should never ship, in a file that may be published:")
        for fn, n, text in epithets:
            print(f"    {fn}:{n}  {text[:100]}")
        print("\n  ** A comment does not print and is not private.  Rewrite it to say")
        print("     what it means; the content of such a note is usually worth keeping.")
        return 1

    print("  OK    no epithet-class language in any comment.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
