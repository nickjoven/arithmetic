"""
adic_asymmetry.py

Which N-adic is interesting, and do two primes straddle a symmetry?

The Collatz map mixes /2 (prime q2 = 2) and *3 (prime q3 = 3), so one might
expect 2 and 3 to be a symmetric pair across the two completions. They are
NOT. This script shows why, and where the genuine symmetries actually sit.

  A  THE +1 IS A SYMMETRY-BREAKER. For every odd n, 3n+1 is simultaneously
     EVEN (v2 >= 1) and COPRIME TO 3 (v3 = 0). So the same +1 that creates
     2-adic structure (an even number to halve) destroys 3-adic structure
     (the *3 builds no 3-adic depth). The map tilts entirely toward p = 2:
     v2 drives the dynamics (Lagarias conjugacy in Z_2, two_completions.md);
     v3 collapses to 0 after the first odd step. Strip the +1 and the *3 DOES
     build 3-adic depth -- the symmetry is broken by hand.

  B  THE REAL STRADDLE IS 3 and 5, about the multiplier line q2^2 = 4 -- a
     symmetry in the MULTIPLIER, not the completion. 3n+1 (=4-1) contracts,
     5n+1 (=4+1) expands; the neutral line q=4 is even, an invalid odd
     multiplier, so it is unoccupied.

  C  A SEPARATE FIELD SYMMETRY (phi's field Q(sqrt5)): 2 = -3 (mod 5), both
     INERT; the framework's Farey counts 11=|F5|, 19=|F7| SPLIT. The two
     forced primes and the two Farey denominators fall in opposite classes of
     the mod-5 symmetry.

Class 2: identifies which completion is singular and why; no new constant.
Pure Python, no numpy. Deterministic. Run: python3 adic_asymmetry.py
"""


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def vp(n, p):
    k = 0
    while n and n % p == 0:
        n //= p
        k += 1
    return k


# ===========================================================================
print("=" * 70)
print("A  THE +1 IS A SYMMETRY-BREAKER: 3n+1 is EVEN and COPRIME TO 3 at once")
print("=" * 70)
print("   for odd n: v2(3n+1) >= 1 (even, halve-able) AND v3(3n+1) = 0 (coprime to 3):")
allgood = True
for n in range(1, 22, 2):
    a, b = vp(3 * n + 1, 2), vp(3 * n + 1, 3)
    allgood = allgood and a >= 1 and b == 0
print(f"   verified for all odd n < 22: even & coprime-to-3 = {allgood}")
print()
print("   along the orbit of 27: v2 is rich, v3 dies:")
x = 27
v2s, v3s = [], []
for _ in range(20):
    v2s.append(vp(x, 2))
    v3s.append(vp(x, 3))
    x = T(x)
print(f"     v2: {v2s}")
print(f"     v3: {v3s}   (0 after the first odd step)")
print()
print("   contrast: WITHOUT the +1 (pure odd->3n), the *3 DOES build 3-adic depth:")
def pure(n):  # n/2 if even else 3n  (no +1)
    return n // 2 if n % 2 == 0 else 3 * n
x = 5
seq = []
for _ in range(6):
    seq.append((x, vp(x, 3)))
    x = pure(x)
print(f"     (n, v3) under n->3n/ ÷2: {seq}  -> v3 accumulates")
print("   => the +1 simultaneously enriches p=2 and trivializes p=3. One operation,")
print("      both effects, both favoring the prime 2. The 2-adic is singular.")


# ===========================================================================
print("\n" + "=" * 70)
print("B  THE REAL STRADDLE: 3 and 5 about the multiplier line q2^2 = 4")
print("=" * 70)
for q in (3, 4, 5):
    rate = q / 4
    tag = "CONTRACT" if q < 4 else ("NEUTRAL (the symmetry line)" if q == 4 else "EXPAND")
    print(f"   {q}n+1: per-odd-cycle multiplier ~ {q}/4 = {rate:.2f}  ->  {tag}")
print("   3 = 4-1 and 5 = 4+1 mirror about q = q2^2 = 4; the line (even) is an")
print("   invalid odd multiplier -> unoccupied. The straddle is in the MULTIPLIER,")
print("   not the completion (cf. collatz/minimal_chaos.md M1).")


# ===========================================================================
print("\n" + "=" * 70)
print("C  A FIELD SYMMETRY: 2 = -3 (mod 5), both inert in phi's field Q(sqrt5)")
print("=" * 70)
def status_in_Qsqrt5(p):
    # p splits iff p = +/-1 mod 5; inert iff +/-2 mod 5; ramified iff p = 5
    r = p % 5
    return "ramified" if r == 0 else ("split" if r in (1, 4) else "inert")
for p in (2, 3, 5, 11, 13, 19, 29):
    print(f"   p={p:>2}: {p} mod 5 = {p % 5}  ->  {status_in_Qsqrt5(p)}")
print("   2 = 2 and 3 = -2 (mod 5): negatives of each other -> symmetric about 5; both INERT.")
print("   the Farey counts 11=|F5|, 19=|F7| SPLIT -> {2,3} and {11,19} sit in")
print("   opposite classes of the same mod-5 (golden-field) symmetry.")


# ===========================================================================
print("\n" + "=" * 70)
print("VERDICT")
print("=" * 70)
print("   ONE N-adic is singularly interesting -- the 2-adic -- BECAUSE the +1")
print("   breaks the 2<->3 symmetry (enriching 2, trivializing 3). The genuine")
print("   straddles are shifted off the completions: 3<->5 about the multiplier")
print("   q2^2=4, and 2<->3 about 0 mod 5 in phi's field. The +1 -- which is also")
print("   the mediant with the tree root (minimal_chaos M3) -- is the breaker.")
