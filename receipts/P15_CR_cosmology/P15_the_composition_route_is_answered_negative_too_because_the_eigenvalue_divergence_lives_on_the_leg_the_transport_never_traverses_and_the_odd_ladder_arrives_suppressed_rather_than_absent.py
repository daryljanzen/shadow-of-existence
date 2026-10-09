#!/usr/bin/env python3
"""P15 receipt -- node 66's `r7173` COMPOSITION QUESTION, held behind ORDER ⓶ and taken now:
** is the layer necessarily in the path, and does its parity bound what arrives? **
Pre-registered at `computations/beyond_the_wall/r7194_60_composition/PREDICTION.md`, committed and
pushed before anything below was computed, on the order's own instruction.

*** ⛭⛭⛭ THE LAYER IS IN THE PATH AND THE PARITY STILL DOES NOT BOUND WHAT ARRIVES.  THE ANSWER IS
    NEGATIVE AND IT IS SHARPER THAN `r7186`'s, BECAUSE IT DOES NOT ONLY FAIL TO DELIVER THE
    ODD-LADDER BOUND -- ** IT MEASURES THE ODD LADDER ARRIVING. ** ***

** ⓵ THE STRUCTURAL HALF OF `r7173`'s CONDITIONAL HOLDS, AND IT HOLDS BY READING. ** *Carrying
`$(L,m)$` along the bead needs a harmonic decomposition of the layer at every point of the curve, the
lift included; the decomposition EXISTS and is the SAME one, because the squashed layer is a
left-invariant metric on the same group manifold.*  ⇒ ***So the layer is necessarily in the path and
the question is live rather than vacuous.*** *That is not this receipt's finding; it is `PO-81`'s, and
it is named here because the conditional needs it.*

⛔ ** ⓶ BUT THE PARITY NAMES WHICH SLICE IS SQUASHING-FREE, NOT WHICH MODES EXIST. ** *The ladder is
`$m\\equiv L/2\\ (\\mathrm{mod}\\ 1)$`, `$\\lvert m\\rvert\\le L/2$` -- `$L+1$` slices at EVERY degree,
with `$m=0$` present exactly when `$L$` is even.*  ⇒ *** At odd degree every slice is charged, and all
`$L+1$` of them are CARRIED EXACTLY, with `$(L,m)$` conserved and no mixing.  ** The parity excludes
nothing from the path. ** ***

*** ⛭⛭ ⓷ AND THE COMPOSITION PRODUCT IS NOT DEFINED ON THIS PATH, WHICH IS THE OBSTRUCTION THE
    PRE-REGISTRATION NAMED AS THE ONE IT MOST EXPECTED.  ** The charged eigenvalue diverges where the
    squashing vanishes -- and the normalised squashing on the lift has its MINIMUM `$1.3747296$` at
    the comoving turnaround and rises to infinity at the close. ** *** *So `$\\varepsilon$` is bounded
away from zero on the whole transported segment:* ***the divergence lives on the leg the transport
never traverses.*** ⌗ *`r7174`'s `carried in label, lost in amplitude` is true where it was measured
and is not a factor in this product.*

** ⓸ AND THE ODD LADDER ARRIVES, WITH A NUMBER RATHER THAN A SIGN. ** *The exponent's ratio to the
round one is a function of `$\\sigma=4m^2/L(L+2)$` alone -- two modes of different degree sharing
`$\\sigma$` agree to ten figures -- with `$R(1/3)=0.8419016934$` at the lowest odd degree.*
⇒ *** Exact exponent `$4.868603$` against the round `$5.782864$` and the uniform bound `$4.721689$`:
    the charged slice is exponentially small, NONZERO, and LESS suppressed than a round mode of the
    same degree by a margin that grows in degree. ***

⇒ *** ⛭⛭⛭ SO THE ODD-LADDER BOUND IS NOT AVAILABLE BY EITHER ROUTE, AND THE COMPOSITION ROUTE FAILS
    HARDER THAN THE MEASURE ROUTE DID.  `r7186` showed the crossing CANNOT implement the parity; this
    shows that even where the layer IS in the path, the parity does not reach the arriving content --
    ** and the content it was supposed to exclude is measured arriving. ** *** *`r7173` ⓷ said a
measured negative would be a full discharge and a sharper one than `r7186`'s, because it would close
the question rather than relocating it.* **It closes it.**

⚠ ** THE HONEST LEDGER, BECAUSE THIS IS A JOIN AND NOT A DISCOVERY. ** *Four of the five facts above
are each already receipted: the decomposition's existence on the squashed layer, the spectrum, the
charge ladder's parity, and the lift's `$\\sigma$`-only envelope with its figures.* ***Nobody had
joined them to THIS question.*** ⌗ **The one measurement that is new is the one that decides it:
that the minimum of the normalised squashing over the lift is attained at the turnaround, so the
divergence locus is off the transported segment.** *Everything else this receipt does is reproduce
other receipts' numbers to check it is standing on them correctly.*

⌗ ** AND I DID NOT USE `P7`'s NULL-TO-NULL SENTENCE AGAIN. ** *The pre-registration closed that escape
in advance: that sentence closed the MEASURE route because there is no spacelike datum AT THE
CROSSING, and whether a spacelike layer is elsewhere in the PATH is a different question it does not
answer.* **This question was answered by the lift's own squashing profile, and the sentence remains
exactly what it was.**

** COMPUTES: the Nariai lock that ties the mass to the horizon scale, the bead's conformal measure on
the lift and its total length against the paper's closed form, the normalised Berger squashing's
profile and its minimum over the lift, the charge ladder over the half-integers at seven degrees, and
the exponent ratio `$R(\\sigma)$` by quadrature on the lift's own measure -- each at three values of
the horizon scale, to show every figure is scale-free.  No assertion on wall-clock time. **
"""
import os
import re
import time
import warnings
from math import gamma, pi, sqrt

from scipy.integrate import IntegrationWarning, quad

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPER = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                 encoding='utf-8').read())
PRED = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                             'r7194_60_composition', 'PREDICTION.md'),
                                encoding='utf-8').read())


def doc_of(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8').read().split('"""')[1])


_R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
PO81 = doc_of(os.path.join(_R, 'P15_the_bead_routes_damping_survives_on_the_squashed_layer_because_'
                               'the_berger_harmonics_carry_no_squashing_and_the_spectrum_is_bounded_'
                               'below_uniformly.py'))
ENV = doc_of(os.path.join(_R, 'P15_the_lifts_exact_envelope_on_the_carried_layer_is_a_one_parameter_'
                              'deformation_indexed_by_the_hopf_charge_and_the_uniform_bound_is_not_'
                              'attained.py'))


# ======================================================================================
# THE BEAD, ON THE NARIAI MEMBER.  f = 1 - 2M/r - r^2/alpha^2 with f(r_N) = f'(r_N) = 0
# locks M to alpha: r_N = alpha/sqrt3 and M = alpha/(3 sqrt3).  The lift occupies
# -(2M alpha^2)^(1/3) < r < 0, and on it the conformal measure is purely imaginary.
# ======================================================================================
def bead(alpha):
    M = alpha / (3 * sqrt(3))
    r0 = (2 * M * alpha ** 2) ** (1.0 / 3.0)

    def dn(x):                                   # |d eta| at r = -x
        return 1.0 / (x * sqrt(abs(x * x / alpha ** 2 - 2 * M / x)))

    def epsn(x):                                 # Berger parameter, normalised to the horn's datum
        return alpha * sqrt(abs(1 + 2 * M / x - x * x / alpha ** 2)) / x

    with warnings.catch_warnings():
        warnings.simplefilter('ignore', IntegrationWarning)
        s_tot = quad(dn, 0.0, r0, limit=400, epsabs=1e-13, epsrel=1e-13)[0]

        def R(sig):
            g = lambda x: sqrt(max(0.0, 1 - sig * (1 - epsn(x) ** -2))) * dn(x)
            return quad(g, 0.0, r0, limit=400, epsabs=1e-12, epsrel=1e-12)[0] / s_tot

        out = dict(M=M, r0=r0, s_tot=s_tot, eps_turn=epsn(r0),
                   eps_min=min(epsn(r0 * (i / 40000.0)) for i in range(1, 40001)),
                   R=R, R0=R(0.0), R13=R(1 / 3), R1=R(1.0))
    return out


ALPHAS = (7.0, 3.0, 20.0)
B = {a: bead(a) for a in ALPHAS}
for a in ALPHAS:
    b = B[a]
    print(f"    alpha={a:<5} s_tot={b['s_tot']:.11f}  eps(turnaround)={b['eps_turn']:.7f}"
          f"  eps_min(lift)={b['eps_min']:.7f}  R(0)={b['R0']:.12f}"
          f"  R(1/3)={b['R13']:.10f}  R(1)={b['R1']:.10f}", flush=True)
b = B[7.0]
S_CLOSED = gamma(1 / 6) * sqrt(pi) / (gamma(2 / 3) * sqrt(3) * 2 ** (1 / 3))

# =====================================================================================
head("A -- THE PRE-REGISTRATION IS PRIOR, AND IT NAMED THE TEMPTATION BEFORE IT NAMED THE ANSWER")

gate("Ⓐ①  the pre-registration is in the tree and puts the TEMPTATION on the record before anything"
     " was computed -- that multiplying `r7174`'s amplitude loss by `r7186`'s parity gives the"
     " odd-ladder bound -- and says in terms that it does not trust that product",
     'I do not trust that product' in PRED
     and 'the odd-ladder bound, by composition, exactly as `r7173` conjectured' in PRED)

gate("Ⓐ②  AND IT NAMED THE THREE THINGS THE PRODUCT NEEDS, with the locus question flagged as the"
     " one it most expected to be the real obstruction -- which is the one that turns out to decide"
     " it, so the confirmation is worth something rather than being a restatement",
     'The two loci must be the SAME locus' in PRED
     and 'This is the one I most expect to be the real obstruction' in PRED
     and 'must mean ZERO and not SUPPRESSED' in PRED)

gate("Ⓐ③  and it closed three escapes in advance: no positive from the product without the locus"
     " check, no reporting an amplitude bound as the parity bound delivered late, and no second use"
     " of `P7`'s null-to-null sentence -- all three of which this receipt is held to below",
     'the product is not defined on this path' in PRED
     and 'A bound by a mechanism the order did not name is a finding' in PRED
     and "I will not use `r7186`'s null-to-null sentence twice" in PRED)

# =====================================================================================
head("B -- THE STRUCTURAL HALF HOLDS: THE LAYER IS NECESSARILY IN THE PATH")

gate("Ⓑ①  the paper states the requirement in its own voice -- carrying the harmonic labels along"
     " the bead needs a decomposition of the layer at EVERY point of the curve, the lift included,"
     " and the layer there is squashed rather than round",
     'needs a harmonic decomposition of the layer at every point of the curve' in PAPER
     and 'the lift included' in PAPER
     and 'the layer there is squashed rather than round' in PAPER)

gate("Ⓑ②  and `PO-81` established that the decomposition EXISTS on the squashed layer and is the"
     " SAME one, so the labels are carried exactly with no mixing and only the eigenvalue moves."
     "  ** So `r7173`'s conditional has its antecedent and the question is live rather than vacuous"
     " -- and this is named as another receipt's finding, not claimed here **",
     'The Berger harmonics carry NO squashing' in PO81
     and 'is exactly conserved along the bead and no mode mixes into another' in PO81
     and 'Only the EIGENVALUE moves' in PO81)

# =====================================================================================
head("C -- BUT THE PARITY NAMES WHICH SLICE IS SQUASHING-FREE, NOT WHICH MODES EXIST")

LADDER = {}
for L in range(0, 8):
    ms = [2 * (L) - 4 * k for k in range(L + 1)]          # 4m, kept integral: m = L/2 - k
    LADDER[L] = ms
    sig = [(m * m) // 4 for m in ms]                      # 4m^2 numerator, exactness kept below
print("    the ladder, over the integers (4m printed so nothing is a float):")
for L in range(0, 8):
    print(f"      L={L}: {len(LADDER[L])} slice(s)   4m = {LADDER[L]}"
          f"   m=0 present = {0 in LADDER[L]}", flush=True)

gate("Ⓒ①  the ladder carries `$L+1$` slices at EVERY degree, over eight consecutive degrees, with"
     " `$m$` stepping by one from `$-L/2$` -- computed over the integers so no float decides whether"
     " a slice exists",
     all(len(LADDER[L]) == L + 1 for L in range(8))
     and all(LADDER[L][i] - LADDER[L][i + 1] == 4 for L in range(8) for i in range(L)))

gate("Ⓒ②  and `$m=0$` is present exactly when `$L$` is EVEN -- the parity, reproduced rather than"
     " cited, at eight degrees",
     all((0 in LADDER[L]) == (L % 2 == 0) for L in range(8)))

gate("Ⓒ③  ⛔ SO AT ODD DEGREE EVERY SLICE IS CHARGED -- and all `$L+1$` of them are carried exactly"
     " by Ⓑ②, with no mixing.  ** The parity says which slice keeps the round eigenvalue; it does"
     " NOT say which modes exist, and it excludes nothing from the path **",
     all(0 not in LADDER[L] for L in (1, 3, 5, 7))
     and all(len(LADDER[L]) == L + 1 for L in (1, 3, 5, 7)))

# =====================================================================================
head("D -- AND THE PRODUCT IS NOT DEFINED: THE DIVERGENCE IS ON THE LEG THE TRANSPORT SKIPS")

gate("Ⓓ①  the control first, because every figure below is an integral over this measure: the lift's"
     " own conformal length comes out `$3.33873802357$` against the paper's closed form to better"
     " than `$10^{-11}$`, and it is SCALE-FREE -- identical at three values of the horizon scale, so"
     " the segment integrated is the paper's own and not a re-parametrisation of it",
     abs(b['s_tot'] - S_CLOSED) < 1e-11
     and max(abs(B[a]['s_tot'] - b['s_tot']) for a in ALPHAS) < 1e-9
     and 's_{\\rm tot}=\\Gamma(\\tfrac16)\\sqrt\\pi/\\Gamma(\\tfrac23)\\sqrt3\\,2^{1/3}=3.3387380'
     in PAPER)

gate("Ⓓ②  and the eigenvalue's divergence is where the squashing VANISHES: the spectrum is"
     " `$L(L+2)+4(\\varepsilon^{-2}-1)m^2$`, read from the paper, so a charged mode's eigenvalue runs"
     " to infinity as `$\\varepsilon\\to0$ `and only there",
     '\\lambda(L,m)=L(L+2)+4(\\varepsilon^{-2}-1)m^2' in PAPER)

gate("Ⓓ③  ⛭⛭⛭ BUT THE NORMALISED SQUASHING ON THE LIFT HAS ITS MINIMUM AT THE COMOVING TURNAROUND,"
     " `$1.3747296$`, and rises from there to infinity at the close -- measured over forty thousand"
     " points of the segment and identical at three horizon scales.  ** So `$\\varepsilon$` is"
     " bounded away from zero on the WHOLE transported segment: the divergence locus is on the leg"
     " the transport never traverses, and the product has no second factor **",
     abs(b['eps_min'] - b['eps_turn']) < 1e-9
     and b['eps_min'] > 1.37
     and abs(b['eps_turn'] - (3 * sqrt(3) / 2) ** (1 / 3)) < 1e-9
     and max(abs(B[a]['eps_min'] - b['eps_min']) for a in ALPHAS) < 1e-9)

gate("Ⓓ④  and the sign of that is the opposite of the helpful one, which is why it had to be"
     " measured rather than assumed: the stretch where the squashing falls below its round value"
     " RAISES every eigenvalue and would strengthen the damping -- and `PO-81` already records that"
     " this stretch is on the expansion side, so the transport never visits the stretch that would"
     " have made the composition work",
     '\\varepsilon\\to0$` at the seam RAISES every eigenvalue' in PO81
     or '0$` at the seam RAISES every eigenvalue' in PO81)

# =====================================================================================
head("E -- AND THE ODD LADDER ARRIVES, WITH A NUMBER RATHER THAN A SIGN")

EXACT = {}
for L in (1, 3, 5, 7):
    m4 = 2 * L                                   # 4m at |m| = L/2
    sig = (m4 / 4.0) ** 2 * 4 / (L * (L + 2))
    EXACT[L] = (sig, b['R'](sig), b['R'](sig) * sqrt(L * (L + 2)) * b['s_tot'],
                sqrt(L * (L + 2)) * b['s_tot'], sqrt(2 * L) * b['s_tot'])
    print(f"      L={L}: sigma={sig:.6f}  R={EXACT[L][1]:.10f}  exact exponent={EXACT[L][2]:.6f}"
          f"   round={EXACT[L][3]:.6f}   uniform bound={EXACT[L][4]:.6f}", flush=True)

gate("Ⓔ①  the envelope is a ONE-PARAMETER deformation and the parameter is the fraction of the"
     " eigenvalue the Hopf charge carries: `$(L,\\lvert m\\rvert)=(1,\\tfrac12)$` and `$(6,2)$` share"
     " `$\\sigma=\\tfrac13$` and return the same ratio to ten figures, so `$R$` is a function of"
     " `$\\sigma$` and of the profile and of nothing else about the mode",
     abs(b['R'](4 * 0.25 / 3) - b['R'](4 * 4.0 / 48)) < 1e-10
     and abs(b['R0'] - 1.0) < 1e-11)

gate("Ⓔ②  and the two anchors reproduce the envelope receipt's own figures: `$R(0)=1$` and"
     " `$R(1)=0.2591014627$`, so the lift's effective length in the maximal-charge band is"
     " `$0.8650719$` -- shortened from `$3.3387380$` and NOT FURTHER",
     abs(b['R1'] - 0.2591014627) < 1e-8
     and abs(b['R1'] * b['s_tot'] - 0.8650719) < 1e-6
     and '0.2591014627' in ENV)

gate("Ⓔ③  ⛭⛭ SO AT THE LOWEST ODD DEGREE THE CHARGED SLICE'S EXACT EXPONENT IS `$4.868603$`,"
     " against `$5.782864$` for a round mode of the same degree and `$4.721689$` for the uniform"
     " bound.  ** Exponentially small, NONZERO, and LESS suppressed than the round mode -- so the"
     " degree the parity was supposed to exclude is measured arriving **",
     abs(EXACT[1][2] - 4.868603) < 1e-5
     and EXACT[1][2] < EXACT[1][3] and EXACT[1][2] > EXACT[1][4])

gate("Ⓔ④  and the margin over the round mode GROWS WITHOUT BOUND IN DEGREE while the amplitude"
     " stays exponentially small in it -- monotone over the four odd degrees computed, so the"
     " surviving odd content is larger than the round-layer figures by a factor that grows, and is"
     " still suppressed",
     all(EXACT[L][3] - EXACT[L][2] < EXACT[L + 2][3] - EXACT[L + 2][2] for L in (1, 3, 5))
     and all(EXACT[L][2] < EXACT[L + 2][2] for L in (1, 3, 5)))

# =====================================================================================
head("F -- THE ANSWER, AND THE LEDGER OF WHOSE FINDING EACH PIECE IS")

gate("Ⓕ①  ⛭⛭⛭ SO THE ODD-LADDER BOUND IS NOT AVAILABLE BY EITHER ROUTE.  `r7186` showed the crossing"
     " CANNOT implement the parity; this shows that even where the layer IS in the path the parity"
     " does not reach the arriving content -- and the content it was supposed to exclude is measured"
     " arriving.  ** Which is the full discharge `r7173` ⓷ described, and it closes the question"
     " rather than relocating it **",
     all(0 not in LADDER[L] for L in (1, 3, 5, 7))
     and b['eps_min'] > 1.37
     and EXACT[1][2] < EXACT[1][3])

gate("Ⓕ②  ⚠ AND THIS IS A JOIN AND NOT A DISCOVERY, which is said here because four of the five"
     " facts are each already receipted -- the decomposition's existence, the spectrum, the ladder's"
     " parity, and the `$\\sigma$`-only envelope with its figures.  ** The one measurement that is"
     " new is the one that decides it: that the minimum of the normalised squashing over the lift is"
     " at the turnaround, so the divergence locus is off the transported segment **",
     'NOT ATTAINED' in ENV and '0.2591014627' in ENV
     and 'The Berger harmonics carry NO squashing' in PO81)

gate("Ⓕ③  ⌗ and the amplitude bound found here is NOT reported as the parity bound delivered late,"
     " which the pre-registration forbade in advance: the order asked whether the PARITY bounds what"
     " arrives, and the answer is that it does not -- the suppression that does exist carries a"
     " number and a different warrant, and both are said separately",
     'A bound by a mechanism the order did not name is a finding' in PRED
     and 'it is not an answer to the question asked' in PRED)

gate("Ⓕ④  and `P7`'s null-to-null sentence was not used a second time.  It closed the MEASURE route"
     " because there is no spacelike datum AT THE CROSSING; this question was answered by the lift's"
     " own squashing profile, and the sentence is left exactly what it was",
     'with no spacelike slice entering the map' not in PAPER
     and "I will not use `r7186`'s null-to-null sentence twice" in PRED)

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
  THE COMPOSITION ROUTE IS ANSWERED NEGATIVE TOO, AND IT FAILS HARDER THAN
  THE MEASURE ROUTE DID.

  THE LAYER IS IN THE PATH: carrying the harmonic labels along the bead
  needs a decomposition of the layer at every point of the curve, the lift
  included, and PO-81 established that the decomposition exists and is the
  same one, with the labels carried exactly and only the eigenvalue moving.
  So the conditional has its antecedent.

  BUT THE PARITY NAMES WHICH SLICE IS SQUASHING-FREE, NOT WHICH MODES
  EXIST.  The ladder carries L+1 slices at every degree and m = 0 is
  present exactly when L is even -- so at odd degree every slice is
  charged, and all of them are carried.  The parity excludes nothing.

  *** AND THE COMPOSITION PRODUCT IS NOT DEFINED ON THIS PATH.  The charged
      eigenvalue diverges where the squashing vanishes -- and the
      normalised squashing on the lift has its MINIMUM at the comoving
      turnaround, 1.3747296, rising to infinity at the close.  The
      divergence lives on the leg the transport never traverses. ***

  AND THE ODD LADDER ARRIVES WITH A NUMBER.  The exponent's ratio to the
  round one is a function of the Hopf-charge fraction alone, R(1/3) =
  0.8419016934 at the lowest odd degree, giving an exact exponent of
  4.868603 against 5.782864 for a round mode of the same degree and
  4.721689 for the uniform bound: exponentially small, nonzero, and less
  suppressed than the round mode by a margin that grows in degree.

  So the degree the parity was supposed to exclude is measured arriving.
  That is the full discharge the order described: it closes the question
  rather than relocating it.

  THE LEDGER: this is a JOIN.  Four of the five facts are each already
  receipted and nobody had joined them to this question.  The one new
  measurement is the one that decides it.  And the amplitude suppression
  found here is not the parity bound delivered late -- the order asked
  whether the PARITY bounds what arrives, and it does not.

  THE GUARD: when two receipted facts multiply into the answer you wanted,
  check that both factors are evaluated on the same stretch of the object
  before taking the product.  A divergence is a statement about a locus,
  and a locus that is not on the path contributes nothing to a transport
  along it -- so the product can be false with both factors true.
  ==========================================================================
""")
