# No Closed Form: Three Bodies as the Unlocked Face of Rank

## Status / classification (read first)

**Class 2 — structural reading.** This note reads a *theorem about an
external object* — the non-integrability of the three-body problem
(no exact algebraic formula for the motion of three or more coupled
oscillators) — in the framework's locked-vs-unlocked vocabulary. It
locates that theorem on the same axis as Collatz and Riemann: the
unlocked complement of the `{2,3}` mode-locking arena.

**What it is NOT.** It does **not** prove, reprove, or strengthen the
three-body result; Poincaré (1892) and Bruns (1887) did that. It derives
no constant, makes no prediction, and in particular makes **no claim about
the Earth–Moon system's history** — the Earth–Moon system appears only as
a *qualitative* example of why a hierarchical subsystem is tractable. The
framework supplies the locked arena (one rotation number) and names its
boundary (the golden mean); the obstruction to a closed form is imported,
not produced.

One difference from the sibling studies is worth stating up front: the
Collatz and Riemann studies leave an **open conjecture** standing. Here the
negative result is a **theorem** — three bodies provably have no extra
algebraic integral. So "the unlocked interior stays open" becomes "the
unlocked interior is *closed by theorem* — non-integrable." The framework
reads which side of its own boundary the object sits on; it does not move
the boundary.

Companion check: `no_closed_form.py` (pure-Python, deterministic; prints
every number below).

---

## The object

Three (or more) bodies interacting gravitationally are coupled phase
oscillators: each orbit has a phase, and the couplings shift the phases.
The question — *is there an exact algebraic formula for the motion?* — is
the question of **integrability**: enough conserved quantities to solve the
system by quadratures. Two bodies have them (the Kepler problem closes:
one rotation number, an ellipse that stands). Three do not. Poincaré showed
the perturbation series for any new integral diverges, killed by **small
divisors** `1/(k·ω)`; Bruns showed no new *algebraic* integral exists at
all. The ten classical integrals (energy, the momentum and
centre-of-mass components, angular momentum) are all there are.

The framework's minimum alphabet (`harmonics:minimum_alphabet.md`) derives
the circle map and its Stern–Brocot staircase of locks for **one** rotation
number — the `mode_locking/standing_waves.md` arena, run on the bare
`×q₃/÷q₂ = ×3/÷2` ratio. The reading here is the single step beyond that
arena: what changes when there is more than one rotation number to lock.

---

## Weak layer vs strong layer (kept apart)

**The weak layer** (generic; almost anything satisfies it): *"a system of
`n` coupled oscillators has `n−1` independent frequency ratios."* That is
just bookkeeping — true of any oscillator network, no framework content.

**The strong layer** (framework-native, non-generic): two specific things
line up with framework objects the repo already owns.

1. **Rank 1 is exactly the framework's arena.** The one case where a single
   rotation number is a *complete* invariant (Denjoy) is `n = 2` — and that
   is precisely the `×3/÷2` circle map of `standing_waves.md`. The
   framework's locked census is the rank-1 census, and *only* the rank-1
   census closes.
2. **The boundary is the golden mean — the tree's deepest point.** The last
   invariant torus to survive as the coupling grows is the one whose
   rotation number is the *worst-approximable* number, the golden mean —
   which `root/golden_root.md` independently identifies as the **deepest
   point of the Stern–Brocot boundary**. The locked/unlocked frontier of
   the three-body problem *is* the framework's deepest node.

The weak layer would let you say "`2` and `3` appear." The strong layer is
that the framework's *own* arena (rank-1 circle map) and its *own* deepest
node (`φ`) are the integrable case and the last-surviving torus — neither
of which is generic.

---

## What the check shows

### T1 — rank: the dimensional jump `n → n−1`

A frequency vector `ω ∈ ℝⁿ`; resonances are `k·ω = 0`, `k ∈ ℤⁿ\{0}`.
Overall time-scaling is a gauge, so the invariant content is the ray
direction — `n−1` independent ratios, the **rank** of the torus.

| n bodies | rank `= n−1` | rotation object |
|---|---|---|
| 2 | **1** | one number on `S¹` — the `standing_waves` arena |
| 3 | **2** | a vector on `T²` — three-body |
| 4 | 3 | a vector on `T³` |

Rank 1 is the only rank where a single rotation number is a complete
invariant. Three bodies (rank 2) are the first step out of the framework's
rank-1 arena (the bare `q₃/q₂ = 3/2`).

### T2 — small divisors: a rank-1 floor vs rank-2 overlap

**Rank 1 has a Diophantine floor.** For a badly-approximable rotation
number the divisor `q·‖q·ρ‖` stays bounded below, so the KAM series
converges and the invariant circle survives. For the most robust case
(golden):

    liminf q·‖q·ρ‖ = 0.4472136 = 1/√5     (bounded away from 0)

**Rank 2 has no such floor — resonances overlap.** Modelling the locked
zones by the standard map (resonances spaced `2π`, each of half-width
`2√K`), the simple two-resonance overlap estimate is

    4√K = 2π  ⟹  K = π²/4 = 2.4674

and the exact last-torus value (Greene 1979) is

    K_c = 0.9716354

The crude criterion overestimates by `2.54×`; both are `O(1)`. Above `K_c`
**no** invariant circle blocks transport: the rank-2 census does not close,
the perturbation series for any new integral diverges, and no exact
algebraic integral survives — Poincaré (1892) / Bruns (1887). The
substrate's own frequency-resolution bound `T_obs ≥ 1/Δω`
(`harmonics:fidelity_bound.md`) is the same `1/(k·ω)` small divisor seen
from the measurement side: nearby frequencies cannot be resolved in finite
time, and that *is* the obstruction.

### T3 — the golden boundary

Which rotation number survives longest? The worst-approximable one.
`liminf q·‖q·x‖` (larger = more avoided by rationals = more robust torus):

| `x` | `liminf q·‖q·x‖` | closed form |
|---|---|---|
| **golden** `(√5−1)/2` | **0.4472136** | `1/√5` (Hurwitz max) |
| `√2 − 1` | 0.3535534 | `1/(2√2)` |
| `√3 − 1` | 0.2886751 | `1/(2√3)` |
| `√5 − 2` | 0.2236068 | `1/(2√5)` |

The maximum is the golden mean at `1/√5 = 0.4472136` — Hurwitz's theorem
says no number can do better. Its continued fraction is `[1; 1, 1, 1, …]`:
every step takes the *smallest* mediant, so it descends the Stern–Brocot
tree as deep as possible at each node. **Worst-approximable = deepest SB
point (`φ = 1.6180340`) = last standing wave to survive = the
locked/unlocked boundary.** It is the rank analogue of Collatz's `q < q₂²`
boundary: the framework owns the boundary; the interior is the hard part.

---

## What this does and does not show

**Does (supportable, checked):**
- Rank `n−1` for `n` bodies, with rank 1 the unique complete-invariant case
  and the exact arena of `standing_waves.md`.
- The rank-1 Diophantine floor (`1/√5` for golden) vs the rank-2 overlap
  threshold (`π²/4` crude, `K_c = 0.9716354` exact), the mechanism by which
  the census fails to close.
- The golden mean as the worst-approximable number (`1/√5`, Hurwitz max
  over the table) and hence the last torus — coinciding with the framework's
  deepest Stern–Brocot node.

**Does NOT (guard rails):**
- It does **not** prove non-integrability. Poincaré/Bruns are cited, not
  reproduced; the framework reads which side of its boundary the object is
  on, nothing more.
- It makes **no Earth–Moon prediction.** The Earth–Moon(–Sun) system is a
  *hierarchical* problem (one dominant pair, weakly perturbed) that sits
  *near* the rank-1 sub-manifold, which is **why** lunar theory is
  perturbatively tractable at all — a structural observation, not a
  numerical forecast of tides, recession, or day-length. The general
  three-body problem lives in the rank-2 interior; this subsystem is
  tractable because it is close to the locked edge, not because the general
  problem is solvable.
- The standard map is a **model** of the locked-zone geometry, not the
  gravitational three-body Hamiltonian; `K_c` is the canonical last-torus
  constant for that model, used to exhibit the overlap mechanism, not as a
  three-body observable.
- The rank-counting layer is generic (see *weak vs strong* above); only the
  arena-coincidence and the `φ`-boundary are framework-native.

---

## The shared place — the third unlocked face

The repo's three hard objects are three faces of the **unlocked** complement
of the one locked arena:

- **Collatz** — unlocked *dynamically*: the `+1` pushes orbits off the
  plateaus into a full shift (`collatz/minimal_chaos.md`).
- **Riemann** — unlocked *asymptotically*: maximal equidistribution of the
  Farey tree in the limit (`farey/equidistribution.md`).
- **Three-body** — unlocked *dimensionally*: rank `≥ 2`, where one rotation
  number is no longer a complete invariant and the resonances overlap
  (this note).

All three sit outside the rank-1 `{2,3}` staircase whose standing waves the
framework owns (`mode_locking/standing_waves.md`), and all three meet its
boundary at the golden mean (`root/golden_root.md`) — here as the literal
last torus. The framework supplies the locked stage and its deepest node;
each object is located in the unlocked complement and the open problem (or,
here, the proven obstruction) is left exactly where it stands.

---

## Open / could-sharpen

1. **Rank 2 vs higher rank.** This note treats "rank `≥ 2`" as one regime
   via the standard map (effectively 1½ degrees of freedom). The genuine
   distinction between rank 2 (KAM tori can still separate the energy
   surface) and rank `≥ 3` (Arnold diffusion along the web for *any*
   coupling) is real and not exhibited here; a higher-rank check is the
   natural next step.
2. **How near is "near"?** The claim that the Earth–Moon system "sits near
   the rank-1 sub-manifold" is qualitative. Quantifying the hierarchy
   (e.g. a Hill-type ratio) and relating it to a Diophantine distance from
   resonance would sharpen it — but any such number is a property of the
   system, **not** a framework output, and would have to be labelled Class 1
   if dressed as a prediction.
3. **Is `φ` forced, or merely deepest?** That the last torus is the golden
   mean is a theorem of one-frequency KAM theory; that the framework's
   deepest node is also `φ` is `root/golden_root.md`. Whether these two
   facts share more than the worst-approximable property is the sharper
   question, and is open.

---

## Check

`no_closed_form.py` — pure Python, no numpy, deterministic. Prints T1 (rank
`= n−1` for `n = 2,3,4`), T2 (the rank-1 golden floor `1/√5 = 0.4472136`
and the rank-2 overlap `π²/4 = 2.4674` vs `K_c = 0.9716354`), and T3 (the
`liminf q·‖q·x‖` table with golden maximal at `1/√5`). The `liminf` is
computed from exact integer convergents against a high-precision `Decimal`
value, avoiding the float blow-up that `q·(q·x − p)` suffers once `q`
exceeds `~1e8`.

## References

- Internal (this repo): `no_closed_form.py`; companions
  `../mode_locking/standing_waves.md` (the rank-1 arena),
  `../collatz/minimal_chaos.md` and `../farey/equidistribution.md` (the
  other two unlocked faces), `../root/golden_root.md` (`φ` as the deepest
  Stern–Brocot node).
- Cross-repo substrate (`nickjoven/harmonics`, pinned at the submodule
  commit recorded in `../MANIFEST.yml`): `minimum_alphabet.md` (the circle
  map and Stern–Brocot staircase from the four primitives);
  `fidelity_bound.md` (the frequency-resolution bound `T_obs ≥ 1/Δω` — the
  small divisor from the measurement side). Referenced, not reproduced; the
  substrate of record is harmonics (see `../README.md`).
- External: Poincaré, *Les méthodes nouvelles de la mécanique céleste*
  (1892, non-existence of new uniform integrals; small divisors); Bruns
  (1887, no new algebraic integral); the KAM theorem (Kolmogorov 1954,
  Arnold 1963, Moser 1962); Chirikov (1979, resonance overlap); Greene
  (1979) and MacKay (last KAM torus, `K_c ≈ 0.9716`); Hurwitz (1891, the
  `1/√5` approximation constant of the golden mean).
