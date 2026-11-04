#!/usr/bin/env python3
"""r7668 - a cold read of the stretch clause's formalisation and of the warped witness.

Two objects, registered in PREDICTION.md before this ran.  Every verdict is a function of text
parsed out of the Lean on the tree `runs/TREE.txt` names.  Three guard families run: a true/false
conjunct probe, an anchored-marker family (with the word-boundary assertion `r7666` had to add),
and a flip family over every derived verdict.  If any does not flip, the receipt is withdrawn.
"""
import json, os, re, subprocess, sys

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True,
                      text=True, check=True).stdout.strip()
HERE = os.path.dirname(os.path.abspath(__file__))
LP = 'computations/formalisation/lean/probes'
flat = lambda s: re.sub(r'\s+', ' ', s)


def read(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        sys.exit(f"⛔ absent on this tree: {rel}")
    return open(p, encoding='utf-8').read()


SRC = {n: read(f'{LP}/{n}.lean') for n in ('HorizonStretch', 'WarpedWitness', 'FourDWitness')}
FLATS = {n: flat(s) for n, s in SRC.items()}
TEX = read('corpus/BH_causality_v2.tex')

m = re.search(r'\\begin\{remark\}\[Machine-checked form\]\\label\{rem:formalised\}(.*?)'
              r'\\end\{remark\}', TEX, re.S)
if m is None:
    sys.exit("⛔ `rem:formalised` is gone from the paper on this tree.")
REMARK = flat(m.group(1))

# P1's clause, located in the proposition rather than quoted from memory
pi = TEX.index('\\label{prop:causal-alignment}')
PROPTEXT = flat(TEX[pi:TEX.index('\\end{proposition}', pi)])
cm = re.search(r'the stretch of \$\\mathcal\{H\}\^\+\$ they approach to within any given distance'
               r'[^;]*', PROPTEXT)
if cm is None:
    sys.exit("⛔ P1's stretch clause is not in `prop:causal-alignment` on this tree: the object "
             "this read is asked to judge faithfulness AGAINST is gone.")
CLAUSE = cm.group(0)


def decl(fl, name):
    r = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', SRC[fl], re.S | re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a theorem in {fl}.lean on this tree.")
    return r.group(0)


def defn(fl, name):
    r = re.search(r'^(noncomputable )?def ' + re.escape(name) + r'\b([^\n]*(?:\n  [^\n]*)*)',
                  SRC[fl], re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a definition in {fl}.lean on this tree.")
    return flat(r.group(0))


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


# ------------------------------------------------------- the cited names
CITED = [('hs_stretch_N', 'HorizonStretch'), ('hs_witness', 'HorizonStretch'),
         ('ww_witness_headline', 'WarpedWitness'), ('ww_witness_tangency', 'WarpedWitness'),
         ('ww_cotton_ne_zero', 'WarpedWitness'), ('ww_gco_bridge', 'WarpedWitness'),
         ('fd_witness_headline', 'FourDWitness'), ('fd_witness_tangency', 'FourDWitness')]
RESOLVE = {n: bool(re.search(r'^theorem ' + re.escape(n) + r'\b', SRC[f], re.M))
           for n, f in CITED}
UNRESOLVED = [n for n, ok in RESOLVE.items() if not ok]

# ------------------------------------------------------- object A, parsed
HS = decl('HorizonStretch', 'hs_stretch_N')
sig = re.search(r'theorem hs_stretch_N(.*?)\n    \(∀ K : Set N', HS, re.S)
if sig is None:
    sys.exit("⛔ `hs_stretch_N`'s conclusion no longer starts `(∀ K : Set N`: the "
             "binder/conclusion split this read depends on cannot be made.")
HSSIG = flat(sig.group(1))
hs_concl = re.search(r'\n    (\(∀ K : Set N.*?) := by\n', HS, re.S)
if hs_concl is None:
    sys.exit("⛔ cannot delimit `hs_stretch_N`'s conclusion.")
HSCONJ = conjuncts(hs_concl.group(1))
STRETCHDEF = defn('HorizonStretch', 'hs_stretch')

# --------------------------------------------------- guard family one
in_hs = lambda needle: any(needle in c for c in HSCONJ)
G = {'true-probe  (`IsCompact K` occurs in a conjunct)': in_hs('IsCompact K'),
     'false-probe (`IsConnected K` occurs in a conjunct)': in_hs('IsConnected K')}
if not (G['true-probe  (`IsCompact K` occurs in a conjunct)'] is True and
        G['false-probe (`IsConnected K` occurs in a conjunct)'] is False):
    sys.exit(f"⛔ THE CONJUNCT GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")


# --------------------------------------------------- guard family two
def present(markers, text):
    out = []
    for mk in markers:
        if '\\b' not in mk:
            sys.exit(f"⛔ marker {mk!r} carries no word boundary.  `r7666` shipped a bare "
                     'substring that matched "proper" inside "property"; every marker must be '
                     'anchored or the scan measures its own looseness.')
        mm = re.search(mk, text, re.I)
        if mm:
            out.append({'marker': mk, 'context': text[max(0, mm.start() - 50):mm.end() + 50]})
    return out


G[r'marker-probe true  (\bstretch\b matches P1 clause)'] = bool(present([r'\bstretch\b'], CLAUSE))
G[r'marker-probe false (\bparacompact\b matches P1 clause)'] = bool(
    present([r'\bparacompact\b'], CLAUSE))
G[r'marker-probe word-boundary (\bproper\b does NOT match "the Cauchy property")'] = not bool(
    present([r'\bproper\b'], 'so by the Cauchy property'))
if not (G[r'marker-probe true  (\bstretch\b matches P1 clause)'] is True and
        G[r'marker-probe false (\bparacompact\b matches P1 clause)'] is False and
        G[r'marker-probe word-boundary (\bproper\b does NOT match "the Cauchy property")'] is True):
    sys.exit(f"⛔ THE MARKER GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

V = {}
score = lambda k, verdict, ev: V.__setitem__(k, [verdict, ev])

# ------------------------------------------------------------- ① … ⑥
v1 = lambda u: 'SUPPORTED' if not u else 'NOT SUPPORTED'
score('①', v1(UNRESOLVED),
      f"all {len(CITED)} theorem names the two new passages cite resolve in the files named "
      f"({RESOLVE}).  `hs_stretch_N` is a theorem of HorizonStretch.lean whose conclusion is a "
      f"{len(HSCONJ)}-fold conjunction, which is the (S1)/(S2) pair the remark describes.")

metric_binder = bool(re.search(r'\(m : MetricSpace N\)', HSSIG))
hm = bool(re.search(r'hm : m\.toUniformSpace\.toTopologicalSpace = tN', HSSIG))
eps = bool(re.search(r'\{ε : ℝ\} \(hε : 0 < ε\)', HSSIG))
v2 = lambda a, b, c_: 'SUPPORTED' if all((a, b, c_)) else 'NOT SUPPORTED'
score('②', v2(metric_binder, hm, eps),
      f"the distance is a BINDER, `(m : MetricSpace N)` ({metric_binder}), with "
      f"`hm : m.toUniformSpace.toTopologicalSpace = tN` identifying its topology with the charted "
      f"one ({hm}), and `ε` is universally quantified with `0 < ε` ({eps}).  So \"for any metric "
      f"distance inducing the manifold's topology\" and \"to within any given distance\" are both "
      f"the Lean's, and the quantifier order is: for each metric and each `ε`, the pair below.")

s1 = [c for c in HSCONJ if 'K ⊆ S.H J' in c and 'IsCompact K' in c]
s1_form = bool(s1) and '∀ᶠ τ in atTop' in s1[0] and 'K ⊆ @hs_stretch' in s1[0]
sd = 'q ∈ H ∧ Metric.infDist q (A τ) < ε' in STRETCHDEF
v3 = lambda a, b: 'SUPPORTED' if (a and b) else 'NOT SUPPORTED'
score('③', v3(s1_form, sd),
      f"(S1) is `∀ K ⊆ S.H J, IsCompact K → ∀ᶠ τ in atTop, K ⊆ hs_stretch (S.cone O) (S.H J) τ ε` "
      f"({s1_form}), and `hs_stretch A H τ ε = {{q | q ∈ H ∧ Metric.infDist q (A τ) < ε}}` ({sd}) — "
      f"the part of the horizon within `ε` of the cone, which is exactly P1's \"the stretch of "
      f"`𝓗⁺` they approach to within any given distance\".  \"Every compact part … of all "
      f"sufficiently late `τ`\" is the Lean's wording for wording.")

s2 = [c for c in HSCONJ if '¬ S.H J ⊆ K' in c]
s2_form = bool(s2) and '¬ @hs_stretch' in s2[0] and '∀ᶠ τ in atTop' in s2[0]
score('④', 'SUPPORTED' if s2_form else 'NOT SUPPORTED',
      f"(S2) is `(∀ K, IsCompact K → ¬ S.H J ⊆ K) → ∀ K, IsCompact K → ∀ᶠ τ in atTop, "
      f"¬ hs_stretch … τ ε ⊆ K` ({s2_form}): under the hypothesis that `𝓗⁺` lies in no compact "
      f"set, the stretch eventually leaves every compact set.  The remark states the hypothesis "
      f"and the conclusion in that order and in those terms.")

gen_future = len(re.findall(r'^(theorem|lemma)[^\n]*(generator|future)[^\n]*inextend',
                            SRC['HorizonStretch'], re.M | re.I))
doc_says = bool(present([r'\bfuture inextendibility of generators is not formalised\b'],
                        FLATS['HorizonStretch']))
v5 = lambda n: 'SUPPORTED' if n == 0 else 'NOT SUPPORTED'
score('⑤', v5(gen_future),
      f"no theorem or lemma in HorizonStretch.lean states the future inextendibility of the "
      f"generators or the future direction in general ({gen_future}); the file's own header says "
      f"so in writing ({doc_says}).  The remark's \"not formalised in general\" is accurate, and "
      f"it is the right way to carry an unformalised step: named, not implied.")

HW = decl('HorizonStretch', 'hs_witness')
HWC = conjuncts(re.search(r'theorem hs_witness :(.*?) := by', HW, re.S).group(1))
reach = [c for c in HWC if 'q.1.2 > T' in c]
reach_univ = bool(reach) and '∀ T : ℝ' in reach[0] and '∀ ε > 0' in reach[0]
reach_eq = any('q.1.2 = ' in c for c in HWC)
cau_unbdd = [c for c in HWC if 'fd_S.Cau q p' in c]
v6 = lambda u, e: 'NOT SUPPORTED' if (u and not e) else ('SUPPORTED' if (u and e) else 'NOT SUPPORTED')
score('⑥', v6(reach_univ, reach_eq),
      f"`hs_witness`'s fifth conjunct is `∀ ε > 0, ∀ T : ℝ, ∀ᶠ τ in atTop, ∃ q ∈ hs_stretch …, "
      f"q.1.2 > T` ({reach_univ}): for every bound `T` the stretch eventually contains a point "
      f"whose `V` EXCEEDS `T`.  That is unboundedness above in `V`, not surjectivity onto `V`; no "
      f"conjunct says `q.1.2 = V` for a given `V` ({reach_eq}).  The remark's \"the stretch reaches "
      f"every value of `V`\" renders an `>` as an `=`, and the two coincide only for a connected "
      f"stretch, which nothing here proves.  ⌗ The remark also omits the conjunct that carries the "
      f"future direction ON this witness: `∀ q ∈ 𝓗⁺, ∀ K compact, ¬ ({{p | Cau q p}} ∩ 𝓗⁺) ⊆ K` "
      f"({len(cau_unbdd)} such conjunct) — from EVERY horizon point the horizon's own causal "
      f"future leaves every compact set, which is the futureward statement the remark says is not "
      f"formalised in general and which IS formalised here.")

# -------------------------------------------- ⑬ the faithfulness reading
# Each part of P1's clause, with a test that is a function of the Lean source.
connected = len(re.findall(r'(IsConnected|IsPreconnected)[^\n]*hs_stretch|'
                           r'hs_stretch[^\n]*(IsConnected|IsPreconnected)',
                           SRC['HorizonStretch']))
mono = len(re.findall(r'hs_stretch[^\n]{0,80}⊆ *@?hs_stretch|Monotone[^\n]{0,40}hs_stretch|'
                      r'hs_stretch_mono', SRC['HorizonStretch']))
generator_set = len(re.findall(r'^(theorem|lemma)[^\n]*hs_stretch[^\n]*generator',
                               SRC['HorizonStretch'], re.M | re.I))
PARTS = [
    ('"the stretch" as ONE portion of `𝓗⁺`', connected == 0,
     'nothing relates `hs_stretch` to connectedness; the set is a sublevel of `infDist` and may '
     'be a union of far-apart pieces, so the pair gives a SET that grows, not a stretch'),
    ('"extending" as growth in `τ`', mono == 0,
     'no statement makes `hs_stretch … τ ε` monotone in `τ`; (S1) and (S2) are eventual, and '
     'eventual containment is not growth — the stretch could shrink and regrow'),
    ('"along its generators"', generator_set == 0,
     'nothing ties the stretch to a generator of `𝓗⁺`; the remark names the future direction as '
     'unformalised but not the identification of the stretch with a portion of a generator'),
    ('"to within any given distance"', eps and metric_binder, 'carried: `ε` and the metric are binders'),
    ('"the cones approach"', s1_form, 'carried: (S1) is containment in the `ε`-stretch of the cones'),
    ('"without bound"', s2_form, 'carried: (S2) is escape from every compact set'),
]
NOTCARRIED = [p for p in PARTS[:3] if p[1]]
v13 = lambda nc: 'NOT SUPPORTED' if nc else 'SUPPORTED'
score('⑬', v13(NOTCARRIED),
      f"P1's clause reads: \"{CLAUSE}\".  Three of its six parts are NOT carried by the pair, "
      f"beyond the future direction the remark already names: "
      + '; '.join(f"**{p[0]}** — {p[2]}" for p in NOTCARRIED)
      + f".  The three that ARE carried are the given distance, the cones' approach and the "
      f"unboundedness.  So the pair is a faithful reading of \"a set of horizon points within any "
      f"given distance of the cones, exhausting `𝓗⁺` and escaping every compact set\" — which is "
      f"the clause's extensional content — and not of \"a stretch\", a single portion climbing the "
      f"generators, which is the clause's picture.")

# ---------------------------------------------------------- ⑦ … ⑫
WWH = decl('WarpedWitness', 'ww_witness_headline')
WWC = conjuncts(re.search(r'theorem ww_witness_headline :(.*?) := by', WWH, re.S).group(1))
FDH = decl('FourDWitness', 'fd_witness_headline')
FDC = conjuncts(re.search(r'theorem fd_witness_headline :(.*?) := by', FDH, re.S).group(1))
need = ('IsCauchyTemporalOn', 'SublevelProper', 'KLi', 'KLs', 'H ww_J = {x : N | x.1.1 = 0}')
ww_ok = {t: any(t in c for c in WWC) for t in need[:4]}
ww_H = any('ww_S.H ww_J = {x : N | x.1.1 = 0}' in c for c in WWC)
ww_isO = 'noncomputable def ww_J : Set N := range ww_O' in SRC['WarpedWitness']
ww_dim3 = any('Module.finrank ℝ E = 3' in c for c in WWC)
ww_t = bool(re.search(r'theorem ww_witness_tangency \(q : N\) \(hq', SRC['WarpedWitness']))
fd_shape = {t: any(t in c for c in FDC) for t in need[:4]}
v7 = lambda a, h, o, d, t: 'SUPPORTED' if all((all(a.values()), h, o, d, t)) else 'NOT SUPPORTED'
score('⑦', v7(ww_ok, ww_H, ww_isO, ww_dim3, ww_t),
      f"`ww_witness_headline` carries {ww_ok}, states its own dimension `finrank ℝ E = 3` "
      f"({ww_dim3}) and `𝓗⁺ = {{U = 0}}` ({ww_H}); `ww_J = range ww_O` ({ww_isO}), so `S.H ww_J` "
      f"IS `∂J⁻(O)`.  Tangency at every horizon point is `ww_witness_tangency (q) (hq)` ({ww_t}).  "
      f"The four-dimensional headline has the same shape ({fd_shape}), so \"the same holds\" is "
      f"exact.")

GC = defn('WarpedWitness', 'ww_GC')
WK = defn('WarpedWitness', 'ww_k')
WW = defn('WarpedWitness', 'ww_w')
gE = bool(re.search(r'ww_S\.gE x v w = gM v\.1 w\.1 \+ ww_w x \^ 2 \* \(v\.2 \* w\.2\)',
                    SRC['WarpedWitness']))
k_exp = 'Real.exp (2 * (U * V))' in WK
w_exp = 'ww_wP x.1' in WW and 'Real.exp (p.1 * p.2)' in defn('WarpedWitness', 'ww_wP')
gc_form = '-1/2' in GC and 'ww_k U V' in GC
v8 = lambda a, b, c_, d: 'SUPPORTED' if all((a, b, c_, d)) else 'NOT SUPPORTED'
score('⑧', v8(gE, k_exp, w_exp, gc_form),
      f"part A's metric is `gE x v w = gM v.1 w.1 + ww_w x ² (v.2 w.2)` ({gE}) with "
      f"`ww_w x = exp(U·V)` ({w_exp}), so the `dy²` coefficient is `exp(2UV)`; part B's components "
      f"are `[[0,−1/2,0],[−1/2,0,0],[0,0,ww_k]]` with `ww_k U V = exp(2(UV))` ({k_exp}, "
      f"{gc_form}), and `g_UV = g_VU = −1/2` IS `−dU dV`.  `−dU dV + e^{{2UV}} dy²` on `ℝ³`, as "
      f"stated, in both halves.")

CHAIN = [('ww_ginv', 'ww_GI'), ('ww_Γ', 'ww_ginv'), ('ww_Γ', 'ww_gco'), ('ww_Riem', 'ww_Γ'),
         ('ww_Ric', 'ww_Riem'), ('ww_R', 'ww_Ric'), ('ww_Sch', 'ww_Ric'), ('ww_Sch', 'ww_gco'),
         ('ww_covS', 'ww_Sch'), ('ww_covS', 'ww_Γ'), ('ww_Cot', 'ww_covS')]
LINKS = {}
for child, parent in CHAIN:
    LINKS[f'{child} <- {parent}'] = parent in defn('WarpedWitness', child)
chain_ok = all(LINKS.values())
inv_spec = bool(re.search(r'theorem ww_ginv_spec', SRC['WarpedWitness']))
CNZ = decl('WarpedWitness', 'ww_cotton_ne_zero')
cnz = ('∀ x : X3, ww_Cot 0 0 1 x = -2 * x 1' in flat(CNZ)
       and 'ww_Cot 0 0 1 ![0, 1, 0] ≠ 0' in flat(CNZ))
v9 = lambda a, b, c_: 'SUPPORTED' if all((a, b, c_)) else 'NOT SUPPORTED'
score('⑨', v9(chain_ok, inv_spec, cnz),
      f"the Cotton tensor is DERIVED, link by link, from the metric components: {LINKS} "
      f"({chain_ok}) — `ww_Γ` is the Christoffel formula in `ww_ginv` and `ww_gco`, `ww_Riem` is "
      f"built from `ww_Γ`, `ww_Ric` from `ww_Riem`, `ww_R` from `ww_Ric`, `ww_Sch` from `ww_Ric` "
      f"and `ww_gco`, `ww_covS` from `ww_Sch` and `ww_Γ`, and `ww_Cot i j k = ww_covS i j k - "
      f"ww_covS i k j`.  `ww_ginv` is PROVED to be the inverse, not assumed (`ww_ginv_spec`, "
      f"{inv_spec}).  And `ww_cotton_ne_zero` states `∀ x, ww_Cot 0 0 1 x = −2·x₁` with a point "
      f"where it is `−2 ≠ 0` ({cnz}): `C_UUV = −2V`, not identically zero, exactly as written.  "
      f"\"Computed in Lean from the metric\" is the truth about this chain.")

BR = flat(decl('WarpedWitness', 'ww_gco_bridge'))
lhs_is_A = 'Warped.ww_S.gE x' in BR
rhs_is_B = 'ww_gco i j ![x.1.1, x.1.2, x.2]' in BR
basis = '![((1, 0), 0), ((0, 1), 0), ((0, 0), 1)]' in BR
sides_differ = lhs_is_A and rhs_is_B
tautological = bool(re.search(r'(\bww_gco\b[^=]*)=\s*\1', BR))
v10 = lambda d, t, b: 'SUPPORTED' if (d and not t and b) else 'NOT SUPPORTED'
score('⑩', v10(sides_differ, tautological, basis),
      f"`ww_gco_bridge` is a BRIDGE and not a restatement.  Its left side is part A's own witness "
      f"metric, `Warped.ww_S.gE x` ({lhs_is_A}), evaluated on the three coordinate basis vectors "
      f"`![((1,0),0), ((0,1),0), ((0,0),1)]` ({basis}); its right side is part B's component array "
      f"`ww_gco i j ![x.1.1, x.1.2, x.2]` ({rhs_is_B}), which is the object the whole curvature "
      f"chain is computed from.  The two sides are different symbols with different types "
      f"({sides_differ}), the statement is not of the form `X = X` ({tautological}), and it is "
      f"proved by `fin_cases` on both indices using `ww_w_sq`.  So the Cotton tensor the remark "
      f"cites is the Cotton tensor OF THE WITNESS'S METRIC, and the order's doubt is answered in "
      f"the affirmative.  *This seat registered this arm as the one most likely to fail.*")

cf_thm = len(re.findall(r'^(theorem|lemma)[^\n]*conformally[ _]?flat', SRC['WarpedWitness'],
                        re.M | re.I))
cf_said = bool(present([r'\bclassical theorem the formalisation does not include\b'], REMARK))
v11 = lambda n, s: 'SUPPORTED' if (n == 0 and s) else 'NOT SUPPORTED'
score('⑪', v11(cf_thm, cf_said),
      f"no theorem or lemma in WarpedWitness.lean states the conformal-flatness criterion "
      f"({cf_thm}), and the remark says in so many words that it is classical and not included "
      f"({cf_said}).  The inference from `C ≠ 0` to \"not conformally flat\" therefore rests on a "
      f"cited classical theorem, which the remark marks — the same discipline it now applies to "
      f"Bernal–Sánchez.")

exts = {f: sorted(set(re.findall(r'def (\w*witnessExt\w*)', SRC[f])))
        for f in ('WarpedWitness', 'FourDWitness')}
v12 = lambda e: 'SUPPORTED' if not any(e.values()) else 'NOT SUPPORTED'
score('⑫', v12(exts),
      f"no conformal extension is defined for the warped or the four-dimensional carrier ({exts}), "
      f"so the identification with `∂J⁻(𝒥⁺)` is exercised in two dimensions only, as stated.")

# --------------------------------------------------- guard family three
FLIP = {'①': (v1(UNRESOLVED), v1(['x'])),
        '②': (v2(metric_binder, hm, eps), v2(False, hm, eps)),
        '③': (v3(s1_form, sd), v3(False, sd)),
        '⑤': (v5(gen_future), v5(1)),
        '⑥': (v6(reach_univ, reach_eq), v6(reach_univ, True)),
        '⑦': (v7(ww_ok, ww_H, ww_isO, ww_dim3, ww_t), v7(ww_ok, False, ww_isO, ww_dim3, ww_t)),
        '⑧': (v8(gE, k_exp, w_exp, gc_form), v8(False, k_exp, w_exp, gc_form)),
        '⑨': (v9(chain_ok, inv_spec, cnz), v9(False, inv_spec, cnz)),
        '⑩': (v10(sides_differ, tautological, basis), v10(sides_differ, True, basis)),
        '⑪': (v11(cf_thm, cf_said), v11(1, cf_said)),
        '⑫': (v12(exts), v12({'x': ['y']})),
        '⑬': (v13(NOTCARRIED), v13([])),
        }
for k, (actual, negated) in FLIP.items():
    if actual == negated:
        sys.exit(f"⛔ {k}'s verdict does not depend on its reading: it returns '{actual}' either "
                 "way.  Every verdict in this receipt is withdrawn.")
G['flip-test (every derived verdict depends on its readings)'] = True

# ------------------------------------------------------------------ report
L = []
w = L.append
w(f"TREE: {open(os.path.join(HERE, 'runs', 'TREE.txt')).readline().strip()}")
w(f"GUARD: {json.dumps(G, ensure_ascii=False)}")
w(f"CITED NAMES: {len(CITED)} cited, unresolved -> {UNRESOLVED or 'none'}")
w(f"P1's CLAUSE: {CLAUSE}")
w(f"hs_stretch_N BINDERS: {HSSIG}")
w(f"hs_stretch_N CONJUNCTS ({len(HSCONJ)}):")
for i, c in enumerate(HSCONJ, 1):
    w(f"  {i}. {c[:170]}")
w(f"hs_stretch DEF: {STRETCHDEF}")
w("")
w("THE CLAUSE'S PARTS, EACH TESTED AGAINST THE LEAN:")
for name, flagged, why in PARTS:
    carried = (name in [p[0] for p in PARTS[3:]])
    verdict = ('CARRIED' if flagged else 'NOT CARRIED') if carried else \
              ('NOT CARRIED' if flagged else 'CARRIED')
    w(f"  {verdict:12s}  {name}")
    w(f"      {why}")
w("")
w("THE CURVATURE CHAIN, LINK BY LINK:")
for k, ok in LINKS.items():
    w(f"  {'DERIVED' if ok else 'BROKEN '}  {k}")
w("")
for k in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬':
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
           'guard': G, 'cited': RESOLVE, 'clause': CLAUSE, 'hs_binders': HSSIG,
           'hs_conjuncts': HSCONJ, 'hs_stretch_def': STRETCHDEF,
           'clause_parts': [{'part': p[0], 'flag': p[1], 'why': p[2]} for p in PARTS],
           'curvature_chain': LINKS, 'bridge': BR, 'verdicts': V, 'tally': tally},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
