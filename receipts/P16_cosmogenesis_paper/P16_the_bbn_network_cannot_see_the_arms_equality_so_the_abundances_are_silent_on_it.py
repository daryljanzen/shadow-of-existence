#!/usr/bin/env python3
"""
RECEIPT -- P16/P15: ** THE BBN NETWORK'S BACKGROUND HAS NO MATTER DENSITY IN IT.  SO THE CR ARM'S
EQUALITY -- WHICH DIFFERS FROM LCDM's THROUGH omega_m, NOT THROUGH THE RADIATION -- IS INVISIBLE TO
IT, AND THE ABUNDANCES ARE SILENT ON IT: NEITHER A COST NOR SUPPORT. **

** ⇒ WHAT THE NETWORK DOES SEE IS A Delta N_eff, AND THAT IS A ROUTE THIS ARM DOES NOT TAKE. **
Reaching z_eq = 3447 by adding radiation at fixed T_CMB moves Y_p from 0.2432 to 0.2577 and D/H
from 2.567e-5 to 2.269e-5.  ** Those numbers price a different model.  Quoting them for or against
the CR arm's equality would be scoring it on a parameter it does not move. **

Built r6760+cc66.7 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s amendment 2:
"the BBN table prices the Delta N_eff route only, so the abundances are SILENT on the arm's
equality -- neither cost nor support -- and the structural finding gets its own receipt."

===================================================================================================
** THE ARGUMENT IS STRUCTURAL AND THAT IS WHY IT NEEDS A RECEIPT RATHER THAN A SENTENCE **
===================================================================================================

The CR arm runs at H0 = 73.00, Om = 0.3066, so omega_m = 0.1634 against LCDM's 0.1431 at
H0 = 67.40, Om = 0.3150.  ** With the SAME radiation density, that is the whole of the arm's
equality difference: z_eq = Om/Or - 1 = 3936 against 3447. **  A 14% shift in z_eq, bought
entirely on the matter side.

`computations/p16_bbn/bbn_network.py` integrates the network on
    H(T) = sqrt(8 pi G rho_rad(T) / 3),   rho_rad from g_*(T) = 2 + (7/8)*4*f_e + 3*(7/8)*2*(T_nu/T)^4
with the baryon density entering only through eta10.  ** omega_m is not in it.  z_eq is not in it.
Omega_Lambda is not in it.  Nothing in it knows what the matter density is, because at T > 0.01 MeV
the matter density is fourteen orders of magnitude below the radiation and BBN is over before it
matters. **  *That is not a defect of the network.  It is the correct physics, and it is exactly
why the abundances cannot arbitrate this question.*

  PART 1  ** THE NETWORK'S FREE INPUTS, READ OFF ITS OWN SIGNATURES. **
  PART 2  ** THE BACKGROUND'S SOURCE, GREPPED. **  No matter term, and the check is a check.
  PART 3  ** THE STANDARD RUN REPRODUCED. **
  PART 4  ** THE TWO EQUALITIES, AND THE ABUNDANCES BIT-IDENTICAL ACROSS THEM. **
  PART 5  ** WHAT THE OTHER ROUTE WOULD COST, so the silence is not mistaken for an absence of
          any constraint at all. **

** COMPUTES: eta10 = 6.14, T9 from 9.0 to 0.08, the REACLIB library -- the network's own defaults.
   CR arm H0 = 73.00, Om = 0.3066; control H0 = 67.40, Om = 0.3150; wr = 4.15e-5.  *** The
   Delta N_eff values in PART 5 are DERIVED from the z_eq targets, not chosen: N_eff is solved so
   that Or gives the stated z_eq at the control's omega_m. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy, pynucastro; ~4 min -- it runs the
                                              network three times)
"""
import inspect
import os
import re
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'p16_bbn'))
import bbn_network as BBN                                                  # noqa: E402

WR = 4.15e-5
CR = dict(name='CR arm', H0=73.00, Om=0.3066)
CTL = dict(name='control', H0=67.40, Om=0.3150)
for d in (CR, CTL):
    d['om_m'] = d['Om'] * (d['H0'] / 100) ** 2
    d['z_eq'] = d['Om'] / (WR / (d['H0'] / 100) ** 2) - 1.0

print("=" * 99)
print("  PART 1 -- ** THE NETWORK'S FREE INPUTS **")
print("=" * 99)
for fn in (BBN.build_background, BBN.run):
    sig = inspect.signature(fn)
    print(f"  {fn.__name__}{sig}")
    for nm in sig.parameters:
        if re.search(r'om|omega|matter|z_eq|zeq|lambda|H0', nm, re.I):
            fail.append(f"{fn.__name__} takes '{nm}' -- the premise of this receipt is wrong")
print()
print("  ⇒ eta10, a temperature range, a grid size, a library, and scale factors on the")
print("    reaction rates.  ** No matter density, no equality, no cosmological constant. **")

print()
print("=" * 99)
print("  PART 2 -- ** THE BACKGROUND'S SOURCE **")
print("=" * 99)
src = inspect.getsource(BBN)
for fn in ('gstar', 'rho_rad', 'Hubble', 'build_background'):
    body = re.search(rf'^def {fn}\(.*?(?=^def |\Z)', src, re.M | re.S)
    if body is None:
        fail.append(f"could not read {fn} out of the module")
        continue
    txt = body.group(0)
    bad = [w for w in ('Om', 'omega_m', 'om_m', 'z_eq', 'zeq', 'OmegaL', 'Omega_L', 'rho_m')
           if re.search(rf'\b{re.escape(w)}\b', txt)]
    print(f"  {fn:>18}  {len(txt.splitlines()):>3} lines   matter/equality symbols: "
          f"{bad if bad else 'NONE'}")
    if bad:
        fail.append(f"{fn} mentions {bad} -- the background is not matter-free")
print()
print("  ⌗ and the one density that DOES enter is the baryons', through eta10:")
for ln in src.splitlines():
    if 'eta10' in ln and ('rho_b' in ln or 'nb' in ln or 'n_b' in ln):
        print(f"      {ln.strip()[:92]}")

print()
print("=" * 99)
print("  PART 3 -- ** THE STANDARD RUN, REPRODUCED **")
print("=" * 99)
std = BBN.run(eta10=6.14, verbose=True)
PIN = dict(Yp=0.2432, DH=2.567e-5, He3H=1.044e-5, Li7H=4.461e-10)
for k, want in PIN.items():
    got = std[k]
    if abs(got - want) / want > 0.01:
        fail.append(f"{k} = {got:.4g}, banked {want:.4g}")
print(f"  ⇒ against the banked Yp = {PIN['Yp']}, D/H = {PIN['DH']:.3e}, "
      f"3He/H = {PIN['He3H']:.3e}, 7Li/H = {PIN['Li7H']:.3e}")
if not std['success']:
    fail.append("the network's integration did not succeed")

print()
print("=" * 99)
print("  PART 4 -- ** THE TWO EQUALITIES, AND THE NETWORK CANNOT TELL THEM APART **")
print("=" * 99)
print(f"  {'':>10} {'H0':>7} {'Om':>8} {'omega_m':>9} {'z_eq(leaf)':>11} {'eta10 it implies':>17}")
for d in (CTL, CR):
    print(f"  {d['name']:>10} {d['H0']:>7.2f} {d['Om']:>8.4f} {d['om_m']:>9.4f} "
          f"{d['z_eq']:>11.1f} {'6.14 (unchanged)':>17}")
print(f"\n  ⌗ the two equalities differ by {(CR['z_eq'] / CTL['z_eq'] - 1) * 100:.1f}%, ALL of it on")
print("    the matter side -- and omega_b, which is what BBN reads, is the same in both.")
print()
print("  ** So the abundances at the two equalities are not 'close'.  They are the SAME NUMBERS,")
print("  produced by the same call, because the parameter that differs is not an input. **")
same = BBN.run(eta10=6.14, verbose=False)
for k in PIN:
    if same[k] != std[k]:
        fail.append(f"{k} is not reproducible call-to-call -- PART 4's argument needs it to be")
print(f"  ⌗ re-run, bit-for-bit:  Yp {same['Yp'] == std['Yp']},  D/H {same['DH'] == std['DH']},"
      f"  3He/H {same['He3H'] == std['He3H']},  7Li/H {same['Li7H'] == std['Li7H']}")

print()
print("=" * 99)
print("  PART 5 -- ** WHAT THE OTHER ROUTE WOULD COST **")
print("=" * 99)
print("  Reaching the same z_eq through the RADIATION at fixed T_CMB has nowhere to put the")
print("  excess but the neutrino sector, so it is a Delta N_eff -- and THAT the network sees.")
_g_orig = BBN.gstar
_gs_orig = BBN.gstar_s


def _with_neff(Neff):
    """Replace the hardcoded 3 neutrino species by Neff in BOTH g_* and g_*s."""
    def gstar(T):
        return _g_orig(T) + (Neff - 3.0) * (7.0 / 8.0) * 2.0 * BBN.Tnu_over_T(T) ** 4
    def gstar_s(T):
        return _gs_orig(T) + (Neff - 3.0) * (7.0 / 8.0) * 2.0 * BBN.Tnu_over_T(T) ** 3
    return gstar, gstar_s


print(f"\n  {'target z_eq':>12} {'N_eff needed':>13} {'Y_p':>8} {'D/H':>11} "
      f"{'3He/H':>11} {'7Li/H':>12}")
rows = []
for z_target in (CTL['z_eq'], 3000.0):
    # Or must grow by (1+z_eq_CR)/(1+z_target) at the ARM's omega_m; the excess is neutrinos.
    fac = (1 + CR['z_eq']) / (1 + z_target)
    # Or = Og (1 + 0.2271 Neff); solve Neff so Or scales by fac, with Or/Og = 1.6918 at Neff = 3.
    r3 = 1.0 + 0.2271 * 3.0
    Neff = (fac * r3 - 1.0) / 0.2271
    BBN.gstar, BBN.gstar_s = _with_neff(Neff)
    try:
        r = BBN.run(eta10=6.14, verbose=False)
    finally:
        BBN.gstar, BBN.gstar_s = _g_orig, _gs_orig
    rows.append((z_target, Neff, r))
    print(f"  {z_target:>12.0f} {Neff:>13.3f} {r['Yp']:>8.4f} {r['DH']:>11.3e} "
          f"{r['He3H']:>11.3e} {r['Li7H']:>12.3e}")
print(f"  {CR['z_eq']:>12.0f} {3.0:>13.3f} {std['Yp']:>8.4f} {std['DH']:>11.3e} "
      f"{std['He3H']:>11.3e} {std['Li7H']:>12.3e}   <- the arm, on the matter route")

moved = [abs(r['Yp'] - std['Yp']) / std['Yp'] for _, _, r in rows]
if max(moved) < 0.02:
    fail.append("the Delta N_eff route does not move Y_p either -- PART 5 says nothing")
print(f"\n  ⌗ Y_p moves {min(moved) * 100:.1f}-{max(moved) * 100:.1f}% on the radiation route and")
print("    EXACTLY 0% on the matter route.")

print(f"""
=================================================================================================
  ** THE STATEMENT, IN THE FORM IT MUST BE READ IN **
=================================================================================================

  ⇒ ** THE ABUNDANCES ARE SILENT ON THE CR ARM'S EQUALITY -- NEITHER A COST NOR SUPPORT. **

  *A `sec:tensions` rewritten around rho_r/rho_m ~ 17 may cite the BBN table neither for it nor
  against it.*  The table constrains omega_b and N_eff.  The arm's equality is a statement about
  omega_m, and the network has no omega_m in it.

  ⚠ ** AND THE SILENCE IS NOT A LICENCE. **  It cuts both ways and the second way is the one worth
  writing down: *the corpus has previously read the standard abundances as SUPPORT for the two-rate
  scoping -- "D1 already showed the same two-rate scoping keeps BBN standard".*  ** That reading is
  correct about what it says and must not be stretched: the network coming out standard shows that
  nothing in the two-rate scoping reached the radiation-era expansion, which is a real result.  It
  does not, and cannot, endorse the equality. **
""")

print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
