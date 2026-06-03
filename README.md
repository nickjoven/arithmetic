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
input that would dissolve the question. Collatz is the model: the framework
explains *why* `3` and `2` produce contraction-to-an-attractor (and why
`5n+1` does not), and then leaves the conjecture itself standing. That is
the intended shape of every study here.

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
| [`collatz/minimal_chaos.md`](collatz/minimal_chaos.md) | Collatz `3n+1` | Minimal discrete chaos: contraction at rate `q₃/q₂² = 3/4`, boundary `q < q₂²`, the `+1` as the mediant with the tree root. Conjecture left open. |

Each study is a markdown note plus a pure-Python check (`no numpy`,
self-contained, deterministic) that prints every number the note cites.

```
python3 collatz/minimal_chaos.py
```

## Discipline

The working discipline imported from harmonics — knowledge as a cache of
the substrate, verify-before-assert, the Class 1–5 ladder — is in
[`CLAUDE.md`](CLAUDE.md). The canonical-claims index, scoped to Class 2
only, is in [`MANIFEST.yml`](MANIFEST.yml).
