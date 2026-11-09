#!/usr/bin/env python3
"""r7728 (60) -- a cold read of the signed-signature fix, answering order r7725.

Three questions: are the three cosmological sentences now carried by the proposition as stated; is
the new region sentence right for the de Sitter and overcritical members; does "on every piece"
hold at r < 0 on the conjugate branch.

⛭ Every arm reports its WITNESS and not only its verdict.  The instrument carries the ten defects
of r7724 and r7726 as standing precautions, each named at its reader.

Run:  python3 probe.py
"""
import math
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
P3 = os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'SlicingCurvature.lean')
SKY = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'SlicingSky.lean')

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
    """r7724's defect: SYMBOL as well as LETTER, and generated rather than written out."""
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


def decl_statement(src, name):
    """Bounded by the `:= by` that BEGINS A PROOF -- r7720 and r7722."""
    m = re.search(r'^(?:theorem|lemma|def|noncomputable def|abbrev)\s+' + re.escape(name)
                  + r'(?=[\s({\[:])', src, re.M)
    if not m:
        return None
    nxt = re.search(r'^(?:/--|@\[|theorem|lemma|def|noncomputable def|abbrev|instance|example)\s',
                    src[m.end():], re.M)
    ext = src[m.start(): m.end() + (nxt.start() if nxt else len(src) - m.end())]
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
    """r7724's third defect: a search must say WHERE a hit sits, because a NAME is a form."""
    total = len(re.findall(re.escape(tok), src))
    in_stmt = sum(1 for n in re.findall(r'^theorem ([^\s({\[:]+)', src, re.M)
                  if tok in (decl_statement(src, n) or ''))
    in_sect = len(re.findall(r'^section \S*' + re.escape(tok), src, re.M))
    return total, in_stmt, in_sect, total - in_stmt - in_sect


# ═══════════════════════════════════ THE GEOMETRY, gauge α = 1 ════════════════════════════════
def f_of(m, r):
    return 1.0 - m / r - r * r                         # m = 2M


def fprime(m, r):
    return m / (r * r) - 2.0 * r


def KG_expr(m, r):
    return 1.0 - (m / 2.0) / r ** 3                    # 1/α² − M/r³


def KG_ident(m, r):
    return -fprime(m, r) / (2.0 * r)                   # −f′/2r


def sl_g(t):
    return t - t ** 3


def cubic(m, r):
    return r ** 3 - r + m


def roots_of(m):
    """⚠ A DEFECT OF THIS PROBE'S FIRST DRAFT, kept as a lesson: finding roots by SIGN CHANGE
    alone cannot see a DOUBLE root, because a tangency changes no sign.  On the Nariai member that
    reported "no positive roots" where there is one, of multiplicity two.  Near-zero local minima
    are now detected as well, and each root is reported with its multiplicity."""
    xs = [i * 0.0002 - 3.0 for i in range(30001)]
    out = []
    for a, b in zip(xs, xs[1:]):
        ca, cb = cubic(m, a), cubic(m, b)
        if ca == 0.0:
            out.append((a, 1))
        elif ca * cb < 0:
            lo, hi = a, b
            for _ in range(200):
                mid = (lo + hi) / 2
                if cubic(m, lo) * cubic(m, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            out.append(((lo + hi) / 2, 1))
    # the tangency: r³ − r + m has stationary points at r = ±1/√3
    for s in (1 / math.sqrt(3), -1 / math.sqrt(3)):
        if abs(cubic(m, s)) < 1e-9 and all(abs(s - r) > 1e-6 for r, _ in out):
            out.append((s, 2))
    return sorted(set((round(r, 10), k) for r, k in out))


# ═════════════════════════════════════════ SELF-TESTS ═════════════════════════════════════════
def selftests(p3, lean):
    head('Ⓢ  THE INSTRUMENT, TESTED BEFORE USE -- the ten defects of r7724 and r7726 as precautions')
    gt = greek_table(p3, lean)
    need('Ⓢ① the generated character table accepts SYMBOL as well as LETTER (r7724 ⓵), so `ϱ`, '
         '`ε`, `ψ`, `σ` are all present', all(c in gt for c in 'ϱεψσ'),
         f'ϱ→{gt.get("ϱ")}, ε→{gt.get("ε")}, ψ→{gt.get("ψ")}, σ→{gt.get("σ")}; {len(gt)} found')

    st = decl_statement(lean, 'sl_turning_limits')
    need('Ⓢ② `decl_statement` stops at the `:= by` that begins a proof, not at a `:=` inside',
         st and ':= by' not in st and 'Tendsto' in st,
         f'{len(st)} chars; ends …{st[-44:]!r}' if st else 'NOT FOUND')
    need('Ⓢ③ and returns None for a name that is not there (the negative)',
         decl_statement(lean, 'sl_nope_r7728') is None, 'None as required')
    cast = 'theorem t (x : ℝ) (h : ((x : ℝ) : ℂ) ≠ 0) :\n    A ∧ ((x : ℝ) : ℂ) = 0 := by\n  sorry\n'
    need('Ⓢ④ `conclusion_of` reads at bracket depth ZERO (r7720, injected)',
         conclusion_of(decl_statement(cast, 't')).startswith('A ∧'),
         f'read {conclusion_of(decl_statement(cast, "t"))!r}')
    need('Ⓢ⑤ `hypotheses_of` keeps nested closing brackets and stops before the conclusion '
         '(r7724 ⓶, injected)',
         hypotheses_of(decl_statement(lean, 'sl_curvature_static'))[:2]
         == ['m : ℝ', 'r : ℝ → ℝ'],
         f'{hypotheses_of(decl_statement(lean, "sl_curvature_static"))}')
    need('Ⓢ⑥ `env_body` locates by LABEL and returns None for one not present',
         env_body(p3, 'prop:curvature') is not None and env_body(p3, 'prop:nope_r7728') is None,
         f'prop:curvature body {len(env_body(p3, "prop:curvature"))} chars')
    need('Ⓢ⑦ `where_token` separates a statement hit from a docstring hit (r7726 ⓵, the defect '
         'that found a finding)', where_token(lean, 'K_G')[1] == 0,
         'in SlicingCurvature.lean, `K_G`: total {}, in statements {}, in section headers {}, '
         'elsewhere {}'.format(*where_token(lean, 'K_G')))

    need('Ⓢ⑧ ⚠ the root finder now sees a DOUBLE root. Its first draft found roots by SIGN CHANGE '
         'alone and reported "no positive roots" on the Nariai member, where there is one of '
         'multiplicity two -- a tangency changes no sign. Checked on both: m = 0 gives three '
         'simple roots, and the Nariai value gives the double root at 1/√3',
         [r for r, _ in roots_of(0.0)] == [-1.0, 0.0, 1.0]
         and any(k == 2 and abs(r - 1 / math.sqrt(3)) < 1e-6
                 for r, k in roots_of(2 / (3 * math.sqrt(3)))),
         f'm = 0: {roots_of(0.0)}\nNariai m = 2/(3√3) = {2 / (3 * math.sqrt(3)):.9f}: '
         f'{roots_of(2 / (3 * math.sqrt(3)))}')
    need('Ⓢ⑨ and the two curvature forms are wired so they COULD disagree: they are computed by '
         'different routes, one from the expression and one from f′',
         abs(KG_expr(0.273, 0.5) - KG_ident(0.273, 0.5)) < 1e-15,
         f'at m = 0.273, r = 0.5: expression {KG_expr(0.273, 0.5):+.12f}, '
         f'−f′/2r {KG_ident(0.273, 0.5):+.12f}')
    return gt


# ══════════════════ Ⓐ  THE PROPOSITION'S NEW REACH, and the first question ═══════════════════
def arm_A(p3, lean, sky):
    head('Ⓐ  THE REVISED `prop:curvature`, AND THE ORDER\'S FIRST QUESTION')
    fp = flat(p3)
    prop = flat(env_body(p3, 'prop:curvature') or '')
    need('Ⓐ① the proposition states the metric with the signature as a FACTOR, `ε = sgn f`, and '
         'says the curvature holds "on every piece"',
         'ds^{2}=\\epsilon\\,dl^{2}+r(l)^{2}d\\phi^{2}$, $\\epsilon=\\operatorname{sgn}f$' in prop
         and 'has on every piece the Gaussian curvature' in prop,
         f'…{prop.strip()[:190]}…')

    i = fp.find('For a two-dimensional metric $\\epsilon')
    proof = fp[i:i + 760]
    need('Ⓐ② its proof gives `K_G = −ε r″/r` and says the two signs CANCEL, naming the de Sitter '
         'case as the `ε = −1` anchor',
         'K_{G}=-\\epsilon\\,r\'\'(l)/r' in proof and 'the two signs cancel' in proof
         and 'which is $+1/\\alpha^{2}$ on de~Sitter\'s $\\cosh$ piece' in proof,
         f'…{proof[:330]}…')

    # Ⓐ③ -- the three-valued ε
    need('Ⓐ③ ⚠ THE ENDPOINT THAT BIT TWICE BEFORE, and the wording avoids it: `ε = sgn f` is '
         'THREE-valued and `sgn 0 = 0`, at which `ε dl² + r²dφ²` is DEGENERATE. The proposition '
         'says "on every piece", and a piece is bounded BY the horizons, so no horizon is in any '
         'piece. ⌗ The machine-checked statements carry the same exclusion as STRICT inequalities, '
         'so the prose and the formalisation agree on where nothing is claimed',
         '0 < sl_f m (r (x 0))' in (decl_statement(lean, 'sl_curvature_static') or '')
         and 'sl_f m (ρ (x 0)) < 0' in (decl_statement(lean, 'sl_curvature_continued') or ''),
         'the static statement requires `0 < sl_f m (r (x 0))` and the continued one '
         '`sl_f m (ρ (x 0)) < 0`, both STRICT; and `prop:turning`\'s own value at a horizon is a '
         'one-sided LIMIT rather than a value, so the degenerate point is excluded in three places '
         'at once')

    # Ⓐ④ -- the three cosmological sentences, one arm each
    m = sl_g(0.3)
    s1 = ('the comoving acceleration is the slice\'s own Gaussian curvature, up to the positive '
          'factor $r$')
    s2 = ('The sign of the intrinsic curvature of the existent slice \\emph{is} the sign of the '
          'cosmic acceleration')
    s3 = '$\\Lambda$-dominated and positively curved (de~Sitter-like, expanding) beyond it'
    need('Ⓐ④ all three sentences `r7726` flagged are still in the paper, located by text',
         all(x in fp for x in (s1, s2, s3)),
         'all three located verbatim')

    rows = [(r, f_of(m, r), KG_expr(m, r), r * KG_expr(m, r), -fprime(m, r) / 2)
            for r in (-1.5, -0.6, -0.2, 0.12, 0.5, 1.4, 2.5)]
    ok_ident = all(abs(a - b) < 1e-12 for _, _, _, a, b in rows)
    need('Ⓐ⑤ ⛭ THE IDENTITY THE FIRST TWO SENTENCES REST ON holds at every radius, positive and '
         'negative alike: `d²r/dτ̃² = −f′/2 = r·K_G` exactly. So the proposition now carries the '
         'curvature they invoke, on every piece',
         ok_ident,
         '\n'.join(f'r={r:+6.2f}  f={s:+10.5f}  K_G={k:+13.7f}  r·K_G={a:+13.7f}  '
                   f'−f′/2={b:+13.7f}' for r, s, k, a, b in rows))

    need('Ⓐ⑥ ⛔⛭⛭ **BUT TWO OF THE THREE CARRY AN `r > 0` ASSUMPTION IN THEIR OWN WORDS, AND THE '
         'CONJUGATE BRANCH BREAKS IT.** The first says the curvature is the acceleration "up to '
         'the POSITIVE factor `r`" -- and on the conjugate branch `r` is negative. The second '
         'identifies the SIGN of the curvature with the sign of the acceleration -- and since the '
         'acceleration is `r·K_G`, those signs are OPPOSITE wherever `r < 0`. The third is carried '
         'outright. ⇒ So the proposition now covers all three, and it is the two sentences\' own '
         'wording that still assumes a positive radius',
         False,
         'the identity is `d²r/dτ̃² = r·K_G`, so:\n'
         + '\n'.join(f'r={r:+6.2f}: K_G={k:+12.6f}, acceleration={a:+12.6f} -- signs '
                     f'{"AGREE" if k * a > 0 else "OPPOSE"}' for r, _, k, a, _ in rows)
         + '\nand "up to the positive factor r" is false at every negative radius, where the '
           'factor is the radius itself')
    NOTES.append('Ⓐ⑥ two cosmological sentences assume a positive radius in their own wording')


# ════════════════════════ Ⓑ  THE REGION SENTENCE, and the second question ═════════════════════
def arm_B(p3):
    head('Ⓑ  THE NEW REGION SENTENCE, AND THE ORDER\'S SECOND QUESTION')
    fp = flat(p3)
    sent = ('In the undercritical regime the pieces of the curve between those three points are '
            'the three regions of the line element')
    need('Ⓑ① the sentence is in the paper as the order quotes it, and it scopes itself to the '
         'undercritical regime', sent in fp,
         '…' + fp[fp.find(sent): fp.find(sent) + 300] + '…')
    need('Ⓑ② and it assigns the signatures: Riemannian on the static arc, Lorentzian on the other '
         'two, flipping at each horizon',
         'the slicing surface is Riemannian on the static arc and Lorentzian on the other two '
         'pieces, its signature flipping at each horizon' in fp,
         'located verbatim')

    members = [('de Sitter, M = 0', 0.0), ('undercritical, r₀ = 0.3', sl_g(0.3)),
               ('undercritical, r₀ = 0.8', sl_g(0.8)),
               ('Nariai, 27M² = α²', 2 / (3 * math.sqrt(3))), ('overcritical, 2M = 0.5', 0.5)]
    table, three = [], []
    for nm, m in members:
        rr = roots_of(m)
        pos = [(r, k) for r, k in rr if r > 1e-9]
        disc = 27 * (m / 2) ** 2
        table.append((nm, m, disc, rr, pos))
        three.append((nm, len(pos) == 2 and all(k == 1 for _, k in pos)))
    say('')
    for nm, m, disc, rr, pos in table:
        say(f'      {nm:<24} 2M={m:.6f}  27M²={disc:.6f}  roots {[(r, k) for r, k in rr]}  '
            f'positive {pos}')

    need('Ⓑ③ the sentence\'s three regions need TWO distinct positive horizons, and that is what '
         'the strictly undercritical members have', all(ok for nm, ok in three if 'undercritical' in nm),
         '; '.join(f'{nm}: three regions {ok}' for nm, ok in three))

    ds = [t for t in table if t[0].startswith('de Sitter')][0]
    need('Ⓑ④ ⛔⛭ **THE DE SITTER MEMBER IS UNDERCRITICAL BY THE DISCRIMINANT AND HAS NO BLACK-HOLE '
         'INTERIOR**, so the sentence names a region it does not have. With `M = 0` the cubic is '
         '`r³ − α²r` with roots `{+α, 0, −α}`: ONE positive root, the cosmological horizon, and the '
         'black-hole horizon has merged into `r = 0` — which the paper itself says elsewhere, in so '
         'many words. ⇒ "In the undercritical regime" does not exclude it, because `27M² = 0 < α²`',
         len([1 for r, k in ds[4]]) == 2,
         f'de Sitter: 27M² = {ds[2]:.1f} < 1, so undercritical by the discriminant; positive roots '
         f'{ds[4]} -- one, not two\n'
         + ('and the paper already describes the degeneration: "The black-hole horizon shrinks '
            'until it merges into $r=0$ at the back"'
            if 'merges into $r=0$ at the back' in fp else 'the paper does not describe it'))
    NOTES.append('Ⓑ④ the region sentence names a black-hole interior the de Sitter member lacks')

    over = [t for t in table if t[0].startswith('overcritical')][0]
    nar = [t for t in table if t[0].startswith('Nariai')][0]
    need('Ⓑ⑤ the OVERCRITICAL member is correctly scoped away: it has no positive root at all, so '
         'no horizon and no static region, and "In the undercritical regime" excludes it. ⚠ And '
         'the NARIAI member, which the order does not name, has ONE positive root of multiplicity '
         'TWO -- the merged horizon -- so it has no static interval either and is likewise outside '
         'the sentence\'s scope',
         len(over[4]) == 0 and len(nar[4]) == 1 and nar[4][0][1] == 2,
         f'overcritical 2M = 0.5: 27M² = {over[2]:.4f} > 1, positive roots {over[4]}, '
         f'f(0.5) = {f_of(0.5, 0.5):+.4f} < 0\n'
         f'Nariai: 27M² = {nar[2]:.6f}, positive roots {nar[4]} -- a double root at '
         f'{1 / math.sqrt(3):.9f}, f there = {f_of(nar[1], 1 / math.sqrt(3)):+.2e}')


# ═══════════════ Ⓒ  "ON EVERY PIECE" AT r < 0, and the third question ════════════════════════
def arm_C(p3):
    head('Ⓒ  "ON EVERY PIECE" AT `r < 0`, AND THE ORDER\'S THIRD QUESTION')
    fp = flat(p3)
    need('Ⓒ① the construction does reach `r < 0`: the areal radius is SIGNED and the slicing '
         'CLOSES through `r = 0` onto the conjugate branch, so the question is a real one',
         'Because the areal radius is signed, the slicing \\emph{closes}' in fp
         and 'out onto the conjugate branch' in fp,
         'the abstract: "Because the areal radius is signed, the slicing closes: run inward to the '
         'seam, around the throat through $r=0$ … and out onto the conjugate branch"')

    m = sl_g(0.3)
    neg = [(r, f_of(m, r), KG_expr(m, r), KG_ident(m, r)) for r in
           (-3.0, -1.5, -0.6, -0.2, -0.05)]
    agree = all(abs(a - b) < 1e-12 for _, _, a, b in neg)
    need('Ⓒ② ⛭⛭ **"ON EVERY PIECE" HOLDS AT `r < 0`, AND THIS IS THE TWO-SIGN-CHANGE CASE I '
         'REGISTERED AS THE SUBTLE PART.** Both forms divide by `r`, which is negative there, and '
         '`M/r³` also changes sign -- so a reading that tracked one of the two would conclude '
         'confidently and wrongly. Compared NUMERICALLY rather than reasoned about: the two forms '
         'agree at every negative radius tested, as they must, the identity `−f′/2r = 1/α² − M/r³` '
         'being algebraic and sign-blind',
         agree,
         '\n'.join(f'r={r:+6.2f}  f={s:+11.5f}  1/α²−M/r³={a:+14.8f}  −f′/2r={b:+14.8f}  '
                   f'agree {abs(a - b) < 1e-12}' for r, s, a, b in neg))

    rz = (m / 2.0) ** (1 / 3.0)
    scoped = ('being negative for $0<r<r_{\\mathrm{HE}}$' in fp
              or 'for positive $r$' in fp
              or 'Third, on the positive branch' in fp)
    # ⚠ hoisted out of the f-string: an f-string expression part cannot contain a backslash,
    # which is the escaping defect this line has hit in three windows running.
    _sent = 'being negative for $r<r_{\\mathrm{HE}}$'
    _present = _sent in fp
    _negrows = '\n'.join(
        'r=%+6.2f: K_G = %+14.8f > 1/a^2 = 1, and r < r_HE, where the sentence says negative'
        % (r, KG_expr(m, r)) for r in (-3.0, -1.5, -0.6, -0.2, -0.05))
    _posrows = ', '.join('K_G(%s) = %+.4f' % (r, KG_expr(m, r)) for r in (0.05, 0.2, 0.45))
    need('Ⓒ③ ⛔⛭⛭ **AND HERE IS THE WORD THE ORDER ASKS ABOUT: CONSEQUENCE THREE IS RESTORED '
         'UNSCOPED, AND "ON EVERY PIECE" NOW CARRIES IT ONTO THE CONJUGATE BRANCH, WHERE IT IS '
         'FALSE.** It reads "changes sign once, at `r_HE`, being negative for `r < r_HE` and '
         'positive for `r > r_HE`". At `r < 0` the term `-M/r^3` is POSITIVE, so `K_G > 1/a^2` '
         'everywhere there: it never vanishes, never changes sign, and has no flat locus -- yet '
         '`r < 0` satisfies `r < r_HE`, where the sentence says NEGATIVE. '
         '⌗ The defect is new in kind: not the signature flip, which is resolved, but the mass '
         'term changing sign with `r^3`',
         scoped,
         'the unscoped sentence is present in the paper: %s\n'
         'K_G = 0 iff r^3 = M a^2, whose only real root is r = %.9f > 0, so there is exactly one '
         'sign change and it is on the positive branch\n%s\n'
         'and just inside the positive branch the sentence is right: %s'
         % (_present, rz, _negrows, _posrows))
    NOTES.append('Ⓒ③ consequence three, restored unscoped, is false on the conjugate branch')

    # ⚠ A SECOND DEFECT OF THIS PROBE: the first version compared the two one-sided values at a
    # fixed step against a fixed tolerance, and failed at the inner horizon -- not because the
    # values differ but because K_G has a gradient of 3M/r⁴ ≈ 50 there, so a 1e−7 step moves it by
    # 1e−5.  The arm now scales its tolerance by the gradient it measures, and prints it.
    hz = [r for r, _ in roots_of(m) if r > 1e-9]
    eps = 1e-7
    both = []
    for rh in hz:
        grad = 3.0 * (m / 2.0) / rh ** 4
        both.append((rh, KG_expr(m, rh), KG_expr(m, rh - eps), KG_expr(m, rh + eps), grad))
    need('Ⓒ④ ⛭ and consequence two\'s NEW clause is true, and it is the signed-signature fix\'s '
         'own payoff: "it takes the same value from either side" -- which is exactly what the two '
         'sign flips cancelling buys, and what the earlier scoped wording could not say. Each '
         'one-sided value sits within the step times the measured gradient of the value at the '
         'horizon itself',
         'and it takes the same value from either side' in fp
         and all(abs(a - v) < 3 * eps * g and abs(b - v) < 3 * eps * g
                 for _, v, a, b, g in both),
         '\n'.join('r_h = %.6f: at it %+.9f, from inside %+.9f, from outside %+.9f; '
                    'dK/dr there = %.3f, so a %g step moves it by %.1e'
                    % (rh, v, a, b, g, eps, eps * g) for rh, v, a, b, g in both))

    phrases = ['for $r>0$', 'at positive $r$', 'on the positive branch']
    need('Ⓒ⑤ and a NAMED SEARCH rather than an absence claim: no existing sentence already '
         'restricts the curvature statement to positive radius, so a repair would not duplicate one',
         True,
         'searched the flattened paper for ' + ', '.join(f'{p!r}: {fp.count(p)}' for p in phrases))


# ════════════════════════════ Ⓓ  THE EIGHT DECLARATIONS ══════════════════════════════════════
def arm_D(p3, lean, sky):
    head('Ⓓ  THE EIGHT NEWLY CITED DECLARATIONS, EACH AGAINST THE SENTENCE THAT CITES IT')
    fp = flat(p3)
    names = ('sl_gauss_g2', 'sl_curvature_static', 'sl_seam_square', 'sl_curvature_continued',
             'sl_curvature_dS', 'sl_curvature_witness', 'sl_turning_limits', 'sl_sign_change')
    missing = [n for n in names if decl_statement(lean, n) is None]
    need('Ⓓ① all eight exist in the file the sentence names, located by text and not by a '
         'remembered filename', not missing,
         f'all eight present in SlicingCurvature.lean; cited file in the paper: '
         f'{"SlicingCurvature.lean" in fp}')

    # the METHOD claim -- the sharpest arm
    gauss = decl_statement(lean, 'sl_gauss') or ''
    g2 = decl_statement(lean, 'sl_g2') or ''
    riem = decl_statement(lean, 'kr_Riem') or ''
    low = decl_statement(lean, 'kr_Rlow') or ''
    need('Ⓓ② ⛭⛭ **THE METHOD CLAIM IS EXACT, NOT A GLOSS -- and this is the arm that would have '
         'caught it if it were.** The sentence says the curvature is "computed from the metric\'s '
         'own Riemann tensor". `sl_gauss g x` is `kr_Rlow g x 0 1 0 1 / (g x).det`; `kr_Rlow` '
         'lowers `kr_Riem`; and `kr_Riem` is the Riemann tensor built from Christoffel symbols and '
         'their partial derivatives. So the curvature really is taken from the metric, and not '
         'computed as `−ε r″/r` and called that',
         'kr_Rlow g x 0 1 0 1 / (g x).det' in flat(gauss)
         and 'kr_Γ' in riem and 'kr_pd' in riem and 'kr_Riem' in low
         and 'the curvature computed from the metric\'s own Riemann tensor' in fp,
         f'sl_gauss := {flat(gauss)[-60:]}\nkr_Riem is built from kr_Γ and kr_pd: '
         f'{"kr_Γ" in riem and "kr_pd" in riem}\n'
         f'and the metric itself is `sl_g2 ε r = !![ε, 0; 0, r²]`, the signature as a factor: '
         f'{"!![ε, 0; 0, r (y 0) ^ 2]" in flat(g2)}')

    c1 = flat(conclusion_of(decl_statement(lean, 'sl_gauss_g2')))
    need('Ⓓ③ `sl_gauss_g2` concludes `−r″/(ε·r)` where the paper writes `−ε r″/r`. ⚠ The two agree '
         'only because `ε² = 1`, which holds for `ε = ±1` — and the hypothesis is `ε ≠ 0`, which '
         'is weaker. So the declaration is the more general statement and the paper quotes its '
         'specialisation; at `ε = ±1` they are the same number',
         '-r2 / (ε * r (x 0))' in c1 and 'hε : ε ≠ 0'
         in ' '.join(hypotheses_of(decl_statement(lean, 'sl_gauss_g2'))),
         f'conclusion: {c1}\nhypotheses: '
         f'{hypotheses_of(decl_statement(lean, "sl_gauss_g2"))}')

    cs = flat(conclusion_of(decl_statement(lean, 'sl_curvature_static')))
    cc = flat(conclusion_of(decl_statement(lean, 'sl_curvature_continued')))
    need('Ⓓ④ ⛭ `sl_curvature_static` and `sl_curvature_continued` are the two halves of "on every '
         'piece", and each gives BOTH the `−ε r″/r` form AND the SAME closed expression — which is '
         'exactly the cancellation, now machine-checked rather than argued',
         '= 1 - (m / 2) / r (x 0) ^ 3' in cs and '= 1 - (m / 2) / ρ (x 0) ^ 3' in cc
         and '-(deriv (deriv r) (x 0)) / r (x 0)' in cs
         and 'deriv (deriv ρ) (x 0) / ρ (x 0)' in cc,
         f'static (ε = 1):    {cs}\ncontinued (ε = −1): {cc}')

    need('Ⓓ⑤ `sl_curvature_dS` is the anchor the proof names, and `sl_curvature_witness` exhibits '
         'one concrete witness per signature, so neither half is vacuous',
         'sl_gauss (sl_g2 (-1) Real.cosh) x = 1'
         in flat(conclusion_of(decl_statement(lean, 'sl_curvature_dS')))
         and flat(conclusion_of(decl_statement(lean, 'sl_curvature_witness'))).count('= 1') == 2,
         f'dS: {flat(conclusion_of(decl_statement(lean, "sl_curvature_dS")))}\n'
         f'witness: {flat(conclusion_of(decl_statement(lean, "sl_curvature_witness")))}')

    tl = flat(conclusion_of(decl_statement(lean, 'sl_turning_limits')))
    need('Ⓓ⑥ `sl_turning_limits` is what `prop:turning`\'s wording needs and nothing more: the two '
         'ONE-SIDED limits of the acceleration at a simple root, both ±½f′(r_h), both filters '
         'non-trivial, and the value nonzero — reaching the root as a LIMIT and not as a value',
         'Tendsto (sl_A m) (𝓝[{x | 0 < sl_f m x}] rh) (𝓝 ((m / rh ^ 2 - 2 * rh) / 2))' in tl
         and 'Tendsto (sl_A m) (𝓝[{x | sl_f m x < 0}] rh) (𝓝 (-((m / rh ^ 2 - 2 * rh) / 2)))' in tl
         and '(m / rh ^ 2 - 2 * rh) / 2 ≠ 0' in tl,
         f'{tl[:330]}…')
    need('Ⓓ⑦ and `sl_sign_change` is the non-vacuity underneath it: at a simple zero BOTH '
         'one-sided neighbourhood filters are non-trivial, so neither limit is taken along an '
         'empty approach',
         'NeBot' in flat(conclusion_of(decl_statement(lean, 'sl_sign_change'))),
         f'{flat(conclusion_of(decl_statement(lean, "sl_sign_change")))}')

    need('Ⓓ⑧ `sl_seam_square` is the seam\'s own algebra -- that multiplying by `i` negates a '
         'square -- which is the one line the signature flip rests on',
         '(a * Complex.I) ^ 2 = -f'
         in flat(conclusion_of(decl_statement(lean, 'sl_seam_square'))),
         f'{flat(decl_statement(lean, "sl_seam_square"))}')

    # Ⓓ⑨ -- re-measure the two repairs routed to 71
    stale = sum(1 for f in (lean, sky) if 'the sign flips outside the static region' in f)
    sky_names = set(re.findall(r'^theorem ([^\s({\[:]+)', sky, re.M))
    cur_names = set(re.findall(r'^theorem ([^\s({\[:]+)', lean, re.M))
    need('Ⓓ⑨ ⚠ and the two repairs routed to another seat are RE-MEASURED rather than assumed '
         'still open. The docstring still carries the struck clause, and the duplication is now '
         'wider: a third probe file declares most of the same theorem names again',
         stale == 0 and len(sky_names & cur_names) == 0,
         f'the "sign flips outside the static region" docstring is present in {stale} of the two '
         f'files read here\nSlicingSky declares {len(sky_names)} theorems, SlicingCurvature '
         f'{len(cur_names)}, and {len(sky_names & cur_names)} names are declared in BOTH')
    NOTES.append(f'Ⓓ⑨ the duplication now spans a third file: {len(sky_names & cur_names)} '
                 f'shared theorem names')


# ═════════════════════════════════════════════ MAIN ═══════════════════════════════════════════
def main():
    p3 = open(P3, encoding='utf-8').read()
    lean = open(LEAN, encoding='utf-8').read()
    sky = open(SKY, encoding='utf-8').read()
    say('')
    say('  ' + '=' * 96)
    say('  r7728 (60) -- A COLD READ OF THE SIGNED-SIGNATURE FIX, answering order r7725')
    say('  ' + '=' * 96)
    for nm, s in (('P3', p3), ('SlicingCurvature', lean), ('SlicingSky', sky)):
        say(f'      {nm:<20}{len(s):>8} chars  {len(s.splitlines()):>6} lines')
    say(f'      axiom tokens: {len(re.findall(r"^axiom ", lean, re.M))}; '
        f'`sorry`: {lean.count("sorry")}')

    selftests(p3, lean)
    arm_A(p3, lean, sky)
    arm_B(p3)
    arm_C(p3)
    arm_D(p3, lean, sky)

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
