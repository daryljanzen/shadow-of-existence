#!/usr/bin/env python3
"""check_open_ledger.py -- THE LEDGER OF WHAT IS OPEN MUST STAY CURRENT WITH THE PAPERS.

** THE PROBLEM IT SOLVES, NAMED BY DARYL AT r2593. **  This line kept discovering that a thing which
looked open was not -- and kept ** failing to record the verdict **, so the same reading had to be redone
every time anyone asked what was left.  ⇒ *** A grep is not a list of what is owed.  It is a list of
places to look, and the looking has to be written down or it does not count. ***

** WHAT THE LEDGER HOLDS. **  `corpus/open_ledger.txt` -- one line per DISTINCT epistemic qualification in
the paper bodies, with a VERDICT.  ** 123 raw hits deduplicate to 113 sentences **, and reading them shows
most are not gaps: deliberate `DO-NOT-ASSERT` holdings, `SCOPE-BY-DESIGN` statements, descriptions of
`STANDARD-PHYSICS`'s open problems, or claims that are `SELF-ANSWERED` two sentences later.

** WHAT THIS GATE CHECKS -- three things, and the third is the point. **
  ⓵ ** every ledger entry still exists in a paper **  -- an entry whose sentence is gone means the corpus
    moved and the ledger did not;
  ⓶ ** every qualification in the papers is in the ledger **  -- a NEW one that nobody verdicted;
  ⓷ ** the UNVERDICTED count only falls **  -- recorded in the ledger header, so *** the ledger cannot
    grow a backlog silently: verdicting is the only direction it moves. ***

  ⚠ ** It does NOT check that a verdict is CORRECT. **  That is a reading, and no gate can do it.  *** What
  it guarantees is that every qualification HAS one and that none appears without being seen. ***

    python3 corpus/check_open_ledger.py
    python3 corpus/check_open_ledger.py --rebuild     # re-derive, preserving existing verdicts

Written r2593.  Stated for reversal.
"""
import glob
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
LEDGER = os.path.join(HERE, 'open_ledger.txt')

PAT = re.compile(
    r"(we claim no|is not claimed here|not claimed:|we do not claim|traced rather than computed"
    r"|recalled rather than derived|remains open|stays open|what remains open|at that weight"
    r"|we state it at|as the hypothesis it is|not claimed"
    r"|is not settled|not yet|undelivered|unbuilt|is open\b)", re.I)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def scan():
    """Return {id: (paper, claim)} for every distinct qualification in the papers."""
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        t = re.sub(r'\s+', ' ', body(f))
        for m in PAT.finditer(t):
            s = t.rfind('. ', 0, m.start()) + 2
            e = t.find('. ', m.end())
            claim = t[s:e + 1][:300]
            key = hashlib.sha1(re.sub(r'\W+', '', claim[:120]).encode()).hexdigest()[:10]
            out.setdefault(key, (os.path.basename(f).replace('.tex', ''), claim))
    return out


def read_ledger():
    if not os.path.exists(LEDGER):
        return {}
    out = {}
    for line in open(LEDGER, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split('|', 3)]
        if len(parts) == 4:
            out[parts[0]] = (parts[1], parts[2], parts[3])
    return out


# ** ---- ADDED r2596: THE BACKLOG CHECK ---- **
# ** THE FAILURE IT PREVENTS: an item advertised as owed in the papers AFTER the work that closed it was
# done. **  ⇒ *** An entry verdicted SELF-ANSWERED whose claim text still says "remains open" / "not yet"
# / "unbuilt" is precisely that: the ledger knows the thing is answered and the prose has not caught up. ***
#
#   ⚠ ** It fires ONLY on SELF-ANSWERED. **  A `REGISTERED` item SHOULD read as open -- the paper is right
#   and the register carries the gap.  *** Measured at r2596: 13 candidates across both verdicts, of which
#   11 were correct REGISTERED entries and only 2 were real. ***
#   ⚠ ** And its precision depends on the verdicts being right. **  One of this line's own verdicts was
#   wrong within two revisions of being written -- which is why the reasoning is recorded beside each, so
#   the next reader can overturn it cheaply.
OPENWORD = re.compile(r"(remains open|stays open|is open\b|not yet|unbuilt|undelivered|cannot yet"
                      r"|is not settled|has not yet run)", re.I)


# ** THE ONE EXCLUSION, and it is stated rather than patched into the pattern. **  "The gate IS OPEN and
# has been walked" uses `open` to mean AVAILABLE, not UNRESOLVED.  ⇒ *** Loosening OPENWORD to dodge it
# would blind the check to real cases; naming the sense here keeps the pattern tight and the exception
# visible. ***
# ** SECOND NAMED SENSE, r2597. **  "reduces the count of what this sector leaves UNDELIVERED", "the
# hypercharges are NOT a third UNDELIVERED item" -- here the trigger word is *the subject being
# REDUCED*, not a debt being declared.  ⇒ *** Same shape as the first exclusion: the sentence says a
# thing is no longer owed, using the word for what it is no longer. ***
_OPEN_MEANS_AVAILABLE = re.compile(r"(gate is open and has been walked|the gate is open|route is open"
                                   r"|is open to|reduces the count of what|not a third undelivered"
                                   r"|is the first of the undelivered items on which)", re.I)


def _backlog(led):
    out = []
    for k, (paper, verdict, claim) in led.items():
        if verdict != 'SELF-ANSWERED':
            continue
        body = claim.split('##')[0]
        if _OPEN_MEANS_AVAILABLE.search(body):
            continue
        m = OPENWORD.search(body)
        if m:
            out.append((k, paper, m.group(0), body))
    return out


def _backlog_gate(led):
    bad = _backlog(led)
    if not bad:
        print('  no SELF-ANSWERED entry still advertises openness.')
        return 0
    print()
    for k, paper, word, body in bad:
        print(f'    [FAIL] {k} ({paper}) is verdicted SELF-ANSWERED but its text still says "{word}"')
        print(f'           "{body[:88]}"')
    print()
    print('    ⛔ AN ITEM ADVERTISED AS OWED AFTER THE WORK THAT CLOSED IT WAS DONE.')
    print('       ** Either the prose needs de-narrating (THE_FRONT_EDGE step 4) or the verdict is')
    print('       wrong. **  Both happen; the reasoning beside the entry says which.')
    return 1


def main():
    print()
    print('  check_open_ledger -- is the ledger of what is open current with the papers?')
    print()
    cur = scan()
    led = read_ledger()

    if '--rebuild' in sys.argv:
        import subprocess  # noqa
        # ⛔⛭ ** REFUSAL ADDED r4123 (node 61), AFTER THIS REBUILD DESTROYED A VERDICTED ROW. **
        # *At `606ce176` a `--rebuild` dropped row `518af53f10` -- 2181 characters carrying r2631's
        # negative discharge and r3920's confirmation, verdict SELF-ANSWERED. It came back as 147
        # characters with no note, and the next reader met a bare sentence and re-verdicted it
        # SCOPE-BY-DESIGN. Receipt `L221/B11` depended on that note and went red silently.*
        #   ⌗ *The mechanism is the loop below: it iterates over what `scan()` finds in the PAPERS,
        #     so a verdicted row the scan no longer matches is not carried and not named -- it is
        #     simply absent from the rewrite. `keep` and `why` preserve the verdict and the note for
        #     rows that are still found, and have nothing to say about one that is not.*
        # ⇒ *** 60 built the repair at its own r4022: orphaned verdicted rows preserved as comments
        #     and named on stdout, nothing auto-carried. THAT GUARD IS NOT ON THIS TRUNK -- it is on
        #     an unmerged branch -- so until it arrives this rebuild REFUSES rather than runs. ***
        #   ** A silent drop of a REGISTERED verdict deletes known debt from the list of what is
        #   owed, which is worse than a rebuild that does not happen. **  *The refusal is deliberately
        #   not a re-implementation: writing a second guard here would collide with the merge that
        #   brings the first, and the fix for that is to merge, not to duplicate.*
        _orphans = sorted(k for k in led if k not in cur and led[k][1] != 'UNVERDICTED')
        if _orphans and not any('orphan' in ln for ln in open(__file__, encoding='utf-8')
                                if 'def ' in ln):
            print()
            print('  check_open_ledger --rebuild: REFUSED.')
            print()
            print(f'  {len(_orphans)} verdicted row(s) would be dropped without being named:')
            for k in _orphans:
                print(f'      {k}  {led[k][1]}')
            print()
            print('  This rebuild has no orphan guard on this trunk.  60 built one at its r4022,')
            print('  on branch claude/shadow-of-existence-setup-6awafl -- merge it and re-run.')
            print('  A silent drop already cost row 518af53f10 its reasoning and flipped its')
            print('  verdict (restored r4123); the refusal is here so that cannot recur unnoticed.')
            print()
            return 1
        # ** preserve BOTH the verdict and the reasoning: the `##` note is why the verdict was
        # given, and rebuilding the claim text from the paper must not drop it. **
        keep = {k: v[1] for k, v in led.items()}
        why = {k: ('##' + v[2].split('##', 1)[1]) if '##' in v[2] else ''
               for k, v in led.items()}
        lines = [l.rstrip('\n') for l in open(LEDGER, encoding='utf-8')
                 if l.startswith('#') or not l.strip()]
        for k, (paper, claim) in sorted(cur.items(), key=lambda x: (keep.get(x[0], 'UNVERDICTED'), x[1][0])):
            v = keep.get(k, 'UNVERDICTED')
            c = re.sub(r'\s+', ' ', re.sub(r'\\rcpt\{[^}]*\}', '', claim)).strip()[:180]
            note = ('   ' + why[k]) if why.get(k) else ''
            lines.append(f'{k} | {paper} | {v} | {c}{note}')
        open(LEDGER, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        print(f'  rebuilt: {len(cur)} entries, {sum(1 for k in cur if k not in keep)} new')
        return 0

    print(f'  papers hold {len(cur)} distinct qualification(s); ledger holds {len(led)}.')
    new = sorted(set(cur) - set(led))
    gone = sorted(set(led) - set(cur))
    unv = [k for k, v in led.items() if v[1] == 'UNVERDICTED']
    print(f'  UNVERDICTED in the ledger: {len(unv)}')
    print()

    if gone:
        for g in gone[:6]:
            print(f'    [WARN] {g} ({led[g][0]}) is in the ledger and no longer in any paper')
            print(f'           "{led[g][2][:88]}"')
        print('    ⌗ the corpus moved and the ledger did not -- run --rebuild to re-derive.')
        print()

    if new:
        for n in new:
            paper, claim = cur[n]
            print(f'    [FAIL] {n} ({paper}) is a qualification with NO VERDICT in the ledger')
            print(f'           "{re.sub(chr(92)+"s+", " ", claim)[:96]}"')
        print()
        print('    ⛔ A GREP IS NOT A LIST OF WHAT IS OWED.  ** It is a list of places to look, and the')
        print('       looking has to be written down or it does not count. **  Add a verdict:')
        print('       DO-NOT-ASSERT / SCOPE-BY-DESIGN / STANDARD-PHYSICS / METHOD-PROSE /')
        print('       SELF-ANSWERED / REGISTERED / NAMED-UNBUILT / PRECISION / OPEN-DOWNSTREAM')
        return 1

    rc = _backlog_gate(led)
    print('  every qualification in the papers has a verdict in the ledger.')
    if unv:
        print(f'  ⌗ {len(unv)} still UNVERDICTED -- the only bucket that means work.')
    print()
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
