# Standing Waves: the `{2,3}` Mode-Locking Staircase

## Status / classification (read first)

**Class 2 — structural reading, framework-native side.** This note reads
the framework's own mode-locking staircase (`harmonics:minimum_alphabet.md`)
in the vocabulary of the two forced primes, by running the bare `×q₃ / ÷q₂`
dynamics and showing its **standing waves** — the mode-locked, periodic,
resonant orbits — are the `{2,3}`-dominated locks the framework predicts. No
new constant, no scorecard claim; it demonstrates structure the framework
already derives, in a concrete dynamical system. Companion check:
`standing_waves.py` (pure-Python, deterministic; prints every number below).

A **standing wave** here is precise: a mode-locked plateau of the circle
map — an orbit that phase-locks to a rational winding number `p/q` and
thereafter repeats, a stationary resonant pattern of `q` modes. This is the
"locked" side of the framework's devil's staircase. Its complement — the
unlocked, never-repeating regime — is where **Collatz** lives, and that is a
separate study (`../collatz/minimal_chaos.md`): *the Collatz conjecture's
vocabulary does not admit standing-wave dynamics.* This note is the standing
waves; that note is their absence.

---

## The object

The framework's minimum alphabet derives the circle map and its devil's
staircase from four primitives (`harmonics:minimum_alphabet.md` Part I):
winding numbers (integers + fixed-point) live on `S¹`, the locked
frequencies are ordered by the Stern–Brocot tree (mediant), and the locking
itself comes from the saddle-node (parabola). The mode-locked plateaus are
the Arnold tongues; their widths scale as `(K/2)^q`, so small denominators
dominate.

The claim tested here: the **bare ratio of the two forced primes**, run as a
dynamical system, *is* such a staircase, and its widest standing waves are
the `{2,3}` locks. The system is the oldest one in music — stack a fifth
(`×q₃/q₂ = ×3/2`), fold by an octave (`÷q₂ = ÷2`) — i.e. the circle of
fifths.

---

## What running the dynamics shows

### S1 — the `×3/2` rotation is a Stern–Brocot rotation number

Stacking `×3/2` and folding `÷2` is rotation on the pitch circle by

    ρ = log₂(q₃/q₂) = log₂(3/2) = 0.5849625…

Its continued-fraction convergents are exactly the historical equal
temperaments — *"q fifths ≈ p octaves"* — and **each lies on the
Stern–Brocot mediant descent to ρ**:

| q fifths ≈ p octaves | `p/q` | value | |
|---|---|---|---|
| 2 ≈ 1 | `1/2` | 0.5000 | on tree |
| 5 ≈ 3 | `3/5` | 0.6000 | on tree |
| **12 ≈ 7** | **`7/12`** | **0.5833** | on tree — **12-tone equal temperament** |
| 41 ≈ 24 | `24/41` | 0.58537 | on tree |
| 53 ≈ 31 | `31/53` | 0.58491 | on tree |

The locks of the `×3/2` rotation are not arbitrary rationals; they are the
mediants the Stern–Brocot tree produces on its way to `ρ`. The `{2,3}` ratio
*generates* the tree path. (That `7/12` is 12-tone equal temperament is the
familiar face of this: twelve fifths almost close seven octaves.)

### S2 — running the circle map grows the tongues, `{2,3}` widest

The sine circle map `θ → θ + Ω − (K/2π)·sin(2πθ)` at critical coupling
`K = 1` produces a devil's staircase whose standing-wave (locked-plateau)
widths rank strictly by denominator:

| winding `W` | denominator | tongue width |
|---|---|---|
| `0/1`, `1/1` | 1 | 0.159 |
| **`1/2`** | **2** | **0.074** |
| **`1/3`, `2/3`** | **3** | **0.031** |
| `1/4`, `3/4` | 4 | 0.016 |
| `1/5`, `2/5` | 5 | 0.009–0.011 |

The widest standing waves after the trivial `0/1, 1/1` are the `q₂ = 2` lock
and then the `q₃ = 3` locks — the framework's two forced primes, in order of
Stern–Brocot depth. This is the quantitative content of "`{2,3}` dominate":
they are not merely *present*, they carry the **widest resonances** of the
staircase.

### S3 — the wave literally stands (locked = periodic), the gap does not

The locked plateaus are standing waves in the strict sense — periodic
orbits. Located by winding number (the coupling shifts every tongue off
`Ω = p/q` except the symmetric `1/2`):

| lock | found at | asymptotic orbit |
|---|---|---|
| `q₂` lock, `W = 1/2` | `Ω ≈ 0.500`, `K = 0.9` | **period 2** — a standing wave of 2 modes |
| `q₃` lock, `W = 1/3` | `Ω ≈ 0.349`, `K = 0.9` | **period 3** — a standing wave of 3 modes |
| a gap, `W` irrational | `Ω = ρ`, `K = 0.2` | **no period** — quasiperiodic, never repeats |

Inside a tongue the orbit settles into a `q`-cycle and stands; in a gap it
wanders forever. The `{2,3}` of the framework live here, as the widest
standing waves of the `×3/÷2` staircase.

---

## What this does and does not show

**Does (supportable, checked):**
- The bare ratio of the two forced primes, run as dynamics, is a genuine
  mode-locking system: rotation number `log₂(3/2)` whose locks are
  Stern–Brocot mediants (the equal temperaments), and a devil's staircase
  whose widest Arnold tongues are the `{2,3}` denominators.
- The locked plateaus are standing waves in the literal sense (periodic
  orbits of period `q`); `q₂` and `q₃` give the period-2 and period-3
  resonances.

**Does NOT (guard rails):**
- This is the framework's *own* structure (`minimum_alphabet.md` derives the
  staircase from the four primitives). The note **reads** that structure in
  the `×3/÷2` / circle-of-fifths vocabulary and confirms the `{2,3}`
  dominance numerically; it does **not** add a new derivation or constant.
- It does **not** import the physical-forcing claims for `(q₂, q₃) = (2,3)`.
  Those rest on the Klein-bottle / gauge arguments in harmonics and are
  audited separately; here `{2,3}` enter as the bare ratio whose dynamics we
  run.
- The `{2,3}`-dominance of tongue *widths* is the Stern–Brocot ordering
  (`width ∝ (K/2)^q`), a property of the staircase, not evidence for any
  particular physical claim downstream of it.

---

## The shared place — and its boundary

This note establishes the half of the `{2,3}`↔Collatz question that *does*
hold: the `×3/÷2` skeleton is a real mode-locking staircase, and `{2,3}` are
its widest standing waves — the same Stern–Brocot object the framework
derives. That is the arena.

The other half is the boundary. **Collatz adds a `+1`**, and the `+1` pushes
orbits off the plateaus into the gaps: the parity dynamics become a full
shift (maximal complexity, no eventual periodicity — see
`../collatz/minimal_chaos.md`). So Collatz inhabits this staircase, but in
its *unlocked* regime — the part that admits **no** standing wave. The
framework supplies the stage and its resonances; Collatz is what plays out
between them, where nothing stands still. The two studies are one picture:
the locked locks here, the unlocked complement there.

---

## Open / could-sharpen

1. **Completion at `K = 1`.** The framework calls `K = 1` the critical point
   where the plateaus cover measure 1 and the gaps are a measure-zero Cantor
   set (`harmonics:minimum_alphabet.md` Part III). Quantifying the locked
   measure here is resolution-limited (a finite Ω-grid undercounts narrow
   tongues); a Farey/Stern–Brocot tongue-width sum would give the exact
   statement and is the natural next check.
2. **Where exactly is `ρ`?** `ρ = log₂(3/2)` is irrational, so it sits in the
   Cantor complement (no exact lock); its convergents `7/12, 24/41, …` are
   the standing waves that bracket it. How the *bracketing* depth relates to
   the framework's forced depth (≤ 6) is a sharper question than this note
   resolves.

---

## Check

`standing_waves.py` — pure Python, no numpy, deterministic. Prints S1 (the
rotation, its continued fraction, convergents = equal temperaments, all on
the Stern–Brocot descent), S2 (circle-map tongue widths by denominator at
`K = 1`), and S3 (period-2 and period-3 standing waves located by winding
number, and the aperiodic gap).

## References

- Internal (this repo): `standing_waves.py`; companion
  `../collatz/minimal_chaos.md` (the unlocked complement).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (derivation of `S¹`, the circle map, the devil's staircase, and the
  Stern–Brocot ordering of locks from the four primitives; the `K = 1`
  criticality and completion discussion). Referenced, not reproduced; the
  substrate of record is harmonics (see `../README.md`).
- External: the circle map / Arnold tongues / devil's staircase
  (Arnold 1965; Jensen–Bak–Bohr); the circle of fifths and equal-temperament
  convergents of `log₂(3/2)` (continued-fraction theory of musical tuning).
