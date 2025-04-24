n, k = map(int, input().split())
h = list(map(int, input().split()))

# This is similar to the other problem

# We can try all possible jumps from i-k to i-1
# And take the minimum of all of them

# We can have max n potential jumps
# Hence we can store 10**10 inside as thats larger than N
dp = [10**10] * n
dp[0] = 0

for i in range(1, n):
    best = dp[i]
    for j in range(max(0, i-k), i):
        cost = dp[j] + abs(h[i] - h[j])
        best = min(best, cost)
    dp[i] = best

print(dp[n-1])
