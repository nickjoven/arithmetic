# Boundaries of the Collatz Conjecture — an Outline from the Repository Findings

## Status / classification (read first)

**Class 2 — synthesis / roadmap. NOT a study, NOT a new claim, NOT a proof.**
This outline assembles the repository's Collatz findings into a single
progression that *arrives at the boundaries* of the conjecture — the places
where each class of method provably stops. It introduces **no new result**:
every step cites the study and check that establishes it. Status tags:

- **[established]** — a proven / machine-checked fact in a study;
- **[negative]** — a class of proof strategy ruled out, with reason;
- **[circular]** — true but presupposes the conjecture;
- **[standard]** — classical mathematics used, not a repo finding;
- **[open]** — the conjecture's live edge.

The discipline of the repo applies: weak and strong kept apart, "open" means
open, and the boundaries are negative results assembled honestly — not a path
to a proof.

---

## I. Setup — the object and its two readings

1. **The map** (shortcut form): `T(n) = n/2` if `n≡0 (2)`, `(3n+1)/2` if
   `n≡1 (2)`. Open since 1937; verified to `2⁶⁸`. **[standard]**
2. **Reading A — dynamics on the Stern–Brocot tree.** Rational extension
   `C(p/q)`; integers are the `q=1` boundary; `{1,2}` is the attractor.
   `[established — minimal_chaos.md / .py]`
3. **Reading B — the lossy mod-2 operator.** Each step reads and discards one
   parity bit. `[established — two_completions.md / .py]`

> Both readings are exact; the boundaries come from following each to where it
> stops.

---

## II. The `{2,3}` dynamics — what is *forced* vs only *statistical*

1. **Contraction rate** `q₃/q₂² = 3/4` per odd-cycle, because
   `E[v₂(3n+1)] = q₂ = 2`. `[established — minimal_chaos M2]`
2. **The transition is structural:** `q·n+1` contracts iff `q < q₂² = 4`;
   `3n+1` converges, `5n+1` diverges (1742/1998). `[established — minimal_chaos M1]`
3. **But the descent is statistical, not forced.** Altitude is *non-monotone*
   (e.g. `27 → 4616`, `77031 → 1.1×10⁷` before falling): no Lyapunov function
   in size. `[negative — no_dissipation D1]`
4. **The `+1` is the mediant with the tree root**, and it drives orbits *off*
   the mode-locked plateaus: the parity dynamics are a full 2-shift (Terras),
   maximal complexity — Collatz admits **no standing wave**.
   `[established — minimal_chaos M3, M5]`

> **First lesson:** the `{2,3}` structure explains *why* orbits descend on
> average and *where* the 3-vs-5 transition is, but supplies no forced descent.

---

## III. The two completions — where the dynamics is natural

1. **Ostrowski:** the only completions of ℚ are the Archimedean ℝ and the
   `p`-adics `ℚ_p`. `[standard]`
2. **Collatz's mod-2 lives in `ℤ₂`.** The lossy read is lossless in aggregate:
   the parity stream is a bijection on `ℤ/2ᵏ` (Terras) with exact inverse — the
   2-adic coordinate. `[established — two_completions L1]`
3. **On `ℤ₂` the map is a measure-preserving isometry** (Lagarias).
   `[established/standard — two_completions L3]`
4. **The completions disagree on dissipation:** ℝ shows statistical
   contraction; `ℤ₂` shows *zero* (an isometry). This disagreement is the root
   of every boundary below. `[established — synthesis of II.3 + III.3]`

---

## IV. Boundary #1 — the **cycle** case is CLOSED

1. The only integer cycle is `{1,2}`, because `q₃^a = q₂^b` (`3^a = 2^b`) has
   **no** positive-integer solution. `[established — minimal_chaos, no_dissipation]`
2. **Why this one closes:** a cycle is a *finite, closed, Diophantine*
   condition — a single algebraic equation — and a **uniqueness / rigidity**
   argument is exactly the right tool for it. `[synthesis]`
3. **→ The only remaining failure mode is divergence to ∞.**

---

## V. Boundary #2 — **divergence** resists every non-arithmetic tool

1. **Measure / ergodic theory — BLOCKED.** `ℤ₂` is measure-preserving →
   Poincaré recurrence → a.e. orbit *recurs forever* (never converges); the
   integers are **dense but measure-zero**, so convergence is invisible to the
   Haar measure. "Almost all" (Tao 2019) cannot be upgraded to "all" by any
   measure argument. `[negative — no_dissipation D2]`
2. **Geometry / topology — WRONG COMPLETION.** The holomorphic extension to ℂ
   agrees on integers but diverges super-exponentially off-axis (no conserved
   current); and `q₂ = 2` **ramifies** (`−i(1+i)² = 2`), the non-Archimedean
   fact that Archimedean ℂ/ℍ cannot see. No higher-dimensional geometric
   embedding supplies a forcing conservation law. `[negative — no_dissipation D3]`
3. **Forced dissipation (a Lyapunov function) — absent in either completion
   alone.** ℝ gives only the non-monotone, statistical drift (II.3); `ℤ₂` gives
   the isometry (III.3). A forcing quantity must be **adelic**. `[negative → VI]`

---

## VI. The adelic frontier — the **squeeze**

1. **A monotone height exists iff Collatz is true.** The stopping time `σ(n)`
   satisfies `σ(T(n)) = σ(n)−1` exactly — a perfect Lyapunov function, but
   defining it presupposes the orbit reaches 1. `[circular — adelic_height [0]]`
2. **A closed-form `h(|n|, v₂-data)` is squeezed:**
   - finite 2-adic data is **blind to the climbs** — `n = 2ᵏ−1` gives `k`
     consecutive odd steps with `v₂ ≡ 0` while `log|n|` rises; runs are
     unbounded. `[negative — adelic_height [1]]`
   - the **full** 2-adic coordinate is **conserved** (isometry) — a continuous
     `h:ℤ₂→ℝ` strictly decreasing is impossible (recurrence).
     `[negative — adelic_height [2]]`
3. **All *local* arithmetic is blind** — `v₃(n)` is also `0` along the climb;
   the best `log₂n − α·v₂ − β·v₃` keeps `β=0`. The climb is the *accumulated
   `×3` count* — a **trajectory** quantity, not a local function of `n`.
   `[negative — adelic_height [3], [3b]]`
4. **→ Precise boundary:** any non-circular `h` must be *Archimedean-non-
   monotone* **and** *2-adically discontinuous* — definable on **neither**
   completion, living only on the **measure-zero integers**, where real
   analysis and 2-adic/ergodic theory both fail to apply.
   `[established characterization — adelic_height [4]]`

---

## VII. The outer boundary — what *kind* of argument could remain

1. **Uniqueness vs self-consistency** (the IV/V asymmetry, generalized):
   - cycles fell to **uniqueness** because they are a *finite/closed*
     condition;
   - divergence is an *infinite/open* condition, with no algebraic uniqueness
     handle. `[synthesis]`
2. **The natural self-consistency law is vacuous.** The adelic **product
   formula** `∏_v |x|_v = 1` (the law tying the Archimedean size to all
   `p`-adic valuations) holds *identically* for every rational — verified on
   orbit terms — so it is satisfied by every step of every orbit and adds **no
   dynamical constraint**. `[established (identity); standard]`
3. **→ Outer boundary:** a proof, if one exists, must be **arithmetic** —
   control of the *measure-zero exceptional set* (the integers whose 2-adic
   parity statistics deviate) — not dynamical, geometric, or measure-theoretic.
   This is Tao's frontier, restated as an arithmetic-not-dynamical problem.
   `[open]`

---

## VIII. Map of the boundaries (summary)

| failure mode → method | verdict | where |
|---|---|---|
| **cycle** → uniqueness (`3^a≠2^b`) | **CLOSED** | IV |
| divergence → measure / ergodic | **BLOCKED** (measure-zero) | V.1 |
| divergence → geometry / topology (ℂ, ℍ) | **BLOCKED** (wrong completion) | V.2 |
| divergence → closed-form / local height | **BLOCKED** (the squeeze) | VI |
| divergence → self-consistency (product formula) | **VACUOUS** (identity) | VII.2 |
| **divergence**, *in toto* | **OPEN** — reduces to an arithmetic statement about a measure-zero set | VII.3 |

**The boundary, in one line:** *Collatz's cycle case is closed by arithmetic
uniqueness; its divergence case is walled off from every dynamical, geometric,
and measure-theoretic tool — because the truth is a measure-zero phenomenon
visible to neither completion — and what remains is an arithmetic statement
about that measure-zero set, for which no uniqueness or (non-vacuous)
self-consistency handle is known.*

---

## Honest scope

- **Synthesis only.** No new claim; every leaf cites a study + check (or a
  standard fact). The boundaries are the repo's *negative results* assembled
  into a map.
- It does **not** prove Collatz, nor prove it unprovable. "BLOCKED" means a
  *class of strategy* is ruled out with reason; "OPEN" means open.
- Classical inputs (Ostrowski, Lagarias' conjugacy, Tao's a.e. result, the
  ℂ extension, the product formula) are used, not claimed as repo findings.

## Sources (all in this repo unless noted)

`minimal_chaos.{md,py}` (II, IV) · `../completion/two_completions.{md,py}` (III) ·
`no_dissipation.{md,py}` (II.3, V) · `adelic_height.{md,py}` (VI) · the
product-formula identity (VII.2, standard). External: Terras 1976, Lagarias
1985, Tao 2019, Ostrowski; harmonics `minimum_alphabet.md` (`q₂=2, q₃=3`).
