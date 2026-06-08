# Ford / Apollonian: Stern–Brocot Depth Made Canonical

## Status / classification (read first)

**Class 2 — structural reading.** This note observes that the framework's
ambiguous notion of *Stern–Brocot depth* has a rigid, canonical realization,
and that **one fact** — the unit determinant `|bc − ad| = 1` — underlies
three things the repo otherwise treats separately: PSL(2,ℤ) unimodularity,
the `1/q²` resolution floor, and (the new observation here) Ford-circle
tangency / integer Apollonian curvature. The canonical depth of a node is
its **curvature `q²`**, not its tree level.

**What it is NOT.** It does **not** claim the framework *derives* or
*produces* Ford circles or Apollonian gaskets — those are classical objects
(Ford 1938; Descartes' circle theorem). The Class-2 content is the
**correspondence**: the repo already commits, independently, to the
algebraic face (`completion/sb_boundary.md`: "every tree-adjacent pair is
unimodular") and the metric face (`sb_boundary.md`: the `1/q²` floor;
`root/golden_root.md`: `|φ·ψ| = |det M| = 1`); this note shows the geometric
face is the *same object*, and uses it to fix "depth." No new constant, no
derivation.

Companion check: `ford_apollonian.py` (pure Python, deterministic; prints
every number below).

---

## The object

Map each reduced `p/q` to its **Ford circle**: centre `(p/q, 1/2q²)`, radius
`1/2q²`, curvature `κ = 2q²`. Two facts make this the geometry of the tree:

- two Ford circles are **tangent** iff `|p q′ − p′ q| = 1` — the
  tree-adjacency / unimodular condition;
- the **mediant** `(p+p′)/(q+q′)` is the unique circle inscribed in the
  curvilinear triangle between two tangent circles and the real line.

So the tree's seed-and-mediant generation *is* a circle packing, and its
adjacency *is* the unit determinant. The completion study's `1/q²` floor and
the golden-root study's `det M = ±1` are the metric and algebraic shadows of
this one geometric picture.

---

## Weak layer vs strong layer (kept apart)

**Weak layer** (classical, generic): that the Farey tree has a Ford-circle
realization, and that Ford packings are (degenerate) Apollonian gaskets, is
standard since Ford (1938). No framework content on its own.

**Strong layer** (framework-native, the point): the repo had *already*
fixed two faces of this independently — `|bc−ad|=1` (`sb_boundary.md:34`) and
`det M = ±1` (`golden_root.md:65`) — without naming the geometry. The
non-generic content is that **these are one object**, and that identifying
them resolves a standing ambiguity: the framework's "depth" is not the soft
tree-level count but the **rigid curvature `q²`** (= `1/`floor =
matrix-entry size = PSL(2,ℤ) translation length). That sharpening is what
feeds the open `lunar-theory` `#20` question (below).

---

## What the check shows

### T1 — tangency = unimodularity (exact)

For Ford circles of `p/q`, `p′/q′`, the squared tangency gap is exactly

    d² − (r + r′)² = (D² − 1)/(q² q′²),    D = p q′ − p′ q.

So the circles are **tangent (gap 0) iff `|D| = 1`** — the unimodular,
tree-adjacency condition. All 12 adjacent pairs of `F₆` give `|D| = 1`, gap
`0`. A non-adjacent pair `1/4` vs `2/3` has `D = −5`, gap
`(25−1)/144 = 0.1667 > 0` (separated). The repo's "tree-adjacent =
unimodular" and the geometry's "tangent" are the same statement.

### T2 — mediant = Apollonian inscription (integer curvature)

Descartes' theorem for two tangent Ford circles `(2q², 2q′²)` and the line
`(0)` gives the inscribed curvature

    κ₄ = 2q² + 2q′² + 2√(4q²q′²) = 2(q + q′)²,

which is exactly the Ford curvature of the **mediant** — an integer. Checked:
`(0/1,1/1)→1/2: 8`, `(0/1,1/2)→1/3: 18`, `(1/3,1/2)→2/5: 50`,
`(2/5,1/2)→3/7: 98`. The tree's generating step *is* Apollonian inscription,
and curvatures stay integral (an integral Apollonian gasket).

### T3 — canonical depth: `q²` (rigid), not tree level (soft)

At a **fixed** Stern–Brocot level the denominators — and so the curvatures
`2q²` — span a range:

| level | denominators `q` | curvature range `2q²` |
|---|---|---|
| 1 | {2} | [8, 8] |
| 2 | {3} | [18, 18] |
| 3 | {4, 5} | [32, 50] |
| 4 | {5, 7, 8} | [50, 128] |
| 5 | {6, 9, 10, 11, 12, 13} | [72, 338] |

Tree level counts generations; `q²` is the Möbius/Descartes-canonical size.
They diverge (one level → many curvatures), so the framework's "depth" must
mean the **rigid `q²`**, not the soft count.

### T4 — `φ` is the deepest (slowest curvature growth)

Along the golden path the denominators are the Fibonacci numbers, so the
curvature grows by the **slowest possible** factor — the continued fraction
is all `1`s. The ratio of successive curvatures converges to

    φ² = 2.61803…

(2.25, 2.778, 2.560, 2.641, 2.609, 2.621, … → 2.61803). Slowest curvature
growth = the node the tree resolves slowest = the worst-approximable real
(Hurwitz, `1/√5 = 0.4472136`) = the deepest point of the boundary
(`root/golden_root.md`, `completion/sb_boundary.md`).

---

## What this does and does not show

**Does (supportable, checked):**
- The exact identity `d² − (r+r′)² = (D²−1)/(q²q′²)`: Ford tangency *is* the
  unimodular floor `|D| = 1`.
- The mediant *is* Descartes inscription, with integer curvature `2(q+q′)²`.
- Tree level and curvature `q²` genuinely diverge; the canonical depth is
  `q²`. The golden path has the slowest curvature growth, `φ²`.

**Does NOT (guard rails):**
- It does **not** claim the framework derives/produces Ford circles or
  Apollonian gaskets; those are classical. The Class-2 content is that the
  repo's *own* unimodular floor and `1/q²` floor are this geometry.
- "Canonical depth = `q²`" is a **reading** that resolves an ambiguity; it
  is not a forced framework quantity. It is offered because it is
  Möbius/Descartes-invariant where the tree-level count is not.
- The `Ford → Apollonian` = `rank-1 → rank-2` lift (a 1-D line's packing
  vs the 2-D plane's gasket) is **suggested, not shown** (see Open).

---

## The shared place — and the `#20` payoff

This note ties three studies together at one floor: `completion/sb_boundary.md`
(the `1/q²` floor), `root/golden_root.md` (`det M = ±1`), and the geometry
here. Its working payoff is for the *empirical* sibling: the `lunar-theory`
`#20` claim (the Li & Liao locked census) landed only as a **regularity**
(`T* ∝ L_f`, word length) because word length is the *soft* depth and the
correlation may be generic. The canonical-depth result gives the
**discriminating null**: at *fixed* word length, does an observable still
track the rigid curvature `q²`? If yes, the structure is framework-specific;
if flat, it was generic monotonicity. The clean form lives on the **rank-1**
Farey / Arnold-tongue objects, where `q²`-depth is canonical — *not*
automatically on the rank-2 braid catalog, whose `free_group` words live in
`F₂`, not PSL(2,ℤ). (Building that null is the next step.)

---

## Open / could-sharpen

1. **Ford → Apollonian as rank-1 → rank-2.** Ford circles sit on a 1-D line
   (rank-1 Farey); a full Apollonian gasket fills the 2-D plane. The lift may
   *be* the rank-1 → rank-2 step of `three_body/no_closed_form.md`; the
   Apollonian group generalizes PSL(2,ℤ) from line to plane, and its residual
   set has a fixed fractal dimension (≈ 1.3057) — a metric "floor." Not shown
   here.
2. **Which "unitary floor"?** This note reads the floor as the unit
   determinant `|det| = 1`. A metric reading (the modular surface's systole /
   minimal geodesic length) is an alternative; whether they coincide for the
   framework's purposes is open.
3. **`Σ 1/q²` and the locked measure.** `sb_boundary.md` notes
   `Σ 1/q²` ties to the `K=1` locked measure of `mode_locking/`. Curvature
   `2q²` is its reciprocal; relating the tongue-width sum to the Ford-curvature
   spectrum is a sharper statement than this note makes.

---

## Check

`ford_apollonian.py` — pure Python, no numpy, deterministic. Prints T1 (the
exact tangency-gap identity `(D²−1)/(q²q′²)`, zero iff unimodular), T2 (the
mediant as Descartes inscription, integer curvature `2(q+q′)²`), T3 (same
tree level → curvature range, so depth = `q²`), and T4 (the golden path's
curvature growth → `φ² = 2.61803`).

## References

- Internal (this repo): `ford_apollonian.py`; `completion/sb_boundary.md`
  (the `1/q²` floor and unimodular adjacency), `root/golden_root.md`
  (`det M = ±1`, Cassini, `|φψ| = 1`), `farey/equidistribution.md` (the tree),
  `mode_locking/standing_waves.md` (`Σ 1/q²` locked measure),
  `three_body/no_closed_form.md` (the rank-1 → rank-2 axis).
- Cross-repo substrate (`nickjoven/harmonics`, pinned in `../MANIFEST.yml`):
  `minimum_alphabet.md` (the mediant, the `1/q²` floor, Part III);
  `canonical_glossary.md` (mediant = PSL(2,ℤ) generator). Referenced, not
  reproduced.
- External: L. R. Ford, *Fractions* (1938, Ford circles); Descartes' circle
  theorem / integral Apollonian gaskets; A. Hurwitz (1891, `1/√5`);
  PSL(2,ℤ) ≅ ℤ/2 ∗ ℤ/3 acting on `ℍ`.
