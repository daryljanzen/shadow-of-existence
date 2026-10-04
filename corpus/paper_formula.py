r"""paper_formula -- read a LABELLED EQUATION out of a paper and return it as sympy.

`r7153`'s repair template was: make the receipt PARSE the figure out of the paper's own
sentence rather than carry it as a literal.  This is that template at the next size up --
**an EXPRESSION in a labelled equation instead of a number in a sentence** -- and it is what
the `NO-READ/FORMULA` class needs, because what those receipts attribute is a formula.

⌗ WHAT IT IS NOT.  This is not a LaTeX parser.  It translates the narrow dialect the corpus's
own display equations are written in, and it is built to FAIL rather than to guess: an
unknown macro survives translation as itself and then raises out of `sympify`, which is the
behaviour wanted.  A silent mistranslation is the one outcome that would make a receipt agree
with a paper it had misread.

⛭ THE CONTROL that makes it usable at all: every call site asserts the parsed form equals the
expression the receipt had hard-coded BEFORE the repair.  So the first use of this module is
to confirm the literals, and only then to replace them.
"""
import os
import re

import sympy as sp

#: the spacing and sizing macros that carry no content
_DROP = (r'\left', r'\right', r'\,', r'\;', r'\:', r'\!', r'\quad', r'\qquad',
         r'\displaystyle', r'\dd', r'\nonumber',
         #: sizing macros carry no content, longest first so `\Bigl` does not leave an `l`
         r'\biggl', r'\biggr', r'\bigg', r'\Bigl', r'\Bigr', r'\Big',
         r'\bigl', r'\bigr', r'\big')
#: name macros -> a bare identifier sympy can hold
_NAMES = {r'\alpha': 'alpha', r'\Lambda': 'Lambda', r'\lambda': 'lambda_', r'\pi': 'pi',
          r'\tau': 'tau', r'\theta': 'theta', r'\phi': 'phi', r'\chi': 'chi', r'\psi': 'psi',
          r'\varepsilon': 'varepsilon', r'\ell': 'ell', r'\Omega': 'Omega', r'\omega': 'omega',
          r'\rho': 'rho', r'\sigma': 'sigma', r'\mu': 'mu', r'\nu': 'nu', r'\eta': 'eta',
          r'\Delta': 'Delta', r'\delta': 'delta', r'\Gamma': 'Gamma', r'\gamma': 'gamma',
          r'\sqrt': 'sqrt', r'\cosh': 'cosh', r'\sinh': 'sinh', r'\tanh': 'tanh',
          r'\coth': 'coth', r'\csch': 'csch', r'\cos': 'cos', r'\sin': 'sin', r'\tan': 'tan',
          r'\log': 'log', r'\exp': 'exp', r'\infty': 'oo',
          #: ⌗ `\psi` is declared above; `check_loaders` caught it listed twice here, where the
          #: later entry would have silently won and any edit to the first been discarded at load.
          r'\Psi': 'Psi', r'\Phi': 'Phi', r'\beta': 'beta'}


def _brace(s, i):
    """The span of the {...} group starting at `i` (which must be `{`)."""
    assert s[i] == '{', (s[i:i + 20],)
    d = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0:
                return j
    raise AssertionError('unbalanced brace: ' + s[i:i + 40])


def _frac(s):
    """`\\frac{A}{B}` -> `((A)/(B))`, innermost first, until none remain."""
    while True:
        m = re.search(r'\\(?:frac|dfrac|tfrac)\s*\{', s)
        if not m:
            return s
        a0 = s.index('{', m.start())
        a1 = _brace(s, a0)
        assert s[a1 + 1:].lstrip().startswith('{'), 'frac without a second group: ' + s[m.start():m.start() + 40]
        b0 = s.index('{', a1 + 1)
        b1 = _brace(s, b0)
        s = s[:m.start()] + f'(({s[a0 + 1:a1]})/({s[b0 + 1:b1]}))' + s[b1 + 1:]


def _tud(s):
    """`\\Tud{a}{b}` -> `Tud_a_b`, the corpus's mixed stress-energy macro."""
    while True:
        m = re.search(r'\\Tud\s*\{', s)
        if not m:
            return s
        a0 = s.index('{', m.start())
        a1 = _brace(s, a0)
        b0 = s.index('{', a1 + 1)
        b1 = _brace(s, b0)
        a = _NAMES.get('\\' + s[a0 + 1:a1].strip().lstrip('\\'), s[a0 + 1:a1].strip().lstrip('\\'))
        b = _NAMES.get('\\' + s[b0 + 1:b1].strip().lstrip('\\'), s[b0 + 1:b1].strip().lstrip('\\'))
        s = s[:m.start()] + f'Tud_{a}_{b}' + s[b1 + 1:]


def _bare_arg(s):
    r"""`\tfrac12` -> `\tfrac{1}{2}` and `\sqrt\Lambda` / `\sqrt3` -> `\sqrt{...}`.

    TeX lets a one-token argument go unbraced.  Normalising here keeps the brace-matched
    rewrites below as the only places that have to think about arguments.
    """
    s = re.sub(r'\\(t|d)?frac(\d)(\d)', r'\\frac{\2}{\3}', s)
    s = re.sub(r'\\sqrt\s*(\\[A-Za-z]+|\d|[A-Za-z])', r'\\sqrt{\1}', s)
    return s


def _subscripts(s):
    r"""`X_{\mathrm{SdS}}`, `X_{r}`, `X_a` -> one identifier `X_SdS`, `X_r`, `X_a`.

    A subscript in these papers NAMES a thing (`\Delta_r`, `f_{\rm SdS}`, `\Omega_m`); it is
    never an index to compute with, so it becomes part of the symbol's name.
    """
    s = re.sub(r'\\(?:mathrm|mathit|text|rm|operatorname)\s*\{([^{}]*)\}', r'\1', s)
    while True:
        m = re.search(r'_\s*\{', s)
        if not m:
            break
        a0 = s.index('{', m.start())
        a1 = _brace(s, a0)
        inner = s[a0 + 1:a1]
        assert '{' not in inner, 'paper_formula: nested subscript ' + repr(inner)
        #: ⛔ ⛭ r7161+cc66.128: ** `X_{+}` AND `X_{-}` BOTH BECAME `X_`, AND THAT IS A SILENT WRONG
        #: ANSWER RATHER THAN A REFUSAL. **  The strip below removes every non-alphanumeric, so a sign
        #: subscript vanished: `\alpha_{+}-\alpha_{-}` translated to `alpha_-alpha_`, which is
        #: IDENTICALLY ZERO -- a difference of two distinct quantities reading as vanishing.  *Measured
        #: on the shipped dialect, which I wrote at r7157, while extending it for the `-6H^2` site.*
        #:   · `+` and `-` are NAMED, as `plus` and `minus`, because a sign subscript labels a thing
        #:     (Misner's `\beta_{\pm}`, a root `r_{\pm}`) and is not an index to compute with -- the
        #:     same reading this function already applies to `\Delta_r`.
        #:   · and a subscript that strips to NOTHING is now REFUSED, which is the general repair: the
        #:     two sign cases are the ones these papers use, and anything else that would collapse to a
        #:     bare `X_` stops the parse instead of colliding with its sibling.
        _sub = inner.replace('\\', '')
        for _a, _b in (('+', 'plus'), ('-', 'minus')):
            _sub = _sub.replace(_a, _b)
        _sub = re.sub(r'[^A-Za-z0-9]', '', _sub)
        assert _sub or not inner.strip(), (
            'paper_formula: the subscript %r carries nothing a symbol name can hold, so `%s_` would '
            'collide with every other subscript of the same base. The site is refused rather than '
            'translated to a name that is not its own.' % (inner, s[:m.start()].strip()[-12:]))
        s = s[:m.start()] + '_' + _sub + s[a1 + 1:]
    s = re.sub(r'_\s*(\\[A-Za-z]+|[A-Za-z0-9])', lambda m: '_' + m.group(1).lstrip('\\'), s)
    return s


def _dot(s):
    r"""`\dot\beta_{+}` / `\dot{x}` -> `<name>_dot`, a symbol distinct from the undotted one.

    ⌗ The same convention as `_tilde`, and for the same reason: a dot NAMES a different quantity (a
    time derivative) and this dialect holds symbols rather than differentiating.  ** A receipt that
    wants the derivative COMPUTED must compute it; what this gives it is the paper's own name for it. **
    ⛔ And `\dot` applied to a BRACKETED EXPRESSION rather than a single name is refused, because
    `\dot{(ab)}` is a derivative of a product and naming it `ab_dot` would assert a factorisation the
    paper did not write.
    """
    #: ⛔ the braced form must hold ONE NAME and nothing else.  The first draft of this guard looked
    #: for an operator inside the braces, which let `\dot{(ab)}` through as `(ab)_dot` -- a name that
    #: asserts the derivative of a product is a symbol.  *Caught by testing the guard against the case
    #: it was written for, which is the fourth time this round that my check was narrower than my
    #: claim.*  An allow-list of "a single name" refuses every such form instead of enumerating them.
    for _m in re.finditer(r'\\dot\s*\{([^{}]*)\}', s):
        assert re.fullmatch(r'\\?[A-Za-z]+', _m.group(1).strip()), (
            'paper_formula: `\\dot` applied to %r, which is not a single name. This dialect NAMES a '
            'dotted symbol rather than differentiating, so the site is refused instead of being given '
            'a name that asserts a structure the paper did not write.' % _m.group(1))
    s = re.sub(r'\\dot\s*\{([^{}]*)\}', lambda m: m.group(1).lstrip('\\') + '_dot', s)
    s = re.sub(r'\\dot\s*(\\[A-Za-z]+|[A-Za-z])', lambda m: m.group(1).lstrip('\\') + '_dot', s)
    return s


def _tilde(s):
    r"""`\tilde\tau` / `\tilde{x}` -> `<name>_tilde`, a symbol distinct from the untilded one."""
    s = re.sub(r'\\tilde\s*\{([^{}]*)\}', lambda m: m.group(1).lstrip('\\') + '_tilde', s)
    s = re.sub(r'\\tilde\s*(\\[A-Za-z]+|[A-Za-z])', lambda m: m.group(1).lstrip('\\') + '_tilde', s)
    return s


_FN = (r'sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|coth|csch|sech|log|exp'
       r'|arcsin|arccos|arctan|operatorname\{csch\}|operatorname\{sech\}')


def _fn_power(s):
    r"""`\coth^{2}(x)` -> `(\coth(x))^{2}`.

    ⌗ THIS IS A CONVENTION AND NOT A GUESS, which is why it is translated rather than refused.
    For a NAMED function `f^{n}(x)` means `(f(x))^{n}` throughout this corpus's papers and in
    ordinary usage -- `\coth^2`, `\cosh^2`, `\csch^2`.  *The one reading that is NOT this is
    `f^{-1}`, the inverse, so a negative exponent is left alone and then refused downstream.*
    ⛔ Before this, the rewrites below turned `\coth^2(x)` into `coth**2 * (x)` -- a silent wrong
    answer over the right symbols.  Refusing it was better than that; translating it is better still.
    """
    pat = re.compile(r'\\(' + _FN + r')\s*\^\s*(?:\{(\d+)\}|(\d+))')
    while True:
        m = pat.search(s)
        if not m:
            return s
        fn, n = m.group(1), (m.group(2) or m.group(3))
        j = m.end()
        while j < len(s) and (s[j].isspace() or s.startswith('\\!', j) or s.startswith('\\,', j)):
            j += 2 if s[j] == '\\' else 1
        #: the argument: a braced group, a (possibly \left-sized) bracket, or one bare token
        if j < len(s) and s[j] == '{':
            k = _brace(s, j)
            arg, rest = s[j + 1:k], s[k + 1:]
        elif s.startswith('\\left(', j) or (j < len(s) and s[j] == '('):
            o = s.index('(', j)
            d, k = 0, None
            for i in range(o, len(s)):
                if s[i] == '(':
                    d += 1
                elif s[i] == ')':
                    d -= 1
                    if d == 0:
                        k = i
                        break
            assert k is not None, 'paper_formula: unbalanced bracket after ' + fn
            arg, rest = s[o + 1:k], s[k + 1:]
            arg = arg.replace('\\left', '').replace('\\right', '')
        else:
            mt = re.match(r'(\\[A-Za-z]+|[A-Za-z0-9])', s[j:])
            assert mt, 'paper_formula: no argument after %s^%s' % (fn, n)
            arg, rest = mt.group(1), s[j + mt.end():]
        s = s[:m.start()] + '((\\%s(%s))^{%s})' % (fn, arg, n) + rest


def to_text(frag):
    """The LaTeX fragment as a sympify-able string.  Raises on anything it cannot name."""
    s = frag
    s = _fn_power(s)
    s = _bare_arg(s)
    s = _dot(s)
    s = _tilde(s)
    s = _frac(s)
    s = _tud(s)
    s = _subscripts(s)
    for d in _DROP:
        s = s.replace(d, ' ')
    # primes: f'' and f' are distinct symbols, longest first
    s = re.sub(r"([A-Za-z])''", r'\1pp', s)
    s = re.sub(r"([A-Za-z])'", r'\1p', s)
    #: ⛔ THE PADDING IS LOAD-BEARING AND SO IS ITS EXCEPTION.  A macro becomes ` name ` so that
    #: `8\pi` reads as a product under implicit multiplication -- but a macro that CARRIES A
    #: SUBSCRIPT is one identifier, and padding it split `\Delta_{r}` into `Delta * _r`, which the
    #: strict check then rejected as an undeclared `_r`.  *Found by the strict check refusing three
    #: sites that the dialect can in fact carry: the guard caught my own translator, not the paper.*
    for k in sorted(_NAMES, key=len, reverse=True):
        s = re.sub(re.escape(k) + r'(?=_)', _NAMES[k], s)
        s = s.replace(k, ' ' + _NAMES[k] + ' ')
    s = s.replace('^', '**')
    # `**{2}` -> `**(2)`;  bare `{...}` groups are grouping only
    s = s.replace('{', '(').replace('}', ')')
    s = s.replace('&', ' ')
    assert '\\' not in s, 'paper_formula: unhandled macro in ' + repr(frag[:80])
    #: ⛔ `\coth^2(x)` means `(coth x)^2` and NOT `coth**2 * (x)`, which is what the rewrites
    #: above would produce.  That is a SILENT mistranslation -- the one outcome that would make a
    #: receipt agree with a paper it had misread -- so it is refused instead of guessed.
    _fn = r'(?:sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|coth|csch|sech|sqrt|log|exp)'
    #: ⛔ AND A PRIMED NAME FOLLOWED BY A BRACKET IS AN APPLICATION, NOT A PRODUCT.
    #: `\Delta_{r}''(r)` rewrites to `Delta_rpp(r)`, which implicit multiplication reads as the
    #: PRODUCT `Delta_rpp * r`.  *The strict check cannot catch it: both names are declared, so it
    #: returns a plausible expression over the right symbols and the wrong operation.*
    #: ⌗ THE TEST IS THE PRIME AND NOT THE BRACKET, and getting that wrong cost two passes.  A first
    #: version refused ANY identifier before a bracket, which also refused `-4\Lambda(r^{2}+p^{2})` --
    #: where juxtaposition IS multiplication and the paper means exactly that.  **`f'(x)` is an
    #: application in every reading; `\Lambda(x)` is a product in this corpus's.**  So the raw
    #: fragment is tested for a prime immediately before a bracket, before the prime is rewritten
    #: away, and an undeclared name is left to the strict check below.
    assert not re.search(r"['\u2032]+\s*\\?[a-z]*\s*\(", frag), (
        'paper_formula: %r applies a PRIMED name to an argument; this dialect multiplies instead of '
        'applying, so the site is refused rather than mistranslated.' % frag[:70])
    assert not re.search(_fn + r'\s*\*\*', s), (
        'paper_formula: a function raised to a power is outside this dialect -- '
        '`f^n(x)` is ambiguous here and is not guessed: ' + repr(frag[:80]))
    return s


def to_sympy(frag, locals_=None, strict=True):
    """The LaTeX fragment as a sympy expression, with implicit multiplication.

    ⛭ `strict` (the default) asserts every free symbol of the result was SUPPLIED by the
    caller.  Without it, `parse_expr` silently invents a `Symbol` for any name the rewrites
    above mangled -- so a mistranslation would return a plausible expression over symbols
    nobody declared, and compare unequal for a reason that looks like physics.  *With it, a
    name this dialect cannot carry fails at the call site, which is where it can be read.*
    """
    from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                            implicit_multiplication_application,
                                            convert_xor)
    t = standard_transformations + (implicit_multiplication_application, convert_xor)
    loc = dict(locals_ or {})
    out = parse_expr(to_text(frag), local_dict=loc, transformations=t, evaluate=True)
    if strict:
        #: ⛭ WHAT COUNTS AS DECLARED.  A caller may map a paper's name to an EXPRESSION rather
        #: than a symbol -- `f_SdS` is a whole metric function, `t` is this file's `eta` -- so the
        #: result's free symbols legitimately include everything reachable from the supplied values.
        #: *Comparing against the keys alone refused two sites that the dialect carries correctly;
        #: the guard was right in intent and wrong in detail, and this is the detail.*
        allowed = set(loc)
        for _v in loc.values():
            fs = getattr(_v, 'free_symbols', None)
            if fs:
                allowed |= {str(a) for a in fs}
        undeclared = sorted(str(a) for a in out.free_symbols if str(a) not in allowed)
        assert not undeclared, (
            'paper_formula: %r is not carried by this dialect -- undeclared symbol(s) %s '
            'in %r.  Supply them, or read this site by hand.' % (frag[:60], undeclared, to_text(frag)[:90]))
    return out


#: ⛔ ⛭ r7164+cc66.134: ** "CONTAINS A NEWLINE" WAS A PROXY FOR "IS TEXT", AND IT SENT 400 KB OF A
#: PAPER TO `open()` AS A FILENAME. **  Both readers took `tex` as a path unless it held a newline.
#: `P15_the_bead_routes...` reads its paper through a helper that NORMALISES WHITESPACE, so the body it
#: hands over is text with no newline in it -- and the call died on `File name too long` rather than on
#: anything about the paper.
#: ⇒ A path is now what a path actually is: no newline, short enough to be one, AND present on disk.
#: Anything else is the source itself.  ⌈ `os.path.exists` swallows the OSError a 400 KB "name" raises,
#: so the length bound is what makes the test decide rather than merely not crash.
#: *Seventh of this round's shape and the first in the instrument's API rather than its logic: a
#: property that USUALLY accompanies the thing is not the thing.*
def _source(tex):
    """The paper's text, whether `tex` is the text or a path to it."""
    if '\n' not in tex and len(tex) < 4096 and os.path.exists(tex):
        return open(tex, encoding='utf-8').read()
    return tex


def equation(tex, label):
    """The body of the equation carrying `\\label{label}`, as LaTeX.

    Asserts the label occurs EXACTLY ONCE in the paper -- the same control as `r7153`'s
    `len(m) == 1`: an attribution to a label the paper carries twice is not an attribution.
    """
    src = _source(tex)
    tag = r'\label{%s}' % label
    assert src.count(tag) == 1, f'{label}: the paper carries {src.count(tag)} copies, not one'
    i = src.index(tag)
    starts = [m.start() for m in re.finditer(r'\\begin\{(equation|align|gather|equation\*|align\*)\}', src) if m.start() < i]
    assert starts, f'{label}: no display environment opens before it'
    b = starts[-1]
    e = re.search(r'\\end\{(equation|align|gather|equation\*|align\*)\}', src[i:])
    assert e, f'{label}: no display environment closes after it'
    body = src[src.index('}', b) + 1:i + e.start()]
    # inside an align, keep only the line carrying this label
    if '\\\\' in body:
        lines = [l for l in body.split('\\\\') if tag in l or label in l]
        assert len(lines) == 1, f'{label}: {len(lines)} aligned lines carry it'
        body = lines[0]
    body = body.replace(tag, ' ')
    body = re.sub(r'\\label\{[^}]*\}', ' ', body)
    body = re.sub(r'\\qquad.*$', '', body, flags=re.S)
    body = re.sub(r'\\text\{[^}]*\}', ' ', body)
    #: ⌗ AN APPROXIMATION IS A DIFFERENT CLAIM FROM AN EQUALITY, so the exact chain ends at the
    #: first `\approx`.  `eq:ds-entropy` reads `S = A/4l^2 = pi(a/l)^2 = 3pi/(Lambda l^2) \approx 3e122`:
    #: what a receipt attributes to it is the exact tail, and the numeric estimate after it is the
    #: paper rounding, not the identity.  *Keeping it would make the dialect refuse the site instead.*
    body = re.split(r'\\(?:approx|simeq|sim|propto|lesssim|gtrsim)', body)[0]
    return body.strip().rstrip(',.').strip()


def rhs(tex, label, locals_=None):
    """The LAST side of the labelled equation, as sympy.

    `8\\pi T^t_t = 8\\pi T^r_r = <expr>` has three sides and the claim is about the last.
    """
    body = equation(tex, label)
    parts = [p for p in body.split('=') if p.strip()]
    assert len(parts) >= 2, f'{label}: not an equation -- {body[:60]!r}'
    return to_sympy(parts[-1], locals_)


def sides(tex, label, locals_=None):
    """Every side of the labelled equation, as sympy, in the paper's own order."""
    body = equation(tex, label)
    parts = [p for p in body.split('=') if p.strip()]
    return [to_sympy(p, locals_) for p in parts]


# ---------------------------------------------------------------------------- r7161+cc66.123
#: ** THE INLINE READER: for a figure the paper states in a SENTENCE and not in a labelled display. **
#: `equation()` keys on `\label{}`, which is why `r7155`'s feasibility measurement split the backlog
#: into `17 ANCHORED` and `14 NO-ANCHOR`.  The `NO-ANCHOR` sites are not harder, they are a different
#: claim: the expression is inline math inside prose (`the degeneracy is $2(n-1)(n+3)$`), and the paper
#: never writes the RECEIPT's form at all -- so there is nothing to compare a left side against and the
#: labelled-display template is the wrong instrument rather than an unavailable one.
#:
#: ⛭ AGREEMENT, NOT UNIQUENESS -- the `r7159` correction, here by construction.  Four of the seven
#: expressions these sites cite occur more than once in their paper, so `exactly once` would refuse a
#: paper for restating its own result.  Every occurrence is PARSED and compared as an expression, so a
#: re-spacing, a `\!` or a `\left` is not a disagreement.
#:
#: ⛔ AND A PREFIX OF A LONGER EXPRESSION IS NOT AN OCCURRENCE.  `canonical_time.tex` writes both
#: `R=4\Lambda` and `R=4\Lambda+\kappa\Theta`; `n(n+2)` also appears inside `n(n+2)-2`.  A reader that
#: counted those would compare the trace-coupled form against the vacuum one and then "agree" with
#: itself.  *Found by COUNTING the occurrences before writing the repair, and recorded in
#: `r7161_cc66_nine_derivation/PREDICTION.md` before either was touched.*  So a match whose next
#: character would CONTINUE the expression is skipped, and the count of skipped ones is returned rather
#: than swallowed -- a reader that silently drops half its matches is the same defect one level down.
def _extends(src, j):
    """Would the text at `j` continue a mathematical expression?  `+`, `-`, a digit, a letter or a
    LaTeX name do; `$`, punctuation, `\\,` and a `\\\\` line break do not."""
    t = src[j:j + 2]
    if not t:
        return False
    if t[0] in '+-*/^_=' or t[0].isdigit() or t[0].isalpha():
        return True
    if t[0] == '\\' and len(t) > 1:
        return t[1].isalpha()
    return False


#: ⛔ ⛭ r7161+cc66.124: ** AND A SUFFIX IS NOT AN OCCURRENCE EITHER, WHICH THE FIRST VERSION GOT WRONG
#: AND WOULD HAVE ANSWERED SILENTLY. **  `_extends` looks only FORWARD, so `(n-1)(n+3)` -- which the
#: NEXT receipt in this block cites -- read as `kept=2, skipped=0` against a paper that writes
#: `2(n-1)(n+3)` both times.  *That is not a refusal and not a disagreement: it is the degeneracy
#: without its factor of two, attributed to the paper as if the paper had printed it.*
#: ⇒ Found by testing the instrument against the NEXT site before using it there, rather than by the
#: site passing wrongly.  ⌗ The trailing case was predicted and the leading one was not, and they are
#: the same class -- *a boundary rule written on one side is half a boundary rule.*
#: ⌈ STATED LIMIT, because naming it is the honest half: a match preceded by `(` is treated as a
#: boundary, so an expression quoted out of the inside of a group is still readable.  Requiring more
#: would refuse `$(n-1)(n+3)$` itself.  A receipt citing a parenthesised sub-expression therefore gets
#: no protection from this rule and has to be read by hand.
def _preceded(src, i):
    """Would the text ending at `i` be part of a LARGER expression to its left?"""
    k = i - 1
    while k >= 0 and src[k] == ' ':
        k -= 1
    if k < 0:
        return False
    ch = src[k]
    return ch in '+-*/^_)}' or ch.isdigit() or ch.isalpha()


def inline(tex, pattern, locals_=None, strict=True):
    """Parse an expression the paper states inline, from EVERY occurrence, requiring agreement.

    `pattern` is a regex matching the expression as the paper writes it.  Returns
    `(expr, kept, skipped)`: the agreed sympy expression, how many occurrences were read, and how
    many were skipped as prefixes of something longer.
    """
    src = _source(tex)
    kept, skipped, got = [], 0, None
    for m in re.finditer(pattern, src):
        if _extends(src, m.end()) or _preceded(src, m.start()):
            skipped += 1
            continue
        kept.append(m)
    #: ⛭ r7161+cc66.123: ** NO MATCH AND ALL-SKIPPED ARE DIFFERENT FINDINGS AND WERE ONE MESSAGE. **
    #: The first draft said "matches 0 time(s) and every one of them is a PREFIX", which is incoherent
    #: at zero and would have sent a reader looking for a longer expression that does not exist.
    #: *Found by the pre-registered perturbation test (`Q5`), which is what that test is for: it
    #: perturbed the paper, the refusal fired correctly, and the SENTENCE was wrong.*
    #:   · 0 matches  ⇒ the paper does not carry this expression at all: a DRIFTED attribution, or a
    #:     pattern that does not match how the paper writes it.  Either way not a parse failure.
    #:   · matched but every one skipped ⇒ the paper states it only INSIDE something longer, so it is
    #:     not a figure the paper asserts on its own.  `canonical_time`'s `-6H^{2}` is exactly this:
    #:     the paper prints `K_{ij}K^{ij}-K^{2}=-6H^{2}+6(...)` and `-6H^2` is its ISOTROPIC LIMIT,
    #:     which a receipt must derive rather than quote.
    if not kept:
        assert skipped, (
            'paper_formula.inline: %r does not match the paper at ALL. Either the paper no longer '
            'carries this expression -- a DRIFTED attribution, which is a finding and not a parse '
            'failure -- or the pattern does not match how the paper writes it.' % (pattern,))
        raise AssertionError(
            'paper_formula.inline: %r matches %d time(s) in the paper and EVERY ONE is PART of a '
            'longer expression -- extended on the left, the right or both -- so the paper never states '
            'this figure on its own; it states something of which this is a part. What the receipt '
            'claims is a DERIVED CONSEQUENCE and not a quotation, and it has to be derived here rather '
            'than pattern-matched.' % (pattern, skipped))
    for m in kept:
        frag = m.group(1) if m.groups() else m.group(0)
        e = to_sympy(frag, locals_, strict=strict)
        if got is None:
            got = e
        else:
            assert sp.simplify(got - e) == 0, (
                'paper_formula.inline: the paper states %r as %r in one place and %r in another, which '
                'do not agree as expressions -- the paper contradicts itself and no reading of it is '
                'the attribution.' % (pattern, str(got), str(e)))
    return got, len(kept), skipped
