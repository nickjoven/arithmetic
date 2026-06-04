# The Adelic Height: Is There a Provably Monotone `h(n)`?

## Status / classification (read first)

**Class 2 — the frontier question, answered honestly (a negative/structural
result). NOT a proof of Collatz.** `no_dissipation.md` showed that a forcing
quantity, if one exists, must be **adelic** — built from both the Archimedean
size `|n|` and 2-adic (`v₂`-type) data — because neither completion alone
gives a forced descent. This note asks the direct question: *does such a
provably monotone `h(n)` exist?* The answer is complete and precise: **yes iff
Collatz is true (the stopping time), but circularly; no non-circular /
closed-form one is known, and the natural constructions provably fail — the
height is squeezed between the two completions and can live only on the
measure-zero integers.** Companion check: `adelic_height.py` (every number
below is printed by it).

---

## [0] Existence is circular: the stopping time is the height

A monotone height **exists iff Collatz is true.** The stopping time
`σ(n)` = (steps for `n` to reach 1) satisfies, by definition,

    σ(T(n)) = σ(n) − 1      (verified for n = 2…1999),

a perfect Lyapunov function — strictly decreasing by exactly 1 every step. But
it is **non-constructive**: defining `σ(n)` presupposes the orbit reaches 1.
So "does a monotone `h` exist?" is *identical to* "is Collatz true?" — unless
we demand `h` be **closed-form / locally computable**. That is the real
question, and the rest of this note is about it.

---

## The squeeze: why no closed-form adelic height is known

A closed-form `h(n)` would combine `log|n|` (Archimedean) with some 2-adic
quantity. The two ends defeat each other.

### [1] Finite 2-adic data is blind to the climbs

Take `n = 2ᵏ − 1`. It produces **`k` consecutive odd steps** — an ascending
run — during which `|n|` climbs by `log₂(3/2)` each step while **`v₂(n) = 0`
throughout**:

| `n` | odd steps | `max v₂` on run | `log₂|n|` climbs |
|---|---|---|---|
| `2⁴−1 = 15` | 4 | 0 | `3.9 → 6.3` |
| `2⁷−1 = 127` | 7 | 0 | `7.0 → 11.1` |
| `2¹⁰−1 = 1023` | 10 | 0 | `10.0 → 15.8` |
| `2¹⁴−1 = 16383` | 14 | 0 | `14.0 → 22.2` |

The runs are **unbounded**. Since `v₂(n) = 0` at every step of every climb, no
function of `v₂(n)` — nor any *finite* 2-adic truncation (the bottom `d` bits)
— can offset the rising `log|n|`. The 2-adic *bottom* is blind to the climb.

### [2] The full 2-adic coordinate is conserved (can't descend)

The only 2-adic datum that *does* see the whole climb is the **full
parity-vector coordinate** — and that is **measure-preserving** (an isometry;
`../completion/two_completions.md`). A continuous `h : ℤ₂ → ℝ` strictly
decreasing along orbits is **impossible**: Poincaré recurrence forces a.e.
orbit (hence `h`) to return near its start, contradicting strict decrease.

So the height is **squeezed from both ends**: *finite* 2-adic data can't
compensate the climbs [1]; the *full* 2-adic data can't descend [2].

### [3] The best naive candidate fails for every parameter

`h_α(n) = log₂(n) − α·v₂(n)` is the natural adelic guess. It fails for **every
`α`** (`adelic_height.py`): even steps descend only if `α < 1` (`Δh = α − 1`),
while odd ascending steps (where `v₂(3n+1) = 1`) rise by `log₂(3/2)` for *all*
`α`. No `α` is monotone — the squeeze of [1]+[2] made quantitative.

### [4] Window heights don't escape it

What if `h(n)` peeks at the next `w` iterates (so it can *see* a climb)? A
finite window `w` fails on runs longer than `w` — and runs are unbounded [1].
An *unbounded* window is the entire orbit, i.e. the stopping time [0] —
circular. So: **pointwise and finite-window heights fail; unbounded-window is
circular.** There is no middle.

---

## The answer, stated precisely

> A provably monotone `h(n)` **exists iff Collatz is true** — the stopping time
> is one. A **non-circular, closed-form** such `h` would have to be
> simultaneously **Archimedean-non-monotone** (its `|n|`-part must climb on the
> ascending runs, [1]) and **2-adically discontinuous** (else recurrence
> forbids descent, [2]). Such a function is definable on **neither completion**
> of ℤ; it lives only on the **measure-zero integers**, where the tools of
> real analysis and of 2-adic / ergodic theory both fail to apply. A closed
> form equal to the stopping time *is* a proof of Collatz — and **none is
> known, for exactly this reason.**

So the honest answer to "is there an `h(n)`…?" is: **not a constructive one,
and the obstruction is now precise** — it is not that no one has been clever
enough, but that any such `h` must evade both completions at once, which is the
analytic shape of the conjecture itself.

---

## What this does and does not show

**Does (supportable, checked):**
- The stopping time is a perfect but circular Lyapunov function (`σ∘T = σ−1`).
- Unbounded ascending runs (`2ᵏ−1`) with `v₂ ≡ 0` defeat every finite-2-adic
  height [1]; the conserved full coordinate defeats every continuous-2-adic
  height [2]; the natural `log₂n − α·v₂` fails for all `α` [3]; window heights
  are squeezed between "too short" and "circular" [4].

**Does NOT (guard rails):**
- It does **not** prove Collatz unprovable, or prove no closed-form height
  exists. It shows the *natural* adelic constructions fail and characterizes
  what any working one must look like (neither-completion, ℤ-only). That
  characterization is itself the analytic content of the conjecture.
- The stopping-time observation and the recurrence obstruction are classical;
  the Class 2 content is the squeeze and the precise "neither completion"
  verdict.
- No constant, no scorecard claim.

In one line: *a monotone height exists iff Collatz is true; a closed-form one
would have to be Archimedean-non-monotone and 2-adically discontinuous at once
— belonging to neither completion, only to the measure-zero integers — which
is why none is known and why the adelic route, while the right one, is hard.*

---

## Open / could-sharpen (where traction might still be)

1. **A third place — tested, also blind.** The map *multiplies by 3*, so a
   natural hope is a 3-adic term (`v₃`, or the 3-adic size) tracking the
   numerator growth the 2-adic side misses. It does **not** work
   (`adelic_height.py` [3b]): along the `2ᵏ−1`
   climb, `v₃(n) = 0` for the entire run after the first step, and
   `log₂n − α·v₂ − β·v₃` is best at `β = 0` — the 3-adic valuation is *also*
   blind to the climb. The reason is general and worth stating: **any local
   valuation `v_p(n)` measures the current point, but the climb is driven by
   the accumulated count of `×3` operations** — the odd-step count — which is a
   *trajectory* quantity, not a local function of `n`. So no local `p`-adic
   datum escapes the squeeze; the only thing that tracks the climb is
   essentially the orbit itself, i.e. circular [0]. The squeeze is tighter than
   "`v₂` is blind": *all* local arithmetic is.
2. **Average vs pointwise, made rigorous.** The squeeze is about *pointwise*
   monotonicity. A height monotone *in expectation with a martingale bound*
   that also controls the measure-zero exceptional set would suffice; this is
   essentially Tao's route, and the open part is exactly the exceptional-set
   control. Framing the exceptional set 2-adically (the orbits whose parity
   statistics deviate) is the arithmetic-not-dynamical restatement.

---

## Check

`adelic_height.py` — pure Python, no numpy, deterministic. Prints [0] (the
stopping time as a circular Lyapunov function), [1] (ascending runs with
`v₂ ≡ 0`), [2] (the conserved-coordinate obstruction), [3] (`log₂n − α·v₂`
failing for every `α`), and [4] the neither-completion verdict.

## References

- J. C. Lagarias, *The 3x+1 problem and its generalizations* (1985) — the
  2-adic conjugacy / measure-preservation behind [2].
- T. Tao, arXiv:1909.03562 (2019) — the in-expectation / exceptional-set route
  (Open #2).
- Poincaré recurrence (the [2] obstruction).
- Internal (this repo): `adelic_height.py`; `no_dissipation.md` (which posed
  the adelic question); `../completion/two_completions.md` (the two
  completions, the 2-adic isometry); `minimal_chaos.py` (the `3/4` drift, the
  cycle exclusion).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (`q₂ = 2`, `q₃ = 3`). Referenced, not reproduced; substrate of record is
  harmonics.
