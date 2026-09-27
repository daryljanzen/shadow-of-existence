"""fold r6925's runs into the banks the receipt reads -- r6925+cc66.43.

  * `r6925_visleaf_{lcdm,cr}.npz` -- the INJECTION under `VISLEAF=1` (the other admissible clock for
    the optical depth) and the REAL reported spectrum under it, so the order's two questions -- what
    it does to the contrast and what it does to the COMB -- are answered off one bank and neither is
    picked over the other.
  * `r6925_geometry.npz` -- d r_s / d chi across the FWHM under BOTH assignments, per arm.  This is
    the answer: 0.396733 -> 0.396957 on the arm, so 12.8 per cent lower becomes 12.7.
  * `r6925_noop.npz` -- `VISLEAF` unset on both arms, AND set on the control, where the rate identity
    makes it bit-identical.  *Two different gates: one that the switch is inert unset, one that it is
    inert on the arm the two clocks coincide on.*
"""
import os, re, subprocess, sys, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6925'
NK = {'lcdm': 2547, 'cr': 1452}

for arm in ('lcdm', 'cr'):
    out = {}
    for tag, sub in (('injvl', 'inj'), ('combvl', 'comb')):
        fs = sorted((int(re.search(r'_k(\d+)$', f[:-4]).group(1)), f)
                    for f in os.listdir(f'{D}/{sub}')
                    if f.startswith(f'{tag}_{arm}_k') and f.endswith('.npz'))
        assert [i for i, _ in fs] == list(range(0, NK[arm], 250)), f'{tag} {arm}: slices {[i for i,_ in fs]}'
        ds = [np.load(os.path.join(D, sub, f)) for _, f in fs]
        ls = ds[0]['ls']
        for d in ds:
            assert np.array_equal(d['ls'], ls), f'{tag} {arm}: slices differ on the multipoles'
        out[f'ls__{tag}'] = ls
        out[f'Dl__{tag}'] = sum(d['Dl'] for d in ds)
        for q in ('l_A', 'D_M', 'r_s', 'arm'):
            out[f'{q}__{tag}'] = ds[0][q]
    np.savez(os.path.join(SP, f'r6925_visleaf_{arm}.npz'), **out)
    print(f'  {arm}: the injection and the real spectrum under VISLEAF=1, '
          f'{len(out["ls__injvl"])} multipoles -> spectra/r6925_visleaf_{arm}.npz')

CODE = '''
import numpy as np, json, ACOUSTIC_two_arm as M
w = M.ETA_LS_W
rs = M.rs_leaf_of if M.LEAFSCALES else M.rs_stack_of
lo, hi = M.ETA_LS - w / 2, M.ETA_LS + w / 2
print("__J__" + json.dumps(dict(
    arm=str(M.ARM), visleaf=bool(M._VISL), eta_ls=float(M.ETA_LS), fwhm=float(w),
    d_rs=float(rs(hi) - rs(lo)), d_chi=float(w), cs=float((rs(hi) - rs(lo)) / w),
    rD=float(np.sqrt(M._kD2inv[M._gi])), R_S=float(M.R_S), l_A=float(M.L_A), D_M=float(M.D_M))))
'''
ENV = {'lcdm': dict(ARM='lcdm', LH0='67.410309', LOM='0.309826', WBH2='0.021966', NS='0.954248'),
       'cr': dict(ARM='cr', CRH0='68.581133', CROM='0.297209', ZSTART='3e7', LEAFSCALES='1',
                  WBH2='0.021524', NS='0.997952')}
geo = {}
for arm, env in ENV.items():
    for v in ('0', '1'):
        r = subprocess.run([sys.executable, '-c', CODE], cwd=os.path.join(HERE, '..'),
                           env={**os.environ, **env, 'VISLEAF': v}, capture_output=True, text=True)
        ln = [x for x in r.stdout.splitlines() if x.startswith('__J__')]
        if not ln:
            sys.exit(f'{arm} VISLEAF={v}: no geometry line\n{r.stderr[-600:]}')
        for k, val in json.loads(ln[0][5:]).items():
            geo[f'{k}__{arm}_{v}'] = np.array(val)
np.savez(os.path.join(SP, 'r6925_geometry.npz'), **geo)
print('  the geometry under both assignments, per arm -> spectra/r6925_geometry.npz')

out = {}
for tag in ('noop_lcdm', 'noop_cr', 'visl_lcdm'):
    d = np.load(f'{D}/noop/{tag}.npz')
    out[f'ls__{tag}'], out[f'Dl__{tag}'] = d['ls'], d['Dl']
np.savez(os.path.join(SP, 'r6925_noop.npz'), **out)
print('  the two no-op gates: 3 spectra -> spectra/r6925_noop.npz')
