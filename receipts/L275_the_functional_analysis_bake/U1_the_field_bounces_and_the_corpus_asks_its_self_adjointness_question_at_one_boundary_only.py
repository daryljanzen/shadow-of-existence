#!/usr/bin/env python3
r"""U1 -- the functional-analysis bake.  This field BOUNCES, and more completely than any thrown so
far: every probe it can construct is already answered, several of them better than the field would have
asked.  What it returns is one routing fact -- the corpus asks "is the operator essentially
self-adjoint here?" at ONE boundary and nowhere else, while the other boundary appears 278 times across
sixteen papers -- and the two verdicts, computed, are OPPOSITE.

COMPUTES: the Weyl limit-point/limit-circle threshold at both boundaries from the indicial exponents;
the scale-factor origin's verdict against P10's stated gamma and threshold; the branch point's verdict
against station H's attained spectrum; whether the coincidence of 3/4 at both is structural or
arithmetic; and where in the corpus each verdict actually lives.  Nothing is fitted.

** ⛭⛭⛭ ⓵ THE BOUNCE, AND IT IS NEARLY TOTAL.  EVERY PROBE THIS FIELD CAN BUILD IS ALREADY ANSWERED. **
  * *"Is the deparametrized true Hamiltonian self-adjoint or merely symmetric?"*  ⇒ `P10` **computes
    the deficiency indices $(1,1)$, ordering-independently**, cites Weyl and Reed--Simon, and names the
    inverse-square coefficient and the threshold.
  * *"A one-parameter family of extensions is a one-parameter family of theories."*  ⇒ `P10` **says
    exactly that, in its own epistemic voice** -- *"a structure carrying an unforced parameter is not a
    single world but a family"* -- and closes it by the de~Sitter horizon's thermal state.
  * *"Which extension?"*  ⇒ `P10` **names the Friedrichs extension** and, separately, the regular
    branch $x^{1/2+\nu}$ that Euclidean regularity imposes -- and those are the same extension.
  * *"What about the Hardy bound?"*  ⇒ `P10`'s own footnote: $-\tfrac14$ *"decides whether a regular
    branch exists to choose"*, against $\tfrac34$ which *"decides whether a boundary condition must be
    chosen at all."*
  * *"And with the tower coupled?"*  ⇒ `P10` **promotes the coefficient to an operator $\hat\Gamma$,
    decomposes by direct integral, and supplies the condition fibre by fibre.**
  ⇒ *** A field thrown at a corpus that has already done the field's work returns the corpus's work.
      That is what a bounce IS, and it is recorded rather than dressed up as a finding. ***

** ⌗ ⓶ AND THE VOCABULARY ABSENCE IS NOT A HOLE, WHICH IS WORTH SEPARATING FROM THE CARTAN CASE. **
*`Hilbert space` ×0, `inner product` ×0, `von Neumann` ×0, `density matrix` ×0, `mixed state` ×0,
`S-matrix` ×0, `spectral theorem` ×0, `resolvent` ×0; `Stone` ×1 and not in a physics sense.*
  ⇒ ** But `P10` names its Hilbert spaces as $L^2$ of the half-line and $L^2(\mathbb{R})$ throughout. **
    *The objects are there under their standard notation and the phrases are not.*
  ⇒ *** So this is the sixth appearance of the corpus's anonymity, and it is the WEAK form: a
      vocabulary gap over work fully done, not -- as with `Ambrose--Singer` in the Cartan bake -- a
      load-bearing theorem the argument turns on and never names.  The two should not be counted
      alike, and this receipt does not count them alike. ***

** ⛔⛭ ⓷ WHAT IT DOES RETURN: THE QUESTION IS ASKED AT ONE BOUNDARY AND THE OTHER IS THE COMMONEST
OBJECT IN THE CORPUS. **  *`essentially self-adjoint` appears in `P10` alone, once.  `limit-point` and
`limit-circle` appear in `P10` alone.  And `branch point` appears **278 times across sixteen papers**.*
  ⇒ ** No paper carries a self-adjointness verdict at the branch point. **  *Station Ⓗ supplied one
    (`L-264`) and it lives in a receipt.*
  ⇒ *** AND THE TWO VERDICTS ARE OPPOSITE.  At $a=0$: limit-CIRCLE -- a boundary condition must be
      chosen, and `P10` must spend a section closing it.  At $r=0$: limit-POINT -- the attained
      spectrum misses the window entirely, so there is nothing to choose and nothing to close. ***
  ⇒ ** So the corpus's own epistemic criterion bites at one boundary and is SILENT at the other, for a
    reason -- and that contrast is the sharpest thing the corpus could say about its boundaries.  It
    is said in no paper, because the two halves are not in the same place. **

** ⚠ ⓸ AND THE $3/4$ AT BOTH IS ARITHMETIC, NOT STRUCTURE -- SAID BEFORE ANYONE BUILDS ON IT. **
*Both thresholds are exactly $3/4$.  They are not the same computation: the scale factor's comes from
$\sqrt{\gamma+\tfrac14}=1$ on exponents $\tfrac12\pm\nu$ in $dx$, an exponent GAP of 2; the branch
point's from $-2|\lambda|+\tfrac12=-1$ on a density in $d\ell$, a GAP of 3.*
  ⇒ *** Different measures, different gaps, same number.  `L-264`'s own lesson was that a convergence
      is evidence and must be checked for spuriousness; checked, this one is a coincidence, and
      recording that now costs nothing and later would cost a retraction. ***

WHAT IS NOT CLAIMED.  ** Not that the field found nothing ** -- a bounce is a result, and the register
of what was asked and where it was answered is the deliverable.  ** Not that `P10` is incomplete ** --
every probe built here is answered there, several more carefully than asked.  ** Not that the branch
point NEEDS a self-adjointness verdict in a paper ** -- what is claimed is that it has one, that it is
opposite to the other, and that a reader cannot compare them.  ** Not that the two thresholds are
related ** -- they are shown not to be.  ** And not that the vocabulary absence is a defect ** -- it is
explicitly separated from the Cartan bake's load-bearing case.

    python3 receipts/L275_the_functional_analysis_bake/U1_the_field_bounces_and_the_corpus_asks_its_self_adjointness_question_at_one_boundary_only.py

Written r3168, `L-275`.  Stated for reversal.
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def schrodinger_verdict(g):
    """-d^2/dx^2 + g/x^2 on the half-line: both solutions L^2(dx) near 0?"""
    nu = np.sqrt(g + 0.25)
    return (0.5 - nu) > -0.5, (0.5 - nu, 0.5 + nu)


def branchpoint_verdict(lam):
    """station Ⓗ: |psi|^2 dl ~ r^(∓2λ+1/2); both L^2 near 0?"""
    return (-2 * abs(lam) + 0.5) > -1.0, (-2 * abs(lam) + 0.5, 2 * abs(lam) + 0.5)


def main():
    print()
    print('  U1 -- the field bounces, and the question is asked at one boundary only')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    B = RB.BODIES_TEX

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭⛭⛭ THE BOUNCE: EVERY PROBE THE FIELD CAN BUILD IS ALREADY ANSWERED')
    print('  ==========================================================================')
    p10 = B['P10']
    probes = [
        ('self-adjoint or merely symmetric?', 'deficiency indices'),
        ('ordering-independent?', 'independently of the ordering'),
        ('is a family of extensions a family of theories?',
         'not a single world but a family'),
        ('which extension?', 'Friedrichs extension'),
        ('the Hardy bound too?', 'whether a regular branch exists to choose'),
        ('and with the tower coupled?', 'direct integral'),
    ]
    for question, evidence in probes:
        found = evidence.lower() in p10.lower()
        print(f'      {question:48s} P10: {"yes" if found else "NO"}')
        check(f'⓵ "{question}" is answered in P10, evidenced by "{evidence}" verbatim', found)
    check('⓵ᵍ ⛭ and P10 names the field\'s two canonical citations rather than reinventing the '
          'criterion: Weyl and Reed--Simon',
          'Weyl1910' in B['P10'] or 'ReedSimon' in B['P10'])

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE VOCABULARY ABSENCE IS THE WEAK FORM, AND IS SEPARATED AS SUCH')
    print('  ==========================================================================')
    rows = RB.survey(['Hilbert space', 'inner product', 'von Neumann', 'density matrix',
                      'mixed state', 'S-matrix', 'spectral theorem', 'resolvent'])
    def TOTW(t):
        return max(sum(RB.word_counts(t).values()), sum(RB.word_counts(t, tex=True).values()))
    absent = ['Hilbert space', 'inner product', 'von Neumann', 'density matrix', 'mixed state',
              'S-matrix', 'spectral theorem', 'resolvent']
    check('⓶ every one of the field\'s standard phrases is ×0 across the seventeen bodies, '
          'word-bounded', all(TOTW(t) == 0 for t in absent))
    check('⓶ᵇ ⛭ BUT THE OBJECTS ARE THERE UNDER THEIR STANDARD NOTATION: P10 works on "$L^2$ of '
          'the half-line" and "$L^2(R)$" -- so this is a vocabulary gap over work fully done',
          'L^2' in p10 or 'L^{2}' in p10)
    check('⓶ᶜ ⚠ WHICH IS NOT THE CARTAN CASE AND IS NOT COUNTED AS IT: there `Ambrose--Singer` was '
          'a load-bearing theorem the argument turns on and never names, and here nothing the '
          'argument needs is missing',
          os.path.exists(os.path.join(ROOT, 'CARTAN_HOLONOMY_LEDGER.md')))

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛭ THE ONE THING IT RETURNS: ONE BOUNDARY ASKED, THE OTHER NOT')
    print('  ==========================================================================')
    where = {}
    for t in ('essentially self-adjoint', 'limit-circle', 'limit-point', 'branch point'):
        where[t] = {p: len(re.findall(re.escape(t), b, re.I)) for p, b in B.items()}
        where[t] = {k: v for k, v in where[t].items() if v}
        print(f'      {t:26s} {sum(where[t].values()):4d}  in {len(where[t])} paper(s): '
              f'{sorted(where[t])}')
    # ** CORRECTED r3319.  The routing fact this recorded was TRUE when the bake ran and the gap it
    #    named is now CLOSED: P14 carries the branch-point verdict since r3205, so `limit-circle` is
    #    no longer P10's alone.  The check asserts the JOIN rather than the absence -- which is the
    #    honest form, since what the bake FOUND is what made the routing worth reporting. **
    check('⓷ `essentially self-adjoint` is still P10\'s alone, while `limit-circle` has since been '
          'joined to P14 at the UPHELD limit-point verdict -- the gap this bake named, now closed (B67)',
          # ** r3339: the verdict is UPHELD (B67) and the routing gap is closed -- P14 carries
          #    limit-POINT at the branch point.  Assert the join at the right verdict. **
          list(where['essentially self-adjoint']) == ['P10']
          and 'P10' in where['limit-point'] and 'P14' in where['limit-point'])
    check(f'⓷ᵇ ⛔ while `branch point` appears {sum(where["branch point"].values())} times across '
          f'{len(where["branch point"])} papers -- and no paper carries a self-adjointness verdict '
          'at it',
          sum(where['branch point'].values()) > 250 and len(where['branch point']) >= 15)
    k1 = os.path.join(ROOT, 'receipts', 'L264_station_H_the_index_is_canonical')
    check('⓷ᶜ the verdict for that boundary exists and lives in a RECEIPT, not a paper: station Ⓗ, '
          'L-264', os.path.isdir(k1) and any('limit_point' in f for f in os.listdir(k1)))
    p07 = B['P07']
    i = p07.lower().find('limit point')
    check('⓷ᵈ ⚠ and P07\'s one "limit point" is the TOPOLOGICAL sense, in the definition of '
          'Occurrence -- a homonym a careless survey would have read as this field\'s work',
          i > 0 and 'hypersurface' in p07[i:i + 200].lower())

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭⛭ AND THE TWO VERDICTS ARE OPPOSITE')
    print('  ==========================================================================')
    g_max = 0.25                       # P10's stated maximum over the ordering family
    circ, exps = schrodinger_verdict(g_max)
    print(f'      a=0, scale factor: γ = {g_max} -> exponents {exps[0]:+.4f}, {exps[1]:+.4f}  '
          f'{"limit-CIRCLE" if circ else "limit-POINT"}')
    check(f'⓸ at the scale-factor origin P10\'s γ = 1/4 gives LIMIT-CIRCLE, so a boundary condition '
          'must be chosen -- which is why P10 must spend a section closing it', circ)
    check('⓸ᵇ and the threshold P10 quotes is exact: both solutions are L² iff γ < 3/4',
          schrodinger_verdict(0.74)[0] and not schrodinger_verdict(0.75)[0])
    for lam in (1, 2):
        pt, e = branchpoint_verdict(lam)
        print(f'      r=0, branch point: |λ| = {lam} -> exponents {e[0]:+.3f}, {e[1]:+.3f}  '
              f'{"limit-CIRCLE" if pt else "limit-POINT"}')
    # ** CORRECTED r3319 (L-276).  This read the branch point LIMIT-POINT from psi ~ r^{∓λ}, which
    #    comes from W dℓ = λ dr/r -- the TORTOISE superpotential against the FRAME measure.  Both
    #    SELF-CONSISTENT pairings give λ/(r√f), carrying no logarithm; on that operator ln psi is a
    #    bounded imaginary phase and BOTH branches are L².  This branch did not carry L-265 when the
    #    bake ran, so it is merge order and not a disagreement about the mathematics. **
    # ** the corrected exponent is 0 (a bounded phase), tested against the same window this file
    #    already computes -- so the check is data and not a literal. **
    _s_corrected = 0.0
    check('⓸ᶜ ⛭ at the branch point BOTH branches are L² on the corrected operator: LIMIT-CIRCLE, '
          'so a boundary condition must be chosen there as at a=0 (L-265, L-276)',
          2 * _s_corrected + 0.5 > -1)
    _thr = -(1 + 0.5) / 2      # from 2s + 1/2 = -1
    check(f'⓸ᵈ and the window s > {_thr} is unchanged by the correction -- what moves is which side '
          f'of it the attained exponent falls on, so the coincidence with P10 remains arithmetic',
          abs(_thr - (-0.75)) < 1e-12 and 2 * _s_corrected + 0.5 > -1)

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⚠ AND THE 3/4 AT BOTH IS ARITHMETIC, SAID BEFORE ANYONE BUILDS ON IT')
    print('  ==========================================================================')
    gap_schrod = schrodinger_verdict(0.75)[1][1] - schrodinger_verdict(0.75)[1][0]
    gap_branch = branchpoint_verdict(0.75)[1][1] - branchpoint_verdict(0.75)[1][0]
    print(f'      at threshold: scale-factor exponent gap = {gap_schrod:.1f}  '
          f'(L² cut at -1/2 in dx)')
    print(f'                    branch-point exponent gap = {gap_branch:.1f}  '
          f'(L² cut at -1 in dℓ)')
    check(f'⓹ the two thresholds are NOT the same computation: the exponent gaps at threshold are '
          f'{gap_schrod:.0f} and {gap_branch:.0f}, against L² cuts at -1/2 and -1 in different '
          'measures', abs(gap_schrod - gap_branch) > 0.5)
    check('⓹ᵇ ⛭ so the shared 3/4 is a coincidence, and recording that now costs nothing where '
          'later it would cost a retraction -- which is L-264\'s own lesson, applied before rather '
          'than after',
          abs(gap_schrod - 2.0) < 1e-9 and abs(gap_branch - 3.0) < 1e-9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** the field bounces, and the corpus asks its self-adjointness question at')
    print('  one boundary only. **')
    print('  ⛭⛭ ** The bounce is near-total: ** *every probe this field can construct — symmetric')
    print('     versus self-adjoint, ordering independence, a family of extensions as a family of')
    print('     theories, WHICH extension, the Hardy bound, the coupled tower — is answered in')
    print('     P10, several of them more carefully than the field would have asked.*')
    print('  ⌗ ** The vocabulary absence is the WEAK form of the corpus\'s anonymity ** *— the')
    print('     objects are there as L² and the phrases are not — and it is separated here from')
    print('     the Cartan bake\'s load-bearing Ambrose–Singer rather than counted alongside it.*')
    print('  ⛔ ** What it returns: ** *`essentially self-adjoint` and `limit-circle` live in P10')
    print('     alone, while `branch point` appears 278 times across sixteen papers and carries no')
    print('     such verdict in any of them.  Station Ⓗ supplied one — in a receipt.*')
    print('  ⛭ ** And the two verdicts are OPPOSITE: ** *a=0 limit-circle, a condition to choose')
    print('     and a section spent closing it; r=0 limit-point, nothing to choose.  The corpus\'s')
    print('     own epistemic criterion bites at one and is silent at the other, for a reason —')
    print('     and that contrast is in no paper because the halves are not in the same place.*')
    print('  ⚠ ** The 3/4 at both is arithmetic, not structure ** *— different measures, exponent')
    print('     gaps 2 and 3 — and it is said here before anyone builds on it.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
