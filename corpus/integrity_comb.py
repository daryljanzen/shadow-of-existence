#!/usr/bin/env python3
"""integrity_comb.py -- THE COMPREHENSIVE COMB (`OWED` 589).

The three whole-corpus censuses each recorded this as owed in their own words -- "the
comprehensive comb the corpus has NOT yet done", "OTHER homes to be FOUND by combing" -- and
none of them said what a comb should LOOK for.  This does, and it looks for four things,
every one of which was found by walking into it during r3378--r3418 rather than by looking.

  (1) SEVERED ROUTES.  A correction applied where a fact is STATED and not where it is USED.
      Three instances in two revisions: P13's real-form COUNT corrected to five while the
      conclusion still read "the unique real form"; TURNAROUND_CUBIC recording "PO-3 was
      STRUCK" two paragraphs above "a node may not close it"; and this node's own L8.5
      withdrawing a finding while leaving the claim.  ** It is not carelessness about facts.
      It is carelessness about ROUTES. **

  (2) STALE REGISTERS.  Prose narrating a row as live that is struck, killed or closed.
      Six in the geometry docs alone at r3418, all disposed at or before r3001.

  (3) NAMED-BY-ABSENCE.  A thing named for a component it LACKS, which presupposes it is
      built from components.  "radiation-free rate" x86 across fourteen files, retired
      r3401--r3404: it invited LambdaCDM-minus-a-term and cost this node two paper edits
      against what the papers said.

  (4) BORROWED PARAMETER.  A sentence stating what the CONSTRUCTION fixes, written in the
      fitted parameter rather than the native one.  Five in P15 at r3405 -- and 23 of 28
      correctly did NOT move, because a sentence quoting what was MEASURED keeps the fitted
      one.  The comb reports; it does not decide.

WHAT THIS IS NOT.  It is not a spelling check and it does not edit.  Every hit is a CANDIDATE
and the register it belongs to is the reader's call -- (1) and (2) are usually real, (3) and
(4) are usually judgement.  A comb that decided would manufacture findings, which is the
failure mode `L8.0` forbids and which this node committed twice in the arc that produced it.
"""
import os
import re
import sys
import glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


# ** SCOPE.  The comb reads documents that carry the CURRENT STATE and no others.  A changelog
# is SUPPOSED to say "struck" and "was open"; combing it measures the changelog's job, not a
# defect -- the first run of this instrument returned 244 severed routes and 177 stale
# registers, almost all of them histories doing what histories do.  The corpus declares the
# distinction itself, in frontmatter `kind:`, and RECORD is the exclusion. **
RECORDING = re.compile(r'^kind:\s*(RECORD)\b', re.M)
RECORD_NAMES = ('CORPUS_MAP', 'INGESTION', 'BUNDLE_', 'FORK_', 'ABSORPTION', 'CLAUDE_CODE_WORK_ORDER',
                'CONSOLIDATE_', 'c22_keepers', 'THE_LIVE_ARC', 'STATE_OF_THE_STATE', 'kills')


def is_record(p):
    b = os.path.basename(p)
    if any(b.startswith(n) or n in p for n in RECORD_NAMES):
        return True
    return bool(RECORDING.search(read(p)[:600]))


def docs():
    out = []
    for pat in ('*.md', 'corpus/*.tex', 'capstones/*.md'):
        out += sorted(glob.glob(os.path.join(ROOT, pat)))
    return [p for p in out if '.git' not in p and not is_record(p)]


# ---------------------------------------------------------------- (1) severed routes
# a document that records a disposal AND still asserts the disposed state.
DISPOSED = re.compile(r'\b(STRUCK|struck|KILLED|WITHDRAWN|withdrawn|SUPERSEDED|superseded|'
                      r'RETIRED|retired|CLOSED r\d|corrected here|is now wrong)\b')
ASSERTS_LIVE = re.compile(r'\b(may not close|is not closed|remains open|stays open|still open|'
                          r'is the unique|are the four|OPEN DRILL|open drill-site)\b')


ID = re.compile(r'\bPO-\d+[a-z]?\b|\bL-\d+\b|\b[A-Z]\d+\.\d+\b')


def severed_routes():
    """A severed route is a disposal and a live assertion ABOUT THE SAME OBJECT.

    ** The first tightening this instrument needed.  Requiring only that both phrases fall
    in one window returned 85 hits, almost all of them a register listing two different rows
    -- 'KILLED' for one and 'stays open' for the next.  Two phrases near each other are not
    a severed route; the same IDENTIFIER on both sides is. **
    """
    hits = []
    for p in docs():
        s = read(p)
        for m in DISPOSED.finditer(s):
            lo, hi = max(0, m.start() - 700), m.end() + 700
            win = s[lo:hi]
            a = ASSERTS_LIVE.search(win)
            if not a:
                continue
            left = set(ID.findall(s[lo:m.end()]))
            right = set(ID.findall(win[a.start():]))
            shared = left & right
            if shared:
                hits.append((os.path.relpath(p, ROOT), sorted(shared)[0], m.group(0), a.group(0)))
    return hits


# ---------------------------------------------------------------- (2) stale registers
def stale_registers():
    kills = {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT, 'kills', '*.md'))}
    reg = read(os.path.join(ROOT, 'THE_REGISTER.md')) if os.path.exists(os.path.join(ROOT, 'THE_REGISTER.md')) else ''
    struck = set(re.findall(r'~~\*\*(PO-\d+[a-z]?)\*\*~~', reg)) | kills
    hits = defaultdict(list)
    for p in docs():
        if '/kills/' in p or p.endswith('THE_REGISTER.md'):
            continue
        s = read(p)
        for row in sorted(struck):
            for m in re.finditer(re.escape(row) + r'\b', s):
                win = s[max(0, m.start() - 240):m.end() + 240]
                if re.search(r'\b(open|OPEN|live|LIVE|may not close|carries)\b', win) and \
                   not re.search(r'\b(STRUCK|struck|kill|disposed|closed|repaired)\b', win):
                    hits[os.path.relpath(p, ROOT)].append(row)
                    break
    return hits


# ---------------------------------------------------------------- (3) named by absence
ABSENCE = [r'radiation-free', r'\bmatter-free\b', r'\bmassless (?:rate|member|limit)\b',
           r'\bcharge-free\b', r'\bsource-free (?:rate|law)\b', r'\bvacuum-free\b']


def named_by_absence():
    hits = defaultdict(int)
    for p in docs():
        s = read(p)
        for pat in ABSENCE:
            n = len(re.findall(pat, s))
            if n:
                hits[(os.path.relpath(p, ROOT), pat)] = n
    return hits


# ---------------------------------------------------------------- (4) borrowed parameter
FIXES = re.compile(r'\b(fixed by|forced by|set by|determined by|selects|privileges)\b')
FITTED = re.compile(r'\\Omega_m|\\omega_m|\\Omega_\\Lambda|\bH_0\b')
NATIVE = re.compile(r'x_\{?0\}?|\\alpha\b|r_N|z_\{?\\mathrm\{acc\}\}?')


def borrowed_parameter():
    hits = []
    for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        s = read(p)
        for m in FIXES.finditer(s):
            win = s[max(0, m.start() - 200):m.end() + 260]
            if FITTED.search(win) and not NATIVE.search(win):
                hits.append((os.path.basename(p), win.replace('\n', ' ')[180:300]))
    return hits


def main():
    print("=" * 78)
    print("  THE COMPREHENSIVE COMB — OWED 589")
    print("=" * 78)
    print(f"  scanned {len(docs())} documents\n")

    sr = severed_routes()
    print(f"  (1) SEVERED ROUTES — disposal recorded and disposed state still asserted: {len(sr)}")
    for f, oid, d, a in sr[:12]:
        print(f"        {f:40s} {oid:8s} '{d}' ... '{a}'")
    if len(sr) > 12:
        print(f"        ... and {len(sr)-12} more")

    st = stale_registers()
    print(f"\n  (2) STALE REGISTERS — struck rows narrated as live: {sum(len(v) for v in st.values())}")
    for f, rows in list(st.items())[:12]:
        print(f"        {f:44s} {sorted(set(rows))}")

    na = named_by_absence()
    print(f"\n  (3) NAMED BY ABSENCE — a thing named for what it lacks: {sum(na.values())}")
    for (f, pat), n in sorted(na.items(), key=lambda kv: -kv[1])[:12]:
        print(f"        {f:44s} {pat:22s} x{n}")

    bp = borrowed_parameter()
    print(f"\n  (4) BORROWED PARAMETER — 'fixed by' + fitted parameter, no native one nearby: {len(bp)}")
    for f, w in bp[:10]:
        print(f"        {f:26s} ...{w.strip()[:96]}...")

    print("\n" + "=" * 78)
    print("  Every hit is a CANDIDATE.  (1) and (2) are usually real; (3) and (4) are")
    print("  judgement.  THE COMB REPORTS AND DOES NOT DECIDE — a comb that decided would")
    print("  manufacture findings, which is the failure this arc committed twice.")
    print("=" * 78)
    return 0


if __name__ == '__main__':
    sys.exit(main())
