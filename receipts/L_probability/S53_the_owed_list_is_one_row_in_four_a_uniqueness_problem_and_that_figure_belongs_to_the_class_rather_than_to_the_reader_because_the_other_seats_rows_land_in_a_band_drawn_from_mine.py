#!/usr/bin/env python3
"""S53 -- THE WHOLE OWED LIST, MEASURED: `23` of `83` owed rows are uniqueness problems -- about one
in four -- ** and all three registered arms land INSIDE their bands, which is the first revision of
this phase where every arm does. ** ⛭⛭⛭ *** AND THE DECISIVE ONE IS THE SAMPLING TEST: the rows the
OTHER reader filed come in inside a band drawn from THIS seat's own blocks, so the figure belongs to
the CLASS and not to the noticing. ***

** WHY A MEASUREMENT AND NOT A REPAIR. **  `r7360` closed the last block this seat can take.  Of the
`83` owed rows that remain, `74` carry `69`'s reading, three `70.1`'s and four `cc66`'s, and the last
two are this seat's own and routed.  ** Not one is takeable without reaching into another seat's
reading, and partitioning that is `66`'s to do. **  *The other open frontier row is blocked on a
SAMPLE rather than on work.*  ⇒ So the one piece of this phase left that collides with nobody is to
READ the population, and this revision edits no receipt of anyone's.

** Ⓐ THE QUESTION, ASKED TWICE AND ANSWERED THREE TIMES BADLY. **  `r7351` ③ asked whether the owed
list is a uniqueness backlog.
      `cc66`   `0` of `7`    -- no uniqueness backlog at all
      this seat `17` of `30`  -- plainly one   ⛔ *withdrawn at `r7358`: it was counting the ledger*
      refined   `0.167`, `0.263`, `0.286` on three blocks -- *every one a block THIS SEAT repaired*
  ⇒ ** A share measured on the rows one seat noticed may be a fact about the noticing, and no number
    of this seat's own blocks can tell the difference. **

** Ⓑ ARM ⒜ -- `23` OF `83` = `0.277`.  ⛭ INSIDE THE BAND. **  Central `0.24` (this seat's three
readings pooled by row count), band `0.17`-`0.31`, two-sided, decisive `0.157`.
  ⇒ ** About one owed row in four.  Neither "mainly" nor "not at all" -- and the first corpus-wide
    figure for the quantity rather than a block's. **

** Ⓒ ARM ⒝ -- THE SAMPLING TEST: `17` OF THE `74` ROWS `69` FILED = `0.230`.  ⛭⛭ INSIDE A BAND DRAWN
FROM THIS SEAT'S OWN BLOCKS. **  Central `0.24`, band `0.16`-`0.32`, decisive `0.102`.
  ⇒⇒ *** SO THE PROPORTION IS A PROPERTY OF THE CLASS AND NOT OF THE READER: two seats reading
      independently, with different habits and different prefixes, find the same share. ***
  ⇒ ** Which licenses the pooling the three block readings could not justify on their own ** -- *and
    the arm was registered to TEST that rather than to assume it, with the opposite outcome named in
    advance as equally a result.*

** Ⓓ ARM ⒞ -- `31` OF `83` = `0.373` INVISIBLE TO THE REFINED ARBITER.  ⛭ INSIDE THE BAND. **  Central
`0.35`, band `0.27`-`0.43`, decisive `0.134`.
  ⌗ ** And the price falls on ONE TARGET, not on both: ** `31` of the `48` `SOURCE` rows are unseen
  and `0` of the `35` `PAPER` rows are.  *Excluding the ledgers costs the arbiter its sight of pins
  into `scripts/`, the root registers and live instruments, and costs it nothing on the papers.*

** ⛭⛭⛭ Ⓔ AND THE STRUCTURE UNDER THE SHARE IS SHARPER THAN THE SHARE, WHICH NO ARM REGISTERED. **

      TOKEN     `18` of `34`  = `0.529`
      SENTENCE  ` 5` of `49`  = `0.102`

  ⇒⇒ *** UNIQUENESS FAILURE IS A TOKEN PHENOMENON, FIVE-FOLD OVER.  The owed list is not "a
      uniqueness backlog" -- it is a TOKEN backlog, and non-uniqueness is what a token pin LOOKS
      LIKE from the arbiter's side. ***
  ⌗ *That is the same KIND of identity `r7356` claimed between two of its arms and `r7358` withdrew
  for counting the ledger.*  ** Arriving here on the population instead of on a block, between
  different quantities, and holding. **
  ⚠ One literal occurs `9,647` times in a single file.  *It is the word `no`.*

** COMPUTES: ** the owed population at a pinned commit, by reader, target and tier; the refined
arbiter over all of it and over the other reader's rows alone; both against their registered bands
with their decisive fractions; the blind count split by target; the token-against-sentence split; and
the effort, reported.  No paper quantity, and no repair.

** WHAT IS NOT CLAIMED. **  ** Not that `0.277` is the share of the owed list in general ** -- it is
the share of what REMAINS owed after four revisions of repair, and the repaired rows are gone from
it.  ** Not that the two readers agree on WHICH rows are owed ** -- only that the uniqueness share
among them matches; the populations are disjoint by construction.  ** Not that the token split is
causal ** -- a token pin is short, and shortness and non-uniqueness are the same property seen twice,
which is why it is reported as structure rather than as a mechanism.  ** And not that any row here is
repaired **: every one belongs to another seat's reading and this file touches none of them.

Written r7362.  Stated for reversal.
"""
import collections
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
COST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7362_60_the_whole_owed_list',
                    'cost.py')
REG = '4f0308a6'                 # the registration commit, pushed before the measurement


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  S53 -- the whole owed list, and whose property the share is')
    print()
    spec = importlib.util.spec_from_file_location('r7362_cost', COST)
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    R, S = C.RESULT, C.scored()

    # ── Ⓐ the population, read where it stood ────────────────────────────────────────────────────
    rows = C.owed()
    reader = collections.Counter(C.reader_of(r) for r in rows)
    check(f'Ⓐ① the owed list at the pinned census {C.CENSUS}: {len(rows)} rows in '
          f'{len({r[0] for r in rows})} receipts over {len({r[0].split("/")[1] for r in rows})} '
          f'prefixes, read THERE and not live',
          len(rows) == R['A_ROWS'] == 83 and len({r[0] for r in rows}) == 24)
    check(f'Ⓐ② and by the seat that READ each row: {dict(reader)} -- so {reader["69"]} of the '
          f'{len(rows)} are another seat\'s reading and {reader[C.SEAT]} are this seat\'s, both of '
          f'them routed',
          dict(reader) == R['BY_READER'] and reader[C.SEAT] == 2 and reader['69'] == 74)
    #: ⛔ the restraint: this revision edits NO receipt, which is what makes it takeable without a
    #: ruling.  Shown over its own commits rather than asserted.
    # ⛔⛭⛭⛭ r7364+60: AND IT WAS MEASURED OVER `CENSUS..HEAD`, SO THE NEXT REVISION'S LEGITIMATE WORK
    #   BROKE IT.  *`r7364` repaired seven receipts -- six of them red, one of them this clause -- and
    #   every one lands after `r7362`'s census, so this gate read them as `r7362` having touched six
    #   receipts it did not touch.  **The claim was true and the range it was asserted over keeps
    #   growing**, which is this phase's own class in its eighth face and the first time it has been
    #   found in a RESTRAINT rather than in a measurement.*
    #   ⇒ *** The range is now THIS REVISION'S OWN COMMITS, found by the revision id in the subject
    #     the way `S50`'s `Ⓗ①` finds them, so a later revision's work cannot enter it. ***
    #   ⌗ *And the working-tree term goes with it.  It was added at `r7362` so the claim would hold
    #     before this file's own commit as well as after -- correct then, and once the revision is
    #     landed it is a term that ANY later edit of ANY receipt satisfies.  A restraint about a
    #     landed revision is a fact about its commits and nothing else.*
    #   ⛔⛭⛭⛭ r7370: ** AND THE REPAIR ABOVE WAS THE SAME DEFECT ONE SPELLING ON. **  *Finding the
    #     revision's commits "by the revision id in the subject" selects every commit WHOSE SUBJECT
    #     NAMES IT, and the corpus's convention is to cite revisions by number.  `S29` carried the
    #     identical form and went red when another seat's commit cited `r7290` and touched two
    #     receipts; this one is not broken yet only because no later subject has named `r7362`.*
    #     ⇒ *** `r7364`'s note above -- "a later revision's work cannot enter it" -- is false as
    #         written: a later revision WRITING ABOUT this one enters it.  The commits are PINNED,
    #         and the id match is kept as the CONTROL beside them. ***
    OWN_C = ('c6fe446c', '4f0308a6')      # this revision's own two commits, pinned
    _own_c = [c for c in OWN_C if git('cat-file', '-t', c).strip() == 'commit']
    assert len(_own_c) == len(OWN_C), f'{OWN_C} do not all resolve in this clone'
    _matched_c = [l.split()[0] for l in
                  git('log', '--no-merges', '--format=%H %s', f'{C.CENSUS}..HEAD').split('\n')
                  if l.strip() and 'r7362' in l]
    print(f'      the pinned commits: {len(_own_c)};  what the id match in the subject returns: '
          f'{len(_matched_c)} -- REPORTED, and the control in the clause')
    _touched = {f for c in _own_c
                for f in git('show', '--no-merges', '--name-only', '--format=', c).split()
                if f.startswith('receipts/') and f.endswith('.py')}
    _others = sorted(f for f in _touched if 'L_probability/S53' not in f)
    check(f'Ⓐ③ ⛭ and the RESTRAINT is shown rather than promised: over this revision\'s OWN '
          f'{len(_own_c)} commit(s), {len(_touched)} receipt(s) differ and '
          f'{len(_others)} of them is anyone else\'s -- no row of any seat\'s reading is touched '
          f'{_others or ""}.  ⛭ r7364: *read from the commits whose subject names this revision '
          f'rather than from `CENSUS..HEAD`, because the next revision\'s repairs land in that '
          f'range and were being counted as this one\'s*',
          not _others and len(_touched) == 1 and len(_own_c) >= 1
          # ⛭⛭⛭ r7370: and the id match is the control -- it must still return at least the
          # pinned pair, so the pin cannot quietly become the match again.
          and all(any(m.startswith(c) for m in _matched_c) for c in _own_c))

    # ── Ⓑ arm ⒜ ──────────────────────────────────────────────────────────────────────────────────
    texts = C._corpus_texts(C.CENSUS)
    u = C.uniqueness(rows, texts)
    multi = [k for k, v in u.items() if v > 1]
    blind = [k for k, v in u.items() if v == 0]
    share = len(multi) / len(rows)
    check(f'Ⓑ① arm ⒜: {len(multi)} of {len(rows)} owed literals occur MORE THAN ONCE in a single '
          f'file of the text they are pinned into, ledgers excluded -- {share:.3f}, against central '
          f'{C.A_CENTRAL} and band {C.A_BAND[0]}-{C.A_BAND[1]}, decisive {S["a"][3]:.3f}',
          len(multi) == R['A_MULTI'] == 23 and abs(share - 0.277) < 0.001)
    check('Ⓑ② ⛭ INSIDE THE BAND -- about one owed row in four, and the first corpus-wide figure for '
          'the quantity rather than a block\'s',
          S['a'][2] is True and C.A_BAND[0] <= share <= C.A_BAND[1])

    # ── Ⓒ arm ⒝, the sampling test ───────────────────────────────────────────────────────────────
    other = [r for r in rows if C.reader_of(r) == '69']
    uo = {k: v for k, v in u.items() if k in {(r[0], r[1]) for r in other}}
    mo = [k for k, v in uo.items() if v > 1]
    so = len(mo) / len(other)
    check(f'Ⓒ① arm ⒝, THE SAMPLING TEST: on the {len(other)} rows the OTHER reader filed the share '
          f'is {len(mo)} of {len(other)} = {so:.3f}, against the band {C.B_BAND[0]}-{C.B_BAND[1]} '
          f'drawn from THIS seat\'s own blocks, decisive {S["b"][3]:.3f}',
          len(mo) == R['B_MULTI'] == 17 and len(other) == R['B_ROWS'] == 74)
    check('Ⓒ② ⛭⛭ INSIDE IT -- so the proportion is a property of the CLASS and not of the reader: '
          'two seats reading independently, with different habits and disjoint prefixes, find the '
          'same share',
          S['b'][2] is True and C.B_BAND[0] <= so <= C.B_BAND[1])
    check('Ⓒ③ ⇒ which LICENSES the pooling the three block readings could not justify alone -- and '
          'the arm was registered to TEST that, with the opposite outcome named in advance as '
          'equally a result',
          C.B_CENTRAL == C.A_CENTRAL
          and abs(so - share) < (C.B_BAND[1] - C.B_BAND[0]))
    #: ⌗ and the two populations are DISJOINT, so the agreement is not two readings of one set.
    _mine_rows = {(r[0], r[1]) for r in rows if C.reader_of(r) == C.SEAT}
    check(f'Ⓒ④ ⌗ and the two populations are DISJOINT by construction ({len(_mine_rows)} rows this '
          f'seat read, {len(other)} the other did, no row in both), so the agreement is two readings '
          f'of two sets and not two readings of one',
          not (_mine_rows & {(r[0], r[1]) for r in other}))

    # ── Ⓓ arm ⒞, the blind share ─────────────────────────────────────────────────────────────────
    bs = len(blind) / len(rows)
    _bl_src = [k for k in blind if next(r for r in rows if (r[0], r[1]) == k)[2] == 'SOURCE']
    _bl_pap = [k for k in blind if next(r for r in rows if (r[0], r[1]) == k)[2] == 'PAPER']
    check(f'Ⓓ① arm ⒞: {len(blind)} of {len(rows)} = {bs:.3f} occur nowhere in the text set the '
          f'refined arbiter reads -- every `.tex`, `.md`, `.tsv` and `.txt` under `corpus/` scanned '
          f'in full, the ledgers excluded -- against band {C.C_BAND[0]}-{C.C_BAND[1]}, decisive '
          f'{S["c"][3]:.3f}',
          len(blind) == R['C_BLIND'] == 31 and S['c'][2] is True)
    check(f'Ⓓ② ⌗ and the price falls on ONE TARGET: {len(_bl_src)} of the SOURCE rows are unseen and '
          f'{len(_bl_pap)} of the PAPER rows are -- the refinement costs the arbiter its sight of '
          f'pins into scripts, the root registers and live instruments, and costs it nothing on the '
          f'papers',
          len(_bl_src) == R['C_BLIND_SOURCE'] == 31 and len(_bl_pap) == R['C_BLIND_PAPER'] == 0)

    # ── Ⓔ the structure no arm registered ────────────────────────────────────────────────────────
    tok = [r for r in rows if r[3] == 'TOKEN']
    sen = [r for r in rows if r[3] == 'SENTENCE']
    tm = [r for r in tok if u[(r[0], r[1])] > 1]
    sm = [r for r in sen if u[(r[0], r[1])] > 1]
    check(f'Ⓔ① ⛭⛭ AND THE STRUCTURE UNDER THE SHARE: uniqueness failure is a TOKEN phenomenon, '
          f'{len(tm)} of {len(tok)} = {len(tm)/len(tok):.3f} against {len(sm)} of {len(sen)} = '
          f'{len(sm)/len(sen):.3f} on sentences -- five-fold',
          len(tm) == R['TOKEN_MULTI'] == 18 and len(sm) == R['SENTENCE_MULTI'] == 5
          and (len(tm)/len(tok)) > 4 * (len(sm)/len(sen)))
    check('Ⓔ② ⇒ so the owed list is not "a uniqueness backlog" -- it is a TOKEN backlog, and '
          'non-uniqueness is what a token pin looks like from the arbiter\'s side.  *Reported as '
          'STRUCTURE and not as a mechanism: a token pin is short, and shortness and non-uniqueness '
          'are one property seen twice*',
          len(tok) == R['TOKEN_ROWS'] == 34 and len(sen) == R['SENTENCE_ROWS'] == 49)
    _seen = [k for k, v in u.items() if v > 0]
    check(f'Ⓔ③ and over what the arbiter can SEE the share is {len(multi)} of {len(_seen)} = '
          f'{len(multi)/len(_seen):.3f}, which is the upper bound on arm ⒜ and is stated beside it '
          f'rather than instead of it',
          len(_seen) == R['SEEN_ROWS'] == 52 and len(multi) == R['SEEN_MULTI'] == 23)
    check(f'Ⓔ④ ⚠ and the worst single literal occurs {max(u.values()):,} times in one file: '
          f'{json.dumps(sorted(u.items(), key=lambda kv: -kv[1])[0][0][1])}',
          max(u.values()) == R['MAX_OCCURRENCES'] == 9647)

    # ── Ⓕ the registration came first, shown from the record ─────────────────────────────────────
    check(f'Ⓕ① the registration was committed and PUSHED before the measurement: {REG} contains '
          f'the bands and no result block, and the result block arrives in a later commit',
          'RESULT.update' not in git('show', f'{REG}:computations/beyond_the_wall/'
                                     'r7362_60_the_whole_owed_list/cost.py')
          and 'A_BAND = (0.17, 0.31)' in git('show', f'{REG}:computations/beyond_the_wall/'
                                             'r7362_60_the_whole_owed_list/cost.py'))
    check('Ⓕ② and all three decisive fractions are above 0.10, so each arm could have failed',
          all(S[k][3] > 0.10 for k in ('a', 'b', 'c')))

    print()
    print('=' * 78)
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for m in FAILED:
            print(f'    - {m}')
        return 1
    print('  ⇒ ** ALL CHECKS PASS. **')
    print('  ⛭⛭ ** ALL THREE ARMS LAND INSIDE THEIR BANDS -- the first revision of this phase where')
    print('     every arm does, and the bands were drawn before the reading. **')
    print('  ⛭⛭⛭ ** THE OWED LIST IS ONE ROW IN FOUR A UNIQUENESS PROBLEM (23 of 83 = 0.277), AND')
    print('     THE FIGURE BELONGS TO THE CLASS RATHER THAN TO THE READER: the 74 rows the other')
    print('     seat filed come in at 0.230, inside a band drawn from this seat\'s own blocks. **')
    print('  ⛭ ** AND THE STRUCTURE IS SHARPER THAN THE SHARE: uniqueness failure is a TOKEN')
    print('     phenomenon five-fold over, 0.529 against 0.102.  The owed list is a TOKEN backlog. **')
    return 0


if __name__ == '__main__':
    sys.exit(main())
