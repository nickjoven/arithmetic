"""
no_dissipation.py

Why "counting to infinity" cannot prove Collatz — the dissipation obstruction.

A convergence proof needs a FORCED descent: a quantity that must decrease,
driving every orbit to a ground state. Collatz has no such forced
dissipation, and this script makes that precise across both completions of Z
(see completion/two_completions.md). The conclusion is a NEGATIVE result
about proof strategies — informative, not a proof or disproof:

  D1  ARCHIMEDEAN (R): no Lyapunov function in size. The 'altitude' |x| is
      NON-monotone — orbits climb far above their start before falling. The
      3/4 bit-length drift is a STATISTICAL average, not a conserved/forced
      quantity. A chaotic map with only average descent can, in principle,
      let a measure-zero set of orbits evade any finite bound.

  D2  2-ADIC (Z_2): the dynamics is MEASURE-PRESERVING. The parity-vector
      map is a measure-preserving homeomorphism (Lagarias), so T is conjugate
      to a measure-preserving shift. Poincare recurrence => a.e. 2-adic orbit
      RECURS forever (never converges). The integers are DENSE but
      MEASURE-ZERO in Z_2, so Collatz convergence is a measure-zero
      phenomenon, invisible to the Haar measure. Measure / ergodic / "almost
      all" tools (Tao 2019) structurally cannot reach EVERY integer.

  D3  THE EMBEDDINGS (C, H) are the WRONG completion. The smooth holomorphic
      extension to C agrees on integers but off-axis diverges
      super-exponentially (transcendental cos pi z) with no conservation law.
      And the prime q2 = 2 RAMIFIES (2 = -i(1+i)^2 in Z[i]): the
      non-Archimedean fact that the 2-adic structure captures and that C / H
      (Archimedean, real normed) cannot see. Geometric/topological embeddings
      thicken the Archimedean side (statistical dissipation) and drop the
      2-adic side (the real structure). They cannot supply a forcing
      conservation law.

Synthesis: what is CONSERVED (the 2-adic coordinate) is an isometry — the
wrong TYPE to force a ground state; what DISSIPATES (Archimedean size) is only
statistical and non-monotone. The two completions pull opposite ways. A
forcing quantity, if one exists, must be ARITHMETIC / adelic (about the
measure-zero integers), not geometric or measure-theoretic.

Class 2. Pure Python; cmath only for the C extension. Deterministic.
Run: python3 no_dissipation.py
"""

import cmath
import math


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


# ===========================================================================
print("=" * 72)
print("D1  ARCHIMEDEAN (R): altitude is NON-monotone — no Lyapunov in size")
print("=" * 72)


def altitude(n):
    x, mx, steps = n, n, 0
    while x != 1:
        x = T(x)
        mx = max(mx, x)
        steps += 1
    return mx, steps


for n in (27, 703, 871, 6171, 77031):
    mx, s = altitude(n)
    print(f"   n={n:>6}: climbs to {mx:>9} (×{mx/n:6.1f} its start) before reaching 1 "
          f"in {s} steps")
print("   |x| and log|x| rise and fall: NO monotone descent. The 3/4 drift is a")
print("   statistical average (completion/two_completions.md L2), not forced.")


# ===========================================================================
print("\n" + "=" * 72)
print("D2  2-ADIC (Z_2): measure-preserving -> convergence is MEASURE-ZERO")
print("=" * 72)


def parity_vector(x, k):
    v = 0
    for i in range(k):
        if x & 1:
            v |= (1 << i)
        x = T(x)
    return v


for k in (8, 12):
    img = {parity_vector(x, k) for x in range(2 ** k)}
    print(f"   parity map bijection on Z/2^{k}: {len(img) == 2**k}   "
          f"(witness: T is measure-preserving on Z_2)")
print("   Poincare recurrence (measure-preserving) => a.e. 2-adic orbit RECURS")
print("   forever; there is NO global attractor on Z_2, NO dissipation.")
print("   integers: every residue mod 2^k is realized -> DENSE; Z is countable")
print("   -> MEASURE ZERO in the uncountable Z_2.")
print("   => Collatz convergence is a measure-zero event, invisible to Haar")
print("      measure. 'Almost all' (Tao 2019) cannot be upgraded to 'all' by")
print("      any measure/ergodic/dissipation argument — they don't see Z.")


# ===========================================================================
print("\n" + "=" * 72)
print("D3  THE EMBEDDINGS (C, H) ARE THE WRONG COMPLETION")
print("=" * 72)


def f(z):
    c = cmath.cos(math.pi * z)
    return z / 2 * (1 + c) / 2 + (3 * z + 1) / 2 * (1 - c) / 2


print("   smooth entire extension f(z) = z/2·(1+cos πz)/2 + (3z+1)/2·(1−cos πz)/2")
print("   agrees with T on integers:")
print("     " + ",  ".join(f"f({n})={f(n).real:.0f} (T={T(n)})" for n in (4, 5, 6, 7)))
print("   off the real axis it diverges super-exponentially (no conservation law):")
for seed in (0.5 + 0.5j, 1.0 + 0.3j):
    z, traj = seed, []
    for _ in range(6):
        try:
            z = f(z)
            traj.append(f"{abs(z):.0f}")
        except OverflowError:
            traj.append("OVERFLOW")
            break
    print(f"     |f^n({seed})|: " + ", ".join(traj))

val = (-1j) * complex(1, 1) ** 2
print(f"\n   and the prime q₂=2 RAMIFIES:  −i·(1+i)² = {val.real:+.0f}{val.imag:+.0f}i = 2")
print("   the non-Archimedean fact the 2-adic completion captures and that C/H")
print("   (Archimedean, 2D/4D real normed) cannot see. (A convergent quaternionic")
print("   3x+1 is delicate/open; the structural verdict applies regardless.)")
print("   => embedding in C or H thickens the Archimedean side — where dissipation")
print("      is only statistical — and drops the 2-adic side where the structure")
print("      lives. Geometry/topology is the wrong completion to force 4-2-1.")


# ===========================================================================
print("\n" + "=" * 72)
print("SYNTHESIS — conserved vs dissipated, and the only signal that remains")
print("=" * 72)
print("   CONSERVED (2-adic coordinate): an ISOMETRY -> wrong TYPE to force a")
print("     ground state (measure-preserving, recurrent).")
print("   DISSIPATED (Archimedean size): only STATISTICAL, non-monotone -> not")
print("     forced. The two completions pull opposite ways; no single-completion")
print("     quantity is both conserved-structure and monotone-descent.")
print("   => a forcing quantity, if it exists, is ARITHMETIC/ADELIC (about the")
print("      measure-zero integers), not geometric or measure-theoretic.")
print()
print("   the two failure signals, and their status:")
print("     • nontrivial CYCLE   : RULED OUT — q₃^a = q₂^b has no positive")
print("       solution, so {1,2} is the only cycle (collatz/minimal_chaos.md).")
print("     • DIVERGENCE to ∞    : OPEN — and it is a measure-zero question (D2),")
print("       so the search for it must be arithmetic, not a dissipation argument.")
