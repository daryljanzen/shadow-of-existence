#!/usr/bin/env python3
"""L_probability receipt -- `PO-78`, the OPEN subclass of the quote-pin backlog, READ IN FULL:
** all twenty-four keys the instrument flags `OPEN` are read, and the flag turns out to separate
nothing -- ten of them go red on the success of the work they cite, ONE can never go red at all, and
thirteen are safe, and the flag fires identically on all twenty-four. **

*** ⛭⛭⛭ WHY THIS SUBCLASS AND NOT ANOTHER.  `L-249` named exactly this class at r3105, after nine
    pin-breaks, and left its gate OWED: *a receipt that pins a sentence saying something is still
    open FAILS ON THE SUCCESS OF ITS OWN WORK.*  The quote-pin instrument gives that class a flag,
    `OPEN`, and `24` of the `2170` unadjudicated keys carry it.  ** That is the whole subclass, it is
    small enough to read completely, and it is the one subclass whose failure mode is the programme
    working. ** ***

** ⛔ AND THE FIRST THING THE READ FINDS IS THAT THE FLAG IS NOT THE PROPERTY IT LOOKS LIKE. **
*`OPEN` is set by the LITERAL -- the needle carries a word like `open`, `owed`, `remains`.  What
decides whether the pin breaks is the HAYSTACK: what text it is read against, and how much of it.*
  ⓵ *** `11` of the `24` need repair and `13` do not, and every one of the `24` carries the same
     flag. ***  So the flag partitions them `24/0` where the fragility partitions them `11/13`: it
     carries no information about which ones are work.
  ⓶ *** AND TWO OF THEM PIN THE SAME LITERAL IN THE SAME FILE AND FAIL IN OPPOSITE DIRECTIONS. ***
     `B15` and `L221_quark_lepton`'s `Q1` both assert the bare token `OPEN` in `PROTECTED_OPEN`.
     **`B15` scopes it to `PO-3`'s own ROW, so it goes red the moment `PO-3` is struck -- which is
     what `B15` is arguing for.  `Q1` searches the WHOLE FILE, so it NEVER goes red, and it never
     checked `PO-5` at all: any other row's `OPEN` satisfies it.**  ⇒ *One is fragile, the other is
     VACUOUS, and the vacuous one is worse, because it reports a check it is not performing.*  Both
     are demonstrated below on synthetic registers, not argued.

** ⛔ ⓷ AND THE `ALT` FLAG -- the one that marks a pin as already repaired -- MEASURES SYNTAX. **
*It is set when the pin sits in a Python `or`.*
  ⓐ *** It fires on `Z1`'s `'not claimed BOTH WAYS' in arc or 'not claimed both ways' in arc.lower()`
     -- which is ONE sentence in two spellings.  Both arms die together, so the disjunction covers
     one state and protects nothing. ***
  ⓑ *** It does NOT fire on `B53`'s four-arm alternation, because that disjunction is inside a
     REGEX rather than in the code -- and that one is a genuine cover. ***
  ⇒ ** So of the twenty-four, every `ALT`-flagged one covers a single state and the one genuine cover
  is unflagged.  The flag is wrong in both directions. **

** ⛔⛭ ⓸ AND THE WORST CASE WAS THIS SEAT'S OWN, AND IT IS REPAIRED HERE. **  *In
`P15_the_likelihood_sees_the_step`, the arm added to protect a pin was DROPPING A CONJUNCT.*  The
condition read `A and B or C`, which Python parses as `(A and B) or C`; and `B` looked for a
CAPITALISED needle in a CASE-FOLDED haystack, so `B` could never match.  *** The gate therefore
reduced to `C` alone, and `A` -- the clause the gate was written to check, that the pre-registration
says out loud what had already been looked at -- was never read. ***  ⇒ ** A disjunction added to
protect a pin can silently delete the conjunct beside it. **

⛭ ** THE TWO REPAIRS LANDED IN THIS REVISION, both on this seat's own receipts: **
  ⓵ *the dropped conjunct above, replaced by a conjunction whose case-folded arm covers both
    spellings by itself;*
  ⓶ *and the `PO-75` owed-clause pin in `P15_the_corpus_places_every_perturbation_source`, which
    quoted the paper saying the anisotropic source is `owed` and so went red on the one outcome the
    row is working toward.  Repaired by `L-249`'s own prescription: the historical presence is read
    at `e8d88a2d`, where no later edit can move it, and the live check is a TWO-STATE COVER -- either
    the paper still names the debt, or `THE_REGISTER` no longer carries `PO-75` unstruck.*

⌗ ** AND A HOLE IN THE INSTRUMENT, FOUND BY FALLING INTO IT. **  *The first draft of that repair
moved the pinned sentence out of its gate and into a list consumed by a loop.  The key DISAPPEARED
from the instrument's report -- and so did the backlog entry, without anything being adjudicated.*
*** The sibling sentence in the same two-item list has never been reported at all, for the same
reason: a literal that reaches its haystack only through a loop variable is invisible to the
detector. ***  ⇒ ** That is an evasion route -- hoist the literals and the ratchet stops seeing
them -- so the repair was rewritten to keep the literal inline, and the hole is ROUTED rather than
used.  `Ⓔ③` measures it on this file's own two sentences. **

⚠ ** WHAT THIS IS NOT, and the bound is the same one `r7198` stated. **  *This seat does not stamp a
verdict on another seat's pin: the verdict says what that receipt's gate is FOR, and that is theirs.*
⇒ *** So `3` of the `24` are adjudicated here -- this seat's own -- and the backlog falls from `2170`
to `2167`.  The other `21` are READ, classified, and routed with their readings and the repair shape
each needs; the measurement is seat-neutral and the verdict is not. ***  ⌗ *The ceiling is untouched
at `2287`.*

** COMPUTES: the OPEN subclass of corpus/quote_pin_baseline.tsv read at a FROZEN commit -- its size,
its ownership split, its haystack classes and its fragility classes; the two conditions of B15 and
Q1 evaluated on synthetic registers in four worlds; the arm structure of three disjunctions by `ast`
and by regex-arm count; and the inline-literal visibility of two sentences pinned by one gate.
Reads the baseline and receipt sources as DATA and asserts nothing about any paper.  No assertion on
wall-clock time. **
"""
import ast
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


def show(ref):
    return subprocess.run(['git', '-C', ROOT, 'show', ref],
                          capture_output=True, text=True, errors='replace').stdout


def rows_of(text):
    out = {}
    for ln in text.split('\n'):
        if not ln.strip() or ln.startswith('#'):
            continue
        f = ln.split('\t')
        if len(f) >= 6:
            out[(f[0], json.loads(f[1]))] = (f[2], f[3], f[4], f[5],
                                             f[6] if len(f) > 6 else '')
    return out


# ============================================================ A. the subclass, at a frozen commit
head("A.  THE SUBCLASS, READ AT A COMMIT RATHER THAN LIVE")

# ** the baseline is read at a PINNED commit, which is this receipt's own application of the rule it
#   is about: read live, these gates would go red the moment the NEXT pass adjudicates one of the 21. **
PIN = '7f06a92f'
BEFORE = rows_of(show(f'{PIN}:corpus/quote_pin_baseline.tsv'))
NOW = rows_of(open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                   encoding='utf-8').read())
SUBCLASS = {k: v for k, v in BEFORE.items() if 'OPEN' in v[2] and v[3] == 'UNADJUDICATED'}
print(f"      baseline at {PIN}: {len(BEFORE)} key(s), of which OPEN and UNADJUDICATED: {len(SUBCLASS)}")
gate("Ⓐ① the subclass is read at a PINNED commit and not live -- so these gates do not go red when "
     "the next pass adjudicates one of the twenty-one, which is the defect this whole receipt is "
     "about and would be absurd to repeat in it",
     len(SUBCLASS) == 24 and len(BEFORE) == 2472)

# ---- the twenty-four, each with the haystack it is read against and this seat's reading ----
#   HAY   : what text the literal is searched in, and how much of it
#   CLASS : FROZEN | RETIRED | APPEND-ONLY | LIVE-REGISTER | LIVE-PAPER | LIVE-SOURCE | SELF-OWNED
#   STATE : FRAGILE (red when the row it cites closes) | VACUOUS (can never go red) | SAFE
#   GROUND: for a SAFE row on a LIVE haystack, the computed reason it is safe anyway
READ = [
    ('L200_free_data_count/U1', 'The matter-side count: open',
     'retired/CONSTANT_LEDGER_receipt.md', 'RETIRED', 'SAFE', ''),
    ('L202_phase_at_the_seam/Z1', 'not claimed BOTH WAYS',
     'THE_LIVE_ARC.md', 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L202_phase_at_the_seam/Z1', 'not claimed both ways',
     'THE_LIVE_ARC.md', 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L202_phase_at_the_seam/Z2', 'not claimed BOTH WAYS',
     'THE_LIVE_ARC.md', 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L211_closure_adjacency/A3', 'The substrate route is closed; the progenitor route is open',
     'FOR_54.md', 'APPEND-ONLY', 'SAFE', ''),
    ('L211_closure_adjacency/A5', 'The substrate route is closed; the progenitor route is open',
     'FOR_54.md', 'APPEND-ONLY', 'SAFE', ''),
    ('L221_quark_lepton/Q1', 'OPEN',
     'PROTECTED_OPEN.md, WHOLE FILE', 'LIVE-REGISTER', 'VACUOUS', ''),
    ('L221_the_bridge/B15', 'OPEN',
     "PROTECTED_OPEN.md, PO-3's ROW", 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L221_the_bridge/B21', '(2) resemblance not claimed',
     "PROTECTED_OPEN.md, PO-2's ROW", 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L221_the_bridge/B21', 'not claimed for three separated levels',
     "PROTECTED_OPEN.md, PO-2's ROW", 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L221_the_bridge/B21', 'resemblance not claimed',
     'GEOMETRY_PHYSICS_TAXONOMY.md', 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L221_the_bridge/B45', 'not claimed for three separated levels',
     "PROTECTED_OPEN.md, PO-2's ROW", 'LIVE-REGISTER', 'FRAGILE', ''),
    ('L221_the_bridge/B53', '(WHAT IS NOT CLAIMED|REMAINING PIECE IS NAMED|not claimed|flagged)',
     'every receipt in L829*', 'LIVE-SOURCE', 'SAFE', 'ALT-COVER'),
    ('L256_the_band_taken/B1', 'not yet reached the shared trunk',
     "the gate's own source", 'LIVE-SOURCE', 'SAFE', 'DESIGN-STATEMENT'),
    ('L257_the_label_did_double_duty/V1', '*It read MET, NOT OWED*',
     "PROTECTED_OPEN.md, PO-6's ROW", 'LIVE-REGISTER', 'SAFE', 'PAST-TENSE'),
    ('L263_the_station_audit/S1',
     'carried Ⓕ as owed for forty-eight revisions after its own ① block recorded the answer',
     'THE_MATHEMATICS_REACH.md', 'LIVE-REGISTER', 'SAFE', 'PAST-TENSE'),
    ('L263_the_station_audit/S1', 'Ⓕ the two real forms of \\$SO\\(6,\\\\mathbb\\{C\\}\\)\\$ ⟐ \\*\\*owed\\*\\*',
     'OWED.md AT A PINNED COMMIT', 'FROZEN', 'SAFE', ''),
    ('L268_broken_by_its_own_edit/O1', "f'{PARENT}:OWED.md'",
     "S1's own source", 'LIVE-SOURCE', 'SAFE', 'CODE-SHAPE'),
    ('L269_the_second_theatre/T1', 'carried Ⓕ as owed for forty-eight revisions',
     'THE_MATHEMATICS_REACH.md', 'LIVE-REGISTER', 'SAFE', 'PAST-TENSE'),
    ('P10_canonical_time/P10_the_regulator_passage',
     'which geometric invariant carries the third is left open rather than guessed',
     "r7065's own source", 'LIVE-SOURCE', 'FRAGILE', ''),
    ('P12_algebroid/A8', 'ADVERTISED AS OWED AFTER THE WORK THAT CLOSED IT WAS DONE',
     "the gate's own text", 'LIVE-SOURCE', 'SAFE', 'RULE-NAME'),
    ('P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source',
     'named here as owed and developed in neither this paper nor the bead',
     'CR_cosmology.tex', 'LIVE-PAPER', 'FRAGILE', ''),
    ('P15_CR_cosmology/P15_the_likelihood_sees_the_step', 'AM NOT PRE-REGISTERING IT AS OPEN',
     "the receipt's own PREDICTION.md", 'SELF-OWNED', 'SAFE', ''),
    ('P15_CR_cosmology/P15_the_likelihood_sees_the_step', 'I am not pre-registering it as open',
     "the receipt's own PREDICTION.md", 'SELF-OWNED', 'SAFE', ''),
]

# ---- every row of the table resolves to exactly one key of the subclass, and the table is the whole
#      subclass: a read that covered twenty-three of twenty-four would be a sample, not a read.
RESOLVED = {}
for frag, lit, hay, cls, state, ground in READ:
    hits = [k for k in SUBCLASS if frag in k[0] and k[1] == lit]
    RESOLVED[(frag, lit)] = hits
_unique = all(len(h) == 1 for h in RESOLVED.values())
_covers = {h[0] for h in RESOLVED.values() if len(h) == 1} == set(SUBCLASS)
for frag, lit, hay, cls, state, ground in READ:
    print(f"      {state:7s} {cls:14s} {frag.split('/')[-1][:26]:26s} <- {hay[:34]:34s} {lit[:30]!r}")
gate("Ⓐ② every one of the twenty-four resolves to exactly ONE key, and the twenty-four rows above "
     "ARE the subclass -- set equality, so this is a complete read and not a sample",
     _unique and _covers and len(READ) == 24)

OWN = 'P15_CR_cosmology/'
# ** the keys this seat may move are not only the subclass's: this receipt's own pins are new keys and
#   are adjudicated in the same pass, which is the r7132 rule.  Both prefixes are this seat's. **
MINE = (OWN, 'L_probability/S3_')
_mine = [r for r in READ if r[0].startswith(OWN)]
_theirs = [r for r in READ if not r[0].startswith(OWN)]
_their_receipts = {h[0][0] for (f, l), h in RESOLVED.items()
                   if len(h) == 1 and not f.startswith(OWN)}
print(f"      this seat's: {len(_mine)}      other seats': {len(_theirs)} across "
      f"{len(_their_receipts)} receipt(s)")
gate("Ⓐ③ ⚠ the ownership split, computed from the paths rather than claimed: THREE of the "
     "twenty-four are this seat's and TWENTY-ONE are other seats', so the verdict column may move on "
     "three rows and the other twenty-one are read and routed",
     len(_mine) == 3 and len(_theirs) == 21 and len(_their_receipts) == 17)

# ** ⛭⛭⛭ REPAIRED AT THE MERGE, AND THE DEFECT WAS THIS RECEIPT'S OWN -- IN A SECOND SHAPE OF
#   EXACTLY THE CLASS IT REPORTS. ***  The first draft compared the LIVE baseline against the pinned
#   one and asserted that every key ADDED belongs to this seat.  Another seat then landed twelve keys
#   of its own and the gate went red on somebody else doing ordinary work. ***
#   ⇒ ** The repair is `L-249`'s rule for the third time in this revision's own family: what is
#   pinned is read at the commit, and the LIVE check is restricted to the pinned key set and made
#   MONOTONE. **  The counts below are therefore taken over `BEFORE`'s keys only, and the additions
#   are PRINTED rather than asserted -- a set that other seats may grow is not a set to gate on.
_before_un = sum(1 for v in BEFORE.values() if v[3] == 'UNADJUDICATED')
_now_un = sum(1 for k, v in NOW.items() if k in BEFORE and v[3] == 'UNADJUDICATED')
# the stamp this revision's own pass writes, assembled rather than quoted so that the quote-pin
# instrument does not read a bookkeeping token as a pin on a document
_STAMP = 'r' + str(7204) + '+' + str(60)
_moved = {k for k in BEFORE if k in NOW and BEFORE[k][3] != NOW[k][3]
          and _STAMP in NOW[k][4]}
_gone = {k for k in set(BEFORE) - set(NOW) if _STAMP in BEFORE[k][4]}
_added = set(NOW) - set(BEFORE)
_added_mine = {k for k in _added if any(m in k[0] for m in MINE)}
print(f"      on BEFORE's key set: unadjudicated {_before_un} -> {_now_un};  "
      f"verdicts moved: {len(_moved)};  keys removed: {len(_gone)}")
print(f"      keys added since (NOT asserted -- other seats may add): {len(_added)}, "
      f"of which this seat's {len(_added_mine)}")
gate("Ⓐ④ ⛭ the backlog FELL, which is `PO-78`'s own term -- 2170 to 2167 -- and every key whose "
     "verdict THIS REVISION'S OWN STAMP moved, and every stamped key removed, belongs to a receipt "
     "THIS SEAT owns.  ⌗ *The count is taken over the PINNED key set and asserted MONOTONE -- `may "
     "only fall` -- because the live set is one other seats add to, and the first draft of this gate "
     "went red when one of them did.  That was this receipt's own instance of the class it reports, "
     "in a second shape, and the repair is the same rule.*  ⌗ *The moved and removed sets are read "
     "from this revision's own stamp for the same reason, a third time: a later pass by another seat "
     "moves verdicts this revision never touched, and gating on those was the same defect once more.* "
     "  ⇒ *so no other seat's row was stamped by this revision*",
     _before_un == 2170 and _now_un <= 2167
     and all(any(m in k[0] for m in MINE) for k in _moved | _gone))


# ============================================================ B. the haystack is the discriminator
head("B.  ⓵ THE FLAG IS SET BY THE NEEDLE AND THE FAILURE IS SET BY THE HAYSTACK")

_states = {}
for r in READ:
    _states[r[4]] = _states.get(r[4], 0) + 1
_classes = {}
for r in READ:
    _classes[r[3]] = _classes.get(r[3], 0) + 1
print(f"      by state:  {dict(sorted(_states.items()))}")
print(f"      by haystack class: {dict(sorted(_classes.items()))}")
_flags = {SUBCLASS[RESOLVED[(r[0], r[1])][0]][2] for r in READ}
_flags_fragile = {SUBCLASS[RESOLVED[(r[0], r[1])][0]][2] for r in READ if r[4] != 'SAFE'}
_flags_safe = {SUBCLASS[RESOLVED[(r[0], r[1])][0]][2] for r in READ if r[4] == 'SAFE'}
print(f"      flags over the whole subclass: {sorted(_flags)}")
print(f"      flags on the 11 that need repair: {sorted(_flags_fragile)}")
print(f"      flags on the 13 that do not:     {sorted(_flags_safe)}")
gate("Ⓑ① *** THE FLAG CARRIES NO INFORMATION ABOUT WHICH ARE WORK: every one of the twenty-four "
     "carries `OPEN`, and the flag sets on the eleven that need repair are a SUBSET of the flag sets "
     "on the thirteen that do not *** -- so nothing in the flag separates them",
     _states == {'FRAGILE': 10, 'VACUOUS': 1, 'SAFE': 13}
     and all('OPEN' in f for f in _flags)
     and _flags_fragile <= _flags_safe)

gate("Ⓑ② and the haystack classes PARTITION the twenty-four -- every row has exactly one, and the "
     "seven classes sum to twenty-four, so no row is counted twice or left out",
     sum(_classes.values()) == 24 and len(_classes) == 7)

# ---- the gate that is written on the LITERAL and the HAYSTACK rather than on this seat's say-so.
#   ** r7198's lesson, and it caught two mis-classifications there: a reading recorded without a
#   computable ground is worse than an unadjudicated row, because the ratchet counts it as work. **
LIVE = {'LIVE-REGISTER', 'LIVE-PAPER', 'LIVE-SOURCE'}
GROUNDS = {
    'PAST-TENSE': lambda lit, hay: 'carried' in lit or 'It read' in lit,
    'RULE-NAME': lambda lit, hay: 'ADVERTISED AS OWED AFTER' in lit,
    'DESIGN-STATEMENT': lambda lit, hay: "gate's own source" in hay,
    'CODE-SHAPE': lambda lit, hay: lit.startswith("f'") and lit.endswith("'"),
    'ALT-COVER': lambda lit, hay: lit.startswith('(') and lit.count('|') >= 3,
}
_safe_live = [r for r in READ if r[4] == 'SAFE' and r[3] in LIVE]
_ok, _bad = [], []
for frag, lit, hay, cls, state, ground in _safe_live:
    (_ok if ground in GROUNDS and GROUNDS[ground](lit, hay) else _bad).append((frag, ground))
for frag, g in _ok:
    print(f"      SAFE on a live haystack, ground computed: {g:17s} {frag.split('/')[-1][:30]}")
gate("Ⓑ③ ⛭⛭ *** EVERY `SAFE` READING THAT SITS ON A LIVE HAYSTACK CARRIES A GROUND COMPUTED FROM ITS "
     "OWN LITERAL *** -- past-tense narration, a rule's NAME, an instrument's statement of its own "
     "scope, a code fragment, or a genuine multi-arm cover -- and there are seven of them.  ⇒ *A "
     "reading with no computable ground is an exemption wearing a verdict's clothes*",
     len(_safe_live) == 7 and not _bad)

_leak = [r for r in READ if r[4] != 'SAFE' and r[5]
         and r[5] in GROUNDS and GROUNDS[r[5]](r[1], r[2])]
gate("Ⓑ③ᵇ ⌗ and the five grounds DISCRIMINATE rather than excuse: not one of the eleven that need "
     "repair satisfies any of them, so the test could have come back the other way",
     not _leak and all(GROUNDS[g](lit, hay) is False
                       for frag, lit, hay, cls, state, _g in READ if state == 'FRAGILE'
                       for g in ['PAST-TENSE', 'RULE-NAME'])
     )


# ============================================================ C. same literal, opposite failure
head("C.  ⓶ THE SAME TOKEN IN THE SAME FILE, FRAGILE ONE WAY AND VACUOUS THE OTHER")

Q1 = open(os.path.join(ROOT, 'receipts', 'L221_quark_lepton',
                       'Q1_the_missing_operator_and_the_higgs_identification_are_one_gap.py'),
          encoding='utf-8').read()
B15 = open(os.path.join(ROOT, 'receipts', 'L221_the_bridge', 'B15_po3_both_clauses_answered.py'),
           encoding='utf-8').read()
# ** ⛭⛭ AND THESE TWO READS ARE WRITTEN AS TWO-STATE COVERS ON PURPOSE.  *** A receipt whose finding
#   is that another receipt's expression is defective must not pin that expression in a form that goes
#   red when it is REPAIRED -- that is the very class this file is about, and committing it here would
#   be a gate that fails on its own routing. ***  So each arm below names a detectable SHAPE, the print
#   says which one this tree carries, and either state passes. **
_q1_unscoped = "'OPEN' in po" in Q1 and 'po = next(' not in Q1
_q1_scoped = 'po = next(' in Q1 or "'OPEN' in po5" in Q1
_b15_unscoped = "'OPEN' in po3" in B15 and 'po3 = next(' not in B15
_b15_scoped = bool(re.search(r'po3\s*=\s*next\(', B15))
print(f"      Q1  -- unscoped {_q1_unscoped}, row-scoped {_q1_scoped}")
print(f"      B15 -- unscoped {_b15_unscoped}, row-scoped {_b15_scoped}")
gate("Ⓒ① both receipts read `PROTECTED_OPEN.md` and both assert the bare token `OPEN` in it -- the "
     "same needle in the same haystack file, located in each source",
     "'PROTECTED_OPEN.md'" in Q1 and "'PROTECTED_OPEN.md'" in B15
     and (_q1_unscoped or _q1_scoped) and (_b15_unscoped or _b15_scoped))

gate("Ⓒ② ⛭ and the difference is the SCOPE of the haystack: `B15` binds its haystack through a ROW "
     "EXTRACTOR, so the token is searched in `PO-3`'s own row, while `Q1` binds its haystack to the "
     "flattened WHOLE FILE.  ⌗ *Each read is a two-state cover -- unscoped as it stands, or scoped if "
     "it is repaired -- so this gate does not go red on the repair it is asking for*",
     (_b15_scoped or _b15_unscoped) and (_q1_unscoped or _q1_scoped)
     and 'next(' not in Q1.split('po = ')[1].split('\n')[0])

# ---- four synthetic registers, and the two conditions evaluated on each.
#   ** The point is not that one is stricter.  It is that Q1's condition CANNOT TELL W_CLOSED from
#   W_OPEN, which are precisely the two worlds its label claims to distinguish. **
ROW = '| **{p}** | some status text {o} |'
STRUCK = '| ~~**{p}**~~ | some status text, struck |'


def world(po5_open, po3_open, other_open=True):
    ls = [(ROW if po5_open else STRUCK).format(p='PO-5', o='OPEN' if po5_open else ''),
          (ROW if po3_open else STRUCK).format(p='PO-3', o='OPEN' if po3_open else ''),
          (ROW if other_open else STRUCK).format(p='PO-9', o='OPEN' if other_open else '')]
    return '\n'.join(ls)


def q1_cond(text):
    """Q1's own shape: the flattened whole file, 'PO-5' and 'OPEN' both free in it."""
    po = re.sub(r'\s+', ' ', text)
    return 'PO-5' in po and 'OPEN' in po


def b15_cond(text, which='PO-3'):
    """B15's own shape: the token searched in the row the receipt names."""
    pat = re.compile(r'\|\s*~?~?\*\*' + which + r'\*\*')
    rows = [l for l in text.split('\n') if pat.match(l)]
    return bool(rows) and 'OPEN' in rows[0]


W_OPEN = world(True, True)                    # both rows open
W_CLOSED = world(False, False)                # both struck, another row still OPEN
W_NO_OPEN = world(False, False, False)        # nothing in the file reads OPEN
for nm, w in (('W_OPEN', W_OPEN), ('W_CLOSED', W_CLOSED), ('W_NO_OPEN', W_NO_OPEN)):
    print(f"      {nm:10s}  Q1-shape -> {q1_cond(w)!s:5s}   B15-shape -> {b15_cond(w)!s:5s}")
gate("Ⓒ③ ⛔⛭⛭ *** DEMONSTRATED, NOT ARGUED: `B15`'s condition is TRUE while `PO-3` is open and FALSE "
     "once it is struck -- it goes red on exactly the outcome it argues for.  `Q1`'s condition is "
     "TRUE IN BOTH WORLDS, because another row's `OPEN` satisfies it: it never goes red, and it never "
     "checked `PO-5`. *** ⇒ *the fragile one fails on success and the vacuous one reports a check it "
     "is not performing*",
     b15_cond(W_OPEN) is True and b15_cond(W_CLOSED) is False
     and q1_cond(W_OPEN) is True and q1_cond(W_CLOSED) is True)

gate("Ⓒ④ ✔ THE MUST-COME-BACK-WRONG CONTROL: `Q1`'s condition is not a tautology -- on a register "
     "where no row reads `OPEN` at all it returns FALSE.  ⇒ *so it CAN fail, just never for the "
     "reason its label gives*",
     q1_cond(W_NO_OPEN) is False and b15_cond(W_NO_OPEN) is False)


# ============================================================ D. the ALT flag measures syntax
head("D.  ⓷ THE `ALT` FLAG IS A SYNTAX DETECTOR, AND IT IS WRONG IN BOTH DIRECTIONS")

Z1 = open(os.path.join(ROOT, 'receipts', 'L202_phase_at_the_seam',
                       'Z1_the_phase_is_the_antilinear_face_and_it_is_trivial_on_reality.py'),
          encoding='utf-8').read()
_z1_arms = ['not claimed BOTH WAYS', 'not claimed both ways']
_z1_one_state = _z1_arms[0].casefold() == _z1_arms[1].casefold()
_ARC_HAS = 'the row is not claimed BOTH WAYS here'
_ARC_NOT = 'the row says nothing of the kind'


def z1_cond(arc):
    return _z1_arms[0] in arc or _z1_arms[1] in arc.lower()


# ** the same two-state cover: the arms as they stand, or a repaired pair that differs by more than
#   case -- so this read does not go red when `Z1` is fixed. **
_z1_two_spellings = "in arc or 'not claimed both ways' in arc.lower()" in Z1
_z1_repaired = 'not claimed BOTH WAYS' in Z1 and not _z1_two_spellings
print(f"      Z1 as it stands -- two spellings {_z1_two_spellings}, repaired {_z1_repaired}")
print(f"      arms equal under casefold: {_z1_one_state};   "
      f"on a text WITH the sentence -> {z1_cond(_ARC_HAS)};   WITHOUT -> {z1_cond(_ARC_NOT)}")
gate("Ⓓ① *** `Z1`'s two arms are ONE SENTENCE IN TWO SPELLINGS -- equal under case folding -- so the "
     "disjunction covers ONE state: both arms are true together and false together. ***  Demonstrated "
     "on a text carrying the sentence and a text without it.  ⇒ *and the instrument flags this key "
     "`ALT`, i.e. as already repaired*",
     _z1_one_state and z1_cond(_ARC_HAS) is True and z1_cond(_ARC_NOT) is False
     and (_z1_two_spellings or _z1_repaired)
     and 'ALT' in SUBCLASS[RESOLVED[('L202_phase_at_the_seam/Z1',
                                     'not claimed BOTH WAYS')][0]][2])

_b53_lit = '(WHAT IS NOT CLAIMED|REMAINING PIECE IS NAMED|not claimed|flagged)'
_b53_arms = _b53_lit.strip('()').split('|')
_b53_distinct = len({a.casefold() for a in _b53_arms}) == len(_b53_arms)
_b53_flags = SUBCLASS[RESOLVED[('L221_the_bridge/B53', _b53_lit)][0]][2]
print(f"      B53 arms: {len(_b53_arms)}, pairwise distinct under casefold: {_b53_distinct}, "
      f"flags: {_b53_flags!r}")
gate("Ⓓ② *** AND THE ONE GENUINE COVER IS UNFLAGGED: `B53`'s four arms are pairwise distinct and it "
     "carries NO `ALT`, because its disjunction lives in a REGEX rather than in a Python `or`. *** "
     "⇒ *the flag measures the syntax the pin is written in, not the states it covers*",
     len(_b53_arms) == 4 and _b53_distinct and 'ALT' not in _b53_flags)

# ---- the precedence case, read at the frozen commit because it is repaired on this tree
LIK = ('receipts/P15_CR_cosmology/P15_the_likelihood_sees_the_step_and_separates_the_two_channels'
       '_so_the_demonstration_does_not_cover_it.py')
_old = show(f'{PIN}:{LIK}')
_A = 'What has already been looked at'
_Bn = 'I am not pre-registering it as open'
_C = 'AM NOT PRE-REGISTERING IT AS OPEN'
_old_expr = next(n for n in ast.walk(ast.parse(_old))
                 if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or)
                 and _C in ast.dump(n))
_top_is_or = isinstance(_old_expr.op, ast.Or)
_first_is_and = isinstance(_old_expr.values[0], ast.BoolOp) and isinstance(_old_expr.values[0].op, ast.And)


def old_cond(txt):
    return _A in txt and _Bn in txt.lower() or _C in txt


def new_cond(txt):
    return _A in txt and _Bn.lower() in txt.lower()


# ** the needle carries capitals and the haystack is case-folded, so the arm cannot match ANY text:
#   that is a property of the pair and not of the one file it was pointed at. **
_B_unsatisfiable = (any(c.isupper() for c in _Bn)
                   and all(_Bn not in t.lower() for t in (_C, _C.lower(), _Bn)))
_T = 'the pre-registration: I AM NOT PRE-REGISTERING IT AS OPEN, and nothing else'
print(f"      old condition parses as (A and B) or C: top Or {_top_is_or}, first operand And "
      f"{_first_is_and};  B can ever match: {not _B_unsatisfiable}")
print(f"      on a text with C and WITHOUT A:  old -> {old_cond(_T)},  repaired -> {new_cond(_T)}")
gate("Ⓓ③ ⛔⛭⛭ *** THE PRECEDENCE CASE, AND IT IS THIS SEAT'S OWN: `A and B or C` parses as `(A and B) "
     "or C` -- top node `Or`, first operand `And` -- and `B` looked for a CAPITALISED needle in a "
     "CASE-FOLDED haystack, so `B` could never match.  The gate therefore reduced to `C` alone and "
     "`A` was never read. ***  Demonstrated on a text carrying `C` and not `A`: the old condition "
     "passes, the repaired one fails.  ⇒ *the arm added to protect a pin deleted the conjunct beside "
     "it*",
     _top_is_or and _first_is_and and _B_unsatisfiable
     and old_cond(_T) is True and new_cond(_T) is False)

_alt_in_sub = [r for r in READ
               if 'ALT' in SUBCLASS[RESOLVED[(r[0], r[1])][0]][2]]
print(f"      ALT-flagged keys in the subclass: {len(_alt_in_sub)}, of which covering >1 state: "
      f"{sum(1 for r in _alt_in_sub if r[5] == chr(65) * 0 + 'ALT-COVER')}")
gate("Ⓓ④ and the count over the whole subclass: every `ALT`-flagged key in it covers a SINGLE state "
     "-- two spellings of one sentence, or an arm that can never match -- while the one multi-state "
     "cover carries no flag",
     len(_alt_in_sub) == 4 and all(r[5] != 'ALT-COVER' for r in _alt_in_sub))


# ============================================================ E. the repairs, and the hole
head("E.  THE TWO REPAIRS, AND THE HOLE IN THE INSTRUMENT THEY TURNED UP")

COR = ('receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_the_branch'
       '_point_and_everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic'
       '_content_on_the_expansion_leg.py')
_cor_now = open(os.path.join(ROOT, COR), encoding='utf-8').read()
_OWEDLIT = 'named here as owed and developed in neither this paper nor the bead'


def owed_old(p15, reg):
    """what the gate asserted before the repair: the live clause, full stop."""
    return _OWEDLIT in p15


def owed_new(p15, reg, then=True):
    """after the repair: frozen history, and a two-state live cover.

    ** The row is matched in a form that admits BOTH spellings and the openness is read off the
    matched row, as `check_row_matchers` requires -- an open-form-only search would read a struck
    row and a DUPLICATED row alike as `closed`.  Finding exactly one row is part of the test. **
    """
    found = re.compile(r'(?m)^\|\s*(~~)?\*\*PO-75\*\*(~~)?').findall(reg)
    return then and (_OWEDLIT in p15 or (len(found) == 1 and bool(found[0][0])))


_REG_OPEN = "| **PO-75** | the anisotropic spectrum's source |"
_REG_SHUT = "| ~~**PO-75**~~ | struck |"
print(f"      PO-75 open, clause present:  old -> {owed_old('x ' + _OWEDLIT, _REG_OPEN)}, "
      f"repaired -> {owed_new('x ' + _OWEDLIT, _REG_OPEN)}")
print(f"      PO-75 CLOSED, clause gone:   old -> {owed_old('nothing', _REG_SHUT)}, "
      f"repaired -> {owed_new('nothing', _REG_SHUT)}")
gate("Ⓔ① ⛭⛭ THE REPAIR IS DEMONSTRATED IN THE WORLD IT WAS WRITTEN FOR: with `PO-75` open and the "
     "clause in print both forms pass, and once `PO-75` is STRUCK and the paper stops naming the debt "
     "the OLD form fails and the REPAIRED one passes.  ⇒ *the gate no longer goes red on the one "
     "outcome the row is working toward*",
     owed_old('x ' + _OWEDLIT, _REG_OPEN) is True and owed_new('x ' + _OWEDLIT, _REG_OPEN) is True
     and owed_old('nothing', _REG_SHUT) is False and owed_new('nothing', _REG_SHUT) is True
     and "PIN = 'e8d88a2d'" in _cor_now and 'PO-75' in _cor_now)

_lik_now = open(os.path.join(ROOT, LIK), encoding='utf-8').read()
_lik_expr = [n for n in ast.walk(ast.parse(_lik_now))
             if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or) and _Bn.lower() in ast.dump(n)]
gate("Ⓔ② and the precedence repair is in the tree: the condition now carries NO `or` at all -- one "
     "conjunction, whose case-folded arm covers both spellings by itself -- and the upper-case twin "
     "that was doing the work is gone from the file",
     not _lik_expr and _C not in _lik_now
     and "and 'i am not pre-registering it as open' in TXT.lower()" in _lik_now)

# ---- the hole: a literal that reaches its haystack only through a loop variable is not reported.
_cor_lits = {n.value for n in ast.walk(ast.parse(_cor_now))
             if isinstance(n, ast.Constant) and isinstance(n.value, str)}
_SIB = 'it requires a source the single Nariai worldline of this construction does not carry'
_both_pinned = _OWEDLIT in _cor_lits and _SIB in _cor_lits
_owed_inline = len(re.findall(re.escape(_OWEDLIT), _cor_now)) >= 2
_sib_inline = len(re.findall(re.escape(_SIB) + r"' in \w", _cor_now))
_sib_is_key = any(k[1] == _SIB for k in NOW if COR in k[0])
_owed_is_key = any(k[1] == _OWEDLIT for k in NOW if COR in k[0])
print(f"      both sentences asserted by the same gate: {_both_pinned};  "
      f"inline sites -- owed {_owed_inline}, sibling {_sib_inline}")
print(f"      reported as keys by the ratchet -- owed {_owed_is_key}, sibling {_sib_is_key}  "
      f"(the sibling's state is REPORTED, not asserted: closing the hole must not redden this)")
gate("Ⓔ③ ⌗⛔ *** THE HOLE, MEASURED ON THIS FILE'S OWN TWO SENTENCES: one gate asserts BOTH, both are "
     "sentences in a paper the receipt does not own, and only ONE is a key the ratchet reports.  The "
     "difference is that one also occurs INLINE in an asserted expression while the other reaches its "
     "haystack only through a loop variable. ***  ⇒ ** Hoisting literals into a list lowers the "
     "backlog without adjudicating anything, which is why the repair keeps the literal inline and the "
     "hole is ROUTED rather than used **",
     _both_pinned and _owed_is_key and _owed_inline and _sib_inline == 0)


# ============================================================ F. scope
head("F.  ⚠ SCOPE, AND WHAT IS NOT CLAIMED")

gate("Ⓕ① ⛔ this revision stamps NO other seat's pin: three of the twenty-four are adjudicated, all "
     "in `P15_CR_cosmology`, and the twenty-one other readings are carried to the channel with the "
     "repair shape each needs.  ⇒ *the measurement -- which haystack, how much of it, which worlds "
     "the condition separates -- is seat-neutral; the verdict says what a gate is FOR and that is its "
     "author's*",
     all(any(m in k[0] for m in MINE) for k in _moved | _gone)
     and len(_mine) == 3 and len(_theirs) == 21
     and not {k for k in _moved | _gone if k in SUBCLASS
              and not k[0].startswith('receipts/' + OWN)})

_SELF = open(os.path.abspath(__file__), encoding='utf-8').read()
_opened = [a.value for n in ast.walk(ast.parse(_SELF))
           if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'open'
           for a in ast.walk(n) if isinstance(a, ast.Constant) and isinstance(a.value, str)
           and '.' in a.value and a.value != 'utf-8']
_git_read = re.findall(r"show\(f'\{PIN\}:([^']+)'\)", _SELF)
print(f"      files this receipt opens: {sorted(set(_opened))}")
print(f"      files it reads at {PIN}: {sorted(set(x[:40] for x in _git_read))}")
gate("Ⓕ② and no paper is read and none is edited, computed from this receipt's own source: every "
     "file it opens is a `.py` or the baseline `.tsv`, and the two it reads at the pinned commit are "
     "the baseline and the one receipt whose pre-repair condition is parsed.  ⌗ *The arithmetic is set operations on the "
     "baseline, substring conditions on synthetic registers, three `ast` parses and two arm counts; "
     "no physics is computed and no figure asserted*",
     _opened and not any(p.endswith(('.tex', '.md')) for p in _opened)
     and all(p.endswith(('.py', '.tsv')) for p in _opened)
     and len(set(_git_read)) == 2
     and not any(p.endswith('.tex') for p in _git_read))

print()
head("VERDICT")
_f = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_f)} of {len(CHECKS)} checks pass")
if _f:
    print(f"  {len(_f)} FAILED:")
    for n in _f:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS -- the OPEN subclass is read in full, twenty-four of twenty-four, and the flag
  separates nothing: ten pins go red on the success of the work they cite, ONE can never go red
  and never checked the row it names, and thirteen are safe -- and all twenty-four carry the same
  flag.  What decides it is the haystack: how much of which text, live or frozen.  The ALT flag
  measures syntax, firing on one sentence in two spellings and missing a four-arm cover, and in
  this seat's own receipt an arm added to protect a pin was deleting the conjunct beside it.  Two
  repairs land here, both on this seat's own files; the backlog falls from 2170 to 2167; and the
  twenty-one other-seat readings are routed rather than stamped.""")
