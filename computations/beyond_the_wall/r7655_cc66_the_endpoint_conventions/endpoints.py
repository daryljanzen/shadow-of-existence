"""r_D UNDER EVERY DEFENSIBLE ENDPOINT CONVENTION -- r7655 (cc66), 69's item 1.

** THIS SCRIPT EXISTS BECAUSE THE INSTRUMENT MUST NOT BE TOUCHED, AND THAT IS A MEASURED
CONSTRAINT RATHER THAN A PREFERENCE. **  The first version of this work added two prints to
`ACOUSTIC_two_arm.py`.  They were additive and changed no physics -- and they still broke
`P15_the_1p57_has_no_parameter_address...`, whose gate ⓿⓿ asserts
`_snap['instrument_blob'] == _BCFG['instrument_blob']`: the git blob hash of the instrument that
RAN against the one stored in the bank it produced.  ⇒ *An additive print is a different instrument
by that standard, and the standard is right: a bank's provenance is the file that made it, not the
file's intentions.  So the measurement moves out of the instrument and into a reader of it.*

** HOW IT GETS THE ENDPOINTS WITHOUT RE-IMPLEMENTING ANYTHING. **  `main()` is guarded by
`if __name__ == '__main__':`, while the background -- the opacity, the visibility, and the
cumulative diffusion integral `kD2inv_of` -- is built at MODULE level.  So importing the instrument
runs exactly the part this needs and none of the spectrum, and every quantity below is the
instrument's own object: no copy, no re-derivation, nothing to drift.
   ⌗ *The import also emits the instrument's own `diffusion: r_D at the visibility peak = X Mpc`
     line, so a log banked from this script carries BOTH that line and the table, which is what
     the receipt's Ⓗ① checks against the production banks' 7.10 / 7.12 / 7.26.*

Run it as the launcher does, with the arm's switches in the environment.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np                                                          # noqa: E402
import ACOUSTIC_two_arm as A                                                # noqa: E402

# Every endpoint a reader of this instrument could defensibly call "the" diffusion length, with the
# instrument's own names for them.  `_half` is its FWHM mask; `_tau` its optical depth, zero today.
_EDGES = A._egrid[A._half]
_ENDPOINTS = [('eta_rec (fixed A_REC)', A.eta_rec),
              ('visibility peak', A.ETA_LS),
              ('visibility FWHM, early edge', float(_EDGES[0])),
              ('visibility FWHM, late edge', float(_EDGES[-1])),
              ('tau = 1', float(np.interp(1.0, A._tau[::-1], A._egrid[::-1]))),
              ('today (eta_0)', A.eta_0)]

print("  diffusion: r_D by ENDPOINT CONVENTION (r7655, cc66 -- read off the instrument by import; "
      "the line above is its own, at two decimals, and is untouched)")
for _nm, _e in _ENDPOINTS:
    _r = float(np.sqrt(A.kD2inv_of(_e)))
    print(f"      r_D at {_nm:30s} eta = {_e:9.3f}   r_D = {_r:12.6f} Mpc"
          f"   r_D/D_M = {_r / A.D_M:.8e}")
