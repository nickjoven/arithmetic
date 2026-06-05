"""
sb_boundary.py

The completion of Q as a limiting process on the Stern-Brocot tree.

harmonics:minimum_alphabet.md (Part III, Status: Open) asks to "formalize
the completion as a specific limiting process on the Stern-Brocot tree."
This script shows that the formalization is classical and exact: the
BOUNDARY of the SB tree IS the completion R≥0, the path encoding IS the
continued fraction, and four framework claims land on four standard facts
about it. The framework does not derive this; it adopts a known
construction as the rigorous home for claims it was making informally.

  C1  RESOLUTION FLOOR.  Every tree-adjacent pair a/b, c/d is unimodular
      (|bc − ad| = 1), so the bracket they bound has width exactly
      1/(b·d). This IS the framework's "smallest resolved interval ~ 1/q²"
      (minimum_alphabet.md Part III) — not an analogy, the same quantity.

  C2  COMPLETION = LIMIT OF MEDIANTS.  Descending toward a real x, the
      bracketing intervals shrink to {x} (a Cauchy / nested-interval
      limit). The L/R path's run-lengths are exactly x's continued-fraction
      coefficients, and the bracket endpoints are its convergents. The
      continuum is reached as this limit — "completion of Q," concretely.

  C3  THE TWO TAILS = 0.999... = 1.  A rational has exactly TWO finite paths
      ([..,a_n] and [..,a_n−1,1]); an irrational has ONE infinite path.
      The double representation of rationals is the tree's 0.999...=1, which
      minimum_alphabet.md ties to the alternating psi-mode.

  C4  phi IS THE DEEPEST POINT.  The golden ratio's CF is all-1s, so its
      convergent denominators are the Fibonacci numbers — the MINIMAL
      possible growth. Hence its resolution floor 1/(q_n q_{n+1}) shrinks
      SLOWEST: phi is the worst-approximable real, the slowest point of the
      completion. This is exactly minimum_alphabet.md's 1/phi self-similarity
      and the Planck-floor-reached-slowest claim.

  C5  WHERE THE FACES MEET.  The completion holds both faces of the repo's
      register at once: rationals = finite nodes (locked centres),
      irrationals = infinite paths (unlocked gaps). The standing-wave
      rotation rho = log2(3/2) is one such infinite path; its convergents
      7/12, 24/41, 31/53 are the very nodes that bracket it.

Pure Python, no numpy. Exact integer/Fraction arithmetic for convergents
(floats only to read off a CF for pi and e). Deterministic.
Run: python3 sb_boundary.py
"""

import math
from fractions import Fraction


def cf_from_float(x, n=20):
    """Continued-fraction coefficients of x (float; reliable for ~15-18 terms)."""
    a = []
    for _ in range(n):
        i = math.floor(x)
        a.append(i)
        x -= i
        if x < 1e-12:
            break
        x = 1 / x
    return a


def convergents(a):
    """Exact convergents p_k/q_k from CF coefficients, via integer recurrence."""
    h0, h1, k0, k1 = 0, 1, 1, 0
    out = []
    for ai in a:
        h0, h1 = h1, ai * h1 + h0
        k0, k1 = k1, ai * k1 + k0
        out.append((h1, k1))
    return out


# exact (periodic) CFs where we know them; float-derived CFs otherwise
CF = {
    "phi": [1] * 14,                 # golden ratio = [1;1,1,1,...]
    "sqrt2": [1] + [2] * 13,         # √2 = [1;2,2,2,...]
    "pi": cf_from_float(math.pi, 14),
    "e": cf_from_float(math.e, 14),
}
VAL = {"phi": (1 + 5 ** 0.5) / 2, "sqrt2": 2 ** 0.5, "pi": math.pi, "e": math.e}


# ===========================================================================
print("=" * 72)
print("C1  RESOLUTION FLOOR:  tree-adjacent a/b, c/d are unimodular -> width 1/(bd)")
print("=" * 72)
# Walk the SB tree toward a target via mediants; check unimodularity at each node.
def descend(target, depth):
    lo, hi = (0, 1), (1, 0)   # 0/1 and 1/0; bound all of [0, inf)
    nodes = []
    for _ in range(depth):
        med = (lo[0] + hi[0], lo[1] + hi[1])
        nodes.append((lo, hi, med))
        if target < med[0] / med[1]:
            hi = med
        else:
            lo = med
    return nodes


unimodular = True
for name in CF:
    for (a, b), (c, d), _ in descend(VAL[name], 30):
        if abs(b * c - a * d) != 1:
            unimodular = False
print(f"   |bc − ad| = 1 at every node, all targets: {unimodular}")
print("   => bracket width = |a/b − c/d| = 1/(b·d) exactly. The framework's")
print("      resolution floor 1/q² IS the Stern-Brocot interval width.")


# ===========================================================================
print("\n" + "=" * 72)
print("C2  COMPLETION = LIMIT OF MEDIANTS:  brackets shrink; path runs = CF")
print("=" * 72)
print(f"   {'x':>6} {'CF (first 6)':>22} {'conv p/q (k=5)':>16} "
      f"{'floor 1/(q5 q6)':>16}")
for name, a in CF.items():
    conv = convergents(a)
    p5, q5 = conv[4]
    p6, q6 = conv[5]
    floor = Fraction(1, q5 * q6)
    print(f"   {name:>6} {str(a[:6]):>22} {f'{p5}/{q5}':>16} "
          f"{f'1/{q5*q6}={float(floor):.2e}':>16}")
print("   The bracket endpoints ARE the convergents; the width is 1/(q_k q_{k+1});")
print("   the nested intervals shrink to the real. That limit is the completion.")


# ===========================================================================
print("\n" + "=" * 72)
print("C3  TWO TAILS = 0.999...=1:  rationals have 2 finite paths, irrationals 1")
print("=" * 72)
def other_cf_form(a):
    """The unique other finite CF of the same rational (the two-tails pair)."""
    if len(a) > 1 and a[-1] == 1:
        return a[:-2] + [a[-2] + 1]          # [...,k,1] = [...,k+1]
    return a[:-1] + [a[-1] - 1, 1]           # [...,k>=2] = [...,k-1,1]


for r in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(5, 8)):
    a = cf_from_float(float(r))
    alt = other_cf_form(a)
    same = convergents(a)[-1] == convergents(alt)[-1]
    print(f"   {str(r):>4}:  [{','.join(map(str,a))}]  ==  "
          f"[{','.join(map(str,alt))}]   both -> {r}  : {same}")
print("   Two finite descents reach the same rational node = the tree's 0.999...=1.")
print("   Irrationals (phi, sqrt2, pi, e): CF infinite -> a UNIQUE infinite path.")


# ===========================================================================
print("\n" + "=" * 72)
print("C4  phi IS THE DEEPEST POINT:  Fibonacci denominators = slowest floor")
print("=" * 72)
print("   convergent denominators q_n along each path (slower growth = finer")
print("   resolution reached later = 'deeper' into the completion):")
for name, a in CF.items():
    qs = [q for _, q in convergents(a)[1:9]]
    tag = "  <- Fibonacci: MINIMAL growth" if name == "phi" else ""
    print(f"   {name:>6}: {qs}{tag}")
# quantitative: floor after 8 levels, smaller q => larger (coarser) floor
print("\n   resolution floor 1/(q8 q9) after 8 levels (LARGER = coarser = slower):")
for name, a in CF.items():
    conv = convergents(a)
    q8, q9 = conv[7][1], conv[8][1]
    print(f"   {name:>6}: 1/(q8 q9) = {float(Fraction(1, q8*q9)):.3e}"
          + ("   <- coarsest: phi is worst-approximable" if name == "phi" else ""))
print("   phi keeps the coarsest floor longest: the golden ratio is the slowest")
print("   point of the completion (minimum_alphabet.md: 1/phi self-similarity).")


# ===========================================================================
print("\n" + "=" * 72)
print("C5  WHERE THE FACES MEET:  rho = log2(3/2) as an infinite path")
print("=" * 72)
rho = math.log(3 / 2) / math.log(2)
a = cf_from_float(rho, 10)
conv = convergents(a)
print(f"   rho = log2(3/2) = {rho:.8f}  (irrational -> infinite path)")
print(f"   its convergents (the bracketing NODES): "
      + ", ".join(f"{p}/{q}" for p, q in conv[1:6]))
print("   7/12 = 12-tone equal temperament is one such node (mode_locking study).")
print("   So the completion holds both faces at once:")
print("     rationals  = finite nodes      = mode-lock CENTRES   (locked)")
print("     irrationals = infinite paths   = the GAPS / rho      (unlocked)")
print("   The boundary of the Stern-Brocot tree is exactly their union — the")
print("   completion of Q, where the repo's locked and unlocked faces meet.")
