#!/usr/bin/env python3
"""L_probability receipt -- `PO-78`, the quote-pin backlog READ BY REVERSAL rather than by eye:
** of the `1,140` paper-targeted pins this instrument can read, only `279` -- ONE IN FOUR -- would go
red if the clause they quote from were turned round. **

*** ⛭⛭⛭ THE CLASS, AND WHY IT IS NEITHER OF THE TWO ALREADY READ. ***

*Two subclasses of this backlog have been read.*  `r7201+70.1` measured **`MULTI`** -- `249` keys whose
literal occurs twice or more in the file its trace names, so the pin *survives the REMOVAL of its
sentence* while any copy stands.  `S3` read **`OPEN`** in full -- `24` keys that go red on the success
of the work they cite.  ⇒ ** Both are blindnesses of the pin's SITE: they ask whether the sentence can
be taken AWAY without the pin noticing. **  *This asks the opposite question, about the pin's CONTENT:
whether the sentence can be TURNED ROUND without the pin noticing.*

⌗ *This is `r7207`'s lesson moved one layer down.  A gate that enumerates what a page HAS can verify
every one of them and never see what is MISSING.  A pin that asserts a string is PRESENT can verify its
presence on every push and never see the clause around it change sides.*

** ⓵ THE TEST ASSERTS NOTHING ABOUT THE LITERAL, WHICH IS THE WHOLE POINT. **  ⛔ *No word-list is
applied to the quoted string and no intent is guessed.*  The four transform families act on the CLAUSE
in the shipped paper -- the span the literal's own assertion occupies, cut at the marks that separate
one assertion from the next -- and whether the literal survives is then a pure substring question.  A
transform that leaves the clause unchanged is DISCARDED, and a clause no transform can move is counted
`UNFLIPPABLE` and ** NOT counted blind **: an instrument that cannot move a sentence has not shown that
a pin survives anything.

** ⓶ THE READABLE POPULATION IS `1,140` OF THE `1,489`, AND IT SPLITS THREE WAYS. **

  `DISCRIMINATING` `279` -- every available reversal of the clause destroys the literal.  ** The pin
               quotes the polarity, the quantity or the number.  It would go red.  These are the pins
               doing the job the class is named for, and they are ONE IN FOUR. **
  `REVERSAL`   `442` -- survives EVERY available reversal: negation, antonym, quantifier and numeral
               alike.  ** The clause can be turned round four independent ways and the pin sees none
               of them. **  *This is the class the pre-registration named, and `442 > 249` makes it
               the larger blindness, as predicted.*
  `REVERSAL-PARTIAL` `419` -- survives at least one reversal but not all.
  ⇒ ** `861` of `1,140` survive at least one reversal of their own clause. **

** ⓷ AND IT IS A NEW CLASS, MEASURED AND NOT ASSUMED. **  *`33%` of the reversal class is multi-site
and `67%` is not, so this is not `MULTI` renamed; the overlap with the `OPEN` flag is `0`, so it is not
`S3`'s class either.  It runs across `189` of the `256` receipts holding a paper-targeted key.*

⚠ ** AND THE TIER THIS RECEIPT WANTED TO LEAD WITH DOES NOT HOLD, SO IT IS REPORTED AS A LIMIT
   INSTEAD. **  *`341` of the readable keys sit in a clause carrying exactly ONE of the declared
   auxiliaries, and the first draft called that `the clause's only assertion` -- so that negating it
   would reverse the very proposition the literal belongs to, with nothing else for the negation to
   land on.*  ⛔ ** It does not follow, and the data says so: `the near-horizon geometry of the
   degenerate member is $\mathrm{dS}_{2}\times S^{2}$, which carries a scale of its own` carries ONE
   declared auxiliary and TWO finite verbs, `carries` being invisible to a list of auxiliaries. **
   ⇒ *An auxiliary list is not a parser, `one auxiliary` is not `one assertion`, and the honest count
   is `LONE-AUX`: one landing site in the declared set, and no claim about which proposition got
   negated.*  ⌗ ** The headline does not need it: `one in four would go red` is a count of what the
   pins quote, and needs no parse at all. **

⚠ ** THE RECALL LIMITS, COUNTED AND EXCLUDED RATHER THAN ESTIMATED -- `349` OF THE `1,489`. **
`218` keys are `ABSENT`: the literal is not an exact substring of any of the eighteen paper BODIES,
because the needle is assembled at run time, is a regex, or names an appendix rather than a paper.
`60` are `UNFLIPPABLE`.  `18` quote a cross-reference key or a label rather than a claim.  `53` are
`SATURATED` -- more than twenty sites across the bodies, which `r7201+70.1` already settled as a pin on
the FILE, and reading twenty of five hundred sites would be a verdict on a sample dressed as a verdict
on a key.  ⛔ ** None of the four is counted blind, and none is counted discriminating either: an
unmeasured key is not a clean one. **

⌗ *No verdict is filed on any receipt and no file outside this one is written.  The reversal class is
a REPAIR LIST, routed in the channel; adjudicating it is the baseline owner's call.*

⌗ *The population and the paper bodies are read at a PINNED commit, so no count below can move when a
seat adds a file -- `L-249`'s repair, with the live state asserted separately as a disjunction rather
than as a value.  No assertion on wall-clock time.*
"""
import collections
import hashlib
import json
import os
import re
import subprocess

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ** the PIN is the trunk head this revision was derived against. **
PIN = 'bdf502b0c0e04d5fbb59c9cd43b858f9d0769439'
BASELINE = 'corpus/quote_pin_baseline.tsv'
# the eighteen paper BODIES, as `mutate_assertions.PAPER_OF_DIR` names them.  ⛔ The corpus's generated
# appendix `.tex` files are NOT papers: a literal found only there is a receipt's own words echoed back.
PAPERS = ('BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
          'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator', 'range_paper',
          'canonical_time', 'dynamics_paper', 'algebroid_paper', 'boundary_paper',
          'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper', 'geometric_core_paper',
          'CR_synthesis')


def _at(rev, path):
    return subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


# ⛭⛭ THE CLAUSE, NOT THE SENTENCE.  The span the literal's own assertion occupies: cut at the marks
#    that separate one assertion from the next.  A sentence can carry three claims joined by a colon
#    and a dash, and a reversal in the third is not a reversal of the first.
CLAUSE_DELIM = re.compile(r'(?<=[.!?;:])\s+|---|\s--\s|\n\s*\n|\\item\b')
WINDOW = 1200
# ⛭ A literal occurring more than this often across the eighteen bodies is NOT half-read: it goes in
#   its own `SATURATED` bucket.  `r7201+70.1` already settled what such a key is -- a pin on the FILE
#   and not on the claim -- and reading twenty of its five hundred sites would be a verdict on a
#   sample dressed as a verdict on a key.  53 keys, 15,593 of the 18,827 located sites.
SITE_CAP = 20

# ⛭⛭ THE TRANSFORMS, CLOSED AND DECLARED HERE.  Each is a STATE THE PAPER MAY PRODUCE, which is what
#    the standing guard asks of a defence against a paper changing: enumerate the states, do not pin.
AUX = re.compile(r'\b(is|are|was|were|does|do|did|can|could|will|would|has|have|had|must|may)\b', re.I)
NEGATED = re.compile(r'\b(not|never|cannot|nor|no)\b', re.I)
UNNEG = {'cannot': 'can', 'nor': 'or', 'no': 'a'}
ANTONYM = {'absent': 'present', 'present': 'absent', 'above': 'below', 'below': 'above',
           'raises': 'lowers', 'lowers': 'raises', 'finite': 'infinite', 'infinite': 'finite',
           'inside': 'outside', 'outside': 'inside', 'more': 'less', 'less': 'more',
           'greater': 'smaller', 'smaller': 'greater', 'rises': 'falls', 'falls': 'rises',
           'same': 'different', 'different': 'same', 'open': 'closed', 'closed': 'open',
           'vanishes': 'survives', 'survives': 'vanishes', 'conserved': 'broken',
           'broken': 'conserved', 'increases': 'decreases', 'decreases': 'increases',
           'earlier': 'later', 'later': 'earlier', 'faster': 'slower', 'slower': 'faster',
           'positive': 'negative', 'negative': 'positive', 'possible': 'impossible',
           'impossible': 'possible', 'included': 'excluded', 'excluded': 'included',
           'before': 'after', 'after': 'before', 'with': 'without', 'without': 'with'}
QUANTIFIER = {'all': 'some', 'some': 'all', 'every': 'no', 'both': 'neither', 'neither': 'both',
              'always': 'sometimes', 'sometimes': 'always', 'none': 'every', 'exactly': 'at most'}
# a literal that quotes a LaTeX control sequence or a cross-reference key is not quoting a claim
# ⛔ NARROW ON PURPOSE: a cross-reference key or a label is not a claim, but a literal carrying
#    `\emph{...}` or `$\mathrm{dS}_{2}$` IS quoting the paper's content and stays in the population.
#    The first draft of this pattern matched any `name{`, which swallowed 132 keys whose quoted
#    content happened to carry a macro -- an exclusion dressed as a definition.
MARKUP = re.compile(r'\b(label|ref|cite|rcpt|eqref|autoref)\{|\b(sec|eq|tab|fig|app):')


def clause_at(text, i, j):
    """the clause containing text[i:j] -- bounded by WINDOW so one unpunctuated block cannot swallow
    a whole section"""
    lo = max(0, i - WINDOW)
    for m in CLAUSE_DELIM.finditer(text[lo:i]):
        lo = max(0, i - WINDOW) + m.end()
    hi = len(text)
    m = CLAUSE_DELIM.search(text[j:j + WINDOW])
    if m:
        hi = j + m.start()
    return text[lo:hi].strip()


def _pat(table):
    return re.compile(r'\b(' + '|'.join(sorted(table, key=len, reverse=True)) + r')\b', re.I)


ANTONYM_PAT, QUANTIFIER_PAT = _pat(ANTONYM), _pat(QUANTIFIER)


def _swap(s, table, pat):
    return pat.sub(lambda m: table.get(m.group(1).lower(), m.group(0)), s)


def reversals(c):
    """every state the declared transforms can put this clause in.  A transform that changes nothing
    is DISCARDED -- an instrument has not moved a sentence it left alone."""
    out = {}
    if NEGATED.search(c):
        out['NEG-'] = NEGATED.sub(lambda m: UNNEG.get(m.group(1).lower(), ''), c)
    else:
        m = AUX.search(c)
        if m:
            out['NEG+'] = c[:m.end()] + ' not' + c[m.end():]
    out['ANTONYM'] = _swap(c, ANTONYM, ANTONYM_PAT)
    out['QUANT'] = _swap(c, QUANTIFIER, QUANTIFIER_PAT)
    out['NUM'] = re.sub(r'\d+(\.\d+)?', lambda m: '%g' % (float(m.group(0)) + 1), c)
    return {k: v for k, v in out.items() if v != c}


def read_baseline(text):
    rows = []
    for ln in text.split('\n'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        f = ln.split('\t')
        if len(f) >= 6 and f[2] == 'PAPER':
            rows.append((f[0], json.loads(f[1]), f[3], f[4], f[5]))
    return rows


def classify(rows, bodies):
    """every key put in exactly one bucket, with the witness that put it there"""
    t = collections.Counter()
    strict, neg, rev, multi = [], [], [], set()
    for rec, lit, tier, flags, verdict in rows:
        key = (rec, lit)
        if MARKUP.search(lit):
            t['MARKUP'] += 1
            continue
        sites = []
        for p, x in bodies.items():
            k = x.find(lit)
            while k >= 0:
                sites.append((p, k, k + len(lit)))
                k = x.find(lit, k + 1)
        if not sites:
            t['ABSENT'] += 1
            continue
        if len(sites) > SITE_CAP:
            t['SATURATED'] += 1
            continue
        if len(sites) > 1:
            multi.add(key)
        moved = nmoved = smoved = 0
        all_s = n_s = s_s = True
        any_s = False
        w = nw = sw = None
        for p, i, j in sites:
            c = clause_at(bodies[p], i, j)
            if lit not in c:
                t['NO-CLAUSE'] += 1
                moved = -1
                break
            lone = len(AUX.findall(c)) == 1
            for name, fl in reversals(c).items():
                moved += 1
                held = lit in fl
                if name.startswith('NEG'):
                    nmoved += 1
                    if held:
                        nw = nw or (p, name, c, fl)
                    else:
                        n_s = False
                    if lone:
                        smoved += 1
                        if held:
                            sw = sw or (p, name, c, fl)
                        else:
                            s_s = False
                if held:
                    any_s = True
                    w = w or (p, name, c, fl)
                else:
                    all_s = False
        if moved < 0:
            continue
        if moved == 0:
            t['UNFLIPPABLE'] += 1
            continue
        if smoved and s_s:
            t['LONE-AUX'] += 1
            strict.append((rec, lit, sw, flags))
        if nmoved and n_s:
            t['NEG'] += 1
            neg.append((rec, lit, nw, flags))
        if all_s:
            t['REVERSAL'] += 1
            rev.append((rec, lit, w, flags))
        elif any_s:
            t['REVERSAL-PARTIAL'] += 1
        else:
            t['DISCRIMINATING'] += 1
    return t, strict, neg, rev, multi


# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("A. THE INSTRUMENT, SEEDED BOTH WAYS BEFORE IT IS POINTED AT ANYTHING")

SEEDS = (
    ('polarity quoted', 'the radiation is absent from the vacuum kernel',
     'is absent from the vacuum kernel', 'DISCRIMINATING'),
    ('bare noun phrase', 'the branch point is a third case for the crossing',
     'a third case', 'REVERSAL'),
    ('nothing to move', 'kernel, leg, throat', 'leg', 'UNFLIPPABLE'),
    ('numeral quoted', 'the geometric one is 13 percent below the other',
     'is 13 percent below', 'DISCRIMINATING'),
)


def seed_bucket(clause, lit):
    if lit not in clause:
        return 'NOT-PLANTED'
    fl = reversals(clause)
    if not fl:
        return 'UNFLIPPABLE'
    if any(lit not in v for v in fl.values()):
        return 'DISCRIMINATING'
    return 'REVERSAL'


for nm, cl, lt, want in SEEDS:
    got = seed_bucket(cl, lt)
    print(f"    {nm:20s} planted {lt!r:36s} -> {got}")
    gate(f"Ⓖ① the seeding discriminates: a planted clause whose case is '{nm}' lands in {want} and "
         f"not somewhere convenient ({got})", got == want)

gate(f"Ⓖ② the transform tables are CLOSED and declared in this file -- 40 antonym entries, 9 "
     f"quantifier entries, one negation rule ({len(ANTONYM)}/{len(QUANTIFIER)})",
     len(ANTONYM) == 40 and len(QUANTIFIER) == 9)
_noop = reversals('kernel, leg, throat')
gate("Ⓖ③ a transform that leaves the clause unchanged is DISCARDED rather than counted as a state "
     f"the paper may produce ({len(_noop)} survive on a clause with nothing to move)", not _noop)
_c = 'the branch point is a third case for the crossing'
gate("Ⓖ④ the negation really does reverse the planted clause, checked by reading the result rather "
     "than by trusting the rule",
     reversals(_c).get('NEG+') == 'the branch point is not a third case for the crossing')

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("B. THE POPULATION, READ AT THE PIN")

_bl = _at(PIN, BASELINE)
ROWS = read_baseline(_bl)
BODIES = {p: _at(PIN, f'corpus/{p}.tex') for p in PAPERS}
print(f"    pinned baseline            {len(_bl.splitlines())} lines, "
      f"sha256 {hashlib.sha256(_bl.encode()).hexdigest()[:12]}")
print(f"    PAPER-targeted keys        {len(ROWS)} in {len({r for r, *_ in ROWS})} receipts")
print(f"    paper bodies read          {len(BODIES)}  "
      f"({sum(len(v) for v in BODIES.values()):,} characters)")
gate(f"Ⓖ⑤ the population is the pinned baseline's PAPER-targeted keys -- 1489 of them ({len(ROWS)})",
     len(ROWS) == 1489)
gate(f"Ⓖ⑥ all eighteen paper bodies are present at the pin ({len(BODIES)})", len(BODIES) == 18)

TALLY, LONE, NEG, REV, MULTI = classify(ROWS, BODIES)
for k in ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'LONE-AUX', 'NEG', 'UNFLIPPABLE',
          'NO-CLAUSE', 'MARKUP', 'ABSENT', 'SATURATED'):
    print(f"    {k:18s} {TALLY[k]}")

_limits = TALLY['ABSENT'] + TALLY['UNFLIPPABLE'] + TALLY['MARKUP'] + TALLY['SATURATED']
_readable = TALLY['REVERSAL'] + TALLY['REVERSAL-PARTIAL'] + TALLY['DISCRIMINATING']
gate(f"Ⓖ⑦ the three verdicts PARTITION the readable population and the four limit buckets account "
     f"for the rest -- {_readable} + {_limits} = {len(ROWS)}, so no count below rests on a key "
     f"counted twice or dropped", _readable + _limits == len(ROWS) and _readable == 1140)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("C. ONE IN FOUR WOULD GO RED, AND THAT IS THE WHOLE FINDING")

gate(f"Ⓖ⑧ DISCRIMINATING -- every available reversal of the clause destroys the literal, so the pin "
     f"quotes the polarity, the quantity or the number and WOULD go red: 279 of 1140, one in four "
     f"({TALLY['DISCRIMINATING']})", TALLY['DISCRIMINATING'] == 279)
gate(f"Ⓖ⑨ REVERSAL -- survives EVERY available reversal: 442 keys ({TALLY['REVERSAL']})",
     TALLY['REVERSAL'] == 442)
gate(f"Ⓖ⑩ and 861 of the 1140 survive AT LEAST ONE reversal of their own clause "
     f"({TALLY['REVERSAL'] + TALLY['REVERSAL-PARTIAL']})",
     TALLY['REVERSAL'] + TALLY['REVERSAL-PARTIAL'] == 861)
gate("Ⓖ⑪ so the instrument SEPARATES the population rather than flagging it -- all three verdicts "
     "are populated and none is the whole",
     0 < TALLY['DISCRIMINATING'] < _readable and 0 < TALLY['REVERSAL'] < _readable
     and 0 < TALLY['REVERSAL-PARTIAL'] < _readable)

# ⛭⛭ THE TIER THIS RECEIPT WANTED TO LEAD WITH, AND THE READING THAT TOOK IT AWAY.
_lone_claim = ('the near-horizon geometry of the degenerate member is $\\mathrm{dS}_{2}\\times S^{2}$, '
               'which carries a scale of its own')
gate(f"Ⓖ⑫ LONE-AUX is reported as a landing-site count and NOT as `the clause's only assertion`: a "
     f"real clause in BH_causality_v2 carries ONE declared auxiliary and TWO finite verbs, `carries` "
     f"being invisible to a list of auxiliaries, so one auxiliary is not one assertion "
     f"({len(AUX.findall(_lone_claim))} auxiliary in it)", len(AUX.findall(_lone_claim)) == 1)
gate(f"Ⓖ⑬ and the headline does not rest on it -- `one in four would go red` is a count of what the "
     f"pins QUOTE and needs no parse: {TALLY['DISCRIMINATING']} of {_readable} is measured with the "
     f"auxiliary list used only to MOVE a clause, never to parse one",
     TALLY['LONE-AUX'] == 341 and TALLY['DISCRIMINATING'] == 279)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("D. EVERY REVERSAL VERDICT CARRIES THE REVERSED CLAUSE IT SURVIVES")

gate(f"Ⓖ⑭ every one of the {len(REV)} reversal verdicts exhibits a reversed clause that CHANGED and "
     f"still contains the literal -- the verdict is a demonstration, not an inference",
     all(w and lit in w[3] and w[2] != w[3] for _, lit, w, _ in REV))


def window(a, b, lit, span=58):
    """show the clause round the point the transform CHANGED it, and not the first 150 characters --
    the first draft printed the head of a long clause, where two of four witnesses showed no visible
    difference at all and the exhibit proved nothing by eye"""
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), 0)
    lo = max(0, i - span)
    return (('...' if lo else '') + a[lo:i + span].replace('\n', ' '),
            ('...' if lo else '') + b[lo:i + span].replace('\n', ' '))


for rec, lit, w, flags in REV[:4]:
    before, after = window(w[2], w[3], lit)
    print(f"\n    {os.path.basename(rec)[:70]}")
    print(f"      pins    {lit!r}")
    print(f"      clause  {before!r}   ({w[0]})")
    print(f"      {w[1]:7s} {after!r}")
    print("      ⇒ the clause now says something the paper does not, and the pin is still green")

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("E. IT IS A NEW CLASS, AND THAT IS MEASURED")

_r = {(r, l) for r, l, _, _ in REV}
_ov = len(_r & MULTI)
_open = sum(1 for r, l, w, f in REV if 'OPEN' in f)
print(f"    multi-site keys              {len(MULTI)}")
print(f"    REVERSAL that are multi-site {_ov}  ({100 * _ov / len(_r):.0f}% of REVERSAL)")
print(f"    REVERSAL carrying OPEN       {_open}")
print(f"    receipts holding one         {len({r for r, l, w, f in REV})} of "
      f"{len({r for r, *_ in ROWS})}")
gate(f"Ⓖ⑮ REVERSAL is not MULTI renamed -- {100 * _ov / len(_r):.0f}% of it is multi-site, far under "
     f"the 90% the pre-registration set as the refuting overlap", _ov < 0.90 * len(_r))
gate(f"Ⓖ⑯ REVERSAL is not S3's class either -- 0 of it carries the OPEN flag ({_open})", _open == 0)
gate(f"Ⓖ⑰ and it is the LARGER blindness, as pre-registered: 442 against MULTI's 249 "
     f"({TALLY['REVERSAL']} > 249)", TALLY['REVERSAL'] > 249)
gate(f"Ⓖ⑱ and it is not one receipt's habit -- it runs across 189 of the 256 receipts holding a "
     f"paper-targeted key ({len({r for r, l, w, f in REV})})",
     len({r for r, l, w, f in REV}) == 189)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("F. THE LIMITS, COUNTED AND EXCLUDED RATHER THAN ESTIMATED")

print(f"    ABSENT       {TALLY['ABSENT']:4d}  literal not an exact substring of any paper BODY -- a "
      f"needle built at run time, a regex, or an appendix target")
print(f"    UNFLIPPABLE  {TALLY['UNFLIPPABLE']:4d}  no declared transform moves the clause")
print(f"    MARKUP       {TALLY['MARKUP']:4d}  the literal quotes a reference key or a label, not a claim")
print(f"    SATURATED    {TALLY['SATURATED']:4d}  more than {SITE_CAP} sites -- already a pin on the FILE "
      f"by r7201's measure, and not half-read here")
gate(f"Ⓖ⑲ the four limit buckets are EXCLUDED from the verdicts rather than absorbed by them, so "
     f"every fraction above is of 1140 and not of 1489 ({_limits} limited)",
     _limits == 349 and _readable == 1140)
gate("Ⓖ⑳ UNFLIPPABLE in particular is NOT reported blind -- the instrument that cannot move a "
     f"sentence has not shown that a pin survives anything ({TALLY['UNFLIPPABLE']} of them)",
     TALLY['UNFLIPPABLE'] > 0)

# ⛭ THE LIVE STATE, AS A DISJUNCTION AND NOT AS A VALUE.  `L-249`'s repair, and the recorded lesson
#   applied rather than quoted: never re-run a measurement for reassurance, only on a tree that
#   actually changed.  Identical input IS the same measurement, and saying so is the stronger claim.
_live_bl = open(os.path.join(ROOT, BASELINE), encoding='utf-8').read()
_live_rows = read_baseline(_live_bl)
_live_bodies = {p: open(os.path.join(ROOT, 'corpus', f'{p}.tex'), encoding='utf-8').read()
                for p in PAPERS}
_same = _live_bl == _bl and _live_bodies == BODIES
_lt = TALLY if _same else classify(_live_rows, _live_bodies)[0]
print(f"\n    live PAPER keys {len(_live_rows)}   byte-identical to the pin: {_same}   "
      f"live REVERSAL {_lt['REVERSAL']}   live DISCRIMINATING {_lt['DISCRIMINATING']}")
gate(f"Ⓖ㉑ the live state as a DISJUNCTION, which the standing guard prefers to a pin: EITHER the "
     f"live tree is byte-identical to the pin, so the pinned measurement IS the live one, OR it is "
     f"re-run and the reversal class still exceeds MULTI's 249 (identical={_same}, live "
     f"reversal={_lt['REVERSAL']})", _same or _lt['REVERSAL'] > 249)
gate(f"Ⓖ㉒ and on whichever of the two it was, the instrument still clears pins as well as flagging "
     f"them ({_lt['DISCRIMINATING']} discriminating)", _lt['DISCRIMINATING'] > 0)

_after = hashlib.sha256(_at(PIN, BASELINE).encode()).hexdigest()
gate(f"Ⓖ㉓ the pinned baseline this receipt reads is byte-identical after the run -- checked by "
     f"digest, so nothing here edited the population it measured ({_after[:12]})",
     _after == hashlib.sha256(_bl.encode()).hexdigest())

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print("""
  THE QUOTE-PIN BACKLOG IS READ BY REVERSAL, AND ONLY ONE IN FOUR OF THE PAPER-TARGETED PINS WOULD
  NOTICE.  Of the 1,140 keys this instrument can read, 279 quote the polarity, the quantity or the
  number and would go red if their clause were turned round; 861 survive at least one reversal and
  442 survive all four, each of the 442 exhibiting the reversed clause it stays green on rather
  than being inferred from the literal's shape.  The class is new: 33% of it is multi-site, so it
  is not r7201's MULTI renamed; none of it carries the OPEN flag, so it is not S3's; 442 against
  MULTI's 249 makes it the larger blindness, as pre-registered; and it runs across 189 of the 256
  receipts holding a paper-targeted key.  AND THE TIER THIS RECEIPT WANTED TO LEAD WITH IS REPORTED
  AS A LIMIT: 341 keys sit in a clause with exactly one declared auxiliary, and the first draft
  called that the clause's only assertion -- but a real clause in BH_causality_v2 carries one
  auxiliary and two finite verbs, so an auxiliary list is not a parser and one auxiliary is not one
  assertion.  The headline never needed it.  349 keys are excluded and counted -- 218 ABSENT, 60
  UNFLIPPABLE, 18 quoting a reference key, 53 SATURATED -- because an unmeasured key is not a clean
  one.  No verdict is filed on any receipt and nothing outside this file is written: the reversal
  set is a repair list, routed in the channel, and adjudicating it belongs to the baseline's
  owner.""")
raise SystemExit(1 if _bad else 0)
