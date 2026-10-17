#!/usr/bin/env python3
"""rerun_guard.py -- A STALE RE-RUN DOES NOT VOTE, AND SAYS SO.  r7433 ① (66), built r7433+70 from r7429+70 / r7431 ②.

** WHY.  **  A re-run of an OLD run on a branch used to join the branch's concurrency group and cancel the HEAD's own
push run (r7423+70.3); the dead run's record step still filed (60, r7432) -- composed, a re-run could file a hundred
false reds against the head it cancelled (66, r7429 ①).  `gates.yml`'s concurrency key now gives a re-run a group of
its own, so it no longer cancels the head; this guard is the other half: a re-run of a commit that is no longer the
branch tip runs to completion and then FILES NOTHING, because that commit's attempt 1 already filed for it.

** THE RE-CUT, AND WHY IT IS NOT "sha != tip".  **  r7431 E-g measured that the plain staleness test would also
silence an ATTEMPT-1 run cancelled by a newer push -- and that run's `unmeasured` record (60's r7432) is the only
trace that its pushed range was never measured.  So the guard declines only a RE-RUN (`GITHUB_RUN_ATTEMPT > 1`) whose
sha is not the tip.  Attempt 1 always records, measured or `unmeasured`.

** VISIBLE, NEVER SILENT (r7433 ③).  **  Every call prints exactly one `RERUN-GUARD:` line, recording or declining,
so a log read later can tell a guard that declined from a guard that never ran.

    python3 scripts/rerun_guard.py     exit 0 = record, 10 = declined (a stale re-run); needs GH_TOKEN on a re-run
In a step:   rc=0; python3 scripts/rerun_guard.py || rc=$?; [ "$rc" = 10 ] && exit 0
(any other non-zero is a broken guard, and the step records anyway: a broken guard must not silence a record.)
"""
import os
import subprocess
import sys

DECLINED = 10


def verdict(env=os.environ, read_tip=None):
    """(proceed: bool, line: str)"""
    attempt = int(env.get('GITHUB_RUN_ATTEMPT', '1') or '1')
    sha = env.get('GITHUB_SHA', '')
    ref = env.get('GITHUB_REF_NAME', '')
    if attempt <= 1:
        return True, f'RERUN-GUARD: attempt 1 of {sha[:9]} -- RECORDING (a first attempt always files, measured or unmeasured)'
    tip = (read_tip or _read_tip)(env)
    if not tip:
        return False, (f'RERUN-GUARD: attempt {attempt} of {sha[:9]}; the tip of {ref} could not be read -- DECLINED '
                       f'(attempt 1 already filed for this commit; nothing filed here)')
    if tip == sha:
        return True, f'RERUN-GUARD: attempt {attempt} of {sha[:9]}, which is still the tip of {ref} -- RECORDING'
    return False, (f'RERUN-GUARD: attempt {attempt} of {sha[:9]}; the tip of {ref} is {tip[:9]} -- STALE RE-RUN, '
                   f'DECLINED (attempt 1 already filed for this commit; nothing filed here)')


def _read_tip(env):
    repo, ref = env.get('GITHUB_REPOSITORY', ''), env.get('GITHUB_REF_NAME', '')
    if not (repo and ref):
        return ''
    r = subprocess.run(['gh', 'api', f'repos/{repo}/git/ref/heads/{ref}', '--jq', '.object.sha'],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ''


def main():
    ok, line = verdict()
    print(line, flush=True)
    return 0 if ok else DECLINED


if __name__ == '__main__':
    sys.exit(main())
