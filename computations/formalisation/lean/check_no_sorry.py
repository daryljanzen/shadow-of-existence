"""check_no_sorry.py -- does every stated theorem in ShadowFormal compile, and rest on no sorryAx?

r7263+71.  A theorem that type-checks is not yet evidence, because `sorry` type-checks too.
This reads the axioms Lean reports for each theorem (Axioms.lean) and separates:
  PROVED  -- compiles, and its axioms are a subset of {propext, Classical.choice, Quot.sound};
  STATED  -- compiles, and rests on sorryAx: a statement, never reported as proved;
  BROKEN  -- does not compile.
GATE ZERO: the positive control (controls/SorryControl.lean) must come back STATED.  If the
checker cannot see a sorry it was handed, nothing below it prints.

Run from this directory, with elan's lake on PATH:  python3 check_no_sorry.py
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STD = {"propext", "Classical.choice", "Quot.sound"}


def lean(*args, timeout=3600):
    env = dict(os.environ)
    env["PATH"] = os.path.expanduser("~/.elan/bin") + os.pathsep + env.get("PATH", "")
    r = subprocess.run(["lake", *args], cwd=HERE, capture_output=True, text=True,
                       timeout=timeout, env=env)
    return r.returncode, r.stdout + r.stderr


def parse_axioms(out):
    res = {}
    for m in re.finditer(r"'([\w\.]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                         out):
        name, ax = m.group(1), m.group(2)
        res[name] = set(a.strip() for a in ax.split(",")) if ax else set()
    return res


def verdict(ax):
    if "sorryAx" in ax:
        return "STATED"
    return "PROVED" if ax <= STD else "OTHER-AXIOM"


fails = []
print("GATE ZERO -- the positive control")
rc, out = lean("env", "lean", "controls/SorryControl.lean")
ctrl = parse_axioms(out)
cv = verdict(ctrl.get("shadow_control_sorry", set())) if "shadow_control_sorry" in ctrl else "UNREAD"
print(f"  control shadow_control_sorry -> {cv}")
if cv != "STATED":
    print("VERDICT: GATE ZERO FAILED -- the checker cannot see a sorry it was handed; nothing below is a reading")
    sys.exit(1)

print("\nBUILD")
rc, out = lean("build")
print("  " + (out.strip().splitlines() or ["(no output)"])[-1])
if rc != 0:
    print(out[-4000:])
    print("VERDICT: BROKEN -- lake build failed")
    sys.exit(1)

print("\nAXIOMS")
rc, out = lean("env", "lean", "Axioms.lean")
if rc != 0:
    print(out[-4000:])
    print("VERDICT: BROKEN -- Axioms.lean did not elaborate")
    sys.exit(1)
listed = re.findall(r"^#print axioms ([\w\.]+)", open(os.path.join(HERE, "Axioms.lean")).read(), re.M)
ax = parse_axioms(out)
counts = {}
for name in listed:
    v = verdict(ax[name]) if name in ax else "UNREAD"
    counts[v] = counts.get(v, 0) + 1
    print(f"  [{v:7s}] {name}   {sorted(ax.get(name, []))}")
    if v != "PROVED":
        fails.append(name)

print()
print("  " + "  ".join(f"{k} {v}" for k, v in sorted(counts.items())))
if fails:
    print(f"VERDICT: {len(fails)} NOT PROVED: {', '.join(fails)}")
    sys.exit(1)
print(f"VERDICT: ALL {len(listed)} THEOREMS COMPILE AND REST ON NO sorryAx -- the control's sorry was seen, so this reading can fail")
