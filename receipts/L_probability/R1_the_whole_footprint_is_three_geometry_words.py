"""R1 — PROBABILITY'S ENTIRE FOOTPRINT IN THIS CORPUS IS THREE WORDS FROM DIFFERENTIAL GEOMETRY.

PROBABILITY / STOCHASTIC FIELD BAKE, probe R1.  The sixth and last of the six.

The order said: "PROBABILITY / STOCHASTIC -- x6 -- thinnest.  A bounce here is a result."
*** It is a bounce, and this receipt is what makes it a result rather than a shrug. ***

** THE FIELD'S OWN VOCABULARY IS ABSENT OUTRIGHT. **
    probability x0 · stochastic x0 · Markov x0 · martingale x0 · Brownian x0 ·
    ensemble average x0
*** The corpus runs CMB likelihood fits and quotes sigma-levels and NEVER WRITES THE WORD
    "PROBABILITY". ***

** AND THE APPARENT FOOTPRINT IS GEOMETRY WEARING STATISTICS' CLOTHES. **
    `variance`  x86 raw -> the string is inside INVARIANCE and COVARIANCE
    `Gaussian`  x20     -> GAUSSIAN CURVATURE, K_G = 1/alpha^2 - M/r^3, in every occurrence
    `covariance` x24    -> GENERAL COVARIANCE.  P08's own TITLE is "Covariance of geometries
                           over the de Sitter substrate"

VERDICTS -- and each can return otherwise, because each asks whether a statistical sense exists:
  1. the field's core vocabulary is absent, term by term.
  2. `Gaussian` is followed by `curvature` in EVERY occurrence -- checked, not assumed.
  3. `covariance` never occurs as a covariance MATRIX or an estimator; it is the geometric
     invariance sense throughout, and P08's title carries it.
  4. `variance` word-bounded survives at x27, and it is COSMIC VARIANCE -- a real statistical
     object, correctly used, and already the statistics-inference bake's.
  5. THE CONTROL: the same machinery run over a word that IS statistical in this corpus
     (`likelihood`) must find it, or the screen is only capable of finding absences.

⛔ THE WRITING SCAR, A FIFTH TIME, AND THIS IS THE LAST FIELD SO IT IS ALSO THE TALLY.
`check_receipts` / `lint_assertions` caught an `expr == True` assertion here after r3608, r3610,
r3614 and r3616.  *** FIVE FIELDS, FIVE CATCHES, ONE GATE. ***  The gate is not too strict; the
habit is real, and the useful record is that an automatic check caught every single instance of a
defect a careful reader kept reproducing.

Written r3618 by node 60, probability bake.  Stated for reversal.
"""
import glob, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
CODE = {'BH_causality_v2':'P01','janzen_circle_v3':'P02','SdS-slicing-curve_v2':'P03',
        'modern_parallax':'P04','groupoid_paper':'P05','shadow_of_existence':'P06',
        'CR_framework':'P07','slicing_operator':'P08','range_paper':'P09',
        'canonical_time':'P10','dynamics_paper':'P11','algebroid_paper':'P12',
        'boundary_paper':'P13','matter_sector_paper':'P14','CR_cosmology':'P15',
        'cosmogenesis_paper':'P16','geometric_core_paper':'p0'}

FAIL = []
def check(label, got, want):
    ok = got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}   got={got!r} want={want!r}")
    if not ok:
        FAIL.append(label)

def body(path):
    # ⛔⛭⛭ AMENDED r3940, AND THE FIX IS THE EXTRACTION RATHER THAN THE PIN.  This receipt asserts
    #   the probability field's core terms are ABSENT from the corpus.  It began failing at
    #   `probability` x3 -- and all three are THIS BAKE'S OWN LANDINGS, not physics prose:
    #   `\ldg{probability}` x2 in P04 (markers naming the probability field-bake LEDGER) and one
    #   `\textsf{probability}` in P07's table of field names.
    #     ⇒ *** A field bake that measures a word's absence must not count the MARKERS ITS OWN
    #         LANDING WROTE.  The corpus still never writes `probability` in its own voice; what it
    #         now does is CITE the ledger by name, which is the bake succeeding, not the absence
    #         ending. ***  D2's r3610 comment names the same hazard for `index` -- "a receipt that
    #     counts the corpus counts its own landings once they are corpus prose".  Second sighting,
    #     and here it is a FALSE POSITIVE rather than an honest drift, so the extraction is fixed.
    #   Marker ARGUMENTS are stripped; the surrounding prose is untouched.
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    t = re.split(r'\\begin\{thebibliography\}', t)[0]
    t = re.sub(r'\\(?:ldg|rcpt|label|ref|cite[a-z]*)\{[^}]*\}', ' ', t)
    t = re.sub(r'\\textsf\{[^}]*\}', ' ', t)
    return re.sub(r'\s+', ' ', t)

BODIES = {}
for p in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
    b = os.path.basename(p)[:-4]
    if b.startswith('appendix_receipts') or b.startswith('appendix_') or b not in CODE:
        continue
    BODIES[CODE[b]] = body(p)

def wcount(term):
    pat = re.compile(r'\b' + term.replace(' ', r'\s+') + r'\w{0,3}\b', re.I)
    return {c: len(pat.findall(t)) for c, t in BODIES.items() if pat.search(t)}

print("=" * 78)
print("R1 — PROBABILITY'S FOOTPRINT IS THREE GEOMETRY WORDS")
print("=" * 78)
print(f"\n  {len(BODIES)} paper bodies, comments / bibliography / generated appendices stripped.")

# --------------------------------------------------------------- VERDICT 1
print("\nVERDICT 1 — THE FIELD'S CORE VOCABULARY, TERM BY TERM.")
absent = ['probability', 'stochastic', 'Markov', 'martingale', 'Brownian',
          'ensemble average', 'Wiener', 'Ito', 'Fokker']
found = {}
for t in absent:
    w = wcount(t)
    found[t] = sum(w.values())
    print(f"    {t:<18} x{found[t]}   {w if w else ''}")
check("every one of the field's core terms is absent", sorted(set(found.values())), [0])
print("    *** The corpus fits CMB likelihoods and quotes sigma-levels and never writes")
print("        'probability'.  That is not a defect; it is a measurement. ***")

# --------------------------------------------------------------- VERDICT 2
print("\nVERDICT 2 — `Gaussian`: is it EVER a distribution?")
GAUSS = re.compile(r'\bGaussian\b(?:\s+|\\?[a-z]*\{?)?(\w+)?', re.I)
after = {}
for c, t in BODIES.items():
    for m in re.finditer(r'\bGaussian\b\s+(\w+)', t, re.I):
        after.setdefault(m.group(1).lower(), []).append(c)
print(f"    the word that FOLLOWS `Gaussian`, every occurrence: "
      f"{ {k: len(v) for k, v in sorted(after.items())} }")
check("`Gaussian` is followed by `curvature` and by nothing else", sorted(after), ['curvature'])
tot_g = sum(len(v) for v in after.values())
print(f"    total: x{tot_g}, all of them Gaussian CURVATURE, K_G = 1/alpha^2 - M/r^3")

# --------------------------------------------------------------- VERDICT 3
print("\nVERDICT 3 — `covariance`: a matrix, or general covariance?")
cov = wcount('covariance')
print(f"    covariance: {cov}  (total x{sum(cov.values())})")
mat = sum(len(re.findall(r'covariance\s+(?:matrix|matrices|estimator)', t, re.I))
          for t in BODIES.values())
geo = sum(len(re.findall(r'covariance\s+of\s+geometr|general\s+covariance|'
                         r'covariance[- ]of[- ]geometries', t, re.I)) for t in BODIES.values())
print(f"    as a covariance MATRIX / estimator : x{mat}")
print(f"    as GENERAL covariance / of geometries: x{geo}")
check("not one covariance matrix in the corpus", mat, 0)
import re as _re
_t = _re.search(r'\\title\{([^}]*)', BODIES['P08'])
title = _t.group(1)[:24] if _t else '(no title found)'
print(f"    P08's title begins: {title!r}")
check("and P08's own TITLE carries the geometric sense", title, 'Covariance of geometries')

# --------------------------------------------------------------- VERDICT 4
print("\nVERDICT 4 — `variance`: what survives the word boundary IS statistical.")
var = wcount('variance')
print(f"    variance word-bounded: {var}  (total x{sum(var.values())})")
cosmic = sum(len(re.findall(r'cosmic[- ]variance', t, re.I)) for t in BODIES.values())
print(f"    of which `cosmic variance`: x{cosmic}")
check("cosmic variance occurs twenty-four times", cosmic, 24)
print("    *** A genuine statistical object, correctly used with an exact cosmic-variance")
print("        likelihood -- and it is the statistics-inference bake's, not this one's. ***")

# --------------------------------------------------------------- VERDICT 5
print("\nVERDICT 5 — THE CONTROL.  A word that IS statistical here must be FOUND.")
print("  If this screen can only report absences it is not a screen, it is a mood.")
lik = wcount('likelihood')
print(f"    likelihood: {lik}  (total x{sum(lik.values())})")
# ** FIFTH `expr == True` IN SIX FIELDS.  Pin the measured value. **
check("the control word is found, and P15 carries twenty-six", lik.get('P15'), 26)
check("and it is the dominant carrier", max(lik, key=lik.get), 'P15')
print("    *** The screen finds a statistical word when there is one.  The absences above")
print("        are absences, not blindness. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  probability, stochastic, Markov, martingale, Brownian and ensemble")
print("  average are all x0.  `Gaussian` is CURVATURE in every occurrence, `covariance` is")
print("  GENERAL covariance and never a matrix, and `variance` x86 raw is mostly the string inside")
print("  INvariance and COvariance.  *** The field's whole apparent footprint is three words from")
print("  differential geometry, and the one real statistical object -- cosmic variance -- belongs")
print("  to a bake that has already been run. ***")
print("=" * 78)
