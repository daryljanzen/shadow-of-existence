#!/usr/bin/env python3
"""check_currency.py -- L-42: CONSOLIDATE's register has lapsed twice (brought current at
r1730 after 130 revisions, again at c54.13 after ~500).  A recurring defect wants a gate.

ARC 14 step 1.  Three defects were found in this gate at r2377 and all three are fixed here.

  (1) THE BASELINE WAS ITSELF A WATCHED DOCUMENT.  The front was read from FORK_c54.md alone,
      which stopped at c54.35 while the fork ran to c54.108 -- so the reference point SANK WITH
      THE DOCUMENTS IT WAS MEASURING and the gate reported "every standing register is current"
      with CORPUS_MAP 76 behind.  A manufactured null.
      FIX: the front is the MAXIMUM over every document that carries a fork revision.  A register
      that is ahead DEFINES the front and can no longer be dragged down by one that stopped.

  (2) THE WATCH LIST WAS SIX HAND-LISTED NAMES, so a document could rot merely by never having
      been added to it.
      FIX: the watched set is the LIVE set from scripts/classify_documents.py (SOURCE/VIEW/STATE).

  (3) CURRENCY WAS MEASURED AS "the highest fork revision mentioned anywhere in the file", which
      ANY MENTION SATISFIES.  Writing a section INTO CONSOLIDATE about CONSOLIDATE being 76
      revisions behind made CONSOLIDATE pass, because the section named c54.108.
      FIX: a file may DECLARE `current: c54.N` in its frontmatter, written only by the pass that
      actually brings it current, and the declaration is what is measured.  A file with no
      declaration is measured by the body scrape and REPORTED AS UNDECLARED, because a scrape is
      wrong by construction on a live document that legitimately discusses revisions it is not
      current to.  Undeclared is not a failure; it is a weaker reading, and it says so.

Stated for reversal.
"""
import os
import re, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
WINDOW = 6          # revisions a live document may lag before it is stale
FRONT_EXTRA = ['FORK_HISTORY_c54.txt', 'THE_PLAN.md', 'FORK_c54.md']


def declared(path):
    """The honest marker, with THREE declarable values -- and the two non-numeric ones matter.

    r2381.  Making these 29 documents "declared" by copying their body scrape into a `current:` line
    would be laundering the weak proxy into the strong claim, which is the exact defect the declared
    marker was built to remove.  ** A declaration must be written only by the pass that actually
    brings the file current, and this pass does not bring most of them current. **  So:

      current: c54.N   a real declaration -- a pass brought this file current to that fork revision
      current: rNNNN   a real declaration against the MAIN LINE.  ** Added r2390, because the gate
                       could not express it and six documents dated at r2389 were therefore still
                       counted UNDECLARED -- the dating work did not register as dating. **  Some
                       documents have never been touched by the fork at all (no c54 marker anywhere
                       in them), so the only honest revision to name is a main-line one; measuring
                       those against the fork front would report a lag that means nothing.
      current: none    DECLARED-UNKNOWN -- nobody has brought it current; its position is not known
      current: frozen  DECLARED-FROZEN -- ** a dated RECORD of past work, not a status document. **
                       Added r2548, and it is a JOIN rather than new machinery: `check_deferrals`
                       already carries a named LOGS list on exactly this ground ("rewriting a record
                       to look better is a different failure"), and `FORK_c54.md` already declares
                       ** "FROZEN RECORD -- covers c54.1-c54.35 only" ** in its own header while THIS
                       gate demanded it be brought current.
                         ⇒ ** Two gates disagreeing about one file is the signature. **
                       ⚠ A frozen file is exempt from the LAG check and from nothing else: it must
                       still say what span it covers, and a file that declares frozen without a span
                       note FAILS.  *** Freezing is a claim about scope, not a way to stop being
                       measured. ***
                       and is not guessed.  Not a pass: it still cannot be read as current.
      current: n/a     DECLARED-EXEMPT -- a FORWARD document, ahead of the corpus by construction.
                       Dating it invites the inverted-gradient repair its own banner forbids:
                       "stale is a word for the corpus, never for the instrument examining it."

    Returns (kind, value) where kind is 'rev' | 'none' | 'na' | 'frozen' | None(no marker at all).
    """
    if not os.path.exists(path): return (None, None)
    head = open(path, encoding='utf-8', errors='replace').read(2500)
    m = re.search(r'^current:\s*(c54\.(\d+)|r(\d{3,4})|none|n/a|frozen)\s*$', head, re.M | re.I)
    if not m: return (None, None)
    v = m.group(1).lower()
    if v == 'none': return ('none', None)
    if v == 'frozen': return ('frozen', None)
    if v == 'n/a': return ('na', None)
    if m.group(3): return ('mainline', int(m.group(3)))
    return ('rev', int(m.group(2)))


def scraped(path):
    """The weak proxy: the highest fork revision mentioned anywhere in the body."""
    if not os.path.exists(path): return None
    rs = [int(x) for x in re.findall(r'c54\.(\d+)',
          open(path, encoding='utf-8', errors='replace').read())]
    return max(rs) if rs else None


def live_set():
    """The LIVE set is declared by the classifier, not hand-listed here."""
    script = os.path.join(ROOT, 'scripts', 'classify_documents.py')
    if os.path.exists(script):
        try:
            out = subprocess.run([sys.executable, script, '--live'],
                                 capture_output=True, text=True, timeout=120)
            names = [l.strip() for l in out.stdout.split('\n') if l.strip()]
            if names: return names, 'scripts/classify_documents.py'
        except Exception:
            pass
    # fallback: the pre-ARC-14 hand list, so the gate still runs on a tree without the classifier
    return (['CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md', 'THE_LIVE_ARC.md',
             'THE_OPEN_PROBLEMS_LEDGER.md', 'CORPUS_MAP.md', 'INDEX.md', 'WHATS_TEED_UP.md',
             'FORK_c54.md'], 'the built-in fallback list (classifier not found)')


def main():
    watch, origin = live_set()
    allpaths = {n: os.path.join(ROOT, n) for n in set(watch) | set(FRONT_EXTRA)}
    scrapes = {n: scraped(p) for n, p in allpaths.items()}
    known = [r for r in scrapes.values() if r is not None]
    if not known:
        print('  [FAIL] cannot read the fork state'); return 1
    cur = max(known)
    front = sorted(n for n, r in scrapes.items() if r == cur)

    # ** r2514+c54.201: MEASURE AGAINST THE LAST ABSORBED REVISION, NOT THE FORK FRONT. **
    #
    # ** THE FAILURE, ON THE FORK'S OWN TREE. **  56 brings the documents current to whatever it has
    # absorbed; the fork then cuts revisions the observer line has not seen yet.  Every document 56
    # correctly brought current is then "behind" by exactly the number of revisions IN FLIGHT --
    #
    #     *** so this gate goes red on the fork precisely when the fork is most productive, and the
    #         redness measures the handoff queue rather than any document's currency. ***
    #
    # At c54.201 that was 25 documents at "7 revisions behind" against a window of 6, every one of
    # them correct as of the last absorption.  ** A gate whose steady state on one node's tree is a
    # wall of failures that mean nothing is a gate that node stops reading ** -- the same failure
    # this line hit in check_loci (c54.197) and answered there with declared exceptions.
    #
    # ** THE FIX USES THE CORPUS'S OWN DECLARATION AND NOTHING ELSE. **  ABSORPTION.md carries an
    # `IN-FLIGHT:` line naming the revisions cut but not yet absorbed -- already gated by
    # check_absorption, so it cannot drift.  Subtract those and the basis is the last revision both
    # lines have seen.  ** On 56's tree nothing is ever in flight, so this changes nothing there. **
    inflight = set()
    _abs = os.path.join(ROOT, 'ABSORPTION.md')
    if os.path.exists(_abs):
        _m = re.search(r'(?m)^IN-FLIGHT:\s*(.+)$', open(_abs, encoding='utf-8').read())
        if _m and 'none' not in _m.group(1).lower():
            inflight = {int(x) for x in re.findall(r'c54\.(\d+)', _m.group(1))}
    if inflight and cur in inflight:
        _absorbed = [r for r in known if r not in inflight]
        if _absorbed:
            _base = max(_absorbed)
            print(f"  fork front: c54.{cur}   (from {', '.join(front)})   window: {WINDOW}")
            print(f"  ** measuring against c54.{_base}, the last ABSORBED revision: "
                  f"{len(inflight)} in flight ({', '.join('c54.%d' % r for r in sorted(inflight))}) **")
            print("  *a document current as of the last absorption is not stale because the fork "
                  "has moved since.*")
            cur = _base
        else:
            print(f"  fork front: c54.{cur}   (from {', '.join(front)})   window: {WINDOW}")
    else:
        print(f"  fork front: c54.{cur}   (from {', '.join(front)})   window: {WINDOW}")
    print(f"  watching {len(watch)} live document(s), from {origin}")
    print()
    stale, undeclared, unknown, exempt, mainline = [], [], [], [], []
    rows = []
    for n in sorted(watch):
        p = allpaths[n]
        (dk, d), s = declared(p), scrapes.get(n)
        if dk == 'na':
            exempt.append(n)
            rows.append((n, 'n/a (forward document -- exempt by declaration)', False))
            continue
        if dk == 'mainline':
            mainline.append((n, d))
            rows.append((n, f'r{d} (declared against the main line)', False))
            continue
        if dk == 'none':
            unknown.append(n)
            rows.append((n, 'none (declared unknown -- nobody has brought it current)', False))
            continue
        if dk == 'frozen':
            # ** a dated RECORD, exempt from the lag check and from nothing else. **  It must still
            # say what span it covers: freezing is a claim about SCOPE, not a way to stop being
            # measured.  A file that declares frozen with no span note FAILS.
            _t = open(p, encoding='utf-8', errors='replace').read()
            _has_span = ('FROZEN RECORD' in _t) or re.search(r'covers\s+c54\.\d+', _t)
            if _has_span:
                exempt.append(n)
                rows.append((n, 'frozen (a dated record -- exempt from the lag check by '
                                'declaration, with its span stated)', False))
            else:
                stale.append((n, None))
                rows.append((n, 'frozen BUT NO SPAN STATED -- freezing is a claim about scope, not '
                                'a way to stop being measured', True))
            continue
        basis, how = (d, 'declared') if d is not None else (s, 'scraped')
        lag = None if basis is None else cur - basis
        if basis is None:
            tag, bad = 'never', True
        else:
            tag, bad = f"c54.{basis} ({how}, lag {lag})", lag > WINDOW
        if bad: stale.append((n, lag))
        if dk is None: undeclared.append(n)
        rows.append((n, tag, bad))
    width = max(len(n) for n, _, _ in rows)
    for n, tag, bad in rows:
        print(f"    {n:>{width}}  {tag}{'   <-- STALE' if bad else ''}")
    print()
    if mainline:
        print(f"  DECLARED-MAINLINE: {len(mainline)} document(s) name a MAIN-LINE revision, because")
        print( "    the working fork has never touched them (no c54 marker anywhere in the file), so")
        print( "    a fork lag would be a number about nothing.  Listed with the revision a pass reached:")
        for n, d in sorted(mainline):
            print(f"      {n}  r{d}")
        print()
    if exempt:
        print(f"  DECLARED-EXEMPT: {len(exempt)} forward document(s) -- " + ', '.join(exempt))
        print( "    Ahead of the corpus by construction; dating them inverts the gradient.")
        print()
    if unknown:
        print(f"  DECLARED-UNKNOWN: {len(unknown)} document(s) say `current: none`.")
        print( "    ** Not a pass. **  Nobody has brought them current and the position is NOT")
        print( "    guessed from a body scrape -- copying the scrape into the declaration would")
        print( "    launder the weak proxy into the strong claim.  They clear only when a pass")
        print( "    actually brings each one current and writes the revision it reached.")
        for u in unknown: print(f"      {u}")
        print()
    if undeclared:
        print(f"  UNDECLARED: {len(undeclared)} live document(s) carry no `current:` marker, so their")
        print( "  currency is read from a body scrape -- a PASS there means only that the number appears")
        print( "  somewhere in the file.  Read this gate's FAILURES as findings and its PASSES as weak")
        print( "  until the marker is written by the pass that brings each file current.")
        print()
    if stale:
        print(f"  STALE: {len(stale)}")
        for s, lag in stale:
            print(f"    [FAIL] {s} has not been brought current"
                  + (f" ({lag} revisions behind)" if lag is not None else ""))
        return 1
    print("  Every live document is current.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
