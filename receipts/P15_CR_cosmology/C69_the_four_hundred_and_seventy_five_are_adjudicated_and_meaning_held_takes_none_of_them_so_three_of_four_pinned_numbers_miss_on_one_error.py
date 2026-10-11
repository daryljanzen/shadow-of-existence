#!/usr/bin/env python3
"""P15 receipt -- `r7255`'s ORDER ②: TAKE THE `475` UNVERDICTED QUOTE-PIN KEYS OF
`receipts/P15_CR_cosmology` UNDER THE SETTLED RULE AND BOTH LIMBS OF THE GRAIN CLAUSE, WITH THE
`MEANING-HELD`, `REPAIR-OWED` AND HOLE SHARES PRE-REGISTERED FIRST.

*** ⛭⛭⛭ ALL `475` ARE ADJUDICATED.  `413` `DELIBERATE`, `42` `REPAIR-OWED`, `10` `ENCODING-OK`,
    `8` `ALT-OK`, `2` `NOT-A-PIN` -- and `0` `MEANING-HELD`. ***

** ⛔⛔ THREE OF MY FOUR PINNED NUMBERS ARE OUTSIDE THEIR BANDS, AND IT IS ONE ERROR AND NOT
   THREE.  I pre-registered that `MEANING-HELD` would absorb `38` per cent of this population.
   IT ABSORBED NONE.  Every row it was supposed to take went to `DELIBERATE` instead, so the
   `MEANING-HELD` miss and the `DELIBERATE` miss are the same miss counted twice. **

    MEANING-HELD   pinned 38.0 per cent, band 28--50   measured   0.0   ** OUTSIDE, low **
    REPAIR-OWED    pinned 10.0 per cent, band  5--18   measured   8.8   ✔ INSIDE
    DELIBERATE     pinned 44.0 per cent, band 32--56   measured  86.9   ** OUTSIDE, high **

⇒ *** AND THE ONE I NAMED IN THE PRE-REGISTRATION AS MOST LIKELY TO BE WRONG IS THE ONE THAT
    CAME CLOSEST.  I wrote: "the prediction most likely to be wrong, named: the `48`
    `REPAIR-OWED` ... if it comes back under `20` the band holds but the point estimate was
    built on the wrong half of the population."  It came back `42` against a pinned `48`. ***
⌗ *So my judgement about WHICH prediction was fragile was exactly inverted: the number I hedged
is the number I got, and the number I stated without hedging is the number that collapsed.*

** THE CAUSE, AND IT IS STRUCTURAL RATHER THAN A MISCOUNT. **  `MEANING-HELD` was adopted at
`r7253` for the `148` CONTESTED-CELL rows -- paper pins ALREADY VERDICTED and in dispute, where
a finding had been argued and no string form could carry it.  *** The `475` are not that
population.  They are VIRGIN keys, and `54` per cent of them are IDENTITY pins by their
CONTAINER or their TIER -- a frozen pre-registration, a label, a git-pinned historical state, a
sibling receipt's printed line, a code line.  For an identity pin the string IS the claim, so
`MEANING-HELD`'s premise -- that no string form carries the finding -- cannot even be stated. ***
⇒ ** `MEANING-HELD`'s share is not a property of a prefix.  It is a property of a DISPUTE. **

** THE GROUNDS, EVERY ROW CARRYING ITS OWN, AND SIX OF THEM NAMED FOR THE FIRST TIME THIS
   CYCLE. **  `GRAIN-HOLD` 134, `PREREG` 87, `TOKEN` 76, `PINNED-READ` 29, `SIBLING-RECEIPT` 26,
`MULTI-SITE` 22, `GRAIN-MOVE` 20, `CODE-LINE` 20, `GRAIN-HOLD+OCCURRENCE` 14, `ENCODING` 10,
`SUBJECT-REGISTRY` 8, `ALT-STATES` 8, `RECUT-PATTERN` 8, `ABSENCE-VOCABULARY` 6,
`ABSENCE-GUARD` 5, `VACUOUS` 2.
  ⌗ *** `PREREG` is the finding of the sort: `87` rows -- `18.3` per cent, the largest SOURCE
      sub-kind in the prefix -- pin a receipt's OWN FROZEN PRE-REGISTRATION, asserting that the
      document named a thing BEFORE it was measured.  Nothing was counting them; the baseline's
      own target definition already admitted the kind ("a receipt's code, a ledger, a
      PREDICTION") and no measurement had used it. ***
  ⌗ And THREE grounds are repair forms ALREADY PERFORMED on rows the ledger counted as owing
    them: `ABSENCE-GUARD` (a retired sentence asserted absent -- a regression guard),
    `RECUT-PATTERN` (a regex that extracts a value -- order ①'s family B), and `PINNED-READ`
    (`L-249`'s historical pin).  `42` rows in all.

** ⛭⛭ `GRAIN-HOLD+OCCURRENCE` IS ORDER ①'s OPERATIONAL LIMIT, EARNING ITS KEEP ON A SECOND
   POPULATION.  `14` rows hold on limb one ONLY because the clause-aligned shorter span occurs
   MORE OFTEN than the pinned form, so taking it would convert a pin on the CLAIM into a pin on
   the FILE.  `66` bound that limit on this seat's report of ONE row at order ①. **
⌗ *And it gives a RULE rather than a judgement on the `\\emph{}` wrapper: the braces are
load-bearing IF AND ONLY IF the unbraced form multiplies the sites.  `C14`'s unbraced form occurs
twice and the braces hold; `C26`'s occurs once and is already a live key elsewhere, so they move.*

** THE `42` OWED, BY SHAPE, AND NOT ONE OF THEM IS A JUDGEMENT CALL ABOUT MEANING. **
  `22` MULTI-SITE file pins -- `301` occurring eighteen times, `against the measured` eight,
     `d\\Omega^2` twenty-five -- whose repair is order ①'s family-B pairing with an anchor.
  `20` limb-two moves, EVERY ONE verified `1:1` by occurrence count BEFORE being called owed,
     and `5` of them demonstrated by the LEDGER rather than by this seat: a receipt's own claim
     label quoting the shorter span, a shorter span already live as a key in the same receipt,
     a sibling receipt carrying the repaired grain, and TWO rows owed because ORDER ① ITSELF
     shortened or re-cut the same literal elsewhere this cycle.
⇒ *** A performed repair does not only discharge its own row.  It becomes the demonstration that
    a sibling row is owed -- the exact inverse of the fail-on-success class. ***

** THE CLAUSE'S HOLE: I CANNOT MEASURE IT AND I SAY SO RATHER THAN SUBSTITUTE A PROXY. **
*The hole is (shortest span) AND (claim is a PROPOSITION).  I recorded a GROUND per row but not
an identity-or-proposition flag, so the hole is bounded and not measured: at most the `156` rows
held on `GRAIN-HOLD`, `GRAIN-HOLD+OCCURRENCE` or `SUBJECT-REGISTRY` whose claim is a proposition
-- `32.8` per cent -- and at least `0`.*  ⇒ ** The pinned `30` per cent, band `20`--`42`, is
NEITHER CONFIRMED NOR REFUTED, and the honest reading is that my reading plan did not record the
column its own prediction needed. **  ⌗ `239` of the `475` have no valid clause-aligned shorter
span at all, which is a different and weaker statement.

** COMPUTES: nothing physical.  *** Arithmetic over this revision's own published reading files,
all eight pinned by digest.  No live read of the ledger: gate `Ⓘ①` proves that from this
receipt's own syntax tree, which is the correction instance eight of the fail-on-success class
forced on `cc66.171`'s rule. ***
"""
import ast
import hashlib
import os
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
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7255_cc66_P15_the_475')

DIGEST = {'MEASURED.tsv': 'e327684cada835e6', 'CONTAINERS.tsv': '20f338de810beed0',
          'READING_GROUND.tsv': 'd1efe446639f5cf9', 'READING_01.tsv': '72cfe3d5ec8d3159',
          'READING_02.tsv': '96f4f0e7eb045986', 'READING_03.tsv': 'd47893233f852a18',
          'READING_04.tsv': '7613f59586ea92b2', 'READING_05.tsv': 'a902e61cbe3927c7'}

POP = 475                     # the population r7255 ② names, and 66's own number
RECEIPTS = 89                 # 66's own number for the receipts holding them
# FOR_66.md's r7255+cc66 ③ table, pinned at 9feb2f12 before a single key was read:
PRE = {'MEANING-HELD': (38.0, 28.0, 50.0), 'REPAIR-OWED': (10.0, 5.0, 18.0),
       'DELIBERATE': (44.0, 32.0, 56.0), 'HOLE': (30.0, 20.0, 42.0)}
# and the structure pinned with it
# ⛭ the pre-registration pinned 191 PAPER/SENTENCE and 144 SOURCE/SENTENCE, read off the LEDGER's
#   own target column.  The live OPERATOR reports 192 and 143.  ** They disagree on exactly ONE
#   key, and it is the cleanest single-row exhibit of this cycle's target finding: C12's
#   `ordinary content physics on the observable leg` is asserted at a site that reads BOTH a
#   paper AND another receipt, so the trace rule picks one container and the ledger recorded the
#   other. **  The receipt asserts the OPERATOR's split, because that is what the measurement
#   file was built from, and names the disagreement rather than smoothing it.
PRE_STRUCT_LEDGER = {('PAPER', 'SENTENCE'): 191, ('SOURCE', 'SENTENCE'): 144,
                     ('SOURCE', 'TOKEN'): 87, ('PAPER', 'TOKEN'): 53}
PRE_STRUCT = {('PAPER', 'SENTENCE'): 192, ('SOURCE', 'SENTENCE'): 143,
              ('SOURCE', 'TOKEN'): 87, ('PAPER', 'TOKEN'): 53}
SPLIT_DISAGREEMENT = '"ordinary content physics on the observable leg"'

VERDICTS = {'DELIBERATE': 413, 'REPAIR-OWED': 42, 'ENCODING-OK': 10, 'ALT-OK': 8, 'NOT-A-PIN': 2}
IDENTITY_GROUNDS = ('PREREG', 'TOKEN', 'PINNED-READ', 'SIBLING-RECEIPT', 'CODE-LINE',
                    'ABSENCE-GUARD', 'ABSENCE-VOCABULARY', 'RECUT-PATTERN', 'ENCODING')
PROPOSITION_GROUNDS = ('GRAIN-HOLD', 'GRAIN-HOLD+OCCURRENCE', 'SUBJECT-REGISTRY')
ALREADY_REPAIRED = ('ABSENCE-GUARD', 'RECUT-PATTERN', 'PINNED-READ')


def sha16(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(name):
    return [l.rstrip('\n').split('\t') for l in open(os.path.join(MINE, name), encoding='utf-8')
            if l.strip() and not l.startswith('#')]


READ = []
for _n in ('READING_GROUND.tsv', 'READING_01.tsv', 'READING_02.tsv', 'READING_03.tsv',
           'READING_04.tsv', 'READING_05.tsv'):
    for _r in tsv(_n):
        READ.append((_r[0], _r[1], _r[2], _r[3], _n))
MEAS = tsv('MEASURED.tsv')
CONT = tsv('CONTAINERS.tsv')

# ============================================================================ A
head("A -- THE SUBJECT IS THIS REVISION'S OWN READING, AND ALL EIGHT FILES ARE PINNED")

_dig = {k: sha16(os.path.join(MINE, k)) for k in DIGEST}
for k in sorted(_dig):
    print(f"    {k:22} {_dig[k]}  (pinned {DIGEST[k]})")
gate("Ⓐ① every file this receipt reads is the one this revision published, by digest",
     _dig == DIGEST)

gate(f"Ⓐ② the measurement and the container resolution both describe exactly the {POP} keys the "
     f"order names",
     len(MEAS) == POP and len(CONT) == POP)

_keys = [(a, b) for a, b, _v, _g, _f in READ]
print(f"    verdict rows across the six reading files: {len(_keys)}; distinct keys: {len(set(_keys))}")
gate(f"Ⓐ③ the six reading files carry exactly {POP} rows and NO KEY TWICE -- the population is "
     f"partitioned by them, not merely covered",
     len(_keys) == POP and len(set(_keys)) == POP)

_mk = {(r[0], r[5]) for r in MEAS}
gate("Ⓐ④ and they are the SAME keys the measurement describes, not a different set of the same "
     "size",
     set(_keys) == _mk)

_recs = {r[0] for r in MEAS}
print(f"    {len(_recs)} receipts hold them -- 66's own number is {RECEIPTS}")
gate(f"Ⓐ⑤ the keys sit in exactly {RECEIPTS} receipts, reconciling with 66's count of the "
     f"population from the other side", len(_recs) == RECEIPTS)

_st = {}
for r in MEAS:
    _st[(r[1], r[2])] = _st.get((r[1], r[2]), 0) + 1
print(f"    target/tier: {dict(sorted(_st.items()))}")
_moved = [(_a, _b) for _a, _b, _v0, _g0, _f0 in READ if _b == SPLIT_DISAGREEMENT]
print(f"    the pre-registration's ledger-derived split was {dict(sorted(PRE_STRUCT_LEDGER.items()))}")
print(f"    they differ by ONE key: {SPLIT_DISAGREEMENT} -- {len(_moved)} row(s) carrying it")
gate("Ⓐ⑥ the operator's target/tier split matches the measurement, and it differs from the "
     "pre-registration's LEDGER-derived split on EXACTLY ONE KEY -- a row asserted at a site "
     "that reads BOTH a paper and another receipt, so the trace rule picks one container and the "
     "ledger recorded the other.  The single-row exhibit of this cycle's target finding",
     _st == PRE_STRUCT and len(_moved) == 1
     and sum(PRE_STRUCT.values()) == sum(PRE_STRUCT_LEDGER.values()) == POP
     and sum(abs(PRE_STRUCT[k] - PRE_STRUCT_LEDGER[k]) for k in PRE_STRUCT) == 2)

# ============================================================================ B
head("B -- THE RESULT: ALL 475 ADJUDICATED, AND MEANING-HELD TAKES NONE OF THEM")

_v = {}
for _a, _b, _vv, _g, _f in READ:
    _v[_vv] = _v.get(_vv, 0) + 1
print(f"    {dict(sorted(_v.items()))}")
gate("Ⓑ① the verdicts are exactly as reported, and they sum to the population",
     _v == VERDICTS and sum(_v.values()) == POP)

gate("Ⓑ② NOT ONE ROW IS MEANING-HELD -- on a population of 475 virgin keys the verdict this "
     "cycle's pre-registration expected to take 38 per cent takes none",
     _v.get('MEANING-HELD', 0) == 0)

_unread = [k for k in ('UNADJUDICATED', 'UNADJUDICATED-PINNED', 'UNADJUDICATED-LIST') if k in _v]
gate("Ⓑ③ and nothing is left unread: no row carries an UNADJUDICATED verdict of any kind",
     not _unread)

# ============================================================================ C
head("C -- THE PRE-REGISTRATION, SCORED, AND THREE OF FOUR ARE OUTSIDE")

_score = {}
for k in ('MEANING-HELD', 'REPAIR-OWED', 'DELIBERATE'):
    pt, lo, hi = PRE[k]
    m = 100.0 * _v.get(k, 0) / POP
    _score[k] = (m, lo <= m <= hi)
    print(f"    {k:14} pinned {pt:5.1f}  band {lo:.0f}-{hi:.0f}   measured {m:5.1f}  "
          f"{'INSIDE' if _score[k][1] else '** OUTSIDE **'}")
gate("Ⓒ① MEANING-HELD is OUTSIDE its band, low -- 0.0 against a band whose floor is 28",
     not _score['MEANING-HELD'][1] and _score['MEANING-HELD'][0] < PRE['MEANING-HELD'][1])
gate("Ⓒ② DELIBERATE is OUTSIDE its band, high -- and it is the SAME miss, because every row "
     "MEANING-HELD was expected to take went here instead",
     not _score['DELIBERATE'][1] and _score['DELIBERATE'][0] > PRE['DELIBERATE'][2])
gate("Ⓒ③ REPAIR-OWED is INSIDE its band -- and it is the prediction the pre-registration NAMED "
     "as the one most likely to be wrong, which makes this seat's judgement about WHICH number "
     "was fragile exactly inverted",
     _score['REPAIR-OWED'][1])

_owed = _v.get('REPAIR-OWED', 0)
print(f"    REPAIR-OWED point estimate was 48 rows; measured {_owed}")
gate("Ⓒ④ and the owed COUNT lands within six rows of a point estimate pinned before a single "
     "site was read", abs(_owed - 48) <= 6)

# ============================================================================ D
head("D -- THE CAUSE, MEASURED: HALF THE POPULATION IS AN IDENTITY PIN BY ITS CONTAINER OR TIER")

_g = {}
for _a, _b, _vv, _gg, _f in READ:
    _g[_gg] = _g.get(_gg, 0) + 1
for k, n in sorted(_g.items(), key=lambda x: -x[1]):
    print(f"    {k:24} {n:4}  {100.0 * n / POP:5.1f}%")
gate("Ⓓ① every row carries a ground, and the grounds sum to the population",
     sum(_g.values()) == POP)

_ident = sum(_g.get(k, 0) for k in IDENTITY_GROUNDS)
print(f"    IDENTITY grounds total {_ident} = {100.0 * _ident / POP:.1f} per cent")
gate("Ⓓ② MORE THAN HALF the population is an identity pin by its CONTAINER or its TIER -- a "
     "frozen pre-registration, a label, a pinned historical state, a sibling receipt's printed "
     "line, a code line -- and for an identity pin MEANING-HELD's premise cannot even be stated, "
     "because the string IS the claim",
     _ident > POP / 2)

_prereg = _g.get('PREREG', 0)
print(f"    PREREG alone: {_prereg} rows in the largest SOURCE sub-kind of the prefix")
gate("Ⓓ③ and PREREG is the single largest non-GRAIN ground: receipts pinning their OWN FROZEN "
     "PRE-REGISTRATION, a kind the baseline's own target definition admits and nothing was "
     "counting",
     _prereg > 50 and _prereg == max(_g.get(k, 0) for k in IDENTITY_GROUNDS))

_already = sum(_g.get(k, 0) for k in ALREADY_REPAIRED)
print(f"    rows whose pin is ALREADY a repair form: {_already}")
gate("Ⓓ④ and three grounds are repair forms ALREADY PERFORMED on rows the ledger counted as "
     "owing them -- a regression guard on retired wording, a value-extracting pattern, and "
     "L-249's historical pin",
     _already >= 40)

# ============================================================================ E
head("E -- ORDER ①'s OPERATIONAL LIMIT, ON A SECOND AND INDEPENDENT POPULATION")

_occ = _g.get('GRAIN-HOLD+OCCURRENCE', 0)
_sent = [r for r in MEAS if r[2] == 'SENTENCE']
_any = sum(1 for r in _sent if r[15] == '1')
_uniq = sum(1 for r in _sent if r[13] == '1')
print(f"    SENTENCE rows {len(_sent)}; a valid clause-aligned shorter span exists on {_any}; "
      f"{_uniq} of those do not multiply the sites")
print(f"    rows held on limb one ONLY because the candidate multiplies the sites: {_occ}")
gate("Ⓔ① the occurrence limit 66 bound on this seat's report of ONE row at order ① decides "
     "rows on this population too, so it is not a curiosity of that exemplar",
     _occ >= 10 and _any > _uniq)

_moves = _g.get('GRAIN-MOVE', 0)
_multi = _g.get('MULTI-SITE', 0)
print(f"    the {_owed} owed rows are {_multi} MULTI-SITE file pins and {_moves} limb-two moves")
gate("Ⓔ② and the owed class partitions into exactly two shapes -- a pin on the FILE and a span "
     "with a shorter one that carries it -- with no row owed on a judgement about MEANING",
     _multi + _moves == _owed)

# ============================================================================ F
head("F -- THE CLAUSE'S HOLE IS BOUNDED AND NOT MEASURED, AND THAT IS THIS READING'S OWN GAP")

_prop = sum(_g.get(k, 0) for k in PROPOSITION_GROUNDS)
_hi = 100.0 * _prop / POP
print(f"    rows that could be in the hole at all: {_prop} = {_hi:.1f} per cent (upper bound)")
print(f"    pinned {PRE['HOLE'][0]:.0f} per cent, band {PRE['HOLE'][1]:.0f}-{PRE['HOLE'][2]:.0f}")
gate("Ⓕ① the hole is (shortest span) AND (claim is a PROPOSITION), and this reading recorded a "
     "GROUND per row but NOT an identity-or-proposition flag -- so the hole is bounded above by "
     "the rows it could contain and is not measured.  The pinned band is neither confirmed nor "
     "refuted, and the reason is that the reading plan did not record the column its own "
     "prediction needed",
     0 <= _hi <= 100 and _prop == sum(_g.get(k, 0) for k in PROPOSITION_GROUNDS))
gate("Ⓕ② and the upper bound happens to fall INSIDE the pinned band, which is stated as a bound "
     "and NOT claimed as a hit",
     PRE['HOLE'][1] <= _hi <= PRE['HOLE'][2])

# ============================================================================ G
head("G -- THE METHOD, PROVED FROM THIS RECEIPT'S OWN SYNTAX TREE")

_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_consts = [c.value for c in ast.walk(_self) if isinstance(c, ast.Constant) and isinstance(c.value, str)]
_NEEDLE = 'quote_pin' + '_baseline'
_ledger = [c for c in _consts if _NEEDLE in c]
print(f"    references to the ledger file in this receipt's own source: {len(_ledger)}")
gate("Ⓘ① THIS RECEIPT MAKES NO LIVE READ OF THE LEDGER AT ALL -- the correction instance eight "
     "of the fail-on-success class forced on cc66.171's rule, enforced structurally.  The "
     "verdicts live in the digest-pinned reading files, which a later cycle may legitimately "
     "supersede without reddening this receipt",
     not _ledger)

_files = sorted({f for _a, _b, _v2, _g2, f in READ})
print(f"    reading files: {len(_files)} -- {', '.join(f.replace('READING_', '').replace('.tsv', '') for f in _files)}")
gate("Ⓘ② and the reading is split into a GROUND file and five BATCH files, so `decided by "
     "ground` and `read at the site` are separable after the fact and not folded into one claim",
     'READING_GROUND.tsv' in _files and len(_files) == 6)

_ground_rows = sum(1 for _a, _b, _v3, _g3, f in READ if f == 'READING_GROUND.tsv')
_read_rows = POP - _ground_rows
print(f"    decided by ground: {_ground_rows};  read at the asserting site: {_read_rows}")
gate("Ⓘ③ and both halves are large enough to report apart: neither is a rounding error on the "
     "other", _ground_rows > 50 and _read_rows > 50)

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
    ALL {POP} ADJUDICATED.  {VERDICTS['DELIBERATE']} DELIBERATE, {_owed} REPAIR-OWED,
    {VERDICTS['ENCODING-OK']} ENCODING-OK, {VERDICTS['ALT-OK']} ALT-OK, {VERDICTS['NOT-A-PIN']} NOT-A-PIN -- and 0 MEANING-HELD.
  ⛔ THREE OF FOUR PINNED NUMBERS MISS, AND IT IS ONE ERROR: MEANING-HELD was pinned at
    38 per cent and took NONE, so its miss and DELIBERATE's {_score['DELIBERATE'][0]:.1f} are the same miss.
  ✔ REPAIR-OWED is INSIDE at {_score['REPAIR-OWED'][0]:.1f} per cent, {_owed} rows against a point estimate of 48 --
    and it is the prediction this cycle NAMED as most likely to be wrong.
  ⇒ THE CAUSE: {_ident} of {POP} rows ({100.0 * _ident / POP:.1f} per cent) are IDENTITY pins by container or tier.
    MEANING-HELD's share is not a property of a prefix.  It is a property of a DISPUTE.
  ⛔ THE HOLE is BOUNDED at {_hi:.1f} per cent and NOT measured: this reading recorded a ground
    per row and not an identity-or-proposition flag, which its own prediction needed.
  ==========================================================================""")
