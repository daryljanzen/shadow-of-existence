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

── MEASURED AGAIN AT r2501+c54.197, because the shipped tool did NOT catch its own motivating case ──

  ** The check was verified against a clean tree, which measures nothing. **  Seeding P15's
  prop:subhorizon body back to "inside the horizon at the branch point" -- the sentence routed item
  21 names FIRST, the exact class the r2289 quote in the header describes -- left this file printing
  "clean" and exiting 0.  The receipt binding for a proposition lives in its ARGUMENT paragraph, a
  separate sentence, so the corpus's most load-bearing claim shape was the one shape structurally
  invisible.  Theorem-body binding added; the scan is otherwise unchanged.

  re-measured on the whole corpus, both states:
      before  : 11 bindings, 1 flag  (the declared C6 false positive), motivating defect MISSED
      after   : 12 bindings, 1 flag  (the same, now EXCUSED), motivating defect CAUGHT at line 223
  ⇒ ** +1 binding, +0 false alarms, and the one site the tool exists for moved from invisible to
     caught. **  Precision is unchanged, which is the constraint the contributor named as binding.

  ⚠ AND THE DECLARED-EXCEPTION MACHINERY BELOW EXISTS FOR THE SAME REASON IN REVERSE: after the
  c54.197 sweep the tool's entire steady-state output was one flag known to be bogus, and a lint
  read that way is a lint not read.  Exceptions are keyed to sentence TEXT and go STALE loudly.
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
# ** r2554: the POSSESSIVE and COMPOUND-NOUN forms added, which node 52 attempted, left unapplied, and
# declined to claim precision for. **  Measured before adding, the way r2376 measured the assertion
# patterns:
#   * ** 25 possessive and 73 compound-noun sites across the papers ** -- which reads as a large change;
#   * ** but check_loci examines RECEIPT-BOUND sentences only, and only 3 + 5 = 8 of those 98 are
#     receipt-bound. **  ⇒ *** The extension adds EIGHT newly-checked sites, not ninety-eight. ***
#   * ** All eight read clean ** -- legitimate uses, no conflation.  ⇒ ** Which is the right result for a
#     lint: green on a clean corpus, and there to catch the drift that has not happened yet. **
# ⚠ ** AND WHAT IT DOES NOT FIX, stated because 54 named the gap and this is not it: ** items 19 and 20
# (P1's scope against its own abstract, P7's conflated loci) were found ** by reading **, because they
# are ** not receipt-bound at all **.  *** This extension widens the FORMS matched inside the bound
# sentences; it does not widen the BOUND.  Two different gaps, and only the cheap one closes here. ***
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


# ── r2501+c54.197: THE DECLARED EXCEPTIONS, and why they are keyed to TEXT and not to a line ──
#
# This lint's own header names precision as the binding constraint: "a false alarm in the register
# costs more than the error, because the next reader inherits a debt that does not exist."  After the
# item-21 sweep (c54.197) every real mismatch in P15 is fixed, and the ONE flag left standing is a
# site the finder named as a false positive BEFORE the tool was ever run: the sentence orders the
# branch point against the neutrinos' decoupling in TEMPERATURE along the excursion, which is not a
# horizon property at a locus and is true as written.
#
# *** A lint whose entire steady-state output is one known-bogus flag trains its readers to skip it,
#     which is the same failure as a green result from a broken instrument, arriving from the other
#     side. ***  So the exception is declared here.
#
# ⚠ AND THE DISCIPLINE THAT MAKES IT SAFE.  An exception keyed to a FILE AND LINE silently protects
# whatever text later moves onto that line -- it is a suppression that outlives its reason.  Each
# entry below therefore carries a distinctive fragment of the sentence it excuses, and:
#   (a) the exception applies only while that fragment is still present in the flagged sentence;
#   (b) if the fragment is present NOWHERE in the corpus, the exception is reported as STALE and the
#       tool exits non-zero -- so a rewritten sentence loses its cover LOUDLY rather than quietly.
# Verified against a seeded defect both ways at c54.197, not against a clean tree.
EXCEPTIONS = [
    {
        'tex':      'CR_cosmology.tex',
        'rcpt':     'C6_neutrino_term',
        'fragment': 'branch point is far below their decoupling',
        'why':      'a TEMPERATURE ordering along the excursion, not a horizon property at a locus '
                    '-- named as a false positive by the finder of routed item 21 in advance, and '
                    'confirmed against C6 (the seam temperature is 1.6 eV; decoupling is ~1 MeV)',
    },
]


def excused(tex, key, sent):
    """Is this flag a DECLARED exception, and does its sentence still carry the declared fragment?"""
    for e in EXCEPTIONS:
        if e['tex'] == tex and e['rcpt'] == key and e['fragment'] in sent:
            return e
    return None


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


# ── r2501+c54.197: THE RECALL HOLE AT THE LINT'S OWN MOTIVATING SITE ──
#
# ** This tool did not catch the defect it was built to catch, and that was found by SEEDING it. **
# Re-breaking P15's prop:subhorizon body -- "inside the horizon at the branch point", the exact
# sentence routed item 21 names first and the exact class the header's r2289 quote describes --
# left this lint printing "clean" and exiting 0.
#
# THE MECHANISM: the binding between a claim and its receipt is not always intra-sentence.  A
# `proposition` states its claim in the body and cites its receipt in the SEPARATE argument
# paragraph below it, so a per-sentence scan sees an assertion with no receipt (skipped: "a sentence
# citing no receipt is not checked") and a citation with no assertion.  ** The corpus's most
# load-bearing claim shape was the one shape structurally invisible to the check. **
#
#   *** A gate verified only against a clean tree measures nothing.  The header's own lesson --
#       "a green result from a broken instrument is the worst outcome available" -- had a second
#       instance sitting inside the instrument that states it. ***
#
# THE FIX, kept structural rather than widening the window (which would trade precision for recall,
# and this tool's header names precision as binding): a theorem-like environment's BODY is bound to
# the receipt cited in the argument/proof paragraph that immediately follows it.  Nothing else about
# the scan changes.  Re-measured at c54.197 on the whole corpus -- see MEASURED below.
THEOREM_ENVS = r'proposition|theorem|lemma|corollary|claim|observation'


def sentences_with_rcpt(tex):
    """Yield (sentence, receipt_key, line) for each \\rcpt{} call, with its enclosing sentence --
    plus, for each theorem-like environment, its BODY bound to the receipt its argument cites."""
    s = re.sub(r'(?m)^%.*$', '', tex)
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', s):
        key = m.group(1).replace('\\_', '_')
        # the enclosing sentence: back to the previous sentence end, forward to the next
        # ** r3107: the forward bound was `s.find('. ', m.end())` alone, and the citation is written
        #    IMMEDIATELY AFTER the period at 69 sites in this corpus -- ".\rcpt{...}", no space --
        #    so the split never fired at the sentence the citation belongs to and the "sentence"
        #    ran on to the next ". " downstream, swallowing whatever loci that text named.  It
        #    reported P7's cube-root-two site as naming the SEAM, from a sentence four lines below
        #    the citation.  A splitter that over-runs attributes one claim's locus to another's
        #    argument, which is the exact failure this gate exists to catch. **
        lo = max(s.rfind('. ', 0, m.start()), s.rfind('\n\n', 0, m.start()))
        lo = 0 if lo < 0 else lo + 1
        # the citation ENDS its sentence: stop at it, and never run past a paragraph break
        hi = m.end()
        nxt = s.find('. ', m.end())
        par = s.find('\n\n', m.end())
        if nxt >= 0 and (par < 0 or nxt < par):
            hi = nxt + 1
        yield s[lo:hi], key, s[:m.start()].count('\n') + 1

    # theorem body ← receipt cited in the argument paragraph that follows it
    for m in re.finditer(r'\\begin\{(%s)\}(.*?)\\end\{\1\}' % THEOREM_ENVS, s, re.S):
        body = m.group(2)
        # The argument/proof paragraph.  Bounded STRUCTURALLY, not by a character count: the search
        # runs to the next sectioning command or the next theorem-like environment, and the receipt
        # must sit in the argument's OWN paragraph.  (A fixed 1400-char window was the first attempt
        # and it silently missed this paper's very first proposition -- the clarification paragraphs
        # between the statement and its argument are longer than the window, so the binding fell off
        # the end.  A cap chosen by eye is a recall hole with no error message.)
        tail = s[m.end():]
        stop = re.search(r'\\(?:sub)*section\b|\\begin\{(?:%s)\}' % THEOREM_ENVS, tail)
        if stop:
            tail = tail[:stop.start()]
        am = re.search(r'(?:Argument|Proof)\.?\}?', tail)
        if not am:
            continue
        para = tail[am.start():]
        endp = re.search(r'\n\s*\n', para)
        if endp:
            para = para[:endp.start()]
        for r in re.finditer(r'\\rcpt\{([^}]+)\}', para):
            yield body, r.group(1).replace('\\_', '_'), s[:m.start()].count('\n') + 1


def main():
    problems = []
    excused_hits = []
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
                flat = re.sub(r'\s+', ' ', sent)
                ex = excused(tex, key, flat)
                if ex is not None:
                    excused_hits.append((tex, line, key, ex))
                    continue
                problems.append((tex, line, key, sorted(claimed), sorted(named), flat[:150]))

    print('check_loci: %d receipt-bound locus claims checked' % checked)

    for tex, line, key, ex in excused_hits:
        print('  EXCUSED  %s:%d cites %s -- %s' % (tex, line, key, ex['why']))

    # an exception whose sentence no longer exists is a suppression outliving its reason
    stale = [e for e in EXCEPTIONS
             if not any(e['tex'] == t and e['rcpt'] == k for t, _, k, _ in excused_hits)]
    for e in stale:
        print('\n  ** STALE EXCEPTION ** %s / %s' % (e['tex'], e['rcpt']))
        print('     declared fragment no longer flagged: %r' % e['fragment'])
        print('     the sentence was rewritten or the flag went away -- REMOVE the entry, do not keep it')

    if not problems and not stale:
        print('  clean -- every locus-naming claim agrees with the receipt it cites')
        return 0
    if problems:
        print('  %d MISMATCH(ES):' % len(problems))
        for tex, line, key, claimed, named, sent in problems:
            print('\n  %s:%d  cites %s' % (tex, line, key))
            print('    paper names  : %s' % ', '.join(claimed))
            print('    receipt names: %s' % ', '.join(named))
            print('    > %s' % sent)
    return 1


if __name__ == '__main__':
    sys.exit(main())
