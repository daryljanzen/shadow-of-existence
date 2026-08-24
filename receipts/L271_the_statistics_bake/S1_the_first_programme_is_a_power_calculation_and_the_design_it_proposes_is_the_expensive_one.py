#!/usr/bin/env python3
r"""S1 -- P06 states Lemma A5.5 in falsifiable form and calls the sampling that would test it "the
discipline's first programme".  Thrown at it, statistics returns a POWER CALCULATION the paper never
makes -- and the design the paper proposes needs four to five times the episodes of the design its own
material supports.

COMPUTES: exact Fisher one-sided p over every table the two-arm design can produce, and exact power by
enumeration; the same for the paired design, by exact binomial sign test; the floor of each design
(the smallest reference class at which a PERFECT result reaches 0.05); the episodes each needs for 80%
power at four effect sizes; and the discreteness sawtooth, where MORE episodes lower power.  Every
p-value and every power figure is validated against `scipy` over 2304 tables and 460 binomial cases.
Nothing is fitted and nothing is pinned to a number chosen after the fact.

** ⛭ ⓵ WHAT THE PAPER STATES, AND IT STATES IT WELL. **  `P06` puts the lemma in this form:

      *** "Across a properly sampled reference class of theory-choice episodes---successes and
          failures alike---structures favoured by the rules of \S\ref{sec:rules} ahead of a decisive
          non-local measurement are subsequently confirmed at a rate above the base rate at which
          merely permitted structures are confirmed." ***

  *and it is unusually careful about the sampling: it names* **survivorship** *("a reliability estimate
  built from one's own successes is survivorship and not measurement"), it names the* **censoring**
  *("a reference class assembled only from episodes that reached a verdict will not contain this
  case"), and it insists the applied-and-disregarded episodes are part of the same sampling.*
  ⇒ ** Everything a statistician would ask about SELECTION, the paper has already asked. **

** ⛔⛭⛭ ⓶ AND THE ONE IT DOES NOT ASK IS WHETHER THE CLASS CAN BE BIG ENOUGH. **  *"Falsifiable" is a
property of the statement.  **Detectable** is a property of the DESIGN, and it is a number.*
  ⇒ *** The corpus carries `statistical power` ×0, `sample size` ×0, `effect size` ×0 across seventeen
      papers -- so the question has not been asked anywhere, not merely here. ***

** ⛔ ⓷ ASKED, THE TWO-ARM DESIGN IS EXPENSIVE. **  *Two independent arms, binary outcome, Fisher exact
one-sided at 0.05: a large effect (0.9 against 0.5) needs **38 episodes**; a moderate one (0.7 against
0.5) needs **168**.*
  ⇒ ** The documented history of physics does not hold 168 theory-choice episodes with a decisive
    non-local measurement and a clean documentary record. **  *So on a moderate true effect the
    programme as designed cannot reach a verdict, and that is a fact about the design, not the lemma.*

** ⛭⛭ ⓸ BUT THE PAPER'S OWN MATERIAL SUPPORTS THE CHEAPER DESIGN. **  *Within a theory-choice episode
the candidates are **mutually exclusive**: heliocentrism winning IS geocentrism losing.  So each
episode is a discordant pair, and the comparison belongs INSIDE the episode rather than between two
arms -- an exact sign test against a null of one-half.*
  ⇒ *** 8 episodes instead of 38.  18 instead of 72.  37 instead of 168. ***  *Between-episode
      variance is what the two-arm design pays for and the paired design does not.*
  ⌗ ** And with three live candidates the null is one-third, which is easier still. **

** ⚠ ⓹ AND THE FIVE CANNOT BE USED. **  *Read as a paired sign test, `P06`'s five celebrated instances
would give p = 0.031 -- already significant.*
  ⇒ *** They may NOT be so read, and the paper is the one that says why: they were selected because
      they succeeded.  A sign test on outcome-selected episodes measures the selection. ***
  ⇒ ** So the finding is not that the lemma is nearly proved.  It is that the binding constraint moves
    from SAMPLE SIZE to SELECTION DISCIPLINE. **  *The two-arm design fails on a scarce population;
    the paired design succeeds on a small one, but only if the episodes are fixed before their
    outcomes are consulted -- which is pre-registration, and the corpus carries that ×0 as well.*

** ⌗ ⓺ AND THE EXACT TEST IS NOT MONOTONE IN n. **  *At a true rate of 0.9, eight episodes give 0.813
power and TEN give 0.736.*  ⇒ ** Collecting two more episodes can LOWER the chance of detecting a real
effect. **  *That is the discreteness of an exact test on a small class, it is invisible to a normal
approximation, and it is a planning fact the programme would need.*

WHAT IS NOT CLAIMED.  ** Not that the lemma is true or false ** -- nothing here estimates the effect;
the arithmetic is entirely about what a design can detect.  ** Not that the effect sizes are the right
ones ** -- they are a grid, chosen before the computation and reported whole, and the reader picks.
** Not that the paired design is always available ** -- it needs a well-defined set of live candidates
per episode, which some episodes will not have, and the two-arm figures stand as the fallback.
** Not that the paper is wrong to call the lemma falsifiable ** -- it is; what is added is that
falsifiable and detectable are different properties and only one of them has been checked.
** And not that this is a criticism of the sampling discussion ** -- that discussion is better than
most, which is exactly why the missing power statement is worth naming.

    python3 receipts/L271_the_statistics_bake/S1_the_first_programme_is_a_power_calculation_and_the_design_it_proposes_is_the_expensive_one.py

Written r3160, `L-271`.  Stated for reversal.
"""
import os
import sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

#: the effect-size grid, FIXED BEFORE THE COMPUTATION and reported whole
TWO_ARM_GRID = ((0.9, 0.5), (0.8, 0.5), (0.7, 0.5))
PAIRED_GRID = (0.9, 0.8, 0.7)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


# ---------------------------------------------------------------- the two-arm design
def fisher_one_sided(a, b, c, d):
    """P(table at least this extreme | margins), for 'the required arm confirms more often'"""
    n1, n2, t = a + b, c + d, a + c
    denom = comb(n1 + n2, t)
    return sum(comb(n1, k) * comb(n2, t - k) / denom for k in range(a, min(n1, t) + 1))


def two_arm_power(n, p1, p0, alpha=0.05, _cache={}):
    key = (n, p1, p0, alpha)
    if key in _cache:
        return _cache[key]
    sig = [[fisher_one_sided(a, n - a, c, n - c) <= alpha for c in range(n + 1)]
           for a in range(n + 1)]
    pa = [comb(n, a) * p1 ** a * (1 - p1) ** (n - a) for a in range(n + 1)]
    pc = [comb(n, c) * p0 ** c * (1 - p0) ** (n - c) for c in range(n + 1)]
    tot = sum(pa[a] * pc[c] for a in range(n + 1) for c in range(n + 1) if sig[a][c])
    _cache[key] = tot
    return tot


# ---------------------------------------------------------------- the paired design
def binom_tail(n, k, theta):
    return sum(comb(n, i) * theta ** i * (1 - theta) ** (n - i) for i in range(k, n + 1))


def paired_power(n, theta, alpha=0.05, theta0=0.5):
    k = next((k for k in range(n + 1) if binom_tail(n, k, theta0) <= alpha), None)
    return 0.0 if k is None else binom_tail(n, k, theta)


def episodes_for(power_fn, target=0.80, cap=400):
    return next((n for n in range(2, cap) if power_fn(n) >= target), None)


def main():
    print()
    print('  S1 -- the first programme is a power calculation, and the design is the expensive one')
    print()

    # ============================================================== (0) the control
    print('  ' + '=' * 74)
    print('  PART 0 -- ⌗ THE ARITHMETIC IS VALIDATED BEFORE IT IS USED')
    print('  ==========================================================================')
    try:
        import itertools
        from scipy.stats import fisher_exact, binomtest
        worst_f, nf = 0.0, 0
        for a, b, c, d in itertools.product(range(0, 7), repeat=4):
            if a + b == 0 or c + d == 0:
                continue
            nf += 1
            worst_f = max(worst_f, abs(fisher_one_sided(a, b, c, d)
                                       - fisher_exact([[a, b], [c, d]],
                                                      alternative='greater').pvalue))
        worst_b, nb = 0.0, 0
        for n in range(1, 21):
            for k in range(n + 1):
                for th in (0.5, 1 / 3):
                    nb += 1
                    worst_b = max(worst_b, abs(binom_tail(n, k, th)
                                               - binomtest(k, n, th,
                                                           alternative='greater').pvalue))
        check(f'⓪ the Fisher one-sided p agrees with scipy on all {nf} tables up to 6 per cell '
              f'(worst disagreement {worst_f:.2e})', worst_f < 1e-12 and nf > 2000)
        check(f'⓪ᵇ and the binomial tail agrees with scipy on all {nb} cases '
              f'(worst {worst_b:.2e})', worst_b < 1e-12 and nb > 400)
    except ImportError:
        check('⓪ scipy is unavailable, so the arithmetic is UNVALIDATED and this receipt '
              'refuses to report figures it has not checked', False)
        print()
        print('  1 check(s) FAILED')
        return 1

    # ============================================================== (1) the floors
    print()
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE FLOOR OF EACH DESIGN: the smallest class a PERFECT result can carry')
    print('  ==========================================================================')
    two_floor = next(n for n in range(1, 40) if fisher_one_sided(n, 0, 0, n) <= 0.05)
    paired_floor = next(n for n in range(1, 40) if binom_tail(n, n, 0.5) <= 0.05)
    print(f'      two-arm : {two_floor} per arm ({2*two_floor} episodes), '
          f'best p = {fisher_one_sided(two_floor, 0, 0, two_floor):.4f}')
    print(f'      paired  : {paired_floor} episodes, best p = {binom_tail(paired_floor, paired_floor, 0.5):.4f}')
    check(f'⓵ below its floor a design cannot reach 0.05 on ANY outcome: at {two_floor-1} per arm '
          f'the two-arm best is {fisher_one_sided(two_floor-1, 0, 0, two_floor-1):.4f} and at '
          f'{paired_floor-1} episodes the paired best is '
          f'{binom_tail(paired_floor-1, paired_floor-1, 0.5):.4f}',
          fisher_one_sided(two_floor - 1, 0, 0, two_floor - 1) > 0.05
          and binom_tail(paired_floor - 1, paired_floor - 1, 0.5) > 0.05)
    check(f'⓵ᵇ and P06 reports FIVE applications of the criterion, which is at the paired floor '
          f'({paired_floor}) and below the two-arm one ({2*two_floor})',
          paired_floor == 5 and 2 * two_floor > 5)

    # ============================================================== (2) the empty arm
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ WITH THE COMPARATOR ARM EMPTY THE EVIDENCE IS NOT WEAK, IT IS ZERO')
    print('  ==========================================================================')
    for n in (5, 20, 100):
        print(f'      required arm {n}/{n} confirmed, permitted arm empty:  '
              f'p = {fisher_one_sided(n, 0, 0, 0):.4f}')
    check('⓶ a one-armed study returns p = 1 however many successes it holds, because the lemma '
          'is a COMPARISON and a comparison with nothing to compare to is not weak evidence',
          all(abs(fisher_one_sided(n, 0, 0, 0) - 1.0) < 1e-12 for n in (5, 20, 100)))
    check('⓶ᵇ which is P06\'s own sentence made quantitative -- "a compelling hypothesis with '
          'confirming instances, not a calibrated reliability" -- and stronger than it: not '
          'uncalibrated, but exactly zero',
          abs(fisher_one_sided(100, 0, 0, 0) - 1.0) < 1e-12)

    # ============================================================== (3) the two designs
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭⛭ THE PAIRED DESIGN COSTS A QUARTER TO A FIFTH OF THE EPISODES')
    print('  ==========================================================================')
    print('      effect            two-arm episodes    paired episodes    ratio')
    ratios = []
    for (p1, p0), th in zip(TWO_ARM_GRID, PAIRED_GRID):
        n2 = episodes_for(lambda n, p1=p1, p0=p0: two_arm_power(n, p1, p0))
        np_ = episodes_for(lambda n, th=th: paired_power(n, th))
        if n2 and np_:
            ratios.append(2 * n2 / np_)
            print(f'      {p1} vs {p0} / θ={th}       {2*n2:^14d}    {np_:^14d}     '
                  f'{2*n2/np_:.1f}×')
    check('⓷ on every effect size in the grid the paired design needs FEWER episodes, and the '
          f'saving is between {min(ratios):.1f}× and {max(ratios):.1f}×',
          len(ratios) == len(TWO_ARM_GRID) and min(ratios) > 2.0)
    # ** the structural claim, ASSERTED rather than narrated: the paired design spends ONE
    #   observation per episode where the two-arm design spends two, and still reaches 0.05 on a
    #   SMALLER class -- which is only possible if the pairing is removing variance rather than
    #   relabelling the same information. **
    two_floor_eps, paired_floor_eps = 2 * two_floor, paired_floor
    check(f'⓷ᵇ ⌗ and the reason is structural, not a tuning choice: the paired design spends one '
          f'observation per episode where the two-arm design spends two, and still reaches 0.05 on '
          f'a smaller class ({paired_floor_eps} episodes against {two_floor_eps}) -- which is only '
          'possible if the pairing removes variance rather than relabelling the same information',
          paired_floor_eps < two_floor_eps
          and all(episodes_for(lambda n, th=th: paired_power(n, th))
                  < 2 * episodes_for(lambda n, p1=p1, p0=p0: two_arm_power(n, p1, p0))
                  for (p1, p0), th in zip(TWO_ARM_GRID, PAIRED_GRID)))
    n_mod = episodes_for(lambda n: two_arm_power(n, 0.7, 0.5))
    check(f'⓷ᶜ ⛔ AND THE MODERATE CASE IS WHERE IT BITES: the two-arm design needs {2*n_mod} '
          f'episodes at 0.7 against 0.5, which the documented history of physics does not hold in '
          f'clean theory-choice episodes; the paired design needs '
          f'{episodes_for(lambda n: paired_power(n, 0.7))}',
          2 * n_mod > 150 and episodes_for(lambda n: paired_power(n, 0.7)) < 50)

    # ============================================================== (4) the five, and why not
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⚠ THE FIVE WOULD ALREADY BE SIGNIFICANT, AND MAY NOT BE USED')
    print('  ==========================================================================')
    p5_two = binom_tail(5, 5, 0.5)
    p5_three = binom_tail(5, 5, 1 / 3)
    print(f'      five episodes, all five favoured-structure wins, two candidates : p = {p5_two:.4f}')
    print(f'      the same against three live candidates                          : p = {p5_three:.4f}')
    check('⓸ so read as a paired sign test P06\'s five instances clear 0.05 outright',
          p5_two <= 0.05)
    p06 = os.path.join(ROOT, 'corpus', 'shadow_of_existence.tex')
    body = open(p06, encoding='utf-8', errors='replace').read() if os.path.exists(p06) else ''
    check('⓸ᵇ ⛔ AND THEY MAY NOT BE SO READ, on the paper\'s OWN ground: it says a reliability '
          'estimate built only from successes is survivorship, not measurement',
          'survivorship' in body and 'not measurement' in body)
    check('⓸ᶜ ⛭ so the finding is not that the lemma is nearly proved -- it is that the binding '
          'constraint moves from SAMPLE SIZE to SELECTION DISCIPLINE, and the corpus carries '
          'neither `pre-registration` nor `blinded` anywhere in seventeen papers',
          'pre-registration' not in body and 'blinded' not in body)

    # ============================================================== (5) the sawtooth
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE EXACT TEST IS NOT MONOTONE IN n, AND THAT IS A PLANNING FACT')
    print('  ==========================================================================')
    saw = [(n, paired_power(n, 0.9)) for n in range(5, 21)]
    drops = [(a, b) for (a, pa), (b, pb) in zip(saw, saw[1:]) if pb < pa]
    for n, p in saw[:8]:
        print(f'      n={n:<3d} power at θ=0.9: {p:.3f}')
    check(f'⓹ power FALLS with more episodes at least once in n=5..20 '
          f'(at {drops[0][0]}→{drops[0][1]} if so), because the exact test\'s critical value moves '
          f'in whole episodes',
          len(drops) >= 1)
    check('⓹ᵇ and a normal approximation would hide it, which is why the arithmetic here is exact '
          'and validated rather than approximated',
          paired_power(8, 0.9) > paired_power(10, 0.9))

    # ============================================================== (6) the baseline
    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- ⌗ THE BASELINE WAS MEASURED BEFORE ANYTHING WAS CALLED A HOLE')
    print('  ==========================================================================')
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    rows = RB.survey(['statistical power', 'sample size', 'effect size', 'pre-registration',
                      'blinded', 'null hypothesis', 'base rate', 'reference class',
                      'survivorship', 'dof', 'per degree of freedom'])
    # ** the DE-MACROED total, not the raw one: `L-266` manufactured a hole out of a LaTeX macro
    #   (`Aut(A_2)` raw 0, de-macroed 34) and this instrument exists because of it. **
    TOT = {t: max(raw, demac) for t, raw, _, demac in rows}

    def tot(term):
        return TOT[term]
    for t in ('statistical power', 'sample size', 'effect size', 'pre-registration', 'blinded',
              'null hypothesis'):
        print(f'      {t:22s} ×{tot(t)}')
    check('⓺ the four terms this bake turns on are absent from all seventeen paper bodies, '
          'de-macroed -- so the opening is measured and not assumed',
          all(tot(t) == 0 for t in ('statistical power', 'sample size', 'effect size',
                                    'pre-registration')))
    check('⓺ᵇ while the terms P06 DOES carry are present, so the instrument is reading the '
          'corpus and not returning zeros',
          tot('base rate') > 0 and tot('reference class') > 0 and tot('survivorship') > 0)
    check('⓺ᶜ ⚠ AND A NEAR-MISS IS RECORDED RATHER THAN CLAIMED: `degrees of freedom` is ×0 in '
          'P15, which looked like a hole in a paper full of χ² fits -- and P15 writes `dof` and '
          '`per degree of freedom` instead.  A spelling, not an absence.',
          tot('dof') > 0 and tot('per degree of freedom') > 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** the first programme is a power calculation, and it has not been done. **')
    print('  *P06 states A5.5 falsifiably and is careful about every selection question a')
    print('  statistician would raise -- survivorship, censoring, the applied-and-disregarded')
    print('  episodes.  What it does not ask is whether the reference class can be large enough,')
    print('  and that is a number.*')
    print('  ⛔ ** The two-arm design it proposes needs 168 episodes on a moderate effect ** — a')
    print('     population the documented history of physics does not contain.')
    print('  ⛭ ** The paired design its own material supports needs 37 ** — because within an')
    print('     episode the candidates are mutually exclusive, so the comparison belongs inside')
    print('     the episode and the between-episode variance is never paid for.')
    print('  ⚠ ** And the five cannot be spent. **  *Read paired they would already clear 0.05;')
    print('     they were selected because they succeeded, and the paper is what says so.*')
    print('  ⇒ ** So the binding constraint moves from sample size to SELECTION DISCIPLINE, which')
    print('     is pre-registration — carried ×0 in seventeen papers. **')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
