n = int(input())

a = []

for i in range(n):
    a.append(tuple(map(int, input().split())))

# print(a)

dp0, dp1, dp2 = a[0]

for i in range(1, n):
    ai, bi, ci = a[i]

    # If we choose A, then the others must be yesterday
    val1 = ai + max(dp1, dp2)
    # We can do the same for B and C
    val2 = bi + max(dp0, dp2)
    val3 = ci + max(dp0, dp1)
    dp0, dp1, dp2 = val1, val2, val3

# Max happiness can be on any of the dps

print(max(dp0, dp1, dp2))