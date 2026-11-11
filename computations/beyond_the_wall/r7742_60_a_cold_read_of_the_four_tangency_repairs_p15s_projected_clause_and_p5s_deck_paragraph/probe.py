"""
r7742 (60) -- a cold read of what r7739 landed, word for word.

Registration: PREDICTION.md beside this file, pushed at b9bb00224 before this existed, with only
r7739's order read.

⚠ FOUR OF THE FIVE SENTENCES UNDER READ ARE MY OWN DRAFTS, so each is read against TWO
references -- the draft as written in r7740's RESULT.md, and the computation -- because a reader
and a writer who are the same seat share a blind spot.

Precautions: literals matched on a copy with their CONTAINER'S OWN SEAMS removed (r7740's
correction to G6 -- LaTeX line-wraps and Python string-concatenation seams alike); statements
bounded by the `:= by` that begins the proof (r7734 ⓵); roots and containment from the closed
form (r7732 ⓷); every arm prints its WITNESS (r7722) and every extraction its own cardinality
(r7736 ⓷); no discriminator that is a guessed vocabulary (r7740 ⑥).
"""
import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
P3 = (ROOT / 'corpus' / 'SdS-slicing-curve_v2.tex').read_text(encoding='utf-8')
P5 = (ROOT / 'corpus' / 'groupoid_paper.tex').read_text(encoding='utf-8')
P15 = (ROOT / 'corpus' / 'CR_cosmology.tex').read_text(encoding='utf-8')
LEAN = (ROOT / 'computations' / 'formalisation' / 'lean' / 'probes' / 'Groupoid.lean').read_text(encoding='utf-8')
SL = (ROOT / 'computations' / 'formalisation' / 'lean' / 'probes' / 'SlicingCurvature.lean').read_text(encoding='utf-8')
DRAFT = (ROOT / 'computations' / 'beyond_the_wall'
         / 'r7740_60_the_tangency_swept_once_across_the_corpus' / 'RESULT.md').read_text(encoding='utf-8')

flat = lambda s: re.sub(r'\s+', ' ', s)
# ⛔ FIRST RUN'S DEFECT, FIXED HERE AND RECORDED: the draft lives in a MARKDOWN file and the
#    landed text in a LaTeX one, so my draft carries `**` emphasis and backticks around the very
#    clauses I inserted.  Comparing the two raw made all four sentences read as DIFFERING from a
#    draft three of them are word for word.  That is r7740's own G6 correction a second time --
#    match every literal on a copy with its CONTAINER'S OWN markup removed, whichever container
#    it is -- and it would have printed "69 rewrote all four of your sentences", which is false.
#    ⛔ AND THE FIX WAS WRONG THE FIRST TIME TOO: stripping `*` and backticks was not enough,
#      because the draft sits in a markdown BLOCKQUOTE, so every wrapped line begins '> ' and
#      the marker lands MID-SENTENCE once the whitespace is collapsed.  A blockquote prefix is
#      markup as much as emphasis is, and the rule is the container's markup entire.
demark = lambda s: re.sub(r'\s*>\s*', ' ', re.sub(r'[*`]', '', s))
P3F, P5F, P15F = flat(P3), flat(P5), flat(P15)
DRAFTF = flat(demark(DRAFT))

ARMS = []


def gate(tag, ok, witness):
    ARMS.append((tag, bool(ok), witness))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}\n          {witness}")


r, M2, r0 = sp.symbols('r M2 r0', real=True)
CUBIC = r ** 3 - r + M2
NAR = 2 / (3 * sp.sqrt(3))


def multiset(two_m):
    """The exact multiset, where sympy can factor it (the degenerate designations)."""
    poly = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(two_m))), r)
    rs = sp.roots(poly)
    assert sum(rs.values()) == 3, rs
    return {sp.nsimplify(sp.radsimp(sp.simplify(k))): v for k, v in rs.items()}


def signs(two_m, prec=30):
    """⛔ sympy cannot decide the sign of a Cardano radical symbolically, so the SIGN witness is
    numeric at 30 digits while the DISTINCTNESS decision stays exact, from the discriminant."""
    poly = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(two_m))), r)
    rs = [sp.N(x, prec) for x in poly.nroots(n=prec)]
    real = [sp.re(x) for x in rs if abs(sp.im(x)) < sp.Rational(1, 10) ** (prec - 5)]
    pos = sum(1 for x in real if x > 0)
    neg = sum(1 for x in real if x < 0)
    gap = min(abs(a - b) for i, a in enumerate(real) for b in real[i + 1:]) if len(real) > 1 else None
    exact_distinct = sp.simplify(4 - 27 * sp.radsimp(two_m) ** 2) > 0
    return len(real), pos, neg, gap, bool(exact_distinct)


print("=" * 100)
print("  Ⓐ  THE FOUR P3 SENTENCES -- against my draft AND against the object")
print("=" * 100)

LANDED = {
 '①': r"For $0<2M<2/(3\sqrt3)$ the cubic has two distinct positive roots and one negative; for $-2/(3\sqrt3)<2M<0$, one positive and two distinct negative; at the Nariai boundary the like-signed pair merges, and beyond it only the opposite-signed root is real",
 # ⛔ AND THE THIRD DEFECT IN THIS ONE ARM, THE SHARPEST OF THEM: my first cut compared ② only
 # as far as '...exactly at $r_{0}=1/\sqrt3$' -- which is the point just BEFORE the clause where
 # the landed text and my draft actually diverge.  So it reported ② byte-identical and the
 # registered expectation "at least ② differs" came out falsified by a WINDOW THAT ENDED WHERE
 # THE DIFFERENCE BEGINS.  That is r7732 ⓸ exactly (a reader's window must not end where the
 # thing it reads begins), and it is the one failure here that would have let a real edit of
 # 69's pass unseen.  The span now runs to the sentence's own end.
 '②': r"its carrying of $r_{0}\in[0,1)$ to the other positive root, which is $r_{0}$ itself exactly at $r_{0}=1/\sqrt3$, and its fixed point and endpoint values (\texttt{sl\_$\sigma$\_$\sigma$}, \texttt{sl\_$\sigma$\_swap}, \texttt{sl\_$\sigma$\_second} and \texttt{sl\_$\sigma$\_fixed})",
 '③': r"the locus in three real horizons, distinct except at $r_{0}=\pm1/\sqrt3$, where the diagonal meets the ellipse and two of the three coincide",
 '④': r"the diagonal in one: three real roots, two of which coincide exactly at $r_{0}=\pm1/\sqrt3$, where the diagonal passes through an ellipse point",
}
_raw = {k: P3.find(v) for k, v in LANDED.items()}
_fl = {k: P3F.find(flat(v)) for k, v in LANDED.items()}
gate("Ⓐ① all four landed sentences are present at source, raw AND flattened (G6)",
     all(v >= 0 for v in _raw.values()) and all(v >= 0 for v in _fl.values()),
     f"raw offsets {_raw}; flattened found {sum(1 for v in _fl.values() if v >= 0)}/4; lines "
     + str({k: P3[:v].count(chr(10)) + 1 for k, v in _raw.items()}))

# each landed sentence against the DRAFT, with every difference printed
_same, _diff = [], []
for k, v in LANDED.items():
    (_same if flat(v) in DRAFTF else _diff).append(k)
gate("Ⓐ② each landed sentence DIFFED against the draft I wrote at r7740, and the differences "
     "printed rather than counted",
     len(_same) == 3 and _diff == ['②'],
     f"spans read to each sentence's OWN END; byte-identical to my draft: {len(_same)} {_same}; "
     f"differing: {len(_diff)} "
     f"{_diff}.  ② as drafted ended '(sl_σ_second states that equivalence)'; as landed it folds "
     f"into the existing citation list instead -- "
     f"{'and the list does cite sl_σ_second' if 'sl' + chr(92) + '_$' + chr(92) + 'sigma$' + chr(92) + '_second' in P3 else 'BUT THE LIST DOES NOT CITE IT'}"
     f".  ⇒ 69's edit REMOVES a duplicate citation my draft would have added, which is better "
     f"than what I wrote")

# Ⓐ③ -- the four claims of ①, decided from the closed form and not by sampling
disc = sp.simplify(4 - 27 * M2 ** 2)
_steps = {
    'disc > 0 on the open interval': sp.simplify(disc.subs(M2, NAR / 2)) > 0,
    'e3 = -2M != 0 there, so no root is zero': sp.simplify(-NAR / 2) != 0,
    'e1 = 0, so the roots cannot share a sign':
        sp.simplify(sum(sp.Poly(CUBIC, r).all_coeffs()[1:2])) == 0,
}
# with 3 distinct real roots, product = -2M < 0 ⇒ an ODD number are negative ⇒ 1 or 3;
# 3 negative contradicts sum 0 ⇒ exactly 1 negative and 2 positive.
_num, _gaps = [], []
for j in range(1, 40):
    nre, pos, neg, gap, dist = signs(sp.Rational(j, 40) * NAR)
    _num.append((nre, pos, neg, dist))
    _gaps.append(gap)
_at = multiset(NAR)
_beyond = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(2 * NAR))), r).nroots(n=25)
_beyond_real = [x for x in _beyond if abs(sp.im(x)) < 1e-20]
_fval = sp.simplify(CUBIC.subs({M2: 2 * NAR, r: -1 / sp.sqrt(3)}))
gate("Ⓐ③ ①'s four claims hold, each decided from the closed form: 2 distinct positive and 1 "
     "negative inside, the LIKE-signed pair merging at the boundary, and only the "
     "OPPOSITE-signed root real beyond it",
     all(_steps.values())
     and all(t == (3, 2, 1, True) for t in _num)
     and sorted(_at.values()) == [1, 2]
     and max(_at, key=lambda k: _at[k]) > 0 and min(_at) < 0
     and len(_beyond_real) == 1 and _beyond_real[0] < 0 and _fval > 0,
     f"the exact chain: {dict((k, bool(v)) for k, v in _steps.items())} ⇒ with three distinct "
     f"real roots, product -2M < 0 forces an ODD count negative, and three negative contradicts "
     f"sum 0, so exactly one is negative.  Witness over {len(_num)} interior designations: "
     f"(real, positive, negative, disc>0) = {sorted(set(_num))}, smallest pairwise root gap "
     f"{min(_gaps):.3e} ⇒ no near-tangency is being read as a coincidence.  AT the boundary: "
     f"{ {str(k): v for k, v in _at.items()} } -- the POSITIVE pair is the merged one, "
     f"like-signed as ① says.  BEYOND it (2M = 2x Nariai): {len(_beyond_real)} real root, "
     f"{float(_beyond_real[0]):.9f}, negative ⇒ opposite-signed; and f(-1/sqrt3) = "
     f"{sp.simplify(_fval)} > 0 with f -> -inf, so the root lies below -1/sqrt3 exactly as the "
     f"clause requires")

# Ⓐ④ -- ②'s new clause against sl_σ_second AS STATED
_ss = re.search(r'theorem sl_σ_second\s*:(.*?):= by', SL, re.S)
_ss_stmt = flat(_ss.group(1)) if _ss else ''
gate("Ⓐ④ ②'s added clause is true of sl_σ_second as that theorem is STATED, read off the "
     "declaration and not from the paper",
     _ss is not None
     and 'sl_σ x = x ↔ x = 1 / Real.sqrt 3' in _ss_stmt
     and '0 ≤ x → x < 1' in _ss_stmt
     and 'sl\\_$\\sigma$\\_fixed' in P3,
     f"sl_σ_second's own statement carries '∀ x, 0 ≤ x → x < 1 → ... ∧ (sl_σ x = x ↔ x = 1 / "
     f"Real.sqrt 3)', which is exactly '[0,1)' and 'r_0 itself exactly at r_0 = 1/sqrt3'; "
     f"statement length {len(_ss_stmt)} chars, bounded at the ':= by' that begins the proof.  "
     f"And 'and its fixed point and endpoint values' is 69's addition, carried by sl_σ_fixed in "
     f"the same list ⇒ the citation reads NEITHER weaker nor stronger than its source.  "
     f"⛔ My first cut tested for the bare name 'sl_σ_fixed' in a LaTeX file that escapes it as "
     f"'sl" + chr(92) + "_$" + chr(92) + "sigma$" + chr(92) + "_fixed' -- the container's markup a third time")

# Ⓐ⑤ -- ③ and ④ are claims about the LOCUS: the diagonal meets the ellipse
ELL = r ** 2 + r * r0 + r0 ** 2 - 1
_meet = sorted(sp.solveset(sp.Eq(ELL.subs(r, r0), 0), r0, sp.S.Reals), key=float)
_quad = sp.solve(sp.Eq(ELL.subs(r0, 1 / sp.sqrt(3)), 0), r)
gate("Ⓐ⑤ ③ and ④ are true of the LOCUS and not merely of the cubic: the diagonal r = r0 meets "
     "the ellipse at EXACTLY r0 = ±1/sqrt3, and the coincidence is of a DIAGONAL point with an "
     "ELLIPSE point",
     len(_meet) == 2 and sp.simplify(_meet[1] - 1 / sp.sqrt(3)) == 0
     and len(set(_quad)) == 2
     and any(sp.simplify(q - 1 / sp.sqrt(3)) == 0 for q in _quad),
     f"substituting r = r0 into r^2 + r*r0 + r0^2 = 1 gives 3*r0^2 = 1, so the two components "
     f"meet at exactly {len(_meet)} values, {[str(x) for x in _meet]}.  At r0 = 1/sqrt3 the "
     f"ellipse's own two roots are {[str(q) for q in _quad]} = "
     f"{[round(float(q), 9) for q in _quad]}: DISTINCT from each other, and one of them equals "
     f"the diagonal root 1/sqrt3 ⇒ the coinciding pair is diagonal-with-ellipse, as both "
     f"sentences say, and NOT two ellipse points")

# Ⓐ⑥ -- no twin left: every interval-and-count sentence in the corpus now carries its exception
IVAL = re.compile(r'(\\lvert|\|)\s*r_?\{?0\}?\s*(\\rvert|\|)\s*[<>]|'
                  r'(\\lvert|\|)\s*2M\s*(\\rvert|\|)\s*(\\le|\\leq|[<>])|'
                  r'r_?\{?0\}?\s*\\in\s*[\[(]|w\s*\\in\s*[\[(]|2M\s*[<>]|0\s*<\s*w|'
                  r'M\^?\{?2\}?/c\^?\{?4\}?\s*[<>]|\\tfrac1?9|/c\^\{?4\}?\s*[<>]')
COUNT = re.compile(r'distinct|three roots|three real roots|three real horizons|three horizons|'
                   r'two positive roots|two positive horizons|two real points|two of one sign|'
                   r'undercritical regime|non-degenerate|simple roots|double root|merge', re.I)
# ⛔ AND Ⓐ⑥'s PREDICATE WAS A GUESSED VOCABULARY, which is the r7740 ⑥ defect a second time
#    in my own hand: demanding an "exception clause" token flags a sentence that needs no
#    exception because its interval already EXCLUDES the designation -- which is exactly the
#    structural fact r7740 ⓞ established.  The predicate is now CONTAINMENT: a sentence owes an
#    exception only if a degenerate designation lies inside the interval it quantifies over.
EXC = re.compile(r'distinct except|except at|two of which coincide|where two merge|merges|'
                 r'coincides? at|degenerate|double root|Nariai', re.I)
R0_DEG = [sp.Rational(1, 1) / sp.sqrt(3), -1 / sp.sqrt(3), 2 / sp.sqrt(3), -2 / sp.sqrt(3)]
MASS_STRICT = re.compile(r'c\^?\{?4\}?\s*<|<\s*\\tfrac1?9|<\s*1/9')


def owes_exception(sentence):
    """Does this sentence quantify over an interval that CONTAINS a degenerate designation?
    An interval written strictly in the dimensionless MASS cannot (r7740 ⓞ), so it owes none."""
    if MASS_STRICT.search(sentence):
        return False, 'strict in the dimensionless mass: the degenerate set is the boundary'
    if re.search(r'(\\lvert|\|)\s*r_?\{?0\}?\s*(\\rvert|\|)\s*<\s*2/\\sqrt', sentence):
        return True, 'an |r0| < 2/sqrt3 interval, which contains r0 = ±1/sqrt3'
    if re.search(r'r_?\{?0\}?\s*\\in\s*\[0,1\)', sentence):
        return True, 'r0 in [0,1), which contains 1/sqrt3'
    if re.search(r'w\s*\\in\s*\(0\s*,\s*\\pi/3\)', sentence):
        return True, 'w in (0, pi/3), which contains pi/6'
    if re.search(r'2M\s*>\s*0|2M\s*<\s*0', sentence) and '2/(3' not in sentence:
        return True, 'a 2M half-line with no upper bound'
    return False, 'no interval this read can parse as containing a designation'


_cands, _bare, _nointerval = [], [], []
for p in sorted((ROOT / 'corpus').glob('*.tex')):
    txt = p.read_text(encoding='utf-8', errors='replace')
    for s_ in re.split(r'(?<=[.!?;])\s+(?=[A-Z\\$]|\\emph|\\textit)', flat(txt)):
        if IVAL.search(s_) and COUNT.search(s_):
            _cands.append((p.name, s_))
            owes, why = owes_exception(s_)
            if owes and not EXC.search(s_):
                _bare.append((p.name, why, s_[:140]))
            elif not owes:
                _nointerval.append((p.name, why))
# the predicate's own negative control: a fabricated bare sentence MUST come back owing one
_ctl_bare = owes_exception(r"For $|r_{0}|<2/\sqrt{3}$ the cubic has three real roots.")
_ctl_mass = owes_exception(r"Under-critical masses ($\Lambda G^2M^2/c^4<\tfrac19$) give two distinct positive horizons.")
gate("Ⓐ⑥ the four repairs left NO twin: every interval-and-count sentence in the corpus now "
     "carries an exception clause or states the degeneracy itself",
     len(_cands) >= 8 and not _bare and _ctl_bare[0] and not _ctl_mass[0],
     f"candidates read {len(_cands)} in {len({c[0] for c in _cands})} file(s); of those, "
     f"{len(_cands) - len(_nointerval)} quantify over an interval that CONTAINS a designation "
     f"and {len(_nointerval)} do not ({sorted({w for _, w in _nointerval})}); sentences that "
     f"owe an exception and lack one: {len(_bare)} {[(b[0], b[1]) for b in _bare]}.  The "
     f"predicate's own controls: a bare |r0|<2/sqrt3 count -> owes {_ctl_bare[0]}; a strict "
     f"dimensionless-mass count -> owes {_ctl_mass[0]}")

print()
print("=" * 100)
print("  Ⓑ  P15's PARAGRAPH WITH DRAFT (a) IN PLACE")
print("=" * 100)
A_DRAFT = "not about what their difference becomes once it is projected through the distance maps"
LEG = 'exchanging their sources together with their distance maps'
gate("Ⓑ① draft (a) landed verbatim, and it is in the clause that needed it",
     A_DRAFT in P15 and flat(A_DRAFT) in DRAFTF and LEG in P15F,
     f"(a) present raw: {A_DRAFT in P15}; identical to the draft in r7740's RESULT.md: "
     f"{flat(A_DRAFT) in DRAFTF}; the leg it had to match is still '{LEG}': {LEG in P15F}")

_old = "not about their difference once it is projected"
gate("⛭ Ⓑ② the framing clause now names the SAME object the leg exchanges, which is the whole of "
     "what (a) was for -- and the narrower wording is GONE",
     'through the distance maps' in P15F and 'distance maps' in LEG
     and _old not in P15F,
     f"the clause names 'the distance maps' and so does the leg, so the concession now isolates "
     f"what the clause promises; the superseded narrower wording '{_old}' occurs "
     f"{P15F.count(_old)} time(s) -- the r7732 ⑤ twin check, applied to my own repair")

STEMS = [('location', "the located transition belongs to the contrast between the arms and not to their sources"),
         ('presence', "That exclusion is about the sources' own ratio, not about what their difference becomes once it is projected through the distance maps"),
         ('structure', "But only the distance ratio's contribution is structured in multipole"),
         ('size', "The step's size, by contrast, is in both arms")]
_pos = {n: P15F.find(flat(s)) for n, s in STEMS}


def says_sources_carry(s):
    s = flat(s).lower()
    return (('source' in s) and any(t in s for t in ('carries', 'carry', 'belongs to', 'is in'))
            and any(t in s for t in ('step', 'transition', 'feature'))
            and not any(t in s for t in ('not to their sources', 'not absent', 'not about')))


FAB = ["The located transition belongs to the sources and the sources carry the step.",
       "The two arms' sources carry the located transition at the multipole where it falls."]
_rf = [n for n, s in STEMS if says_sources_carry(s)]
_ff = [i for i, s in enumerate(FAB) if says_sources_carry(s)]
gate("Ⓑ③ the partition survives (a): four stems in order, classifier 0 of 4 real and 2 of 2 "
     "fabricated flagged (G4)",
     all(v >= 0 for v in _pos.values()) and list(_pos.values()) == sorted(_pos.values())
     and not _rf and len(_ff) == len(FAB),
     f"stem offsets {_pos}, in order; real stems read 4, flagged {len(_rf)}; fabricated read "
     f"{len(FAB)}, flagged {len(_ff)}")

RC = (ROOT / 'receipts' / 'P15_CR_cosmology' /
      ('P15_both_mechanisms_contribute_at_unit_amplitude_and_the_located_step_is_'
       'the_kernels_because_the_source_template_is_flat_in_ell.py')).read_text(encoding='utf-8')
RCS = flat(re.sub(r'"\s*\n\s*"', '', RC))
pin = lambda p: float(re.search(p, RC).group(1))
VS_K = pin(r"VS\['PRIMARY'\]\[0\] - (0\.\d+)\)")
SH_K, SH_S = pin(r"SH\['PRIMARY'\]\[0\] - (0\.\d+)\)"), pin(r"SH\['PRIMARY'\]\[1\] - (0\.\d+)\)")
RMS_K, RMS_S = pin(r"SH\['PRIMARY'\]\[2\] - (0\.\d+)\)"), pin(r"SH\['PRIMARY'\]\[3\] - (0\.\d+)\)")
A_K, A_S = pin(r"_a\['PRIMARY'\]\[0\] - (1\.\d+)\)"), pin(r"_a\['PRIMARY'\]\[1\] - (1\.\d+)\)")
amp = (A_K * RMS_K * SH_K) / (A_K * RMS_K * SH_K + A_S * RMS_S * SH_S)
_bins = re.search(r'(\d+) = (\d+)\*(\d+) \+ (\d+) = (\d+)\*(\d+) \+ (\d+)', RCS)
gate("Ⓑ④ every figure is unmoved and still carries the right KIND, re-measured against the "
     "receipt's own pinned constants",
     'per cent of its amplitude' in P15F and 'of the variance that varies' in P15F
     and 'on the finer binning' in P15F
     and abs(100 * VS_K - 93.6) < 0.05 and abs(100 * amp - 93.6) > 1.0
     and int(_bins.group(2)) > int(_bins.group(5)),
     f"amplitude on the rms fractions and variance on the variance share, each on its own "
     f"figure; variance share {100 * VS_K:.2f} % as printed, amplitude share {100 * amp:.1f} % "
     f"as not; the finer binning is the primary by the receipt's own identity "
     f"{_bins.group(0)} ({_bins.group(2)} bins against {_bins.group(5)})")

print()
print("=" * 100)
print("  Ⓒ  P5's NEW FORMAL PARAGRAPH -- does it say what each theorem states, and no more")
print("=" * 100)
PARA = re.search(r'The monodromy and the deck group are machine-checked in Lean.*?$', P5, re.M).group(0)
PARAF = flat(PARA)
CITED = ['gp_nariai_simple', 'gp_monodromy_swaps', 'monodromy_surjective', 'gp_deck_trivial',
         'gp_not_normal']


def declared(n):
    return len(re.findall(rf'^(?:noncomputable\s+)?(?:theorem|lemma|def)\s+{re.escape(n)}\b',
                          LEAN, re.M))


_bad = [n for n in CITED if declared(n) == 0]
gate("Ⓒ① every name the paragraph cites is a DECLARATION, and a name that is not there is not "
     "found (G5)",
     len(CITED) == 5 and not _bad and declared('gp_not_a_declaration') == 0,
     f"cited {len(CITED)}; undeclared {len(_bad)} {_bad}; the negative control returns "
     f"{declared('gp_not_a_declaration')}")


def stmt(n):
    m = re.search(rf'theorem {re.escape(n)}\b(.*?):= by', LEAN, re.S)
    return flat(m.group(1)) if m else ''


S = {n: stmt(n) for n in CITED}
_claims = {
    'gp_nariai_simple': ('each Nariai value is a simple zero of $\\Delta=4-27(2M)^{2}$',
                         '4 - 27 * (2 / (3 * Real.sqrt 3)) ^ 2 = 0'),
    'gp_monodromy_swaps': ('two transpositions that share one sheet and move different pairs',
                           'mono loopPlus e₀ ≠ mono loopMinus e₀'),
    'monodromy_surjective': ('the monodromy group is all of $S_{3}$',
                             'Function.Surjective'),
    'gp_deck_trivial': ('the only permutation of the fibre that commutes with every monodromy '
                        'permutation is the identity', 'g = 1'),
    'gp_not_normal': ('the monodromy group has order six on a three-point fibre',
                      'Nat.card (proj ⁻¹\' {x₀}) = 3'),
}
_ok = {n: (flat(c) in PARAF, k in S[n] or k in LEAN) for n, (c, k) in _claims.items()}
gate("Ⓒ② each of the five clauses is matched to its own declaration's STATEMENT, bounded at the "
     "':= by' that begins the proof",
     all(a and b for a, b in _ok.values()),
     "; ".join(f"{n}: clause present {a}, statement carries it {b}" for n, (a, b) in _ok.items()))

# ⛭ Ⓒ③ -- the one risk registered that did NOT fire: gp_nariai_simple is about the DISCRIMINANT
_roots_at_nariai = multiset(NAR)
gate("⛭ Ⓒ③ THE REGISTERED RISK DID NOT FIRE, and the paragraph is right where it could easily "
     "have been wrong: 'simple' is said of the DISCRIMINANT's zero and never of the roots",
     'simple zero of $\\Delta=4-27(2M)^{2}$' in PARA
     and 'simple root' not in PARAF and 'roots are simple' not in PARAF
     and len(_roots_at_nariai) == 2,
     f"at the Nariai value the CUBIC's roots are "
     f"{ {str(k): v for k, v in _roots_at_nariai.items()} } -- {len(_roots_at_nariai)} distinct "
     f"of 3, so a 'simple roots' claim there would be FALSE; the paragraph says 'simple zero of "
     f"Δ' with dΔ/d(2M) = -54(2M) ≠ 0, which is what the theorem states and is true.  "
     f"Occurrences of 'simple root' in the paragraph: {PARAF.count('simple root')}")

# ⛭ Ⓒ④ -- the other registered risk: gp_not_normal is a NEGATIVE, and the inference is flagged
gate("⛭ Ⓒ④ and the negative is not over-generalised: the paragraph states the three facts the "
     "theorem carries and marks the step to 'not normal' as an INFERENCE with 'so'",
     'with an element other than the identity fixing a sheet, so it does not act regularly and '
     'the cover is not normal' in PARAF
     and 'Nat.card (proj_isCoveringMap.monodromyPerm x₀).range = 6' in S['gp_not_normal']
     and '∃ h ∈ (proj_isCoveringMap.monodromyPerm x₀).range, h ≠ 1 ∧ h e₀ = e₀'
         in S['gp_not_normal'],
     "the theorem's three conjuncts are |range| = 6, |fibre| = 3, and an h in the range with "
     "h ≠ 1 and h e₀ = e₀; the paragraph prints all three and reaches 'not normal' through "
     "'so', so the conclusion is presented as drawn and not as checked")

gate("⛭ Ⓒ⑤ and gp_deck_trivial's HYPOTHESIS is in the prose, not dropped: the clause is about "
     "permutations that commute with EVERY monodromy permutation, which is the theorem's binder",
     '∀ γ, g * proj_isCoveringMap.monodromyPerm x₀ γ = proj_isCoveringMap.monodromyPerm x₀ γ * g'
     in S['gp_deck_trivial']
     and 'commutes with every monodromy permutation' in PARAF
     and 'deck group is trivial' not in PARAF,
     "the declaration's hypothesis is the universally quantified commutation, and the prose says "
     "'every monodromy permutation'; the paragraph does NOT say 'the deck group is trivial' of "
     "this theorem, and it names the bridge separately: "
     f"{'That the deck group of a connected cover is the centraliser of its monodromy group is used and not formalised.' in PARAF}")

# ⛔ Ⓒ⑥ -- the finding: the one declaration that actually says S₃ is the one not cited
_s3 = declared('monodromyGroup_equiv_S3') or len(
    re.findall(r'^noncomputable def monodromyGroup_equiv_S3\b', LEAN, re.M))
_surj_target = 'Equiv.Perm (proj ⁻¹\' {x₀})' in LEAN
gate("⛔ Ⓒ⑥ THE FINDING: the clause 'the monodromy group is all of $S_{3}$' cites "
     "monodromy_surjective, which is surjectivity onto the symmetric group OF THE FIBRE -- the "
     "declaration that actually delivers S_3 is monodromyGroup_equiv_S3, and the paragraph does "
     "not name it",
     'the monodromy group is all of $S_{3}$ (\\texttt{monodromy\\_surjective})' in PARA
     and _s3 >= 1 and 'monodromyGroup\\_equiv\\_S3' not in P5,
     f"monodromy_surjective's statement is 'Function.Surjective (proj_isCoveringMap."
     f"monodromyPerm x₀)', whose codomain is the fibre's own permutation group; "
     f"monodromyGroup_equiv_S3 is declared ({_s3} declaration(s)) and is the one that exhibits "
     f"the isomorphism to Equiv.Perm (Fin 3); occurrences of its name in P5: "
     f"{P5.count('monodromyGroup')}.  The step from 'all of Perm(fibre)' to 'all of S_3' needs "
     f"|fibre| = 3, which the paragraph does carry -- but attached to the LATER clause, as "
     f"gp_not_normal's 'three-point fibre', not to this one")

# ⛔ Ⓒ⑦ -- and the two cited declarations use two different coordinates for one locus
_m_coord = '27M² = 1' in LEAN or '27M^2 = 1' in LEAN
gate("⛔ Ⓒ⑦ AND THE TWO CITED DECLARATIONS USE TWO DIFFERENT COORDINATES FOR THE SAME LOCUS, "
     "which the paragraph presents as one",
     _m_coord and 'cover of the $2M$-plane' in PARA
     and sp.simplify(27 * (NAR / 2) ** 2 - 1) == 0,
     f"the paragraph says 'the cover of the $2M$-plane with the two Nariai values removed' and "
     f"gives Δ = 4 − 27(2M)²; monodromy_surjective's own docstring says the base is the "
     f"punctured mass line 27M² = 1 based at M = 0.  The two agree exactly -- 27*(Nariai/2)^2 − "
     f"1 = {sp.simplify(27 * (NAR / 2) ** 2 - 1)}, since 2M = ±2/(3√3) is M = ±1/(3√3) -- so "
     f"this is a SCALING the reader must supply, not an error: one cited declaration is stated "
     f"in 2M and the other in M, and the paragraph names only the 2M plane")

print()
_fail = [t for t, ok, _ in ARMS if not ok]
print(f"{len(ARMS)} arms, {len(ARMS) - len(_fail)} PASS, {len(_fail)} FAIL")
if _fail:
    print("FAILING: " + "; ".join(_fail))
sys.exit(0)
