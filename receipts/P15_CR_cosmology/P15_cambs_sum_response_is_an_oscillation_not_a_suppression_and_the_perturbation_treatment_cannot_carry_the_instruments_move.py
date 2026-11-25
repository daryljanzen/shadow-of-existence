# -*- coding: utf-8 -*-
"""⛭⛔⛭ `r7871+cc66` ** ⑩ CAMB's SUM RESPONSE AT FIXED PARAMETERS **IS READABLE** WHERE `r7869`'s
PER-BIN SHARE WAS NOT -- BUT IT IS NOT A SUPPRESSION: IT **OSCILLATES**, CHANGING SIGN `11`-`13`
TIMES ACROSS `60`'s RANGE WITH ABOUT HALF THE MULTIPOLES POSITIVE, SO WHAT GROWS WITH `Σ` IS THE
**ENVELOPE**. ⛔ AND THE PERTURBATION TREATMENT **CANNOT CARRY `60`'s MOVE**: CAMB's FOUR
`MassiveNuMethod` SETTINGS SPAN `7.306e-08` IN THE RATIO -- WITH THE KNOB **PROVED LIVE** FIRST **

COMPUTES: nothing.  Every figure is read out of the two JSON records this revision's drivers wrote
(`sum_response.json`, `method_is_live.json`).  No parameter is pinned here.

⌗ `Ⓓ④` IS REFUTED AND `Ⓔ⑤` PASSES FOR THE WRONG REASON, both named as such below.  The registration
expected a monotone suppression; the response is an acoustic-peak SHIFT, which follows from holding
`H0`, `Ω_m`, `ω_b` and `n_s` fixed while adding `Σ` -- the angular scale moves.  That was a wrong
expectation about the physics, not a measurement that came out surprising.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7871_cc66_cambs_sum_response_at_the_spectrum_level')

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

SR = load(os.path.join(MINE, 'sum_response.json'))
ML = load(os.path.join(MINE, 'method_is_live.json'))
OSC = SR['oscillation']

# ───────────────────────────────────────────── Ⓐ① the control is 60's, read not chosen
con = SR['control']
check("⛭ `r7871` ** ⑩ Ⓐ① THE CONTROL IS **60's OWN, READ FROM THEIR MODULE AT RUN TIME** AND NOT "
      "RETYPED -- AND `τ` IS NOT AMONG THE INSTRUMENT'S FOUR, SO IT IS FIXED HERE AND **DECLARED** "
      "** ⇒ *** `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965`, the `lcdm` arm's centre "
      "that 60's four fitted parameters are offsets from. ** 60 profile `τ` over their own range, so "
      "there is no control `τ` to read: it is set to `0.054` here, printed in the output, and "
      "`Ⓒ③` measures whether anything turns on that choice rather than assuming nothing does. *** "
      "⌗ *A control read at run time cannot drift from the instrument's; a retyped one can*",
      (abs(con['H0'] - 67.40) < 1e-9 and abs(con['OM'] - 0.3150) < 1e-9
       and abs(con['WB'] - 0.0224) < 1e-9 and abs(con['NS'] - 0.965) < 1e-9
       and abs(SR['tau'] - 0.054) < 1e-12),
      'control %s; tau %.3f declared; %d multipole(s) %d..%d, unbinned'
      % (con, SR['tau'], SR['n_multipoles'], SR['l_lo'], SR['l_hi']))

# ───────────────────────────────────────────── Ⓑ② the ratio is readable: 69's premise confirmed
check("⛭⛭ `r7871` ** ⑩ Ⓑ② **THE RATIO IS READABLE WHERE `r7869`'s SHARE WAS NOT, AND THAT WAS THE "
      "ORDER'S OWN PREMISE** ** ⇒ *** raising CAMB's `lens_potential_accuracy` from `1` to `3` moves "
      "every TT and EE ratio by at most `9.303e-05`, against a registered band of `1e-03`. ** Set "
      "beside `r7869`: there the per-bin SHARE ran `0.036` to `0.291` with the step, a factor of "
      "eight, and never closed. Here the worst move is four orders below the signal's own envelope. "
      "*** ⌗ *69 reasoned that a ratio at fixed parameters is not a share and cannot depend on a "
      "step. Measured, that is right, and it is the reason this item delivers anything at all*",
      SR['accuracy_move_worst'] < 1e-3,
      'worst accuracy move %.3e against the band 1e-03; smallest envelope measured %.5f'
      % (SR['accuracy_move_worst'], OSC['0.06']['TT']['envelope']))

# ───────────────────────────────────────────── Ⓒ③ it does not turn on my tau
check("⛭ `r7871` ** ⑩ Ⓒ③ AND IT DOES **NOT** TURN ON THE `τ` THIS SEAT HAD TO CHOOSE ** ⇒ *** moving "
      "`τ` by `±0.01` about `0.054` moves every ratio by at most `1.044e-04`, against a registered "
      "`5e-03`. *** ⌗ *Registered because 60 pin no `τ`: a deliverable that moved with it would be "
      "this seat's choice reported as CAMB's answer*",
      SR['tau_move_worst'] < 5e-3,
      'worst tau move %.3e against the band 5e-03' % SR['tau_move_worst'])

# ───────────────────────────────────────────── Ⓓ④ refuted: it is an oscillation
sc = {s: {sp: OSC[s][sp]['sign_changes'] for sp in ('TT', 'EE')} for s in OSC}
check("⛔⛔ `r7871` ** ⑩ Ⓓ④ **REFUTED: THE RESPONSE IS NOT A SUPPRESSION AT ALL -- IT OSCILLATES** ** "
      "⇒ *** across 60's range it changes sign `11`-`13` times in every spectrum at every sum, with "
      "`51`-`59` per cent of multipoles POSITIVE. At `Σ = 0.60` TT runs `+0.0395` at `ℓ = 100`, "
      "`+0.0415` at `500`, `−0.0071` at `1000`, `−0.0473` at `1500`. ** That is an acoustic-peak "
      "**SHIFT**, not a damping, and it follows from the order's own \"at fixed other parameters\": "
      "holding `H0`, `Ω_m`, `ω_b` and `n_s` while adding `Σ` moves the angular scale. ** ✔ **What IS "
      "monotone in `Σ` is the ENVELOPE** -- TT `0.00656 → 0.03427 → 0.06701`, EE `0.01240 → 0.06596 "
      "→ 0.13779`. *** ⌗ *This seat registered \"every ratio negative, monotone in `Σ`\". That was a "
      "wrong expectation about the physics and is recorded as refuted, not softened*",
      (not SR['sign_all_negative'] and not SR['monotone_in_sum']
       and all(11 <= sc[s][sp] <= 13 for s in sc for sp in ('TT', 'EE'))
       and SR['envelope_monotone_in_sum'] is True),
      'sign changes %s; all-negative %s; monotone-in-sum %s; ENVELOPE monotone %s'
      % (sc, SR['sign_all_negative'], SR['monotone_in_sum'], SR['envelope_monotone_in_sum']))

# ───────────────────────────────────────────── Ⓔ⑤ passes for the wrong reason
check("⚠⛔ `r7871` ** ⑩ Ⓔ⑤ **PASSES ARITHMETICALLY AND IS RECORDED AS PASSING FOR THE WRONG REASON** "
      "** ⇒ *** the band asked whether TT's suppression deepens from `ℓ = 100` to `ℓ = 1996`, and "
      "numerically it does -- `+0.00291` against `+0.03950`. ** But `Ⓓ④` shows there is no deepening "
      "suppression to measure: `ℓ = 1996` simply sits near one of the twelve zero crossings, and a "
      "sample a hundred multipoles either side would have given either sign. *** ⌗ ⛔ *A band that "
      "passes by accident of where it was sampled is worth less than one that fails, so it is "
      "reported rather than counted. The repair is `Ⓓ④`'s envelope, which is sample-independent*",
      SR['tt_suppression_grows_with_l'] is True,
      'the arithmetic holds and the quantity does not exist; TT at l=1996 %+.5f against l=100 %+.5f'
      % (SR['standard']['0.6']['TT']['l1996'], SR['standard']['0.6']['TT']['l100']))

# ───────────────────────────────────────────── Ⓕ⑥ the three spectra do not agree
check("⛭⛭ `r7871` ** ⑩ Ⓕ⑥ AND \"THE SUM SUPPRESSES THE SPECTRUM\" IS **EMPHATICALLY NOT ONE "
      "NUMBER**: TT AND EE DISAGREE BY `0.164` ** ⇒ *** the worst TT-EE gap above `ℓ = 1000` at "
      "`Σ = 0.60`, against a registered band of merely `1e-03` somewhere. ** EE's envelope is about "
      "twice TT's at every sum and its oscillation carries one more sign change. *** ⌗ *So a single "
      "scalar \"response to the sum\" is not available at the spectrum level, which is the same "
      "lesson `r7869` learned about a single per-bin share*",
      SR['tt_ee_gap_at_0p60'] > 1e-3,
      'worst TT-EE gap above l=1000 at Sigma=0.60: %.5f; EE envelope %.5f against TT %.5f'
      % (SR['tt_ee_gap_at_0p60'], OSC['0.6']['EE']['envelope'], OSC['0.6']['TT']['envelope']))

# ───────────────────────────────────────────── Ⓖ⑦ the knob, proved live, and the refusal
check("⛭⛭⛔ `r7871` ** ⑩ Ⓖ⑦ THE PERTURBATION TREATMENT **CANNOT CARRY 60's `81.94 → 185.96` meV "
      "MOVE** -- AND THE KNOB IS **PROVED LIVE BEFORE THAT IS CALLED PHYSICS** ** ⇒ *** CAMB's four "
      "`MassiveNuMethod` settings span `7.306e-08` in the ratio: four orders below `Ⓕ⑥`'s `0.164` "
      "and three below `Ⓑ②`'s own accuracy move. ** ⛔ **Four distinct treatments agreeing to one "
      "part in ten million is equally the signature of a knob that never reached the computation** -- "
      "the shape that caught this seat at the spelling-keyed guard, the rounded memo, the summed "
      "cache and the directory list -- so it is established three ways: the setting is read back "
      "after `set_cosmology` AND `set_for_lmax`; the outputs are **not** bit-identical "
      "(`6.149e-06` relative, `Nu_int` against `Nu_approx`); and it scales with the physics it "
      "should, reaching `6.166e-05` at `Σ = 2.0` eV. ** ✔ The coherent reading: the treatments "
      "differ by about `6e-06` in the **SPECTRA** and only `7.306e-08` in the **RATIO**, because the "
      "method's effect cancels between numerator and denominator. *** ⌗ *So the bound is useful, and "
      "more strongly than registered*",
      (SR['method_spread_worst'] < 1e-6 and SR['bound_is_useful'] is True
       and ML['knob_is_live'] is True and ML['bit_identical_at_60s_range'] is False
       and all(ML['survives'].values())
       and ML['probe']['mnu=2'] > ML['probe']['mnu=0.6']),
      'spread %.3e; live %s; bit-identical %s; survives %s; rel at 0.6 eV %.3e -> at 2.0 eV %.3e'
      % (SR['method_spread_worst'], ML['knob_is_live'], ML['bit_identical_at_60s_range'],
         all(ML['survives'].values()), ML['probe']['mnu=0.6'], ML['probe']['mnu=2']))

# ───────────────────────────────────────────── the refusal the order asked for
check("⛔⛭ `r7871` ** ⑩ AND THE SECOND HALF IS **REFUSED AS THE ORDER REQUIRES**: NONE OF CAMB's FOUR "
      "IS 60's INSTRUMENT'S TREATMENT, AND I DID NOT BUILD ONE ** ⇒ *** the order says *\"if CAMB "
      "exposes a way to do that. If it does not, say so; do not build one.\"* The literal answer is "
      "that CAMB exposes a choice among **its own** four treatments -- `Nu_int`, `Nu_trunc`, "
      "`Nu_approx`, `Nu_best` -- which is not the same thing. ** 60's instrument counts the mass as "
      "matter at every epoch (`r7862`) with `NUFD` supplying a Fermi-Dirac **background**; it solves "
      "no neutrino hierarchy at all, and no setting of CAMB's does that. *** ⌗ *What is delivered "
      "instead is the four-way spread as a BOUND, which `Ⓖ⑦` shows is tight enough to settle the "
      "question the order was really asking: the treatment is not where the instrument's move lives*",
      len(SR['methods_available']) == 4 and SR['method_spread_worst'] < SR['tt_ee_gap_at_0p60'],
      'the four CAMB offers: %s; none is the instrument\'s, and none was constructed'
      % SR['methods_available'])

# ───────────────────────────────────────────── every figure the INDEX row prints, pinned here
_pins = {
    'accuracy move 9.303e-05': abs(SR['accuracy_move_worst'] - 9.303e-05) < 5e-9,
    'tau move 1.044e-04': abs(SR['tau_move_worst'] - 1.044e-04) < 5e-8,
    'method spread 7.306e-08': abs(SR['method_spread_worst'] - 7.306e-08) < 5e-12,
    'TT-EE gap 0.16400': abs(SR['tt_ee_gap_at_0p60'] - 0.16400) < 5e-6,
    'TT envelope 0.06 -> 0.00656': abs(OSC['0.06']['TT']['envelope'] - 0.00656) < 5e-6,
    'TT envelope 0.30 -> 0.03427': abs(OSC['0.3']['TT']['envelope'] - 0.03427) < 5e-6,
    'TT envelope 0.60 -> 0.06701': abs(OSC['0.6']['TT']['envelope'] - 0.06701) < 5e-6,
    'EE envelope 0.60 -> 0.13779': abs(OSC['0.6']['EE']['envelope'] - 0.13779) < 5e-6,
    'bit-identity probe 6.149e-06': abs(ML['probe']['mnu=0.6'] - 6.149e-06) < 5e-10,
    'the 2.0 eV probe 6.166e-05': abs(ML['probe']['mnu=2'] - 6.166e-05) < 5e-9,
    'TT at 0.60, l=100, +0.03950': abs(SR['standard']['0.6']['TT']['l100'] - 0.03950) < 5e-6,
    'TT at 0.60, l=1500, -0.04729': abs(SR['standard']['0.6']['TT']['l1500'] + 0.04729) < 5e-6,
}
check("⛭ `r7871` ** ⑩ EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH BY A TWO-SIDED "
      "COMPARISON TO HALF ITS LAST PRINTED DIGIT ** ⇒ *twelve of them: the accuracy and `τ` moves, "
      "the method spread, the TT-EE gap, four envelopes, both liveness probes and two TT samples* "
      "⌗ *A one-sided bound never pins, and this seat's `INDEX` row was caught by "
      "`check_figures_pinned` at `r7861`, `r7863` and `r7865` before `r7869` got it right*",
      all(_pins.values()),
      'pinned %d of %d: %s' % (sum(1 for v in _pins.values() if v), len(_pins),
                               [k for k, v in _pins.items() if not v] or 'all'))

check("⛭ `r7871` ** ⑩ THE COUNT: `5` OF THE `7` REGISTERED BANDS HOLD, `1` IS REFUTED AND `1` PASSES "
      "FOR THE WRONG REASON ** ⇒ *`Ⓐ①` `Ⓑ②` `Ⓒ③` `Ⓕ⑥` `Ⓖ⑦` hold; `Ⓓ④` is refuted because the "
      "response oscillates; `Ⓔ⑤` is satisfied arithmetically on a quantity that does not exist*",
      _n[0] == 9, '%d arm(s) in this receipt; the registration carried 7 bands' % (_n[0] + 1))

print('\n' + '=' * 100)
print('  %s   %d of %d gates;  %d failure(s)'
      % ('OK  ' if not _fail[0] else 'FAIL', _n[0] - _fail[0], _n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
