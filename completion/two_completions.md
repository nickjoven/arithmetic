# Two Completions: Collatz's Lossy mod-2 and the 2-adic Sibling

## Status / classification (read first)

**Class 2 — structural reading. NOT a proof of Collatz, NOT a new
constant.** This note takes the *lossy* operator at the heart of Collatz —
the mod-2 read — to depth, and finds it is the doorway to the **second
completion of ℤ**. `sb_boundary.md` built one completion (the Archimedean
ℝ, as the Stern–Brocot tree boundary); the mod-2 reduction's natural home is
the other (the non-Archimedean 2-adics `ℤ₂`), where the loss *vanishes*.
The conjecture turns out to live in the **gap between the two completions** —
the repo's inside/outside seam, made exact. Companion check:
`two_completions.py` (pure-Python, deterministic; every number below is
printed by it).

This pairs with `sb_boundary.md`: the `completion/` directory now holds
**both** completions of ℚ, and Collatz is what reveals the second one.

---

## The object — a lossy operator

The shortcut Collatz map reads one bit and discards it:

    T(x) = x/2        if x ≡ 0 (mod 2)
    T(x) = (3x+1)/2   if x ≡ 1 (mod 2)

The `mod 2` is a projection `ℤ → ℤ/2` — **lossy**: it forgets everything but
the bottom bit. Every step extracts and destroys one bit of `x`. The
question this note answers is what that loss *is*, taken to depth.

---

## L1 — lossy per step, lossless in aggregate

Record the bit read at each step. The first `k` reads, packed as a 2-adic
integer, give the **parity vector**, and (Terras 1976) the map
`x ↦ parity-vector(x)` is a **bijection on `ℤ/2ᵏ`** for every `k` (verified
to `k=12`), with an **exact inverse**: the `k` lossy reads reconstruct
`x mod 2ᵏ` precisely.

So the mod-2 loss is a *per-step artifact*. One bit dies each step, but the
**stream** loses nothing — it is exactly the 2-adic coordinate of `x`. The
lossy operator, read along the orbit, is a lossless change of coordinates.

---

## L2 — the loss has a direction (the `3/4` contraction, in bits)

Measure the loss in **bit-length** `log₂ x`:

| read | `Δ log₂ x` | |
|---|---|---|
| even (`÷q₂`) | `−1` | strip a 0-bit |
| odd (`×q₃/q₂`) | `log₂(3/2) = 0.585` | the only growth |

At parity `1/2` the mean drift is `−(1 − log₂(3/2))/2 ≈ −0.207` per step;
measured over real orbits it is `≈ −0.236` (same sign and scale, exact only
at parity `1/2`). This is the `q₃/q₂² = 3/4` contraction of
`../collatz/minimal_chaos.md`, recast in **information units**: the lossy
`÷2` reads out-strip the `×3` gains, so bit-length drifts down. The contraction
*is* the asymmetry of the lossy operator — it removes a full bit on `0` and
adds only `log₂(3/2)` of one on `1`.

---

## L3 — the two completions of ℤ, and where the loss goes

By **Ostrowski's theorem**, ℚ has exactly two kinds of completion:

- **ℝ** — the Archimedean one. This is `sb_boundary.md`: the Stern–Brocot
  tree boundary, continued fractions, the real line, where Collatz orbits
  are real-valued descents.
- **ℚ_p** — the p-adics, one per prime. Collatz's lossy operator is the
  `q₂ = 2` reduction, so its home is the **2-adics `ℤ₂`**.

And here is the resolution of the loss. The parity-vector map
`Q_∞ : ℤ₂ → ℤ₂` (Lagarias 1985) is a **measure-preserving homeomorphism** —
the bijection on every `ℤ/2ᵏ` (L1) is its finite witness. So:

> **The lossy mod-2, completed 2-adically, is a lossless isometry.** On `ℤ₂`
> there is no loss and no hard problem: `T` is conjugate to a shift, and
> almost-everywhere statements are clean (this is the setting of Tao 2019's
> "almost all orbits").

The same integer orbit, under the two completions, is two different objects:

| `n` | steps to 1 (in ℝ) | `v₂(n)` (in ℤ₂) |
|---|---|---|
| 27 | 70 | 0 |
| 97 | 75 | 0 |
| 871 | 113 | 0 |

ℝ sees a **length** (a real-valued descent); `ℤ₂` sees a **valuation** (a
digit). They are the Archimedean and non-Archimedean shadows of one integer.

---

## The seam between the completions

The conjecture sits exactly in the gap the two completions leave:

- **`ℤ₂` / outside** — the map is a measure-preserving isometry; *almost
  every* orbit behaves (Tao 2019). Clean, because `ℤ₂` is the completion
  where the loss is an isometry.
- **ℤ / inside** — does *every specific integer* descend? The integers are
  the points both completions agree on, and the bound observer lives there.

This is the repo's recurring **inside/outside, every-vs-almost-every** seam,
now in its sharpest form: as **Archimedean (ℝ) vs non-Archimedean (`ℤ₂`)
completion**. The earlier studies met the seam as locked-vs-unlocked; here it
is the cut between the two ways ℚ can be completed. (And it gives the "act of
division / the only seam" intuition a precise object: the lossy mod-2 *is* the
2-adic seam, and the conjecture is whether the inside view can ever match the
outside one.)

---

## What this does and does not show

**Does (supportable, checked):**
- The lossy mod-2 is lossless in aggregate: the parity stream is a bijection
  on `ℤ/2ᵏ` (Terras) with an exact inverse — it is the 2-adic coordinate.
- The contraction `3/4` is the bit-length asymmetry of the lossy operator
  (`−1` on even, `+log₂(3/2)` on odd; net negative drift).
- Collatz's natural completion is `ℤ₂` (Ostrowski: the `q₂=2`-adic), the
  non-Archimedean sibling of the ℝ-completion in `sb_boundary.md`; on `ℤ₂`
  the operator is a measure-preserving isometry (Lagarias) — the loss
  vanishes.

**Does NOT (guard rails):**
- It does **not** prove Collatz. The 2-adic picture is *clean precisely
  because* it is an a.e. / measure statement; the gap to *every integer* is
  the conjecture, untouched. Cleanness on `ℤ₂` is not descent on ℤ.
- The 2-adic conjugacy is **classical** (Terras 1976, Lagarias 1985). The
  Class 2 content is the **identification** — naming `ℤ₂` as Collatz's
  completion and pairing it with the repo's ℝ-completion and inside/outside
  spine — not a new theorem.
- No constant, no scorecard claim. `q₂, q₃` imported from harmonics.

In one line: *the mod-2 is lossy on ℤ but a lossless isometry on `ℤ₂`;
Collatz's natural completion is the 2-adic sibling of the Stern–Brocot ℝ, and
the conjecture is the seam between the two completions — the inside view (ℤ)
trying to match the outside one (`ℤ₂`).*

---

## Open / could-sharpen

1. **Both completions at once.** A real `x` has an ℝ-position (its
   Stern–Brocot path, `sb_boundary.md`) and the integers have a 2-adic
   coordinate (their parity vector). Is there a single object carrying both —
   the adelic view — in which the framework's finite-depth structure sits? The
   adeles `ℝ × ∏ℚ_p` are the standard home; whether the framework's `{2,3}` and
   forced depth have an adelic reading is the sharp question.
2. **Why 2-adic measure-preservation, framework-side.** Lagarias' isometry is
   the reason a.e. orbits behave. The framework's `q₂ = 2` is the prime here;
   does the substrate's `q₂`-structure (`klein_bottle.md` Z₂) have anything to
   say about the Haar measure the parity map preserves, or is that purely
   number-theoretic? (Likely the latter — flagged as such.)

---

## Check

`two_completions.py` — pure Python, no numpy, deterministic (seeded). Prints
L1 (parity bijection on `ℤ/2ᵏ` + exact inverse), L2 (bit-length drift, the
`3/4` in information units), and L3 (the two completions via Ostrowski, the
`ℤ₂` measure-preservation witness, and the same orbit's ℝ-length vs 2-adic
valuation).

## References

- R. Terras (1976) — the parity-vector / coefficient-stopping-time structure.
- J. C. Lagarias, *The 3x+1 problem and its generalizations*, Amer. Math.
  Monthly **92** (1985) — the parity-vector map as a measure-preserving
  homeomorphism of `ℤ₂`.
- T. Tao, arXiv:1909.03562 (2019) — "almost all" orbits (the a.e. statement
  that is clean on `ℤ₂`).
- Ostrowski's theorem — the completions of ℚ are ℝ and the `ℚ_p`.
- Internal (this repo): `two_completions.py`; the sibling completion
  `sb_boundary.md` (ℝ); the dynamics `../collatz/minimal_chaos.md` (the `3/4`
  contraction this recasts in bits).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md` (the
  completion of ℚ as the continuum limit; `q₂ = 2`). Referenced, not
  reproduced; substrate of record is harmonics (see `../README.md`).
