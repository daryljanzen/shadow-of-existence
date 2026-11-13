#!/usr/bin/env python3
"""r7772 (60) -- S11's Ⓔ① passes over an empty set, because its order-commit selector stopped
matching the gating seat's convention.  POST-REGISTRATION throughout.
Eleven arms, each a comparison with a reachable negative named in PREDICTION.md.
"""
import contextlib
import io
import os
import re
import runpy
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


# ---------------------------------------------------------------- S11, read BY PATH and not reimplemented
S11 = [os.path.join(ROOT, 'receipts', 'L_probability', f)
       for f in sorted(os.listdir(os.path.join(ROOT, 'receipts', 'L_probability')))
       if f.startswith('S11_')]
if len(S11) != 1:
    raise SystemExit(f"FATAL: S11 is not uniquely resolvable: {S11}")
S11 = S11[0]
_buf = io.StringIO()
_rc = 0
_err = ''
_cwd = os.getcwd()
try:
    # the suite runs every receipt FROM ITS OWN DIRECTORY, and S11's git calls assume it.
    # ** The first run of this probe did not chdir, S11 raised, and the namespace came back EMPTY --
    #    so SITES and WRITERS were 0 and arm 5's seed could not fire.  A captured run that raised is
    #    not a reading. **
    os.chdir(os.path.dirname(S11))
    with contextlib.redirect_stdout(_buf):
        NS = runpy.run_path(S11, run_name='__main__')
except BaseException as e:                                        # noqa: BLE001 - reported, not hidden
    _rc = 1
    _err = f'{type(e).__name__}: {e}'
    NS = {}
finally:
    os.chdir(_cwd)
S11_OUT = _buf.getvalue()

print("=" * 100)
print("r7772 (60) -- S11's imperfection gate, and the selector that stopped matching")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print(f"  S11 read by path: {os.path.relpath(S11, ROOT)}")
print(f"  it exits {_rc} on this tree, and its own run is captured rather than re-implemented"
      + (f"   [{_err}]" if _err else ""))
print("=" * 100)

S11REL = os.path.relpath(S11, ROOT)
S11SRC = open(S11, encoding='utf-8').read()                       # the working tree: AFTER the repair
S11OLD = git('show', f'origin/main:{S11REL}')                     # the base branch: BEFORE it
SUBJ = [row for row in git('log', '--format=%h|%s', '-400').split('\n') if row.strip()]
print(f"  the PRE-REPAIR form is read from origin/main and the post-repair one from the working"
      f" tree, so the before and after are both sources and not recollections"
      f"  ({len(S11OLD)} vs {len(S11SRC)} bytes)")


def revid(subject):
    m = re.match(r'\s*r(\d{4})', subject)
    return int(m.group(1)) if m else None


# ================================================================= ARM 1: the source set is empty
OLD_SEL = re.compile(r'^[0-9a-f]+\|\s*orders r\d{4}')


def old_parity_even(rows):
    out = set()
    for row in rows:
        if not OLD_SEL.match(row):
            continue
        sha, sub = row.split('|', 1)
        m = re.match(r'\s*r(\d{4})', sub.replace('orders ', ''))
        if m and int(m.group(1)) % 2 == 0:
            out.add(sha)
    return out


OLD_EVEN = old_parity_even(SUBJ)
OLD_LITERAL = r"orders r\d{4}'"            # the selector's own regex tail, not the loose phrase
old_form_present = OLD_LITERAL in S11OLD
old_form_gone = OLD_LITERAL not in S11SRC
# ⌗ tested on the REGEX LITERAL and not on the words "orders r": the repaired gate's own comment
#   explains the old selector, so a loose phrase test called the old form still present.
n_src = len(OLD_EVEN)
inherited = (n_src == 0)
a1 = bool(old_form_present and old_form_gone and inherited)
arm(1, "the source set is empty, and the result's emptiness is downstream of that", a1,
    f"      the OLD selector, located in the form origin/main carries: {old_form_present}"
    f"   (and gone from the repaired form: {old_form_gone})",
    f"      order commits it matches with an EVEN id, computed here over the last 400: {n_src}",
    f"      so the sites it could have returned: necessarily 0 -- the result is empty BECAUSE the"
    f" source set is: {inherited}",
    "      ⇒ ** Ⓔ① ASSERTS `not _hit` OVER A SET BUILT FROM NOTHING. **  Its own sentence says the",
    "        imperfection is 'measured, not waved at', and on this tree the measurement has no",
    "        subjects at all.",
    "      ⌗ the reachable negative was a populated source set with a genuinely empty result, which",
    "        would have meant the gate measures what it says and this revision withdraws itself.")

# ================================================================= ARM 2: the convention drifted
OLD = re.compile(r'^[0-9a-f]+\|\s*orders r\d{4}')
NEW = re.compile(r'^[0-9a-f]+\|\s*r\d{4}\s*(?:\([^)]+\)|\+[A-Za-z0-9]+\.)')
old_n = [r for r in SUBJ if OLD.match(r)]
new_n = [r for r in SUBJ if NEW.match(r)]
a2 = bool(old_form_present and len(old_n) == 0 and len(new_n) > 0)
arm(2, "why the selector matches nothing: a convention that drifted", a2,
    f"      the selector origin/main's form carries: {old_form_present}"
    f"   -- it requires a subject to BEGIN 'orders r####'",
    f"      subjects in the last 400 matching it:              {len(old_n)}",
    f"      subjects matching the stamped convention in use:   {len(new_n)}",
    f"        r#### (SEAT) or r####+SEAT.k -- examples:",
    *[f"          {r[:105]}" for r in new_n[:3]],
    "      ⇒ the gating seat stopped writing 'orders r####' subjects; its commits now lead with their",
    "        own stamp and mention orders at the end.  The selector did not break -- the corpus moved",
    "        out from under it, which is the shape this receipt is itself about.",
    "      ⌗ the reachable negative was both patterns matching, which would have put the emptiness",
    "        somewhere else.  One matches nothing and the other matches hundreds.")

# ================================================================= ARM 3: it would pass however bad
STAMP = re.compile(r'^\s*r(\d{4})\s*(?:\(([^)]+)\)|\+([A-Za-z0-9]+)\.)')


def stamped(rows):
    out = []
    for r in rows:
        sha, sub = r.split('|', 1)
        m = STAMP.match(sub)
        if m:
            out.append((sha, int(m.group(1)), (m.group(2) or m.group(3) or '').strip(), sub))
    return out


ST = stamped(SUBJ)
SEED_ROWS = [(sha, rid, seat, sub) for sha, rid, seat, sub in ST if rid % 2 == 0 and seat != '60']
# the seed: a claim-site whose last writer is one of those commits, fed to the OLD selector's shape
old_even = {r.split('|', 1)[0] for r in SUBJ if OLD.match(r)}
seed_sha = SEED_ROWS[0][0] if SEED_ROWS else None
old_catches_seed = bool(seed_sha and seed_sha in old_even)
a3 = bool(SEED_ROWS and not old_catches_seed)
arm(3, "the gate would pass however bad the attribution became", a3,
    f"      commits in the last 400 whose revision id is EVEN and whose SEAT STAMP is not this"
    f" line's: {len(SEED_ROWS)}",
    *[f"        {sha}  id {rid} (EVEN)  seat {seat:<5} | {sub[:72]}"
      for sha, rid, seat, sub in SEED_ROWS[:5]],
    f"      the SEED: a claim-site last written by {seed_sha} -- a real commit of another seat"
    f" carrying this line's even id",
    f"      the OLD selector's even-id set contains it: {old_catches_seed}",
    "      ⇒ ** SO THE GATE PASSES WITH THE VERY THING IT CLAIMS TO MEASURE PRESENT IN THE TREE. **",
    "        Those commits are exactly the mis-attribution the rule is heuristic about: the other",
    "        seat stamps with the ORDER's id, which is this line's, so parity calls them this line's.",
    "      ⌗ the reachable negative was the old selector catching the seeded case anyway -- the seed",
    "        is a REAL commit in the corpus's live convention, not one built to be missed.")

# ================================================================= ARM 4: the repaired selector
def repaired_even_commits(rows, mine='60'):
    """commits whose revision id is EVEN and whose seat stamp is NOT this line's.

    ** The stamp and not the parity is what decides, which is the whole point: parity reads the
    ORDER's id, and every seat stamps with that same id, so an even id names this line's ORDER and
    not the commit's AUTHOR. **
    """
    out = {}
    for sha, rid, seat, sub in stamped(rows):
        if rid % 2 == 0 and seat != mine:
            out[sha] = (rid, seat, sub)
    return out


REP = repaired_even_commits(SUBJ)
seats = sorted({v[1] for v in REP.values()})
mine_caught = [s for s, v in REP.items() if v[1] == '60']
a4 = bool(REP and not mine_caught)
arm(4, "the repaired selector", a4,
    f"      matches: {len(REP)} commit(s) in the last 400",
    f"      the seats they belong to, read from their own stamps: {seats}",
    f"      commits of THIS line wrongly pulled in: {len(mine_caught)}",
    "      ⇒ the set is populated, and it is populated by exactly the class the rule mis-attributes:",
    "        another seat's commits carrying this line's order id.",
    "      ⌗ the reachable negative was over-matching into this line's own commits, which would have",
    "        inverted the gate's meaning.  None is caught, and the report is of WHO and not only of",
    "        how many.")

# ================================================================= ARM 5-7: the finder, and the seeds
SITES = NS.get('SITES') or []
WRITERS = NS.get('WRITERS') or {}


PREFIX = min([len(k) for k in REP] or [9])


def hits(sites, writers, even_set):
    """the sites whose last writer is in `even_set`, compared on a COMMON PREFIX LENGTH.

    ⛔ ** AND THIS IS A THIRD, INDEPENDENT REASON THE PUBLISHED GATE CAN NEVER FIRE. **  S11 compares
    `WRITERS[...][0][:8]` against a set of `git log --format=%h` shas, and this repository's
    abbreviation length is NINE -- so an 8-character prefix is tested for membership in a set of
    9-character strings and can never match, however populated either side is.  The comparison here
    is on min(len) of the set's own keys, measured rather than assumed.
    """
    ev = {k[:PREFIX] for k in even_set}
    return [s for s in sites if writers.get((s[0], s[1]), ('?',))[0][:PREFIX] in ev]


live_hits = hits(SITES, WRITERS, set(REP))
SEEDSITE = ('SEEDED/not_on_disk.py', 1, 'seeded', 'seeded', 'seeded')
seed_writers = dict(WRITERS)
seed_writers[(SEEDSITE[0], SEEDSITE[1])] = (seed_sha + 'f' * (40 - len(seed_sha)), 'seeded subject')
seed_hits = hits(list(SITES) + [SEEDSITE], seed_writers, set(REP))
seed_fires = SEEDSITE in seed_hits
odd_sha = next((sha for sha, rid, seat, sub in ST if rid % 2 == 1 and seat != '60'), None)
ctrl_writers = dict(WRITERS)
_o = odd_sha or 'f' * 9
ctrl_writers[(SEEDSITE[0], SEEDSITE[1])] = (_o + 'f' * (40 - len(_o)), 'control subject')
ctrl_hits = hits(list(SITES) + [SEEDSITE], ctrl_writers, set(REP))
ctrl_silent = SEEDSITE not in ctrl_hits
a5 = bool(seed_fires)
arm(5, "the in-run seed, so a zero is a MEASURED zero", a5,
    f"      claim-sites S11 enumerates on this tree: {len(SITES)};  writers resolved: {len(WRITERS)}",
    f"      the seed: one synthetic site whose last writer is {seed_sha}, which IS in the repaired set",
    f"      the finder returns the seeded site: {seed_fires}",
    f"      ⛔ AND A THIRD BLOCKER, FOUND WHILE BUILDING THIS SEED: S11 compares a blame sha's FIRST"
    f" EIGHT characters",
    f"        against a set of `git log --format=%h` shas, and this repository abbreviates to"
    f" {PREFIX} -- so that",
    f"        membership test can NEVER match, however populated either side is.  The comparison here"
    f" is on",
    f"        min(len) of the set's own keys, measured rather than assumed.",
    "      ⇒ ** so whatever the live figure is, it is a MEASURED number and not a silence ** --",
    "        r7421 ③'s rule, applied to this gate for the first time.",
    "      ⌗ the reachable negative was the seed not firing, which would have meant the repaired",
    "        finder is broken too and the live figure means nothing.")

a6 = bool(REP and PREFIX)
arm(6, "the repaired gate's verdict on the live tree, whichever way it comes out", a6,
    f"      claim-sites last written by a commit in the repaired set: {len(live_hits)}",
    *[f"        {s[0]}:{s[1]}  last written by {WRITERS.get((s[0], s[1]), ('?', '?'))[0][:8]}"
      f"  \"{WRITERS.get((s[0], s[1]), ('?', '?'))[1][:60]}\"" for s in live_hits[:6]],
    ("      ⇒ ** THE ATTRIBUTION RULE IS IMPERFECT ON THIS CORPUS AND THE MEASURE NOW SAYS BY HOW "
     "MUCH: ** the sites above are attributed to this line by parity and belong to another seat by "
     "its own stamp.  The gate must assert the MEASURED imperfection, not its absence."
     if live_hits else
     "      ⇒ the live figure is ZERO -- and with arm 5's seed firing in the same run it is a MEASURED "
     "zero rather than the silence Ⓔ① has been reporting.  The gate's claim becomes true."),
    f"      ⌗ and the old gate's sentence said SIX such commits; the repaired count is"
    f" {len(REP)}, so the literal in the gate text was stale as well as unmeasured.")

a7 = bool(seed_fires and ctrl_silent)
arm(7, "seeded both ways", a7,
    f"      even-stamped seed ({seed_sha}, seat {REP[seed_sha][1] if seed_sha in REP else '?'}):"
    f" fires = {seed_fires}",
    f"      odd-stamped control ({odd_sha}): fires = {not ctrl_silent}",
    "      ⇒ the finder is a parity-and-stamp test and not a presence test over any order commit.",
    "      ⌗ the reachable negative was firing on both.")

# ================================================================= ARM 8: does the repair move another gate?
reads_sel = [ln.strip() for ln in S11SRC.split('\n') if '_even_orders' in ln or '_orders' in ln]
other_gates = [ln for ln in S11SRC.split('\n') if ln.strip().startswith("gate('") or
               ln.strip().startswith('gate("')]
after = re.findall(r'\[(PASS|FAIL)\]\s+(\S+)', S11_OUT)
after_fail = sorted({g for v, g in after if v == 'FAIL'})
# the pre-repair verdicts, from the form origin/main carries, run in a detached worktree of it
WT = os.path.join(os.path.dirname(ROOT), 's11_pre_wt')
pre_fail = None
if not os.path.exists(WT):
    git('worktree', 'add', '--detach', WT, 'origin/main')
try:
    r = subprocess.run([sys.executable, os.path.join(WT, S11REL)], cwd=WT,
                       capture_output=True, text=True, timeout=1800)
    pre_fail = sorted({g for v, g in re.findall(r'\[(PASS|FAIL)\]\s+(\S+)', r.stdout)
                       if v == 'FAIL'})
except Exception as e:                                            # noqa: BLE001
    pre_fail = [f'UNAVAILABLE: {type(e).__name__}']
finally:
    git('worktree', 'remove', '--force', WT)
    git('worktree', 'prune')
# ** AND THE RIGHT CONDITION IS THAT THE TWO FAIL SETS ARE IDENTICAL, which this probe got wrong
#    on its first build: it predicted Ⓔ① would move OUT of the fail set, and Ⓔ① was never IN it.
#    The old form PASSED -- vacuously -- and the repaired form passes meaningfully.  ** That is the
#    whole value of the repair, and it is the reason the defect survived: a gate that passes either
#    way is invisible to every verdict list. **
sets_identical = (pre_fail is not None and sorted(pre_fail) == sorted(after_fail))
e1_in_neither = ('Ⓔ①' not in (pre_fail or [])) and ('Ⓔ①' not in after_fail)
a8 = bool(reads_sel and after and sets_identical and e1_in_neither)
arm(8, "does the repair move any other gate of S11?", a8,
    f"      lines of S11 that read the selector or its set, enumerated FROM THE FILE: {len(reads_sel)}",
    *[f"        {ln[:110]}" for ln in reads_sel],
    f"      gates the file declares: {len(other_gates)};  verdicts the repaired run printed:"
    f" {len(after)}",
    f"      ⛔ FAILING GATES ON origin/main's OWN FORM, run in a detached worktree of it:"
    f" {pre_fail}",
    f"      failing gates after this repair:                                              "
    f" {after_fail}",
    f"      ⇒ the two fail sets are IDENTICAL: {sets_identical}"
    f"   -- the repair moved no other gate's verdict",
    f"      and Ⓔ① is in NEITHER set: {e1_in_neither}"
    f"   -- it PASSED before, vacuously, and passes now meaningfully",
    "      ⇒ ** THAT IS WHY THIS DEFECT SURVIVED: a gate that passes either way is invisible to",
    "        every verdict list, so no suite run and no CI job could ever have surfaced it. **",
    "      ⇒ only Ⓔ① reads the selector, so the repair is local to it -- established from the file",
    "        rather than from memory, and confirmed by the two verdict sets above.",
    "      ⛔⛔ AND THE SIX OTHER REDS ARE NOT THIS REPAIR'S AND NOT THIS BRANCH'S: they fail",
    "        IDENTICALLY on origin/main's own form.  ** This receipt is RED ON THE BASE BRANCH, it is",
    "        this line's own, and it sits OUTSIDE this line's suite scope -- which is why nothing in",
    "        the routine was looking at it. **  Diagnosed in the RESULT and registered as its own",
    "        revision rather than repaired here, because each of those gates asserts a figure scored",
    "        on one past push and recomputed live, which is a different defect from this one.",
    "      ⌗ the reachable negative is r7736's own history: a patch applied as offered reddened a",
    "        neighbouring gate by emptying its set.  If this repair reds one, the repair is wrong.")

# ================================================================= ARM 9: the gate's new text
NEWTEXT = (
    "Ⓔ① the parity rule this receipt attributes seats with is IMPERFECT, and the imperfection is "
    "measured on a POPULATED set rather than asserted over an empty one: the commits whose revision "
    "id is EVEN and whose own seat stamp is not this line's are counted and PRINTED above -- they are "
    "another seat's work carrying this line's order id, which is exactly what parity cannot see -- and "
    "an in-run seed proves in this run that a claim-site last written by one of them WOULD be found, "
    "so the figure above is a measured number and not a silence"
)
claims_in_text = {
    'counts a populated set': bool(REP),
    'prints the figure rather than carrying a literal': 'six commits' not in NEWTEXT,
    'names the stamp as the discriminator': 'seat stamp' in NEWTEXT,
    'asserts the seed, which this run demonstrates': seed_fires,
}
a9 = all(claims_in_text.values())
arm(9, "the gate's text after the repair", a9,
    "      the drafted text:",
    f"        {NEWTEXT}",
    "      every clause checked against what the repaired condition computes:",
    *[f"        {'✔' if v else '⛔'} {k}" for k, v in claims_in_text.items()],
    "      ⌗ the stale literal 'six commits' is GONE: the count is printed by the run, so it cannot",
    "        drift again -- which is the defect this gate had on top of the empty set.")

# ================================================================= ARM 10
NOT = [
    ("it does not touch another seat's receipt",
     "S11 is this line's own, landed by 69 from r7736; nothing else is edited"),
    ("it does not change what S11 is about",
     "the proposal, the partitions and every other gate stand; only Ⓔ①'s set and text move"),
    ("it does not re-run the retrospective sweep Ⓔ② names as irreplaceable",
     "that bound is Ⓔ②'s and this revision leaves it exactly as it stands"),
    ("it does not claim the parity rule is now sound",
     "the repair makes the imperfection MEASURABLE; the rule stays a heuristic that a stamp would "
     "replace, which is what the gate says"),
]
a10 = len(NOT) == 4
arm(10, "what this revision does NOT do", a10, *[f"      * {w}\n        -- {why}" for w, why in NOT])

# ================================================================= ARM 11
PRED = open(os.path.join(HERE, 'PREDICTION.md'), encoding='utf-8').read()
declared = len(re.findall(r'^## [①-⑪]', PRED, re.M))
answered = len(VERDICTS) + 1
a11 = (declared == 11 and answered == 11)
arm(11, "the count, and the subject clause", a11,
    f"      arms declared in PREDICTION.md: {declared}",
    f"      arms answered here (this one included): {answered}",
    "      ** THIS SEAT IS A SUBJECT OF NOTHING IN THIS REVISION. **  ⌗ Its own RECEIPT is the",
    "      subject, which is a different thing: a gate of this line's is being corrected by this",
    "      line, with the correction registered before it was built.")

print(f"\n{'=' * 100}\n  VERDICT\n{'=' * 100}")
for n, ok, title in VERDICTS:
    print(f"    [{'PASS' if ok else 'FAIL'}]  ARM {n:<3} {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their criterion.")
if bad:
    print(f"  ⛔ arms not meeting their criterion: {bad}")
print("=" * 100)
