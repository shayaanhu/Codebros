n, w = map(int, input().split())

items = []
for _ in range(n):
    w_i, v_i = map(int, input().split())
    items.append((w_i, v_i))

dp = [0] * (w + 1)

# Knapsack problem
for w_i, v_i in items:
    for j in range(w, w_i - 1, -1):
        dp[j] = max(dp[j], dp[j - w_i] + v_i)

print(dp[w])