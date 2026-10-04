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
          r'\Psi': 'Psi', r'\Phi': 'Phi'}


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
        s = s[:m.start()] + '_' + re.sub(r'[^A-Za-z0-9]', '', inner.replace('\\', '')) + s[a1 + 1:]
    s = re.sub(r'_\s*(\\[A-Za-z]+|[A-Za-z0-9])', lambda m: '_' + m.group(1).lstrip('\\'), s)
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


def equation(tex, label):
    """The body of the equation carrying `\\label{label}`, as LaTeX.

    Asserts the label occurs EXACTLY ONCE in the paper -- the same control as `r7153`'s
    `len(m) == 1`: an attribution to a label the paper carries twice is not an attribution.
    """
    src = tex if '\n' in tex else open(tex, encoding='utf-8').read()
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
