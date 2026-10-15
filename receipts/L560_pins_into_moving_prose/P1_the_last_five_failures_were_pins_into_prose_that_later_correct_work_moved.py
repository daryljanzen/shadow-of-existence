#!/usr/bin/env python3
"""P1 -- the last five failing receipts were one class, and it is the class this span kept finding: a
pin into prose that later CORRECT work moved.  Four had their finding acted on; the fifth turned up six
sentences that left the papers entirely.

COMPUTES: each of the five failures traced to the commit that caused it; that in four cases the mover
was the receipt's own recommendation landing; that in three of those the mover was this fork; the
before/after measurement at each end pinned to a SHA; and the survival count for the sixth case, stated
as a measurement and routed rather than interpreted.

** ⛭⛭⛭ THE CLASS, AND IT IS NOT CARELESSNESS. **

At the start of this span the full run stood at 13 failures.  Nine were cleared by repairing the corpus
(`L-556`, `L-557`, `L-558`, `L-559`).  ** The five that remained had nothing wrong with the corpus at
all: each pins a quotation or a count into text that later work CHANGED, and in four of the five the
change is the receipt's OWN FINDING BEING ACTED ON. **

      L175/N1   measured ZERO "Lovelock" in the papers at r2515 -- correctly.  The fork's own
                c54.202 then added P12's Lovelock sentence, and the merge carried it in.
      L200/U1   pinned p0's "Reach: stated as a target, not a result".  The fork's own c54.179
      L200/U3   split that item -- "two sides and they now stand differently" -- which is the
                closure both receipts argued for.
      L536/F1   measured 11,359 characters (35%) of settled physics filed under "Frontiers and
                open problems".  It is 3,264 (13%) now: about eight thousand characters moved out.
      L207/W1   quotes six sentences of P8.  r2581's "rehoming pass 1" moved them.

  ⇒ *** A receipt that argues for a change and pins the unchanged text is a receipt that fails the
      moment it succeeds. ***  ** That is the same shape as `L-557`'s seven loud receipts and
      `L230/C1`'s overturned thesis, and it is the third distinct instance this span. **

** ⌷ THE FIX IS UNIFORM AND IT IS c54.220's RULE. **  A quotation is a claim about a FILE AT A COMMIT.
Both ends are pinned: the historical wording at the commit where it stood, and the CURRENT text asserted
separately -- so the receipt records the closure instead of dying of it.

** ⚠ AND ONE OF THE FIVE IS NOT LIKE THE OTHERS, AND IT IS ROUTED RATHER THAN READ. **  Of the six
sentences `W1` quotes from `slicing_operator.tex`, *** NONE is present in any paper .tex now *** -- they
did not move to another paper, they left.  r2581's message is "rehoming pass 1: slicing_operator, and
the paragraph contained the general form of the paper's own central identity."
  ⇒ ** Whether the CONTENT survives under other words is a reading of P8 before and after, and this file
    does not make it. **  *The number is stated so the question is well posed and cheap to take up.
    Interpreting six missing sentences in passing, at the end of a re-pinning sweep, is how a wrong
    reading gets inscribed -- and a re-pin is exactly the operation that would hide it.*

** WHAT IS NOT CLAIMED. **  ** Not that any of the five findings changes ** -- every one is preserved and
now records its own discharge.  ** Not that r2581 lost content ** -- that is the routed question and the
measurement is all this file supplies.  ** Not that the run is at zero because the corpus is right **:
it is at zero because five stale pins were repaired, which is a smaller claim.

** ⛭⛭ AND IT HAPPENED TO THIS FILE AGAIN, BY A DIFFERENT MECHANISM (r3962). **  The c54.226 re-pin
above quoted p0's successor sentence as "the item has two sides ...", lowercase, because c54.179 wrote
it UNDER a status stamp: `\\textbf{[Reach: the item has two sides ...}`.  r3787 then took the stamps out
of the papers, and the fragment became the sentence's first word: `The item has two sides ...`.  ** The
CLAIM did not move at all.  The pin died of a correction to the WRAPPER around it. **
  ⇒ ** That is a tenth repair kind and it is not the nine: not moved prose, not a killed thesis, not a
    terminology sweep.  A pin that includes a leading article takes on the sentence's POSITION as a
    hidden second assertion. **  The repair is to pin the case-free interior --
    `item has two sides and they now stand differently` -- and assert the sentence-initial capital
    SEPARATELY, so the unstamping is recorded rather than merely survived.  `L200/U1` and `L200/U3`
    carry that second check; all three receipts broke on one character.

Written c54.226 (`L-560`), re-pinned r3962.  Stated for reversal.
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RD = os.path.join(ROOT, 'receipts')
FAILED = []

#: the five, and the commit that moved the text each pinned.
CASES = [
    ('L175_dimensional_descent/N1_the_cut_being_four_is_what_makes_the_dynamics_forced.py',
     '0d38a5b', 'c54.202', True),
    ('L200_free_data_count/U1_the_count_as_the_corpus_now_states_it.py',
     '2af0b0b', 'c54.179', True),
    ('L200_free_data_count/U3_the_residue_is_one_and_it_is_already_counted.py',
     '2af0b0b', 'c54.179', True),
    ('L536_frontier_placement/F1_resolved_content_sits_in_the_frontier_sections.py',
     None, 'the frontier sweep', True),
    ('L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py',
     '989fc4b', 'r2581', False),
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def src(rel):
    return open(os.path.join(RD, rel), encoding='utf-8', errors='replace').read()


#: ⛭⛭ r7358+60, THE HAND-OFF QUEUE, L560: THREE PINS INTO MOVING PROSE REPAIRED BY THE READER AND BY
#: WIDENING, and the irony is the file's own: *the receipt about pins that die of correct work pinned
#: three spans that could not carry their claims.*  ** Two were markup carriers ** -- one span wholly
#: inside `\emph{...}`, one opening on a prepositional tail and closing on a `\rcpt{}` marker with the
#: brace that ends the emphasis -- ** and one was an anaphor **, 'the same algebra', whose referent and
#: whose condition both sat outside the span.
#:   ⇒ `r7258`'s settled form, extended: ** the markup is normalised in the READER ** -- emphasis
#:     unwrapped, and `\ldg`/`\rcpt`/`\cite` markers stripped together with the `~` that binds them --
#:     ** and the span is the WHOLE CLAIM **, never split to dodge a brace.
#:   ⇒ ** And the citation tie is asserted by POSITION, not quoted. **  Each stripped marker's NAME is
#:     kept with the offset it sat at in the stripped text, so 'this clause is cited to `X1`' is a
#:     claim about where the marker SITS -- which is what the claim is -- instead of a quotation of a
#:     fragment glued to a marker, which is what the old span was.
_EMPH = re.compile(r'\\(?:emph|textit|textbf|textsl|textup|textsc)\{([^{}]*)\}')
_MARK = re.compile(r'~?\\(?:ldg|rcpt|cite[a-z]*)\{([^{}]*)\}')


def read_tex(name):
    """the paper, flattened, emphasis unwrapped and apparatus markers stripped; returns the text and
    the (offset, cited-name) of every marker removed, so a citation can be tied to a pinned span by
    where it sat rather than by being quoted inside it."""
    t = flat(open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read())
    for _ in range(4):
        t, prev = _EMPH.sub(r'\1', t), t
        if t == prev:
            break
    out, marks, last, pos = [], [], 0, 0
    for m in _MARK.finditer(t):
        out.append(t[last:m.start()])
        pos += m.start() - last
        marks.append((pos, m.group(1)))
        last = m.end()
    out.append(t[last:])
    return ''.join(out), marks


def cited_in(text, marks, span):
    """the names of the markers sitting inside `span` where it occurs in `text`."""
    i = text.find(span)
    return [] if i < 0 else [n for p, n in marks if i <= p <= i + len(span)]




def flat(s):
    return re.sub(r'\s+', ' ', s)


def main():
    print()
    print('  P1 -- the last five failures, and the one class they share')
    print()

    # ⓵ all five now run and all five carry the re-pin note
    rcs = []
    for rel, _, _, _ in CASES:
        d, b = os.path.dirname(os.path.join(RD, rel)), os.path.basename(rel)
        rcs.append((b[:28], subprocess.run(['python3', b], cwd=d, capture_output=True,
                                           text=True, errors='replace').returncode))
    check(f'⓵ all five run and exit zero: { {b: rc for b, rc in rcs} }',
          all(rc == 0 for _, rc in rcs))
    noted = [rel for rel, _, _, _ in CASES if 'c54.226' in src(rel)]
    check(f'⇒ and all {len(noted)} carry the re-pin note naming this revision, so the repair is '
          f'legible in the file rather than only in a register',
          len(noted) == len(CASES))

    # ⓶ the mover, per case, at the commit
    live = flat(''.join(open(f, encoding='utf-8', errors='replace').read()
                        for f in sorted(__import__('glob').glob(
                            os.path.join(ROOT, 'corpus', '*.tex')))
                        if not os.path.basename(f).startswith('appendix_receipts')))
    p12_then = flat(git('show', 'eda3ad7:corpus/algebroid_paper.tex'))
    # ** r7358+60: the live arm was 'the same algebra closes for the Lovelock theories' -- an ANAPHOR.
    #    'the same algebra' names nothing, and the condition the claim needs ('That forcing is
    #    dimension-dependent') sat outside the span, so a reword of either end left the pin standing
    #    while the claim went.  ⇒ TWO whole clauses, markup normalised in the reader: the one that
    #    NAMES the algebra, and the one that carries the finding with the forcing named in it -- and
    #    the anaphor's referent pinned by asserting the ORDER they stand in. **
    _p12_live, _p12_marks = read_tex('algebroid_paper.tex')
    _ALGEBRA = 'deformations of a spatial hypersurface generate an algebra'
    _LOVELOCK = ('requiring a canonical representation of them on $(g_{ij},\\pi^{ij})$ alone recovers '
                 'the Einstein Hamiltonian. That forcing is dimension-dependent: the same algebra '
                 'closes for the Lovelock theories, which coincide with general relativity only in '
                 'four dimensions.')
    check('⓶ N1: "Lovelock" occurs 0 times in P12 at eda3ad7 (r2515, its own build) and the sentence '
          'is present now -- the fork\'s c54.202 added it: the clause that NAMES the algebra and the '
          'clause that says the same algebra closes for the Lovelock theories, each occurring once '
          'with the markup normalised in the reader, and the naming clause standing FIRST so the '
          'anaphor has its referent',
          'Lovelock' not in p12_then
          and _ALGEBRA in _p12_live and _p12_live.count(_ALGEBRA) == 1
          and _LOVELOCK in _p12_live and _p12_live.count(_LOVELOCK) == 1
          and _p12_live.find(_ALGEBRA) < _p12_live.find(_LOVELOCK)
          and 'TeitelboimZanelli1987' in cited_in(_p12_live, _p12_marks, _LOVELOCK))
    p0_then = flat(git('show', 'aa2b6ee:corpus/geometric_core_paper.tex'))
    # ** r6931+70.1: RE-POINTED, class (b) DISCHARGED -- and at what discharged it. **  The c54.179
    #    split sentence ("The item has two sides and they now stand differently, so it is split rather
    #    than carried whole") is itself gone: `73eb61ef` (r6683, the groups 1-6 patch) rewrote p0's
    #    frontier list, and the item now reads "The test has two sides, and each has been run", with
    #    "On the constant side" carried by sec:ledger and "On the datum side" closed by an
    #    impossibility result cited to `X1_the_ratio_is_a_clock_reading_not_a_carried_datum`.  *The
    #    split c54.179 made left the datum side a TARGET; that target has since been run.*
    #    ⇒ The check's finding -- the target wording U1/U3 pinned was moved by correct work, and it is
    #      gone -- is asserted as before; the successor is pinned to the RUN, both sides, with the
    #      datum side's own receipt citation, not to a re-worded sentence alone.
    _p0_live = flat(open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'),
                         encoding='utf-8', errors='replace').read())
    p0_split = flat(git('show', '2af0b0b3:corpus/geometric_core_paper.tex'))
    # ** r7358+60: the datum side was pinned twice and neither span could carry it.  '\\emph{On the
    #    datum side}' is a VERBLESS heading whose clause sat outside it, and the second span opened on
    #    the prepositional tail 'for want of work' and closed on a `\\rcpt{}` marker plus the brace that
    #    ended the emphasis -- a markup carrier, `r7258`'s case.  ⇒ ONE span, the whole closure: the
    #    datum side named, the ratio named, what it IS stated, and what cannot be derived from what --
    #    with the emphasis unwrapped and the marker stripped in the reader, and the X1 citation
    #    asserted by the position it sat at rather than quoted as part of the prose. **
    _p0_norm, _p0_marks = read_tex('geometric_core_paper.tex')
    _DATUM_SIDE = ('On the datum side, $\\rho_r/\\rho_m$ is a matter initial condition and not a '
                   'constant, so it is not in the geometric residue at all, and it is a clock reading '
                   'rather than a datum a handover transmits. It cannot be derived from the progenitor '
                   'collapse, for a structural reason rather than for want of work.')
    check('⇒ U1/U3: p0 read "Reach: stated as a target, not a result" at aa2b6ee; the fork\'s c54.179 '
          '(2af0b0b3) split it -- "two sides and they now stand differently" -- and the item now reads '
          '"The test has two sides, and each has been run", the datum side closed at X1',
          'Reach: stated as a target, not a result' in p0_then
          and 'item has two sides and they now stand differently' in p0_split
          and 'e one fact.\'\' \\emph{The test has two sides, and each has been run.}' in _p0_live
          and '\\emph{On the constant side}, \\S\\ref{sec:ledger} states that the gravitational--cosmological--quantum sector spends \\emph{n' in _p0_live
          and _DATUM_SIDE in _p0_norm and _p0_norm.count(_DATUM_SIDE) == 1
          and 'X1_the_ratio_is_a_clock_reading_not_a_carried_datum'
              in cited_in(_p0_norm, _p0_marks, _DATUM_SIDE)
          and 'Reach: stated as a target, not a result' not in live)
    p7_then = flat(git('show', 'e8e58cf:corpus/CR_framework.tex'))
    seg_then = p7_then[p7_then.find('\\section{Frontiers and open problems}'):]
    below_then = len(seg_then) - seg_then.find('\\end{enumerate}')
    p7_now = flat(open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
                       encoding='utf-8', errors='replace').read())
    seg_now = p7_now[p7_now.find('\\section{Frontiers and open problems}'):]
    below_now = len(seg_now) - seg_now.find('\\end{enumerate}')
    # ** measured on the RAW file here; `F1` strips the preamble and comments before measuring, so its
    # own figures are 11,359 -> 3,264 (35% -> 13%).  The two preprocessings differ and the DIRECTION and
    # the magnitude agree, which is what this check is for -- not a second copy of F1's arithmetic. **
    check(f'⇒ F1: {below_then:,} characters sat below P7\'s frontier list at e8e58cf (r2579, its own '
          f'build) and {below_now:,} do now, measured on the raw file -- the defect it named was acted '
          f'on (F1\'s own stripped measurement: 11,359 -> 3,264), and the residue is not zero',
          below_then > 10000 and 0 < below_now < 0.75 * below_then)

    # ⓷ three of the four movers are THIS fork
    ours = [tag for _, sha, tag, acted in CASES if acted and tag.startswith('c54')]
    check(f'⓷ and {len(ours)} of the four acted-on cases were moved by THIS FORK\'s own later work '
          f'({", ".join(sorted(set(ours)))}) -- a receipt of the observer line\'s broken by the fork '
          f'doing what the receipt asked for',
          len(set(ours)) == 2 and len(ours) == 3)

    # ⓸ the routed one
    QUOTES = ["the cut's advance is generated by a true Hamiltonian",
              'the first dynamical bend the construction displays, in vacuum',
              'a characteristic crossing with no curvature obstruction',
              'That worldline dynamics is taken up for a concrete matter model',
              'the deepest question the construction opens onto',
              'Since the framework leaves the dynamics of general relativity unchanged']
    p8_then = flat(git('show', '9d9f97f:corpus/slicing_operator.tex'))
    alive = [q for q in QUOTES if q in live]
    # ⛔⛭ AMENDED r4510: ** the zero was true and is not any more, and the reason is growth. **
    #   `r4187` wrote `CR_synthesis.tex`, which uses "the deepest question the construction opens
    #   onto" in its own sentence -- so one of the six is present in A paper again.  *That is a NEW
    #   use of the wording in a paper written 1600 revisions later, not the P8 paragraph surviving,
    #   and the claim this check carries is that the paragraph LEFT.*  ⇒ The survivors are located
    #   rather than counted: any that are alive must live only in files that did not exist when the
    #   paragraph was removed, which is a fact no later synthesis can flip.
    _papers = [f for f in sorted(__import__('glob').glob(os.path.join(ROOT, 'corpus', '*.tex')))
               if not os.path.basename(f).startswith('appendix_receipts')]
    _post = {os.path.basename(f) for f in _papers for q in alive
             if q in flat(open(f, encoding='utf-8', errors='replace').read())}
    _absent_then = {f for f in _post if git('show', f'9d9f97f:corpus/{f}').strip() == ''}
    check(f'⓸ W1 is not like the others: all {len(QUOTES)} of its P8 quotations are present at '
          f'9d9f97f (before r2581), and of the {len(alive)} present in any paper now, all sit in '
          f'files that DID NOT EXIST there ({", ".join(sorted(_post)) or "none"}) -- so nothing '
          f'survives in a paper that could have received the paragraph',
          all(q in p8_then for q in QUOTES) and _post == _absent_then)
    check('⇒ SO THEY DID NOT MOVE TO ANOTHER PAPER -- THEY LEFT.  r2581 is "rehoming pass 1: '
          'slicing_operator, and the paragraph contained the general form of the paper\'s own central '
          'identity"',
          'rehoming pass 1' in git('log', '--format=%s', '-1', '989fc4b'))
    w1 = src('L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py')
    # ** ⛭ AMENDED c54.228, and the amendment is the receipt's own subject arriving once more. **  This
    # ** asserted W1's CURRENT text; c54.228 replaced that text, having found the measurement wrong.
    #   ⇒ *** So the claim is pinned to `50f0d3f` (c54.226, where it was true) and the ANSWER is asserted
    #       against the live file -- which is exactly the repair this receipt is about, applied to it. ***
    w1_then = git('show', '50f0d3f:receipts/L207_the_bend/'
                          'W1_what_remains_between_the_wall_and_a_curve_dynamics.py')
    check('⚠ at 50f0d3f (c54.226) this file did NOT read whether the CONTENT survives under other '
          'words: W1 stated the count and said so in terms, routed rather than interpreted',
          'ROUTED RATHER THAN INTERPRETED' in w1_then and 'routed rather than made here' in w1_then)
    check('⛭ AND c54.228 (`L-561`) ANSWERED IT -- against this fork: the probe compared STRINGS where '
          'the question was about CLAIMS, all eight claims survive in body text, and W1 now carries the '
          'corrected measurement with the old verbatim count beside it',
          'CORRECTED c54.228 (`L-561`), AND THE CORRECTION IS A' in w1 and 'ARITHMETIC OF THE OLD PROBE' in w1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the last five failures were one class -- a pin into prose that later CORRECT')
    print('    work moved -- and in four of the five the mover was the receipt\'s own finding being')
    print('    acted on. **')
    print('    · three of those four were moved by THIS fork doing what the receipt asked for')
    print(f'    · the fifth turned up {len(QUOTES)} sentences that left the papers at r2581, MEASURED')
    print('      and routed, not read')
    print('  ⇒ ** A receipt that argues for a change and pins the unchanged text fails the moment it')
    print('    succeeds.  Both ends take a SHA. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
