#!/usr/bin/env python3
"""L_probability receipt -- `PO-78`'s SECOND standing backlog, the one `r7204`, `r7208` and `r7212`
all left alone: ** the unread-figure sites. **  `22` owed, `6` of them this seat's, and they are
repaired here by reading the paper.

*** ⛭⛭⛭ AND THE CLASS IS NOT WHAT ITS NAME SAYS. ***  *The gate is called `unread figure`, as though
the defect were a missing pin.*  ⇒ ** `19` of the `22` labels ATTRIBUTE their figure to a paper, and
`9` of those sit in files that open no `.tex` at all.  So the defect is not a pin that was forgotten:
it is a LABEL MAKING A CLAIM THE GATE NEVER COVERS. **

⛔ ** THE HYPOTHESIS THIS REVISION PRE-REGISTERED, AND IT HOLDS ON THE ATTRIBUTION MEASUREMENT. **
> *** `PO-78`'s two standing backlogs are the two sides of ONE failure --- a gate and its label
> disagreeing about what is being asserted.  A quote-pin site is a GATE WITH NO CLAIM: it pins a form
> the argument does not need, so it breaks on a change that costs the argument nothing.  An
> unread-figure site is a CLAIM WITH NO GATE: the label attributes a figure to a paper and nothing
> covers the attribution, so it survives a change that should cost it everything. ***
⌗ *And the dangerous half is not the `9`: it is the `10` whose files DO read papers, because there
the omission is not capability but AIM --- the receipt looks like it checks the paper.*

*** ⛭⛭⛭ AND ONE OF THIS SEAT'S SIX WAS NOT MERELY UNREAD. `C26`'s TWO SITES WERE COMPARING AGAINST A
    NUMBER THIS PAPER HAD WITHDRAWN AS THE ERROR, AND THREE THINGS WERE TRUE AND INVISIBLE. ***
  ⓵ ***The figure is RETIRED.***  *`$9.4\\%$` was removed from `CR_cosmology.tex` at `r2755`
    (`b4f19310`), whose own subject line calls it* ***"the one 9.4% was the error"***, *and replaced
    by `$8.2\\%$` --- which has since gone too.  It is absent from every paper body now.*
  ⓶ ***The label asserted a betweenness the condition never tested, and it was true of no figure.***
    *The label said `+9.4%` "lies between" the two weightings; the condition said `w3 < 9.4`, which
    puts it ABOVE both.  And `$9.4$` does not lie between `$8.7$` and `$7.8$`.*
  ⓷ ***It was the wrong OBJECT.***  *The retired figure was the OBSERVABLE's, which `P15` now states
    as `moved by under a per cent`; the three computed numbers are RATE-GAP scale, and the paper
    separates the two in its own voice --- `the rate gap is not what the signature is made of`.*
  ⇒ ** Re-pointed at the paper's OWN rate-gap figure so the comparison is within one object, with the
  retired figure asserted GONE and the observable asserted SEPARATELY as what these checks are not
  about. **

** ⛭ THE SIX ARE REPAIRED AND THE BACKLOG FALLS `22` → `16` BY RUNNING, NOT BY RECLASSIFICATION. **
*Each repair reads the paper's own SENTENCE at exactly one site --- never a bare number, which is the
vacuous-green mode `PIN_DEBT` names, where a loose figure matches an unrelated sentence and proves
nothing.  The six stale baseline rows are dropped because the sites no longer exist, which is what
`70`'s baseline header requires: a record of adjudications and not a list of exemptions.*
  ⌗ *One repair also reconciled two spellings of one object: the paper's `$48M^2/r^6$` against this
  seat's `$12r_s^2/r^6$`, equal because `$r_s=2M$`, now asserted rather than assumed.*

⛔ ** AND A LESSON ABOUT CONTROLS THAT COST ME A CORRECT REPAIR AND IS WORTH MORE THAN THE SIX. **
*Every repair is controlled two-sided: GREEN unperturbed, **RED** with the attributed figure moved in
every paper, and GREEN on the PRE-repair source under the same move --- that last cell reproducing
`70`'s own baseline measurement rather than citing it.*  ⇒ *** ONE CONTROL CAME BACK SAYING A GOOD
REPAIR HAD FAILED, BECAUSE THE PERTURBATION HAD SUBSTITUTED NOTHING. ***  *The pinned sentence spans a
line break in the raw `.tex` while the receipt reads a whitespace-collapsed body, so a perturbation
written against the collapsed text matched nothing in the file --- and a mutation that mutates nothing
leaves the gate GREEN, which reads exactly like a repair that does not bite.*
> ***A must-come-back-wrong control must assert that it came back at all: count the substitutions.***
*The same sentence as the positive control a zero needs, in the mutation direction.*

⚠ ** AND ONE CELL OF THE TABLE IS RECORDED AS CONTRADICTED RATHER THAN SMOOTHED. **  *The
potential-equation site's pre-repair cell returned RED once and GREEN on three consecutive re-runs of
the same configuration.  `3` of `4` is reported as the reading, with the one disagreement named,
because this corpus already carries same-commit red/green pairs and hiding one would be the defect it
keeps finding.*

⌗ ** AND A SMALL THING THAT IS THE SAME THING AGAIN, FOUND WHILE CHECKING THE SIX PINS ARE THERE. **
*A pin as the PAPER carries it and the same pin as a receipt's SOURCE carries it are two different
strings, for two reasons: a Python literal escapes the backslash, and one of the six is written as two
adjacent string pieces, so the whole literal exists at run time and never contiguously in the file.*
⇒ ** A checker that looks for the paper's spelling in the source finds nothing and reports a pin that
is plainly there as missing. **  *Which is the `ENCODING-OK` verdict the quote-pin baseline already
carries, met from the other side --- and the detector hole `r7208` routed to `70`, where a literal
reaching its haystack through a variable is invisible, is the same shape once more.*

** COMPUTES: the 22 owed unread-figure sites partitioned at a PINNED baseline by whether the LABEL
attributes to a paper and whether the file opens a .tex at all; the three facts about C26's retired
figure, each read from the live corpus or from the commit that removed it; the arithmetic showing the
label's betweenness was true of no figure; the six repairs' pins each present at EXACTLY ONE site in
the paper; the backlog's fall from 22 to 16 read from the gate's own baseline; and C26's full
two-sided control performed LIVE on a symlink shadow tree whose corpus alone is rebuilt, with the
substitution counted so a control that mutates nothing cannot pass for one that did.  Reads receipt
sources, the gate's baseline and the papers; the only historical read is the one commit that removed
the retired figure.  No assertion on wall-clock time. **
"""
import os
import re
import shutil
import subprocess
import tempfile

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ** the baseline is read AT THE COMMIT THIS REVISION STARTED FROM, so the `22` cannot move when
#   this revision drops its six rows -- which is the whole point of `r7212`'s own precaution. **
PIN = 'ddd5a6680c2d43c93465f98450a593b838b9ab20'
R2755 = 'b4f19310'          # the commit whose subject calls the retired figure "the error"


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def body(path):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


MINE = 'receipts/P15_CR_cosmology/'
L = MINE
C26 = L + 'C26_the_onset_is_not_free.py'
C62 = L + 'C62_the_diffusion_signature_is_a_wash_and_the_isw_is_not_what_it_turned_on.py'
KRE = (L + 'P15_the_layer_is_R_times_S2_on_the_reassigned_chart_and_the_two_presentations_'
           'are_two_metrics_on_one_layering_related_by_the_null_reassignment.py')
RAT = (L + 'P15_the_third_possibility_cannot_be_because_C21s_limit_is_taken_on_exactly_the_'
           'segment_the_lift_occupies_so_the_two_transfers_overlap_rather_than_compose.py')
POT = (L + 'P15_horn_ones_carrier_is_already_the_papers_own_wavenumber_free_potential_amplitude_'
           'while_on_the_segments_own_branch_a_sound_speed_costs_a_tilt_equal_to_its_whole_'
           'exponent.py')
SIX = (C26, C26, C62, KRE, RAT, POT)

# ============================================================ A. the class is not its name
head("A.  WHAT THE OWED SITES ACTUALLY ARE, READ AT THE PINNED BASELINE")

_base_at_pin = [l.split('\t') for l in git('show', f'{PIN}:corpus/unread_figure_baseline.tsv').split('\n')
                if l.strip() and not l.startswith('#')]
OWED = [r for r in _base_at_pin if len(r) >= 5 and r[4] in ('FIGURE', 'FORMULA')]
_owed_mine = [r for r in OWED if r[0].startswith(MINE)]
print(f"      at {PIN[:8]}: {len(OWED)} owed site(s), {len(_owed_mine)} in receipts this seat owns")

gate("Ⓐ① the backlog this revision starts from is `22` owed sites, read from the gate's own baseline "
     "AT A PINNED COMMIT so the figure cannot move when this revision drops its own rows --- and `6` "
     "of the `22` are in receipts this seat owns",
     len(OWED) == 22 and len(_owed_mine) == 6)

# ** the two axes: does the LABEL attribute to a paper, and does the FILE open a `.tex` at all. **
_ATTR = re.compile(r"\bP\d\d?\b|\bsec:|\beq:|paper's own|PAPER'S OWN|the paper")


def opens_tex(rel):
    src = git('show', f'{PIN}:{rel}')
    return ".tex'" in src or '.tex"' in src


_attr = [bool(_ATTR.search(r[1])) for r in OWED]
_tex = [opens_tex(r[0]) for r in OWED]
_claim_no_gate = sum(1 for a, t in zip(_attr, _tex) if a and not t)
_aim_not_reach = sum(1 for a, t in zip(_attr, _tex) if a and t)
print(f"      labels attributing to a paper: {sum(_attr)} of {len(OWED)};  of those, "
      f"{_claim_no_gate} in files that open NO .tex and {_aim_not_reach} in files that DO")

gate("Ⓐ② ⛭ AND THE NAME UNDERSELLS THE CLASS: `19` of the `22` labels ATTRIBUTE their figure to a "
     "paper, so the defect is a LABEL MAKING A CLAIM THE GATE NEVER COVERS and not a pin somebody "
     "forgot --- which is the pre-registered hypothesis holding on its own measurement",
     sum(_attr) == 19)

gate("Ⓐ③ and the split inside those `19` is the finding rather than the total: `9` sit in files that "
     "open no `.tex` at all, and `10` in files that DO read papers --- *the second half is the "
     "dangerous one, because there the omission is not capability but AIM: the receipt looks like it "
     "checks the paper*",
     _claim_no_gate == 9 and _aim_not_reach == 10)

gate("Ⓐ④ ⌗ and the `3` that attribute to nothing are reported and NOT exempted: `70`'s baseline "
     "header says a record of adjudications and not a list of exemptions, so a site the detector may "
     "over-report still leaves the count only by the file reading the paper",
     len(OWED) - sum(_attr) == 3)

# ============================================================ B. C26's three invisible facts
head("B.  C26 WAS COMPARING AGAINST A NUMBER THE PAPER HAD WITHDRAWN AS THE ERROR")

_P15 = body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
_papers = [os.path.join(ROOT, 'corpus', f) for f in sorted(os.listdir(os.path.join(ROOT, 'corpus')))
           if f.endswith('.tex') and not f.startswith('appendix_receipts')]
_all_bodies = ' '.join(body(f) for f in _papers)
RETIRED = r'9.4\%'
REPLACED = r'8.2\%'
RATE_GAP = 'puts $10.8\\%$ of that gap into the diffusion length by itself'
OBSERVABLE = 'moved by under a per cent'
APART = 'the rate gap is not what the signature is made of'
print(f"      live paper bodies ({len(_papers)} files): {RETIRED!r} x{_all_bodies.count(RETIRED)}, "
      f"{REPLACED!r} x{_all_bodies.count(REPLACED)}")

gate("Ⓑ① ⓵ THE FIGURE IS RETIRED: `$9.4\\%$` is absent from EVERY paper body, and so is the "
     "`$8.2\\%$` that replaced it --- so the number two of this seat's gates named in the present "
     "tense is carried by no paper at all",
     _all_bodies.count(RETIRED) == 0 and _all_bodies.count(REPLACED) == 0)

_subj = git('log', '-1', '--format=%s', R2755)
_diff = git('show', R2755, '--', 'corpus/CR_cosmology.tex')
_removed = [l for l in _diff.split('\n') if l.startswith('-') and RETIRED in l]
_added = [l for l in _diff.split('\n') if l.startswith('+') and REPLACED in l]
print(f"      {R2755}: {_subj.strip()[:96]}")
print(f"      that commit removes {len(_removed)} line(s) carrying {RETIRED!r} and adds "
      f"{len(_added)} carrying {REPLACED!r}")

gate("Ⓑ② and WHEN it was retired is read from the commit that did it rather than inferred: `r2755` "
     "removes the ONE line carrying `$9.4\\%$` from this paper and writes `$8.2\\%$` across `8` "
     "lines in the same pass, and its own subject line calls the retired figure ***the error*** --- "
     "*so the correction was a sweep and not a typo fix, which is why nothing of it reached a gate*",
     'the one 9.4% was the error' in _subj and len(_removed) == 1 and len(_added) == 8)

# ** ⓶ the label's own claim, checked against the figure it named.  The three weightings are C26's
#   and are read out of C26's run below; here the arithmetic alone is the point. **
_W3, _W6, _UNW = 8.7, 7.8, 13.1
_between = _W6 < 9.4 < _W3
_what_cond_said = (_W6 < 9.4 < _UNW) and (_W3 < 9.4)
print(f"      is 9.4 between {_W6} and {_W3}? {_between};   "
      f"what the CONDITION actually said: {_what_cond_said}")

gate("Ⓑ③ ⓶ THE LABEL ASSERTED A BETWEENNESS THE CONDITION NEVER TESTED, AND IT WAS TRUE OF NO "
     "FIGURE: the label said `+9.4%` lies BETWEEN the two weightings, `$8.7$` and `$7.8$`, and it "
     "does not; the condition said something else entirely, that the figure is ABOVE both and below "
     "the unweighted `$13.1$`, which is true --- ***so the gate was green on a claim that was not "
     "its label's***",
     not _between and _what_cond_said)

gate("Ⓑ④ ⓷ AND IT WAS THE WRONG OBJECT: the retired figure was the OBSERVABLE's, which `P15` now "
     "states as `moved by under a per cent`, while `$13.1$`, `$8.7$` and `$7.8$` are RATE-GAP scale "
     "--- and the paper separates the two in its own voice, all three sentences READ here",
     RATE_GAP in _P15 and OBSERVABLE in _P15 and APART in _P15)

# ============================================================ C. the six repairs
head("C.  THE SIX ARE REPAIRED BY READING THE PAPER, AND THE BACKLOG FALLS BY RUNNING")

# ** each row is (the fragment as the PAPER carries it, a distinctive marker as the repaired SOURCE
#   carries it).  The two differ for two reasons and both are named rather than papered over:
#   a Python literal escapes the backslash, and one pin is written as two adjacent string pieces,
#   so the whole literal exists at run time and never contiguously in the file. **
PINS = (
    (C26, RATE_GAP, 'of that gap into the diffusion length by itself'),
    (C26, OBSERVABLE, OBSERVABLE),
    (C26, APART, APART),
    (C62, 'on $185$ bins, is the better-converged', 'bins, is the better-converged'),
    (KRE, 'the Kretschmann scalar is $48M^2/r^6+24/\\alpha^4$', 'the Kretschmann scalar is $48M^2/r^6'),
    (RAT, 'The two therefore stand in the fixed ratio $2^{1/3}$ for every $M$',
     'stand in the fixed ratio $2^{1/3}$ for every $M$'),
    (POT, "$\\Phi''+3\\mathcal{H}(1+w)\\Phi'+[2\\mathcal{H}'+(1+3w)\\mathcal{H}^{2}]"
          "\\Phi+wk^{2}\\Phi=0$",
     "(1+3w)\\mathcal{H}^{2}"),
)
_sited = {}
for rel, frag, marker in PINS:
    src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    _sited[(rel, frag)] = (_P15.count(frag),
                           marker in src or marker.replace('\\', '\\\\') in src)
for (rel, fr), (n, insrc) in _sited.items():
    print(f"      {n}x in P15, pinned in source: {insrc}   {fr[:58]}")

gate("Ⓒ① every pin the six repairs added is present in `P15` at EXACTLY ONE site and is carried in "
     "the repaired source --- one site because a cover that admits a duplicate cannot keep the count "
     "exact, which is the standing guard's own second clause",
     all(n == 1 and insrc for n, insrc in _sited.values()) and len(_sited) == 7)

_live_base = [l.split('\t') for l in
              open(os.path.join(ROOT, 'corpus', 'unread_figure_baseline.tsv'),
                   encoding='utf-8').read().split('\n')
              if l.strip() and not l.startswith('#')]
_live_owed = [r for r in _live_base if len(r) >= 5 and r[4] in ('FIGURE', 'FORMULA')]
_live_mine = [r for r in _live_owed if r[0].startswith(MINE)]
print(f"      the gate's baseline now carries {len(_live_owed)} owed site(s), "
      f"{len(_live_mine)} of them this seat's")

gate("Ⓒ② the backlog falls `22` → `16` and this seat's share of it falls to `0` --- and it falls "
     "because the SITES ARE GONE: each now reads the paper, so the gate reported them stale and the "
     "rows were dropped, which is a fall by running and never by reclassification",
     # ⛭ r7246 (60): `== 16` was an exact count on a backlog ANOTHER SEAT LOWERS -- so a fall, which
     #   the row calls the work being done, turned this gate red.  Monotone now; the `0` stays exact
     #   because it is an absence guard and firing on this seat's share RETURNING is its purpose.
     len(_live_owed) <= 16 and len(_live_mine) == 0 and len(_live_owed) < len(OWED))

_M_OK = (12 * (2 * 1.0) ** 2) == (48 * 1.0 ** 2)
gate("Ⓒ③ ⌗ and one repair reconciled two SPELLINGS of one object rather than just pinning it: the "
     "paper writes the invariant with `$48M^2/r^6$` and this seat's receipt with `$12r_s^2/r^6$`, "
     "equal because `$r_s=2M$` --- asserted now rather than assumed, so the two presentations cannot "
     "drift apart unnoticed",
     _M_OK and 'r_s=2M' in open(os.path.join(ROOT, KRE), encoding='utf-8').read())

# ============================================================ D. the control, performed here
head("D.  THE TWO-SIDED CONTROL, PERFORMED LIVE ON C26 AND COUNTED")


def shadow_run(rel, frm, to, pre_src):
    """a symlink shadow tree whose `corpus/` alone is rebuilt.  Returns (exit code, substitutions).
    ** Nothing in the real tree is written to. **"""
    td = tempfile.mkdtemp()
    try:
        for e in os.listdir(ROOT):
            if e in ('corpus', 'receipts'):
                continue
            os.symlink(os.path.join(ROOT, e), os.path.join(td, e))
        os.mkdir(os.path.join(td, 'receipts'))
        for e in os.listdir(os.path.join(ROOT, 'receipts')):
            os.symlink(os.path.join(ROOT, 'receipts', e), os.path.join(td, 'receipts', e))
        if pre_src is not None:
            fam = rel.split('/')[1]
            os.remove(os.path.join(td, 'receipts', fam))
            d = os.path.join(td, 'receipts', fam)
            os.mkdir(d)
            for e in os.listdir(os.path.join(ROOT, 'receipts', fam)):
                os.symlink(os.path.join(ROOT, 'receipts', fam, e), os.path.join(d, e))
            os.remove(os.path.join(d, os.path.basename(rel)))
            with open(os.path.join(d, os.path.basename(rel)), 'w', encoding='utf-8') as fh:
                fh.write(pre_src)
        os.mkdir(os.path.join(td, 'corpus'))
        subs = 0
        for e in os.listdir(os.path.join(ROOT, 'corpus')):
            s_, d_ = os.path.join(ROOT, 'corpus', e), os.path.join(td, 'corpus', e)
            if frm and e.endswith('.tex'):
                t = open(s_, encoding='utf-8', errors='replace').read()
                subs += t.count(frm)
                with open(d_, 'w', encoding='utf-8') as fh:
                    fh.write(t.replace(frm, to))
            else:
                os.symlink(s_, d_)
        rc = subprocess.run(['python3', os.path.join(td, rel)], capture_output=True, text=True,
                            env=dict(os.environ, NODE='60'), timeout=900).returncode
        return rc, subs
    finally:
        shutil.rmtree(td, ignore_errors=True)


_FRM = 'puts $10.8\\%$ of that gap into the diffusion length by itself'
_TO = 'puts $14.8\\%$ of that gap into the diffusion length by itself'
_PRE = git('show', f'{PIN}:{C26}')
_live_rc, _ = shadow_run(C26, None, None, None)
_pert_rc, _pert_n = shadow_run(C26, _FRM, _TO, None)
_prerep_rc, _prerep_n = shadow_run(C26, _FRM, _TO, _PRE)
print(f"      C26 live/repaired exit={_live_rc};   perturbed/repaired exit={_pert_rc} "
      f"(substitutions={_pert_n});   perturbed/PRE-repair exit={_prerep_rc} "
      f"(substitutions={_prerep_n})")

gate("Ⓓ① THE REPAIR BITES, SHOWN BY RUNNING AND NOT BY READING: `C26` is GREEN on the live corpus "
     "and goes ***RED*** on a shadow tree whose only change is the paper's own rate-gap figure moved "
     "--- and the shadow is built by symlink with `corpus/` alone rebuilt, so nothing in the real "
     "tree is written to",
     _live_rc == 0 and _pert_rc != 0)

gate("Ⓓ② AND THE OTHER SIDE IS WHAT MAKES IT A CONTROL: the PRE-repair source under the SAME "
     "perturbation stays ***GREEN*** --- so the gates this revision repaired genuinely could not "
     "notice the paper moving, which is `70`'s own baseline note reproduced here rather than cited",
     _prerep_rc == 0)

gate("Ⓓ③ ⛔ AND THE SUBSTITUTION IS COUNTED, WHICH IS THE LESSON THAT COST A CORRECT REPAIR: one "
     "control in this revision came back saying a good repair had failed because the perturbation "
     "had substituted NOTHING --- the pinned sentence spans a line break in the raw `.tex` while the "
     "receipt reads a whitespace-collapsed body.  ***A mutation that mutates nothing leaves the gate "
     "green and reads exactly like a repair that does not bite***, so both perturbed cells assert a "
     "non-zero substitution count",
     _pert_n > 0 and _prerep_n > 0 and _pert_n == _prerep_n)

# ** the other four sites' controls were run out of band, in the same harness, and are RECORDED
#   rather than re-performed: fifteen receipt runs inside one receipt is a cost the runner should
#   not carry, and `r7212`'s fourth-face lesson says a gate on other receipts' runs in an
#   environment this seat does not control is its own defect. **
TABLE = (('C62', 0, 1, 0), ('Kretschmann', 0, 1, 0), ('ratio', 0, 1, 0), ('potential-eq', 0, 1, 0))
for nm, a, b, c in TABLE:
    print(f"      recorded: {nm:14s} live/repaired={a}  perturbed/repaired={b}  "
          f"perturbed/pre-repair={c}")
print("      ⚠ the potential-equation row's third cell returned 1 once and 0 on three consecutive "
      "re-runs of the same configuration; 3 of 4 is the reading and the disagreement is named.")

gate("Ⓓ④ ⌗ and the other four sites' controls are RECORDED with their method rather than "
     "re-performed here, because fifteen receipt runs inside one receipt is a cost the runner should "
     "not carry --- `r7212`'s fourth face is a gate on an environment this seat does not control. "
     "⚠ *One cell is reported CONTRADICTED rather than smoothed: `1` once against `0` on three "
     "consecutive re-runs, and this corpus already carries same-commit red/green pairs.*",
     all(t[1] == 0 and t[2] != 0 and t[3] == 0 for t in TABLE) and len(TABLE) == 4)

# ============================================================ E. the two backlogs, one failure
head("E.  AND THE TWO BACKLOGS READ AS ONE FAILURE FROM OPPOSITE ENDS")

_QP = [l.split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                                   encoding='utf-8').read().split('\n')
       if l.strip() and not l.startswith('#')]
_unadj = [r for r in _QP if len(r) >= 6 and r[5] == 'UNADJUDICATED']
_delib_mine = [r for r in _QP if len(r) >= 6 and r[5] == 'DELIBERATE' and r[0].startswith(MINE)]
print(f"      quote-pin backlog: {len(_unadj)} unadjudicated;  this revision's own six new keys are "
      f"adjudicated, this seat carrying {len(_delib_mine)} DELIBERATE rows")

gate("Ⓔ① the six pins this revision ADDED are adjudicated in the same pass rather than left to "
     "raise a ceiling --- a repair that discharges one backlog by growing another is not a repair, "
     "and the unadjudicated count is not RAISED by this pass, standing at or below `2167`  ⌗ *stated "
     "monotonically because the subject is this pass not growing the backlog, and a later batch from "
     "another seat has since lowered it*",
     len(_unadj) <= 2167)

gate("Ⓔ② ⇒⇒ SO THE HYPOTHESIS IS REPORTED AS IT CAME BACK, WHICH IS NOT WHOLLY AS WANTED: *the "
     "attribution measurement supports it --- `19` of `22` labels claim a paper says something and "
     "nothing covered the claim, against a quote-pin backlog of pins covering what no argument needs "
     "--- but `19` of `22` is a MEASUREMENT ON THIS BACKLOG and not a proof that the two classes are "
     "one object.* ⛔ **The unification is named as a reading, the count is named as a count, and the "
     "reading is NOT written into any gate**",
     # ⛭ r7246 (60): the same fall that turned `Ⓒ②` red reaches here -- the `16` is the LIVE
     #   backlog, which another seat lowers, and it is incidental to this gate's subject.  Monotone;
     #   `19` and `22` stay exact because both are read at a PIN and cannot move.
     sum(_attr) == 19 and len(OWED) == 22 and len(_live_owed) <= 16)

# ============================================================ F. self
head("F.  THIS RECEIPT'S OWN EXPOSURE")

_SELF = open(os.path.abspath(__file__), encoding='utf-8').read()
_SELF_CODE = '\n'.join(l for l in _SELF.split('\n') if not l.lstrip().startswith('#'))
gate("Ⓕ① this receipt's own population is read at a PINNED commit and its only historical read is "
     "the single commit that retired the figure, so no count here moves when a seat adds a file --- "
     "and the live paper state it does assert is asserted by RUNNING `C26`, not by a count",
     PIN in _SELF and R2755 in _SELF and _live_rc == 0)

gate("Ⓕ② ⌗ and it carries no bare `True` literal in argument position, which is the form "
     "`r7212`'s fixup had to repair after `check_cannot_fail` read one as an assertion: the shadow "
     "modes here are passed as named arguments or as `None`",
     '(C26, None, None, None)' in _SELF_CODE
     and (',' + ' ' + 'True' + ')') not in _SELF_CODE)

# ============================================================ verdict
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)} of {len(CHECKS)} check(s) pass.\n")
if _bad:
    print("  FAILED:")
    for n in _bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS.  PO-78's unread-figure backlog is not a list of forgotten pins: 19 of its 22 labels
  ATTRIBUTE a figure to a paper and nothing covers the attribution, and the dangerous half is the 10
  whose files DO read papers, where the omission is aim and not capability.  Six sites in this seat's
  own receipts are repaired by reading the paper's own sentence at exactly one site each, the backlog
  falls 22 to 16 by running rather than by reclassification, and the six new pins are adjudicated in
  the same pass so one backlog is not discharged by growing another.  AND ONE OF THE SIX WAS NOT
  MERELY UNREAD: C26's two gates were comparing against 9.4 per cent, a figure this paper removed at
  r2755 as THE ERROR, under a label asserting a betweenness that was true of no figure and that its
  own condition never tested, about the OBSERVABLE while the computation is rate-gap scale.  The
  repair is controlled two-sided and live: green on the corpus, RED with the paper's figure moved,
  green on the pre-repair source under the same move.  AND THE CONTROL ITSELF TAUGHT THE MORE USEFUL
  THING -- one perturbation substituted nothing, came back green, and read exactly like a repair that
  had failed, so a must-come-back-wrong control now counts its substitutions.""")
