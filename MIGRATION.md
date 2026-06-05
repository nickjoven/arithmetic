# Migration / provenance

This repo is the standalone home of the **vocabulary-studies** content
staged inside harmonics by
[harmonics#210](https://github.com/nickjoven/harmonics/pull/210)
("Stage vocabulary-studies (federated): Ramanujan / Collatz / Riemann
through the minimum alphabet"). The PR's own framing — *"vocabulary-studies
= arithmetic"* — is why this repo is named `arithmetic`.

## Why these readings live here, not in the harmonics spine

The harmonics derivation spine (`sync_cost/derivations/`) makes
load-bearing quantitative claims backed by a content-addressed substrate
and gated on drift. The studies here make **none** — they are Class 2
structural readings of objects the framework did not produce. Keeping them
out of the spine prevents a reader (or a drift check) from mistaking a
"noted correspondence" for a sealed derivation. Different register,
different repo.

## The federation boundary

| | harmonics | arithmetic (this repo) |
|---|---|---|
| Holds | the derivation spine + substrate | Class 2 readings only |
| Substrate of record | yes (`.ket`) | no — defers to harmonics |
| Makes scorecard/MANIFEST claims | yes | no |
| References the other | — | by name, as `harmonics:<path>` |

Concepts such as `(q₂, q₃) = (2, 3)`, the cross-link `q₃ = q₂² − 1`, the
four primitives of `minimum_alphabet.md`, and the mediant ↔ PSL(2,ℤ)
identification are **referenced, not reproduced**. The authority on what
they say is the harmonics substrate. If a borrowed claim here disagrees
with harmonics, harmonics is right and the note here is stale.

## Status of the staged content

| Study | In harmonics | In this repo |
|---|---|---|
| Collatz (minimal chaos) | source material in spine + `docs/archive/collatz.html` | **authored** (`collatz/`) |
| Ramanujan 1/π thread (3 notes + check) | exists on branch `claude/ramanujan-pi-formula-*` | not yet ported |
| Farey / Riemann synthesis (capstone) | — | not yet authored |

The Collatz study was authored first, as the model for the register: it
reads the *mechanism* (why `3` and `2` give contraction) and leaves the
conjecture open, rather than chasing an input that would "derive" it. The
remaining studies, when ported/authored, must carry the same guard rails
(see `CLAUDE.md`).

## Lifting further (if ever)

If this repo is later folded back, mirrored, or re-homed, the only hard
requirement is preserved: the **substrate of record stays harmonics**, and
every framework reference here remains a `harmonics:<path>` pointer, never a
reproduced source of truth.
