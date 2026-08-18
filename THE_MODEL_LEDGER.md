---
name: the-model-ledger
description: Binds every adjustable term in RADSCAN.py to the theory statement that determines it, and records what the theory says versus what the run does. Read this BEFORE changing any switch; it is the thing that stops the modelling becoming a fishing expedition.
sources: [observer]
current: r3045
---

# ▣ THE MODEL LEDGER — every switch, and what the theory says about it

***The problem this solves: for twenty revisions I varied terms without holding what the framework says
they are, and read physical conclusions off my own edits. This table makes that impossible to repeat.***

**⚙ THE RULE:** *a switch is **DETERMINED** if the corpus fixes it, **OPEN** if it does not. **A run that
needs a DETERMINED switch off its determined value is evidence about the implementation or the theory —
never a free parameter.** Say which before changing it.*

---

| switch | what it controls | theory | value | source |
|---|---|---|---|---|
| **`RATE`** | radiation in the expansion rate | **DETERMINED — `0`** | *the expansion is a property of the **layer sequence**, how $h_t$ evolves in cosmic time; it is geometric because the layers are. Radiation is layer **content**, not layer **evolution**.* | *P7 layered-framework axioms; `eq:rate` states $H^2=\tfrac13(8\pi G\rho+\Lambda c^2)$ as **what the law satisfies**, matter and $\Lambda$ only* |
| **`SRC`** | photons + neutrinos source the potential | **DETERMINED — `1`** | *the plasma lives **on** a layer; its dynamics are ordinary physics on $(S_t,h_t)$ and **every content sources them***. **A valid projection must "faithfully encode SIGNAL PROPAGATION"** — which is the acoustic physics itself. | *P7 projection principle* |
| **`NU`** | neutrinos present | **DETERMINED — `1`** | *same as `SRC`: neutrinos are layer content.* ⚠ *`fnu=0.4052` is hardcoded and **not traced to a source** — the fraction is unverified even though its presence is determined.* | *same; the value is **UNTRACED*** |
| **`TOT`** | radiation in the $\Omega$ denominator $r_t$ | ⛔ **OPEN — and it is THE DEFECT** | *this is the term that disagrees with `RATE`. The rate's own total is $r_H=\Omega_m/a^3+\Omega_\Lambda$; $r_t$ adds radiation to it. **Every $\Omega$ in the potential source inherits the mismatch.** Setting it to $0$ makes the fractions consistent with the rate and **loses the spectrum's structure** (r3038/r3041) — so consistency alone does not rescue it.* | *r3041: the ratio is $4.57$ at onset, $2.15$ at recombination* |
| **`MAT`** | matter fraction's denominator ⚠ **and whether $\Omega_m$ is a gravitating fraction at all** | ⚠ **OPEN — currently `1`, and r3046 raises the deeper question** | *the fractions are $\rho_i/\rho_{\rm tot}$, and **which total** depends on what the $(3H_c^2/2)\Omega$ conversion is allowed to assume. **This is the site of the $r_t$-vs-$r_H$ inconsistency** (r3041).* | *unresolved: the rate excludes radiation, the denominator includes it* |
| **`CS`** | baryon loading in the sound speed | **DETERMINED — `1`** | *$R_b$ is the photon–baryon ratio of the actual plasma. Ordinary layer physics.* | *standard, and `Rb_rec` is derived from $\omega_b$ in-code* |
| **`LA`** | the acoustic-scale target the seam datum is solved to | ⚠ **OPEN — currently `301.6`** | ***this is a TARGET, not a prediction**: $z_{\rm onset}$ is root-found to hit it. Every "the scale comes out right" statement traces here.* | *r3026* |

---

## ⛔ THE ONE INCONSISTENCY THE LEDGER MAKES UNAVOIDABLE

*`RATE=0` (determined) says the rate carries no radiation. The $\Omega$ denominator $r_t$ **does** carry
it. So $4\pi Ga^2\rho_i=(3H_c^2/2)\Omega_i$ — **the conversion the potential source uses** — is
**inconsistent by the ratio $r_t/r_H$**, which is $4.57$ at onset and $2.15$ at recombination (r3041).*

⇒ ***That is not a knob. It is a defect, it is in `MAT`'s row, and it is the first thing to fix.***

## ⌗ WHAT THE SCAN SAYS, HELD AGAINST THE THEORY

| setting | positions | height | ledger verdict |
|---|---|---|---|
| shipped | $150/360/555/780$ | $1.447$ | *all determined switches at their values — **and it does not fit*** |
| `RATE=1,NU=0` | $225/510/780$ | $3.652$ | ***two DETERMINED switches violated**. Good positions are a symptom, not a result* |
| `RATE=1,MAT=0` | $240/555/810$ | $7.323$ | *one determined violated, one open moved* |
| `SRC=0` | $300/525/780$ | $1.971$ | ***a DETERMINED switch violated**; best height so far, and inadmissible as physics* |

**⇒ THE SHAPE OF THE PROBLEM, STATED HONESTLY:** *every setting that improves the fit **violates a
determined switch**. The all-determined configuration is the shipped one, and it is the worst. **Either
the implementation misplaces something the switches do not expose, or a determined value is wrong.**
Those are the only two options, and the ledger is what keeps them apart.*
