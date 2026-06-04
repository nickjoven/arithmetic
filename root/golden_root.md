# One Root: the Framework from a Single Object

## Status / classification (read first)

**Class 2 — synthesis. The most singular representation of the repo, NOT a
reduction of the alphabet.** This note answers one question: *how singularly
can the framework be represented, from one root?* The answer has two layers,
both checked in `golden_root.py`:

1. **One tree, one seed, one operation.** Everything in these studies is the
   Stern–Brocot tree, grown from the seed `(0/1, 1/0)` by the mediant. The
   four studies are four readings of that single tree.
2. **One object carries all four primitives.** The golden matrix
   `M = [[1,1],[1,0]]` holds integers, parabola, fixed-point, and mediant
   simultaneously — and its eigenvalue `φ` is the deepest point of the very
   tree it generates.

**Honesty guard (the line this note does not cross).** This does **not**
collapse the four primitives into one. Their irreducibility — each is
necessary, none derivable from the others — is proved in
`harmonics:minimum_alphabet.md` Part II and is untouched here. What is shown
is a single **common locus** where all four are inseparably present, and from
which the structure unfolds. A singular *representation*, not a smaller
alphabet. No new constant, no scorecard claim; this is existing framework
content viewed from its tightest point.

---

## Layer 1 — one tree, one seed, one operation

The Stern–Brocot tree grows from a single seed — `0/1` and `1/0` (zero and
infinity) — by a single operation, the mediant `(a,b) ⊕ (c,d) = (a+c, b+d)`.
The first mediant is the root node `1/1`; iterating produces every positive
rational once, and the boundary is the completion `R≥0`. The four studies are
four readings of this one tree:

| reading | object | study |
|---|---|---|
| **count** the nodes | `|F_n|`, the framework's `13/19` | `../farey/equidistribution.md` |
| **width** of the nodes | Arnold tongues / standing waves | `../mode_locking/standing_waves.md` |
| a **map** on the nodes | Collatz (integers = `q=1` boundary) | `../collatz/minimal_chaos.md` |
| the **boundary** | the completion of ℚ | `../completion/sb_boundary.md` |

Locked (the nodes) and unlocked (the boundary paths) are not two structures;
they are the interior and the closure of the one tree.

---

## Layer 2 — one object carries all four primitives

The minimum alphabet's four primitives are integers, the mediant, the
fixed-point `x = f(x)`, and the parabola `x² + μ = 0`. They are *all present,
inseparably, in the single matrix* `M = [[1,1],[1,0]]`:

| primitive | how `M` carries it | check |
|---|---|---|
| **Integers** (counting) | `Mⁿ` entries are the Fibonacci numbers | `[1]` |
| **Parabola** (orientation) | char. poly of `M` is `x² − x − 1`; roots `φ, ψ` | `[2]` |
| **Fixed-point** (iteration) | `Mⁿv → φ`-direction; `φ = 1 + 1/φ` | `[3]` |
| **Mediant** (rationals) | `M`'s iteration is the φ-path; convergents = Fibonacci ratios = `Mⁿ` columns | `[4]` |

And the structure that ties them — the parabola's *second* root `ψ`, the
Born/uncertainty content — is `det M = −1`:

    det(Mⁿ) = (−1)ⁿ = F_{n+1}F_{n−1} − F_n²        (Cassini's identity)
    |φ·ψ| = |det M| = 1                            (the uncertainty product)

The exponent-2 of `|ψ|²` (the Born rule) *is* the parabola; the alternating
`(−1)ⁿ` *is* the ψ-mode. `minimum_alphabet.md` already names this cluster
(`x² − x − 1`, `φ`, `ψ`, Cassini, `|φψ| = 1`); the singular statement is that
they are one matrix.

---

## The singularity — generation and completion are the same object

The sharpest point is self-reference. `M` **generates** the tree: its
iteration is the golden path (`[4]`). And `M`'s eigenvalue `φ` is the
**deepest point of the boundary** that tree generates — the worst-
approximable real, with Fibonacci denominators and the slowest-shrinking
resolution floor (`../completion/sb_boundary.md` C4). So:

> `x = f(x)`, with `f` the mediant step and `x = φ` both the generator's
> fixed direction **and** the deepest point of the boundary it generates.
> Generation and completion are one object.

That is the answer to the question. The framework, read down to one root, is
a single self-referential object: the mediant from one seed, whose fixed
point `φ` is simultaneously the operation's eigenvalue and the last point its
own tree resolves. The interior (rationals, the locked nodes), the boundary
(reals, the unlocked completion), and the four primitives all unfold from —
and return to — that one matrix.

---

## What this does and does not show

**Does (supportable, checked):**
- The repo's four studies are four readings of one tree (one seed, one
  operation).
- A single object `M = [[1,1],[1,0]]` carries all four primitives at once,
  with `det M = −1` supplying the ψ-mode / Born / uncertainty content.
- `M`'s eigenvalue `φ` is the deepest point of the boundary `M` generates —
  generation and completion coincide.

**Does NOT (guard rails):**
- It does **not** reduce the alphabet from four primitives to one. The
  irreducibility proof (`minimum_alphabet.md` Part II — each primitive
  necessary) stands. "One object carrying four" is co-location, not
  reduction; the count is still four.
- It is **synthesis of existing framework content**, not a new derivation.
  The `x² − x − 1` / `φ,ψ` / Cassini structure is already in
  `minimum_alphabet.md`; this note states it at its most singular.
- It adds **no** constant and **no** scorecard claim, and it imports the
  physical readings (Born, uncertainty) without re-deriving or vouching for
  them; their status is harmonics', audited there.
- The golden matrix is *a* singular root — the one where the four primitives
  visibly coincide and where the self-reference (generator = deepest
  boundary point) is exact. It is the tightest representation found here, not
  a proof that no other exists.

In one line: *the framework, from one root, is the mediant on one seed — and
the single matrix `[[1,1],[1,0]]` in which its four primitives coincide is
its own tree's deepest point: generation and completion in one self-
referential object.*

---

## Check

`golden_root.py` — pure Python, no numpy, exact integer arithmetic,
deterministic. Prints Layer 1 (one seed, one operation, the four readings),
Layer 2 (the five facts `[1]`–`[5]` showing `M` carries all four primitives
and Cassini/`det`), and the singularity (generator eigenvalue = boundary
deepest point).

## References

- Internal (this repo): `golden_root.py`; the four studies it unifies —
  `../mode_locking/standing_waves.md`, `../collatz/minimal_chaos.md`,
  `../farey/equidistribution.md`, `../completion/sb_boundary.md`.
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md` (the
  four primitives and their irreducibility, Part II; the `x²−x−1` / `φ,ψ` /
  Cassini / `|φψ|=1` cluster; the `1/φ` self-similarity). Referenced, not
  reproduced; the substrate of record is harmonics, and the physical readings
  (Born rule, uncertainty) are claimed there, not here (see `../README.md`).
