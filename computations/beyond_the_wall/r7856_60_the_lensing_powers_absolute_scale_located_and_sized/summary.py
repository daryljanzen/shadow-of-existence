#!/usr/bin/env python3
"""`r7856` — the five measurements gathered, each keyed to the arm it answers.

Reads the jsons the measuring files wrote; computes nothing of its own except the arm verdicts, so
there is one place the receipt and `RESULT.md` both read and no figure is retyped between them.

Run: python3 summary.py        (writes summary.json)
"""
import io
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def rd(name):
    with io.open(os.path.join(_HERE, name), encoding='utf-8') as fh:
        return json.load(fh)


def main():
    ratio, amp, norm = rd('ratio.json'), rd('amp_twice.json'), rd('normalise.json')
    resid, rep, hand = rd('residual_share.json'), rd('repair_scale.json'), rd('handover.json')
    cmb = rd('cmb_side.json')
    s = {}
    s['O0'] = dict(ratio['control'])
    s['O0b'] = rep['switch']
    s['A1'] = ratio['A1']
    s['A1b'] = ratio['A1b']
    s['A1c'] = dict(as_coded=ratio['A1c'], revisited=norm['A1c_revisited'])
    s['A1d_pre'] = dict(as_measured=amp['A1d_pre'],
                        withdrawn=True,
                        withdrawal='the arm omitted the T_CMB^2 conversion model6.pp_model itself '
                                   'applies, so its conclusion that the two sides were never put '
                                   'on one AMP is withdrawn; handover.py carries the correction')
    s['A1d'] = hand['readings']
    s['B2a'] = dict(share_at_most=resid['shares']['share_radiation_era_at_most'],
                    holds=resid['shares']['A2a_holds'],
                    trend_first=resid['rows'][0]['ratio'], trend_last=resid['rows'][-1]['ratio'],
                    rad_first=resid['rows'][0]['rad_over_mat'],
                    rad_last=resid['rows'][-1]['rad_over_mat'],
                    attribution_refuted=resid['rows'][-1]['ratio'] > resid['rows'][0]['ratio'],
                    confound=resid['confound'])
    s['B2b'] = dict(share=resid['shares']['share_normalisation'],
                    holds=resid['shares']['A2b_holds'],
                    derivation=norm['derivation'],
                    superhorizon_check=norm['vs_reference']['ratio_repaired'][0],
                    mean_ratio_repaired=norm['vs_reference']['mean_ratio_repaired'],
                    mean_ratio_landed=norm['vs_reference']['mean_ratio_landed'])
    s['B2c'] = dict(pair=resid['shares']['pair'], passes=resid['shares']['A2c_passes'],
                    vacuous_by_construction=True,
                    note='share_normalisation was formed as 1 - share_radiation_era, so the pair '
                         'summing to one is an identity and not a measurement; the content is the '
                         'two shares, each measured, with nothing left unaccounted')
    s['C3'] = rep['C3']
    s['C3b'] = rep['C3b']
    s['cancellation'] = hand['cancellation']
    s['D4a'] = cmb['tt_absolute']
    s['D4'] = dict(answered=False, routed=True,
                   reason='the remaining repair is in the SHARED CMB bank, which every CMB score '
                          'in the corpus reads, so it is not "re-run the control only"; it is '
                          'routed as the fork this revision registered, and no limit is reported '
                          'on a configuration this revision reports as wrong by a factor two')
    s['E5'] = dict(arm_of_record_judged=False, p15_touched=False, batch_72_waiting=True,
                   nothing_concluded_about_the_neutrino_mass=True)
    with io.open(os.path.join(_HERE, 'summary.json'), 'w', encoding='utf-8') as fh:
        json.dump(s, fh, indent=1, sort_keys=True)
    print('\n  wrote summary.json: %d arms gathered\n' % len(s))
    for k in sorted(s):
        v = s[k]
        flag = v.get('holds', v.get('passes', v.get('answered', v.get('A1d_passes'))))
        print('   %-10s %s' % (k, '' if flag is None else ('OK' if flag else 'NOT MET')))
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
