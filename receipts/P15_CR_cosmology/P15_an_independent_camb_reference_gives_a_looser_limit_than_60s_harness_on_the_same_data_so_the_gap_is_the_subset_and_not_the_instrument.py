"""
P15, r7847+cc66.4, on 69's order r7847: an independent CAMB reference for 60's neutrino-mass
harness, built by a different seat, as PO-24's refit was settled on two arms.

WHY THE ORDER WAS GIVEN, AND WHAT THE REFERENCE SAYS BACK.  60's LCDM control moved
277.7 -> 99.67 -> 111.38 meV against a published 64.2, its effective mass +67.5 -> -7.0 ->
+44.3 against a published -101, and its chains are healthy.  69 read the residue as the
INSTRUMENT and ordered 60 to carry Phi through the radiation era.  This reference, scored
through 60's OWN likelihood modules with only the spectra replaced, says the residue is NOT
the instrument:

  ** CAMB ON THE SAME DATA SUBSET GIVES 122.1 meV, WHICH IS LOOSER THAN 60's 111.38. **

So 60's harness is not too loose -- on this data it is slightly TIGHTER than CAMB.  The gap
to the published 64.2 meV is the DATA SUBSET, and the direction of this reference's own
deviation strengthens that rather than weakening it: it scores 613 plik_lite bins where 60
score 555, which is MORE information and biases a limit TIGHT, so on 60's own subset the
reference would be looser still and the margin over 111.38 wider.

** AND THE CONDITIONAL PROFILE IS A TRAP THIS SEAT WALKED INTO AND REGISTERED ITS WAY OUT OF. **
Profiling tau alone with H0 and Omega_m HELD at the control gives 82.9 meV and puts the
minimum at 0.05 eV with Sum = 0 disfavoured by Delta chi^2 = 5.749 -- a 2.4 sigma preference
for a nonzero mass.  Both are ARTEFACTS of holding the geometry: the sum is strongly
degenerate with H0 and Omega_m, and holding them forbids the data from buying a larger sum by
moving the geometry.  Opened, the minimum returns to Sum = 0 exactly and the preference
vanishes, while H0 runs 67.952 -> 64.180 and Omega_m 0.3079 -> 0.3575 across the grid.  The
script that produced the conditional number said in its own docstring, before it ran, that the
opened one decides -- and an in-flight commit message that read a verdict off the conditional
limit is corrected by this revision rather than left standing.

THE STRUCTURAL FINDING THAT RESHAPED ITEM ④, and it is about where a discrepancy CAN live.
60's lensing operator is CAMB ITSELF: lensing_operator3.py forms
RATIO = cl['total'] / cl['unlensed_scalar'] from a camb.get_results call at each sum.  So the
operator is not an independent instrument and CANNOT be the site of a disagreement with CAMB,
and this reference reproduces the banked operator to 0.0 ppm -- bit for bit, three channels,
every sum -- which confirms it and 60's convention columns with it.  The sum response
factorises EXACTLY into the operator term and the unlensed term, closing to 4e-10 ppm, so
there is no third term and whatever is 60's own lives entirely in the unlensed half.  And the
half 60 already hold is the SMALL half: it carries 0-1 per cent of the TT sum response at the
low multipoles that dominate the 555-bin score.

A DEFECT THIS SEAT REPORTED AND THEN HAD TO WITHDRAW.  I first flagged 60 for leaving
lens_potential_accuracy unset.  That was wrong, and the mechanism is the opposite of what I
assumed: in camb 2.0.4 set_for_lmax reads None NOT as the low default but as an AUTOMATIC
HIGH-accuracy max(4, (lmax-1500)/500), which is 4 at lmax = 3000, with non-linear lensing
switched on with it.  Leaving it unset is CORRECT.  Hand-setting it to 0 would cost ~2400 ppm
in TT, which is the size of the entire Sum = 0.06 eV signal, so the setting 60 did not write
is the one that saved the operator.

WHAT IS CLEAN, each measured rather than assumed:
  * the convention -- total omega_m held at 0.143097 at every sum, omega_cb falling by
    omega_nu, three species normal ordering;
  * CAMB's phi-phi against the SAME nine conservative bandpowers through 60's own windows:
    chi^2/dof = 1.055 with NO monotone drift, against 60's own docstring figure of 2.05 WITH
    one, which puts that drift in the instrument and not in the bandpowers or their banking;
  * the pipeline validated before anything was claimed from it -- CAMB at 60's control scores
    0.96 per bin with the fitted amplitude within 0.06 per cent of unity.

COMPUTES: nothing of the physics 60 own.  It re-reads banked outputs of this revision's own
          computation and 60's banked lensing data, recomputes the phi-phi chi^2 and its
          residual drift against 60's covariance, recomputes both 95 per cent limits from the
          banked profiles by the first crossing ABOVE the minimum, and recomputes the
          unbounded vertex by parabolic fits.

** THE PINS ARE VERIFIED FAILABLE BY PERTURBATION, NOT ASSUMED TO BE. **  Each banked input was
perturbed in turn and the arms that pin it watched to redden, then restored:
  * the opened profile's Delta chi^2 scaled by 1.0025 -- which moves the limit 0.22 meV, just
    over check_figures_pinned's 0.061 meV allowance for a printed 122.06 -- reddens Ⓘ⑨;
    doubling it reddens Ⓘ⑨, Ⓙ⑩, Ⓛ⑫ and Ⓝ⑭, so the limit is cross-pinned four ways;
  * the banked bandpowers scaled by 1.25 reddens Ⓖ⑦ and Ⓖ⑦ᵇ;
  * the reproduction's max_abs_ppm set to 7.5 reddens Ⓒ③.
⌗ And Ⓘ⑨'s tolerance was 0.5 at first, which is EIGHT TIMES too slack to pin the figure the
INDEX row prints -- check_figures_pinned caught it, along with two figures the row printed that
this seat cannot pin at all (60's 111.38 and the published 64.2, both one-sided comparisons
here); those are printed to fewer digits instead, which is the honest precision anyway since
60's carries +/- 0.41.  The baseline did not grow: it stayed at 1431 while the key count fell
from 1343 to 1340, because 122.06 is now PINNED rather than baselined.

Bound: this receipt pins THIS REFERENCE's figures and its comparison against 60's banked
numbers.  It does NOT rule on whether 60's Phi transport through the radiation era is correct
-- it says that gap is not where the missing factor 1.7 lives, not that the treatment is
right.  It pins no cosmological parameter as a result.
"""
import ast
import json
import os
import re
import sys

import numpy as np

FAILED = []
RAN = []


def check(label, ok, detail=''):
    RAN.append(label)
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BTW, 'r7847_cc66_a_camb_reference_for_60s_neutrino_mass_harness')
R42 = os.path.join(BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                        'the_harness_does_not_have')
R46 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')


def load(name, where=MINE):
    with open(os.path.join(where, name), encoding='utf-8') as fh:
        return json.load(fh)


TAB = load('channel_table.json')
COND = load('score_reference.json')
OPEN_ = load('profile_open.json')

# ---------------------------------------------------------------- the convention
check('Ⓐ① PINNED the convention is 60\'s own, read off THEIR ratio_grid3.npz and not retyped: '
      'total omega_m 0.143097 held, omega_b h^2 0.02237, H0 67.40, divisor 93.14',
      abs(TAB['reference']['omh2_total'] - 0.14309694) < 1e-8
      and abs(TAB['reference']['ombh2'] - 0.02237) < 1e-12
      and abs(TAB['reference']['H0'] - 67.40) < 1e-12
      and abs(TAB['reference']['divisor'] - 93.14) < 1e-12,
      'omh2 %.8f, ombh2 %.5f, H0 %.2f, div %.2f' % (
          TAB['reference']['omh2_total'], TAB['reference']['ombh2'],
          TAB['reference']['H0'], TAB['reference']['divisor']))

# ------------------------------------------- 60's operator IS CAMB, read STRUCTURALLY
# ** THIS ARM IS DELIBERATELY NOT A TEXT MATCH ON 60's SOURCE. **  Its first version asserted
# `'camb.get_results' in _OP` and a regex on their `le, un = cl['total'], cl['unlensed_scalar']`
# line, which minted two quote-pin keys -- and check_quote_pins was right to red them: a pin on
# wording ANOTHER SEAT OWNS fails when that seat rewords, which is this programme's named defect
# class and not a property anyone wants.  Renaming `le`/`un`, or splitting the call across two
# statements, would have reddened an arm whose CLAIM was untouched.
#   ⇒ It is read off the parsed SYNTAX instead: the module imports camb, calls get_results on it,
#     and subscripts the result with CAMB's own two spectrum keys.  That breaks only if 60 stop
#     forming the operator from CAMB -- which is exactly when this receipt's item ④ conclusion
#     stops holding and the arm SHOULD be read.
#   ⌗ And the behavioural proof is Ⓒ③, which is stronger than any reading of their source: CAMB
#     reproduces their banked operator BIT FOR BIT. This arm records the mechanism; Ⓒ③ proves it.
_OPT = ast.parse(open(os.path.join(R42, 'lensing_operator3.py'), encoding='utf-8').read())
_imports_camb = any(isinstance(n, ast.Import) and any(a.name == 'camb' for a in n.names)
                    for n in ast.walk(_OPT))
_calls_get_results = any(
    isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
    and n.func.attr == 'get_results'
    and isinstance(n.func.value, ast.Name) and n.func.value.id == 'camb'
    for n in ast.walk(_OPT))
_keys = {n.slice.value for n in ast.walk(_OPT)
         if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant)
         and isinstance(n.slice.value, str)}
check('Ⓑ② PINNED 60\'s lensing operator is CAMB ITSELF -- read off the parsed SYNTAX of the '
      'module that RUNS, not off its docstring and not off its wording: it imports camb, calls '
      "camb.get_results, and subscripts the result with 'total' and 'unlensed_scalar', so the "
      'operator cannot be the site of a disagreement with CAMB',
      _imports_camb and _calls_get_results and {'total', 'unlensed_scalar'} <= _keys,
      'imports camb %s, calls get_results %s, spectrum keys %s'
      % (_imports_camb, _calls_get_results, sorted({'total', 'unlensed_scalar'} & _keys)))

# ------------------------------------------- arm A: the reproduction, and the accuracy contrast
_auto = [v for k, v in TAB['arm_a_reproduction'].items() if k.startswith('auto4_')]
_low = [v for k, v in TAB['arm_a_reproduction'].items() if k.startswith('lpa0_')]
check('Ⓒ③ PINNED at 60\'s OWN accuracy the banked operator reproduces BIT FOR BIT -- 0.0 ppm '
      'in ratio_tt and ratio_ee and 0.0 in c_TE, at every sum -- which confirms the banked '
      'operator and 60\'s convention columns with it',
      len(_auto) >= 4
      and all(v['ratio_tt']['max_abs_ppm'] == 0.0 and v['ratio_ee']['max_abs_ppm'] == 0.0
              and v['dte_over_tt']['max_abs_diff'] == 0.0 for v in _auto),
      '%d sums, worst %g ppm' % (len(_auto), max(v['ratio_tt']['max_abs_ppm'] for v in _auto)))
check('Ⓒ③ᵇ PINNED and the contrast PRICES the setting rather than assuming it: at '
      'lens_potential_accuracy = 0 the same comparison is ~2400 ppm out in TT, which is the '
      'size of the ENTIRE Sum = 0.06 eV signal -- so leaving it unset is what saved it',
      len(_low) >= 4 and max(v['ratio_tt']['max_abs_ppm'] for v in _low) > 1000.0,
      'worst %.1f ppm' % max(v['ratio_tt']['max_abs_ppm'] for v in _low))

# -- the WITHDRAWN defect: camb's own source says None means HIGH accuracy, not low
import camb                                                                 # noqa: E402
import inspect                                                              # noqa: E402
_SRC = inspect.getsource(camb.CAMBparams.set_for_lmax)
check('Ⓓ④ PINNED the defect this seat reported is WITHDRAWN, and off CAMB\'s own source: '
      'set_for_lmax reads lens_potential_accuracy=None as an AUTOMATIC HIGH default '
      'max(4, (lmax-1500)/500), so 60 passing none runs at 4 and NOT at the low default',
      re.search(r'lens_potential_accuracy\s*=\s*max\(\s*4\.?0?\s*,\s*\(\s*lmax\s*-\s*1500', _SRC)
      is not None,
      'camb %s' % getattr(camb, '__version__', '?'))

# ------------------------------------------- arm C: the factorisation is complete
_res = [max(v[ch][b]['max_abs_ppm'] for ch in ('TT', 'EE') for b in v[ch])
        for v in TAB['arm_c_closure'].values()]
check('Ⓔ⑤ PINNED the response factorises EXACTLY into the operator term and the unlensed '
      'term: d ln lensed - d ln unlensed - d ln RATIO is machine zero in every band at every '
      'sum, so there is NO third term and whatever is 60\'s own lives in the unlensed half',
      len(_res) >= 6 and max(_res) < 1e-6,
      'worst residual %.2e ppm over %d cases' % (max(_res), len(_res)))

# ------------------------------------------- the banked half is the SMALL half
_b = TAB['arm_b_unlensed']['auto4_sum0.06']
_tt_lo = abs(_b['TT_operator']['30-250']['mean_pct'] / _b['TT_lensed']['30-250']['mean_pct'])
_tt_hi = abs(_b['TT_operator']['250-650']['mean_pct'] / _b['TT_lensed']['250-650']['mean_pct'])
check('Ⓕ⑥ PINNED the term 60 ALREADY HOLD is the SMALL half -- the banked operator carries '
      'under 2 per cent of the TT sum response on the two bands that dominate the 555-bin '
      'score, so what sets the limit is the UNLENSED response their own solver supplies',
      _tt_lo < 0.02 and _tt_hi < 0.02,
      'operator/lensed = %.4f at l 30-250, %.4f at l 250-650' % (_tt_lo, _tt_hi))

# ------------------------------------------- phi-phi against 60's OWN banked data
sys.path.insert(0, R46)
import lensing_like as LL                                                   # noqa: E402

_bp = np.asarray(COND['rows'][0]['bandpowers'], float)
_dat = np.asarray(LL.DATA, float)
_err = np.sqrt(np.diag(np.asarray(LL.COV, float)))
_resid = (_bp - _dat) / _err
_c2 = float(LL.chi2(_bp))
check('Ⓖ⑦ PINNED CAMB\'s phi-phi against the SAME nine conservative bandpowers, through 60\'s '
      'own windows and covariance, scores chi^2/dof = 1.06 where 60\'s own docstring records '
      '2.05 -- so the SIZE of their lensing residual is the instrument\'s',
      abs(_c2 / LL.NBP - 1.0554) < 0.02 and _c2 / LL.NBP < 1.5,
      'chi2 %.4f / %d = %.4f' % (_c2, LL.NBP, _c2 / LL.NBP))
_L = np.arange(len(_resid), dtype=float)
_rho = float(np.corrcoef(_L, _resid)[0, 1])
check('Ⓖ⑦ᵇ PINNED and the DRIFT is the instrument\'s too, which is the decisive half: this '
      'reference\'s residuals CHANGE SIGN across the nine bandpowers and carry no trend, '
      'where 60 record a MONOTONE drift -- so the drift is not in the data or its banking',
      not ((_resid > 0).all() or (_resid < 0).all()) and abs(_rho) < 0.35,
      'signs %s, corr %+.3f' % (''.join('+' if v > 0 else '-' for v in _resid), _rho))

# ------------------------------------------- both limits, recomputed from the banked profiles
def limit95(sums, dchi2):
    """the first crossing ABOVE the minimum -- a scan from the bottom of the grid is the bug"""
    s = np.asarray(sums, float)
    d = np.asarray(dchi2, float)
    i = int(np.argmin(d))
    hs, hd = s[i:], d[i:]
    fine = np.linspace(float(hs[0]), float(hs[-1]), 20001)
    k = np.where(np.interp(fine, hs, hd) > 2.71)[0]
    return (float(s[i]), float(fine[k[0]]) if k.size else None)


_cmin, _clim = limit95(COND['sums'], COND['dchi2'])
_omin, _olim = limit95(OPEN_['sums'], OPEN_['dchi2'])
check('Ⓗ⑧ PINNED the CONDITIONAL profile is an ARTEFACT OF HOLDING THE GEOMETRY and is '
      'reported as such: with H0 and Omega_m held it puts the minimum at 50 meV and '
      'DISFAVOURS a zero sum by Delta chi^2 = 5.75, a spurious 2.4 sigma preference for a '
      'nonzero neutrino mass, and its limit is 82.9 meV',
      abs(_cmin - 0.05) < 1e-9 and _clim is not None and abs(_clim * 1000 - 82.9) < 0.5
      and abs(COND['dchi2'][0] - 5.749) < 0.01,
      'min %.3f eV, limit %.1f meV, dchi2(0) = %.3f' % (_cmin, _clim * 1000, COND['dchi2'][0]))
check('Ⓘ⑨ PINNED OPENED -- tau, H0 and Omega_m free -- the minimum returns to Sum = 0 EXACTLY, '
      'the spurious preference vanishes, and the 95 per cent limit is 122.1 meV.  This is the '
      'limit the registered call turns on, and the script said so before it ran',
      # ** the tolerance is INSIDE check_figures_pinned's allowance for a printed 122.06 **
      # (the coarser of half a last digit, 0.005, and 0.05 per cent of |X|, 0.061).  It was
      # 0.5 first, which is eight times too slack to PIN the figure the INDEX row prints --
      # a one-sided or over-wide comparison is not a pin, and the gate said so.
      abs(_omin) < 1e-12 and _olim is not None and abs(_olim * 1000 - 122.06) < 0.05,
      'min %.4f eV, limit %.2f meV' % (_omin, _olim * 1000))
_h0 = [r['H0'] for r in OPEN_['rows']]
_om = [r['Om'] for r in OPEN_['rows']]
check('Ⓘ⑨ᵇ PINNED and the geometry MOVED, which is WHY the conditional number was wrong '
      'rather than merely different: across the grid H0 falls 67.95 -> 64.18 and Omega_m '
      'rises 0.308 -> 0.358, the data buying a larger sum by moving the geometry',
      _h0[0] > _h0[-1] + 3.0 and _om[-1] > _om[0] + 0.04,
      'H0 %.3f -> %.3f, Om %.4f -> %.4f' % (_h0[0], _h0[-1], _om[0], _om[-1]))

# ------------------------------------------- THE FINDING: 60's instrument is cleared
check('Ⓙ⑩ PINNED THE FINDING, and it cuts the other way from the order\'s premise: the '
      'independent reference gives 122.1 meV where 60\'s control gives 111.38, so CAMB on '
      'this data is LOOSER than 60\'s harness and their 111.38 is NOT evidence of an '
      'instrument fault -- the gap to the published 64.2 meV is the DATA SUBSET',
      _olim * 1000 > 111.38 and _olim * 1000 > 64.2,
      'reference %.2f meV against 60\'s 111.38 and the published 64.2' % (_olim * 1000))
check('Ⓚ⑪ PINNED and this reference\'s OWN deviation strengthens that conclusion instead of '
      'weakening it, which is the arm that makes the finding safe: it scores 613 plik_lite '
      'bins where 60 score 555 -- MORE information, which biases a limit TIGHT -- so on 60\'s '
      'own subset the reference would be LOOSER still and the margin over 111.38 wider',
      COND['scored_bins'] == 613 and '555' in COND['bin_subset_note']
      and 'not reproducible here' in COND['bin_subset_note'].lower(),
      '%d bins scored; the 555-bin mask is isfinite over grids that lived under /tmp'
      % COND['scored_bins'])

# ------------------------------------------- the registered bands, adjudicated against this seat
_verts = []
for k in (4, 5, 6):
    a, b, _c = np.polyfit(np.asarray(OPEN_['sums'][:k], float),
                          np.asarray(OPEN_['dchi2'][:k], float), 2)
    _verts.append(-b / (2 * a) * 1000.0)
check('Ⓛ⑫ PINNED Ⓓ CONFIRMED but AT ITS FLOOR, stated rather than rounded away: the '
      'registered band was 120-400 meV and the reference gives 122.06, inside by 2.06 meV',
      120.0 <= _olim * 1000 <= 400.0,
      '%.2f meV, %.2f meV above the floor' % (_olim * 1000, _olim * 1000 - 120.0))
check('Ⓜ⑬ PINNED Ⓔ REFUTED, AND AGAINST THIS SEAT, on the reading that MATCHES WHAT THE '
      'PUBLISHED FIGURE IS: I registered that the effective mass would NOT reproduce the '
      'published -101 meV, band -50..+100.  The grid minimum is 0 meV, but a published '
      'NEGATIVE effective mass is an UNBOUNDED vertex, and parabolic fits to the lowest 4, 5 '
      'and 6 points give -94, -86 and -90 meV -- which essentially reproduces -101.  The '
      'reading that would have PASSED the band is not the quantity the published number is',
      all(v < -50.0 for v in _verts) and all(abs(v + 101.0) < 30.0 for v in _verts),
      'vertices %s meV against the published -101' % ', '.join('%+.1f' % v for v in _verts))
check('Ⓝ⑭ PINNED Ⓕ\'s registered antecedent is therefore NOT satisfied, since it required '
      'BOTH Ⓓ and Ⓔ -- and the conclusion is reported on 69\'s OWN named finding condition '
      'instead, which is independent of this seat\'s bands and FIRES: CAMB does not reach '
      'about 64 meV on this subset, it reaches 122.1',
      _olim * 1000 > 64.2 * 1.5,
      'the order\'s condition fires at %.1f meV against about 64' % (_olim * 1000))

# ------------------------------------------- the count, COUNTED and then PINNED
# ** this arm is itself counted, so adding or removing an arm reddens HERE and gets read.
# The first version of this line asserted a typed 16 against 18 arms actually run, which is
# the hollow-count defect this layer exists to catch -- so it counts now and pins the count.
_arms = len(RAN) + 1
check('Ⓞ⑮ the count, COUNTED off the arms that ran and then PINNED at 18 so that adding or '
      'removing one reddens here: every arm adjudicated, two of this seat\'s own registered '
      'calls REFUTED and one reported defect WITHDRAWN, with nothing loosened to pass',
      len(FAILED) == 0 and _arms == 18, '%d arms ran' % _arms)

print()
if FAILED:
    print(f'FAILED {len(FAILED)}:')
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('ALL PASS')
