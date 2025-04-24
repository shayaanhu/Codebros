n = int(input())

dp = [10**9] * (n + 1)
dp[0] = 0

# Using strings might be costly so we can try to simulate taking digits out
# Through modulus and division

for i in range(1, n + 1):
    x = i
    while x:
        digit = x % 10
        x //= 10
        dp[i] = min(dp[i], dp[i - digit] + 1)

print(dp[n])