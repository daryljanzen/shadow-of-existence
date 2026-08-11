#!/usr/bin/env python3
"""L171_what_sets_the_first_peak.py -- ** WHICH OF ROUTE B'S INPUTS PUTS THE FIRST PEAK AT 150? **

Built r2376+c54.164, working front #5 (`L-171` - `PO-7` - `frontier:scalar`), the two internal
routes to the first acoustic peak: the transfer argument gives 220, `ROBUST_p1p2_scan` gives 150.

** THE METHOD, AND IT IS THE POINT OF THE FILE. **  This does NOT rewrite the disputed calculation.
It EXECS `ROBUST_p1p2_scan.py`'s own source with ONE substitution -- the initial-data block -- so
every other line (background, hierarchy, opacity, damping, discrete ladder, projection) is byte-
identical to the registered receipt.  ** Anything that moves, moves because of the initial data. **

The switch, ICMODE:
  asis        the receipt unmodified -- the control, and it must reproduce 150/360/555/780.
  consistent  Psi's VALUE and its DERIVATIVE taken from the same function.  ** The receipt takes
              Ph0 from the smooth matched envelope 1/(1+xs^2/3) and dPh0 from the numerical
              derivative of the OSCILLATORY 3(sin x - x cos x)/x^3.  Two different functions. **
  flatpsi     Psi flat in k at the entry value, which is what P15 sec:envelope actually claims:
              "all of them reaching the branch point with the same driving amplitude Psi(1/sqrt3)/2".
  zerovel     theta = 0 identically -- the literal reading of the receipt's own docstring,
              "the common phase is taken at an extremum (velocities zero)".

Run:  ICMODE=asis|consistent|flatpsi|zerovel python3 L171_what_sets_the_first_peak.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', 'ROBUST_p1p2_scan.py')

ANCHOR = "    dPh0=-dPl*(kk/np.sqrt(3))                       # d Psi/d eta from C1"

# Injected immediately after the anchor, inside modes_all, where xs/kk/Pl/Ph0/dPh0 are all in scope.
INJECT = '''
    # ---- L171 PROBE, r2376+c54.164: the ONLY departure from the registered receipt ----
    _icm = os.environ.get('ICMODE', 'asis')
    if _icm == 'consistent':
        # Psi' from the SAME envelope Psi came from:  Pl = 1/(1+xs^2/3),  Pl' = -(2xs/3)/(1+xs^2/3)^2
        _dPl_env = -(2.0*xs/3.0)/(1.0+xs**2/3.0)**2
        dPh0 = -_dPl_env*(kk/np.sqrt(3))
    elif _icm == 'flatpsi':
        # sec:envelope: every mode reaches the branch point with the SAME driving amplitude.
        Ph0 = -np.ones_like(kk)/(1.0+(1.0/np.sqrt(3))**2/3.0)
        dPh0 = np.zeros_like(kk)
    elif _icm == 'zerovel':
        dPh0 = np.zeros_like(kk)
    # dg0/th0v are rebuilt from Ph0/dPh0 below, so the switch propagates without further edits.
    # ---------------------------------------------------------------------------------
'''

src = open(RECEIPT, encoding='utf-8').read()
if ANCHOR not in src:
    sys.exit("ANCHOR not found -- the receipt moved; re-point this probe before trusting it.")
src = src.replace(ANCHOR, ANCHOR + INJECT, 1)

# The probe reads the SOURCE extrema, which is the quantity the disagreement is about.
os.environ.setdefault('SRCDIAG', '1')

print()
print("=" * 78)
print(f"  L171 PROBE -- ICMODE = {os.environ.get('ICMODE','asis')}")
print("  ROBUST_p1p2_scan's own source, initial-data block substituted, everything else identical")
print("=" * 78)

g = {'__name__': '__main__', '__file__': RECEIPT}
os.chdir(os.path.dirname(RECEIPT))
exec(compile(src, RECEIPT, 'exec'), g)
