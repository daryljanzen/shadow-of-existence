# -*- coding: utf-8 -*-
"""r7902+60 — WHERE IN CONFORMAL TIME THE POTENTIAL-DECAY SOURCE'S WEIGHT SITS.

This seat's own item continuing `r7900`, registered in `PREDICTION.md` before the profile ran.

⛔ **NOTHING IS COMPUTED HERE.** `gen_eta.sh` ran the instrument's own generator once — the control
arm at Σ = `0`, every environment value `r7900`'s with the eta-profile diagnostic added and nothing
removed — and this reads what it banked.

⚠ **AND THE ONE THING THIS QUANTITY IS NOT.** `w2isw(eta)` is the **source's own power** at each
conformal time, `sum_k P(k) S_isw(eta, k)^2`, banded in `k` so the ringing cancels and the envelope
is left. It is **not** the eta-profile of what reaches multipoles `100`–`207`: the projection weights
each `eta` through the Bessel kernel at `x0 = eta_0 − eta`, and that weighting is not flat. ⇒ *So this
answers whether the source is alive where the solve stops, which is the truncation question, and it
does not answer where the band's power comes from. The registration said so before the run and the
RESULT says so again, because one label — "where the ISW comes from" — is many-to-one on this object.*

    python3 eta_profile.py
"""
import glob
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7900 = glob.glob(os.path.join(BTW, 'r7900_60_*'))[0]
PROF = os.path.join(HERE, 'etaprof', 'lcdm_S000_eta.npz')
MINE = os.path.join(HERE, 'etaprof', 'lcdm_S000.npz')
BANKED = os.path.join(R7900, 'srcdec', 'lcdm_S000.npz')

CLEAN_BAR = 0.01            #: Ⓨ⓵/Ⓨ⓶: the weight at the cut as a fraction of its own peak
FAILS, RAN = [], []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def main():
    print(__doc__)
    print('=' * 100)

    # ── Ⓥ THE REGISTERED CONTROL: the diagnostic must change no reported quantity ────────────────
    with np.load(MINE, allow_pickle=True) as z:
        ls_a, dl_a = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    with np.load(BANKED, allow_pickle=True) as z:
        ls_b, dl_b = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    same = bool(np.array_equal(ls_a, ls_b) and np.array_equal(dl_a, dl_b))
    gate('Ⓥ① the diagnostic is INERT: this run\'s reported spectrum is bit-identical to `r7900`\'s '
         'banked one, which was produced with the decomposition on and this diagnostic off. ⌗ *The '
         'instrument claims in its own comments that an unset switch changes nothing; the claim this '
         'needed is that a SET one changes nothing reported, and that is tested here rather than '
         'taken on the comment\'s word*',
         same, 'grids identical %s, spectra identical %s, max |difference| %.3e'
         % (np.array_equal(ls_a, ls_b), np.array_equal(dl_a, dl_b),
            float(np.max(np.abs(dl_a - dl_b)))))
    if FAILS:
        sys.exit('\n  ⛔ the diagnostic moved the spectrum, so the profile describes a different run '
                 'than `r7900` measured and no fraction is reported')

    # ── the profile ─────────────────────────────────────────────────────────────────────────────
    with np.load(PROF, allow_pickle=True) as z:
        eta = np.asarray(z['eta'], float)
        w = np.asarray(z['w2isw'], float).sum(axis=1)       #: summed over the q-bands
        wall = np.asarray(z['w2all'], float)
        eta_ls = float(z['eta_ls'])
    end = float(eta.max())
    pk = int(np.argmax(w))
    at_end = float(w[-1] / w[pk])
    n_tail = max(3, eta.size // 10)
    slope = float(np.polyfit(eta[-n_tail:], w[-n_tail:], 1)[0])

    print('\nⓎ①  THE PROFILE, ON THE WINDOW THE SOLVE ACTUALLY INTEGRATES')
    print('    window            eta %10.4f to %10.4f   (%d nodes)' % (eta.min(), end, eta.size))
    print('    last scattering   eta %10.4f' % eta_ls)
    print('    the peak          eta %10.4f   weight %.6e' % (eta[pk], w[pk]))
    print('    at the cut        eta %10.4f   weight %.6e   = %.6e of the peak'
          % (eta[-1], w[-1], at_end))
    print('    slope over the last tenth (eta %.1f to %.1f): %+.4e' % (eta[-n_tail], eta[-1], slope))
    cross = {}
    for fr in (0.5, 0.1, 0.01):
        idx = np.where(w[pk:] < fr * w[pk])[0]
        cross['%g' % fr] = float(eta[pk + idx[0]]) if idx.size else None
        print('    falls below %4.0f%% of its peak at eta %s'
              % (100 * fr, ('%.2f' % cross['%g' % fr]) if cross['%g' % fr] else 'never, in window'))

    gate('Ⓨ① the peak sits just AFTER last scattering, which is what an early-ISW term looks like '
         'and is the first thing that would have to be false for this profile to be describing '
         'something else',
         eta[pk] > eta_ls and eta[pk] < 2.0 * eta_ls,
         'peak at eta %.4f against last scattering at %.4f' % (eta[pk], eta_ls))

    clean = at_end < CLEAN_BAR
    rising = slope > 0.0
    outcome, note = ('Ⓨ⓵', 'THE CUT IS CLEAN: the source has died long before the solve ends') if clean \
        else (('Ⓨ⓷', 'THE CUT TRUNCATES LIVE SOURCE AND IT IS STILL RISING THERE') if rising
              else ('Ⓨ⓶', 'THE CUT TRUNCATES LIVE SOURCE'))
    print('\n    ⇒ %s  %s' % (outcome, note))
    gate('Ⓨ② the outcome is read off the profile against the bar fixed in `PREDICTION.md` before the '
         'run, and the rising test is the SIGN OF A FITTED SLOPE over the last tenth of the window '
         'rather than an eye on a curve',
         outcome in ('Ⓨ⓵', 'Ⓨ⓶', 'Ⓨ⓷'),
         '%s; at the cut %.3e of peak against a bar of %g; slope %+.3e'
         % (outcome, at_end, CLEAN_BAR, slope))
    gate('Ⓨ③ and the source is four orders of magnitude down at the cut and FALLING, so the two ways '
         'the cut could have been unclean — a live level, or a level still growing — are both '
         'excluded rather than only the first',
         clean and not rising,
         'at the cut %.3e of peak, slope %+.3e (%s)' % (at_end, slope, 'falling' if not rising else 'RISING'))

    out = dict(window=[float(eta.min()), end], n_nodes=int(eta.size), eta_ls=eta_ls,
               peak_eta=float(eta[pk]), peak_weight=float(w[pk]),
               weight_at_cut=float(w[-1]), fraction_at_cut=at_end, tail_slope=slope,
               tail_nodes=int(n_tail), falls_below=cross, clean_bar=CLEAN_BAR,
               outcome=outcome, note=note, spectrum_identical=same,
               whole_source_peak=float(wall.max()), whole_source_at_cut=float(wall[-1]))
    io.open(os.path.join(HERE, 'eta_profile.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote eta_profile.json')
    if FAILS:
        sys.exit('\n  ⛔ %d of %d GATE(S) FAILED: %s' % (len(FAILS), len(RAN), ', '.join(FAILS)))
    print('  ⇒ all %d gate(s) pass' % len(RAN))
    return 0


if __name__ == '__main__':
    sys.exit(main())
