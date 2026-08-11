---
name: setup-the-repo
kind: METHOD
current: c54.163
job: THE STANDING INSTRUCTIONS for creating the GitHub repository and giving this line access to it. Gated on Daryl being at a computer, or on the decision to publish. ASK FOR THIS BY NAME — "dig up the repo instructions".
sources: [chat]
---

# SETUP THE REPO — standing instructions, for when you are at a computer

> **⌗ WHY THIS IS A DOCUMENT AND NOT A MESSAGE.** *Written r2409 while you were outside on a phone, and filed
> here so it survives every session boundary.* **Ask for it by name — "dig up the repo instructions" — and it
> comes back whole.** *It is gated on **either** trigger: you at a computer, **or** the decision to publish.*

---

## ⛭⛭ READ THIS FIRST — IT DECIDES THE REST

**There is one real decision and it is about ACCESS, not about git.**

| | **PUBLIC repo** | **PRIVATE repo** |
|---|---|---|
| *how this line reaches it* | ***`git clone https://…` — no credential at all*** | *needs a **token pasted into the session*** |
| *what that costs* | **nothing** | ⚠ ***the token then lives in a chat transcript*** |
| *what it exposes* | the whole corpus, the register, every withdrawn result | nothing |

⇒ ***PUBLIC IS DRAMATICALLY SIMPLER FOR ACCESS, AND THAT IS A REAL INPUT TO THE PUBLISH DECISION — but it must
not be the DECIDING one.*** *If you want the repo private for now, use a **fine-grained, single-repo,
short-expiry** token and **revoke it when the session ends**; that is a workable but genuinely worse hygiene
story, and I would rather say so than let convenience make a publication decision for you.*

**⌗ AND IF YOU GO PUBLIC, KNOW WHAT GOES WITH IT** *(none of this is a reason not to — several are reasons to):*
*· **`THE_BASE_RATE`** scores the corpus's own Rule-2 arguments and marks one **"on the unfavourable side, and
should be watched."***
*· **the c54.153 capstone** opens with **"14 results that stand · 13 things withdrawn"** and calls one of its own
receipted claims unbacked.*
*· **`CORPUS_MAP`** carries every correction, including this line's own — a file overwritten to 213 bytes, a
premature closure retracted, three structured-edit failures.*
*· **`PROTECTED_OPEN`** names what the construction cannot yet do, by name.*
⇒ ***That is the corpus's honesty showing, and it is the strongest thing about it.*** *But publish it knowingly
rather than as a side-effect of wanting an easy clone.*

---

## ① PREREQUISITES — five minutes

```bash
git --version                 # any modern git
git lfs version               # if missing: brew install git-lfs   /   apt install git-lfs
git lfs install               # once per machine
```

*A GitHub account. **Free tier is fine**: the binaries are ~41 MB against LFS's 1 GB free storage.*

## ② CREATE THE REPO ON GITHUB

*Web UI → **New repository**.*

| field | value |
|---|---|
| name | `cosmological-relativity` *(or your preference)* |
| visibility | **Private** *(or Public — see the decision above)* |
| initialise with README | ***NO*** — *the tree already has everything* |
| add .gitignore / licence | ***NO*** — *`.gitignore` and `.gitattributes` are already in the tree* |

## ③ UNPACK A CUT AND MAKE IT THE REPO

*Use the **newest bundle** — both parts, extracted into one directory.*

```bash
mkdir cr && cd cr
tar xzf ~/Downloads/cr_r2408_part1_corpus.tar.gz
tar xzf ~/Downloads/cr_r2408_part2_rest.tar.gz
cd cr_r2408                      # the tree; .gitignore/.gitattributes/.github are inside it

git init -b main
git lfs track                    # reads .gitattributes; confirms pdf/png/eps/dat are tracked
git add -A
git commit -m "r2408 — the consolidated corpus, twenty-one gates, the entry-point front worked once through"
git remote add origin https://github.com/<you>/cosmological-relativity.git
git push -u origin main
```

⚠ ***If the push is rejected for size***, *it means LFS did not pick the binaries up.* **Check `git lfs ls-files`
before pushing** — *it should list the PDFs, PNGs, the `.eps` and the Planck `.dat`. If it is empty, run
`git lfs install` again and re-add.*

## ④ THE BRANCHES

```bash
git branch line/56              # this line
git push -u origin line/56
# line/54 is created when the fork joins — that is first contact, and it is your call when
```

*`THE_HUB.md` in the tree carries the full discipline: branch layout, the **reserved ID bands**, why
`merge=union` is on four files and no others, and what CI enforces.*

## ⑤ CONFIRM CI RAN

*`.github/workflows/gates.yml` runs on the first push.* **Actions tab → the `fast` job should be green**: *seven
view-checks, fifteen gates, the hollow-assertion lint.* ⌗ *`compile` (LaTeX, minutes) runs on `main` and
nightly; `receipts` (~9 min, installs `camb` and `pynucastro`) runs nightly — **and that is the tier this
container cannot run at all**, so its first green is a genuinely new fact about the corpus.*

## ⑥ GIVE THIS LINE ACCESS

**If PUBLIC** — *nothing to do.* **Just tell me the URL** *and I will clone it.*

**If PRIVATE** — *GitHub → Settings → Developer settings → **Fine-grained personal access tokens** → Generate:*
*· **Repository access:** only this repo. · **Permissions:** Contents **read** (add **write** only when you want
me pushing). · **Expiry:** 7 days, or the shortest that covers the session.*
⚠ ***Paste it into the session when you want me to use it, and REVOKE it afterwards.*** *Treat it as burned once
sent.*

---

## ⌗ WHAT I WILL DO ONCE I HAVE ACCESS

*① clone · ② run the full suite against the clone to confirm the repo is the tree and not a copy of it · ③ from
then on, **cut = commit**, and the `out*/` bundles become a fallback rather than the channel.*
⌗ *And when 54 joins: **absorption becomes `git merge line/54`**. `audit_trail.py` stays — it reports **register
deltas, frontier departures and grain currency**, which `git diff` does not — but the pristine-baseline
discipline, `reapply_annotations` and the duplicate sweep all become unnecessary, because* ***git does those
three by construction.***

## ⚠ THE ONE THING THE REPO DOES NOT CHANGE, restated because it will be assumed away

***Every defect the r2377–r2408 consolidation found was SEMANTIC, and git merges text, not meaning.*** *`PO-8`
open beside a struck row; a pointer at a struck `L-164`; "seven families are open" naming two that closed; a
verdict written where no parser reads it; a heading indexed as a door; 95 receipts that ran green and could not
fail.* **Git would have caught none of them.** ⇒ **The gates are the load-bearing part. The repo makes them run
on every push instead of when someone remembers — which is the whole of what it buys, and it is worth a lot.**
