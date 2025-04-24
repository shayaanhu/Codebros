mod = 10**9 + 7

n = int(input())

grid = []
for i in range(n):
    grid.append(input())

# we can dp to store number of paths to cell (i, j)
dp = []
for i in range(n):
    dp.append([0] * n)

# If the first cell is blocked, there are no paths
if grid[0][0] == '.':
    dp[0][0] = 1
else:
    dp[0][0] = 0

# Traverse the grid and fill the dp table
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            continue

        # Add the cell to the right for i > 0 and up for j > 0
        # * has a count of 0 so it should not effect the sum
        if i > 0:
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % mod
        if j > 0:
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % mod

print(dp[n-1][n-1])