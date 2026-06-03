"""
equidistribution.py

The Farey / Stern-Brocot tree has two faces, and the three problems this
repo studies sit on different ones:

  LOCKED face  (finite-depth COUNTING).  |F_n| = 1 + Σ_{k≤n} φ(k) is an exact,
    local, finite-depth count -- the number of mode-lock centres up to
    denominator n. The framework's structural quantities live here:
    Ω_Λ = |F₆|/|F₇| = 13/19 is a depth-6 count (a standing-wave census).

  UNLOCKED face  (asymptotic EQUIDISTRIBUTION).  As n → ∞, how uniformly do
    the Farey fractions fill [0,1]? This is the depth→∞ continuum limit
    (minimum_alphabet.md Part III, "completion of Q"), and it is where the
    RIEMANN HYPOTHESIS lives, via:

      Franel (1924) / Landau:  RH  ⇔  the Farey fractions are
      equidistributed to the maximal degree, i.e. with
        δ_ν = ρ_ν − ν/N   (ν-th Farey fraction minus its uniform position),
        S1(n) = Σ_ν |δ_ν| = O(n^{1/2+ε})      [Landau form]
        S2(n) = Σ_ν δ_ν²  = O(n^{-1+ε})        [Franel form]

This script computes both faces. The register that organizes the repo —
LOCKED (mode-locked standing waves) vs UNLOCKED (the gaps / equidistributed
complement) — places RH on the unlocked side, the same side as Collatz:

  - standing waves (mode_locking/) : LOCKED   — the {2,3} resonances
  - Collatz       (collatz/)       : UNLOCKED — dynamical (no standing wave)
  - Riemann       (this study)     : UNLOCKED — asymptotic (equidistribution)

Class 2: this records where the framework's finite-depth Farey machinery
meets, and where it does NOT meet, the asymptotic statement RH. It does NOT
test RH (finite data is only ever consistent with it) and adds no constant.

Pure Python, no numpy. Deterministic. Run: python3 equidistribution.py
"""

import math


def totient(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def farey_count(n):
    """|F_n| = 1 + Σ_{k=1}^n φ(k)  — the locked, finite-depth census."""
    return 1 + sum(totient(k) for k in range(1, n + 1))


def farey_sequence(n):
    """F_n as (a,b) pairs in order, via the neighbour recurrence (no floats)."""
    a, b, c, d = 0, 1, 1, n
    out = [(0, 1)]
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        out.append((a, b))
    return out


# ===========================================================================
print("=" * 72)
print("LOCKED FACE — finite-depth COUNTS (the framework reads these)")
print("=" * 72)
print(f"   |F₆| = {farey_count(6)}   |F₇| = {farey_count(7)}")
print(f"   Ω_Λ = |F₆|/|F₇| = 13/19 = {13/19:.6f}   (an exact depth-6 census)")
print("   the 13/19 ratio is DEPTH-SPECIFIC, not an asymptotic invariant:")
for n in (6, 20, 100, 400):
    print(f"      n={n:>3}:  |F_n|/|F_(n+1)| = {farey_count(n)/farey_count(n+1):.5f}"
          + ("   ← the framework's operating depth" if n == 6 else
             "   → 1 as n→∞"))
print("   So the locked face is a finite-depth count; it carries the framework's")
print("   structural quantity but says nothing about the n→∞ limit.")


# ===========================================================================
print("\n" + "=" * 72)
print("UNLOCKED FACE — asymptotic EQUIDISTRIBUTION (Franel–Landau; RH lives here)")
print("=" * 72)
print("   δ_ν = ρ_ν − ν/N ;   S1 = Σ|δ_ν| ,  S2 = Σδ_ν²")
print(f"   {'n':>4} {'|F_n|':>7} {'S1=Σ|δ|':>10} {'S1/√n':>8} "
      f"{'S2=Σδ²':>11} {'S2·n':>8}")
for n in (8, 16, 32, 64, 128, 256, 512):
    seq = [a / b for a, b in farey_sequence(n)]
    N = len(seq) - 1
    delta = [seq[v] - v / N for v in range(len(seq))]
    S1 = sum(abs(x) for x in delta)
    S2 = sum(x * x for x in delta)
    print(f"   {n:>4} {len(seq):>7} {S1:>10.4f} {S1/math.sqrt(n):>8.4f} "
          f"{S2:>11.6f} {S2*n:>8.4f}")
print("   RH ⇔  S1 = O(n^{1/2+ε})  [Landau]   and   S2 = O(n^{-1+ε})  [Franel].")
print("   Read: S1/√n stays bounded and S2·n stays bounded — CONSISTENT with RH.")
print("   This is consistency, NOT a test: every finite n is consistent with both")
print("   RH and its negation; the theorem is about the n→∞ rate.")


# ===========================================================================
print("\n" + "=" * 72)
print("THE TWO FACES — where the framework reaches, and where it cannot")
print("=" * 72)
print("   LOCKED   (finite depth, counting):  framework forces depth-6 structure")
print("            (|F₆|=13, Ω_Λ=13/19). Exact, local, a standing-wave census.")
print("   UNLOCKED (depth→∞, equidistribution):  RH = the Farey fractions fill")
print("            the continuum as uniformly as possible. A completion-limit")
print("            statement (minimum_alphabet.md Part III).")
print()
print("   The framework's machinery is constitutionally FINITE-DEPTH: it counts")
print("   modes at the forced depth and reads ratios off them. RH is a property")
print("   of the depth→∞ completion. Same tree, different faces — the framework")
print("   shares the Farey TREE with RH but reads only its locked, counted face.")
print()
print("   On the unlocked side it keeps company with Collatz:")
print("     Collatz — UNLOCKED dynamical : no orbit locks onto a standing wave")
print("               (Terras full shift; collatz/minimal_chaos.md)")
print("     Riemann — UNLOCKED asymptotic : the fractions equidistribute maximally")
print("               (Franel–Landau; this study)")
print("   Both are statements about the gaps / the completion — exactly the part")
print("   the framework's finite-depth counting does not reach.")
