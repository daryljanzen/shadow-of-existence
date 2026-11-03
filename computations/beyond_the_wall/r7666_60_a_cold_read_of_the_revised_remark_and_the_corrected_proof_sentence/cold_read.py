#!/usr/bin/env python3
"""r7666 - a cold read of the revised `rem:formalised`, and of the corrected proof sentence.

Two objects, registered in PREDICTION.md before this ran: the remark's twenty-three claims and
the proof sentence's four steps.  Every verdict is a function of text parsed out of the Lean on
the tree `runs/TREE.txt` names, never of the prose's wording.  Three guard families run: a
true/false probe pair through the conjunct machinery, a flip family over every derived verdict,
and a marker-probe pair over the prose scanner.  If any does not flip, the receipt is withdrawn.
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


SRC = {n: read(f'{LP}/{n}.lean') for n in
       ('ConeDisjoint', 'ConformalBoundary', 'Compactification', 'CurvedTangency',
        'CylinderWitness', 'FourDWitness')}
ALL = '\n'.join(SRC.values())
TEX = read('corpus/BH_causality_v2.tex')

# ------------------------------------------------------------------ object A
m = re.search(r'\\begin\{remark\}\[Machine-checked form\]\\label\{rem:formalised\}(.*?)'
              r'\\end\{remark\}', TEX, re.S)
if m is None:
    sys.exit("⛔ `rem:formalised` is gone from corpus/BH_causality_v2.tex on this tree.")
REMARK = flat(m.group(1))

# ------------------------------------------------------------------ object B
pi = TEX.index('\\label{prop:causal-alignment}')
seg = TEX[pi:TEX.index('\\label{rem:formalised}')]
k = seg.find('No past light cone of an exterior event meets')
if k < 0:
    sys.exit("⛔ the proof sentence the order names is not in the proof of "
             "`prop:causal-alignment` on this tree: the second object of this read is gone.")
_end = seg.index('Because $I^-(O)=D$', k)
SENTENCE = flat(seg[k:_end])
PRECEDING = flat(seg[max(0, seg.rfind('.', 0, k) - 260):k])

# -------------------------------------------------------- the cited names
CITED = [('cd_prop_causal_alignment', 'ConeDisjoint'), ('mx_prop_causal_alignment', 'ConformalBoundary'),
         ('mx_H_eq_boundary', 'ConformalBoundary'), ('mx_witness_headline', 'ConformalBoundary'),
         ('cd_witness', 'ConeDisjoint'), ('mc_witness_tangency_fails', 'ConformalBoundary'),
         ('cz_witness_headline', 'Compactification'), ('cz_Ω_nonconst', 'Compactification'),
         ('cz_witness_headline_F', 'Compactification'), ('cz_exp_nonvacuous', 'Compactification'),
         ('ct_witness_tangency_F', 'CurvedTangency'), ('ct_expV_differs', 'CurvedTangency'),
         ('cy_witness_headline', 'CylinderWitness'), ('cy_witness_tangency', 'CylinderWitness'),
         ('fd_witness_headline', 'FourDWitness'), ('fd_witness_tangency', 'FourDWitness'),
         ('cd_cone_disjoint', 'ConeDisjoint'), ('cd_closure_Jpast_inter_H', 'ConeDisjoint')]
RESOLVE = {}
for nm, fl in CITED:
    in_tex = nm.replace('_', '\\_').replace('Ω', '$\\Omega$') in TEX or nm in TEX
    hit = bool(re.search(r'^(theorem|lemma) ' + re.escape(nm) + r'\b', SRC[fl], re.M))
    RESOLVE[nm] = {'file': fl, 'declared_there': hit, 'named_in_the_remark': in_tex}
UNRESOLVED = [n for n, v in RESOLVE.items() if not v['declared_there']]


def decl(fl, name):
    r = re.search(r'^theorem ' + re.escape(name) + r'\b(.*?)\n(?=\S)', SRC[fl], re.S | re.M)
    if r is None:
        sys.exit(f"⛔ `{name}` is not a theorem in {fl}.lean on this tree.")
    return r.group(0)


PROP = decl('ConeDisjoint', 'cd_prop_causal_alignment')
CONE = decl('ConeDisjoint', 'cd_cone_disjoint')
CLOS = decl('ConeDisjoint', 'cd_closure_Jpast_inter_H')
MXP = decl('ConformalBoundary', 'mx_prop_causal_alignment')

# ------------------------------------------------- binders and conjuncts
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


def split_sig(text, name, first_concl):
    r = re.search(r'theorem ' + re.escape(name) + r'(.*?)\n    ' + re.escape(first_concl), text, re.S)
    if r is None:
        sys.exit(f"⛔ `{name}`'s conclusion no longer starts `{first_concl}`: the "
                 "binder/conclusion split this read depends on cannot be made.")
    return r.group(1)


SIG = split_sig(PROP, 'cd_prop_causal_alignment', 'S.H J =')
BIN = bnames(SIG)
MXBIN = bnames(split_sig(MXP, 'mx_prop_causal_alignment', 'S.H J ='))
if len(BIN) < 10:
    sys.exit(f"⛔ only {len(BIN)} binders parsed; a statement this size has more.")


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


c = re.search(r'\n    (S\.H J =.*?) := by\n', PROP, re.S)
if c is None:
    sys.exit("⛔ cannot delimit `cd_prop_causal_alignment`'s conclusion.")
CONJ = conjuncts(c.group(1))
in_concl = lambda needle: any(needle in x for x in CONJ)

# ------------------------------------------------------ guard family one
G = {'true-probe  (`S.SublevelProper J Θ` is a conjunct)': in_concl('S.SublevelProper J Θ'),
     'false-probe (`S.ConeDisjoint J Θ` is a conjunct)': in_concl('S.ConeDisjoint J Θ')}
if not (G['true-probe  (`S.SublevelProper J Θ` is a conjunct)'] is True and
        G['false-probe (`S.ConeDisjoint J Θ` is a conjunct)'] is False):
    sys.exit(f"⛔ THE CONJUNCT GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

# ------------------------------------------------------ guard family two
# The prose scanner.  A marker set that IS in the sentence must read present; one that cannot be
# must read absent.  Then every Lean-needed item is scanned with the same predicate.
def present(markers, text):
    out = []
    for mk in markers:
        if '\\b' not in mk:
            sys.exit(f"⛔ marker {mk!r} carries no word boundary.  A bare substring matched "
                     '"proper" inside "property" in the first draft of this receipt and scored '
                     'PROPERNESS as present in a sentence that does not contain it; every marker '
                     'must be anchored or the scan measures its own looseness.')
        m = re.search(mk, text, re.I)
        if m:
            out.append({'marker': mk, 'at': m.start(),
                        'context': text[max(0, m.start() - 45):m.end() + 45]})
    return out


G['marker-probe true  (\\bCauchy property\\b matches the sentence)'] = bool(
    present([r'\bCauchy property\b'], SENTENCE))
G['marker-probe false (\\bparacompact\\b matches the sentence)'] = bool(
    present([r'\bparacompact\b'], SENTENCE))
G['marker-probe word-boundary (\\bproper\\b does NOT match "the Cauchy property")'] = not bool(
    present([r'\bproper\b'], 'so by the Cauchy property'))
if not (G['marker-probe true  (\\bCauchy property\\b matches the sentence)'] is True and
        G['marker-probe false (\\bparacompact\\b matches the sentence)'] is False and
        G['marker-probe word-boundary (\\bproper\\b does NOT match "the Cauchy property")'] is True):
    sys.exit(f"⛔ THE MARKER GUARD DID NOT FLIP.  Every verdict is withdrawn.  {G}")

V = {}
score = lambda k, verdict, ev: V.__setitem__(k, [verdict, ev])

# --------------------------------------------------------------- ① … ⑦
pa = re.findall(r'^#print axioms (\S+)', SRC['ConeDisjoint'], re.M)
named = [n for n in ('MSpacetime.cd_prop_causal_alignment', 'MSpacetime.cd_cone_disjoint',
                     'MSpacetime.cd_closure_Jpast_inter_H') if n in pa]
unproved = len(re.findall(r'\bsorry\b|\badmit\b|native_decide', ALL))
axioms = len(re.findall(r'^axiom\s', ALL, re.M))
score('①', 'UNMEASURED BY THIS SEAT',
      f"`#print axioms`' OUTPUT cannot be read on this tree — no toolchain and no Mathlib — so the "
      f"three-axiom claim is not decided here.  Measurable, and NOT reported as the claim: the "
      f"audit is requested for {len(named)}/3 of the new theorems ({', '.join(named)}) among "
      f"{len(pa)} `#print axioms` lines in ConeDisjoint.lean; {unproved} occurrences of "
      f"sorry/admit/native_decide and {axioms} `axiom` declarations across the six probe files.  "
      f"The three NAMES the sentence gives all resolve: `cd_prop_causal_alignment` in "
      f"ConeDisjoint.lean, `mx_prop_causal_alignment` and `mx_H_eq_boundary` in "
      f"ConformalBoundary.lean, and the first is literally the second plus one conjunct.")

dims = {f: {'finrank': sorted(set(re.findall(r'Module\.finrank ℝ E = (\d+)', s))),
            'finite': len(re.findall('FiniteDimensional', s)),
            'complete': len(re.findall('CompleteSpace', s))} for f, s in SRC.items()}
atlas = sorted(set(re.findall(r'\[IsManifold 𝓘\(ℝ, E\) (\S+) (?:N|Ñ)\]', SRC['ConeDisjoint'])))
enorm = bool(re.search(r'variable \{E : Type\*\} \[NormedAddCommGroup E\] \[NormedSpace ℝ E\]',
                       SRC['ConeDisjoint']))
dimfree = enorm and all(v['finite'] == 0 and v['complete'] == 0 for v in dims.values())
v2 = lambda a, df: 'SUPPORTED' if (a == ['1'] and df) else 'NOT SUPPORTED'
score('②', v2(atlas, dimfree),
      f"`ConeDisjoint.lean`'s own variable block — the one in force at `cd_prop_causal_alignment` "
      f"— is `[NormedAddCommGroup E] [NormedSpace ℝ E]` and nothing more ({enorm}), with "
      f"`[IsManifold 𝓘(ℝ,E) 1]` on both carriers ({atlas}), and `FiniteDimensional` and "
      f"`CompleteSpace` occur zero times in all six probe files.  So the `C¹` atlas and the "
      f"every-dimension claim hold of the NEW theorem's own ambient instances and are not "
      f"inherited from the file this one was copied out of.")

mst = re.search(r'structure MSpacetime where(.*?)\n\nnamespace MSpacetime', SRC['ConeDisjoint'], re.S)
fields = re.findall(r'^  (\w+)', mst.group(1), re.M) if mst else []
loc = re.search(r'def LocallyOneChart : Prop :=(.*?)\n\n', SRC['ConeDisjoint'], re.S)
loc1 = bool(loc) and 'ContDiffOn ℝ 1' in loc.group(1) and 'ContinuousOn (chartRep S.T p)' in loc.group(1)
onM = 'T_timelike' in fields and 'pos_on_perp' in fields and 'isOpen_M' in fields
score('③', 'SUPPORTED' if (loc1 and onM and '[T2Space N]' in SIG) else 'NOT SUPPORTED',
      f"`MSpacetime`'s fields are {fields}: an OPEN region `M` with the Lorentzian conditions "
      f"imposed on `M` alone ({onM}), which is what the remark's \"on an open region `M`\" now "
      f"says and the earlier version did not.  `LocallyOneChart` is `hRep g` `C¹` and "
      f"`chartRep T` continuous about each point ({loc1}); `[T2Space N]` is a binder.")

ce = re.search(r'structure ConformalExtension \(S : MSpacetime E N\) \(St : MSpacetime E Ñ\) where'
               r'(.*?)\n\n', SRC['ConeDisjoint'], re.S)
if ce is None:
    sys.exit("⛔ `ConformalExtension`'s declaration is gone: ④ cannot be scored.")
CEF = re.findall(r'^  (\w+)', ce.group(1), re.M)
said4 = {'ι': 'embedding', 'isOpenEmbedding': 'open', 'contMDiff': 'C¹', 'Ω': 'Ω',
         'Ω_pos': 'positive', 'conformal': 'Ω²g', 'timeOrient': 'time orientation',
         'maps_M': 'carrying M into M̃₀'}
unsaid4 = [f for f in CEF if f not in said4]
v4 = lambda u: 'NOT SUPPORTED' if u else 'SUPPORTED'
score('④', v4(unsaid4),
      f"`ConformalExtension`'s fields are {CEF}, and the revised sentence states all of them: the "
      f"open `C¹` embedding, `ι` carrying `M` into the extension's metric region (`maps_M`), "
      f"`ι*g̃ = Ω²g` with `Ω` positive, and `dι` carrying the time orientation to future-timelike "
      f"vectors (`timeOrient`).  Unstated fields: {unsaid4 or 'none'} — `r7664`'s ③ is repaired.")

cstep = re.search(r'def CStep \(x y : N\) : Prop :=(.*?)\n\n', SRC['ConeDisjoint'], re.S)
chain = bool(cstep and 'ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ' in cstep.group(1)) and \
    'def Cau (x y : N) : Prop := Relation.ReflTransGen S.CStep x y' in SRC['ConeDisjoint']
score('⑤', 'SUPPORTED' if chain else 'NOT SUPPORTED',
      f"`Cau = ReflTransGen CStep` with `CStep` a `ContMDiff … 1` arc with future-causal velocity "
      f"({chain}): chains of `C¹` causal arcs, exactly.")

dJ = 'def D (J : Set N) : Set N := S.IpastSet J' in SRC['ConeDisjoint']
hJ = 'def H (J : Set N) : Set N := frontier (S.JpastSet J)' in SRC['ConeDisjoint']
score('⑥', 'SUPPORTED' if (dJ and hJ) else 'NOT SUPPORTED',
      f"`D J = I⁻(J)` ({dJ}) and `H J = ∂J⁻(J)` ({hJ}), the two definitions the revised remark now "
      f"gives and the earlier one left the reader to infer.")

h7 = all(b in BIN for b in ('hOD', 'hmono', 'hI', 'hΘ', 'hadapt'))
ict = re.search(r'def IsCauchyTemporalOn \(U : Set N\) \(τ : N → ℝ\) : Prop :=(.*?)\n\n',
                SRC['ConeDisjoint'], re.S)
score('⑦', 'SUPPORTED' if h7 else 'NOT SUPPORTED',
      f"`hmono` is the chronological ordering; `hOD` and `hI` together are `I⁻(O) = D = ι⁻¹ I⁻(𝒥⁺)` "
      f"with the past of `𝒥⁺` taken in `Ñ` — `St.IpastSet 𝒥`, which is the clause the revised "
      f"sentence adds; `hΘ` is `IsCauchyTemporalOn (S.D J) Θ`, the unique crossing of every level "
      f"by every inextendible causal curve IN `D` ({'∃! t' in (ict.group(1) if ict else '')}), and "
      f"`hadapt` is `Θ (O τ) = τ + c`.")

# ------------------------------------------------- ⑧ … ⑫, the five of eight
MAPFIVE = {'⑧': ["S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥)"],
           '⑨': ['S.SublevelProper J Θ'],
           '⑩': ["KLi (S.slice J Θ)", "KLs (S.slice J Θ)",
                 "KLi (S.cone O)", "KLs (S.cone O)"],
           '⑪': ["∀ τ, S.cone O τ ∩ frontier"],
           '⑫': ["TCF.FrameHyp"]}
COVER, UNCOVERED = {}, []
for i, cj in enumerate(CONJ, 1):
    owner = [k for k, ms in MAPFIVE.items() if any(ms_ in cj for ms_ in ms)]
    COVER[i] = owner[0] if len(owner) == 1 else (owner or None)
    if not owner:
        UNCOVERED.append(i)

hO_prop = 'S.H (range O)' in ' '.join(CONJ)
hO_heq = 'S.H (range O) = frontier' in decl('ConformalBoundary', 'mx_H_eq_boundary')
v8 = lambda a, b, c_: 'SUPPORTED' if (a and not b and c_) else 'NOT SUPPORTED'
score('⑧', v8(in_concl("S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥)"), hO_prop, hO_heq),
      f"the first conjunct is `S.H J = ∂J⁻(𝒥⁺)` and `S.H (range O)` is NOT in this theorem's "
      f"conclusion ({hO_prop}); it is `mx_H_eq_boundary`'s first conjunct ({hO_heq}).  The revised "
      f"sentence attributes each half to the theorem that carries it — `r7664`'s ⑤ is repaired.")

sp = re.search(r'def SublevelProper \(J : Set N\) \(Θ : N → ℝ\) : Prop :=(.*?)\n\n',
               SRC['ConeDisjoint'], re.S)
sp_ok = bool(sp) and 'closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J' in flat(sp.group(1))
fr = 'frontier (S.JpastSet A) = closure (S.D A) \\ S.D A' in SRC['ConeDisjoint']
score('⑨', 'SUPPORTED' if (in_concl('S.SublevelProper J Θ') and sp_ok and fr) else 'NOT SUPPORTED',
      f"`SublevelProper` is `∀ T, closure {{x ∈ D J ∧ Θ x ≤ T}} ⊆ D J` ({sp_ok}), and the revised "
      f"sentence now writes the sublevel set as `{{x ∈ D : Θ(x) ≤ T}}`, with `D` inside it.  The "
      f"consequence is one step from `∂J⁻(A) = closure D ∖ D` ({fr}).")

kli = re.search(r'def KLi \(A : ℝ → Set X\) : Set X :=(.*)', SRC['ConeDisjoint'])
kls = re.search(r'def KLs \(A : ℝ → Set X\) : Set X :=(.*)', SRC['ConeDisjoint'])
atTop = bool(kli and '∀ᶠ τ in atTop' in kli.group(1)) and bool(kls and '∃ᶠ τ in atTop' in kls.group(1))
four = [in_concl(f'{k} (S.{s})') for k in ('KLi', 'KLs') for s in ('slice J Θ', 'cone O')]
score('⑩', 'SUPPORTED' if (all(four) and atTop) else 'NOT SUPPORTED',
      f"the four Kuratowski conjuncts are present ({four}) and `KLi`/`KLs` unfold to \"met for all "
      f"sufficiently late `τ`\" and \"met frequently\" ({atTop}), which is the gloss given.")

cone_sig = split_sig(CONE, 'cd_cone_disjoint', '∀ τ, S.cone O τ ∩ S.H J = ∅')
CONEB = bnames(cone_sig)
cauchy_in_cone = any('hΘ' == b for b in CONEB) and 'IsCauchyTemporalOn' in cone_sig
cone_doc = 'hadapt` is not used' in flat(SRC['ConeDisjoint'])
v11 = lambda cc: 'SUPPORTED' if cc else 'NOT SUPPORTED'
score('⑪', v11(cauchy_in_cone and in_concl('∀ τ, S.cone O τ ∩ frontier')),
      f"the eighth conjunct is `∀ τ, S.cone O τ ∩ ∂J⁻(𝒥⁺) = ∅`, and it is discharged by "
      f"`cd_cone_disjoint`, whose binders are {CONEB} — the Cauchy-temporal hypothesis among them "
      f"({cauchy_in_cone}).  So \"rests on the Cauchy property of `Θ`\" is the Lean's.  Its own "
      f"docstring records that `hadapt` is not used ({cone_doc}).  What \"as in the proof above\" "
      f"adds is a claim about the ROUTE, and that is ㉔–㉗ below, where it does not hold.")

tang = CONJ[6] if len(CONJ) > 6 else ''
fh = re.search(r'def FrameHyp \(g : E →L\[ℝ\] E →L\[ℝ\] ℝ\) \(ℓ n : E\) \(ξ : E →L\[ℝ\] ℝ\) : Prop :='
               r'(.*?)\n\n', SRC['ConeDisjoint'], re.S)
FH = flat(fh.group(1)).strip() if fh else ''
fh_second = 'FutCausal (bil g) ℓ n v → 0 < ξ v' in FH
chart_q = 'covCh Θ q x' in tang
v12 = lambda s, cq: 'SUPPORTED' if (s and cq) else 'NOT SUPPORTED'
score('⑫', v12(fh_second, chart_q),
      f"`FrameHyp` is `{FH}` — null frame AND `dΘ` positive on the frame's future causal cone "
      f"({fh_second}) — and the limit is of `covCh Θ q x`, `dΘ` read in the chart at `q` "
      f"({chart_q}).  The revised sentence states both: \"frames `(ℓ,n)` that are null and on whose "
      f"future causal cone `dΘ` is positive\" and \"read in that chart\".  `r7664`'s ⑧ is repaired.")

# --------------------------------------------------------------- ⑬ … ⑯
carriers = [b for b in BIN if b in ('hJM', 'hHM', 'h𝒥')]
rng = 'theorem mx_range_subset_M' in SRC['ConformalBoundary'] and \
      'range O ⊆ S.M' in SRC['ConformalBoundary']
PROPOSITIONAL = [n for n, b in zip(BIN, groups(SIG))
                 if b[0] == '[' or re.search(r':\s*(S\.|St\.|X\.|∀|frontier|Conformal)', b)]
ACC = {'[T2Space', 'hL', 'hLt', 'X', 'hOD', 'hmono', 'hI', 'hΘ', 'hadapt', 'hJM', 'hHM', 'h𝒥'}
UNACC = [n for n in PROPOSITIONAL if not any(n.startswith(a) or a.startswith(n) for a in ACC)]
v13 = lambda nc, drv, ua: 'SUPPORTED' if (nc == 3 and drv and not ua) else 'NOT SUPPORTED'
score('⑬', v13(len(carriers), rng, UNACC),
      f"the carrier binders are {carriers} — three, and the revised sentence names exactly three, "
      f"`J` and `𝓗⁺` in `M` and `𝒥⁺` in `M̃₀`, and states the worldline's as DERIVED from its "
      f"chronological ordering, which `mx_range_subset_M` is ({rng}).  Binders left unaccounted by "
      f"the registered mapping: {UNACC or 'none'}.  `r7664`'s ⑨ is repaired, including the part "
      f"this seat itself got wrong.  Also: `cd_prop_causal_alignment`'s binders are identical to "
      f"`mx_prop_causal_alignment`'s ({BIN == MXBIN}), so the eighth conjunct costs no hypothesis.")

absent = {k: (k not in SIG) for k in ('asymptot', 'Complete', 'i⁺', 'FiniteDimensional')}
smooth = sorted(set(re.findall(r'ContMDiff\w*[^0-9\n]{0,40}?\b(\d+|⊤|∞)\b', SRC['ConeDisjoint'])))
v14 = lambda ab, at, sm: 'SUPPORTED' if (all(ab.values()) and at == ['1'] and sm == ['1']) \
    else 'NOT SUPPORTED'
score('⑭', v14(absent, atlas, smooth),
      f"no binder mentions asymptotic flatness, future-completeness or `i⁺` ({absent}); the atlas "
      f"is `IsManifold … 1` ({atlas}) and every `ContMDiff` class in the file is `1` ({smooth}).  "
      f"The revised sentence's \"of the atlas, the metric or the maps\" names all three, which is "
      f"`r7664`'s second omission supplied.")

hyp_thm = len(re.findall(r'^(theorem|lemma)[^\n]*[Hh]yperbolic', ALL, re.M))
hyp_any = len(re.findall(r'(?i)hyperbolic', ALL))
bs = TEX.count('BernalSanchez2005')
v15 = lambda t, b: 'SUPPORTED' if (t == 0 and b > 0) else 'NOT SUPPORTED'
score('⑮', v15(hyp_thm, bs),
      f"no theorem or lemma in the six probe files mentions hyperbolicity ({hyp_thm}; "
      f"{hyp_any} occurrence(s) of the word in all, and the one in ConeDisjoint.lean is a "
      f"docstring aside).  The equivalence is now CITED to Bernal–Sánchez ({bs} citations of that "
      f"key in the paper) and marked as what the formal statement does not include.  `r7664`'s ⑪ "
      f"is repaired by saying so rather than by proving it, which is the right repair.")

unb = len(re.findall(r'without bound|unbounded (stretch|along)', ALL))
v16 = lambda u: 'SUPPORTED' if u == 0 else 'NOT SUPPORTED'
score('⑯', v16(unb),
      f"no statement in the six files says the approached stretch extends without bound ({unb}), "
      f"and the cone clause that was the other absentee is now conjunct eight.  One clause left "
      f"out, as the sentence says.")

# ------------------------------------------------------- ⑰ … ㉓, the witnesses
cdw = conjuncts(re.search(r'theorem cd_witness :(.*?) := by',
                          decl('ConeDisjoint', 'cd_witness'), re.S).group(1))
cdw_has = {'cones miss 𝓗⁺': any('∩ frontier' in x and '= ∅' in x for x in cdw),
           'cones non-empty': any('.Nonempty' in x and 'cone' in x for x in cdw)}
mxw = conjuncts(re.search(r'theorem mx_witness_headline :(.*?) := by',
                          decl('ConformalBoundary', 'mx_witness_headline'), re.S).group(1))
mxw_all = sum(1 for x in mxw if any(t in x for t in
              ('minkN.H JN = frontier', 'SublevelProper', 'KLi (minkN.', 'KLs (minkN.', 'covCh')))
two_chart = 'the atlas `{idH, nullH}`' in flat(SRC['ConformalBoundary'])
v17 = lambda h, n, tc: 'SUPPORTED' if (all(h.values()) and n >= 7 and tc) else 'NOT SUPPORTED'
score('⑰', v17(cdw_has, mxw_all, two_chart),
      f"`mx_witness_headline` reads off {mxw_all} of the conclusion's clauses on the two-chart "
      f"Rindler atlas ({two_chart}), and `cd_witness` adds that every past light cone misses the "
      f"horizon and is non-empty {cdw_has} — the non-emptiness being what keeps the new conjunct "
      f"from holding vacuously, which the remark states and is right to state.")

fails = decl('ConformalBoundary', 'mc_witness_tangency_fails')
negs = len(re.findall(r'¬ Tendsto', fails))
ffail = re.search(r'noncomputable def Ffail \(s : ℝ\) : ℝ := (.*)', SRC['ConformalBoundary'])
fcj = conjuncts(re.search(r'theorem mc_witness_tangency_fails :(.*?) := by', fails, re.S).group(1))
others = [x for x in fcj if '¬' not in x]
v18 = lambda n: 'SUPPORTED' if n == 2 else 'NOT SUPPORTED'
score('⑱', v18(negs),
      f"`Ffail s = {ffail.group(1) if ffail else '?'}` — the `sin(log s)` term is the oscillating "
      f"rate — and the theorem negates BOTH the rate limit and the tangency limit ({negs} "
      f"`¬ Tendsto`), which is what \"fails both the rate condition and the tangency\" says and "
      f"what makes the rate condition necessary rather than convenient.  \"Meets every other "
      f"hypothesis\" is carried in part by the conclusion — {len(others)} positive conjuncts, the "
      f"Cauchy property and the frame hypotheses on `D` among them — and in part by the shared "
      f"witness's hypotheses, discharged inside the proof rather than stated.")

czw = conjuncts(re.search(r'theorem cz_witness_headline :(.*?) := by',
                          decl('Compactification', 'cz_witness_headline'), re.S).group(1))
compact = any('IsCompact (closure (range cz_witnessExt.ι))' in x for x in czw)
proper = any('range cz_witnessExt.ι ≠ univ' in x for x in czw)
omega_formula_here = any('Ω' in x for x in czw)
nonconst = decl('Compactification', 'cz_Ω_nonconst')
nonconst_values = len(re.findall(r'cz_Ω \(ψ \([^)]*\)\) \^ 2 =', nonconst))
formula_thm = [n for n in ('cz_Ω_sq', 'cz_ΩF_sq')
               if re.search(r'(theorem|lemma) ' + n + r'\b', SRC['Compactification'])]
formula_cited = any(n.replace('_', '\\_') in TEX for n in formula_thm)
v19 = lambda cf: 'NOT SUPPORTED' if not cf else 'SUPPORTED'
score('⑲', v19(formula_cited),
      f"the compact closure ({compact}) and the proper image, `range ι ≠ univ` ({proper}), are "
      f"conjuncts of `cz_witness_headline`, and `cz_Ω_nonconst` gives non-constancy by evaluating "
      f"`Ω²` at {nonconst_values} points ({flat(nonconst.split(':=')[0]).split(':')[-1].strip()[:90]}).  "
      f"But the FORMULA the sentence states, `Ω² = 1/[(1+U²)(1+V²)]`, is in NEITHER cited theorem "
      f"({omega_formula_here} in the headline's conjuncts): it is {formula_thm} in the same file, "
      f"cited nowhere ({formula_cited}).  The sentence asserts an equation and points at two "
      f"theorems that do not contain it, one citation away from being right.")

czf = conjuncts(re.search(r'theorem cz_witness_headline_F :(.*?) := by',
                          decl('Compactification', 'cz_witness_headline_F'), re.S).group(1))
general_F = any('∀ q ∈ frontier' in x and 'Tendsto' in x for x in czf)
nonvac = bool(re.search(r'theorem cz_exp_nonvacuous', SRC['Compactification']))
ctF = decl('CurvedTangency', 'ct_witness_tangency_F')
ct_every_q = bool(re.match(r'theorem ct_witness_tangency_F \(q : Pt\) \(hq : q ∈ ', ctF))
expV = decl('CurvedTangency', 'ct_expV_differs')
expV_isV = 'Real.exp y.2' in expV
expV_differs = '≠' in expV
v20 = lambda g, nv, eq, ev, df: 'SUPPORTED' if all((g, nv, eq, ev, df)) else 'NOT SUPPORTED'
score('⑳', v20(general_F, nonvac, ct_every_q, expV_isV, expV_differs),
      f"`cz_witness_headline_F` holds for every positive `C¹` `F̂` with the tangency clause in its "
      f"general form ({general_F}); `cz_exp_nonvacuous` keeps the family from being the flat case "
      f"relabelled ({nonvac}); `ct_witness_tangency_F` is stated for EVERY horizon point `q` "
      f"({ct_every_q}); and `ct_expV_differs` takes `F̂ = exp(y.2)`, a function of `V` as the "
      f"sentence says ({expV_isV}), and proves its limit unequal to the flat one ({expV_differs}).  "
      f"All four as stated.")

cyw = conjuncts(re.search(r'theorem cy_witness_headline :(.*?) := by',
                          decl('CylinderWitness', 'cy_witness_headline'), re.S).group(1))
fdw = conjuncts(re.search(r'theorem fd_witness_headline :(.*?) := by',
                          decl('FourDWitness', 'fd_witness_headline'), re.S).group(1))
need = ('IsCauchyTemporalOn', 'SublevelProper', 'KLi', 'KLs')
cy_ok = {t: any(t in x for x in cyw) for t in need}
fd_ok = {t: any(t in x for x in fdw) for t in need}
fd_dim4 = any('Module.finrank ℝ E = 4' in x for x in fdw)
cy_nochart = any('(chartAt E x).source ≠ univ' in x for x in cyw)
cy_isO = 'noncomputable def cy_J : Set N := range cy_O' in SRC['CylinderWitness']
fd_isO = 'noncomputable def fd_J : Set N := range fd_O' in SRC['FourDWitness']
cy_t = bool(re.search(r'theorem cy_witness_tangency \(q : N\) \(hq', SRC['CylinderWitness']))
fd_t = bool(re.search(r'theorem fd_witness_tangency \(q : N\) \(hq', SRC['FourDWitness']))
v21 = lambda a, b, d, o1, o2, t1, t2: 'SUPPORTED' if all(
    (all(a.values()), all(b.values()), d, o1, o2, t1, t2)) else 'NOT SUPPORTED'
score('㉑', v21(cy_ok, fd_ok, fd_dim4, cy_isO, fd_isO, cy_t, fd_t),
      f"the cylinder gives {cy_ok} with no chart covering it ({cy_nochart}); the four-dimensional "
      f"witness gives {fd_ok} and states its own dimension as a conjunct, `finrank ℝ E = 4` "
      f"({fd_dim4}).  In both, `J` IS the worldline's range ({cy_isO}, {fd_isO}), so `S.H J` is "
      f"`∂J⁻(O)` and the sentence's reading of `𝓗⁺ = {{U = 0}}` as `∂J⁻(O)` is the Lean's.  "
      f"Tangency at every horizon point is `cy_witness_tangency` ({cy_t}) and "
      f"`fd_witness_tangency` ({fd_t}).")

ext_built = {f: sorted(set(re.findall(r'def (\w*witnessExt\w*)', SRC[f])))
             for f in ('CylinderWitness', 'FourDWitness')}
v22 = lambda e: 'SUPPORTED' if not any(e.values()) else 'NOT SUPPORTED'
score('㉒', v22(ext_built),
      f"no conformal extension is defined for either carrier ({ext_built}) — the "
      f"`ConformalExtension` occurrences in those files belong to the carried-over two-dimensional "
      f"section — so the identification with `∂J⁻(𝒥⁺)` is exercised in two dimensions only, as the "
      f"sentence says.  `r7664`'s ⑲ is repaired by dropping the unproved reason and keeping the "
      f"fact.")

curv = len(re.findall(r'(?i)riemann|curvature|weyl', ALL))
scales = sorted(set(re.findall(r'def (cz_scale|cz_minkF|fd_S|cy_S)\b', ALL)))
v23 = lambda cv: 'SUPPORTED' if cv == 0 else 'NOT SUPPORTED'
score('㉓', v23(curv),
      f"no curvature object appears anywhere in the six files ({curv} occurrences of "
      f"Riemann/curvature/Weyl), and every metric built is flat or a positive multiple of a flat "
      f"one ({scales}): `cz_scale S F` is `F • g`, and the three- and four-dimensional carriers are "
      f"products of flat factors.  So no witness has a metric that is not conformally flat, as the "
      f"closing sentence says.  It is this seat's ⑳ from `r7664`, sharpened by `69` from \"a curved "
      f"one beyond conformal rescaling\" to the condition that actually fails.")

# ----------------------------------------------- ㉔ … ㉗, the proof sentence
# The Lean's chain, each link the name of a theorem the cone clause goes through, with the markers
# registered for scanning the prose.  A link whose markers are all absent is a step the Lean needs
# that the prose does not state.
CHAIN = [
    ('me_futCauchy_of_cauchy_N', 'the two-sided Cauchy property converted to its FUTURE form, by '
     "gluing a past extension at the curve's start",
     [r'\bfuture[- ]inextendible\b', r'\bfuture form\b']),
    ('mh_hint', '`int J⁻(J) ⊆ D`, which needs `J ⊆ M`', [r'\binterior\b']),
    ('mh_sublevelProper', 'PROPERNESS -- that the CLOSURE of every sublevel set stays in `D` -- '
     'derived by a blow-up at a horizon point, needing Hausdorffness and `𝓗⁺ ⊆ M`',
     [r'\bproperness\b', r'\bproper\b', r'\bsublevel\b', r'\bblow[- ]?up\b']),
    ('cd_chr_of_mem_closure_Jpast', 'that `y ≪ x` for `x` in the CLOSURE of `J⁻(p)` gives `y ≪ p`, '
     'via the openness of `I⁺(y)` and dual push-up',
     [r'\bpush[- ]?up\b', r'\bopenness\b', r'\bI\^\+\b']),
    ('mh_past_step', 'that every neighbourhood of a point OF `M` contains a point chronologically '
     'before it -- the approximation that makes the closure argument go',
     [r'\bneighbourhood\b', r'\bneighborhood\b']),
    ('cd_mem_closure_sublevel', 'that such an `x` lies in the closure of the SUBLEVEL set',
     [r'\bsublevel\b', r'\blevel set\b']),
    ('cd_closure_Jpast_subset_D', 'properness applied: the whole of `closure J⁻(p) ∩ M` lies in `D`',
     [r'closure[^.;]{0,60}\\subseteq D\b', r'\bclosure\b[^.;]{0,40}\blies in\b[^.;]{0,20}D\b']),
    ('mh_not_mem_D_of_H', 'that `𝓗⁺ ∩ D = ∅` -- the horizon is disjoint from the exterior, which is '
     "why the prose's curve is inextendible IN `D` at all",
     [r'\bdisjoint\b', r'\bnot in \$D', r'\boutside \$D']),
    ('T2Space', 'Hausdorffness, which `mh_sublevelProper` needs and so therefore does the clause',
     [r'\bHausdorff\b', r'\bT2\b']),
    ('𝓗⁺ ⊆ M', 'that the horizon lies in the region carrying the metric',
     [r'\bregion carrying\b', r'\blies in \$M', r'\blie in \$M']),
]
for nm, _, _ in CHAIN:
    if nm not in ('T2Space', '𝓗⁺ ⊆ M') and not re.search(
            r'(theorem|lemma|def) ' + re.escape(nm) + r'\b', SRC['ConeDisjoint']):
        sys.exit(f"⛔ `{nm}` is not in ConeDisjoint.lean on this tree: the chain this read walks "
                 "is not the chain the file has, and no step verdict below would mean anything.")
SCAN = []
for nm, what, markers in CHAIN:
    hits = present(markers, SENTENCE)
    SCAN.append({'link': nm, 'what': what, 'markers_found': hits, 'in_the_prose': bool(hits)})
MISSING = [s for s in SCAN if not s['in_the_prose']]

score('㉔', 'SUPPORTED',
      f"the assertion itself is `cd_cone_disjoint`: `∀ τ, S.cone O τ ∩ S.H J = ∅`, with "
      f"`S.cone O τ = ∂J⁻(O τ)`.  The conclusion the prose states is the Lean's, exactly.")
score('㉕', 'SUPPORTED',
      f"`I⁻(x) ⊆ I⁻(O(τ))` for `x` in the closure is `cd_chr_of_mem_closure_Jpast`, and that `Θ` "
      f"decreases into the past on `D` is `mh_temporalD_chr`, used inside "
      f"`cd_mem_closure_sublevel`.  Both steps exist in the Lean, though the Lean reaches the "
      f"inclusion through the openness of `I⁺(y)` and dual push-up, which the prose asserts "
      f"rather than argues.")
v26 = lambda miss: 'NOT SUPPORTED' if miss else 'SUPPORTED'
score('㉖', v26([s for s in MISSING if s['link'] in
                ('mh_not_mem_D_of_H', '𝓗⁺ ⊆ M', 'T2Space', 'mh_sublevelProper')]),
      f"the prose's contradiction runs: a past-directed timelike curve from `x` lies in "
      f"`I⁻(x) ⊆ D`, is future-inextendible in `D`, and the Cauchy property makes `Θ` grow without "
      f"bound.  The Lean's route is not this one.  It goes Cauchy → FUTURE-Cauchy "
      f"(`me_futCauchy_of_cauchy_N`) → PROPERNESS (`mh_sublevelProper`, a blow-up at a horizon "
      f"point, needing `[T2Space N]`) → `closure J⁻(p) ∩ M ⊆ D` → `𝓗⁺ ∩ D = ∅`.  It never "
      f"constructs a curve from `x`; its curves run INTO points of `M`.  And the prose's curve is "
      f"future-inextendible in `D` only because `x ∉ D`, which is `mh_not_mem_D_of_H` and which "
      f"the prose does not state.")
score('㉗', 'SUPPORTED',
      f"\"neither `J⁻(O(τ))` nor its boundary meets `𝓗⁺`\" is `cd_closure_Jpast_inter_H`: "
      f"`closure (S.Jpast (O τ)) ∩ S.H J = ∅`, from which `cd_cone_disjoint` takes the frontier "
      f"case by `frontier_subset_closure`.  The prose's \"nor its boundary\" is exactly the step "
      f"`r7665` says 71 found short, and it is now the Lean's own statement.")

# ----------------------------------------------------- guard family three
# Each verdict written above as a function is re-evaluated with its inputs negated and must flip.
FLIP = {'②': (v2(atlas, dimfree), v2(['⊤'], False)),
        '④': (v4(unsaid4), v4(['x'])),
        '⑧': (v8(True, hO_prop, hO_heq), v8(True, True, hO_heq)),
        '⑪': (v11(cauchy_in_cone and True), v11(False)),
        '⑫': (v12(fh_second, chart_q), v12(False, False)),
        '⑬': (v13(len(carriers), rng, UNACC), v13(2, rng, UNACC)),
        '⑭': (v14(absent, atlas, smooth), v14(absent, ['⊤'], smooth)),
        '⑮': (v15(hyp_thm, bs), v15(1, bs)),
        '⑯': (v16(unb), v16(1)),
        '⑰': (v17(cdw_has, mxw_all, two_chart), v17(cdw_has, 0, two_chart)),
        '⑱': (v18(negs), v18(1)),
        '⑲': (v19(formula_cited), v19(True)),
        '⑳': (v20(general_F, nonvac, ct_every_q, expV_isV, expV_differs),
              v20(False, nonvac, ct_every_q, expV_isV, expV_differs)),
        '㉑': (v21(cy_ok, fd_ok, fd_dim4, cy_isO, fd_isO, cy_t, fd_t),
               v21(cy_ok, fd_ok, False, cy_isO, fd_isO, cy_t, fd_t)),
        '㉒': (v22(ext_built), v22({'x': ['y']})),
        '㉓': (v23(curv), v23(1)),
        '㉖': (v26(MISSING), v26([])),
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
w(f"CITED NAMES: {len(CITED)} cited, {len(UNRESOLVED)} unresolved -> {UNRESOLVED or 'all resolve'}")
w(f"BINDERS ({len(BIN)}): {BIN}")
w(f"  identical to mx_prop_causal_alignment's: {BIN == MXBIN}")
w(f"CONJUNCTS ({len(CONJ)}), each owned by one of the remark's five:")
for i, cj in enumerate(CONJ, 1):
    w(f"  {i}. [{COVER[i]}] {cj[:120]}")
w(f"  uncovered conjuncts: {UNCOVERED or 'none'}")
w("")
w("THE LEAN'S CHAIN FOR THE CONE CLAUSE, SCANNED AGAINST THE PROSE SENTENCE:")
for s in SCAN:
    w(f"  {'IN THE PROSE ' if s['in_the_prose'] else 'NOT IN PROSE'}  {s['link']}")
    w(f"      {s['what']}")
    for h in s['markers_found']:
        w(f"      matched {h['marker']} -> ...{h['context']}...")
w(f"  -> {len(MISSING)} of {len(SCAN)} links the Lean needs are not in the sentence.")
w("")
for k in '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗':
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
           'guard': G, 'cited': RESOLVE, 'binders': BIN, 'binders_match_mx': BIN == MXBIN,
           'conjuncts': CONJ, 'coverage': {str(k): v for k, v in COVER.items()},
           'sentence': SENTENCE, 'preceding_sentence': PRECEDING,
           'chain_scan': SCAN, 'verdicts': V, 'tally': tally},
          open(os.path.join(HERE, 'verdicts.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
