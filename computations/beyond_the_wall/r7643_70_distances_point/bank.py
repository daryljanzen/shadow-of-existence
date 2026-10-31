"""r7643+70: fold the r7643 bank (launch.sh).

  ① the no-fit configuration on the arm of record -- the distances' point with LEAFREC=1:
       refit_grid185_leafrec1_distances/cr_*.npz, refit_grid_leafrec1_distances/cr_*.npz (namesakes' file names),
       spectra/cc66_cr_x_{h686_L2000,h686_pol,h6862_pol}_leafrec1_distances.npz;
     gate: the no-fit base differs from refit_grid185_leafrec1/cr_base.npz by > 1 Mpc in D_M.
  ② the key family: spectra/<name>_leafrec1.npz = the namesake's keys UNCHANGED plus arm-of-record keys with the arm
     token `cr` -> `cr_leafrec1` (noop: r6897/r6911/r6915/r6919/r6925/r6929; geometry: r6919/r6925/r6929; fields:
     r6897); spectra/c54.178_cr_leafrec1_distances.npz (the crossing receipt's own definition, LEAFREC=1).
  ③ 60's 24th Layer-2 reading: r6941_fine_cr rebuilt at its own configuration (LEAFREC=0) from six slices, compared
     with the namesake as 60's layer2.py does (its own `rel_of`, lifted).
Run with STAGE=geometry to bank the geometry family alone (it needs no instrument run)."""
import ast
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank4')
AR = dict(ARM='cr', CRH0='68.570730', CROM='0.291246', ZSTART='3e7', LEAFSCALES='1', LEAFREC='1', WBH2='0.021643',
          NS='1.015066')
MAN, fail, report = {}, [], []


def relabel(key):
    """The arm token `cr` -> `cr_leafrec1`, wherever it is the arm in a key (`x__cr`, `x__cr_0`, `x__noop_cr`)."""
    a, b = key.split('__', 1)
    return a + '__' + re.sub(r'(^|_)cr(?=$|_)', r'\1cr_leafrec1', b, count=1)


def manifest(path, namesake, switches, held, point):
    return dict(file=os.path.relpath(path, BW), namesake=os.path.relpath(namesake, BW), LEAFREC=1, point=point,
                switches=switches, held=held)


def save(path, out, man):
    if 'config' in out and not json.loads(str(out['config'])).get('LEAFREC'):
        fail.append(f'{os.path.basename(path)}: config LEAFREC not true')
    out['manifest'] = np.array(json.dumps(man))
    np.savez(path, **out)
    MAN[os.path.relpath(path, BW)] = man


def sw(log):
    t = open(log).read()
    if '__DONE__ rc=0' not in t:
        fail.append(f'{os.path.relpath(log, D)}: not __DONE__ rc=0')
    return ' '.join(w for w in next((l for l in t.splitlines() if l.startswith('__SWITCHES__ ')), '_ ?').split()[1:]
                    if not w.startswith(('SAVE=', 'KSLICE=', 'ZPSAVE=')))


def config_of(env):
    r = subprocess.run([sys.executable, '-c', 'import ACOUSTIC_two_arm as M; print("__C__" + str(M._resolved_config()))'],
                       cwd=BW, capture_output=True, text=True, env={**os.environ, **env, 'OMP_NUM_THREADS': '1'})
    return np.array(next(l[5:] for l in r.stdout.splitlines() if l.startswith('__C__')))


def probe(code, env):
    r = subprocess.run([sys.executable, '-c', code], cwd=BW, capture_output=True, text=True,
                       env={**os.environ, **env, 'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1'})
    ln = [x for x in r.stdout.splitlines() if x.startswith('__J__')]
    if not ln:
        sys.exit(f'probe failed\n{r.stderr[-600:]}')
    return json.loads(ln[0][5:])


def lift_code(path):
    """A geometry script's own `CODE` probe string, lifted from its source unchanged."""
    tree = ast.parse(open(path).read())
    return next(n.value.value for n in tree.body if isinstance(n, ast.Assign)
                and getattr(n.targets[0], 'id', '') == 'CODE')


def geometry():
    # r6919: one probe per arm
    old = np.load(os.path.join(SP, 'r6919_geometry.npz'), allow_pickle=True)
    out = {k: old[k] for k in old.files}
    for k, v in probe(lift_code(os.path.join(BW, 'r6919_directions', 'geom.py')), AR).items():
        out[f'{k}__cr_leafrec1'] = np.array(v)
    out['config'] = config_of(AR)
    save(os.path.join(SP, 'r6919_geometry_leafrec1.npz'), out,
         manifest(os.path.join(SP, 'r6919_geometry_leafrec1.npz'), os.path.join(SP, 'r6919_geometry.npz'),
                  ' '.join(f'{k}={v}' for k, v in AR.items()), "r6919 geom.py's probe unchanged; `__cr` keys are the "
                  "namesake's, `__cr_leafrec1` the arm of record's", AR))
    # r6925: the probe under VISLEAF 0 and 1
    old = np.load(os.path.join(SP, 'r6925_geometry.npz'), allow_pickle=True)
    out = {k: old[k] for k in old.files}
    code = lift_code(os.path.join(BW, 'r6925_directions', 'bank.py'))
    for v in ('0', '1'):
        for k, val in probe(code, {**AR, 'VISLEAF': v}).items():
            out[f'{k}__cr_leafrec1_{v}'] = np.array(val)
    out['config'] = config_of(AR)
    save(os.path.join(SP, 'r6925_geometry_leafrec1.npz'), out,
         manifest(os.path.join(SP, 'r6925_geometry_leafrec1.npz'), os.path.join(SP, 'r6925_geometry.npz'),
                  ' '.join(f'{k}={v}' for k, v in AR.items()) + ' VISLEAF=0,1', "r6925 bank.py's probe unchanged; "
                  "`__cr_0/1` the namesake's, `__cr_leafrec1_0/1` the arm of record's", AR))
    # r6929: re-keyed the same way -- the namesake's `__cr` keys kept, the arm of record's under `__cr_leafrec1`
    old = np.load(os.path.join(SP, 'r6929_geometry.npz'), allow_pickle=True)
    prev = np.load(os.path.join(SP, 'r6929_geometry_leafrec1.npz'), allow_pickle=True)   # r7641's arm-of-record values
    out = {k: old[k] for k in old.files}
    for k in old.files:
        if k.endswith('__cr'):
            out[relabel(k)] = prev[k]
    out['config'] = prev['config']
    save(os.path.join(SP, 'r6929_geometry_leafrec1.npz'), out,
         manifest(os.path.join(SP, 'r6929_geometry_leafrec1.npz'), os.path.join(SP, 'r6929_geometry.npz'),
                  ' '.join(f'{k}={v}' for k, v in AR.items()) + ' VISLEAF=<15 values>', "r6929 geom.py's probe "
                  "unchanged (r7641); RE-KEYED r7643: `__cr` keys are now the namesake's, `__cr_leafrec1` the arm of "
                  "record's", AR))
    report.append('geometry family: r6919, r6925, r6929 carry `__cr_leafrec1` keys')


if __name__ == '__main__':
    geometry()
    if os.environ.get('STAGE') != 'geometry':
        # ---- ② the noop family: the namesake's keys plus the arm of record's, re-keyed
        NOOP = {'r6897_noop': {'cr': 'r6897_noop_cr'}, 'r6911_noop': {'noop_cr': 'r6911_noop_cr', 'xsonly_cr': 'r6911_xsonly_cr'},
                'r6915_noop': {'noop_cr': 'r6915_noop_cr'}, 'r6919_noop': {'noop_cr': 'r6919_noop_cr'},
                'r6925_noop': {'noop_cr': 'r6925_noop_cr'},
                'r6929_noop': {'unset_cr': 'r6929_unset_cr', 'zero_cr': 'r6929_zero_cr'}}
        base = np.load(f'{D}/noop/r6915_noop_cr.npz', allow_pickle=True)
        for name, m in NOOP.items():
            old = np.load(os.path.join(SP, name + '.npz'), allow_pickle=True)
            out = {k: old[k] for k in old.files}
            for tag, run in m.items():
                d = np.load(f'{D}/noop/{run}.npz', allow_pickle=True)
                s = sw(f'{D}/noop/{run}.log')
                for q, src in (('ls', 'ls'), ('Dl', 'Dl')):
                    out[relabel(f'{q}__{tag}')] = d[src]
                if f'rc__{tag}' in old.files:
                    out[relabel(f'rc__{tag}')] = np.int32(0)
                out['config'] = d['config']
                if not np.array_equal(d['Dl'], base['Dl']) and 'xsonly' not in run and 'zero' not in run:
                    fail.append(f'{run}: a noop differs from the plain arm at the same grid')
            save(os.path.join(SP, name + '_leafrec1.npz'), out,
                 manifest(os.path.join(SP, name + '_leafrec1.npz'), os.path.join(SP, name + '.npz'), s,
                          'the namesake launcher\'s noop runs (HIER=1 LSTEP=16 LMAXL=500) at the arm of record; '
                          '`__..._cr` keys the namesake\'s, `__..._cr_leafrec1` the arm of record\'s', AR))
        report.append('noop family: every noop run equals the plain arm at the same grid bit for bit '
                      '(xsonly and VISLEAF=0 checked separately below)')
        for run in ('r6911_xsonly_cr', 'r6929_zero_cr'):
            d = np.load(f'{D}/noop/{run}.npz')
            report.append(f'  {run} against the plain arm: bit-identical {np.array_equal(d["Dl"], base["Dl"])}')
        # r6897_fields: ZPSAVE's own output, re-keyed
        old = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
        out = {k: old[k] for k in old.files}
        f = np.load(f'{D}/zp/fields_cr.npz', allow_pickle=True)
        for k in f.files:
            out[f'{k}__cr_leafrec1'] = f[k]
        miss = [k[:-4] for k in old.files if k.endswith('__cr') and k[:-4] not in f.files]
        if miss:
            fail.append(f'r6897_fields: ZPSAVE keys missing {miss}')
        out['config'] = np.load(f'{D}/zp/zp_cr.npz', allow_pickle=True)['config']
        save(os.path.join(SP, 'r6897_fields_leafrec1.npz'), out,
             manifest(os.path.join(SP, 'r6897_fields_leafrec1.npz'), os.path.join(SP, 'r6897_fields.npz'),
                      sw(f'{D}/zp/zp_cr.log'), 'r6897 launch.sh: ZPSAVE at LSTEP=64 LMAXL=2000, the arm of record; '
                      '`__cr` the namesake\'s, `__cr_leafrec1` the arm of record\'s', AR))
        # ---- c54.178 at the crossing point
        d = np.load(f'{D}/x/c54.178_cr.npz', allow_pickle=True)
        PX = dict(CRH0=68.62, CROM=0.2973, ZSTART=3e7, LEAFREC=1, LEAFSCALES='unset (0)')
        save(os.path.join(SP, 'c54.178_cr_leafrec1_distances.npz'), {k: d[k] for k in d.files},
             manifest(os.path.join(SP, 'c54.178_cr_leafrec1_distances.npz'), os.path.join(SP, 'c54.178_cr.npz'),
                      sw(f'{D}/x/c54.178_cr.log'), "the crossing receipt's own definition: the c54.178 command with "
                      "CRH0=68.62, CROM=0.2973, ZSTART=3e7 and nothing else -- LEAFSCALES unset -- with LEAFREC=1", PX))
        # ---- ① the distances' point, LEAFREC=1
        PD = dict(CRH0=68.60, CROM=0.2973, WBH2='built-in', NS='built-in', ZSTART=3e7, LEAFSCALES=1, LEAFREC=1)
        for sub, dest in (('g2000', 'refit_grid185'), ('g1300', 'refit_grid')):
            os.makedirs(os.path.join(BW, dest + '_leafrec1_distances'), exist_ok=True)
            for t in ('cr_base', 'cr_H0p', 'cr_H0m', 'cr_OMp', 'cr_OMm', 'cr_WBp', 'cr_WBm', 'cr_NSp', 'cr_NSm'):
                d = np.load(f'{D}/{sub}/{t}.npz', allow_pickle=True)
                out = {k: d[k] for k in d.files}
                out['switches'] = np.array('__SWITCHES__ ' + sw(f'{D}/{sub}/{t}.log'))
                p = os.path.join(BW, dest + '_leafrec1_distances', t + '.npz')
                save(p, out, manifest(p, os.path.join(BW, dest, t + '.npz'), sw(f'{D}/{sub}/{t}.log'),
                                      f'{dest}/launch.sh verbatim with LEAFREC=1: the NO-FIT configuration on the arm '
                                      'of record (the distances\' point, the built-in omega_b and n_s)', PD))
        for t, pt in (('cc66_cr_x_h686_L2000', 68.60), ('cc66_cr_x_h686_pol', 68.60), ('cc66_cr_x_h6862_pol', 68.62)):
            d = np.load(f'{D}/x/{t}.npz', allow_pickle=True)
            p = os.path.join(SP, t + '_leafrec1_distances.npz')
            save(p, {k: d[k] for k in d.files}, manifest(p, os.path.join(SP, t + '.npz'), sw(f'{D}/x/{t}.log'),
                                                         f'the namesake\'s own point (CRH0={pt}) with LEAFREC=1',
                                                         {**PD, 'CRH0': pt}))
        nf = np.load(os.path.join(BW, 'refit_grid185_leafrec1_distances', 'cr_base.npz'))
        rf = np.load(os.path.join(BW, 'refit_grid185_leafrec1', 'cr_base.npz'))
        dd = abs(float(nf['D_M']) - float(rf['D_M']))
        report.append(f'no-fit base D_M {float(nf["D_M"]):.4f} against the refitted {float(rf["D_M"]):.4f}: |dD_M| = {dd:.4f}')
        if not dd > 1.0:
            fail.append('the no-fit base does not differ from the refitted one')
        # ---- ③ 60's 24th Layer-2 reading
        sl = [np.load(f'{D}/l2/fine_cr_k{i}.npz', allow_pickle=True) for i in range(0, 1452, 250)]
        for i in range(0, 1452, 250):
            sw(f'{D}/l2/fine_cr_k{i}.log')
        reb = dict(ls=sl[0]['ls'], Dl=sum(d['Dl'] for d in sl), l_A=sl[0]['l_A'], D_M=sl[0]['D_M'], r_s=sl[0]['r_s'],
                   config=sl[0]['config'])
        np.savez(os.path.join(HERE, 'r6941_fine_cr_rebuilt_leafrec0.npz'), **reb)
        L2 = os.path.join(BW, [x for x in os.listdir(BW) if x.startswith('r7642_60_')][0], 'layer2.py')
        ns = {'np': np}
        tree = ast.parse(open(L2).read())
        exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'rel_of'],
                                type_ignores=[]), L2, 'exec'), ns)
        old = np.load(os.path.join(SP, 'r6941_fine_cr.npz'))
        same_ls = np.array_equal(old['ls'], reb['ls'])
        rel = float(np.max(np.abs(reb['Dl'] - old['Dl'])) / np.max(np.abs(old['Dl'])))
        try:
            rel60 = ns['rel_of'](os.path.join(SP, 'r6941_fine_cr.npz'), os.path.join(HERE, 'r6941_fine_cr_rebuilt_leafrec0.npz'))
        except Exception as e:                       # noqa: BLE001
            rel60 = f'(rel_of: {e})'
        report.append(f'60\'s 24th: r6941_fine_cr rebuilt at its own configuration (LEAFREC=0, six slices): same ls {same_ls}, '
                      f'max|dDl|/max = {rel:.3e}; layer2.rel_of = {rel60}')
    json.dump(MAN, open(os.path.join(HERE, 'MANIFEST.json'), 'w'), indent=1)
    print('\n'.join(report))
    print(f'{len(MAN)} files banked')
    print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
    sys.exit(1 if fail else 0)
