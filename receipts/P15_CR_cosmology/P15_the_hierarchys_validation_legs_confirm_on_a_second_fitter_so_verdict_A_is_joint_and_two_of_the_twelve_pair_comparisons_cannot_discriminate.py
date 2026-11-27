# -*- coding: utf-8 -*-
"""
⛭⛭ r7885+cc66 ⑰ -- THE SECOND FIT ON `60`'s r7882 VALIDATION LEGS.

COMPUTES: nothing.  Every figure is read out of the one JSON record this revision's driver wrote
(`valid_legs.json`) and compared against literals here.  The driver is
`computations/beyond_the_wall/r7885_cc66_the_second_fit_on_the_hierarchy_validation_legs/valid_legs.py`,
which IMPORTS `r7875`'s fitter and CAMB leg through `r7879` and `r7877` rather than copying either.

⛔ `Ⓒ③` DECIDES WHAT THE AGREEMENT IS WORTH, AND IT WAS REGISTERED BEFORE THE FIT.  PREDICTION.md
   (`344141a35`, pushed in its own commit before a line of the computation existed) named
   `base`-`lmax18` in EE at BOTH sums as the two comparisons that would fall below this seat's own
   EE interpolation floor, with the figures it expected.  Both did.
"""
import io
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(_HERE))
REC = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7885_cc66_the_second_fit_on_the_hierarchy_validation_legs', 'valid_legs.json')
L = json.load(io.open(REC, encoding='utf-8'))
F, S, BR = L['fits'], L['separation'], L['against_bar']

_n, _fail = [0], [0]


def check(label, cond, detail):
    _n[0] += 1
    ok = bool(cond)
    if not ok:
        _fail[0] += 1
    print('    [%s] %s' % ('OK  ' if ok else 'FAIL', label))
    print('           %s' % detail)


print(__doc__)
print('=' * 100)

# ───────────────────────────────────────────── Ⓐ① the legs and the shared zero
check("⛭⛭ `r7885` ** ⑰ Ⓐ① **THREE LEGS, AND THE ZERO LEG IS BYTE-IDENTICAL ACROSS ALL THREE, SO THE "
      "CONVERGENCE SWITCH IS PROVABLY INERT AT `Σ = 0`** ** ⇒ *** `60`'s `valid/` holds `base`, "
      "`nq24` and `lmax18`, and `lcdm_S000_pol.npz` and `lcdm_S000_tt.npz` each carry ONE sha across "
      "the three. ** So there is one shared zero leg and no choice of zero leg is this seat's -- "
      "which matters because at `r7877` and `r7879` the zero leg WAS a choice, `60`'s, and had to be "
      "attributed to them. *** ⌗ *checked rather than assumed: an identity assumed is not an "
      "identity measured*",
      (L['legs'] == ['base', 'nq24', 'lmax18']
       and L['zero_leg_byte_identical_across_legs'] is True
       and len(F) == 12 and L['absent'] == []
       and sorted({k.split('|')[-1] for k in F}) == ['0.30', '0.60']
       and L['window'] == [100, 420]
       and sorted({v['n'] for v in F.values()}) == [41]),
      'three legs, %d fits, 0 absent, sums %s, window %s, every fit on 41 multipoles'
      % (len(F), sorted({k.split('|')[-1] for k in F}), L['window']))

# ───────────────────────────────────────────── Ⓑ② the twelve fits
check("⛭⛭⛭ `r7885` ** ⑰ Ⓑ② **ALL TWELVE FITS CONFIRM `60`, WORST `6.998106e-06`, INSIDE THE `5e-05` "
      "REGISTERED BEFORE THE RUN** ** ⇒ *** `base` reads `0.98914091` and `0.97884859` in TT against "
      "`60`'s `0.98914185` and `0.97885026`, and `0.98055933` and `0.97739393` in `EE`; `nq24` reads "
      "`0.98998200` and `0.97921051` in TT; `lmax18` reads `0.98918671` and `0.97887058`. ** Twelve "
      "of twelve inside the registered tolerance, the worst seven times tighter than it. *** ⌗ *the "
      "band was fixed at `r7885+cc66.1` from this seat's own history -- `8.818003e-06` at `r7877`, "
      "`1.039197e-05` at `r7879` -- so it is a band this instrument had to meet, not one drawn "
      "around the answer after the fact*",
      (L['n_hits'] == 12 and all(v['hits'] for v in F.values())
       and abs(L['tol'] - 5e-05) < 1e-18
       and abs(L['worst_diff'] - 6.998105730571247e-06) < 1e-15
       and L['worst_diff'] < L['tol']
       and abs(F['base|TT|0.30']['A'] - 0.989140913505438) < 1e-13
       and abs(F['base|TT|0.60']['A'] - 0.9788485882731793) < 1e-13
       and abs(F['base|EE|0.30']['A'] - 0.9805593304451495) < 1e-13
       and abs(F['base|EE|0.60']['A'] - 0.9773939339439367) < 1e-13
       and abs(F['nq24|TT|0.30']['A'] - 0.9899819965705808) < 1e-13
       and abs(F['nq24|TT|0.60']['A'] - 0.9792105130597624) < 1e-13
       and abs(F['nq24|EE|0.30']['A'] - 0.9808198699226599) < 1e-13
       and abs(F['nq24|EE|0.60']['A'] - 0.9775632099064561) < 1e-13
       and abs(F['lmax18|TT|0.30']['A'] - 0.989186711450227) < 1e-13
       and abs(F['lmax18|TT|0.60']['A'] - 0.9788705787276899) < 1e-13
       and abs(F['lmax18|EE|0.30']['A'] - 0.9805595001057306) < 1e-13
       and abs(F['lmax18|EE|0.60']['A'] - 0.9773942766635267) < 1e-13
       and abs(F['base|TT|0.30']['target_60'] - 0.9891418529) < 1e-13
       and abs(F['base|TT|0.60']['target_60'] - 0.9788502587) < 1e-13
       and abs(F['nq24|TT|0.30']['target_60'] - 0.9899863) < 1e-13
       and abs(F['lmax18|EE|0.30']['target_60'] - 0.980552502) < 1e-13),
      '%d of %d inside %.0e; worst %.6e' % (L['n_hits'], len(F), L['tol'], L['worst_diff']))

# ───────────────────────────────────────────── Ⓒ③ the two that cannot discriminate
check("⛭⛔⛭ `r7885` ** ⑰ Ⓒ③ **TWO OF THE TWELVE LEG-PAIR COMPARISONS CANNOT DISCRIMINATE, AND BOTH "
      "WERE NAMED BEFORE THE FIT: `base`-`lmax18` IN `EE` AT BOTH SUMS** ** ⇒ *** the three legs are "
      "CONVERGENCE VARIANTS, not different repairs, so their separations are small by construction. "
      "Measured here, `base`-`lmax18` separates by `1.696606e-07` in `EE` at `Σ = 0.30` and "
      "`3.427196e-07` at `0.60`, against this seat's own `EE` interpolation floor of `5.307333e-05` "
      "-- `313` and `155` times below it. ** So for those two the agreement with `60` confirms the "
      "BANK READING and not the leg. The other `10` separate above the floors and do bear on the "
      "legs. *** ⌗ *PREDICTION.md named these two, and the figures it expected from `60`'s own "
      "record (`1.582000e-07`, `3.369000e-07`) agree with the measured ones -- so this is a "
      "registered prediction met, not a caveat found afterwards*",
      (L['n_pairs'] == 12 and L['n_unresolvable'] == 2
       and L['unresolvable_keys'] == ['base-lmax18|EE|0.30', 'base-lmax18|EE|0.60']
       and abs(S['base-lmax18|EE|0.30']['mine'] - 1.6966058102863002e-07) < 1e-18
       and abs(S['base-lmax18|EE|0.60']['mine'] - 3.4271959004072983e-07) < 1e-18
       and S['base-lmax18|EE|0.30']['mine'] < L['floors']['EE']
       and S['base-lmax18|EE|0.60']['mine'] < L['floors']['EE']
       and abs(L['floors']['EE'] - 5.307332502169082e-05) < 1e-18
       and abs(L['floors']['TT'] - 3.515263913511646e-06) < 1e-18
       and all(v['resolvable'] for k, v in S.items() if k not in L['unresolvable_keys'])),
      '%d of %d resolvable; the %d that are not: %s'
      % (L['n_pairs'] - L['n_unresolvable'], L['n_pairs'], L['n_unresolvable'],
         ', '.join(L['unresolvable_keys'])))

# ───────────────────────────────────────────── Ⓓ④ the joint bar
check("⛭⛭⛭ `r7885` ** ⑰ Ⓓ④ **ALL THREE LEGS ARE INSIDE `69`'s `0.03` ON THIS FITTER TOO, SO `60`'s "
      "VERDICT Ⓐ IS NOW **JOINT ON TWO FITTERS**** ** ⇒ *** worst `|A − 1|` is `0.022606` for "
      "`base`, `0.022437` for `nq24` and `0.022606` for `lmax18`, every one of them at `EE` at "
      "`Σ = 0.60` and every one inside the bar. ** `69` stated the verdict is joint only on two "
      "fitters; this is the second, and it agrees. *** ⌗ *the bar is `69`'s and unchanged from "
      "`r7879`, where no decomposition leg could meet it -- the hierarchy legs meet it with a third "
      "of the bar to spare*",
      (L['all_legs_within_bar'] is True
       and L['verdict_A_joint_on_two_fitters'] is True
       and abs(L['bar'] - 0.03) < 1e-12
       and abs(BR['base']['worst'] - 0.0226060660560633) < 1e-15
       and abs(BR['nq24']['worst'] - 0.022436790093543935) < 1e-15
       and abs(BR['lmax18']['worst'] - 0.02260572333647326) < 1e-15
       and all(v['passes'] for v in BR.values())
       and all(v['worst_key'] == 'EE|0.60' for v in BR.values())
       and all(v['within_bar'] for v in F.values())),
      'base %.6f, nq24 %.6f, lmax18 %.6f, all at %s, all inside %.2f'
      % (BR['base']['worst'], BR['nq24']['worst'], BR['lmax18']['worst'],
         BR['base']['worst_key'], L['bar']))

# ───────────────────────────────────────────── Ⓔ⑤ the regression control
check("⛭⛭ `r7885` ** ⑰ Ⓔ⑤ **THE INSTRUMENT IS PROVED THE SAME AS `r7875`'s AT EXACTLY ZERO, BEFORE "
      "ANY VALIDATION LEG IS READ** ** ⇒ *** the harness imports that fitter and CAMB leg through "
      "`r7879` and `r7877` rather than copying them, and re-derives `r7875`'s four landed amplitudes "
      "at `0.0` -- not approximately, exactly. ** The control runs FIRST and the driver returns "
      "without reading a leg if it fails, so no agreement below can come from a drifted instrument. "
      "*** ⌗ *a copied fitter could reproduce its ancestor's numbers and still differ where it meets "
      "new legs, which is why this is an import and not a copy*",
      (L['regression_worst'] == 0.0 and L['legs_read'] is True),
      'regression worst %.1f, exactly zero; legs read %s'
      % (L['regression_worst'], L['legs_read']))

# ───────────────────────────────────────────── Ⓕ⑥ what this does not establish
check("⛭⛔⛭ `r7885` ** ⑰ Ⓕ⑥ **WHAT THIS DOES **NOT** ESTABLISH** ** ⇒ *** that a second fitter "
      "agrees with `60` on twelve numbers says the NUMBERS are right. It does not say the "
      "hierarchy is the right physics, and it cannot say the three convergence legs differ from one "
      "another, because `Ⓒ③` shows two of their comparisons sit below this seat's resolution. ** "
      "`ε` is reported (`-0.00161222` to `0.00348115`) and is never used to decide any verdict here, "
      "because it is a grid quantity on this fitter. **⛔ No limit is read: nothing in this revision "
      "licenses one.** *** ⌗ *stated because 'confirmed on two fitters' is the kind of phrase that "
      "travels further than what it was measured on*",
      (abs(min(L['eps'].values()) + 0.0016122250000000042) < 1e-15
       and abs(max(L['eps'].values()) - 0.003481150000000003) < 1e-15
       and L['n_unresolvable'] == 2),
      'eps %.8g .. %.8g, reported only; %d comparisons below resolution'
      % (min(L['eps'].values()), max(L['eps'].values()), L['n_unresolvable']))

# ───────────────────────────────────────────── the count
check("⛭ `r7885` ** ⑰ Ⓖ⑦ THE ARMS ABOVE ARE **ALL OF THEM** ** ⇒ *** six arms precede this one: "
      "the legs and the shared zero, the twelve fits, the two comparisons that cannot discriminate, "
      "the joint bar, the regression control, and what this does not establish. ** Nothing is "
      "computed in this file. *** ⌗ *the count is pinned so an arm cannot be dropped silently*",
      _n[0] == 6 and _fail[0] == 0,
      '%d arm(s) before this one, %d failed' % (_n[0], _fail[0]))

print()
print('  %d arm(s), %d failed' % (_n[0], _fail[0]))
print('=' * 100)
raise SystemExit(1 if _fail[0] else 0)
