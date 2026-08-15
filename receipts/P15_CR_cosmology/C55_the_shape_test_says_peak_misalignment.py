#!/usr/bin/env python3
"""C55 -- the SHAPE TEST RUNS AND KILLS r2786's CANDIDATE: the CR arm's residual does not follow the
damping envelope, it oscillates at the acoustic spacing.  The $281$ is PEAK MISALIGNMENT.

** THE TEST r2786 NAMED, RUN. **  *** "Extract the CR arm's per-bin residual and check whether it
follows $\\exp[-(\\ell/\\ell_D)^2]$ -- rising from $\\sim0.06\\%$ at $\\ell=100$ to $\\sim34\\%$ at
$\\ell=2000$ -- or is flat.  ** A profile match converts the candidate; a flat residual kills it. ** "
Both arms are banked, so the test needs only their ratio. ***

** ⛔ ⓵ IT IS NEITHER A MATCH NOR FLAT.  IT OSCILLATES. **

      *** ell     measured ratio    predicted
          100          0.4771       0.9991
          420          1.3126       0.9847
          740          0.8500       0.9532
         1380          0.6684       0.8464
         1996          2.3754       0.7055 ***

  ** measured range $0.237$ to $2.375$ against a predicted $0.999$ to $0.706$ **, and
  ** correlation $=-0.296$ ** -- *** NEGATIVE.  The residual is anticorrelated with the profile it was
  supposed to follow. ***

** ⛭⛭⛭ ⓶ AND THE OSCILLATION IS THE ACOUSTIC COMB. **  *** A Fourier transform of the ratio gives a
dominant period of $317$ in $\\ell$ against $\\Lambda$CDM's acoustic spacing $\\ell_A=301$ -- ** a ratio
of $1.05$ **. ***

  ⇒⇒ *** THE $281$ IS DOMINATED BY PEAK MISALIGNMENT, NOT BY AN ENVELOPE.  Two combs slightly out of
      register produce a ratio that swings above and below one at the comb spacing, which is exactly
      what is measured. ***

** ⓷ AND THE ARMS' OWN NUMBERS SAY WHERE IT COMES FROM. **

      *** l_A:  CR 301.60   LCDM 301.37     -- agree to 0.08%
          r_s:  CR 135.46   LCDM 144.53     -- differ by 6.3% ***

  ⇒ *** The projected acoustic SCALE agrees and the sound HORIZON does not -- so the two arms put their
      peaks in nearly the same places by construction while the physics underneath differs.  ** A
      residual $\\ell_A$ mismatch of even $0.08\\%$ accumulates across six peaks into a visible phase
      slip by $\\ell\\sim2000$. ** ***

** ⓸ SO r2786 IS WITHDRAWN, AND THE ROW GAINS A SHARPER REMAINDER. **  *** r2786 said $281$ might be
P15's prediction being measured.  ** It is not: the prediction is a smooth envelope and the measurement
is an oscillation. **  What `PO-10` now owes is whether the phase slip is PHYSICAL (the two models
genuinely place peaks differently) or NUMERICAL (the arm's $\\ell_A$ calibration) -- and the $6.3\\%$
$r_s$ gap against a $0.08\\%$ $\\ell_A$ gap is the place to look. ***

WHAT IS NOT CLAIMED.  ** Not that the damping signature is absent ** -- *** it is a $\\sim30\\%$ effect at
$\\ell=2000$ and would sit UNDER an oscillation of this size; this receipt shows it does not DOMINATE,
not that it is missing. ***  ** Not that the phase slip is a defect ** -- *** physical or numerical is
exactly the open question. ***  ** Not that $281$ is re-derived ** -- the arms' $\\chi^2$ is not
recomputed here.

** COMPUTES: the banked arms' ratio, its correlation with P15's profile, and its dominant Fourier
period against $\\ell_A$.  *** Both spectra are `c54.178`, the corpus's own. *** **

Written r2787.  Stated for reversal.
"""
import glob
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

R_DAMP, L_D = 1.0824, 1400.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C55 -- does the CR arm's residual follow the damping profile?")
    print()
    cr = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_cr.npz'), recursive=True)[0])
    lc = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_lcdm.npz'), recursive=True)[0])
    ls = cr['ls']
    ratio = cr['Dl']/lc['Dl']
    pred = np.exp(-(ls/L_D)**2*(R_DAMP**2 - 1))

    check(f'⛔ ⓵ the measured ratio swings {ratio.min():.3f} to {ratio.max():.3f}, against a predicted '
          f'{pred.min():.3f} to {pred.max():.3f} -- ** it is not an envelope **',
          ratio.max() - ratio.min() > 3*(pred.max() - pred.min()))

    c = float(np.corrcoef(ratio, pred)[0, 1])
    check(f'and their correlation is {c:.3f} -- ** NEGATIVE: anticorrelated with the profile it was '
          'supposed to follow **', c < 0)

    # ⓶ the oscillation period is the acoustic spacing
    sig = ratio - ratio.mean()
    F = np.abs(np.fft.rfft(sig))
    f = np.fft.rfftfreq(len(sig), d=float(ls[1]-ls[0]))
    k = int(np.argmax(F[1:]) + 1)
    per = 1.0/f[k]
    lA = float(lc['l_A'])
    check(f'⛭⛭⛭ ⓶ and its dominant period is {per:.0f} in $\\ell$ against $\\Lambda$CDM\'s acoustic '
          f'spacing $\\ell_A={lA:.0f}$ -- ** a ratio of {per/lA:.2f} **',
          0.8 < per/lA < 1.3)

    # ⓷ l_A agrees, r_s does not
    lA_cr, rs_cr, rs_lc = float(cr['l_A']), float(cr['r_s']), float(lc['r_s'])
    check(f'⓷ while the arms\' $\\ell_A$ agree to {100*abs(lA_cr-lA)/lA:.2f}% '
          f'({lA_cr:.2f} vs {lA:.2f}) and their $r_s$ differ by '
          f'{100*abs(rs_cr-rs_lc)/rs_lc:.1f}% ({rs_cr:.2f} vs {rs_lc:.2f})',
          abs(lA_cr-lA)/lA < 0.005 and abs(rs_cr-rs_lc)/rs_lc > 0.03)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the shape test kills r2786's candidate — 281 is PEAK MISALIGNMENT. **")
    print(f'  ⛔ ⓵ ** The residual is neither a match nor flat: ** it swings {ratio.min():.3f} to')
    print(f'     {ratio.max():.3f} against a predicted {pred.min():.3f}–{pred.max():.3f}, with')
    print(f'     ** correlation {c:.3f} — NEGATIVE. **')
    print(f'  ⛭⛭⛭ ⓶ ** And the oscillation IS the acoustic comb: ** dominant period {per:.0f} against')
    print(f'     ℓ_A = {lA:.0f}, a ratio of {per/lA:.2f}.')
    print('     *** Two combs slightly out of register produce a ratio swinging above and below one')
    print('     at the comb spacing — which is exactly what is measured. ***')
    print(f'  ⓷ ** And the arms say where it comes from: ** ℓ_A agrees to')
    print(f'     {100*abs(lA_cr-lA)/lA:.2f}% while r_s differs by {100*abs(rs_cr-rs_lc)/rs_lc:.1f}%.')
    print('     ** The projected scale agrees and the sound horizon does not — so a residual ℓ_A')
    print('     mismatch accumulates across six peaks into a visible phase slip by ℓ~2000. **')
    print('  ⓸ ** So r2786 is WITHDRAWN and the row gains a sharper remainder: ** is the phase slip')
    print('     PHYSICAL or NUMERICAL?  ** The 6.3% r_s gap against a 0.08% ℓ_A gap is where to look. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
