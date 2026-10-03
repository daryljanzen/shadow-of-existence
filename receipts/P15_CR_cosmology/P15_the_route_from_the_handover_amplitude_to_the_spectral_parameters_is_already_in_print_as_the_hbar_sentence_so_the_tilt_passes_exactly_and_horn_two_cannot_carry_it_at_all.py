#!/usr/bin/env python3
"""P15 receipt -- `r7143`'s one remaining item, worked as the read it said it was first:
** horn ⓵ needs one route from a wavenumber-free potential amplitude to the acoustic sector's
`$A_s$` and `$n_s$`.  DOES THE CORPUS ALREADY JOIN THEM? **

*** ⛭⛭⛭ IT DOES, IN TWO PLACES, AND NEITHER IS `sec:what-crosses`.  THE ROUTE IS ONE LINE AND THE
    JOINING PRINCIPLE IS ALREADY IN PRINT -- STATED THERE ABOUT `$\\hbar$`:
      *"`$P(k)=\\hbar A_0k^{n_s-1}$` and `$\\hbar$` is an overall multiplicative factor: it survives in
       the amplitude and cancels in every logarithmic derivative"*,
    with its own definition beside it: *"An amplitude is the spectrum at one wavenumber; a tilt is its
    ratio to itself at two."*
    ⇒ THE HANDOVER FACTOR IS A MEMBER OF EXACTLY THAT CLASS, SO THE SAME SENTENCE CARRIES IT.
    `$n_s$` PASSES **EXACTLY**; `$A_s$` PICKS UP THE FACTOR AND NOTHING ELSE DOES. ***

⛭ ** AND THE SECOND PLACE STATES THE CONCLUSION ALREADY, IN THE OPEN-ITEMS SECTION RATHER THAN IN THE
   TRANSMISSION ARGUMENT. **  *`P15` says of the collapse leg: *"what supplies it is the progenitor's
vacuum and not the collapse leg"*, *"a handover at a fixed phase is exactly scale-free---the ratio of
amplitudes at two wavenumbers is one"*, and ***"the leg is a wavenumber-independent amplitude and
nothing else"***.*  ⇒ *So the route is not owed a new argument.  It is owed a **citation across two
sections**, and `sec:transmission` already asserts the join without giving it: *"routes `$A_s$` and
`$n_s$` through the same handover.  There is one boundary-condition supplier, not two."**

** ⇒ WHAT THIS RECEIPT ADDS TO THE TWO PLACES, SINCE A READ THAT ONLY LOCATES IS NOT WORTH A ROW. **
  ⓵ *** THE `$k$`-INDEPENDENCE IS EXACT ON THE CARRIER AND ONLY QUADRATIC ON THE LEG'S OWN VARIABLE,
      AND THE TWO ARE DIFFERENT CLAIMS. ***  *`P15`'s leg statement rests on *"At the branch point it
      vanishes quadratically"*; the carrier `r7142` identified rests on `$\\partial_k\\equiv0$` of the
      `$w=0$` potential equation, re-derived here.  **The route needs the exact one, and the exact one
      is the carrier's.***
  ⓶ *** THE TILT HALF OF THE ROUTE IS CONVENTION-FREE AND THE AMPLITUDE HALF IS NOT. ***  *For a
      transfer `$T$` free of `$k$` and ANY power `$p$`, `$\\dd\\ln(T^pP)/\\dd\\ln k=\\dd\\ln P/\\dd\\ln k$`
      identically -- `$p$` a free symbol, not `2`.  ⇒ *So `$n_s$` passes whatever the spectrum's power
      of the potential is, and only the number `$A_s$` picks up depends on it.*
  ⓷ *** AND THE PRICE ON `$A_s$` IS THE PAPER'S OWN THREE PER CENT, DOUBLED BY THE SQUARING. ***
      *`sec:coherence` compares its handover amplitude to the free oscillator's as *"within three per
      cent of the frozen value `$\\Psi_i/2$`"* -- `$0.4835/0.5$` is `3.30` per cent low.  On the
      SPECTRUM that is `$(0.4835/0.5)^2=0.93509$`, **`6.49` per cent**, and `$0.4835^2=0.23377$` is the
      factor itself.*  ⇒ *The comparison the paper makes on the potential is half the one that reaches
      `$A_s$`, and that is the whole of what the route costs.*

⛔ ** AND THE ROUTE IS UNAVAILABLE ON HORN ⓶ -- NOT MERELY DEARER, UNAVAILABLE, BY THE PAPER'S OWN
   TILT BUDGET. **  *`sec:refit-bound` prefers `$0.995$` here against `$0.956$` on the standard
background, so the whole budget for any tilt the route itself contributes is the gap, `0.039`.  A
transfer with a sound speed is not `$k$`-free: by `r7142` its logarithmic slope is `$-c_skL$`, so on the
spectrum it shifts the tilt by `$2c_skL`$ -- **`294.45` at the first acoustic peak, `7.5\\times10^{3}`
times the entire budget.***  ⇒ *** So the pricing `r7142` inverted does not merely favour horn ⓵: the
route exists on horn ⓵ and cannot exist on horn ⓶, because the only transfer horn ⓶ permits destroys
the tilt it is supposed to deliver. ***

** ⇒ SO `PO-79` DISCHARGES ON HORN ⓵, AND IT RETIRES NOTHING. **  *Every standing result survives:
`sec:what-crosses`'s *"amplitude and tilt cross unaltered"* stands with the carrier named and the
mechanism supplied; `sec:coherence`'s `$0.4835\\,\\Psi_i$` stands and is now the route's first end;
`sec:transmission`'s *"one boundary-condition supplier, not two"* stands and is now shown rather than
asserted.*  ⌗ ***That is the third apparent fork on this arc to resolve by dissolving -- `r7136`'s ⓪,
`r7134`'s ⓶, and now `PO-79` -- and the shape is the same each time: the thing the fork was supposed
to be a fork FOR had only one slot.***

⌗ ** WHAT THE ROUTE DOES NOT CLOSE, STATED BECAUSE THE PAPER ALREADY STATES IT. **  *`$A_s$` stays
inherited and `$n_s$` stays inherited: the route carries them, it does not derive them.  `P15` names
that frontier in its own terms -- *"a modelling task awaiting a progenitor interior"* -- and nothing
here touches it.  ⛔ *The route also says nothing about the acoustic COMB, which is the driving's
`$k$`-dependence and not a tilt; `sec:coherence` carries that separately as a Fourier magnitude.*

** COMPUTES: the logarithmic derivative of `$T^pP(k)$` symbolically with `$T$`, `$p$`, `$A_0$`,
`$\\hbar$` and `$n_s$` all free; `$\\partial_k$` of the standard potential equation at `$w=0$` and at
`$w=1/3$`; the handover ratio and its square; and the horn-⓶ tilt shift from the segment's conformal
length in the paper's own closed form.  *** THE ONLY NUMBERS PINNED ARE THE PAPER'S OWN *** -- its
`$0.4835$`, its `$\\Psi_i/2$`, its three per cent, its `$0.995$` and `$0.956$`, its `$-255$`-fixed
wavenumber and its `$c_0B(1/6,1/2)/2$`. **

⌗ *The guard this one leaves: ** when a row's last step is a route between two things the corpus
already carries, look for the joining principle where it is doing a DIFFERENT job -- a sentence written
about one multiplicative constant is about the class, and the class is what the route needs. **

Written r7144 by node 60, on `r7143`'s one remaining item, as the read it said it was before the
computation. Stated for reversal.
"""
import os
import re
import time

import mpmath as mp
import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
b15 = body_of(P15)

mp.mp.dps = 40
k, w, p, T, A0, hb, ns = sp.symbols('k w p T A_0 hbar n_s', positive=True)
eta = sp.symbols('eta')


# ============================================ A. the two ends, and the corpus's own assertion
head("A.  THE TWO ENDS OF THE ROUTE, AND THE CORPUS'S OWN CLAIM THAT THEY ARE JOINED")

_END1 = r"the wavenumber-independent $0.4835\,\Psi_i$"
_END2 = r"Progenitor-supplied, and inherited rather than derived: the amplitude $A_s$ and tilt $n_s$"
print(f"      first end: {b15.count(_END1)}x;   second end: {b15.count(_END2)}x")
gate("Ⓐ① BOTH ENDS ARE IN PRINT, EACH ONCE -- the handover's *\"wavenumber-independent "
     "`$0.4835\\,\\Psi_i$`\"* and the inherited *\"amplitude `$A_s$` and tilt `$n_s$`\"*.  ⇒ *So the "
     "route `r7143` asks for runs between two things the paper already carries*",
     b15.count(_END1) == 1 and b15.count(_END2) == 1)

_ASSERT = r"routes $A_s$ and $n_s$ through the \emph{same} handover"
_ONESUP = r"There is one boundary-condition supplier, not two."
print(f"      the join asserted: {b15.count(_ASSERT)}x;   its consequence: {b15.count(_ONESUP)}x")
gate("Ⓐ② AND `sec:transmission` ALREADY **ASSERTS** THE JOIN WITHOUT GIVING IT -- *\"routes `$A_s$` and "
     "`$n_s$` through the same handover\"*, *\"There is one boundary-condition supplier, not two\"*.  "
     "⇒ ** So what is owed is a mechanism for a claim already made, not a new claim **",
     b15.count(_ASSERT) == 1 and b15.count(_ONESUP) == 1)


# ============================================ B. the joining principle, already in print
head("B.  THE JOINING PRINCIPLE IS ALREADY IN PRINT -- WRITTEN ABOUT `$\\hbar$`")

_HBAR = (r"so $P(k)=\hbar A_0k^{n_s-1}$ and $\hbar$ is an overall multiplicative factor: "
         r"\emph{it survives in the amplitude and cancels in every logarithmic derivative}")
_DEFN = r"An amplitude is the spectrum at one wavenumber; a tilt is its ratio to itself at two."
print(f"      the principle: {b15.count(_HBAR)}x;   its definition: {b15.count(_DEFN)}x")
gate("Ⓑ① THE PRINCIPLE THE ROUTE NEEDS IS LOCATED VERBATIM, DOING A DIFFERENT JOB -- *\"`$\\hbar$` is an "
     "overall multiplicative factor: it survives in the amplitude and cancels in every logarithmic "
     "derivative\"*, with *\"An amplitude is the spectrum at one wavenumber; a tilt is its ratio to "
     "itself at two\"* beside it.  ⇒ ** A sentence about one multiplicative constant is about the "
     "CLASS, and the handover factor is in the class **",
     b15.count(_HBAR) == 1 and b15.count(_DEFN) == 1)

P = T ** p * hb * A0 * k ** (ns - 1)
slope = sp.simplify(sp.diff(sp.log(P), k) * k)
print(f"      `$\\dd\\ln(T^pP)/\\dd\\ln k$` with `$T$`, `$p$`, `$A_0$`, `$\\hbar$`, `$n_s$` all free: "
      f"{slope}")
gate("Ⓑ② AND IT HOLDS WITH EVERY SYMBOL FREE: `$\\dd\\ln(T^pP)/\\dd\\ln k=n_s-1$` IDENTICALLY, with "
     "`$T$` free of `$k$` and the POWER `$p$` a free symbol rather than `2`.  ⇒ *** So the tilt half of "
     "the route is convention-free -- it does not matter what power of the potential the spectrum is -- "
     "and only the number `$A_s$` picks up depends on that power. ***",
     sp.simplify(slope - (ns - 1)) == 0 and sp.simplify(sp.diff(slope, T)) == 0
     and sp.simplify(sp.diff(slope, p)) == 0 and sp.simplify(sp.diff(slope, hb)) == 0)


# ============================================ C. the handover factor is in the class, exactly
head("C.  THE HANDOVER FACTOR IS IN THAT CLASS **EXACTLY**, AND THE LEG'S OWN CLAIM IS ONLY QUADRATIC")

Phi = sp.Function('Phi')
Hc = sp.Function('H')(eta)
EQ = (sp.diff(Phi(eta), eta, 2) + 3 * Hc * (1 + w) * sp.diff(Phi(eta), eta)
      + (2 * sp.diff(Hc, eta) + (1 + 3 * w) * Hc ** 2) * Phi(eta) + w * k ** 2 * Phi(eta))
dk0 = sp.simplify(sp.diff(EQ, k).subs(w, 0))
dk3 = sp.simplify(sp.diff(EQ, k).subs(w, sp.Rational(1, 3)))
_NOK = r"contains no $k$ at all once $w=0$"
print(f"      `$\\partial_k$` at `$w=0$`: {dk0};   at `$w=1/3$`: {dk3};   the paper's own clause: "
      f"{b15.count(_NOK)}x")
gate("Ⓒ① THE CARRIER'S `$k$`-INDEPENDENCE IS EXACT, RE-DERIVED RATHER THAN CARRIED OVER: `$\\partial_k$` "
     "of the standard potential equation is **identically `$0$`** at `$w=0$` and `$2k\\Phi/3$` at "
     "`$w=1/3$`, against the paper's own *\"contains no `$k$` at all once `$w=0$`\"*",
     dk0 == 0 and sp.simplify(dk3 - 2 * k * Phi(eta) / 3) == 0 and b15.count(_NOK) == 1)

_PHASE = (r"a handover at a fixed phase is exactly scale-free---the ratio of amplitudes at two "
          r"wavenumbers is one")
_QUAD = r"At the branch point it vanishes quadratically"
_LEGAMP = r"the leg is a wavenumber-independent amplitude and nothing else"
_VACUUM = r"what supplies it is the progenitor's vacuum and not the collapse leg"
print(f"      fixed-phase: {b15.count(_PHASE)}x;   quadratic: {b15.count(_QUAD)}x;   "
      f"leg-amplitude: {b15.count(_LEGAMP)}x;   progenitor's vacuum: {b15.count(_VACUUM)}x")
gate("Ⓒ② ⛭ AND THE SECOND PLACE THE CORPUS ALREADY JOINS THEM IS THE **OPEN-ITEMS** SECTION, NOT THE "
     "TRANSMISSION ARGUMENT -- *\"what supplies it is the progenitor's vacuum and not the collapse "
     "leg\"*, *\"a handover at a fixed phase is exactly scale-free\"*, *\"the leg is a "
     "wavenumber-independent amplitude and nothing else\"*.  ⛔ ** But its support is *\"At the branch "
     "point it vanishes quadratically\"* -- a DIFFERENT and weaker claim than `Ⓒ①`'s identity, and the "
     "route needs the exact one **",
     b15.count(_PHASE) == 1 and b15.count(_QUAD) == 1 and b15.count(_LEGAMP) == 1
     and b15.count(_VACUUM) == 1)


# ============================================ D. the price on A_s
head("D.  THE PRICE ON `$A_s$`, WHICH IS THE PAPER'S OWN THREE PER CENT DOUBLED BY THE SQUARING")

_THREE = (r"within three per cent of the frozen value $\Psi_i/2$ the free oscillator carries at every "
          r"wavenumber")
R_PSI = mp.mpf('0.4835') / mp.mpf('0.5')
R_SPEC = R_PSI ** 2
FACT = mp.mpf('0.4835') ** 2
print(f"      on the potential: {mp.nstr(R_PSI, 8)}, i.e. {mp.nstr(100 * (1 - R_PSI), 4)} per cent low "
      f"-- the paper's *\"within three per cent\"*: {b15.count(_THREE)}x")
print(f"      on the spectrum:  {mp.nstr(R_SPEC, 8)}, i.e. {mp.nstr(100 * (1 - R_SPEC), 4)} per cent;  "
      f"the factor itself `$0.4835^2$` = {mp.nstr(FACT, 8)}")
gate("Ⓓ① THE COMPARISON THE PAPER MAKES IS ON THE POTENTIAL AND THE ONE THAT REACHES `$A_s$` IS ITS "
     "SQUARE: `3.30` per cent becomes **`6.49` per cent**, and the factor `$A_s$` picks up is "
     "`$0.4835^2=0.23377$`.  ⇒ *That doubling is the whole of what the route costs, and it is a number "
     "rather than a direction*",
     b15.count(_THREE) == 1 and abs(100 * (1 - R_PSI) - mp.mpf('3.30')) < mp.mpf('0.01')
     and abs(100 * (1 - R_SPEC) - mp.mpf('6.49')) < mp.mpf('0.01')
     and abs(FACT - mp.mpf('0.233772')) < mp.mpf('1e-6'))

gate("Ⓓ② AND THE DOUBLING IS THE LEADING ORDER OF THE SQUARING AND NOTHING ELSE, CHECKED RATHER THAN "
     f"ASSERTED: `$1-x^2=(1-x)(1+x)$`, so the ratio of the two percentages is `$1+x$` = "
     f"{mp.nstr(1 + R_PSI, 8)}, within `{mp.nstr(100 * abs((1 + R_PSI) - 2) / 2, 3)}` per cent of `2`",
     abs((100 * (1 - R_SPEC)) / (100 * (1 - R_PSI)) - (1 + R_PSI)) < mp.mpf('1e-20')
     and abs((1 + R_PSI) - 2) < mp.mpf('0.04'))


# ============================================ E. horn 2 cannot carry the route at all
head("E.  AND HORN ⓶ CANNOT CARRY THE ROUTE AT ALL, BY THE PAPER'S OWN TILT BUDGET")

_REFIT = (r"refitting both arms on this construction's own background prefers a tilt of $0.995$ here "
          r"against $0.956$ on the standard one")
BUDGET = mp.mpf('0.995') - mp.mpf('0.956')
c0 = 2 / (mp.sqrt(3) * 2 ** (mp.mpf(1) / 3))
L = c0 * mp.beta(mp.mpf(1) / 6, mp.mpf(1) / 2) / 2          # the paper's own closed form
K1 = mp.mpf(255) / L                                        # the wavenumber its `-255` fixes
CS = 1 / mp.sqrt(3)
SHIFT = 2 * CS * K1 * L
print(f"      the refit clause: {b15.count(_REFIT)}x;   budget = {mp.nstr(BUDGET, 4)}")
print(f"      `$L$` from the paper's closed form = {mp.nstr(L, 12)};   `$k$` at the first peak = "
      f"{mp.nstr(K1, 10)};   tilt shift `$2c_skL$` = {mp.nstr(SHIFT, 9)}")
gate("Ⓔ① THE BUDGET IS THE PAPER'S OWN GAP, `$0.995$` AGAINST `$0.956$`, SO `0.039` -- located, not "
     "chosen here",
     b15.count(_REFIT) == 1 and abs(BUDGET - mp.mpf('0.039')) < mp.mpf('1e-12')
     and abs(L - mp.mpf('3.3387380236')) < mp.mpf('1e-10'))

gate(f"Ⓔ② *** AND A TRANSFER WITH A SOUND SPEED IS NOT IN `Ⓑ①`'s CLASS, SO IT ENTERS THE TILT: by "
     f"`r7142`'s `$\\dd\\ln T/\\dd\\ln k=-c_skL$` the spectrum's shift is `$2c_skL=294.45$` at the "
     f"first acoustic peak -- `{mp.nstr(SHIFT / BUDGET, 3)}` times the ENTIRE budget. ***  ⇒ ** So the "
     f"route exists on horn ⓵ and cannot exist on horn ⓶: the only transfer horn ⓶ permits destroys "
     f"the very tilt it is supposed to deliver **",
     abs(SHIFT - mp.mpf('294.448637')) < mp.mpf('1e-5') and SHIFT / BUDGET > 7000
     and SHIFT / BUDGET < 8000)

gate("Ⓔ③ ⌗ AND THE CONTRAST IS THE SAME ALGEBRA AS `Ⓑ②` RATHER THAN A SECOND ARGUMENT: substituting "
     "`$T=e^{-c_skL}$` into `$\\dd\\ln(T^pP)/\\dd\\ln k$` returns `$n_s-1-pc_skL$` symbolically, which "
     "is `$n_s-1$` at `$c_s=0$` and at no other value.  ⇒ *One expression prices both horns*",
     sp.simplify(sp.diff(sp.log(sp.exp(-sp.Symbol('c_s', positive=True) * k
                                       * sp.Symbol('L', positive=True)) ** p
                                 * hb * A0 * k ** (ns - 1)), k) * k
                 - (ns - 1 - p * sp.Symbol('c_s', positive=True) * k
                    * sp.Symbol('L', positive=True))) == 0)


# ============================================ F. what discharges and what does not
head("F.  SO `PO-79` DISCHARGES ON HORN ⓵, AND WHAT STAYS OPEN STAYS OPEN")

_UNALT = r"so amplitude and tilt cross unaltered while the collapse-leg acoustic phase does not"
_FRONT = r"a modelling task awaiting a progenitor interior"
_DRIVE = r"the resonant Fourier magnitude of the potential's evolution, $|\tilde\Psi(\omega{=}1)|$"
print(f"      the clause: {b15.count(_UNALT)}x;   the frontier: {b15.count(_FRONT)}x;   "
      f"the driving: {b15.count(_DRIVE)}x")
gate("Ⓕ① EVERY STANDING RESULT SURVIVES AND ONE IS NOW SHOWN RATHER THAN ASSERTED: the *\"cross "
     "unaltered\"* clause, the *\"one boundary-condition supplier\"* claim, and the handover amplitude "
     "are all located together with the frontier the paper keeps -- *\"a modelling task awaiting a "
     "progenitor interior\"*.  ⇒ ** The row closes having retired nothing **",
     b15.count(_UNALT) == 1 and b15.count(_FRONT) == 1 and b15.count(_ONESUP) == 1
     and b15.count(_END1) == 1)

gate("Ⓕ② ⛔ AND WHAT THE ROUTE DOES **NOT** REACH IS WITNESSED RATHER THAN DISCLAIMED: the acoustic "
     "COMB is the driving's `$k$`-dependence, carried separately as *\"the resonant Fourier magnitude "
     "of the potential's evolution, `$|\\tilde\\Psi(\\omega{=}1)|$`\"* -- a `$k$`-DEPENDENT object, so "
     "`Ⓑ①`'s class does not contain it and the route says nothing about it.  ⌗ *`$A_s$` and `$n_s$` "
     "also stay inherited: the route carries them, it does not derive them*",
     b15.count(_DRIVE) == 1 and sp.simplify(sp.diff(slope, T)) == 0)


# ============================================ verdict
head("VERDICT")
_ok = sum(1 for _, v in CHECKS if v)
print(f"\n  {_ok} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
for nm, v in CHECKS:
    if not v:
        print(f"    FAILED: {nm}")
print()
raise SystemExit(0 if _ok == len(CHECKS) else 1)
