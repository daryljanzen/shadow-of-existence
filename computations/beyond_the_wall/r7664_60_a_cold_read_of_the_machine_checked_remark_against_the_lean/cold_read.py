#!/usr/bin/env python3
"""r7664 - a cold read of P1's `rem:formalised` against the Lean.

Twenty claims of the remark, registered in PREDICTION.md before this ran, each scored
against the Lean source on the tree `runs/TREE.txt` names.  Nothing is scored from the
remark's own wording: every verdict is a function of text parsed out of the Lean.
Two guard probes run through the conjunct machinery and must flip.
"""
import json, os, re, subprocess, sys

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True,
                      text=True, check=True).stdout.strip()
HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
LP = 'computations/formalisation/lean/probes'


def read(rel):
    p = P(rel)
    if not os.path.exists(p):
        sys.exit(f"⛔ absent on this tree: {rel}")
    return open(p, encoding='utf-8').read()


CB = read(f'{LP}/ConformalBoundary.lean')
CZ = read(f'{LP}/Compactification.lean')
CY = read(f'{LP}/CylinderWitness.lean')
TEX = read('corpus/BH_causality_v2.tex')
# every prose probe below runs on the FLAT copy: the Lean's docstrings wrap, and a probe that
# cannot see across a line break answers about the line break.
CBF = re.sub(r'\s+', ' ', CB)

# ---------------------------------------------------------------- the object
M = re.search(r'\\begin\{remark\}\[Machine-checked form\]\\label\{rem:formalised\}(.*?)'
              r'\\end\{remark\}', TEX, re.S)
if M is None:
    sys.exit("⛔ `rem:formalised` is not in corpus/BH_causality_v2.tex on this tree: "
             "the object of this read is gone and no verdict below would be about it.")
REMARK = M.group(1)

# ------------------------------------------------- the statement, parsed out
def decl(src, name, where):
    m = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', src, re.S | re.M)
    if m is None:
        sys.exit(f"⛔ `{name}` is not a theorem in {where} on this tree.")
    return m.group(0)


PROP = decl(CB, 'mx_prop_causal_alignment', 'ConformalBoundary.lean')
HEQ = decl(CB, 'mx_H_eq_boundary', 'ConformalBoundary.lean')
WIT = decl(CB, 'mx_witness_headline', 'ConformalBoundary.lean')
CZW = decl(CZ, 'cz_witness_headline', 'Compactification.lean')
CZF = decl(CZ, 'cz_witness_headline_F', 'Compactification.lean')
CYW = decl(CY, 'cy_witness_headline', 'CylinderWitness.lean')
CYT = decl(CY, 'cy_witness_tangency', 'CylinderWitness.lean')

# the signature is everything up to the first `:` that starts a line of its own depth;
# in this file the conclusion begins at the line `    S.H J =`.
sig_m = re.search(r'theorem mx_prop_causal_alignment(.*?)\n    S\.H J =', PROP, re.S)
if sig_m is None:
    sys.exit("⛔ `mx_prop_causal_alignment`'s conclusion no longer starts `S.H J =`: "
             "the binder/conclusion split this read depends on cannot be made.")
SIG = sig_m.group(1)
BODY = PROP[sig_m.end():]

# binders: every top-level (...) / [...] / {...} group in the signature
def binders(sig):
    out, depth, start, kind = [], 0, None, None
    for i, ch in enumerate(sig):
        if ch in '([{':
            if depth == 0:
                start, kind = i, ch
            depth += 1
        elif ch in ')]}':
            depth -= 1
            if depth == 0:
                out.append(sig[start:i + 1])
                start = None
    if depth != 0:
        sys.exit("⛔ the signature's brackets do not balance: the binder parse is unsound.")
    return out


BINDERS = binders(SIG)
if len(BINDERS) < 10:
    sys.exit(f"⛔ only {len(BINDERS)} binders parsed out of the signature; a statement this "
             "size has more, so the parse is wrong and no census below would mean anything.")

def bname(b):
    inner = b[1:-1].strip()
    if b[0] == '[':
        return '[' + inner.split()[0] + ']'
    return inner.split(' ')[0].split(':')[0].strip()


BNAMES = [bname(b) for b in BINDERS]

# conclusion: split the top-level ∧ chain
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
    return [re.sub(r'\s+', ' ', c) for c in out if c.strip()]


concl_m = re.search(r'\n    (S\.H J =.*?) := by\n', PROP, re.S)
if concl_m is None:
    sys.exit("⛔ `mx_prop_causal_alignment`'s conclusion does not end ` := by`: cannot delimit it.")
CONCL = concl_m.group(1)
CONJ = conjuncts(CONCL)

# ------------------------------------------------------------------ the guard
# Both probes go through `in_conclusion`, the same predicate every conjunct claim uses.
def in_conclusion(needle):
    return any(needle in c for c in CONJ)


GUARD = {'true-probe  (`S.SublevelProper J Θ` is a conjunct)': in_conclusion('S.SublevelProper J Θ'),
         'false-probe (`S.FiniteDimensional J Θ` is a conjunct)':
             in_conclusion('S.FiniteDimensional J Θ')}
if not (GUARD['true-probe  (`S.SublevelProper J Θ` is a conjunct)'] is True and
        GUARD['false-probe (`S.FiniteDimensional J Θ` is a conjunct)'] is False):
    sys.exit("⛔ THE GUARD DID NOT FLIP.  Every verdict in this receipt is withdrawn: a checker "
             f"that cannot return both answers measures itself.  {GUARD}")

# ------------------------------------------------------- the registered mapping
# claim -> the binders that claim accounts for.  Registered, then checked for coverage.
MAP = {
    '②': ['[T2Space', 'hL', 'hLt'],
    '③': ['X'],
    '④': ['hOD', 'hmono', 'hI', 'hΘ', 'hadapt'],
    '⑨': ['hJM', 'hHM', 'h𝒥'],
}
PROPOSITIONAL = [n for n, b in zip(BNAMES, BINDERS)
                 if b[0] == '[' or re.search(r':\s*(S\.|St\.|X\.|∀|frontier|Conformal)', b)]
ACCOUNTED = {b for v in MAP.values() for b in v}
UNACCOUNTED = [n for n in PROPOSITIONAL
               if not any(n.startswith(a) or a.startswith(n) for a in ACCOUNTED)]

V = {}          # claim -> [verdict, evidence]
def score(key, verdict, evidence):
    V[key] = [verdict, evidence]


# ---------------------------------------------------------------- the verdicts
# ① the attestation
pa = re.findall(r'^#print axioms (\S+)', CB, re.M)
unproved = len(re.findall(r'\bsorry\b|\badmit\b|native_decide', CB + CZ + CY))
decl_axiom = re.findall(r'^axiom\s', CB + CZ + CY, re.M)
named_audited = [n for n in ('MSpacetime.mx_prop_causal_alignment',
                             'MSpacetime.mx_H_eq_boundary') if n in pa]
score('①', 'UNMEASURED BY THIS SEAT',
      f"no Lean toolchain and no Mathlib on this tree, so `#print axioms`' OUTPUT cannot be read "
      f"here and the three-axiom claim is not decided.  What IS measurable: the file requests the "
      f"audit for {len(named_audited)}/2 of the two named theorems ({', '.join(named_audited)}), "
      f"{len(pa)} `#print axioms` lines in ConformalBoundary.lean in all; "
      f"{unproved} occurrences of sorry/admit/native_decide and {len(decl_axiom)} `axiom` "
      f"declarations across the three probe files.")

# ② the setting
t2 = '[T2Space N]' in SIG
t2t = 'T2Space Ñ' in SIG
mfd = re.findall(r'\[IsManifold 𝓘\(ℝ, E\) (\S+) (N|Ñ)\]', CB)
loc = re.search(r'def LocallyOneChart : Prop :=(.*?)\n\n', CB, re.S)
if loc is None:
    sys.exit("⛔ `LocallyOneChart`'s definition is gone: ② cannot be scored.")
loc1 = 'ContDiffOn ℝ 1' in loc.group(1) and 'ContinuousOn (chartRep S.T p)' in loc.group(1)
mst = re.search(r'structure MSpacetime where(.*?)\n\nnamespace MSpacetime', CB, re.S)
fields = re.findall(r'^  (\w+)', mst.group(1), re.M) if mst else []
score('②', 'SUPPORTED' if (t2 and loc1 and all(c == '1' for c, _ in mfd)) else 'NOT SUPPORTED',
      f"`[T2Space N]` is a binder of the theorem ({t2}); `LocallyOneChart` is exactly `hRep g` "
      f"`C¹` and `chartRep T` continuous on an open set in the preferred chart about each point "
      f"({loc1}); the charted structure is `IsManifold … 1` on both carriers ({mfd}).  "
      f"`MSpacetime`'s fields are {fields}: the Lorentzian conditions `T_timelike` and "
      f"`pos_on_perp` are imposed ON `M` only, which the remark's own phrase \"the region carrying "
      f"the metric\" (⑨) matches.  Hausdorffness is assumed for `N` ALONE — `T2Space Ñ` is not a "
      f"binder ({t2t}) — so the setting sentence is, if anything, stronger than the Lean needs.")

# ③ the extension
ce = re.search(r'structure ConformalExtension \(S : MSpacetime E N\) \(St : MSpacetime E Ñ\) where'
               r'(.*?)\n\n', CB, re.S)
if ce is None:
    sys.exit("⛔ `ConformalExtension`'s declaration is gone: ③ cannot be scored.")
CEF = re.findall(r'^  (\w+)', ce.group(1), re.M)
said = {'ι': 'open', 'isOpenEmbedding': 'open', 'contMDiff': 'C¹', 'Ω': 'Ω', 'Ω_pos': 'positive',
        'conformal': 'Ω²g'}
unsaid = [f for f in CEF if f not in said]
cstep = re.search(r'def CStep \(x y : N\) : Prop :=(.*?)\n\n', CB, re.S)
chain = bool(cstep and 'ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ' in cstep.group(1)) \
    and 'def Cau (x y : N) : Prop := Relation.ReflTransGen S.CStep x y' in CB
score('③', 'NOT SUPPORTED' if (unsaid or not chain) else 'SUPPORTED',
      f"`ConformalExtension`'s fields are {CEF}.  The remark states the open `C¹` embedding, the "
      f"positive `Ω` and `ι*g̃ = Ω²g`, and \"causal curves are chains of `C¹` causal arcs\" is "
      f"exactly `Cau = ReflTransGen CStep` with `CStep` a `ContMDiff … 1` arc ({chain}).  But "
      f"{len(unsaid)} field(s) of the structure go unstated: {unsaid} — the agreement of the time "
      f"orientations under `Dι` on `M`, and `ι(M) ⊆ M̃`.  A reader asked what the formal statement "
      f"assumes about the extension is told five of its seven fields.")

# ④ the hypotheses on O and Θ
ict = re.search(r'def IsCauchyTemporalOn \(U : Set N\) \(τ : N → ℝ\) : Prop :=(.*?)\n\n', CB, re.S)
score('④', 'SUPPORTED' if ('hOD' in BNAMES and 'hmono' in BNAMES and 'hI' in BNAMES
                           and 'hΘ' in BNAMES and 'hadapt' in BNAMES) else 'NOT SUPPORTED',
      f"`hmono : ∀ s t, s < t → S.Chr (O s) (O t)` is the chronological ordering; `hOD` is "
      f"`I⁻(range O) = D J` and `hI` is `I⁻(range O) = ι⁻¹ Ĩ⁻(𝒥)`, which together are the "
      f"remark's `I⁻(O) = D = I⁻(𝒥⁺)`; `hΘ : S.IsCauchyTemporalOn (S.D J) Θ` and "
      f"`hadapt : ∀ τ, Θ (O τ) = τ + c`.  `IsCauchyTemporalOn` unfolds to `IsTemporalOn` plus a "
      f"unique crossing for every inextendible causal curve IN `U` "
      f"({'∃! t' in (ict.group(1) if ict else '')}), so \"Cauchy temporal function of `D`\" is the "
      f"intrinsic property on `D` and not a statement about surfaces of the whole spacetime.")

# ⑤ conclusion one
c1 = in_conclusion('S.H J = frontier (X.ι ⁻¹\' St.JpastSet 𝒥)')
hO_in_prop = 'S.H (range O)' in CONCL
hO_in_heq = 'S.H (range O) = frontier' in HEQ
score('⑤', 'NOT SUPPORTED' if (c1 and not hO_in_prop and hO_in_heq) else
      ('SUPPORTED' if c1 and hO_in_prop else 'NOT SUPPORTED'),
      f"the first conjunct is `S.H J = frontier (ι⁻¹ J̃⁻(𝒥))` ({c1}), i.e. `∂J⁻(J) = ∂J⁻(𝒥⁺)`.  "
      f"The remark's first of four is `∂J⁻(O) = ∂J⁻(𝒥⁺) = 𝓗⁺`, and `S.H (range O)` does NOT "
      f"appear in this theorem's conclusion ({hO_in_prop}); it is the FIRST conjunct of "
      f"`mx_H_eq_boundary` ({hO_in_heq}), which the remark names separately, in the clause before.  "
      f"The pair of theorems carries the double equality; the theorem the sentence attributes it "
      f"to carries one half.")

# ⑥ conclusion two
sp = re.search(r'def SublevelProper \(J : Set N\) \(Θ : N → ℝ\) : Prop :=(.*?)\n\n', CB, re.S)
sp_ok = bool(sp and 'closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J' in re.sub(r'\s+', ' ', sp.group(1)))
fr = 'frontier (S.JpastSet A) = closure (S.D A) \\ S.D A' in CB
score('⑥', 'SUPPORTED' if in_conclusion('S.SublevelProper J Θ') and sp_ok and fr
      else 'NOT SUPPORTED',
      f"the second conjunct is `S.SublevelProper J Θ`, which unfolds to "
      f"`∀ T, closure {{x ∈ D J ∧ Θ x ≤ T}} ⊆ D J` ({sp_ok}) — the remark's sentence exactly, with "
      f"the sublevel set taken inside `D`, which the remark's \"{{Θ≤T}}\" leaves to its own \"lies "
      f"inside `D`\".  The consequence the remark draws, that no finite-`Θ` slice meets `𝓗⁺`, is "
      f"NOT a conjunct: it is one step from `mx_frontier_JpastSet`, `∂J⁻(A) = closure D ∖ D` "
      f"({fr}), which is disjoint from `D`.  The remark's \"so that\" is accurate as a derivation "
      f"and the derivation's one input is a proved lemma of the same file.")

# ⑦ conclusion three
kli = re.search(r'def KLi \(A : ℝ → Set X\) : Set X :=(.*)', CB)
kls = re.search(r'def KLs \(A : ℝ → Set X\) : Set X :=(.*)', CB)
sl = re.search(r'def slice \(J : Set N\) \(Θ : N → ℝ\) \(τ : ℝ\) : Set N :=(.*)', CB)
cn = re.search(r'def cone \(O : ℝ → N\) \(τ : ℝ\) : Set N :=(.*)', CB)
four = [in_conclusion(f'{k} (S.{s}') for k in ('KLi', 'KLs') for s in ('slice J Θ)', 'cone O)')]
atTop = bool(kli and '∀ᶠ τ in atTop' in kli.group(1)) and bool(kls and '∃ᶠ τ in atTop' in kls.group(1))
score('⑦', 'SUPPORTED' if all(four) and atTop else 'NOT SUPPORTED',
      f"four of the seven conjuncts are `KLi`/`KLs` of `S.slice J Θ` and of `S.cone O`, each equal "
      f"to the same frontier ({four}).  `KLi A = {{p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}}` "
      f"is literally \"met by ALL SUFFICIENTLY LATE τ\" and `KLs` is \"met FREQUENTLY\" ({atTop}); "
      f"`slice J Θ τ = {{x ∈ D J | Θ x = τ}}` and `cone O τ = frontier (J⁻(O τ))` are the remark's "
      f"`S_τ` and `∂J⁻(O(τ))`.  The remark's gloss names the substantive half of each equality — "
      f"`frontier ⊆ KLi` for the lower limit, `KLs ⊆ frontier` for the upper — and each conjunct "
      f"is in fact an equality, so the Lean gives both inclusions of both.")

# ⑧ conclusion four
tang = CONJ[-1]
fh = re.search(r'def FrameHyp \(g : E →L\[ℝ\] E →L\[ℝ\] ℝ\) \(ℓ n : E\) \(ξ : E →L\[ℝ\] ℝ\) : Prop :='
               r'(.*?)\n\n', CB, re.S)
if fh is None:
    sys.exit("⛔ `FrameHyp`'s definition is gone: ⑧ cannot be scored.")
FH = re.sub(r'\s+', ' ', fh.group(1)).strip()
fh_second = 'FutCausal (bil g) ℓ n v → 0 < ξ v' in FH
limit_in_chart = 'covCh Θ q x' in tang
v8f = lambda second, chart: 'NOT SUPPORTED' if (second or chart) else 'SUPPORTED'
V8 = v8f(fh_second, limit_in_chart)
score('⑧', V8,
      f"the seventh conjunct quantifies over every `q ∈ frontier`, every `ℓ n L C ℓ₀` with "
      f"`L ≤ 𝓝 q`, and takes FOUR hypotheses: `∀ᶠ FrameHyp (gE x) (ℓ x) (n x) (dcov Θ x)`, "
      f"`∀ᶠ ‖dchartL q x (n x)‖ ≤ C`, `dchartL q x (ℓ x) → ℓ₀`, and the rate `→ 0`; the limit is "
      f"`(dcov Θ x (n x))⁻¹ • covCh Θ q x → −(gE q ℓ₀)`.  `FrameHyp` is `{FH}` — a null frame AND "
      f"`ξ` POSITIVE ON THE FUTURE CAUSAL CONE OF `(ℓ, n)` ({fh_second}).  The remark states the "
      f"frame as \"null frames (ℓ,n)\" and never states that second half, which is not implied by "
      f"`Θ` being temporal on `D`, because the hypothesis is asked eventually along a filter "
      f"converging to a point OF `𝓗⁺`, where `IsTemporalOn (S.D J)` says nothing.  Separately the "
      f"limit is of `covCh Θ q x`, `dΘ_x` RE-READ IN THE CHART AT `q` ({limit_in_chart}); the "
      f"remark attaches \"in a chart\" to the bound on `n` only, and without the chart-reading its "
      f"`dΘ/dΘ(n) → −g(ℓ₀,·)` compares covectors at different points.")

# ⑨ assumes only
rng = 'theorem mx_range_subset_M' in CB and 'range O ⊆ S.M' in CB
carriers = [n for n in BNAMES if n in ('hJM', 'hHM', 'h𝒥')]
v9f = lambda ncar, derived: 'NOT SUPPORTED' if (ncar != 2 or derived) else 'SUPPORTED'
V9 = v9f(len(carriers), rng)
score('⑨', V9,
      f"the carrier binders actually assumed are {carriers}: `hJM : J ⊆ S.M`, "
      f"`hHM : frontier (ι⁻¹ J̃⁻(𝒥)) ⊆ S.M` and `h𝒥 : 𝒥 ⊆ St.M` — three, on `J`, on `𝓗⁺` and on "
      f"`𝒥⁺`.  The remark names two, \"the worldline and `𝓗⁺`\", and the WORLDLINE's carrier is "
      f"not among them: `range O ⊆ S.M` is DERIVED from the chronological ordering by "
      f"`mx_range_subset_M` ({rng}) and is assumed nowhere.  What is assumed in its place is the "
      f"carrier of `J`, the set whose chronological past is `D`, which is not the worldline.  "
      f"Compounding it, ⑧'s positivity of `dΘ` on the frame's cone is a tangency hypothesis the "
      f"sentence's \"the convergence and bound on the frame just stated\" does not cover.  "
      f"Binders left unaccounted by the registered mapping: {UNACCOUNTED or 'none'}.")

# ⑩ does not use
absent = {k: (k not in SIG) for k in ('asymptot', 'Complete', 'i⁺', 'FiniteDimensional')}
smooth = sorted(set(re.findall(r'ContMDiff\w*[^0-9\n]{0,40}?\b(\d+|⊤|∞)\b', CB)))
atlas = sorted(set(c for c, _ in re.findall(r'\[IsManifold 𝓘\(ℝ, E\) (\S+) (N|Ñ)\]', CB)))
score('⑩', 'SUPPORTED' if all(absent.values()) and atlas == ['1'] else 'NOT SUPPORTED',
      f"no binder mentions asymptotic flatness, future-completeness of `O`, or `O(τ)→i⁺` "
      f"({absent}), and the regularity is `1` throughout: the CHARTED STRUCTURE itself is "
      f"`IsManifold 𝓘(ℝ,E) 1` on both carriers ({atlas}), not `⊤`, so the atlas is `C¹` too and "
      f"the claim holds at a level the sentence does not even claim.  The smoothness classes "
      f"appearing with `ContMDiff` in the file are {smooth}.  The model space carries "
      f"`NormedAddCommGroup`/`NormedSpace ℝ` and nothing else — no finite dimensionality, no "
      f"completeness — so the theorem is dimension-free.")

# ⑪ the standard equivalent
hyp = len(re.findall(r'(?i)hyperbolic', CB + CZ + CY))
v11f = lambda n: 'NOT SUPPORTED' if n == 0 else 'SUPPORTED'
V11 = v11f(hyp)
score('⑪', V11,
      f"the word \"hyperbolic\" does not occur once in the three probe files ({hyp} occurrences), "
      f"so there is no machine-checked statement relating global hyperbolicity of `D` to the "
      f"existence of a Cauchy temporal function on it.  That global hyperbolicity enters only "
      f"through `hΘ` is SUPPORTED — it is the single binder in which `D`'s causal character is "
      f"used.  Its appositive, \"its standard equivalent\", is a claim about the literature "
      f"standing inside a remark headed \"Machine-checked form\", and the attestation does not "
      f"reach it.")

# ⑫ the two clauses not in the formal statement
cone_meets = bool(re.search(r'cone[^\n]*(Disjoint|∩[^\n]*H |= *∅)', CB))
unbounded = bool(re.search(r'without bound|unbounded (stretch|along)', CB))
score('⑫', 'SUPPORTED' if not cone_meets and not unbounded else 'NOT SUPPORTED',
      f"neither clause is among the seven conjuncts, and neither is proved elsewhere in the file: "
      f"no statement disjoints a past cone from `𝓗⁺` ({cone_meets}) and none says the approached "
      f"stretch extends without bound ({unbounded}).  The remark's account of what is missing is "
      f"accurate, and so is its reason for the second — `KLi`/`KLs` are set limits and carry no "
      f"metric extent.")

# ⑬ the first witness
wconj = conjuncts(re.search(r'theorem mx_witness_headline :(.*?) := by', WIT, re.S).group(1))
wit_has = {'identification (H J)': any('minkN.H JN = frontier' in c for c in wconj),
           'properness': any('SublevelProper' in c for c in wconj),
           'KLi slice': any('KLi (minkN.slice' in c for c in wconj),
           'KLs slice': any('KLs (minkN.slice' in c for c in wconj),
           'KLi cone': any('KLi (minkN.cone' in c for c in wconj),
           'KLs cone': any('KLs (minkN.cone' in c for c in wconj),
           'tangency at p₀': any('Tendsto' in c and 'covCh' in c for c in wconj)}
two_chart = 'the atlas `{idH, nullH}`' in CBF
arctanV = bool(re.search(r"mx_witnessExt\.Ω x \^ 2 = 1 / \(1 \+ \(φ x\)\.2 \^ 2\)", CB))
score('⑬', 'SUPPORTED' if all(wit_has.values()) and two_chart and arctanV
      else 'NOT SUPPORTED',
      f"`mx_witness_headline` discharges every hypothesis of `mx_prop_causal_alignment` and reads "
      f"off all seven conjuncts {wit_has}, the tangency one instantiated at `p₀` with the frame "
      f"`(ℓN, nN)` along `𝓝[D] p₀`.  The carrier is the two-chart atlas `{{idH, nullH}}` "
      f"({two_chart}) and the compactification is `v = arctan V` alone, visible in "
      f"`Ω² = 1/(1 + V²)` ({arctanV}).  \"Every clause of the conclusion instantiated\" is exact.")

# ⑭ ⑮ the two slicings
th0 = 'noncomputable def Θ₀ : P → ℝ := ThetaG fun s => -Real.log s' in CB
ffail = re.search(r'noncomputable def Ffail \(s : ℝ\) : ℝ := (.*)', CB)
fails = decl(CB, 'mc_witness_tangency_fails', 'ConformalBoundary.lean')
neg = len(re.findall(r'¬ Tendsto', fails))
score('⑭', 'SUPPORTED' if th0 and wit_has['tangency at p₀'] else 'NOT SUPPORTED',
      f"`Θ₀ = ThetaG (fun s => −log s)`, i.e. `−log(−U) + V` ({th0}), and it is the slicing "
      f"`mx_witness_headline`'s tangency limit is proved for.")
score('⑮', 'SUPPORTED' if ffail and neg >= 2 else 'NOT SUPPORTED',
      f"`Ffail s = {ffail.group(1) if ffail else '?'}`, so `Θf = F(−U) + V` with a `sin(log s)` "
      f"term: the rate across the generators oscillates.  `mc_witness_tangency_fails` proves `Θf` "
      f"is still Cauchy temporal on `D` and the frame hypotheses still hold on `D`, and then "
      f"NEGATES both the rate limit and the tangency limit ({neg} `¬ Tendsto`).  SUPPORTED — but "
      f"the remark cites only `mx_witness_headline` for this sentence, and that theorem says "
      f"nothing about `Θf`; the result is `mc_witness_tangency_fails`, which the remark never "
      f"names.")

# ⑯ ⑰ the compactification and the F family
czc = conjuncts(re.search(r'theorem cz_witness_headline :(.*?) := by', CZW, re.S).group(1))
compact = any('IsCompact (closure (range cz_witnessExt.ι))' in c for c in czc)
nonconst_here = any('Ω' in c for c in czc)
nonconst_thm = 'cz_Ω_nonconst' in CZ
czfc = conjuncts(re.search(r'theorem cz_witness_headline_F :(.*?) := by', CZF, re.S).group(1))
general = any('∀ q ∈ frontier' in c and 'Tendsto' in c for c in czfc)
nonvac = 'theorem cz_exp_nonvacuous' in CZ
score('⑯', 'SUPPORTED' if compact and nonconst_thm else 'NOT SUPPORTED',
      f"`cz_witness_headline`'s conclusion opens with `IsCompact (closure (range ι))` and "
      f"`range ι ≠ univ` ({compact}) — the image's compact closure, stated as a conjunct, with the "
      f"target `Ñ = P` a different type from `N = Pt`, so this is a genuine compactification and "
      f"not a relabelling.  The non-constancy of `Ω²` is NOT a conjunct of this theorem "
      f"({nonconst_here}): it is the separate `cz_Ω_nonconst` ({nonconst_thm}), which the remark's "
      f"single citation does not distinguish.")
score('⑰', 'SUPPORTED' if general and 'cz_witness_headline_F' in CZ else 'NOT SUPPORTED',
      f"`cz_witness_headline_F` is stated for every positive `C¹` `F̂`, with `g_F = F·g = −F dU dV`, "
      f"and its last conjunct is the tangency clause in full generality — `∀ q ∈ frontier, ∀ ℓ n L "
      f"C ℓ₀, …` ({general}) — with no point instantiated, exactly as the remark says.  The remark "
      f"omits `cz_exp_nonvacuous` ({nonvac}), which exhibits `F̂ = e^{{UV}}` and proves `g_F ≠ g`: "
      f"without it the `F`-family could be read as the flat case relabelled.")

# ⑱ ⑲ the cylinder
cyc = conjuncts(re.search(r'theorem cy_witness_headline :(.*?) := by', CYW, re.S).group(1))
cy_has = {'no chart covers': any('(chartAt E x).source ≠ univ' in c for c in cyc),
          'H = {U=0}': any('cy_S.H cy_J = {x : N | x.1.1 = 0}' in c for c in cyc),
          'Cauchy on the manifold': any('IsCauchyTemporalOn' in c for c in cyc),
          'properness': any('SublevelProper' in c for c in cyc),
          'KLi/KLs slice': sum('KLi (cy_S.slice' in c or 'KLs (cy_S.slice' in c for c in cyc) == 2,
          'KLi/KLs cone': sum('KLi (cy_S.cone' in c or 'KLs (cy_S.cone' in c for c in cyc) == 2}
cy_J_is_O = 'noncomputable def cy_J : Set N := range cy_O' in CY
cy_tang = 'Tendsto' in CYT and 'cy_witness_tangency' in CY
CYF = re.sub(r'\s+', ' ', CY)
reported = 'REPORTED, not built' in CYF
score('⑱', 'SUPPORTED' if all(cy_has.values()) and cy_J_is_O and cy_tang else 'NOT SUPPORTED',
      f"`cy_witness_headline` {cy_has}; `cy_J = range cy_O` ({cy_J_is_O}), so `cy_S.H cy_J` IS "
      f"`∂J⁻(O)` and the remark's reading of `𝓗⁺ = {{U=0}}×S¹` as `∂J⁻(O)` is the Lean's.  The "
      f"Cauchy property is `cy_isCauchyTemporalOn`, a conjunct, stated on `N` itself.  Tangency at "
      f"every horizon point is `cy_witness_tangency` ({cy_tang}).  Six of the seven conjuncts plus "
      f"tangency; the identification conjunct is the one absent, which is ⑲.")
v19f = lambda rep: 'NOT SUPPORTED' if rep else 'SUPPORTED'
V19 = v19f(reported)
score('⑲', V19,
      f"the non-exercise is right — no `ConformalExtension` is built for the cylinder.  But the "
      f"REASON the remark gives is not machine-checked: the file's own header carries it as "
      f"\"`ConformalExtension` / `mx_prop_causal_alignment` — REPORTED, not built\" ({reported}), "
      f"an argument in prose that a conformal `g̃ = h(−du dv) + k dy²` would need `k = Ω²` and "
      f"`h = Ω²(1+U²)(1+V²)`, so either the circle's size vanishes at `𝒥⁺` or `h` blows up.  "
      f"No theorem states it.  A sentence of a remark headed \"Machine-checked form\" asserts, "
      f"without marking it, something the probe file itself marks as reported rather than built.")

# ⑳ what is not yet built
instantiators = sorted(os.path.basename(p) for p in
                       [f'{LP}/{f}' for f in sorted(os.listdir(P(LP))) if f.endswith('.lean')]
                       if re.search(r'mx_prop_causal_alignment|mh_causal_alignment_gh_N',
                                    read(p)))
dims = sorted(set(re.findall(r'Module\.finrank ℝ E = (\d+)', CB + CZ + CY)))
score('⑳', 'SUPPORTED' if '4' not in dims else 'NOT SUPPORTED',
      f"the files instantiating the headline are {instantiators}; the model dimensions they state "
      f"are {dims} — the cylinder's 3 is the largest and no witness states 4.  The curved stretch "
      f"that exists is `cz_scale`, a conformal rescaling `F·g` whose causal objects are unchanged "
      f"by construction, so \"a curved one beyond conformal rescaling\" is indeed not built.")

# ------------------------------------------------- the guard, second family
# A verdict written as a constant measures nothing.  Each of the four verdicts that read
# NOT SUPPORTED from a boolean is re-evaluated with that boolean negated, and must flip.
FLIP = {
    '⑧': (v8f(fh_second, limit_in_chart), v8f(False, False)),
    '⑨': (v9f(len(carriers), rng), v9f(2, False)),
    '⑪': (v11f(hyp), v11f(hyp + 1)),
    '⑲': (v19f(reported), v19f(not reported)),
}
for k, (actual, negated) in FLIP.items():
    if actual == negated:
        sys.exit(f"⛔ {k}'s verdict does not depend on its reading: it returns '{actual}' "
                 'either way.  Every verdict in this receipt is withdrawn.')
GUARD['flip-test (⑧ ⑨ ⑪ ⑲ verdicts depend on their readings)'] = True

# ------------------------------------------------------------- the omissions
OMITTED = [
    "the theorem is DIMENSION-FREE: `E` carries only `NormedAddCommGroup` and `NormedSpace ℝ`, "
    "with no `FiniteDimensional` and no `CompleteSpace` anywhere in the three files, so the "
    "proposition is proved for any real normed model space.  The remark's closing sentence speaks "
    "only of which WITNESSES are built, leaving a reader to suppose the theorem itself is tied to "
    "low dimension.",
    "the charted structure is `IsManifold 𝓘(ℝ,E) 1`, a `C¹` ATLAS, not `⊤`.  The remark says no "
    "smoothness beyond `C¹` is used of the metric and the maps; that it is not used of the atlas "
    "either is stronger and is not said.",
    "`mc_witness_tangency_fails` — the theorem behind the remark's oscillating slicing — is never "
    "named, though it is the only place a NEGATIVE result is proved, and it is the sharper half of "
    "the pair: `Θf` satisfies every hypothesis of the proposition except the rate limit, so the "
    "rate hypothesis is shown necessary and not merely convenient.",
    "`cz_exp_nonvacuous` (`F̂ = e^{UV}`, `g_F ≠ g`) is not named, so nothing in the remark rules "
    "out the `F`-family being the flat metric under another name.",
    "`cz_witness_headline`'s conclusion also carries `range ι ≠ univ`: the extension is proper, "
    "the boundary genuinely added.  The remark gives the compact closure and not this.",
]

# ------------------------------------------------------------------- the report
LINES = []
w = LINES.append
w(f"TREE: {open(os.path.join(HERE, 'runs', 'TREE.txt')).readline().strip()}")
w(f"GUARD: {GUARD}  -> both probes flipped; the verdicts stand.")
w(f"BINDERS ({len(BINDERS)}): {BNAMES}")
w(f"CONJUNCTS ({len(CONJ)}):")
for i, c in enumerate(CONJ, 1):
    w(f"  {i}. {c[:150]}")
w("")
for k in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳':
    if k in V:
        w(f"{k}  {V[k][0]}")
        w(f"     {V[k][1]}")
        w("")
w("OMITTED BY THE REMARK, PROVED BY THE LEAN:")
for o in OMITTED:
    w(f"  * {o}")
w("")
tally = {}
for k, (verdict, _) in V.items():
    tally[verdict] = tally.get(verdict, 0) + 1
w(f"TALLY: {tally}")

OUT = '\n'.join(LINES)
print(OUT)
open(os.path.join(HERE, 'verdicts.txt'), 'w', encoding='utf-8').write(OUT + '\n')
json.dump({'tree': open(os.path.join(HERE, 'runs', 'TREE.txt')).read().splitlines(),
           'guard': GUARD, 'binders': BNAMES, 'conjuncts': CONJ,
           'verdicts': V, 'omitted': OMITTED, 'tally': tally,
           'unaccounted_binders': UNACCOUNTED},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
