"""
two_completions.py

The lossy mod-2 operator of Collatz, to depth: it is the doorway to the
SECOND completion of Z.

`sb_boundary.py` built one completion of Q — the Archimedean one, R, as the
Stern-Brocot tree boundary (continued fractions, the real line). Collatz's
defining operator is a lossy modulo:

    T(x) = x/2        if x ≡ 0 (mod 2)
    T(x) = (3x+1)/2   if x ≡ 1 (mod 2)

Each step reads ONE bit (x mod 2) and discards it. That mod-2 read is a
projection Z -> Z/2 — lossy. But the loss is the doorway to the OTHER
completion of Z, the non-Archimedean 2-adic one Z_2, where the loss
vanishes. This script develops that to depth.

  L1  LOSSY PER STEP, LOSSLESS IN AGGREGATE.  The parity stream is a
      bijection on Z/2^k (Terras) and reconstructs x mod 2^k exactly. One
      bit lost per step; the stream is a 2-adic coordinate.

  L2  THE LOSS HAS A DIRECTION.  In bit-length: even read Δlog2 = −1, odd
      read Δlog2 = log2(3/2). Net drift negative — the 3/4 contraction in
      information units: the lossy ÷2 reads out-strip the ×3 gains.

  L3  THE TWO COMPLETIONS.  Z has two completions (Ostrowski): the
      Archimedean R (sb_boundary.py) and the 2-adic Z_2. On Z_2 the
      parity-vector map is a measure-preserving homeomorphism (Lagarias):
      the lossy mod-2, completed 2-adically, is a LOSSLESS isometry. The
      conjecture is the gap between the clean Z_2 / outside view and the
      integer / inside view — the repo's inside-vs-outside seam, as
      Archimedean-vs-2-adic completion.

Class 2: identifies Collatz's natural completion and ties it to the repo's
R-completion and inside/outside spine. The 2-adic conjugacy is classical
(Terras 1976, Lagarias 1985); the reading is the Class 2 content. Does NOT
solve Collatz; adds no constant.

Pure Python, no numpy. Deterministic (seeded). Run: python3 two_completions.py
"""

import math
import random

log2 = lambda x: math.log(x) / math.log(2)


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


# ===========================================================================
print("=" * 72)
print("L1  LOSSY PER STEP, LOSSLESS IN AGGREGATE  (the mod-2 stream is 2-adic)")
print("=" * 72)


def parity_vector(x, k):
    """First k parity reads of x, packed as a 2-adic integer Σ a_i 2^i."""
    v = 0
    for i in range(k):
        if x & 1:
            v |= (1 << i)
        x = T(x)
    return v


print("   x -> (first k parities) is a bijection Z/2^k -> Z/2^k (Terras):")
for k in (1, 4, 8, 12):
    img = {parity_vector(x, k) for x in range(2 ** k)}
    print(f"     k={k:>2}: {len(img):>5}/{2**k:>5} distinct   bijection={len(img) == 2**k}")

k = 12
fwd = {x: parity_vector(x, k) for x in range(2 ** k)}
inv = {v: x for x, v in fwd.items()}
recoverable = all(inv[fwd[x]] == x for x in range(2 ** k))
print(f"   inverse exists: the k lossy reads recover x mod 2^{k} exactly: {recoverable}")
print("   => one mod-2 bit is destroyed per step, but the STREAM loses nothing:")
print("      it is the 2-adic coordinate of x. Loss is a per-step artifact.")


# ===========================================================================
print("\n" + "=" * 72)
print("L2  THE LOSS HAS A DIRECTION  (the 3/4 contraction in information units)")
print("=" * 72)
print(f"   even read:  Δlog2(x) = −1              (strip a 0-bit; ÷q₂)")
print(f"   odd  read:  Δlog2(x) = log2(3/2) = {log2(3/2):.4f}   (×q₃/q₂)")
random.seed(3)
samples = random.sample(range(10 ** 6, 10 ** 7), 300)
drifts = []
for n in samples:
    x, s = n, 0
    while x != 1 and s < 100000:
        x = T(x)
        s += 1
    drifts.append(log2(n) / s)            # mean |Δlog2| per step over the descent
emp = sum(drifts) / len(drifts)
pred = (1 - log2(3 / 2)) / 2              # at parity 1/2
print(f"   predicted mean −Δlog2/step at parity 1/2 = {pred:.4f}")
print(f"   empirical  mean  Δlog2/step to reach 1    = {emp:.4f}   (same sign & scale;")
print("     exact only at parity 1/2 — the heuristic of the 3/4 contraction, in bits)")
print("   the lossy ÷2 reads out-strip the ×3 gains: bit-length drifts DOWN.")


# ===========================================================================
print("\n" + "=" * 72)
print("L3  THE TWO COMPLETIONS OF Z  (Ostrowski) — the loss vanishes in Z_2")
print("=" * 72)
print("   By Ostrowski's theorem the only completions of Q are:")
print("     • R   — Archimedean      (sb_boundary.py: the Stern-Brocot tree boundary)")
print("     • Q_p — p-adic, one per prime p   (here p = q₂ = 2: the 2-adics Z_2)")
print()
print("   Collatz's lossy mod-2 is the q₂ = 2 reduction; its natural home is Z_2.")
print("   The parity-vector map Q_∞ : Z_2 -> Z_2 (Lagarias 1985) is a MEASURE-")
print("   PRESERVING homeomorphism — the bijection on every Z/2^k above is its")
print("   finite witness. So the lossy mod-2, completed 2-adically, is a LOSSLESS")
print("   ISOMETRY: on Z_2 there is no loss and no hard problem (the map is")
print("   conjugate to a shift; a.e. statements are clean — Tao 2019).")
print()
print("   side-by-side, the same integer orbit under the two completions:")
print(f"   {'n':>6} {'steps to 1 (in R)':>18} {'2-adic val v2(n)':>18}")
for n in (27, 97, 871, 6171):
    x, s = n, 0
    while x != 1 and s < 100000:
        x = T(x)
        s += 1
    v2 = (n & -n).bit_length() - 1
    print(f"   {n:>6} {s:>18} {v2:>18}")
print("   R sees a length (a real-valued descent); Z_2 sees a valuation (a digit).")
print()
print("   THE SEAM: the conjecture is the gap between the two completions —")
print("     Z_2 / outside : almost every orbit behaves (measure-preserving, a.e.)")
print("     Z   / inside  : does EVERY specific integer? (the open problem)")
print("   the same inside-vs-outside, every-vs-almost-every seam as the rest of")
print("   the repo, now as Archimedean (R) vs non-Archimedean (Z_2) completion.")
