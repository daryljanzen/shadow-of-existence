"""r7865+cc66 item ③: reduce `background_check.json` to the quantities the bands are about.

Recomputes nothing: the instrument was run twelve times by `check_the_background.py` and the raw
values are in its JSON.  This derives the `H(z)` relative departures, the density ratios and the
ruler's shape per setting, so the receipt pins a record rather than re-deriving them beside it.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ZS = (0, 1, 1100)
SETTINGS = ('unset', 'ordered_0.0293', 'measured_0.044')


def main():
    d = json.load(open(os.path.join(HERE, 'background_check.json')))
    camb = d['camb_here']['0.06']
    out = dict(worst_rel_vs_sixty_camb=d['worst_rel_vs_sixty_camb'],
               order_figure=d['order_figure'], camb_H=camb['H'],
               camb_Omega_nu=camb['Omega_nu'], settings={})
    for name in SETTINGS:
        s = d['instrument'][name]
        hrel = [abs(a / b - 1.0) for a, b in zip(s['rho']['H'], camb['H'])]
        gaps = [r['rel'] for r in s['rows']]
        out['settings'][name] = dict(
            gaps=gaps, all_above=s['all_above'], monotone=s['monotone'],
            worst_abs_gap=s['worst_abs_gap'], rho_rel=s['rho']['rel'],
            H_rel=hrel, H_worst=max(hrel), H_worst_at_z=ZS[hrel.index(max(hrel))],
            n_below=sum(1 for g in gaps if g < 0))
    u, o = out['settings']['unset']['rho_rel'], out['settings']['ordered_0.0293']['rho_rel']
    out['rho_improvement_ordered'] = u / o
    out['rho_improvement_measured'] = u / out['settings']['measured_0.044']['rho_rel']
    out['closest_on_density'] = d['closest_on_density']
    json.dump(out, open(os.path.join(HERE, 'background_read.json'), 'w'), indent=1)
    print('  worst |mine - theirs| on the CAMB leg: %.3e' % out['worst_rel_vs_sixty_camb'])
    print('  order figure: N_eff %.6f, massless %.6f, massless+1 %.6f, order says %.4f, gap %.6f'
          % (out['order_figure']['N_eff'], out['order_figure']['num_massless'],
             out['order_figure']['massless_plus_integer'], out['order_figure']['order_says'],
             out['order_figure']['gap_to_three']))
    for name in SETTINGS:
        s = out['settings'][name]
        print('  %-16s rho %.3e  H worst %.3e at z=%-5d  ruler all-above %s (below at %d)  '
              'monotone %s  worst gap %.3e'
              % (name, s['rho_rel'], s['H_worst'], s['H_worst_at_z'], s['all_above'],
                 s['n_below'], s['monotone'], s['worst_abs_gap']))
    print('  density improves x%.2f at the ordered figure and x%.2f at the measured one'
          % (out['rho_improvement_ordered'], out['rho_improvement_measured']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
