import math

for _ in range(int(input())):
    n = int(input())

    xs = []
    ys = []

    for i in range(2*n):
        x, y = map(int, input().split())
        ys.append(abs(y)) if x == 0 else xs.append(abs(x))

    xs.sort()
    ys.sort()

    total = 0.0

    for i in range(len(xs)):
        # total += ((xs[i] + ys[i]) * (xs[i] + ys[i]))**0.5
        total += math.hypot(xs[i], ys[i])

    print(total)
