#!/usr/bin/env python3
"""check_quote_pins.py -- EVERY QUOTE-PIN SITE IS EITHER ADJUDICATED OR COUNTED, AND THE UNREAD COUNT ONLY FALLS.

** A DRAFT BY NODE 70 (r7125+70.1) FOR NODE 66 TO TAKE, REWRITE OR REFUSE. **  *It is written to run from
`corpus/` beside `quote_pin_baseline.tsv` as `check_prose_pins.py` does, and from this directory as it sits.  It is
NOT registered in `gates.yml`: registering a gate is the gate's call.*

** WHAT A QUOTE-PIN IS. **  An asserting test of a string literal's PRESENCE in text the receipt reads from a file
it does not own -- `'the sentence' in body15`, `re.search('...', body)`, `body.find('...') >= 0`.  *** The defect
is an assertion pinned to wording another seat owns: it fails when that seat rewords, and -- seven times in this
programme -- when the sentence said something was OPEN and the work it was watching succeeded and retired it. ***

** THE MEASUREMENT IS 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs `scripts/mutate_assertions.py
--quote` as a subprocess and compares the sites against the adjudication baseline.  The same three checks as
`check_prose_pins`:
  ⓵ every reported (receipt, literal) is in the baseline -- a NEW quote-pin is a `[FAIL]`;
  ⓶ every baseline key is still reported -- a `[STALE]` entry describes nothing and is removed;
  ⓷ the UNADJUDICATED count may only FALL, against a ceiling declared HERE and nowhere else.

** THE KEY IS (receipt, literal), NOT A LINE. **  *A line-keyed baseline goes stale on any edit above the site.
The same literal tested twice in one receipt is one adjudication.  A reworded literal is a new key and is read
again -- which is the point: the rewording is exactly the event this class fails on.*

  python3 check_quote_pins.py
  python3 check_quote_pins.py --list        # the unadjudicated backlog, complete and unfiltered
  python3 check_quote_pins.py --multi       # the MULTI-SITE backlog (r7201+70.1), with its section split

Drafted r7125+70.1.  Stated for reversal.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, 'scripts', 'mutate_assertions.py')) and ROOT != os.path.dirname(ROOT):
    ROOT = os.path.dirname(ROOT)
BASELINE = os.path.join(HERE, 'quote_pin_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')

LINE = re.compile(r'\s*\[QUOTE-PIN\]\[(PAPER|SOURCE)\]\[(SENTENCE|TOKEN)\]\[([A-Z,]*)\]\s+(\S+?):(\d+):(\d+)\s+(".*")$')
UNREAD = 'UNADJUDICATED'
# ⓷ the ratchet.  Seeded at r7125+70.1 as the count of distinct (receipt, literal) keys; lowering it is the point.
CEILING = 2287
# ⓸ r7201+70.1 (66's r7191 order): THE MULTI-SITE BACKLOG.  A PAPER key whose literal occurs twice or more in the file
#   its read trace names is a pin on the FILE and not on the claim -- it survives the removal of its sentence while
#   any copy stands.  The operator flags it `MULTI` (and `SECSHARED` when two copies share a section, so a section
#   scope cannot single-site it).  Counted over the PINNED key set -- keys in the baseline -- so a new receipt's key
#   fails as NEW and not twice, and the direction is `<=` (r7191 item 4): the count is a backlog interior to its
#   range, so the monotone form is live (r7199's discriminator).  Measured at r7201+70.1: 249 keys, 127 SECSHARED.
MULTI_CEILING = 249
# ⓹ r7201+70.1 (66's r7197 addition): the LIST keys -- a receipt's own pin collections, keyed for the first time -- carry
#   their own bucket, `UNADJUDICATED-LIST`, and their own ceiling.  ⛔ Not folded into `UNADJUDICATED`: that count is
#   held monotone by other receipts (`S2_the_quote_pin_backlog...` at <= 2170), and a population newly COUNTED is not
#   new work in the old backlog -- folding it in turned that receipt and `S5` red on the first CI run of this build.
UNREAD_LIST = 'UNADJUDICATED-LIST'
LIST_CEILING = 60
# ⓺ r7223+70.1 (66's r7223 order, 60's routed blindness): keys behind a PINNED read -- `git show`, inline or through a
#   helper such as `S7`'s `_at` -- which the operator could not trace until `_READ` learned that form.  Newly COUNTED,
#   not newly written, so they take their own bucket and ceiling as the list keys did, and their MULTI flags are
#   counted apart: folding them into `MULTI_CEILING` would read seven old pins newly seen as seven new multi-site pins.
#   Measured at r7223+70.1: 102 keys, 7 of them MULTI.
UNREAD_PINNED = 'UNADJUDICATED-PINNED'
PINNED_CEILING = 102
PINNED_MULTI_CEILING = 7


#: ⛭ r7229+70.1 (66's r7229 order, 60's routed ⓶): ** THE LEDGER'S KEYS ARE UNIQUE, AND NOTHING SAID SO. **  *Two rows
#: on one key read as ONE in the dictionary below, so the second row's verdict silently replaces the first and every
#: count taken from the ledger is short by one -- `L175/E2`'s two extended literals landed on one string at r7225+70.1
#: and read as `EXTENDED 107` against 108 rows.*  ⇒ ** A duplicate is REPORTED as a class with both rows' line numbers,
#: and fails unless it is named here with its reason. **
KNOWN_DUPLICATE_KEYS = {}
DUPLICATE_KEYS = {}


# ⛭⛭⛭ r7253+70.1 (66's r7253 ①): THE VERDICT VOCABULARY IS CLOSED, AND `MEANING-HELD` IS GATED.
#   *Until this revision the verdict column was never checked: ANY string counted as adjudicated, so a new verdict --
#   or a typo -- was already an exemption.*  `MEANING-HELD` (r7251+70.2, adopted r7253): a pin on what a paper MEANS,
#   which no string form can repair; the finding is HELD at a commit (L-249's historical half) and the live assertion
#   is a READ TRIGGER, not a guard.  Counted, not owed -- and never a discharge of UNADJUDICATED by another route,
#   because a held row must prove it was READ: it names the commit its finding is held at, and that commit must
#   (H1) resolve, (H2) be an ancestor of HEAD, (H3) carry the literal in what the key reads, (H4) be a SENTENCE, and
#   (H5) be a commit that CHANGED the receipt.  ⇒ ** H5 is what separates held from unread: measured at r7253+70.1,
#   H1-H4 alone pass a key stamped with HEAD that nobody read, because a green receipt's sentence is present at
#   HEAD by construction. **  See computations/beyond_the_wall/r7253_70_meaning_held/.
MEANING_HELD = 'MEANING-HELD'
VOCABULARY = {UNREAD, UNREAD_LIST, UNREAD_PINNED, 'DELIBERATE', 'ALT-OK', 'REPAIR-OWED', 'NOT-A-PIN', 'ENCODING-OK',
              'EXTENDED', MEANING_HELD}
_HELD_AT = re.compile(r'held at ([0-9a-f]{8,40})\b')
_SHOW_CACHE = {}


def _git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace')


def _flat(t):
    return re.sub(r'\s+', ' ', t)


def _present_at(sha, lit, target, receipt):
    """H3: is the literal in what the key reads, at `sha`?  Whitespace-normalised, because a paper sentence wraps
    across lines and a line-based grep would miss it; a literal that is a regex is matched as one."""
    def hit(text):
        if lit in text:
            return True
        if '\\' in lit:
            try:
                return re.search(lit, text) is not None
            except re.error:
                return False
        return False
    if target == 'PAPER':
        names = [n for n in _git('ls-tree', '--name-only', sha, 'corpus/').stdout.split()
                 if n.endswith('.tex') and not os.path.basename(n).startswith('appendix_receipts')]
    else:
        words = ' '.join(lit.split()[:3]).replace('\\', '')
        names = [n.split(':', 1)[1] for n in _git('grep', '-l', '-F', '-e', words.split()[0] if words else lit, sha,
                                                  '--').stdout.split('\n') if ':' in n]
        names = [n for n in names if n != receipt]
    for n in names:
        key = (sha, n)
        if key not in _SHOW_CACHE:
            _SHOW_CACHE[key] = _flat(_git('show', f'{sha}:{n}').stdout)
        if hit(_SHOW_CACHE[key]):
            return True
    return False


def held_check(receipt, lit, target, tier, why, provenance=True):
    """'' if the MEANING-HELD row is held, else the first condition it fails"""
    m = _HELD_AT.search(why or '')
    if not m:
        return 'H1 names no `held at <sha>`'
    sha = m.group(1)
    r = _git('rev-parse', '--verify', '--quiet', f'{sha}^{{commit}}')
    if r.returncode != 0:
        return f'H1 {sha} does not resolve to a commit'
    full = r.stdout.strip()
    if _git('merge-base', '--is-ancestor', full, 'HEAD').returncode != 0:
        return f'H2 {sha} is not an ancestor of HEAD'
    if tier != 'SENTENCE':
        return 'H4 a TOKEN is not a meaning pin'
    if provenance and full not in set(_git('log', '--format=%H', '--', receipt).stdout.split()):
        return f'H5 {sha} never changed {os.path.basename(receipt)}'
    if not _present_at(full, lit, target, receipt):
        return f'H3 the literal is not in what the key reads at {sha}'
    return ''


def _held_seeds():
    """each seeded row must come out as stated, or the gate has lost a direction"""
    rc = 'receipts/L204_physics_reach/P13_the_entropy_is_the_corpuss_own_number.py'
    lit = 'The one physical length is $\\alpha$, not $\\ell_P$'
    sha = _git('log', '-1', '--format=%H', '--', rc).stdout.strip()
    head = _git('rev-parse', 'HEAD').stdout.strip()
    bad = []
    for why, l, tier, want in [
            (f'held at {sha[:12]}', lit, 'SENTENCE', ''),
            ('read and held', lit, 'SENTENCE', 'H1'),
            ('held at deadbeefdeadbeef', lit, 'SENTENCE', 'H1'),
            (f'held at {sha[:12]}', 'a horizon that is a perfectly ordinary Tuesday', 'SENTENCE', 'H3'),
            (f'held at {sha[:12]}', lit, 'TOKEN', 'H4')]:
        got = held_check(rc, l, 'PAPER', tier, why)
        if (got[:2] if got else '') != want:
            bad.append(f'{why!r} / {l[:30]!r} / {tier}: expected {want or "held"}, got {got or "held"}')
    if head not in set(_git('log', '--format=%H', '--', rc).stdout.split()):
        if not held_check(rc, lit, 'PAPER', 'SENTENCE', f'held at {head[:12]}').startswith('H5'):
            bad.append('a row stamped with HEAD, a commit that never changed its receipt, must fail H5')
    if 'TYPO-OK' in VOCABULARY:
        bad.append('the vocabulary must not admit an unknown verdict')
    return bad


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    DUPLICATE_KEYS.clear()
    for _n, ln in enumerate(open(BASELINE, encoding='utf-8'), 1):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 6:
            _k = (p[0], json.loads(p[1]))
            if _k in rows:
                DUPLICATE_KEYS.setdefault(_k, []).append(_n)
            rows[_k] = (p[2], p[3], p[4], p[5], p[6] if len(p) > 6 else '')
    return rows


def measure():
    r = subprocess.run([sys.executable, INSTRUMENT, '--quote'], cwd=ROOT, capture_output=True, text=True,
                       timeout=600)
    out = {}
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            target, tier, flags, path, _l, _c, lit = m.groups()
            key = (path, json.loads(lit))
            prev = out.get(key)
            # one key, several sites: ALT only if every site is ALT (the stricter reading wins); MULTI and SECSHARED
            #   are properties of the literal in its file, so any site carrying them carries them for the key
            keep = {f for f in ((prev[2] if prev else '') + ',' + flags).split(',') if f in ('MULTI', 'SECSHARED')}
            if prev is None or ('ALT' in prev[2] and 'ALT' not in flags):
                out[key] = (target, tier, flags)
            t_, ti_, f_ = out[key]
            out[key] = (t_, ti_, ','.join([x for x in f_.split(',') if x and x not in keep] + sorted(keep)))
    return out


def main():
    print()
    print('  QUOTE-PIN RATCHET -- is every pin on a sentence another seat owns adjudicated, or at least counted?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    _dups = {k: v for k, v in DUPLICATE_KEYS.items() if k not in KNOWN_DUPLICATE_KEYS}
    print(f'    ledger keys unique: {len(DUPLICATE_KEYS)} duplicate key(s), {len(KNOWN_DUPLICATE_KEYS)} named as known')
    if _dups:
        print(f'  ⛔ {len(_dups)} KEY(S) CARRY MORE THAN ONE ROW -- the ledger counts each once, so a verdict is lost:')
        for (rc, lit), lines in sorted(_dups.items()):
            print(f'      {rc}  {str(lit)[:60]!r}  -- rows at lines {lines} and an earlier one')
        print('    ⇒ merge the rows into one that records both, or name the key in KNOWN_DUPLICATE_KEYS with why.')
        return 1
    live = measure()
    print(f'    the instrument reports {len(live)} distinct (receipt, literal) key(s); the baseline carries {len(base)}')
    tally = {}
    for t, tier, flags in live.values():
        for k in [f'{t}/{tier}'] + [f'{t}/{f}' for f in flags.split(',') if f]:
            tally[k] = tally.get(k, 0) + 1
    print(f'    by target/tier and flag: {dict(sorted(tally.items()))}')
    verdicts = {}
    for _t, _ti, _f, v, _w in base.values():
        verdicts[v] = verdicts.get(v, 0) + 1
    print(f'    by verdict: {verdicts}')
    _seed_bad = _held_seeds()
    if _seed_bad:
        print('  ⛔ a MEANING-HELD seed lost its direction:')
        for b in _seed_bad:
            print(f'      {b}')
        return 1
    print('    MEANING-HELD seeds hold: a valid row is held; no sha, a bad sha, an absent literal, a TOKEN, and a '
          'HEAD stamp each fail')
    _unknown = sorted({v for *_x, v, _w in base.values()} - VOCABULARY)
    if _unknown:
        print(f'  ⛔ VERDICT(S) OUTSIDE THE VOCABULARY: {_unknown} -- an unknown verdict counts as adjudicated and is an '
              f'exemption by typo.  Use one of {sorted(VOCABULARY)}.')
        return 1
    _held = [(k, v) for k, v in base.items() if v[3] == MEANING_HELD]
    _held_bad = [(k, r) for k, v in _held for r in [held_check(k[0], k[1], v[0], v[1], v[4])] if r]
    print(f'    {MEANING_HELD}: {len(_held)} key(s) HELD, not owed -- each at a commit that changed its receipt and '
          f'carries its literal; {len(_held_bad)} fail')
    if _held_bad:
        for (p, lit), r in _held_bad[:20]:
            print(f'      [NOT HELD] {p}  {json.dumps(lit, ensure_ascii=False)[:60]}  -- {r}')
        print('  ⛔ A MEANING-HELD ROW THAT CANNOT SHOW IT WAS READ IS AN EXEMPTION WITH A NICER NAME.')
        return 1
    unread = verdicts.get(UNREAD, 0)
    print(f'    {UNREAD}: {unread}   ** the only bucket that means work, and it may only fall **')

    if '--list' in sys.argv:
        print()
        print(f'  THE BACKLOG, COMPLETE AND UNFILTERED -- {unread} key(s):')
        for (p, lit), (t, tier, flags, v, _w) in sorted(base.items()):
            if v == UNREAD:
                print(f'    [{t}/{tier}{"/" + flags if flags else ""}] {p}')
                print(f'               {json.dumps(lit, ensure_ascii=False)}')
        return 0

    bad = 0
    new = sorted(k for k in live if k not in base)
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW QUOTE-PIN KEY(S) -- not in the baseline:')
        for p, lit in new[:40]:
            print(f'    [FAIL] {p}')
            print(f'           {json.dumps(lit, ensure_ascii=False)}')
        if len(new) > 40:
            print(f'    ... and {len(new) - 40} more')
        print('     ⌗ READ IT AND RECORD A VERDICT.  A gate that asserts another seat\'s sentence is present fails')
        print('       when that seat rewords -- and fails on SUCCESS when the sentence said something was open.')
        print('       If the claim is the sentence\'s MEANING, assert what the sentence is for; if both paper')
        print('       states are legitimate, test the disjunction (ALT); if the wording itself is the claim, say so')
        print('       in the baseline as DELIBERATE.')
        bad += 1
    else:
        print('    no new key: the class has not grown.')

    gone = sorted(k for k in base if k not in live)
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- no longer reported, so the adjudication describes nothing:')
        for p, lit in gone[:40]:
            print(f'    [STALE] {p}')
            print(f'            {json.dumps(lit, ensure_ascii=False)}')
        if len(gone) > 40:
            print(f'    ... and {len(gone) - 40} more')
        bad += 1
    else:
        print('    no stale entry: every adjudication still describes a live key.')

    pinned = {k for k, (_t, _ti, _f, v, _w) in base.items() if v == UNREAD_PINNED}
    pinned_multi = sorted(k for k, (_t, _ti, fl) in live.items() if k in pinned and 'MULTI' in fl.split(','))
    multi = sorted(k for k, (_t, _ti, fl) in live.items() if k in base and k not in pinned and 'MULTI' in fl.split(','))
    shared = sum(1 for k in multi if 'SECSHARED' in live[k][2].split(','))
    if '--multi' in sys.argv:
        print()
        print(f'  THE MULTI-SITE BACKLOG, COMPLETE AND UNFILTERED -- {len(multi)} key(s), {shared} SECSHARED:')
        for p, lit in multi:
            print(f'    [{"SECSHARED" if "SECSHARED" in live[(p, lit)][2] else "SECTION-UNIQUE"}] {p}')
            print(f'               {json.dumps(lit, ensure_ascii=False)}')
        return 0
    print(f'    MULTI-SITE: {len(multi)} pinned key(s) -- {len(multi) - shared} a section scope would single-site, '
          f'{shared} that need a neighbourhood or a longer literal')
    if len(multi) > MULTI_CEILING:
        print()
        print(f'  ⛔ THE MULTI-SITE COUNT ROSE: {len(multi)} against the declared ceiling {MULTI_CEILING}.')
        print('     ⌗ A pinned literal now occurs more than once in its file: name the section it is about, or')
        print('       lengthen it until it names one site (`python3 check_quote_pins.py --multi` lists them).')
        bad += 1
    else:
        print(f'    the multi-site ratchet holds: {len(multi)} against a ceiling of {MULTI_CEILING}')

    unread_list = verdicts.get(UNREAD_LIST, 0)
    if unread_list > LIST_CEILING:
        print()
        print(f'  ⛔ THE UNADJUDICATED LIST-PIN COUNT ROSE: {unread_list} against the declared ceiling {LIST_CEILING}.')
        bad += 1
    else:
        print(f'    the list-pin ratchet holds: {unread_list} unadjudicated list key(s) against a ceiling of {LIST_CEILING}')

    unread_pinned = verdicts.get(UNREAD_PINNED, 0)
    if unread_pinned > PINNED_CEILING or len(pinned_multi) > PINNED_MULTI_CEILING:
        print()
        print(f'  ⛔ THE PINNED-READ BUCKET ROSE: {unread_pinned} unadjudicated against {PINNED_CEILING}, '
              f'{len(pinned_multi)} multi-site against {PINNED_MULTI_CEILING}.')
        bad += 1
    else:
        print(f'    the pinned-read ratchet holds: {unread_pinned} unadjudicated pinned-read key(s) against a ceiling of '
              f'{PINNED_CEILING}, {len(pinned_multi)} of them multi-site against {PINNED_MULTI_CEILING}')

    if unread > CEILING:
        print()
        print(f'  ⛔ THE UNADJUDICATED COUNT ROSE: {unread} against the declared ceiling {CEILING}.')
        bad += 1
    else:
        print(f'    the ratchet holds: {unread} unadjudicated against a ceiling of {CEILING}')

    print()
    if bad:
        print('  ⛔ THE QUOTE-PIN RATCHET IS RED.')
        return 1
    print('  the quote-pin class is fully accounted: no new key, no stale entry, and the backlog in the open.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
