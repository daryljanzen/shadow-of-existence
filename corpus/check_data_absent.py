#!/usr/bin/env python3
"""check_data_absent.py -- A RECEIPT MAY REASON FROM A DATUM'S ABSENCE, BUT NOT AFTER IT ARRIVES.
Built r7842+60.

** WHAT THIS CATCHES. **  `r7842` was ordered to add polarisation to the score and to say what the
low-multipole and lensing-reconstruction information would decide.  Two of the three could not be
answered, because the data are not in this repository -- and *a finding that rests on an absence is
the one kind of finding that can be falsified by someone else's success.*  The day a node banks the
lensing-reconstruction bandpowers, every sentence that says the harness cannot score against them
becomes false, silently, in a file nobody is editing.  This gate is what makes that arrival loud.

** THE LEDGER RANGES OVER ITS OWN ROWS AND NOTHING ELSE. **  `data_absent.tsv` is not a census of
what the harness lacks and cannot be one: absence is not enumerable.  It is a list of the absences
some receipt REASONS FROM, each with the probe that shows it, and the gate's claim is exactly
`every row's datum is still absent` -- never `these are the only data missing`.  A datum not in the
ledger is not thereby present, and nothing here should be read as saying so.

** WHY THE PROBES ARE BEHAVIOURAL AND NOT A GREP. **  `planck_lite_py` is WIRED for low-multipole
bins -- it carries an `nbintt_low_ell` and a `use_low_ell_bins` switch -- and asking it for them
raises `FileNotFoundError` naming `CTT_bin_low_ell_2018.dat`.  So the harness does not LACK THE
CAPABILITY; it was never given the data, and the distinction is the whole finding.  A grep for the
word `lensing` would have found the derived `phi-phi` spectra this repository does hold and
concluded the opposite of the truth: *what is missing is not a spectrum to compute, it is a
measurement to be scored against.*  The probes therefore ask the harness, not the prose.

Fails on:
  ARRIVED    a listed datum whose probe now reads PRESENT -- the absence is over, and the receipt
             named in its row has to be updated to assert the state the corpus now holds (r2673)
  ORPHANED   a row whose receipt is not a file -- an absence nothing reasons from is not adjudicated
  MALFORMED  a row that is not four fields, or a probe of an unknown kind
  SEED       the two-sided control: each probe kind must read a thing that IS there as PRESENT and a
             one-character perturbation of it as ABSENT.  ** A detector that never fires is not
             evidence of absence, and this is the arm that stops the gate being decorative. **

    python3 corpus/check_data_absent.py [--list]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(HERE, 'data_absent.tsv')

# the two-sided control: (probe that must read PRESENT, probe that must read ABSENT)
SEEDS = (
    ('path:computations/planck_tt_likelihood/data/planck2018_plik_lite/c_matrix_plik_v22.dat',
     'path:computations/planck_tt_likelihood/data/planck2018_plik_lite/c_matrix_plik_v23.dat'),
    ('attr:computations/planck_tt_likelihood/planck_lite_py.py:PlanckLitePy:nbintt',
     'attr:computations/planck_tt_likelihood/planck_lite_py.py:PlanckLitePy:nbinttX'),
)


def rows():
    out = []
    with open(LEDGER, encoding='utf-8') as fh:
        for n, line in enumerate(fh, 1):
            if line.startswith('#') or not line.strip():
                continue
            out.append((n, line.rstrip('\n').split('\t')))
    return out


def present(probe):
    """True if the datum the probe names is THERE; raises ValueError on an unknown probe kind

    ** `attr` IS READ OFF THE SOURCE AND NOT BY IMPORTING. **  Importing `planck_lite_py` costs a
    613-square covariance read and would make a cheap gate expensive; worse, it would make the
    answer depend on whether the data files happen to be present, which is the very thing being
    measured.  The class body's assignments are what declare its channels, so they are what is
    read.
    """
    kind, rest = probe.split(':', 1)
    if kind == 'path':
        return os.path.exists(os.path.join(ROOT, rest))
    if kind == 'attr':
        path, cls, name = rest.rsplit(':', 2)
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            raise ValueError(f'probe names a file that is not there: {path}')
        src = open(full, encoding='utf-8').read()
        m = re.search(r'^class\s+%s\b' % re.escape(cls), src, re.M)
        if not m:
            raise ValueError(f'probe names a class that is not there: {cls} in {path}')
        tail = src[m.start():]
        nxt = re.search(r'^class\s+\w', tail[1:], re.M)
        body = tail[:nxt.start() + 1] if nxt else tail
        return re.search(r'\b(?:self\.)?%s\s*(?::[^=\n]+)?=' % re.escape(name), body) is not None
    raise ValueError(f'unknown probe kind: {kind}')


def main(argv):
    bad = []

    for good, absent in SEEDS:
        try:
            if not present(good):
                bad.append(f'SEED      the control that must read PRESENT reads absent: {good}')
            if present(absent):
                bad.append(f'SEED      the control that must read ABSENT reads present: {absent}')
        except ValueError as e:
            bad.append(f'SEED      a control probe could not run: {e}')

    rs = rows()
    if not rs:
        bad.append('MALFORMED the ledger has no rows -- a gate over nothing asserts nothing')
    for n, f in rs:
        if len(f) != 4:
            bad.append(f'MALFORMED line {n}: {len(f)} field(s), want 4')
            continue
        key, probe, receipt, decides = f
        if not os.path.exists(os.path.join(ROOT, receipt)):
            bad.append(f'ORPHANED  {key}: no receipt at {receipt}')
        if not decides.strip():
            bad.append(f'MALFORMED {key}: the fourth field must say what the datum would decide')
        try:
            if present(probe):
                bad.append(f'ARRIVED   {key}: {probe} now reads PRESENT.  The absence this row '
                           f'records is over; update {receipt} to assert the state the corpus now '
                           f'holds, then drop this row.')
        except ValueError as e:
            bad.append(f'MALFORMED {key}: {e}')

    if '--list' in argv:
        for n, f in rs:
            if len(f) == 4:
                print(f'  {f[0]:<32} absent via {f[1].split(":", 1)[0]:<5} -- {f[3][:64]}')

    if bad:
        print(f'check_data_absent: {len(bad)} problem(s)')
        for b in bad:
            print('  ' + b)
        return 1
    print(f'check_data_absent: {len(rs)} adjudicated absence(s), all still absent; '
          f'{2 * len(SEEDS)} seed control(s) fired correctly')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
