#!/usr/bin/env python3
"""check_supersession.py -- the EIGHTH gate, and it exists because of a pattern this session hit
six times in nine revisions.

** THE FAILURE. **  Over the c54.67-c54.75 sweep, SIX open leads turned out to be answered
already -- not by new work, but by results banked earlier and never claimed against them:

  L-68  the Z_3 grading "derived from the slicing"      -- paid by the wall-per-hinge reading
  L-05  is normal-bundle su(3) reachable?               -- paid by the reality obstruction
  L-97  the rank tension                                -- paid by the same
  L-14  does the A_2 reason bridge to su(3)?            -- paid by the branching
  L-02  is the collapse a requirement?                  -- paid by the D=5 computation
  L-03  nothing forces a descent of length > 1          -- paid by the M=0 cut result

** THE REGISTER RECORDS WHAT IS OWED AND HAS NO MECHANISM FOR NOTICING WHEN SOMETHING ELSE PAYS
IT. **  Every one of these sat open while its answer sat in a receipt, sometimes for dozens of
revisions.  check_burndown polices HOT leads and languishing debt; nothing polices leads that
have quietly been ANSWERED.

** ONE FALSE-POSITIVE MODE, FOUND ON THE FIRST RUN AND FILTERED. **  A lead whose own text was
written after a receipt usually CITES that receipt, so the two share many terms and the pair
scores highest of all -- self-reference wearing the shape of a discovery.  The first run's top
three were exactly that.  Pairs are now skipped when the lead's text names a revision at or
after the receipt's build.

** WHAT THIS IS AND IS NOT. **  It is a triage REPORT, not a verdict: it matches distinctive
terms between open leads and receipt summaries and ranks the overlaps.  A high score means "go
read this receipt against this lead", not "this lead is struck."  ** A gate that guessed at
supersession would be worse than none, because a wrong strike is invisible. **  So this one
never fails on content -- it exits non-zero only if it cannot read its inputs.

Run it before opening new work, and read the top of the list.
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')

TOP = 12          # how many candidate pairings to print
MIN_SCORE = 2.0   # length-normalised weighted-score floor (see the IDF + normalisation note in main)
MIN_SHARED = 3    # fewer shared distinctive terms than this is noise

STOP = set("""the a an and or of to in on at for with by is are was were be been being that this
these those it its as from not no nor but if then than so such which who whom what when where
how why all any both each few more most other some only own same too very can will just should
now here there we our us they them their he she his her i me my one two three there's does do
did doing done has have had having up down out over under again further once about into through
during before after above below between only very s t don should now corpus paper section
result results open lead leads work worked working thing things question questions answer
answered still what's it's isn't aren't p3 p14 p13 p9 p7 p6 p12 p17 receipt receipts built
r2376 c54 ok yes no none new old first second third same different whether rather instead
daryl daryl's row's node node's line's fork fork's revision revisions register registered
struck landed reading read stated named carried carries holds held says said found finding
package queued owed audit annotated corrected correction verdict verdicts state states""".split())

# ** r2382: THE STOP LIST GAINED THE PROGRAMME'S OWN META-VOCABULARY, and the reason is measured. **
# A register row carries two kinds of language: the OBJECT's (throat, monodromy, triality) and the
# PROCESS's (registered, struck, corrected, Daryl, node, audit).  Only the first can indicate that a
# receipt answers a lead.  Before this, L-206's top pair was scored on `daryl, row's, door, daryl's,
# complete, tour` -- self-description matching self-description.  Length normalisation cut the noise
# floor; this cuts the noise itself.

WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_'\-]{3,}")


def terms(text):
    t = re.sub(r"[^A-Za-z0-9_' \-]", " ", text.lower())
    return {w for w in WORD.findall(t) if w not in STOP}


def main():
    try:
        arc = open(ARC, encoding='utf-8').read()
        idx = open(INDEX, encoding='utf-8').read()
    except OSError as e:
        print(f"  [FAIL] cannot read inputs: {e}")
        return 1

    # open leads: rows whose id is NOT struck
    leads = []
    for ln in arc.split("\n"):
        m = re.match(r"\|\s*(~~)?\*?\*?(L-\d+)\*?\*?(~~)?\s*\|(.*)", ln)
        if m and not m.group(1):
            # r2378: skip kind:WORK rows.  The arcs and phases folded from CONSOLIDATE live in the
            # same ID space -- the assignment is one place for everything owed -- but "has a receipt
            # already answered ARC 14?" is not a well-formed query, and scoring a programme of work
            # against 268 receipts produces noise that pushes real candidates off the list.
            # ** One register, kinds scoped per gate. **
            if 'KIND:WORK' in m.group(4).upper():
                continue
            leads.append((m.group(2), m.group(4)))   # whole row: the revision markers live at the END

    # receipts: INDEX rows, with their build revision if present
    receipts = []
    for ln in idx.split("\n"):
        if not ln.startswith("| P"):
            continue
        stem = re.search(r"`([A-Za-z0-9_/]+\.py)`", ln)
        # r2382: the build-revision regex required "built rN (c54.N)" and matched only 85 of 266
        # rows.  ** So the false-positive filter below -- the one this gate's own docstring says was
        # "found on the first run and filtered" -- could not fire on 68% of the receipt corpus, and
        # the top of the scan filled with self-reference showing `built: ?`. **  A filter that is
        # inert on two-thirds of its inputs is a filter nobody can see failing.
        # Read at source, the rows use three forms: "built rN (c54.N)", "built rN" alone, and
        # "built new".  Take the c54 revision where present, else the main-line rNNNN, else '?'.
        rev = re.search(r"built r\d+ \((c[\d.]+)[^)]*\)", ln)
        if not rev:
            m2 = re.search(r"built r(\d{3,4})", ln)
            rev = None if not m2 else type('M', (), {'group': staticmethod(lambda i, v='r' + m2.group(1): v)})()
        if stem:
            receipts.append((stem.group(1).split('/')[-1][:-3],
                             rev.group(1) if rev else '?', ln))

    print()
    print("  SUPERSESSION SCAN -- open leads against receipts that may already answer them")
    print(f"  {len(leads)} open lead(s) x {len(receipts)} receipt(s)")
    print()
    if not leads:
        print("  No open leads.  Nothing to scan.")
        return 0
    if not receipts:
        print("  [WARN] no receipts parsed from INDEX.md; scan is vacuous.")
        return 0

    # ** IDF WEIGHTING, added r2376+c54.96, because the fold degraded the signal. **
    # The scan was tuned on SHORT lead rows.  After the open-problems map was folded in, rows grew
    # to paragraphs and the top of the list filled with pairs sharing only common vocabulary --
    # "action", "carries", "exactly".  A raw count of shared terms rewards long rows and common
    # words equally with short rows and rare ones.  So score by INVERSE DOCUMENT FREQUENCY over
    # the receipt corpus: a term shared by two documents is worth much more than one shared by
    # eighty.  The threshold is on the WEIGHTED score; MIN_SHARED still applies to the raw count,
    # so a single freak term cannot carry a pair on its own.
    import math
    df = Counter()
    rterms = {}
    for stem, rev, rline in receipts:
        # the row carries its own FILE PATH, so the stem and its parts leak into the term set and
        # then match any lead that happens to name the receipt.  Strip them.
        rterms[stem] = terms(rline) - {stem.lower()} - set(stem.lower().split('_'))
        for t in rterms[stem]:
            df[t] += 1
    N = max(1, len(receipts))

    def idf(t):
        return math.log(N / (1 + df.get(t, 0)))

    pairs = []
    for lid, ltext in leads:
        lt = terms(ltext)
        if len(lt) < MIN_SHARED:
            continue
        for stem, rev, rline in receipts:
            shared = lt & rterms[stem]
            if len(shared) < MIN_SHARED:
                continue
            # ** r2382: NORMALISE BY THE LEAD'S OWN SIZE, because IDF alone did not stop the
            # blinding. **  Measured: L-150 is 16,546 characters -- 33 accreted segments, 25 revision
            # markers -- and it topped the scan at 107.5 on `stays`, `falls`, `ever`, `size`.  A long
            # row shares SOME rare term with almost every receipt, so raw IDF still rewards length.
            #
            # The fix is at the INSTRUMENT and not at the rows, deliberately: L-150 is the working
            # fork's live front and trimming it would (a) cross ARC 15's seat line and (b) be
            # overwritten at the next absorption.  A gate that only works when the register is tidy
            # is a gate with a hidden precondition.
            #
            # Divide by sqrt(|lead terms|): a row with four times the vocabulary needs twice the
            # weighted overlap to score the same.  sqrt, not linear, so a genuinely rich row is not
            # punished out of the list altogether.
            score = sum(idf(t) for t in shared) / math.sqrt(max(1, len(lt)))
            if score < MIN_SCORE:
                continue
            # ** THE FALSE-POSITIVE MODE, filtered: a lead whose own text was written AFTER the
            # receipt usually CITES it, so the overlap is self-reference rather than an
            # unnoticed answer.  Skip when the lead names a revision at or after the build. **
            touched = re.findall(r"c54\.(\d+)", ltext)
            # main-line rNNNN builds: a lead naming a revision at or after the build is
            # self-reference too, and 90 rows carry only that form.
            if rev.startswith('r') and not rev.startswith('r2376'):
                lrevs = [int(x) for x in re.findall(r"\br(1\d{3}|2\d{3})\b", ltext)]
                try:
                    if lrevs and max(lrevs) >= int(rev[1:]):
                        continue
                except ValueError:
                    pass
            if rev.startswith('c54.') and touched:
                try:
                    if max(int(x) for x in touched) >= int(rev.split('.')[1]):
                        continue
                except ValueError:
                    pass
            top = sorted(shared, key=lambda t: -idf(t))[:6]
            pairs.append((round(score, 1), lid, stem, rev, top))
    pairs.sort(reverse=True)

    if not pairs:
        print("  No overlaps above threshold.  (That is a weak signal, not a clean bill.)")
        return 0

    print(f"  {'score':>7} {'lead':>7}  {'receipt':<44} {'built':>8}  the RAREST shared terms")
    seen = Counter()
    shown = 0
    for n, lid, stem, rev, sh in pairs:
        if seen[lid] >= 2:      # at most two candidates per lead, so one lead cannot flood
            continue
        seen[lid] += 1
        shown += 1
        print(f"  {n:>7} {lid:>7}  {stem[:44]:<44} {rev:>8}  {', '.join(sh)}")
        if shown >= TOP:
            break

    print()
    print("  ** These are CANDIDATES, not verdicts.  Read the receipt against the lead. **")
    print("     A lead answered by banked work should be STRUCK with the receipt named, not")
    print("     re-worked -- and six such were found by hand across c54.67-c54.75 before this")
    print("     gate existed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
