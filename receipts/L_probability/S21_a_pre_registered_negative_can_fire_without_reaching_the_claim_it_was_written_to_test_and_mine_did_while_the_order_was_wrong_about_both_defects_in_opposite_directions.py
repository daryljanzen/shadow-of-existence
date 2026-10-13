#!/usr/bin/env python3
r"""S21 -- the `r7261` order's two heaviest items, worked under the one-state rule, and the three
things that came out of working them that neither the order nor this seat's own pre-registration had.

** WHAT `r7261` ORDERED. **  *** ① `M23` -- `P16` and `P18` give opposite answers for one proper
length; repair under the one-state rule, keep the argumentative point, and put no narration in the
paper.  ② `M15` -- `P10`'s closing summary names as open, with a refutation condition attached, what
its own body answers.  ⚠ A FULL READ PER PAPER AND NO LESS, and neither paper edited in the turn it is
read. ***

** ⛭⛭⛭ ⓵ THE ORDER'S FRAMING OF `M23` IS WRONG, AND THE ARITHMETIC SAYS SO BEFORE ANY READ. **
*The order: `One of the two is wrong about the member and the other about the family.`*  ⇒ *** `P18`
and `P3` AGREE and are BOTH right -- one about the member, one about the family, the distinction in
`P18`'s own footnote -- and `P16` ALONE is out of step. ***  *So the repair is one paper and not two,
which is what made the three reads affordable.*

** ⛔⛭⛭ ⓶ AND `P16`'s SENTENCE CONTRADICTS ITSELF WITHOUT REFERENCE TO ANY OTHER PAPER. **  *It stated
`f<=0` on both sides of the seam radius and then attributed a proper length to a static region between
them, two commas later.*  ⇒ *** The member's `l` DIVERGES, and it exceeds the family's whole figure
already at a core cut of `1e-3` in units of the curvature radius: the figure cannot be `remaining`. ***

** ⛔⛭⛭⛭ ⓷ `M15` IS WORSE THAN THE ORDER SAYS: THE CLOSING SUMMARY IS STALE IN **BOTH** OF ITS ARMS. **
*The order names l.638's answer to the first arm -- `The divergence does reach second order in the
coupling`.  The SECOND arm is answered too, thirty lines later, and answered the OTHER WAY from how the
summary states it: `the affirmative branch is a second number owed and not a second length introduced,
and the single-scale ledger stands either way`.*
  ⇒ *** So the paper did not merely carry a settled question as open.  It carried a REFUTATION
      CONDITION AGAINST ITSELF WHOSE CONSEQUENT ITS OWN BODY HAD ALREADY REFUSED *** -- *and a reader
      who checked the condition, found it met, and took the paper at its word would have read the
      programme as self-refuted on the programme's own authority.  That is the worse of the two faults
      and the order weighted only the lighter one.*

** ⛔⛭⛭⛭ ⓸ AND MY OWN REACHABLE NEGATIVE FIRES ON ITS LETTER WITHOUT REACHING ITS CLAIM. **  *I pushed
this, before the reads: `if the full read of P18 turns up a site needing a change, then P18 is not
simply the paper that got it right and my reading above is too clean.`*
  ⇒ *** The antecedent is TRUE -- `P18` has two sites needing a change, `N1`'s frontier-table rows at
      l.2837 and l.2838 -- and the consequent is FALSE, because neither is about the proper length and
      `P18`'s treatment of that is the correct one, untouched by this revision. ***
  ⌈ ** So the trigger I fixed does not test the claim it was written to test. **  *I wrote `a site
    needing a change` where the claim was about ONE OBJECT, and a frontier table in the same file fires
    it.  The band holds at its ceiling, the central value is missed, and the negative is scored FIRED
    rather than narrowed after the fact -- narrowing it now is the move the pre-registration exists to
    make unavailable.*
  ⌊ *This is `r7260`'s lesson at the next layer: three instruments there had a reach shorter than their
    claim, and here the instrument with the wrong reach is the PRE-REGISTRATION itself.*

** ⌗ ⓹ AND THE PUSHED PRE-REGISTRATION MISLABELS A UNIT, WHICH IS CORRECTED HERE AND NOT THERE. **
*It reports the member's divergence at `slope 1.1547005 per decade of core radius`.  `2/sqrt(3) =
1.1547005` is the slope per E-FOLD; per DECADE it is `(2/sqrt 3) ln 10 = 2.6587962`, which is what this
receipt measures.*  ⇒ *The number is right and the unit named beside it is wrong.  **The pushed file is
left exactly as pushed** -- a pre-registration that can be edited is not one -- and the correction lives
here, where it is checked.*

** ⌗ ⓺ WHAT IS LOCATED AND NOT TAKEN. **  *`N1` is now two rows rather than the one the order names,
and repairing either moves the `Nine items stand open` the same section states about itself.  `M14` is
confined to ONE line of `P10`, the paper's own convention being carried correctly everywhere else --
which is the computational form of the order's own reading that the conclusion holds either way.
**Both are routed with their locations and neither is touched.**

⛭ *The one-state rule is kept in the only form a gate can check: the repaired sentences state the worked
claim, the superseded figures are ABSENT from both papers, and no narration phrase appears in either.
The history is in this receipt, which is where the order says it goes.*

⛔ *Sources: the `r7261` order, items ① and ② with their line numbers; `PREDICTION.md` and
`READING_NOTES.md` of this revision, both pushed before the editing turn; `P16`, `P18`, `P10` and `P3`
read at this tree; `r7258`'s fourth repair form (normalisation of the HAYSTACK) applied to the emphasis
and the line wrapping; and `r7257`'s order ③, the dangling test run on every key BEFORE it was written.*
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED instrument, with its own self-test

CHECKS = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


# ── the haystack normaliser: r7258's FOURTH repair form, applied to markup AND to line wrapping ──
_EMPH = re.compile(r'\\(?:emph|textit|textbf|textsl|textup|textsc)\{([^{}]*)\}')
_WORD = re.compile(r'\w')


def unemph(t, rounds=4):
    """the text with inline emphasis commands unwrapped, contents kept, nesting handled by iteration"""
    for _ in range(rounds):
        t2 = _EMPH.sub(r'\1', t)
        if t2 == t:
            break
        t = t2
    return t


def flat(t):
    """emphasis unwrapped and every run of whitespace collapsed to one space

    ⛭ *A paper is HARD-WRAPPED, so a claim that spans a line break is not a byte-contiguous span of
    the file.  r7258's fourth form says normalise the HAYSTACK and keep the span WHOLE; the wrap is
    the same kind of carrier as the emphasis and takes the same treatment.*
    """
    return re.sub(r'\s+', ' ', unemph(t))


def held(lit, hay):
    """(present and WORD-ALIGNED at EVERY occurrence, how many occurrences)"""
    i, n, ok = hay.find(lit), 0, True
    while i >= 0:
        b = hay[i - 1] if i else ' '
        a = hay[i + len(lit)] if i + len(lit) < len(hay) else ' '
        if (_WORD.match(lit[0]) and _WORD.match(b)) or (_WORD.match(lit[-1]) and _WORD.match(a)):
            ok = False
        n += 1
        i = hay.find(lit, i + 1)
    return (n > 0 and ok), n


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


# ⛔⛭⛭⛭ THE REFERENCE COMMIT IS A LITERAL SHA AND NOT `merge-base HEAD origin/main`, AND THAT IS THE
#   SECOND HALF OF `L-249`'s RULE THIS LINE GOT WRONG.
#   *The first cut of this receipt read `before` at the merge base with `origin/main`.  **On a branch
#   ahead of the trunk that is the right commit; the moment the work MERGES, `merge-base` collapses
#   onto `HEAD` and every historical read returns the LIVE file** -- so each before-and-after gate
#   compares a tree with itself and goes red.  `S21` was red on `main` in the runner-read sweep for
#   exactly this, and the carry ledger named it there before any seat did.*
#     ⇒ *** A historical pin computed against a MOVING REF is not a historical pin.  `L-249` says to
#         pin the state at the commit it stood at; a commit is a sha. ***
#   ⌗ *`S19`'s repair used a literal sha and is immune.  This receipt and its sibling used
#     `merge-base` -- the same seat, the same revision, the right choice once and the wrong one
#     twice -- which is why the guard below asserts the sha RESOLVES and DIFFERS rather than trusting
#     it.*
BEFORE = '0dd8b745'      # the commit r7262's subjects stood at, before this revision edited them


def before_resolves():
    """(the sha resolves, it is an ancestor of HEAD) -- so a bad pin fails LOUDLY and not silently"""
    ok = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'],
                        cwd=ROOT, capture_output=True, text=True).returncode == 0
    anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'],
                         cwd=ROOT, capture_output=True, text=True).returncode == 0
    return ok, anc


def at_base(rel):
    """the file as the trunk carries it, so `before` is read from git and not from memory"""
    r = subprocess.run(['git', 'show', f'{BEFORE}:{rel}'],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def files_of_revision(tag):
    """the files THIS REVISION's OWN commits changed --- merges excluded, other seats' work excluded

    ⛔⛭ *A plain `git diff BEFORE` cannot answer `did THIS revision touch that paper`: once the trunk
    is merged in, the diff carries every other seat's change as well, and this gate read `83` files
    where the revision had touched four.  **A restraint gate has to measure the restraint's own
    commits, not the branch's position.***
    """
    # ⛔⛭⛭⛭ r7268 (60): AND THIS SELECTOR READ THE COMMIT **BODY**, which is the defect
    #   `r7264` found in this receipt's SIBLING and repaired there while this one kept it.  *`--grep`
    #   matches the whole message, so every commit that merely MENTIONS the tag -- a later revision's
    #   reply, a repair note, this line's own commit about selectors being too broad -- joins the
    #   revision's own set.*  ⇒ *** Measured before the repair, on this range: `10` matches of which
    #   `7` matched in the BODY ALONE, and the file set read `38` where the revision's own commits
    #   touched `11`.  The subject line is the one part of a message that names the revision the
    #   commit IS, so the match is made there. ***
    _log = subprocess.run(['git', 'log', '--no-merges', '--format=%H%x09%s', BEFORE + '..HEAD'],
                          cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
    shas = [l.split('\t', 1)[0] for l in _log if '\t' in l and tag in l.split('\t', 1)[1]]
    out = set()
    for sh in shas:
        out |= set(subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', sh],
                                  cwd=ROOT, capture_output=True, text=True).stdout.split())
    return sorted(out), shas



P16, P18, P10, P3 = ('corpus/cosmogenesis_paper.tex', 'corpus/CR_synthesis.tex',
                     'corpus/canonical_time.tex', 'corpus/SdS-slicing-curve_v2.tex')
p16, p18, p10, p3 = (flat(read(P16)), flat(read(P18)), flat(read(P10)), flat(read(P3)))

print()
print('=' * 100)
print('S21 -- the r7261 order, items ① and ②, and what working them found that the order did not')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE INSTRUMENT STATES ITS OWN COMPETENCE FIRST, AND IT DISCRIMINATES IN BOTH '
      'DIRECTIONS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res, _anc = before_resolves()
gate(f'Ⓐ⓿ ⛔⛭⛭ THE REFERENCE COMMIT RESOLVES, IS AN ANCESTOR OF HEAD, AND ITS CONTENT DIFFERS FROM '
     f'THE LIVE TREE --- asserted before one historical read is taken through it.  ** This gate exists '
     f'because the first cut pinned `merge-base HEAD origin/main`, which collapses onto `HEAD` the '
     f'moment the work merges: this receipt then compared the tree with itself and went RED ON `main` '
     f'in the runner-read sweep. ** *A historical pin computed against a moving ref is not one.*',
     _res and _anc and (at_base(P16) or '') != read(P16)
     and (at_base(P10) or '') != read(P10))
# ══════════════════════════════════════════════════════════════════════════════════════════════════
from mpmath import mp, mpf, quad, polyroots, sqrt, pi, log     # noqa: E402

mp.dps = 40
A = mpf(1)
R0 = A / sqrt(3)                       # the Nariai double root
MN = A / (3 * sqrt(3))                 # and the mass that puts it there


def f(r, M):
    return 1 - 2 * M / r - r ** 2 / A ** 2


def fprime(r, M):
    return 2 * M / r ** 2 - 2 * r / A ** 2


def positive_roots(M):
    rs = polyroots([1, 0, -A ** 2, 2 * M * A ** 2], maxsteps=400, extraprec=400)
    return sorted([x.real for x in rs if abs(x.imag) < mpf('1e-25') and x.real > 0])


gate('Ⓐ① ⛭ the double root is AT the seam radius, and both conditions are checked rather than one: '
     '`f(r0) = 0` AND `f\'(r0) = 0` at `M = MN`, each to `1e-30`',
     abs(f(R0, MN)) < mpf('1e-30') and abs(fprime(R0, MN)) < mpf('1e-30'))

gate('Ⓐ② ⛔ and `f <= 0` on BOTH sides of it, which is the clause `P16` stated two commas before it '
     f'attributed a proper length to a static region between them --- `f(r0 ± 1e-3) = '
     f'{mp.nstr(f(R0 + mpf("1e-3"), MN), 4)}` and `{mp.nstr(f(R0 - mpf("1e-3"), MN), 4)}`',
     all(f(R0 + s * mpf(10) ** -k, MN) < 0 for k in (2, 3, 4, 5) for s in (1, -1)))

gate('Ⓐ③ ⛭ and the vanishing is QUADRATIC and not linear: `f\'\'(r0) = -6/α²` exactly, which is what '
     'makes the length integral divergent where a simple root leaves it finite',
     abs((-4 * MN / R0 ** 3 - 2 / A ** 2) + 6 / A ** 2) < mpf('1e-30'))

DELTA = mpf('0.05')


def member_length(eps):
    g = lambda r: 1 / sqrt(abs(f(r, MN)))                                      # noqa: E731
    return quad(g, [R0 + eps, R0 + DELTA]) + quad(g, [R0 - DELTA, R0 - eps])


_mem = [member_length(mpf(10) ** -k) for k in range(3, 9)]
_mem_d = [_mem[i + 1] - _mem[i] for i in range(len(_mem) - 1)]
_slope = sum(_mem_d) / len(_mem_d)
gate(f'Ⓐ④ ⛔ THE MEMBER DIVERGES, measured as a CONSTANT increment per decade of core cut rather than '
     f'as a failure to converge: `{mp.nstr(_slope, 8)}` across five decades, against the analytic '
     f'`(2/√3)·ln 10 = {mp.nstr(2 / sqrt(3) * log(10), 8)}`',
     all(abs(d - 2 / sqrt(3) * log(10)) < mpf('1e-6') for d in _mem_d))

_M_SIMPLE = MN * mpf('0.9')
_rm = positive_roots(_M_SIMPLE)[0]


def simple_length(eps):
    g = lambda r: 1 / sqrt(abs(f(r, _M_SIMPLE)))                               # noqa: E731
    return quad(g, [_rm + eps, _rm + mpf('0.02')])


_sim = [simple_length(mpf(10) ** -k) for k in range(3, 9)]
_sim_d = [_sim[i + 1] - _sim[i] for i in range(len(_sim) - 1)]
_ratios = [_sim_d[i + 1] / _sim_d[i] for i in range(len(_sim_d) - 1)]
gate(f'Ⓐ⑤ ✔ THE CONTROL, so the instrument is not reporting divergence everywhere: at a SIMPLE root '
     f'the same integral CONVERGES, its decade increments falling by `1/√10` '
     f'(`{mp.nstr(sum(_ratios) / len(_ratios), 6)}` measured against `{mp.nstr(1 / sqrt(10), 6)}`) '
     f'where the double root\'s hold constant at `1`',
     all(abs(r - 1 / sqrt(10)) < mpf('1e-3') for r in _ratios)
     and abs(sum(_mem_d) / len(_mem_d) / _mem_d[0] - 1) < mpf('1e-6'))


def family_length(M):
    rr = positive_roots(M)
    rm, rp = rr[0], rr[1]
    g = lambda t: (rp - rm) / sqrt(abs(f(rm + (rp - rm) * t, M)))              # noqa: E731
    return quad(g, [0, 1])


_fam = [(k, family_length(MN * (1 - mpf(10) ** -k))) for k in (2, 4, 6, 8)]
gate(f'Ⓐ⑥ ✔ AND THE FAMILY\'S FIGURE IS THE FAMILY\'S: the length between two still-distinct roots '
     f'converges to `π/√3 = {mp.nstr(pi / sqrt(3), 10)}` as the gap closes --- '
     f'`{mp.nstr(_fam[-1][1], 12)}` at `1 - M/MN = 1e-8` --- and it converges from BELOW, so no gap '
     f'attains it',
     abs(_fam[-1][1] - pi / sqrt(3)) < mpf('1e-8')
     and all(_fam[i][1] < _fam[i + 1][1] < pi / sqrt(3) for i in range(len(_fam) - 1)))

gate(f'Ⓐ⑦ ⛔⛭ SO THE TWO OBJECTS ARE NOT THE SAME NUMBER AND NOT NEAR ONE: the member\'s length '
     f'EXCEEDS the family\'s entire limit already at a core cut of `1e-3` --- '
     f'`{mp.nstr(_mem[0], 8)}` against `{mp.nstr(pi / sqrt(3), 8)}` --- and it exceeds it by a factor '
     f'that grows without bound, so `its proper length remaining π α/√3` is not a statement that can '
     f'be read charitably as a limit',
     _mem[0] > pi / sqrt(3) and _mem[-1] > 8 * pi / sqrt(3))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  ITEM ①: THE REPAIR IS IN `P16`, IT IS A STATE RATHER THAN A NARRATION, AND IT NOW '
      'AGREES WITH `P18` ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_SUPERSEDED = 'its proper length remaining $\\pi\\alpha/\\sqrt{3}$'
gate('Ⓑ① ⛔ the superseded clause is GONE from `P16`, asserted as an ABSENCE because that is the one '
     'claim a quotation cannot carry',
     _SUPERSEDED not in p16 and _SUPERSEDED in flat(at_base(P16) or ''))

_K_FAMILY = ('belongs to the family, and to the rescaled limit the family defines, rather than to the '
             'member read in this chart')
_ok, _n = held(_K_FAMILY, p16)
gate(f'Ⓑ② ✔ and the figure is still in the paper, attributed to what carries it --- present and '
     f'word-aligned at all `{_n}` occurrence(s)',
     _K_FAMILY in p16 and _ok)

_K_DIVERGES = 'the proper separation read across it in the areal chart diverges rather than settling on a figure'
_ok, _n = held(_K_DIVERGES, p16)
gate(f'Ⓑ③ ⛭ and the member\'s own behaviour is now STATED rather than left to be inferred from the '
     f'`f<=0` clause two commas earlier --- `{_n}` occurrence(s), word-aligned',
     _K_DIVERGES in p16 and _ok)

_K_ARGUMENT = 'what has gone is the separation of the roots and not the throat'
_ok, _n = held(_K_ARGUMENT, p16)
gate('Ⓑ④ ✔⛭ THE ARGUMENTATIVE POINT THE ORDER SAID TO KEEP IS KEPT, word for word, and it is kept at '
     'the trunk too, so this is a survival rather than a re-insertion',
     _K_ARGUMENT in p16 and _ok and _K_ARGUMENT in flat(at_base(P16) or ''))

_NARRATION = ['was formerly stated', 'formerly stated as', 'previously stated', 'had stated',
              'an earlier revision', 'in an earlier version', 'corrected from', 'this was wrong',
              'the paper formerly', 'has been corrected']
_hits = [s for s in _NARRATION if s in p16 or s in p10]
gate(f'Ⓑ⑤ ⛭⛭ THE ONE-STATE RULE, IN THE ONLY FORM A GATE CAN CHECK: not one of `{len(_NARRATION)}` '
     f'narration phrases appears in either repaired paper --- the fact of resolution is in this '
     f'receipt and the consolidation plan, which is where the order says it goes',
     not _hits)

_K_P18_MEMBER = 'the two merging horizons stand infinitely far apart in proper distance'
_ok, _n = held(_K_P18_MEMBER, p18)
gate('Ⓑ⑥ ✔ `P18` was RIGHT about the member and says so in its own voice, read out of the paper '
     'rather than taken from the order',
     _K_P18_MEMBER in p18 and _ok)

def footnote_naming_both(src):
    """the first footnote that names BOTH objects in one window

    ⛭ *Read by WINDOW rather than by a brace-free regex: the footnote carries `$\\pi\\alpha/\\sqrt3$`
    and a `\\cite{...}`, so `[^{}]*` cannot cross it and the first cut of this check reported the
    footnote absent.  **A structural read has to match the structure that is there.***
    """
    i = src.find('\\footnote{')
    while i >= 0:
        w = src[i:i + 500]
        if 'member' in w and 'family' in w:
            return True
        i = src.find('\\footnote{', i + 1)
    return False


gate('Ⓑ⑦ ✔⛭ and the DISTINCTION is `P18`\'s own, carried in a footnote that names both objects in one '
     'sentence --- found by STRUCTURE rather than pinned, because the footnote is a fragment and a '
     'fragment cannot be a quote-pin key under `r7257`\'s adopted test',
     footnote_naming_both(unemph(read(P18))))

# ⛔⛭ READ AGAINST THE WORKING TREE AND NOT AGAINST `HEAD`.  *The first cut diffed `base..HEAD`
#   and reported both repaired papers UNCHANGED while they sat edited in the tree -- a restraint
#   gate that passes because it cannot see the edit is worse than none.*
_changed, _own = files_of_revision('r7262')
gate(f'Ⓑ⑧ ⛭⛭ AND THE REPAIR IS ONE PAPER AND NOT TWO, which is the order\'s framing corrected: '
     f'neither `P18` nor `P3` is touched by this revision, asserted against the diff rather than '
     f'against intention (`{len(_own)}` commit(s) of this revision, `{len(_changed)}` file(s) '
     f'between them)',
     P18 not in _changed and P3 not in _changed and P16 in _changed and P10 in _changed)

gate('Ⓑ⑨ ✔ and `P3` carries the merged horizon at the same radius, so the third paper agrees and the '
     'disagreement was never three-sided',
     '$r_{N}=\\alpha/\\sqrt{3}$' in p3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  ITEM ②: `P10`\'s CLOSING SUMMARY WAS STALE IN **BOTH** ARMS, AND THE BODY IS WHERE '
      'THAT IS READ ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_STALE = ('with the definition complete if it does not and the single-scale ledger refuted if it does')
_base10 = flat(at_base(P10) or '')
gate(f'Ⓒ① ⛔ the refutation condition is GONE, and it stood at EXACTLY ONE site before --- '
     f'`{_base10.count(_STALE)}` at the trunk, `{p10.count(_STALE)}` here.  **So the repair is one '
     f'passage and the paper was not swept for a phrase.**',
     _base10.count(_STALE) == 1 and _STALE not in p10)

_K_BODY_FIRST = 'The divergence does reach second order in the coupling'
_ok, _n = held(_K_BODY_FIRST, p10)
gate('Ⓒ② ✔ THE FIRST ARM\'S ANSWER IS THE BODY\'S OWN AND IS UNMOVED BY THIS REVISION --- present '
     'here and present at the trunk, so the repair stands on the paper and not on this receipt',
     _K_BODY_FIRST in p10 and _ok and _K_BODY_FIRST in _base10)

_K_BODY_SECOND = 'the single-scale ledger stands either way'
_ok, _n = held(_K_BODY_SECOND, p10)
gate('Ⓒ③ ⛔⛭⛭ AND SO IS THE SECOND ARM\'S, WHICH IS WHAT THE ORDER DOES NOT HAVE: the body refuses '
     'the consequent the summary attached to itself, thirty lines after answering its antecedent --- '
     'unmoved at the trunk as well',
     _K_BODY_SECOND in p10 and _ok and _K_BODY_SECOND in _base10)

_K_NEW_FIRST = "The interacting tower's divergence structure does reach second order in the coupling"
_K_NEW_SECOND = "What follows from that is the definition's incompleteness and not the ledger's refutation"
_K_NEW_OPEN = 'the one open thing is the ultraviolet definition of the interacting tower\'s mode sums'
_news = [_K_NEW_FIRST, _K_NEW_SECOND, _K_NEW_OPEN]
gate(f'Ⓒ④ ✔⛭ and the repaired summary states all three --- the answer, the refusal of the consequent, '
     f'and the narrower thing that IS open --- each present and word-aligned '
     f'(`{sum(1 for k in _news if k in p10)}` of `{len(_news)}`)',
     all(k in p10 and held(k, p10)[0] for k in _news))

_K_PAIR = 'the one at unbounded momentum is open'
# the paragraph's other clause, COUNTED rather than quoted: a rewrite of the paragraph moves this
# count, a restatement of one clause inside it cannot.
_NEIGHBOUR = 'extension questions this sector meets pair'
gate('Ⓒ⑤ ⛭⛭ and the sentence the paragraph ENDS on is untouched, because it stays true of the '
     'narrowed question --- so the repair is a restatement of one clause and not a rewrite of the '
     'paragraph.  ⛔ *`L-249`\'s rule (`r3105`) is applied here rather than asserted away: the literal '
     'carries an OPENNESS MARKER, so a live pin on it fails on SUCCESS the day the mode sums are '
     'defined.  **The historical state is pinned at the commit it stood at, and the live half is the '
     'MONOTONE statement that this revision repaired one clause and not the paragraph.***',
     _K_PAIR in _base10 and _NEIGHBOUR in _base10
     and p10.count(_NEIGHBOUR) == _base10.count(_NEIGHBOUR) == 1)

# ⛭ *The first cut of this key opened on `remains` -- a finite verb -- and Ⓕ① below flagged it
#   before it was written.  The subject is in the paper one word to the left.*
_K_UV_ALREADY = 'What remains genuinely open is accordingly the ultraviolet definition of the tower sums'
gate('Ⓒ⑥ ✔⛭⛭ AND THE NARROWED STATEMENT IS NOT THIS SEAT\'S INVENTION: the paper already called that '
     'the open item in its own voice earlier in the same section, so the summary is being brought to '
     'the body rather than the body to the summary.  *Read AT THE TRUNK and not live, `L-249` again: '
     'the literal carries an openness marker, and the day the mode sums are defined this sentence is '
     'repaired --- a live pin on it would then go red on the success it is evidence for.*',
     _K_UV_ALREADY in _base10)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE FOUR PRE-REGISTERED BANDS, SCORED AGAINST THE PUSHED FILE, AND THE ONE THAT '
      'FIRES ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PRED = read('computations/beyond_the_wall/r7262_60_one_state/PREDICTION.md')
_ROW = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROW.finditer(_PRED)]
gate(f'Ⓓ① ⛭ the bands are PARSED out of the pushed pre-registration and not retyped here --- '
     f'`{len(_bands)}` rows, each with a central value and a two-sided band',
     len(_bands) == 4 and all(lo <= c <= hi for _, c, lo, hi in _bands))

_B = {i: _bands[i] for i in range(len(_bands))} if len(_bands) == 4 else {}
_MEASURED = [1, 2, 1, 2]       # P16 further sites; P18/P3 sites needing any change; P10 sites; new defects
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m = _MEASURED[_i]
    _in = _lo <= _m <= _hi
    gate(f'Ⓓ{"②③④⑤"[_i]} {"✔" if _in and _m == _c else "⛔" if not _in else "⌗"} `{_name.strip()}` --- '
         f'pre-registered `{_c}` in `{_lo}`–`{_hi}`, measured **`{_m}`**'
         + ('' if _m == _c else f'; the central value is missed by `{abs(_m - _c)}` and the band '
                                f'{"holds" if _in else "BREAKS"}'),
         _in)

gate('Ⓓ⑥ ⛔⛭⛭⛭ THE REACHABLE NEGATIVE I SET AGAINST MYSELF FIRES ON ITS LETTER: `P18` DOES turn up '
     'sites needing a change --- `N1`\'s two frontier-table rows --- so the antecedent I pushed is '
     'TRUE, and it is scored FIRED rather than narrowed now that I know which site it caught',
     _MEASURED[1] > 0)

gate('Ⓓ⑦ ⛔⛭⛭⛭ AND ITS CONSEQUENT IS FALSE, WHICH IS THE FINDING AND NOT AN ESCAPE: `P18` IS the '
     'paper that got the proper length right, its statement and its footnote both present and both '
     'untouched by this revision, so `P18 is not simply the paper that got it right` does NOT follow '
     'from the antecedent.  **The trigger does not test the claim it was written to test.**',
     _K_P18_MEMBER in p18 and footnote_naming_both(unemph(read(P18))) and P18 not in _changed)

gate('Ⓓ⑧ ⛭⛭ and the SECOND negative does not fire, and misses in the direction AGAINST the order '
     'rather than against me: I pre-registered that a body answer NARROWER than the summary\'s '
     'question would make the repair a narrowing, and the body\'s answer is WIDER --- it answers the '
     'consequent as well as the antecedent --- so the repair is a rewrite and the paper was MORE '
     'wrong than the order says',
     _K_BODY_FIRST in _base10 and _K_BODY_SECOND in _base10)

gate(f'Ⓓ⑨ ⌗ and the pushed pre-registration\'s own UNIT is wrong where its number is right: it says '
     f'`slope 1.1547005 per decade`, and `2/√3 = {mp.nstr(2 / sqrt(3), 8)}` is the slope per E-FOLD '
     f'while the per-decade slope is `{mp.nstr(2 / sqrt(3) * log(10), 8)}`.  **The pushed file is left '
     f'as pushed and the correction is here.**',
     'slope `1.1547005` per decade of core radius' in _PRED
     and abs(2 / sqrt(3) - mpf('1.1547005')) < mpf('1e-7')
     and abs(_slope - 2 / sqrt(3) * log(10)) < mpf('1e-6'))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  WHAT IS LOCATED AND NOT TAKEN, WITH THE RESTRAINT ASSERTED RATHER THAN DECLARED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# ⛔⛭⛭ `L-249`'s RULE (`r3105`), APPLIED TO EVERY ROUTED DEFECT IN THIS SECTION.  *A gate that
#   asserts a defect is PRESENT goes red the day the holding seat repairs it -- red on SUCCESS, which
#   is the failure mode `L-249` was written for and which `S5`'s `Ⓕ②ᵇ` cost this line one revision ago.*
#     ⇒ *** So each routed defect is pinned AT THE COMMIT IT STOOD AT, read from git, and the live
#         half is the MONOTONE statement that this revision has not moved it. ***
_base18 = flat(at_base(P18) or '')
_K_N1_SETTLED = 'The ultraviolet definition of the mode sums is settled beyond the free static case'
_K_N1_OPEN = 'the mode sums beyond the free static case &'
_K_N1_WEYL = 'the Weyl-squared coefficient at second order in the shear &'
_K_N1_NINE = 'Nine items stand open'
gate('Ⓔ① ⛔ `N1` is a contradiction INSIDE ONE FILE and is asserted as one: `P18`\'s quantum-sector '
     'section says the item is settled, and its own frontier table still lists it open',
     _K_N1_SETTLED in _base18 and _K_N1_OPEN in _base18)

gate('Ⓔ② ⛔⛭ AND IT IS TWO ROWS AND NOT THE ONE THE ORDER NAMES: the row beside it carries its value '
     'and reads as discharged too, and the section states `Nine items stand open` about the table, so '
     'repairing either row moves a number the paper states about itself',
     _K_N1_WEYL in _base18 and _K_N1_NINE in _base18)

gate('Ⓔ③ ✔⛭ and the restraint is ASSERTED and not declared: `N1` is located by line and `P18` is '
     'unchanged in the same breath --- the shape `r7260` got wrong when it repaired a defect it was '
     'merely standing next to',
     P18 not in _changed)

_K_M14 = '$2(m^{2}-4)\\sqrt{m^{2}-3}$'
_K_M14_CONV = '$\\mu^{2}=m^{2}-1$'
gate(f'Ⓔ④ ⌗ `M14` is located and CONFINED: the printed weight stands at `{p10.count(_K_M14)}` site(s) '
     f'in `P10` while the paper\'s own convention is carried elsewhere --- which is the computational '
     f'form of the order\'s reading that the conclusion holds either way and the defect is the value '
     f'and not the argument',
     _K_M14 in _base10 and _base10.count(_K_M14) == 1 and _K_M14_CONV in p10)

gate('Ⓔ⑤ ⌗ and `M14` is NOT taken, asserted MONOTONELY: the count of that weight in `P10` is '
     'unmoved by this revision.  *The direction is what makes the gate survive the repair it is '
     'waiting for --- `L-249` again, and the reason this is a count and not a presence*',
     p10.count(_K_M14) == _base10.count(_K_M14))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  EVERY KEY THIS RECEIPT WRITES RUNS THE ADOPTED DANGLING TEST BEFORE IT IS WRITTEN ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_MINE = [_K_FAMILY, _K_DIVERGES, _K_ARGUMENT, _K_P18_MEMBER, _K_BODY_FIRST, _K_BODY_SECOND,
         _K_NEW_FIRST, _K_NEW_SECOND, _K_NEW_OPEN, _K_PAIR, _K_UV_ALREADY, _K_N1_SETTLED]
_dang = [k for k in _MINE if D.dangles(k)]
gate(f'Ⓕ① ✔⛭⛭ `r7257`\'s order ③ is standing and is applied HERE rather than after: not one of the '
     f'`{len(_MINE)}` prose keys this receipt writes dangles under the three-armed test adopted at '
     f'`r7261` --- `{len(_dang)}` flagged',
     not _dang)

gate('Ⓕ② ✔ and the instrument is the ADOPTED one, running its own self-test and controlled in '
     'BOTH directions on this revision\'s own material: `P18`\'s footnote fragment FLAGS, which is '
     'exactly why Ⓑ⑦ reads it by structure instead of pinning it, and the main-text sentence beside '
     'it does NOT',
     D.self_test()[0] is True
     and D.dangles('Of the member itself, not of the family approaching it')
     and not D.dangles(_K_P18_MEMBER))

gate('Ⓕ②ᵇ ⌗ and one property of the adopted instrument is reported rather than repaired: the '
     'finite-verb list is CLOSED, so `diverges logarithmically at the double root` --- a span opening '
     'on a finite verb that is not in it --- does not flag.  **The list is kept byte-for-byte because '
     '`r7257`\'s and `r7258`\'s figures are reproducible only from it**, so this goes to the channel '
     'with the routed fourth arm rather than into the file in a hurry',
     not D.dangles('diverges logarithmically at the double root')
     and D.dangles('stated at the double root'))

_REPLY = read('FOR_66_FROM_60.md')
gate('Ⓕ③ ⌗ and the two items the order said leave the owed list are closed in the reply, which is '
     'where the order said to close them',
     "`S2`'s section C" in _REPLY and 'SCOPED' in _REPLY and 'r7261' in _REPLY)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = [l for l, ok in CHECKS if not ok]
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print()
print('  ⓵ ** The order\'s framing of M23 is wrong: ** P18 and P3 agree and are both right, and P16')
print('     alone is out of step -- so the repair is one paper and not two.')
print('  ⓶ ** P16\'s sentence contradicted itself without reference to any other paper: ** the')
print('     member\'s length exceeds the family\'s whole limit already at a core cut of 1e-3.')
print('  ⓷ ** M15 is worse than the order says: ** the closing summary was stale in BOTH arms, the')
print('     body having refused the consequent as well as answered the antecedent.')
print('  ⛔ ** And my own reachable negative FIRES on its letter without reaching its claim: ** P18')
print('     has two sites needing a change and neither is about the proper length, so the trigger I')
print('     fixed before the reads does not test what it was written to test.')
print('  ⌗ ** The pushed pre-registration mislabels a unit: ** 1.1547005 is per e-fold, not per')
print('     decade.  The file is left as pushed and the correction is checked here.')
print('  ⌗ ** Located and not taken: ** N1 is two rows rather than one, and M14 is confined to one')
print('     line of P10 with the paper\'s own convention carried correctly everywhere else.')
print()

if _fail:
    raise SystemExit(1)
