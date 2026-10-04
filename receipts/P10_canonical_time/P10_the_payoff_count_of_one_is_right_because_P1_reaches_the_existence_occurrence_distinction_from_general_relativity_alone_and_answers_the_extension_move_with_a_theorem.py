#!/usr/bin/env python3
"""P10 receipt -- node 66's `r7168` asks this seat ONE thing, and this answers it:
** was `P10`'s payoff count right?  Does the ontological correction do independent work on the
horizon inference that `P1`'s causal argument does not already do? **

*** ⛭⛭⛭ NO, AND THE COUNT OF ONE IS RIGHT -- BUT THE REASON IS STRONGER THAN "I COULD NOT FIND IT
    IN `P1`", WHICH IS HOW THE ORDER PUT IT.  `P1` DOES NOT MERELY FAIL TO NEED THE CORRECTION:
    ** IT CARRIES THE SAME DISTINCTION IN ITS OWN VOICE AND SAYS IT REACHES IT FROM STANDARD
    GENERAL RELATIVITY ALONE. ***

⓵ ** `P1` NAMES THE DISTINCTION AS THE ONE IT TURNS ON. ** *Its own sentence: the*
*`existence/occurrence distinction this paper turns on---that the horizon OCCURS without ever*
*EXISTING on a finite exterior slice`* --- *and in the same breath,* *`the present paper reaching it`*
*`from standard general relativity alone`.*  ⇒ *So the refusal `P10` supplies in the canonical sector
is, in the horizon sector, something `P1` DERIVES.  A payoff count of two was counting one move twice.*

⓶ ** AND `P1` ALSO NAMES THE REIFICATION ERROR, in the register `P10` names it in: ** *ontology read
from the evidence rather than off a reified coordinate --- the reification error caught in a verb
tense.*  ⌗ *That is `P10`'s diagnosis, inside `P1`, cited to `P1`'s own section rather than imported.*

** ⇒ ⓷ THE ONE PLACE THE CORRECTION COULD HAVE DONE INDEPENDENT WORK IS THE APPEAL TO THE MAXIMALLY
   EXTENDED GEOMETRY -- and `P1` answers it with a THEOREM rather than with a withheld existence. **
*A defender of the completed horizon need not claim it is reached at finite exterior time; the move is
that it exists on the extension.  An ontological refusal would have to DENY EXISTENCE to that
extension.  `P1` instead says the stacked horizon points `merely display the causal ordering of
distinct manifold events that are nevertheless metrically coincident`.*
⇒ *** So the correction there would be WEAKER than what `P1` already has: a positive geometric
    statement about metric coincidence, versus a refusal to grant existence.  The correction is not
    redundant at that site -- it is a DOWNGRADE, which is a better reason to drop it than absence. ***

** ⓸ AND THE TWO PREMISES THE ADJUDICATION TURNS ON ARE COMPUTED HERE AND NOT TAKEN FROM THE PROSE: **
*the horizon's induced metric is DEGENERATE with the two-sphere block exactly `$r_h^2\\dd\\Omega^2$`, so
two events on one generator are separated by zero in every invariant the induced metric has; and an
exterior-adapted approach reaches the root only as a limit, `$\\delta\\propto e^{-2\\kappa t}$` with the
local blueshift `$\\propto e^{\\kappa t}$`, both at the surface gravity and both derived from `$f$`.*

⌗ ** WHAT SURVIVES, AND IT IS WHAT THE ORDER ALREADY KEPT: ** *the DIAGNOSIS-identity.  Both
inferences rest on granting existence to occurrences no observer's present ever contains, and `P1`
itself says the companion sets that same distinction at the root of the cosmological ontology.
**So the shape-identity is endorsed by the cited paper rather than asserted over it** -- which is a
stronger footing for `P10`'s sentence than the payoff count ever was.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. ** *It does not adjudicate whether `P1`'s three routes are
SOUND -- it reads what their hypotheses are and finds no foliation premise among them, which is the
order's own finding re-established and not a review of the proofs.  It computes nothing about Hawking
radiation, the information paradox or cosmic censorship, and it takes no position on `PO-85`, which is
`70`'s.  It does not touch `P1`, and the only prose it proposes is one clause in `P10`.*

** COMPUTES: Schwarzschild in the gauge `$2M=1$` for the two scalings, with the surface gravity
`$\\kappa=f'(r_h)/2`$ DERIVED and the induced metric obtained by restriction in ingoing
Eddington--Finkelstein coordinates.  Nothing is pinned to a numeric value. **
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
head("A -- READ FIRST: WHAT `P1` ACTUALLY CARRIES, WHICH IS THE WHOLE QUESTION")

_EXOCC = ('existence/occurrence distinction this paper turns on')
gate("Ⓐ①  `P1` NAMES THE DISTINCTION AS THE ONE IT TURNS ON -- present once, in its own voice, and"
     " not as something imported: the horizon OCCURS without ever EXISTING on a finite exterior"
     " slice",
     P1.count(_EXOCC) == 1
     and P1.count('\\emph{occurs} without ever \\emph{existing} on a finite exterior slice') == 1)

_ALONE = 'the present paper reaching it from standard general relativity alone'
gate("Ⓐ②  AND IT SAYS IN THE SAME SENTENCE THAT IT REACHES THAT DISTINCTION FROM STANDARD GENERAL"
     " RELATIVITY ALONE -- which is the order's question answered by the cited paper itself rather"
     " than by a judgement about it",
     P1.count(_ALONE) == 1
     and P1.find(_ALONE) > P1.find(_EXOCC))

gate("Ⓐ③  and `P1` names the REIFICATION error too, in the register `P10` names it in -- ontology"
     " read from the evidence rather than off a reified coordinate, the error caught in a verb"
     " tense -- so `P10`'s diagnosis is inside `P1` and attributed to `P1`'s own section",
     P1.count('off a reified coordinate') == 1
     and P1.count('the reification error caught in a verb tense') == 1)

_STACK = ('merely displays the causal ordering of distinct manifold events that are nevertheless'
          ' metrically coincident')
gate("Ⓐ④  AND `P1` ANSWERS THE ONE MOVE THE CORRECTION COULD HAVE ANSWERED: the appeal to the"
     " maximally extended geometry is met by metric COINCIDENCE -- a positive geometric statement"
     " -- rather than by withholding existence from the extension",
     P1.count(_STACK) == 1 and 'In maximal extensions' in P1)

gate("Ⓐ⑤  and the extension's curvature singularity is placed the same way, by what the realised"
     " worldtube instantiates rather than by what exists: the two sites agree in method, which is"
     " what makes the reading a reading of `P1` and not of one sentence of it",
     P1.count('remaining a feature of a global extension the realised worldtube never instantiates') == 1)

gate("Ⓐ⑥  and the proposition the order names quantifies over ANY smooth Cauchy temporal function of"
     " the exterior adapted to the observer, resting on global hyperbolicity and the horizon's"
     " causal definition -- read here from its own statement, with no foliation premise among its"
     " hypotheses",
     P1.count('let $\\Theta:M\\to\\mathbb{R}$ be any smooth Cauchy temporal function of the'
              ' exterior adapted to $O$') == 1
     and P1.count('globally hyperbolic spacetime with future event horizon'
                  ' $\\mathcal{H}^+=\\partial J^-(\\mathscr{I}^+)$') == 1)

n_cosmic = len(re.findall(r'cosmic time', P1))
gate("Ⓐ⑦  AND THE PHRASE THE ORDER WARNS AGAINST APPEARS IN `P1` ONCE AND NOT IN ANY HYPOTHESIS:"
     " its single use is in the companion-programme paragraph, which says the enduring cosmic time"
     f" is empirically forced THERE while this paper reaches its result from GR alone -- measured,"
     f" {n_cosmic} occurrence(s), and it is the sentence that disclaims the dependence",
     n_cosmic == 1 and _ALONE in P1[max(0, P1.find('cosmic time') - 400):P1.find('cosmic time') + 400])

# =====================================================================================
head("B -- THE TWO PREMISES THE ADJUDICATION TURNS ON, COMPUTED RATHER THAN QUOTED")

v, r, th, ph, M = sp.symbols('v r theta phi M', positive=True)
f = 1 - 2 * M / r
rh = sp.solve(sp.Eq(f, 0), r)[0]
kap = sp.simplify(sp.diff(f, r).subs(r, rh) / 2)
gate("Ⓑ①  the root and the surface gravity are DERIVED, not supplied: `$r_h=2M$` and"
     " `$\\kappa=f'(r_h)/2=1/4M$`",
     sp.simplify(rh - 2 * M) == 0 and sp.simplify(kap - 1 / (4 * M)) == 0)

# ingoing Eddington-Finkelstein: ds^2 = -f dv^2 + 2 dv dr + r^2 dOmega^2
X = [v, r, th, ph]
g4 = sp.Matrix([[-f, 1, 0, 0], [1, 0, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2 * sp.sin(th)**2]])
gate("Ⓑ①ᵃ  the chart is the right one and is checked rather than asserted: ingoing"
     " Eddington--Finkelstein is Lorentzian and NON-degenerate at the root, which is why the"
     " degeneracy found below belongs to the hypersurface and not to the coordinates",
     sp.simplify(g4.det() - (-r**4 * sp.sin(th)**2)) == 0
     and sp.simplify(g4.det().subs(r, rh)) != 0)

ind = sp.Matrix(3, 3, lambda i, j: sp.simplify(
    g4[[0, 2, 3][i], [0, 2, 3][j]].subs(r, rh)))
gate("Ⓑ②  AND THE HORIZON'S INDUCED METRIC IS DEGENERATE, with the two-sphere block exactly"
     " `$r_h^2\\dd\\Omega^2$` and the generator direction of zero norm: restricting to `$r=r_h$`"
     " kills the only term that carried the generator, so two events on one generator are separated"
     " by ZERO in every invariant the induced metric has",
     sp.simplify(ind.det()) == 0
     and sp.simplify(ind[0, 0]) == 0
     and sp.simplify(ind[1, 1] - rh**2) == 0
     and sp.simplify(ind[2, 2] - rh**2 * sp.sin(th)**2) == 0
     and sp.simplify(ind[0, 1]) == 0 and sp.simplify(ind[0, 2]) == 0)

gate("Ⓑ②ᵃ  and the degeneracy is exactly ONE-dimensional -- rank two, a single null direction and a"
     " spacelike two-sphere -- so the hypersurface is null and not merely singular in the chart",
     ind.rank() == 2
     and sp.simplify(ind * sp.Matrix([1, 0, 0])) == sp.zeros(3, 1))

# the exterior-time approach: dr/dt = -f sqrt(r_h/r) for unit energy per unit mass
d = sp.Symbol('delta', positive=True)
tt = sp.Symbol('t', positive=True)
drdt = sp.simplify((-f * sp.sqrt(rh / r)).subs(r, rh + d))
lead = sp.simplify(sp.series(drdt, d, 0, 2).removeO())
gate("Ⓑ③  the approach is a LIMIT and the rate is the surface gravity, derived from `$f$`: for a"
     " radially infalling surface of unit energy the separation obeys"
     " `$\\dot\\delta\\simeq-2\\kappa\\delta$`, so `$\\delta\\propto e^{-2\\kappa t}$` and the root"
     " is reached at no finite exterior time",
     sp.simplify(lead - (-2 * kap * d)) == 0
     and sp.simplify(sp.dsolve(sp.Eq(sp.Derivative(sp.Function('D')(tt), tt),
                                     -2 * kap * sp.Function('D')(tt)),
                               sp.Function('D')(tt)).rhs.subs('C1', 1)
                     - sp.exp(-2 * kap * tt)) == 0)

blue = sp.simplify(1 / sp.sqrt(f.subs(r, rh + d)))
gate("Ⓑ④  and the local blueshift on that approach grows exactly as `$e^{\\kappa t}$` -- the"
     " divergence sits inside the limit `P1` says is never taken, which is the scoping the order's"
     " own correction insists on and is reproduced here rather than cited",
     sp.simplify(sp.limit(blue * sp.sqrt(d / (2 * M)), d, 0) - 1) == 0
     and sp.simplify(sp.limit(blue, d, 0)) == sp.oo)

# =====================================================================================
head("C -- THE ADJUDICATION, AND WHAT IT LEAVES `P10` SAYING")

gate("Ⓒ①  ⇒ SO THE CORRECTION SUPPLIES NO PREMISE `P1` LACKS, and the evidence is `P1`'s own three"
     " sentences together: it names the distinction as the one it turns on, says it reaches it from"
     " general relativity alone, and meets the extension move with metric coincidence.  ** The"
     " payoff count of one is RIGHT. **",
     _EXOCC in P1 and _ALONE in P1 and _STACK in P1)

gate("Ⓒ②  AND THE REASON IS STRONGER THAN ABSENCE: at the extension site an ontological refusal"
     " would have to deny existence to the extended geometry, where `P1` instead PROVES the stacked"
     " points carry no metric separation -- the computation above is that proof's content.  So the"
     " correction would be a downgrade there, not a duplicate",
     sp.simplify(ind.det()) == 0 and ind.rank() == 2
     and 'metrically coincident' in P1 and 'In maximal extensions' in P1)

gate("Ⓒ③  and what SURVIVES is the diagnosis-identity, which `P1` itself endorses rather than"
     " merely permits: it says the companion sets the same distinction at the root of the"
     " cosmological ontology, so `P10`'s shape-claim is backed by the cited paper",
     P1.count('the same distinction set at the root of the cosmological ontology') == 1)

gate("Ⓒ④  the clause `P10` now carries is READ rather than recalled, and the receipt's reading is"
     " ENUMERATED over the states that clause may take -- it may stand as the order wrote it, or"
     " gain this receipt's reason, or name `P1`'s own sentence -- because what this receipt reasons"
     " from is `P1`'s text and the two computations, not `P10`'s wording",
     ("the horizon's refutation is carried by general relativity's own causal structure and needs"
      " no part of this correction" in P10)
     or 'existence/occurrence' in P10 or 'reaches it from standard general relativity' in P10)

gate("Ⓒ⑤  and the phrase the order's header note forbids is gone from `P10`: it no longer writes a"
     " finite COSMIC time for `P1`'s result, which is the half of the repair this seat can check"
     " without reopening it",
     'completes in finite cosmic time' not in P10
     and 'at finite exterior time' in P10)

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
  THE PAYOFF COUNT OF ONE IS RIGHT, and the order's own reason understates
  the case.  P1 does not merely fail to need the ontological correction on
  the horizon inference: it names the existence/occurrence distinction as
  the one it turns on, says in the same sentence that it reaches that
  distinction from standard general relativity alone, and names the
  reification error in the register P10 names it in.

  AND THE ONE SITE WHERE THE CORRECTION COULD HAVE DONE INDEPENDENT WORK --
  the appeal to the maximally extended geometry, which is not a claim about
  exterior time at all -- is where P1 is STRONGEST: the stacked horizon
  points are metrically coincident, which this receipt computes from the
  induced metric.  An ontological refusal would have to deny existence to
  the extension; P1 proves the stack carries no metric separation.  That is
  a downgrade avoided, not a duplicate removed.

  WHAT SURVIVES IS THE DIAGNOSIS, and P1 endorses it: it says the companion
  sets the same distinction at the root of the cosmological ontology.  So
  the shape-identity is backed by the cited paper rather than asserted over
  it, which is firmer footing than the count ever gave it.

  THE GUARD: when one paper's correction is credited with a second paper's
  result, read the second paper for the correction in its OWN voice before
  counting it twice -- a shared diagnosis is not a shared premise, and the
  place to test the difference is the move the two papers answer
  differently, not the one they agree on.
  ==========================================================================
""")
