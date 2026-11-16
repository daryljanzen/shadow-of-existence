"""Bank r7809's omega_m response (control, five Omega_m at fixed h via LOM, summed over KSLICE pieces) into
spectra/r7809_omm_response_lcdm.npz, in the layout of r6897_wb_response_lcdm.npz so 60's harness reads
it the same way: ls__<omega_m>, Dl__<omega_m> (omega_m = Omega_m h^2), nsl__, lA__, rs__, DM__, config__, plus 'omega_m', 'Omega_m' and 'missing'.
Also checks the centre against r6897's banked centre spectrum (the same run but for the knob)."""
import os, glob, json, numpy as np
SP = '/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
D = '/tmp/n70/r7809/omm'; H = 0.67410309
DN = ['0.28504', '0.297433', '0.309826', '0.322219', '0.334612']; NEXP = len(range(0, 2547, 250))
def ok(lg):
    return os.path.exists(lg) and any(L.startswith('__DONE__ rc=0') for L in open(lg))
W = {}; miss = []
for dn in DN:
    sl = sorted(glob.glob(f'{D}/omm{dn}_k*.npz'), key=lambda q: int(q.split('_k')[-1][:-4]))
    sl = [q for q in sl if ok(q[:-4] + '.log')]
    if len(sl) != NEXP:
        miss.append(f'{dn}:{len(sl)}/{NEXP}'); continue
    ls = None
    for q in sl:
        d = np.load(q, allow_pickle=True)
        if ls is None: ls = d['ls'].astype(np.int32); tot = np.zeros(len(ls))
        assert np.array_equal(d['ls'].astype(np.int32), ls)
        tot = tot + d['Dl'].astype(np.float64)
    d0 = np.load(sl[0], allow_pickle=True); key = f'{float(dn) * H * H:.6f}'
    cfg = json.loads(str(d0['config'])) if 'config' in d0.files else {}
    W[f'ls__{key}'] = ls; W[f'Dl__{key}'] = tot; W[f'nsl__{key}'] = np.int32(len(sl))
    W[f'lA__{key}'] = np.float64(d0['l_A']); W[f'rs__{key}'] = np.float64(d0['r_s']); W[f'DM__{key}'] = np.float64(d0['D_M'])
    W[f'config__{key}'] = str(d0['config'])
if W:
    W['omega_m'] = np.array(sorted(float(k.split('__')[1]) for k in W if k.startswith('Dl__'))); W['Omega_m'] = W['omega_m'] / H / H
    W['missing'] = np.array(miss, dtype=object)
    # the bank's `config` is the INSTRUMENT's resolved switches (check_banked_config's defining five and
    # the rest, from the centre's own save), with LOM given as the bank's five values and the bank added
    _ck = [k for k in W if k.startswith('config__')]
    _cfg = json.loads(W.get(f'config__{0.309826 * H * H:.6f}', W[_ck[0]]))
    _cfg['LOM'] = [float(x) for x in DN]
    _cfg['bank'] = {'what': 'r7809 omega_m response (Omega_m at fixed h, so Omega_Lambda and D_M move with it), control (lcdm) at r6897 refit background',
                    'LH0': 67.410309, 'WBH2': 0.021966, 'NS': 0.954248,
                    'LSTEP': 8, 'LMAXL': 2000, 'KSLICE': '250 x 11', 'LOM_centre': 0.309826}
    W['config'] = json.dumps(_cfg)
    out = os.path.join(SP, 'r7809_omm_response_lcdm.npz'); np.savez_compressed(out, **W)
    print(f'  {os.path.basename(out)}: omega_m = {list(W["omega_m"])}, missing = {miss}')
    _c = f'{0.309826 * H * H:.6f}'
    if f'Dl__{_c}' in W:
        R = np.load(os.path.join(SP, 'r6897_wb_response_lcdm.npz'), allow_pickle=True)
        assert np.array_equal(R['ls__0.021966'].astype(np.int32), W[f'ls__{_c}'])
        print(f"  centre against r6897's centre (same run but for the knob): max |rel| = "
              f"{np.max(np.abs(W[f'Dl__{_c}'] / R['Dl__0.021966'] - 1)):.2e}")
else:
    print(f'  nothing complete yet: {miss}')
