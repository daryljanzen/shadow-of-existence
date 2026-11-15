"""Bank r7801's N_eff response (control, five Delta N_eff, summed over KSLICE pieces) into
spectra/r7801_neff_response_lcdm.npz, in the layout of r6897_wb_response_lcdm.npz so 60's harness reads
it the same way: ls__<N_eff>, Dl__<N_eff>, nsl__, lA__, rs__, DM__, config__, plus 'neff' and 'missing'.
Also checks the centre against r6897's banked centre spectrum (the same run but for the knob)."""
import os, glob, json, numpy as np
SP = '/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
D = '/tmp/n70/r7801/neff'; N0 = 3.0
DN = ['-0.5', '-0.25', '0', '0.25', '0.5']; NEXP = len(range(0, 2547, 250))
def ok(lg):
    return os.path.exists(lg) and any(L.startswith('__DONE__ rc=0') for L in open(lg))
W = {}; miss = []
for dn in DN:
    sl = sorted(glob.glob(f'{D}/neff{dn}_k*.npz'), key=lambda q: int(q.split('_k')[-1][:-4]))
    sl = [q for q in sl if ok(q[:-4] + '.log')]
    if len(sl) != NEXP:
        miss.append(f'{dn}:{len(sl)}/{NEXP}'); continue
    ls = None
    for q in sl:
        d = np.load(q, allow_pickle=True)
        if ls is None: ls = d['ls'].astype(np.int32); tot = np.zeros(len(ls))
        assert np.array_equal(d['ls'].astype(np.int32), ls)
        tot = tot + d['Dl'].astype(np.float64)
    d0 = np.load(sl[0], allow_pickle=True); key = f'{N0 + float(dn):.2f}'
    cfg = json.loads(str(d0['config'])) if 'config' in d0.files else {}
    assert cfg.get('DNEFF') == float(dn), (dn, cfg.get('DNEFF'))
    W[f'ls__{key}'] = ls; W[f'Dl__{key}'] = tot; W[f'nsl__{key}'] = np.int32(len(sl))
    W[f'lA__{key}'] = np.float64(d0['l_A']); W[f'rs__{key}'] = np.float64(d0['r_s']); W[f'DM__{key}'] = np.float64(d0['D_M'])
    W[f'config__{key}'] = str(d0['config'])
if W:
    W['neff'] = np.array(sorted(float(k.split('__')[1]) for k in W if k.startswith('Dl__')))
    W['missing'] = np.array(miss, dtype=object)
    W['config'] = json.dumps({'bank': 'r7801 N_eff response, control (lcdm) at r6897 refit background',
                              'LH0': 67.410309, 'LOM': 0.309826, 'WBH2': 0.021966, 'NS': 0.954248,
                              'LSTEP': 8, 'LMAXL': 2000, 'KSLICE': '250 x 11', 'N0_coded': N0})
    out = os.path.join(SP, 'r7801_neff_response_lcdm.npz'); np.savez_compressed(out, **W)
    print(f'  {os.path.basename(out)}: N_eff = {list(W["neff"])}, missing = {miss}')
    if 'Dl__3.00' in W:
        R = np.load(os.path.join(SP, 'r6897_wb_response_lcdm.npz'), allow_pickle=True)
        assert np.array_equal(R['ls__0.021966'].astype(np.int32), W['ls__3.00'])
        print(f"  centre against r6897's centre (same run but for the knob): max |rel| = "
              f"{np.max(np.abs(W['Dl__3.00'] / R['Dl__0.021966'] - 1)):.2e}")
else:
    print(f'  nothing complete yet: {miss}')
