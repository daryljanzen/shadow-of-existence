#!/usr/bin/env python3
"""r7726 (60) -- which surface P3 commits to beyond a horizon, answering order r7723.

Three questions: is the |f|-reading or the continuation the surface P3 commits to past a horizon;
if the continuation, does the static-region scoping leave anything false; if the |f|-reading, draft
the sign clause back in.

⛭ The deciding arms are stated as readings of P3's own text with BOTH outcomes named, and none of
them mentions r7724 -- the instrument is not shown which answer flatters its author.

Run:  python3 probe.py
"""
import math
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P3 = os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
SKY = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'SlicingSky.lean')
HINGE = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'SlicingHinge.lean')

FAILED, NOTES = [], []


def say(*a):
    print(*a)


def need(label, ok, witness=''):
    if not ok:
        FAILED.append(label)
    say(f'  [{"PASS" if ok else "FAIL"}] {label}')
    for line in str(witness).split('\n'):
        if line:
            say(f'         ⌗ {line}')


def head(t):
    say('')
    say('  ' + '=' * 96)
    say('  ' + t)
    say('  ' + '=' * 96)


# ═════════════════════════════════════════ READERS ════════════════════════════════════════════
def flat(s):
    return re.sub(r'\s+', ' ', s)


def greek_table(*texts):
    """⚠ r7724's own defect: filtering on 'LETTER' misses `ϱ`, which is GREEK RHO SYMBOL.
    SYMBOL is accepted here, and the table is still GENERATED rather than written out."""
    out = {}
    for t in texts:
        for ch in set(t):
            if ord(ch) < 128:
                continue
            try:
                nm = unicodedata.name(ch)
            except ValueError:
                continue
            if 'GREEK' in nm and ('LETTER' in nm or 'SYMBOL' in nm):
                key = 'LETTER' if 'LETTER' in nm else 'GREEK'
                out[ch] = nm.split(key)[-1].strip().lower().replace(' ', '_')
    return out


def decl_extent(src, name):
    m = re.search(r'^(?:theorem|lemma|def|noncomputable def|abbrev)\s+' + re.escape(name)
                  + r'(?=[\s({\[:])', src, re.M)
    if not m:
        return None
    nxt = re.search(r'^(?:/--|@\[|theorem|lemma|def|noncomputable def|abbrev|instance|example)\s',
                    src[m.end():], re.M)
    return src[m.start(): m.end() + (nxt.start() if nxt else len(src) - m.end())]


def decl_statement(src, name):
    """Bounded by the `:= by` that BEGINS A PROOF, never by the first `:=` -- r7720 and r7722."""
    ext = decl_extent(src, name)
    if ext is None:
        return None
    for pat in (' := by', ':= by'):
        k = ext.find(pat)
        if k > 0:
            return ext[:k].strip()
    return ext.strip()


def conclusion_of(statement):
    """At BRACKET DEPTH ZERO -- r7720."""
    depth = 0
    for k, ch in enumerate(statement):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0 and statement[k:k + 2] != '::':
            return statement[k + 1:].strip()
    return statement


def hypotheses_of(statement):
    """Binder groups at depth 1, bounded by the same depth-zero colon -- r7724's two defects."""
    head_, depth = statement, 0
    for k, ch in enumerate(statement):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0 and statement[k:k + 2] != '::':
            head_ = statement[:k]
            break
    out, buf, depth = [], '', 0
    for ch in head_:
        if ch in '({[':
            depth += 1
            if depth == 1:
                buf = ''
                continue
        elif ch in ')}]':
            if depth == 1:
                out.append(buf.strip())
                depth -= 1
                continue
            depth -= 1
        if depth >= 1:
            buf += ch
    return out


def env_body(tex, label):
    m = re.search(r'\\begin\{(\w+)\}(?:\[[^\]]*\])?\\label\{' + re.escape(label) + r'\}', tex)
    if not m:
        m = re.search(r'\\begin\{(\w+)\}[^\n]*?\\label\{' + re.escape(label) + r'\}', tex)
    if not m:
        return None
    end = tex.find('\\end{' + m.group(1) + '}', m.end())
    return tex[m.end(): end] if end > 0 else None


def where_token(src, tok):
    """⚠ r7724's third defect: a token search must say WHERE a hit sits, because a NAME is a form.
    Returns (total, in_statements, in_section_headers, in_docstrings_or_comments)."""
    total = len(re.findall(re.escape(tok), src))
    in_stmt = sum(1 for n in re.findall(r'^theorem\s+(\S+)', src, re.M)
                  if tok in (decl_statement(src, n) or ''))
    in_sect = len(re.findall(r'^section \S*' + re.escape(tok), src, re.M))
    return total, in_stmt, in_sect, total - in_stmt - in_sect


# ═══════════════════════════════════ THE GEOMETRY, gauge α = 1 ════════════════════════════════
def f_of(m, r):
    return 1.0 - m / r - r * r                      # m = 2M


def fprime(m, r):
    return m / (r * r) - 2.0 * r


def KG_expr(m, r):
    return 1.0 - (m / 2.0) / r ** 3                 # 1/α² − M/r³, with M = m/2


def sl_g(t):
    return t - t ** 3


def cubic(m, r):
    return r ** 3 - r + m


def roots_of(m):
    xs, out = [i * 0.0005 - 3.0 for i in range(12001)], []
    for a, b in zip(xs, xs[1:]):
        if cubic(m, a) == 0.0:
            out.append(a)
        elif cubic(m, a) * cubic(m, b) < 0:
            lo, hi = a, b
            for _ in range(200):
                mid = (lo + hi) / 2
                if cubic(m, lo) * cubic(m, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            out.append((lo + hi) / 2)
    return sorted(set(round(r, 12) for r in out))


def rsecond_riemannian(m, r):
    """r''(l) along dr/dl = √|f|, as P3's own proof gives it: ½f′·sgn f."""
    s = f_of(m, r)
    return 0.5 * fprime(m, r) * (1.0 if s > 0 else (-1.0 if s < 0 else 0.0))


def rsecond_lorentzian(m, r):
    """r''(ψ) on the CONTINUED piece, where (dr/dψ)² = −f and the parameter is proper time:
    d/dψ √(−f) = √(−f) · (−f′)/(2√(−f)) = −f′/2."""
    return -0.5 * fprime(m, r)


def K_riemannian(m, r):
    """ds² = dl² + r²dφ², signature (+,+):  K = −r''/r."""
    return -rsecond_riemannian(m, r) / r


def K_lorentzian(m, r):
    """ds² = −dψ² + r²dφ², signature (−,+):  K = +r''/r."""
    return rsecond_lorentzian(m, r) / r


# ═════════════════════════════════════════ SELF-TESTS ═════════════════════════════════════════
def selftests(p3, sky, hinge):
    head('Ⓢ  THE INSTRUMENT, TESTED BEFORE USE -- every reader shown a NEGATIVE of the opposite class')
    gt = greek_table(p3, sky, hinge)
    need('Ⓢ① the generated character table now accepts SYMBOL as well as LETTER, so `ϱ` -- GREEK '
         'RHO SYMBOL, which r7724\'s own generator missed -- is present, along with `σ`, `χ`, `ψ`, `θ`',
         all(c in gt for c in 'ϱσχψθ'),
         'ϱ→{}, σ→{}, χ→{}, ψ→{}, θ→{}; {} letters found'.format(
             gt.get('ϱ'), gt.get('σ'), gt.get('χ'), gt.get('ψ'), gt.get('θ'), len(gt)))

    st = decl_statement(hinge, 'sl_tangent_height')
    need('Ⓢ② `decl_statement` stops at the `:= by` that begins a proof and not at a `:=` inside',
         st is not None and ':= by' not in st and 'Real.sqrt 3 * α' in st,
         f'{len(st)} chars, ends …{st[-40:]!r}' if st else 'NOT FOUND')
    need('Ⓢ③ and returns None for a name that is not there (the negative)',
         decl_statement(hinge, 'sl_not_a_declaration_r7726') is None, 'None as required')

    cast = 'theorem t (x : ℝ) (h : ((x : ℝ) : ℂ) ≠ 0) :\n    A ∧ ((x : ℝ) : ℂ) = 0 := by\n  sorry\n'
    need('Ⓢ④ `conclusion_of` reads at bracket depth ZERO: a nested ascription in the hypotheses '
         'does not steal the split (r7720\'s defect, injected)',
         conclusion_of(decl_statement(cast, 't')).startswith('A ∧'),
         f'read {conclusion_of(decl_statement(cast, "t"))!r}')
    need('Ⓢ⑤ `hypotheses_of` keeps nested closing brackets and stops before the conclusion '
         '(r7724\'s two defects, both injected here)',
         hypotheses_of(decl_statement(sky, 'sl_conjugacy')) == ['x : ℝ', 'hx : x ∈ Set.Icc (0 : ℝ) 1'],
         f'{hypotheses_of(decl_statement(sky, "sl_conjugacy"))}')
    need('Ⓢ⑥ `env_body` locates by LABEL, and returns None for a label not present',
         env_body(p3, 'prop:flip') is not None and env_body(p3, 'prop:nope_r7726') is None,
         f'prop:flip body {len(env_body(p3, "prop:flip"))} chars; absent label → None')
    need('Ⓢ⑦ `where_token` separates a statement hit from a section-header hit -- the shape that '
         'produced r7724\'s false positive', where_token(sky, 'KG')[2] == 8,
         'in SlicingSky.lean, `KG`: total {}, in statements {}, in `section KG…` headers {}, '
         'elsewhere {}'.format(*where_token(sky, 'KG')))

    need('Ⓢ⑧ the root finder returns the known roots of r³ − r at m = 0',
         [round(r, 9) for r in roots_of(0.0)] == [-1.0, 0.0, 1.0], f'{roots_of(0.0)}')
    need('Ⓢ⑨ ⚠ and the two curvature conventions are verified on a case whose answer is known '
         'INDEPENDENTLY: on the de Sitter member (m = 0) the spherical piece and the continued '
         'Lorentzian piece must both give the constant +1/α² = +1',
         abs(K_riemannian(0.0, 0.5) - 1.0) < 1e-12 and abs(K_lorentzian(0.0, 1.5) - 1.0) < 1e-12,
         f'm = 0: f(0.5) = {f_of(0.0, 0.5):+.4f} (static) → K_riem = {K_riemannian(0.0, 0.5):+.12f}; '
         f'f(1.5) = {f_of(0.0, 1.5):+.4f} (past the seam) → K_lor = {K_lorentzian(0.0, 1.5):+.12f}\n'
         'the second is the order\'s own statement that the continued piece keeps 1/α², reproduced '
         'here, so the Lorentzian convention K = +r″/r is not assumed but checked against it')
    need('Ⓢ⑩ and the conventions DISAGREE where they should: read as a Riemannian surface with the '
         'modulus, the same de Sitter radius gives −1, which is the reading the two differ over',
         abs(K_riemannian(0.0, 1.5) + 1.0) < 1e-12,
         f'K_riem(m=0, r=1.5) = {K_riemannian(0.0, 1.5):+.12f} against K_lor = '
         f'{K_lorentzian(0.0, 1.5):+.12f} -- so an arm that cannot tell the two apart would decide '
         f'this revision\'s question by its own convention')
    return gt


# ═══════════════════ Ⓐ  WHAT P3 COMMITS TO BEYOND A HORIZON (the deciding group) ═══════════════
def arm_A(p3):
    head('Ⓐ  WHAT P3 COMMITS TO BEYOND A HORIZON -- read from its own text, both outcomes named')
    fp = flat(p3)

    i = fp.find('The turning points of the slicing curve are the horizons')
    need('Ⓐ① ⛭ FIRST, THE LABEL: is a "seam" the same locus as a horizon, or a different one? The '
         'seam section\'s OWN FIRST SENTENCE settles it by definition, so the question "what is the '
         'surface past a horizon" and "what is the surface past a seam" are one question',
         i > 0 and 'We call such a turning point a \\emph{seam}' in fp[i:i + 420],
         '…' + fp[i:i + 300] + '…')

    need('Ⓐ② THE ABSTRACT commits the two-dimensional slicing surface, at the seam, to the '
         'CONTINUATION and to a LORENTZIAN piece -- not to a Riemannian surface read with the '
         'modulus', 'the equatorial seam joins a Riemannian spherical piece to a Lorentzian '
         'de~Sitter piece by the continuation $\\theta\\mapsto\\pi/2+i\\psi$, the signature flip '
         'automatic and confined to the two-dimensional slicing surface' in fp,
         'the abstract says: "…joins a Riemannian spherical piece to a Lorentzian de Sitter piece '
         'by the continuation θ ↦ π/2 + iψ, the signature flip automatic and CONFINED TO THE '
         'TWO-DIMENSIONAL SLICING SURFACE, the spacetime Lorentzian throughout"')

    st = flat(env_body(p3, 'prop:flip') or '')
    need('Ⓐ③ `prop:flip`\'s STATEMENT, not its remark: its subject is the LINE ELEMENT, and its '
         'conclusion is a signature',
         'the spherical line element' in st and 'of Lorentzian signature $(-,+)$' in st,
         f'…{st.strip()[:230]}…')

    need('Ⓐ④ and the correspondence subsection says WHICH signature flips, in so many words -- the '
         'two-dimensional slicing-surface metric\'s, the radial direction reading spacelike inside '
         'and timelike outside',
         'The signature that flips here is that of this two-dimensional slicing-surface metric' in fp
         and 'timelike on the de~Sitter (cosmological) piece $r>\\alpha$' in fp,
         'located verbatim; and it adds "It is not the signature of the spacetime, which is '
         'Lorentzian throughout"')

    rl = flat(env_body(p3, 'rem:reality-lines') or '')
    need('Ⓐ⑤ `rem:reality-lines` carries the same commitment and adds that BOTH pieces are real '
         'and the join is C¹ -- so the continued piece is an object of the construction and not a '
         'formal device',
         'both pieces are real' in rl and 'the join is $C^{1}$' in rl
         and 'along which $r=\\cosh\\psi$ is the Lorentzian one' in rl,
         f'…{rl.strip()[:200]}…')

    # Ⓐ⑥ -- the named search, in both directions
    mod_phrases = ['ds^{2}=dl^{2}+r(l)^{2}d\\phi^{2}', 'read with the modulus', '\\sqrt{|f(r)|}',
                   '\\sqrt{\\lvert f\\rvert}']
    hits = {ph: fp.count(ph) for ph in mod_phrases}
    where_mod = []
    for mm in re.finditer(re.escape('read with the modulus'), fp):
        where_mod.append(fp[max(0, mm.start() - 150): mm.start() + 60])
    need('Ⓐ⑥ ⛭⛭ THE DECIDING SEARCH, named and in both directions: does any sentence of P3 apply '
         'the Riemannian surface line element with the modulus law at a radius where f < 0? **It '
         'does not** -- the only place the modulus reading appears beyond the static region is the '
         'formal sentence that explicitly contrasts it with the continuation. So the modulus is '
         'P3\'s law for the CURVE and the continuation is its account of the SURFACE',
         len(where_mod) == 1 and 'whereas past a seam the slicing surface is carried by the '
         'continuation' in fp,
         'searched for ' + ', '.join(f'{k!r}: {v}' for k, v in hits.items())
         + f'\n"read with the modulus" occurs {len(where_mod)} time(s), and its context is:\n'
         + '\n'.join('   …' + w + '…' for w in where_mod))

    need('Ⓐ⑦ ⇒ **THE ANSWER TO THE ORDER\'S FIRST QUESTION: THE CONTINUATION.** And the fork was '
         'not a two-way one: P3 commits to BOTH readings, of TWO DIFFERENT OBJECTS -- the modulus '
         'law for the one-dimensional curve (the abstract defines the curve by it) and the '
         'continuation for the two-dimensional surface past a seam. The paper now states that '
         'distinction itself, in the formal sentence after `prop:curvature`\'s proof',
         'defined by $dr/dl=\\sqrt{|f(r)|}$' in fp
         and 'whereas past a seam the slicing surface is carried by the continuation of '
             'Proposition~\\ref{prop:flip}' in fp,
         'the abstract: "a single radial curve $r(l)$, defined by $dr/dl=\\sqrt{|f(r)|}$" -- the '
         'CURVE;\nthe formal sentence: "…whereas past a seam the slicing surface is carried by the '
         'continuation of Proposition prop:flip" -- the SURFACE')
    NOTES.append('Ⓐ⑦ the surface past a seam is the continuation; the modulus law is the curve\'s')


# ═══════════ Ⓑ  WHAT THE FORMALISATION COMMITS TO, which is a different question ══════════════
def arm_B(sky, hinge, p3):
    head('Ⓑ  WHAT THE FORMALISATION COMMITS TO -- the curve, or a surface?')
    st = decl_statement(sky, 'sl_curvature_sign')
    hyp = hypotheses_of(st)
    need('Ⓑ① `sl_curvature_sign` quantifies over a CURVE `r : ℝ → ℝ` satisfying the modulus law, '
         'and over no surface at all -- so what it proves is a fact about the curve, and the '
         'distinction Ⓐ⑦ found is already present in Lean and was only absent from the prose',
         any('r : ℝ → ℝ' in h for h in hyp)
         and any('Real.sqrt |sl_f m (r t)|' in h for h in hyp),
         f'binders: {hyp}')

    t_sky = where_token(sky, 'K_G')
    need('Ⓑ② and it is about `-a / r l`, i.e. −r″/r: `K_G` appears once in that file, in a '
         'DOCSTRING and in no statement, and "Gauss" nowhere -- so the surface-of-revolution bridge '
         'is cited and unformalised, exactly as the paragraph says',
         t_sky[1] == 0 and re.search(r'[Gg]auss', sky) is None,
         '`K_G` in SlicingSky.lean: total {}, in statements {}, in section headers {}, '
         'elsewhere {}'.format(*t_sky) + f"; 'Gauss': {len(re.findall(r'[Gg]auss', sky))}")

    sf = decl_statement(hinge, 'sl_flip')
    need('Ⓑ③ `sl_flip` is about the CONTINUATION itself -- the derivative of θ ↦ π/2 + ψi, that '
         'i² = −1, that sin(π/2 + ψi) = cosh ψ, and the two signs −1 < 0 < cosh²ψ that ARE the '
         'signature -- and it is in `SlicingHinge.lean`, which is the file the paper cites',
         'Complex.I ^ 2 = -1' in sf and 'Complex.sin (π / 2 + ψ * Complex.I) = Real.cosh ψ' in sf
         and '(-1 : ℝ) < 0 ∧ 0 < Real.cosh ψ ^ 2' in sf
         and 'in \\texttt{SlicingHinge' in flat(p3),
         f'conclusion: {flat(conclusion_of(sf))}')
    th = where_token(hinge, 'K_G')
    need('Ⓑ④ ⚠ and no STATEMENT in either file gives the Gaussian curvature of the CONTINUED '
         'piece: the token sits in a docstring and nowhere else, and "Gauss" is absent from both '
         'files -- so the machine answer to "what is the curvature past a seam" does not exist '
         'yet, which is consistent with that computation being ordered elsewhere',
         th[1] == 0 and re.search(r'[Gg]auss', hinge) is None,
         'in SlicingHinge.lean, `K_G`: total {}, in statements {}, in section headers {}, '
         'elsewhere (docstrings and comments) {}'.format(*th)
         + f"; 'Gauss': {len(re.findall(r'[Gg]auss', hinge))}")

    doc = re.search(r"/--[^/]*?the paper's `K_G[^/]*?-/", hinge, re.S)
    stale = doc.group(0) if doc else ''
    in_both = sum(1 for f in (sky, hinge) if 'the sign flips outside the static region' in f)
    need('Ⓑ⑤ ⛔⛭⛭ **BUT THE CORRECTION DID NOT REACH THE DOCSTRING, AND THE DOCSTRING MAKES THE '
         'VERY CONFLATION THE PAPER JUST REMOVED.** `sl_curvature_sign` is headed, in BOTH files, '
         'by a docstring calling the quantity "the paper\'s `K_G`" and saying "the sign flips '
         'outside the static region". What the theorem proves is about the CURVE read with the '
         'modulus; the paper\'s `K_G` is the SURFACE\'s, and past a seam that surface is the '
         'continuation. So the clause removed from `prop:curvature` is still asserted here, of '
         'the paper\'s own symbol',
         in_both == 0,
         f'present in {in_both} of the two files, verbatim:\n   {flat(stale)}')
    NOTES.append("Ⓑ⑤ sl_curvature_sign's docstring still asserts the removed clause of the "
                 "paper's own K_G, in both files")

    # ⚠ a sixth defect of this probe, caught by reading its own witness: `[a-z_0-9]+` truncates a
    # name at its first non-ASCII character, so `bs_Φ…` was printed as `bs_`.  The class is the
    # same one every defect of this line has been -- a pattern that is a form, not the thing.
    names_s = set(re.findall(r'^theorem ([^\s({\[:]+)', sky, re.M))
    names_h = set(re.findall(r'^theorem ([^\s({\[:]+)', hinge, re.M))
    shared = sorted(names_s & names_h)
    need('Ⓑ⑥ ⛔⛭ **AND A SECOND FINDING THE FIRST UNCOVERED: the two files declare the same '
         'theorem NAMES in bulk.** So a citation naming a declaration and a file is ambiguous '
         'about which copy a reader is sent to -- and the paper cites `sl_curvature_sign` to one '
         'file while the other declares it too, with the same stale docstring',
         len(shared) == 0,
         f'SlicingSky declares {len(names_s)} theorems, SlicingHinge {len(names_h)}, and '
         f'{len(shared)} names are declared in BOTH\nfirst ten: {shared[:10]}')
    NOTES.append(f'Ⓑ⑥ {len(shared)} theorem names are declared in both Lean files')


# ═════════════ Ⓒ  THE ARITHMETIC -- and whether the scoping leaves anything false ══════════════
def arm_C(p3):
    head('Ⓒ  THE CURVATURE OF THE CONTINUED PIECE, AND THE ORDER\'S SECOND QUESTION')
    fp = flat(p3)

    # ⛭⛭ the computation the whole answer turns on
    members = [('de Sitter, m = 0', 0.0), ('undercritical, r₀ = 0.3', sl_g(0.3)),
               ('undercritical, r₀ = 0.8', sl_g(0.8)), ('near-Nariai, r₀ = 0.57', sl_g(0.57))]
    rows, ok = [], True
    for nm, m in members:
        rr = [r for r in roots_of(m) if r > 0]
        test = [r for r in (0.12, 0.2, 1.4, 2.0, 2.6) if f_of(m, r) < 0 and r > 0]
        for r in test:
            kl, ke = K_lorentzian(m, r), KG_expr(m, r)
            kr = K_riemannian(m, r)
            rows.append((nm, r, f_of(m, r), ke, kl, kr))
            if abs(kl - ke) > 1e-9:
                ok = False
    need('Ⓒ① ⛭⛭ **THE FORMULA IS UNCHANGED ON THE CONTINUED PIECE, FOR EVERY MEMBER AND NOT ONLY '
         'DE SITTER.** On the Lorentzian piece the parameter is proper time, (dr/dψ)² = −f, so '
         'r″(ψ) = −f′/2; and for signature (−,+) the Gaussian curvature is K = +r″/r. The two sign '
         'flips -- the sgn f in r″ and the convention in K -- CANCEL, giving K = −f′/2r = '
         '1/α² − M/r³ exactly, the same expression as on the static region',
         ok,
         '\n'.join(f'{nm:<26} r={r:<5} f={s:+9.4f}  1/α²−M/r³={e:+12.6f}  K_continued={l:+12.6f}  '
                   f'(modulus-as-Riemannian would give {kr:+12.6f})'
                   for nm, r, s, e, l, kr in rows))
    NOTES.append('Ⓒ① on the continued piece K = 1/α² − M/r³ unchanged, the two sign flips cancelling')

    need('Ⓒ② ⚠ and P3 ALREADY CONTAINS BOTH HALVES OF THAT COMPUTATION WITHOUT JOINING THEM: it '
         'states the marginal congruence\'s areal acceleration as d²r/dτ̃² = −f′/2, which IS the '
         'r″(ψ) above, and it states K_G = −f′/2r identically. What it does not say is that the '
         'first is the continued piece\'s own r″ and therefore that the second holds there too',
         'For the marginal congruence the areal acceleration is $\\dd^{2}r/\\dd\\tilde\\tau^{2}=-f\'/2$'
         in fp and 'K_{G}=-f\'/2r$ identically' in fp,
         'both located verbatim in the paper; the missing step is one line: on the Lorentzian piece '
         'r″(ψ) = −f′/2 and K = +r″/r, so K = −f′/2r')

    need('Ⓒ③ the proposition is now scoped and the sign clause is gone from it',
         'On the static region $f>0$' in flat(env_body(p3, 'prop:curvature') or '')
         and 'its sign is reversed' not in flat(env_body(p3, 'prop:curvature') or ''),
         f'…{flat(env_body(p3, "prop:curvature")).strip()[:150]}…')

    # consequence two: now a LIMIT claim
    m = sl_g(0.3)
    rr = [r for r in roots_of(m) if r > 0]
    lims = []
    for rh in rr:
        inside = rh + 1e-7 if f_of(m, rh + 1e-7) > 0 else rh - 1e-7
        lims.append((rh, KG_expr(m, rh), KG_expr(m, inside)))
    need('Ⓒ④ CONSEQUENCE TWO is now a LIMIT claim and it is TRUE: approaching a horizon from '
         'inside the static region, K_G tends to 1/α² − M/r_h³, which is finite. ⌗ And it no longer '
         'asserts a value AT the horizon, which is what the earlier wording did',
         'the curvature tends to $1/\\alpha^{2}-M/r_{h}^{3}$' in fp
         and all(abs(a - b) < 1e-5 for _, a, b in lims),
         '\n'.join(f'r_h = {rh:.6f}: value at r_h {a:+.9f}, approached from inside {b:+.9f}'
                   for rh, a, b in lims))

    # consequence three: once within the static region
    zeros = [(nm, (m / 2.0) ** (1 / 3.0) if m > 0 else None, [r for r in roots_of(m) if r > 0])
             for nm, m in (('r₀ = 0.3', sl_g(0.3)), ('r₀ = 0.8', sl_g(0.8)))]
    good = all(z is not None and rs and rs[0] < z < rs[-1] for _, z, rs in zeros)
    need('Ⓒ⑤ CONSEQUENCE THREE\'s "within the static region … changes sign once" is TRUE on the '
         'members it is about: K_G has exactly ONE zero in r > 0 (r³ = Mα² has one positive root), '
         'and it lies strictly between the two horizons',
         good,
         '\n'.join(f'{nm}: horizons {[round(x, 6) for x in rs]}, r_HE = {z:.6f}, strictly between: '
                   f'{rs[0] < z < rs[-1]}' for nm, z, rs in zeros)
         + '\nand K_G = 0 ⟺ r³ = Mα², one positive root, so "once" cannot fail by a second zero')

    need('Ⓒ⑥ ⚠ and the abstract\'s "changing sign once **there**" resolves to the static region by '
         'its own sentence, which is the pronoun checked rather than assumed',
         'finite throughout the static region, invisible to the horizons, and changing sign once '
         'there' in fp,
         'the abstract: "…finite throughout the static region, invisible to the horizons, and '
         'changing sign once there, at $r_{\\mathrm{HE}}$…" -- "there" follows "the static region" '
         'in the same list, with no competing antecedent between them')

    # C7 -- does the scoping leave anything false?
    unscoped = []
    for ph, why in (
        ('the comoving acceleration is the slice\'s own Gaussian curvature, up to the positive '
         'factor $r$', 'a comoving worldline crosses horizons, so this needs K_G outside f > 0'),
        ('The sign of the intrinsic curvature of the existent slice \\emph{is} the sign of the '
         'cosmic acceleration', 'a cosmic history crosses horizons'),
        ('$\\Lambda$-dominated and positively curved (de~Sitter-like, expanding) beyond it',
         '"beyond $r_{HE}$" is unbounded and leaves the static region')):
        if ph in fp:
            unscoped.append((ph, why))
    need('Ⓒ⑦ ⛔⛭ **THE ORDER\'S SECOND QUESTION: YES, THE SCOPING LEAVES THREE DOWNSTREAM SENTENCES '
         'UNSUPPORTED** -- all of them in the cosmological reading, all of them calling K_G "the '
         'slice\'s own Gaussian curvature" at radii the now-scoped proposition does not reach. ⌗ '
         'But by Ⓒ① the remedy is to EXTEND rather than to scope: the formula holds on the '
         'continued piece too, so these sentences were right all along and it is the proposition '
         'that is now narrower than the paper needs',
         len(unscoped) == 0,
         '\n'.join(f'• "{ph[:96]}…"\n    ⇒ {why}' for ph, why in unscoped))
    NOTES.append('Ⓒ⑦ three cosmological sentences need K_G outside the static region')


# ═════════════════════════════════ Ⓓ  THE REST OF THE LANDING ═════════════════════════════════
def arm_D(p3, p15, sky, hinge):
    head('Ⓓ  THE REST OF THE LANDING -- each a citation against a statement')
    fp = flat(p3)

    need('Ⓓ① `prop:turning`\'s new wording says what `sl_accel_pos`/`sl_accel_neg` state -- a '
         'one-sided limit with the sign by the side -- checked against the DECLARATIONS and not '
         'against the words that were offered for it',
         'from either side' in fp and 'the sign according as $f\\gtrless0$ there' in fp
         and "\\longrightarrow\\;\\pm\\tfrac12 f'(r_{h})\\neq0" in fp
         and 'HasDerivAt (deriv r) (f\' / 2) l' in flat(decl_statement(sky, 'sl_accel_pos'))
         and 'HasDerivAt (deriv r) (-f\' / 2) l' in flat(decl_statement(sky, 'sl_accel_neg')),
         'the proposition now reads "…→ ±½f′(r_h) ≠ 0 as r → r_h from either side, the sign '
         'according as f ≷ 0 there", and the two declarations give +f′/2 under 0 < f and −f′/2 '
         'under f < 0 -- the pair the wording names')

    cj = fp[fp.find('The conjugacy is machine-checked'):][:420]
    need('Ⓓ② the conjugacy citation now closes BEFORE the amount, so what it covers is what the '
         'two declarations conclude and no more -- this seat\'s ⓸ of last round, landed',
         0 < cj.find('SlicingSky.lean})') < cj.find('differing'),
         f"the citation closes at offset {cj.find('SlicingSky.lean})')} and the amount begins at "
         f"{cj.find('differing')}:\n   …{cj[:290]}…")

    need('Ⓓ③ `prop:triple` now says "the unique **positive** value", matching '
         '`sl_triple_unique`\'s `0 < ϱ`',
         'the unique positive value of the slicing scale' in fp
         and '0 < ϱ' in ' '.join(hypotheses_of(decl_statement(sky, 'sl_triple_unique'))),
         'the proposition: "…is the unique positive value of the slicing scale for which this '
         'holds"; Lean hypothesis `hϱ : 0 < ϱ`')

    need('Ⓓ④ ⛔⛭ **BUT THE ABSTRACT WAS NOT FIXED WITH IT, AND IT CARRIES THE WORD THE '
         'PROPOSITION DROPPED.** A named search over the whole paper finds the unqualified form '
         'still standing in the abstract -- the twin a repair leaves behind, which is exactly what '
         'such a search is for',
         'forced as the unique value removing the residual harmonic' not in fp,
         'searched the flattened paper for both forms:\n'
         f'   "the unique positive value of the slicing scale": '
         f'{fp.count("the unique positive value of the slicing scale")}  ← the proposition\n'
         f'   "forced as the unique value removing the residual harmonic": '
         f'{fp.count("forced as the unique value removing the residual harmonic")}  ← the abstract')
    NOTES.append('Ⓓ④ the abstract still says "the unique value" where prop:triple now says '
                 '"the unique positive value"')

    tw = decl_statement(hinge, 'sl_twoalpha')
    need('Ⓓ⑤ `sl_twoalpha` is in the cited file under `0 < α` and `α ≤ R`, and its conclusion '
         'is FIVE `↔ R = 2α` equivalences -- with (vi) carried by `sl_hinge_null`, which is how '
         'the paragraph itself divides them, so "all six" has six to point at across two '
         'declarations rather than six inside one',
         tw is not None and flat(conclusion_of(tw)).count('R = 2 * α') == 5
         and 'α ≤ R' in ' '.join(hypotheses_of(tw))
         and decl_statement(hinge, 'sl_hinge_null') is not None
         and 'and (vi) is \\texttt{sl\\_hinge\\_null}' in fp,
         f'{flat(conclusion_of(tw)).count("R = 2 * α")} equivalences in `sl_twoalpha`; '
         f'hypotheses {hypotheses_of(tw)}; `sl_hinge_null` present and cited for (vi)')

    th = decl_statement(hinge, 'sl_tangent_height')
    con = flat(conclusion_of(th))
    need('Ⓓ⑥ ⚠ (v)\'s new wording has THREE claims in one clause and the arm checks each: the '
         'tangent length is √(R²−α²) at every R; the hinge\'s height in the embedding is the same '
         '√(R²−α²) at every R; and the VALUE √3α holds **iff R = 2α**. ⌗ So "at every R" attaches '
         'to the EQUALITY and not to the value -- reading it the other way would have reported a '
         'false defect',
         'Real.sqrt (sl_nsq (sl_H₀ R - T)) = Real.sqrt (R ^ 2 - α ^ 2)' in con
         and 'X₀ = Real.sqrt (R ^ 2 - α ^ 2)' in con
         and 'Real.sqrt (R ^ 2 - α ^ 2) = Real.sqrt 3 * α ↔ R = 2 * α' in con
         and 'which equals the hinge\'s height in the embedding at every $R$, is '
             '$\\sqrt3\\,\\alpha$' in fp,
         'the three conjuncts are present and the value is an `↔ R = 2α`, so the clause parses as '
         'the declaration states it')

    need('Ⓓ⑦ `sl_flip` is cited after `prop:flip`\'s proof and concludes what the citation says',
         'so the signature is $(-,+)$ (\\texttt{sl\\_flip}, in \\texttt{SlicingHinge.lean})' in fp,
         'located verbatim')

    # Ⓓ⑦ -- P15's new clause, read against its receipt's RUN-TIME output
    clause = ('and beyond every one of a million step-free surrogates of the curve\'s own scatter '
              'and autocorrelation at all three widths')
    need('Ⓓ⑧ P15\'s new clause is in the paper as the order quotes it', clause in flat(p15),
         '…' + flat(p15)[max(0, flat(p15).find(clause) - 90): flat(p15).find(clause) + len(clause)] + '…')

    rec = None
    for fn in os.listdir(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')):
        if 'million_step_free_surrogates' in fn:
            rec = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', fn)
    need('Ⓓ⑨ and its host receipt is on disk, located by the clause\'s own words rather than by a '
         'remembered name', rec is not None, f'{os.path.basename(rec) if rec else "NOT FOUND"}')
    if rec:
        say('')
        say('      ⛭ running it, because these values exist only AT RUN TIME (negative probe 22)')
        p = subprocess.run([sys.executable, rec], capture_output=True, text=True, timeout=3600)
        out = flat(p.stdout)
        widths = re.findall(r'h(0\.\d+)', out)
        need('Ⓓ⑩ ⛭ the receipt runs green, and the surrogate claim is carried at ALL THREE widths '
             '-- so "all three widths" is the right set here, where the EARLIER clause\'s "two '
             'wider" was right for a different quantity. ⌗ Every number is read from a witness and '
             'never from a label',
             p.returncode == 0 and '[FAIL]' not in p.stdout and len(set(widths)) >= 3
             and 'AT ALL THREE HALF-WIDTHS' in p.stdout,
             f'⚠ and a fifth defect of this probe, of the same family as the four above: the arm '
             f'first searched for a SUMMARY STRING it had guessed rather than read, and this '
             f'receipt prints a different one. It now reads the receipt\'s own per-gate verdicts.\n'
             f'exit {p.returncode}; `[FAIL]` lines: {p.stdout.count("[FAIL]")}; '
             f'widths named: {sorted(set(widths))}\n'
             + '\n'.join('   ' + l[:168] for l in p.stdout.split('\n')
                         if 'surrogate' in l.lower() and '[' in l)[:1400])


# ═════════════════════════════════════════════ MAIN ═══════════════════════════════════════════
def main():
    p3, p15 = open(P3, encoding='utf-8').read(), open(P15, encoding='utf-8').read()
    sky, hinge = open(SKY, encoding='utf-8').read(), open(HINGE, encoding='utf-8').read()
    say('')
    say('  ' + '=' * 96)
    say('  r7726 (60) -- WHICH SURFACE P3 COMMITS TO BEYOND A HORIZON, answering order r7723')
    say('  ' + '=' * 96)
    for nm, s in (('P3', p3), ('P15', p15), ('SlicingSky', sky), ('SlicingHinge', hinge)):
        say(f'      {nm:<14}{len(s):>8} chars  {len(s.splitlines()):>6} lines')
    say(f'      axiom tokens: Sky {len(re.findall(r"^axiom ", sky, re.M))}, '
        f'Hinge {len(re.findall(r"^axiom ", hinge, re.M))}; `sorry`: '
        f'{sky.count("sorry")}, {hinge.count("sorry")}')

    selftests(p3, sky, hinge)
    arm_A(p3)
    arm_B(sky, hinge, p3)
    arm_C(p3)
    arm_D(p3, p15, sky, hinge)

    head('THE VERDICT')
    if FAILED:
        say(f'  {len(FAILED)} arm(s) report a FINDING -- each a reading, not a crash:')
        for f in FAILED:
            say(f'    - {f.split(".")[0][:150]}')
    else:
        say('  no arm reports a finding.')
    say('')
    say('  WHAT IS CARRIED:')
    for n in NOTES:
        say(f'    ⌗ {n}')
    say('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
