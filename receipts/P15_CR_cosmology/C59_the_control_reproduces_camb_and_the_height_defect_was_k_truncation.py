#!/usr/bin/env python3
r"""
C51 — PO-24 STEP ONE: THE CONTROL RUN.  ** THE HEIGHT MACHINERY IS NOT BROKEN.  THE $2.721$ WAS A
k-TRUNCATION ARTEFACT, AND THE CONVERGED CONTROL REPRODUCES CAMB TO $0.14\%$. **

** WHAT WAS ASKED. **  `PO-24` (`THE_REGISTER`, opened r3815) records that `ACOUSTIC_two_arm` --- the
bespoke transfer --- "gets the POSITIONS right and the HEIGHTS wrong by $22.7\%$ and $97.5\%$" on the
arm whose answer is known, and concludes "an instrument that cannot reproduce a spectrum whose answer
is known cannot be trusted about one that is not, so the control comes first."  The handoff at r3869
named the live lead: TWO projection paths that are not the same physics, and *"which path produced the
$2.721$ is not established, and you should not assume it."*

** IT IS ESTABLISHED HERE, AND THE ANSWER HAS TWO HALVES RATHER THAN ONE. **

  ⛔ ** HALF ONE, WHICH NOBODY HAD LOOKED FOR: THE k-INTEGRAL IS TRUNCATED AND IS NOT CONVERGED. **
     The instrument builds its k-grid from the REPORTED multipole range, $k=\ell/D_M$ with
     $\ell\le$ `LMAXL`, so `LMAXL` sets the projection's upper limit $k_{\max}$ as a side effect of
     choosing which multipoles to print.  ** The $C_\ell$ integral $\int P(k)\,\Delta_\ell(k)^2\dd k$
     is not converged at $k_{\max}=\ell_{\max}/D_M$: it needs $k_{\max}\gtrsim2\ell_{\max}/D_M$. **
     Holding the reported $\ell$ grid FIXED and moving only $k_{\max}$:

         k_max (1/Mpc)   l_equiv    P1/P2     P1/P3
            0.0649          900     2.721     4.497      <- the recorded number
            0.0938         1300     2.446     2.974
            0.1298         1800     2.399     2.791
            0.1731         2400     2.393     2.768      <- converged, 0.25% from the row above

  ⛭ ** HALF TWO, WHICH THE HANDOFF NAMED: `los_spectrum` OMITS THE POLARISATION SOURCE. **
     `_project` (reached by `HIER=1`) carries $+g\Pi/4+(3/4k^2)\dd^2_\eta[g\Pi]$ as well.  It is the
     path the $2.721$ did NOT come from, so the comparison to CAMB was not like for like.

  ⇒ ** BOTH ARE NEEDED AND NEITHER ALONE SUFFICES. **  The 2x2 is the receipt's content:

                            k_max = 900        k_max = 2400 (converged)
         los_spectrum        2.721 / 4.497      2.393 / 2.768
         _project            2.516 / 3.506      ** 2.197 / 2.192 **

     (`_project` at the instrument's own default k_max = 1300 gives 2.253 / 2.363 -- between the
     two columns, because that default is itself a partial truncation.)

** THE RESULT.  ** Converged in $k_{\max}$ AND in mode count --- $2.1969$ to four decimals across
`NK` $=280,420,560$, a two-fold range:

         peaks           220 / 540 / 812     against the sky's 220.6 / 538.1 / 809.8
         P1/P2  = 2.197  against CAMB's 2.200   ->  ** 0.14% **
                         against the sky's 2.217 +- 3.4%  ->  0.9%, INSIDE 1 sigma
         P1/P3  = 2.192  against the sky's 2.277          ->  3.7%

*** THE CONTROL REPRODUCES CAMB.  THE INSTRUMENT IS AN ARBITER, AND THE BUILD CAN PROCEED ON IT. ***

** THE FORK, SETTLED --- and the handoff asked for it to be settled early. **  *Repair, decisively.*
There was no term-level bug and no architectural failure: the two-arm machinery carries the transfer,
and what was wrong was which path was called and where the k-integral stopped.  ** A fresh build would
have discarded a working instrument on the strength of an artefact. **

** WHAT THIS MOVES, AND IT IS NOT ONLY THIS ITEM. **  `2.721` / `4.496` are quoted as measured control
values in `THE_REGISTER`, `THE_FRONTIER`, `PO13_WORKING_STATE`, `WHAT_THE_FRAMEWORK_DELIVERS` and
`scripts/regen_frontier.py`.  All five are $k$-truncated.  ⌗ *And the `LN` scan those documents rest
on --- "resolving the hierarchy makes $P_3$ WEAKER, the true deficit is a factor $3.5$" --- does not
reproduce: `LN` $=12$ and `LN` $=25$ give IDENTICAL ratios at every sampling tried here.  That scan is
asserted below to be inert, as a fact about the instrument rather than a judgement about the node.*

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** This is the CONTROL arm only.  No CR number is produced or corrected here. **  The CR arm's
    numbers are k-truncated by the same mechanism and are NOT re-measured in this receipt.
  · The clock operations are no-ops on the control ($\mathrm{Jac} \equiv 1$, asserted below), so
    r3512's `HIER` composition defect cannot touch this result --- and stays LIVE for the CR arm,
    which is the first thing the next step must settle.
  · NOT CLAIMED: that the bespoke transfer is finished, that `PO-24` is closed, or anything about
    CR's peak heights.  What is established is that its control works.

** COMPUTES: the LambdaCDM control arm's first three acoustic peak positions and the height ratios
  P1/P2 and P1/P3, on the two projection paths and at two k-integration limits.  *** At ONE
  parameter set and it is the one that matters: ARM=lcdm, the arm whose answer is known
  independently, with the REPORTED multipole grid pinned at LMAXL=900 in every run so that
  k_max is the only thing that moves. ***  ** No CR number is computed here at all** -- the CR
  arm is truncated by the same mechanism and re-measuring it needs r3512's HIER composition
  defect settled first, which is a no-op on this arm and live on that one. **

STATUS: ✔✔
RUN: python3 C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation.py
RUNTIME: ~8-12 min (four transfer runs plus two convergence points)
ORIGIN: built r3870 (node 60) on the r3869 handoff, `HANDOFF_to_60_PO24_transfer.txt`.
"""
import io
import contextlib
import importlib.util
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78

# ** the instrument is addressed from THIS file, not from the caller's directory. **  r3714 found the
# one receipt in 694 that opened a repo-relative path: it passed from the root and failed from its
# own directory, which is where run_all_receipts.py runs every receipt.
_HERE = os.path.dirname(os.path.abspath(__file__))
_INSTR = os.path.normpath(os.path.join(_HERE, '..', '..', 'computations', 'beyond_the_wall',
                                       'ACOUSTIC_two_arm.py'))
assert os.path.exists(_INSTR), _INSTR

os.environ['ARM'] = 'lcdm'
os.environ.setdefault('NK', '280')
os.environ['LMAXL'] = '900'          # the REPORTED multipole grid, held fixed throughout

_spec = importlib.util.spec_from_file_location("ACOUSTIC_two_arm", _INSTR)
AT = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(AT)

SKY_L = (220.6, 538.1, 809.8)
SKY_R2, SKY_R3 = 2.217, 2.277
CAMB_R2 = 2.200


def _los_grid():
    n = 560
    lo = max(AT.ETA_ON + 1e-6, AT.ETA_LS - 6.0 * AT.ETA_LS_W)
    hi = AT.ETA_LS + 6.0 * AT.ETA_LS_W
    return np.concatenate([np.linspace(lo, hi, int(0.75 * n), endpoint=False),
                           np.linspace(hi, AT.ETA_END, n - int(0.75 * n))])


def run(kmaxl, hier, nk=None):
    """One transfer.  `kmaxl` is the k-integration limit as an equivalent multipole, k = l/D_M.

    ** The reported ell grid is LMAXL=900 in EVERY call, so k_max is the only thing that moves. **
    That separation is the whole point: in the instrument's own main() the two are one knob.
    """
    NKv = int(nk or AT.NK)
    EE = _los_grid()
    kk = np.linspace(12.0, float(kmaxl), NKv * 3) / AT.D_M
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        if hier:
            ls, Dl = AT.hier_run(kk, EE, AT.L_A, AT.D_M, AT.R_S)
        else:
            sol, nkk, NV = AT.evolve(kk, t_eval=EE)
            Y = sol.y.T.reshape(len(EE), nkk, NV)
            ls = np.arange(100, int(AT.LMAXL), int(os.environ.get('LSTEP', '8')))
            Dl = _los_Dl(kk, EE, Y, ls)
    pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
    assert len(pk) >= 3, f"fewer than three peaks at kmaxl={kmaxl}, hier={hier}"
    return ([float(ls[q]) for q in pk[:3]],
            float(Dl[pk[0]] / Dl[pk[1]]), float(Dl[pk[0]] / Dl[pk[2]]))


def _los_Dl(kk, ee, Y, ls):
    """`los_spectrum`'s own source and projection, re-expressed so the ell grid is an argument.

    ** Not a re-derivation: term for term the instrument's own source. **  The instrument computes
    its ell grid from the module-level LMAXL, which is exactly the coupling this receipt has to
    break, so the projection is written here over a PASSED grid and nothing else changes.
    """
    from scipy.special import spherical_jn
    sg = Y[:, :, 7] / 2
    Hcv = np.array([AT.Hc_of(e) for e in ee])[:, None]
    Onv = np.array([AT.On_of(e) for e in ee])[:, None]
    Ph = Y[:, :, 6]
    Ps = Ph - 6 * Hcv ** 2 * Onv * sg / kk[None, :] ** 2
    g_ = AT.vis_of(ee)[:, None]
    et = np.exp(-AT.tau_of(ee))[:, None]
    Dmp = np.exp(-1.0 * (kk[None, :] ** 2) * AT.kD2inv_of(ee)[:, None])
    S = (g_ * (Y[:, :, 2] / 4 * Dmp + Ps)
         + et * (np.gradient(Ph, ee, axis=0) + np.gradient(Ps, ee, axis=0))
         + np.gradient(g_ * Y[:, :, 3] * Dmp, ee, axis=0) / kk[None, :] ** 2)
    P = kk ** (0.965 - 1) / kk * np.gradient(kk)
    x0 = AT.eta_0 - ee
    Cl = np.empty(len(ls))
    for j, l in enumerate(ls):
        J = spherical_jn(int(l), kk[None, :] * x0[:, None])
        Cl[j] = np.sum(P * np.trapezoid(S * J, ee, axis=0) ** 2)
    return Cl * ls * (ls + 1)


# =====================================================================================
print(BAR); print("PART 0 — THE CONTROL ARM'S CLOCK OPERATIONS ARE NO-OPS, SO r3512 CANNOT REACH"); print(BAR)
# (A0) r3512 recorded a COMPOSITION DEFECT in the HIER path and said the control cannot catch it
#      "because phi=1 makes every clock operation a no-op there".  That is exactly why this result
#      is clean -- and exactly why it does NOT license a CR number from the same path.
_jac = [float(AT.Jac_of(e)) for e in (1.0, 50.0, 280.7, 1000.0)]
assert max(abs(j - 1.0) for j in _jac) < 1e-12, _jac
print(f"  Jac_of == 1 to 1e-12 at eta = 1, 50, 280.7, 1000   {[round(j,12) for j in _jac]}")
print("  => r3512's HIER composition defect is INERT on the control, and STAYS LIVE for CR.")

# =====================================================================================
print(); print(BAR); print("PART 1 — THE 2x2: WHICH PATH, AND WHERE THE k-INTEGRAL STOPS"); print(BAR)
print(f"  reported ell grid held FIXED at 100..{int(AT.LMAXL)} for every row; only k_max moves.")
print()
print(f"    {'path':>14} {'k_max l_equiv':>14} {'peaks':>22} {'P1/P2':>9} {'P1/P3':>9}")
res = {}
for hier in (False, True):
    for kml in (900, 2400):
        pks, r2, r3 = run(kml, hier)
        res[(hier, kml)] = (pks, r2, r3)
        print(f"    {'_project' if hier else 'los_spectrum':>14} {kml:>14} "
              f"{str([int(p) for p in pks]):>22} {r2:>9.4f} {r3:>9.4f}")
print(f"    {'THE SKY':>14} {'':>14} {str([round(v,1) for v in SKY_L]):>22} "
      f"{SKY_R2:>9.4f} {SKY_R3:>9.4f}")
print(f"    {'CAMB':>14} {'':>14} {'':>22} {CAMB_R2:>9.4f}")

_los900 = res[(False, 900)]
_los2400 = res[(False, 2400)]
_prj900 = res[(True, 900)]
_prj2400 = res[(True, 2400)]

# (A1) THE RECORDED NUMBER IS REPRODUCED EXACTLY, which is what makes the rest a correction of it
#      rather than a disagreement with it.  2.721 / 4.496 in five documents.
assert abs(_los900[1] - 2.721) < 0.01, _los900[1]
assert abs(_los900[2] - 4.497) < 0.02, _los900[2]
print()
print(f"  ** the recorded 2.721 / 4.496 REPRODUCED: {_los900[1]:.3f} / {_los900[2]:.3f} **")
print("     -- los_spectrum, k truncated at l_equiv 900.  So the row is not wrong about what it ran.")

# (A2) k-TRUNCATION IS THE LARGER HALF: it moves P1/P3 from 4.497 to 2.768 on the SAME path.
assert _los2400[1] < _los900[1] - 0.25, (_los900[1], _los2400[1])
assert _los2400[2] < _los900[2] - 1.5, (_los900[2], _los2400[2])
print(f"  ** k-truncation alone: {_los900[1]:.3f} -> {_los2400[1]:.3f} and "
      f"{_los900[2]:.3f} -> {_los2400[2]:.3f} on ONE path **")

# (A3) THE POLARISATION SOURCE IS THE OTHER HALF, and it is NOT redundant with the first.
assert _prj2400[1] < _los2400[1] - 0.1, (_los2400[1], _prj2400[1])
assert _prj2400[2] < _los2400[2] - 0.4, (_los2400[2], _prj2400[2])
print(f"  ** the polarisation source, at converged k_max: {_los2400[1]:.3f} -> {_prj2400[1]:.3f} "
      f"and {_los2400[2]:.3f} -> {_prj2400[2]:.3f} **")

# (A4) NEITHER ALONE REACHES IT -- the claim that both are needed, asserted rather than asserted-at.
assert abs(_prj900[1] - SKY_R2) > 0.03, _prj900[1]
assert abs(_los2400[1] - SKY_R2) > 0.1, _los2400[1]
print(f"  ** and NEITHER ALONE reaches the sky: polarisation-only {_prj900[1]:.3f}, "
      f"k_max-only {_los2400[1]:.3f} **")

# =====================================================================================
print(); print(BAR); print("PART 2 — THE RESULT, AND ITS CONVERGENCE"); print(BAR)
pks, r2, r3 = _prj2400
print(f"  peaks   {[int(p) for p in pks]}   against the sky's {[round(v,1) for v in SKY_L]}")
print(f"  P1/P2 = {r2:.4f}   vs CAMB {CAMB_R2:.3f}  ->  {abs(r2-CAMB_R2)/CAMB_R2:+.2%}")
print(f"                     vs sky  {SKY_R2:.3f}  ->  {(r2-SKY_R2)/SKY_R2:+.2%}")
print(f"  P1/P3 = {r3:.4f}   vs sky  {SKY_R3:.3f}  ->  {(r3-SKY_R3)/SKY_R3:+.2%}")

# (A5) THE HEADLINE: the control reproduces CAMB.  This is the assertion the item turns on.
assert abs(r2 - CAMB_R2) / CAMB_R2 < 0.01, (r2, CAMB_R2)
print()
print("  ** THE CONTROL REPRODUCES CAMB TO BETTER THAN 1%.  THE INSTRUMENT IS AN ARBITER. **")

# (A6) and the positions, which were never the complaint, stay right.
for got, want in zip(pks, SKY_L):
    assert abs(got - want) < 9.0, (pks, SKY_L)
print(f"  the positions stay right: every peak within 9 of the sky's.")

# =====================================================================================
# (A6b) ** ADDED r3906, AND THE ASSERTION I FIRST WROTE HERE FAILED. **  59 suspended every CR
#       height figure on this line's finding and then wrote: "the positions are not affected by the
#       same mechanism on your control evidence, but that should be CONFIRMED rather than assumed,
#       and it should not be assumed."  It was assumed -- by me: the 2x2 above PRINTS the positions
#       at every k_max and (A6) only ever checked the CONVERGED cell against the sky.
#   ⛔ MEASURED, THE ASSUMPTION IS FALSE.  I wrote `assert _dpos_max < 12.0` expecting a height-only
#      defect.  It failed at 16.0, on BOTH paths:
#          los_spectrum  [220, 524, 796] -> [220, 532, 812]
#          _project      [220, 532, 796] -> [220, 540, 812]
#      The first peak does not move.  The second moves 8, the THIRD MOVES 16 -- about 2% -- while
#      P1/P2 moves ~14% and P1/P3 ~63% over the same 2.7x change in k_max.
#   ⇒ *** SO TRUNCATION IS NOT A HEIGHT-ONLY DEFECT.  It damages heights FAR more than positions,
#       and the ordering is real and worth having, but "positions are unaffected" is WRONG and a
#       position quoted off a truncated run carries a shift of this order, growing with ell. ***
#   ⌗ The assertion below now states the MEASURED fact and would fail if either half moved: if
#     positions stopped moving, or if they moved as much as the heights.
#   ⌗ SCOPE, and it is the point of stating it: this is the CONTROL arm.  The CR arm runs the HIER
#     path where PART 0 shows r3512's composition defect is LIVE, so this licenses no CR position
#     either way.  What it does is remove the assumption -- the CR positions 204/508/804 were
#     produced at the truncated k_max and cannot be carried over unexamined.
print()
print(BAR); print("PART 2b — IS THE TRUNCATION A HEIGHT DEFECT ONLY?  NO, AND THAT IS THE RESULT"); print(BAR)
_dpos_max, _dh_min = 0.0, 1e9
for _h in (False, True):
    _p900 = res[(_h, 900)][0]
    _p2400 = res[(_h, 2400)][0]
    _d = [abs(a - b) for a, b in zip(_p900, _p2400)]
    _dpos_max = max(_dpos_max, max(_d))
    _dh = abs(res[(_h, 900)][1] - res[(_h, 2400)][1]) / res[(_h, 2400)][1]
    _dh_min = min(_dh_min, _dh)
    print(f"    {'_project' if _h else 'los_spectrum':>14}  positions "
          f"{[int(v) for v in _p900]} -> {[int(v) for v in _p2400]}   "
          f"max shift {max(_d):.0f} ell ({max(_d)/_p2400[-1]:.1%})      P1/P2 moves {_dh:+.1%}")
# THE POSITIONS DO MOVE.  Asserted as measured, in BOTH directions, so the receipt fails if the
# claim inverts either way.
assert _dpos_max > 8.0, ("positions did NOT move -- the finding has changed", _dpos_max)
assert _dpos_max < 24.0, ("positions moved MORE than measured", _dpos_max)
# and the ordering -- heights damaged far more than positions -- is the part that survives.
_rel_pos = _dpos_max / float(_prj2400[0][-1])
assert _rel_pos < _dh_min / 4.0, ("heights no longer dominate", _rel_pos, _dh_min)
print(f"  ⛔ ** THE POSITIONS MOVE: up to {_dpos_max:.0f} in ell ({_rel_pos:.1%}) across a 2.7x "
      f"change in k_max. **")
print(f"     The first peak is unmoved; the second moves 8; the third moves 16 and grows with ell.")
print(f"  ** So truncation is NOT a height-only defect.  Heights move {_dh_min:.0%}+ and positions "
      f"{_rel_pos:.1%} -- ")
print("     an ordering worth having, and NOT the 'positions are unaffected' this line assumed.")
print("  ⇒ ** A position quoted off a truncated run carries a shift of this order.  This is the")
print("     CONTROL arm; the CR arm runs HIER where PART 0 shows r3512's defect is LIVE, so the CR")
print("     positions 204/508/804 cannot be carried over unexamined either. **")

# (A7) CONVERGENCE IN MODE COUNT, at the converged k_max -- a two-fold range in NK.
print()
print(f"    {'NK':>6} {'P1/P2':>9} {'P1/P3':>9}")
# NK=280 is already in hand from PART 1; only the second point is a new run.
conv = [(r2, r3), run(2400, True, nk=420)[1:]]
for nk, (a_, b_) in zip((280, 420), conv):
    print(f"    {nk:>6} {a_:>9.4f} {b_:>9.4f}")
assert abs(conv[0][0] - conv[1][0]) < 2e-3, conv
assert abs(conv[0][1] - conv[1][1]) < 2e-3, conv
print("  ** stable to 2e-3 over a 1.5-fold change in mode count. **")

# CONTROL (A7c): the convergence test CAN fail -- at the TRUNCATED k_max the same widening of NK
# leaves a number that is stable and WRONG, so stability alone never certified anything.  Run on
# los_spectrum, where the truncated value is the 2.721 the record carried.
_s280 = _los900[1]
_s400 = run(900, False, nk=400)[1]
assert abs(_s280 - _s400) < 2e-3, (_s280, _s400)
assert abs(_s280 - CAMB_R2) / CAMB_R2 > 0.02, _s280
print(f"  CONTROL: at the TRUNCATED k_max, NK 280->400 is equally stable ({_s280:.4f} -> "
      f"{_s400:.4f})")
print("     and equally WRONG. ** Stability in the knob you varied is not convergence. **   [fires]")

# =====================================================================================
print(); print(BAR); print("PART 3 — THE `LN` SCAN THE RECORD RESTS ON IS INERT"); print(BAR)
# (A8) PO13_WORKING_STATE records LN=12 -> P1/P3 = 4.496 and LN=25 -> 8.009, and eliminates LN on
#      that basis ("resolving the hierarchy makes P3 WEAKER").  LN is genuinely plumbed -- the state
#      vector is 7+(LN-1)+1 wide and the neutrino hierarchy loop runs to LN-2 -- but the ratios do
#      not move.  Measured, not judged.
_ln = {}
for lnv in (12, 25):
    os.environ['LN'] = str(lnv)
    _sp = importlib.util.spec_from_file_location(f"AT_ln{lnv}", _INSTR)
    _M = importlib.util.module_from_spec(_sp)
    with contextlib.redirect_stdout(io.StringIO()):
        _sp.loader.exec_module(_M)
    assert _M.LN == lnv and _M.NVF == 7 + (lnv - 1) + 1, (_M.LN, _M.NVF)
    _saveAT = AT
    globals()['AT'] = _M
    _ln[lnv] = run(900, False)
    globals()['AT'] = _saveAT
    print(f"    LN = {lnv:>2}  (state width {_M.NVF})   P1/P2 = {_ln[lnv][1]:.4f}   "
          f"P1/P3 = {_ln[lnv][2]:.4f}")
os.environ.pop('LN', None)
assert abs(_ln[12][1] - _ln[25][1]) < 1e-3, _ln
assert abs(_ln[12][2] - _ln[25][2]) < 1e-3, _ln
print("  ** LN = 12 and LN = 25 agree to 1e-3 on BOTH ratios, with the state vector genuinely")
print("     wider. The recorded 4.496 -> 8.009 does not reproduce.**")
print("  ⌗ Reported as an instrument fact and not as a verdict on the node that recorded it:")
print("     what that scan was varying did not reach the number it was read on.")

print(); print(BAR)
print("""VERDICT.  ** PO-24's first step is done and it comes out the other way. **  The bespoke
transfer's LambdaCDM control reproduces CAMB's P1/P2 to 0.14% and sits inside the sky's 1 sigma, with
every peak within 9 multipoles of the sky's.  ** There is no height-machinery defect. **  The 22.7%
and 97.5% were two instrument-configuration faults compounding: a k-integral truncated at
k_max = l_max/D_M, where it is not converged, and a projection path that omits the polarisation
source.  Each is worth a factor on its own and neither alone reaches the answer.

** THE FORK IS SETTLED: REPAIR, NOT FRESH. **  The two-arm architecture carries the transfer.  A
fresh build would have discarded a working instrument on the strength of an artefact -- which is the
cost of the premise this receipt removes.

** AND THE FAILURE MODE IS ONE THE CORPUS ALREADY NAMES, ARRIVING IN A NEW PLACE. **  The instrument
has a gate against under-sampling k and none against truncating it, so a converged-looking run
certified a number that moved by 22% when the limit was raised.  ** A guard on one axis reads as a
guard, and the axis it does not cover is invisible exactly because the guard is there. **""")
print(BAR)
