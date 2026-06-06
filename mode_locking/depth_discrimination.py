"""
depth_discrimination.py

The discriminating test for "canonical depth = q^2, not tree level"
(farey/ford_apollonian.md), run on the framework's OWN rank-1 object: the
sine circle map's Arnold tongues. This is the rank-1 analogue of the open
lunar-theory #20 question (is the locked census organized by curvature-depth
or merely by a soft count?), where q^2-depth IS canonical.

Class-2 / gate note: this runs the framework's own dynamics (the circle map,
exactly as mode_locking/standing_waves.py does) and controls against a
WITHIN-FRAMEWORK shuffle of its own computed widths. It is NOT an empirical
test against external data -- those live in the sibling scope. It asks an
internal-consistency question: among the framework's tongues, does the rigid
depth q carry organizing information BEYOND the tree-level count?

THE QUESTION. Tongue width ~ (K/2)^q is governed by the DENOMINATOR q (the
curvature-depth), not by the Stern-Brocot tree level (the soft count). Since
q and level correlate but differ (same level -> many q; ford_apollonian T3),
we can separate them:

  D1  Does -log(width) track q, tree-level, and CF-length? (all should be
      positive; the question is which is the organizer.)
  D2  THE DISCRIMINATOR: WITHIN a fixed tree level, does -log(width) still
      rise with q? If yes, q organizes width beyond the count -> canonical
      depth is real. Null: shuffle q within each level (seeded) -> if the
      observed within-level trend beats the shuffle, the count alone does
      not explain the widths.

Pure Python, no numpy. Deterministic (random.seed(0)). Run:
    python3 depth_discrimination.py
"""

import math
import random
from fractions import Fraction

random.seed(0)

K = 0.9            # sub-critical: finite tongues, width ~ (K/2)^q
QMAX = 7           # denominators 2..7 (q=8 widths approach grid resolution)
M = 6000           # Omega grid over [0,1]
N, BURN = 2500, 1500


def line(c="="):
    print(c * 72)


def winding(Omega, k=K, n=N, burn=BURN):
    th = 0.123456789
    for _ in range(burn):
        th = th + Omega - (k / (2 * math.pi)) * math.sin(2 * math.pi * th)
    t0 = th
    for _ in range(n):
        th = th + Omega - (k / (2 * math.pi)) * math.sin(2 * math.pi * th)
    return (th - t0) / n


def sb_level(p, q):
    """Stern-Brocot insertion level of p/q in [0,1] via the mediant descent."""
    a, b, c, d = 0, 1, 1, 1          # bracketing 0/1 .. 1/1
    lvl = 0
    while True:
        m = (a + c, b + d)
        lvl += 1
        if (m[0], m[1]) == (p, q):
            return lvl
        if p * m[1] < m[0] * q:      # target < mediant -> go left
            c, d = m
        else:
            a, b = m


def cf_len(p, q):
    """Length of the continued fraction of p/q (a soft 'depth' count)."""
    n = 0
    while q:
        p, q = q, p % q
        n += 1
    return n


print(f"  circle map  theta -> theta + Omega - (K/2pi) sin 2pi theta,  K = {K}")
print(f"  measuring Arnold-tongue widths on an Omega grid of {M} over [0,1]\n")

# winding over the grid (computed once)
grid = [(i / (M - 1)) for i in range(M)]
wind = [winding(Om) for Om in grid]


def tongue_width(target, tol=1.5e-3):
    frac = sum(1 for w in wind if abs(w - target) < tol)
    return frac / M


# all reduced p/q in (0,1) with 2 <= q <= QMAX
data = []
for q in range(2, QMAX + 1):
    for p in range(1, q):
        if math.gcd(p, q) != 1:
            continue
        w = tongue_width(p / q)
        if w <= 0:
            continue
        data.append({
            "frac": Fraction(p, q), "q": q, "curv": 2 * q * q,
            "level": sb_level(p, q), "cf_len": cf_len(p, q),
            "width": w, "nlogw": -math.log(w),
        })


def avg_ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        r = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = r
        i = j + 1
    return ranks


def spearman(xs, ys):
    rx, ry = avg_ranks(xs), avg_ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    vx = sum((rx[i] - mx) ** 2 for i in range(n))
    vy = sum((ry[i] - my) ** 2 for i in range(n))
    if vx == 0 or vy == 0:
        return 0.0
    return cov / math.sqrt(vx * vy)


# ===========================================================================
line()
print(f"D1  WHICH MEASURE ORGANIZES WIDTH?  ({len(data)} tongues, 2<=q<={QMAX})")
line()
nlogw = [d["nlogw"] for d in data]
for key, label in [("q", "denominator q (curvature-depth)"),
                   ("level", "Stern-Brocot tree level (count)"),
                   ("cf_len", "continued-fraction length (count)")]:
    rho = spearman([d[key] for d in data], nlogw)
    print(f"    Spearman( -log width , {label:34s} ) = {rho:+.4f}")
print()
print("    (all positive: deeper = narrower. q is the framework's organizer;")
print("     the question D2 settles is whether it beats the COUNT.)")
print()

# ===========================================================================
line()
print("D2  THE DISCRIMINATOR:  within a fixed tree level, does width track q?")
line()
levels = {}
for d in data:
    levels.setdefault(d["level"], []).append(d)
usable = {L: ds for L, ds in levels.items() if len({d["q"] for d in ds}) >= 2}


def mean_within_level_rho(assign_q):
    """Average within-level Spearman(-log width, q'), q' from assign_q."""
    rhos = []
    for L, ds in usable.items():
        if len(ds) < 3:
            continue
        qs = [assign_q[id(d)] for d in ds]
        rhos.append(spearman(qs, [d["nlogw"] for d in ds]))
    return sum(rhos) / len(rhos) if rhos else 0.0


true_assign = {id(d): d["q"] for d in data}
obs = mean_within_level_rho(true_assign)
print(f"    usable levels (>=3 tongues, >=2 distinct q): "
      f"{sorted(L for L, ds in usable.items() if len(ds) >= 3)}")
print(f"    observed mean within-level Spearman(-log width, q) = {obs:+.4f}\n")

TRIALS = 20000
ge = 0
for _ in range(TRIALS):
    shuffled = {}
    for L, ds in usable.items():
        qs = [d["q"] for d in ds]
        random.shuffle(qs)
        for d, qq in zip(ds, qs):
            shuffled[id(d)] = qq
    if mean_within_level_rho(shuffled) >= obs - 1e-12:
        ge += 1
p_emp = ge / TRIALS
print(f"    NULL: shuffle q within each level, {TRIALS} seeded draws")
print(f"    p(shuffle >= observed) = {ge}/{TRIALS} = {p_emp:.4f}")
print()
line()
print("  VERDICT")
line()
if p_emp <= 0.05 and obs > 0:
    print(f"    Within a fixed tree level, width still rises with q")
    print(f"    (mean rho = {obs:+.3f}, p = {p_emp:.4f}).  The curvature-depth q")
    print("    carries organizing information BEYOND the tree-level count:")
    print("    on the framework's own rank-1 tongues, 'depth' is q, not the")
    print("    soft count -- supporting farey/ford_apollonian's canonical depth.")
else:
    print(f"    Within-level q does NOT beat the count (mean rho = {obs:+.3f},")
    print(f"    p = {p_emp:.4f}).  The width organization is not distinguishable")
    print("    from the tree-level count on this sample -- reported as inconclusive.")
print()
print("    SCOPE: rank-1, framework-internal (own dynamics + within-framework")
print("    null). The rank-2 Li & Liao catalog (lunar-theory #20) has free_group")
print("    words in F2, not PSL(2,Z), so q^2-depth is not canonical there; #20")
print("    stays a regularity until a rank-2 canonical depth is found.")
