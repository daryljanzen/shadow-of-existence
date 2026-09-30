"""Bank what a REGISTERED receipt needs to re-derive the acceptance convergence reading.

** WHY A BANK AND NOT THE GRIDS THEMSELVES. **  `GRIDSAVE` writes 2.1 MB over 24 configurations and those
files are untracked scratch -- so a registered receipt cannot read them, the same wall `r7041+cc66.70`'s
first receipt hit with the 15.5 MB transfer.  *The fix there was to thin the bank and have the receipt
RECOMPUTE against it, and that is the fix here.*

Three files, and the split is deliberate:
  (1) `_sample`  -- the FULL background for four configurations, so `A_l` can be re-derived end to end and
      the `KFAC` axis walked from its own inputs rather than trusted.
  (2) `_Al`      -- the per-multipole `A_l`, the acceptance span, the mode count and the eta count for ALL
      24, so every axis in the reading is present.
  (3) `_digest`  -- sha256 of `k`, `dk`, `eta`, `x0`, `vis` per configuration.
      ⛭ ** A DIGEST IS A STRONGER CARRIER FOR THE INERT CLAIM THAN THE ARRAYS ARE. **  The claim is
      "byte-identical", and a hash is exactly that claim in 32 bytes: it cannot be satisfied by a near
      miss, it makes the claim auditable for as long as the receipt lives, and it does not need the
      2.1 MB it is a statement about.
  plus the five `k0` slices that carry the SPECTRUM-level half of the NK identity and its control -- five
  files of 5.3 kB, which is cheaper than the sentence describing them.
"""
import hashlib
import os

import numpy as np

D = '/tmp/n66/r7041'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
TAGS = ['base', 'kfac26', 'kfac32', 'kfac40', 'nk15', 'nk20',
        'nlos1120', 'nlos2240', 'nlosw9', 'nlosw12', 'nlosf90', 'lstep4']
KEYS = ('k', 'dk', 'eta', 'x0', 'vis')
SAMPLE = [('cr', 'base'), ('cr', 'kfac40'), ('lcdm', 'base'), ('lcdm', 'kfac40')]


def main():
    dig, Al, sample = {}, {}, {}
    for arm in ('cr', 'lcdm'):
        for t in TAGS:
            g = f'{D}/grid/g_{arm}_{t}.npz'
            a = f'{D}/acc_cache/a_{arm}_{t}.npz'
            if not (os.path.exists(g) and os.path.exists(a)):
                print(f"  ⛔ missing {arm}/{t} -- bank NOT written")
                return 1
            gd, ad = np.load(g), np.load(a)
            for q in KEYS:
                dig[f'{arm}_{t}_{q}'] = hashlib.sha256(
                    np.ascontiguousarray(gd[q]).tobytes()).hexdigest()
            dig[f'{arm}_{t}_r_s'] = f"{float(gd['r_s']):.17g}"
            for q, v in (('A', ad['A']), ('wd', ad['wd']), ('ls', ad['ls'])):
                Al[f'{arm}_{t}_{q}'] = np.asarray(v)
            Al[f'{arm}_{t}_n'] = np.array([int(gd['n_modes']), int(gd['nlos'])])
            Al[f'{arm}_{t}_span'] = np.array([float(ad['span'])])
            if (arm, t) in SAMPLE:
                for q in KEYS + ('r_s', 'l_A'):
                    sample[f'{arm}_{t}_{q}'] = np.asarray(gd[q])
    np.savez_compressed(os.path.join(OUT, 'r7041_accept_digest.npz'), **dig)
    np.savez_compressed(os.path.join(OUT, 'r7041_accept_Al.npz'), **Al)
    np.savez_compressed(os.path.join(OUT, 'r7041_accept_sample.npz'), **sample)
    # the spectrum-level half of the NK identity, and the control that makes it a reading
    sl = {}
    for nm, p in (('arm_base', 'real/real_cr_base_k0'), ('arm_nk15', 'real/real_cr_nk15_k0'),
                  ('arm_nk20', 'real/real_cr_nk20_k0'),
                  ('ctl_nk15', 'inj/inj_fixed_lcdm_nk15_k0'),
                  ('ctl_nk20', 'inj/inj_fixed_lcdm_nk20_k0')):
        d = np.load(f'{D}/{p}.npz')
        sl[f'{nm}_Dl'], sl[f'{nm}_ls'] = np.asarray(d['Dl']), np.asarray(d['ls'])
    np.savez_compressed(os.path.join(OUT, 'r7041_accept_nk_slices.npz'), **sl)
    for f in ('digest', 'Al', 'sample', 'nk_slices'):
        p = os.path.join(OUT, f'r7041_accept_{f}.npz')
        print(f"  banked {os.path.basename(p):32s} {os.path.getsize(p) / 1024:7.1f} kB")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
