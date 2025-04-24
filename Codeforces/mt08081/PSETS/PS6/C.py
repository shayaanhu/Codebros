n, x = map(int, input().split())
c = list(map(int, input().split()))

# This seems like a classic DM problem


# We initialize everything with any number greater than x
# So that if some value is that number then we print -1
dp = [2*x] * (x + 1)
# 0 can be formed with 0 coins
dp[0] = 0

# Now we can try to build up the dp array by going coin by coin

for coin in c:
    for s in range(coin, x + 1):
        # We can try to take the coin or not take it
        # If we take it, we add 1 to the previous value
        dp[s] = min(dp[s], dp[s - coin] + 1)


print(dp[x] if dp[x] != 2*x else -1)

