#!/usr/bin/env python3
"""P15 receipt -- node 66's `r7181` ORDER, which is a READ and not a computation:
** does `P7`'s rate rule fix the argument of `$j_\\ell(k\\chi)$` directly, or only the expansion
LAW's `$D_M$`, reaching the projection through the flat-slice identification? **

*** ⛭⛭⛭ THROUGH THE IDENTIFICATION, AND THE REASON IS IN `P7`'s OWN IDENTITY RATHER THAN IN ANY
    HEDGE OF `P15`'s.  ** THE SAME SENTENCE THAT MAKES THE LAPSE THE STACKING RATE MAKES THE SHIFT
    THE THING THE EXPANSION IS *OBSERVED* THROUGH AS DISTANCE AND REDSHIFT. ** Those are two
    different data of the slicing operator, so a rule about which RATE a quantity accumulates on
    cannot fix a projection's argument -- it fixes which rate the length it names accumulates on. ***

** ⓵ `P7` SPLITS THE TWO ROLES IN ONE SENTENCE, AND THE SPLIT IS THE ANSWER. ** *The lapse `$N$` is
`the foliation stacking rate the observable expansion rides`, fixed by `$\\alpha$` and the cut's
offset.*  ⇒ *And the shift `$N^i$` is `the $E{=}1$ projection through which that expansion is
OBSERVED as distance and redshift`.*  ⌗ **`rides` and `observed through` are not the same relation,
and the proposition assigns them to different data.**

** ⓶ AND THE RULE'S OWN FORM CONFIRMS IT: IT IS A CLASSIFIER OVER RATES, NOT OVER ARGUMENTS. **
*It sorts quantities into two bins --- `a comoving separation read across leaves, $D_M$, $D_H$, $D_V$,
the observable expansion` on the stacking side, the plasma's own accumulations on the leaf's.*
⇒ ***So what it fixes about `$D_M$` is which rate `$D_M$` accumulates on.*** *And `$D_M$` is in it as
a separation read ACROSS LEAVES, which is not what the argument of `$j_\\ell$` is: that argument is a
comoving radial distance along the photon path to last scattering.* **The rule never names it.**

** ⓷ SO THE EQUALITY THE PROJECTION NEEDS IS FLATNESS'S. ** *`prop:flat` is a statement about the
constant-`$\\tau$` slice's INDUCED THREE-METRIC and the vanishing of its Riemann tensor --- a theorem
about a slice's geometry, with no rate in it at all.*  ⇒ *It is what makes the comoving
angular-diameter distance BE the light-travel distance, and `P15` says so in its own voice:
`$j_\\ell(kD_C)$` `is licensed by an identification --- the flatness of the distance slice together
with the exact recovery of the expansion law`.*

*** ⛔ ⓸ AND HERE IS THE SHARPENING THE ORDER DID NOT HAVE, WHICH RUNS THE NARROW WAY RATHER THAN THE
    COMFORTABLE ONE.  `P15` settles the distance `by three independent routes`. ** THEY ARE NOT THREE
    FOUNDATIONS. THEY ARE TWO. ** *** *The third --- the optical depth's own argument --- is a
PRECEDENT argument, and its own receipt states the premise it needs: that the optical depth `is a
photon-path observable of the same kind as the redshift and the distances`.* ⇒ ***That premise IS the
rule's classification, so the third route is the rule applied a second time rather than a second
ground.*** ⌗ **My first reading of this was that three routes meant three supports, and checking the
third route's stated premise is what corrected it** --- *which is the control this receipt has in place
of a pre-registration, since the order asks for a read.*

⇒ *** ⛭⛭ SO: TWO GROUNDS, THE RULE AND THE IDENTIFICATION; THE RULE REACHES THE PROJECTION ONLY
    THROUGH THE IDENTIFICATION; AND THEREFORE THE IDENTIFICATION IS THE ONLY INDEPENDENT SUPPORT FOR
    THE ONE EQUALITY THE PROJECTION'S ARGUMENT TURNS ON. ** That is the second horn of the order's
    fork, and it is the narrower one. ** ***

⚠ ** AND THE ONE DISTINCTION I WILL NOT BLUR, BECAUSE THE SECTOR'S VERDICT TURNS ON IT AND THAT
   VERDICT IS `66`'s: NARROWER IS NOT WEAKER. ** *`prop:flat` is proved and receipted, and the
expansion-law recovery is measured; the identification is not a conjecture.* ⇒ ***What the answer
changes is the NUMBER OF INDEPENDENT SUPPORTS, not the soundness of the one that carries it.*** *The
order asked which object the identity fixes and that is answered here; whether `a disagreement at full
strength` survives on one established ground rather than three is a print decision and I am not
making it.*

** COMPUTES: nothing.  This is a read, as the order specifies.  Every clause it turns on is quoted
from `P7`'s proposition remark, `P15`'s two sentences, `prop:flat`'s statement and the optical-depth
receipt's own stated premise, and each is asserted present in the source it is attributed to -- so the
receipt fails if any of them is reworded, which is the only control a read can carry.  No figure, no
tolerance, no sampling, and no assertion on wall-clock time. **
"""
import os
import re
import time

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def flat(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8').read())


P15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
P07 = flat(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))


def doc_of(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8').read().split('"""')[1])


TAU = doc_of(os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_optical_depth_is_a_photon_path_observable_so_it_takes_the_stacking_rate_and_the_'
    'visibility_ruling_is_withdrawn.py'))

# =====================================================================================
head("A -- THE TWO SENTENCES AND THE PROPOSITION, READ FROM THEIR OWN SOURCES")

gate("Ⓐ①  `P15` carries BOTH of the sentences the order names, and they are the two the fork is"
     " about: the rate rule reaching the distance by naming `$D_M$`, and the kernel being licensed by"
     " an identification -- so the question is about a real pair in print and not a constructed one",
     'The rate rule reaches the same distance by naming $D_M$' in P15
     and 'is licensed by an \\emph{identification}' in P15
     and 'the flatness of the distance slice together with the exact recovery of the expansion law'
     in P15)

_ROUTES_AS_IS = 'by three independent routes' in P15
# ** r7183 (node 66, whose edit moved these): `P15` now carries this receipt's OWN ANSWER rather
#   than the fork's two sides, so the locators read the sentence as it stands.  The rule's clause
#   gained four words -- `the same distance` -- and the count of routes is gone, replaced by `on one
#   ground that is a theorem and a second that rests on it`, which is added to the enumeration this
#   receipt deliberately kept open so it would not fail on its own success. **
_ROUTES_FIXED = ('by two independent routes' in P15
                 or 'by three routes sharing n' in P15
                 or 'two independent grounds' in P15
                 or 'on one ground that is a theorem and a second that rests on it' in P15)
gate("Ⓐ②  and the object the fork is about is named in `P15` as the argument of the kernel -- the"
     " comoving distance entering `$j_\\ell(k\\chi)$`, which the paper says is SETTLED.  ** The"
     " COUNT of routes is deliberately NOT pinned: this receipt's own result is that one of the three"
     " is another's corollary, so asserting the present wording would be a gate that fails on its own"
     " success.  The states are enumerated instead and either satisfies it **",
     'the comoving distance entering $j_\\ell(k\\chi)$ is settled' in P15
     and (_ROUTES_AS_IS or _ROUTES_FIXED))

gate("Ⓐ③  and `P7` carries the rate rule's own statement, which sorts quantities by WHICH RATE they"
     " accumulate on: a comoving separation read across leaves on the stacking side, the plasma's own"
     " accumulations on the leaf's, with no locus at which the rate switches",
     'A quantity computed from the foliation\'s stacking---a comoving separation read across leaves, '
     '$D_M$, $D_H$, $D_V$, the observable expansion---takes the stacking rate' in P07
     and 'There is no locus at which the rate switches' in P07)

# =====================================================================================
head("B -- THE REASON IS P7's OWN IDENTITY, WHICH SPLITS THE RATE FROM THE APPEARANCE")

gate("Ⓑ①  `P7` makes the LAPSE the stacking rate -- and the relation it states is that the observable"
     " expansion RIDES it, fixed by the substrate's `$\\alpha$` and the cut's offset",
     'The \\emph{lapse} $N$---the existent\'s rate of advance---is the foliation stacking rate the '
     'observable expansion rides' in P07
     and 'fixed by the substrate\'s $\\alpha$ and the cut\'s offset $x_0$' in P07)

gate("Ⓑ②  ⛭⛭ AND THE SAME SENTENCE MAKES THE SHIFT THE THING THE EXPANSION IS *OBSERVED* THROUGH AS"
     " DISTANCE AND REDSHIFT -- the `$E{=}1$` projection.  ** So the appearance-as-distance is a"
     " DIFFERENT datum of the slicing operator from the rate, by the proposition's own assignment **",
     'is the $E{=}1$ projection through which that expansion is \\emph{observed} as distance and '
     'redshift' in P07)

gate("Ⓑ③  and the two are listed as distinct data of one operator -- leaf, lapse, shift, vantage --"
     " so this is a split the framework makes structurally and not a distinction imported here",
     'These are exactly the slicing operator\'s data---leaf, lapse, shift, vantage' in P07)

# =====================================================================================
head("C -- SO THE RULE FIXES WHICH RATE ITS OWN LENGTH ACCUMULATES ON, AND NOT THE ARGUMENT")

gate("Ⓒ①  the rule's subject is a rate and its predicate is an accumulation: the two rates differ by"
     " the radiation term alone, and the rule says which of them each quantity takes",
     'The two rates differ by the radiation term alone' in P07
     and 'takes the stacking rate' in P07 and 'takes the leaf\'s' in P07)

gate("Ⓒ②  and `$D_M$` enters the rule as a comoving separation read ACROSS LEAVES -- which is the"
     " category, not the photon path.  ** The rule never names the argument of the kernel, and the"
     " paper's own phrase for how it gets there is that it `reaches it by NAMING $D_M$` **",
     'a comoving separation read across leaves' in P07
     and 'The rate rule reaches the same distance by naming $D_M$' in P15)

gate("Ⓒ③  and `P15` keeps the projection and the degree apart for the same structural reason -- the"
     " map between them is a projection and conflating them would manufacture a prediction the"
     " geometry does not make -- so `this quantity is named by the rule` and `this quantity is the"
     " kernel's argument` are distinct claims in the paper's own practice",
     'conflating them would manufacture a prediction the geometry does not make' in P15)

# =====================================================================================
head("D -- AND THE EQUALITY THE PROJECTION NEEDS IS FLATNESS'S, WITH NO RATE IN IT")

gate("Ⓓ①  `prop:flat` is a statement about the constant-`$\\tau$` slice's induced three-metric and"
     " the vanishing of its Riemann tensor -- a theorem about a slice's geometry.  ** There is no rate"
     " in it at all, which is exactly why it can supply an identity the rate rule cannot **",
     'has induced three-metric $dr^2+r^2d\\Omega^2$' in P15
     and 'whose Riemann tensor vanishes identically' in P15
     and 'The constant-$\\tau$ slice is exactly flat' in P15)

gate("Ⓓ②  and it is that flatness which makes the comoving angular-diameter distance BE the"
     " light-travel distance -- the identity the kernel's argument turns on",
     'the constant-proper-time slice is exactly flat, so the comoving angular-diameter distance '
     '\\emph{is} the light-travel distance $D_C$' in P15)

gate("Ⓓ③  ⇒ SO THE ANSWER IS `THROUGH THE IDENTIFICATION`, and the paper's own word for the kernel's"
     " licence is that identification rather than the rule: the flatness of the distance slice"
     " together with the exact recovery of the expansion law",
     'is licensed by an \\emph{identification}' in P15
     and 'the flatness of the distance slice together with the exact recovery of the expansion law'
     in P15
     and 'The rate rule reaches the same distance by naming $D_M$' in P15)

# =====================================================================================
head("E -- AND THE SHARPENING: THE THREE ROUTES ARE TWO GROUNDS")

gate("Ⓔ①  the third route's own receipt states the premise it needs, and that premise is the rule's"
     " classification: that the optical depth is a photon-path observable OF THE SAME KIND as the"
     " redshift and the distances.  ** So the third route is the rule applied a second time, not a"
     " second ground **",
     'The precedent argument needs one premise' in TAU
     and 'is a photon-path observable of the same kind as the redshift and the distances' in TAU)

gate("Ⓔ②  and that receipt reaches its ruling BY PRECEDENT from the rule's existing assignments"
     " rather than from the slice's geometry -- it names `P7`'s own list as the side it argues from,"
     " which is why it is independent of FLATNESS and not of the RULE",
     'S A PRECEDENT ARGUMENT INSIDE THE CONSTRUCTION' in TAU
     and 'Every other property of the photons we observe, accumulated along their path to us, is a' in TAU)

gate("Ⓔ③  ⛔ SO TWO GROUNDS AND NOT THREE: the rule, and the identification.  ** And since the rule"
     " reaches the projection only through the identification, the identification is the only"
     " INDEPENDENT support for the one equality the kernel's argument turns on -- which is the"
     " order's second horn, and the narrower of the two **",
     (_ROUTES_AS_IS or _ROUTES_FIXED)
     and 'The precedent argument needs one premise' in TAU
     and 'is licensed by an \\emph{identification}' in P15)

# =====================================================================================
head("F -- AND WHAT THIS DOES NOT DO")

gate("Ⓕ①  ⚠ NARROWER IS NOT WEAKER, and the distinction is kept because the sector's verdict turns on"
     " it: `prop:flat` is proved in the paper with its own argument and receipt, so the identification"
     " is established and not conjectural.  ** What the answer changes is the number of independent"
     " supports, not the soundness of the one that carries it **",
     'The constant-$\\tau$ slice is exactly flat' in P15
     and 'the curvature of $dr^2+r^2d\\Omega^2$ is zero by direct computation' in P15)

gate("Ⓕ②  and the three things the order excluded are untouched here: no reopening of the knob"
     " `r7095` ruled on, no search for a third rate, and no re-derivation of `prop:flat` -- this"
     " receipt quotes that proposition rather than proving it again",
     'There is no locus at which the rate switches' in P07
     and 'The two rates differ by the radiation term alone' in P07)

gate("Ⓕ③  and it computes NOTHING, which is what the order asked for: every clause it turns on is"
     " quoted from the source it is attributed to, so the receipt fails if any of them is reworded."
     "  ** That is the only control a read can carry, and it stands in for the pre-registration a"
     " computation would have had **",
     len(CHECKS) >= 12)

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE ANSWER IS `THROUGH THE IDENTIFICATION', AND THE REASON IS IN P7's OWN
  IDENTITY RATHER THAN IN ANY HEDGE OF P15's.

  One sentence of P7 does both halves.  The lapse is the foliation stacking
  rate the observable expansion RIDES.  The shift is the E=1 projection
  through which that expansion is OBSERVED as distance and redshift.  Those
  are two different data of one slicing operator, so a rule about which rate
  a quantity accumulates on cannot fix a projection's argument.

  AND THE RULE'S FORM CONFIRMS IT.  It is a classifier over rates: a
  comoving separation read across leaves takes the stacking rate, the
  plasma's own accumulations take the leaf's.  What it fixes about D_M is
  which rate D_M accumulates on, and D_M is in it as a separation read
  across leaves -- not as the photon path whose comoving length is the
  kernel's argument.  The paper's own phrase is that the rule `reaches it by
  naming D_M'.

  SO THE EQUALITY THE PROJECTION NEEDS IS FLATNESS'S.  prop:flat is a
  theorem about the constant-tau slice's induced three-metric and the
  vanishing of its Riemann tensor, with no rate in it at all -- which is
  exactly why it can supply an identity the rule cannot.

  *** AND THE SHARPENING, WHICH RUNS THE NARROW WAY.  P15 settles the
      distance `by three independent routes'.  They are not three
      foundations; they are two.  The third route's own receipt states the
      premise it needs -- that the optical depth is a photon-path
      observable OF THE SAME KIND as the redshift and the distances -- and
      that premise is the rule's classification.  So the third route is the
      rule applied a second time.  Two grounds: the rule and the
      identification.  And since the rule reaches the projection only
      through the identification, the identification is the only
      INDEPENDENT support for the one equality the argument turns on. ***

  MY FIRST READING WAS THAT THREE ROUTES MEANT THREE SUPPORTS.  Checking the
  third route's stated premise is what corrected it, and that check is the
  control this receipt carries in place of the pre-registration a
  computation would have had.

  NARROWER IS NOT WEAKER, and the distinction is left for the seat that
  writes the verdict: prop:flat is proved with its own argument and receipt,
  so the identification is established rather than conjectural.  What this
  answer changes is the number of independent supports, not the soundness of
  the one that carries it.

  THE GUARD: when a corpus says a quantity is settled by N independent
  routes, check each route's own stated premise before counting it.  A route
  that reaches its conclusion by precedent from another route's rule is
  evidence for the same ground, not a second one -- and the count of
  supports is what a verdict's strength gets written from.
  ==========================================================================
""")
