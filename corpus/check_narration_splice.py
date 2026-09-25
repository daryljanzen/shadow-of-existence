#!/usr/bin/env python3
"""
check_narration_splice -- did an appended narration land INSIDE a sentence?

`THE_FRONTIER.md` is generated in full from the `EST` table in `scripts/regen_frontier.py`, and
each narrowing appends a narration to a row's entry.  Three breaks have now happened in the same
few characters of that table: `r6805` and `r6809` were parse failures from an apostrophe inside a
single-quoted literal, and `r6830` repaired two narrations inserted between "against the control"
and "'s 0.9559" -- which split the sentence carrying the target number and left the view reading
"...gives for m^2 alpha^2.'s 0.9559, bluer by 0.039."

** `check_generators_parse` cannot see this one, and that is the point: the file PARSES and RUNS,
and the OUTPUT is what is wrong. **  So this gate reads the generated view rather than the
generator, and looks for the one signature a mid-sentence insertion leaves -- a sentence's
terminator immediately followed by a clitic that cannot begin a sentence.

⌗ GATED on the generated view only, and REPORTED elsewhere.  A splice in `THE_FRONTIER` is a live
regeneration defect and fails.  The same signature in a hand-written RECORD is history and is
printed rather than failed -- there is one in `CORPUS_MAP`'s `r1491` changelog entry, where two
possessives lost their paper labels; one owner is recoverable (`P15`, the phrase is in
`CR_cosmology.tex`) and the other is not, the phrase surviving in no paper.  ** So it is reported
and NOT quietly repaired, because rewriting a frozen changelog on an inference is worse than the
defect. **

⌗ Narrow on purpose.  Not a grammar checker and not to become one: it reports only patterns no
correct English sentence produces, so a hit is a defect and not a style note.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GATED = ('THE_FRONTIER.md',)                                     # generated in full -- a hit fails
REPORTED = ('CORPUS_MAP.md', 'THE_WEAVE.md', 'OPEN_PROBLEMS_MAP.md')   # hand-written -- printed only

PATTERNS = (
    (re.compile(r"[.!?]['’]s\s"),
     "a sentence terminator immediately followed by a possessive 's -- the r6830 signature exactly"),
    (re.compile(r"[.!?]\s+['’](?:s|t|re|ve|ll|d|m)\s"),
     "a sentence terminator followed by a bare clitic, which no sentence begins with"),
    (re.compile(r"[.!?](?:n't|'t)\s"),
     "a sentence terminator followed by a contraction's tail"),
)


def scan(name):
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        return None
    text = io.open(path, encoding='utf-8').read()
    out = []
    for rx, why in PATTERNS:
        for m in rx.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            lo = max(0, m.start() - 70)
            out.append((line, why, text[lo:m.end() + 40].replace('\n', ' ')))
    return out


def main() -> int:
    print()
    print("  check_narration_splice -- did an appended narration land inside a sentence?")
    print()
    failures = []
    for name in GATED:
        hits = scan(name)
        if hits is None:
            continue
        for line, why, ctx in hits:
            failures.append((name, line, why, ctx))
    print(f"    gated on {len(GATED)} generated view(s), {len(PATTERNS)} splice signature(s) each.")

    noted = []
    for name in REPORTED:
        for line, why, ctx in (scan(name) or ()):
            noted.append((name, line, why, ctx))
    if noted:
        print()
        print("    reported, not gated -- hand-written record text, where the same signature is")
        print("    history rather than a regeneration defect:")
        for name, line, why, ctx in noted:
            print(f"      ⌗ {name}:{line}  {why}")
            print(f"        ...{ctx}...")
        print()
        print("      ** Not repaired here on purpose: in CORPUS_MAP's r1491 entry two possessives")
        print("         lost their paper labels, one owner is recoverable from CR_cosmology.tex and")
        print("         the other survives in no paper.  Rewriting a frozen changelog on an")
        print("         inference is worse than the defect, so it is named and left. **")

    print()
    if not failures:
        print("    no narration landed inside a sentence in the generated view.")
        print()
        print("  ⌗ *Parse is not enough here, which is why this gate exists beside")
        print("    check_generators_parse: the file that broke three times parsed and ran every")
        print("    time, and the OUTPUT carried the defect.*")
        print()
        return 0

    for name, line, why, ctx in failures:
        print(f"    ⛔ {name}:{line}  {why}")
        print(f"       ...{ctx}...")
    print()
    print("    ⌗ A narration was appended at the wrong offset in scripts/regen_frontier.py's EST")
    print("      table.  Move the inserted block to the END of the entry rather than editing the")
    print("      sentence it split, and keep every word: r6830's repair asserted the non-whitespace")
    print("      character multiset unchanged, so the only token change was the reattached 's.")
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
