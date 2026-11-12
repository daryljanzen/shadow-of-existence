"""One clean model trial per call, recorded in full.  Shared by E1-E8.

Each trial runs in its own new directory under /tmp, never under the repository or this seat's scratchpad
(whose path names the repository: SUBJECT_ROUTE_PROBE.md).  The session has no setting sources, no MCP
servers, no tools, no persistence and a one-line system prompt; the variables that carry extra CLAUDE.md
directories and the account email are removed.  What still reaches a subject, identically in every condition,
is recorded in SUBJECT_ROUTE_PROBE.md.

Every trial writes one JSON record: experiment, condition, item, model, UTC timestamp, the exact system prompt
and message, the full response, usage and timing.  A record that exists is never re-run, so a batch resumes
where it stopped.

    from subject import Trial, run_batch
    run_batch([Trial(exp, cond, item_id, system, message, out_path), ...], workers=4, model='claude-opus-5-5')
"""
import json
import os
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

DROP_ENV = ('CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD', 'CLAUDE_ADDITIONAL_DIRECTORIES',
            'CLAUDE_CODE_USER_EMAIL')
DEFAULT_MODEL = 'claude-opus-5-5'


@dataclass
class Trial:
    exp: str
    cond: str
    item: str
    system: str
    message: str
    out: str               # path of the JSON record
    role: str = 'subject'  # 'subject' or 'scorer'
    rep: int = 0


def _clean_env():
    env = dict(os.environ)
    for k in DROP_ENV:
        env.pop(k, None)
    return env


def run_one(t: Trial, model: str = DEFAULT_MODEL, timeout: int = 600, retries: int = 2):
    if os.path.exists(t.out):
        return json.load(open(t.out))
    os.makedirs(os.path.dirname(t.out), exist_ok=True)
    rec = dict(asdict(t), model=model, started=datetime.now(timezone.utc).isoformat())
    for attempt in range(retries + 1):
        d = tempfile.mkdtemp(prefix='subj_', dir='/tmp')
        t0 = time.time()
        try:
            p = subprocess.run(
                ['claude', '-p', '--setting-sources', '', '--strict-mcp-config', '--no-session-persistence',
                 '--tools', '', '--model', model, '--system-prompt', t.system, '--output-format', 'json',
                 t.message],
                cwd=d, env=_clean_env(), capture_output=True, text=True, timeout=timeout)
            out = json.loads(p.stdout)
            if out.get('is_error'):
                raise RuntimeError(out.get('result'))
            rec.update(response=out.get('result', ''), usage=out.get('usage'),
                       cost_usd_list=out.get('total_cost_usd'), duration_ms=out.get('duration_ms'),
                       wall_s=round(time.time() - t0, 2), attempt=attempt)
            break
        except Exception as e:                       # noqa: BLE001 -- recorded, then retried
            rec['error_' + str(attempt)] = repr(e)[:500]
            time.sleep(5 * (attempt + 1))
        finally:
            shutil.rmtree(d, ignore_errors=True)
    else:
        rec['failed'] = True
    tmp = t.out + '.part'
    json.dump(rec, open(tmp, 'w'), indent=1, ensure_ascii=False)
    os.replace(tmp, t.out)
    return rec


def run_batch(trials, workers: int = 4, model: str = DEFAULT_MODEL):
    with ThreadPoolExecutor(workers) as ex:
        recs = list(ex.map(lambda t: run_one(t, model), trials))
    bad = [r for r in recs if r.get('failed')]
    print(f'  {len(recs)} trials, {len(bad)} failed after retries')
    return recs
