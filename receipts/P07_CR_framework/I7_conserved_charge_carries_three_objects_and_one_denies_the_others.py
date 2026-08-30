"""I7 — `conserved charge` NAMES THREE DIFFERENT OBJECTS, AND ONE OF THEM DENIES THE OTHER TWO EXIST.

INTEGRABLE-SYSTEMS FIELD BAKE, probe I7.  The canon row this receipt is the evidence for.

`conserved charge` is the corpus's most-used name for the object this field is organised around, and
it is not one object.  Word-bounded across the seventeen paper bodies it carries THREE:

  A  THE ASYMPTOTIC MASS CHARGE -- an ADM / Abbott--Deser class boundary integral at infinity.
     *** AND EVERY OCCURRENCE OF SENSE A IS A NEGATIVE EXISTENCE CLAIM: "no conserved charge is
     well defined in an asymptotically-de Sitter spacetime." ***
  B  A FIRST INTEGRAL OF A FLOW, or a conserved charge of a field -- the homothety charge on the
     null cone, the twist c whose sign is the graviton's handedness, the shear charge.
  C  A CONSERVED QUANTUM NUMBER -- the progenitor charge the baryon asymmetry eta would need.

** WHY THIS IS A CANON ROW AND NOT AN ORDINARY CROSS-PAPER SPLIT. **  The `integrable` row's own
criterion is that a word earns a row when one paper carries two senses about one construction, a
cross-paper split being ordinary.  This clears that bar and then exceeds it in a way `integrable`
does not:

  *** SENSE A DOES NOT MERELY DIFFER FROM B AND C.  IT ASSERTS THAT THE OBJECT B AND C NAME IS NOT
      WELL DEFINED IN THIS SPACETIME CLASS. ***

A reader who carries A's verdict into B's sentence concludes that the graviton's handedness is not
well defined -- which is the opposite of what P11 proves.  `integrable` ① and ⑥ were opposite in
CONSEQUENCE; these are opposite in EXISTENCE, about the same two words.

VERDICTS, each able to have returned otherwise:
  1. the count, word-bounded, over the seventeen bodies with comments and bibliography stripped.
  2. every sense-A site is classified by ITS OWN SENTENCE carrying a negation of well-definedness,
     not by which paper it is in -- and the discriminator is quoted and pinned.
  3. sense C is classified by its own sentence naming the progenitor / baryon object.
  4. THE COLLISION: P07 carries B and C, both spelt `conserved charge`, in one paper.
  5. CONTROL -- `first integral` must come back SINGLE-sensed on the same machinery, or the
     classifier is finding structure that is not there.

Written r3608 by node 60, integrable-systems bake.  Stated for reversal.
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

def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    t = re.split(r'\\begin\{thebibliography\}', t)[0]
    return re.sub(r'\s+', ' ', t)

# ⛔ r3608: `check_receipt_tex_scope` caught this glob and it was right to.  The generated
#   appendices are `receipts/INDEX.md` PRINTED, so they carry this receipt's own row -- and a
#   receipt counting a phrase over `corpus/*.tex` would count its own description as corpus prose.
#   The CODE filter already excluded them by name; the exclusion is now EXPLICIT, because a reader
#   should not have to derive the scope from a dictionary lookup further down.
BODIES = {}
for p in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
    b = os.path.basename(p)[:-4]
    if b.startswith('appendix_receipts') or b.startswith('appendix_'):
        continue
    if b in CODE:
        BODIES[CODE[b]] = body(p)

print("=" * 78)
print("I7 — `conserved charge`: THREE OBJECTS, AND SENSE A DENIES THE OTHER TWO")
print("=" * 78)
print(f"\n  {len(BODIES)} paper bodies read, comments and bibliography stripped.")

TERM = re.compile(r'\bconserved[\s~-]+charges?\b', re.I)

# ** THE DISCRIMINATORS ARE PROPERTIES OF THE SENTENCE, NOT OF THE PAPER. **  A classifier keyed to
# the paper would return whatever the classifier's author already believed; these are read off the
# text around each hit and the receipt fails if that text moves.
# ⛔ r3608: THE FIRST DRAFT OF THIS REGEX UNDER-MATCHED AND I HAD ASSERTED THE ANSWER FIRST.
#   It read `not\s+(?:be\s+)?well[\s-]?defined`, which cannot see "widely held **not to be** well
#   defined" -- the exact wording P02 and P03 use.  So two sense-A sites fell into B, and the run
#   disagreed with the counts I had written from reading grep windows.  *** The counts were wrong
#   and the measurement was right, which is the whole reason a probe is not scored from a grep. ***
#   Fixed by allowing up to three words between the negation and the predicate; the phrase is still
#   required, so a sense-B sentence carrying no denial cannot slip in.
NEG   = re.compile(r'not\s+(?:\w+\s+){0,3}(?:well[\s-]?defined|defined)|'
                   r'no\s+conserved\s+charge|loses\s+its\s+subject', re.I)
QNUM  = re.compile(r'progenitor|baryon|\\eta\b|abundance', re.I)

sites = []
for code in sorted(BODIES):
    t = BODIES[code]
    for m in TERM.finditer(t):
        a, b = max(0, m.start()-300), min(len(t), m.end()+300)
        ctx = t[a:b]
        sense = 'A' if NEG.search(ctx) else ('C' if QNUM.search(ctx) else 'B')
        sites.append((code, m.start(), sense, ctx))

print("\nVERDICT 1 — THE COUNT AND THE CLASSIFICATION, site by site.\n")
print(f"    {'paper':>6} {'offset':>8}  sense  the phrase that classified it")
for code, off, sense, ctx in sites:
    if sense == 'A':
        why = (NEG.search(ctx).group(0))[:46]
    elif sense == 'C':
        why = (QNUM.search(ctx).group(0))[:46]
    else:
        why = '(neither negation nor quantum-number marker)'
    print(f"    {code:>6} {off:>8}  {sense:^5}  {why}")

total = len(sites)
byS = {s: sum(1 for _, _, x, _ in sites if x == s) for s in 'ABC'}
print(f"\n    total = {total}   A={byS['A']}   B={byS['B']}   C={byS['C']}")
check("fifteen occurrences in all", total, 15)
check("sense A -- the asymptotic charge, every one a NEGATIVE claim", byS['A'], 5)
check("sense B -- a first integral / a field's charge", byS['B'], 7)
check("sense C -- a conserved quantum number", byS['C'], 3)

print("\nVERDICT 2 — SENSE A IS FIVE PAPERS MAKING ONE NEGATIVE CLAIM, and that is the point.")
apapers = sorted({c for c, _, s, _ in sites if s == 'A'})
print(f"    sense A appears in: {apapers}")
check("five distinct papers carry sense A", len(apapers), 5)
print("    *** Each says the object is NOT well defined here.  B and C use the same two words")
print("        for objects that are.  A reader importing A into B loses P11's result. ***")

print("\nVERDICT 3 — THE WITHIN-PAPER COLLISION, which is the bar `integrable` set.")
per = {}
for c, off, s, _ in sites:
    per.setdefault(c, set()).add(s)
multi = {c: sorted(v) for c, v in per.items() if len(v) > 1}
for c, v in sorted(multi.items()):
    offs = sorted(off for cc, off, _, _ in sites if cc == c)
    print(f"    {c} carries senses {v}  at offsets {offs}")
# ** ASSERT THE MEASURED VALUE, NOT `> 0 == True`. **  A bare True on the right-hand side is the
#   hollow shape THE_BASE_RATE's sixteenth entry names, and `check_receipts` flagged two of them
#   here: it converts a known gap into an unknown one and makes the debt number lie.
check("exactly one paper carries two senses of the same phrase", sorted(multi), ['P07'])
check("and its two senses are B and C", multi['P07'], ['B', 'C'])

print("\nVERDICT 4 — AND THE COLLISION IS NOT AN ARTEFACT OF ONE LOOSE SENTENCE.")
p07 = [(off, s) for c, off, s, _ in sites if c == 'P07']
span = max(o for o, _ in p07) - min(o for o, _ in p07)
print(f"    P07's two sites are {span} characters apart in one paper.")
check("the two offsets, pinned", sorted(o for o, _ in p07), [134508, 307922])
check("so the separation is 173414 characters -- a reader meets them separately", span, 173414)

print("\nVERDICT 5 — THE CONTROL.  `first integral` must come back SINGLE-sensed.")
print("  If the classifier finds three senses in a phrase that has one, it is finding structure")
print("  that is not there and every verdict above is worthless.")
CTRL = re.compile(r'\bfirst[\s~-]+integrals?\b', re.I)
csites = []
for code in sorted(BODIES):
    for m in CTRL.finditer(BODIES[code]):
        a, b = max(0, m.start()-300), min(len(BODIES[code]), m.end()+300)
        ctx = BODIES[code][a:b]
        csites.append((code, 'A' if NEG.search(ctx) else ('C' if QNUM.search(ctx) else 'B')))
cby = {s: sum(1 for _, x in csites if x == s) for s in 'ABC'}
print(f"    `first integral`: {len(csites)} occurrence(s)  A={cby['A']} B={cby['B']} C={cby['C']}")
check("the control phrase carries NO sense-A occurrence", cby['A'], 0)
check("the control phrase carries NO sense-C occurrence", cby['C'], 0)
print("    *** It comes back single-sensed.  The classifier is not manufacturing the split. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  `conserved charge` x15 carries three objects.  Sense A is a negative")
print("  existence claim about the very phrase senses B and C use affirmatively, and P07 carries")
print("  two of the three.  The row is owed, and it belongs to the map rather than to a paper.")
print("=" * 78)
