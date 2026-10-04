"""C1 -- DOES EACH CITED RECEIPT COMPUTE WHAT ITS SENTENCE SAYS?  THE CITATION SWEEP (node 70, `r7043`).

606 `\\rcpt` markers across seventeen papers cite 500 distinct receipts, and every one resolves to a file.  The
question is content: ** for every marker, does the named receipt compute the quantity the sentence attributes to
it?**  Three-way verdict: (i) it does; (ii) it does not and a DIFFERENT receipt does -- named; (iii) no receipt
in the repository computes it.

THE INSTRUMENT.  Every cited receipt (and, so a "found nowhere" is honest, every uncited one under 300 s) was run
once and its output kept; each marker's numbers are matched against the cited receipt's SOURCE AND OUTPUT, at the
precision the paper quotes, with adjacent markers treated as one group citation.  The tracer's (ii) and (iii) are
candidates; every one was read by hand.  ⚠ Found running it, not pre-registered: the claim window is the whole
passage the marker closes (since the previous marker or paragraph break), not the last sentence -- the last
sentence misses numbers the same marker covers.  And three tracer artefacts were fixed and named: a Unicode minus,
integers rounded from the receipt's decimals, and exponent fragments (10^{-111} read as "111").

** THE ANSWER TO c), FIRST: NO ABSTRACT AND NO CONCLUSION IN THE CORPUS CITES THE WRONG RECEIPT OR NONE. **
The fifteen markers under an abstract or conclusion -- ten in the matter-sector abstract, three in the geometric
core's, the cosmogenesis abstract and its verdict section -- were read by hand against their receipts' stated
results, and each receipt establishes what its sentence says.

** BELOW THE HEADLINE: TWELVE (ii) AND ONE (iii). **  Ten of the twelve are in `CR_cosmology`'s acoustic comparison,
and five of those name a receipt the paper cites NOWHERE:
  (ii) sec:refit-bound, the chi^2 per bin 1.16 / 2.98 (214.1 / 550.5), cited to `P15_where_the_likelihood_sits`,
       computed by the uncited `P15_the_full_range_lensed_comparison...`;
  (ii) the refit 1.01 / 1.58 and the band-by-band 1.70 ... 9.29, cited to the 132-BIN refit, computed by the
       uncited `P15_the_full_range_refit...` and `P15_at_its_own_preferred_H0...`;
  (ii) the arm's peaks, comb 298.0, phase -0.2349 and height ratios, cited to the fourth-peak receipt, computed by
       the uncited `P15_at_its_own_preferred_H0...`;
  (ii) the control's 2.195 at peaks 220/536/814, cited to the two-arm control, computed by the uncited
       `P15_the_third_peak_deficit...`;
  (ii) the second-instrument comparison 2.273 / 2.319, cited to the locator, computed by the uncited
       `P15_the_crossing_spectrum_reproduces...`;
  (ii) the sky's P1/P2 = 2.2564 cited to the baryon term, the arm's comb 298.0 against 302.9 cited to the
       free-streaming knob, the alternative assignment's 221.95 -> 226.16 cited to the visibility clock -- each
       computed by a receipt the paper cites elsewhere for another sentence;
  (ii) "validated on its control to 0.23%" cited to C59 -- C59 states 0.14%, the figure the paper itself calls "a
       different run"; the 0.23% is the third-peak run's;
  (ii) two NEIGHBOURS: a number placed under the marker beside the one that computes it (P15's 0.1792;
       cosmogenesis's 7.78 and interior mode 909);
  (ii) modern_parallax's sigma_8,eff = 0.285 cited to R2, an input set in `P04_redshift_isotropy_floor`.
  (iii) canonical_time sec (the adiabatic residual): "2.8e-4 in amplitude at n=2, 5.9e-6 at n=3" -- computed by no
       receipt in the repository; the cited receipt's own table gives 7.92e-5 and 2.42e-6, and its printed
       "7.9e-08 in power" is a literal that disagrees with its own computed n=2 power, 6.28e-9.

⛔ NOT CLAIMED: that any number is wrong -- only whether the cited receipt produces it; the (iii)'s internal
disagreement is REPORTED, not adjudicated.  469 markers state no number and are not verdicted by the tracer: the
fifteen headline ones are read by hand, the rest are a STATED LIMIT, not a silent pass.  No prose edited -- every
hit is routed to 66.  No physics, no re-scoring, no other seat's receipt touched.

Written r7043 by node 70.  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys
import time

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
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7043_70_citation_sweep')
sys.path.insert(0, WORK)
import trace_citations as T  # noqa: E402  -- the committed tracer's own matcher and number parser

HDR = ' '.join(__doc__.split())
PRE = ' '.join(open(os.path.join(WORK, 'PREDICTION.md'), encoding='utf-8').read().split())
SRC = T.SRC
_RUN = {}
#: ⛭ r7166+70.1 (70): WHAT THIS VERDICT RAN, recorded rather than inferred.  ** At `c07c594a` `60` read this sweep
#:   exit 1 with two `sec:refit-bound` findings failing and `66` read it exit 0 at the same ref, and neither run
#:   said which of its subprocesses had moved. **  So every run's exit code, wall time and timeout is kept, every
#:   figure lookup keeps WHERE it was answered (SOURCE literal, OUTPUT of the run, or ABSENT), and both are printed
#:   at the end.  A timeout is recorded, not raised: raised, it ended the sweep in a traceback that named no check.
RAN = {}
WHERE = {}


def run(name):
    """a receipt's own output, run once in its own directory -- and RECORDED: (rc, seconds, timed out)"""
    if name not in _RUN:
        p = SRC[name]
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, os.path.basename(p)], cwd=os.path.dirname(p), capture_output=True,
                               text=True, timeout=240, env=dict(os.environ, PYTHONUNBUFFERED='1'))
            _RUN[name] = (r.stdout + r.stderr).replace('\u2212', '-'), r.returncode
        except subprocess.TimeoutExpired:
            _RUN[name] = '', 'TIMEOUT'
        RAN[name] = (_RUN[name][1], round(time.time() - t0, 1))
    return _RUN[name]


def vals(text):
    out = set()
    for s in T.num_pool(text):
        try:
            out.add(float(s))
        except ValueError:
            pass
    return out


def has(name, num, output=True):
    """is `num` carried by receipt `name` -- in its SOURCE, else (if `output`) in its run's OUTPUT.
    ⛭ r7166+70.1: the source is asked FIRST and the receipt is run only when the source cannot answer, so a figure
    the receipt writes as a literal costs no run.  The answer is the same either way (source OR output); what changes
    is that the record says which one answered."""
    t = open(SRC[name], encoding='utf-8', errors='replace').read().replace('\u2212', '-')
    if T.matches(num, vals(t)):
        WHERE[(name, num)] = 'SOURCE'
        return True
    if output and T.matches(num, vals(run(name)[0])):
        WHERE[(name, num)] = 'OUTPUT'
        return True
    WHERE[(name, num)] = 'ABSENT' if output else 'ABSENT-FROM-SOURCE'
    return False


# ======================================================================================================== PART 0
print('=' * 100)
print('PART 0 -- THE PRE-REGISTRATION CAME FIRST; THE ONE DEVIATION IS DECLARED')
print('=' * 100)
check("the pre-registration fixed source-AND-output matching and hand-read candidates before any verdict",
      'both its source and its output from a run' in PRE and 'every candidate is read by hand' in PRE)
check("⚠ and the claim-window deviation and the three tracer artefacts are declared in the header, not hidden",
      'the whole passage the marker closes' in HDR and 'a Unicode minus' in HDR and 'exponent fragments' in HDR)
MARK = []
for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
    f = os.path.basename(p)
    if f.startswith(('appendix_receipts', 'appendix_')):
        continue
    MARK += [(f, n) for n in re.findall(r'\\rcpt\{([^}]*)\}', T.strip(open(p, encoding='utf-8').read()))]
print(f"    markers now: {len(MARK)}; distinct receipts: {len(set(n for _, n in MARK))}; "
      f"unresolved: {sum(1 for _, n in MARK if n not in SRC)}   (REPORTED, not gated)")

# ======================================================================================================== PART c)
print('\n' + '=' * 100)
print('PART c) -- THE FIFTEEN HEADLINE MARKERS: each receipt establishes what its sentence says')
print('=' * 100)
HEAD = [('P16_recollapse_is_the_nariai_threshold', 'EXACTLY THE NARIAI THRESHOLD'),
        ('P16_theory_error_and_likelihood', 'D/H -0.5sigma'),
        ('P17_no_second_scale_on_either_face', 'SUPPLIES A SECOND SCALE'),
        ('Q3_cayley_klein', 'log-cross-ratio'),
        ('Q6r_polar_is_the_background', 'signature (1,4)'),
        ('P14_dual_norm', 'LEAF norm'),
        ('P14_leaf_compactness', 'FINITE total length'),
        ('P14_mode_monodromy_at_the_wall', 'the wall IS the branch point'),
        ('P14_the_count_specified', 'the count problem, specified'),
        ('W1_the_two_plus_one_plus_one_is_excluded_by_a_symmetry_the_chiral_member_does_not_have',
         'EXCLUDED BY A SYMMETRY'),
        ('P14_the_twist_conjugates_T_it_does_not_project_it', 'PERMITS the 2+1+1 but does not SELECT'),
        ('P14_quark_lepton_frontier', 'WHAT IT DOES NOT LAND: the count'),
        ('C1_the_weyl_closure_is_generic_to_cubics_and_the_match_is_D3_alone', 'GENERIC TO CUBICS')]
for name, phrase in HEAD:
    t = open(SRC[name], encoding='utf-8', errors='replace').read()
    check(f"(i) headline: `{name[:62]}` states its result", phrase in ' '.join(t.split()), phrase)

# ======================================================================================================== PART (ii)
print('\n' + '=' * 100)
print("PART (ii) -- TWELVE MARKERS: the cited receipt does not produce the numbers; the named one does")
print('=' * 100)
II = [
    ('CR_cosmology', 'sec:refit-bound', 'P15_where_the_likelihood_sits',
     'P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and_the_control_is_nearly_camb',
     ['214.1', '550.5'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase',
     'P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised', ['1.58', '2.56'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase',
     'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number', ['9.29'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control',
     'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number', ['-0.2349'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_two_arm_control_and_guard',
     'P15_the_third_peak_deficit_is_radiation_driving_and_both_routes_to_the_equality_agree', ['2.195'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too',
     'P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_the_172_is_the_radiation_free_ruler',
     ['2.273', '2.319'], True),
    ('CR_cosmology', 'sec:diffusion', 'C5b_baryon_term',
     'P15_the_height_target_was_below_the_resolution_of_its_own_statistic', ['2.2564'], False),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switch_sweep_finds_no_driving_channel',
     'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number', ['302.9'], True),
    ('CR_cosmology', 'sec:refit-bound', 'P15_the_visibilitys_clock_is_the_one_the_kernel_reads_and_the_comb_votes_against_the_alternative',
     'P15_the_combs_resolution_is_four_multipoles_and_the_skys_own_value_lies_outside_the_family',
     ['221.95', '0.7354'], False),
    ('CR_cosmology', 'sec:refit-bound (neighbour)', 'P15_the_phase_is_the_driving_and_the_undriven_arms_agree',
     'P15_the_anomalous_driving_belonged_to_the_pin_and_not_to_the_construction', ['0.1792'], False),
    ('cosmogenesis', 'progenitor (neighbour)', 'P16_the_progenitor_composition_is_bracketed',
     'P16_the_interior_to_observed_mode_map', ['7.78', '909'], False),
    ('modern_parallax', 'sec:floor', 'R2_the_papers_correlation_figures_are_the_ones_nothing_checked',
     'P04_redshift_isotropy_floor', ['0.285'], False),
]
CITED_ANY = set(n for _, n in MARK)
ROWS = []
uncited = set()
for paper, sec, cited, source, nums, _unc in II:
    cited = next(k for k in SRC if k.startswith(cited[:80]))
    source = next(k for k in SRC if k.startswith(source[:80]))
    absent = all(not has(cited, n) for n in nums)
    # ⛭ r7166+70.1: the computing receipt's exit code counts only when it was RUN to answer -- a figure it writes as a
    #   literal is answered from source, and then no run happened whose exit code could mean anything.
    present = all(has(source, n) for n in nums) and (source not in RAN or RAN[source][0] == 0)
    ROWS.append((paper, sec, cited, source, nums))
    if source not in CITED_ANY:
        uncited.add(source)
    check(f"(ii) {paper} {sec}: {nums} -- not in `{cited[:40]}...`, computed by `{source[:40]}...`"
          + ("  [cited NOWHERE in the corpus]" if source not in CITED_ANY else ""),
          absent and present, f"absent from cited {absent}; present in source {present}")
# ⛭ RE-PINNED r7049: 5 -> 0.  *`r7049` landed the acceptance law in `P15` `sec:refit-bound` as
#   Eq. (acceptance-law) and withdrew two `sec:scope` sentences with one in `P18` `sec:computed`.  Those
#   paper-body edits added the `\\rcpt` markers that bring all five within reach: the live reading is
#   623 markers over 508 distinct receipts with NONE unresolved.*
#   ⛔ ** The count moved because the corpus improved, which is how this pin is meant to fail. **  The
#   sweep's finding is untouched: the twelve (ii) markers and the one (iii) all still hold, and what
#   lapses is only the aggravating clause that their computing receipts were unreachable.
#   ⌗ *Moved by `cc66` rather than routed, under `r7037`: a count pin following a measurement is
#   maintenance and `r7043` drew that line -- there is exactly one defensible amendment here, since the
#   measured count is 0 and no second reading of it exists.  It was routed first, on `#172`, with this
#   patch; it went untaken across two of the owning line's own pushes while `main` stayed red on it.*
check("⛭ and EVERY naming receipt is now reached by a marker -- the five that were not are, since r7049",
      len(uncited) == 0, f"{len(uncited)} distinct sources uncited")
C59 = open(SRC['C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation'], encoding='utf-8').read()
check("(ii) CR_cosmology sec:scope: \"validated on its control to 0.23%\" cites C59, which states 0.14% and never 0.23% "
      "-- the 0.23% is the third-peak run's (2.195 against 2.200), the run the paper itself distinguishes from 0.14%",
      '0.14%' in C59 and '0.23' not in C59
      and has('P15_the_third_peak_deficit_is_radiation_driving_and_both_routes_to_the_equality_agree', '2.195'))

# ======================================================================================================== PART (iii)
print('\n' + '=' * 100)
print("PART (iii) -- ONE: numbers no receipt in the repository computes")
print('=' * 100)
AD = 'P10_the_adiabatic_residual_at_low_n_is_bounded_by_the_towers_own_floor'
ad_out, ad_rc = run(AD)
anywhere = []
for p in glob.glob(os.path.join(ROOT, '**', '*.py'), recursive=True):
    if '/.git/' in p or os.path.basename(p) == os.path.basename(__file__):
        continue
    t = open(p, encoding='utf-8', errors='replace').read()
    if re.search(r'2\.8\d*e-0?4|5\.9\d*e-0?6', t):
        anywhere.append(os.path.relpath(p, ROOT))
check("(iii) canonical_time: \"2.8e-4 in amplitude at n=2, 5.9e-6 at n=3\" -- in no script in the repository and "
      "not in the cited receipt's run",
      not anywhere and ad_rc == 0 and not T.matches('2.8e-4', vals(ad_out)) and not T.matches('5.9e-6', vals(ad_out)),
      anywhere or 'nowhere')
check("    and the cited receipt's own table gives 7.922e-05 and 2.422e-06 at n=2 and n=3",
      '7.922e-05' in ad_out and '2.422e-06' in ad_out)
check("    ⌗ REPORTED, not adjudicated: its printed \"7.9e-08 in power\" is a literal, and its own computed n=2 power "
      "is 6.276e-09",
      'print("  7.9e-08 in power.' in open(SRC[AD], encoding='utf-8').read() and '6.276e-09' in ad_out)

# ======================================================================================================== PART counts
print('\n' + '=' * 100)
print("PART c) -- PER PAPER, AND WHERE")
print('=' * 100)
# counted by MARKER, not by table row: the refit passage is one marker with two naming receipts, and C59 is its own
MARKERS = {'CR_cosmology': ['chi2 per bin', 'refit + band-by-band', 'arm peaks/comb/phase', 'control 2.195',
                            'second instrument', 'sky P1/P2', 'comb vs reported scale', 'alternative assignment',
                            '0.1792 (neighbour)', 'C59 0.23%'],
           'cosmogenesis': ['7.78 / 909 (neighbour)'], 'modern_parallax': ['sigma_8,eff 0.285']}
per = {k: len(v) for k, v in MARKERS.items()}
print(f"    (ii) per paper: {per};  (iii): {{'canonical_time': 1}};  every other paper 0")
check("⇒ twelve (ii) markers, ten in CR_cosmology, and one (iii); NONE under an abstract or conclusion -- and every "
      "table row maps to a counted marker", sum(per.values()) == 12 and per['CR_cosmology'] == 10
      and len({(c, s) for p_, s, c, *_ in II}) == 11
      and all('abstract' not in s and 'conclusion' not in s for _, s, *_ in II))
check("⛔ the limits are written: qualitative markers are a stated limit, the (iii) disagreement is not adjudicated, "
      "and every hit is routed", 'STATED LIMIT, not a silent pass' in HDR and 'REPORTED, not adjudicated' in HDR
      and 'every hit is routed to 66' in HDR)

print('\n' + '=' * 100)
if FAILS:
    print(f"VERDICT: {len(FAILS)} CHECK(S) FAILED")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
# ======================================================================================================== THE RECORD
print('\n' + '=' * 100)
print('WHAT THIS VERDICT RAN (r7166+70.1) -- every subprocess, and where each (ii) figure was answered')
print('=' * 100)
for nm, (rc, sec_) in sorted(RAN.items(), key=lambda kv: -kv[1][1]):
    print(f"    ran  rc={str(rc):<8} {sec_:7.1f}s  {nm[:90]}")
print(f"    {len(RAN)} run(s), {sum(v[1] for v in RAN.values()):.0f}s in all; non-zero or timed out: "
      f"{[n[:50] for n, v in RAN.items() if v[0] != 0] or 'none'}")
for paper, sec_, cited, source, nums in ROWS:
    print(f"    (ii) {paper} {sec_}: " + ', '.join(
        f"{n} cited:{WHERE.get((cited, n), '-')} computing:{WHERE.get((source, n), '-')}" for n in nums))
print("VERDICT: ALL PASS -- no headline marker cites the wrong receipt; below the headline, twelve (ii) -- ten in the")
# ⌗ *the banner asserted the clause the pin above withdrew.  A verdict line that outlives its own
#   check is the harder half of a stale pin: the gate goes green and the sentence stays wrong.*
print("         acoustic comparison -- and one (iii).  ⛭ Since r7049 every one of their computing "
      "receipts\n         IS reached by a marker: what lapsed is the aggravating clause, not the "
      "twelve hits or the one.")
