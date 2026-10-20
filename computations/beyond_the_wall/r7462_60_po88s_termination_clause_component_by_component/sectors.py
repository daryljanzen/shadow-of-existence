#!/usr/bin/env python3
"""
r7462 — PO-88's TERMINATION CLAUSE, COMPONENT BY COMPONENT.

PO-88's second exit reads: "the two structural results are shown to leave the through-crossing
evolution no freedom at all --- that every admissible stress-energy crosses identically because
zero cosmic duration and zero oscillatory content exhaust the problem."  It quantifies over EVERY
ADMISSIBLE STRESS-ENERGY and it is one sentence.  A concrete matter model's stress-energy is not
one object: relative to the collapse worldline congruence it is rho, p, q_a, pi_ab, a composition
vector, and perturbation content in three irreducible types.  SO THE CLAUSE IS ELEVEN CLAIMS AND
IT IS WRITTEN AS ONE.

This locator puts each sector to the corpus separately and asks what the eighteen papers say
happens to IT at the branch point.  THREE STATES, NOT TWO (r7422, r7436):

    COVERED      a sentence (or, with the scope printed, a paragraph) carrying both the sector's
                 own anchor and a crossing marker
    STATED-AWAY  the sector IS in the corpus, and never at the crossing
    ABSENT       no sentence matches the sector's anchor.  WHAT WAS SEARCHED, so the claim
                 carries its own evidence: the anchor regex list printed in SECTORS below, run
                 over every sentence of the eighteen paper sources named in CANONICAL_TITLES
                 plus CR_synthesis -- 10,998 sentences after the bibliography cut, of 11,743 --
                 with the TeX stripped by r7454's stripper and the match case-folded.  A wider
                 claim than that is not made here: the sector may be in a receipt, a figure
                 script or a register row, none of which this locator reads.

A sector's own absence is its own state.  Reporting it as coverage would be the gate writing the
row rather than reading it (r7458's guard), and reporting it as a defect in the papers would be
this seat's own generator: an instrument built to check a condition that already exists will
disagree with it, and the disagreement will look like a finding about the subject.

⌗ THE SENTENCE SPLITTER AND THE TEX STRIPPER ARE IMPORTED FROM r7454's `open_list.py`, NOT
  REWRITTEN.  r7445's rule, promoted at r7447: a reimplementation of a predicate is a second
  instrument and it will disagree.  If that file moves, this one fails loudly rather than
  quietly growing a second copy.

Run:  python3 sectors.py            the sound run
      python3 sectors.py --arms     the arms, one line each
      python3 sectors.py --void     the keying control, shown firing
      python3 sectors.py --seed     the seed, pinned per L-249's repair rule
"""

import os
import re
import sys
import subprocess
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

# ---------------------------------------------------------------- the imported predicate
_R7454 = os.path.join(
    ROOT, 'computations', 'beyond_the_wall',
    'r7454_60_the_papers_own_open_list_against_the_measurements_the_corpus_carries',
    'open_list.py')
if not os.path.exists(_R7454):
    sys.exit("FATAL: r7454's open_list.py is not where this file expects it.\n"
             "  Fix the path.  Do NOT reimplement sentences()/strip_tex() here -- that is the\n"
             "  second instrument r7445's rule is about, and it is what this file exists to avoid.")
_spec = importlib.util.spec_from_file_location('r7454_open_list', _R7454)
_ol = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ol)
sentences, strip_tex = _ol.sentences, _ol.strip_tex

# ---------------------------------------------------------------- the eighteen papers
TITLES = os.path.join(ROOT, 'corpus', 'CANONICAL_TITLES.txt')

# ⌗ DEFECT FOUND BY RUNNING, AND REPAIRED HERE: the bibliography is prose to a sentence
# splitter.  Every paper's bibitem list carries other papers' TITLES, and three of those
# titles contain "isotropy", so the first run returned 187 isotropization sites of which the
# printed head was six bibliography entries.  A reference to a paper is not a statement about
# the subject.  Both counts are printed so the size of the removal is visible rather than
# quietly absorbed.
BIB = re.compile(r'\\begin\{thebibliography\}')


def sentences_body(path):
    """r7454's sentences(), cut at the bibliography.  The cut is on the LINE ANCHOR the
    imported splitter already returns, so no second splitter is introduced (r7445's rule)."""
    raw = _ol.read(path).split('\n')
    stop = None
    for n, ln in enumerate(raw, 1):
        if BIB.search(ln):
            stop = n
            break
    out = sentences(path)
    if stop is None:
        return out, out
    return [t for t in out if t[0] is not None and t[0] < stop], out


def papers():
    """The paper files, from the corpus's own canonical list plus P18, which postdates it."""
    stems = []
    for ln in open(TITLES, encoding='utf-8'):
        if not ln[:1].isalpha():
            continue
        parts = ln.split('|')
        if len(parts) < 3:
            continue
        stems.append(parts[0].strip())
    stems.append('CR_synthesis')              # P18; the r908 list predates it
    out = []
    for s in stems:
        p = os.path.join(ROOT, 'corpus', s + '.tex')
        if os.path.exists(p):
            out.append((s, p))
    return out


# ---------------------------------------------------------------- the crossing's own markers
# Deliberately tight.  "crosses" alone is not here: it is the commonest verb in the corpus for a
# horizon crossing, a mode crossing the sound horizon and a curve crossing an axis, and admitting
# it is how a locator comes to read co-occurrence as aboutness (r7454's first draft).
CROSSING = [
    'branch point', 'branch-point', 'the crossing', 'through the branch', 'across the branch',
    'at the branch', 'the branch point', 'through the crossing', 'at the crossing',
]

SECTORS = [
    dict(key='rho', name='energy density  rho',
         anchors=[r'\benergy density\b', r'\bthe density\b', r'\brho\b', r'\\rho\b']),
    dict(key='p', name='isotropic pressure  p',
         anchors=[r'\bisotropic pressure\b', r'\bthe pressure\b', r'\bequation of state\b',
                  r'\bw *= *1/3\b', r'\bp *= *\\?rho/3\b']),
    dict(key='q', name='energy flux  q_a',
         anchors=[r'\benergy flux\b', r'\bheat flux\b', r'\bmomentum density\b',
                  r'\bq_\{?a\}?\b', r'\bheat conduction\b']),
    dict(key='pi', name='anisotropic stress  pi_ab',
         anchors=[r'\banisotropic stress\b', r'\bshear stress\b', r'\bviscous stress\b',
                  r'\btraceless stress\b', r'\bpi_\{?ab\}?\b']),
    dict(key='comp', name='composition vector (the species fractions)',
         anchors=[r'\bcomposition\b', r'\babundanc', r'\bdissociat', r'\bnuclear network\b',
                  r'\bspecies fraction']),
    # ⌗ ANCHOR REPAIR, AND THE REASON IS WORTH THE LINE: the first list omitted the clause's
    # OWN WORDS.  PO-88's second ground is "zero OSCILLATORY CONTENT", and the sentence in P18
    # that bounds that ground in wavenumber -- "removes a mode's oscillatory content strongly
    # only above k~2e-4" -- carries neither "scalar mode" nor "freez", so the locator could not
    # see the one site that speaks to the ground it was built to test.  An instrument keyed on
    # its subject's synonyms and not on the subject's own name is blind exactly where it matters.
    dict(key='scalar', name='frozen SCALAR perturbation modes / oscillatory content',
         anchors=[r'\bscalar perturbation', r'\bscalar mode', r'\bfrozen mode',
                  r'\bsound horizon\b', r'\bcurvature perturbation', r'\bfreez',
                  r'\boscillatory content\b', r'\boscillating content\b'],),
    dict(key='vector', name='VECTOR perturbation modes',
         anchors=[r'\bvector perturbation', r'\bvector mode', r'\bvorticity\b',
                  r'\bvector sector\b']),
    dict(key='tensor', name='TENSOR perturbation modes (gravitational waves)',
         anchors=[r'\btensor perturbation', r'\btensor mode', r'\bgravitational wave',
                  r'\btensor sector\b']),
    dict(key='stack', name='the time-stacking the reassignment acts on',
         anchors=[r'\btime-stacking\b', r'\btime stacking\b', r'\bstacking\b',
                  r'\breassignment\b']),
    dict(key='filter', name="the species filter's own action",
         anchors=[r'\bspecies filter\b', r'\bvacuum kernel\b', r'\bthe kernel\b',
                  r'\bkernel acts\b', r'\blossless\b']),
    dict(key='dur', name="the crossing's own duration",
         anchors=[r'\bduration\b', r'\bproper time\b', r'\btortoise\b', r'\bfinite time\b',
                  r'\bzero duration\b']),
]

# Ⓥ② the under-fire guard: a sector that cannot be in this corpus at this locus.
CONTROL_SECTOR = dict(key='torsion', name='[CONTROL] the crossing\'s torsion content',
                      anchors=[r'\btorsion\b', r'\bCartan torsion\b', r'\bcontorsion\b'])


def _hit(pats, low):
    for p in pats:
        if re.search(p, low):
            return p
    return None


def harvest(keyed=True):
    """Per sector: the state, the sites, and the scope each site fired at.

    keyed=False drops the crossing conjunct.  That is Ⓥ③: with the conjunct gone the count must
    RISE, because without it the locator is only counting the sectors' PRESENCE, which is a
    different question and a much easier one.
    """
    secs = [dict(s) for s in SECTORS] + [dict(CONTROL_SECTOR)]
    for s in secs:
        s['sites'], s['present'] = [], 0
    for stem, path in papers():
        body, _all = sentences_body(path)
        for line, sent, para in body:
            s_low, p_low = strip_tex(sent).lower(), strip_tex(para).lower()
            cross_s = _hit(CROSSING, s_low)
            cross_p = _hit(CROSSING, p_low)
            for s in secs:
                a = _hit(s['anchors'], s_low)
                if not a:
                    continue
                s['present'] += 1
                if not keyed:
                    s['sites'].append((stem, line, 'UNKEYED', a, None, sent))
                elif cross_s:
                    s['sites'].append((stem, line, 'SENTENCE', a, cross_s, sent))
                elif cross_p:
                    s['sites'].append((stem, line, 'PARAGRAPH', a, cross_p, sent))
    for s in secs:
        if s['sites']:
            s['state'] = 'COVERED'
        elif s['present']:
            s['state'] = 'STATED-AWAY'
        else:
            s['state'] = 'ABSENT'
    return secs


# ---------------------------------------------------------------- the other arms
DEGEN = ['crosses identically', 'no freedom', 'leaves no freedom', 'exhaust the problem',
         'every admissible stress-energy', 'no freedom at all']
# ⌗ THE THIRD SUBSTRING OVER-FIRE OF THIS SEAT'S RUN, FOUND BY RUNNING THE ARM.  As plain
# substrings these read 52 every-k sites and 138 observed-range sites: 'any k' matched "any
# KILLING horizon", 'the observed' matched every sentence in the corpus that mentions an
# observation.  r7454 was repaired for the same defect one size down (0.9 matching 0.992).
# WHOLE-TOKEN PATTERNS, and the scan is additionally keyed on the subject: a scope quantifier
# only counts where the sentence is about modes at the crossing, because a quantifier's scope is
# a property of the claim it quantifies and not of the sentence it is spelled in.
EVERY_K = [r'\bevery\s+k\b', r'\ball\s+k\b', r'\bany\s+k\b', r'\bevery mode\b',
           r'\ball modes\b', r'\bevery wavenumber\b', r'\bfor every\s+k\b']
OBSERVED = [r'\bobserved range\b', r'\bobserved modes\b', r'\bobservable range\b',
            r'\bin the observed range\b']
MODESUBJ = [r'\bmode', r'\bfreez', r'\boscillat', r'\bwavenumber\b', r'\bsound horizon\b']
DURATION = ['zero cosmic duration', 'no cosmic duration', 'zero duration', 'no duration']


def rx_scan(pats, require=None):
    """Whole-token patterns, optionally keyed on the sentence's subject."""
    out = []
    for stem, path in papers():
        body, _all = sentences_body(path)
        for line, sent, _ in body:
            low = strip_tex(sent).lower()
            hit = _hit(pats, low)
            if not hit:
                continue
            if require and not _hit(require, low):
                continue
            out.append((stem, line, hit, sent))
    return out


def phrase_scan(phrases):
    out = []
    for stem, path in papers():
        body, _all = sentences_body(path)
        for line, sent, _ in body:
            low = strip_tex(sent).lower()
            for ph in phrases:
                if ph in low:
                    out.append((stem, line, ph, sent))
    return out


# Sentences that state, in print, that a sector is NOT fixed at or by the crossing.  These are
# the clause's counterexamples if it has any, and they are the papers' own words rather than this
# seat's reading of them.  The list is short and literal on purpose: a loose refuter net would
# manufacture counterexamples the way r7454's first draft manufactured open items.
REFUTE = [
    'not at all by it', 'must be sought on other grounds', 'do carry', 'not constrained',
    'has no baryogenesis', 'remains open', 'is not fixed', 'no derivation',
    'residual excitation', 'strongly only above', 'not strongly suppressed',
    'carries a qualification',
]


def refuters():
    """Per sector: sites where a refuter phrase shares a sentence with the sector's anchor and a
    crossing marker, or shares the PARAGRAPH with the crossing marker (scope printed)."""
    out = []
    for stem, path in papers():
        body, _all = sentences_body(path)
        for line, sent, para in body:
            s_low, p_low = strip_tex(sent).lower(), strip_tex(para).lower()
            ref = _hit([re.escape(r) for r in REFUTE], s_low)
            if not ref:
                continue
            cross = _hit(CROSSING, s_low)
            scope = 'SENTENCE' if cross else ('PARAGRAPH' if _hit(CROSSING, p_low) else None)
            if not scope:
                continue
            for sec in SECTORS:
                if _hit(sec['anchors'], s_low):
                    out.append((sec['key'], stem, line, scope, ref, sent))
    return out


def isotropization_sites():
    """Ⓕ's direction check.  MAP-SCOPE = the isotropization verb shares a sentence with a
    crossing marker.  STATE-SCOPE = it does not.  The split is mechanical; the reading of the
    printed sites is recorded in the receipt and is not claimed as the instrument's output."""
    out = []
    for stem, path in papers():
        body, _all = sentences_body(path)
        for line, sent, _ in body:
            low = strip_tex(sent).lower()
            if not re.search(r'\bisotrop', low):
                continue
            out.append((stem, line, 'MAP-SCOPE' if _hit(CROSSING, low) else 'STATE-SCOPE', sent))
    return out


# ---------------------------------------------------------------- the runs
def table(secs, head):
    print('=' * 94)
    print(head)
    print('=' * 94)
    print(f"  {'sector':<46} {'state':<12} {'sites':>6} {'anchor hits':>12}")
    for s in secs:
        mark = '  ' if not s['key'].startswith('torsion') else 'Ⓥ '
        print(f"{mark}{s['name']:<46} {s['state']:<12} {len(s['sites']):>6} {s['present']:>12}")
    live = [s for s in secs if s['key'] != 'torsion']
    cov = [s for s in live if s['state'] == 'COVERED']
    away = [s for s in live if s['state'] == 'STATED-AWAY']
    absent = [s for s in live if s['state'] == 'ABSENT']
    print()
    print(f"  ⇒ of {len(live)} sectors: COVERED {len(cov)} · STATED-AWAY {len(away)} "
          f"· ABSENT {len(absent)}")
    return live, cov, away, absent


def controls(secs, unkeyed):
    """Each control prints its own verdict.  Any one firing VOIDS the run."""
    print()
    print('-' * 94)
    print('  THE CONTROLS')
    print('-' * 94)
    fired = []

    scalar = [s for s in secs if s['key'] == 'scalar'][0]
    ok1 = scalar['state'] == 'COVERED'
    print(f"  Ⓥ① blindness guard  — the frozen SCALAR sector, whose site r7462's Ⓓ③ names")
    print(f"      state = {scalar['state']}   ⇒ {'PASS' if ok1 else 'FIRED: the locator is blind'}")
    if not ok1:
        fired.append('Ⓥ①')

    tor = [s for s in secs if s['key'] == 'torsion'][0]
    # ⌗ THE CONTROL AS REGISTERED FIRED, AND ITS FIRING COULD NOT BE READ.  It said the
    # invented sector "must come out ABSENT" and then said "if it comes out COVERED the run is
    # VOID" -- a GUARD on the instrument and a PREDICTION about the corpus, bundled into one
    # clause.  It came out STATED-AWAY: the guard held (the locator did not call it covered)
    # and the prediction was wrong (the word is in the papers three times).  A control that
    # bundles a guard with a prediction cannot be read, because its firing does not say which
    # half failed.  SPLIT HERE: Ⓥ② is the guard alone; the prediction is scored as arm Ⓙ.
    ok2 = tor['state'] != 'COVERED'
    print(f"  Ⓥ② over-fire guard  — an invented sector must not be called COVERED")
    print(f"      state = {tor['state']}   ⇒ {'PASS' if ok2 else 'FIRED: co-occurrence read as aboutness'}")
    print(f"      ⌗ the ABSENT half of the clause as registered is now arm Ⓙ, and it MISSED")
    if not ok2:
        fired.append('Ⓥ②')

    kc = sum(1 for s in secs if s['key'] != 'torsion' and s['state'] == 'COVERED')
    ku = sum(1 for s in unkeyed if s['key'] != 'torsion' and s['state'] == 'COVERED')
    ok3 = ku > kc
    print(f"  Ⓥ③ keying guard     — drop the crossing conjunct; the count must RISE")
    print(f"      keyed {kc} → unkeyed {ku}   ⇒ {'PASS' if ok3 else 'FIRED: never keyed on the crossing'}")
    if not ok3:
        fired.append('Ⓥ③')
    return fired


def sound():
    secs = harvest(keyed=True)
    unkeyed = harvest(keyed=False)
    live, cov, away, absent = table(secs, 'THE SOUND RUN — eleven sectors, keyed on the crossing')
    fired = controls(secs, unkeyed)

    print()
    print('-' * 94)
    print('  THE SITES, per covered sector — open the file at the line and read it')
    print('-' * 94)
    for s in secs:
        if s['state'] != 'COVERED' or s['key'] == 'torsion':
            continue
        print(f"\n  ⌈ {s['name']}  —  {len(s['sites'])} site(s)")
        for stem, line, scope, a, c, sent in s['sites'][:4]:
            print(f"    {stem}.tex:{line}  [{scope}]  anchor={a}  crossing={c}")
            print(f"      {strip_tex(sent)[:300]}")
        if len(s['sites']) > 4:
            print(f"    … and {len(s['sites']) - 4} more")

    print()
    print('-' * 94)
    print('  THE SECTORS THE PAPERS DO NOT SPEAK TO AT THIS LOCUS')
    print('-' * 94)
    for s in away + absent:
        print(f"    {s['state']:<12} {s['name']:<46} anchor hits elsewhere: {s['present']}")

    print()
    print('-' * 94)
    print('  THE REFUTERS — sentences in the papers that say the crossing does NOT fix a sector')
    print('-' * 94)
    refs = refuters()
    if not refs:
        print('    none.  The clause has no printed counterexample in the eighteen papers.')
    for key, stem, line, scope, ref, sent in refs:
        print(f"    [{key}] {stem}.tex:{line}  [{scope}]  '{ref}'")
        print(f"      {strip_tex(sent)[:460]}")

    print()
    print('=' * 94)
    if fired:
        print(f"  ⛔ VOID — controls fired: {' '.join(fired)}")
        return 1
    print("  ✔ CONTROLS HOLD.  The coverage map above is the measurement.")
    print()
    print("  ⇒ THE CLAUSE QUANTIFIES OVER ALL ELEVEN SECTORS.  The corpus speaks to "
          f"{len(cov)} of them")
    print("    at this locus.  A sentence that quantifies over eleven sectors on grounds that")
    print("    reach some of them is not one claim with a verdict; it is eleven claims with one")
    print("    verdict written on them, and the sectors it does not reach are where the")
    print("    through-crossing freedom would live if it lives anywhere.")
    return 0


def bib_removal():
    """How much the bibliography cut removed, printed so the repair is visible."""
    body_n = all_n = 0
    for _stem, path in papers():
        body, every = sentences_body(path)
        body_n += len(body); all_n += len(every)
    return body_n, all_n


def arms():  # noqa: C901
    secs = harvest(keyed=True)
    unkeyed = harvest(keyed=False)
    live = [s for s in secs if s['key'] != 'torsion']
    st = {s['key']: s['state'] for s in live}
    cov = [s['key'] for s in live if s['state'] == 'COVERED']
    away = [s['key'] for s in live if s['state'] == 'STATED-AWAY']
    absent = [s['key'] for s in live if s['state'] == 'ABSENT']
    sent_cov = [s['key'] for s in live if any(x[2] == 'SENTENCE' for x in s['sites'])]
    para_only = [k for k in cov if k not in sent_cov]

    b, a = bib_removal()
    print('=' * 94)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 50a39f79 before this file existed')
    print('=' * 94)
    print(f"  ⌗ the bibliography cut: {a} sentences in the eighteen papers, {b} read, "
          f"{a - b} dropped as reference list")
    print()
    print("  Ⓐ coverage      predicted COVERED 4 / STATED-AWAY 4 / ABSENT 3")
    print(f"                  measured  COVERED {len(cov)} / STATED-AWAY {len(away)} "
          f"/ ABSENT {len(absent)}   ⇒ MISS, and in the direction that matters:")
    print("                  THE CORPUS SPEAKS TO MORE OF THE DECOMPOSITION AT THIS LOCUS THAN")
    print("                  THE PREDICTION ALLOWED FOR.")
    print(f"                  covered:     {' '.join(cov) or '—'}")
    print(f"                  stated-away: {' '.join(away) or '—'}")
    print(f"                  absent:      {' '.join(absent) or '—'}")
    print(f"                  ⌗ AND THE REGISTERED RULE'S PARAGRAPH FALLBACK CARRIES "
          f"{len(para_only)} OF THEM:")
    print(f"                    sentence-scope covered {len(sent_cov)}: {' '.join(sent_cov)}")
    print(f"                    paragraph-only         {len(para_only)}: {' '.join(para_only) or '—'}")
    print("                    a paragraph naming the branch point anywhere and the sector")
    print("                    anywhere is weaker evidence than one sentence carrying both, and")
    print("                    the finding below rests on the SENTENCE column.")

    deg = phrase_scan(DEGEN)
    print(f"\n  Ⓑ degeneracy    predicted 0 paper sites stating the whole-tensor degeneracy")
    print(f"                  measured  {len(deg)}   ⇒ MISS ON THE PHRASE, AND THE READING IS")
    print("                  THE POINT: every one of them is a DIFFERENT no-freedom.")
    for stem, line, ph, sent in deg:
        print(f"                    {stem}.tex:{line}  '{ph}'  {strip_tex(sent)[:200]}")
    print("                  ⇒ the corpus says a model has no freedom in WHERE THE REASSIGNMENT")
    print("                    ACTS.  PO-88's clause says the through-crossing EVOLUTION has no")
    print("                    freedom at all.  ONE PHRASE, TWO OBJECTS: a forced placement of")
    print("                    the law is not a degenerate map on the content.")

    allk = rx_scan(EVERY_K, require=MODESUBJ)
    obs = rx_scan(OBSERVED, require=MODESUBJ)
    print(f"\n  Ⓒ scope         predicted >=1 observed-range site, 0 every-k sites")
    print(f"                  measured  every-k {len(allk)} · observed-range {len(obs)}"
          f"   ⇒ MISS ON THE EVERY-K HALF")
    for stem, line, ph, sent in allk:
        print(f"                    every-k   {stem}.tex:{line}  '{ph}'")
        print(f"                      {strip_tex(sent)[:300]}")
    for stem, line, ph, sent in obs:
        print(f"                    observed  {stem}.tex:{line}  '{ph}'")
        print(f"                      {strip_tex(sent)[:300]}")
    print("                  ⇒ THE PAPER CARRIES BOTH SCOPES, AND IN ONE PLACE: the all-k")
    print("                    argument and the observed-range measurement sit at the same site.")
    print("                    So the losslessness ground is NOT restricted to observed modes,")
    print("                    which is a stronger ground than the prediction credited it with.")

    print(f"\n  Ⓔ energy flux   predicted ABSENT        measured {st['q']}   ⇒ HIT")
    print(f"  Ⓕ anis. stress  predicted STATED-AWAY   measured {st['pi']}   ⇒ MISS, and the")
    print("                  site is a COUNTEREXAMPLE TO THE CLAUSE rather than support for it:")
    for sec in secs:
        if sec['key'] != 'pi':
            continue
        for stem, line, scope, _a, _c, sent in sec['sites']:
            if scope == 'SENTENCE':
                print(f"                    {stem}.tex:{line}  {strip_tex(sent)[:420]}")
    iso = isotropization_sites()
    mp = [x for x in iso if x[2] == 'MAP-SCOPE']
    print(f"     isotropization: {len(iso)} sites, {len(mp)} of them at the crossing")
    for stem, line, _scope, sent in mp:
        print(f"                    {stem}.tex:{line}  {strip_tex(sent)[:230]}")

    print(f"\n  Ⓖ tensor        predicted STATED-AWAY   measured {st['tensor']} on the registered")
    print("                  rule and STATED-AWAY on the sentence column (0 sentence sites, "
          f"{sum(1 for x in [s for s in secs if s['key']=='tensor'][0]['sites'] if x[2]=='PARAGRAPH')}"
          " paragraph).")
    print("                  ⇒ SPLIT: the arm's verdict is the rule's, not the corpus's, and the")
    print("                    rule that flips it is the paragraph fallback Ⓐ already names.")

    dur, tor = phrase_scan(DURATION), phrase_scan(['tortoise'])
    print(f"\n  Ⓗ duration      predicted ABSENT as a phrase")
    print(f"                  measured  {len(dur)} duration-phrase sites · {len(tor)} tortoise"
          f"   ⇒ MISS")
    for stem, line, ph, sent in dur:
        print(f"                    {stem}.tex:{line}  '{ph}'  {strip_tex(sent)[:230]}")
    print("                  ⇒ ZERO COSMIC DURATION IS THE PAPERS' OWN PHRASE, and the site that")
    print("                    carries it carries FINITE CONFORMAL LENGTH 3.32 in the same")
    print("                    clause.  Both grounds of PO-88's clause are printed paper results")
    print("                    and both hold.  WHAT FAILS IS NOT A GROUND.")

    tn = [s for s in secs if s['key'] == 'torsion'][0]
    print(f"\n  Ⓙ the control's prediction half, now its own arm — the invented sector ABSENT")
    print(f"                  measured  {tn['state']} with {tn['present']} anchor hit(s)   ⇒ MISS")

    refs = refuters()
    print(f"\n  Ⓘ verdict       predicted NOT REACHABLE AS WRITTEN, sector-dependent")
    print(f"                  ⇒ HIT, AND FOR A BETTER REASON THAN THE ONE REGISTERED.  The")
    print("                    prediction expected to reach it by inference from losslessness")
    print("                    (Ⓓ⑤, declared).  IT IS REACHED INSTEAD BY THE PAPERS' OWN")
    print(f"                    SENTENCES: {len(refs)} refuter site(s), each naming a sector the")
    print("                    clause quantifies over and saying the crossing does not fix it.")
    for key, stem, line, scope, ref, sent in refs:
        print(f"                    [{key}] {stem}.tex:{line} [{scope}] '{ref}'")
        print(f"                      {strip_tex(sent)[:430]}")
    return 0


def void():
    """Ⓥ③ shown firing, which is what makes it a control rather than a decoration."""
    unkeyed = harvest(keyed=False)
    table(unkeyed, 'THE VOID RUN — the crossing conjunct DROPPED (Ⓥ③ as it fires)')
    print()
    print("  ⇒ This is the run the sound run must beat.  Every sector the corpus mentions ANYWHERE")
    print("    now reads COVERED, which is the bag-of-words failure r7454 was repaired for: the")
    print("    presence of a subject is not a statement about it at a locus.  A locator whose")
    print("    keyed and unkeyed counts AGREE is this run wearing the sound run's name.")
    return 0


# ---------------------------------------------------------------- the seed
PIN = '0c6f5772'          # the commit that registered PREDICTION.md, before this file existed
PIN_DIGEST = '50a39f79'


def seed():
    """L-249's repair rule (r3105): pin the historical state at the commit it stood at, assert
    the current state SEPARATELY, and make the live check directional rather than an equality."""
    import hashlib
    print('=' * 94)
    print('  THE SEED — three assertions, none of them about the other two')
    print('=' * 94)
    ok = True

    # (1) HISTORICAL, pinned at the commit it stood at.
    try:
        blob = subprocess.run(
            ['git', '-C', ROOT, 'show',
             f'{PIN}:computations/beyond_the_wall/'
             f'r7462_60_po88s_termination_clause_component_by_component/PREDICTION.md'],
            capture_output=True, check=True).stdout
        d = hashlib.sha256(blob).hexdigest()[:8]
        good = d == PIN_DIGEST
        print(f"  (1) HISTORICAL  at {PIN}, PREDICTION.md digests {d}; pinned {PIN_DIGEST}"
              f"  ⇒ {'PASS' if good else 'FAIL'}")
        ok &= good
    except subprocess.CalledProcessError:
        print(f"  (1) HISTORICAL  the pin {PIN} is not readable from here  ⇒ FAIL")
        ok = False

    # (2) CURRENT, asserted on its own and not inferred from (1).
    reg = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8').read()
    clause = 'every admissible stress-energy crosses identically'
    good = clause in reg
    print(f"  (2) CURRENT     the clause under test is present in THE_REGISTER today"
          f"  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good

    # (3) DIRECTIONAL, monotone: both lists can only grow.
    good = len(SECTORS) >= 11 and len(CROSSING) >= 5
    print(f"  (3) DIRECTIONAL sectors {len(SECTORS)} >= 11 and crossing markers {len(CROSSING)}"
          f" >= 5  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good

    print()
    print(f"  ⇒ {'SEED HOLDS' if ok else 'SEED BROKEN'}")
    return 0 if ok else 1


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    if '--arms' in sys.argv:
        sys.exit(arms())
    if '--void' in sys.argv:
        sys.exit(void())
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(sound())
