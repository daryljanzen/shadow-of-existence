#!/usr/bin/env python3
"""r7672 - a cold read of the two-reading remark and the along-the-connection theorem.

Registered in PREDICTION.md before this ran.  The Lean verdicts are functions of text parsed out of
`AlongConnection.lean`; the residue verdict is a COMPARISON computed over every sentence of P1 that
mentions the temporal separation, classified by markers drawn from the remark's own text — which is
`r7670`'s correction applied by name.  Three guard families must flip or the receipt is withdrawn.
"""
import json, os, re, subprocess, sys

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True,
                      text=True, check=True).stdout.strip()
HERE = os.path.dirname(os.path.abspath(__file__))
flat = lambda s: re.sub(r'\s+', ' ', s)


def read(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        sys.exit(f"⛔ absent on this tree: {rel}")
    return open(p, encoding='utf-8').read()


AC = read('computations/formalisation/lean/probes/AlongConnection.lean')
TEX = read('corpus/BH_causality_v2.tex')
FTEX = flat(TEX)
SENTS = re.split(r'(?<=[.!?]) ', FTEX)

ti = TEX.index('\\label{thm:metric-singularity}')
rm = re.search(r'\\begin\{remark\}(.*?)\\end\{remark\}', TEX[ti:ti + 9000], re.S)
if rm is None:
    sys.exit("⛔ the along-the-connection remark is gone after `thm:metric-singularity`.")
REMARK = flat(rm.group(1))
if 'temporal leg accumulated along it' not in REMARK:
    sys.exit("⛔ the remark's new sentences are not in it on this tree: the object of this read is "
             "gone, and no verdict below would be about it.")


def decl(name):
    r = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', AC, re.S | re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a theorem in AlongConnection.lean on this tree.")
    return r.group(0)


def groups(sig):
    out, depth, start = [], 0, None
    for i, ch in enumerate(sig):
        if ch in '([{':
            if depth == 0:
                start = i
            depth += 1
        elif ch in ')]}':
            depth -= 1
            if depth == 0:
                out.append(sig[start:i + 1])
    if depth:
        sys.exit("⛔ the signature's brackets do not balance: the binder parse is unsound.")
    return out


def bnames(sig):
    out = []
    for b in groups(sig):
        inner = b[1:-1].strip()
        out.append('[' + inner.split()[0] + ']' if b[0] == '[' else
                   inner.split(' ')[0].split(':')[0].strip())
    return out


def conjuncts(text):
    out, depth, buf = [], 0, ''
    for ch in text:
        if ch in '([{':
            depth += 1
        elif ch in ')]}':
            depth -= 1
        if ch == '∧' and depth == 0:
            out.append(buf.strip()); buf = ''
        else:
            buf += ch
    out.append(buf.strip())
    return [flat(c) for c in out if c.strip()]


CITED = ['ac_metric_singularity_along', 'ac_lapse_pos_forces_point', 'ac_witness']
RESOLVE = {n: bool(re.search(r'^theorem ' + re.escape(n) + r'\b', AC, re.M)) for n in CITED}
UNRESOLVED = [n for n, ok in RESOLVE.items() if not ok]

MSA = decl('ac_metric_singularity_along')
LPF = decl('ac_lapse_pos_forces_point')
WIT = decl('ac_witness')

msa_sig = re.search(r'theorem ac_metric_singularity_along(.*?)\n    σ\.Δτ = 0', MSA, re.S)
if msa_sig is None:
    sys.exit("⛔ `ac_metric_singularity_along`'s conclusion no longer starts `σ.Δτ = 0`.")
MSASIG = flat(msa_sig.group(1))
MSAB = bnames(msa_sig.group(1))
MSAC = conjuncts(re.search(r'\n    (σ\.Δτ = 0.*?) := by\n', MSA, re.S).group(1))

lpf_sig = re.search(r'theorem ac_lapse_pos_forces_point(.*?)\n    \(∀ s ∈ Icc', LPF, re.S)
LPFSIG = flat(lpf_sig.group(1)) if lpf_sig else ''
LPFB = bnames(lpf_sig.group(1)) if lpf_sig else []
WITC = conjuncts(re.search(r'theorem ac_witness :(.*?) := by', WIT, re.S).group(1))

# ------------------------------------------------------- guard family one
in_msa = lambda needle: any(needle in c for c in MSAC)
G = {'true-probe  (`σ.Δτ = 0` is a conjunct)': in_msa('σ.Δτ = 0'),
     'false-probe (`σ.Δs = 0` is a conjunct)': in_msa('σ.Δs = 0')}
if not (G['true-probe  (`σ.Δτ = 0` is a conjunct)'] is True and
        G['false-probe (`σ.Δs = 0` is a conjunct)'] is False):
    sys.exit(f"⛔ THE CONJUNCT GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")


# ------------------------------------------------------- guard family two
def present(markers, text):
    """Anchored markers only, in the two forms `r7670` fixed: a word boundary, or an escaped
    LaTeX/Lean control sequence, which cannot occur inside a word."""
    out = []
    for mk in markers:
        if '\\b' not in mk and '\\\\' not in mk:
            sys.exit(f"⛔ marker {mk!r} is unanchored: neither a word boundary nor an escaped "
                     'control sequence.  `r7666` shipped a bare substring that matched "proper" '
                     'inside "property".')
        mm = re.search(mk, text, re.I)
        if mm:
            out.append({'marker': mk, 'context': text[max(0, mm.start() - 55):mm.end() + 55]})
    return out


G[r'marker-probe true  (\btemporal leg\b in the remark)'] = bool(
    present([r'\btemporal leg\b'], REMARK))
G[r'marker-probe false (\bparacompact\b in the remark)'] = bool(
    present([r'\bparacompact\b'], REMARK))
G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] = not bool(
    present([r'\bproper\b'], 'so by the Cauchy property'))
if not all((G[r'marker-probe true  (\btemporal leg\b in the remark)'] is True,
            G[r'marker-probe false (\bparacompact\b in the remark)'] is False,
            G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] is True)):
    sys.exit(f"⛔ THE MARKER GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

V = {}
score = lambda k, verdict, ev: V.__setitem__(k, [verdict, ev])

# ----------------------------------------------------------------- ① … ④
leg = bool(present([r'\btemporal leg accumulated along it\b'], REMARK))
intN = bool(present([r'\\Delta\\tau=\\int N\\,\\|\\mathrm\{d\}t\\|'], REMARK))
one_value = bool(present([r'\bstays at one value of the invariant spatial coordinate\b'], REMARK))
dtau_def = bool(re.search(r'def Δτ : ℝ := ∫ s in \(0:ℝ\)\.\.1, σ\.n s \* \|σ\.dt s \(vel γ s\)\|', AC))
dx_def = bool(re.search(r'def Δx : ℝ := ∫ s in \(0:ℝ\)\.\.1, √\(σ\.h s \(vel γ s\) \(vel γ s\)\)', AC))
v1 = lambda a, b, c_, d: 'SUPPORTED' if all((a, b, c_, d)) else 'NOT SUPPORTED'
score('①', v1(leg, intN, one_value, dtau_def),
      f"the remark's reading and the Lean's definition agree to the symbol: `Δτ` is \"the temporal "
      f"leg accumulated along it\" ({leg}), written `Δτ = ∫N|dt|` ({intN}), and the Lean's is "
      f"`def Δτ := ∫ s in 0..1, σ.n s * |σ.dt s (vel γ s)|` ({dtau_def}), with "
      f"`Δx := ∫ √(h(γ′,γ′))` beside it ({dx_def}).  Both are INTEGRALS along the curve, not "
      f"endpoint differences, and the remark's reason — the geodesic staying at one value of the "
      f"invariant spatial coordinate, so running along the frame's own time direction ({one_value}) "
      f"— is the clause that makes an integral the right object.")

kill = bool(present([r'\\int\\|\\chi\\|\\,\\mathrm\{d\}\\lambda', r'\\int\|\\chi\|'], REMARK))
kill_in_P1 = bool(present([r'ds\^\{2\}=g\(\\chi,\\chi\)\\,d\\lambda\^\{2\}'], FTEX))
wit_boost = any('gM (χ x) (χ x) = x.1 * x.2' in c for c in WITC)
wit_lambda = bool(present([r'\bKilling parameter\b'], flat(AC)))
v2 = lambda a, b: 'SUPPORTED' if (a and b) else 'NOT SUPPORTED'
score('②', v2(kill, kill_in_P1),
      f"the Killing-horizon form is now written in the remark ({kill}), and `lem:killing`'s own "
      f"proof carries `ds² = g(χ,χ)dλ²` ({kill_in_P1}), so the specialisation the remark cites to "
      f"that lemma is in that lemma.  `r7670` found this consistent but unwritten; it is written "
      f"now.  The witness carries the same field concretely — `g(χ,χ) = UV` ({wit_boost}) — and the "
      f"file names `λ = log V` the Killing parameter ({wit_lambda}).")

invariant = bool(present([r'\bIts integrand is invariant and it is not a coordinate difference\b'],
                         REMARK))
v3 = lambda a: 'SUPPORTED' if a else 'NOT SUPPORTED'
score('③', v3(invariant),
      f"the remark states it in one clause ({invariant}).  In the Lean the integrand is "
      f"`σ.n s * |σ.dt s (vel γ s)|`, built from the splitting and the `mfderiv` velocity, so it is "
      f"frame data and a vector, not a chart coordinate's increment — which is what \"not a "
      f"coordinate difference\" has to mean for the formal object.")

nonvar = bool(present([r'\bassigned by an arbitrary temporal function stays non-invariant\b'], REMARK))
cites = bool(present([r'Corollary~\\ref\{cor:threefold\}\(iv\)'], REMARK))
c4 = re.search(r'\\label\{cor:threefold\}(.*?)\\end\{corollary\}', TEX, re.S)
iv_says = bool(c4 and present([r'\bhas no invariant geometric meaning\b'], flat(c4.group(1))))
v4 = lambda a, b, c_: 'SUPPORTED' if all((a, b, c_)) else 'NOT SUPPORTED'
score('④', v4(nonvar, cites, iv_says),
      f"the remark says the arbitrary-temporal-function separation stays non-invariant ({nonvar}) "
      f"and cites `cor:threefold`(iv) ({cites}), which does say it — \"has no invariant geometric "
      f"meaning, and may be altered arbitrarily by smooth local deformations\" ({iv_says}).  The "
      f"citation holds and the two readings are now related in one place, which is `r7670`'s ⑩ "
      f"repaired.")

# ----------------------------------------------------------------- ⑤ ⑥ ⑦
split_in_struct = bool(re.search(r'split : ∀ s ∈ Icc \(0:ℝ\) 1, S\.gE \(γ s\) = h s - \(n s\) \^ 2',
                                 AC))
n_nonneg = 'n_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ n s' in flat(AC)
h_nonneg = 'h_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ h s (vel γ s) (vel γ s)' in flat(AC)
hcont = 'hcont' in MSAB
gamma_class = bool(re.search(r'ContMDiff[^\n]{0,60}γ', MSASIG))
# "on any manifold": which instances are in force at the theorem's line?
msa_line = AC[:AC.index('theorem ac_metric_singularity_along')].count('\n') + 1
ismf_line = (AC[:AC.index('variable [IsManifold')].count('\n') + 1
             if 'variable [IsManifold' in AC else 10 ** 9)
msa_needs_ismf = msa_line > ismf_line
lpf_line = AC[:AC.index('theorem ac_lapse_pos_forces_point')].count('\n') + 1
lpf_needs_ismf = lpf_line > ismf_line
fd = len(re.findall('FiniteDimensional', AC))
t2 = len(re.findall('T2Space', AC))
v5 = lambda hc, gc, ni, nf, nt: 'NOT SUPPORTED' if (hc or gc) else 'SUPPORTED'
score('⑤', v5(hcont, gamma_class, msa_needs_ismf, fd, t2),
      f"the splitting IS `g = h − n²dt⊗dt` as a field of the structure ({split_in_struct}) with "
      f"`n ≥ 0` ({n_nonneg}), and the conclusion's first conjunct is `Δτ = 0`.  \"On any manifold\" "
      f"is not only true but UNDERSTATED: at this theorem's line only `[TopologicalSpace N]` and "
      f"`[ChartedSpace E N]` are in force — the `[IsManifold 𝓘(ℝ,E) 1 N]` instance is declared "
      f"LATER in the file ({not msa_needs_ismf} that it is needed here) — and `FiniteDimensional` "
      f"and `T2Space` occur {fd} and {t2} times.  So it holds without even a `C¹` atlas.  ⌗ But the "
      f"sentence's hypothesis list is INCOMPLETE and its curve class is SPURIOUS.  Binders: "
      f"{MSAB}.  `hcont`, the continuity of `s ↦ h s (γ′ s) (γ′ s)` on `[0,1]`, is a FOURTH "
      f"hypothesis the sentence does not state ({hcont}) and is NOT implied by the splitting, whose "
      f"`h` is an arbitrary field; the structure also carries `h_nonneg` ({h_nonneg}), the spatial "
      f"part non-negative on the velocity, which the sentence's `g = h − N²dt²` does not say.  And "
      f"the sentence says \"along a `C¹` curve\" while the theorem imposes NO differentiability "
      f"class on `γ` at all ({gamma_class}) — `vel` is `mfderiv`, defined regardless.  ⌗ The "
      f"conclusion is also THREE conjuncts, not one: `Δτ = 0`, `n·dt(γ′) = 0` pointwise, and "
      f"`h(γ′,γ′) = 0` pointwise — (b) recovered pointwise from its integral form, which is the "
      f"step the registration called the expected stop.")

lpf_extra = [b for b in LPFB if b in ('hcont', 'hpd')]
lpf_concl = conjuncts(re.search(r'\n    (\(∀ s ∈ Icc.*?) := by\n', LPF, re.S).group(1))
lpf_implication = any('MDifferentiableAt' in c and 'γ 1 = γ 0' in c for c in lpf_concl)
v6 = lambda ex, im: 'NOT SUPPORTED' if (ex or im) else 'SUPPORTED'
score('⑥', v6(lpf_extra, lpf_implication),
      f"`ac_lapse_pos_forces_point` does conclude the events coincide, but on more than the "
      f"sentence states.  Binders: {LPFB} — besides `hn` (`0 < n`), it carries {lpf_extra}: "
      f"`hcont` again, and `hpd`, that each `h s` is POSITIVE DEFINITE on `ker dt s`.  `hpd` is the "
      f"hypothesis doing the work — it is what turns `dt(γ′) = 0` into `γ′ = 0` — and the sentence "
      f"does not state it.  And `γ 1 = γ 0` is not a conjunct but the consequent of an IMPLICATION "
      f"({lpf_implication}): it holds for `γ` manifold-differentiable on `[0,1]`, which the "
      f"sentence's \"force `p = q`\" reads as unconditional.  This theorem, unlike the first, does "
      f"sit after the `IsManifold` instance ({lpf_needs_ismf}), so the `C¹` atlas is needed here "
      f"and not there — a distinction \"on any manifold\" flattens.")

wit = {'g(χ,χ) = UV': any('gM (χ x) (χ x) = x.1 * x.2' in c for c in WITC),
       'χ is the velocity': any('χ (γ s) = vel' in c for c in WITC),
       'the velocity is null and non-zero': any('= 0 ∧ vel' in c and '≠ 0' in c for c in WITC),
       'the lapse vanishes on γ': any('σ.n s = 0' in c for c in WITC),
       'the Killing parameter separates': any('σ.dt s (vel γ s)) = 1' in c for c in WITC),
       'Δτ = 0': any('σ.Δτ = 0' in c for c in WITC),
       'p ≠ q': any('γ 0 ≠ γ 1' in c for c in WITC)}
nolapse = bool(re.search(r'theorem ac_witness_no_positive_lapse', AC))
isom = bool(re.search(r'(theorem|lemma) ac_boost_isometry', AC)) and \
    bool(re.search(r'(theorem|lemma) ac_boost_generator', AC))
v7 = lambda w: 'SUPPORTED' if all(w.values()) else 'NOT SUPPORTED'
score('⑦', v7(wit),
      f"`ac_witness` carries both halves and more {wit}: the lapse vanishes along the whole curve, "
      f"`Δτ = 0`, and `γ 0 = (0,1) ≠ (0,e) = γ 1`, with `∫dt(γ′) = 1` so the Killing parameter still "
      f"separates them.  `χ` is proved Killing (`ac_boost_isometry`, `ac_boost_generator`: {isom}), "
      f"and `ac_witness_no_positive_lapse` ({nolapse}) closes the circle — along this curve NO "
      f"positive-lapse splitting satisfies (a) and (b), so the vanishing is forced and not chosen.  "
      f"That last theorem is the sharper half and the remark does not name it.")

# -------------------------------------------------- ⑧ the residue, COMPUTED
DTAU = [(i, s) for i, s in enumerate(SENTS) if re.search(r'\\Delta\\?\s*\\?tau', s)]
if len(DTAU) < 5:
    sys.exit(f"⛔ only {len(DTAU)} sentences of P1 mention the temporal separation; the enumeration "
             "this residue depends on is wrong.")
# Each account is a marker the REMARK now carries; a sentence is accounted-for when the remark's
# text covers the reading it uses.  Markers drawn from the remark, not invented here.
ACCOUNTS = {
    'the adapted-frame leg': [r'\btemporal leg accumulated along it\b'],
    'the arbitrary-temporal-function separation': [
        r'\bassigned by an arbitrary temporal function stays non-invariant\b'],
    'the coordinate-difference exclusion': [r'\bit is not a coordinate difference\b'],
    'the Killing-horizon form': [r'\\int\|\\chi\|'],
}
HAVE = {k: bool(present(v, REMARK)) for k, v in ACCOUNTS.items()}
# classify each Δτ sentence
CLASSES = [
    ('endpoint difference of a temporal function',
     [r'\\Delta\\tau=\\tau\(q\)-\\tau\(p\)', r'\\tau\(q\)-\\tau\(p\)'],
     'the arbitrary-temporal-function separation'),
    ('the adapted-frame conjugate',
     [r'\btemporal separation conjugate to it\b', r'\btemporal leg\b'],
     'the adapted-frame leg'),
    ('the theorem\'s conclusion',
     [r'\btheir temporal separation vanishes\b', r'\bgives \$\\Delta\\tau=0'],
     'the adapted-frame leg'),
    ('the metric relation',
     [r'\\Delta s\^2 = \\Delta x\^2 - \\Delta\\tau\^2', r'\\Delta x\^2=\\Delta\\tau\^2',
      r'\\Delta\\tau\^2=0'],
     'the adapted-frame leg'),
    ('frame-dependence, not degeneracy',
     [r'\bis frame-dependent does not mean it can be driven to zero\b'],
     'the arbitrary-temporal-function separation'),
    ('the accumulation exclusion',
     [r'\bnot coordinate differences accumulated along some path\b'],
     None),
]
CLASSIFIED, RESIDUE = [], []
for i, s in DTAU:
    hit = None
    # A sentence that IS part of the remark is accounted for by construction -- it is the account.
    # The first draft of this classifier had no such class, so the remark's own attestation
    # sentence ("In this form the theorem is machine-checked ... give Delta-tau = 0") came back
    # UNCLASSIFIED and inflated the residue to 1.  A residue is a statement about P1's OTHER
    # sentences; counting the remark against itself measures the classifier.
    if s.strip() and s.strip()[:60] in REMARK:
        hit = ("the remark's own sentence", 'the adapted-frame leg')
    else:
        for name, marks, account in CLASSES:
            if present(marks, s):
                hit = (name, account)
                break
    covered = bool(hit and hit[1] and HAVE.get(hit[1]))
    CLASSIFIED.append({'i': i, 'class': hit[0] if hit else 'UNCLASSIFIED',
                       'account': (hit[1] if hit else None), 'covered': covered,
                       'text': s[:260]})
    if not covered:
        RESIDUE.append(CLASSIFIED[-1])
# the accumulation sentence does not itself mention Δτ; check it separately
ACCUM = [s for s in SENTS if present([r'\bnot coordinate differences accumulated along some path\b'], s)]
accum_covered = HAVE['the coordinate-difference exclusion']
remark_accumulates = bool(present([r'\baccumulated along it\b'], REMARK))
v8 = lambda res, ac_cov, ra: 'NOT SUPPORTED' if (res or (ra and not ac_cov) or ra) else 'SUPPORTED'
score('⑧', v8(RESIDUE, accum_covered, remark_accumulates),
      f"the residue was COMPUTED over all {len(DTAU)} sentences of P1 that mention the temporal "
      f"separation, classified by markers drawn from the remark's own text; the remark's four "
      f"accounts are {HAVE}, and **{len(RESIDUE)} sentence(s) of that set fall outside them**: "
      + ('; '.join(f"[{r['i']}] {r['class']}" for r in RESIDUE) if RESIDUE else 'none')
      + f".  ⌗ But the sentence the order names is not in that set, because it does not use the "
      f"symbol: the proof's *\"These are not coordinate differences accumulated along some path "
      f"between `p` and `q`\"* ({len(ACCUM)} such).  The remark answers its COORDINATE half — "
      f"\"it is not a coordinate difference\" ({accum_covered}) — and not its ACCUMULATION half, "
      f"while the remark itself now says `Δτ` is \"the temporal leg **accumulated along** it\" "
      f"({remark_accumulates}).  The two sentences now use the same word for opposite purposes, "
      f"two paragraphs apart, and that is sharper than it was at `r7670`: the collision is no "
      f"longer latent.  One clause in the proof — that an invariant integrated along the "
      f"connection is not what \"accumulated\" excludes — would close it.")

# ----------------------------------------------------- guard family three
FLIP = {'①': (v1(leg, intN, one_value, dtau_def), v1(False, intN, one_value, dtau_def)),
        '②': (v2(kill, kill_in_P1), v2(False, kill_in_P1)),
        '③': (v3(invariant), v3(False)),
        '④': (v4(nonvar, cites, iv_says), v4(nonvar, False, iv_says)),
        '⑤': (v5(hcont, gamma_class, msa_needs_ismf, fd, t2),
              v5(False, False, msa_needs_ismf, fd, t2)),
        '⑥': (v6(lpf_extra, lpf_implication), v6([], False)),
        '⑦': (v7(wit), v7({'x': False})),
        '⑧': (v8(RESIDUE, accum_covered, remark_accumulates), v8([], True, False)),
        }
for k, (actual, negated) in FLIP.items():
    if actual == negated:
        sys.exit(f"⛔ {k}'s verdict does not depend on its reading: it returns '{actual}' either "
                 "way.  Every verdict in this receipt is withdrawn.")
G['flip-test (every derived verdict depends on its readings)'] = True
# the remark-own class must actually fire, and must not swallow a sentence outside the remark
G["class-probe (the remark's own attestation sentence is classified, not residual)"] = any(
    c['class'] == "the remark's own sentence" for c in CLASSIFIED)
G['class-probe (a Section-1 sentence is NOT classified as the remark\'s own)'] = not any(
    c['class'] == "the remark's own sentence" and c['i'] < 60 for c in CLASSIFIED)
if not (G["class-probe (the remark's own attestation sentence is classified, not residual)"] is True
        and G['class-probe (a Section-1 sentence is NOT classified as the remark\'s own)'] is True):
    sys.exit(f"⛔ THE CLASS GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

# ------------------------------------------------------------------ report
L = []
w = L.append
w(f"TREE: {open(os.path.join(HERE, 'runs', 'TREE.txt')).readline().strip()}")
w(f"GUARD: {json.dumps(G, ensure_ascii=False)}")
w(f"CITED NAMES: {len(CITED)} cited, unresolved -> {UNRESOLVED or 'none'}")
w("")
w(f"ac_metric_singularity_along BINDERS: {MSAB}")
w(f"  instances in force at its line: TopologicalSpace, ChartedSpace"
  f"{'' if not msa_needs_ismf else ', IsManifold'}")
w(f"  CONCLUSION ({len(MSAC)} conjuncts):")
for i, c in enumerate(MSAC, 1):
    w(f"    {i}. {c[:120]}")
w(f"ac_lapse_pos_forces_point BINDERS: {LPFB}")
w(f"  IsManifold needed here: {lpf_needs_ismf}")
w("")
w("THE REMARK'S FOUR ACCOUNTS:")
for k, v in HAVE.items():
    w(f"  {'CARRIED    ' if v else 'NOT CARRIED'}  {k}")
w("")
w(f"P1's Δτ SENTENCES, CLASSIFIED ({len(DTAU)}):")
for c in CLASSIFIED:
    w(f"  [{c['i']}] {'COVERED    ' if c['covered'] else 'NOT COVERED'}  {c['class']}")
    w(f"        {c['text'][:200]}")
w(f"  -> residue: {len(RESIDUE)}")
w("")
for k in '①②③④⑤⑥⑦⑧':
    if k in V:
        w(f"{k}  {V[k][0]}")
        w(f"     {V[k][1]}")
        w("")
tally = {}
for k, (verdict, _) in V.items():
    tally[verdict] = tally.get(verdict, 0) + 1
w(f"TALLY: {tally}")
OUT = '\n'.join(L)
print(OUT)
open(os.path.join(HERE, 'verdicts.txt'), 'w', encoding='utf-8').write(OUT + '\n')
json.dump({'tree': open(os.path.join(HERE, 'runs', 'TREE.txt')).read().splitlines(),
           'guard': G, 'cited': RESOLVE, 'msa_binders': MSAB, 'msa_conclusion': MSAC,
           'lpf_binders': LPFB, 'witness': wit, 'accounts': HAVE,
           'classified': CLASSIFIED, 'residue': len(RESIDUE),
           'accumulation_sentences': len(ACCUM), 'verdicts': V, 'tally': tally},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
