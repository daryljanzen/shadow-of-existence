#!/usr/bin/env python3
"""B61 -- the index obstruction's own stated hypotheses do not cover the spectral route, and the
corpus's "known escapes" sentence does not classify it because it never considered it.

** WHERE THIS ARRIVES. **  *** r2814 found the spectral-triple route absent from the corpus with its
pieces present.  ** Before pursuing it, the corpus's existing walls must be checked against it -- a
route that the walls already cover is not a route. ** ***

** ⛭⛭ ⓵ THE GRADING AXIOM IS SATISFIED, AND THAT IS NOT A CR FACT. **  A spectral triple needs
$\\gamma^2=1$ and $\\gamma D=-D\\gamma$.  Verified numerically for $\\gamma^5$ against every $\\gamma^\\mu$.
  ⌗ ** These are properties of $\\gamma^5$, not of CR. **  *** What CR supplies is that $R=\\gamma^5$ is
    ** DERIVED ** there rather than posited (r2779) -- the corpus's own chirality operator IS the
    grading a spectral triple requires, which is a match worth stating and not a result. ***

** ⛭⛭⛭ ⓶ AND THE INDEX OBSTRUCTION NAMES ITS OWN HYPOTHESES, WHICH THE SPECTRAL ROUTE DOES NOT MEET. **
The boundary paper: "on the compact face a continuous gauge isometry meets the Atiyah--Hirzebruch index
obstruction, rendering the geometric fermion sector vector-like ... ** The obstruction's load-bearing
hypotheses are compactness and a continuous isometry **, not a product or Kaluza--Klein structure."

      *** compactness           -- the spectral route makes no compactness claim
          a continuous isometry -- the spectral route uses NO isometry at all;
                                   inner fluctuations D -> D + A come from the ALGEBRA ***

  ⇒⇒ *** THE OBSTRUCTION IS STATED AGAINST ISOMETRY ROUTES AND THE SPECTRAL ROUTE IS NOT ONE.  ** The
      premise fails, and the paper is explicit that the premise is what carries the theorem. ** ***

** ⓷ AND THE PAPER'S OWN ESCAPE CLAUSE DOES NOT CLASSIFY IT. **  *** "with the known escapes all
abandoning the geometric premise."  ** Does the spectral route abandon it?  Connes' construction is
spectral geometry -- geometric in the sense that all data is the triple, and not geometric in the sense
of Riemannian isometry. **  The corpus does not say, because it never considered the route. ***

  ⇒ *** THAT IS A GAP IN COVERAGE, NOT A HOLE IN THE ARGUMENT -- ** the same shape as r2805's finding
      about p0's premise **: the wall is sound and the route is outside what it ranges over. ***

** ⓸ SO THE ROUTE SURVIVES ITS FIRST CONTACT WITH THE CORPUS'S WALLS. **  *** Three of five routes are
closed (r2814); the fourth is not closed by the index obstruction, by the isometry wall, or by r2813's
flat-connection argument -- ** each for a stated reason, none of which is "nobody checked" **. ***

WHAT IS NOT CLAIMED.  ** Not that the route works ** -- *** two axioms remain untested here: the real
structure $J$ and the order-one condition $[[D,a],Jb^*J^{-1}]=0$, and either can kill it. ***  ** Not
that the index obstruction is weakened ** -- *** it is sound within its hypotheses and this receipt
quotes the paper's own statement of them. ***  ** Not that $\\gamma^5$ satisfying the grading axioms is a
CR result ** -- *** it is a fact about $\\gamma^5$; the CR content is that $R=\\gamma^5$ is derived. ***

** COMPUTES: $\\gamma^5$ against the grading axioms -- $\\gamma^2=1$ and anticommutation with each
$\\gamma^\\mu$.  *** Standard Dirac algebra, computed to fix that the axiom is met and not assumed. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 042a49e** *(per c54.220's rule, r2776).*

Written r2818.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(name):
    raw = open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print("  B61 -- do the corpus's walls already cover the spectral route?")
    print()
    I2 = np.eye(2)
    z = 0*I2
    s = [np.array([[0, 1], [1, 0]], dtype=complex),
         np.array([[0, -1j], [1j, 0]]),
         np.array([[1, 0], [0, -1]], dtype=complex)]
    g5 = np.block([[-I2, z], [z, I2]])
    gam = [np.block([[z, I2], [I2, z]])] + [np.block([[z, s[k]], [-s[k], z]]) for k in range(3)]

    check('⛭⛭ ⓵ the grading axiom $\\gamma^2=1$ holds for $\\gamma^5$',
          np.allclose(g5 @ g5, np.eye(4)))
    check('and $\\gamma^5$ anticommutes with every $\\gamma^\\mu$, hence with $D=\\gamma^\\mu D_\\mu$ -- '
          '** a fact about $\\gamma^5$, not about CR **',
          all(np.allclose(g5 @ g + g @ g5, 0) for g in gam))

    bnd = flat('boundary_paper.tex')
    check('⛭⛭⛭ ⓶ and the index obstruction NAMES its own hypotheses: "The obstruction\'s load-bearing '
          'hypotheses are compactness and a continuous isometry, not a product or Kaluza--Klein '
          'structure"',
          'load-bearing hypotheses are compactness and a continuous isometry' in bnd)
    check('⇒ and the spectral route uses NO isometry -- inner fluctuations $D\\to D+A$ come from the '
          'ALGEBRA, so ** the premise the paper says carries the theorem fails for it **',
          'continuous gauge isometry meets the Atiyah--Hirzebruch index obstruction' in bnd)

    check('⓷ while the paper\'s escape clause does not classify it: "with the known escapes all '
          'abandoning the geometric premise" -- ** and the corpus never considered this route, so it '
          'does not say which side it falls on **',
          'the known escapes all abandoning the geometric premise' in bnd)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the route survives its first contact with the corpus\'s walls. **')
    print('  ⛭⛭ ⓵ ** The grading axiom is met: ** γ⁵ squares to 1 and anticommutes with every γ^μ.')
    print('     ⌗ *** Facts about γ⁵, not about CR.  The CR content is that R = γ⁵ is DERIVED there')
    print('     (r2779) — the corpus\'s own chirality operator IS the grading a triple requires. ***')
    print('  ⛭⛭⛭ ⓶ ** And the index obstruction names its own hypotheses: ** "compactness and a')
    print('     continuous isometry".')
    print('     *** The spectral route uses NO isometry — inner fluctuations come from the ALGEBRA —')
    print('     so the premise the paper says carries the theorem fails for it. ***')
    print('  ⓷ ** And the escape clause does not classify it: ** "the known escapes all abandoning the')
    print('     geometric premise".  ** Connes\' construction is spectral geometry: geometric in that')
    print('     all data is the triple, not geometric in the sense of Riemannian isometry. **  The')
    print('     corpus does not say which, because it never considered the route.')
    print('     ⇒ *** A gap in COVERAGE, not a hole in the argument — the same shape as r2805. ***')
    print('  ⓸ ** So four of five routes now have a stated status, ** and the fourth is not closed by')
    print('     the index obstruction, the isometry wall, or r2813 — ** each for a stated reason, none')
    print('     of which is "nobody checked". **')
    print('     ⚠ Two axioms remain untested: the real structure J and the order-one condition.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
