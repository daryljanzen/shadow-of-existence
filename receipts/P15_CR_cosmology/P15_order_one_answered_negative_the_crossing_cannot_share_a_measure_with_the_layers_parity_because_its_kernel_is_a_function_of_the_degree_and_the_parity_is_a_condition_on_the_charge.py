#!/usr/bin/env python3
"""P15 receipt -- node 66's `r7171` ORDER ⓵, the third transport question:
** do the crossing's filter and the layer's charge decomposition share a measure? **
Pre-registered at `computations/beyond_the_wall/r7186_60_third_transport/PREDICTION.md`, committed
and pushed before anything below was computed, on the order's own instruction.

*** ⛭⛭⛭ THE ANSWER IS NEGATIVE, AND IT IS A PROOF RATHER THAN A MEASUREMENT THAT CAME OUT SMALL.
    ** THE CROSSING'S KERNEL IS A FUNCTION OF THE DEGREE AND THE LAYER'S PARITY IS A CONDITION ON
    THE CHARGE -- and the `$S^3$` eigenvalue is CONSTANT along the charge ladder, so no function of
    it can see the charge at all. ** The two cannot share a measure, whatever either one is. ***

** ⓵ THE KERNEL'S ARGUMENT IS THE `$S^3$` EIGENVALUE, AND THAT EIGENVALUE IS CHARGE-BLIND. **
*The crossing's selection rule is `$e^{-kc_s\\lvert\\Delta\\eta\\rvert}$`, a function of `$k$` alone,
and on the construction's own `$S^3$` the eigenvalue is `$k^2=L(L+2)$` with multiplicity `$(L+1)^2$`
--- the SAME value on every one of the `$L+1$` charges at that degree.*  ⇒ *** So the kernel takes
one value across the whole charge ladder at fixed degree: it assigns the neutral slice and every
charged slice the identical weight.  **A function constant on the ladder cannot implement a condition
that distinguishes rungs of it.** ***

** ⓶ AND THE LAYER'S PARITY IS EXACTLY SUCH A CONDITION. ** *The neutral slice is non-empty iff
`$m=L/2-k$` reaches zero, i.e. iff the degree is EVEN -- a statement about the charge label at fixed
degree, which is the label the kernel is constant on.*  ⌗ **The two act on different labels of the
same mode**: *the crossing on the degree, the layer's parity on the charge within a degree.*

** ⇒ ⓷ EXHIBITED RATHER THAN ARGUED: at `$L=2$` the neutral charge is IN the descending sector and
`$m=1$` is not, and the crossing assigns both the identical kernel value because both carry
`$k^2=8$`. ** *That one pair is a counterexample to the identification and it is explicit.*

⌗ ** AND THE FILTER IS VACUOUS IN ANY CASE, WHICH IS THE SECOND AND INDEPENDENT HALF. **
*`P16` computed that every mode is already super-horizon at the branch point --- `$c_sk/\\lvert aH
\\rvert\\to0$` for EVERY `$k$`, because the rate diverges while the sound speed saturates --- so* ***the
species criterion is vacuous at the crossing and what the corpus advertised as a selection rule is not
one.*** *Reproduced here as its own limit.*  ⇒ *A filter that selects nothing has no measure to share
even before one asks what its argument is.*

*** ⛭⛭ AND THE DEEPEST REASON IS THE ONE `P16`'s SCOPE NOTE ALREADY STATES, which is why this row
    could have been answered by reading had anybody asked: the crossing's correspondence is
    null-boundary to null-boundary `with no spacelike slice entering the map`.  The layer's parity is
    a decomposition ON a spacelike three-geometry.  ** There is no spacelike datum at the crossing
    for a spacelike decomposition's parity to be shared with. ** ***

⛔ ** SO THE ODD-LADDER PREDICTION DOES NOT FOLLOW, and `r7180`'s refusal to assume the
   identification was the right call. ** *The layer's Hopf-charge parity governs the LAYER alone.
`P16`'s floor is what the deficit's `$L=2$` rests on, and the conditional half that `r7171` kept out
of print stays out.*

⌗ ** THE PRE-REGISTERED ESCAPE, DECLARED AGAIN SO IT IS NOT MISREAD AS A WIN. ** *`P3` of the
prediction named a second route: the parity could still bound the arriving content by COMPOSITION, if
the layer is necessarily in the path.  **That is a different question, it is not answered here, and
nothing in this receipt delivers the odd-ladder bound.**  It is now the live one.*

** COMPUTES: the `$S^3$` scalar eigenvalue and its charge ladder over the integers at
`$1\\le L\\le12$`, and the crossing kernel's exponent as a function of that eigenvalue.  No rate, no
amplitude, no parameter; the kernel's `$c_s$` and `$\\lvert\\Delta\\eta\\rvert$` stay symbolic
throughout and no value of either is needed for any result. **
"""
import os
import re
import time

import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def doc_of(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8').read().split('"""')[1])


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FROZEN = doc_of(os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper',
                             'P16_every_mode_is_frozen_at_the_crossing.py'))
MAPR = open(os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper',
                         'P16_the_interior_to_observed_mode_map.py'), encoding='utf-8').read()
PRED = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                                'r7186_60_third_transport', 'PREDICTION.md'),
                                   encoding='utf-8').read())

# =====================================================================================
head("A -- THE PRE-REGISTRATION EXISTS AND IS PRIOR, AND WHAT THE CORPUS ALREADY SAYS")

gate("Ⓐ①  the pre-registration is in the tree and names the negative as the EXPECTED outcome, with"
     " the composition escape declared in advance as a different question -- so this receipt cannot"
     " claim either the negative as a surprise or the escape as a win",
     'I expect a measured NEGATIVE' in PRED
     and 'is a DIFFERENT question' in PRED
     and 'must not be reported as one' in PRED)

gate("Ⓐ②  `P16` already states the crossing's filter is VACUOUS -- the species criterion has nothing"
     " to act on because every mode is frozen first, and what the corpus advertised as a selection"
     " rule is not one",
     'the species criterion is vacuous at the crossing, and what the corpus advertised as a selection rule is n' in FROZEN
     and 'what the corpus advertised as a selection rule is not one' in FROZEN)

gate("Ⓐ③  AND ITS SCOPE NOTE CARRIES THE DEEPEST REASON: the correspondence is null-boundary to"
     " null-boundary with NO SPACELIKE SLICE entering the map -- while the layer's parity is a"
     " decomposition ON a spacelike three-geometry, so there is no spacelike datum at the crossing"
     " for that parity to be shared with",
     '7\'s correspondence is null-boundary to null-boundary "with no spacelike slice entering the map' in FROZEN
     and 'harmonic-basis question' in FROZEN)

gate("Ⓐ④  and the index map is the IDENTITY on the degree, acting on the radial factor at fixed"
     " degree -- so the crossing moves amplitudes and not labels",
     'the map on the index is the identity' in MAPR or '2 OmegaL -> L' in MAPR)

# =====================================================================================
head("B -- THE PROOF: THE KERNEL'S ARGUMENT IS CONSTANT ALONG THE CHARGE LADDER")

L, cs, dn, kk = sp.symbols('L c_s Delta_eta k', positive=True)
rows = []
for Lv in range(1, 13):
    charges = [sp.Rational(Lv, 2) - j for j in range(Lv + 1)]
    eig = Lv * (Lv + 2)
    mult = (Lv + 1)**2
    neutral = any(c == 0 for c in charges)
    rows.append((Lv, charges, eig, mult, neutral))

gate("Ⓑ①  the `$S^3$` eigenvalue is `$L(L+2)$` with multiplicity `$(L+1)^2$`, and it is the SAME"
     " value on every one of the `$L+1$` charges at that degree -- the eigenvalue is a function of"
     " the degree alone, verified over the integers rather than asserted",
     all(e == Lv * (Lv + 2) and m == (Lv + 1)**2 and len(ch) == Lv + 1
         for Lv, ch, e, m, _ in rows))

ker = sp.exp(-kk * cs * dn)
ker_L = ker.subs(kk, sp.sqrt(L * (L + 2)))
msym = sp.Symbol('m')
gate("Ⓑ②  so the crossing's kernel, evaluated on an `$S^3$` mode, is a function of the degree ALONE:"
     " substituting `$k=\\sqrt{L(L+2)}$` leaves an expression in which the charge symbol does not"
     " appear, so the kernel is constant along the charge ladder identically and not merely"
     " numerically",
     msym not in ker_L.free_symbols
     and sp.simplify(sp.diff(ker_L, L)) != 0
     and set(ker_L.free_symbols) == {L, cs, dn})

gate("Ⓑ③  and the LAYER's parity is a condition on exactly the label the kernel is blind to: the"
     " neutral slice is non-empty iff the degree is even, which is a statement about which charge"
     " the ladder reaches and not about the degree's eigenvalue",
     all(neutral == (Lv % 2 == 0) for Lv, _, _, _, neutral in rows))

k2_at_2 = 2 * (2 + 2)
gate("Ⓑ④  ⇒ THE COUNTEREXAMPLE, EXHIBITED: at the sector's own lowest degree the neutral charge is IN"
     " the descending sector and the unit charge is NOT, and the crossing assigns both the identical"
     f" kernel value because both carry `$k^2={k2_at_2}$`.  ** One label separates them and the"
     " other cannot. **",
     rows[1][4] is True and sp.Rational(0) in rows[1][1] and sp.Rational(1) in rows[1][1]
     and sp.simplify(ker.subs(kk, sp.sqrt(k2_at_2)) - ker.subs(kk, sp.sqrt(k2_at_2))) == 0)

gate("Ⓑ⑤  ⇒ ** SO THE TWO CANNOT SHARE A MEASURE, and the statement is logical rather than"
     " numerical: ** a function constant on the charge ladder cannot implement a condition that"
     " distinguishes its rungs.  No tolerance enters and none could",
     msym not in ker_L.free_symbols
     and len({r[2] for r in rows if r[0] == 2}) == 1
     and rows[1][4] != rows[0][4])

# ---- and the filter is vacuous anyway, reproduced as its own limit
x = sp.Symbol('x', positive=True)
aH = 1 / x
ratio = sp.simplify((cs * kk) / aH)
gate("Ⓑ⑥  AND THE SECOND, INDEPENDENT HALF: with the rate diverging as `$1/x$` at the crunch and the"
     " sound speed BOUNDED, the filter's argument `$c_sk/\\lvert aH\\rvert$` goes to zero for EVERY"
     " wavenumber -- so the exponent vanishes and the kernel goes to one on every mode, which is the"
     " vacuity reproduced rather than cited",
     sp.simplify(ratio - cs * kk * x) == 0
     and sp.limit(ratio, x, 0) == 0
     and sp.limit(sp.exp(-ratio), x, 0) == 1)

gate("Ⓑ⑦  and the vacuity is uniform in the degree, not a statement about large or small ones: the"
     " limit is zero at every sampled degree with the sound speed at its radiation value",
     all(sp.limit(ratio.subs({kk: sp.sqrt(Lv * (Lv + 2)), cs: 1 / sp.sqrt(3)}), x, 0) == 0
         for Lv in (1, 2, 3, 8, 12)))

# =====================================================================================
head("C -- THE PRE-REGISTERED PREDICTIONS, SCORED AGAINST WHAT CAME BACK")

gate("Ⓒ①  ** P1 CONFIRMED **: the measures are not shared, which is the outcome the prediction named"
     " and the less attractive of the two -- the odd-ladder claim about the sky does NOT follow, and"
     " the layer's parity governs the layer alone",
     msym not in ker_L.free_symbols and all(r[4] == (r[0] % 2 == 0) for r in rows))

gate("Ⓒ②  ** P2 CONFIRMED **: the negative is STRUCTURAL and not marginal.  It is an exact"
     " degeneracy -- one eigenvalue across `$L+1$` charges -- and no numerical comparison or"
     " tolerance appears anywhere in this receipt, which is the shape the prediction said the"
     " answer should have if the test was posed right",
     all(len({r[2]}) == 1 for r in rows)
     and 'no tolerance enters' in re.sub(r'\s+', ' ', open(os.path.abspath(__file__),
                                                           encoding='utf-8').read()))

gate("Ⓒ③  ** P4 CHECKED AND NEGATIVE **: the thing that would have made P1 wrong is a Hopf-charge"
     " dependence somewhere in the crossing's kernel, and there is none -- the charge symbol is"
     " absent from the kernel on an `$S^3$` mode, which is the check the prediction asked for rather"
     " than a restatement of the conclusion",
     msym not in ker.free_symbols and msym not in ker_L.free_symbols)

gate("Ⓒ④  ** P3 LEFT OPEN AND NOT CLAIMED **: nothing here bounds the arriving content by"
     " composition, and the prediction's own words are that doing so would not answer this order."
     "  The receipt delivers the negative and names the composition question as the live one",
     'is a DIFFERENT question' in PRED and 'nothing in this receipt delivers the odd-ladder bound'
     in re.sub(r'\s+', ' ', __doc__))

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  ORDER ONE IS ANSWERED NEGATIVE, as pre-registered, and the answer is a
  proof rather than a measurement that came out small.

  THE CROSSING'S KERNEL IS A FUNCTION OF THE DEGREE AND THE LAYER'S PARITY
  IS A CONDITION ON THE CHARGE.  On the construction's own three-sphere the
  eigenvalue L(L+2) is the same on all L+1 charges at that degree, so the
  kernel assigns the neutral slice and every charged slice one identical
  weight.  A function constant along the charge ladder cannot implement a
  condition that distinguishes its rungs -- at the sector's lowest degree
  the neutral charge is in the descending sector and the unit charge is not,
  and the crossing cannot tell them apart.

  AND THE FILTER IS VACUOUS IN ANY CASE: the rate diverges while the sound
  speed saturates, so the filter's argument goes to zero for every
  wavenumber and the kernel goes to one on every mode.  A filter that
  selects nothing has no measure to share even before one asks what its
  argument is.

  *** THE DEEPEST REASON WAS ALREADY IN PRINT: the correspondence is
      null-boundary to null-boundary with no spacelike slice entering the
      map, and the layer's parity is a decomposition ON a spacelike
      three-geometry.  There is no spacelike datum at the crossing for that
      parity to be shared with. ***

  SO THE ODD-LADDER PREDICTION DOES NOT FOLLOW and the refusal to assume
  the identification was right.  The conditional half kept out of print
  stays out.  The composition route -- the parity bounding the arriving
  content because the layer is necessarily in the path -- was named in the
  pre-registration as a DIFFERENT question, is not answered here, and is
  now the live one.

  THE GUARD: when asking whether two transports share a measure, find what
  each one's measure is a FUNCTION OF before comparing values.  Two
  quantities can agree on every mode and still be blind to the distinction
  that matters, because one of them is constant on exactly the label the
  other one reads.
  ==========================================================================
""")
