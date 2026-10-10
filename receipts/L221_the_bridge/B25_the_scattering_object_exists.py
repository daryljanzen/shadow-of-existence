#!/usr/bin/env python3
"""B25 -- `PO-11`'s missing OBJECT is one line from the corpus's own superpotential: $W=\\lambda\\sqrt f/r$
gives Regge--Wheeler partner potentials that vanish at BOTH horizons, so scattering states with continuum
normalisation are DEFINED on the static region.

** WHAT r2690 LEFT. **  The obstruction is uniform in $\\lambda$ -- no high-$j$ corner rescues the tower --
so what `PO-11` needs is "** not a better mode but a different OBJECT: a scattering state with a continuum
normalisation **".

** ⛭⛭ ⓵ AND THE CORPUS ALREADY HAS WHAT BUILDS ONE. **  `P14_B3_spinor_vielbein` derives, from the
explicit leaf tetrad and the Cartan structure equations, that "** the massless radial Dirac operator
carries superpotential $W=\\lambda\\sqrt f/r$ ** --- exactly P13's deferred equation".  *** A radial Dirac
operator with a superpotential is a SUSY-QM pair, and its partner potentials are
$V_\\pm=W^2\\pm dW/dx$ with $x$ the tortoise coordinate.  That is the Regge--Wheeler form, and at
`1971c67` --- the tree this receipt was written against, where its absence claims are pinned --- the
corpus had not written it. ***

** ⌗ AND IT HAS WRITTEN IT SINCE, WHICH IS THIS RECEIPT'S OBJECT ARRIVING IN THE PAPERS AND IS WHY ⓷
BELOW ASSERTS A PRESENCE RATHER THAN AN ABSENCE. **  `matter_sector_paper` (`P14`) carries
$W=\\lambda\\sqrt f/r$ with $V_\\pm=W^2\\pm\\dd W/\\dd x$ and both partner potentials decaying
exponentially in $r_*$, an ordinary short-range scattering problem with unitary transmission across the
tower --- written at `r3652`, nine hundred revisions after this receipt.  *So the live half of ⓷ is the
corpus's state now, and the historical absence stays pinned where it was measured.*

** ⛔ AND THE LIVE ABSENCE CHECK THIS REPLACES WAS KEYED ON A LABEL AND NOT ON THE OBJECT, WHICH IS WHY
IT PASSED FOR THREE AND A HALF THOUSAND REVISIONS WITH THE OBJECT IN THE CORPUS. **  It counted the
string `Regge`, and `P14` wrote the FORM without the NAME.  *** It finally fired at `r7167`, on a
sentence that used the words for an unrelated purpose --- so the one time it spoke, it was wrong about
both halves: the form was present, and the thing it had detected was a name. ***  ⌗ *An absence keyed
on what a thing is called cannot see the thing; and an absence with no presence assertion beside it
cannot tell a true absence from a search that misses.  Both are repaired below.*

** ⓶ COMPUTED, on the undercritical member $M=0.12$, $\\alpha=1$ (horizons $0.2570$, $0.8464$): **

      ***        r        f       W^2       V_+       V_-
           0.25697  0.00000   0.00005   0.01081  -0.01072      <- inner horizon
           0.40000  0.24000   1.50000   1.19381   1.80619
           0.60000  0.24000   0.66667   0.12234   1.21100
           0.84644  0.00000   0.00000  -0.00094   0.00094      <- outer horizon ***

  ⇒⇒ *** BOTH PARTNER POTENTIALS VANISH AT BOTH HORIZONS and are bounded between.  On the tortoise line
      that is a BARRIER OF COMPACT SUPPORT: plane-wave asymptotics exist at both ends, so scattering
      states are defined and carry the continuum normalisation `PO-11` asks for. ***

** ⓷ WHICH RELOCATES THE ROW'S DEBT. **  *** It is not "construct an object" -- the object is
constructible from a receipt already banked.  What is owed is the SPECTRUM: transmission and reflection
across that barrier, and whether the bound tower and the scattering continuum together are complete. ***
  ⌗ ** And that is the ordinary Regge--Wheeler problem on SdS, ** *** which has decades of literature --
    exactly the "M-L, standard but substantial" this line sized it at, now with its entry point
    identified. ***

WHAT IS NOT CLAIMED.  ** Not that the sector is built ** -- *** completeness of bound-plus-continuum is
the physics question and is untouched. ***  ** Not that $V_\\pm$ is derived here ** -- $W$ is the corpus's,
verified in `B3`; the SUSY-QM partner form is standard and is applied, not proved.  ** Not that the two
horizons make this a standard black-hole scattering problem ** -- *** the static region here is bounded by
a black-hole AND a cosmological horizon, which is the SdS case and differs from Schwarzschild in exactly
the way that makes both ends asymptotically flat in $x$. ***

** COMPUTES: the SUSY partner potentials V_pm = W^2 +- dW/dx at the undercritical member M=0.12,
alpha=1.  *** M and alpha are the corpuss own SdS parameters; nothing is imported. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 1971c67** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2714.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, AL, LAM = 0.12, 1.0, 1.0
RB, RC = 0.25696832, 0.84643915


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/AL**2


def W(r):
    return LAM*np.sqrt(max(f(r), 0.0))/r


def dWdx(r, h=1e-7):
    return f(r)*(W(r+h) - W(r-h))/(2*h)


def main():
    print()
    print("  B25 -- is a scattering state definable on the static region?")
    print()
    b3 = open(glob.glob(os.path.join(ROOT, 'receipts', '**', 'P14_B3_spinor_vielbein.py'),
                        recursive=True)[0], encoding='utf-8', errors='replace').read()

    check('⛭⛭ ⓵ the corpus derives the superpotential: "the massless radial Dirac operator carries '
          'superpotential W=lambda sqrt(f)/r -- exactly P13\'s deferred eq"',
          '1=(sqrt f/r)e), and shows\n  the massless radial Dirac operator carries superpotential W=lambda sqrt(f)/r' in b3)
    check('and notes it vanishes at every horizon: "W=0 at every horizon (f=0) and is ODD in signed r"',
          'W=0 at every horizon' in b3)

    # ⓶ the potentials vanish at both horizons
    for name, rh in (('inner', RB), ('outer', RC)):
        vp = W(rh+1e-6)**2 + dWdx(rh+1e-6) if rh == RB else W(rh-1e-6)**2 + dWdx(rh-1e-6)
        vm = W(rh+1e-6)**2 - dWdx(rh+1e-6) if rh == RB else W(rh-1e-6)**2 - dWdx(rh-1e-6)
        check(f'⓶ at the {name} horizon r={rh:.5f}: $V_+$={vp:+.5f}, $V_-$={vm:+.5f} -- both within '
              '0.02 of zero',
              abs(vp) < 0.02 and abs(vm) < 0.02)

    # bounded in between, and genuinely non-zero
    mid = [W(r)**2 + dWdx(r) for r in (0.4, 0.5, 0.6)]
    check(f'and bounded but NON-ZERO between: $V_+$ = {", ".join(f"{v:.3f}" for v in mid)} at '
          'r=0.4, 0.5, 0.6 -- so the check is not vacuous',
          max(abs(v) for v in mid) > 0.1 and max(abs(v) for v in mid) < 10)

    # ⓷ the corpus HAS written this form since -- a presence, keyed on the object and not on its name.
    #   The historical absence is pinned in the docstring at 1971c67 and is not re-measured here.
    #   r7168: this replaced a live count of the string `Regge` over all papers.  That count read ZERO
    #   for ~3,500 revisions while P14 carried the form itself, because P14 wrote the FORM without the
    #   NAME -- and it went red at r7167 on a P15 sentence using the words for an unrelated purpose.
    #   ** An absence keyed on a label cannot see the object, and an absence with no presence beside it
    #   cannot be told from a search that misses. **  So the live assertion is now a PRESENCE of the
    #   formula, which fails if P14's passage moves and cannot pass by a pattern going stale.
    def body(p):
        b = '\n'.join(l for l in open(p, encoding='utf-8', errors='replace').read().split('\n')
                      if not l.lstrip().startswith('%'))
        j = b.find('\\begin{thebibliography}')
        return b[:j] if j > 0 else b
    P14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    check('⓷ and the corpus HAS written this form since: P14 carries $W=\\lambda\\sqrt f/r$ with '
          '$V_\\pm=W^2\\pm dW/dx$',
          'W=\\lambda\\sqrt f/r$ and $V_{\\pm}=W^{2}\\pm\\dd W/\\dd x$' in P14)
    # ⌗ r7169: this asserted P14's `unitary transmission across the tower` beside the formula and the
    #   phrase is dropped.  ** It is prose that paper can reword without changing anything this receipt
    #   claims, and the formula beside it carries the same content. **  *Adding a fragile pin while
    #   repairing a fragile pin is the shape this revision is about.*
    check('and states the scattering consequence this receipt computed, as a formula and not as prose: '
          'both partner potentials $W^2\\pm dW/dr_*$',
          'both partner potentials $W^{2}\\pm\\dd W/\\dd r_{*}$' in P14)

    # and the NAME, measured where it now sits: the corpus locates the reduction and computes it nowhere
    tex = {os.path.basename(p): body(p)
           for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
           if not os.path.basename(p).startswith('appendix_receipts')}
    named = {k: len(re.findall(r'Regge', v)) for k, v in tex.items()}
    where = sorted(k for k, n in named.items() if n)
    p15 = re.sub(r'\s+', ' ', tex['CR_cosmology.tex'])
    m = re.search(r'Regge', p15)
    sent = p15[m.start():m.start() + 600] if m else ''
    check(f'and the NAME is in exactly one paper, {where}, where it LOCATES the reduction rather than '
          'computing it (the companion dynamics paper)',
          where == ['CR_cosmology.tex'] and sum(named.values()) == 1
          and 'companion dynamics paper' in sent)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the object PO-11 needs is one line from the corpus's own superpotential. **")
    print('  ⛭⛭ ⓵ ** `B3` derives W = λ√f/r from the explicit tetrad ** — and a radial Dirac operator')
    print('     with a superpotential is a SUSY-QM pair, whose partners are ** V_± = W² ± dW/dx ** on the')
    print('     tortoise line.  *** That is the Regge–Wheeler form, absent from the corpus at 1971c67,')
    print('     where this receipt pinned its absence — and WRITTEN INTO P14 at r3652, nine hundred')
    print('     revisions later, formula and scattering consequence both. ***')
    print('  ⓶ ** Computed: BOTH partners vanish at BOTH horizons ** and are bounded and non-zero')
    print('     between (V₊ ≈ 1.19, 0.50, 0.12 at r = 0.4, 0.5, 0.6).')
    print('     ⇒⇒ *** On the tortoise line that is a barrier with plane-wave asymptotics at both ends —')
    print('       so scattering states ARE defined, with the continuum normalisation PO-11 asks for. ***')
    print('  ⓷ ** So the debt relocated, and the papers have since taken up where it went: ** P14 states')
    print('     the ω≠0 problem as an ordinary short-range scattering problem, both partners decaying')
    print('     exponentially in r_* at the surface gravity, with unitary transmission across the tower.')
    print('     ⇒ ** What P14 names as still the undertaking is the quantised field, its mode')
    print('       completeness, and the join between the static continuum and the wall ** — a different')
    print('       object from this receipt\'s, carried where that paper carries it.')
    print('     ⌗ The entry point this receipt identified is therefore walked, not merely named.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
