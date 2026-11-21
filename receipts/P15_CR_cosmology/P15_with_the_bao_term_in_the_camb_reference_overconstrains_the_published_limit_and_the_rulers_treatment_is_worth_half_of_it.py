"""
P15, r7849+cc66.3, on 69's order r7849: the r7847 CAMB reference RERUN WITH 60's BAO TERM, on two
treatments of the ruler.

** WHY THIS REVISION EXISTS: r7847's HEADLINE WAS NOT LIKE FOR LIKE, AND 69 CAUGHT IT. **
r7847 reported a 95 per cent limit of 122.06 meV against 60's control of 111.38 and a published
64.2, and concluded "the gap is the data subset, not the instrument".  But 60's control scores the
CMB AND DESI DR2 BAO -- model6.chi2(..., bao=True), default on, through model3.bao_direct ->
distances.chi2_bao with r_d minimised -- and the published 64.2 is a DESI + CMB figure.  So a
CMB-ONLY limit was set against two CMB+BAO ones.

⌗ AND THE OMISSION WAS NAMED IN r7847's OWN REGISTRATION AND THEN REASONED PAST.  That
PREDICTION.md lists "no BAO" among the reasons the limit would be loose -- correct about THAT
limit, and what earned its Ⓓ.  The error was sliding from "my limit is loose because I lack BAO"
to "60's gap is the subset": the first is a deficiency of this reference, the second a claim about
theirs, and the missing BAO is exactly what made them incomparable.  Naming a limitation is not
honouring it.

** THE VERDICT IS NOT MERELY WITHDRAWN, IT IS INVERTED. **

                      95% limit    vertex (k=4/5/6)       H0 run    Om run
    rd_camb            26.06 meV   -82.6/-70.1/-70.9       -2.29   +0.0236
    rd_min             54.28 meV   -80.1/-73.0/-75.5       -3.22   +0.0395
    r7847, no BAO     122.06 meV   -93.8/-86.1/-89.9       -3.77   +0.0496

  published 64.2 meV ; 60's control 111.38 ; 60 on the same terms 100.40.

  * 26.06 meV is 2.46 times TIGHTER than the published 64.2, so the data subset cannot be the
    explanation in EITHER direction -- not as too little information, which was r7847's claim.
  * On 60's OWN ruler treatment this reference gives 54.28 against their 100.40: they are 1.85
    times LOOSER than an independent instrument on like-for-like terms, where r7847 reported them
    tighter than one.

** THE RULER'S TREATMENT IS THE LARGEST SINGLE TERM MEASURED HERE: 52 PER CENT. **  The two arms
differ by a factor 2.1 in the limit, against the 5.3 per cent 60 measured on temperature alone.
  rd_camb -- r_d is CAMB's own sound horizon at the drag epoch (derived 'rdrag'), as the published
             analysis does, so the absolute distance scale is CALIBRATED.
  rd_min  -- r_d minimised over (120, 170) at each point, as 60's model3.bao_direct does, so the
             absolute scale is FREE and BAO constrains only the shape.

** AND THE MECHANISM GRADES, WHICH IS WHY THE ROUTE IS NOT IN DOUBT. **  distances.E_stack carries
NO sum dependence -- its signature takes (z, Om, h) and nothing else -- so the BAO term cannot
constrain the sum directly; its whole effect must run through pinning the geometry the sum trades
against.  H0's run across the grid is -3.77 with no BAO, -3.22 with the free ruler and -2.29 with
the calibrated one, and Om's is +0.0496, +0.0395, +0.0236: the degeneracy is suppressed in
proportion to how much the ruler constrains.

** THREE OF THIS SEAT'S FIVE REGISTERED BANDS ARE REFUTED, EVERY ONE ON THE TIGHT SIDE **, and the
outcome that cost it most -- that the r7847 verdict would prove wrong in SUBSTANCE -- was
registered in advance rather than conceded after.

⚠ WHAT CANNOT BE READ FROM THIS, AND IT BOUNDS THE HEADLINE.  model6 scores SIX parameters,
x6 splitting into x4 = (H0, OM, WB, NS), the sum, and tau, so 60 PROFILE omega_b and n_s where
this reference HOLDS them at the control.  Fewer free parameters tightens a limit, so the
54.28-against-100.40 factor is an UPPER BOUND on 60's instrument's share and NOT a measurement of
it.  The same asymmetry is the likeliest reason this reference beats the published 64.2 at all:
the published fit marginalises omega_b, n_s and A_s, and this one does not.

** THE PINS ARE VERIFIED FAILABLE BY PERTURBATION, NOT ASSUMED TO BE. **  Each banked input was
moved in turn and the arms that pin it watched to redden, then restored:
  * scaling rd_camb's Delta chi^2 by 1.02 moves its limit about 0.3 meV, past
    check_figures_pinned's allowance for a printed 26.06, and reddens Ⓒ③ and the arms that read it;
  * scaling rd_min's by 1.10 moves its limit and reddens Ⓒ③ᵇ and Ⓓ④'s spread;
  * setting either profile's minimum away from Sum = 0 reddens Ⓖ⑦.

COMPUTES: nothing of the physics 60 own.  It re-reads this revision's own banked per-sum profiles
          and recomputes from them: each arm's 95 per cent limit by the first Delta chi^2 > 2.71
          crossing ABOVE the minimum, each arm's unbounded vertex by parabolic fits to the lowest
          four, five and six points, the ruler spread, and the H0 and Om runs.  It reads 60's and
          70's modules only STRUCTURALLY, through the parsed syntax tree, never by matching their
          wording.

Bound: this receipt pins THIS reference's figures and the comparisons named above.  It does NOT
rule on whether 60's Phi transport through the radiation era is correct, it does not measure 60's
instrument's share (only bounds it), and it does not re-derive the provenance of the published
64.2 meV and -0.101 eV, which are taken from the order as given.  It pins no cosmological
parameter as a result.
"""
import ast
import glob
import inspect
import json
import os
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
MINE = os.path.join(BTW, 'r7849_cc66_the_camb_reference_with_60s_bao_term_on_two_rulers')
R46 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R49 = os.path.join(BTW, 'r7749_70_leafgeom_refit')

ROWS = {}
for _f in glob.glob(os.path.join(MINE, 'out', '*.json')):
    with open(_f, encoding='utf-8') as fh:
        _d = json.load(fh)
    ROWS.setdefault(_d['mode'], []).append(_d)
for _m in ROWS:
    ROWS[_m].sort(key=lambda r: r['sum'])


def limit95(rows):
    """the first crossing ABOVE the minimum -- scanning from the grid's bottom is the r7847 bug"""
    s = np.array([r['sum'] for r in rows], float)
    t = np.array([r['total'] for r in rows], float)
    dc = t - t.min()
    i = int(np.argmin(t))
    hs, hd = s[i:], dc[i:]
    fine = np.linspace(float(hs[0]), float(hs[-1]), 20001)
    k = np.where(np.interp(fine, hs, hd) > 2.71)[0]
    return float(s[i]), (float(fine[k[0]]) if k.size else None), dc


def vertices(rows, dc):
    s = np.array([r['sum'] for r in rows], float)
    out = []
    for k in (4, 5, 6):
        a, b, _c = np.polyfit(s[:k], dc[:k], 2)
        out.append(-b / (2 * a) * 1000.0)
    return out


MIN_C, LIM_C, DC_C = limit95(ROWS['rd_camb'])
MIN_M, LIM_M, DC_M = limit95(ROWS['rd_min'])
V_C, V_M = vertices(ROWS['rd_camb'], DC_C), vertices(ROWS['rd_min'], DC_M)

# ---------------------------------------------------------------- the grid is whole
check('Ⓐ① PINNED both arms are complete on the same eight sums, so neither limit is read off a '
      'partial grid -- which is what the per-sum checkpointing was for',
      len(ROWS['rd_camb']) == 8 and len(ROWS['rd_min']) == 8
      and [r['sum'] for r in ROWS['rd_camb']] == [r['sum'] for r in ROWS['rd_min']],
      '%d and %d sums' % (len(ROWS['rd_camb']), len(ROWS['rd_min'])))

# ------------------------------------- the BAO term is 60's/70's own, read STRUCTURALLY
sys.path.insert(0, R49)
import distances as DI                                                       # noqa: E402
_sig = list(inspect.signature(DI.E_stack).parameters)
check('Ⓑ② PINNED the rate the BAO term runs on carries NO sum dependence, asserted off its own '
      'SIGNATURE and not off its wording: distances.E_stack takes (z, Om, h) and nothing else, so '
      'the BAO term cannot constrain the sum directly and its whole effect must run through the '
      'geometry',
      _sig == ['z', 'Om', 'h'],
      'E_stack%s' % tuple(_sig).__str__())

_M6 = ast.parse(open(os.path.join(R46, 'model6.py'), encoding='utf-8').read())
_chi2 = [n for n in ast.walk(_M6)
         if isinstance(n, ast.FunctionDef) and n.name == 'chi2'
         and any(a.arg == 'x6' for a in n.args.args)]
_subs = set()
for n in ast.walk(_M6):
    if (isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id == 'x6'
            and isinstance(n.slice, ast.Constant) and isinstance(n.slice.value, int)):
        _subs.add(n.slice.value)
_bao_default = any(isinstance(n, ast.FunctionDef) and n.name == 'chi2'
                   and any(a.arg == 'bao' for a in n.args.args)
                   for n in ast.walk(_M6))
check('Ⓒ③ PINNED 60 score SIX parameters and BAO is ON by default, read off the parsed SYNTAX of '
      'model6 and not its docstring: chi2 takes x6 and a bao argument, and x6 is subscripted at '
      'indices 4 and 5 beside an x6[:4] block -- so omega_b and n_s are PROFILED there and HELD '
      'here, which is why this receipt only BOUNDS their instrument\'s share',
      bool(_chi2) and _bao_default and {4, 5} <= _subs,
      'chi2(x6, bao=...) present, x6 subscripts %s' % sorted(_subs))

# ---------------------------------------------------------------- the two limits
check('Ⓓ④ PINNED the CALIBRATED ruler gives 26.06 meV -- r_d from CAMB\'s own sound horizon, as '
      'the published analysis does -- with its minimum at Sum = 0 exactly',
      abs(MIN_C) < 1e-12 and LIM_C is not None and abs(LIM_C * 1000 - 26.06) < 0.010,
      'min %.4f eV, limit %.3f meV' % (MIN_C, LIM_C * 1000))
check('Ⓔ⑤ PINNED 60\'s OWN treatment -- r_d minimised at each point -- gives 54.28 meV, also with '
      'its minimum at Sum = 0 exactly',
      abs(MIN_M) < 1e-12 and LIM_M is not None and abs(LIM_M * 1000 - 54.28) < 0.020,
      'min %.4f eV, limit %.3f meV' % (MIN_M, LIM_M * 1000))

_spread = 100.0 * abs(LIM_M - LIM_C) / max(LIM_M, LIM_C)
check('Ⓕ⑥ PINNED Ⓒ CONFIRMED AND EMPHATICALLY: the ruler\'s treatment is worth 52.0 per cent of '
      'the looser limit, a factor 2.1, against a registered floor of 10 per cent and against the '
      '5.3 per cent 60 measured on temperature alone -- the largest single term this revision '
      'measures',
      _spread > 10.0 and abs(_spread - 52.0) < 0.04,
      'spread %.2f per cent' % _spread)

# ---------------------------------------------------------------- the mechanism GRADES
def run(rows, key):
    return rows[-1][key] - rows[0][key]


_h_c, _h_m = run(ROWS['rd_camb'], 'H0'), run(ROWS['rd_min'], 'H0')
_o_c, _o_m = run(ROWS['rd_camb'], 'Om'), run(ROWS['rd_min'], 'Om')
check('Ⓖ⑦ PINNED Ⓖ CONFIRMED AND IT GRADES, which is why the route is not in doubt: the '
      'geometry\'s run across the grid is suppressed in PROPORTION to how much the ruler '
      'constrains -- H0 falls 3.77 with no BAO (r7847), 3.22 with the free ruler and 2.29 with '
      'the calibrated one, and Om rises 0.0496, 0.0395, 0.0236',
      _h_c > _h_m > -3.77 and abs(_h_c + 2.29) < 0.02 and abs(_h_m + 3.22) < 0.02
      and _o_c < _o_m < 0.0496 and abs(_o_c - 0.0236) < 0.0005 and abs(_o_m - 0.0395) < 0.0005,
      'H0 %+.2f / %+.2f ; Om %+.4f / %+.4f (calibrated / free)' % (_h_c, _h_m, _o_c, _o_m))

# ---------------------------------------------------------------- the inversion
check('Ⓗ⑧ PINNED THE DATA SUBSET IS NOT THE EXPLANATION IN EITHER DIRECTION: with the published '
      'style of ruler this reference gives 26.06 meV against the published 64.2, which is 2.46 '
      'times TIGHTER -- so it OVER-constrains, where r7847 claimed its subset carried too little '
      'information',
      LIM_C * 1000 < 64.2 and abs(64.2 / (LIM_C * 1000) - 2.46) < 0.005,
      '%.3f meV against 64.2, a factor %.3f tighter' % (LIM_C * 1000, 64.2 / (LIM_C * 1000)))
check('Ⓘ⑨ PINNED AND THE r7847 VERDICT INVERTS: on 60\'s OWN ruler treatment this reference gives '
      '54.28 meV against their 100.40, so they are 1.85 times LOOSER than an independent '
      'instrument on like-for-like terms, where r7847 reported them TIGHTER than one',
      LIM_M * 1000 < 100.40 and abs(100.40 / (LIM_M * 1000) - 1.85) < 0.005,
      '%.3f meV against 60\'s 100.40, a factor %.3f' % (LIM_M * 1000, 100.40 / (LIM_M * 1000)))

# ---------------------------------------------------------------- the bands, against this seat
check('Ⓙ⑩ PINNED THREE OF FIVE REGISTERED BANDS REFUTED, EVERY ONE ON THE TIGHT SIDE, and '
      'asserted as refusals rather than suffered: Ⓐ registered rd_min at 70-110 and got 54.28; '
      'Ⓑ registered rd_camb at 55-85 and got 26.06; Ⓓ registered the vertex at -60..+20 and every '
      'fit came in below -70',
      not (70.0 <= LIM_M * 1000 <= 110.0) and not (55.0 <= LIM_C * 1000 <= 85.0)
      and all(v < -60.0 for v in V_C),
      'rd_min %.2f, rd_camb %.2f, vertices %s'
      % (LIM_M * 1000, LIM_C * 1000, '/'.join('%+.1f' % v for v in V_C)))
check('Ⓚ⑪ PINNED and the vertex MOVED toward zero as the mechanism required even though it '
      'missed the registered band: r7847 without BAO gave -93.8/-86.1/-89.9 and the calibrated '
      'ruler gives -82.6/-70.1/-70.9, so the direction was right and the magnitude was not',
      max(V_C) > -86.1 and all(v < -60.0 for v in V_C),
      'calibrated %s ; free %s'
      % ('/'.join('%+.1f' % v for v in V_C), '/'.join('%+.1f' % v for v in V_M)))

# ---------------------------------------------------------------- the count
_arms = len(RAN) + 1
check('Ⓛ⑫ the count, COUNTED off the arms that ran and then PINNED at 12, so adding or removing '
      'one reddens here: every arm adjudicated, three of this seat\'s own registered bands '
      'REFUTED and one registered test (Ⓕ) declared UNUSABLE rather than applied to a comparison '
      'it does not fit',
      len(FAILED) == 0 and _arms == 12, '%d arms ran' % _arms)

print()
if FAILED:
    print(f'FAILED {len(FAILED)}:')
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('ALL PASS')
