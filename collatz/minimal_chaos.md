# Collatz as Minimal Discrete Chaos

## Status / classification (read first)

**Class 2 — structural reading of a mechanism. NOT a proof of Collatz,
NOT a new framework constant.** This note records *why* the Collatz
operations produce contraction-to-an-attractor, stated in the framework's
two forced primes `q₂ = 2`, `q₃ = 3`. The hard part of the conjecture
(every orbit reaches 1, not merely almost every) is **untouched** and is
located explicitly below. What is offered is a mechanism, not a theorem.
Companion check: `minimal_chaos.py` (pure-Python, self-contained, every
number below is printed by it).

The register here is deliberate. The interesting move is **learning from
the pattern** — understanding why these particular ratios and operations
give the behavior they do — rather than chasing an input that would
"derive" Collatz and, in doing so, dissolve the question. The conjecture
is left standing; the *engine* underneath it is what gets read.

---

## The object

The Collatz map on positive integers:

    T(n) = n / 2        if n even
    T(n) = 3n + 1       if n odd

Open since 1937; verified to 2^68 ≈ 2.95·10^20 (Barina 2021); no proof.
The obstruction is that the parity sequence looks random, which blocks
any monotone-descent argument.

Two framework readings make the map legible without resolving it.

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

The **only odd multiplier inside the window** `(1, 4)` is `q = 3`. And the
framework's own cross-link identity between its two primes is

    q₃ = q₂² − 1 = 3,

so **Collatz sits exactly one unit under the contraction wall.** It is the
boundary case of the smallest map that contracts at all. (`harmonics`
forces `(q₂, q₃) = (2, 3)` via `q₂² − 1 = q₃`, `q₃² − 1 = q₂³` — see
`harmonics:farey_partition.md`; here we only borrow the arithmetic of the
identity, not its physical forcing.)

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
- Collatz's contraction-on-average is a consequence of `q₃ < q₂²`, with
  rate `q₃/q₂² = 3/4` measured to match. The two forced primes and their
  cross-link `q₃ = q₂² − 1` place `3n+1` at the contraction boundary, and
  the boundary correctly separates the convergent `3n+1` from the
  divergent `5n+1, 7n+1`.
- The `+1` is the mediant primitive at the Stern–Brocot root; the
  integers are the `q = 1` boundary (the hard case) of a rational map that
  is gentler in its interior.
- The only integer cycle is `{1, 2}`, because `q₃^a = q₂^b` has no
  positive solution (fundamental theorem of arithmetic).

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

Collatz is the **minimal discrete-chaos map**: the smallest competition
between the two forced primes that lands just inside contraction. Read
through the alphabet —

- the **arena** is the Stern–Brocot tree (integers = `q₂`-rich boundary);
- the **expansion** is `×q₃`, the **contraction** is `÷q₂`;
- the **restoring move** is the mediant with the root (`+1`);
- the **net drift** is `q₃/q₂² < 1`, guaranteed by `q₃ = q₂² − 1`;
- the **residue** — whether *every* orbit, not just almost every, obeys
  the drift — is the conjecture, and it is left open.

This is the "learning from the pattern" register: the contraction, the
unique cycle, the boundary against `5n+1` are all consequences of `{2,3}`
and the mediant, and they are the genuinely structural part. What the
framework cannot hand over is the pointwise upgrade — and that limit is
honest, not hidden.

---

## Open / could-sharpen

1. **Parity equidistribution as a tongue statement.** The mechanism
   reduces Collatz to "no orbit sustains an odd-step frequency above the
   contraction threshold indefinitely." In the circle-map picture
   (`harmonics:minimum_alphabet.md` §staircase) parity frequency is a
   winding number; can the open step be phrased as a mode-locking
   exclusion on the staircase? That would be a framework-native
   restatement, not a proof.
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
convergence), and the unique-cycle / where-the-conjecture-lives summary.

## References

- Collatz problem; Barina, *Convergence verification of the Collatz
  problem*, J. Supercomput. **77** (2021) — verified to 2^68.
- T. Tao, *Almost all orbits of the Collatz map attain almost bounded
  values*, arXiv:1909.03562 (2019) — "almost all" in logarithmic density;
  the gap to "all" is the conjecture.
- Internal (this repo): `minimal_chaos.py`.
- Cross-repo substrate (`nickjoven/harmonics`): `minimum_alphabet.md`
  (the four primitives; staircase / parity as winding number),
  `farey_partition.md` (`(q₂,q₃) = (2,3)` and the cross-link identity
  `q₃ = q₂² − 1`), `canonical_glossary.md` §5 (mediant = PSL(2,ℤ) Farey
  generator). These are referenced, not reproduced; the substrate of
  record for the framework claims is harmonics (see `../README.md`).
