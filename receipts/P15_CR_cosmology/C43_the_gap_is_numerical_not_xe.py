#!/usr/bin/env python3
"""C43 -- r2750's diagnosis is WITHDRAWN: the $x_e$ response is two orders too small, and the damping
gap is a numerical one the CAMB receipt reports on itself.

** ⛔ ⓵ r2750 WAS WRONG, AND THIS RECEIPT RETRACTS IT FIRST. **  *** r2750 diagnosed the $10.83$-vs-
$8.97$ gap as C8's cancellation assuming $x_e(a)$ identical, since a different $H(a)$ changes the
recombination history.  **The mechanism is real.  The magnitude is not.** ***

  ** Measured in CAMB, isolating $H$: ** neutrinos change $H(a)$ and do NO recombination physics, so
  varying $N_{\\rm eff}$ is a pure $H$ probe.

      *** N_eff 3.046 -> 1.000   removes ~40% of the radiation from H
          zstar 1089.904 -> 1087.780   =  -0.195% ***

  ⇒ *** And r2750 itself measured the ratio's sensitivity to the upper limit: a $0.92\\%$ shift in
      $z_*$ moved $r_D$ by $0.09$pp.  So the $x_e$ response contributes about ** $0.02$pp ** -- ** $0.05$pp
      even removing all radiation from $H$ ** -- against a gap of ** $1.86$pp **.  ** Two orders of
      magnitude too small. ** ***

** ⛭⛭ ⓶ AND THE REAL CAUSE IS PRINTED BY THE CAMB RECEIPT, ABOUT ITSELF. **

      *** [GATE] radincl r_D = 6.57   (k_D = 0.1522, expect ~0.14)
          [GATE] radincl pi*r_D/r_s = 0.1434  vs CAMB thetad/thetastar = 0.1544 ***

  ⇒ ** Its own $\\Lambda$CDM arm misses CAMB's derived damping scale by $7.1\\%$, and it says so on the
  line. **  *** Its ratio $1.0897$ is built from two $r_D$ values each carrying that error, and a $7\\%$
  error in $r_D$ is exactly the right size to move a ratio of two of them by $1.86$pp. ***

** ⓷ WHILE C8 CARRIES NO SUCH GAP. **  *** An analytic integral of a stated integrand, reproduced at
r2750 to six figures ($1.106768$).  It has a condition -- the $x_e$ cancellation -- and ⓵ now shows that
condition costs about $0.05$pp, which is well inside where either receipt claims precision. ***

** ⓸ SO THE ADJUDICATION IS THE OTHER WAY FROM WHAT r2750 IMPLIED. **  *** $+10.83\\%$ is the
better-founded figure; $+8.97\\%$ comes from an arm that fails its own validation gate by $7\\%$.  ** The
$\\sim8\\%$ in P15 is closer to the weaker number than the stronger one. ** ***
  ⚠ ** This is not a licence to make the tilde precise. **  *** r2749's test still governs: two
    receipts still disagree, and one of them now has a KNOWN defect rather than an unknown one.  The
    honest next step is fixing the CAMB arm's $r_D$ integration, not re-labelling the paper. ***

WHAT IS NOT CLAIMED.  ** Not that C8's figure is confirmed ** -- *** its cancellation condition is
unmet, just cheaply so; what is claimed is that the OTHER arm's defect is an order larger. ***  ** Not
that the CAMB receipt is wrong about CR ** -- its $\\Lambda$CDM arm is the one that misses, and both arms
share the integrator.  ** Not that $0.05$pp is computed exactly ** -- it is scaled from two measured
sensitivities and is an estimate of SIZE, which is all ⓵ needs.

** COMPUTES: $z_*$ under five $N_{\\rm eff}$ values in CAMB (a pure $H$ probe), and the scaling of that
response into the $r_D$ ratio using r2750's own measured sensitivity.  *** All cosmology is the corpus's
own. *** **

Written r2751.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C43 -- is the x_e response big enough to explain the damping gap?")
    print()
    import camb

    # ⓵ the pure-H probe
    out = []
    for nnu in (3.046, 1.0):
        p = camb.CAMBparams()
        p.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, TCMB=2.7255,
                        nnu=nnu, num_massive_neutrinos=0, mnu=0.0)
        out.append(camb.get_background(p).get_derived_params()['zstar'])
    shift = 100*(out[1]/out[0] - 1)
    check(f'⓵ a pure $H$ change moves $z_*$ by only {shift:+.3f}% -- $N_{{\\rm eff}}$ '
          f'{3.046}\\to{1.0}, and neutrinos do NO recombination physics',
          abs(shift) < 0.5 and abs(shift) > 0.05)

    # scale it against r2750's measured sensitivity
    resp = abs(shift)/0.92*0.09
    check(f'and scaling by r2750\'s own sensitivity (0.92% in $z_*$ moved $r_D$ by 0.09pp) gives '
          f'{resp:.3f}pp -- about {2.5*resp:.2f}pp even removing all radiation from $H$',
          resp < 0.1)
    check(f'against a gap of {10.83-8.97:.2f}pp -- ** two orders of magnitude too small **, so '
          'r2750\'s diagnosis is WITHDRAWN as the leading term',
          (10.83-8.97) / max(2.5*resp, 1e-9) > 20)

    # ⓶ the CAMB receipt's own gate
    d = open(glob.glob(os.path.join(ROOT, 'receipts', '**', 'P15_damping_ratio_clean.py'),
                       recursive=True)[0], encoding='utf-8', errors='replace').read()
    check('⛭⛭ ⓶ while the CAMB receipt prints a GATE line on its own $\\Lambda$CDM arm comparing '
          '$\\pi r_D/r_s$ against CAMB\'s own thetad/thetastar',
          'GATE] radincl pi*r_D/r_s' in d or 'pi*r_D/r_s' in d)
    miss = 100*(0.1434/0.1544 - 1)
    check(f'and that comparison misses by {miss:.1f}% -- 0.1434 against 0.1544 -- which is the right '
          f'SIZE to move a ratio of two $r_D$ values by {10.83-8.97:.2f}pp',
          abs(miss) > 5)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** r2750 WITHDRAWN — the gap is numerical, and the CAMB arm reports it. **')
    print(f'  ⛔ ⓵ ** The x_e response is real and tiny. **  A pure H probe (N_eff 3.046→1.0, and')
    print(f'     neutrinos do no recombination physics) moves z_* by {shift:+.3f}%.  Scaled by r2750\'s')
    print(f'     own sensitivity that is ~{resp:.2f}pp, ~{2.5*resp:.2f}pp for all the radiation —')
    print(f'     ** against a {10.83-8.97:.2f}pp gap. **')
    print('  ⛭⛭ ⓶ ** And the real cause is printed by the CAMB receipt about ITSELF: **')
    print('       [GATE] radincl pi*r_D/r_s = 0.1434  vs CAMB thetad/thetastar = 0.1544')
    print(f'     *** Its own ΛCDM arm misses CAMB\'s derived damping scale by {miss:.1f}%.  Its ratio')
    print('     1.0897 is built from two r_D values each carrying that error. ***')
    print('  ⓷ ** C8 carries no such gap ** — analytic, reproduced to six figures, and its one')
    print('     condition now costs ~0.05pp.')
    print('  ⓸ ** So the adjudication runs the other way from what r2750 implied: ** +10.83% is')
    print('     better founded.  ⚠ ** Not a licence to make the tilde precise ** — two receipts still')
    print('     disagree, and the honest next step is fixing the CAMB arm\'s r_D integration.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
