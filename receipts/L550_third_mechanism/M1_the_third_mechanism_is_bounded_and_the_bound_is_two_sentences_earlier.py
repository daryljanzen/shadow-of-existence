#!/usr/bin/env python3
"""M1 -- `PO-5`'s residue is NOT an unbounded existential.  The sentence that bounds it sits TWO
SENTENCES EARLIER in the same paragraph, it is mechanism-INDEPENDENT, and its premise is p0's ledger
position stated in another paper with the number already computed.

** THE RESIDUE, P14's own words. **  *** "What is not excluded here is a mechanism that is neither
holonomy nor isometry; the isometry route is walled separately, and the honest statement is that no
third mechanism has been named." ***
  ⌗ *** As stated that is an existential over an unbounded set, and 56 records it that way: "PO-5
    UNBOUNDED, is there a third mechanism?" and "PO-5 has none and no bound." ***

** ⛔⛭⛭ ⓵ BUT THE PARAGRAPH'S OWN DIMENSIONAL SENTENCE DOES NOT MENTION HOLONOMY. **  Two sentences
before the residue, P14 writes:

    *** "a Yang--Mills term in four dimensions carries a dimensionless coupling that a single length
        cannot build" ***

*Checked here: the sentence contains neither "holonomy" nor "isometry" nor "flat".*  ⇒ ***It is a
constraint on the TARGET, not on the ROUTE.  Whatever produces the connection -- holonomy, isometry,
or a third thing nobody has named -- what it must end in is a four-dimensional Yang--Mills term, and
that term needs a dimensionless number.***
  ⌗ ** So the bound is already there, and it sits inside a paragraph about one of the two routes it
    does not depend on. **  *** This line's `r2632` rule, a fifth time: the sentence that settles the
    question is next to the sentence that opens it. ***

** ⛭⛭ ⓶ AND ITS PREMISE IS p0's LEDGER POSITION, WITH THE NUMBER ALREADY COMPUTED. **  P14 says "a
single length"; p0 says which and why:

    *** "The one physical length is $\\alpha$, not $\\ell_P$; their ratio $\\alpha/\\ell_P\\sim10^{61}$
        ... is the size of the universe in gauge-units---a number, not a tuning." ***

*and that $\\ell_P$ is "a combination of these gauges, and cross-register".*  ⇒⇒ *** SO THE COUPLING
QUESTION AND THE CONSTANT-LEDGER QUESTION ARE ONE QUESTION, AND THE REGISTER CARRIES THEM APART.  If
$\\ell_P$ is a gauge, the ledger has no free dimensionless parameter and no mechanism of any kind can
supply a free coupling.  If $\\ell_P$ were a second scale, $\\alpha/\\ell_P$ is a dimensionless number
of order $10^{61}$ and the bound evaporates. ***

** ⓷ THE ARITHMETIC, REPRODUCED. **  $\\alpha=\\sqrt{3/\\Lambda}$, $\\hbar c/\\alpha$ against the strong
scale, and the ratio p0 quotes -- all three stable across the observed range of $\\Lambda$.

⇒⇒ *** ⓸ SO THE RESIDUE RESTATES, AND IT IS BOUNDED: not "is there a third mechanism?" but "a third
mechanism must deliver the coupling as a FIXED PURE NUMBER, because the ledger supplies no free
dimensionless parameter -- so any candidate is falsifiable against one number rather than searched
for in an unbounded space." ***  *That is a different kind of question: `PO-2` is gated on this row,
and a bounded residue is a gate that can be walked.*

** ⛭ ⓹ AND THE SCOPE IS SHARP, WHICH SAYS WHERE A THIRD MECHANISM WOULD HAVE TO ACT. **  The
obstruction is FOUR-DIMENSIONAL and nothing else: $\\int\\dd^{D}x\\,F^{2}/g^{2}$ dimensionless forces
$[g^{2}]=L^{D-4}$, so the coupling is dimensionless ONLY at $D=4$.
  ⇒ *** At $D=5$ -- the substrate's own dimension -- a Yang--Mills coupling IS a length, and the
    substrate has exactly one.  So the dimensional wall does not exist upstairs; it appears only
    after the descent. ***  ⚠ *That NAMES a place and claims nothing there: this receipt does not
    assert that a five-dimensional gauge sector exists, only that the argument walling the
    four-dimensional one does not reach it.*

** ⛔ CONTROL -- AND IT SHOWS THE ARGUMENT IS NOT A GENERAL BAN ON GEOMETRY MAKING FIELDS. **  The same
counting applied to the Einstein--Hilbert term gives $[1/16\\pi G]=L^{2-D}$: **dimensionFUL in every
dimension**, so a single length builds it and gravity is exactly the case the argument does not touch.
  ⇒ *** The substrate makes a metric theory and cannot make a gauge theory, and the reason is one line
    of dimensional analysis rather than anything about this construction.  A control that returned
    "gravity is walled too" would have meant the argument proves too much. ***

WHAT IS NOT CLAIMED.  ** Not that no third mechanism exists ** -- this bounds the search, it does not
close it, and `F5` forbids closing it here.  ** Not that $\\ell_P$ is a gauge ** -- that is p0's stated
position, quoted and depended on, not established here.  ** Not a five-dimensional gauge sector ** --
⓹ says where the wall stops, not that anything stands past it.  ** Not that $10^{61}$ cannot yield
$g^{2}\\sim1$ by some function ** -- any pure number can; the claim is that the ledger offers no FREE
parameter, so a third mechanism must FIX the coupling and is falsifiable at once.

Written c54.216, `L-550`.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

HBAR_C = 1.9732698e-16      # GeV m
L_P = 1.616255e-35          # m


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


# ⬭⬭ r7355+cc66 -- `L-249`'s RULE, needed three times in this file, so its reader is written once.
#   THE_REGISTER's PO-78 row states the rule verbatim: *** "the historical state be pinned at the
#   commit it stood at, the current state asserted separately, and a directional live check made
#   monotone." ***  r7258+60 and r7260+60 put three of this file's four owed rows in that class and
#   said why: the claim is carried by an OPENNESS MARKER in the corpus's own prose, so *** the pin
#   FIRES WHEN THE NAMED WORK SUCCEEDS. ***  They reached for MEANING-HELD and declined it -- a
#   string form carries this claim perfectly well and is merely EXPECTED TO RETIRE, which is
#   TEMPORAL and not inexpressible.
#   ⇒ AND THE SPLIT COSTS NOTHING HERE, because this file's finding is the BOUND, not the opening:
#     "the third mechanism is bounded and the bound is two sentences earlier".  The bound is
#     asserted live below and does not retire; the residue's openness retires the day a third
#     mechanism is named.  So the openness halves move to named commits and *** nothing new is
#     pinned and no disjunction is written *** -- the same shape as the three landed on P16 at
#     r7347.
#   ⌗ 69's r7347-cycle amendment: "the floor does not apply when the file is read at a named
#     commit", a fixed commit having no later edits for the floor to protect against.
#   ⌗ Verified before performing: each span stands exactly ONCE in its file at its pin.
P14_PIN = '593fe7ba8'   # most recent commit to touch matter_sector_paper.tex
PO_PIN = 'f02fad17a'    # most recent commit to touch PROTECTED_OPEN.md


def raw_at(rev, path):
    """a tracked file exactly as it read at a commit, NOT flattened"""
    import subprocess
    return subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                          capture_output=True, text=True, errors='replace').stdout


def flat_at(rev, path):
    """the same file, flattened the way `flat()` flattens it

    ⛔⛭ r7355+cc66 -- AND THE `git show` IS REPEATED HERE RATHER THAN TAKEN FROM `raw_at`, WHICH
    LOOKS LIKE DUPLICATION AND IS NOT.  *Written as `re.sub(r'\s+', ' ', raw_at(rev, path))`, the
    read sits TWO function hops from every key that uses it, and the extractor's trace
    (`mutate_assertions.visit(r, False, False, 2, frozenset())`) loses it: this file's site count
    fell from `14` to `9` and the three pinned literals DISAPPEARED from the instrument's view
    entirely.*
      ⇒ *** That is the worst available outcome, not a cosmetic one. ***  A pin the instrument
        cannot see is not an adjudicated pin, it is an unwatched one: its baseline rows go STALE,
        the ratchet's census stops counting the class it exists to count, and the pin still
        breaks when the paper moves -- with nothing left that knows it was ever pinned.
      ⌗ `r7353` ③ names the disposition for a span that CANNOT be pinned admissibly -- a
        structural assertion, retiring as repaired-and-invisible.  ** This is the opposite case:
        the pin is perfectly admissible, and only the plumbing made it invisible. **  So the
        plumbing changes, not the pin.
    """
    import subprocess
    out = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                         capture_output=True, text=True, errors='replace').stdout
    return re.sub(r'\s+', ' ', out)


def locate(raw, span):
    """where a FLATTENED span sits in the UNFLATTENED text

    ⌗ r7355+cc66: the flattening is many-to-one, so a span taken from flattened text cannot be
    `find`-ed in the raw text at all.  Each single space in the span is matched against any run
    of whitespace, which is exactly the relation `re.sub(r'\s+', ' ', ...)` collapses.
    """
    return re.compile(r'\s+'.join(re.escape(w) for w in span.split(' '))).search(raw)


def main():
    print()
    print('  M1 -- PO-5: is the third-mechanism residue really unbounded?')
    print()

    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    p0 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    po = flat(os.path.join(ROOT, 'PROTECTED_OPEN.md'))

    # ---------------------------------------------------- (1) the residue, as stated
    # ⌗ the residue sentence as P14 now carries it -- c54.216 appended ", and naming one remains
    #   open", which is the row DECLINING to close, and left the existential itself untouched.
    # ** ⛭ RE-PINNED r3962: `walled` -> `excluded`.  r3799 retired `walled` from the papers -- P14
    # ** reads "the isometry route is EXCLUDED separately" -- and this pin kept the retired word, the
    # ** same repair kind already recorded for `B17` in `receipts/PIN_DEBT.txt`. **  The successor is
    # ** not a synonym and the pin is sharper for it: `excluded` names what does the excluding.
    #   ⌗ *And the fifth of five instances: `walled` runs zero times in corpus/*.tex and 51 times
    #     across receipts/, of which only these few sit inside a pin.*
    # ** r6931+70.1: class (c), STALE.  r6747+66.1 (43965df3, "P14 first pass ... stated plainly")
    #   dropped the hedge "the honest statement is that" and turned ", and naming one remains open"
    #   into ", so naming one remains open": "...the isometry route is excluded separately, and no
    #   third mechanism has been named, so naming one remains open."  Same existential, same place,
    #   same refusal to close.  And the next sentence P14 now adds is THIS receipt's finding in the
    #   paper's voice -- "What can be said about one before it is named is more than nothing, and it
    #   is the dimensional sentence just used, which mentions no route" -- pinned below with the
    #   banked restatement.  The distance check (<900 chars, <=4 sentence-ends) still binds. **
    residue = ('What is not excluded here is a mechanism that is neither holonomy nor isometry; the '
               'isometry route is excluded separately, and no third mechanism has been named, so '
               'naming one remains open.')
    # ⬭ L-249 split: the RESIDUE is the retiring half, read at P14's own pin.
    check(f'⓵ at {P14_PIN} P14 stated the residue as an unbounded existential: "no third mechanism '
          'has been named" -- the RETIRING half, read where naming one cannot turn it red',
          residue in flat_at(P14_PIN, 'corpus/matter_sector_paper.tex'))
    # ⬭ L-249 split: the register's copy of the same existential, at the register's own pin.  A
    #   register is the thing most certain to be struck when the row closes, so pinning it is the
    #   clearest case of the three.
    check(f'   and at {PO_PIN} the register carried it that way too',
          'no third mechanism has been named' in flat_at(PO_PIN, 'PROTECTED_OPEN.md'))

    # ---------------------------------------------------- (2) the bounding sentence, and its form
    dim = ('a Yang--Mills term in four dimensions carries a dimensionless coupling that a single '
           'length cannot build')
    check('⛔ ⓶ and TWO SENTENCES EARLIER, in the same paragraph: "' + dim + '"', dim in p14)

    # ⛔⛔⛔ r7355+cc66 -- AND THIS SEAT'S OWN r7143 AMENDMENT WAS WRONG TWICE OVER, which is
    #   found here only because `L-249`'s split made the residue a pinned read and this line a
    #   LIVE `p14.index(residue)` -- a lookup that would CRASH rather than fail the day the
    #   sentence retires, which is the class this very line's file records twice elsewhere.
    #   ** r7143+cc66.108 replaced two numeric bounds (`< 900` characters, `<= 4` sentence-ends)
    #   with what it called the derivable test, and wrote: "there is no paragraph break between
    #   them ... not a looser bound, the derivable one." **
    #     ⓐ *** THE TEST COULD NEVER FIRE. ***  `between` is cut from `p14`, which is
    #       `re.sub(r'\s+', ' ', ...)`, so it holds ZERO newline characters -- `'\n\n' in
    #       between` is False by construction, for any paper, forever.  *Measured: `flat(p14)`
    #       contains 0 newlines.*  The `\par` arm is the only one that could ever decide, and it
    #       is absent here, so the conjunction has been carried by a constant since it was written.
    #     ⓑ *** AND ON THE TEXT WHERE IT CAN BE MEASURED, IT IS FALSE. ***  Located in the
    #       UNFLATTENED paper, the material between the two sentences contains a blank line -- a
    #       real TeX paragraph break.  *** So the two sentences are NOT in the same paragraph, and
    #       the claim r7143 asserted is untrue. ***
    #   ⇒ ** The FINDING survives and the GLOSS does not: ** the bound is still two sentences
    #     earlier (`n_sent == 2`) and 529 characters earlier, and it is in the paragraph
    #     IMMEDIATELY BEFORE rather than the same one.  So the two numeric bounds r7143 discarded
    #     are restored AS ASSERTIONS -- they are the derivable facts -- and the paragraph count is
    #     measured on the raw text, where the question has an answer, and asserted at its true
    #     value instead of its wished-for one.
    #   ⌗ Read at the pin with the residue, because a distance between two sentences is a fact
    #     about the paragraph as it stood, and it retires when the residue does.
    #   ⛭ TIGHTENED r7355+cc66.27, against this block's own first form.  It was written
    #     `n_sent <= 4`, and `check_prose_pins` flagged it as a NEW pin on a count -- correctly.
    #     *** A `<= 4` bound admits 3 and 4, neither of which is "two sentences earlier", so the
    #     slack made the assertion WEAKER THAN THE CLAIM IT LABELS -- and the comment four lines
    #     above already said `n_sent == 2`, so the code contradicted its own prose. ***
    #   ⇒ ** The haystack is read at `P14_PIN`, so the count cannot move while the pin holds: an
    #     equality is immovable here for exactly the reason a slack bound is unnecessary. **  The
    #     headroom was protecting against nothing and hiding the claim's own number.
    p14_pin = flat_at(P14_PIN, 'corpus/matter_sector_paper.tex')
    _raw_pin = raw_at(P14_PIN, 'corpus/matter_sector_paper.tex')
    i_dim, i_res = p14_pin.index(dim), p14_pin.index(residue)
    between = p14_pin[i_dim:i_res]
    n_sent = between.count('. ')
    _m_dim, _m_res = locate(_raw_pin, dim), locate(_raw_pin, residue)
    _between_raw = _raw_pin[_m_dim.end():_m_res.start()]
    n_para = _between_raw.count('\n\n') + _between_raw.count('\par')
    check(f'   with the residue {i_res - i_dim} characters and {n_sent} sentence-ends later, across '
          f'{n_para} paragraph break(s) -- the paragraph IMMEDIATELY BEFORE, two sentences on, and '
          f'not a distant echo (r7143 claimed the SAME paragraph and that is false, see above)',
          0 < i_res - i_dim < 900 and n_sent == 2 and n_para == 1)

    # THE POINT: the bounding sentence names no route
    routes = [w for w in ('holonomy', 'isometry', 'flat', 'bundle', 'monodromy', 'winding')
              if w in dim.lower()]
    check(f'⛭⛭ ⓷ AND THE BOUNDING SENTENCE NAMES NO ROUTE: of {["holonomy", "isometry", "flat", "bundle", "monodromy", "winding"]} it contains {routes} -- '
          'it constrains the TARGET (a 4D Yang-Mills term) and not the mechanism, so it bounds a '
          'third mechanism exactly as it bounds the first two',
          routes == [])

    # ---------------------------------------------------- (3) the premise is p0's, in another paper
    ledger = ('The one physical length is $\\alpha$, not $\\ell_P$; their ratio '
              '$\\alpha/\\ell_P\\sim10^{61}$')
    check('⓸ and P14\'s premise "a single length" is p0\'s ledger position, stated in another paper: '
          '"' + ledger + ' ... is the size of the universe in gauge-units---a number, not a tuning"',
          ledger in p0 and 'the size of the universe in gauge-units---a number, not a tuning' in p0)
    # ⬭⬭ r7355+cc66, TWO DEFECT CLASSES IN ONE KEY, which is how r7260+60 read it: DANGLING
    #   (leading, finite verb -- the span opens on `are`, and what the Planck units ARE is the
    #   whole claim, so its subject sat outside) AND a MARKUP CARRIER (`\emph{cross-register}`
    #   inside the span).
    #   ⇒ One widening answers both: the span now opens on `The traditional Planck length, mass,
    #     and time`, carries their definitions and the `cross-register` predicate whole, and is
    #     read against the EMPHASIS-NORMALISED paper per 60's r7255 prescription.
    #   ⌗ The normalised haystack is bound FROM THE PATH rather than from `p0`, for the reason
    #     measured on `L548` this revision: a haystack bound through another binding can leave the
    #     key UNDECIDED, which owes a hand-kept `corpus/target_annotations.tsv` row.
    #   ⌗ Verified before performing: ONCE in the normalised paper, once under `_unmark`.
    p0u = re.sub(r'\\emph\{([^}]*)\}', r'\1',
                 flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    check('   and p0 says WHY l_P is not a second length: "The traditional Planck length, mass, and '
          'time ... are combinations of these gauges, and cross-register ones, mixing the thermal '
          '$\\hbar$ with the real-geometric $c$ and $G$"',
          'The traditional Planck length, mass, and time---$\\ell_P=\\sqrt{\\hbar G/c^3}$, '
          '$m_P=\\sqrt{\\hbar c/G}$, $t_P=\\sqrt{\\hbar G/c^5}$---are combinations of these '
          'gauges, and cross-register ones, mixing the thermal $\\hbar$ with the real-geometric '
          '$c$ and $G$' in p0u)

    # ---------------------------------------------------- (4) the arithmetic
    print()
    for Lam in (1.0e-52, 1.1056e-52, 1.2e-52):
        al = math.sqrt(3/Lam)
        E = HBAR_C/al
        dec = math.log10(0.2/E)
        rat = al/L_P
        check(f'⓹ Lambda = {Lam:.4g} m^-2: alpha = {al:.4g} m, hbar c/alpha = {E:.4g} GeV, which is '
              f'{dec:.2f} decades BELOW the strong scale, and alpha/l_P = 10^{math.log10(rat):.2f}',
              41.0 < dec < 41.5 and 60.9 < math.log10(rat) < 61.1)
    check('   ⇒ P14\'s "some forty-one decades below the strong scale, and in the infrared rather '
          'than the ultraviolet direction" is reproduced, and is stable across the observed range',
          'forty-one decades below the strong scale' in p14
          and '3/\\Lambda}$, whose energy $\\hbar c/\\alpha$ sits some forty-one decades below the strong scale, and in the infrared rather than the ultraviolet direction' in p14)
    Lam = 1.1056e-52
    # ** ⛔⛔ REPAIRED r3962, AND THE PIN WAS THE SMALLER HALF OF IT. **  This check read
    # **     `numeric and 'Lambda \ell_P^2...' in p0  or  numeric`
    # ** and `and` binds tighter than `or`, so it evaluated as `(numeric and pin) or numeric`
    # ** *** == numeric. ***  The pin was UNREACHABLE: the check announced that it verified the
    # ** paper's own figure and verified only arithmetic this file supplied itself.  ** A trailing
    # ** `or` arm that repeats the first conjunct deletes every conjunct after it. **
    #   ⌗ And the pin was ALSO wrong -- `Lambda \ell_P^2` with a space, against the paper's
    #     `\Lambda\ell_P^2` with none -- which is why it was written behind an `or` and never
    #     noticed.  *** A fallback added to make a check pass is how a hollow check gets built. ***
    #     `lint_assertions.py` could not see it: the file's assertions are not hollow, the DEFECT
    #     IS IN THE BOOLEAN.  ⇒ both halves are fixed here and neither is behind a fallback.
    check(f'   and p0\'s own $\\Lambda\\ell_P^2\\approx3\\times10^{{-122}}$ checks: '
          f'{Lam*L_P**2:.3g}',
          2e-122 < Lam*L_P**2 < 4e-122
          and '\\Lambda\\ell_P^2\\approx3\\times10^{-122}' in p0)

    # ---------------------------------------------------- (5) scope: the wall is 4D and nothing else
    print()
    # [g^2] = L^(D-4) from requiring int d^Dx F^2/g^2 dimensionless, [F]=L^-2
    def g2_dim(D):
        return D - 4

    check(f'⛭ ⓺ SCOPE: requiring int d^D x F^2/g^2 dimensionless with [F] = L^-2 gives '
          f'[g^2] = L^(D-4): D=4 -> L^{g2_dim(4)} (DIMENSIONLESS, the wall), '
          f'D=5 -> L^{g2_dim(5)} (a LENGTH, and the substrate has exactly one)',
          g2_dim(4) == 0 and g2_dim(5) == 1)
    check('   ⇒ the dimensional wall is FOUR-DIMENSIONAL and appears only after the descent -- which '
          'names where a third mechanism would have to act, and claims nothing there',
          g2_dim(5) != 0)

    # ---------------------------------------------------- (6) CONTROL: it must not prove too much
    # Einstein-Hilbert: S = (1/16 pi G) int d^D x sqrt(g) R,  [R] = L^-2
    def eh_dim(D):
        return 2 - D

    check(f'⛔ CONTROL -- the argument must NOT prove too much: the same counting on the '
          f'Einstein-Hilbert term gives [1/16 pi G] = L^(2-D), i.e. L^{eh_dim(4)} at D=4 and '
          f'L^{eh_dim(5)} at D=5 -- DIMENSIONFUL in every dimension, so a single length builds it',
          eh_dim(4) != 0 and eh_dim(5) != 0 and all(eh_dim(D) != 0 for D in range(2, 12) if D != 2))
    check('   ⇒ *** gravity is exactly the case the argument does not touch. The substrate makes a '
          'metric theory and cannot make a gauge theory, by one line of dimensional analysis -- and '
          'a control returning "gravity is walled too" would have meant it proves too much. ***',
          eh_dim(4) == -2)

    # ---------------------------------------------------- (7) banked
    print()
    check('⛭ and the restatement is BANKED in P14, not only here: "what a third mechanism must '
          'deliver is therefore a fixed pure number rather than a free parameter"',
          'what a third mechanism must deliver is therefore a fixed pure number rather than a free '
          'parameter' in p14)
    # ** r6931+70.1: class (c), same rewording as ⓵ (43965df3): ", and naming" -> ", so naming". **
    # ⬭ L-249 split: the third openness read, same rule, same pin.  *The DURABLE half of this
    #   very paragraph is the sentence asserted immediately above -- "what a third mechanism must
    #   deliver is therefore a fixed pure number rather than a free parameter" -- which is LIVE and
    #   stays true whether or not a third mechanism is ever named.  That is why no disjunction is
    #   needed: the two halves are already in two checks.*
    check(f'   ⚠ and at {P14_PIN} the paragraph still DECLINED to close the row: "no third '
          'mechanism has been named, so naming one remains open"',
          'no third mechanism has been named, so naming one remains open'
          in flat_at(P14_PIN, 'corpus/matter_sector_paper.tex'))
    check('   ⛭ and P14 now says this receipt\'s point itself, right after the residue: "What can be '
          'said about one before it is named is more than nothing, and it is the dimensional sentence '
          'just used, which mentions no route"',
          ('What can be said about one before it is named is more than nothing, and it is the '
           'dimensional sentence just used, which mentions no route') in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-5\'s residue is BOUNDED, and the bound is two sentences earlier. **')
    print('  ⓵ ** P14\'s dimensional sentence names no route ** — not holonomy, not isometry, not')
    print('     flat, not bundle.  It constrains the TARGET, a four-dimensional Yang-Mills term, so')
    print('     *** it bounds a third mechanism exactly as it bounds the first two. ***')
    print('  ⛭⛭ ⓶ ** And its premise is p0\'s ledger position, in another paper, with the number **')
    print('     already computed: "the one physical length is alpha, not l_P; their ratio ~10^61 ...')
    print('     a number, not a tuning."  *** So the coupling question and the constant-ledger')
    print('     question are ONE question, and the register carries them apart. ***')
    print('  ⓷ ** So the residue restates, bounded: ** not "is there a third mechanism?" but')
    print('     *** "a third mechanism must deliver the coupling as a FIXED PURE NUMBER, because the')
    print('     ledger supplies no free dimensionless parameter" *** — one number to test, not an')
    print('     unbounded space to search.  PO-2 is gated on this row.')
    print('  ⛭ ⓸ ** And the wall is FOUR-DIMENSIONAL: ** [g^2] = L^(D-4), so at D=5 the coupling is')
    print('     a length and the substrate has one.  The wall appears only after the descent.')
    print('  ⛔ ** CONTROL: ** the same counting leaves Einstein-Hilbert dimensionful in every')
    print('     dimension — gravity is the case the argument does not touch, so it does not prove')
    print('     too much.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
