#!/usr/bin/env python3
"""r7641 item 2, grid readers 3 and 4 of 6, together because they read the same two banks.

  reader 3  `P15_the_refit_bound_figures_all_reproduce_…`   -- three configurations
  reader 4  `P15_the_no_fit_confrontation_is_three_per_bin_…` -- the no-fit/refit pair

** THE RESULT IS DIFFERENT FOR THE TWO, AND NEITHER IS A REPETITION OF READERS 1 AND 2. **

  ⒜ ** READER 4 IS BLOCKED, AND ITS OWN GATE IS WHAT DETECTS IT. **  The receipt carries a check
     written for exactly this: *"the two NO-FIT spectra are a different pair from the two refitted
     ones, which is what makes this a second confrontation rather than the same one replotted"*,
     asserting `|D_M(no-fit) - D_M(refit)| > 1.0` on each arm.  On the arm of record the two pointers
     resolve to ONE FILE -- `refit_grid185_leafrec1/cr_base.npz` and
     `spectra/cc66_r185_verify_cr_leafrec1.npz` are bit-identical -- so that difference is `0.0000`
     against the namesake's `5.5819`.  ⇒ *** The receipt's entire subject is the CONTRAST between the
     two confrontations, and on this bank there is only one of them.  I do not have to argue the
     block: the receipt says so, through a gate it already had. ***

  ⛭ ⒝ ** READER 3 IS TWO-THIRDS BLOCKED AND ONE-THIRD READABLE, AND THE READABLE THIRD IS THE ONE
     `r7641` ⑵ IS HELD ON. **  Its three configurations part company:
       * `L2000`  -- `cc66_{lcdm,cr_x_h686}_L2000` -- the arm's sibling EXISTS and sits at the
         DISTANCES' point, so the paper's `214.1 / 550.5 / 2.57` pair IS readable here;
       * `grid base` -- blocked by the centre (readers 1 and 2's ⒜);
       * `r185 verify` -- collapses onto `grid base`, as in ⒜ above.
     ⇒ *So the amended P15 rule's precondition for ⑵ -- that every receipt computing a printed figure
     be re-pointable -- is met for the no-fit pair by this route, and this file reproduces
     `r7641+cc66.30`'s `302.1` and `1.41x` INDEPENDENTLY, from the receipt's own `score`.*

** THE CARRY IS CLASS 3 AND THE REASON IS STRUCTURAL: ** every figure here is a lensed chi^2 of one
spectrum against the Planck bandpowers over 185 bins.  No comb-band ratio, and no control quantity
inside the arm's own score -- gated below by recomputing one from its spectrum and the data alone.

Nothing is edited by this file.  Figures are reported old -> new in `FOR_66.md`.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


import camb                                                               # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237, mnu=0.06,
                     omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]


def score(path):
    """reader 3's own `score`, lifted verbatim: the lensed chi^2 over the section's 185 bins."""
    z = np.load(path, allow_pickle=True)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


def dm_of(path):
    z = np.load(path, allow_pickle=True)
    return float(np.atleast_1d(z['D_M'])[0])


CTL = {'L2000': os.path.join(SP, 'cc66_lcdm_L2000.npz'),
       'grid base': os.path.join(BW, 'refit_grid185', 'lcdm_base.npz'),
       'r185 verify': os.path.join(SP, 'cc66_r185_verify_lcdm.npz')}
ARM = {'namesake': {'L2000': os.path.join(SP, 'cc66_cr_x_h686_L2000.npz'),
                    'grid base': os.path.join(BW, 'refit_grid185', 'cr_base.npz'),
                    'r185 verify': os.path.join(SP, 'cc66_r185_verify_cr.npz')},
       'aor': {'L2000': os.path.join(SP, 'cc66_cr_x_h686_L2000_leafrec1.npz'),
               'grid base': os.path.join(BW, 'refit_grid185_leafrec1', 'cr_base.npz'),
               'r185 verify': os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz')}}
CFGS = ('L2000', 'grid base', 'r185 verify')

print(__doc__)
print(BAR)
print("  PART 1 -- READER 3'S THREE CONFIGURATIONS, SCORED ON BOTH ARMS")
print(BAR)
C = {t: score(CTL[t]) for t in CFGS}
A = {a: {t: score(ARM[a][t]) for t in CFGS} for a in ('namesake', 'aor')}
print(f"    {'configuration':>13} {'control':>9} {'/bin':>6}   {'namesake':>9} {'ratio':>7}   "
      f"{'arm of record':>13} {'ratio':>7}")
for t in CFGS:
    print(f"    {t:>13} {C[t][0]:>9.1f} {C[t][0] / C[t][1]:>6.2f}   {A['namesake'][t][0]:>9.1f} "
          f"{A['namesake'][t][0] / C[t][0]:>6.2f}x   {A['aor'][t][0]:>13.1f} "
          f"{A['aor'][t][0] / C[t][0]:>6.2f}x")
check("all three configurations cover the 185 bins the section names, on every arm",
      all(v[1] == 185 for v in list(C.values()) + [A[a][t] for a in A for t in CFGS]),
      ", ".join(f"{t} {C[t][1]}" for t in CFGS))
check("⛔ THE LICENCE GATE: the namesake arm reproduces the receipt's own published pairs -- the "
      "paper's 214.1 / 550.5 at 1.16 / 2.98 per bin on the L2000 configuration, and the "
      "as-computed 212.9 / 545.8 on the grid base",
      abs(C['L2000'][0] - 214.1) < 0.05 and abs(A['namesake']['L2000'][0] - 550.5) < 0.05
      and abs(C['grid base'][0] - 212.9) < 0.05
      and abs(A['namesake']['grid base'][0] - 545.8) < 0.05,
      f"L2000 {C['L2000'][0]:.1f}/{A['namesake']['L2000'][0]:.1f}, grid base "
      f"{C['grid base'][0]:.1f}/{A['namesake']['grid base'][0]:.1f}")

print()
print(BAR)
print("  PART 2 -- ⒜ READER 4'S OWN GATE DETECTS ITS BLOCK")
print(BAR)
DM = {}
for a in ('namesake', 'aor'):
    DM[a] = (dm_of(ARM[a]['grid base']), dm_of(ARM[a]['r185 verify']))
    same = np.array_equal(np.asarray(np.load(ARM[a]['grid base'])['Dl'], float),
                          np.asarray(np.load(ARM[a]['r185 verify'])['Dl'], float))
    print(f"    {a:>13}: no-fit D_M {DM[a][0]:11.4f}   refit D_M {DM[a][1]:11.4f}   "
          f"|diff| {abs(DM[a][0] - DM[a][1]):9.4f}   spectra identical: {same}")
_cdm = (dm_of(CTL['grid base']), dm_of(CTL['r185 verify']))
print(f"    {'control':>13}: no-fit D_M {_cdm[0]:11.4f}   refit D_M {_cdm[1]:11.4f}   "
      f"|diff| {abs(_cdm[0] - _cdm[1]):9.4f}")
check("⛔⛭⛭ READER 4'S OWN GATE IS WHAT BLOCKS IT: it requires |D_M(no-fit) - D_M(refit)| > 1.0 "
      "on each arm -- *\"which is what makes this a second confrontation rather than the same one "
      "replotted\"* -- and on the arm of record the two pointers are ONE FILE, so the difference is "
      "0.0000 against the namesake's 5.5819 and the control's 89.6908.  ⇒ ** The receipt's whole "
      "subject is the CONTRAST between the two confrontations, and this bank holds only one of "
      "them.  The block is the receipt's own finding, not an argument of mine **",
      abs(DM['aor'][0] - DM['aor'][1]) == 0.0
      and abs(DM['namesake'][0] - DM['namesake'][1]) > 1.0
      and abs(_cdm[0] - _cdm[1]) > 1.0,
      f"arm of record {abs(DM['aor'][0] - DM['aor'][1]):.4f}, namesake "
      f"{abs(DM['namesake'][0] - DM['namesake'][1]):.4f}, control "
      f"{abs(_cdm[0] - _cdm[1]):.4f}")

print()
print(BAR)
print("  PART 3 -- ⛭ ⒝ READER 3'S `L2000` ROUTE *IS* READABLE, AND IT CARRIES ⑵'s HELD PAIR")
print(BAR)
_r_nsk = A['namesake']['L2000'][0] / C['L2000'][0]
_r_aor = A['aor']['L2000'][0] / C['L2000'][0]
print(f"    the paper's no-fit pair on the L2000 configuration:")
print(f"      control {C['L2000'][0]:.1f} ({C['L2000'][0] / 185:.2f}/bin)")
print(f"      namesake {A['namesake']['L2000'][0]:.1f} "
      f"({A['namesake']['L2000'][0] / 185:.2f}/bin)  ->  {_r_nsk:.2f}x")
print(f"      arm of record {A['aor']['L2000'][0]:.1f} "
      f"({A['aor']['L2000'][0] / 185:.2f}/bin)  ->  {_r_aor:.2f}x")
check("⛭⛭ READER 3'S `L2000` CONFIGURATION SITS AT THE DISTANCES' POINT ON BOTH ARMS, so the "
      "paper's `214.1 / 550.5 / 2.57` pair IS readable on the arm of record -- and this reproduces "
      "`r7641+cc66.30`'s `302.1` and `1.41x` INDEPENDENTLY, from reader 3's own `score` rather "
      "than from the lensed-pair instrument.  ⇒ ** So the amended P15 rule's precondition for ⑵ is "
      "MET for the no-fit pair: both receipts that compute it can be read on the arm of record **",
      abs(A['aor']['L2000'][0] - 302.1) < 0.1 and abs(_r_aor - 1.41) < 0.005
      and abs(_r_nsk - 2.57) < 0.005,
      f"arm of record {A['aor']['L2000'][0]:.1f} at {_r_aor:.2f}x, namesake {_r_nsk:.2f}x")
check("⛔ AND READER 3'S OTHER TWO CONFIGURATIONS ARE BLOCKED, which is why it is two-thirds "
      "blocked rather than clear: `grid base` sits at the arm of record's fitted point, and "
      "`r185 verify` is that same file",
      abs(A['aor']['grid base'][0] - A['aor']['r185 verify'][0]) == 0.0
      and abs(A['namesake']['grid base'][0] - A['namesake']['r185 verify'][0]) > 1.0,
      f"arm of record grid base {A['aor']['grid base'][0]:.1f} against r185 verify "
      f"{A['aor']['r185 verify'][0]:.1f}; namesake "
      f"{A['namesake']['grid base'][0]:.1f} against {A['namesake']['r185 verify'][0]:.1f}")

print()
print(BAR)
print("  PART 4 -- THE CARRY")
print(BAR)
_solo = score(ARM['aor']['L2000'])
check("⛭ THE CARRY HAS NOTHING TO ACT ON: every figure here is a lensed chi^2 of ONE spectrum "
      "against the Planck bandpowers over 185 bins, so no control quantity enters the arm's own "
      "score -- recomputing it from the arm's spectrum and the data alone is bit-identical.  ** No "
      "comb-band ratio anywhere: class 3 **",
      _solo == A['aor']['L2000'],
      f"solo {_solo[0]:.6f} against pipeline {A['aor']['L2000'][0]:.6f}")

print()
print(BAR)
print("  PART 5 -- WHAT MOVES, OLD -> NEW")
print(BAR)
ROWS = [('L2000 arm chi^2', A['namesake']['L2000'][0], A['aor']['L2000'][0], '.1f', 1),
        ('L2000 arm per bin', A['namesake']['L2000'][0] / 185, A['aor']['L2000'][0] / 185, '.2f', 1),
        ('L2000 ratio', _r_nsk, _r_aor, '.2f', 1),
        ('grid base arm chi^2', A['namesake']['grid base'][0], A['aor']['grid base'][0], '.1f', 0),
        ('grid base ratio', A['namesake']['grid base'][0] / C['grid base'][0],
         A['aor']['grid base'][0] / C['grid base'][0], '.2f', 0),
        ('r185 verify arm chi^2', A['namesake']['r185 verify'][0],
         A['aor']['r185 verify'][0], '.1f', 0),
        ('no-fit minus refit D_M', abs(DM['namesake'][0] - DM['namesake'][1]),
         abs(DM['aor'][0] - DM['aor'][1]), '.4f', 1)]
print(f"    {'figure':>24} {'namesake':>11} {'arm of record':>14}   verdict")
for lab, o, n, f, readable in ROWS:
    if not readable:
        v = '⛔ NOT COMPARABLE -- different centre / collapsed'
    else:
        v = 'unchanged' if abs(n - o) < 1e-12 else (
            'MOVED' if abs(n - o) > 0.005 * max(1e-12, abs(o)) else 'moved (trace)')
    print(f"    {lab:>24} {format(o, f):>11} {format(n, f):>14}   {v}")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
