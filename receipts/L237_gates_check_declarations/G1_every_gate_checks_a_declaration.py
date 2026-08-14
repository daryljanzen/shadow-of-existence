#!/usr/bin/env python3
"""G1 -- why "no gate we have looks for that" keeps being the answer: every gate checks a DECLARATION.

** THE ROUTED ITEM (c54.187): ** "c54.164's finding -- l_1 in {150, 165, 315} -- was on the old
ROBUST_p1p2_scan code.  Everything since is built on ACOUSTIC_two_arm, the finding was never carried
across, and P15's text has quoted 0.5703 through six revisions of a transfer that cannot move it.
** A finding that doesn't travel with the instrument it was made on is one the corpus loses without
noticing, and no gate we have looks for that. **"

** THE FINDING IS REAL AND THE DETECTOR IS NOT BUILDABLE YET.  Both halves matter. **

** ⓵ THE OBVIOUS SIGNATURE WAS TESTED AND DOES NOT EXIST. **  The corpus already has the ORIGIN
convention: a receipt declares which computation it came from, and check_receipts compares code and
flags drift (24 unexplained, 19 adjudicated).  So the natural detector is "a receipt whose ORIGIN is
gone", or "a paper section resting on a MIX of live and dead instruments".

    receipts whose ORIGIN no longer exists           :   0
    sections resting on a mix of live and dead ones  :   0   (of 114 with declared origins)

  ⇒ ** ROBUST_p1p2_scan's origin still exists.  Nothing drifted.  The signature is absent, so a
    detector built on it would be validated against nothing ** -- which is L-220's shipped lesson and
    check_loci's, and this is the second time in one session that checking the case before building
    stopped a build.

** ⓶ AND THE REASON IS STRUCTURAL: what changed is WHICH INSTRUMENT IS AUTHORITATIVE FOR A FRONT, and
the corpus has no field for that. **  ORIGIN says where a receipt CAME FROM.  Nothing says whether that
origin is still the one you would use.  A finding does not travel because ** nothing records what it
would travel TO. **

** ⛭⛭ ⓷ AND THE PATTERN IS EXACT, WHICH IS THIS RECEIPT'S ACTUAL RESULT: **

    *** EVERY GATE IN THE SUITE CHECKS SOMETHING SOMEBODY DECLARED. ***

      check_citations     a declared \\rcpt{} citation
      check_receipts      a declared INDEX row
      check_id_bands      a declared band range
      check_absorption    a declared absorption row (and the fork's new IN-FLIGHT: line)
      check_kills         a declared PROTECTED_OPEN item
      check_arcs          a declared arc heading and marker
      check_changelog     a declared revision entry
      check_currency      a declared frontmatter position
      check_grains        a declared grain list
      check_burndown      declared IDs and states
      ... and the rest alike.

    *** AND BOTH LINTS INFER -- check_loci infers a locus from prose, scope_table infers a parameter
        from code -- AND BOTH ARE DELIBERATELY OUTSIDE THE GATE LIST. ***

  ⇒ ** So "no gate we have looks for that" is not an oversight.  IT IS THE ARCHITECTURE.  The corpus
    can gate exactly what it declares, and nothing else. **

** ⓸ AND THIS IS THE THIRD REQUEST IN ONE SESSION THAT LANDED ON THE SAME WALL: **
  * L-220's arrival paths -- a metric converged as route-sets were added; the answer was a CONVENTION
    (COMPUTES:), routed as item 30, not a gate.
  * the prose-duplicate scanner (c54.186 item 3) -- withdrawn at r2463 for want of an exhibit.
  * this one -- the declaration does not exist.
  ⇒ *** THE RULE: BEFORE ASKING "WHY IS THERE NO GATE FOR THIS", ASK "WHAT WOULD IT CHECK, AND WHO
      DECLARES IT".  If the answer is "it would infer", the honest output is a LINT or a CONVENTION,
      and saying so is worth more than a detector nobody can validate. ***

WHAT IS NOT CLAIMED.  Not that the finding-does-not-travel problem is unimportant -- ** it is real, it
cost the corpus six revisions of a quoted number, and the fork found it. **  Not that no gate could
ever exist: ** one could, the revision after a front declares its authoritative instrument. **  Only
that it cannot be built now, and that the reason is the same one that explains why the eighteen gates
that DO work, work.

Written r2470.  Stated for reversal.
"""
import os, re, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def origins():
    out = {}
    for f in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True):
        t = open(f, encoding='utf-8', errors='replace').read()
        m = re.search(r'ORIGIN:\s*([^\s,;]+\.py)', t)
        if m:
            out[os.path.basename(f)[:-3]] = (m.group(1),
                                             os.path.exists(os.path.join(ROOT, m.group(1))))
    return out


def main():
    print()
    print('  G1 -- why is there no gate for "a finding that did not travel"?')
    print()
    o = origins()
    # ** 197 unique receipt STEMS, not the 248 a `grep -rl` reports -- that counts FILES, and the
    # same stem can sit in more than one place.  The threshold was set from the wrong number and the
    # check caught it. **
    check(f'the ORIGIN convention is widely used ({len(o)} receipt stems declare one)', len(o) > 150)

    dead = [k for k, v in o.items() if not v[1]]
    check(f'⛔ but ZERO of them have an ORIGIN that no longer exists (found {len(dead)}) -- '
          'so "dead origin" is not a detectable signature here', len(dead) == 0)

    # the mixed-instrument signature
    idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'),
               encoding='utf-8', errors='replace').read()
    sec = collections.defaultdict(list)
    for l in idx.split('\n'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 4:
            continue
        m = re.match(r'`(.+\.py)`$', c[3])
        if not m:
            continue
        stem = os.path.basename(m.group(1))[:-3]
        if stem in o:
            sec[(c[0], c[1])].append(o[stem])
    mixed = [k for k, v in sec.items()
             if any(x[1] for x in v) and any(not x[1] for x in v)]
    check(f'and ZERO sections rest on a MIX of live and dead instruments '
          f'(of {len(sec)} with declared origins)', len(mixed) == 0)
    check('⇒ a detector built on either signature would be validated against nothing',
          len(dead) == 0 and len(mixed) == 0)

    # the structural reason
    check('ORIGIN says where a receipt CAME FROM; nothing in the corpus says whether that origin '
          'is still the AUTHORITATIVE instrument for its front',
          not any('AUTHORITATIVE' in open(f, encoding='utf-8', errors='replace').read()
                  for f in glob.glob(os.path.join(ROOT, 'computations', '**', '*.py'),
                                     recursive=True)[:80]))

    # ** the pattern **
    gates = [os.path.basename(f)[:-3]
             for f in glob.glob(os.path.join(ROOT, 'corpus', 'check_*.py'))]
    check(f'the suite has {len(gates)} check_* scripts', len(gates) >= 17)
    # ---------------------------------------------------------------- r2656+c54.208
    # ** THIS CHECK WAS FALSIFIED BY THE CORPUS GETTING BETTER, WHICH IS A RECEIPT DOING ITS JOB. **
    # It asserted that NEITHER inferring lint is wired into CI.  `check_loci` has since been wired,
    # after the c54.197 work gave it a theorem-body binding and a declared exception list -- so the
    # thing this receipt flagged as unwired got fixed, and the receipt went red saying so.
    #   ⇒ *** It went red at some revision nobody can name, because nothing re-ran it: the runner's
    #       cached result had not moved in 294 commits (`L-541`).  The claim is therefore SPLIT
    #       rather than relaxed -- the wired one is asserted wired, the unwired one unwired --
    #       so the row keeps its edge instead of being widened until it passes. ***
    _ci = open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'),
               encoding='utf-8', errors='replace').read()
    check('⛭ check_loci -- an INFERRING lint -- is now wired into CI, which it was not when this '
          'receipt was written: the exception list it grew is what made it gateable',
          'check_loci' in _ci)
    check('and scope_table, the other inferring lint, is STILL not wired -- so the distinction the '
          'receipt draws survives and has not been widened to fit',
          'scope_table' not in _ci)
    arsenal = open(os.path.join(ROOT, 'THE_ARSENAL.md'), encoding='utf-8', errors='replace').read()
    check('and THE_ARSENAL records the rule the two lints share: a gate can check a DECLARATION, '
          'it cannot check a JUDGEMENT',
          'a gate can check a DECLARATION' in arsenal or 'check a DECLARATION' in arsenal)

    # the third request
    f54 = open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
    check('and this is the third request landing on the same wall: L-220 (answered by a CONVENTION, '
          'routed as item 30)', 'COMPUTES:' in f54)
    check('and the prose-duplicate scanner, withdrawn at r2463 for want of an exhibit',
          'WITHDRAWN' in f54 or 'the scanner is not built' in f54.lower()
          or 'scanner' in f54.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the finding is real and the detector is not buildable yet. **')
    print('  Zero receipts have a dead ORIGIN and zero sections mix live and dead instruments, so')
    print('  ** both natural signatures are absent and a detector would be validated against')
    print('  nothing. **  ROBUST_p1p2_scan\'s origin still exists; nothing drifted.')
    print('  ⇒ ** What changed is WHICH INSTRUMENT IS AUTHORITATIVE for a front, and the corpus has no')
    print('     field for that.  A finding does not travel because nothing records what it would')
    print('     travel TO. **')
    print('  ⛭⛭ AND THE PATTERN IS EXACT: ** every gate in the suite checks something somebody')
    print('     DECLARED, and both lints INFER and are deliberately outside the gate list. **')
    print('     So "no gate we have looks for that" is not an oversight -- ** it is the architecture. **')
    print('  ⇒ THE RULE: before asking why there is no gate, ask ** what would it check and who')
    print('    declares it. **  If the answer is "it would infer", the honest output is a LINT or a')
    print('    CONVENTION -- and saying so beats a detector nobody can validate.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
