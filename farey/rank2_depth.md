# Rank-2 Depth: the q₂ / F₂ / Noncommutativity Decomposition

## Status / classification (read first)

**Class 2 — structural reading.** `ford_apollonian.md` fixed the **rank-1**
canonical depth (curvature `q²`, not the soft tree-level count) and left one
question open: what plays that role for the **rank-2** census — the Li & Liao
braid words, which live in the free group `F₂`, not in PSL(2,ℤ)? This note
decomposes that obstruction and names the answer.

**The decomposition (theorems, verified in the check):**
`F₂` resists the `q²`-depth because `F₂` is precisely the part of the modular
group left after **throwing away `q₂` and `q₃`** — the torsion. The
"noncommutativity" *is* the commutator subgroup, and what you quotient to
reach it is exactly `q₂ × q₃`.

**What is theorem vs reading.** S1–S3 below are theorems (the check verifies
them). S4 — that the *framework's* canonical rank-2 depth is the **hyperbolic
length on `X(2)`** — is a **reading**: it is the natural pullback of
PSL(2,ℤ)'s geometry, but whether it organizes the Li & Liao periods better
than word length is an **empirical** question, tested in the sibling
(`lunar-theory`), not here (per the empirical gate). No derivation, no
constant.

Companion check: `rank2_depth.py` (pure Python, deterministic).

---

## S1 — `{2,3}` are the torsion of PSL(2,ℤ)

The group that generates the whole Stern–Brocot / Farey tree factors as a
free product:

    PSL(2,ℤ) = ℤ/q₂ ∗ ℤ/q₃ = ℤ/2 ∗ ℤ/3.

Verified: the generators have orders `order(S) = 2 = q₂` and
`order(ST) = 3 = q₃`. So the forced primes enter the tree's *generator* as
the **orders of the two torsion elements** — a different appearance of
`{2,3}` than the bare `3/2` ratio of `mode_locking`.

## S2 — the noncommutative core is `F₂`; the abelian shadow is `q₂ × q₃`

The commutator subgroup `[PSL(2,ℤ), PSL(2,ℤ)]` is `F₂`, giving a short exact
sequence

    1 → F₂ → PSL(2,ℤ) → ℤ/q₂ × ℤ/q₃ → 1,    ℤ/q₂ × ℤ/q₃ = ℤ/6.

The "noncommute" is the kernel `F₂`; the commutative shadow is `ℤ/6` (the
abelianization of `ℤ/2 ∗ ℤ/3`, cyclic since `gcd(2,3)=1`). The torsion-free,
geometrically clean representative is `Γ(2)`, with

    [PSL(2,ℤ) : Γ(2)] = |PSL(2,𝔽₂)| = 6 = q₂·q₃

(verified: invertible 2×2 over `𝔽₂` number 6, nonabelian `≅ S₃`), and
`Γ(2) ≅ F₂`. *(This `6 = q₂q₃` is `[PSL(2,ℤ):Γ(2)]`, a theorem — **not** the
`Γ₀(6)` forcing the `MANIFEST` audit marks unsubstantiated; different
subgroup.)*

## S3 — `F₂ = π₁(X(2)) =` the 3-body shape sphere

The planar 3-body **shape sphere minus its 3 binary-collision points** is a
thrice-punctured sphere: `χ = 2 − 3 = −1`, so `π₁` is free of rank
`1 − χ = 2 = F₂` (verified). `X(2) = Γ(2)\ℍ` is the *same* thrice-punctured
sphere (3 cusps). Hence the rank-2 census — the Li & Liao `free_group` words —
are conjugacy classes in this `F₂ = Γ(2) = π₁(X(2))`. (Montgomery's
shape-sphere program is the citable backbone.)

## S4 — canonical depth = hyperbolic length, not word length

`F₂` is **free** — no torsion, no relations, every generator equal — so its
only intrinsic length is the **word metric** (the soft count). That is *why*
`lunar-theory #20` only saw `T* ∝ L_f`: a free group has nothing else to
offer. Pulling PSL(2,ℤ)'s geometry back through `Γ(2)` gives each word a
**hyperbolic length** on `X(2)`:

    ℓ(w) = 2·arccosh(|tr M(w)| / 2),    M(w) ∈ Γ(2) ⊂ PSL(2,ℤ),

(`ℓ = 0` for parabolics — the cusp loops). Using the standard `Γ(2)`
parabolic generators `a = [[1,2],[0,1]]`, `b = [[1,0],[2,1]]`:

| word | \|tr\| | hyperbolic length `ℓ` | type |
|---|---|---|---|
| `ab` | 6 | 3.52549 | hyperbolic |
| `aB` | 2 | 0.00000 | parabolic (cusp) |
| `abab` | 34 | 7.05099 | hyperbolic |
| `abAB` | 18 | 5.77454 | hyperbolic |
| `aabb` | 18 | 5.77454 | hyperbolic |

Two length-2 words: `ab` is hyperbolic (`ℓ = 3.525`), `aB` is a parabolic
cusp loop (`ℓ = 0`). **Word length does not fix the depth.** Across all
freely reduced words, at each fixed word length `ℓ` spans a range:

| word length `n` | # words | # parabolic | `ℓ` range [min, max] |
|---|---|---|---|
| 2 | 12 | 8 | [3.5255, 3.5255] |
| 3 | 36 | 12 | [3.5255, 4.5849] |
| 4 | 108 | 24 | [3.5255, 7.0510] |
| 5 | 324 | 36 | [3.5255, 8.1203] |

Word length is the **soft** count; hyperbolic length is the **rigid** depth —
the rank-2 analogue of `ford_apollonian`'s (tree level vs `q²`).

---

## What this does and does not show

**Does (theorems, checked):** `PSL(2,ℤ) = ℤ/q₂ ∗ ℤ/q₃`; the SES with
abelianization `ℤ/q₂ × ℤ/q₃`; `[PSL(2,ℤ):Γ(2)] = q₂q₃ = 6`;
`F₂ = π₁(X(2)) =` shape sphere minus collisions; and that hyperbolic length
on `X(2)` is a genuine, rigid depth on `F₂` distinct from word length.

**Does NOT (guard rails):**
- It does **not** show the X(2) hyperbolic length is *the* framework depth —
  that it organizes the Li & Liao `T*` better than word length is the
  empirical claim, tested in the sibling (`lunar-theory`), not asserted here.
- The standard-`Γ(2)` hyperbolic length is a **proxy** for the orbit's true
  length in the dynamical (shape-sphere / Jacobi–Maupertuis) metric; they
  need not coincide. The combinatorial pullback is canonical *as a depth*,
  not as the physical period. The sibling probed this directly
  (`lunar-theory:three_body_dynamical_depth.py`): the two naive *physical*
  candidates fail — the full-config abbreviated action is **virial-locked**
  (`= 2·T*` identically) and the round shape-sphere arc length
  *anti*-correlates with `T*` within fixed word length — while `ℓ` organizes
  it. So `ℓ` (the canonical, geodesic, minimal-in-class length) is the
  relevant depth; the proxy flag is **sharpened, not closed**.
- The braid-generator ↔ parabolic-generator identification is a fixed choice;
  `|tr|` (hence `ℓ`) is conjugation-invariant, so `ℓ` is well-defined on
  conjugacy classes (free-homotopy classes), but the labeling convention is a
  modelling input.

---

## Open / could-sharpen

1. **Does `ℓ` beat word length on the catalog?** The decisive test: compute
   `ℓ` for each Li & Liao word and re-run the `#20` discrimination
   (`T*` vs `ℓ` vs `L_f`). That is the sibling task this note sets up.
2. **The dynamical vs modular metric — probed, one refinement left.** The
   sibling integrated all 695 catalog orbits
   (`lunar-theory:three_body_dynamical_depth.py`): the abbreviated action is
   virial-locked to `T*` and the *round* shape-sphere arc length anti-organizes,
   so neither is the physical reconciliation. The one untested candidate that
   could still upgrade `ℓ` from proxy to physical depth is the
   **Jacobi–Maupertuis-*conformal*** length on the shape sphere (the round
   length weighted by `√(2(E−V))`), not the round length used so far.

---

## Check

`rank2_depth.py` — pure Python, no numpy, deterministic. Prints S1 (generator
orders `q₂=2, q₃=3`), S2 (the SES; `|PSL(2,𝔽₂)| = 6 = q₂q₃`), S3 (`χ=−1 →
F₂`), and S4 (hyperbolic lengths: `ab → 3.52549`, `aB → 0`, and the
fixed-word-length `ℓ`-range table).

## References

- Internal: `rank2_depth.py`; `ford_apollonian.md` (rank-1 canonical depth,
  the open item this closes as a reading), `../mode_locking/depth_discrimination.md`
  (the rank-1 discrimination), `../three_body/no_closed_form.md` (the rank-1
  → rank-2 axis).
- Sibling: `lunar-theory` `#20` (the rank-2 census; the hyperbolic-length
  discrimination is the next step there).
- External: PSL(2,ℤ) `= ℤ/2 ∗ ℤ/3`; the commutator subgroup `≅ F₂` of index 6;
  `Γ(2)` free of rank 2; R. Montgomery, the three-body problem and the shape
  sphere (free-homotopy classes = conjugacy classes in `F₂`); hyperbolic
  translation length `2·arccosh(|tr|/2)`.
