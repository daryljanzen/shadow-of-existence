"""r7865+cc66 item ③: 60's REPAIRED NEUTRINO BACKGROUND AGAINST CAMB, INDEPENDENTLY.

Order r7865 (69): *"ρ_ν(a), H(z) at 0, 1 and 1100, and rdrag at Σ = 0, 0.06, 0.30 and 0.60 eV
against CAMB, independently.  Note that 60 codes N_eff = 3.000 where your reference uses 3.0293.
The control is to be run at DNEFF = +0.0293, so check at that setting."*  Bands Ⓐ-Ⓔ registered at
`r7865+cc66.1` before this file existed.

** INDEPENDENT MEANS THE CAMB LEG IS BUILT HERE, not read out of 60's file. **  Their `validate.py`
records a `rdrag_ref` column and band Ⓐ checks mine against it -- but mine is constructed from the
control's parameters in this file, so an agreement is a reproduction and not a copy.

** AND THE INSTRUMENT LEG CALLS 60's OWN HELPERS rather than a second implementation of them. **
`validate.inst` and `validate.drag` are imported from their module, which has a `__main__` guard, so
importing runs nothing.  ⇒ What this file adds is the comparison, not a rival way of reading the
instrument.

** ⚠ THE ORDER'S `N_eff` FIGURE IS PUT TO A MEASUREMENT RATHER THAN TAKEN. **  The order says the
reference uses `3.0293`.  Read off the CAMB object this reference builds, `N_eff` is `3.044`, with
`num_nu_massless = 2.0293` and one massive neutrino whose contribution is `1.0147` in those units.
⇒ `3.0293` is `2.0293 + 1`: the EFFECTIVE massless count added to the INTEGER massive count.  If
that is where the figure came from, the gap from 60's `3.000` is `0.044` and not `0.0293`, leaving
`0.0147` unaccounted.  ⌗ *So the instrument is run at THREE settings -- `DNEFF` unset, `+0.0293` as
ordered, and `+0.044` -- and which lands closest is reported.  Running only the ordered setting
would have made the answer depend on the figure being right.*

Run: python3 -I check_the_background.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT     # THREE dirnames, asserted
R7864 = os.path.join(BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                          'density_and_both_limits_re_read')
assert os.path.isdir(R7864), R7864
sys.path.insert(0, R7864)
import validate as V                                                        # noqa: E402

SUMS = (0.0, 0.06, 0.30, 0.60)
ZS = (0.0, 1.0, 1100.0)
H = 0.674
SETTINGS = (('unset', {}), ('ordered_0.0293', {'DNEFF': '0.0293'}),
            ('measured_0.044', {'DNEFF': '0.044'}))


def camb_here(sum_ev):
    """the reference leg, BUILT HERE from the control's parameters"""
    import camb
    onu = sum_ev / 93.14 / H ** 2
    p = camb.set_params(H0=67.40, ombh2=0.0224,
                        omch2=(0.3150 - 0.0224 / H ** 2 - onu) * H ** 2,
                        mnu=sum_ev, tau=0.054, ns=0.965, As=2.1e-9)
    b = camb.get_background(p)
    d = b.get_derived_params()
    return dict(rdrag=float(d['rdrag']), zdrag=float(d['zdrag']),
                H=[float(b.hubble_parameter(z)) for z in ZS],
                omnuh2=float(p.omnuh2), Omega_nu=float(p.omnuh2) / H ** 2,
                N_eff=float(p.N_eff), num_massless=float(p.num_nu_massless),
                num_massive=int(p.num_nu_massive))


def main():
    out = {'camb_here': {}, 'instrument': {}, 'order_figure': {}}

    print('  Ⓐ THE REFERENCE LEG, BUILT HERE, AGAINST 60\'s RECORDED `rdrag_ref`')
    print('  ' + '-' * 96)
    sixty = {r['sum']: r for r in json.load(
        open(os.path.join(R7864, 'validate.json')))['reference']['rdrag']}
    worst_a = 0.0
    for s in SUMS:
        c = camb_here(s)
        out['camb_here']['%.2f' % s] = c
        theirs = sixty[s]['rdrag_ref']
        rel = abs(c['rdrag'] / theirs - 1.0)
        worst_a = max(worst_a, rel)
        print('    Sum %.2f   mine %12.6f   theirs %12.6f   rel %.3e' % (s, c['rdrag'], theirs, rel))
    out['worst_rel_vs_sixty_camb'] = worst_a
    print('    ⇒ worst %.3e' % worst_a)

    c0 = out['camb_here']['0.06']
    out['order_figure'] = dict(N_eff=c0['N_eff'], num_massless=c0['num_massless'],
                               num_massive=c0['num_massive'],
                               order_says=3.0293, massless_plus_integer=c0['num_massless'] + 1,
                               gap_to_three=c0['N_eff'] - 3.000)
    print('\n  ⚠ THE ORDER\'S `N_eff` FIGURE, MEASURED OFF THE OBJECT THIS REFERENCE BUILDS')
    print('  ' + '-' * 96)
    print('    N_eff %.6f   massless %.6f   massive %d   massless+1 = %.6f   order says 3.0293'
          % (c0['N_eff'], c0['num_massless'], c0['num_massive'], c0['num_massless'] + 1))
    print('    ⇒ the gap from 60\'s 3.000 is %.6f' % out['order_figure']['gap_to_three'])

    print('\n  Ⓑ Ⓒ Ⓓ Ⓔ THE INSTRUMENT AT THREE SETTINGS')
    print('  ' + '-' * 96)
    for name, extra in SETTINGS:
        rows, rho = [], None
        for s in SUMS:
            env = dict(extra); env.update(NUFD='1', MNU=repr(s))
            d = V.drag(env)
            c = out['camb_here']['%.2f' % s]
            rows.append(dict(sum=s, r_drag=float(d['r_drag']), camb=c['rdrag'],
                             rel=float(d['r_drag']) / c['rdrag'] - 1.0))
            if abs(s - 0.06) < 1e-9:
                i = V.inst(env, V.WANT)
                rho = dict(onu=i['Onu'][0], camb=c['Omega_nu'],
                           rel=abs(i['Onu'][0] / c['Omega_nu'] - 1.0),
                           H=i['Hphys'][:1] + [i['Hphys'][1]] + [i['Hphys'][2]])
        gaps = [r['rel'] for r in rows]
        out['instrument'][name] = dict(rows=rows, rho=rho,
                                       all_above=bool(all(g > 0 for g in gaps)),
                                       monotone=bool(all(gaps[i + 1] > gaps[i]
                                                         for i in range(len(gaps) - 1))),
                                       worst_abs_gap=max(abs(g) for g in gaps))
        print('    %-16s gaps %s   all above %s   monotone %s   rho rel %s'
              % (name, ['%+.3e' % g for g in gaps], out['instrument'][name]['all_above'],
                 out['instrument'][name]['monotone'],
                 ('%.3e' % rho['rel']) if rho else '-'), flush=True)

    best = min(out['instrument'], key=lambda k: out['instrument'][k]['rho']['rel'])
    out['closest_on_density'] = best
    print('\n    ⇒ closest on the density at Sum = 0.06: %s' % best)
    json.dump(out, open(os.path.join(HERE, 'background_check.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
