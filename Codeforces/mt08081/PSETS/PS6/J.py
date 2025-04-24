n, w = map(int, input().split())

# Also a knapsack problem

items = []
total_value = 0
for _ in range(n):
    w_i, v_i = map(int, input().split())
    items.append((w_i, v_i))
    total_value += v_i

dp = [w + 1] * (total_value + 1)
dp[0] = 0

for w_i, v_i in items:
    for v in range(total_value, v_i - 1, -1):
        cv = dp[v - v_i] + w_i
        if cv < dp[v]:
            dp[v] = cv

ans = 0
for v in range(total_value + 1):
    if dp[v] <= w:
        ans = v

print(ans)