# Depth Discrimination: q beats the count (rank-1 tongues)

## Status / classification (read first)

**Class 2 — framework-internal demonstration.** This is the discriminating
test for the canonical-depth claim of `../farey/ford_apollonian.md` ("depth
is the curvature `q²`, not the soft tree-level count"), run on the
framework's own rank-1 object — the sine circle map's Arnold tongues, the
same dynamics `standing_waves.py` runs.

**Gate note.** It runs the framework's *own* dynamics and controls against a
**within-framework** shuffle of its own computed widths. It is **not** an
empirical test against external data — those live in the sibling scope
(`lunar-theory`). It answers an internal-consistency question, and it is the
rank-1 analogue of the open `lunar-theory #20` question (is the locked
census organized by curvature-depth, or only by a soft count?), tested where
`q²`-depth is canonical.

Companion check: `depth_discrimination.py` (pure Python, deterministic,
`random.seed(0)`; prints every number below).

---

## The test

Tongue width scales as `(K/2)^q` — governed by the **denominator `q`** (the
curvature-depth), not by the tree level. Because `q` and tree level
correlate but differ (same level → many `q`; `ford_apollonian` T3), they can
be separated:

- **D1** — which measure organizes `−log(width)`?
- **D2 (the discriminator)** — *within a fixed tree level*, does `−log(width)`
  still rise with `q`? If yes, `q` organizes width beyond the count. Null:
  shuffle `q` within each level (20 000 seeded draws) and ask whether the
  observed within-level trend is beaten by chance.

---

## What the check shows (K = 0.9, 17 tongues, 2 ≤ q ≤ 7)

**D1 — `q` is the organizer.** Spearman of `−log(width)` with:

| measure | Spearman |
|---|---|
| denominator `q` (curvature-depth) | **+0.9749** |
| Stern–Brocot tree level (count) | +0.8937 |
| continued-fraction length (count) | +0.2920 |

**D2 — `q` carries information beyond the count.** Usable levels (≥3 tongues,
≥2 distinct `q`): {3, 4}. Observed mean within-level Spearman(`−log width`,
`q`) = **+0.9330**; the within-level shuffle null gives
`p = 214/20000 = 0.0107`. So even at fixed tree level, narrower tongues are
the higher-`q` ones — the curvature-depth does work the count cannot.

**Verdict:** on the framework's own rank-1 tongues, "depth" is `q` (curvature),
not the soft count — supporting `ford_apollonian`'s canonical depth.

---

## What this does and does not show

**Does:** on the rank-1 circle map, `q` organizes tongue width better than
either count (D1), and beats a within-level shuffle (D2, `p = 0.011`).

**Does NOT:**
- **Small basis.** Only two tree levels are usable at `q ≤ 7`; the `p = 0.011`
  is *suggestive*, not decisive. `q` and tree level are themselves strongly
  correlated, so D2 removes only part of the confound.
- It is **framework-internal** (own dynamics, within-framework null), not an
  external empirical test.
- It does **not** validate `lunar-theory #20`. That census is **rank-2**: its
  `free_group` words live in `F₂`, not PSL(2,ℤ), so `q²`-depth is *not*
  canonical there. #20 stays a **regularity** until a rank-2 canonical depth
  is found. This note resolves the *principle* (depth = curvature) on the
  object where it is canonical; the rank-2 transfer is open.

---

## Open / could-sharpen

1. **More levels.** Pushing to `q ≤ 10` (finer Ω grid) would add usable
   levels and tighten D2 beyond "suggestive."
2. **The rank-2 canonical depth.** What plays the role of `q²` for `F₂` braid
   words? Until that exists, #20 cannot be discriminated. The
   `ford_apollonian` Ford→Apollonian (rank-1→rank-2) lift is the natural
   place to look.

---

## Check

`depth_discrimination.py` — pure Python, no numpy, deterministic
(`random.seed(0)`). Measures circle-map tongue widths on a 6000-point Ω grid
at `K = 0.9`, then prints D1 (Spearman of `−log width` vs `q`, tree level,
CF-length) and D2 (within-level Spearman vs a 20 000-draw shuffle null).

## References

- Internal: `depth_discrimination.py`; `../farey/ford_apollonian.md` (the
  canonical-depth claim this tests), `standing_waves.md` (the same circle-map
  dynamics), `../three_body/no_closed_form.md` (rank-1 vs rank-2).
- Sibling: `lunar-theory` `#20` (the rank-2 census this is the rank-1 analogue
  of; held as a regularity).
- External: the sine circle map / Arnold tongues (Arnold 1965; widths
  `(K/2)^q`).
