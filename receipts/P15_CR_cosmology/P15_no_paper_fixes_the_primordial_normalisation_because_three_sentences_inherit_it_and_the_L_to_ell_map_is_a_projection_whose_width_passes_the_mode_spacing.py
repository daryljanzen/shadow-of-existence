#!/usr/bin/env python3
"""P15 receipt -- `r7163`'s TWO ORDERS, both taken in one revision because both are dependencies of
the same narrowed row:
** ⓵ WHERE IS THE PROGENITOR'S ANISOTROPIC AMPLITUDE AT THE LIFT'S ENTRY FIXED, IF ANYWHERE?
   ⓶ AND WHAT DOES `sec:largescale`'s `$L\\to\\ell$` MAP RETURN ON THE LIFT'S OWN DEGREES? **

*** ⛭⛭⛭ ⓵ NO PAPER FIXES IT, AND THE CORPUS SAYS SO IN ITS OWN VOICE THREE TIMES RATHER THAN BY
    OMISSION -- WHICH IS THE OUTCOME `r7163` BET ON, WITH ONE ADDITION IT DID NOT ASK FOR:
      ⓐ `P16` carries the apparatus and declares the normalisation INHERITED: the input is
         *"a fully specified input, available from standard cosmology, and not an idealisation to be
         chosen"*, *"the mode content is the part of the primordial sector this construction inherits
         rather than derives"*, and in the one place it scores an amplitude, *"The amplitude is fitted
         in closed form in both cases"*.
      ⓑ `P15` says the same in its own voice: *"Progenitor-supplied, and inherited rather than
         derived: the amplitude `$A_s$` and tilt `$n_s$`"*.
      ⓒ And the count that establishes it: `$A_s$` occurs `21` times in `P15` and **zero** times in
         `P16` and `P14`; `P14` has `anisotrop` **zero** times; `P16`'s single `normalisation` is the
         Euclidean action's GRAVITATIONAL normalisation and not a spectrum's.
    ⇒ *** AND THE ADDITION: THE CORPUS DOES FIX THE AMPLITUDE'S PROPAGATION EVEN THOUGH IT DOES NOT
        FIX ITS VALUE.  `P16` computes the density contrast peaking *"where matter domination ends, at
        `$\\sim10^{-6}$`"* with *"The peak value is independent of the composition"* -- linear in the
        inherited `$\\zeta$`.  So the missing scalar is ONE number and the chain from it is built. ***

*** ⛭⛭⛭ ⓶ AND THE MAP IS A PROJECTION, NOT A RELABELLING -- ONE-TO-ONE FOR THE FIRST TWO DEGREES AND
    SMEARING FROM THE THIRD UP, WITH `eq:lowell`'s VALUE NOT ITS CENTRE:
      ⓐ `$\\sum_\\ell(2\\ell+1)j_\\ell(x)^2=1$` EXACTLY, so `$w_\\ell(L)=(2\\ell+1)j_\\ell(k_LD_C)^2$` is a
         distribution over `$\\ell$` and the question is well posed rather than rhetorical.
      ⓑ `eq:lowell` returns the ARGUMENT `$k_LD_C$`, which sits near that distribution's **ninetieth
         percentile**, not its centre: `$4.78$` against a mode at `$\\ell=3$`, `$7.81$` against `$6$`,
         `$10.70$` against `$8$`, `$13.53$` against `$11$`.
      ⓒ THE WIDTH CROSSES THE SPACING AT `$L=3$`: standard deviations `$1.20$`, `$1.82$`, `$2.44$`,
         `$3.06$`, `$3.68$`, `$4.30$`, `$4.92$`, `$5.54$` against a mean spacing of `$2.2$`--`$2.4$`.
      ⓓ So below it the map is quasi-injective and above it each `$\\ell$` draws on several degrees,
         the overlap growing linearly without bound.
    ⇒ *** AN ENVELOPE EXPONENTIAL IN `$L$` IS THEREFORE NOT AN ENVELOPE EXPONENTIAL IN `$\\ell$` ABOVE
        `$L=3$`: the sum at fixed `$\\ell$` is dominated by the LOWEST contributing degree, because the
        envelope falls steeply in `$L$`.  Below `$L=3$` the relabelling reading is safe. *** ***

⛭⛭ ** ⓵ THE READ, AND WHY ITS NEGATIVE IS NOT AN INFERENCE FROM SILENCE. **  *`r7163` asked for a
statement about the CORPUS rather than about `P16`, and said a negative would be a result if it came
with the count that establishes it.  It does.  Three sentences in two papers assign the normalisation
to inherited data, in the papers' own words, and the term that would carry it (`$A_s$`) appears
nowhere in either paper that would have to supply it.*  ⇒ ** A corpus that names the quantity
twenty-one times in the paper that USES it and zero times in the two that would have to PRODUCE it
has located it outside itself, not mislaid it. **

⌗ ** AND `P14` IS RULED OUT THE SAME WAY `r7122` RULED IT OUT, re-measured here: ** *`anisotrop`
appears zero times; its `31` occurrences of `turnaround` are the turnaround-MASS row's and not the
comoving turnaround, with the two words co-occurring in a single sentence.*

⛭ ** AND THE PRECEDENT FOR WHAT KIND OF DATUM THIS IS, WHICH IS THE PAPER'S OWN. **  *`sec:intro`
already carries one: flat `$\\Lambda$`CDM *"carries the baryon-to-photon ratio `$\\eta$` as a measured
datum from a baryogenesis it does not model"*, and this cosmology carries the same `$\\eta$`.*  ⇒ *So
an inherited primordial normalisation is the same KIND of object the paper already carries without
owing a derivation for it -- which bears on `r7163`'s termination condition: the normalisation does not
live in another paper of this corpus, so the row neither closes here nor MOVES; what it becomes is a
dependency on a measured datum.*  ⌗ **That is this seat's reading and the classification is node 66's.**

⛭⛭⛭ ** ⓶ THE MAP, EVALUATED RATHER THAN QUOTED -- AND THE FINDING GOES FIRST. **  *`r7163` said that
if the map turns out to be a different object from what either of us assumed, that is a finding and it
goes above the evaluation.  It is.*  ⇒ *** `eq:lowell` is the PEAK ARGUMENT of a projection and not the
projection's centre.  Because `$\\sum_\\ell(2\\ell+1)j_\\ell^2=1$`, each source degree carries a genuine
distribution over `$\\ell$`, and `$k_LD_C$` sits near its ninetieth percentile: the probability below
`$\\ell_L$` measures `$0.879$`, `$0.890$`, `$0.911$`, `$0.930$` for `$L=1..4$`. ***  ⌗ *The paper's
`$\\simeq$` is therefore carrying an offset of order the mode spacing itself at the degrees that matter,
which is a fact about the sign of a correction rather than about its size.*

⌗ ** AND THE LOW-`$\\ell$` LEAK IS SMALL WHERE THE FLOOR ARGUMENT NEEDS IT TO BE. **  *The quadrupole
source puts `$P(\\ell\\le3)=0.150$` of its weight below `$\\ell=3$`, the `$L=3$` mode `$0.058$` and the
`$L=4$` mode `$0.033$`.*  ⇒ *So the deficit below `$\\ell_2$` is not a hard edge, and it is not undone
either: the leak is a sixth of one mode's weight and falls fast with degree.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **  *⓵ is a READ: it computes no physics and postulates none,
and its arithmetic is word counts and one co-occurrence.*  ⛔ *It does NOT claim the normalisation is
unobtainable -- only that no paper of this corpus fixes it, which is what was asked.*  ⛔ *⓶ computes
the projection KERNEL's distribution over `$\\ell$` and not a `$C_\\ell$`: the weights `$w_L$` that
multiply each kernel are the primordial power and the transfer, which this receipt does not supply, so
no spectrum is predicted and no figure of `sec:lowl` is re-derived.*  ⛔ *The `$D_C$` and `$r_0$` it
uses are the PAPER's printed values, taken as given rather than re-derived from the background.*  ⛔ *It
does not re-open the guard: `$L$` is the layer degree and `$\\ell$` the observable multipole, and the
whole point of ⓶ is that the two are related by a projection.*  ⛔ *It proposes no paper edit and
classifies no row.*

** COMPUTES: term counts over four paper bodies with comment lines stripped, the located sentences
matched against the CURRENT sources, and `P14`'s turnaround/mass co-occurrence; then the stretch factor
from the paper's own two lengths, `eq:lowell` on `$L=1..8$` with its spacings, the completeness identity
for the projection kernel, and that kernel's distribution over `$\\ell$` -- mean, median, mode, standard
deviation, `$P(\\ell\\le3)$` and `$P(\\ell\\le\\ell_L)$` -- with the width compared against the spacing
degree by degree.  *** THE ONLY PAPER QUANTITIES PINNED ARE THE FIVE INHERITANCE SENTENCES, THE
`$\\eta$` PRECEDENT, `eq:lowell` AND ITS TWO PRINTED NUMBERS. *** **

⌗ *The guard this one leaves: ** when a paper writes `$X\\simeq g(L)$` for a projected label, ask what
percentile of the projection `$g$` is before reading it as a relabelling -- a formula that locates a
distribution's edge and one that locates its centre look identical on the page. **

Written r7164 by node 60, on `r7163`'s two orders.
Stated for reversal.
"""
import os
import re
import time

import mpmath as mp

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
    src = open(path, encoding='utf-8', errors='replace').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
C = lambda n: os.path.join(ROOT, 'corpus', n)
P15 = body_of(C('CR_cosmology.tex'))
P16 = body_of(C('cosmogenesis_paper.tex'))
P14 = body_of(C('matter_sector_paper.tex'))
P07 = body_of(C('CR_framework.tex'))

# ------------------------------------------------------------------ Ⓐ the read
head("Ⓐ  ORDER ⓵ -- WHERE A PRIMORDIAL ANISOTROPIC NORMALISATION IS FIXED, IF ANYWHERE")

_SPEC = "a fully specified input, available from standard cosmology, and not an idealisation to be chosen"
_INH = "the mode content is the part of the primordial sector this construction inherits rather than derives"
_FIT = "The amplitude is fitted in closed form in both cases"
_P15INH = "Progenitor-supplied, and inherited rather than derived: the amplitude $A_s$ and tilt $n_s$"
_ETA = "carries the baryon-to-photon ratio $\\eta$ as a measured datum from a baryogenesis it does not model"
_DELTA = "then peaks where matter domination ends, at $\\sim10^{-6}$"
_COMP = "The peak value is independent of the composition"

gate("Ⓐ①  P16 calls the input fully specified and available from STANDARD COSMOLOGY, not chosen",
     P16.count(_SPEC) == 1)
gate("Ⓐ②  P16 says in its own voice that the mode content is INHERITED rather than derived",
     P16.count(_INH) == 1)
gate("Ⓐ③  and in the one place P16 scores an amplitude it is FITTED, not derived",
     P16.count(_FIT) == 1)
gate("Ⓐ④  P15 says the same of A_s and n_s: progenitor-supplied, inherited rather than derived",
     P15.count(_P15INH) == 1)

counts = {'P15 A_s': P15.count('A_s'), 'P16 A_s': P16.count('A_s'), 'P14 A_s': P14.count('A_s'),
          'P14 anisotrop': P14.count('anisotrop'), 'P15 anisotrop': P15.count('anisotrop'),
          'P16 normalisation': P16.count('normalisation')}
print("\n    the counts that establish the negative:")
for k, v in counts.items():
    print(f"      {k:<20} {v}")
gate("Ⓐ⑤  A_s appears 21 times in the paper that USES it and ZERO times in the two that would have"
     " to produce it -- the negative is located, not inferred from silence",
     counts['P15 A_s'] == 21 and counts['P16 A_s'] == 0 and counts['P14 A_s'] == 0)
gate("Ⓐ⑥  P14 is not a candidate: `anisotrop` ZERO times, against 8 in P15 -- the control that the"
     " instrument works",
     counts['P14 anisotrop'] == 0 and counts['P15 anisotrop'] == 8)
_NSENT = [s for s in re.split(r'(?<=\.)\s', P16) if 'normalisation' in s]
_SPECTRAL = ('amplitude', 'spectrum', 'spectral', 'A_s', 'primordial', 'tilt')
print(f"\n    P16's one `normalisation` sentence names an action: "
      f"{bool(_NSENT) and 'action' in _NSENT[0]};  "
      f"spectral words in it: {[w for w in _SPECTRAL if _NSENT and w in _NSENT[0]]}")
gate("Ⓐ⑦  P16's single `normalisation` sits in a sentence about an ACTION and carries NONE of the"
     " words that would make it a spectrum's -- read off the sentence's subject rather than pinned"
     " to its wording, so a rewording that keeps the meaning keeps the gate",
     counts['P16 normalisation'] == 1
     and len(_NSENT) == 1
     and 'action' in _NSENT[0]
     and not any(w in _NSENT[0] for w in _SPECTRAL))
tm = len(re.findall(r'turnaround[^.]{0,60}mass|mass[^.]{0,60}turnaround', P14))
print(f"\n    P14 'turnaround' occurrences: {P14.count('turnaround')}, "
      f"co-occurring with 'mass' in {tm} sentence(s)")
gate("Ⓐ⑧  and P14's turnarounds are the turnaround-MASS row's rather than the comoving turnaround",
     P14.count('turnaround') == 31 and tm >= 1)

gate("Ⓐ⑨  but the corpus DOES fix the amplitude's propagation: P16 computes the contrast peaking at"
     " 1e-6 where matter domination ends, composition-independent",
     P16.count(_DELTA) == 1 and P16.count(_COMP) == 1)
gate("Ⓐ⑩  and the paper supplies its own precedent for an inherited measured datum, the eta analogy",
     P15.count(_ETA) == 1)

# ------------------------------------------------------------------ Ⓑ the map
head("Ⓑ  ORDER ⓶ -- sec:largescale's L→ℓ MAP, EVALUATED ON THE LIFT'S OWN DEGREES")

_LOWELL = r"\ell_L\simeq\sqrt{L(L+2)}\;\frac{D_C}{r_0}"
_STRETCH = "The stretch factor $D_C/r_0\\approx2.76$"
_FLOOR = "carries the lowest mode to $\\ell_2\\approx7.8$, with no source below it"
gate("Ⓑ①  eq:lowell is in print in the form this receipt evaluates", P15.count(_LOWELL) == 1)
gate("Ⓑ②  and so are the two printed numbers it is evaluated with",
     P15.count(_STRETCH) == 1 and P15.count(_FLOOR) == 2)

mp.mp.dps = 25
DC = mp.mpf('1.395e4')          # the paper's printed comoving distance to last scattering, Mpc
R0 = mp.mpf(5051)               # the paper's printed present S^3 areal radius, Mpc
STRETCH = DC / R0
print(f"\n    stretch D_C/r_0 = {mp.nstr(STRETCH, 8)}   against the paper's printed 2.76")
gate("Ⓑ③  the stretch factor from the paper's own two lengths reproduces its printed 2.76",
     abs(STRETCH - mp.mpf('2.76')) < mp.mpf('0.01'))

ell_of = lambda L: mp.sqrt(L * (L + 2)) * STRETCH
jl = lambda l, x: mp.sqrt(mp.pi / (2 * x)) * mp.besselj(l + mp.mpf('0.5'), x)

tot1 = mp.nsum(lambda l: (2 * l + 1) * jl(int(l), ell_of(2))**2, [0, 250])
gate("Ⓑ④  Σ_ℓ (2ℓ+1) j_ℓ(x)² = 1 exactly, so the kernel IS a distribution over ℓ and the question"
     " 'one-to-one or smearing' is well posed",
     abs(tot1 - 1) < mp.mpf('1e-12'))

NMAX = 220
rows = []
print("\n     L   eq:lowell   mode   median   mean     sd    P(ℓ≤3)   P(ℓ≤ℓ_L)")
for L in range(1, 9):
    x = ell_of(L)
    W = [(2 * l + 1) * jl(l, x)**2 for l in range(NMAX)]
    s = sum(W)
    W = [w / s for w in W]
    m1 = sum(l * W[l] for l in range(NMAX))
    sd = mp.sqrt(sum(l * l * W[l] for l in range(NMAX)) - m1**2)
    c, med = 0, 0
    for l in range(NMAX):
        c += W[l]
        if c >= mp.mpf('0.5'):
            med = l
            break
    mode = W.index(max(W))
    p3 = sum(W[l] for l in range(4))
    pL = sum(W[l] for l in range(int(mp.floor(x)) + 1))
    rows.append((L, x, mode, med, m1, sd, p3, pL))
    print(f"    {L:>2}   {mp.nstr(x,6):>8}   {mode:>4}   {med:>5}   {mp.nstr(m1,5):>6}"
          f"  {mp.nstr(sd,4):>5}   {mp.nstr(p3,4):>7}   {mp.nstr(pL,4):>7}")

exc = [r[1] - r[2] for r in rows]
print("\n    eq:lowell minus the mode, by degree: "
      + "  ".join(mp.nstr(e, 4) for e in exc))
gate("Ⓑ⑤  eq:lowell's value is ABOVE the distribution's mode at every degree, by 1.70 to 2.93 "
     "-- a displacement of order one whole mode, bounded both ways and not growing with degree",
     all(mp.mpf('1.69') < e < mp.mpf('2.93') for e in exc)
     and max(exc) - min(exc) < mp.mpf('1.3'))
gate("Ⓑ⑥  it sits near the NINETIETH PERCENTILE rather than the centre: P(ℓ≤ℓ_L) is 0.88 to 0.96",
     all(mp.mpf('0.87') < pL < mp.mpf('0.97') for (L, x, mode, med, m1, sd, p3, pL) in rows))

means = [r[4] for r in rows]
spac = [means[i + 1] - means[i] for i in range(len(means) - 1)]
sds = [r[5] for r in rows]
print(f"\n    mean spacing between consecutive degrees: {mp.nstr(min(spac),4)} to {mp.nstr(max(spac),4)}")
print("    sd / spacing by degree:",
      "  ".join(mp.nstr(sds[i] / spac[min(i, len(spac) - 1)], 3) for i in range(len(sds))))
gate("Ⓑ⑦  the spacing is 2.2 to 2.4 while the width runs 1.20 to 5.54, so the width CROSSES the"
     " spacing at L = 3 and grows past it without bound",
     sds[0] < spac[0] and sds[1] < spac[1] and sds[2] > spac[2]
     and sds[-1] / spac[-1] > 2)
gate("Ⓑ⑧  so the map is quasi-injective for the first two degrees and smears from the third up --"
     " a projection and not a relabelling",
     sds[0] / spac[0] < mp.mpf('0.6') and sds[2] / spac[2] > 1)
gate("Ⓑ⑨  and the low-ℓ leak falls fast with degree: P(ℓ≤3) = 0.60, 0.15, 0.058, 0.033 for L = 1..4,"
     " so the floor below ℓ_2 is softened by a sixth of one mode and not erased",
     abs(rows[1][6] - mp.mpf('0.150')) < mp.mpf('0.01')
     and rows[3][6] < mp.mpf('0.04') and rows[0][6] > mp.mpf('0.55'))

# ------------------------------------------------------------------ Ⓒ the consequence
head("Ⓒ  WHAT THAT DOES TO AN ENVELOPE EXPONENTIAL IN THE LAYER DEGREE")

print("\n    r7162's maximal-charge exponents, and the degrees that reach a given ℓ:")
for L in range(1, 7):
    x = ell_of(L)
    W = [(2 * l + 1) * jl(l, x)**2 for l in range(NMAX)]
    s = sum(W)
    reach = [l for l in range(NMAX) if W[l] / s > mp.mpf('0.02')]
    print(f"      L={L}  ℓ_L={mp.nstr(x,6):>8}   ℓ with >2% of this degree's weight:"
          f" {min(reach)}..{max(reach)}")
bands = []
for L in range(1, 7):
    x = ell_of(L)
    W = [(2 * l + 1) * jl(l, x)**2 for l in range(NMAX)]
    s = sum(W)
    bands.append({l for l in range(NMAX) if W[l] / s > mp.mpf('0.02')})
overlaps = [len(bands[i] & bands[i + 1]) for i in range(len(bands) - 1)]
print(f"    overlap in those bands between consecutive degrees: {overlaps}")
gate("Ⓒ①  consecutive degrees' 2%-bands OVERLAP from the third degree up, so a fixed ℓ draws on"
     " several layer degrees at once",
     overlaps[2] > 0 and overlaps[-1] >= overlaps[2])
gate("Ⓒ②  hence an envelope exponential in L is NOT exponential in ℓ above L = 3, while the"
     " relabelling reading is safe for the first two degrees",
     sds[2] > spac[2] and sds[0] < spac[0])

# ------------------------------------------------------------------ verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
if bad:
    print("\n  FAILED:")
    for n in bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""
  ==========================================================================
  VERDICT, ORDER (1): NO paper of this corpus fixes the progenitor's
  anisotropic normalisation, and the corpus says so in its own voice three
  times rather than by omission -- with A_s named 21 times in the paper that
  uses it and zero times in the two that would have to produce it.  What the
  corpus DOES fix is the amplitude's propagation: the contrast peaks at 1e-6
  where matter domination ends, composition-independent and linear in the
  inherited datum.  So the missing scalar is one number, the chain from it is
  built, and the paper's own eta precedent says what KIND of datum that is.

  VERDICT, ORDER (2): the map is a PROJECTION and not a relabelling.
  eq:lowell returns the kernel's peak ARGUMENT, which sits near the
  distribution's ninetieth percentile rather than its centre -- above the
  mode by 1.70 to 2.93 at the degrees that matter.  The width crosses the mode
  spacing at L = 3 and grows past it without bound, so the map is
  quasi-injective for the first two degrees and smears above them.
  *** An envelope exponential in L is therefore not an envelope exponential
      in ell above L = 3; below it the relabelling reading is safe. ***
  ==========================================================================
""")
