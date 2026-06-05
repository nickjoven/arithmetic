# The Completion of ℚ as the Boundary of the Stern–Brocot Tree

## Status / classification (read first)

**Class 2 — structural reading that *resolves* a framework Open item.**
`harmonics:minimum_alphabet.md` Part III lists, under **Open**: *"formalize
the completion [of ℚ to the reals] as a specific limiting process on the
Stern–Brocot tree."* This note records that the formalization is **classical
and exact** — the boundary of the SB tree *is* the completion `R≥0`, with the
continued fraction as the path encoding — and that four of the framework's
informal claims (the resolution floor `1/q²`, completion-as-limit,
`0.999…=1` as the ψ-mode, and `1/φ` as the deepest structure) land on four
standard facts about it. The framework does **not** derive this; it **adopts**
a known construction as the rigorous home for claims it had been stating
informally. No new constant, no scorecard claim. Companion check:
`sb_boundary.py` (pure-Python, exact integer arithmetic; prints every number
below).

This is the study where the repo's two faces **meet**. Rationals are the
tree's finite nodes (the locked mode-lock centres); irrationals are its
infinite paths (the unlocked gaps); and the **completion is their union — the
boundary `∂T`**. The earlier studies live *on* the faces; this one is the
closure that contains both.

---

## The construction (all standard, all checked)

The Stern–Brocot tree generates every positive rational once by mediants,
bracketing each target between two neighbours `a/b < c/d`.

### C1 — the resolution floor is the bracket width `1/(bd)`

Every tree-adjacent pair is **unimodular**: `|bc − ad| = 1` at every node
(verified for `√2, φ, π, e` to depth 30). Therefore the interval they bound
has width

    |a/b − c/d| = (bc − ad)/(bd) = 1/(b·d).

This is not an analogy for the framework's *"smallest resolved interval ~
1/q²"* (`minimum_alphabet.md` Part III, the Planck/UV floor) — it is the same
quantity. The tree's resolution at a node *is* `1/(bd)`, and the floor falls
as the denominators grow down a path.

### C2 — the completion is the limit of mediants

Descending toward a real `x`, the bracketing intervals are nested and shrink
to `{x}` — a Cauchy / nested-interval limit. Two exact facts make this the
continued fraction:

- the **L/R path's run-lengths are `x`'s CF coefficients**, and
- the **bracket endpoints are `x`'s convergents** `p_k/q_k`, with width
  `1/(q_k q_{k+1})`.

| `x` | CF (first 6) | convergent `p₅/q₅` | floor `1/(q₅q₆)` |
|---|---|---|---|
| `φ` | `[1,1,1,1,1,1]` | `8/5` | `2.5e-2` |
| `√2` | `[1,2,2,2,2,2]` | `41/29` | `4.9e-4` |
| `π` | `[3,7,15,1,292,1]` | `103993/33102` | `9.1e-10` |
| `e` | `[2,1,2,1,1,4]` | `19/7` | `4.5e-3` |

The continuum is *reached as this limit* — "completion of ℚ," concretely, on
the tree. (`π`'s tiny floor reflects its `292` coefficient: the bracket
collapses where a real is exceptionally well-approximated, e.g. `355/113`.)

### C3 — the two tails are the tree's `0.999… = 1`

A rational has **exactly two** finite paths — `[a₀;…,aₙ]` and
`[a₀;…,aₙ−1,1]` (or `[…,k,1] = […,k+1]`) — both descending to the same node:

    1/2: [0;2] = [0;1,1]      3/5: [0;1,1,2] = [0;1,1,1,1]
    2/3: [0;1,2] = [0;1,1,1]  5/8: [0;1,1,1,1,1] = [0;1,1,1,2]

(all verified to reach the identical rational). An **irrational** has a
**unique** infinite path. The double representation of rationals is the
tree's `0.999… = 1` — the same identity `minimum_alphabet.md` reads as the
alternating ψ-mode collapsing its residual.

### C4 — `φ` is the deepest point of the completion

The golden ratio's CF is all-1s, so its convergent denominators are the
**Fibonacci numbers** — the *minimal* possible growth:

    φ:    q_n = 1, 2, 3, 5, 8, 13, 21, 34      (Fibonacci — slowest)
    √2:   q_n = 2, 5, 12, 29, 70, 169, 408, …
    π:    q_n = 7, 106, 113, 33102, …           (plunges at 292)
    e:    q_n = 1, 3, 4, 7, 32, 39, 71, 465

So `φ`'s resolution floor `1/(q_n q_{n+1})` shrinks **slowest** — after 8
levels it is still `1.4e-3`, against `√2`'s `2.5e-6` and `π`'s `3.8e-11`.
`φ` is the **worst-approximable** real (Hurwitz), the point the tree resolves
last. This is exactly `minimum_alphabet.md`'s claim that the staircase's
finest self-similar structure sits at `1/φ`, and that the Planck floor is
reached slowest there: the same statement, now as a property of the SB
boundary.

### C5 — where the faces meet

The completion holds both faces of the repo's register at once. The
standing-wave rotation `ρ = log₂(3/2) = 0.5849625…` (`../mode_locking/`) is
an **irrational → infinite path**, and its convergents are the very nodes
that bracket it:

    ρ's bracketing nodes:  1/1, 1/2, 3/5, 7/12, 24/41, …

`7/12` (12-tone equal temperament) is one of them. So:

- **rationals** = finite nodes = mode-lock **centres** → the **locked** face;
- **irrationals** = infinite paths = the **gaps** (`ρ`, and where Collatz
  orbits wander) → the **unlocked** face;
- **`∂T`** = their union = **the completion of ℚ**, where the two faces meet.

---

## What this does and does not show

**Does (supportable, checked):**
- The framework's Open item has a **classical, exact answer**: the SB-tree
  boundary is the completion `R≥0`; the path encoding is the continued
  fraction; the resolution `1/(bd)` is the bracket width by unimodularity.
- Four informal framework claims map exactly onto standard facts: floor
  `1/q²` (C1), completion-as-limit (C2), `0.999…=1` (C3), `1/φ`-depth (C4).
- The completion contains the repo's locked and unlocked faces as the
  finite-node / infinite-path dichotomy (C5).

**Does NOT (guard rails):**
- The construction is **classical mathematics**, not a framework discovery
  (continued fractions / Stern–Brocot / Minkowski's `?`-function). The Class 2
  content is the **identification** — naming the framework's Open item *as*
  this construction and checking the claims line up. It adds no new
  derivation.
- It resolves the **mathematical** half of the Open item (the "limiting
  process"). The other half `minimum_alphabet.md` poses — *what physical
  observable distinguishes "rational resolved at depth d" from "irrational in
  the gap"?* — is **physics, and remains open**. The tree gives the structural
  distinction (terminating vs non-terminating path); it does not supply the
  observable.
- No constant, no scorecard claim. `1/φ`, `13/19`, etc. are imported; their
  physical status is audited in harmonics, not asserted here.

In one line: *the framework's "completion on the Stern–Brocot tree" is the
classical SB-boundary / continued-fraction construction; naming it closes the
mathematical Open item and gives the resolution floor, `0.999…=1`, and the
`1/φ`-depth claims an exact home — while the physical-observable half stays
open.*

---

## What this closes, and what stays open

**Closes (downgrade from Open):**
- `minimum_alphabet.md` Part III "formalize the completion as a limiting
  process on the SB tree" — **answered**: it is the tree boundary, CF-encoded,
  with width `1/(q_n q_{n+1})`.
- `../farey/equidistribution.md` Open #1 ("the completion as the bridge") —
  this **is** that bridge; the locked nodes and unlocked paths are unified as
  `∂T`.

**Stays open:**
1. **The physical observable.** Structurally, "resolved at depth `d`" = path
   reaches a node with `q_n q_{n+1}` below the floor; "in the gap" = path
   continues. What *measurement* realizes that cut is physics the tree does
   not decide.
2. **A measure on `∂T`.** Minkowski's `?`-function is the canonical
   homeomorphism `∂T → [0,1]` (sending CF to binary, quadratic irrationals to
   rationals); relating its singular measure to the framework's tongue-width
   `Σ 1/q²` (the `K=1` locked measure of `../mode_locking/`) would tie the
   completion's metric to the staircase's. A concrete, framework-native next
   step.

---

## Check

`sb_boundary.py` — pure Python, no numpy, exact integer/`Fraction`
arithmetic (floats only to read off the CF of `π, e`). Prints C1
(unimodularity → width `1/(bd)`), C2 (CF = path run-lengths, convergents,
shrinking floor), C3 (the two-tails `0.999…=1` and unique irrational paths),
C4 (`φ`'s Fibonacci denominators = slowest floor), and C5 (`ρ = log₂(3/2)` as
an infinite path bracketed by `7/12, 24/41, …`).

## References

- A. Hurwitz (worst-approximability of `φ`); H. Minkowski, the `?`-function
  (the canonical `∂T → [0,1]` map); standard continued-fraction / Stern–Brocot
  theory (the tree boundary as the real completion).
- Internal (this repo): `sb_boundary.py`; the faces it unifies —
  `../mode_locking/standing_waves.md` (locked nodes), `../collatz/minimal_chaos.md`
  (unlocked dynamics), `../farey/equidistribution.md` (the asymptotic face).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (Part III — completion of ℚ, the `1/q²` floor, `0.999…=1` as the ψ-mode,
  `1/φ` self-similarity; **Status: Open**, which this note addresses on its
  mathematical side). Referenced, not reproduced; the substrate of record is
  harmonics (see `../README.md`).
