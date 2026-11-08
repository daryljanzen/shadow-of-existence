#!/usr/bin/env python3
"""r7716 (60) -- P2's new back-seam sentence, read cold.

Arms registered in PREDICTION.md before the sentence, or any of the four new
declarations, was read.  The readers r7714 repaired are carried forward unchanged
and re-tested on their negatives before use.  Every verdict below is BUILT FROM its readings; nothing
is asserted that is not printed first.

GUARDS.  G1 one predicate per conjunct.  G2 three anchor forms only -- a prose
marker must be plain prose, an escaped control sequence with ONE leading
backslash, or an escaped math delimiter; anything else is REFUSED before use.
G3 the flip family, striking EVERY copy.  G4 classifier probes tested on BOTH
classes before use.  G5 reader probes with negatives.  G6 every prose probe runs
on a WHITESPACE-FLATTENED copy, since the source wraps mid-sentence.
"""
import re
import sys

ROOT = '/home/user/shadow-of-existence'
P2 = ROOT + '/corpus/janzen_circle_v3.tex'
LEAN = ROOT + '/computations/formalisation/lean/probes/CircleBackSeam.lean'

FAIL = []
def say(*a):
    print(*a)
def need(label, ok):
    say(('   ok  ' if ok else '  FAIL ') + label)
    if not ok:
        FAIL.append(label)
    return ok

def flat(s):
    """G6: one line, single spaces."""
    return re.sub(r'\s+', ' ', s)

# ---------------------------------------------------------------- G2 anchors
def anchor(marker):
    """G2: a marker is usable only in one of the three anchored forms."""
    if re.fullmatch(r'[A-Za-z0-9 ,.;:\'\-()]+', marker):
        return 'prose'
    if re.fullmatch(r'\\[A-Za-z]+(\{[^{}]*\})?', marker):
        return 'macro'
    if re.fullmatch(r'\$[^$]+\$', marker):
        return 'math'
    return None

def anchored(marker):
    kind = anchor(marker)
    if kind is None:
        say(f'  G2 REFUSED (unanchored marker): {marker!r}')
        FAIL.append('G2 refused a marker: ' + marker)
        return False
    return True

# -------------------------------------------- the name-skeleton matcher (r7712)
GREEK = {'\u03a6': 'Phi', '\u03a8': 'Psi', '\u03b7': 'eta', '\u03c1': 'rho',
         '\u03c4': 'tau', '\u0393': 'Gamma'}

def cited_in_tex(tex, name):
    """A NAME IS A FORM (negative probe 19).  P2 prints Greek letters in MATH
    MODE inside \\texttt, so the literal character is not what is on the page.
    Match the name's SKELETON: each ASCII run in order, each Greek letter as the
    character, as $\\X$, as \\X, or as X."""
    parts = []
    for ch in name:
        if ch in GREEK:
            g = GREEK[ch]
            parts.append('(?:' + re.escape(ch) + r'|\$\\' + g + r'\$|\\' + g + '|' + g + ')')
        elif ch == '_':
            parts.append(r'\\?_')
        else:
            parts.append(re.escape(ch))
    return re.search(''.join(parts), tex) is not None

def decl_header(src, name):
    """The header of a declaration: from its keyword to the ':=' or 'by' that
    begins its proof.  Binders are read from the HEADER ONLY, so casts in the
    body are never reported as hypotheses (r7706)."""
    m = re.search(r'^(?:theorem|lemma|def|abbrev|noncomputable def)\s+' + re.escape(name)
                  + r'\b', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    cut = len(tail)
    for pat in (r'\s:=\s', r'\sby\s*$', r'\sby\s'):
        mm = re.search(pat, tail, re.M)
        if mm and mm.start() < cut:
            cut = mm.start()
    return flat(tail[:cut])

def decl_extent(src, name):
    """A declaration's WHOLE text, bounded by where the NEXT declaration begins
    (the r7708 lesson).  decl_header stops at ':=' so that binders are read from
    the header only; a `def`'s CONTENT lives after ':=' and needs this."""
    m = re.search(r'^(?:theorem|lemma|def|abbrev|noncomputable def)\s+' + re.escape(name)
                  + r'\b', src, re.M)
    if not m:
        return None
    tail = src[m.start():]
    nxt = re.search(r'\n(?:/--|@\[|theorem|lemma|def|abbrev|noncomputable|variable|include|end)\s',
                    tail[1:])
    return flat(tail[:nxt.start() + 1] if nxt else tail)

def binders(header):
    """Bracket-depth matching, so a binder whose TYPE carries parentheses is not
    invisible (r7706)."""
    out, i = [], 0
    while i < len(header):
        if header[i] in '({[':
            close = {'(': ')', '{': '}', '[': ']'}[header[i]]
            depth, j = 0, i
            while j < len(header):
                if header[j] in '({[':
                    depth += 1
                elif header[j] in ')}]':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j < len(header) and header[j] == close:
                out.append(header[i:j + 1])
            i = j + 1
        elif header[i] == ':':
            break
        else:
            i += 1
    return out


# ------------------------------------------- the classifiers this revision needs
def covering_shape(header):
    """COVERING, read by the SHAPE of the statement and not by the word.  A
    covering claim quantifies over the RADIUS and produces a POINT; a domain
    claim quantifies over points, or asserts only that something is defined.
    Returns 'covering', 'domain' or 'other'."""
    concl = header.rsplit(') :', 1)[-1] if ') :' in header else header
    first = concl.split('∧')[0]
    over_r = re.search(r'∀\s*r\s*<\s*0', first)
    makes_point = re.search(r'∃\s*p\s*∈', first) or re.search(r'∃\s*\(?[uv]', first)
    if over_r and makes_point:
        return 'covering'
    if over_r or re.search(r'∀\s*\(?p', first):
        return 'domain'
    return 'other'


def constructs_object(src, name):
    """An OBJECT is CONSTRUCTED when a declaration gives it a STRUCTURE TYPE with
    fields, not when properties of functions are proved about it.  `def x : T
    where` / `:= { .. }` is a construction; a theorem about `f r` is not."""
    ext = decl_extent(src, name)
    if ext is None:
        return False
    hdr = ext.split(':=')[0] if ':=' in ext else ext
    typed = re.search(r'def\s+' + re.escape(name) + r'\s*(\([^)]*\))*\s*:\s*[A-Za-z_][\w.]*',
                      hdr)
    return bool(typed) and ('where' in ext[:400] or 'with' in ext[:200])

# =============================================================== SELF-TESTS
def selftests(p2flat):
    say('=' * 78)
    say('SELF-TESTS -- every classifier and reader on BOTH of its classes, before use')
    say('=' * 78)

    # G2, carried forward, on all three anchor forms and one that mixes.
    need('G2 accepts plain prose', anchor('covering every r less than zero') == 'prose')
    need('G2 accepts an escaped control sequence', anchor(r'\texttt') == 'macro')
    need('G2 accepts an escaped math delimiter', anchor('$r<0$') == 'math')
    need('G2 REFUSES a marker mixing prose with math',
         anchor(r'the patches at $r < 0$') is None)

    # the skeleton matcher, carried forward, on its negatives.
    need('skeleton: a plain ASCII name IS found',
         cited_in_tex(r'(\texttt{bs\_backseam})', 'bs_backseam'))
    need('skeleton: a math-mode Greek name IS found',
         cited_in_tex(r'(\texttt{ce\_$\Psi$\_inj})', 'ce_Ψ_inj'))
    need('skeleton: a name NOT on the page is NOT found',
         not cited_in_tex(r'(\texttt{bs\_backseam})', 'bs_nowhere'))
    need('skeleton: a name that is a PREFIX of another is not credited to it',
         not cited_in_tex(r'(\texttt{bs\_coeffs})', 'bs_coeffs_two'))

    # the declaration readers, carried forward from r7714 WITH their negatives.
    need('reader: bs_backseam has a header', decl_header(LEANSRC, 'bs_backseam') is not None)
    need('reader: a declaration that does not exist reads as absent',
         decl_header(LEANSRC, 'bs_backseam_not_a_declaration') is None)
    need('reader: decl_extent reaches a def\'s BODY, which lives after ":="',
         '1 - 2 * M / r' in (decl_extent(LEANSRC, 'bs_f') or ''))
    need('reader: decl_extent stops before the NEXT declaration',
         'bs_f1' not in (decl_extent(LEANSRC, 'bs_f') or ''))
    need('reader: binders survive a type carrying parentheses',
         binders('theorem t (hM : 0 < M) {x : Fin 4 → ℝ} (hx : (x 0, x 1) ∈ bs_Ω) :')
         == ['(hM : 0 < M)', '{x : Fin 4 → ℝ}', '(hx : (x 0, x 1) ∈ bs_Ω)'])

    # G4: the COVERING classifier, on both classes.
    need('covering classifier: over the RADIUS, producing a POINT, is covering',
         covering_shape('theorem t (hM : 0 < M) : (∀ r < 0, ∃ p ∈ bs_Ω, '
                        'bs_s M p.1 p.2 = r) ∧ Q') == 'covering')
    need('covering classifier: over POINTS is a DOMAIN claim and not covering',
         covering_shape('theorem t (hM : 0 < M) : (∀ p ∈ bs_Ω, bs_s M p.1 p.2 < 0) '
                        '∧ Q') == 'domain')
    need('covering classifier: a limit statement is neither',
         covering_shape('theorem t (hM : 0 < M) : Filter.Tendsto (bs_f M) Filter.atBot '
                        '(nhds 1)') == 'other')

    # G4: the OBJECT classifier, on both classes.
    need('object classifier: a structure-valued def with fields IS a construction',
         constructs_object(LEANSRC, 'bs_SD'))
    need('object classifier: a real-valued def is NOT a construction',
         not constructs_object(LEANSRC, 'bs_f'))
    need('object classifier: a theorem is NOT a construction',
         not constructs_object(LEANSRC, 'bs_coeffs'))

    # G6: the flattener, on a sentence the source wraps.
    need('G6: the back-seam sentence is one line only after flattening',
         'machine-checked as a geometry in their own right' in p2flat)
    say('')


# ==================================================================== ARMS
def q1(p2flat, lean):
    say('=' * 78)
    say('Q1 -- IS "covering every $r<0$" WHAT bs_backseam\'s FIRST CONJUNCT PROVES?')
    say('=' * 78)
    mark = 'and covering every $r<0$'
    anchored('and covering every r less than zero')
    need('the phrase is at source, verbatim', mark in p2flat)
    h = decl_header(lean, 'bs_backseam')
    say(f'    bs_backseam: {h}')
    shape = covering_shape(h or '')
    say(f'    READING: the first conjunct\'s shape is ..... {shape}')
    need('the first conjunct quantifies over the RADIUS and produces a POINT, which IS '
         'covering and not a domain claim', shape == 'covering')
    say('    ⌗ And what makes it reachable: the tortoise is strictly monotone and ONTO.')
    for n in ('bs_rs_strictMonoOn', 'bs_rs_surj', 'bs_ρ_image'):
        say(f'    {decl_header(lean, n)}')
    need('the tortoise is strictly monotone on the patch', 
         'StrictMonoOn' in (decl_header(lean, 'bs_rs_strictMonoOn') or ''))
    need('and its inverse\'s image is the whole of the patch\'s radius range',
         "bs_ρ M '' Set.Iio 0 = Set.Iio 0" in (decl_extent(lean, 'bs_ρ_image') or ''))
    return shape


def q2(p2flat, lean):
    say('')
    say('=' * 78)
    say('Q2 -- DOES "a geometry in their own right" CLAIM MORE THAN THE CITATIONS GIVE?')
    say('      The phrase names an OBJECT; a list of properties is not an object.')
    say('=' * 78)
    need('the phrase is at source, verbatim',
         'The two $r<0$ patches are machine-checked as a geometry in their own right' in p2flat)

    say('')
    say('  (a) IS AN OBJECT CONSTRUCTED?  Read from the declaration, not the prose:')
    ext = decl_extent(lean, 'bs_SD') or ''
    say(f'    bs_SD: {ext[:200]}')
    need('bs_SD is a STRUCTURE-valued def with fields -- a warped metric datum, not a '
         'list of coefficient properties', constructs_object(lean, 'bs_SD'))
    good = decl_header(lean, 'bs_SD_good')
    say(f'    {good}')
    need('and its goodness is CHECKED on the patch\'s own open set',
         good is not None and 'Good bs_Ω' in good)
    kr = decl_header(lean, 'bs_kretschmann')
    say(f'    {kr}')
    need('the curvature is computed from THAT object\'s metric', 'bs_SD M).gW' in (kr or ''))

    say('')
    say('  (b) THE HEDGE -- read from the declaration\'s hypotheses, not from the prose:')
    say(f'    binders: {binders(kr or "")}')
    need('"away from the poles of the sphere\'s chart" is a REAL hypothesis '
         '(sin of the polar angle non-zero), and it is in the stem already',
         'Real.sin (x 2) ≠ 0' in (kr or '')
         and "away from the poles of the sphere's chart" in p2flat)

    say('')
    say('  (c) ⛔ OVER WHAT, THOUGH -- the registered third outcome, and the corpus guard:')
    say('      *before two stretches are identified by a label, check how many-to-one')
    say('      the label is on the object.*')
    say(f'    {decl_extent(lean, "bs_Ω")}')
    say(f'    {decl_extent(lean, "bs_s")}')
    need('bs_Ω is ONE region of the null plane',
         'p.2 - p.1 < 0' in (decl_extent(lean, 'bs_Ω') or ''))
    need('and bs_s gives each radius ONCE on it, since the tortoise is strictly monotone, '
         'so the object\'s radius runs over the range exactly once',
         'bs_ρ M ((v - u) / 2)' in (decl_extent(lean, 'bs_s') or ''))
    # a NAMED search, reported as NOT FOUND over the names it had (negative probe 19).
    rel = [n for n in ('bs_reflection', 'bs_reflect', 'bs_glue', 'bs_iso', 'bs_isometry',
                       'bs_patches', 'bs_two')
           if decl_header(lean, n) is not None]
    say(f'    NAMED SEARCH for a declaration relating the TWO patches -- '
        f'bs_reflection, bs_reflect, bs_glue, bs_iso, bs_isometry, bs_patches, bs_two: '
        f'{rel if rel else "NOT FOUND over all seven names"}')
    shape = [n for n in re.findall(r'^(?:theorem|lemma)\s+(bs_\w+)', lean, re.M)
             if re.search(r'∃\s*\w*\s*,?.*(?:Isometr|=\s*-)',
                          decl_header(lean, n) or '')]
    say(f'    AND BY THE SHAPE of its conclusion over every bs_ theorem: '
        f'{shape if shape else "none states a relation between two copies"}')
    need('NOTHING in the file relates the two patches -- no reflection, no gluing, no '
         'isometry -- which the exteriors needed ce_reflection for',
         not rel and not shape)
    say('')
    say('    AND THE PLURAL SUBJECT, read rather than waved at: is "the two patches" ')
    say('    carried DISTRIBUTIVELY by machine-checked facts?')
    cyp = decl_header(lean, 'cy_patches') or ''
    rneg = [c for c in cyp.split('\u2227') if 'Real.cosh' in c and '1 - Real.cosh' in c]
    for c in rneg:
        say(f'      {c.strip()}')
    need('cy_patches checks BOTH branches (s = 1 and s = -1) give the SAME real radius, '
         'so the two patches agree in the quantity every item of the list is a function of',
         's = 1 \u2228 s = -1' in cyp and '1 - Real.cosh' in cyp)
    need('and that both are ONTO the whole range, so neither is a proper part of it',
         '\u2200 r \u2208 Iio 0, \u2203 \u03c1 > 0, M * (1 - Real.cosh \u03c1) = r' in cyp)
    say('    ⌗ READING: every item in the sentence\'s own colon-list is a function of the')
    say('      RADIUS alone, and cy_patches checks both branches share it, so each item')
    say('      holds of EACH patch identically -- the plural subject is carried')
    say('      DISTRIBUTIVELY, and machine-checked. What no declaration states is a')
    say('      relation BETWEEN the two, so the one reading the sentence does NOT')
    say('      support is the COLLECTIVE one, where the two together form a single')
    say('      geometry. That is not the paper\'s own reading elsewhere, which keeps them')
    say('      as two patches "both with r = M(1 - cosh rho)".')
    return True


def q3(p2flat):
    say('')
    say('=' * 78)
    say('Q3 -- DOES THE SENTENCE SIT CONSISTENTLY BESIDE THE SKETCH\'S COMPANION CLAUSE?')
    say('=' * 78)
    sketch = ('their geometric identity---the backward radial direction, the negative root '
              'of the horizon cubic---is established in the companion slicing paper')
    anchored('their geometric identity')
    need('the sketch\'s clause is still at source, verbatim', sketch in p2flat)
    need('and it is in the PROOF SKETCH, upstream of the formal paragraph',
         p2flat.find(sketch) < p2flat.find('machine-checked as a geometry in their own right'))
    say('')
    say('    THE TWO CLAIMS, compared as the registered predicate requires:')
    say('      sketch:  WHICH geometry -- "geometric identity", named as the backward')
    say('               radial direction and the negative root of the horizon cubic,')
    say('               and sent to the companion paper.')
    say('      formal:  THAT it is one -- horizonless, asymptotically flat coefficients,')
    say('               a chart covering every radius, a finite curvature scalar.')
    for np in ('geometric identity', 'backward radial direction', 'negative root'):
        i = p2flat.find('machine-checked as a geometry in their own right')
        seg = p2flat[i:i + 900]
        say(f'      is {np!r} claimed in the formal sentence? {np in seg}')
    i = p2flat.find('machine-checked as a geometry in their own right')
    seg = p2flat[i:i + 900]
    need('the formal sentence claims NONE of the identity words, so it does not claim '
         'what the sketch sends to the companion paper',
         not any(np in seg for np in
                 ('geometric identity', 'backward radial direction', 'negative root')))
    need('and the sketch claims none of the formal sentence\'s properties, so neither '
         'is redundant',
         not any(np in p2flat[max(0, p2flat.find(sketch) - 200):p2flat.find(sketch) + 300]
                 for np in ('horizonless,', 'Kretschmann scalar is')))
    return True


def item4(p2flat, lean):
    say('')
    say('=' * 78)
    say('ITEM 4 -- THE REST OF THE LANDING')
    say('=' * 78)
    half = ('each chart map being onto its quadrant of the domain, horizons excluded '
            '(\\texttt{cp\\_onto\\_BH}, \\texttt{cp\\_onto\\_RE} and \\texttt{cp\\_kruskal}, in '
            '\\texttt{CirclePatches.lean})')
    need('4a this seat\'s half-repair is landed, verbatim', half in p2flat)
    say('    ⌗ "horizons excluded" is READ rather than assumed: the onto theorems\' own')
    say('      binders carry STRICT sign conditions, so the quadrants are open and the')
    say('      horizons are the partition\'s separate fifth set.')
    cp = ROOT + '/computations/formalisation/lean/probes/CirclePatches.lean'
    cpsrc = open(cp).read()
    for n in ('cp_onto_BH', 'cp_onto_RE'):
        say(f'    {decl_header(cpsrc, n)}')
    need('both onto theorems ask STRICT inequalities, so "horizons excluded" is exact',
         all(re.search(r'0 < [UV]|[UV] < 0', decl_header(cpsrc, n) or '')
             for n in ('cp_onto_BH', 'cp_onto_RE'))
         and 'cp_Hor : Set P' in (decl_extent(cpsrc, 'cp_Hor') or ''))

    say('')
    last = 'That the Kruskal--Szekeres extension is maximal is not formalised.'
    need('4b the last sentence is at source, verbatim', last in p2flat)
    need('its OLD second clause -- the $r<0$ patches as a geometry -- is gone from it, '
         'which is what this landing checks',
         'the $r<0$ patches as a geometry in their own right, are not formalised'
         not in p2flat)
    # and the thing it still bounds is bounded: a NAMED search for maximality.
    names = [n for n in ('bs_maximal', 'bs_inextendible', 'cp_maximal', 'sk_maximal')
             if decl_header(lean, n) is not None]
    say(f'    NAMED SEARCH for a maximality declaration -- bs_maximal, bs_inextendible, '
        f'cp_maximal, sk_maximal: {names if names else "NOT FOUND over all four names"}')
    need('and by the SHAPE: no bs_ or cp_ declaration mentions maximality or '
         'inextendibility at all',
         not re.search(r'(?:Maximal|maximal|Inextendible|inextendible)',
                       '\n'.join(decl_header(lean, n) or '' for n in
                                 re.findall(r'^(?:theorem|lemma)\s+(bs_\w+)', lean, re.M))))

    say('')
    for n in ('bs_coeffs', 'bs_SD', 'bs_kretschmann', 'bs_backseam'):
        h = decl_header(lean, n)
        need(f'4c {n} exists', h is not None)
        need(f'4c {n} is cited in P2 (by SKELETON)', cited_in_tex(p2flat, n))
    say(f'    bs_coeffs: {decl_header(lean, "bs_coeffs")}')
    bc = decl_header(lean, 'bs_coeffs') or ''
    need('bs_coeffs states all three things the prose attributes to it -- $f>1$ on the '
         'patch, and $f$ and $f^{-1}$ tending to one',
         '∀ r < 0, 1 < bs_f M r' in bc and bc.count('Filter.Tendsto') == 2)

    say('')
    nax = len(re.findall(r'^axiom\s', lean, re.M))
    nsorry = len(re.findall(r'\bsorry\b', lean))
    say(f'    4d CircleBackSeam.lean: axiom tokens = {nax}; sorry = {nsorry}')
    need('zero axiom tokens and zero sorry', nax == 0 and nsorry == 0)
    return True


def main():
    global LEANSRC
    p2 = flat(open(P2).read())
    LEANSRC = open(LEAN).read()
    selftests(p2)
    q1(p2, LEANSRC)
    q2(p2, LEANSRC)
    q3(p2)
    item4(p2, LEANSRC)
    say('')
    say('=' * 78)
    if FAIL:
        say(f'{len(FAIL)} ARM(S) FAILED:')
        for f in FAIL:
            say('  - ' + f)
        return 1
    say('ALL ARMS AND SELF-CHECKS PASS.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
