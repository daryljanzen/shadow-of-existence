"""
r7738 (60) -- a cold read of P15's two-mechanism sentence and P5's dihedral core.

Registration: PREDICTION.md beside this file, committed and pushed before a line of this
existed.  r7735's order.

Every arm is an assertion that can FAIL and every arm prints its WITNESS and not only its
verdict (r7722).  Every prose literal is matched on the raw file AND on a whitespace-FLATTENED
copy (G6, bought at r7732 ⓶).  Every extraction prints its own cardinality beside its verdict,
because r7736 ⓷ was a comparison that returned "none changed" from two empty extractions.
"""
import math
import re
import sys

import sympy as sp

ROOT = __import__('pathlib').Path(__file__).resolve().parents[3]
P15 = (ROOT / 'corpus' / 'CR_cosmology.tex').read_text(encoding='utf-8')
P5 = (ROOT / 'corpus' / 'groupoid_paper.tex').read_text(encoding='utf-8')
LEAN = (ROOT / 'computations' / 'formalisation' / 'lean' / 'probes' / 'Groupoid.lean').read_text(encoding='utf-8')
RCPT_PATH = (ROOT / 'receipts' / 'P15_CR_cosmology' /
             ('P15_both_mechanisms_contribute_at_unit_amplitude_and_the_located_step_is_'
              'the_kernels_because_the_source_template_is_flat_in_ell.py'))
RCPT = RCPT_PATH.read_text(encoding='utf-8')


def flat(s):
    """The whitespace-FLATTENED copy: a printed sentence line-wraps, so a literal that is
    absent from the raw file may be present here.  G6."""
    return re.sub(r'\s+', ' ', s)


P15F, P5F, LEANF, RCPTF = flat(P15), flat(P5), flat(LEAN), flat(RCPT)

ARMS = []


def gate(tag, ok, witness):
    ARMS.append((tag, bool(ok), witness))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}\n          {witness}")


# ===================================================================== Ⓐ  THE P15 SENTENCE
STEMS = [
    ('location', "the located transition belongs to the contrast between the arms and not to their sources"),
    ('presence', "That exclusion is about the sources' own ratio, not about their difference once it is projected"),
    ('structure', "But only the projection's contribution is structured in multipole"),
    ('size', "The step's size, by contrast, is in both arms"),
]

_raw = {n: P15.find(s) for n, s in STEMS}
_fl = {n: P15F.find(flat(s)) for n, s in STEMS}
_ord = [_fl[n] for n, _ in STEMS]
gate("Ⓐ① the four stems are present, raw AND flattened, in the printed order",
     all(v >= 0 for v in _fl.values()) and all(v >= 0 for v in _raw.values())
     and _ord == sorted(_ord),
     f"flattened offsets {_fl}; raw found {sum(1 for v in _raw.values() if v >= 0)}/4; "
     f"in order {_ord == sorted(_ord)}")

FIGS = ['1.0076', '1.0035', '97.93', '22.39', '93.6']
_fig = {f: (P15.count(f), RCPT.count(f)) for f in FIGS}
gate("Ⓐ② every figure the sentence prints is carried by the receipt too",
     all(a >= 1 and b >= 1 for a, b in _fig.values()),
     "; ".join(f"{f}: paper x{a}, receipt x{b}" for f, (a, b) in _fig.items()))

_s1 = dict(STEMS)['location']
_s2 = dict(STEMS)['presence']
_s4 = dict(STEMS)['size']
_after2 = P15F[_fl['presence']:_fl['structure']]
gate("Ⓐ③ the four stems PARTITION: location, presence, ℓ-structure, size",
     'located' in _s1 and 'not absent from the step' in _after2
     and 'carr' not in _s2 and 'in both arms' in _s4,
     f"stem1 contains 'located': {'located' in _s1}; stem2's concession is "
     f"'not absent from the step': {'not absent from the step' in _after2}; "
     f"stem2 contains no verb of carriage: {'carr' not in _s2}; stem4 gives the size to both arms")


def says_sources_carry(sentence):
    """Does THIS sentence assert that the sources carry the located step?  It must find a
    source-subject AND a carriage predicate AND a located-step object, and it must not be
    satisfied by a denial.  G4: run on both classes."""
    s = flat(sentence).lower()
    src = any(t in s for t in ('source', 'sources'))
    carry = any(t in s for t in ('carries', 'carry', 'belongs to', 'is in', 'produced by'))
    step = any(t in s for t in ('step', 'transition', 'feature'))
    denied = any(t in s for t in ('not to their sources', 'not absent', 'not about'))
    return src and carry and step and not denied


FABRICATED = [
    "The located transition belongs to the sources and the sources carry the step.",
    "The two arms' sources carry the located transition at the multipole where it falls.",
]
_real_flagged = [n for n, s in STEMS if says_sources_carry(s)]
_fab_flagged = [i for i, s in enumerate(FABRICATED) if says_sources_carry(s)]
gate("Ⓐ④ the classifier, on BOTH classes: 0 of 4 real stems, 2 of 2 fabricated",
     len(_real_flagged) == 0 and len(_fab_flagged) == len(FABRICATED),
     f"real stems read: 4, flagged {len(_real_flagged)} {_real_flagged}; "
     f"fabricated read: {len(FABRICATED)}, flagged {len(_fab_flagged)} {_fab_flagged}")


def pinned(pattern):
    m = re.search(pattern, RCPT)
    if not m:
        raise SystemExit(f"receipt literal not found: {pattern}")
    return float(m.group(1))


# The receipt's own pinned constants, read out of its source so this arm reds if they move.
SH_K = pinned(r"SH\['PRIMARY'\]\[0\] - (0\.\d+)\)")          # rms fraction, kernel template
SH_S = pinned(r"SH\['PRIMARY'\]\[1\] - (0\.\d+)\)")          # rms fraction, source template
RMS_K = pinned(r"SH\['PRIMARY'\]\[2\] - (0\.\d+)\)")         # kernel template rms
RMS_S = pinned(r"SH\['PRIMARY'\]\[3\] - (0\.\d+)\)")         # source template rms
VS_K = pinned(r"VS\['PRIMARY'\]\[0\] - (0\.\d+)\)")          # VARIANCE share, kernel
RATIO = pinned(r"VS\['PRIMARY'\]\[2\] - (3\.\d+)\)")         # rms ratio kernel/source
A_K = pinned(r"_a\['PRIMARY'\]\[0\] - (1\.\d+)\)")
A_S = pinned(r"_a\['PRIMARY'\]\[1\] - (1\.\d+)\)")

# the two kinds the one sentence prints, computed the two ways it could mean
amp_k = A_K * RMS_K * SH_K          # fitted ℓ-structured amplitude, kernel
amp_s = A_S * RMS_S * SH_S          # fitted ℓ-structured amplitude, source
share_amp = amp_k / (amp_k + amp_s)                 # the AMPLITUDE reading
share_var_nocross = RATIO ** 2 / (1 + RATIO ** 2)   # variance, cross-term dropped
share_var = VS_K                                    # the receipt's own, cross-term kept
root_of_var = math.sqrt(VS_K)                       # variance share read back as an amplitude
printed = 93.6

_readings = {'amplitude share': 100 * share_amp,
             'variance share (receipt)': 100 * share_var,
             'variance share, no cross-term': 100 * share_var_nocross,
             'sqrt of the variance share': 100 * root_of_var}
_matches = {k: v for k, v in _readings.items() if abs(v - printed) < 0.05}
gate("⛔ Ⓐ⑤ the three percentages in ONE sentence are NOT the same kind of quantity: "
     "97.93 and 22.39 are AMPLITUDE fractions, 93.6 is a VARIANCE share",
     abs(100 * share_var - printed) < 0.05 and abs(100 * share_amp - printed) > 1.0
     and len(_matches) == 1,
     "; ".join(f"{k} {v:.2f} %" for k, v in _readings.items())
     + f"  ⇒ printed {printed}; readings matching it: {len(_matches)} "
       f"({list(_matches)}); the amplitude reading, which is the kind the SAME sentence's "
       f"other two percentages are computed in, is {100 * share_amp:.1f} % -- "
       f"{printed - 100 * share_amp:+.1f} points from what is printed")

gate("Ⓐ⑤ᵇ and the two fractions beside it ARE amplitude fractions, verified against the "
     "ratio the receipt pins independently",
     abs(amp_k / amp_s - RATIO) < 5e-4,
     f"kernel ℓ-amplitude {amp_k:.6f} / source {amp_s:.6f} = {amp_k / amp_s:.5f} against the "
     f"receipt's own pinned rms ratio {RATIO:.5f}")

_sec = {'1.0195': RCPT.count('1.01952'), '1.0045': RCPT.count('1.00446')}
_names_binning = re.search(r'primary|secondary', P15F[_fl['presence']:_fl['structure']], re.I)
gate("Ⓐ⑥ the two printed amplitudes are ONE binning's, and the sentence does not say which",
     all(v >= 1 for v in _sec.values()) and _names_binning is None,
     f"printed 1.0076/1.0035 = primary ({A_K:.5f}/{A_S:.5f}); the secondary binning carries "
     f"1.01952/1.00446 (receipt hits {_sec}); the sentence names a binning: "
     f"{_names_binning is not None}, while attributing the exclusion to two of them")

# Ⓐ⑦ -- the 0.4642 occurrences, classified into CLAIM and CORRECTION RECORD by the record's
# own marker, never counted together (r7730 ⓶).
#
# ⛔ FIRST RUN'S DEFECT, FIXED HERE AND RECORDED: the window was ONE LINE.  Prose in this
#    repository wraps, so a hit on the second line of a sentence whose marker sits on the first
#    was binned as a surviving claim -- 10 of 16, every one of them spurious, including two in
#    this probe's OWN registration.  That is the r7730 ⓶ family (a reader that cannot see the
#    correction record it is standing in) crossed with the standing precaution that a prose
#    window must be bounded by its own END and never by a count.  The window is now the
#    enclosing BLANK-LINE-DELIMITED BLOCK, and this revision's own files are censused
#    separately rather than silently skipped.
# ⛔ THIRD DEFECT OF THIS SAME READER, AND THE ONE WORTH KEEPING: the discriminator was a
#    GUESSED VOCABULARY.  Two window repairs above both left one hit standing, and the hit was
#    a correction record all along -- its window reads "That figure is not the model's",
#    "overstates ... by about a factor of ten", "imperfect, not incomplete", and not one of
#    CORRECT / supersed / overtak / ⛔ that the marker list hoped for.  The standing precaution
#    is "no summary string guessed", and a marker list IS a guessed summary string; widening it
#    until the last hit flipped would have been padding the gate.
#    ⇒ THE DISCRIMINATOR IS NOW THE RECORD'S OWN CONTENT: a correction record states the
#      superseded figure BESIDE the figure that replaces it.  The replacements are read out of
#      the receipt's own pinned assertions, so this predicate is derived and not written.
SUPERSEDED = '0.4642'
# ⛔ AND THE f-STRING BACKSLASH, FIFTH WINDOW RUNNING: an f-string expression part cannot
#    contain a backslash, and a regex for a bracketed key is all backslashes.  The remedy is
#    always the same -- hoist the expression out of the f-string -- and it is recorded here
#    because the remedy never changes and the mistake keeps being made.
_RP = pinned(r"RES\['PRIMARY'\]\['fitted'\] - (0\.\d+)\)")
_RS = pinned(r"RES\['SECONDARY'\]\['fitted'\] - (0\.\d+)\)")
REPLACEMENT = sorted({format(_RP, '.6f'), format(_RS, '.6f'),
                      format(_RP, '.4f'), format(_RS, '.4f')})


def is_record(window):
    """A record carries the replacement beside the superseded figure; a claim stands alone."""
    return any(r in window for r in REPLACEMENT)


SELF = 'r7738_60_a_cold_read'
_hits, _claims, _records, _own = [], [], [], []
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix not in ('.md', '.tex', '.py', '.tsv') or '.git' in p.parts:
        continue
    try:
        txt = p.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    if '0.4642' not in txt:
        continue
    rel = p.relative_to(ROOT).as_posix()
    for m in re.finditer(r'0\.4642', txt):
        # the enclosing block, bounded by its own blank lines and never by a character count
        lo = txt.rfind('\n\n', 0, m.start())
        lo = 0 if lo < 0 else lo + 2
        hi = txt.find('\n\n', m.end())
        hi = len(txt) if hi < 0 else hi
        block = txt[lo:hi]
        # ⛔ SECOND WINDOW DEFECT, FIXED HERE: a markdown TABLE is its own blank-line block, and
        #    a table ROW IS NOT AN ASSERTION -- the assertion is the sentence that introduces the
        #    table.  r7731's corrected figure survives as the row `| ... r7731's figure,
        #    reproduced | 0.4642 |` whose correction stands in the paragraph above and below it,
        #    so a block window classified it as a live claim.  The rule is structural and not a
        #    token added until the gate passed: a table is a DISPLAY inside a sentence and the
        #    sentence can continue after it, so the window extends over the paragraph on EITHER
        #    side -- the r7732 ⓸ lesson that a reader's window must not end where the thing it
        #    reads begins, taken in both directions.  Its negative control is below and is
        #    exercised on both sides.
        if block and all(l.lstrip().startswith('|') for l in block.splitlines() if l.strip()):
            prev = txt.rfind('\n\n', 0, max(lo - 2, 0))
            nxt = txt.find('\n\n', hi + 2)
            block = txt[0 if prev < 0 else prev + 2: len(txt) if nxt < 0 else nxt]
        rec = (rel, flat(block)[:70])
        _hits.append(rec)
        if SELF in rel:
            _own.append(rec)
        elif is_record(block):
            _records.append(rec)
        else:
            _claims.append(rec)
# the negative control for BOTH window rules (G5): a table row carrying the figure with no
# correcting paragraph before it MUST come back a surviving claim, and one introduced by a
# correction MUST NOT.  Without this the `0 claims` above would mean nothing -- r7736 ⓷.
def classify(doc):
    m = re.search(r'0\.4642', doc)
    lo = doc.rfind('\n\n', 0, m.start())
    lo = 0 if lo < 0 else lo + 2
    hi = doc.find('\n\n', m.end())
    hi = len(doc) if hi < 0 else hi
    block = doc[lo:hi]
    if block and all(l.lstrip().startswith('|') for l in block.splitlines() if l.strip()):
        prev = doc.rfind('\n\n', 0, max(lo - 2, 0))
        nxt = doc.find('\n\n', hi + 2)
        block = doc[0 if prev < 0 else prev + 2: len(doc) if nxt < 0 else nxt]
    return 'record' if is_record(block) else 'claim'


_TBL = "| the ratio | value |\n|---|---|\n| the model's own | `%s` |" % SUPERSEDED
_REPL = REPLACEMENT[0]
NEG = {
    'the figure alone -> claim': ("Some other paragraph entirely.\n\n" + _TBL
                                  + "\n\nAnd a further unrelated paragraph.\n", 'claim'),
    'the replacement BEFORE it -> record': (f"The model's own is {_REPL}.\n\n" + _TBL
                                            + "\n\nAnd a further unrelated paragraph.\n", 'record'),
    'the replacement AFTER it -> record': ("Some other paragraph entirely.\n\n" + _TBL
                                           + f"\n\nThe model's own is {_REPL}.\n", 'record'),
    'a correcting WORD but no replacement -> claim': ("This is CORRECTED and superseded.\n\n" + _TBL
                                                      + "\n\nStill nothing.\n", 'claim'),
}
_ctl = {k: classify(d) for k, (d, _) in NEG.items()}
gate("Ⓐ⑦ᵇ the discriminator is the record's OWN CONTENT and can still FAIL, exercised on both "
     "sides of the display and against a correcting word that carries no replacement (G5)",
     all(_ctl[k] == want for k, (_, want) in NEG.items()),
     "; ".join(f"{k.split(' ->')[0]} -> {_ctl[k]}" for k in NEG)
     + f"  ({len(NEG)} controls, both classes assigned; replacements read from the receipt: "
       f"{REPLACEMENT})")

gate("Ⓐ⑦ the repair that corrected 0.4642 left NO surviving claim (the r7732 ⑤ check)",
     len(_hits) >= 5 and len(_records) >= 5 and len(_claims) == 0,
     f"occurrences read: {len(_hits)} in "
     f"{len({h[0] for h in _hits})} file(s); correction records: {len(_records)}; this "
     f"revision's own files: {len(_own)}; SURVIVING CLAIMS: {len(_claims)} "
     f"{[c[0] for c in _claims]}; and the one that matters, r7731's own VERDICT.md, reads "
     f"{[h[1][:60] for h in _records if 'r7731_cc66' in h[0]]}")

# ===================================================================== Ⓑ  P5's σ SENTENCE
SIGMA_SENT = ("the group permutes the three roots, and $\\sigma$ exchanges two of them, "
              "positive for $w\\in(0,\\pi/3)$, and fixes the third")
_sig_at = P5F.find(flat(SIGMA_SENT))
gate("Ⓑ⓪ the σ sentence is located, raw and flattened",
     _sig_at >= 0 and P5.find(SIGMA_SENT) >= 0,
     f"flattened offset {_sig_at}; raw offset {P5.find(SIGMA_SENT)}; line "
     f"{P5[:P5.find(SIGMA_SENT)].count(chr(10)) + 1}")


def declared(name):
    """Is `name` a DECLARATION in the Lean file, or only a docstring mention?  Classified, and
    both counts printed -- a mention is not a declaration (G5/r7732 ⓹)."""
    decl = re.findall(rf'^(?:noncomputable\s+)?(?:theorem|lemma|def)\s+{re.escape(name)}\b',
                      LEAN, re.M)
    mentions = len(re.findall(rf'`{re.escape(name)}`', LEAN))
    return len(decl), mentions


CITED = sorted(set(re.findall(r'gp\\_((?:\$\\sigma\$|\$\\tau\$|[A-Za-z0-9])(?:\\_|[A-Za-z0-9α-ω])*)',
                              P5)))
def unescape(n):
    return (n.replace('\\_', '_').replace('$\\sigma$', 'σ').replace('$\\tau$', 'τ'))


CITED = ['gp_' + unescape(n) for n in CITED]
_bad = [n for n in CITED if declared(n)[0] == 0]
_absent = declared('gp_not_a_declaration_at_all')
gate("Ⓑ① every gp_ name the paper cites is a DECLARATION in Groupoid.lean, and a name that is "
     "not there is not found (G5)",
     len(CITED) >= 15 and not _bad and _absent == (0, 0),
     f"cited names read: {len(CITED)}; undeclared: {len(_bad)} {_bad}; "
     f"the negative control returns {_absent}; sample {CITED[:4]}")

_sr = re.search(r'theorem gp_σ_roots\s*:(.*?):= by', LEAN, re.S).group(1)
_swap = dict((int(a), int(b)) for a, b in re.findall(r'gp_ψ \(\.sr 0\) (\d) = (\d)', _sr))
_rp = re.search(r'theorem gp_roots_pos\s*(.*?):= by', LEAN, re.S).group(1)
_pos = sorted(int(k) for k in re.findall(r'0 < gp_root w (\d)', _rp))
_moved = sorted(k for k, v in _swap.items() if k != v)
_fixedlab = sorted(k for k, v in _swap.items() if k == v)
gate("Ⓑ② the two labels σ SWAPS are exactly the two gp_roots_pos proves positive",
     _swap == {0: 1, 1: 0, 2: 2} and _pos == _moved == [0, 1] and _fixedlab == [2],
     f"gp_σ_roots reads {_swap} ⇒ moved {_moved}, fixed {_fixedlab}; "
     f"gp_roots_pos establishes positivity for {_pos} (read off the declarations, "
     f"{len(_swap)} label statements and {len(_pos)} positivity conjuncts)")

w = sp.Symbol('w', real=True)
sigma = sp.pi / 3 - w
_img = [sp.nsimplify(sigma.subs(w, v)) for v in (sp.Integer(0), sp.pi / 3)]
_stable = all(0 <= float(x) <= float(sp.pi / 3) for x in _img)
gate("Ⓑ③ the interval (0, π/3) is σ-STABLE, so the exchange stays where positivity is claimed",
     _stable and sp.simplify(sigma.subs(w, sp.pi / 6) - sp.pi / 6) == 0,
     f"σ(w) = π/3 − w maps the closed endpoints to {[str(x) for x in _img]}, so σ((0,π/3)) = "
     f"(0,π/3); its interior fixed point is π/6")

root = lambda k: 2 / sp.sqrt(3) * sp.sin(w + k * 2 * sp.pi / 3)
_r2 = [float(root(2).subs(w, sp.Rational(j, 60) * sp.pi / 3)) for j in range(1, 60)]
gate("Ⓑ④ the third root -- the one σ fixes -- is NEGATIVE throughout (0, π/3), so 'fixes the "
     "third' is not a positivity claim in disguise",
     max(_r2) < 0,
     f"r₂ over 59 interior points: max {max(_r2):.6f}, min {min(_r2):.6f}; "
     f"r₂(π/6) = {float(root(2).subs(w, sp.pi / 6)):.6f}")

r0 = 2 / sp.sqrt(3) * sp.sin(w)
_resid = sp.simplify(sp.expand_trig(sp.simplify(r0 - r0 ** 3)) - 2 / (3 * sp.sqrt(3)) * sp.sin(3 * w))
gate("Ⓑ⑤ the two parametrisations agree IDENTICALLY: 2M = r₀ − r₀³ equals (2/3√3) sin 3w",
     _resid == 0,
     f"symbolic residual {_resid} (sympy {sp.__version__}); and each root solves the cubic: "
     f"max |r³−r+2M| over 3 labels x 7 angles = "
     f"{max(abs(float((root(k) ** 3 - root(k) + 2 / (3 * sp.sqrt(3)) * sp.sin(3 * w)).subs(w, sp.Rational(j, 7) * sp.pi))) for k in range(3) for j in range(1, 8)):.3e}")

# Ⓑ⑥ -- the degeneracy, from the CLOSED FORM.  r7732 ⓷: a grid cannot resolve a near-tangency,
# and `distinct` is exactly the regime in which two roots come arbitrarily close without meeting.
twoM = 2 / (3 * sp.sqrt(3)) * sp.sin(3 * w)
disc = sp.simplify(4 - 27 * twoM ** 2)
_disc_is = sp.simplify(disc - 4 * sp.cos(3 * w) ** 2)
_degen = sp.solveset(sp.Eq(sp.cos(3 * w), 0), w, sp.Interval.open(0, sp.pi / 3))
_degen = sorted(_degen, key=float)
_at = sp.pi / 6
_vals = [sp.simplify(root(k).subs(w, _at)) for k in range(3)]
gate("⛔ Ⓑ⑥ the sentence says 'the three roots', and at w = π/6 -- STRICTLY INSIDE (0, π/3) -- "
     "there are only TWO",
     _disc_is == 0 and len(_degen) == 1 and _degen[0] == _at
     and sp.simplify(_vals[0] - _vals[1]) == 0 and sp.simplify(_vals[0] - _vals[2]) != 0,
     f"disc(r³−r+2M) = 4 − 27(2M)² = 4cos²3w exactly (residual {_disc_is}); it vanishes on the "
     f"open interval at {len(_degen)} point(s), {[str(x) for x in _degen]}; there the roots are "
     f"{[str(v) for v in _vals]} = {[round(float(v), 9) for v in _vals]} -- r₀ = r₁ = 1/√3 -- and "
     f"2M = {sp.simplify(twoM.subs(w, _at))} = the Nariai mass "
     f"{float(sp.simplify(twoM.subs(w, _at))):.12f}")

_fx = P5F.find(flat("the fixed points of $\\sigma$ are machine-checked to be exactly $w=\\pi/6$"))
gate("Ⓑ⑦ the paper's own disclosure of π/6 stands AFTER the sentence, not before it",
     _fx >= 0 and _fx > _sig_at,
     f"σ sentence at flattened offset {_sig_at} (line "
     f"{P5[:P5.find(SIGMA_SENT)].count(chr(10)) + 1}); the gp_σ_fixed paragraph at {_fx} (line "
     f"{P5[:P5.find('the fixed points of $' + chr(92) + 'sigma$ are machine-checked')].count(chr(10)) + 1}) "
     f"-- {_fx - _sig_at} characters later")

# ===================================================================== Ⓒ  THE ANTI-HOMOMORPHISM
_psi_ty = re.search(r'def gp_ψ\s*:\s*(.*?)\s*:=\s*(.*)', LEAN)
_act_mulproof = re.search(r'map_mul\'\s*:=\s*by', LEAN) is not None
gate("Ⓒ① gp_ψ is a MONOID HOMOMORPHISM, machine-checked -- the 'anti' is not a failure of "
     "homomorphy",
     _psi_ty is not None and '→*' in _psi_ty.group(1) and 'gp_act' in _psi_ty.group(2)
     and _act_mulproof,
     f"gp_ψ : {_psi_ty.group(1)} := {_psi_ty.group(2)}; it is built by gp_act, whose map_mul' "
     f"carries a proof: {_act_mulproof}")


# D₃ with Mathlib's law.  Testing homomorphy under this table is a test OF the table, since
# Lean proves map_mul' holds: a wrong table would red Ⓒ②.
def mul(g, h):
    (a, i), (b, j) = g, h
    if a == 'r' and b == 'r':   return ('r', (i + j) % 3)
    if a == 'r' and b == 'sr':  return ('sr', (j - i) % 3)
    if a == 'sr' and b == 'r':  return ('sr', (i + j) % 3)
    return ('r', (j - i) % 3)


D3 = [('r', i) for i in range(3)] + [('sr', i) for i in range(3)]


def psi(sign):
    """gp_act (e) 1 on the labels, with e = sign * id."""
    def f(g):
        a, i = g
        e = (sign * i) % 3
        if a == 'r':
            return tuple((k + e) % 3 for k in range(3))
        return tuple((-k + (1 - e)) % 3 for k in range(3))
    return f


PSI, PSI_PLUS = psi(-1), psi(+1)
_homo = all(tuple(PSI(mul(g, h))[k] for k in range(3))
            == tuple(PSI(g)[PSI(h)[k]] for k in range(3)) for g in D3 for h in D3)
_homo_plus = all(tuple(PSI_PLUS(mul(g, h))[k] for k in range(3))
                 == tuple(PSI_PLUS(g)[PSI_PLUS(h)[k]] for k in range(3)) for g in D3 for h in D3)
gate("Ⓒ①ᵇ and both sign conventions are homomorphisms, over all 36 pairs -- which is also the "
     "check that this table IS Mathlib's",
     _homo and _homo_plus,
     f"pairs tested {len(D3) ** 2}; e = −id homomorphic {_homo}; e = +id homomorphic "
     f"{_homo_plus}; ψ(r 1) = {PSI(('r', 1))} is k ↦ k − 1 while the angle goes w ↦ w + 2π/3")

LIFT = {('r', i): (lambda v, i=i: v + i * 2 * sp.pi / 3) for i in range(3)}
LIFT.update({('sr', i): (lambda v, i=i: -v + (sp.pi / 3 - i * 2 * sp.pi / 3)) for i in range(3)})
_perm_err = []
for g in D3:
    for k in range(3):
        for j in (1, 3, 5):
            v = sp.Rational(j, 11) * sp.pi
            lhs = root(PSI(g)[k]).subs(w, LIFT[g](v))
            rhs = root(k).subs(w, v)
            _perm_err.append(abs(float(sp.N(lhs - rhs, 30))))
_perm_err_plus = []
for g in D3:
    for k in range(3):
        v = sp.Rational(1, 11) * sp.pi
        _perm_err_plus.append(abs(float(sp.N(root(PSI_PLUS(g)[k]).subs(w, LIFT[g](v))
                                             - root(k).subs(w, v), 30))))
gate("Ⓒ② what is 'anti' is the SIGN: e = −id is the convention gp_root_perm's own direction "
     "r_{ψ(g)k}(g·w) = r_k(w) requires, and e = +id does not satisfy it",
     max(_perm_err) < 1e-24 and max(_perm_err_plus) > 1e-3,
     f"e = −id: {len(_perm_err)} (g,k,w) triples, max |lhs−rhs| {max(_perm_err):.3e}; "
     f"e = +id: {len(_perm_err_plus)} triples, max {max(_perm_err_plus):.6f} ⇒ the covariant "
     f"sign does NOT reproduce the theorem")

_agree = [g for g in D3 if PSI(g) == PSI_PLUS(g)]
gate("⛭ Ⓒ③ the sentence is IMMUNE, and exactly measurably so: σ is one of exactly TWO elements "
     "on which the two conventions agree, and the only nontrivial one",
     len(_agree) == 2 and ('r', 0) in _agree and ('sr', 0) in _agree
     and PSI(('sr', 0)) == PSI_PLUS(('sr', 0)) == (1, 0, 2),
     f"elements read {len(D3)}; conventions agree on {len(_agree)} of them, {_agree} = "
     f"{{identity, σ}}; on σ both give {PSI(('sr', 0))} = 0↔1, 2 fixed, which IS gp_σ_roots; "
     f"they differ on {[g for g in D3 if g not in _agree]}")

_tau_root = [s for s in re.split(r'(?<=\.)\s', P5F)
             if ('tau' in s or 'τ' in s) and re.search(r'r_\{?[k0-9]', s)]
gate("Ⓒ④ and the paper makes no τ-labelled root claim -- the one claim the convention would "
     "reach",
     len(_tau_root) == 0,
     f"sentences read {len(re.split(chr(40) + '?<=' + chr(92) + '.' + chr(41) + chr(92) + 's', P5F))}; "
     f"naming both τ and a labelled root: {len(_tau_root)}")

# ===================================================================== the tally
_fail = [t for t, ok, _ in ARMS if not ok]
print(f"\n{len(ARMS)} arms, {len(ARMS) - len(_fail)} PASS, {len(_fail)} FAIL")
if _fail:
    print("FAILING: " + "; ".join(_fail))
sys.exit(0)
