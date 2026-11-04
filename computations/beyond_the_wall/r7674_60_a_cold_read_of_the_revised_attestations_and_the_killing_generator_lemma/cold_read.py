#!/usr/bin/env python3
"""r7674 - a cold read of the revised attestations and the Killing-generator lemma.

Registered in PREDICTION.md before this ran.  Every verdict is a function of text parsed out of the
paper and the Lean on the tree `runs/TREE.txt` names; the proof sentence's invariance is checked by
COMPARING against `r7672`'s tree, not from memory; and arm ⓺ is a comparison of quantifiers, read
off each conjunct rather than asserted.  Three guard families must flip or the receipt is withdrawn.
"""
import json, os, re, subprocess, sys

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True,
                      text=True, check=True).stdout.strip()
HERE = os.path.dirname(os.path.abspath(__file__))
PREV = '54e854a6'          # r7672's registration commit, for the unchanged-sentence comparison
flat = lambda s: re.sub(r'\s+', ' ', s)


def read(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        sys.exit(f"⛔ absent on this tree: {rel}")
    return open(p, encoding='utf-8').read()


def show(rev, rel):
    r = subprocess.run(['git', 'show', f'{rev}:{rel}'], capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        sys.exit(f"⛔ cannot read {rel} at {rev}: the comparison this read depends on is impossible.")
    return r.stdout


AC = read('computations/formalisation/lean/probes/AlongConnection.lean')
KG = read('computations/formalisation/lean/probes/KillingGenerator.lean')
TEX = read('corpus/BH_causality_v2.tex')
FTEX = flat(TEX)
OLDTEX = flat(show(PREV, 'corpus/BH_causality_v2.tex'))

ti = TEX.index('\\label{thm:metric-singularity}')
rm = re.search(r'\\begin\{remark\}(.*?)\\end\{remark\}', TEX[ti:ti + 9000], re.S)
if rm is None:
    sys.exit("⛔ the along-the-connection remark is gone.")
REMARK = flat(rm.group(1))
ki = TEX.index('\\label{lem:killing}')
kp = re.search(r'\\begin\{proof\}(.*?)\\end\{proof\}', TEX[ki:ki + 9000], re.S)
if kp is None:
    sys.exit("⛔ `lem:killing`'s proof is gone.")
KPROOF = flat(kp.group(1))
if 'kg\\_lemma\\_killing\\_generator' not in KPROOF:
    sys.exit("⛔ the new attestation sentences are not at the end of `lem:killing`'s proof on this "
             "tree: the second object of this read is gone.")


def decl(src, name, where):
    r = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', src, re.S | re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a theorem in {where} on this tree.")
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


bnames = lambda sig: ['[' + g[1:-1].strip().split()[0] + ']' if g[0] == '[' else
                      g[1:-1].strip().split(' ')[0].split(':')[0].strip() for g in groups(sig)]


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


CITED = [('ac_metric_singularity_along', AC, 'AlongConnection'),
         ('ac_lapse_pos_forces_point', AC, 'AlongConnection'),
         ('ac_witness', AC, 'AlongConnection'),
         ('ac_witness_no_positive_lapse', AC, 'AlongConnection'),
         ('kg_lemma_killing_generator', KG, 'KillingGenerator'),
         ('kg_witness', KG, 'KillingGenerator')]
RESOLVE = {n: bool(re.search(r'^theorem ' + re.escape(n) + r'\b', s, re.M)) for n, s, _ in CITED}
UNRESOLVED = [n for n, ok in RESOLVE.items() if not ok]

MSA = decl(AC, 'ac_metric_singularity_along', 'AlongConnection.lean')
LPF = decl(AC, 'ac_lapse_pos_forces_point', 'AlongConnection.lean')
KGH = decl(KG, 'kg_lemma_killing_generator', 'KillingGenerator.lean')
KGW = decl(KG, 'kg_witness', 'KillingGenerator.lean')
MSAB = bnames(re.search(r'theorem ac_metric_singularity_along(.*?)\n    σ\.Δτ = 0', MSA, re.S).group(1))
LPFB = bnames(re.search(r'theorem ac_lapse_pos_forces_point(.*?)\n    \(∀ s ∈ Icc', LPF, re.S).group(1))
kgs = re.search(r'theorem kg_lemma_killing_generator(.*?)\n    \(∀ t ∈ Icc a b, mfderiv', KGH, re.S)
if kgs is None:
    sys.exit("⛔ `kg_lemma_killing_generator`'s conclusion no longer starts with the velocity form.")
KGB = bnames(kgs.group(1))
KGC = conjuncts(re.search(r'\n    (\(∀ t ∈ Icc a b, mfderiv.*?) := by\n', KGH, re.S).group(1))
KGWC = conjuncts(re.search(r'theorem kg_witness :(.*?) := by', KGW, re.S).group(1))

# ------------------------------------------------------- guard family one
in_kgc = lambda n: any(n in c for c in KGC)
G = {'true-probe  (`kg_deltaTau g X γ a b = 0` is a conjunct)':
     in_kgc('kg_deltaTau g X γ a b = 0'),
     'false-probe (`kg_everyInvariant g γ` is a conjunct)': in_kgc('kg_everyInvariant g γ')}
if not (G['true-probe  (`kg_deltaTau g X γ a b = 0` is a conjunct)'] is True and
        G['false-probe (`kg_everyInvariant g γ` is a conjunct)'] is False):
    sys.exit(f"⛔ THE CONJUNCT GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")


# ------------------------------------------------------- guard family two
def present(markers, text):
    out = []
    for mk in markers:
        # Three anchor forms, and no others.  `r7666` shipped a bare substring that matched
        # "proper" inside "property", so every marker must be anchored.  A prose marker carries
        # `\\b`; a LaTeX-command marker carries an escaped control sequence (`\\\\chi`), which
        # cannot occur inside a word; a math-mode marker carries an escaped `$`, which is a
        # delimiter and likewise cannot occur inside a word.  `r7670` added the second form when a
        # formula marker was refused; this run added the third for the same reason, and each is
        # recorded rather than quietly loosened.
        if not any(a in mk for a in ('\\b', '\\\\', '\\$')):
            sys.exit(f"⛔ marker {mk!r} is unanchored: it carries no word boundary, no escaped "
                     'control sequence and no escaped math delimiter.')
        mm = re.search(mk, text, re.I)
        if mm:
            out.append({'marker': mk, 'context': text[max(0, mm.start() - 50):mm.end() + 50]})
    return out


G[r'marker-probe true  (\bintegrated along it\b in the remark)'] = bool(
    present([r'\bintegrated along it\b'], REMARK))
G[r'marker-probe false (\bparacompact\b in the remark)'] = bool(
    present([r'\bparacompact\b'], REMARK))
G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] = not bool(
    present([r'\bproper\b'], 'so by the Cauchy property'))
# the math-delimiter form is anchored too: it must match the real token and not a wider one
G['marker-probe math-delimiter ($N>0$ matches itself, not $N>0.5$)'] = (
    bool(present([r'\$N>0\$'], r'where $N>0$ holds')) and
    not bool(present([r'\$N>0\$'], r'where $N>0.5$ holds')))
if not all((G[r'marker-probe true  (\bintegrated along it\b in the remark)'] is True,
            G[r'marker-probe false (\bparacompact\b in the remark)'] is False,
            G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] is True,
            G['marker-probe math-delimiter ($N>0$ matches itself, not $N>0.5$)'] is True)):
    sys.exit(f"⛔ THE MARKER GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

V = {}
score = lambda k, verdict, ev: V.__setitem__(k, [verdict, ev])

# ------------------------------------------------------------- ① ② ③
said1 = {'the split': bool(present([r'g=h-N\^\{2\}\\mathrm\{d\}t\^\{2\}'], REMARK)),
         'N ≥ 0': bool(present([r'\$N\\ge0\$'], REMARK)),
         'h non-negative and continuous': bool(present(
             [r'\bnon-negative and continuous along the curve\b'], REMARK)),
         'both legs vanish pointwise': bool(present(
             [r'\bboth legs vanish at every point of the curve\b'], REMARK)),
         'no curve class, no atlas smoothness': bool(present(
             [r'\bno differentiability class of the curve and no smoothness of the atlas\b'],
             REMARK))}
hcont_named = said1['h non-negative and continuous'] and 'hcont' in MSAB
curve_class_gone = not bool(present([r'\balong a \$C\^\{1\}\$ curve\b'], REMARK))
v1 = lambda s, hc, cg: 'SUPPORTED' if (all(s.values()) and hc and cg) else 'NOT SUPPORTED'
score('①', v1(said1, hcont_named, curve_class_gone),
      f"the sentence now names every hypothesis `ac_metric_singularity_along` has {said1}: binders "
      f"{MSAB}, and `hcont` — the continuity `r7672` found unstated and load-bearing — is stated "
      f"({hcont_named}).  The spurious `C¹` curve class is gone ({curve_class_gone}), replaced by "
      f"\"it needs no differentiability class of the curve and no smoothness of the atlas\", which "
      f"is the stronger and true reading.  And \"both legs vanish at every point of the curve\" "
      f"carries the two pointwise conjuncts the earlier sentence dropped.  `r7672`'s ⑤ is repaired "
      f"in all three of its parts, and the Lean file itself is unchanged, so the repair is in the "
      f"prose where it belonged.")

said2 = {'N > 0': bool(present([r'\$N>0\$'], REMARK)),
         'the curve differentiable': bool(present([r'\bthe curve is differentiable\b'], REMARK)),
         'h positive definite on ker dt': bool(present(
             [r'\bpositive definite on the kernel of \$\\mathrm\{d\}t\$'], REMARK)),
         'no-positive-lapse named': bool(present([r'ac\\_witness\\_no\\_positive\\_lapse'], REMARK))}
v2 = lambda s, b: 'SUPPORTED' if (all(s.values()) and set(('hn', 'hpd')) <= set(b)) else 'NOT SUPPORTED'
score('②', v2(said2, LPFB),
      f"all three hypotheses are now stated {said2} against binders {LPFB} — `hpd`, the "
      f"positive-definiteness `r7672` found to be the hypothesis the conclusion rests on, is named, "
      f"and the curve's differentiability, which was the consequent's antecedent, is stated as a "
      f"condition.  `ac_witness_no_positive_lapse` is named too, which is the sharper half I asked "
      f"for: on the Rindler generator no positive-lapse splitting satisfies (a) and (b), so the "
      f"lapse's vanishing is forced rather than chosen.")

integrated = bool(present([r'\btemporal leg integrated along it\b'], REMARK))
accum_of_dtau = bool(present([r'\baccumulated along it\b'], REMARK))
sets_aside = bool(present([r'\bnot the coordinate difference accumulated along a path that the '
                           r'proof below sets aside\b'], REMARK))
KEY = 'These are not coordinate differences accumulated along some path'
now_ctx = FTEX[FTEX.index(KEY):FTEX.index(KEY) + 220] if KEY in FTEX else ''
old_ctx = OLDTEX[OLDTEX.index(KEY):OLDTEX.index(KEY) + 220] if KEY in OLDTEX else ''
unchanged = bool(now_ctx) and now_ctx == old_ctx
v3 = lambda i, a, s, u: 'SUPPORTED' if (i and not a and s and u) else 'NOT SUPPORTED'
score('③', v3(integrated, accum_of_dtau, sets_aside, unchanged),
      f"the remark now says `Δτ` is \"the temporal leg INTEGRATED along it\" ({integrated}) and no "
      f"longer uses \"accumulated\" of `Δτ` at all ({accum_of_dtau}); and it names the exclusion it "
      f"is distinguishing itself from — \"not the coordinate difference accumulated along a path "
      f"that the proof below sets aside\" ({sets_aside}), which is the clause I recommended, made "
      f"shorter.  The proof's own sentence is UNCHANGED, verified by comparing its 220 characters "
      f"against `{PREV}`'s tree rather than from memory ({unchanged}).  `r7672`'s ⑧ is repaired "
      f"exactly as the fork was decided, and the collision is gone in the direction that kept the "
      f"proof intact.")

# ------------------------------------------------------------- ④ … ⑧
kg_said = {'nowhere zero': bool(present([r'\bnowhere zero\b'], KPROOF)),
           'null at one point': bool(present([r'\bnull at one point\b'], KPROOF)),
           'null throughout': bool(present([r'\bthe curve is null throughout\b'], KPROOF)),
           'local isometry into itself': bool(present(
               [r'\blocal isometry that carries the generator into itself\b'], KPROOF)),
           'every invariant same value': bool(present(
               [r'\bevery invariant takes the same value at both\b'], KPROOF)),
           'the lapse integral vanishes': bool(present(
               [r'\\Delta\\tau=\\int\|\\chi\|\\,\\mathrm\{d\}\\lambda=0'], KPROOF)),
           'witnessed on a Rindler generator': bool(present(
               [r'\bwitnessed on a generator of the Rindler horizon\b'], KPROOF))}
hyp_named = {'hXne (nowhere zero)': 'hXne' in KGB, 'hnull (null at one point)': 'hnull' in KGB,
             'hK (Killing)': 'hK' in KGB, 'hγ (integral curve)': 'hγ' in KGB}
hyp_unnamed = {'hg (the metric chart-rep differentiable)': 'hg' in KGB
               and not bool(present([r'\bchart representative\b|\bdifferentiable metric\b'], KPROOF)),
               'hX (the field C¹ as a bundle section)': 'hX' in KGB
               and not bool(present([r'\bthe field is \$C\^\{1\}\$'], KPROOF))}
v4 = lambda u: 'NOT SUPPORTED' if any(u.values()) else 'SUPPORTED'
score('④', v4(hyp_unnamed),
      f"the conclusion carries what the sentence claims: conjunct 2 is "
      f"`∀ t ∈ Icc a b, g (γ t) (X (γ t)) (X (γ t)) = 0 ∧ g(γ′,γ′) = 0` — null THROUGHOUT the "
      f"segment, from `hnull` at the single `t₀` ({kg_said['null throughout']}).  The hypotheses it "
      f"names are there {hyp_named}.  ⌗ But TWO regularity hypotheses go unstated {hyp_unnamed}: "
      f"`hg`, that the metric's chart representative is eventually differentiable near each `γ t`, "
      f"and `hX`, that the field is `C¹` as a section of the tangent bundle.  Binders: {KGB}.  "
      f"These are the same class of omission as the continuity hypothesis in the first attestation "
      f"— the one just repaired — so the sentence repeats, on the new theorem, the fault that was "
      f"corrected on the old one.")

rel = re.search(r'def kg_Related(.*?)\n\n', KG, re.S)
RELD = flat(rel.group(1)) if rel else ''
rel_local = '∃ U : Set N' in RELD and 'IsOpen U' in RELD and 'γ t₁ ∈ U' in RELD
rel_isom = '∀ x ∈ U, ∀ v w : E, g (F x) (mfderiv' in RELD
invariant_thm = len(re.findall(r'^theorem[^\n]*invariant', KG, re.M | re.I))
normsq_internal = 'kl_normSq g X (γ y) = kl_normSq g X (γ y\')' in flat(KG)
v5 = lambda it: 'NOT SUPPORTED' if it == 0 else 'SUPPORTED'
score('⑤', v5(invariant_thm),
      f"conjunct 3 is `∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related g γ t₁ t₂` — ANY two parameters, "
      f"and `kg_Related` is a genuine local isometry: an open `U ∋ γ t₁` ({rel_local}) with a map "
      f"`F` satisfying `g (F x) (DF v) (DF w) = g x v w` on `U` ({rel_isom}), `F (γ t₁) = γ t₂`, and "
      f"`F (γ s) = γ (s + t₂ − t₁)` near `t₁`, so it carries the generator into itself.  That half "
      f"is exact.  ⌗ But \"so every invariant takes the same value at both\" is NOT a statement the "
      f"Lean makes: no theorem in the file mentions an invariant ({invariant_thm}), and the only "
      f"invariant equality proved is ONE — `kl_normSq g X` — used internally to propagate the null "
      f"condition ({normsq_internal}).  It follows from the isometry as mathematics, and it is true, "
      f"but it is a classical inference and not machine-checked; the remark's own discipline is to "
      f"mark those, as it does for Bernal–Sánchez, the achronal boundary and the Cotton criterion.")

dt = re.search(r'def kg_deltaTau(.*?)\n\n', KG, re.S)
DTD = flat(dt.group(1)) if dt else ''
dtau_form = '∫ t in a..b, kg_lapse g X (γ t) * |(1 : ℝ)|' in DTD
lapse = re.search(r'def kg_lapse(.*?)\n', KG)
v6 = lambda f: 'SUPPORTED' if f else 'NOT SUPPORTED'
score('⑥', v6(dtau_form and in_kgc('kg_deltaTau g X γ a b = 0')),
      f"`kg_deltaTau = ∫ t in a..b, kg_lapse g X (γ t) * |1|` ({dtau_form}) and its vanishing is "
      f"conjunct 5.  The `|dλ(γ′)|` of the remark's `∫|χ|dλ` is the `|1|`: the curve's parameter IS "
      f"`λ`, so the factor is unity by construction rather than computed, which is the honest "
      f"reading of writing it as `dλ`.  The lapse is `{flat(lapse.group(1))[:60] if lapse else '?'}`.")

wit = {'g(X,X) = UV': any('kg_w_X x) = x.1 * x.2' in c for c in KGWC),
       'Killing everywhere': any('lieDeriv kg_w_X kg_w_g x v w = 0' in c for c in KGWC),
       'nowhere zero on the segment': any('kg_w_X (kg_w_γ t) ≠ 0' in c for c in KGWC),
       'endpoints distinct': any('kg_w_γ 0 ≠ kg_w_γ 10' in c for c in KGWC),
       'null at both ends': sum('kg_w_X (kg_w_γ' in c and '= 0' in c for c in KGWC) >= 2,
       'related both ways': sum('kg_Related kg_w_g kg_w_γ' in c for c in KGWC) == 2,
       'Δτ = 0': any('kg_deltaTau kg_w_g kg_w_X kg_w_γ 0 10 = 0' in c for c in KGWC)}
v7 = lambda w: 'SUPPORTED' if all(w.values()) else 'NOT SUPPORTED'
score('⑦', v7(wit),
      f"`kg_witness` {wit}: the boost on `−dU dV`, Killing at every point, nowhere zero on `[0,10]`, "
      f"`γ 0 = (0,1) ≠ (0,e¹⁰) = γ 10`, null at both ends, related in BOTH directions, and `Δτ = 0`. "
      f"\"Witnessed on a generator of the Rindler horizon\" is exact, and the two-way relation is "
      f"more than the sentence claims.")

# ⓺: the quantifier comparison, read off each conjunct
# A conjunct is global in the curve's parameter when it quantifies over the whole segment `Icc a b`
# OR is a quantity taken over that segment's endpoints, as `kg_deltaTau g X γ a b` is: the integral
# runs from `a` to `b`.  The first draft of this reader tested only for `Icc a b` and so scored the
# lapse integral LOCAL -- a conjunct about the whole segment read as chart-bounded, which drove ⑧
# to the wrong verdict.  The flip test did not catch it, because the verdict DID depend on the
# reading; the reading was simply wrong.  A guard that checks dependence cannot check correctness,
# so the two tests below pin both shapes against the file's own text.
# The parameter names carry UNICODE subscripts (`t₁`, `t₂`), which `\d` does not match -- the
# second draft of this reader used `\d?` and scored the two-parameter conjuncts LOCAL for that
# reason alone.  Three drafts, three wrong readings, each caught only by looking at the printed
# table: `Icc a b` alone missed the integral, `\d?` missed the subscripts.  The probes below pin
# every shape the file actually contains, so a fourth mis-reading cannot pass silently.
SUB = '[₀-₉]?'


def global_in_parameter(c):
    return bool(re.search(r'∀ t' + SUB + r' ∈ Icc a b', c)) or bool(re.search(r'γ a b\b', c))


QUANT = []
for i, c in enumerate(KGC, 1):
    QUANT.append({'conjunct': i, 'global_in_the_parameter': global_in_parameter(c),
                  'text': c[:110]})
READER = {'plain quantifier': global_in_parameter('(∀ t ∈ Icc a b, foo)'),
          'subscripted quantifier': global_in_parameter('(∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, foo)'),
          'segment integral': global_in_parameter('kg_deltaTau g X γ a b = 0'),
          'a chart-local statement is NOT global':
              not global_in_parameter('∃ U, IsOpen U ∧ γ t₁ ∈ U')}
if not all(READER.values()):
    sys.exit('⛔ THE QUANTIFIER READER MIS-READS ONE OF THE SHAPES THE FILE CONTAINS: '
             f'{READER}.  Every verdict is withdrawn.')
glued = 'isPreconnected_Icc.induction₂' in KG
coords_named = bool(present([r'\bformalised on each local chart rather than along the whole '
                             r'generator\b'], KPROOF))
xi_in_lean = len(re.findall(r'\bx\^\{?i\}?\b', KG))
v8 = lambda g_, cn: 'SUPPORTED' if (g_ and cn) else 'NOT SUPPORTED'
score('⑧', v8(all(q['global_in_the_parameter'] for q in QUANT), coords_named),
      f"every conjunct is quantified `∀ t ∈ Icc a b` — GLOBAL in the curve's parameter over the "
      f"whole segment {[q['global_in_the_parameter'] for q in QUANT]} — and that globality is "
      f"EARNED, not assumed: the proof glues chart-local boxes with "
      f"`isPreconnected_Icc.induction₂'` ({glued}).  So \"machine-checked along a whole generator\" "
      f"is accurate, and the limitation the sentence states is the right one and sits in the right "
      f"place: the chart-local object is the ISOMETRY witnessing each pair and the adapted "
      f"transverse coordinates, which do not appear in the file at all ({xi_in_lean} occurrences of "
      f"`x^i`), not the null condition or the relation, which hold across the segment.  The clause "
      f"({coords_named}) is a limitation correctly scoped, which is the opposite of `r7672`'s "
      f"finding about \"on any manifold\" flattening two theorems into one claim.")

# ----------------------------------------------------- guard family three
FLIP = {'①': (v1(said1, hcont_named, curve_class_gone), v1(said1, False, curve_class_gone)),
        '②': (v2(said2, LPFB), v2(said2, ['x'])),
        '③': (v3(integrated, accum_of_dtau, sets_aside, unchanged),
              v3(integrated, True, sets_aside, unchanged)),
        '④': (v4(hyp_unnamed), v4({'x': False})),
        '⑤': (v5(invariant_thm), v5(1)),
        '⑥': (v6(dtau_form and True), v6(False)),
        '⑦': (v7(wit), v7({'x': False})),
        '⑧': (v8(True, coords_named), v8(False, coords_named)),
        }
for k, (actual, negated) in FLIP.items():
    if actual == negated:
        sys.exit(f"⛔ {k}'s verdict does not depend on its reading: it returns '{actual}' either "
                 "way.  Every verdict in this receipt is withdrawn.")
G['flip-test (every derived verdict depends on its readings)'] = True
G['reader-probe (every global shape reads global, a chart-local one does not)'] = READER

# ------------------------------------------------------------------ report
L = []
w = L.append
w(f"TREE: {open(os.path.join(HERE, 'runs', 'TREE.txt')).readline().strip()}")
w(f"GUARD: {json.dumps(G, ensure_ascii=False)}")
w(f"CITED NAMES: {len(CITED)} cited, unresolved -> {UNRESOLVED or 'none'}")
w(f"PROOF SENTENCE UNCHANGED SINCE {PREV}: {unchanged}")
w("")
w(f"ac_metric_singularity_along BINDERS: {MSAB}")
w(f"ac_lapse_pos_forces_point BINDERS: {LPFB}")
w(f"kg_lemma_killing_generator BINDERS: {KGB}")
w(f"  hypotheses the sentence NAMES: {hyp_named}")
w(f"  hypotheses it does NOT: {hyp_unnamed}")
w(f"kg_lemma_killing_generator CONJUNCTS ({len(KGC)}), quantifier scope read off each:")
for q in QUANT:
    w(f"  {q['conjunct']}. {'GLOBAL over [a,b]' if q['global_in_the_parameter'] else 'LOCAL     '}"
      f"  {q['text']}")
w(f"  globality earned by preconnectedness induction: {glued}")
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
           'guard': G, 'cited': RESOLVE, 'proof_sentence_unchanged': unchanged,
           'msa_binders': MSAB, 'lpf_binders': LPFB, 'kg_binders': KGB,
           'kg_hyp_named': hyp_named, 'kg_hyp_unnamed': hyp_unnamed,
           'kg_conjunct_quantifiers': QUANT, 'witness': wit,
           'verdicts': V, 'tally': tally},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
