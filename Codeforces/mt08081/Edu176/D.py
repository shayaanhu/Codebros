# for _ in range(int(input())):
#     x, y = map(int, input().split())

#     if x == y:
#         print(0)
#         continue


# Precompute minimal cost for every total shift T (T = Lx + Ly) up to 120.
MAX_T = 120
INF = 10**30
dp = [INF] * (MAX_T + 1)
dp[0] = 0
# For each possible k (each allowed operation, used at most once),
# update dp[t] = minimum cost (sum of 2^k for the chosen operations) to achieve total shift t.
for k in range(1, MAX_T + 1):
    cost_k = 2 ** k
    for t in range(MAX_T, k - 1, -1):
        dp[t] = min(dp[t], dp[t - k] + cost_k)

# print(dp)

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    # If the numbers are already equal, no operations (cost 0) are needed.
    if x == y:
        print(0)
        continue

    ans = INF
    # Try all possible splits of operations: 
    # Lx operations on x and Ly operations on y (each represented as total shift)
    # Since dividing by 2^L is equivalent to right shifting by L bits,
    # we test Lx and Ly in the range [0, 60] (enough for numbers up to 10^17).
    for Lx in range(61):
        for Ly in range(61):
            if (x >> Lx) == (y >> Ly):
                total_shift = Lx + Ly
                ans = min(ans, dp[total_shift])
    print(ans)
