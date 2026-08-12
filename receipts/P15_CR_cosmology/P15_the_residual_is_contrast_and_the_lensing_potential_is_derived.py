#!/usr/bin/env python3
"""
RECEIPT -- P15: ** WHAT THE CONTROL'S REMAINING chi^2 IS MADE OF -- POSITIONS 0.1%, PEAK CONTRAST 13%
TOO HIGH AND WORTH 38%, AND 53% IN NEITHER -- AND THE LENSING POTENTIAL BUILT TO ATTACK IT, CARRIED
ON THIS INSTRUMENT'S OWN Phi WITH NO NEW PARAMETER. **

Built r2376+c54.184, front #2.  Instrument:
`computations/beyond_the_wall/L171x_lensing_potential.py`.

===================================================================================================
** PART A -- THE RESIDUAL, DECOMPOSED, SO THE NEXT BUILD IS CHOSEN BY MEASUREMENT. **
===================================================================================================

c54.181 measured what two candidate builds could be worth.  ** This asks the prior question: what
SHAPE is the residual. **  Templates are projected through the same inverse covariance the chi^2
uses, so each reports the chi^2 it removes.

  POSITIONS       d(chi^2) = 1.4 of 1320 -- ** 0.1%. **  The peaks are where the sky puts them and
                  that is not where the residual lives.  *Independent of the peak table, which said
                  the same thing: 220/540/812 against 220.6/538.1/809.8.*
  ENVELOPE        a smooth multiplicative distortion, three parameters: 15%.
  CONTRAST        the peak-trough oscillation at FIXED position, two parameters: ** 38%, and the
                  model's contrast is 13.1% TOO HIGH. **  *Reducing contrast without moving peaks is
                  what lensing does, and it is consistent with the ~400 a lensing-shaped smoothing
                  bought at c54.181.*
  NEITHER         ** 53% of the residual is in neither set. **  So even a perfect lensing
                  calculation leaves about half, and that is the expectation to carry INTO the build
                  rather than discover after it.

** THESE ARE FITTED TEMPLATES. **  Each share is an upper bound on what the corresponding physical
effect can claim, not a measurement of anything physical, and the two sets overlap by ~7 points.

===================================================================================================
** PART B -- THE LENSING POTENTIAL, AND WHY IT COSTS NO PARAMETER. **
===================================================================================================

The line-of-sight solve stops at eta = 4000, which is z = 12.8 -- where the visibility and the ISW
finish.  ** The lensing kernel does not finish there: it peaks at chi_*/2, which is z ~ 3.3. **  So
Phi is carried on by the background's own growth factor, g(a) = D(a)/a with
D prop. H INT da/(aH)^3 -- a background quadrature, exact in linear theory for matter and Lambda,
carrying no k-dependence and importing no transfer function.  ** The k-dependence is this
instrument's own Phi at eta_ref. **

** AND THE NORMALISATION IS THE ONE THE TEMPERATURE COMPARISON ALREADY FITTED. **  The same
primordial amplitude sets both spectra, and the comparison fits A in closed form; A/T_0^2 is the
dimensionless normalisation of Phi.  *So lensing enters the transfer with NO new parameter -- which
is what would make it a derivation rather than c54.181's fitted smoothing.*

  PART 1  ** LIMBER IS ADEQUATE, AND THAT IS MEASURED AGAINST AN EXACT PROJECTION RATHER THAN
          ASSUMED. **  Agreement within 5% over l = 5-200.  *I suspected Limber of the low-l
          behaviour below and I was WRONG; the check is recorded because the suspicion was.*
  PART 2  ** THE DEFLECTION-POWER MAXIMUM IS BROAD -- within 10% of its peak over l = 12-42 -- so
          its argmax is not a sharp quantity and nothing should be read from its exact location. **
  PART 3  ** THE ABSOLUTE rms DEFLECTION IS 2.69 ARCMIN WITH NOTHING FITTED TO IT. **

** !! AND THE EPISTEMIC STATUS OF PART 3 IS STATED, BECAUSE IT IS NOT WHAT IT LOOKS LIKE. **  The
numbers it is compared against -- ~2.7 arcmin, and a deflection power of order 1e-7 -- are RECALLED,
not derived here and not checked against a source this corpus holds.  ** This programme has been
bitten twice in three revisions by exactly that: the 16/15 shear coefficient adopted on recollection
at c54.176 and withdrawn, and the Limber suspicion in PART 1 which was also recollection and was
also wrong. **  *So what PART 3 establishes is INTERNAL consistency -- the growth, the projection and
the temperature normalisation agree with each other -- and its agreement with an external number is
CORROBORATION AT THE STRENGTH OF A MEMORY, which is not a receipt's strength.*  The successor should
treat 2.69 as internally consistent and externally unverified.

rc=0 on success.  Run: python3 P15_the_residual_is_contrast_and_the_lensing_potential_is_derived.py
"""
import os
import sys

import numpy as np
import scipy.linalg

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

_z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra', 'c54.178_lcdm.npz'))
mb = CS.bin_spectrum(_z['ls'], _z['Dl'])
keep = np.isfinite(mb)
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(keep, keep)]),
                           np.identity(keep.sum()))
F = 0.5 * (F + F.T)
m, d = mb[keep], CS.X_DATA[keep]
A = float((m @ F @ d) / (m @ F @ m))
r = d - A * m
lc, _ = CS.bin_center_and_fac()
lc = lc[keep]
CHI = float(r @ F @ r)
x, y = np.log(lc), np.log(m)


def loess(s):
    """a LOCAL LINEAR envelope -- ** a local MEAN is biased at the edges of a steep power law, and
    this model falls as l^-4 in the binned C_l, which produced an 'oscillation' larger than the
    model itself before it was fixed. **"""
    o = np.empty_like(y)
    for i in range(len(x)):
        w = np.exp(-0.5 * ((x - x[i]) / s) ** 2)
        X = np.vstack([np.ones_like(x), x - x[i]]).T
        W = X.T * w
        o[i] = np.linalg.solve(W @ X, W @ y)[0]
    return np.exp(o)


# ** the templates carry the FITTED AMPLITUDE, or the coefficient is A times too large -- which is
# how the contrast coefficient first came out as -1330 instead of -0.13. **
env = loess(0.20)
osc = m - env
te, to = A * env, A * osc
xm = x - np.log(500)


def blk(ts):
    T = np.vstack(ts).T
    return float((T.T @ F @ r) @ np.linalg.solve(T.T @ F @ T, T.T @ F @ r))


POS = np.gradient(A * m, x)
d_pos = float(POS @ F @ r) ** 2 / float(POS @ F @ POS)
E = [te, te * xm, te * xm ** 2]
O = [to, to * xm]
d_env, d_osc, d_both = blk(E), blk(O), blk(E + O)
c_contrast = float(to @ F @ r) / float(to @ F @ to)

print("=" * 78)
print("PART A — WHAT THE RESIDUAL IS MADE OF")
print("=" * 78)
print(f"  chi^2 = {CHI:.1f} over {keep.sum()} bins, fitted A = {A:.4e}\n")
print(f"  {'component':>40} {'d(chi^2)':>10} {'share':>8} {'free':>5}")
for nm, v, nf in (('peak POSITION', d_pos, 1), ('smooth ENVELOPE', d_env, 3),
                  ('peak CONTRAST', d_osc, 2), ('envelope + contrast', d_both, 5)):
    print(f"  {nm:>40} {v:>10.1f} {v/CHI:>7.1%} {nf:>5}")
print(f"  {'in NEITHER':>40} {CHI-d_both:>10.1f} {(CHI-d_both)/CHI:>7.1%}")
print(f"\n  ** THE MODEL'S PEAK-TROUGH CONTRAST IS {abs(c_contrast):.1%} TOO HIGH at fixed "
      f"POSITION. **")
print("     *Which is what lensing reduces, and it is the largest NAMED piece.*")
if d_pos / CHI > 0.02:
    fail.append(f"the position template removes {d_pos/CHI:.1%} -- PART A says positions are not it")
if not (0.25 < d_osc / CHI < 0.5):
    fail.append(f"the contrast template removes {d_osc/CHI:.1%} -- outside what PART A reports")
if (CHI - d_both) / CHI < 0.4:
    fail.append("less than 40% survives both template sets -- PART A overstates what remains")
if c_contrast >= 0:
    fail.append("the data want MORE contrast, not less -- the lensing reading is backwards")

# =====================================================================
print()
print("=" * 78)
print("PART B — THE LENSING POTENTIAL: LIMBER, THE BROAD MAXIMUM, AND THE ABSOLUTE SCALE")
print("=" * 78)
EX = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra', 'c54.182_clpp.npz')
z2 = np.load(EX)
ls, cl = z2['ls'].astype(float), z2['cl']
lx, ex, lim = z2['l_exact'].astype(float), z2['cl_exact'], z2['cl_limber']
AMP = A / 2.7255e6 ** 2
print(f"  {'l':>6} {'exact':>12} {'Limber':>12} {'ratio':>8}")
for a_, b_, c_ in zip(lx, ex, lim):
    print(f"  {a_:>6.0f} {b_:>12.4e} {c_:>12.4e} {c_/b_:>8.3f}")
worst = float(np.max(np.abs(lim / ex - 1.0)))
print(f"\n  ** Limber departs from the exact projection by at most {worst:.1%} over l = "
      f"{lx.min():.0f}-{lx.max():.0f}. **")
P = (ls * (ls + 1)) ** 2 * cl / (2 * np.pi) * AMP
msk = (ls >= 5) & (ls <= 150)
hi = ls[msk][P[msk] > 0.9 * P[msk].max()]
print(f"  ** the deflection-power maximum is BROAD: within 10% of peak over l = {hi.min():.0f}-"
      f"{hi.max():.0f}, peak {P[msk].max():.3e}. **")
d2 = float(np.trapezoid(ls * (ls + 1) * cl * (2 * ls + 1) / (4 * np.pi), ls))
rms = float(np.degrees(np.sqrt(d2 * AMP)) * 60)
print(f"\n  ** rms deflection = {rms:.3f} arcmin, with the normalisation taken from the TEMPERATURE")
print(f"     fit (A = {A:.3e} micro-K^2 -> AMP = A/T_0^2 = {AMP:.4e}) and nothing tuned to it. **")
print("     ⚠ *The ~2.7 arcmin it agrees with is RECALLED and is not checked against a source this")
print("     corpus holds.  What is established here is INTERNAL consistency; the external agreement")
print("     is corroboration at the strength of a memory.  See the header.*")
if worst > 0.10:
    fail.append(f"Limber departs by {worst:.1%} -- too far to use for the lensing convolution")
if not (1.5 < rms < 4.5):
    fail.append(f"the rms deflection is {rms:.2f} arcmin -- outside any plausible range")
if not (hi.max() - hi.min() > 15):
    fail.append("the deflection maximum is not broad -- PART 2's claim fails")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — positions are 0.1% of the residual, the contrast is 13% too high and is the")
print("largest named piece, 53% is in neither, Limber is good to 5%, the deflection maximum is broad,")
print("and the rms deflection is 2.69 arcmin on the temperature fit's own normalisation.")
print("=" * 78)

# ============================================================================================
# GATE — r2376+c54.184.  The successor builds the lensing convolution on these, so each is pinned.
#   (1) positions are NOT the residual -- if this ever rises the whole diagnosis reorders;
#   (2) the contrast excess, which is what the convolution must remove;
#   (3) what survives both, which is the expectation the build must not be allowed to forget;
#   (4) Limber's adequacy, since the convolution will use it;
#   (5) the absolute rms deflection, which is the zero-parameter check on the normalisation.
# ============================================================================================
assert d_pos / CHI < 0.02, f"the position template removes {d_pos/CHI:.1%}"
assert abs(abs(c_contrast) - 0.131) < 0.02, f"the contrast excess is {abs(c_contrast):.3f}"
assert abs((CHI - d_both) / CHI - 0.53) < 0.05, f"{(CHI-d_both)/CHI:.1%} survives, expected 53%"
assert worst < 0.10, f"Limber departs by {worst:.1%}"
assert abs(rms - 2.692) < 0.10, f"the rms deflection is {rms:.3f} arcmin, expected 2.692"
print(f"GATE c54.184 (r2376): positions {d_pos/CHI:.1%} of the residual, contrast "
      f"{abs(c_contrast):.1%} high and {d_osc/CHI:.0%} of it, {(CHI-d_both)/CHI:.0%} in neither; "
      f"Limber good to {worst:.1%}; rms deflection {rms:.3f} arcmin on the temperature fit's own "
      f"normalisation -- pinned against THE_WORK front #2.")
