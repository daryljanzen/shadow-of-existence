"""the DANGLING-PREDICATE test, SECOND CUT -- r7260+60, after r7257 adopted the first.

** WHAT THE FIRST CUT WAS. **  A span that begins with a finite verb, a participle or a bare
conjunction cannot name its own subject, so it passes on any sentence carrying that predicate.  That
is a HEAD test over a closed word list, and r7257 adopted it corpus-wide.

** THE TWO ERROR MODES FOUND BY USING IT, both exhibited by rows repaired at r7260. **

  ⓐ ** A FALSE POSITIVE on `that`/`this`/`these`/`those`/`which`/`what`/`whose` as a DETERMINER. **  `That sentence
     constrains the target rather than the mechanism` names its subject -- `That sentence` -- and the
     head test calls it dangling because `that` is also a subordinating conjunction.  The
     discriminator is cheap and is not a guess: a determiner is followed by a word that is NOT a verb
     form, and the span then carries a finite verb LATER.  A subordinating `that` has its own clause's
     verb and no noun phrase of its own standing before it.

  ⓑ ** A FALSE NEGATIVE on a span that ENDS on a bare conjunction or preposition. **  `non-geometric
     but` promises a continuation it does not carry, and the head test cannot see it -- it looks at
     the first word only.  *My own r7258 reply asserted that this span dangles.  The adopted
     detector cannot see that it does, so the assertion was true of the span and not of the
     instrument, and the two were not distinguished.*

  ⓒ ** A SECOND FALSE NEGATIVE, on a span whose head is a NEGATOR. **  `not need a lower bound` and
     `not by the peak's value` name no subject either, and `not` is not on the closed list -- so the
     head test looks at the negator and stops.  Stripping a leading negator and re-running the SAME
     list catches them, which is why this is an arm and not a new word in the list.

⇒ So the test has THREE ARMS -- LEADING, TRAILING and NEGATOR-STRIPPED LEADING -- and the adopted
single-arm figure is a LOWER BOUND on the class.  ** The word list is kept BYTE-FOR-BYTE and the arms
are reported separately, so r7258's and r7257's figures stay reproducible from this file. **
"""
import json
import re

FINITE = r"""is|are|was|were|be|been|being|has|have|had|does|do|did|can|could|may|might|must|
shall|should|will|would|needs?|carry|carries|carried|names?|named|naming|reach|reaches|reached|
remain|remains|remained|determine|determines|determined|puts?|put|moved?|moves|gives?|gave|given|
makes?|made|takes?|took|taken|states?|stated|says?|said|shows?|shown|leaves?|left|holds?|held|
starts?|started|sits?|sat|rests?|rested|lies?|lay|runs?|ran|acts?|acted|goes|went|comes?|came|
enters?|entered|returns?|returned|fixes|fixed|excluded|included|constrains?|constrained"""
_FINITE1 = FINITE.replace('\n', '')

# the adopted first cut, kept BYTE-FOR-BYTE so the r7258 figures stay reproducible from this file
LEAD = re.compile(r'^(?:' + _FINITE1 + r'|and|or|but|so|then|than|that|which|with|without|'
                  r'for|from|into|onto|across|through|by|at|in|on|of|to|as|per|rather)\b', re.I)
STRIP = re.compile(r'^[^A-Za-z]+')

# ⓐ the determiner exemption
_DET = re.compile(r'^(that|this|these|those|which|what|whose)\b', re.I)
_FIN_ANY = re.compile(r'\b(?:' + _FINITE1 + r')\b', re.I)
_WORDS = re.compile(r"[A-Za-z][A-Za-z'\-]*")
# a demonstrative DETERMINER is followed by its noun, never by another function word: that is the
# discriminator between `That sentence constrains ...` (a subject) and `that the walls are three`
# (a subordinate clause).  Closed list, stated rather than learned.
_FUNC = frozenset('''a an the this that these those its their his her our your my no any some each
every all both either neither which what whose there it he she they we i you one two three four five
and or but nor so than as if when where while because since unless though although of to in on at by
for from into onto with without within across through over under between among against about upon
toward towards via per rather is are was were be been being has have had does do did can could may
might must shall should will would'''.split())

# ⓑ the trailing arm: a span may not END on a word that promises a continuation
TRAIL = re.compile(r'\b(?:and|or|but|nor|so|than|that|which|whose|whom|with|without|within|for|from|'
                   r'into|onto|across|through|throughout|by|at|in|on|of|to|as|per|rather|while|'
                   r'whereas|because|since|unless|though|although|if|when|where|upon|under|over|'
                   r'between|among|against|about|toward|towards|via|是)[\s\W]*$', re.I)


def dangles_leading_adopted(lit):
    """the test exactly as r7257 adopted it -- kept for comparability, errors and all"""
    return bool(LEAD.match(STRIP.sub('', lit)))


# ==================================================================================================
# ⛔⛭⛭⛭ THE BORROWED EXEMPTION, REPAIRED r7294+60 ON 66's r7289 ORDER ① -- THE 78th MEMBER.
#
# ** THE DEFECT. **  The exemption below was written for ONE caller: arm ⓐ's leading head test,
# which fires on `that|this|these|those|which|what|whose` because each is also a subordinator.
# Scoped there, matching DEMONSTRATIVES ONLY is not a limitation -- it is the whole of the class the
# arm can wrongly catch, since `LEAD` never fires on `a` or `the`, so there is nothing else to
# exempt.
#   ⇒ ** Then r7285's PRONOUN-SUBJECT arm BORROWED it, and a subject test has no such luck: it
#     asks whether a span names its own subject, and `a symmetry-breaking modulus is ...` names one.
#     Measured at r7288: the borrowed form read 3 of 11 disputed spans where its own three
#     conditions, over the whole determiner class, read 6. **
#   ⌈ ⛭⛭ 66's ruling: *AN EXEMPTION IS CORRECT ONLY INSIDE THE TEST IT WAS WRITTEN FOR, AND
#     BORROWING IT CARRIES THE EXEMPTION WITHOUT ITS CONDITIONS.*
#   ⌊ ⌗ Which is this line's own fail-on-success class one level up: a predicate carries its
#     scope in a comment, and the comment does not travel with the call.
#
# ** THE REPAIR, AND WHY IT IS NOT A FLAG WITH A DEFAULT. **  A default is exactly how a borrower
# inherits a defect silently -- it is this defect again, one call deep.  So `within` is REQUIRED and
# it names THE TEST THE EXEMPTION IS BEING USED INSIDE, from a closed set:
#     'leading-dangling-arm'  the arms below.  Demonstratives only, byte-identical to the adopted
#                             behaviour, because that is the class those arms can wrongly catch.
#     'subject-test'          any test asking whether a span names its own subject.  The SAME three
#                             conditions over the FULL closed determiner class.
# ** A caller that does not say which it is gets a TypeError at its own call site rather than a wrong
# answer at ours **, which is the exemption carrying its conditions instead of describing them.
#   ⚠ The three conditions are written ONCE, in `_subject_by_determiner`, so the two scopes differ
#     in their determiner class and in nothing else.  A repair to the conditions reaches both.
# ==================================================================================================
#: the two determiner classes -- the ONLY difference between the two scopes
_DET_WORDS = (
    'a an the that those these this its their his her our your my no every each some any all both either neither which what whose'
).split()
_DET_SCOPE = {
    'leading-dangling-arm': _DET,
    #: the full closed class, stated and not learned, longest-first so `the` cannot shadow `these`.
    #: `_FUNC` already carries exactly these words; this is that list as a head test.
    'subject-test': re.compile(
        r'^(?:' + '|'.join(sorted(_DET_WORDS, key=len, reverse=True)) + r')\b', re.I),
}


#: ⛔⛭⛭ A FOURTH CONDITION THE WIDE CLASS NEEDS AND THE NARROW ONE NEVER DID, found by measuring
#: this repair's own blast radius before landing it (r7294+60).  Widening the determiner class makes
#: the test reach `a harmonic oscillator, whose Hamiltonian is bounded below` -- which P10 writes as
#: an APPOSITION inside `that sector is ..., a harmonic oscillator, whose ...`, so its subject sits
#: OUTSIDE the span and header ⓸ rules it dangling.  The demonstrative class never reached a span
#: like that, so the condition was never needed there.
#:   ⇒ ** The discriminator is the COMMA, not the relative pronoun: a non-restrictive relative
#:     after a comma carries the span's only finite verb, so the span has no main verb of its own.
#:     `a consistency check that matches nothing is green forever` has a RESTRICTIVE relative with no
#:     comma and does name its subject, which is why the test is comma-gated and not word-gated. **
_APPOS_REL = re.compile(r',\s*(?:whose|which|who|whom|that)\b', re.I)


def _subject_by_determiner(lit, head_re):
    """the conditions, written once: the head is a determiner of `head_re`'s class, the next word is
    not a function word or a verb form, a finite verb comes later, and that finite verb is not inside
    a non-restrictive relative clause -- so the span has a subject and a predicate OF ITS OWN, the
    leading-conjunction reading is unavailable, and an apposition whose head sits outside the span is
    not mistaken for a subject."""
    head = STRIP.sub('', lit)
    if not head_re.match(head):
        return False
    w = _WORDS.findall(head)
    if len(w) < 3:
        return False
    if w[1].lower() in _FUNC or _FIN_ANY.fullmatch(w[1]):
        return False
    m = _FIN_ANY.search(' '.join(w[2:]))
    if not m:
        return False
    #: the span up to and including its first finite verb, read on the ORIGINAL text so the comma
    #: survives -- `_WORDS` drops punctuation, which is why this is matched against `head`.
    _upto = head[:head.lower().find(m.group(0).lower()) + len(m.group(0))] if m.group(0).lower() in head.lower() else head
    return not _APPOS_REL.search(_upto)

def names_own_subject_by_determiner(lit, within=None):
    """True when the head is a DETERMINER standing in front of its own noun.

    ⚠ `within` is REQUIRED and names the test this exemption is being used inside -- see the block
    above.  `'leading-dangling-arm'` is demonstratives only and is byte-identical to the behaviour
    r7257 and r7258 measured; `'subject-test'` is the same three conditions over the full closed
    determiner class.  Omitting it RAISES, because an exemption that can be borrowed without its
    conditions is the defect this signature exists to make unreachable."""
    if within not in _DET_SCOPE:
        raise TypeError(
            'names_own_subject_by_determiner() requires within=' + ' or '.join(
                repr(k) for k in _DET_SCOPE)
            + '. The demonstrative-only form is correct ONLY inside the leading dangling arm it '
              'was written for: LEAD never fires on `a` or `the`, so there is nothing else there '
              'to exempt. A SUBJECT test must pass within=\'subject-test\', which reads the same '
              'three conditions over the full closed determiner class. r7289 ruling, the 78th '
              'member: an exemption is correct only inside the test it was written for, and '
              'borrowing it carries the exemption without its conditions.')
    return _subject_by_determiner(lit, _DET_SCOPE[within])


def names_own_subject(lit):
    """the SUBJECT-TEST form, for any caller asking whether a span names its own subject.  This is
    the one a subject arm wants, and the demonstrative-only form is not reachable from here."""
    return names_own_subject_by_determiner(lit, within='subject-test')


def dangles_leading(lit):
    """the leading arm with the determiner false positive removed"""
    return dangles_leading_adopted(lit) and not names_own_subject_by_determiner(
        lit, within='leading-dangling-arm')


_NEG = re.compile(r'^(?:not|never|nor|no longer)\s+', re.I)


def dangles_negated(lit):
    """arm ⓒ: the head is a negator, and what follows it is itself a dangling head.  The negator is
    stripped and the ADOPTED list is re-run, so this adds no word to the list."""
    head = STRIP.sub('', lit)
    m = _NEG.match(head)
    if not m:
        return False
    rest = head[m.end():]
    return bool(LEAD.match(rest)) and not names_own_subject_by_determiner(
        rest, within='leading-dangling-arm')


def dangles_trailing(lit):
    """True when the span ends on a conjunction or preposition, promising a continuation it does not
    carry -- the mirror of the leading defect, and invisible to a head test."""
    return bool(TRAIL.search(lit))


def dangles(lit):
    """any of the three arms"""
    return dangles_leading(lit) or dangles_trailing(lit) or dangles_negated(lit)


def rows(path='corpus/quote_pin_baseline.tsv'):
    for line in open(path, encoding='utf-8'):
        c = line.rstrip('\n').split('\t')
        if len(c) >= 7 and c[0].startswith('receipts/'):
            try:
                c[1] = json.loads(c[1])
            except Exception:
                continue
            yield c


# ** THE CONTROLS, two-sided, run on import-free call so the instrument states its own competence **
POSITIVE_LEADING = [
    'is purely imaginary',
    'which mentions no route',
    'which can be non-zero at second order in the metric perturbation',
    'carried continuously from zero at the turnaround',
    'with the wall structure fixing the number at either seat',
    'through which an L1 or L2 quantity appears as distance and redshift',
    'that the walls are three',
]
POSITIVE_NEGATED = [
    'not need a lower bound',
    "not by the peak's value",
    'not that the spectrum has a floor',
]
POSITIVE_TRAILING = [
    'non-geometric but',
    '4$ with a right-handed neutrino and',
    'the three throat walls are distinct loci, so',
]
NEGATIVE = [
    'That sentence constrains the target rather than the mechanism',
    'not a debt',
    'Which modes give the zero is a question about the configuration and not a general rule',
    'the triality class is the fractional part of the charge',
    'the conformal time $\\dd\\eta=\\dd\\tilde\\tau/a$ is purely imaginary',
    'one generation splits $12$ coloured against $3$ colourless ($4$ with a right-handed neutrino)',
    'This paper takes up that opening concretely',
]


def self_test():
    """(all controls pass, the failures) -- a detector that does not state its own competence is a
    claim and not an instrument."""
    bad = []
    for s in POSITIVE_LEADING:
        if not dangles_leading(s):
            bad.append(('expected LEADING dangle', s))
    for s in POSITIVE_TRAILING:
        if not dangles_trailing(s):
            bad.append(('expected TRAILING dangle', s))
    for s in POSITIVE_NEGATED:
        if not dangles_negated(s):
            bad.append(('expected NEGATOR-STRIPPED dangle', s))
    for s in NEGATIVE:
        if dangles(s):
            bad.append(('expected CLEAN', s))
    return (not bad), bad


if __name__ == '__main__':
    ok, bad = self_test()
    print('self-test:', 'ALL PASS' if ok else f'{len(bad)} FAIL')
    for why, s in bad:
        print('   ', why, '::', s)
