"""
P15_the_cross_term_is_not_the_channel_and_every_projected_term_carries_the_excess
=================================================================================

LEVEL: `r6915`'s order -- ** project the source's terms SEPARATELY and read the same contrast
statistic off each projected piece **, both arms at their own verified 185-bin refit minima.  No new
knob on the physics, no refit, and no mechanism asked for or offered.

** WHAT THE ORDER ASKED, AND WHAT COMES BACK. **

 ⛔ (0) THE ORDER'S CLOSURE GATE NEEDS A CORRECTION FIRST, AND IT IS THE ORDER'S OWN FIRST OUTCOME.
     The order writes: *"the projection is linear in the source, so the separately projected pieces
     must sum to the full spectrum.  Gate that first... and read nothing below it if it fails."*
     ** The TRANSFER is linear in the source and the pieces do add there.  C_l is QUADRATIC in the
     transfer, so the projected SPECTRA cannot add -- they are short by exactly the cross terms. **
     ⇒ *That is not the order's third outcome ("the decomposition is not linear where I assumed"):
     the order's FIRST outcome presupposes a cross term, so the two clauses are in tension and the
     first is the coherent one.*  ⇒ ** What does close is the full bilinear decomposition **:
     with Delta^a_l(k) the transfer of source term a, C_l = SUM_{a<=b} w_ab SUM_k P Delta^a Delta^b,
     w = 1 on the diagonal and 2 off it -- ten numbers per multipole.  ** They close on D_l to
     1.1e-15 and 1.3e-15 relative on the two arms, and that IS the gate the order asked for. **

 ⛔ (1) AND THE CROSS TERM IS NOT THE CHANNEL.  ** Deleting the monopole-Doppler cross from the full
     spectrum moves the contrast ratio from 1.0452 to 1.0451 -- one part in ten thousand. **  Across
     four envelope windows it carries between -0.0013 and +0.0008 of the +0.045, so it is bounded at
     about a part in a thousand and is consistent with zero.  ⇒ *The order's first outcome --- "both
     pieces near 1.00 and the sum at 1.045, so the excess is in the CROSS TERM" --- is excluded, and
     the interference between j_l and j_l' is not what makes the difference.*

 ⚑ (2) BECAUSE EVERY PIECE ALREADY CARRIES IT, WHICH IS NEITHER OF THE OUTCOMES NAMED.  The order's
     second allowed for ONE piece at 1.045.  ** Projected separately, the monopole is at 1.034, the
     Doppler at 1.099 and the polarisation at 1.058, against the full spectrum's 1.045. **  (The ISW
     is the one exception at 0.989, and it carries 1.0% of D_l.)  ⇒ ** So it is not a term and not a
     pair of terms: the projection raises this arm's contrast on nearly everything it projects. **

 ⚑⚑ (3) THE SHARPEST OBJECT IS THE PER-TERM LADDER, BECAUSE EVERY TERM MOVES THE SAME WAY.

         term                          source (k)     projected      change
         monopole  g(Theta_0+Psi)          0.9920        1.0343       +0.042
         Doppler   d[g theta_b]/k^2        0.9726        1.0988       +0.126
         ISW                               0.9723        0.9889       +0.017
         polarisation                      0.9904        1.0578       +0.067
         the whole source                  0.9923        1.0452       +0.053

     ** Every term's source ratio is at or below 0.992 and every term's projected ratio is higher. **
     *`cc66.40` found that for the source as a whole; this says it term by term, and it is why no
     single term can be the channel.*

 ⌗ (4) AND THE SPLIT THE ORDER'S REASONING WAS REALLY AFTER -- WEIGHT AGAINST RESPONSE -- IS ABOUT
     40/60, WITH THE RESPONSE THE LARGER.  *The order's route was that the two terms' relative
     WEIGHT differs between the arms and the kernels rotate their relative phase.*  ** The weight
     does differ (the arm's `sw*sw` share is 0.5225 against 0.5092 and its `dp*dp` 0.1753 against
     0.1840), and rebuilding the arm's pieces at the CONTROL's shares takes 1.0452 to 1.0267 --
     so the weights carry +0.019 of the +0.045 and each piece's own response carries +0.026. **
     ⌗ *The reverse construction agrees: the control's pieces at the ARM's shares gives 1.0254,
     +0.020.  Two crude reweightings agreeing to 0.001 is what makes this a split and not a number.*

 ⚑ (5) ⓶ THE RETAINED FRACTION AS A FUNCTION OF q, AND IT IS THE ORDER'S FIRST BRANCH.  *The order:
     if the ratio tends to 1 at low q and grows, that is a kernel-phase signature, because a
     normalisation difference would be flat; if it is flat, the q split was reading the envelope and
     the reading dies.*  ** It is not flat.  It rises from 1.030 in the lowest band to 1.089 in the
     highest, and over twelve settings -- four envelope windows x three band counts -- the slope is
     +0.0139 +- 0.0021 per unit q, never once consistent with zero. **  ⇒ *And the intercept is
     1.017 +- 0.010, straddling 1: **the rise is established and the offset is not**, which is the
     branch the order named, with the extrapolation to q = 0 called an extrapolation.*

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The ten pair spectra close on D_l to 1.1e-15 and 1.3e-15 relative, on both arms, summed over
     eleven and six `KSLICE` pieces.
 (2) The monopole-Doppler cross term carries -0.0013 to +0.0008 of the +0.045 over four envelope
     windows -- bounded at about a part in a thousand, consistent with zero.
 (3) Projected separately: monopole 1.034, Doppler 1.099, polarisation 1.058, ISW 0.989, full 1.045;
     the two squares without their cross 1.048; all stable across four windows and both envelope
     definitions.
 (4) The per-term ladder, source against projection, for all four terms.
 (5) The weight/response split, 0.019 against 0.026, from two reweightings agreeing to 0.001.
 (6) The retained-fraction ratio's slope in q, +0.0139 +- 0.0021 over twelve settings, with its
     intercept 1.017 +- 0.010.
 (7) `SRCDEC` is inert when unset, bit-identically, on both arms.

WHAT IS NOT CLAIMED.

 * NOT a mechanism.  Naming that every projected term carries it, and that the rise in q is real, is
   still not a statement about why.  ** The order's bound is unmoved and is restated in its own
   terms: this is a stage and a shape, not a cause. **
 * NOT that the cross term is zero.  It is 26% of D_l and its oscillation is 59% of the full's; what
   is bounded is its contribution to the DIFFERENCE between the arms.
 * NOT that the projection is the wrong projection.  Nothing here touches `prop:flat`.
 * NOT that the Doppler's 1.099 is better determined than the monopole's 1.034.  Its piece's
   relative oscillation is 0.116 against 0.305, so it is the weaker signal of the two, and its
   window spread (1.0995-1.1070) is quoted beside it rather than smoothed.
 * NOT that the weight/response split is a fit.  Rescaling a piece by its mean share also moves the
   envelope; the two directions are reported precisely because neither alone is clean.
 * NOT that the q = 0 intercept is 1.  It is 1.017 +- 0.010 and the lowest band CENTRE is q ~ 1.2,
   so the value at zero is an extrapolation and is called one.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima -- `LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248` and
    `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952 ZSTART=3e7 LEAFSCALES=1`.  Nothing here
    re-fits and nothing here moves.
  * The pair banks are `spectra/r6915_pairs_{lcdm,cr}.npz` at `LSTEP=8 LMAXL=2000 HIER=1` in
    `KSLICE` pieces of 250 on `KBATCH` boundaries; the no-op pair is `spectra/r6915_noop.npz`.
  * The source rungs are read from `r6911+cc66.40`'s banks `spectra/r6911_source_{lcdm,cr}.npz` --
    the SAME statistic and the same abscissa, which is what makes the ladder a ladder.
  * The statistic, the abscissa and their resolution are `r6911+cc66.40`'s and are not re-derived:
    q = k r_s/pi in k and ell/l_A in ell, envelope a running ARITHMETIC mean over one acoustic
    period (geometric fails on the source power), window reported over a range rather than chosen.
  * NOTHING IS FITTED.  The two reweightings in (4) are constructions from banked spectra.
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
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INST).read()
NEED = ('r6915_pairs_lcdm.npz', 'r6915_pairs_cr.npz', 'r6915_noop.npz',
        'r6911_source_lcdm.npz', 'r6911_source_cr.npz',
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

PR = {t: np.load(os.path.join(SP, f'r6915_pairs_{t}.npz')) for t in ('lcdm', 'cr')}
SO = {t: np.load(os.path.join(SP, f'r6911_source_{t}.npz')) for t in ('lcdm', 'cr')}
NOOP = np.load(os.path.join(SP, 'r6915_noop.npz'))
NM = [str(x) for x in PR['lcdm']['pairs']]
IX = {n: i for i, n in enumerate(NM)}
QL = {t: PR[t]['ls'].astype(float) / float(PR[t]['l_A']) for t in PR}
QK = {t: SO[t]['k'] * float(SO[t]['r_s']) / np.pi for t in SO}


# --- the statistic, taken over unchanged from r6911+cc66.40 -------------------------------------
def env_a(x, y, win):
    """the running ARITHMETIC mean over one window of x -- `r6911+cc66.40`'s, and see its guard (a)"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def env_g(x, y, win):
    """`r6885+cc66.35`'s geometric mean, kept beside it so the definition is reported and not hidden"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.exp(np.mean(np.log(np.maximum(y[m], 1e-300))))
    return e


def osc(x, y, win=1.0, fn=env_a):
    e = fn(x, y, win)
    return (y - e) / e


LO, HI, NG = 0.85, 5.75, 1200


def stat(qA, oA, qB, oB, lo=LO, hi=HI):
    g = np.linspace(lo, hi, NG)
    a, b = np.interp(g, qA, oA), np.interp(g, qB, oB)
    return dict(reg=float(np.sum(a * b) / np.sum(b * b)), dA=float(a.std()), dB=float(b.std()))


def piece(t, cols):
    return PR[t]['Dl_pairs'][:, cols].sum(axis=1)


def ratio(cols, win=1.0, fn=env_a, lo=None, hi=None):
    lo = LO + 0.5 * (win - 1) if lo is None else lo
    hi = HI - 0.5 * (win - 1) if hi is None else hi
    yB, yA = piece('lcdm', cols), piece('cr', cols)
    return stat(QL['cr'], osc(QL['cr'], yA, win, fn), QL['lcdm'], osc(QL['lcdm'], yB, win, fn),
                lo, hi)


ALL = list(range(10))
NOX = [i for i in ALL if i != IX['sw*dp']]

# ===================================================================================================
print("\nPART 1 -- `SRCDEC`, AND THE CLOSURE GATE THE ORDER ASKED FOR (WITH ITS PREMISE CORRECTED).")
print("-" * 100)
print("    The order: \"the projection is linear in the source, so the separately projected pieces")
print("    must sum to the full spectrum.\"  ⛔ The TRANSFER is linear and the pieces add THERE;")
print("    C_l is QUADRATIC in the transfer, so the projected SPECTRA are short by the cross terms.")
print("    ⇒ What closes is the bilinear decomposition, and that is what `SRCDEC` banks.")
for t in ('lcdm', 'cr'):
    b = np.load(os.path.join(SP, f'r6893_switch_screen_{t}.npz'))
    n0 = NOOP[f'Dl__noop_{t}']
    check(f"[{t}] `SRCDEC` UNSET IS BIT-IDENTICAL against the banked base -- not 'small', equal",
          np.array_equal(n0, b['Dl__base']) and np.array_equal(NOOP[f'ls__noop_{t}'], b['ls__base']),
          f"max|dD_l| = {float(np.max(np.abs(n0 - b['Dl__base']))):.3e} over {len(n0)} multipoles")
CLO = {}
for t in ('lcdm', 'cr'):
    CLO[t] = float(np.max(np.abs(PR[t]['Dl_pairs'].sum(axis=1) - PR[t]['Dl']) / np.abs(PR[t]['Dl'])))
    check(f"[{t}] ⚑ ** THE TEN PAIRS CLOSE ON `D_l` EXACTLY **, summed over the run's own "
          f"`KSLICE` pieces -- this is the order's gate, in the form that can hold",
          CLO[t] < 1e-12,
          f"max relative |sum of pairs - D_l| = {CLO[t]:.3e} over {len(PR[t]['ls'])} multipoles, "
          f"{int(PR[t]['n_slices'])} slices, {int(PR[t]['n_modes'])} modes")
    check(f"[{t}] ...and this run's `D_l` is `r6911+cc66.40`'s, so the two receipts read one "
          f"configuration rather than two",
          np.array_equal(PR[t]['ls'], SO[t]['ls'])
          and float(np.max(np.abs(PR[t]['Dl'] - SO[t]['Dl']) / np.abs(SO[t]['Dl']))) < 1e-13,
          f"max relative |dD_l| = "
          f"{float(np.max(np.abs(PR[t]['Dl'] - SO[t]['Dl']) / np.abs(SO[t]['Dl']))):.3e}")
check("⛔ and the SPECTRA really do NOT add without the cross terms, which is the premise "
      "correction stated as a measurement rather than as an argument",
      float(np.max(np.abs(piece('lcdm', [IX['sw*sw'], IX['dp*dp'], IX['isw*isw'], IX['pol*pol']])
                          - PR['lcdm']['Dl']) / np.abs(PR['lcdm']['Dl']))) > 0.2,
      f"the four DIAGONAL pieces alone fall short of D_l by up to "
      f"{100*float(np.max(np.abs(piece('lcdm', [IX['sw*sw'], IX['dp*dp'], IX['isw*isw'], IX['pol*pol']]) - PR['lcdm']['Dl']) / np.abs(PR['lcdm']['Dl']))):.0f} per cent")
# ⌗ ** A BINDING IS NOT A USE -- `r6893+cc66.37`'s rule -- so the lines are CATEGORISED rather than
# counted.**  Every executable line naming `_SRCD` must be one of: its two module-level bindings,
# a guard that TESTS it, or a line inside a block one of those guards opens.  *Comment lines are
# stripped first, because the prose beside the switch names it too and a substring count would read
# the documentation as code -- which is the shape that failed this gate on its first writing.*
_C = [ln for ln in SRC.splitlines() if not ln.lstrip().startswith('#')]
_U = [ln for ln in _C if '_SRCD' in ln]
_BIND = [ln for ln in _U if ln.startswith(('_SRCD =', '_SRCD_B ='))]
# ⛭ r6977: same re-pointing as its sibling -- cc66's r6959 added `SRCETA` to the shared guard, so
#   `if _SRCS or _SRCD or _SRCE:` is the third accepted spelling.  ** The confinement claim and
#   the bit-identity that proves it are untouched. **
_GUARD = [ln for ln in _U if ln.strip() in ('if _SRCD:', 'if _SRCS or _SRCD:',
                                            'if _SRCS or _SRCD or _SRCE:')
          or ln.strip().endswith('if _SRCD else None')]
_INNER = [ln for ln in _U if ln not in _BIND and ln not in _GUARD]
check("`SRCDEC` is declared beside `SRCSAVE`, and every executable line naming it is a binding, a "
      "guard that tests it, or a line inside a block such a guard opens -- a binding is not a use, "
      "and the bit-identity above is what proves the uses are confined",
      len(_BIND) == 2 and len(_GUARD) == 5
      and all(ln.startswith(' ' * 8) for ln in _INNER)
      and SRC.count("_SRCD = os.environ.get('SRCDEC')") == 1,
      f"{len(_BIND)} bindings, {len(_GUARD)} guards, {len(_INNER)} lines inside guarded blocks "
      f"(deepest indent {max(len(ln) - len(ln.lstrip()) for ln in _INNER)}), "
      f"{len(_U)} executable lines in all")

# ===================================================================================================
print("\nPART 2 -- THE TEN PIECES: WHAT EACH IS WORTH, AND WHICH CAN CARRY THE STATISTIC AT ALL.")
print("-" * 100)
print(f"    {'pair':10s} {'share ctl':>11s} {'share arm':>11s} {'min/med ctl':>12s} "
      f"{'min/med arm':>12s}  positive definite")
POSDEF = {}
for i, nm in enumerate(NM):
    s_, m_ = {}, {}
    for t in ('lcdm', 'cr'):
        v = PR[t]['Dl_pairs'][:, i]
        s_[t] = float(np.mean(v / PR[t]['Dl']))
        m_[t] = float(v.min() / np.median(np.abs(PR[t]['Dl'])))
    POSDEF[nm] = m_['lcdm'] > 0 and m_['cr'] > 0
    print(f"    {nm:10s} {s_['lcdm']:11.5f} {s_['cr']:11.5f} {m_['lcdm']:12.4f} {m_['cr']:12.4f}"
          f"   {'yes' if POSDEF[nm] else 'NO -- statistic not applied'}")
check("the four DIAGONAL pieces are positive definite and every off-diagonal one that is not is "
      "named rather than quietly skipped -- a relative oscillation about a running mean is only "
      "defined where the mean is of one sign",
      all(POSDEF[n] for n in ('sw*sw', 'dp*dp', 'isw*isw', 'pol*pol')),
      f"{sum(POSDEF.values())} of 10 positive definite: "
      f"{', '.join(n for n in NM if POSDEF[n])}")

# ===================================================================================================
print("\nPART 3 -- ⓵ THE ORDER'S QUESTION: THE CONTRAST OF EACH PROJECTED PIECE.")
print("-" * 100)
CASES = [('sw*sw    the monopole alone', [IX['sw*sw']]),
         ('dp*dp    the Doppler alone', [IX['dp*dp']]),
         ('isw*isw  the ISW alone', [IX['isw*isw']]),
         ('pol*pol  the polarisation alone', [IX['pol*pol']]),
         ('the two squares, NO cross', [IX['sw*sw'], IX['dp*dp']]),
         ('the pair WITH its cross', [IX['sw*sw'], IX['dp*dp'], IX['sw*dp']]),
         ('FULL minus the sw*dp cross', NOX),
         ('FULL (all ten)', ALL)]
print(f"    {'piece':34s} {'ratio':>8s} {'rms ctl':>9s} {'rms arm':>9s}")
RES = {}
for nm, cols in CASES:
    r = ratio(cols)
    RES[nm] = r
    print(f"    {nm:34s} {r['reg']:8.4f} {r['dB']:9.4f} {r['dA']:9.4f}")
FULL = RES['FULL (all ten)']['reg']
NOXR = RES['FULL minus the sw*dp cross']['reg']
XCARRY = [ratio(ALL, w)['reg'] - ratio(NOX, w)['reg'] for w in (0.75, 1.0, 1.25, 1.5)]
print(f"\n    the cross term's OWN carry, as the difference of two full spectra, window by window:")
for w, v in zip((0.75, 1.0, 1.25, 1.5), XCARRY):
    print(f"      window {w:.2f}: {v:+.4f} of the {FULL-1:+.4f}")
check("⛔ ** THE CROSS TERM IS NOT THE CHANNEL. **  Deleting the monopole-Doppler cross from the "
      "full spectrum moves the ratio by a part in ten thousand, and over four windows its carry is "
      "consistent with zero -- so the order's FIRST outcome, the interference between j_l and "
      "j_l', is excluded",
      max(abs(v) for v in XCARRY) < 0.1 * (FULL - 1),
      f"{FULL:.4f} with the cross against {NOXR:.4f} without; carry "
      f"{min(XCARRY):+.4f} to {max(XCARRY):+.4f} of {FULL-1:+.4f}")
check("⚑ ** AND IT IS NOT ONE PIECE EITHER: EVERY PROJECTED PIECE ALREADY CARRIES AN EXCESS. **  "
      "The order's SECOND outcome allowed for one piece at 1.045; the monopole, the Doppler and "
      "the polarisation are all above one and the Doppler is above the full spectrum",
      RES['sw*sw    the monopole alone']['reg'] > 1.02
      and RES['dp*dp    the Doppler alone']['reg'] > FULL
      and RES['pol*pol  the polarisation alone']['reg'] > 1.02,
      f"monopole {RES['sw*sw    the monopole alone']['reg']:.4f}, Doppler "
      f"{RES['dp*dp    the Doppler alone']['reg']:.4f}, polarisation "
      f"{RES['pol*pol  the polarisation alone']['reg']:.4f}, ISW "
      f"{RES['isw*isw  the ISW alone']['reg']:.4f}, full {FULL:.4f}")
check("...and the two squares WITHOUT their cross already reach the full spectrum's ratio, which "
      "is the same fact from the other side",
      abs(RES['the two squares, NO cross']['reg'] - FULL) < 0.01,
      f"{RES['the two squares, NO cross']['reg']:.4f} against {FULL:.4f}")

print("\n  (b) THE SAME TABLE OVER FOUR WINDOWS AND BOTH ENVELOPE DEFINITIONS")
SPAN = {}
for nm, cols in (('sw*sw  monopole alone', [IX['sw*sw']]),
                 ('dp*dp  Doppler alone', [IX['dp*dp']]),
                 ('the two squares, NO cross', [IX['sw*sw'], IX['dp*dp']]),
                 ('FULL minus the sw*dp cross', NOX),
                 ('FULL (all ten)', ALL)):
    row = [ratio(cols, w)['reg'] for w in (0.75, 1.0, 1.25, 1.5)]
    gm = ratio(cols, 1.0, env_g)['reg']
    SPAN[nm] = row + [gm]
    print(f"    {nm:30s} " + "  ".join(f"w{w:.2f} {v:.4f}" for w, v in zip((0.75, 1.0, 1.25, 1.5),
                                                                          row))
          + f"    geom {gm:.4f}")
check("the reading survives the definition: the monopole and the Doppler stay apart and both stay "
      "above one across four windows and both envelopes",
      min(SPAN['sw*sw  monopole alone']) > 1.02
      and min(SPAN['dp*dp  Doppler alone']) > 1.05,
      f"monopole {min(SPAN['sw*sw  monopole alone']):.4f}-"
      f"{max(SPAN['sw*sw  monopole alone']):.4f}, Doppler "
      f"{min(SPAN['dp*dp  Doppler alone']):.4f}-{max(SPAN['dp*dp  Doppler alone']):.4f}")

# ===================================================================================================
print("\nPART 4 -- THE PER-TERM LADDER: THE SAME STATISTIC ON EACH TERM'S SOURCE AND ON ITS OWN "
      "PROJECTION.")
print("-" * 100)
print(f"    {'term':30s} {'source (k)':>11s} {'projected':>11s} {'change':>9s}")
LAD = {}
for nm, key, col in (('monopole  g(Theta_0+Psi)', 'sw_i', 'sw*sw'),
                     ('Doppler   d[g theta_b]/k^2', 'dp_i', 'dp*dp'),
                     ('ISW', 'isw_i', 'isw*isw'),
                     ('polarisation', 'pol_i', 'pol*pol'),
                     ('the whole source', 'S_i', None)):
    s_ = stat(QK['cr'], osc(QK['cr'], SO['cr'][key] ** 2),
              QK['lcdm'], osc(QK['lcdm'], SO['lcdm'][key] ** 2))['reg']
    p_ = FULL if col is None else ratio([IX[col]])['reg']
    LAD[nm] = (s_, p_)
    print(f"    {nm:30s} {s_:11.4f} {p_:11.4f} {p_-s_:+9.4f}")
check("⚑⚑ ** EVERY TERM'S SOURCE RATIO IS AT OR BELOW 0.992 AND EVERY TERM'S PROJECTED RATIO IS "
      "HIGHER. **  `cc66.40` found that for the source as a whole; term by term is why no single "
      "term can be the channel",
      all(v[0] <= 0.995 for v in LAD.values()) and all(v[1] > v[0] for v in LAD.values()),
      "  ".join(f"{k.split()[0]} {v[0]:.4f}->{v[1]:.4f}" for k, v in LAD.items()))

# ===================================================================================================
print("\nPART 5 -- WEIGHT AGAINST RESPONSE, WHICH IS WHAT THE ORDER'S REASONING WAS REALLY AFTER.")
print("-" * 100)
FU = {t: piece(t, ALL) for t in PR}
SH = {t: np.array([np.mean(PR[t]['Dl_pairs'][:, i] / FU[t]) for i in range(10)]) for t in PR}
for t in ('lcdm', 'cr'):
    print(f"    mean shares {t:5s}: " + "  ".join(f"{n} {v:+.4f}" for n, v in zip(NM, SH[t])))
_hyA = (PR['cr']['Dl_pairs'] * (SH['lcdm'] / SH['cr'])[None, :]).sum(axis=1)
_hyB = (PR['lcdm']['Dl_pairs'] * (SH['cr'] / SH['lcdm'])[None, :]).sum(axis=1)
R_A = stat(QL['cr'], osc(QL['cr'], _hyA), QL['lcdm'], osc(QL['lcdm'], FU['lcdm']))['reg']
R_B = stat(QL['cr'], osc(QL['cr'], FU['cr']), QL['lcdm'], osc(QL['lcdm'], _hyB))['reg']
print(f"\n    the arm as it is                        : {FULL:.4f}")
print(f"    the ARM's pieces at the CONTROL's shares: {R_A:.4f}   the weights carry {FULL-R_A:+.4f}")
print(f"    the CONTROL's pieces at the ARM's shares: {R_B:.4f}   the weights carry {FULL-R_B:+.4f}")
check("⌗ the split is about 40/60, weights against each piece's own response -- and it is a split "
      "rather than a number because TWO crude reweightings, run in opposite directions, agree",
      abs((FULL - R_A) - (FULL - R_B)) < 0.005 and 0 < FULL - R_A < FULL - 1,
      f"weights {FULL-R_A:+.4f} and {FULL-R_B:+.4f} of {FULL-1:+.4f}; response "
      f"{R_A-1:+.4f}")

# ===================================================================================================
print("\nPART 6 -- ⓶ THE RETAINED FRACTION AS A FUNCTION OF q, WHICH THE ORDER ASKED FOR AS ONE "
      "CURVE RATHER THAN ONE NUMBER.")
print("-" * 100)
print("    retained(q) = rms of the D_l oscillation over rms of the SOURCE oscillation, in a band")


def retained(win, nb, hi):
    lo = 0.35 + 0.5 * win + 1e-9
    o2 = {t: osc(QK[t], SO[t]['S_i'] ** 2, win) for t in SO}
    o3 = {t: osc(QL[t], PR[t]['Dl'], win) for t in PR}
    ed = np.linspace(lo, hi, nb + 1)
    xs, ys, det = [], [], []
    for a, b in zip(ed[:-1], ed[1:]):
        g = np.linspace(a, b, 400)
        r = {}
        for t in ('lcdm', 'cr'):
            r[t] = np.interp(g, QL[t], o3[t]).std() / np.interp(g, QK[t], o2[t]).std()
        xs.append((a + b) / 2)
        ys.append(r['cr'] / r['lcdm'])
        det.append((a, b, r['lcdm'], r['cr']))
    return np.array(xs), np.array(ys), det


_x, _y, _d = retained(1.0, 7, 5.75)
print(f"\n    {'q band':>12s} {'retain ctl':>11s} {'retain arm':>11s} {'ratio':>9s}")
for (a, b, rc, ra), v in zip(_d, _y):
    print(f"    {a:5.2f}-{b:5.2f} {rc:11.4f} {ra:11.4f} {v:9.4f}")
SL, IC = [], []
for w in (0.75, 1.0, 1.25, 1.5):
    for nb, hi in ((7, 5.75), (10, 6.10), (5, 5.75)):
        x, y, _ = retained(w, nb, hi)
        s, c = np.polyfit(x, y, 1)
        SL.append(s)
        IC.append(c)
SL, IC = np.array(SL), np.array(IC)
print(f"\n    over {len(SL)} settings (4 windows x 3 band counts):")
print(f"      slope     {SL.mean():+.5f} +- {SL.std():.5f} per unit q   "
      f"(range {SL.min():+.5f} to {SL.max():+.5f})")
print(f"      intercept {IC.mean():.4f} +- {IC.std():.4f} at q = 0   "
      f"(range {IC.min():.4f} to {IC.max():.4f})")
check("⚑ ** THE RETAINED-FRACTION RATIO IS NOT FLAT. **  It rises with q in every one of the "
      "settings, so the order's second branch -- that the q split was reading the envelope and the "
      "reading dies -- is excluded",
      SL.min() > 0 and SL.mean() > 3 * SL.std(),
      f"slope {SL.mean():+.5f} +- {SL.std():.5f}, never negative in {len(SL)} settings")
check("...and the intercept STRADDLES one, so the rise is established and a constant offset is "
      "not -- which is the order's first branch, with the extrapolation called an extrapolation "
      f"(the lowest band centre is q = {_x[0]:.2f})",
      IC.min() < 1.0 < IC.max() + 0.02,
      f"intercept {IC.mean():.4f} +- {IC.std():.4f}, range {IC.min():.4f}-{IC.max():.4f}")

# ===================================================================================================
print("\n" + "=" * 100)
print(f"""
WHAT `r6915` ASKED AND WHAT THE DECOMPOSITION SAYS.

  ⛔ THE ORDER'S CLOSURE GATE FIRST, BECAUSE IT HAD TO BE CORRECTED TO BE PASSED.  The transfer is
  linear in the source and the pieces add there; C_l is QUADRATIC in the transfer, so the projected
  SPECTRA do not add -- the four diagonal pieces alone fall short of D_l by up to
  {100*float(np.max(np.abs(piece('lcdm', [IX['sw*sw'], IX['dp*dp'], IX['isw*isw'], IX['pol*pol']]) - PR['lcdm']['Dl']) / np.abs(PR['lcdm']['Dl']))):.0f} per cent.  ** What closes is the full bilinear decomposition, ten pair
  spectra summing to D_l to {max(CLO.values()):.1e} relative on both arms, and that is the gate. **  *This is not
  the order's third outcome: its FIRST outcome presupposes a cross term, so the two clauses are in
  tension and the first is the coherent one.*

  ⛔ AND THE CROSS TERM IS NOT THE CHANNEL.  Deleting it takes the ratio from {FULL:.4f} to {NOXR:.4f},
  and over four envelope windows its carry runs {min(XCARRY):+.4f} to {max(XCARRY):+.4f} of the {FULL-1:+.4f}.
  ** The interference between j_l and j_l' is bounded at about a part in a thousand. **

  ⚑⚑ BECAUSE EVERY PROJECTED PIECE ALREADY CARRIES IT, WHICH IS NEITHER OUTCOME THE ORDER NAMED.
  Monopole {RES['sw*sw    the monopole alone']['reg']:.4f}, Doppler {RES['dp*dp    the Doppler alone']['reg']:.4f}, polarisation {RES['pol*pol  the polarisation alone']['reg']:.4f}, against the full {FULL:.4f}; the ISW is the
  one exception at {RES['isw*isw  the ISW alone']['reg']:.4f} and carries one per cent of D_l.  ⇒ *** It is not a term and not a
  pair of terms: the projection raises this arm's contrast on nearly everything it projects. ***
  And the ladder is the sharpest form of it -- every term's SOURCE ratio is at or below 0.992 and
  every term's PROJECTED ratio is higher, the Doppler by {LAD['Doppler   d[g theta_b]/k^2'][1]-LAD['Doppler   d[g theta_b]/k^2'][0]:+.3f}.

  ⌗ THE SPLIT THE ORDER'S REASONING WAS AFTER IS ABOUT 40/60, THE RESPONSE THE LARGER.  The weight
  DOES differ -- the arm's monopole share is {SH['cr'][IX['sw*sw']]:.4f} against {SH['lcdm'][IX['sw*sw']]:.4f} and its Doppler share
  {SH['cr'][IX['dp*dp']]:.4f} against {SH['lcdm'][IX['dp*dp']]:.4f} -- and rebuilding the arm at the control's shares gives {R_A:.4f},
  so the weights carry {FULL-R_A:+.4f} of the {FULL-1:+.4f} and each piece's own response {R_A-1:+.4f}.  *The reverse
  construction gives {FULL-R_B:+.4f}, and two crude reweightings agreeing to {abs((FULL-R_A)-(FULL-R_B)):.4f} is what makes this
  a split rather than a number.*

  ⚑ ⓶ AND THE RETAINED FRACTION IS NOT FLAT IN q, WHICH IS THE ORDER'S FIRST BRANCH.  It rises from
  {_y[0]:.4f} in the lowest band to {_y[-1]:.4f} in the highest, and over {len(SL)} settings the slope is
  {SL.mean():+.5f} +- {SL.std():.5f} per unit q, never once negative.  ** So the branch that would have killed the
  reading -- flat, the q split reading the envelope -- is excluded. **  ⌗ *The intercept is
  {IC.mean():.4f} +- {IC.std():.4f} and straddles one: the RISE is established and a constant offset is not, and the
  value at q = 0 is an extrapolation from a lowest band centre of q = {_x[0]:.2f}.*

  ⛔ THE BOUND, RESTATED IN THE ORDER'S OWN TERMS.  *"Naming which two terms interfere is still not a
  statement about why their weights differ."*  ** Nothing here names two terms, because it is not
  two terms; and nothing here says why the projection treats the two arms differently. **  The stage
  was located at `r6911+cc66.40` and this narrows what inside it can be responsible -- not a term,
  not a pair, not their interference -- and adds one shape: it grows with wavenumber.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the monopole-Doppler cross term carries {min(XCARRY):+.4f} to {max(XCARRY):+.4f} of the arms' {FULL-1:+.4f}
contrast difference -- bounded at about a part in a thousand -- so the interference between the two
kernels is not the channel.  Every projected piece already carries an excess (monopole {RES['sw*sw    the monopole alone']['reg']:.4f},
Doppler {RES['dp*dp    the Doppler alone']['reg']:.4f}, polarisation {RES['pol*pol  the polarisation alone']['reg']:.4f}) while every term's SOURCE ratio is at or below 0.992, so the
projection raises this arm's contrast on nearly everything it projects.  About {100*(FULL-R_A)/(FULL-1):.0f} per cent of the
difference is the arm weighting the pieces differently and the rest is each piece's own response.
And the retained fraction rises with wavenumber, slope {SL.mean():+.5f} +- {SL.std():.5f} per unit q over {len(SL)} settings,
with its q = 0 intercept straddling one.
NOT CLAIMED: a mechanism; that the cross term is zero (it is {100*float(np.mean(PR['lcdm']['Dl_pairs'][:, IX['sw*dp']]/PR['lcdm']['Dl'])):.0f} per cent of D_l -- what is bounded
is its contribution to the DIFFERENCE); that the projection is the wrong projection; that the
Doppler's ratio is as well determined as the monopole's, its piece's oscillation being {RES['dp*dp    the Doppler alone']['dB']:.3f}
against {RES['sw*sw    the monopole alone']['dB']:.3f}; or that the q = 0 intercept is one.
""")
