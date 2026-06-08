"""
ford_apollonian.py

Stern-Brocot "depth" made canonical: ONE rigidity in THREE faces.

The framework's notion of Stern-Brocot depth is ambiguous as a raw count
(tree level / continued-fraction length). But the tree carries a rigid
geometric structure that fixes a canonical depth. The single fact behind
all of it is the UNIT DETERMINANT:

    |b c - a d| = 1   for every tree-adjacent pair a/b, c/d.

(This is already in the repo: completion/sb_boundary.md "every tree-adjacent
pair is unimodular"; root/golden_root.md "det(M^n) = (-1)^n, |phi.psi| = 1".)

That one floor wears three masks:

  ALGEBRAIC   PSL(2,Z) unimodularity: the minimal nonzero |det| over the
              integer lattice is 1. (golden_root.md)
  METRIC      the resolution / approximation floor 1/q^2 (Hurwitz); phi is
              where it shrinks slowest -- the deepest point. (sb_boundary.md)
  GEOMETRIC   Ford-circle tangency = integer Apollonian curvature. (NEW here)

Draw each reduced p/q as a FORD CIRCLE: centre (p/q, 1/(2q^2)), radius
1/(2q^2), curvature kappa = 2 q^2.  This script shows, with exact integer
arithmetic where possible:

  T1  TANGENCY = UNIMODULARITY.  For p/q, p'/q' the squared "tangency gap"
      d^2 - (r+r')^2 = (D^2 - 1)/(q^2 q'^2),  D = p q' - p' q.
      So the Ford circles are TANGENT (gap 0) iff |D| = 1 -- exactly the
      tree-adjacency / unimodular condition.  |D|>1 => a positive gap.

  T2  MEDIANT = APOLLONIAN INSCRIPTION.  The mediant (p+p')/(q+q') is the
      unique circle inscribed between two tangent Ford circles and the line.
      Descartes' theorem with curvatures (2q^2, 2q'^2, 0) gives
      kappa_4 = 2q^2 + 2q'^2 + 4qq' = 2(q+q')^2 -- the Ford curvature of the
      mediant, an INTEGER.  The tree's generating operation IS Apollonian
      inscription; curvatures stay integral (an integral Apollonian gasket).

  T3  CANONICAL DEPTH: q^2 (rigid), NOT tree level (soft).  At a FIXED
      Stern-Brocot level the denominators -- and so the curvatures 2q^2 --
      vary widely.  Tree level counts generations; curvature q^2 is the
      Moebius/Descartes-canonical size.  This is the de-ambiguation: the
      framework's depth is the curvature, not the count.

  T4  phi IS THE DEEPEST.  Along the golden path the denominators are the
      Fibonacci numbers, so the curvature grows by the SLOWEST possible
      factor phi^2 = 2.6180 per level.  Slowest curvature growth = the node
      the tree resolves slowest = the worst-approximable real (Hurwitz,
      1/sqrt5), the deepest point of the boundary (root/golden_root.md).

Class 2: a noted structural correspondence (Ford/Apollonian <-> the repo's
unimodular floor). No derivation, no constant, no claim the framework
PRODUCES Apollonian gaskets. Pure Python, no numpy, deterministic.
Run: python3 ford_apollonian.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2


def line(c="="):
    print(c * 72)


def farey(n):
    """Farey sequence F_n in [0,1], ascending, as reduced (p, q)."""
    seq = [(0, 1)]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        seq.append((a, b))
    return seq


# ===========================================================================
line()
print("T1  TANGENCY = UNIMODULARITY   gap d^2-(r+r')^2 = (D^2-1)/(q^2 q'^2)")
line()
print("  Ford circle of p/q: centre (p/q, 1/2q^2), radius 1/2q^2, curvature 2q^2.")
print("  D = p q' - p' q (the determinant). Tangent (gap 0) iff |D| = 1.\n")

F = farey(6)
print(f"  Farey F_6 adjacent pairs ({len(F)} terms): every |D| = 1, every gap = 0")
print(f"    {'a/b':>7s} {'c/d':>7s} {'D':>4s} {'gap (exact)':>14s}")
all_unit = True
for (p, q), (p2, q2) in zip(F, F[1:]):
    D = p * q2 - p2 * q
    gap_num = D * D - 1
    if abs(D) != 1:
        all_unit = False
    if (p, q) in [(0, 1), (1, 4), (1, 3), (2, 5)]:  # a sample of rows
        print(f"    {p:>3d}/{q:<3d} {p2:>3d}/{q2:<3d} {D:>4d} "
              f"{gap_num}/{q*q*q2*q2:<8d} = {gap_num/(q*q*q2*q2):.4f}")
print(f"    ... all {len(F)-1} adjacent pairs unimodular: {all_unit}")
print()
# a NON-adjacent pair: 1/4 and 2/3
p, q, p2, q2 = 1, 4, 2, 3
D = p * q2 - p2 * q
gap = (D * D - 1) / (q * q * q2 * q2)
print(f"  Non-adjacent 1/4 vs 2/3: D = {D}, |D| = {abs(D)} > 1  ->  "
      f"gap = ({D*D}-1)/({q*q*q2*q2}) = {gap:.4f} > 0  (separated, not tangent)")
print()


# ===========================================================================
line()
print("T2  MEDIANT = APOLLONIAN INSCRIPTION   Descartes(2q^2, 2q'^2, 0) = 2(q+q')^2")
line()


def descartes_inscribed(k1, k2, k3):
    """Curvature of the circle inscribed among three mutually tangent ones
    (k3 = 0 is the straight line)."""
    return k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1)


print("  Two tangent Ford circles (curv 2q^2, 2q'^2) and the line (curv 0):")
print(f"    {'a/b':>6s} {'c/d':>6s} {'mediant':>8s} {'Descartes k4':>13s} "
      f"{'2(q+q2)^2':>10s} {'int?':>5s}")
for (p, q), (p2, q2) in [((0, 1), (1, 1)), ((0, 1), (1, 2)), ((1, 3), (1, 2)),
                          ((1, 2), (2, 3)), ((2, 5), (1, 2))]:
    k1, k2 = 2 * q * q, 2 * q2 * q2
    k4 = descartes_inscribed(k1, k2, 0)
    med = 2 * (q + q2) ** 2
    print(f"    {p:>2d}/{q:<2d}  {p2:>2d}/{q2:<2d}  {p+p2:>3d}/{q+q2:<3d}  "
          f"{k4:13.4f} {med:10d} {str(abs(k4-med) < 1e-9):>5s}")
print()
print("  The mediant's Ford curvature = Descartes inscription, always an")
print("  INTEGER (x2): the tree's generating step IS Apollonian inscription.")
print()


# ===========================================================================
line()
print("T3  CANONICAL DEPTH: q^2 (rigid)  vs  tree level (soft)")
line()


def sb_levels(maxlevel):
    """Stern-Brocot / Farey tree on [0,1]; node -> insertion level."""
    nodes = {}
    intervals = [((0, 1), (1, 1))]
    for lvl in range(1, maxlevel + 1):
        nxt = []
        for lft, rgt in intervals:
            m = (lft[0] + rgt[0], lft[1] + rgt[1])
            nodes[m] = lvl
            nxt.append((lft, m))
            nxt.append((m, rgt))
        intervals = nxt
    return nodes


nodes = sb_levels(5)
by_level = {}
for (p, q), lvl in nodes.items():
    by_level.setdefault(lvl, []).append(q)
print("  Same tree level -> a RANGE of denominators q, hence curvatures 2q^2:\n")
print(f"    {'level':>5s} {'denominators q':>26s} {'curvature range 2q^2':>22s}")
for lvl in sorted(by_level):
    qs = sorted(by_level[lvl])
    curv = sorted(set(2 * q * q for q in qs))
    print(f"    {lvl:>5d} {str(qs):>26s} {str([curv[0], curv[-1]]):>22s}")
print()
print("  Tree level counts generations; q^2 is the Moebius/Descartes-canonical")
print("  size. They diverge (one level, many curvatures) -> 'depth' must mean")
print("  the rigid q^2, not the soft count. (This is the #20 discriminator:")
print("  at fixed word-length, does an observable still track q^2?)")
print()


# ===========================================================================
line()
print("T4  phi IS THE DEEPEST   golden path = slowest curvature growth = phi^2")
line()
# golden path convergents on [0,1]: 1/2, 2/3, 3/5, 5/8, ... (Fibonacci)
fib = [1, 1]
for _ in range(12):
    fib.append(fib[-1] + fib[-2])
qs = fib[2:]                      # denominators 2,3,5,8,13,...
print("  golden-path denominators = Fibonacci; curvature 2q^2 grows by ~phi^2:\n")
print(f"    {'q (Fib)':>8s} {'curvature 2q^2':>15s} {'ratio to prev':>14s}")
prev = None
for q in qs[:9]:
    k = 2 * q * q
    r = "" if prev is None else f"{k/prev:.5f}"
    print(f"    {q:>8d} {k:>15d} {r:>14s}")
    prev = k
print()
print(f"  ratio -> phi^2 = {PHI*PHI:.5f}  (the SLOWEST possible growth: CF all-1s).")
print("  Slowest curvature growth = the node the tree resolves slowest = the")
print("  worst-approximable real (Hurwitz 1/sqrt5 = 0.4472136) = the deepest")
print("  point of the boundary (root/golden_root.md, completion/sb_boundary.md).")
print()
line()
print("SUMMARY")
line()
print("  One floor |bc-ad|=1, three faces: PSL(2,Z) det (algebraic) = 1/q^2")
print("  floor (metric) = Ford tangency / integer Apollonian curvature 2q^2")
print(f"  (geometric). Canonical depth = q^2, deepest at phi (ratio phi^2={PHI*PHI:.4f}).")
