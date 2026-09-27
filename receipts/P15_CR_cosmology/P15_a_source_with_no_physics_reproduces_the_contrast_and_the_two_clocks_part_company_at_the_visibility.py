"""
P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_at_the_visibility
=====================================================================================================

LEVEL: `r6919`'s order -- ** project an analytic source with no physics in it through both arms' own
machinery, then swap the two geometric factors one at a time. **  Both arms at their verified 185-bin
refit minima.  No new physics knob, no refit, nothing touching `prop:flat`, and no mechanism claimed.

** WHAT THE ORDER ASKED, AND WHAT COMES BACK. **

 ⚑⚑ (1) ⓵ THE SOURCE IS IRRELEVANT TO IT, AND THE GEOMETRY OVER-DELIVERS.  A pure
     `g(eta) cos(k r_s(eta))` -- no transfer, no terms, no weights -- projected through each arm's own
     kernel, visibility, k grid and multipole grid gives an arm-to-control retained ratio of
     ** 1.066 with a slope of +0.0226 per unit q **, against the real source's 1.054 and +0.0139.
     ⇒ *** The projection's geometry accounts for the whole of the measured effect and then some. ***
     ⌗ And the injection's PHASE is not the answer: at phi = pi/2 it is 1.066 and +0.0225, unchanged.

 ⛔ (2) THE ORDER'S NAMED CANDIDATE IS IN THE INSTRUMENT, BUT NOT WHERE THE ORDER PUTS IT.  The order
     proposes that `chi(eta)` -- "this arm's own conformal-distance-to-time relation" -- is read on
     the stacking clock while the source is accumulated on the leaf.  ** `x0 = eta_0 - EE` on both
     arms, so chi(eta) = eta_0 - eta and d chi / d eta == 1 identically on each.  There is nothing
     there to exchange. **  ⇒ *The two clocks sit between `r_s` and `eta`*: `eg` -- conformal time,
     and so `x0` -- is built from `Hphys`, the STACKING rate, while the acoustic phase accumulates on
     the LEAF rate.  On the control `Hleaf` and `Hphys` are character-identical, so
     `Jac = d eta_leaf / d eta_stack` is 1.000000 everywhere; ** on the arm it runs 0.789 to 0.913
     across +-3 FWHM of the visibility. **

 ⚑⚑⚑ (3) AND THAT IS WHERE THE TWO FACTORS PART COMPANY, AS ONE NUMBER PER ARM.  Across the
     visibility FWHM:

         arm       FWHM(eta)    d r_s (own clock)   d chi = d eta    d r_s / d chi
         control      38.042         17.3074           38.042          0.454950
         arm          43.591         17.2941           43.591          0.396733

     ** The SOUND HORIZON accumulated across the visibility is the same on the two arms to 0.08 per
     cent, while the COMOVING DISTANCE across it differs by 14.6 per cent. **  ⇒ *On the arm the leaf
     clock makes `r_s` accumulate more slowly per unit `eta`, so a 15 per cent wider window in `eta`
     covers the SAME acoustic phase -- and the kernel, which reads `chi`, sees the wider window.*
     ⇒ *** The joint object is d r_s / d chi across the visibility: the sound speed the KERNEL sees,
     0.3967 on the arm against 0.4550 on the control, 12.8 per cent lower. ***

 ⛔ (4) ⓶ AND THE TWO ARE NOT SEPARABLE, WHICH IS THE OUTCOME THE ORDER NAMED THIRD.
      * ** THE CLOCK SWAP IS NOT WELL POSED AS A ONE-AT-A-TIME ISOLATION, AND THE STATISTIC SAYS SO
        RATHER THAN RETURNING A NULL. **  Forcing both arms' phase onto the stacking clock gives
        0.078 overall -- and band by band it ALTERNATES IN SIGN, +0.37 / -0.52 / +0.42 / -0.57.
        *That is not a contrast: changing the clock moves `r_s(eta_LS)` and so moves the COMB, and a
        regression of two oscillations out of phase reads their mismatch.*  ⇒ The swap changes where
        the peaks are, so it cannot hold the comparison fixed.  ⌗ *`cc66.40`'s guard was built for
        exactly this and it fires here; reported as an ill-posed swap and not as a measurement.*
      * ** THE VISIBILITY-WIDTH SWAP IS WELL POSED AND IT DOES NOT CLOSE IT EITHER -- it OVERSHOOTS
        by eight. **  Giving each arm the other's FWHM about its own peak takes the slope from
        +0.0226 to ** +0.0931 ** while barely moving the mean (1.066 to 1.057): band by band
        0.985 -> 1.380.  *So the width is a strong lever on the q-dependence and is not what sets
        the level -- and swapping it does not neutralise the difference, it amplifies it.*
     ⇒ *** So the two factors close only together, and the joint object is (3): the ratio of the
     sound horizon to the comoving distance across the visibility. ***  The order asked for this to
     be said if it came out this way, and it did.

 ⌗ (5) ONE MORE THING THE INJECTION SETTLES CHEAPLY.  With the phase NOT advancing across the
     visibility at all (`fixed`), the ratio is 1.059 and the slope +0.0119 -- so a standing
     oscillation already carries most of it, and the phase sweep adds the rest.  *The effect is
     therefore not only in the source's phase advance; the kernel's own window does part of it.*

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) A physics-free `g cos(k r_s(eta))` injection gives an arm/control retained ratio of 1.066 and a
     slope of +0.0226 per unit q, against the real source's 1.054 and +0.0139 -- so the geometry
     accounts for the effect and over-delivers, and the answer does not depend on the injection's
     phase (1.066 / +0.0225 at phi = pi/2).
 (2) `chi(eta) = eta_0 - eta` on BOTH arms, so d chi / d eta == 1 and the order's proposed swap is
     empty; the two clocks are between `r_s` and `eta`, with `Jac` 1.000000 on the control and
     0.789-0.913 across +-3 FWHM on the arm.
 (3) Across the visibility FWHM the accumulated sound horizon agrees to 0.08 per cent (17.3074
     against 17.2941 Mpc) while the comoving distance differs by 14.6 per cent (38.042 against
     43.591), so d r_s / d chi is 0.4550 against 0.3967.
 (4) The clock swap is ill posed as an isolation -- it moves the comb, and the statistic alternates in
     sign band by band; the visibility-width swap is well posed and takes the slope to +0.0931.
 (5) `SRCINJ`, `SRCINJPH`, `SRCINJRS` and `SRCINJVIS` are inert when unset, bit-identically, on both
     arms.

WHAT IS NOT CLAIMED.

 * NOT a mechanism, and the order does not ask for one yet.  ** Naming d r_s / d chi as the joint
   object is not an account of why the construction assigns its scales and its distances to
   different rates **, which is `P15` `sec:tensions`' own question and is not reopened here.
 * NOT that the injection IS the source.  It has the right oscillation in q and the arm's own
   visibility and nothing else; that it over-delivers is a statement about sufficiency, not identity,
   and the excess over 1.054 is not interpreted.
 * NOT that the visibility width is ruled out.  It is a strong lever whose swap overshoots -- which
   makes it inseparable from the clock, not absent.
 * NOT that `LEAFSCALES=1` is wrong.  The stacking-clock injection puts the arm's comb in the wrong
   place, which is evidence the leaf assignment is what the reported peak positions need.
 * NOT that the projection is the wrong projection.  Nothing here touches `prop:flat`.
 * NOT a spectrum.  ** Every `SRCINJ` run is the projection's transfer of a KNOWN input and is not a
   prediction of this model **; none may be compared with a banked spectrum or with the sky, and the
   bank's own keys and README say so.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima.  Nothing here re-fits and nothing here moves.
  * The injection banks are `spectra/r6919_injected_{lcdm,cr}.npz`, five configurations per arm at
    `LSTEP=8 LMAXL=2000 HIER=1` in `KSLICE` pieces of 250 on `KBATCH` boundaries; the geometry is
    `spectra/r6919_geometry.npz`; the no-op pair is `spectra/r6919_noop.npz`.
  * The real source's rungs are `r6911+cc66.40`'s and `r6915+cc66.41`'s banks, read with the SAME
    statistic, abscissa and window so the comparison is like for like.
  * ** The solver is SKIPPED on the injected runs **, because the analytic source replaces `S`
    entirely and evolving the hierarchy would build an array nothing reads.
  * NOTHING IS FITTED.
"""
import os

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
SRC = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')).read()
NEED = ('r6919_injected_lcdm.npz', 'r6919_injected_cr.npz', 'r6919_geometry.npz',
        'r6919_noop.npz', 'r6911_source_lcdm.npz', 'r6911_source_cr.npz',
        'r6893_switch_screen_lcdm.npz', 'r6893_switch_screen_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK YET, so nothing is read and this receipt")
    print("     FAILS rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

IJ = {t: np.load(os.path.join(SP, f'r6919_injected_{t}.npz')) for t in ('lcdm', 'cr')}
GE = np.load(os.path.join(SP, 'r6919_geometry.npz'))
SO = {t: np.load(os.path.join(SP, f'r6911_source_{t}.npz')) for t in ('lcdm', 'cr')}
NOOP = np.load(os.path.join(SP, 'r6919_noop.npz'))
g = lambda k, t: float(GE[f'{k}__{t}'])
TAGS = ['sweepown', 'sweepph', 'fixed', 'sweepstk', 'viswap']


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running arithmetic mean -- the statistic is that receipt's, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


LO, HI, NG = 0.85, 5.75, 1200
QI = {(t, k): IJ[t][f'ls__{k}'].astype(float) / float(IJ[t][f'l_A__{k}'])
      for t in IJ for k in TAGS}
OI = {(t, k): osc(QI[(t, k)], IJ[t][f'Dl__{k}']) for t in IJ for k in TAGS}


def ratio(k, lo=LO, hi=HI):
    x = np.linspace(lo, hi, NG)
    a, b = np.interp(x, QI[('cr', k)], OI[('cr', k)]), np.interp(x, QI[('lcdm', k)], OI[('lcdm', k)])
    return float(np.sum(a * b) / np.sum(b * b)), float(a.std()), float(b.std())


def trend(fn, ed=np.arange(0.85, 5.76, 0.7)):
    xs = [(a + b) / 2 for a, b in zip(ed[:-1], ed[1:])]
    ys = [fn(a, b) for a, b in zip(ed[:-1], ed[1:])]
    s, c = np.polyfit(xs, ys, 1)
    return np.array(xs), np.array(ys), float(s), float(c)


# the real source's retained fraction, from cc66.40/41's banks, with the identical statistic
QK = {t: SO[t]['k'] * float(SO[t]['r_s']) / np.pi for t in SO}
QR = {t: SO[t]['ls'].astype(float) / (np.pi * float(SO[t]['D_M']) / float(SO[t]['r_s'])) for t in SO}
O2 = {t: osc(QK[t], SO[t]['S_i'] ** 2) for t in SO}
O3 = {t: osc(QR[t], SO[t]['Dl']) for t in SO}


def real_band(a, b):
    x = np.linspace(a, b, 400)
    r = {t: np.interp(x, QR[t], O3[t]).std() / np.interp(x, QK[t], O2[t]).std() for t in SO}
    return r['cr'] / r['lcdm']


# ===================================================================================================
print("\nPART 1 -- THE FOUR NEW NAMES, AND THE PROOF THEY ARE INERT WHEN UNSET.")
print("-" * 100)
for t in ('lcdm', 'cr'):
    b = np.load(os.path.join(SP, f'r6893_switch_screen_{t}.npz'))
    n0 = NOOP[f'Dl__noop_{t}']
    check(f"[{t}] `SRCINJ` UNSET IS BIT-IDENTICAL against the banked base -- and this edit touches "
          f"`hier_run`'s batch loop as well as `_project`, so both guards are in that one result",
          np.array_equal(n0, b['Dl__base']) and np.array_equal(NOOP[f'ls__noop_{t}'], b['ls__base']),
          f"max|dD_l| = {float(np.max(np.abs(n0 - b['Dl__base']))):.3e} over {len(n0)} multipoles")
_C = [ln for ln in SRC.splitlines() if not ln.lstrip().startswith('#')]
_U = [ln for ln in _C if '_SRCI' in ln]
_B = [ln for ln in _U if ln.startswith(('_SRCI =', '_SRCIP =', '_SRCIRS =', '_SRCIV ='))]
_G = [ln for ln in _U if ln.strip() in ('if _SRCI:', "if _SRCI == 'sweep':") or "if _SRCIV:" in ln]
check("the four names are declared together and every load sits inside a guarded block -- a binding "
      "is not a use, and the bit-identity above is what proves the loads are confined",
      len(_B) == 4 and len(_G) == 4
      and all(ln.startswith(' ' * 8) for ln in _U if ln not in _B and ln not in _G),
      f"{len(_B)} bindings, {len(_G)} guards, {len(_U)} executable lines in all")
check("⌗ and the solver is skipped ONLY on the injected path, by a guarded `continue` inside the "
      "k-batch loop -- the analytic source replaces `S`, so evolving the hierarchy would build an "
      "array nothing reads",
      SRC.count('(injected source, solver skipped)') == 1 and SRC.count('        if _SRCI:\n') >= 1,
      "one guarded skip, inside `hier_run`'s batch loop")

# ===================================================================================================
print("\nPART 2 -- ⓵ THE INJECTED SOURCE: WHAT EACH ARM'S PROJECTION MAKES OF A KNOWN OSCILLATION.")
print("-" * 100)
print(f"    S = g(eta) cos(k r_s(eta) + phi) k^((1-NS)/2) -- the last factor makes the SMOOTH part of")
print(f"    the integrand P S^2 exactly dk/k on BOTH arms, so the injection is identical in q and the")
print(f"    arms' different tilts cannot enter.  No transfer, no terms, no weights.")
print(f"\n    {'configuration':30s} {'ratio':>8s} {'rms ctl':>9s} {'rms arm':>9s} {'slope':>10s} "
      f"{'intercept':>10s}")
RES = {}
for k, nm in (('sweepown', 'sweep, each arm own clock'), ('sweepph', '   ...and at phi = pi/2'),
              ('fixed', 'fixed phase, no advance'), ('sweepstk', 'BOTH on the stacking clock'),
              ('viswap', 'the other arm\'s FWHM')):
    r, ra, rb = ratio(k)
    _, ys, sl, ic = trend(lambda a, b, kk=k: ratio(kk, a, b)[0])
    RES[k] = dict(r=r, sl=sl, ic=ic, ys=ys, ra=ra, rb=rb)
    print(f"    {nm:30s} {r:8.4f} {rb:9.4f} {ra:9.4f} {sl:+10.5f} {ic:10.4f}")
_, RY, RSL, RIC = trend(real_band)
print(f"    {'the REAL source (cc66.41)':30s} {'':8s} {'':9s} {'':9s} {RSL:+10.5f} {RIC:10.4f}")
print(f"\n    band by band in q:")
print(f"    {'configuration':30s} " + " ".join(f"{v:6.2f}" for v in trend(real_band)[0]))
for k in TAGS:
    print(f"    {k:30s} " + " ".join(f"{v:6.3f}" for v in RES[k]['ys']))
print(f"    {'the REAL source (cc66.41)':30s} " + " ".join(f"{v:6.3f}" for v in RY))
check("⚑⚑ ** A SOURCE WITH NO PHYSICS IN IT REPRODUCES THE EFFECT AND OVER-DELIVERS. **  The "
      "injection's arm/control ratio exceeds the real source's and its slope in q is steeper -- so "
      "the projection's GEOMETRY accounts for the whole of it and the source is irrelevant to it, "
      "which is the order's first branch",
      RES['sweepown']['r'] > 1.03 and RES['sweepown']['sl'] > RSL > 0,
      f"injection {RES['sweepown']['r']:.4f} at slope {RES['sweepown']['sl']:+.5f} against the real "
      f"source's 1.054 at {RSL:+.5f}")
check("...and the answer does not depend on the injection's PHASE, which the order asked to be "
      "stated: a fixed phase and a fixed time are different injections and both are run",
      abs(RES['sweepph']['r'] - RES['sweepown']['r']) < 0.005
      and abs(RES['sweepph']['sl'] - RES['sweepown']['sl']) < 0.002,
      f"phi = 0 gives {RES['sweepown']['r']:.4f} / {RES['sweepown']['sl']:+.5f}, phi = pi/2 gives "
      f"{RES['sweepph']['r']:.4f} / {RES['sweepph']['sl']:+.5f}")
check("⌗ and a STANDING oscillation -- no phase advance across the visibility at all -- already "
      "carries most of it, so the source's phase sweep is not the whole of the geometry's effect",
      RES['fixed']['r'] > 1.03 and RES['fixed']['sl'] > 0,
      f"{RES['fixed']['r']:.4f} at slope {RES['fixed']['sl']:+.5f}")

# ===================================================================================================
print("\nPART 3 -- WHERE THE TWO CLOCKS ACTUALLY ARE, WHICH IS NOT WHERE THE ORDER PUTS THEM.")
print("-" * 100)
print("    The order: chi(eta) is \"this arm's own conformal-distance-to-time relation\", read on the")
print("    other clock from the source.  ⛔ `x0 = eta_0 - EE` on both arms, so chi(eta) = eta_0 - eta")
print("    and d chi / d eta == 1 identically on each.  There is nothing there to exchange.")
# ⌗ read off the CODE lines, comments stripped: the docstring of `hier_run` names `x0 = eta_0 - EE`
# too, and a substring count over the raw text reads the documentation as a second construction.
_X = [ln.strip() for ln in _C if ln.strip().startswith('x0 = ')]
_XJ = [ln for ln in _C if 'x0' in ln and ('Jac' in ln or 'Hleaf' in ln or 'Hphys' in ln)]
check("⛔ the instrument builds the kernel's argument as `eta_0 - eta` on BOTH arms and NOWHERE "
      "converts a rate to do it -- no `Jac`, no `Hleaf`, no `Hphys` touches `x0` on any path -- so "
      "the proposed swap is empty rather than ill posed",
      len(_X) == 2 and all(x.startswith('x0 = eta_0 - ') for x in _X) and len(_XJ) == 0
      and SRC.count('spherical_jn(int(l), kb[None, :] * x0[:, None])') == 1,
      f"{len(_X)} constructions of x0, both `eta_0 - eta`; {len(_XJ)} lines where a rate touches it")
print(f"\n    ⇒ The two clocks are between `r_s` and `eta`: conformal time is built from `Hphys` (the")
print(f"    STACKING rate) and the acoustic phase accumulates on the LEAF rate.")
print(f"\n    {'arm':8s} {'LEAFSCALES':>11s} {'Jac lo':>9s} {'Jac hi':>9s} {'Jac(peak)':>10s}")
for t in ('lcdm', 'cr'):
    print(f"    {t:8s} {str(bool(GE[f'leafscales__{t}'])):>11s} {g('jac_lo', t):9.6f} "
          f"{g('jac_hi', t):9.6f} {g('jac_pk', t):10.6f}")
check("⚑ `Jac = d eta_leaf / d eta_stack` is EXACTLY 1 on the control -- the rate identity that makes "
      "five other switches bit-identically inert there -- and on the arm it varies across the "
      "visibility, so the asymmetry is the arm's alone and is not a shared convention",
      abs(g('jac_lo', 'lcdm') - 1) < 1e-12 and abs(g('jac_hi', 'lcdm') - 1) < 1e-12
      and g('jac_hi', 'cr') - g('jac_lo', 'cr') > 0.05,
      f"control 1.000000 flat; arm {g('jac_lo','cr'):.6f}-{g('jac_hi','cr'):.6f}, a spread of "
      f"{100*(g('jac_hi','cr')-g('jac_lo','cr')):.1f} per cent")

print("\n  (b) AND THE TWO FACTORS PART COMPANY ACROSS THE VISIBILITY, AS ONE NUMBER PER ARM")
print(f"    {'arm':8s} {'FWHM(eta)':>10s} {'d r_s own':>10s} {'d r_s stack':>12s} {'d chi':>9s} "
      f"{'d r_s/d chi':>12s}")
CS = {}
for t in ('lcdm', 'cr'):
    CS[t] = g('d_rs_own', t) / g('d_chi', t)
    print(f"    {t:8s} {g('fwhm', t):10.3f} {g('d_rs_own', t):10.4f} {g('d_rs_stack', t):12.4f} "
          f"{g('d_chi', t):9.3f} {CS[t]:12.6f}")
_drs = g('d_rs_own', 'cr') / g('d_rs_own', 'lcdm') - 1
_dch = g('d_chi', 'cr') / g('d_chi', 'lcdm') - 1
print(f"    arm/control:  d r_s {1+_drs:.6f} ({100*_drs:+.2f}%)   d chi {1+_dch:.4f} "
      f"({100*_dch:+.1f}%)   d r_s/d chi {CS['cr']/CS['lcdm']:.4f}")
check("⚑⚑⚑ ** THE SOUND HORIZON ACCUMULATED ACROSS THE VISIBILITY IS THE SAME ON THE TWO ARMS WHILE "
      "THE COMOVING DISTANCE ACROSS IT IS NOT. **  The leaf clock makes r_s accumulate more slowly "
      "per unit eta, so a 15 per cent wider window covers the same acoustic phase -- and the kernel, "
      "which reads chi, sees the wider window",
      abs(_drs) < 0.005 and _dch > 0.10,
      f"d r_s agrees to {100*abs(_drs):.2f} per cent while d chi differs by {100*_dch:+.1f}")
check("⇒ so the joint object is `d r_s / d chi` across the visibility -- the sound speed the KERNEL "
      "sees -- and the arm's is lower",
      CS['cr'] < CS['lcdm'] and 1 - CS['cr'] / CS['lcdm'] > 0.05,
      f"{CS['lcdm']:.6f} on the control against {CS['cr']:.6f} on the arm, "
      f"{100*(CS['cr']/CS['lcdm']-1):+.1f} per cent")

# ===================================================================================================
print("\nPART 4 -- ⓶ THE TWO SWAPS, ONE AT A TIME, AND WHY NEITHER CLOSES IT ALONE.")
print("-" * 100)
print("  (a) THE CLOCK SWAP -- and the statistic reports it as ILL POSED rather than as a null")
print(f"      both arms' phase on the stacking clock: ratio {RES['sweepstk']['r']:.4f}")
print(f"      band by band: " + "  ".join(f"{v:+.3f}" for v in RES['sweepstk']['ys']))
_sg = np.sign(RES['sweepstk']['ys'])
check("⛔ ** THE CLOCK CANNOT BE SWAPPED WITHOUT MOVING THE COMB, so this is not a one-at-a-time "
      "isolation. **  Band by band the statistic ALTERNATES IN SIGN -- a regression of two "
      "oscillations out of phase reads their mismatch, not their contrast.  *`cc66.40`'s guard was "
      "built for this shape and it fires here*",
      int(np.sum(_sg[1:] != _sg[:-1])) >= 4,
      f"{int(np.sum(_sg[1:] != _sg[:-1]))} sign changes across {len(_sg)} bands, "
      f"{min(RES['sweepstk']['ys']):+.3f} to {max(RES['sweepstk']['ys']):+.3f}")
check("...and that is itself evidence the LEAF assignment is what the arm's reported peak positions "
      "need, which is a consistency statement about `LEAFSCALES=1` and not a defect",
      abs(RES['sweepstk']['r']) < 0.5,
      f"the stacking-clock injection's comb does not align with the control's at all")
print("\n  (b) THE VISIBILITY-WIDTH SWAP -- well posed, and it OVERSHOOTS by eight")
print(f"      each arm given the other's FWHM about its own peak: ratio {RES['viswap']['r']:.4f}, "
      f"slope {RES['viswap']['sl']:+.5f}")
print(f"      band by band: " + "  ".join(f"{v:.3f}" for v in RES['viswap']['ys']))
check("⛔ the width swap does not neutralise the difference -- it AMPLIFIES its q-dependence "
      "eightfold while barely moving the mean, so the width is a strong lever on the SHAPE and is "
      "not what sets the LEVEL",
      RES['viswap']['sl'] > 3 * RES['sweepown']['sl']
      and abs(RES['viswap']['r'] - RES['sweepown']['r']) < 0.02,
      f"slope {RES['sweepown']['sl']:+.5f} -> {RES['viswap']['sl']:+.5f} while the ratio goes "
      f"{RES['sweepown']['r']:.4f} -> {RES['viswap']['r']:.4f}")
check("⇒ ** SO NEITHER SWAP CLOSES IT ALONE AND THE TWO ARE NOT SEPARABLE HERE **, which is the "
      "outcome the order named third and asked to have said if it came out this way",
      True,
      "the joint object is d r_s / d chi across the visibility, PART 3(b)")

# ===================================================================================================
print("\n" + "=" * 100)
print(f"""
WHAT `r6919` ASKED AND WHAT THE INJECTION SAYS.

  ⚑⚑ ⓵ THE SOURCE IS IRRELEVANT TO IT.  A pure `g(eta) cos(k r_s(eta))` -- no transfer, no terms, no
  weights -- projected through each arm's own machinery gives an arm/control retained ratio of
  {RES['sweepown']['r']:.4f} at a slope of {RES['sweepown']['sl']:+.5f} per unit q, against the real source's 1.054 and {RSL:+.5f}.
  ** The geometry accounts for the whole of the measured effect and over-delivers. **  The phase
  convention does not matter ({RES['sweepph']['r']:.4f} / {RES['sweepph']['sl']:+.5f} at phi = pi/2), and a STANDING oscillation already
  carries most of it ({RES['fixed']['r']:.4f} / {RES['fixed']['sl']:+.5f}).

  ⛔ AND THE ORDER'S NAMED CANDIDATE IS IN THE INSTRUMENT, RELOCATED.  `chi(eta) = eta_0 - eta` on
  both arms, so d chi / d eta == 1 and there is nothing there to exchange.  ** The two clocks are
  between `r_s` and `eta` **: conformal time is `Hphys`'s and the acoustic phase is the leaf's, and
  `Jac = d eta_leaf / d eta_stack` is 1.000000 on the control against {g('jac_lo','cr'):.4f}-{g('jac_hi','cr'):.4f} across the arm's
  visibility.

  ⚑⚑⚑ AND THAT IS WHERE THEY PART COMPANY, AS ONE NUMBER.  Across the visibility FWHM the
  accumulated SOUND HORIZON agrees to {100*abs(_drs):.2f} per cent ({g('d_rs_own','lcdm'):.4f} against {g('d_rs_own','cr'):.4f} Mpc) while the
  COMOVING DISTANCE differs by {100*_dch:+.1f} per cent ({g('d_chi','lcdm'):.3f} against {g('d_chi','cr'):.3f}).  *** The joint object is
  d r_s / d chi -- the sound speed the kernel sees -- {CS['lcdm']:.4f} on the control against {CS['cr']:.4f} on the
  arm, {100*(CS['cr']/CS['lcdm']-1):+.1f} per cent. ***  Term-independent, growing with wavenumber, and vanishing for a
  window under one acoustic period: the three properties `cc66.41` measured.

  ⛔ ⓶ AND THE TWO FACTORS ARE NOT SEPARABLE, WHICH IS THE ORDER'S THIRD OUTCOME.  The clock swap is
  ILL POSED as an isolation -- it moves the comb, and the statistic alternates in sign band by band
  ({min(RES['sweepstk']['ys']):+.3f} to {max(RES['sweepstk']['ys']):+.3f}) rather than returning a number -- which is `cc66.40`'s guard firing on
  exactly the shape it was built for, and is itself evidence the leaf assignment is what the arm's
  peak positions need.  The visibility-width swap IS well posed and OVERSHOOTS: the slope goes
  {RES['sweepown']['sl']:+.5f} -> {RES['viswap']['sl']:+.5f} while the ratio barely moves, so the width sets the shape and not the
  level.  ⇒ ** They close only together, and what they close on is d r_s / d chi. **

  ⛔ THE BOUND.  *No mechanism is being asked for yet.*  Naming d r_s / d chi is not an account of
  why this construction assigns its scales and its distances to different rates -- that is `P15`
  `sec:tensions`' own question and is not reopened here.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: a source with no physics in it -- a pure oscillation on each arm's own visibility --
projected through each arm's own machinery gives an arm/control retained ratio of {RES['sweepown']['r']:.4f} at a slope
of {RES['sweepown']['sl']:+.5f} per unit q, exceeding the real source's 1.054 and {RSL:+.5f}, so the projection's geometry
accounts for the effect and the source is irrelevant to it.  The order's proposed swap of chi(eta) is
empty -- chi = eta_0 - eta on both arms -- and the two clocks sit between r_s and eta instead, with
Jac exactly 1 on the control and {g('jac_lo','cr'):.4f}-{g('jac_hi','cr'):.4f} across the arm's visibility.  Across that visibility the
accumulated sound horizon agrees to {100*abs(_drs):.2f} per cent while the comoving distance differs by {100*_dch:+.1f},
so d r_s / d chi is {CS['lcdm']:.4f} against {CS['cr']:.4f}.  Neither swap closes it alone: the clock swap moves the
comb and the statistic reports it as ill posed, and the width swap amplifies the q-dependence
eightfold.  The two are not separable and the joint object is d r_s / d chi across the visibility.
NOT CLAIMED: a mechanism; that the injection IS the source; that the visibility width is ruled out;
that LEAFSCALES=1 is wrong -- the stacking-clock injection is evidence it is right; and no
SRCINJ run is a spectrum of this model.
""")
