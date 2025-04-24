n, x = map(int, input().split())
c = list(map(int, input().split()))

mod = 10**9 + 7

# x is the desired sum so we would probably have to access dp[x]

# For each desired sum, we might have to iterate over all coins
# However, the time limit is only 1 sec
# Lets try it anyways

dp = [0] * (x + 1)
dp[0] = 1

for s in range(x+1):
    v = dp[s]
    if not v:
        continue
    for coin in c:
        # If v is 0, we can skip this value idk
        if s + coin > x:
            continue
        else:
            dp[s + coin] = (dp[s + coin] + v) % mod


print(dp[x])