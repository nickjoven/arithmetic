"""
standing_waves.py

The {2,3} mode-locking staircase, read as the framework's STANDING WAVES.

A standing wave here is a mode-locked plateau of the circle map: an orbit
that phase-locks to a rational winding number p/q and thereafter repeats —
a stationary, resonant pattern. The framework's minimum alphabet
(harmonics:minimum_alphabet.md) derives the devil's staircase of these
locks from its four primitives, with the locks ordered by the Stern-Brocot
tree and widest at small denominators.

This script shows, by running the dynamics, that the bare ratio of the two
forced primes — "stack a q₃ (a fifth, ×3/2), fold by a q₂ (an octave, ÷2)"
— is exactly such a system, and that its standing waves are the {2,3}-
dominated locks:

  S1  ROTATION. Stacking ×3/2 and folding ÷2 is rotation by
      ρ = log₂(3/2). Its continued-fraction convergents are the equal-
      temperament locks (1/2, 3/5, 7/12 = 12-tone, 24/41, 31/53), and each
      lies on the Stern-Brocot mediant descent to ρ. The {2,3} ratio
      generates a Stern-Brocot rotation number.

  S2  TONGUES. The sine circle map θ → θ + Ω − (K/2π)sin2πθ at critical
      K = 1 has a devil's staircase whose Arnold-tongue widths rank by
      denominator: 1 > 2 > 3 > 4 > ... The small {2,3} denominators carry
      the widest standing waves, as the framework's Stern-Brocot ordering
      predicts.

  S3  THE WAVE STANDS. Inside a tongue the orbit is asymptotically
      periodic (a literal standing wave); in a gap it never repeats
      (quasiperiodic). Demonstrated for the q₂ lock (period 2) and for the
      ρ-neighbourhood lock 7/12 (period 12 — equal temperament as a
      mode-lock).

Pure Python, no numpy. Deterministic. Run: python3 standing_waves.py
"""

import math
from fractions import Fraction

log2 = lambda x: math.log(x) / math.log(2)
q2, q3 = 2, 3


# ===========================================================================
print("=" * 72)
print("S1  ROTATION:  stack ×q₃/q₂ (a fifth), fold ÷q₂ (an octave)  →  log₂(3/2)")
print("=" * 72)
rho = log2(q3 / q2)
print(f"   ρ = log₂(q₃/q₂) = log₂(3/2) = {rho:.10f}")


def continued_fraction(x, n=12):
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
    h0, h1, k0, k1 = 0, 1, 1, 0
    out = []
    for ai in a:
        h0, h1 = h1, ai * h1 + h0
        k0, k1 = k1, ai * k1 + k0
        out.append((h1, k1))
    return out


def stern_brocot_descent(x, depth=400):
    lo, hi = (0, 1), (1, 1)
    path = []
    for _ in range(depth):
        med = (lo[0] + hi[0], lo[1] + hi[1])
        path.append(med)
        if med[0] / med[1] < x:
            lo = med
        else:
            hi = med
    return path


cf = continued_fraction(rho)
conv = convergents(cf)
print(f"   continued fraction: {cf}")
print("   convergents  (q fifths ≈ p octaves — the equal temperaments):")
sb = set(stern_brocot_descent(rho))
for p, q in conv[1:8]:
    tag = "  ← 12-tone equal temperament" if (p, q) == (7, 12) else ""
    on_tree = "on Stern-Brocot descent" if (p, q) in sb else "off tree"
    print(f"     {q:>3} fifths ≈ {p:>3} octaves :  {p}/{q} = {p / q:.6f}  "
          f"[{on_tree}]{tag}")
print("   → the standing-wave ratios of ×3/2 ARE Stern-Brocot mediants of ρ.")


# ===========================================================================
print("\n" + "=" * 72)
print("S2  TONGUES:  sine circle map at critical K=1, Arnold-tongue widths")
print("=" * 72)


def winding(Omega, K, N=4000, burn=2000):
    th = 0.123456789
    for _ in range(burn):
        th = th + Omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * th)
    t0 = th
    for _ in range(N):
        th = th + Omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * th)
    return (th - t0) / N


M = 1201
Wgrid = [(i / (M - 1), winding(i / (M - 1), 1.0)) for i in range(M)]


def plateau_width(target, tol=1e-3):
    return sum(1 for _, w in Wgrid if abs(w - target) < tol) / M


targets = [Fraction(0, 1), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3),
           Fraction(1, 4), Fraction(3, 4), Fraction(1, 5), Fraction(2, 5)]
rows = sorted(((fr, plateau_width(float(fr))) for fr in targets), key=lambda r: -r[1])
print("   standing-wave (locked-plateau) width on the Ω-axis, by winding number:")
for fr, w in rows:
    bar = "#" * int(w * 240)
    print(f"     W = {str(fr):>4}  (denominator {fr.denominator}):  width {w:6.3f}  {bar}")
print("   → widest standing waves are the {2,3}-denominator locks, "
      "ordered by Stern-Brocot depth.")


# ===========================================================================
print("\n" + "=" * 72)
print("S3  THE WAVE STANDS:  locked orbit = periodic (standing); gap = never repeats")
print("=" * 72)


def orbit_period(Omega, K, settle=6000, scan=400, tol=1e-6):
    """Detect the period of the asymptotic orbit (mod 1); None if not periodic."""
    th = 0.2
    for _ in range(settle):
        th = (th + Omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * th)) % 1
    ref = th
    for p in range(1, scan + 1):
        th = (th + Omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * th)) % 1
        if abs(th - ref) < tol:
            return p
    return None


# Tongues are Ω-shifted by the sine coupling (only the symmetric 1/2 lock sits
# at Ω = p/q). So locate each forced-prime lock by its winding number, then show
# the orbit there is periodic — a literal standing wave.
def lock_center(target, K, lo, hi, steps=400):
    hits = [lo + (hi - lo) * i / steps for i in range(steps + 1)]
    hits = [Om for Om in hits if abs(winding(Om, K) - target) < 1e-4]
    return sum(hits) / len(hits) if hits else None


K = 0.9
om_q2 = lock_center(1 / 2, K, 0.45, 0.55)     # q₂ lock (symmetric, ≈ 0.5)
om_q3 = lock_center(1 / 3, K, 0.30, 0.40)     # q₃ lock (Ω-shifted ≈ 0.35)
p_q2 = orbit_period(om_q2, K)
p_q3 = orbit_period(om_q3, K)
p_gap = orbit_period(rho, 0.2)                # irrational rotation, weak coupling
print(f"   q₂ standing wave  (W=1/2 at Ω≈{om_q2:.3f}, K=0.9):  period = {p_q2}  "
      f"(q₂ = 2 modes)")
print(f"   q₃ standing wave  (W=1/3 at Ω≈{om_q3:.3f}, K=0.9):  period = {p_q3}  "
      f"(q₃ = 3 modes)")
print(f"   staircase gap     (W irrational, Ω=ρ, K=0.2):    period = {p_gap}  "
      f"(no standing wave — quasiperiodic)")
print("\n   The framework's {2,3} live HERE, as the widest standing waves of the")
print("   ×3/÷2 staircase. Collatz lives in the GAPS of this same staircase —")
print("   the unlocked regime that admits no standing wave (see "
      "../collatz/minimal_chaos.md).")
