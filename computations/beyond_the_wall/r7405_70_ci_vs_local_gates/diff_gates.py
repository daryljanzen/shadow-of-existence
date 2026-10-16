"""r7405+70: every command a gates.yml job runs, against what run_fast_job.sh and sweep_gates.sh run locally."""
import re, sys, yaml
wf = yaml.safe_load(open('.github/workflows/gates.yml'))
src = open('.github/workflows/gates.yml').read()
loop = set()
for m in re.finditer(r'for (\w+) in ((?:[^;]|\n)*?); do', src):
    loop |= {t for t in re.split(r'\s+|\\\n', m.group(2)) if re.match(r'^[a-z_][a-z0-9_]*$', t)}
SKIP = ('pip ', 'git ', 'echo', 'cat ', 'if ', 'fi', 'for ', 'done', 'fails=', 'printf', 'blob=', 'tree=', 'set ', '[ ', 'then', 'else', 'exit', 'cd ', 'export', 'mkdir', 'cp ', 'ls ', 'tee', 'sleep')
rows = []
for jn, job in wf['jobs'].items():
    cond = str(job.get('if', 'always'))
    for st in job.get('steps', []):
        run = st.get('run')
        if not run: continue
        for line in run.split('\n'):
            l = line.strip()
            for m in re.finditer(r'(python3\s+(?:-\S+\s+)*(corpus|scripts)/([\w.]+\.py)[^|;&]*|bash\s+(scripts/[\w.]+\.sh)[^|;&]*)', l):
                cmd = m.group(0).strip()
                name = (m.group(3) or m.group(4) or '').replace('.py', '')
                if m.group(2) == 'scripts' and '$c' in l: continue
                rows.append((jn, cond, st.get('name', '?'), m.group(2) or 'bash', name, cmd))
seen = set()
print(f'{"job":15s} {"local?":28s} command')
for jn, cond, sn, kind, name, cmd in rows:
    key = (jn, name)
    if key in seen: continue
    seen.add(key)
    if kind == 'corpus' and name.startswith('check_'):
        local = 'sweep_gates.sh' + (' + run_fast_job.sh' if name in loop else '')
    elif name in loop:
        local = 'run_fast_job.sh'
    elif '$g' in cmd or '$c' in cmd:
        local = 'run_fast_job.sh (loop)'
    else:
        local = '-- NONE --'
    per_push = 'push' in cond or 'pull_request' in cond or cond == 'always'
    print(f'{jn:15s} {local:28s} {cmd[:110]}  {"" if per_push else "[schedule/dispatch only]"}')
