"""r7853+cc66 item ③: bank 60's `phi_shape(4000)` transfer under `BVEL=1`, the REPAIRED solver.

`r7851` banked the pre-repair transfer because it costs ~608 s over 220 modes.  This does the same
for the repaired one, and records what `r7851`'s bank did NOT: the state width `NV` and the baryon
slot `I_DB`, because 60's repair MOVES THE STATE LAYOUT and `phiphi.phi_shape` reads slot 6 with a
hardcoded index.

** THE SLOT IS VERIFIED, NOT ASSUMED. **  60's own `repair.py` reads `Y[:, :, 6]` on both sides of
the repair, so slot 6 is expected to still be `Phi` -- but a hardcoded index into a state whose
layout moved is exactly the class of error that nearly broke `r7851` twice, so this records `NV`
and `I_DB` and the caller checks `Phi(k -> 0)` against the analytic `-9/10`.

Run: BVEL=1 python3 -I make_repaired_bank.py            (writes phi60_transfer_eta4000_bvel1.npz)
     BVEL=0 python3 -I make_repaired_bank.py --probe     (2 modes, just to read NV and I_DB)
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.abspath(os.path.join(HERE, '..'))
R46 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')

PROBE = '--probe' in sys.argv
BVEL = os.environ.get('BVEL', '0')
ETAREF = 4000.0

sys.path.insert(0, R46)
import phiphi as PP                                                          # noqa: E402

A = PP.A
NKP = 2 if PROBE else PP.NKP
kk = np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), NKP)
etas = np.array([ETAREF])

print('  BVEL=%s  NKP=%d  eta_ref=%.0f Mpc' % (BVEL, NKP, ETAREF), flush=True)
sol, nk, NV = A.evolve(kk, t_eval=etas, e_end=ETAREF)
Y = sol.y.T.reshape(len(etas), nk, NV)
I_DB = int(getattr(A, 'I_DB_F', -1))
print('  state: nk=%d  NV=%d  I_DB=%d  A.BVEL=%s'
      % (nk, NV, I_DB, getattr(A, 'BVEL', '?')), flush=True)

Phi = np.asarray(Y[0, :, 6], float)
print('  slot 6 at the super-horizon end: %.6f   (the analytic value is -0.9)' % Phi[0], flush=True)

if not PROBE:
    out = os.path.join(HERE, 'phi60_transfer_eta4000_bvel%s.npz' % BVEL)
    np.savez_compressed(out, kk=kk, Phi=Phi, NV=NV, I_DB=I_DB, bvel=int(BVEL))
    print('  wrote %s' % os.path.basename(out), flush=True)
