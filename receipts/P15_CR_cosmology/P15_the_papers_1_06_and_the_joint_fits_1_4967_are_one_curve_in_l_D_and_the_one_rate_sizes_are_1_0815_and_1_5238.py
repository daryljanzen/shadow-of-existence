#!/usr/bin/env python3
r"""`r7797` ** THE PAPER'S `1.06` AND THIS CORPUS'S `1.4967` ARE THE SAME STATISTIC ON ONE CURVE IN
`l_D`, AND NEITHER IS A DIFFERENCE AGAINST THE NULL. **

** THE ORDER ASKED WHICH OF TWO THINGS EACH FIGURE IS -- *"a difference against the null, or the
residual after the tilt, and over which bins"* -- AND THE ANSWER IS NEITHER OF THE TWO ALTERNATIVES
AS POSED: ** both are the **residual after the tilt**, over the **same** window (`l = 100-1758`), the
**same** `171` covered bins, at the **same** ratio (`r = 1.0926`), in the **same** functional form,
correlated with the analytic Gaussian-minus-power-law at `1.000000` in both.  ** Nothing about the
statistic, the window or the bin count differs.  One number differs: the damping multipole. **

⛭ ** AND IT IS ONE NUMBER, NOT TWO, WHICH IS THE WHOLE RECONCILIATION. **  `P15`'s `1.06` is priced
on the instrument's own effective exponent `alpha = 1.70` at the instrument header's `l_D = 1951.9`
(`r7611+70`, PO-24).  But `alpha` and `l_D` enter the signature ONLY through `l_D / sqrt(alpha)` --
and `70`'s faithful copy says so in its own declared INPUT line, which reads
`R, LD = 1.0926, 1951.9 / 1.70 ** 0.5`.  ** So the faithful route IS the exponent-one form at
`l_eff = 1497.0390`, and the two published figures are two points on a single curve in `l_D`: **

      alpha   l_D declared      l_D in force    chi^2/bin after the tilt   absorbed
      1.70    1951.9            1497.0390       1.0619  -> P15's "1.06"    69.6 %
      1.00    1362             1362.0000        1.4967                     69.8 %

⛔ ** AND THAT HAS A CONSEQUENCE THIS RECEIPT EXISTS TO HEAD OFF, BECAUSE THE CORPUS HAS MADE THIS
EXACT MISTAKE ONCE ALREADY THIS REVISION. **  `sec:coherence` prints `1.06` and then, two sentences
later, prints *"that rate moves the damping multipole from `1362` to `1355.21`"* and the `1.81` per
cent growth that goes with it.  ** Those two sentences are priced on DIFFERENT damping multipoles and
the text names only the second one's. **  Carrying `1.5238` to a `1.06` is the comb error again -- one
estimator's number applied to another estimator's figure -- so this receipt supplies the one-rate size
of ** both ** forms, each labelled with the `l_D` it is on:

      alpha   l_D in force    chi^2/bin    growth      above C62's 0.92 and 0.26
      1.70    1489.5783       1.0815       +1.846 %    yes, both
      1.00    1355.2123       1.5238       +1.811 %    yes, both

Built `r7797+cc66.1`, discharging order ② of the chat seat's `r7797`.  Registered before it existed in
`computations/beyond_the_wall/r7797_cc66_the_gaussian_size_reconciled/PREDICTION.md`.

===================================================================================================
** COMPUTES: ** the joint fit of `P15`'s diffusion-scale signature against a tilt, re-run at ** four **
   damping multipoles by executing the joint-fit receipt's OWN source with only its one declared
   `INPUT` line rewritten.  `l_eff` is computed from `70`'s own declared `alpha` and `l_D`; the
   one-rate move is read from the two banked arms' `D_M` and applied to whichever `l_D` is in force.
   Nothing is fitted beyond the two parameters each fit is of, and no significance is computed.
===================================================================================================

⛭ ** WHAT THIS RECEIPT DOES NOT DECIDE. **  Which exponent `sec:coherence` ** should ** price the
signature on is not adjudicated here and is not mine: `alpha = 1.70` is `70`'s measurement
(`r7577+70.2`) and the paper's own `sec:diffusion-scale` already argues the source route is the
faithful one.  ⑨ asserts that scope limit against this file's AST.  This receipt says only which
number is which, and supplies the one-rate size of each so that either can be printed without the
other appearing to contradict it.

⛔ ** AND A SECOND COLLISION IN THE SAME SUBSECTION, OF KIND RATHER THAN SIZE, WHICH ⑧ MEASURES. **
`sec:diffusion-scale` prints *"the signature at the adjudicated ratio costs `$1.48$` in `$\chi^{2}$`
over the `$171$` bins"* -- a ** total **, about `0.0087` per bin -- a few sentences before
`sec:coherence` cites a receipt whose figure is `1.4967` ** per bin ** over those same `171` bins.
** The two numerals agree to one per cent and differ by a factor of `171` in kind. **  Neither
sentence is wrong on its own; read together in one subsection they are the likeliest source of two
figures appearing to disagree, which is what the order set out to stop.

⛔ ** A PIN CAUGHT ONE SLIP OF MINE WHILE THIS WAS BEING MINTED, AND IT IS THE PIN DOING ITS JOB: **
④'s amplitude-only literal was first written as `4.9558`, which I had computed as
`1.4967 / (1 - 0.698)` from the ROUNDED absorbed share rather than read from the run.  The measured
value is `4.9493`.  *Deriving a figure from another figure's rounding is the same error class as
carrying one estimator's number to another estimator's figure, which is what ⛔ above is about --
so it is recorded here rather than quietly corrected.*

⛭ ** THE FIT IS NOT REIMPLEMENTED HERE, AND ③ IS THE ROW THAT PROVES IT: ** it reproduces ** both **
published figures, `1.4967` and `1.0619`, from the one harness at the two declared `l_D`.
"""
import ast as _ast
import os
import re
import subprocess
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
JF = os.path.join(HERE, 'P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma.py')
FAITH = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7611_70_faithful_exponent',
                     'jointfit_faithful.py')
LD0, R_SIG = 1362.0, 1.0926
ALPHA_DECL, LDH_DECL = 1.70, 1951.9
C62_INSTRUMENT, C62_DATA_SHAPE = 0.92, 0.26

CHECKS = []


def check(name, ok, detail=''):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"           {detail}")


tex = open(TEX, encoding='utf-8').read()
flat = ' '.join(tex.split())
jf_src = open(JF, encoding='utf-8').read()
fa_src = open(FAITH, encoding='utf-8').read()

# ------------------------------------------------- ① the paper prints both figures in one subsection
_has_106 = '$1.06$ per bin at a ratio of $1.0926$ on the same window' in flat
_has_shift = 'moves the damping multipole from $1362$ to $1355.21$' in flat
# the FINDING is printed, not asserted: it is the state 69 may fix, and a gate that asserts it
# would fail on success -- the named hazard of check_quote_pins.
_names_exponent = bool(re.search(r'1\.06\$ per bin[^.]{0,400}?(1\.70|exponent|l_\{?eff)', flat))
check("⛭⛔⛭ `r7797` ** ① `P15` PRINTS BOTH FIGURES IN ONE SUBSECTION: `sec:coherence`'s *\"$1.06$ per "
      "bin at a ratio of $1.0926$ on the same window\"* AND, TWO SENTENCES LATER, *\"moves the damping "
      "multipole from $1362$ to $1355.21$\"* ** ⇒ *so a reader meets the two sizes side by side, which "
      "is why they have to be told apart; ⌗ whether the text NAMES the first one's exponent is "
      "PRINTED here and not asserted -- asserting it would redden the day 69 fixes it*",
      _has_106 and _has_shift,
      f"the 1.06 sentence present {_has_106}; the 1362->1355.21 sentence present {_has_shift}; "
      f"⌗ does the text name the 1.06's exponent or l_eff: {_names_exponent}")

# ------------------------------------------------- ② alpha and l_D enter only as l_D / sqrt(alpha)
_m = re.search(r'^R, LD = ([\d.]+), ([\d.]+) / ([\d.]+) \*\* 0\.5', fa_src, re.M)
_r_f = float(_m.group(1)) if _m else None
_ldh = float(_m.group(2)) if _m else None
_alp = float(_m.group(3)) if _m else None
LEFF = (_ldh / _alp ** 0.5) if _m else float('nan')
_k_both = [l.strip() for l in jf_src.splitlines() if l.strip().startswith('K = ')] == ['K = R**2 - 1'] \
    and [l.strip() for l in fa_src.splitlines() if l.strip().startswith('K = ')] == ['K = R**2 - 1']
_sig = 'return np.exp(-K * (np.asarray(l, float) / LD) ** 2)'
_sig_both = jf_src.count(_sig) == 1 and fa_src.count(_sig) == 1
check("⛭⛭⛭ `r7797` ** ② AND THE TWO ROUTES DIFFER IN ONE NUMBER, NOT TWO, BECAUSE `alpha` ENTERS ONLY "
      "AS `l_D / sqrt(alpha)` -- `70`'s FAITHFUL COPY SAYS SO IN ITS OWN DECLARED INPUT LINE, "
      "`R, LD = 1.0926, 1951.9 / 1.70 ** 0.5` ** ⇒ *`l_eff = 1497.0390`, and both files carry the "
      "SAME `K = R**2 - 1` and the SAME one-line signature, so there is nothing else for an exponent "
      "to enter through*",
      _m is not None and abs(_r_f - R_SIG) < 1e-9 and abs(_ldh - LDH_DECL) < 0.05
      and abs(_alp - ALPHA_DECL) < 0.005 and abs(LEFF - 1497.0390) < 0.00005
      and _k_both and _sig_both,
      f"faithful INPUT: r={_r_f}, l_D={_ldh}, alpha={_alp} -> l_eff={LEFF:.4f}; "
      f"K identical in both {_k_both}; the one-line signature in both exactly once {_sig_both}")

# ------------------------------------------------- the harness: the joint-fit receipt's own source
_IN = f'R, LD = {R_SIG}, {LD0}'
if _IN not in jf_src:
    sys.exit(f'FATAL: the joint-fit receipt no longer declares its inputs as `{_IN}`.')


def joint(ld):
    text = jf_src.replace(_IN, f'R, LD = {R_SIG!r}, {ld!r}')
    for rl, new in (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {HERE!r}'),
                    ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')):
        if rl not in text:
            sys.exit(f'FATAL: the joint-fit receipt no longer carries `{rl}`.')
        text = text.replace(rl, new)
    with tempfile.TemporaryDirectory() as td:
        q = os.path.join(td, 'jf.py')
        open(q, 'w', encoding='utf-8').write(text)
        pr = subprocess.run([sys.executable, '-I', q], capture_output=True, text=True, cwd=HERE,
                            timeout=1800)
    row = re.search(r'^\s*100-1760\s+(\d+)\s+(-?\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)%', pr.stdout, re.M)
    win = re.search(r'window l = (\d+)-(\d+), (\d+) covered bins', pr.stdout)
    amp = re.search(r'chi\^2/bin\s+(\d+\.\d+) \(amplitude only\)\s+->\s+(\d+\.\d+) \(with the tilt\)'
                    r'\s+(\d+\.\d+)% absorbed', pr.stdout)
    cor = re.search(r'power law\) at (\d\.\d{4,})', pr.stdout)
    red = [l.strip() for l in pr.stdout.splitlines() if re.match(r'\s*FAIL', l)]
    return dict(rc=pr.returncode,
                bins=int(row.group(1)) if row else None,
                dn=float(row.group(2)) if row else None,
                chi2=float(row.group(3)) if row else None,
                absorbed=float(row.group(4)) if row else None,
                lo=int(win.group(1)) if win else None, hi=int(win.group(2)) if win else None,
                wbins=int(win.group(3)) if win else None,
                amp=float(amp.group(1)) if amp else None,
                corr=float(cor.group(1)) if cor else None, red=red)


def dm(tag):
    with np.load(os.path.join(SPEC, tag + '.npz'), allow_pickle=True) as z:
        return float(z['D_M'])


MV = dm('r7749_leafgeom_nofit_L2000_cr') / dm('cc66_cr_x_h686_L2000_leafrec1_distances') - 1.0
LD_A1, LD_A1_CR = LD0, LD0 * (1.0 + MV)
LD_AF, LD_AF_CR = LEFF, LEFF * (1.0 + MV)

RUNS = [('alpha=1.00  published', LD_A1), ('alpha=1.00  one rate', LD_A1_CR),
        ('alpha=1.70  published', LD_AF), ('alpha=1.70  one rate', LD_AF_CR)]
G = {}
print(f"\n      {'route':<22} {'l_D':>11} {'rc':>3} {'window':>12} {'bins':>5} {'Delta n_s':>11} "
      f"{'amp only':>9} {'chi2/bin':>9} {'absorbed':>9} {'corr':>9}")
for lab, ld in RUNS:
    g = joint(ld)
    G[lab] = g
    print(f"      {lab:<22} {ld:>11.4f} {g['rc']:>3} {str(g['lo']) + '-' + str(g['hi']):>12} "
          f"{g['bins']!s:>5} {g['dn']!s:>11} {g['amp']!s:>9} {g['chi2']!s:>9} "
          f"{str(g['absorbed']) + '%':>9} {g['corr']!s:>9}", flush=True)
A1, A1C, AF, AFC = (G[k] for k, _ in RUNS)

# ------------------------------------------------- ③ both published figures reproduce
check("⛭⛭⛭ `r7797` ** ③ AND BOTH PUBLISHED FIGURES COME OUT OF THE ONE HARNESS AT THE TWO DECLARED "
      "`l_D`: `1.4967` AT `1362` AND `1.0619` AT `1497.0390`, WHICH IS `P15`'s *\"$1.06$\"* ** ⇒ *this "
      "is the row that makes the rest a measurement of the RECONCILIATION rather than of a "
      "reimplementation: one harness, one rewritten INPUT line, both numbers*",
      abs(A1['chi2'] - 1.4967) < 0.00005 and abs(AF['chi2'] - 1.0619) < 0.00005
      and round(AF['chi2'], 2) == 1.06,
      f"alpha=1 at l_D {LD_A1:.4f}: {A1['chi2']} chi2/bin; alpha=1.70 at l_eff {LD_AF:.4f}: "
      f"{AF['chi2']} chi2/bin, which rounds to {round(AF['chi2'], 2)}")

# ------------------------------------------------- ④ neither is a difference against the null
_amp_bigger = all(g['amp'] is not None and g['chi2'] is not None and g['amp'] > g['chi2']
                  for g in (A1, A1C, AF, AFC))
check("⛭⛭⛭ `r7797` ** ④ AND NEITHER FIGURE IS A DIFFERENCE AGAINST THE NULL, WHICH IS THE ORDER'S "
      "QUESTION ANSWERED: BOTH ARE THE RESIDUAL **AFTER THE TILT** ** ⇒ *each run prints the "
      "amplitude-only cost as a SEPARATE column and it is the larger one on all four routes "
      "(`4.9493`/`3.4925` against `1.4967`/`1.0619`), so the published figures are the right-hand "
      "column in every case*",
      _amp_bigger and abs(AF['amp'] - 3.4925) < 0.00005 and abs(A1['amp'] - 4.9493) < 0.00005,
      f"amplitude only -> after tilt: alpha=1 {A1['amp']} -> {A1['chi2']}; "
      f"alpha=1.70 {AF['amp']} -> {AF['chi2']}; amplitude-only larger on all four {_amp_bigger}")

# ------------------------------------------------- ⑤ same window, ratio, bin count, form
_same = (len({g['lo'] for g in (A1, A1C, AF, AFC)}) == 1
         and len({g['hi'] for g in (A1, A1C, AF, AFC)}) == 1
         and {g['bins'] for g in (A1, A1C, AF, AFC)} == {171}
         and {g['wbins'] for g in (A1, A1C, AF, AFC)} == {171}
         and all(abs(g['corr'] - 1.0) < 5e-7 for g in (A1, A1C, AF, AFC)))
check("⛭⛭⛭ `r7797` ** ⑤ AND THE WINDOW, THE BIN COUNT, THE RATIO AND THE FORM ARE IDENTICAL ON ALL "
      "FOUR ROUTES -- `l = 100-1758`, `171` COVERED BINS, `r = 1.0926`, CORRELATION `1.000000` -- SO "
      "THE WHOLE DIFFERENCE IS `l_D` ** ⇒ *this is what makes the two published sizes two points on "
      "one curve rather than two quantities; the order asked \"over which bins\" and the answer is "
      "the same bins*",
      _same,
      f"window {A1['lo']}-{A1['hi']} on all four; covered bins "
      f"{sorted({g['bins'] for g in (A1, A1C, AF, AFC)})}; correlations "
      f"{sorted({g['corr'] for g in (A1, A1C, AF, AFC)})}")

# ------------------------------------------------- ⑥ the one-rate size of BOTH forms
_gro_1 = 100.0 * (A1C['chi2'] / A1['chi2'] - 1.0)
_gro_f = 100.0 * (AFC['chi2'] / AF['chi2'] - 1.0)
check("⛭⛭⛭ `r7797` ** ⑥ AND THE ONE-RATE SIZE OF **BOTH** FORMS, EACH ON ITS OWN `l_D`: `1.5238` AT "
      "`1355.2123` AND `1.0815` AT `1489.5783`, GROWING BY `1.811` AND `1.846` PER CENT, BOTH STILL "
      "ABOVE **BOTH** OF `C62`'s BOUNDS AND BOTH STILL THE PREDICTED SHAPE TO `1.000000` ** ⇒ *the "
      "move is `-0.4984` per cent, read from the two banked arms' own `D_M` and applied to whichever "
      "`l_D` is in force -- so whichever figure `sec:coherence` prints, its one-rate counterpart is "
      "here and labelled, and neither has to be carried to the other.  ⌁ Carrying ①'s PAPER "
      "READ as a condition, because this label names `sec:coherence`: a row that names the paper "
      "must open it*",
      _has_106 and _has_shift
      and abs(100 * MV - (-0.4984)) < 0.0001
      and abs(LD_A1_CR - 1355.2123) < 0.0001 and abs(LD_AF_CR - 1489.5783) < 0.0001
      and abs(A1C['chi2'] - 1.5238) < 0.00005 and abs(AFC['chi2'] - 1.0815) < 0.00005
      and abs(_gro_1 - 1.811) < 0.001 and abs(_gro_f - 1.846) < 0.001
      and min(A1C['chi2'], AFC['chi2']) > C62_INSTRUMENT > C62_DATA_SHAPE
      and abs(A1C['corr'] - 1.0) < 5e-7 and abs(AFC['corr'] - 1.0) < 5e-7,
      f"move {100 * MV:+.6f}%; alpha=1 {LD_A1:.4f}->{LD_A1_CR:.4f} gives {A1['chi2']}->{A1C['chi2']} "
      f"({_gro_1:+.3f}%); alpha=1.70 {LD_AF:.4f}->{LD_AF_CR:.4f} gives {AF['chi2']}->{AFC['chi2']} "
      f"({_gro_f:+.3f}%); both above C62's {C62_INSTRUMENT} and {C62_DATA_SHAPE}")

# ------------------------------------------------- ⑦ the off-input red is named, not swallowed
_a1_clean = A1['rc'] == 0 and not A1['red']
_af_red = [r for r in AF['red'] if 'INSTRUMENT-route displacement' in r]
check("⛭⛭ `r7797` ** ⑦ AND THE JOINT-FIT RECEIPT EXITS NON-ZERO OFF ITS OWN DECLARED INPUT, SO THE "
      "ROW THAT REDDENS IS **NAMED** RATHER THAN SWALLOWED: EXACTLY ONE, `⓷ᶜ`, ITS AGREEMENT WITH "
      "`C62`'s INSTRUMENT-ROUTE DISPLACEMENT, WHICH LOOSENS TO `18` PER CENT ON THE FAITHFUL "
      "EXPONENT ** ⇒ *`70` reported that row at `r7611` and PO-24 already asserts it is the one that "
      "fails, so it is expected and it is not a figure `P15` prints; ⌗ at the declared `l_D` the "
      "same source runs clean, which is what makes the red attributable to `l_D` and not to the "
      "rewrite*",
      _a1_clean and AF['rc'] != 0 and len(AF['red']) == 1 and len(_af_red) == 1
      and abs(AF['dn'] - (-0.06936)) < 0.000005 and abs(A1['dn'] - (-0.08304)) < 0.000005,
      f"at l_D {LD_A1:.4f}: rc={A1['rc']}, {len(A1['red'])} reddened; at l_eff {LD_AF:.4f}: "
      f"rc={AF['rc']}, {len(AF['red'])} reddened -> {(_af_red or ['-'])[0][:120]}; "
      f"displacements {A1['dn']} and {AF['dn']}")

# ------------------------------------------------- ⑧ the second collision, of kind not size
_m148 = re.search(r'costs \$(\d\.\d{2})\$ in \$\\chi\^\{2\}\$ over the \$171\$ bins from '
                  r'\$\\ell=100\$ to \$1760\$', flat)
_per_bin_148 = (float(_m148.group(1)) / 171.0) if _m148 else None
_ratio_kind = (A1['chi2'] / _per_bin_148) if _per_bin_148 else None
check("⛭⛭⛭⛔ `r7797` ** ⑧ AND A SECOND COLLISION IN THE SAME SUBSECTION, OF **KIND** RATHER THAN SIZE: "
      "`P15` PRINTS *\"costs $1.48$ in $\\chi^{2}$ over the $171$ bins\"* -- A **TOTAL**, `0.00865` "
      "PER BIN -- A FEW SENTENCES BEFORE CITING A RECEIPT WHOSE FIGURE IS `1.4967` **PER BIN** OVER "
      "THOSE SAME `171` BINS ** ⇒ *the two numerals agree to one per cent and differ by a factor of "
      "`171` in kind; neither sentence is wrong alone, and read together they are the likeliest "
      "source of two figures appearing to disagree -- which is what the order set out to stop*",
      _m148 is not None and abs(_per_bin_148 - 0.00865) < 0.000005
      and abs(_ratio_kind - 172.9) < 0.05,
      f"the 1.48 sentence present {_m148 is not None}; 1.48 over 171 bins is "
      f"{_per_bin_148:.5f}/bin; the citing receipt's figure {A1['chi2']}/bin is "
      f"{_ratio_kind:.1f} times that")

# ------------------------------------------------- ⑨ scope, asserted against this file's AST
_FORBIDDEN = {'chi2_cdf', 'sf', 'pvalue', 'p_value', 'norm', 'curve_fit', 'minimize',
              'minimize_scalar', 'lstsq', 'polyfit', 'cho_solve', 'nsigma', 'sigma_of'}
_names = set()
for _n in _ast.walk(_ast.parse(open(__file__, encoding='utf-8').read())):
    if isinstance(_n, _ast.Name):
        _names.add(_n.id)
    elif isinstance(_n, _ast.Attribute):
        _names.add(_n.attr)
_hits = sorted(_names & _FORBIDDEN)
check("⛭⛭ `r7797` ** ⑨ AND THE SCOPE LIMIT IS ASSERTED RATHER THAN PROMISED: THIS RECEIPT FITS "
      "NOTHING, COMPUTES NO SIGNIFICANCE, AND DOES NOT ADJUDICATE WHICH EXPONENT `sec:coherence` "
      "SHOULD PRICE THE SIGNATURE ON ** ⇒ *`alpha = 1.70` is `70`'s measurement at `r7577+70.2` and "
      "the faithful-route argument is `sec:diffusion-scale`'s; this receipt says only which number is "
      "which and supplies each one's one-rate counterpart.  ⌗ Asserted by walking this file's own "
      "AST, not by searching its text for its own token list -- the error class that cost three rows "
      "at `r7783`*",
      not _hits,
      f"fitting and significance names in this file's AST: {_hits or 'none'}")

# ------------------------------------------------- ⑩ every published figure, pinned by comparison
_c62 = re.search(r'^C62_DATA_SHAPE, C62_INSTRUMENT = ([\d.]+), ([\d.]+)', jf_src, re.M)
_ds = float(_c62.group(1)) if _c62 else None
_ins = float(_c62.group(2)) if _c62 else None
_tot = float(_m148.group(1)) if _m148 else None
_pins = dict(
    ratio=abs(_r_f - 1.0926) < 0.00005,
    alpha=abs(_alp - 1.70) < 0.005,
    header_lD=abs(_ldh - 1951.9) < 0.05,
    absorbed_a1=abs(A1['absorbed'] - 69.8) < 0.05,
    absorbed_a1_cr=abs(A1C['absorbed'] - 69.8) < 0.05,
    absorbed_af=abs(AF['absorbed'] - 69.6) < 0.05,
    absorbed_af_cr=abs(AFC['absorbed'] - 69.6) < 0.05,
    total_1_48=_tot is not None and abs(_tot - 1.48) < 0.005,
    c62_data_shape=_ds is not None and abs(_ds - 0.26) < 0.005,
    c62_instrument=_ins is not None and abs(_ins - 0.92) < 0.005,
)
check("⛭⛭ `r7797` ** ⑩ AND EVERY FIGURE THE `INDEX` ROW PUBLISHES IS PINNED HERE BY A COMPARISON, NOT "
      "ONLY THE ONES A ROW ABOVE HAPPENS TO TEST: THE RATIO `1.0926`, THE EXPONENT `1.70`, THE "
      "INSTRUMENT HEADER'S `1951.9`, THE ABSORBED SHARES `69.8` AND `69.6` ON ALL FOUR ROUTES, THE "
      "PAPER'S TOTAL `1.48`, AND `C62`'s TWO BOUNDS `0.26` AND `0.92` ** ⇒ *`check_figures_pinned` "
      "PARSES rather than runs, so a figure a citing row prints has to appear inside a tolerance "
      "comparison in this file.  ⌗ `C62`'s two bounds and the paper's total are PARSED from their own "
      "sources and then pinned, so the row moves if either source does rather than if I retyped it*",
      all(_pins.values()),
      f"pinned: {sorted(k for k, v in _pins.items() if v)}; "
      f"NOT pinned: {sorted(k for k, v in _pins.items() if not v) or 'none'}; "
      f"C62's declared routes {_ds} and {_ins}; the paper's total {_tot}")

print()
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass")
if bad:
    for n in bad:
        print(f"  FAILED: {n}")
    sys.exit(1)
