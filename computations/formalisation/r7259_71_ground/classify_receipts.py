"""r7259+71.4 -- reproduce the r7259 four-way receipt classification by the rule
pre-registered in PREDICTION.md section A, and list the symbolic population.

Rule (fixed in PREDICTION.md before running):
  numerical  : imports any of numpy, scipy, camb, classy, healpy, astropy
  symbolic   : not numerical, imports sympy or mpmath
  corpus     : neither, and opens corpus .tex/.md files or the git history
  arithmetic : everything else
A receipt is a .py file under receipts/, helpers and __init__ excluded.
"""
import re, sys, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parents[3]
NUM = {"numpy", "scipy", "camb", "classy", "healpy", "astropy"}
SYM = {"sympy", "mpmath"}
IMP = re.compile(r"^[ \t]*(?:from[ \t]+([A-Za-z_]\w*)|import[ \t]+([A-Za-z_][\w \t,\.]*))", re.M)  # [ \t], not \s: \s spans newlines and swallowed later imports (bug in the first run, fixed; the rule is unchanged)
CORPUS = re.compile(r"\.tex\b|\.md\b|git\s+log|subprocess.*git|['\"]git['\"]")

def modules(src):
    out = set()
    for a, b in IMP.findall(src):
        if a:
            out.add(a.split(".")[0])
        else:
            for part in b.split(","):
                part = part.strip().split(" as ")[0].strip()
                if part:
                    out.add(part.split(".")[0])
    return out

def is_receipt(p):
    n = p.name
    return n != "__init__.py" and not n.startswith("_") and "helper" not in n.lower()

def classify(p):
    src = p.read_text(encoding="utf-8", errors="replace")
    mods = modules(src)
    if mods & NUM:
        return "numerical"
    if mods & SYM:
        return "symbolic"
    if CORPUS.search(src):
        return "corpus"
    return "arithmetic"

files = sorted(p for p in (ROOT / "receipts").rglob("*.py") if is_receipt(p))
cls = {str(p.relative_to(ROOT)): classify(p) for p in files}
counts = {k: sum(1 for v in cls.values() if v == k) for k in ("numerical", "symbolic", "arithmetic", "corpus")}
n = len(files)
for k, v in counts.items():
    print(f"{k:11s} {v:5d}  {100*v/n:5.1f}%")
print(f"{'total':11s} {n:5d}")
out = pathlib.Path(__file__).with_name("symbolic_population.json")
out.write_text(json.dumps(sorted(k for k, v in cls.items() if v == "symbolic"), indent=1) + "\n")

ok_n = 1000 <= n <= 1090
ok_s = 230 <= counts["symbolic"] <= 300
print(f"receipts {n} in band 1000-1090: {'YES' if ok_n else 'NO'}")
print(f"symbolic {counts['symbolic']} in band 230-300: {'YES' if ok_s else 'NO'}")
print("VERDICT: POPULATION REPRODUCED" if ok_n and ok_s else "VERDICT: RULE DIFFERS FROM THE GATE'S -- report both")
