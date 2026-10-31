#!/usr/bin/env python3
"""r7644 (60) -- THE LENSING OPERATOR, COMPUTED ONCE AND SAVED AS DATA.

** WHY THIS IS A SEPARATE FILE AND A SEPARATE INTERPRETER, AND WHY THAT IS THE CAREFUL CHOICE RATHER
THAN A WORKAROUND. **

cc66's lensed comparison imposes CAMB's FULL lensed/unlensed ratio, and its receipt rejects the
first-order kernel by name -- the kernel reads a spurious +13% at ell = 1900 where the full operator
gives +6.5%.  `camb` is absent from the interpreter this corpus is verified on.

⛔ ** AND INSTALLING IT THERE WOULD HAVE MOVED THE ARITHMETIC UNDER EVERY FLOAT COMPARISON IN THE
CORPUS. **  `pip install camb` pulls a newer `scipy`, and `requirements-ci.txt` and
`receipts/ENV_FINGERPRINT.txt` exist precisely because *"an UNPINNED install moves the arithmetic
under every float comparison in the corpus with no push at all"*.  ⇒ *So the install was deliberately
NOT put on the pinned interpreter's path: it landed under a different Python, `check_env_fingerprint`
stays green, and the scoring interpreter still reports the swept numpy and scipy.*

⇒ ** THE OPERATOR IS AN IMPOSED INPUT AND NOT A FITTED ONE, so it is DATA, and data may be computed
by another interpreter and read as an array. **  This file runs under the Python that has `camb`,
writes the ratio, and is never imported by the scorer.  *The scorer reads the saved array on the
pinned interpreter, so nothing about the score's arithmetic depends on the other install.*

⌗ The cosmology is cc66's own, verbatim from its receipt, so the operator is the same operator:
  H0 = 67.40, ombh2 = 0.02237, omch2 = 0.3150*0.674^2 - 0.02237, mnu = 0.06, omk = 0, tau = 0.054,
  As = 2.1e-9, ns = 0.965, lmax = 3000.
"""
import os

import numpy as np
import camb

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'lensing_operator.npz')

pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * (0.674 ** 2) - 0.02237,
                       mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
lensed, unlens = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
lg = np.arange(len(lensed))
ratio = np.ones_like(lensed)
m = unlens > 0
ratio[m] = lensed[m] / unlens[m]

r1900 = float(np.interp(1900, lg, ratio))
print(f"  camb {camb.__version__}; the operator's lensed/unlensed at ell = 1900: {r1900:.4f}")
print("  ** cc66's receipt gates this into [1.05, 1.08] for the FULL operator, against the")
print("     first-order kernel's spurious ~1.13.  Same gate, stated here. **")
assert 1.05 <= r1900 <= 1.08, f"the operator gives {r1900:.4f}, not the full operator's ~1.065"

np.savez(OUT, ell=lg, ratio=ratio, r1900=r1900, camb_version=camb.__version__,
         cosmology='H0=67.40 ombh2=0.02237 omch2=0.3150*0.674^2-0.02237 mnu=0.06 omk=0 '
                   'tau=0.054 As=2.1e-9 ns=0.965 lmax=3000  (cc66''s own, verbatim)')
print(f"  written: {OUT}")
