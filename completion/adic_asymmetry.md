# Which N-adic? The `+1` as Symmetry-Breaker

## Status / classification (read first)

**Class 2 — structural reading. NOT a new constant, NOT a proof.** Answers a
sharp question: *does one N-adic completion carry very interesting structure
for Collatz, or do two primes straddle a line of symmetry?* The answer is the
first — **one N-adic (the 2-adic) is singular** — and the reason it is *not*
two-straddling-a-symmetry is the `+1`. The genuine symmetric pairs exist but
are shifted off the completions. Companion check: `adic_asymmetry.py` (every
number below is printed by it). This sharpens `two_completions.md` (it explains
*why* `ℤ₂` and not `ℤ₃`); it overturns nothing.

---

## The setup

Collatz mixes two primes: `÷q₂` (`q₂ = 2`) and `×q₃` (`q₃ = 3`). Symmetric on
the face of it — one valuation-changing operation per prime. So one might
expect `ℤ₂` and `ℤ₃` to be a balanced pair. They are not, and the imbalance
is instructive.

---

## A — the `+1` is a symmetry-breaker

For every odd `n`, the quantity `3n+1` is **simultaneously**:

- **even** (`v₂(3n+1) ≥ 1`) — there is a factor of 2 to halve, and
- **coprime to 3** (`v₃(3n+1) = 0`) — since `3n+1 ≡ 1 (mod 3)`.

(verified for all odd `n < 22`.) So the *same* `+1` that **creates** 2-adic
structure (an even number, the whole point of the shortcut map) **destroys**
3-adic structure (the `×3` builds no 3-adic depth). Along an orbit:

    v₂ of 27's orbit: 0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,…   (rich — drives it)
    v₃ of 27's orbit: 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,…   (dies after one step)

The contrast is decisive. **Strip the `+1`** (pure `odd → 3n`) and the `×3`
*does* build 3-adic depth:

    (n, v₃) under n→3n / ÷2 :  (5,0),(15,1),(45,2),(135,3),(405,4),(1215,5)  →  v₃ accumulates

So the `+1` is what tilts the map entirely onto the prime 2: it enriches the
2-adic (where Lagarias' measure-preserving conjugacy lives, `two_completions.md`
L3) and trivializes the 3-adic, by hand, in one stroke. **One N-adic — the
2-adic — is singular, *because* the `+1` breaks the `2↔3` symmetry.**

And the `+1` is exactly the **mediant with the Stern–Brocot root** `1/1`
(`../collatz/minimal_chaos.md` M3): the operation that *makes the seam* is the
operation that *breaks the symmetry*.

---

## B — the genuine straddle: 3 and 5 about the multiplier line `q₂² = 4`

There *is* a symmetric pair — but it is in the **multiplier**, not the
completion:

| `q` | `q/4` | |
|---|---|---|
| `3 = 4−1` | 0.75 | contracts (`3n+1` converges) |
| `4 = q₂²` | 1.00 | **neutral — the symmetry line** |
| `5 = 4+1` | 1.25 | expands (`5n+1` diverges) |

`3n+1` and `5n+1` are mirror images about the neutral line `q = q₂² = 4`. The
line itself is **even** — an invalid odd multiplier — so it is **unoccupied**:
the symmetry has no fixed point on it, and the two nearest odd maps sit one
step on either side (`../collatz/minimal_chaos.md` M1). This is "two straddle a
line of symmetry," but the two are *maps*, not completions.

---

## C — a separate field symmetry: `2 ≡ −3 (mod 5)` in φ's field

In `ℚ(√5)` — the field of the golden ratio (`../root/golden_root.md`,
`sb_boundary.md` C4) — primes split by residue mod 5. The two forced primes
land symmetrically:

    p = 2 : 2 mod 5 = 2  → inert      p = 3 : 3 mod 5 = 3 → inert
    2 ≡ −3 (mod 5)  → negatives of each other, symmetric about 5; both INERT.

Meanwhile the framework's Farey counts **split**: `11 = |F₅|` (`≡1`) and
`19 = |F₇|` (`≡−1`, the denominator of `Ω_Λ = 13/19`). So `{2,3}` (the forced
primes) and `{11,19}` (Farey counts `|F₅|, |F₇|`) fall in **opposite classes**
of the same mod-5 symmetry. A clean, separate "line of symmetry" — about `5`,
in φ's field — distinct from both A and B.

---

## What this does and does not show

**Does (supportable, checked):**
- The `+1` makes `3n+1` even and coprime to 3 at once; so `v₂` is rich and
  `v₃` collapses — the 2-adic is the singular interesting completion, and the
  `+1` is the symmetry-breaker (confirmed against the no-`+1` map, where `v₃`
  accumulates).
- The symmetric straddle `3↔5` is about the multiplier `q₂² = 4`, not the
  completions; the neutral line is unoccupied.
- In `ℚ(√5)`, `2 ≡ −3 (mod 5)` (both inert) while `11, 19` split.

**Does NOT (guard rails):**
- It does **not** prove anything about Collatz; it explains *which* completion
  is structurally singled out and *why*. The 3-adic triviality is consistent
  with — indeed it is the mechanism behind — `adelic_height` [3b] ("`v₃` is
  also blind").
- The mod-5 splitting is **standard** (Legendre symbol / decomposition in a
  quadratic field); the Class 2 content is noticing that `{2,3}` and `{11,19}`
  sit on opposite sides of it. No claim that this *forces* anything.
- No constant, no scorecard claim.

In one line: *the `+1` breaks the `2↔3` symmetry — enriching the 2-adic,
trivializing the 3-adic — so one N-adic is singular; the real symmetric pairs
are `3↔5` about the multiplier `q₂²=4` and `2↔3` about `5` in φ's field.*

---

## Open / could-sharpen

1. **The `+1` family.** `3n + 1` is `3n + c` with `c = 1`. For which residues
   `c` is `3n+c` coprime to 3? Exactly `c ≢ 0 (mod 3)` — so the `2-adic`-
   favoring trivialization of the 3-adic holds for any `c ∈ {1,2} (mod 3)`. The
   special role of `c = 1` is the *mediant* (M3), not the coprimality. Worth
   stating which property needs `c = 1` and which only needs `c ⊥ 3`.
2. **Both forced primes inert in `ℚ(√5)`.** Is the fact that `q₂, q₃` are both
   inert (while the Farey counts split) a coincidence of small residues, or
   does it connect to why `{2,3}` generate the *structure* and `{11,19}` the
   *counts*? Almost certainly the former (Class 2, named as such), but it is
   the one thread that ties A/B (Collatz primes) to C (φ's field).

---

## Check

`adic_asymmetry.py` — pure Python, no numpy, deterministic. Prints A (the `+1`
making `3n+1` even & coprime-to-3; `v₂` vs `v₃` along an orbit; the no-`+1`
contrast where `v₃` accumulates), B (the `3↔5` straddle about `q₂²=4`), and C
(the mod-5 inert/split split of `{2,3}` vs `{11,19}`).

## References

- J. C. Lagarias (1985) — the 2-adic conjugacy (why `ℤ₂` is the rich one).
- Quadratic-field decomposition (Legendre symbol; `p` splits in `ℚ(√5)` iff
  `p ≡ ±1 mod 5`) — standard.
- Internal (this repo): `adic_asymmetry.py`; `two_completions.md` (the two
  completions — this explains *why* the 2-adic); `../collatz/minimal_chaos.md`
  (M1 the `q<q₂²` boundary, M3 the `+1` = mediant); `../collatz/adelic_height.md`
  ([3b] `v₃` blind); `../root/golden_root.md` and `sb_boundary.md` (φ, `ℚ(√5)`).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (`q₂=2, q₃=3`), `farey_partition.md` (`|F₅|=11, |F₇|=19`, `Ω_Λ=13/19`).
  Referenced, not reproduced; substrate of record is harmonics.
