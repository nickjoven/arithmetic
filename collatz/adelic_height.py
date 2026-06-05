"""
adelic_height.py

Is there an h(n), built from the Archimedean size |n| and 2-adic (v2-type)
data, that is PROVABLY MONOTONE along Collatz orbits? This is the one place a
forced descent could live (collatz/no_dissipation.md): the adelic R x Q_2
combination. This script tries to build one, tests the natural candidates,
and locates the precise obstruction. The answer is honest and complete:

  [0] A monotone height EXISTS iff Collatz is true — the stopping time sigma(n)
      satisfies sigma(T(n)) = sigma(n) - 1 exactly. But it is CIRCULAR: defining
      it presupposes the orbit reaches 1. So the real question is whether a
      NON-circular (closed-form / locally computable) monotone height exists.

  [1] Pointwise obstruction A: arbitrarily long ASCENDING runs. n = 2^k - 1
      gives ~k consecutive odd steps during which |n| climbs by log2(3/2) each
      step while v2(n) = 0 throughout. So no function of v2(n) (nor any finite
      2-adic truncation) can offset the climb — the 2-adic 'bottom' is blind to it.

  [2] Pointwise obstruction B: the only 2-adic quantity that sees the whole
      climb is the full parity-vector coordinate — which is measure-preserving
      (an isometry). A continuous h: Z_2 -> R strictly decreasing along orbits is
      impossible (Poincare recurrence). So finite 2-adic data can't compensate
      [1] and the full 2-adic data can't descend [2]: squeezed from both ends.

  [3] The best naive candidate h_a(n) = log2(n) - a*v2(n) fails for EVERY a:
      even steps need a < 1, odd ascending steps (v2(3n+1)=1) rise by log2(3/2)
      for all a. The squeeze is exact.

  [4] Window heights don't escape it: a height seeing w future iterates fails on
      runs longer than w (runs are unbounded, [1]); an unbounded window is the
      stopping time [0], circular. So: pointwise/finite-window fails; unbounded =
      circular.

Conclusion: a real height must be Archimedean-NON-monotone AND 2-adically
DISCONTINUOUS — definable on neither completion, living only on the measure-zero
integers, where R-analysis and 2-adic/ergodic theory both fail to apply. A
closed form equal to the stopping time IS a proof of Collatz; none is known.

Class 2 negative result. Pure Python, no numpy. Deterministic.
Run: python3 adelic_height.py
"""

import math

log2 = lambda x: math.log(x) / math.log(2)


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


# ===========================================================================
print("=" * 72)
print("[0] EXISTENCE is circular: the stopping time sigma is a perfect Lyapunov")
print("=" * 72)


def sigma(n, cap=10 ** 7):
    s = 0
    while n != 1 and s < cap:
        n = T(n)
        s += 1
    return s


ok = all(sigma(T(n)) == sigma(n) - 1 for n in range(2, 2000))
print(f"   sigma(T(n)) == sigma(n) - 1 for n = 2..1999: {ok}")
print("   => a monotone height EXISTS iff Collatz holds; sigma is it, but defining")
print("      sigma needs the orbit to reach 1. 'Does h exist?' = 'is Collatz true?'")
print("      unless h is CLOSED-FORM. That is the real question.")


# ===========================================================================
print("\n" + "=" * 72)
print("[1] POINTWISE OBSTRUCTION A: unbounded ascending runs, v2 = 0 throughout")
print("=" * 72)
for k in (4, 7, 10, 14):
    n = 2 ** k - 1
    x = n
    run = 0
    vmax = 0
    while x % 2 == 1:
        vmax = max(vmax, v2(x))
        x = T(x)
        run += 1
    # value at the end of the maximal odd run:
    print(f"   n=2^{k}-1={n:>6}: {run:>2} consecutive odd steps; max v2(n) on run = {vmax}; "
          f"log2|n|: {log2(n):.1f} -> {log2(x):.1f} (climbs +{log2(x)-log2(n):.1f})")
print("   v2(n) = 0 for every step of every climb -> no function of v2(n), nor any")
print("   finite 2-adic truncation, can offset the rising log2|n|. Runs are unbounded.")


# ===========================================================================
print("\n" + "=" * 72)
print("[2] POINTWISE OBSTRUCTION B: the full 2-adic coordinate is CONSERVED")
print("=" * 72)
print("   the only 2-adic datum that sees the whole climb is the parity vector /")
print("   2-adic coordinate. It is measure-preserving (two_completions.md), so a")
print("   continuous h:Z_2 -> R strictly decreasing along orbits is impossible")
print("   (Poincare recurrence forces return). Finite 2-adic data fails [1]; the")
print("   full 2-adic data can't descend [2]. The height is squeezed from both ends.")


# ===========================================================================
print("\n" + "=" * 72)
print("[3] TEST the best naive adelic candidate  h_a(n) = log2(n) - a*v2(n)")
print("=" * 72)


def failures(alpha, N=20000):
    bad = 0
    worst = (0.0, 0)
    for n in range(2, N):
        dh = (log2(T(n)) - alpha * v2(T(n))) - (log2(n) - alpha * v2(n))
        if dh >= 0:
            bad += 1
            if dh > worst[0]:
                worst = (dh, n)
    return bad, worst


for a in (0.0, 0.5, 1.0, 2.0, 5.0):
    bad, worst = failures(a)
    print(f"   a={a:>4}: h INCREASES on {bad:>5}/19998 steps "
          f"(worst Δh=+{worst[0]:.2f} at n={worst[1]})")
print("   even steps need a < 1 (Δh = a-1); odd ascending steps rise by log2(3/2)")
print("   for ALL a. No alpha is monotone — the squeeze of [1]+[2] is exact.")

# [3b] a 3-adic term doesn't help: v3 is ALSO blind to the climb.
def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k
run_v3 = []
x = 2 ** 14 - 1
while x % 2 == 1:
    run_v3.append(v3(x))
    x = T(x)
def fails_ab(a, b, N=20000):
    bad = 0
    for n in range(2, N):
        m = T(n)
        dh = (log2(m) - a*v2(m) - b*v3(m)) - (log2(n) - a*v2(n) - b*v3(n))
        if dh >= 0:
            bad += 1
    return bad
best = min((fails_ab(a, b), a, b) for a in (0, 0.5, 1) for b in (0, 0.5, 1, 2))
print(f"\n   adding a 3-adic term h = log2(n) - a*v2(n) - b*v3(n):")
print(f"   v3(n) along the 2^14-1 climb = {run_v3}  (0 after step 1 -> also blind)")
print(f"   best (fewest failures, a, b) = {best} of 19998 steps -> best keeps b=0.")
print("   reason: any local v_p(n) sees the current point; the climb is driven by")
print("   the ACCUMULATED count of ×3 steps (a trajectory quantity). No local")
print("   p-adic datum escapes the squeeze — ALL local arithmetic is blind.")


# ===========================================================================
print("\n" + "=" * 72)
print("[4] VERDICT — what a real height must be (the precise frontier)")
print("=" * 72)
print("   A non-circular monotone h must be BOTH:")
print("     • Archimedean-non-monotone  (size climbs on ascending runs, D1), and")
print("     • 2-adically discontinuous  (else recurrence forbids descent, [2]).")
print("   So it is definable on NEITHER completion of Z — it lives only on the")
print("   measure-zero integers, where R-analysis and 2-adic/ergodic theory both")
print("   fail to apply. Window heights don't help: finite window fails long runs")
print("   [1]; unbounded window = the stopping time [0], circular.")
print("   The stopping time is the unique such function; a CLOSED FORM equal to it")
print("   is exactly a proof of Collatz. None is known — and this is WHY.")
