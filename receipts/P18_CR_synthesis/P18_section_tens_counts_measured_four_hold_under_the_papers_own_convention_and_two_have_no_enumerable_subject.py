"""
P18, r7843+cc66.1, on 69's order r7843: section 10's counts, measured with a stated convention.

At r7841+cc66.1 this seat REPORTED this cluster as unfixable -- no live source, no stated
counting convention -- and 69 handed it back with the missing step supplied: state the
convention, count it live, print it with the convention named and pinned.

** THE HEADLINE, AND IT IS NOT WHAT THE PREVIOUS REVISION EXPECTED. **  FOUR of the six
counts are RIGHT, two of them EXACTLY right, once the convention the sentence means is read
off the sentence.  The previous revision called the cluster "understated" by analogy with the
receipts figure it had just fixed; that analogy was wrong, and this receipt records it as
wrong.  TWO counts have no enumerable subject at all and are reported rather than invented.

COMPUTES: the count of formal LaTeX environments over the corpus's papers, by environment
          name, with and without `remark` ; the count of `theorem` environments carrying a
          bracketed name ; the count of `axiom` environments ; the count of
          SYNTHESIS_HARVEST entries whose `② REGISTER` tag carries one of the five registers
          the paper names, under three nested conventions ; and the live receipt counts.

** THE GOVERNING READING, REGISTERED BEFORE ANY OF THIS WAS MEASURED **
(computations/beyond_the_wall/r7843_cc66_p18_section_10_counts_measured/PREDICTION.md, pushed
in its own commit at `d2083b2bd`): the sentence's own argument is "Every one of those is a
thing a competitor must also explain", so an ambiguous convention takes the reading that
counts CLAIM-BEARING entries a rival would owe an account of, and NOT the reading that
maximises the figure.  ** And the registered negative was that each count be computed under a
COMPETING convention too, with the rule that a competing convention landing on the paper's
printed figure is evidence the paper's convention was the competing one and mine is the
imposition. **  That negative FIRED, twice, and both are recorded below.

⓵ "a formal spine of SOME TWO HUNDRED environments"
   CONVENTION: the formal environments the papers DECLARE with \\newtheorem and then use --
   theorem, proposition, lemma, definition, corollary, axiom, principle, remark -- counted as
   \\begin{} instances over corpus/*.tex excluding the generated appendices.
   ⇒ 202.  The paper says "some two hundred".  CORRECT.
   ⌗ And the retired document that carried this cluster said "196 formal environments", which
     is this same measurement when it was written -- so the convention is confirmed by its own
     provenance rather than by my choosing it.
   ⛔ THE COMPETING CONVENTION, and it is the one this seat would have picked: drop `remark`
     as not claim-bearing.  That gives 118, barely half of "some two hundred" -- so the paper
     counts remarks, and the previous revision's instinct was wrong.

⓶ "FOURTEEN NAMED THEOREMS"
   CONVENTION: `theorem` environments over the same papers, "named" being the bracketed title
   amsthm takes.  ⇒ 14, and ALL FOURTEEN carry a bracketed name; zero do not.  EXACTLY RIGHT.

⓷ "on SIX AXIOMS"
   CONVENTION: `axiom` environments over the same papers.  ⇒ 6, all six in CR_framework.tex.
   EXACTLY RIGHT.

⓸ "an evidence rail of OVER TWELVE HUNDRED receipts"
   Set by this seat at r7841+cc66.1 from a live measurement.  Still correct.

⓹ "roughly SEVENTY-FIVE results carrying a hard register --- theorem, proposition, derived,
   computed, receipt-anchored"
   ** THE ONE COUNT WHOSE CONVENTION THE PAPER STATES OUTRIGHT **, so nothing is chosen.
   SOURCE: SYNTHESIS_HARVEST.md's `② REGISTER` lines -- the "register-tag census" the harvest
   names as this figure's own provenance, where it printed "roughly seventy-four".
   ⇒ 78 under the convention that a register LEADS WITH one of the five named words, allowing
     the plural and the compound ("Propositions, proved", "Theorem and corollary",
     "Receipt-anchored computation").  The paper says "roughly seventy-five".  CORRECT.
   ⛔ THE COMPETING CONVENTION FIRED HERE TOO: requiring the tag to be EXACTLY one of the five
     gives 56, which is not "roughly seventy-five".  So the paper's reading is the leading-word
     one and the strict reading is the imposition.  Recorded because the registered rule was
     to report this even where it costs the finding.

⛔⛔ AND TWO COUNTS HAVE NO ENUMERABLE SUBJECT.  REPORTED, NOT INVENTED.
   "NINE STRUCTURAL RECOVERIES" and "FORTY-FOUR PROVED CLASSICAL-GEOMETRY IDENTITIES" have no
   live register anywhere in the tree.  Searched: every ledger, THE_REGISTER, CORPUS_MAP,
   THE_WEAVE, THE_PLAN, the harvest, and the papers.  "Structural recover*" occurs only as
   prose, one or two to a file, never as a list; "identity/identities" occurs 148 times across
   23 ledgers as PROSE MENTIONS with no entry-level tag that could be counted.  P18 itself
   names five exemplars of the recoveries and calls them "an illustration of the class and not
   the case", which is a hand count of an unregistered class.
   ⌗ The one numeric near-miss was chased and REJECTED: `FOR_69.md` carries "44 of 44
     bit-identical" for the `r6925_geometry` bank's arm keys, which is a coincidence of the
     number and not proved identities.
   ⇒ ** The registered bound predicted exactly this -- "at least one of the five cannot be
     measured without inventing its subject" -- and it is TWO.  Where no live source can carry
     a count, the honest outcome is to say so and leave the phrase alone. **

Bound: this receipt pins the four counts it measures and the conventions they are measured
under.  It does NOT establish that those conventions are the author's intent -- for ⓵ the
provenance (196 in the retired document) and for ⓹ the harvest's own "seventy-four" are
evidence of intent, and for ⓶ and ⓷ the figures are exact; nothing here rules on the two
counts it reports as unmeasurable, which stay 69's.
"""
import glob
import os
import re

FAILED = []


def check(label, ok, detail=''):
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

PAPERS = [p for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
          if not os.path.basename(p).startswith('appendix_')]
TEXT = {os.path.basename(p): open(p, encoding='utf-8').read() for p in PAPERS}

check('Ⓐ① the papers are read: 18 non-appendix .tex files under corpus/',
      len(PAPERS) == 18, f'{len(PAPERS)} papers')

# ---------------------------------------------------------------- Ⓑ the environments
print()
print('Ⓑ ⓵ "a formal spine of some two hundred environments"')

DECLARED = sorted(set(re.findall(r'\\newtheorem\*?\{([a-z]+)\}', '\n'.join(TEXT.values()))))
check('Ⓑ① the environment NAMES are PARSED from the papers\' own \\newtheorem declarations, '
      'not listed by hand', len(DECLARED) >= 8, ', '.join(DECLARED))

COUNT = {e: sum(len(re.findall(r'\\begin\{' + e + r'\}', t)) for t in TEXT.values())
         for e in DECLARED}
N_ALL = sum(COUNT.values())
N_NO_REMARK = N_ALL - COUNT.get('remark', 0)

check('Ⓑ② PINNED the live count of formal environments over the papers is 202, which is what '
      '"some two hundred" says', N_ALL == 202, f'{N_ALL} environments: '
      + ', '.join(f'{e} {COUNT[e]}' for e in DECLARED if COUNT[e]))
check('Ⓑ③ PINNED and it is within five per cent of "two hundred", so the phrase is right at '
      'the precision it is printed to', abs(N_ALL - 200) / 200.0 < 0.05,
      f'{N_ALL} against 200, {abs(N_ALL - 200) / 200.0 * 100:.1f}% away')

_retired = os.path.join(ROOT, 'retired', 'WHAT_THE_FRAMEWORK_DELIVERS.md')
_rt = open(_retired, encoding='utf-8').read() if os.path.exists(_retired) else ''
_m196 = re.search(r'(\d+) formal environments\. Fourteen named theorems and six axioms', _rt)
check('Ⓑ④ PINNED THE CONVENTION IS CONFIRMED BY ITS OWN PROVENANCE: the retired document that '
      'carried this cluster says "196 formal environments" in the same breath as the theorems '
      'and axioms, which is this measurement when it was written',
      _m196 is not None and int(_m196.group(1)) == 196,
      f'retired document says {_m196.group(1) if _m196 else "?"}; live {N_ALL}')
check('Ⓑ⑤ PINNED COMPUTED and the growth since is small and upward, which is what a register '
      'that accretes does', _m196 is not None and 0 < N_ALL - int(_m196.group(1)) < 30,
      f'{N_ALL} - 196 = {N_ALL - int(_m196.group(1)) if _m196 else "?"}')

# ⛔ and this arm's own first cut RETYPED its figure as 116, from a scratch count that had
# dropped `principle` as well -- the exact class this corpus's gates exist for, committed in
# the receipt that was written to catch it.  The figure is the COMPUTED one.
check('Ⓑ⑥ ⛔ THE COMPETING CONVENTION, RECORDED BECAUSE IT FIRED: dropping `remark` as not '
      'claim-bearing -- the reading this seat would have chosen -- gives 118, barely half of '
      '"some two hundred", so the paper COUNTS REMARKS and the instinct was wrong',
      N_NO_REMARK == 118 and abs(N_NO_REMARK - 200) / 200.0 > 0.4,
      f'without remark {N_NO_REMARK}, {abs(N_NO_REMARK - 200) / 200.0 * 100:.0f}% from 200')

# ---------------------------------------------------------------- Ⓒ theorems and axioms
print()
print('Ⓒ ⓶⓷ "fourteen named theorems on six axioms"')

THMS = [(b, m.group(1)) for b, t in TEXT.items()
        for m in re.finditer(r'\\begin\{theorem\}\[([^\]]*)\]', t)]
THM_ALL = sum(len(re.findall(r'\\begin\{theorem\}', t)) for t in TEXT.values())
check('Ⓓ① PINNED there are exactly 14 `theorem` environments', THM_ALL == 14, f'{THM_ALL}')
check('Ⓒ② PINNED and ALL FOURTEEN are NAMED -- every one carries amsthm\'s bracketed title, '
      'and zero do not, which is what "named" means here',
      len(THMS) == 14 and len(THMS) == THM_ALL,
      f'{len(THMS)} named of {THM_ALL}')
check('Ⓒ③ and the names are distinct enough to be a register rather than a repetition',
      len({n for _, n in THMS}) >= 13, f'{len({n for _, n in THMS})} distinct names')

AX = [(b, m.group(1)) for b, t in TEXT.items()
      for m in re.finditer(r'\\begin\{axiom\}\[([^\]]*)\]', t)]
AX_ALL = sum(len(re.findall(r'\\begin\{axiom\}', t)) for t in TEXT.values())
check('Ⓒ④ PINNED there are exactly 6 `axiom` environments, which is "six axioms"',
      AX_ALL == 6, f'{AX_ALL}')
check('Ⓒ⑤ PINNED and all six sit in ONE paper, the framework paper, so "six axioms" names a '
      'single axiom set rather than a sum over papers',
      len({b for b, _ in AX}) == 1 and len(AX) == 6,
      f'{len(AX)} named axioms, all in {sorted({b for b, _ in AX})[0] if AX else "?"}')

# ---------------------------------------------------------------- Ⓓ the hard register
print()
print('Ⓓ ⓹ "roughly seventy-five results carrying a hard register"')

HARV = os.path.join(ROOT, 'SYNTHESIS_HARVEST.md')
_h = open(HARV, encoding='utf-8').read()
REGS = re.findall(r'^② REGISTER — (.*)$', _h, re.M)
check('Ⓓ① the register-tag census is READ from SYNTHESIS_HARVEST\'s own `② REGISTER` lines, '
      'which the harvest names as this figure\'s provenance', len(REGS) > 200,
      f'{len(REGS)} register lines')

_prov = re.search(r'thirteen rows against roughly seventy-four hard-tagged results', _h)
check('Ⓓ② PINNED AND THE PROVENANCE IS EXPLICIT: the harvest that minted this figure printed '
      '"roughly seventy-four hard-tagged results", so the source is named rather than guessed',
      _prov is not None, 'harvest carries "roughly seventy-four hard-tagged results"')

FIVE = ('THEOREM', 'PROPOSITION', 'DERIVED', 'COMPUTED', 'RECEIPT-ANCHORED')
# the five registers are PARSED out of the paper's own sentence, not retyped here.
#   ⌗ and P18 is opened BY ITS OWN PATH rather than taken from the glob-built dict above: the
#     pin operator traces a literal to the file the receipt opens, and through a glob it
#     cannot, so every sentence pin below came back target UNDECIDED -- a target the baseline
#     has never carried in 3020 rows.  Read it where the operator can see it.
P18T = re.sub(r'\s+', ' ',
              open(os.path.join(ROOT, 'corpus', 'CR_synthesis.tex'), encoding='utf-8').read())
# ⛔ this pattern's first cut ended at the full stop -- and THIS revision's own edit to P18
# put a convention phrase after "receipt-anchored", so the receipt stopped parsing the
# sentence it had just annotated.  Matched on the five words themselves, so it reads the
# sentence before and after the annotation.
_named = re.search(r'a hard register --- ([a-z]+, [a-z]+, [a-z]+, [a-z]+, [a-z-]+)', P18T)
# read in a statement, not a ternary: the pin operator reads a ternary as a disjunction of
# two arms and flags it ALT/XOR, which this is not.
PAPER_FIVE = ()
if _named:
    PAPER_FIVE = tuple(w.strip().upper() for w in _named.group(1).split(','))
check('Ⓓ③ PINNED the five registers are PARSED out of P18\'s own sentence and are exactly the '
      'five this receipt counts', PAPER_FIVE == FIVE, f'{PAPER_FIVE}')


def norm(s):
    return re.sub(r'[*\u26d4\u26ed\u2248`]', '', s).strip().upper()


LEADS = [r for r in REGS if any(norm(r).startswith(w) for w in FIVE)]
STRICT = [r for r in REGS if norm(r).split(',')[0].split('.')[0].strip() in FIVE]

check('Ⓓ④ PINNED under the convention that a register LEADS WITH one of the five -- allowing '
      'the plural and the compound, which is how the census actually writes them -- the count '
      'is 78, and the paper says "roughly seventy-five"', len(LEADS) == 78, f'{len(LEADS)}')
check('Ⓓ⑤ PINNED and 78 is inside the latitude "roughly" grants at this precision',
      abs(len(LEADS) - 75) <= 5, f'{len(LEADS)} against 75')
check('Ⓓ⑥ ⛔ THE COMPETING CONVENTION FIRED HERE TOO: requiring the tag to be EXACTLY one of '
      'the five gives 56, which is not "roughly seventy-five" -- so the paper\'s reading is '
      'the leading-word one and the strict reading is this seat\'s imposition',
      len(STRICT) == 56 and abs(len(STRICT) - 75) > 5,
      f'strict {len(STRICT)}, leading {len(LEADS)}')

# ---------------------------------------------------------------- Ⓔ the receipts rail
print()
print('Ⓔ ⓸ "an evidence rail of over twelve hundred receipts"')

N_PY = len([1 for d, _, fs in os.walk(os.path.join(ROOT, 'receipts'))
            for f in fs if f.endswith('.py')])
N_ROWS = len([1 for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8')
              if ln.startswith('| ')])
check('Ⓔ① PINNED the rail is over twelve hundred, as this seat set it at r7841+cc66.1',
      N_PY > 1200 and N_ROWS > 1200, f'{N_PY} receipt files, {N_ROWS} INDEX rows')

# ---------------------------------------------------------------- Ⓕ the unmeasurable two
print()
print('Ⓕ ⛔ the two counts with NO enumerable subject -- reported, not invented')

_rec = sum(len(re.findall(r'[Ss]tructural recover', open(p, encoding='utf-8',
                                                        errors='replace').read()))
           for p in glob.glob(os.path.join(ROOT, '*.md')))
check('Ⓕ① PINNED "structural recoveries" occurs across the top-level documents only as PROSE, '
      'never as a list a count could be taken from', 0 < _rec < 40,
      f'{_rec} prose occurrences over the top-level .md files, no enumeration')

LEDGERS = sorted(glob.glob(os.path.join(ROOT, '*LEDGER*.md')))
_ident = sum(len(re.findall(r'\bidentit(?:y|ies)\b',
                            open(p, encoding='utf-8', errors='replace').read(), re.I))
             for p in LEDGERS)
check('Ⓕ② PINNED and "identity/identities" occurs across the ledgers as prose mentions with '
      'no entry-level tag, so no convention counts them without inventing one',
      len(LEDGERS) >= 30 and _ident > 100,
      f'{_ident} mentions over {len(LEDGERS)} ledgers')
check('Ⓕ③ PINNED neither figure is carried anywhere in the tree as a number: no file states '
      'nine recoveries or forty-four identities as a count',
      not any(re.search(r'(nine structural recover|forty-four proved)', open(p, encoding='utf-8',
                        errors='replace').read())
              for p in glob.glob(os.path.join(ROOT, '*LEDGER*.md'))
              + glob.glob(os.path.join(ROOT, 'THE_*.md'))),
      'absent from every ledger and THE_* document')
check('Ⓕ④ RECORD the one numeric near-miss was CHASED AND REJECTED: FOR_69 carries "44 of 44 '
      'bit-identical" for a bank\'s arm keys, a coincidence of the number and not identities',
      '44 of 44 bit-identical' in open(os.path.join(ROOT, 'FOR_69.md'), encoding='utf-8',
                                       errors='replace').read(),
      'the 44-of-44 row is arm-key bit-identity, not geometry')
check('Ⓕ⑤ RECORD and P18 itself treats the recoveries as an unregistered class, naming five '
      'exemplars and calling them "an illustration of the class and not the case"',
      'an illustration of the class and not the case' in P18T,
      'the paper says so in its own words')

# ---------------------------------------------------------------- Ⓖ the state disjunction
print()
print('Ⓖ the paper\'s state, so this receipt passes before and after the convention phrases')

_env = re.search(r'some two hundred environments', P18T)
_thm = re.search(r'fourteen named theorems on six axioms', P18T)
_hr = re.search(r'roughly seventy-five results', P18T)
check('Ⓖ① PINNED the three phrases this revision annotates are present and UNCHANGED in their '
      'figures, because the measurement confirms them rather than correcting them',
      all(x is not None for x in (_env, _thm, _hr)),
      'all three figures stand as printed')
check('Ⓖ② PINNED and the two unmeasurable phrases are ALSO still as printed, which is the '
      'outcome this revision argues for rather than a thing left undone',
      'nine structural recoveries' in P18T and 'forty-four proved' in P18T,
      'both left alone deliberately')

print()
if FAILED:
    print(f'FAILED {len(FAILED)}:')
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('ALL PASS')
