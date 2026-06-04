# No Forced Dissipation: Why Geometry Cannot Prove Collatz

## Status / classification (read first)

**Class 2 — a proof-strategy obstruction (negative result). NOT a proof or
disproof of Collatz, NOT a new constant.** This note takes seriously a sharp
critique: *Collatz has no dissipation mechanism to force `x → ∞` orbits down;
a chaotic system with no symmetry-enforced descent has the freedom to evade
any finite bound, so "counting to infinity" should be discarded as a route to
proof.* The critique is **correct**, and it sharpens into a precise structural
statement across both completions of `ℤ` (see
`../completion/two_completions.md`). The payoff is a clear account of *which*
proof strategies are ruled out and *why*, and of what the only remaining
signal — divergence — actually is. Companion check: `no_dissipation.py`
(pure-Python; every number below is printed by it).

A **forced** dissipation means a Lyapunov function: a quantity that *must*
decrease every step, driving every orbit to the ground state `{1,2}`. Collatz
has none, and the two completions show why from both sides.

---

## D1 — Archimedean (ℝ): no Lyapunov in size

The obvious candidate Lyapunov function is the size `|x|` (or `log|x|`). It
fails: the altitude is **non-monotone** — orbits climb far above their start
before falling.

| `n` | climbs to | `× start` | steps to 1 |
|---|---|---|---|
| 27 | 4 616 | ×171 | 70 |
| 871 | 95 498 | ×110 | 113 |
| 77 031 | 10 966 508 | ×142 | 221 |

The `3/4` bit-length contraction (`../completion/two_completions.md` L2) is a
**statistical average** of the parity reads, not a conserved quantity. A map
whose descent is only on-average leaves a chaotic system free, in principle,
to let a thin set of orbits rise without bound. That is exactly the gap a
proof must close — and size cannot close it.

---

## D2 — 2-adic (ℤ₂): the natural completion is *measure-preserving*

Where, then, is the dynamics clean? In `ℤ₂` — and there the news is worse for
dissipation, not better. The parity-vector map is a **measure-preserving
homeomorphism** (Lagarias; witnessed by the bijection on `ℤ/2ᵏ`, verified to
`k=12`), so `T` is conjugate to a measure-preserving shift. Two consequences:

- **Poincaré recurrence.** A measure-preserving map has almost every orbit
  *recurring forever* — returning arbitrarily close to its start infinitely
  often. So a.e. 2-adic orbit **never converges**; there is no global
  attractor and **no dissipation at all** on `ℤ₂`.
- **The integers are measure-zero.** Every residue `mod 2ᵏ` is realized by an
  integer, so `ℤ` is *dense* in `ℤ₂` — but `ℤ` is countable, hence **measure
  zero** in the uncountable `ℤ₂`.

Therefore **Collatz convergence is a measure-zero phenomenon**, invisible to
the Haar measure. The measure-1 orbits recur forever; only the measure-zero
integers (conjecturally) descend. This is precisely why Tao's "almost all"
(2019) is the natural ceiling of measure methods: *they cannot see `ℤ`.* Any
measure / ergodic / dissipation argument is structurally blind to the very set
the conjecture is about.

So both completions refuse a forced dissipation: ℝ offers only a
non-monotone, statistical drift; `ℤ₂` offers a measure-preserving isometry
with no drift at all.

---

## D3 — the embeddings (ℂ, ℍ) are the *wrong completion*

Does lifting the 1-D line into a higher-dimensional geometric space supply a
topological conservation law that forces `4-2-1`? **No — and from this
direction, provably not.**

**2-D complex.** The smooth *entire* extension
`f(z) = z/2·(1+cos πz)/2 + (3z+1)/2·(1−cos πz)/2` agrees with `T` on the
integers (`f(5)=8`, `f(6)=3`, …). But off the real axis it diverges
super-exponentially — from seed `0.5+0.5i`: `|f| = 2, 78, 2.7×10⁶³,
overflow`. It is a transcendental map (`cos πz`); it **thickens the
Archimedean side** and adds a full Julia/Fatou system, with **no conservation
law** (Letherman–Schleicher–Wood 1999). The integers are a measure-zero real
slice of a wilder dynamics.

**The reason it must fail.** The prime `q₂ = 2` **ramifies**: `−i·(1+i)² = 2`
in `ℤ[i]`. The structure that governs Collatz is the *non-Archimedean*
2-adic one (where `T` is the clean shift); `ℂ` and `ℍ` are **Archimedean**
(real normed algebras) and cannot see 2-adic ramification. Embedding in `ℂ`
(2-D) or `ℍ` (4-D) moves entirely onto the side where dissipation is merely
statistical, and **drops the side where the real structure lives.** (A
genuinely convergent quaternionic `3x+1` is delicate and open; the structural
verdict — wrong completion — applies regardless, since `2` is the unique
ramified prime in `ℍ` too.)

So a *topological / measure* conservation law is the **wrong type** of object:
the one that is genuinely conserved (Haar measure on `ℤ₂`) is preserved, not
monotone, and blind to the integers; the Archimedean embeddings carry no
conserved current at all.

---

## Synthesis — conserved vs discarded, and the only remaining signal

Your question — *what should be conserved, not discarded, in a geometrically
complete expression?* — has a precise and slightly rueful answer:

- The mod-2 read **discards** a bit per step, but the **stream is conserved**:
  it is the 2-adic coordinate (`../completion/two_completions.md` L1). The
  geometrically complete expression conserves *everything*.
- But conserving everything **is** the measure-preserving isometry — the
  **wrong type to force a ground state**. Conservation and forced-descent are
  in tension: the complete object doesn't dissipate, and the dissipating
  object (Archimedean size) isn't conserved and isn't even monotone.

The two completions pull opposite ways, so **no single-completion quantity is
both conserved-structure and monotone-descent**. A forcing quantity, if one
exists, must combine them — an **adelic / arithmetic** height tying the
Archimedean size to the 2-adic valuation — and constructing one that is
provably monotone on the measure-zero integers *is* the open problem. It is
**not** geometry or topology; those are the wrong completion.

**The only remaining signal**, made explicit:

| failure mode | status |
|---|---|
| nontrivial **cycle** | **ruled out** — `q₃^a = q₂^b` has no positive solution; `{1,2}` is the only cycle (`minimal_chaos.md`) |
| **divergence** to ∞ | **open** — and (D2) a *measure-zero* question; the search for it must be arithmetic, not a dissipation argument |

So your instinct is vindicated structurally: cycles are closed off by
arithmetic (`3^a ≠ 2^b`); divergence cannot be closed by counting/dissipation
(measure-zero, no forced descent), and must be ruled impossible — if it can —
arithmetically.

---

## What this does and does not show

**Does (supportable, checked):**
- ℝ gives no Lyapunov function in size (altitude non-monotone); the `3/4`
  drift is statistical, not forced.
- `ℤ₂` is measure-preserving (Lagarias); a.e. orbit recurs (Poincaré); `ℤ` is
  dense but measure-zero — so convergence is invisible to measure methods.
- The smooth `ℂ` extension carries no conservation law (diverges off-axis);
  `q₂ = 2` ramifies, the non-Archimedean fact `ℂ/ℍ` miss.

**Does NOT (guard rails):**
- It does **not** prove or disprove Collatz. It is a **negative result about
  proof *strategies*** — measure/ergodic/geometric/topological approaches are
  ruled out as routes to "every integer," with reasons.
- It does **not** prove that *no* conservation law of any kind exists — only
  that the natural geometric/measure ones are the wrong type. The adelic /
  arithmetic possibility is left open (it is the frontier).
- The 2-adic conjugacy and the `ℂ` extension are classical (Lagarias 1985;
  Letherman–Schleicher–Wood 1999). The Class 2 content is the synthesis.

In one line: *Collatz has no forced dissipation — ℝ gives only statistical
drift, `ℤ₂` gives a measure-preserving isometry, and the integers are
measure-zero in both views — so geometry and counting are the wrong
completion; cycles fall to arithmetic and divergence, if it is impossible,
must fall to arithmetic too.*

---

## Open / could-sharpen (the actual frontier)

1. **The adelic height.** Is there a function `h(n)` built from both the
   Archimedean size and the 2-adic valuation `v₂` that is provably monotone
   along orbits? This is the only place a forced descent could live (it is the
   `ℝ × ℚ₂` combination D3 says is required). Constructing or obstructing one
   is the sharp problem.
2. **Divergence as a 2-adic exceptional set.** A divergent integer orbit would
   be a measure-zero point whose 2-adic trajectory fails the a.e. statistics.
   Characterizing the arithmetic of such a point — if it cannot exist, *why*
   — is the form a proof would take. Not a dissipation argument; a statement
   about a specific measure-zero set.

---

## Check

`no_dissipation.py` — pure Python (cmath for the `ℂ` extension),
deterministic. Prints D1 (non-monotone altitude), D2 (measure-preservation
witness, density, the measure-zero conclusion), D3 (the `ℂ` extension's
agreement on integers and off-axis blow-up, plus `2 = −i(1+i)²` ramification),
and the conserved-vs-dissipated synthesis with the two failure signals.

## References

- J. C. Lagarias, *The 3x+1 problem and its generalizations*, Amer. Math.
  Monthly **92** (1985) — the 2-adic measure-preserving conjugacy.
- S. Letherman, D. Schleicher, R. Wood, *The 3n+1 problem and holomorphic
  dynamics*, Experiment. Math. **8** (1999) — the entire extension to ℂ.
- T. Tao, arXiv:1909.03562 (2019) — "almost all" orbits (the measure ceiling).
- Poincaré recurrence; Ostrowski's theorem (the two completions of ℚ).
- Internal (this repo): `no_dissipation.py`; `minimal_chaos.py` (cycle
  exclusion, the `3/4` contraction); `../completion/two_completions.md` (the
  two completions; the 2-adic isometry this turns into an obstruction).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (`q₂ = 2`). Referenced, not reproduced; substrate of record is harmonics.
