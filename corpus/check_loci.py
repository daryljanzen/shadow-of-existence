#!/usr/bin/env python3
"""check_loci.py -- the locus lint: does a sentence assert a property of the locus its receipt computed?

** CONTRIBUTED BY NODE 52, r2428.  ADOPTED AT r2440 AS A LINT AND NOT A GATE, ON ITS OWN MEASUREMENT. **

WHAT IT EXPLOITS.  Every computed claim in this corpus is bound to a runnable receipt, so ** the receipt
is the authority on which locus was computed. **  For each \\rcpt{} call it compares the locus the
sentence asserts a property OF against the loci its receipt names.

** WHY IT IS NOT WIRED TO FAIL A BUILD, and this is the contributor's own reason, measured: **

    word-presence (intersection) :  8 flags  -- MISSES the motivating case entirely
    word-presence (subset)       : 12 flags  -- 5 real / 7 false = 42% precision
    ASSERTION-SHAPE (shipped)    :  3 flags  -- 3 real / 0 false = 100% precision, 60% recall

  ⇒ ** Precision, not recall, is the binding constraint: a false alarm in the register costs more than
    the error, because the next reader inherits a debt that does not exist.  A missed site stays as it
    is. **  So this is a TRIAGE LINT whose output a human reads.  ** Do not add it to the CI gate list. **

KNOWN GAPS, stated so they are not rediscovered: it misses POSSESSIVE forms ("the branch point's
radiation amplitude takes...") and COMPOUND-NOUN forms ("built on the branch point handover").  The
contributor attempted those patterns, the edit did not apply, and ** it shipped the tool without them
rather than claim a precision it had not re-measured. **

⚠ ** AND ONE BUG WORTH INHERITING AS A RULE. **  The first version returned empty for EVERYTHING because
`lp.strip('\\b')` also strips the leading 'b' of `branch[ -]point`, giving `ranch[ -]point`.  Every
pattern silently failed and the tool printed "clean".

    *** A gate that reports clean because its regexes are broken is worse than no gate. ***

  It therefore ships PAIRED WITH A CHECK ON LABELLED SENTENCES -- a self-test that fails if the patterns
  stop matching known-positive text.  ** Do not remove that. **  It is the same lesson this line learned
  five times over from the other direction (r2425, r2438): a measure whose meaning depends on its
  subject is not a measurement, and a green result from a broken instrument is the worst outcome
  available.

Adopted r2440.  Stated for reversal.
"""

# ── the contributor's own header, kept verbatim ──
# """check_loci.py -- the gate on LOCUS NAMING, eighth of the corpus's gates.
# 
# ** The failure this exists for has happened three times and each time needed a manual sweep. **
# r2155 established the naming rule for the four loci of the lap -- branch point (r=0), turnaround,
# the lift (turnaround -> r=0), the seam (r = -2a/sqrt3 and +a/sqrt3, one substrate point met a lap
# apart).  r2289 retired `z_bp` outright: "It was WRONG, not loose... the error INVERTED the physics:
# sub-horizon at ONSET; super-horizon at the CROSSING.  Reading either at the other's locus reverses
# it."  Both were hand sweeps.
# 
# ** Seven gates police claims, closure, the register, compilation, currency, queues and grains.
#    NONE polices the locus words, and the naming rule is the one whose violation inverts a result. **
# 
# At r2376+ four sites in P15 still said "branch point" where the receipt cited at the very same
# sentence says "seam" -- and the two behave oppositely (the comoving horizon is near its MAXIMUM at
# the seam, so most modes are inside; at the branch point aH -> infinity, so all have exited).  The
# cost was measurable: two independent nodes each recorded a false alarm from it in one day, one
# concluding "nothing oscillating crosses for l >= 3" and the other "prop:subhorizon inverts for
# l <= 250".  A wrong locus does not read as wrong; it reads as a discovery.
# 
# THE RULE this gate enforces, and it is deliberately narrow to keep the false-positive rate at zero:
# 
#     Where a sentence in a paper cites a receipt AND names a locus, the receipt it cites must
#     name the same locus.
# 
# The corpus already binds every computed claim to a runnable receipt, so the receipt is the
# authority on which locus was computed.  That makes the check mechanical and needs no model of the
# physics.  A sentence citing no receipt is not checked; a receipt naming no locus is not checked.
# Both are silences, not violations.
# 
# Exit 0 clean, 1 on any mismatch.
# """

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

# the four loci of the lap, with the spellings each is actually written in
LOCI = {
    'branch point': [r'branch[ -]point', r'\br\s*=\s*0\b'],
    'seam':         [r'\bseam\b', r'z_\{?\\?mathrm\{?onset', r'\bonset\b'],
    'turnaround':   [r'turnaround', r'turning point of the collapse'],
    'lift':         [r'\bthe lift\b'],
}

RECEIPT_DIRS = ['receipts', 'storyboard_receipts', 'storyboard_receipts_r2381', 'computations']


# r2376+: the ASSERTION patterns.  Measured on the twelve sites the word-presence test flagged:
# presence alone gives 5 real / 7 false (42%).  Every false alarm was a sentence whose SUBJECT is not
# a locus claim -- a negation ("no seam-made asymmetry"), an enumeration ("the derivatives separate
# all four loci"), a summary, or a remark about naming practice.  Every real one asserts a property
# OF a named locus.  These patterns encode that difference; they select the 5 and reject the 7.
ASSERT = [
    r'(?:at|near|on)\s+(?:the\s+)?{L}\b[^.]{{0,80}}?\b(?:is|are|sits?|lies?|becomes?|remains?)\b',
    r'\bthe\s+{L}\b\s+(?:is|are|sits?|lies?|carries|becomes?|remains?|has|takes)\b',
    r'\breach(?:es|ing)?\s+(?:the\s+)?{L}\b',
    r'\b(?:sub|super)-horizon\s+(?:at|near)\s+(?:the\s+)?{L}\b',
    r'\binside the horizon at (?:the )?{L}\b',
]
NEGATED = [r'\bno\s+{L}', r'\bnot\s+(?:the\s+)?{L}', r'\brather than\s+(?:the\s+)?{L}',
           r'\bdistinct from\s+(?:the\s+)?{L}', r'\bseparate[sd]?\s+all\s+four']


def asserted_of(text, name, pats):
    """Is a property ASSERTED OF this locus here (and not merely mentioned or denied)?"""
    for p in pats:
        for lp in LOCI[name]:
            # NB: do NOT strip('\\b') here -- it also strips the leading 'b' of 'branch[ -]point'.
            core = lp[2:] if lp.startswith('\\\\b') else lp
            core = core[:-2] if core.endswith('\\\\b') else core
            if re.search(p.format(L=core), text, re.I):
                # a denial of the same locus cancels it
                for n in NEGATED:
                    if re.search(n.format(L=core), text, re.I):
                        return False
                return True
    return False


def loci_asserted(text):
    """Loci this text asserts a property OF -- the narrow set the gate uses."""
    return {n for n in LOCI if asserted_of(text, n, ASSERT)}


def loci_in(text):
    """Which loci this text names."""
    found = set()
    for name, pats in LOCI.items():
        for p in pats:
            if re.search(p, text, re.I):
                found.add(name)
                break
    return found


def find_receipt(key):
    for d in RECEIPT_DIRS:
        for root, _, fs in os.walk(os.path.join(ROOT, d)):
            if key + '.py' in fs:
                return os.path.join(root, key + '.py')
    return None


def sentences_with_rcpt(tex):
    """Yield (sentence, receipt_key) for each \\rcpt{} call, with its enclosing sentence."""
    s = re.sub(r'(?m)^%.*$', '', tex)
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', s):
        key = m.group(1).replace('\\_', '_')
        # the enclosing sentence: back to the previous sentence end, forward to the next
        lo = max(s.rfind('. ', 0, m.start()), s.rfind('}\n\n', 0, m.start()))
        lo = 0 if lo < 0 else lo + 1
        hi = s.find('. ', m.end())
        hi = len(s) if hi < 0 else hi + 1
        yield s[lo:hi], key, s[:m.start()].count('\n') + 1


def main():
    problems = []
    checked = 0
    for tex in sorted(os.listdir(os.path.join(ROOT, 'corpus'))):
        if not tex.endswith('.tex') or tex.startswith('appendix_receipts'):
            continue
        path = os.path.join(ROOT, 'corpus', tex)
        body = open(path, encoding='utf-8', errors='replace').read()
        for sent, key, line in sentences_with_rcpt(body):
            claimed = loci_asserted(sent)     # narrow: asserted OF, not merely named
            if not claimed:
                continue                        # sentence names no locus: silence, not violation
            rp = find_receipt(key)
            if rp is None:
                continue                        # missing receipts are check_receipts' business
            rtext = open(rp, encoding='utf-8', errors='replace').read()
            named = loci_in(rtext)
            if not named:
                continue                        # receipt names no locus: silence
            checked += 1
            # STRICT: every locus the paper names here must be one the receipt names.
            # An intersection test is not enough -- it passes the motivating case, where a
            # sentence names both loci and attributes the claim to the wrong one (P15 line 289
            # says "the branch point sits on its rising branch... rather than a numerical
            # accident of z_onset", and C2 says the SEAM sits there).
            if not (claimed <= named):
                problems.append((tex, line, key, sorted(claimed), sorted(named),
                                 re.sub(r'\s+', ' ', sent)[:150]))

    print('check_loci: %d receipt-bound locus claims checked' % checked)
    if not problems:
        print('  clean -- every locus-naming claim agrees with the receipt it cites')
        return 0
    print('  %d MISMATCH(ES):' % len(problems))
    for tex, line, key, claimed, named, sent in problems:
        print('\n  %s:%d  cites %s' % (tex, line, key))
        print('    paper names  : %s' % ', '.join(claimed))
        print('    receipt names: %s' % ', '.join(named))
        print('    > %s' % sent)
    return 1


if __name__ == '__main__':
    sys.exit(main())
