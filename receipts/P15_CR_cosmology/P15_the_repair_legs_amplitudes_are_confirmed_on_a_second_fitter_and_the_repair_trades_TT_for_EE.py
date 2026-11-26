# -*- coding: utf-8 -*-
"""⛭⛭⛭ `r7877+cc66` ** ⑮ `60`'s REPAIR-LEG AMPLITUDES ARE CONFIRMED ON A SECOND FITTER -- **ALL
EIGHT** BANKED FITS AGREE TO `8.8e-06`, ON A HARNESS THAT RE-DERIVES `r7875`'s FOUR LANDED
AMPLITUDES AT **EXACTLY ZERO**. ⛔ AND THE REPAIR **TRADES `TT` FOR `EE`**: IT CARRIES `TT` NEARER
UNITY WHILE PUSHING `EE` **FARTHER**, OUT OF ITS `0.05` BAND ON ALL FOUR FITS **

COMPUTES: nothing.  Every figure is read out of the one JSON record this revision's driver wrote
(`refit_legs.json`).  No parameter is pinned here.

⌗ ONLY TWO OF THE SIX LEGS `69` NAMED EXIST.  `60` bank the Fermi–Dirac repair ON and OFF; the four
decomposition legs -- weight alone, continuity alone, Euler alone, the `c_a²` variant -- are NOT
banked, because `69` ordered `60` to produce them in this same round.  That half of ⑮ waits, and
`Ⓘ⑨` records the absence rather than leaving it to be inferred from silence.

⌗ `Ⓗ⑧` WAS REGISTERED AT RISK AND THE RISK MATERIALISED, FOR `EE`: my fitter cannot resolve the two
legs apart in `EE`, so the `EE` agreement confirms the BANK READING and not the leg.  `TT` resolves
cleanly and carries the comparison.  `Ⓖ⑦`'s finding -- the trade -- is sharper than what I
registered, which expected only to report a distance from unity.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7877_cc66_the_second_fitter_on_60s_repair_legs')

_n, _fail = [0], [0]


def check(label, ok, detail=''):
    _n[0] += 1
    if not ok:
        _fail[0] += 1
    print('\n    [%s] %s' % ('PASS' if ok else 'FAIL', label))
    if detail:
        print('             %s' % detail)


def load(p):
    if not os.path.exists(p):
        sys.exit('FATAL: %s is not where this reads it from.' % p)
    return json.load(io.open(p, encoding='utf-8'))


print('=' * 100)
print(__doc__)
print('=' * 100)

RL = load(os.path.join(MINE, 'refit_legs.json'))
F = RL['fits']
S = RL['separation']
D = RL['direction']

# ───────────────────────────────────────────── Ⓐ① the control and 60's multipoles, as 69 ruled
check("⛭ `r7877` ** ⑮ Ⓐ① THE CONTROL IS READ AT RUN TIME AND THE MULTIPOLE SET IS `60`'s `41`, "
      "**AS `69` RULED IN THIS ORDER** ** ⇒ *** `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, "
      "`n_s = 0.965`, `τ = 0.054`, `lmax = 2600`, band `ℓ = 100`--`420`, and every fit on the `41` "
      "in-band multipoles `60`'s bank carries. ** `69`'s order says it in those words: *every "
      "comparison uses `60`'s `41` in-band multipoles, stated* -- because `r7875` measured that "
      "choice as worth `0.004311` in `A`. *** ⌗ *The zero leg is the LANDED one, which is `60`'s "
      "choice and their stated reason: `NUFD` is gated on a non-zero sum, so the repair is provably "
      "inert at `Σ = 0`. A ratio against a different denominator would be a different quantity*",
      (abs(RL['control']['H0'] - 67.40) < 1e-9 and abs(RL['control']['OM'] - 0.3150) < 1e-9
       and abs(RL['control']['WB'] - 0.0224) < 1e-9 and abs(RL['control']['NS'] - 0.965) < 1e-9
       and abs(RL['tau'] - 0.054) < 1e-12 and RL['lmax'] == 2600
       and RL['window'] == [100, 420]
       and all(v['n_multipoles'] == 41 for v in F.values())
       and abs(sorted({float(k.split('|')[2]) for k in F})[0] - 0.30) < 1e-12
       and abs(sorted({float(k.split('|')[2]) for k in F})[1] - 0.60) < 1e-12),
      'control %s; lmax %d; window %s; every fit on %d multipoles'
      % (RL['control'], RL['lmax'], RL['window'],
         sorted({v['n_multipoles'] for v in F.values()})[0]))

# ───────────────────────────────────────────── Ⓑ② the regression control, exact
check("⛭⛭⛭ `r7877` ** ⑮ Ⓑ② **THE HARNESS IS THE SAME INSTRUMENT AS `r7875`'s, PROVED AT EXACTLY "
      "ZERO** -- IT **IMPORTS** THAT FITTER AND CAMB LEG RATHER THAN RE-IMPLEMENTING THEM, AND "
      "RE-DERIVES ITS FOUR LANDED AMPLITUDES BIT-IDENTICALLY ** ⇒ *** `1.1516214172`, `1.2959211455`, "
      "`1.0140591925`, `1.0463071504` -- worst difference over the four is `0.0`. ** This gates "
      "everything below: a fitter that had drifted since `r7875` would report new numbers for the "
      "new legs and nothing would say which half had moved. *** ⌗ *Registered as `Ⓑ②` with that "
      "reason, and written by importing rather than copying, because a COPIED fitter can agree with "
      "its ancestor's numbers and still differ in the code that will meet the new legs*",
      (RL['regression_worst'] == 0.0
       and abs(RL['regression']['TT|0.30']['A'] - 1.151621417168135) < 1e-15
       and abs(RL['regression']['TT|0.60']['A'] - 1.2959211454888449) < 1e-15
       and abs(RL['regression']['EE|0.30']['A'] - 1.0140591924745146) < 1e-15
       and abs(RL['regression']['EE|0.60']['A'] - 1.0463071504477712) < 1e-15
       and RL['legs_read'] is True),
      'worst regression difference %.1e over the four landed amplitudes'
      % RL['regression_worst'])

# ───────────────────────────────────────────── Ⓒ③ the fitter is not hard-wired
check("⛭⛭⛭ `r7877` ** ⑮ Ⓒ③ **THE FITTER RECOVERS PLANTED AMPLITUDES ON BOTH SIDES OF UNITY, TO "
      "`1.110223e-16`** ** ⇒ *** `A = 0.85` at `ε = +0.0055` and `A = 1.25` at `−0.0020` -- chosen "
      "deliberately to straddle unity, because the legs under test sit BELOW it at `0.86` while "
      "`r7875`'s landed instrument sat ABOVE at `1.15`. Worst recovery error `1.110223e-16`. ** A "
      "fitter biased toward one side of unity would confirm `60` on one and not the other. *** ⌗ *A "
      "mechanism that cannot fail cannot confirm -- the same control the `MassiveNuMethod` knob "
      "needed at `r7871`, the custom-source path at `r7873`, and the amplitude fit at `r7875`*",
      (RL['planted_ok'] is True and len(RL['planted']) == 2
       and max(v['dA'] for v in RL['planted'].values()) < 1e-12
       and abs(max(v['dA'] for v in RL['planted'].values())
               - 1.1102230246251565e-16) < 1e-24),
      '2 plants straddling unity, worst |dA| %.6e'
      % max(v['dA'] for v in RL['planted'].values()))

# ───────────────────────────────────────────── Ⓓ④ THE ANSWER: eight of eight
check("⛭⛭⛭ `r7877` ** ⑮ Ⓓ④ **THE ANSWER: ALL EIGHT BANKED FITS REPRODUCE `60`'s, WORST "
      "`8.818003e-06`** -- SO `69`'s *ACCEPTED ON TWO FITTERS, NOT ONE* IS SATISFIED ON THE "
      "MEASUREMENT ** ⇒ *** `shear_on` gives `TT` `0.8640021952` and `0.8146575898`, `EE` "
      "`0.9447322292` and `0.9112079824`; `shear_off` gives `TT` `0.8602490392` and `0.8110362191`, "
      "`EE` `0.9447315869` and `0.9112188013`. Against `60`'s eight figures the worst disagreement "
      "is `8.818003e-06`, on `shear_off` `TT` at `Σ = 0.60`. ** `69`'s merge paragraph quoted "
      "`0.864` and `0.815`; those are the `shear_on` leg, and both legs are named here so the record "
      "cannot inherit an ambiguity about which leg a figure came from. *** ⌗ *Two independent CAMB "
      "runs and two fitters. What this does NOT do is adjudicate the repair: `69` has ruled it "
      "refuted on `60`'s own validation*",
      (RL['n_hits'] == 8 and len(F) == 8
       and all(v['hits'] for v in F.values())
       and abs(F['shear_on|TT|0.30']['A'] - 0.8640021952381803) < 1e-13
       and abs(F['shear_on|TT|0.60']['A'] - 0.8146575897931293) < 1e-13
       and abs(F['shear_off|TT|0.30']['A'] - 0.8602490391737234) < 1e-13
       and abs(F['shear_off|TT|0.60']['A'] - 0.8110362191026903) < 1e-13
       and abs(F['shear_on|EE|0.30']['A'] - 0.9447322291893475) < 1e-13
       and abs(F['shear_off|EE|0.60']['A'] - 0.9112188013342475) < 1e-13
       and abs(max(v['diff_from_60'] for v in F.values())
               - 8.818002690258453e-06) < 1e-15),
      '%d of %d fits within 0.005 of 60\'s; worst |dA| %.6e'
      % (RL['n_hits'], len(F), max(v['diff_from_60'] for v in F.values())))

# ───────────────────────────────────────────── Ⓔ⑤ EE is outside its band
check("⛭⛭⛭ `r7877` ** ⑮ Ⓔ⑤ **`EE` IS OUTSIDE ITS OWN `0.05` BAND ON **ALL FOUR** FITS, WHICH "
      "CONFIRMS `69`'s RULING THAT `EE`'s AGREEMENT IS A CONSTRAINT ** ⇒ *** `|A − 1|` is "
      "`0.055268` on both legs at `Σ = 0.30` and `0.088781`/`0.088792` at `0.60`, against the "
      "`0.05` band `60`'s own record carries. All four are outside it. ** `69` ruled `EE`'s "
      "agreement a constraint rather than a preference, so the repair fails on a criterion fixed "
      "before it existed. *** ⌗ *Measured against the band rather than asserted: the arm reports "
      "`|A − 1|` for each of the four and lets the comparison stand*",
      (abs(RL['ee_band'] - 0.05) < 1e-12
       and len(RL['ee_vs_band']) == 4
       and all(v['outside'] for v in RL['ee_vs_band'].values())
       and abs(RL['ee_vs_band']['shear_on|EE|0.30']['dist'] - 0.05526777081065248) < 1e-15
       and abs(RL['ee_vs_band']['shear_off|EE|0.60']['dist'] - 0.08878119866575251) < 1e-15),
      'all 4 EE fits outside the %.2f band; %.6f at 0.30 and %.6f at 0.60'
      % (RL['ee_band'], RL['ee_vs_band']['shear_on|EE|0.30']['dist'],
         RL['ee_vs_band']['shear_on|EE|0.60']['dist']))

# ───────────────────────────────────────────── Ⓕ⑥ the trade -- sharper than registered
check("⛭⛔⛭ `r7877` ** ⑮ Ⓕ⑥ **THE REPAIR **TRADES `TT` FOR `EE`** -- IT CARRIES `TT` *NEARER* UNITY "
      "WHILE PUSHING `EE` *FARTHER*, AND THIS IS SHARPER THAN WHAT I REGISTERED ** ⇒ *** the sign "
      "flips in all four: the landed instrument sits ABOVE CAMB and every repaired leg sits BELOW. "
      "But the MAGNITUDE does not move the same way. `TT` improves -- `0.151621` from unity landed "
      "against `0.135998` repaired at `Σ = 0.30`, and `0.295921` against `0.185342` at `0.60`. "
      "`EE` WORSENS -- `0.014059` against `0.055268`, and `0.046307` against `0.088792`. ** So the "
      "repair genuinely removes part of `TT`'s discrepancy and enlarges `EE`'s, which is WHY `EE` is "
      "the binding constraint rather than merely THAT it is. *** ⌗ *`Ⓖ⑦` of the registration expected "
      "to report a distance from unity and read the overshoot as one effect. It is two, pulling "
      "opposite ways in the two blocks, and that was not registered*",
      (all(D['shear_on|%s|%.2f' % (b, s)]['sign_flipped']
           for b in ('TT', 'EE') for s in (0.30, 0.60))
       and D['shear_on|TT|0.30']['nearer_unity'] is True
       and D['shear_on|TT|0.60']['nearer_unity'] is True
       and D['shear_on|EE|0.30']['nearer_unity'] is False
       and D['shear_on|EE|0.60']['nearer_unity'] is False
       and abs(D['shear_on|TT|0.30']['landed_dist'] - 0.15162141716813493) < 1e-15
       and abs(D['shear_on|TT|0.30']['repaired_dist'] - 0.13599780476181966) < 1e-15
       and abs(D['shear_on|EE|0.30']['landed_dist'] - 0.014059192474514592) < 1e-15
       and abs(D['shear_on|EE|0.30']['repaired_dist'] - 0.05526777081065248) < 1e-15
       and abs(D['shear_on|TT|0.60']['landed_dist'] - 0.29592114548884485) < 1e-15
       and abs(D['shear_on|TT|0.60']['repaired_dist'] - 0.1853424102068707) < 1e-15
       and abs(D['shear_on|EE|0.60']['landed_dist'] - 0.04630715044777123) < 1e-15
       and abs(D['shear_on|EE|0.60']['repaired_dist'] - 0.08879201755747457) < 1e-15),
      'TT 0.30 %.6f -> %.6f (nearer); EE 0.30 %.6f -> %.6f (farther); all four sign-flipped'
      % (D['shear_on|TT|0.30']['landed_dist'], D['shear_on|TT|0.30']['repaired_dist'],
         D['shear_on|EE|0.30']['landed_dist'], D['shear_on|EE|0.30']['repaired_dist']))

# ───────────────────────────────────────────── Ⓖ⑦ Ⓗ⑧'s registered risk materialised for EE
check("⛭⛔⛭ `r7877` ** ⑮ Ⓖ⑦ **MY REGISTERED `Ⓗ⑧` RISK MATERIALISED: THIS FITTER **CANNOT RESOLVE THE "
      "TWO LEGS APART IN `EE`**, SO THE `EE` AGREEMENT CONFIRMS THE BANK READING AND **NOT THE LEG** "
      "** ⇒ *** `EE`'s `shear_on` minus `shear_off` is `6.422709e-07` at `Σ = 0.30` and "
      "`1.081889e-05` at `0.60`, while my own interpolation floor for `EE`, measured at `r7875`, is "
      "`5.307333e-05` -- eighty times the first and five times the second. ** `TT` separates "
      "cleanly: `0.003753` by my fitter against `0.003755` by `60`'s, on a floor of `3.515264e-06`. "
      "So `TT` carries the leg-to-leg comparison and `EE` does not. *** ⌗ *Registered BEFORE the "
      "run, in those terms: 'if my fitter cannot separate two legs that differ by `6e-07`, then an "
      "agreement with `60` on `EE` says nothing about the leg'. It cannot, and it does not. An "
      "agreement that cannot discriminate is worth reporting as such rather than counting as four "
      "independent confirmations*",
      (S['EE|0.30']['resolvable'] is False and S['EE|0.60']['resolvable'] is False
       and S['TT|0.30']['resolvable'] is True and S['TT|0.60']['resolvable'] is True
       and abs(S['EE|0.30']['mine'] - 6.422708574982394e-07) < 1e-18
       and abs(S['EE|0.30']['my_floor'] - 5.307332502169082e-05) < 1e-18
       and S['EE|0.30']['mine'] < S['EE|0.30']['my_floor']
       and abs(S['TT|0.30']['mine'] - 0.0037531560644569195) < 1e-15
       and S['TT|0.30']['mine'] > S['TT|0.30']['my_floor']),
      'EE on-off %.6e against my floor %.6e (not resolvable); TT on-off %.6f against %.6e '
      '(resolvable)' % (S['EE|0.30']['mine'], S['EE|0.30']['my_floor'],
                        S['TT|0.30']['mine'], S['TT|0.30']['my_floor']))

# ───────────────────────────────────────────── Ⓗ⑧ what is not banked
check("⛭⛔⛭ `r7877` ** ⑮ Ⓗ⑧ **FOUR OF THE SIX LEGS `69` NAMED DO NOT EXIST YET, AND THE ABSENCE IS "
      "RECORDED RATHER THAN LEFT TO BE INFERRED FROM SILENCE ** ⇒ *** `69` ordered a read of `60`'s "
      "decomposition legs -- weight alone, continuity alone, Euler alone, and the `c_a²` variant -- "
      "**when they land**. They have not landed: `60`'s `r7876` banks the repair ON and OFF and "
      "nothing else, because `69` ordered the decomposition in the SAME round. ** So this revision "
      "answers ⑮ on the two legs that exist and names the four that do not. Nothing is invented for "
      "them, and no verdict about the decomposition is offered. *** ⌗ *The harness is built, "
      "registered and proved against `r7875` at exactly zero, so the four legs are a one-command run "
      "the moment `60` bank them*",
      (sorted(RL['legs_missing']) == ['c_a2', 'continuity', 'euler', 'weight']
       and sorted(RL['legs_banked']) == ['shear_off', 'shear_on']
       and len(RL['legs_banked']) == 2 and len(RL['legs_missing']) == 4),
      'banked: %s; NOT banked: %s' % (', '.join(sorted(RL['legs_banked'])),
                                      ', '.join(sorted(RL['legs_missing']))))

# ───────────────────────────────────────────── the count arm
check("⛭ `r7877` ** Ⓘ⑨ THE ARMS ABOVE ARE **ALL OF THEM** ** ⇒ *** eight arms precede this one, all "
      "on item ⑮. *** ⌗ *A receipt that loses an arm to an editing slip reports fewer failures than "
      "it has*",
      _n[0] == 8,
      '%d arm(s) before this one' % _n[0])

print('\n' + '=' * 100)
print('  %d arm(s), %d failed' % (_n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
