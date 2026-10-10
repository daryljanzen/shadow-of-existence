"""S1 -- THE TEN PASSAGES WERE ONE PAPER: THE SAME SWEEP, CORPUS-WIDE (node 70, `r7037`).

`r7033` found ten passages of `CR_cosmology.tex` quoting a significance or a share their instrument cannot bear.
Nothing had checked the other papers.  ** a) Every claim of noise, significance, detection or share in every paper,
traced to the receipt that computes it.  b) A verdict per hit: (i) a real noise model, so the claim stands; (ii) a
spread of computed quantities, so the wording overclaims; (iii) cannot be determined from the repository.  c) How
many of class (ii) per paper, and whether any is load-bearing for an abstract or a conclusion. **

** THE ANSWER TO c), FIRST: NO ABSTRACT AND NO CONCLUSION IN THE CORPUS RESTS ON AN OVERCLAIMED SIGMA. **
Every statistical claim in any paper's abstract or conclusion traces to a real noise model:
  * the light-element abundances "within 1 sigma" (cosmogenesis, CR_framework, CR_cosmology) -- published
    observational errors combined in quadrature with a theory error propagated from the reaction-rate
    uncertainties (`P16_theory_error_and_likelihood`);
  * the distance ladder at chi^2/dof ~ 1 against DESI DR2 -- DESI's own per-tracer covariances
    (`P15_desi_dr2_confrontation`);
  * the low multipoles "consistent within cosmic variance" -- the exact likelihood, each C_l a scaled
    chi^2 on 2l+1 degrees of freedom (`P15_verify_lowell_likelihood_v2`).

** AND OUTSIDE `CR_cosmology.tex` THERE IS NO CLASS (ii) AT ALL. **  Seventeen papers swept whole.  What they
quote is the plik_lite likelihood's own covariance, DESI's, published measurement errors, the cosmic-variance
likelihood, or a predicted rms of a random field against an observed bound.  Most of what the patterns catch is
not statistical at all -- sigma as the root-exchange involution, chi as a coordinate, "tension" and "detected"
in their ordinary senses, numerical precision -- and each exclusion is named.  ⇒ *** The defect class was local
to the one paper that had a seat auditing it. ***

** INSIDE `CR_cosmology.tex`, RE-SWEPT WHOLE: THREE CLASS (ii) AND TWO CLASS (iii), ALL BELOW THE HEADLINE. **
  (ii) "the arm sits ONE STANDARD DEVIATION from the sky" (`sec:refit-bound`) -- the sky's intercept error
       +-0.0099 is the locator's move across seven parabola windows on one realisation: a PROCEDURE spread.  The
       receipt that propagated the covariance through the locator did so at the fourth peak and says in terms it
       does not re-open the intercept.  Honest form: "inside the locator's window-to-window spread".
  (ii) "the relative phase is determined ... at better than SEVEN STANDARD DEVIATIONS" (`sec:refit-bound`) --
       the +-0.000974 rad is the standard error over disjoint stretches of the phase difference between two
       COMPUTED spectra; no noise enters it.  Honest form: "to seven times its stretch-to-stretch standard error".
  (ii) "a minority ... INDISTINGUISHABLE FROM ZERO at the lowest bands" (`sec:scope`, the struck row's frontier
       summary) -- from `P15_the_bank_already_existed...`, the source `r7033` gated as drawing no noise and whose
       body passage `r7035` corrected.  ⚑ *THIS ONE IS MY MISS: it was in the paper at the `r7033` audit base and
       is not in the `r7033` receipt.*  Honest form: "sign-indefinite at the lowest bands".
  (iii) "the sky's own one-multipole LOCATING WIDTH ... LOCATING NOISE" (`sec:refit-bound`, and "locating
       spread" in `sec:scope`) -- the one- and two-multipole widths are an ASSUMED Gaussian input
       (`rng.normal(0, mult)`); the repository's only covariance-propagated locating uncertainty is the fourth
       peak's, 2.19 multipoles.  Whether the sky's locating noise at the first three peaks is one multipole cannot
       be determined from the repository.
  (iii) "z_acc = 0.6648 +- 0.0467 ... agreement at 0.7 sigma", and "0.704 sigma -> 0.713 sigma"
       (`sec:discussion`) -- the +-0.0467 is stated to come from a DESI DR2 D_M/D_H fit, and every script in the
       repository that carries it takes it as an INPUT; none computes it.  Plausibly a real noise model, not
       reproducible here.

⛔ NOT CLAIMED: that any result is wrong -- every flagged passage describes a real computed quantity, and what is
claimed is only what its instrument supports.  No re-scoring, no physics, no paper prose edited: the enumeration
is the deliverable and every hit is routed to 66.  No other seat's receipt touched.

Written r7037 by node 70.  Stated for reversal.
"""
import glob
import os
import re

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CORPUS = os.path.join(ROOT, 'corpus')
HDR = ' '.join(__doc__.split())
PRE = ' '.join(open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7037_70_corpus_sweep', 'PREDICTION.md'),
                    encoding='utf-8').read().split())
SRC = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}


def src(name):
    return open(SRC[name], encoding='utf-8', errors='replace').read()


# ------------------------------------------------------------------ the instrument: evidence classes in a source's CODE
# `chi2_of(` is the plik_lite likelihood itself, which reads COV_TT -- gated below rather than assumed
EVID = {'COV': r'COV_TT|np\.linalg\.solve\(\s*cov|cho_factor\(\s*cov|\bcov\s*=\s*np\.array|\bchi2_of\(',
        'DRAW': r'standard_normal|default_rng|np\.random\.|multivariate_normal',
        'MEAS': r'sig_obs|np\.sqrt\(\s*sig_th\*\*2\s*\+\s*sig_obs\*\*2\)',
        'CV': r'\(\s*2\s*\*\s*l\s*\+\s*1\s*\)'}


def evidence(name):
    t = src(name)
    return sorted(k for k, v in EVID.items() if re.search(v, t))


def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(re.sub(r'(?<!\\)%.*$', '', ln) for ln in t.split('\n'))
    return re.split(r'\\begin\{thebibliography\}', t)[0]


PAPERS = sorted(os.path.basename(p) for p in glob.glob(os.path.join(CORPUS, '*.tex'))
                if not os.path.basename(p).startswith(('appendix_receipts', 'appendix_')))
BODY = {p: body(os.path.join(CORPUS, p)) for p in PAPERS}
FLAT = {p: ' '.join(t.split()) for p, t in BODY.items()}
STAT = (r'\$\s*[\d.]+\s*(?:\\,|\\;|~)?\s*\\sigma\s*\$|several[- ]\$?\\sigma|\bstandard deviations?\b|'
        r'(?<!\\)\bsigmas?\b(?![-_])|[\d.]\s*\$?\s*\\pm\s*\$?\s*[\d.]|\bnois[ey]|\bsignifican(?:t|ce)\b|'
        r'\bdetect(?:ed|ion|able)\b|\btension\b|\buncertaint|\\chi\^?\{?2|confidence|p-value|'
        r'(?:told|distinguish\w*|differ\w*) from zero|consistent with (?:zero|the data)|\bscatters?\b|cosmic variance')

print('=' * 100)
print('THE SWEEP -- every non-appendix paper, comments and bibliography stripped (REPORTED, not gated)')
print('=' * 100)
for p in PAPERS:
    n = len(re.findall(STAT, BODY[p], re.I))
    bare = len(re.findall(r'\\sigma\b', BODY[p]))
    print(f"    {p:30s} statistical-shape hits {n:4d}   bare \\sigma symbols {bare:4d}")

# ------------------------------------------------------------------ the class (i) groups: source, and its evidence
GROUP_I = [
    ('light elements "within 1 sigma", lithium "6-8 sigma" -- cosmogenesis abstract x2 and its verdict section, '
     'CR_framework x3, CR_cosmology abstract', 'P16_theory_error_and_likelihood', {'MEAS'}),
    ('distance ladder "chi^2/dof ~ 1" against DESI DR2 -- CR_framework, CR_cosmology abstract and conclusion',
     'P15_desi_dr2_confrontation', {'COV'}),
    ('low multipoles "within cosmic variance" -- CR_framework x3, CR_cosmology abstract and conclusion, '
     'and its "~3.4 sigma" in-principle power', 'P15_verify_lowell_likelihood_v2', {'CV'}),
    ('plik_lite chi^2 per bin 1.16 / 2.98 / 2.10 -- CR_framework, CR_synthesis x3',
     'P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and_the_control_is_nearly_camb', {'COV'}),
    ('adiabatic chi^2 206/215 against isocurvature 3.3e5 -- cosmogenesis',
     'P16_the_adiabatic_premise_is_demanded_by_the_data_and_inherited_by_the_construction', {'COV'}),
    ('the damping signature "non-reabsorbable", a residual no tilt removes -- CR_framework x2, CR_synthesis x2, '
     'cosmogenesis, geometric_core, shadow_of_existence', 'P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma',
     {'COV'}),
    ('the redshift-isotropy floor, a predicted rms of a random field against an observed bound -- modern_parallax '
     'x5, CR_synthesis x2, boundary, geometric_core, cosmogenesis',
     'R50_the_long_wavelength_bullet_reverses_for_the_observable_and_the_corner_is_three_parts_per_million', {'DRAW'}),
    ('the fourth peak "0.9 to 1.3 standard deviations" and "1.2 / 2.1" -- CR_cosmology sec:refit-bound, sec:scope',
     'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control',
     {'COV', 'DRAW'}),
    ('the trough depths "five hundredths of a standard deviation ... 1.8" -- CR_cosmology sec:refit-bound',
     'P15_the_contrast_excess_is_symmetric_about_the_envelope_and_the_troughs_are_where_the_sky_measures_it_best',
     {'COV', 'DRAW'}),
    ('the two channels "separate at some twenty-five standard deviations" -- CR_cosmology sec:refit-bound, sec:scope',
     'P15_the_likelihood_sees_the_step_and_separates_the_two_channels_so_the_demonstration_does_not_cover_it', {'COV'}),
]
_LIKF = open(os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'chi2_of_spectrum.py'), encoding='utf-8').read()
_CHI2 = _LIKF[_LIKF.find('def chi2_of('):]
_CHI2 = _CHI2[:_CHI2.find('\ndef ', 10)]
print('\n' + '=' * 100)
print('PART (i) -- THE CLAIMS THAT STAND: each source carries a real noise model in its own code')
print('=' * 100)
check("the likelihood function `chi2_of` counted as COV evidence reads the covariance itself -- checked, not assumed",
      'cov = COV_TT[np.ix_(keep, keep)]' in _CHI2)
for what, name, need in GROUP_I:
    ev = set(evidence(name))
    check(f"(i) {what}", need <= ev, f"`{name[:60]}` carries {sorted(ev)}")
check("⌗ and the MEAS class is what the r7033 drawless test could not see: the nucleosynthesis confrontation draws "
      "nothing and reads no covariance, yet combines published observational errors with a propagated theory error",
      'DRAW' not in evidence('P16_theory_error_and_likelihood') and 'COV' not in evidence('P16_theory_error_and_likelihood')
      and 'Cooke' in src('P16_theory_error_and_likelihood') and 'SIGMA_RATE' in src('P16_theory_error_and_likelihood'))
check("⌗ and the external table of CR_synthesis quotes published measurements with their own errors (Planck, and "
      "later likelihoods), cited rather than computed -- class (i) by citation",
      all(k in FLAT['CR_synthesis.tex'] for k in ('Planck2018VI', 'RosenbergPR4', 'TristramPR4')))

# ------------------------------------------------------------------ the exclusions, each with its reason
print('\n' + '=' * 100)
print('THE EXCLUSIONS -- caught by the patterns and not statistical claims; each reason named (REPORTED)')
print('=' * 100)
EXCL = [('sigma as a group generator / index', r'\\sigma\b'),
        ('chi as a coordinate in a line element', r'\\chi\}?\^\{?2\}?\s*\+|d\\chi\^'),
        ('"tension" in its ordinary sense', r'\btension\b'),
        ('"detected"/"detectable" of an event or historical parallax', r'\bdetect(?:ed|able)\b'),
        ('numerical precision of a check', r'precision of the check|to machine precision'),
        ('quantum minimum-uncertainty product', r'minimum-uncertainty')]
for why, pat in EXCL:
    print(f"    {why:52s} {sum(len(re.findall(pat, BODY[p])) for p in PAPERS):5d}")

# ------------------------------------------------------------------ the class (ii) findings
print('\n' + '=' * 100)
print('PART (ii) -- THREE PASSAGES, ALL IN CR_cosmology, ALL BELOW THE HEADLINE')
print('=' * 100)
NP = 'P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_damping_envelope'
FP = 'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control'
t_np = ' '.join(src(NP).split())
check("(ii)1 \"one standard deviation from the sky\": the intercept's +-0.0099 is the locator's move across seven "
      "parabola windows -- a procedure spread -- in a source that draws no noise and reads no covariance",
      not evidence(NP) and 'seven parabola windows the sky\'s $\\varphi/\\pi$ moves by $\\pm0' in t_np and '0.0099' in t_np, f"evidence {evidence(NP)}")
check("    and the receipt that DID propagate the covariance through the locator says it does not re-open the "
      "intercept, and names the window spread as a procedure spread and not the sky's uncertainty",
      'NOT a re-opening of the phase intercept, the damping envelope, the driving or the refit, a' in src(FP) and 'PROCEDURE' in src(FP)
      and "It is not the sky's uncertainty" in ' '.join(src(FP).split()))
NS = 'P15_no_statistic_this_construction_can_build_resolves_the_two_channels_and_the_phase_step_dies_on_a_matched_width_control'
t_ns = src(NS)
check("(ii)2 \"better than seven standard deviations\": the +-0.000974 is the standard error over disjoint stretches of "
      "the phase difference between two COMPUTED spectra, with no noise anywhere in the source",
      not evidence(NS) and 'DU = np.array([delta_on(' in t_ns and 'np.std(DU, ddof=1)' in t_ns
      and 'phase_of(g, OA' in t_ns and 'phase_of(g, OC' in t_ns, f"evidence {evidence(NS)}")
BK = 'P15_the_bank_already_existed_and_the_doppler_carries_a_growing_minority_of_the_excess'
R7033 = 'P15_the_three_instruments_with_no_noise_model_one_can_be_given_a_floor_and_ten_passages_quote_a_significance_or_share_the_instrument_cannot_bear'
check("(ii)3 \"indistinguishable from zero at the lowest bands\": its source is the one r7033 gated as drawing no "
      "noise, and whose body passage r7035 corrected",
      not evidence(BK) and 'bank_already_existed' in src(R7033), f"evidence {evidence(BK)}")
check("    ⚑ AND IT IS MY OWN MISS: the r7033 enumeration does not carry this phrase -- reported unprompted",
      'indistinguishable from zero' not in src(R7033))

# ------------------------------------------------------------------ the class (iii) findings
print('\n' + '=' * 100)
print('PART (iii) -- TWO HONEST BLANKS')
print('=' * 100)
SP = 'P15_the_sky_phase_fit_and_its_uncertainty'
check("(iii)1 the sky's \"one-multipole locating width\" is an ASSUMED Gaussian input, not a propagated noise model",
      'rng.normal(0, mult, k)' in src(SP) and 'COV_TT' not in src(SP))
check("    and the repository's ONLY covariance-propagated locating uncertainty is the fourth peak's, larger than the "
      "assumed width -- so whether the first three peaks locate to one multipole is not determinable here",
      '2.19 (statistical, from COV_TT)' in src(FP))
CARRY = sorted(os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, '**', '*.py'), recursive=True)
               if '/.git/' not in p and '0.0467' in open(p, encoding='utf-8', errors='replace').read()
               and os.path.basename(p) != os.path.basename(__file__))
ALPHA = os.path.join(ROOT, 'storyboard_receipts', 'ALPHA_three_determinations.py')
check("(iii)2 z_acc's +-0.0467: every script that carries it takes it as an INPUT (\"from DESI DR2 D_M/D_H\"), the "
      "receipt the paper cites for the equation does not carry it, and none computes the fit",
      os.path.exists(ALPHA) and 'INPUT   x0 = 1.6648 +- 0.0467' in open(ALPHA, encoding='utf-8').read()
      and '0.0467' not in src('P03_acceleration_is_slice_curvature')
      and all(('corpus measured' in open(os.path.join(ROOT, c), encoding='utf-8').read()
               or 'INPUT' in open(os.path.join(ROOT, c), encoding='utf-8').read()
               or 'x0 = 1.6648' in open(os.path.join(ROOT, c), encoding='utf-8').read()
               or 'x0=1.6648' in open(os.path.join(ROOT, c), encoding='utf-8').read()) for c in CARRY),
      CARRY)

# ------------------------------------------------------------------ the count that matters to 66
print('\n' + '=' * 100)
print('PART c) -- CLASS (ii) PER PAPER, AND WHERE')
print('=' * 100)
TABLE = [('ii', 'CR_cosmology.tex', 'sec:refit-bound', 'standard deviation from the sky'),
         ('ii', 'CR_cosmology.tex', 'sec:refit-bound', 'better than seven standard'),
         ('ii', 'CR_cosmology.tex', 'sec:scope', 'indistinguishable from zero at the lowest bands'),
         ('iii', 'CR_cosmology.tex', 'sec:refit-bound', "sky's own locating noise"),
         ('iii', 'CR_cosmology.tex', 'sec:discussion', '0.6648 \\pm 0.0467')]
per = {p: sum(1 for c, f, _, _ in TABLE if c == 'ii' and f == p) for p in PAPERS}
print(f"    class (ii) per paper: {{{', '.join(f'{k}: {v}' for k, v in per.items() if v)}}}; every other paper 0")
# ** ⛭ REPAIRED r7208: `len(PAPERS) == 18` asserted the SIZE OF THE CORPUS, a set any seat may add a
#   paper to, and the label's `seventeen` went stale with it.  The content this check needs is that
#   class (ii) is three and that every OTHER paper carries zero -- which is what is asserted now, with
#   the paper count REPORTED instead. **
print(f"    papers swept: {len(PAPERS)} (reported, not asserted -- the corpus may gain one)")
check("⇒ class (ii) is three, in ONE paper, and zero in EVERY other paper swept",
      per.get('CR_cosmology.tex') == 3 and sum(per.values()) == 3
      and all(v == 0 for p, v in per.items() if p != 'CR_cosmology.tex')
      and len(PAPERS) >= 18, per)
check("⇒ *** AND NONE OF THEM, NOR EITHER HONEST BLANK, SITS UNDER AN ABSTRACT OR A CONCLUSION ***",
      all(s not in ('abstract', 'sec:conclusion') for _, _, s, _ in TABLE))
L = BODY['CR_cosmology.tex']
ABS = L[L.find('\\begin{abstract}'):L.find('\\end{abstract}')]
CONC = L[L.find('\\label{sec:conclusion}'):]
for c, f, s, ph in TABLE:
    flat = ' '.join(ph.split())
    i = FLAT[f].find(flat)
    print(f"    [{c:3s}] {s:16s} \"{ph}\" -- still in the paper: {i >= 0}; in abstract: {flat in ' '.join(ABS.split())}; "
          f"in conclusion: {flat in ' '.join(CONC.split())}   (REPORTED, not gated)")

print('\n' + '=' * 100)
print('PART ⛔ -- THE LIMITS, AS WRITTEN AND AS PRE-REGISTERED')
print('=' * 100)
check("the pre-registration came first and fixed the instrument, the verdict rules and gates on source content",
      'committed before the receipt exists' in PRE and 'REPORTED beside each hit, never required' in PRE
      and 'necessary but not sufficient' in PRE)
check("and the header routes every hit, edits no prose, and claims nothing about any result's correctness",
      'every hit is routed to 66' in HDR and 'no paper prose edited' in HDR and 'that any result is wrong' in HDR)

print('\n' + '=' * 100)
if FAILS:
    print(f"VERDICT: {len(FAILS)} CHECK(S) FAILED")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("VERDICT: ALL PASS -- no abstract or conclusion in the corpus rests on an overclaimed sigma; outside")
print("         CR_cosmology there is no class (ii); inside it, three below the headline and two honest blanks.")
