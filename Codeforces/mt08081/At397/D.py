import math

N = int(input())

# Hmmpphh

# We need to find x^3 - y^3 = N
# Since N is not zero, x can be written as y+k
# (y+k)^3 - y^3 = N
# y^3 + 3ky^2 + 3k^2y + k^3 - y^3 = N
# 3ky^2 + 3k^2y + k^3
# k(3y^2 + 3ky + k^2) = N
# I guess we can solve the quadratic
# 3y^2 + 3ky + k^2 = N/k
# 3y^2 + 3ky + k^2 - N/k = 0
# Solve for quadratic using formula
# a = 3, b = 3k, c = k^2 - N/k
# Since y is an integer... the discriminant should be non-negative and should be a square (to avoid float)
# Disc = (3k^2) - 4*3 (k^2 - M)
# 9k^2 −12k^2 + 12M
# D = 3*(4M - K^2)
# y = (-3k + root(D))/6
# But wth... we don't have k
# I guess I can try going till root(N) for k
# If a y exists, then x is easy to find for that k, y

found = False

for k in range(1, math.isqrt(N)+2):
    if k * (k*k + 3*k + 3) > N:
        break
    # k must divide N so that the disc is not float
    if N % k != 0:
        continue
    M = N // k  # So that 3y^2 + 3k*y + k^2 = M

    # D = 3*(4M - k^2)
    D = 3 * (4*M - k**2)
    # Non-negative rejected
    if D < 0:
        continue
    # Check perfect square
    d = math.isqrt(D)
    if d*d != D:
        continue

    # d >= 3k so that y > 0 (-3k + d > 0)
    if d < 3 * k:
        continue
    # y = (d - 3k) / 6 must be an integer at least 1.
    if (d - 3 * k) % 6 != 0:
        continue

    y = (d - 3 * k) // 6
    # Adding a check but probably unnecessary
    if y <= 0:
        continue

    x = y + k
    
    if x**3 - y**3 == N:
        print(x, y)
        found = True
        break

if not found:
    print(-1)

