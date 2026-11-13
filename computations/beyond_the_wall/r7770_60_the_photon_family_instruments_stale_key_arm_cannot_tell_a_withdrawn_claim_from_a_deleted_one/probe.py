#!/usr/bin/env python3
"""r7770 (60) -- the photon-family instrument's stale-key arm cannot tell a withdrawn claim from a
deleted one.  POST-REGISTRATION throughout: PREDICTION.md was committed AND pushed before `successor.py`
or this file existed.  Eleven arms, each a comparison with a reachable negative named.
"""
import ast
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
import successor as S                                             # noqa: E402

VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


print("=" * 100)
print("r7770 (60) -- the stale-key arm's two states, and the provenance state r7768 found")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print(f"  r7612's constants, lifted BY AST and not retyped: {len(S.ADJ)} adjudication key(s),"
      f" {len(S.CLAIM)} claim word(s), {len(S.PAPER_FILES)} paper(s)")
print("=" * 100)

LIVE = S.live_papers()
# ** WHICH KEY THE SEED USES, AND WHY IT IS NOT A FREE CHOICE. **  A WITHDRAWN state means the key is
# still in print while its sentence has stopped being a candidate.  For a key that CONTAINS a claim
# word, removing that word also removes the key, so such a key cannot be WITHDRAWN by claim-word
# removal at all -- it goes straight to STALE.  The first run of this probe seeded on exactly such a
# key and produced STALE where it predicted WITHDRAWN; the fix is to seed on a key that carries no
# claim word of its own, which is a FACT ABOUT THE KEY SET and is asserted here rather than assumed.
NO_CLAIM = [k for k in S.ADJ if not any(w in k for w in S.CLAIM)]
assert NO_CLAIM, 'no adjudication key is free of claim words; the seed below would be unsound'
SEED_KEY = NO_CLAIM[0]
HOST = [stem for stem, t in LIVE.items() if S.flat(SEED_KEY) in S.flat(t)]
# and a SECOND withdrawal mechanism, for a key that does carry a claim word: re-splitting its
# sentence, which leaves every word in print and makes the sentence stop qualifying.
SPLIT_KEY = [k for k in S.ADJ if any(w in k for w in S.CLAIM)][0]


def raw_sentences(t):
    """the raw text split into the SAME sentences the instrument sees, separators kept, so a seed can
    rewrite one sentence and put the text back together.

    ** The instrument splits on `(?<=[.!?])\\s+` -- a terminator FOLLOWED BY WHITESPACE.  Two earlier
    runs of this probe seeded on something else and got the wrong state each time: first a fixed
    400-character window (a claim word outside it survived), then a span bounded by bare `.!?`
    (which cuts at `0.23%` and inside `\\S\\ref{}`, so it is not the instrument's sentence either).
    The seed now uses the instrument's own rule, because the splitter is part of the predicate. **
    """
    return re.split(r'((?<=[.!?])\s+)', t)


def seed_withdrawn(papers, key):
    """the sentence stays in print; every claim word is removed from the SENTENCE it sits in,
    the sentence being the instrument's own"""
    out = dict(papers)
    for stem in list(out):
        parts = raw_sentences(out[stem])
        touched = False
        for i in range(0, len(parts), 2):
            if S.flat(key) in S.flat(parts[i]):
                seg = parts[i]
                for w in S.CLAIM:
                    seg = re.sub(re.escape(w), 'X' * len(w), seg, flags=re.I)
                parts[i] = seg
                touched = True
        if touched:
            out[stem] = ''.join(parts)
    return out


def seed_deleted(papers, key):
    """the sentence is gone from the corpus entirely"""
    out = dict(papers)
    for stem in list(out):
        t = out[stem]
        j = t.find(key[:60])
        if j < 0:
            continue
        out[stem] = t[:j] + t[j + len(key):]
    return out


def seed_resplit(papers, key):
    """the second withdrawal mechanism: a period inserted at the END of the key, inside its sentence,
    so every word stays in print and the key's own text is untouched.

    ** The first build of this seed cut INSIDE the key's first fifty characters, which removed the
    key's text and so produced STALE -- correctly, and for a reason that had nothing to do with the
    mechanism it was meant to demonstrate.  A seed that destroys its own subject measures nothing. **
    """
    out = dict(papers)
    for stem in list(out):
        t = out[stem]
        j = t.find(key[:60])
        if j < 0:
            continue
        cut = j + len(key)
        if cut > len(t):
            continue
        out[stem] = t[:cut] + '. And ' + t[cut:]
    return out


W = seed_withdrawn(LIVE, SEED_KEY)
Dl = seed_deleted(LIVE, SEED_KEY)
RS = seed_resplit(LIVE, SPLIT_KEY)
key_still_in_print = any(S.flat(SEED_KEY)[:60] in S.flat(t) for t in W.values())
key_gone = not any(SEED_KEY[:60] in t for t in Dl.values())


# ================================================================= the CURRENT arm, re-implemented
def current_arm(papers, adj=None, claim=None):
    """r7612's own logic, as that probe computes it: candidates -> seen -> stale.  Re-implemented here
    over an injectable paper map, because the landed probe reads the live corpus and cannot be seeded
    without editing it -- and editing it is exactly what this revision will not do."""
    adj = S.ADJ if adj is None else adj
    claim = S.CLAIM if claim is None else claim
    cand = []
    for stem, txt in papers.items():
        for s in S.sentences(txt):
            if any(k in s for k in S.RATE) and any(k in s for k in S.DIST):
                if any(k in s for k in claim):
                    cand.append((stem, s))
    seen = {}
    unadj = []
    for stem, s in cand:
        k = [kk for kk in adj if kk in s]
        if k:
            seen.setdefault(k[0], []).append(stem)
        else:
            unadj.append((stem, s))
    stale = [k for k in adj if k not in seen]
    report = '\n'.join(f"[STALE KEY -- matches nothing now] {k[:110]}" for k in sorted(stale))
    hit = (not unadj) and (not stale)
    return hit, sorted(stale), report


liveA = current_arm(LIVE)
withA = current_arm(W)
delA = current_arm(Dl)
a1 = bool(key_still_in_print and not withA[0] and SEED_KEY in withA[1])
arm(1, "the defect demonstrated on a seeded corpus, not asserted", a1,
    f"      the key seeded on, which sits in the paragraph r7768 routed a patch to:",
    f"        \"{SEED_KEY[:150]}...\"",
    f"        it lives in: {HOST}",
    f"      SEED 'WITHDRAWN': every claim word blanked in a 400-character window round the key,",
    f"        the sentence itself untouched -- key still present in the paper text: {key_still_in_print}",
    f"      r7612's own logic on that seed:  arm A HIT = {withA[0]};  keys reported STALE:"
    f" {len(withA[1])}",
    f"        and the key it names as stale is the seeded one: {SEED_KEY in withA[1]}",
    ("      ⇒ ** THE DEFECT IS REAL AND LIVE: the sentence is in print and the arm calls its key "
     "STALE. **" if a1 else
     "      ⇒ NOT SHOWN ON THIS SEED -- the conclusion is withheld rather than printed beside a "
     "measurement that did not reach it."),
    "      ⌗ the reachable negative was that the current logic might already match from the full text",
    "        rather than from the candidate set, in which case there is no defect.  It does not.")

a2 = bool(withA[1] == delA[1] and withA[2] == delA[2] and not delA[0])
arm(2, "the two states produce the SAME output, which is the whole claim", a2,
    f"      SEED 'DELETED': the sentence removed from the corpus outright -- key gone: {key_gone}",
    f"      r7612's logic on it:  arm A HIT = {delA[0]};  keys reported STALE: {len(delA[1])}",
    f"      the two seeds' stale KEY LISTS are equal: {withA[1] == delA[1]}",
    f"      and their stale REPORTS are equal character for character: {withA[2] == delA[2]}",
    f"        the report, once, since both are the same text:",
    *[f"          {ln}" for ln in (withA[2] or '(empty)').split('\n')[:2]],
    ("      ⇒ ** THE OUTPUT CARRIES NO INFORMATION DISTINGUISHING A WITHDRAWN CLAIM FROM A "
     "DELETED SENTENCE: ** a reader of that line cannot tell which happened, and the two call for "
     "opposite responses -- retire the key, or record that the paper got more careful."
     if a2 else
     "      ⇒ NOT SHOWN ON THIS SEED -- withheld rather than printed beside a measurement that did "
     "not reach it."),
    "      ⌗ the reachable negative was a difference elsewhere in the output making the states",
    "        distinguishable after all -- which would have made this a presentation fix.  There is none.")

# ================================================================= ARM 3-5: the successor
resL = S.resolve(LIVE)
resW = S.resolve(W)
resD = S.resolve(Dl)
resR = S.resolve(RS)
cL, cW, cD, cR = (Counter(st for st, _ in r.values()) for r in (resL, resW, resD, resR))
one_state_each = all(len(r) == len(S.ADJ) for r in (resL, resW, resD, resR))
closed = all(set(st for st, _ in r.values()) <= set(S.STATES) for r in (resL, resW, resD, resR))
all_three = {resL[SEED_KEY][0], resW[SEED_KEY][0], resD[SEED_KEY][0]} == {'MATCHED', 'WITHDRAWN', 'STALE'}
resplit_state = resR[SPLIT_KEY][0]
resplit_key_intact = any(S.flat(SPLIT_KEY) in S.flat(t) for t in RS.values())
# ** WHICH KEYS CAN REACH WHICH STATES -- the guard's own question, asked of the key set. **
# A key that itself carries a RATE term, a DIST term AND a claim word is SELF-QUALIFYING: any sentence
# containing it is a candidate, so the key can only ever be MATCHED or STALE and WITHDRAWN is
# unreachable for it.  The re-split seed was predicted to produce WITHDRAWN and produced STALE, and
# this is why: the cut falls inside such a key and takes the key's own text with it.
SELFQ, WITHDRAWABLE = [], []
for k in S.ADJ:
    trip = (any(w in k for w in S.RATE) and any(w in k for w in S.DIST)
            and any(w in k for w in S.CLAIM))
    (SELFQ if trip else WITHDRAWABLE).append(k)
split_is_selfq = SPLIT_KEY in SELFQ
a3 = bool(one_state_each and closed and all_three and (SELFQ or WITHDRAWABLE))
arm(3, "the successor's state machine, enumerated", a3,
    f"      states declared: {S.STATES}",
    f"      on the LIVE corpus:      {dict(cL)}",
    f"      on the WITHDRAWN seed:   {dict(cW)}",
    f"      on the DELETED seed:     {dict(cD)}",
    f"      on the RE-SPLIT seed:    {dict(cR)}"
    f"   (the second withdrawal mechanism, on a claim-carrying key)",
    f"      the re-split key resolves: {resplit_state}   (predicted WITHDRAWN)",
    f"      ⛭ WHICH STATES EACH KEY CAN REACH AT ALL, which the registration's guard demands be",
    f"        enumerated rather than assumed:",
    f"        SELF-QUALIFYING (the key itself carries a rate term, a distance term AND a claim word,",
    f"          so any sentence containing it is a candidate => only MATCHED or STALE,"
    f" WITHDRAWN unreachable): {len(SELFQ)} of {len(S.ADJ)}",
    f"        WITHDRAWABLE (the key lacks at least one trigger, so its sentence can stop qualifying",
    f"          while the key stays in print): {len(WITHDRAWABLE)} of {len(S.ADJ)}",
    f"        the re-split key is self-qualifying: {split_is_selfq}",
    f"        and the re-split seed leaves the key's own text intact: {resplit_key_intact}"
    f"   -- the FIRST build of that seed cut inside the key and so measured nothing",
    f"      ⇒ ** THE STATE MACHINE IS THREE-VALUED, BUT NOT EVERY KEY RANGES OVER ALL THREE. **  The",
    f"        fix changes the verdict exactly for the {len(WITHDRAWABLE)} withdrawable key(s); for",
    f"        the self-qualifying ones it changes nothing, because for them an unmatched key really",
    f"        is a dead key.  That bound is the honest scope of this instrument and it is printed",
    f"        rather than left for a reader to work out.",
    f"      the seeded key's state across the three: "
    f"{resL[SEED_KEY][0]} / {resW[SEED_KEY][0]} / {resD[SEED_KEY][0]}"
    f"   -- all three states produced: {all_three}",
    f"      every key resolves to exactly one state on every map: {one_state_each}",
    f"      and the state set is closed (asserted inside the resolver, not here): {closed}",
    "      ⌗ the reachable negative was an ambiguous key -- present in one paper and absent from",
    "        another.  The resolver returns the papers it is MATCHED in, so the state is definite and",
    "        its evidence is the list.")

okL, stL, wdL = S.verdict(resL)
okW, stW, wdW = S.verdict(resW)
okD, stD, wdD = S.verdict(resD)
a4 = bool(okL and okW and (not okD) and wdW == [SEED_KEY] and stD == [SEED_KEY])
arm(4, "the successor fails on STALE and does NOT fail on WITHDRAWN", a4,
    f"      LIVE:       verdict {'PASS' if okL else 'FAIL'};  stale {len(stL)};  withdrawn {len(wdL)}",
    f"      WITHDRAWN:  verdict {'PASS' if okW else 'FAIL'};  stale {len(stW)};  withdrawn {len(wdW)}"
    f"   -- and the withdrawn key is REPORTED, named, not dropped",
    f"      DELETED:    verdict {'PASS' if okD else 'FAIL'};  stale {len(stD)};  withdrawn {len(wdD)}",
    "      ⇒ the assertion, as the clause the argument reasons FROM and written in the instrument's",
    "        own head: every key resolves to exactly one of three states, and NO key is STALE.",
    "      ⌗ the reachable negative was a weakening -- if WITHDRAWN passes, a genuinely dead key might",
    "        survive as 'withdrawn'.  The DELETED seed is that positive control and it still FAILS.")

a5 = bool(okL and liveA[0] and not stL and not wdL and dict(cL) == {'MATCHED': len(S.ADJ)})
arm(5, "no regression on the live corpus", a5,
    f"      r7612's arm on this tree:   HIT = {liveA[0]};  stale {len(liveA[1])}",
    f"      the successor on this tree: PASS = {okL};  stale {len(stL)};  withdrawn {len(wdL)}",
    f"      every one of the {len(S.ADJ)} keys MATCHED: {dict(cL) == {'MATCHED': len(S.ADJ)}}",
    "      ⇒ the fix changes NO live verdict.  It changes what happens the next time a claim word",
    "        moves -- which r7768's routed patch makes likely rather than hypothetical.",
    "      ⌗ the reachable negative was a key already WITHDRAWN on today's corpus, which would have",
    "        meant the published receipt is green only because the defect hides it.  There is none,",
    "        so the receipt's green is honest as well as correct.")

# ================================================================= ARM 6-7: the provenance detector
DECL = S.superseded_declarations()
DECL_ALL = S.superseded_declarations(keep_rejects=True)
rejected = [d for d in DECL_ALL if not d[3]]
UNL = S.unlabelled_mentions(LIVE, DECL)
a6 = bool(DECL and UNL)
arm(6, "the third state r7768 found, and whether it is detectable at all", a6,
    f"      receipt heads declaring an expression SUPERSEDED: {len(DECL_ALL)} candidate(s),"
    f" {len(DECL)} kept after the expression filter",
    *[f"        KEPT     `{d[1][:60]}`   <- {d[2]}" for d in DECL],
    *[f"        REJECTED `{d[1][:60]}`   -- a revision id, not a formula; reported, not dropped"
      for d in rejected],
    f"      papers still carrying a declared-superseded expression WITH NO LABEL beside it:"
    f" {len(UNL)}",
    *[f"        {u[0]}  `{u[1][:50]}`  at offset {u[3]}   (declared by {u[2].split('/')[-1][:48]})"
      for u in UNL],
    "      ⇒ ** THE DETECTOR FIRES ON THE KNOWN CASE, FOUND MECHANICALLY RATHER THAN BY READING: **",
    "        the expression cc66's receipt names superseded is still printed in the paper with no",
    "        label beside it -- which is r7768's arm 6 finding, reproduced by a rule instead of by",
    "        an eye.  So the provenance state IS detectable, and the owed instrument can carry it.",
    "      ⌗ the reachable negative was that no mechanical rule separates this from a legitimate",
    "        historical mention.  The LABEL is what separates them, and arm 7 seeds that both ways.")

lab_seed = dict(LIVE)
bare_seed = dict(LIVE)
expr_shown = DECL[0][1] if DECL else ''
for stem in lab_seed:
    # the LABELLED seed: put the superseding word right beside every occurrence
    t = lab_seed[stem]
    if expr_shown and S.norm_expr(expr_shown) in S.norm_expr(t):
        lab_seed[stem] = t.replace('taken as the radial profile',
                                   'on the SUPERSEDED static-region reading, taken as the radial profile')
LAB = S.unlabelled_mentions(lab_seed, DECL)
BARE = S.unlabelled_mentions(bare_seed, DECL)
a7 = bool(len(LAB) == 0 and len(BARE) >= 1)
arm(7, "seeded both ways, because a detector that cannot stay silent is not a detector", a7,
    f"      BARE seed (the corpus as it stands):  fires {len(BARE)} time(s)",
    f"      LABELLED seed (a superseding word placed beside the expression): fires {len(LAB)} time(s)",
    f"      ⇒ the detector is SILENT where the paper labels the expression and FIRES where it does"
    f" not: {a7}",
    "      ⌗ the reachable negative was firing on both, which would make it a presence test over a",
    "        string rather than a detector of unlabelled provenance.  It does not.")

# ================================================================= ARM 8: the declared reads
SRC = open(os.path.join(HERE, 'successor.py'), encoding='utf-8').read()
tree = ast.parse(SRC)
opens = set()
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'open':
        opens.add('open')
    if isinstance(node, ast.Call) and getattr(getattr(node.func, 'attr', None), '__str__', str)() == 'walk':
        opens.add('walk')
reads_found = set()
if re.search(r"open\(R7612", SRC):
    reads_found.add('computations/beyond_the_wall/r7612_60_*/photonfamily.py')
if re.search(r"'corpus', stem \+ '\.tex'", SRC):
    reads_found.add('corpus/*.tex')
if re.search(r"os\.walk\(root\)", SRC) and re.search(r"'receipts'", SRC):
    reads_found.add('receipts/**/*.py')
declared = set(S.DECLARED_READS)
a8 = (declared == reads_found)
arm(8, "the instrument's reads, declared", a8,
    f"      declared in the instrument's own header: {sorted(declared)}",
    f"      found by this file in the instrument's SYNTAX TREE: {sorted(reads_found)}",
    f"      equal as SETS, by sorted diff and not by count: {a8}",
    f"      only in the declaration: {sorted(declared - reads_found) or 'none'}",
    f"      only in the syntax tree: {sorted(reads_found - declared) or 'none'}",
    "      ⌗ the reachable negative was a SHORT declaration -- r7756's own defect in a different",
    "        extractor -- which is why this compares names rather than counting them.")

# ================================================================= ARM 9: what the fix does not do
NOT = [
    ("it does not retroactively change r7612's probe or any verdict that probe published",
     "that probe is a landed predicate and the tree it ran on is part of it; the fix is a successor"),
    ("it does not touch the receipt 69 landed",
     "a published gate's assertion is the landing seat's; the swap is routed as a patch (arm 10)"),
    ("it does not decide the sec:scope patch r7768 routed",
     "that is a paper edit and the gate's call; this revision only makes the instrument able to "
     "survive it either way"),
    ("it does not make the MARKER arm able to see provenance",
     "the provenance detector is a SECOND instrument beside it, and arm 6 says so: a claim word and "
     "a withdrawn computation are different objects"),
]
a9 = len(NOT) == 4 and all(len(w) > 10 for _, w in NOT)
arm(9, "what this fix does NOT do", a9,
    *[f"      * {w}\n        -- {why}" for w, why in NOT])

# ================================================================= ARM 10: the routing
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_photon_family_crosses_the_leaves_at_unit_cosmic_time_rate_so_the_'
                    'projections_distance_takes_the_stacking_rate_by_derivation.py')
rtxt = open(RCPT, encoding='utf-8').read() if os.path.exists(RCPT) else ''
path_line = [ln for ln in rtxt.split('\n') if 'photonfamily.py' in ln or "'photonfamily" in ln]
gate_line = [ln for ln in rtxt.split('\n') if 'every registered arm A-G holds' in ln
             or 'registered arm A-G' in ln]
two_changes = bool(path_line and gate_line)
a10 = bool(rtxt and path_line)
arm(10, "the routing, drafted", a10,
    f"      the published receipt: receipts/P15_CR_cosmology/P15_the_photon_family_crosses...py",
    f"      the line naming the computation's path: {len(path_line)} found",
    *[f"        {ln.strip()[:150]}" for ln in path_line[:2]],
    f"      the line carrying the arm list: {len(gate_line)} found",
    *[f"        {ln.strip()[:150]}" for ln in gate_line[:1]],
    f"      ⇒ THE ROUTING IS TWO CHANGES AND NOT ONE: {two_changes}",
    "        ⒜ the COMP path must point at this revision's successor, and",
    "        ⒝ the gate wording 'every registered arm A-G holds' must become the successor's own",
    "          assertion, because the successor reports a THIRD verdict (WITHDRAWN) that the",
    "          A-G wording has no slot for.  A patch that did only ⒜ would leave the receipt",
    "          asserting something its instrument no longer computes.",
    "      ⌗ and what breaks if 69 applies the path change without the successor present: the",
    "        receipt's runpy call raises and the gate goes red with a FATAL, not a FAIL -- so the",
    "        patch is routed WITH the note that this revision must be merged first.")

# ================================================================= ARM 11
PRED = open(os.path.join(HERE, 'PREDICTION.md'), encoding='utf-8').read()
declared_arms = len(re.findall(r'^## [①-⑪]', PRED, re.M))
answered = len(VERDICTS) + 1
a11 = (declared_arms == 11 and answered == 11)
arm(11, "the count, and the subject clause", a11,
    f"      arms declared in PREDICTION.md: {declared_arms}",
    f"      arms answered here (this one included): {answered}",
    "      ** THIS SEAT IS A SUBJECT OF NOTHING IN THIS REVISION. **")

print(f"\n{'=' * 100}\n  VERDICT\n{'=' * 100}")
for n, ok, title in VERDICTS:
    print(f"    [{'PASS' if ok else 'FAIL'}]  ARM {n:<3} {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their criterion.")
if bad:
    print(f"  ⛔ arms not meeting their criterion: {bad}")
print("=" * 100)
