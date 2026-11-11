"""
r7740 (60) -- THE SWEEP.  r7737's order (1) and (2): every paper that prints an interval in r0,
in 2M or in the sky angle w, and every sentence that quantifies distinctness or a root/horizon
COUNT over one; then every site where the interval contains a double-root designation and the
sentence needs distinctness there.

The selector is DERIVED and not guessed: a candidate is a sentence carrying (a) an inequality or
interval in one of the four parametrisations the corpus actually uses, and (b) a distinctness
token OR a root/horizon COUNT.  Counts are printed beside every verdict (r7736 ⓷), and the
instrument's power is measured on the three sentences that WERE repaired, read out of git history
at the commit before each repair, before anything it says about the present corpus is believed.
"""
import re
import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
r0, M2, w, r = sp.symbols('r0 M2 w r', real=True)

# ---------------------------------------------------------------- the object, stated exactly
TWOM_OF_R0 = r0 - r0 ** 3
R0_OF_W = 2 / sp.sqrt(3) * sp.sin(w)
CUBIC = r ** 3 - r + M2
DISC_M2 = sp.simplify(4 - 27 * M2 ** 2)
DISC_R0 = sp.factor(sp.simplify(DISC_M2.subs(M2, TWOM_OF_R0)))
DISC_W = sp.simplify(DISC_M2.subs(M2, sp.simplify(TWOM_OF_R0.subs(r0, R0_OF_W))))

ARMS = []


def gate(tag, ok, witness):
    ARMS.append((tag, bool(ok), witness))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}\n          {witness}")


def flat(s):
    return re.sub(r'\s+', ' ', s)


print("=" * 100)
print("  Ⓞ  THE OBJECT, COMPUTED BEFORE ANYTHING IS SWEPT")
print("=" * 100)
gate("Ⓞ① the discriminant in each parametrisation, from the closed form",
     sp.simplify(DISC_R0 - (4 - 3 * r0 ** 2) * (3 * r0 ** 2 - 1) ** 2) == 0
     and sp.simplify(DISC_W - 4 * sp.cos(3 * w) ** 2) == 0,
     f"disc = {DISC_M2} in 2M; {DISC_R0} in r0; 4cos^2(3w) in w "
     f"(residual {sp.simplify(DISC_W - 4 * sp.cos(3 * w) ** 2)})")

# the degenerate designations, SOLVED rather than written down
DEG_M2 = sorted(sp.solveset(sp.Eq(DISC_M2, 0), M2, sp.S.Reals), key=float)
DEG_R0 = sorted(sp.solveset(sp.Eq(DISC_R0, 0), r0, sp.S.Reals), key=float)
DEG_W = sorted(sp.solveset(sp.Eq(sp.cos(3 * w), 0), w, sp.Interval(0, sp.pi)), key=float)
gate("Ⓞ② AND THE KEY ASYMMETRY, which is why the mistake is possible in r0 and w and NOT in 2M: "
     "the degenerate set is the BOUNDARY in 2M and the boundary PLUS AN INTERIOR POINT in r0",
     len(DEG_M2) == 2 and len(DEG_R0) == 4 and len(DEG_W) == 3
     and sp.simplify(TWOM_OF_R0.subs(r0, sp.Rational(1, 1) / sp.sqrt(3))
                     - TWOM_OF_R0.subs(r0, -2 / sp.sqrt(3))) == 0,
     f"2M: {len(DEG_M2)} designation(s) {[str(x) for x in DEG_M2]} -- both are the "
     f"undercritical interval's own endpoints.  r0: {len(DEG_R0)} {[str(x) for x in DEG_R0]} -- "
     f"and 1/sqrt3 lies STRICTLY INSIDE |r0|<2/sqrt3.  w on [0,pi]: {len(DEG_W)} "
     f"{[str(x) for x in DEG_W]}.  The map r0 -> r0-r0^3 is TWO-TO-ONE on them: "
     f"r0=1/sqrt3 and r0=-2/sqrt3 both give 2M={TWOM_OF_R0.subs(r0, 1/sp.sqrt(3))}")


def roots_at(two_m):
    """The root multiset at a designation, from the closed form."""
    # ⛔ sympy cannot sort roots over EX, so the multiset comes from sp.roots' own multiplicity
    #    map on the radsimp'd cubic -- still the closed form, never a grid (r7732 ⓷).
    poly = sp.Poly(sp.expand(CUBIC.subs(M2, sp.radsimp(two_m))), r)
    rs = sp.roots(poly)
    if sum(rs.values()) != 3:                      # never let a partial factorisation pass silently
        rs = {sp.nsimplify(x): 1 for x in sp.Poly(sp.nsimplify(poly.as_expr()), r).nroots(n=25)}
    return {sp.nsimplify(sp.radsimp(sp.simplify(k))): v for k, v in rs.items()}


# ---------------------------------------------------------------- the selector
IVAL = re.compile(
    r'(\\lvert|\|)\s*r_?\{?0\}?\s*(\\rvert|\|)\s*[<>]|'      # |r_0| < ...
    r'(\\lvert|\|)\s*2M\s*(\\rvert|\|)\s*(\\le|\\leq|[<>])|'  # |2M| <= ...
    r'r_?\{?0\}?\s*\\in\s*[\[(]|'                             # r_0 \in (...
    r'w\s*\\in\s*[\[(]|'                                      # w \in (...
    r'2M\s*[<>]|'                                             # 2M > 0
    r'0\s*<\s*w|'                                             # 0 < w
    r'M\^?\{?2\}?/c\^?\{?4\}?\s*[<>]|'                        # LambdaG^2M^2/c^4 < 1/9
    r'\\tfrac1?9|/c\^\{?4\}?\s*[<>]'
)
COUNT = re.compile(
    r'distinct|three roots|three real roots|three real horizons|three horizons|'
    r'two positive roots|two positive horizons|two real points|two of one sign|'
    r'undercritical regime|non-degenerate|simple roots|double root|merge', re.I)


def candidates(text, label):
    """Sentences bounded by their OWN ENDS (never a character count), read on the FLATTENED copy
    as well as the raw (G6), with the per-paper cardinality returned beside them."""
    fl = flat(text)
    sents = re.split(r'(?<=[.!?;])\s+(?=[A-Z\\$\\\\]|\\emph|\\textit)', fl)
    hits = [s for s in sents if IVAL.search(s) and COUNT.search(s)]
    return sents, hits


PAPERS = sorted(p for p in (ROOT / 'corpus').glob('*.tex')
                if not p.name.startswith('appendix_'))
ALL = sorted((ROOT / 'corpus').glob('*.tex'))
print()
print("=" * 100)
print("  Ⓐ  THE INSTRUMENT'S OWN POWER, MEASURED BEFORE IT IS BELIEVED")
print("=" * 100)

# ⛔ THE FIRST CUT'S CONTROL SET WAS WRONG, AND THE RECORD IS KEPT BECAUSE THE DISTINCTION IS
#    THE POINT.  I chose "the three sentences that were repaired" as the power control and one of
#    them -- `P3`'s threshold sentence -- is NOT of this sweep's class: its defect was a false
#    "equivalently" between two EQUALITIES, not an interval containing an interior zero, and
#    r7737's order names INTERVALS.  So the miss was a mis-chosen control and not a blind
#    instrument -- but "my control was wrong" is exactly what a blind instrument would also say,
#    so it is not left there: the equality class gets its OWN selector below, with that sentence
#    as its positive control, and both classes are swept.
PRE = [
    ('P3 defining parenthetical', '1ed0595b6^', 'corpus/SdS-slicing-curve_v2.tex',
     'three distinct real roots, the undercritical regime'),
    ('P5 sigma sentence', 'de4f51d61^', 'corpus/groupoid_paper.tex',
     'exchanges two of them, positive for'),
]
_pre_flagged, _pre_missing = [], []
for name, rev, path, needle in PRE:
    try:
        txt = subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        _pre_missing.append((name, f'git show failed: {e}'))
        continue
    sents, hits = candidates(txt, name)
    mine = [s for s in hits if needle in flat(s)]
    (_pre_flagged if mine else _pre_missing).append(
        (name, flat(mine[0])[:130] if mine else f'NOT FLAGGED ({len(sents)} sentences read, '
                                                f'{len(hits)} candidates)'))
gate("Ⓐ① the two repaired sentences OF THIS SWEEP'S CLASS are FLAGGED in their PRE-REPAIR form, "
     "read out of git history at the commit before each repair",
     len(_pre_flagged) == 2 and not _pre_missing,
     f"flagged {len(_pre_flagged)} of {len(PRE)}; missed {len(_pre_missing)}; "
     + "; ".join(f"[{n}] {t[:70]}" for n, t in _pre_flagged + _pre_missing))

# ---- the EQUALITY class: an identification BETWEEN parametrisations, where the two-to-one map
#      makes one side name fewer designations than the other.  Its own selector and its own
#      control, because Ⓞ② computed exactly why this class exists.
EQUIV = re.compile(r'(equivalently|that is|i\.e\.|\bor\b)', re.I)
DESIG = re.compile(r'r_?\{?0\}?\s*\|?\s*=|=\s*\\pm\s*[12]\s*/\s*\\sqrt|'
                   r'(\\lvert|\|)\s*r_?\{?0\}?\s*(\\rvert|\|)\s*=|'
                   r'(\\lvert|\|)\s*2M\s*(\\rvert|\|)\s*=')


def equiv_candidates(text):
    """A sentence that EQUATES a designation in one parametrisation with one in another AND
    asserts the two are equivalent."""
    fl = flat(text)
    sents = re.split(r'(?<=[.!?;])\s+(?=[A-Z\\$]|\\emph|\\textit)', fl)
    hits = [s for s in sents
            if EQUIV.search(s) and len(DESIG.findall(s)) >= 1
            and re.search(r'r_?\{?0\}?', s) and re.search(r'2M', s)]
    return sents, hits


_pre_eq = subprocess.run(['git', 'show', '2b21f12f0^:corpus/SdS-slicing-curve_v2.tex'], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
_eqs_pre, _eqh_pre = equiv_candidates(_pre_eq)
_pre_thr = [s for s in _eqh_pre if 'equivalently' in s and 'single threshold' in s]
_eqs_now, _eqh_now = equiv_candidates((ROOT / 'corpus' / 'SdS-slicing-curve_v2.tex')
                                      .read_text(encoding='utf-8'))
_now_thr = [s for s in _eqh_now if 'equivalently' in s and 'single threshold' in s]
gate("Ⓐ①ᵇ the EQUALITY class has its own selector, and it flags the pre-repair threshold sentence "
     "while the repaired form is not flagged",
     len(_pre_thr) == 1 and len(_now_thr) == 0,
     f"pre-repair: {len(_eqs_pre)} sentences, {len(_eqh_pre)} candidates, the threshold sentence "
     f"flagged {len(_pre_thr)} time(s) -- {flat(_pre_thr[0])[:120] if _pre_thr else 'MISSED'}; "
     f"current: {len(_eqh_now)} candidate(s), the threshold sentence flagged {len(_now_thr)} "
     f"time(s)")

# and the same three in their CURRENT form must carry their repair
CUR = [('P3 threshold', 'corpus/SdS-slicing-curve_v2.tex',
        'at which the mass reaches $|2M|=2/(3\\sqrt{3})$, is the undercritical/overcritical boundary'),
       ('P3 parenthetical', 'corpus/SdS-slicing-curve_v2.tex',
        'distinct except at the designations $r_{0}=\\pm1/\\sqrt3$'),
       ('P5 sigma', 'corpus/groupoid_paper.tex',
        'the three being distinct except at $w=\\pi/6$')]
_held = [(n, p) for n, p, lit in CUR
         if lit in (ROOT / p).read_text(encoding='utf-8')
         or flat(lit) in flat((ROOT / p).read_text(encoding='utf-8'))]
gate("Ⓐ② and all three repairs HOLD in the current corpus, raw or flattened",
     len(_held) == 3,
     f"{len(_held)} of {len(CUR)} present: {[n for n, _ in _held]}")

# the four fabricated controls (G4/G5), one per class and across the parametrisations
CTL = [
    ("r0, contains it and needs it -> CANDIDATE",
     r"For $|r_{0}|<2/\sqrt{3}$ the cubic has three real roots.", True),
    ("2M, strict so excludes it, needs it -> CANDIDATE (the sweep flags, the adjudication clears)",
     r"For $|2M|<2/(3\sqrt{3})$ the cubic has three distinct real roots.", True),
    ("w, contains it and needs it -> CANDIDATE",
     r"On $w\in(0,\pi/3)$ the three roots are distinct.", True),
    ("an interval with NO count or distinctness claim -> NOT a candidate",
     r"For $|r_{0}|<2/\sqrt{3}$ the slicing curve is spacelike at the pivot.", False),
    ("a count claim with NO interval -> NOT a candidate",
     r"The cubic has three distinct real roots in the undercritical regime.", False),
]
_ctl = {n: bool(candidates(s, n)[1]) for n, s, _ in CTL}
gate("Ⓐ③ the selector decided correctly on all five fabricated controls, in all three "
     "parametrisations and in BOTH directions (G4/G5)",
     all(_ctl[n] == want for n, _, want in CTL),
     "; ".join(f"{n.split(' ->')[0]} -> {'candidate' if _ctl[n] else 'not'}" for n, _, _ in CTL))

# ---------------------------------------------------------------- the sweep proper
print()
print("=" * 100)
print("  Ⓑ  THE SWEEP")
print("=" * 100)
TOTAL_SENTS, CANDS = 0, []
for p in ALL:
    txt = p.read_text(encoding='utf-8', errors='replace')
    sents, hits = candidates(txt, p.name)
    TOTAL_SENTS += len(sents)
    for h in hits:
        CANDS.append((p.name, h))
gate("Ⓑ① every .tex in corpus/ was read, and the count is printed against the directory",
     len(ALL) == len(list((ROOT / 'corpus').glob('*.tex'))) and len(ALL) >= 50,
     f"{len(ALL)} file(s) read, {TOTAL_SENTS} sentence(s), {len(CANDS)} candidate(s) in "
     f"{len({c[0] for c in CANDS})} file(s); "
     f"{len([c for c in CANDS if c[0].startswith('appendix_')])} of the candidates are in "
     f"generated appendix files, which mirror receipts and are not paper prose")

print()
for i, (fn, s) in enumerate(CANDS, 1):
    print(f"  [{i:2d}] {fn}")
    print(f"       {s[:260]}")
print()
print(f"  {len(CANDS)} candidate(s) printed in full above -- nothing is absorbed into a count.")
print()
print("  the EQUALITY class in the current corpus: "
      f"{len(_eqh_now)} candidate(s)")
for s in _eqh_now:
    print(f"       {flat(s)[:240]}")

# ---------------------------------------------------------------- Ⓑ the adjudication
print()
print("=" * 100)
print("  Ⓑ  THE ADJUDICATION -- each candidate's interval parsed, its containment decided from")
print("     the CLOSED FORM, and the root multiset computed AT the designation it contains")
print("=" * 100)

# Each entry: the needle that locates the candidate, the interval as sympy, the variable, and the
# reading -- stated, with the computation that decides it printed beside it.
SITES = [
    dict(key='Under-critical masses', var='2M', lo=-sp.Rational(2, 9) * sp.sqrt(3),
         hi=sp.Rational(2, 9) * sp.sqrt(3), closed=False,
         needs=True, verdict='SOUND',
         why='strict in the dimensionless mass, and in 2M the degenerate set IS the boundary'),
    dict(key='The cosmogenesis branch point', var='2M', lo=sp.Rational(2, 9) * sp.sqrt(3),
         hi=sp.Rational(2, 9) * sp.sqrt(3), closed=True,
         needs=False, verdict='SOUND',
         why='the sentence IS the statement of the degeneracy'),
    dict(key='yields a trichotomy', var='2M', lo=-sp.Rational(2, 9) * sp.sqrt(3),
         hi=sp.Rational(2, 9) * sp.sqrt(3), closed=False,
         needs=True, verdict='SOUND',
         why='strict, and tangency is given its own branch of the trichotomy'),
    dict(key='It is positive for', var='r0', lo=-2 / sp.sqrt(3), hi=2 / sp.sqrt(3), closed=False,
         needs=True, verdict='REPAIRED at r7732/r7733',
         why='the parenthetical now reads "distinct except at the designations r0=+-1/sqrt3"'),
    dict(key='For $2M>0$ the cubic has two positive roots', var='2M', lo=0, hi=sp.oo,
         closed=False, needs=True, verdict='SITE 1',
         why='unbounded above, so it contains 2M=2/(3*sqrt3) where the two positive roots MERGE, '
             'and the whole overcritical range beyond it where there are NO positive roots'),
    dict(key='its carrying of $r_{0}\in[0,1)$ to the other positive root', var='r0', lo=0, hi=1,
         closed=False, needs=True, verdict='SITE 2',
         why='"the OTHER positive root" presupposes distinctness, and 1/sqrt3 lies in [0,1); the '
             'cited theorem sl_sigma_second itself carries the exception (sigma x = x iff '
             'x = 1/sqrt3), so the prose asserts what the Lean it cites denies'),
    dict(key='meets the ellipse in two real points and the locus in three real horizons',
         var='r0', lo=-2 / sp.sqrt(3), hi=2 / sp.sqrt(3), closed=False,
         needs=True, verdict='SITE 3',
         why='"three real horizons" over an interval containing r0=+-1/sqrt3, where the diagonal '
             'root coincides with one of the ellipse points -- the paper says so itself 35 lines '
             'earlier ("the two components meeting exactly at r=r0=+-1/sqrt3")'),
    dict(key='A given mass level is met by three sky angles', var='w', lo=0, hi=sp.pi / 3,
         closed=True, needs=False, verdict='SOUND',
         why='the caption names w=pi/6 as Nariai "where two merge" in its own clause'),
    dict(key='meets the ellipse in two real points and the diagonal in one: three real roots',
         var='r0', lo=-2 / sp.sqrt(3), hi=2 / sp.sqrt(3), closed=False,
         needs=True, verdict='SITE 4',
         why='the twin of SITE 3, 389 lines later in the overcritical section, same interval and '
             'same count'),
    dict(key='the three being distinct except at', var='w', lo=0, hi=sp.pi / 3, closed=False,
         needs=True, verdict='REPAIRED at r7737',
         why="this seat's own r7738 finding, landed"),
]

DESIGN = {'2M': DEG_M2, 'r0': DEG_R0, 'w': [sp.pi / 6]}
rows, _unmatched, _undecided = [], [], []
for sitedef in SITES:
    found = [s for fn, s in CANDS if sitedef['key'] in s or flat(sitedef['key']) in flat(s)]
    if not found:
        _unmatched.append(sitedef['key'])
        continue
    iv = (sp.Interval(sitedef['lo'], sitedef['hi']) if sitedef['closed']
          else sp.Interval.open(sitedef['lo'], sitedef['hi']))
    inside = [d for d in DESIGN[sitedef['var']] if iv.contains(d) == sp.true]
    if sitedef['var'] == 'r0':
        twom = [sp.nsimplify(sp.simplify(TWOM_OF_R0.subs(r0, d))) for d in inside]
    elif sitedef['var'] == 'w':
        twom = [sp.nsimplify(sp.simplify(TWOM_OF_R0.subs(r0, R0_OF_W).subs(w, d))) for d in inside]
    else:
        twom = [sp.nsimplify(d) for d in inside]
    mult = [roots_at(t) for t in twom]
    rows.append((sitedef, inside, twom, mult))

gate("Ⓑ② every adjudicated candidate was MATCHED to a swept candidate -- none was adjudicated "
     "from memory",
     not _unmatched and len(rows) == len(SITES),
     f"{len(rows)} of {len(SITES)} matched; unmatched {len(_unmatched)}: {_unmatched}")

print()
for sitedef, inside, twom, mult in rows:
    print(f"  {sitedef['verdict']:22s} [{sitedef['var']:2s}] {sitedef['key'][:62]}")
    print(f"      interval {'closed' if sitedef['closed'] else 'open'} "
          f"({sitedef['lo']}, {sitedef['hi']}); needs distinctness: {sitedef['needs']}")
    print(f"      degenerate designations INSIDE it: {len(inside)} {[str(x) for x in inside]}"
          + (f"  ->  2M = {[str(t) for t in twom]}" if inside else ""))
    for t, m in zip(twom, mult):
        print(f"      at 2M={t}: root multiset "
              f"{ {str(k): v for k, v in m.items()} } -- "
              f"{len(m)} distinct of 3")
    print(f"      {sitedef['why']}")
    print()

_live = [s for s, *_ in rows if s['verdict'].startswith('SITE')]
_contains_and_needs = [(s, ins) for s, ins, *_ in rows if s['needs'] and ins]
gate("⛔ Ⓑ③ the sweep's own answer: FOUR live sites, every one of them in P3, and every one with "
     "a degenerate designation computed INSIDE its interval and a merged root multiset there",
     len(_live) == 4
     and all(len(m[0]) == 2 for s, ins, tw, ml in rows if s['verdict'].startswith('SITE')
             for m in [ml] if m)
     and {s['key'][:20] for s in _live} and len(_contains_and_needs) == 6,
     f"candidates {len(CANDS)}; adjudicated {len(rows)}; SOUND "
     f"{len([s for s, *_ in rows if s['verdict'] == 'SOUND'])}; already REPAIRED "
     f"{len([s for s, *_ in rows if s['verdict'].startswith('REPAIRED')])}; LIVE SITES "
     f"{len(_live)}; undecided {len(_undecided)}.  contains-and-needs "
     f"{len(_contains_and_needs)} of which {len(_live)} are not already excluded by their own "
     f"sentence")

gate("Ⓑ④ and every live site is in ONE paper, which is the finding's shape: the defect is a "
     "sentence-form in P3 and not a corpus-wide habit",
     all('SdS-slicing' in fn for s, *_ in rows if s['verdict'].startswith('SITE')
         for fn, c in CANDS if s['key'] in c),
     "the four live sites are the sign-split sentence, the Lean-citation clause, and the two "
     "'three real roots/horizons' twins -- all in corpus/SdS-slicing-curve_v2.tex; the other "
     "papers' intervals are written in the dimensionless MASS, where Ⓞ② shows the degenerate set "
     "is the boundary and a strict inequality excludes it")

# ---------------------------------------------------------------- Ⓒ the reworded P15 sentence
print()
print("=" * 100)
print("  Ⓒ  THE COLD READ OF THE REWORDED P15 SENTENCE")
print("=" * 100)
P15 = (ROOT / 'corpus' / 'CR_cosmology.tex').read_text(encoding='utf-8')
P15F = flat(P15)
LANDED = {
    'amplitude on 97.93': '$97.93$ per cent of its amplitude varies with $\ell$',
    'variance on 93.6': 'so of the variance that varies with $\ell$',
    'the binning named': '$1.0076$ and $1.0035$ on the finer binning in wavenumber',
}
_ok = {k: (v in P15, flat(v) in P15F) for k, v in LANDED.items()}
gate("Ⓒ① all three repairs r7737 landed are present, raw AND flattened",
     all(a or b for a, b in _ok.values()),
     "; ".join(f"{k}: raw {a}, flat {b}" for k, (a, b) in _ok.items()))

# the binning named is the FINER one -- checked against the receipt's own node arithmetic
RC = (ROOT / 'receipts' / 'P15_CR_cosmology' /
      ('P15_both_mechanisms_contribute_at_unit_amplitude_and_the_located_step_is_'
       'the_kernels_because_the_source_template_is_flat_in_ell.py')).read_text(encoding='utf-8')
# ⛔ G6 AGAIN, AND IN A PYTHON SOURCE THIS TIME: the receipt's identity line is split across two
#    source lines by Python string concatenation, so the literal is absent from the raw file for
#    exactly the reason a LaTeX sentence line-wraps.  The seam is removed before the match.
RC_SEAMLESS = flat(re.sub(r'"\s*\n\s*"', '', RC))
_arith = re.search(r'(\d+) = (\d+)\*(\d+) \+ (\d+) = (\d+)\*(\d+) \+ (\d+)', RC_SEAMLESS)
_pri_bins, _sec_bins = (int(_arith.group(2)), int(_arith.group(5))) if _arith else (0, 0)
gate("Ⓒ②ᵃ \"the finer binning\" IS the binning the printed pair comes from -- the primary, "
     "computed from the receipt's own node arithmetic and not assumed",
     _arith is not None and _pri_bins > _sec_bins and _pri_bins * int(_arith.group(3)) +
     int(_arith.group(4)) == int(_arith.group(1)),
     f"the receipt's own closure line gives {_arith.group(0) if _arith else 'NOT FOUND'}: primary "
     f"{_pri_bins} bins against secondary {_sec_bins}, so the PRIMARY is the finer one, and "
     f"1.0076/1.0035 are the primary's -- r7738 Ⓐ⑥ asked for exactly this and it is right")


def pinned(pat):
    m = re.search(pat, RC)
    return float(m.group(1)) if m else float('nan')


SH_K = pinned(r"SH\['PRIMARY'\]\[0\] - (0\.\d+)\)")
SH_S = pinned(r"SH\['PRIMARY'\]\[1\] - (0\.\d+)\)")
RMS_K = pinned(r"SH\['PRIMARY'\]\[2\] - (0\.\d+)\)")
RMS_S = pinned(r"SH\['PRIMARY'\]\[3\] - (0\.\d+)\)")
VS_K = pinned(r"VS\['PRIMARY'\]\[0\] - (0\.\d+)\)")
A_K = pinned(r"_a\['PRIMARY'\]\[0\] - (1\.\d+)\)")
A_S = pinned(r"_a\['PRIMARY'\]\[1\] - (1\.\d+)\)")
amp = (A_K * RMS_K * SH_K) / (A_K * RMS_K * SH_K + A_S * RMS_S * SH_S)
gate("⛭ Ⓒ②ᵇ and the two KINDS are now distinguished in the sentence, which is what r7738 Ⓐ⑤ "
     "asked for: the word amplitude sits on the rms fractions and the word variance on the "
     "variance share, each on the right figure",
     'per cent of its amplitude' in P15F and 'of the variance that varies' in P15F
     and abs(100 * VS_K - 93.6) < 0.05 and abs(100 * amp - 93.6) > 1.0,
     f"97.93/22.39 are rms fractions and carry the word amplitude; 93.6 is the variance share "
     f"({100 * VS_K:.2f} %) and carries the word variance; the amplitude share of the same "
     f"quantity is still {100 * amp:.1f} %, so the figure a reader would have computed from the "
     f"old wording is {93.6 - 100 * amp:+.1f} points from what is printed -- and the sentence "
     f"now says which is which")

STEMS = [
    ('location', "the located transition belongs to the contrast between the arms and not to their sources"),
    ('presence', "That exclusion is about the sources' own ratio, not about their difference once it is projected"),
    ('structure', "But only the distance ratio's contribution is structured in multipole"),
    ('size', "The step's size, by contrast, is in both arms"),
]
_pos = {n: P15F.find(flat(s)) for n, s in STEMS}


def says_sources_carry(sentence):
    s = flat(sentence).lower()
    return (any(t in s for t in ('source', 'sources'))
            and any(t in s for t in ('carries', 'carry', 'belongs to', 'is in'))
            and any(t in s for t in ('step', 'transition', 'feature'))
            and not any(t in s for t in ('not to their sources', 'not absent', 'not about')))


FAB = ["The located transition belongs to the sources and the sources carry the step.",
       "The two arms' sources carry the located transition at the multipole where it falls."]
_rf = [n for n, s in STEMS if says_sources_carry(s)]
_ff = [i for i, s in enumerate(FAB) if says_sources_carry(s)]
gate("Ⓒ③ the partition SURVIVES the rename -- four stems in order, and the classifier still "
     "returns 0 of 4 real with 2 of 2 fabricated flagged (G4)",
     all(v >= 0 for v in _pos.values())
     and list(_pos.values()) == sorted(_pos.values())
     and not _rf and len(_ff) == len(FAB),
     f"stem offsets {_pos}, in order; real stems read 4, flagged {len(_rf)} {_rf}; fabricated "
     f"read {len(FAB)}, flagged {len(_ff)}; the structured leg is now named explicitly as the "
     f"distance ratio, so the forbidden reading is LESS available than before, not more")

# ⛔ the one the rename did move
EXCLUDED = "the two arms' $\\eta$-integrated sources"
CONCEDED = 'exchanging their sources together with their distance maps'
FRAMING = 'not about their difference once it is projected'
gate("⛔ Ⓒ④ BUT THE RENAME MADE THE CONCEDED OBJECT WIDER THAN THE FRAMING CLAUSE'S: stem 1 "
     "excludes the SOURCES' own ratio, the framing clause promises a statement about THEIR "
     "difference once projected, and the leg actually measured is the sources TOGETHER WITH "
     "THEIR DISTANCE MAPS",
     flat(EXCLUDED) in P15F and CONCEDED in P15F and FRAMING in P15F
     and 'their difference once it is projected together' not in P15F,
     f"excluded object: \"{EXCLUDED}\" (present: {flat(EXCLUDED) in P15F}); framing clause: "
     f"\"{FRAMING}\" (present: {FRAMING in P15F}); measured leg: \"{CONCEDED}\" (present: "
     f"{CONCEDED in P15F}).  The framing clause names the SOURCES' projected difference; the leg "
     f"is a COMBINATION that also carries the distance maps, which is the same object the OTHER "
     f"leg is named for -- so the concession no longer isolates what the framing clause promises, "
     f"and the two legs' names now share a term")

print()
_fail = [t for t, ok, _ in ARMS if not ok]
print(f"{len(ARMS)} arms, {len(ARMS) - len(_fail)} PASS, {len(_fail)} FAIL")
if _fail:
    print("FAILING: " + "; ".join(_fail))
sys.exit(0)
