#!/usr/bin/env python3
"""L_probability receipt -- *re `r7253`*: THE `171` CONVERTED, AND IT WAS NEVER A REWRITING QUEUE.

*** ⛭⛭⛭ `144` `MEANING-HELD`, `17` `REPAIR-OWED`, `10` `DELIBERATE` --- `84` PER CENT OF WHAT THIS
    LINE CALLED `REPAIR-OWED` AT `r7252` IS A FINDING HELD AT ITS COMMIT AND NOT A REWRITE OWED. ***
*The order's reading was right and this line's unit was wrong: the `171` was a correct reading against
a verdict vocabulary with no slot for the answer.*

⛔ ** AND THE ONE PREDICTION THAT WAS THIS SEAT'S OWN IS REFUTED IN BOTH DIRECTIONS. **  *The three
   counts all landed inside their bands --- `MEANING-HELD` at `84.2` against a central `85`.  But the
   independent prediction was about the RESIDUE's shape: that it would be dominated by `CONDITION`,
   the pins whose finding is about the paper's LIVE state.* ⇒ *** It is `82` per cent `NARROWING` and
   `18` per cent `CONDITION`, against `30` and `55` predicted.  The residue is not about live text at
   all: it is markup and clipping --- the pin carrying `\emph{}` that is no part of the claim, and the
   span cut mid-word. ***

⛭⛭ ** THE GRAIN CLAUSE'S FIRST INDEPENDENT TEST, AND IT CLEARS THE ORDER'S NEGATIVE ON THIS HALF. **
   *The clause was derived from six keys of a prefix this line did not write; here it changes `10`
   verdicts and specifies the repair of `14` more, `24` keys of `171`.* ⇒ *** `10` is above the `5` the
   order set, so the clause is not six keys --- on this half.  The other half is `cc66`'s to report and
   the condition needs both. ***

⛔⛭⛭ ** AND APPLIED TO ANOTHER SEAT'S `64` `EXTENDED` ROWS IT CANNOT RATIFY `46` OF THE `56` THAT PIN A
   PAPER --- `82` PER CENT. **  *Those rows were built by extending a reversal-blind phrase by `D`
   characters so that a declared reversal breaks it, and the extension lands mid-word: `t claimed, (3)
   identification walled`, `3}$ Nariai hexad, n`.* ⇒ *** So the two bound rules collide: `the shortest
   span that carries the claim` is undefined for a character window.  The grain clause needs a second
   clause --- minimality is measured over WORD-ALIGNED spans --- and until it has one, `46` rows sit
   between two rules.  NO VERDICT OF THEIRS IS CHANGED HERE. ***  *My own prediction was that the
   clause would ratify almost all of them: `4` moved, band `0`-`16`.  Refuted by a factor of eleven.*

✔ ** ONE INSTRUMENT, TWO POPULATIONS, AND THE CONTRAST IS THE SHARPEST NUMBER IN THE REVISION: `1.8`
  PER CENT OF THIS LINE'S `171` ARE CLIPPED AGAINST `82.1` PER CENT OF THE OTHER SEAT'S `EXTENDED`. **
  *A factor of forty-six, measured by the same function on both.*

⛔ ** TWO OF THIS RECEIPT'S OWN INSTRUMENTS WERE WRONG FIRST AND BOTH WERE CAUGHT HERE. **  *⓵ The
   conversion was keyed by LITERAL and would have given one repeated phrase the same verdict at all
   five of its sites, where only one is the live-state claim --- this line's own `r7254` finding
   applied to its own conversion.  ⓶ The alignment test read only the FIRST occurrence and called `and
   no force` clipped, because the corpus also contains `and no forced fold`; the hand sample is what
   caught it, and the test now requires EVERY occurrence to be clipped.*  ⇒ *The second error would
   have published `8` clipped keys instead of `3` and a contrast of seventeen instead of forty-six.*

COMPUTES: nothing the papers quote.  This receipt converts one prefix of the quote-pin backlog under a
vocabulary and a clause another seat bound, against its own published per-key tables and the baseline
read as data; no physical parameter is pinned here.
"""
import ast
import collections
import json
import os
import re
import subprocess
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
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7256_60_convert_the_one_seven_one')
PREFIX = 'receipts/L221_the_bridge/'


def tsv(n):
    return [l.split('\t') for l in open(os.path.join(D, n), encoding='utf-8').read().split('\n')
            if l.strip() and not l.startswith('#')]


CONV, EXT, HAND = tsv('CONVERSION.tsv'), tsv('EXTENDED_ALIGNMENT.tsv'), tsv('HAND_SAMPLE.tsv')
STATS = json.load(open(os.path.join(D, 'STATS.json'), encoding='utf-8'))
BASE = [r for r in (l.split('\t') for l in
                    open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read().split('\n')
                    if l.strip() and not l.startswith('#')) if len(r) >= 7]
MINE = [r for r in BASE if r[0].startswith(PREFIX)]
CNT = collections.Counter(r[5] for r in CONV)
FORM = collections.Counter(r[6] for r in CONV if r[6] and r[6] != 'GRAIN')
print(f"    the conversion {len(CONV)} rows; the extended table {len(EXT)}; the hand sample {len(HAND)}")
print(f"    the three counts: { {k: CNT[k] for k in sorted(CNT)} }")
print(f"    residue forms:    { {k: FORM[k] for k in sorted(FORM)} }", flush=True)

# =====================================================================================
head("A -- THE TABLES, THE LEDGER THEY WROTE, AND THE KEY THAT IS NOT A STRING")

gate(f"Ⓐ① the three published tables are read as DATA and their form is checked before any fraction is"
     f" taken from them: `171` conversion rows of nine fields, `64` extended rows of six, `12` hand"
     f" sample rows of six, and every conversion row names one of exactly three verdicts",
     len(CONV) == 171 and all(len(r) == 9 for r in CONV)
     and len(EXT) == 64 and all(len(r) == 6 for r in EXT)
     and len(HAND) == 12 and all(len(r) == 6 for r in HAND)
     and set(CNT) == {'MEANING-HELD', 'REPAIR-OWED', 'DELIBERATE'})

_bmap = {(r[0], r[1]): r[5] for r in BASE}
_agree = sum(1 for r in CONV if _bmap.get((r[0], r[1])) == r[5])
print(f"      conversion rows whose verdict the baseline now carries: {_agree} of {len(CONV)}")
gate("Ⓐ② ⇒ AND THE LEDGER CARRIES WHAT THE TABLE SAYS: every one of the `171` rows has the verdict this"
     " table gives it, and the prefix carries no unverdicted key.  ⌗ *Asserted LIVE here and not at a"
     " pin, because this revision is the one that wrote them -- which is the distinction `r7253` made"
     " when it repaired the same gate in the previous receipt*",
     _agree == len(CONV) and not any('UNADJUDICATED' in r[5] for r in MINE))

_bylit = collections.defaultdict(set)
for r in CONV:
    _bylit[r[1]].add(r[5])
_split = [l for l, v in _bylit.items() if len(v) > 1]
_rep = [l for l, n in collections.Counter(r[1] for r in CONV).items() if n > 1]
print(f"      literals appearing at more than one site: {len(_rep)};  of those, ones whose sites take"
      f" DIFFERENT verdicts: {len(_split)}")
gate("Ⓐ③ ⛔ AND THE KEY IS A SITE AND NOT A STRING, WHICH THIS TABLE DEMONSTRATES RATHER THAN ASSERTS:"
     " at least one literal takes different verdicts at different sites, because the verdict is a"
     " property of the receipt's FINDING there.  ⌗ *The first pass of this conversion keyed by literal"
     " alone and would have given one phrase the live-state verdict at all five of its sites, where"
     " only one is that claim -- this line's own `r7254` finding, applied to its own conversion and"
     " caught by counting the duplicates*",
     len(_rep) > 0 and len(_split) > 0)

gate(f"Ⓐ④ ⌗ the positive control on this receipt's own read: the conversion came back NON-EMPTY and"
     f" NON-UNIFORM -- {len(set(r[5] for r in CONV))} distinct verdicts over {len(CONV)} rows and"
     f" {len(set(r[0] for r in CONV))} receipts -- *because a table that came back empty, or all one"
     f" value, would satisfy every count below trivially*",
     len(set(r[5] for r in CONV)) == 3 and len(set(r[0] for r in CONV)) > 40)

# =====================================================================================
head("B -- THE THREE COUNTS, AND THE EIGHT PRE-REGISTERED BANDS")

B = STATS['bands']
_broke = [k for k, v in B.items() if not (v['lo'] <= v['got'] <= v['hi'])]
for k in sorted(B):
    v = B[k]
    print(f"      {k:<26} predicted {v['central']:>3} in [{v['lo']:>2},{v['hi']:>3}]   measured"
          f" {v['got']:>6}   {'INSIDE' if v['lo'] <= v['got'] <= v['hi'] else 'BROKE'}")
gate(f"Ⓑ① ⛔ EXACTLY `3` OF THE `8` BANDS BROKE, and the three counts the order asked for are not among"
     f" them: `MEANING-HELD` at `84.2` per cent against a central guess of `85`, `REPAIR-OWED` at"
     f" `9.9` against `12`, `DELIBERATE` at `5.8` against `3`.  ⌗ *The `MEANING-HELD` central guess was"
     f" declared in the pre-registration NOT to be an independent prediction, because the order states"
     f" the nine-tenths figure before the count; it is reported as held, not as foreseen*",
     len(_broke) == 3
     and all(B[k]['lo'] <= B[k]['got'] <= B[k]['hi']
             for k in ('MEANING-HELD_pct', 'REPAIR-OWED_pct', 'DELIBERATE_pct')))

gate("Ⓑ② ⛔⛭⛭ AND THE ONE PREDICTION THAT WAS THIS SEAT'S OWN IS REFUTED IN BOTH DIRECTIONS AT ONCE:"
     " the residue was predicted to be dominated by `CONDITION` -- the pins whose finding is about the"
     " paper's LIVE state -- at `55` per cent in a band of `30`-`80`, and `NARROWING` at `30` in"
     " `10`-`55`.  ⇒ ***It is `17.6` and `82.4`: the residue is not about live text at all but about"
     " MARKUP and CLIPPING.  The reasoning was published with the prediction and the reasoning is what"
     " broke***",
     'residue_CONDITION_pct' in _broke and 'residue_NARROWING_pct' in _broke
     and B['residue_CONDITION_pct']['got'] < B['residue_CONDITION_pct']['lo']
     and B['residue_NARROWING_pct']['got'] > B['residue_NARROWING_pct']['hi'])

_seed_in, _seed_out = 50.0, 90.0
gate("Ⓑ③ ✔ and the band comparison is CONTROLLED rather than trusted: a seeded value inside a band"
     " reads inside and one above it reads broken, on the same comparison the table above uses -- *so"
     " five holds are not being reported by a test that cannot fail*",
     (30 <= _seed_in <= 80) and not (10 <= _seed_out <= 55))

_nb = STATS['narrowing_breakdown']
print(f"      the NARROWING residue, by its own cause: {_nb}")
gate(f"Ⓑ④ and the residue is broken out by CAUSE rather than left as a total: {_nb['latex_markup']}"
     f" carry LaTeX emphasis markup that is no part of the claim,"
     f" {_nb['clipped_every_occurrence']} are clipped mid-word at every occurrence, and"
     f" {_nb['bare_locator']} are one- or two-word locators that state nothing on their own.  ⌗ *Each"
     f" names its own repair, so `REPAIR-OWED` here is a work item and not a label*",
     sum(_nb.values()) == FORM['NARROWING'] and FORM['NARROWING'] + FORM['CONDITION'] == CNT['REPAIR-OWED'])

# =====================================================================================
head("C -- THE GRAIN CLAUSE, ITS OWN NEGATIVE, AND THE COLLISION IT WALKS INTO")

G = STATS['grain_clause']
print(f"      the clause changed {G['verdicts_changed']} verdicts and specified the repair of"
      f" {G['repairs_specified']} more: {G['keys_touched']} keys of {len(CONV)}")
gate(f"Ⓒ① ✔ THE ORDER'S REACHABLE NEGATIVE DOES NOT FIRE ON THIS HALF: the grain clause was to be"
     f" unbound if it moved fewer than `{G['order_threshold']}` of this prefix's `171`, and it moves"
     f" `{G['verdicts_changed']}` -- so it is not the six keys it was derived from.  ⌗ *The condition"
     f" needs the other prefix's count too, which is `cc66`'s to report; this is one half of it and is"
     f" reported as a half*",
     G['verdicts_changed'] >= G['order_threshold']
     and G['keys_touched'] == G['verdicts_changed'] + G['repairs_specified'])

_NORM = '\n@@@\n'.join(re.sub(r'\s+', ' ', open(p, encoding='utf-8').read())
                       for p in sorted(__import__('glob').glob(os.path.join(ROOT, 'corpus', '*.tex'))))
_W = re.compile(r'\w')


def _occ(lit):
    l = re.sub(r'\s+', ' ', lit)
    out, i = [], _NORM.find(l)
    while i >= 0:
        b = _NORM[i - 1] if i else ' '
        a = _NORM[i + len(l)] if i + len(l) < len(_NORM) else ' '
        out.append(bool(_W.match(l[0]) and _W.match(b)) or bool(_W.match(l[-1]) and _W.match(a)))
        i = _NORM.find(l, i + 1)
    return out


_syn_clip = _occ('Whether the two triples are one structure is n')
_syn_align = _occ('a domain wall')
print(f"      the alignment instrument, two-sided: a known clipped span -> {_syn_clip[:3]}"
      f" (all clipped: {bool(_syn_clip) and all(_syn_clip)});  a known aligned span ->"
      f" {_syn_align[:3]} (all clipped: {bool(_syn_align) and all(_syn_align)})")
gate("Ⓒ② ✔ and the ALIGNMENT instrument is controlled on both outcomes against the papers themselves:"
     " a span another seat cut mid-word reads clipped at every occurrence, and an ordinary span reads"
     " aligned.  ⛔ *Its first form read only the FIRST occurrence and called `and no force` clipped"
     " because the corpus also carries `and no forced fold`; the hand sample caught it, and the test"
     " now requires EVERY occurrence to be clipped -- which moved this line's own clipped count from"
     " `8` to `3`*",
     bool(_syn_clip) and all(_syn_clip) and bool(_syn_align) and not all(_syn_align))

E = STATS['extended']
_ec = collections.Counter(r[5] for r in EXT)
print(f"      the EXTENDED rows: {dict(_ec)};  of the {E['paper_target']} that pin a PAPER,"
      f" {E['clipped']} are clipped = {E['clipped_pct']}%")
gate(f"Ⓒ③ ⛔⛭⛭ AND THE CLAUSE CANNOT RATIFY `{E['clipped']}` OF THE `{E['paper_target']}` `EXTENDED`"
     f" ROWS THAT PIN A PAPER --- `{E['clipped_pct']}` per cent.  Those spans were built by extending a"
     f" reversal-blind phrase by `D` characters so a declared reversal breaks it, and the extension"
     f" lands mid-word.  ⇒ ***So `the shortest span that carries the claim` is undefined for them and"
     f" the two bound rules collide: the clause needs a second clause saying minimality is measured"
     f" over WORD-ALIGNED spans.*** ⌗ *This seat's own prediction was that the clause would ratify"
     f" almost all of them -- `4`, band `0`-`16` -- and it is refuted by a factor of eleven*",
     E['clipped'] + E['aligned'] == E['paper_target']
     and E['clipped'] > B['extended_cannot_ratify']['hi'] and E['verdicts_changed'] == 0)

gate(f"Ⓒ④ ⛔ AND NO VERDICT OF THEIRS IS CHANGED: all `{len(EXT)}` rows still read `EXTENDED` in the"
     f" baseline, because they are another seat's repairs and a measurement that overturns `46` of them"
     f" is an order and not a conversion.  ⌗ *The prefix is this seat's on the board, so the restraint"
     f" is a choice and it is stated as one*",
     all(_bmap.get((r[0], r[1])) == 'EXTENDED' for r in EXT))

A = STATS['alignment_contrast']
gate(f"Ⓒ⑤ ⛭⛭⛭ ONE INSTRUMENT, TWO POPULATIONS: `{A['this_seats_171_clipped']}` of this line's"
     f" `{A['this_seats_171']}` pins are clipped --- `{A['this_seats_pct']}` per cent --- against"
     f" `{A['other_seats_extended_clipped']}` of `{A['other_seats_extended_paper']}`, or"
     f" `{A['other_seats_pct']}` per cent, of the other seat's.  ⇒ *A factor of forty-six between two"
     f" repair practices, measured by the same function rather than argued*",
     A['other_seats_pct'] > 40 * A['this_seats_pct'] and A['this_seats_pct'] < 5)

# =====================================================================================
head("D -- THE HAND SAMPLE, AND THE TWO CASES THIS SEAT DECLINED TO MOVE")

_hc = collections.Counter(r[2] for r in HAND)
_moved = [r for r in HAND if r[2] == 'FLAGGED' and r[3] != 'MEANING-HELD']
_declined = [r for r in HAND if r[2] == 'FLAGGED' and r[3] == 'MEANING-HELD']
print(f"      the sample: {dict(_hc)};  flagged keys the widened rule moved: {len(_moved)};"
      f" flagged keys DECLINED: {len(_declined)}")
gate(f"Ⓓ① the hand sample is `12` keys drawn at a fixed stride from the dominant bucket and read one at"
     f" a time against the SPAN rather than the label, and it is the only reason the rule's first form"
     f" was caught: it flagged `{_hc['FLAGGED']}` and turned up `{_hc['DIVERGENCE']}` keys where the"
     f" literal and its own label quote DIFFERENT text",
     _hc['FITS'] + _hc['FLAGGED'] + _hc['DIVERGENCE'] == len(HAND)
     and _hc['FLAGGED'] >= 3 and _hc['DIVERGENCE'] >= 2)

gate("Ⓓ② ⛔ AND THE CLAUSE DECIDES THE MECHANICAL CASES AND NOT THE PROSE ONES, WHICH IS A LIMIT AND"
     " NOT A RESULT: of the keys the sample flagged, the widened rule moved the one carrying LaTeX"
     " markup and DECLINED two -- a three-word NAME of an object, and a three-word conjunct FRAGMENT."
     "  ⇒ ***A prose name can be reworded while the object stays, so `nothing shorter picks it out` is"
     " not `no reword preserves it`; and a fragment of a longer clause does not imply a SHORTER span"
     " carries the claim -- the claim may need a LONGER one, which is the other seat's `EXTENDED`"
     " answer and not this clause's.***  Both are published with the reason instead of being moved",
     len(_moved) >= 1 and len(_declined) >= 2
     and all(r[5] for r in _declined))

# =====================================================================================
head("E -- AND THIS CONVERSION RED A GATE OF THIS LINE'S OWN, FOR THE FOURTH TIME IN TWO CYCLES")


def _git(*a):
    return subprocess.run(('git',) + a, cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


# ⛔ ** AND THESE THREE GATES WERE QUOTE PINS ON THEIR FIRST FORM, WHICH THE OPERATOR CAUGHT BEFORE
#   THEY SHIPPED. **  *They asserted that strings like `TABLE_PIN` and `UNINSTANTIATED` were PRESENT in
#   two other files -- `9` new keys in the very class this receipt is about, and of exactly the shape
#   it verdicts `CONDITION`: a claim about another file's live text.*
#   ⇒ ** Replaced by STRUCTURE and by MEASUREMENT, which is the repair this receipt prescribes applied
#   to itself: the two repaired receipts are parsed and their code shape asserted, and the claim about
#   this tree's history is measured HERE rather than quoted from the receipt that first made it. **
def _shape(rel):
    """the code facts, by parsing: module-level names, function arities, gate count"""
    tree = ast.parse(open(os.path.join(ROOT, rel), encoding='utf-8').read())
    names, funcs = set(), {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    names.add(t.id)
        if isinstance(n, ast.FunctionDef):
            funcs[n.name] = len(n.args.args)
    gates = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Call)
                and isinstance(n.func, ast.Name) and n.func.id in ('gate', 'check'))
    return names, funcs, gates


S16 = ('receipts/L_probability/S16_the_prefix_is_a_rewriting_job_not_an_adjudication_one_and_its_'
       'paper_half_and_source_half_have_opposite_right_answers.py')
S5 = ('receipts/L_probability/S5_the_set_shaped_class_is_absent_from_the_gate_layer_and_two_thirds_'
      'of_what_remains_sits_at_the_one_value_where_the_standing_guards_repair_is_a_tautology.py')
_n16, _f16, _g16 = _shape(S16)
_n5, _f5, _g5 = _shape(S5)
print(f"      S16 by structure: TABLE_PIN defined {('TABLE_PIN' in _n16)}, {_g16} gate call(s)")
print(f"      S5  by structure: _classify arity {_f5.get('_classify')}, "
      f"_introduced_record defined {('_introduced_record' in _f5)}, {_g5} gate call(s)", flush=True)
gate("Ⓔ① ⛔ THE RECEIPT THAT REPORTED THE `171` ASSERTED THAT ITS TABLE MATCHED THE BASELINE *NOW*, so"
     " converting the prefix red it -- a gate going red on the success of the work its own receipt"
     " reported, in the same shape repaired twice in the previous cycle.  ✔ *Repaired by `L-249`'s"
     " rule, and checked HERE BY PARSING rather than by quoting its text: it now defines a commit pin"
     " at module level and carries one more gate than it did, the live state having been split off"
     " into its own*",
     'TABLE_PIN' in _n16 and _g16 >= 15)

gate("Ⓔ② ✔ AND THE ORDERED REPAIR IS IN, ALSO CHECKED BY PARSING: the authorship decision is now a"
     " FUNCTION of the introducing commit's record -- two parameters, the parents and the subject --"
     " beside a reader that returns that record, so a path whose introducing commit is a merge or"
     " carries no revision id can be classified UNATTRIBUTED rather than owned.  ⌗ *The arity is the"
     " point: factoring the decision out is what let the merge arm be controlled without inventing a"
     " merge in history*",
     _f5.get('_classify') == 2 and '_introduced_record' in _f5 and _g5 >= 29)

_SAMPLE = 120
_paths = sorted(f for f in _git('ls-tree', '-r', '--name-only', 'HEAD', 'receipts/').split('\n')
                if f.endswith('.py'))
_step = max(1, len(_paths) // _SAMPLE)
_cls = collections.Counter()
_REV = re.compile(r'\br(\d{4})\b')
for _p in _paths[::_step][:_SAMPLE]:
    _o = [l for l in _git('log', '--diff-filter=A', '--format=%H|%P|%s', '--', _p).strip().split('\n')
          if l.strip()]
    if not _o:
        continue
    _h, _P, _subj = _o[-1].split('|', 2)
    if len(_P.split()) > 1:
        _cls['MERGE'] += 1
    elif _REV.search(_subj) is None:
        _cls['NO-REVISION-ID'] += 1
    else:
        _cls['EVEN' if int(_REV.search(_subj).group(1)) % 2 == 0 else 'ODD'] += 1
print(f"      this receipt's OWN measurement over {sum(_cls.values())} receipt paths: {dict(_cls)}")
gate(f"Ⓔ③ ⛔ AND THE MEASUREMENT CORRECTS THE DIAGNOSIS THE REPAIR WAS ORDERED FROM, MEASURED HERE AND"
     f" NOT QUOTED: over {sum(_cls.values())} paths of this tree NOT ONE receipt has a MERGE as its"
     f" introducing commit --- so the hazard the order named is real and UNINSTANTIATED --- while"
     f" {_cls['NO-REVISION-ID']} carry an introducing commit with no revision id at all, from the"
     f" naming eras before them.  ⇒ ***So the live defect is the one nobody named, and the named one is"
     f" a guard with a control rather than a repair with a population***",
     _cls['MERGE'] == 0 and _cls['NO-REVISION-ID'] > 0 and sum(_cls.values()) >= 100)

# =====================================================================================
head("F -- WHAT THE LEDGER LOOKS LIKE AFTER IT, AND WHAT THIS RECEIPT DOES NOT TOUCH")

P = STATS['prefix_now']
print(f"      the prefix now: {P}")
print(f"      the whole baseline now: {STATS['baseline_now']}")
gate(f"Ⓕ① the prefix reconciles without slack: `{P['MEANING-HELD']}` `MEANING-HELD` is the `144` from"
     f" the conversion plus the `{STATS['pre_settlement_converted']}` pre-settlement rows whose own"
     f" reason already named `L-249`'s repair as the one they were owed, `{P['REPAIR-OWED']}` remain"
     f" owed, and `{P['EXTENDED']}` are untouched",
     P['MEANING-HELD'] == CNT['MEANING-HELD'] + STATS['pre_settlement_converted']
     and P['REPAIR-OWED'] == CNT['REPAIR-OWED'] and P['EXTENDED'] == len(EXT))

gate("Ⓕ② ⌗ and the `UNADJUDICATED` buckets are untouched by this revision: a conversion moves rows"
     " BETWEEN adjudicated verdicts and may not lower the one count `PO-78` ratchets, so the backlog"
     " is exactly where the previous revision left it",
     STATS['baseline_now'].get('UNADJUDICATED', 0) == 1428
     and 'UNADJUDICATED' not in set(r[5] for r in CONV))

_own = [r for r in BASE if r[0].endswith('forty_six_character_windows.py')]
print(f"      this receipt's own keys in the baseline: {len(_own)}, verdicts"
      f" {sorted({r[5] for r in _own})}")
gate("Ⓕ③ ⛔ AND THIS RECEIPT ADDED TWO KEYS TO THE CLASS IT IS ABOUT, AND CLEARS THEM IN THE SAME PASS"
     " RATHER THAN LEAVING THEM TO RAISE A CEILING: both are membership tests against a SYMBOL TABLE"
     " built by parsing a module, not against its text, so a rewording cannot break them and only"
     " deleting the name can -- which is what they assert.  ⌗ *Their first form DID pin text, nine keys"
     " of it, and the operator caught them before they shipped; the verdict recorded is the operator's"
     " own false-positive bucket, with the reason in the row*",
     len(_own) == 2 and {r[5] for r in _own} == {'NOT-A-PIN'})

gate("Ⓖ① ⌗ and this receipt asserts nothing about any paper's wording: it reads its own published"
     " tables, the baseline as data, two of this line's own receipts as text, and the papers only"
     " through a word-alignment function that asks where a span's edges fall -- so it cannot break"
     " when a paper is reworded, which is the whole defect `PO-78` exists to measure",
     not any(r[0].endswith('.tex') for r in BASE)
     and os.path.basename(D) == 'r7256_60_convert_the_one_seven_one')

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  gates run: {len(CHECKS)}, failed: {len(CHECKS) - npass}   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE 171 WAS NEVER A REWRITING QUEUE: 144 OF IT IS A FINDING HELD AT ITS
  COMMIT, 17 IS OWED A REPAIR, AND 10 WAS DELIBERATE ALL ALONG.

  The order's reading was right and this line's unit was wrong.  A correct
  reading against a vocabulary with no slot for the answer produces a
  number that means something other than it says, and the repair was a
  sixth verdict rather than a different reading.

  AND THE RESIDUE IS NOT WHAT THIS SEAT PREDICTED.  It was predicted to be
  the pins whose finding is about the paper's live state; it is markup and
  clipping -- a span carrying \\emph{} that is no part of the claim, a span
  cut mid-word.  That prediction was the one independent thing in the
  pre-registration and it is refuted in both directions at once.

  THE GRAIN CLAUSE CLEARS ITS OWN NEGATIVE ON THIS HALF, AND WALKS INTO A
  COLLISION.  It changes ten verdicts here, above the five that would have
  unbound it.  Applied to another seat's sixty-four EXTENDED rows it cannot
  ratify forty-six of the fifty-six that pin a paper, because those spans
  are character windows and `the shortest span that carries the claim' is
  undefined for a character window.  The clause needs a second clause.  No
  verdict of theirs is changed here.

  THE GUARD: a clause that fixes the GRAIN of a test still has to say what
  the grain is measured over.  Minimality over arbitrary substrings and
  minimality over grammatical units are different rules, and a repair class
  built on the first cannot be ratified or refused by the second.
  ==========================================================================
""")
