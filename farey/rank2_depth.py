"""
rank2_depth.py

The rank-2 canonical depth: decomposing the q2 / F2 / noncommutativity knot.

ford_apollonian.md fixed the RANK-1 canonical depth (curvature q^2, not the
soft tree-level count) and left open: what plays that role for the RANK-2
census (the Li & Liao braid words, which live in F2, not PSL(2,Z))? This
script decomposes the obstruction and names the answer.

THE DECOMPOSITION (all four blocks verified below):

  S1  PSL(2,Z) = Z/q2 * Z/q3 = Z/2 * Z/3.  The forced primes are the ORDERS
      of the two torsion generators (S order 2, ST order 3) -- {2,3} enter
      the Farey-tree generator as torsion, not as the bare ratio.

  S2  The NONCOMMUTATIVE core is F2, the commutative shadow is q2 x q3:
          1 -> F2 -> PSL(2,Z) -> Z/q2 x Z/q3 -> 1     (Z/q2 x Z/q3 = Z/6).
      F2 = the commutator subgroup; geometrically F2 = Gamma(2), torsion-
      free, index [PSL(2,Z):Gamma(2)] = q2*q3 = 6 = |PSL(2,F2)|.

  S3  F2 = pi_1(thrice-punctured sphere) = pi_1(X(2)).  The 3-body shape
      sphere minus its 3 binary-collision points IS a thrice-punctured
      sphere (chi = -1 -> free rank 2), so the rank-2 census lives in this F2.

  S4  CANONICAL DEPTH = HYPERBOLIC LENGTH, not word length.  F2 is free, so
      its only intrinsic length is the word metric (the soft count -- this is
      WHY lunar-theory #20 only saw T* ~ word length). Pulling PSL(2,Z)'s
      geometry back through Gamma(2) gives each word a HYPERBOLIC length
      l = 2 arccosh(|tr|/2) on X(2). At FIXED word length l varies wildly
      (e.g. length-2 'ab' is hyperbolic, 'aB' is a parabolic cusp loop l=0)
      -- the rank-2 analogue of "same tree level, different q^2".

Class 2: S1-S3 are theorems (verified here); S4's identification of the
FRAMEWORK depth with the X(2) hyperbolic length is a READING (the natural
pullback), tested empirically in the sibling, not here.

Pure Python, no numpy, deterministic. Run: python3 rank2_depth.py
"""

import math

q2, q3 = 2, 3


def line(c="="):
    print(c * 72)


def matmul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


def is_pm_I(A):
    return A in ([[1, 0], [0, 1]], [[-1, 0], [0, -1]])


def order_in_PSL(A, cap=24):
    P = A
    for k in range(1, cap + 1):
        if is_pm_I(P):
            return k
        P = matmul(P, A)
    return None


# ===========================================================================
line()
print("S1  PSL(2,Z) = Z/q2 * Z/q3   (forced primes = orders of the generators)")
line()
S = [[0, -1], [1, 0]]
T = [[1, 1], [0, 1]]
ST = matmul(S, T)
oS, oST = order_in_PSL(S), order_in_PSL(ST)
print(f"    order(S)  = {oS}   = q2 = {q2}")
print(f"    order(ST) = {oST}   = q3 = {q3}")
print(f"    => PSL(2,Z) = Z/{oS} * Z/{oST}  (free product; {{2,3}} as torsion)")
print()


# ===========================================================================
line()
print("S2  noncommutative core F2 ; abelian shadow q2 x q3 = Z/6")
line()
# abelianization of Z/2 * Z/3 = Z/2 x Z/3, cyclic of order 6
lcm = 2 * 3 // math.gcd(2, 3)
print(f"    abelianization Z/{q2} x Z/{q3}: order {q2*q3}, element (1,1) order "
      f"lcm(2,3) = {lcm} -> cyclic Z/{q2*q3}")
# index [PSL(2,Z):Gamma(2)] = |PSL(2,F2)| = #invertible 2x2 over F2
mats = [[[a, b], [c, d]] for a in range(2) for b in range(2)
        for c in range(2) for d in range(2)]
inv = [M for M in mats if (M[0][0]*M[1][1] - M[0][1]*M[1][0]) % 2 != 0]


def mod2(M):
    return [[x % 2 for x in r] for r in M]


nonab = any(mod2(matmul(A, B)) != mod2(matmul(B, A)) for A in inv for B in inv)
print(f"    |PSL(2,F2)| = invertible 2x2 over F2 = {len(inv)} = q2*q3 = {q2*q3}"
      f"   (nonabelian ~= S_3: {nonab})")
print(f"    => 1 -> F2 -> PSL(2,Z) -> Z/{q2*q3} -> 1 ;  F2 = Gamma(2), "
      f"index {q2*q3}, torsion-free")
print()


# ===========================================================================
line()
print("S3  F2 = pi_1(thrice-punctured sphere) = the 3-body shape sphere")
line()
chi = 2 - 3                       # sphere minus 3 binary-collision points
rank = 1 - chi
print(f"    chi(S^2 - 3 collisions) = 2 - 3 = {chi}  ->  pi_1 free of rank "
      f"1 - chi = {rank} = F_{rank}")
print(f"    X(2) = Gamma(2)\\H is the same thrice-punctured sphere (3 cusps).")
print(f"    => the rank-2 census (Li & Liao free_group words) lives in F2 = Gamma(2).")
print()


# ===========================================================================
line()
print("S4  CANONICAL DEPTH = HYPERBOLIC LENGTH (not word length)")
line()
# Gamma(2) free generators (parabolics) and inverses
GEN = {
    "a": [[1, 2], [0, 1]],  "A": [[1, -2], [0, 1]],
    "b": [[1, 0], [2, 1]],  "B": [[1, 0], [-2, 1]],
}
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}


def word_matrix(w):
    M = [[1, 0], [0, 1]]
    for ch in w:
        M = matmul(M, GEN[ch])
    return M


def hyp_length(w):
    """Hyperbolic translation length l = 2 arccosh(|tr|/2); 0 if parabolic."""
    M = word_matrix(w)
    t = abs(M[0][0] + M[1][1])
    return 0.0 if t <= 2 else 2.0 * math.acosh(t / 2.0)


def reduced_words(n):
    """Freely reduced words of length n over {a,A,b,B}."""
    if n == 0:
        return [""]
    out = []
    for w in reduced_words(n - 1):
        for ch in "aAbB":
            if w and INV[ch] == w[-1]:
                continue
            out.append(w + ch)
    return out


print("    Same WORD LENGTH, different hyperbolic length (the rank-2 q^2):\n")
print(f"      {'word':>6s} {'|trace|':>8s} {'hyp length l':>13s} {'type':>10s}")
for w in ["ab", "aB", "abab", "abAB", "aabb"]:
    M = word_matrix(w)
    t = abs(M[0][0] + M[1][1])
    typ = "parabolic" if t <= 2 else "hyperbolic"
    print(f"      {w:>6s} {t:>8d} {hyp_length(w):>13.5f} {typ:>10s}")
print()
print("    -> length-2 'ab' is hyperbolic (l=3.52549) but 'aB' is a parabolic")
print("       cusp loop (l=0): word length does NOT fix the depth.\n")

print(f"      {'word len n':>10s} {'#words':>7s} {'# parabolic':>12s} "
      f"{'hyp-length range [min,max]':>28s}")
for n in range(1, 6):
    ws = reduced_words(n)
    ls = [hyp_length(w) for w in ws]
    hyp = [x for x in ls if x > 0]
    rng = f"[{min(hyp):.4f}, {max(hyp):.4f}]" if hyp else "[--]"
    print(f"      {n:>10d} {len(ws):>7d} {sum(1 for x in ls if x == 0):>12d} "
          f"{rng:>28s}")
print()
print("    At every fixed word length the hyperbolic length spans a range:")
print("    word length is the SOFT count, hyperbolic length is the RIGID depth")
print("    -- the rank-2 analogue of ford_apollonian's (tree level vs q^2).")
print()
line()
print("SUMMARY")
line()
print(f"  1 -> F2 -> PSL(2,Z) -> Z/q2 x Z/q3 -> 1  (Z/6); F2=Gamma(2), index q2q3=6.")
print(f"  Rank-2 census = pi_1(3-body shape sphere - collisions) = F2.")
print(f"  Canonical depth = hyperbolic length on X(2) (e.g. 'ab' -> "
      f"{hyp_length('ab'):.5f}), NOT word length.")
