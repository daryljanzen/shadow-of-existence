#!/usr/bin/env python3
r"""The FOURTH ARM, built on PART OF SPEECH rather than on a fourth word for a closed list.

`r7265` ruled it: three shortfalls in a bound list is not bad luck, it is the list's shape.

** AND THE REASON THE LIST KEPT COMING UP SHORT IS A FACT ABOUT ENGLISH, NOT ABOUT THE LIST. **
*Verbs are an OPEN class -- new ones arrive, and a corpus's verbs are not enumerable in advance --
while DETERMINERS are a CLOSED class, and a list of them can be complete.*
  ⇒ *** So this arm tests the open class BY ITS DISTRIBUTION AGAINST THE CLOSED ONE, and the only
      list it carries is the one that can be finished. ***

** THE DIAGNOSTIC. **  *A noun is frequently preceded by a determiner; a finite verb almost never is.
So for a word `w` occurring `n` times in the corpus, with `d` of those occurrences immediately
preceded by a determiner, `d/n` is low for verbs and high for nouns -- the classic distributional
test, computed here on the corpus the spans are pinned into rather than on an outside tagger.*

⚠ ** THE CLOSED WORD LIST OF THE ADOPTED TEST IS NOT TOUCHED. **  *It is imported, byte-for-byte, so
`r7257`'s and `r7258`'s figures stay reproducible from it, and both arms are reported on the SAME
population so a change in the cell is attributable to the arm and not to the revision.*

COMPUTES: scope.
  * The corpus is `corpus/*.tex` minus the generated appendices, LaTeX commands and math stripped.
  * NOT CLAIMED: that `d/n` is a part-of-speech TAGGER.  It is one diagnostic, calibrated on controls
    drawn from the corpus itself, and its separation is reported rather than assumed.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED arms, byte-for-byte

# ── the one closed class this arm needs, and it IS closed ────────────────────────────────────────
DET = frozenset('''a an the this that these those its their his her our your my no every each
some any all both either neither which what whose'''.split())

_CMD = re.compile(r'\\[A-Za-z@]+\s*(\*)?(\[[^\]]*\])?')
_MATH = re.compile(r'\$[^$]*\$')
_WORD = re.compile(r"[a-z][a-z'\-]*")


def corpus_words():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(p).startswith('appendix_receipts'):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
        t = _MATH.sub(' MATH ', t)
        t = _CMD.sub(' ', t).replace('{', ' ').replace('}', ' ')
        out += _WORD.findall(t.lower())
    return out


WORDS = corpus_words()
N = {}
AFTER_DET = {}
BEFORE_DET = {}
for _i, _w in enumerate(WORDS):
    N[_w] = N.get(_w, 0) + 1
    if _i and WORDS[_i - 1] in DET:
        AFTER_DET[_w] = AFTER_DET.get(_w, 0) + 1
    if _i + 1 < len(WORDS) and WORDS[_i + 1] in DET:
        BEFORE_DET[_w] = BEFORE_DET.get(_w, 0) + 1

MIN_N = 20          # below this the ratio is noise, and the arm declines rather than guesses


def det_ratio(w):
    """how often a determiner comes BEFORE `w` -- high for nouns"""
    n = N.get(w, 0)
    return None if n < MIN_N else AFTER_DET.get(w, 0) / n


# ⛔⛭⛭⛭ ONE DISTRIBUTIONAL AXIS IS NOT ENOUGH, AND THE FIRST CUT OF THIS ARM PROVED IT ON ITSELF.
#   *`d/n` low says `not a noun`, which is not the same as `a verb`: the first run's widening was
#   `24` keys and among them were formula heads (`n`, `x`, `f`, `l`, `m`), ADVERBS (`exactly`,
#   `nearly`, `strictly`), a NEGATOR, a SUBORDINATOR and two NUMERALS.  **Adverbs and symbols are not
#   preceded by determiners either, so the test separated NOUN from NOT-NOUN and I had wanted VERB
#   from NOT-VERB.***
#     ⇒ *** So the arm carries a SECOND axis, and a verb is what satisfies both: rarely preceded by a
#         determiner AND often FOLLOWED by one -- `shows the`, `gives a`, `selects the`.  A noun fails
#         the first, an adverb and a symbol fail the second. ***
def det_after_ratio(w):
    """how often a determiner comes AFTER `w` -- high for transitive verbs, low for adverbs"""
    n = N.get(w, 0)
    return None if n < MIN_N else BEFORE_DET.get(w, 0) / n


def head_word(lit):
    m = _WORD.search(D.STRIP.sub('', lit).lower())
    return m.group(0) if m else None


# ── the calibration, two-sided, on sets drawn from the corpus and not hand-picked ────────────────
def calibrate():
    """(verb-like control median, noun-like control median, the threshold, the margin)

    *POSITIVES: the adopted list's own finite verbs that occur often enough to measure -- known
    verbs, so a HIGH ratio on them would refute the diagnostic.  NEGATIVES: the words most often
    FOLLOWING a determiner, which are nouns by construction and need no list at all.*
    """
    verbs = sorted({w for w in re.findall(r"[a-z][a-z'?]*", D._FINITE1.replace('|', ' '))
                    if det_ratio(w) is not None})
    nouns = sorted({w for w, c in AFTER_DET.items()
                    if c >= 40 and det_ratio(w) is not None and w not in verbs})[:400]
    vr = sorted(det_ratio(w) for w in verbs)
    nr = sorted(det_ratio(w) for w in nouns)
    vmed = vr[len(vr) // 2]
    nmed = nr[len(nr) // 2]
    # the threshold is the geometric midpoint of the two medians, so neither control sets it alone
    thr = (vmed * nmed) ** 0.5 if vmed > 0 else nmed / 10
    # the SECOND axis, calibrated the same way and on the same two control sets
    va = sorted(det_after_ratio(w) for w in verbs)
    na = sorted(det_after_ratio(w) for w in nouns)
    vamed, named = va[len(va) // 2], na[len(na) // 2]
    athr = (vamed * named) ** 0.5 if named > 0 else vamed / 10
    return verbs, nouns, vr, nr, vmed, nmed, thr, vamed, named, athr


VERBS, NOUNS, VR, NR, VMED, NMED, THR, VAMED, NAMED, ATHR = calibrate()


def dangles_pos(lit):
    """True when the span's HEAD word is VERB-like on BOTH distributional axes"""
    h = head_word(lit)
    if h is None or h in DET or len(h) < 3:
        return False          # a one- or two-letter head is a symbol, not a part of speech
    r, a = det_ratio(h), det_after_ratio(h)
    if r is None or a is None:
        return False
    #: ⛔⛭⛭ r7298+60, on r7289's 78th member: this arm asks whether the span NAMES ITS OWN SUBJECT, so
    #: it is a SUBJECT TEST and takes the full closed determiner class.  Before r7294 it reached the
    #: demonstrative-only exemption through the unscoped name --- the borrowed-exemption defect, here
    #: in this line's OWN caller, and the signature change is what surfaced it.
    return r < THR and a > ATHR and not D.names_own_subject(lit)


def main():
    print()
    print('=' * 92)
    print('  THE FOURTH ARM -- part of speech by distribution, not a fourth word on a closed list')
    print('=' * 92)
    print(f'    corpus: {len(WORDS)} word tokens, {len(N)} types; {len(DET)} determiners (CLOSED)')
    print(f'    calibration: {len(VERBS)} known-verb controls, median d/n = {VMED:.4f}')
    print(f'                 {len(NOUNS)} noun controls (words following a determiner >= 40 times),'
          f' median d/n = {NMED:.4f}')
    print(f'    axis ONE  (determiner BEFORE): verbs {VMED:.4f} vs nouns {NMED:.4f}, '
          f'a factor of {NMED / VMED if VMED else float("inf"):.1f};  threshold < {THR:.4f}')
    print(f'    axis TWO  (determiner AFTER) : verbs {VAMED:.4f} vs nouns {NAMED:.4f}, '
          f'a factor of {VAMED / NAMED if NAMED else float("inf"):.1f};  threshold > {ATHR:.4f}')
    print('    *** A word is VERB-LIKE only on BOTH axes: one axis separates noun from not-noun, '
          'which is not what the arm needs. ***')
    _vfp = [w for w in VERBS if not (det_ratio(w) < THR and det_after_ratio(w) > ATHR)]
    _nfp = [w for w in NOUNS if det_ratio(w) < THR and det_after_ratio(w) > ATHR]
    print(f'    controls that cross it: {len(_vfp)} of {len(VERBS)} verbs ABOVE, '
          f'{len(_nfp)} of {len(NOUNS)} nouns BELOW')
    print(f'      verbs above  : {", ".join(_vfp[:12])}')
    print(f'      nouns below  : {", ".join(_nfp[:12])}')

    rd = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict',
                      'READING.tsv')
    keys = []
    for line in open(rd, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        c = line.rstrip('\n').split('\t')
        if len(c) >= 2:
            keys.append(c[1])
    keys = [k for k in keys if k]
    print()
    print(f'    THE POPULATION: {len(keys)} keys, the ones r7260 verdicted, read from its own table')
    closed = {k for k in keys if D.dangles(k)}
    pos = {k for k in keys if dangles_pos(k)}
    print(f'      the THREE ADOPTED ARMS flag      : {len(closed)}')
    print(f'      the PART-OF-SPEECH arm flags     : {len(pos)}')
    print(f'      part-of-speech ONLY (the widening): {len(pos - closed)}')
    print(f'      closed-list ONLY                 : {len(closed - pos)}')
    print(f'      both                             : {len(pos & closed)}')
    print()
    print('    THE WIDENING, by name:')
    for k in sorted(pos - closed)[:40]:
        print(f'      + `{k[:80]}`   head `{head_word(k)}` before={det_ratio(head_word(k)):.4f} after={det_after_ratio(head_word(k)):.4f}')
    print()
    print('    WHAT THE CLOSED LIST CATCHES AND THIS ARM DOES NOT:')
    for k in sorted(closed - pos)[:40]:
        h = head_word(k)
        r = det_ratio(h)
        print(f'      - `{k[:84]}`   head `{h}` at '
              + (f'd/n={r:.4f}' if r is not None else f'n={N.get(h, 0)} (below MIN_N)'))
    print()
    print(f'  ⇒ the order\'s threshold was fixed before this ran: the arm must flag at least 4 keys '
          f'the closed list misses.  Measured: {len(pos - closed)}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
