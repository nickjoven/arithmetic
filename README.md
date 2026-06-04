# arithmetic

A federated sibling of [`nickjoven/harmonics`](https://github.com/nickjoven/harmonics)
holding **Class 2 structural readings** — explorations of famous
mathematical objects (Collatz, Ramanujan's 1/π, the Riemann/Farey
question) *through* the harmonics framework's minimum alphabet, rather
than derivations inside it.

These readings are a different register from the derivation spine and
deliberately do **not** live in harmonics' `sync_cost/derivations/`. The
spine makes load-bearing quantitative claims backed by a content-addressed
substrate; this repo makes none. It studies what the framework's vocabulary
— the two forced primes `{q₂, q₃} = {2, 3}`, the mediant, the Stern–Brocot
tree, the parabola — *says about* objects it did not produce.

## The one rule

Everything here is **Class 2**: a noted structural correspondence with **no
claim of derivation, no prediction, and no new framework constant.** A
reading that crosses that line — that claims the framework *derives* π, or
*proves* Collatz — is a bug, not a result. The status header at the top of
each note states this explicitly; if a note's body drifts from its header,
the header wins.

The interesting move is **learning from the pattern**, not pursuing an
input that would dissolve the question. The studies share one axis —
**locked vs unlocked**: the bare `×3/÷2` ratio is a genuine mode-locking
staircase whose standing waves are the `{2,3}` locks (`mode_locking/`);
Collatz is what that same staircase looks like in its **unlocked
complement** — the regime that admits no standing wave, which is *why* the
conjecture is hard (`collatz/`); and the Riemann Hypothesis is the unlocked
*asymptotic* face of the same tree — maximal equidistribution, via
Franel–Landau (`farey/`). The framework supplies the locked arena and its
resonances; each study locates an object inside it and leaves the open
problem standing.

A claim only earns its `{2,3}` framing if **running the dynamics** produces
the framework's structure (Arnold tongues, mode-locking, the Stern–Brocot
staircase) — not merely because the numbers `2` and `3` appear. Where a
framework-internal forcing claim is invoked, it is audited against the
harmonics substrate first, and any gap is named in the study (see, e.g.,
the `Γ₀(6)` / `{2,3}`-forcing audit notes in `MANIFEST.yml`).

## Provenance — the substrate of record is harmonics

This repo references the framework's concepts (`minimum_alphabet.md`,
`farey_partition.md`, `canonical_glossary.md`, the forcing of
`(q₂, q₃) = (2, 3)`) **by name**; it does not reproduce or re-derive them.
The authority on what any framework concept says is the harmonics substrate
(today a BLAKE3-addressed `.ket` store), not this repo and not a reader's
memory. Cross-repo references are written `harmonics:<path>`. If a borrowed
claim and the substrate disagree, the substrate is right and the note is
stale — re-read it before relying on it.

This repo is the standalone home of the content staged in
[harmonics#210](https://github.com/nickjoven/harmonics/pull/210)
("vocabulary-studies = arithmetic"); see `MIGRATION.md` for the
relationship.

## Contents

| Study | Object | Reading |
|---|---|---|
| [`mode_locking/standing_waves.md`](mode_locking/standing_waves.md) | the `×3/÷2` ratio | **Locked.** The framework's **standing waves**: rotation `log₂(3/2)` whose locks are Stern–Brocot mediants (the equal temperaments), a devil's staircase whose widest Arnold tongues are the `{2,3}` denominators (`q₂` period-2, `q₃` period-3). The arena. |
| [`collatz/minimal_chaos.md`](collatz/minimal_chaos.md) | Collatz `3n+1` | **Unlocked (dynamical).** Contraction `q₃/q₂² = 3/4`, boundary `q < q₂²`, the `+1` as the mediant with the tree root, and the Terras full-shift (no standing wave) that places Collatz in the staircase's gaps. Conjecture left open. |
| [`collatz/no_dissipation.md`](collatz/no_dissipation.md) | Collatz, provability | **Why geometry can't prove it.** No forced dissipation: ℝ gives only statistical, non-monotone drift; `ℤ₂` is measure-preserving (integers are measure-zero); ℂ/ℍ are the wrong (Archimedean) completion. Cycles fall to arithmetic; divergence must too. |
| [`farey/equidistribution.md`](farey/equidistribution.md) | the Farey tree / Riemann | **Unlocked (asymptotic).** The tree's two faces: finite-depth *counting* (`13/19`, locked) vs asymptotic *equidistribution* (RH via Franel–Landau, unlocked). The framework reads the count, not the limit. |
| [`completion/sb_boundary.md`](completion/sb_boundary.md) | the completion of ℚ (ℝ) | **The closure where both faces meet.** The SB-tree boundary *is* the Archimedean completion (continued fractions as paths); resolves a framework Open item and pins its `1/q²` floor, `0.999…=1`, and `1/φ`-depth claims to exact facts. |
| [`completion/two_completions.md`](completion/two_completions.md) | the 2-adic completion (ℤ₂) | **The other completion.** Collatz's lossy mod-2 is lossless in aggregate (a 2-adic coordinate); its natural home is `ℤ₂`, where the loss is a measure-preserving isometry. The conjecture is the seam *between* ℝ and `ℤ₂` — inside vs outside, made exact. |
| [`root/golden_root.md`](root/golden_root.md) | the framework, from one root | **The singular representation.** One tree, one seed, one operation — and one matrix `[[1,1],[1,0]]` carrying all four primitives, whose eigenvalue `φ` is its own tree's deepest point. Generation and completion in one self-referential object. |

These are one picture along a single axis — **locked** (the `{2,3}`
resonances) vs **unlocked** (the gaps) — with the completion as the boundary
`∂T` that holds both: rationals = finite nodes (locked centres), irrationals
= infinite paths (unlocked gaps). Collatz and Riemann are the two unlocked
problems; the framework owns the locked census. Each study is a markdown note
plus a pure-Python check (`no numpy`, self-contained, deterministic) that
prints every number the note cites.

```
python3 mode_locking/standing_waves.py
python3 collatz/minimal_chaos.py
python3 collatz/no_dissipation.py
python3 farey/equidistribution.py
python3 completion/sb_boundary.py
python3 completion/two_completions.py
python3 root/golden_root.py
```

## Discipline

The working discipline imported from harmonics — knowledge as a cache of
the substrate, verify-before-assert, the Class 1–5 ladder — is in
[`CLAUDE.md`](CLAUDE.md). The canonical-claims index, scoped to Class 2
only, is in [`MANIFEST.yml`](MANIFEST.yml).
