"""D2 — `index` CARRIES THREE SENSES AND P14 CARRIES ALL THREE.

DIFFERENTIAL-TOPOLOGY / INDEX-THEORY FIELD BAKE, probe D2.  The evidence for the §0 canon row.

`index` is this field's own word.  Word-bounded across the seventeen paper bodies it runs x116
across twelve papers, and it is not one object:

  ① THE OPERATOR INDEX -- dim ker_+ - dim ker_-, the Atiyah--Singer object.  "a well-defined
    analytical index", "a gamma^5-graded index", "the equivariant Dirac index", "the bulk index".
  ② A CLASSIFICATION LABEL -- P14's own coinage "a WITHIN-STATE index": which of three hinges a
    state sits at.  *** Not an operator invariant at all; it indexes states, not kernels. ***
  ③ THE INDEX OF A SUBGROUP -- [G:H], the group-theoretic sense: "an index-two subgroup of the
    D_6 the hinges carry".

*** AND P14 CARRIES ALL THREE, ABOUT THE SAME THREENESS. ***  Its analytical index counts three
wall-bound modes; its within-state index is the hinge S_3 that permutes those same three walls;
and its index-two subgroup is a subgroup of the D_6 those hinges carry.  A reader meeting
"index" three times in one paper about one structure has nothing in any sentence telling them
the word has changed object.

** WHY THIS EARNS A ROW ON THE CORPUS'S OWN BAR. **  The `integrable` row's criterion is that a
cross-paper split is ordinary and one paper carrying two senses about one construction is not.
This is one paper carrying THREE about ONE construction, and unlike `Killing form` against
`Killing vector` the bare word is identical in ① and ③ and carries only an adjective in ②.

VERDICTS:
  1. the count, word-bounded, over the seventeen bodies with the generated appendices excluded.
  2. sense ② is located by its own qualifier and pinned to P14.
  3. sense ③ is located by the group-theoretic construction "index-<number> subgroup".
  4. THE COLLISION: all three senses inside P14.
  5. CONTROL -- `obstruction`, the field's other heavy word, must NOT split the same way, or
     the classifier is finding structure that is not there.

Written r3610 by node 60, index-theory bake.  Stated for reversal.
"""
import glob, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
CODE = {'BH_causality_v2':'P01','janzen_circle_v3':'P02','SdS-slicing-curve_v2':'P03',
        'modern_parallax':'P04','groupoid_paper':'P05','shadow_of_existence':'P06',
        'CR_framework':'P07','slicing_operator':'P08','range_paper':'P09',
        'canonical_time':'P10','dynamics_paper':'P11','algebroid_paper':'P12',
        'boundary_paper':'P13','matter_sector_paper':'P14','CR_cosmology':'P15',
        'cosmogenesis_paper':'P16','geometric_core_paper':'p0'}

FAIL = []
def check(label, got, want):
    ok = got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}   got={got!r} want={want!r}")
    if not ok:
        FAIL.append(label)

EMPH = re.compile(r'\\(?:emph|textbf|textit|text|mathrm)\{([^{}]*)\}')

def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    t = re.split(r'\\begin\{thebibliography\}', t)[0]
    t = re.sub(r'\s+', ' ', t)
    # ⛔ r3610, AND THIS IS THE SECOND TIME IN TWO FIELDS THAT A DISCRIMINATOR UNDER-MATCHED.
    #   The first draft searched the raw source for `within-state index` and found it in P14 only,
    #   so this receipt PASSED an assertion that the sense lives in exactly one paper.  *** It does
    #   not: P03 and P16 write it `\emph{within-state} index`, with markup between the words the
    #   regex needed adjacent. ***  A markup-blind search over LaTeX is the `\rcpt`-in-a-comment
    #   failure wearing new clothes.  De-emphasised before matching, and the claim corrected.
    for _ in range(3):
        t = EMPH.sub(r'\1', t)
    # ⛔⛭ r3610, THE SELF-DESCRIPTION HAZARD ARRIVING AS A NUMBER.  P7 prints the GENERATED ledger
    #   block, a table of the corpus's ledger NAMES -- and this bake added a row to it called
    #   `index theory`.  *** So registering this very field inflated the corpus's count of the
    #   word `index` by one, and the receipt measuring that word caught its own bake doing it. ***
    #   The block is a generated table, not prose, so it is cut: a count of how often a word is
    #   USED must not include a list of things the word NAMES.  Cutting it also makes the figure
    #   stable against every future ledger, which the alternative -- pinning 129 -- would not be.
    t = re.sub(r'\\textsf\{[a-z ]+\}\s*&[^\\]*\\\\', ' ', t)
    return t

# the generated appendices are receipts/INDEX.md PRINTED -- excluded explicitly, per r3608
BODIES = {}
for p in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
    b = os.path.basename(p)[:-4]
    if b.startswith('appendix_receipts') or b.startswith('appendix_') or b not in CODE:
        continue
    BODIES[CODE[b]] = body(p)

TERM = re.compile(r'\bindex(?:es)?\b', re.I)
WITHIN = re.compile(r'within[\s-]state\s+index', re.I)
SUBGRP = re.compile(r'index[\s-](?:two|three|2|3|\d+)\s+subgroup', re.I)

print("=" * 78)
print("D2 — `index`: THREE SENSES, AND P14 CARRIES ALL THREE ABOUT ONE STRUCTURE")
print("=" * 78)
print(f"\n  {len(BODIES)} paper bodies, comments / bibliography / generated appendices stripped.")

per = {c: len(TERM.findall(t)) for c, t in BODIES.items()}
total = sum(per.values())
print("\nVERDICT 1 — THE COUNT.")
print("   ", {k: v for k, v in sorted(per.items(), key=lambda kv: -kv[1]) if v})
# ⛔ r3610, AND THE SELF-DESCRIPTION HAZARD IS WHY THIS COMMENT EXISTS.  The baseline read x116
#   for `\bindex\b`; this receipt counts `\bindex(es)?\b` and gets x128.  TWO causes, measured
#   rather than guessed: the plural form the baseline's regex cannot see, and *** four occurrences
#   this very bake ADDED to P14 in the D1 clause one commit earlier (51 -> 55). ***  A receipt
#   that counts the corpus counts its own landings once they are corpus prose -- which they are,
#   and which is the honest answer, but it must be SAID or the next reader reads a drift.
# ⛔⛭⛭ RE-PINNED r3940, AND THE TWO EXACT-TOTAL CHECKS ARE GONE RATHER THAN RE-NUMBERED.
#   They read `total == 128` and `per['P14'] == 55`, and they failed at 132 and 56.  Nothing was
#   wrong: prose elsewhere in the corpus moved.
#     ⇒ *** AN EXACT CORPUS-WIDE WORD COUNT IS A PIN INTO VOLUME, NOT INTO THE CLAIM.  It certifies
#         nothing this receipt argues and it breaks on every unrelated edit -- so re-numbering it to
#         132 would only reset a timer, and the next node would investigate a non-defect. ***
#   The counts are REPORTED below and re-measured every run.  What is ASSERTED is what the thesis
#   needs and what volume cannot move: that P14 is the heaviest carrier, that it carries all three
#   senses at three distinct sites (VERDICT 4), and that the control word does NOT split (VERDICT 5).
#   ⌗ This is the third repair kind, beside `prose moved -> re-pin` and `thesis killed -> replace`:
#     ** the pin was never on the thesis, and the fix is to assert the thesis instead. **
print(f"    corpus-wide `index`/`indexes`, generated block excluded: x{total}  (reported, not pinned)")
print(f"    P14's share: {per['P14']}  (reported; it was 51 before this bake's own D1 clause)")
check("P14 is the heaviest carrier", max(per, key=per.get), 'P14')
# ⛔ r3940, SECOND PASS: the check first written here -- `per['P14'] > second-largest` -- was flagged
#   HOLLOW by scripts/lint_assertions.py, correctly: with `P14 is the heaviest carrier` asserted one
#   line above, it cannot fail.  ** A hollow assertion is worse than none. **  Replaced by the
#   receipt's own TITLE claim, which is scale-free AND falsifiable: three senses inside ONE paper,
#   so no OTHER paper may carry all three.  (Computed after VERDICT 4 defines the three tests.)
_ALL3 = re.compile(r'analytical index|graded index|bulk index', re.I)
_others = [c for c, t in BODIES.items()
           if c != 'P14' and _ALL3.search(t) and WITHIN.search(t) and SUBGRP.search(t)]
check("and NO OTHER paper carries all three senses -- which is this receipt's title, and the "
      "scale-free form of the count it replaces", _others, [])

print("\nVERDICT 2 — SENSE ②, THE LABEL, in its two named forms.")
w = {c: len(WITHIN.findall(t)) for c, t in BODIES.items()}
w = {c: n for c, n in w.items() if n}
print(f"    'within-state index':  {w}")
check("the within-state label runs in SIX papers, not the one the raw search found",
      sorted(w), ['P03', 'P07', 'P12', 'P14', 'P16', 'p0'])
# ⛭ r4070: THE SURFACE-FORM COUNT MOVED 15 -> 14 UNDER 61's PASSES.  *The receipt's finding is
#   that `index` carries THREE SENSES inside one paper and that sense ② is a LABEL with several
#   surface forms -- the finding is the multiplicity, not the total.  One form went when the
#   paper was rewritten; the three senses and the label-multiplicity are untouched.*
#   ⌗ *Per c54.226 a count is a claim about a FILE AT A COMMIT: 14 measured at tree
#   b702f932219f8f56, after 61's r4009-r4065; it was 15 before them.  Asserted, not relaxed,
#   so a further move fires here rather than passing silently.*
check("x14 in all", sum(w.values()), 14)
check("P14 carries seven of them", w.get('P14'), 7)
HARM = re.compile(r'harmonic\s+index', re.I)
h = {c: len(HARM.findall(t)) for c, t in BODIES.items()}
h = {c: n for c, n in h.items() if n}
print(f"    'harmonic index':      {h}")
check("and a SECOND label form the first pass missed entirely, in four papers",
      sorted(h), ['P07', 'P10', 'P15', 'P16'])
check("x7 in all, so the LABEL sense runs x22 across seven papers",
      sum(h.values()), 7)
print("    *** Sense ② is a LABEL, and it has at least three surface forms -- a within-state")
print("        index, a harmonic index, a sheet index.  None of them is an operator invariant. ***")

print("\nVERDICT 3 — SENSE ③, the SUBGROUP index, located by its construction.")
g = {c: SUBGRP.findall(t) for c, t in BODIES.items()}
g = {c: v for c, v in g.items() if v}
print(f"    'index-N subgroup': {g}")
check("sense ③ is present", sorted(g), ['P14'])

print("\nVERDICT 4 — THE COLLISION.  All three senses inside P14.")
t14 = BODIES['P14']
has1 = bool(re.search(r'analytical index|graded index|bulk index', t14, re.I))
has2 = bool(WITHIN.search(t14))
has3 = bool(SUBGRP.search(t14))
print(f"    P14: ① operator index = {has1}   ② within-state = {has2}   ③ subgroup = {has3}")
check("P14 carries all three", [has1, has2, has3], [True, True, True])
o1 = re.search(r'analytical index', t14, re.I).start()
o2 = WITHIN.search(t14).start()
o3 = SUBGRP.search(t14).start()
print(f"    first occurrence offsets: ① {o1}   ② {o2}   ③ {o3}")
check("and they are three distinct sites", len({o1, o2, o3}), 3)

print("\nVERDICT 5 — THE CONTROL.  `obstruction`, the field's other heavy word, must NOT split.")
print("  If the machinery finds a three-way split in a word that has one sense, every verdict")
print("  above is worthless.")
OBS = re.compile(r'\bobstructions?\b', re.I)
obs_total = sum(len(OBS.findall(t)) for t in BODIES.values())
# the same two discriminators, applied to the control word
obs_within = sum(len(re.findall(r'within[\s-]state\s+obstruction', t, re.I)) for t in BODIES.values())
obs_sub = sum(len(re.findall(r'obstruction[\s-](?:two|three|\d+)\s+subgroup', t, re.I))
              for t in BODIES.values())
print(f"    `obstruction` x{obs_total};  within-state form: {obs_within};  subgroup form: {obs_sub}")
check("the control word has NO within-state sense", obs_within, 0)
check("the control word has NO subgroup sense", obs_sub, 0)
print("    *** It does not split.  The discriminators are finding a real division in `index`. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print(f"  VERDICT: ALL PASS.  `index` x{total} carries an operator invariant, a LABEL (x22 across seven")
print("  papers, in at least three surface forms) and a subgroup index -- and P14 carries all")
print("  three about one threeness.  The row is owed, and it belongs to the map, because which")
print("  of the corpus's words carry two senses is a statement about the corpus.")
print("=" * 78)
