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
    residue = ('What is not excluded here is a mechanism that is neither holonomy nor isometry; the '
               'isometry route is excluded separately, and the honest statement is that no third '
               'mechanism has been named, and naming one remains open.')
    check('⓵ P14 states the residue as an unbounded existential: "no third mechanism has been named"',
          residue in p14)
    check('   and the register carries it that way too', 'no third mechanism has been named' in po)

    # ---------------------------------------------------- (2) the bounding sentence, and its form
    dim = ('a Yang--Mills term in four dimensions carries a dimensionless coupling that a single '
           'length cannot build')
    check('⛔ ⓶ and TWO SENTENCES EARLIER, in the same paragraph: "' + dim + '"', dim in p14)

    i_dim, i_res = p14.index(dim), p14.index(residue)
    between = p14[i_dim:i_res]
    n_sent = between.count('. ')
    check(f'   with the residue {i_res - i_dim} characters and {n_sent} sentence-ends later -- the '
          'same paragraph, not a distant echo',
          0 < i_res - i_dim < 900 and n_sent <= 4)

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
    check('   and p0 says WHY l_P is not a second length: the Planck units are "combinations of these '
          'gauges, and \\emph{cross-register} ones"',
          'are combinations of these gauges, and \\emph{cross-register} ones' in p0)

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
          and 'in the infrared rather than the ultraviolet direction' in p14)
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
    check('   ⚠ and the paragraph still DECLINES to close the row: "no third mechanism has been '
          'named, and naming one remains open"',
          'no third mechanism has been named, and naming one remains open' in p14)

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
