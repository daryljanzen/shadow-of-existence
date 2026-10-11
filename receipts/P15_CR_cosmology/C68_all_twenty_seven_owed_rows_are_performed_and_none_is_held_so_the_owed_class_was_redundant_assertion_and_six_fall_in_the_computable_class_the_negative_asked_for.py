#!/usr/bin/env python3
"""P15 receipt -- `r7255`'s ORDER ①: PERFORM OR HOLD THE `27` `REPAIR-OWED` ROWS OF
`receipts/P15_CR_cosmology`, AND SAY OF EACH ONE WHETHER THE REPAIR WAS PERFORMED OR WHAT MADE IT
IMPOSSIBLE.

*** ⛭⛭⛭ `27` OF `27` PERFORMED.  `0` HELD.  The prefix carries NO owed row, and the order's question
    -- perform or hold -- has one answer for every row in the population.  `26` keys are RETIRED and
    `1` is re-verdicted in place. ***

** THE PARTITION, AND IT IS NOT THE ONE THIS CYCLE PRE-REGISTERED. **
  `11`  assertion DELETED and nothing replaced it
  ` 8`  limb-two SHORTENING -- `1` of the `8` also needed an ANCHORED SLICE
  ` 7`  WIDTH RE-CUT -- value plus anchor, the connective prose freed
  ` 1`  re-verdict and NOT a repair: `prop:flat` is a `\\label`, so limb ONE holds it
⇒ *** THE `27` WERE NOT A REWRITING BACKLOG.  `11` of them -- more than a third -- were REDUNDANT
    ASSERTION: the receipt already computed the quantity on the line beside the string it quoted.
    `rs_leaf 105.36 Mpc` sat beside `abs(rs_l_on - 105.36) < 0.5`.  The capability was never missing;
    the quotation was. ***
⌗ *And the pre-registration is scored as wrong in its structure rather than its counts: it sorted the
`27` by what the repair WOULD BE, and `11` needed no repair at all.  A pre-registration over repair
FORMS is a weaker instrument than one over repair NECESSITY.*

** ⛔⛭⛭⛭ AND `r7255`'s REACHABLE NEGATIVE FIRES, IN THE SCOPED FORM `FOR_66.md`'s `r7255+cc66` ②
   PRE-REGISTERED.  `6` of the `27` are carried by a form that survives every content-intact rewording
   and reds on the converse -- `4` by an AST PROPERTY TEST written this cycle, `2` by an INDEPENDENT
   COMPUTATION this seat wrote at `cc66.166` (all `81` Riemann components of `prop:flat`'s induced
   three-metric).  The band was `2`--`6`; the measurement is `6`, AT the top edge, which is a band
   that was nearly wrong rather than a prediction that was right. **
⇒ *The claim this receipt makes is NARROW and the gates below are built to it: `70`'s `r7251` negative
says no STRING form works, with "no syntactic or semantic gate was tried" written into its own scope.
Every form above is a SEMANTIC gate.  **So the negative is not refuted -- it is SCOPED, and the scope
line is `computable`, not `string`.***  ⌗ Which locates where `MEANING-HELD` is over-adopted: not
wherever a string could be found, but wherever a receipt could COMPUTE the claim.

** ⛔ LIMB TWO IS DEFEATED ON THE GRAIN CLAUSE'S OWN EXEMPLAR, BY THE SECOND OCCURRENCE THAT SATISFIED
   IT. **  `r7255` cites `c1ff798d` as the clause's canonical limb-two row, which `60` conceded BECAUSE
THE PAPER CARRIES THE SHORTER FORM ELSEWHERE.  *`Because the distance slicing is flat` occurs TWICE in
`CR_cosmology.tex`; the pinned long form occurs once.*  ⇒ ***So shortening converts a single-site pin
into a MULTI-site one -- a pin on the FILE and not on the claim.  Limb two's premise can be SATISFIED
BY a second occurrence and DEFEATED BY the same one, and the row needed an ANCHORED SLICE.***  ⌗ A
third measured limit on the clause, and an operational one: limb two needs an OCCURRENCE COUNT taken
BEFORE the shortening, not only a judgement that a shorter span carries the claim.

** AND THE WIDTH RE-CUT HAS TWO STRENGTHS, REPORTED AS TWO. **  `4` are fully reword-immune because
the anchor is a SYMBOL and the window carries no prose; `3` have their exposure REDUCED AND NOT
REMOVED because the anchor is prose.  *The pairing is not optional on the weak three: `$10.8\\%$`
occurs twice in the paper and `$185$` four times, so the digits alone would not anchor the read.*

** COMPUTES: nothing physical.  *** Arithmetic over this revision's own published manifest, plus live
reads of the corpus papers for the occurrence counts and AST reads of three receipts of this prefix
for the property-test measurement. ***
⚠ *** AND THIS RECEIPT MAKES NO LIVE READ OF THE LEDGER AT ALL -- gate `Ⓗ①` proves that from its own
    syntax tree.  That is the correction instance EIGHT of the fail-on-success class forced on
    `cc66.171`'s rule: a per-revision audit receipt's subject is the literal AS THAT REVISION RECORDED
    IT, and `r7255`'s order to PERFORM repairs retires keys, so even KEY IDENTITY is not a direction
    the corpus guarantees.  `check_quote_pins` keeps the ledger and the instrument in correspondence;
    that is not this receipt's job and asserting it here is how four of this cycle's fourteen
    instances were made. ***
"""
import ast
import glob
import hashlib
import os
import re
import time

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7255_cc66_P15_perform')
PREFIX = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')

# ⛭ THE SUBJECT IS THIS REVISION'S OWN MANIFEST, pinned by digest -- the same form C64, C65, C66 and
#   C67 use, and for the same two reasons: the order's auditability standard, and check_exact_counts.
DIGEST = {'PERFORMED.tsv': 'c2e3f0567a9fdb0e'}

OWED_AT_PREREG = 27          # the population r7255 ① names, and 66's own number
PRE_COMPUTABLE = (2, 6)      # FOR_66.md r7255+cc66 ②: "I expect 2-6 of the 27 to be in the
#                              computable class" -- pinned before a single repair was performed
FORMS = {'DELETED': 11, 'SHORTEN': 7, 'SHORTEN+ANCHOR': 1, 'RECUT': 7, 'REVERDICT': 1}
SUBFORMS = {'REDUNDANT': 5, 'AST-REPLACED': 4, 'COMPUTED-ELSEWHERE': 2,
            'SYMBOL-ANCHOR': 4, 'PROSE-ANCHOR': 3, 'LIMB-TWO': 8, 'LIMB-ONE': 1}
COMPUTABLE = ('AST-REPLACED', 'COMPUTED-ELSEWHERE')

# ⛭ the three SEMANTIC forms, by function name and the receipt whose syntax tree carries it
SEMANTIC = {
    '_hier_accepts_and_uses_none': 'P15_the_fitted_onset',
    '_rad_term_placement': 'P15_the_harmonic_expansion',
    '_prod_uses_phys': 'P15_the_harmonic_expansion',
}
# the names those receipts bind PAPER TEXT to.  A property test that names none of them reads no prose.
PAPERVARS = {'p15', 'p07', 'body15', 'fp15', 'fp07', 'TEX', 'PAPERS'}

EXEMPLAR_SHORT = 'Because the distance slicing is flat'
EXEMPLAR_LONG = 'Because the distance slicing is flat (Proposition~\\ref{prop:flat})'
BARE_DIGITS = ('$10.8\\%$', '$185$')

# ⛭ the generated appendices are receipts/INDEX.md PRINTED, so a receipt that globs them reads a
#   RETIRED paper state as live -- check_receipt_tex_scope's own finding, caught on C67 this cycle.
_PAPERS = [q for q in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
           if not os.path.basename(q).startswith('appendix_receipts')]
TEX = ''.join(open(q, encoding='utf-8').read() for q in _PAPERS)
CR15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()


def sha8(s):
    return hashlib.sha1(s.encode()).hexdigest()[:8]


def sha16_file(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


ROWS = [ln.rstrip('\n').split('\t') for ln in open(os.path.join(MINE, 'PERFORMED.tsv'), encoding='utf-8')
        if ln.strip() and not ln.startswith('#')]
STEM, OSHA, OLIT, FATE, FORM, SUB, NLIT, NOTE = range(8)


def fn_of(name):
    """the FunctionDef node called `name`, from the syntax tree of the receipt SEMANTIC assigns it."""
    pre = SEMANTIC[name]
    hits = [q for q in sorted(glob.glob(os.path.join(PREFIX, pre + '*.py')))]
    if len(hits) != 1:
        return None
    tree = ast.parse(open(hits[0], encoding='utf-8').read())
    found = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == name]
    return found[0] if len(found) == 1 else None


# ============================================================================ A
head("A -- THE MANIFEST IS THE SUBJECT, AND IT IS PINNED")

_dig = {k: sha16_file(os.path.join(MINE, k)) for k in DIGEST}
for k, v in _dig.items():
    print(f"    {k}: {v}  (pinned {DIGEST[k]})")
gate("Ⓐ① the manifest this receipt reads is the one this revision published, by digest",
     _dig == DIGEST)

gate(f"Ⓐ② it carries exactly the {OWED_AT_PREREG} rows the order names, each with 8 fields",
     len(ROWS) == OWED_AT_PREREG and all(len(r) == 8 for r in ROWS))

_keyed = [r for r in ROWS if sha8(r[OLIT]) == r[OSHA]]
print(f"    key integrity: {len(_keyed)} of {len(ROWS)} literals hash to their recorded sha8")
gate("Ⓐ③ every row's literal hashes to the sha8 beside it -- the manifest describes the keys it "
     "says it does, with no claim about whether they are still live",
     len(_keyed) == len(ROWS))

_under = [r for r in ROWS if r[STEM].startswith('receipts/P15_CR_cosmology/')
          and os.path.exists(os.path.join(ROOT, r[STEM]))]
_recs = sorted({os.path.basename(r[STEM]) for r in ROWS})
print(f"    {len(_recs)} receipts hold the {len(ROWS)} rows -- so the unit of work was "
      f"{len(_recs)} reads and not {len(ROWS)}")
gate("Ⓐ④ every row names a receipt of this prefix that exists in the working tree",
     len(_under) == len(ROWS))

# ============================================================================ B
head("B -- PERFORM OR HOLD: THE PARTITION, AND THE ANSWER IS `PERFORMED` FOR ALL 27")

_f = {}
for r in ROWS:
    _f[r[FORM]] = _f.get(r[FORM], 0) + 1
print(f"    forms: {dict(sorted(_f.items()))}")
gate(f"Ⓑ① the forms partition the {OWED_AT_PREREG} exactly as reported: "
     f"{FORMS['DELETED']} deleted, {FORMS['SHORTEN'] + FORMS['SHORTEN+ANCHOR']} limb-two "
     f"({FORMS['SHORTEN+ANCHOR']} of them anchored), {FORMS['RECUT']} width re-cut, "
     f"{FORMS['REVERDICT']} re-verdict",
     _f == FORMS and sum(FORMS.values()) == OWED_AT_PREREG)

_held = [r for r in ROWS if 'HELD' in r[FORM] or 'HELD' in r[SUB]]
print(f"    rows HELD: {len(_held)}")
gate("Ⓑ② NOT ONE ROW IS HELD -- the owed class in this prefix was not work nobody could do",
     len(_held) == 0)

_kept = [r for r in ROWS if r[FATE] == 'KEPT']
_retired = [r for r in ROWS if r[FATE] == 'RETIRED']
print(f"    fate: {len(_retired)} RETIRED, {len(_kept)} KEPT "
      f"-- KEPT forms {sorted({r[FORM] for r in _kept})}")
gate("Ⓑ③ fate and form agree with no slack: the re-verdict is the ONLY row whose key survives, "
     "because a performed repair retires the literal and a re-verdict does not",
     len(_kept) == FORMS['REVERDICT'] and all(r[FORM] == 'REVERDICT' for r in _kept)
     and len(_retired) == OWED_AT_PREREG - FORMS['REVERDICT'])

_short = [r for r in ROWS if r[FORM].startswith('SHORTEN')]
_strict = [r for r in _short if r[NLIT] != '-'
           and r[NLIT].strip('"') in r[OLIT].strip('"') and len(r[NLIT]) < len(r[OLIT])]
print(f"    limb two, measured rather than asserted: {len(_strict)} of {len(_short)} replacements are "
      f"a STRICTLY SHORTER CONTIGUOUS span of the literal they replace")
gate("Ⓑ④ every limb-two repair is what the clause's second limb licenses -- a strictly shorter "
     "contiguous substring -- and not a rewrite dressed as a shortening",
     len(_strict) == len(_short) == FORMS['SHORTEN'] + FORMS['SHORTEN+ANCHOR'])

# ============================================================================ C
head("C -- WHAT THE OWED CLASS ACTUALLY WAS: REDUNDANT ASSERTION, NOT MISSING CAPABILITY")

_s = {}
for r in ROWS:
    _s[r[SUB]] = _s.get(r[SUB], 0) + 1
print(f"    subforms: {dict(sorted(_s.items()))}")
gate("Ⓒ① the subforms reconcile: the 11 deletions are 5 REDUNDANT, 4 AST-REPLACED and "
     "2 COMPUTED-ELSEWHERE, and nothing else deletes a pin",
     _s == SUBFORMS
     and sum(_s[k] for k in ('REDUNDANT', 'AST-REPLACED', 'COMPUTED-ELSEWHERE')) == FORMS['DELETED'])

_del_frac = FORMS['DELETED'] / OWED_AT_PREREG
print(f"    deletions are {100 * _del_frac:.1f} per cent of the population")
gate("Ⓒ② more than a third of the owed class was discharged by DELETION -- the finding of ①, and "
     "the reason the pre-registration's families did not survive performance",
     _del_frac > 1 / 3)

_redundant = [r for r in ROWS if r[SUB] == 'REDUNDANT']
print(f"    each REDUNDANT row records the computation that already sat beside it:")
for r in _redundant:
    print(f"      {r[OSHA]}  {r[NOTE][:88]}")
gate("Ⓒ③ every REDUNDANT deletion names the test that made the quotation unnecessary, so the claim "
     "`the capability was never missing` is on the record row by row and not in prose only",
     len(_redundant) == SUBFORMS['REDUNDANT'] and all(len(r[NOTE]) > 20 for r in _redundant))

# ============================================================================ D
head("D -- THE THREE SEMANTIC FORMS, AND `r7255`'s REACHABLE NEGATIVE")

_nodes = {k: fn_of(k) for k in SEMANTIC}
print(f"    resolved: {{" + ", ".join(f"{k}: {'yes' if v else 'NO'}" for k, v in _nodes.items()) + "}")
gate("Ⓓ① all three property tests exist by name in the syntax trees of the receipts that carry "
     "them -- the semantic forms are runnable code in this prefix, not a proposal",
     all(v is not None for v in _nodes.values()))

_touch = {}
for k, n in _nodes.items():
    if n is None:
        continue
    _touch[k] = sorted({x.id for x in ast.walk(n) if isinstance(x, ast.Name)} & PAPERVARS)
print(f"    paper variables named inside them: {_touch}")
gate("Ⓓ② none of the three names any variable its receipt binds PAPER TEXT to, so none of them "
     "reads prose at all -- which is why no rewording can red them",
     all(v == [] for v in _touch.values()))

_prose = {}
for k, n in _nodes.items():
    if n is None:
        continue
    consts = [c.value for c in ast.walk(n) if isinstance(c, ast.Constant) and isinstance(c.value, str)]
    doc = ast.get_docstring(n) or ''
    _prose[k] = [c for c in consts if c != doc and not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', c)]
print(f"    non-identifier string constants (docstring excluded): {_prose}")
gate("Ⓓ③ every string any of the three compares against is a PYTHON IDENTIFIER -- a function name, "
     "an argument, an attribute, a guard flag -- so there is no text in them for a rewording to "
     "move, and wiring any of them the other way reds the gate",
     all(v == [] for v in _prose.values()))

_computable = [r for r in ROWS if r[SUB] in COMPUTABLE]
_n = len(_computable)
print(f"    the computable class: {_n} rows -- "
      f"{sum(1 for r in _computable if r[SUB] == 'AST-REPLACED')} carried by an AST property test "
      f"written this cycle, {sum(1 for r in _computable if r[SUB] == 'COMPUTED-ELSEWHERE')} by the "
      f"81-component Riemann computation this seat wrote at cc66.166")
print(f"    pre-registered band {PRE_COMPUTABLE[0]}-{PRE_COMPUTABLE[1]}; measured {_n}")
gate(f"Ⓓ④ the computable class is inside the band this cycle pinned BEFORE performing anything",
     PRE_COMPUTABLE[0] <= _n <= PRE_COMPUTABLE[1])
gate("Ⓓ⑤ and it sits ON the band's top edge, which is declared as a band that was nearly wrong "
     "rather than a prediction that was right -- C67's correction, applied to this cycle's own "
     "pre-registration",
     _n == PRE_COMPUTABLE[1])

# ============================================================================ E
head("E -- LIMB TWO IS DEFEATED ON THE CLAUSE'S OWN EXEMPLAR")

_ns = CR15.count(EXEMPLAR_SHORT)
_nl = CR15.count(EXEMPLAR_LONG)
print(f"    in CR_cosmology.tex: the SHORT form occurs {_ns} time(s), the pinned LONG form {_nl}")
gate("Ⓔ① the shortening limb two licenses turns a SINGLE-site pin into a MULTI-site one on the very "
     "row r7255 cites as the clause's exemplar: the short form occurs more often than the long one, "
     "and more than once",
     _ns >= 2 and _ns > _nl and _nl >= 1)

_kern = sorted(glob.glob(os.path.join(PREFIX, 'P15_the_kernels_distance*.py')))
_ktree = ast.parse(open(_kern[0], encoding='utf-8').read()) if len(_kern) == 1 else None
_anchor_names = set()
if _ktree is not None:
    _anchor_names = {t.id for n in ast.walk(_ktree) if isinstance(n, ast.Assign)
                     for t in n.targets if isinstance(t, ast.Name)}
_parts = sum(1 for n in ast.walk(_ktree) if isinstance(n, ast.Attribute) and n.attr == 'partition') \
    if _ktree is not None else 0
_has_anchor = {'_DMDC', '_WHY'} <= _anchor_names
print(f"    the exemplar's receipt binds both anchor names: {_has_anchor}; "
      f"str.partition used {_parts} time(s)")
gate("Ⓔ② so that row was repaired by an ANCHORED SLICE and not by a bare shortening -- the window "
     "is cut with str.partition, which the operator does NOT key, where an `in` guard would have "
     "minted a new pin inside the repair meant to remove one",
     _has_anchor and _parts >= 1)

# ============================================================================ F
head("F -- THE WIDTH RE-CUT HAS TWO STRENGTHS, AND THE WEAKER IS REPORTED AS WEAKER")

_sym = [r for r in ROWS if r[SUB] == 'SYMBOL-ANCHOR']
_pro = [r for r in ROWS if r[SUB] == 'PROSE-ANCHOR']
print(f"    {len(_sym)} SYMBOL-anchored (fully reword-immune), "
      f"{len(_pro)} PROSE-anchored (exposure reduced, not removed)")
gate("Ⓕ① the width re-cut splits 4 / 3 by what anchors it, and the split is recorded per row rather "
     "than claimed for the family",
     len(_sym) == SUBFORMS['SYMBOL-ANCHOR'] and len(_pro) == SUBFORMS['PROSE-ANCHOR']
     and len(_sym) + len(_pro) == FORMS['RECUT'])

_occ = {d: TEX.count(d) for d in BARE_DIGITS}
print(f"    bare-digit occurrences in the papers: {_occ}")
gate("Ⓕ② and the pairing is NOT optional on the weak three: the bare digits occur more than once in "
     "the papers, so the value alone would not anchor the read at all",
     all(v >= 2 for v in _occ.values()))

_bad = []
for r in ROWS:
    if r[FORM] != 'RECUT' or r[NLIT] == '-':
        continue
    try:
        re.compile(r[NLIT].strip('"'))
    except re.error:
        _bad.append(r[OSHA])
print(f"    every re-cut replacement compiles as a regex: {not _bad}"
      + (f" (bad: {_bad})" if _bad else ""))
gate("Ⓕ③ every width re-cut replaced a quotation with a PATTERN that compiles -- the form the family "
     "is named for, checked rather than assumed",
     not _bad and sum(1 for r in ROWS if r[FORM] == 'RECUT') == FORMS['RECUT'])

# ============================================================================ G
head("G -- THE METHOD, PROVED FROM THIS RECEIPT'S OWN SYNTAX TREE")

_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_selfconsts = [c.value for c in ast.walk(_self) if isinstance(c, ast.Constant) and isinstance(c.value, str)]
# ⌗ the needle is assembled rather than written, because a literal spelling of it would appear in
#   this very list and the gate would report itself.  The first draft did exactly that.
_NEEDLE = 'quote_pin' + '_baseline'
_ledger = [c for c in _selfconsts if _NEEDLE in c]
print(f"    references to the ledger file in this receipt's own source: {len(_ledger)}")
gate("Ⓗ① THIS RECEIPT MAKES NO LIVE READ OF THE LEDGER AT ALL -- the correction instance eight of "
     "the fail-on-success class forced on cc66.171's `key identity is admissible` rule, enforced "
     "here structurally and not by intention",
     not _ledger)

# ⌗ the exclusion is checked against the DISK and not against the filtered list: asking whether the
#   filter's own output contains what the filter removes is a tautology, and this gate's whole
#   subject is that the appendices EXIST and are LEFT OUT.
_appx_on_disk = [q for q in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex')))
                 if os.path.basename(q).startswith('appendix_receipts')]
_leaked = sorted(set(_appx_on_disk) & set(_PAPERS))
print(f"    papers read: {len(_PAPERS)}; generated appendices on disk: {len(_appx_on_disk)}; "
      f"leaked into the read: {_leaked}")
gate("Ⓗ② the generated appendices EXIST and are left out of the read -- they are receipts/INDEX.md "
     "printed, so a receipt that globs them reads a RETIRED paper state as live, which is how "
     "check_receipt_tex_scope caught C67 on the first fast run after its own INDEX row landed",
     len(_appx_on_disk) >= 1 and not _leaked and len(_PAPERS) > 10)

# ============================================================================
bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks in {time.time() - t_all:.1f}s")
if bad:
    print("  GATES FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("  GATES: ALL PASS")
print(f"""
  ==========================================================================
  THE ANSWER, IN ONE PLACE:
    {OWED_AT_PREREG} of {OWED_AT_PREREG} PERFORMED.  {len(_held)} HELD.  The prefix owes nothing.
    {FORMS['DELETED']} deleted, {FORMS['SHORTEN'] + FORMS['SHORTEN+ANCHOR']} limb-two shortenings,
    {FORMS['RECUT']} width re-cuts, {FORMS['REVERDICT']} re-verdict.
  ⇒ The owed class was REDUNDANT ASSERTION: {100 * _del_frac:.1f} per cent of it was discharged by
    deleting a quotation the receipt had already computed beside.
  ⛭ r7255's REACHABLE NEGATIVE FIRES: {_n} rows are carried by a SEMANTIC form that reads no prose
    and reds on the converse, inside the pinned band {PRE_COMPUTABLE} at its top edge.
    70's negative is not refuted -- it is SCOPED, and the line is `computable`, not `string`.
  ⛔ LIMB TWO is defeated on the clause's own exemplar: the short form occurs {_ns} times against
    the long form's {_nl}, so shortening alone makes a FILE pin out of a CLAIM pin.
  ⛔ The WIDTH RE-CUT is {len(_sym)} fully immune and {len(_pro)} only reduced, and the weak three
    cannot drop their prose anchor: {_occ}.
  ==========================================================================""")
