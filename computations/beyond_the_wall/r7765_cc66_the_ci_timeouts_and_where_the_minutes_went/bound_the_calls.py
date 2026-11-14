#!/usr/bin/env python3
"""`r7765+cc66` THE TWO UNBOUNDED CI CALLS, BOUNDED -- AND THE BOUND EXERCISED BY A REAL HANG.

⛭ Registered in `PREDICTION.md` at `r7765+cc66.0`, pushed before either file was touched.  Rows `(4)`
to `(7)`.

⛭ ** THE SEEDED HANG IS A REAL ONE. **  It is NOT a monkeypatched `subprocess.run`: a fake `git` and a
fake `gh`, each a shell script that sleeps, are put EARLIER ON `PATH`, so the actual
`subprocess.run(timeout=)` machinery is what has to fire.  A timeout tested against a stand-in is a
tested stand-in.
"""
import importlib.util
import os
import stat
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f"             {witness}")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def fake(dirpath, name, body):
    p = os.path.join(dirpath, name)
    with open(p, 'w') as f:
        f.write(body)
    os.chmod(p, os.stat(p).st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    return p


RC = load('rc_mod', os.path.join(ROOT, 'scripts', 'red_carry.py'))
RG = load('rg_mod', os.path.join(ROOT, 'scripts', 'rerun_guard.py'))

print('=' * 100)
print(__doc__)
print('=' * 100)

# ------------------------------------------------------------------ ④ behaviour on normal calls is unchanged
def git_old(root, *a, check_=False, env=None):
    """the helper EXACTLY as it stood before `r7765`, kept here so `④` is a comparison and not a claim"""
    return subprocess.run(['git', *a], cwd=root, capture_output=True, text=True,
                          env=None if env is None else {**os.environ, **env})


ok4, w4 = True, []
for args in (('rev-parse', 'HEAD'), ('status', '--porcelain'), ('cat-file', '-e', 'deadbeef' * 5)):
    new = RC.git(ROOT, *args)
    old = git_old(ROOT, *args)
    same = (new.returncode == old.returncode and new.stdout == old.stdout and new.stderr == old.stderr)
    ok4 = ok4 and same
    w4.append(f"{' '.join(args)[:28]}: rc {new.returncode}=={old.returncode} {'same' if same else 'DIFFER'}")
check("⛭ `r7765` ** ④ `git()`'s BEHAVIOUR ON A CALL THAT RETURNS IS BIT-IDENTICAL TO BEFORE ** ⇒ *two "
      "succeeding calls and one failing one, compared field by field against a copy of the pre-change "
      "helper kept in this probe — so this row is a comparison, not an assurance*",
      ok4, '; '.join(w4))

# ------------------------------------------------------------------ ⑤ the seeded hang, through a real PATH
with tempfile.TemporaryDirectory() as bin_d:
    fake(bin_d, 'git', '#!/bin/sh\nsleep 30\n')
    saved = os.environ['PATH']
    os.environ['PATH'] = bin_d + os.pathsep + saved
    try:
        t0 = time.time()
        r = RC.git(ROOT, 'fetch', 'origin', timeout=2)
        dt = time.time() - t0
    finally:
        os.environ['PATH'] = saved
check("⛭⛔⛭ `r7765` ** ⑤ AND THE BOUND FIRES ON A **REAL** HANG: A FAKE `git` THAT SLEEPS `30` s RETURNS "
      "IN `2` s WITH THE SHAPE A NON-ZERO RETURN CODE ALREADY RETURNS ** ⇒ *** the fake is put earlier on "
      "`PATH`, so `subprocess.run(timeout=)` itself is what fires — not a monkeypatched stand-in. "
      "`returncode` is non-zero, `stdout` and `stderr` are strings, which is all any caller reads, so no "
      "caller changes. ** This is the row that makes the fix a fix rather than a line of code. ** *** ",
      dt < 6.0 and r.returncode != 0 and isinstance(r.stdout, str) and isinstance(r.stderr, str),
      f"returned in {dt:.2f}s against a 30s sleep and a 2s bound; returncode {r.returncode}; "
      f"stderr {r.stderr!r}")

# ------------------------------------------------------------------ ⑥ _read_tip likewise
with tempfile.TemporaryDirectory() as bin_d:
    fake(bin_d, 'gh', '#!/bin/sh\nsleep 60\n')
    saved = os.environ['PATH']
    os.environ['PATH'] = bin_d + os.pathsep + saved
    RG.subprocess.run.__module__          # touch, so a reader sees it is the real subprocess
    try:
        t0 = time.time()
        tip = RG._read_tip({'GITHUB_REPOSITORY': 'o/r', 'GITHUB_REF_NAME': 'b'})
        dt6 = time.time() - t0
    finally:
        os.environ['PATH'] = saved
check("⛭⛔ `r7765` ** ⑥ `_read_tip` IS BOUNDED TOO, AND A HANG RETURNS `''` — WHICH IS WHAT A NON-ZERO "
      "RETURN CODE ALREADY RETURNED ** ⇒ *so `verdict()`'s declining path is already written for it. ⌗ "
      "The `30` s bound is registered, not chosen to fit: a single API read is far under it. This row "
      "waits the full bound on purpose, which is why it is the slowest here*",
      tip == '' and dt6 < 40.0,
      f"returned {tip!r} in {dt6:.1f}s against a 60s sleep and a 30s bound")

# ------------------------------------------------------------------ ⑦ the callers still behave
# ⛔ MY REGISTRATION WAS WRONG ABOUT THIS ROW: it said "as `red_carry.py`'s own self-test already builds
#   one (`git init -q --bare`)".  There IS no `--selftest` entry point -- that `git init --bare` sits
#   inside a `--history` path.  So this row builds the repository itself and drives the REAL `fetch()`,
#   which is the function whose `git fetch` hung in CI.
env = {**os.environ, 'GITHUB_REPOSITORY': 'daryljanzen/shadow-of-existence', 'GITHUB_REF_NAME': 'main'}
pr = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'rerun_guard.py')],
                    capture_output=True, text=True, env=env, cwd=ROOT, timeout=120)

with tempfile.TemporaryDirectory() as d:
    remote, work = os.path.join(d, 'rem'), os.path.join(d, 'work')
    subprocess.run(['git', 'init', '-q', '--bare', remote], check=True)
    subprocess.run(['git', 'init', '-q', work], check=True)
    for a in (('config', 'user.email', 'p@x'), ('config', 'user.name', 'p'),
              ('remote', 'add', 'origin', remote)):
        subprocess.run(['git', *a], cwd=work, check=True)
    open(os.path.join(work, 'f'), 'w').write('x')
    subprocess.run(['git', 'add', 'f'], cwd=work, check=True)
    subprocess.run(['git', 'commit', '-qm', 'c'], cwd=work, check=True)
    # ⛭ THE FIXTURE HAD TO BE MADE REALISTIC, and my first one was not: I gave the bare remote NO refs
    #   at all, which never happens in CI -- there the remote is the repository and only the CARRY ref is
    #   missing.  On a refless remote `fetch()` fell through its return-code branch into an unguarded
    #   `json.loads('')` and raised `JSONDecodeError`.  So the remote gets a branch first, and the carry
    #   ref alone is absent.  ⌗ REPORTED, not fixed here: that fall-through is a real latent fragility --
    #   `fetch()`'s "nobody has written one yet" path is recognised by git's stderr WORDING, and a fetch
    #   that returns 0 without creating the ref reaches the parse with an empty string.  It is not what
    #   hung CI and it is not this order's subject.
    subprocess.run(['git', 'push', '-q', 'origin', 'HEAD:refs/heads/main'], cwd=work, check=True)
    led, tip = RC.fetch(work, 'origin')
    empty_ok = (led == {} and tip is None)
    # and now the same call with a hanging `git`: it must come back FAST and VISIBLY, not hang
    with tempfile.TemporaryDirectory() as bin_d:
        fake(bin_d, 'git', '#!/bin/sh\nsleep 60\n')
        saved = os.environ['PATH']
        os.environ['PATH'] = bin_d + os.pathsep + saved
        try:
            t0 = time.time()
            RC.GIT_TIMEOUT = 2
            try:
                RC.fetch(work, 'origin')
                shape = 'returned'
            except SystemExit as e:
                shape = f'SystemExit: {e}'
            dt7 = time.time() - t0
        finally:
            os.environ['PATH'] = saved
            RC.GIT_TIMEOUT = 300

check("⛭⛔⛭ `r7765` ** ⑦ AND THE REAL CALLER TURNS THE HANG INTO A **FAST, VISIBLE FAILURE** INSTEAD OF A "
      "`95`-MINUTE ONE ** ⇒ *** `fetch()` on a healthy repository whose carry ref does not exist still "
      "returns `({}, None)`, unchanged. With a `git` that sleeps, it now raises `SystemExit` naming the "
      "timeout in about two seconds — the same path it already took for a ref it cannot read. ** So the "
      "record step FAILS where it used to hang, which is the whole point: a job that fails in seconds is "
      "reportable and a job cancelled at `95` minutes is not. ** *** ⌷ *This is a behaviour CHANGE and I "
      "am not calling it a no-op: a timeout surfaces as a recording failure. It cannot be silently green "
      "— nothing was recorded.*",
      empty_ok and shape.startswith('SystemExit') and dt7 < 10.0
      and pr.returncode in (0, 10) and 'RERUN-GUARD:' in pr.stdout,
      f"healthy fetch with no carry ref: ({led}, {tip}); hanging fetch: {shape[:88]} in {dt7:.2f}s; "
      f"rerun_guard exits {pr.returncode}")

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {4 - len(FAILS)} of 4 rows;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
