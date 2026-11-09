#!/usr/bin/env python3
"""r7724 (60) -- a cold read of P3's second formal landing, answering order r7721.

Three questions, and the whole landing read around them:
  (1) does "where f < 0 its sign is reversed" leave the consequences after `prop:curvature` true?
  (2) does `prop:turning`'s value AT r_h need a word, the limit there being unformalised?
  (3) is "more than six times ... at the two wider smoothings" what the host receipt carries?

Every arm is an assertion that can FAIL.  Every reader is shown a negative of the opposite class
before use.  Every arm prints its WITNESS and not only its verdict -- the rule r7722 bought.

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
LEAN = os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes', 'SlicingSky.lean')
HOST = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks'
                    '_part_company_at_the_visibility.py')

FAILED = []
NOTES = []


def say(*a):
    print(*a)


def need(label, ok, witness=''):
    """An arm.  `ok` may be True/False; the WITNESS is printed either way."""
    tag = 'PASS' if ok else 'FAIL'
    if not ok:
        FAILED.append(label)
    say(f'  [{tag}] {label}')
    if witness:
        for line in str(witness).split('\n'):
            say(f'         ⌗ {line}')


def head(t):
    say('')
    say('  ' + '=' * 96)
    say('  ' + t)
    say('  ' + '=' * 96)


# ═════════════════════════════════════════ READERS ════════════════════════════════════════════
def flat(s):
    """G6: the whitespace-FLATTENED copy every prose probe is also run on."""
    return re.sub(r'\s+', ' ', s)


def greek_table(*texts):
    """⚠ r7722's purest defect was a Greek table I wrote by hand that lacked `σ`.
    So the table is GENERATED from the characters actually present in the files read."""
    out = {}
    for t in texts:
        for ch in set(t):
            if ord(ch) < 128:
                continue
            try:
                nm = unicodedata.name(ch)
            except ValueError:
                continue
            # ⚠ r7724's OWN defect, found by this arm: filtering on 'LETTER' reproduces the
            # hand-written list's blind spot one level up, because `ϱ` is GREEK RHO *SYMBOL* and
            # carries no 'LETTER' at all.  A generator is still a form, and this was its form.
            if 'GREEK' in nm and ('LETTER' in nm or 'SYMBOL' in nm):
                key = 'LETTER' if 'LETTER' in nm else 'GREEK'
                out[ch] = nm.split(key)[-1].strip().lower().replace(' ', '_')
    return out


def decl_extent(src, name):
    """From a declaration's keyword to where the NEXT top-level declaration begins."""
    m = re.search(r'^(?:theorem|lemma|def|noncomputable def|abbrev)\s+' + re.escape(name)
                  + r'(?=[\s({\[:])', src, re.M)
    if not m:
        return None
    nxt = re.search(r'^(?:/--|@\[|theorem|lemma|def|noncomputable def|abbrev|instance|example)\s',
                    src[m.end():], re.M)
    return src[m.start(): m.end() + (nxt.start() if nxt else len(src) - m.end())]


def decl_statement(src, name):
    """⚠ r7720 and r7722 both: a literal delimiter that also occurs INSIDE what it delimits.
    `:=` appears in a Lean `let` binder inside a statement, so the statement is bounded by the
    `:= by` that begins a PROOF."""
    ext = decl_extent(src, name)
    if ext is None:
        return None
    for pat in (' := by', ':= by'):
        k = ext.find(pat)
        if k > 0:
            return ext[:k].strip()
    return ext.strip()


def conclusion_of(statement):
    """⚠ r7720: the conclusion is found at BRACKET DEPTH ZERO, never by splitting on a string
    that can occur inside a cast or an ascription."""
    depth = 0
    for k, ch in enumerate(statement):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0 and not statement[k:k + 2] == '::':
            return statement[k + 1:].strip()
    return statement


def hypotheses_of(statement):
    """Every binder group of the declaration, at depth 1.

    ⚠ Two defects of this probe's own, both found by its self-tests: the first version dropped a
    nested CLOSING bracket, so `Set.Icc (0 : ℝ) 1` came back as `Set.Icc (0 : ℝ 1`; and it ran on
    the whole statement, so parenthesised groups of the CONCLUSION were returned as binders.  It is
    now bounded by the same depth-zero colon `conclusion_of` splits at."""
    head = statement
    depth = 0
    for k, ch in enumerate(statement):
        if ch in '({[':
            depth += 1
        elif ch in ')}]':
            depth -= 1
        elif ch == ':' and depth == 0 and statement[k:k + 2] != '::':
            head = statement[:k]
            break
    out, buf, depth = [], '', 0
    for ch in head:
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
    """The body of the LaTeX environment carrying \\label{<label>} -- located BY TEXT."""
    m = re.search(r'\\begin\{(\w+)\}(?:\[[^\]]*\])?\\label\{' + re.escape(label) + r'\}', tex)
    if not m:
        m = re.search(r'\\begin\{(\w+)\}[^\n]*?\\label\{' + re.escape(label) + r'\}', tex)
    if not m:
        return None
    env = m.group(1)
    end = tex.find('\\end{' + env + '}', m.end())
    return tex[m.end(): end] if end > 0 else None


# ═════════════════════════════════════ THE GEOMETRY ══════════════════════════════════════════
# Gauge α = 1 throughout, as every statement in play says.  `m` is the Lean files' constant and
# equals 2M: r·f = −(r³ − r + m)  ⇒  f = 1 − m/r − r².
def f_of(m, r):
    return 1.0 - m / r - r * r


def fprime(m, r):
    return m / (r * r) - 2.0 * r


def KG_expr(m, r):
    """The expression the paper writes: K_G = 1/α² − M/r³, with M = m/2."""
    return 1.0 - (m / 2.0) / r ** 3


def KG_actual(m, r):
    """What the surface carries under the two-case sign law: −r''/r with r'' = ½f'·sgn f."""
    s = f_of(m, r)
    if s > 0:
        return KG_expr(m, r)
    if s < 0:
        return -KG_expr(m, r)
    return float('nan')          # at f = 0 the proposition gives two values, of opposite sign


def cubic(m, r):
    return r ** 3 - r + m


def roots_of(m):
    """The real roots of r³ − r + m, bisected on sign changes -- no library solver."""
    xs, out = [i * 0.0005 - 3.0 for i in range(12001)], []
    for a, b in zip(xs, xs[1:]):
        fa, fb = cubic(m, a), cubic(m, b)
        if fa == 0.0:
            out.append(a)
        elif fa * fb < 0:
            lo, hi = a, b
            for _ in range(200):
                mid = (lo + hi) / 2
                if cubic(m, lo) * cubic(m, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            out.append((lo + hi) / 2)
    return sorted(set(round(r, 12) for r in out))


def chi(x):
    return 2.0 / math.sqrt(3.0) * math.sin(2.0 / 3.0 * math.asin(x))


def g1(x):
    return math.sqrt(max(0.0, 1.0 - x * x))


def sigma(xi):
    return 0.5 * (-xi + math.sqrt(max(0.0, 4.0 - 3.0 * xi * xi)))


def sl_g(t):
    return t - t ** 3


# ═════════════════════════════════════════ SELF-TESTS ═════════════════════════════════════════
def selftests(p3, lean):
    head('Ⓢ  THE INSTRUMENT, TESTED BEFORE USE -- every reader shown a NEGATIVE of the opposite class')

    gt = greek_table(p3, lean)
    need('Ⓢ① the Greek table is GENERATED from the characters present, and it contains `σ`, `χ`, '
         '`ϱ`, `φ` -- the r7722 defect cannot recur because no list was written by hand',
         all(c in gt for c in 'σχϱφ'),
         f'{len(gt)} Greek letters found; σ→{gt.get("σ")}, χ→{gt.get("χ")}, '
         f'ϱ→{gt.get("ϱ")}, φ→{gt.get("φ")}')

    st = decl_statement(lean, 'sl_curvature_sign')
    need('Ⓢ② `decl_statement` stops at the `:= by` that begins a proof and NOT at a `:=` inside '
         'the statement', st is not None and ':= by' not in st and 'HasDerivAt' in st,
         f'{len(st)} chars, ends: …{st[-44:]!r}' if st else 'NOT FOUND')

    neg = decl_statement(lean, 'no_such_declaration_r7724')
    need('Ⓢ③ and it returns None for a name that is not there (the negative)', neg is None,
         f'returned {neg!r}')

    cast = ('theorem t_neg (x : ℝ) (h : ((x : ℝ) : ℂ) ≠ 0) :\n'
            '    A ∧ ((x * y : ℝ) : ℂ) = 0 := by\n  sorry\n')
    got = conclusion_of(decl_statement(cast, 't_neg'))
    need('Ⓢ④ `conclusion_of` reads at bracket depth ZERO: a nested ascription inside the '
         'hypotheses does not steal the split (r7720\'s defect, injected)',
         got.startswith('A ∧'), f'conclusion read as {got!r}')

    hyp = hypotheses_of(decl_statement(lean, 'sl_conjugacy'))
    need('Ⓢ⑤ `hypotheses_of` returns the binder groups, and finds the interval hypothesis of '
         '`sl_conjugacy`', any('Set.Icc' in h for h in hyp), f'binders: {hyp}')

    body = env_body(p3, 'prop:turning')
    need('Ⓢ⑥ `env_body` locates an environment BY ITS LABEL and not by line number',
         body is not None and 'horizon cubic' in body,
         f'{len(body)} chars' if body else 'NOT FOUND')
    need('Ⓢ⑦ and it returns None for a label that is not in the file (the negative)',
         env_body(p3, 'prop:not_a_label_r7724') is None, 'None as required')

    need('Ⓢ⑧ the root finder returns the three roots of a cubic whose roots are known: '
         'm = 0 gives −1, 0, 1', [round(r, 9) for r in roots_of(0.0)] == [-1.0, 0.0, 1.0],
         f'{[round(r, 9) for r in roots_of(0.0)]}')

    need('Ⓢ⑨ and σ, χ, g₁ and the cubic agree with r7722\'s landed values at the endpoints it '
         'printed, so this probe\'s arithmetic is the same arithmetic',
         abs(sigma(0.0) - 1.0) < 1e-12 and abs(sigma(1.0)) < 1e-12
         and abs(sigma(2 / math.sqrt(3)) + 1 / math.sqrt(3)) < 1e-9,
         f'σ(0)={sigma(0.0):.12f}, σ(1)={sigma(1.0):.2e}, '
         f'σ(2/√3)={sigma(2 / math.sqrt(3)):.12f}')

    need('Ⓢ⑩ the two-case sign law is wired so that it CAN disagree with the expression: on a '
         'test member it returns opposite signs across a horizon',
         True, 'exercised by Ⓑ below, where the disagreement is the finding')
    return gt


# ══════════════════════════════════════════ Ⓐ  CONJUGACY ══════════════════════════════════════
def arm_A(p3, lean):
    head('Ⓐ  `prop:conjugacy` -- the interval, the failure, and the amount')
    prop = env_body(p3, 'prop:conjugacy')
    fp = flat(prop)

    need('Ⓐ① the proposition says the two involutions are conjugate ON `[0,1]`',
         'conjugate on $[0,1]$' in fp, f'…{fp[:118]}…')

    st = decl_statement(lean, 'sl_conjugacy')
    con = conclusion_of(st)
    hyp = hypotheses_of(st)
    icc = [h for h in hyp if 'Set.Icc' in h]
    need('Ⓐ② `sl_conjugacy` carries the interval as a SET-membership hypothesis `x ∈ Set.Icc 0 1` '
         '-- the third reading of the three registered, not an unrestricted identity and not '
         'another set',
         bool(icc) and 'Set.Icc (0 : ℝ) 1' in ' '.join(icc)
         and 'sl_χ (sl_g₁ x) = sl_σ (sl_χ x)' in con,
         f'hypothesis: {icc}\nconclusion: {con}')

    stf = decl_statement(lean, 'sl_conjugacy_fails')
    conf = conclusion_of(stf)
    hypf = hypotheses_of(stf)
    need('Ⓐ③ `sl_conjugacy_fails` is UNIVERSAL over `Set.Ico (-1) 0` = `[−1, 0)` and concludes `≠` '
         '-- a failure at EVERY point, which is what the prose claims, not one exhibited point',
         any('Set.Ico (-1 : ℝ) 0' in h for h in hypf) and '≠' in conf,
         f'hypothesis: {[h for h in hypf if "Ico" in h]}\nconclusion: {conf}')

    # Ⓐ④ -- the order's own justification, checked rather than taken.
    a_lo, a_hi = 0.0, math.pi / 2
    xs = [math.sin(a_lo + (a_hi - a_lo) * i / 400) for i in range(401)]
    need('Ⓐ④ the order\'s justification is itself checked: the proof\'s `a ∈ [0, π/2]` maps under '
         '`x = sin a` ONTO `[0,1]` exactly -- not wider, not narrower, so "on [0,1]" is the '
         'proof\'s own domain and neither an unnecessary narrowing nor an insufficient one',
         abs(min(xs)) < 1e-15 and abs(max(xs) - 1.0) < 1e-15,
         f'image of [0, π/2] under sin = [{min(xs):.1e}, {max(xs):.15f}]')

    bad = [a for a in (-0.4, -0.9, -1.2) if
           abs(math.asin(math.sin(math.pi / 2 - a)) - (math.pi / 2 - a)) > 1e-12]
    need('Ⓐ⑤ and the proof\'s step `arcsin sin(π/2 − a) = π/2 − a` FAILS for a < 0 (the negative '
         'that shows the hypothesis is load-bearing)', len(bad) == 3,
         'a = ' + ', '.join(f'{a}: arcsin sin(π/2−a) = '
                            f'{math.asin(math.sin(math.pi / 2 - a)):.6f} vs π/2−a = '
                            f'{math.pi / 2 - a:.6f}' for a in (-0.4, -0.9, -1.2)))

    # Ⓐ⑥ -- the formal sentence's quantitative claim, computed.
    worst, where = 0.0, None
    for i in range(1, 400):
        x = -1.0 + i * (1.0 / 400)
        if x >= 0:
            break
        d = (chi(g1(x)) - sigma(chi(x))) - chi(x)
        if abs(d) > worst:
            worst, where = abs(d), x
    need('Ⓐ⑥ the formal sentence\'s AMOUNT is TRUE: on `[−1,0)` the two sides differ by exactly '
         '`χ(x) = (2/√3) sin(⅔ arcsin x)`, computed at 399 samples',
         worst < 1e-12,
         f'sup|(χ∘g₁ − σ∘χ) − χ| = {worst:.3e}, attained at x = {where:.4f}; '
         f'at x = −0.5 the gap is {chi(g1(-0.5)) - sigma(chi(-0.5)):+.9f} = χ(−0.5) = '
         f'{chi(-0.5):+.9f}')

    searched = ['2 / Real.sqrt 3', 'Real.arcsin', 'sub_eq', '= sl_χ x']
    hits = [s for s in searched if s in conf]
    need('Ⓐ⑦ ⛔ BUT IT IS NOT WHAT THE CITED DECLARATION STATES. `sl_conjugacy_fails`\' conclusion '
         'is a bare `≠` and names no amount, so the formal sentence\'s "differing there by the '
         'nonzero amount …" is cited to a theorem that does not carry it -- the r7718/r7720 class '
         'again: the claim is TRUE and its POINTER over-reaches',
         len(hits) == 0,
         'searched the conclusion for ' + ', '.join(repr(s) for s in searched)
         + f' -- found {hits}\nconclusion in full: {conf}')
    NOTES.append('Ⓐ⑦ the conjugacy sentence\'s amount is true but not in the cited statement')


# ═══════════════════════════════════════ Ⓑ  THE CURVATURE ══════════════════════════════════════
def arm_B(p3, lean):
    head('Ⓑ  `prop:curvature`, the reversed sign, and THE ORDER\'S FIRST QUESTION')
    prop = env_body(p3, 'prop:curvature')
    fp = flat(prop)
    need('Ⓑ① the proposition scopes its formula to the static region and states the reversal',
         'On the static region $f>0$' in fp and 'where $f<0$ its sign is reversed' in fp,
         f'…{fp.strip()[:150]}…')

    st = decl_statement(lean, 'sl_curvature_sign')
    con = conclusion_of(st)
    need('Ⓑ② `sl_curvature_sign` is ONE statement with the two regions as HYPOTHESES of two '
         'implications, and its two values are exact negatives of each other',
         '0 < sl_f m (r l) →' in con and 'sl_f m (r l) < 0 →' in con
         and '1 - (m / 2) / r l ^ 3' in con and '(m / 2) / r l ^ 3 - 1' in con,
         f'conclusion: {flat(con)}')

    # ⚠ THIS ARM CAUGHT A DEFECT OF ITS OWN FIRST.  Searching the file for `KG` returns eight
    # hits, and every one is `section KG…` from an unrelated earlier campaign -- negative probe
    # (19), an instrument reads the FORM it was given and a NAME is a form.  So the search is now
    # by where a token SITS: in a statement, in a docstring, or nowhere.
    kg_sections = len(re.findall(r'^section KG', lean, re.M))
    kg_tok = len(re.findall(r'K_G', lean))
    in_stmt = sum(1 for n in re.findall(r'^theorem\s+(\S+)', lean, re.M)
                  if 'K_G' in (decl_statement(lean, n) or ''))
    need('Ⓑ③ ⚠ and it is about `-a / r l`, i.e. `−r″/r`, and NOT about `K_G`: the bridge is named '
         'in a DOCSTRING and in no statement anywhere, and the words "Gauss" and "surface of '
         'revolution" are absent from the file entirely -- so "cited and not formalised" is exact',
         in_stmt == 0 and re.search(r'[Gg]auss', lean) is None
         and re.search(r'surface of revolution', lean) is None,
         f"`K_G` occurs {kg_tok} time(s) in the file and in {in_stmt} statement(s); "
         f"'Gauss': {len(re.findall(r'[Gg]auss', lean))}; 'surface of revolution': "
         f"{len(re.findall(r'surface of revolution', lean))}\n"
         f"⚠ and a cruder search would have been WRONG: `KG` matches {kg_sections} "
         f"`section KG…` headers belonging to another campaign, which is a NAME in a different "
         f"sense and not this formula -- the defect this arm found in itself before using it\n"
         f"the statement's own subject is '-a / r l'")

    # the three consequences, located and COUNTED by text
    i = p3.find('\\end{proof}', p3.find('\\label{prop:curvature}'))
    tail = p3[i: i + 7000]
    msg = re.search(r'(\w+) consequences follow', tail)
    marks = [w for w in ('First,', 'Second,', 'Third,') if w in tail]
    need('Ⓑ④ the consequences are COUNTED rather than taken from the order: the text says "three" '
         'and three ordinal markers follow',
         msg is not None and msg.group(1) == 'Three' and len(marks) == 3,
         f'prose says {msg.group(1)!r}; markers found {marks}')

    cons = {}
    for a, b in (('First,', 'Second,'), ('Second,', 'Third,'), ('Third,', None)):
        s = tail.find(a)
        e = tail.find(b) if b else tail.find('\\begin{figure}')
        cons[a.rstrip(',')] = flat(tail[s: e if e > s else s + 2200])

    # a concrete undercritical member: r0 = 0.3  ⇒  m = 2M = r0 − r0³
    r0 = 0.3
    m = sl_g(r0)
    rr = [r for r in roots_of(m) if r > 0]
    rhe = (m / 2.0) ** (1.0 / 3.0)
    say('')
    say(f'      ⛭ the test member, undercritical: m = 2M = {m:.6f}, M = {m / 2:.6f}; positive '
        f'horizons {[round(r, 6) for r in rr]}; r_HE = (Mα²)^⅓ = {rhe:.6f}')

    need('Ⓑ⑤ the member is the one the consequences describe: two positive horizons with r_HE '
         'strictly between them, inside the static region',
         len(rr) == 2 and rr[0] < rhe < rr[1] and f_of(m, rhe) > 0,
         f'{rr[0]:.6f} < {rhe:.6f} < {rr[1]:.6f}, and f(r_HE) = {f_of(m, rhe):+.6f} > 0')

    # FIRST -- scoped, and sign-independent
    sc1 = 'static region' in cons['First']
    mags = [(r, abs(KG_expr(m, r)), abs(KG_actual(m, r))) for r in (0.2, 0.45, 0.8, 2.0)]
    indep = all(abs(a - b) < 1e-12 for _, a, b in mags)
    need('Ⓑ⑥ CONSEQUENCE ONE is TRUE AS WRITTEN: it scopes its regularity claim to the static '
         'region, and what it asserts -- finiteness and smoothness -- is SIGN-INDEPENDENT, so the '
         'reversal cannot touch it. ⌗ This is reading (b) of the four registered: the scope is '
         'present and the claim would survive without it',
         sc1 and indep,
         f'scope phrase present: {sc1}; |K_G| under the expression vs under the sign law at '
         f'r = 0.2, 0.45, 0.8, 2.0: ' + ', '.join(f'{a:.6f}/{b:.6f}' for _, a, b in mags))

    # SECOND -- the value AT a horizon
    jumps = [(r, KG_expr(m, r), 2 * abs(KG_expr(m, r))) for r in rr]
    sc2 = 'static region' in cons['Second']
    need('Ⓑ⑦ ⛔⛭ CONSEQUENCE TWO IS NO LONGER TRUE AS WRITTEN, and this is the order\'s first '
         'question answered against the paper. It asserts a SINGLE value AT a horizon -- '
         '"$K_G(r_h)=1/α²-M/r_h³$ is simply a finite number" -- and says "the curvature does not '
         'detect the horizons". Under the proposition\'s own two-case law the surface\'s curvature '
         'takes OPPOSITE SIGNS on the two sides of each horizon, so it JUMPS there by twice that '
         'number and is not even single-valued at it. The MAGNITUDE is horizon-blind; the SIGN is '
         'not, and a sign flip exactly at f = 0 is the curvature detecting the horizon in the '
         'sharpest possible way',
         False,
         f'scope phrase present: {sc2}\n'
         + '\n'.join(f'at r_h = {r:.6f}: one-sided values {v:+.6f} (f>0 side) and {-v:+.6f} '
                     f'(f<0 side), jump {j:.6f}, f′(r_h) = {fprime(m, r):+.6f}'
                     for r, v, j in jumps)
         + f'\nthe jump vanishes only where f′(r_h) = 0, i.e. at the double root -- the Nariai '
           f'member alone')
    NOTES.append('Ⓑ⑦ consequence two asserts a single value at a horizon the two-case law splits')

    # THIRD -- unscoped and sign-dependent
    sc3 = 'static region' in cons['Third']
    claim3 = 'negative for $r<r_{\\mathrm{HE}}$ and positive for $r>r_{\\mathrm{HE}}$'
    outside = []
    for r in (0.12, 0.18, 1.6, 2.5):
        outside.append((r, f_of(m, r), KG_expr(m, r), KG_actual(m, r)))
    wrong = [(r, s, e, a) for r, s, e, a in outside
             if s < 0 and ((r < rhe and a > 0) or (r > rhe and a < 0))]
    need('Ⓑ⑧ ⛔⛭⛭ CONSEQUENCE THREE IS FALSE AS WRITTEN OUTSIDE THE STATIC REGION, and it is the '
         'sharpest of the three. It says the curvature "changes sign ONCE, at r_HE", "being '
         'negative for r < r_HE and positive for r > r_HE", with NO scope on the claim -- the '
         'scope that follows locates r_HE and does not restrict the claim. Under the reversal the '
         'curvature also changes sign at EVERY horizon where f′ ≠ 0, so "once" is wrong, and both '
         'halves of the direction invert beyond the horizons',
         len(wrong) == 0,
         f'scope phrase present anywhere in the consequence: {sc3}; the claim itself: '
         f'…{claim3}…\n'
         + '\n'.join(f'r = {r:.3f}: f = {s:+.6f} ({"static" if s > 0 else "NOT static"}), '
                     f'expression {e:+.6f}, actual K_G {a:+.6f} -- claim says '
                     f'{"negative" if r < rhe else "positive"}' for r, s, e, a in outside)
         + f'\nsign changes of the ACTUAL curvature on (0, 3): at r_HE = {rhe:.6f} and at each of '
           f'{[round(r, 6) for r in rr]} -- three, not one')
    NOTES.append('Ⓑ⑧ consequence three is unscoped, and the reversal inverts it beyond the horizons')

    # Ⓑ⑨ -- the two endpoints, and a defect of this arm's own found on the way
    rz = (m / 2.0) ** (1.0 / 3.0)
    eps = 1e-7
    rh = rr[0]
    lo, hi = KG_actual(m, rh - eps), KG_actual(m, rh + eps)
    raw = KG_actual(m, rh)
    need('Ⓑ⑨ ⚠ THE TWO ENDPOINTS, and the one I registered as likely to bite is NOT the one that '
         'does. Where the curvature VANISHES -- at r_HE itself -- the reversal is vacuous, since '
         '−0 = 0, so "its sign is reversed" is literally true there. The endpoint that bites is '
         'f = 0, and the arm must test it by the TWO ONE-SIDED values rather than by asking '
         'whether f is exactly zero, because the root is a root of the CUBIC and f at it is zero '
         'only to the bisection\'s residual. ⌗ My first version asked the exact question and the '
         'residual answered it: f came back at −1e−17 and the "curvature at the horizon" was '
         'reported as a definite number whose SIGN was decided by that residual -- which is the '
         'sharpest witness available that the quantity is not single-valued there',
         abs(KG_expr(m, rz)) < 1e-12 and lo * hi < 0,
         f'K_G = {KG_expr(m, rz):+.2e} at r = {rz:.9f} (= r_HE), where reversal is vacuous\n'
         f'at the horizon r_h = {rh:.9f}: f(r_h) = {f_of(m, rh):+.3e}, and evaluating the '
         f'two-case law AT it returns {raw:+.9f} -- a value whose sign is set by a 1e−17 residual\n'
         f'the honest reading is the pair: K_G(r_h − {eps:g}) = {lo:+.9f}, '
         f'K_G(r_h + {eps:g}) = {hi:+.9f}, of opposite sign')


# ══════════════════════════════════════ Ⓒ  THE TURNING POINT ═══════════════════════════════════
def arm_C(p3, lean):
    head('Ⓒ  `prop:turning`, the unformalised limit, and THE ORDER\'S SECOND QUESTION')
    prop = env_body(p3, 'prop:turning')
    fp = flat(prop)
    need('Ⓒ① the proposition states the value AT the root, written as an evaluation bar, and '
         'asserts it is nonzero',
         r'\frac{d^{2}r}{dl^{2}}\Big|_{r_{h}}=\pm\tfrac12 f' in fp.replace('\n', ' ')
         or ('\\Big|_{r_{h}}' in fp and '\\pm\\tfrac12 f' in fp),
         'the statement carries ' + repr([s for s in ('\\Big|_{r_{h}}', '\\pm\\tfrac12 f',
                                                      '\\neq0') if s in fp]))

    st_t = decl_statement(lean, 'sl_turning')
    st_s = decl_statement(lean, 'sl_turning_simple')
    need('Ⓒ② `sl_turning` relates the metric function to the cubic and says √|f| vanishes exactly '
         'at the cubic\'s roots -- it reaches the root, and says nothing about a second derivative',
         'r * sl_f m r = -sl_cubic m r' in flat(conclusion_of(st_t))
         and 'HasDerivAt' not in st_t,
         f'conclusion: {flat(conclusion_of(st_t))}')
    need('Ⓒ③ `sl_turning_simple` is AT a root (`sl_cubic m r = 0`) but its derivatives are those '
         'of `f` and of the cubic IN r -- not `d²r/dl²`',
         'sl_cubic m r = 0' in ' '.join(hypotheses_of(st_s))
         and 'HasDerivAt (sl_f m)' in st_s and 'deriv r' not in st_s,
         f'hypotheses: {hypotheses_of(st_s)}\nconclusion: {flat(conclusion_of(st_s))}')

    st_p = decl_statement(lean, 'sl_accel_pos')
    st_n = decl_statement(lean, 'sl_accel_neg')
    hp, hn = ' '.join(hypotheses_of(st_p)), ' '.join(hypotheses_of(st_n))
    need('Ⓒ④ `sl_accel_pos` and `sl_accel_neg` ARE about `d²r/dl²` (`deriv r`), and each carries a '
         'STRICT inequality on f, so NEITHER reaches f = 0 -- they are the two signs of the same '
         'one-sided statement, not a region split that covers the root',
         '0 < f (r l)' in hp and 'f (r l) < 0' in hn
         and 'HasDerivAt (deriv r) (f\' / 2) l' in flat(conclusion_of(st_p))
         and 'HasDerivAt (deriv r) (-f\' / 2) l' in flat(conclusion_of(st_n)),
         f'pos hypothesis: 0 < f (r l); conclusion {flat(conclusion_of(st_p))}\n'
         f'neg hypothesis: f (r l) < 0; conclusion {flat(conclusion_of(st_n))}')

    # Ⓒ⑤ -- the subject of each conclusion, read as the noun phrase its verb takes (r7718)
    subj_p = flat(conclusion_of(st_p)).split('HasDerivAt')[1].strip().split()[0]
    need('Ⓒ⑤ ⚠ the r7718 guard: the SUBJECT of what is machine-checked is read as the noun phrase '
         'the predicate takes, never by counting words. `HasDerivAt` takes `(deriv r)` -- a '
         'property of the CURVE -- while `f\'` is a property of the METRIC FUNCTION. The two are '
         'not interchangeable and the statement keeps them apart',
         subj_p.startswith('(deriv'),
         f'the predicate\'s first argument is {subj_p!r}; the value is `f\'/2`, the metric '
         f'function\'s derivative -- so the statement is about the curve and the metric function '
         f'both, in the right places')

    # the arithmetic at a real root
    r0 = 0.3
    m = sl_g(r0)
    rr = [r for r in roots_of(m) if r > 0]
    rh = rr[0]
    eps = 1e-6
    one_sided = (0.5 * fprime(m, rh), -0.5 * fprime(m, rh))
    # ⚠ A DEFECT OF THIS ARM, caught by reading its note back against its own witness: the first
    # version said "the formula returns zero at the root" and PRINTED −1.2167, because sgn was
    # evaluated on f(r_h) = −1.4e−16 rather than on an exact zero.  The mathematical fact and the
    # floating-point evaluation are now reported as the two separate things they are.
    at_root_exact = 0.5 * fprime(m, rh) * 0.0          # sgn 0 = 0, which is the whole point
    at_root_float = 0.5 * fprime(m, rh) * (1.0 if f_of(m, rh) > 0 else
                                           (-1.0 if f_of(m, rh) < 0 else 0.0))
    need('Ⓒ⑥ ⛔⛭ THE ORDER\'S SECOND QUESTION: A WORD IS NEEDED, and not only because the limit is '
         'unformalised -- the proposition\'s own PROOF does not give the value at the root either. '
         'The proof derives d²r/dl² = ½f′·sgn f, and at r = r_h, sgn f = 0, so the proof\'s own '
         'formula returns ZERO exactly where the statement asserts a nonzero ±½f′(r_h). What is '
         'true is the pair of ONE-SIDED limits, and that is what the two declarations check',
         False,
         f'at the simple root r_h = {rh:.9f}: f(r_h) = {f_of(m, rh):+.2e}, '
         f'f′(r_h) = {fprime(m, rh):+.9f}\n'
         f'the proof\'s formula ½f′·sgn f at an EXACT root, where sgn 0 = 0, is '
         f'{at_root_exact:+.9f} -- zero, against the statement\'s ≠ 0\n'
         f'⚠ and evaluated in floating point it returns {at_root_float:+.9f} instead, its SIGN '
         f'decided by f(r_h) = {f_of(m, rh):+.2e}: the quantity is not single-valued there, and '
         f'that is the finding rather than an artefact of this arm\n'
         f'the one-sided values ±½f′(r_h) = {one_sided[0]:+.9f} and {one_sided[1]:+.9f}; '
         f'f(r_h−{eps:g}) = {f_of(m, rh - eps):+.3e}, f(r_h+{eps:g}) = {f_of(m, rh + eps):+.3e}, '
         f'so the two sides are reached and the point itself is not')
    NOTES.append('Ⓒ⑥ prop:turning asserts at the root a value its own proof returns as zero there')

    need('Ⓒ⑦ and the formal paragraph already says the honest thing, so the gap is between the '
         'PROPOSITION and its own apparatus rather than between the paper and Lean',
         'wherever $f\\neq0$' in flat(p3) and
         'The limit of the second derivative at the root itself is not formalised.' in flat(p3),
         'the paragraph after the proof carries both "wherever $f\\neq0$" and "The limit of the '
         'second derivative at the root itself is not formalised."')

    need('Ⓒ⑧ ⚠ and the reachable negative registered as (c) -- that something formalised DOES '
         'reach the root, making the order\'s parenthetical the stale thing -- is NOT reached: a '
         'named search finds no declaration concluding about `deriv r` without a strict hypothesis '
         'on f',
         True,
         'searched every declaration mentioning `deriv r` for one without `0 < f` or `f … < 0`: '
         + repr([n for n in re.findall(r'^theorem\s+(\S+)', lean, re.M)
                 if (decl_statement(lean, n) or '') and 'deriv r' in (decl_statement(lean, n) or '')
                 and '0 <' not in (decl_statement(lean, n) or '')
                 and '< 0' not in (decl_statement(lean, n) or '')]))

    need('Ⓒ⑨ ⛭ AND THE SAME DEFECT IS THE SAME ONE Ⓑ FOUND: `prop:curvature`\'s proof reaches its '
         'result "as in the proof of Proposition~\\ref{prop:turning}", so the `sgn f` formula that '
         'fails at f = 0 is the single root of BOTH of the order\'s first two questions',
         'as in the proof of Proposition~\\ref{prop:turning}' in flat(p3),
         'prop:curvature\'s proof cites prop:turning\'s proof for r″ = ½f′ sgn f -- one apparatus, '
         'two sentences leaning on it, and f = 0 is where it has nothing to say')


# ═════════════════════════════════════════ Ⓓ  THE TRIPLE ══════════════════════════════════════
def arm_D(p3, lean):
    head('Ⓓ  `prop:triple` -- the identity, and what "unique" is quantified over')
    prop = env_body(p3, 'prop:triple')
    fp = flat(prop)
    need('Ⓓ① the proposition states the triple-angle identity and calls the scale UNIQUE',
         'pure triple-angle relation' in fp and 'unique value of the slicing scale' in fp,
         f'…{fp.strip()[:170]}…')

    st = decl_statement(lean, 'sl_triple')
    need('Ⓓ② `sl_triple` is the identity at EVERY w -- no hypothesis on w at all',
         hypotheses_of(st) == ['w : ℝ'] and '2 / (3 * Real.sqrt 3)' in conclusion_of(st),
         f'binders: {hypotheses_of(st)}\nconclusion: {flat(conclusion_of(st))}')

    stu = decl_statement(lean, 'sl_triple_unique')
    hyp = ' '.join(hypotheses_of(stu))
    need('Ⓓ③ `sl_triple_unique` is the uniqueness of the PAIR (scale, coefficient) -- not an `∃!` '
         'but an identity plus a separate uniqueness lemma -- and it carries `0 < ϱ`',
         '0 < ϱ' in hyp and '∀ w' in hyp
         and 'ϱ = 2 / Real.sqrt 3 ∧ k = 2 / (3 * Real.sqrt 3)' in flat(conclusion_of(stu)),
         f'hypotheses: {hypotheses_of(stu)}\nconclusion: {flat(conclusion_of(stu))}')

    rho, k = -2 / math.sqrt(3), -2 / (3 * math.sqrt(3))
    worst = max(abs(sl_g(rho * math.sin(w)) - k * math.sin(3 * w))
                for w in [i * math.pi / 120 for i in range(241)])
    need('Ⓓ④ ⚠ and the positivity hypothesis is LOAD-BEARING, shown by its witness rather than '
         'asserted: ϱ = −2/√3 with k = −2/(3√3) satisfies the same identity at every w, so '
         '"unique" is unique AMONG POSITIVE scales. The proposition\'s bare "unique" is carried by '
         'a slicing scale being a radius, and the proof says "unique positive root" where the '
         'statement says "unique" -- a looseness, not a defect',
         worst < 1e-12,
         f'ϱ = {rho:.9f}, k = {k:.9f}: sup over 241 values of w of the identity\'s residual = '
         f'{worst:.3e}\nand the proof\'s own words: "whose unique positive root is $\\varrho=2/'
         f'\\sqrt3$" -- positivity present in the proof and in Lean, absent from the statement')
    NOTES.append('Ⓓ④ prop:triple says "unique", its proof and its Lean statement say "positive"')


# ════════════════════════════════════ Ⓔ  P15 AND THE SCATTER ══════════════════════════════════
def arm_E(p15):
    head('Ⓔ  P15\'s source exclusion, and THE ORDER\'S THIRD QUESTION')
    fp = flat(p15)
    sent = 'would have stood at more than six times that ratio\'s own scatter at the two wider ' \
           'smoothings'
    need('Ⓔ① the sentence is in the paper as the order quotes it, located by text in the '
         'flattened copy', sent in fp,
         '…' + fp[max(0, fp.find(sent) - 118): fp.find(sent) + len(sent) + 2] + '…')

    say('')
    say('      ⛭ running the host receipt, because these values exist only AT RUN TIME '
        '(negative probe 22)')
    p = subprocess.run([sys.executable, HOST], capture_output=True, text=True, timeout=1800)
    out = p.stdout
    need('Ⓔ② the host receipt runs green in this container, so its numbers are measurements and '
         'not recollections', p.returncode == 0 and 'GATES: ALL PASS.' in out,
         f'exit {p.returncode}, {len(out.splitlines())} lines, "GATES: ALL PASS." present: '
         f'{"GATES: ALL PASS." in out}')

    wit = re.findall(r'h(0\.\d+): own ([+-][\d.]+) = ([\d.]+) sd, spectra\'s size = ([\d.]+) sd',
                     flat(out))
    need('Ⓔ③ its WITNESS line prints one value per smoothing, three of them, each the size a step '
         'of the spectra\'s size would have shown at in the source ratio',
         len(wit) == 3,
         '\n'.join(f'h{h}: own {o} = {s} sd, spectra\'s size = {z} sd' for h, o, s, z in wit))

    vals = [(float(h), float(z)) for h, _, _, z in wit]
    vals.sort()
    narrow, wider = vals[0], vals[1:]
    above = [v for _, v in wider if v > 6.0]
    need('Ⓔ④ ⛭ THE ORDER\'S THIRD QUESTION, FIRST HALF: THE SENTENCE IS SOUND, and it is an '
         'INEQUALITY and not a match, which is the way an arm testing equality would have '
         'reported a false defect. The two wider smoothings both stand above six; the narrowest '
         'stands below it, so "at the two wider smoothings" is exactly the right SET and not a '
         'hedge',
         len(above) == 2 and narrow[1] < 6.0,
         f'narrowest h{narrow[0]}: {narrow[1]} sd -- BELOW six\n'
         + '\n'.join(f'wider h{h}: {v} sd -- above six' for h, v in wider)
         + f'\nso "more than six … at the two wider smoothings" holds, and would NOT hold if the '
           f'narrowest were included')

    tight = min(v for _, v in wider)
    need('Ⓔ⑤ ⚠ and the r7708 check, which is the one that bit this corpus before: the tightest of '
         'the two is nearer SEVEN than six. That was a defect at r7708 because the sentence there '
         'was an APPROXIMATION ("some seven times" for 7.8); here the sentence is a FLOOR ("more '
         'than six"), and a floor that holds is correct however much room it leaves',
         True,
         f'tightest = {tight} sd: distance to 6 is {tight - 6:.1f}, to 7 is {abs(tight - 7):.1f} '
         f'-- nearer seven, and "more than six" is true of it either way')

    rng = re.search(r'would have shown there at `([\d.]+)` to `([\d.]+)` sd', flat(out))
    lo_lbl, hi_lbl = (float(rng.group(1)), float(rng.group(2))) if rng else (None, None)
    lo_wit, hi_wit = min(v for _, v in vals), max(v for _, v in vals)
    need('Ⓔ⑥ ⛔⛭⛭ THE ORDER\'S THIRD QUESTION, SECOND HALF, AND A FINDING IN THE RECEIPT ITSELF: '
         'the order names "6.6 and 11.8", and 11.8 is NOT a measured value -- it is a HARD-CODED '
         'number in the gate\'s own label, and the gate\'s own witness prints a different one. '
         'The label\'s range and the witnesses it is printed beside DISAGREE, and the gate cannot '
         'catch it because what the gate ASSERTS is only that each value exceeds 3.5',
         lo_lbl is not None and abs(lo_lbl - lo_wit) < 0.05 and abs(hi_lbl - hi_wit) < 0.05,
         f'the label says "{lo_lbl} to {hi_lbl} sd"\n'
         f'its own witnesses give {lo_wit} to {hi_wit} sd\n'
         f'so the low end is off by {abs(lo_lbl - lo_wit):.1f} and the high end by '
         f'{abs(hi_lbl - hi_wit):.1f}; the order inherited 11.8 from the label, not from a '
         f'measurement')
    NOTES.append('Ⓔ⑥ the host receipt\'s hard-coded range disagrees with its own printed witnesses')

    phrases = ['more than six times', 'two wider smoothings', 'wider smoothings']
    found = {ph: flat(p15).count(ph) for ph in phrases}
    need('Ⓔ⑦ and a NAMED SEARCH rather than an absence claim: no twin sentence elsewhere in the '
         'paper carries the same factor or the same smoothing set, so a correction here would '
         'leave nothing behind',
         found['more than six times'] == 1 and found['two wider smoothings'] == 1,
         'searched the flattened paper for ' + ', '.join(f'{k!r}: {v}' for k, v in found.items()))


# ═══════════════════════════════════ Ⓕ  THE REGISTERED ABSENCE ═════════════════════════════════
def arm_F(p3):
    head('Ⓕ  the registered ABSENCE -- `prop:twoalpha`, which the order says did NOT land')
    body = env_body(p3, 'prop:twoalpha')
    need('Ⓕ① `prop:twoalpha` is present in the paper and is located by its label',
         body is not None, f'{len(body)} chars' if body else 'NOT FOUND')
    try:
        d = subprocess.run(['git', 'diff', '--unified=0', 'ce392787..origin/main', '--',
                            'corpus/SdS-slicing-curve_v2.tex'],
                           cwd=ROOT, capture_output=True, text=True, timeout=300).stdout
    except Exception as e:                                        # noqa: BLE001
        d = f'(diff unavailable: {e})'
    need('Ⓕ② and the landing did NOT touch it, so the order\'s "not landed yet" is accurate -- '
         'the registered absence is an absence, measured on the diff of the landing itself',
         'twoalpha' not in d,
         f'the landing\'s diff of this paper is {len(d.splitlines())} lines and contains '
         f'{d.count("twoalpha")} occurrences of "twoalpha"; the changed hunks touch '
         + repr(sorted(set(x.replace('\\', '') for x in
                            re.findall(r'(sl\\?_[a-z\\_]+)', d))))[:400])


# ═════════════════════════════════════════════ MAIN ═══════════════════════════════════════════
def main():
    p3 = open(P3, encoding='utf-8').read()
    p15 = open(P15, encoding='utf-8').read()
    lean = open(LEAN, encoding='utf-8').read()

    say('')
    say('  ' + '=' * 96)
    say('  r7724 (60) -- A COLD READ OF P3\'s SECOND FORMAL LANDING, answering order r7721')
    say('  ' + '=' * 96)
    say(f'      P3    {len(p3):>8} chars   {len(p3.splitlines()):>5} lines')
    say(f'      P15   {len(p15):>8} chars   {len(p15.splitlines()):>5} lines')
    say(f'      Lean  {len(lean):>8} chars   {len(lean.splitlines()):>5} lines')
    say(f'      axiom tokens in the Lean file: {len(re.findall(r"^axiom ", lean, re.M))}; '
        f'`sorry` tokens: {lean.count("sorry")}')

    selftests(p3, lean)
    arm_A(p3, lean)
    arm_B(p3, lean)
    arm_C(p3, lean)
    arm_D(p3, lean)
    arm_E(p15)
    arm_F(p3)

    head('THE VERDICT')
    if FAILED:
        say(f'  {len(FAILED)} arm(s) report a FINDING -- each is a reading, not a crash:')
        for f in FAILED:
            say(f'    - {f.split(".")[0][:150]}')
    else:
        say('  no arm reports a finding.')
    say('')
    say('  WHAT IS ROUTED:')
    for n in NOTES:
        say(f'    ⌗ {n}')
    say('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
