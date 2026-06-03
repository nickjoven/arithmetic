# The Farey Tree's Two Faces: Counting (Locked) and Equidistribution (Riemann)

## Status / classification (read first)

**Class 2 — structural reading / capstone. NOT a test of RH, NOT a new
constant.** This note places the three objects this repo studies on a
single axis — the **locked** face of the Farey/Stern–Brocot tree (finite-
depth *counting*, where the framework's `{2,3}` quantities live) versus its
**unlocked** face (asymptotic *equidistribution*, where the Riemann
Hypothesis lives via Franel–Landau). It records that the framework reaches
the locked face and not the unlocked one, and that RH keeps company there
with Collatz. It does **not** test RH: finite computation is only ever
*consistent with* it. Companion check: `equidistribution.py` (pure-Python,
deterministic; every number below is printed by it).

This is the capstone of the locked-vs-unlocked register:

| study | face | what it is |
|---|---|---|
| `../mode_locking/standing_waves.md` | **locked** | the `{2,3}` resonances — standing waves of the staircase |
| `../collatz/minimal_chaos.md` | **unlocked** (dynamical) | orbits that lock onto no standing wave |
| **this note** | **unlocked** (asymptotic) | RH = the fractions equidistribute maximally |

---

## The object

The Stern–Brocot / Farey tree enumerates `Q ∩ [0,1]` by mediants. Two
genuinely different questions can be asked of it.

**Counting (the locked face).** `|F_n| = 1 + Σ_{k≤n} φ(k)` is the number of
Farey fractions up to denominator `n` — equivalently the number of
mode-lock centres (Arnold-tongue centres) resolved at depth `n`. It is
exact, local, finite. The framework's structural quantity is read here:

    Ω_Λ = |F₆| / |F₇| = 13/19 = 0.684211     (a depth-6 census)

**Equidistribution (the unlocked face).** As `n → ∞`, how uniformly do the
Farey fractions fill `[0,1]`? This is the depth→∞ continuum limit — the
"completion of `Q`" of `harmonics:minimum_alphabet.md` Part III — and it is
where the Riemann Hypothesis lives:

> **Franel (1924) / Landau.** With `δ_ν = ρ_ν − ν/N` the deviation of the
> `ν`-th Farey fraction from its uniform position, **RH** is *equivalent* to
> the Farey fractions being equidistributed to the maximal degree:
> `Σ_ν |δ_ν| = O(n^{1/2+ε})` (Landau form) and `Σ_ν δ_ν² = O(n^{-1+ε})`
> (Franel form).

The same tree; the count is combinatorial and finite, the equidistribution
is analytic and asymptotic.

---

## What running the tree shows

### The locked face is finite-depth — and depth-specific

`13/19` is exact at depth 6, but it is **not** an asymptotic invariant. The
ratio `|F_n|/|F_{n+1}|` drifts to 1 as the tree deepens:

| `n` | `|F_n|/|F_{n+1}|` | |
|---|---|---|
| 6 | 0.68421 | ← the framework's operating depth (`= 13/19`) |
| 20 | 0.91489 | → 1 |
| 100 | 0.96820 | → 1 |
| 400 | 0.99185 | → 1 |

So the locked face carries the framework's structural quantity **because it
is read at a specific finite depth**. It says nothing about the `n → ∞`
behaviour — that is a different face.

### The unlocked face stays within the RH bounds

Computing the Franel–Landau sums directly (`equidistribution.py`):

| `n` | `|F_n|` | `S1 = Σ|δ|` | `S1/√n` | `S2 = Σδ²` | `S2·n` |
|---|---|---|---|---|---|
| 8 | 23 | 0.5545 | 0.196 | 0.024152 | 0.193 |
| 32 | 325 | 1.5137 | 0.268 | 0.014786 | 0.473 |
| 128 | 5023 | 2.3742 | 0.210 | 0.004334 | 0.555 |
| 512 | 79853 | 4.0988 | 0.181 | 0.001220 | 0.625 |

`S1/√n` stays bounded (no `n^{1/2+ε}` blow-up) and `S2·n` stays bounded
(slowly creeping, consistent with the `O(n^{ε})` slack the Franel form
allows). Both are **consistent with RH** — and that is *all* a finite
computation can be. Every finite `n` is consistent with RH *and* with its
negation; the theorem is a statement about the limiting rate, which no
finite table decides.

---

## What this does and does not show

**Does (supportable, checked):**
- The Farey tree carries two distinct structures: a finite-depth **count**
  (`|F_n|`, the framework's `13/19`) and an asymptotic **equidistribution**
  (the `δ_ν` sums) that is *equivalent to RH* by Franel–Landau.
- The framework's quantity is a depth-6 census; `|F_n|/|F_{n+1}| → 1`
  confirms it is depth-specific, not an asymptotic invariant.
- The computed equidistribution sums stay within the RH-predicted bounds
  over the range checked.

**Does NOT (guard rails):**
- It does **not** test, support, or weigh on RH. Consistency over finite
  `n` is not evidence; it is the absence of a finite counterexample, which
  RH-true and RH-false both predict in this range.
- It does **not** claim the framework derives, or bears on, RH. The framework
  reads the locked/counting face; RH is the unlocked/asymptotic face. They
  share the tree, not a theorem.
- It adds **no** constant and **no** scorecard claim. `13/19` is imported as
  a harmonics quantity (and its physical status is audited there, not here).

In one line: *the framework and RH read the same Farey tree from opposite
faces — finite count versus asymptotic equidistribution — and the
framework's finite-depth machinery does not reach the face RH lives on.*

---

## The register, completed

The repo's organizing axis is **locked vs unlocked**: the mode-locked
standing waves of the `{2,3}` staircase, and the unlocked complement
between them. The three studies fill it out:

- **Locked** — `mode_locking/standing_waves.md`: the `{2,3}` resonances are
  the widest Arnold tongues; the framework's forced structure (and its
  finite-depth Farey *count* `13/19`) lives on this face.
- **Unlocked, dynamical** — `collatz/minimal_chaos.md`: Collatz orbits lock
  onto no standing wave (Terras full shift); they inhabit the *gaps*.
- **Unlocked, asymptotic** — this note: RH is the statement that the Farey
  fractions fill the continuum as uniformly as possible (Franel–Landau).

Collatz and Riemann are the two unlocked problems — one about whether a
*dynamics* ever locks, one about how uniformly the *static* tree
equidistributes — and both concern the part of the structure the
framework's finite-depth counting does not reach. That is the honest shape:
the framework owns the locked census; the open problems live in the
unlocked completion.

The third object, **Ramanujan's 1/π** (modular face), is *not* ported here:
its harmonics-branch reading leans on the claim that the framework "forces
`Γ₀(6)` from physics," which the audit (`../MANIFEST.yml` →
`audit_findings.gamma0_6_forcing`) found the substrate does not support
(`Γ₀(6)` is *identified* by candidate-splitting + `INTERACT`-match, not
forced). It returns only after that layer is downgraded.

---

## Open / could-sharpen

1. **The completion as the bridge.** `minimum_alphabet.md` Part III lists
   "formalize the completion of `Q` as a limiting process on the
   Stern–Brocot tree" as **Open**. RH (via Franel–Landau) is a concrete,
   sharp property *of that completion*. If the completion were formalized
   framework-side, RH would be the natural test question for it — not to
   prove, but to state in framework-native terms. This is the one place the
   two faces could be made to touch.
2. **Locked-measure at criticality.** The `mode_locking` study's `K = 1`
   staircase has its locked plateaus covering measure 1 with a measure-zero
   gap set; the Farey tongue-width sum (a `Σ 1/q²`-type quantity) is the
   exact statement, and it is the same `|F_n|`/totient machinery as the
   locked face here. Tying the two `|F_n|` computations together would unify
   the locked face across the two studies.

---

## Check

`equidistribution.py` — pure Python, no numpy, deterministic. Prints the
locked face (`|F₆|, |F₇|, 13/19`, and the depth-specific drift of
`|F_n|/|F_{n+1}|`), the unlocked face (the Franel–Landau sums `S1, S2` with
their RH-bound normalizations), and the two-faces synthesis positioning
Collatz and Riemann on the unlocked side.

## References

- J. Franel, *Les suites de Farey et le problème des nombres premiers*,
  Göttinger Nachr. (1924); E. Landau, companion note same volume — the
  RH ⇔ Farey-equidistribution equivalence.
- Internal (this repo): `equidistribution.py`; companions
  `../mode_locking/standing_waves.md` (locked face) and
  `../collatz/minimal_chaos.md` (unlocked dynamical face).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (Stern–Brocot tree, the completion of `Q` as the continuum limit, Part
  III), `farey_partition.md` (`|F₆| = 13`, `Ω_Λ = 13/19` as a depth-6
  count), `canonical_glossary.md` §5 (Farey counts). Referenced, not
  reproduced; the substrate of record is harmonics, and the physical status
  of `13/19` is audited there, not asserted here (see `../README.md`).
