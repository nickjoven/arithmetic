"""
golden_root.py

The most singular representation: the whole repo from one root.

Everything in these studies is ONE tree — the Stern-Brocot tree — grown from
ONE seed (0/1, 1/0) by ONE operation (the mediant). The four studies are
four readings of that single tree:

    COUNT the nodes      -> |F_n|, the framework's 13/19     (farey/)
    WIDTH of the nodes   -> Arnold tongues, standing waves   (mode_locking/)
    a MAP on the nodes   -> Collatz, the unlocked dynamics   (collatz/)
    the BOUNDARY of it    -> the completion of Q             (completion/)

This script shows the singularity is tighter still: a SINGLE object — the
golden matrix M = [[1,1],[1,0]] — carries all four of the framework's
irreducible primitives at once, and its eigenvalue phi is the deepest point
of the very tree it generates. Generation and completion are one object.

IMPORTANT (honesty): this does NOT reduce the four primitives to one. Their
irreducibility (each is necessary; minimum_alphabet.md Part II) is untouched.
What is shown is a single COMMON LOCUS where all four are inseparably present
— a singular representation, not a smaller alphabet. Class 2 synthesis; no
new constant.

Pure Python, no numpy, exact integer arithmetic. Deterministic.
Run: python3 golden_root.py
"""

M = [[1, 1], [1, 0]]


def matmul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


def power(A, n):
    P = [[1, 0], [0, 1]]
    for _ in range(n):
        P = matmul(P, A)
    return P


phi = (1 + 5 ** 0.5) / 2
psi = (1 - 5 ** 0.5) / 2

# ===========================================================================
print("=" * 72)
print("ONE TREE, ONE SEED, ONE OPERATION — read four ways")
print("=" * 72)
seed_lo, seed_hi = (0, 1), (1, 0)          # the ONE seed
print(f"   seed: {seed_lo[0]}/{seed_lo[1]} and {seed_hi[0]}/{seed_hi[1]} (i.e. 0 and ∞)")
print(f"   operation: mediant (a,b)⊕(c,d) = (a+c, b+d)   [one operation]")
root = (seed_lo[0] + seed_hi[0], seed_lo[1] + seed_hi[1])
print(f"   root node: {root[0]}/{root[1]}  — and the whole tree grows from here.")
print("   the four studies are four readings of this one tree:")
print("     COUNT nodes  → |F_n| (13/19)            farey/equidistribution")
print("     WIDTH nodes  → Arnold tongues           mode_locking/standing_waves")
print("     MAP on nodes → Collatz                  collatz/minimal_chaos")
print("     BOUNDARY     → completion of Q          completion/sb_boundary")

# ===========================================================================
print("\n" + "=" * 72)
print("ONE OBJECT — the golden matrix M = [[1,1],[1,0]] — carries all 4 primitives")
print("=" * 72)

print("\n  [1] INTEGERS (counting):  M^n entries are Fibonacci numbers")
for n in range(1, 7):
    P = power(M, n)
    print(f"      M^{n} = {P}")

print("\n  [2] PARABOLA (bifurcation/orientation):  char. poly of M is x²−x−1")
tr = M[0][0] + M[1][1]
det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
print(f"      trace={tr}, det={det}  ->  x² − {tr}x + ({det}) = x² − x − 1")
print(f"      roots φ={phi:.6f}, ψ={psi:.6f}  (two roots = the orientation primitive)")

print("\n  [3] FIXED-POINT (self-reference/iteration):  M^n v → the φ-direction")
v = [1, 0]
for _ in range(12):
    v = [M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1]]
print(f"      ratio of M^12·v components = {v[0]/v[1]:.8f}   (φ = {phi:.8f})")
print(f"      φ is the fixed point of x = 1 + 1/x :  1 + 1/φ = {1 + 1/phi:.8f} = φ")

print("\n  [4] MEDIANT (rational structure):  M's iteration IS the φ-path of the tree")
lo, hi = (0, 1), (1, 0)
conv = []
for _ in range(9):
    med = (lo[0] + hi[0], lo[1] + hi[1])
    conv.append(f"{med[0]}/{med[1]}")
    if phi < med[0] / med[1]:
        hi = med
    else:
        lo = med
print(f"      SB convergents to φ: {', '.join(conv)}")
print(f"      = Fibonacci ratios = the columns of M^n. Generator and tree-path coincide.")

print("\n  [5] det M = −1  →  CASSINI = the ψ-mode (Born exponent 2 / uncertainty)")
for n in range(1, 6):
    P = power(M, n)
    cassini = P[0][0]*P[1][1] - P[0][1]*P[0][1]   # F_{n+1}F_{n-1} − F_n²
    print(f"      n={n}: det(M^n) = (−1)^{n} = {(-1)**n:+d} = F_(n+1)F_(n−1) − F_n² = {cassini:+d}")
print(f"      |φ·ψ| = |det M| = {abs(phi*psi):.4f} = 1  (uncertainty product; |ψ|² exponent 2 = the parabola)")

# ===========================================================================
print("\n" + "=" * 72)
print("THE SINGULARITY — the generator's eigenvalue IS its boundary's deepest point")
print("=" * 72)
print("   M GENERATES the tree (its iteration = the golden path, [4]).")
print("   M's eigenvalue φ is the WORST-APPROXIMABLE real = the point the tree")
print("   resolves last (completion/sb_boundary.md C4: Fibonacci denominators,")
print("   the slowest-shrinking resolution floor).")
print("   So the one root is self-referential: x = f(x), with f = the mediant step")
print("   and x = φ both the generator's fixed direction AND the deepest point of")
print("   the boundary it generates. Generation and completion are one object —")
print("   that is how singularly the framework represents, from one root.")
