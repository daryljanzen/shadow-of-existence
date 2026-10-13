#!/usr/bin/env python3
r"""notation_table.py -- THE CLOSED TABLE THAT DECIDES WHETHER TWO SPELLINGS ARE ONE SPELLING.

** WHY THIS IS CODE AND NOT PROSE. **  `r7299` ordered the `ENCODING-OK` ground written in `69`'s
form: *tests over the span and its check that three readers would answer the same way*.  A ground for
a NOTATION class cannot be three readers agreeing that two strings "look like the same thing" --
that is the judgement the ground exists to remove.
  => *** So the ground is a CLOSED, ORDERED list of rewrites, and two spellings are one spelling iff
      the list takes both to the same string.  Nothing is added to the list by a reader at the point
      of use: adding to it is a revision, with its own receipt. ***

** EACH STEP IS NAMED so a verdict can cite the step it needed. **  A pair that needs only `braces`
is a brace-style difference; a pair that needs `binding` is a pair of two SYNTAXES for one binding,
which is the widest step in the table and the one to drop first if the table is cut back.

(c) node 60.  `dangling_predicate_v2.py` is this line's other instrument; this is the second.
"""
import re

GREEK = ('alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu '
         'xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta '
         'Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega ell infty partial nabla sqrt equiv cdot '
         'times approx simeq cos sin tan cosh sinh tanh exp log ln').split()
WRAP = 'emph textit textbf mathrm mathbf mathit text mathcal mathbb operatorname rcpt'.split()
CIRCLED = {chr(0x245F + i): str(i) for i in range(1, 10)}
WORDNUM = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10'}
_NUMTOK = re.compile(r'(?<![A-Za-z0-9.])\d+(?:\.\d+)?(?:[eE][+-]?\d+)?(?![A-Za-z0-9.])')

# the ordered, CLOSED table.  each step is named so a verdict can cite the step it needed.
STEPS = ('wrap', 'size', 'greek', 'spacecmd', 'mathdelim', 'emphasis', 'braces',
         'separators', 'case', 'circled', 'wordnum', 'numeric', 'binding')


def norm(s, upto=None):
    t = s
    use = STEPS if upto is None else STEPS[:STEPS.index(upto) + 1]
    if 'wrap' in use:
        t = re.sub(r'\\(?:' + '|'.join(WRAP) + r')\s*\{', '{', t)
    if 'size' in use:
        t = re.sub(r'\\(?:left|right|big|Big|bigg|Bigg)(?![A-Za-z])', '', t)
    if 'greek' in use:
        t = re.sub(r'\\(' + '|'.join(GREEK) + r')(?![A-Za-z])', r'\1', t)
    if 'spacecmd' in use:
        t = re.sub(r'\\[,;!:>&% /]', '', t)
    if 'mathdelim' in use:
        for a in ('$', '\\(', '\\)', '\\[', '\\]'):
            t = t.replace(a, '')
    if 'emphasis' in use:
        for a in ('**', '__', '`'):
            t = t.replace(a, '')
    if 'braces' in use:
        t = t.replace('{', '').replace('}', '')
    if 'separators' in use:
        t = re.sub(r'[\s\-‐-―_,]+', '', t)
    if 'case' in use:
        t = t.lower()
    if 'circled' in use:
        for a, b in CIRCLED.items():
            t = t.replace(a, b)
    if 'wordnum' in use:
        for a, b in WORDNUM.items():
            t = re.sub(a, b, t)
    if 'numeric' in use:
        t = _NUMTOK.sub(lambda m: repr(float(m.group(0))), t)
    if 'binding' in use:
        t = re.sub(r"['\"=]+", '', t)
    return t


def needed_step(a, b):
    """the FIRST step of the table at which a and b already agree, or None."""
    for i, s in enumerate(STEPS):
        if norm(a, s) == norm(b, s):
            return s
    return None
