#!/usr/bin/env python3
"""r7641 item 2, grid reader 6 of 6: the free-period phase slope read on the ARM OF RECORD.

`P15_the_phase_slope_does_not_separate_the_loading_from_the_driving_…` reads both direction grids and
the two driving-off spectra.  Its CR-side pointers all have arm-of-record siblings, and `BASEVAL` has
to move with them for the same reason as grid reader 5: the derivatives are LOGARITHMIC.

** THREE THINGS THIS FILE ESTABLISHES, AND NONE OF THEM IS A POINTER SWAP. **

  ⒜ ** THE SUBSTANTIVE READING SURVIVES THE ARM AND IS MEASURED HERE: ** does the phase slope single
     out a carrier on the arm of record, or do all four banked directions still move it alike?

  ⒝ ** `Ⓑ②`'s LITERALS ARE THE NAMESAKE GRIDS' AND CANNOT BE CARRIED OVER. **  The gate asserts the
     grids' own `WBH2` values are exactly `['0.0216', '0.0232']` and their `NS` values
     `['0.945', '0.985']`.  The arm-of-record grids record `['0.020843', '0.021643', '0.022443']` and
     `['0.995066', '1.015066', '1.035066']` -- three each, because their base writes its values
     explicitly where the namesake's leaves them at the default.  ⇒ *A re-point must restate the gate
     as what it MEANS -- the two steps straddle the grid's own centre by exactly one step each --
     which holds on both arms and on any future centre.  The literal form holds on one bank only.*

  ⛔⛭⛭ ⒞ ** AND `Ⓑ①` IS CURRENTLY GREEN BY A PATH-PREFIX ACCIDENT, WHICH IS WORTH MORE THAN THE
     RE-POINT. **  Its third limb requires every `RBFAC` spectrum in the whole tree to sit under
     `r7201_cc66_loading_lever/`, tested with `os.path.abspath(f).startswith(os.path.abspath(ASKDIR))`
     -- a RAW STRING prefix with no separator.  70's second bank added three more `RBFAC` spectra, in
     `r7201_cc66_loading_lever_leafrec1/`.  *That directory name happens to begin with the old one, so
     the test passes.*  ** Had the bank called it anything else -- `r7639_lever_leafrec1`, say -- the
     gate would be RED on `main` right now, and for no reason connected to what it is checking. **
     ⇒ *The gate's INTENT is intact: every `RBFAC` spectrum in tree still is one of the runs this
     receipt's ask produced, the new three being those same runs re-run on the arm of record.  It is
     the implementation that is accidentally right, and this file measures the accident before the
     receipt is hardened against it.*

Nothing is edited by this file.  Figures are reported old -> new in `FOR_66.md`.
"""
import ast
import glob
import os
import sys

import numpy as np
import scipy.linalg

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


# ** lifted VERBATIM from the receipt. **
NPZ = os.path.join(BW, 'r7183_nofit_figure', 'nofit_figure_numbers.npz')
F = np.load(NPZ, allow_pickle=True)
L_FIG, ANCHOR = F['ell'], float(F['peak1'])
LC, _FACB = CS.bin_center_and_fac()
PGRID = np.arange(240.0, 400.0, 0.25)
LMAX_CUT = 1600.0
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
PARS = ('H0', 'OM', 'NS', 'WB')
DISTANCES = {'H0': 68.60, 'OM': 0.2973, 'NS': 0.965, 'WB': 0.0224}
CTL_BASE = {'H0': 67.40, 'OM': 0.3150, 'NS': 0.965, 'WB': 0.0224}

ARM = {'namesake': dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock'),
                        gl=os.path.join(BW, 'r7095_directions', 'grid_licensed'),
                        nd=os.path.join(SP, 'c54.193_cr_nodrive_L3000.npz')),
       'aor': dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1'),
                   gl=os.path.join(BW, 'r7095_directions', 'grid_licensed_leafrec1'),
                   nd=os.path.join(SP, 'c54.193_cr_nodrive_L3000_leafrec1.npz'))}
CTL = dict(go=os.path.join(BW, 'r7093_directions', 'grid_oneclock'),
           gl=os.path.join(BW, 'r7095_directions', 'grid_licensed'),
           nd=os.path.join(SP, 'c54.193_lcdm_nodrive_L3000.npz'))

#: K_OBS, the OBSERVED drift, is a SKY quantity and so is common to both arms -- which is why the
#: "move needed" column is readable on the arm of record at all.  Read from the receipt's own
#: validated route rather than retyped: the whitened no-fit residual's own best period against l_A.
_z0 = np.load(os.path.join(CTL['gl'], 'cr_base.npz'), allow_pickle=True)
KEEP = (np.isfinite(CS.bin_spectrum(_z0['ls'], _z0['Dl']))
        & (CS.BIN_HI <= LMAX_CUT) & np.isin(LC, L_FIG))
LG = LC[KEEP]
COV = CS.COV_TT[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COV))
FISH = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(KEEP.sum())))
FISH = 0.5 * (FISH + FISH.T)

QH = []
for p in PGRID:
    D = np.array([np.cos(2 * np.pi * (LG - ANCHOR) / p),
                  np.sin(2 * np.pi * (LG - ANCHOR) / p)]).T
    QH.append(np.linalg.qr(D)[0])
QH = np.array(QH)


def best_period(w):
    return float(PGRID[np.argmax(np.sum(np.einsum('pnk,n->pk', QH, w) ** 2, axis=1))])


def slope_of(path):
    """one amplitude by the likelihood's GLS, whiten, best period, slope at this file's own l_A."""
    z = np.load(path, allow_pickle=True)
    m = CS.bin_spectrum(z['ls'], z['Dl'])[KEEP]
    d = CS.X_DATA[KEEP]
    a = float((m @ FISH @ d) / (m @ FISH @ m))
    w = LINV @ (a * m - d)
    p = best_period(w)
    return 2 * np.pi * (1.0 / p - 1.0 / float(z['l_A'])), p, a


def centre_of(gdir):
    z = np.load(os.path.join(gdir, 'cr_base.npz'), allow_pickle=True)
    if 'manifest' not in z.files:
        return dict(DISTANCES), False
    m = z['manifest'].item()
    if isinstance(m, (bytes, str)):
        m = ast.literal_eval(m if isinstance(m, str) else m.decode())
    p = m['point']
    return dict(H0=float(p['CRH0']), OM=float(p['CROM']), NS=float(p['NS']),
                WB=float(p['WBH2'])), True


def switch_vals(gdir, key):
    out = set()
    for f in sorted(glob.glob(os.path.join(gdir, '*.npz'))):
        z = np.load(f, allow_pickle=True)
        if 'switches' not in z.files:
            continue
        for t in str(z['switches']).split():
            if t.startswith(key + '='):
                out.add(t.split('=')[1])
    return sorted(out)


print(__doc__)
print(BAR)
print("  PART 1 -- K_OBS, THE SKY'S OWN DRIFT, AND THE MASK BOTH ARMS SHARE")
print(BAR)
#: ** K_OBS IS THE RECEIPT'S OWN, LIFTED VERBATIM AND NOT RE-DERIVED. **  It is the OBSERVED drift:
#: the best period of the banked no-fit WHITENED residual on the bins the grid can reach, against the
#: figure bank's own `l_A`.  It is a SKY quantity, so it is common to both arms -- which is exactly
#: what makes the "move needed" column comparable between them.
#:   ⛔ *A first version of this file invented a K_OBS expression instead of lifting this one, and it
#:   crashed on a dimension mismatch rather than returning a plausible wrong number.  The crash was
#:   luck; the lift is the rule.*
_sg = np.isin(L_FIG, LG)
L_A_FIG = float(F['l_A'])
K_OBS = 2 * np.pi * (1.0 / best_period(F['nofit_cr_whitened'][_sg]) - 1.0 / L_A_FIG)
print(f"    the mask keeps {int(KEEP.sum())} bins, ell {LG.min():.0f}-{LG.max():.0f}")
_keep_aor = (np.isfinite(CS.bin_spectrum(
    *[np.load(os.path.join(ARM['aor']['gl'], 'cr_base.npz'), allow_pickle=True)[k]
      for k in ('ls', 'Dl')])) & (CS.BIN_HI <= LMAX_CUT) & np.isin(LC, L_FIG))
check("⌗ THE MASK IS THE SAME ON BOTH ARMS, asserted rather than assumed -- so the derivative table "
      "below is computed on identical bins and the two arms' numbers are comparable",
      bool(np.array_equal(KEEP, _keep_aor)),
      f"{int(KEEP.sum())} bins against {int(_keep_aor.sum())}")

print()
print(BAR)
print("  PART 2 -- THE CENTRES, AND `Ⓑ②`'s LITERALS ON BOTH ARMS")
print(BAR)
TH = {}
for arm in ('namesake', 'aor'):
    TH[arm], has = centre_of(ARM[arm]['go'])
    print(f"    {arm:>9}: " + "  ".join(f"{k} {TH[arm][k]:.6f}" for k in PARS)
          + f"   [{'manifest' if has else 'no manifest'}]")
SV = {}
for arm in ('namesake', 'aor'):
    SV[arm] = {k: switch_vals(ARM[arm]['go'], 'WBH2' if k == 'WB' else k) for k in ('WB', 'NS')}
    print(f"    {arm:>9}: the grid's own WBH2 {SV[arm]['WB']}   NS {SV[arm]['NS']}")
check("⒝ `Ⓑ②`'s LITERALS ARE THE NAMESAKE GRIDS' ONLY: the namesake records two values per lever "
      "and the arm of record three, because its base writes them explicitly.  ⇒ ** A re-point must "
      "restate the gate as what it means **",
      SV['namesake']['WB'] == ['0.0216', '0.0232'] and SV['namesake']['NS'] == ['0.945', '0.985']
      and len(SV['aor']['WB']) == 3 and len(SV['aor']['NS']) == 3,
      f"namesake {SV['namesake']['WB']} / {SV['namesake']['NS']}, arm of record "
      f"{SV['aor']['WB']} / {SV['aor']['NS']}")
for arm in ('namesake', 'aor'):
    for k, key in (('WB', 'WBH2'), ('NS', 'NS')):
        v = sorted(float(x) for x in SV[arm][k])
        lo, hi = v[0], v[-1]
        print(f"    {arm:>9} {key:5s}: {lo:.6f} .. {hi:.6f}, centre {TH[arm][k]:.6f}, "
              f"half-span {(hi - lo) / 2:.6f} against one step {STEP[k]:.6f}")
check("⛭ AND THE MEANING-FORM HOLDS ON BOTH ARMS: on each grid the extreme `WBH2` and `NS` values "
      "straddle that grid's OWN centre by exactly one step each.  ⇒ ** That is the gate the "
      "re-point should carry, and it is true of the namesake bank too, so nothing is weakened **",
      all(abs((max(float(x) for x in SV[a][k]) - min(float(x) for x in SV[a][k])) / 2 - STEP[k])
          < 1e-9
          and abs((max(float(x) for x in SV[a][k]) + min(float(x) for x in SV[a][k])) / 2
                  - TH[a][k]) < 1e-6
          for a in ('namesake', 'aor') for k in ('WB', 'NS')),
      "; ".join(f"{a} {k} half-span "
                f"{(max(float(x) for x in SV[a][k]) - min(float(x) for x in SV[a][k])) / 2:.6f}"
                for a in ('namesake', 'aor') for k in ('WB', 'NS')))

print()
print(BAR)
print("  PART 3 -- ⛔ `Ⓑ①`'s THIRD LIMB, AND THE ACCIDENT THAT KEEPS IT GREEN")
print(BAR)
_ASKDIR = os.path.join(BW, 'r7201_cc66_loading_lever')
_rb = []
for f in sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True)):
    try:
        z = np.load(f, allow_pickle=True)
    except Exception:
        continue
    if 'switches' in set(z.files) and 'RBFAC' in str(z['switches']):
        _rb.append(os.path.abspath(f))
_raw_outside = [f for f in _rb if not f.startswith(os.path.abspath(_ASKDIR))]
_sep_outside = [f for f in _rb if not f.startswith(os.path.abspath(_ASKDIR) + os.sep)]
print(f"    {len(_rb)} spectra in tree name `RBFAC` in their switches:")
for f in _rb:
    print(f"      {os.path.relpath(f, ROOT)}")
print(f"    the gate's RAW-PREFIX test leaves {len(_raw_outside)} outside the ask directory;")
print(f"    a SEPARATOR-AWARE test leaves {len(_sep_outside)}:")
for f in _sep_outside:
    print(f"      {os.path.relpath(f, ROOT)}")
check("⛔⛭⛭ `Ⓑ①`'s THIRD LIMB PASSES BY A PATH-PREFIX ACCIDENT: it requires every `RBFAC` spectrum "
      "in tree to sit under `r7201_cc66_loading_lever/` and tests it with a RAW string prefix.  "
      "70's second bank put three more in `r7201_cc66_loading_lever_leafrec1/`, whose name happens "
      "to begin with the old one.  ⇒ ** Separator-aware, three files fall outside and the limb "
      "would be RED -- so the gate is green for a reason unconnected to what it checks **",
      _raw_outside == [] and len(_sep_outside) == 3
      and all('_leafrec1' in f for f in _sep_outside),
      f"raw leaves {len(_raw_outside)} outside, separator-aware leaves {len(_sep_outside)}")
check("⌗ AND THE GATE'S INTENT IS INTACT, which is why this is a hardening and not a retraction: "
      "every one of the three is the SAME ask's runs re-run on the arm of record -- `cr_rb0.1`, "
      "`cr_rb0.5`, `cr_rb1.5` -- so no `RBFAC` spectrum anywhere in tree is outside this receipt's "
      "own granted ask",
      all(os.path.basename(f).startswith('cr_rb') for f in _sep_outside)
      and all(os.path.dirname(f).endswith('r7201_cc66_loading_lever_leafrec1')
              for f in _sep_outside),
      ", ".join(os.path.basename(f) for f in _sep_outside))
_nrb_grid = 0
for arm in ('namesake', 'aor'):
    for g in ('go', 'gl'):
        for f in sorted(glob.glob(os.path.join(ARM[arm][g], '*.npz'))):
            z = np.load(f, allow_pickle=True)
            if 'switches' in set(z.files) and 'RBFAC' in str(z['switches']):
                _nrb_grid += 1
check("and `Ⓑ①`'s LOAD-BEARING limb still holds on BOTH arms' grids: no nine-run grid records "
      "`RBFAC`, so no loading derivative was available from the grids on either arm",
      _nrb_grid == 0, f"{_nrb_grid} grid spectra name RBFAC")

print()
print(BAR)
print("  PART 4 -- THE DERIVATIVE TABLE, BOTH ARMS, BOTH GRIDS")
print(BAR)
print(f"    K_OBS, the sky's own drift, scored against both arms alike: {K_OBS:+.4e}")
# ⛔⛭ ** AND K_OBS IS PINNED, BECAUSE PERTURBING IT PROVED THE REST OF THIS FILE CANNOT SEE IT. **
#   Replacing the lift above with a plausible constant `-9.0e-04` -- 3 per cent away -- left EVERY
#   gate in this file green.  *That is a property of the statistic and not a flaw: the spread is
#   exactly K_OBS-independent, since `need = (K_OBS - kb)/dk` shares its numerator across the four
#   directions, so the ratio is the ratio of derivatives alone; and the move RANGE shifts by only
#   the same 3 per cent.*  ⇒ ** So a wrong lift would have been invisible, and the only thing that
#   can catch it is a direct pin against the receipt's own printed value. **
check("⛔⛭ K_OBS IS THE RECEIPT'S OWN PUBLISHED VALUE, pinned directly -- because perturbation "
      "showed that replacing it with a plausible constant 3 per cent away leaves every other gate "
      "in this file green.  ⇒ ** The spread is exactly K_OBS-independent by construction and the "
      "move range nearly so, so nothing downstream can detect a wrong lift: this pin is the only "
      "thing that can **",
      abs(K_OBS + 9.2995e-04) < 5e-8,
      f"{K_OBS:+.6e} against the receipt's -9.2995e-04")
RES = {}
print(f"    {'arm':>9} {'grid':9s} {'par':3s} {'dk/dln(th)':>12s} {'move for k_obs':>15s}")
for arm in ('namesake', 'aor'):
    for gname, g in (('oneclock', 'go'), ('licensed', 'gl')):
        kb = slope_of(os.path.join(ARM[arm][g], 'cr_base.npz'))[0]
        RES[(arm, gname, 'base')] = kb
        for par in PARS:
            km = slope_of(os.path.join(ARM[arm][g], f'cr_{par}m.npz'))[0]
            kp = slope_of(os.path.join(ARM[arm][g], f'cr_{par}p.npz'))[0]
            dk = (kp - km) / (2 * STEP[par]) * TH[arm][par]
            RES[(arm, gname, par)] = (dk, (K_OBS - kb) / dk if dk else np.inf)
            print(f"    {arm:>9} {gname:9s} {par:3s} {dk:+12.4e} "
                  f"{RES[(arm, gname, par)][1] * 100:+14.1f} %")
NEED = {a: {p: abs(RES[(a, 'oneclock', p)][1]) for p in PARS} for a in ('namesake', 'aor')}
SPREAD = {a: max(NEED[a].values()) / min(NEED[a].values()) for a in ('namesake', 'aor')}
for a in ('namesake', 'aor'):
    print(f"    {a:>9}: moves needed " + ", ".join(f"{p} {NEED[a][p] * 100:.1f}%" for p in PARS)
          + f"   spread {SPREAD[a]:.2f}x")
CONV = {a: max(abs(RES[(a, 'licensed', p)][1]) / abs(RES[(a, 'oneclock', p)][1]) for p in PARS)
        for a in ('namesake', 'aor')}
for a in ('namesake', 'aor'):
    print(f"    {a:>9}: worst licensed/oneclock disagreement in the move needed {CONV[a]:.2f}x")

# ⛔⛭⛭ ** Ⓒ① DOES NOT SURVIVE AS REGISTERED, AND THE PART THAT FAILS IS IN THE RECEIPT'S TITLE. **
#   As registered it asserted two things: every banked direction needs a 4-6 per cent move, and the
#   most responsive beats the least by under a factor of two.  On the arm of record the moves run
#   4.2 to 10.2 per cent and the spread is 2.44x.  ⇒ *The CONCLUSION is untouched -- a factor of two
#   and a half is still not identifying a carrier, and the two independent reasons stand (no loading
#   lever in either grid, and a response that is convention-dependent).  What weakens is the
#   DECISIVE TELL the title names: on the namesake arm `n_s` needed 5.2 per cent against omega_b's
#   4.1 -- "a primordial tilt moves it AS MUCH AS the baryon density" -- while here `n_s` needs 10.2
#   against 4.2, so omega_b is two and a half times the more responsive.*
#   ** Reported as the arm's measurement, not restated as though the namesake's margin held. **
check("⛔⛭⛭ Ⓒ①'s CONCLUSION SURVIVES AND ITS TELL WEAKENS: the slope still identifies no carrier on "
      "the arm of record -- but the moves run 4.2 to 10.2 per cent against the registered 4-6, the "
      "spread is 2.44x against the registered under-two, and `n_s` is no longer as responsive as "
      "`omega_b` (10.2 against 4.2, a factor of 2.4, where the namesake's was 1.27).  ⇒ ** So the "
      "title's 'a primordial tilt moves it as much as the baryon density' is the NAMESAKE arm's "
      "margin.  The negative result rests on the other two reasons here **",
      SPREAD['aor'] > 2.0 and SPREAD['namesake'] < 2.0
      and NEED['aor']['NS'] / NEED['aor']['WB'] > 2.0
      and NEED['namesake']['NS'] / NEED['namesake']['WB'] < 1.5
      and max(NEED['aor'].values()) < 0.15,
      f"arm of record spread {SPREAD['aor']:.2f}x and n_s:omega_b "
      f"{NEED['aor']['NS'] / NEED['aor']['WB']:.2f}x, against the namesake's "
      f"{SPREAD['namesake']:.2f}x and {NEED['namesake']['NS'] / NEED['namesake']['WB']:.2f}x")

#: ⛭⛭ ** AND Ⓒ③ SURVIVES WHILE ITS HEADLINE NUMBER TURNS OUT TO HAVE BEEN A NEAR-ZERO ARTEFACT. **
#: The namesake arm's `47x` convention disagreement is a RATIO OF MOVES, and a move is `(k_obs - k)/
#: (dk/dln theta)` -- so a derivative near zero sends the move to infinity and the ratio with it.
#: On the namesake's licensed grid `Omega_m`'s derivative is `+2.56e-04`, two orders below the
#: one-clock grid's, which is where the `-293.6%` move and hence the `47x` come from.  *On the arm of
#: record that near-zero is absent and the disagreement is a clean `3.18x`.*  ⇒ ** The conclusion is
#: better supported on the arm of record than on the namesake, which is the opposite of a loss. **
_den_nsk = min(abs(RES[('namesake', 'licensed', p)][0]) for p in PARS)
_den_aor = min(abs(RES[('aor', 'licensed', p)][0]) for p in PARS)
print(f"    smallest |dk/dln| on the licensed grid: namesake {_den_nsk:.3e}, "
      f"arm of record {_den_aor:.3e}  -- a factor of {_den_aor / _den_nsk:.1f}")
check("⛭⛭ Ⓒ③ SURVIVES AND ITS NUMBER IMPROVES: the arm's response is still not robust to its "
      "geometry convention, at 3.18x on the arm of record.  ⛔ *And the namesake's 47x was a "
      "NEAR-ZERO ARTEFACT: its licensed-grid `Omega_m` derivative is 2.56e-04, twenty times smaller "
      "than the arm of record's, and a near-zero denominator sends its 'move needed' to -293.6 per "
      "cent and the ratio with it.*  ⇒ ** So the conclusion is better supported here than where it "
      "was made **",
      CONV['aor'] > 2.5 and CONV['namesake'] > 10 * CONV['aor'] and _den_aor > 10 * _den_nsk,
      f"{CONV['aor']:.2f}x against the namesake's {CONV['namesake']:.2f}x; smallest licensed "
      f"derivative {_den_aor:.2e} against {_den_nsk:.2e}")

print()
print(BAR)
print("  PART 5 -- THE CARRY, AND THE DRIVING LEVER ON BOTH ARMS")
print(BAR)
for arm in ('namesake', 'aor'):
    k, p, _a = slope_of(ARM[arm]['nd'])
    print(f"    driving OFF, {arm:>9}: P = {p:.2f}, slope = {k:+.4e}")
    RES[(arm, 'nodrive')] = k
_kc, _pc, _ = slope_of(CTL['nd'])
print(f"    driving OFF, {'control':>9}: P = {_pc:.2f}, slope = {_kc:+.4e}")
check("Ⓑ③ the driving lever is still banked on both arms and reads finite on each",
      all(np.isfinite(RES[(a, 'nodrive')]) for a in ('namesake', 'aor')) and np.isfinite(_kc),
      f"namesake {RES[('namesake', 'nodrive')]:+.3e}, arm of record "
      f"{RES[('aor', 'nodrive')]:+.3e}")
#: ** THE CARRY: the slope is `2*pi*(1/P - 1/l_A)` with P the best period of the arm's OWN whitened
#: residual and l_A the arm's OWN comb scale.  No control quantity enters, and the gated numbers are
#: RATIOS of derivatives, so even a rigid rescaling of the arm's comb cancels.  Class 3 by
#: construction; measured below by recomputing one derivative from the two files alone. **
_dk_solo = (slope_of(os.path.join(ARM['aor']['go'], 'cr_WBp.npz'))[0]
            - slope_of(os.path.join(ARM['aor']['go'], 'cr_WBm.npz'))[0]) \
    / (2 * STEP['WB']) * TH['aor']['WB']
check("⛭ THE CARRY HAS NOTHING TO ACT ON: the slope is 2*pi*(1/P - 1/l_A) with P the best period of "
      "the ARM's own whitened residual and l_A the ARM's own comb scale, so recomputing a "
      "derivative from its two files alone reproduces the pipeline's bit-for-bit.  ** Class 3, and "
      "the gated quantities are ratios of derivatives besides **",
      _dk_solo == RES[('aor', 'oneclock', 'WB')][0],
      f"solo {_dk_solo:+.6e} against pipeline {RES[('aor', 'oneclock', 'WB')][0]:+.6e}")

print()
print(BAR)
print("  PART 6 -- WHAT MOVES, OLD -> NEW")
print(BAR)
ROWS = [('move needed, H0', NEED['namesake']['H0'] * 100, NEED['aor']['H0'] * 100, '.1f'),
        ('move needed, Omega_m', NEED['namesake']['OM'] * 100, NEED['aor']['OM'] * 100, '.1f'),
        ('move needed, n_s', NEED['namesake']['NS'] * 100, NEED['aor']['NS'] * 100, '.1f'),
        ('move needed, omega_b', NEED['namesake']['WB'] * 100, NEED['aor']['WB'] * 100, '.1f'),
        ('spread, most vs least', SPREAD['namesake'], SPREAD['aor'], '.2f'),
        ('convention disagreement', CONV['namesake'], CONV['aor'], '.2f'),
        ('base slope, oneclock', RES[('namesake', 'oneclock', 'base')],
         RES[('aor', 'oneclock', 'base')], '+.4e'),
        ('base slope, licensed', RES[('namesake', 'licensed', 'base')],
         RES[('aor', 'licensed', 'base')], '+.4e'),
        ('driving-off slope', RES[('namesake', 'nodrive')], RES[('aor', 'nodrive')], '+.4e')]
print(f"    {'figure':>26} {'namesake':>13} {'arm of record':>14}   verdict")
for lab, o, n, f in ROWS:
    v = 'unchanged' if abs(n - o) < 1e-12 else (
        'MOVED' if abs(n - o) > 0.005 * max(1e-12, abs(o)) else 'moved (trace)')
    print(f"    {lab:>26} {format(o, f):>13} {format(n, f):>14}   {v}")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
