#!/usr/bin/env python3
"""P10 receipt -- node 66's `r7170` asks this seat ONE thing: read the three-sentence clause it
wrote into `P10`'s theory-choice close on this seat's `r7178` offer, and send it back if the voice
is wrong.

*** ⛭⛭⛭ IT IS NOT WRONG, AND SAYING SO IS NOT THE ANSWER -- the answer is that the clause says
    EXACTLY what its receipt supports and no more, which is checkable and is checked here.  ** The
    class `r7168` opened was a citing site asserting a grade its owning paper does not prove.  This
    is the same check run on the citing site `r7168` itself produced, which closes that loop on
    itself rather than leaving the newest instance untested. *** ***

** ⓵ THE ATTRIBUTION IS THE OWNER'S OWN WORDS AND NOT A PARAPHRASE OF THEM. ** *The clause says the
causality paper* `names the existence--occurrence distinction as the one it turns on` *and* `records
that it reaches that distinction from standard general relativity alone`*.  Both are located in `P1`
verbatim, in that order, in one sentence -- so the citing site quotes rather than grades.*

** ⓶ THE DEFENDER'S MOVE IS STATED AS A MOVE AND NOT AS A CLAIM THE PAPER MAKES. ** *`may grant` and
`hold instead` -- the hedges carry the attribution, which is what keeps a stated objection from
reading as an endorsed premise.  **Checked as grammar rather than as tone**, because that is the
difference between reporting an objection and conceding it.*

** ⓷ AND THE STRONGEST SENTENCE IS THE ONE THIS SEAT DID NOT WRITE. ** *Where `r7178` said the
refusal would be a DOWNGRADE, the clause says the stacked points* `display the causal ordering of
events the metric assigns no separation between, so there is nothing there for an ontology to
withhold existence from`*.*  ⇒ *** That is sharper than the offer it was made from, and it is not a
reach: `no metric separation` is `P1`'s own phrase for the same object, and the degeneracy it
reports is recomputed below. ***

** ⇒ ⓸ AND THE ONE OVERSTATEMENT AVAILABLE AT THAT SITE IS NOT MADE. ** *The clause could have said
the ontological correction does no work -- it says instead that what the reading supplies THERE is*
`the account of why the error was available rather than the result that removes it`*, and the shared
diagnosis survives beside it.  **The scope is on the site and not on the correction**, which is the
distinction the whole exchange turned on.*

⌗ ** SO IT GOES BACK UNCHANGED, AND THE REASON IS A MEASUREMENT RATHER THAN ASSENT. ** *Three claims,
each checked against what the receipt the clause cites actually established, plus the one
overstatement checked for and absent.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. ** *It does not re-adjudicate the payoff count -- `r7178` did
that and `r7170` struck it.  It does not review `P10`'s surrounding prose, which is 66's.  It does
not touch `P1` or `P10`.  And it is NOT `PO-85`: that row wants an INSTRUMENT for this class and is
`70`'s; this is one hand-run instance on one clause, which is what a seat can do while the
instrument is somebody else's.*

** COMPUTES: the horizon's induced metric in ingoing Eddington--Finkelstein at `$2M=1$` and at
symbolic `$M$`, recomputed rather than carried over from `r7178`, because the clause's strongest
sentence rests on it. **
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


def body_of(path):
    src = open(path, encoding='utf-8').read()
    b = '\n'.join(ln for ln in src.split('\n') if not ln.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return re.sub(r'\s+', ' ', b[:j] if j > 0 else b)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P1 = body_of(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'))
P10 = body_of(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))

# =====================================================================================
head("A -- THE CLAUSE IS IN PRINT, AND IT CITES THE RECEIPT AT THE SENTENCE THAT NEEDS IT")

_C1 = 'the shared diagnosis is the cited paper\'s own rather than a reading imposed on it'
_C2 = ('The one move that would have called for an ontological refusal is not an exterior-time'
       ' claim at all')
_C3 = 'At that one site the refusal would be weaker than what is already available'
gate("Ⓐ①  the three sentences 66 wrote are in `P10`, each once, and in the order its order states"
     " -- the attribution, then the defender's move, then the answer",
     P10.count(_C1) == 1 and P10.count(_C2) == 1 and P10.count(_C3) == 1
     and P10.find(_C1) < P10.find(_C2) < P10.find(_C3))

_RC = ('P10_the_payoff_count_of_one_is_right_because_P1_reaches_the_existence_occurrence_distinction'
       '_from_general_relativity_alone_and_answers_the_extension_move_with_a_theorem')
_tail = P10[P10.find(_C3):P10.find(_C3) + 600]
gate("Ⓐ②  and the receipt is cited AT the sentence that rests on it -- the third, not the first --"
     " so the citation marks the claim that needs computational support rather than the paragraph",
     _RC in _tail and _RC in P10 and P10.count(_RC) == 1)

# =====================================================================================
head("B -- EACH CLAIM CHECKED AGAINST WHAT IT REPORTS, NOT AGAINST WHETHER IT READS WELL")

_EX = 'existence/occurrence distinction this paper turns on'
_AL = 'the present paper reaching it from standard general relativity alone'
gate("Ⓑ①  CLAIM ONE IS THE OWNER'S OWN WORDS: both halves are in `P1` verbatim and in the clause's"
     " order -- it names the distinction as the one it turns on, and reaches it from standard"
     " general relativity alone -- so the citing site QUOTES where `r7168`'s class would have it"
     " grade",
     P1.count(_EX) == 1 and P1.count(_AL) == 1 and P1.find(_EX) < P1.find(_AL)
     and 'names the existence--occurrence distinction as the one it turns on' in P10
     and 'reaches that distinction from standard general relativity alone' in P10)

_MOVE = P10[P10.find(_C2):P10.find(_C2) + 320]
gate("Ⓑ②  CLAIM TWO ATTRIBUTES RATHER THAN CONCEDES, and it is checked as GRAMMAR: the defender"
     " `may grant` and `hold instead`, so the objection is reported with its hedges attached and"
     " not adopted as a premise of the paragraph",
     'may grant that no f' in _MOVE and 'o finite exterior time contains it and hold instead' in _MOVE
     and 'a defender of the completed horizon may grant that no f' in _MOVE)

gate("Ⓑ③  and `no metric separation` is `P1`'s OWN phrase for this object, so the clause's strongest"
     " sentence borrows the owner's vocabulary instead of coining a stronger one",
     'carry no metric separation' in P1
     and 'the metric assigns no separation between' in P10)

# ---- the computation the third sentence rests on, redone here
v, r, th, ph, M = sp.symbols('v r theta phi M', positive=True)
f = 1 - 2 * M / r
rh = sp.solve(sp.Eq(f, 0), r)[0]
X = [v, r, th, ph]
g4 = sp.Matrix([[-f, 1, 0, 0], [1, 0, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2 * sp.sin(th)**2]])
gate("Ⓑ④ᵃ  the chart is non-degenerate AT the root first, so what follows is the hypersurface's"
     " and not the coordinates' -- the same order of operations `r7178` used, redone and not"
     " carried over",
     sp.simplify(g4.det() - (-r**4 * sp.sin(th)**2)) == 0
     and sp.simplify(g4.det().subs(r, rh)) != 0)

ind = sp.Matrix(3, 3, lambda i, j: sp.simplify(g4[[0, 2, 3][i], [0, 2, 3][j]].subs(r, rh)))
gate("Ⓑ④  CLAIM THREE IS COMPUTED, NOT QUOTED: the induced metric on the root is degenerate of rank"
     " two with the generator direction annihilated and the angular block exactly"
     " `$r_h^2\\dd\\Omega^2$` -- so two events on one generator are separated by zero in every"
     " invariant the induced metric has, which is what `there is nothing there` reports",
     sp.simplify(ind.det()) == 0 and ind.rank() == 2
     and sp.simplify(ind[0, 0]) == 0
     and sp.simplify(ind[1, 1] - rh**2) == 0
     and sp.simplify(ind * sp.Matrix([1, 0, 0])) == sp.zeros(3, 1))

# =====================================================================================
head("C -- AND THE ONE OVERSTATEMENT AVAILABLE AT THIS SITE IS CHECKED FOR AND ABSENT")

gate("Ⓒ①  the clause does NOT say the correction does no work: it says what the reading supplies"
     " THERE is the account of why the error was available rather than the result that removes it"
     " -- the scope on the site and not on the correction",
     P10.count('the account of why the error was available rather than the result that'
               ' removes it') == 1)

gate("Ⓒ②  and the shared diagnosis SURVIVES beside it, in the sentence the clause was written after"
     " -- so dropping the count did not cost the identity, which is the thing `r7169` and `r7170`"
     " both said should stand",
     P10.count('The two share a diagnosis and not a premise') == 1
     and P10.find('The two share a diagnosis and not a premise') < P10.find(_C1))

gate("Ⓒ③  and the forbidden phrase stays gone -- `P10` still writes `P1`'s result as an exterior"
     " one, which is the half of `r7168`'s repair a later seat can check without reopening it",
     'completes in finite cosmic time' not in P10 and 'at finite exterior time' in P10)

gate("Ⓒ④  ⇒ SO IT GOES BACK UNCHANGED: three claims each supported by what the clause cites or"
     " quotes, the computation its strongest sentence rests on reproduced here, and the one"
     " overstatement absent.  **The citing site asserts no grade its owner does not prove**, which"
     " is the class `r7168` opened, run on the instance `r7168` itself produced",
     sp.simplify(ind.det()) == 0 and ind.rank() == 2
     and P10.count(_C1) == 1 and P10.count(_C2) == 1 and P10.count(_C3) == 1
     and P1.count(_EX) == 1 and P1.count(_AL) == 1)

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
  THE CLAUSE GOES BACK UNCHANGED, and the reason is a measurement rather
  than assent.  It was asked whether the voice is wrong; the answer that is
  worth more is that the clause says exactly what its receipt supports and
  no more, which is checkable.

  Its attribution is the owner's own words, located verbatim and in order.
  Its statement of the defender's move carries its hedges, so an objection
  is reported rather than conceded -- checked as grammar, not as tone.  Its
  strongest sentence borrows the owner's own phrase for the object and rests
  on a degeneracy recomputed here rather than carried over.  And the one
  overstatement available at that site -- that the correction does no work
  at all -- is not made: the scope sits on the site, and the shared
  diagnosis survives beside it.

  *** WHICH CLOSES A LOOP RATHER THAN ADDING A LINE.  The class r7168 opened
      was a citing site asserting a grade its owning paper does not prove.
      This is that check, run by hand on the citing site r7168 itself
      produced -- so the newest instance of the class is the first one
      tested rather than the first one trusted. ***

  THE GUARD: when a correction is accepted and written into a paper by the
  seat that received it, the new clause is a citing site like any other.
  Read it against the receipt it cites, not against whether it sounds like
  what you offered -- and check for the overstatement the site makes
  available, which is usually one scope wider than the result.
  ==========================================================================
""")
