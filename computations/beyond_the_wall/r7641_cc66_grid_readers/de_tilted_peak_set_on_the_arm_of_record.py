#!/usr/bin/env python3
"""r7641 item 2, grid reader 5 of 6: the de-tilted peak set read on the ARM OF RECORD.

`P15_the_de_tilted_peak_set_is_the_phase_observable_the_slope_was_not_…` reads the two direction
grids and the driving pair.  All four CR-side pointers have arm-of-record siblings, so unlike grid
reader 1 this receipt is re-pointable in full:

    r7093_directions/grid_oneclock/cr_*     -> .../grid_oneclock_leafrec1/cr_*
    r7095_directions/grid_licensed/cr_*     -> .../grid_licensed_leafrec1/cr_*
    spectra/c54.186_cr_L3000.npz            -> spectra/c54.186_cr_L3000_leafrec1.npz
    spectra/c54.193_cr_nodrive_L3000.npz    -> spectra/c54.193_cr_nodrive_L3000_leafrec1.npz

** AND `BASEVAL` MOVES WITH THEM, WHICH IS THE PART A POINTER-ONLY RE-POINT WOULD GET WRONG. **  The
gated quantities are LOGARITHMIC derivatives, `d(phi)/dln(theta)`, so the base value is a divisor.
The arm-of-record grids are centred on the arm of record's own fitted point -- read here from each
grid's `manifest['point']`, not assumed -- so leaving `BASEVAL['cr']` at the distances' point would
scale every arm-of-record derivative by the ratio of two different centres.  *That is the same fact
that BLOCKED grid reader 1, acting here as a correction rather than a blocker: reader 1's question
was about the distance from the distances' point, and this receipt's is about the response AT the
centre, which every grid has.*

** THE CARRY (`band_excess_own`, r7639+cc66.22) CANNOT CHANGE ANY GATED NUMBER, AND THAT IS PROVED
BY CONSTRUCTION AND THEN MEASURED. **  The carry adds a rigid offset to the arm's comb phase.  Every
gated quantity here is a DIFFERENCE of the common offset between two spectra of the SAME arm --
`(phi_plus - phi_minus) * base/(2*step)` -- so a constant common to both cancels identically.  The
gate below injects a rigid shift into the phase and requires every derivative unchanged to machine
precision.  ⇒ ** Class 2 in effect: the carry is an identity on this statistic, not merely
inapplicable to it. **

Nothing is edited by this file; every figure is reported old -> new in `FOR_66.md`.
"""
import ast
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BW, 'spectra')

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


# ** lifted VERBATIM from the receipt. **
LMIN, LMAX = 150.0, 1600.0
NPK = 5
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
PARS = ('H0', 'OM', 'NS', 'WB')
DISTANCES = {'H0': 68.60, 'OM': 0.2973, 'NS': 0.965, 'WB': 0.0224}
CTL_BASE = {'H0': 67.40, 'OM': 0.3150, 'NS': 0.965, 'WB': 0.0224}

#: the two arms as pointer sets.  The control's grids and its driving pair are in neither column:
#: they do not move, and the `_leafrec1` directories hold `cr_*` only.
ARM = {'namesake': dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock'),
                        gl=os.path.join(BW, 'r7095_directions', 'grid_licensed'),
                        on='c54.186_cr_L3000.npz', off='c54.193_cr_nodrive_L3000.npz'),
       'aor': dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1'),
                   gl=os.path.join(BW, 'r7095_directions', 'grid_licensed_leafrec1'),
                   on='c54.186_cr_L3000_leafrec1.npz',
                   off='c54.193_cr_nodrive_L3000_leafrec1.npz')}
CTL = dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock'),
           gl=os.path.join(BW, 'r7095_directions', 'grid_licensed'),
           on='c54.186_lcdm_L3000.npz', off='c54.193_lcdm_nodrive_L3000.npz')


def centre_of(gdir, tag='cr'):
    """the grid's own centre, from `manifest['point']`.  No manifest => the distances' point."""
    z = np.load(os.path.join(gdir, f'{tag}_base.npz'), allow_pickle=True)
    if 'manifest' not in z.files:
        return dict(DISTANCES), False
    m = z['manifest'].item()
    if isinstance(m, (bytes, str)):
        m = ast.literal_eval(m if isinstance(m, str) else m.decode())
    p = m.get('point', {})
    return dict(H0=float(p['CRH0']), OM=float(p['CROM']), NS=float(p['NS']),
                WB=float(p['WBH2'])), True


def peak_series(path, halfwin=40.0, detilt=True):
    """the receipt's own locator: de-tilt, find the maxima, refine by a parabola on the samples."""
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt if detilt else Dl.copy()
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    D = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(D) - 2)
           if D[i] > D[i - 1] and D[i] >= D[i + 1] and D[i] > D[i - 2] and D[i] >= D[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - halfwin) & (ls <= l0 + halfwin)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA, tilt


def phi_alt(path, halfwin=40.0, detilt=True, shift=0.0):
    """the common offset and the odd-even alternation, in units of l_A.

    `shift` is the CARRY PROBE and nothing else: a rigid offset injected into the comb phase, which
    is what mapping the arm onto the control's comb would add.  It is 0.0 everywhere but in the one
    gate that measures whether the derivatives notice it.
    """
    pk, lA, _t = peak_series(path, halfwin, detilt)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA + shift
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum())


def deriv(gdir, arm, par, base, halfwin=40.0, detilt=True, shift=0.0):
    sm = phi_alt(os.path.join(gdir, f'{arm}_{par}m.npz'), halfwin, detilt, shift)
    sp = phi_alt(os.path.join(gdir, f'{arm}_{par}p.npz'), halfwin, detilt, shift)
    g = base[par] / (2 * STEP[par])
    return (sp[0] - sm[0]) * g, (sp[1] - sm[1]) * g


print(__doc__)
print(BAR)
print("  PART 1 -- EACH GRID'S OWN CENTRE, AND WHY `BASEVAL` HAS TO MOVE WITH THE POINTER")
print(BAR)
BASE = {}
for arm in ('namesake', 'aor'):
    BASE[arm], has = centre_of(ARM[arm]['go'])
    print(f"    {arm:>9} ({os.path.basename(ARM[arm]['go']):>24}): "
          + "  ".join(f"{k} {BASE[arm][k]:.6f}" for k in PARS)
          + f"   [{'manifest' if has else 'no manifest -- the distances point'}]")
_gl, _ = centre_of(ARM['aor']['gl'])
print(f"    and the licensed grid agrees: " + "  ".join(f"{k} {_gl[k]:.6f}" for k in PARS))
check("⛔ THE ARM-OF-RECORD GRIDS SIT AT THE ARM OF RECORD'S OWN FITTED POINT, both of them, and "
      "the namesake grids at the distances' point.  ⇒ ** So a pointer-only re-point would divide "
      "every arm-of-record log-derivative by the wrong base: n_s alone is out by 5 per cent and "
      "omega_b by 3 **",
      all(abs(BASE['namesake'][k] - DISTANCES[k]) < 1e-9 for k in PARS)
      and abs(BASE['aor']['H0'] - 68.57073) < 1e-5 and abs(BASE['aor']['OM'] - 0.291246) < 1e-6
      and all(abs(_gl[k] - BASE['aor'][k]) < 1e-9 for k in PARS),
      f"namesake H0 {BASE['namesake']['H0']:.5f}, arm of record H0 {BASE['aor']['H0']:.5f} / "
      f"NS {BASE['aor']['NS']:.6f}")
print(f"    the base ratios the re-point applies: "
      + "  ".join(f"{k} x{BASE['aor'][k] / BASE['namesake'][k]:.4f}" for k in PARS))

print()
print(BAR)
print("  PART 2 -- THE DE-TILT CONTROL, BOTH ARMS")
print(BAR)
SW = {}
for arm in ('namesake', 'aor'):
    raw, det = [], []
    for hw in (25.0, 40.0, 55.0, 75.0):
        for dt, box in ((False, raw), (True, det)):
            dn = deriv(ARM[arm]['go'], 'cr', 'NS', BASE[arm], hw, dt)
            dw = deriv(ARM[arm]['go'], 'cr', 'WB', BASE[arm], hw, dt)
            box.append((abs(dn[0]), abs(dw[0])))
            SW[(arm, dt, hw)] = (dn, dw)
    r_ = [a for a, _ in raw]
    d_ = [a for a, _ in det]
    print(f"    {arm:>9}: |dphi/dlnNS| raw {min(r_):.5f}-{max(r_):.5f}, de-tilted "
          f"{min(d_):.5f}-{max(d_):.5f}  -- a factor of {np.mean(r_) / np.mean(d_):.0f}")
    SW[(arm, 'summary')] = (min(r_), max(r_), min(d_), max(d_), np.mean(r_) / np.mean(d_))

print()
print(BAR)
print("  PART 3 -- THE SEPARATION: THE BARYON DIRECTION AGAINST A PURE TILT")
print(BAR)
D = {}
RAT = {}
print(f"    {'arm':>9} {'grid':9s} {'par':3s} {'dphi/dln':>11s} {'dalt/dln':>11s}")
for arm in ('namesake', 'aor'):
    for gname in ('go', 'gl'):
        for par in PARS:
            D[(arm, gname, par)] = deriv(ARM[arm][gname], 'cr', par, BASE[arm])
            print(f"    {arm:>9} {gname:9s} {par:3s} {D[(arm, gname, par)][0]:+11.5f} "
                  f"{D[(arm, gname, par)][1]:+11.5f}")
    RAT[arm] = (abs(D[(arm, 'go', 'WB')][0] / D[(arm, 'go', 'NS')][0]),
                abs(D[(arm, 'go', 'WB')][1] / D[(arm, 'go', 'NS')][1]))
    print(f"    {arm:>9}: WB:NS = {RAT[arm][0]:.1f}x on the common offset, {RAT[arm][1]:.1f}x on "
          f"the alternation")
for par in PARS:
    D[('ctl', 'go', par)] = deriv(CTL['go'], 'lcdm', par, CTL_BASE)
    D[('ctl', 'gl', par)] = deriv(CTL['gl'], 'lcdm', par, CTL_BASE)
RAT['ctl'] = (abs(D[('ctl', 'go', 'WB')][0] / D[('ctl', 'go', 'NS')][0]),
              abs(D[('ctl', 'go', 'WB')][1] / D[('ctl', 'go', 'NS')][1]))
print(f"    {'control':>9}: WB:NS = {RAT['ctl'][0]:.1f}x / {RAT['ctl'][1]:.1f}x   (unchanged -- the "
      f"control's grids do not move)")

CONV = {}
for arm in ('namesake', 'aor'):
    CONV[arm] = max(max(abs(D[(arm, 'gl', p)][i] / D[(arm, 'go', p)][i]) for i in (0, 1))
                    for p in PARS)
    print(f"    {arm:>9}: worst licensed/oneclock disagreement {CONV[arm]:.2f}x")
NSC = {a: [abs(D[(a, g, 'NS')][0]) for g in ('go', 'gl')] for a in ('namesake', 'aor')}

check("⛔ THE LICENCE GATE: the namesake arm reproduces every figure the receipt publishes -- the "
      "de-tilt factor of 22 with its raw and de-tilted ranges, WB:NS at 11.3x and 21.4x on the arm "
      "and 11.4x/22.6x on the control, and the worst convention disagreement at 2.01x.  ⇒ ** So "
      "what moves below is the arm and the base, not the instrument **",
      abs(SW[('namesake', 'summary')][4] - 22) < 0.5
      and abs(SW[('namesake', 'summary')][0] - 0.04887) < 5e-5
      and abs(SW[('namesake', 'summary')][1] - 0.06015) < 5e-5
      and abs(RAT['namesake'][0] - 11.3) < 0.05 and abs(RAT['namesake'][1] - 21.4) < 0.05
      and abs(RAT['ctl'][0] - 11.4) < 0.05 and abs(RAT['ctl'][1] - 22.6) < 0.05
      and abs(CONV['namesake'] - 2.01) < 0.01,
      f"de-tilt x{SW[('namesake', 'summary')][4]:.0f} ({SW[('namesake', 'summary')][0]:.5f}-"
      f"{SW[('namesake', 'summary')][1]:.5f}), arm {RAT['namesake'][0]:.1f}x/"
      f"{RAT['namesake'][1]:.1f}x, control {RAT['ctl'][0]:.1f}x/{RAT['ctl'][1]:.1f}x, "
      f"convention {CONV['namesake']:.2f}x")

print()
print(BAR)
print("  PART 4 -- THE DRIVING PAIR, RE-ASKED ON THE ARM OF RECORD")
print(BAR)
GAPS = {}


def gaps(path):
    pk, lA, _ = peak_series(path)
    return float(np.max(np.abs(np.diff(pk / lA) - 1.0))), pk / lA


for lab, path in (('grid cr_base, namesake', os.path.join(ARM['namesake']['go'], 'cr_base.npz')),
                  ('grid cr_base, AOR', os.path.join(ARM['aor']['go'], 'cr_base.npz')),
                  ('cr driving ON, namesake', os.path.join(SP, ARM['namesake']['on'])),
                  ('cr driving ON, AOR', os.path.join(SP, ARM['aor']['on'])),
                  ('cr driving OFF, namesake', os.path.join(SP, ARM['namesake']['off'])),
                  ('cr driving OFF, AOR', os.path.join(SP, ARM['aor']['off'])),
                  ('lcdm driving ON', os.path.join(SP, CTL['on'])),
                  ('lcdm driving OFF', os.path.join(SP, CTL['off']))):
    GAPS[lab], ser = gaps(path)
    print(f"    {lab:>26} peaks/l_A = {np.round(ser, 3)}  worst gap error {GAPS[lab]:.3f}")

# ⛔⛭⛭ ** Ⓓ① DOES NOT HOLD ON THE ARM OF RECORD, AND THIS IS THE FINDING OF THIS FILE. **  The
#   receipt refused to claim a CR driving number because the CR arm's banked driving-ON spectrum had
#   no integer-spaced peak series -- worst gap error 0.275 against the grid's 0.105, a factor of
#   2.6 -- and revised `cc66.155`'s ask from eight runs to TEN on exactly that ground.  On the arm
#   of record the same spectrum reads 0.103 against the grid's 0.102: ** a factor of 1.0. **
#   ⇒ *So the obstruction was the namesake arm's, and on the arm of record the statistic CAN read
#   the CR driving pair.  The gate is therefore written the way round the measurement puts it, and
#   the step it unblocks is computed immediately below rather than left as a note.*
check("⛔⛭⛭ Ⓓ① IS NAMESAKE-SPECIFIC: on the arm of record the CR driving-ON spectrum's peak series "
      "IS integer-spaced -- worst gap error 0.103 against the grid's own 0.102, a factor of 1.0, "
      "where the namesake arm's was 0.275 against 0.105.  ⇒ ** The receipt's stated reason for "
      "claiming no CR driving number, and for revising the ask from eight runs to ten, does not "
      "survive the re-point.  The CR driving step is therefore measured below **",
      GAPS['cr driving ON, AOR'] < 1.25 * GAPS['grid cr_base, AOR']
      and GAPS['cr driving ON, namesake'] > 2.5 * GAPS['grid cr_base, namesake'],
      f"arm of record {GAPS['cr driving ON, AOR']:.3f} against the grid's "
      f"{GAPS['grid cr_base, AOR']:.3f} (factor "
      f"{GAPS['cr driving ON, AOR'] / GAPS['grid cr_base, AOR']:.1f}); namesake "
      f"{GAPS['cr driving ON, namesake']:.3f} against {GAPS['grid cr_base, namesake']:.3f} "
      f"(factor {GAPS['cr driving ON, namesake'] / GAPS['grid cr_base, namesake']:.1f})")

#: ** THE STEP Ⓓ① HAD BLOCKED, NOW THAT IT READS. **  Measured, not asserted -- and reported with the
#: one thing that keeps it honest: the arm's driving pair is a DIFFERENT VINTAGE from its grids
#: (`c54.186`/`c54.193` at L3000 against the grids' own configuration), so this is the step the
#: receipt said needed a `NODRIVE` pair at the grids' configuration to measure cleanly.  What has
#: changed is that the statistic can now read the pair at all, which is what Ⓓ① denied.
_cr_on = phi_alt(os.path.join(SP, ARM['aor']['on']))
_cr_off = phi_alt(os.path.join(SP, ARM['aor']['off']))
_cdphi, _cdalt = _cr_off[0] - _cr_on[0], _cr_off[1] - _cr_on[1]
_awb = D[('aor', 'go', 'WB')]
print(f"    ⛭ THE CR DRIVING STEP, ON THE ARM OF RECORD: phi {_cr_on[0]:+.5f} -> "
      f"{_cr_off[0]:+.5f} (Dphi {_cdphi:+.5f}), alt {_cr_on[1]:+.5f} -> {_cr_off[1]:+.5f} "
      f"(Dalt {_cdalt:+.5f})")
print(f"       against the arm's own baryon direction {_awb[0]:+.5f} / {_awb[1]:+.5f}")
check("⛭⛭ AND THE ORTHOGONALITY THE ASK RESTED ON NOW HOLDS ON THE ARM ITSELF, not only on the "
      "control: the CR driving step and the arm of record's own baryon direction move the peak set "
      "OPPOSITE ways on both components.  ⛔ *Reported with its limit: the driving pair is a "
      "different vintage from the grids, so this is the step the receipt said needs a NODRIVE pair "
      "at the grids' configuration -- what has changed is that the statistic can read the pair at "
      "all, which is what Ⓓ① denied*",
      _cdphi * _awb[0] < 0 and _cdalt * _awb[1] < 0,
      f"Dphi {_cdphi:+.5f} against {_awb[0]:+.5f}, Dalt {_cdalt:+.5f} against {_awb[1]:+.5f}")

_on = phi_alt(os.path.join(SP, CTL['on']))
_off = phi_alt(os.path.join(SP, CTL['off']))
_dphi, _dalt = _off[0] - _on[0], _off[1] - _on[1]
for arm in ('namesake', 'aor'):
    _wb = D[(arm, 'go', 'WB')]
    print(f"    the control's driving step Dphi {_dphi:+.5f} / Dalt {_dalt:+.5f} against the "
          f"{arm} baryon direction's {_wb[0]:+.5f} / {_wb[1]:+.5f}   "
          f"{'OPPOSITE on both' if _dphi * _wb[0] < 0 and _dalt * _wb[1] < 0 else 'NOT opposite'}")
check("⛭ Ⓓ② SURVIVES THE RE-POINT: the control's driving pair and the arm of record's baryon "
      "direction still move the peak set OPPOSITE ways on both components, which is the "
      "orthogonality the ask rested on",
      _dphi * D[('aor', 'go', 'WB')][0] < 0 and _dalt * D[('aor', 'go', 'WB')][1] < 0,
      f"Dphi {_dphi:+.5f} vs {D[('aor', 'go', 'WB')][0]:+.5f}, "
      f"Dalt {_dalt:+.5f} vs {D[('aor', 'go', 'WB')][1]:+.5f}")

print()
print(BAR)
print("  PART 5 -- THE CARRY IS AN IDENTITY HERE, AND THAT IS MEASURED")
print(BAR)
_SHIFT = 0.137
_worst = 0.0
for par in PARS:
    a = deriv(ARM['aor']['go'], 'cr', par, BASE['aor'])
    b = deriv(ARM['aor']['go'], 'cr', par, BASE['aor'], shift=_SHIFT)
    _worst = max(_worst, abs(a[0] - b[0]), abs(a[1] - b[1]))
print(f"    a rigid comb-phase shift of {_SHIFT} injected into every peak series moves the worst "
      f"arm-of-record derivative by {_worst:.3e}")
check("⛭⛭ THE CARRY CANNOT CHANGE A GATED NUMBER: every statistic here is a DIFFERENCE of the "
      "common offset between two spectra of the SAME arm, so a rigid offset -- which is exactly "
      "what mapping the arm onto the control's comb adds -- cancels identically.  ⇒ ** Class 2: "
      "the carry is an IDENTITY on this statistic, not merely inapplicable to it, and the probe "
      "measures it rather than arguing it **", _worst < 1e-12, f"worst move {_worst:.3e}")

print()
print(BAR)
print("  PART 6 -- WHAT MOVES, OLD -> NEW")
print(BAR)
_rn0 = [abs(SW[('namesake', False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
_r0 = [abs(SW[('aor', False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
ROWS = [('WB:NS on the common offset', RAT['namesake'][0], RAT['aor'][0], '.1f'),
        ('WB:NS on the alternation', RAT['namesake'][1], RAT['aor'][1], '.1f'),
        ('de-tilt factor', SW[('namesake', 'summary')][4], SW[('aor', 'summary')][4], '.0f'),
        ('|dphi/dlnNS| raw, min', SW[('namesake', 'summary')][0], SW[('aor', 'summary')][0], '.5f'),
        ('|dphi/dlnNS| raw, max', SW[('namesake', 'summary')][1], SW[('aor', 'summary')][1], '.5f'),
        ('|dphi/dlnNS| de-tilted, min', SW[('namesake', 'summary')][2],
         SW[('aor', 'summary')][2], '.5f'),
        ('|dphi/dlnNS| de-tilted, max', SW[('namesake', 'summary')][3],
         SW[('aor', 'summary')][3], '.5f'),
        ('worst convention disagreement', CONV['namesake'], CONV['aor'], '.2f'),
        ('dphi/dlnWB', D[('namesake', 'go', 'WB')][0], D[('aor', 'go', 'WB')][0], '+.5f'),
        ('dalt/dlnWB', D[('namesake', 'go', 'WB')][1], D[('aor', 'go', 'WB')][1], '+.5f'),
        ('n_s residual, min', min(NSC['namesake']), min(NSC['aor']), '.5f'),
        ('n_s residual, max', max(NSC['namesake']), max(NSC['aor']), '.5f'),
        ('grid cr_base worst gap', GAPS['grid cr_base, namesake'], GAPS['grid cr_base, AOR'], '.3f'),
        ('cr driving ON worst gap', GAPS['cr driving ON, namesake'],
         GAPS['cr driving ON, AOR'], '.3f'),
        ('cr driving OFF worst gap', GAPS['cr driving OFF, namesake'],
         GAPS['cr driving OFF, AOR'], '.3f'),
        ('raw window spread', (max(_rn0) - min(_rn0)) / np.mean(_rn0),
         (max(_r0) - min(_r0)) / np.mean(_r0), '.3f'),
        ('CR driving step, Dphi', float('nan'), _cdphi, '+.5f'),
        ('CR driving step, Dalt', float('nan'), _cdalt, '+.5f')]
print(f"    {'figure':>30} {'namesake':>12} {'arm of record':>14}   verdict")
for lab, o, n, f in ROWS:
    if o != o:                      # NaN: the namesake arm has no such figure to move FROM
        v = '⛭ NEW -- unreadable on the namesake arm (Ⓓ①)'
    elif abs(n - o) < 1e-9:
        v = 'unchanged'
    else:
        v = 'MOVED' if abs(n - o) > 0.005 * max(1e-9, abs(o)) else 'moved (trace)'
    print(f"    {lab:>30} {format(o, f):>12} {format(n, f):>14}   {v}")

print()
print(BAR)
print("  PART 7 -- THE GATES THE RECEIPT CARRIES, ON THE ARM OF RECORD")
print(BAR)
check("Ⓐ① without the de-tilt n_s still moves the common offset by more than the baryon direction "
      "does -- the control still fires on this arm",
      all(abs(SW[('aor', False, h)][0][0]) > abs(SW[('aor', False, h)][1][0])
          for h in (25.0, 40.0, 55.0)),
      " ".join(f"{abs(SW[('aor', False, h)][0][0]):.4f}>{abs(SW[('aor', False, h)][1][0]):.4f}"
               for h in (25.0, 40.0, 55.0)))
_r = [abs(SW[('aor', False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
_d = [abs(SW[('aor', True, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
_rn = [abs(SW[('namesake', False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
# ⛔ ** AND Ⓐ②'s THIRD LIMB IS ALSO NAMESAKE-SPECIFIC, WHICH IS NOT THE SAME AS THE DE-TILT
#   FAILING. **  The gate as registered required three things: the de-tilt collapses the violation
#   by ten or more, the de-tilted reading is window-independent, and the RAW reading is NOT.  The
#   first two hold on the arm of record (a factor of 21, de-tilted spread 6 per cent).  The third
#   does not: the arm of record's raw reading is already window-independent, at a spread of 1.4 per
#   cent against the namesake's 21.  ⇒ *So the de-tilt is still FORCED (Ⓐ① fires here too) and still
#   removes the violation; what is absent is the raw reading's drift, which was the receipt's
#   evidence that the de-tilt is a repair rather than a tuning.  That evidence is the namesake arm's
#   and is reported as such rather than restated as though it held.*
check("Ⓐ② the de-tilt still removes the violation by a factor of ten or more and the de-tilted "
      "reading is still window-independent -- the two limbs that survive",
      np.mean(_r) / np.mean(_d) > 10.0 and (max(_d) - min(_d)) / np.mean(_d) < 0.15,
      f"factor {np.mean(_r) / np.mean(_d):.0f}, de-tilted spread "
      f"{(max(_d) - min(_d)) / np.mean(_d):.3f}")
check("⛔ Ⓐ②'s THIRD LIMB IS NAMESAKE-SPECIFIC: the raw reading's window-DEPENDENCE, which was the "
      "receipt's evidence that the de-tilt is a repair and not a tuning, is absent on the arm of "
      "record -- a raw spread of 1.4 per cent against the namesake's 21.  ⇒ ** Reported, not "
      "restated: the de-tilt is still forced and still works here; its repair-not-tuning argument "
      "rests on the namesake arm **",
      (max(_r) - min(_r)) / np.mean(_r) < 0.05 and (max(_rn) - min(_rn)) / np.mean(_rn) > 0.15,
      f"arm of record raw spread {(max(_r) - min(_r)) / np.mean(_r):.3f}, namesake "
      f"{(max(_rn) - min(_rn)) / np.mean(_rn):.3f}")
check("Ⓑ① the peak set still separates the baryon direction from a pure tilt by an order of "
      "magnitude on both components and both arms",
      RAT['aor'][0] > 8.0 and RAT['aor'][1] > 15.0 and RAT['ctl'][0] > 8.0 and RAT['ctl'][1] > 15.0,
      f"arm of record {RAT['aor'][0]:.1f}x/{RAT['aor'][1]:.1f}x, control "
      f"{RAT['ctl'][0]:.1f}x/{RAT['ctl'][1]:.1f}x")
check("Ⓑ② and the tilt's residual leakage is still consistent across both grids rather than "
      "scattering",
      (max(NSC['aor']) - min(NSC['aor'])) / np.mean(NSC['aor']) < 0.25,
      f"{min(NSC['aor']):.5f} to {max(NSC['aor']):.5f}, spread "
      f"{(max(NSC['aor']) - min(NSC['aor'])) / np.mean(NSC['aor']):.3f}")
check("Ⓒ① and the response is still convention-robust between LEAFGEOM and LEAFREC",
      CONV['aor'] < 2.5, f"{CONV['aor']:.2f}x")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
