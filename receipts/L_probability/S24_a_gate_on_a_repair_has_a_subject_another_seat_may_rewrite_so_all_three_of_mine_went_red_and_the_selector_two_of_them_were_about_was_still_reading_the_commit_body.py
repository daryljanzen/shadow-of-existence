#!/usr/bin/env python3
r"""S24 -- `r7267`'s three rulings, worked; and what all three of this line's own snapshot gates did.

COMPUTES: nothing the papers quote.  This receipt measures three instruments of the corpus's own
gate layer -- a reference-commit pin, a revision selector and an ownership predicate -- and the
population is the two sibling receipts and the restraint gate that carry them.

** ⛔⛭⛭⛭ `r7266` NAMED FIVE GATES THAT STORED A SNAPSHOT OF A RULE.  SECTION `Ⓕ` OF ITS OWN RECEIPT
WAS WRITTEN TO ASSERT THAT THOSE FIVE HAD BEEN REPAIRED -- AND ALL THREE OF ITS GATES HAVE NOW GONE
RED, EACH ON A LEGITIMATE REPAIR BY THE OTHER SEAT. **
  ⇒ *** A GATE THAT ASSERTS A REPAIR LANDED HAS AS ITS SUBJECT A THING ANOTHER SEAT MAY REWRITE, SO
      IT MUST ASSERT THE REPAIR'S *PROPERTY* AND NEVER ITS FORM. *** *That is not the same statement
      as `r7266`'s, which was about a rule's REACH changing.  This one is about a gate whose subject
      is somebody else's code, and the three instances are the three ways it went wrong:*
  ⌈ *`Ⓕ①` asked for the identifier `BEFORE = '` -- the NAME this seat's repair chose, broken when the
    trunk's spelling arrived; repaired at `r7266` and the reason this receipt exists.*
  ⌈ *`Ⓕ②` asked for the ABSENCE of `--grep`, so when `66` selected a range's start by the
    pre-registration's SUBJECT -- better than a bare sha, because it says WHAT the start is -- the
    gate called the better instrument the defect.*
  ⌊ *`Ⓕ③` asked for the PARITY predicate this seat wrote, which `66` reversed. **The reversal is
    accepted and the numbers are below: parity would own `591` of `1{,}025` live receipts against the
    prefix pair's `325`, so it retires the restraint claim rather than bounding it.***

** ⛔⛭⛭⛭ AND THE SELECTOR TWO OF THOSE GATES WERE ABOUT WAS STILL READING THE COMMIT BODY, LIVE ON
`main`, IN THE SIBLING THE REPAIR WAS COPIED FROM. **  *`r7264` found that `--grep` matches the whole
message and repaired `S22`.  `S21` kept `f'--grep={tag}'` over its own range, and nothing noticed
because `Ⓕ②` was asking a question about the OTHER receipt's spelling.*
  ⇒ *** Measured on the trunk before this repair: `10` commits matched, `7` of them IN THE BODY ALONE,
      and the file set read `38` where the revision's own commits touched `11`. *** ⌗ *One of the
      seven is this line's own commit saying a restraint selector was too broad: **the defect ate the
      sentence describing it**.*
  ⌊ *Repaired the way `S22` was: match on `%s`, the subject line, which is the one part of a message
    that names the revision the commit IS rather than a revision it mentions.*

** ⛭⛭ AND `P03`'s OWNERSHIP PREDICATE DID NOT OWN THE FILE THE GATE IS IN -- ONE GATE WITH TWO
DEFINITIONS OF `MINE`, AND THE WEAKER ONE WAS IN THE CLAIM. **  *The restraint gate already resolves
WHICH COMMITS ARE THIS SEAT'S by the session marker on the introducing commit.  It then asked a
different question of the FILES: do they sit under one of two path prefixes.*
  ⇒ *** `receipts/P03_SdS_slicing/` matches neither, so the clause read THIS SEAT EDITING ITS OWN
      RECEIPT as a crossing -- which is exactly what this branch did, one crossing, and the file was
      that receipt. ***  *So ownership is read with the gate's own marker, asked of the file: `+95`
      receipts against parity's `+266`, and the difference is receipts introduced by OTHER sessions of
      this line, which a claim about THIS SEAT'S restraint was never about.*

** ⛔⛭ AND THE GUARD AGAINST A BLANKET AUTHORISATION WAS ITSELF A SNAPSHOT OF THE CROSSING SET. **
*`r7267` bounded the restraint claim by carrying the authorised crossings BY NAME and asserting that
each is a path the branch CURRENTLY crosses -- true on the trunk it was written on, false on any tree
where those commits have merged out of the range the gate reads.*  ⇒ *Measured here: **both
authorisations uncrossed on this branch and the clause red**, on a branch that had crossed neither.
Pinned at the commit that MADE each crossing -- `L-249` again, which is what this whole stretch has
been about -- with the live arm kept as the fast path.*

⌗ *Sources: `r7267`'s three rulings; `S23`'s section `Ⓕ` read at `4f28c24b`, the merge commit where
all three of its gates were red, and live; `S21`'s selector censused over its own range both ways;
`P03` run to completion; and the ownership counts recomputed from the introducing commit of every
live receipt.*
"""

import io
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED arms, byte-for-byte

CHECKS = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


# ⛔⛭⛭ THE REFERENCE COMMIT IS A LITERAL SHA WITH A RESOLVE-AND-ANCESTOR GUARD, which is the form
#   `r7267` ruled better than a bare sha and better than a relation: a bad pin fails LOUDLY.
BEFORE = '4f28c24b'      # the merge commit at which all three of S23's section-Ⓕ gates were red


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True).stdout


def before_resolves():
    ok = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                        capture_output=True).returncode == 0
    anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                         capture_output=True).returncode == 0
    return ok, anc


def at_before(rel):
    r = subprocess.run(['git', 'show', f'{BEFORE}:{rel}'], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def run(rel, timeout=1800):
    return subprocess.run([sys.executable, os.path.join(ROOT, rel)],
                          cwd=os.path.dirname(os.path.join(ROOT, rel)),
                          capture_output=True, text=True, timeout=timeout)


S21 = ('receipts/L_probability/S21_a_pre_registered_negative_can_fire_without_reaching_the_claim_it_'
       'was_written_to_test_and_mine_did_while_the_order_was_wrong_about_both_defects_in_opposite_'
       'directions.py')
S22 = ('receipts/L_probability/S22_the_sentence_over_reached_and_the_receipt_cited_on_it_under_'
       'reached_so_the_rcpt_convention_was_violated_at_a_site_where_nothing_could_fail.py')
S23 = ('receipts/L_probability/S23_four_items_and_every_one_was_mis_described_because_five_gates_'
       'stored_a_snapshot_of_a_rule_instead_of_the_rule.py')
P03 = ('receipts/P03_SdS_slicing/P03_the_enclosed_mass_is_monotone_so_the_turnaround_ratio_cannot_'
       'fall_below_one_and_the_contested_direction_is_two_different_quantities.py')
_S5 = ('receipts/L_probability/S5_the_set_shaped_class_is_absent_from_the_gate_layer_and_two_thirds_'
       'of_what_remains_sits_at_the_one_value_where_the_standing_guards_repair_is_a_tautology.py')
HERE_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, '/')

print()
print('=' * 100)
print("S24 -- r7267's three rulings, and the three gates this line wrote about other seats' code")
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE REFERENCE COMMIT, ASSERTED BEFORE ANYTHING IS READ THROUGH IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res, _anc = before_resolves()
_s23b, _s23l = at_before(S23), read(S23)
_p03b, _p03l = at_before(P03), read(P03)
_s21b, _s21l = at_before(S21), read(S21)
gate(f'Ⓐ① ⛔⛭⛭ the reference is a LITERAL SHA (`{BEFORE}`), it RESOLVES (`{_res}`), it is an ANCESTOR '
     f'of `HEAD` (`{_anc}`), and all three files come back from it DIFFERING from the working tree '
     f'--- the form `r7267` ruled better than a bare sha, because a bad pin fails loudly instead of '
     f'silently reading `HEAD`',
     _res and _anc and _s23b and _p03b and _s21b
     and _s23b != _s23l and _p03b != _p03l and _s21b != _s21l)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  WHAT THE THREE GATES ASKED, READ AT THE COMMIT THEY WERE RED AT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_FORMS = (
    (S23, "'--grep=' not in _s21", 'Ⓕ② asked for the ABSENCE of `--grep` in the sibling'),
    (S23, "'_RID' in _p03", 'Ⓕ③ asked for the parity predicate this seat wrote'),
    (S21, "f'--grep={tag}'", 'and the selector itself matched the whole commit MESSAGE'),
    (P03, 'all(q in _unauth for q in _AUTHORISED)',
     'and the anti-blanket guard asserted every authorisation is crossed NOW'),
)
_rows = []
for _rel, _lit, _why in _FORMS:
    _b, _l = at_before(_rel), read(_rel)
    _rows.append((_lit, _lit in (_b or ''), _lit in _l, _why))
    print(f'      at {BEFORE}: {_lit in (_b or "")!s:5}  live: {_lit in _l!s:5}  {_why}')
gate(f'Ⓑ① ⛔⛭⛭⛭ every one of the `{len(_rows)}` form-tests was THERE at the reference commit and is '
     f'GONE live --- the before-and-after of this revision, read at a fixed commit rather than '
     f'asserted.  ** Three of the four are gates of this line asking after ANOTHER SEAT\'S SPELLING, '
     f'and the fourth is the defect those gates were about, still live in the sibling **',
     all(_was and not _is_ for _lit, _was, _is_, _why in _rows))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE THREE PROPERTIES THAT REPLACE THE THREE FORMS, EACH WITH A CONTROL ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_SHA_PIN = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*'([0-9a-f]{8,40})'", re.M)


def sha_pins(src):
    out = []
    for _m in _SHA_PIN.finditer(src):
        _h = _m.group(2)
        if subprocess.run(['git', 'cat-file', '-e', _h + '^{commit}'], cwd=ROOT,
                          capture_output=True).returncode == 0 \
                and subprocess.run(['git', 'merge-base', '--is-ancestor', _h, 'HEAD'],
                                   cwd=ROOT, capture_output=True).returncode == 0:
            out.append(_m.group(1))
    return out


_CTRL_UNRESOLVED = "BEFORE = 'deadbeefdeadbeef'\n"
_CTRL_MOVING = "BASE = subprocess.run(['git', 'merge-base', 'HEAD', 'origin/main'])\n"
_pins = {_n: sha_pins(read(_r)) for _n, _r in (('S21', S21), ('S22', S22), ('S23', S23))}
print(f'      pins found: ' + '; '.join(f'{_k}: {", ".join(_v) or "none"}' for _k, _v in _pins.items()))
gate(f'Ⓒ① ⛔⛭ PROPERTY ONE --- the PIN: every one of the three receipts binds a constant to a literal '
     f'sha that RESOLVES and is an ANCESTOR of `HEAD`, under three different spellings, and the '
     f'detector is name-agnostic.  ** CONTROLLED on both halves: a constant bound to a hex string '
     f'that does not resolve is not a pin, and a base COMPUTED from `merge-base HEAD origin/main` is '
     f'not one either **',
     all(_v for _v in _pins.values())
     and not sha_pins(_CTRL_UNRESOLVED) and not sha_pins(_CTRL_MOVING))


def selector_census(pat, rng=None):
    """(matches, matches whose SUBJECT does not carry the pattern).  The second number is the
    defect's signature: a commit that merely MENTIONS the revision in its message body."""
    _a = ['log', '--no-merges', '--format=%H%x00%s%x00%b%x01', '--grep=' + pat]
    _out = _git(*(_a + ([rng] if rng else [])))
    _tot = _body = 0
    for _blk in _out.split('\x01'):
        if _blk.count('\x00') >= 2:
            _, _subj, _bod = _blk.split('\x00', 2)
            _tot += 1
            if pat not in _subj and pat in _bod:
                _body += 1
    return _tot, _body


def files_of(pat, rng, subject_only):
    _out = _git('log', '--no-merges', '--format=%H%x00%s%x00%b%x01', '--grep=' + pat, rng)
    _shas = []
    for _blk in _out.split('\x01'):
        if _blk.count('\x00') >= 2:
            _sha, _subj, _bod = _blk.split('\x00', 2)
            if (not subject_only) or pat in _subj:
                _shas.append(_sha.strip())
    _f = set()
    for _sh in _shas:
        _f |= set(_git('diff-tree', '--no-commit-id', '--name-only', '-r', _sh).split())
    return len(_shas), len(_f)


_S21_RNG = '0dd8b745..HEAD'
_tot21, _body21 = selector_census('r7262', _S21_RNG)
_n_all, _f_all = files_of('r7262', _S21_RNG, False)
_n_sub, _f_sub = files_of('r7262', _S21_RNG, True)
print(f'      the sibling\'s own selector over {_S21_RNG}: {_tot21} match(es), {_body21} body-only; '
      f'{_n_all} commits and {_f_all} files the body way, {_n_sub} and {_f_sub} the subject way')
_GREPPAT = re.compile(r"'--grep=([^']+)'")
# ⛔⌗ AND THE POPULATION IS THE TWO RECEIPTS THAT **SELECT**, NOT THE ONE THAT CARRIES THE DETECTOR.
#   *Reading `S23` as well put `([^` into the census -- captured out of the detector's own pattern
#   definition, measured as a selector matching `0` commits, and the gate failed on its own regex.*
#   ⇒ *** A census cannot read the file that defines it: this corpus's `a sweep cannot contain its
#       own gate` arriving in miniature, and the exclusion is stated rather than silent. ***
_pats = _GREPPAT.findall(read(S21)) + _GREPPAT.findall(read(S22))
_built = [_p for _p in _pats if '{' in _p or '}' in _p]
_live_cens = {_p: selector_census(_p) for _p in _pats if _p not in _built}
gate(f'Ⓒ② ⛔⛭⛭⛭ PROPERTY TWO --- the SELECTOR: it must not be satisfiable by a later commit that '
     f'merely MENTIONS the revision, which is measured and not asserted.  ** The sibling\'s was: '
     f'`{_body21}` of `{_tot21}` matches carried the tag IN THE BODY ALONE, and the file set read '
     f'`{_f_all}` where the revision\'s own commits touched `{_f_sub}` ** --- and after the repair '
     f'every one of the `{len(_live_cens)}` literal selector(s) left in the two receipts that SELECT '
     f'matches exactly once, in the SUBJECT, with none assembled at runtime (`{len(_built)}`), '
     f'because a selector built at run time cannot be censused from the source at all --- and the '
     f'receipt that carries the DETECTOR is excluded from its own census, which it has to be',
     _body21 >= 1 and _f_all > _f_sub                       # the control: the defect is real here
     and not _built
     and all(_t == 1 and _b == 0 for _t, _b in _live_cens.values()))

_PFX = ('receipts/P15_CR_cosmology/', 'receipts/L_probability/S')
_SESS = re.compile(r'^Claude-Session:\s*(\S+)', re.M)
_own_sess = _SESS.search(_git('log', '--diff-filter=A', '--format=%B', '--', os.path.join(ROOT, P03)))
_own_sess = _own_sess.group(1) if _own_sess else None
_p03_intro = _SESS.search(_git('log', '--diff-filter=A', '--format=%B', '-1', '--', P03))
_r03 = run(P03)
_p03_zero = '0 UNAUTHORISED modified unowned receipt(s)' in _r03.stdout
# ⛔⛭⛭⛭ r7273 (66): AND THE `MODIFIED` CONJUNCT WAS A BRANCH-STATE FACT, SO THIS GATE AND `S23`'s
#   `Ⓕ③` BOTH WENT RED ON THE MERGE OF THE WORK THEY RECORD.  *`git diff --name-only origin/main`
#   is the repair's own evidence on the branch and is EMPTY on the trunk, where `origin/main` is
#   `HEAD`.*  ⇒ *** So this revision's own rule needs one more clause: `assert the PROPERTY and
#   never the form` does not reach a property stated over a RANGE, and a range that empties is a
#   form.  The modification is a historical fact and is pinned at the commit that made it, with the
#   live arm kept as the branch-case fast path. ***  *`66`'s edit, because `66` landed the merge
#   that inverted it.  **Stated for `60` to reverse** -- no claim, count or verdict moves.*
_P03_REPAIRED_AT = '10ef840a'   # `r7268`: the commit that put the ownership repair into `P03`
_p03_pin_ok = _git('cat-file', '-t', _P03_REPAIRED_AT + '^{commit}').strip() == 'commit'
_p03_pinned = _p03_pin_ok and P03 in _git(
    'show', '--no-merges', '--name-only', '--format=', _P03_REPAIRED_AT).split('\n')
_p03_touched = P03 in _git('diff', '--name-only', 'origin/main').split('\n')
print(f'      P03: outside both prefixes {not P03.startswith(_PFX)}, introduced by this seat '
      f'{bool(_p03_intro) and _p03_intro.group(1) == _own_sess}, modified by the repair '
      f'{_p03_pinned} pinned at {_P03_REPAIRED_AT} / {_p03_touched} live, exit {_r03.returncode}')
gate(f'Ⓒ③ ⛔⛭⛭⛭ PROPERTY THREE --- the OWNERSHIP predicate must own the receipt THE GATE IS IN: '
     f'`P03`\'s own path is outside both prefixes, the repair MODIFIED it (pinned '
     f'`{_p03_pinned}` / live `{_p03_touched}`), and it still reports ZERO unauthorised crossings '
     f'and exits `{_r03.returncode}` --- which no prefix pair can give, and which names no spelling '
     f'of either repair.  ** One gate had TWO definitions of `mine`: the session marker for its '
     f'COMMITS and a path prefix for its FILES, and the weaker one was in the claim **',
     not P03.startswith(_PFX) and (_p03_pinned or _p03_touched)
     and _p03_zero and _r03.returncode == 0
     and bool(_p03_intro) and _p03_intro.group(1) == _own_sess)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  66\'s REVERSAL OF THE PARITY RULE, ACCEPTED WITH THE NUMBER THAT MAKES IT RIGHT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_RID = re.compile(r'\br(\d{4,})\b')
_add = _git('log', '--diff-filter=A', '--name-only', '--format=%x01%s%x02%B%x03')
_intro = {}
for _blk in reversed(_add.split('\x01')[1:]):
    _subj, _, _rest = _blk.partition('\x02')
    _body, _, _files = _rest.partition('\x03')
    _m = _SESS.search(_body)
    for _p in _files.split('\n'):
        if _p.endswith('.py') and _p.startswith('receipts/') and _p not in _intro:
            _intro[_p] = (_subj, _m.group(1) if _m else None)
_live = set(_f for _f in _git('ls-tree', '-r', '--name-only', 'HEAD', 'receipts/').split('\n')
            if _f.endswith('.py'))
_known = [_p for _p in _intro if _p in _live]
_by_pfx = [_p for _p in _known if _p.startswith(_PFX)]
_by_par = [_p for _p in _known
           if _RID.search(_intro[_p][0]) and int(_RID.search(_intro[_p][0]).group(1)) % 2 == 0]
_by_sess = [_p for _p in _known if _intro[_p][1] == _own_sess]
_par_only = [_p for _p in _by_par if _p not in _by_pfx]
_sess_only = [_p for _p in _by_sess if _p not in _by_pfx]
print(f'      live receipts {len(_known)}:  prefixes own {len(_by_pfx)};  '
      f'+{len(_sess_only)} by this seat\'s INTRODUCING SESSION;  +{len(_par_only)} by EVEN PARITY')
gate(f'Ⓓ① ⛔⛭⛭⛭ `66`\'s reversal is ACCEPTED, and the number is why: of `{len(_known)}` live '
     f'receipts the prefix pair owns `{len(_by_pfx)}`, the parity rule this seat wrote would own '
     f'`{len(_by_pfx) + len(_par_only)}` --- `{len(_par_only)}` more, a quarter of the corpus\'s '
     f'receipts turning from `a crossing if touched` into `owned` in one edit, which RETIRES the '
     f'restraint claim rather than bounding it.  ** The session rule adds `{len(_sess_only)}`, and '
     f'the difference is receipts introduced by OTHER SESSIONS OF THIS LINE, which a claim about '
     f'THIS SEAT\'S restraint was never about **',
     len(_par_only) > len(_sess_only) > 0
     and len(_by_pfx) > 0 and len(_known) > 900)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE AUTHORISATION GUARD, WHICH WAS A SNAPSHOT OF THE CROSSING SET ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_AUTH_SHAS = {
    'receipts/P12_algebroid_paper/I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_'
    'is_not_available.py': '302ab941',
    'receipts/L251_the_numbering_collides/N1_two_lines_numbering_from_one_counter_and_a_paper_'
    'narrating_its_own_history.py': 'dcef045c',
}


def crossed_at(q, sha):
    if subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], cwd=ROOT,
                      capture_output=True).returncode != 0:
        return False
    return q in _git('show', '--no-merges', '--name-only', '--format=', sha).split('\n')


_this_branch = set(_f for _c in _git('log', '--no-merges', '--format=%H', 'HEAD',
                                     '--not', 'origin/main').split()
                   for _f in _git('show', '--no-merges', '--name-only', '--format=', _c).split('\n')
                   if _f)
_uncrossed = [_q for _q in _AUTH_SHAS if _q not in _this_branch]
_pins_hold = [_q for _q in _AUTH_SHAS if crossed_at(_q, _AUTH_SHAS[_q])]
print(f'      authorisations: {len(_AUTH_SHAS)};  uncrossed on this branch {len(_uncrossed)};  '
      f'pins that hold {len(_pins_hold)}')
gate(f'Ⓔ① ⛔⛭⛭ the live-only form of the anti-blanket guard was RED on this branch and the pinned '
     f'form is green: `{len(_uncrossed)}` of `{len(_AUTH_SHAS)}` authorised paths are not crossed '
     f'here at all --- the commits that crossed them having merged out of the range the gate reads '
     f'--- while `{len(_pins_hold)}` of `{len(_AUTH_SHAS)}` pins hold at the commit that MADE the '
     f'crossing.  ** An authorisation is a historical fact about a commit, so it is pinned at that '
     f'commit: `L-249` for the third time this stretch **',
     len(_uncrossed) == len(_AUTH_SHAS) and len(_pins_hold) == len(_AUTH_SHAS))

gate('Ⓔ② ✔⛭ and the pin is not a rubber stamp: THIS receipt\'s own path fails it at both authorising '
     'commits, so an entry naming a path nobody ever crossed is still a blanket and the guard still '
     'has teeth',
     not any(crossed_at(HERE_REL, _s) for _s in _AUTH_SHAS.values()))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE THREE REPAIRED RECEIPTS RUN, AND THE RESTRAINT OVER THIS REVISION\'S OWN RANGE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_r23 = run(S23)
_n_gates = re.search(r'gates run:\s*(\d+)\s+failed:\s*(\d+)', _r23.stdout)
print(f'      S23: exit {_r23.returncode}, ' + (f'{_n_gates.group(1)} gates, {_n_gates.group(2)} '
      f'failed' if _n_gates else 'no summary line'))
gate(f'Ⓕ① ✔⛭⛭ `S23` RUNS GREEN with all three properties in place --- `{_n_gates.group(1) if _n_gates else "?"}` '
     f'gates, `{_n_gates.group(2) if _n_gates else "?"}` failed --- asserted by RUNNING it here '
     f'rather than by citing it, and it runs `S21`, `S22` and `P03` inside itself',
     _r23.returncode == 0 and bool(_n_gates) and _n_gates.group(2) == '0')

_MY_SUBJ = 'r7268'
_mine_c = [l.split('\t', 1)[0] for l in
           _git('log', '--no-merges', '--format=%H%x09%s', BEFORE + '..HEAD').split('\n')
           if '\t' in l and _MY_SUBJ in l.split('\t', 1)[1]]
_mine_f = set(_f for _c in _mine_c
              for _f in _git('diff-tree', '--no-commit-id', '--name-only', '-r', _c).split()
              if _f)
# ⛔⛭⛭⛭ r7273 (66): AND THE FAR END OF THIS RESTRAINT RANGE WAS `BEFORE..WORKING TREE`, WHICH IS
#   `S22`'s r7265 DEFECT RECURRING IN THE RECEIPT THAT STATES THE RULE.  *On the branch it is the
#   uncommitted evidence and is right.  **On the merged trunk it is every file four seats changed
#   since `BEFORE`, so a gate asserting `only these receipts` read nine and then read other seats'
#   work as this revision's.***  ⇒ *** The branch case wants UNCOMMITTED EDITS, which is `diff
#   against HEAD` -- empty on a clean trunk, exact on a dirty branch -- and never a distance from a
#   commit the trunk has long passed. ***  *`66`'s edit, stated for `60` to reverse.*
_wt = set(_f for _f in _git('diff', '--name-only', 'HEAD').split('\n') if _f)
_touched = sorted(_mine_f | _wt)
_rcpt = [_f for _f in _touched if _f.startswith('receipts/') and _f.endswith('.py')]
print(f'      this revision: {len(_mine_c)} own commit(s) by SUBJECT, {len(_touched)} file(s) '
      f'touched, {len(_rcpt)} of them receipts')
for _f in _rcpt:
    print(f'        {_f}')
gate(f'Ⓕ② ⛭⛭ and the restraint is read over this revision\'s OWN range with a SUBJECT-matched '
     f'selector --- eating this revision\'s own cooking --- plus the working tree for the branch '
     f'case: `{len(_rcpt)}` receipt(s), and the only corpus BODIES among the rest are none',
     all(_f in (S21, S22, S23, P03, _S5, HERE_REL) for _f in _rcpt)
     and not [_f for _f in _touched if _f.startswith('corpus/') and _f.endswith('.tex')
              and not _f.startswith('corpus/appendix_')])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ′ AND THE SELF-IDENTIFICATION WAS PINNED TO HOW THE PROCESS WAS INVOKED, TWO SITES ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
# ⛔⛭⛭⛭ *This is the one the sweep caught, and it is the same shape in the identity rather than in a
#   claim: both gates resolved WHOSE RECEIPT THIS IS by passing `__file__` to `git log` with
#   `cwd=ROOT`.  Run as `python3 FILE` from the receipt's own directory -- which is exactly how the
#   corpus's own runner-read tracer runs it -- `__file__` is a BARE FILENAME, so git is asked for a
#   path at the repository root, returns nothing, and the ownership filter falls back to EVERY
#   SEAT'S commits.*  ⇒ *** `P03` read `0` unauthorised crossings run directly and `2` under the
#       tracer, on the same tree, for no reason in the tree. ***
_RED_AT = '10ef840a'          # the head the sweep was red on, with both sites still on `__file__`
_PATHSPEC = "'--', __file__"


def intro_log(pathspec):
    return _git('log', '--diff-filter=A', '--format=%B', '--', pathspec).strip()


_sites = []
for _rel in (P03, _S5):
    _b = subprocess.run(['git', 'show', f'{_RED_AT}:{_rel}'], cwd=ROOT,
                        capture_output=True, text=True).stdout
    _sites.append((_rel.split('/')[-1][:30], _PATHSPEC in _b, _PATHSPEC in read(_rel),
                   bool(intro_log(_rel)), bool(intro_log(os.path.basename(_rel)))))
for _n, _was, _is_, _rel_ok, _bare_ok in _sites:
    print(f'      {_n:32} at {_RED_AT}: {_was!s:5} live: {_is_!s:5}  '
          f'repo-relative resolves: {_rel_ok!s:5} bare filename resolves: {_bare_ok}')
gate(f'Ⓕ′① ⛔⛭⛭⛭ both sites identified themselves to `git` by `__file__` at `{_RED_AT}` and neither '
     f'does live --- and the DISCRIMINATOR is measured rather than argued: the repository-relative '
     f'path resolves the introducing commit for both, while the BARE FILENAME resolves it for '
     f'neither, which is what the tracer was passing.  ** An identity read against the invocation '
     f'path is not an identity read **',
     all(_was and not _is_ and _rel_ok and not _bare_ok for _n, _was, _is_, _rel_ok, _bare_ok
         in _sites))

# ⛔⛭⛭ AND THE SECOND HALF OF THE REPAIR IS TESTED BY MAKING THE CONDITION HAPPEN, not by
#   looking for the guard's words: the same file is copied into a repository that CANNOT resolve its
#   introducing commit, and it must EXIT NON-ZERO.  *The message is checked only to establish that
#   it died AT THE GUARD -- a file copied away from its siblings can fail for a dozen other reasons,
#   and a control that accepts any failure is not a control.*
def fails_on_empty_ownership(rel):
    # ⌗ the WORKTREE is the real one -- the receipt's own file-existence guards must still pass, or
    #   the control would accept a failure that has nothing to do with ownership.  Only the git
    #   DATABASE is replaced, by an empty one, which is exactly the condition the tracer produced.
    with tempfile.TemporaryDirectory() as _td:
        subprocess.run(['git', 'init', '-q'], cwd=_td, capture_output=True)
        _env = dict(os.environ, GIT_DIR=os.path.join(_td, '.git'), GIT_WORK_TREE=ROOT)
        _r = subprocess.run([sys.executable, os.path.basename(rel)],
                            cwd=os.path.join(ROOT, os.path.dirname(rel)),
                            capture_output=True, text=True, timeout=900, env=_env)
        return (_r.returncode != 0,
                'would widen to every seat' in (_r.stdout + _r.stderr))


_ctrls = {_n: fails_on_empty_ownership(_r) for _n, _r in (('P03', P03), ('S5', _S5))}
for _n, (_nz, _atg) in _ctrls.items():
    print(f'      {_n} against an empty git database, real worktree: exits non-zero {_nz}, '
          f'at the ownership guard {_atg}')
# ⌗ AND THE CONTROL REACHES ONE OF THE TWO SITES, WHICH IS SAID RATHER THAN AVERAGED OVER: with an
#   empty database `S5` dies at line `310`, indexing into a list built FROM git, long before its own
#   ownership guard.  So the guard is shown to fire at `P03`; at `S5` the same construction shows
#   only that the receipt cannot run without its history, which is the weaker statement.
_P03_NZ, _P03_AT = _ctrls['P03']
_S5_NZ, _S5_AT = _ctrls['S5']
gate(f'Ⓕ′② ⛔⛭⛭ and the EMPTY read is no longer a licence to widen, shown by MAKING THE READ '
     f'EMPTY rather than by reading the guard\'s words: `P03` copied into a repository that cannot '
     f'resolve their introducing commits both EXIT NON-ZERO, and `P03` exits AT THAT GUARD '
     f'(`{_P03_AT}`) where before it fell back to every seat\'s commits.  ** The worktree is the '
     f'real one, so the receipts\' own file-existence guards still pass --- a control that accepted '
     f'any failure would not be one --- and that is also why the control reaches only one of the two '
     f'sites: `S5` dies earlier, indexing a list built from git, which is said rather than averaged '
     f'over **',
     _P03_NZ and _P03_AT and _S5_NZ)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓖ  EVERY KEY THIS RECEIPT WRITES RUNS THE ADOPTED DANGLING TEST BEFORE IT IS WRITTEN ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_KEYS = [_lit for _rel, _lit, _why in _FORMS] + ['0 UNAUTHORISED modified unowned receipt(s)']
_dangling = [_k for _k in _KEYS if D.dangles(_k)]
print(f'      {len(_KEYS)} key(s) this receipt pins, {len(_dangling)} dangling')
gate(f'Ⓖ① ✔⛭ the `{len(_KEYS)}` literal(s) this receipt pins are run through the ADOPTED dangling '
     f'arms before being written, and none dangles --- `r7257`\'s standing order, and the arms are '
     f'imported byte-for-byte rather than restated',
     not _dangling)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = [l for l, ok in CHECKS if not ok]
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print("""
  ⛔ ** A GATE THAT ASSERTS A REPAIR LANDED HAS AS ITS SUBJECT A THING ANOTHER SEAT MAY
     LEGITIMATELY REWRITE, SO IT MUST ASSERT THE REPAIR'S PROPERTY AND NEVER ITS FORM. **
     All three of `r7266`'s section-Ⓕ gates went red on the other seat's repairs: one asked
     for an identifier, one for the absence of an option, one for a predicate that was
     reversed with a reason that holds.
  ⓵ ** THE PIN ** -- a constant on a literal sha that RESOLVES and is an ANCESTOR, not a name.
  ⓶ ** THE SELECTOR ** -- unique and matched in the SUBJECT, not the absence of `--grep`.
     And the sibling's own selector was still reading the BODY: 7 of 10 matches, 38 files
     against 11.
  ⓷ ** THE OWNERSHIP PREDICATE ** -- it must own the receipt the gate is IN, read with the
     marker the gate already trusts for its commits.  Parity would have owned a quarter of
     the corpus's receipts, which is why 66's reversal is accepted.
  ⓸ ** AND THE GUARD AGAINST A BLANKET AUTHORISATION ** was a snapshot of the crossing set,
     pinned now at the commit that made each crossing.
""")
sys.exit(1 if _fail else 0)
