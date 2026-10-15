#!/usr/bin/env python3
r"""S39 -- THE ITEM ROUTED TO THIS SEAT SINCE `r7289`, AND IT WAS NOT A COUNTER RACE.

** WHAT WAS ROUTED. **  `check_revision_collisions` has been red on the trunk and in this line's
every run since `r7289`, routed to this seat and re-stated as not withdrawn at `r7295`, `r7297`,
`r7299`, `r7303`, `r7307` and `r7309`.  *Six orders carried the same line: still yours, not
withdrawn.*

** ⛔⛭⛭⛭ AND THE DIAGNOSIS IS NOT THE ONE THE GATE'S OWN NARRATIVE OFFERS. **  *The gate is about
two lines numbering from one counter, and the remedy it names is a parity BAND.*  ** Neither
collision is that. **
  ⓘ `r7285`: the ordering line's ORDER and its RULING -- two commits, one session, correctly read
     as one line -- against a THIRD session's commit `r7285 ①: ...`, which is that seat's ANSWER to
     order ① with the order's own number in front of it.
  ⓙ `r7287`: the same, exactly.
  => *** THE BAND IS PARITY OVER TWO LINES, AND A SEAT ANSWERING AN ORDER IS A THIRD LINE.  The
      answering seat is not picking a number from the front at all -- it is CITING the order it
      answers, in the one syntax the claim-reader cannot tell from a claim. ***

** ✔⛭⛭ AND THE PREVENTION WAS ALREADY IN THE FILE, ALREADY IN USE, AND ALREADY PROVEN ONCE. **  *The
SUFFIX form `rNNNN+<seat>` is a different identifier by this gate's own `r3100a` rule; three seats
write it already; and `cc66` moved to it at `r7225+cc66.164` after the `r7185` instance of this exact
shape.*
  => ** So the repair is a CONVENTION for answering commits and not a new band -- and making it the
      ordered form is the gating seat's to order, because it binds other seats.  Routed with this
      evidence rather than taken. **
  ⌈ ** What IS taken here: ** *the two instances are NAMED in the baseline with their shas, which
    is this list's own rule and the third and fourth time this shape has been named in it; and both
    forms are SEEDED in the gate, so an edit that loses the distinction fails.*
  ⌊ ⚠ *And the limit, stated rather than stepped around: a gate asserting the ABSENCE of a
    historical collision can never go green once one has happened.  **The only half that can be green
    is the NEW-collision half** -- which is what the baseline is for, and why naming an instance is
    the repair here and not an evasion.*

⚠ WHAT THIS CANNOT SETTLE is at the foot.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
os.environ.setdefault('NODE', 'ci')
import check_revision_collisions as G                        # noqa: E402  -- the routed gate itself

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


# the two ids and the three commits each, read out of history rather than restated
PAIRS = {'r7285': ('8afa9ed3', ('fadf708d', '311e7ac6')),
         'r7287': ('e7b7c7ab', ('a2555f4f', '566a97fc'))}

# ⛔⛭⛭⛭ r7370: ** THE SHAS WERE PINNED AND THE FACT READ OFF THEM WAS NOT. **  *`Ⓑ①` below took each
#   commit's session marker out of `G._SESSION`, which the collision gate fills by WALKING THE WHOLE
#   HISTORY REACHABLE FROM `HEAD`.  On a shallow clone that walk stops at the horizon -- the gate's
#   own comment says it was once "reporting green over 8 per cent of the corpus's revision history"
#   -- and these six commits sit some eighty revisions back.*
#   ⌈ *So the map has no entry for them, `_sa` reads empty, `bool(_sa)` is False and the gate fails
#     -- on the runner and not here, where the clone is full.  Red on five lines for five pushes,
#     green on this tree every time, with nothing in the tree to explain it.*
#   ⇒ *** A PIN IS ONLY AS GOOD AS WHAT RESOLVES IT.  `S29`'s reference OVER-resolved -- a string
#       match that later commits citing the revision join -- and this one UNDER-resolves: a sha the
#       environment may not reach.  Both wanted the fact committed beside the measurement. ***
#   ⌊ *The markers are stored here, which is `r7365` ②'s rule.  Where the object IS present they are
#     CHECKED against what the commit says, so the stored data cannot drift unchallenged; where it is
#     absent the stored value carries the claim and the absence is REPORTED.*
SESSIONS = {
    '8afa9ed3': 'https://claude.ai/code/session_01YGJEEs8cWKLi4PTi1bxhuK',
    'fadf708d': 'https://claude.ai/code/session_01XXeapZm1snJuJTXbjf7Wtv',
    '311e7ac6': 'https://claude.ai/code/session_01XXeapZm1snJuJTXbjf7Wtv',
    'e7b7c7ab': 'https://claude.ai/code/session_01YGJEEs8cWKLi4PTi1bxhuK',
    'a2555f4f': 'https://claude.ai/code/session_01XXeapZm1snJuJTXbjf7Wtv',
    '566a97fc': 'https://claude.ai/code/session_01XXeapZm1snJuJTXbjf7Wtv',
}
_SESS_RE = __import__('re').compile(r'^Claude-Session:\s*(\S+)', __import__('re').M)
_UNREACHED = []


def session_of(sha):
    """the session marker of a PINNED commit: checked against the commit where this clone reaches
    it, taken from the stored value where it does not, and the absence reported either way."""
    _body = subprocess.run(['git', 'log', '-1', '--format=%B', sha], cwd=ROOT,
                           capture_output=True, text=True, errors='replace').stdout
    _m = _SESS_RE.search(_body)
    if _m:
        assert _m.group(1) == SESSIONS[sha], (
            f'{sha} says {_m.group(1)} and this file stores {SESSIONS[sha]}')
        return _m.group(1)
    _UNREACHED.append(sha)
    return SESSIONS[sha]


def _subj(sha):
    return subprocess.run(['git', 'log', '-1', '--format=%s', sha], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()


print()
print('=' * 100)
print('S39 -- the routed collision item: an ANSWER read as a CLAIM, and the prevention already in use')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE GATE IS GREEN, AND WHAT MADE IT GREEN IS A NAMING AND NOT A RENUMBERING ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rc = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_revision_collisions.py')],
                     cwd=ROOT, capture_output=True, text=True,
                     env=dict(os.environ, NODE='60'))
_green = _rc.returncode == 0 and 'no NEW revision-number collision' in _rc.stdout
print(f'      the routed gate, run as this line runs it: exit {_rc.returncode}; '
      f'"no NEW collision" in its output: {"no NEW revision-number collision" in _rc.stdout}')
gate(f'Ⓐ① ⛭⛭⛭ ** THE ITEM ROUTED SINCE `r7289` IS CLOSED: the gate exits `{_rc.returncode}` and says '
     f'in its own words that there is no NEW collision. **  *Six orders carried it forward as still '
     f'this seat\'s; what it needed was a diagnosis and a naming, and neither of those is a '
     f'renumbering*',
     _green)

_still_claimed = {}
for _rev, (_ans, _own) in PAIRS.items():
    _still_claimed[_rev] = [s for s in (_ans,) + _own if _subj(s).startswith(_rev)]
_all_named = all(_rev in G.BASELINE for _rev in PAIRS)
_all_present = all(len(v) == 3 for v in _still_claimed.values())
print(f'      in the baseline: {sorted(r for r in PAIRS if r in G.BASELINE)}; '
      f'commits still carrying each id: { {k: len(v) for k, v in _still_claimed.items()} }')
gate(f'Ⓐ② ⛭⛭ and NOTHING IS RENUMBERED, which is this list\'s own rule: both ids are named in the '
     f'baseline (`{_all_named}`) and all `3` commits of each still carry the id in their subject '
     f'(`{_all_present}`).  ** `r3563`\'s reason, and the one the baseline gives twice already: '
     f'renumbering either side breaks every citation written to it.  A named collision is a FACT '
     f'recorded, and the gate\'s job is the next one **',
     _all_named and _all_present)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  AND THE SHAPE IS AN ANSWER IN CLAIM SYNTAX, READ OFF THE COMMITS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
G.collisions()        # populates the gate's own session map from the commits
_shape = {}
for _rev, (_ans, _own) in PAIRS.items():
    _sa = session_of(_ans)
    _so = [session_of(s) for s in _own]
    _shape[_rev] = (bool(_sa) and all(_so) and _sa not in _so and len(set(_so)) == 1,
                    G._same_line(_own[0], _own[1]),
                    not G._same_line(_ans, _own[0]) and not G._same_line(_ans, _own[1]))
    print(f'      {_rev}: answering session differs from the ordering line\'s {_shape[_rev][0]}; '
          f'the ordering line\'s two commits are ONE line {_shape[_rev][1]}; '
          f'the answer is NOT that line {_shape[_rev][2]}')
print(f'      the pinned commits this clone does not reach: {len(_UNREACHED)} of '
      f'{len(SESSIONS)} -- REPORTED, and where it does reach one the stored marker is CHECKED '
      f'against what the commit says rather than trusted')
gate(f'Ⓑ① ⛔⛭⛭⛭ and the shape is read off the COMMITS and not from the gate\'s narrative: in both, '
     f'the two commits of the ordering line are one session and are correctly read as ONE line, and '
     f'the third commit is ANOTHER session answering that order.  ** So the collision is not two '
     f'lines picking from one counter --- which is what the band is for --- but a THIRD line citing '
     f'the order it answers.  The band is parity over TWO halves and has no half for an answering '
     f'seat **',
     all(all(v) for v in _shape.values()))

_bare = 'r7285 ①: the subject rule rewritten in the quote-pin header'
_sfx = 'r7285+69 ①: the subject rule rewritten in the quote-pin header'
_bare_claims = bool(G.claim_of(_bare)) and G.claim_of(_bare).group(1) == 'r7285'
_sfx_claims = bool(G.claim_of(_sfx))
print(f'      the bare form reads as a claim on r7285: {_bare_claims}; '
      f'the suffix form reads as a claim: {_sfx_claims}')
gate(f'Ⓑ② ✔⛭⛭⛭ ** AND THE PREVENTION IS CHECKED, NOT PROPOSED: ** the bare form reads as a claim on '
     f'the order\'s id (`{_bare_claims}`) and the SUFFIX form does not (`{not _sfx_claims}`) --- a '
     f'different identifier by this gate\'s own `r3100a` rule.  *Both are now SEEDED in the gate in '
     f'opposite directions, so an edit that loses the distinction fails there rather than here.*  '
     f'** The whole repair is that one of two forms reads as a claim and the other does not **',
     _bare_claims and not _sfx_claims)

_log = subprocess.run(['git', 'log', '--format=%s', 'origin/main'], cwd=ROOT,
                      capture_output=True, text=True).stdout
_sfx_used = len(set(re.findall(r'^(r\d{3,5}\+[A-Za-z0-9.]+)', _log, re.M)))
_seats = sorted({m.split('.')[0] for m in re.findall(r'^r\d{3,5}\+([A-Za-z0-9.]+)', _log, re.M)})
print(f'      the suffix form is already in use on the trunk: {_sfx_used} distinct identifiers '
      f'across seats {_seats}')
gate(f'Ⓑ③ ⛭⛭ and it is ALREADY IN USE rather than newly invented: `{_sfx_used}` distinct suffixed '
     f'identifiers appear on the trunk across `{len(_seats)}` seats (`{_seats}`).  ** Which is why '
     f'the recommendation is a CONVENTION and not a band: the form exists, passes, and is written by '
     f'most of the campaign already --- what is missing is that it is not ORDERED, and ordering it '
     f'binds other seats, so it is routed and not taken **',
     _sfx_used >= 20 and len(_seats) >= 3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE RESTRAINT, AND THE LIMIT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_diff = [f for f in subprocess.run(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT,
                                   capture_output=True, text=True).stdout.split('\n') if f]
_untracked = [f for f in subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'],
                                        cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
              if f]
#: ⛔⌗ TWO CORRECTIONS TO THIS GATE'S OWN SUBJECT, BOTH MADE BY RUNNING IT.
#:   ① A RECEIPT is a `.py` file under `receipts/`.  The first form counted every untracked path
#:     there and caught `S36`'s transient probe mid-run, which is not a receipt -- and `S36` has been
#:     changed so it no longer writes a `.py` name at all.
#:   ② And the first form claimed the shared gate's edit was `the whole of this revision's reach`,
#:     which the gate then correctly refuted: this revision also repairs three of this seat's OWN
#:     receipts.  ** So the negative is stated where it actually binds: no receipt belonging to
#:     ANOTHER SEAT is touched, and the shared gate's edit removes no behaviour. **
_HOME = 'receipts/L_probability/'
_rec_touched = [f for f in _diff + _untracked if f.startswith('receipts/') and f.endswith('.py')]
_foreign = [f for f in _rec_touched if not f.startswith(_HOME)]
_gate_diff = subprocess.run(['git', 'diff', '-U0', '--', 'corpus/check_revision_collisions.py'],
                            cwd=ROOT, capture_output=True, text=True).stdout
_removed = [l[1:] for l in _gate_diff.split('\n') if l.startswith('-') and not l.startswith('---')]
_removed_behaviour = [l for l in _removed
                      if re.search(r'\bdef\b|\breturn\b|sys\.exit|\bif\b|\bfor\b', l)]
print(f'      receipts in the working diff: {len(_rec_touched)}, of which outside this seat\'s own '
      f'directory: {len(_foreign)};  lines the shared gate\'s diff REMOVES: {len(_removed)}, of '
      f'which carry behaviour: {len(_removed_behaviour)}')
gate(f'Ⓒ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE where it binds: of the `{len(_rec_touched)}` '
     f'receipts this revision touches, `{len(_foreign)}` belong to another seat --- the rest are '
     f'this seat\'s own, repaired here --- and the shared gate\'s diff removes `{len(_removed)}` '
     f'lines, `{len(_removed_behaviour)}` of which carry behaviour.  ** The gate gates `main` for '
     f'every seat, so the claim is that the change is to its DATA: two named collisions and two '
     f'seeds, and not one line of its test.  That, and reversibility in one line, is the condition '
     f'under which a seat should touch a shared gate at all **',
     not _foreign and not _removed_behaviour)

_hist_half_can_be_green = len(G.BASELINE) > 0
gate(f'Ⓒ② ⚠⛭ and the LIMIT is asserted rather than left implicit: the gate carries '
     f'`{len(G.BASELINE)}` named collisions, which is the only reason a green is possible at all.  '
     f'** A gate asserting the ABSENCE of a historical collision can never go green once one has '
     f'happened; the half that can be green is the NEW-collision half.  ⇒ So naming an instance is '
     f'the repair here and not an evasion --- but a baseline that only ever grows is a ratchet in '
     f'the wrong direction, and the thing to watch is its RATE **',
     _hist_half_can_be_green)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭ ** THE ITEM ROUTED TO THIS SEAT SINCE r7289 IS CLOSED, ** and the gate says so in its own words.
  ⛔ ** AND IT WAS NOT A COUNTER RACE. ** Both collisions are a THIRD line's ANSWER to an order,
     written with the order's own number in front of it. The band is parity over TWO lines and
     has no half for an answering seat.
  ✔ ** THE PREVENTION WAS ALREADY IN THE FILE AND ALREADY IN USE: ** the suffix form is a different
     identifier by the gate's own rule, {_sfx_used} of them are on the trunk across {len(_seats)} seats, and both
     forms are now seeded in opposite directions.
  ⌗ Ordering it binds other seats, so it is ROUTED with this evidence rather than taken.
""")
sys.exit(1 if FAILURES else 0)
