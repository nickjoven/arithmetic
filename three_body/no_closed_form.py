"""
no_closed_form.py

The three-body problem, read on the framework's LOCKED-vs-UNLOCKED axis as
the UNLOCKED face of *rank*: stepping from one rotation number to many.

The framework's arena (mode_locking/standing_waves.md) is RANK 1 — two
coupled phase oscillators reduce to a SINGLE rotation number on a circle,
and the whole Farey / Stern-Brocot census of its locks closes cleanly
(Denjoy/KAM: a circle map below criticality keeps a positive-measure set of
quasiperiodic orbits). Three bodies are RANK 2 — a rotation VECTOR on a
torus. There the resonances k.w = 0 are dense, their zones OVERLAP, and the
perturbation series for any conserved quantity is poisoned by small divisors
1/(k.w). That is the content of Poincare (1892, no new uniform analytic
integral) and Bruns (1887, no new algebraic one): the n>=3 problem has no
exact algebraic closed form. This is a THEOREM we read in the framework
vocabulary, NOT one the framework proves (Class 2).

What this script computes (every load-bearing number in no_closed_form.md):

  T1  RANK. n coupled phase oscillators -> (n-1) independent frequency
      ratios. n=2 -> rank 1 (one rotation number; the standing_waves arena).
      n=3 -> rank 2; n=4 -> rank 3. Rank 1 is the ONLY rank where a single
      rotation number is a complete invariant.

  T2  SMALL DIVISORS. Rank 1 has a Diophantine FLOOR: for a badly-
      approximable rotation number the divisor q*||q.rho|| stays bounded
      below, so the KAM series converges and tori survive. Rank 2 has no
      such global floor: neighbouring resonance zones OVERLAP at finite
      coupling (Chirikov), destroying the tori between them. Crude two-
      resonance overlap K = 1/16; exact last-torus value K_c = 0.9716354
      (Greene 1979).

  T3  THE GOLDEN BOUNDARY. Which rotation number survives longest? The
      WORST-approximable one: liminf q*||q.x|| is maximal for the golden
      mean (= 1/sqrt5, Hurwitz). The golden mean is the deepest point of the
      Stern-Brocot boundary (root/golden_root.md); it is also the LAST KAM
      torus to break. Worst-approximable = deepest SB point = locked/unlocked
      boundary -- the rank analogue of Collatz's q < q2^2 boundary.

Pure Python, no numpy. Deterministic. Run: python3 no_closed_form.py
"""

import math
from decimal import Decimal, getcontext

getcontext().prec = 60           # enough that q*X - p is exact for q up to ~1e8

q2, q3 = 2, 3
SQRT5 = math.sqrt(5)
PHI = (SQRT5 + 1) / 2            # phi = 1 + 1/phi, the deepest Stern-Brocot node


def dsqrt(n):
    return Decimal(n).sqrt()


def liminf_q_norm(X, n_terms=40, tail=8):
    """Asymptotic liminf of q*||q*X|| for a quadratic irrational X.

    Uses EXACT integer convergents p_n/q_n against a high-precision Decimal
    X, so q_n*X - p_n stays accurate where float q*(q*x - p) collapses to
    noise (q ~ 1e12 vs float ulp ~ 1e-4). q_n*||q_n*X|| attains the liminf
    along convergents; we take the min over the last `tail` of them
    (asymptotic / one full CF period), skipping the transient."""
    a, y = [], X                                  # continued-fraction expansion
    for _ in range(n_terms):
        ai = int(y)                               # floor (X > 0)
        a.append(ai)
        frac = y - ai
        if frac == 0:
            break
        y = 1 / frac
    h_prev, h = 1, a[0]                            # convergent recurrence
    k_prev, k = 0, 1
    ds = []
    for ai in a[1:]:
        h, h_prev = ai * h + h_prev, h
        k, k_prev = ai * k + k_prev, k
        ds.append(float(k * abs(k * X - h)))
    return min(ds[-tail:]), ds


def line(c="="):
    print(c * 72)


# ===========================================================================
line()
print("T1  RANK:  n coupled phase oscillators  ->  (n-1) frequency ratios")
line()
print("   A frequency vector w in R^n; resonances are k.w = 0, k in Z^n\\{0}.")
print("   Overall time-scaling is a gauge, so the invariant content is the")
print("   RAY direction -> (n-1) independent ratios = the 'rank' of the torus.\n")
print("     n bodies   rank = n-1   rotation object")
for n in (2, 3, 4):
    rank = n - 1
    obj = {1: "one number on S^1  (the standing_waves arena)",
           2: "a vector on T^2    (three-body)",
           3: "a vector on T^3"}[rank]
    print(f"        {n}           {rank}        {obj}")
print()
print("   Rank 1 is the ONLY rank where a single rotation number is a")
print("   COMPLETE invariant (Denjoy). Three bodies (rank 2) are the first")
print(f"   step out of the framework's rank-1 arena (the bare q3/q2 = {q3}/{q2}).")
print()


# ===========================================================================
line()
print("T2  SMALL DIVISORS:  a rank-1 floor vs rank-2 overlap")
line()


# Rank 1: the Diophantine floor for the golden rotation number.
g_floor, _ = liminf_q_norm((dsqrt(5) - 1) / 2)
print("   RANK 1 -- divisor floor  q*||q*rho||  for rho = golden (most robust):")
print(f"     liminf q*||q*rho||  = {g_floor:.7f}   (analytic 1/sqrt5 = {1/SQRT5:.7f})")
print("     -> bounded below by a constant: small divisors never collapse,")
print("        so the KAM series converges and the invariant circle SURVIVES.")
print()

# Rank 2: resonance overlap destroys the floor at finite coupling.
K_overlap = math.pi ** 2 / 4         # simple two-resonance overlap estimate
K_c = 0.9716354                      # Greene 1979 last (golden) KAM torus
print("   RANK 2 -- resonances overlap (standard map: spacing 2*pi, half-width 2*sqrtK):")
print(f"     simple overlap  4*sqrtK = 2*pi  ->  K = pi^2/4 = {K_overlap:.4f}")
print(f"     exact last torus (Greene 1979)         K_c    = {K_c:.7f}")
print(f"     (the crude criterion OVERestimates by {K_overlap / K_c:.2f}x; both are O(1))")
print("     -> above K_c NO invariant circle blocks transport: the rank-2")
print("        census does NOT close. No exact algebraic integral survives")
print("        (Poincare 1892 / Bruns 1887) -- the three-body problem is")
print("        non-integrable. (Theorem READ here, not proved.)")
print()


# ===========================================================================
line()
print("T3  THE GOLDEN BOUNDARY:  worst-approximable = deepest SB point = last torus")
line()
print("   liminf q*||q*x|| for quadratic irrationals")
print("   (larger = MORE avoided by rationals = MORE robust torus):\n")
cases = [
    ("golden  g=(sqrt5-1)/2", (dsqrt(5) - 1) / 2),   # [0;1,1,1,...]
    ("sqrt2 - 1",             dsqrt(2) - 1),          # [0;2,2,2,...]
    ("sqrt3 - 1",             dsqrt(3) - 1),          # [0;1,2,1,2,...]
    ("sqrt5 - 2",             dsqrt(5) - 2),          # [0;4,4,4,...]
]
results = []
for name, x in cases:
    val, _ = liminf_q_norm(x)
    results.append((name, val))
    print(f"     {name:24s}  liminf q*||q*x|| = {val:.7f}")
winner = max(results, key=lambda t: t[1])
print()
print(f"   MAX is {winner[0].split()[0]}  =  {winner[1]:.7f}  =  1/sqrt5 = {1/SQRT5:.7f}")
print("   (Hurwitz: 1/sqrt5 is the largest possible -- golden is THE worst-")
print("    approximable number.)\n")
print("   Tie to the tree (root/golden_root.md): the golden mean is the")
print(f"   DEEPEST point of the Stern-Brocot boundary (phi = {PHI:.7f}, the")
print("   continued fraction [1;1,1,...], every step the smallest mediant).")
print("   Worst-approximable  =  deepest SB point  =  the last standing wave")
print("   to survive as non-integrability turns on  =  the LOCKED/UNLOCKED")
print("   boundary. It is the rank analogue of Collatz's q < q2^2 boundary:")
print("   the framework owns the boundary; the unlocked interior stays open")
print("   (here: closed by theorem -- non-integrable -- not by conjecture).")
print()
line()
print("SUMMARY")
line()
print(f"   rank(n=3) = 2 ; KAM floor(golden) = {g_floor:.7f} = 1/sqrt5 ;")
print(f"   overlap K = {float(K_overlap):.4f} ; last torus K_c = {K_c:.7f} .")
print("   Rank 1 census closes (standing_waves); rank >= 2 does not -> no")
print("   exact algebraic closed form for three or more phase oscillators.")
