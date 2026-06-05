# Collatz as Minimal Discrete Chaos

## Status / classification (read first)

**Class 2 — structural reading of a mechanism. NOT a proof of Collatz,
NOT a new framework constant.** This note reads Collatz as the **unlocked
complement** of the `{2,3}` mode-locking staircase. Its companion study
`../mode_locking/standing_waves.md` shows the bare `×3/÷2` ratio is a
genuine mode-locking system whose standing waves are the `{2,3}` locks;
**this** note shows that adding the `+1` pushes Collatz off those plateaus
into the gaps — *the Collatz conjecture's vocabulary admits no
standing-wave dynamics.* What is offered is a mechanism (why it contracts,
why no second cycle, why its parity is maximally complex), not a theorem.
Companion check: `minimal_chaos.py` (pure-Python, self-contained, every
number below is printed by it).

The register is deliberate. The interesting move is **learning from the
pattern** — why these ratios and operations give this behavior — rather
than chasing an input that would "derive" Collatz and dissolve the
question. The conjecture is left standing; the *engine* underneath it is
what gets read. Two readings make the map legible without resolving it:
the contraction mechanism (below), and the rational extension on the
Stern–Brocot tree.

---

## The object

The Collatz map on positive integers:

    T(n) = n / 2        if n even
    T(n) = 3n + 1       if n odd

Open since 1937; verified to 2^68 ≈ 2.95·10^20 (Barina 2021); no proof.
The obstruction is that the parity sequence looks random, which blocks
any monotone-descent argument.

**Rational extension.** Integers are the boundary of the rationals;
extend `T` to all reduced `p/q ∈ Q⁺`:

    C(p/q) = (p/2) / q          if p even
    C(p/q) = p / (q/2)          if q even
    C(p/q) = (3p+1) / (q+1)     if both odd      (reduce to lowest terms)

On the **Stern–Brocot tree**, the integers `n/1` are the rightmost
branch; the extension fills the interior. At `q = 1`, rule 3 is exactly
standard Collatz. The rational orbits converge to the attractor
`{1/1, 2/1}`: the check runs all 979 reduced fractions with `p, q ≤ 40`
to that 2-cycle in ≤ 74 steps, none escaping.

---

## The mechanism — why these numbers contract

The minimum alphabet (`harmonics:minimum_alphabet.md`) supplies four
primitives — integers, mediant, fixed-point/iteration, parabola. Collatz
is a composition of them, and the composition explains the dynamics.

### M1 — the contraction boundary is `q < q₂²`

Read the generic accelerated map `n → q·n + 1 / n → n/2` as a competition
between expansion by `q₃ = 3` (odd steps) and contraction by `q₂ = 2`
(even steps). Per **odd cycle** — one `×q` followed by the run of forced
halvings — the net multiplier is `q / 2^v`, where `v = v₂(qn+1)` is the
number of times `q₂` divides the result. For a random odd argument the
valuation is geometric with mean `q₂ = 2`, so the expected net multiplier
is

    q / q₂²    →    contracts iff  q < q₂² = 4.

The **only odd multiplier inside the window** `(1, 4)` is `q = 3`: Collatz
is the unique odd `qn+1` map that contracts at all, sitting one unit under
the wall `q₂² = 4`. That is the real, `3`-specific content of M1 — and it
needs nothing from the framework beyond the bare ratio `q₃/q₂²`.

> **A coincidence, named as one.** The framework also carries the identity
> `q₃ = q₂² − 1` (and `q₃² − 1 = q₂³`), whose unique positive solution is
> `(2,3)` (`harmonics:mass_sector_closure.md`). It is tempting to read "the
> contraction wall is at `q₂²` and `q₃ = q₂² − 1`" as the framework
> *explaining* Collatz's position. Stripped down, that is just *"3 is the
> odd number immediately below 4 = 2²"* — a small-`{2,3}` arithmetic
> coincidence, not a derivation. The genuine `{2,3}`↔Collatz link is **not**
> here; it is the shared **mode-locking arena** of
> `../mode_locking/standing_waves.md`. This note does not lean on the
> cross-link identity, and (per the audit in that study) does not import its
> physical-forcing claim.

### M2 — the rate, measured

The heuristic above is checked on real orbits, not asserted:

| quantity | predicted | measured (`minimal_chaos.py`) |
|---|---|---|
| `E[v₂(3n+1)]` over random odd `n` | `q₂ = 2` | `1.9976` |
| net per-odd-cycle multiplier | `q₃/q₂² = 3/4 = 0.750` | `0.747` |

The same formula sends `5n+1` to `5/4 > 1`. The dynamical check confirms
the boundary is real and not cosmetic:

| map | rate `q/4` | integers `2…1999` |
|---|---|---|
| `3n+1` | `0.75` | **1998 / 1998 reach 1** |
| `5n+1` | `1.25` | 113 reach 1, 143 fall into other cycles, **1742 diverge** |

So the framework's `{2,3}` structure does not predict *that* `3n+1` is
true — it predicts *where the transition is*. `q = 3` is special because
`3 < 2²`; `q = 5, 7, 9` expand, and `5n+1` visibly fails to converge. The
pattern is the prediction.

### M3 — the `+1` is the mediant with the tree root

Rule 3 of the rational map is not "triple and nudge." `(3p+1)/(q+1)` is
the **mediant** of `3·(p/q)` with `1/1`, the root of the Stern–Brocot
tree:

    mediant( 3p/q , 1/1 ) = (3p + 1)/(q + 1).

Its structural job: when `p, q` are both odd, the mediant makes **both**
the numerator and denominator even, so the next halving exists on either
coordinate. The check verifies this for every reduced odd `p/q` with
`p, q < 60`. The `+1` that makes Collatz mysterious is, in the alphabet,
primitive #2 applied at the tree's basepoint — the one operation that
restores divisibility-by-`q₂`.

### M4 — integers are the `q = 1` boundary, the hard case

In the rational map, interior fractions enjoy extra cancellation at rule
3 (average `gcd(3p+1, q+1) = 5.68`), while integers get the minimum —
always exactly `q₂ = 2`. So the integer Collatz problem is the **minimal-
cancellation boundary** of a map that contracts faster everywhere in the
interior. The famous case is hard precisely because it is the edge of the
tree, where the mediant hands back the least.

---

## What this does and does not show

**Does (supportable, checked):**
- Collatz's contraction-on-average is a consequence of the bare ratio
  `q₃/q₂² = 3/4 < 1`, measured to match (`0.747`). The boundary `q < q₂²`
  correctly separates the convergent `3n+1` from the divergent `5n+1,
  7n+1` — `q = 3` is the unique odd multiplier that contracts.
- The `+1` is the mediant primitive at the Stern–Brocot root; the
  integers are the `q = 1` boundary (the hard case) of a rational map that
  is gentler in its interior.
- The only integer cycle is `{1, 2}`, because `q₃^a = q₂^b` has no
  positive solution (fundamental theorem of arithmetic).
- Collatz admits **no standing wave**: for the shortcut map, the first-`k`
  parities are a bijection onto `{0,1}^k` (Terras), a full 2-shift of
  entropy `log 2`. No orbit settles into a repeated parity word, so Collatz
  sits in the *gaps* of the `{2,3}` staircase, never on a plateau.

**Does NOT (guard rails):**
- It does **not** prove Collatz. M1–M4 explain why almost every orbit
  contracts; upgrading "almost every orbit equidistributes in parity"
  (Tao 2019, logarithmic density, arXiv:1909.03562) to "**every** orbit"
  is exactly the open conjecture. The framework supplies the mechanism,
  not the theorem.
- It contributes **no** scorecard/MANIFEST claim and **no** new constant.
  `q₂ = 2`, `q₃ = 3` are imported as given; the note explains a known map
  with them, it does not derive them here.
- The contraction *rate* `3/4` is the standard parity-`1/2` /
  `E[v₂] = 2` heuristic, exact only in expectation. The robust, exact
  content is the **boundary** `q < q₂²` and the **unique cycle**.

In one line: *the framework does not solve Collatz — it explains why the
problem has the shape it has, and why 3 and 2 are the numbers that make
the shape.*

---

## The pattern, stated plainly

Collatz is **minimal discrete chaos in the gaps of the `{2,3}`
staircase**. The companion study (`../mode_locking/standing_waves.md`)
establishes the arena: the bare `×3/÷2` ratio is a mode-locking system
whose standing waves — the locked, periodic resonances — are the `{2,3}`
denominators (`q₂` period-2, `q₃` period-3, widest tongues). Collatz adds
the `+1`, and that is the whole story:

- the **arena** is the Stern–Brocot tree / circle-map staircase (integers
  = `q₂`-rich boundary), shared with the standing-wave study;
- the **expansion** is `×q₃`, the **contraction** is `÷q₂`, net drift
  `q₃/q₂² = 3/4 < 1` — measured, and `3`-specific;
- the **`+1` is the mediant with the root**, and it is exactly what drives
  orbits *off* the plateaus: the parity dynamics become a full 2-shift (no
  eventual periodicity, no standing wave);
- the **residue** — whether *every* orbit, not just almost every, obeys
  the drift — is the conjecture, left open.

So the `{2,3}` of Collatz and the `{2,3}` of the framework do share a place
— the mode-locking staircase — but Collatz lives in its **unlocked
complement**, the regime that admits no standing wave. That placement is
the honest payoff: it says *why* Collatz is hard (its symbolic dynamics are
maximally complex, so there is no resonance to lock onto and exploit),
without pretending the framework resolves it. The contraction, the unique
cycle, the full-shift parity are the genuinely structural part; the
pointwise upgrade is what the framework cannot hand over, and that limit is
named, not hidden.

---

## Open / could-sharpen

1. **The open step as a no-standing-wave statement.** The mechanism
   reduces Collatz to "no orbit sustains an odd-step frequency above the
   contraction threshold indefinitely." Given M5 (the parity dynamics are a
   full 2-shift), this is precisely the statement that no orbit locks onto a
   standing wave of the `{2,3}` staircase that would defeat the drift. Can
   the conjecture be phrased exactly as a mode-locking *exclusion* on the
   staircase of `../mode_locking/standing_waves.md`? That would be a
   framework-native restatement, not a proof.
2. **Why `E[v₂] = q₂` exactly.** The rate `3/4` depends on the valuation
   mean being `q₂ = 2`. Is that itself an alphabet fact (the `2`-adic
   measure of `3n+1` over odd `n`), or incidental? The check measures it;
   a derivation would tighten M2 from heuristic to exact.
3. **The interior as a regularization.** Interior fractions contract
   faster (M4). Is there a continuity-in-`q` statement — the rational map
   as a smoothing of the integer boundary — that the hard case inherits a
   bound from?

---

## Check

`minimal_chaos.py` — pure Python, no numpy, deterministic (seeded). Prints
M1 (boundary), M2 (`E[v₂]`, measured rate, `3n+1` vs `5n+1` dynamics), M3
(mediant identity + both-even), M4 (cancellation asymmetry, rational
convergence), M5 (the Terras parity bijection — full 2-shift / no standing
wave), and the unique-cycle / where-the-conjecture-lives summary.

## References

- Collatz problem; Barina, *Convergence verification of the Collatz
  problem*, J. Supercomput. **77** (2021) — verified to 2^68.
- T. Tao, *Almost all orbits of the Collatz map attain almost bounded
  values*, arXiv:1909.03562 (2019) — "almost all" in logarithmic density;
  the gap to "all" is the conjecture.
- R. Terras, *A stopping time problem on the positive integers*, Acta
  Arith. **30** (1976) — the parity-vector / coefficient-stopping-time
  structure underlying M5's bijection.
- Internal (this repo): `minimal_chaos.py`; companion study
  `../mode_locking/standing_waves.md` (the locked `{2,3}` arena whose
  unlocked complement this note reads).
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (the four primitives; staircase / parity as winding number),
  `mass_sector_closure.md` (the cross-link identity `q₃ = q₂² − 1`,
  `q₃² − 1 = q₂³`, unique solution `(2,3)` — invoked here only as a named
  coincidence, not a bridge), `canonical_glossary.md` §5 (mediant = PSL(2,ℤ)
  Farey generator). Referenced, not reproduced; the substrate of record for
  framework claims is harmonics (see `../README.md`).
