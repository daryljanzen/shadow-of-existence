#!/usr/bin/env python3
"""r7670 - two cold reads: the two-step stretch and the densities corollary, and the reading of Δτ.

Registered in PREDICTION.md before this ran.  Object A's verdicts are functions of text parsed out
of the Lean; object B's are functions of P1's own SENTENCES, enumerated from the paper rather than
taken from the ruling that asks about them.  Three guard families must flip or the receipt is
withdrawn.
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


SRC = {n: read(f'{LP}/{n}.lean') for n in ('HorizonStretch', 'GeneratorStretch', 'Densities')}
ALL = '\n'.join(SRC.values())
TEX = read('corpus/BH_causality_v2.tex')
FTEX = flat(TEX)
SENTS = re.split(r'(?<=[.!?]) ', FTEX)

m = re.search(r'\\begin\{remark\}\[Machine-checked form\]\\label\{rem:formalised\}(.*?)'
              r'\\end\{remark\}', TEX, re.S)
if m is None:
    sys.exit("⛔ `rem:formalised` is gone from the paper on this tree.")
REMARK = flat(m.group(1))
if 'carried in two steps' not in REMARK:
    sys.exit("⛔ the two-step stretch passage is not in `rem:formalised` on this tree: the first "
             "object of this read is gone.")
cor = re.search(r'\\begin\{corollary\}\[Finite densities\]\\label\{cor:densities\}(.*?)'
                r'\\end\{proof\}', TEX, re.S)
if cor is None:
    sys.exit("⛔ `cor:densities` and its proof are gone on this tree.")
COR = flat(cor.group(1))


def decl(fl, name):
    r = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', SRC[fl], re.S | re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a theorem in {fl}.lean on this tree.")
    return r.group(0)


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


CITED = [('hs_stretch_N', 'HorizonStretch'), ('hs_witness', 'HorizonStretch'),
         ('gs_segment_stretch', 'GeneratorStretch'), ('gs_future_stretch', 'GeneratorStretch'),
         ('gs_witness', 'GeneratorStretch'), ('dn_cor_densities', 'Densities'),
         ('dn_witness', 'Densities')]
RESOLVE = {n: bool(re.search(r'^theorem ' + re.escape(n) + r'\b', SRC[f], re.M)) for n, f in CITED}
UNRESOLVED = [n for n, ok in RESOLVE.items() if not ok]

GS = decl('GeneratorStretch', 'gs_segment_stretch')
GF = decl('GeneratorStretch', 'gs_future_stretch')
GW = decl('GeneratorStretch', 'gs_witness')
DN = decl('Densities', 'dn_cor_densities')
DW = decl('Densities', 'dn_witness')
HS = decl('HorizonStretch', 'hs_stretch_N')

hfg = re.search(r'def HasFutureGenerators \(J : Set N\) : Prop :=(.*?)\n\n',
                SRC['GeneratorStretch'], re.S)
if hfg is None:
    sys.exit("⛔ `HasFutureGenerators` is not defined in GeneratorStretch.lean: step two's "
             "hypothesis cannot be read.")
HFG = flat(hfg.group(1))

# ------------------------------------------------------- guard family one
DNC = conjuncts(re.search(r'\n    (\(∀ Θ τ.*?) :=\n', DN, re.S).group(1))
in_dn = lambda needle: any(needle in c for c in DNC)
G = {'true-probe  (`S.slice J Θ τ` occurs in a conjunct)': in_dn('S.slice J Θ τ'),
     'false-probe (`S.IsCauchyTemporalOn` occurs in a conjunct)': in_dn('S.IsCauchyTemporalOn')}
if not (G['true-probe  (`S.slice J Θ τ` occurs in a conjunct)'] is True and
        G['false-probe (`S.IsCauchyTemporalOn` occurs in a conjunct)'] is False):
    sys.exit(f"⛔ THE CONJUNCT GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")


# ------------------------------------------------------- guard family two
def present(markers, text):
    """Every marker must be ANCHORED, and there are exactly two ways to be.

    `r7666` shipped a bare substring that matched "proper" inside "property", so a prose marker
    must carry `\\b`.  A LaTeX-formula marker cannot: `ds^{2}=g(\\chi,\\chi)` has no word
    boundary anywhere in it.  It is anchored a different way — it contains an escaped control
    sequence (`\\\\chi`), which cannot occur inside a word.  Anything carrying neither is
    refused, so the exemption cannot be used to smuggle a bare substring back in.
    """
    out = []
    for mk in markers:
        if '\\b' not in mk and '\\\\' not in mk:
            sys.exit(f"⛔ marker {mk!r} is unanchored: it carries neither a word boundary nor an "
                     'escaped LaTeX control sequence.  `r7666` shipped a bare substring that '
                     'matched "proper" inside "property"; every marker must be anchored one way '
                     'or the other or the scan measures its own looseness.')
        mm = re.search(mk, text, re.I)
        if mm:
            out.append({'marker': mk, 'context': text[max(0, mm.start() - 50):mm.end() + 50]})
    return out


G[r'marker-probe true  (\btwo steps\b in the passage)'] = bool(present([r'\btwo steps\b'], REMARK))
G[r'marker-probe false (\bparacompact\b in the passage)'] = bool(
    present([r'\bparacompact\b'], REMARK))
G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] = not bool(
    present([r'\bproper\b'], 'so by the Cauchy property'))
# the formula path is anchored too: a control-sequence marker must not match a truncated variant
G['marker-probe formula (a control-sequence marker does not match a truncation)'] = (
    bool(present([r'ds\^\{2\}=g\(\\chi,\\chi\)'], r'ds^{2}=g(\chi,\chi)\,d\lambda^{2}'))
    and not bool(present([r'ds\^\{2\}=g\(\\chi,\\chi\)'], r'ds^{2}=g(\chi,\xi)')))
if not all((G[r'marker-probe true  (\btwo steps\b in the passage)'] is True,
            G[r'marker-probe false (\bparacompact\b in the passage)'] is False,
            G[r'marker-probe word-boundary (\bproper\b not in "the Cauchy property")'] is True,
            G['marker-probe formula (a control-sequence marker does not match a truncation)'] is True)):
    sys.exit(f"⛔ THE MARKER GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

V = {}
score = lambda k, verdict, ev: V.__setitem__(k, [verdict, ev])

# ================================================== OBJECT A
v1 = lambda u: 'SUPPORTED' if not u else 'NOT SUPPORTED'
score('①', v1(UNRESOLVED),
      f"all {len(CITED)} names the two passages cite resolve in the files named ({RESOLVE}).  The "
      f"passage's \"two steps\" are `hs_stretch_N` and the `gs_` pair, and that is how they stand "
      f"in the Lean: `gs_segment_stretch` calls `(hs_stretch_N …).1` on a compact segment, so step "
      f"two is built ON step one rather than beside it.")

stretch_word = len(present([r'\bthe stretch of \$\\mathcal\{H\}\^\+\$'], REMARK))
set_of_points = len(present([r'\bthe set of horizon points within that distance\b'], REMARK))
hsconj = conjuncts(re.search(r'\n    (\(∀ K : Set N.*?) := by\n', HS, re.S).group(1))
v2 = lambda sp: 'SUPPORTED' if sp else 'NOT SUPPORTED'
score('②', v2(set_of_points),
      f"step one's sentence now says \"the set of horizon points within that distance\" "
      f"({set_of_points} occurrence(s)) where the earlier version said \"the stretch\".  That is "
      f"`hs_stretch`'s actual content — a sublevel set of `infDist` within `𝓗⁺` — and the change "
      f"is `r7668`'s ⑬ repaired at the root: the noun no longer claims a connectedness the Lean "
      f"does not prove.  `hs_stretch_N`'s two conjuncts are unchanged ({len(hsconj)} of them).")

causal_in_hfg = 'S.Cau q (γ t)' in HFG
cont_only = 'ContinuousOn γ (Ici 0)' in HFG
no_cstep = 'CStep' not in HFG and 'ContMDiff' not in HFG
gs_binders_named = all(h in GS for h in ('hG : S.HasFutureGenerators J', 'm : MetricSpace N'))
gf_same = all(h in GF for h in ('hG : S.HasFutureGenerators J', 'm : MetricSpace N'))
seg = 'γ \'\' Icc 0 t₀ ⊆ @hs_stretch' in flat(GS)
fut = '∃ p ∈ @hs_stretch' in flat(GF) and 'S.Cau q p ∧ p ∉ K' in flat(GF)
v3 = lambda a, b, c_, d: 'NOT SUPPORTED' if (a and b and c_ and d) else 'SUPPORTED'
score('③', v3(cont_only, no_cstep, seg, fut),
      f"the two conclusions are the sentence's: every finite segment `γ''[0,t₀]` inside the "
      f"`ε`-stretch ({seg}), and a point of `J⁺(q) ∩ 𝓗⁺` in the stretch outside any compact `K` "
      f"({fut}); the binders are `hs_stretch_N`'s plus `hG` and nothing else ({gs_binders_named}, "
      f"{gf_same}).  But the HYPOTHESIS is weaker than the sentence states.  "
      f"`HasFutureGenerators` is `{HFG[:210]}…` — it asks for a CONTINUOUS `γ` ({cont_only}) with "
      f"each `γ t` in `𝓗⁺` and causally after `q` ({causal_in_hfg}), and NOTHING relating `γ t` to "
      f"`γ t'` for `0 < t < t'`: no `CStep`, no `ContMDiff` ({no_cstep}), and its own docstring "
      f"calls it \"purely topological\".  The sentence says \"a future-directed causal curve runs "
      f"in `𝓗⁺`\", which is strictly more than that.  The Lean is therefore STRONGER than "
      f"advertised, and a reader who supplies only the paper's hypothesis would be supplying more "
      f"than the theorem needs.")

achronal = len(re.findall(r'(?i)achronal', ALL))
hfg_thm = len(re.findall(r'^theorem[^\n]*: *S?\.?HasFutureGenerators', SRC['GeneratorStretch'], re.M))
v4 = lambda a: 'SUPPORTED' if a == 0 else 'NOT SUPPORTED'
score('④', v4(achronal),
      f"the word \"achronal\" does not occur once in the three probe files ({achronal}), so no "
      f"theorem derives `HasFutureGenerators` from an achronal-boundary argument; it is a NAMED "
      f"hypothesis, discharged only on a witness ({hfg_thm} theorem(s) concluding it).  The "
      f"passage's \"which the formalisation does not include in general\" is accurate, and naming "
      f"the standard result rather than gesturing at it is the right way to carry the gap.")

GWC = conjuncts(re.search(r'theorem gs_witness :(.*?) := by', GW, re.S).group(1))
gw_proves = any('HasFutureGenerators' in c for c in GWC)
gw_future = any('∃ p ∈ hs_stretch' in c for c in GWC)
gen_exhibited = bool(re.search(r'def gs_gen \(q : N\) \(s : ℝ\) : N := \(\(q\.1\.1, q\.1\.2 \+ s\), q\.2\)',
                               SRC['GeneratorStretch']))
hw = decl('HorizonStretch', 'hs_witness')
bound_V = 'q.1.2 > T' in flat(hw)
v5 = lambda a, b, c_: 'SUPPORTED' if all((a, b, c_)) else 'NOT SUPPORTED'
score('⑤', v5(gw_proves, gw_future, gen_exhibited),
      f"`gs_witness` PROVES `fd_S.HasFutureGenerators fd_J` on the four-dimensional witness "
      f"({gw_proves}) and carries the futureward conclusion ({gw_future}); the curve is exhibited, "
      f"`gs_gen q s = ((U, V + s), y, z)` ({gen_exhibited}), translation along the generator "
      f"direction.  So \"on the four-dimensional witness below it is proved\" is exact and not a "
      f"restatement of `hs_witness`, whose own `V`-bound conjunct is `q.1.2 > T` ({bound_V}) — the "
      f"`>` the passage now renders as \"exceeds every bound in `V`\", which is `r7668`'s ⑥ "
      f"repaired.")

mono = len(re.findall(r'hs_stretch[^\n]{0,80}⊆ *@?hs_stretch|Monotone[^\n]{0,40}hs_stretch|'
                      r'hs_stretch_mono', ALL))
disclaim = len(present([r'\bnot that the stretch grows monotonically with \$\\tau\$'], REMARK))
v6 = lambda mo, d: 'SUPPORTED' if (mo == 0 and d) else 'NOT SUPPORTED'
score('⑥', v6(mono, disclaim),
      f"no statement anywhere makes the stretch monotone in `τ` ({mono}), and the passage now says "
      f"so itself ({disclaim} occurrence(s) of the disclaimer).  `r7668`'s second uncarried part is "
      f"carried by admitting it, which is the only honest way to carry it.")

dn_sig = re.search(r'theorem dn_cor_densities(.*?)\n    \(∀ Θ τ,', DN, re.S).group(1)
theta_binder = bool(re.search(r'\{?Θ *:', dn_sig))
cauchy_binder = 'IsCauchyTemporalOn' in dn_sig or 'IsTemporalOn' in dn_sig
slice_def = bool(re.search(r'def slice \(J : Set N\) \(Θ : N → ℝ\) \(τ : ℝ\) : Set N := '
                           r'\{x \| x ∈ S\.D J ∧ Θ x = τ\}', flat(SRC['Densities'])))
four = {'the black-hole region': in_dn('(S.M \\ X.ι ⁻¹\' St.JpastSet 𝒥) ∩ S.slice J Θ τ = ∅'),
        '∂J⁻(𝒥⁺)': in_dn('S.slice J Θ τ ∩ frontier'),
        '𝓗⁺': in_dn('S.slice J Θ τ ∩ S.H J = ∅'),
        'any set inside it': any('∀ B ⊆' in c for c in DNC)}
paper_flags = len(present([r'\bits slices taken in \$D\$ as here\b'], COR))
DWC = conjuncts(re.search(r'theorem dn_witness :(.*?) := by', DW, re.S).group(1))
bh_eq = any('↔ 0 ≤ (φ x).1' in c for c in DWC)
bh_ne = any('.Nonempty' in c and 'JpastSet mx_scri' in c for c in DWC)
slices_ne = any('minkN.slice JN (Θ₀ ∘ φ) τ).Nonempty' in c for c in DWC)
matter = len(re.findall(r'(?i)oppenheimer|collapsing matter|density', ALL))
v7 = lambda tb, cb, f4, bh, ne, sn, sd: 'SUPPORTED' if (
    not tb and not cb and all(f4.values()) and bh and ne and sn and sd) else 'NOT SUPPORTED'
score('⑦', v7(theta_binder, cauchy_binder, four, bh_eq, bh_ne, slices_ne, slice_def),
      f"`dn_cor_densities` has NO `Θ` binder ({theta_binder}) and no temporal or Cauchy hypothesis "
      f"({cauchy_binder}): `Θ` is universally quantified inside each of its four conjuncts, which "
      f"are exactly the sentence's three plus the `B`-form {four}.  \"For every function `Θ`\" is "
      f"therefore literal — and the reason is the one the PAPER ITSELF names, \"its slices taken in "
      f"`D` as here\" ({paper_flags} occurrence(s)): `slice J Θ τ = {{x ∈ D J | Θ x = τ}}` "
      f"({slice_def}), so the slice is inside `D` by definition and `D` is disjoint from the "
      f"black-hole region and from `𝓗⁺` whatever `Θ` is.  The statement is exactly as strong as it "
      f"looks and no stronger, and the sentence does not overclaim because it says where the "
      f"strength comes from.  `dn_witness` gives the black-hole region as `{{U ≥ 0}}` ({bh_eq}), "
      f"non-empty ({bh_ne}), with non-empty slices ({slices_ne}) so no conjunct is vacuous.  "
      f"Nothing in the three files models matter ({matter} mentions), so \"not formalised\" holds.")

# ================================================== OBJECT B
# P1's own sentences about Δτ, enumerated from the paper.
DTAU = [(i, s) for i, s in enumerate(SENTS) if re.search(r'\\Delta\\?\s*\\?tau', s)]
if len(DTAU) < 5:
    sys.exit(f"⛔ only {len(DTAU)} sentences of P1 mention `Δτ`; the enumeration this read depends "
             "on is wrong.")
# Registered classification markers, each anchored.
SUPPORTS = {
    'the adapted-frame definition': [r'\btemporal separation conjugate to it in the frame adapted\b'],
    'the line element in the adapted frame': [r'\blocal form of the line element in a frame adapted\b'],
    'the temporal LEG of the triangle': [r'\bspatial and temporal legs are equal\b'],
    'the along-the-connection condition': [r'\bcondition along the whole connection\b'],
    'the Killing-parameter line element': [r'ds\^\{2\}=g\(\\chi,\\chi\)\\,d\\lambda\^\{2\}'],
    'the lapse named N, collapsing': [r'\bN=\\sqrt\{1-r_h/r\}'],
    'a vanishing lapse times a nonzero increment carries no duration':
        [r'\bcarrying no metrical duration\b'],
}
AGAINST = {
    'Δτ as an endpoint difference of a temporal function':
        [r'\\Delta\\tau=\\tau\(q\)-\\tau\(p\)\$ assigned by a smooth temporal function'],
    'the separations not accumulated along a path':
        [r'\bnot coordinate differences accumulated along some path\b'],
}
SUP = {k: present(v, FTEX) for k, v in SUPPORTS.items()}
AGA = {k: present(v, FTEX) for k, v in AGAINST.items()}
SUPPORTED_BY = [k for k, v in SUP.items() if v]
AGAINST_BY = [k for k, v in AGA.items() if v]
# does any sentence read Δτ as the null curve's own LENGTH?
as_length = [i for i, s in DTAU
             if present([r'\bgeodesic joining them is null\b'], s)
             and present([r'\\Delta\\tau\b'], s)]
formula_in_P1 = present([r'\\int *N'], FTEX) + present([r'\\int *\\lvert\\chi\\rvert'], FTEX)

v8 = lambda sb: 'SUPPORTED' if len(sb) >= 5 else 'NOT SUPPORTED'
score('⑧', v8(SUPPORTED_BY),
      f"P1's text SUPPORTS the ruling's reading in {len(SUPPORTED_BY)} distinct places: "
      + '; '.join(f"**{k}**" for k in SUPPORTED_BY)
      + f".  The proof names `Δτ` as \"the temporal separation conjugate to [`Δx`] in the frame "
      f"adapted to the same foliation\", puts the relation in \"the local form of the line element "
      f"in a frame adapted to the foliation of (b)\", and calls it the triangle's temporal LEG — "
      f"`69`'s own word.  `lem:killing`'s proof writes the generator's line element as "
      f"`ds² = g(χ,χ)dλ² = |χ|²dλ²` with `λ` the Killing parameter, which is the ruling's "
      f"Killing-horizon specialisation in P1's own hand.  `N` is P1's symbol for the lapse, and "
      f"Section 3 says in as many words that a vanishing lapse times a nonzero coordinate "
      f"increment is \"causal ORDER drawn as coordinate length, carrying no metrical duration\" — "
      f"which is the ruling's `∫N|dt|` with `N → 0`, stated as physics.")

v9 = lambda al: 'SUPPORTED' if not al else 'NOT SUPPORTED'
score('⑨', v9(as_length),
      f"NO sentence of P1 reads `Δτ` as the null curve's own length ({len(as_length)} such).  The "
      f"zero length belongs to `Δs`: \"their spacetime separation is zero, because the geodesic "
      f"joining them is null\".  `Δs²`, `Δx` and `Δτ` are three named quantities throughout, and "
      f"the ruling's negative half — that `Δτ` is not the null curve's length — is the paper's own "
      f"distinction.")

v10 = lambda ab: 'NOT SUPPORTED' if len(ab) != 1 else 'SUPPORTED'
score('⑩', v10(AGAINST_BY),
      f"**{len(AGAINST_BY)} sentences read otherwise, not one.**  ⓵ *\"the temporal separation "
      f"`Δτ = τ(q) − τ(p)` assigned by a smooth temporal function `τ` is not a geometric "
      f"invariant\"* — that `Δτ` is an ENDPOINT DIFFERENCE of a temporal function, and P1 calls it "
      f"explicitly NON-invariant, while the proof's `Δτ` is listed among \"the invariant "
      f"separations named in the hypotheses\".  `∫N|dt(γ′)|` is neither an endpoint difference nor "
      f"non-invariant, so it is not the Section-1 object; the SYMBOL carries two objects.  ⓶ "
      f"*\"These are not coordinate differences accumulated along some path between `p` and `q`\"* "
      f"— `∫N|dt(γ′)|` IS an accumulation along a path, of an invariant integrand rather than a "
      f"coordinate, so the sentence excludes the coordinate reading and not the integral; but it "
      f"is the sentence a reader would cite against the ruling and it needs the distinction said.  "
      f"⌗ Neither `∫N|dt|` nor `∫|χ|dλ` appears anywhere in P1 ({len(formula_in_P1)} occurrence(s) "
      f"of either integral): the formulae are consistent with `Δs² = Δx² − Δτ²` and with "
      f"`ds² = |χ|²dλ²` but are `69`'s construction, not the paper's text.")

# ----------------------------------------------------- guard family three
FLIP = {'①': (v1(UNRESOLVED), v1(['x'])),
        '②': (v2(set_of_points), v2(0)),
        '③': (v3(cont_only, no_cstep, seg, fut), v3(False, no_cstep, seg, fut)),
        '④': (v4(achronal), v4(1)),
        '⑤': (v5(gw_proves, gw_future, gen_exhibited), v5(False, gw_future, gen_exhibited)),
        '⑥': (v6(mono, disclaim), v6(1, disclaim)),
        '⑦': (v7(theta_binder, cauchy_binder, four, bh_eq, bh_ne, slices_ne, slice_def),
              v7(True, cauchy_binder, four, bh_eq, bh_ne, slices_ne, slice_def)),
        '⑧': (v8(SUPPORTED_BY), v8([])),
        '⑨': (v9(as_length), v9([1])),
        '⑩': (v10(AGAINST_BY), v10(['one'])),
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
w("")
w("HasFutureGenerators, the hypothesis step two names:")
w(f"  {HFG}")
w(f"  continuous only: {cont_only}   no causal-step condition between times: {no_cstep}")
w("")
w(f"dn_cor_densities CONJUNCTS ({len(DNC)}):")
for i, c in enumerate(DNC, 1):
    w(f"  {i}. {c[:140]}")
w(f"  Θ binder: {theta_binder}   Cauchy/temporal binder: {cauchy_binder}")
w("")
w(f"P1's SENTENCES MENTIONING Δτ ({len(DTAU)}):")
for i, s in DTAU:
    w(f"  [{i}] {s[:230]}")
w("")
w("P1 SENTENCES SUPPORTING THE RULING:")
for k, v in SUP.items():
    w(f"  {'FOUND    ' if v else 'NOT FOUND'}  {k}")
    for h in v:
        w(f"      ...{h['context']}...")
w("P1 SENTENCES READING OTHERWISE:")
for k, v in AGA.items():
    w(f"  {'FOUND    ' if v else 'NOT FOUND'}  {k}")
    for h in v:
        w(f"      ...{h['context']}...")
w("")
for k in '①②③④⑤⑥⑦⑧⑨⑩':
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
           'guard': G, 'cited': RESOLVE, 'hasFutureGenerators': HFG,
           'dn_conjuncts': DNC, 'dtau_sentences': [{'i': i, 's': s} for i, s in DTAU],
           'supports': {k: bool(v) for k, v in SUP.items()},
           'against': {k: bool(v) for k, v in AGA.items()},
           'verdicts': V, 'tally': tally},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
